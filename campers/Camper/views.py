from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from Camper.forms import CamperForm
from Camper.models import Camper, Dorm, Band

MAX_BANDS = 8
MAX_DORMS = 6
MAX_GENDER_IN_BAND = 3
MAX_GENDER_IN_DORM = 3


def add_camper_in_dorm(camper, dorm):
    if camper.age in [13, 14]:
        if dorm.gender == camper.gender and dorm.young_count < 2:
            dorm.camper.add(camper)
            dorm.young_count += 1
            dorm.save()
            return True
    elif camper.age in [15, 16]:
        if dorm.gender == camper.gender and dorm.middle_count < 2:
            dorm.camper.add(camper)
            dorm.middle_count += 1
            dorm.save()
            return True
    elif camper.age in [17, 18]:
        if dorm.gender == camper.gender and dorm.old_count < 2:
            dorm.camper.add(camper)
            dorm.old_count += 1
            dorm.save()
            return True
    return False


def camper_add(request):
    form = CamperForm()
    if request.POST:
        form = CamperForm(request.POST)
        if form.is_valid():
            camper = form.save()
            dorms = Dorm.objects.all()
            camper_added = False
            for dorm in dorms:
                if add_camper_in_dorm(camper, dorm):
                    camper_added = True
                    break
            if (not camper_added) and dorms.count() < MAX_DORMS:
                dorm_name = '%s-%s' % ('Dorm', str(dorms.count()))
                if Dorm.objects.filter(gender='M').count() < MAX_GENDER_IN_DORM:
                    new_dorm = Dorm.objects.create(name=dorm_name, gender='M')
                    if add_camper_in_dorm(camper, new_dorm):
                        camper_added = True
                if Dorm.objects.filter(gender='M').count() < MAX_GENDER_IN_DORM and not camper_added:
                    new_dorm = Dorm.objects.create(name=dorm_name, gender='F')
                    add_camper_in_dorm(camper, new_dorm)

            added = False
            for band in Band.objects.all():
                if not band.camper.filter(category=camper.category) and band.camper.filter(
                        gender=camper.gender).count() < MAX_GENDER_IN_BAND:
                    band.camper.add(camper)
                    if camper.gender == 'M':
                        band.boys_count += 1
                    else:
                        band.girls_count += 1

                    band.save()
                    added = True
                    break

            if not added and Band.objects.all().count() < MAX_BANDS:
                name = '%s-%s' % ('band', str(Band.objects.all().count()))
                band = Band.objects.create(name=name)
                band.camper.add(camper)
                if camper.gender == 'M':
                    band.boys_count += 1
                else:
                    band.girls_count += 1
                band.save()

            return redirect(reverse('dorms'))

    form = CamperForm()
    return render(request, 'inputCamper.html', {'form': form})


def test(request):
    campers = Camper.objects.all()
    return render(request, 'test.html', {'campers_list': campers})


def show_list(request):
    campers = Camper.objects.all.filter(age=12)
    return render(request, 'camper_list.html', {'campers_list': campers})


def bands(request):
    data_camper_list = {}
    band_list = []
    for band in Band.objects.all():
        band_list.append(band)
        for camper in band.camper.all():
            if camper.category in data_camper_list.keys():
                data_camper_list[camper.category].append(camper)
            else:
                data_camper_list[camper.category] = [camper]

    return render(request, 'bands.html', {'bands_list': data_camper_list, 'bands': band_list})


def dorm_list(request):
    dorms = Dorm.objects.all()
    return render(request, 'dorms.html', {'dorms': dorms})

import numpy
import applicant

def test():
    DormM1 = []
    DormM2 = []
    DormM3 = []
    DormF1 = []
    DormF2 = []
    DormF3 = []
    for applicant in applicant_list:
        if applicant.gender == "M":
            assign = dorm_assign(DormM1,DormM2,DormM3,applicant.age)
            if assign == 1 :
                applicant.dorm = 1
                DormM1.append(applicant.age)
            elif assign == 2:
                applicant.dorm = 2
                DormM2.append(applicant.age)
            else:
                applicant.dorm = 3
                DormM3.append(applicant.age)
        else:
            assign = dorm_assign(DormF1,DormF2,DormF3,applicant.age)
            if assign == 1 :
                applicant.dorm = 1
                Dorm4.append(applicant.age)
            elif assign == 2:
                applicant.dorm = 2
                Dorm5.append(applicant.age)
            else:
                applicant.dorm = 3
                Dorm6.append(applicant.age)

def isFull(dorm):
    if (len(dorm) == 8):
        return True
    else:
        return False
def avg(data_List):
    if len(data_List) == 0:
        return 0
    else:
        return sum(data_List)/len(data_List)

def dorm_assign(Dorm1,Dorm2,Dorm3,age):
    Dorm_Status = [isFull(Dorm1),isFull(Dorm2),isFull(Dorm3)]
    if Dorm_Status == [False,False,False]:
        check_list = [ abs(avg(Dorm1)-age),abs(avg(Dorm2)-age),abs(avg(Dorm3)-age)]
        if max(check_list) == abs(avg1-age):
            return 1
        elif max(check_list) == abs(avg2-age):
            return 2
        else:
            return 3
    elif Dorm_Status == [True,False,False]:
        if abs(avg(Dorm2)-age) > abs(avg(Dorm3)-age):
            return 2
        else: 
            return 3
    elif Dorm_Status == [False,True,False]:
        if abs(avg(Dorm1)-age) > abs(avg(Dorm3)-age):
            return 1
        else: 
            return 3
    elif Dorm_Status == [False,False,True]:
        if abs(avg(Dorm1)-age) > abs(avg(Dorm2)-age):
            return 1
        else: 
            return 2
    elif Dorm_Status == [False,True,True]:
        return 1
    elif Dorm_Status == [True,False,True]:
        return 2
    elif Dorm_Status == [True,True,False]:
        return 3

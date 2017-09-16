import wx

class test(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Title_Test',size=(800,600))
		panel = wx.Panel(self)

	# ListBox
		Test_List = ['Item1','Item2','Item3']
		container = wx.ListBox(panel,-1,(50,50),(200,300),Test_List,wx.LB_SINGLE) # Parent,ID,pos,size,List,Style
		container.SetSelection(3) # Set Default

	# CheckBox
		wx.CheckBox(panel,-1,"Check1",(20,20),(160,-1)) #(Parent,ID,Title,pos,size)
		wx.CheckBox(panel,-1,"Check2",(20,20),(160,-1)) #(Parent,ID,Title,pos,size)
		wx.CheckBox(panel,-1,"Check3",(20,20),(160,-1)) #(Parent,ID,Title,pos,size)
    # Spinner
		spinner = wx.SpinCtrl(panel,-1,"",(40,40),(90,-1)) #(Parent,ID,empty string, pos,size)
		spinner.SetRange(1,100)
		spinner.SetValue(50) # Set Default

	# Slider
		slider = wx.Slider(panel,-1,50,1,100,pos=(10,10),size=(250,-1),style=wx.SL_AUTOTICKS | wx.SL_LABELS) #(Parent,ID,default,min,max,)
		slider.SetTickFreq(5,1) # marks
"""	# Image
		pic = wx.Image("Pic.bmp",wx.BITMAP_TYPE_BMP).ConvertToBitmap()
		self.button = wx.BitmapButton(panel,-1,pic,pos=(20,20))
		self.button.SetDefault()
"""
	# Text label
		wx.StaticText(panel,-1,"check",(200,400)) #(Parent,ID,Inner Text, pos,size,sytle)
		custom = wx.StaticText(Panel,-1,"ColorTest",(10,10),(260,-1),wx.ALIGN_CENTER)
		custom.SetForegroundColour('white')
		custom.SetBackgroundColour('Blue')
	
	# Single Choice box
		InputBox = wx.SingleChoiceDialog(None,'Question','Title',['1','2','3']) #(Parent,Question,Title,List of options)
		if InputBox.ShowModal() == wx.ID_OK:
			checkResult = InputBox.GetStringSelection() # Store selection
	
	# Text Box	
		txtBox = wx.TextEntryDialog(None, "Hello", "Title","default") #(Parent, Popping text,Title, default txt)
		# Store content if ok is being clicked
		if txtBox.ShowModal() == wx.ID_OK: #ShowModal -> Value of choice
			txtCotent = txtBox.GetValue()
		
	# Msg box	
		box = wx.MessageDialog(None,'Test_Msg','MsgTitle',wx.YES_NO) #(Parent,Msg,Msg_Title,box style) wx.OK -> OK box
		answer = box.ShowModal() #Store the answer
		box.Destroy()
	
	# Menu Bar	
		status = self.CreateStatusBar() # Status bar as footer
		menubar = wx.MenuBar()
		first = wx.Menu()
		second = wx.Menu()
		first.Append(wx.NewId(),"FirstTest","Test One") #(ID,Item name, Status txt)
		first.Append(wx.NewId(),"FirstTest-1","Test One-1")
		second.Append(wx.NewId(),"SecondTest","Test Two")
		menubar.Append(first,"111") # Item Category
		menubar.Append(second,"222")
		self.SetMenuBar(menubar)

    # Button and event
		button = wx.Button(panel,label = "Go",pos=(500,400),size=(100,60)) #(Parent,BtnTxt,Pos,Size)
		self.Bind(wx.EVT_BUTTON, self.closebutton, button) #(Bing with event, trigger which function, binded object)
		self.Bind(wx.EVT_CLOSE, self.closewindow)
	
	def closebutton(self,event):
		self.Close(True)
	def closewindow(self,event):
		self.Destroy()

if __name__ =='__main__':
	app = wx.App()
	frame = test(parent=None,id = -1)
	frame.Show()
	app.MainLoop()
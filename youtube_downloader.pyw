from Tkinter import Tk,Label,Button,Entry,Text,Frame,SUNKEN,X,FALSE
import os
import ctypes
import bar
from progress.bar import Bar

class mygui:

        
    def __init__(self,master):

        self.trans(master)
        
        
        
    def trans(self,master):
        global E2

        self.master=master

        #separator = Frame(height=255, bd=25, relief=SUNKEN)
        master.title("gui")
        self.Label=Label(master,text="Youtube_downloader")
        #separator.pack(fill=X, padx=5, pady=5)
        
        master.title("gui")
        self.Label=Label(master,text="Youtube_downloader")
        self.Label.pack()
        self.greet_button=Button(master,text="download",command=self.greet)
        self.greet_button.pack()
        
        self.Label=Label(master,text="download")
        self.E2= Entry(root,width=50)
        self.E2.pack()
        
        

        
    def greet(self):
        bar = Bar('Processing', max=100)
        for i in range(1):
          try:
              if not self.E2.get():
                  ctypes.windll.user32.MessageBoxA(0, "Provide link", "Final", 1)
                  root.destroy()  
              else:    

                  
                  os.system("youtube-dl "+ self.E2.get())
                  ctypes.windll.user32.MessageBoxA(0, "Download_complete", "Final", 1)
                  root.destroy()
            #print "Unexpected error:", sys.exc_info()[0]
              bar.next()
          except:
              ctypes.windll.user32.MessageBoxA(0, "Download_complete", "Final", 1)

              print "Unexpected error:", sys.exc_info()[0]
        
        bar.finish()    
root=Tk()
root.resizable(width=FALSE, height=FALSE)
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
my_gui=mygui(root)
root.mainloop()


        

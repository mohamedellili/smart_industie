import pyrebase
import time
import os
import subprocess
import config as c

firebase = pyrebase.initialize_app(c.config)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(c.mail,c.password)

# Get a reference to the database service
db = firebase.database()
#-------------------------------------------------------------
global procGetConfiguration
global procRFID
global procKeypad
global procRegulation
global procCapteurs
global procEtatSwitches
global procLampes
global procControle
global procEtatLampe



def ActivationSystemeToltal():
	global procGetConfiguration
	global procRFID
	global procKeypad
	global procRegulation
	global procCapteurs
	global procEtatSwitches
	global procLampes
	global procControle
	global procEtatLampe
	procGetConfiguration = subprocess.Popen(["python3","GetConfiguration.py"])
	procRFID = subprocess.Popen(["python","ReadRFID.py"])
	procKeypad = subprocess.Popen(["python3","keypadLCD.py"])
	procRegulation = subprocess.Popen(["python3","Regulation.py"])
	procCapteurs = subprocess.Popen(["python3","capteurs/capteurs.py"])
	procEtatSwitches = subprocess.Popen(["python3","capteurs/EtatSwitches.py"])
	procLampes = subprocess.Popen(["python3","controle/lampe.py"])
	procControle = subprocess.Popen(["python3","controle/controle.py"])
	procEtatLampe =subprocess.Popen(["python3","updateEtatLampe.py"])

def DesactivationSystemeToltal():
	global procGetConfiguration
	global procRFID
	global procKeypad
	global procRegulation
	global procCapteurs
	global procEtatSwitches
	global procLampes
	global procControle
	global procEtatLampe
	procGetConfiguration.kill()
	procRFID.kill()
	procKeypad.kill()
	procRegulation.kill()
	procCapteurs.kill()
	procEtatSwitches.kill()
	procLampes.kill()
	procControle.kill()
	procEtatLampe.kill()

#	os.system("sudo kill "+str(procGetConfiguration.pid))
#	os.system("sudo kill "+str(procRFID.pid))
#	os.system("sudo kill "+str(procKeypad.pid))
#
#	os.system("sudo kill "+str(procRegulation.pid))
#	os.system("sudo kill "+str(procCapteurs.pid))
#	os.system("sudo kill "+str(procEtatLmapes.pid))
#	os.system("sudo kill "+str(procLampes.pid))
#	os.system("sudo kill "+str(procControle.pid))



#ActivationSystemeToltal()
#time.sleep(0.5)
#DesactivationSystemeToltal()



def stream_handler_Activation_Systeme_Totale(message):
        SystemeTotal(bool(int(message['data'])))
my_stream = db.child("Activation_Systeme/Activation_Systeme_Total").stream(stream_handler_Activation_Systeme_Totale)



def SystemeTotal(boolVar):
        if boolVar :
                print ("Activation Systeme_Total")
                ActivationSystemeToltal()
        else :
                try :
                        print ("Desactivation Systeme_Total")
                        DesactivationSystemeToltal()
                except :
                        pass




import tkinter as tk
import RPi.GPIO as GPIO
import time
import tkinter.font

GPIO21=21
GPIO20=20
GPIO16=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO21, GPIO.OUT)
GPIO.setup(GPIO20, GPIO.OUT)
GPIO.setup(GPIO16, GPIO.OUT)

master = tk.Tk()
master.title("GPIO Control")
master.geometry("600x400")



GPIO21_state = True
GPIO20_State = True
GPIO16_sTate = True

def blueButton():
	global GPIO21_state
	if GPIO21_state == True:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = False
		ONlabel = tk.Label(master, text="Turned ON", fg="green")
		ONlabel.grid(row=0, column=1)
	else:
		GPIO.output(GPIO21, GPIO21_state)
		GPIO21_state = True
		ONlabel = tk.Label(master, text="Turned OFF", fg ="red")
		ONlabel.grid(row=0, column =1)

def redButton():
        global GPIO20_State
        if GPIO20_State == True:
                GPIO.output(GPIO20, GPIO20_State)
                GPIO20_State = False
                OFFlabel = tk.Label(master, text="Turned ON", fg="green")
                OFFlabel.grid(row=1, column=1)
        else:
                GPIO.output(GPIO20, GPIO20_State)
                GPIO20_State = True
                OFFlabel = tk.Label(master, text="Turned OFF", fg ="red")
                OFFlabel.grid(row=1, column =1)

def yellowButton():
        global GPIO16_sTate
        if GPIO16_sTate == True:
                GPIO.output(GPIO16, GPIO16_sTate)
                GPIO16_sTate = False
                Ylabel = tk.Label(master, text="Turned ON", fg="green")
                Ylabel.grid(row=2, column=1)
        else:
                GPIO.output(GPIO16, GPIO16_sTate)
                GPIO16_sTate = True
                Ylabel = tk.Label(master, text="Turned OFF", fg ="red")
                Ylabel.grid(row=2, column =1)



def partyButton():
        t_end = time.time() + 10
        while time.time() < t_end:
                GPIO.output(GPIO16, False)
                GPIO.output(GPIO21,True)
                time.sleep(0.5)
                GPIO.output(GPIO16, True)
                GPIO.output(GPIO21,False)
                time.sleep(0.5)
                GPIO.output(GPIO20,False)
                time.sleep(0.5)
                GPIO.output(GPIO20, True)
                time.sleep(0.5)



def restartButton():

        GPIO.output(GPIO16, False)
        GPIO.output(GPIO21, False)
        GPIO.output(GPIO20, False)




myFont = tk.font.Font(family = "Helvetica", size = 20, weight = "bold")

ONbutton = tk.Button(master, text="BLUE led", font = myFont, bg="blue", command= blueButton)
ONbutton.grid(row=0, column=0)

OFFbutton = tk.Button(master, text="RED led", font = myFont, bg = "red", command=redButton)
OFFbutton.grid(row=1, column=0)

Ybutton = tk.Button(master, text="YELLOW led", font = myFont, bg = "yellow", command=yellowButton)
Ybutton.grid(row=2, column=0)

partyButton = tk.Button(master, text="PARTY", font = myFont, bg = "pink", command=partyButton)
partyButton.grid(row=3, column=0)

restartButton = tk.Button(master, text="RESTART", font = myFont, bg = "white", command=restartButton)
restartButton.grid(row=4, column=0)

Exitbutton = tk.Button(master, text="EXIT", font = myFont, bg="grey", command=master.destroy)
Exitbutton.grid(row=6, column=0)

master.mainloop()

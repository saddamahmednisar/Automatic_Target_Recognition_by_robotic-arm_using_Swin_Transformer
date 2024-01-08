import serial
import time
import tkinter as tk
from tkinter import ttk

root = tk.Tk
root = tk.Tk()
root.geometry('500x400')
root.title('robotic welding arm')
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=3)
# slider current value
current_value = tk.DoubleVar()


my_arduino = serial.Serial('COM10', 9600)
while 1:
    b = input("enter d if you  drop a thing and p if you pick up the thing: ")
    if (b == 'd'):
    # my_arduino.write()
        print("Thing droped")



    #channel = str('0:')
        time.sleep(1)
        channel = str('0:')
        value_label3='30'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(2)
        print('wrist aligend')

        channel = str('4:')
        value_label3 = '180'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('based')



        channel = str('2:')
        value_label3 = '100'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Elbow aligned')

        #channel = str('3:')
        #value_label3 = '30'
        #final_value1 = channel + value_label3
        #my_ascii = final_value1.encode('ascii')
        #my_arduino.write(my_ascii)
        #print(my_ascii)
        #time.sleep(3)
        #print('shoulder')



        channel = str('1:')
        value_label3 = '100'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Jaw aligned')

    elif (b == 'p'):
        #my_arduino.write()
        print("Thing picked")

        channel = str('1:')
        value_label3 = '80'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Jaw opened ')
        time.sleep(1)

        channel = str('0:')
        value_label3 = '30'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(2)
        print('wrist aligend')



        channel = str('4:')
        value_label3 = '40'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('based')



        channel = str('2:')
        value_label3 = '170'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Elbow aligned')

        channel = str('1:')
        value_label3 = '150'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Jaw closed ')

        channel = str('2:')
        value_label3 = '30'
        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
        time.sleep(3)
        print('Elbow aligned')


        #channel = str('3:')
        #value_label3 = '30'
        #final_value1 = channel + value_label3
        #my_ascii = final_value1.encode('ascii')
        #my_arduino.write(my_ascii)
        #print(my_ascii)
        #time.sleep(3)
        #print('shoulder')


        #channel = str('1:')
        #value_label3 = '155'
        #final_value1 = channel + value_label3
        #my_ascii = final_value1.encode('ascii')
        #my_arduino.write(my_ascii)
        #print(my_ascii)
        #time.sleep(3)
        #print('Jaw opend  ')

        # channel = str('4:')
        # value_label3 = '180'
        # final_value1 = channel + value_label3
        # my_ascii = final_value1.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)
        # time.sleep(3)
        # print('based')

        #channel = str('1:')
        #value_label3 = '125'
        #final_value1 = channel + value_label3
        #my_ascii = final_value1.encode('ascii')
        #my_arduino.write(my_ascii)
        #print(my_ascii)
        #time.sleep(3)
        #print('Jaw aligned')
    elif (b == 'e'):
        #my_arduino.write()
        print("exiting program")
        #
        #time.sleep(1)
        break
#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)
'''
def get_current_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(current_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def wrist_changed(event):
    value_label.configure(text=get_current_value())
    value_label2=(get_current_value())
    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label2 == '10'):
        channel = str('0:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value = channel + value_label2
        my_ascii = final_value.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label2 == '15'):
        value_label2 = str('0:')
        my_ascii = value_label2.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label2 == '59'):
        value_label2 = str('0:')
        my_ascii = value_label2.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('0:')
            final_value = channel + value_label2
            my_ascii = final_value.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


# label for the slider
wrist_label = ttk.Label(
    root,
    text='wrist:'
)

wrist_label.grid(
    column=0,
    row=0,
    sticky='w'
)

#  slider
wrist = ttk.Scale(
    root,
    from_=1,
    to=18,
    orient='horizontal',  # vertical
    command=wrist_changed,
    variable=current_value
)

wrist.grid(
    column=1,
    row=0,
    sticky='w'
)

# current value label
current_value_label = ttk.Label(
    root,
    text=''
)

current_value_label.grid(
    row=0,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    root,
    text=get_current_value()
)
value_label.grid(
    row=0,
    columnspan=2,
    sticky='n'
)
##2nd slider
# slider current value
slider2_value = tk.DoubleVar()


#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)

def get_slider2_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(slider2_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def jaw_changed(event):
    value_label1.configure(text=get_slider2_value())
    value_label3=(get_slider2_value())

    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label3 == '10'):
        channel = str('1:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value1 = channel + value_label3
        my_ascii = final_value1.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label3 == '15'):
        value_label3 = str('1:')
        my_ascii = value_label3.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label3 == '59'):
        value_label3 = str('1:')
        my_ascii = value_label3.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('1:')
            final_value1 = channel + value_label3
            my_ascii = final_value1.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


# label for the slider
jaw_label1 = ttk.Label(
    root,
    text='jaw:'
)

jaw_label1.grid(
    column=0,
    row=3,
    sticky='w'
)

#  slider
jaw = ttk.Scale(
    root,
    from_=1,
    to=7,
    orient='horizontal',  # vertical
    command=jaw_changed,
    variable=slider2_value
)

jaw.grid(
    column=1,
    row=3,
    sticky='w'
)

# current value label
jaw_value_label = ttk.Label(
    root,
    text=''
)

jaw_value_label.grid(
    row=3,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label1 = ttk.Label(
    root,
    text=get_slider2_value()
)
value_label1.grid(
    row=3,
    columnspan=8,
    sticky='n'
)

#third motor
# slider current value
slider3_value = tk.DoubleVar()


#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)

def get_slider3_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(slider3_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def elbow_changed(event):
    value_label6.configure(text=get_slider3_value())
    value_label7=(get_slider3_value())
    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label7 == '10'):
        channel = str('4:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value2 = channel + value_label7
        my_ascii = final_value2.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label7== '15'):
        value_label7 = str('4:')
        my_ascii = value_label7.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label7 == '59'):
        value_label7 = str('4:')
        my_ascii = value_label7.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('4:')
            final_value2 = channel + value_label7
            my_ascii = final_value2.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


#label for the slider
elbow_label6 = ttk.Label(
    root,
    text='elbow:'
)

elbow_label6.grid(
    column=0,
    row=5,
    sticky='w'
)

#  slider
elbow = ttk.Scale(
    root,
    from_=1,
    to=12,
    orient='horizontal',  # vertical
    command=elbow_changed,
    variable=slider3_value
)

elbow.grid(
    column=1,
    row=5,
    sticky='w'
)

# current value label
elbow_value_label = ttk.Label(
    root,
    text=''
)

elbow_value_label.grid(
    row=5,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label6 = ttk.Label(
    root,
    text=get_slider3_value()
)
value_label6.grid(
    row=5,
    columnspan=8,
    sticky='n'
)
#slider4
slider4_value = tk.DoubleVar()


#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)

def get_slider4_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(slider4_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def shoulder_changed(event):
    value_label16.configure(text=get_slider4_value())
    value_label17=(get_slider4_value())
    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label17 == '10'):
        channel = str('3:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value3 = channel + value_label17
        my_ascii = final_value3.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label17== '15'):
        value_label17 = str('3:')
        my_ascii = value_label17.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label17 == '59'):
        value_label17 = str('3:')
        my_ascii = value_label17.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('3:')
            final_value3 = channel + value_label17
            my_ascii = final_value3.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


# label for the slider
shoulder_label16 = ttk.Label(
    root,
    text='shoulder:'
)

shoulder_label16.grid(
    column=0,
    row=7,
    sticky='w'
)

#  slider
shoulder = ttk.Scale(
    root,
    from_=1,
    to=14,
    orient='horizontal',  # vertical
    command=shoulder_changed,
    variable=slider4_value
)

shoulder.grid(
    column=1,
    row=7,
    sticky='w'
)

# current value label
shoulder_value_label = ttk.Label(
    root,
    text=''
)

shoulder_value_label.grid(
    row=7,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label16 = ttk.Label(
    root,
    text=get_slider4_value()
)
value_label16.grid(
    row=7,
    columnspan=8,
    sticky='n'
)
#slider5
slider5_value = tk.DoubleVar()


#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)

def get_slider5_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(slider5_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def base_changed(event):
    value_label61.configure(text=get_slider5_value())
    value_label71=(get_slider5_value())
    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label71 == '10'):
        channel = str('2:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value4 = channel + value_label71
        my_ascii = final_value4.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label71== '15'):
        value_label71 = str('2:')
        my_ascii = value_label71.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label71 == '59'):
        value_label71 = str('2:')
        my_ascii = value_label71.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('2:')
            final_value4 = channel + value_label71
            my_ascii = final_value4.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


# label for the slider
base_label61 = ttk.Label(
    root,
    text='base'
)

base_label61.grid(
    column=0,
    row=9,
    sticky='w'
)

#  slider
base = ttk.Scale(
    root,
    from_=1,
    to=12,
    orient='horizontal',  # vertical
    command=base_changed,
    variable=slider5_value
)

base.grid(
    column=1,
    row=9,
    sticky='w'
)

# current value label
base_value_label = ttk.Label(
    root,
    text=''
)

base_value_label.grid(
    row=9,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label61 = ttk.Label(
    root,
    text=get_slider5_value()
)
value_label61.grid(
    row=9,
    columnspan=8,
    sticky='n'
)
#slider4
slider4_value = tk.DoubleVar()


#my_arduino2 = serial.Serial('COM11', 9600)
#time.sleep(2)

def get_slider4_value():
    #return '{: .2f}'.format(current_value.get())
    return '{0:.0f}'.format(slider4_value.get()*10)
    #arduino = serial.Serial('COM11', 9600)
    time.sleep(2)

def sliderrrr_changed(event):
    value_label16.configure(text=get_slider4_value())
    value_label17=(get_slider4_value())
    #value_label2=str(value_label2)
    #print('label 2',value_label2)
    #print(value_label)
    #my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2.05)
   # my_arduino = serial.Serial('COM11', 9600)
    #time.sleep(2)

    #my_arduino.write(bytes(value_label2, 'utf-8'))
    #time.sleep(0.05)
    #value_label2 = '50'

    if (value_label17 == '10'):
        channel = str('3:')
        # my_ascii = value_label3.encode('ascii')
        # my_arduino.write(my_ascii)
        # print(my_ascii)

        final_value3 = channel + value_label17
        my_ascii = final_value3.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)


    elif (value_label17== '15'):
        value_label17 = str('3:')
        my_ascii = value_label17.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)

    elif (value_label17 == '59'):
        value_label17 = str('3:')
        my_ascii = value_label17.encode('ascii')
        my_arduino.write(my_ascii)
        print(my_ascii)
    else:
            channel = str('3:')
            final_value3 = channel + value_label17
            my_ascii = final_value3.encode('ascii')
            my_arduino.write(my_ascii)
            print(my_ascii)

    #my_ascii = value_label2.encode('ascii')


    #print('my ascii',my_ascii)
    #my_arduino.write(my_ascii)
    #time.sleep(2)
   #my_string = str(input("Servo position: "))

    #my_ascii = my_string.encode('ascii')
    #my_arduino.write(my_ascii)


# label for the slider
sliderrrr_label16 = ttk.Label(
    root,
    text='Shoulder:'
)

sliderrrr_label16.grid(
    column=0,
    row=7,
    sticky='w'
)

#  slider
sliderrrr = ttk.Scale(
    root,
    from_=1,
    to=14,
    orient='horizontal',  # vertical
    command=sliderrrr_changed,
    variable=slider4_value
)

sliderrrr.grid(
    column=1,
    row=7,
    sticky='w'
)

# current value label
sliderrrr_value_label = ttk.Label(
    root,
    text=''
)

sliderrrr_value_label.grid(
    row=7,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label16 = ttk.Label(
    root,
    text=get_slider4_value()
)
value_label16.grid(
    row=7,
    columnspan=8,
    sticky='n'
)
root.mainloop()
'''

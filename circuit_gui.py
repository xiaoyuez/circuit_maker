# GUI for a ciruit maker program. It creates a customized workout for you and times it.
# Written by xiaoyuez, Jan 2020.

import tkinter as tk
from pygame import mixer
import time
import pandas as pd
import numpy as np

# load workout dataframe
df = pd.read_csv('~/circuit_maker/workouts.csv')

# load the beeps
single_beep = "~/circuit_maker/single_beep.mp3"

# improvement ideas:
# 1. resize the buttons (it seems impossible in Mac)
# 2. fix radio button if unclicked
# 4. enlarge the workout database 
# 5. figure out what to do when there is insufficient number of workouts based on choice 
# 6. more continuity between workouts 


class Circuits(object):
    # the main circuit maker program
    def circuit_maker(self, num_circ, num_sets, intensity, emphasis, emphasis_prob = 0.7):
        # determine body parts and their chosen probability 
        body_parts = ['Arms','Legs','Butt','Abs','Back']
        emp_inx = [i for i in range(len(body_parts)) if body_parts[i] == emphasis][0]
        others_prob = (1 - emphasis_prob) / (len(body_parts) - 1)
        prob_list = np.repeat(others_prob, len(body_parts))
        prob_list[emp_inx] = emphasis_prob
        
        # choose workouts based on criteria without replacements
        circuits = pd.DataFrame()
        for i in range(num_circ * num_sets):
            if i % num_sets == 0: # if this is a new circuit, start with cardio
                this_workout = df[(df.Type == 'Cardio') & (df.chosen == 0)].sample()
                df.chosen[this_workout.index] = 1 # tag this workout
                circuits = circuits.append(this_workout)
            else:           
                chosen_type = np.random.choice(body_parts, p = prob_list)
                this_workout = df[(df[chosen_type] == 1) & (df.Intensity <= intensity) & (df.chosen == 0)].sample()
                df.chosen[this_workout.index] = 1
                circuits = circuits.append(this_workout)
        circuits = circuits.reset_index(drop = True)
        return circuits
    
    # the welcome window
    def init(self, root):
        self.frame = tk.Frame(root)
        self.frame.pack()

        bruh = tk.Label(self.frame, text = " ")
        bruh.grid(row = 0, column = 1, pady = 8)

        bruh2 = tk.Label(self.frame, text = " ")
        bruh2.grid(row = 1, column = 1, pady = 8)

        bruh3 = tk.Label(self.frame, text = " ")
        bruh3.grid(row = 2, column = 1, pady = 8)

        title = tk.Label(self.frame, text = "Circuit Maker ", font = ("Avenir", 50, 'bold'))
        title.grid(row = 3, column = 1, pady = 8)

        start_button = tk.Button(self.frame, text = 'Start', font = ("Avenir", 20), 
        justify = 'center', command = self.window_1)
        start_button.grid(row = 4, column = 1, pady = 8)

    # number of circuits & sets window
    def window_1(self):
        self.frame.destroy()
        self.frame = tk.Frame(root)
        self.frame.pack()

        title = tk.Label(self.frame, text = "Create Your Own Circuit Programs ", font = ("Avenir", 40, 'bold'))
        title.grid(row = 0, columnspan = 9, pady = 8)

        circ_response = tk.Label(self.frame, text = "Number of circuits:", font = ("Avenir", 20), justify = 'left')
        circ_response.grid(row = 1, column = 0, padx = 5, pady = 5)

        set_response = tk.Label(self.frame, text = "Number of sets:", font = ("Avenir", 20), justify = 'left')
        set_response.grid(row = 2, column = 0, padx = 5, pady = 5)

        repeat_response = tk.Label(self.frame, text = "Number of repeats:", font = ("Avenir", 20), justify = 'left')
        repeat_response.grid(row = 3, column = 0, padx = 5, pady = 5) 

        self.circ = tk.StringVar(value = '4')
        circ_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.circ, width = 5)
        circ_proposal.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.set = tk.StringVar(value = '4')
        set_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.set, width = 5)
        set_proposal.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.repeat = tk.StringVar(value = '2')
        repeat_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.repeat, width = 5)
        repeat_proposal.grid(row = 3, column = 1, padx = 5, pady = 5)

        emp_response = tk.Label(self.frame, text = "Body Part:", font = ("Avenir", 20), justify = 'left')
        emp_response.grid(row = 4, column = 0, padx = 5, pady = 5)

        self.v1 = tk.IntVar()
        self.v1.set(1)
        radio_values = {"Arms": "1","Legs": "2","Butt": "3","Abs": "4", "Back": "5"}
        for (text, value) in radio_values.items(): 
            tk.Radiobutton(self.frame, text = text, value = value, variable = self.v1, command = self.emp_chosen, font = ("Avenir", 20)).grid(row = 4, column = int(value), padx = 5, pady = 5)

        intensity_response = tk.Label(self.frame, text = "Training intensity:", font = ("Avenir", 20), justify = 'left')
        intensity_response.grid(row = 5, column = 0, padx = 5, pady = 5)

        self.v2 = tk.IntVar()
        self.v2.set(1)
        radio_values = {"Low": "1","Medium": "2","High": "3"}
        for (text, value) in radio_values.items(): 
            tk.Radiobutton(self.frame, text = text, value = value, variable = self.v2, command = self.int_chosen, font = ("Avenir", 20)).grid(row = 5, column = int(value), padx = 5, pady = 5)
        
        next_button = tk.Button(self.frame, text = 'Next', font = ("Avenir", 20), justify = 'center', command = self.window_2)
        next_button.grid(row = 7, column = 7)
  
    # body part button commands
    def emp_chosen(self):
        body_parts = ['Arms','Legs','Butt','Abs','Back']
        self.emphasis = body_parts[self.v1.get() - 1]

    # training intensity button commands
    def int_chosen(self):
        intensities = ['Low', 'Medium', 'High']
        self.intensity = intensities[self.v2.get() - 1]

    # the timer window 
    def window_2(self):
        self.frame.destroy()
        self.frame = tk.Frame(root)
        self.frame.pack()
        
        title = tk.Label(self.frame, text = "Create Your HIIT Timer (seconds)", font = ("Avenir", 40, 'bold'))
        title.grid(row=0, columnspan=9, pady=8)

        ht_response = tk.Label(self.frame, text = "High Intensity:", font = ("Avenir", 20), justify = 'left')
        ht_response.grid(row = 1, column = 1, pady = 5, padx = 5)

        lt_response = tk.Label(self.frame, text = "Low Intensity:", font = ("Avenir", 20), justify = 'left')
        lt_response.grid(row = 2, column = 1, pady = 5, padx = 5)

        between_response = tk.Label(self.frame, text = "Between Circuits:", font = ("Avenir", 20), justify = 'left')
        between_response.grid(row = 3, column = 1, pady = 5, padx = 5)

        warmup_response = tk.Label(self.frame, text = "Warmup:", font = ("Avenir", 20), justify = 'left')
        warmup_response.grid(row = 4, column = 1, pady = 5, padx = 5)

        cool_response = tk.Label(self.frame, text = "Cool Down:", font = ("Avenir", 20), justify = 'left')
        cool_response.grid(row = 5, column = 1, pady = 5, padx = 5)

        self.ht = tk.StringVar(root, value='50')
        ht_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.ht, width = 5)
        ht_proposal.grid(row = 1, column = 2, pady = 5, padx = 5)

        self.lt = tk.StringVar(root, value='10')
        lt_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.lt, width = 5)
        lt_proposal.grid(row = 2, column = 2, pady = 5, padx = 5)

        self.between = tk.StringVar(root, value='30')
        between_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.between, width = 5)
        between_proposal.grid(row = 3, column = 2, pady = 5, padx = 5)

        self.warmup = tk.StringVar(root, value='60')
        warmup_proposal = tk.Entry(self.frame, font = ("Avenir",20), textvariable = self.warmup, width = 5)
        warmup_proposal.grid(row = 4, column = 2, pady = 5, padx = 5)

        self.cool = tk.StringVar(root, value='60')
        cool_proposal = tk.Entry(self.frame, font = ("Avenir", 20), textvariable = self.cool, width = 5)
        cool_proposal.grid(row = 5, column = 2, pady = 5, padx = 5)

        next_button = tk.Button(self.frame, text = 'Ready?', font = ("Avenir", 20), justify = 'center', command = self.circuit_wrapper)
        next_button.grid(row = 6, column = 3)

        prev_button = tk.Button(self.frame, text = 'Previous', font = ("Avenir", 20), justify = 'center', command = self.window_1)
        prev_button.grid(row = 6, column = 0)
      
    # pass the entry info to the main circuit maker function
    def circuit_wrapper(self):
        today_circuit = self.circuit_maker(num_circ = int(self.circ.get()), 
        num_sets = int(self.set.get()),
        emphasis = self.emphasis,
        intensity = self.v2.get())
        self.workout_list = today_circuit.Name
        self.workout_iter = 0
        self.circuit_iter = 1
        self.repeat_iter = 1
        self.countdown_init()

    def play_single_beep(self):
        mixer.init(44100)
        mixer.music.load(single_beep)
        mixer.music.play()
        time.sleep(0.7)
        mixer.music.stop()
    
    # initialize the countdown from warmup
    def countdown_init(self):
        self.frame.destroy()
        self.frame = tk.Frame(root)
        self.frame.pack()

        self.countdown_title = tk.Label(self.frame, text = "Warmup", font = ("Avenir", 40, 'bold'), bg = '#ff8c00', bd = 4)
        self.countdown_title.grid(row = 0, column = 1, pady = 8)

        self.countdown_label = tk.Label(self.frame, text = " ", font = ("Avenir", 35, 'bold'))
        self.countdown_label.grid(row = 2, column = 1, pady = 8 )

        self.countdown_clock = tk.Label(self.frame, text = " ", font = ("Avenir", 200, 'bold'), fg = '#ff8c00')
        self.countdown_clock.grid(row = 3, columnspan = 3, pady = 8 )

        self.countdown_circ = tk.Label(self.frame, text = " ", font = ("Avenir", 28, 'bold'))
        self.countdown_circ.grid(row = 0, column = 0, padx = 15, pady = 8 )

        self.countdown_repeat = tk.Label(self.frame, text = " ", font = ("Avenir", 28, 'bold'))
        self.countdown_repeat.grid(row = 0, column = 2, padx = 15, pady = 8 )

        self.paused = 0
        self.pause_button = tk.Button(self.frame, text = "Pause", font = ("Avenir", 20, 'bold'), command = self.pause, width = 6)
        self.pause_button.grid(row = 6, column = 2, padx = 15, pady = 8 )

        self.play_single_beep()
        self.next_section = 'ht'
        self.countdown(int(self.warmup.get()))

    # little command function for the pause button 
    def pause(self):
        if self.paused == 1:
            self.paused = 0
            self.pause_button.config(text = "Pause")
        elif self.paused == 0:
            self.paused = 1
            self.pause_button.config(text = "Resume")
 
    # the main countdown function
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        # decide where to go once the countdown has finished
        if self.remaining <= 0:
            self.blank_window()
        else:
            minutes = '%02d' % int(self.remaining / 60)
            seconds = '%02d'% (round(self.remaining) % 60)
            clock = "{}:{}".format(minutes, seconds)
            self.countdown_clock.configure(text = clock)
            if self.paused == 1: # if pause button is pressed
                self.remaining = self.remaining
            else: 
                self.remaining = self.remaining - 1
            root.after(1000, self.countdown)

    # to avoid flickering between transitions
    def blank_window(self):
        self.countdown_title.configure(text = " ", fg = 'white')
        self.countdown_label.configure(text = " ")
        self.countdown_clock.configure(text = " ", fg = 'white')
        self.countdown_circ.configure(text = " ")
        self.countdown_repeat.configure(text = " ")

        if self.next_section == 'ht':
            self.ht_init()
        elif self.next_section == 'lt':
            self.lt_init()
        elif self.next_section == 'between':
            self.between_init()
        elif self.next_section == 'cool':
            self.cool_init()
        else:
            self.last_window()

    # high intensity countdown initializer 
    def ht_init(self):      
        self.countdown_title.configure(text = "High Intensity", bg = '#d82525')
        self.countdown_label.configure(text = "[ {} ]".format(self.workout_list[self.workout_iter]))
        self.countdown_clock.configure(text = " ", fg = '#d82525')
        self.countdown_circ.configure(text = "Circuit: {}/{}".format(self.circuit_iter, int(self.circ.get())))
        self.countdown_repeat.configure(text = "Repeat: {}/{}".format(self.repeat_iter, int(self.repeat.get())))

        self.workout_iter += 1
        if self.workout_iter % int(self.set.get()) == 0: # if a circuit is completed
            if self.repeat_iter == int(self.repeat.get()): # if this circuit has been repeated 
                self.circuit_iter += 1
                self.repeat_iter = 1 # reset 
                if self.workout_iter == len(self.workout_list): # if all the circuits are completed
                    self.next_section = 'cool'
                else:
                    self.next_section = 'between' # take a break 
            else:
                self.repeat_iter += 1
                self.workout_iter = self.workout_iter - int(self.set.get()) # repeat the workout
                self.next_section = 'lt'
        else: # if stil in the circuit
            self.next_section = 'lt'

        self.play_single_beep()
        self.countdown(remaining = int(self.ht.get()))

    # low intensity countdown initializer
    def lt_init(self):      
        self.countdown_title.configure(text = "Low Intensity", bg = '#399d72')
        self.countdown_label.configure(text = "[ Quick Rest ]")
        self.countdown_clock.configure(text = " ", fg = '#399d72')
        self.countdown_circ.configure(text = "Circuit: {}/{}".format(self.circuit_iter, int(self.circ.get())))
        self.countdown_repeat.configure(text = "Repeat: {}/{}".format(self.repeat_iter, int(self.repeat.get())))
        
        self.next_section = 'ht'
        self.play_single_beep()
        self.countdown(remaining = int(self.lt.get()))

    # mini break countdown initializer
    def between_init(self):      
        str1 = "Good job! You have completed circuit {} / {}".format(int(self.workout_iter / int(self.set.get())), int(self.circ.get()))
        self.countdown_title.configure(text = "Mini Break", bg = '#6d9eeb')
        self.countdown_label.configure(text = str1)
        self.countdown_clock.configure(text = " ", fg = '#6d9eeb')

        self.next_section = 'ht'
        self.play_single_beep()
        self.countdown(remaining = int(self.between.get()))

    # cool down countdown initializer
    def cool_init(self):      
        str1 = "Excellent! All circuits completed."
        self.countdown_title.configure(text = "Cool Down", bg = '#597073')
        self.countdown_label.configure(text = str1)
        self.countdown_clock.configure(text = " ", fg = '#597073')

        self.next_section = 'out'
        self.play_single_beep()
        self.countdown(remaining = int(self.lt.get()))
    
    def last_window(self):
        self.frame.destroy()
        self.frame = tk.Frame(root)
        self.frame.pack()

        bruh = tk.Label(self.frame, text = " ")
        bruh.grid(row = 0, column = 1, pady = 8)

        bruh2 = tk.Label(self.frame, text = " ")
        bruh2.grid(row = 1, column = 1, pady = 8)

        bruh3 = tk.Label(self.frame, text = " ")
        bruh3.grid(row = 2, column = 1, pady = 8)

        title = tk.Label(self.frame, text = "Please exit the program", font = ("Avenir", 45, 'bold'))
        title.grid(row = 3, column = 1, pady = 8)

root = tk.Tk()
root.geometry("800x600")
root.title('Circuit Maker')
app = Circuits()
app.init(root)
root.mainloop()
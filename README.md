## Circuit Maker
This is a toy project that creates customized workout programs for you. It started with my frustration that it is hard to find flexible HIIT (High Intensity Interval Timing) training apps. They either come with a few sets of pre-determined workouts, or do not allow you to create your own timer, or both. I soon realized that each workout has its own unique attributes and can be coded into a data frame. For example, a simple plank works on your abs and arms but not back and legs. It is of medium intensity and it does not require weights. Once you have a table of these workouts, you can select the workouts needed to train certain body parts with your desired training intensity. This is exactly what Circuit Maker is designed to do. 

## Requirements
`python 2.7 `or above

`pandas`

`numpy`

`tkinter`

`pygame`

## How to use it
1. Once you have cloned it, go to its directory and type `python circuit_gui.py`, it should automatically start.

2.  On this window, specify the number of circuits, the number of sets ( n sets = 1 circuit) and the number of repeats ( e.g. 2 means to repeat each circuit twice).  And select the body part to train and the desired training intensity.
![img1](https://github.com/xiaoyuez/circuit_maker/blob/master/images/image1.png)<!-- .element height="50%" width="50%" -->

3.  On this window, specifiy the duration (in seconds) for each period in your workout. The default should work for most people.
![img2|200x200,20%](https://github.com/xiaoyuez/circuit_maker/blob/master/images/image2.png)

4. The program will start. You will see these following windows:
![img3](https://github.com/xiaoyuez/circuit_maker/blob/master/images/image3.png)
![img4](https://github.com/xiaoyuez/circuit_maker/blob/master/images/image4.png)

## Future improvements
1. Enlarge the workout database.
2. Maybe add a restart button.

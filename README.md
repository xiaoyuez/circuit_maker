## Circuit Maker
This is a toy project that creates customized workout programs for you. It started with my frustration that it is hard to find flexible HIIT (High Intensity Interval Timing) training apps. They either come with a few sets of pre-determined workouts, or do not allow you to create your own timer, or both. I soon realized that each workout has its own unique attributes and can be coded into a data frame. For example, a simple plank works on your abs and arms but not back and legs. It is of medium intensity and it does not require weights. Once you have a table of these workouts, you can select the workouts needed to train certain body parts with your desired training intensity. This is exactly what Circuit Maker is designed to do. 

## Requirements
`python 2.7 `or above

`pandas`

`numpy`

`tkinter`

`pygame`

## How to use it
1. Once you have cloned it, go to terminal and run `~/circuit_maker/circuit_gui.py`, it should automatically start.

2.  On this window, specify the number of circuits, the number of sets ( n sets = 1 circuit) and the number of repeats ( e.g. 2 means to repeat each circuit twice).  And select the body part to train and the desired training intensity.
![img1](/Users/xiaoyue/Desktop/repo/circuit_maker/images/1.png)

3.  On this window, specifiy the duration (in seconds) for each period in your workout. The default should work for most people.
![img2](/Users/xiaoyue/Desktop/repo/circuit_maker/images/2.png)

4. The program will start. You will see these following windows:
![img3](/Users/xiaoyue/Desktop/repo/circuit_maker/images/3.png)
![img4](/Users/xiaoyue/Desktop/repo/circuit_maker/images/4.png)
![img5](/Users/xiaoyue/Desktop/repo/circuit_maker/images/5.png)
![img6](/Users/xiaoyue/Desktop/repo/circuit_maker/images/6.png)
![img7](/Users/xiaoyue/Desktop/repo/circuit_maker/images/7.png)

## Future improvements
1. As this started out as a personal project, it just provides the workout name, assuming the user already knows what to do.  In the future version, I would like to add some verbal / image / video instructions to make it clear to new users. 
2. I did not implement a warning system that alerts the user if the option selected (e.g. 4 circuits, 4 sets, Back, High intensity) results in insuffiicent workouts in the database. This will be added in the future version. 
3. I would also like to add a `weights?` feature, so that you can do just a bodyweight workout when you don't have the weights. 

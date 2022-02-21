import csv
import matplotlib.pyplot as plt


import ball_tracker as BallTracker
from trajectory_curve_fitter import ParabolaTrajectoryFinder


if __name__ == "__main__":

    ball_video_1_path = "assets/ball_video1"
    ball_video_2_path = "assets/ball_video2"

    # calling the ball tracker class to get the ball postion and save it in a csv file
    BallTracker.get_ball_trajectory(ball_video_1_path)
    BallTracker.get_ball_trajectory(ball_video_2_path)

    data_1 = list()
    with open(ball_video_1_path.split('/')[1]+"pos.csv", 'r') as f:
        reader = csv.reader(f)
        for pos in reader:
            data_1.append(pos)

    data_2 = list()
    with open(ball_video_2_path.split('/')[1]+"pos.csv", 'r') as f:
        reader = csv.reader(f)
        for pos in reader:
            data_2.append(pos)
    
    # splitting the orifinal data to x and y
    data1_x = [int(x) for x,y in data_1]
    data1_y = [int(y) for x,y in data_1]
    data2_x = [int(x) for x,y in data_2]
    data2_y = [int(y) for x,y in data_2]
    
    # finding the parabola from data1
    curve_finder_1= ParabolaTrajectoryFinder(data_1)
    x1, y1 = curve_finder_1.get_curve_data()
    
    # finding the parabola from data2
    curve_finder_2 = ParabolaTrajectoryFinder(data_2)
    x2, y2 = curve_finder_2.get_curve_data()

    # plotting the data for both data
    plt.title("Parbola trajectory for Ball Video 1")
    plt.xlabel('X axis') 
    plt.ylabel('Y axis') 
    plt.scatter(data1_x, data1_y)
    plt.plot(x1, y1)

    plt.axes([0,600, 0, 600])
    plt.show()
    
    plt.title("Parbola trajectory for Ball Video 2")
    plt.xlabel('X axis') 
    plt.ylabel('Y axis') 
    plt.scatter(data2_x, data2_y)
    plt.plot(x2, y2)

    plt.axes([0,600, 0, 600])
    plt.show()
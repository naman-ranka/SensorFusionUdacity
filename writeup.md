# Writeup: Track 3D-Objects Over Time

Please use this starter template to answer the following questions:

### 1. Write a short recap of the four tracking steps and what you implemented there (filter, track management, association, camera fusion). Which results did you achieve? Which part of the project was most difficult for you to complete, and why?

**Step 1**: Buliding a kalman filter.

Kalman Filter:

Implemented update and predict function in [filter.py](/student/filter.py)



**Step 2** : Building a track management system.

Built a rack managment system in [trackmanagment.py](/student/trackmanagement.py) .

Functions : Initalize new tracks , Delete old and unassigned tracks, Decrease score for unassined tracks and increase score for associated tracks.



**Step 3** : Nearest neighbour association.

Associate tracks with measurmenst. Also used mahalanobis distance measure for accurate association [association.py](/student/association.py)

**Step 4** : Camera Fusion
To fuse camera meausrments we use a Extended kalman filter as relation between camera measurmentsa and states of vehicle are non linear. Functions implementd in [measurments.py](/student/measurements.py) are
- check if track is in FOV of sensor.
- finding h(x) for camera sensor.


### 2. Do you see any benefits in camera-lidar fusion compared to lidar-only tracking (in theory and in your concrete results)? 

**In theory**:
Fusing sensor data provides better estimation of accuracy, over a wide range of operating conditions (Best of both sensors lidar and camera) .Fault tolerance and resilience of the sensor system is increased.

**In this project**:
By comaring tracking results of [Lidar only](/img/PMSE_plot_lidar.png) measurments and results of [sensor fusion](/img/LidarCameraFusion.gif) system, we see that the Root mean square error of sensor fusuin system is lower than that of only lidar.



### 3. Which challenges will a sensor fusion system face in real-life scenarios? Did you see any of these challenges in the project?

Main challenge of a sensor fusion system is Resolution difference and different sampling times of the sesnors involved.



### 4. Can you think of ways to improve your tracking results in the future?

Ways to impove tracking results:

- Using a batter 3D object detection model for Lidar and better 2D object detection fo camera
- Inceasing the sampling frequency of sensors.
- Using a better motion model. The current model allows a car to have a free celocity in all 3 directions(x,y,z) whereas in reality a car can only move forward and backwards and the y-direction velocity is dependent on the yaw of the vehice.
 Bicyle model would be a better choice.



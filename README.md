# Robosapians_Saintgits College Of Engineering_Develop a 2D Occupancy Grid Map of a Room using Overhead Cameras
### Final Report Submission for Intel Unnati Industrial Training

---

## Abstract

This project explores the development of a 2D occupancy grid map of an indoor environment using a network of overhead RGB cameras, aimed at enhancing Autonomous Mobile Robot (AMR) navigation. Utilizing the ROS 2 Foxy framework and Gazebo for simulation, the project seeks to demonstrate the potential for accurate and rapid mapping in controlled indoor settings. The motivation behind this work stems from the need for reliable environment mapping to facilitate AMR path planning and obstacle avoidance. Through a series of methodical steps, including camera calibration, data collection, and image processing, the project partially succeeded in generating an occupancy grid map that identifies occupied and unoccupied spaces. The results underscore both the promise of using overhead cameras for detailed environmental mapping and the challenges related to calibration precision and data processing. Despite these challenges, the project highlights significant strides towards effective AMR navigation and sets the stage for future improvements and more comprehensive mapping solutions.

---

## Keywords

2D occupancy grid map, Overhead cameras, Autonomous Mobile Robots (AMRs), ROS 2 Foxy, Gazebo simulation, Indoor environment mapping, RGB cameras, Path planning, Obstacle avoidance, Environment mapping

---

## Introduction

The rise of Autonomous Mobile Robots (AMRs) has significantly impacted various industries by automating tasks that were previously labor-intensive and time-consuming. This project investigates the use of overhead RGB cameras to develop a 2D occupancy grid map for indoor environments. By leveraging the ROS 2 Foxy framework and Gazebo for simulation, the project aims to showcase the potential of RGB cameras in generating accurate and fast occupancy grids. The primary objective is to demonstrate the feasibility and effectiveness of this approach in mapping indoor environments for AMR navigation.

---

## Libraries Used

In the project for various tasks, the following libraries and packages are used:

- ROS 2 Foxy
- Gazebo
- Rviz 2
- OpenCV
- PCL (Point Cloud Library)
- rclcpp
- tf2_ros
- numpy

---

## Methodology

This project utilized four overhead RGB cameras and ROS 2 Foxy for real-time data processing. The methodology is as follows:

1. **Hardware Setup:** Four overhead RGB cameras were strategically positioned in the simulated indoor environment.
2. **Camera Calibration:** Precise calibration ensured accurate spatial mapping by minimizing optical distortions.
3. **Data Processing:** Real-time image processing algorithms in ROS 2 Foxy performed object detection and segmentation to classify areas as occupied or free.
4. **Occupancy Grid Mapping:** Processed data was converted into a 2D occupancy grid map representing the environment’s spatial layout.
5. **Validation in Gazebo:** The solution was tested and validated in the Gazebo simulation environment for accuracy and performance under various conditions.
6. **Iterative Refinement:** Feedback from validation drove iterative improvements in camera calibration, algorithms, and overall mapping accuracy.

---

## Implementation

The implementation of our project involved a systematic approach integrating ROS 2 Foxy, Gazebo simulation, and overhead RGB cameras to develop a detailed 2D occupancy grid map of indoor environments. The pre-processing and cleaning stage is completed in four distinct and consecutive steps:

1. **Hardware Setup:** Positioning of overhead RGB cameras in the simulated indoor environment.
2. **Camera Calibration:** Ensuring precise calibration for accurate spatial mapping.
3. **Data Processing:** Real-time image processing for object detection and segmentation.
4. **Occupancy Grid Mapping:** Conversion of processed data into a 2D occupancy grid map.
5. **Validation in Gazebo:** Testing and validation in the Gazebo simulation environment.
6. **Iterative Refinement:** Continual improvement based on validation feedback.

---

## Results & Discussion

The project involves developing a 2D occupancy grid map for indoor environments using overhead RGB cameras and ROS 2 Foxy in a Gazebo simulation. This innovative approach aims to offer a cost-effective alternative to traditional LIDAR-based mapping methods, focusing on accurate and real-time spatial mapping to enhance Autonomous Mobile Robots (AMRs) navigation. Key features include precise camera calibration, real-time image processing, and simulation-based optimization. While offering advantages like accuracy, cost-effectiveness, and scalability, challenges include dependency on lighting conditions and computational complexity. The project demonstrates the feasibility of using overhead cameras for effective AMR navigation.

---

## Conclusion

In this project, we successfully developed a detailed 2D occupancy grid map using overhead RGB cameras integrated with ROS 2 Foxy and validated within the Gazebo simulation environment. This approach offers a cost-effective alternative to traditional LIDAR-based methods while ensuring robust performance in real-time data processing and environmental mapping. Iterative refinements based on simulation results enhanced our system’s accuracy in camera calibration, image processing, and overall mapping quality. Our methodology lays a solid foundation for advancing Autonomous Mobile Robot (AMR) navigation in dynamic indoor environments, supporting optimized path planning, obstacle avoidance, and spatial awareness. This project demonstrates the feasibility and potential of using overhead cameras for effective AMR navigation and spatial mapping applications.

---

## Authors

- Arvind Raju - raju.arvind@intel.com
- Amit Baxi - amit.s.baxi@intel.com
- Ajay Kumar Sandula - ajay.kumar.sandula@intel.com

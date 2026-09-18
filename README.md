<p align="center">




<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/ManchesterRoboticsLtd/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/blob/main/Misc/Logos/MCR2_Logo_White.png">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/ManchesterRoboticsLtd/TE3003B_Integration_of_Robotics_and_Intelligent_Systems/blob/main/Misc/Logos/MCR2_Logo_Black.png">
  <img alt="Shows MCR2 logo in black or white." width="150" align="right">
</picture>

</p>


---
---

# MCR2- Intensive ROS 2 Course

---
---

  ## Introduction
This course, developed by Manchester Robotics Ltd (MCR2), provides students with a practical introduction to the Robot Operating System 2 (ROS 2) and its application to robotics.

   * The course is divided into four sessions, carefully designed to equip participants with the fundamental skills required to develop, configure, visualise, and model robotic systems using ROS 2.
   * Starting with the fundamental concepts of ROS 2, participants progressively develop expertise in ROS architecture, nodes, topics, messages, launch files, namespaces, parameters, coordinate transformations, TF2, URDF, and robot visualisation. Learning is reinforced through practical activities and three mini challenges.
   * By the end of the course, participants will have developed a basic ROS 2 development workflow—from creating ROS 2 nodes and communication systems to managing coordinate transformations and modelling robots using URDF.
   * This repository contains all the presentations, activities, examples, mini challenges, and supporting files required for the ROS 2 Express course.
   * The repository is organised by session, with each subfolder containing the materials and files required to complete the corresponding activities.

  
  ## Learning Outcomes
  Upon successful completion of this course, participants will be able to:
  * Develop basic robotic applications using the ROS 2 middleware framework.
  * Create and manage ROS 2 nodes, topics, messages, packages, and launch files.
  * Configure ROS 2 systems using namespaces and parameters.
  * Use parameter files to configure ROS 2 nodes.
  * Visualise and analyse ROS 2 systems using tools such as rqt_graph and rqt_plot.
  * Define and manage coordinate transformations using the TF2 framework
  * Create static and dynamic transformations in ROS 2.
  * Use TF broadcasters and listeners to manage coordinate frames.
  * Create, configure, and visualise robot models using URDF and RViz.
  * Define links and joints for robotic systems.
  * Use Robot State Publisher and Joint State Publisher.
  * Integrate ROS 2 components into practical robotic applications.
  * Apply ROS 2 development practices to practical robotics engineering problems.

  ## General Information
  * Duration: 2 Weeks
  * Professors: TBD
  * Number of Classes: 4
  * Starts: September 15th
  * Teams Link Classes: https://teams.microsoft.com/meet/318362166342773?p=24AJxpaliPMQX7YJV6
  * Video recordings: https://manchesterrobotics-my.sharepoint.com/:f:/g/personal/mario_mtz_manchester-robotics_com/IgATBLvnvRwgRIcMekYBSr8xAQiuQdt6pzmGz0QzXQb5nRU?e=cOteUa
  * CERTIFICATION: https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=dQfP28SpnUOvp08zgT4jvp6Xm1zRBXVAji8N1f1MmDVUNVJTMVpHS0UyR0dFVFA1WjZEU0ZRNDZaNS4u&origin=QRCode

## General Requirements

The following general requirements apply throughout the course. Please note that additional requirements specific to each session are provided in the corresponding session subsection. Some requirements may therefore be repeated.

* Computer with access to Microsoft Teams for online classes.
* Basic knowledge of Python.
* Basic knowledge of Object-Oriented Programming (OOP) in Python.
* Basic knowledge of Linear Algebra and Kinematics.
* Basic knowledge of Ubuntu.
* Virtual Machine installed before starting the course.
* Students who require support with Linear Algebra or Kinematics can attend the additional support sessions on Mondays and Wednesdays from 4:30 PM to 6:00 PM.
* Supporting videos for Virtual Machine installation and basic Ubuntu concepts can be found on this link: https://manchesterrobotics-my.sharepoint.com/:f:/g/personal/mario_mtz_manchester-robotics_com/IgBzfPhlSc2SRZT5z0nXC0ZeAdIKf-20_VbZG07WafiOGXU?e=VMp0yg
* VMWare installation link: https://manchesterrobotics-my.sharepoint.com/:f:/g/personal/mario_mtz_manchester-robotics_com/Ek7a-yCprKNAvD2lWlNBVDsBW21FV5kKFtZhKlbxL9h7aQ?e=g8yefL


# Sessions

## Week 1: ROS 2 Core Concepts

  ### Sesion 1: ROS 2 Introduction

  This session will introduce the teaching team and the fundamental concepts of the Robot Operating System 2.

  #### Session:
  * What is ROS?
  * ROS Basics
  * ROS Architecture
  * ROS Communication
  * ROS Nodes
  * ROS Topics and Messages
  * ROS Packages
  * ROS Workspaces
  * ROS Command Line Tools
  * ROS Launch Files

  #### Activities:
  * A1: ROS 2 Basic Communication
  * A2: Creating a ROS 2 Package
  * A3: Creating Publisher and Subscriber Nodes
  * A4: ROS 2 Communication Example
  * A5: ROS Launch Files

  ### Sesion 2: ROS 2 Practicalities
  This session will introduce additional ROS 2 tools used to organise, configure, and manage more complex robotic systems.

  #### Session:
  * ROS Namespaces
  * ROS Namespaces Examples
  * Nested Launch Files
  * ROS Parameters
  * ROS Parameter Files
  * YAML Configuration Files
  * ROS Custom Messages
  * ROS Custom Messages Examples
  * ROS Services
  * ROS Visualisation Tools

  #### Activities:
  * A1: ROS Namespaces
  * A2: Multiple ROS Nodes using Namespaces
  * A3: Launch File Parameters
  * A4: ROS Parameter Files
  * A5: YAML Configuration
  * A6: ROS Custom Messages
  * A7: Simulated DC Motor System


## Week 2: Robot Transforms and Modelling

### Sesion 3: ROS 2 Transforms
  This session will introduce coordinate transformations and the TF2 framework used in ROS 2.

  #### Session:
  * Introduction to Coordinate Transformations
  * Coordinate Frames
  * Parent and Child Frames
  * Static Transformations
  * Dynamic Transformations
  * TF2
  * Transform Broadcasters
  * Static Transform Broadcasters
  * Dynamic Transform Broadcasters
  * Transformation Listeners
  * TF Buffers
  * Transformation Queries
  * Visualising Coordinate Frames

  #### Activities:
  * A1: Basic Coordinate Transformations
  * A2: Static Transformations
  * A3: Dynamic Transformations
  * A4: TF Broadcaster
  * A5: TF Listener
  * A6: Transformation Buffer
  * A7: TF Tree Visualisation
  * A8: RViz Transform Visualisation

### Sesion 4: Robot Modelling with URDF
  This session will introduce robot modelling and visualisation using URDF and RViz.

  #### Session:
  * Introduction to URDF Files
  * URDF Structure
  * Links and Joints
  * Fixed Joints
  * Revolute Joints
  * Continuous Joints
  * Prismatic Joints
  * Robot State Publisher
  * Joint State Publisher
  * Joint State Publisher GUI
  * Robot Description
  * Robot Visualisation in RViz

  #### Activities:
  * A1: Create URDF Files
  * A2: Fixed Joints
  * A3: Revolute, Continuous, and Prismatic Joints
  * A4: Joint State Publisher
  * A5: Robot State Publisher
  * A6: Robot Visualisation in RViz
  * A7: Robot Links and Meshes

## Declaration
At Manchester Robotics, we firmly believe that innovation is driven by change, so we have made it our mission to change access to educational robotics. We hope you enjoy our products and support this revolution.

So, from the team at MCR2, we would like to say 

                                                          Thank you!
                                                   {Learn, Create, Innovate};
---
  ## Disclaimer
 *THE PIECES, IMAGES, VIDEOS, DOCUMENTATION, ETC. SHOWN HERE ARE FOR INFORMATIVE PURPOSES ONLY. THE DESIGN IS PROPRIETARY AND CONFIDENTIAL TO MANCHESTER ROBOTICS LTD. (MCR2). THE INFORMATION, CODE, SIMULATORS, DRAWINGS, VIDEOS PRESENTATIONS ETC. CONTAINED IN THIS REPOSITORY IS THE SOLE PROPERTY OF MANCHESTER ROBOTICS LTD. ANY REPRODUCTION OR USAGE IN PART OR AS A WHOLE WITHOUT THE WRITTEN PERMISSION OF MANCHESTER ROBOTICS LTD. IS STRICTLY PROHIBITED*

*THIS WEBSITE MAY CONTAIN LINKS TO OTHER WEBSITES OR CONTENT BELONGING TO OR ORIGINATING FROM THIRD PARTIES OR LINKS TO WEBSITES AND FEATURES IN BANNERS OR OTHER ADVERTISING. SUCH EXTERNAL LINKS ARE NOT INVESTIGATED, MONITORED, OR CHECKED FOR ACCURACY, ADEQUACY, VALIDITY, RELIABILITY, AVAILABILITY OR COMPLETENESS BY US.*

*WE DO NOT WARRANT, ENDORSE, GUARANTEE, OR ASSUME RESPONSIBILITY FOR THE ACCURACY OR RELIABILITY OF ANY INFORMATION OFFERED BY THIRD-PARTY WEBSITES LINKED THROUGH THE SITE OR ANY WEBSITE OR FEATURE LINKED IN ANY BANNER OR OTHER ADVERTISING.*


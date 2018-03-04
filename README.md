# Smart-Parko
IoT Based smart Parking slot finder



CHAPTER 1
INTRODUCTION

In the urban mobility sector, parking place an important role whether parking at work, at home, in the city center or at the outskirts. Making parking a part of city life and connect flowing traffic with stationary traffic.So, here we introducing a smart parking system. Smart parking is a parking strategy that combines technology and human innovation in an effort to users few resources as possible such as fuel, time and space to achieve faster, easier and denser parking of vehicles for the majority of time they remain idle.
Smart parking and its sister approach, intelligent transportation, are based on the fundamental ecological principle that we are all connected. Parking and transportation are both essential in the movement of people and goods. The smart parking and intelligent Transportation vision and overlapping technologies are steadily melding into one integrated stream.
Our project is IoT based smart parking slot finder “SMART-PARKO”. By using an android mobile app we can find the parking space. Through this, user can easily find out the free slot in the metro politian city. The App Smart parko is an easy to install, simple to use app that the driver install on their smart phone. The driver uses app smart parko to locate best available parking spaces. Once a space is chosen, the driver is directed to their space with smart parko app is clear, precise directions which are GPS controlled. 






CHAPTER 2
LITERATURE REVIEW

In some studies [1], the authors proposed a new algorithm for treatment planning in real-time parking. First, they used an algorithm to schedule the online problem of a parking system into an offline problem. Second, they set up a mathematical model describing the offline problem as a linear problem. Third, they designed an algorithm to solve this linear problem. Finally, they evaluated the proposed algorithm using experimental simulations of the system. The experimental results indicated timely and efficient performance. However, these papers do not mention the resource reservation mechanism (all parking requirements are derived immediately and are placed in the queue), the mechanism for assessing the resources system, the mechanism to guide vehicles to the parking space, the mechanism for handling situations when the request for service is denied and do not calculate the average waiting time and average total time that each vehicle spends on the system.
In another study [2], the authors propose an SPS based on the integration of UHF frequency, RFID and IEEE 802.15.4 Wireless Sensor Network technologies. This system can collect information about the state of occupancy of the car parks, and can direct drivers to the nearest vacant parking spot by using a software application. However, in this work, the authors have no mathematical equations for the system architecture and do not create a large-scale parking system. The results of this paper only implement the proposed architecture; they do not mention the performance of the parking system. Hsu et al. [3] proposed an innovative system including the parking guidance service. A parking space can be reserved by a smartphone via Internet access. Upon entering the car park, the reserved parking space will be displayed on a small map using wireless transmission for vehicles under the dedicated short-range communication protocol DSRC. An inertial navigation system (INS) is implemented to guide the vehicle to the reserved space. The system will periodically update the status of the parking space in real time to help ensure system accuracy. System performance is measured through the accuracy of the inertial navigation systems run in an indoor environment, and the system implementation is evaluated by considering the accuracy of the GPS. In this paper, the authors have not evaluated the performance of the parking services, they do not provide any mathematical model of the system, and do not consider the waiting time of each vehicle for service.
Other researchers have designed architecture for parking management in smart cities [4]. They proposed intelligent parking assistant (IPA) architecture aimed at overcoming current public parking management solutions. This architecture provides drivers with information about on-street parking stall availability and allow drivers to reserve the most convenient parking stall at their destination before their departure. They use RFID technology in this system. When a car parks or leaves the IPA parking spot, the RFID reader and the magnetic loop detect the action and send this information to the unit controller to update the information on the car park status. This study uses only some simple mathematical equations for the system architecture and does not create a large-scale parking system. In other works, authors have designed and implemented an SPS [5] to solve the parking problem. A part of this system is implemented in the Zigbee network which sends urgent information to a PC through a coordinator and then updates the database. The application layer can quickly pass the parking information over the Internet, and use the advantages of a web service to gather all the scattered parking information for the convenience of those who want to find a parking space. This paper simply reports the design and implementation of an SPS and does not evaluate the system performance. 
Bonde et al.  aimed to automate the car and the car parking. The paper discusses a project which presents a miniature model of an automated car parking system that can regulate and manage the number of cars that can be parked in a given area at any given time based on the availability of parking spaces. The automated parking method allows the parking and exiting of cars using sensing devices. Entry to or exit from the car park is commanded by an Android based application. The difference between the Bonde system and the other existing systems is that the authors were aiming to make the system as little human dependent as possible by automating the cars as well as the entire car park; on the other hand, most existing systems require human intervention (the car owner or other) to park the car. 
Lambrinos and Dosis [6] described a new SPS architecture based on the Internet of Things technology. The architecture of this system consists of a Zigbee Wireless Sensor Network (WSN), an IoT middleware layer and a front-end layer as the final user interface that provides data reporting to the user. However, there are disadvantage as it does not use a suitable application protocol for the transfer of data from the WSN to the server, such as the constrained application protocol (CoAP), there is no mathematical model for the system operations, and there is no system performance evaluation.














CHAPTER 3
PROPOSED METHOD

3.1 Overview of project

Our idea focuses on use of Internet of Things and OpenCV as the image processing tool to figure out the availability of vacant and filled parking slots upon a request by the user from android application and getting acknowledge of the same if the current one is occupied. It allows drivers to effectively find and reserve vacant parking slots in a parking lot using IoT with slot allocation method.
Project have hardware and software parts. In hardware parts it includes a Raspberry Pi as processor and Pi cam for capturing parking slots vacant spaces, and on software we have an Android app, which the main operating part of this system. It will show all available near by parking slots and navigate the user to that slots.This is the basic things what our project does.  




fig 3.1 : Block Diagram
3.1.1  System Architecture

Architecture of  Parking system as per proposed concept:


Fig 3.2: Architecture of proposed system


3.2  Key elements of this Projects are:
a.Car Detection using Pi cam
b.Image processing
c.Cloud platform
d.User side platform
3.2.a  A Car Detection with Raspberry Pi + Pi Camera
In this project we explore a car counter device using:
OpenCV
A Raspberry Pi 3
Raspberry Pi Camera
The Digital Ocean cloud.

To make the overall procedure simple, we assume that the camera is fixed i.e., it cannot rotate or zoom.
1.Define background image - Take snapshot of the parking space as background image (without having any car parked in the parking lot and marking lines clearly visible).
2.Initialize parking map as rectangles - Do it manually(as we assumed the camera is fixed) or automatically by detecting white marker lines through color or line detection or any other image processing technique.
3.Continuously check for parking status - For each frame of the camera feed, check if parking spaces(marked rectangular positions) are occupied or not by background subtraction method or any other methods.
4.Update status - Update parking status accordingly (as shown in the right window of the video).












3.2.b Image Processing

Image processing is a method to convert an image into digital form and perform some operations on it, in order to get an enhanced image or to extract some useful information from it. It is a type of signal dispensation in which input is image, like video frame or photograph and output may be image or characteristics associated with that image. Usually Image Processing system includes treating images as two dimensional signals while applying already set signal processing methods to them. 


Fig 3.3 : Image Processing

3.2.b.1.Fundamental Steps of Digital Image Processing:

There are some fundamental steps but as they are fundamental, all these steps may have sub-steps. The fundamental steps are described below with a neat diagram.



	Fig 3.4 : Fundamental block diagram of Digital Image Processing
3.2.b.1.1.Image Acquisition:
This is the first step or process of the fundamental steps of digital image processing. Image acquisition could be as simple as being given an image that is already in digital form. Generally, the image acquisition stage involves pre-processing, such as scaling etc.

3.2.b.1.2. Image Enhancement:
Image enhancement is among the simplest and most appealing areas of digital image processing. Basically, the idea behind enhancement techniques is to bring out detail that is obscured, or simply to highlight certain features of interest in an image. Such as, changing brightness & contrast etc.

3.2.b.1.3. Image Restoration:
Image restoration is an area that also deals with improving the appearance of an image. However, unlike enhancement, which is subjective, image restoration is objective, in the sense that restoration techniques tend to be based on mathematical or probabilistic models of image degradation.

3.2.b.1.4. Color Image Processing:
Color image processing is an area that has been gaining its importance because of the significant increase in the use of digital images over the Internet. This may include color modeling and processing in a digital domain etc.

3.2.b.1.5. Wavelets and Multi-Resolution Processing:
Wavelets are the foundation for representing images in various degrees of resolution. Images subdivision successively into smaller regions for data compression and for pyramidal representation.

3.2.b.1.6. Compression:
Compression deals with techniques for reducing the storage required to save an image or the bandwidth to transmit it. Particularly in the uses of internet it is very much necessary to compress data.

3.2.b.1.7. Morphological Processing:
Morphological processing deals with tools for extracting image components that are useful in the representation and description of shape.

3.2.b.1.8. Segmentation:
Segmentation procedures partition an image into its constituent parts or objects. In general, autonomous segmentation is one of the most difficult tasks in digital image processing. A rugged segmentation procedure brings the process a long way toward successful solution of imaging problems that require objects to be identified individually.

3.2.b.1.9. Representation and Description:
Representation and description almost always follow the output of a segmentation stage, which usually is raw pixel data, constituting either the boundary of a region or all the points in the region itself. Choosing a representation is only part of the solution for transforming raw data into a form suitable for subsequent computer processing. Description deals with extracting attributes that result in some quantitative information of interest or are basic for differentiating one class of objects from another.

3.2.b.1.10. Object recognition:
Recognition is the process that assigns a label, such as,  “vehicle” to an object based on its descriptors.
3.2.b.1.11. Knowledge Base:
Knowledge may be as simple as detailing regions of an image where the information of interest is known to be located, thus limiting the search that has to be conducted in seeking that information. The knowledge base also can be quite complex, such as an interrelated list of all major possible defects in a materials inspection problem or an image database containing high-resolution satellite images of a region in connection with change-detection applications.

3.2.C Cloud platform



Fig 3.5: Work-flow of Cloud platform
MQTT MQ Telemetry Transport: MQTT described as Machine to Machine (M2M)/ IoT connectivity protocol. This protocol is light weighted; the protocol can be supported by smallest measuring and monitoring device. MQTT is publish-subscribe messaging transport protocol that helps to connect physical devices to the servers. There are many challenges of connecting sensors, actuators, mobile phones, tablets and desktops with established software technologies, MQTT designed to overcome these problems. The MQTT messages are delivered asynchronously through publish-subscribe architecture. It works by exchanging a series of MQTT control packets in a defined way. 
The control packet sent over the network has a specific purpose and every bit in the packet is carefully crafted to reduce the data transmission an MQTT topology has an MQTT server and an MQTT client. MQTT client and server are communicating through different control packets. MQTT control packet headers are kept as small as possible. An individual MQTT control packet divides into three parts, a fixed header, a variable header, and the payload. Fixed header for each MQTT control packet is 2 bytes. Some of the control packets have variable headers and payload. A variable header contains packet identifier when it is used by the control packet. The packets can be attached payload up to 256MB.
3.2.D  User Side Platform
                                    Fig 3.6: Data flow diagram of User Side Platform
User Side Platform section, the user will open the app, he will search for the nearest parking area, it checks for availability of free parking lot. 162 PROCEEDINGS OF RICE. GOPESHWAR, 2017 If the parking lot is empty, the user will book the lot. After that he chooses for payment option then user id and payment information will be generated. The information about user and payment is updated in the database. The user will park the vehicle, and the timer will start when the user leaves the space timer will be stopped. The time is calculated, if the time exceeds than allotted time then the user have to pay once again and the database is updated that slot is free for parking.
3.3 Open CV
OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. Originally developed by Intel, it was later supported by Willow Garage and is now maintained by Itseez.The library is cross-platform and free for use under the open-source BSD license. OpenCV supports the Deep  Learning frameworks TensorFlow, Torch/PyTorch and Caffe. It has C++, C, Python and Java interfaces and supports Windows, Linux, Mac OS, iOS and Android. OpenCV was designed for computational efficiency and with a strong focus on real-time applications. Written in optimized C/C++, the library can take advantage of multi-core processing. Enabled with OpenCL, it can take advantage of the hardware acceleration of the underlying heterogeneous compute platform.
Adopted all around the world, OpenCV has more than 47 thousand people of user community and estimated number of downloads exceeding 14 million. Usage ranges from interactive art, to mines inspection, stitching maps on the web or through advanced robotics.
3.3.1  Features:

i.Image data manipulation (allocation, release, copying, setting, conversion).
ii.Image and video I/O (file and camera based input, image/video file output). 
iii.Matrix and vector manipulation and linear algebra routines. 
iv.Various dynamic data structures (lists, queues, sets, trees, graphs). 
v.Basic image processing (filtering, edge detection, corner detection, sampling and interpolation, color conversion, morphological operations, histograms, image pyramids). 
vi.Structural analysis (connected components, contour processing, distance transform, various moments, template matching, Hough transform, polygonal approximation, line fitting, ellipse fitting, Delaunay triangulation). 
vii.Camera calibration (finding and tracking calibration patterns, calibration, fundamental matrix estimation, homography estimation, stereo correspondence). … Motion analysis (optical flow, motion segmentation, tracking). 
viii.Object recognition (eigen-methods, HMM). … Basic GUI (display image/video, keyboard and mouse handling, scroll-bars). … Image labeling (line, conic, polygon, text drawing).

3.3.2  Image Processing using open CV

 	OpenCV is pretty powerful but tedious to learn. Once you are comfortable with basics the curve is upwards. The more you program the better you understand. Also the best part is its open source and free. There are tons of resources available on the internet to learn.
MATLAB is relatively easy to learn since the libraries and tool boxes have in built features. But it comes with a cost. If you are a student thats fine, you can purchase the software for under 150$. But if you want to learn how the process actually implement, you should start with OpenCV. Understanding what goes behind the program is very important to get a grip in computer vision and image processing.


Fig 3.7 : OpenCV
	
3.3.3  How to Use Background Subtraction Methods
Background subtraction (BS) is a common and widely used technique for generating a foreground mask (namely, a binary image containing the pixels belonging to moving objects in the scene) by using static cameras.
As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene.



Fig 3.8: Example for Background subtraction
Background modelling consists of two main steps:
	1. Background Initialization
	2. Background Update.
In the first step, an initial model of the background is computed, while in the second step that model is updated in order to adapt to possible changes in the scene.








CHAPTER 4
SYSTEM REQUIREMENTS

4.1 Things Used in this Project
1.Hardware Components:
I.Raspberry Pi 3
II.Pi Camera
2.Software Application and Online services:
I. OpenCV
II.Node.js wrapper for OpenCV
III.Digital Ocean Cloud Service
IV.Android studio
V.Google Cloud
4.1.I Raspberry Pi
     	The Raspberry Pi is a low cost, credit-card sized computer that plugs into a computer monitor or TV, and uses a standard keyboard and mouse. It is a capable little device that enables people of all ages to explore computing, and to learn how to program in languages like Scratch and Python. It’s capable of doing everything you’d expect a desktop computer to do, from browsing the internet and playing high-definition video, to making spreadsheets, word-processing, and playing games.What’s more, the Raspberry Pi  has the ability to interact with the outside world, and has been used in a wide array of digital maker projects, from music machines and parent detectors to weather stations and tweeting birdhouses with infra-red cameras. We want to see the Raspberry Pi being used by kids all over the world to learn to program and understand how computers work.




4 . 1  Raspberry Pi 3

Fig 4.1: Raspberry Pi 3
Raspberry Pi is well known as the perfect board for learning, coding, and creating your own projects. In celebration of The Raspberry Pi Foundation fourth birthday, Raspberry Pi 3 is released. The Raspberry Pi 3 has included integrated 802.11 b/g/n wireless LAN, Bluetooth Classical and LE. You didn’t need additional peripherals to make it wireless. It is 10x the performance of Raspberry Pi 1. What’s more, it has complete compatibility with Raspberry Pi 2, which means almost all the previous Raspberry Pi 2 accessories are compatible with Raspberry Pi 3.The Raspberry Pi 3 Model B features a quad-core 64-bit ARM Cortex A53 clocked at 1.2 GHz. This puts the Pi 3 roughly 50% faster than the Pi 2. Compared to the Pi 2, the RAM remains the same – 1GB of LPDDR2-900 SDRAM, and the graphics capabilities, provided by the VideoCore IV GPU, are the same as they ever were. As the leaked FCC docs will tell you, the Pi 3 now includes on-board 802.11n WiFi and Bluetooth 4.0. WiFi, wireless keyboards, and wireless mice now work out of the box.

                                                                                                                  


4.1.II  Pi camera
The Raspberry Pi Camera Board v2 is a high quality 8 megapixel Sony IMX219 image sensor custom designed add-on board for Raspberry Pi, featuring a fixed focus lens. It's capable of 3280 x 2464 pixel static images, and also supports 1080p30, 720p60, and 640x480p90 video. It attaches to the Pi by way of one of the small sockets on the board's upper surface and uses the dedicated CSi interface, designed especially for interfacing to cameras.The camera module is very popular in home security applications, and in wildlife camera traps. You can also use it to take snapshots. 


Fig 4.2: Pi Camera
4.2.1 Features
5MP sensor
Wider image, capable of 2592x1944 stills, 1080p30 video
1080p video supported
CSI
Size: 25 x 20 x 9 mm
4.2.II  Node.js wrapper for OpenCV
OpenCV bindings for Node.js. OpenCV is the defacto computer vision library - by interfacing with it natively in node, we get powerful real time vision in is. People are using node-opencv to fly control quadrocoptors, detect faces from webcam images and annotate video streams. 

Fig 4.3 : Node JS
4.3 IoT Cloud 
The platform is built to take in the massive volumes of data generated by devices, sensors, websites, applications, customers and partners and intimate actions for real-time responses. For example, wind turbines could adjust their behaviour based on current weather data; airline passengers whose connecting flights are delayed or cancelled could be rebooked before the planes they are on have landed.
4.3.1 Digital Ocean

Fig 5.4 : Digital ocean cloud
DigitalOcean is a simple and robust cloud computing platform, designed for developers. Digital Ocean tries to offer the best of all worlds with its simple VPS hosting. It includes pre-configured web app images for a taste of shared hosting's simplicity, per-hour pricing like cloud computing services, while still letting you run the Linux distro and software you want on a virtual private server. And it's cheap enough to easily start a test server for a new site whenever you need.

4.4 Android Application “SMART-PARKO”

An android application named “SMART-PARKO” is used in this project. The output of project is displayed out to android app. It got two main screens. In first screen the App will switch on GPS and find users position and display Available nearby parking slots.
Smart Parko takes parking into the digital era, the application is a platform which aggregate all the available parking lots within the cities. The drivers can find the parking spaces in a hassle-free way. It offers different types of parking spaces from private car parks, public car parks to metro station. The quickest and simplest way for drivers to find and book parking, wherever and whenever they need it. More and more new spaces are being added!


Fig 4.5: Android application



4.4.1. Features available in Android App :
1.Find parking spaces near to the user location (GPS) or by searching the desired space.
2. View the live availability of the parking spots for selected parking spaces.
3. View the amount for the selected period for selected parking spaces.

4.5.Android studio

Android Studio is the official integrated development environment (IDE) for Google's Android operating system, built on JetBrains' IntelliJ IDEA software and designed specifically for Android development. It is available for download on Windows, macOS and Linux based operating systems. It is a replacement for the Eclipse Android Development Tools (ADT) as primary IDE for native Android application development.

4.5.1.Features
The following features are provided in the current stable version:

Gradle-based build support
Android-specific refactoring and quick fixes
Lint tools to catch performance, usability, version compatibility and other problems
ProGuard integration and app-signing capabilities
Template-based wizards to create common Android designs and components
A rich layout editor that allows users to drag-and-drop UI components, option to preview layouts on multiple screen configurations
Support for building Android Wear apps
Built-in support for Google Cloud Platform, enabling integration with Firebase Cloud Messaging (Earlier 'Google Cloud Messaging') and Google App Engine
Android Virtual Device (Emulator) to run and debug apps in the Android studio.
Android Studio supports all the same programming languages of IntelliJ, and PyCharm e.g. Python, and Kotlin; and Android Studio 3.0 supports "Java 7 language features and a subset of Java 8 language features that vary by platform version." External projects backport some Java 9 features.

4.6. Google Cloud Functions and Firebase

            Google Cloud Functions is Google's serverless compute solution for creating event-driven applications. It is a joint product between the Google Cloud Platform team and the Firebase team.For Google Cloud Platform developers, Cloud Functions serve as a connective layer allowing you to weave logic between Google Cloud Platform (GCP) services by listening for and responding to events.
             For Firebase developers, Cloud Functions for Firebase provides a way to extend the behavior of Firebase and integrate Firebase features through the addition of server-side code.Both solutions provide fast and reliable execution of functions in a fully managed environment where there's no need for you to worry about managing any servers or provisioning any infrastructure.

4.6.1Cloud Functions for Firebase
             You should use Cloud Functions for Firebase if you're a developer building a mobile or mobile web app. Firebase gives mobile developers access to a complete range of fully managed mobile-centric services including analytics, authentication and Realtime Database. Cloud Functions rounds out the offering by providing a way to extend and connect the behavior of Firebase features through the addition of server-side code.
             Firebase developers can easily integrate with external services for tasks like processing payments and sending SMS messages. Also, developers can include custom logic that is either too heavyweight for a mobile device, or which needs to be secured on a server. See What Can I Do with Cloud Functions? to learn more about typical integration use cases. For developers that need a more full-featured backend, Cloud Functions provides a gateway to the powerful capabilities in Google Cloud Platform.

4.6.2.Cloud Functions for Firebase is optimized for Firebase developers:

Firebase SDK to configure your functions through code
Integrated with Firebase Console and Firebase CLI
The same triggers as Google Cloud Functions, plus Firebase Realtime Database, Firebase Authentication, and Firebase Analytics triggers
Cloud Functions for Google Cloud Platform

            Developers can connect and extend GCP services by writing code in the form of a Cloud Function. Cloud Functions serve as a connective layer allowing you to weave logic between GCP services by listening for and responding to events. With just a few lines of code, developers can enrich their use of GCP services to create higher level combinations without needing to provision or manage servers.
            
            
4.6.3.Known limitations on interoperability
            There are still some areas where Google Cloud Functions and the Firebase SDK for Cloud Functions do not have full interoperability:Cloud Functions written using the Firebase SDK for Cloud Functions can't be deployed using the gcloud command-line tool, and vice-versa.












CONCLUSION

The concept of Smart Cities have always been a dream for humanity. Since the past couple of years large advancements have been made in making smart cities a reality. The growth of Internet of Things and Cloud technologies have give rise to new possibilities in terms of smart cities. Smart parking facilities and traffic management systems have always been at the core of constructing smart cities. In this paper, we address the issue of parking and present an IoT based Cloud integrated smart parking system. The system that we propose provides real time information regarding availability of parking slots in a parking area. Users from remote locations could book a parking slot for them by the use of our mobile application. The efforts made in this paper are indented to improve the parking facilities of a city and thereby aiming to enhance the quality of life of the peoples.


REFERENCES

[1]
	Y. Geng, C. G. Cassandras, "A new ‘smart parking’ system based on optimal resource allocation and reservations", Proc. 14th Int. IEEE Conf. Intell. Transp. Syst. (ITSC), pp. 979-984, Oct. 2011.

[2]	Y. Geng, C. G. Cassandras, "New ‘smart parking’ system based on resource allocation and reservations", IEEE Trans. Intell. Transp. Syst., vol. 14, pp. 1129-1139, Sep. 2013.

[3]	 X. Zhao, K. Zhao, F. Hai, "An algorithm of parking planning for smart parking system", Proc. 11th World Congr. Intell. Control Autom. (WCICA), pp. 4965-4969, 2014.

[4]	L. Mainetti, L. Palano, L. Patrono, M. L. Stefanizzi, R. Vergallo, "Integration of RFID and WSN technologies in a smart parking system", Proc. 22nd Int. Conf. Softw. Telecommun. Comput. Netw. (SoftCOM), pp. 104-110, 2014. 

[5]	 C. W. Hsu, M. H. Shih, H. Y. Huang, Y. C. Shiue, S. C. Huang, "Verification of smart guiding system to search for parking space via DSRC communication", Proc. 12th Int. Conf. ITS Telecommun. (ITST), pp. 77-81, 2012.
	
[6]	 R. E. Barone, T. Giuffrè, S. M. Siniscalchi, M. A. Morgano, G. Tesoriere, "Architecture for parking management in smart cities", IET Intell. Transp. Syst., vol. 8, no. 5, pp. 445-452, 2014.

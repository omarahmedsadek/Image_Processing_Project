# Road Traffic Detection Lights (Image processing project)

Requirements & Installation
------
- Python 3.5+ - Please see `python_req.txt` to know python modules are required
&nbsp;
- XAMPP 3.1^ (PHP localhost) for running the app
you can download it from this link: [https://www.apachefriends.org/download.html](https://www.apachefriends.org/download.html)
&nbsp;
you can also see this tutorial: [https://www.youtube.com/watch?v=k9em7Ey00xQ](https://www.youtube.com/watch?v=k9em7Ey00xQ)
&nbsp;

Steps of Running the Project
------
-Please watch the demo video first
-Open the folder named Project
-Open cmd  window in that destination
-Copy this "python -m http.server 1337" in the cmd window and press enter
-Open this link "http://localhost:1337/index.html" this will get u the web app
-Run the file named Final.py
-Select the Video from a folder named Traffic Lights Video Used In Testing

---

Project description
------
Today’s technology development has speed up our life so that everything around us gets smarter, integrable, faster and sometimes more complex or easier depending on the goal to be achieved.

Nowadays, Image processing and computer vision involved in many real and daily life applications.
One of that applications which we will consider as our project is used to solve a daily issue exits in our life. The Road Traffic Detection and how to make the traffic lights more accurate and precise?

Every time you went to a road to go to somewhere heir will be of course a traffic lights with an officer to handle it or it maybe be a time automatic traffic lights which swap between the red and the green light after a constant amount of time lets say 60 seconds, but in our application the traffic lights only will depends on the amount of cars now detected by a camera in the street, so les say the the number of cars = x so if the number of cars now exceeds x the light will go green till the now of cars be less than y for an example.

Hence, we concern in presenting an application that will be capable of providing you with information about the traficc road situaion and how the traffic lights is dealing with the traffic.
  - the number of cars in the road right now?
  - the time taken for the traffic lights to swap the green and the red light and vice verse.


---


Project Impact
------
> On individuals
-	Optimization for driver time, efforts and resources – e.g. car fuel.
<br/> Through finding the suitable traffic light for the road traffic right now not a consant delay of time as the normal digital traffic lights. 
> On community
-	Traffic jam reduction.
  <br/>As, the number of the cars in the streets will be handled by the Road Traffic Detection Lights
> On Environment
-	The other plus side is the environmental impact.
  <br/>The less drivers idle, waiting inthe traffic jam, the less the negative impact on the environment.
  <br/>As, the decrement in number of cars waitting in the roads will also decrease the amount of vehicle oil burnt and by turn reduces the global ecological footprint.

---

Algorithm Procedure
------
The implementation of the desired project through the main following points:
>1. DETERMINE THE NUMBER OF CARS NOW IN THE ROAD

The configuration of the cars in an image or video frame can be achieved using:
  -	Edge detection using canny functions to get the benefits of the moving cars inte street then Hough the outer lines               of the car  to specifically determine the start and the end of the car in the image
  -	Then, followed by drawing contour for each car  and numbering them. So that, the numbers can be used further in               the reset of the algorithm
  -           Determine the variable x and the variable  y in which the traffic light will swap inbetween the red and the green               lights.
  -           Take the  right action depends on the current number of ha cars now in the roads.
---

Note
------
Please keep in mind that the code was compiled at the beginning without the use `Github`
and as a team we finally compiled the code with each and every one of us has his
own mark `(at comments)` on the part he did in the project.

---

Shareholders
------
- [https://github.com/olgarose/ParkingLot](ParkingLot)

License
------
MIT

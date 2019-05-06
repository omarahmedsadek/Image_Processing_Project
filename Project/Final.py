import cv2
import numpy as np
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from matplotlib import pyplot as plt
#####

# processing
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))
bg1 = cv2.createBackgroundSubtractorKNN() #Detect the background by subtracting 3 frames

#Select a video from fileOpen GUi
root = tk.Tk()
root.withdraw()
vid = filedialog.askopenfilename()
cap = cv2.VideoCapture(vid)

# mouse callback function : collect the points when the mouse is pressed
def draw_circle(event,a,b,flags,param):
    global xy,t
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(a,b),2,(0,0,255),1) #draw a circle in the clicked position
        xy.append((a,b))                    #get the position which we clicked
    elif event == cv2.EVENT_RBUTTONDOWN:    #MouseRightClick to end
        t = 0

#create mask
def mask(image):
    global xy,t,img
    xy = []                                 #array to save the points
    t = -1

    # Create a window and bind the function to window
    cv2.namedWindow('image')
    cv2.moveWindow('image', 50,50)
    cv2.setMouseCallback('image',draw_circle)
    img = image.copy()
    while(1):
        cv2.imshow('image',img)
        if (cv2.waitKey(25) & 0xFF == 27) | (t==0):
            break

    fgmask = bg1.apply(image)
    black = np.full(fgmask.shape,0,dtype='uint8')  #create a black image
    cv2.fillPoly(black, [np.array(xy)], 255)       #create a white pollygon on the black image
    cimg = cv2.bitwise_and(img,img,mask = black)   #Anding the image with the mask
    cv2.destroyWindow('image')
    return cimg , black                            #return the masked image and the mask


def remask(frame):
    global cimg,black
    cimg,black = mask(frame)
    cv2.imshow('Mask',cimg)
    while(1):
        k = cv2.waitKey(1) & 0xFF
        if k == ord('r'):
                cimg,black = mask(frame)
                cv2.imshow('Mask',cimg)
        elif k == 13:
            break
    cv2.destroyWindow('Mask')

#create messageBox
messagebox.showinfo( "","please select the contour of the desired road")

#First time masking
ret, frame = cap.read()
cimg,black = mask(frame)
cv2.imshow('Mask',cimg)
cv2.moveWindow('Mask', 50,50)
while(1):
        k = cv2.waitKey(1) & 0xFF
        if k == ord('r'):                   #click r to remask
                cimg,black = mask(frame)
                cv2.imshow('Mask',cimg)
        elif k == 13:                       #click ENTER to apply mask
            break
cv2.destroyWindow('Mask')

#create button doing =>   remask(frame)
red = cv2.imread("r.jpg")
green = cv2.imread("g.jpg")

q=-1
while True:                    #read until video is completed

    q+=1
    ret, frame = cap.read()    #capture frame by frame

    frame2 = frame.copy()
    fgmask = bg1.apply(frame)       #apply the subtractor to get the background
    ret,fgmask = cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)    #get the moving objects
    opened = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel2)
    closed2 = cv2.bitwise_and(closed, closed, mask = black)         #Anding the closed image with the mask
    num, labels, stats, centroids = cv2.connectedComponentsWithStats(closed2)
    stats = stats[1:num-1]
    if q < 3 :
        pass
    else :
    	x = stats[:,0]                      #left point of the car
    	y = stats[:,1]                      #top point of the car
    	w = stats[:,2]                      #width of the car
    	h = stats[:,3]                      #height of the car
    	a = stats[:,4]                      #area of the car
    	me = int(cv2.mean(a)[0])            #mean of the areas
    	font = cv2.FONT_HERSHEY_SIMPLEX
    	i = -1
    	counter = 0
    	while i < num-3:
    	    	i += 1
    	    	if (a[i]>0.4*me) &(a[i]<15*me) :
    	    		counter += 1
    	    		i0 = str(i)
	    	    	h0=int(h[i])
    		    	w0=int(w[i])
    	    		x0=int(x[i])
	    	    	y0=int(y[i])
    		    	cv2.rectangle(frame,(x0,y0),(x0+w0,y0+h0),(0,255,0),2)
    	    		cv2.putText(frame, i0, (x0,y0), font, 0.3,(0,0,0),1,cv2.LINE_AA)
                        text_file = open("counter.txt", "w")
                        text_file.write(str(counter))
                        text_file.close()
    	cv2.putText(frame,  str(counter), (frame.shape[1]-50,50), font, 0.8,(0,0,0),1,cv2.LINE_AA)
    	cimg = cv2.bitwise_and(frame2,frame2,mask = black)
    	cv2.imshow('MainWindow',np.full((800,1920),255,dtype='uint8'))
    	cv2.moveWindow('MainWindow', 0,0)
    	if counter > 3 : cv2.imshow('Traffic',red)
    	else : cv2.imshow('Traffic',green)
    	cv2.moveWindow('Traffic', 1380,670)
    	thre=cv2.resize( fgmask,(640,360), interpolation= cv2.INTER_NEAREST)
    	cv2.imshow('Thresholded',thre)
    	cv2.moveWindow('Thresholded', 20,40)
    	clo=cv2.resize( closed, (640,360), interpolation= cv2.INTER_NEAREST)
    	cv2.imshow('closed',clo)
    	cv2.moveWindow('closed', 20,430)
    	clo2=cv2.resize( closed2, (640,360), interpolation= cv2.INTER_NEAREST)
    	cv2.imshow('closed2',clo2)
    	cv2.moveWindow('closed2', 720,430)
    	ci=cv2.resize( cimg, (640,360), interpolation= cv2.INTER_NEAREST)
    	cv2.imshow('Mask',ci)
    	cv2.moveWindow('Mask', 720,40)
    	im=cv2.resize( frame, (640,360), interpolation= cv2.INTER_NEAREST)
    	cv2.imshow('image',im)
    	cv2.moveWindow('image', 370,270)
    	if cv2.waitKey(25) & 0xFF == ord('q'):break


cap.release()
cv2.destroyAllWindows()


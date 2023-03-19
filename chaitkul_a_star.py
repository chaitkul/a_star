# Import the necessary libraries

import numpy as np
import math
import heapq
import cv2

def move_center(current_node, cost=1):  
    """Function to move the robot with a step size equal to the radius and orientation same as the start theta.

    Args:
        current_node (tuple): The node that is currently being explored
        cost (int): The cost to move the robot with step size equal to radius. Defaults to 1.

    Returns:
        tuple: (child node, cost)
    """    
    x, y, theta = current_node
    child_node = (round(x + radius * np.cos(np.deg2rad(theta))), round(y + radius * np.sin(np.deg2rad(theta))), theta)
    if 0<=child_node[0]<=600 and 0<=child_node[1]<=250 and 0<=child_node[2]<=360:
        return child_node, cost
    else:
        return None, None

def move_up_30(current_node, cost=1):   
    """Function to move the robot with a step size equal to the radius and orientation 30 degrees more than that of the start.

    Args:
        current_node (tuple): The node that is currently being explored
        cost (int): The cost to move the robot with step size equal to radius. Defaults to 1.

    Returns:
        tuple: (child node, cost)  
    """    
    x, y, theta = current_node
    child_node = (round(x + radius * np.cos(np.deg2rad(theta + 30))), round(y + radius * np.sin(np.deg2rad(theta + 30))), (theta-30))
    if 0<=child_node[0]<=600 and 0<=child_node[1]<=250 and 0<=child_node[2]<=360:
        return child_node, cost
    else:
        return None, None

def move_up_60(current_node, cost=1):   # 
    """Function to move the robot with a step size equal to the radius and orientation 60 degrees more than that of the start.

    Args:
        current_node (tuple): The node that is currently being explored
        cost (int): The cost to move the robot with step size equal to radius. Defaults to 1.

    Returns:
        tuple: (child node, cost)
    """    
    x, y, theta = current_node
    child_node = (round(x + radius * np.cos(np.deg2rad(theta + 60))), round(y + radius * np.sin(np.deg2rad(theta + 60))), (theta-60))
    if 0<=child_node[0]<=600 and 0<=child_node[1]<=250 and 0<=child_node[2]<=360:
        return child_node, cost
    else:
        return None, None
    
def move_down_30(current_node, cost=1): 
    """Function to move the robot with a step size equal to the radius and orientation 30 degrees less than that of the start.

    Args:
        current_node (tuple): The node that is currently being explored
        cost (int): The cost to move the robot with step size equal to radius. Defaults to 1.

    Returns:
        tuple: (child node, cost)    
    """    
    x, y, theta = current_node
    child_node = (round(x + radius * np.cos(np.deg2rad(theta - 30))), round(y + radius * np.sin(np.deg2rad(theta - 30))), (theta+30))
    if 0<=child_node[0]<=600 and 0<=child_node[1]<=250 and 0<=child_node[2]<=360:
        return child_node, cost
    else:
        return None, None
    
def move_down_60(current_node, cost=1): 
    """Function to move the robot with a step size equal to the radius and orientation 60 degrees less than that oof the start.

    Args:
        current_node (tuple): The node that is currently being explored
        cost (int): The cost to move the robot with step size equal to radius. Defaults to 1.

    Returns:
        tuple: (child node, cost)
    """    
    x, y, theta = current_node
    child_node = (round(x + radius * np.cos(np.deg2rad(theta - 60))), round(y + radius * np.sin(np.deg2rad(theta - 60))), (theta+60))
    if 0<=child_node[0]<=600 and 0<=child_node[1]<=250 and 0<=child_node[2]<=360:
        return child_node, cost
    else:
        return None, None
    
def make_canvas():
    """This function creates the map with the obstacles

    Returns:
        tuple: (obstacle, canvas)
    """    
    canvas = np.zeros((250, 600, 3), dtype="uint8")

    blue = (255,0,0)
    red = (0,0,255)

    # Obstacle rectangles

    cv2.rectangle(canvas, (95,0), (155,105), red, thickness=-1)
    cv2.rectangle(canvas, (95,145), (155,250), red, thickness=-1)
    cv2.rectangle(canvas, (100, 0), (150,100), blue, thickness=-1)
    cv2.rectangle(canvas, (100,150), (150,250), blue, thickness=-1)

    # Obstacle triangle

    pt1 = (460,25)
    pt2 = (460,225)
    pt3 = (510,125)
    pt4 = (455,246)
    pt5 = (455,4)
    pt6 = (515,125)

    # Drawing 3 lines to crate a triangle

    cv2.line(canvas, pt1, pt2, blue, 1)
    cv2.line(canvas, pt2, pt3, blue, 1)
    cv2.line(canvas, pt3, pt1, blue, 1)
    cv2.line(canvas, pt4, pt5, red, 1)
    cv2.line(canvas, pt5, pt6, red, 1)
    cv2.line(canvas, pt6, pt4, red, 1)

    # Using the fillPoly function to fill the obstacle space

    points1 = np.array([[455,246],[455,4],[515,125]])
    points1 = points1.reshape((-1,1,2))
    cv2.fillPoly(canvas, [points1], red)

    points2 = np.array([[510,125],[460,225],[460,25]])
    points2 = points2.reshape((-1,1,2))
    cv2.fillPoly(canvas, [points2], blue)

    # Obstacle hexagon

    center = (300,125)
    side_length = 75

    # Drawing six lines to create a hexagon

    pts3 = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = np.pi / 180 * (angle_deg + 90)
        pt = (int(center[0] + side_length * np.cos(angle_rad)),
            int(center[1] + side_length * np.sin(angle_rad)))
        pts3.append(pt)

    for i in range(6):
        cv2.line(canvas, pts3[i], pts3[(i+1)%6], blue, 1)

    center = (300,125)
    side_length = 81

    pts4 = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = np.pi / 180 * (angle_deg + 90)
        pt = (int(center[0] + side_length * np.cos(angle_rad)),
            int(center[1] + side_length * np.sin(angle_rad)))
        pts4.append(pt)

    for i in range(6):
        cv2.line(canvas, pts4[i], pts4[(i+1)%6], red, 1)

    # Using the fillPoly function to fill the obstacle space

    points4 = np.array([[230,85],[230,165],[300,206],[370,165],[370,85],[300,44]])
    points4 = points4.reshape((-1,1,2))
    cv2.fillPoly(canvas, [points4], red)

    points3 = np.array([[300,200],[235,162],[235,87],[300,50],[364,87],[364,162]])
    points3 = points3.reshape((-1,1,2))
    cv2.fillPoly(canvas, [points3], blue)

    # Finding all the nonzero pixels from the canvas and appending them to the list of obstacle points

    obstacle = []
    for y in range(canvas.shape[0]):
        for x in range(canvas.shape[1]):
            if canvas[y,x].any():
                obstacle.append((x,y))

    # Returning the obstacle space and the canvas image

    return obstacle, canvas

obstacle, canvas = make_canvas()

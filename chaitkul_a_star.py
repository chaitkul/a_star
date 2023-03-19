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
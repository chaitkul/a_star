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

# Function to get the user input

def user_input():
    """Takes start and goal coordinates as user input. Also gets the step size of the robot

    Returns:
        tuple: (start_node, goal_node, radius)
    """    
    valid_input = False
    while valid_input == False:
        start_x = int(input("Enter X coordinate of start node: "))  # X coordinate of start node
        start_y = int(input("Enter Y coordinate of start node: "))  # Y coordinate of start node
        start_theta = int(input("Enter the theta at the start node from 0 to 330 in multiples of 30: "))    # Angle at the start node
        goal_x = int(input("Enter X coordinate of goal node: "))    # X coordinate of goal node
        goal_y = int(input("Enter Y coordinate of goal node: "))    # Y coordinate of goal node
        goal_theta = int(input("Enter the theta at the goal node from 0 to 330 in multiples of 30: "))      # Angle at the goal node
        radius = int(input("Enter the step size for the vector between 1 and 10: "))    # Step size of the robot

        
        start_node = (start_x,start_y,start_theta)
        goal_node = (goal_x,goal_y,goal_theta)
    
        if start_node in obstacle:
            print(f"Start node {start_node} is in obstacle space. Enter another node.") # Error message if start node is in obstacle space
            valid_input = False
        elif goal_node in obstacle:
            print(f"Goal node {goal_node} is in obstacle space. Enter another node") # Error message if goal node is in obstacle space
            valid_input = False
        elif start_x<0 or start_x>600 or goal_x<0 or goal_x>600 or start_y<0 or start_y>250 or goal_y<0 or goal_y>250 or start_theta<0 or start_theta>=360 or goal_theta<0 or goal_theta>=360:
            print("The coordinates you entered are beyond the scope of the map. Enter valid start and goal coordinates.") # Error message if start or goal node is beyond the scope of the map
            valid_input = False
        elif radius<1 or radius>10:
            valid_input = False
            print("Enter a step size between 1 and 10.")    # Error message if the size is not withiin the specified limit
        elif start_node not in obstacle and goal_node not in obstacle:
            valid_input = True
            break
        
    return start_node, goal_node, radius

start_node, goal_node, radius = user_input()
closed_dict = {}
open_list = []

theta = start_node[2]
current_node = start_node
x = radius * np.cos(np.deg2rad(theta))
y = radius * np.sin(np.deg2rad(theta))

# Action set to move the robot 

action_set = [move_center, move_up_30, move_up_60, move_down_30, move_down_60]

V = np.empty((1201,501,13), dtype=object)
for x in range(1201):
    for y in range(501):
        for theta in range(13):
            V[x][y][theta] = 0

xg = goal_node[0]
yg = goal_node[1]

# Setting the distance and angle threshold

threshold_dist = 0.5
threshold_angle = 30
xc = current_node[0]
yc = current_node[1]
cost_to_go = math.sqrt((xg - current_node[0])**2 + (yg - current_node[1])**2)
heapq.heappush(open_list, (cost_to_go, 0, start_node))
closed_dict[start_node] = (start_node, None, 0 + cost_to_go)
V[int(start_node[0]/threshold_dist)][int(start_node[1]/threshold_dist)][int(start_node[2]/threshold_angle)] = 1

def a_star(start_node, goal_node):
    """A-Star Algorithm to find out the optimal path between start node and goal node.

    Args:
        start_node (tuple): (start_x,start_y,start_theta)
        goal_node (tuple): (goal_x,goal_y,goal_theta)
    """
    while open_list:

        cost_to_go, cost_to_come, current_node = heapq.heappop(open_list)
        if current_node == goal_node:
            print("Goal node reached.")
            break
        elif V[int(current_node[0]/threshold_dist)][int(current_node[1]/threshold_dist)][int(current_node[2]/threshold_angle)] == 1 and closed_dict[current_node][2] < cost_to_come + cost_to_go:
            continue
        for move in action_set:
            child_node, cost = move(current_node)
            if cost is not None:
                cost_to_come += cost
            try:
                if child_node is not None and V[int(child_node[0]/threshold_dist)][int(child_node[1]/threshold_dist)][int(child_node[2]/threshold_angle)] != 1 and (child_node[0],child_node[1]) not in obstacle:
                    cost_to_go = math.sqrt((xg - child_node[0])**2 + (yg - child_node[1])**2)   # Calculating the cost to go the goal node from child node
                    heapq.heappush(open_list, (cost_to_go, cost_to_come, child_node))           # Appending the child node to the open list
                    closed_dict[child_node] = (child_node, current_node, cost_to_come + cost_to_go) # Updating the visited nodes in the dictionary
                    V[int(child_node[0]/threshold_dist)][int(child_node[1]/threshold_dist)][int(child_node[2]/threshold_angle)] = 1 # Storing information to avoid duplicate nodes
                    point1 = (closed_dict[child_node][1][0], closed_dict[child_node][1][1])
                    point2 = (closed_dict[child_node][0][0], closed_dict[child_node][0][1])
                    cv2.arrowedLine(canvas, point1, point2, (0,255,0), 1, tipLength=0.5)    # Plotting the arrowed line for visited nodes
                    canvas_flip = cv2.flip(canvas,0)    # Inverting the y axis since origin is at the bottom left
                    cv2.imshow("canvas", canvas_flip)
                    cv2.waitKey(1)
                elif child_node is not None and V[int(child_node[0]/threshold_dist)][int(child_node[1]/threshold_dist)][int(child_node[2]/threshold_angle)] == 1 and closed_dict[child_node][2] > cost_to_come + cost_to_go and (child_node[0],child_node[1]) not in obstacle:
                    closed_dict[child_node] = (child_node, current_node, cost_to_come + cost_to_go) # Updating the total cost if the node has already been visited
            except:
                pass

    if not open_list:
        print("Goal node cannot be reached.")

              
a_star(start_node, goal_node)
backtrack_dict = {}

# Function to generate path using backtracking

def generate_path(start_node, goal_node):
    """Generates path from the start node to the goal node

    Args:
        start_node (tuple): (start_x,start_y,start_theta)
        goal_node (_type_): (goal_x,goal_y,goal_theta)

    Returns:
        list: backtrack_path
    """    
    backtrack_path = []
    current_node = goal_node
    while closed_dict[current_node][0] != closed_dict[start_node][0]:
        backtrack_path.append((closed_dict[current_node][0], round(closed_dict[current_node][2],1)))
        current_node = closed_dict[current_node][1]
    backtrack_path.append((closed_dict[start_node][0], round(closed_dict[start_node][2],1)))
    backtrack_path.reverse()
    for index, node in enumerate(backtrack_path):
        backtrack_dict[index] = (node)
    
    return backtrack_path

path = generate_path(start_node, goal_node)
print(path) # Printing the backtrack path along with the cost

for key in backtrack_dict:
    try:
        point1 = (backtrack_dict[key][0][0], backtrack_dict[key][0][1])
        point2 = (backtrack_dict[int(key+1)][0][0], backtrack_dict[int(key+1)][0][1])
        cv2.arrowedLine(canvas, point1, point2, (255,255,255),1, tipLength=1) # Plotting the nodes in the path as arrowed lines
        canvas_flip = cv2.flip(canvas,0)    # Inverting the y axis since origin is at the bottom left
        cv2.imshow("canvas", canvas_flip)
        cv2.waitKey(100)
    except:
        pass

print(f"Total cost required to reach goal node : {closed_dict[goal_node][2]}")  # Printing the total cost required to reach the goal node

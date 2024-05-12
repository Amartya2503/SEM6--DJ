import math

#steps of grahams scan:
# 1. find the min point from all the points (with lowest Y coordinate and for ones with equal Y , the lowest X coordinates ) 
# 2. sort the points in polar order using atan2(point1[0] - start[0], point1[1] - start[1])
# 3. insert first 2 points in the stack as  any convex hull has atleast 3 points
# 4. at every point of insertion we will keep popping till the top 2 points of stack and the incoming point are such that we need to take a right turn to reach the incoming point
# 5. at the end we will only be left with points which are part of convex hull 

def orientation(p, q, r):
    val = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1]) #this is for finding the direction somehow 
    # A(X1, Y1)  B(X2, Y2)   c(X3,Y3) ---> (Y2 - Y1)*(X3 - X2) - (X2 - X1)*(Y3 - Y2)
    if val == 0:
        return 0 #both points in same direction / polar angle
    if val >0:
        return 1 #clockwise
    if val<0:
        return 2 #antiClock

def convexHull(points):
    n = len(points)
    if n< 3:
        return None
    start = min(points, key = lambda point: (point[1], point[0])) #this gives us the min point from points 
    
    #sort the points using this function which will return the smaller polar angle point
    def sorthelp(point):
        return math.atan2(point[1] - start[1], point[0] - start[0])
    
    #now we have sorted the points using sorted which will return a new list of sorted points(sort just updates the previous list but sorted returns a new list)
    sorted_points = sorted(points, key = sorthelp)
    print(sorted_points)
    
    stack = [start,sorted_points[0]]
    #now we iterate through the points 
    
    for i in range(1, len(sorted_points)):
        
        while len(stack) >1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2 :
            stack.pop()
        stack.append(sorted_points[i])
    
    return stack

points = [(0, 3),(1, 1),(2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_points = convexHull(points)
print("the points which are a part of covex hull ")
while len(convex_points) : 
    print(convex_points.pop())
    

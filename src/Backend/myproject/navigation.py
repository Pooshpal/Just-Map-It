import math
import numpy as np 
import heapq
import json
import cv2
import base64
def getDirection(list_items):   
    with open('./assets/metadata.json', 'r') as f:
        data = json.load(f)
    section_list = data['sectionWiseItemList']
    coord_dict = data['coord_dict']
    connections = data['connections']
    main_paths = data['main_paths']
    access_nodes = data['access_nodes']
    def adjmat(coord_dict,connections):
        dict_len = len(coord_dict) 
        adj_mat  = [[0] * dict_len for _ in range(dict_len)]
        for i in connections:
            x                           =       coord_dict[str(i[0])]
            y                           =       coord_dict[str(i[1])]
            dist                        =       int((y[0]-x[0])**2+(y[1]-x[1])**2)
            dist_sqr                    =       int(math.sqrt(dist))
            if [i[0],i[1]] in main_paths:
                dist_sqr = 0.75*dist_sqr
            adj_mat[i[0]-1][i[1]-1]   =       dist_sqr
            adj_mat[i[1]-1][i[0]-1]   =       dist_sqr
        
        return adj_mat

    def shortest_path1(matrix, start, end):
        n = len(matrix)
        distances = [float('inf')] * n
        distances[start] = 0
        visited = [False] * n
        queue = [(0, start)]
        path = {}
        heapq.heapify(queue)

        while queue:
            (dist, node) = heapq.heappop(queue)
            if node == end:
                break
            if not visited[node]:
                visited[node] = True
                for i in range(n):
                    if matrix[node][i] != 0:
                        new_dist = dist + matrix[node][i]
                        if new_dist < distances[i]:
                            distances[i] = new_dist
                            path[i] = node
                            heapq.heappush(queue, (new_dist, i))

        shortest_path = []
        path_tuples = []
        while end != start:
            shortest_path.append(path[end])
            path_tuples.append((path[end], end))
            end = path[end]
        shortest_path.reverse()
        path_tuples.reverse()
        return(shortest_path)

        
    def generate_path1(access_points,start,end):
        matrix = adjmat(coord_dict,connections)
        path = []
        #access_points.sort()
        for i in range(len(access_points)-1):
            temp_path = shortest_path1(matrix,access_points[i]-1,access_points[i+1]-1)
            for i in temp_path:
                path.append(i+1)
        temp_path_start = shortest_path1(matrix,start,access_points[0]-1) 
        temp_path_end = shortest_path1(matrix,access_points[-1]-1,end) 
        for i in temp_path_start + temp_path_end:
                path.append(i+1)
        return path

    def func_sort(access_points):
         # Calculate the distances from access point 89 to all other access points
        access_point_89 = coord_dict.get("89")
        distances = {}
        for point in access_points:
            if str(point) in coord_dict and point>68:
                coords = coord_dict.get(str(point))
                # Calculate the Euclidean distance
                distance = math.sqrt((access_point_89[0] - coords[0])**2 + (access_point_89[1] - coords[1])**2)
                distances[point] = distance

        # Sort the access points based on their distances (shortest comes first)
        access_points = sorted([point for point in access_points if point <= 68])
        access_points.extend(sorted(distances, key=lambda point: distances[point],reverse =True))
        return access_points
    

    section = []
    for key, value in section_list.items():
        for i in list_items:
            if i in value:
                section.append(key)

    access_points = []
    for i in section:
        access_points.append(access_nodes[i])
    unique_list = list(set(access_points))
    access_points = func_sort(access_points)
    path1 = generate_path1(access_points,start=0,end=89)
    dest = []
    for i in path1:
        if i in unique_list:
            dest.append(i)
    unique_dest = []
    for i in dest:
        if i not in unique_dest:
            unique_dest.append(i)
    my_dict = {}	
    sect = []	
    for i in unique_dest:
        for key, value in access_nodes.items():
            if value == i:
                sect.append(key)
    
    n = len(unique_dest)

    for i in range(n):
        info = {}
        item_list = []
        path_list = []
        list1 = []
        for value in section_list[sect[i]]:
            for j in list_items:
                if j==value:
                    item_list.append(j)
        info["item"] = item_list
        list1.append(access_points[i])
        if i == 0:
            path_list = generate_path1(list1, start = 0, end = unique_dest[0] - 1)
            for k in range(len(path_list)):
                path_list[k] = coord_dict.get(str(path_list[k]))
            path_list.append(coord_dict.get(str(unique_dest[0])))
        else:
            path_list = generate_path1(list1,start = unique_dest[i-1] - 1 ,end = unique_dest[i] - 1)
            for k in range(len(path_list)):
                path_list[k] = coord_dict.get(str(path_list[k]))
            path_list.append(coord_dict.get(str(unique_dest[i])))
        
        info["path"] = path_list
        my_dict[i+1] = info
    list2 = []
    list2.append(90)
    path1 = generate_path1(list2,start = unique_dest[n-1] - 1,end = 89)
    for k in range(len(path1)):
            path1[k] = coord_dict.get(str(path1[k]))
    path1.append(coord_dict.get('90'))
    my_dict["billing"] = {"item": "Billing", "path":path1} 
    

    def make_line(path,img):
        for i in range(len(path)-1):
            cv2.line(img,(int(path[i][0]),int(path[i][1])),(int(path[i+1][0]),int(path[i+1][1])),(0, 0, 255), 2)
        return img
    
    img = cv2.imread('./assets/floor_blueprint.png')
    for i in my_dict.values():
        img=make_line(i['path'],img)
    #cv2.imwrite("./assets/full_path.png",img)
    _, encoded_image = cv2.imencode('.png', img)
    base64_image = base64.b64encode(encoded_image.tobytes()).decode()
    return my_dict,base64_image



# /print(getDirection(['Apples','Dates']))

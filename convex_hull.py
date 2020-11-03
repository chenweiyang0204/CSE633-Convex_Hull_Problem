import math
import copy
import matplotlib.pyplot as plt

def degree_cal(p1,p2):
    # slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    angel = math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))
    theta = angel * (180/math.pi)
    return theta

def draw_graph(data): #Draw Point graph
    xs = [x[0] for x in data]
    ys = [x[1] for x in data]
    plt.figure('Draw')
    plt.scatter(xs,ys)
    plt.plot(xs,ys,label="plot A")
    plt.draw()
    plt.legend()
    plt.pause(20)

def direction_determine(p1,p2,p3):
    y = p2[1] - p1[1]
    x = p1[0] - p2[0]
    z = p2[0]*p1[1] - p1[0]*p2[1]
    f = y*p3[0] + x*p3[1] + z
    if(f<0): # in the left
        return -1
    elif(f==0):  # in the line
        return 0
    else:  # in the right
        return 1

def isleft(p1,p2,p3):
    return (p2[0] - p1[0])*(p3[1]-p1[0]) - (p3[0]-p1[0])*(p2[1]-p1[1])

def convex_hull(data):
    data = sorted(data , key=lambda k: [k[1], k[0]]) #sort data
    start = data[0]

    degree_list = []
    for i in range(0,len(data)):
        deg = degree_cal(start,data[i])
        data[i].append(deg)

    data = sorted(data , key=lambda k: [k[2],
                    abs(start[1]-k[1])**2+abs(start[0]-k[0])**2]) #sort data

    stack = []
    i = 2
    first = data[0]
    second = data[1]
    stack.append(first[0:2])
    stack.append(second[0:2])
    while(i<len(data)):
        third = data[i]
        dir = direction_determine(first,second,third)
        if dir == 1:
            stack.pop()
            second = stack[len(stack)-1]
            first = stack[len(stack)-2]
        else:
            stack.append(third[0:2])
            first = second
            second = third
            i += 1

    # draw_graph(stack)
    return stack


def findBottomTangentLine(l1,l2):
    left = l1.index(max(l1))
    right = l2.index(min(l2))

    check = False
    while(check == False):
        check = True
        while(direction_determine(l2[right],l1[left],l1[left-1]) == -1 ):
            left = left - 1

        input = 0 if right + 1 == len(l2) else right + 1

        while(direction_determine(l1[left],l2[right],l2[input]) == 1):
            right = input
            input = 0 if input + 1 == len(l2) else input + 1
            check = False
    return left,right

def findTopTangentLine(l1,l2):
    left = l1.index(max(l1))
    right = l2.index(min(l2))

    check = False
    while(check == False):
        check = True
        input = 0 if left + 1 == len(l1) else left + 1
        while(direction_determine(l2[right],l1[left],l1[input]) == 1 ):
            left = input
            input = 0 if input + 1 == len(l2) else input + 1

        while(direction_determine(l1[left],l2[right],l2[right-1]) == -1):
            right = right - 1
            check = False
    return left,right

def combineTwoConvexHull(botleft,botright,topleft,topright,l1,l2):
    removeList = []
    for i in range(topleft-1,botleft,-1):
        removeList.append(l1[i])
    if botright > 0:
        for j in range(topright+1,botright,+1):
            removeList.append(l2[j])
    elif botright == 0:
        for j in range(topright+1,len(l2),+1):
            removeList.append(l2[j])
    elif botright < 0 :
        for j in range(topright+1,len(l2),+1):
            removeList.append(l2[j])
        for x in range(0,botright,-1):
            removeList.append(l2[x])

    data = l1 + l2
    for i in removeList:
        data.remove(i)

    data = sorted(data , key=lambda k: [k[1], k[0]]) #sort data
    start = data[0]

    for i in range(0,len(data)):
        deg = degree_cal(start,data[i])
        data[i].append(deg)

    data = sorted(data , key=lambda k: [k[2],
                    abs(start[1]-k[1])**2+abs(start[0]-k[0])**2])
    return data
if __name__ == "__main__":
    data = []
    with open('CSE633/data_100.txt', 'r') as filehandle:
        filecontents = filehandle.readlines()
        for line in filecontents:
            data.append([int(x) for x in line.split(" ")])
    filehandle.close()

    result = convex_hull(data[0:25])
    result2 = convex_hull(data[25:50])
    result3 = convex_hull(data[50:75])
    result4 = convex_hull(data[75:100])

    a,b = findBottomTangentLine(result,result2)
    c,d = findTopTangentLine(result,result2)

    l = combineTwoConvexHull(a,b,c,d,result,result2)

    a,b = findBottomTangentLine(result3,result4)
    c,d = findTopTangentLine(result3,result4)
    l2 = combineTwoConvexHull(a,b,c,d,result3,result4)

    a,b = findBottomTangentLine(l,l2)
    c,d = findTopTangentLine(l,l2)
    result = combineTwoConvexHull(a,b,c,d,l,l2)

    draw_graph([[447, 0, 0.0, 0.0], [819, 88, 0.0, 13.309178695400478], [972, 247, 46.101706115206376, 25.19586763415938], [986, 335, 55.936848950206446, 31.861833033634557], [978, 829, 77.88940223234559, 57.359188414900295], [966, 986, 80.70330198687586, 62.23906449091959], [902, 988, 84.73095978177295, 65.27268561330986], [163, 988, 106.03726505711444, 106.03726505711444], [51, 861, 114.69913471532166, 114.69913471532166], [43, 815, 116.36786884020876, 116.36786884020876], [35, 567, 126.00333235871084, 126.00333235871084], [23, 52, 173.00807465333222, 173.00807465333222], [46, 19, 177.28726620477636, 177.28726620477636]] )
    # draw_graph(result)

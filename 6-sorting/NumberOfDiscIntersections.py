def solution(A):
    circle_ends=[]
    for center, rad in enumerate(A):
        circle_ends += [(center-rad,True),(center+rad, False)]
    #pairs sorting:
    circle_ends.sort(key=lambda x: (x[0], not x[1]))

    current_circles, intersections = 0, 0

    for place, end_type in circle_ends:
        if end_type :
            intersections+=current_circles
            current_circles+=1
        else:
            current_circles-=1
        if intersections > 10E6:
            return -1
    return intersections
    pass

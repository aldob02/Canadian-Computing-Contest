N = int(input())
height = input()
width = input()
tarea=0

heights = height.split()
widths = width.split()

for i in range(N):
    h1 = int(heights[i])
    h2 = int(heights[i+1])
    w = int(widths[i])
        
    if h1 > h2:
        h = h2
    else:
        h = h1
        
    area = (((abs(h1-h2))*w)/2) + (h*w)
    tarea += area
    
print(tarea)
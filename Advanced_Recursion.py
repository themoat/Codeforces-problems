a=[[1,1,0],[1,2,1],[1,0,2]]

def floodfill(a,r,c,tofill,prevfill): # yahaan pe, r and c denote the row and column we are at, or in paint we will click at.
    #Let's mention out how many rows and columns are there
    rows = len(a)
    col = len(a[0])

    #Since we are applyng recursion over here, so let's start with our base condition.
    if rows<0 or r>rows or c<0 or c>col:
        return

    # We check if the new cell in which we are, that it is the cell, jisko
    #hum update karnaa chahte hain, i.e see if [r][c]==prevfill, agar nahi hai toh return kar jaao
    # kyuki uss cell ko mujhe chhednaa hiii nahi hai.
    if a[r][c]!=prevfill:
        return
    #now we fill our color
    a[r][c]=tofill

    floodfill(a,r-1,c,tofill,prevfill)
    floodfill(a,r,c-1,tofill,prevfill)
    floodfill(a,r+1,c,tofill,prevfill)
    floodfill(a,r,c+1,tofill,prevfill)

floodfill(a,1,1,8,2)
print(a)



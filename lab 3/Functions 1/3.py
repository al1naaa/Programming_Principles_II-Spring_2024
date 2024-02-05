def solve(numheads, numlegs):
    rabbit=(numlegs-2*numheads)/2
    chicken=numheads-rabbit
    print("rabbit: ", int(rabbit), " chicken: ", int(chicken))
x=int(input())
y=int(input())
solve(x,y)
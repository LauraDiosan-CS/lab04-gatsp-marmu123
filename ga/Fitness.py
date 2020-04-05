def fitnessOfPath(sol,graph):
    pathDistance = 0
    fromCity=-1
    toCity=-1
    for i in range(0, len(sol)-1):
        fromCity = sol[i]
        toCity=sol[i+1]
        pathDistance += graph[fromCity][toCity]
    pathDistance+=graph[sol[-1]][sol[0]]
    return 1/pathDistance

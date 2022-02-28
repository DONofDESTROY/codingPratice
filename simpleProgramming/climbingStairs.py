def climb(cost):
    # [10,15,20] + 0
    cost.append(0)
    for i in range(len(cost)-3,-1,-1):
        cost[i] += min(cost[i+1],+cost[i+2])
    print("something")
    print(min(cost[0],cost[1]))




def main():
    cost = [10,15,20]
    climb(cost)
main()

# 1.11

# p=[0.2,0.2,0.2,0.2,0.2]
# pHit = 0.6
# pMiss = 0.2

# #Enter code here
# hits = [ 1, 2 ]
# misses = [ 0, 3, 4 ]

# p = [p[i] * pHit if i in hits else p[i] * pMiss for i in range(len(p)) ]


# print(p)


# 1.13

# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# Z = 'red'
# pHit = 0.6
# pMiss = 0.2

# def sense(p, Z):
#     q = []
#     for i in range(len(p)):
#         q.append(p[i] * pHit if world[i] == Z else p[i] * pMiss)
#     return q

# print(sense(p,Z))

#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


# p=[0.2, 0.2, 0.2, 0.2, 0.2]
# world=['green', 'red', 'red', 'green', 'green']
# Z = 'red'
# pHit = 0.6
# pMiss = 0.2

# def sense(p, Z):
#     q=[]
#     for i in range(len(p)):
#         hit = (Z == world[i])
#         q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
#     return q
# print sense(p,Z)
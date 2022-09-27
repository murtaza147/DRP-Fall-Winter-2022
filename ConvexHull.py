coordinates = [(1, 2), (4, 2), (3, 1), (4, 7), (5, 3)]
def rightTurn(l):
     return False
def convexHull(p):
     sorted(p)
     upper = [p[0], p[1]]
     i = 2
     while i < len(coordinates):
          upper.append(p[i])
          while len(upper) > 2 and not rightTurn([upper[-1], upper[-2], upper[-3]]):
               upper.remove(upper[-2])
          i+=1
     lower = [p[-1], p[-2]]
     i = len(coordinates) - 2
     while i > 0:
          lower.append(p[i])
          while len(lower) > 2 and not rightTurn([lower[-1], lower[-2], lower[-3]]):
               lower.remove(lower[-2])
          i-=1
     lower.remove(lower[-1])
     return upper.append(lower)


print(convexHull(coordinates))

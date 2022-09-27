coordinates = [(2, 2), (7, 7), (4, 1), (5, 4), (3, 5), (6, 3)]


def rightTurn(l):
    # Calculating the determinant
    #          x          y
    # c1| l[0][0]    l[0][1] |
    # c2| l[1][0]    l[1][1] |
    # c3| l[2][0]    l[2][1] |

    # -ve value meaning right turn
    print((l[0][0] * l[1][1] + l[1][0] * l[2][1]) - (l[0][1] * l[1][0] + l[1][1] * l[2][0]))
    return ((l[0][0] * l[1][1] + l[1][0] * l[2][1]) - (l[0][1] * l[1][0] + l[1][1] * l[2][0])) > 0


def convexHull(p):
    p = sorted(p)
    upper = [p[0], p[1]]
    print(p)
    print(upper)
    i = 2
    while i < len(coordinates):
        upper.append(p[i])
        print("cor being appended: " + str(p[i]))
        print(upper)
        while len(upper) > 2 and not rightTurn([upper[-1], upper[-2], upper[-3]]):
            # print(rightTurn([upper[-1], upper[-2], upper[-3]]))
            print("removed: " + str(upper[-2]))
            upper.remove(upper[-2])
            print(upper)
        i += 1
    print(upper)


    print()
    print('-'*25)
    print()


    lower = [p[-1], p[-2]]
    print(p)
    print(lower)
    i = len(coordinates) - 3
    while i > 1:
        lower.append(p[i])
        print("cor being appended: " + str(p[i]))
        print(lower)
        while len(lower) > 2 and not rightTurn([lower[-1], lower[-2], lower[-3]]):
            print("removed: " + str(lower[-2]))
            lower.remove(lower[-2])
            print(lower)
        i -= 1
    lower.remove(lower[-2])
    lower.remove(lower[0])
    print(lower)
    return upper + lower


print("Convex Hull Plot: " + str(convexHull(coordinates)))

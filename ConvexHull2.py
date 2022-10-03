coordinates = [(30, 60), (50, 40), (70, 30), (0, 30), (15, 25), (55, 20), (50, 10), (20, 0)]


def rightTurn(l):
    # Calculating the determinant
    # Here's how im doing it: https://www.youtube.com/watch?v=bkJX3q7wvJc&ab_channel=Mario%27sMathTutoring
    #          x         y
    # c1| l[0][0]   l[0][1]   1 | l[0][0]   l[0][1]   1 |
    # c2| l[1][0]   l[1][1]   1 | l[1][0]   l[1][1]   1 |
    # c3| l[2][0]   l[2][1]   1 | l[2][0]   l[2][1]   1 |

    # -ve value meaning right turn
    print("Right Turn?")
    print(((l[0][0] * l[1][1] * 1) + (l[0][1] * 1 * l[2][0]) + (1 * l[1][0] * l[2][1])) - ((l[2][0] * l[1][1] * 1) + (l[2][1] * 1 * l[0][0]) + (1 * l[1][0]) * l[0][1]) > 0)
    return (((l[0][0] * l[1][1] * 1) + (l[0][1] * 1 * l[2][0]) + (1 * l[1][0] * l[2][1])) - ((l[2][0] * l[1][1] * 1) + (l[2][1] * 1 * l[0][0]) + (1 * l[1][0]) * l[0][1])) > 0


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
    print('-' * 25)
    print()

    lower = [upper[-1], upper[-2]]
    print(upper)
    print(lower)
    i = len(coordinates) - 3
    while i >= 1:
        lower.append(p[i])
        print("cor being appended: " + str(p[i]))
        print(lower)
        while len(lower) > 2 and not rightTurn([lower[-1], lower[-2], lower[-3]]):
            print("removed: " + str(lower[-2]))
            lower.remove(lower[-2])
            print(lower)
        i -= 1
    if len(lower) > 2:
        lower.remove(lower[-1])
        lower.remove(lower[0])
    else:
        lower.remove(lower[0])
    print(lower)
    return upper + lower


print("Convex Hull Plot: " + str(convexHull(coordinates)))

xs = [p[0] for p in coordinates]
ys = [p[1] for p in coordinates]

hull = convexHull(coordinates)

hull_xs = [p[0] for p in hull]
hull_ys = [p[1] for p in hull]
hull_xs.append(hull_xs[0])
hull_ys.append(hull_ys[0])

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

ax.scatter(xs, ys)
ax.plot(hull_xs, hull_ys)

plt.show()
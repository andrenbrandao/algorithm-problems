"""
An [H-tree](https://en.wikipedia.org/wiki/H_tree) is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by `√2`.

Here are some examples of H-trees at different levels of depth:

![https://www.pramp.com/img/content/img03.png](https://www.pramp.com/img/content/img03.png)
depth = 1

![https://www.pramp.com/img/content/img04.png](https://www.pramp.com/img/content/img04.png)
depth = 2

![https://www.pramp.com/img/content/img05.png](https://www.pramp.com/img/content/img05.png)
depth = 3

Write a function `drawHTree` that constructs an H-tree, given its center (`x` and `y` coordinates), a starting `length`, and `depth`. Assume that the starting line is parallel to the X-axis.

Use the function `drawLine` provided to implement your algorithm. In a production code, a `drawLine` function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement `drawLine` such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that `drawLine`'s time and space complexities are constant, i.e. `O(1)`.

**Constraints:**

- **[time limit] 5000ms**
- **[input] double** `x`
- **[input] double** `y`
- **[input] double** `length`
- **[input] double** `depth`
    - 0 ≤ depth ≤ 10



### SOLUTION ###

drawHTree(x, y, length, depth)
(x, y) is the center point

To remember:
- Reduce the length of the line segment at each stage by sqrt(2)

 H   H
 |   |
x|---|x
 |   |
 H   H

center (0, 0)

base case:

depth is 0
return

recursive step:
- draw a line from (center_x - length // 2, center_y), (center_x + length // 2, center_y)
- draw the vertical lines
  - left_vertical_line: (center_x - length // 2, center_y + length // 2), (center_x - length // 2, center_y - length // 2)
  - right_vertical_line: (center_x + length // 2, center_y + length // 2), (center_x + length // 2, center_y - length // 2)

- repeat for points:
  - left_top
  - left_bottom
  - right_top
  - right_bottom


call drawHTree with length / sqrt(2)

    H
  / | | \
  H
  /\

O(4^depth)
O(depth)

"""
import math
from matplotlib import pyplot


def drawLine(x1, y1, x2, y2):
    x_values = [x1, x2]
    y_values = [y1, y2]
    pyplot.plot(x_values, y_values)
    print("(" + str(x1) + "," + str(y1) + ")", "(" + str(x2) + "," + str(y2) + ")")


def drawHTree(x, y, length, depth):
    if depth == 0:
        return

    left_x = x - length / 2
    right_x = x + length / 2
    top_y = y + length / 2
    bottom_y = y - length / 2

    drawLine(left_x, y, right_x, y)
    drawLine(left_x, top_y, left_x, bottom_y)
    drawLine(right_x, top_y, right_x, bottom_y)

    drawHTree(left_x, top_y, length / math.sqrt(2), depth - 1)
    drawHTree(left_x, bottom_y, length / math.sqrt(2), depth - 1)
    drawHTree(right_x, top_y, length / math.sqrt(2), depth - 1)
    drawHTree(right_x, bottom_y, length / math.sqrt(2), depth - 1)


drawHTree(0, 0, 2, 2)
pyplot.show()

# Coordinate Geometry of Circles: A Comprehensive Guide

## 1. Definition and Standard Form
A circle is the locus of all points in a plane that are equidistant from a fixed point called the center. In coordinate geometry, if $(h,k)$ is the center and $r$ is the radius, then any point $(x,y)$ on the circle satisfies:

$$(x-h)^2 + (y-k)^2 = r^2$$

This is known as the standard form equation of a circle.

## 2. General Form
The general equation of a circle is:
$$x^2 + y^2 + 2gx + 2fy + c = 0$$
where:
- Center: $(-g,-f)$
- Radius: $r = \sqrt{g^2 + f^2 - c}$

## 3. Key Properties

### 3.1 Tangent and Normal
For a circle with center $(h,k)$ and point of tangency $(x_1,y_1)$:

- **Tangent equation**:
  $$(x-h)(x_1-h) + (y-k)(y_1-k) = r^2$$

- **Normal equation**:
  $$\frac{x-x_1}{x_1-h} = \frac{y-y_1}{y_1-k}$$

### 3.2 Length of Tangent
The length of tangent from an external point $(x_1,y_1)$ to a circle $(x-h)^2 + (y-k)^2 = r^2$ is:
$$T = \sqrt{(x_1-h)^2 + (y_1-k)^2 - r^2}$$

## 4. Power of a Point
For any point $P(x_1,y_1)$ and a circle with center $O$:
$$\text{Power of P} = OP^2 - r^2 = (x_1-h)^2 + (y_1-k)^2 - r^2$$

### Properties:
- If $P$ is outside: Power = (Length of tangent from $P$)$^2$
- If $P$ is on circle: Power = 0
- If $P$ is inside: Power is negative

## 5. Intersection of Circles

Two circles:
$$x^2 + y^2 + 2g_1x + 2f_1y + c_1 = 0$$
$$x^2 + y^2 + 2g_2x + 2f_2y + c_2 = 0$$

Their radical axis equation is:
$$2(g_1-g_2)x + 2(f_1-f_2)y + (c_1-c_2) = 0$$

## 6. System of Circles

### 6.1 Family of Circles
The equation of family of circles passing through the intersection of two circles $S_1 = 0$ and $S_2 = 0$ is:
$$S_1 + \lambda S_2 = 0$$
where $\lambda$ is a parameter.

### 6.2 Orthogonal Circles
Two circles are orthogonal if they intersect at right angles. For circles with centers $(h_1,k_1)$, $(h_2,k_2)$ and radii $r_1$, $r_2$:
$$(h_1-h_2)^2 + (k_1-k_2)^2 = r_1^2 + r_2^2$$

## 7. Special Cases and Applications

### 7.1 Circle through Three Points
For points $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$:

$$\begin{vmatrix} 
x^2+y^2 & x & y & 1 \\
x_1^2+y_1^2 & x_1 & y_1 & 1 \\
x_2^2+y_2^2 & x_2 & y_2 & 1 \\
x_3^2+y_3^2 & x_3 & y_3 & 1
\end{vmatrix} = 0$$

### 7.2 Coaxial Circles
Family of circles whose centers lie on a straight line and have a common radical axis:
$$x^2 + y^2 + 2gx + 2fy + c + \lambda(x^2 + y^2 + 2g'x + 2f'y + c') = 0$$

## 8. Important Theorems

1. **Apollonian Circles**: The locus of points whose distances from two fixed points are in a constant ratio.

2. **Angle Properties**: The angle between two circles is equal to the angle between their tangents at their point of intersection.

## Practice Problems

1. Find the equation of circle passing through $(0,0)$, $(a,0)$, $(0,b)$.
2. Prove that the radical axis of two circles is perpendicular to the line joining their centers.
3. Find the condition for two circles to be orthogonal.

---
*Note: This document covers the essential aspects of coordinate geometry of circles. For deeper understanding, practice solving problems involving these concepts.*
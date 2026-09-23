"""Independent small controls for the frozen PR8158 review.

This uses the stated mathematical definitions, not the submitted programs.
"""

from fractions import Fraction
from itertools import product


def neighbours(x):
    for axis in range(3):
        for step in (-1, 1):
            y = list(x)
            y[axis] += step
            yield tuple(y)


plaquette = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
outside = set().union(*(set(neighbours(x)) for x in plaquette)) - set(plaquette)
touch_counts = {x: sum(x in set(neighbours(y)) for y in plaquette) for x in outside}
print("plaquette outside-neighbour attachment counts:", sorted(set(touch_counts.values())))
assert max(touch_counts.values()) == 1
assert not (set(neighbours(plaquette[0])) & set(neighbours(plaquette[1])))


def phi(i, j, p, q, r):
    if i == j:
        return p
    if i // 2 == j // 2:
        return q
    return r


def normalized(weights):
    z = sum(weights.values())
    return {k: Fraction(v, z) for k, v in weights.items()}


def tv(a, b):
    return sum((abs(a[k] - b[k]) for k in a), Fraction()) / 2


def bridge_factor(a, b, rule):
    return sum(rule[a][u] * rule[u][b] for u in range(6))


for p, q, r in ((3, 1, 2), (5, 2, 4), (2, 1, 2), (2, 2, 2)):
    rule = [[phi(i, j, p, q, r) for j in range(6)] for i in range(6)]
    # Embeddable path: x=(-1,0,0), a=(0,0,0), y=(1,0,0).
    one = {(a, b): 1 for a, b in product(range(6), repeat=2)}
    two = {(a, b): bridge_factor(a, b, rule) for a, b in one}
    print("actual two-record path", (p, q, r), "TV", tv(normalized(one), normalized(two)))
    # Submitted plaquette fixture is an abstract graph with a triangle.
    ring = {}
    ring_bridge = {}
    for vals in product(range(6), repeat=4):
        a, b, c, d = vals
        w = rule[a][b] * rule[b][c] * rule[c][d] * rule[d][a]
        ring[vals] = w
        ring_bridge[vals] = w * bridge_factor(a, b, rule)
    print("abstract ring plus triangle", (p, q, r), "TV", tv(normalized(ring), normalized(ring_bridge)))


# Independent face-to-face transfer computation for the actual cube graph.
rule = [[phi(i, j, 3, 1, 2) for j in range(6)] for i in range(6)]
faces = list(product(range(6), repeat=4))
face_weight = {
    v: rule[v[0]][v[1]] * rule[v[1]][v[2]] * rule[v[2]][v[3]] * rule[v[3]][v[0]]
    for v in faces
}
top = [(u, face_weight[u]) for u in faces]
cube = {
    v: face_weight[v]
    * sum(w * rule[v[0]][u[0]] * rule[v[1]][u[1]] * rule[v[2]][u[2]] * rule[v[3]][u[3]] for u, w in top)
    for v in faces
}
print("actual cube face", (3, 1, 2), "TV", tv(normalized(face_weight), normalized(cube)))

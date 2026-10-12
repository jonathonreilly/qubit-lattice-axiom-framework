"""B2 check c2: number of independent quadratic (stiffness) forms on the 5-dim
TT/traceless-strain space left free by a point group G (= number of numbers a
symmetry leaves to be tuned).  tr(eps^2) is invariant under every G in O(3),
so the count is >= 1 for every finite G: no finite point group forces the TT
stiffness to vanish.  Also: hop-count (graph) distance on Z^3 is l1, not
Euclidean."""
import math, itertools
def chi2(theta):          # l = 2 character of a rotation by theta
    return 1 + 2*math.cos(theta) + 2*math.cos(2*theta)
def n_inv_sym2(classes, order):
    s = 0.0
    for size, th in classes:
        s += size*(chi2(th)**2 + chi2(2*th))/2
    return s/order
O = [(1,0),(8,2*math.pi/3),(3,math.pi),(6,math.pi/2),(6,math.pi)]
I = [(1,0),(15,math.pi),(20,2*math.pi/3),(12,2*math.pi/5),(12,4*math.pi/5)]
T = [(1,0),(8,2*math.pi/3),(3,math.pi)]
D4= [(1,0),(2,math.pi/2),(1,math.pi),(4,math.pi)]
for name,cl,o in [("T (12)",T,12),("O (24)",O,24),("I (60)",I,60),("D4 (8)",D4,8)]:
    print(f"{name}: invariant quadratic forms on traceless strains = {n_inv_sym2(cl,o):.6f}")
# SO(3) continuum: exactly 1 (Schur) -- it is tr(eps^2), and only a continuous
# relabelling symmetry (SL(3) acting on the strain itself, not just rotations)
# can remove it.
# hop-count geometry on Z^3
n=10
print("graph distance to (n,n,n) / Euclidean distance =", 3*n/math.sqrt(3*n*n), "(= sqrt 3): l1 ball is an octahedron")

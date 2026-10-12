"""C5 R5-1 (1b): explicit infinite-order elements of Gamma fixing off-axis spacelike supports
(the BFS ball of r51_stabilizers.py, built from axis boosts + cubic rotations, does not reach them).
Pell construction on the G7-orthogonal complement, then the least power that is integral on Z^4."""
import sympy as sp
G7 = sp.diag(-7, 1, 1, 1)
def check(name, B, A):
    M = B * A * B.inv()
    for k in range(1, 13):
        Mk = M ** k
        if all(x.is_integer for x in Mk):
            ok = (Mk.T * G7 * Mk == G7) and Mk.det() == 1 and Mk[0, 0] > 0
            print(f"{name}: M^{k} integral, in SO+(Q7,Z): {ok}; fixes support: "
                  f"{[bool(Mk * B[:, i] == B[:, i]) for i in range(B.shape[1]) if A[i, i] == 1 and all(A[i, j] == (1 if i == j else 0) for j in range(4))]};"
                  f" trace {Mk.trace()} (>4 => loxodromic, infinite order)")
            return Mk
    print(name, "no integral power <= 12")
# (1) spacelike link d = (1,3,0,0), Q7 = 2.  d-perp basis: v=(3,7,0,0) [Q=-14], e2, e3.
d = sp.Matrix([1, 3, 0, 0]); v = sp.Matrix([3, 7, 0, 0]); e2 = sp.Matrix([0, 0, 1, 0]); e3 = sp.Matrix([0, 0, 0, 1])
assert (d.T * G7 * v)[0] == 0
B = sp.Matrix.hstack(d, v, e2, e3)
A = sp.Matrix([[1, 0, 0, 0], [0, 15, 4, 0], [0, 56, 15, 0], [0, 0, 0, 1]])   # Pell 15^2 - 14*4^2 = 1 on (v,e2)
assert sp.Matrix([[15, 4], [56, 15]]).T * sp.diag(-14, 1) * sp.Matrix([[15, 4], [56, 15]]) == sp.diag(-14, 1)
check("spacelike link {0,(1,3,0,0)}", B, A)
# (2) spacelike plane W = span((1,3,0,0), e3): W-perp = span(v, e2), form diag(-14,1)
check("spacelike plane {0,(1,3,0,0),e3}", B, A)

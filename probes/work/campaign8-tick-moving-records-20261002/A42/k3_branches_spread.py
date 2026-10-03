"""A42 check k3.
(a) Axis soldering: the allowed neighbour-support lines n_z (invariant under the
    half-turn about d_z = (e_x - e_y)/sqrt2) and the angle between n_z and n_x =
    rho(C) n_z.  Lists the parallel and perpendicular members.
(b) In the perpendicular branches a controlled turn with u_+ != u_- (u in
    {1, sigma_w}) is not an automorphism: [alpha(sigma_w at x), alpha(b at y)] != 0.
(c) Spreading of the sign-twist mover C_s' = CZ_z . H_yz (Clifford skeleton over
    F2[x^+-1, y^+-1, z^+-1]): support of alpha^t(X_0) and alpha^t(Z_0), trace.
    Control: the shear L_s (CZ layer alone) never spreads.
"""
import numpy as np, sympy as sp, itertools

# ---------- (a) ----------
th = sp.symbols('theta', real=True)
cz, sz_ = sp.cos(th), sp.sin(th)
nz = sp.Matrix([sz_ / sp.sqrt(2), sz_ / sp.sqrt(2), cz])        # cos th e_z + sin th (e_x+e_y)/sqrt2
Cmat = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])               # rho(C) = cyclic e_x->e_y->e_z->e_x
nx = Cmat * nz
dz = sp.Matrix([1, -1, 0]) / sp.sqrt(2)
assert sp.simplify(nz.dot(dz)) == 0
dot = sp.simplify(nz.dot(nx))
print('(a) n_z . n_x =', dot)
print('    perpendicular at theta in', sp.solveset(sp.Eq(dot, 0), th, sp.Interval(-sp.pi / 2, sp.pi / 2)))
print('    parallel (|dot|=1) at theta in', sp.solveset(sp.Eq(dot, 1), th, sp.Interval(-sp.pi / 2, sp.pi / 2)))
for val in [0, sp.atan(sp.sqrt(2)), -sp.atan(2 * sp.sqrt(2))]:
    v = sp.simplify(nz.subs(th, val)); print('    theta =', val, ' n_z =', list(v), ' n_x =', list(sp.simplify(Cmat * v)))
dd = (Cmat * dz)
print('    d-branch: n_z = d_z, n_x =', list(dd), ' dot =', sp.nsimplify(dz.dot(dd)))

# ---------- (b) ----------
I2 = np.eye(2, dtype=complex); SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex); SZ = np.array([[1, 0], [0, -1]], complex)
def sig(n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n); return n[0] * SX + n[1] * SY + n[2] * SZ
def kron_all(ops):
    out = np.array([[1]], complex)
    for o in ops: out = np.kron(out, o)
    return out
# star of y: sites y, y+-e_a ; x = y - e_z is in it.  Index: 0=y, 1=+x,2=-x,3=+y,4=-y,5=+z,6=-z(= x)
dirs = [None, 0, 0, 1, 1, 2, 2]
w = np.array([1, 1, 1]) / np.sqrt(3)
for label, frame in [('n_a = e_a', np.eye(3)), ('n_a = (I - 2ww^T) e_a', np.eye(3) - 2 * np.outer(w, w))]:
    S = kron_all([I2] + [sig(frame[:, dirs[k]]) for k in range(1, 7)])   # S'_y
    Pp = (np.eye(128) + S) / 2; Pm = (np.eye(128) - S) / 2
    worst = 0
    for (up, um) in [(I2, sig(w)), (sig(w), I2)]:
        for b in [SX, SY, SZ]:
            ab = lambda u: kron_all([u @ b @ u.conj().T] + [I2] * 6)
            alpha_b = ab(up) @ Pp + ab(um) @ Pm
            sw_x = kron_all([I2] * 6 + [sig(w)])       # alpha(sigma_w at x) = sigma_w at x
            worst = max(worst, np.abs(sw_x @ alpha_b - alpha_b @ sw_x).max())
    print(f'(b) {label:24s} max |[alpha(sw_x), alpha(b_y)]| over mixed controls = {worst:.4f}  (nonzero => not an automorphism)')

# ---------- (c) ----------
NB = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
def add(a, b): return tuple(i + j for i, j in zip(a, b))
def shift(S, v): return {add(p, v) for p in S}
def xor(A, B): return A ^ B
O = (0, 0, 0)
# images (Xset, Zset) of X_0 and Z_0
def skeleton(name):
    N = set(NB)
    if name == "C_s'":   # Ad(CZ) Ad(H_yz): X0 -> -X0 prod Z ; Z0 -> Y0 prod Z
        return ({O}, N), ({O}, N | {O})
    if name == 'C_s':    # Ad(CZ) Ad(H_xz): X0 -> Z0 ; Z0 -> X0 prod Z
        return (set(), {O}), ({O}, N)
    if name == 'L_s':    # Ad(CZ): X0 -> X0 prod Z ; Z0 -> Z0
        return ({O}, N), (set(), {O})
def apply(sk, P):
    (ax, az), (bx, bz) = sk
    X, Z = set(), set()
    for p in P[0]:
        X = xor(X, shift(ax, p)); Z = xor(Z, shift(az, p))
    for p in P[1]:
        X = xor(X, shift(bx, p)); Z = xor(Z, shift(bz, p))
    return X, Z
for name in ["C_s'", 'C_s', 'L_s']:
    sk = skeleton(name)
    # trace = X-part of image of X0 + Z-part of image of Z0 (as Laurent polys mod 2)
    tr = xor(sk[0][0], sk[1][1])
    sizes = {}
    for start in ['X', 'Z']:
        P = ({O}, set()) if start == 'X' else (set(), {O})
        out = []
        for t in range(1, 9):
            P = apply(sk, P); out.append(len(P[0] | P[1]))
        sizes[start] = out
    print(f"(c) {name:5s} trace support {sorted(tr)}  |supp alpha^t(X0)| t=1..8: {sizes['X']}  |supp alpha^t(Z0)|: {sizes['Z']}")

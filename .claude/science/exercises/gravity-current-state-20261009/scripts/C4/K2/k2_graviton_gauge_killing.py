"""K2 part 1: free staggered linearized graviton on Z^4 (K7a placement), exact gauge
invariance, and the Killing algebra of the lattice linearized gauge map.

Placement (base-point labels): h_mn[x] sits at x+(e_m+e_n)/2, xi_n[x] at x+e_n/2.
nabla_m maps position p -> p+e_m/2:  (nabla_m F)(q) = F(q+e_m/2) - F(q-e_m/2).
delta h_mn[x] = xi_n[x+e_m]-xi_n[x] + xi_m[x+e_n]-xi_m[x].

Action (lattice Fierz-Pauli = K7a's Q in real space):
 S = 1/4 sum (nabla_r h_mn)^2 - 1/2 sum_n div_n^2 + 1/2 sum_n div_n nabla_n trh - 1/4 sum_r (nabla_r trh)^2
 div_n[y] = sum_m (h_mn[y]-h_mn[y-e_m])  (at y+e_n/2);  trh[z] = sum_r h_rr[z-e_r] (site z).
All arithmetic is on small integers / dyadic rationals in float64 -> exact.
"""
import numpy as np, itertools, sympy as sp

rng = np.random.default_rng(1)
D = 4

def sh(F, mu, n):  # F(x + n e_mu) on a torus
    return np.roll(F, -n, axis=mu)

def action(h):
    # h: array (4,4,L,L,L,L) symmetric in first two indices
    S = 0.0
    for r in range(D):
        for m in range(D):
            for n in range(D):
                g = sh(h[m, n], r, 1) - h[m, n]   # nabla_r h_mn (position shift irrelevant on torus)
                S += 0.25 * np.sum(g * g)
    div = [sum(h[m, n] - sh(h[m, n], m, -1) for m in range(D)) for n in range(D)]
    trh = sum(sh(h[r, r], r, -1) for r in range(D))   # site field
    for n in range(D):
        dtr = sh(trh, n, 1) - trh                      # at z+e_n/2, base z
        # div_n[y] lives at y+e_n/2 -> same base convention as dtr
        S += -0.5 * np.sum(div[n] * div[n]) + 0.5 * np.sum(div[n] * dtr) - 0.25 * np.sum(dtr * dtr)
    return S

def gauge(xi):
    h = np.zeros((D, D) + xi.shape[1:])
    for m in range(D):
        for n in range(D):
            h[m, n] = (sh(xi[n], m, 1) - xi[n]) + (sh(xi[m], n, 1) - xi[m])
    return h

def rand_sym(L):
    a = rng.integers(-20, 21, size=(D, D) + (L,) * D).astype(float)
    return a + np.transpose(a, (1, 0, 2, 3, 4, 5))

print("== A. real-space exact gauge invariance of the lattice FP action (torus) ==")
for L in (3, 4, 5):
    worst = 0.0
    for trial in range(3):
        h = rand_sym(L)
        xi = rng.integers(-20, 21, size=(D,) + (L,) * D).astype(float)
        dh = gauge(xi)
        val = action(h + dh) - action(h)
        val2 = action(dh)
        worst = max(worst, abs(val), abs(val2))
    print(f"L={L}: max |S(h+dh)-S(h)|, |S(dh)| over 3 random integer trials = {worst}")

# control: flip the cross-term sign -> not invariant
def action_bad(h):
    S = 0.0
    for r in range(D):
        for m in range(D):
            for n in range(D):
                g = sh(h[m, n], r, 1) - h[m, n]
                S += 0.25 * np.sum(g * g)
    div = [sum(h[m, n] - sh(h[m, n], m, -1) for m in range(D)) for n in range(D)]
    trh = sum(sh(h[r, r], r, -1) for r in range(D))
    for n in range(D):
        dtr = sh(trh, n, 1) - trh
        S += -0.5 * np.sum(div[n] * div[n]) - 0.5 * np.sum(div[n] * dtr) - 0.25 * np.sum(dtr * dtr)
    return S
h = rand_sym(4); xi = rng.integers(-20, 21, size=(D,) + (4,) * D).astype(float)
print("control (cross-term sign flipped): S(dh) =", action_bad(gauge(xi)), "(nonzero expected)")

print("\n== B. symbol: K(s) D(s) = 0 exactly (sympy), spectrum ==")
s = sp.symbols('s0:4', real=True)
pairs = [(m, n) for m in range(D) for n in range(m, D)]
idx = {p: i for i, p in enumerate(pairs)}
def comp(m, n):
    return idx[(min(m, n), max(m, n))]
# quadratic form Q(h) with h symmetric, h_mn -> variables; use real symbol s_m (staggered placement removes phases)
H = sp.Matrix(4, 4, lambda m, n: sp.Symbol(f"h{min(m,n)}{max(m,n)}"))
hv = [sp.Symbol(f"h{m}{n}") for (m, n) in pairs]
s2 = sum(si**2 for si in s)
hs = H * sp.Matrix(s)
shs = (sp.Matrix(s).T * H * sp.Matrix(s))[0]
tr = H.trace()
Q = sp.Rational(1, 4) * (s2 * sum(H[m, n]**2 for m in range(D) for n in range(D)) - 2 * (hs.T * hs)[0]
                         + 2 * shs * tr - s2 * tr**2)
K = sp.hessian(Q, hv) / 2
xis = sp.symbols('x0:4')
dh = {(m, n): s[m] * xis[n] + s[n] * xis[m] for (m, n) in pairs}
Dmat = sp.Matrix([[sp.diff(dh[p], x) for x in xis] for p in pairs])
print("K*D simplified is zero:", sp.simplify(K * Dmat) == sp.zeros(10, 4))
# spectrum at a random numeric s, in the h:h metric (off-diagonal components counted twice)
G = sp.diag(*[1 if m == n else 2 for (m, n) in pairs])
sv = {s[0]: 0.3, s[1]: -1.1, s[2]: 0.7, s[3]: 1.9}
Kn = np.array(K.subs(sv), dtype=float); Gn = np.array(G, dtype=float)
ev = np.sort(np.linalg.eigvals(np.linalg.solve(Gn, Kn)).real)
print("generalized eigenvalues / s^2 :", np.round(ev / float(s2.subs(sv)), 12))

print("\n== C. Killing vectors of the lattice gauge map on an open box (no torus) ==")
n = 4
# unknowns xi_nu[x] for base points x in box with x_nu <= n-2 (link inside box)
unk = []
for nu in range(D):
    for x in itertools.product(range(n), repeat=D):
        if x[nu] <= n - 2:
            unk.append((nu, x))
uidx = {u: i for i, u in enumerate(unk)}
rows = []
def e(mu):
    v = [0] * D; v[mu] = 1; return tuple(v)
def add(a, b): return tuple(i + j for i, j in zip(a, b))
for m in range(D):
    for nn in range(m, D):
        for x in itertools.product(range(n), repeat=D):
            terms = [((nn, add(x, e(m))), 1), ((nn, x), -1), ((m, add(x, e(nn))), 1), ((m, x), -1)]
            if all(t[0] in uidx for t in terms):
                r = np.zeros(len(unk))
                for t, c in terms:
                    r[uidx[t]] += c
                rows.append(r)
A = np.array(rows)
sv_ = np.linalg.svd(A, compute_uv=False)
null = A.shape[1] - np.sum(sv_ > 1e-9)
print(f"box {n}^4: unknowns {A.shape[1]}, equations {A.shape[0]}, kernel dimension = {null}")
print("smallest singular values:", np.round(np.sort(sv_)[:12], 6))
# explicit Killing fields: translations c_nu and rotations xi_nu = w_{nu mu} x_mu (position of xi_nu: x+e_nu/2)
def field(fun):
    v = np.zeros(len(unk))
    for (nu, x), i in uidx.items():
        pos = np.array(x, float); pos[nu] += 0.5
        v[i] = fun(nu, pos)
    return v
K_fields = []
for c in range(D):
    K_fields.append(field(lambda nu, p, c=c: 1.0 if nu == c else 0.0))
for a in range(D):
    for b in range(a + 1, D):
        # xi_nu = w_{nu mu} x_mu with w_ab = 1, w_ba = -1
        K_fields.append(field(lambda nu, p, a=a, b=b: (p[b] if nu == a else 0.0) - (p[a] if nu == b else 0.0)))
Kf = np.array(K_fields).T
print("max |A * (explicit translations + rotations)| =", np.abs(A @ Kf).max(),
      "; rank of the 10 explicit fields =", np.linalg.matrix_rank(Kf))
print("=> the lattice gauge map has exactly the 10 affine Killing fields of e(4):",
      "4 translations + 6 rotations, including the 3 time-space 'Euclidean boosts' (rotations in (4,j) planes).")

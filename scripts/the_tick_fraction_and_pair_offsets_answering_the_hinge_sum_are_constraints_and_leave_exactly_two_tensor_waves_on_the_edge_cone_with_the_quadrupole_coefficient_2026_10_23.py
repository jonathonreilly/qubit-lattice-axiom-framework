AUDIT_INPUT_PATHS = ('docs/THE_TICK_FRACTION_AND_PAIR_OFFSETS_ANSWERING_THE_HINGE_SUM_ARE_CONSTRAINTS_AND_LEAVE_EXACTLY_TWO_TENSOR_WAVES_ON_THE_EDGE_CONE_WITH_THE_QUADRUPOLE_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Tick-fraction waves: the time-dependent sector of the tick-fraction rule.
Variables: the site tick fraction N (tick edge, one per site), the tick offset of each neighbour
pair (mixed edge, one per spatial edge) and every spatial edge, all answering the CL-3 hinge sum.
Linearised Euclidean Regge hinge sum on prisms over the campaign's spatial triangulation (axis edges
plus even-sum face diagonals, five tetrahedra per cube, alternating; 13 edges per site), with the
Freudenthal (Kuhn) carrier as a contrast.  Transfer roots z = e^{-E} of the singular matrix polynomial
are found with a random rank-completing perturbation (true roots are perturbation-independent).
Continuum part: sympy expansion of sqrt(-g) R (SUPPLIED Regge limit) for the coefficients.
Self-contained; seeded; numpy + scipy + sympy only."""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
import sympy as sp
from scipy.linalg import eig
from sympy.calculus.euler import euler_equations

T0 = time.time()
P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

# ================= A. continuum coefficients from sqrt(-g) R (supplied Regge limit) =================
t, x, y, z, eps = sp.symbols('t x y z epsilon', real=True); X = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
def tr2(e):
    e = sp.expand(e); return sum(e.coeff(eps, k)*eps**k for k in range(3))
def sqrtg_R2(h):
    """O(eps^2) coefficient of sqrt(-g) R for g = eta + eps h (truncated series)."""
    ei = eta.inv(); A = ei*h
    gi = (ei - eps*A*ei + eps**2*A*A*ei).applyfunc(tr2); g = eta + eps*h
    sg = 1 + eps*A.trace()/2 + eps**2*(A.trace()**2/8 - (A*A).trace()/4)
    dg = [[[sp.diff(g[l, m], X[k]) for k in range(4)] for m in range(4)] for l in range(4)]
    Gm = [[[tr2(sum(gi[a, l]*(dg[l][m][k] + dg[l][k][m] - dg[m][k][l]) for l in range(4))/2)
            for k in range(4)] for m in range(4)] for a in range(4)]
    R = 0
    for m in range(4):
        for k in range(4):
            if gi[m, k] == 0: continue
            Ric = sum(sp.diff(Gm[a][m][k], X[a]) - sp.diff(Gm[a][m][a], X[k]) for a in range(4)) + \
                sum(Gm[a][a][b]*Gm[b][m][k] - Gm[a][k][b]*Gm[b][m][a] for a in range(4) for b in range(4))
            R += tr2(gi[m, k]*Ric)
    return sp.expand(tr2(sg*R)).coeff(eps, 2)
fn = lambda s: sp.Function(s)(t, z)
n_, bz, bx, c_, d_ = fn('n'), fn('bz'), fn('bx'), fn('c'), fn('d')
LS = sqrtg_R2(sp.Matrix([[-2*n_, bx, 0, bz], [bx, d_, 0, 0], [0, 0, d_, 0], [bz, 0, 0, c_]]))
ELS = {f: sp.expand(e.lhs) for f, e in zip('n bz bx c d'.split(), euler_equations(LS, [n_, bz, bx, c_, d_], [t, z]))}
second_t = [sp.diff(q, t, 2) for q in (n_, bz, bx)]
noacc = all(not e.has(q) for e in ELS.values() for q in second_t)
check("A1 lapse and shift carry no tick-to-tick acceleration: no d_t^2 of n, beta in any equation; n enters linearly",
      noacc and ELS['n'] == -2*sp.diff(d_, z, 2) and ELS['bx'] == -sp.diff(bx, z, 2),
      f"E_n = {ELS['n']}, E_bz = {ELS['bz']}, E_bx = {ELS['bx']}")
check("A2 scalar/vector sector has no wave: vacuum d = 0 (Hamiltonian constraint), bx = 0, c fixed by n, bz (gauge)",
      sp.simplify(ELS['d'].subs(d_, 0) - (sp.diff(c_, t, 2) - 2*sp.diff(n_, z, 2) - 2*sp.diff(bz, t, z))) == 0 and ELS['c'] == sp.diff(d_, t, 2),
      "E_c = d_tt; E_d|_(d=0) = c_tt - 2 n_zz - 2 bz_tz")
a_, b_ = fn('a'), fn('b')
ELT = [sp.expand(e.lhs) for e in euler_equations(sqrtg_R2(sp.Matrix([[0, 0, 0, 0], [0, a_, b_, 0], [0, b_, -a_, 0], [0, 0, 0, 0]])), [a_, b_], [t, z])]
kap = sp.Rational(1, 2)
check("A3 two tensor polarisations obey the wave equation at the hinge-sum speed: L2 = (1/2)(a_t^2 - a_z^2 + b_t^2 - b_z^2)",
      all(sp.simplify(e + 2*kap*(sp.diff(q, t, 2) - sp.diff(q, z, 2))) == 0 for e, q in zip(ELT, (a_, b_))), f"E_a = {ELT[0]}")
Phi = sp.Function('Phi')(x, y, z)
ELN = sp.expand(euler_equations(sqrtg_R2(sp.diag(-2*Phi, -2*Phi, -2*Phi, -2*Phi)), [Phi], [x, y, z])[0].lhs)
cN = sp.Rational(-2)
check("A4 static sector (gamma = 1) from the same sqrt(-g) R: L2 = -2 |grad Phi|^2",
      sp.simplify(ELN + 2*cN*sum(sp.diff(Phi, q, 2) for q in (x, y, z))) == 0, f"E_Phi = {ELN}")
v1, v2, h00, hxx, hxy, m = sp.symbols('v1 v2 h00 hxx hxy m', real=True)
Lpp = -m*sp.sqrt(1 - v1**2 - v2**2 - eps*(h00 + hxx*v1**2 + 2*hxy*v1*v2))
lin = sp.series(Lpp, eps, 0, 2).removeO().coeff(eps, 1)
check("A5 record phase -m dtau couples (1/2) h_mn T^mn (T^ij = m v^i v^j gamma)",
      sp.simplify(lin - m*(h00 + hxx*v1**2 + 2*hxy*v1*v2)/(2*sp.sqrt(1 - v1**2 - v2**2))) == 0)
G = sp.Symbol('G', positive=True)
GN = -cN*G/2            # (1/16piG)(-2c_N) lap Phi = rho  ->  lap Phi = 4 pi G_N rho
GT = G/(2*kap)          # (1/16piG)(-2kap) box a + (1/2)(T^xx - T^yy) = 0 -> box h^TT = -16 pi G_T T^TT
Kflux = kap/(16*sp.pi*G)   # outgoing-wave flux of L = (1/16piG) kap (adot^2 - a'^2 + ...) = Kflux * sum_ij hdot_ij^2 (sum_ij h^2 = 2(a^2+b^2))
# sphere moments int n^a n^b n^c dOmega (exact) and Lambda contraction for a traceless Q
def mom(a, b, c):
    if a % 2 or b % 2 or c % 2: return 0
    return 2*sp.gamma(sp.Rational(a+1, 2))*sp.gamma(sp.Rational(b+1, 2))*sp.gamma(sp.Rational(c+1, 2))/sp.gamma(sp.Rational(a+b+c+3, 2))
nx, ny, nz = sp.symbols('nx ny nz')
Qs = sp.Matrix([[2, 1, 3], [1, -5, 4], [3, 4, 3]]); nv = sp.Matrix([nx, ny, nz])
QQ = sum(Qs[i, j]**2 for i in range(3) for j in range(3)); Qn = Qs*nv; nQn = (nv.T*Qs*nv)[0]
integrand = sp.Poly(sp.expand(QQ - 2*(Qn.T*Qn)[0] + nQn**2/2), nx, ny, nz)
ILam = sum(cf*mom(*mn) for mn, cf in integrand.terms())/QQ
Pcoef = sp.simplify(Kflux * (4*GT/2)**2 * ILam)   # h^TT = (4 G_T / r) int T^TT, int T^ij = Qddot/2
Om, R0, mu = sp.symbols('Omega r mu', positive=True)
nr = sp.Matrix([sp.cos(Om*t), sp.sin(Om*t), 0]); Qb = mu*R0**2*(nr*nr.T - sp.eye(3)/3)
Q3 = Qb.diff(t, 3); circ = sp.simplify(sum(Q3[i, j]**2 for i in range(3) for j in range(3)))
check("A6 quadrupole formula from the derived coefficients: P = (G_T/5) <dddQ dddQ>, circular binary 32/5 G mu^2 r^4 Om^6",
      sp.simplify(ILam - 8*sp.pi/5) == 0 and sp.simplify(Pcoef - GT/5) == 0 and sp.simplify(circ - 32*mu**2*R0**4*Om**6) == 0,
      f"int Lambda dOmega -> {ILam}; P coef {Pcoef}; G_T/G_N = {sp.simplify(GT/GN)}")
check("A7 radiation and Newtonian couplings are one constant: G_T = G_N = G (Hulse-Taylor ratio 1)", sp.simplify(GT/GN - 1) == 0)
print(f"  (A done {time.time()-T0:.1f}s)")

# ================= B. lattice: linearised hinge sum, every edge responding =================
WO = np.array([1.0, 0.1, 0.01]); PAIRS = list(itertools.combinations(range(5), 2))
def simplex_grad5(L):
    Gm = np.array([[0.5*(L[0, i]**2 + L[0, j]**2 - L[i, j]**2) for j in range(1, 5)] for i in range(1, 5)])
    D = np.linalg.inv(np.linalg.cholesky(Gm)); nrm = [D.sum(axis=1)] + [-D[:, i] for i in range(4)]
    g = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        th = np.arccos(np.clip(-nrm[i] @ nrm[j]/np.linalg.norm(nrm[i])/np.linalg.norm(nrm[j]), -1, 1))
        a, b, c = [k for k in range(5) if k not in (i, j)]
        xx, yy, zz = L[a, b], L[b, c], L[a, c]
        A = 0.25*np.sqrt(2*xx*xx*yy*yy + 2*yy*yy*zz*zz + 2*zz*zz*xx*xx - xx**4 - yy**4 - zz**4)
        for (p, q), s, o1, o2 in (((a, b), xx, yy, zz), ((b, c), yy, xx, zz), ((a, c), zz, xx, yy)):
            g[p, q] += th*s*(o1*o1 + o2*o2 - s*s)/(8*A)
    return np.array([g[p, q] for p, q in PAIRS])
def simplex_hess(Xv):   # Richardson of central differences of the Schlaefli gradient
    L0 = np.linalg.norm(Xv[:, None, :] - Xv[None, :, :], axis=2)
    def sh(h):
        H = np.zeros((10, 10))
        for e, (a, b) in enumerate(PAIRS):
            gs = []
            for s in (1, -1):
                L = L0.copy(); L[a, b] += s*h; L[b, a] = L[a, b]; gs.append(simplex_grad5(L))
            H[e] = (gs[0] - gs[1])/(2*h)
        return H
    H = (4*sh(1e-4) - sh(2e-4))/3; return 0.5*(H + H.T)
def tri_hess(l):        # analytic Hessian of Heron's area
    A = 0.25*np.sqrt(2*l[0]**2*l[1]**2 + 2*l[1]**2*l[2]**2 + 2*l[2]**2*l[0]**2 - (l**4).sum())
    s2 = (l**2).sum(); g = l*(s2 - 2*l**2)/(8*A); H = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            H[i, j] = ((s2 - 4*l[i]**2) if i == j else 2*l[i]*l[j])/(8*A) - l[i]*(s2 - 2*l[i]**2)/(8*A*A)*g[j]
    return H
class Free:
    """prisms over a periodic 3D triangulation; spatial, tick (tick fraction) and mixed (pair offset) edges all free."""
    def __init__(self, tets, Pc, tau):
        self.P, self.tau = Pc, tau; self.cls = {}; self.flat = {}; self.vec = {}; self.kind = {}
        order = lambda vs: sorted(vs, key=lambda v: v @ WO); self.simps = []; tris = {}
        for T in tets:
            vs = order([np.array(v) for v in T])
            for j in range(4):
                V = [(vs[i], 0) for i in range(j+1)] + [(vs[i], 1) for i in range(j, 4)]
                Xv = np.array([np.r_[v, tau*tt] for v, tt in V], float)
                self.simps.append((simplex_hess(Xv), [self.edge(V[a], V[b]) for a, b in PAIRS]))
                for tri in itertools.combinations(range(5), 3):
                    W = [V[i] for i in tri]; shf = np.r_[np.floor_divide(W[0][0], Pc)*Pc, W[0][1]]
                    key = tuple(sorted(tuple(np.r_[w[0], w[1]] - shf) for w in W))
                    if key not in tris:
                        prs = ((0, 1), (1, 2), (0, 2))
                        l = np.array([np.linalg.norm(np.r_[W[b][0] - W[a][0], tau*(W[b][1] - W[a][1])]) for a, b in prs])
                        tris[key] = (tri_hess(l), [self.edge(W[a], W[b]) for a, b in prs])
        self.tris = list(tris.values()); self.n = len(self.cls)
        self.kinds = np.array([self.kind[c] for c in range(self.n)])
    def edge(self, A, B):
        (a, ta), (b, tb) = A, B
        if (ta, a @ WO) > (tb, b @ WO): (a, ta), (b, tb) = (b, tb), (a, ta)
        kd = 's' if ta == tb else ('t' if np.array_equal(a, b) else 'm')
        key = (kd, tuple(np.mod(a, self.P)), tuple(b - a))
        if key not in self.cls:
            c = len(self.cls); self.cls[key] = c; self.kind[c] = kd
            dv = np.r_[b - a, self.tau*(tb - ta)].astype(float); self.vec[c] = dv; self.flat[c] = np.linalg.norm(dv)
        return (self.cls[key], a, min(ta, tb))
    def Q(self, k):
        M = np.zeros((self.n, self.n), complex)
        def J(eds):
            r = np.zeros((len(eds), self.n), complex)
            for i, (c, a, tt) in enumerate(eds): r[i, c] = np.exp(1j*(k[:3] @ a + k[3]*tt))
            return r
        for H, eds in self.tris:
            Jm = J(eds); M += 2*np.pi*Jm.conj().T @ H @ Jm
        for H, eds in self.simps:
            Jm = J(eds); M -= Jm.conj().T @ H @ Jm
        return 0.5*(M + M.conj().T)
    def G(self, k):     # vertex displacements (4 per cell site) -> edge lengths
        sites = list(itertools.product(range(self.P), repeat=3)); si = {s: i for i, s in enumerate(sites)}
        Gm = np.zeros((self.n, 4*len(sites)), complex)
        for (kd, a, dv), c in self.cls.items():
            a = np.array(a); bvec = a + np.array(dv); tb = 0 if kd == 's' else 1; u = self.vec[c]/self.flat[c]
            ib = si[tuple(np.mod(bvec, self.P))]; ia = si[tuple(a)]
            Gm[c, 4*ib:4*ib+4] += u*np.exp(1j*(k[:3] @ (bvec - a) + k[3]*tb)); Gm[c, 4*ia:4*ia+4] -= u
        return Gm
    def M(self, k):     # smooth metric (10) -> edge lengths, line-averaged
        out = np.zeros((self.n, 10), complex)
        for (kd, a, dv), c in self.cls.items():
            d = self.vec[c]; l = self.flat[c]; pd = k[:3] @ d[:3] + k[3]*d[3]/self.tau
            f = 1.0 if abs(pd) < 1e-14 else (np.exp(1j*pd) - 1)/(1j*pd)
            for s, (i, j) in enumerate(SYM): out[c, s] = (1 if i == j else 2)*d[i]*d[j]/(2*l)*f*np.exp(1j*(k[:3] @ np.array(a, float)))
        return out
SYM = [(i, j) for i in range(4) for j in range(i, 4)]
def kuhn_tets():
    out = []
    for p in itertools.permutations(range(3)):
        v = [np.zeros(3, int)]
        for j in p:
            w = v[-1].copy(); w[j] = 1; v.append(w)
        out.append(v)
    return out
def five_tets():
    out = []
    for o in itertools.product((0, 1), repeat=3):
        o = np.array(o); C = [o + np.array(c) for c in itertools.product((0, 1), repeat=3)]
        ev = [c for c in C if c.sum() % 2 == 0]; out.append(ev)
        for q in [c for c in C if c.sum() % 2 == 1]: out.append([q] + [c for c in ev if np.abs(c - q).sum() == 1])
    return out
def fourier(Qf, ks, Nt=8):
    kts = 2*np.pi*np.arange(Nt)/Nt; Ms = [Qf(np.r_[ks, tt]) for tt in kts]
    C = {n: sum(Mm*np.exp(-1j*n*tt) for Mm, tt in zip(Ms, kts))/Nt for n in range(-3, 4)}
    return [C[-1], C[0], C[1]], max(np.abs(C[n]).max() for n in (-3, -2, 2, 3))
def true_roots(C, nul, tol=1e-7):
    d = C[0].shape[0]; A = np.zeros((2*d, 2*d), complex); B = np.eye(2*d, dtype=complex)
    A[:d, d:] = np.eye(d); A[d:, :d] = -C[0]; A[d:, d:] = -C[1]; B[d:, d:] = C[2]
    zs = []
    for sd in (1, 2):
        r = np.random.default_rng(sd)
        U = r.normal(size=(2*d, nul)) + 1j*r.normal(size=(2*d, nul)); V = r.normal(size=(2*d, nul)) + 1j*r.normal(size=(2*d, nul))
        zs.append(eig(A + U @ np.diag(r.normal(size=nul)) @ V.conj().T, B + U @ np.diag(r.normal(size=nul)) @ V.conj().T, right=False))
    zz = np.array([q for q in zs[0] if np.isfinite(q) and abs(q) > 1e-30 and np.min(np.abs(zs[1] - q)) < tol*max(1, abs(q))])
    E = -np.log(zz.astype(complex)); return E[np.abs(E) < 15], len(zz)
Qz = lambda C, zv: C[0]/zv + C[1] + C[2]*zv
srel = lambda Mm: (lambda e: int(np.sum(np.abs(e) < 1e-8*np.abs(e).max())))(np.linalg.eigvalsh(Mm))
disp = lambda ks, tau: 2*np.arcsinh(tau*np.sqrt(np.sum(np.sin(np.asarray(ks)/2)**2)))
rng = np.random.default_rng(20261023)

F6 = Free(five_tets(), 2, 1.0); FK = Free(kuhn_tets(), 1, 1.0)
cnt = {kd: int((F6.kinds == kd).sum())//8 for kd in 'stm'}
kr = [rng.uniform(-np.pi, np.pi, 4) for _ in range(2)]
nul6 = [srel(F6.Q(k)) for k in kr]; gres = max(np.linalg.norm(F6.Q(k) @ F6.G(k))/np.linalg.norm(F6.Q(k)) for k in kr)
check("B1 campaign carrier, every edge responding: 13 edges/site; generic null space = vertex displacements only (no zero-action branch)",
      cnt == {'s': 6, 't': 1, 'm': 6} and nul6 == [32, 32] and gres < 1e-9, f"per site {cnt}; nullity {nul6} = 4 x 8 sites; |QG|/|Q| {gres:.0e}")
# Kuhn contrast: the extra zero-action direction and its cell-averaged metric
nulK = srel(FK.Q(kr[0]))
def kuhn_v0(kk):
    k = kk*np.array([0.3, 0.5, 0.7, 0.4])/np.linalg.norm([0.3, 0.5, 0.7, 0.4]); Qk = FK.Q(k); Gk = FK.G(k)
    w, U = np.linalg.eigh(Qk); Ns = U[:, np.abs(w) < 1e-8*np.abs(w).max()]
    Pg = np.eye(FK.n) - Gk @ np.linalg.pinv(Gk); u, s, _ = np.linalg.svd(Pg @ Ns); v0 = u[:, 0]
    gs = []   # per-4-simplex metric from its 10 edge lengths, then the cell average (24 equal simplices)
    for p in itertools.permutations(range(4)):
        vv = [np.zeros(4, int)]
        for j in p:
            q = vv[-1].copy(); q[j] = 1; vv.append(q)
        A = np.zeros((10, 10)); bb = np.zeros(10, complex)
        for r, (a, b) in enumerate(PAIRS):
            dv = (vv[b] - vv[a]).astype(float); key = ('s' if dv[3] == 0 else ('t' if not dv[:3].any() else 'm'), (0, 0, 0), tuple(int(q) for q in dv[:3]))
            c = FK.cls[key]
            for s_, (i, j) in enumerate(SYM): A[r, s_] = (1 if i == j else 2)*dv[i]*dv[j]
            bb[r] = 2*FK.flat[c]*v0[c]*np.exp(1j*k @ vv[a])
        gs.append(np.linalg.solve(A, bb))
    gav = np.mean(gs, axis=0)
    Gg = np.zeros((10, 4), complex)
    for mm in range(4):
        for s_, (i, j) in enumerate(SYM): Gg[s_, mm] = 1j*(k[i]*(mm == j) + k[j]*(mm == i))
    return np.linalg.norm(gav - Gg @ np.linalg.lstsq(Gg, gav, rcond=None)[0]), np.linalg.norm(v0[FK.kinds != 's'])
kv = [kuhn_v0(q) for q in (0.05, 0.025)]
check("B2 contrast, Freudenthal (Kuhn) carrier: nullity 5 = 4 displacements + 1 zero-action non-metric branch at every k",
      nulK == 5 and min(q[0] for q in kv) > 0.3,
      f"its cell-averaged metric keeps a non-gauge part {kv[0][0]:.2f}, {kv[1][0]:.2f} at |k| = .05, .025 (no decay); weight on tick/mixed edges {kv[0][1]:.2f}")
mI = np.where(F6.kinds != 's')[0]; hI = np.where(F6.kinds == 's')[0]
ks0 = 0.02*np.array([0.3, 0.5, 0.8])/np.linalg.norm([0.3, 0.5, 0.8]); C0, leak = fourier(F6.Q, ks0)
mm_t = max(np.abs(C0[0][np.ix_(mI, mI)]).max(), np.abs(C0[2][np.ix_(mI, mI)]).max())
tcols = [4*i + 3 for i in range(8)]
# time displacement u_t: m-rows at z^0 and z^1 (A + B z); both must lie in null(Q_mm)
kt_ = 2*np.pi*np.arange(4)/4; Gs = [F6.G(np.r_[ks0, q])[:, tcols] for q in kt_]
GA = sum(g*np.exp(-0j*q) for g, q in zip(Gs, kt_))/4; GB = sum(g*np.exp(-1j*q) for g, q in zip(Gs, kt_))/4
Qmm = C0[1][np.ix_(mI, mI)]; w, U = np.linalg.eigh(Qmm); Nmm = U[:, np.abs(w) < 1e-8*np.abs(w).max()]
TG = np.c_[GA[mI], GB[mI]]; inspan = np.linalg.norm(TG - Nmm @ (Nmm.conj().T @ TG))/np.linalg.norm(TG)
check("B3 tick fractions and pair offsets are constraints (derived): their block has no tick-to-tick coupling; its null space = time relabelling",
      mm_t < 1e-12 and np.abs(C0[2][np.ix_(hI, mI)]).max() < 1e-12 and Nmm.shape[1] == 16 and np.linalg.matrix_rank(TG, 1e-6) == 16 and inspan < 1e-6,
      f"|Q_mm z^+-1| {mm_t:.0e}; null(Q_mm) dim {Nmm.shape[1]} = 2 x 8 sites, spanned by the time-displacement parts to {inspan:.0e}; Fourier leak {leak:.0e}")
# root census at |k| = 0.02: every finite root is the tensor branch at one of the 8 folded momenta
cens = []
for dd in ((0, 0, 1), (1, 1, 1), (0.3, 0.5, 0.8)):
    ks = 0.02*np.array(dd)/np.linalg.norm(dd); C, _ = fourier(F6.Q, ks); E, ntr = true_roots(C, 32)
    pred = np.sort(np.concatenate([[s*disp(ks + np.pi*np.array(gv), 1.0)]*2 for gv in itertools.product((0, 1), repeat=3) for s in (1, -1)]))
    Er = np.sort(E.real); ok = len(E) == 32 and np.abs(E.imag).max() < 1e-6 and np.abs(Er - pred).max() < 1e-6
    light = Er[np.abs(Er) < 0.1]
    cens.append((ok, len(E), len(light), np.abs(np.abs(light)/0.02 - 1).max(), np.abs(Er - pred).max()))
check("B4 transfer census, all edges responding: 32 finite roots/cell = 2 polarisations x (+-E) x 8 folded momenta, nothing else",
      all(c[0] for c in cens), "; ".join(f"{c[1]} roots, light {c[2]} at |E/k-1| <= {c[3]:.1e}, max dev from tensor branch {c[4]:.0e}" for c in cens))
print("  INFO fixed lapse + zero shift on the same carrier (edge-modes E3): 4 light roots plus 48-50 zero-frequency roots; responding N and offsets remove them")
# polarisations at the light root
pol = []
for kk in (0.05, 0.025):
    ks = kk*np.array([0.3, 0.5, 0.8])/np.linalg.norm([0.3, 0.5, 0.8]); C, _ = fourier(F6.Q, ks); E, _ = true_roots(C, 32)
    e = np.sort(E.real[(E.real > 0) & (E.real < 0.5)])[0]; Qr = Qz(C, np.exp(-e)); _, s, Vh = np.linalg.svd(Qr)
    nul = int(np.sum(s < 1e-7*s[0])); Ns = Vh[-nul:].conj().T; pc = np.r_[ks, 1j*e]
    Qg = np.linalg.qr(F6.G(pc))[0]; Rm = Ns - Qg @ (Qg.conj().T @ Ns); u, sv, _ = np.linalg.svd(Rm); phys = u[:, :nul - 32]
    Am = np.c_[F6.M(pc), F6.G(pc)]; res = []
    for vv in phys.T:
        xx = np.linalg.lstsq(Am, vv, rcond=None)[0]; h = np.zeros((4, 4), complex)
        for s_, (i, j) in enumerate(SYM): h[i, j] = h[j, i] = xx[s_]
        Ee = np.array([[pc[3]**2*h[i, j] + pc[i]*pc[j]*h[3, 3] - pc[3]*pc[j]*h[i, 3] - pc[3]*pc[i]*h[3, j] for j in range(3)] for i in range(3)])
        kh = ks/np.linalg.norm(ks)
        res.append((np.linalg.norm(Am @ xx - vv), abs(np.trace(Ee))/np.linalg.norm(Ee), np.linalg.norm(Ee @ kh)/np.linalg.norm(Ee)))
    pol.append((nul, np.max([r[0] for r in res]), np.max([max(r[1], r[2]) for r in res])))
check("B5 at the light root the null space is displacements + exactly 2 physical vectors, both transverse-traceless tensor waves",
      all(p[0] == 34 and p[2] < 1e-3 for p in pol) and pol[1][1] < pol[0][1],
      f"nullity {pol[0][0]}, {pol[1][0]} = 32 + 2; electric curvature trace/longitudinal part <= {max(p[2] for p in pol):.0e}; non-metric admixture {pol[0][1]:.3f} -> {pol[1][1]:.3f} at |k| = .05 -> .025")
# exact lattice dispersion at large k, two tick lengths
F7 = Free(five_tets(), 2, 0.7); dev = 0; ndeg = 0
for Fc, tau in ((F6, 1.0), (F7, 0.7)):
    for kx in (0.3, 1.0, 1.5):
        for dd in ((0, 0, 1), (1, 1, 1), (0.3, 0.5, 0.8)):
            ks = kx*np.array(dd)/np.linalg.norm(dd); C, _ = fourier(Fc.Q, ks); E, _ = true_roots(C, 32)
            Er = E.real[(np.abs(E.imag) < 1e-6) & (E.real > 0)]; pr = disp(ks, tau)
            near = np.sort(np.abs(Er - pr))[:2]; dev = max(dev, near.max()); ndeg += int(near.max() < 1e-6)
check("B6 tensor branch (both polarisations, degenerate) is exactly sinh(E/2) = tau [sum_i sin^2(k_i/2)]^(1/2) out to |k| = 1.5",
      dev < 1e-6 and ndeg == 18, f"18 (k, direction, tau) cases, max |E - formula| {dev:.0e}; tau = tick edge / spatial edge (E = tau|k| at small k: the edge cone)")
# single normalisation: effective action on smooth metrics (non-metric modes respond) vs Gamma-Gamma form
def L2gg(p):
    Bt = np.zeros((10, 4, 4, 4), complex)
    for s_, (i, j) in enumerate(SYM):
        h = np.zeros((4, 4)); h[i, j] = h[j, i] = 1
        Bt[s_] = 0.5j*(np.einsum('m,an->amn', p, h) + np.einsum('n,am->amn', p, h) - np.einsum('a,mn->amn', p, h))
    Mq = np.einsum('samb,rbma->sr', Bt.conj(), Bt) - np.einsum('samm,rbab->sr', Bt.conj(), Bt)
    return 0.5*(Mq + Mq.conj().T)
dd4 = np.array([0.3, 0.5, 0.7, 0.4]); dd4 /= np.linalg.norm(dd4); fits = []
for kk in (0.02, 0.01):
    k = kk*dd4; Qk = F6.Q(k); Mk = F6.M(k); U, s, _ = np.linalg.svd(Mk); Xc = U[:, 10:]
    Cm = Xc.conj().T @ Qk @ Xc; w, V = np.linalg.eigh(Cm); keep = np.abs(w) > 1e-7*np.abs(w).max()
    Ci = (V[:, keep]/w[keep]) @ V[:, keep].conj().T; Bm = Mk.conj().T @ Qk @ Xc
    Qe = Mk.conj().T @ Qk @ Mk - Bm @ Ci @ Bm.conj().T; Lk = L2gg(k)
    cfit = np.vdot(Lk.ravel(), Qe.ravel()).real/np.vdot(Lk.ravel(), Lk.ravel()).real
    fits.append((cfit, np.linalg.norm(Qe - cfit*Lk)/np.linalg.norm(Qe)))
pz = np.array([0, 0, 1.0, 0]); hT = np.zeros(10); hN = np.zeros(10)
hT[SYM.index((0, 0))], hT[SYM.index((1, 1))] = 1, -1
for i in range(3): hN[SYM.index((i, i))] = -2
hN[SYM.index((3, 3))] = 2
ratio = (hN @ L2gg(pz) @ hN).real/(hT @ L2gg(pz) @ hT).real
check("B7 one coefficient for every metric component: lattice effective action = c x Gamma-Gamma form, residual falling as k^2",
      abs(fits[1][0] - 8) < 1e-3 and fits[1][1] < 2e-5 and fits[0][1]/fits[1][1] > 3.5 and abs(ratio - 4) < 1e-12,
      f"c = {fits[0][0]:.5f}, {fits[1][0]:.5f} (cell 4-volume 8); rel resid {fits[0][1]:.1e}, {fits[1][1]:.1e}; static Newtonian/TT ratio {ratio:.3f} = sympy's (-2)/(-1/2) = 4")
e00 = np.zeros(10); e00[SYM.index((3, 3))] = 1
check("B8 a uniform change of the tick edge is a zero of the hinge sum: the flat tick/edge ratio tau is not fixed by it",
      np.linalg.norm(F6.Q(np.zeros(4)) @ F6.M(np.zeros(4)) @ e00) < 1e-9)
print(f"  (B done {time.time()-T0:.1f}s)")

# ================= C. speed tie, lattice dispersion and measurement =================
# Lorentzian reading (SUPPLIED continuation tau^2 -> -tau^2, E -> i w): sin(w/2) = tau s(k); c(k) = w/(tau |k|)
kh = np.array([0.3, 0.5, 0.8]); kh /= np.linalg.norm(kh); kq = 1e-3; tau_ = 0.4
wq = 2*np.arcsin(tau_*np.sqrt(np.sum(np.sin(kq*kh/2)**2))); cq = wq/(tau_*kq) - 1
form = kq**2/24*(tau_**2 - np.sum(kh**4))
check("C1 lattice graviton speed c(k) = 1 + (ka)^2 (tau^2 - sum khat_i^4)/24; with CL-1's tick (tau = sin eps/sqrt 3 <= 1/sqrt 3) never superluminal",
      abs(cq - form) < 1e-3*abs(form), f"exact {cq:.4e} vs formula {form:.4e} at ka = 1e-3; sum khat^4 >= 1/3 >= tau^2")
print("  INFO speed tie: graviton label speed = tau (blocks per tick, B6); walk light speed = sin(eps)/sqrt 3 (CL-1 band).",
      "Equal iff tau = sin(eps)/sqrt 3: CL-1's clause that the tick is that fraction of the edges' light crossing (B8: the hinge sum leaves tau free)")
cl = 2.998e8; kGW = 2*np.pi*100/cl; Lc = 8.1e-35
dcmax = (kGW*Lc*100)**2/24; amax = np.sqrt(24*3e-15)/kGW
check("C2 GW170817 (-3e-15 < dc < 7e-16): lattice term at 100 Hz <= 1e-76 for block edges up to 100 cells of 8.1e-35 m",
      dcmax < 3e-15, f"|dc| <= {dcmax:.1e}; GW170817 alone bounds the step only to a < {amax:.2f} m; at k->0 c_gw = c_light exactly given the tie")
ht, hs = 0.9983, 0.0016
check("C3 Hulse-Taylor: Pbdot(rule)/Pbdot(GR) = G_T/G_N = 1 vs 0.9983 +- 0.0016", abs(1 - ht)/hs < 2,
      f"{abs(1-ht)/hs:.2f} sigma; a separate tensor coupling (e.g. 0.81, unsubtracted sea) is off by {abs(0.81-ht)/hs:.0f} sigma")
check("C4 no scalar, vector or breathing mode at any k (B4/B5/A2): no dipole or breathing radiation",
      all(c[0] for c in cens) and all(p[0] == 34 for p in pol))
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")

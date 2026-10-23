AUDIT_INPUT_PATHS = ('docs/ONE_G_THE_HINGE_SUMS_NEWTONIAN_KERNEL_IS_EXACTLY_THE_LATTICE_LAPLACIAN_ISOTROPIC_AT_LONG_WAVELENGTH_WITH_ONE_FREE_SCALE_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""One G: is there one Newton constant under the adopted rules, and is it isotropic?
Adopted content: the CL-3 hinge sum (coefficient kappa, register text: one) on the six-edge carrier
(prisms over the campaign's spatial triangulation: axis edges plus even-sum face diagonals, five
tetrahedra per cube; 13 edges per site), with the tick fraction N, the pair offsets and every spatial
edge responding (CL-1 tick-fraction clause); Freudenthal (Kuhn) carrier as a contrast.
A. static Newtonian kernel: the response of the tick edges (where a record's phase -m dtau couples)
   to a static tick-edge source, every other edge responding; its k-direction dependence; normalisation
   against the static reduction of (kappa/2) int sqrt(g) R (sympy; SUPPLIED Regge limit).
B. which area the hinge sum uses (Heron areas in the edges' own lengths) versus the count area.
C. the value: scale-freeness of the hinge sum, Regge replica entropy with the same kappa, the vacuum
   standard removing the induced (Sakharov) term (toy), and the supplied lattice numbers of the
   entanglement and induced routes.
Self-contained; seeded (20261023); numpy + scipy + sympy only."""
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

# ---------- linearised Euclidean Regge hinge sum on prisms (every edge responding) ----------
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

rng = np.random.default_rng(20261023)
lap = lambda ks: 4*np.sum(np.sin(np.asarray(ks, float)/2)**2)     # nearest-neighbour lattice Laplacian symbol
def kernel(Fc, ks):
    """static tick-edge kernel: source on every site's tick edge (plane wave), every other edge responding."""
    tI = np.where(Fc.kinds == 't')[0]; Q = Fc.Q(np.r_[ks, 0.0])
    Qp = np.linalg.pinv(Q, rcond=1e-9, hermitian=True); one = np.ones(len(tI))
    return 1/((one @ Qp[np.ix_(tI, tI)] @ one).real/len(tI))

# ================= A. the static Newtonian kernel and its direction dependence =================
F6 = Free(five_tets(), 2, 1.0)
dev8 = max(abs(kernel(F6, 2*np.pi*np.array(n)/8)/(-2*lap(2*np.pi*np.array(n)/8)) - 1)
           for n in itertools.product(range(8), repeat=3) if any(n))
w16 = [n for n in itertools.product(range(9), repeat=3) if n[0] >= n[1] >= n[2] and any(n)]
dev16 = max(abs(kernel(F6, 2*np.pi*np.array(n)/16)/(-2*lap(2*np.pi*np.array(n)/16)) - 1) for n in w16)
check("A1 six-edge carrier, every edge responding: the static tick-edge kernel is exactly -2 x the nearest-neighbour Laplacian",
      dev8 < 1e-6 and dev16 < 1e-6, f"K(k) = -2 * 4 sum_i sin^2(k_i/2): all 511 momenta of the 8^3 torus, max rel dev {dev8:.0e}; {len(w16)} wedge momenta of 16^3, {dev16:.0e}")
F7 = Free(five_tets(), 2, 0.7); FK = Free(kuhn_tets(), 1, 1.0); dv7 = dvK = 0
for d in ((1, 0, 0), (1, 1, 1), (0.3, 0.5, 0.8)):
    for kk in (0.05, 0.7, 2.0):
        ks = kk*np.array(d)/np.linalg.norm(d)
        dv7 = max(dv7, abs(0.7*kernel(F7, ks)/(-2*lap(ks)) - 1)); dvK = max(dvK, abs(kernel(FK, ks)/(-2*lap(ks)) - 1))
check("A2 the same kernel at tick/edge ratio tau = 0.7 (K = -2 lap/tau, i.e. -2 lap per proper 4-volume in Phi = dN/tau) and on the Kuhn carrier",
      dv7 < 1e-6 and dvK < 1e-6, f"9 (k, direction) cases each, max rel dev {dv7:.0e} (tau = .7), {dvK:.0e} (Kuhn): G does not depend on the free ratio tau or on the carrier")
dirs = {'100': (1, 0, 0), '110': (1, 1, 0), '111': (1, 1, 1)}
def ratio(kk, d):
    d = np.array(d, float)/np.linalg.norm(d); return kernel(F6, kk*d)/(-2*kk**2), lap(kk*d)/kk**2
r0 = {n: ratio(0.02, d) for n, d in dirs.items()}; r16 = {n: ratio(2*np.pi/16, d) for n, d in dirs.items()}
sp0 = max(v[0] for v in r0.values()) - min(v[0] for v in r0.values())
sp16 = r16['111'][0] - r16['100'][0]; pr16 = r16['111'][1] - r16['100'][1]; lo16 = (2*np.pi/16)**2/18
check("A3 long-wavelength isotropy: K/(-2|k|^2) -> 1 along (100), (110), (111); the only anisotropy is the Laplacian's, 1 - (ka)^2 sum khat^4/12 + ...",
      sp0 < 1e-4 and abs(sp16 - pr16) < 1e-6 and all(abs(v[0] - v[1]) < 1e-6 for v in list(r0.values()) + list(r16.values())),
      f"|k| = .02: " + ", ".join(f"{n} {v[0]:.6f}" for n, v in r0.items()) + f"; |k| = 2pi/16: " + ", ".join(f"{n} {v[0]:.5f}" for n, v in r16.items())
      + f" (spread {sp16:.5f} = Laplacian's {pr16:.5f}; leading k^2/18 = {lo16:.5f})")
print("  INFO torus momenta 2pi n/L, n = (100), (110), (111): K/(-2|k|^2) = " + "; ".join(
      f"L={L}: " + ", ".join(f"{kernel(F6, 2*np.pi/L*np.array(d))/(-2*(2*np.pi/L)**2*sum(d)):.5f}" for d in dirs.values()) for L in (8, 12, 16)))
# continuum normalisation: static reduction of sqrt(-g) R with lapse Phi and spatial conformal Psi
t, x, y, z, eps = sp.symbols('t x y z epsilon', real=True); X = [t, x, y, z]; eta = sp.diag(-1, 1, 1, 1)
def tr2(e):
    e = sp.expand(e); return sum(e.coeff(eps, k)*eps**k for k in range(3))
def sqrtg_R2(h):
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
Phi, Psi = sp.Function('Phi')(x, y, z), sp.Function('Psi')(x, y, z); lp = lambda f: sum(sp.diff(f, q, 2) for q in (x, y, z))
L2 = sqrtg_R2(sp.diag(-2*Phi, -2*Psi, -2*Psi, -2*Psi))
E_Psi = sp.expand(euler_equations(L2, [Phi, Psi], [x, y, z])[1].lhs)
E_red = sp.expand(euler_equations(L2.subs(Psi, Phi).doit(), [Phi], [x, y, z])[0].lhs)
kap = sp.Symbol('kappa', positive=True); Gs = sp.Symbol('G', positive=True)
okA4 = sp.simplify(E_Psi + 4*lp(Psi - Phi)) == 0 and sp.simplify(E_red - 4*lp(Phi)) == 0
# action (kappa/2) int sqrt g R; Hessian convention S = (1/2) Phi* K Phi: K = (kappa/2)(-2)(2)|k|^2 = -2 kappa |k|^2; lattice -2 lap => kappa = 1
Gsol = sp.solve(sp.Eq(1/(16*sp.pi*Gs), kap/2), Gs)[0]
check("A4 normalisation: static reduction of (kappa/2) sqrt(g) R gives Psi = Phi and K_Phi = -2 kappa |k|^2: the lattice's -2 is kappa = 1, so G_N = 1/(8 pi kappa)",
      okA4 and sp.simplify(Gsol - 1/(8*sp.pi*kap)) == 0, f"E_Psi = -4 lap(Psi - Phi); reduced E_Phi = 4 lap Phi; G = {Gsol}; Poisson lap Phi = 4 pi G rho from the phase -m dtau")
print(f"  (A done {time.time()-T0:.1f}s)")

# ================= B. which area the hinge sum uses =================
sv = [F6.vec[c][:3] for c in range(F6.n) if F6.kinds[c] == 's']
dens = {n: sum(abs(v @ (np.array(d)/np.linalg.norm(d))) for v in sv)/8 for n, d in dirs.items()}
dax = {n: np.sum(np.abs(d))/np.linalg.norm(d) for n, d in dirs.items()}
tz = set()
for T in five_tets():
    for tri in itertools.combinations([tuple(v) for v in T], 3):
        if all(v[2] == 0 for v in tri): tz.add(tuple(sorted(tri)))
def heron(p):
    a, b, c = (np.linalg.norm(np.subtract(p[i], p[j])) for i, j in ((0, 1), (1, 2), (0, 2))); s = (a + b + c)/2
    return np.sqrt(s*(s - a)*(s - b)*(s - c))
hz = sum(heron(tr) for tr in tz)/4
check("B1 count area is direction dependent on the six-edge carrier, but the hinge sum's area is each hinge's Heron area in the edges' own lengths",
      max(dens.values())/min(dens.values()) - 1 > 0.1 and abs(hz - 1) < 1e-12 and sp0 < 1e-4,
      "edges crossed per Euclidean area " + ", ".join(f"{n} {v:.4f}" for n, v in dens.items()) + f" (max/min {max(dens.values())/min(dens.values()):.3f}; axis edges alone "
      + ", ".join(f"{v:.4f}" for v in dax.values()) + f"); Heron area of the carrier's (100) hinges per unit area {hz:.12f}; the kernel built from those areas is isotropic (A3)")

# ================= C. the value of G =================
n_, A_ = sp.symbols('n A', positive=True); I1 = sp.Symbol('I1')
logZ = kap*A_*2*sp.pi*(1 - n_) - n_*I1          # -I_n, I_n = -kappa A delta_n + n I_1, deficit delta_n = 2 pi (1 - n)
S = sp.simplify((logZ - n_*sp.diff(logZ, n_)).subs(n_, 1))
check("C1 replica entropy of the same hinge sum: S = (1 - n d/dn) ln Z_n = 2 pi kappa A = A/(4G) with G = 1/(8 pi kappa) (the Newtonian G of A4)",
      sp.simplify(S - A_/(4*Gsol)) == 0, f"S = {S}")
Xv = np.eye(5, 4) + 0.15*rng.normal(size=(5, 4)); Xv[4] = -0.3
hs = np.abs(simplex_hess(3*Xv) - simplex_hess(Xv)).max()/np.abs(simplex_hess(Xv)).max()
lt = np.array([1.0, 1.2, 0.9]); ht = np.abs(tri_hess(3*lt) - tri_hess(lt)).max()
check("C2 the hinge sum is homogeneous of degree 2 in the edges, so its Hessian is unit-free: kappa is its only number",
      hs < 1e-6 and ht < 1e-12, f"random 4-simplex scaled x3: Hessian rel change {hs:.0e}; Heron Hessian {ht:.0e}; the register size s, its step and the block size b_e do not enter, so 8 pi G = u^2/kappa in whatever unit u the edges are counted")
def ring_H(h):
    N = len(h); Hm = np.zeros((N, N))
    for i in range(N): Hm[i, (i+1) % N] = Hm[(i+1) % N, i] = -np.exp(-h[i])
    return Hm
def ring_E(h, nf, occ): return nf*np.linalg.eigvalsh(ring_H(h))[:occ].sum()
def proj(h, occ):
    w, U = np.linalg.eigh(ring_H(h)); return U[:, :occ] @ U[:, :occ].T
N = 10; mod = np.cos(2*np.pi*2*np.arange(N)/N); dh = 1e-3; P0 = proj(0*mod, 5)
d2 = lambda f: (f(dh*mod) - 2*f(0*mod) + f(-dh*mod))/dh**2
raw = {nf: d2(lambda h: ring_E(h, nf, 5)) for nf in (1, 2)}
fixd = d2(lambda h: ring_E(h, 1, 5) - np.trace(P0 @ ring_H(h)))
sub = max(abs(np.trace(proj(h, 5) @ ring_H(h)) - ring_E(h, 1, 5)) for h in rng.normal(0, .3, (5, N)))
check("C3 Sakharov route under the vacuum standard (toy ring, 10 sites, 5 fermions): the induced edge term scales with content and the same-edge vacuum removes it whole",
      abs(raw[1]) > 0.1 and abs(raw[2]/raw[1] - 2) < 1e-6 and abs(fixd) > 0.01 and sub < 1e-12,
      f"raw d2E0/dh2 {raw[1]:.4f} (N_f = 1), {raw[2]:.4f} (N_f = 2); a fixed flat reference leaves {fixd:.4f}; the vacuum of the same edges leaves {sub:.0e} at 5 random edge sets")
eta_D = 0.19664/2; cG = {'staggered': 0.004966, 'Wilson': 0.01032}
ind = {k: 4*np.pi*v for k, v in cG.items()}; rat = {k: v/eta_D for k, v in ind.items()}
check("C4 SUPPLIED lattice numbers: the sea's induced 1/(4G) and its entanglement area coefficient differ at O(1) and by regulator (no lattice identity)",
      all(abs(r - 1) > 0.2 for r in rat.values()),
      f"per Dirac: entanglement {eta_D:.4f}, induced 4 pi c_G " + ", ".join(f"{k} {v:.4f} (ratio {rat[k]:.3f})" for k, v in ind.items())
      + f"; hinge 1/(4G) = 2 pi kappa per u^2 = {np.pi/2:.4f} per site^2 (cell rung u = 2 sites) or {2*np.pi:.4f} (site)")
print("  INFO under the vacuum standard both sea routes are vacuum shares on the same edges: the induced action is subtracted (C3) and its paired")
print("       entanglement (Susskind-Uglum/Kabat pairing, continuum, SUPPLIED) is matter entropy, not a second G")
au, cell = 1.496e11, 8.10e-35
an = (2*np.pi/au*100*cell)**2/18
check("C5 measurement: G's direction dependence at 1 AU on blocks of <= 100 cells is (ka)^2/18, far below preferred-location bounds (|xi| < 3.9e-9, supplied)",
      an < 3.9e-9, f"{an:.1e}; the count reading's factor 1.48 does not apply to the hinge sum")
check("C6 one G: Newtonian (A1, A4), horizon entropy (C1) and, citing tick-fraction-waves, tensor waves all carry 1/(8 pi kappa); independent of tau, carrier and content",
      okA4 and dev8 < 1e-6 and dv7 < 1e-6 and dvK < 1e-6 and sub < 1e-12 and sp.simplify(S - A_/(4*Gsol)) == 0)
print("  INFO value: kappa = 1 (CL-3 text) names the cell rung u = sqrt(8 pi) l_P (hbar c/u = 2.435e18 GeV, the reduced Planck mass): a units statement, not a derived number")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")

AUDIT_INPUT_PATHS = ('docs/D4_EVENT_SET_ROOT_SLICED_HINGE_SUM_GRAVITY_CARRY_OVER_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-gravity: does the adopted gravity sector carry over to the D4 event set sliced along a root?
Carrier: D4 events, Delaunay 16-cells coned from their centres (the deep holes, i.e. the Voronoi
24-cell vertices); W(F4)-symmetric. Linearised Euclidean Regge hinge sum, every edge responding.
Time = root t = (1,1,0,0)/sqrt2. Analytic continuation uses the opposite-momentum transpose.
Self-contained; seeded; numpy + scipy only."""
AUDIT_TIMEOUT_SEC = 120
import itertools, time
import numpy as np
from scipy.linalg import eig

T0 = time.time(); P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))
rng = np.random.default_rng(20261026)
PAIRS = list(itertools.combinations(range(5), 2))

# ---------------- Regge pieces (inlined from tick-fraction-waves) ----------------
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
def dihedrals(L):   # dihedral angle at each of the 10 triangles (opposite pair i,j)
    Gm = np.array([[0.5*(L[0, i]**2 + L[0, j]**2 - L[i, j]**2) for j in range(1, 5)] for i in range(1, 5)])
    D = np.linalg.inv(np.linalg.cholesky(Gm)); nrm = [D.sum(axis=1)] + [-D[:, i] for i in range(4)]
    out = {}
    for i, j in itertools.combinations(range(5), 2):
        out[tuple(k for k in range(5) if k not in (i, j))] = np.arccos(np.clip(-nrm[i] @ nrm[j]/np.linalg.norm(nrm[i])/np.linalg.norm(nrm[j]), -1, 1))
    return out
def simplex_hess(Xv):
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
def tri_hess(l):
    A = 0.25*np.sqrt(2*l[0]**2*l[1]**2 + 2*l[1]**2*l[2]**2 + 2*l[2]**2*l[0]**2 - (l**4).sum())
    s2 = (l**2).sum(); g = l*(s2 - 2*l**2)/(8*A); H = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            H[i, j] = ((s2 - 4*l[i]**2) if i == j else 2*l[i]*l[j])/(8*A) - l[i]*(s2 - 2*l[i]**2)/(8*A*A)*g[j]
    return H

# ---------------- D4 cone complex ----------------
OFF = [np.zeros(4), np.array([1., 0, 0, 0]), np.full(4, .5), np.array([.5, .5, .5, -.5])]
def vert(p):   # point of D4* -> (translation in D4, type)
    for t, o in enumerate(OFF):
        a = p - o
        if np.allclose(a, np.round(a)) and int(round(a.sum())) % 2 == 0: return (tuple(int(round(x)) for x in a), t)
    raise ValueError(p)
pos = lambda v: np.array(v[0], float) + OFF[v[1]]
box = [np.array(q) for q in itertools.product(range(-2, 4), repeat=4) if sum(q) % 2 == 0]
SIMPS = []
for t in (1, 2, 3):
    h = OFF[t]; nb = [q for q in box if abs(np.linalg.norm(q - h) - 1) < 1e-9]
    for c4 in itertools.combinations(range(8), 4):
        if all(abs(np.linalg.norm(nb[i] - nb[j]) - np.sqrt(2)) < 1e-9 for i, j in itertools.combinations(c4, 2)):
            SIMPS.append([vert(h)] + [vert(nb[i].astype(float)) for i in c4])
ECLS, EVEC = {}, []
def edge(u, v):
    if (u[1], tuple(pos(u))) > (v[1], tuple(pos(v))): u, v = v, u
    d = pos(v) - pos(u)
    if u[1] == v[1] and tuple(d) < tuple(-d): u, v = v, u; d = -d
    key = (u[1], v[1], tuple(np.round(d, 6)))
    if key not in ECLS: ECLS[key] = len(EVEC); EVEC.append((d, u[1], v[1], np.array(v[0]) - np.array(u[0])))
    return (ECLS[key], np.array(u[0]))
SIMPDATA, TRIS = [], {}
for S in SIMPS:
    Xv = np.array([pos(v) for v in S]); SIMPDATA.append((simplex_hess(Xv), [edge(S[a], S[b]) for a, b in PAIRS]))
    for tri in itertools.combinations(range(5), 3):
        W = [S[i] for i in tri]; base = min(W, key=lambda v: (v[1], tuple(pos(v))))[0]
        key = tuple(sorted((v[1], tuple(np.array(v[0]) - base)) for v in W))
        if key not in TRIS:
            prs = ((0, 1), (1, 2), (0, 2)); l = np.array([np.linalg.norm(pos(W[b]) - pos(W[a])) for a, b in prs])
            TRIS[key] = (tri_hess(l), [edge(W[a], W[b]) for a, b in prs])
NE = len(EVEC)
def Jm(eds, K):
    r = np.zeros((len(eds), NE), complex)
    for i, (c, a) in enumerate(eds): r[i, c] = np.exp(1j*(K @ a))
    return r
def Q(K):
    K = np.asarray(K, complex); M = np.zeros((NE, NE), complex)
    for H, eds in TRIS.values(): M += 2*np.pi*Jm(eds, -K).T @ H @ Jm(eds, K)
    for H, eds in SIMPDATA: M -= Jm(eds, -K).T @ H @ Jm(eds, K)
    return M   # Q(K)^T = Q(-K); Hermitian at real K
def Gauge(K):
    K = np.asarray(K, complex); G = np.zeros((NE, 16), complex)
    for c, (d, ta, tb, da) in enumerate(EVEC):
        u = d/np.linalg.norm(d); G[c, 4*tb:4*tb+4] += u*np.exp(1j*(K @ da)); G[c, 4*ta:4*ta+4] -= u
    return G
SYM = [(i, j) for i in range(4) for j in range(i, 4)]
def Mread(K):   # smooth metric h_ab e^{iK.x} -> line-integrated edge-length change
    K = np.asarray(K, complex); out = np.zeros((NE, 10), complex)
    for c, (d, ta, tb, da) in enumerate(EVEC):
        l = np.linalg.norm(d); pd = K @ d; f = 1.0 if abs(pd) < 1e-12 else (np.exp(1j*pd) - 1)/(1j*pd)
        for s, (i, j) in enumerate(SYM): out[c, s] = (1 if i == j else 2)*d[i]*d[j]/(2*l)*f*np.exp(1j*(K @ OFF[ta]))
    return out
print(f"  complex: {len(SIMPS)} simplices, {len(TRIS)} triangles, {NE} edge classes per D4 cell ({time.time()-T0:.1f}s)")

# ================= G. geometry and root slicing =================
ROOTS = np.array([s for s in itertools.product((-1, 0, 1), repeat=4) if np.sum(np.abs(s)) == 2], float)
tt = np.array([1., 1, 0, 0])/np.sqrt(2)
u1, u2, u3 = np.array([1., -1, 0, 0])/np.sqrt(2), np.array([0., 0, 1, 1])/np.sqrt(2), np.array([0., 0, 1, -1])/np.sqrt(2)
proj = np.round(ROOTS @ tt*np.sqrt(2), 9); cnt = {v: int(np.sum(np.abs(proj) == v)) for v in (2, 1, 0)}
Sp = lambda p: np.array([p @ u1, p @ u2, p @ u3])*np.sqrt(2)   # slice coordinates in units of the cube edge a = 1/sqrt2
sl = {m: np.array([Sp(np.array(q, float)) for q in box if q[0] + q[1] == m]) for m in (0, 1)}
cub0 = np.all(np.abs(sl[0] - 2*np.round(sl[0]/2)) < 1e-9); cub1 = np.all(np.abs(sl[1] - 1 - 2*np.round((sl[1] - 1)/2)) < 1e-9)
check("G1 24 roots split 2/16/6 along the root time (tick edge / pair-offset edges / slice edges); slices are the two cube-centre tilings, alternating",
      len(ROOTS) == 24 and cnt == {2: 2, 1: 16, 0: 6} and cub0 and cub1,
      f"|r.t|*sqrt2 = 2,1,0: {cnt}; slice m even on 2Z^3, odd on 2Z^3+(1,1,1) (a units); one tick root spans 2 half-ticks")
dsum = {}
for S in SIMPS:
    Xv = np.array([pos(v) for v in S]); dh = dihedrals(np.linalg.norm(Xv[:, None] - Xv[None], axis=2))
    for tri, th in dh.items():
        W = [S[i] for i in tri]; base = min(W, key=lambda v: (v[1], tuple(pos(v))))[0]
        key = tuple(sorted((v[1], tuple(np.array(v[0]) - base)) for v in W)); dsum[key] = dsum.get(key, 0) + th
check("G2 flat D4 cone: per D4 cell 48 4-simplices (3 hole types x 16 facets), 104 hinges, 36 edges (12 roots + 24 spokes); every deficit 0",
      len(SIMPS) == 48 and len(dsum) == len(TRIS) == 104 and NE == 36 and max(abs(2*np.pi - v) for v in dsum.values()) < 1e-12,
      f"max |deficit| {max(abs(2*np.pi - v) for v in dsum.values()):.0e}")
srel = lambda Mm: int(np.sum(np.abs(np.linalg.eigvalsh(Mm)) < 1e-8*np.abs(np.linalg.eigvalsh(Mm)).max()))
kr = [rng.uniform(-np.pi, np.pi, 4) for _ in range(2)]
nul = [srel(Q(k)) for k in kr]; gres = max(np.linalg.norm(Q(k) @ Gauge(k))/np.linalg.norm(Q(k)) for k in kr)
check("G3 every edge responding: null space at generic k = vertex displacements only (4 vertex classes x 4); no zero-action branch",
      nul == [16, 16] and gres < 1e-9, f"nullity {nul}; |Q G|/|Q| {gres:.0e}")
w0 = np.linalg.eigvalsh(Q(np.zeros(4))); N0 = np.linalg.eigh(Q(np.zeros(4)))[1][:, np.abs(w0) < 1e-8]
Cc = np.linalg.eigh(Q(np.zeros(4)))[1][:, np.abs(w0) > 1e-8]
PAIRINGS = (({0, 1}, {2, 3}), ({0, 2}, {1, 3}), ({0, 3}, {1, 2}))   # the three orthogonal root 4-frames
FR = [[e for e, (d, ta, tb, da) in enumerate(EVEC) if ta == tb == 0 and set(np.nonzero(d)[0].tolist()) in pr] for pr in PAIRINGS]
Y = np.zeros((NE, 2))
for g, c in enumerate(FR):
    for e in c: Y[e, 0] += [1, -1, 0][g]; Y[e, 1] += [1, 1, -2][g]
B0 = np.c_[Gauge(np.zeros(4)), Mread(np.zeros(4)), Y]; extra = np.linalg.matrix_rank(N0, 1e-8) - np.linalg.matrix_rank(np.c_[Gauge(np.zeros(4)), Mread(np.zeros(4))], 1e-8)
inN0 = np.linalg.norm(Y - N0 @ (N0.T @ Y))
n_g = np.array([.3, .5, .7, .4]); n_g /= np.linalg.norm(n_g)
ev = [np.sort(np.abs(np.linalg.eigvalsh(Q(s*n_g)))) for s in (.05, .025)]
soft = ev[0][16:24]/ev[1][16:24]
check("G4 small-k spectrum: 16 exact zeros, 8 soft (x4 on halving k) = 6 metric + 2 frame-scale strains, 12 cell-gapped (|eig| >= 16)",
      len(FR) == 3 and all(len(c) == 4 for c in FR) and extra == 2 and inN0 < 1e-8 and np.all(np.abs(soft - 4) < .02) and ev[1][24] > 15.9,
      f"k=0 flat non-metric deformations {extra} = the frame doublet: rescale the three orthogonal root 4-frames by (a,b,c), a+b+c=0, spokes fixed; soft ratios {soft.min():.3f}..{soft.max():.3f}; gap {ev[1][24]:.2f}; pre-registered 'only metric soft' MISSED")
print(f"  (G done {time.time()-T0:.1f}s)")

# ================= R. linearised response =================
def Emat(s):
    i, j = SYM[s]; E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1; return E
def FEH(K):   # quadratic part of int sqrt(g) R (Euclidean), analytic pairing h(-K) . F(K) . h(K)
    K = np.asarray(K, complex); K2 = K @ K; Fm = np.zeros((10, 10), complex)
    for s in range(10):
        for t in range(10):
            a, b = Emat(s), Emat(t)
            Fm[s, t] = -.25*K2*np.sum(a*b) + .5*(K @ a) @ (K @ b) - .25*((K @ a @ K)*np.trace(b) + (K @ b @ K)*np.trace(a)) + .25*K2*np.trace(a)*np.trace(b)
    return Fm
def Qeff(K):   # metric (10) + frame doublet (2); the 12 cell-gapped modes integrated out
    K = np.asarray(K, complex); A = np.c_[Mread(K), Y]; Am = np.c_[Mread(-K), Y]; q = Q(K)
    return Am.T @ q @ A - (Am.T @ q @ Cc) @ np.linalg.solve(Cc.T @ q @ Cc, Cc.T @ q @ A)
DIRS = [np.array(v, float)/np.linalg.norm(v) for v in ([1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [.3, .5, .7, .4], [1, -.2, .4, .9], [0, 0, 1, .3])]
cs, rr, hy, yy = [], [], [], []
for n in DIRS:
    r2 = []
    for s in (.05, .025):
        Qe = Qeff(s*n); Fm = FEH(s*n); hh = Qe[:10, :10]
        c = np.real(np.vdot(Fm.ravel(), hh.ravel())/np.vdot(Fm.ravel(), Fm.ravel())); cs.append(c)
        r2.append(np.linalg.norm(hh - c*Fm)/np.linalg.norm(c*Fm)); hy.append(np.abs(Qe[:10, 10:]).max()/s**2)
        yy += list(np.linalg.eigvals(np.linalg.solve(np.diag([8., 24.]), Qe[10:, 10:]))/s**2)
    rr.append(r2)
rr = np.array(rr)
check("R1 metric block = c x linearised sqrt(g) R with ONE c in every direction (root, axis, generic): c = 2 = the D4 cell 4-volume",
      np.ptp(cs) < 1e-3 and abs(np.mean(cs) - 2) < 1e-3 and rr.max() < 2e-2 and np.all(rr[:, 0]/rr[:, 1] > 3),
      f"c = {min(cs):.5f}..{max(cs):.5f}; rel resid {rr[:, 0].max():.1e} -> {rr[:, 1].max():.1e} (ratio {np.min(rr[:, 0]/rr[:, 1]):.2f})")
yy = np.real(yy)
check("R2 frame doublet: own kinetic term -k^2 per unit (sign of the tensor block); metric mixing O(k^3) (|Q_hy|/k^2 halves with k)",
      np.all(np.abs(yy + 1) < 2e-3) and max(hy[0::2])/max(hy[1::2]) > 1.9,
      f"yy/k^2 = {yy.min():.4f}..{yy.max():.4f}; |Q_hy|/k^2 {max(hy[0::2]):.1e} -> {max(hy[1::2]):.1e}")
def Qcoef(ks):   # Laurent coefficients in z = exp(-E/sqrt2) (one half-tick per power) at spatial momentum ks
    C = {}
    def add(H, eds, w):
        for i, (ci, ai) in enumerate(eds):
            for j, (cj, aj) in enumerate(eds):
                p = int(round(aj[0] + aj[1] - ai[0] - ai[1])); C.setdefault(p, np.zeros((NE, NE), complex))
                C[p][ci, cj] += w*H[i, j]*np.exp(1j*ks @ (aj - ai))
    for H, eds in TRIS.values(): add(H, eds, 2*np.pi)
    for H, eds in SIMPDATA: add(H, eds, -1.0)
    return C
def roots(C, nul=16, tol=1e-6):   # finite roots of the singular matrix polynomial (random rank completion, twice)
    d = max(abs(p) for p in C); n = NE; deg = 2*d; A = [C.get(q - d, np.zeros((n, n))) for q in range(deg + 1)]
    N = n*deg; Aa = np.zeros((N, N), complex); Bb = np.eye(N, dtype=complex); Aa[:-n, n:] = np.eye(N - n)
    for q in range(deg): Aa[-n:, q*n:(q + 1)*n] = -A[q]
    Bb[-n:, -n:] = A[deg]; zs = []
    for sd in (1, 2):
        r = np.random.default_rng(sd); U = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul)); V = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul))
        zs.append(eig(Aa + U @ np.diag(r.normal(size=nul)) @ V.conj().T, Bb + U @ np.diag(r.normal(size=nul)) @ V.conj().T, right=False))
    zz = np.array([q for q in zs[0] if np.isfinite(q) and abs(q) > 1e-30 and np.min(np.abs(zs[1] - q)) < tol*max(1, abs(q))])
    return -np.sqrt(2)*np.log(zz.astype(complex)), d
def light(nv, k):
    nv = np.array(nv, float)/np.linalg.norm(nv); ns = nv[0]*u1 + nv[1]*u2 + nv[2]*u3
    E, d = roots(Qcoef(k*ns)); return E, ns
def yfrac(ns, k, e):   # frame-doublet share of each null vector at a light root
    K = k*ns + 1j*e*tt; vh = np.linalg.svd(Q(K))[2]; Nn = vh[-18:].conj().T; Gk = Gauge(K)
    phys = np.linalg.svd((np.eye(NE) - Gk @ np.linalg.pinv(Gk, rcond=1e-9)) @ Nn)[0][:, :2]
    X = np.c_[Mread(K), Y, Gk]; cf = np.linalg.lstsq(X, phys, rcond=None)[0]; Hy = Y @ cf[10:12]; Hh = Mread(K) @ cf[:10]
    from scipy.linalg import eigh as geigh
    return geigh(Hy.conj().T @ Hy, Hy.conj().T @ Hy + Hh.conj().T @ Hh, eigvals_only=True)
SDIRS = [[1, 0, 0], [1, 1, 0], [1, 1, 1], [.3, .5, .8], [.2, .9, .4]]
tab, cnts, heavy, yf, cdev = [], [], [], [], []
for nv in SDIRS:
    Ak = []
    for k in (.1, .05):
        E, ns = light(nv, k); L = E[np.abs(E) < 3*k]; cnts.append(len(L)); heavy.append(np.min(np.abs(E[np.abs(E) >= 3*k])))
        Lp = np.sort(L[L.real > 0].real)/k; cdev.append(np.abs(Lp - 1).max() if k == .05 else 0)
        Ak.append((Lp - 1)/(k/np.sqrt(2))**2)
        if k == .1 and nv in ([1, 0, 0], [.3, .5, .8]):
            for e in np.unique(np.round(Lp, 7)): yf.append(yfrac(ns, k, e*k))
    tab.append((nv, Ak))
check("R3 real-time census along the root: 8 light roots = 4 branches x (+-E) on the edge cone (2 tensor + 2 frame), all else cell-gapped",
      all(c == 8 for c in cnts) and min(heavy) > 4 and max(cdev) < 1e-3,
      f"light per k {sorted(set(cnts))}; |c - 1| <= {max(cdev):.1e} at ka = .035; heavy |E| >= {min(heavy):.2f} (lattice units; ka = 2.4)")
yf = np.array(yf)
check("R4 every light pair = one metric (tensor) mode + one frame mode, degenerate in speed",
      np.all(np.abs(np.sort(yf, axis=1) - [0, 1]) < 1e-2), f"frame shares per pair {np.round(yf, 3).tolist()}")
Aall = np.array([a for _, Ak in tab for a in Ak]); stab = max(np.abs(Ak[0] - Ak[1]).max() for _, Ak in tab)
print("  birefringence c = 1 + A (ka)^2 per slice direction (a = cube edge), k=.1 / k=.05:")
for nv, Ak in tab: print(f"   n={nv}: A = {np.round(np.unique(np.round(Ak[0], 4)), 4).tolist()} / {np.round(np.unique(np.round(Ak[1], 4)), 4).tolist()}")
amax = np.abs(Aall).max(); L_rung = 8.1e-35; k100 = 2*np.pi*100/2.998e8; dc = 2*amax*(k100*L_rung)**2
check("R5 graviton birefringence (W(F4)-only quartic term): +-A, zero polarisation-averaged shift, A = 1/6 on the cube axis, 0 on the body diagonal",
      stab < 2e-2*amax and abs(np.mean(Aall)) < 1e-3 and abs(np.abs(tab[0][1][1]).max() - 1/6) < 2e-3 and np.abs(tab[2][1][1]).max() < 2e-3,
      f"|A| <= {amax:.4f}; mean {np.mean(Aall):.1e}; two-scale drift {stab:.1e}")
check("R6 GW170817 (|dc| < 1e-15) and dispersion bounds: splitting 2A(kL)^2 at 100 Hz with the cell rung L = 8.1e-35 m",
      dc < 1e-15, f"|dc| = {dc:.0e}; bound needs L < {np.sqrt(1e-15/(2*amax))/k100:.0e} m")
print(f"  (R done {time.time()-T0:.1f}s)")
def Aform(nv):
    n2 = (np.array(nv, float)/np.linalg.norm(nv))**2; S = n2[0]*n2[1] + n2[0]*n2[2] + n2[1]*n2[2]; Pp = np.prod(n2)
    return np.sqrt(max((1 - S)**2 - 12*Pp, 0))/6
rd = [rng.normal(size=3) for _ in range(3)]
fit = [(lambda E: abs(np.sort(E[(np.abs(E) < .3) & (E.real > 0)].real/.1)[-1] - 1)/(.1/np.sqrt(2))**2)(light(v, .1)[0]) for v in rd]
fe = max(abs(f - Aform(v)) for f, v in zip(fit, rd)) ; fe0 = max(abs(np.abs(Ak[1]).max() - Aform(nv)) for nv, Ak in tab)
check("R7 angular law of the splitting (fitted on 5 directions, tested on 3 seeded random ones): A = (1/6) sqrt((1 - S)^2 - 12 P)",
      fe < 3e-3 and fe0 < 3e-3, f"S = sum_{{i<j}} n_i^2 n_j^2, P = n_1^2 n_2^2 n_3^2 (slice cube axes); max misfit {max(fe, fe0):.1e}")

# ================= N. static weak field, one G, frame dragging =================
def solve(Qm, src, ng):   # least-norm solve off the ng exact gauge zeros
    w, U = np.linalg.eig(Qm); i = np.argsort(np.abs(w))[ng:]; Ui = np.linalg.pinv(U)
    return U[:, i] @ ((Ui[i] @ src)/w[i])
def tvec(T): return np.array([(1 if i == j else 2)*T[i, j] for i, j in SYM])
def hmat(hv):
    H = np.zeros((4, 4), complex)
    for s, (i, j) in enumerate(SYM): H[i, j] = H[j, i] = hv[s]
    return H
gam, gn, lt = [], [], []
for nv in ([1, 0, 0], [.3, .5, .8], [1, 1, 1]):
    for k in (.05, .025):
        nv_ = np.array(nv, float)/np.linalg.norm(nv); ns = nv_[0]*u1 + nv_[1]*u2 + nv_[2]*u3; K = k*ns
        Pt = np.eye(4) - np.outer(tt, tt) - np.outer(ns, ns); jv = np.linalg.svd(Pt)[0][:, 0]
        Ql = Qeff(K); Fc = 2*FEH(K)
        out = []
        for Qm, ng, pad in ((Ql, 4, 2), (Fc, 4, 0)):
            hs = hmat(solve(Qm, np.r_[tvec(np.outer(tt, tt)), np.zeros(pad)], ng)[:10])
            hv = hmat(solve(Qm, np.r_[tvec(np.outer(tt, jv) + np.outer(jv, tt)), np.zeros(pad)], ng)[:10])
            out.append((tt @ hs @ tt, np.sum(Pt*hs), jv @ hv @ tt))
        (htl, ptl, vl), (htc, ptc, vc) = out
        gam.append(np.real(-ptl/(2*htl))); gn.append(np.real(htl/htc)); lt.append(np.real(vl/vc))
        if k == .05 and nv == [1, 0, 0]: g_c = np.real(-ptc/(2*htc)); kphi = np.real(htl*k**2)
check("N1 static point source (T = rho t t, k_t = 0): Newtonian 1/k^2 potential and PPN gamma = 1 (gauge-invariant transverse spatial trace / h_tt)",
      max(abs(np.array(gam) - 1)) < 2e-2 and abs(g_c - 1) < 1e-9, f"gamma = {min(gam):.5f}..{max(gam):.5f} (continuum {g_c:.3f}); k^2 h_tt = {kphi:.4f}")
GT = np.mean(cs)/2
check("N2 one G: static (Newtonian) coupling / tensor-block coupling = 1 (both read from the one hinge-sum c)",
      max(abs(np.array(gn)/GT - 1)) < 2e-2, f"G_N/G_T = {min(gn)/GT:.5f}..{max(gn)/GT:.5f}")
check("N3 frame dragging: transverse current -> gravitomagnetic h_ti equals the continuum (Lense-Thirring) value",
      max(abs(np.array(lt) - 1)) < 2e-2, f"ratio {min(lt):.5f}..{max(lt):.5f}")
print(f"  (N done {time.time()-T0:.1f}s)")

# ================= M. matter reading, the tie, clause bookkeeping =================
pp = rng.normal(size=(5, 4)); fr_roots = [ROOTS[[set(np.nonzero(r)[0].tolist()) in pr for r in ROOTS]] for pr in PAIRINGS]
q2 = max(abs(np.sum((R_ @ p)**2) - 4*(p @ p)) for R_ in fr_roots for p in pp)
q4 = min(np.ptp([np.sum((R_ @ p)**4) for R_ in fr_roots]) for p in pp)
check("M1 frame doublet is invisible to every W(F4) two-derivative matter term: each root frame gives sum (r.p)^2 = 4 p^2 (8 signed roots); first reading at (r.p)^4",
      len(fr_roots) == 3 and all(len(R_) == 8 for R_ in fr_roots) and q2 < 1e-12 and q4 > 1e-3, f"dim-4 residual {q2:.0e}; quartic frame spread >= {q4:.2f} (seeded p)")
Mz = Mread(np.zeros(4)); e_tt = tvec(np.outer(tt, tt))/np.array([1 if i == j else 2 for i, j in SYM])
stretch = np.linalg.norm(Q(np.zeros(4)) @ (Mz @ e_tt))
rl = np.linalg.norm(ROOTS, axis=1)
check("M2 the hinge sum does not fix the tick/edge ratio (a uniform time stretch is a zero); 'all 24 roots alike' does: tick root = slice root, so graviton cone = event cone",
      stretch < 1e-10 and np.ptp(rl) < 1e-12, f"|Q(0) M h_tt| = {stretch:.0e}; root lengths {rl.min():.4f}..{rl.max():.4f}; no free tau")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")

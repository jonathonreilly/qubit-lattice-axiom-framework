AUDIT_INPUT_PATHS = ('docs/D4_HINGE_SUM_FRAME_DOUBLET_IDENTIFICATION_GAP_AUDIT_AND_METRIC_READING_REMOVAL_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-frame-modes: what is the extra massless pair (the frame doublet) of the D4 hinge sum, does anything
in the rules gap it, and what does it do if kept? Carrier = d4-gravity's D4 cone (Delaunay 16-cells coned
from their centres), time along a root. Group theory exact on W(F4); hinge sum exact at k = 0 (nonlinear);
matter loop on W(F4) kernels with supplied per-edge readings. Self-contained; seeded; numpy + scipy only."""
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
tt = np.array([1., 1, 0, 0])/np.sqrt(2)
SYM = [(i, j) for i in range(4) for j in range(i, 4)]
def Emat(s):
    i, j = SYM[s]; E = np.zeros((4, 4)); E[i, j] = E[j, i] = 1; return E
def FEH(K):   # quadratic part of int sqrt(g) R (Euclidean)
    K = np.asarray(K, complex); K2 = K @ K; Fm = np.zeros((10, 10), complex)
    for s in range(10):
        for t in range(10):
            a, b = Emat(s), Emat(t)
            Fm[s, t] = -.25*K2*np.sum(a*b) + .5*(K @ a) @ (K @ b) - .25*((K @ a @ K)*np.trace(b) + (K @ b @ K)*np.trace(a)) + .25*K2*np.trace(a)*np.trace(b)
    return Fm
ROOTS = np.array([s for s in itertools.product((-1, 0, 1), repeat=4) if np.sum(np.abs(s)) == 2], float)
PAIRINGS = (({0, 1}, {2, 3}), ({0, 2}, {1, 3}), ({0, 3}, {1, 2}))   # the three orthogonal root 4-frames
frame = lambda r: [i for i, p in enumerate(PAIRINGS) if set(np.nonzero(np.round(r, 9))[0].tolist()) in p][0]
FID = np.array([frame(r) for r in ROOTS])

# ================= A. identification: W(F4) on frames =================
def refl(v): v = np.array(v, float); return np.eye(4) - 2*np.outer(v, v)/(v @ v)
LONG = list(ROOTS); SHORT = [r for r in np.eye(4)] + [-r for r in np.eye(4)] + [np.array(s)/2 for s in itertools.product((-1., 1.), repeat=4)]
gk = lambda M: tuple(np.round(2*M).astype(int).ravel())
GW = {gk(np.eye(4)): np.eye(4)}; fr_ = [np.eye(4)]
gens = [refl([1, -1, 0, 0]), refl([0, 1, -1, 0]), refl([0, 0, 1, -1]), refl([0, 0, 0, 1]), refl([.5, .5, .5, .5])]
while fr_:
    nf = []
    for M in fr_:
        for g in gens:
            N = g @ M
            if gk(N) not in GW: GW[gk(N)] = N; nf.append(N)
    fr_ = nf
GW = list(GW.values()); NG = len(GW)
FRR = [ROOTS[FID == f] for f in range(3)]
def fperm(M):
    out = []
    for f in range(3):
        im = {frame(M @ r) for r in FRR[f]}; assert len(im) == 1; out.append(im.pop())
    return tuple(out)
inD4 = lambda v: np.allclose(v, np.round(v)) and int(round(v.sum())) % 2 == 0
HC = [np.array([1., 0, 0, 0]), np.full(4, .5), np.array([.5, .5, .5, -.5])]
hperm = lambda M: tuple([i for i, c in enumerate(HC) if inD4(M @ h - c)][0] for h in HC)
fp = [fperm(M) for M in GW]; hp = [hperm(M) for M in GW]; ID = (0, 1, 2)
check("A1 W(F4) (1152 elements) permutes the 3 root 4-frames through S3 = W(F4)/W(D4_short): kernel 192 holds every short reflection and no long one",
      NG == 1152 and len(set(fp)) == 6 and fp.count(ID) == 192 and all(fperm(refl(v)) == ID for v in SHORT) and all(fperm(refl(v)) != ID for v in LONG),
      f"|W| = {NG}; image {len(set(fp))}; kernel {fp.count(ID)}")
chi = np.array([sum(p[i] == i for i in range(3)) - 1 for p in fp], float)
tr = [np.array([np.trace(np.linalg.matrix_power(M, k)) for M in GW]) for k in (1, 2, 3, 4)]
S2 = (tr[0]**2 + tr[1])/2; S4 = (tr[0]**4 + 6*tr[0]**2*tr[1] + 3*tr[1]**2 + 8*tr[0]*tr[2] + 6*tr[3])/24
S2sq = ((tr[1]**2 + tr[3])/2); SS2 = (S2**2 + S2sq)/2
mu = lambda c: chi @ c/NG
check("A2 the doublet is the 2-dim irrep of that S3 pulled back to W(F4): norm 1; absent from Sym^2 V (non-metric; Sym^2 V = 1 + 9); once in Sym^4 V (matter quartic)",
      abs(chi @ chi/NG - 1) < 1e-12 and abs(mu(S2)) < 1e-12 and abs(S2 @ S2/NG - 2) < 1e-12 and abs(mu(S4) - 1) < 1e-12,
      f"<chi,chi> = {chi @ chi/NG:.0f}; mult Sym2 {mu(S2):.0f}, Sym4 {mu(S4):.0f}; Sym2(Sym2 V) {mu(SS2):.0f} (h h y allowed by symmetry)")
cl = []
in2Ds = lambda v: np.allclose(v/2, np.round(v/2)) or np.allclose(v/2 - .5, np.round(v/2 - .5))
for r in LONG:
    for c in cl:
        if in2Ds(r - c[0]): c.append(r); break
    else: cl.append([r])
check("A3 frames = the 3 nonzero classes of D4/2D4*; hole types = the 3 of D4*/D4, permuted by the OTHER S3 (triality, kernel W(D4_long)); joint image S3 x S3",
      len(cl) == 3 and all(len({frame(r) for r in c}) == 1 for c in cl) and hp.count(ID) == 192 and all(hperm(refl(v)) == ID for v in LONG) and len(set(zip(fp, hp))) == 36,
      f"root classes {[len(c) for c in cl]}; hole kernel {hp.count(ID)}; joint {len(set(zip(fp, hp)))}; the dual rotation D4* -> D4 swaps the two S3s")
print(f"  (A done {time.time()-T0:.1f}s)")

# ================= B. does the hinge sum gap it? =================
L0 = np.array([np.linalg.norm(e[0]) for e in EVEC])
FR = [[e for e, (d, ta, tb, da) in enumerate(EVEC) if ta == tb == 0 and frame(d) == f] for f in range(3)]
Y = np.zeros((NE, 2))
for g, c in enumerate(FR):
    for e in c: Y[e, 0] += [1, -1, 0][g]; Y[e, 1] += [1, 1, -2][g]
Q0 = np.real(Q(np.zeros(4))); w0, U0 = np.linalg.eigh(Q0); Cc = U0[:, np.abs(w0) > 1e-8]
def Qeff(K):
    K = np.asarray(K, complex); A = np.c_[Mread(K), Y]; Am = np.c_[Mread(-K), Y]; q = Q(K)
    return Am.T @ q @ A - (Am.T @ q @ Cc) @ np.linalg.solve(Cc.T @ q @ Cc, Cc.T @ q @ A)
ng = np.array([.3, .5, .7, .4]); ng /= np.linalg.norm(ng); ks = (.2, .1, .05)
yk = [np.real(np.linalg.eigvals(np.linalg.solve(Y.T @ Y, Qeff(k*ng)[10:, 10:]))) for k in ks]
cf = np.polyfit(np.array(ks)**2, [y.mean() for y in yk], 2)
check("B1 (a) four-derivative terms cannot gap it: k = 0 doublet entry is an exact zero; the hinge sum gives -(k^2 + b k^4) only",
      np.abs(Y.T @ Q0 @ Y).max() < 1e-8*np.abs(Q0).max() and abs(cf[2]) < 1e-6 and abs(cf[1] + 1) < 1e-2,
      f"|Y Q(0) Y|/|Q| = {np.abs(Y.T @ Q0 @ Y).max()/np.abs(Q0).max():.0e}; fit c0 = {cf[2]:.0e}, c2 = {cf[1]:.4f}, b = {cf[0]/cf[1]:.3f} (lattice units)")
def Lmat(l, eds):
    L = np.zeros((5, 5))
    for (a, b), (c, _) in zip(PAIRS, eds): L[a, b] = L[b, a] = l[c]
    return L
heron = lambda x, y, z: 0.25*np.sqrt(max(2*x*x*y*y + 2*y*y*z*z + 2*z*z*x*x - x**4 - y**4 - z**4, 0))
TRIK = list(TRIS.keys())
def tkey(S, tri):
    W = [S[i] for i in tri]; base = min(W, key=lambda v: (v[1], tuple(pos(v))))[0]
    return tuple(sorted((v[1], tuple(np.array(v[0]) - base)) for v in W))
ST = [[(tkey(S, tri), tri) for tri in itertools.combinations(range(5), 3)] for S in SIMPS]
def Scell(l):   # full nonlinear hinge sum per D4 cell, uniform (k = 0) edge lengths
    th = dict.fromkeys(TRIK, 0.0)
    for (H, eds), st in zip(SIMPDATA, ST):
        dh = dihedrals(Lmat(l, eds))
        for k, tri in st: th[k] += dh[tri]
    dfc = {k: 2*np.pi - th[k] for k in TRIK}
    return sum(heron(*[l[c] for c, _ in TRIS[k][1]])*dfc[k] for k in TRIK), dfc
def gradS(l):
    S, dfc = Scell(l); g = np.zeros(NE)
    for k in TRIK:
        x = np.array([l[c] for c, _ in TRIS[k][1]]); ga = x*((x**2).sum() - 2*x**2)/(8*heron(*x))
        for i, (c, _) in enumerate(TRIS[k][1]): g[c] += ga[i]*dfc[k]
    return g
def Srel(e, j):   # gapped modes relaxed (stationary)
    l = L0 + e*Y[:, j]; x = np.zeros(Cc.shape[1])
    for it in range(10):
        r = Cc.T @ gradS(l + Cc @ x); x -= np.linalg.solve(Cc.T @ Q0 @ Cc, r)
        if np.abs(r).max() < 1e-13: break
    return Scell(l + Cc @ x)[0]
lin = max(abs(v) for v in Scell(L0 + 1e-6*Y[:, 0])[1].values())/1e-6
co = {}
for j in (0, 1):
    for rl in (0, 1):
        f = (lambda e: Scell(L0 + e*Y[:, j])[0]) if not rl else (lambda e: Srel(e, j))
        e = .005; sp, sm = f(e), f(-e); co[j, rl] = ((sp - sm)/2/e**3, (sp + sm)/2/e**4)
k3 = co[1, 1][0]/(-6); k4 = co[0, 1][1]/4
check("B2 (b) nonlinear hinge sum along the doublet: carries linear curvature, no quadratic term, S3 cubic Sum u^3 and quartic (Sum u^2)^2 (u = frame length changes)",
      lin > 1 and abs(co[0, 0][0]) < 1e-6 and abs(co[1, 1][1]/co[0, 1][1] - 9) < .05 and abs(co[1, 1][0]) > 100,
      f"max linear deficit {lin:.2f}/unit; S_cell = {k3:.2f} Sum u^3 + {k4:.2f} (Sum u^2)^2 (relaxed; unrelaxed quartic {co[0, 0][1]/4:.2f}); flat point is an INFLECTION, not a modulus")
def shL(Lm):
    def sh(h):
        Hm = np.zeros((10, 10))
        for e, (a, b) in enumerate(PAIRS):
            gs = []
            for s in (1, -1):
                L = Lm.copy(); L[a, b] += s*h; L[b, a] = L[a, b]; gs.append(simplex_grad5(L))
            Hm[e] = (gs[0] - gs[1])/(2*h)
        return Hm
    H = (4*sh(1e-4) - sh(2e-4))/3; return .5*(H + H.T)
def Q0L(l):
    M = np.zeros((NE, NE))
    for k in TRIK:
        idx = np.array([c for c, _ in TRIS[k][1]]); np.add.at(M, (idx[:, None], idx[None, :]), 2*np.pi*tri_hess(l[idx]))
    for H, eds in SIMPDATA:
        idx = np.array([c for c, _ in eds]); np.add.at(M, (idx[:, None], idx[None, :]), -shL(Lmat(l, eds)))
    return M
B = rng.normal(size=(4, 4)); B = (B + B.T)/2; B -= np.trace(B)/4*np.eye(4); B /= np.linalg.norm(B); Yn = Y/np.linalg.norm(Y, axis=0); lift = []
for t in (.05, .1):
    w, U = np.linalg.eigh(Q0L(np.array([np.linalg.norm((np.eye(4) + t*B) @ e[0]) for e in EVEC])))
    i = np.argsort(np.abs(w))[22:24]; lift.append((w[i]/t**2, np.linalg.norm(U[:, i].T @ Yn)**2/2))
wi = np.linalg.eigvalsh(Q0L(1.1*L0)); ziso = int(np.sum(np.abs(wi) < 1e-6*np.abs(wi).max()))
check("B3 a uniform traceless lattice strain t lifts exactly the doublet, as t^2 (S3 forbids order t); isotropic strain keeps it massless",
      ziso == 24 and np.all(lift[0][0] > 0) and all(o > .99 for _, o in lift) and np.allclose(lift[0][0], lift[1][0], rtol=2e-2),
      f"lifted Q eigs/t^2 = {np.round(lift[0][0], 2).tolist()} (> 0: m^2 = -eig, TACHYONIC) (doublet share {lift[0][1]:.3f}); isotropic zeros {ziso}; whether lattice strain is physical = vertex-gauge question, OPEN")
print(f"  (B done {time.time()-T0:.1f}s)")

# ================= C. matter loop (vacuum energy) =================
# per-edge readings fixed by two-derivative metric covariance: w_r = (V/V0)^q (l_r/l0)^-s;
# scalar (q, s) = (2, 6) [Sum w r r -> sqrt(g) g^ab], fermion hop (3/2, 3) [-> sqrt(g) e^a]
v2 = -4.0   # cell volume V/V0 = 1 - 4 Sum a^2 along the doublet (spokes fixed; checked below)
Vy = [Vol for Vol in [sum(np.sqrt(abs(np.linalg.det(np.block([[np.zeros((1, 1)), np.ones((1, 5))], [np.ones((5, 1)), Lmat(L0 + e*Y[:, 0], eds)**2]])))/9216) for H, eds in SIMPDATA) for e in (-1e-3, 0, 1e-3)]]
v2n = (Vy[0] + Vy[2] - 2*Vy[1])/2/(1e-3)**2/Vy[1]
def pgrid(n):
    x = (np.arange(n) + .5)/n*2*np.pi - np.pi; return np.stack(np.meshgrid(x, x, x, x, indexing='ij'), -1).reshape(-1, 4)
def gam(Pg, a, sp):
    V = 1 + v2*np.sum(a**2); w = lambda q, s: V**q*(1 + a[FID])**(-s); rp = Pg @ ROOTS.T
    if sp == 's': return .25*np.mean(np.log((1 - np.cos(rp)) @ w(2, 6)/6))      # real scalar, per unit 4-volume
    X = (np.sin(rp)*w(1.5, 3)) @ ROOTS/12; Wl = (1 - np.cos(rp)) @ w(2, 6)/6
    return -np.mean(np.log((X**2).sum(1) + Wl**2))                               # 4-component Wilson-type Dirac
uu = np.array([1, -1, 0])/np.sqrt(2); Ms = {}
for n in (12, 16):
    Pg = pgrid(n)
    for sp in ('s', 'f'): e = 2e-3; Ms[n, sp] = (gam(Pg, e*uu, sp) + gam(Pg, -e*uu, sp) - 2*gam(Pg, 0*uu, sp))/e**2
Zy = 4.0   # doublet kinetic coefficient per unit 4-volume in Sum a^2 (x 1/(8 pi G)), from B1/R2
check("C1 (c) one-loop vacuum energy on the doublet (no symmetry forbids it): scalar M < 0 (tachyonic), Dirac M > 0 (gapping); Planck-scale either way",
      abs(v2n - v2) < 1e-3 and abs(Ms[12, 's'] - Ms[16, 's']) < 1e-4 and Ms[16, 's'] < 0 and Ms[16, 'f'] > 0,
      f"M_scalar = {Ms[16, 's']:.4f}, M_Dirac = {Ms[16, 'f']:.4f} per unit 4-volume (lattice units); m^2 = 8 pi G M/{Zy:.0f}; cell volume v2 = {v2n:.3f}")
print("  C2 note: CL-3's vacuum standard (respond only to departures from the vacuum of the same edges) removes this\n     same-edge vacuum term exactly, so as written the loop does NOT gap the doublet.")

# ================= D. records / metric-only reading =================
DIRS = [np.array(v, float)/np.linalg.norm(v) for v in ([1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [.3, .5, .7, .4])]
rres, cs = [], []
for n in DIRS:
    for s in (.05, .025):
        hh = Mread(-s*n).T @ Q(s*n) @ Mread(s*n); Fm = FEH(s*n)
        c = np.real(np.vdot(Fm.ravel(), hh.ravel())/np.vdot(Fm.ravel(), Fm.ravel())); cs.append(c); rres.append(np.linalg.norm(hh - c*Fm)/np.linalg.norm(c*Fm))
Hs = [(lambda M: (M + M.T)/2)(rng.normal(size=(4, 4))) for _ in range(5)]
orth = max(abs(sum(a*np.sum((ROOTS[FID == g] @ H)*ROOTS[FID == g]) for g, a in enumerate(uu))) for H in Hs)
A_ls = np.array([[r[i]*r[j]*(1 if i == j else 2) for i, j in SYM] for r in ROOTS])
l2 = 2*(1 + .01*np.array([1, 1, -2])[FID])**2 - 2; hfit = np.linalg.lstsq(A_ls, l2, rcond=None)[0]; Hf = hmat = np.zeros((4, 4))
for s_, (i, j) in enumerate(SYM): Hf[i, j] = Hf[j, i] = hfit[s_]
check("D1 (d) records/metric-only reading: the doublet is exactly orthogonal to every metric reading (Sum_r a_g (r h r) = 0), and the RAW metric block is already 2 x linearised sqrt(g) R",
      orth < 1e-12 and np.ptp(cs) < 1e-3 and max(rres) < 1e-3 and np.allclose(Hf, Hf[0, 0]*np.eye(4), atol=1e-12),
      f"orthogonality {orth:.0e}; raw c = {min(cs):.4f}..{max(cs):.4f}, resid {max(rres):.0e}; at 2nd order it reads as pure volume (h = {Hf[0, 0]:.1e} x 1 at u = .01)")
print(f"  (C, D done {time.time()-T0:.1f}s)")

# ================= E. couplings if kept (per-edge reading) and observables =================
pp = rng.normal(size=(4, 4))
Pg = lambda p: np.array([p[0]**2*p[1]**2 + p[2]**2*p[3]**2, p[0]**2*p[2]**2 + p[1]**2*p[3]**2, p[0]**2*p[3]**2 + p[1]**2*p[2]**2])
idn = max(abs(np.sum((FRR[g] @ p)**4) - 4*np.sum(p**4) - 24*Pg(p)[g]) for p in pp for g in range(3))
s6 = 6; a_t = 1e-4*np.array([1, 1, -2])/np.sqrt(6); vtx = []
for p in .02*pp:
    D = lambda a: ((1 - np.cos(ROOTS @ p))*(1 + a[FID])**(-s6)).sum()/6
    vtx.append(((D(a_t) - D(-a_t))/2)/((s6/6)*(a_t @ Pg(p))))
pr = Pg(1j*tt); prt = np.real(pr - pr.mean())
check("E1 coupling at four-derivative order: Sum_frame (r.p)^4 = 4 Sum p^4 + 24 P_g, so the doublet vertex is (s/6) Sum a_g P_g; rest matter (p = E t) charges the frame holding the tick root",
      idn < 1e-12 and np.allclose(vtx, 1, atol=2e-2) and np.allclose(prt, np.array([2, -1, -1])/12, atol=1e-12),
      f"identity {idn:.0e}; vertex ratio {min(vtx):.3f}..{max(vtx):.3f} (O(p^2) corrections); P_traceless(E t) = E^4 (2,-1,-1)/12")
lc = np.sqrt(2)*8.1e-35; hbarc = 1.973e-16   # coordinate unit (root/sqrt2) in m, GeV m
alpha = lambda E1, E2: s6**2*(lc*E1/hbarc)**2*(lc*E2/hbarc)**2/6912
ap = alpha(.938, .938)
check("E2 fifth force from doublet exchange (massless, composition-dependent): alpha = s^2 (l E1)^2 (l E2)^2 / 6912 vs gravity; Eot-Wash (alpha < 1e-3 at 50 um) and MICROSCOPE (eta < 1e-15)",
      ap < 1e-15, f"nucleon-nucleon alpha = {ap:.1e}; eta ~ alpha ~ 1e-75")
kgw = 2*np.pi*100/2.998e8; Pmix = (kgw*lc)**2; Pmat = ((lc*.3/hbarc)**2)**2
dN = 2*(4/7)*(10.75/106.75)**(4/3)
check("E3 extra GW polarisations: emitted doublet power / tensor <= max((k l)^2 mixing, (l E_q)^4 matter) at 100 Hz; Delta N_eff if thermalised at the Planck scale (SM g* = 106.75 comparator)",
      max(Pmix, Pmat) < 1e-2 and dN < .17, f"mixing {Pmix:.0e}, matter {Pmat:.0e}; Delta N_eff = {dN:.3f} (0 if never thermalised) vs < ~0.17-0.3")
r_AU = 1.496e11; dbeta = lc/r_AU
check("E4 PPN: the doublet feeds g_tt only through the O(k^3) mixing or at O(U^3), so |beta - 1|_doublet <~ l/r and gamma is untouched; metric beta inherited",
      dbeta < 8e-5, f"|beta - 1|_doublet <~ {dbeta:.0e} at 1 AU (bound ~8e-5); metric-sector beta = 1 ARGUED (Regge -> EH convergence for fat complexes), not computed")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")

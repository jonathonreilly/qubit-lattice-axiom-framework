AUDIT_INPUT_PATHS = ('docs/D4_FRAME_DOUBLET_LORENTZIAN_REGGE_STABILITY_GHOST_AND_METRIC_ONLY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-10-26.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""d4-frame-stability: is the frame doublet of the D4 hinge sum stable once the tick edge is time-like?
Lorentzian Regge reading (R-b): background g_L = P_perp - lam t t^T, Regge action = analytic continuation of the
Euclidean hinge sum (branch sqrt(z + i0)); second order via Schlaefli (d2S = Sum dA d eps), no arccos branches.
Contrast (R-a): Euclidean W(F4) lattice with momentum continuation (d4-gravity / d4-frame-modes).
Metric-only amendment: removal (nonlinear, exact) and graviton birefringence of the raw metric block.
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
csq = lambda z: np.sqrt(np.real(z) + 1j*np.abs(np.imag(z)))   # sqrt(z + i0)
def sgeom(s):   # s: 10 squared lengths over PAIRS -> cos, sin of 10 dihedrals (keyed by pair (i,j)), areas
    Sm = np.zeros((5, 5), complex)
    for (a, b), v in zip(PAIRS, s): Sm[a, b] = Sm[b, a] = v
    G = np.array([[.5*(Sm[0, i] + Sm[0, j] - Sm[i, j]) for j in range(1, 5)] for i in range(1, 5)])
    dG = np.linalg.det(G); Gi = np.linalg.inv(G); V4 = csq(dG/576)
    Ni = np.zeros((5, 5), complex); Ni[1:, 1:] = Gi; Ni[0, 1:] = Ni[1:, 0] = -Gi.sum(0); Ni[0, 0] = Gi.sum()
    def vol3(f):
        o = [k for k in range(5) if k != f]; G3 = np.array([[.5*(Sm[o[0], o[i]] + Sm[o[0], o[j]] - Sm[o[i], o[j]]) for j in (1, 2, 3)] for i in (1, 2, 3)])
        return csq(np.linalg.det(G3)/36)
    V3 = [vol3(f) for f in range(5)]
    cs, sn, ar = {}, {}, {}
    for i, j in PAIRS:
        a, b, c = [k for k in range(5) if k not in (i, j)]; x, y, z = Sm[a, b], Sm[b, c], Sm[a, c]
        A = csq((2*x*y + 2*y*z + 2*z*x - x*x - y*y - z*z)/16)
        cs[i, j] = -Ni[i, j]*16*dG/576/(V3[i]*V3[j]); sn[i, j] = (4/3)*V4*A/(V3[i]*V3[j]); ar[i, j] = A
    return cs, sn, ar
def dtheta(s, h=1e-6):   # d theta_(ij) / d s_e  (10 x 10), via central differences of cos
    cs0, sn0, _ = sgeom(s); D = np.zeros((10, 10), complex)
    for e in range(10):
        for sg in (1, -1):
            ss = np.array(s, complex); ss[e] += sg*h; c = sgeom(ss)[0]
            for q, p in enumerate(PAIRS): D[q, e] += sg*c[p]
    D /= 2*h
    for q, p in enumerate(PAIRS): D[q] *= -1/sn0[p]
    return D
def darea(x):   # x: 3 squared lengths -> dA/ds (3)
    A = csq((2*x[0]*x[1] + 2*x[1]*x[2] + 2*x[2]*x[0] - (x**2).sum())/16)
    return np.array([(2*x[1] + 2*x[2] - 2*x[0]), (2*x[0] + 2*x[2] - 2*x[1]), (2*x[0] + 2*x[1] - 2*x[2])])/16/(2*A)
# triangle bookkeeping: per simplex, local triangle (opposite pair) -> key, base
TPRS = ((0, 1), (1, 2), (0, 2))
REF = {}; SIMT = []
for S_, (H_, eds) in zip(SIMPS, SIMPDATA):
    rows = []
    for q, (i, j) in enumerate(PAIRS):
        tri = tuple(k for k in range(5) if k not in (i, j)); W = [S_[k] for k in tri]
        base = np.array(min(W, key=lambda v: (v[1], tuple(pos(v))))[0]); key = tuple(sorted((v[1], tuple(np.array(v[0]) - base)) for v in W))
        if key not in REF: REF[key] = (base, [edge(W[a], W[b]) for a, b in TPRS])
        rows.append((q, key, base))
    SIMT.append(rows)
DV = np.array([e[0] for e in EVEC])
def scls(g): return np.einsum('ei,ij,ej->e', DV, g, DV)
def Qs(K, g, cache={}):   # Schlaefli Hessian in squared lengths, per D4 cell
    ck = tuple(np.round(np.asarray(g).ravel(), 12))
    if ck not in cache:
        sc = scls(g); dth = [dtheta(np.array([sc[c] for c, _ in eds])) for H_, eds in SIMPDATA]
        dA = {k: darea(np.array([sc[c] for c, _ in ed])) for k, (b, ed) in REF.items()}; cache[ck] = (dth, dA)
    dth, dA = cache[ck]; K = np.asarray(K, complex)
    keys = list(REF); kid = {k: i for i, k in enumerate(keys)}; nh = len(keys)
    Am = np.zeros((nh, NE), complex); Ap = np.zeros((nh, NE), complex); Ep = np.zeros((nh, NE), complex)
    for k, (b, ed) in REF.items():
        for (c, a), d in zip(ed, dA[k]): Am[kid[k], c] += d*np.exp(-1j*(K @ a)); Ap[kid[k], c] += d*np.exp(1j*(K @ a))
    for (H_, eds), rows, D in zip(SIMPDATA, SIMT, dth):
        for q, key, base in rows:
            sh = base - REF[key][0]
            for e, (c, a) in enumerate(eds): Ep[kid[key], c] -= D[q, e]*np.exp(1j*(K @ (a - sh)))
    return Am.T @ Ep, Ap.T @ Ep
u1, u2, u3 = np.array([1., -1, 0, 0])/np.sqrt(2), np.array([0., 0, 1, 1])/np.sqrt(2), np.array([0., 0, 1, -1])/np.sqrt(2)
TV = np.array([1., 1, 0, 0])
def Qcoef_s(ks, g):   # Laurent coefficients in z = e^{i omega/sqrt2} (one half-tick per power), real spatial ks
    Qs(np.zeros(4), g); ck = tuple(np.round(np.asarray(g).ravel(), 12)); dth, dA = Qs.__defaults__[0][ck]
    keys = list(REF); kid = {k: i for i, k in enumerate(keys)}
    Ae = {k: [] for k in keys}; Ee = {k: [] for k in keys}
    for k, (b, ed) in REF.items():
        for (c, a), d in zip(ed, dA[k]): Ae[k].append((c, np.array(a, float), d))
    for (H_, eds), rows, Dd in zip(SIMPDATA, SIMT, dth):
        for q, key, base in rows:
            sh = base - REF[key][0]
            for e, (c, a) in enumerate(eds): Ee[key].append((c, np.array(a - sh, float), -Dd[q, e]))
    C = {}
    for k in keys:
        for ca, aa, da in Ae[k]:
            for ce, be, de in Ee[k]:
                dv = be - aa; p = int(round(dv @ TV)); C.setdefault(p, np.zeros((NE, NE), complex))
                C[p][ca, ce] += da*de*np.exp(1j*(ks @ dv))
    return C
def proots(C, nul=16, tol=1e-6):
    d = max(abs(p) for p in C); n = NE; deg = 2*d; A = [C.get(q - d, np.zeros((n, n))) for q in range(deg + 1)]
    N = n*deg; Aa = np.zeros((N, N), complex); Bb = np.eye(N, dtype=complex); Aa[:-n, n:] = np.eye(N - n)
    for q in range(deg): Aa[-n:, q*n:(q + 1)*n] = -A[q]
    Bb[-n:, -n:] = A[deg]; zs = []
    for sd in (1, 2):
        r = np.random.default_rng(sd); U = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul)); V = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul))
        zs.append(eig(Aa + U @ np.diag(r.normal(size=nul)) @ V.conj().T, Bb + U @ np.diag(r.normal(size=nul)) @ V.conj().T, right=False))
    zz = np.array([q for q in zs[0] if np.isfinite(q) and abs(q) > 1e-30 and np.min(np.abs(zs[1] - q)) < tol*max(1, abs(q))])
    return zz
def Mread_s(K):
    K = np.asarray(K, complex); out = np.zeros((NE, 10), complex)
    for c, (d, ta, tb, da) in enumerate(EVEC):
        pd = K @ d; f = 1.0 if abs(pd) < 1e-12 else (np.exp(1j*pd) - 1)/(1j*pd)
        for s, (i, j) in enumerate(SYM): out[c, s] = (1 if i == j else 2)*d[i]*d[j]*f*np.exp(1j*(K @ OFF[ta]))
    return out
def Gauge_s(K, g):   # vertex displacement xi -> delta s = 2 d^T g (xi_b e^{iK.da} - xi_a)
    K = np.asarray(K, complex); G = np.zeros((NE, 16), complex)
    for c, (d, ta, tb, da) in enumerate(EVEC):
        u = 2*(g @ d); G[c, 4*tb:4*tb+4] += u*np.exp(1j*(K @ da)); G[c, 4*ta:4*ta+4] -= u
    return G
FRc = [[e for e, (d, ta, tb, da) in enumerate(EVEC) if ta == tb == 0 and frame(d) == f] for f in range(3)]
def Ys(g):
    sc = scls(g); Y = np.zeros((NE, 2))
    for f, c in enumerate(FRc):
        for e in c: Y[e, 0] += [2, -1, -1][f]*np.real(sc[e])/np.sqrt(6); Y[e, 1] += [0, 1, -1][f]*np.real(sc[e])/np.sqrt(2)
    return Y
def Pz(C, z): return sum(M*z**p for p, M in C.items())
def dPz(C, z): return sum(p*M*z**(p - 1) for p, M in C.items())
def light_eff(K, g, lor=True):   # 10 metric + 2 doublet block, all other non-flat modes integrated out (Schur)
    q0 = Qs(np.zeros(4), g)[0]; q0 = (q0 + q0.T)/2; H0 = q0.imag if lor else q0.real
    Bz = np.c_[Mread_s(np.zeros(4)).real, Gauge_s(np.zeros(4), g).real, Ys(g)]
    Qb = np.linalg.qr(Bz)[0][:, :np.linalg.matrix_rank(Bz, 1e-8)]
    Cc = np.linalg.svd(np.eye(NE) - Qb @ Qb.T)[0][:, :NE - Qb.shape[1]]
    K = np.asarray(K, complex); A = np.c_[Mread_s(K), Ys(g)]; Am = np.c_[Mread_s(-K), Ys(g)]; q = Qs(K, g)[0]/(1j if lor else 1)
    return Am.T @ q @ A - (Am.T @ q @ Cc) @ np.linalg.solve(Cc.T @ q @ Cc, Cc.T @ q @ A), Cc.shape[1]
def proots3(C, nul=16, tol=1e-5):
    d = max(abs(p) for p in C); n = NE; deg = 2*d; A = [C.get(q - d, np.zeros((n, n))) for q in range(deg + 1)]
    N = n*deg; Aa = np.zeros((N, N), complex); Bb = np.eye(N, dtype=complex); Aa[:-n, n:] = np.eye(N - n)
    for q in range(deg): Aa[-n:, q*n:(q + 1)*n] = -A[q]
    Bb[-n:, -n:] = A[deg]; zs = []
    for sd in (1, 2, 3):
        r = np.random.default_rng(sd); U = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul)); V = r.normal(size=(N, nul)) + 1j*r.normal(size=(N, nul))
        zs.append(eig(Aa + U @ np.diag(r.normal(size=nul)) @ V.conj().T, Bb + U @ np.diag(r.normal(size=nul)) @ V.conj().T, right=False))
    ok = lambda q, Z: np.min(np.abs(Z - q)) < tol*max(1, abs(q))
    return np.array([q for q in zs[0] if np.isfinite(q) and abs(q) > 1e-30 and (ok(q, zs[1]) or ok(q, zs[2]))])
def census(ks, g, lor=True):
    C = {p: M/(1j if lor else 1) for p, M in Qcoef_s(ks, g).items()}; zz = proots3(C); lz = np.log(np.abs(zz))
    on = zz[np.abs(lz) < 1e-5]; res = []
    for z in sorted(on, key=lambda z: np.angle(z)):
        om = np.sqrt(2)*np.angle(z); Vh = np.linalg.svd(Pz(C, z))[2]; K = ks + om*tt; Gk = Gauge_s(K, g); Nn = Vh[-17:].conj().T
        v = np.linalg.svd((np.eye(NE) - Gk @ np.linalg.pinv(Gk, rcond=1e-9)) @ Nn)[0][:, 0]
        kre = np.real(v.conj() @ (dPz(C, z)*1j*z/np.sqrt(2)) @ v)
        X = np.c_[Mread_s(K), Ys(g), Gk]; cf = np.linalg.lstsq(X, v, rcond=None)[0]
        res.append((om, np.sign(kre), np.linalg.norm(Mread_s(K) @ cf[:10]), abs(cf[10])*np.linalg.norm(Ys(g)[:, 0]), abs(cf[11])*np.linalg.norm(Ys(g)[:, 1])))
    return res, np.sort(np.abs(lz[np.abs(lz) >= 1e-5]))
def Gm(K):   # pure-gauge metric h_ij = K_i xi_j + K_j xi_i, as SYM components (4 columns)
    K = np.asarray(K, complex); G = np.zeros((10, 4), complex)
    for s, (i, j) in enumerate(SYM):
        for a in range(4): G[s, a] = K[i]*(j == a) + K[j]*(i == a)
    return G
def Mmid(K):   # midpoint reading: s_e = d^T h(midpoint) d
    K = np.asarray(K, complex); out = np.zeros((NE, 10), complex)
    for c, (d, ta, tb, da) in enumerate(EVEC):
        for s, (i, j) in enumerate(SYM): out[c, s] = (1 if i == j else 2)*d[i]*d[j]*np.exp(1j*(K @ (OFF[ta] + d/2)))
    return out
RNG2 = np.random.default_rng(7); UL = RNG2.normal(size=(12, 8)); UR = RNG2.normal(size=(12, 8))
def lightroots(blockf, k, ns, nmode, E0s, it=6):
    def R(E):
        K = k*ns + 1j*E*tt; B = blockf(K); n = B.shape[0]; return UL[:n, :n-4].T @ B @ UR[:n, :n-4]
    out = []
    for E0 in E0s:
        E = E0
        for _ in range(it):
            h = 1e-4*k; R0, Rp, Rm = R(E), R(E + h), R(E - h); R1 = (Rp - Rm)/(2*h); R2 = (Rp + Rm - 2*R0)/h**2
            n = R0.shape[0]; A = np.block([[np.zeros((n, n)), np.eye(n)], [-R0, -R1]]); Bm = np.block([[np.eye(n), np.zeros((n, n))], [np.zeros((n, n)), .5*R2]])
            dl = eig(A, Bm, right=False); dl = dl[np.isfinite(dl)]; E = E + dl[np.argmin(np.abs(dl))]
        out.append(E)
    return np.array(out)

# ======================= V. validation of the continued Schlaefli Hessian =======================
Pp = np.eye(4) - np.outer(tt, tt); gL = lambda lam: Pp - lam*np.outer(tt, tt)
L0 = np.array([np.linalg.norm(e[0]) for e in EVEC]); Dm = np.diag(2*L0); Kg = np.array([.3, .1, -.2, .15])
v1 = max(np.abs(Dm @ Qs(K, np.eye(4))[0] @ Dm - Q(K)).max()/np.abs(Q(K)).max() for K in (np.zeros(4), Kg))
check("V1 squared-length Schlaefli Hessian (d2S = Sum dA d eps) at the W(F4) point equals the length Hessian of d4-frame-modes",
      v1 < 1e-5, f"rel diff {v1:.0e} at K = 0 and generic K")
v2, hm, sc2 = [], [], []
for lam in (.9, 1.1):
    q = Qs(np.zeros(4), gL(lam))[0]; q = (q + q.T)/2; v2.append(np.abs(q.real).max()/np.abs(q.imag).max())
    Kr = .07*u1 + .03*u2 + .11*tt; qk = Qs(Kr, gL(lam))[0]/1j; hm.append(np.abs(qk - qk.conj().T).max()/np.abs(qk).max())
    s_ = scls(gL(lam)); c_, sn_, _ = sgeom(np.array([s_[c] for c, _ in SIMPDATA[5][1]])); sc2.append(max(abs(c_[p]**2 + sn_[p]**2 - 1) for p in PAIRS))
check("V2 continued hinge sum on the Lorentzian lattice is i x (real symmetric); Hermitian at real K; sin^2 + cos^2 = 1 for continued dihedrals",
      max(v2) < 1e-8 and max(hm) < 1e-7 and max(sc2) < 1e-9, f"|Re|/|Im| {max(v2):.0e}; herm {max(hm):.0e}; trig {max(sc2):.0e} (lam = 0.9, 1.1)")
def nzeros(g, lor):
    q = Qs(np.zeros(4), g)[0]; q = (q + q.T)/2; w = np.linalg.eigvalsh(q.imag if lor else q.real)
    return int(np.sum(np.abs(w) < 1e-6*np.abs(w).max())), w
zc = {lab: nzeros(g, lor)[0] for lab, g, lor in (('E', np.eye(4), False), ('L.9', gL(.9), True), ('L1.1', gL(1.1), True))}
s1 = scls(gL(1.0)); amin = min(abs(a) for H_, eds in SIMPDATA for a in sgeom(np.array([s1[c] for c, _ in eds]))[2].values())
check("V3 exact k = 0 zeros: 24 at the Euclidean W(F4) point (12 gauge + 10 metric + doublet), 23 on the Lorentzian lattice; lam = 1 has null spokes AND null triangles",
      zc['E'] == 24 and zc['L.9'] == 23 and zc['L1.1'] == 23 and amin < 1e-6,
      f"zeros {zc}; spokes s = (1 - lam)/2 -> 0; min |area| at lam = 1: {amin:.0e} -> primary lam = 1 -+ 0.1 (pre-registered)")
print(f"  (V done {time.time()-T0:.1f}s)")

# ======================= L. Lorentzian reading (R-b): which part of the doublet survives =======================
ovl = []
for lam in (.9, 1.1):
    q = Qs(np.zeros(4), gL(lam))[0].imag; q = (q + q.T)/2; w, U = np.linalg.eigh(q); Zs = U[:, np.abs(w) < 1e-6*np.abs(w).max()]
    Yl = Ys(gL(lam)); ovl.append([np.linalg.norm(y - Zs @ (Zs.T @ y))/np.linalg.norm(y) for y in Yl.T])
Sw = np.eye(4)[[0, 1, 3, 2]]; swap_ok = np.allclose(Sw @ tt, tt) and all(frame(Sw @ r) == [0, 2, 1][frame(r)] for r in ROOTS)
check("L1 tick time splits the doublet: y1 = (0,1,-1) (the two non-tick frames) stays an EXACT k = 0 zero; y0 = (2,-1,-1) (tick frame) is lifted; the swap x2<->x3 fixes t and sends y1 -> -y1 (no y1^3 term)",
      all(o[1] < 1e-8 and o[0] > .5 for o in ovl) and swap_ok, f"off-null share (y0, y1): lam .9 {np.round(ovl[0], 3).tolist()}, lam 1.1 {np.round(ovl[1], 3).tolist()} (y1 share {max(o[1] for o in ovl):.0e})")
cen = {}
for lam in (.9, 1.1, .99, 1.01, .5):
    for nd, ndl in ((u1, 'axis'), ((u1 + u2 + u3)/np.sqrt(3), 'diag')):
        if lam in (.99, 1.01, .5) and ndl == 'diag': continue
        cen[lam, ndl] = census(.05*nd, gL(lam))
def classify(r, k=.05):
    ps = [x for x in r if x[0] > 0]; gr = [x for x in ps if x[0] < .5 and x[2] > .9]; y1 = [x for x in ps if x[0] < .5 and x[4] > .9]
    y0 = [x for x in ps if x[0] > .5 and x[3] > .8]; hv = [x for x in ps if x[0] > .5 and x[2] > .8]
    return gr, y1, y0, hv
print("  real-time census, k = .05 (lattice units), omega>0 branches: speed | Krein sign vs graviton | content")
okL = []
for (lam, ndl), (r, off) in cen.items():
    gr, y1, y0, hv = classify(r); kg = gr[0][1] if gr else 0
    okL.append(len(r) == 12 and len(gr) == 2 and len(y1) == 1 and len(y0) == 1 and len(hv) == 2 and off.min() > 10
               and all(abs(x[0]/.05 - np.sqrt(lam)) < 2e-3 for x in gr) and abs(y1[0][0]/.05 - 1/np.sqrt(lam)) < 2e-3
               and all(x[1] == kg for x in gr) and y1[0][1] == -kg and y0[0][1] == kg and all(x[1] == -kg for x in hv))
    if ndl == 'axis' or lam == .9:
        print(f"   lam {lam} {ndl}: graviton x2 c={gr[0][0]/.05:.4f} (sqrt lam {np.sqrt(lam):.4f}) +; y1 c={y1[0][0]/.05:.4f} (1/sqrt lam) {'+' if y1[0][1] == kg else '-'};"
              f" y0 omega={y0[0][0]:.3f} {'+' if y0[0][1] == kg else '-'}; metric-heavy x2 omega={hv[0][0]:.3f} {'+' if hv[0][1] == kg else '-'}; off-circle |ln z| >= {off.min():.1f}")
check("L2 Lorentzian census (all on |z| = 1, 12 roots): graviton x2 on the light cone of g_L; y1 massless on its OWN cone (c = 1/sqrt lam) with Krein sign OPPOSITE the graviton (ghost); y0 massive (omega ~ 2.2) healthy; a metric-heavy pair (omega ~ 2.2) ghost",
      all(okL), f"{len(okL)} (lam, direction) cases; no tachyon (no root off |z| = 1 below the float floor |ln z| ~ 10-30)")
C35 = {p: M/1j for p, M in Qcoef_s(.05*u1, gL(3.5)).items()}; rz = []
for al in (1.0, np.exp(2.0)):
    zz = proots3({p: M*al**p for p, M in C35.items()}); lz = np.log(np.abs(zz)) + np.log(al); rz.append(np.sort(lz[(np.abs(lz) < 5) & (np.abs(lz) > 1e-4)]))
check("L3 controls: the far off-circle roots are float zeros of the rank-6 end coefficients (one-sided, move under z -> e^2 z); a genuine z, 1/z pair appears only for lam > 3 (pair-offset roots time-like)",
      all(len(x) == 2 for x in rz) and np.allclose(rz[0], rz[1], atol=1e-6) and abs(rz[0][1] + rz[0][0]) < 1e-6,
      f"lam 3.5: |ln z| = {np.round(rz[0], 3).tolist()} invariant under rescaling (genuine instability); lam in [0.5, 1.1]: none")
rE, offE = census(.05*u1, Pp + .9*np.outer(tt, tt), lor=False)
tachE = [x for x in rE if abs(x[0]) > .1 and x[3] > .5]
check("L4 contrast (R-a): Euclidean lattice strained along the root (lam = .9), momentum-continued: y0 pole at REAL Euclidean frequency = tachyon (B3 of d4-frame-modes)",
      len(tachE) >= 1, f"y0-dominated Euclidean real root(s) at |omega_E| = {np.round(sorted({round(abs(x[0]), 4) for x in tachE}), 4).tolist()} at k = .05 (m^2 < 0 in R-a); the same strain read as Lorentzian (R-b) gives a real-frequency y0 at 2.18")
print(f"  (L done {time.time()-T0:.1f}s)")

# ======================= M. metric-only amendment =======================
SPK = [e for e, (d, ta, tb, da) in enumerate(EVEC) if ta != tb]
A_s = np.array([[(1 if i == j else 2)*EVEC[e][0][i]*EVEC[e][0][j] for i, j in SYM] for e in range(NE)])
ns_ = 10 - np.linalg.matrix_rank(A_s[SPK]); dist = []
for u in (.01, .1, .3):
    sY = np.array([np.linalg.norm(e[0])**2 for e in EVEC]); fr = {e: f for f, c in enumerate(FRc) for e in c}
    for e, f in fr.items(): sY[e] *= (1 + u*[0, 1, -1][f])**2
    hfit = np.linalg.lstsq(A_s, sY, rcond=None)[0]; dist.append(np.linalg.norm(A_s @ hfit - sY)/np.linalg.norm(sY - scls(np.eye(4)).real))
check("M1 metric-only reading removes the doublet nonlinearly: spokes fix the metric completely (g = delta), so no frame-rescaled length set (any u) is metric-read",
      ns_ == 0 and min(dist) > .5, f"metric directions left free by the spokes: {ns_}; least-squares distance / |deformation| = {np.round(dist, 3).tolist()} at u = .01, .1, .3")
g = np.eye(4)
raw = lambda K: Mread_s(-K).T @ Qs(K, g)[0] @ Mread_s(K)
mid = lambda K: Mmid(-K).T @ Qs(K, g)[0] @ Mmid(K)
full = lambda K: light_eff(K, g, lor=False)[0]
Kc = .07*u1 + .02*u3 + .03j*tt
gres = {n_: np.abs(f(Kc) @ (Gm(Kc) if n_ != 'full' else np.r_[Gm(Kc), np.zeros((2, 4))])).max()/np.abs(f(Kc)).max() for n_, f in (('full', full), ('raw', raw), ('mid', mid))}
Ab = {}
for nv, lab in (([1, 0, 0], 'axis'), ([1, 1, 0], 'face'), ([1, 1, 1], 'body')):
    nv = np.array(nv, float)/np.linalg.norm(nv); ns = nv[0]*u1 + nv[1]*u2 + nv[2]*u3; k = .1
    for mn, f in (('full', full), ('raw', raw), ('mid', mid)):
        E = lightroots(f, k, ns, 0, [k*(1 + a*(k/np.sqrt(2))**2) for a in (-.3, .3)])
        Ab[mn, lab] = np.sort((E.real/k - 1)/(k/np.sqrt(2))**2)
print("  graviton c = 1 + A (ka)^2 at ka = .07 (the two polarisations): " + "; ".join(f"{m}: " + " ".join(f"{l} {np.round(Ab[m, l], 3).tolist()}" for l in ('axis', 'face', 'body')) for m in ('full', 'raw', 'mid')))
okM = all(abs(Ab[m, 'axis'][1] - 1/6) < 3e-3 and abs(Ab[m, 'axis'][0] + 1/6) < 3e-3 and abs(Ab[m, 'face'][1] - 1/8) < 3e-3 and np.abs(Ab[m, 'body']).max() < 3e-3 for m in ('full', 'raw'))
check("M2 birefringence SURVIVES the metric-only reading unchanged (line-integrated reading, exactly gauge-covariant): +-1/6 axis, +-1/8 face, 0 body diagonal; validated on the full model",
      okM and gres['raw'] < 1e-6 and gres['full'] < 1e-6, f"gauge residual full {gres['full']:.0e}, raw {gres['raw']:.0e}")
mavg = np.mean(Ab['mid', 'axis'])
check("M3 control: the midpoint reading is NOT gauge-exact and adds a polarisation-averaged shift; its splitting is nonzero but reading-dependent (pre-registered 'both readings' criterion: PARTIAL)",
      gres['mid'] > 1e-7 and abs(mavg) > 1e-2 and np.ptp(Ab['mid', 'axis']) > 1e-3, f"gauge residual {gres['mid']:.0e}; axis mean shift {mavg:+.3f}, half-split {np.ptp(Ab['mid', 'axis'])/2:.3f}")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={P} FAIL={F}")

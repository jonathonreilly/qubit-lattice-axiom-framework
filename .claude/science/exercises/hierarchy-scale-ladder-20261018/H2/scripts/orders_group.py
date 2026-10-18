#!/usr/bin/env python3
"""HIER-2 A3: symmetry-fixed orders of protected Dirac masses at the eight cube-point nodes.

Node space V16 = C^8 (nodes s in Z2^3, chirality (-1)^hw(s)) x C^2 (spin-1/2), the node and
charge structure of PR #9702 item 7 (and of naive/staggered fermions).
Symmetry group Gamma = Z2^3 (translations mod 2, acting by (-1)^{s.t}) x| O_h, with
  proper rotations: node s -> P s (axis permutation), spin U (binary octahedral lift);
  improper elements (rotation x inversion): node s -> P s + 111, spin U of the proper part.
For each spurion irrep R of Gamma (translation charge orbit x little-group irrep) and each
symmetry-fixed direction phi in R (a line that is the full fixed space of some subgroup),
build a GENERIC equivariant effective Hamiltonian on V16,
  H(eps) = sum_{n=1..NMAX} eps^n f_n(phi),  f_n = Reynolds average of a random degree-n
polynomial map R -> Herm(V16),
and read the Dirac masses as the singular values of its chirality-odd block P_+ H P_-.
Report the leading order in eps of every Dirac mass.  Supplied: the node representation; the
assumption that the symmetric theory has all eight nodes at E = 0 (f_0 = 0).
"""
import itertools, sys
import numpy as np

NMAX = 7
rng_master = np.random.default_rng(20261018)

# ---------------- O_h as signed permutation matrices
OH = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i, j in enumerate(perm): M[i, j] = sg[i]
        OH.append(M)
assert len(OH) == 48
def oidx(M):
    for k, X in enumerate(OH):
        if (X == M).all(): return k
    raise ValueError
DET = [int(round(np.linalg.det(M))) for M in OH]
PROP = [DET[k] * OH[k] for k in range(48)]          # proper part
PERM = [np.abs(M) for M in OH]                       # axis permutation matrix
OMUL = np.array([[oidx(OH[a] @ OH[b]) for b in range(48)] for a in range(48)])

# ---------------- spin lift via the binary octahedral group (construction as in the PR #9702 runner)
def q2su(qv):
    a, b, c, d = qv; return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])
qs = []
for i in range(4):
    for s_ in (1, -1):
        vv = [0]*4; vv[i] = s_; qs.append(vv)
for sg in itertools.product((1, -1), repeat=4): qs.append([x/2 for x in sg])
for i, j in itertools.combinations(range(4), 2):
    for si, sj in itertools.product((1, -1), repeat=2):
        vv = [0]*4; vv[i], vv[j] = si/np.sqrt(2), sj/np.sqrt(2); qs.append(vv)
G2 = [q2su(qv) for qv in qs]
PAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
def so3(U): return np.rint(np.array([[0.5*np.real(np.trace(PAU[i] @ U @ PAU[j] @ U.conj().T)) for j in range(3)] for i in range(3)])).astype(int)
SPIN = [None]*48
for U in G2:
    R = so3(U)
    for k in range(48):
        if DET[k] == 1 and (OH[k] == R).all() and SPIN[k] is None: SPIN[k] = U
for k in range(48):
    if DET[k] == -1: SPIN[k] = SPIN[oidx(PROP[k])]
assert all(S is not None for S in SPIN)
for k in range(48):  # check U sigma_j U^dag = sum_i R_ij sigma_i (axial)
    U = SPIN[k]; R = PROP[k]
    for j in range(3):
        assert np.allclose(U @ PAU[j] @ U.conj().T, sum(R[i, j] * PAU[i] for i in range(3)))

# ---------------- node labels and Gamma
NODES = list(itertools.product((0, 1), repeat=3)); NID = {s: i for i, s in enumerate(NODES)}
HW = [sum(s) for s in NODES]; CHI = np.array([(-1)**h for h in HW])
TR = NODES  # translations mod 2, same labels
def tvec(t): return np.array(t)
def node_map(k, s):
    s2 = tuple(int(x) % 2 for x in PERM[k] @ np.array(s))
    if DET[k] == -1: s2 = tuple((x + 1) % 2 for x in s2)
    return s2
GAM = [(ti, k) for ti in range(8) for k in range(48)]   # element (t, M)
GID = {g: i for i, g in enumerate(GAM)}
def gmul(g1, g2):
    (t1, k1), (t2, k2) = g1, g2
    t = tuple((a + b) % 2 for a, b in zip(TR[t1], PERM[k1] @ np.array(TR[t2])))
    return (NID[t], OMUL[k1, k2])
NG = len(GAM)
MUL = np.array([[GID[gmul(a, b)] for b in GAM] for a in GAM])

def kinv(k): return oidx(OH[k].T)
VARIANT = sys.argv[1] if len(sys.argv) > 1 else 'A1-A1'
if VARIANT == 'naive': VARIANT = 'A1-A1'
if VARIANT == 'twist': VARIANT = 'A2-A1'
TAU0, TAU6 = VARIANT.split('-')
def a2(k):
    return int(round(np.linalg.det(np.abs(PROP[k]))))
def tau0(k):      # character of O (proper) on the {000,111} orbit
    return 1 if TAU0 == 'A1' else a2(k)
def tau6(k):      # character of D4 (proper, about z) on the 6-node orbit
    R = PROP[k]; A2 = R[2, 2]; B1 = int(round(np.linalg.det(np.abs(R[:2, :2]))))
    return {'A1': 1, 'A2': A2, 'B1': B1, 'B2': A2 * B1}[TAU6]
ORB0 = [(0, 0, 0), (1, 1, 1)]
ORB6 = [s for s in NODES if s not in ORB0]
CR = {}
for s in ORB0 + ORB6:
    base = (0, 0, 0) if s in ORB0 else (0, 0, 1)
    for k in range(48):
        if node_map(k, base) == s: CR[s] = k; break
def node_phase(k, s):
    s2 = node_map(k, s)
    h = OMUL[OMUL[kinv(CR[s2]), k], CR[s]]
    if s in ORB0:
        assert DET[h] == 1
        return tau0(h)
    assert DET[h] == 1 and abs(OH[h][2, 2]) == 1
    return tau6(h)
def D_node(g):
    ti, k = g; t = TR[ti]
    P = np.zeros((8, 8))
    for s in NODES:
        P[NID[node_map(k, s)], NID[s]] = node_phase(k, s)
    T = np.diag([(-1.0)**int(np.dot(s, t)) for s in NODES])
    return np.kron(T @ P, SPIN[k])
DN = np.array([D_node(g) for g in GAM])
# projective check: D(g1)D(g2) = phase * D(g1 g2)
for _ in range(200):
    a, b = rng_master.integers(NG, size=2)
    X = DN[a] @ DN[b]; Y = DN[MUL[a, b]]
    ph = np.vdot(Y.ravel(), X.ravel()) / np.vdot(Y.ravel(), Y.ravel())
    assert abs(abs(ph) - 1) < 1e-9 and np.allclose(X, ph * Y)
# the node-space Weyl frames are covariant: H_s(q) = sum_j (-1)^{s_j} q_j sigma_j
def H0(q):
    H = np.zeros((16, 16), complex)
    for s in NODES:
        i = NID[s]; H[2*i:2*i+2, 2*i:2*i+2] = sum(((-1)**s[j]) * q[j] * PAU[j] for j in range(3))
    return H
for _ in range(20):
    q = rng_master.normal(size=3); g = int(rng_master.integers(NG)); ti, k = GAM[g]
    lhs = DN[g] @ H0(q) @ DN[g].conj().T
    rhs = H0(OH[k] @ q)   # improper elements: q -> M q (vector), frames as derived in PREREG notes
    assert np.allclose(lhs, rhs), "node-space Weyl theory not covariant"

# ---------------- spurion irreps of Gamma
def oh_irreps():
    B = np.array([[1, -1, 0], [1, 1, -2]], float).T; B /= np.linalg.norm(B, axis=0)
    out = {}
    for name in ['A1', 'A2', 'E', 'T1', 'T2']:
        for par in 'gu':
            mats = []
            for k in range(48):
                R = PROP[k]; Pm = np.abs(R); sgn = int(round(np.linalg.det(Pm)))
                p = DET[k] if par == 'u' else 1
                if name == 'A1': m = np.eye(1)
                elif name == 'A2': m = sgn * np.eye(1)
                elif name == 'E': m = B.T @ Pm @ B
                elif name == 'T1': m = R.astype(float)
                else: m = sgn * R.astype(float)
                mats.append(p * m)
            out[name + par] = mats
    return out
OHIRR = oh_irreps()
LZ = [k for k in range(48) if abs(OH[k][2, 2]) == 1]   # D4h about z
def d4h_irreps():
    out = {}
    for name in ['A1', 'A2', 'B1', 'B2', 'E']:
        for par in 'gu':
            d = {}
            for k in LZ:
                R = PROP[k]; p = DET[k] if par == 'u' else 1
                a2 = R[2, 2]; b1 = int(round(np.linalg.det(np.abs(R[:2, :2]))))
                m = {'A1': np.eye(1), 'A2': a2*np.eye(1), 'B1': b1*np.eye(1), 'B2': a2*b1*np.eye(1),
                     'E': R[:2, :2].astype(float)}[name]
                d[k] = p * m
            out[name + par] = d
    return out
D4IRR = d4h_irreps()
# coset reps g_i with P g_i e_z = e_i
EZ = np.array([0, 0, 1])
COS = {}
for k in range(48):
    v = tuple(PERM[k] @ EZ)
    if v not in COS and DET[k] == 1: COS[v] = k
CREP = [COS[(1, 0, 0)], COS[(0, 1, 0)], COS[(0, 0, 1)]]

def build_rep(kind, irr):
    """kind in {'000','111','hw1','hw2'}; returns list of matrices rho(g) for g in GAM."""
    mats = []
    if kind in ('000', '111'):
        c = (0, 0, 0) if kind == '000' else (1, 1, 1)
        for (ti, k) in GAM:
            mats.append(((-1.0)**int(np.dot(c, TR[ti]))) * OHIRR[irr][k])
        return mats
    c0 = np.array([0, 0, 1]) if kind == 'hw1' else np.array([1, 1, 0])
    dimr = D4IRR[irr][LZ[0]].shape[0]
    for (ti, k) in GAM:
        M = np.zeros((3*dimr, 3*dimr))
        for j in range(3):
            ej = PERM[CREP[j]] @ EZ
            ei = PERM[k] @ ej
            i = [tuple(PERM[CREP[x]] @ EZ) for x in range(3)].index(tuple(ei))
            h = OMUL[OMUL[kinv(CREP[i]), k], CREP[j]]
            assert h in D4IRR[irr]
            ci = PERM[CREP[i]] @ c0
            M[i*dimr:(i+1)*dimr, j*dimr:(j+1)*dimr] = ((-1.0)**int(np.dot(ci, TR[ti]))) * D4IRR[irr][h]
        mats.append(M)
    return mats

REPS = {}
for kind in ('000', '111'):
    for irr in OHIRR: REPS[(kind, irr)] = build_rep(kind, irr)
for kind in ('hw1', 'hw2'):
    for irr in D4IRR: REPS[(kind, irr)] = build_rep(kind, irr)
# homomorphism + irreducibility checks
for key, mats in REPS.items():
    for _ in range(60):
        a, b = rng_master.integers(NG, size=2)
        assert np.allclose(mats[a] @ mats[b], mats[MUL[a, b]]), key
    chi = np.array([np.trace(m) for m in mats])
    assert abs(np.dot(chi, chi) / NG - 1) < 1e-9, ("reducible", key)

# ---------------- subgroups and symmetry-fixed directions
def closure(gens):
    S = {GID[(0, oidx(np.eye(3, dtype=int)))]}
    frontier = list(S)
    gens = list(gens)
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = MUL[x, g]
                if y not in S: S.add(y); new.append(y)
        frontier = new
    return frozenset(S)
SUBS = set()
for a in range(NG):
    SUBS.add(closure([a]))
for a in range(NG):
    for b in range(a+1, NG):
        SUBS.add(closure([a, b]))
pt = [GID[(0, k)] for k in range(48)]
for a, b, c in itertools.combinations(pt, 3):
    SUBS.add(closure([a, b, c]))
SUBS = list(SUBS)
print(f"subgroups found (<=2 generators of Gamma, <=3 of the point group): {len(SUBS)}")

def fixed_lines(mats):
    lines = []
    MA = np.array(mats)
    for H in SUBS:
        P = MA[list(H)].mean(axis=0)
        w, v = np.linalg.eigh((P + P.T) / 2)
        if np.sum(w > 0.5) == 1:
            phi = v[:, np.argmax(w)]
            lines.append((len(H), phi))
    # dedupe up to sign and Gamma-orbit
    reps = []
    seen = set()
    for order, phi in sorted(lines, key=lambda x: -x[0]):
        key = tuple(np.round(phi * np.sign(phi[np.argmax(np.abs(phi) > 1e-6)]), 6))
        if key in seen: continue
        seen.add(key)
        imgs = MA @ phi
        if any(np.max(np.abs(imgs @ psi)) > 1 - 1e-8 for _, psi in reps): continue
        reps.append((order, phi))
    return reps

# ---------------- generic equivariant effective Hamiltonians
def herm(n, rng):
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); return (A + A.conj().T) / 2
def generic_maps(mats, rng, K=24):
    d = mats[0].shape[0]
    polys = []
    for n in range(1, NMAX+1):
        W = rng.normal(size=(K, d)); Hs = [herm(16, rng) for _ in range(K)]
        polys.append((n, W, Hs))
    return polys
def f_eval(polys, mats, phi):
    out = []
    imgs = np.array([m @ phi for m in mats])            # (NG, d)
    for n, W, Hs in polys:
        coef = (imgs @ W.T) ** n                          # (NG, K)
        Hstack = np.array(Hs)                             # (K,16,16)
        X = np.einsum('gk,kij->gij', coef, Hstack)
        acc = np.einsum('gji,gjk,gkl->il', DN.conj(), X, DN)
        out.append(acc / NG)
    return out
PL = np.kron(np.diag((CHI < 0).astype(float)), np.eye(2)); PRm = np.kron(np.diag((CHI > 0).astype(float)), np.eye(2))
iL = [i for i in range(16) if PL[i, i] > 0]; iR = [i for i in range(16) if PRm[i, i] > 0]
EPS = [0.08, 0.04, 0.02, 0.01]
def masses(fs, eps):
    H = sum((eps**(n+1)) * fs[n] for n in range(NMAX))
    M = H[np.ix_(iR, iL)]
    return np.sort(np.linalg.svd(M, compute_uv=False))[::-1], H
def orders(fs):
    sv = np.array([masses(fs, e)[0] for e in EPS])        # (4 eps, 8 singular values)
    res = []
    for j in range(8):
        y = sv[:, j]
        if y[-1] < 1e-13 * max(1.0, sv[0, 0]) and y[0] < 1e-12:
            res.append(np.inf); continue
        sl = np.polyfit(np.log(EPS), np.log(np.maximum(y, 1e-300)), 1)[0]
        res.append(sl)
    return res, sv
def axial_shift_order(fs, j_nodes=None):
    # largest traceless (sigma) part of the even blocks at order eps^2: node shifts that can close order>=3 gaps
    E2 = fs[1]
    m = 0.0
    for s in NODES:
        i = NID[s]; B = E2[2*i:2*i+2, 2*i:2*i+2]
        m = max(m, np.linalg.norm(B - np.trace(B)/2*np.eye(2)))
    return m


EPS = [0.04, 0.02, 0.01, 0.005]
def stab(mats, phi):
    return [g for g in range(NG) if np.allclose(mats[g] @ phi, phi, atol=1e-9)]
def charge_of(kind, mats, phi):
    # translation character of phi (only meaningful if phi has a single charge)
    for ti, t in enumerate(TR):
        pass
    return None
def herm_basis_fixed(H, cvec):
    """dimension of the space of Hermitian X on V16 with D_h X D_h^dag = X for h in H and charge c."""
    # average a random Hermitian over H, project to charge c; rank of many samples
    rng = np.random.default_rng(5)
    S = []
    Tt = [np.kron(np.diag([(-1.0)**int(np.dot(s, t)) for s in NODES]), np.eye(2)) for t in TR]
    chi = [(-1.0)**int(np.dot(cvec, t)) for t in TR] if cvec is not None else None
    DH = DN[H]
    for _ in range(40):
        X = herm(16, rng)
        X = np.einsum('hij,jk,hlk->il', DH, X, DH.conj()) / len(H)
        if cvec is None:
            T111 = Tt[NID[(1, 1, 1)]]; X = (X - T111 @ X @ T111) / 2      # all odd charges (chirality-odd part)
        else:
            X = sum(chi[a] * Tt[a] @ X @ Tt[a] for a in range(8)) / 8
        S.append(np.concatenate([X.real.ravel(), X.imag.ravel()]))
    return np.linalg.matrix_rank(np.array(S), tol=1e-8)
def span_dim(vals):
    if not vals: return 0
    S = np.array([np.concatenate([X.real.ravel(), X.imag.ravel()]) for X in vals])
    return np.linalg.matrix_rank(S, tol=1e-8 * max(1.0, np.abs(S).max()))
def masses(fs, eps):
    H = sum((eps**(n+1)) * fs[n] for n in range(NMAX))
    M = H[np.ix_(iR, iL)]
    return np.sort(np.linalg.svd(M, compute_uv=False))[::-1]
def orders(fs):
    sv = np.array([masses(fs, e) for e in EPS])
    res = []
    for j in range(8):
        y = sv[:, j]
        if y.max() < 1e-12: res.append(np.inf); continue
        sl = np.log(y[-1] / y[-2]) / np.log(EPS[-1] / EPS[-2])
        res.append(sl)
    return res, sv[-1]
def mults(svs):
    svs = svs[svs > 1e-12]; out = []
    for v in svs:
        if out and abs(v - out[-1][0]) <= 1e-7 * v: out[-1][1] += 1
        else: out.append([v, 1])
    return [m for _, m in out]

if __name__ == '__main__':
    summary = []
    for ki, (key, mats) in enumerate(REPS.items()):
        kind = key[0]
        if kind in ('000', 'hw2'):
            cvecs = None
        lines = fixed_lines(mats)
        for li, (order, phi) in enumerate(lines):
            H = stab(mats, phi)
            # charge vector of phi: translations act on phi by a character if phi has one charge
            tch = []
            for ti in range(8):
                g = GID[(ti, oidx(np.eye(3, dtype=int)))]
                v = mats[g] @ phi
                tch.append(1 if np.allclose(v, phi) else (-1 if np.allclose(v, -phi) else 0))
            single = all(x != 0 for x in tch)
            cvec = None
            if single:
                for c in NODES:
                    if all(tch[ti] == (-1)**int(np.dot(c, TR[ti])) for ti in range(8)): cvec = c
            odd = cvec is not None and sum(cvec) % 2 == 1
            # generic maps: seeds for orders, plus extra samples for span dims
            od_all = []; svlast = None
            Vn = {1: [], 3: [], 5: []}
            for sd in range(6):
                rng = np.random.default_rng(1000 * ki + 17 * li + sd)
                polys = generic_maps(mats, rng)
                fs = f_eval(polys, mats, phi)
                fs = [f / max(np.linalg.norm(f), 1e-300) if np.linalg.norm(f) > 1e-10 else 0 * f for f in fs]
                for n in (1, 3, 5): Vn[n].append(fs[n-1])
                if sd < 2:
                    od, sv = orders(fs); od_all.append(od)
                    if sd == 0: svlast = sv
            d1 = span_dim(Vn[1]); d3 = span_dim(Vn[1] + Vn[3]); d5 = span_dim(Vn[1] + Vn[3] + Vn[5])
            dfix = herm_basis_fixed(H, cvec) if odd else (herm_basis_fixed(H, None) if cvec is None else None)
            r = [[('inf' if np.isinf(x) else f"{x:.2f}") for x in od] for od in od_all]
            fin = sorted(set(int(round(x)) for x in od_all[0] if np.isfinite(x)))
            fin2 = sorted(set(int(round(x)) for x in od_all[1] if np.isfinite(x)))
            mu = mults(svlast)
            summary.append(dict(key=key, li=li, H=len(H), c=cvec, fin=fin, fin2=fin2, mult=mu, d1=d1, d3=d3, d5=d5, dfix=dfix))
            print(f"{kind:>3} {key[1]:<4} dir{li:<2} |Stab|={len(H):<3} charge={cvec} orders s1={r[0]} s2={r[1]} distinct={fin}/{fin2} "
                  f"Dirac-mass multiplicities(sv)={mu} dimV1={d1} dimV1+3={d3} dimV1+3+5={d5} dimFix(H,charge)={dfix}")
            sys.stdout.flush()
    print(f"\nVARIANT = {VARIANT}")
    from collections import Counter
    print("distinct finite orders per (spurion, direction):", dict(Counter(len(s['fin']) for s in summary)))
    print("all finite orders seen:", sorted(set(o for s in summary for o in s['fin'] + s['fin2'])))
    odd = [s for s in summary if s['dfix'] is not None and s['c'] is not None]
    mc = [s for s in summary if s['c'] is None and s['key'][0] in ('111', 'hw1')]
    print(f"multi-charge directions: {len(mc)}; odd-part saturated at order 3: {sum(1 for s in mc if s['d3'] >= s['dfix'])} (note: V counts all charges, Fix counts odd part only; see per-line dims)")
    sat3 = [s for s in odd if s['d3'] == s['dfix']]
    print(f"odd single-charge directions: {len(odd)}; span saturated at order 3 (dim V1+V3 = dim Fix): {len(sat3)}; at order 1: {sum(1 for s in odd if s['d1'] == s['dfix'])}")
    bad = [s for s in odd if s['d3'] != s['dfix']]
    for s in bad: print("  NOT saturated at 3:", s['key'], s['li'], s['d1'], s['d3'], s['d5'], s['dfix'])
    multi = [s for s in summary if s['c'] is None and s['fin']]
    print(f"multi-charge directions with masses: {len(multi)}; their distinct orders: {sorted(set(tuple(s['fin']) for s in multi))}")
    print("max number of distinct Dirac-mass values (sv groups) for any single spurion:", max(len(s['mult']) for s in summary))

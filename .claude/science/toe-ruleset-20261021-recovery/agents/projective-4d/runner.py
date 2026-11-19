#!/usr/bin/env python3
"""projective-4d: does a projective site character on 2^4 tesseract blocks give one B4+-protected light taste?

Supplied model (finite diagnostics unless marked THEOREM; no physical identification is established): Z^4 sites with
one fermion mode each, tiled in two ways by 2^4 blocks offset by (1,1,1,1); a nearest-neighbour hop W inside each block,
Hermitian with W^2 = 1; the hypercubic group B4 (rotations B4+) about a block centre acting by site permutations times
phases (a monomial action = any projective site character); Euclidean operators built from the two tilings' hops.
 A  exact group theory: corner stabiliser and its Spin/Pin lift; forcing of the pi flux; the forced projective class;
    spin x taste factorisation of the light modes; all conjugacy classes of subgroups of B4 and B4+.
 B  the forced lattice: bands of D1 = 1 - Wo We, We + Wo, [Wo, We]; the diagonal shift; the block copy sign;
    dimension-four kinetic structures allowed on the light modes.
 C  Ginsparg-Wilson chirality (chirality Wo) and its index with U(1) links; transfer positivity tests.
Cited, not rederived: Nielsen-Ninomiya; Kogut-Susskind / Golterman-Smit staggered spin-taste; Adams (two-taste) and
Hoelbling (one-taste) staggered Wilson terms. Own code; no imports from other folders."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
import itertools, os, sys, time, signal
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
import numpy as np
T0 = time.time(); NP = NF = 0
rng = np.random.default_rng(20261022)
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
# ------------------------------------------------------------------ groups, lifts, block
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0]).astype(complex)]
Z2 = np.zeros((2, 2))
GAM = [np.block([[Z2, -1j * S], [1j * S, Z2]]) for S in SIG] + [np.block([[Z2, np.eye(2)], [np.eye(2), Z2]]).astype(complex)]
G5 = GAM[0] @ GAM[1] @ GAM[2] @ GAM[3]
allR = []
for perm in itertools.permutations(range(4)):
    for sg in itertools.product((1, -1), repeat=4):
        R = np.zeros((4, 4), int)
        for i in range(4): R[perm[i], i] = sg[i]
        allR.append(R)
n = len(allR); key = {tuple(R.ravel()): i for i, R in enumerate(allR)}
MUL = np.array([[key[tuple((allR[i] @ allR[j]).ravel())] for j in range(n)] for i in range(n)])
E0 = key[tuple(np.eye(4, dtype=int).ravel())]; INV = np.array([int(np.where(MUL[i] == E0)[0][0]) for i in range(n)])
det = np.array([int(round(np.linalg.det(R))) for R in allR]); PLUS = [g for g in range(n) if det[g] > 0]
CONJ = np.array([[MUL[MUL[g, i], INV[g]] for i in range(n)] for g in range(n)])
INVI = key[tuple((-np.eye(4, dtype=int)).ravel())]
def implementer(R, twist):
    d = (np.linalg.det(R) if twist else 1.0)
    A = np.vstack([np.kron(np.eye(4), GAM[r].T) - np.kron(d * sum(R[s, r] * GAM[s] for s in range(4)), np.eye(4)) for r in range(4)])
    _, sv, Vh = np.linalg.svd(A); S = Vh[-1].conj().reshape(4, 4); S = S / np.sqrt(np.trace(S.conj().T @ S).real / 4)
    S = S / np.linalg.det(S) ** 0.25
    if np.linalg.det(R) > 0 and abs(np.linalg.det(S[:2, :2]) + 1) < 1e-6: S = 1j * S      # chiral blocks in SU(2)
    return S
SPu = [implementer(R, False) for R in allR]                   # S gamma S^-1 = R gamma (Spin(4) on B4+)
SPt = [implementer(R, True) for R in allR]                    # twisted adjoint (Pin) on det -1
C16 = np.array([[(i >> m) & 1 for m in range(4)] for i in range(16)])
def cidx(x): return int(sum(int(x[m]) << m for m in range(4)))
PERM = np.array([[cidx(np.rint(R @ (C16[i] - .5) + .5).astype(int)) for i in range(16)] for R in allR])
EDGES = [(i, i + (1 << mu)) for i in range(16) for mu in range(4) if C16[i][mu] == 0]
FACES = [(i, i + (1 << a), i + (1 << a) + (1 << b), i + (1 << b)) for i in range(16) for a, b in itertools.combinations(range(4), 2)
         if C16[i][a] == 0 and C16[i][b] == 0]
def eta(x, mu): return (-1) ** int(sum(x[:mu]))
W = np.zeros((16, 16))
for (i, j) in EDGES: mu = int(np.log2(j - i)); W[i, j] = W[j, i] = 0.5 * eta(C16[i], mu)
ADJ = [[j for j in range(16) if W[i, j] != 0] for i in range(16)]
def covariance(Wb, perm):
    P = np.zeros((16, 16)); P[perm, np.arange(16)] = 1; Wp = P @ Wb @ P.T; d = np.zeros(16, complex); d[0] = 1; q = [0]; seen = {0}
    while q:
        x = q.pop(0)
        for y in ADJ[x]:
            if y not in seen: d[y] = d[x] * np.conj(Wb[x, y] / Wp[x, y]); seen.add(y); q.append(y)
    Ug = np.diag(d) @ P
    return Ug if np.allclose(Ug @ Wb @ Ug.conj().T, Wb) else None
def flux(Wb, f):
    a, b, c, d = f; z = Wb[b, a] * Wb[c, b] * Wb[d, c] * Wb[a, d]; return z / abs(z)
def key4(M): return tuple(np.round(np.concatenate([M.real.ravel(), M.imag.ravel()]), 6))
def gen_group(mats):
    I = np.eye(mats[0].shape[0], dtype=complex); seen = {key4(I): I}; fr = [I]
    while fr:
        new = []
        for X in fr:
            for g in mats:
                Y = X @ g; kk = key4(Y)
                if kk not in seen: seen[kk] = Y; new.append(Y)
        fr = new
    return list(seen.values())
def minus1_is_commutator(mats):
    cm = {}
    for a in mats:
        for b in mats: X = a @ b @ np.linalg.inv(a) @ np.linalg.inv(b); cm[key4(X)] = X
    return key4(-np.eye(mats[0].shape[0], dtype=complex)) in {key4(x) for x in gen_group(list(cm.values()))}
def commutant_basis(mats, d):
    A = np.vstack([np.kron(M, np.eye(d)) - np.kron(np.eye(d), M.T) for M in mats])
    _, s, vh = np.linalg.svd(A, full_matrices=False); k = int(np.sum(s < 1e-8)); return vh[d * d - k:].conj()
def vclosure(elems):
    S = np.zeros(n, bool); S[E0] = True; S[list(elems)] = True; gens = np.array(sorted(set(elems)) or [E0], int)
    while True:
        idx = np.nonzero(S)[0]; new = np.zeros(n, bool); new[MUL[np.ix_(idx, gens)].ravel()] = True
        if (new | S).sum() == S.sum(): return S
        S = S | new
def gens_of(H):
    gs = []; cur = np.zeros(n, bool); cur[E0] = True
    for h in H:
        if not cur[h]: gs.append(int(h)); cur = vclosure(gs)
    return gs

print('== A. exact group theory on the tesseract block')
stab = [g for g in range(n) if PERM[g][0] == 0]; stp = [g for g in stab if det[g] > 0]
klein = [g for g in stp if g != E0 and np.trace(allR[g]) == 0 and (allR[g] @ allR[g] == np.eye(4)).all()]
anti = all(np.allclose(SPu[a] @ SPu[b], -SPu[b] @ SPu[a]) for a, b in itertools.combinations(klein, 2))
pin_ok = all(minus1_is_commutator([L[g] for g in stab]) for L in (SPt, [SPt[g] * (1 if det[g] > 0 else 1j) for g in range(n)]))
Q8 = gen_group([SPu[g] for g in klein])
def chij(j, u):
    t = np.trace(u).real
    if abs(t - 2) < 1e-9: return 2 * j + 1
    if abs(t + 2) < 1e-9: return (2 * j + 1) * (-1) ** int(round(2 * j))
    th = 2 * np.arccos(np.clip(t / 2, -1, 1)); return np.sin((2 * j + 1) * th / 2) / np.sin(th / 2)
lines = {(jL, jR): round(sum(chij(jL, q[:2, :2]) * chij(jR, q[2:, 2:]) for q in Q8) / len(Q8), 6)
         for jL in np.arange(0, 2.01, 0.5) for jR in np.arange(0, 2.01, 0.5)}
spin_none = all(lines[k] == 0 for k in lines if (k[0] + k[1]) % 1 == 0.5) and any(lines[k] > 0 for k in lines if (k[0] + k[1]) % 1 == 0)
check('A1 THEOREM the corner stabiliser is S4 (B4), A4 (B4+); its 3 double transpositions are half-turns about orthogonal '
      'axes normal to the body diagonal; their Spin(4) lifts anticommute (quaternions), so -1 is a commutator in every '
      'Spin/Pin lift and no one-mode site character is spinorial; 4D coherent states (jL,jR) exist only for integral jL+jR',
      len(stab) == 24 and len(stp) == 12 and len(klein) == 3 and anti and len(Q8) == 8 and pin_ok and spin_none,
      f'eigenlines (1/2,0) {abs(lines[(0.5, 0)]):g}, (3/2,0) {abs(lines[(1.5, 0)]):g}, (1,1/2) {abs(lines[(1.0, 0.5)]):g}, (1/2,1/2) {lines[(0.5, 0.5)]:g}, (1,0) {abs(lines[(1.0, 0)]):g}')
eorb = {frozenset((int(PERM[g][EDGES[0][0]]), int(PERM[g][EDGES[0][1]]))) for g in PLUS}
dorb = {(int(PERM[g][EDGES[0][0]]), int(PERM[g][EDGES[0][1]])) for g in PLUS}
agree = tot = 0
for t in range(4000):
    if t % 4 < 2:
        ph = rng.uniform(0, 2 * np.pi, 32) if t % 4 == 0 else np.pi * rng.integers(0, 2, 32); Wt = np.zeros((16, 16), complex)
        for (a, b), p in zip(EDGES, ph): Wt[a, b] = 0.5 * np.exp(1j * p); Wt[b, a] = np.conj(Wt[a, b])
    else:
        dg = np.exp(1j * rng.uniform(0, 6.3, 16)); Wt = dg[:, None] * W * dg.conj()[None]
        if t % 4 == 3: a, b = EDGES[t % 32]; Wt[a, b] *= np.exp(1e-3j); Wt[b, a] = np.conj(Wt[a, b])
    agree += ((np.abs(Wt @ Wt - np.eye(16)).max() < 1e-9) == all(abs(flux(Wt, f) + 1) < 1e-9 for f in FACES)); tot += 1
inc = np.zeros((24, 32))
for fi, f in enumerate(FACES):
    for a, b in zip(f, f[1:] + f[:1]): inc[fi, EDGES.index((min(a, b), max(a, b)))] = 1 if a < b else -1
U = np.array([covariance(W, PERM[g]).real for g in range(n)])
check('A2 THEOREM forcing: B4+ is transitive on the 32 edges and 64 directed edges (covariant hops have equal moduli 1/2); '
      'a Hermitian equal-modulus hop has W^2 = 1 iff all 24 faces carry -1; the faces span the 17-dim cycle space, so the '
      'hop is unique up to gauge; it is covariant under all 384 elements, by signed permutations unique up to a phase',
      len(eorb) == 32 and len(dorb) == 64 and agree == tot and np.linalg.matrix_rank(inc) == 17 and len(FACES) == 24
      and all(np.allclose(U[g] @ W @ U[g].T, W) for g in range(n)), f'{agree}/{tot} random hops agree; cycle rank {np.linalg.matrix_rank(inc)}')
pi_ = np.abs(U).argmax(1); sg_ = np.take_along_axis(U, pi_[:, None, :], 1)[:, 0, :]          # U(g) e_x = sg_[g,x] e_pi_[g,x]
om = sg_[:, 0][None, :] * sg_[:, pi_[:, 0]] * sg_[:, 0][MUL]                          # omega(g,h) = U(g)U(h)U(gh)^-1
pairs = [(g, h) for g in PLUS for h in PLUS if MUL[g, h] == MUL[h, g]]
cU = np.array([om[g, h] / om[h, g] for g, h in pairs])
cS = np.array([(SPu[g] @ SPu[h] @ np.linalg.inv(SPu[h] @ SPu[g]))[0, 0].real for g, h in pairs])
Eh = [g for g in PLUS if g != E0 and (allR[g] == np.diag(np.diag(allR[g]))).all()]
eE = all(abs(om[g, h] / om[h, g] - (SPu[g] @ SPu[h] @ np.linalg.inv(SPu[h] @ SPu[g]))[0, 0]) < 1e-9 for g in Eh for h in Eh)
kl = [om[a, b] / om[b, a] for a, b in itertools.combinations(klein, 2)]
check('A3 THEOREM the forced class is neither trivial nor spin: the lifts of the 7 coordinate half-turns commute exactly as '
      'in Spin(4), but the corner Klein group acts linearly (commutators +1; spin -1)',
      eE and all(abs(k - 1) < 1e-12 for k in kl) and (cU < 0).sum() > 0 and np.abs(cU - cS).max() > 1,
      f'B4+ commuting pairs {len(pairs)}: forced -1 {(cU < 0).sum()}, spin -1 {(cS < 0).sum()}, differ {(np.abs(cU - cS) > 1e-9).sum()}')
# ---- light modes at K = 0 of D1 = 1 - Wo(K) We: Clifford, spin x taste
def Wo_of(K):
    M = np.zeros((16, 16), complex)
    for i in range(16):
        for mu in range(4):
            if C16[i][mu] == 1:
                j = i - (1 << mu); a = 0.5 * eta(C16[i], mu); M[i, j] += a * np.exp(1j * K[mu]); M[j, i] += a * np.exp(-1j * K[mu])
    return M
Gm = []
for mu in range(4):
    e = np.zeros(4); e[mu] = 1e-6; X = 2j * (Wo_of(e) - Wo_of(-e)) / 2e-6 @ W; Gm.append((X + X.conj().T) / 2)
G5L = Gm[0] @ Gm[1] @ Gm[2] @ Gm[3]
def joint(P1, P2):
    w, Vv = np.linalg.eigh(P1); Vp = Vv[:, w > 0]; w2, V2 = np.linalg.eigh(Vp.conj().T @ P2 @ Vp); return Vp @ V2[:, w2 > 0]
e1 = joint(G5, 1j * GAM[0] @ GAM[1])[:, 0]; Fb = joint(G5L, 1j * Gm[0] @ Gm[1])
SUBS = [s for k in range(5) for s in itertools.combinations(range(4), k)]
def mono(M, s):
    X = np.eye(M[0].shape[0], dtype=complex)
    for a in s: X = X @ M[a]
    return X
Phi = np.zeros((16, 16), complex)
for al in range(4):
    Eal = np.outer(np.eye(4)[al], e1.conj()); EG = sum(np.trace(mono(GAM, s).conj().T @ Eal) / 4 * mono(Gm, s) for s in SUBS)
    for a in range(4): Phi[:, 4 * al + a] = EG @ Fb[:, a]
V = Phi.conj().T
tau = []; fres = 0.0
for g in range(n):
    X = V @ U[g] @ V.conj().T; Y = np.kron(np.linalg.inv(SPu[g]), np.eye(4)) @ X; t_ = sum(Y[4 * a:4 * a + 4, 4 * a:4 * a + 4] for a in range(4)) / 4
    fres = max(fres, np.abs(np.kron(SPu[g], t_) - X).max()); tau.append(t_ / np.linalg.det(t_) ** 0.25)
tau = np.array(tau); T5 = (V @ (W @ G5L) @ V.conj().T)[:4, :4]
cliff = max(np.abs(Gm[a] @ Gm[b] + Gm[b] @ Gm[a] - 2 * (a == b) * np.eye(16)).max() for a in range(4) for b in range(4))
vec = max(np.abs(U[g] @ Gm[m] @ U[g].T - sum(allR[g][nu, m] * Gm[nu] for nu in range(4))).max() for g in range(n) for m in range(4))
kq = all(np.allclose(tau[a] @ tau[b], -tau[b] @ tau[a]) for a, b in itertools.combinations(klein, 2))
cp = len(commutant_basis([tau[g] for g in gens_of(PLUS)], 4)); cb = len(commutant_basis([tau[g] for g in gens_of(range(n))], 4))
t5ok = max(np.abs(tau[g] @ T5 - T5 @ tau[g]).max() for g in PLUS) < 1e-9 and max(np.abs(tau[g] @ T5 + T5 @ tau[g]).max() for g in range(n) if det[g] < 0) < 1e-9
check('A4 THEOREM the 16 light modes are spin x taste: Gamma_mu Clifford and a vector, U = S x tau exactly; tau lifts the '
      'corner Klein group to anticommuting matrices, so every taste space is even-dimensional: under B4+ the four tastes '
      'split into two inequivalent pairs T+, T- (taste sign t5, traceless), under B4 they are one irreducible quartet',
      cliff < 1e-9 and vec < 1e-12 and fres < 1e-9 and kq and cp == 2 and cb == 1 and t5ok and abs(np.trace(T5)) < 1e-9,
      f'Clifford {cliff:.0e}, factorisation {fres:.0e}; commutant B4+ {cp}, B4 {cb}')
def subgroup_classes(G):
    known = {}; reps = []
    def add(S):
        k = S.tobytes()
        if k in known: return
        idx = np.nonzero(S)[0]; cls = set()
        for g in G:
            T_ = np.zeros(n, bool); T_[CONJ[g, idx]] = True; cls.add(T_.tobytes())
        for c in cls: known[c] = len(reps)
        reps.append(S)
    for g in G: add(vclosure([g]))
    i = 0
    while i < len(reps):
        idx = np.nonzero(reps[i])[0]; gs = gens_of(idx.tolist()); seen = set(idx.tolist())
        for g in G:
            if g in seen: continue
            add(vclosure(gs + [g])); seen |= set(MUL[idx, g].tolist())
        i += 1
    return reps
def inv_counts(H):
    H = list(H); ch = np.array([np.trace(allR[g]) for g in H], float); ch2 = np.array([np.trace(allR[g] @ allR[g]) for g in H], float)
    ch4 = np.array([np.trace(np.linalg.matrix_power(allR[g], 4)) for g in H], float); cL = (ch ** 2 - ch2) / 2; cL2 = (ch2 ** 2 - ch4) / 2
    return tuple(int(round(np.mean(x))) for x in ((ch ** 2 + ch2) / 2, (ch ** 2 - ch2) / 2, (cL ** 2 + cL2) / 2))
def min_taste(gs):
    if not gs: return 1
    B = commutant_basis([tau[g] for g in gs], 4); X = sum((rng.normal() + 1j * rng.normal()) * b.reshape(4, 4) for b in B); X = X + X.conj().T
    ev = np.sort(np.linalg.eigvalsh(X)); mult = np.diff(np.r_[0, np.nonzero(np.diff(ev) > 1e-7)[0] + 1, 4]); return int(mult.min())
val = [len(subgroup_classes([g for g in range(n) if (allR[g] >= 0).all()])), len(subgroup_classes([g for g in range(n) if (allR[g] >= 0).all() and det[g] > 0]))]
summ = {}
for nm, G in (('B4+', PLUS), ('B4', list(range(n)))):
    out = []
    for S in subgroup_classes(G):
        H = np.nonzero(S)[0].tolist(); out.append((len(H), inv_counts(H), min_taste(gens_of(H))))
    full = max(out); prot = sorted((o[0], o[2]) for o in out if o[1][0] == 1 and o[1][2] <= full[1][2])
    one = [o for o in out if o[2] == 1]
    summ[nm] = (len(out), full, prot, max(o[0] for o in one), min(o[1][2] for o in one if o[1][0] == 1), all(o[1][0] > 1 or o[1][2] > full[1][2] for o in one))
check('A5 THEOREM all subgroup classes (78 of B4+, 193 of B4; the code finds 11 for S4 and 5 for A4): every class allowing a '
      'single light taste leaves a dimension-4 anisotropy (matter n_S = 2, or light n_F above the full group\'s); the classes '
      'keeping both forms are B4+ and its order-96 A4 x| E (not two-generated), with 2 tastes, and B4 (4), W(D4), A4-signed (2)',
      val == [11, 5] and summ['B4+'][0] == 78 and summ['B4'][0] == 193 and summ['B4+'][5] and summ['B4'][5]
      and summ['B4+'][2] == [(96, 2), (192, 2)] and summ['B4'][2] == [(192, 2), (192, 2), (384, 4)],
      f"largest single-taste class: B4+ order {summ['B4+'][3]} (n_F with n_S=1: {summ['B4+'][4]}), B4 order {summ['B4'][3]} (n_F {summ['B4'][4]})")
print(f'   [{time.time() - T0:.0f} s]')

print('== B. the forced lattice: two tilings, pi flux on every plaquette of Z^4')
errs = []
for _ in range(40):
    K = rng.uniform(-np.pi, np.pi, 4); Wo = Wo_of(K); ev = np.sort(np.linalg.eigvals(Wo @ W).real)
    errs.append(max(np.abs(Wo @ Wo - np.eye(16)).max(), np.abs(ev - np.cos(K).sum() / 4).max()))
z = {nm: [int(np.sum(np.abs(np.linalg.eigvals(f(K))) < 1e-9)) for K in (np.zeros(4), np.pi * np.ones(4))]
     for nm, f in (('D1', lambda K: np.eye(16) - Wo_of(K) @ W), ('We+Wo', lambda K: W + Wo_of(K)), ('[Wo,We]', lambda K: Wo_of(K) @ W - W @ Wo_of(K)))}
th = [np.abs(np.angle(np.linalg.eigvals(Wo_of(0.01 * d) @ W))).max() / 0.01 for d in (np.eye(4)[0], np.eye(4)[3], np.ones(4) / 2)]
check('B1 THEOREM Wo^2 = We^2 = 1 and Re eig(Wo We) = S(K) = sum_mu cos K_mu / 4 on all 16 bands (every plaquette pi): '
      'D1 = 1 - Wo We vanishes only at K = 0, where all 16 modes have theta = |K|/2: four Dirac tastes; We + Wo has its 16 '
      'zeros at K = pi(1,1,1,1); [Wo, We] at both', max(errs) < 1e-12 and z == {'D1': [16, 0], 'We+Wo': [0, 16], '[Wo,We]': [16, 16]}
      and max(abs(x - 0.5) for x in th) < 1e-4, f'S(K) residual {max(errs):.0e}; theta/|K| axis, tick, diagonal ' + ' '.join(f'{x:.5f}' for x in th))
TdK = covariance(W, [15 - i for i in range(16)]).real
K = rng.uniform(-np.pi, np.pi, 4); Sh = np.zeros((16, 16), complex)
for i in range(16): Sh[15 - i, i] = np.exp(-1j * np.dot(K, C16[i]))
TS = np.diag(np.diag(TdK @ np.eye(16)[[15 - i for i in range(16)]].T)) @ Sh; WoK = Wo_of(K); A0 = TdK.T @ W
sw = max(np.abs(TS @ W @ TS.conj().T - WoK).max(), np.abs(TS @ WoK @ TS.conj().T - W).max())
AK = TS.conj().T @ WoK; D1K = np.eye(16) - WoK @ W
check('B2 THEOREM the diagonal shift by (1,1,1,1), with KS signs, swaps the two tilings exactly; A = T^-1 Wo commutes with D1 '
      'and acts on the light modes as a pure taste matrix', sw < 1e-12 and np.abs(AK @ D1K @ np.linalg.inv(AK) - D1K).max() < 1e-12
      and max(np.abs(A0 @ g - g @ A0).max() for g in Gm) < 1e-12, f'swap {sw:.0e}')
J = U[INVI]; s4 = J @ W
Ws = [np.zeros((16, 16)) for _ in range(4)]
for (i, j) in EDGES: mu = int(np.log2(j - i)); Ws[mu][i, j] = Ws[mu][j, i] = eta(C16[i], mu)
eps = np.diag([(-1.0) ** int(C16[i].sum()) for i in range(16)])
Jl = V @ J @ V.conj().T; s4l = V @ s4 @ V.conj().T
Mm = 0.4 * (np.eye(16) - s4) / 2; sv0 = np.linalg.svd(np.eye(16) - W @ W + Mm, compute_uv=False)
lt = [np.sort(np.linalg.svd(np.eye(16) - Wo_of(0.01 * d) @ W + Mm, compute_uv=False))[:8] / 0.01 for d in (np.eye(4)[0], np.eye(4)[3], np.ones(4) / 2, np.array([1, 1, 0, 0]) / np.sqrt(2))]
check('B3 THEOREM copy sign s4 = J W, J the block inversion (= eps R1R2R3R4): a Hermitian involution invariant under all of '
      'B4+ and odd under every reflection; on the light modes J = gamma5 x 1 and s4 = 1 x t5; the mass m(1 - s4)/2 leaves '
      'exactly two light Dirac tastes (T+) with one common cone, speed |K|/2 on axes, tick and diagonals',
      np.allclose(J @ W, W @ J) and np.allclose(s4, s4.T) and np.allclose(s4 @ s4, np.eye(16)) and min(np.abs(Ws[0] @ Ws[1] @ Ws[2] @ Ws[3] - c * eps @ J).max() for c in (1, -1)) < 1e-12
      and max(np.abs(U[g] @ s4 - s4 @ U[g]).max() for g in PLUS) < 1e-12 and max(np.abs(U[g] @ s4 + s4 @ U[g]).max() for g in range(n) if det[g] < 0) < 1e-12
      and min(np.abs(Jl - c * np.kron(G5, np.eye(4))).max() for c in (1, -1)) < 1e-9 and min(np.abs(s4l - c * np.kron(np.eye(4), T5)).max() for c in (1, -1)) < 1e-9
      and int(np.sum(sv0 < 1e-10)) == 8 and max(np.abs(l - 0.5).max() for l in lt) < 1e-3,
      f"K=0 zero modes {int(np.sum(sv0 < 1e-10))}, heavy {sv0.max():.2f}; light speeds " + ' '.join(f'{l.mean():.5f}' for l in lt))
def avg(Ms, G):
    out = np.zeros_like(Ms)
    for g in G: X = np.einsum('nm,snab->smab', allR[g].astype(float), Ms); out += np.matmul(np.matmul(U[g].T, X), U[g])
    return out / len(G)
def span_rows(arrs):
    A = np.array([a.ravel() for a in arrs]); _, s_, vh = np.linalg.svd(A, full_matrices=False); return vh[s_ > 1e-8 * s_[0]]
def null_in(B, cons):
    Am = np.vstack([np.array([f(b.reshape(4, 16, 16)).ravel() for b in B]).T for f in cons]); _, s2, vh2 = np.linalg.svd(Am, full_matrices=False)
    return vh2[int(np.sum(s2 > 1e-8)):].conj() @ B
def inter(A_, B_): return np.linalg.matrix_rank(A_, 1e-8) + np.linalg.matrix_rank(B_, 1e-8) - np.linalg.matrix_rank(np.vstack([A_, B_]), 1e-8)
gw = lambda M: np.einsum('ab,mbc->mac', W, M) + np.einsum('mab,bc->mac', M, W)
td = lambda M: np.einsum('ab,mbc->mac', A0, M) - np.einsum('mab,bc->mac', M, A0)
cc = lambda M: np.transpose(M, (0, 2, 1)) + np.einsum('ab,mbc,cd->mad', W, M, W)
lor = span_rows([np.array([Gm[m] @ c.reshape(16, 16) for m in range(4)]) for c in commutant_basis(Gm, 16)] +
                [np.array([Gm[m] @ G5L @ c.reshape(16, 16) for m in range(4)]) for c in commutant_basis(Gm, 16)])
Pp = (np.eye(16) + W @ G5L) / 2; kin = {}
for nm, G, ns in (('B4+', PLUS, 14), ('B4', list(range(n)), 8)):
    B0 = span_rows(avg(rng.normal(size=(ns, 4, 16, 16)) + 1j * rng.normal(size=(ns, 4, 16, 16)), G)); B1 = null_in(B0, [gw]); B3 = null_in(null_in(B1, [td]), [cc])
    Bp = span_rows([np.einsum('ab,mbc,cd->mad', Pp, b.reshape(4, 16, 16), Pp) for b in B0]); Lp = span_rows([np.einsum('ab,mbc,cd->mad', Pp, l.reshape(4, 16, 16), Pp) for l in lor])
    kin[nm] = tuple(int(x) for x in (len(B0), inter(B0, lor), len(B1), inter(B1, lor), len(B3), inter(B3, lor), len(Bp), inter(Bp, Lp)))
check('B4 THEOREM dimension-4 kinetic terms on the 16 light modes: B4+ allows 8, of which 4 are not Lorentz invariant (they '
      'mix T+ with T-); the exact chirality Wo removes those 4, leaving only Lorentz-invariant vector and axial terms per pair; '
      'on the light pair T+ alone B4+ allows only its Lorentz-invariant pair: every multiplet\'s cone is protected',
      kin['B4+'][:4] == (8, 4, 4, 4) and kin['B4+'][4] == kin['B4+'][5] and kin['B4+'][6] == kin['B4+'][7] == 2 and kin['B4'][:4] == (4, 2, 2, 2),
      'B4+ [all, LI, +GW, LI, +T_d+C, LI, T+, LI] ' + str(list(kin['B4+'])) + '; B4 ' + str(list(kin['B4'])))
def Wo0_of(K):        # the other real relative gauge: pi on block faces, 0 on mixed plaquettes
    M = np.zeros((16, 16), complex)
    for i in range(16):
        for mu in range(4):
            if C16[i][mu] == 1:
                j = i - (1 << mu); a = 0.5 * eta(C16[i], mu) * (-1) ** int(C16[i].sum() - 1); M[i, j] += a * np.exp(1j * K[mu]); M[j, i] += a * np.exp(-1j * K[mu])
    return M
gg = 2 * np.pi * np.arange(8) / 8; zc = {'pi': 0, 'zero': 0}
for Kv in itertools.product(gg, repeat=4):
    Kv = np.array(Kv)
    zc['pi'] += int(np.abs(1 - np.linalg.eigvals(Wo_of(Kv) @ W)).min() < 1e-9); zc['zero'] += int(np.abs(1 - np.linalg.eigvals(Wo0_of(Kv) @ W)).min() < 1e-9)
check('B5 FINITE the relative gauge of the two tilings is a supplied choice; of the two real ones, pi on every plaquette '
      'gives the single isolated cone point K = 0, while 0 on the mixed plaquettes leaves zero modes on extended sets of the zone',
      zc['pi'] == 1 and zc['zero'] > 100 and np.abs(Wo0_of(K) @ Wo0_of(K) - np.eye(16)).max() < 1e-12, f"zero points on an 8^4 grid: pi {zc['pi']}, mixed-0 {zc['zero']}")
print(f'   [{time.time() - T0:.0f} s]')

print('== C. chirality with links; transfer positivity')
Ls = 4; NS = Ls ** 4
coords = np.array(list(itertools.product(range(Ls), repeat=4)))[:, ::-1]
def sidx(y): y = np.asarray(y) % Ls; return int(y[0] + Ls * y[1] + Ls * Ls * y[2] + Ls ** 3 * y[3])
nbr = np.array([[sidx(y + np.eye(4, dtype=int)[mu]) for mu in range(4)] for y in coords])
etas = np.array([[(-1) ** int(y[:mu].sum()) for mu in range(4)] for y in coords])
def blocksign(Ul, parity):
    H = np.zeros((NS, NS), complex)
    for i, y in enumerate(coords):
        for mu in range(4):
            if y[mu] % 2 == parity: a = 0.5 * etas[i, mu] * Ul[mu][i]; j = nbr[i, mu]; H[j, i] += a; H[i, j] += np.conj(a)
    out = np.zeros_like(H); blocks = {}
    for i, y in enumerate(coords): blocks.setdefault(tuple(((y - parity) % Ls) // 2), []).append(i)
    gap = 9.0
    for idx in blocks.values():
        w, v = np.linalg.eigh(H[np.ix_(idx, idx)]); gap = min(gap, np.abs(w).min()); out[np.ix_(idx, idx)] = (v * np.sign(w)) @ v.conj().T
    return out, gap
def thooft(n01, n23):
    Uu = np.ones((4, NS), complex)
    for (a_, b_, nn) in ((0, 1, n01), (2, 3, n23)):
        Uu[b_] *= np.exp(2j * np.pi * nn * coords[:, a_] / Ls ** 2); ed = coords[:, a_] == Ls - 1; Uu[a_][ed] *= np.exp(-2j * np.pi * nn * coords[ed, b_] / Ls)
    return Uu
cres = []
for Ul in (np.exp(1j * rng.normal(0, 0.3, (4, NS))), thooft(1, 1)):
    We_, ge = blocksign(Ul, 0); Wo_, go = blocksign(Ul, 1); Dl = np.eye(NS) - Wo_ @ We_
    w, vv = np.linalg.eig(Wo_ @ We_); idx = np.argsort(np.abs(1 - w)); nz = int(np.sum(np.abs(1 - w) < 1e-9))
    chir = np.linalg.eigvalsh((lambda Q: Q.conj().T @ Wo_ @ Q)(np.linalg.qr(vv[:, idx[:max(nz, 1)]])[0])) if nz else np.array([])
    cres.append((min(ge, go), np.abs(Wo_ @ Dl + Dl @ Wo_ - Dl @ Wo_ @ Dl).max(), (np.trace(Wo_) + np.trace(We_)).real / 2, nz, np.round(chir, 6)))
check('C1 THEOREM D1 = 1 - Wo We with links (block sign functions) obeys {Wo, D1} = D1 Wo D1 exactly, but its index '
      '(Tr Wo + Tr We)/2 vanishes in every admissible background (bipartite blocks): in the Q = 1 flux the 4 exact zero '
      'modes have Wo-chirality (-,-,+,+); on the light modes Wo = gamma5 x t5: the exact chirality is taste non-singlet',
      all(c[1] < 1e-12 and abs(c[2]) < 1e-9 and c[0] > 0.3 for c in cres) and cres[1][3] == 4 and list(cres[1][4]) == [-1, -1, 1, 1] and cres[0][3] == 0,
      f'block gaps {cres[0][0]:.2f}, {cres[1][0]:.2f}; GW residual {max(c[1] for c in cres):.0e}; random links: {cres[0][3]} zero modes')
C8 = np.array([[(i >> m) & 1 for m in range(3)] for i in range(8)]); Tt = 24; N = 8 * Tt
def ops(P, apbc):
    We = np.zeros((N, N), complex); Wo = np.zeros((N, N), complex); Ae = np.zeros((N, N), complex); Ao = np.zeros((N, N), complex)
    def I(t, i): return 8 * (t % Tt) + i
    for t in range(Tt):
        for i in range(8):
            x = C8[i]
            for j in range(3):
                a = 0.5 * eta(x, j)
                if x[j] == 0: k = i + (1 << j); We[I(t, k), I(t, i)] += a; We[I(t, i), I(t, k)] += a; Ae[I(t, i), I(t, k)] += a; Ae[I(t, k), I(t, i)] -= a
                else:
                    k = i - (1 << j); ph = np.exp(1j * P[j]); Wo[I(t, k), I(t, i)] += a * ph; Wo[I(t, i), I(t, k)] += a * np.conj(ph)
                    Ao[I(t, i), I(t, k)] += a * ph; Ao[I(t, k), I(t, i)] -= a * np.conj(ph)
            a = 0.5 * eta(np.r_[x, 0], 3) * (apbc if t == Tt - 1 else 1); Mw, Ma = (We, Ae) if t % 2 == 0 else (Wo, Ao)
            Mw[I(t + 1, i), I(t, i)] += a; Mw[I(t, i), I(t + 1, i)] += a; Ma[I(t, i), I(t + 1, i)] += a; Ma[I(t + 1, i), I(t, i)] -= a
    return We, Wo, Ae, Ao
def reflection(Ws_, theta):
    Pm = np.zeros((N, N))
    for t in range(Tt):
        for i in range(8): Pm[8 * (theta(t) % Tt) + i, 8 * t + i] = 1
    Hs = sum(np.abs(w) for w in Ws_); d = np.zeros(N); d[0] = 1; q = [0]; Wp = [Pm @ w @ Pm.T for w in Ws_]
    while q:
        x = q.pop()
        for y in np.nonzero(Hs[x] > 1e-12)[0]:
            if d[y] == 0:
                w, wp = [(w, wp) for w, wp in zip(Ws_, Wp) if abs(w[x, y]) > 1e-12][0]; d[y] = d[x] * np.real(w[x, y] / wp[x, y]); q.append(y)
    return np.diag(d) @ Pm
EPS = np.diag([(-1.0) ** (int(C8[i].sum()) + t) for t in range(Tt) for i in range(8)])
We0, Wo0, Ae0, Ao0 = ops(np.zeros(3), -1)
blk = np.zeros((N, N), complex)                       # the copy sign embedded on the even time blocks
for mb in range(Tt // 2):
    for a in range(16):
        for b in range(16):
            if s4[a, b] != 0:
                xa, xb = C16[a], C16[b]; blk[8 * (2 * mb + xa[3]) + xa[0] + 2 * xa[1] + 4 * xa[2], 8 * (2 * mb + xb[3]) + xb[0] + 2 * xb[1] + 4 * xb[2]] = s4[a, b]
rp = {'KS': [], 'D1': []}; s4odd = []; m = 0.2
for P in (np.zeros(3), np.array([0.5, 0.2, -0.3]), np.array([np.pi, 0.4, 0.0])):
    We_, Wo_, Ae_, Ao_ = ops(P, -1)
    for nm, D, Ws_, plane in (('KS', Ae_ + Ao_ + m * np.eye(N), [Ae0, Ao0], 0), ('KS', Ae_ + Ao_ + m * np.eye(N), [Ae0, Ao0], 1),
                              ('D1', (1 - m / 2) * (np.eye(N) - Wo_ @ We_) + m * np.eye(N), [We0, Wo0], 0), ('D1', (1 - m / 2) * (np.eye(N) - Wo_ @ We_) + m * np.eye(N), [We0, Wo0], 1)):
        th_ = (lambda t: 1 - t) if plane == 0 else (lambda t: 3 - t); Rs = reflection(Ws_, th_)
        Rc = EPS @ Rs if nm == 'KS' else (Wo_ if plane == 0 else We_) @ Rs
        inv_ = np.abs(Rc @ D.conj().T @ Rc - D).max(); G_ = np.linalg.inv(D); S_ = [8 * ((1 + plane + k) % Tt) + i for k in range(6) for i in range(8)]
        Mx = -(G_ @ Rc).T[np.ix_(S_, S_)]; ev = np.linalg.eigvalsh((Mx + Mx.conj().T) / 2) / np.abs(Mx).max()
        rp[nm].append((inv_, np.abs(Mx - Mx.conj().T).max(), ev.min(), ev.max()))
        if nm == 'KS':
            Dm = D + 0.5 * (np.eye(N) - blk) / 2
            s4odd.append((np.abs(Rc @ blk @ Rc - blk).max(), np.abs(Rc @ blk @ Rc + blk).max(), np.abs(Rc @ Dm.conj().T @ Rc - Dm).max()))
G_ = np.linalg.inv((np.eye(N) - (lambda o: o[1] @ o[0])(ops(np.array([0.6, -0.4, 0.9]), -1))) + 0.0 * np.eye(N) + 1e-3 * np.eye(N))
cosh_pred = np.exp(-np.arccosh(4 - np.cos([0.6, -0.4, 0.9]).sum()))
dec = [np.linalg.norm(G_[16 * k:16 * k + 8, :8]) for k in range(1, 5)]; rat = np.array(dec[1:]) / np.array(dec[:-1])
check('C2 FINITE OS reflection (antiperiodic time, planes through even and odd block middles): the Kogut-Susskind action '
      'A_e + A_o + m (Theta psi = eps R psibar) is reflection positive, the Margolus product D1 is not (indefinite for both '
      'natural reflections), and the reflection maps the copy sign to neither +s4 nor -s4, so the two-taste action loses this OS '
      'symmetry; '
      'D1\'s block transfer eigenvalue is real, exp(-E) with cosh E = 4 - sum_j cos P_j',
      all(r[0] < 1e-12 and r[1] < 1e-12 and r[3] < 1e-12 for r in rp['KS']) and all(r[0] < 1e-12 and r[2] < -0.5 and r[3] > 0.5 for r in rp['D1'])
      and min(min(x) for x in s4odd) > 0.1 and np.abs(rat - cosh_pred).max() < 2e-2,
      f"KS max eig of M {max(r[3] for r in rp['KS']):.0e}; D1 eig ranges [{max(r[2] for r in rp['D1']):+.2f}, {min(r[3] for r in rp['D1']):+.2f}]; "
      f"copy-sign OS residual {min(x[2] for x in s4odd):.2f}; decay {rat.mean():.4f} vs {cosh_pred:.4f}")
print('supplied: Z^4 with two 2^4 tilings, one mode per site, nearest-neighbour Hermitian W^2 = 1 hop, B4/B4+ acting by monomial maps,')
print('  the operators D1, We+Wo, [Wo,We], KS, the copy-sign mass and U(1) links. forced: pi flux, its projective class (not spin),')
print('  even taste multiplets (4 = 2+2 under B4+), single taste only below every dimension-4-protecting subgroup, zero GW index.')
print(f'elapsed {time.time() - T0:.0f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')

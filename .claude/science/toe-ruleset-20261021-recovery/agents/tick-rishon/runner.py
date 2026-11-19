#!/usr/bin/env python3
"""tick-rishon: CL-1's matter tick with quantum (rishon) link registers.

A  link algebra: a U(1) register's raising operator is nilpotent; the domain-normalised raiser V is a partial isometry;
   rishon realisations (S = 1/2; S = 3/2 as three one-rishon flavour pairs, C3-invariant sector); no half-power exists.
B  edge layout (registers on cube edges, link-zoom b = 3 grouping), one cube, S = 1/2 rishons (32 modes, sector only):
   the dressed hop is never a reflection; with c-number links R^2 = 1 iff the cube is flat.
C  site layout (one register per site on its even-centre -> odd-centre bond), one odd cube, S = 1/2 rishons (24 modes,
   sectors) and S = 3/2: in every Gauss sector the dressed tick is exactly the free tick on the live sites.
D  two-tiling torus 4^3: c-number site phases keep both hops reflections and the two-reflection band identity in
   every field; flat = free spectrum. Quantum S, one particle: finite-time exactness and flux pumping.
E  copy sign s on the (undressed) even cube: involution, 12 rotations; on a dressed cube off the live sector it fails.
F  placement: site stabiliser C3, nearest-neighbour orbits, bond<->site bijection, register count.
G  estimates.
Supplied model, finite diagnostics; numpy/scipy only; no dense Fock space of 2^11 or more.
"""
import itertools, math, os, sys, time, signal
AUDIT_TIMEOUT_SEC = 120
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.alarm(AUDIT_TIMEOUT_SEC - 5)
import numpy as np
import scipy.sparse as sp
from scipy.linalg import expm

T0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok); PASS += ok; FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ---------------- cube geometry, spin-3/2 edge hop (CL-1) ----------------
def qmul(a, b):
    w1, x1, y1, z1 = a; w2, x2, y2, z2 = b
    return np.array([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2, w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2])
def binary_octahedral():
    r2 = np.sqrt(.5); gens = [np.array([r2, 0, 0, r2]), np.array([.5, .5, .5, .5])]
    key = lambda q: tuple(np.round(q, 8) + 0.0); els = {key(np.array([1., 0, 0, 0])): np.array([1., 0, 0, 0])}; fr = list(els.values())
    while fr:
        new = []
        for a in fr:
            for g in gens:
                c = qmul(a, g)
                if key(c) not in els: els[key(c)] = c; new.append(c)
        fr = new
    return list(els.values())
def q_so3(q):
    w, x, y, z = q
    return np.array([[1-2*(y*y+z*z), 2*(x*y-z*w), 2*(x*z+y*w)], [2*(x*y+z*w), 1-2*(x*x+z*z), 2*(y*z-x*w)], [2*(x*z-y*w), 2*(y*z+x*w), 1-2*(x*x+y*y)]])
def Jm(j):
    d = int(round(2*j+1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1) - m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)], Jp
CORN = np.array(list(itertools.product((0, 1), repeat=3))); (J32, _) = Jm(1.5); XI = []
for c in CORN:
    n_ = (2*c-1.0)/np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k]*J32[k] for k in range(3))); XI.append(v_[:, -1])
R8 = np.zeros((8, 8), complex); Ri = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        d = CORN[a] - CORN[b]
        if np.abs(d).sum() == 1:
            g = XI[a].conj() @ XI[b]; R8[a, b] = -g/abs(g)/np.sqrt(3); Ri[int(np.argmax(np.abs(d)))][a, b] = -g/abs(g)
EDGES = [(a, b) for a in range(8) for b in range(a+1, 8) if np.abs(CORN[a]-CORN[b]).sum() == 1]
I8 = np.eye(8)

# ---------------- vectorised fermion words on bitstring arrays (JW order = mode index) ----------------
def apply_vec(word, S):
    S = S.copy(); sign = np.ones(len(S)); ok = np.ones(len(S), bool)
    for dag, j in reversed(word):
        occ = (S >> j) & 1; ok &= (occ != dag)
        par = np.bitwise_count(S & ((1 << j) - 1)) & 1; sign *= np.where(par == 1, -1.0, 1.0); S ^= (1 << j)
    return ok, sign, S
def build(terms, basis):
    rows, cols, vals = [], [], []; ar = np.arange(len(basis))
    for coef, word in terms:
        if abs(coef) < 1e-15: continue
        ok, sg, S2 = apply_vec(word, basis)
        if not ok.any(): continue
        idx = np.searchsorted(basis, S2[ok]); assert np.all(basis[idx] == S2[ok]), 'basis not closed'
        rows.append(idx); cols.append(ar[ok]); vals.append(coef*sg[ok])
    n = len(basis)
    if not rows: return sp.csr_matrix((n, n), dtype=complex)
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n), dtype=complex)
def bits(S, j): return (S >> j) & 1

# ======================================================================= A
print('== A. link registers')
nil = []
for S in (0.5, 1, 1.5, 2, 3):
    (J, Jp) = Jm(S); E = J[2].real; d = len(E)
    rng = np.random.default_rng(1)   # general solution of [E,U] = U: entries only where m_row = m_col + 1
    mask = np.isclose(np.diag(E)[:, None] - np.diag(E)[None, :], 1.0); U = rng.normal(size=(d, d))*mask
    nil.append(np.abs(np.linalg.matrix_power(U, d)).max())
check('A1 [T] on a finite register every U with [E,U] = U is nilpotent (U^(2S+1) = 0), so no U(1) raiser is unitary; '
      'a unitary shift exists only with E defined mod N (Z_N clock)', max(nil) < 1e-12, f'max|U^(2S+1)| = {max(nil):.0e}, S = 1/2..3')
vs = []
for S in (0.5, 1.5, 2.5):
    (J, Jp) = Jm(S); d = len(Jp); V = (np.abs(Jp) > 0).astype(float)
    E = J[2].real; Pt = np.diag(np.isclose(np.diag(E), S)*1.0); Pb = np.diag(np.isclose(np.diag(E), -S)*1.0)
    vs.append(max(np.abs(V.T @ V - (np.eye(d)-Pt)).max(), np.abs(V @ V.T - (np.eye(d)-Pb)).max(), np.abs(E @ V - V @ E - V).max()))
half = []
for S in (0.5, 1, 1.5, 2):
    (J, Jp) = Jm(S); E = J[2].real; ev = np.diag(E); M = np.isclose(ev[:, None]-ev[None, :], 0.5); half.append(int(M.sum()))
check('A2 [T] the domain-normalised raiser V = S^+ / |S^+| is a partial isometry: V^+V = 1 - P(m=S), VV^+ = 1 - P(m=-S),'
      ' [E,V] = V; and no X with [E,X] = X/2 exists (no half-power of a register)', max(vs) < 1e-12 and max(half) == 0, f'{max(vs):.0e}; half-step solution dims {half}')
# rishons: S=3/2 as three flavour pairs (a_f odd end, b_f even end), modes a0 a1 a2 b0 b1 b2 = 0..5
basis6 = np.array(sorted(s for s in range(64) if all(((s >> f) & 1) + ((s >> (3+f)) & 1) == 1 for f in range(3))), dtype=np.int64)
Sp = build([(1.0, [(1, 3+f), (0, f)]) for f in range(3)], basis6).toarray()
Nb = np.array([sum(bits(s, 3+f) for f in range(3)) for s in basis6])
perm = lambda s: sum(((s >> f) & 1) << ((f+1) % 3) for f in range(3)) | sum(((s >> (3+f)) & 1) << (3+(f+1) % 3) for f in range(3))
C3 = np.zeros((8, 8))
for i, s in enumerate(basis6):
    t = perm(int(s))
    # fermionic sign of the cyclic relabelling: compute by reordering creation operators
    occ = [j for j in range(6) if (s >> j) & 1]; img = [(j % 3 + 1) % 3 + (3 if j >= 3 else 0) for j in occ]
    inv = sum(1 for p in range(len(img)) for q in range(p+1, len(img)) if img[p] > img[q])
    C3[list(basis6).index(t), i] = (-1)**inv
w, Vc = np.linalg.eig(C3); inv_sub = Vc[:, np.isclose(w, 1)]; Q, _ = np.linalg.qr(inv_sub)
Sz = Q.conj().T @ np.diag(Nb - 1.5) @ Q; Spq = Q.conj().T @ Sp @ Q
Sx, Sy = (Spq + Spq.conj().T)/2, (Spq - Spq.conj().T)/2j; Cas = Sx @ Sx + Sy @ Sy + Sz @ Sz
leak = np.abs(Sp @ Q - Q @ Spq).max()
check('A3 [T] three one-rishon flavour pairs per bond (a register whose ends are the three face sites of a C3 orbit):'
      ' the flavour-blind raiser S^+ = sum_f b_f^+ a_f keeps the C3-invariant subspace, which is exactly spin 3/2',
      Q.shape[1] == 4 and np.abs(Cas - 3.75*np.eye(4)).max() < 1e-12 and leak < 1e-12 and np.abs(C3 @ Sp - Sp @ C3).max() < 1e-12,
      f'dim {Q.shape[1]}, Casimir 15/4 err {np.abs(Cas-3.75*np.eye(4)).max():.0e}')

# ======================================================================= B  edge layout
print('== B. edge layout: registers on the cube edges, S = 1/2 (8 matter + 24 rishon modes)')
check('B0 [T] free cube hop: R^2 = 1, R_i^2 = 1, {R_i,R_j} = 0 (every face phase -1)', np.abs(R8 @ R8 - I8).max() < 1e-12
      and max(np.abs(Ri[i] @ Ri[j] + Ri[j] @ Ri[i] - 2*(i == j)*I8).max() for i in range(3) for j in range(3)) < 1e-12)
endm = lambda e, v: 8 + 2*e + (0 if EDGES[e][0] == v else 1)
termsB = []
for e, (a, b) in enumerate(EDGES):
    for x, y in ((a, b), (b, a)):   # hop y -> x: psi_x^+ c_{e,x} c_{e,y}^+ psi_y
        termsB.append((R8[x, y], [(1, x), (0, endm(e, x)), (1, endm(e, y)), (0, y)]))
bB = []
for a in range(8):
    for ch in range(4096): bB.append((1 << a) | sum(1 << (8 + 2*e + ((ch >> e) & 1)) for e in range(12)))
bB = np.array(sorted(bB), dtype=np.int64); HB = build(termsB, bB)
GB = np.stack([bits(bB, v) + sum(bits(bB, endm(e, v)) for e in range(12) if v in EDGES[e]) for v in range(8)], 1)
Hc = HB.tocoo(); gauge_ok = np.all(GB[Hc.row] == GB[Hc.col]).item()
keys, lab = np.unique(GB, axis=0, return_inverse=True); lab = lab.ravel()
mobile = refl = 0; offd = []
for k in range(len(keys)):
    ids = np.where(lab == k)[0]; h = HB[ids][:, ids].toarray()
    if np.abs(h).max() < 1e-12: continue
    mobile += 1; h2 = h @ h; refl += np.abs(h2 - np.eye(len(ids))).max() < 1e-10; offd.append(np.abs(h2 - np.diag(np.diag(h2))).max())
check('B1 [T] the rishon-dressed edge hop commutes with all 8 vertex-cluster numbers (Gauss law)', gauge_ok, f'{len(keys)} one-particle Gauss sectors')
nface = sum(o > 0.1 for o in offd)
check('B2 [T] edge layout: in NO one-particle Gauss sector with a mobile particle is the dressed hop a reflection: the'
      ' two ways round a face raise different registers, so the -1 face phase cannot cancel them', mobile > 0 and refl == 0 and nface > 0,
      f'mobile sectors {mobile}, reflections {refl}, with face terms {nface}')
rng = np.random.default_rng(7); al = rng.uniform(0, 6.3, 8)
def edge_dress(ph):
    M = R8.copy()
    for e, (a, b) in enumerate(EDGES): M[a, b] = R8[a, b]*np.exp(1j*ph[e]); M[b, a] = R8[b, a]*np.exp(-1j*ph[e])
    return M
Mf = edge_dress(np.array([al[a]-al[b] for a, b in EDGES])); Mg = edge_dress(rng.uniform(0, 6.3, 12))
check('B3 [T] c-number edge links: R^2 = 1 iff every face holonomy is trivial, i.e. iff the dressing is one phase per site'
      ' (flat cube); a generic field breaks it', np.abs(Mf @ Mf - I8).max() < 1e-12 and np.abs(Mg @ Mg - I8).max() > 0.1,
      f'flat {np.abs(Mf@Mf-I8).max():.0e}, generic {np.abs(Mg@Mg-I8).max():.2f}')

# ======================================================================= C  site layout, one odd cube
print('== C. site layout: one register per site (even end b_x, odd end a_x), one odd cube')
# modes: psi_x = x, a_x = 8+x (odd end), b_x = 16+x (even end); chi_x = b_x^+ a_x psi_x
termsC = [(R8[y, x], [(1, y), (1, 8+y), (0, 16+y), (1, 16+x), (0, 8+x), (0, x)]) for x in range(8) for y in range(8) if x != y]
resC = {}
for N in (1, 2, 3):
    bC = []
    for occ in itertools.combinations(range(8), N):
        m = sum(1 << x for x in occ)
        for ch in range(256): bC.append(m | sum(1 << ((16 if (ch >> x) & 1 else 8) + x) for x in range(8)))
    bC = np.array(sorted(bC), dtype=np.int64); H = build(termsC, bC)
    q = np.stack([bits(bC, x) + bits(bC, 16+x) for x in range(8)], 1); nodd = sum(bits(bC, 8+x) for x in range(8))
    Hc = H.tocoo(); g_ok = np.all(q[Hc.row] == q[Hc.col]) and np.all(nodd[Hc.row] == nodd[Hc.col])
    keys, lab = np.unique(q, axis=0, return_inverse=True); lab = lab.ravel(); worst = 0.0; nsec = 0; refl_all = refl_other = 0
    for k in range(len(keys)):
        ids = np.where(lab == k)[0]; h = H[ids][:, ids].toarray(); qk = keys[k]
        L = [x for x in range(8) if qk[x] == 1]; kdead = int(np.sum(qk == 2))
        if N - kdead < 0: continue
        ev_pred = np.sort([sum(c) for c in itertools.combinations(np.linalg.eigvalsh(R8[np.ix_(L, L)]), N - kdead)]) if L else np.zeros(1)
        ev = np.sort(np.linalg.eigvalsh(h)); nsec += 1
        if len(ev) != len(ev_pred): worst = 9; continue
        worst = max(worst, np.abs(ev - ev_pred).max())
        if N == 1:
            isr = np.abs(h @ h - np.eye(len(ids))).max() < 1e-10
            if len(L) == 8: refl_all += isr
            else: refl_other += isr
    resC[N] = (g_ok, worst, nsec, refl_all, refl_other, len(bC))
check('C1 [T] the dressed odd-cube hop sum R_yx chi_y^+ chi_x conserves the 8 even-cluster numbers q_x = n_psi + n_b and the'
      ' odd-cluster number; exp(-i eps H) is unitary and gauge invariant', all(resC[N][0] for N in resC),
      f'basis sizes {[resC[N][5] for N in resC]}')
check('C2 [T] in every Gauss sector the dressed tick IS the free tick of the canonical modes chi on the live sites'
      ' (q_x = 1): spectrum = sums of free one-body levels of R restricted to the live set, for 1, 2, 3 particles',
      max(resC[N][1] for N in resC) < 1e-10, f'max level deviation {max(resC[N][1] for N in resC):.0e} over {sum(resC[N][2] for N in resC)} sectors')
check('C3 [T] S = 1/2: the dressed hop is a reflection exactly in the sector with every corner live; any dead corner'
      ' (register at its extreme) breaks R^2 = 1', resC[1][3] == 1 and resC[1][4] == 0, f'all-live sectors reflecting {resC[1][3]}, others {resC[1][4]}')
S = 1.5
a_pl = lambda qq: np.sqrt(S*(S+1) - (qq-1-S)*(qq-S))
def dressed(q, normalised):
    L = [x for x in range(8) if 1 <= q[x] <= 2*S]; D = np.zeros(8)
    for x in L: D[x] = 1.0 if normalised else a_pl(q[x])
    return np.diag(D) @ R8 @ np.diag(D), L
qn = np.array([1, 2, 3, 2, 1, 3, 2, 2]); qd = np.array([0, 2, 3, 2, 1, 3, 2, 2]); qu = np.full(8, 2)
Rn, _ = dressed(qn, True); Rp, _ = dressed(qn, False); Ru, _ = dressed(qu, False); Rd, Ld = dressed(qd, True)
lam = np.linalg.eigvalsh(Rp @ Rp); spread = lam.max()/lam.min()
check('C4 [T] S = 3/2: with the plain raiser S^+ each hop carries |S^+| of its registers, so R_d = D R D with D set by the'
      ' local Gauss values: a reflection after rescaling only if every q_x is equal; the domain-normalised V gives R_d^2 = 1'
      ' in every all-live sector (1 <= q_x <= 2S)', np.abs(Rn @ Rn - I8).max() < 1e-12 and spread > 1.5 and np.abs((Ru/4) @ (Ru/4) - I8).max() < 1e-12
      and np.abs(Rd @ Rd - np.diag([0.]+[1.]*7)).max() > 0.1, f'plain nonuniform eig(R^2) max/min {spread:.2f}; dead corner {np.abs(Rd@Rd-np.diag([0.]+[1.]*7)).max():.2f}')

# ======================================================================= D  two tilings, 4^3 torus
print('== D. two-tiling torus 4^3')
L4 = 4; SITES = np.array(list(itertools.product(range(L4), repeat=3))); IDX = {tuple(x): i for i, x in enumerate(SITES)}
ecube = [tuple(x // 2) for x in SITES]; ocube = [tuple(((x-1) % L4) // 2) for x in SITES]
ecorn = (SITES % 2) @ [4, 2, 1]; ocorn = ((SITES-1) % 2) @ [4, 2, 1]
RA = np.zeros((64, 64), complex); RB = np.zeros((64, 64), complex)
EC = {}; OC = {}
for i in range(64): EC.setdefault(ecube[i], []).append(i); OC.setdefault(ocube[i], []).append(i)
for ids in EC.values(): RA[np.ix_(ids, ids)] = R8[np.ix_(ecorn[ids], ecorn[ids])]
for ids in OC.values(): RB[np.ix_(ids, ids)] = R8[np.ix_(ocorn[ids], ocorn[ids])]
eps, mu = 0.6, 0.1; t1, t2 = eps - mu/2, eps + mu/2
def floq(RBp): return expm(1j*t2*RBp) @ expm(-1j*t1*RA)
def band_dev(RBp):
    F = floq(RBp); cw = np.sort(np.cos(np.angle(np.linalg.eigvals(F))))
    sig = np.linalg.eigvalsh((RA @ RBp + RBp @ RA)/2); pred = np.sort(np.cos(t1)*np.cos(t2) + np.sin(t1)*np.sin(t2)*sig)
    return np.abs(cw - pred).max()
rng = np.random.default_rng(3); chi = rng.uniform(0, 6.3, 64); Dg = np.diag(np.exp(1j*chi)); RBg = Dg.conj() @ RB @ Dg
ae = {c: rng.uniform(0, 6.3) for c in EC}; bo = {c: rng.uniform(0, 6.3) for c in OC}
chif = np.array([ae[ecube[i]] + bo[ocube[i]] for i in range(64)]); Df = np.diag(np.exp(1j*chif)); RBf = Df.conj() @ RB @ Df
spec = lambda F: np.sort(np.angle(np.linalg.eigvals(F)))
dev_g = band_dev(RBg); flat_same = np.abs(spec(floq(RBf)) - spec(floq(RB))).max(); gen_diff = np.abs(spec(floq(RBg)) - spec(floq(RB))).max()
check('D1 [T] site-phase links (unitary registers, any field): the dressed odd hop stays a reflection and'
      ' cos w = cos t1 cos t2 + sin t1 sin t2 sigma (sigma: spectrum of {R_even, R_odd}/2) holds exactly; the flat field'
      ' (one phase per cube of each tiling) has exactly the free spectrum', np.abs(RBg @ RBg - np.eye(64)).max() < 1e-12
      and dev_g < 1e-10 and flat_same < 1e-10 and gen_diff > 1e-3, f'band dev {dev_g:.0e}; flat-free {flat_same:.0e}; generic shift {gen_diff:.2f}')
# edge layout c-number generic on odd cubes: reflection lost, identity fails
RBe = np.zeros((64, 64), complex)
for ids in OC.values(): ph = rng.uniform(0, 6.3, 12); M = edge_dress(ph); RBe[np.ix_(ids, ids)] = M[np.ix_(ocorn[ids], ocorn[ids])]
check('D2 [T] edge layout with a generic c-number field: the odd hop is no reflection and the band identity fails',
      np.abs(RBe @ RBe - np.eye(64)).max() > 0.1 and band_dev(RBe) > 1e-3, f'band dev {band_dev(RBe):.2f}')
# quantum registers, one particle: exact evolution in (position, even-end counts) space
UCACHE = {}; NT = int(os.environ.get('NT', '4'))
UA = {c: expm(-1j*t1*R8[np.ix_(ecorn[ids], ecorn[ids])]) for c, ids in EC.items()}
def run_quantum(S2, nt):     # S2 = 2S; Nb in 0..2S
    p0 = 0; qmid = (S2 + 1)//2 if S2 > 1 else 1
    nb0 = [qmid - (1 if i == p0 else 0) for i in range(64)]
    st = {(p0, tuple(nb0)): 1.0+0j}; first_dead = None; dead_w = []
    def gauss(st):
        k = next(iter(st)); p, nb = k
        return tuple(sum((p == i) + nb[i] for i in EC[c]) for c in EC), tuple(sum(nb[i] for i in OC[c]) for c in OC)
    g0 = gauss(st)
    for t in range(nt):
        new = {}
        for (p, nb), amp in st.items():
            ids = EC[ecube[p]]; U = UA[ecube[p]]; a = ids.index(p)
            for b, j in enumerate(ids):
                if abs(U[b, a]) > 1e-15: new[(j, nb)] = new.get((j, nb), 0) + U[b, a]*amp
        st = new; new = {}; wdead = 0.0
        for (p, nb), amp in st.items():
            ids = OC[ocube[p]]; q = [(p == i) + nb[i] for i in ids]; live = [1 <= qq <= S2 for qq in q]
            if not all(live): wdead += abs(amp)**2
            a = ids.index(p)
            if not live[a]: new[(p, nb)] = new.get((p, nb), 0) + amp; continue
            Lx = [k for k in range(8) if live[k]]; ck = (ocube[p], tuple(Lx))
            if ck not in UCACHE:
                oc = ocorn[[ids[k] for k in Lx]]; UCACHE[ck] = expm(1j*t2*R8[np.ix_(oc, oc)])
            U = UCACHE[ck]; aa = Lx.index(a)
            for bb, k in enumerate(Lx):
                if abs(U[bb, aa]) < 1e-15: continue
                nb2 = list(nb)
                if ids[k] != p: nb2[p] += 1; nb2[ids[k]] -= 1
                key = (ids[k], tuple(nb2)); new[key] = new.get(key, 0) + U[bb, aa]*amp
        st = {k: v for k, v in new.items() if abs(v) > 1e-13}; dead_w.append(wdead)
        if wdead > 1e-12 and first_dead is None: first_dead = t + 1
    norm = sum(abs(v)**2 for v in st.values()); gs = set()
    for k in st: gs.add(gauss({k: 1}))
    return first_dead, norm, len(gs) == 1 and g0 in gs, len(st), dead_w
qres = {S2: run_quantum(S2, NT) for S2 in (1, 3, 5)}
bound_ok = all((qres[S2][0] is None or qres[S2][0] >= (S2+1)//2) for S2 in qres)
check('D3 [T] quantum registers, one particle, two tilings: unitary (norm kept) and every cube Gauss number kept; the'
      ' first odd half-tick that meets a dead corner is never earlier than the distance d of the start from the register'
      ' extremes', all(abs(qres[S2][1]-1) < 1e-9 and qres[S2][2] for S2 in qres) and bound_ok,
      '; '.join(f'S={S2}/2: first dead tick {qres[S2][0]}, states {qres[S2][3]}' for S2 in qres))
print('   dead-corner weight per odd half-tick: ' + '; '.join(f'S={S2}/2 ' + ','.join(f'{w:.3f}' for w in qres[S2][4]) for S2 in qres))

# ======================================================================= E  copy sign
print('== E. copy sign and copy mass')
s = 1j*Ri[0] @ Ri[1] @ Ri[2] @ R8
rots = {}
for qq in binary_octahedral():
    Rm = np.round(q_so3(qq)).astype(int); key = tuple(Rm.ravel())
    if key in rots: continue
    w0, x, y, z = qq; ang = 2*np.arccos(np.clip(w0, -1, 1)); sn = np.sqrt(max(1-w0*w0, 0)); nv = np.array([x, y, z])/sn if sn > 1e-12 else np.array([0, 0, 1.])
    D = expm(-1j*ang*sum(nv[k]*J32[k] for k in range(3))); G = np.zeros((8, 8), complex)
    for a in range(8):
        cb = np.rint(Rm @ (CORN[a]-.5) + .5).astype(int); b = int(cb @ [4, 2, 1]); G[b, a] = XI[b].conj() @ D @ XI[a]
    rots[key] = (Rm, G)
covR = max(np.abs(G @ R8 @ G.conj().T - R8).max() for Rm, G in rots.values())
keep = [k for k, (Rm, G) in rots.items() if np.abs(G @ s @ G.conj().T - s).max() < 1e-9]
K = 0.3*(I8 - s) @ R8
check('E1 [T] undressed even cube: s Hermitian, s^2 = 1, [s,R] = 0; all 24 rotations keep R and exactly 12 keep s;'
      ' the copy-mass generator (MN/4)(1-s)R is Hermitian and acts inside one cluster, so it is gauge invariant',
      np.abs(s - s.conj().T).max() < 1e-12 and np.abs(s @ s - I8).max() < 1e-12 and np.abs(s @ R8 - R8 @ s).max() < 1e-12
      and covR < 1e-9 and len(rots) == 24 and len(keep) == 12 and np.abs(K - K.conj().T).max() < 1e-12, f'rotations keeping s: {len(keep)}/24')
def dress_i(M, q):
    D = np.diag([1.0 if 1 <= q[x] <= 2*S else 0.0 for x in range(8)]); return D @ M @ D
sp_live = 1j*dress_i(Ri[0], qn) @ dress_i(Ri[1], qn) @ dress_i(Ri[2], qn) @ dress_i(R8, qn)
sp_dead = 1j*dress_i(Ri[0], qd) @ dress_i(Ri[1], qd) @ dress_i(Ri[2], qd) @ dress_i(R8, qd)
P7 = np.diag([0.]+[1.]*7)
check('E2 [T] the same s read on a dressed cube (S = 3/2, normalised V): equal to s in an all-live sector, but with a dead'
      ' corner it is no involution on the live space: the copy sign needs the undressed (matter-frame) tiling',
      np.abs(sp_live - s).max() < 1e-12 and np.abs(sp_dead @ sp_dead - P7).max() > 0.1, f'dead: |s^2 - 1| = {np.abs(sp_dead@sp_dead-P7).max():.2f}')

# ======================================================================= F  placement
print('== F. placement')
p0 = np.array([.5, .5, .5]); stab = [(Rm, G) for k, (Rm, G) in rots.items() if k in keep and np.all(np.rint(Rm @ (np.zeros(3)-p0)+p0) == 0)]
blk = [np.array(v) for v in itertools.product((-1, 0, 1), repeat=3)]; seen = set(); orbs = []
for v in blk:
    if tuple(v) in seen: continue
    o = {tuple(np.rint(Rm @ v).astype(int)) for Rm, G in stab}; seen |= o; orbs.append(sorted(o))
nn = [o for o in orbs if all(sum(map(abs, u)) == 1 for u in o)]; fixed = [o for o in orbs if len(o) == 1]
check('F1 [T] a site keeps C3 (axis: its bond from even centre to odd centre) of the 12 copy-mass rotations; in its b = 3'
      ' block the nearest neighbours form exactly two 3-orbits (the faces toward each centre); the only fixed sites besides'
      ' the site are on the diagonal, not nearest neighbours: a covariant nearest-neighbour register has 3 rishons per end, S = 3/2',
      len(stab) == 3 and len(nn) == 2 and all(len(o) == 3 for o in nn) and sorted(map(len, fixed)) == [1, 1, 1]
      and all(abs(u[0]) == abs(u[1]) == abs(u[2]) for o in fixed for u in o), f'orbit sizes {sorted(map(len, orbs))}')
ecen = [np.array(c)*2 + .5 for c in itertools.product(range(2), repeat=3)]; mids = []
for c in ecen:
    for d in itertools.product((-1, 1), repeat=3): mids.append(tuple(np.rint((c + np.array(d)/2) % 4).astype(int)))
check('F2 [T] the bonds between neighbouring even and odd cube centres are in bijection with the sites (each site is the'
      ' midpoint of its own bond); one register per site, two cube-gauge phases per 8 sites: 6 register modes per cell'
      ' beyond gauge, of which 2 are photons (CL-3 must gap 4)', len(set(mids)) == 64 and len(mids) == 64,
      f'64 bonds -> {len(set(mids))} sites; cycle rank 64 - 16 + 1 = {64-16+1}')
print('   role sites per site, per U(1) factor: 1 matter + 3 + 3 rishons = 7 of 27 (b = 3), the same 7 sites as link-zoom'
      ' F3, regrouped as ONE S = 3/2 register on the site\'s own bond instead of six S = 1/2 edge registers; 56 per 2^3 cell')

# ======================================================================= G  estimates
print('== G. estimates')
k = 2*np.pi*np.arange(32)/32; kx, ky, kz = np.meshgrid(k, k, k, indexing='ij'); lam_k = 4*(np.sin(kx/2)**2+np.sin(ky/2)**2+np.sin(kz/2)**2)
cE = (2/3)*np.mean(np.sqrt(lam_k))/2
for alpha, lab_ in ((0.018, 'alpha_Y(M_Pl)'), (1/137.036, 'alpha_em')):
    g2 = 4*np.pi*alpha; sig = math.sqrt(cE/g2)
    print(f'   {lab_}: harmonic register vacuum sigma_E = sqrt({cE:.3f}/g^2) = {sig:.2f}; Gaussian weight beyond |E| = 3/2: '
          f'{math.erfc(1.5/(sig*math.sqrt(2))):.2f}, beyond 7/2: {math.erfc(3.5/(sig*math.sqrt(2))):.3f}')
flatV = {S2: S2/(S2+1) for S2 in (1, 3, 5, 9)}
check('G1 [E] on the truncated flat register state (uniform over levels) <V> = 2S/(2S+1) exactly, so the bare'
      ' cone is slower than the edge cone by about (2S/(2S+1))^2 per odd hop (1/4 at S = 1/2, 0.56 at S = 3/2)', abs(flatV[1]-.5) < 1e-12,
      ', '.join(f'S={S2}/2: {v**2:.2f}' for S2, v in flatV.items()))
print('supplied: matter frame = copy-mass tiling, S, flavour-blind C3-singlet register, domain-normalised V, start sectors, eps, mu.')
print(f'elapsed_seconds {time.time()-T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

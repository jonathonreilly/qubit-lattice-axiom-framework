#!/usr/bin/env python3
"""su2-disentangler: can an anomaly-free chiral SU(2) be made on-site by a constant-depth circuit (so it can be linked)?
 A representation arithmetic (exact): SM doublet count and anomalies; each simple factor alone is vector-like, the joint
   SU(3) x SU(2) and SU(2) x Y content is chiral; doublet pairing; 1+1D levels and SO(8) triality
 B rotor frame (TPF circuit at the self-dual radius, inline): the Cartan of an anomaly-free chiral SU(2) is disentangled;
   the U(1) rotor ancilla cannot carry SU(2)
 C Majorana carrier: an exact lattice chiral SU(2) (su(2)_+ on one chirality, su(2)_- on the other), its Gaussian
   disentangler needs one ancilla Majorana per cell and is then a depth-2 circuit; many-body check
 D non-abelian T1: a one-body su(2) with momentum-independent spectrum carries the same representation on both chiralities
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification. Cited, not rederived:
Thorngren-Preskill-Fidkowski arXiv:2601.04304 (U(1) only), Seifnashri-Shirley arXiv:2503.09717 (finite groups, 1+1D),
Witten 1982 (SU(2) global anomaly), SO(8) triality, bosonisation at the self-dual radius."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, math, os, random, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from collections import Counter
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm
import scipy.sparse as sp

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max()) if np.size(X) else 0.0

# ============================================ A. representation arithmetic ============================================
print('== A. representation arithmetic (exact fractions)')
FAM = [('3', 2, Fr(1, 6)), ('3b', 1, Fr(-2, 3)), ('3b', 1, Fr(1, 3)), ('1', 2, Fr(-1, 2)), ('1', 1, Fr(1)), ('1', 1, Fr(0))]
CDIM = {'1': 1, '3': 3, '3b': 3}; CONJ = {'1': '1', '3': '3b', '3b': '3'}
nD = sum(CDIM[c] for c, d, y in FAM if d == 2)
y2 = sum(CDIM[c] * y for c, d, y in FAM if d == 2)
sig = [np.array(m, dtype=complex) for m in ([[0, 1], [1, 0]], [[0, -1j], [1j, 0]], [[1, 0], [0, -1]])]
dabc = max(abs(np.trace(sig[a] @ (sig[b] @ sig[c] + sig[c] @ sig[b]))) for a, b, c in itertools.product(range(3), repeat=3))
def vectorlike(keep, nfam=1):
    """Weyl content is vector-like (admits an invariant mass) iff it is rho + conj(rho); a pseudoreal irrep (SU(2) doublet
    with conjugation-invariant remaining labels) must then appear an even number of times."""
    M = Counter()
    for c, d, y in FAM:
        lab = (c if 'c' in keep else '1', d if 'w' in keep else 1, y if 'y' in keep else Fr(0))
        M[lab] += nfam * (1 if 'c' in keep else CDIM[c]) * (1 if 'w' in keep else d)
    cj = lambda l: (CONJ[l[0]], l[1], -l[2])
    for l, m in M.items():
        if cj(l) != l and M[cj(l)] != m: return False
        if cj(l) == l and l[1] == 2 and m % 2: return False
    return True
VL = {k: vectorlike(k) for k in ['w', 'c', 'y', 'cw', 'wy', 'cy']}
check('A1 [T] SM family (with nu^c): N_doublets = N_c + 1 = 4 (Witten Z_2 cancels), SU(2)^2 Y = 3/6 - 1/2 = 0, SU(2)^3 vanishes '
      'identically (d^abc = 0); the content is vector-like under SU(2) alone and SU(3) alone, chiral under Y, SU(3)xSU(2), SU(2)xY',
      nD == 4 and y2 == 0 and dabc < 1e-14 and VL == {'w': True, 'c': True, 'y': False, 'cw': False, 'wy': False, 'cy': False}
      and all(vectorlike(k, 3) == v for k, v in VL.items()), 'vector-like: ' + ', '.join(f'{k}={v}' for k, v in VL.items()))
eps = np.array([[0, 1], [-1, 0]], dtype=complex)
pair_ok = all(nrm(eps @ s.conj() @ np.linalg.inv(eps) + s) < 1e-15 for s in sig)
Ys = [Fr(1, 6)] * 3 + [Fr(-1, 2)]
def matchings(xs):
    if not xs: yield []; return
    a = xs[0]
    for i in range(1, len(xs)):
        for m in matchings(xs[1:i] + xs[i + 1:]): yield [(a, xs[i])] + m
pairs = list(matchings(list(range(4))))
vec_pair = [all(Ys[a] == -Ys[b] for a, b in m) for m in pairs]
check('A2 [T] eps sigma^a* eps^-1 = -sigma^a: two left-handed doublets chi_1, chi_2 form one Dirac doublet (chi_1, eps chi_2^c) with '
      'vector SU(2), so SU(2) can be on-site on doublets; in each of the 3 pairings of a family\'s 4 doublets Y acts chirally '
      '(q_L = Y_a != q_R = -Y_b), and pairing Q with Q puts colour on L as 3, on R as 3bar',
      pair_ok and len(pairs) == 3 and not any(vec_pair), 'pairings (q_L, q_R): ' + '; '.join(
          ','.join(f'({Ys[a]},{-Ys[b]})' for a, b in m) for m in pairs))
def wts(h, rep):
    if rep == 'v': W_ = [tuple(s if i == k else 0 for i in range(4)) for k in range(4) for s in (1, -1)]
    else: W_ = [w for w in itertools.product((Fr(1, 2), Fr(-1, 2)), repeat=4) if (sum(x < 0 for x in w) % 2 == 0) == (rep == 's')]
    return sorted(sum(Fr(a) * b for a, b in zip(w, h)) for w in W_)
def decomp(ms):
    c = Counter(ms); out = Counter()
    while c:
        top = max(c); j = top; m = j
        while m >= -j: c[m] -= 1; c[m] == 0 and c.pop(m); m -= 1
        out[j] += 1
    return {str(k): v for k, v in sorted(out.items())}
hv, hs = (1, 0, 0, 0), (Fr(1, 2),) * 4
D_ = {(h, r): decomp(wts(hh, r)) for h, hh in (('v', hv), ('s', hs)) for r in 'vsc'}
lev = [sum(m * m for m in wts(hh, 'v')) for hh in (hv, hs)]
fock_v, fock_s = decomp(wts(hv, 's') + wts(hv, 'c')), decomp(wts(hs, 's') + wts(hs, 'c'))
check('A3 [T] 1+1D, 8 Majoranas: E_v (8_v = 3 + 5x1, a Majorana triplet) and E_s (8_v = 4 doublets, two complex doublets) both have '
      'level sum m^2 = 2, so L: two doublets vs R: triplet + 5 singlets is anomaly-free (k = 2, c = 4) and chiral; triality '
      'swaps them (E_v on 8_s = E_s on 8_v); on one site\'s 16-dim Fock space they differ, so no site unitary maps one to the other',
      lev == [2, 2] and D_[('v', 'v')] == {'0': 5, '1': 1} and D_[('s', 'v')] == {'1/2': 4} and D_[('v', 's')] == D_[('s', 'v')]
      and D_[('s', 's')] == D_[('v', 'v')] and fock_v != fock_s,
      f'E_v: 8v {D_[("v","v")]}, 8s {D_[("v","s")]}; Fock E_v {fock_v} vs E_s {fock_s}')

# ============================================ B. rotor frame (TPF, inline) ============================================
print('== B. rotor frame: angle phi_j in [0,1), winding n_j per link; TPF disentangler rederived (exact rationals)')
def rnd(x): return math.floor(x + Fr(1, 2))
def f1(x): return x - math.floor(x)
def cp(x): return ([r[:] for r in x[0]], [r[:] for r in x[1]], x[2][:], x[3][:])
def QAw(p, n): N = len(p); return -sum(rnd(p[(j + 1) % N] - p[j]) + n[j] for j in range(N))
def sym(x, be, qs):
    y = cp(x); y[0][:] = [[f1(p + qV * be) for p in x[0][a]] for a, (qV, qA) in enumerate(qs)]; y[2][:] = [f1(t + be) for t in x[2]]
    return y, be * sum(qA * QAw(x[0][a], x[1][a]) for a, (qV, qA) in enumerate(qs))
def ylink(ph, n, th, qs, k):
    N = len(th); return sum(qA * (rnd(ph[al][(k + 1) % N] - ph[al][k] + qV * (th[(k + 1) % N] - th[k])) + n[al][k]) for al, (qV, qA) in enumerate(qs))
def Xr(ph, qs, k): return rnd(sum(qA * ph[al][k % len(ph[al])] for al, (qV, qA) in enumerate(qs)))
def Phi(ph, n, th, qs): return -sum(th[k] * (ylink(ph, n, th, qs, k) - (Xr(ph, qs, k + 1) - Xr(ph, qs, k))) for k in range(len(th)))
def Wf(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] + qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, Phi(x[0], x[1], x[2], qs)
def Wd(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] - qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, -Phi(y[0], y[1], y[2], qs)
def comp(x, ops):
    ps = Fr(0)
    for op in ops: x, p = op(x); ps += p
    return x, ps
rng = random.Random(20261022); NB = 5; NT = 200
def ident(qs):
    fails = 0
    for t in range(NT):
        x = ([[Fr(rng.randrange(48), 48) for _ in range(NB)] for _ in qs], [[rng.randrange(-2, 3) for _ in range(NB)] for _ in qs],
             [Fr(rng.randrange(48), 48) for _ in range(NB)], [Fr(0)] * NB); be = Fr(rng.randrange(1, 97), 97)
        u = comp(x, [lambda z: Wf(z, qs), lambda z: sym(z, be, qs), lambda z: Wd(z, qs)]); v = cp(x); v[2][:] = [f1(tt + be) for tt in x[2]]
        fails += not (u[0] == v and f1(u[1]) == 0)
    return fails
hw = lambda p, w: (Fr((p + w) ** 2, 4), Fr((p - w) ** 2, 4))
cur = [hw(1, 1), hw(-1, -1), hw(1, -1), hw(-1, 1)]
SETS = {'L1+R2': [(1, 1), (1, -1)], 'L1 alone': [(1, 1)], 'L1+L2': [(1, 1), (1, 1)], 'L1+L3+R1+R2 (A3 bosonised)': [(2, 0), (1, 1), (1, -1)]}
res = {k: (ident(q), sum(a * b for a, b in q)) for k, q in SETS.items()}
check('B1 [T] self-dual radius: e^{+-i(phi + theta)} (p, w) = +-(1, 1) have (h, hbar) = (1, 0), e^{+-i(phi - theta)} have (0, 1): '
      'the SU(2)_1 x SU(2)_1 currents; the Cartan 2J3_L = p + w is the TPF charge (qV, qA) = (1, 1); the anomaly-free chiral '
      'Cartans (c = sum qV qA = 0) are disentangled exactly, SU(2)_L alone and L1+L2 fail',
      cur == [(1, 0), (1, 0), (0, 1), (0, 1)] and all((f == 0) == (c == 0) for f, c in res.values())
      and res['L1+R2'][0] == 0 and res['L1 alone'][0] > NT // 4,
      '; '.join(f'{k}: c={c}, fails {f}/{NT}' for k, (f, c) in res.items()))
mu_rotor = lambda m: 1
def multiplicity_from_irreps(n, m): return sum(v for j, v in n.items() if j >= abs(m) and (j - m) % 1 == 0)
# weight multiplicities mu(m) of any SU(2) rep fix n_j = mu(j) - mu(j+1); the rotor (mu = 1 for all m in Z or Z/2) gives n_j = 0
nj = {Fr(j, 2): mu_rotor(Fr(j, 2)) - mu_rotor(Fr(j, 2) + 1) for j in range(0, 40)}
pw = {Fr(j, 2): 2 * Fr(j, 2) + 1 for j in range(0, 40)}
check('B2 [T] in TPF\'s frame the symmetry acts only by ancilla turns e^{2 pi i b L_j}; an SU(2) with Cartan L_j (or L_j/2) on the '
      'rotor l^2(Z) would need n_j = mu(j) - mu(j+1) = 0 for every spin j, yet mu(0) = 1: none exists. An SU(2)-rotor ancilla '
      'L^2(SU(2)) (n_j = 2j + 1, Peter-Weyl) is admissible, but pi_1(SU(2)) = 0 gives it no winding integer for TPF\'s phase',
      all(v == 0 for v in nj.values()) and multiplicity_from_irreps(nj, 0) == 0 != mu_rotor(0)
      and multiplicity_from_irreps(pw, 0) > 0, 'rotor n_j all 0; SU(2) rotor mu(0) truncated = ' + str(multiplicity_from_irreps(pw, 0)))

# ============================================ C. Majorana carrier ============================================
print('== C. Majorana chain, 4 flavours per cell (one doublet = 2 qubit sites), H = sum (i/2) chi^a_j chi^a_j+1')
def Lij(n, i, j): M = np.zeros((n, n)); M[i, j] = 1; M[j, i] = -1; return M
def su2pm(n=4):
    Gp = [0.5 * (Lij(n, b, c) + Lij(n, a, 3)) for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1))]
    Gm = [0.5 * (Lij(n, b, c) - Lij(n, a, 3)) for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1))]
    s = 1 if nrm(Gp[0] @ Gp[1] - Gp[1] @ Gp[0] - Gp[2]) < 1e-14 else -1
    sm = 1 if nrm(Gm[0] @ Gm[1] - Gm[1] @ Gm[0] - Gm[2]) < 1e-14 else -1
    return [s * g for g in Gp], [sm * g for g in Gm]
Gp, Gm = su2pm()
def closes(G): return max(nrm(G[a] @ G[b] - G[b] @ G[a] - G[c]) for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)))
def inspan(X, G):
    B = np.array([g.ravel() for g in G]).T; c = np.linalg.lstsq(B, X.ravel(), rcond=None)[0]; return nrm(B @ c - X.ravel())
Lc = 12; NF = 4; ix = lambda j, a, nf=NF: (j % Lc) * nf + a
def chainH(nf, flav):
    A = np.zeros((Lc * nf, Lc * nf))
    for j in range(Lc):
        for a in flav: A[ix(j, a, nf), ix(j + 1, a, nf)] += 1; A[ix(j + 1, a, nf), ix(j, a, nf)] -= 1
    return A
def onsite(g, nf):
    M = np.zeros((Lc * nf, Lc * nf)); k = g.shape[0]
    for j in range(Lc): M[j * nf:j * nf + k, j * nf:j * nf + k] = g
    return M
AH = chainH(NF, range(4))
S = np.eye(Lc * NF)
for j in range(Lc): S[ix(j, 3), ix(j, 3)] = 0
for j in range(Lc): S[ix(j + 1, 3), ix(j, 3)] = 1        # chi^4_j -> chi^4_{j+1}: a Majorana translation of one flavour
Gc = [S @ onsite(g, NF) @ S.T for g in Gp]
def reach(M, nf):
    d = [min((i // nf - j // nf) % Lc, (j // nf - i // nf) % Lc) for i, j in zip(*np.nonzero(np.abs(M) > 1e-12))]; return max(d) if d else 0
def bloch(M, nf, k):
    out = np.zeros((nf, nf), dtype=complex)
    for a, b in itertools.product(range(nf), repeat=2):
        for jp in range(Lc): out[a, b] += M[ix(0, a, nf), ix(jp, b, nf)] * np.exp(1j * k * jp)
    return out
G0, Gpi = [bloch(g, NF, 0).real for g in Gc], [bloch(g, NF, np.pi).real for g in Gc]
spec = np.sort(np.linalg.eigvalsh(1j * Gc[2]))
check('C1 [T] T^a = (i/4) chi G^a chi with G^a = S (onsite su(2)_+) S^T, S the one-flavour Majorana translation: conserved, exact '
      'su(2) ([T^a, T^b] = i eps T^c), one-body levels +-1/2, range one cell, not on-site; it acts as su(2)_+ at K = 0 and su(2)_- '
      'at K = pi, where H\'s two light points move oppositely: an exact anomaly-free chiral SU(2) (L1+R2 after bosonisation)',
      max(nrm(g @ AH - AH @ g) for g in Gc) < 1e-14 and closes(Gc) < 1e-14 and np.allclose(np.abs(spec), 0.5)
      and reach(Gc[0], NF) == 1 and max(inspan(g, Gp) for g in G0) < 1e-12 and max(inspan(g, Gm) for g in Gpi) < 1e-12
      and min(inspan(g, Gp) for g in Gpi) > 0.1, f'reach {reach(Gc[0], NF)}, K = pi residual in su(2)_+ {min(inspan(g, Gp) for g in Gpi):.2f}')
nr = np.random.default_rng(7); Ao = nr.normal(size=(4, 4)); O = expm(Ao - Ao.T); Dm = np.diag([1., 1., 1., -1.])
pres = max(inspan(O @ g @ O.T, Gp) for g in Gp); swap = max(inspan(O @ Dm @ g @ Dm @ O.T, Gm) for g in Gp)
def layer_det(ks):     # random translation-invariant parity-even brickwork: onsite g1 in SO(4), bond gate g2 in SO(4) on (2,3 | 0,1 of next cell)
    A1 = nr.normal(size=(4, 4)); g1 = expm(A1 - A1.T); A2 = nr.normal(size=(4, 4)); g2 = expm(A2 - A2.T); out = []
    for k in ks:
        P = np.diag([1, 1, np.exp(-1j * k), np.exp(-1j * k)]); R = np.zeros((4, 4), dtype=complex)
        R[np.ix_([2, 3, 0, 1], [2, 3, 0, 1])] = g2; out.append(np.linalg.det(P.conj() @ R @ P @ g1))
    return out
ks = np.linspace(0, 2 * np.pi, 9); dets = layer_det(ks)
wind_S = np.angle(np.linalg.det(np.diag([1, 1, 1, np.exp(1j * np.pi)])))
check('C2 [T] SO(4) preserves su(2)_+ and every improper O(4) element maps it to su(2)_-, so any translation-invariant Gaussian '
      'disentangler V(K) on these 4 flavours has det V(0) det V(pi) = -1, an odd winding of det V(K) (S itself: e^{iK}); every '
      'parity-even translation-invariant Gaussian circuit has det V(K) = 1 at all K: without ancillas no such circuit disentangles',
      pres < 1e-12 and swap < 1e-12 and max(abs(d - 1) for d in dets) < 1e-12 and abs(abs(wind_S) - np.pi) < 1e-12,
      f'max |det - 1| on random brickwork {max(abs(d - 1) for d in dets):.1e}')
NA = 6; ixa = lambda j, a: ix(j, a, NA)
def rot(n, pairs):     # chi_x -> chi_y, chi_y -> -chi_x for each (x, y)
    M = np.eye(n)
    for x, y in pairs: M[x, x] = M[y, y] = 0; M[y, x] = 1; M[x, y] = -1
    return M
Oa = rot(Lc * NA, [(ixa(j + 1, 3), ixa(j, 4)) for j in range(Lc)]); Ob = rot(Lc * NA, [(ixa(j, 4), ixa(j, 3)) for j in range(Lc)])
Wc = Ob @ Oa
emb = lambda M: (lambda E: (E.__setitem__(np.ix_(*[[ixa(j, a) for j in range(Lc) for a in range(4)]] * 2), M[np.ix_(*[[ix(j, a) for j in range(Lc) for a in range(4)]] * 2)]), E)[1])(np.zeros((Lc * NA, Lc * NA)))
GcA = [emb(g) for g in Gc]; Gd = [Wc @ g @ Wc.T for g in GcA]
AHA = emb(AH); Anc = np.zeros_like(AHA)
for j in range(Lc): Anc[ixa(j, 4), ixa(j, 5)] = 1; Anc[ixa(j, 5), ixa(j, 4)] = -1
Hd = Wc @ (AHA + Anc) @ Wc.T
blk = [g[:4, :4] for g in Gd]
onsite_ok = max(nrm(Gd[a] - onsite(np.pad(blk[a], ((0, 2), (0, 2))), NA)) for a in range(3))
anc_gap = np.min(np.abs(np.linalg.eigvalsh(1j * (Wc @ Anc @ Wc.T))[np.abs(np.linalg.eigvalsh(1j * (Wc @ Anc @ Wc.T))) > 1e-9]))
check('C3 [T] with one singlet ancilla Majorana pair per cell (gapped by i chi^5 chi^6), the depth-2 circuit [bond swaps '
      'chi^4_{j+1} <-> chi^5_j, then onsite swaps chi^5_j <-> chi^4_j] maps T^a exactly to an on-site su(2) on each cell, '
      'leaves the ancilla gapped (bond dimers), and the new update term commutes with the on-site SU(2) at range one',
      onsite_ok < 1e-14 and closes(blk) < 1e-14 and (max(inspan(b, Gp) for b in blk) < 1e-12 or max(inspan(b, Gm) for b in blk) < 1e-12)
      and max(nrm(g @ Hd - Hd @ g) for g in Gd) < 1e-14 and reach(Hd, NA) == 1 and abs(anc_gap - 1) < 1e-12,
      f'on-site residual {onsite_ok:.0e}, ancilla gap {anc_gap:.3f}')
# many-body check on 3 cells x 6 Majoranas = 9 modes (512 states)
Lm, nm = 3, 9
I2, Z, X, Y = sp.identity(2, format='csr'), sp.csr_matrix([[1, 0], [0, -1]]), sp.csr_matrix([[0, 1], [1, 0]]), sp.csr_matrix([[0, -1j], [1j, 0]])
def kron_all(ms):
    out = ms[0]
    for m in ms[1:]: out = sp.kron(out, m, format='csr')
    return out
chi = [kron_all([Z] * q + [P] + [I2] * (nm - q - 1)) for q in range(nm) for P in (X, Y)]
def Pq(A): return 0.25 * sum(A[x, y] * (chi[x] @ chi[y]) for x, y in zip(*np.nonzero(np.abs(A) > 1e-14)))
def small(L_):
    global Lc
    Lc = L_; S_ = np.eye(Lc * NA)
    for j in range(Lc): S_[ixa(j, 3), ixa(j, 3)] = 0
    for j in range(Lc): S_[ixa(j + 1, 3), ixa(j, 3)] = 1
    G_ = [S_ @ onsite(np.pad(g, ((0, 2), (0, 2))), NA) @ S_.T for g in Gp]
    gates = [[(ixa(j + 1, 3), ixa(j, 4)) for j in range(Lc)], [(ixa(j, 4), ixa(j, 3)) for j in range(Lc)]]
    Wone = np.eye(Lc * NA)
    for lay in gates: Wone = rot(Lc * NA, lay) @ Wone
    return G_, gates, Wone
G3, gates3, W3 = small(Lm)
T = [1j * Pq(g) for g in G3]
alg = max(abs((T[a] @ T[b] - T[b] @ T[a] - 1j * T[c])).max() for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1)))
def mb_unitary(B): return expm(Pq(B).toarray())
Wmb = np.eye(2 ** nm, dtype=complex)
for lay in gates3:
    for x, y in lay:
        B = np.zeros((Lc * NA, Lc * NA)); B[x, y] = np.pi / 2; B[y, x] = -np.pi / 2; Wmb = mb_unitary(B) @ Wmb
cands = [W3, W3.T]
target = [[1j * Pq(Ow @ g @ Ow.T).toarray() for g in G3] for Ow in cands]
conj = [Wmb @ t.toarray() @ Wmb.conj().T for t in T]
mbres = min(max(nrm(conj[a] - target[i][a]) for a in range(3)) for i in range(2))
ev3 = np.linalg.eigvalsh(T[2].toarray()); halfint = nrm(2 * ev3 - np.round(2 * ev3))
check('C4 [T] many-body (3 cells, 9 modes): the T^a close su(2) exactly with T^3 levels in Z/2, and the depth-2 gate circuit '
      'conjugates them to the on-site Gaussian image (Gaussian = many-body, no hidden phase)',
      alg < 1e-12 and mbres < 1e-12 and halfint < 1e-12, f'algebra {alg:.0e}, conjugation {mbres:.0e}, T3 levels {sorted(set(float(x) for x in np.round(ev3, 6)))}')
Lc = 12

# ============================================ D. non-abelian T1 ============================================
print('== D. non-abelian T1 (one-body charges of a free translation-invariant update)')
kk = np.linspace(0, np.pi, 13)
GK = [[bloch(g, NF, k) for g in Gc] for k in kk]
constspec = max(nrm(np.sort(np.linalg.eigvalsh(1j * G[2])) - np.array([-.5, -.5, .5, .5])) for G in GK)
check('D1 [T] if one-body X^a(K) close su(2) at each K with K-independent spectra, the su(2) character is continuous and '
      'integral, so the representation at K = 0 equals the one at K = pi: C1 passes (2 + 2 at every K, su(2)_+ vs su(2)_- is '
      'invisible to it), the genuinely chiral pair E_s (R) vs E_v (L) of A3 cannot be a free one-body charge',
      constspec < 1e-12 and D_[('s', 'v')] != D_[('v', 'v')], f'C1 spectrum deviation {constspec:.0e}; E_s {D_[("s","v")]} vs E_v {D_[("v","v")]}')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('all [T]. Supplied: the carriers (Villain rotors; Majorana flavours with a singlet ancilla pair), the free chain, the SM content. '
      'Cited: TPF 2601.04304, Seifnashri-Shirley 2503.09717, Witten SU(2) anomaly, SO(8) triality.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

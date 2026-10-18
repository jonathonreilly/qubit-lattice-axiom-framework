"""B23 checker: the step letters rebuilt from B7_check/chk_core.py (own GF(2) gauge solver, own brute-force PSG,
own conventions H(k) = sum_d h_d e^{-i k.d}).  Nothing from chk_model / chklib / b23lib / b20lib / walklib.
Letters (same geometric definitions as the runner, different gauge and code):
  H_on = -sum_onsite (-1)^u,  R_L = -(1/sqrt2) sum_link (-1)^u,  Lambda = i (-1)^u around oriented octant triangles,
  S = symmetrisation of the hop {x,y}@0 -> {x,y}@(1,1,0) over proper rotations (PSG lifts) and translations.
On-site phase words from the eigenprojectors of H_on (sorted ascending) and Lambda (sorted ascending)."""
import os, sys, itertools
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ.setdefault(_v, "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B7_check'))
import numpy as np
import chk_core as K

Lt = 4
T4 = K.torus_ops(Lt)
sites, si, n = T4['sites'], T4['si'], T4['n']
CORN, CI = K.CORN, K.CI
def dm(x): return ((x + 1) % Lt) - 1
def idx(v, c): return 12 * si[tuple(x % Lt for x in v)] + CI[c]
def usign(v, c1, w, c2):
    s = tuple(dm(b - a) for a, b in zip(v, w))
    return (-1.0) ** int(K.u[K.ETYPES[K.edge_key(c1, c2, s)]])
Hon = np.zeros((n, n)); HL = np.zeros((n, n)); LamR = np.zeros((n, n), complex)
for v in sites:
    for c in CORN:
        a, b = tuple(c)
        for x, y in ((a, b), (b, a)):
            for f in K.third(x, y):
                c2 = frozenset((x, f)); i, j = idx(v, c), idx(v, c2)
                Hon[i, j] = -usign(v, c, v, c2)
            w = K.vadd(v, x); c2 = frozenset((K.neg(x), y)); i, j = idx(v, c), idx(w, c2)
            HL[i, j] = -usign(v, c, w, c2)
assert np.allclose(Hon, Hon.T) and np.allclose(HL, HL.T)
for v in sites:
    for sg in itertools.product((1, -1), repeat=3):
        x, y, z = (sg[0], 0, 0), (0, sg[1], 0), (0, 0, sg[2])
        cy = [frozenset((x, y)), frozenset((y, z)), frozenset((z, x))]
        if round(np.linalg.det(np.array([x, y, z]))) < 0: cy = cy[::-1]
        for a_ in range(3):
            q, r = cy[a_], cy[(a_ + 1) % 3]
            amp = 1j * usign(v, q, v, r); LamR[idx(v, r), idx(v, q)] += amp; LamR[idx(v, q), idx(v, r)] += np.conj(amp)
RL = HL / np.sqrt(2)
assert np.allclose(RL @ RL, np.eye(n))
cxy = frozenset(((1, 0, 0), (0, 1, 0)))
i0, j0 = idx((0, 0, 0), cxy), idx((1, 1, 0), cxy)
Gs = [T4['G'](g) for g in K.PROPER]
X0 = np.zeros((n, n)); X0[j0, i0] = 1
Y = sum(G @ X0 @ G.T for G in Gs)
Ssum = np.zeros((n, n))
for a in sites:      # translations (no signs in this translation-invariant gauge) as index permutations
    perm = np.zeros(n, int)
    for v in sites:
        w = tuple((x + y) % Lt for x, y in zip(v, a)); perm[12 * si[w]:12 * si[w] + 12] = np.arange(12 * si[v], 12 * si[v] + 12)
    # (T Y T^T)[perm[p], perm[q]] = Y[p, q]
    Z_ = np.zeros((n, n)); Z_[np.ix_(perm, perm)] = Y; Ssum += Z_
Sreal = Ssum / np.abs(Ssum).max()
assert np.allclose(Sreal @ Sreal.T, np.eye(n)) and np.all(np.isin(np.round(np.abs(Sreal), 9), [0, 1]))
hS, hL, hON, hLam = (T4['to_blocks'](M) for M in (Sreal, RL, Hon, LamR))
Hon0 = hON[(0, 0, 0)].real; Lam0 = hLam[(0, 0, 0)]
assert all(np.abs(hON[d]).max() < 1e-12 for d in hON if d != (0, 0, 0))
def Hk1(h, k):
    M = np.zeros((12, 12), complex)
    for d, B in h.items():
        if np.abs(B).max() > 0: M += B * np.exp(-1j * np.dot(k, d))
    return M
def eproj(M):
    w_, V_ = np.linalg.eigh(M); ls = sorted(set(np.round(w_, 6)))
    return ls, [V_[:, np.abs(w_ - l) < 1e-6] @ V_[:, np.abs(w_ - l) < 1e-6].conj().T for l in ls]
lsH, PHc = eproj(Hon0); lsL, PLc = eproj(Lam0)
def onH(a, b, unit=3): return PHc[0] + np.exp(1j * np.pi * unit * a / 6) * PHc[1] + np.exp(1j * np.pi * unit * b / 6) * PHc[2]
def onL(a, b, c, unit=3):
    return PLc[0] + np.exp(1j * np.pi * unit * a / 6) * PLc[1] + np.exp(1j * np.pi * unit * b / 6) * PLc[2] + np.exp(1j * np.pi * unit * c / 6) * PLc[3]
def onsite_by_name(nm):
    """names as in b23lib: 'H{a}{b}', 'L{a}{b}{c}' (unit pi/2), 'H{a}*L..' products, 'H{a}.{b}', 'L{a}.{b}.{c}' (unit pi/6), 'L202'"""
    if '*' in nm:
        a, b = nm.split('*'); return onsite_by_name(a) @ onsite_by_name(b)
    if nm == 'L202': return onL(2, 0, 2)
    if '.' in nm:
        p = [int(x) for x in nm[1:].split('.')]
        return onH(*p, unit=1) if nm[0] == 'H' else onL(*p, unit=1)
    p = [int(x) for x in nm[1:]]
    return onH(*p) if nm[0] == 'H' else onL(*p)
fdiag = None
def S_k(k, p):
    d = np.diag(Hk1(hS, k))
    assert np.allclose(Hk1(hS, k), np.diag(d))
    return np.diag(d ** p) if p > 0 else np.diag(np.conj(d) ** (-p))
PWR = {'S': 1, 'Si': -1, 'S2': 2, 'S2i': -2}
def word(sk, names):
    it = iter(names); out = []
    for Lr in sk: out.append(onsite_by_name(next(it)) if Lr == 'o' else Lr)
    return out
def Wk(w, k):
    k = np.asarray(k, float); M = np.eye(12, dtype=complex)
    for Lr in w:
        if isinstance(Lr, str): M = M @ (Hk1(hL, k) if Lr == 'R' else S_k(k, PWR[Lr]))
        else: M = M @ Lr
    return M
def nS(w): return sum(PWR.get(x, 0) for x in w if isinstance(x, str))
Dsp = np.linalg.eigh(Hon0)[1][:, np.abs(np.linalg.eigvalsh(Hon0) - 2) < 1e-6]       # H_on = 2 space (D+ + D-)

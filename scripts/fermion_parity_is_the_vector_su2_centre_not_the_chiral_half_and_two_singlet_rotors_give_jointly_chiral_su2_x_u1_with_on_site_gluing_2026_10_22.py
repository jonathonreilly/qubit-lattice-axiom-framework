#!/usr/bin/env python3
"""fermion-spin-half: carry the SU(2) doublet on fermion modes, so the SU(2) centre is fermion parity, and ask whether the
Z_2 gluing of charge parity to isospin parity becomes local; then build the 1+1D jointly chiral SU(2) x U(1) swap content.
 A one cell of two complex modes (4 Majoranas): centre = fermion parity; the chiral SU(2) of su2-disentangler too
 B what fermion parity cannot do (exact rationals): the gluing's spin half is the LEFT-mover centre z_L (chiral fermion
   parity, Z_8 index 4), not the centre z_V = z_L z_R of any on-site SU(2); a c = 1 SU(2)_1 spin carrier has no fermions
 C half-filled Hubbard ring (exact diagonalisation): with the charge gapped the IR spin half is translation again
 D construction: genuine fermion doublet and singlets with on-site vector charges and on-site SU(2), plus two SU(2)-singlet
   TPF rotors that carry the anomaly; one null locking term per rotor; residual = swap content (3,1); TPF; gluing on-site
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification. Cited, not
rederived: TPF arXiv:2601.04304 (rotor disentangler, inlined as in su2-disentangler B), Haldane null-vector gapping
criterion (lattice algebra checked here, the flow to the locked phase is cited), Else-Nayak, Lieb-Schultz-Mattis."""
from __future__ import annotations
AUDIT_INPUT_PATHS = ('docs/FERMION_PARITY_IS_THE_VECTOR_SU2_CENTRE_NOT_THE_CHIRAL_HALF_AND_TWO_SINGLET_ROTORS_GIVE_JOINTLY_CHIRAL_SU2_X_U1_WITH_ON_SITE_GLUING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')

AUDIT_TIMEOUT_SEC = 120

import itertools, math, os, random, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np
from scipy.linalg import expm

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
nrm = lambda X: float(np.abs(X).max()) if np.size(X) else 0.0
H = Fr(1, 2)
I2, Zp, Xp, Yp = np.eye(2), np.diag([1., -1.]), np.array([[0., 1.], [1., 0.]]), np.array([[0, -1j], [1j, 0]])
def kron_all(ms):
    out = np.array([[1.]])
    for m in ms: out = np.kron(out, m)
    return out
def jw(nq):   # complex modes c_q and Majoranas chi_{2q}, chi_{2q+1}
    lo = np.array([[0., 1.], [0., 0.]])
    c = [kron_all([Zp] * q + [lo] + [I2] * (nq - q - 1)) for q in range(nq)]
    chi = [kron_all([Zp] * q + [P] + [I2] * (nq - q - 1)) for q in range(nq) for P in (Xp, Yp)]
    return c, chi

# ================================ A. one cell ================================
print('== A. one cell: c_up, c_dn (= 4 Majoranas); spin S^a = c^dag sigma^a c / 2, pseudospin eta^+ = c_up^dag c_dn^dag')
(cu, cd), _ = jw(2); cdg = lambda m: m.conj().T
nu, nd = cdg(cu) @ cu, cdg(cd) @ cd; n = nu + nd; Pf = expm(1j * np.pi * n)
Sp = cdg(cu) @ cd; Sz = (nu - nd) / 2; Ep = cdg(cu) @ cdg(cd); Ez = (n - np.eye(4)) / 2
zS, zE = expm(2j * np.pi * Sz), expm(2j * np.pi * Ez)
comm = lambda A, B: A @ B - B @ A
ok = (nrm(zS - Pf) < 1e-12 and nrm(zE + Pf) < 1e-12 and nrm(zS @ zE + np.eye(4)) < 1e-12
      and max(nrm(comm(Sp, X)) for X in (Ep, cdg(Ep), Ez)) < 1e-12 and nrm(comm(Sz, Ep)) < 1e-12 and nrm(comm(n, Ep) - 2 * Ep) < 1e-12)
check('A1 [T] on a cell of two complex modes the SU(2) centre e^{2 pi i S^z} IS the cell fermion parity (-1)^n; the commuting '
      'pseudospin (charge) SU(2) has centre -(-1)^n, so (spin centre)(charge centre) = -1 on every cell: on fermion modes the '
      'doublet gluing is an operator identity; the singlet pair c_up^dag c_dn^dag commutes with SU(2) and carries charge 2', ok)
def Lij(m, i, j): M = np.zeros((m, m)); M[i, j] = 1; M[j, i] = -1; return M
Gp = [0.5 * (Lij(4, b, c) + Lij(4, a, 3)) for a, b, c in ((0, 1, 2), (1, 2, 0), (2, 0, 1))]
if nrm(comm(Gp[0], Gp[1]) - Gp[2]) > 1e-12: Gp = [-g for g in Gp]
Lc = 3; S = np.eye(4 * Lc)
for j in range(Lc): S[4 * j + 3, 4 * j + 3] = 0; S[4 * ((j + 1) % Lc) + 3, 4 * j + 3] = 1
G3 = S @ np.kron(np.eye(Lc), Gp[2]) @ S.T
_, chi = jw(2 * Lc)
T3 = 0.25 * sum(G3[x, y] * chi[x] @ chi[y] for x in range(4 * Lc) for y in range(4 * Lc) if abs(G3[x, y]) > 1e-14)
T3 = 1j * T3; Ptot = kron_all([Zp] * (2 * Lc)); U = expm(2j * np.pi * T3); ph = U[0, 0] / Ptot[0, 0]
check('A2 [T] the exact chiral (non-on-site) SU(2) of su2-disentangler C1 (3 cells, 12 Majoranas) also has centre '
      'e^{2 pi i T^3} = (phase) x (-1)^F: internal, on-site and equal to fermion parity before any disentangler',
      nrm(U - ph * Ptot) < 1e-10 and abs(abs(ph) - 1) < 1e-12, f'phase {ph.real:+.0f}')

# ================================ B. what fermion parity cannot do ================================
print('== B. vertex lattices v = (nL, mL, nR, mR), spin = (nL^2 + mL^2 - nR^2 - mR^2)/4; F = doublet, B = charge x spin rotor')
def ip(u, v): return Fr(u[0] * v[0] + u[1] * v[1] - u[2] * v[2] - u[3] * v[3], 2)
spin = lambda v: ip(v, v) / 2
add = lambda u, v: tuple(x + y for x, y in zip(u, v))
box = list(itertools.product(range(-4, 5), repeat=4))
F = [v for v in box if (v[0] - v[1]) % 2 == 0 and (v[2] - v[3]) % 2 == 0]
B = [v for v in box if (v[0] - v[2]) % 2 == 0 and (v[1] - v[3]) % 2 == 0]
tw = lambda L, d: sorted({str(spin(add(v, d)) % H) for v in L})
phase = lambda d, v: (-1) ** int(2 * ip(d, v))
zL, zV, cL = (0, 1, 0, 0), (0, 1, 0, -1), (1, 0, 0, 0)
fpar = lambda v: (-1) ** int(2 * spin(v))
dirac = [(p, q) for p in range(-4, 5) for q in range(-4, 5)]
tw_dirac = sorted({str(Fr((2 * p + 1) ** 2 - 4 * q * q, 8) % H) for p, q in dirac})
ok = (tw(F, zV) == ['0'] and tw(F, zL) == ['1/4'] and tw(F, cL) == ['1/4'] and tw_dirac == ['1/8']
      and all(phase(zV, v) == fpar(v) for v in F) and all(phase(zL, v) * phase(cL, v) == 1 for v in F)
      and all(phase(zV, v) == 1 for v in B) and any(phase(zL, v) == -1 for v in B))
check('B1 [T] an on-site SU(2) acts on both chiralities, so its centre flows to z_V = z_L z_R = (-1)^{mL+mR}: on F it is (-1)^F '
      '(twisted spins 0 mod 1/2, Z_8 index 0), on B it is 1. The gluing needs z_L = (-1)^{mL}, which on F is the chiral fermion '
      'parity (-1)^{F_L} of the doublet (twisted spin 1/4 = 4/16: Z_8 index 4; check: (-1)^{F_L} of one Dirac gives 1/8 = 2/16) '
      'and equals the charge half (-1)^{nL} as an operator. So "SU(2) centre = fermion parity" supplies z_V, never z_L',
      ok, f'twisted spins mod 1/2 on F: z_V {tw(F, zV)}, z_L {tw(F, zL)}, charge half {tw(F, cL)}; Dirac (-1)^F_L {tw_dirac}')
prim = [Fr(0), Fr(1, 4)]
sp_su2 = sorted({str((a - b) % 1) for a in prim for b in prim})
res = sorted({(x * x - y * y) % 4 for x in range(4) for y in range(4)})
check('B2 [T] a spin carrier whose gapless sector is one SU(2)_1 per chirality (c = 1) has no fermionic operator: primaries '
      'h in {0, 1/4} give spins in {0, 1/4, 3/4} mod 1 (integer lattice form: mL^2 - mR^2 is never 2 mod 4). Its UV fermion '
      'parity therefore acts as 1 on the whole gapless sector, and charge half x (-1)^{F_s} has the IR image of the charge '
      'half alone (Z_8 index 4): pairing with the fermion parity of a spin-only carrier never makes the gluing local',
      '1/2' not in sp_su2 and 2 not in res, f'spins mod 1 {sp_su2}; mL^2 - mR^2 mod 4 in {res}')

# ================================ C. Hubbard ring ================================
print('== C. half-filled Hubbard ring, t = 1, U = 4, periodic, sector N_up = N_dn = L/2 (dense ED)')
def hubbard(L, nup, ndn, U):
    modes = 2 * L
    basis = [s for s in range(1 << modes) if bin(s & ((1 << L) - 1)).count('1') == nup and bin(s >> L).count('1') == ndn]
    ix = {s: i for i, s in enumerate(basis)}; dim = len(basis)
    def hop(s, a, b):   # c_a^dag c_b
        if not (s >> b) & 1 or ((s >> a) & 1 and a != b): return None, 0
        lo, hi = min(a, b), max(a, b); between = bin(s & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))).count('1')
        return (s ^ (1 << b)) | (1 << a), (-1) ** between
    Hm = np.zeros((dim, dim)); Tm = np.zeros((dim, dim))
    for i, s in enumerate(basis):
        for sg in (0, 1):
            for j in range(L):
                a, b = sg * L + (j + 1) % L, sg * L + j
                for x, y in ((a, b), (b, a)):
                    t_, sgn = hop(s, x, y)
                    if t_ is not None: Hm[ix[t_], i] -= sgn
        Hm[i, i] += U * bin((s & ((1 << L) - 1)) & (s >> L)).count('1')
        occ = [m for m in range(modes) if (s >> m) & 1]; img = [(m // L) * L + (m % L + 1) % L for m in occ]
        perm = sorted(range(len(img)), key=lambda k: img[k]); par = 1
        seen = [False] * len(perm)
        for k in range(len(perm)):
            if not seen[k]:
                c_, cyc = k, 0
                while not seen[c_]: seen[c_] = True; c_ = perm[c_]; cyc += 1
                par *= (-1) ** (cyc - 1)
        Tm[ix[sum(1 << m for m in img)], i] = par
    return basis, ix, Hm, Tm
def splus(L, bA, bB_ix):
    M = np.zeros((len(bB_ix), len(bA)))
    for i, s in enumerate(bA):
        for j in range(L):
            a, b = j, L + j
            if (s >> b) & 1 and not (s >> a) & 1:
                lo, hi = a, b; between = bin(s & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))).count('1')
                M[bB_ix[(s ^ (1 << b)) | (1 << a)], i] += (-1) ** between
    return M
resC = {}
for L in (4, 6):
    bA, ixA, HA, TA = hubbard(L, L // 2, L // 2, 4.0); bB, ixB, _, _ = hubbard(L, L // 2 + 1, L // 2 - 1, 4.0)
    Spl = splus(L, bA, ixB); S2 = Spl.T @ Spl
    E, V = np.linalg.eigh(HA); Sv = [float(V[:, i] @ S2 @ V[:, i]) for i in range(len(E))]
    t1 = next(i for i in range(1, len(E)) if abs(Sv[i] - 2) < 1e-6)
    Tg, Tt = float(V[:, 0] @ TA @ V[:, 0]), float(V[:, t1] @ TA @ V[:, t1])
    resC[L] = (abs(Sv[0]) < 1e-8, round(Tt * Tg, 8), E[t1] - E[0], nrm(TA @ HA - HA @ TA))
check('C1 [T] a fermion-mode spin carrier with its charge gapped is back to Lieb-Schultz-Mattis: in the half-filled Hubbard '
      'ring the on-site centre (-1)^{n_j} multiplies to the c-number (-1)^N, and the lowest triplet carries momentum pi '
      'relative to the singlet ground state, so the IR spin half is lattice translation, not fermion parity',
      all(r[0] and r[1] == -1 and r[3] < 1e-12 for r in resC.values()),
      '; '.join(f'L={L}: T-ratio {r[1]:+.0f}, triplet gap {r[2]:.3f}' for L, r in resC.items()))

# ================================ D. construction ================================
print('== D. carrier: rotor (N, W) [pairing NW\' + WN\', Q = qV N + qA W] (+) fermions Z^4 (L1, L2, R1, R2) [diag(1,1,-1,-1)]')
def blk(qV, qA, v, t3):   # one locking block: Gram, Q covector, 2T3 covector, fermion-number covector
    G = np.zeros((6, 6), dtype=int); G[0, 1] = G[1, 0] = 1; G[2:, 2:] = np.diag([1, 1, -1, -1])
    return G, np.array([qV, qA, v, v, v, v]), np.array([0, 0, t3, -t3, t3, -t3]), np.array([0, 0, 1, 1, 1, 1])
ell = np.array([1, -1, 1, 1, 0, 0])
E4 = [np.array([1, 0, 1, 0, 0, 0]), np.array([1, 0, 0, 1, 0, 0]), np.array([0, 0, 0, 0, 1, 0]), np.array([0, 0, 0, 0, 0, 1])]
fvec = np.array([-1, 0, 0, 0, 0, 0])
blocks = {'doublet': (2, 4, 1, 1), 'singlets': (-2, 4, 3, 0)}
out = {}; okD1 = True
for name, (qV, qA, v, t3) in blocks.items():
    G, Qc, Tc, Fc = blk(qV, qA, v, t3)
    null = int(ell @ G @ ell) == 0; neutral = int(Qc @ ell) == 0 and int(Tc @ ell) == 0
    perp = all(int(e @ G @ ell) == 0 for e in E4); gram = np.array([[int(a @ G @ b) for b in E4] for a in E4])
    basis_det = round(abs(np.linalg.det(np.array(E4 + [ell, fvec], dtype=float))))
    okD1 &= null and neutral and perp and (gram == np.diag([1, 1, -1, -1])).all() and basis_det == 1 and int(fvec @ G @ ell) == 1
    out[name] = ([int(Qc @ e) for e in E4], [int(Tc @ e) for e in E4], [int(Fc @ e) % 2 for e in E4])
Lq = out['doublet'][0][:2] + out['singlets'][0][:2]; Rq = out['doublet'][0][2:] + out['singlets'][0][2:]
Lrep = [(2 if t else 1, q) for q, t in zip(Lq, out['doublet'][1][:2] + out['singlets'][1][:2])]
Rrep = [(2 if t else 1, q) for q, t in zip(Rq, out['doublet'][1][2:] + out['singlets'][1][2:])]
swap = sorted(Lrep) == sorted([(2, 3), (2, 3), (1, 1), (1, 1)]) and sorted(Rrep) == sorted([(2, 1), (2, 1), (1, 3), (1, 3)])
check('D1 [T] locking term ell = (cell pair c_L1^dag c_L2^dag-type, SU(2) singlet, spin 1) x (rotor vertex N = 1, W = -1, '
      'spin -1): null, primitive, Q-neutral, T3-neutral, for the doublet block (vector charge 1, rotor (qV, qA) = (2, 4)) and '
      'the singlet-pair block (vector charge 3, rotor (-2, 4)); the residual ell^perp/ell is spanned by e = (pair-partner x '
      'e^{i phi}, R fermions) with Gram diag(1,1,-1,-1) (unimodular completion, det 1): exactly free Weyl modes with '
      'L = (2,3) + 2(1,1), R = (2,1) + 2(1,3), the swap content (a, b) = (3, 1), every residual mode odd (a fermion)',
      okD1 and swap and all(all(p == 1 for p in o[2]) for o in out.values()), f'L {Lrep}; R {Rrep}')
anom = lambda qs: sum(q * q for q in qs)
rot_anom = 2 * 2 * 4
inv = [(l, r) for l in Lrep for r in Rrep if l[0] == r[0] and any(s1 * l[1] + s2 * r[1] == 0 for s1 in (1, -1) for s2 in (1, -1))]
kL = sum(1 for d, q in Lrep if d == 2) - sum(1 for d, q in Rrep if d == 2)
dq = anom([q for d, q in Lrep if d == 2] ) - anom([q for d, q in Rrep if d == 2])
check('D2 [T] anomalies: U(1)^2 sum_L q^2 - sum_R q^2 = 0, SU(2) doublets L - R = 0, gravity 0; the doublet sector alone carries '
      'U(1)^2 = 16 = 2 qV qA of its rotor (anomaly moved from the rotor onto the doublet by the locking); no L-R pair has equal '
      'SU(2) rep and matching charge, so no invariant bilinear mass: jointly chiral, vector-like under U(1) alone and SU(2) alone; '
      'the UV doublet mass c_L^dag c_R pairs to -1 with ell, so it is disordered in the locked phase',
      anom(Lq) == anom(Rq) and kL == 0 and dq == rot_anom and inv == [] and sorted(Lq) == sorted(Rq)
      and int(np.array([0, 0, -1, 0, 1, 0]) @ blk(2, 4, 1, 1)[0] @ ell) == -1, f'doublet U(1)^2 {dq}, rotor 2 qV qA {rot_anom}')
# gluing on the whole carrier: e^{i pi Q} x (SU(2) centre) = singlet fermion parity, an on-site product
okg = True; cnt = 0
for nf in itertools.product((-1, 0, 1), repeat=8):
    nd_, ns_ = nf[:4], nf[4:]
    for rv in itertools.product((-1, 0, 1), repeat=4):
        Q = 2 * rv[0] + 4 * rv[1] - 2 * rv[2] + 4 * rv[3] + 1 * sum(nd_) + 3 * sum(ns_)
        okg &= (-1) ** (Q % 2) * (-1) ** ((nd_[0] - nd_[1] + nd_[2] - nd_[3]) % 2) == (-1) ** (sum(ns_) % 2); cnt += 1
check('D3 [T] the gluing generator e^{i pi Q} x (SU(2) centre) equals the singlet fermion parity on every carrier state '
      '(rotor charges qV, qA all even, so e^{i pi Q} is 1 on both rotors and no winding parity enters): a product of on-site '
      'commuting involutions, commuting with everything; the anomalous halves z_L and (-1)^{N+W} never appear', okg, f'{cnt} states')

print('== D\'. TPF on the two SU(2)-singlet rotors (exact rationals, inline from su2-disentangler B)')
def rnd(x): return math.floor(x + H)
def f1(x): return x - math.floor(x)
def cp(x): return ([r[:] for r in x[0]], [r[:] for r in x[1]], x[2][:], x[3][:])
def QAw(p, n_): N = len(p); return -sum(rnd(p[(j + 1) % N] - p[j]) + n_[j] for j in range(N))
def sym(x, be, qs):
    y = cp(x); y[0][:] = [[f1(p + qV * be) for p in x[0][a]] for a, (qV, qA) in enumerate(qs)]; y[2][:] = [f1(t + be) for t in x[2]]
    return y, be * sum(qA * QAw(x[0][a], x[1][a]) for a, (qV, qA) in enumerate(qs))
def ylink(ph, n_, th, qs, k):
    N = len(th); return sum(qA * (rnd(ph[al][(k + 1) % N] - ph[al][k] + qV * (th[(k + 1) % N] - th[k])) + n_[al][k]) for al, (qV, qA) in enumerate(qs))
def Xr(ph, qs, k): return rnd(sum(qA * ph[al][k % len(ph[al])] for al, (qV, qA) in enumerate(qs)))
def Phi(ph, n_, th, qs): return -sum(th[k] * (ylink(ph, n_, th, qs, k) - (Xr(ph, qs, k + 1) - Xr(ph, qs, k))) for k in range(len(th)))
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
rng = random.Random(20261022); NB = 5; NT = 120
def rx(F_):
    return ([[Fr(rng.randrange(48), 48) for _ in range(NB)] for _ in range(F_)], [[rng.randrange(-2, 3) for _ in range(NB)] for _ in range(F_)],
            [Fr(rng.randrange(48), 48) for _ in range(NB)], [Fr(0)] * NB)
def ident(qs):
    fails = 0
    for t in range(NT):
        x = rx(len(qs)); be = Fr(rng.randrange(1, 97), 97)
        u = comp(x, [lambda z: Wf(z, qs), lambda z: sym(z, be, qs), lambda z: Wd(z, qs)]); v = cp(x); v[2][:] = [f1(tt + be) for tt in x[2]]
        fails += not (u[0] == v and f1(u[1]) == 0)
    return fails
SETS = {'(2,4)+(-2,4)': [(2, 4), (-2, 4)], '(2,4) alone': [(2, 4)], '(2,4)+(-2,2)': [(2, 4), (-2, 2)], '(-2,4) alone': [(-2, 4)]}
resT = {k: (ident(q), sum(a * b for a, b in q)) for k, q in SETS.items()}
check('D4 [T] TPF disentangler on the two anomaly rotors: W^dag e^{2 pi i b Q} W = e^{2 pi i b Q_anc} exactly when c = sum qV qA '
      '= 8 - 8 = 0; anomalous sets fail (one rotor alone, or a mismatched partner); the fermions\' vector charge is on-site and '
      'untouched by W, and SU(2) acts on the fermions only, so [W, SU(2)] = 0 and the gauged U(1) and SU(2) Gauss laws are '
      'both on-site and commute; the Schwinger term of the U(1) Gauss law is proportional to c (su2-tpf E1), zero here',
      resT['(2,4)+(-2,4)'][0] == 0 and all(f > NT // 4 for k, (f, c) in resT.items() if c != 0),
      '; '.join(f'{k}: c={c}, fails {f}/{NT}' for k, (f, c) in resT.items()))
def K1(x, j):
    N = len(x[2]); y = cp(x); p = x[0][0]; d1 = p[j] - p[(j - 1) % N]; d2 = p[(j + 1) % N] - p[j]
    y[1][0][(j - 1) % N] += rnd(d1) - rnd(d1 + 1); y[1][0][j] += rnd(d2) - rnd(d2 - 1); return y
def Sk(x, k, s): y = cp(x); y[1][0][k] += s; return y
qs1 = [(2, 4)]; chg = {1: set(), -1: set()}; kc = 0
for t in range(NT):
    x = rx(1); j, k, i = rng.randrange(NB), rng.randrange(NB), rng.randrange(NB); be = Fr(rng.randrange(1, 97), 97)
    for s in (1, -1):
        y, p0 = sym(x, be, qs1); z, p1 = sym(Sk(x, k, s), be, qs1)
        if z != Sk(y, k, s): chg[s].add('config')
        dif = x[0][0][j] + p1 - p0 - y[0][0][j]
        chg[s].add(next((q for q in range(-12, 13) if f1(dif - q * be) == 0), None))
    kc += K1(Sk(x, k, 1), i) != Sk(K1(x, i), k, 1)
check('D5 [T] the rotor half of the locking term is local and constraint-invariant: e^{2 pi i phi_j} and the link shift S_k '
      '(n_k -> n_k + s) commute with every Villain constraint K_i(1) and carry exact charges -qV - s qA under TPF\'s symmetry, so '
      'e^{2 pi i phi_j} S_k^{-1} (IR vertex (N, W) = (-1, 1), spin -1) has charge -2 + 4 = 2, cancelled by the cell pair c c',
      kc == 0 and chg[1] == {-6} and chg[-1] == {2}, f'charges s=+1 {sorted(map(str, chg[1]))}, s=-1 {sorted(map(str, chg[-1]))}')
# relevance: embed in R^{3,3}; rotor radius r; an SU(2)-singlet current-current deformation = boost in the null plane
def kvec(v, r):
    N, W_ = v[0], v[1]
    return np.array([(N / r + W_ * r) / math.sqrt(2), v[2], v[3]]), np.array([(N / r - W_ * r) / math.sqrt(2), v[4], v[5]])
Dm = lambda kl, kr: (kl @ kl + kr @ kr) / 2
rs = np.linspace(0.5, 2, 301); dmin = min(Dm(*kvec(ell, r)) for r in rs)
kl, kr = kvec(ell, 1.0); u = kl / np.linalg.norm(kl); w = kr / np.linalg.norm(kr)
def boost(kl, kr, eta):
    xu, xw = kl @ u, kr @ w; nu_, nw_ = math.cosh(eta) * xu - math.sinh(eta) * xw, -math.sinh(eta) * xu + math.cosh(eta) * xw
    return kl + (nu_ - xu) * u, kr + (nw_ - xw) * w
eta = 0.5; bl, br = boost(kl, kr, eta)
cur = np.array([0, 0, 1, -1, 0, 0]); cl, cr = kvec(cur, 1.0); cbl, cbr = boost(cl, cr, eta)
check('D6 [T] at the decoupled free point the locking vertex has dimension >= 2 (minimum 2 at r = 1: marginal); an '
      'SU(2)-singlet, Q-neutral forward-scattering term between the doublet\'s charge current and the rotor is an O(3,3) boost '
      'in the null plane, keeps ell null and the SU(2)_1 currents at h = 1, and lowers the dimension to 2 e^{-2 eta}: relevant',
      abs(dmin - 2) < 1e-6 and abs(Dm(bl, br) - 2 * math.exp(-2 * eta)) < 1e-12 and abs(bl @ bl - br @ br) < 1e-12
      and abs(Dm(cbl, cbr) - 1) < 1e-12 and abs(u[1] - u[2]) < 1e-12,
      f'min dim {dmin:.4f}; boosted (eta = {eta}) {Dm(bl, br):.4f}; SU(2) current dim {Dm(cbl, cbr):.3f}')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('[T] throughout. Supplied: two complex modes per cell for the doublet and per singlet pair, vector charges (1, 3), '
      'two SU(2)-singlet Villain rotors (2,4), (-2,4) with ancillas, the locking couplings and forward scattering; the flow '
      'to the locked phase is cited (Haldane), not computed. Cited: TPF 2601.04304, Else-Nayak, LSM.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

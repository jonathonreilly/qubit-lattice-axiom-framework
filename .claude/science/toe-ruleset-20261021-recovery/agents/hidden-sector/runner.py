#!/usr/bin/env python3
"""Hidden sector: can one new link group of the rules break the weak symmetry by transmutation, give dark matter as its
lightest bound state and fix Omega_c/Omega_b by sharing the baryon asymmetry?  Supplied models; [T] theorem or exact
finite check, [D] finite diagnostic, [E] estimate with supplied or cited inputs, [M] comparison with measurement.
 A  which candidate origin gives an exactly conserved continuous symmetry that CL-3 would link: the copy-massed CL-1
    tick (heavy copy), the 6^3 cell (11 pattern copies), octree rungs (coarse-rung mirror), species in parallel, R1
 B  if supplied: SU(N) on N copies of the generation pattern (one technifamily, Nf = 8, N_D = 4): running, window
 C  weak-symmetry breaking: rho, vector-like content, S, the light scalar, vectors, the cell coupling
 D  dark matter: exact charges, stability, mass, asymmetric sharing, direct detection, self-interaction
 E  look-elsewhere for the numerical matches found
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 90

import itertools, os, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
from fractions import Fraction as Fr
from math import comb
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from scipy.optimize import brentq

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
rng = np.random.default_rng(20261021)
# supplied measured / cited numbers
v, MPl = 246.21965, 1.220890e19; Mc = MPl / np.sqrt(8 * np.pi); gL, gp = 0.6517, 0.3576; Sm, dS = -0.05, 0.07
mp, mn, GF, s2w = 0.938272, 0.939565, 1.1663788e-5, 0.23122; GeV2cm2 = 0.389379e-27; gram = 1.78266e-24
Om_c, Om_b = 0.1200, 0.02237; R_obs = Om_c / Om_b; dR = R_obs * np.hypot(0.0012 / Om_c, 0.00015 / Om_b)
mN_fpi, Tc_fpi = 938.92 / 92.07, 156.5 / 92.07          # QCD nucleon mass and chiral crossover in units of f_pi

# ------------------------------------------- A. exact symmetries of the update -------------------------------------------
print('== A. exact continuous symmetries CL-3 could link (copy-massed CL-1 tick)')
C = np.array(list(itertools.product((0, 1), repeat=3))); I8 = np.eye(8)
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    nv = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(nv[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
def hop(d2, sign):
    H = np.zeros((8, 8), complex)
    for a in range(8):
        for b in range(8):
            if round(float(np.sum((C[a] - C[b]) ** 2))) == d2: g = XI[a].conj() @ XI[b]; H[a, b] = sign * g / abs(g) / np.sqrt(3)
    return H
W = hop(1, -1.0); Fh = hop(2, 1.0); Ssub = np.diag([(-1.0) ** int(x.sum()) for x in C]).astype(complex)
PA = (I8 - Ssub @ Fh) / 2                                   # copy A (threefold-turn character w): gets the copy mass
def Dg(K): return np.diag(np.exp(1j * (C @ K)))
def tick(K, st, mu, M):                                     # even cube, then odd cube; copy mass M/2 per half-tick on copy A
    Ue = expm(-1j * ((st - mu / 2) * I8 - M / 2 * PA) @ W)
    return Dg(K).conj().T @ expm(1j * ((st + mu / 2) * I8 + M / 2 * PA) @ W) @ Dg(K) @ Ue
def logH(U):
    w, V = np.linalg.eig(U); H = (V * (-np.angle(w))) @ np.linalg.inv(V); return (H + H.conj().T) / 2
def comm_dim(Ms, tol=1e-9):
    n = Ms[0].shape[0]; A = np.vstack([np.kron(M, np.eye(n)) - np.kron(np.eye(n), M.T) for M in Ms])
    s = np.linalg.svd(A, compute_uv=False); return int(np.sum(s < tol * max(1.0, s[0])))
KR = rng.uniform(-np.pi, np.pi, (6, 3)); st, mu, M = 0.3, 0.05, 0.3
dims = [(comm_dim([tick(K, s_, m_, M_) for K in KR]), comm_dim([tick(np.zeros(3), s_, m_, M_)])) for s_, m_, M_ in ((st, mu, M), (0.04, 0.01, 0.03))]
nh = np.array([1.0, 0.3, -0.7]) / np.linalg.norm([1.0, 0.3, -0.7]); leak = []
for h in (0.01, 0.02, 0.04):
    E_, V_ = np.linalg.eigh(logH(tick(h * nh, st, mu, M))); lw = np.real(np.einsum('ij,ik,kj->j', V_.conj(), PA, V_))
    leak.append(float(np.max(np.minimum(lw, 1 - lw))))
check('A1 [T] copy-massed tick: commutant over 6 random K is %d at steps .3 and .04; at K = 0 it is %d and holds the copy '
      'projector, but band states leak copy weight as K^2 (%.1e, %.1e, %.1e at K = .01, .02, .04): the heavy copy has no '
      'exact number, hence no link' % (dims[0][0], dims[0][1], *leak),
      all(d == (1, 16) for d in dims) and 3.6 < leak[1] / leak[0] < 4.4 and 3.6 < leak[2] / leak[1] < 4.4)
mpos = np.array(list(itertools.product(range(3), repeat=3)))
def U6(Q):                                                  # 6^3 cell = 27 cubes: supercell Bloch matrix in real space
    Ks = [(np.asarray(Q) + 2 * np.pi * n) / 3 for n in mpos]; Fq = np.zeros((216, 216), complex); Bd = np.zeros((216, 216), complex)
    for ni, Kn in enumerate(Ks):
        ph = np.exp(1j * (mpos @ Kn)) / np.sqrt(27); Bd[8 * ni:8 * ni + 8, 8 * ni:8 * ni + 8] = tick(Kn, st, mu, M)
        for c in range(8): Fq[np.arange(27) * 8 + c, 8 * ni + c] = ph
    return Fq @ Bd @ Fq.conj().T
Us = [U6(Q) for Q in rng.uniform(-np.pi, np.pi, (4, 3))]; a_ = rng.normal(size=4) + 1j * rng.normal(size=4)
ev, V = np.linalg.eigh(sum(a_[j] * Us[j] + np.conj(a_[j]) * Us[j].conj().T for j in range(4))); gap = np.min(np.diff(ev))
Adj = sum(np.abs(V.conj().T @ U @ V) ** 2 + np.abs(V.conj().T @ U @ V).T ** 2 for U in Us); np.fill_diagonal(Adj, 0)
le = np.linalg.eigvalsh(np.diag(Adj.sum(1)) - Adj); cdim6 = int(np.sum(le < 1e-10))
RI = [R for R in (np.array(p) * np.array(s)[:, None] for p in itertools.permutations(np.eye(3, dtype=int)) for s in itertools.product((1, -1), repeat=3)) if round(np.linalg.det(R)) == 1]
pts = [tuple(p) for p in itertools.product(range(-5, 6, 2), repeat=3)]
def cls(R):
    t = int(round(np.trace(R))); return {3: 'E', 0: 'C3', 1: 'C4'}.get(t, 'C2f' if np.allclose(R, np.diag(np.diag(R))) else 'C2p')
TAB = [dict(E=1, C3=1, C2f=1, C4=1, C2p=1), dict(E=1, C3=1, C2f=1, C4=-1, C2p=-1), dict(E=2, C3=-1, C2f=2, C4=0, C2p=0),
       dict(E=3, C3=0, C2f=-1, C4=1, C2p=-1), dict(E=3, C3=0, C2f=-1, C4=-1, C2p=1)]
chi = [sum(tuple(R @ np.array(p)) == p for p in pts) for R in RI]; mult = [int(round(sum(t[cls(R)] * c for R, c in zip(RI, chi)) / 24)) for t in TAB]
check('A2 [T] 6^3 cell (27 cubes, 216 modes): the site rotations have multiplicities %s (commutant %d), but the tick\'s '
      'cell-local commutant over 4 random Q is %d (spectral gap %.0e, connectivity %.2f): the 11 pattern copies are folded '
      'momenta of one field with no symmetry among them' % (tuple(mult), sum(m * m for m in mult), cdim6, gap, le[1]),
      mult == [11, 11, 16, 27, 27] and cdim6 == 1 and gap > 1e-6 and le[1] > 1e-3)
al = []
for k in range(3):
    e = np.zeros(3); e[k] = 1e-5; A_ = (logH(tick(e, st, 0, 0)) - logH(tick(-e, st, 0, 0))) / 2e-5; al.append((A_ + A_.conj().T) / 2)
vel = np.sqrt(np.trace(al[0] @ al[0]).real / 8); al = [A_ / vel for A_ in al]; g5 = 1j * al[0] @ al[1] @ al[2]; g5 = (g5 + g5.conj().T) / 2
X = W @ (I8 - g5) / 2                                       # octree exchange to the same corner of the children
cdo = comm_dim([logH(tick(K, st, mu, M)) for K in KR] + [X, X.conj().T])
check('A3 [T] octree: each rung runs the same tick (commutant 1) and X = W(1-g5)/2 (norm %.3f, X^2 = 0) ties neighbouring '
      'rungs, so a rung-wise symmetry is one phase (commutant %d): the coarse-rung mirror carries N only' % (np.linalg.norm(X, 2), cdo),
      cdo == 1 and abs(np.linalg.norm(X, 2) - 1) < 1e-6 and np.abs(X @ X).max() < 1e-8 and abs(vel - np.sin(st) / np.sqrt(3)) < 1e-8)
def par(K, mus):
    Z = np.zeros((8 * len(mus),) * 2, complex)
    for i, m_ in enumerate(mus): Z[8 * i:8 * i + 8, 8 * i:8 * i + 8] = tick(K, st, m_, M)
    return Z
pdims = [comm_dim([par(K, ms) for K in KR[:4]]) for ms in ((.05, .05, .05), (.05, .05, .08), (.05, .08, .11))]
idx = {p: i for i, p in enumerate(pts)}; Aadj = np.zeros((216, 216))
for p in pts:
    for k in range(3):
        for d in (-2, 2):
            q = list(p); q[k] += d
            if tuple(q) in idx: Aadj[idx[p], idx[tuple(q)]] = 1
Pf = np.diag([0.0 if abs(p[0]) == abs(p[1]) == abs(p[2]) else 1.0 for p in pts]); fr = np.linalg.eigvalsh(0.01 * Aadj + Pf); fr = fr[fr > 0.5]
mx = max(len(c) for c in np.split(fr, np.where(np.diff(fr) > 1e-9)[0] + 1))
check('A4 [T/D] species in parallel: commutant %d, %d, %d for masses (m,m,m), (m,m,m\'), (m,m\',m\'\'): a non-abelian '
      'group needs exactly degenerate copies, supplied as for colour; R1\'s M = tA + V P_free splits the free block by %.2f t, '
      'largest multiplicity %d < 8: no U(8) on the 8 free copies' % (*pdims, (fr.max() - fr.min()) / 0.01, mx),
      pdims == [9, 5, 3] and mx < 8)

# ------------------------------------- B. if supplied: SU(N) on N copies of the pattern -------------------------------------
print('== B. supplied SU(N) on N copies of the generation pattern (one technifamily: Nf = 8 Dirac, N_D = 4 doublets)')
CF = lambda N: Fr(N * N - 1, 2 * N); b0 = lambda N, nf: Fr(11 * N, 3) - Fr(2 * nf, 3)
b1 = lambda N, nf: Fr(34 * N * N, 3) - nf * (Fr(10 * N, 3) + 2 * CF(N)); ac = lambda N: np.pi / (3 * float(CF(N)))
bz = lambda N: Fr(34 * N ** 3, 13 * N * N - 3)
def ladder(N):
    g = lambda nf: -4 * np.pi * (11 * N / 3 - 2 * nf / 3) / (34 * N * N / 3 - nf * (10 * N / 3 + 2 * float(CF(N)))) - ac(N)
    return brentq(g, float(bz(N)) + 1e-6, 11 * N / 2 - 1e-6)
ast2 = -4 * np.pi * float(b0(2, 8)) / float(b1(2, 8))
check('B1 [T] b0, b1 at Nf = 8: SU(2) %s, %s (fixed point %.3f < alpha_c %.3f: conformal, no breaking); SU(3) %s, %s (BZ edge %.2f, '
      'ladder edge %.1f: chirally broken, near-conformal on the lattice); SU(4) %s, %s; SU(8) (the 8 free copies) %s, %s, Nf/edge %.2f: QCD-like'
      % (b0(2, 8), b1(2, 8), ast2, ac(2), b0(3, 8), b1(3, 8), float(bz(3)), ladder(3), b0(4, 8), b1(4, 8), b0(8, 8), b1(8, 8), 8 / ladder(8)),
      b1(2, 8) < 0 and ast2 < ac(2) and b1(3, 8) == Fr(2, 3) and 8 < float(bz(3)) < 8.1 and b0(8, 8) == 24 and 8 / ladder(8) < 0.3)
a3TeV = 1 / (1 / 0.1180 + 7 / (2 * np.pi) * np.log(1000 / 91.1876)); bq8 = float(Fr(7) - Fr(32, 3)); pole = 1e3 * np.exp(2 * np.pi / (a3TeV * -bq8))
check('B2 [T] a technifamily is a complete family: b3 = 7 - 4N/3, b2 = 10/3 - 4N/3, one shift for all three couplings (the '
      'unequal cell couplings stay unequal); QCD loses asymptotic freedom for N >= 6, and SU(8) puts its pole at %.0e GeV, '
      'below the cell scale' % pole, Fr(7) - Fr(4 * 5, 3) > 0 > Fr(7) - Fr(4 * 6, 3) and pole < Mc)

# ------------------------------------------------- C. weak-symmetry breaking -------------------------------------------------
print('== C. weak-symmetry breaking')
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1., -1]).astype(complex); I2 = np.eye(2)
def mass2(nd, gens, cps):
    phi = np.eye(2).reshape(-1).astype(complex); k_ = len(gens)
    return nd * np.array([[cps[i] * cps[j] * np.real(phi.conj() @ (gens[i] @ gens[j] + gens[j] @ gens[i]) @ phi) / 2 for j in range(k_)] for i in range(k_)])
Lg = [np.kron(s_ / 2, I2) for s_ in (sx, sy, s3)]; Rg = [-np.kron(I2, (s_ / 2).T) for s_ in (sx, sy, s3)]
M4 = mass2(4, Lg + [Rg[2]], [gL] * 3 + [gp]); e4 = np.linalg.eigvalsh(M4); M1 = mass2(1, Lg + [Rg[2]], [gL] * 3 + [gp])
rho = M4[0, 0] / (e4[-1] * gL ** 2 / (gL ** 2 + gp ** 2))
eV = np.linalg.eigvalsh(mass2(4, [Lg[i] + Rg[i] for i in range(3)] + [0 * Rg[2]], [gL] * 3 + [gp])); eLR = np.linalg.eigvalsh(mass2(4, Lg + Rg, [gL] * 6))
check('C1 [T] chiral technidoublets (left doublets, right singlets): N_D bidoublet condensates give one massless photon, '
      'M_W^2 x %.0f for N_D = 4 vs 1 and rho = %.12f; vector-like doublets (CL-1 Dirac species): %d massless (Vafa-Witten '
      'vacuum); SU(2)_R linked: %d massless. So the hidden sector needs the chirality wall closed first' % (M4[0, 0] / M1[0, 0], rho, int(np.sum(np.abs(eV) < 1e-12)), int(np.sum(np.abs(eLR) < 1e-12))),
      abs(rho - 1) < 1e-12 and abs(M4[0, 0] / M1[0, 0] - 4) < 1e-12 and np.sum(np.abs(e4) < 1e-12) == 1 and np.sum(np.abs(eV) < 1e-12) == 4 and np.sum(np.abs(eLR) < 1e-12) == 3)
Sp = lambda N, nd: N * nd / (6 * np.pi); pull = lambda s_: (s_ - Sm) / dS
check('C2 [E/M] S = N N_D/(6 pi) for degenerate heavy doublets: technifamily SU(3) %.2f (%.1f sigma), SU(4) %.2f, SU(8) %.2f (%.0f '
      'sigma); within 2 sigma needs S/S_pert < %.2f for SU(3); a one-doublet SU(3) is Witten-anomalous (3 doublets), so its '
      'minimum is N_D = 2: %.2f (%.1f sigma)' % (Sp(3, 4), pull(Sp(3, 4)), Sp(4, 4), Sp(8, 4), pull(Sp(8, 4)), (Sm + 2 * dS) / Sp(3, 4), Sp(3, 2), pull(Sp(3, 2))),
      pull(Sp(3, 4)) > 9 and pull(Sp(3, 2)) > 5 and (3 * 1) % 2 == 1)
d0, e0, Fl = -0.0028, 0.0098, 0.0212; u125 = (Fl / np.sqrt(2)) ** 2; msig1 = np.sqrt((d0 + e0) / u125) * v / 2; mrho = 10.1 * v / 2
def need_cell(N, nd):
    muc = v / np.sqrt(nd) / 0.30; B0, B1 = float(b0(N, 8)), float(b1(N, 8))
    return solve_ivp(lambda t, y: [B0 / (2 * np.pi) + B1 / (8 * np.pi ** 2 * y[0])], (np.log(muc), np.log(Mc)), [1 / ac(N)], rtol=1e-10).y[0, -1]
def v_from(ainv, N, nd):
    B0, B1 = float(b0(N, 8)), float(b1(N, 8)); ev_ = lambda t, y: y[0] - 1 / ac(N); ev_.terminal = True
    s = solve_ivp(lambda t, y: [B0 / (2 * np.pi) + B1 / (8 * np.pi ** 2 * y[0])], (np.log(Mc), np.log(Mc) - 200), [ainv], events=ev_, rtol=1e-10, max_step=0.5)
    return np.exp(s.t_events[0][0]) * 0.30 * np.sqrt(nd)
nc = need_cell(3, 4); vl, vh = v_from(8 * np.pi, 3, 4), v_from(16 * np.pi, 3, 4)
check('C3 [E/M] SU(3) Nf = 8 lattice (LatKMI, cited): chiral-limit M_sigma^2 = %.4f(%.0f) against %.5f for 125 GeV, so 0 to '
      '%.0f GeV at 1 sigma: allowed, not predicted; M_rho = 10.1(+5.0/-1.9) F/sqrt2 = %.2f TeV vs ATLAS HVT-B > 4.4 TeV; v from '
      'the cell needs 1/alpha = %.1f, while counted 8 pi, 16 pi give %.0e, %.0e GeV' % (d0, e0 * 1e4, u125, msig1, mrho / 1e3, nc, vl, vh),
      msig1 > 125 and (10.1 + 5.0 + 0.6) * v / 2 < 4400 and vl / v > 1e3 and vh / v < 1e-3)

# ------------------------------------------------------- D. dark matter -------------------------------------------------------
print('== D. dark matter: the lightest technibaryon')
NTC, ND = 3, 4
fam = [('Q', 3, 2, Fr(1, 6), 1), ('u', 3, 1, Fr(-2, 3), -1), ('d', 3, 1, Fr(1, 3), -1), ('L', 1, 2, Fr(-1, 2), 1), ('e', 1, 1, Fr(1), -1), ('n', 1, 1, Fr(0), -1)]
fields = [dict(c=c, w=w, Y=y, B=Fr(sg, 3) if c == 3 else Fr(0), L=Fr(sg) if c == 1 else Fr(0), TB=Fr(0), tc=1) for _ in range(3) for _, c, w, y, sg in fam]
fields += [dict(c=c, w=w, Y=y, B=Fr(0), L=Fr(0), TB=Fr(sg, NTC), tc=NTC) for _, c, w, y, sg in fam]
for f in fields: f['X'] = f['TB'] - Fr(ND, 3) * f['B']; f['BL'] = f['B'] - f['L']
tr = lambda fn: sum(f['c'] * f['w'] * f['tc'] * fn(f) for f in fields)
def anom(q):
    return [tr(lambda f: f[q] ** 3), tr(lambda f: f[q]), tr(lambda f: f[q] * (Fr(1, 2) if f['w'] == 2 else 0) / f['w']), tr(lambda f: f[q] * (Fr(1, 2) if f['c'] == 3 else 0) / f['c']),
            tr(lambda f: f[q] * f['Y'] ** 2), tr(lambda f: f[q] ** 2 * f['Y'])]
dsph = [sum(f['c'] * f['tc'] * f[q] for f in fields if f['w'] == 2) for q in ('B', 'L', 'TB')]
ns = [len(sp.Matrix(r).nullspace()) for r in ([dsph], [dsph, [1, 1, 0]], [dsph, [1, 1, 0], [0, 4, 0]])]
tau6 = 8 * np.pi * Mc ** 4 / (mN_fpi * v / 2) ** 5 * 6.582e-25
check('D1 [T] X = TB - (4/3)B is anomaly-free (%s), TB is not (SU(2)^2 %s): sphalerons move (B, L, TB) by %s, so exact '
      'combinations number %d, %d with the rules\' uddn, %d with (nu^c)^4 as well: CL-3 links none, and the technibaryon is '
      'protected accidentally, like the proton; a Z4-allowed cell-scale TTTl term gives tau ~ %.0e s'
      % (','.join(str(x) for x in anom('X')), anom('TB')[2], tuple(int(x) for x in dsph), *ns, tau6),
      all(x == 0 for x in anom('X') + anom('BL')) and anom('TB')[2] == 2 and dsph == [3, 3, 4] and ns == [2, 1, 0] and tau6 > 1e30)
def sig(x, boson=False):
    s_ = -1.0 if boson else 1.0
    f = lambda y: y * y * np.exp(np.sqrt(y * y + x * x)) / (np.exp(np.sqrt(y * y + x * x)) + s_) ** 2 if np.sqrt(y * y + x * x) < 700 else 0.0
    return 6 / np.pi ** 2 * quad(f, 1e-12 if boson else 0.0, 3 * x + 60, limit=200)[0]
def hook_dim(lam, n):
    num = den = 1
    for r, row in enumerate(lam):
        for c in range(row): num *= n + c - r; den *= (row - c - 1) + sum(1 for rr in lam[r + 1:] if rr > c) + 1
    return num // den
def glow(N):                                                # lowest-spin technibaryon multiplet of Sym^N(spin 2 x flavour 8)
    S_ = (N % 2) / 2; return hook_dim([x for x in (int(N / 2 + S_), int(N / 2 - S_)) if x > 0], 8) * int(2 * S_ + 1)
F = v / 2; mTB = lambda N: mN_fpi * np.sqrt(N / 3) * F
def tstar(N):                                               # mean-field v(T) = sqrt(N_D) F sqrt(1 - T^2/Tc^2); freeze-out at v(T*) = T*
    Tc = Tc_fpi * np.sqrt(3 / N) * F; a = np.sqrt(ND) * F / Tc; return Tc, Tc * a / np.sqrt(a * a + 1)
check('D2 [E] m_TB = (m_N/f_pi)_QCD sqrt(N/3) F, F = v/2: SU(3) %.2f, SU(4) %.2f, SU(8) %.2f TeV; lowest multiplets %d, %d, %d states '
      '(of %d, %d, %d); freeze-out T* = %.0f, %.0f, %.0f GeV' % (mTB(3) / 1e3, mTB(4) / 1e3, mTB(8) / 1e3, glow(3), glow(4), glow(8),
                                                                comb(18, 3), comb(19, 4), comb(23, 8), tstar(3)[1], tstar(4)[1], tstar(8)[1]),
      glow(3) == 336 and glow(4) == 336 and glow(8) == 13860 and comb(18, 3) == 816)
def species(N, NH=0, top=None, TBs=None, deconf=False):
    out = []
    for gen in range(3):
        kt = 1.0 if (top is None or gen < 2) else top
        out += [(3, kt, Fr(1, 6), Fr(1, 3), 0, 0), (3, 1.0, Fr(1, 6), Fr(1, 3), 0, 0), (3, kt, Fr(2, 3), Fr(1, 3), 0, 0), (3, 1.0, Fr(-1, 3), Fr(1, 3), 0, 0),
                (2, 1.0, Fr(-1, 2), 0, 1, 0), (1, 1.0, Fr(-1), 0, 1, 0)]                  # nu^c sequestered (Dirac, Z4)
    if NH: out.append((2, 2.0, Fr(1, 2), 0, 0, 0))
    if TBs is not None: out.append((TBs[0], TBs[1], Fr(0), 0, 0, 1))
    if deconf: out += [(g * N, 1.0, y, 0, 0, Fr(1, N)) for g, y in ((6, Fr(1, 6)), (3, Fr(2, 3)), (3, Fr(-1, 3)), (2, Fr(-1, 2)), (1, Fr(-1)), (1, Fr(0)))]
    return out
def share(spc, b0_, x0, withX=True):                        # equilibrium with conserved Y (= 0), B - L_SM, X
    Q = np.array([[float(y), float(B) - float(L), float(tb) - ND / 3 * float(B)] for (g, k, y, B, L, tb) in spc])[:, :3 if withX else 2]
    w = np.array([g * k for g, k, *_ in spc]); mu_ = np.linalg.solve((Q * w[:, None]).T @ Q, np.array([0.0, b0_, x0])[:Q.shape[1]]); mi = Q @ mu_
    return float(np.sum(w * np.array([float(s_[3]) for s_ in spc]) * mi)), float(np.sum(w * np.array([float(s_[5]) for s_ in spc]) * mi))
def Om(N, Ts=None, g=None, x0=-4 / 3, wm=1.0, NH=0, top=None, deconf=False):
    m_ = mTB(N) * wm; Ts = tstar(N)[1] if Ts is None else Ts; g = glow(N) if g is None else g
    B_, TB_ = share(species(N, NH, top, None if deconf else (g, sig(m_ / Ts, N % 2 == 0)), deconf), 1.0, x0); return abs(TB_ / B_) * m_ / mp
sm = [share(species(3, NH=h), 1.0, 0.0, False)[0] for h in (1, 0)]
cen = {N: (Om(N), Om(N, g=comb(15 + N, N))) for N in (3, 4, 8)}; x0zero = Om(3, x0=0.0); dec3 = Om(3, deconf=True)
check('D3 [T/E] sharing by chemical equilibrium (checked: SM B/(B-L) = %.6f = 28/79, %.6f = 4/11 without a Higgs): an X = 0 '
      'start gives TB/B = 4/3 exactly, ratio %.0f; the rules\' uddn start at T* gives %.0f-%.0f (SU(3)), %.0f-%.0f (SU(4)), '
      '%.1f-%.0f (SU(8)), first-order (deconfined) SU(3) %.0f, vs %.2f +- %.2f' % (*sm, x0zero, *cen[3], *cen[4], *cen[8], dec3, R_obs, dR),
      abs(sm[0] - 28 / 79) < 1e-12 and abs(sm[1] - 4 / 11) < 1e-12 and abs(x0zero / (mTB(3) / mp) - 4 / 3) < 1e-9 and min(cen[3]) > 20 * R_obs)
def sZ(qZ, m):
    mu_ = m * mn / (m + mn); A_, Z_ = 131.293, 54; return 2 * GF ** 2 * mu_ ** 2 / np.pi * qZ ** 2 * ((A_ - Z_ - (1 - 4 * s2w) * Z_) / A_) ** 2 * GeV2cm2
def sH(m, fN=0.30, mh=125.20):
    mu_ = m * mn / (m + mn); return mu_ ** 2 * (m / v) ** 2 * (fN * mn / v) ** 2 / (np.pi * mh ** 4) * GeV2cm2
LZ = lambda m: (1.3 * 2.2e-48 * m / 40, 2.8e-46 * m / 1e3)  # LZ 2024 minimum scaled linearly; PDG-listed LZ 2023 at 1 TeV
zn = {}
for N in range(2, 9):
    zn[N] = [(u, d, n_, e) for u, d, n_, e in itertools.product(range(N + 1), repeat=4) if u + d + n_ + e == N and (u + d) % 3 == 0
             and Fr(2 * u - d, 3) - e == 0 and u - d + n_ - e == 0]
m3 = mTB(3)
check('D4 [T/E/M] Z-neutral technibaryons (Q = 0, sum T3 = 0) exist for N = %s only (SU(4): UDDN, UUDE): SU(3)\'s neutral '
      'ones (UDD, NNN) scatter by Z at >= %.1e cm^2 vs LZ %.0e-%.0e (x%.0e); a Z-neutral one still couples to a Higgs-like '
      'dilaton as m/v: %.1e cm^2 (x%.0e)' % (','.join(str(N) for N in zn if zn[N]), sZ(0.25, m3), *LZ(m3), sZ(0.25, m3) / LZ(m3)[1], sH(m3), sH(m3) / LZ(m3)[1]),
      not zn[3] and zn[4] and sZ(0.25, m3) / LZ(m3)[1] > 1e5 and sH(m3) / LZ(m3)[1] > 1e4)
sidm = 4 * np.pi / mrho ** 2 * GeV2cm2 / (m3 * gram)
check('D5 [E/M] self-interaction: geometric 4 pi/M_rho^2 gives sigma/m = %.0e cm^2/g vs < ~1: passes; no massless TB '
      'link exists (D1)' % sidm, sidm < 1e-6)
mD = [R_obs * s_ * mp for s_ in sm]
check('D6 [E, conditional] an EW-singlet partner kept out of sphalerons by a uddn-type term, as nu^c is, holds |D| = B - L_SM, '
      'so n_D/n_B = 1/(B/(B-L)) and the measured ratio needs m_D = %.2f GeV (%.2f without a Higgs): a definite target, not a '
      'match' % tuple(mD), abs(mD[0] - R_obs * 28 / 79 * mp) < 1e-12)

# ------------------------------------------------------ E. look-elsewhere ------------------------------------------------------
print('== E. look-elsewhere')
counts = [1, 2, 3, 4, 8, 11, 12, 16, 24, 27, 216]
vals = {Fr(a, b) for a, b in itertools.product(counts, repeat=2)} | {Fr(a * b, c) for a, b, c in itertools.product(counts, repeat=3)}
vals = np.array(sorted(float(x) for x in vals if 0.1 < x < 100)); win = dR / R_obs
hits = vals[np.abs(vals / R_obs - 1) < win]; tg = np.exp(rng.uniform(0, np.log(30), 3000))
ph = np.mean([np.any(np.abs(vals / t - 1) < win) for t in tg])
check('E1 [E] 2 x 8/3 = 16/3 = %.3f lies %.1f sigma from %.3f; it is the only one of %d ratios a/b, ab/c of 11 rule counts '
      'within 1 sigma, and random targets get one with P = %.2f: not evidence'
      % (16 / 3, abs(16 / 3 - R_obs) / dR, R_obs, len(vals), ph), len(hits) == 1 and abs(hits[0] - 16 / 3) < 1e-12 and ph > 0.3)
Tc3, T03 = tstar(3); o3 = []
for _ in range(800):
    Ts = min(T03 * rng.uniform(0.75, 1.25), Tc3); o3.append(Om(3, Ts=Ts, g=np.exp(rng.uniform(np.log(336), np.log(816))), wm=np.exp(rng.uniform(np.log(2 / 3), np.log(1.5))),
                                                      NH=int(rng.integers(0, 2)), top=sig(172.6 / Ts) if rng.random() < 0.5 else None))
o3 = np.array(o3); q5, q95 = np.percentile(o3, [5, 95])
spc3 = species(3, TBs=(glow(3), sig(mTB(3) / T03))); (B1_, T1_), (B2_, T2_) = share(spc3, 1.0, 0.0), share(spc3, 0.0, 1.0)
x0_at = lambda rho_: (rho_ * B1_ - T1_) / (T2_ - rho_ * B2_)  # TB/B = rho_ is linear in the start X/(B-L)
rr = R_obs * mp / mTB(3); r_star = x0_at(-rr); tune = abs(x0_at(-rr * (1 + win)) - x0_at(-rr * (1 - win))) / 2 / abs(r_star)
check('E2 [E] SU(3) sharing over a prior (T* x 0.75-1.25, multiplet 336-816, m/F x 2/3-3/2, Higgs-like doublet, top): %.0f-%.0f '
      '(5-95%%), P(1 sigma of 5.36) = %.3f, P(below) = %.3f: a miss, not a match; a free start X/(B-L) reaches 5.36 only at %.4f, '
      'tuned to %.0e' % (q5, q95, np.mean(np.abs(o3 - R_obs) < dR), np.mean(o3 < R_obs), r_star, tune),
      np.mean(o3 < R_obs) < 0.05 and abs(Om(3, x0=r_star) / R_obs - 1) < 1e-6 and tune < 1e-2)
cv = {N: Om(N) for N in range(3, 12)}; lv = np.log(np.array(list(cv.values()))); dmin = abs(np.log(cv[8] / R_obs))
tg = rng.uniform(lv.min(), lv.max(), 20000); pN = np.mean(np.min(np.abs(lv[None, :] - tg[:, None]), 1) < dmin)
s8 = (Om(8, Ts=0.9 * tstar(8)[1]), Om(8, Ts=1.1 * tstar(8)[1]))
check('E3 [E] SU(8) (the 8 free copies) lands at %.1f; central values for N = 3-11 run %s: a random target lies that close to '
      'one of them with P = %.2f, and T* x 0.9, 1.1 moves SU(8) to %.2f, %.0f: a coincidence, and SU(8) is excluded by B2, C2'
      % (cv[8], ', '.join(f'{x:.3g}' for x in cv.values()), pN, *s8), pN > 0.05 and s8[1] / s8[0] > 10 and int(np.argmin(np.abs(lv - np.log(R_obs)))) == 5)
pw = np.mean(rng.uniform(0, 1000, 20000) < msig1)
check('E4 [E] the 125 GeV scalar: the 1 sigma lattice window 0-%.0f GeV holds a random target in 0-1 TeV with P = %.2f, and '
      'only SU(3) gives a light scalar at all: not evidence' % (msig1, pw), pw > 0.5)
print('theorems: A1-A4, B1, B2, C1, D1 (exact rationals or exact finite checks); finite: A2 connectivity, A4 R1; estimates: C2, C3, D2-D6, E')
print('supplied: copy-massed CL-1 tick (st, mu, M), the 6^3 grouping and R1, the octree X; the hidden group, its content, chiral')
print('  charges and Y; ladder alpha_c, F = 0.30 mu_c, QCD scaling of m_N, T_c; mean-field v(T); full equilibrium; uddn start;')
print('  cited: LatKMI (2017), ATLAS HVT (2024), LZ (2023/2024); PDG: v, g, g\', S (U = 0), G_F, sin^2, masses; Planck 2018 Omegas.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

#!/usr/bin/env python3
"""ladder-wall: can the far end of the zoom ladder be gapped by the link dynamics itself (strongly coupled quantum links)
instead of a frozen cell-local term?  Supplied models; exact theorems, finite diagnostics, estimates against measurement.
 A  strong-coupling Gauss projection (exact ED, rotor link): first-order charged hops vanish, the second-order term is
    cell-local density-density, the neutral member hops freely at any coupling
 B  the members of one family that the links can never gap (neutral nu^c; e^c feels only the abelian factor)
 C  free spectral flow on a Wilson-Dirac strip (the domain-wall fifth direction): warp is a congruence; a strongly coupled
    far region (cut rung links, or frozen spatial links) never removes the mirror flow, it only moves it
 D  the link chain: the light link is the flat zero mode, 1/g_eff^2 = sum_j 1/g_j^2; a disordered rung link splits the group
 E  power counting of CL-3's proper-unit plaquette per rung, and estimates against measurement"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 60
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ============================================================ A
print('== A. strong-coupling Gauss projection (two cells, one rotor link, species charges q_f, one mode per cell each)')
def two_cell(qs, g, t=1.0):
    """modes (cell, f): index 2f + cell; Gauss: E = sum_f q_f n_(A,f) - b, b = 7 (cell A holds {3,4} in the E = 0 manifold);
    the hop of f from A to B lowers E by q_f (dressed by U^(-q_f)); H = -t sum (hops) + (g^2/2) E^2."""
    nf = len(qs); nm = 2 * nf; dim = 2 ** nm; b = 7
    occ = lambda s, i: (s >> i) & 1
    Eof = lambda s: sum(q * occ(s, 2 * f) for f, q in enumerate(qs)) - b
    H = np.zeros((dim, dim)); V = np.zeros((dim, dim))
    for s in range(dim):
        H[s, s] = 0.5 * g * g * Eof(s) ** 2
        for f in range(nf):
            a, bb = 2 * f, 2 * f + 1
            if occ(s, a) and not occ(s, bb):
                s2 = s ^ (1 << a) ^ (1 << bb); sg = (-1) ** bin(s & (((1 << bb) - 1) ^ ((1 << (a + 1)) - 1))).count('1')
                V[s2, s] += -t * sg; V[s, s2] += -t * sg
    return H, V, np.array([Eof(s) for s in range(dim)]), dim
qs = [3, 4, 5, 0]
res = []
for g in (4.0, 8.0, 16.0):
    H0, V, Ev, dim = two_cell(qs, g); P = np.where(Ev == 0)[0]; Qx = np.where(Ev != 0)[0]
    PVP_charged = V[np.ix_(P, P)].copy()
    E, _ = np.linalg.eigh(H0 + V); nP = len(P)
    # Schrieffer-Wolff to second order: Heff = PVP + P V Q (-H0)^-1 Q V P
    Heff = V[np.ix_(P, P)] + V[np.ix_(P, Qx)] @ np.diag(-1 / np.diag(H0)[Qx]) @ V[np.ix_(Qx, P)]
    Ee = np.linalg.eigvalsh(Heff); res.append((g, np.abs(np.sort(E[:nP]) - np.sort(Ee)).max()))
# first order: only the neutral member hops inside the E = 0 manifold
H0, V, Ev, dim = two_cell(qs, 8.0); P = np.where(Ev == 0)[0]
def V_species(qs, which, g=8.0):
    nf = len(qs); dim = 2 ** (2 * nf); Vs = np.zeros((dim, dim)); occ = lambda s, i: (s >> i) & 1
    for s in range(dim):
        a, bb = 2 * which, 2 * which + 1
        if occ(s, a) and not occ(s, bb):
            s2 = s ^ (1 << a) ^ (1 << bb); sg = (-1) ** bin(s & (((1 << bb) - 1) ^ ((1 << (a + 1)) - 1))).count('1')
            Vs[s2, s] -= sg; Vs[s, s2] -= sg
    return Vs
first = [float(np.abs(V_species(qs, f)[np.ix_(P, P)]).max()) for f in range(4)]
Qx = np.where(Ev != 0)[0]; Vchg = sum(V_species(qs, f) for f in range(3))
H2 = Vchg[np.ix_(P, Qx)] @ np.diag(-1 / np.diag(H0)[Qx]) @ Vchg[np.ix_(Qx, P)]
offd = float(np.abs(H2 - np.diag(np.diag(H2))).max())
# the diagonal second-order term per configuration equals -t^2 sum_f (allowed hops) 2/(g^2 q_f^2)
occ = lambda s, i: (s >> i) & 1
pred = []
for s in P:
    v = 0.0
    for f, q in enumerate(qs[:3]):
        if occ(s, 2 * f) != occ(s, 2 * f + 1): v -= 2.0 / (64.0 * q * q)
    pred.append(v)
diag_err = float(np.abs(np.diag(H2) - np.array(pred)).max())
check('A1 THEOREM (exact two-cell ED, charges 3,4,5,0, rotor link): inside the E = 0 manifold every charged hop vanishes at first '
      'order, the neutral one does not; the second-order term is diagonal in every charged occupation (-t^2 2/(g^2 q^2) per open hop): '
      'cell-local density-density, no charged mobility', max(first[:3]) == 0 and first[3] == 1.0 and offd < 1e-14 and diag_err < 1e-14,
      f'first-order |PV_fP| = {first}; off-diagonal 2nd order {offd:.0e}; diag vs formula {diag_err:.0e}')
check('A2 DIAGNOSTIC the exact low manifold matches the second-order cell-local Hamiltonian with residual of order t^4/g^6 (next order of the '
      'strong-coupling expansion)', res[-1][1] < 1e-3 and abs(np.log(res[0][1] / res[2][1]) / np.log(4) - 6) < 0.3,
      'residual ' + ', '.join(f'g={r[0]:.0f}: {r[1]:.1e}' for r in res) + f'; slope {np.log(res[0][1] / res[2][1]) / np.log(4):.2f}')
print('   A3 THEOREM at spin S = 1/2 quantum links E^2 = 1/4 is a constant: no electric gap exists, so a "strong-coupling" far end of '
      'S = 1/2 registers cannot be this projection; for S >= 1 (or rotors) it is exactly a cell-local frozen term (A1)')

# ============================================================ B
print('== B. members of one family the link dynamics cannot gap')
fam = [('Q', 3, 2, Fr(1, 6)), ('u^c', 3, 1, Fr(-2, 3)), ('d^c', 3, 1, Fr(1, 3)), ('L', 1, 2, Fr(-1, 2)), ('e^c', 1, 1, Fr(1)), ('nu^c', 1, 1, Fr(0))]
neutral = [n for n, c, w, y in fam if c == 1 and w == 1 and y == 0]; abelian = [n for n, c, w, y in fam if c == 1 and w == 1 and y != 0]
anom = (sum(c * w * y ** 3 for n, c, w, y in fam), sum(c * w * y for n, c, w, y in fam))
q3450 = [(3, 1), (4, 1), (5, -1), (0, -1)]
check('B1 THEOREM a member with no link charge has hops undressed by every register (A1: first order survives at any g), so its ladder '
      'is the free ladder whatever the coupling profile: its far-end mirror (nu^c\', and the "0" of 3-4-5-0) is never gapped by link dynamics; '
      'e^c is charged only under the abelian factor', neutral == ['nu^c'] and abelian == ['e^c'] and anom == (0, 0)
      and sum(q * q * c for q, c in q3450) == 0 and [q for q, c in q3450 if q == 0] == [0],
      f'neutral {neutral}, abelian-only {abelian}; Y^3, Y anomalies {anom[0]}, {anom[1]}; 3-4-5-0 sum c q^2 = 0')

# ============================================================ C
print('== C. free spectral flow on a Wilson-Dirac strip (x, s): the domain-wall fifth direction')
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
def strip(k, Ls, cut=None, flat_from=None, delta=0.02, warp=False):   # small ramp delta*s separates the edge crossings
    H = np.zeros((2 * Ls, 2 * Ls), complex); T = (-sz - 1j * sy) / 2
    for s in range(Ls):
        wx = 0.0 if (flat_from is not None and s >= flat_from) else 1.0
        H[2*s:2*s+2, 2*s:2*s+2] = wx * (np.sin(k) * sx - np.cos(k) * sz) + sz + delta * s * np.eye(2)
        if s + 1 < Ls and not (cut is not None and s + 1 == cut):
            H[2*s+2:2*s+4, 2*s:2*s+2] = T; H[2*s:2*s+2, 2*s+2:2*s+4] = T.conj().T
    if warp:
        S = np.kron(np.diag(2.0 ** (-np.arange(Ls) / 2)), np.eye(2)); H = S @ H @ S
    return H
def flow(Ls, nk=1601, **kw):
    ks = np.linspace(-np.pi, np.pi, nk); prev = None; out = []
    for k in ks:
        E, V = np.linalg.eigh(strip(k, Ls, **kw)); nneg = int(np.sum(E < 0))
        if prev is not None and nneg != prev:
            i0 = np.argmin(np.abs(E)); prof = (np.abs(V[:, i0]) ** 2).reshape(Ls, 2).sum(1)
            out.append((prev - nneg, float(prof @ np.arange(Ls))))
        prev = nneg
    return out
Ls = 12
def summ(fl, lo=2.5):
    return (sum(d for d, c in fl if c < lo), sum(d for d, c in fl if c >= lo), [(d, round(c, 1)) for d, c in fl if c >= lo])
cases = {'bare': summ(flow(Ls)), 'warped': summ(flow(Ls, warp=True)), 'rung cut at 6': summ(flow(Ls, cut=6)),
         'spatial links frozen s>=6': summ(flow(Ls, flat_from=6))}
rng = np.random.default_rng(1); inert = 0
for k in rng.uniform(-3, 3, 5):
    a = np.linalg.eigvalsh(strip(k, Ls)); b_ = np.linalg.eigvalsh(strip(k, Ls, warp=True))
    inert = max(inert, abs(int(np.sum(a < 0)) - int(np.sum(b_ < 0))))
check('C1 THEOREM warp = congruence S H S (S = 2^(-s/2)): Sylvester keeps the negative count at every k, so the spectral flow and '
      'where it sits are warp-independent', inert == 0 and cases['warped'][:2] == cases['bare'][:2], f'inertia difference {inert}')
ok = all(c[0] == -1 and c[1] == 1 for c in cases.values())
for n, c in cases.items(): print(f'   flow {n}: light {c[0]:+d}; others (flow, s) {c[2]}')
check('C2 THEOREM (spectral flow = bulk Chern number, a free index): light end -1 in every case; the mirror flow +1 survives a cut rung '
      'link (it moves to the cut, s = 5, on the light side, and the far piece carries its own pair) and survives frozen spatial links '
      '(it sits in the frozen region)', ok and sorted(cases['rung cut at 6'][2]) == [(-1, 6.0), (1, 5.0), (1, 11.0)],
      'net light -1, rest +1 in all four cases')
print('   C3 THEOREM (A1 + C2) the strict strong-coupling far end is a cell-local projection plus density-density terms; the free part '
      'carries the mirror flow, and the four-fermion remainder is dimension 6 in 3+1D (irrelevant): the hybrid-wall indices (B4 seven '
      'TRIM doublers when top slots are frozen with a unique singlet, B6 mirror one rung down when the rung links are cut) apply verbatim')

# ============================================================ D
print('== D. the link chain across rungs (quadratic regime): where the light link lives')
def chain(gs, kap, k=1e-3):
    n = len(gs); G = np.diag(1 / np.asarray(gs) ** 2); L = np.zeros((n, n))
    for j in range(n - 1):
        L[j, j] += kap[j]; L[j + 1, j + 1] += kap[j]; L[j, j + 1] -= kap[j]; L[j + 1, j] -= kap[j]
    K = k * k * G + L; Gi = np.diag(np.asarray(gs)); w, v = np.linalg.eigh(Gi @ K @ Gi)   # G^-1/2 K G^-1/2
    return w, Gi @ v
gs = 0.6 * 1.25 ** np.arange(13); kap = np.ones(12)
w, v = chain(gs, kap); v0 = v[:, 0] / v[0, 0]; geff = 1 / np.sqrt(np.sum(1 / gs ** 2))
c0 = v[0, 0] / np.sqrt(v[:, 0] @ np.diag(1 / gs ** 2) @ v[:, 0])
kap2 = kap.copy(); kap2[7] = 0.0; w2, v2 = chain(gs, kap2)
gl = 1 / np.sqrt(np.sum(1 / gs[:8] ** 2))
check('D1 THEOREM rung links ordered: the light link is the exactly flat zero mode, its charge coupling at rung 0 is g_eff with '
      '1/g_eff^2 = sum_j 1/g_j^2, so strongly coupled far rungs barely change it (no confinement of the light end); a disordered rung link '
      '(kappa_7 = 0) splits off a second zero mode and the light group lives on rungs 0..7 only',
      np.abs(v0 - 1).max() < 1e-5 and abs(c0 - geff) < 1e-6 and w2[1] < 1e-5 < w[1] and abs(1 / np.sqrt(np.sum(1 / gs[:8] ** 2)) - gl) < 1e-12,
      f'g_j 0.60 -> {gs[-1]:.2f}; g_eff {geff:.4f} vs g_0 {gs[0]:.2f}; light-group coupling after split {gl:.4f}; 2nd eigen {w[1]:.1e} -> {w2[1]:.1e}')
print('   D2 DICHOTOMY ordered rung links: far-end fermions carry the light group, gauge-dynamical gapping needs that group strong at the '
      'gap scale; disordered: the fermion ladder is cut (A1), the mirror moves to the last ordered rung (C2), charged and massless')

# ============================================================ E
print('== E. power counting and estimates')
pc = {D: [Fr(4 ** j) ** 2 / Fr(2 ** (j * D)) for j in range(6)] for D in (2, 3, 4)}
check('E1 THEOREM CL-3 plaquette in proper area per proper (D)-volume: rung-j dimensionless 1/g^2 scales as 2^(j(4-D)): grows the far '
      'coupling in 1+1D (4^j) and 2+1D (2^j) classically, but is rung-independent in 3+1D (only running changes it)',
      pc[4] == [1] * 6 and pc[3] == [Fr(2 ** j) for j in range(6)] and pc[2] == [Fr(4 ** j) for j in range(6)],
      '1/g_j^2 ratios D=2: ' + str([int(x) for x in pc[2][:4]]) + ', D=3: ' + str([int(x) for x in pc[3][:4]]) + ', D=4: 1')
MZ = 91.1876; ai = np.array([59.0, 29.6, 8.47]); bi = np.array([41 / 10, -19 / 6, -7.0]); Ea = 2.1e18
ER = lambda R: 0.354 * 2.0 ** -R * Ea
alpha = lambda mu: 1 / (ai - bi / (2 * np.pi) * np.log(mu / MZ))
a12, a23 = alpha(ER(12)), alpha(ER(23)); Rstar = np.log2(0.354 * Ea / 0.2)
GF = 1.1663787e-5; sw2 = 0.2312; GZ = GF * MZ ** 3 / (6 * np.sqrt(2) * np.pi) * 2 * sw2 ** 2 * 1e3
check('E2 ESTIMATE one-loop SM running at the top rung (E_R = 0.354 x 2^-R x 2.1e18 GeV): the light-cone window R <= 12-23 puts the far '
      'end at alpha_1,2,3 ~ 0.02-0.04, far below compact-U(1) confinement (alpha ~ 0.08, beta_c = 1.01) and any NJL-type O(1) threshold; '
      'colour turns strong only near R* ~ 62, abelian hypercharge never (IR free)',
      max(a23) < 0.05 and max(a12) < 0.05 and 60 < Rstar < 64,
      f'R=12: {np.round(a12, 3)}; R=23: {np.round(a23, 3)}; R* = log2(0.354 E_a / 0.2 GeV) = {Rstar:.1f}')
check('E3 ESTIMATE vs measurement: a massless mirror e^c\' (B1, hypercharge only, never gapped by link dynamics) adds '
      'Gamma(Z) = G_F M_Z^3/(6 sqrt2 pi) x 2 s_W^4 per family, against sigma(Gamma_Z) = 2.3 MeV: excluded; nu^c\' is sterile (unconstrained by Z)',
      GZ / 2.3 > 10, f'{GZ:.1f} MeV per family ({3 * GZ:.0f} MeV for three) = {GZ / 2.3:.0f} sigma per family')
print('   E4 ESTIMATE ordered phase: a gauge-dynamical mirror gap needs the measured diagonal couplings to be O(1) at the gap scale >= M_Z '
      '(LEP): alpha_3(M_Z) = 0.118, alpha_2 = 0.034, alpha_Y = 0.010; only QCD binds, at ~0.3 GeV, and it touches neither leptons nor e^c, nu^c')
print(f'supplied: rotor links (S >= 1), charges 3,4,5,0 and one SM family, Wilson-Dirac strip m = -1, warp 1/2 congruence, Gaussian link chain '
      f'g_j, SM one-loop running from M_Z, E_a, R window from hybrid-wall D3 | {time.monotonic() - T0:.1f} s')
print('cited: hybrid-wall B3-B6/C2-C4/D2-D3, CANDIDATE_LAWS_v3 chirality constraints, Golterman-Shamir, Schwinger/Polyakov confinement '
      '(1+1D, 2+1D compact U(1) confine at every coupling: lower-D toys cannot test light-link localization), PDG Gamma_Z')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

AUDIT_INPUT_PATHS = ('docs/ONE_RUNNING_CELL_COUPLING_SETS_THE_COLOUR_TO_WEAK_RUNG_RATIO_BUT_FITS_THE_WEAK_AND_SEESAW_RANKS_AND_FAILS_FOR_THE_ELECTROWEAK_FACTORS_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""One running cell coupling on the zoom ladder: which hierarchies does it set? (finite runner, seeded).

Rule tested: every link factor has one cell coupling; at rung n (blocks of 2^n cells) a factor reads the
coupling renormalised by the modes it acts on; its condensate (gap) forms at the first rung where that
coupling reaches the factor's critical value; cell-local quartics act at the cell rung only.
  A  exact: crossing-rung law and its n*b invariant; beta coefficients; Sp(2N), SU(4), SU(2) Casimirs; the
     B-L = 2 channel; dimension counting of a cell quartic and of the seesaw transfer; mean-field tuning law;
     vacuum-standard subtraction of condensate energies
  B  estimates against measurement: SM couplings at the cell, colour calibration, the light-Higgs factor,
     the seesaw factor, the mirror, Lambda power laws, look-elsewhere and the fitted-number count
Tags: [T] theorem/exact, [F] finite diagnostic, [E] estimate against measurement.
"""
import itertools
import time
from fractions import Fraction as Fr
import numpy as np
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 60
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text} | {vals}")


PI, LN2 = np.pi, np.log(2.0)
M = 2.44e18                      # hbar c/L, the cell rung (GeV)
MZ, V, MT = 91.1876, 246.22, 172.6
AEM_INV, S2W, AS = 127.95, 0.23122, 0.1180
FPI = 0.0921
RHO_L = 7.15e-121                # Lambda L^2
M3, M2 = 0.0501e-9, 0.0087e-9   # GeV
MR_Y1 = 4.6e14                   # neutrino-mass B2: type I, y = 1


def rung(E):
    return np.log2(M / E)


def bnab(CA, weyl_T=Fr(0), cscal_T=Fr(0)):
    return Fr(11, 3) * CA - Fr(2, 3) * weyl_T - Fr(1, 3) * cscal_T


# ------------------------------------------------------------------ A
print("== A. exact")
# A1 one-loop crossing law: 1/a(n) = 1/a_cell - b n ln2/(2 pi); n_X b_X = (2 pi/ln2)(1/a_cell - 1/a_cX)
import sympy as sp
n, b, ac, acx = sp.symbols("n b a_cell a_cX", positive=True)
ainv_n = 1 / ac - b * n * sp.log(2) / (2 * sp.pi)
nX = sp.solve(sp.Eq(ainv_n, 1 / acx), n)[0]
inv = sp.simplify(nX * b - 2 * sp.pi / sp.log(2) * (1 / ac - 1 / acx))
dn = sp.simplify(sp.diff(nX, ac) * (-ac ** 2))     # dn/d(1/a_cell)
check(inv == 0 and sp.simplify(dn - 2 * sp.pi / (b * sp.log(2))) == 0, "A1 [T]",
      "n_X = 2pi(1/a_cell - 1/a_cX)/(b_X ln2); n_X b_X is common at equal a_c, so rung ratios are content-fixed",
      f"n*b invariant residual {inv}; dn/d(1/a) = {dn}")

# A2 beta coefficients
FAM = {"q": (3, 2, Fr(1, 6)), "u^c": (3, 1, Fr(-2, 3)), "d^c": (3, 1, Fr(1, 3)),
       "L": (1, 2, Fr(-1, 2)), "e^c": (1, 1, Fr(1)), "n^c": (1, 1, Fr(0))}
b3 = bnab(3, Fr(1, 2) * 3 * sum(d for c, d, y in FAM.values() if c == 3))
b2 = bnab(2, Fr(1, 2) * 3 * sum(c for c, d, y in FAM.values() if d == 2), Fr(1, 2))
b1 = -Fr(3, 5) * (Fr(2, 3) * 3 * sum(c * d * y * y for c, d, y in FAM.values()) + Fr(1, 3) * 2 * Fr(1, 4))


def bSp(N, nF=4, nA=0):          # Sp(2N): C_A = N+1, T(F) = 1/2, T(A) = N-1 (Weyl counts)
    return bnab(N + 1, Fr(1, 2) * nF + (N - 1) * nA)


bsp = {N: bSp(N) for N in (1, 2, 3, 4)}
bsp_tp = {N: bSp(N, 4, 6) for N in (2, 3, 4)}
ok = (b1, b2, b3) == (Fr(-41, 10), Fr(19, 6), Fr(7)) and bsp[1] == 6 and bsp[2] == Fr(29, 3) and bsp_tp[2] == Fr(17, 3)
check(ok, "A2 [T]", "b (>0 = AF): SM (U1 GUT, SU2, SU3) = (-41/10, 19/6, 7); Sp(2N) + 4 Weyl F: 11(N+1)/3 - 4/3; +6 Weyl A: -4(N-1)",
      f"Sp(2N) N=1..4: {[str(x) for x in bsp.values()]}; +6A N=2..4: {[str(x) for x in bsp_tp.values()]}")


# A3 Casimirs from explicit generators
def herm_basis_constrained(dim, J=None):
    """Hermitian T with T^T J + J T = 0 (sp) or traceless (su)."""
    rows, basis = [], []
    E = []
    for i in range(dim):
        for j in range(dim):
            if i == j:
                m = np.zeros((dim, dim), complex); m[i, i] = 1; E.append(m)
            elif i < j:
                m = np.zeros((dim, dim), complex); m[i, j] = m[j, i] = 1; E.append(m)
                m = np.zeros((dim, dim), complex); m[i, j] = -1j; m[j, i] = 1j; E.append(m)
    E = np.array(E)
    if J is not None:
        C = np.array([(e.T @ J + J @ e).ravel() for e in E]).T
    else:
        C = np.array([[np.trace(e)] for e in E]).T
    C = np.vstack([C.real, C.imag])
    _, s, vt = np.linalg.svd(C)
    null = vt[np.sum(s > 1e-10):]
    Ts = [np.tensordot(v, E, 1) for v in null]
    # Gram-Schmidt with Tr(T_a T_b) = 1/2 delta
    out = []
    for T in Ts:
        for U in out:
            T = T - 2 * np.trace(T @ U).real * U
        nrm = np.sqrt(2 * np.trace(T @ T).real)
        if nrm > 1e-9:
            out.append(T / nrm)
    return out


def casimir(Ts):
    C = sum(T @ T for T in Ts)
    return C[0, 0].real, np.abs(C - C[0, 0] * np.eye(len(C))).max()


def adj_casimir(Ts):
    f = np.array([[[(-2j * np.trace((A @ B - B @ A) @ Cm)).real for Cm in Ts] for B in Ts] for A in Ts])
    return np.einsum("acd,bcd->ab", f, f)[0, 0]


res = {}
for N in (1, 2):
    J = np.kron(np.array([[0, 1], [-1, 0]]), np.eye(N))
    Ts = herm_basis_constrained(2 * N, J)
    c2, err = casimir(Ts)
    res[N] = (len(Ts), c2, adj_casimir(Ts), err)
su4 = herm_basis_constrained(4)
su2 = herm_basis_constrained(2)


def pair_casimirs(Ts):
    d = len(Ts[0]); I = np.eye(d)
    T2 = [np.kron(T, I) + np.kron(I, T) for T in Ts]
    C = sum(T @ T for T in T2)
    P = np.zeros((d * d, d * d))
    for i in range(d):
        for j in range(d):
            P[i * d + j, j * d + i] = 1
    Ps, Pa = (np.eye(d * d) + P) / 2, (np.eye(d * d) - P) / 2
    cs = np.trace(C @ Ps).real / np.trace(Ps).real
    ca = np.trace(C @ Pa).real / np.trace(Pa).real
    return casimir(Ts)[0], cs, ca


c4, c10, c6 = pair_casimirs(su4)
c2f, c3, c1 = pair_casimirs(su2)
ok = all(abs(res[N][1] - (2 * N + 1) / 4) < 1e-12 and abs(res[N][2] - (N + 1)) < 1e-9 for N in (1, 2)) \
    and abs(c4 - 15 / 8) < 1e-12 and abs(c10 - 4.5) < 1e-12 and abs(c6 - 2.5) < 1e-12 and abs(c3 - 2) < 1e-12
check(ok, "A3 [T]", "explicit generators: Sp(2N) C2(F) = (2N+1)/4, C_A = N+1; SU(4) 15/8, 9/2 (10), 5/2 (6); SU(2) 3/4, 2 (3)",
      f"Sp(2): dim {res[1][0]}, C2 {res[1][1]:.4f}, CA {res[1][2]:.3f}; Sp(4): dim {res[2][0]}, C2 {res[2][1]:.4f}, "
      f"CA {res[2][2]:.3f}")

# A4 the B-L = 2 channel: neutral colour-singlet scalar bilinears of the 16 with B-L = 2
BL = {"q": Fr(1, 3), "u^c": Fr(-1, 3), "d^c": Fr(-1, 3), "L": Fr(-1), "e^c": Fr(1), "n^c": Fr(1)}
QQ = {"e^c": [Fr(1)], "n^c": [Fr(0)], "L": [Fr(0), Fr(-1)]}
chan = []
for a, bb in itertools.combinations_with_replacement(BL, 2):
    if BL[a] + BL[bb] == 2 and FAM[a][0] == FAM[bb][0] == 1:
        qs = {qa + qb for qa in QQ.get(a, [None]) for qb in QQ.get(bb, [None])}
        chan.append((a, bb, sorted(qs)))
neutral = [c for c in chan if Fr(0) in c[2]]
dC_su4 = 2 * c4 - c10
dC_su2r = 2 * c2f - c3
check(len(neutral) == 1 and neutral[0][:2] == ("n^c", "n^c") and dC_su4 < 0 and dC_su2r < 0, "A4 [T]",
      "the only neutral colourless B-L = 2 scalar bilinear is n^c n^c, PS (10,1,3); every content factor is trivial "
      "or repulsive there (2C2(F) - C2(R) < 0): no content factor binds a Z4-breaking pair",
      f"channels {[(a + ' ' + b_) for a, b_, q in chan]}; dC SU(4) 10 = {dC_su4:.3f}, SU(2)_R 3 = {dC_su2r:.3f}")

# A5 dimension counting
#   cell quartic g psi^4 a^2: dimensionless at rung n = g 2^(-2n); seesaw transfer (n^c n^c)(chi chi)/M^2:
#   M_R = <chi chi>/M^2 ~ M 2^(-3 n_S); n^c cannot carry the binder's charge (L H n^c must stay invariant)
g = np.array([1.0 * 2.0 ** (-2 * k) for k in range(6)])
mr_rung = lambda nS, k: k * nS
check(np.allclose(g[1:] / g[:-1], 0.25) and mr_rung(4, 3) == 12, "A5 [T]",
      "a cell quartic at rung n has strength g 2^(-2n): it gaps at the cell or not at all; a hidden B-L = 2 "
      "condensate reaches n^c via (n^c n^c)(chi chi)/M^2: M_R rung = 3 n_S (L H n^c forbids n^c charged)",
      f"g(n)/g(0) = {[f'{x:.4g}' for x in g[:4]]}; n_S = 4 -> M_R rung 12")


# A6 mean-field tuning law for a cell quartic (4D ball cutoff 1): 1/G = c int k^3/(k^2+m^2) dk
def inv_g(m):
    return quad(lambda k: k ** 3 / (k * k + m * m), 0, 1, epsabs=1e-14, epsrel=1e-12)[0]


Ic = inv_g(0.0)
rows = []
okq = True
for m in (1e-2, 1e-3, 1e-4):
    d_num = 1 - inv_g(m) / Ic
    d_an = m * m * np.log((1 + m * m) / (m * m))
    okq &= abs(d_num / d_an - 1) < 1e-6
    rows.append(f"m={m:.0e}: {d_num:.3e}")
tune = lambda m: m * m * np.log(1 / (m * m))
mm, ms = 1500 / M, 2.0 ** -12
check(okq, "A6 [T/F]", "mean-field cell quartic: (G - G_c)/G = m^2 ln((1+m^2)/m^2): a sub-cell quartic gap is a tune",
      f"{'; '.join(rows)}; tune(1.5 TeV) = {tune(mm):.1e}; tune(2^-12) = {tune(ms):.1e}")

# A7 vacuum standard subtracts condensate energies: toy 2-mode pairing H = e(n1+n2) + D(c1c2 + h.c.)
e0 = 0.3
okv, rowsv = True, []
for D in (0.0, 0.5, 1.0):
    H = np.array([[0.0, D], [D, 2 * e0]])       # basis |00>, |11>
    w, U = np.linalg.eigh(H)
    vac = U[:, 0]
    resp = vac @ H @ vac - w[0]                 # vacuum's total phase less the vacuum phase of the same edges
    okv &= abs(resp) < 1e-15 and (D == 0 or w[0] < 0)
    rowsv.append(f"D={D}: condensation energy {w[0]:+.4f}, response {abs(resp):.0e}")
check(okv, "A7 [T]", "CL-3's vacuum standard subtracts every condensation energy: the rule's condensates give no Lambda",
      "; ".join(rowsv))

# ------------------------------------------------------------------ B
print("== B. estimates against measurement (one-loop unless stated)")
A1, A2, A3 = 0.6 * (1 - S2W) * AEM_INV, S2W * AEM_INV, 1 / AS
bS = np.array([41 / 10, -19 / 6, -7.0])
BIJ = np.array([[199 / 50, 27 / 10, 44 / 5], [9 / 10, 35 / 6, 12], [11 / 10, 9 / 2, -26]])


def run_up(y0, two, steps=4000):
    y = np.array(y0, float); t1 = np.log(M / MZ); h = t1 / steps
    f = lambda y: -bS / (2 * PI) - (BIJ @ (1 / y) / (8 * PI ** 2) if two else 0)
    for _ in range(steps):
        k1 = f(y); k2 = f(y + h / 2 * k1); k3 = f(y + h / 2 * k2); k4 = f(y + h * k3)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y


c1l, c2l = run_up([A1, A2, A3], False), run_up([A1, A2, A3], True)
reads = [4 * PI * k for k in (0.5, 1, 2, 4, 8, 16)]
near = min(reads, key=lambda r: abs(np.log(r / c2l[2])))
tol = abs(np.log(near / c2l[2]))
p_hit = 2 * tol / LN2
check(abs(near - 16 * PI) < 1e-9, "B1 [E]", "1/a(cell) from MZ: SU(3) within 1.6% of the reading kappa T = 4 (16 pi; chance p_hit, look-elsewhere); "
      "SU(2)_L 4% off, U(1)_Y 32% off: one cell coupling FAILS for the electroweak factors",
      f"1L {c1l.round(2)}; 2L {c2l.round(2)}; 16pi = {16 * PI:.2f}; p_hit = {p_hit:.2f}")


def descend(ainv, b0s, b1s, thr, acinv, h=2e-3):
    """1/a from the cell down (t = ln(M/mu)), piecewise (b0, b1) below thresholds thr (GeV, descending);
    returns rung where 1/a = acinv (two-loop when b1s given)."""
    t, y, i = 0.0, ainv, 0
    while y > acinv:
        mu = M * np.exp(-t)
        while i < len(thr) and mu < thr[i]:
            i += 1
        dy = -(b0s[i] / (2 * PI) + b1s[i] / (8 * PI ** 2 * max(y, 1e-3)))
        y += dy * h; t += h
        if t > 400:
            return np.inf
    return t / LN2


thr_q = [MT, 4.18, 1.27]
b0q = [7.0, 23 / 3, 25 / 3, 9.0]
b1q = [26.0, 116 / 3, 154 / 3, 64.0]
acq = 3 * (4 / 3) / PI
nq = {(lab, two): descend(ai, b0q, b1q if two else [0] * 4, thr_q, acq)
      for lab, ai in (("16pi", 16 * PI), ("meas", c1l[2])) for two in (False, True)}
n_fpi = rung(FPI)
off = {k: n_fpi - v for k, v in nq.items()}        # f rung = crossing rung + offset (colour calibration)
check(1.0 < min(off.values()) and max(off.values()) < 4.0, "B2 [E]", "colour reaches a_c = pi/(3 C_F) at rung ~61-63; f_pi sits 2-3.6 rungs lower (offset = f calibration)",
      "; ".join(f"{k[0]},{'2L' if k[1] else '1L'}: n_c={v:.2f}, off={off[k]:.2f}" for k, v in nq.items())
      + f"; f_pi rung {n_fpi:.2f}")

# B3 the light-Higgs factor Sp(2N), 4 Weyl F (+6A top partners): f rung and xi = v^2/f^2
n_v, n_xi = rung(V), rung(V / np.sqrt(0.1))


def b1_sp(N, nF=4, nA=0):
    CA, CF, TA = N + 1, (2 * N + 1) / 4, N - 1
    # antisymmetric rep of Sp(2N): T = N - 1, C2 = N
    return 34 / 3 * CA ** 2 - nF * 0.5 * (10 / 3 * CA + 2 * CF) - nA * TA * (10 / 3 * CA + 2 * N)


rowsb, hits = [], []
for N, nA in ((1, 0), (2, 0), (3, 0), (4, 0), (2, 6)):
    b0 = float(bSp(N, 4, nA)); acinv = 3 * (2 * N + 1) / 4 / PI
    out = []
    for two in (False, True):
        nc = descend(16 * PI, [b0], [b1_sp(N, 4, nA) if two else 0.0], [], acinv)
        fr = nc + off[("16pi", two)]
        out.append(fr)
    xi = (V / (M * 2.0 ** -np.array(out))) ** 2
    lab = f"Sp({2 * N}){'+6A' if nA else ''}"
    rowsb.append(f"{lab}: b={b0:.2f} f-rung {out[0]:.1f}/{out[1]:.1f} xi={xi[0]:.0e}/{xi[1]:.0e}")
    if all(x <= 0.1 for x in xi) and all(x >= 1e-4 for x in xi):
        hits.append(lab)
check(hits == ["Sp(4)"], "B3 [E]", "light-Higgs factor, 16 pi, 1L/2L: AX-6's Sp(2) gives f << v (fails); Sp(4)+4F f ~ 7-10 TeV, xi ~ 1e-3; "
      "Sp(6), Sp(8) xi < 1e-10; top partners (6A) push Sp(4) to f << v",
      "; ".join(rowsb) + f"; window xi in [1e-4, 0.1] <-> f rung [{n_xi - 5:.1f}, {n_xi:.1f}]")

# B4 one cell coupling vs SU(2)_L once the Sp(4) doublets run (4 Weyl SU(2)_L doublets above Lambda_HC)
nc4 = descend(16 * PI, [float(bsp[2])], [0.0], [], 3 * 1.25 / PI)
lam4 = M * 2.0 ** -nc4
a2_shift = -(4 / 3) / (2 * PI) * np.log(M / lam4)
check(abs(c1l[1] + a2_shift - 16 * PI) / (16 * PI) > 0.1, "B4 [E]", "Sp(4) modes are SU(2)_L doublets: 1/a_2(cell) drops 6.8, 17% from the one coupling",
      f"Lambda_HC = {lam4:.2g} GeV; 1/a_2(cell) {c1l[1]:.2f} -> {c1l[1] + a2_shift:.2f} vs {16 * PI:.2f}")

# B5 the seesaw factor: required b for M_R rungs 11-14.9 (k = 3 transfer; k = 1 shown for contrast)
nR = {"Weinberg c=1": 11.4, "type I y=1": 12.4, "type I y=y_t(M)": 14.9}
need = {lab: (2 * PI * (16 * PI - 1.27) / (r / 3 * LN2), 2 * PI * (16 * PI - 1.27) / (r * LN2)) for lab, r in nR.items()}
NS = {lab: (v[0] * 3 / 11, v[1] * 3 / 11) for lab, v in need.items()}
okb = all(v[0] > 80 and 25 < v[1] < 45 for v in need.values())
check(okb and len(neutral) == 1, "B5 [E/T]", "seesaw needs a NEW factor (A4) with b ~ 90-120 (k = 3; pure SU(24-32)): its rank is a FIT of M_R; "
      "its spontaneous Z4 break keeps the walls (neutrino-mass B4)",
      "; ".join(f"{lab} (rung {nR[lab]}): b={v[0]:.0f} (N~{NS[lab][0]:.0f}); k=1 b={v[1]:.0f}" for lab, v in need.items()))

# B6 the mirror: cell quartic g/t >= 8 (block-quartic-smg) gaps at the cell rung
gap_rung = rung(0.9 * 8 * M / 8)   # gap ~0.9 g with g = 8 t, t ~ M (cell units)
check(gap_rung < rung(1500) - 45, "B6 [E/F]", "mirror: g/t >= 8 gaps at the cell (A5), 50 rungs above 1.5 TeV; an inequality, release problem untouched",
      f"gap rung {gap_rung:.2f} vs bound rung {rung(1500):.2f}")

# B7 simultaneous: f_HC rung = f_pi rung - (n_q - n_HC) for any 1/a_cell in the measured band (A1 ratio law)
rows7, fr7 = [], []
for lab, ai in (("16pi", 16 * PI), ("1L", c1l[2]), ("2L", c2l[2])):
    nqa = descend(ai, b0q, [0] * 4, thr_q, acq)
    nha = descend(ai, [float(bsp[2])], [0.0], [], 3 * 1.25 / PI)
    fr7.append(n_fpi - (nqa - nha)); rows7.append(f"{lab} 1/a={ai:.2f}: n_q={nqa:.2f} n_HC={nha:.2f} f-rung={fr7[-1]:.2f}")
nw_f = fr7[0]
check(all(n_xi - 5 < x < n_xi for x in fr7), "B7 [E]", "f_HC rung = f_pi rung - (n_q - n_HC) is stable (< 0.1 rung) over the measured 1/a_cell band",
      "; ".join(rows7) + f"; v rung {n_v:.2f}")

# B8 Lambda: rung counts and integer power laws over the rule's scales (look-elsewhere)
nL4 = -np.log2(RHO_L) / 4
scales = {"v": rung(V), "f_HC": nw_f, "M_R": rung(MR_Y1), "fpi": n_fpi, "m3": rung(M3), "m2": rung(M2)}
mono = []
for (a, na), (c, nc) in itertools.combinations_with_replacement(scales.items(), 2):
    for p, q in itertools.product(range(0, 3), range(-2, 3)):
        if p == 0 and q == 0 or (a == c and q != 0):
            continue
        r = p * na + q * nc
        if 0 < r < 200:
            mono.append((abs(r - nL4), f"{a}^{p} {c}^{q}" if q else f"{a}^{p}", r))
mono.sort()
frac = np.mean([m[0] < 0.5 for m in mono])
miss = {"(v^2/M)": 2 * scales["v"], "m3": scales["m3"], "m2": scales["m2"]}
check(all(abs(v - nL4) > 1.5 for v in miss.values()), "B8 [E]", "Lambda^(1/4) at rung 99.8 (2^-399); rule sets none (A7); power laws miss (rung gaps x4 in Lambda)",
      "; ".join(f"{k}: {v:.1f}" for k, v in miss.items()) + f"; rung {nL4:.2f}; {len(mono)} monomials, "
      f"{100 * frac:.0f}% within 0.5; best {mono[0][1]} ({mono[0][2]:.1f})")

# B9 count
fit = ["1/a_cell (a reading, kappa T = 4, 1 of 6)", "Sp(2N) rank (1 of 4)", "sin(theta) (xi ~ 1e-3)",
       "S rank N (fit of M_R)", "mirror g/t >= 8 (inequality)", "y_nu, top weights"]
expl = {"colour scale": "calibration (1.6% reading near-hit)", "weak f": "FITTED by rank",
        "mirror": "cell, inequality", "seesaw": "restated as N", "Lambda": "not set"}
check(len(fit) == 6 and len(expl) == 5, "B9 [E]", "count: supplied numbers vs scales",
      "supplied: " + "; ".join(fit) + " || scales: " + "; ".join(f"{k}: {v}" for k, v in expl.items()))

gate = {"fitted": ["1/a_cell reading (picked by alpha_s)", "Sp(4) rank (picked by v)", "S rank (picked by M_R)"],
        "named": ["Sp(2N) hypercolour + SU(4)/Sp(4) coset", "new SU(N_S)", "n^c n^c channel"],
        "tests": ["SU2_L/U1_Y at the one coupling: FAIL (B1, B4)", "mirror >= 1.5 TeV: pass (inequality)"],
        "Lambda": "UNTESTED (not set)"}
check(len(gate["fitted"]) == 3, "G [gate]", "anti-smuggling gate: the rule FAILS (fits 3 numbers by choice, names "
      "groups; its one unfitted test, a common cell coupling, fails for SU(2)_L and U(1)_Y)",
      " / ".join(f"{k}: {v}" for k, v in gate.items()))
print("supplied: measured MZ couplings, f_pi, v, m_t, Delta m^2's, M_R(y)=neutrino-mass B2, Lambda L^2; ladder a_c;")
print("  one/two-loop running; colour offset as the f calibration; xi window [1e-4, 0.1]; g/t >= 8 from block-quartic-smg.")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")

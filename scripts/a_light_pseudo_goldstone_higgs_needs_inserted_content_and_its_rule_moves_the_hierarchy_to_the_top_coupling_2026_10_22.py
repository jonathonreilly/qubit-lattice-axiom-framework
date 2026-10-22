AUDIT_INPUT_PATHS = ('docs/A_LIGHT_PSEUDO_GOLDSTONE_HIGGS_NEEDS_INSERTED_CONTENT_AND_ITS_RULE_MOVES_THE_HIERARCHY_TO_THE_TOP_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""AX-6 light-Higgs rule: can the content be derived, and does the rule work? (finite runner, seeded).

Sections:
  A  derivation attempt: is (2)_0 + (1)_+1/2 + (1)_-1/2 with a pseudoreal two-valued index
     present in any structure of the laws (families, mirrors, tick copies, registers)?
  B  conditional test of the inserted-content rule: coset algebra, anomalies, the
     misalignment potential from gauge, top and species-mass terms, m_H
  C  the scale f: transmutation, near-critical quartic, rung placement
  D  estimates against measurement (xi, S, T)
Every number chosen to reproduce v or m_H is printed as FITTED.
"""
import time
from fractions import Fraction as Fr
from itertools import product
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text} | {vals}")


PI, LN2 = np.pi, np.log(2.0)
M_CELL = 2.44e18
V_EW, M_H, M_T = 246.22, 125.1, 172.6
G, GP = 0.6517, 0.3576
NC = 3

# ---------------------------------------------------------------- A
print("== A. derivation attempt from the laws' structure")
FAM = {"q": (3, 2, Fr(1, 6)), "u^c": (3, 1, Fr(-2, 3)), "d^c": (3, 1, Fr(1, 3)),
       "L": (1, 2, Fr(-1, 2)), "e^c": (1, 1, Fr(1)), "n^c": (1, 1, Fr(0))}
modes = []                                   # (dim SU2, Y, Q) over the 16 and its mirror (16bar)
for sgn in (1, -1):
    for c, d, y in FAM.values():
        for t3 in ([Fr(1, 2), Fr(-1, 2)] if d == 2 else [Fr(0)]):
            modes.append((d, sgn * y, sgn * (t3 + y)))
dY = sorted({str(y) for d, y, q in modes if d == 2})
sY = sorted({str(y) for d, y, q in modes if d == 1})
qs = {q for d, y, q in modes}
ok = "0" not in dY and "1/2" not in sY and "-1/2" not in sY and all((3 * q).denominator == 1 for q in qs) \
    and Fr(1, 2) not in qs
check(ok, "A1 [T]", "family 16 + mirror 16bar: no Y = 0 doublet, no Y = +-1/2 singlet, every charge in Z/3 "
      "(none = +-1/2); the needed modes have Q = +-1/2, so no family or mirror mode is one",
      f"doublet Y {dY}; singlet Y {sY}")
# bosonic registers: SU(2) centre trivial on adjoint (links), edges singlets -> no doublet at any zoom
sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
g = expm(0.5j * np.tensordot(RNG.normal(size=3), np.array(sig), axes=1))
ad = lambda u: np.array([[0.5 * np.trace(sig[a] @ u @ sig[b] @ u.conj().T).real for b in range(3)] for a in range(3)])
check(np.allclose(ad(g), ad(-g)), "A2 [T]", "link, rishon and edge registers are centre-blind (Ad(-g) = Ad(g)); "
      "no register configuration is an SU(2)_L doublet, so the new doublet must be fermion modes",
      f"|Ad(g)-Ad(-g)| = {np.abs(ad(g) - ad(-g)).max():.0e}")
# tick copies as the index: the copy mass diag(0, M) has commutant u(1)+u(1) in u(2): no Sp(2) index
basis = [np.eye(2)] + sig
cm = np.diag([0.0, 1.0])
A = np.array([(b @ cm - cm @ b).ravel() for b in basis]).T
comm_dim = 4 - np.linalg.matrix_rank(np.vstack([A.real, A.imag]))
check(comm_dim == 2, "A3 [T]", "tick's two copies as the index: the copy mass (extra M on s = -1) commutes only with "
      "u(1) + u(1), not Sp(2); the index is not a symmetry, CL-1's link rule gives no Sp(2), and the s = -1 copy "
      "sits at the cell rung (decoupled at f)", f"commutant dim {comm_dim} (Sp(2) would need 4)")


# JW check: index-singlet Lorentz-scalar pair is flavour-antisymmetric only WITH a two-valued index
def jw(n):
    a = np.array([[0, 1], [0, 0]]); z = np.diag([1, -1]); I2 = np.eye(2)
    ops = []
    for k in range(n):
        m = np.array([[1.0]])
        for j in range(n):
            m = np.kron(m, z if j < k else (a if j == k else I2))
        ops.append(m)
    return ops


eps = np.array([[0, 1], [-1, 0]])
c4 = jw(4)                                   # (flavour i, spin al) -> 2i+al
P = lambda i, j: sum(eps[a, b] * c4[2 * i + a] @ c4[2 * j + b] for a in range(2) for b in range(2))
sym_noidx = np.abs(P(0, 1) - P(1, 0)).max() < 1e-12 and np.abs(P(0, 0)).max() > 0.5
c8 = jw(8)                                   # (i, index x, spin al) -> 4i+2x+al
P8 = lambda i, j: sum(eps[x, y] * eps[a, b] * c8[4 * i + 2 * x + a] @ c8[4 * j + 2 * y + b]
                      for x in range(2) for y in range(2) for a in range(2) for b in range(2))
anti_idx = np.abs(P8(0, 1) + P8(1, 0)).max() < 1e-12 and np.abs(P8(0, 0)).max() < 1e-12
check(sym_noidx and anti_idx, "A4 [T]", "Grassmann check (Jordan-Wigner): eps_spin pair is flavour-SYMMETRIC "
      "without an index (no SU(4)/Sp(4)), ANTISYMMETRIC with an Sp(2)-singlet index; with per-site single modes the "
      "index needs 8 new sites per cell, which no clause of the laws carries", "exact operator identities")
print("   GATE (a) result: no structure of the laws yields the content; inserting it fails criterion (2).")

# ---------------------------------------------------------------- B
print("== B. conditional test of the inserted-content rule (gate FAIL; physics check only)")
# flavours: 0 D1, 1 D2 (Y=0 doublet), 2 S+ (Y=1/2), 3 S- (Y=-1/2)
SB = np.zeros((4, 4)); SB[0, 1], SB[2, 3] = 1, 1; SB -= SB.T
SH = np.zeros((4, 4)); SH[0, 3], SH[1, 2] = 1, 1; SH -= SH.T
Sig = lambda th: np.cos(th) * SB + np.sin(th) * SH
pf = lambda s: s[0, 1] * s[2, 3] - s[0, 2] * s[1, 3] + s[0, 3] * s[1, 2]
TL = [np.pad(s / 2, ((0, 2), (0, 2))) for s in sig]
Y = np.diag([0, 0, 0.5, -0.5]); Q = TL[2] + Y
gm = []
for i in range(4):
    for j in range(i + 1, 4):
        m = np.zeros((4, 4), complex); m[i, j] = m[j, i] = 0.5; gm.append(m)
        m = np.zeros((4, 4), complex); m[i, j], m[j, i] = -0.5j, 0.5j; gm.append(m)
for k in range(1, 4):
    d = np.zeros(4); d[:k] = 1; d[k] = -k; gm.append(np.diag(d) / np.sqrt(2 * k * (k + 1)))
act = lambda X, S: X @ S + S @ X.T


def broken_rank(S):
    M = np.array([act(X, S).ravel() for X in gm]).T
    return np.linalg.matrix_rank(np.vstack([M.real, M.imag]), tol=1e-9)


ths = np.linspace(0, PI / 2, 7)
unit = max(np.abs(Sig(t) @ Sig(t).T - np.eye(4)).max() for t in ths)
nbr = {broken_rank(Sig(t)) for t in ths}
qk = max(np.abs(act(Q, Sig(t))).max() for t in ths)
ew0 = max(np.abs(act(X, SB)).max() for X in TL + [Y])
mw = lambda t: sum(np.linalg.norm(act(TL[a], Sig(t))) ** 2 for a in range(2))
ratio = [mw(t) / mw(PI / 2) for t in ths]
check(unit < 1e-12 and nbr == {5} and qk < 1e-12 and ew0 < 1e-12 and np.allclose(ratio, np.sin(ths) ** 2)
      and abs(pf(Sig(0.7)) - 1) < 1e-12, "B1 [T]", "coset SU(4)/Sp(4): 5 broken generators at every theta, Q kept, "
      "theta = 0 keeps SU(2)_L x U(1)_Y, m_W^2(theta)/m_W^2(pi/2) = sin^2 theta (v = f sin theta)",
      f"unitarity {unit:.0e}, Pf 1, ratios {[round(float(r), 4) for r in ratio]}")
# Goldstone quantum numbers at theta=0
M0 = np.array([act(X, SB).ravel() for X in gm]).T
Mr = np.vstack([M0.real, M0.imag])
_, sv, vt = np.linalg.svd(Mr)
Bk = [sum(c * X for c, X in zip(vt[k], gm)) for k in range(5)]
proj = lambda Z: np.array([np.trace(Bk[k].conj().T @ Z).real * 2 for k in range(5)])
Rm = lambda T: np.array([proj(1j * (T @ Bk[k] - Bk[k] @ T)) for k in range(5)]).T
cas = sum(Rm(T).T @ Rm(T) for T in TL)
cy = Rm(Y).T @ Rm(Y)
ec, ey = np.sort(np.linalg.eigvalsh((cas + cas.T) / 2)), np.sort(np.linalg.eigvalsh((cy + cy.T) / 2))
check(np.allclose(ec, [0, .75, .75, .75, .75]) and np.allclose(ey, [0, .25, .25, .25, .25]), "B2 [T]",
      "Goldstones at theta = 0: one Y = 1/2 doublet (SU2 Casimir 3/4, Y^2 = 1/4) + one neutral singlet eta",
      f"C2 {np.round(ec, 3)}, Y^2 {np.round(ey, 3)}")
# anomalies with the Sp(2) index: (Sp2, SU2L, Y)
cont = [(2, 2, Fr(0)), (2, 1, Fr(1, 2)), (2, 1, Fr(-1, 2))]
an = (sum(a * b * y for a, b, y in cont), sum(a * b * y ** 3 for a, b, y in cont),
      sum(a * y for a, b, y in cont if b == 2), sum(b * y for a, b, y in cont if a == 2))
wL, wS, wL1 = sum(a for a, b, y in cont if b == 2), sum(b for a, b, y in cont if a == 2), 1
check(an == (0, 0, 0, 0) and wL % 2 == 0 and wS % 2 == 0 and wL1 % 2 == 1, "B3 [T]",
      "with the index: Y, Y^3, SU2_L^2 Y, Sp2^2 Y anomalies vanish and both Witten counts are even; without it the "
      "single (2)_0 has an odd SU(2)_L Witten count", f"{tuple(str(a) for a in an)}; doublets SU2_L {wL}, Sp2 {wS}; no-index {wL1}")
# top term: m_t^2 = y^2 f^2 sum_al |Sig_{al,S+}|^2 ; theorem: O(g^2), O(y^2) invariants linear in sin^2
tt = np.linspace(0.05, 1.5, 9)
mt2 = np.array([abs(Sig(t)[0, 2]) ** 2 + abs(Sig(t)[1, 2]) ** 2 for t in tt])
gsum = np.array([sum(gg ** 2 * np.linalg.norm(act(X, Sig(t))) ** 2 for gg, X in
                     [(G, TL[0]), (G, TL[1]), (G, TL[2]), (GP, Y)]) for t in tt])
fitres = max(np.abs(np.polyval(np.polyfit(np.sin(tt) ** 2, v, 1), np.sin(tt) ** 2) - v).max() for v in (mt2, gsum))
check(np.allclose(mt2, np.sin(tt) ** 2) and fitres < 1e-12, "B4 [T]", "the top's Yukawa-type term (q t^c)(D S+) "
      "gives m_t = y f sin theta exactly; its O(y^2) and the gauge O(g^2) invariants are linear in sin^2 theta: "
      "no interior minimum without a further term", f"linear-fit residual {fitres:.0e}")
print("   species-mass term -B cos(theta) (Sp(4)-keeping mass of the new modes, supplied):")
print("   V = -A sin^2 - B cos  ->  cos th* = B/2A;  V''(th*) = 2A sin^2 th*;  d ln xi/d ln B = -2 cot^2 th*")


def Ifn(m2, L2):                              # int_0^L2 x ln(1 + m2/x) dx
    return 0.5 * (L2 ** 2 * np.log1p(m2 / L2) + m2 * L2 - m2 ** 2 * np.log1p(L2 / m2)) if m2 > 0 else 0.0


def V0(th, f, y, Lt):
    s2 = np.sin(th) ** 2
    mw2, mz2 = G ** 2 * f * f * s2 / 4, (G ** 2 + GP ** 2) * f * f * s2 / 4
    return -NC / (8 * PI ** 2) * Ifn((y * f) ** 2 * s2, Lt ** 2) + 3 / (32 * PI ** 2) * (2 * Ifn(mw2, Lt ** 2)
                                                                                        + Ifn(mz2, Lt ** 2))


def mh(lam, xi, mt=M_T):
    f = V_EW / np.sqrt(xi); y = mt / V_EW; th = np.arcsin(np.sqrt(xi)); h = 1e-4
    d1 = (V0(th + h, f, y, lam * f) - V0(th - h, f, y, lam * f)) / (2 * h)
    B = -d1 / np.sin(th)
    V = lambda t: V0(t, f, y, lam * f) - B * np.cos(t)
    d2 = (V(th + h) - 2 * V(th) + V(th - h)) / h ** 2
    return np.sqrt(max(d2, 0)) / f, B


tab = {lam: mh(lam, 0.05)[0] for lam in (1, 2, 3, 5, 10)}
l125 = {xi: brentq(lambda l: mh(l, xi)[0] - M_H, 0.5, 20) for xi in (0.05, 0.02)}
l125b = brentq(lambda l: mh(l, 0.05, 150.0)[0] - M_H, 0.5, 20)
sens = {xi: 2 * (1 - xi) / xi for xi in (0.05, 0.02, 0.0025)}
check(mh(3, 0.05)[1] > 0 and 2 < l125[0.05] < 4, "B5 [F]", "one-loop sea energy (4D cutoff Lt on top and W/Z "
      "terms) + species mass tuned to the minimum: m_H grows with Lt/f (~0.26 (Lt/f) m_t at large Lt); 125.1 GeV needs Lt/f FITTED",
      "m_H(Lt/f=1,2,3,5,10; xi=.05) = " + ",".join(f"{v:.0f}" for v in tab.values()) +
      f"; FITTED Lt/f = {l125[0.05]:.2f} (xi .05), {l125[0.02]:.2f} (.02), {l125b:.2f} (m_t 150); vacuum-angle "
      f"sensitivity 2cot^2 = {sens[0.05]:.0f}, {sens[0.02]:.0f}, {sens[0.0025]:.0f} at xi = .05, .02, .0025")
# NJL (mean-field quartic binder, N_hc = 2): f^2/m^2 = (2/4pi^2)(ln(1+x^2) - x^2/(1+x^2)), x = Lambda/m
Fx = lambda x: 2 / (4 * PI ** 2) * (np.log1p(x * x) - x * x / (1 + x * x))
xs = np.logspace(-1, 2, 3000)
lf_min = min(x / np.sqrt(Fx(x)) for x in xs)
mh_cut = mh(lf_min, 0.05)[0]
x125 = brentq(lambda x: 1 / np.sqrt(Fx(x)) - l125[0.05], 1.0, 1e3)
mh_cell = mh(1 / np.sqrt(Fx(M_CELL / 3e3)), 0.05)[0]
check(mh_cut > 3 * M_H, "B6 [F]", "mean-field binder: f/Lambda <= 0.105, so a top term cut at Lambda gives m_H >= "
      "~3x measured; cut at the constituent mass m_psi, m_H runs from ~430 GeV (Lambda ~ m) down to tens of GeV "
      "(Lambda = cell); 125 needs Lambda/m FITTED",
      f"Lambda/f >= {lf_min:.1f} -> m_H >= {mh_cut:.0f}; Lt = m_psi: FITTED Lambda/m = {x125:.2f}; "
      f"Lambda = cell: m_H = {mh_cell:.0f} GeV")
# cell-local top term: natural coefficient 1/M^2 (ETC suppression) or cell-scale quadratic
f05 = V_EW / np.sqrt(0.05); mpsi = l125[0.05] * f05; Lam = x125 * mpsi
cond = 2 * mpsi * (Lam ** 2 - mpsi ** 2 * np.log1p(Lam ** 2 / mpsi ** 2)) / (4 * PI ** 2)
enh = 33.8 ** (4.5 / 12)
mt_nat = enh * cond / M_CELL ** 2
mh_nat = 0.25 * (M_CELL / f05) * M_T
check(mt_nat < 1e-20 and (M_H / mh_nat) ** 2 < 1e-28, "B7 [E]", "a cell-local Yukawa-type term (coefficient "
      "1/M^2, the laws' only scale) gives m_t = <psi psi>_M/M^2; raising its coefficient to fit m_t makes the "
      "top's mass local up to the cell and m_H cell-sized",
      f"m_t(natural) ~ {mt_nat:.0e} GeV vs 172.6; else cancellation (m_H/m_H,nat)^2 ~ {(M_H / mh_nat) ** 2:.0e}")

# ---------------------------------------------------------------- C
print("== C. the scale f")
b0 = Fr(11, 3) * 2 - Fr(2, 3) * Fr(1, 2) * 4
b1 = Fr(34, 3) * 4 - 4 * Fr(3, 4) * Fr(1, 2) * 2 - Fr(20, 3) * 2 * Fr(1, 2) * 2
n_need = [np.log2(M_CELL / f) for f in (1.09e3, 3e3)]
ia = [n * float(b0) * LN2 / (2 * PI) for n in n_need]
reads = [8 * PI ** 2 * k / (float(b0) * LN2) for k in (0.5, 1, 2, 4, 8, 16)]
ia2 = 1 / (G ** 2 / (4 * PI)) + (19 / 6) / (2 * PI) * np.log(1.09e3 / 91.19) + 2.5 / (2 * PI) * np.log(M_CELL / 1.09e3)
n_su2 = 2 * PI * ia2 / (float(b0) * LN2)
check(b0 == 6 and b1 == 29 and min(abs(r - 50) for r in reads) > 10 and n_su2 - n_need[0] > 10, "C1 [T/E]",
      "the index's Sp(2) (forced by the link rule once the index exists): b0 = 6, b1 = 29; f/M = 2^-n with "
      "1/alpha_cell FITTED; count readings and an SU(2)_L-equal cell coupling miss",
      f"needed n {n_need[1]:.1f}-{n_need[0]:.1f}, FITTED 1/alpha_cell {ia[1]:.1f}-{ia[0]:.1f} (sensitivity "
      f"{n_need[0] * LN2:.0f}); readings n {','.join(f'{r:.1f}' for r in reads)}; 1/alpha_2(M) {ia2:.1f} -> n {n_su2:.1f}")
dcrit = (3e3 / M_CELL) ** 2 * np.log1p((M_CELL / 3e3) ** 2)
check(dcrit < 1e-25, "C2 [T/E]", "quartic binder at the cell without a gauge factor: f << M needs (g - g_c)/g_c "
      "~ (m/M)^2 ln(M^2/m^2)", f"{dcrit:.1e} (FITTED)")
lv_coef = (1 / 137.036) / (3 * PI) * 8 * 0.25 / 2
lam_min = 1e11 * np.sqrt(lv_coef)
n_max = np.log2(PI * M_CELL / lam_min)
check(n_max < 40, "C3 [E/M]", "sector read on a coarse rung (f = 2^-n M by an integer): its lattice enters the "
      "photon's dispersion through the charged constituents' loop, quadratic LV scale ~ Lambda_B/sqrt(alpha/3pi)",
      f"bound E_QG2 > ~1e11 GeV -> Lambda_B > {lam_min:.0e} GeV, rung n <= {n_max:.0f}; TeV rung n ~ 51 excluded")

# ---------------------------------------------------------------- D
print("== D. estimates against measurement (conditional on the inserted content)")
xi_max = 1 - (1.035 - 1.96 * 0.031) ** 2
cw2 = G ** 2 / (G ** 2 + GP ** 2)
Sm, Se, Tm, Te, rho = -0.05, 0.07, 0.00, 0.06, 0.93
Cst = np.array([[Se ** 2, rho * Se * Te], [rho * Se * Te, Te ** 2]])


def st(xi):
    lg = np.log((4 * PI * V_EW / np.sqrt(xi)) ** 2 / M_H ** 2)
    return xi / (12 * PI) * lg + 2 * xi / (6 * PI), -3 * xi / (16 * PI * cw2) * lg


chi = lambda xi: (lambda d: d @ np.linalg.solve(Cst, d))(np.array(st(xi)) - [Sm, Tm]) if xi > 0 else \
    np.array([-Sm, -Tm]) @ np.linalg.solve(Cst, np.array([-Sm, -Tm]))
dchi = lambda xi: chi(xi) - chi(0)
xi_st = brentq(lambda x: dchi(x) - 3.84, 1e-4, 0.5)
dS, dT = st(0.05)
check(abs(xi_max - 0.051) < 2e-3 and xi_st < xi_max, "D1 [E/M]", "kappa_V = kappa_t = cos theta bounds xi; T = 0 at "
      "tree level (custodial Sp(4)); the IR running (dS > 0, dT < 0, Lambda = 4 pi f) plus a constituent S gives a "
      "stronger bound than kappa_V with these (approximate, U = 0) S, T inputs",
      f"kappa_V: xi <= {xi_max:.3f} (f >= {V_EW / np.sqrt(xi_max) / 1e3:.2f} TeV); xi = .05: dS = {dS:.3f}, "
      f"dT = {dT:.3f}, dchi2 = {dchi(0.05):.1f}; S,T: xi <= {xi_st:.3f} (f >= {V_EW / np.sqrt(xi_st) / 1e3:.2f} TeV)")
print("supplied: the 8 modes and their charges (INSERTED, gate FAIL), Sp(2) index, top term, species mass B,")
print("  4D sharp cutoff, NJL mean field, gamma0/(2b0) enhancement, LV bound 1e11 GeV; measured: v, m_H, m_t, g, g',")
print("  kappa_V = 1.035(31), S = -0.05(7), T = 0.00(6). FITTED: Lt/f or Lambda/m, B (vacuum angle), 1/alpha_cell.")
print("   GATE: (1) FITTED numbers above; (2) content inserted by charge -> FAIL; (3) kappa_V = kappa_t = cos th and\n"
      "   an eta singlet are consequences, untested against data beyond the bounds; (4) bends Lattice (new role sites).")
print(f"elapsed_seconds {time.time() - T0:.1f}")
print(f"TOTAL: PASS={NP} FAIL={NF}")

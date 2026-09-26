#!/usr/bin/env python3
"""Exact checks: relabellings in time whose clock profile varies in space need no new term in the walker's coupling through
first order in the strain. A time relabelling with profile xi0 moves the walker by its own smeared generator
exp(-i u (1/2){xi0, H_s}) (unitary: the time shift together with the coin's boost); then H' - H_s = -(i u/2)[xi0, H_s^2] (+ the
lapse's own term for profiles that vary in time), and this equals exactly the walker's coupling to the member's new shift
N'^k = g^{jk} d_j xi0, (1/2){N', -i d} plus block 163's frame-rotation coupling, at orders u and u s (continuum, smooth
zero-corner states, half-densities, the lengths' symmetric frame, zero background lapse and shift; the supervisor's own).

A (premises): landed block 150's clock rules (the lattice matches the member's exactly for uniform profiles, and through second
   order in the profiles' wave numbers otherwise).
B (T1): order u: the principal part is the shift term with N' = grad xi0 and the residual vanishes (all basis profiles).
C (T2): order u s: on all 600 basis pairs the principal part is the shift term with the metric-raised gradient
   N'^k = g^{jk} d_j xi0, and the residual vanishes once block 163's coupling (1/4) sigma_c eps_cab (e L_N E)_ab is included.
D (T3): without block 163's coupling the residual is nonzero (so the lapse sector needs it too); block 158's (1/8) eps.C does
   not enter at this order.
Exact arithmetic over the Gaussian rationals; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from sympy.polys.domains import QQ, QQ_I
from sympy.polys.rings import ring


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_RELABELLINGS_IN_TIME_WHOSE_CLOCK_PROFILE_VARIES_IN_SPACE_NEED_NO_NEW_TERM_THE_WALKERS_OWN_GENERATOR_MOVES_IT_AS_THE_MEMBERS_SHIFT_CHANGES_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_EVERY_CLOCK_PROFILE_A_RELABELLING_FORCES_THE_WHOLE_MOMENTUM_CONSTRAINT_AND_NO_POSITIVE_INERTIA_CAN_BE_ADDED_TO_THE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_the_walkers_own_generator_moves_it_as_the_members_shift_changes_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "flat_shift_sign_forged": "B",
    "shift_raise_forged": "C",
    "v163_coefficient_forged": "C",
    "necessity_forged": "D",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()

# ============================================================================================ fields near a point
LC = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
def lc(a, b, c): return LC.get((a, b, c), 0)
SYM = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
MONS = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 2, 0), (0, 1, 1), (0, 0, 2)]
R, X1, X2, X3, TT, S_, U_ = ring("X1 X2 X3 T s u", QQ_I)
X = [X1, X2, X3]; I_ = R(QQ_I(0, 1)); ONE, ZERO = R.one, R.zero
def qi(p, q=1): return QQ_I(QQ(p, q), 0)
def tr(p):
    return R({m: c for m, c in p.items() if m[0] + m[1] + m[2] <= 2 and m[3] <= 1 and m[4] <= 1 and m[5] <= 1})
def d(p, k): return p.diff(X[k])
def dt(p): return R({m[:3] + (m[3] - 1,) + m[4:]: c * m[3] for m, c in p.items() if m[3] >= 1})
def t0(p): return R({m: c for m, c in p.items() if m[3] == 0})
def at0(p, ks, ku):
    for m, c in p.items():
        if m == (0, 0, 0, 0, ks, ku): return c
    return QQ_I(0)
def mono(m): return X1 ** m[0] * X2 ** m[1] * X3 ** m[2]
mm = lambda A, B: [[tr(sum((A[p][q] * B[q][r] for q in range(3)), ZERO)) for r in range(3)] for p in range(3)]
def inv(e):
    A = [[e[a][b] - (ONE if a == b else ZERO) for b in range(3)] for a in range(3)]
    A2 = mm(A, A)
    return [[tr((ONE if a == b else ZERO) - A[a][b] + A2[a][b]) for b in range(3)] for a in range(3)]
def pmul(A, B):
    a0, a = A[0], A[1:]; b0, b = B[0], B[1:]
    out = [tr(a0 * b0 + a[0] * b[0] + a[1] * b[1] + a[2] * b[2])]
    for f in range(3):
        cr = sum((lc(f, g, h) * a[g] * b[h] for g in range(3) for h in range(3) if lc(f, g, h)), ZERO)
        out.append(tr(a0 * b[f] + b0 * a[f] + I_ * cr))
    return out
def pcomm(A, B):
    P, Q = pmul(A, B), pmul(B, A); return [P[i] - Q[i] for i in range(4)]
def padd(*As): return [tr(sum((A[i] for A in As), ZERO)) for i in range(4)]
def psc(c, A): return [tr(c * A[i]) for i in range(4)]
def framed(E):
    M = [[ZERO] + [tr(-I_ * E[j][a]) for a in range(3)] for j in range(3)]
    M0 = [ZERO] + [tr(-I_ / 2 * sum((d(E[j][a], j) for j in range(3)), ZERO)) for a in range(3)]
    return M, M0
def axial(e):
    E = inv(e); tot = ZERO
    for (a, b, c), sg in LC.items():
        for i in range(3):
            for j in range(3):
                tot += sg * E[i][b] * E[j][c] * (d(e[a][j], i) - d(e[a][i], j))
    return tr(tot)

def run(eta, zeta, xi, chi):
    s, u, T = S_, U_, TT
    etat = [[tr(eta[a][i] + T * zeta[a][i]) for i in range(3)] for a in range(3)]
    xit = [tr(xi[k] + T * chi[k]) for k in range(3)]
    e = [[tr((ONE if a == i else ZERO) + s * etat[a][i]) for i in range(3)] for a in range(3)]
    Le = [[tr(sum((xit[k] * d(e[a][i], k) + e[a][k] * d(xit[k], i) for k in range(3)), ZERO)) for i in range(3)] for a in range(3)]
    ALe = [[tr((Le[a][b] - Le[b][a]) / 2) for b in range(3)] for a in range(3)]
    Th0 = [[R({m: c for m, c in ALe[a][b].items() if m[4] == 0}) for b in range(3)] for a in range(3)]
    A1 = [[R({m[:4] + (0, 0): c for m, c in ALe[a][b].items() if m[4] == 1}) for b in range(3)] for a in range(3)]
    Th0h, hTh0 = mm(Th0, etat), mm(etat, Th0)
    Th1 = [[tr(A1[a][b] - (Th0h[a][b] + hTh0[a][b]) / 2) for b in range(3)] for a in range(3)]
    Th = [[tr(Th0[a][b] + s * Th1[a][b]) for b in range(3)] for a in range(3)]
    The = mm(Th, e)
    W = [[tr(-Le[a][i] + The[a][i]) for i in range(3)] for a in range(3)]
    th = [tr(sum((lc(a, b, c) * Th[a][c] for a in range(3) for c in range(3) if lc(a, b, c)), ZERO) / 2) for b in range(3)]
    K = [ZERO] + [tr(-I_ / 2 * th[b]) for b in range(3)]
    Kdot = [t0(dt(k)) for k in K]
    # everything at t = 0
    e0 = [[t0(e[a][i]) for i in range(3)] for a in range(3)]
    W0 = [[t0(W[a][i]) for i in range(3)] for a in range(3)]
    Wd = [[t0(dt(W[a][i])) for i in range(3)] for a in range(3)]
    K0 = [t0(k) for k in K]
    xi0 = [t0(k) for k in xit]
    eP = [[tr(e0[a][i] + u * W0[a][i]) for i in range(3)] for a in range(3)]
    M, M0 = framed(inv(e0)); MP, M0P = framed(inv(eP))
    B0 = axial(e0); BP = axial(eP)
    Bmat = [B0 * qi(1, 8)] + [ZERO] * 3
    divxi = sum((d(xi0[k], k) for k in range(3)), ZERO)
    N = []
    for j in range(3):
        t1 = padd(*[psc(xi0[k], [d(M[j][c], k) for c in range(4)]) for k in range(3)])
        t2 = padd(*[psc(d(xi0[j], k), M[k]) for k in range(3)])
        N.append(padd(M[j], psc(-u, t1), psc(u, t2), psc(u, pcomm(K0, M[j]))))
    dK = [[d(K0[c], j) for c in range(4)] for j in range(3)]
    M0B = padd(M0, Bmat)
    N0 = padd(M0B, psc(-u, padd(*[psc(xi0[k], [d(M0B[c], k) for c in range(4)]) for k in range(3)])),
              psc(u * qi(1, 2), padd(*[psc(d(divxi, j), M[j]) for j in range(3)])),
              psc(-u, padd(*[pmul(M[j], dK[j]) for j in range(3)])), psc(u, pcomm(K0, M0B)))
    # i u dX/dt = u * (-i chi.d - (i/2) div chi) + i u Kdot
    divchi = sum((d(chi[k], k) for k in range(3)), ZERO)
    for j in range(3):
        N[j] = padd(N[j], [tr(-I_ * u * chi[j])] + [ZERO] * 3)
    N0 = padd(N0, [tr(-I_ / 2 * u * divchi)] + [ZERO] * 3, psc(I_ * u, Kdot))
    # target (known part): framed walk of e' + B'/8 + (1/2){u chi, -i d} = -i u chi.d - (i/2) u div chi
    NP = [padd(MP[j], [tr(-I_ * u * chi[j])] + [ZERO] * 3) for j in range(3)]
    N0P = padd(M0P, [BP * qi(1, 8)] + [ZERO] * 3, [tr(-I_ / 2 * u * divchi)] + [ZERO] * 3)
    out = {"dparts": [at0(N[j][c] - NP[j][c], k, 1) for j in range(3) for c in range(4) for k in (0, 1)],
           "res": {(c, k): at0(N0[c] - N0P[c], k, 1) for c in range(4) for k in (0, 1)}}
    # data for the unknown couplings at x = 0
    out["Wd"] = {(a, i, k): at0(Wd[a][i], k, 0) for (a, i) in SYM for k in (0, 1)}
    out["W0"] = {(a, i, k): at0(W0[a][i], k, 0) for (a, i) in SYM for k in (0, 1)}
    out["K0"] = [at0(K0[c], 0, 0) for c in range(4)]
    return out

def basis_sym(P):
    (a, i), m = P
    M = [[ZERO] * 3 for _ in range(3)]
    M[a][i] = mono(m); M[i][a] = mono(m)
    return M
def basis_vec(Q):
    k, m = Q
    return [mono(m) if kk == k else ZERO for kk in range(3)]
ZM = [[ZERO] * 3 for _ in range(3)]; ZV = [ZERO] * 3

def framed_full(e):
    E = inv(e)
    M, M0 = framed(E)
    B = axial(e)
    M0 = padd(M0, [tr(B * qi(1, 8))] + [ZERO] * 3)
    return E, M, M0
def V163(e, N):
    """(1/4) sig_c eps_cab (e (L_N E))_ab with (L_N E_b)^i = N^j d_j E^i_b - E^j_b d_j N^i (static: no d_t term)."""
    E = inv(e)
    v = [ZERO, ZERO, ZERO, ZERO]
    for (c, a, b), sg in LC.items():
        tot = ZERO
        for i in range(3):
            LNE = sum((N[j] * d(E[i][b], j) - E[j][b] * d(N[i], j) for j in range(3)), ZERO)
            tot += e[a][i] * LNE
        v[1 + c] = tr(v[1 + c] + sg * tot / 4)
    return v
def run_lapse(eta, xi0):
    s, u = S_, U_
    e = [[tr((ONE if a == i else ZERO) + s * eta[a][i]) for i in range(3)] for a in range(3)]
    E, M, M0 = framed_full(e)
    # H^2 = A_jk d_j d_k + B_k d_k + C
    A = [[pmul(M[j], M[k]) for k in range(3)] for j in range(3)]
    Bk = [padd(*([pmul(M[j], [d(M[k][c], j) for c in range(4)]) for j in range(3)] + [pmul(M0, M[k]), pmul(M[k], M0)])) for k in range(3)]
    # -(i u/2)[xi0, H^2] = (i u/2)(sum A_jk d_j d_k xi0 + sum_k (sum_j (A_jk + A_kj) d_j xi0) d_k + sum_k B_k d_k xi0)
    deriv = []
    for k in range(3):
        deriv.append(psc(I_ * u / 2, padd(*[psc(d(xi0, j), padd(A[j][k], A[k][j])) for j in range(3)])))
    zeroth = psc(I_ * u / 2, padd(*([psc(d(d(xi0, j), k), A[j][k]) for j in range(3) for k in range(3)] + [psc(d(xi0, k), Bk[k]) for k in range(3)])))
    g_inv = [[tr(sum((E[i][a] * E[j][a] for a in range(3)), ZERO)) for j in range(3)] for i in range(3)]
    Np = [tr(shift_sign * sum((g_inv[k][j] * d(xi0, j) for j in range(3)), ZERO)) for k in range(3)]
    tgt_deriv = [[tr(-I_ * u * Np[k])] + [ZERO] * 3 for k in range(3)]
    tgt_zero = padd([tr(-I_ * u / 2 * sum((d(Np[k], k) for k in range(3)), ZERO))] + [ZERO] * 3, psc(u, V163(e, Np)))
    out = {"dparts": [at0(deriv[k][c] - tgt_deriv[k][c], ks, 1) for k in range(3) for c in range(4) for ks in (0, 1)],
           "res": {(c, ks): at0(zeroth[c] - tgt_zero[c], ks, 1) for c in range(4) for ks in (0, 1)},
           "res_noV": {(c, ks): at0(zeroth[c] - tgt_zero[c] + psc(u, V163(e, Np))[c], ks, 1) for c in range(4) for ks in (0, 1)}}
    return out


def v163_scaled(e, N, factor):
    v = V163(e, N)
    return [tr(x * factor) for x in v]


def run_l(eta, xi0, v_factor, raise_metric=True, with_b=True, shift_sign=1):
    s, u = S_, U_
    e = [[tr((ONE if a == i else ZERO) + s * eta[a][i]) for i in range(3)] for a in range(3)]
    E = inv(e)
    M, M0 = framed(E)
    if with_b:
        M0 = padd(M0, [tr(axial(e) * qi(1, 8))] + [ZERO] * 3)
    A = [[pmul(M[j], M[k]) for k in range(3)] for j in range(3)]
    Bk = [padd(*([pmul(M[j], [d(M[k][c], j) for c in range(4)]) for j in range(3)] + [pmul(M0, M[k]), pmul(M[k], M0)])) for k in range(3)]
    deriv = [psc(I_ * u / 2, padd(*[psc(d(xi0, j), padd(A[j][k], A[k][j])) for j in range(3)])) for k in range(3)]
    zeroth = psc(I_ * u / 2, padd(*([psc(d(d(xi0, j), k), A[j][k]) for j in range(3) for k in range(3)] + [psc(d(xi0, k), Bk[k]) for k in range(3)])))
    if raise_metric:
        g_inv = [[tr(sum((E[i][a] * E[j][a] for a in range(3)), ZERO)) for j in range(3)] for i in range(3)]
    else:
        g_inv = [[ONE if i == j else ZERO for j in range(3)] for i in range(3)]
    Np = [tr(shift_sign * sum((g_inv[k][j] * d(xi0, j) for j in range(3)), ZERO)) for k in range(3)]
    tgt_deriv = [[tr(-I_ * u * Np[k])] + [ZERO] * 3 for k in range(3)]
    tgt_zero = padd([tr(-I_ * u / 2 * sum((d(Np[k], k) for k in range(3)), ZERO))] + [ZERO] * 3, psc(u, v163_scaled(e, Np, v_factor)))
    return ([at0(deriv[k][c] - tgt_deriv[k][c], ks, 1) for k in range(3) for c in range(4) for ks in (0, 1)],
            {(c, ks): at0(zeroth[c] - tgt_zero[c], ks, 1) for c in range(4) for ks in (0, 1)})


EB = [(p, m) for p in SYM for m in MONS]


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walker's coupling, the member's relabellings and the comparator are supplied)")
    needle = "the walker's clocks close for a uniform lapse, but not for all pairs."
    if mut("landed_quote_forged"):
        needle = needle.replace("but not", "and")
    checks.check("A3", needle in texts[2], "landed block 150: the walker's clock rules match the member's exactly when one clock profile is uniform, and on the lattice only through second order in the profiles' wave numbers otherwise")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    sgn = -1 if mut("flat_shift_sign_forged") else 1
    for m in MONS:
        dp, res = run_l(ZM, mono(m), qi(1), shift_sign=sgn)
        ok &= all(not v for v in dp) and all(not res[(c, 0)] for c in range(4))
    checks.check("B1", ok, "order u (flat): for all 10 basis clock profiles, -(i u/2)[xi0, H^2] is exactly the shift term (1/2){u grad xi0, -i d}: principal parts agree and nothing is left")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    okd = okr = True
    raise_m = not mut("shift_raise_forged")
    fac = qi(1, 2) if mut("v163_coefficient_forged") else qi(1)
    for P in EB:
        Sm = basis_sym(P)
        for m in MONS:
            dp, res = run_l(Sm, mono(m), fac, raise_metric=raise_m)
            okd &= all(not v for v in dp)
            okr &= all(not res[(c, 1)] for c in range(4))
    checks.check("C1", okd and okr, "order u s, all 600 basis pairs (strain jets x clock-profile jets): the principal part is the shift term with the metric-raised gradient N'^k = g^{jk} d_j xi0, and the residual vanishes with block 163's coupling (1/4) sigma_c eps_cab (e L_N E)_ab")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    nz_without = 0
    nz_noB = 0
    for P in EB:
        Sm = basis_sym(P)
        for m in MONS:
            _, res0 = run_l(Sm, mono(m), qi(0))
            nz_without += any(res0[(c, 1)] for c in range(4))
            _, resB = run_l(Sm, mono(m), qi(1), with_b=False)
            nz_noB += any(resB[(c, 1)] for c in range(4))
    need = 0 if mut("necessity_forged") else 1
    checks.check("D1", nz_without >= need and nz_without > 0 if need else nz_without == 0, f"without block 163's coupling the residual at order u s is nonzero on {nz_without} of 600 basis pairs, so the lapse sector needs it as well")
    checks.check("D2", nz_noB == 0, "block 158's (1/8) eps.C does not enter at this order (it is second order in the strain): the residual vanishes with or without it")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 101, 136 and 150 as landed on main (the walker's framed coupling, the rate as a multiplier, the shift and the clock rules); it reports what relabellings in time with clock profiles that vary in space require of the walker's coupling, through first order in the strain, at leading order in the spacing; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the lapse."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Ivanenko", "Belinfante", "Rosenfeld", "Cartan", "Kibble",
                   "Sciama", "Hehl", "Wilson", "Pauli", "Fierz", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton",
                   "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Weyl) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the smeared generator's commutator with H^2 as an operator at a point",
    "per_site: executed - all 10 basis clock profiles at first order",
    "per_mode: executed - all 600 basis pairs of strain jets and clock-profile jets at order u s",
    "per_block: executed - with and without block 163's coupling, with and without block 158's term",
    "lattice_wide: checked and not executed - second order in the strain, background lapse and shift, the lattice (block 150's defect at higher wave numbers), and the eight species",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: relabellings in time with clock profiles varying in space, continuum, zero background lapse and shift, through first order in the strain: the walker's own smeared generator moves it as the member's shift changes (N' = g^-1 grad xi0) with block 163's coupling, which is needed, and no new term; own derivation; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line

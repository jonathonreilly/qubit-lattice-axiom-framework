#!/usr/bin/env python3
"""Exact checks: the walker coupled to the member's lengths through the symmetric frame keeps the member's relabellings at
first order; at the next order (strain times relabelling) it misses them by a coin scalar, and exactly one local term
restores them, (1/8) of the frame's inversion-odd curl eps.C, which is the comparator's connection term (leading order in
the spacing, smooth states of the zero-corner species; not adopted).

A (premise): the framed walk on half-densities is exactly covariant under relabellings when its frame is dragged along.
B (T1): the comparator's two-component operator on half-densities minus the framed walk is (1/8) eps.C times the identity,
   with no vector part, through second order, for general and for symmetric frames; for symmetric frames eps.C vanishes at
   first order and equals 2 eps_abc eta_aq d_b eta_cq at second.
C (T2): with the coin rotation that keeps the frame symmetric, the relabelled framed walk equals the framed walk of the new
   lengths at order u, and at order u s up to a coin scalar t = (change of eps.C)/8 = -(1/8) eps_abc (eta d S + S d eta);
   t is not zero (a stretched rod twisted about its axis: t = -lambda tau / 4).
D (T3): among local potentials with at most one derivative (constant-free; linear or quadratic in the strain; scalar or coin
   vector) exactly one restores the relabellings at orders u and u s: (1/8) eps.C times the identity; a coin rotation beyond
   the fixed one breaks the frame's symmetry, and a phase adds only a coin-vector term.
Exact arithmetic over the Gaussian rationals (sympy polynomial rings, domain matrices over Q); identities bilinear in the
jets are proved on every pair of basis jets. The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
import time
from pathlib import Path

from sympy.polys.domains import QQ, QQ_I
from sympy.polys.matrices import DomainMatrix
from sympy.polys.rings import ring


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_WALKER_ON_THE_MEMBERS_LENGTHS_KEEPS_RELABELLINGS_AT_FIRST_ORDER_AND_AT_THE_NEXT_NEEDS_EXACTLY_ONE_TERM_THE_COMPARATORS_INVERSION_ODD_CURL_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_walker_on_the_members_lengths_keeps_relabellings_at_first_order_and_at_the_next_needs_exactly_one_term_the_comparators_inversion_odd_curl_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "half_density_weight_forged": "A",
    "axial_coefficient_forged": "B",
    "compensating_rotation_forged": "C",
    "uniqueness_target_forged": "D",
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
LC = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}


def lc(a, b, c):
    return LC.get((a, b, c), 0)


SYM = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
MONS = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0), (1, 1, 0), (1, 0, 1), (0, 2, 0), (0, 1, 1), (0, 0, 2)]

# ============================================================================================ fields near a point
# Fields are polynomials in x1..x3 kept to total degree 2 (every identity below involves at most two derivatives at the
# point x = 0), with bookkeeping parameters s (size of the strain, kept to degree 1) and u (size of the relabelling, kept
# to degree 1), over the Gaussian rationals. Coin-matrix fields are 4-lists [p0, p1, p2, p3] = p0 + sum_f p_f sigma_f.
R, X1, X2, X3, S_, U_ = ring("X1 X2 X3 s u", QQ_I)
X = [X1, X2, X3]
I_ = R(QQ_I(0, 1))          # QQ_I(a, b) is a + b i


def qi(p, q=1):
    """the rational p/q as a Gaussian rational"""
    return QQ_I(QQ(p, q), 0)

ONE, ZERO = R.one, R.zero


def tr(p):
    return R({m: c for m, c in p.items() if m[0] + m[1] + m[2] <= 2 and m[3] <= 1 and m[4] <= 1})


def mono(m):
    return X1 ** m[0] * X2 ** m[1] * X3 ** m[2]


def at0(p, ks, ku):
    for m, c in p.items():
        if m == (0, 0, 0, ks, ku):
            return c
    return QQ_I(0)


def d(p, k):
    return p.diff(X[k])


def mm(A, B):
    return [[tr(sum((A[p][q] * B[q][r] for q in range(3)), ZERO)) for r in range(3)] for p in range(3)]


def inv(e):
    """(1 + A)^-1 through second order in the small matrix A = e - 1."""
    A = [[e[a][b] - (ONE if a == b else ZERO) for b in range(3)] for a in range(3)]
    A2 = mm(A, A)
    return [[tr((ONE if a == b else ZERO) - A[a][b] + A2[a][b]) for b in range(3)] for a in range(3)]


def pmul(A, B):
    a0, a = A[0], A[1:]
    b0, b = B[0], B[1:]
    out = [tr(a0 * b0 + a[0] * b[0] + a[1] * b[1] + a[2] * b[2])]
    for f in range(3):
        cr = sum((lc(f, g, h) * a[g] * b[h] for g in range(3) for h in range(3) if lc(f, g, h)), ZERO)
        out.append(tr(a0 * b[f] + b0 * a[f] + I_ * cr))
    return out


def pcomm(A, B):
    P, Q = pmul(A, B), pmul(B, A)
    return [P[i] - Q[i] for i in range(4)]


def padd(*As):
    return [tr(sum((A[i] for A in As), ZERO)) for i in range(4)]


def psc(c, A):
    return [tr(c * A[i]) for i in range(4)]


def framed(E):
    """The framed walk at long wavelength on half-densities, H = (1/2){E^j_a sigma_a, -i d_j} = sum_j M_j d_j + M_0,
    from the frame vectors E[j][a] = E^j_a."""
    M = [[ZERO] + [tr(-I_ * E[j][a]) for a in range(3)] for j in range(3)]
    M0 = [ZERO] + [tr(-I_ / 2 * sum((d(E[j][a], j) for j in range(3)), ZERO)) for a in range(3)]
    return M, M0


def axial(e):
    """eps.C = eps^{abc} C_abc, C_abc = E^i_b E^j_c (d_i e^a_j - d_j e^a_i), from the covector frame e[a][i]."""
    E = inv(e)
    tot = ZERO
    for (a, b, c), sg in LC.items():
        for i in range(3):
            for j in range(3):
                tot += sg * E[i][b] * E[j][c] * (d(e[a][j], i) - d(e[a][i], j))
    return tr(tot)


def relabel(eta, xi, rotate=True, weight=None, second_order_rotation=True):
    """Relabel the walker and its lengths by the flow of u*xi (pushforward: psi -> psi - u(xi.d psi + weight div xi psi),
    e -> e - u L_xi e) and, if rotate, turn the coin by the rotation that keeps the covector frame e = 1 + s eta symmetric.
    Returns the quantities at x = 0 used by the checks."""
    s, u = S_, U_
    weight = qi(1, 2) if weight is None else weight
    e = [[tr((ONE if a == i else ZERO) + s * eta[a][i]) for i in range(3)] for a in range(3)]
    Le = [[tr(sum((xi[k] * d(e[a][i], k) + e[a][k] * d(xi[k], i) for k in range(3)), ZERO)) for i in range(3)] for a in range(3)]
    ALe = [[tr((Le[a][b] - Le[b][a]) / 2) for b in range(3)] for a in range(3)]
    Th0 = [[R({m: c for m, c in ALe[a][b].items() if m[3] == 0}) for b in range(3)] for a in range(3)]
    A1 = [[R({m[:3] + (0, 0): c for m, c in ALe[a][b].items() if m[3] == 1}) for b in range(3)] for a in range(3)]
    Th0h, hTh0 = mm(Th0, eta), mm(eta, Th0)
    Th1 = [[tr(A1[a][b] - (Th0h[a][b] + hTh0[a][b]) / 2) for b in range(3)] for a in range(3)]
    if not second_order_rotation:
        Th1 = [[ZERO] * 3 for _ in range(3)]
    Th = [[tr(Th0[a][b] + s * Th1[a][b]) if rotate else ZERO for b in range(3)] for a in range(3)]
    The = mm(Th, e)
    W = [[tr(-Le[a][i] + The[a][i]) for i in range(3)] for a in range(3)]
    eP = [[tr(e[a][i] + u * W[a][i]) for i in range(3)] for a in range(3)]
    th = [tr(sum((lc(a, b, c) * Th[a][c] for a in range(3) for c in range(3) if lc(a, b, c)), ZERO) / 2) for b in range(3)]
    K = [ZERO] + [tr(-I_ / 2 * th[b]) for b in range(3)]           # coin rotation U = 1 + u K turns sigma-vectors by + th x
    M, M0 = framed(inv(e))
    MP, M0P = framed(inv(eP))
    divxi = sum((d(xi[k], k) for k in range(3)), ZERO)
    N = []
    for j in range(3):
        t1 = padd(*[psc(xi[k], [d(M[j][c], k) for c in range(4)]) for k in range(3)])
        t2 = padd(*[psc(d(xi[j], k), M[k]) for k in range(3)])
        N.append(padd(M[j], psc(-u, t1), psc(u, t2), psc(u, pcomm(K, M[j]))))
    dK = [[d(K[c], j) for c in range(4)] for j in range(3)]
    N0 = padd(M0, psc(-u, padd(*[psc(xi[k], [d(M0[c], k) for c in range(4)]) for k in range(3)])),
              psc(u * weight, padd(*[psc(d(divxi, j), M[j]) for j in range(3)])),
              psc(-u, padd(*[pmul(M[j], dK[j]) for j in range(3)])), psc(u, pcomm(K, M0)))
    out = {"asym": [at0(tr(eP[a][i] - eP[i][a]), k, 1) for a in range(3) for i in range(3) for k in (0, 1)],
           "dparts": [at0(N[j][c] - MP[j][c], k, 1) for j in range(3) for c in range(4) for k in (0, 1)]}
    res = [N0[c] - M0P[c] for c in range(4)]
    out["t"] = {(c, k): at0(res[c], k, 1) for c in range(4) for k in (0, 1)}
    B0, BP = axial(e), axial(eP)
    Btr = tr(B0 - u * sum((xi[k] * d(B0, k) for k in range(3)), ZERO))
    out["dB1"] = at0(BP - Btr, 1, 1)
    Sx = [[d(xi[j], i) + d(xi[i], j) for j in range(3)] for i in range(3)]
    out["cross"] = at0(tr(sum((sg * (eta[a][q] * d(Sx[c][q], b) + Sx[a][q] * d(eta[c][q], b)) for (a, b, c), sg in LC.items() for q in range(3)), ZERO)), 0, 0)
    out["W"] = {(a, i, k): [at0(W[a][i], k, 0)] + [at0(d(W[a][i], j), k, 0) for j in range(3)] for (a, i) in SYM for k in (0, 1)}
    out["K0"] = [at0(K[c], 0, 0) for c in range(4)]
    out["M"] = M
    return out


def basis_eta(P, sym=True):
    (a, i), m = P
    eta = [[ZERO] * 3 for _ in range(3)]
    eta[a][i] = mono(m)
    if sym:
        eta[i][a] = mono(m)
    return eta


def basis_xi(Q):
    k, m = Q
    return [mono(m) if kk == k else ZERO for kk in range(3)]


EB = [(p, m) for p in SYM for m in MONS]
XB = [(k, m) for k in range(3) for m in MONS]
ZERO_ETA = [[ZERO] * 3 for _ in range(3)]
RUNS: dict = {}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walker's coupling, the member's relabellings and the comparator are supplied)")
    w = qi(1) if mut("half_density_weight_forged") else qi(1, 2)
    ok = True
    for P in EB:
        eta = basis_eta(P)
        for Q in XB:
            o = relabel(eta, basis_xi(Q), rotate=False, weight=w)
            ok &= all(not v for v in o["dparts"]) and all(not o["t"][(c, k)] for c in range(4) for k in (0, 1))
    for Q in XB:
        o = relabel(ZERO_ETA, basis_xi(Q), rotate=False, weight=w)
        ok &= all(not v for v in o["dparts"]) and all(not o["t"][(c, 0)] for c in range(4))
    checks.check("A3", ok, "the framed walk on half-densities, relabelled with its frame dragged along (no coin rotation), is exactly the framed walk of the dragged frame at orders u and u s, on all 1800 pairs of basis jets")


# ============================================================================================ family B
def comparator_minus_framed(sym: bool):
    """At a point, the comparator's operator on half-densities minus the framed walk (both with principal part
    -i sigma_a E^j_a d_j), for the covector frame e = 1 + s eta with generic jets eta(0), d eta(0); s kept to degree 2."""
    pairs = [(a, i) for a in range(3) for i in range(3) if (not sym or a <= i)]
    names = [f"v{a}{i}" for (a, i) in pairs] + [f"d{a}{i}_{k}" for (a, i) in pairs for k in range(3)] + ["s"]
    Rb, *G = ring(names, QQ_I)
    g = dict(zip(names, G))
    s = g["s"]
    I = Rb(QQ_I(0, 1))          # the imaginary unit
    one, zero = Rb.one, Rb.zero
    isx = names.index("s")

    def trb(p):
        return Rb({m: c for m, c in p.items() if m[isx] <= 2})

    def ent(a, i, k=None):
        key = (a, i) if (a, i) in pairs else (i, a)
        return g[f"v{key[0]}{key[1]}"] if k is None else g[f"d{key[0]}{key[1]}_{k}"]

    def mmb(A, B):
        return [[trb(sum((A[p][q] * B[q][r] for q in range(3)), zero)) for r in range(3)] for p in range(3)]

    e0 = [[(one if a == i else zero) + s * ent(a, i) for i in range(3)] for a in range(3)]
    de = [[[s * ent(a, i, k) for i in range(3)] for a in range(3)] for k in range(3)]      # de[k][a][i] = d_k e^a_i
    A = [[e0[a][i] - (one if a == i else zero) for i in range(3)] for a in range(3)]
    A2 = mmb(A, A)
    E0 = [[trb((one if i == a else zero) - A[i][a] + A2[i][a]) for a in range(3)] for i in range(3)]
    dE = [[[-x for x in row] for row in mmb(mmb(E0, de[k]), E0)] for k in range(3)]       # dE[k][i][a] = d_k E^i_a
    dg = [[[trb(sum((de[k][a][i] * e0[a][j] + e0[a][i] * de[k][a][j] for a in range(3)), zero)) for j in range(3)] for i in range(3)] for k in range(3)]
    gi = [[trb(sum((E0[i][a] * E0[j][a] for a in range(3)), zero)) for j in range(3)] for i in range(3)]
    Chr = [[[trb(sum((gi[k][l] * (dg[i][l][j] + dg[j][l][i] - dg[l][i][j]) for l in range(3)), zero) / 2) for j in range(3)] for i in range(3)] for k in range(3)]

    def om(j, a, b):     # connection coefficients omega_{j a b} = e^a_k (d_j E^k_b + Gamma^k_{jl} E^l_b)
        return trb(sum((e0[a][k] * (dE[j][k][b] + sum((Chr[k][j][l] * E0[l][b] for l in range(3)), zero)) for k in range(3)), zero))

    dlog = [trb(sum((gi[i][j] * dg[k][i][j] for i in range(3) for j in range(3)), zero)) for k in range(3)]
    D0 = zero
    Dv = [zero, zero, zero]
    for j in range(3):
        Gv = [trb(I / 4 * sum((om(j, a, b) * lc(a, b, c) for a in range(3) for b in range(3)), zero)) for c in range(3)]   # (1/8) omega_jab [sigma_a, sigma_b]
        Gs = -dlog[j] / 4                                                                                                   # half-density weight
        for a in range(3):
            c0 = -I * E0[j][a]
            D0 = trb(D0 + c0 * Gv[a])
            for c in range(3):
                Dv[c] = trb(Dv[c] + c0 * ((Gs if c == a else zero) + I * sum((lc(a, b, c) * Gv[b] for b in range(3)), zero)))
            Dv[a] = trb(Dv[a] + I / 2 * dE[j][j][a])                                                                        # minus the framed walk's zeroth-order part
    B = trb(sum((sg * E0[i][b] * E0[j][c] * (de[i][a][j] - de[j][a][i]) for (a, b, c), sg in LC.items() for i in range(3) for j in range(3)), zero))
    coef = qi(1, 4) if mut("axial_coefficient_forged") else qi(1, 8)
    q2 = sum((sg * 2 * ent(a, qq) * ent(c, qq, b) for (a, b, c), sg in LC.items() for qq in range(3)), zero) * s ** 2
    Bs = {k: Rb({m: c for m, c in B.items() if m[isx] == k}) for k in (1, 2)}
    return trb(D0 - coef * B) == 0, all(v == 0 for v in Dv), Bs, q2


def family_b(checks: Checks) -> None:
    okS, okV, Bs, _ = comparator_minus_framed(sym=False)
    checks.check("B1", okS and okV and Bs[1] != 0, "general covector frame e = 1 + s eta, generic jets: the comparator's operator on half-densities minus the framed walk is (1/8) eps.C times the identity with no vector part, through s^2 (eps.C is already nonzero at order s)")
    okS, okV, Bs, q2 = comparator_minus_framed(sym=True)
    checks.check("B2", okS and okV and Bs[1] == 0 and Bs[2] == q2, "symmetric frame (the lengths' own): the same identity through s^2; eps.C vanishes at order s and equals 2 eps_abc eta_aq d_b eta_cq at order s^2")


# ============================================================================================ family C
def compute_runs(rot2: bool) -> dict:
    runs = {}
    for Q in XB:
        runs[(None, Q)] = relabel(ZERO_ETA, basis_xi(Q), second_order_rotation=rot2)
    for P in EB:
        eta = basis_eta(P)
        for Q in XB:
            runs[(P, Q)] = relabel(eta, basis_xi(Q), second_order_rotation=rot2)
    return runs


def family_c(checks: Checks) -> None:
    rot2 = not mut("compensating_rotation_forged")
    runs = RUNS if rot2 else compute_runs(False)
    ok0 = True
    for Q in XB:
        o = runs[(None, Q)]
        ok0 &= all(not v for v in o["asym"]) and all(not v for v in o["dparts"]) and all(not o["t"][(c, 0)] for c in range(4))
    checks.check("C1", ok0, "order u (first order): with the coin turned by the rotation part of the relabelling, the new frame is symmetric and the relabelled framed walk is the framed walk of the new lengths, no residual (all 30 basis relabellings)")
    ok_sym = ok_d = ok_vec = ok_B = ok_x = True
    nonzero = 0
    for P in EB:
        for Q in XB:
            o = runs[(P, Q)]
            ok_sym &= all(not v for v in o["asym"])
            ok_d &= all(not v for v in o["dparts"])
            ok_vec &= all(not o["t"][(c, 1)] for c in (1, 2, 3))
            t = o["t"][(0, 1)]
            ok_B &= not (t - o["dB1"] / 8)
            ok_x &= not (t + o["cross"] / 8)
            nonzero += bool(t)
    checks.check("C2", ok_sym and ok_d and ok_vec, "order u s, all 1800 pairs of basis jets: the new frame is symmetric, the derivative terms are the new frame's, and the residual has no coin-vector part")
    checks.check("C3", ok_B and ok_x and nonzero > 0, f"order u s: the residual is the coin scalar t = (change of eps.C)/8 = -(1/8) eps_abc (eta_aq d_b S_cq + S_aq d_b eta_cq), S = d xi + d xi^T; so framed walk + eps.C/8 keeps the relabelling; t is nonzero on {nonzero} basis pairs")
    eta = [[ZERO] * 3 for _ in range(3)]
    eta[0][0] = ONE
    o = relabel(eta, [ZERO, -X1 * X3, X1 * X2], second_order_rotation=rot2)
    checks.check("C4", o["t"][(0, 1)] == qi(-1, 4) and all(not o["t"][(c, 1)] for c in (1, 2, 3)), "example: a rod stretched by lambda along axis 1 (eta_11 = lambda) and twisted about that axis by tau per unit length (xi = tau x1 (0, -x3, x2)): t = -lambda tau / 4")


# ============================================================================================ family D
def jets_eta(P):
    pair, m = P
    al = SYM.index(pair)
    v = [0] * 6
    dv = [[0] * 3 for _ in range(6)]
    ddv = [[[0] * 3 for _ in range(3)] for _ in range(6)]
    if sum(m) == 0:
        v[al] = 1
    if sum(m) == 1:
        dv[al][m.index(1)] = 1
    if sum(m) == 2:
        for k in range(3):
            for b in range(3):
                mk = [0, 0, 0]
                mk[k] += 1
                mk[b] += 1
                if tuple(mk) == m:
                    ddv[al][k][b] = 2 if k == b else 1
    return v, dv, ddv


def re_(z):
    assert z.y == 0, "complex coefficient"
    return QQ(z.x)


def family_d(checks: Checks) -> None:
    unk = []
    for c in range(4):
        unk += [("z", c, al) for al in range(6)]
        unk += [("y", c, al, be) for al in range(6) for be in range(al, 6)]
        unk += [("L", c, al, b) for al in range(6) for b in range(3)]
        unk += [("T", c, al, b, be) for al in range(6) for b in range(3) for be in range(6)]
    col = {k: i for i, k in enumerate(unk)}
    rows, rhs = [], []
    for Q in XB:
        o = RUNS[(None, Q)]
        W = o["W"]
        for c in range(4):
            row = {}
            for al, pair in enumerate(SYM):
                w = W[(pair[0], pair[1], 0)]
                row[col[("z", c, al)]] = row.get(col[("z", c, al)], QQ(0)) + re_(w[0])
                for b in range(3):
                    row[col[("L", c, al, b)]] = row.get(col[("L", c, al, b)], QQ(0)) + re_(w[1 + b])
            rows.append(row)
            rhs.append(-re_(o["t"][(c, 0)]))
    for P in EB:
        v, dv, ddv = jets_eta(P)
        for Q in XB:
            o = RUNS[(P, Q)]
            W, K0 = o["W"], o["K0"]
            x0 = [0, 0, 0]
            if sum(Q[1]) == 0:
                x0[Q[0]] = 1
            W0 = [W[(p[0], p[1], 0)] for p in SYM]
            W1 = [W[(p[0], p[1], 1)] for p in SYM]
            for c in range(4):
                row = {}

                def add(key, val):
                    if val:
                        row[col[key]] = row.get(col[key], QQ(0)) + val
                for al in range(6):
                    add(("z", c, al), -re_(W1[al][0]))
                    for b in range(3):
                        add(("L", c, al, b), -re_(W1[al][1 + b]))
                    add(("z", c, al), -QQ(sum(x0[k] * dv[al][k] for k in range(3))))
                    for b in range(3):
                        add(("L", c, al, b), -QQ(sum(x0[k] * ddv[al][k][b] for k in range(3))))
                    for be in range(al, 6):
                        add(("y", c, al, be), -(re_(W0[be][0]) * v[al] + re_(W0[al][0]) * v[be]))
                    for b in range(3):
                        for be in range(6):
                            add(("T", c, al, b, be), -(v[al] * re_(W0[be][1 + b]) + re_(W0[al][0]) * dv[be][b]))
                if c >= 1:
                    f = c - 1
                    for g in range(3):
                        for h in range(3):
                            if not lc(g, h, f):
                                continue
                            coef = re_(QQ_I(0, 2) * lc(g, h, f) * K0[1 + g])
                            for al in range(6):
                                add(("z", h + 1, al), coef * v[al])
                                for b in range(3):
                                    add(("L", h + 1, al, b), coef * dv[al][b])
                rows.append(row)
                rhs.append(-re_(o["t"][(c, 1)]))
    n = len(unk)
    A = DomainMatrix([[r.get(j, QQ(0)) for j in range(n)] for r in rows], (len(rows), n), QQ)
    Ab = DomainMatrix([[r.get(j, QQ(0)) for j in range(n)] + [b] for r, b in zip(rows, rhs)], (len(rows), n + 1), QQ)
    rA, rAb = A.rank(), Ab.rank()
    rref, piv = Ab.rref()
    Mx = rref.to_Matrix()
    sol = [QQ(0)] * n
    for i, p in enumerate(piv):
        if p < n:
            sol[p] = QQ(Mx[i, n].p, Mx[i, n].q)
    tgt = [QQ(0)] * n
    scale = QQ(1, 2) if mut("uniqueness_target_forged") else QQ(1, 4)
    for (a, b, c), sg in LC.items():
        for q in range(3):
            al = SYM.index(tuple(sorted((a, q))))
            be = SYM.index(tuple(sorted((c, q))))
            tgt[col[("T", 0, al, b, be)]] += sg * scale
    checks.check("D1", rA == n and rAb == n and sol == tgt, f"{len(rows)} exact equations over Q in {n} unknowns (linear and quadratic, with and without one derivative, scalar and coin vector): rank {rA} = rank with the residual {rAb} = {n}, and the unique solution is (1/8) eps.C = (1/4) eps_abc eta_aq d_b eta_cq times the identity")
    # the coin's transformation law: an extra coin rotation rho changes the frame's antisymmetric part; a phase adds only a coin-vector term
    M = RUNS[(None, XB[0])]["M"]
    antisym_changed = True
    for f in range(3):
        rho = [ZERO] * 3
        rho[f] = ONE
        Kx = [ZERO] + [tr(-I_ / 2 * rho[b]) for b in range(3)]
        Ej = [[pcomm(Kx, M[j])[1 + a] * I_ for a in range(3)] for j in range(3)]      # change of E^j_a: M_j = -i E^j_a sigma_a
        antisym_changed &= any(at0(Ej[j][a] - Ej[a][j], 0, 0) for j in range(3) for a in range(3))
    phi = X1 * X2 + X3
    ph_scalar = sum((d(phi, j) * M[j][0] for j in range(3)), ZERO)
    ph_vec = [sum((d(phi, j) * M[j][1 + a] for j in range(3)), ZERO) for a in range(3)]
    checks.check("D2", antisym_changed and ph_scalar == 0 and any(ph_vec), "the walker's local law is fixed: a further coin rotation gives the frame an antisymmetric part (not the lengths' frame), and a phase phi adds -i M_j d_j phi, a pure coin-vector term, so neither removes a coin-scalar residual")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62 and 65 as landed on main (the walker's framed coupling, the member's lengths and relabellings, and what turning the coin does); it reports what the member's relabellings require of the walker's coupling at the order of the member's cubic completion, at leading order in the spacing; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at one term."}
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
    "per_element: executed - the comparator-minus-walk identity for every jet of a general and of a symmetric frame through second order",
    "per_site: executed - the relabelled walker at a point, on every pair of basis jets of the strain and the relabelling (1800 pairs, orders u and u s)",
    "per_mode: executed - the residual's closed form and its nonzero example (a stretched rod twisted about its axis)",
    "per_block: executed - the uniqueness system over Q (7320 equations, 612 unknowns) and the coin's transformation law",
    "lattice_wide: checked and not executed - the lattice placement of the term for the eight species, relabellings in time, and third order",
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
    RUNS.update(compute_runs(True))
    family_c(checks)
    family_d(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: the walker's framed coupling through the symmetric frame of the member's lengths, long wavelength, spatial relabellings; first order kept, order strain x relabelling missed by -(1/8) eps (eta dS + S d eta), restored uniquely by (1/8) eps.C (the comparator's term); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line

#!/usr/bin/env python3
"""Exact checks: relabellings that vary in time make the walker's coin turn with its frame. At first order the walker needs the
spin's coupling to the shift's vorticity, (1/4) sigma.curl N, which is the spin part of block 138's symmetric momentum; at
the next order it needs the coin's coupling to the frame's rotation rate relative to the shift's flow,
(1/4) sigma_c eps_cab (e (d_t + L_N) E)_ab; among local couplings with one derivative, linear in the shift or the frame's rate,
up to first order in the strain, scalar or coin vector, these are unique up to a multiple of the expansion rate, which time
reversal excludes (continuum, smooth zero-corner states, half-densities, spatial relabellings that vary in time, zero
background shift; the supervisor's own derivation).

A (premises): landed block 138's symmetric momentum P^B = P'' + (1/2) curl(S~/2).
B (T1): order u: on all 60 basis relabellings (static and time-varying) the principal parts agree, the shift absorbs the
   moving-relabelling term, and the residual is exactly (1/4) sigma.curl chi (chi = the relabelling's rate).
C (T2): order u s: the coupling (1/4) sigma.curl N + (1/4) sigma_c eps_cab [-(eta M)_ab + (M eta)_ab + (edot eta)_ab],
   M_ij = d_j N^i, solves all 29040 exact equations from the basis pairs.
D (T3): the system has 636 unknowns and rank 635; its one-dimensional kernel is the scalar expansion rate
   div N + N.grad tr(e - 1) + tr edot - tr((e - 1) edot), odd under time reversal.
E (T4): the comparator's connection along its time direction, from the 3+1 metric at a point, has rotation part
   antisym(e (d_t - L_N) E): with the note's sign of N, block 163's coupling is the comparator's.
Exact arithmetic over the Gaussian rationals; identities bilinear in the jets are proved on every pair of basis jets.
The runner scans its own source for floating-point literals.
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
    "docs/ADMISSIBILITY_RULE_RELABELLINGS_THAT_VARY_IN_TIME_MAKE_THE_WALKERS_COIN_TURN_WITH_ITS_FRAME_THE_SPIN_COUPLES_TO_THE_SHIFTS_VORTICITY_AND_THE_FRAMES_ROTATION_RATE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_the_spin_couples_to_the_shifts_vorticity_and_the_frames_rotation_rate_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLE = "`P^B = P″ + ½∇̄ × (S̃/2)`"

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "turning_rate_forged": "B",
    "candidate_sign_forged": "C",
    "kernel_forged": "D",
    "adm_sign_forged": "E",
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

# ============================================================================================ fields near a point, with time
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


IDXJ = [(j, k) for j in range(3) for k in range(3)]
UNK = []
for c in range(4):
    UNK += [("A0", c, j, k) for (j, k) in IDXJ]
    UNK += [("A1", c, q, j, k) for q in range(6) for (j, k) in IDXJ]
    UNK += [("A2", c, q, l, k) for q in range(6) for l in range(3) for k in range(3)]
    UNK += [("K0", c, p) for p in range(6)]
    UNK += [("K1", c, p, q) for p in range(6) for q in range(6)]
COL = {kk: i for i, kk in enumerate(UNK)}
EB = [(p, m) for p in SYM for m in MONS]
XB = [(k, m) for k in range(3) for m in MONS]


def re_(z):
    assert z.y == 0
    return QQ(z.x)


def jet_sym(P):
    pair, m = P
    q = SYM.index(pair)
    v = [0] * 6
    dv = [[0] * 3 for _ in range(6)]
    if sum(m) == 0:
        v[q] = 1
    if sum(m) == 1:
        dv[q][m.index(1)] = 1
    return v, dv


def jet_vec(Q):
    k, m = Q
    v = [0, 0, 0]
    dv = [[0] * 3 for _ in range(3)]
    if sum(m) == 0:
        v[k] = 1
    if sum(m) == 1:
        dv[m.index(1)][k] = 1
    return v, dv


def rows_for(o, strain, relab, order):
    ev, edv = ([0] * 6, [[0] * 3 for _ in range(6)])
    zv, zdv = ([0] * 6, [[0] * 3 for _ in range(6)])
    if strain[0] == "eta":
        ev, edv = jet_sym(strain[1])
    if strain[0] == "zeta":
        zv, zdv = jet_sym(strain[1])
    xv, xdv = ([0] * 3, [[0] * 3 for _ in range(3)])
    cv, cdv = ([0] * 3, [[0] * 3 for _ in range(3)])
    if relab[0] == "xi":
        xv, xdv = jet_vec(relab[1])
    if relab[0] == "chi":
        cv, cdv = jet_vec(relab[1])
    Wd, W0, K0v = o["Wd"], o["W0"], o["K0"]
    Wd0 = [re_(Wd[(p[0], p[1], 0)]) for p in SYM]
    Wd1 = [re_(Wd[(p[0], p[1], 1)]) for p in SYM]
    W00 = [re_(W0[(p[0], p[1], 0)]) for p in SYM]
    theta0 = [re_(QQ_I(0, 2) * K0v[1 + f]) for f in range(3)]
    out = []
    for c in range(4):
        row = {}

        def add(key, val):
            if val:
                row[COL[key]] = row.get(COL[key], QQ(0)) + QQ(val)
        if order == 0:
            for (j, k) in IDXJ:
                add(("A0", c, j, k), -cdv[j][k])
            for p in range(6):
                add(("K0", c, p), -Wd0[p])
            out.append((row, -re_(o["res"][(c, 0)])))
        else:
            for q in range(6):
                for (j, k) in IDXJ:
                    add(("A1", c, q, j, k), -ev[q] * cdv[j][k])
                for l in range(3):
                    for k in range(3):
                        add(("A2", c, q, l, k), -edv[q][l] * cv[k])
            for p in range(6):
                add(("K0", c, p), -Wd1[p])
                for q in range(6):
                    add(("K1", c, p, q), -(ev[q] * Wd0[p] + W00[q] * zv[p]))
                add(("K0", c, p), -sum(xv[k] * zdv[p][k] for k in range(3)))
            if c >= 1:
                f = c - 1
                for g in range(3):
                    for h in range(3):
                        if lc(f, g, h):
                            for p in range(6):
                                add(("K0", h + 1, p), lc(f, g, h) * theta0[g] * zv[p])
            out.append((row, -re_(o["res"][(c, 1)])))
    return out


SYSTEM: dict = {}


def build_system():
    rows, rhs = [], []
    first_ok = True
    okd = True
    fac = QQ(1, 2) if mut("turning_rate_forged") else QQ(1, 4)
    for Q in XB:
        for kind in ("xi", "chi"):
            rel = basis_vec(Q)
            o = run(ZM, ZM, rel if kind == "xi" else ZV, rel if kind == "chi" else ZV)
            okd &= all(not v for v in o["dparts"])
            cv, cdv = jet_vec(Q) if kind == "chi" else ([0] * 3, [[0] * 3 for _ in range(3)])
            curl = [sum(lc(f, j, k) * cdv[j][k] for j in range(3) for k in range(3)) for f in range(3)]
            first_ok &= re_(o["res"][(0, 0)]) == 0 and all(re_(o["res"][(1 + f, 0)]) == fac * curl[f] for f in range(3))
            for r, b in rows_for(o, (None, None), (kind, Q), 0):
                rows.append(r)
                rhs.append(b)
    for P in EB:
        Sm = basis_sym(P)
        for skind in ("eta", "zeta"):
            for Q in XB:
                for kind in ("xi", "chi"):
                    rel = basis_vec(Q)
                    o = run(Sm if skind == "eta" else ZM, Sm if skind == "zeta" else ZM, rel if kind == "xi" else ZV, rel if kind == "chi" else ZV)
                    okd &= all(not v for v in o["dparts"])
                    for r, b in rows_for(o, (skind, P), (kind, Q), 1):
                        rows.append(r)
                        rhs.append(b)
    SYSTEM.update(rows=rows, rhs=rhs, first_ok=first_ok, okd=okd)


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walker's coupling, the member's relabellings and the comparator are supplied)")
    needle = "`P^B = P″ − ½∇̄ × (S̃/2)`" if mut("landed_quote_forged") else LANDED_NEEDLE
    checks.check("A3", needle in texts[2], "landed block 138: the symmetric momentum that block 136 couples to the shift is the two-step momentum plus half the curl of the spin, P^B = P'' + (1/2) curl(S~/2)")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    checks.check("B1", SYSTEM["okd"] and SYSTEM["first_ok"], "order u, all 60 basis relabellings (static and time-varying) and then all 7200 basis pairs: the principal parts of the moved walker and of the walker of the new fields agree (the shift N' = u chi absorbs the moving relabelling), and at order u the residual is exactly (1/4) sigma.curl chi, the turning rate of the coin; so the walker needs (1/4) sigma.curl N")


# ============================================================================================ family C (T2)
def candidate():
    n = len(UNK)
    v = [QQ(0)] * n
    sgnK = -1 if mut("candidate_sign_forged") else 1

    def symidx(a, b):
        return SYM.index(tuple(sorted((a, b))))
    for (c_, a, b), sg in LC.items():
        c = c_ + 1
        v[COL[("A0", c, b, a)]] += QQ(-sg, 4)
        for dd in range(3):
            v[COL[("A1", c, symidx(a, dd), b, dd)]] += QQ(-sg, 4)
            v[COL[("A1", c, symidx(dd, b), dd, a)]] += QQ(sg, 4)
            v[COL[("K1", c, symidx(a, dd), symidx(dd, b))]] += QQ(sgnK * sg, 4)
    return v


def family_c(checks: Checks) -> None:
    v = candidate()
    ok = all(sum((r.get(j, QQ(0)) * v[j] for j in r), QQ(0)) == b for r, b in zip(SYSTEM["rows"], SYSTEM["rhs"]))
    checks.check("C1", ok, f"the coupling (1/4) sigma_c eps_cab (e (d_t + L_N) E)_ab, expanded to first order in the strain as (1/4) sigma.curl N + (1/4) sigma_c eps_cab [-(eta M)_ab + (M eta)_ab + (edot eta)_ab] with M_ij = d_j N^i, satisfies all {len(SYSTEM['rows'])} exact equations at orders u and u s")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    rows = SYSTEM["rows"]
    n = len(UNK)
    A = DomainMatrix([[r.get(j, QQ(0)) for j in range(n)] for r in rows], (len(rows), n), QQ)
    ns = A.nullspace().to_Matrix()
    want_dim = 0 if mut("kernel_forged") else 1
    ok = ns.rows == want_dim
    if ok and ns.rows == 1:
        kv = {UNK[j]: ns[0, j] for j in range(n) if ns[0, j] != 0}
        scalar_only = all(k[1] == 0 for k in kv)
        ref = kv.get(("A0", 0, 0, 0))
        expect = {}
        for j in range(3):
            expect[("A0", 0, j, j)] = 1
            for q in (0, 3, 5):
                expect[("A2", 0, q, j, j)] = 1
        for q in (0, 3, 5):
            expect[("K0", 0, q)] = 1
        for q in range(6):
            expect[("K1", 0, q, q)] = -(1 if q in (0, 3, 5) else 2)
        ok = scalar_only and ref is not None and set(kv) == set(expect) and all(kv[k] == ref * expect[k] for k in expect)
    checks.check("D1", ok, "the exact system in 636 unknowns (couplings linear in the shift's gradient, in the shift times the strain's gradient, or in the frame's rate, up to first order in the strain, scalar and coin vector) has rank 635; its kernel is one scalar coupling, the expansion rate div N + N.grad tr(e - 1) + tr edot - tr((e - 1) edot), odd under time reversal (the walk's Theta commutes with H, and edot, N are odd)")


# ============================================================================================ family E (T4: the comparator's connection along time)
def family_e(checks: Checks) -> None:
    import sympy as sp
    X = sp.symbols("t x1 x2 x3")
    s_, r_ = sp.symbols("s r")
    eta = [[None] * 3 for _ in range(3)]
    for (a, i) in SYM:
        p = sp.Symbol(f"h{a}{i}") + sum(sp.Symbol(f"h{a}{i}_{m}") * X[m] for m in range(4))
        eta[a][i] = eta[i][a] = p
    nu = [sp.Symbol(f"n{k}") + sum(sp.Symbol(f"n{k}_{m}") * X[m] for m in range(1, 4)) for k in range(3)]

    def trunc(ex):
        ex = sp.expand(ex)
        return sp.expand(sum(ex.coeff(s_, i).coeff(r_, j) * s_ ** i * r_ ** j for i in range(2) for j in range(2)))
    e = sp.Matrix(3, 3, lambda a, i: (1 if a == i else 0) + s_ * eta[a][i])
    E = (sp.eye(3) - s_ * sp.Matrix(3, 3, lambda a, i: eta[a][i])).T
    N = [r_ * nu[k] for k in range(3)]
    g = (e.T * e).applyfunc(trunc)
    G4 = sp.zeros(4, 4)
    G4[0, 0] = trunc(-1 + sum(g[i, j] * N[i] * N[j] for i in range(3) for j in range(3)))
    for i in range(3):
        G4[0, i + 1] = G4[i + 1, 0] = trunc(sum(g[i, j] * N[j] for j in range(3)))
        for j in range(3):
            G4[i + 1, j + 1] = g[i, j]
    eA = sp.zeros(4, 4)
    eA[0, 0] = 1
    for i in range(3):
        eA[0, i + 1] = -N[i]
    for a in range(3):
        for i in range(3):
            eA[a + 1, i + 1] = E[i, a]
    zero = {x: 0 for x in X}
    dd = lambda f, m: sp.diff(f, X[m])
    G0 = G4.subs(zero).applyfunc(trunc)
    gam_inv = (E * E.T).applyfunc(trunc)
    Gi = sp.zeros(4, 4)
    Gi[0, 0] = -1
    for i in range(3):
        Gi[0, i + 1] = Gi[i + 1, 0] = N[i]
        for j in range(3):
            Gi[i + 1, j + 1] = trunc(gam_inv[i, j] - N[i] * N[j])
    Gi0 = Gi.subs(zero).applyfunc(trunc)
    inv_ok = (G0 * Gi0).applyfunc(trunc) == sp.eye(4)
    dG = [[[trunc(dd(G4[m, n], l).subs(zero)) for l in range(4)] for n in range(4)] for m in range(4)]
    Chr = [[[trunc(sum(Gi0[k, l] * (dG[l][m][n] + dG[l][n][m] - dG[m][n][l]) for l in range(4)) / 2) for n in range(4)] for m in range(4)] for k in range(4)]
    eA0 = eA.subs(zero).applyfunc(trunc)
    omega = sp.zeros(3, 3)
    for b in range(3):
        nb = []
        for nu_ in range(4):
            v = sum(eA0[0, l] * trunc(dd(eA[b + 1, nu_], l).subs(zero)) for l in range(4))
            v += sum(Chr[nu_][l][k] * eA0[0, l] * eA0[b + 1, k] for l in range(4) for k in range(4))
            nb.append(trunc(v))
        for a in range(3):
            omega[a, b] = trunc(sum(G0[m, n] * eA0[a + 1, m] * nb[n] for m in range(4) for n in range(4)))
    sgn = 1 if mut("adm_sign_forged") else -1          # the comparator's derivative along its time direction is d_t - L_N
    LNE = sp.zeros(3, 3)
    for i in range(3):
        for b in range(3):
            LNE[i, b] = sum(N[j] * dd(E[i, b], j + 1) - E[j, b] * dd(N[i], j + 1) for j in range(3))
    DtE = sp.Matrix(3, 3, lambda i, b: dd(E[i, b], 0)) + sgn * LNE
    cand = (e * DtE).subs(zero).applyfunc(trunc)
    anti = lambda M: ((M - M.T) / 2).applyfunc(sp.expand)
    ok = inv_ok and anti(omega) == anti(cand) and ((omega + omega.T) / 2).applyfunc(sp.expand) == sp.zeros(3, 3)
    checks.check("E1", ok, "the comparator's connection along the time direction e_0 = d_t - N.d of the time-gauge tetrad of ds^2 = -dt^2 + g_ij (dx^i + N^i dt)(dx^j + N^j dt), computed from the 3+1 metric at a point with generic jets, is antisymmetric and equals antisym(e (d_t - L_N) E) at first order in the strain and the shift (their product kept); with the note's opposite sign for N this is block 163's coupling, (1/4) eps_abc omega_0ab sigma_c being the rotation part of the two-component operator's connection term")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 62, 65, 136 and 138 as landed on main (the walker's framed coupling, what turning the coin does, the shift and the symmetric momentum); it reports what relabellings that vary in time require of the walker's coupling to the shift and to the frame's rate, through first order in the strain, at leading order in the spacing; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the turning rate."}
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
    "per_element: executed - the moved walker at a point with time: principal parts, the moving term, the turning rate",
    "per_site: executed - all 60 basis relabellings (static and time-varying) at first order",
    "per_mode: executed - all 7200 basis pairs of strain or strain rate and relabelling or relabelling rate at order u s",
    "per_block: executed - the 29040-equation system: the candidate solves it, rank 635 of 636, the kernel is the expansion rate",
    "lattice_wide: checked and not executed - relabellings in time with varying clock profiles (the lapse), a background shift, second order in the strain, and the lattice placement",
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
    build_system()
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: spatial relabellings that vary in time, zero background shift, long wavelength: the walker needs (1/4) sigma.curl N at first order and the frame's rotation-rate coupling (1/4) sigma_c eps_cab (e (d_t + L_N) E)_ab at order strain x relabelling, unique up to the time-odd expansion rate; own derivation; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line

#!/usr/bin/env python3
"""Exact checks: no local tie makes the coin's rotation a bond strain. A tie B = T theta of the three site rotations to the nine
bond strains of block 64 whose response T^dagger J vanishes on every bounded stationary state of the infinite lattice is a
relabelling B = d(M theta), at every finite reach r, with M reading theta within r steps (the supervisor's own proof); the probes
found the same at reaches one and two on finite tori (#8853 with #8977, #9215 with #9320). With the rotations kept apart, block 64's
field-energy family has the four-factor solvability condition and the exponent of #8853 part (b) (with #8977). Blocks 63, 64, 65 as
landed.

A (premises): landed blocks 63, 64, 65; the axioms.
B (T1): the pair symbol of the strain coupling on plane waves, e^{iq.x} (e^{ik_a} + e^{-ik'_a})(s_j + s'_j)/4 chi'^dag sigma_a chi, and
   its divergence (i/2)(s_j + s'_j) chi'^dag (h(k) - h(k')) chi; a relabelling tie's symbol is -(1 - e^{-iq_a}) mu_j(q).
C (T2): six pairs of energy one at q0 = (q1, 0, 0), e^{iq1/2} = (4 + 3i)/5: their symbols are divergence-free and of rank six, the
   dimension of the divergence-free space; the implicit-function condition 2 sin q1 cos(2k1 - q1) != 0 holds at each.
D (T3): the chain lemma (a relabelling tie inside the reach-r stencils has M on the radius-r ball) and the count 3|ball_r|; the
   forward-bond tie fails at a certificate pair; the reach-one system of the 6^3 torus has rank 87 mod p (only relabellings).
E (T4): block 64's quadratic family on a plane wave: blind to bond rotations iff (c1, c2, c3) ~ (1, 2, -4); eigenvalues of the static
   form on the six transverse strains; the blind member's kernel is the bond rotations; beta = c4/(2(2c1 + c2 + 2c3)).
Exact (sympy; integer arithmetic mod p in D). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import numpy as np
import sympy as sp
from sympy import isprime
from sympy.ntheory import sqrt_mod


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_NO_LOCAL_TIE_MAKES_THE_COINS_ROTATION_A_BOND_STRAIN_EVERY_TIE_STATIONARY_CONTENT_CANNOT_FEEL_IS_A_RELABELLING_AT_EVERY_REACH_BOUNDED_THEOREM_NOTE_2026-09-27.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md",
    "docs/ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_no_local_tie_makes_the_coins_rotation_a_bond_strain_every_tie_stationary_content_cannot_feel_is_a_relabelling_at_every_reach_bounded_theorem_note_2026-09-27"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED63 = (
    "`i[H, G_ξ] = Σ_a Σ_j σ_a ½{C_a[d_aξ_j], S_j}`",
    "If `Hψ = Eψ` — or `ψ` is any superposition of eigenstates of one energy — the left side of (b) vanishes for every `ξ`",
    "`J_a^j = e^{iq_a/2} cos(k̄_a) Θ_a^j`",
    "Stationary means a superposition of eigenstates of one energy.",
)
LANDED64 = (
    "`H[B] = H + Σ_{a,j} σ_a ½{C_a[B_a^j], S_j}`",
    "block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 4c_3)`",
    "consider the strain `δB_a^j(x) = ω_{aj}(x)`: a rotation of the three bonds that leave `x`",
    "the second-order part of `D*` has zero variational derivative with respect to the antisymmetric part",
    "`T_1 = T^j_{kl}T^j_{kl}`, `T_2 = T^j_{kl}T^l_{kj}`, `T_3 = V_lV_l`",
)
LANDED65 = (
    "It vanishes at every site if psi is stationary under the unperturbed H.",
    "*A rotation of the bonds is not a rotation of the coin.*",
    "Which lattice variables carry the symmetric six numbers (bonds, by blocks 63 and 64) and which the rotation three (sites, by this note), in one formulation, is the named next step.",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "symbol_forged": "B",
    "span_forged": "C",
    "chain_forged": "D",
    "family_ratio_forged": "E",
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
I = sp.I
R = sp.Rational
SIG = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def vadd(u, v, s=1):
    return tuple(u[i] + s * v[i] for i in range(3))


def l1(v):
    return sum(abs(t) for t in v)


def sine(z):
    return sp.expand((z - 1 / z) / (2 * I))


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t63, t64, t65 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, the strains and the ties are supplied)")
    checks.check("A3", all(n in t63 for n in LANDED63), "landed block 63: the relabelling's deformation i[H, G_xi]; its response vanishes on stationary states; the pair form of the bond current; stationary = one energy")
    needles = list(LANDED64)
    if mut("landed_quote_forged"):
        needles[1] = "block 59's exponent is `β = c_4/(4c_1 + 2c_2 + 2c_3)`"
    checks.check("A4", all(n in t64 for n in needles), "landed block 64: the strain coupling H[B]; the exponent beta = c4/(4c1 + 2c2 + 4c3); the rotation of a site's bonds; the blind density ignores the antisymmetric strain; T1, T2, T3")
    checks.check("A5", all(n in t65 for n in LANDED65), "landed block 65: the coin's rotation response vanishes on stationary states; a rotation of the bonds is not a rotation of the coin; the named next step")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    z = sp.symbols("z1:4")
    w = sp.symbols("w1:4")
    c = sp.symbols("c1:3")
    d = sp.symbols("dbar1:3")
    chi = sp.Matrix(c)
    chipd = sp.Matrix([d]).reshape(1, 2)  # chi'^dagger

    def psi(y):
        return chi * sp.Mul(*[z[i] ** y[i] for i in range(3)])

    def psipd(y):
        return chipd * sp.Mul(*[w[i] ** (-y[i]) for i in range(3)])

    def S(f, j):
        return lambda y: (f(vadd(y, E3[j])) - f(vadd(y, E3[j], -1))) / (2 * I)

    def C(f, a, x0):
        xa = vadd(x0, E3[a])

        def g(y):
            out = sp.zeros(2, 1)
            if y == x0:
                out += f(xa) / 2
            if y == xa:
                out += f(x0) / 2
            return out
        return g

    ok = True
    quarter = R(1, 4) if not mut("symbol_forged") else R(1, 2)
    for x0 in ((0, 0, 0), (1, 2, 3)):
        window = [y for y in itertools.product(range(-2, 6), repeat=3)]
        for a in range(3):
            for j in range(3):
                t1 = S(C(psi, a, x0), j)   # S_j C psi
                t2 = C(S(psi, j), a, x0)   # C S_j psi
                tot = 0
                for y in window:
                    if l1(vadd(y, x0, -1)) > 3:
                        continue
                    v = (t1(y) + t2(y)) / 2
                    if v == sp.zeros(2, 1):
                        continue
                    tot += (psipd(y) * SIG[a] * v)[0]
                M = (chipd * SIG[a] * chi)[0]
                phase = sp.Mul(*[(z[i] / w[i]) ** x0[i] for i in range(3)])
                want = quarter * phase * (z[a] + 1 / w[a]) * (sine(z[j]) + sine(w[j])) * M
                ok = ok and sp.simplify(sp.expand(tot - want)) == 0
    checks.check("B1", ok, "pair symbol: <psi'| sigma_a (1/2){C_a[delta_x], S_j} |psi> = e^{iq.x} (e^{ik_a} + e^{-ik'_a})(s_j + s'_j)/4 chi'^dag sigma_a chi for plane waves chi e^{ik.y}, chi' e^{ik'.y}, q = k - k', at x = 0 and x = (1, 2, 3), all nine (a, j)")

    s = [sine(zz) for zz in z]
    sp_ = [sine(ww) for ww in w]
    ok = True
    for j in range(3):
        div = sum((1 - w[a] / z[a]) * R(1, 4) * (z[a] + 1 / w[a]) * (s[j] + sp_[j]) * (chipd * SIG[a] * chi)[0] for a in range(3))
        h = sum((s[a] * SIG[a] for a in range(3)), sp.zeros(2))
        hp = sum((sp_[a] * SIG[a] for a in range(3)), sp.zeros(2))
        want = (I / 2) * (s[j] + sp_[j]) * (chipd * (h - hp) * chi)[0]
        ok = ok and sp.simplify(sp.expand(div - want)) == 0
    checks.check("B2", ok, "divergence of the pair symbol: sum_a (1 - e^{-iq_a}) Jhat_a^j = (i/2)(s_j + s'_j) chi'^dag (h(k) - h(k')) chi; zero for eigen-coins of one energy (block 63 T3)")

    # a relabelling tie: c(a, j, d) = mu_j(d - e_a) - mu_j(d); its symbol sum_d c e^{-iq.d} = -(1 - e^{-iq_a}) mu_j(q)
    y = sp.symbols("y1:4")  # y_a = e^{-iq_a}
    mu = {(0, 0, 0): 3, (1, 0, 0): -2, (0, -1, 0): 5, (0, 0, 1): 7, (-1, 0, 0): 1}
    muhat = sum(v * sp.Mul(*[y[i] ** dd[i] for i in range(3)]) for dd, v in mu.items())
    ok = True
    for a in range(3):
        coeffs = {}
        for dd, v in mu.items():
            coeffs[vadd(dd, E3[a])] = coeffs.get(vadd(dd, E3[a]), 0) + v
            coeffs[dd] = coeffs.get(dd, 0) - v
        chat = sum(v * sp.Mul(*[y[i] ** dd[i] for i in range(3)]) for dd, v in coeffs.items())
        ok = ok and sp.expand(chat + (1 - y[a]) * muhat) == 0
    checks.check("B3", ok, "a relabelling tie B_a^j = xi_j(x + e_a) - xi_j(x), xi_j = sum mu_j(d) theta(x + d), has symbol chat_aj(q) = -(1 - e^{-iq_a}) muhat_j(q): its pairing with any divergence-free symbol vanishes")


# ============================================================================================ family C (T2)
def zfrom(s_, c_):
    return c_ + I * s_


ALPHA = zfrom(R(3, 5), R(4, 5))  # e^{i q1 / 2}
ONE = sp.Integer(1)


def certificate_pairs():
    pts = []
    b1 = (ALPHA, 1 / ALPHA)          # k1 = q1/2, k1' = -q1/2
    b2 = (I * ALPHA, I / ALPHA)      # k1 = q1/2 + pi/2, k1' = pi/2 - q1/2
    for (z2, z3) in [(zfrom(R(4, 5), R(3, 5)), ONE), (zfrom(R(4, 5), R(3, 5)), -ONE), (ONE, zfrom(R(4, 5), R(3, 5))), (-ONE, zfrom(R(4, 5), R(3, 5)))]:
        pts.append(([b1[0], z2, z3], [b1[1], z2, z3]))
    for (z2, z3) in [(zfrom(R(3, 5), R(4, 5)), ONE), (ONE, zfrom(R(3, 5), R(4, 5)))]:
        pts.append(([b2[0], z2, z3], [b2[1], z2, z3]))
    return pts


def pair_symbol(zk, zkp):
    s = [sine(t) for t in zk]
    s2 = [sine(t) for t in zkp]
    E2 = sp.expand(sum(t ** 2 for t in s))
    E2p = sp.expand(sum(t ** 2 for t in s2))
    E = sp.sqrt(E2)
    u = sp.Matrix([E + s[2], s[0] + I * s[1]])
    up = sp.Matrix([E + s2[2], s2[0] + I * s2[1]])
    h = sum((s[a] * SIG[a] for a in range(3)), sp.zeros(2))
    hp = sum((s2[a] * SIG[a] for a in range(3)), sp.zeros(2))
    eig = sp.simplify(h * u - E * u) == sp.zeros(2, 1) and sp.simplify(hp * up - E * up) == sp.zeros(2, 1)
    J = sp.zeros(3, 3)
    for a in range(3):
        M = sp.expand((up.H * SIG[a] * u)[0])
        for j in range(3):
            J[a, j] = sp.expand(R(1, 4) * (zk[a] + 1 / zkp[a]) * (s[j] + s2[j]) * M)
    return J, E2, E2p, eig, s


def family_c(checks: Checks):
    q1z = sp.expand(ALPHA ** 2)
    pts = certificate_pairs()
    if mut("span_forged"):
        pts = pts[:5] + [pts[4]]
    rows, ok_e, ok_q, ok_div, ok_ift, ok_cont = [], True, True, True, True, True
    w = [1 - 1 / q1z, 0, 0]
    sinq1 = sine(q1z)
    for zk, zkp in pts:
        ok_q = ok_q and [sp.simplify(zk[a] / zkp[a]) for a in range(3)] == [q1z, 1, 1]
        J, E2, E2p, eig, s = pair_symbol(zk, zkp)
        ok_e = ok_e and E2 == 1 and E2p == 1 and eig
        ok_div = ok_div and all(sp.simplify(sum(w[a] * J[a, j] for a in range(3))) == 0 for j in range(3))
        # d/dk1 [E(k)^2 - E(k - q)^2] = 2 sin q1 cos(2 k1 - q1); e^{i(2 k1 - q1)} = zk1^2 / q1z
        e2 = sp.expand(zk[0] ** 2 / q1z)
        cos2 = sp.expand((e2 + 1 / e2) / 2)
        ok_ift = ok_ift and sp.simplify(2 * sinq1 * cos2) != 0
        ok_cont = ok_cont and sp.simplify(1 + s[2]) > 0
        rows.append([J[a, j] for a in range(3) for j in range(3)])
    checks.check("C1", ok_q and ok_e, "six pairs (k, k') with e^{i(k - k')} = ((7 + 24i)/25, 1, 1): both energies exactly one, coins exact eigenvectors of s.sigma (four with k1 = q1/2, two with k1 = q1/2 + pi/2)")
    Mx = sp.Matrix(rows)
    wv = sp.Matrix([w])
    Dq = sp.Matrix(3, 9, lambda jj, col: w[col // 3] if col % 3 == jj else 0)
    checks.check("C2", ok_div and Dq.rank() == 3 and Mx.rank(simplify=True) == 6 and wv != sp.zeros(1, 3), "their symbols are divergence-free and have rank six, the dimension of the divergence-free space D(q0) (9 minus 3): they span it")
    x = sp.symbols("k1:4", real=True)
    qs = sp.symbols("q1:4", real=True)
    F = sum(sp.sin(x[a]) ** 2 - sp.sin(x[a] - qs[a]) ** 2 for a in range(3))
    G = sum(sp.sin(qs[a]) * sp.sin(2 * x[a] - qs[a]) for a in range(3))
    ident = sp.simplify(sp.expand_trig(F - G)) == 0
    checks.check("C3", ident and ok_ift and ok_cont, "E(k)^2 - E(k - q)^2 = sum_a sin q_a sin(2k_a - q_a); at each base pair its k1-derivative 2 sin q1 cos(2k1 - q1) = +-48/25 is non-zero and E + s_3 > 0: the pairs and their coins continue smoothly to every q near q0")
    return pts


# ============================================================================================ family D (T3)
def stencil(a, r):
    box = range(-r - 1, r + 3)
    return {dd for dd in itertools.product(box, repeat=3) if min(l1(dd), l1(vadd(dd, E3[a], -1))) <= r}


def chain_free_sites(r, pad=3):
    """union-find: mu(d) = mu(d - e_a) whenever d is outside the reach-r stencil of bond a; mu = 0 outside a box"""
    Rb = r + pad
    box = list(itertools.product(range(-Rb, Rb + 1), repeat=3))
    inbox = set(box)
    parent = {dd: dd for dd in box}
    parent["out"] = "out"

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u

    def union(u, v):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
    st = [stencil(a, r) for a in range(3)]
    for a in range(3):
        for dd in itertools.product(range(-Rb, Rb + 2), repeat=3):
            if dd in st[a]:
                continue
            u = dd if dd in inbox else "out"
            v = vadd(dd, E3[a], -1)
            v = v if v in inbox else "out"
            union(u, v)
    outroot = find("out")
    groups = {}
    for dd in box:
        groups.setdefault(find(dd), []).append(dd)
    return [g for rt, g in groups.items() if rt != outroot]


def family_d(checks: Checks, pts):
    ok = True
    counts = []
    for r in (1, 2, 3):
        comps = chain_free_sites(r)
        free = sorted(g[0] for g in comps) if all(len(g) == 1 for g in comps) else None
        ball = sorted(dd for dd in itertools.product(range(-r, r + 1), repeat=3) if l1(dd) <= r)
        nb = (2 * r + 1) * (2 * r * r + 2 * r + 3) // 3
        if mut("chain_forged"):
            nb += 1
        ok = ok and free == ball and len(ball) == nb
        counts.append(3 * nb)
    st_sizes = [len(stencil(0, 1)), len(stencil(0, 2))]
    checks.check("D1", ok and counts == [21, 75, 189] and st_sizes == [12, 38], f"chain lemma: inside the reach-r stencils (12 and 38 sites at r = 1, 2) a relabelling tie's M is supported exactly on the radius-r ball, each ball site free; ties per rotation component 3|ball_r| = (2r+1)(2r^2+2r+3) = {counts} at r = 1, 2, 3")

    # the forward-bond tie B_a^j(x) = eps_{abj} theta_b(x): chat_aj = eps_{abj}, constant; it fails at a certificate pair
    bad = []
    for b in range(3):
        viol = 0
        for zk, zkp in pts:
            J = pair_symbol(zk, zkp)[0]
            val = sum(int(sp.LeviCivita(a, b, j)) * J[a, j] for a in range(3) for j in range(3))
            viol += int(sp.simplify(val) != 0)
        bad.append(viol)
    checks.check("D2", all(v > 0 for v in bad), f"the forward-bond tie of issue #8659 (B_a^j = eps_abj theta_b(x)) pairs to non-zero with some certificate pair for each b (pairs violated: {bad}): not a relabelling, and T^dagger J != 0 on a stationary state")

    # the reach-one system on the 4^3 and 6^3 tori, mod p (the probes' method, #8853 with #8977)
    p = next(qq for qq in range(1 << 20, 1 << 21) if qq % 24 == 1 and isprime(qq))
    Ii, R2, R3 = sqrt_mod(p - 1, p), sqrt_mod(2, p), sqrt_mod(3, p)

    def inv(a_):
        return pow(int(a_) % p, p - 2, p)
    z6 = (1 + Ii * R3) * inv(2) % p
    emb = (Ii * Ii) % p == p - 1 and (R2 * R2) % p == 2 and (R3 * R3) % p == 3 and pow(z6, 6, p) == 1 and pow(z6, 3, p) == p - 1
    Dl = [[dd for dd in itertools.product(range(-2, 4), repeat=3) if min(l1(dd), l1(vadd(dd, E3[a], -1))) <= 1] for a in range(3)]
    cols = [(a, j, dd) for a in range(3) for j in range(3) for dd in Dl[a]]
    cidx = {cc: i for i, cc in enumerate(cols)}
    NC = len(cols)
    SG = [[[0, 1], [1, 0]], [[0, (p - Ii) % p], [Ii, 0]], [[1, 0], [0, p - 1]]]
    ID = [[1, 0], [0, 1]]

    def mm(A, B):
        return [[(A[i][0] * B[0][j] + A[i][1] * B[1][j]) % p for j in range(2)] for i in range(2)]

    def madd(A, B):
        return [[(A[i][j] + B[i][j]) % p for j in range(2)] for i in range(2)]

    def msc(cc, A):
        return [[cc * A[i][j] % p for j in range(2)] for i in range(2)]

    def system(Lt):
        zz = Ii if Lt == 4 else z6

        def ep(n):
            return pow(zz, n % Lt, p)

        def sn(n):
            return (ep(n) - ep(-n)) * inv(2 * Ii) % p
        shell = {}
        for kk in itertools.product(range(Lt), repeat=3):
            cnt = sum(1 for n in kk if (2 * n) % Lt != 0)
            shell.setdefault(cnt, []).append((kk, [sn(n) for n in kk]))
        rows = []
        for cnt, lst in shell.items():
            if cnt == 0:
                branches = [None]
            else:
                rr = {1: 1, 2: R2, 3: R3}[cnt] if Lt == 4 else {1: R3 * inv(2) % p, 2: R2 * R3 * inv(2) % p, 3: 3 * inv(2) % p}[cnt]
                branches = [rr, (p - rr) % p]
            for br in branches:
                Pt = {kk: (ID if br is None else madd(msc(br, ID), madd(msc(sv[0], SG[0]), madd(msc(sv[1], SG[1]), msc(sv[2], SG[2]))))) for kk, sv in lst}
                for (k1, s1), (k2, s2) in itertools.product(lst, lst):
                    qv = tuple((k2[i] - k1[i]) % Lt for i in range(3))
                    row = np.zeros((4, NC), dtype=np.int64)
                    Xa = [mm(mm(Pt[k1], SG[a]), Pt[k2]) for a in range(3)]
                    for ci, (a, j, dd) in enumerate(cols):
                        f = pow(zz, (-sum(qv[i] * dd[i] for i in range(3))) % Lt, p) * ((ep(k2[a]) + ep(-k1[a])) % p) % p * ((s2[j] + s1[j]) % p) % p
                        for e, (i1, i2) in enumerate(((0, 0), (0, 1), (1, 0), (1, 1))):
                            row[e, ci] = f * Xa[a][i1][i2] % p
                    rows.append(row)
        return np.concatenate(rows)

    def modrank(A):
        basis, piv = [], []
        A = A % p
        for s0 in range(0, A.shape[0], 4000):
            Cm = A[s0:s0 + 4000].copy()
            for bvec, pc in zip(basis, piv):
                Cm = (Cm - np.outer(Cm[:, pc], bvec)) % p
            for col in range(Cm.shape[1]):
                if col in piv:
                    continue
                nz = np.nonzero(Cm[:, col])[0]
                if len(nz) == 0:
                    continue
                rvec = Cm[nz[0]].copy() * inv(Cm[nz[0], col]) % p
                for i in range(len(basis)):
                    if basis[i][col]:
                        basis[i] = (basis[i] - basis[i][col] * rvec) % p
                Cm = (Cm - np.outer(Cm[:, col], rvec)) % p
                basis.append(rvec)
                piv.append(col)
        return len(basis)

    A4 = system(4)
    A6 = system(6)
    r4, r6 = modrank(A4), modrank(A6)
    star = [(0, 0, 0)] + [tuple(sg * E3[a][i] for i in range(3)) for a in range(3) for sg in (1, -1)]
    rel = []
    for j0 in range(3):
        for dp in star:
            t = [0] * NC
            for a in range(3):
                t[cidx[(a, j0, vadd(E3[a], dp))]] += 1
                t[cidx[(a, j0, dp)]] -= 1
            rel.append(t)
    relrank = sp.Matrix(rel).rank()
    relnp = np.array([[v % p for v in t] for t in rel], dtype=np.int64)
    kernel_ok = int(np.count_nonzero((A6 @ relnp.T) % p)) == 0 and int(np.count_nonzero((A4 @ relnp.T) % p)) == 0
    checks.check("D3", emb and relrank == 21 and kernel_ok and r6 == NC - 21 == 87 and r4 == 81 and A6.shape[0] == 125184, f"reach one on tori (the probes' method): Z[1/2][i, sqrt2, sqrt3] -> F_p, p = {p} = 1 mod 24; 6^3 has {A6.shape[0]} rows of rank {r6} = 108 - 21 mod p, so rank over the field >= 87 and the 21 relabelling ties (rank 21, all in the kernel) are all; 4^3 has rank {r4} (offsets 2 and -2 alias)")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    k = sp.symbols("kk1:4", real=True)

    def quadT(B, kv):
        Tt = {(j, a, b): I * (kv[a] * B[b, j] - kv[b] * B[a, j]) for j in range(3) for a in range(3) for b in range(3)}
        cj = sp.conjugate
        T1 = sum(Tt[(j, a, b)] * cj(Tt[(j, a, b)]) for j in range(3) for a in range(3) for b in range(3))
        T2 = sum(Tt[(j, a, b)] * cj(Tt[(b, a, j)]) for j in range(3) for a in range(3) for b in range(3))
        V = [sum(Tt[(a, a, b)] for a in range(3)) for b in range(3)]
        T3 = sum(V[b] * cj(V[b]) for b in range(3))
        return [sp.expand(sp.re(sp.expand(zz))) for zz in (T1, T2, T3)]

    c1, c2, c3, c4 = sp.symbols("c1 c2 c3 c4", real=True)
    Sr = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"s{min(i, j)}{max(i, j)}", real=True))
    al = sp.Matrix(sp.symbols("al1:4", real=True))
    Aa = sp.Matrix(3, 3, lambda a, j: sum(sp.LeviCivita(a, j, b) * al[b] for b in range(3)))

    def fam(qq):
        return c1 * qq[0] + c2 * qq[1] + c3 * qq[2]
    dA = sp.expand(fam(quadT(Sr + Aa, k)) - fam(quadT(Sr, k)))
    sol = sp.solve(sp.Poly(dA, *k, *al, *list(set(Sr))).coeffs(), [c1, c2, c3], dict=True)
    want = [{c1: -c3 / 4, c2: -c3 / 2}] if not mut("family_ratio_forged") else [{c1: -c3 / 4, c2: c3 / 2}]
    checks.check("E1", sol == want, "block 64's quadratic density c1 T1 + c2 T2 + c3 T3 of a plane-wave strain is independent of its antisymmetric part (the bond rotations) iff (c1, c2, c3) is along (1, 2, -4): the blind ratio (#8853 (b))")
    kap = sp.Symbol("kappa", positive=True)
    xs = sp.symbols("x1:7", real=True)
    Bt = sp.zeros(3, 3)
    Bt[0, 0], Bt[0, 1], Bt[0, 2], Bt[1, 0], Bt[1, 1], Bt[1, 2] = xs
    M6 = sp.hessian(fam(quadT(Bt, (0, 0, kap))), xs) / 2
    lam = sp.Symbol("lam")
    cp = sp.expand(M6.charpoly(lam).as_expr())
    target = (lam - kap ** 2 * (2 * c1 - c2)) * (lam - kap ** 2 * (2 * c1 + c2)) ** 2 * (lam - kap ** 2 * (2 * c1 + c2 + c3)) ** 2 * (lam - kap ** 2 * (2 * c1 + c2 + 2 * c3))
    checks.check("E2", sp.expand(cp - target) == 0, "at wave vector kappa e_3 (B_3^j a relabelling) the static form on the six transverse strains has eigenvalues kappa^2 x {2c1 - c2, 2c1 + c2 (twice), 2c1 + c2 + c3 (twice), 2c1 + c2 + 2c3}: every divergence-free source is balanced iff the four factors are non-zero")
    Mb = M6.subs({c1: -c3 / 4, c2: -c3 / 2})
    ker = Mb.subs(c3, 1).nullspace()
    # bond rotations transverse to e_3: omega_12 (B_1^2 = -B_2^1), B_1^3, B_2^3 (their partners B_3^j are relabellings here)
    rot = [sp.Matrix([0, 1, 0, -1, 0, 0]), sp.Matrix([0, 0, 1, 0, 0, 0]), sp.Matrix([0, 0, 0, 0, 0, 1])]
    same = sp.Matrix.hstack(*ker).rank() == 3 and sp.Matrix.hstack(*(ker + rot)).rank() == 3
    checks.check("E3", Mb.rank() == 3 and same, "at the blind ratio the form has rank three and its kernel is exactly the three bond rotations: a source with a bond torque (block 64 T5) has no static balance there")
    beta = c4 / (4 * c1 + 2 * c2 + 4 * c3)
    b1 = sp.simplify(beta.subs({c1: -c3 / 4, c2: -c3 / 2}).subs(c3, c4 / 2))
    checks.check("E4", sp.simplify(beta - c4 / (2 * (2 * c1 + c2 + 2 * c3))) == 0 and sp.solve(sp.Eq(beta, 1), c4) == [4 * c1 + 2 * c2 + 4 * c3] and b1 == 1, "block 64 T4's exponent beta = c4/(2(2c1 + c2 + 2c3)); on the blind ratio with block 64's c4 it is one; off it beta = 1 is the hyperplane c4 = 2(2c1 + c2 + 2c3)")


# ============================================================================================ family F
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the blind ratio."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Cartan", "Hayashi", "Shirafuji", "Newton", "Wilson", "Belinfante", "Rosenfeld", "Ivanenko", "Weitzenböck", "Kibble", "Sciama", "Hehl", "Laurent", "Newton")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Noether) —", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the pair symbol of the strain coupling and its divergence, symbolically in e^{ik}, e^{ik'} and the coins",
    "per_site: executed - the chain lemma by union-find on boxes at reaches one to three; the relabelling tie's symbol",
    "per_mode: executed - six exact pairs of energy one at q0 = (q1, 0, 0): rank six, divergence-free, implicit-function condition",
    "per_block: executed - the reach-one systems of the 4^3 and 6^3 tori mod p; block 64's family on a plane wave and on transverse strains",
    "lattice_wide: checked and not executed - every reach and every q near q0 (proof: implicit functions, continuity, trigonometric identities, factorisation, the chain lemma); ties that are not linear or not local; rates and varying frames",
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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    pts = family_c(checks)
    family_d(checks, certificate_pairs())
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: a local tie of the three site rotations to the nine bond strains whose response vanishes on every bounded stationary state of the infinite lattice is a relabelling, at every reach (own proof; the probes' tori at reaches one and two agree); block 64's family balances every divergence-free source iff (2c1 - c2)(2c1 + c2)(2c1 + c2 + c3)(2c1 + c2 + 2c3) != 0, the blind member cannot balance a bond torque, beta = c4/(2(2c1 + c2 + 2c3)); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line

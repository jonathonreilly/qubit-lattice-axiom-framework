#!/usr/bin/env python3
"""check.py for J:derive:the-two-step-content-and-the-members-identity:a1 (worker w-macbookpro9927a-jb994, claude-opus-5-5).

Setting (blocks 54, 55, 69/73 on main; blocks 120, 134 on their branches). Walk H = sum_a sigma_a S_a, (T_a f)(x) = f(x+e_a),
S_a = (T_a - T_a^-1)/(2i), C_a = (T_a + T_a^-1)/2; two-step momentum P_j = S_j C_j (symbol (1/2) sin 2k_j). Energy density
(block 55, wbar = 1): e(x) = Re psi(x)^dag (H psi)(x). Two-step bond current on x -> x+e_a (block 120):
K_a^j = (1/2) Re[psi(x+e_a)^dag sigma_a (P_j psi)(x) + (P_j psi)(x+e_a)^dag sigma_a psi(x)]. Block 120's realisation
B_i^j = -(1/2) phi_j h_ij, phi_j = (1/2)(1 + T_j^-1) prod_{l!=j} C_l; the content's Lagrangian coupling -<K, B> is written
(1/2) sum Theta2_ij h_ij with h in block 62's staggered placement (h_ij at x + (e_i+e_j)/2): this defines Theta2.
The member's demand at beta = -alpha, alpha = K/4 (block 134 T1): e'' = -p.Theta.p per wave vector, p_j = 2 sin(q_j/2).
A beat: psi = u e^{i(k.x - l t)} + u' e^{i(k'.x - l' t)}, (sigma.s)u = l u, (sigma.s')u' = l' u', q = k - k'.

Result: p.Theta2.p = prod_l cos q_l * (-e''_q) exactly, for every pair of eigen-waves (every species, either branch).

Families
  Q  pinned sources
  F  exact (sympy): the trig identities sin q_j (P_j(k)+P_j(k')) = cos q_j (s_j^2 - s'_j^2) and p_i cos(Kbar_i) = s_i - s'_i;
     the eigen-identity sum_i (s_i - s'_i) u'^dag sigma_i u = (l - l') u'^dag u; the assembly
     p.Theta2.p = (1/2)(l-l')^2 (l+l') u'^dag u prod cos q_l against -e''_q = (1/2)(l-l')^2 (l+l') u'^dag u; the defect's
     order (prod cos q_l = 1 - |q|^2/2 + O(q^4)); prod C_l - 1 as an explicit sum of forward differences (a total difference)
  T  [float] the L^3 torus (L = 12, 40 random beats of both branches): lattice fields give e_q and K_q as stated, the
     ratio p.Theta2.p/(-e''_q) = prod cos q_l, the same from a site-placed test field, and the corner average
     e' = (prod C_l) e restores the identity (ratio 1)
  X  exact certificates from lattice fields: an axis beat in Gaussian rationals (sin a = 5/13, sin a' = 3/5): ratio exactly
     cos(a - a') = 63/65, identity exact after the corner average; a three-dimensional beat in exact algebraic numbers
     (sympy): ratio exactly prod cos q_l
"""
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []
ONLY = set(sys.argv[1:])


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
MAIN = "60c5f194d940a7bbaf1cdd545296e31d74a02f1a"
N55 = ("docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS"
       "_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N69 = ("docs/ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE"
       "_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md")
N120 = ("docs/ADMISSIBILITY_RULE_ONLY_THE_TWO_STEP_CURRENT_CAN_SOURCE_BLOCK_62S_SYMMETRIC_MEMBER_NO_LOCAL_PLACEMENT_OF_THE"
        "_FRAME_RESPONSE_OR_OF_THE_ONE_STEP_CURRENT_KEEPS_ITS_DIVERGENCE_CONDITION_BOUNDED_THEOREM_NOTE_2026-09-24.md")
N134 = ("docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_FROM_THE_SOURCE_LINK_THE_WALKERS_SMOOTH_STATES_MEET_THE_MEMBERS_IDENTITY_AT"
        "_LEADING_ORDER_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md")
SRC = [("block55", MAIN, N55, "39d93ccb81349ae535401587958e86b3401fe8947830ebbd0ad07f955ee430da",
        ["Write E=chi^dagger H_w chi and e_x=Re[chi_x^dagger(H_w chi)_x]"], "main"),
       ("block69", MAIN, N69, "a0ab39ae2a58fcf92549bc122bb7c4791b57ad88c0dc4bb147cf49dec5a25163",
        ["*Statement.* `P_j = S_jC_j` has the symbol `½ sin 2k_j`, which vanishes at `k_j = 0, π` with slope `+1` at both; "
         "`[H, P_j] = 0`; `d⟨P_j⟩/dt = 0` for every state."], "main"),
       ("block120", "2c7d2337779890bd4e0175508a6c698bab6b89d6", N120,
        "2e5ca6b175b69008b3be216a14f8fb9c2a49b48c29e7776d958f2b46db696255",
        ["`J_a^j = ½Re[ψ†(x+e_a)σ_a(S_jψ)(x) + (S_jψ)†(x+e_a)σ_aψ(x)]` (block 63);",
         "`K_a^j` is the same with `P_j`.",
         "- (b) **A compatible realisation.** `B_i^j = −½ φ_j h_ij`, with `φ_j = ½(1 + T_j⁻¹)Π_{l≠j} C_l`."],
        "physics-loop/admissibility-induced-law-block120-only-the-two-step-current-can-source-the-symmetric-member-20260924"),
       ("block134", "52e320a4b6a6e1ea2bd763adf9a83a524e3838a8", N134,
        "a70c64b47045e4350657744ec29a73e34026640aaacd38c54d0a3630115816a9",
        ["- `e_q = ½w̄(l + l′)u′†u`, so `ë_q = −w̄²(l − l′)²e_q`;",
         "The walker's six partly reflected species cannot be such content at any `α`."],
        "physics-loop/admissibility-induced-law-block134-one-light-cone-from-the-source-link-alpha-equals-k-over-four-20260925")]
TASKQ = ("6ae1dbc2809efbe20dc08e9c74d9b80d798a4ef8", "J:derive:the-two-step-content-and-the-members-identity:a1",
         ["decide whether e'' = -wbar^2 p.Theta2.p holds exactly;",
          "whether adding a total difference to the energy density (a local redefinition) repairs it;",
          "whether it makes alpha = K/4 the exact lattice condition for every species.",
          "HIT: the exact identity, or the exact obstruction with a certificate (a rational beat where it fails)."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or "main"], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes, br in SRC:
        b = git_show(f"{c}:{p}", br)
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json", "ai/probes")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ F: exact symbolic chain
def fam_F():
    a, b = sp.symbols("a b", real=True)
    t1 = sp.simplify(sp.expand_trig(sp.sin(a - b) * (sp.sin(a) * sp.cos(a) + sp.sin(b) * sp.cos(b))
                                    - sp.cos(a - b) * (sp.sin(a) ** 2 - sp.sin(b) ** 2)))
    t2 = sp.simplify(sp.expand_trig(2 * sp.sin((a - b) / 2) * sp.cos((a + b) / 2) - (sp.sin(a) - sp.sin(b))))
    # eigen-identity with u = (l + s3, s1 + i s2), l^2 = |s|^2
    s1, s2, s3, t1_, t2_, t3_, l, lp = sp.symbols("s1 s2 s3 r1 r2 r3 l lp", real=True)
    I = sp.I
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    s = [s1, s2, s3]
    sq = [t1_, t2_, t3_]
    sdot = lambda v: sum((v[i] * sig[i] for i in range(3)), sp.zeros(2))
    u = sp.Matrix([l + s3, s1 + I * s2])
    up = sp.Matrix([lp + t3_, t1_ + I * t2_])
    red = lambda ex: sp.expand(sp.expand(ex).subs({l ** 2: s1 ** 2 + s2 ** 2 + s3 ** 2, lp ** 2: t1_ ** 2 + t2_ ** 2 + t3_ ** 2}))
    eig1 = [red(v) for v in (sdot(s) * u - l * u)]
    eig2 = [red(v) for v in (sdot(sq) * up - lp * up)]
    # u'^dag sigma_i u with u'^dag the conjugate transpose (real symbols)
    upd = up.H
    lhs = sum(((s[i] - sq[i]) * (upd * sig[i] * u)[0] for i in range(3)))
    rhs = (l - lp) * (upd * u)[0]
    ok_eig = all(v == 0 for v in eig1 + eig2) and red(lhs - rhs) == 0
    # assembly with generic M_i, bond current K_q = (1/2) e^{i q_i/2} cos(Kbar_i)(P_j(k)+P_j(k')) M_i,
    # staggered stress Theta_ij = K_i^j cos(q_j/2) prod_{l!=j} cos q_l e^{-i q_i/2}
    k = sp.symbols("k1:4", real=True)
    kp = sp.symbols("kp1:4", real=True)
    Msym = sp.symbols("M1:4")
    q = [k[i] - kp[i] for i in range(3)]
    Kb = [(k[i] + kp[i]) / 2 for i in range(3)]
    Pk = [sp.sin(k[j]) * sp.cos(k[j]) for j in range(3)]
    Pkp = [sp.sin(kp[j]) * sp.cos(kp[j]) for j in range(3)]
    p = [2 * sp.sin(qq / 2) for qq in q]
    Th = [[sp.Rational(1, 2) * sp.cos(Kb[i]) * (Pk[j] + Pkp[j]) * Msym[i] * sp.cos(q[j] / 2)
           * sp.Mul(*[sp.cos(q[m]) for m in range(3) if m != j]) for j in range(3)] for i in range(3)]
    pTp = sum(p[i] * p[j] * Th[i][j] for i in range(3) for j in range(3))
    fac1 = sum((sp.sin(k[i]) - sp.sin(kp[i])) * Msym[i] for i in range(3))                 # = (l - l') u'^dag u
    fac2 = sp.Mul(*[sp.cos(qq) for qq in q]) * sum(sp.sin(k[j]) ** 2 - sp.sin(kp[j]) ** 2 for j in range(3))
    # numeric-exact spot check of the factorisation at rational multiples of pi (sympy exact trig values)
    okas = True
    rnd = random.Random(2)
    for _ in range(6):
        vals = {v: sp.pi * sp.Rational(rnd.randint(-11, 11), 12) for v in k + kp}
        vals.update({Msym[0]: sp.Rational(rnd.randint(-5, 5), 3), Msym[1]: sp.Rational(rnd.randint(-5, 5), 7),
                     Msym[2]: sp.Rational(rnd.randint(-5, 5), 5)})
        okas &= sp.simplify((pTp - fac1 * fac2 / 2).subs(vals)) == 0
    qs = sp.symbols("q1:4", real=True)
    ser = sp.series(sp.cos(qs[0] * sp.Symbol("t")) * sp.cos(qs[1] * sp.Symbol("t")) * sp.cos(qs[2] * sp.Symbol("t")),
                    sp.Symbol("t"), 0, 4).removeO()
    ok_ser = sp.expand(ser - (1 - sp.Symbol("t") ** 2 * (qs[0] ** 2 + qs[1] ** 2 + qs[2] ** 2) / 2)) == 0
    # prod C_l - 1 = (C1-1) + C1(C2-1) + C1C2(C3-1), C_j - 1 = (1/2)(T_j - 1)(1 - T_j^-1): symbols with z_j = e^{i q_j}
    z = sp.symbols("z1:4")
    Cz = [(zz + 1 / zz) / 2 for zz in z]
    decomp = (Cz[0] - 1) + Cz[0] * (Cz[1] - 1) + Cz[0] * Cz[1] * (Cz[2] - 1)
    ok_dec = sp.simplify(decomp - (Cz[0] * Cz[1] * Cz[2] - 1)) == 0 and all(
        sp.simplify(Cz[j] - 1 - (z[j] - 1) * (1 - 1 / z[j]) / 2) == 0 for j in range(3))
    rep("F", t1 == 0 and t2 == 0 and ok_eig and okas and ok_ser and ok_dec,
        "exact: sin q_j (P_j(k)+P_j(k')) = cos q_j (s_j^2 - s'_j^2) and 2 sin(q_i/2) cos(Kbar_i) = s_i - s'_i (sympy); "
        "(sigma.s)u = l u for u = (l+s3, s1+i s2) and sum_i (s_i - s'_i) u'^dag sigma_i u = (l - l') u'^dag u; so "
        "p.Theta2.p = (1/2)(l-l')^2(l+l') u'^dag u prod cos q_l (factorisation checked exactly at 6 points), against "
        "-e''_q = (1/2)(l-l')^2(l+l') u'^dag u; prod cos q_l = 1 - |q|^2/2 + O(q^4); prod C_l - 1 = (C1-1) + C1(C2-1) + "
        "C1C2(C3-1) with C_j - 1 = (1/2)(T_j - 1)(1 - T_j^-1): a sum of forward differences of local fields")


# ------------------------------------------------------------------ T [float]
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def fam_T():
    t0 = time.time()
    L = 12
    Tm = lambda f, a, n=1: np.roll(f, -n, axis=a)
    Sf = lambda f, a: (Tm(f, a) - Tm(f, a, -1)) / 2j
    Cf = lambda f, a: (Tm(f, a) + Tm(f, a, -1)) / 2
    Hf = lambda f: sum(np.einsum("ij,xyzj->xyzi", SIG[a], Sf(f, a)) for a in range(3))
    X = np.stack(np.meshgrid(*[np.arange(L)] * 3, indexing="ij"), axis=-1)

    def wave(n, br):
        k = 2 * np.pi * np.array(n) / L
        s = np.sin(k)
        ev, U = np.linalg.eigh(sum(s[a] * SIG[a] for a in range(3)))
        i = 1 if br > 0 else 0
        return k, ev[i], U[:, i]

    def phi(f, j):
        g = 0.5 * (f + np.roll(f, 1, axis=j))
        for m in range(3):
            if m != j:
                g = 0.5 * (np.roll(g, -1, axis=m) + np.roll(g, 1, axis=m))
        return g

    rng = np.random.default_rng(5)
    rows, oks, used = [], True, 0
    maxdev = 0.0
    while used < 40:
        n1, n2 = rng.integers(0, L, 3), rng.integers(0, L, 3)
        b1, b2 = rng.choice([-1, 1]), rng.choice([-1, 1])
        k1, l1, u1 = wave(n1, b1)
        k2, l2, u2 = wave(n2, b2)
        pref = (l1 - l2) ** 2 * (l1 + l2) * (np.conj(u2) @ u1) / 2
        if np.all(n1 == n2) or abs(pref) < 1e-6 or np.all((2 * (n1 - n2)) % L == 0):
            continue                                                         # q = -q (mod 2 pi) aliases the two cross terms
        used += 1
        psi = np.exp(1j * (X @ k1))[..., None] * u1 + np.exp(1j * (X @ k2))[..., None] * u2
        q = k1 - k2
        Fq = lambda fld: (fld * np.exp(-1j * (X @ q))).sum() / L ** 3
        e = np.real(np.einsum("xyzi,xyzi->xyz", psi.conj(), Hf(psi)))
        edd = -(l1 - l2) ** 2 * Fq(e)
        eq_ok = abs(Fq(e) - (l1 + l2) * (np.conj(u2) @ u1) / 2) < 1e-10
        M = np.array([np.conj(u2) @ SIG[a] @ u1 for a in range(3)])
        Kb = (k1 + k2) / 2
        Pv = lambda k: np.sin(k) * np.cos(k)
        ThS = np.zeros((3, 3), complex)
        ThA = np.zeros((3, 3), complex)
        Kok = True
        for i in range(3):
            for j in range(3):
                Pp = Sf(Cf(psi, j), j)
                Kij = 0.5 * np.real(np.einsum("xyzi,ij,xyzj->xyz", Tm(psi, i).conj(), SIG[i], Pp)
                                    + np.einsum("xyzi,ij,xyzj->xyz", Tm(Pp, i).conj(), SIG[i], psi))
                Kq = Fq(Kij)
                Kok &= abs(Kq - 0.5 * np.exp(1j * q[i] / 2) * np.cos(Kb[i]) * (Pv(k1[j]) + Pv(k2[j])) * M[i]) < 1e-10
                off = (np.eye(3)[i] + np.eye(3)[j]) / 2
                hst = np.exp(-1j * ((X + off) @ q))                          # staggered test mode
                ThS[i, j] = (Kij * phi(hst, j)).sum() / L ** 3              # 2 * (1/2) sum K phi h / N
                hsi = np.exp(-1j * (X @ q))                                  # site test mode
                ThA[i, j] = (Kij * phi(hsi, j)).sum() / L ** 3
        p = 2 * np.sin(q / 2)
        pTp = p @ ThS @ p
        pTp_site = -sum((np.exp(-1j * q[i]) - 1) * (np.exp(-1j * q[j]) - 1) * ThA[i, j] for i in range(3) for j in range(3))
        fac = np.prod(np.cos(q))
        ratio = pTp / (-edd)
        rep_ratio = pTp / ((l1 - l2) ** 2 * fac * Fq(e))                   # -e''_q' = (l-l')^2 e'_q, e'_q = fac e_q
        dev = max(abs(ratio - fac), abs(pTp_site - pTp), abs(rep_ratio - 1) if abs(fac) > 1e-6 else 0.0)
        maxdev = max(maxdev, dev)
        oks &= eq_ok and Kok and dev < 1e-9
    rep("T", oks, f"[float] L = 12 torus, 40 random beats (both branches, all corners): lattice fields give e_q = "
        f"(l+l')u'^dag u/2 and K_q = (1/2)e^(iq_i/2) cos(Kbar_i)(P_j+P'_j)M_i; p.Theta2.p/(-e''_q) = prod cos q_l, the "
        f"staggered and site test fields agree, and e' = (prod C_l) e gives ratio 1; max deviation {maxdev:.1e}  "
        f"({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ X: exact certificates from lattice fields
class G:
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a - o.a, s.b - o.b)

    def __rsub__(s, o):
        return G(o) - s

    def __neg__(s):
        return G(-s.a, -s.b)

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def conj(s):
        return G(s.a, -s.b)

    def inv(s):
        d = s.a * s.a + s.b * s.b
        return G(s.a / d, -s.b / d)

    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s * o.inv()

    def __pow__(s, n):
        r = G(1)
        base = s if n >= 0 else s.inv()
        for _ in range(abs(n)):
            r = r * base
        return r

    def __eq__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s.a == o.a and s.b == o.b

    def __repr__(s):
        return f"{s.a}+{s.b}i"


SIGG = [[[G(0), G(1)], [G(1), G(0)]], [[G(0), G(0, -1)], [G(0, 1), G(0)]], [[G(1), G(0)], [G(0), G(-1)]]]


def lattice_certificate_rational():
    # k = (a, 0, 0), k' = (a', 0, 0); sin a = 5/13, cos a = 12/13; sin a' = 3/5, cos a' = 4/5
    z = [G(Fr(12, 13), Fr(5, 13)), G(1), G(1)]
    zp = [G(Fr(4, 5), Fr(3, 5)), G(1), G(1)]
    s = [Fr(5, 13), Fr(0), Fr(0)]
    sp_ = [Fr(3, 5), Fr(0), Fr(0)]
    l, lp = Fr(5, 13), Fr(3, 5)                       # positive branches of sigma_x s_1
    u = [G(l + s[2]), G(s[0], s[1])]
    up = [G(lp + sp_[2]), G(sp_[0], sp_[1])]

    def psi(x):
        f = G(1)
        fp = G(1)
        for j in range(3):
            f = f * z[j] ** x[j]
            fp = fp * zp[j] ** x[j]
        return [u[c] * f + up[c] * fp for c in range(2)]

    add = lambda x, d: tuple(x[i] + d[i] for i in range(3))
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    neg = lambda d: tuple(-v for v in d)
    S = lambda fn, a: (lambda x: [(fn(add(x, E[a]))[c] - fn(add(x, neg(E[a])))[c]) / G(0, 2) for c in range(2)])
    Cc = lambda fn, a: (lambda x: [(fn(add(x, E[a]))[c] + fn(add(x, neg(E[a])))[c]) * Fr(1, 2) for c in range(2)])
    mv = lambda M, v: [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]
    dot = lambda a_, b_: a_[0].conj() * b_[0] + a_[1].conj() * b_[1]

    def H(x):
        out = [G(0), G(0)]
        for a_ in range(3):
            v = mv(SIGG[a_], S(psi, a_)(x))
            out = [out[0] + v[0], out[1] + v[1]]
        return out

    def e(x):
        return dot(psi(x), H(x)).a                    # real part

    def K(x, i, j):
        P = S(Cc(psi, j), j)
        t1 = dot(psi(add(x, E[i])), mv(SIGG[i], P(x)))
        t2 = dot(P(add(x, E[i])), mv(SIGG[i], psi(x)))
        return (t1 + t2).a / 2

    # Vandermonde along e1: f(x) = f0 + f_q w^x + f_-q w^-x, w = e^{i q_1} = z_1/z'_1
    w = z[0] / zp[0]

    def coeff_q(f):
        v = [G(f((m, 0, 0))) for m in (0, 1, 2)]
        # rows [1, w^m, w^-m]; solve by elimination
        A = [[G(1), w ** m, w ** (-m)] + [v[m]] for m in range(3)]
        for c in range(3):
            pv = A[c][c]
            A[c] = [x / pv for x in A[c]]
            for r in range(3):
                if r != c:
                    fct = A[r][c]
                    A[r] = [xr - fct * xc for xr, xc in zip(A[r], A[c])]
        return A[1][3]

    eq = coeff_q(e)
    Kq11 = coeff_q(lambda x: K(x, 0, 0))
    cq1 = Fr(12, 13) * Fr(4, 5) + Fr(5, 13) * Fr(3, 5)             # cos(a - a')
    theta_site = (G(1) + w) * Fr(1, 2) * Kq11                    # (1/2)(1 + e^{iq_1}) prod_{l != 1} cos q_l * K_q
    pTp = -((w.inv() - 1) * (w.inv() - 1)) * theta_site          # p.Theta^st.p = -sum (e^{-iq_i}-1)(e^{-iq_j}-1) Theta^site
    edd = -(l - lp) ** 2 * eq
    ratio = pTp / (-edd)
    ok = ratio == G(cq1) and cq1 == Fr(63, 65)
    # repaired: e' = prod C_l e has e'_q = cos q1 e_q (q2 = q3 = 0): identity exact
    ok &= pTp == -(-(l - lp) ** 2 * (eq * cq1))
    # e_q against the stated formula
    ok &= eq == ((l + lp) * dot(up, u)) * Fr(1, 2)
    return ok, ratio, eq, pTp


def lattice_certificate_3d():
    # k with rational trig values in all three components; algebraic eigenvalues (exact sympy)
    I = sp.I
    sc = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(8, 17), sp.Rational(15, 17))]
    scp = [(sp.Rational(-3, 5), sp.Rational(4, 5)), (sp.Rational(7, 25), sp.Rational(24, 25)), (sp.Rational(12, 13), sp.Rational(-5, 13))]
    z = [c + I * s for s, c in sc]
    zp = [c + I * s for s, c in scp]
    s = sp.Matrix([t[0] for t in sc])
    sp_ = sp.Matrix([t[0] for t in scp])
    l = sp.sqrt(s.dot(s))
    lp = -sp.sqrt(sp_.dot(sp_))
    u = sp.Matrix([l + s[2], s[0] + I * s[1]])
    up = sp.Matrix([lp + sp_[2], sp_[0] + I * sp_[1]])
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I], [I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    add = lambda x, d: tuple(x[i] + d[i] for i in range(3))
    neg = lambda d: tuple(-v for v in d)
    cache = {}

    def psi(x):
        if x not in cache:
            f = sp.Mul(*[z[j] ** x[j] for j in range(3)])
            fp = sp.Mul(*[zp[j] ** x[j] for j in range(3)])
            cache[x] = u * f + up * fp
        return cache[x]

    S = lambda fn, a: (lambda x: (fn(add(x, E[a])) - fn(add(x, neg(E[a])))) / (2 * I))
    Cc = lambda fn, a: (lambda x: (fn(add(x, E[a])) + fn(add(x, neg(E[a])))) / 2)
    dot = lambda a_, b_: (a_.H * b_)[0]

    def e(x):
        Hx = sum((sig[a_] * S(psi, a_)(x) for a_ in range(3)), sp.zeros(2, 1))
        return sp.re(sp.expand(dot(psi(x), Hx)))

    def K(x, i, j):
        P = S(Cc(psi, j), j)
        return sp.re(sp.expand(dot(psi(add(x, E[i])), sig[i] * P(x)) + dot(P(add(x, E[i])), sig[i] * psi(x)))) / 2

    v = (1, 1, 1)
    w = sp.simplify(sp.Mul(*[z[j] / zp[j] for j in range(3)]))

    def coeff_q(f):
        vals = [f(tuple(m * vv for vv in v)) for m in (0, 1, 2)]
        c0, cq, cm = sp.symbols("c0 cq cm")
        sol = sp.solve([c0 + cq * w ** m + cm * w ** (-m) - vals[m] for m in range(3)], [c0, cq, cm], dict=True)[0]
        return sp.simplify(sol[cq])

    eq = coeff_q(e)
    cosq = [sp.re(sp.expand(z[j] * sp.conjugate(zp[j]))) for j in range(3)]
    eiq = [sp.expand(z[j] * sp.conjugate(zp[j])) for j in range(3)]
    ths = {}
    for i in range(3):
        for j in range(3):
            Kq = coeff_q(lambda x, i=i, j=j: K(x, i, j))
            ths[(i, j)] = (1 + eiq[j]) / 2 * sp.Mul(*[cosq[m] for m in range(3) if m != j]) * Kq
    pTp = -sum((sp.conjugate(eiq[i]) - 1) * (sp.conjugate(eiq[j]) - 1) * ths[(i, j)] for i in range(3) for j in range(3))
    edd = -(l - lp) ** 2 * eq
    fac = sp.Mul(*cosq)
    ok = sp.simplify(pTp - fac * (-edd)) == 0 and sp.simplify(fac - 1) != 0 and fac != 0 and sp.simplify(edd) != 0
    return ok, fac, sp.N(pTp / (-edd), 12)


def fam_X():
    t0 = time.time()
    ok1, ratio, eq, pTp = lattice_certificate_rational()
    ok2, fac, num = lattice_certificate_3d()
    rep("X", ok1 and ok2, f"exact from lattice fields (Vandermonde extraction of the e^(iq.x) parts at three sites): axis "
        f"beat k = (a,0,0), k' = (a',0,0), sin a = 5/13, sin a' = 3/5, both positive branches: e_q = {eq}, p.Theta2.p = "
        f"{pTp}, ratio to -e''_q exactly 63/65 = cos(a - a'), and exact after the corner average; three-dimensional beat "
        f"(sines 3/5, 5/13, 8/17 and -3/5, 7/25, 12/13, branches +,-; algebraic eigenvalues): ratio exactly prod cos q_l = "
        f"{fac} = {float(fac):.6f}  ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    for tag, fn in (("Q", fam_Q), ("F", fam_F), ("T", fam_T), ("X", fam_X)):
        if not ONLY or tag in ONLY:
            fn()
    print(f"total {time.time() - T0:.0f}s; failing families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + ",".join(sorted(set(FAILS))))
    else:
        print("SUMMARY: PROVED for every beat of two eigen-waves of the walk (every species, either branch): with block "
              "120's two-step stress and block 55's energy density, p.Theta2.p = prod_l cos q_l * (-e''_q) exactly; the "
              "identity fails at relative order |q|^2/2, isotropically; the corner average e' = (prod C_l) e, a total "
              "difference away from e, satisfies it exactly, so alpha = K/4 is then the exact condition for all eight species")
        print("HIT: the two-step content meets the member's identity up to one exact factor: for every beat of two "
              "eigen-waves of the walk, of any species and either branch, block 120's two-step stress gives p.Theta2.p = "
              "prod_l cos q_l * (-e''_q) with block 55's energy density (exact; certificate: sin a = 5/13, sin a' = 3/5 "
              "gives 63/65); the corner average e' = (prod_l C_l) e, block 55's density plus a total difference, meets "
              "e'' = -p.Theta2.p exactly on every state, so alpha = K/4 becomes the exact lattice condition for all eight "
              "species")

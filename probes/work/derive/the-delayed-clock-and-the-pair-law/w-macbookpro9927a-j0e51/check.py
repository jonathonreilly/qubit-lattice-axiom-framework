#!/usr/bin/env python3
"""check.py for J:derive:the-delayed-clock-and-the-pair-law:a1 (worker w-macbookpro9927a-j0e51, claude-opus-5-5).

Every finite claim of ATTEMPT.md is checked with exact arithmetic (fractions.Fraction, sympy).
Family S is a direct floating-point simulation of the joint process and is labelled [float]; it is
evidence for the assumptions A0/A1 and for the float observations, never a proof step.

Families
  Q  quoted definitions pinned by commit and SHA-256 (landed block 95 and block 53 notes, the task text)
  A  torus Green functions: Delta G = delta0 - 1/V, sum G = 0, G even, strict maximum at 0;
     G2 = G*G: Delta G2 = G and G2(0) - G2(e) = G(0)/q
  B  step S1: sum_z exp(-u_z) is conserved by every fixed-configuration flow; Lyapunov derivative (S2)
  C  step S2: equilibria u*(C); the slaved chain is reversible for pi95/Z; Z(C) varies with C at order lambda^2
  D  step S3: next-separation law of two records is uniform on N(D)\\{0} for any two clocks; martingale step
  E  step S4: first order in lambda, every Gamma, N and a: m(C) = pi0 gamma phi*(C) solves the moment equations,
     block 95 at gamma*lambda solves the O(lambda) master equation; wrong-gamma controls fail; uniqueness rank
  F  steps S6-S7: drift on the equilibrium line; averaged-flow Lyapunov derivative; the weighted-constant step
  H  step S8: sojourn route at first order in 1/Gamma (exact identities) and its agreement with S4
  K  step S9: quasi-static limit: harmonic-mean identity, R0 versus Rinf, instability threshold
  S  [float] direct simulation of the joint process (numba)
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as F
from itertools import combinations, product

import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q: pinned sources
NOTE95 = ("8cc5f114f0d703100d6a7a764a1c689c7a56d65f",
          "docs/ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH"
          "_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md",
          "285dcf4bca2cc72027dff3599b9734e7ddf3c6c90a628cf5175c64e0add8cf9a")
NOTE53 = ("c3f8c47a58bfba48c1d9e030d6d79ecda00a294e",
          "docs/ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE"
          "_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md",
          "fe403d12e816037d29b567f06d7a39cc8533372b15b339d360612315be24bf5d")
TASKS = ("63ad2529d6d5583b536eec059599fd1141e226bf", "probes/TASKS.json")
Q95 = ["Let lambda=log kappa be real. The supplied configuration-following field is u_z(C)=6lambda sum_{r in C}G(z-r), with mean u=0.",
       "set h=W(C')/[W(C)+W(C')] and rate=exp[a u_x(C)+(1-a)u_y(C)] h/6, a real.",
       "pi(C) is proportional to W(C) exp[6lambda(1-2a) sum_{unordered pairs}G(r-s)].",
       "Restrict now to W=1, so h=1/2. At a=1 every allowed hop of a record at x has rate w_x/12.",
       "Their relative-position stationary weight per offset is exp[-6lambda G(d)], up to normalization."]
Q53 = ["The optional record law uses fixed strengths s_x=(log kappa)n_x in the selected equation L u=s, L=I-A with A the six-neighbour average.",
       "A single test walker jumps along each incident cubic bond at w_x/6",
       "pi_x=(1/w_x)/sum_y(1/w_y) satisfies pi_x w_x/6=pi_y w_y/6 across every bond"]
QT = ["du_z/dt = Gamma w_z ((1/6) sum_e u_(z+e) - u_z + log(kappa)(n_z - nbar))",
      "then departure-timed hopping is in detailed balance with W(C) exp(6 log(kappa) sum_pairs G)",
      "block 95's pair law is a neutralized torus law",
      "HIT: (a) or (b) exact, or an exact proof that no joint law of product form is stationary."]


def git_show(spec):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for (c, p, h), quotes, tag in ((NOTE95, Q95, "block95"), (NOTE53, Q53, "block53")):
        b = git_show(f"{c}:{p}")
        if b is None:
            rep("Q", False, f"{tag} note not readable at {c[:10]}")
            return
        good = hashlib.sha256(b).hexdigest() == h
        txt = b.decode()
        hits = sum(q in txt for q in quotes)
        ok &= good and hits == len(quotes)
        msg.append(f"{tag}@{c[:8]} sha256 {'ok' if good else 'MISMATCH'} {hits}/{len(quotes)} quotes")
    b = git_show(f"{TASKS[0]}:{TASKS[1]}")
    tasks = json.loads(b.decode()) if b else []
    tasks = tasks if isinstance(tasks, list) else tasks.get("tasks", [])
    what = next((t.get("what", "") for t in tasks if t.get("id") == "J:derive:the-delayed-clock-and-the-pair-law:a1"), "")
    hits = sum(q in what for q in QT)
    ok &= hits == len(QT)
    msg.append(f"task@{TASKS[0][:8]} {hits}/{len(QT)} quotes")
    rep("Q", ok, "; ".join(msg) + ". Note: at a=1 the landed T2 exponent is 6lambda(1-2a) = -6lambda; the task's "
        "'exp(6 log(kappa) sum_pairs G)' has the opposite sign; the landed sign is used throughout")


# ------------------------------------------------------------------ exact torus machinery
def solve_exact(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        if p != c:
            M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        if pv != 1:
            M[c] = [x / pv for x in M[c]]
        Mc = M[c]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], Mc)]
    return [M[i][n] for i in range(n)]


def rank_exact(A):
    M = [row[:] for row in A]
    rows, cols, r = len(M), len(M[0]), 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


class Torus:
    def __init__(self, dims):
        self.dims = dims
        self.sites = list(product(*[range(L) for L in dims]))
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.V, self.q = len(self.sites), 2 * len(dims)
        self.E = []
        for j in range(len(dims)):
            for sg in (1, -1):
                e = [0] * len(dims)
                e[j] = sg
                self.E.append(tuple(e))
        self.Ei = [self.idx[tuple(x % L for x, L in zip(e, dims))] for e in self.E]
        self.nbrs = [[self.idx[tuple((x + y) % L for x, y, L in zip(s, e, dims))] for e in self.E] for s in self.sites]
        self.dif = [[self.idx[tuple((x - y) % L for x, y, L in zip(self.sites[a], self.sites[c], dims))]
                     for c in range(self.V)] for a in range(self.V)]
        self.neg = [self.dif[0][i] for i in range(self.V)]
        V, q = self.V, self.q
        A = [[F(1, V)] * V for _ in range(V)]
        for i in range(V):
            A[i][i] += q
            for j in self.nbrs[i]:
                A[i][j] -= 1
        self.g = solve_exact(A, [(F(1) if i == 0 else F(0)) - F(1, V) for i in range(V)])
        self.g2 = [sum(self.g[j] * self.g[self.dif[i][j]] for j in range(V)) for i in range(V)]

    def lap(self, f):
        return [self.q * f[i] - sum(f[j] for j in self.nbrs[i]) for i in range(self.V)]

    def Mop(self, f):
        return [sum(f[j] for j in self.nbrs[i]) / self.q - f[i] for i in range(self.V)]

    def phi(self, C):  # phi*(C)_z = q sum_{r in C} G(z - r)
        return [self.q * sum(self.g[self.dif[z][r]] for r in C) for z in range(self.V)]

    def moves(self, C):  # (C', x, y): record at x moves to empty neighbour y
        return [(C - {x} | {y}, x, y) for x in C for y in self.nbrs[x] if y not in C]

    def name(self):
        return "x".join(map(str, self.dims))


TORI = {}


def torus(dims):
    if dims not in TORI:
        TORI[dims] = Torus(dims)
    return TORI[dims]


# ------------------------------------------------------------------ A: Green functions
def fam_A():
    ok, info = True, []
    dl = [(L,) for L in range(3, 11)] + [(3, 3), (4, 4), (3, 3, 3), (4, 4, 4)]
    for d in dl:
        T = torus(d)
        V, q, g, g2 = T.V, T.q, T.g, T.g2
        lg = T.lap(g)
        ok &= all(lg[i] == (F(1) if i == 0 else 0) - F(1, V) for i in range(V))
        ok &= sum(g) == 0 and all(g[T.neg[i]] == g[i] for i in range(V))
        ok &= all(g[0] > g[i] for i in range(1, V))
        ok &= T.lap(g2) == g and all(g2[0] - g2[e] == g[0] / q for e in T.Ei)
        if len(d) == 1:
            L = d[0]
            ok &= all(g[z] == F(L * L - 1, 12 * L) - F(z * (L - z), 2 * L) for z in range(L))
        if d in [(6,), (3, 3, 3), (4, 4, 4)]:
            info.append(f"G(0)[{T.name()}]={g[0]}")
    rep("A", ok, f"rings 3..10, 3x3, 4x4, 3^3, 4^3: Delta G = delta0 - 1/V, sum 0, even, strict max at 0, ring closed form; "
                 f"Delta G2 = G and G2(0)-G2(e) = G(0)/q; " + ", ".join(info))


# ------------------------------------------------------------------ B: invariant and Lyapunov derivative
def fam_B():
    ok = True
    lam, Gam = sp.symbols("lambda Gamma", real=True)
    for d, occ in [((5,), (0, 2)), ((3, 3), (0, 4, 5)), ((3, 3, 3), (0, 13))]:
        T = torus(d)
        V = T.V
        u = sp.symbols(f"u0:{V}", real=True)
        n = [1 if z in occ else 0 for z in range(V)]
        nbar = sp.Rational(len(occ), V)
        Mu = [sum(u[j] for j in T.nbrs[z]) / T.q - u[z] for z in range(V)]
        udot = [Gam * sp.exp(u[z]) * (Mu[z] + lam * (n[z] - nbar)) for z in range(V)]
        dS = sp.expand(sum(-sp.exp(-u[z]) * udot[z] for z in range(V)))
        ok &= sp.simplify(dS) == 0
    # Lyapunov: with v = u - u*, udot = Gamma w (M v); dE/dt for E = <v,-Mv>/2 equals -Gamma sum w (Mv)^2
    T = torus((5,))
    v = sp.symbols("v0:5", real=True)
    w = sp.symbols("w0:5", positive=True)
    Mv = [sum(v[j] for j in T.nbrs[z]) / T.q - v[z] for z in range(5)]
    Evd = sum(-Mv[z] * Gam * w[z] * Mv[z] for z in range(5))  # <grad E, vdot>, grad E = -M v
    ok &= sp.simplify(Evd + Gam * sum(w[z] * Mv[z] ** 2 for z in range(5))) == 0
    rep("B", ok, "S1: d/dt sum_z exp(-u_z) = -Gamma sum_z (Mu + lambda(n - nbar))_z = 0 symbolically (ring 5 N=2, 3x3 N=3, "
                 "3^3 N=2); jumps leave u unchanged; S2: dE_C/dt = -Gamma sum_z w_z ((M(u-u*))_z)^2")


# ------------------------------------------------------------------ C: slaved limit
def fam_C():
    ok, zinfo = True, []
    for d, Ns in [((5,), (1, 2)), ((6,), (2, 3)), ((3, 3), (2,)), ((3, 3, 3), (2,))]:
        T = torus(d)
        for N in Ns:
            cfgs = [frozenset(c) for c in combinations(range(T.V), N)]
            nbar = F(N, T.V)
            for C in cfgs:
                ph = T.phi(C)
                ok &= T.Mop(ph) == [-((1 if z in C else 0) - nbar) for z in range(T.V)]
            P = {C: sum(T.g[T.dif[r][s]] for r, s in combinations(sorted(C), 2)) for C in cfgs}
            for a in (F(1), F(1, 2), F(0), F(3, 7)):
                for C in cfgs:
                    ph = T.phi(C)
                    for C2, x, y in T.moves(C):
                        ph2 = T.phi(C2)
                        lhs = T.q * (1 - 2 * a) * P[C] + a * ph[x] + (1 - a) * ph[y]
                        rhs = T.q * (1 - 2 * a) * P[C2] + a * ph2[y] + (1 - a) * ph2[x]
                        ok &= lhs == rhs
    T = torus((6,))
    zc = {}
    for D in (1, 2, 3):
        ph = T.phi({0, D})
        zc[D] = sum(p * p for p in ph) / 2
        ok &= sum(ph) == 0
    ok &= len(set(zc.values())) == 3
    zinfo = ", ".join(f"D={D}: {zc[D]}" for D in zc)
    rep("C", ok, "S2: M u*(C) = -lambda(n_C - nbar) for u* = q lambda sum G (all configurations checked); slaved chain log-balance "
                 "for pi95 at a in {1,1/2,0,3/7}, every move, so pi_inf = pi95/Z(C) (rates carry Z(C)/S); Z(C) = V + "
                 f"lambda^2 c2(C) + O(lambda^3), ring 6 two records c2 = {zinfo} (varies with D)")


# ------------------------------------------------------------------ D: jump chains
def fam_D():
    ok = True
    for d in [(3,), (4,), (5,), (6,), (3, 3), (4, 4), (3, 3, 3), (4, 4, 4)]:
        T = torus(d)
        for D in range(1, T.V):
            m1 = sorted(T.dif[D][e] for k, e in enumerate(T.Ei) if T.Ei[k] != D)   # record 1 moves by e: D -> D - e
            m2 = sorted(T.nbrs[D][k] for k, e in enumerate(T.Ei) if T.neg[e] != D)  # record 2 moves by e: D -> D + e
            nd = sorted(j for j in T.nbrs[D] if j != 0)
            ok &= m1 == m2 == nd and len(nd) == T.q - (1 if D in T.Ei else 0)
    S = sp.symbols("s0:3", real=True)
    for dd in (1, 2, 3):
        Es = []
        for j in range(dd):
            for sg in (1, -1):
                e = [0] * dd
                e[j] = sg
                Es.append(e)
        inc = sum(sum((S[i] + e[i]) ** 2 for i in range(dd)) - sum(S[i] ** 2 for i in range(dd)) for e in Es) / (2 * dd)
        ok &= sp.expand(inc) == 1
    rep("D", ok, "S3: for every D != 0 on rings 3-6, 3x3, 4x4, 3^3, 4^3 the moves of record 1 and of record 2 each reach every "
                 "D' in N(D)\\{0} exactly once, so the next separation is uniform for any clocks (w1,w2); deg(D) = q - [D in E]; "
                 "mean one-step increment of |X|^2 is exactly 1 (d=1,2,3)")


# ------------------------------------------------------------------ E: first order in lambda, every Gamma
def first_order(T, N, Gam, a, gamma_override=None):
    V, q = T.V, T.q
    r0 = F(1, 2 * q)
    gamma = Gam / (Gam + r0 * q) if gamma_override is None else gamma_override
    cfgs = [frozenset(c) for c in combinations(range(V), N)]
    pi0 = F(1, len(cfgs))
    nbar = F(N, V)
    m = {C: [pi0 * gamma * x for x in T.phi(C)] for C in cfgs}
    mv = {C: T.moves(C) for C in cfgs}
    res1 = 0
    for C in cfgs:
        Mm = T.Mop(m[C])
        for z in range(V):
            r = Gam * (Mm[z] + pi0 * ((1 if z in C else 0) - nbar)) + r0 * sum((m[C2][z] - m[C][z] for C2, _, _ in mv[C]), F(0))
            assert isinstance(r, F)
            res1 += r != 0
    P = {C: sum((T.g[T.dif[r][s]] for r, s in combinations(sorted(C), 2)), F(0)) for C in cfgs}
    Pbar = sum(P.values(), F(0)) / len(cfgs)
    pi1 = {C: pi0 * gamma * q * (1 - 2 * a) * (P[C] - Pbar) for C in cfgs}
    assert all(isinstance(x, F) for x in pi1.values())
    res2 = 0
    for C0 in cfgs:
        tot = F(0)
        for C, x, y in mv[C0]:      # C0 -> C moves x -> y; C -> C0 moves y -> x
            tot += pi1[C] - pi1[C0] + a * m[C][y] + (1 - a) * m[C][x] - a * m[C0][x] - (1 - a) * m[C0][y]
        assert isinstance(tot, F)
        res2 += tot != 0
    return gamma, res1, res2, len(cfgs), m, pi1


def moment_operator(T, N, Gam):
    V, q = T.V, T.q
    r0 = F(1, 2 * q)
    cfgs = [frozenset(c) for c in combinations(range(V), N)]
    ci = {C: i for i, C in enumerate(cfgs)}
    n = len(cfgs) * V
    A = [[F(0)] * n for _ in range(n)]
    for C in cfgs:
        for z in range(V):
            row = ci[C] * V + z
            A[row][row] += -Gam
            for j in T.nbrs[z]:
                A[row][ci[C] * V + j] += Gam / q
            for C2, _, _ in T.moves(C):
                A[row][ci[C2] * V + z] += r0
                A[row][row] -= r0
    return A, n


def fam_E():
    ok, cnt, ctrl = True, 0, 0
    cases = [((5,), 1), ((6,), 2), ((7,), 3), ((3, 3), 2), ((4, 4), 2), ((3, 3, 3), 1), ((3, 3, 3), 2)]
    for d, N in cases:
        T = torus(d)
        for Gam in (F(1, 3), F(1), F(5, 2)):
            for a in (F(1), F(1, 2), F(0)):
                g, r1, r2, nc, m, pi1 = first_order(T, N, Gam, a)
                ok &= r1 == 0 and r2 == 0
                cnt += 1
            for bad in (F(1), Gam / (Gam + 2 * F(1, 2))):   # slaved gamma = 1, and a doubled-rate gamma
                _, r1b, _, _, _, _ = first_order(T, N, Gam, F(1), gamma_override=bad)
                ctrl += r1b > 0
    g, r1, r2, nc, m, pi1 = first_order(torus((4, 4, 4)), 2, F(1), F(1))
    ok &= r1 == 0 and r2 == 0
    cnt += 1
    ranks = []
    for d, N in [((5,), 2), ((6,), 2)]:
        T = torus(d)
        A, n = moment_operator(T, N, F(1))
        rk = rank_exact(A)
        ones = [F(1)] * n
        ok &= rk == n - 1 and all(sum(A[i][j] * ones[j] for j in range(n)) == 0 for i in range(n))
        ranks.append(f"{T.name()} N={N}: rank {rk}/{n}")
    ok &= ctrl == 6 * len(cases)
    Gs, lam = sp.symbols("Gamma lambda", positive=True)
    gam = Gs / (Gs + sp.Rational(1, 2))
    ok &= sp.simplify(1 - gam - 1 / (2 * Gs + 1)) == 0
    ser = sp.series(gam, Gs, sp.oo, 3).removeO()
    ok &= sp.simplify(ser - (1 - 1 / (2 * Gs) + 1 / (4 * Gs ** 2))) == 0
    T6, T3 = torus((6,)), torus((3, 3, 3))
    rng = f"ring 6: E[u_X]/lambda = gamma*{T6.q * T6.g[0]}; 3^3: gamma*{T3.q * T3.g[0]}"
    Pd = {D: T6.g[D] for D in (1, 2, 3)}
    Pbar = (6 * Pd[1] + 6 * Pd[2] + 3 * Pd[3]) / 15
    pl = ", ".join(f"D={D}: {-T6.q * (Pd[D] - Pbar)}*gamma*lambda" for D in (1, 2, 3))
    rep("E", ok, f"S4: {cnt} (torus,N,Gamma,a) cases incl. 4^3 N=2: moment equations solved exactly by m(C) = pi0 gamma phi*(C), "
                 f"gamma = Gamma/(Gamma + r0 q); O(lambda) master equation solved by block 95 at gamma*lambda; controls gamma=1 and "
                 f"Gamma/(Gamma+1) fail in all {ctrl} cases; operator kernel = constants ({'; '.join(ranks)}); 1-gamma = 1/(2Gamma+1), "
                 f"gamma = 1 - 1/(2Gamma) + 1/(4Gamma^2) + ...; one record a=1: {rng}; ring-6 pair law pi1/pi0: {pl}")


# ------------------------------------------------------------------ F: product-law and reversibility ingredients
def fam_F():
    ok = True
    V = 4
    T = torus((4,))
    lam, Gam, c, beta = sp.symbols("lambda Gamma c beta", real=True)
    rho = list(sp.symbols("rho0:3", real=True))
    N = 2
    rho.append(N - sum(rho))
    nbar = sp.Rational(N, V)
    urho = sp.symbols("U0:4", real=True)
    Mur = [-lam * (rho[z] - nbar) for z in range(V)]   # M u_rho = -lambda(rho - nbar) (definition of u_rho)
    for occ in [(0, 1), (0, 2), (1, 3)]:
        n = [1 if z in occ else 0 for z in range(V)]
        drift = [Gam * sp.exp(urho[z] + c) * (Mur[z] + lam * (n[z] - nbar)) for z in range(V)]
        target = [Gam * lam * sp.exp(c) * sp.exp(urho[z]) * (n[z] - rho[z]) for z in range(V)]
        ok &= all(sp.simplify(drift[z] - target[z]) == 0 for z in range(V))
    w = sp.symbols("w0:4", positive=True)
    n = [1, 0, 1, 0]
    sol = sp.solve([w[z] * (n[z] - rho[z]) - beta for z in range(V)], rho[:3] + [beta], dict=True)
    ok &= len(sol) == 1 and sp.simplify(sol[0][beta]) == 0
    v = sp.symbols("v0:4", real=True)
    Mv = [sum(v[j] for j in T.nbrs[z]) / T.q - v[z] for z in range(V)]
    ok &= sp.simplify(sum(-Mv[z] * Gam * w[z] * Mv[z] for z in range(V)) + Gam * sum(w[z] * Mv[z] ** 2 for z in range(V))) == 0
    nonconst = True
    for d in [(3,), (4,), (6,), (3, 3), (3, 3, 3)]:
        Tt = torus(d)
        for x in range(Tt.V):
            for y in Tt.nbrs[x]:
                diffv = [Tt.g[Tt.dif[z][x]] - Tt.g[Tt.dif[z][y]] for z in range(Tt.V)]
                nonconst &= len(set(diffv)) > 1
    ok &= nonconst
    rep("F", ok, "S6: on u = u_rho + c1 the configuration-C drift equals Gamma lambda e^c w_rho (n_C - rho) (symbolic, ring 4); "
                 "w (n - rho) = beta 1 with sum(n - rho) = 0 forces beta = 0 and n = rho; averaged-flow Lyapunov derivative "
                 "-Gamma sum w (M(u-u_rho))^2; S2/S8: u*(C) - u*(C') is non-constant for every move (rings 3,4,6, 3x3, 3^3)")


# ------------------------------------------------------------------ H: sojourn route, first order in 1/Gamma
def fam_H():
    ok, wit = True, []
    for d in [(4,), (5,), (6,), (7,), (8,), (3, 3), (4, 4), (3, 3, 3), (4, 4, 4)]:
        T = torus(d)
        V, q, g, g2 = T.V, T.q, T.g, T.g2
        r0 = F(1, 2 * q)
        e = T.Ei[0]
        v0 = [q * (g[T.dif[z][T.neg[e]]] - g[z]) for z in range(V)]          # lag after a hop from -e to 0 (lambda = 1)
        x = [q * sum(g[T.dif[z][y]] * v0[y] for y in range(V)) for z in range(V)]  # claimed integral q G * v0
        ok &= [-t for t in T.Mop(x)] == v0 and sum(x) == 0 and x[0] == -q * g[0]
        for D in range(1, V):
            nb = [j for j in T.nbrs[D] if j != 0]
            s = sum(g2[j] - g2[D] for j in nb)
            adj = D in T.Ei
            ok &= s == -g[D] - (g[0] / q if adj else 0)
            ok &= r0 * (-q * len(nb) * g[0] + q * q * s) == -r0 * q * q * (g[0] + g[D])
        if d in [(6,), (3, 3, 3)]:
            for D in range(1, V):
                vals = sorted({g2[j] for j in T.nbrs[D] if j != 0})
                if len(vals) > 1:
                    wit.append(f"{T.name()}: D={T.sites[D]} arrivals give G2 in {{{vals[0]}, {vals[-1]}}}")
                    break
    ok &= len(wit) == 2
    Gs = sp.symbols("Gamma", positive=True)
    ok &= sp.simplify(sp.series(Gs / (Gs + sp.Rational(1, 2)), Gs, sp.oo, 2).removeO() - (1 - 1 / (2 * Gs))) == 0
    rep("H", ok, "S8: int_0^inf e^{sM} v0 ds = q G*v0 (solves -Mx = v0, sum 0) with value -q G(0) lambda at the record; for every "
                 "D != 0: sum over N(D)\\{0} of (G2(D')-G2(D)) = -G(D) - [D in E] G(0)/q, so the mean sojourn shift is "
                 "-(r0 q^2 lambda/Gamma)(G(0)+G(D)) for adjacent and distant D alike (rings 4-8, 3x3, 4x4, 3^3, 4^3); matches "
                 "gamma = 1 - 1/(2Gamma) + O(Gamma^-2); arrival dependence: " + "; ".join(wit))


def fam_H_float():
    try:
        import numpy as np
        from scipy.integrate import solve_ivp
    except Exception as ex:  # pragma: no cover
        print(f"[H] SKIP [float] J(lambda): {ex}")
        return
    L, q, r0 = 6, 2, 0.25
    Gv = np.array([35 / 72, 5 / 72, -13 / 72, -19 / 72, -13 / 72, 5 / 72])
    out, ok = [], True
    for lam in (-1.5, -0.05, 0.05, 1.0):
        Z = np.sum(np.exp(-q * lam * Gv))
        us = q * lam * Gv + np.log(Z / L)
        v0 = q * lam * np.roll(Gv, -1) - q * lam * Gv

        def f(s, y):
            v = y[:L]
            Mv = 0.5 * (np.roll(v, 1) + np.roll(v, -1)) - v
            return np.concatenate([np.exp(us + v) * Mv, [np.exp(v[0]) - 1.0]])
        sol = solve_ivp(f, (0, 400), np.concatenate([v0, [0.0]]), rtol=1e-11, atol=1e-13, method="LSODA")
        coef = r0 * q * np.exp(us[0]) * sol.y[L, -1]
        ratio = coef / (-q * lam * Gv[0] / 2)
        ok &= np.sign(coef) == np.sign(-lam)
        if abs(lam) < 0.1:
            ok &= abs(ratio - 1) < 0.05
        out.append(f"lambda={lam}: {coef:.4f} (x{ratio:.3f} of linear)")
    rep("H", ok, "[float] ring 6, one record, exact-in-lambda first-order coefficient R_inf*J(lambda) of 1/Gamma in R/R_inf: "
                 + "; ".join(out))


# ------------------------------------------------------------------ K: quasi-static limit
def fam_K():
    ok = True
    w = sp.symbols("w0:5", positive=True)
    q, r0 = sp.Integer(2), sp.Rational(1, 4)
    S = sum(1 / x for x in w)
    ok &= sp.simplify(sum((1 / x) / S * q * r0 * x for x in w) - q * r0 * 5 / S) == 0
    lam = sp.symbols("lambda", real=True)
    T = torus((6,))
    Gs = [sp.Rational(x.numerator, x.denominator) for x in T.g]
    diff = T.V * sp.exp(-2 * lam * Gs[0]) - sum(sp.exp(-2 * lam * x) for x in Gs)
    ok &= sp.simplify(sp.series(diff, lam, 0, 2).removeO() + 2 * lam * T.V * Gs[0]) == 0
    thr = []
    cosr = {3: [F(1), F(-1, 2), F(-1, 2)], 4: [F(1), F(0), F(-1), F(0)],
            6: [F(1), F(1, 2), F(-1, 2), F(-1), F(-1, 2), F(1, 2)]}
    for d in [(6,), (3, 3, 3), (4, 4, 4)]:
        Tt = torus(d)
        L = d[0]
        c = cosr[L]
        spec = [-sum(2 - 2 * c[k] for k in kv) / Tt.q for kv in product(range(L), repeat=len(d)) if any(kv)]
        mu1 = max(spec)
        ok &= mu1 == -(2 - 2 * c[1]) / Tt.q
        f = [c[Tt.sites[z][0]] for z in range(Tt.V)]
        ok &= Tt.Mop(f) == [mu1 * x for x in f]
        thr.append(f"{Tt.name()}: lambda_c = V mu1 = {Tt.V * mu1}")
    u = sp.symbols("u0:4", real=True)
    eps = sp.symbols("epsilon", real=True)
    du = [1, -1, 2, -2]
    rho = [sp.exp(-(eps * du[z])) / sum(sp.exp(-(eps * du[y])) for y in range(4)) for z in range(4)]
    ok &= all(sp.simplify(sp.diff(rho[z], eps).subs(eps, 0) + sp.Rational(du[z], 4)) == 0 for z in range(4))
    rep("K", ok, "S9: fixed-field departure-timed rate sum_x (w_x^-1/S) q r0 w_x = q r0 V/S for any positive field, so R -> r0 q V/S "
                 "as Gamma -> 0 (averaging assumed); V e^{-q lambda G(0)} - Z = -q lambda V G(0) + O(lambda^2) and G(0) = max G give "
                 "R0 > R_inf iff lambda < 0; uniform quasi-static field: d rho = -d u/V and growth Gamma w0 (mu - lambda/V): " + "; ".join(thr))


# ------------------------------------------------------------------ S: [float] direct simulation
SIM_SRC = r'''
import numpy as np
import numba as nb

@nb.njit(cache=False)
def rhs(u, n, Gam, lam, nbar, L, out):
    for z in range(L):
        mu = 0.5 * (u[(z + 1) % L] + u[(z - 1) % L]) - u[z]
        out[z] = Gam * np.exp(u[z]) * (mu + lam * (n[z] - nbar))

@nb.njit(cache=False)
def step(u, n, Gam, lam, nbar, L, h, k1, k2, k3, k4, tmp, S0):
    rhs(u, n, Gam, lam, nbar, L, k1)
    for z in range(L):
        tmp[z] = u[z] + 0.5 * h * k1[z]
    rhs(tmp, n, Gam, lam, nbar, L, k2)
    for z in range(L):
        tmp[z] = u[z] + 0.5 * h * k2[z]
    rhs(tmp, n, Gam, lam, nbar, L, k3)
    for z in range(L):
        tmp[z] = u[z] + h * k3[z]
    rhs(tmp, n, Gam, lam, nbar, L, k4)
    s = 0.0
    for z in range(L):
        u[z] += h * (k1[z] + 2 * k2[z] + 2 * k3[z] + k4[z]) / 6.0
        s += np.exp(-u[z])
    sh = np.log(s / S0)
    for z in range(L):
        u[z] += sh

@nb.njit(cache=False)
def run(L, N, Gam, lam, nhops, burn, hmax, seed, B):
    np.random.seed(seed)
    r0 = 0.25
    nbar = N / L
    u = np.zeros(L)
    n = np.zeros(L)
    pos = np.zeros(N, np.int64)
    for i in range(N):
        pos[i] = (i * (L // N)) % L
        n[pos[i]] = 1.0
    k1 = np.zeros(L); k2 = np.zeros(L); k3 = np.zeros(L); k4 = np.zeros(L); tmp = np.zeros(L)
    S0 = float(L)
    T = 0.0
    hops = 0
    occ = np.zeros(L)
    aw = 0.0
    awmu = 0.0
    viol = 0
    rates = np.zeros(2 * N)
    started = False
    while hops < nhops + burn:
        gap = -np.log(np.random.random()) / B
        nsub = int(gap / hmax) + 1
        h = gap / nsub
        for s in range(nsub):
            if started:
                if N == 1:
                    x = pos[0]
                    wx = np.exp(u[x])
                    aw += 0.5 * h * wx
                    awmu += 0.5 * h * wx * (0.5 * (u[(x + 1) % L] + u[(x - 1) % L]) - u[x])
                else:
                    occ[(pos[1] - pos[0]) % L] += h
            step(u, n, Gam, lam, nbar, L, h, k1, k2, k3, k4, tmp, S0)
            if started:
                T += h
                if N == 1:
                    x = pos[0]
                    wx = np.exp(u[x])
                    aw += 0.5 * h * wx
                    awmu += 0.5 * h * wx * (0.5 * (u[(x + 1) % L] + u[(x - 1) % L]) - u[x])
        tot = 0.0
        for i in range(N):
            x = pos[i]
            wx = np.exp(u[x])
            for j in range(2):
                y = (x + 1) % L if j == 0 else (x - 1) % L
                rates[2 * i + j] = r0 * wx if n[y] == 0.0 else 0.0
                tot += rates[2 * i + j]
        if tot > B:
            viol += 1
        if np.random.random() * B < tot:
            r = np.random.random() * tot
            c = 0.0
            k = 0
            for k in range(2 * N):
                c += rates[k]
                if r < c:
                    break
            i = k // 2
            x = pos[i]
            y = (x + 1) % L if k % 2 == 0 else (x - 1) % L
            n[x] = 0.0
            n[y] = 1.0
            pos[i] = y
            hops += 1
            if hops == burn:
                started = True
    return T, hops - burn, occ, aw, awmu, viol
'''


def fam_S():
    try:
        import numpy as np
        ns = {}
        exec(SIM_SRC, ns)
        run = ns["run"]
    except Exception as ex:
        print(f"[S] SKIP [float] simulation unavailable: {type(ex).__name__}")
        return
    L, q, r0 = 6, 2, 0.25
    Gv = np.array([35 / 72, 5 / 72, -13 / 72, -19 / 72, -13 / 72, 5 / 72])
    run(L, 1, 1.0, 0.1, 500, 50, 0.02, 1, 1.0)
    ok, viol, o1, o2 = True, 0, [], []
    for Gam in (0.25, 1.0, 4.0):
        gam = 2 * Gam / (2 * Gam + 1)
        R = {}
        for lam, sd in ((0.2, 11), (-0.2, 12)):
            T, h, occ, aw, awmu, vi = run(L, 1, Gam, lam, 300000, 2000, min(0.02, 0.05 / Gam), sd, 2 * r0 * np.exp(0.5))
            R[lam], viol = h / T, viol + vi
        odd = (R[0.2] - R[-0.2]) / (2 * 0.2 * r0 * q)
        ok &= abs(odd - gam * q * Gv[0]) < 0.03 and abs(odd - q * Gv[0]) > 0.08
        o1.append(f"G={Gam}: {odd:.3f}/{gam * q * Gv[0]:.3f}")
        pis = {}
        for lam, sd in ((0.2, 21), (-0.2, 22)):
            T, h, occ, aw, awmu, vi = run(L, 2, Gam, lam, 500000, 2000, min(0.02, 0.05 / Gam), sd, 4 * r0 * np.exp(0.5))
            p = occ / T
            pis[lam], viol = np.array([p[1] + p[5], p[2] + p[4], p[3]]), viol + vi
        pi0 = np.array([6, 6, 3]) / 15
        base = -q * pi0 * (Gv[1:4] - pi0 @ Gv[1:4])
        fit = ((pis[0.2] - pis[-0.2]) / 0.4) @ base / (base @ base)
        ok &= abs(fit - gam) < 0.08 and abs(fit - 1) > 0.08
        o2.append(f"G={Gam}: {fit:.3f}/{gam:.3f}")
    lam = -1.5
    Z = np.sum(np.exp(-q * lam * Gv))
    Rinf = r0 * q * (Z / L) * np.exp(q * lam * Gv[0])
    R0 = r0 * q
    umax = np.max(q * lam * Gv + np.log(Z / L))
    Rs, idn = [], None
    for Gam, nh in ((0.01, 100000), (1.0, 100000), (10.0, 60000)):
        T, h, occ, aw, awmu, vi = run(L, 1, Gam, lam, nh, 2000, min(0.02, 0.04 / Gam), 31, r0 * q * np.exp(umax + 0.6))
        viol += vi
        Rs.append(h / T)
        if Gam == 1.0:
            idn = ((Gam + r0 * q) * awmu / T + Gam * lam * (1 - 1 / L) * aw / T) / (Gam * abs(lam) * aw / T)
    ok &= Rs[0] > Rs[1] > Rs[2] > Rinf and abs(Rs[0] / R0 - 1) < 0.06 and abs(Rs[2] / Rinf - 1) < 0.06 and abs(idn) < 0.01
    ok &= viol == 0
    rep("S", ok, f"[float] ring 6, thinning + RK4 on the level set: one-record odd part of R/(r0 q) per lambda (sim/theory "
                 f"gamma q G(0), slaved 0.972): {'; '.join(o1)}; pair-law gamma fit (sim/theory): {'; '.join(o2)}; lambda=-1.5: "
                 f"R/(r0q) at Gamma=0.01,1,10 = {Rs[0] / R0:.3f},{Rs[1] / R0:.3f},{Rs[2] / R0:.3f} between R0=1 and R_inf="
                 f"{Rinf / R0:.4f}; exact identity (S5) relative residual {idn:.1e}; bound violations {viol}")


if __name__ == "__main__":
    fam_Q()
    fam_A()
    fam_B()
    fam_C()
    fam_D()
    fam_E()
    fam_F()
    fam_H()
    fam_H_float()
    fam_K()
    fam_S()
    print(f"runtime {time.time() - T0:.0f}s; failed families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT check families {sorted(set(FAILS))}")
        sys.exit(1)
    print("SUMMARY: PARTIAL exact, for a well-posed joint process (A0): with log(kappa) != 0 and finite Gamma no stationary law "
          "(record law) x (field law) exists and no stationary law is reversible; sum_z 1/w_z is conserved; two records' separation "
          "jumps as simple random walk on the torus minus 0 at every Gamma. First order in log(kappa) (A1), every Gamma and record "
          "number: mean clock field given the records = gamma x slaved field, gamma = Gamma/(Gamma + r0 q) = 2Gamma/(2Gamma+1); record "
          "law = block 95's with log(kappa) -> gamma log(kappa). Not exact in log(kappa) at finite Gamma.")
    print("HIT: supplied relaxation clause, departure-timed hopping, W = 1 (well-posedness A0; first order also needs A1): (i) for "
          "log kappa != 0 and finite Gamma no joint law of product form is stationary and the joint process is never reversible; (ii) at "
          "first order in log kappa, for every Gamma and record number, block 95's pair law survives with log kappa -> gamma log kappa, "
          "gamma = 2Gamma/(2Gamma+1) = 1 - 1/(2Gamma) + O(Gamma^-2); (iii) one record: R = R_inf[1 - q log(kappa) G(0)/(2Gamma+1)] + "
          "O(log^2 kappa), diffusion constant exactly R/(2d): for kappa < 1 the lagging record is faster than the slaved one.")

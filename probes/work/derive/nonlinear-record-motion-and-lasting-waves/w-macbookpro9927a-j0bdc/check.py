#!/usr/bin/env python3
"""check.py for J:derive:nonlinear-record-motion-and-lasting-waves:a1 (worker w-macbookpro9927a-j0bdc, claude-opus-5-5).

The rule (the Nagel-Schreckenberg rule): N records on the ring Z_L, at most one per site, each carrying a speed content
v in 0..V. One step, all records at once: u = min(v + 1, V, gap), gap = number of empty sites up to the next record
ahead; then with probability r, u -> max(u - 1, 0); then every record advances by u and keeps speed u.
Slack s = gap - u. A record is SATURATED at a step when s = 0 (it moves its full gap).

Families
  Q  pinned sources (block 96 on main; blocks 122 and 123 on their branches; the task)
  D  r = 0: on every state that occurs after one step (all rings L <= 11, 9, 8 for V = 1, 2, 3; all N; all speeds):
     gap >= speed of the record ahead; a saturated record stays saturated and copies its leader's speed one step late;
     an unsaturated record moves min(v + 1, V). Every orbit from every initial state enters the free set (all move V)
     when N(V+1) < L, the jam set (all move their full gap) when N(V+1) > L, both when N(V+1) = L; both sets are
     invariant. Two modulated long-wave states translated exactly for 2000 steps; random large rings
  E  0 < r < 1: the support graph (the same for every r in (0,1)) on every state of every ring L <= 12, 9, 7 for
     V = 1, 2, 3 and every N < L: every state reaches a reference state (the stopped jam, with a self-loop, when N >= 2;
     one record cruising otherwise); its forward closure has period 1; under all-slowdown no speed ever rises
  M  the site-factorized mean-field version, exact: linearization weights W equal the ring Jacobian (unit differences
     are exact because the map is affine in each variable); V = 1 closes on the density with weights
     (1 - p, p(1 - rho), p rho) at displacements (0, +1, -1), p = 1 - r, and 1 - |lam|^2 = 2p(1-p)(1-cos k)
     + 4 p^2 rho(1-rho) sin^2 k; for V >= 2 some weights are negative; exact Schur-Cohn damping at 144 rational points;
     exact certificates of a root outside the unit circle at (V, r, rho, e^{ik}) = (2, 0, 3/20, (-5+12i)/13),
     (2, 1/50, 3/20, (-5+12i)/13), (5, 0, 1/50, (-8+15i)/17); the Schur-Cohn routine is also tested on random polynomials
  N  [float] controlled numerics at r > 0: the stationary autocorrelation of the density mode at fixed k0 = 2 pi/64 on
     rings L = 128..1024 (jackknife errors over 32 independent rings), decay and L-independence, phase velocity; the
     same simulator at r = 0 keeps the mode exactly (the exact result of D); decay time versus k; one small r
"""
import hashlib
import itertools
import json
import os
import random
import subprocess
import sys
import time
from collections import deque
from fractions import Fraction as F
from math import comb

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
B96 = ("docs/ADMISSIBILITY_RULE_WAVES_AMONG_MOVING_RECORDS_NEED_A_COUPLING_THAT_TIME_REVERSAL_FLIPS_CLOCKED_RECORD_MOTION"
       "_NEVER_OSCILLATES_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B122 = ("docs/ADMISSIBILITY_RULE_WAVES_NEED_SIGNED_WEIGHTS_A_FORMATION_RULE_WITH_NONNEGATIVE_WEIGHTS_KEEPS_AN_UNDAMPED_BRANCH"
        "_ONLY_BY_RIGID_TRANSPORT_AND_THE_AMPLITUDE_STEP_IS_A_SIGNED_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md")
B123 = ("docs/ADMISSIBILITY_RULE_PERSISTENT_RECORDS_IN_THREE_DIMENSIONS_CARRY_DAMPED_DENSITY_WAVES_ALONG_THE_BODY_DIAGONALS"
        "_PAST_AN_EXACT_THRESHOLD_AND_NONE_ALONG_THE_AXES_BOUNDED_THEOREM_NOTE_2026-09-24.md")
SRC = [("block96", "60c5f194d940a7bbaf1cdd545296e31d74a02f1a", B96,
        "641c25cec40bd76fe0c6cf5f08da3a131c617d39fe9e03945fdd4312b2ce321a",
        ["For centered real f, <f,exp(tQ)f>_pi=sum c_j exp(lambda_j t), c_j>=0 and lambda_j<=0.",
         "The endpoints p=0 and p=1 are exceptional, with period-two behavior and free streams respectively."], "main"),
       ("block122", "248efca4af4cccbc4c22124d477f8eb2c1d7bb06", B122,
        "7823e475f85f1c14556d164852b4eeada207b000f8f368aec0f692b664a4abfe",
        ["- For nonnegative gain-one weights, every branch satisfies `|λ(k)| ≤ 1`.",
         "*Statement.* For nonnegative gain-one weights, some branch has `|λ(k)| = 1` on a set of `k` with nonempty "
         "interior only if the rule is rigid transport.",
         "- **Rigid transport.** Each entry of each `w_j` is carried by a single displacement, and the resulting phases "
         "form a diagonal conjugation times a global phase. The rule then moves everything at one velocity, up to a gauge.",
         "1. *Nonlinear rules.* T1–T2 are about the linear law in level time. A nonlinear formation law is not covered."],
        "physics-loop/admissibility-induced-law-block122-waves-need-signed-weights-20260924"),
       ("block123", "f8fb5519520fe9ff1a2a39be8f9cf38aca6124e4", B123,
        "4a6eb7a37f21dad0c8c6281cabae93474d3e6d0edea586f57bc0d0e9fa50d371",
        ["- **T4: damped.** Every such density branch has modulus below one away from `k = 0`, as block 122 requires of "
         "any rule with nonnegative weights."],
        "physics-loop/admissibility-induced-law-block123-persistent-records-in-three-dimensions-damped-density-waves-20260924")]
TASKQ = ("74754e62f3cd2d6e538922a83d4b3bfe65c3c8b4", "J:derive:nonlinear-record-motion-and-lasting-waves:a1",
         ["every LINEAR formation or motion rule with nonnegative gain-one weights has every branch |lambda| <= 1",
          "each record carries a speed 0..v; it rises by one if the sites ahead are empty, falls to the gap if blocked, "
          "then slows by one with probability r; all records then advance by their speed",
          "(b) linearize the mean-field version about the uniform state and show whether the linear branches are damped, "
          "as block 122 requires;",
          "HIT: (a) with an exact or controlled demonstration either way."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
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


# ------------------------------------------------------------------ D: r = 0, exact
def det_step(g, v, V):
    """gaps g_i (record i to record i+1), speeds v_i -> (new gaps, new speeds = moves u)."""
    N = len(g)
    u = [min(v[i] + 1, V, g[i]) for i in range(N)]
    return [g[i] - u[i] + u[(i + 1) % N] for i in range(N)], u


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for a in range(total + 1):
        for rest in compositions(total - a, parts - 1):
            yield (a,) + rest


def in_free(g, v, V):
    return all(x >= V - 1 for x in v) and all(x >= V for x in g)


def in_jam(g, v, V):
    N = len(g)
    return all(g[i] <= min(v[i] + 1, V) for i in range(N)) and all(g[(i + 1) % N] <= g[i] + 1 for i in range(N))


def sim_positions(x, v, V, L, steps, shift):
    """exact integer run on positions; returns True iff the occupied set shifts by `shift` at every step."""
    x, v = list(x), list(v)
    N = len(x)
    for _ in range(steps):
        order = sorted(range(N), key=lambda i: x[i])
        x = [x[i] for i in order]
        v = [v[i] for i in order]
        g = [((x[(i + 1) % N] - x[i] - 1) % L) if N > 1 else L - 1 for i in range(N)]
        u = [min(v[i] + 1, V, g[i]) for i in range(N)]
        old = set(x)
        x = [(x[i] + u[i]) % L for i in range(N)]
        v = u
        if set(x) != {(y + shift) % L for y in old}:
            return False
    return True


def fam_D():
    t0 = time.time()
    LMAX = {1: 11, 2: 9, 3: 8}
    lemma_viol = orbit_viol = inv_viol = crit_viol = 0
    n_states = 0
    worst = {}
    for V in (1, 2, 3):
        for L in range(2, LMAX[V] + 1):
            w = 0
            for N in range(1, L):
                crit = N * (V + 1) - L
                for g0 in compositions(L - N, N):
                    for v0 in itertools.product(range(V + 1), repeat=N):
                        n_states += 1
                        g1, v1 = det_step(list(g0), list(v0), V)          # a state that occurs after one step
                        u1 = [min(v1[i] + 1, V, g1[i]) for i in range(N)]
                        g2, v2 = det_step(g1, v1, V)
                        u2 = [min(v2[i] + 1, V, g2[i]) for i in range(N)]
                        for i in range(N):
                            j = (i + 1) % N
                            if g1[i] < v1[j]:
                                lemma_viol += 1                                  # gap >= speed of the record ahead
                            if u1[i] == g1[i]:
                                if not (u2[i] == g2[i] and u2[i] == u1[j]):
                                    lemma_viol += 1                              # saturation persists, copies leader
                            elif u1[i] != min(v1[i] + 1, V):
                                lemma_viol += 1                                  # unsaturated moves min(v+1, V)
                        g, v = list(g0), list(v0)
                        for tt in range(3 * L + 5):
                            if (crit <= 0 and in_free(g, v, V)) or (crit >= 0 and in_jam(g, v, V)):
                                break
                            g, v = det_step(g, v, V)
                        else:
                            orbit_viol += 1
                            continue
                        w = max(w, tt)
                        for _ in range(2):                                       # invariance and the rigid move
                            u = [min(v[i] + 1, V, g[i]) for i in range(N)]
                            if crit <= 0 and not (in_free(g, v, V) and all(x == V for x in u)):
                                inv_viol += 1
                            if crit >= 0 and not (in_jam(g, v, V) and u == g):
                                inv_viol += 1
                            g, v = det_step(g, v, V)
                        if crit == 0 and any(x != V for x in g):
                            crit_viol += 1
            worst[(V, L)] = w
    g, v = [0, 2], [0, 2]                                    # at t = 0 saturation need not persist
    sat0 = [min(v[i] + 1, 2, g[i]) == g[i] for i in range(2)]
    g, v = det_step(g, v, 2)
    sat1 = [min(v[i] + 1, 2, g[i]) == g[i] for i in range(2)]
    rep("D", lemma_viol == 0 and sat0 == [True, True] and sat1[0] is False,
        f"lemmas on the states after one step of {n_states} initial states (car 0 at site 0; V<=3, L<=11/9/8, all N): "
        f"violations {lemma_viol}; at t=0 they can fail: gaps (0,2), speeds (0,2), V=2, L=4 saturated {sat0} -> {sat1}")
    rep("D", orbit_viol == 0 and inv_viol == 0 and crit_viol == 0,
        f"every orbit enters the free set (N(V+1)<L) / jam set (N(V+1)>L) / uniform gaps V (=): misses {orbit_viol}, "
        f"invariance or rigid-move violations {inv_viol}, critical non-uniform {crit_viol}")
    tr = {V: [worst[(V, L)] for L in range(2, LMAX[V] + 1)] for V in (1, 2, 3)}
    ok_tr = all(worst[(V, L)] <= L // 2 for (V, L) in worst)
    rep("D", ok_tr, f"maximal transients for L = 2..: V=1 {tr[1]}; V=2 {tr[2]}; V=3 {tr[3]} (all <= floor(L/2))")

    # two modulated long-wave states, translated exactly for 2000 steps
    L, V = 240, 2
    N = 60                                    # free: N(V+1) = 180 < 240
    extra = [1 + round(np.cos(2 * np.pi * i / N)) for i in range(N)]
    extra[0] += (L - N - N * V) - sum(extra)
    gaps = [V + e for e in extra]
    x = list(itertools.accumulate([0] + [gg + 1 for gg in gaps[:-1]]))
    okf = in_free(gaps, [V] * N, V) and sim_positions(x, [V] * N, V, L, 2000, +V)
    ampf = abs(np.exp(-2j * np.pi * np.array(x) / L).sum())
    N = 120                                   # jam: N(V+1) = 360 > 240
    gaps = [round(1 + np.cos(2 * np.pi * i / N)) for i in range(N)]
    gaps[0] += (L - N) - sum(gaps)
    x = list(itertools.accumulate([0] + [gg + 1 for gg in gaps[:-1]]))
    okj = in_jam(gaps, gaps, V) and sim_positions(x, gaps, V, L, 2000, -1)
    ampj = abs(np.exp(-2j * np.pi * np.array(x) / L).sum())
    rep("D", okf and okj, f"L=240, V=2: a modulated free state (N=60) moves +2 and a modulated jam (N=120) moves -1 "
        f"every step for 2000 steps; |rho_hat(2pi/L)| = {ampf:.3f}, {ampj:.3f} [float], constant")

    # random large rings
    rng = random.Random(5)
    trans_ratio = 0
    bad = 0
    for V in (2, 5):
        for L in (500, 2000):
            for _ in range(10):
                N = rng.randint(1, L - 1)
                pos = sorted(rng.sample(range(L), N))
                g = np.array([((pos[(i + 1) % N] - pos[i] - 1) % L) if N > 1 else L - 1 for i in range(N)])
                v = np.array([rng.randint(0, V) for _ in range(N)])
                crit = N * (V + 1) - L
                for tt in range(4 * L):
                    free = (v >= V - 1).all() and (g >= V).all()
                    jam = (g <= np.minimum(v + 1, V)).all() and (np.roll(g, -1) <= g + 1).all()
                    if (crit <= 0 and free) or (crit >= 0 and jam):
                        break
                    u = np.minimum(np.minimum(v + 1, V), g)
                    g, v = g - u + np.roll(u, -1), u
                else:
                    bad += 1
                    continue
                trans_ratio = max(trans_ratio, tt / L)
    rep("D", bad == 0, f"40 random states on rings L = 500, 2000 (V = 2, 5): all reach the rigid regime; "
        f"max transient/L = {trans_ratio:.3f}  ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ E: 0 < r < 1, exact support graph
def successors(P, S, V, L):
    """P sorted positions, S speeds. Yields (new sorted positions, new speeds, all_slow flag, per-record new speeds)."""
    N = len(P)
    g = [((P[(i + 1) % N] - P[i] - 1) % L) if N > 1 else L - 1 for i in range(N)]
    u = [min(S[i] + 1, V, g[i]) for i in range(N)]
    movers = [i for i in range(N) if u[i] >= 1]
    for mask in range(1 << len(movers)):
        w = list(u)
        for b, i in enumerate(movers):
            if mask >> b & 1:
                w[i] -= 1
        newx = [(P[i] + w[i]) % L for i in range(N)]
        order = sorted(range(N), key=lambda i: newx[i])
        yield tuple(newx[i] for i in order), tuple(w[i] for i in order), mask == (1 << len(movers)) - 1, w


def fam_E():
    """Reference state s*: the stopped jam at sites 0..N-1 (N >= 2, or V = 1, or L = 2); for one record with
    m = min(V, L-1) >= 2 the record at site 0 with speed m. Exact: every state reaches s*; the forward closure R of s*
    (then the unique closed class) has period 1 (gcd of level differences along its edges)."""
    from math import gcd
    t0 = time.time()
    total = cases = n_jam = 0
    fails = []
    for V, Lmax in ((1, 12), (2, 9), (3, 7)):
        for L in range(2, Lmax + 1):
            for N in range(1, L):
                states = [(P, S) for P in itertools.combinations(range(L), N)
                          for S in itertools.product(range(V + 1), repeat=N)]
                idx = {s: i for i, s in enumerate(states)}
                succ = [[] for _ in states]
                preds = [[] for _ in states]
                rise = 0
                for i, (P, S) in enumerate(states):
                    for P2, S2, allslow, w in successors(P, S, V, L):
                        b = idx[(P2, S2)]
                        succ[i].append(b)
                        preds[b].append(i)
                        if allslow and any(w[j] > S[j] for j in range(N)):
                            rise += 1
                jamref = N >= 2 or V == 1 or L == 2
                ref = idx[(tuple(range(N)), (0,) * N)] if jamref else idx[((0,), (min(V, L - 1),))]
                n_jam += jamref
                back = [False] * len(states)
                back[ref] = True
                dq = deque([ref])
                while dq:
                    a = dq.popleft()
                    for b in preds[a]:
                        if not back[b]:
                            back[b] = True
                            dq.append(b)
                lev = {ref: 0}
                dq = deque([ref])
                while dq:
                    a = dq.popleft()
                    for b in succ[a]:
                        if b not in lev:
                            lev[b] = lev[a] + 1
                            dq.append(b)
                per = 0
                for a in lev:
                    for b in succ[a]:
                        per = gcd(per, lev[a] + 1 - lev[b])
                selfloop = ref in succ[ref]
                total += len(states)
                cases += 1
                if not (all(back) and per == 1 and rise == 0 and (selfloop or not jamref)):
                    fails.append((V, L, N, sum(back), len(states), per, rise, selfloop))
    rep("E", not fails, f"{cases} (V, L, N) cases, {total} states: every state reaches the reference state (the stopped "
        f"jam at sites 0..N-1 in {n_jam} cases, which has a self-loop; one record cruising at min(V, L-1) otherwise); "
        f"its forward closure has period 1; no speed rises under all-slowdown; failures {fails[:3]}  "
        f"({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ M: mean-field version, exact
class G:
    """Gaussian rational a + b i with Fraction parts."""
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a + o.a, s.b + o.b)
    __radd__ = __add__

    def __sub__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a - o.a, s.b - o.b)

    def __neg__(s):
        return G(-s.a, -s.b)

    def __mul__(s, o):
        o = o if isinstance(o, G) else G(o)
        return G(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__

    def conj(s):
        return G(s.a, -s.b)

    def n2(s):
        return s.a * s.a + s.b * s.b

    def inv(s):
        d = s.n2()
        return G(s.a / d, -s.b / d)

    def __truediv__(s, o):
        o = o if isinstance(o, G) else G(o)
        return s * o.inv()

    def iszero(s):
        return s.a == 0 and s.b == 0

    def __complex__(s):
        return complex(float(s.a), float(s.b))


def trans(V, r, q):
    """T[v][u]: probability that a record of speed v ends with speed (= move) u, given densities q[0..V-1] at the
    next V sites, the sites independent (the mean-field factorization). Works for Fractions and sympy."""
    T = [[0] * (V + 1) for _ in range(V + 1)]
    for v in range(V + 1):
        a = min(v + 1, V)
        emp, pw = 1, []
        for d in range(a):
            pw.append(emp * q[d])
            emp = emp * (1 - q[d])
        pw.append(emp)
        for w in range(a + 1):
            if w >= 1:
                T[v][w] += (1 - r) * pw[w]
                T[v][w - 1] += r * pw[w]
            else:
                T[v][0] += pw[0]
    return T


def solve_q(A, b):
    n = len(A)
    Mx = [list(A[i]) + [b[i]] for i in range(n)]
    for c in range(n):
        p = next(i for i in range(c, n) if Mx[i][c] != 0)
        Mx[c], Mx[p] = Mx[p], Mx[c]
        Mx[c] = [x / Mx[c][c] for x in Mx[c]]
        for i in range(n):
            if i != c and Mx[i][c] != 0:
                f = Mx[i][c]
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
    return [Mx[i][n] for i in range(n)]


def mf_weights(V, r, rho):
    """uniform fixed point p (speed distribution) and weights W[u][d] + T0: delta c_u(y) = sum_v' T0[v'][u] eps_v'(y-u)
    + sum_d Wd[u][d] eta(y-d), eta = sum_v' eps_v'. Multilinearity: dT/dq_j = T(q_j=1) - T(q_j=0)."""
    T0 = trans(V, r, [rho] * V)
    A = [[T0[v][u] - (1 if u == v else 0) for v in range(V + 1)] for u in range(V)] + [[F(1)] * (V + 1)]
    p = solve_q(A, [F(0)] * V + [F(1)])
    assert all(sum(p[v] * T0[v][u] for v in range(V + 1)) == p[u] for u in range(V + 1))
    Wd = [dict() for _ in range(V + 1)]
    for j in range(V):
        hi = trans(V, r, [rho] * j + [F(1)] + [rho] * (V - 1 - j))
        lo = trans(V, r, [rho] * j + [F(0)] + [rho] * (V - 1 - j))
        for u in range(V + 1):
            gu = sum(rho * p[v] * (hi[v][u] - lo[v][u]) for v in range(V + 1))
            d = u - (j + 1)
            Wd[u][d] = Wd[u].get(d, F(0)) + gu
    return T0, p, Wd


def mf_map_ring(c, V, r, L):
    rho = [sum(c[v][x] for v in range(V + 1)) for x in range(L)]
    out = [[F(0)] * L for _ in range(V + 1)]
    for x in range(L):
        T = trans(V, r, [rho[(x + j) % L] for j in range(1, V + 1)])
        for v in range(V + 1):
            if c[v][x] != 0:
                for u in range(V + 1):
                    out[u][(x + u) % L] += c[v][x] * T[v][u]
    return out


def symbol(V, T0, Wd, z):
    """M(z)[u][v'] = T0[v'][u] z^-u + sum_d Wd[u][d] z^-d, z = e^{ik} a Gaussian rational of modulus one."""
    zi = z.inv()
    pw = {0: G(1)}
    for e in range(1, V + 2):
        pw[e] = pw[e - 1] * z
        pw[-e] = pw[-(e - 1)] * zi
    M = []
    for u in range(V + 1):
        ex = G(0)
        for d, w in Wd[u].items():
            ex = ex + pw[-d] * w
        M.append([pw[-u] * T0[vp][u] + ex for vp in range(V + 1)])
    return M


def charpoly(A):
    """Faddeev-LeVerrier; returns coefficients c_0..c_n of det(lam I - A)."""
    n = len(A)
    c = [G(0)] * (n + 1)
    c[n] = G(1)
    Mk = [[G(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = [[sum((A[i][l] * Mk[l][j] for l in range(n)), G(0)) for j in range(n)] for i in range(n)]
        Mk = [[AM[i][j] + (c[n - k + 1] if i == j else G(0)) for j in range(n)] for i in range(n)]
        AM = [[sum((A[i][l] * Mk[l][j] for l in range(n)), G(0)) for j in range(n)] for i in range(n)]
        c[n - k] = -sum((AM[i][i] for i in range(n)), G(0)) / k
    return c


def schur_cohn(a):
    """a_0..a_n Gaussian rationals, a_n != 0: True iff every root lies strictly inside the unit circle."""
    a = list(a)
    while len(a) > 1:
        a0, an = a[0], a[-1]
        if a0.n2() >= an.n2():
            return False
        n = len(a) - 1
        q = [an.conj() * a[j] - a0 * a[n - j].conj() for j in range(n + 1)]
        assert q[0].iszero()
        a = q[1:]
    return True


def det(Mx):
    Mx = [row[:] for row in Mx]
    n, d = len(Mx), G(1)
    for c in range(n):
        p = next((i for i in range(c, n) if not Mx[i][c].iszero()), None)
        if p is None:
            return G(0)
        if p != c:
            Mx[c], Mx[p] = Mx[p], Mx[c]
            d = -d
        d = d * Mx[c][c]
        ic = Mx[c][c].inv()
        for i in range(c + 1, n):
            if not Mx[i][c].iszero():
                f = Mx[i][c] * ic
                Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[c])]
    return d


def resultant(a, b):
    """Sylvester resultant of polynomials with coefficient lists a_0..a_m, b_0..b_n."""
    m, n = len(a) - 1, len(b) - 1
    S = []
    for i in range(n):
        S.append([G(0)] * i + list(reversed(a)) + [G(0)] * (n - 1 - i))
    for i in range(m):
        S.append([G(0)] * i + list(reversed(b)) + [G(0)] * (m - 1 - i))
    return det(S)


def fam_M():
    t0 = time.time()
    # M1: the ring Jacobian equals the weights, exactly
    okJ = True
    for V, r, rho, L in ((1, F(1, 4), F(1, 3), 5), (2, F(1, 4), F(1, 4), 7), (2, F(0), F(3, 20), 7), (3, F(1, 2), F(1, 10), 9)):
        T0, p, Wd = mf_weights(V, r, rho)
        c0 = [[rho * p[v]] * L for v in range(V + 1)]
        base = mf_map_ring(c0, V, r, L)
        okJ &= all(base[v][x] == c0[v][x] for v in range(V + 1) for x in range(L))
        for vp in range(V + 1):
            for x in range(L):
                c1 = [row[:] for row in c0]
                c1[vp][x] += 1
                out = mf_map_ring(c1, V, r, L)
                for u in range(V + 1):
                    for y in range(L):
                        d = (y - x) % L
                        want = (T0[vp][u] if (u - d) % L == 0 else 0) + sum(w for dd, w in Wd[u].items() if (dd - d) % L == 0)
                        okJ &= out[u][y] - base[u][y] == want
    rep("M", okJ, "fixed point and linearization weights equal the exact ring Jacobian at 4 (V, r, rho) points "
        "(unit differences are exact: the map is affine in each variable)")

    # M2: V = 1 closes on the density with nonnegative weights; the exact damping identity
    pS, rS, kS = sp.symbols("p rho k", real=True)
    T0, p, Wd = None, None, None
    okV1 = True
    for r, rho in ((F(1, 4), F(1, 3)), (F(0), F(1, 5)), (F(1, 2), F(7, 10))):
        T0, pp, Wd = mf_weights(1, r, rho)
        w = {0: T0[0][0] + Wd[1].get(0, 0), 1: T0[0][1], -1: Wd[0].get(-1, 0)}
        okV1 &= all(T0[v][u] == T0[0][u] for v in range(2) for u in range(2))
        okV1 &= w == {0: r, 1: (1 - r) * (1 - rho), -1: (1 - r) * rho}
    lam = (1 - pS) + pS * (1 - rS) * sp.exp(-sp.I * kS) + pS * rS * sp.exp(sp.I * kS)
    ident = sp.simplify(sp.expand_complex(1 - lam * sp.conjugate(lam)) - (2 * pS * (1 - pS) * (1 - sp.cos(kS))
                                                                          + 4 * pS ** 2 * rS * (1 - rS) * sp.sin(kS) ** 2))
    okV1 &= ident == 0
    rep("M", okV1, "V=1: T independent of the speed, density weights (r, (1-r)(1-rho), (1-r)rho) at (0,+1,-1) at 3 "
        "points; 1-|lam|^2 = 2p(1-p)(1-cos k) + 4p^2 rho(1-rho) sin^2 k (sympy, symbolic)")

    # M3: V >= 2 weights are signed
    negs = []
    for V in (2, 3, 5):
        T0, pp, Wd = mf_weights(V, F(1, 4), F(1, 4))
        neg = [(u, d, w) for u in range(V + 1) for d, w in Wd[u].items() if w < 0 and d != u]
        negs.append((V, len(neg), min(w for _, _, w in neg)))
    rep("M", all(n > 0 for _, n, _ in negs), "r=rho=1/4: negative weights at displacements carrying no T0 term: "
        + ", ".join(f"V={V}: {n} (min {m})" for V, n, m in negs))

    # Schur-Cohn sanity on random polynomials against numpy roots
    rng = random.Random(3)
    agree = tested = 0
    while tested < 300:
        n = rng.randint(1, 6)
        co = [G(F(rng.randint(-9, 9), rng.randint(1, 9)), F(rng.randint(-9, 9), rng.randint(1, 9))) for _ in range(n)]
        co.append(G(F(rng.randint(1, 9), rng.randint(1, 9)), F(rng.randint(-9, 9), rng.randint(1, 9))))
        rts = np.roots([complex(c) for c in reversed(co)])
        m = max(abs(rts))
        if abs(m - 1) < 1e-6:
            continue
        tested += 1
        agree += schur_cohn(co) == (m < 1)
    # M4: damping certificates at rational points
    zs = [G(F(4, 5), F(3, 5)), G(F(3, 5), F(4, 5)), G(0, 1), G(F(-5, 13), F(12, 13)), G(F(-3, 5), F(4, 5)), G(-1)]
    ncert = nstable = 0
    for V in (2, 3, 5):
        for r in (F(1, 4), F(1, 2)):
            for rho in (F(1, 10), F(1, 4), F(1, 2), F(4, 5)):
                T0, pp, Wd = mf_weights(V, r, rho)
                for z in zs:
                    ncert += 1
                    nstable += schur_cohn(charpoly(symbol(V, T0, Wd, z)))
    rep("M", agree == tested and nstable == ncert,
        f"Schur-Cohn routine agrees with numpy roots on {agree}/{tested} random polynomials; exact damping (all roots "
        f"strictly inside) at {nstable}/{ncert} points V in (2,3,5), r in (1/4,1/2), rho in (1/10,1/4,1/2,4/5), "
        f"e^ik in (4+3i)/5,(3+4i)/5,i,(-5+12i)/13,(-3+4i)/5,-1")

    # M5: exact roots outside the unit circle
    out, mxs = [], []
    for V, r, rho, z in ((2, F(0), F(3, 20), G(F(-5, 13), F(12, 13))), (2, F(1, 50), F(3, 20), G(F(-5, 13), F(12, 13))),
                         (5, F(0), F(1, 50), G(F(-8, 17), F(15, 17)))):
        T0, pp, Wd = mf_weights(V, r, rho)
        chi = charpoly(symbol(V, T0, Wd, z))
        while chi[0].iszero():
            chi = chi[1:]                                  # strip roots at 0
        n = len(chi) - 1
        star = [chi[n - j].conj() for j in range(n + 1)]
        res = resultant(chi, star)
        sc = schur_cohn(chi)
        mx = max(abs(np.roots([complex(c) for c in reversed(chi)])))
        out.append((not sc) and not res.iszero())
        mxs.append(round(float(mx), 5))
    rep("M", all(out), f"3 points (V,r,rho,e^ik) = (2,0,3/20,(-5+12i)/13), (2,1/50,3/20,same), (5,0,1/50,(-8+15i)/17): "
        f"Schur-Cohn fails and Res(chi, chi*) != 0 (no root on the circle), so a root lies outside: {out}; "
        f"max|lam| {mxs} [float]  "
        f"({time.time() - t0:.0f}s)")

    # M6: [float] grid scan of max_k |lam(k)|, weights exact then converted
    ks = np.pi * np.arange(1, 361) / 360
    unstable = {}
    for V in range(2, 7):
        us = np.arange(V + 1)
        for r in (F(0), F(1, 50), F(1, 20), F(1, 10), F(1, 5)):
            for irho in range(1, 100):
                T0, pp, Wd = mf_weights(V, r, F(irho, 100))
                A = np.array([[float(T0[vp][u]) for vp in range(V + 1)] for u in range(V + 1)])
                Ms = np.exp(-1j * np.outer(ks, us))[:, :, None] * A[None]
                for u in range(V + 1):
                    ex = sum(float(w) * np.exp(-1j * ks * d) for d, w in Wd[u].items())
                    Ms[:, u, :] += ex[:, None]
                m = np.abs(np.linalg.eigvals(Ms)).max()
                if m > 1 + 1e-9:
                    unstable.setdefault((V, str(r)), []).append(irho)
    need = all(x in unstable.get(key, []) for key, x in (((2, "0"), 15), ((2, "1/50"), 15), ((5, "0"), 2)))
    damped_hi = not any(key[1] in ("1/20", "1/10", "1/5") for key in unstable)
    desc = "; ".join(f"V={V} r={r}: rho in [{min(v) / 100}, {max(v) / 100}] ({len(v)} pts)" for (V, r), v in sorted(unstable.items()))
    rep("M", need and damped_hi, f"[float] scan V=2..6, r in (0,1/50,1/20,1/10,1/5), rho = 0.01..0.99, 360 k in (0,pi]: "
        f"max|lam| > 1 only at {desc}; damped at every r >= 1/20 point")


# ------------------------------------------------------------------ N: [float] controlled numerics
def mc_run(L, rho, V, r, S, Teq, T, ms, seed):
    rng = np.random.default_rng(seed)
    N = int(round(rho * L))
    x = np.sort(np.stack([rng.choice(L, N, replace=False) for _ in range(S)]), axis=1)
    v = np.zeros((S, N), np.int64)
    ks = 2 * np.pi * np.array(ms) / L
    rec = np.zeros((len(ms), S, T), complex)
    moved = 0
    for t in range(Teq + T):
        gap = (np.roll(x, -1, axis=1) - x - 1) % L
        v = np.minimum(np.minimum(v + 1, V), gap)
        if r > 0:
            v = np.where(rng.random((S, N)) < r, np.maximum(v - 1, 0), v)
        x = (x + v) % L
        if t >= Teq:
            moved += v.sum()
            for a, k in enumerate(ks):
                rec[a, :, t - Teq] = np.exp(-1j * k * x).sum(1)
    return N, rec, moved / (S * T * L)


def corr(rec, N, taus):
    S, T = rec.shape
    return np.array([(rec[:, tau:] * np.conj(rec[:, :T - tau])).mean(1) / N for tau in taus]).T   # (S, len(taus))


def ratio_jk(C):
    """R(tau) = |mean_s C_s(tau)| / mean_s C_s(0); jackknife errors over the S independent rings."""
    S = C.shape[0]
    R = np.abs(C.mean(0)) / C[:, 0].real.mean()
    loo = np.array([np.abs(np.delete(C, s, 0).mean(0)) / np.delete(C, s, 0)[:, 0].real.mean() for s in range(S)])
    return R, np.sqrt((S - 1) / S * ((loo - loo.mean(0)) ** 2).sum(0))


def phase_velocity(C, k, tmax=32):
    m = C.mean(0)
    ph = np.unwrap(np.angle(m[1:tmax + 1] / m[0]))
    t = np.arange(1, tmax + 1)
    return -np.polyfit(t, ph, 1)[0] / k


def fam_N():
    t0 = time.time()
    taus_chk = [64, 256, 1024]
    dense = list(range(0, 33))
    lines = []
    allok = True
    for V, rho, r, cexact in ((1, 0.25, 0.25, None), (2, 0.5, 0.25, None), (2, 0.15, 0.25, None)):
        Rs, Es, cs, Js = [], [], [], []
        for L in (128, 256, 512, 1024):
            N, rec, J = mc_run(L, rho, V, r, S=32, Teq=10000, T=16384, ms=[L // 64], seed=L + 10 * V)
            C = corr(rec[0], N, dense + taus_chk)
            R, E = ratio_jk(C[:, [0] + list(range(len(dense), len(dense) + len(taus_chk)))])
            Rs.append(R[1:]); Es.append(E[1:]); cs.append(phase_velocity(C[:, :len(dense)], 2 * np.pi / 64)); Js.append(J)
        Rs, Es = np.array(Rs), np.array(Es)
        big = max(abs(Rs[2, j] - Rs[3, j]) / np.hypot(Es[2, j], Es[3, j]) for j in range(3))   # L = 512 vs 1024
        drift = np.abs(Rs - Rs[3]).max()                                                       # every L vs 1024
        decay = Rs[:, 0].max() < 0.95 and Rs[:, 1].max() < 0.35 and Rs[:, 2].max() < 0.05
        ok = decay and big < 3 and drift < 0.05
        if V == 1:
            p = 1 - r
            Jx = (1 - np.sqrt(1 - 4 * p * rho * (1 - rho))) / 2
            cx = p * (1 - 2 * rho) / np.sqrt(1 - 4 * p * rho * (1 - rho))
            ok &= abs(Js[-1] - Jx) / Jx < 0.005 and abs(cs[-1] - cx) / cx < 0.03
            extra = f"; J={Js[-1]:.5f} vs exact {Jx:.5f}, c={cs[-1]:.4f} vs J'(rho)={cx:.4f}"
        else:
            ok &= (cs[-1] < 0) if rho == 0.5 else (cs[-1] > 0)
            extra = f"; J={Js[-1]:.4f}, c={cs[-1]:.3f}"
        allok &= ok
        lines.append(f"V={V} rho={rho} r={r}: R(64,256,1024) L=128: {np.round(Rs[0], 3)}  L=1024: {np.round(Rs[-1], 3)} "
                     f"(+-{np.round(Es[-1], 3)}); 512 vs 1024 max |dR|/err {big:.2f}, max drift vs 1024 {drift:.3f}{extra}")
    rep("N", allok, "[float] density mode at k0 = 2pi/64 decays (R(1024) < 0.05 on every L); the curve converges as L grows "
        "(L = 512 and 1024 within 3 errors, every L within 0.05 of L = 1024):\n     " + "\n     ".join(lines))

    # the same simulator at r = 0 keeps the mode exactly (D's result)
    ok0, msg0 = True, []
    for rho, cexp in ((0.15, 2.0), (0.5, -1.0)):
        N, rec, J = mc_run(256, rho, 2, 0.0, S=8, Teq=2048, T=4096, ms=[4], seed=1)
        C = corr(rec[0], N, [0, 1, 64, 1024])
        R = np.abs(C) / C[:, [0]].real
        c = -np.angle(C[:, 1] / C[:, 0]) / (2 * np.pi * 4 / 256)
        ok0 &= np.abs(R - 1).max() < 1e-9 and np.abs(c - cexp).max() < 1e-9
        msg0.append(f"rho={rho}: max|R-1| {np.abs(R - 1).max():.1e}, c={c.mean():+.6f}")
    rep("N", ok0, "[float] r=0, V=2, L=256 through the same simulator: " + "; ".join(msg0))

    # decay time versus k at L = 1024
    zl = []
    okz = True
    for V, rho in ((1, 0.25), (2, 0.5)):
        ms = [4, 8, 16, 32, 64]
        N, rec, J = mc_run(1024, rho, V, 0.25, S=32, Teq=20000, T=32768, ms=ms, seed=7 + V)
        taus = np.unique(np.round(np.logspace(0, np.log10(6000), 80)).astype(int))
        te = []
        for a, m in enumerate(ms):
            Cm = corr(rec[a], N, [0] + list(taus)).mean(0)
            rel = np.abs(Cm[1:]) / Cm[0].real
            i = int(np.argmax(rel < np.exp(-1)))
            y1, y2 = np.log(rel[i - 1]), np.log(rel[i])
            te.append(taus[i - 1] + (y1 + 1) / (y1 - y2) * (taus[i] - taus[i - 1]))
        z = -np.diff(np.log(te)) / np.diff(np.log(ms))
        okz &= bool(np.all((z > 1.2) & (z < 1.8)))
        zl.append(f"V={V} rho={rho}: tau_1/e {np.round(te, 1)}, local z {np.round(z, 2)}")
    rep("N", okz, "[float] L=1024, k = 2pi m/1024, m = 4..64: " + "; ".join(zl))

    # one small r
    N, rec, J = mc_run(512, 0.5, 2, 0.05, S=32, Teq=20000, T=16384, ms=[8], seed=3)
    R, E = ratio_jk(corr(rec[0], N, [0, 256, 2048]))
    rep("N", R[2] < 0.1, f"[float] V=2 rho=1/2 r=0.05 L=512 k0: R(256) = {R[1]:.3f}, R(2048) = {R[2]:.3f} +- {E[2]:.3f}  "
        f"({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    for tag, fn in (("Q", fam_Q), ("D", fam_D), ("E", fam_E), ("M", fam_M), ("N", fam_N)):
        if not ONLY or tag in ONLY:
            fn()
    print(f"total {time.time() - T0:.0f}s; failing families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + ",".join(sorted(set(FAILS))))
    else:
        print("SUMMARY: PROVED (A) r = 0: on every ring every orbit ends, after a finite transient, in rigid translation "
              "of the occupied set (+V per step if N(V+1) < L, -1 if N(V+1) > L, uniform gaps V if equal); (B) 0 < r < 1: "
              "every finite ring has one aperiodic closed class, so every disturbance decays; (C) mean field: signed "
              "weights for V >= 2, exact damping at 144 points, exact outside roots at 3; numerics: the fixed-k decay "
              "persists as L grows")
        print("HIT: records on a ring with speed contents, u = min(v+1, V, gap), slowed by one with probability r. At "
              "r = 0 a record that uses its full gap at a step t >= 1 keeps doing so and copies its leader's move one "
              "step late, so every orbit on every ring ends in rigid translation of the occupied set: +V per step below "
              "density 1/(V+1), a jam wave at -1 above; every density mode then keeps its modulus forever. At every "
              "0 < r < 1 each finite ring has one aperiodic closed class, so every disturbance decays; numerically the "
              "fixed-k decay persists as the ring grows. The mean-field linearization is not always damped (exact roots "
              "outside the unit circle, V = 2, r = 0, rho = 3/20).")

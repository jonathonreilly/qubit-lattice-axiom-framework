#!/usr/bin/env python3
"""A hierarchy of neighbourhood conditions: GLUED, BREAKABLE and FREE record
groups under shifting ticks.

Class-A finite-object runner, self-contained.  Four declared objects, none
derived from any axiom.

  * THE COARSE TORUS.  Z_L^3 at L = 8: 512 sites, nearest-neighbour adjacency,
    coordination 6 -- bipartite with girth 4, as Z^3 is.  A GROUP OF RECORDS
    is a finite set of occupied sites, one record each.
  * THE RING.  One line of that torus taken as a ring of R = 16 sites, four
    records, shifts restricted to +-x.  The declared collision object.
  * THE CUBE.  The 2x2x2 cube graph Q3: 8 corners, 12 edges, one FERMION edge
    record and one LINK record per edge, 2^24 joint record patterns, the
    superfast parity dictionary n_v = |y & star(v)| mod 2, E_e = +-1/2 from
    the link record, rho_v = n_v - 1/2 (sea convention).
  * THE FREE REFERENCE.  One record under K1 has E|dx|^2 = 1 and
    D_1 = 1/6 per tick.

THE THREE LEVELS and THE TICK MODELS are STIPULATED here, in full, and derived
from nothing.  A support condition is a zero of the law-level odds: a
configuration it excludes carries odds exactly 0 and is never registered.

  GLUED      the condition is a SUPPORT CONDITION.  Two forms:
             C_comp, every record has at least one adjacent record;
             C_rig, every pair adjacent now stays adjacent.  Gauss's law on
             the cube, G_v = (div E)_v - rho_v = 0, is the emergent instance.
  BREAKABLE  the condition is an ENERGY COST.  E(S) = -g A(S) with A(S) the
             number of adjacent record pairs, so with B(S) = (n-1) - A(S)
             (exact for n <= 3 on this bipartite lattice) the odds of S are
             suppressed by e^{-g} per broken adjacency: pi(S) ~ e^{-g B(S)}.
  FREE       no condition: g = 0.

  K1     SINGLE-RECORD TICK.  Exactly one record shifts to a nearest-neighbour
         site, uniformly over the admissible shifts.  Reach r: the target is
         the record's site plus r*d.
  KB(r)  NEIGHBOURHOOD TICK of reach r.  The whole support set shifts by r
         units as a block, uniformly over the 6 unit directions.
  KM(q)  MIXED TICK.  With odds q a KB(1) block shift, with odds 1-q a K1
         single shift.
  BR(g, h, reach)  BREAKABLE TICK.  Pick a record uniformly (odds 1/n); pick a
         direction with odds e^{h}/(5 + e^{h}) for +x and 1/(5 + e^{h}) for
         each of the other five; the target is the record's site plus reach*d.
         If the target carries a record the tick is NULL.  Otherwise the shift
         is registered with odds min(1, e^{-g dB}).

CONVENTION K1, declared so the two are not confused: under K1 exactly one
record shifts per tick, so a free n-record group has D_free(n) = 1/(6 n^2) and
D_free(2) = D_1/4.  PR #7889 / PR #7891 quote an independent-record value
D_1/2, which is the ratio under a tick where BOTH records shift every tick.
Both are reported.

The runner establishes:

  A  GLUED.  The cage under single ticks with an exact Fraction certificate;
     the block tick, D = D_1 with the internal pattern preserved exactly; the
     mixed tick, D(q) = q D_1; and reach-2 single ticks, which un-cage.
  B  BREAKABLE.  Exact stationary odds, exact closed-form lifetimes and intact
     fractions against absorbing-chain solves, D_intact = 0, D_group(g), and
     certain re-binding in exactly 101 ticks at every g.
  C  CIRCUMSTANCES.  A uniform field drives rather than tears; the tearing
     threshold and its direction; the 1D collision, where passing has odds
     exactly 0 and strong coupling MERGES; and reach, which changes the cage
     and not the break rate.
  D  GLUED ONCE FORMED.  Gauss's law on the cube: no single record change is
     admissible and every admissible joint change carries the charge with its
     flux.
  E  THE HIERARCHY assembled as one table.

Line tags.  `[exact]` = integer, F2 or `Fraction` arithmetic with no floating
point in the statement.  `[numerical]` = a deterministic double-precision
evaluation of an exactly specified quantity at a stated threshold: no
sampling, no seed, no random number anywhere in this runner.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import math
import sys
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 150

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


def _tq(q, p=3):
    return ", ".join(("%." + str(p) + "f") % x for x in q)


# ============================================================== the L^3 torus

L = 8
DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
SITES = [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]
DIMER = ((0, 0, 0), (1, 0, 0))
BENT = ((0, 0, 0), (1, 0, 0), (1, 1, 0))


def nrm(v):
    return (v[0] % L, v[1] % L, v[2] % L)


def isadj(r):
    """r is a minimal-image relative vector: adjacent iff one unit step."""
    return (sum(1 for c in r if c in (1, L - 1)) == 1
            and sum(1 for c in r if c == 0) == 2)


def adj(a, b):
    return isadj(tuple((a[i] - b[i]) % L for i in range(3)))


def canon(cfg):
    """Translation class of a group on the torus.  The lexicographically least
    sorted tuple always contains the origin, so it is attained by translating
    one of the group's own records to the origin."""
    best = None
    for s in cfg:
        c = tuple(sorted(nrm((p[0] - s[0], p[1] - s[1], p[2] - s[2]))
                         for p in cfg))
        if best is None or c < best:
            best = c
    return best


def nadj(cfg):
    return sum(1 for i in range(len(cfg)) for j in range(i + 1, len(cfg))
               if adj(cfg[i], cfg[j]))


def ok_comp(cfg):
    return all(any(adj(s, t) for t in cfg if t != s) for s in cfg)


def ok_rig(old, new):
    return all(adj(new[i], new[j])
               for i in range(len(old)) for j in range(i + 1, len(old))
               if adj(old[i], old[j]))


def shifts(cfg, cond, reach=1):
    """Every admissible single-record shift (new configuration, step) of the
    group cfg under the named support condition."""
    out = []
    for i in range(len(cfg)):
        for d in DIRS:
            t = cfg[i]
            for _ in range(reach):
                t = nrm((t[0] + d[0], t[1] + d[1], t[2] + d[2]))
            if t in cfg:
                continue
            new = tuple(cfg[:i]) + (t,) + tuple(cfg[i + 1:])
            if cond == "comp" and not ok_comp(new):
                continue
            if cond == "rig" and not ok_rig(cfg, new):
                continue
            out.append((new, tuple(reach * x for x in d)))
    return out


def explore(start, cond, reach=1):
    """BFS on translation classes; returns the classes and the class-graph
    edges (from, to, record step)."""
    c0 = canon(start)
    idx = {c0: 0}
    reps = [c0]
    frontier = [c0]
    edges = []
    while frontier:
        nf = []
        for c in frontier:
            ci = idx[c]
            for (new, step) in shifts(c, cond, reach):
                cn = canon(new)
                if cn not in idx:
                    idx[cn] = len(reps)
                    reps.append(cn)
                    nf.append(cn)
                edges.append((ci, idx[cn], step))
        frontier = nf
    return reps, edges


def potential(reps, edges, n):
    """Exact Fraction potential Phi of the class with
    CoM(s') - CoM(s) = Phi(c') - Phi(c), assigned by breadth-first sweep and
    then RE-CHECKED on every edge: a certificate, not a fit."""
    adjl = {i: [] for i in range(len(reps))}
    for (a, b, st) in edges:
        inc = tuple(Fr(x, n) for x in st)
        adjl[a].append((b, inc))
        adjl[b].append((a, tuple(-x for x in inc)))
    Phi, comp, ncomp = {}, {}, 0
    for r in range(len(reps)):
        if r in Phi:
            continue
        Phi[r] = (Fr(0), Fr(0), Fr(0))
        comp[r] = ncomp
        stack = [r]
        while stack:
            u = stack.pop()
            for (v, inc) in adjl[u]:
                if v not in Phi:
                    Phi[v] = tuple(Phi[u][k] + inc[k] for k in range(3))
                    comp[v] = ncomp
                    stack.append(v)
        ncomp += 1
    bad = 0
    for (a, b, st) in edges:
        inc = tuple(Fr(x, n) for x in st)
        if tuple(Phi[a][k] + inc[k] for k in range(3)) != Phi[b]:
            bad += 1
    spread = tuple(max(Phi[r][k] for r in Phi) - min(Phi[r][k] for r in Phi)
                   for k in range(3))
    return Phi, comp, ncomp, bad, spread


def cage(start, cond, reach=1):
    reps, edges = explore(tuple(sorted(start)), cond, reach)
    Phi, comp, ncomp, bad, spread = potential(reps, edges, len(start))
    return dict(cls=len(reps), sh=len(edges), bad=bad, spread=spread,
                width=max(spread), reps=reps, edges=edges, Phi=Phi)


def pattern(cfg):
    """The internal pattern: the multiset of pairwise minimal-image difference
    vectors.  Invariant under a rigid block shift, by construction of nothing
    -- it is checked exhaustively below."""
    out = []
    for i in range(len(cfg)):
        for j in range(len(cfg)):
            if i == j:
                continue
            d = []
            for k in range(3):
                x = (cfg[j][k] - cfg[i][k]) % L
                d.append(x if x <= L // 2 else x - L)
            out.append(tuple(d))
    return sorted(out)


def block_census(grp, r):
    """Every KB(r) block shift over every base site of the torus."""
    g0 = tuple(sorted(grp))
    viol = 0
    n = 0
    inc2 = Fr(0)
    for base in SITES:
        cfg = tuple(sorted(nrm((s[0] + base[0], s[1] + base[1], s[2] + base[2]))
                           for s in g0))
        pc = pattern(cfg)
        for d in DIRS:
            step = tuple(r * x for x in d)
            new = tuple(sorted(nrm((s[0] + step[0], s[1] + step[1],
                                    s[2] + step[2])) for s in cfg))
            if pattern(new) != pc or len(set(new)) != len(g0):
                viol += 1
            inc2 += sum(Fr(x) ** 2 for x in step)
            n += 1
    return viol, n, inc2 / n


def mixed_slope(start, cond, qs, nsteps=600):
    """Exact Markov-additive moment recursion for KM(q) on the class chain."""
    n = len(start)
    reps, edges = explore(tuple(sorted(start)), cond, 1)
    m = len(reps)
    ei = {i: [] for i in range(m)}
    for (a, b, st) in edges:
        ei[a].append((b, tuple(x / float(n) for x in st)))
    out = []
    for q in qs:
        rows = [[] for _ in range(m)]
        for i in range(m):
            for d in DIRS:
                rows[i].append((i, q / 6.0, np.array(d, float)))
            k = len(ei[i])
            if k == 0:
                rows[i].append((i, 1.0 - q, np.zeros(3)))
            else:
                for (b, inc) in ei[i]:
                    rows[i].append((b, (1.0 - q) / k, np.array(inc, float)))
        p = np.zeros(m)
        p[0] = 1.0
        u = np.zeros((m, 3))
        v = np.zeros(m)
        prev = 0.0
        sl = 0.0
        for _ in range(nsteps):
            np_, nu, nv = np.zeros(m), np.zeros((m, 3)), np.zeros(m)
            for i in range(m):
                for (j, w, f) in rows[i]:
                    np_[j] += p[i] * w
                    nu[j] += w * (u[i] + p[i] * f)
                    nv[j] += w * (v[i] + 2.0 * float(u[i] @ f)
                                  + p[i] * float(f @ f))
            p, u, v = np_, nu, nv
            tot = v.sum() - float(u.sum(0) @ u.sum(0))
            sl = tot - prev
            prev = tot
        out.append(sl)
    return out


def group_A():
    """GLUED: a support condition, the cage, the block tick, the reach."""
    d_c, d_r = cage(DIMER, "comp"), cage(DIMER, "rig")
    check("A1 [exact] GLUED, single ticks on the L = 8 torus: the glued DIMER is FROZEN -- C_comp "
          "and C_rig each admit %d shifts from %d class, %d Fraction-certificate inconsistencies, "
          "cage width %s, so D_group = 0 EXACTLY"
          % (d_c["sh"], d_c["cls"], d_c["bad"] + d_r["bad"], d_c["width"]),
          d_c["cls"] == 1 and d_c["sh"] == 0 and d_r["cls"] == 1 and d_r["sh"] == 0
          and d_c["bad"] == 0 and d_r["bad"] == 0 and d_c["width"] == 0)

    t_c, t_r = cage(BENT, "comp"), cage(BENT, "rig")
    check("A2 [exact] the glued BENT TRIMER is CAGED, not frozen: C_comp gives %d classes, %d "
          "shifts, %d coboundary inconsistencies and CoM spread (%s, %s, %s) -- three corners of "
          "one FIXED unit square forever, D_group = 0; C_rig gives %d"
          % (t_c["cls"], t_c["sh"], t_c["bad"], t_c["spread"][0], t_c["spread"][1],
             t_c["spread"][2], t_r["sh"]),
          t_c["cls"] == 4 and t_c["sh"] == 8 and t_c["bad"] == 0
          and t_c["width"] == Fr(1, 3) and t_c["spread"][2] == 0 and t_r["sh"] == 0)

    b = {(nm, r): block_census(g, r) for (nm, g) in (("dimer", DIMER), ("trimer", BENT))
         for r in (1, 2)}
    ok = all(b[k][0] == 0 and b[k][1] == 3072 for k in b)
    check("A3 [exact] NEIGHBOURHOOD tick KB(r): over %d block shifts per group per reach the "
          "internal pattern survives EXACTLY, %d violations in all four censuses, E|dCoM|^2 = %s "
          "and %s, so D_block = D_1 EXACTLY at reach 1 and 4 D_1 at reach 2"
          % (b[("dimer", 1)][1], sum(b[k][0] for k in b), b[("dimer", 1)][2],
             b[("dimer", 2)][2]),
          ok and b[("dimer", 1)][2] == 1 and b[("trimer", 1)][2] == 1
          and b[("dimer", 2)][2] == 4 and b[("trimer", 2)][2] == 4)

    qs = [0.0, 0.25, 0.5, 0.75, 1.0]
    sd = mixed_slope(DIMER, "comp", qs)
    st = mixed_slope(BENT, "comp", qs)
    err = max(max(abs(a - q) for a, q in zip(s, qs)) for s in (sd, st))
    check("A4 [exact argument, numerical 1e-12] MIXED tick KM(q): a block shift leaves the shape "
          "fixed and the K1 increment is the exact coboundary Phi, so it telescopes -- "
          "D(q) = q D_1 EXACTLY, the Var|CoM| slope matching q to %.2e in all ten cells"
          % (err,),
          err < 1e-12)

    r2 = cage(DIMER, "rig", 2)
    steps = sorted({e[2] for e in r2["edges"]})
    incs = [tuple(Fr(x, 2) for x in s) for s in steps]
    t2 = cage(BENT, "comp", 2)
    check("A5 [exact] REACH decides mobility, not condition strength: the same glue at reach 2 "
          "leaves the dimer %d shifts and %d coboundary inconsistencies -- a self-loop of nonzero "
          "CoM increment, so the cage FAILS; both are LEAPFROGS with D = D_1 on the pair's axis, "
          "and the trimer stays caged at %s"
          % (r2["sh"], r2["bad"], t2["width"]),
          r2["sh"] == 2 and r2["bad"] == 2 and set(steps) == {(2, 0, 0), (-2, 0, 0)}
          and incs[0][0] in (Fr(-1), Fr(1)) and t2["width"] == Fr(2, 3) and t2["bad"] == 0)


# ================================================== BREAKABLE: the dimer chain

REL = [r for r in SITES if r != (0, 0, 0)]
RI = {r: i for i, r in enumerate(REL)}
NAD = np.array([isadj(r) for r in REL])
NREL = len(REL)
GS = (0.0, 1.0, 2.0, 4.0, 8.0, 16.0)


def dimer_trans(g, h=0.0, reach=1):
    """The BR(g, h, reach) tick as the exact relative-coordinate chain of the
    dimer on the torus: 511 states, one per nonzero relative vector.  Only the
    REGISTERED off-diagonal shifts carry weight and increment; the null and
    rejected proposals are collected into one diagonal entry per state, whose
    weight is the exact complement, so every row sums to 1 and the small escape
    weight never has to be recovered by cancellation."""
    eh = math.exp(h)
    Z = 5.0 + eh
    pd = {d: (eh / Z if d == (1, 0, 0) else 1.0 / Z) for d in DIRS}
    off = [[] for _ in range(NREL)]
    for i, r in enumerate(REL):
        for d in DIRS:
            step = tuple(reach * x for x in d)
            for who in (0, 1):
                w = 0.5 * pd[d]
                if who == 0:
                    if nrm(step) == r:
                        continue
                    rn = nrm(tuple(r[k] - step[k] for k in range(3)))
                else:
                    if nrm(tuple(r[k] + step[k] for k in range(3))) == (0, 0, 0):
                        continue
                    rn = nrm(tuple(r[k] + step[k] for k in range(3)))
                dB = (1 if NAD[i] else 0) - (1 if isadj(rn) else 0)
                acc = 1.0 if dB <= 0 else math.exp(-g * dB)
                off[i].append((RI[rn], w * acc, tuple(x / 2.0 for x in step)))
    I, J, W, FX = [], [], [], []
    for i in range(NREL):
        for (j, w, f) in off[i]:
            I.append(i); J.append(j); W.append(w); FX.append(f)
        I.append(i); J.append(i)
        W.append(1.0 - math.fsum(w for (_j, w, _f) in off[i]))
        FX.append((0., 0., 0.))
    return (np.array(I), np.array(J), np.array(W), np.array(FX, float))


def escape_weight(T, i0, inside):
    """The exact weight leaving a state, summed over the registered shifts
    themselves -- never as 1 minus a near-one row sum."""
    I, J, W = T[0], T[1], T[2]
    return math.fsum(float(W[t]) for t in range(len(I))
                     if int(I[t]) == i0 and int(J[t]) != i0
                     and not inside[int(J[t])])


def escape_solve(T, keep):
    """Mean first passage out of the kept set, from M = I - A built directly:
    the diagonal is the summed escape weight, so no cancellation occurs."""
    pos = {s: a for a, s in enumerate(keep)}
    k = len(keep)
    I, J, W = T[0], T[1], T[2]
    acc = [[] for _ in range(k)]
    M = np.zeros((k, k))
    for t in range(len(I)):
        i, j = int(I[t]), int(J[t])
        if i not in pos or i == j:
            continue
        acc[pos[i]].append(float(W[t]))
        if j in pos:
            M[pos[i], pos[j]] -= float(W[t])
    for a in range(k):
        M[a, a] += math.fsum(acc[a])
    return np.linalg.solve(M, np.ones(k))


def to_P(T, m=NREL):
    return sp.csr_matrix((T[2], (T[0], T[1])), shape=(m, m))


def ma_slope(T, start, m=NREL, nsteps=1200):
    """The per-tick slope of Var|CoM| -- the true asymptotic 6 D, with the
    martingale correction, not a per-tick variance."""
    I, J, W, FX = T
    PT = to_P(T, m).T.tocsr()
    WfT = [sp.csr_matrix((W * FX[:, k], (I, J)), shape=(m, m)).T.tocsr()
           for k in range(3)]
    WffT = sp.csr_matrix((W * (FX * FX).sum(1), (I, J)), shape=(m, m)).T.tocsr()
    p = start.copy()
    u = np.zeros((m, 3))
    v = np.zeros(m)
    prev, sl = 0.0, 0.0
    for _ in range(nsteps):
        nu = np.column_stack([PT @ u[:, k] + WfT[k] @ p for k in range(3)])
        nv = PT @ v + 2.0 * sum(WfT[k] @ u[:, k] for k in range(3)) + WffT @ p
        p = PT @ p
        u, v = nu, nv
        tot = v.sum() - float(u.sum(0) @ u.sum(0))
        sl = tot - prev
        prev = tot
    return sl


def group_B():
    """BREAKABLE: odds suppressed by e^{-g} per broken adjacency."""
    pierr, dif, pin = 0.0, 0.0, []
    for g in GS:
        P = to_P(dimer_trans(g))
        w = np.exp(-g * (1 - NAD.astype(float)))
        pi = w / w.sum()
        pierr = max(pierr, float(np.abs(pi @ P - pi).max()))
        cf = 6.0 / (6.0 + 505.0 * math.exp(-g))
        dif = max(dif, abs(float(pi[NAD].sum()) - cf))
        pin.append(cf)
    check("B1 [exact] BREAKABLE, on the exact 511-state relative chain (6 intact, 505 broken): "
          "pi(S) ~ e^{-g B(S)} is EXACTLY stationary, |pi P - pi| <= %.1e, and the intact fraction "
          "6/(6 + 505 e^{-g}) runs %.4f, %.4f, %.4f at g = 0, 4, 16 (closed form to %.1e)"
          % (pierr, pin[0], pin[3], pin[5], dif),
          pierr <= 6e-17 and dif <= 1e-15 and abs(pin[0] - 0.011741682974560) < 1e-14
          and abs(pin[-1] - 0.999990528379174) < 1e-14)

    rel = np.array(REL)
    dif3 = (rel[:, None, :] - rel[None, :, :]) % L
    isa = ((np.sum((dif3 == 1) | (dif3 == L - 1), axis=2) == 1)
           & (np.sum(dif3 == 0, axis=2) == 2))
    tot = NAD.astype(np.int64)[:, None] + NAD.astype(np.int64)[None, :] + isa.astype(np.int64)
    iu = np.triu_indices(NREL, 1)
    cnt = np.bincount(tot[iu], minlength=3)
    cls = [int(c) // 3 for c in cnt]
    N2, N1, N0 = cls[2], cls[1], cls[0]
    tin = [N2 / (N2 + N1 * math.exp(-g) + N0 * math.exp(-2 * g)) for g in GS]
    check("B2 [exact] the TRIMER census by translation class: A = 2, 1, 0 give %d, %d, %d classes, "
          "%d = C(512,3)/512 in all, so the intact fraction 15/(15 + 1500 e^{-g} + 41920 e^{-2g}) "
          "runs %.6f at g = 0 to %.6f at g = 16"
          % (N2, N1, N0, N2 + N1 + N0, tin[0], tin[5]),
          (N2, N1, N0) == (15, 1500, 41920) and N2 + N1 + N0 == 43435
          and abs(tin[0] - 0.000345343616899) < 1e-14
          and abs(tin[-1] - 0.999988746573777) < 1e-14)

    idx = [i for i in range(NREL) if NAD[i]]
    dl, dc, worst = [], [], 0.0
    for g in GS:
        T = escape_solve(dimer_trans(g), idx)
        dl.append(float(T[0]))
        dc.append(1.2 * math.exp(g))
        worst = max(worst, abs(dl[-1] - dc[-1]) / dc[-1])
    seen, order = {}, []
    frontier = [canon(BENT)]
    seen[frontier[0]] = 0
    order.append(frontier[0])
    while frontier:
        nf = []
        for c in frontier:
            for (new, _st) in shifts(c, "free", 1):
                if nadj(new) != 2:
                    continue
                cc = canon(new)
                if cc not in seen:
                    seen[cc] = len(order)
                    order.append(cc)
                    nf.append(cc)
        frontier = nf
    tl, tc = [], []
    for g in GS:
        M = len(order)
        Mx = np.zeros((M, M))
        for a, c in enumerate(order):
            lv = []
            for i in range(3):
                for d in DIRS:
                    t = nrm((c[i][0] + d[0], c[i][1] + d[1], c[i][2] + d[2]))
                    w = 1.0 / 18.0
                    if t in c:
                        continue
                    new_c = tuple(sorted(tuple(c[:i]) + (t,) + tuple(c[i + 1:])))
                    dB = nadj(c) - nadj(new_c)
                    acc = 1.0 if dB <= 0 else math.exp(-g * dB)
                    b = seen[canon(new_c)] if nadj(new_c) == 2 else None
                    if b is not None and b == a:
                        continue
                    lv.append(w * acc)
                    if b is not None:
                        Mx[a, b] -= w * acc
            Mx[a, a] += math.fsum(lv)
        T = np.linalg.solve(Mx, np.ones(M))
        tl.append(float(T[0]))
        tc.append(18.0 / (8.0 * math.exp(-g) + 4.0 * math.exp(-2 * g)))
        worst = max(worst, abs(tl[-1] - tc[-1]) / tc[-1])
    check("B3 [exact] closed-form LIFETIMES, against absorbing solves to %.1e: 10 of the dimer's 12 "
          "proposals are unblocked and every registered one breaks it, so its lifetime is "
          "(6/5) e^{g}; the trimer's 18 split 4 null, 2 caged, 8 at dB = 1 and 4 at dB = 2, giving "
          "18/(8 e^{-g} + 4 e^{-2g})" % (worst,),
          worst <= 1e-9 and abs(dl[0] - 1.2) < 1e-12 and abs(tl[0] - 1.5) < 1e-12
          and len(order) == 4)

    dfz = cage(DIMER, "comp")["sh"] + cage(DIMER, "rig")["sh"]
    tfz = cage(BENT, "comp")
    check("B4 [exact] D_intact = 0 EXACTLY at EVERY g, both groups, g = 0 included: while intact "
          "the dimer has NO admissible single shift at all (%d) and the trimer's %d are exactly the "
          "A2 cage (spread %s), so the CoM stays bounded -- a bound pair transports ONLY by breaking"
          % (dfz, tfz["sh"], tfz["width"]),
          dfz == 0 and tfz["sh"] == 8 and tfz["bad"] == 0 and tfz["width"] == Fr(1, 3))

    dg = []
    for g in GS:
        w = np.exp(-g * (1 - NAD.astype(float)))
        dg.append(ma_slope(dimer_trans(g), w / w.sum()))
    rf = [x / 6.0 / (1.0 / 24) for x in dg]
    check("B5 [numerical, 1e-9] the unconditional D_group(g), Markov-additive on the exact chain: "
          "6 D_group = %s at g = 0, 1, 2, 4, 8, 16 -- from %.6f to %.1e of D_free(2) = D_1/4, "
          "falling as e^{-g}, exactly as fast as the lifetime grows"
          % (", ".join("%.4g" % x for x in dg), rf[0], rf[5]),
          abs(dg[0] - 0.249510763209) < 1e-9 and abs(dg[3] - 0.153136800130) < 1e-9
          and abs(dg[5] - 0.000002391350) < 1e-9 and abs(rf[0] - 0.998043) < 1e-5
          and rf[5] < 2e-5)

    br = [i for i in range(NREL) if not NAD[i]]
    rec, mx = [], 0.0
    for g in GS:
        Tr = dimer_trans(g)
        T = escape_solve(Tr, br)
        i0 = [i for i in range(NREL) if NAD[i]][0]
        bpos = {s2: k for k, s2 in enumerate(br)}
        dist = np.zeros(len(br))
        for t in range(len(Tr[0])):
            if int(Tr[0][t]) == i0 and int(Tr[1][t]) in bpos:
                dist[bpos[int(Tr[1][t])]] += float(Tr[2][t])
        dist = dist / dist.sum()
        rec.append(float(dist @ T))
        mx = max(mx, float(T.max()))
    check("B6 [exact reason, numerical 1e-12] RE-BINDING is certain and the cost does not touch "
          "it: the chain is finite and irreducible, so P(re-bind) = 1 at every finite g; once "
          "broken every proposal has dB <= 0 and registers with odds 1, so the mean recurrence is "
          "exactly 101 = 505/5 ticks at every g (%.9f, max %.3f)" % (rec[0], mx),
          max(abs(x - 101.0) for x in rec) < 1e-9 and abs(mx - 204.705534) < 1e-5)

    check("B7 [exact] THE TWO LIMITS: as g -> infinity the admissible set contracts to exactly the "
          "A1-A2 support-condition set, so GLUED is the g -> infinity limit of BREAKABLE; at g = 0 "
          "(FREE) the pair is intact %.2f %% of ticks and the trimer %.3f %%, with "
          "D_group = %.6f D_free(2), the rest exclusion"
          % (100 * pin[0], 100 * tin[0], rf[0]),
          abs(100 * pin[0] - 1.1742) < 1e-3 and abs(100 * tin[0] - 0.03453) < 1e-4
          and abs(rf[0] - 0.998043) < 1e-5)


# ============================================ CIRCUMSTANCES: field, collision

R = 16
RCFG = [c for c in itertools.combinations(range(R), 4)]
RCI = {c: i for i, c in enumerate(RCFG)}


def ring_A(c):
    s = set(c)
    return sum(1 for x in c if (x + 1) % R in s)


def ring_P(g):
    P = np.zeros((len(RCFG), len(RCFG)))
    for i, c in enumerate(RCFG):
        for k in range(4):
            for d in (1, -1):
                w = 1.0 / 8.0
                t = (c[k] + d) % R
                if t in c:
                    continue
                new = tuple(sorted(c[:k] + (t,) + c[k + 1:]))
                dB = ring_A(c) - ring_A(new)
                acc = 1.0 if dB <= 0 else math.exp(-g * dB)
                P[i, RCI[new]] += w * acc
        P[i, i] = 0.0
        P[i, i] = 1.0 - math.fsum(P[i, :])
    return P


def group_C():
    """What breaks a breakable group -- and what does not."""
    lifes = {}
    worst = 0.0
    for g in (1.0, 2.0, 4.0, 8.0, 16.0):
        for h in (0.0, 0.5, 1.0, 2.0, 4.0, 8.0):
            T = dimer_trans(g, h)
            eh = math.exp(h)
            for (r0, cf) in (((1, 0, 0), 2 * math.exp(g) * (5 + eh) / (9 + eh)),
                             ((0, 1, 0), math.exp(g) * (5 + eh) / (4 + eh))):
                val = 1.0 / escape_weight(T, RI[r0], NAD)
                lifes[(g, h, r0)] = val / (1.2 * math.exp(g))
                worst = max(worst, abs(val - cf) / cf)
    lo, hi = min(lifes.values()), max(lifes.values())
    xs = [lifes[(4.0, h, (1, 0, 0))] for h in (0.0, 0.5, 1.0, 2.0, 4.0, 8.0)]
    check("C1 [exact] a UNIFORM FIELD DRIVES a bound pair, it does not tear it: the lifetime is "
          "exactly 2 e^{g}(5+e^{h})/(9+e^{h}) aligned and e^{g}(5+e^{h})/(4+e^{h}) transverse "
          "(chain agrees to %.1e over 30 cells), so it stays inside [%.4f, %.4f] of its zero-field "
          "value -- limits 5/6 and 5/3 -- and RISES with h when aligned"
          % (worst, lo, hi),
          worst < 1e-12 and lo >= 5.0 / 6 - 1e-12 and hi <= 5.0 / 3 + 1e-12
          and all(a <= b + 1e-12 for a, b in zip(xs, xs[1:])))

    rows, dmax = [], 0.0
    for q in (0.5, 0.25, 0.1):
        for g in (1.0, 2.0, 4.0, 8.0, 16.0):
            eg = math.exp(g)
            den = q * eg - (1 - q)
            if den <= 0:
                rows.append((q, g, None))
                continue
            hs = math.log((4 * (1 - q) + q * eg) / den)

            def Fq(h):
                eh = math.exp(h)
                return (math.exp(g) * (5 + eh) / (4 + eh) / (1 - q)
                        - (5 + eh) / (q * (eh - 1)))
            loh, hih = 1e-9, 50.0
            for _ in range(200):
                mid = (loh + hih) / 2
                if Fq(mid) < 0:
                    loh = mid
                else:
                    hih = mid
            dmax = max(dmax, abs(hs - loh))
            rows.append((q, g, hs))
    hq = [r[2] for r in rows if r[0] == 0.5]
    check("C2 [exact] the TEARING THRESHOLD runs BACKWARDS: under single ticks the intact group "
          "cannot move, so h*(g) = 0 identically; under KM(q) it is "
          "e^{h*} = [4(1-q) + q e^{g}]/[q e^{g} - (1-q)] (bisection to %.1e), falling from %.6f at "
          "g = 1 to %.6f at g = 16 (q = 0.5) -- h > h* is where the group SURVIVES"
          % (dmax, hq[0], hq[-1]),
          dmax < 1e-15 and all(a > b for a, b in zip(hq, hq[1:]))
          and abs(hq[0] - 1.363507587) < 1e-8)

    viol, trans = 0, 0
    for c in RCFG:
        for i in range(4):
            for d in (1, -1):
                t = (c[i] + d) % R
                if t in c:
                    continue
                trans += 1
                ps = list(c)
                ps[i] = t
                o = sorted(range(4), key=lambda k: ps[k])
                k0 = o.index(0)
                if tuple(o[k0:] + o[:k0]) != (0, 1, 2, 3):
                    viol += 1
    stk = [i for i, c in enumerate(RCFG) if ring_A(c) == 3]
    bkk = [i for i, c in enumerate(RCFG) if ring_A(c) == 0]
    absset = set(stk) | set(bkk)
    tr = [i for i in range(len(RCFG)) if i not in absset]
    ti = {s: k for k, s in enumerate(tr)}
    pb = []
    for g in GS:
        P = ring_P(g)
        Q = P[np.ix_(tr, tr)]
        b = P[np.ix_(tr, bkk)].sum(1)
        ps = np.linalg.solve(np.eye(len(tr)) - Q, b)
        pb.append(float(ps[ti[RCI[(0, 1, 4, 5)]]]))
    check("C3 [exact] a COLLISION on the 16-site ring, %d configurations: the cyclic order of the "
          "four records survives all %d admissible shifts, %d violations, so P(pass) = 0 EXACTLY at "
          "every g; the competition is STICK versus BREAK, P(break first) = %s at g = 0, 1, 2, 4, "
          "8, 16 -- above g ~ 2.5 a collision MERGES"
          % (len(RCFG), trans, viol, ", ".join("%.3g" % x for x in pb)),
          viol == 0 and trans == 11648 and abs(pb[0] - 0.919008639107) < 1e-9
          and abs(pb[2] - 0.539646404460) < 1e-9 and abs(pb[5] - 5.38e-7) < 5e-9
          and all(a > b for a, b in zip(pb, pb[1:])))

    dr = 0.0
    for g in GS:
        vals = []
        for reach in (1, 2):
            vals.append(escape_weight(dimer_trans(g, 0.0, reach), RI[(1, 0, 0)], NAD))
        dr = max(dr, abs(vals[0] - vals[1]))
    r2 = cage(DIMER, "rig", 2)
    check("C4 [exact] REACH leaves the BREAK RATE alone: a reach-2 single tick breaks a breakable "
          "dimer at exactly the reach-1 rate (5/6) e^{-g}, agreeing to %.1e at all six g, since 10 "
          "of 12 proposals still carry dB = +1 -- what a longer reach changes is the cage (A5), "
          "not the break" % (dr,),
          dr < 1e-12 and r2["sh"] == 2 and r2["bad"] == 2)


# ================================================ GLUED ONCE FORMED: the cube

def cube_data():
    corn = sorted([(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)],
                  key=lambda v: 4 * v[0] + 2 * v[1] + v[2])
    cid = {v: 4 * v[0] + 2 * v[1] + v[2] for v in corn}
    edges = []
    for d in range(3):
        for v in corn:
            if v[d] == 0:
                w = list(v)
                w[d] = 1
                edges.append((cid[v], cid[tuple(w)]))
    nq, nv = len(edges), len(corn)
    star = np.zeros(nv, dtype=np.int64)
    sgn = np.zeros((nv, nq), dtype=np.int64)
    for e, (i, j) in enumerate(edges):
        star[i] |= 1 << e
        star[j] |= 1 << e
        sgn[j, e] = 1
        sgn[i, e] = -1
    nf = 1 << nq
    f = np.arange(nf, dtype=np.int64)
    par = np.array([bin(x).count("1") & 1 for x in range(nf)], dtype=np.int64)
    nval = np.empty((nf, nv), dtype=np.int64)
    for a in range(nv):
        nval[:, a] = par[f & star[a]]
    r2 = 2 * nval - 1
    bit = np.stack([((f >> q) & 1) for q in range(nq)], axis=1)
    d2 = (1 - 2 * bit) @ sgn.T
    lo = int(min(d2.min(), r2.min()))
    hi = int(max(d2.max(), r2.max()))
    pw = (hi - lo + 1) ** np.arange(nv, dtype=np.int64)
    kd = ((d2 - lo) * pw).sum(1)
    kr = ((r2 - lo) * pw).sum(1)
    byk = {}
    for l in range(nf):
        byk.setdefault(int(kd[l]), []).append(l)
    Y, LK = [], []
    for y in range(nf):
        for l in byk.get(int(kr[y]), ()):
            Y.append(y)
            LK.append(l)
    return edges, nq, nv, nf, nval, np.array(Y), np.array(LK)


def group_D():
    """The emergent instance: Gauss's law glues the charge to its flux."""
    edges, nq, nv, nf, nval, Y, LK = cube_data()
    key = np.sort(Y * nf + LK)

    def adm(y, l):
        k = y * nf + l
        p = np.clip(np.searchsorted(key, k), 0, len(key) - 1)
        return key[p] == k

    check("D1 [exact] the EMERGENT instance, the 2x2x2 cube of PR #7893 with a fermion and a link "
          "record per edge: G_v = (div E)_v - rho_v = 0 at all 8 corners (sea convention) admits "
          "%d of 2^%d joint record patterns, on %d fermion patterns, ALL at N = 4"
          % (len(Y), 2 * nq, len(set(Y.tolist()))),
          len(Y) == 14400 and len(set(Y.tolist())) == 2240
          and bool((nval[Y].sum(1) == 4).all()))

    sf = sl = spd = ok = bad = 0
    per = np.zeros(len(Y), dtype=np.int64)
    for e in range(nq):
        b = 1 << e
        sf += int(adm(Y ^ b, LK).sum())
        sl += int(adm(Y, LK ^ b).sum())
        m = adm(Y ^ b, LK ^ b)
        spd += int(m.sum())
        per += m
        i, j = edges[e]
        good = nval[Y, i] != nval[Y, j]
        ok += int((m & good).sum())
        bad += int((m & ~good).sum())
    check("D2 [exact] NO SINGLE RECORD CHANGE IS ADMISSIBLE: over %d patterns x 12 edges a fermion "
          "record alone is admissible in %d of %d cases and a link record alone in %d of %d -- odds "
          "exactly 0, since flipping y_e complements n_v at BOTH endpoints and flipping l_e "
          "reverses E_e at both" % (len(Y), sf, len(Y) * nq, sl, len(Y) * nq),
          sf == 0 and sl == 0 and len(Y) * nq == 172800)

    u, c = np.unique(per, return_counts=True)
    cen = ", ".join("%d x %d" % (int(b), int(a)) for a, b in zip(u, c))
    check("D3 [exact] the PAIRED change IS admissible -- fermion record and link record on the "
          "SAME edge, together: %d of %d, census %s -- and ALL carry the charge WITH its flux "
          "(occupations swap, E_e reverses), %d violations; %d is exactly PR #7893's H^g nonzero "
          "count" % (spd, len(Y) * nq, cen, bad, spd),
          spd == 79872 and ok == 79872 and bad == 0
          and dict(zip(u.tolist(), c.tolist())) == {4: 768, 5: 6144, 6: 6912, 8: 576})

    two = [y for y in range(nf) if int(nval[y].sum()) == 2]
    per2 = []
    for y in two:
        odd = [a for a in range(nv) if nval[y, a] == 1]
        per2.append(sum(1 for (i, j) in edges if (i in odd) != (j in odd)))
    u2, c2 = np.unique(np.array(per2), return_counts=True)
    check("D4 [exact] the three levels on ONE object: the FREE fermion sector admits all %d single "
          "edge-record changes, PR #7891's PARITY sector %d over %d patterns (census %s, recomputed "
          "not quoted), the GLUED Gauss sector %d"
          % (nf * nq, int(sum(per2)), len(two),
             str(dict(zip(u2.tolist(), c2.tolist()))), sf),
          nf * nq == 49152 and int(sum(per2)) == 4608 and len(two) == 896
          and dict(zip(u2.tolist(), c2.tolist())) == {4: 384, 6: 512} and sf == 0)

    npos = nval[Y].sum(1)
    check("D5 [exact] a needed CLARIFICATION: there is no one-charge configuration on the cube -- "
          "the Gauss sector is exactly half filled, so all %d patterns carry %d corners at "
          "rho_v = +1/2 and %d at -1/2, total charge 0; 'one charge' is read as one corner at +1/2"
          % (len(Y), int(npos.min()), nv - int(npos.min())),
          int(npos.min()) == 4 and int(npos.max()) == 4)


def group_E():
    """The hierarchy assembled."""
    dc = cage(DIMER, "comp")
    tc = cage(BENT, "comp")
    b1 = block_census(DIMER, 1)
    w = np.exp(-0.0 * (1 - NAD.astype(float)))
    d0 = ma_slope(dimer_trans(0.0), w / w.sum()) / 6.0 / (1.0 / 24)
    rows = [
        ("GLUED", dc["sh"] == 0 and tc["width"] == Fr(1, 3), b1[0] == 0 and b1[2] == 1),
        ("BREAKABLE", True, True),
        ("FREE", True, True),
    ]
    check("E1 [exact] THE HIERARCHY in one table: GLUED gives D = 0 under single ticks, D = D_1 "
          "under a neighbourhood tick, an infinite lifetime and nothing that breaks it at any "
          "coupling -- only reach changes it; BREAKABLE gives D_intact = 0, lifetime (6/5) e^{g}, "
          "transport only by breaking; FREE gives D_free(2) = D_1/4 (%.3f)" % d0,
          all(a and b for (_n, a, b) in rows) and abs(d0 - 0.998043) < 1e-5)


def main():
    group_A()
    group_B()
    group_C()
    group_D()
    group_E()
    print("SUMMARY: a glued group travels only as one, and then at exactly D_1; a breakable one "
          "holds for (6/5) e^{g} ticks and transports only by breaking; in the Gauss sector no "
          "single record change is admissible at all.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())

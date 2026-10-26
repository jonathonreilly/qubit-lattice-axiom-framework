#!/usr/bin/env python3
"""
J:derive:review-20260929-wall-formation-and-clock-selection:a1
Record-scattering identity (wall T17) -- the same observables (N, P, L, energy current J)
on the two lane-supplied classical record gases ("original clause" O and the
angular-momentum-repaired clause V*), plus one third comparator S (synchronous
collide-then-stream) that the sources did not test.

Everything below is written from scratch (own event generators, own class enumeration,
own exact linear algebra with fractions.Fraction); it shares no code with the source
scripts.  All finite claims are exact (integers / Fractions).  numpy/scipy are used
only for strongly-connected-component bookkeeping on integer graphs.

Models (all are LANE-SUPPLIED classical comparators, not axiom content):
  config  = set of occupied sites, each with a content in the axis unit vectors (a direction)
  N = #records,  P = sum of contents,  L = sum position x content,  energy of a record = 1
  J(c) = sum over records whose target site is EMPTY of the content (instantaneous
         energy/mass current of asynchronous streaming)   -- the rate-1 streaming clause
  O   : a record at s with content k tries s -> s+k.  empty target: move.  same content:
        nothing.  other content: the two contents are exchanged (pass-through).
  V*  : as O but a PERPENDICULAR occupied target blocks (nothing happens); only an
        antiparallel target exchanges.  (Plus the same plaquette class events.)
  class events: on every 2x2 plaquette, any reassignment of contents of the occupied
        sites with the same (P, L) (rate gamma each).
  S   : synchronous tick = (collide) reassign contents within the (P,L) class so the
        targets r_i + c_i are pairwise distinct, then (stream) every record moves.
"""
import itertools
import random
import sys
import time
from collections import defaultdict
from fractions import Fraction

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

T0 = time.time()
RESULTS = []


def chk(name, cond, detail=""):
    ok = bool(cond)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)
    return ok


# ----------------------------------------------------------------------------------
# geometry helpers
# ----------------------------------------------------------------------------------
E2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
OPP2 = {0: 1, 1: 0, 2: 3, 3: 2}
E3 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def cr2(p, c):
    return p[0] * c[1] - p[1] * c[0]


def cr3(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


# ==================================================================================
# A.  Two-record events that keep P and L: exact criterion (all lattice displacements)
# ==================================================================================
def part_A():
    bad = 0
    nontrivial_dirs = set()
    total = 0
    for d in itertools.product(range(-3, 4), repeat=3):
        if d == (0, 0, 0):
            continue
        r1, r2 = d, (0, 0, 0)
        has_event = False
        for a in E3:
            for b in E3:
                for u in E3:
                    for v in E3:
                        total += 1
                        brute = (add(u, v) == add(a, b)) and (
                            add(cr3(r1, u), cr3(r2, v)) == add(cr3(r1, a), cr3(r2, b)))
                        du = sub(u, a)
                        crit = (add(u, v) == add(a, b)) and (cr3(du, d) == (0, 0, 0))
                        if brute != crit:
                            bad += 1
                        if brute and (u, v) != (a, b):
                            has_event = True
        nz = [abs(x) for x in d if x]
        shape = "axis" if len(nz) == 1 else ("facediag" if (len(nz) == 2 and nz[0] == nz[1]) else "other")
        if has_event:
            nontrivial_dirs.add(shape)
        else:
            nontrivial_dirs.add("none:" + shape)
    chk("A1 pair rule: (u,v) keeps P and L  <=>  u+v=a+b and (u-a) parallel to r1-r2",
        bad == 0, f"{total} (displacement, a,b,u,v) tuples compared, {bad} mismatches")
    expect = {"axis", "facediag", "none:other"}
    chk("A2 nontrivial two-record events exist exactly for axis and face-diagonal displacements "
        "(never body-diagonal or knight-type), |d_i|<=3",
        nontrivial_dirs == expect, f"shape classes seen: {sorted(nontrivial_dirs)}")


# ==================================================================================
# B.  Cluster census replication (independent code): which configurations a
#     (P,L)-preserving event can move
# ==================================================================================
def census(sites, contents, dim):
    n = len(sites)
    cfgs = list(itertools.product(range(len(contents)), repeat=n))
    idx = {c: i for i, c in enumerate(cfgs)}

    def pad(v):
        return tuple(v) + (0,) * (3 - len(v))

    def inv(c):
        P = (0, 0, 0)
        L = (0, 0, 0)
        for s, k in zip(sites, c):
            ck = pad(contents[k])
            P = add(P, ck)
            L = add(L, cr3(pad(s), ck))
        return P, L

    classes = defaultdict(list)
    for c in cfgs:
        classes[inv(c)].append(idx[c])

    def uf_new():
        return list(range(len(cfgs)))

    def find(p, a):
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a

    ufs = {"bond": uf_new(), "pair": uf_new(), "full": uf_new()}
    for mem in classes.values():
        for m in mem[1:]:
            ra, rb = find(ufs["full"], mem[0]), find(ufs["full"], m)
            if ra != rb:
                ufs["full"][ra] = rb
    for c in cfgs:
        for i in range(n):
            for j in range(i + 1, n):
                d2 = sum((x - y) ** 2 for x, y in zip(sites[i], sites[j]))
                fams = ["bond", "pair"] if d2 == 1 else (["pair"] if d2 == 2 else [])
                if not fams:
                    continue
                a, b = pad(contents[c[i]]), pad(contents[c[j]])
                Pab = add(a, b)
                Lab = add(cr3(pad(sites[i]), a), cr3(pad(sites[j]), b))
                for u in range(len(contents)):
                    for v in range(len(contents)):
                        uu, vv = pad(contents[u]), pad(contents[v])
                        if add(uu, vv) == Pab and add(cr3(pad(sites[i]), uu), cr3(pad(sites[j]), vv)) == Lab:
                            nc = list(c)
                            nc[i], nc[j] = u, v
                            for f in fams:
                                ra, rb = find(ufs[f], idx[c]), find(ufs[f], idx[tuple(nc)])
                                if ra != rb:
                                    ufs[f][ra] = rb
    out = {}
    for f in ("bond", "pair", "full"):
        comp = defaultdict(int)
        for k in range(len(cfgs)):
            comp[find(ufs[f], k)] += 1
        out[f] = sum(s for s in comp.values() if s > 1)
    return len(cfgs), out


def part_B():
    cases = [
        ("bond pair, 3D contents", [(0, 0, 0), (1, 0, 0)], E3, (36, 2, 2, 2)),
        ("face-diagonal pair, 3D contents", [(0, 0, 0), (1, 1, 0)], E3, (36, 0, 8, 8)),
        ("body-diagonal pair, 3D contents", [(0, 0, 0), (1, 1, 1)], E3, (36, 0, 0, 0)),
        ("2x2 plaquette, 4 records, 2D contents", [(0, 0), (1, 0), (0, 1), (1, 1)], E2, (256, 120, 220, 228)),
        ("2x2 plaquette, 4 records, 3D contents", [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0)], E3,
         (1296, 280, 636, 758)),
    ]
    for name, sites, contents, expect in cases:
        n, res = census(sites, contents, len(sites[0]))
        got = (n, res["bond"], res["pair"], res["full"])
        chk("B " + name + ": configs moved by bond / pair(<=sqrt2) / whole-class events",
            got == expect, f"got (configs, bond, pair, full) = {got}; REPLICATION of an old number, not new")


# ==================================================================================
# C.  Event ledger on the excluded state space, same observables on both models
# ==================================================================================
def make_torus(Lx):
    def sid(x, y):
        return (x % Lx) + Lx * (y % Lx)

    def xy(s):
        return s % Lx, s // Lx

    return sid, xy


_cls_cache = {}


def class_moves2(loc, ks):
    key = (tuple(loc), ks)
    if key in _cls_cache:
        return _cls_cache[key]
    Pt = (sum(E2[k][0] for k in ks), sum(E2[k][1] for k in ks))
    Lt = sum(cr2(p, E2[k]) for p, k in zip(loc, ks))
    out = []
    for cand in itertools.product(range(4), repeat=len(ks)):
        if cand == ks:
            continue
        P2 = (sum(E2[k][0] for k in cand), sum(E2[k][1] for k in cand))
        L2 = sum(cr2(p, E2[k]) for p, k in zip(loc, cand))
        if P2 == Pt and L2 == Lt:
            out.append(cand)
    _cls_cache[key] = out
    return out


def events_for(state, Lx, model):
    """state: tuple length Lx*Lx, entries -1 (empty) or content index 0..3.
    returns list of (new_state, changes, kind); changes = [(relpos, before, after)], before/after -1 or content."""
    sid, xy = make_torus(Lx)
    V = Lx * Lx
    ev = []
    for s in range(V):
        k = state[s]
        if k < 0:
            continue
        x, y = xy(s)
        t = sid(x + E2[k][0], y + E2[k][1])
        kt = state[t]
        if kt < 0:
            ns = list(state)
            ns[s] = -1
            ns[t] = k
            ev.append((tuple(ns), [((0, 0), k, -1), (E2[k], -1, k)], "move"))
        elif kt != k:
            if model in ("O_note", "O_class") or kt == OPP2[k]:
                ns = list(state)
                ns[s], ns[t] = kt, k
                ev.append((tuple(ns), [((0, 0), k, kt), (E2[k], kt, k)], "exch_" + ("par" if kt == OPP2[k] else "perp")))
    if model == "O_note":
        # bond clause (C) of the 2026-09-20 note: an opposite pair is redrawn uniformly on opposite
        # pairs (the other axis), any other pair is exchanged (the exchange is the nontrivial redraw)
        for s in range(V):
            x, y = xy(s)
            for e, kk in (((1, 0), 0), ((0, 1), 2)):
                t = sid(x + e[0], y + e[1])
                a, b = state[s], state[t]
                if a < 0 or b < 0:
                    continue
                if b == OPP2[a]:
                    for ax in (0, 2):
                        for (u, v) in ((ax, ax + 1), (ax + 1, ax)):
                            if (u, v) != (a, b):
                                ns = list(state)
                                ns[s], ns[t] = u, v
                                ev.append((tuple(ns), [((0, 0), a, u), (e, b, v)], "redraw"))
                elif a != b:
                    ns = list(state)
                    ns[s], ns[t] = b, a
                    ev.append((tuple(ns), [((0, 0), a, b), (e, b, a)], "bond_exch"))
    else:
        loc = [(0, 0), (1, 0), (0, 1), (1, 1)]
        for y in range(Lx):
            for x in range(Lx):
                sites = [sid(x, y), sid(x + 1, y), sid(x, y + 1), sid(x + 1, y + 1)]
                occ = [i for i in range(4) if state[sites[i]] >= 0]
                if len(occ) < 2:
                    continue
                ks = tuple(state[sites[i]] for i in occ)
                for cand in class_moves2([loc[i] for i in occ], ks):
                    ns = list(state)
                    ch = []
                    for i, kk in zip(occ, cand):
                        ch.append((loc[i], state[sites[i]], kk))
                        ns[sites[i]] = kk
                    ev.append((tuple(ns), ch, "class"))
    return ev


def ledger(changes):
    dN = dPx = dPy = dL = 0
    for rel, b, a in changes:
        if b >= 0:
            dN -= 1
            dPx -= E2[b][0]
            dPy -= E2[b][1]
            dL -= cr2(rel, E2[b])
        if a >= 0:
            dN += 1
            dPx += E2[a][0]
            dPy += E2[a][1]
            dL += cr2(rel, E2[a])
    return dN, (dPx, dPy), dL


def J_of(state, Lx):
    sid, xy = make_torus(Lx)
    jx = jy = 0
    for s, k in enumerate(state):
        if k < 0:
            continue
        x, y = xy(s)
        if state[sid(x + E2[k][0], y + E2[k][1])] < 0:
            jx += E2[k][0]
            jy += E2[k][1]
    return jx, jy


def P_of(state):
    return (sum(E2[k][0] for k in state if k >= 0), sum(E2[k][1] for k in state if k >= 0))


def part_C():
    for N in (2, 3):
        Lx = 5 if N == 2 else 4
        V = Lx * Lx
        tally = {m: defaultdict(int) for m in ("O_note", "O_class", "Vstar")}
        Jne = 0
        Jne_by_model_same = True
        nconf = 0
        t0 = time.time()
        for occ in itertools.combinations(range(V), N):
            for ks in itertools.product(range(4), repeat=N):
                st = [-1] * V
                for s, k in zip(occ, ks):
                    st[s] = k
                st = tuple(st)
                nconf += 1
                if J_of(st, Lx) != P_of(st):
                    Jne += 1
                for m in tally:
                    for ns, ch, kind in events_for(st, Lx, m):
                        dN, dP, dL = ledger(ch)
                        T = tally[m]
                        T["events"] += 1
                        if dN != 0:
                            T["dN!=0"] += 1
                        if dP != (0, 0):
                            T["dP!=0"] += 1
                        if dL != 0:
                            T["dL!=0"] += 1
                            T["dL!=0:" + kind] += 1
        for m, T in tally.items():
            print(f"     info C N={N} {m}: events={T['events']} dN!=0:{T['dN!=0']} dP!=0:{T['dP!=0']} dL!=0:{T['dL!=0']} "
                  + " ".join(f"{k}={v}" for k, v in sorted(T.items()) if k.startswith('dL!=0:')), flush=True)
        chk(f"C{N}a N and P are kept by every event of all three models on the {Lx}x{Lx} torus, N={N} "
            f"({nconf} configurations, exhaustive)",
            all(T["dN!=0"] == 0 and T["dP!=0"] == 0 for T in tally.values()))
        chk(f"C{N}b L is kept by every event of V* and violated by O (exchange of perpendicular contents), N={N}",
            tally["Vstar"]["dL!=0"] == 0 and tally["O_class"]["dL!=0"] > 0 and tally["O_note"]["dL!=0"] > 0,
            f"dL!=0 events: Vstar {tally['Vstar']['dL!=0']}, O_class {tally['O_class']['dL!=0']}, O_note {tally['O_note']['dL!=0']}")
        if N == 2:
            # closed form: ordered adjacent pairs 4V, perpendicular partner contents 2
            chk("C2c O's L-violating streaming exchanges at N=2: count = 4V*2*(contents of the mover fixed)=200 "
                "(plus class events none)",
                tally["O_class"]["dL!=0:exch_perp"] == 4 * V * 2,
                f"{tally['O_class']['dL!=0:exch_perp']} vs {4*V*2}")
            chk("C2d configurations with J != P (target occupied for an unbalanced set of records), N=2: 12*V=300, "
                "a property of the configuration only -- identical for O, O_note, V*",
                Jne == 12 * V, f"{Jne} vs {12*V}")
        else:
            print(f"     info C3: configurations with J != P: {Jne} of {nconf} (same set for every model by construction)")
            chk("C3c J != P on a nonempty proper subset of configurations for N=3 and the set does not depend on the "
                "scattering events", 0 < Jne < nconf, f"{Jne}/{nconf}")
        print(f"     info C N={N} time {time.time()-t0:.1f}s", flush=True)


# ==================================================================================
# D.  Exact stationary measures and exact mean energy current (4x4 torus, N=2)
# ==================================================================================
def build_chain(Lx, N, model, gamma, with_class=True):
    V = Lx * Lx
    states = []
    for occ in itertools.combinations(range(V), N):
        for ks in itertools.product(range(4), repeat=N):
            st = [-1] * V
            for s, k in zip(occ, ks):
                st[s] = k
            states.append(tuple(st))
    idx = {s: i for i, s in enumerate(states)}
    edges = defaultdict(Fraction)  # (src, dst) -> rate
    stream_edges = defaultdict(Fraction)
    for st in states:
        i = idx[st]
        for ns, ch, kind in events_for(st, Lx, model):
            j = idx[ns]
            if kind == "class":
                if with_class:
                    edges[(i, j)] += gamma
            else:
                edges[(i, j)] += 1
                stream_edges[(i, j)] += 1
    return states, idx, edges, stream_edges


def closed_classes(n, edges):
    rows = [b for (a, b) in edges]
    cols = [a for (a, b) in edges]
    A = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n)).tocsr()
    nc, lab = connected_components(A, directed=True, connection="strong")
    out_comp = np.zeros(nc, dtype=int)
    for (a, b) in edges:
        if lab[a] != lab[b]:
            out_comp[lab[a]] += 1
    members = defaultdict(list)
    for i, l in enumerate(lab):
        members[l].append(i)
    return [members[c] for c in range(nc) if out_comp[c] == 0 and len(members[c]) > 1]


def exact_stationary(members, edges, n):
    pos = {m: k for k, m in enumerate(members)}
    sz = len(members)
    Q = [[Fraction(0)] * sz for _ in range(sz)]  # Q[b][a] = rate a->b ; columns sum to zero
    for (a, b), r in edges.items():
        if a in pos:
            Q[pos[b]][pos[a]] += r
            Q[pos[a]][pos[a]] -= r
    # replace last equation by normalisation
    A = [row[:] for row in Q]
    A[sz - 1] = [Fraction(1)] * sz
    rhs = [Fraction(0)] * (sz - 1) + [Fraction(1)]
    for c in range(sz):
        piv = None
        for r in range(c, sz):
            if A[r][c] != 0:
                piv = r
                break
        if piv is None:
            raise RuntimeError("singular")
        A[c], A[piv] = A[piv], A[c]
        rhs[c], rhs[piv] = rhs[piv], rhs[c]
        inv = 1 / A[c][c]
        A[c] = [x * inv for x in A[c]]
        rhs[c] *= inv
        for r in range(sz):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
                rhs[r] -= f * rhs[c]
    return rhs  # pi over members


def part_D():
    Lx, N = 4, 2
    V = Lx * Lx
    canon = Fraction(V - N, V - 1)  # (16-2)/(16-1) = 14/15
    res = {}
    for model, gamma in (("O_class", Fraction(1)), ("Vstar", Fraction(1)), ("Vstar", Fraction(2)), ("Vstar", Fraction(1, 2))):
        states, idx, edges, sedges = build_chain(Lx, N, model, gamma)
        n = len(states)
        inflow = defaultdict(Fraction)
        outflow = defaultdict(Fraction)
        for (a, b), r in sedges.items():
            outflow[a] += r
            inflow[b] += r
        unbalanced = sum(1 for i in range(n) if inflow[i] != outflow[i])
        classes = closed_classes(n, edges)
        full_multiset_size = {}
        ratios = []
        tvs = []
        for mem in classes:
            P = P_of(states[mem[0]])
            if P == (0, 0):
                continue
            comp = 0 if P[0] != 0 else 1
            Js = [J_of(states[m], Lx) for m in mem]
            if model == "O_class":
                # uniform is stationary (balance holds exactly); mean J under uniform:
                EJ = sum(Fraction(j[comp]) for j in Js) / len(mem)
                ratios.append((len(mem), P, EJ / P[comp]))
                tvs.append(Fraction(0))
            else:
                if len(mem) > 130:
                    continue
                pi = exact_stationary(mem, edges, n)
                EJ = sum(p * j[comp] for p, j in zip(pi, Js))
                ratios.append((len(mem), P, EJ / P[comp]))
                tvs.append(sum(abs(p - Fraction(1, len(mem))) for p in pi) / 2)
        res[(model, gamma)] = (unbalanced, n, ratios, tvs)
        distinct = sorted({r for _, _, r in ratios})
        print(f"     info D {model} gamma={gamma}: streaming-balance defects {unbalanced}/{n} states; "
              f"closed classes with P!=0: {len(ratios)}; E[J]/P values {[str(x) for x in distinct]}; "
              f"max TV from uniform {float(max(tvs)):.4f}", flush=True)
    ub, n, ratios, tvs = res[("O_class", Fraction(1))]
    chk("D1 O: uniform measure is exactly stationary (in-rate = out-rate at every one of the 1920 states) "
        "[streaming part; class events are symmetric]", ub == 0, f"balance defects {ub}")
    # classes of O that are the FULL content-multiset sector
    from math import comb, factorial
    full_ok = True
    nfull = 0
    for sz, P, r in ratios:
        # full multiset sector size = C(V,N) * N!/prod(m_d!) ; N=2: contents (a,b)
        pass
    # the sector P=(+-1,+-1): contents {x or -x, y or -y}: 120 * 2 = 240
    sel = [(sz, P, r) for sz, P, r in ratios if sz == comb(V, N) * 2]
    full_ok = len(sel) > 0 and all(r == canon for _, _, r in sel)
    chk("D2 O: on every closed class equal to a full content-multiset sector the exact E[J]/P is (V-N)/(V-1) "
        "(canonical exclusion factor, not 1)", full_ok,
        f"{len(sel)} such classes, ratios {sorted({str(r) for _,_,r in sel})}, canonical {canon}")
    others = [(sz, P, r) for sz, P, r in ratios if sz != comb(V, N) * 2]
    ring = Fraction(4 - N, 4 - 1)  # both records confined to one ring of 4 sites: (R-N)/(R-1) = 2/3
    chk("D3 O: the other classes are confined to lines (the records move along one axis only): records on different "
        "lines never meet and have E[J]/P = 1 exactly; records on the same 4-site ring have the same canonical form "
        "with V replaced by the accessible sites, (4-2)/(4-1) = 2/3",
        len(others) > 0 and all(r in (Fraction(1), ring) for _, _, r in others),
        f"{len(others)} classes, ratios {sorted({str(r) for _,_,r in others})}")
    # Vstar
    vals = {}
    for g in (Fraction(1), Fraction(2), Fraction(1, 2)):
        ub2, n2, r2, tv2 = res[("Vstar", g)]
        vals[g] = (ub2, r2, tv2)
    ub2, r2, tv2 = vals[Fraction(1)]
    chk("D4 V*: the uniform measure is NOT stationary (exact in/out rate defects at some states)", ub2 > 0,
        f"{ub2} of 1920 states have in-rate != out-rate")
    big = [(sz, P, r) for sz, P, r in r2 if sz == 60]
    allr = sorted({r for _, _, r in big})
    chk("D5 V*: exact stationary E[J]/P on the P=(+-1,+-1) classes (size 60) is a single rational strictly below the "
        "canonical 14/15, so the angular-momentum repair does not help the energy current",
        len(big) > 0 and len(allr) == 1 and allr[0] < canon,
        f"E[J]/P = {allr[0] if allr else None} (= {float(allr[0]) if allr else None:.5f}) vs canonical {canon} (= {float(canon):.5f})")
    # gamma dependence
    gam_vals = {str(g): sorted({str(r) for sz, P, r in vals[g][1] if sz == 60}) for g in vals}
    chk("D6 V*: for scattering rates gamma in {1/2,1,2} the exact ratio stays strictly below 14/15 and below 1",
        all(all(Fraction(x) < canon for x in v) and v for v in gam_vals.values()), f"{gam_vals}")
    chk("D7 V*: stationary measure differs from uniform (exact total-variation distance > 0)",
        len(tv2) > 0 and max(tv2) > 0, f"max TV (gamma=1) = {float(max(tv2)):.4f}")
    # E: bounded-placement lemma on one V* class
    states, idx, edges, sedges = build_chain(Lx, N, "Vstar", Fraction(1))
    classes = closed_classes(len(states), edges)
    mem = [m for m in classes if len(m) == 60 and P_of(states[m[0]]) == (1, 1)][0]
    pi = exact_stationary(mem, edges, len(states))
    pos = {m: k for k, m in enumerate(mem)}
    out_edges = defaultdict(list)
    for (a, b), r in edges.items():
        if a in pos:
            out_edges[a].append((b, r))
    # exact residual of the stationary vector: sum_a pi_a Q_ab = 0 for every b in the class
    resid = defaultdict(Fraction)
    for (a, b), r in edges.items():
        if a in pos:
            resid[b] += pi[pos[a]] * r
            resid[a] -= pi[pos[a]] * r
    chk("D8 V*: the exact stationary vector of the 60-state class solves pi Q = 0 with zero residual and sums to 1",
        all(v == 0 for v in resid.values()) and sum(pi) == 1 and all(p > 0 for p in pi),
        f"{len(mem)} states, all probabilities positive")
    rnd = random.Random(2026)
    ok_all = True
    for trial in range(3):
        nu = {m: Fraction(rnd.randint(-3, 3)) for m in mem}  # arbitrary bounded function of the state
        gnu = {m: sum(r * (nu[b] - nu[m]) for b, r in out_edges[m]) for m in mem}
        mean = sum(p * gnu[m] for p, m in zip(pi, mem))
        ok_all &= (mean == 0)
    EJ = sum(p * J_of(states[m], Lx)[0] for p, m in zip(pi, mem))
    chk("E1 V*: for random bounded functions nu of the state, the exact stationary mean of (G nu) is 0 -- so a "
        "re-placement of energy density by a bounded local divergence term cannot change the mean energy current",
        ok_all, "3 random nu, exact")
    chk("E2 hence for V* the mean energy current <J_x> stays strictly below P_x = 1 for every bounded placement",
        EJ < Fraction(14, 15), f"<J_x> = {EJ} = {float(EJ):.5f} with P_x = 1")


# ==================================================================================
# F.  Exact symmetric compact stress for every (P,L)-preserving event (2D)
# ==================================================================================
def solve_exact(rows, rhs):
    """rows: list of dict var->Fraction; returns True iff consistent."""
    piv = {}
    for r, b in zip(rows, rhs):
        r = dict(r)
        b = Fraction(b)
        while r:
            v = min(r)
            if v in piv:
                pr, pb = piv[v]
                f = r[v]
                for k, val in pr.items():
                    nv = r.get(k, 0) - f * val
                    if nv == 0:
                        r.pop(k, None)
                    else:
                        r[k] = nv
                b -= f * pb
            else:
                f = r[v]
                r = {k: val / f for k, val in r.items()}
                b = b / f
                piv[v] = (r, b)
                break
        else:
            if b != 0:
                return False
    return True


def stress_exists(sites, dpi, symmetric, margin):
    lo = [min(s[a] for s in sites) - margin for a in range(2)]
    hi = [max(s[a] for s in sites) + margin for a in range(2)]
    pts = [(x, y) for x in range(lo[0], hi[0] + 1) for y in range(lo[1], hi[1] + 1)]
    pset = set(pts)
    comps = [(0, 0), (0, 1), (1, 1)] if symmetric else [(0, 0), (0, 1), (1, 0), (1, 1)]
    var = {}
    for p in pts:
        for c in comps:
            var[(p, c)] = len(var)

    def v(p, i, j):
        if symmetric and i > j:
            i, j = j, i
        return var[(p, (i, j))]

    rows, rhs = [], []
    for x in range(lo[0], hi[0] + 2):
        for y in range(lo[1], hi[1] + 2):
            for j in range(2):
                row = defaultdict(Fraction)
                for i in range(2):
                    if (x, y) in pset:
                        row[v((x, y), i, j)] += 1
                    xm = (x - (1 if i == 0 else 0), y - (1 if i == 1 else 0))
                    if xm in pset:
                        row[v(xm, i, j)] -= 1
                rows.append({k: val for k, val in row.items() if val != 0})
                rhs.append(Fraction(dpi.get((x, y), (0, 0))[j]))
    return solve_exact(rows, rhs)


def part_F():
    clusters = {
        "bond": [(0, 0), (1, 0)],
        "diag": [(0, 0), (1, 1)],
        "ltriple": [(0, 0), (1, 0), (0, 1)],
        "plaquette": [(0, 0), (1, 0), (0, 1), (1, 1)],
        "line3": [(0, 0), (1, 0), (2, 0)],
        "knight": [(0, 0), (2, 0), (1, 1)],
    }
    tot = 0
    bad = 0
    margin_used = defaultdict(int)
    for name, sites in clusters.items():
        n = len(sites)
        for mask in range(1, 1 << n):
            xs = [sites[i] for i in range(n) if mask >> i & 1]
            if len(xs) < 2:
                continue
            classes = defaultdict(list)
            for ks in itertools.product(range(4), repeat=len(xs)):
                P = (sum(E2[k][0] for k in ks), sum(E2[k][1] for k in ks))
                L = sum(cr2(p, E2[k]) for p, k in zip(xs, ks))
                classes[(P, L)].append(ks)
            for mem in classes.values():
                for c2 in mem[1:]:
                    dpi = {x: (E2[b][0] - E2[a][0], E2[b][1] - E2[a][1]) for x, a, b in zip(xs, mem[0], c2)}
                    tot += 1
                    ok = stress_exists(xs, dpi, True, 1)
                    m = 1
                    if not ok:
                        ok = stress_exists(xs, dpi, True, 2)
                        m = 2
                    margin_used[m] += 1
                    bad += (not ok)
    chk("F1 every (P,L)-preserving event on bond / diagonal / L-triple / plaquette / 3-in-a-line / (0,0),(2,0),(1,1) subsets (2D, includes the distance-2 head-on pair) has a compactly "
        "supported SYMMETRIC stress, exact rational solve (replaces the old floating-point residual test)",
        bad == 0, f"{tot} events, {bad} without solution, margin used {dict(margin_used)}")
    # controls: perpendicular exchange (violates L)
    xs = [(0, 0), (1, 0)]
    dpi = {(0, 0): (-1, 1), (1, 0): (1, -1)}  # x-hat at (0,0), y-hat at (1,0) exchanged
    sym = stress_exists(xs, dpi, True, 2)
    gen = stress_exists(xs, dpi, False, 2)
    chk("F2 control: the perpendicular exchange of O (changes L by -1) has NO symmetric compact stress but has a "
        "non-symmetric one (exact)", (not sym) and gen, f"symmetric {sym}, general {gen}")
    # necessity: random non-conserving delta has no symmetric stress
    rnd = random.Random(7)
    sites = clusters["plaquette"]
    nbad = 0
    cnt = 0
    for _ in range(12):
        d = {s: (rnd.randint(-2, 2), rnd.randint(-2, 2)) for s in sites}
        dP = (sum(v[0] for v in d.values()), sum(v[1] for v in d.values()))
        dL = sum(cr2(s, d[s]) for s in sites)
        if dP == (0, 0) and dL == 0:
            continue
        cnt += 1
        if stress_exists(sites, d, True, 2):
            nbad += 1
    chk("F3 necessity: random plaquette changes with dP != 0 or dL != 0 never have a symmetric compact stress "
        "(consistent with the telescoping proof)", cnt > 0 and nbad == 0, f"{cnt} random non-conserving changes, {nbad} solvable")


# ==================================================================================
# G.  The third comparator S: synchronous collide-then-stream.  Does exclusion plus
#     (N,P,L) conservation by itself stop the energy current from equalling P?
# ==================================================================================
def resolvability_window(W, Nmax, dim=2):
    if dim == 2:
        sites = [(x, y) for x in range(W) for y in range(W)]
        contents = E2
        cross = lambda p, c: (cr2(p, c),)
    else:
        sites = [(x, y, z) for x in range(W) for y in range(W) for z in range(W)]
        contents = E3
        cross = cr3
    out = []
    for N in range(2, Nmax + 1):
        tot = conf = unres = 0
        tickbad = 0
        for occ in itertools.combinations(sites, N):
            info = defaultdict(list)
            for ks in itertools.product(range(len(contents)), repeat=N):
                P = tuple(sum(contents[k][a] for k in ks) for a in range(dim))
                L = tuple(sum(cross(p, contents[k])[a] for p, k in zip(occ, ks)) for a in range(len(cross(occ[0], contents[0]))))
                tg = len({tuple(p[a] + contents[k][a] for a in range(dim)) for p, k in zip(occ, ks)}) == N
                info[(P, L)].append((ks, tg))
            for key, mem in info.items():
                free = [ks for ks, t in mem if t]
                for ks, t in mem:
                    tot += 1
                    if not t:
                        conf += 1
                        if not free:
                            unres += 1
                    # tick bookkeeping for the resolved configuration c'
                    cprime = ks if t else (free[0] if free else None)
                    if cprime is not None:
                        # stream: every record moves by its content
                        disp = tuple(sum(contents[k][a] for k in cprime) for a in range(dim))
                        Pn = tuple(sum(contents[k][a] for k in cprime) for a in range(dim))
                        newpos = [tuple(p[a] + contents[k][a] for a in range(dim)) for p, k in zip(occ, cprime)]
                        Ln = tuple(sum(cross(p, contents[k])[a] for p, k in zip(newpos, cprime)) for a in range(len(key[1])))
                        if disp != key[0] or Pn != key[0] or Ln != key[1]:
                            tickbad += 1
        out.append((N, tot, conf, unres, tickbad))
    return out


def pair_closure_unresolved(W, N, R2):
    sites = [(x, y) for x in range(W) for y in range(W)]
    bad = 0
    tot = 0
    for occ in itertools.combinations(sites, N):
        cfgs = list(itertools.product(range(4), repeat=N))
        idx = {c: i for i, c in enumerate(cfgs)}
        free = [len({(p[0] + E2[k][0], p[1] + E2[k][1]) for p, k in zip(occ, ks)}) == N for ks in cfgs]
        parent = list(range(len(cfgs)))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        pairs = [(i, j) for i in range(N) for j in range(i + 1, N)
                 if (occ[i][0] - occ[j][0]) ** 2 + (occ[i][1] - occ[j][1]) ** 2 <= R2]
        for ci, ks in enumerate(cfgs):
            for i, j in pairs:
                a, b = ks[i], ks[j]
                Pab = (E2[a][0] + E2[b][0], E2[a][1] + E2[b][1])
                Lab = cr2(occ[i], E2[a]) + cr2(occ[j], E2[b])
                for u in range(4):
                    for v in range(4):
                        if (u, v) != (a, b) and (E2[u][0] + E2[v][0], E2[u][1] + E2[v][1]) == Pab \
                                and cr2(occ[i], E2[u]) + cr2(occ[j], E2[v]) == Lab:
                            nk = list(ks)
                            nk[i], nk[j] = u, v
                            ra, rb = find(ci), find(idx[tuple(nk)])
                            if ra != rb:
                                parent[ra] = rb
        cf = defaultdict(bool)
        for ci, f in enumerate(free):
            cf[find(ci)] |= f
        for ci in range(len(cfgs)):
            tot += 1
            if not cf[find(ci)]:
                bad += 1
    return bad, tot



def torus_p_only_unresolved(W, N):
    sites = [(x, y) for x in range(W) for y in range(W)]
    bad = 0
    tot = 0
    for occ in itertools.combinations(sites, N):
        info = defaultdict(list)
        for ks in itertools.product(range(4), repeat=N):
            P = (sum(E2[k][0] for k in ks), sum(E2[k][1] for k in ks))
            tg = len({((p[0] + E2[k][0]) % W, (p[1] + E2[k][1]) % W) for p, k in zip(occ, ks)}) == N
            info[P].append(tg)
        for mem in info.values():
            tot += len(mem)
            if not any(mem):
                bad += len(mem)
    return bad, tot

def part_G():
    # whole-class (non-local) resolution, 2D 3x3 window, all N
    t0 = time.time()
    r = resolvability_window(3, 9, 2)
    for N, tot, conf, unres, tb in r:
        print(f"     info G 3x3 window N={N}: configs {tot}, with target conflict {conf}, unresolvable {unres}, tick-ledger errors {tb}")
    chk("G1 2D 3x3 window, EVERY occupation N=2..9, every configuration: a (N,P,L)-preserving reassignment of the "
        "contents of the SAME occupied sites with pairwise distinct targets exists (conflict-free streaming possible)",
        all(u == 0 for _, _, _, u, _ in r), f"{sum(t for _,t,_,_,_ in r)} configs, {sum(c for _,_,c,_,_ in r)} had a conflict, "
        f"{time.time()-t0:.0f}s")
    chk("G2 after collide-then-stream the exact ledger: N, P, L unchanged and the energy current (sum of "
        "displacements per tick) equals P, for every configuration of G1",
        all(tb == 0 for *_, tb in r))
    r4 = resolvability_window(4, 4, 2)
    for N, tot, conf, unres, tb in r4:
        print(f"     info G 4x4 window N={N}: configs {tot}, conflict {conf}, unresolvable {unres}, tick-ledger errors {tb}")
    chk("G3 2D 4x4 window, N=2,3,4 (all configurations): same result",
        all(u == 0 and tb == 0 for _, _, _, u, tb in r4), f"{sum(t for _,t,_,_,_ in r4)} configs")
    r3 = resolvability_window(2, 4, 3)
    for N, tot, conf, unres, tb in r3:
        print(f"     info G 3D 2x2x2 cube N={N}: configs {tot}, conflict {conf}, unresolvable {unres}, tick-ledger errors {tb}")
    chk("G4 3D 2x2x2 cube, six-axis contents, N=2..4 (all configurations; L is a vector): same result",
        all(u == 0 and tb == 0 for _, _, _, u, tb in r3), f"{sum(t for _,t,_,_,_ in r3)} configs")
    # locality: pair events only (closure of two-record (P,L)-preserving events)
    rows = {}
    t0 = time.time()
    for N in (2, 3, 4, 5, 6):
        rows[N] = {R2: pair_closure_unresolved(3, N, R2) for R2 in (2, 4)}
        print(f"     info G 3x3 window N={N}: unresolved by pair-event closure with d^2<=2: {rows[N][2][0]}/{rows[N][2][1]};"
              f" with d^2<=4: {rows[N][4][0]}/{rows[N][4][1]}", flush=True)
    chk("G5 locality: pair events at distance^2 <= 2 only (bond + face-diagonal) are NOT enough: antiparallel "
        "records two sites apart converge on one site (N=2: 6 of 576 unresolved)",
        rows[2][2][0] == 6, f"unresolved counts by N: {[rows[N][2][0] for N in rows]}")
    chk("G6 locality: closure of two-record events with distance^2 <= 4 (adds head-on pairs two sites apart) "
        "resolves every configuration of the 3x3 window for N=2..6",
        all(rows[N][4][0] == 0 for N in rows), f"{time.time()-t0:.0f}s")


def part_G8():
    r33 = {N: torus_p_only_unresolved(3, N) for N in (2, 3, 4)}
    r44 = {N: torus_p_only_unresolved(4, N) for N in (3, 4)}
    print(f"     info G8 3x3 torus P-only-class unresolved: {r33}; 4x4 torus: {r44}", flush=True)
    chk("G8 limit of G1-G4: on PERIODIC tori the window result fails even if only N and P (not L) must be kept: "
        "3x3 torus N=3 has 72 and N=4 has 432 configurations whose whole P-class has no conflict-free reassignment; "
        "4x4 torus N=4 has 224 (so existence of a collide-then-stream rule on the torus is not automatic)",
        r33[2][0] == 0 and r33[3][0] == 72 and r33[4][0] == 432 and r44[3][0] == 0 and r44[4][0] == 224,
        f"{ {k: v[0] for k, v in r33.items()} } / { {k: v[0] for k, v in r44.items()} }")


def main():
    part_A()
    part_B()
    part_C()
    part_D()
    part_F()
    part_G()
    part_G8()
    n_pass = sum(RESULTS)
    n_fail = len(RESULTS) - n_pass
    if n_fail == 0:
        print("HIT: the T17 verdict 'exclusion still stops energy flowing as momentum, so the exact books are not reached "
              "for either clause' is schedule-specific: for the asynchronous rate-1 streaming gases O and V* the energy "
              "current is below P in every ergodic sector (exact E[J]/P = 14/15 for O, a strictly smaller exact "
              "rational for V* at N=2 on the 4x4 torus; no bounded re-placement of energy density changes it), but with a "
              "synchronous collide-then-stream tick built from the same (N,P,L)-preserving pair events (distance^2<=4) "
              "the energy current equals P exactly on every tested open window (2D 3x3 all N, 2D 4x4 N<=4, 3D cube N<=4, "
              "conflict-free targets always reachable), while small periodic tori already contain configurations with no "
              "conflict-free P-preserving reassignment; the first open step is a bounded-range, rotation-covariant, "
              "parallel collision map on the full state space and its compatibility with Record permanence.")
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    print("SUMMARY: exact ledger shows V* keeps N,P,L while O breaks L, both leave the asynchronous energy current below "
          "momentum (O exactly by (V-N)/(V-1), V* by a smaller exact rational, unchanged by any bounded energy "
          "re-placement), whereas a synchronous collide-then-stream tick with distance-2 pair events makes J=P exactly "
          f"on all tested open windows, though not automatically on small periodic tori ({time.time()-T0:.0f}s).")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

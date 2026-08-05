#!/usr/bin/env python3
"""Cycle 926 -- INDEPENDENT CHECK of the gate sweep and the separation family,
spec'd to REFUTE.

Independence of implementation, top to bottom (the 917/919 checker pattern):

  * Hamiltonians are assembled as SPARSE PAULI KRONECKER PRODUCTS from the
    geometry declarations (the primary uses a diagonal array plus XOR gathers);
  * the propagator is scipy.sparse.linalg.expm_multiply, stepped interval by
    interval (the primary uses Chebyshev/Bessel, a Taylor marcher and a dense
    eigendecomposition);
  * reduced states come from np.tensordot contractions over complement axes;
  * spectra come from scipy.linalg.eigvalsh with the explicit 'ev' driver;
  * R_ind is a brute-force BITMASK maximum-clique search over the independence
    graph (the primary descends over itertools.combinations);
  * every geometry is rebuilt from the BLOCK SPECIFICATION and the primary's
    prose declaration, never from its receipt, and the rebuilt sites/bonds are
    then compared against the receipt's published lists;
  * fragment partitions are re-derived from the FROZEN MEMO'S OWN BYTES (the
    signed-axis labelling and the three tie-break clauses are parsed out of the
    memo and applied);
  * every statistic -- pointer degree, max degree, branch count, fragment count,
    components of G-S, loops, depth -- is recomputed from the rebuilt adjacency,
    so a doctored statistic cannot travel;
  * the G6 cube rows are re-expanded from the pinned 914 receipt using a pair-class
    map read out of the 914 SOURCE BYTES, not from the primary.

It then ATTACKS, in this order:

  (i)   THE CLAIM-BOUNDARY VALUES.  Every boundary the primary quotes is
        re-probed independently: the claim must hold strictly inside the quoted
        band and FAIL immediately outside it.  A band that is too wide or too
        narrow is a refutation.
  (ii)  THE SEPARATION FAMILY'S CONSTRUCTION.  Each geometry is checked to
        actually separate the statistics it is claimed to separate, with all
        five statistics recomputed from adjacency under the frozen rule -- and
        the frozen rule re-derived from the memo bytes, so a geometry that only
        separates under a bent rule is caught.
  (iii) THE CARRYING-STATISTIC VERDICT.  Model degeneracy: does the rival
        statistic fit the same cells equally well?  Every candidate is fitted as
        an equality predictor for the ceiling and as a threshold predictor for
        the field ceiling, over the full 29-geometry set, and ties are reported
        as ties rather than resolved in the primary's favour.

Exit 0 whatever survives.  A refutation is a result, not an error.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import hashlib
import itertools
import json
import os
import platform
import re
import resource
import subprocess
import sys
import time
from collections import deque

import numpy as np
import scipy.sparse as sp
from scipy.linalg import eigvalsh
from scipy.sparse.linalg import expm_multiply

T_START = time.perf_counter()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIMARY = "scripts/frontier_cycle926_gate_sweep_separation_2026_07_28.py"
RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
C914_SOURCE = "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C919_SOURCE = "scripts/frontier_cycle919_degree_five_2026_07_28.py"

CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
DEADLINE = 1.0
PERSIST = 3
HEADLINE = 0.10
DRIFT_MAX = 0.10
DELTAS = (0.05, 0.10, 0.20)
FROZEN_LAMBDAS = (0.05, 0.10)
LAMBDAS = (0.05, 0.075, 0.10)
PROBE_LAMBDAS = (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20)
TIMES = [round(0.1 * i, 10) for i in range(13)]
CUBE_ORDER = ["+x", "-x", "+y", "-y", "+z", "-z"]

LADDER = ["G1", "G2", "G3a", "G3b", "G4", "G5", "G6", "H1", "H2", "H3", "H4"]
NEWK = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4",
        "C1", "C2", "C3", "D1", "E1", "E2"]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(a):
    return subprocess.run(["git"] + a, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


# ============================ the frozen rule, re-derived from the memo bytes ==
def memo_rule(memo):
    """Parse the frozen labelling / tie-break clauses out of the memo's own bytes."""
    got = {}
    m = re.search(r"1\. assign each axial face site to its own signed-axis fragment;", memo)
    got["clause1"] = bool(m)
    m2 = re.search(r"2\. assign an edge with `x != 0` to `F_\(sign\(x\)x\)`;", memo)
    got["clause2"] = bool(m2)
    m3 = re.search(r"3\. for an edge with `x=0` and for every corner, ignore the corner's "
                   r"`x` sign and map `\(sign\(y\),sign\(z\)\)` by `\(\+,\+\)->\+y`, "
                   r"`\(-,\+\)->\+z`, `\(-,-\)->-y`, and `\(\+,-\)->-z`\.", memo)
    got["clause3"] = bool(m3)
    m4 = re.search(r"every pair has `C_ab <= (0\.02) bit`", memo)
    got["indep_max"] = float(m4.group(1)) if m4 else None
    m5 = re.search(r"persistence flag requires three consecutive certification samples", memo)
    got["persist_is_three"] = bool(m5)
    m6 = re.search(r"The headline onset deadline remains `Jt <= (1)`", memo)
    got["deadline"] = float(m6.group(1)) if m6 else None
    m7 = re.search(r"`R_ind` is the largest pairwise-independent certifying subset", memo)
    got["r_ind_def"] = bool(m7)
    if not all([got["clause1"], got["clause2"], got["clause3"], got["r_ind_def"],
                got["persist_is_three"]]) or got["indep_max"] != INDEP_MAX \
            or got["deadline"] != DEADLINE:
        print("CHECKER-FAIL memo-rule-not-parsed %s" % BOUNDARY_LINE)
        sys.exit(2)
    return got


def sgn_label(c):
    """Clause 1/2/3 as a single function of a cube coordinate: the signed axis of the
    first nonzero coordinate.  Verified below to reproduce the memo's six cube lists."""
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    return None


def clause3(c):
    y, z = c[1], c[2]
    return {(1, 1): "+y", (-1, 1): "+z", (-1, -1): "-y", (1, -1): "-z"}[
        (1 if y > 0 else -1, 1 if z > 0 else -1)]


def tiebreak(c, cand_labels):
    """The memo's tie-break, applied to a coordinate with several equidistant anchors."""
    x = c[0]
    nz = sum(1 for v in c if v != 0)
    want = ("+x" if x > 0 else "-x") if (nz == 2 and x != 0) else clause3(c)
    return want if want in cand_labels else None


# ================================================ independent geometry build ==
def _b(sites, bonds, pointer, labeller, dim="graph"):
    idx = {c: i for i, c in enumerate(sites)}
    n = len(sites)
    E = sorted({tuple(sorted((idx[a], idx[b]))) for a, b in bonds})
    adj = {i: set() for i in range(n)}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    S = idx[pointer]
    rec = sorted(adj[S])
    lab = {r: labeller(sites[r]) for r in rec}
    # BFS distances from every anchor, computed here (not imported)
    def bf(src):
        d = {src: 0}
        q = deque([src])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    q.append(v)
        return d
    dS = bf(S)
    if len(dS) != n:
        return None
    dr = {r: bf(r) for r in rec}
    frag = {}
    for r in rec:
        frag.setdefault(lab[r], []).append(r)
    ties = 0
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: dr[r].get(i, 10 ** 9) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        cl = sorted({lab[c] for c in cands})
        if len(cl) == 1:
            pick = cl[0]
        else:
            ties += 1
            pick = tiebreak(sites[i], cl)
            if pick is None:
                return None
        frag[pick].append(i)
    labels = sorted(frag, key=lambda L: (CUBE_ORDER.index(L) if L in CUBE_ORDER else 99, L))
    for L in labels:
        heads = [r for r in rec if lab[r] == L]
        rest = [i for i in frag[L] if i not in heads]
        frag[L] = sorted(heads, key=lambda i: str(sites[i])) + \
            sorted(rest, key=lambda i: (dS[i], str(sites[i])))
    deg = {i: len(adj[i]) for i in range(n)}
    rest = [i for i in range(n) if i != S]
    seen, comps = set(), 0
    for i in rest:
        if i in seen:
            continue
        comps += 1
        q = deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v != S and v not in seen:
                    seen.add(v)
                    q.append(v)
    return {"sites": sites, "strsites": [str(c) for c in sites], "bonds": E, "adj": adj,
            "S": S, "rec": rec, "labels": labels, "frags": frag, "dS": dS,
            "degrees": deg, "n_ties": ties,
            "stats": {"n_sites": n, "n_bonds": len(E), "pointer_degree": len(rec),
                      "max_degree": max(deg.values()),
                      "branch_count_at_pointer": len(rec),
                      "components_of_G_minus_S": comps,
                      "depth_eccentricity_from_pointer": max(dS.values()),
                      "cyclomatic_number_loops": len(E) - n + 1,
                      "loop_free": bool(len(E) - n + 1 == 0),
                      "n_fragments": len(labels),
                      "fragment_sizes": {L: len(frag[L]) for L in labels}}}


def _lat(sites):
    return [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
            if sum(abs(a[k] - b[k]) for k in range(3)) == 1]


def _nb(P):
    out = []
    for ax in range(3):
        for s in (1, -1):
            q = list(P)
            q[ax] += s
            out.append(tuple(q))
    return out


def spec_geometries():
    """Every geometry rebuilt from the block specification / prose declaration."""
    G = {}
    # ---------------- the pinned 917 / 919 ladder -----------------------------
    ch = [(k, 0, 0) for k in range(-4, 5)]
    G["G1"] = (ch, [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)], (0, 0, 0),
               lambda c: ("+x" if c[0] > 0 else "-x"))
    G["G2"] = (["S"] + ["a%d" % i for i in range(1, 7)],
               [("S", "a%d" % i) for i in range(1, 7)], "S", lambda c: c)
    for nb_, key in ((3, "G3a"), (4, "G3b"), (5, "H2")):
        s, e = ["S"], []
        for b in range(nb_):
            s.append("b%d" % b)
            e.append(("S", "b%d" % b))
            for k in range(2):
                s.append("b%dg%d" % (b, k))
                e.append(("b%d" % b, "b%dg%d" % (b, k)))
        G[key] = (s, e, "S", lambda c: c)
    pl = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    G["G4"] = (pl, _lat(pl), (0, 0, 0),
               lambda c: ("+x" if c[0] > 0 else "-x") if c[0] != 0
               else ("+y" if c[1] > 0 else "-y"))
    c11 = [(0, 0, 0)] + [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
                         (0, 0, -1)] + [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    G["G5"] = (c11, _lat(c11), (0, 0, 0), sgn_label)
    c27 = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    G["G6"] = (c27, _lat(c27), (0, 0, 0), sgn_label)
    G["H1"] = (["S"] + ["a%d" % i for i in range(1, 6)],
               [("S", "a%d" % i) for i in range(1, 6)], "S", lambda c: c)
    s, e = ["S"], []
    for b in range(5):
        s.append("b%d" % b)
        e.append(("S", "b%d" % b))
        if b < 2:
            for k in range(2):
                s.append("b%dg%d" % (b, k))
                e.append(("b%d" % b, "b%dg%d" % (b, k)))
    G["H3"] = (s, e, "S", lambda c: c)
    c10 = [(0, 0, 0)] + [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)] + \
        [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    G["H4"] = (c10, _lat(c10), (0, 0, 0), sgn_label)
    # ---------------- the Q2 separation family (from the spec) ----------------
    def cstar(P, N):
        return ([P] + list(N), [(P, q) for q in N], P, sgn_label)
    G["A1"] = cstar((0, 0, 1), [(1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1), (0, 0, 2)])
    G["A2"] = cstar((0, 1, 1), [(1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2)])
    G["A3"] = cstar((0, 1, 1), [(1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2), (0, 1, 0)])
    G["A4"] = cstar((1, 1, 0), [(0, 1, 0), (2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1)])
    G["A5"] = cstar((1, 1, 0), [(2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1), (1, 1, -1)])
    P = (0, 0, 1)
    G["A6"] = ([P] + _nb(P), [(P, q) for q in _nb(P)], P,
               lambda c: "-z" if c == (0, 0, 0) else sgn_label(c))
    G["A7"] = cstar((0, 1, 1), _nb((0, 1, 1)))
    G["A8"] = cstar((1, 1, 0), _nb((1, 1, 0)))
    G["B1"] = (["S", "a", "b", "c", "d", "a1"],
               [("S", "a"), ("S", "b"), ("S", "c"), ("S", "d"), ("a", "a1")], "S",
               lambda c: c)
    G["B2"] = (["S", "a", "b", "c", "a1", "a2"],
               [("S", "a"), ("S", "b"), ("S", "c"), ("a", "a1"), ("a", "a2")], "S",
               lambda c: c)
    G["B3"] = (["S", "a", "b", "a1", "a2", "a3"],
               [("S", "a"), ("S", "b"), ("a", "a1"), ("a", "a2"), ("a", "a3")], "S",
               lambda c: c)
    G["B4"] = (["S", "a", "a1", "a2", "a3", "a4"],
               [("S", "a"), ("a", "a1"), ("a", "a2"), ("a", "a3"), ("a", "a4")], "S",
               lambda c: c)
    G["C1"] = (["S", "a", "b"] + ["a%d" % i for i in range(1, 6)],
               [("S", "a"), ("S", "b")] + [("a", "a%d" % i) for i in range(1, 6)], "S",
               lambda c: c)
    G["C2"] = (["S", "a", "b"] + ["a%d" % i for i in range(1, 4)]
               + ["b%d" % i for i in range(1, 4)],
               [("S", "a"), ("S", "b")] + [("a", "a%d" % i) for i in range(1, 4)]
               + [("b", "b%d" % i) for i in range(1, 4)], "S", lambda c: c)
    G["C3"] = (["S", "a", "b", "c", "d"] + ["a%d" % i for i in range(1, 6)],
               [("S", x) for x in ("a", "b", "c", "d")]
               + [("a", "a%d" % i) for i in range(1, 6)], "S", lambda c: c)
    d1s = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
           (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0), (1, 0, 1)]
    G["D1"] = (d1s, _lat(d1s), (0, 0, 0), sgn_label)
    e1s = [(0, 1, 1), (1, 1, 1), (-1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2),
           (2, 1, 1), (-2, 1, 1), (0, 3, 1), (0, 1, 3)]
    G["E1"] = (e1s, _lat(e1s), (0, 1, 1), sgn_label)
    G["E2"] = (["S", "a", "b", "c", "d", "a1", "a2", "a3", "b1", "c1"],
               [("S", x) for x in ("a", "b", "c", "d")]
               + [("a", "a1"), ("a1", "a2"), ("a1", "a3"), ("b", "b1"), ("c", "c1")],
               "S", lambda c: c)
    out = {}
    for k, (s, e, p, l) in G.items():
        g = _b(s, e, p, l)
        if g is None:
            print("CHECKER-FAIL geometry-build %s %s" % (k, BOUNDARY_LINE))
            sys.exit(2)
        out[k] = g
    return out


# ================================================ independent numerics ========
I2 = sp.identity(2, format="csr", dtype=np.float64)
SZ = sp.csr_matrix(np.array([[1.0, 0.0], [0.0, -1.0]]))
SX = sp.csr_matrix(np.array([[0.0, 1.0], [1.0, 0.0]]))


def kron_op(n, ops):
    """ops: {site: 2x2}; site 0 is the LEAST significant bit (the primary's convention)."""
    M = None
    for i in range(n - 1, -1, -1):
        A = ops.get(i, I2)
        M = A if M is None else sp.kron(M, A, format="csr")
    return M


def hamiltonian(n, bonds, lam):
    H = sp.csr_matrix((1 << n, 1 << n), dtype=np.float64)
    for (a, b) in bonds:
        H = H - kron_op(n, {a: SZ, b: SZ})
    for i in range(n):
        H = H - lam * kron_op(n, {i: SX})
    return H.tocsc()


def prep(n, plusx):
    v = np.array([1.0])
    for i in range(n - 1, -1, -1):
        s = (np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plusx else np.array([1.0, 0.0])
        v = np.kron(v, s)
    return v.astype(np.complex128)


def evolve(H, psi0, times):
    out, cur, tprev = [], psi0.copy(), 0.0
    for t in times:
        dt = t - tprev
        if dt > 1e-15:
            cur = expm_multiply(-1j * dt * H, cur)
        out.append(cur.copy())
        tprev = t
    return out


def rdm(psi, n, sites):
    T = psi.reshape((2,) * n)
    ax = [n - 1 - s for s in sites]
    keep = ax
    comp = [a for a in range(n) if a not in keep]
    T2 = np.transpose(T, keep + comp).reshape(1 << len(keep), -1)
    return np.tensordot(T2, T2.conj(), axes=([1], [1]))


def ent(rho):
    w = eigvalsh(rho, driver="ev").real
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum())


def chi_and_H(psi, n, S, frag):
    r = rdm(psi, n, [S] + list(frag))
    d = 1 << len(frag)
    b0, b1 = r[:d, :d], r[d:, d:]
    p0, p1 = float(np.trace(b0).real), float(np.trace(b1).real)
    tot = p0 + p1
    Sav = ent((b0 + b1) / tot)
    Sc = 0.0
    for b, p in ((b0, p0), (b1, p1)):
        if p > 1e-14:
            Sc += (p / tot) * ent(b / p)
    Hz = -sum((q / tot) * np.log2(q / tot) for q in (p0, p1) if q / tot > 1e-15)
    return Sav - Sc, Hz, p0 / tot


def cmi(psi, n, S, fa, fb):
    r = rdm(psi, n, [S] + list(fa) + list(fb))
    ka, kb = len(fa), len(fb)
    d = 1 << (ka + kb)
    tot = 0.0
    blocks = [r[:d, :d], r[d:, d:]]
    ps = [float(np.trace(b).real) for b in blocks]
    Z = sum(ps)
    for b, p in zip(blocks, ps):
        if p <= 1e-14:
            continue
        rr = b / p
        T = rr.reshape(1 << ka, 1 << kb, 1 << ka, 1 << kb)
        ra = np.einsum("aibi->ab", T)
        rb = np.einsum("iaib->ab", T)
        tot += (p / Z) * (ent(ra) + ent(rb) - ent(rr))
    return tot


def rind_bitmask(labels, passes, C, gate):
    """Brute-force maximum clique over the independence graph, by bitmask."""
    m = len(passes)
    if m == 0:
        return 0, []
    ok = [[True] * m for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            key = tuple(sorted((passes[i], passes[j]), key=labels.index))
            v = C.get(key)
            good = (v is not None and v <= gate)
            ok[i][j] = ok[j][i] = good
    best, bestkey = [], None
    for mask in range(1, 1 << m):
        sel = [i for i in range(m) if mask >> i & 1]
        if len(sel) < len(best):
            continue
        good = all(ok[a][b] for a, b in itertools.combinations(sel, 2))
        if not good:
            continue
        key = tuple(labels.index(passes[i]) for i in sel)
        if len(sel) > len(best) or (len(sel) == len(best)
                                    and (bestkey is None or key < bestkey)):
            best, bestkey = [passes[i] for i in sel], key
    return len(best), best


def cell_rows(g, lam):
    n, S = g["stats"]["n_sites"], g["S"]
    H = hamiltonian(n, g["bonds"], lam)
    psi0 = prep(n, set([S] + g["rec"]))
    states = evolve(H, psi0, TIMES)
    rows = []
    chi0 = None
    for it, (t, a) in enumerate(zip(TIMES, states)):
        chi, Hz, p0 = {}, None, None
        for L in g["labels"]:
            c, Hz, p0 = chi_and_H(a, n, S, g["frags"][L])
            chi[L] = c
        if it == 0:
            chi0 = dict(chi)
        exc = {L: chi[L] - chi0[L] for L in g["labels"]}
        C = {}
        for a1, b1 in itertools.combinations(g["labels"], 2):
            C[(a1, b1)] = cmi(a, n, S, g["frags"][a1], g["frags"][b1])
        rows.append({"jt": t, "H_Z": Hz, "chi": chi, "excess": exc, "C": C,
                     "drift": abs(p0 - 0.5)})
    return rows


def passes_of(g, r, delta=HEADLINE, excess_min=EXCESS_MIN, hmin=CONTENT_H_MIN):
    return [L for L in g["labels"] if r["H_Z"] >= hmin
            and r["chi"][L] >= (1.0 - delta) * r["H_Z"] and r["excess"][L] >= excess_min]


def verdict(g, rows, gate=INDEP_MAX, persist=PERSIST, deadline=DEADLINE, delta=HEADLINE):
    led = []
    for r in rows:
        k, w = rind_bitmask(g["labels"], passes_of(g, r, delta), r["C"], gate)
        led.append((k, w))
    idx = next((i for i, (k, _) in enumerate(led) if k >= 2), None)
    maxr = max(k for k, _ in led)
    if idx is None:
        return "NO", None, maxr, led
    run = 0
    for (k, _) in led[idx:]:
        if k >= 2:
            run += 1
        else:
            break
    ev = {"jt": rows[idx]["jt"], "r_ind": led[idx][0], "witness": led[idx][1], "run": run}
    if rows[idx]["jt"] > deadline + 1e-12:
        return "NO", ev, maxr, led
    if run < persist:
        return "NO", ev, maxr, led
    if rows[idx]["drift"] > DRIFT_MAX:
        return "NO", ev, maxr, led
    return "YES", ev, maxr, led


# =============================== the G6 rows, re-expanded from the 914 bytes ===
def g6_from_914(rec914, src914, lam_key):
    """Read the pair-class map out of the 914 SOURCE, then expand the pinned rows."""
    blk = re.search(r"declared_classes = \{(.*?)\n    \}", src914, re.S)
    if blk is None:
        print("CHECKER-FAIL 914-class-block-not-found %s" % BOUNDARY_LINE)
        sys.exit(2)
    body = blk.group(1)
    pmap = {}
    for cls, members in re.findall(r'"([a-z0-9-]+)": (\[[^\]]*\])', body):
        if "for q in" in members:
            head = re.search(r'\("([+-][xyz])", q\)', members).group(1)
            qs = re.findall(r'"([+-][xyz])"', members.split("for q in")[1])
            for q in qs:
                pmap[tuple(sorted((head, q), key=CUBE_ORDER.index))] = cls
        else:
            for a, b in re.findall(r'\("([+-][xyz])", "([+-][xyz])"\)', members):
                pmap[tuple(sorted((a, b), key=CUBE_ORDER.index))] = cls
    if len(pmap) != 15:
        print("CHECKER-FAIL 914-class-map-size=%d %s" % (len(pmap), BOUNDARY_LINE))
        sys.exit(2)
    rows = []
    chi0 = None
    for r in rec914["measurement"]["rows"][lam_key]:
        chi = {L: (r["chi_closed_five"] if L in ("+x", "-x") else r["chi_wedge_four"])
               for L in CUBE_ORDER}
        exc = {L: (r["excess_closed_five"] if L in ("+x", "-x") else r["excess_wedge_four"])
               for L in CUBE_ORDER}
        C = {}
        if r["pair_classes"]:
            for pa, cls in pmap.items():
                C[pa] = r["pair_classes"][cls]
        rows.append({"jt": r["jt"], "H_Z": r["H_Z"], "chi": chi, "excess": exc, "C": C,
                     "drift": r["pointer_tv_drift"]})
        _ = chi0
    gg = {"labels": list(CUBE_ORDER), "frags": {L: [] for L in CUBE_ORDER}}
    return gg, rows, pmap


# ==================================================================== main ====
def main():
    rec = json.load(open(os.path.join(ROOT, RECEIPT)))
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    rule = memo_rule(memo)
    src914 = open(os.path.join(ROOT, C914_SOURCE)).read()
    src919 = open(os.path.join(ROOT, C919_SOURCE)).read()
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    prim_bytes = open(os.path.join(ROOT, PRIMARY), "rb").read()

    findings, teeth = [], {}
    G = spec_geometries()

    # ---- tooth 1: the partition rule, rebuilt from the memo bytes, on the cube ----
    memo_frags = {}
    for lab in CUBE_ORDER:
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        memo_frags[lab] = {tuple(int(v) for v in s)
                           for s in re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)",
                                               m.group(1))}
    cube = G["G6"]
    mine = {L: {cube["sites"][i] for i in cube["frags"][L]} for L in CUBE_ORDER}
    rule_ok = all(mine[L] == memo_frags[L] for L in CUBE_ORDER)
    teeth["T1_frozen_rule_rebuilt_from_memo_bytes_reproduces_the_cube"] = {
        "ok": bool(rule_ok), "clauses_parsed": rule, "fires": True}
    if not rule_ok:
        findings.append("REFUTED: the partition rule rebuilt from the memo bytes does not "
                        "reproduce the memo's own six cube fragment lists")

    # ---- tooth 2: every statistic recomputed from adjacency ----------------------
    SHARED = ["n_sites", "n_bonds", "pointer_degree", "max_degree",
              "branch_count_at_pointer", "components_of_G_minus_S",
              "depth_eccentricity_from_pointer", "cyclomatic_number_loops", "loop_free",
              "n_fragments", "fragment_sizes"]
    stat_check, stat_bad = {}, []
    for k in NEWK:
        pub = rec["separation_family"]["geometries"][k]["stats"]
        got = G[k]["stats"]
        # only the statistics BOTH implementations compute; the primary's receipt also
        # carries presentation fields (dimension, seam lists) this checker does not build
        diffs = {s: [got.get(s), pub.get(s)] for s in SHARED if got.get(s) != pub.get(s)}
        stat_check[k] = {"agrees": not diffs, "differences": diffs,
                         "four_statistics": {s: got[s] for s in
                                             ("pointer_degree", "max_degree",
                                              "branch_count_at_pointer", "n_fragments")},
                         "components_of_G_minus_S": got["components_of_G_minus_S"]}
        if diffs:
            stat_bad.append(k)
    for k in [x for x in LADDER if x != "G6"]:
        pub = (r917["branching_statistics"].get(k) or r919["branching_statistics"].get(k))
        got = G[k]["stats"]
        if pub and any(got.get(s) != pub.get(s) for s in ("pointer_degree", "max_degree",
                                                          "n_fragments",
                                                          "components_of_G_minus_S")):
            stat_bad.append(k)
    teeth_note_shared = SHARED
    teeth["T2_statistics_recomputed_from_adjacency"] = {
        "geometries_checked": len(NEWK) + len(LADDER) - 1,
        "statistics_compared": teeth_note_shared,
        "disagreements": stat_bad, "per_geometry": stat_check, "fires": True}
    if stat_bad:
        findings.append("REFUTED: recomputed statistics disagree on %s" % stat_bad)

    # ---- tooth 3: the partitions themselves, site by site ------------------------
    part_bad = []
    for k in NEWK:
        pub = rec["separation_family"]["geometries"][k]["partition_site_by_site"]
        got = {L: [G[k]["strsites"][i] for i in G[k]["frags"][L]] for L in G[k]["labels"]}
        if {L: sorted(v) for L, v in pub.items()} != {L: sorted(v) for L, v in got.items()}:
            part_bad.append(k)
    teeth["T3_partitions_rederived_from_the_frozen_rule"] = {
        "geometries": len(NEWK), "disagreements": part_bad, "fires": True}
    if part_bad:
        findings.append("REFUTED: rebuilt partitions differ on %s" % part_bad)

    # ---- the independent measurement --------------------------------------------
    ROWS = {}
    for k in [x for x in LADDER if x != "G6"]:
        for lam in (LAMBDAS if k in ("H1", "H2", "H3", "H4") else FROZEN_LAMBDAS):
            ROWS[(k, "%g" % lam)] = cell_rows(G[k], lam)
    for k in NEWK:
        for lam in LAMBDAS:
            ROWS[(k, "%g" % lam)] = cell_rows(G[k], lam)
    g6g, g6r05, pmap = g6_from_914(r914, src914, "0.05")
    _, g6r10, _ = g6_from_914(r914, src914, "0.1")
    G["G6"] = dict(G["G6"], labels=list(CUBE_ORDER))
    ROWS[("G6", "0.05")] = g6r05
    ROWS[("G6", "0.1")] = g6r10
    G6G = {"labels": list(CUBE_ORDER)}

    def vd(k, lk, **kw):
        gg = G6G if k == "G6" else G[k]
        return verdict(gg, ROWS[(k, lk)], **kw)

    # ---- tooth 4: the 26-cell frozen table reproduced on independent machinery ----
    dev = {"chi": 0.0, "C": 0.0}
    tab_bad = []
    for cellkey, pubc in sorted(rec["frozen_point_26_cell_table"].items()):
        k, lk = cellkey.split("@")
        v, ev, maxr, _ = vd(k, lk)
        if v != pubc["verdict"] or maxr != pubc["max_r_ind"]:
            tab_bad.append("%s: %s/%d vs %s/%d" % (cellkey, v, maxr, pubc["verdict"],
                                                   pubc["max_r_ind"]))
        if ev and pubc["first_jt"] is not None:
            if abs(ev["jt"] - pubc["first_jt"]) > 1e-12 or ev["run"] != pubc["run"]:
                tab_bad.append("%s: event %s/%s vs %s/%s" % (cellkey, ev["jt"], ev["run"],
                                                             pubc["first_jt"], pubc["run"]))
    # numeric agreement against the primary's published rows (the pinned family)
    for k in ("H1", "H4", "G3b", "G1"):
        for lk in ("0.05", "0.1"):
            pubrows = r919["degree_five_geometries"][k]["lambdas"][lk]["rows"] \
                if k in ("H1", "H4") else r917["geometries"][k]["lambdas"][lk]["rows"]
            for r, q in zip(ROWS[(k, lk)], pubrows):
                for L in r["chi"]:
                    dev["chi"] = max(dev["chi"], abs(r["chi"][L] - q["chi"][L]))
                for pa, v in r["C"].items():
                    dev["C"] = max(dev["C"], abs(v - q["C_ab"]["|".join(pa)]))
    teeth["T4_26_cell_frozen_table_on_independent_machinery"] = {
        "cells": len(rec["frozen_point_26_cell_table"]), "disagreements": tab_bad,
        "max_abs_dev_vs_pinned_rows": dev, "fires": True}
    if tab_bad:
        findings.append("REFUTED: the frozen 26-cell table does not reproduce: %s"
                        % tab_bad[:6])

    # ---- ATTACK (i): the claim-boundary values ----------------------------------
    DEG = {}
    NFR = {}
    for k in LADDER:
        st = (G[k]["stats"] if k != "G6" else G["G6"]["stats"])
        DEG[k], NFR[k] = st["pointer_degree"], st["n_fragments"]

    SD = {k: (G[k]["stats"]["pointer_degree"]) for k in LADDER + NEWK}
    SF = {k: (G[k]["stats"]["n_fragments"]) for k in LADDER + NEWK}

    def threshold_at(gate, persist=PERSIST, deadline=DEADLINE):
        ys = {k: vd(k, "0.1", gate=gate, persist=persist, deadline=deadline)[0] == "YES"
              for k in LADDER}
        thr = 7
        for d in range(1, 8):
            if all(ys[k] for k in LADDER if DEG[k] >= d):
                thr = d
                break
        clean = all(ys[k] == (DEG[k] >= thr) for k in LADDER)
        return thr, clean, ys

    def claim_fn(name, gate, persist=PERSIST, deadline=DEADLINE):
        if name == "chain_certifies_at_0.05":
            return vd("G1", "0.05", gate=gate, persist=persist, deadline=deadline)[0] == "YES"
        if name == "threshold_is_degree_5":
            t, c, _ = threshold_at(gate, persist, deadline)
            return t == 5 and c
        if name == "threshold_exists_and_is_clean":
            return threshold_at(gate, persist, deadline)[1]
        if name == "ceiling_law_at_0.05":
            return all(vd(k, "0.05", gate=gate, persist=persist,
                          deadline=deadline)[2] == DEG[k] for k in LADDER)
        if name == "ceiling_law_at_0.05_vs_fragments":
            return all(vd(k, "0.05", gate=gate, persist=persist,
                          deadline=deadline)[2] == NFR[k] for k in LADDER)
        if name == "loop_cost_at_0.10":
            lo = [k for k in LADDER if not (G[k]["stats"]["loop_free"] if k != "G6"
                                            else False)]
            lf = [k for k in LADDER if k not in lo]
            return (all(vd(k, "0.1", gate=gate, persist=persist,
                           deadline=deadline)[2] < DEG[k] for k in lo)
                    and all(vd(k, "0.1", gate=gate, persist=persist,
                               deadline=deadline)[2] == DEG[k] for k in lf if DEG[k] >= 3))
        if name == "degree_five_all_yes_at_0.10":
            return all(vd(k, "0.1", gate=gate, persist=persist,
                          deadline=deadline)[0] == "YES" for k in ("H1", "H2", "H3", "H4"))
        if name == "degree_four_all_no_at_0.10":
            return all(vd(k, "0.1", gate=gate, persist=persist,
                          deadline=deadline)[0] == "NO" for k in LADDER if DEG[k] == 4)
        ALLG = LADDER + NEWK
        if name == "ceiling_equals_FRAGMENT_COUNT_at_0.05_on_all_29":
            return all(vd(k, "0.05", gate=gate, persist=persist,
                          deadline=deadline)[2] == SF[k] for k in ALLG)
        if name == "ceiling_equals_POINTER_DEGREE_at_0.05_on_all_29":
            return all(vd(k, "0.05", gate=gate, persist=persist,
                          deadline=deadline)[2] == SD[k] for k in ALLG)
        if name == "threshold_conjunction_degree5_AND_three_fragments":
            return all((vd(k, "0.1", gate=gate, persist=persist, deadline=deadline)[0]
                        == "YES") == (SD[k] >= 5 and SF[k] >= 3) for k in ALLG)
        if name == "threshold_tracks_POINTER_DEGREE_alone":
            return all((vd(k, "0.1", gate=gate, persist=persist, deadline=deadline)[0]
                        == "YES") == (SD[k] >= 5) for k in ALLG)
        if name == "threshold_tracks_FRAGMENT_COUNT_alone":
            return all((vd(k, "0.1", gate=gate, persist=persist, deadline=deadline)[0]
                        == "YES") == (SF[k] >= 5) for k in ALLG)
        return None

    EPS = 1e-9
    bound = {}
    for name, c in sorted(rec["claims"].items()):
        band = c["containing_gate_band_at_the_frozen_slice"]
        if band is None:
            bound[name] = {"band": None, "checked": False,
                           "note": "the primary reports no band containing the frozen gate"}
            continue
        lo, hi = band
        if claim_fn(name, INDEP_MAX) is None:
            bound[name] = {"band": band, "checked": False,
                           "note": "this checker has no independent implementation of "
                                   "the claim"}
            continue
        # probe STRICTLY inside: the band endpoints are exact-arithmetic breakpoints
        # (measured C_ab values), and the two implementations differ there by ~1e-13,
        # so `at the endpoint` is a knife edge and is reported separately, not as a
        # refutation.
        inside = [lo + EPS, 0.5 * (lo + hi), hi - EPS]
        probes = {"strictly_inside": [bool(claim_fn(name, g)) for g in inside],
                  "just_below_lower": (None if lo <= 0.005 + EPS
                                       else bool(claim_fn(name, lo - EPS))),
                  "just_above_upper": (None if hi >= 0.08 - EPS
                                       else bool(claim_fn(name, hi + EPS)))}
        endpoint = {"at_lower_endpoint": bool(claim_fn(name, lo)),
                    "at_upper_endpoint": (None if hi >= 0.08 - EPS
                                          else bool(claim_fn(name, hi)))}
        tight = (all(probes["strictly_inside"])
                 and (probes["just_below_lower"] in (None, False))
                 and (probes["just_above_upper"] in (None, False)))
        bound[name] = {"band": band, "probes": probes,
                       "exact_endpoint_knife_edge": endpoint,
                       "boundary_is_tight": bool(tight), "checked": True,
                       "endpoint_note": "the endpoints are measured C_ab values; at "
                                        "exactly the endpoint the two implementations "
                                        "can differ because their C_ab agree only to "
                                        "~1e-13, so only the strict interior is a claim"}
        if not tight:
            findings.append("REFUTED: the quoted band for '%s' is not tight (%s)"
                            % (name, probes))
    teeth["T5_claim_boundary_values_recomputed_independently"] = {
        "per_claim": bound,
        "all_tight": all(v.get("boundary_is_tight", True) for v in bound.values()),
        "fires": True}

    # the threshold boundary specifically, and where the threshold moves TO
    tb = rec["sweep"]["threshold_boundaries"]
    lo_b, hi_b = tb["lower_boundary_gate_bits"], tb["upper_boundary_gate_bits"]
    tv = {"inside": threshold_at(0.5 * (lo_b + hi_b))[:2],
          "at_lower": threshold_at(lo_b)[:2],
          "just_below_lower": threshold_at(lo_b - EPS)[:2],
          "at_upper": threshold_at(hi_b)[:2],
          "far_below": threshold_at(0.005)[:2], "far_above": threshold_at(0.08)[:2]}
    agree_below = (tb["threshold_just_below"] is None
                   or tv["just_below_lower"][0] == tb["threshold_just_below"]["threshold"])
    agree_above = (tb["threshold_just_above"] is None
                   or tv["at_upper"][0] == tb["threshold_just_above"]["threshold"])
    teeth["T6_threshold_boundary_and_where_it_moves"] = {
        "primary_band": [lo_b, hi_b], "independent": {k: list(v) for k, v in tv.items()},
        "primary_threshold_just_below": (tb["threshold_just_below"] or {}).get("threshold"),
        "primary_threshold_just_above": (tb["threshold_just_above"] or {}).get("threshold"),
        "agrees_below": bool(agree_below), "agrees_above": bool(agree_above),
        "fires": True}
    if not (agree_below and agree_above):
        findings.append("REFUTED: the threshold's destination outside the band does not "
                        "reproduce (independent %s vs primary %s/%s)"
                        % (tv, (tb["threshold_just_below"] or {}).get("threshold"),
                           (tb["threshold_just_above"] or {}).get("threshold")))

    # ---- ATTACK (ii): does the family actually separate what it claims? ----------
    sep = {}
    for k in NEWK:
        s = G[k]["stats"]
        sep[k] = {"pointer_degree": s["pointer_degree"], "max_degree": s["max_degree"],
                  "branch_count_at_pointer": s["branch_count_at_pointer"],
                  "n_fragments": s["n_fragments"],
                  "components_of_G_minus_S": s["components_of_G_minus_S"],
                  "separates_fragments_from_degree":
                      bool(s["n_fragments"] != s["pointer_degree"]),
                  "separates_maxdeg_from_degree":
                      bool(s["max_degree"] != s["pointer_degree"]),
                  "separates_components_from_degree":
                      bool(s["components_of_G_minus_S"] != s["pointer_degree"])}
    fam_frag = sorted(k for k in NEWK if sep[k]["separates_fragments_from_degree"])
    fam_max = sorted(k for k in NEWK if sep[k]["separates_maxdeg_from_degree"])
    fam_comp = sorted(k for k in NEWK if sep[k]["separates_components_from_degree"])
    idsep = sorted(k for k in NEWK
                   if G[k]["stats"]["branch_count_at_pointer"] != G[k]["stats"]["pointer_degree"])
    src_identity = bool(re.search(r'"branch_count_at_pointer": len\(rec\)', src919)
                        and re.search(r'"pointer_degree": len\(rec\)', src919))
    teeth["T7_separation_family_actually_separates"] = {
        "per_geometry": sep,
        "geometries_separating_n_fragments_from_pointer_degree": fam_frag,
        "geometries_separating_max_degree_from_pointer_degree": fam_max,
        "geometries_separating_components_from_pointer_degree": fam_comp,
        "geometries_separating_branch_count_from_pointer_degree": idsep,
        "branch_count_identity_confirmed_in_the_919_source_bytes": src_identity,
        "fires": True}
    if not fam_frag:
        findings.append("REFUTED: no geometry in the family separates n_fragments from "
                        "pointer degree")
    if not fam_max:
        findings.append("REFUTED: no geometry in the family separates max degree from "
                        "pointer degree")
    if idsep:
        findings.append("REFUTED: branch_count_at_pointer is NOT an identity -- %s" % idsep)

    # the A-family controls: identical dynamics, different partition
    ctl = {}
    for newk, oldk in (("A1", "H1"), ("A6", "G2")):
        d = {}
        for lk in ("0.05", "0.1"):
            va, _, ma, _ = vd(newk, lk)
            vb, _, mb, _ = vd(oldk, lk)
            dv = 0.0
            for ra, rb in zip(ROWS[(newk, lk)], ROWS[(oldk, lk)]):
                dv = max(dv, max(abs(x - y) for x, y in
                                 zip(sorted(ra["chi"].values()), sorted(rb["chi"].values()))))
                dv = max(dv, max(abs(x - y) for x, y in
                                 zip(sorted(ra["C"].values()), sorted(rb["C"].values()))))
            d[lk] = {"verdicts": [va, vb], "ceilings": [ma, mb], "max_abs_dev": dv,
                     "identical": bool(va == vb and ma == mb and dv < 1e-9)}
        ctl["%s_vs_%s" % (newk, oldk)] = d
    teeth["T8_A_family_controls_reproduce_the_pinned_stars"] = {
        "per_control": ctl,
        "all_identical": all(v["identical"] for d in ctl.values() for v in d.values()),
        "fires": True}
    if not all(v["identical"] for d in ctl.values() for v in d.values()):
        findings.append("REFUTED: an A-family control does not reproduce its pinned star")

    # ---- ATTACK (iii): model degeneracy on the carrying statistic ----------------
    ALL = LADDER + NEWK
    def stat(k, s):
        return (G[k]["stats"][s] if k != "G6" else G["G6"]["stats"][s])

    def cellv(k, lk):
        return vd(k, lk)[0]

    def cellc(k, lk):
        return vd(k, lk)[2]

    CAND = ["pointer_degree", "max_degree", "branch_count_at_pointer", "n_fragments",
            "components_of_G_minus_S"]
    ceil_fit = {}
    for lk in ("0.05", "0.1"):
        keys = [k for k in ALL if (k, lk) in ROWS]
        d = {}
        for s in CAND:
            hits = [k for k in keys if cellc(k, lk) == stat(k, s)]
            d[s] = {"accuracy": len(hits) / float(len(keys)), "n": len(keys),
                    "misses": sorted(set(keys) - set(hits))}
        best = max(d, key=lambda s: d[s]["accuracy"])
        ties = sorted(s for s in d if abs(d[s]["accuracy"] - d[best]["accuracy"]) < 1e-12)
        d["_best"] = best
        d["_ties"] = ties
        ceil_fit[lk] = d
    thr_fit = {}
    keys10 = [k for k in ALL if (k, "0.1") in ROWS]
    ys = {k: cellv(k, "0.1") == "YES" for k in keys10}
    for s in CAND:
        best = None
        for cut in range(0, 9):
            wrong = [k for k in keys10 if ys[k] != (stat(k, s) >= cut)]
            acc = 1.0 - len(wrong) / float(len(keys10))
            if best is None or acc > best["accuracy"]:
                best = {"cut": cut, "accuracy": acc, "counterexamples": sorted(wrong)}
        thr_fit[s] = best
    tbest = max(thr_fit, key=lambda s: thr_fit[s]["accuracy"])
    tties = sorted(s for s in thr_fit
                   if abs(thr_fit[s]["accuracy"] - thr_fit[tbest]["accuracy"]) < 1e-12)
    prim_ceiling = rec["refined_law"]["ceiling_law"]["carrying_statistic"]
    prim_thr = rec["refined_law"]["threshold_law"]["best_fitting_single_statistic"]

    # --- the primary's REFINED law is a CONJUNCTION; search conjunctions too, and
    # --- report every distinct prediction pattern that fits, not just the primary's
    atoms = [(st, c) for st in CAND for c in range(0, 9)]
    patterns = {}

    def add_pat(name, pred):
        vec = tuple(pred[k] for k in keys10)
        wrong = sorted(k for k in keys10 if pred[k] != ys[k])
        rec_ = patterns.setdefault(vec, {"accuracy": 1.0 - len(wrong) / float(len(keys10)),
                                         "wrong": wrong, "descriptions": []})
        rec_["descriptions"].append(name)

    for (st, c) in atoms:
        add_pat("%s>=%d" % (st, c), {k: stat(k, st) >= c for k in keys10})
    for (s1, c1), (s2, c2) in itertools.combinations(atoms, 2):
        if s1 == s2:
            continue
        add_pat("%s>=%d AND %s>=%d" % (s1, c1, s2, c2),
                {k: (stat(k, s1) >= c1) and (stat(k, s2) >= c2) for k in keys10})
    perfect = [v for v in patterns.values() if v["accuracy"] == 1.0]
    prim_perfect = [m["shortest_description"]
                    for m in rec["separation_family"]["model_search"]["perfect_models"]]
    conj_pred = {k: (stat(k, "pointer_degree") >= 5 and stat(k, "n_fragments") >= 3)
                 for k in keys10}
    conj_wrong = sorted(k for k in keys10 if conj_pred[k] != ys[k])
    teeth["T16_conjunctive_law_and_its_degeneracy"] = {
        "conjunction_tested": "pointer_degree >= 5 AND n_fragments >= 3",
        "independent_counterexamples": conj_wrong,
        "conjunction_fits_all": bool(not conj_wrong),
        "n_geometries": len(keys10),
        "n_distinct_patterns_searched": len(patterns),
        "n_distinct_patterns_at_100_percent": len(perfect),
        "perfect_pattern_descriptions": [min(v["descriptions"], key=len) for v in perfect],
        "primary_perfect_models": prim_perfect,
        "agrees_with_primary": bool(sorted(min(v["descriptions"], key=len)
                                           for v in perfect) == sorted(prim_perfect)),
        "unique_model": bool(len(perfect) == 1),
        "fires": True}
    if conj_wrong:
        findings.append("REFUTED: the refined conjunctive threshold law fails on %s"
                        % conj_wrong)
    if len(perfect) > 1:
        findings.append("DEGENERACY: %d distinct prediction patterns fit all %d "
                        "geometries -- the family does not single out the primary's law"
                        % (len(perfect), len(keys10)))
    if sorted(min(v["descriptions"], key=len) for v in perfect) != sorted(prim_perfect):
        findings.append("DISAGREEMENT: independent model search returns %s, primary "
                        "returns %s" % (sorted(min(v["descriptions"], key=len)
                                               for v in perfect), sorted(prim_perfect)))
    # --- the ceiling law as an EQUALITY, on independent machinery, at the low field
    ceq = {k: {"max_r_ind": cellc(k, "0.05"), "n_fragments": stat(k, "n_fragments"),
               "pointer_degree": stat(k, "pointer_degree")} for k in keys10
           if (k, "0.05") in ROWS}
    frag_hits = [k for k, v in ceq.items() if v["max_r_ind"] == v["n_fragments"]]
    deg_hits = [k for k, v in ceq.items() if v["max_r_ind"] == v["pointer_degree"]]
    teeth["T17_ceiling_equals_fragment_count_not_degree"] = {
        "n_cells": len(ceq), "fragment_count_exact_hits": len(frag_hits),
        "pointer_degree_exact_hits": len(deg_hits),
        "fragment_count_misses": sorted(set(ceq) - set(frag_hits)),
        "pointer_degree_misses": sorted(set(ceq) - set(deg_hits)),
        "separation_is_decisive": bool(len(frag_hits) == len(ceq)
                                       and len(deg_hits) < len(ceq)),
        "fires": True}
    if len(frag_hits) != len(ceq):
        findings.append("REFUTED: max R_ind does not equal the fragment count at the "
                        "frozen low field on %s" % sorted(set(ceq) - set(frag_hits)))
    degenerate = {"ceiling_ties_at_0.05": ceil_fit["0.05"]["_ties"],
                  "ceiling_ties_at_0.10": ceil_fit["0.1"]["_ties"],
                  "threshold_ties": tties}
    teeth["T9_model_degeneracy_of_the_carrying_statistic"] = {
        "ceiling_fit": {lk: {s: round(v["accuracy"], 6) for s, v in ceil_fit[lk].items()
                             if not s.startswith("_")} for lk in ceil_fit},
        "ceiling_best": {lk: ceil_fit[lk]["_best"] for lk in ceil_fit},
        "threshold_fit": {s: {"cut": v["cut"], "accuracy": round(v["accuracy"], 6),
                              "counterexamples": v["counterexamples"]}
                          for s, v in sorted(thr_fit.items())},
        "threshold_best": tbest, "ties": degenerate,
        "primary_says_ceiling_carrier": prim_ceiling,
        "primary_says_threshold_carrier": prim_thr,
        "agrees_on_ceiling": bool(prim_ceiling in ceil_fit["0.05"]["_ties"]),
        "agrees_on_threshold": bool(prim_thr in tties),
        "rival_fits_equally_well": bool(len(tties) > 1
                                        or len(ceil_fit["0.05"]["_ties"]) > 1),
        "fires": True}
    if prim_ceiling not in ceil_fit["0.05"]["_ties"]:
        findings.append("REFUTED: the primary's ceiling carrier '%s' is not among the "
                        "best-fitting statistics %s" % (prim_ceiling,
                                                        ceil_fit["0.05"]["_ties"]))
    if prim_thr not in tties:
        findings.append("REFUTED: the primary's threshold carrier '%s' is not among the "
                        "best-fitting statistics %s" % (prim_thr, tties))
    genuine_ties = [t for t in tties
                    if not (set([t, prim_thr]) <= {"pointer_degree",
                                                   "branch_count_at_pointer"})]
    if len(tties) > 1 and genuine_ties:
        findings.append("DEGENERACY: the field-ceiling threshold is fitted equally well by "
                        "%s -- the family does not resolve between them" % tties)
    elif len(tties) > 1:
        findings.append("TIE BY IDENTITY (not a degeneracy): the single-statistic fit is "
                        "tied between %s, which the frozen rule defines to be the same "
                        "variable; no geometry can separate them and the primary reports "
                        "them as an identity" % tties)

    # ---- tooth 10: the matched pairs recomputed ----------------------------------
    mp = {}
    for hi_k, lo_k in (("A2", "B1"), ("A3", "B2"), ("A4", "B3"), ("A5", "B4"),
                       ("E1", "E2")):
        d = {}
        for lk in ("0.05", "0.075", "0.1"):
            vh, _, mh, _ = vd(hi_k, lk)
            vl, _, ml, _ = vd(lo_k, lk)
            d[lk] = {"high": [vh, mh], "low": [vl, ml], "verdicts_agree": bool(vh == vl),
                     "ceilings_agree": bool(mh == ml)}
        pub = rec["separation_family"]["matched_pairs"]["%s_vs_%s" % (hi_k, lo_k)]
        ok = all(d[lk]["verdicts_agree"] == pub["per_field"][lk]["agree"]
                 for lk in ("0.05", "0.075", "0.1"))
        mp["%s_vs_%s" % (hi_k, lo_k)] = {"independent": d, "agrees_with_primary": bool(ok),
                                         "fragment_sizes_matched":
                                             sorted(G[hi_k]["stats"]["fragment_sizes"].values())
                                             == sorted(G[lo_k]["stats"]["fragment_sizes"].values())}
        if not ok:
            findings.append("REFUTED: matched pair %s/%s does not reproduce" % (hi_k, lo_k))
    teeth["T10_matched_pairs_recomputed"] = {"per_pair": mp, "fires": True}

    # ---- tooth 11: a planted wrong boundary must be refuted ----------------------
    planted = hi_b + 0.002
    t_pl, c_pl, _ = threshold_at(planted)
    teeth["T11_planted_wrong_boundary"] = {
        "planted_gate": planted, "claimed": "threshold_is_degree_5 still holds",
        "independent_threshold": t_pl, "clean": bool(c_pl),
        "refuted": bool(not (t_pl == 5 and c_pl)), "fires": bool(not (t_pl == 5 and c_pl))}
    # ---- tooth 12: a planted wrong statistic must be refuted --------------------
    planted_stat = "max_degree"
    wrong = thr_fit[planted_stat]["counterexamples"]
    teeth["T12_planted_wrong_carrying_statistic"] = {
        "planted": planted_stat, "best_accuracy": thr_fit[planted_stat]["accuracy"],
        "counterexamples": wrong, "refuted": bool(wrong), "fires": bool(wrong)}
    # ---- tooth 13: the G6 expansion re-derived from the 914 source bytes ---------
    g6ok = []
    for lam_key in ("0.05", "0.1"):
        pub = r914["measurement"]["rows"][lam_key]
        _, rows, _ = g6_from_914(r914, src914, lam_key)
        good = True
        for r, q in zip(rows, pub):
            for d in DELTAS:
                ps = [L for L in CUBE_ORDER if r["H_Z"] >= CONTENT_H_MIN
                      and r["chi"][L] >= (1.0 - d) * r["H_Z"] and r["excess"][L] >= EXCESS_MIN]
                k, _w = rind_bitmask(CUBE_ORDER, ps, r["C"], INDEP_MAX)
                good = good and (k == q["r_ind"][str(d)])
        g6ok.append(good)
    teeth["T13_G6_expansion_from_the_914_source_bytes"] = {
        "pair_class_map_size": len(pmap), "ledger_reproduced": g6ok,
        "fires": all(g6ok)}
    if not all(g6ok):
        findings.append("REFUTED: the G6 row expansion does not reproduce the pinned 914 "
                        "R_ind ledger")
    # ---- tooth 14: non-monotonicity of the verdict in the gate -------------------
    nonmono = {}
    for k in LADDER:
        for lk in (("0.05", "0.075", "0.1") if k in ("H1", "H2", "H3", "H4")
                   else ("0.05", "0.1")):
            if (k, lk) not in ROWS:
                continue
            crit = sorted({v for r in ROWS[(k, lk)] for v in r["C"].values()
                           if 0.005 < v <= 0.08})
            seq = [vd(k, lk, gate=g)[0] for g in [0.005] + crit]
            if "YES" in seq and any(seq[i] == "NO" and "YES" in seq[:i]
                                    for i in range(len(seq))):
                nonmono["%s@%s" % (k, lk)] = seq
    pub_nm = set(rec["teeth"]["T11_verdict_monotonicity_in_the_gate"][
        "cells_where_the_verdict_is_NON_monotone_in_the_gate"])
    teeth["T14_non_monotonicity_independently_reproduced"] = {
        "independent_non_monotone_cells": sorted(nonmono),
        "primary_non_monotone_cells": sorted(pub_nm),
        "agree": bool(set(nonmono) == pub_nm), "fires": True}
    if set(nonmono) != pub_nm:
        findings.append("DISAGREEMENT: non-monotone cells differ (independent %s vs "
                        "primary %s)" % (sorted(nonmono), sorted(pub_nm)))
    # ---- tooth 15: the new-family cell table --------------------------------------
    new_bad = []
    for cellkey, pubc in sorted(rec["separation_family"]["cells"].items()):
        k, lk = cellkey.split("@")
        v, ev, maxr, _ = vd(k, lk)
        if v != pubc["verdict"] or maxr != pubc["max_r_ind"]:
            new_bad.append("%s: %s/%d vs %s/%d" % (cellkey, v, maxr, pubc["verdict"],
                                                   pubc["max_r_ind"]))
    teeth["T15_separation_family_cells_reproduced"] = {
        "cells": len(rec["separation_family"]["cells"]), "disagreements": new_bad,
        "fires": True}
    if new_bad:
        findings.append("REFUTED: separation-family cells do not reproduce: %s"
                        % new_bad[:6])

    # ================================================================== output ===
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30
    out = {
        "schema": "gate-sweep-independent-check-cycle926-v1",
        "cycle": 926, "date": "2026-07-28",
        "runner": "scripts/frontier_cycle926_gate_sweep_independent_check_2026_07_28.py",
        "checks_receipt": RECEIPT,
        "primary_sha256": sha(prim_bytes),
        "primary_git_blob": git(["hash-object",
                                 os.path.join(ROOT, PRIMARY)]).stdout.decode().strip(),
        "receipt_sha256": sha(open(os.path.join(ROOT, RECEIPT), "rb").read()),
        "boundary_sentences": BOUNDARY,
        "independence": [
            "sparse Pauli-kronecker Hamiltonians", "expm_multiply interval propagation",
            "tensordot reduced states", "scipy eigvalsh('ev') spectra",
            "bitmask maximum-clique R_ind",
            "geometries rebuilt from the block spec, statistics from adjacency",
            "the partition rule re-derived from the frozen memo's bytes",
            "the G6 pair-class map read out of the 914 source bytes"],
        "attacks": {
            "i_claim_boundaries": bound,
            "ii_family_separation": sep,
            "iii_model_degeneracy": teeth["T9_model_degeneracy_of_the_carrying_statistic"],
        },
        "teeth": teeth,
        "findings": findings,
        "numerics": {"wall_s": wall, "peak_rss_gib": rss,
                     "python": platform.python_version(), "numpy": np.__version__,
                     "max_abs_dev_vs_pinned_rows": dev},
    }
    outp = os.path.join(ROOT,
                        "outputs/gate_sweep_independent_check_cycle926_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=float)

    print("CHECK-SETUP receipt=%s primary-sha=%s geometries-rebuilt=%d cells-recomputed=%d "
          "machinery=independent %s"
          % (RECEIPT, out["primary_sha256"][:16], len(G), len(ROWS), BOUNDARY_LINE))
    for nm, t in sorted(teeth.items()):
        print("TOOTH %-58s fires=%s %s"
              % (nm, t.get("fires"),
                 json.dumps({k: v for k, v in t.items()
                             if k not in ("fires", "per_geometry", "per_control",
                                          "per_pair", "per_claim", "threshold_fit")},
                            sort_keys=True, default=str)[:300] + " " + BOUNDARY_LINE))
    for nm, b in sorted(bound.items()):
        print("BOUNDARY-PROBE %-34s band=%s tight=%s probes=%s %s"
              % (nm, b.get("band"), b.get("boundary_is_tight"),
                 json.dumps(b.get("probes"), sort_keys=True), BOUNDARY_LINE))
    print("THRESHOLD-INDEPENDENT %s %s"
          % (json.dumps({k: list(v) for k, v in tv.items()}, sort_keys=True), BOUNDARY_LINE))
    for k in NEWK:
        s = sep[k]
        print("SEPARATION %-3s deg=%d maxdeg=%d branch=%d frags=%d comps=%d :: "
              "frag!=deg=%s maxdeg!=deg=%s comps!=deg=%s %s"
              % (k, s["pointer_degree"], s["max_degree"], s["branch_count_at_pointer"],
                 s["n_fragments"], s["components_of_G_minus_S"],
                 s["separates_fragments_from_degree"], s["separates_maxdeg_from_degree"],
                 s["separates_components_from_degree"], BOUNDARY_LINE))
    print("CEILING-FIT-INDEPENDENT %s %s"
          % (json.dumps({lk: {s: round(v["accuracy"], 4) for s, v in ceil_fit[lk].items()
                              if not s.startswith("_")} for lk in ceil_fit}, sort_keys=True),
             BOUNDARY_LINE))
    print("THRESHOLD-FIT-INDEPENDENT best=%s ties=%s %s %s"
          % (tbest, tties,
             json.dumps({s: {"cut": v["cut"], "acc": round(v["accuracy"], 4),
                             "wrong": v["counterexamples"]}
                         for s, v in sorted(thr_fit.items())}, sort_keys=True),
             BOUNDARY_LINE))
    nfire = sum(1 for t in teeth.values() if t.get("fires"))
    print("FINDINGS %d %s %s" % (len(findings), json.dumps(findings), BOUNDARY_LINE))
    print("CHECK-TOTAL teeth=%d/%d findings=%d wall=%.1fs rss=%.2fGiB %s"
          % (nfire, len(teeth), len(findings), wall, rss, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0)


if __name__ == "__main__":
    main()

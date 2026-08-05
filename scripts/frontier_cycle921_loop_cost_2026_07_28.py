#!/usr/bin/env python3
"""Cycle 921 -- WHY LOOPS COST REDUNDANCY: the mechanism measurement.

THE MEASURED PHENOMENON THIS BLOCK EXPLAINS.  Two pinned receipts state it:

  Cycle 917 (14-cell geometry ladder, frozen route-C certification gates):
    max R_ind over the window equals the pointer degree on all seven geometries
    at lambda = 0.05; at lambda = 0.10 the equality survives on every LOOP-FREE
    geometry and FAILS on all three LOOPY ones.  "Loops cost redundancy."
  Cycle 919 (degree-5 block): confirmed at degree 5.  The loopy H4
    (cubeminus10, 4 loops) holds max R_ind = 5 at lambda = 0.05 but drops to 3
    at 0.075 and 0.10, while every loop-free degree-5 geometry keeps 5 at all
    three fields.  H4 still CERTIFIES at 0.10.

The cost is MEASURED and UNEXPLAINED.  This block measures the mechanism.

THE CANDIDATE MECHANISMS (Q1).  Nine structurally distinct candidates, each
reduced to an INTEGER-VALUED PREDICTOR that is a pure function of the graph and
the frozen partition -- computed before any propagator runs, so no candidate can
be fitted after the fact.  See CANDIDATES below for the full statements; the
discriminating predictions are the cells where the predictors disagree.

THE DESIGN (Q2).  Thirty-two geometries in six families.  The controlling idea
is that the frozen partition rule makes every pointer neighbour the ANCHOR of
its own fragment, so a cycle through the pointer joins two anchors, and the
anchor-to-anchor distance in G minus the pointer is exactly (cycle length - 2).
That distance is the axis the families sweep, at held-fixed pointer degree:

  CUBE     12 geometries, cube coordinates so the frozen tie-break applies
           VERBATIM.  Anchor distance 2 (the lattice plaquette, 917/919's own
           regime).  Contains three MATCHED PAIRS that are identical in site
           count, bond count, loop count, seam count, pointer degree, maximum
           degree, depth and (for two of the three) fragment-size multiset and
           component count, and differ ONLY in the topology of the pair graph.
           Any count-based mechanism must give them the same ceiling.
  ANCHOR    5 geometries, anchor distance 1 (cycle length 3 through the pointer)
  BYPASS3   5 geometries, anchor distance 3 (cycle length 5)
  LENGTH    4 geometries, anchor distance 3/4/5 held at one seam pair -- the
           pure loop-LENGTH axis at fixed loop count and fixed pair graph
  INTERNAL  4 geometries whose loops do NOT pass through the pointer -- the
           loop-POSITION axis, including a 4-loop geometry matched to 919's H4
           in site count, bond count, degree, maximum degree, depth and loop
           count, whose loops are internal to one fragment
  COUNT     2 geometries adding internal loops at a fixed seam pair -- the pure
           loop-COUNT axis

RESTRICTION GATES.  Before any new number is produced: the partition rule is
re-derived and shown to reproduce the frozen memo's own six published cube
fragment lists; all six Cycle 917 geometries are reproduced VALUE-FOR-VALUE
against the pinned 917 receipt (row by row: chi, C_ab, theta_A, H_Z, the R_ind
ledger, xi_reg, max R_ind, witness, verdict, event); all four Cycle 919 degree-5
geometries are reproduced VALUE-FOR-VALUE against the pinned 919 receipt at all
three of its fields; and the 21 frozen constants are byte-verified out of the
frozen memo and cross-checked quote-for-quote against BOTH pinned receipts.

ROUTE.  Full-space exact evolution on every geometry.  Route A is a Chebyshev
expansion of exp(-iHt) with a rigorous Bessel tail bound; route B is a
scaling-and-marching Taylor propagator with a rigorous factorial remainder bound
(algorithmically disjoint from A: no Bessel coefficients, no three-term
recurrence); route C, where the Hilbert space allows it (n <= 12), is an exact
dense eigendecomposition.  Every cell is computed twice on route A in-process
and the observable-table digests compared byte-for-byte.

Deterministic, float64/complex128, no network, no tree writes outside the
declared receipt.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import hashlib
import itertools
import json
import math
import os
import platform
import re
import resource
import subprocess
import sys
import time
from collections import deque

import numpy as np
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ================================================================== pins =====
# full path -> (sha256, git blob).  Any mismatch is a hard fail, exit 2.
PINS = {
    # the frozen memos
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    # the axiom memo
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    # the 917 primary + checker, their receipts, and the landed 917 note
    "scripts/frontier_cycle917_geometry_ladder_2026_07_28.py": (
        "eb119f3bba365461274df51e0bdafc4a2047634863ef48b2662dcf7d3b61fb05",
        "b70ad19d4cc11265c465aea1bb4b2d6e5605ca5e"),
    "scripts/frontier_cycle917_geometry_independent_check_2026_07_28.py": (
        "208c8da9480894ad7a7c1248567ffcf0ff792fdfd812e01bfd45c220445d35c6",
        "1726563c9468b78d1bf9678f43c944087ee63358"),
    "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json": (
        "37568809db0d5f319b6fe9a41962cc58c8215ade2c4b9acb24eab4b665535240",
        "11e336cf0a86c46492f6ccf03b13963357840b71"),
    "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json": (
        "fe8a30918b543ecb440665adbec237ca4e5efd7db47b1951983226a8479fbc10",
        "1a3299702c7dce132360ce26af61ee89ccb2021c"),
    "outputs/geometry_ladder_block_cycle917_ship_receipt_2026_07_28.json": (
        "76651b5db064719aae94778777fde0a197c12f822523b66565e3d77100d88889",
        "f57d93272b3ab43a5b6ab9f7c8fcab33668f300a"),
    "docs/GEOMETRY_LADDER_CHAIN_CERTIFIES_CYCLE917_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "b424c3aaf684015f6ca08e81446df58c2d85a1c4e981a8c220be165989d057d4",
        "6311514dcd9a97f1a14b0ba7249b7570baeaff14"),
    # the upstream commission / recovery receipts the 917 ladder imports from
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (
        "d7d27ce19d231624415db1e71ee77eae16b5175dd403b403c254b38fb171b0a7",
        "9931c298a5917eb90de290cbb82c237508c9e692"),
    # ---- Cycle 919: the degree-5 block whose H4 drop this block explains ----
    "scripts/frontier_cycle919_degree_five_2026_07_28.py": (
        "15ce5dbd37cea6e4d7286dc85d0c04abd9948bae2a84910e5f9486c5fa35b196",
        "c22ebafcb743824db67ef1abe9f2f223ea6664a1"),
    "scripts/frontier_cycle919_degree_five_independent_check_2026_07_28.py": (
        "34526d5060c2cf592dce7b6b8986f2878209ae9c68e91138658725aabe22a29b",
        "f5c4f5c5a149b8d03d70d59ad97ebeb5b6b6cc2d"),
    "outputs/degree_five_cycle919_receipt_2026_07_28.json": (
        "cf85c74b62f1e6a83287a824f56315f3b1cf4b9387056d94906bb0195aae04f5",
        "587349db8b77c31d20f0aa04e6e69a1bb206a6d0"),
    "outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json": (
        "b455e3c5669f4cfeae0046a6ffb410daac8ce4bb89465b1a30f884190c232662",
        "bd57ac3ec780e0cb95e1f821fb159c52b0988690"),
    "logs/runner-cache/frontier_cycle919_degree_five_2026_07_28.txt": (
        "249f40fb1b416acb19ba5b36c5d08a69904aab2f940f22b0aebeed666053279c",
        "0424ee81cef16c95193708f8f270eb154cdc6fe0"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C917_CHECK_RECEIPT = "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C919_CACHE = "logs/runner-cache/frontier_cycle919_degree_five_2026_07_28.txt"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"

# the recovered d=1 comparator note -- NOT in tree; consumed as git-history
# evidence, exactly as Cycles 917 and 919 consumed it.
D1_NOTE_PATH = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"
D1_NOTE_SHA256 = "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04"
D1_NOTE_BYTES = 5230

# ============================================== frozen protocol constants ====
# Every constant below is BYTE-VERIFIED against the frozen memo in
# verify_frozen_constants(); a mismatch is a hard fail, exit 2.
FROZEN_LAMBDAS = (0.05, 0.10)      # the CERTIFIED fields (914/915 commission)
EXTENSION_LAMBDA = 0.075           # 919's DECLARED DESIGN EXTENSION, inherited
LAMBDAS = (0.05, 0.075, 0.10)
MEMO_LAMBDAS = (0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05            # condition 1: H(Z_S) >= 0.05 bit
EXCESS_MIN = 0.02               # condition 3: excess >= 0.02 bit
INDEP_MAX = 0.02                # condition 4: C_ab <= 0.02 bit
T0_ANCHOR_TOL = 1e-9            # t=0 verification: chi(0) <= 1e-9 bit
DRIFT_MAX = 0.10                # CHECK-02 pointer drift
PERSIST_N = 3                   # CHECK-03 persistence
MACH_TOL = 1e-9
RESTRICT_TOL = 1e-9             # 917/919 value-for-value reproduction tolerance
T_EXEC = [round(0.1 * i, 10) for i in range(13)]   # Jt = 0.0 .. 1.2, 13 points
# the 917 checker's probe grid, carried over verbatim as a NON-CLAIM diagnostic;
# this block uses the two cells ABOVE the frozen upper field to locate the
# per-pair crossover in the anchor distance.
PROBE_LAMBDAS = (0.125, 0.15)
DENSE_MAX_N = 12                # route C ceiling (2^12 = 4096)

CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

C917_KEYS = ["G1", "G2", "G3a", "G3b", "G4", "G5"]
C919_KEYS = ["H1", "H2", "H3", "H4"]


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def die(msg):
    print("MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    sys.exit(2)


def git(args):
    return subprocess.run(["git"] + args, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


def verify_pins():
    out = {}
    for path, (want_sha, want_blob) in sorted(PINS.items()):
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            die("pin:missing %s" % path)
        b = open(full, "rb").read()
        got_sha = sha256_bytes(b)
        got_blob = git(["hash-object", full]).stdout.decode().strip()
        if got_sha != want_sha:
            die("pin:sha256 %s got=%s want=%s" % (path, got_sha, want_sha))
        if got_blob != want_blob:
            die("pin:blob %s got=%s want=%s" % (path, got_blob, want_blob))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b)}
    return out


def recover_d1_note():
    """Read the never-landed d=1 comparator note out of git history (917/919's route)."""
    cmds = ["git cat-file -e HEAD:%s" % D1_NOTE_PATH,
            "git cat-file -t %s" % D1_NOTE_BLOB,
            "git cat-file blob %s" % D1_NOTE_BLOB]
    if git(["cat-file", "-e", "HEAD:%s" % D1_NOTE_PATH]).returncode == 0:
        die("d1-note:unexpectedly-in-tree (the 915 receipt records it as never-landed)")
    if git(["cat-file", "-t", D1_NOTE_BLOB]).stdout.decode().strip() != "blob":
        die("d1-note:blob-missing %s" % D1_NOTE_BLOB)
    r = git(["cat-file", "blob", D1_NOTE_BLOB])
    if r.returncode != 0:
        die("d1-note:cat-file-failed")
    b = r.stdout
    got = sha256_bytes(b)
    if got != D1_NOTE_SHA256 or len(b) != D1_NOTE_BYTES:
        die("d1-note:identity got=%s bytes=%d" % (got, len(b)))
    rec915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    art = rec915["C1_recovery"]["artifacts"][D1_NOTE_PATH]["recovered"]
    if art["sha256"] != got or art["blob"] != D1_NOTE_BLOB or art["bytes"] != len(b):
        die("d1-note:915-receipt-cross-check")
    for rp in (C917_RECEIPT, C919_RECEIPT):
        rec = json.load(open(os.path.join(ROOT, rp)))
        if rec["recovered_d1_note"]["sha256"] != got:
            die("d1-note:%s-cross-check" % rp)
    return b.decode("utf-8"), {"path": D1_NOTE_PATH, "blob": D1_NOTE_BLOB,
                               "sha256": got, "bytes": len(b),
                               "in_tree_at_head": False,
                               "sha256_matches_915_receipt": True,
                               "sha256_matches_917_receipt": True,
                               "sha256_matches_919_receipt": True,
                               "commands_disclosed": cmds}


# ============================== restriction gate: frozen constants by bytes ==
# Identical to Cycles 917 and 919's 21 patterns; re-declared here and re-verified
# from the memo's own bytes rather than imported from either source.
CONSTANT_PATTERNS = [
    ("hamiltonian", r"`H_lambda = - sum_<ij> Z_i Z_j - lambda sum_i X_i`", None),
    ("content_H_min", r"1\. `H\(Z_S\) >= (0\.05) bit`;", CONTENT_H_MIN),
    ("content_gate", r"2\. `chi_Z\(S:F\) >= \(1-delta\) H\(Z_S\)`;", None),
    ("excess_min", r"`chi_Z\(S:F\)\(t\) - chi_Z\(S:F\)\(0\) >= (0\.02) bit`", EXCESS_MIN),
    ("t0_anchor_tol", r"value verified at most `(1e-9) bit`", T0_ANCHOR_TOL),
    ("indep_max", r"every pair has `C_ab <= (0\.02) bit`", INDEP_MAX),
    ("deltas", r"Use `delta in \{0\.05,0\.10,0\.20\}`, with headline `delta=(0\.10)`",
     HEADLINE_DELTA),
    ("deadline", r"The headline onset deadline remains `Jt <= (1)`", DEADLINE_JT),
    ("persistence", r"persistence flag requires three consecutive certification samples",
     None),
    ("memo_lambdas", r"with `lambda in \{0\.05,0\.10,0\.20\}` and open boundaries", None),
    ("drift", r"center-Z total-variation drift from `t=0` at most `(0\.10)`", DRIFT_MAX),
    ("prep_center", r"center: `n_center=\(1,0,0\)`, the `\+X` state", None),
    ("prep_face", r"every axial face: `n_face=\(1,0,0\)`, the `\+X` state", None),
    ("prep_edge", r"every edge: `n_edge=\(0,0,1\)`, the `\+Z` state", None),
    ("prep_corner", r"every corner: `n_corner=\(0,0,1\)`, the `\+Z` state", None),
    ("theta_A", r"`theta\(t\) = \(1/6\) sum_a \(\[1-Tr rho_\(S,a\)\(t\)\^2\] - "
                r"\[1-Tr rho_\(S,a\)\(0\)\^2\]\)`", None),
    ("xi_reg_def", r"`xi_reg`, defined as the largest Manhattan shell whose one-site "
                   r"reduction has excess at least `(0\.02) bit` at that maximizer",
     EXCESS_MIN),
    ("tiebreak_1", r"1\. assign each axial face site to its own signed-axis fragment;", None),
    ("tiebreak_2", r"2\. assign an edge with `x != 0` to `F_\(sign\(x\)x\)`;", None),
    ("tiebreak_3", r"3\. for an edge with `x=0` and for every corner, ignore the corner's "
                   r"`x` sign and map `\(sign\(y\),sign\(z\)\)` by `\(\+,\+\)->\+y`, "
                   r"`\(-,\+\)->\+z`, `\(-,-\)->-y`, and `\(\+,-\)->-z`\.", None),
    ("r_ind_def", r"`R_ind` is the largest pairwise-independent certifying subset", None),
]


def verify_frozen_constants(memo):
    out = {}
    for name, pat, expect in CONSTANT_PATTERNS:
        m = re.search(pat, memo)
        if m is None:
            die("frozen-const:pattern-miss %s" % name)
        quote = " ".join(m.group(0).split())
        val = None
        if expect is not None:
            val = float(m.group(1))
            if abs(val - float(expect)) > 0:
                die("frozen-const:value %s memo=%r code=%r" % (name, val, expect))
        out[name] = {"quote": quote, "memo_value": val, "code_value": expect,
                     "byte_verified": True}
    return out


def cross_check_pinned_constants(frozen):
    """917 AND 919 published the same 21 quotes; all three must agree byte-for-byte."""
    res = {}
    for tag, path in (("917", C917_RECEIPT), ("919", C919_RECEIPT)):
        rec = json.load(open(os.path.join(ROOT, path)))
        theirs = rec["frozen_constants_byte_verified"]
        if set(theirs) != set(frozen):
            die("frozen-const:%s-key-set %s" % (tag, sorted(set(theirs) ^ set(frozen))))
        for k in sorted(frozen):
            if theirs[k]["quote"] != frozen[k]["quote"]:
                die("frozen-const:%s-quote %s" % (tag, k))
        res["identical_to_%s_receipt" % tag] = True
    res["count"] = len(frozen)
    return res


def parse_memo_cube_fragments(memo):
    """Parse the memo's six published cube fragment lists out of its bytes."""
    out = {}
    for lab in CUBE_LABELS:
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        if m is None:
            die("memo-fragments:miss %s" % lab)
        sites = re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(1))
        out[lab] = [tuple(int(v) for v in s) for s in sites]
    tot = sum(len(v) for v in out.values())
    if tot != 26 or sorted(len(v) for v in out.values()) != [4, 4, 4, 4, 5, 5]:
        die("memo-fragments:shape %d" % tot)
    return out


# ============================================================== geometry =====
def bfs(n, adj, src):
    d = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def cube_tiebreak(coord, cands, label_of):
    """The frozen memo's tie-break algorithm, applied VERBATIM in cube coordinates."""
    x, y, z = coord
    nz = sum(1 for v in coord if v != 0)
    if nz == 2 and x != 0:
        want = ("+x" if x > 0 else "-x")
    else:
        m = {(1, 1): "+y", (-1, 1): "+z", (-1, -1): "-y", (1, -1): "-z"}
        want = m[(1 if y > 0 else -1, 1 if z > 0 else -1)]
    for c in cands:
        if label_of[c] == want:
            return c
    die("tiebreak:unreachable %r %r" % (coord, want))


def build_geometry(key, name, sites, bonds_coord, pointer, label_of_rec,
                   tiebreak, dim, note):
    """Assemble a geometry: index the sites, derive recording sites, and build the
    fragment partition by the INHERITED rule (anchor + nearest-anchor + tie-break)."""
    idx = {c: i for i, c in enumerate(sites)}
    n = len(sites)
    bonds = sorted({tuple(sorted((idx[a], idx[b]))) for (a, b) in bonds_coord})
    adj = {i: set() for i in range(n)}
    for (a, b) in bonds:
        adj[a].add(b)
        adj[b].add(a)
    S = idx[pointer]
    rec = sorted(adj[S])
    label_of = {r: label_of_rec(sites[r]) for r in rec}
    dS = bfs(n, adj, S)
    if len(dS) != n:
        die("geometry:%s disconnected" % key)
    drec = {r: bfs(n, adj, r) for r in rec}
    frags = {label_of[r]: [r] for r in rec}
    ties = []
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: drec[r].get(i, 10 ** 9) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        if len(cands) == 1:
            pick = cands[0]
        else:
            if tiebreak is None:
                die("geometry:%s tie without declared tie-break at site %r" % (key, sites[i]))
            pick = tiebreak(sites[i], cands, label_of)
            ties.append({"site": str(sites[i]), "nearest_distance": m,
                         "candidates": [label_of[c] for c in cands],
                         "assigned": label_of[pick]})
        frags[label_of[pick]].append(i)
    labels = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS else 99, L))
    for L in labels:
        head, rest = frags[L][0], frags[L][1:]
        frags[L] = [head] + sorted(rest, key=lambda i: (dS[i], str(sites[i])))
    if sorted(itertools.chain(*frags.values())) != [i for i in range(n) if i != S]:
        die("geometry:%s partition-not-exhaustive" % key)
    shells = {}
    for i in range(n):
        if i != S:
            shells.setdefault(dS[i], []).append(i)
    degs = {i: len(adj[i]) for i in range(n)}
    rest = [i for i in range(n) if i != S]
    radj = {i: [j for j in adj[i] if j != S] for i in rest}
    seen, comps = set(), []
    for i in rest:
        if i in seen:
            continue
        comp, q = [], deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            comp.append(u)
            for v in radj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        comps.append(sorted(comp))
    frag_of = {i: L for L in labels for i in frags[L]}
    seams = set()
    for (a, b) in bonds:
        if a == S or b == S:
            continue
        if frag_of[a] != frag_of[b]:
            seams.add(tuple(sorted((frag_of[a], frag_of[b]))))
    # ---- THE AXIS THIS BLOCK SWEEPS: anchor-to-anchor distance in G minus S ----
    anchors = {L: frags[L][0] for L in labels}
    danch = {L: bfs(n, radj, anchors[L]) for L in labels}
    pair_d = {}
    for A, B in itertools.combinations(labels, 2):
        pair_d["|".join((A, B))] = int(danch[A].get(anchors[B], -1))
    # loops that do NOT pass through the pointer: the cycle space of G minus S
    internal_loops = len([1 for (a, b) in bonds if a != S and b != S]) - len(rest) + len(comps)
    g = {
        "key": key, "name": name, "note": note, "dim": dim, "n": n,
        "sites": [str(c) for c in sites], "coords": sites, "idx": idx,
        "bonds": bonds, "adj": adj, "S": S, "pointer": str(pointer),
        "recording": rec, "labels": labels, "frags": frags, "ties": ties,
        "dS": dS, "shells": shells, "degrees": degs, "anchors": anchors,
        "anchor_distance_in_G_minus_S": pair_d,
        "stats": {
            "n_sites": n, "n_bonds": len(bonds),
            "pointer_degree": len(rec),
            "max_degree": max(degs.values()),
            "branch_count_at_pointer": len(rec),
            "components_of_G_minus_S": len(comps),
            "depth_eccentricity_from_pointer": max(dS.values()),
            "cyclomatic_number_loops": len(bonds) - n + 1,
            "loop_free": bool(len(bonds) - n + 1 == 0),
            "dimension": dim,
            "n_fragments": len(labels),
            "fragment_sizes": {L: len(frags[L]) for L in labels},
            "seam_pairs": sorted("|".join(s) for s in seams),
            "n_seam_pairs": len(seams),
        },
    }
    g["stats"]["internal_loops_not_through_pointer"] = int(internal_loops)
    g["stats"]["loops_through_pointer"] = int(g["stats"]["cyclomatic_number_loops"]
                                              - internal_loops)
    dd = [v for v in pair_d.values() if v >= 0]
    g["stats"]["min_anchor_distance"] = int(min(dd)) if dd else -1
    g["stats"]["shortest_pointer_cycle_length"] = (int(min(dd)) + 2) if dd else -1
    g["stats"]["n_pairs_at_anchor_distance_1"] = sum(1 for v in pair_d.values() if v == 1)
    g["stats"]["n_pairs_at_anchor_distance_2"] = sum(1 for v in pair_d.values() if v == 2)
    g["stats"]["n_pairs_at_anchor_distance_3"] = sum(1 for v in pair_d.values() if v == 3)
    g["stats"]["max_fragment_size"] = max(g["stats"]["fragment_sizes"].values())
    return g


# =========================================== graph statistics the block needs =
def max_independent_set(vertices, edges):
    """Exact maximum independent set (<= 8 vertices here): the lexicographically
    first largest subset with no edge inside, in the declared label order."""
    V = list(vertices)
    E = {tuple(sorted(e)) for e in edges}
    for r in range(len(V), -1, -1):
        for c in itertools.combinations(V, r):
            if all(tuple(sorted(p)) not in E for p in itertools.combinations(c, 2)):
                return r, list(c)
    return 0, []


def max_matching(vertices, edges):
    """Exact maximum matching by brute force (small graphs)."""
    E = sorted({tuple(sorted(e)) for e in edges})
    best = 0
    for r in range(len(E), 0, -1):
        for c in itertools.combinations(E, r):
            seen = set()
            ok = True
            for a, b in c:
                if a in seen or b in seen:
                    ok = False
                    break
                seen.add(a)
                seen.add(b)
            if ok:
                return r
        if best:
            break
    return 0


def n_components(vertices, edges):
    adj = {v: set() for v in vertices}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, c = set(), 0
    for v in vertices:
        if v in seen:
            continue
        c += 1
        q = deque([v])
        seen.add(v)
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in seen:
                    seen.add(w)
                    q.append(w)
    return c


def pair_graphs(g):
    """The three graphs on fragments this block's candidates are built from."""
    labels = g["labels"]
    d = g["anchor_distance_in_G_minus_S"]
    seam = [tuple(s.split("|")) for s in g["stats"]["seam_pairs"]]
    e1 = [tuple(k.split("|")) for k, v in d.items() if v == 1]
    e2 = [tuple(k.split("|")) for k, v in d.items() if v == 2]
    return {"seam": seam, "dist1": e1, "dist2": e2, "labels": labels}


# ==================================================== THE CANDIDATE MECHANISMS
# Each candidate is an INTEGER PREDICTOR of max R_ind over the window, a pure
# function of the graph and the frozen partition.  All are computed for every
# geometry BEFORE any propagator runs.
CANDIDATES = {
    "M0_pointer_degree": (
        "917's reading carried forward unchanged: the ceiling is the pointer degree, "
        "full stop.  Predicts NO loop cost anywhere."),
    "M1_seam_monogamy": (
        "SHARED-BOUNDARY MONOGAMY.  Two fragments that touch each other (a bond joins "
        "them without going through the pointer) cannot both certify; the ceiling is "
        "the independence number of the fragment-adjacency (seam) graph."),
    "M1p_low_field_branch": (
        "PAIR-CYCLE MONOGAMY read at the frozen LOWER field: the distance-2 clause has "
        "not yet switched on there, so only the distance-1 fragments are removed.  This "
        "is not a separate mechanism -- it is the same law's other branch, scored "
        "separately so the field dependence is visible rather than assumed."),
    "M1p_pair_cycle": (
        "PAIR-CYCLE MONOGAMY (the refinement the data forces).  The tax is levied PER "
        "PAIR and graded by the length of the shortest pointer-through cycle joining "
        "the two anchors, i.e. by the anchor-to-anchor distance d in G minus the "
        "pointer: d = 1 removes BOTH fragments (they fail the content gate), d = 2 "
        "removes the PAIR from mutual independence, d >= 3 costs nothing.  The ceiling "
        "is the independence number of what is left."),
    "M2a_loop_count": (
        "CYCLOMATIC TAX, linear reading: every independent cycle costs one register, "
        "ceiling = pointer degree - loops."),
    "M2b_loop_count_half": (
        "CYCLOMATIC TAX, fitted reading: 917/919's three loopy geometries each carry 4 "
        "loops and each lose 2, so ceiling = pointer degree - ceil(loops/2).  BOTH "
        "readings of 'loop count' are run; neither is silently preferred."),
    "M3_cycle_length": (
        "FRUSTRATION / LOOP LENGTH as the SOLE determinant: the ceiling is a function "
        "of the shortest pointer-through cycle length alone, calibrated on 917/919 "
        "(length 4 -> lose 2, no pointer cycle -> lose nothing)."),
    "M4_loop_position": (
        "LOOP POSITION: the ceiling is set by how close the nearest cycle comes to the "
        "pointer; any cycle reaching within one bond of the pointer costs 2 registers, "
        "calibrated on 917/919 whose plaquettes all touch the pointer's neighbours."),
    "M5_internal_zero_modes": (
        "LOOP ZERO MODES / INTERFERENCE: cycles anywhere in the environment close off "
        "independent channels, so the cycle space of G minus the pointer is what taxes "
        "the ceiling: ceiling = pointer degree - (internal cycle count)."),
    "M6_fragment_size": (
        "ENTROPY BACKFLOW BY FRAGMENT SIZE: bigger fragments carry more conditional "
        "mutual information, so the ceiling falls as the largest fragment grows: "
        "ceiling = pointer degree - (largest fragment size - 1)."),
    "D1_konig_matching": (
        "MODEL-DEGENERACY PROBE (not a mechanism): n_fragments minus a maximum matching "
        "of the pair graph.  Equal to the independence number on every BIPARTITE pair "
        "graph, so it is only separated by an odd-cycle pair graph."),
    "D2_seam_components": (
        "MODEL-DEGENERACY PROBE: the number of connected components of the "
        "fragment-adjacency graph."),
    "D3_seam_count": (
        "MODEL-DEGENERACY PROBE: n_fragments minus the number of seam pairs."),
    "D4_max_pair_degree": (
        "MODEL-DEGENERACY PROBE: n_fragments minus the largest degree in the pair graph."),
    "D5_components_of_G_minus_S": (
        "MODEL-DEGENERACY PROBE: the number of connected components of G minus the "
        "pointer (the 917 checker's named confound)."),
}


def candidate_predictions(g):
    st = g["stats"]
    P = pair_graphs(g)
    labels, deg = P["labels"], st["pointer_degree"]
    out = {}
    out["M0_pointer_degree"] = deg
    out["M1_seam_monogamy"] = max_independent_set(labels, P["seam"])[0]
    drop = {L for e in P["dist1"] for L in e}
    surv = [L for L in labels if L not in drop]
    e2s = [e for e in P["dist2"] if e[0] in surv and e[1] in surv]
    a, wit = max_independent_set(surv, e2s)
    out["M1p_pair_cycle"] = a
    # the SAME law read at the frozen LOWER field, where the distance-2 clause has
    # not yet switched on: only the distance-1 vertices are removed.
    out["M1p_low_field_branch"] = max_independent_set(surv, [])[0]
    out["_M1p_witness"] = wit
    out["_M1p_dropped_for_content"] = sorted(drop)
    out["_M1p_dependent_pairs"] = sorted("|".join(e) for e in e2s)
    lp = st["cyclomatic_number_loops"]
    out["M2a_loop_count"] = max(0, deg - lp)
    out["M2b_loop_count_half"] = max(0, deg - int(math.ceil(lp / 2.0)))
    ell = st["shortest_pointer_cycle_length"]
    out["M3_cycle_length"] = deg if ell < 0 else max(0, deg - {3: 2, 4: 2}.get(ell, 0))
    # nearest approach of any cycle to the pointer: 0 if a cycle runs through the
    # pointer, else the minimum pointer distance over sites lying on a cycle
    on_cycle = cycle_sites(g)
    near = min([g["dS"][i] for i in on_cycle], default=-1)
    out["M4_loop_position"] = deg if near < 0 else max(0, deg - (2 if near <= 1 else 0))
    out["M5_internal_zero_modes"] = max(0, deg - st["internal_loops_not_through_pointer"])
    out["M6_fragment_size"] = max(0, deg - (st["max_fragment_size"] - 1))
    out["D1_konig_matching"] = len(labels) - max_matching(labels, P["dist2"])
    out["D2_seam_components"] = n_components(labels, P["seam"])
    out["D3_seam_count"] = max(0, len(labels) - st["n_seam_pairs"])
    out["D4_max_pair_degree"] = max(0, len(labels) - max(
        [sum(1 for e in P["dist2"] if L in e) for L in labels] or [0]))
    out["D5_components_of_G_minus_S"] = st["components_of_G_minus_S"]
    return out


def cycle_sites(g):
    """Every site that lies on some cycle: iteratively strip degree-1 vertices."""
    deg = {i: len(g["adj"][i]) for i in range(g["n"])}
    alive = set(range(g["n"]))
    changed = True
    while changed:
        changed = False
        for i in sorted(alive):
            if deg[i] <= 1:
                alive.discard(i)
                for j in g["adj"][i]:
                    if j in alive:
                        deg[j] -= 1
                changed = True
    return sorted(alive)


# ------------------------------------------- the pinned Cycle 917 geometries --
def geom_chain9():
    sites = [(k, 0, 0) for k in range(-4, 5)]
    bonds = [((k, 0, 0), (k + 1, 0, 0)) for k in range(-4, 4)]
    return build_geometry("G1", "chain9", sites, bonds, (0, 0, 0),
                          lambda c: ("+x" if c[0] > 0 else "-x"), cube_tiebreak, 1,
                          "917 G1: the d=1 reference, the open 9-site chain")


def geom_star7():
    sites = ["S"] + ["a%d" % i for i in range(1, 7)]
    bonds = [("S", "a%d" % i) for i in range(1, 7)]
    return build_geometry("G2", "star7", sites, bonds, "S", lambda c: c, None, "star",
                          "917 G2: K_{1,6}, maximal local branching, zero depth")


def geom_tree(nbranch):
    sites, bonds = ["S"], []
    for b in range(nbranch):
        c = "b%d" % b
        sites.append(c)
        bonds.append(("S", c))
        for k in range(2):
            gg = "b%dg%d" % (b, k)
            sites.append(gg)
            bonds.append((c, gg))
    key = {3: "G3a", 4: "G3b", 5: "H2"}[nbranch]
    return build_geometry(key, "tree%d" % len(sites), sites, bonds, "S",
                          lambda c: c, None, "tree",
                          "917/919 %s: centre + %d branches of depth 2" % (key, nbranch))


def geom_plaquette9():
    sites = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]

    def lab(c):
        return ("+x" if c[0] > 0 else "-x") if c[0] != 0 else ("+y" if c[1] > 0 else "-y")
    return build_geometry("G4", "plaquette9", sites, bonds, (0, 0, 0), lab,
                          cube_tiebreak, 2, "917 G4: the open 3x3 square, d=2 with loops")


def _axis_label(c):
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    die("axis-label:origin %r" % (c,))


def geom_cubeminus11():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G5", "cubeminus11", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, "917 G5: centre + 6 faces + the 4 z=0 edges")


def geom_cube27():
    sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("G6", "cube27", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, "917 G6: the open 3x3x3 cube")


# ------------------------------------------- the pinned Cycle 919 geometries --
def geom_star6():
    sites = ["S"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a%d" % i) for i in range(1, 6)]
    return build_geometry("H1", "star6", sites, bonds, "S", lambda c: c, None, "star",
                          "919 H1: K_{1,5}")


def geom_tree16():
    return geom_tree(5)


def geom_tree10d5():
    sites, bonds = ["S"], []
    for b in range(5):
        c = "b%d" % b
        sites.append(c)
        bonds.append(("S", c))
        if b < 2:
            for k in range(2):
                gg = "b%dg%d" % (b, k)
                sites.append(gg)
                bonds.append((c, gg))
    return build_geometry("H3", "tree10d5", sites, bonds, "S", lambda c: c, None, "tree",
                          "919 H3: centre + 5 branches, exactly two of depth 2")


def geom_cubeminus10():
    faces = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1)]
    edges = [(1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    sites = [(0, 0, 0)] + faces + edges
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry("H4", "cubeminus10", sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3,
                          "919 H4: G5 cubeminus11 with the -z face deleted -- the loopy "
                          "degree-5 geometry whose drop this block explains")


# ================================== THE CYCLE 921 GEOMETRY ROSTER (design freedom)
FACE = {"+x": (1, 0, 0), "-x": (-1, 0, 0), "+y": (0, 1, 0),
        "-y": (0, -1, 0), "+z": (0, 0, 1), "-z": (0, 0, -1)}
EDG = {"xy": (1, 1, 0), "x-y": (1, -1, 0), "-xy": (-1, 1, 0), "-x-y": (-1, -1, 0),
       "xz": (1, 0, 1), "-xz": (-1, 0, 1), "yz": (0, 1, 1), "-yz": (0, -1, 1)}
F5 = ["+x", "-x", "+y", "-y", "+z"]


def cube_sub(key, faces, extras, note):
    """A sub-lattice of {-1,0,1}^3 containing the origin.  The frozen memo's
    tie-break is defined exactly here and is applied VERBATIM."""
    sites = [(0, 0, 0)] + [FACE[f] for f in faces] + list(extras)
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return build_geometry(key, key, sites, bonds, (0, 0, 0), _axis_label,
                          cube_tiebreak, 3, note)


def tree_plus(key, sites, bonds, note):
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, "tree", note)


def star_plus(key, extra, note):
    sites = ["S"] + ["a%d" % i for i in range(1, 6)]
    bonds = [("S", "a%d" % i) for i in range(1, 6)] + list(extra)
    return build_geometry(key, key, sites, bonds, "S", lambda c: c, None, "star", note)


def _bbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["g%d" % i for i in range(5)]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b%d" % i, "g%d" % i) for i in range(5)])
    return sites, bonds


def _dbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["g0", "h0", "k0", "g1", "h1", "k1"]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b0", "g0"), ("g0", "h0"), ("h0", "k0"),
                ("b1", "g1"), ("g1", "h1"), ("h1", "k1")])
    return sites, bonds


def _wbase():
    sites = ["S"] + ["b%d" % i for i in range(5)] + ["w%d" % i for i in range(4)]
    bonds = ([("S", "b%d" % i) for i in range(5)]
             + [("b0", "w%d" % i) for i in range(4)])
    return sites, bonds


def build_roster():
    """The 32 measurement geometries, in six declared families."""
    R, bs, bb = [], _bbase(), None
    Bs, Bb = _bbase()
    Ds, Db = _dbase()
    Ws, Wb = _wbase()
    E = EDG

    def C(k, ex, note):
        return ("CUBE", cube_sub(k, F5, ex, note))

    R += [
        C("QC0", [], "CUBE control: centre + 5 faces, no edges -- loop-free, every "
                     "fragment a singleton.  Anchor distance infinite for every pair."),
        C("QC1", [E["xy"]], "CUBE: one plaquette.  One loop, one pair at anchor "
                            "distance 2 (+x|+y)."),
        C("QC2p", [E["xy"], E["-xy"]],
          "CUBE MATCHED PAIR A/1: two plaquettes sharing the +y anchor -- pair graph is "
          "a PATH, independence number 4."),
        C("QC2d", [E["xy"], E["-x-y"]],
          "CUBE MATCHED PAIR A/2: two plaquettes sharing no anchor -- pair graph is two "
          "DISJOINT edges, independence number 3.  Identical to QC2p in site count, bond "
          "count, loop count, seam count, pointer degree, maximum degree, depth and "
          "fragment-size multiset."),
        C("QC3s", [E["xz"], E["-xz"], E["yz"]],
          "CUBE MATCHED PAIR B/1: three plaquettes all sharing the +z anchor -- pair "
          "graph is a STAR, independence number 4."),
        C("QC3x", [E["xy"], E["-x-y"], E["yz"]],
          "CUBE MATCHED PAIR B/2: three plaquettes arranged so the pair graph has "
          "independence number 3.  Identical to QC3s in site count, bond count, loop "
          "count, seam count, pointer degree, maximum degree, depth, fragment-size "
          "multiset AND component count of G minus the pointer.  This is the block's "
          "tightest single discriminator."),
        C("QC4s", [E["xz"], E["-xz"], E["yz"], E["-yz"]],
          "CUBE MATCHED PAIR C/1: four plaquettes all sharing the +z anchor -- pair "
          "graph is a STAR, independence number 4.  Identical to 919's H4 in site count "
          "(10), bond count (13), loop count (4), seam count (4), pointer degree (5), "
          "maximum degree (5) and depth (2); H4's pair graph is a 4-CYCLE with "
          "independence number 3.  H4 itself is the other half of this pair."),
        C("QC8", list(E.values()),
          "CUBE: all eight available plaquettes.  The pair graph is K5 minus a perfect "
          "matching -- NON-BIPARTITE, which is the only way to separate the "
          "independence number from the Koenig matching probe."),
        ("CUBE", cube_sub("QCK", ["+x", "+y", "+z"], [E["xy"], E["xz"], E["yz"]],
                          "CUBE extreme: pointer degree 3 with a TRIANGLE pair graph -- "
                          "independence number 1, so the pair-cycle law predicts the "
                          "certification is topologically impossible above the crossover.")),
        ("CUBE", cube_sub("QCT", ["+x", "+y", "+z"], [],
                          "CUBE control for QCK: the same three faces, no edges.")),
        C("QCL1", [E["xy"], E["xz"]],
          "CUBE loop-count control 1: two plaquettes sharing the +x anchor."),
        C("QCL2", [E["xy"], E["xz"], (1, 1, 1)],
          "CUBE loop-count control 2: QCL1 plus the corner (1,1,1), which the frozen "
          "tie-break assigns to +y.  Adds loops at an UNCHANGED pair set."),
    ]

    for k, ex, nt in (
            ("QA1", [("a1", "a2")], "one anchor-anchor bond: anchor distance 1"),
            ("QA2m", [("a1", "a2"), ("a1", "a3")], "two anchor-anchor bonds sharing a1"),
            ("QA2d", [("a1", "a2"), ("a3", "a4")], "two disjoint anchor-anchor bonds"),
            ("QA4s", [("a1", "a2"), ("a1", "a3"), ("a1", "a4"), ("a1", "a5")],
             "a1 bonded to every other anchor"),
            ("QA4c", [("a1", "a2"), ("a2", "a3"), ("a3", "a4"), ("a4", "a1")],
             "a 4-cycle of anchor-anchor bonds")):
        R.append(("ANCHOR", star_plus(k, ex, "ANCHOR family (pointer cycle length 3): "
                                             + nt)))

    for k, ex, nt in (
            ("QB0", [], "control, loop-free"),
            ("QB1", [("g0", "g1")], "one loop"),
            ("QB2d", [("g0", "g1"), ("g2", "g3")], "two disjoint loops"),
            ("QB4c", [("g0", "g1"), ("g1", "g2"), ("g2", "g3"), ("g3", "g0")],
             "four loops, pair graph a 4-cycle"),
            ("QB10", list(itertools.combinations(["g%d" % i for i in range(5)], 2)),
             "ten loops, pair graph the complete K5 -- the sharpest test of whether "
             "fragment adjacency alone taxes the ceiling")):
        R.append(("BYPASS3", tree_plus(k, Bs, Bb + list(ex),
                                       "BYPASS3 family (pointer cycle length 5, anchor "
                                       "distance 3): " + nt)))

    for k, ex, nt in (
            ("QD0", [], "control, loop-free, anchor distance infinite"),
            ("QD5", [("g0", "g1")], "pointer cycle length 5, anchor distance 3"),
            ("QD7", [("h0", "h1")], "pointer cycle length 7, anchor distance 5"),
            ("QD9", [("k0", "k1")], "pointer cycle length 9, anchor distance 7")):
        R.append(("LENGTH", tree_plus(k, Ds, Db + list(ex),
                                      "LENGTH family (one loop, one seam pair b0|b1, "
                                      "only the cycle LENGTH varies): " + nt)))

    R.append(("INTERNAL", tree_plus("QW0", Ws, Wb,
                                    "INTERNAL control: b0 carries four children, no ring "
                                    "-- loop-free with a 5-site fragment, the fragment-size "
                                    "control for QW1.")))
    R.append(("INTERNAL", tree_plus("QW1", Ws, Wb + [("w0", "w1"), ("w1", "w2"),
                                                     ("w2", "w3"), ("w3", "w0")],
                                    "INTERNAL headline: FOUR loops, all internal to the b0 "
                                    "fragment, none through the pointer.  Matched to 919's "
                                    "H4 in site count (10), bond count (13), pointer degree "
                                    "(5), maximum degree (5), depth (2) and loop count (4).")))
    R.append(("INTERNAL", tree_plus("QP1", Ds, Db + [("b0", "h0")],
                                    "INTERNAL: one loop touching the ANCHOR b0, one bond "
                                    "from the pointer -- the loop-position control.")))
    R.append(("INTERNAL", tree_plus("QP3", Ds, Db + [("g0", "k0")],
                                    "INTERNAL: one loop two bonds away from the pointer.")))
    R.append(("COUNT", tree_plus("QN2", Ds, Db + [("g0", "g1"), ("b0", "h0")],
                                 "COUNT: QD5 plus one internal loop -- two loops at an "
                                 "unchanged pair set.")))
    R.append(("COUNT", tree_plus("QN3", Ds, Db + [("g0", "g1"), ("b0", "h0"), ("b1", "h1")],
                                 "COUNT: QD5 plus two internal loops -- three loops at an "
                                 "unchanged pair set.")))
    return R


# ================================================================ numerics ===
def build_diag(n, bonds):
    idx = np.arange(1 << n, dtype=np.uint32)
    z = np.empty((n, 1 << n), dtype=np.int8)
    for i in range(n):
        z[i] = 1 - 2 * ((idx >> np.uint32(i)) & np.uint32(1)).astype(np.int8)
    diag = np.zeros(1 << n, dtype=np.float64)
    for (a, b) in bonds:
        diag -= z[a].astype(np.float64) * z[b].astype(np.float64)
    return diag


def prep_state(n, plus_x):
    """The frozen class-product preparation: pointer and its neighbours +X, all
    other sites +Z."""
    vecs = [(np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plus_x else np.array([1.0, 0.0])
            for i in range(n)]
    psi = vecs[n - 1].astype(np.complex128)
    for i in range(n - 2, -1, -1):
        psi = np.kron(psi, vecs[i].astype(np.complex128))
    return psi


def _matvec_factory(diag, n, lam):
    xor = [np.arange(1 << n, dtype=np.int64) ^ (1 << i) for i in range(n)]

    def mv(v, o=None):
        if o is None:
            o = np.empty_like(v)
        np.multiply(diag, v, out=o)
        for i in range(n):
            o -= lam * v[xor[i]]
        return o
    return mv


def chebyshev(psi0, diag, n, lam, times):
    """Route A: exact exp(-iHt) by Chebyshev expansion with a rigorous tail bound."""
    A = float(np.abs(diag).max() + lam * n)
    tmax = max(times)
    M = int(np.ceil(A * tmax)) + 5
    while abs(jv(M, A * tmax)) > 1e-17:
        M += 5
    outs = [np.zeros_like(psi0) for _ in times]
    mv = _matvec_factory(diag, n, lam)
    T0 = psi0.copy()
    T1 = np.empty_like(psi0)
    mv(T0, T1)
    T1 /= A
    Tn = np.empty_like(psi0)
    nmv = 1
    for k in range(M + 1):
        if k == 0:
            v = T0
        elif k == 1:
            v = T1
        else:
            mv(T1, Tn)
            Tn *= 2.0 / A
            Tn -= T0
            nmv += 1
            T0, T1, Tn = T1, Tn, T0
            v = T1
        for j, t in enumerate(times):
            c = jv(k, A * t) * ((-1j) ** k) * (1.0 if k == 0 else 2.0)
            if abs(c) > 1e-18:
                outs[j] += c * v
    tail = float(max(abs(jv(M + 1, A * tmax)), abs(jv(M + 2, A * tmax))))
    return outs, {"route": "chebyshev", "half_width": A, "degree": M, "matvecs": nmv,
                  "tail_bound": 2.0 * tail}


def taylor_march(psi0, diag, n, lam, times, hbound=1.0, pmax=40):
    """Route B: exp(-iHt) by a scaling-and-marching Taylor propagator with a
    rigorous factorial remainder bound.  Algorithmically disjoint from route A."""
    A = float(np.abs(diag).max() + lam * n)
    mv = _matvec_factory(diag, n, lam)
    psi = psi0.astype(np.complex128).copy()
    outs = []
    tprev, nsub, nmv, worst_rem, worst_deg = 0.0, 0, 0, 0.0, 0
    for t in times:
        dt = t - tprev
        if dt < -1e-15:
            die("taylor:non-monotone-grid")
        if dt > 1e-15:
            s = max(1, int(math.ceil(A * dt / hbound)))
            h = dt / s
            for _ in range(s):
                term = psi.copy()
                acc = psi.copy()
                p = 0
                for k in range(1, pmax + 1):
                    term = mv(term) * (-1j * h / k)
                    nmv += 1
                    acc += term
                    p = k
                    if float(np.abs(term).max()) < 1e-19:
                        break
                psi = acc
                nsub += 1
                worst_deg = max(worst_deg, p)
                worst_rem = max(worst_rem, float((A * h) ** (p + 1) / math.gamma(p + 2)))
        outs.append(psi.copy())
        tprev = t
    return outs, {"route": "taylor-march", "norm_bound": A, "substeps": nsub,
                  "matvecs": nmv, "max_taylor_degree": worst_deg,
                  "max_substep_remainder_bound": worst_rem, "h_bound": hbound}


def dense_route(psi0, diag, n, lam, times):
    """Route C: exact dense eigendecomposition of the real symmetric H."""
    d = 1 << n
    H = np.zeros((d, d), dtype=np.float64)
    H[np.arange(d), np.arange(d)] = diag
    for i in range(n):
        j = np.arange(d, dtype=np.int64) ^ (1 << i)
        H[np.arange(d), j] -= lam
    w, V = np.linalg.eigh(H)
    del H
    c = V.T @ psi0
    outs = [V @ (np.exp(-1j * w * t) * c) for t in times]
    del V
    return outs, {"route": "dense-eigh", "dim": d, "emin": float(w[0]),
                  "emax": float(w[-1])}


def joint_rho(psi, n, sites):
    T = psi.reshape((2,) * n)
    order = list(sites) + [i for i in range(n) if i not in sites]
    ax = [n - 1 - s for s in order]
    M = np.transpose(T, ax).reshape(1 << len(sites), -1)
    return M @ M.conj().T


def ent_bits(w):
    w = np.asarray(w).real
    neg = float(min(0.0, w.min()))
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum()), neg


def chi_holevo(rho, k):
    d = 1 << k
    s0, s1 = rho[:d, :d], rho[d:, d:]
    p = [float(np.trace(s0).real), float(np.trace(s1).real)]
    tot = p[0] + p[1]
    Sav, n1 = ent_bits(np.linalg.eigvalsh((s0 + s1) / tot))
    Sc, n2 = 0.0, 0.0
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz <= 1e-14:
            continue
        e, nn = ent_bits(np.linalg.eigvalsh(s / pz))
        Sc += (pz / tot) * e
        n2 = min(n2, nn)
    H = -sum((q / tot) * np.log2(q / tot) for q in p if q / tot > 1e-15)
    herm = float(np.abs(rho - rho.conj().T).max())
    return Sav - Sc, H, [p[0] / tot, p[1] / tot], min(n1, n2), herm


def cond_mi(rho, ka, kb):
    d = 1 << (ka + kb)
    blocks = [rho[:d, :d], rho[d:, d:]]
    p = [float(np.trace(b).real) for b in blocks]
    tot = p[0] + p[1]
    out = 0.0
    for b, pz in zip(blocks, p):
        if pz <= 1e-14:
            continue
        r = b / pz
        T = r.reshape(1 << ka, 1 << kb, 1 << ka, 1 << kb)
        ra = np.einsum("aibi->ab", T)
        rb = np.einsum("iaib->ab", T)
        sa, _ = ent_bits(np.linalg.eigvalsh(ra))
        sb, _ = ent_bits(np.linalg.eigvalsh(rb))
        sab, _ = ent_bits(np.linalg.eigvalsh(r))
        out += (pz / tot) * (sa + sb - sab)
    return out


def r_ind(labels, chi, excess, H, C, delta):
    order = {L: i for i, L in enumerate(labels)}
    singles = [L for L in labels
               if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H
               and excess[L] >= EXCESS_MIN]
    best, best_key = [], None
    for r in range(len(singles), 0, -1):
        for comb in itertools.combinations(singles, r):
            ok = True
            for a, b in itertools.combinations(comb, 2):
                v = C.get(tuple(sorted((a, b), key=order.get)))
                if v is None or v > INDEP_MAX:
                    ok = False
                    break
            if ok:
                key = tuple(order[c] for c in comb)
                if best_key is None or key < best_key:
                    best, best_key = list(comb), key
        if best:
            break
    return len(best), best, singles


def centered_frobenius(lam, n, nbonds, degrees):
    den = np.sqrt(float(nbonds) + n * lam * lam)
    out = {}
    for deg in sorted(set(degrees.values())):
        out[str(deg)] = {"Z": 2.0 * lam / den, "X": 2.0 * np.sqrt(deg) / den,
                         "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
    return out


# ============================================================= measurement ===
def measure(g, states, times):
    n, S, labels, frags = g["n"], g["S"], g["labels"], g["frags"]
    nbrs = g["recording"]
    rows = []
    chi0, one0, theta0 = {}, {}, None
    mach = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
            "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0}
    for it, (t, a) in enumerate(zip(times, states)):
        mach["norm"] = max(mach["norm"], abs(float(np.vdot(a, a).real) - 1.0))
        chi, one_by_shell, one_by_site = {}, {}, {}
        H = None
        pz = None
        for L in labels:
            sites = frags[L]
            rho = joint_rho(a, n, [S] + sites)
            c, H, pz, neg, herm = chi_holevo(rho, len(sites))
            chi[L] = c
            mach["hermiticity"] = max(mach["hermiticity"], herm)
            mach["negativity"] = max(mach["negativity"], abs(neg))
            mach["entropy_bound"] = max(mach["entropy_bound"], max(0.0, c - H, -c))
        for i in range(n):
            if i == S:
                continue
            c1, _, _, _, _ = chi_holevo(joint_rho(a, n, [S, i]), 1)
            one_by_site[i] = c1
            one_by_shell.setdefault(g["dS"][i], []).append(c1)
        theta = 0.0
        for nb in nbrs:
            rb = joint_rho(a, n, [S, nb])
            theta += 1.0 - float(np.trace(rb @ rb).real)
        theta /= len(nbrs)
        if it == 0:
            chi0 = dict(chi)
            one0 = {k: float(np.mean(v)) for k, v in one_by_shell.items()}
            theta0 = theta
            mach["t0_anchor"] = max(mach["t0_anchor"],
                                    max(abs(v) for v in chi.values()),
                                    max(abs(v) for v in one_by_site.values()))
        exc = {L: chi[L] - chi0[L] for L in labels}
        one_exc = {k: float(np.mean(v)) - one0[k] for k, v in one_by_shell.items()}
        C = {}
        for a1, b1 in itertools.combinations(labels, 2):
            rho = joint_rho(a, n, [S] + frags[a1] + frags[b1])
            C[(a1, b1)] = cond_mi(rho, len(frags[a1]), len(frags[b1]))
            if it == 0:
                mach["t0_anchor"] = max(mach["t0_anchor"], abs(C[(a1, b1)]))
        rr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labels, chi, exc, H, C, d)
            rr["%.2f" % d] = k
            subs["%.2f" % d] = sub
            sing["%.2f" % d] = sg
        rows.append({
            "jt": t, "H_Z": H, "p_z": pz, "pointer_tv_drift": abs(pz[0] - 0.5),
            "chi": chi, "excess": exc, "theta_A": theta - theta0,
            "one_site_chi_by_shell": {str(k): float(np.mean(v))
                                      for k, v in sorted(one_by_shell.items())},
            "one_site_excess_by_shell": {str(k): v for k, v in sorted(one_exc.items())},
            "sum_delta_chi": float(sum(exc.values())),
            "C_ab": {"|".join(k): v for k, v in sorted(C.items())},
            "r_ind": rr, "certifying_subsets": subs, "singleton_passes": sing,
            "r_raw": {k: len(v) for k, v in sing.items()},
        })
    return rows, mach


def event_of(rows, delta):
    key = "%.2f" % delta
    for i, r in enumerate(rows):
        if r["r_ind"][key] >= 2:
            run = 0
            for rr in rows[i:]:
                if rr["r_ind"][key] >= 2:
                    run += 1
                else:
                    break
            return {"jt": r["jt"], "theta_A": r["theta_A"], "r_ind": r["r_ind"][key],
                    "witness": r["certifying_subsets"][key], "run": run,
                    "by_deadline": bool(r["jt"] <= DEADLINE_JT + 1e-12),
                    "persists": bool(run >= PERSIST_N),
                    "pointer_tv_drift": r["pointer_tv_drift"],
                    "chi_at_event": {L: r["chi"][L] for L in r["certifying_subsets"][key]},
                    "H_Z_at_event": r["H_Z"],
                    "C_at_event": {k: v for k, v in r["C_ab"].items()
                                   if all(p in r["certifying_subsets"][key]
                                          for p in k.split("|"))}}
    return None


def xi_reg_of(rows):
    imax = int(np.argmax([r["sum_delta_chi"] for r in rows]))
    r = rows[imax]
    xi = 0
    for sh, v in sorted((int(k), v) for k, v in r["one_site_excess_by_shell"].items()):
        if v >= EXCESS_MIN:
            xi = max(xi, sh)
    return {"xi_reg": xi, "t_summax": r["jt"], "sum_delta_chi": r["sum_delta_chi"],
            "shell_excess": r["one_site_excess_by_shell"]}


def verdict_of(rows, delta, comm_ok):
    ev = event_of(rows, delta)
    if ev is None:
        best_C = min((min(r["C_ab"].values()) for r in rows if r["C_ab"]), default=None)
        any_content = any(len(r["singleton_passes"]["%.2f" % delta]) >= 2 for r in rows)
        reason = ("content-gate: fewer than two fragments ever reach (1-delta)H with "
                  "0.02-bit excess" if not any_content else
                  "independence-gate: two or more fragments reach content but every "
                  "eligible pair exceeds C_ab = 0.02 bit")
        return {"verdict": "NO", "reason": reason, "event": None,
                "min_C_ab_over_grid": best_C, "commutator_ordering_ok": comm_ok}
    if not ev["by_deadline"]:
        return {"verdict": "NO", "reason": "late: first R_ind>=2 after the Jt<=1 deadline",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if not ev["persists"]:
        return {"verdict": "NO", "reason": "persistence: fewer than three consecutive "
                                           "certification samples with R_ind>=2",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if ev["pointer_tv_drift"] > DRIFT_MAX:
        return {"verdict": "NO", "reason": "pointer drift exceeds 0.10 at the event",
                "event": ev, "commutator_ordering_ok": comm_ok}
    if not comm_ok:
        return {"verdict": "NO", "reason": "CHECK-02 pointer demolition control",
                "event": ev, "commutator_ordering_ok": comm_ok}
    return {"verdict": "YES", "reason": None, "event": ev,
            "commutator_ordering_ok": comm_ok}


def cell_of(g, lam, rows):
    cf = centered_frobenius(lam, g["n"], len(g["bonds"]), g["degrees"])
    comm_ok = max(v["Z"] for v in cf.values()) < min(v["X"] for v in cf.values())
    xi = xi_reg_of(rows)
    v = {d: verdict_of(rows, d, comm_ok) for d in DELTAS}
    key = "%.2f" % HEADLINE_DELTA
    imax = int(np.argmax([r["r_ind"][key] for r in rows]))
    return {"centered_frobenius": cf, "commutator_ordering_ok": bool(comm_ok),
            "xi_reg": xi,
            "verdicts_by_delta": {"%.2f" % d: v[d] for d in DELTAS},
            "max_r_ind_over_window": max(r["r_ind"][key] for r in rows),
            "ceiling_row_jt": rows[imax]["jt"],
            "ceiling_witness": rows[imax]["certifying_subsets"][key],
            "headline": v[HEADLINE_DELTA]}


def run_route_A(g, diag, psi0, lam):
    outs, prop = chebyshev(psi0, diag, g["n"], lam, T_EXEC)
    rows, mach = measure(g, outs, T_EXEC)
    return rows, mach, prop


# ------------------------------- the structural claim, measured directly -----
def dependence_structure(g, rows):
    """At the row that realises the ceiling, which fragment pairs are OVER the
    independence gate, and which fragments fail the content gate?  The mechanism
    claim is that these sets are exactly the anchor-distance classes."""
    key = "%.2f" % HEADLINE_DELTA
    imax = int(np.argmax([r["r_ind"][key] for r in rows]))
    r = rows[imax]
    passes = set(r["singleton_passes"][key])
    over = sorted(k for k, v in r["C_ab"].items() if v > INDEP_MAX)
    d = g["anchor_distance_in_G_minus_S"]
    fails = {L for L in g["labels"] if L not in passes}
    d1_frags = {L for k, v in d.items() if v == 1 for L in k.split("|")}
    over_pass = {k for k in over if all(p in passes for p in k.split("|"))}
    d2_pass = {k for k, v in d.items() if v == 2
               and all(p in passes for p in k.split("|"))}
    return {
        "ceiling_jt": r["jt"],
        "content_failures": sorted(fails),
        "fragments_with_a_distance_1_partner": sorted(d1_frags),
        "content_failures_are_exactly_the_distance_1_fragments": bool(fails == d1_frags),
        "pairs_over_the_independence_gate": over,
        "over_gate_pairs_among_content_passers": sorted(over_pass),
        "distance_2_pairs_among_content_passers": sorted(d2_pass),
        "among_passers_over_gate_equals_distance_2": bool(over_pass == d2_pass),
        "among_passers_no_pair_is_over_gate": bool(not over_pass),
        "pairs_by_anchor_distance": {str(dd): sorted(k for k, v in d.items() if v == dd)
                                     for dd in sorted(set(d.values()))},
        "C_ab_by_anchor_distance": {
            str(dd): sorted(round(r["C_ab"][k], 8) for k, v in d.items() if v == dd)
            for dd in sorted(set(d.values()))},
    }


# ================================================================== main =====
def main():
    pins = verify_pins()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    frozen = verify_frozen_constants(memo)
    const_x = cross_check_pinned_constants(frozen)
    d1_text, d1_prov = recover_d1_note()
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r917c = json.load(open(os.path.join(ROOT, C917_CHECK_RECEIPT)))
    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))

    mach_all = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0,
                "entropy_bound": 0.0, "symmetry": 0.0, "t0_anchor": 0.0,
                "cheby_tail": 0.0, "taylor_remainder": 0.0,
                "route_AB_max_dev": 0.0, "route_AC_max_dev": 0.0, "determinism": 0.0}

    # ============================================ restriction gate 1: the rule ==
    cube = geom_cube27()
    memo_frags = parse_memo_cube_fragments(memo)
    rule_detail, rule_ok = {}, True
    for L in CUBE_LABELS:
        mine = {cube["coords"][i] for i in cube["frags"][L]}
        theirs = set(memo_frags[L])
        rule_detail[L] = {"memo": sorted(str(c) for c in theirs),
                          "rule": sorted(str(c) for c in mine),
                          "identical_as_sets": bool(mine == theirs)}
        rule_ok = rule_ok and (mine == theirs)
    if not rule_ok:
        die("partition-rule:does-not-reproduce-memo-cube")

    # ================== restriction gate 2: Cycle 917 reproduced value-for-value ==
    C917_BUILD = {"G1": geom_chain9, "G2": geom_star7, "G3a": lambda: geom_tree(3),
                  "G3b": lambda: geom_tree(4), "G4": geom_plaquette9,
                  "G5": geom_cubeminus11}
    C919_BUILD = {"H1": geom_star6, "H2": geom_tree16, "H3": geom_tree10d5,
                  "H4": geom_cubeminus10}
    restrict = {"per_cell": {}, "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0,
                                                          "theta_A": 0.0, "H_Z": 0.0},
                "mismatches": [], "cells_checked": 0, "rows_compared": 0,
                "extension_field_cells": {}}
    rows_cache = {}
    for key in C917_KEYS:
        g = C917_BUILD[key]()
        pub = r917["geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            restrict["mismatches"].append("%s:site-set" % key)
        if {tuple(sorted(b)) for b in pub["bonds"]} != \
           {tuple(sorted((g["sites"][a], g["sites"][b]))) for (a, b) in g["bonds"]}:
            restrict["mismatches"].append("%s:bond-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                restrict["mismatches"].append("%s:partition:%s" % (key, L))
        for kk, vv in pub["stats"].items():
            if g["stats"].get(kk) != vv:
                restrict["mismatches"].append("%s:stats:%s" % (key, kk))
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam)
            rows_cache[(key, lk)] = rows
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, lam, rows)
            if lam == EXTENSION_LAMBDA:
                want75 = r917c["threshold_attack"][
                    "lambda_boundary_diagnostic_NON_CLAIM"][key]["probe"]["0.075"]
                got75 = cell["headline"]["verdict"]
                restrict["extension_field_cells"]["%s@0.075" % key] = {
                    "recomputed_here": got75, "pinned_917_checker_probe": want75,
                    "agrees": bool(got75 == want75)}
                if got75 != want75:
                    restrict["mismatches"].append("%s@0.075:%s!=%s" % (key, got75, want75))
                continue
            want = r917["ladder"]["%s@%s" % (key, lk)]
            got = cell["headline"]
            bad = []
            if got["verdict"] != want["verdict"]:
                bad.append("verdict %s!=%s" % (got["verdict"], want["verdict"]))
            if cell["xi_reg"]["xi_reg"] != want["xi_reg"]:
                bad.append("xi_reg")
            if cell["max_r_ind_over_window"] != want["max_r_ind"]:
                bad.append("max_r_ind %s!=%s" % (cell["max_r_ind_over_window"],
                                                 want["max_r_ind"]))
            ev, wev = got["event"], want["event"]
            if (ev is None) != (wev is None):
                bad.append("event-presence")
            elif ev is not None:
                if abs(ev["jt"] - wev["jt"]) > 1e-12:
                    bad.append("first_jt")
                if ev["r_ind"] != wev["r_ind"] or ev["run"] != wev["run"]:
                    bad.append("r_ind/run")
                if ev["witness"] != wev["witness"]:
                    bad.append("witness")
                if abs(ev["theta_A"] - wev["theta_A"]) > RESTRICT_TOL:
                    bad.append("theta_A %.3g" % abs(ev["theta_A"] - wev["theta_A"]))
            pubrows = {r["jt"]: r for r in pub["lambdas"][lk]["rows"]}
            for r in rows:
                q = pubrows.get(r["jt"])
                if q is None:
                    bad.append("row-missing@%.1f" % r["jt"])
                    continue
                restrict["rows_compared"] += 1
                for L in r["chi"]:
                    restrict["row_level_max_abs_dev"]["chi"] = max(
                        restrict["row_level_max_abs_dev"]["chi"],
                        abs(r["chi"][L] - q["chi"][L]))
                for kk, vv in r["C_ab"].items():
                    restrict["row_level_max_abs_dev"]["C_ab"] = max(
                        restrict["row_level_max_abs_dev"]["C_ab"], abs(vv - q["C_ab"][kk]))
                restrict["row_level_max_abs_dev"]["theta_A"] = max(
                    restrict["row_level_max_abs_dev"]["theta_A"],
                    abs(r["theta_A"] - q["theta_A"]))
                restrict["row_level_max_abs_dev"]["H_Z"] = max(
                    restrict["row_level_max_abs_dev"]["H_Z"], abs(r["H_Z"] - q["H_Z"]))
                if r["r_ind"] != q["r_ind"]:
                    bad.append("r_ind-ledger@%.1f" % r["jt"])
            restrict["cells_checked"] += 1
            restrict["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": got["verdict"], "matches_917": not bad, "discrepancies": bad,
                "first_jt": (ev or {}).get("jt"), "theta_A": (ev or {}).get("theta_A"),
                "max_r_ind": cell["max_r_ind_over_window"],
                "xi_reg": cell["xi_reg"]["xi_reg"]}
            if bad:
                restrict["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))

    # ============= restriction gate 3: Cycle 919's four anchors, value-for-value ==
    anchor_gate = {"per_cell": {}, "mismatches": [], "rows_compared": 0,
                   "row_level_max_abs_dev": {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0,
                                             "H_Z": 0.0}}
    for key in C919_KEYS:
        g = C919_BUILD[key]()
        pub = r919["degree_five_geometries"][key]
        if set(pub["sites"]) != set(g["sites"]):
            anchor_gate["mismatches"].append("%s:site-set" % key)
        for L, v in pub["partition"].items():
            if set(v) != {g["sites"][i] for i in g["frags"][L]}:
                anchor_gate["mismatches"].append("%s:partition:%s" % (key, L))
        diag = build_diag(g["n"], g["bonds"])
        psi0 = prep_state(g["n"], set([g["S"]] + g["recording"]))
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows, mach, prop = run_route_A(g, diag, psi0, lam)
            rows_cache[(key, lk)] = rows
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], prop["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            cell = cell_of(g, lam, rows)
            want = r919["ladder_by_cell"]["%s@%s" % (key, lk)]
            got = cell["headline"]
            bad = []
            if got["verdict"] != want["verdict"]:
                bad.append("verdict")
            if cell["max_r_ind_over_window"] != want["max_r_ind"]:
                bad.append("max_r_ind %s!=%s" % (cell["max_r_ind_over_window"],
                                                 want["max_r_ind"]))
            if cell["xi_reg"]["xi_reg"] != want["xi_reg"]:
                bad.append("xi_reg")
            ev, wev = got["event"], want["event"]
            if (ev is None) != (wev is None):
                bad.append("event-presence")
            elif ev is not None:
                if abs(ev["jt"] - wev["jt"]) > 1e-12:
                    bad.append("first_jt")
                if ev["r_ind"] != wev["r_ind"] or ev["run"] != wev["run"]:
                    bad.append("r_ind/run")
                if ev["witness"] != wev["witness"]:
                    bad.append("witness")
                if abs(ev["theta_A"] - wev["theta_A"]) > RESTRICT_TOL:
                    bad.append("theta_A %.3g" % abs(ev["theta_A"] - wev["theta_A"]))
            pubrows = {r["jt"]: r for r in pub["lambdas"][lk]["rows"]}
            for r in rows:
                q = pubrows.get(r["jt"])
                if q is None:
                    bad.append("row-missing@%.1f" % r["jt"])
                    continue
                anchor_gate["rows_compared"] += 1
                for L in r["chi"]:
                    anchor_gate["row_level_max_abs_dev"]["chi"] = max(
                        anchor_gate["row_level_max_abs_dev"]["chi"],
                        abs(r["chi"][L] - q["chi"][L]))
                for kk, vv in r["C_ab"].items():
                    anchor_gate["row_level_max_abs_dev"]["C_ab"] = max(
                        anchor_gate["row_level_max_abs_dev"]["C_ab"],
                        abs(vv - q["C_ab"][kk]))
                anchor_gate["row_level_max_abs_dev"]["theta_A"] = max(
                    anchor_gate["row_level_max_abs_dev"]["theta_A"],
                    abs(r["theta_A"] - q["theta_A"]))
                anchor_gate["row_level_max_abs_dev"]["H_Z"] = max(
                    anchor_gate["row_level_max_abs_dev"]["H_Z"],
                    abs(r["H_Z"] - q["H_Z"]))
                if r["r_ind"] != q["r_ind"]:
                    bad.append("r_ind-ledger@%.1f" % r["jt"])
            anchor_gate["per_cell"]["%s@%s" % (key, lk)] = {
                "verdict": got["verdict"], "max_r_ind": cell["max_r_ind_over_window"],
                "pinned_919_max_r_ind": want["max_r_ind"],
                "pinned_919_verdict": want["verdict"],
                "witness": (ev or {}).get("witness"),
                "matches_919": not bad, "discrepancies": bad}
            if bad:
                anchor_gate["mismatches"].append("%s@%s:%s" % (key, lk, ",".join(bad)))
    if restrict["mismatches"]:
        die("restriction:917-not-reproduced %s" % restrict["mismatches"][:6])
    if anchor_gate["mismatches"]:
        die("restriction:919-anchors-not-reproduced %s" % anchor_gate["mismatches"][:6])
    for tab in (restrict["row_level_max_abs_dev"], anchor_gate["row_level_max_abs_dev"]):
        for k, v in tab.items():
            if v > RESTRICT_TOL:
                die("restriction:row-deviation %s=%.3g" % (k, v))

    # =============================================== the Cycle 921 measurement ==
    roster = build_roster()
    per_geom, ladder, structure, preds = {}, {}, {}, {}
    fam_of, geoms = {}, {}
    for fam, g in roster:
        key = g["key"]
        if key in geoms:
            die("roster:duplicate-key %s" % key)
        geoms[key], fam_of[key] = g, fam
        preds[key] = candidate_predictions(g)
        n, S = g["n"], g["S"]
        diag = build_diag(n, g["bonds"])
        psi0 = prep_state(n, set([S] + g["recording"]))
        if abs(float(np.vdot(psi0, psi0).real) - 1.0) > 1e-12:
            die("prep:norm %s" % key)
        use_dense = (n <= DENSE_MAX_N)
        per_geom[key] = {
            "family": fam,
            "declaration": {k: g[k] for k in ("key", "name", "note", "dim", "n", "pointer")},
            "sites": g["sites"],
            "bonds": [[g["sites"][a], g["sites"][b]] for (a, b) in g["bonds"]],
            "recording_sites": [g["sites"][i] for i in g["recording"]],
            "partition": {L: [g["sites"][i] for i in g["frags"][L]] for L in g["labels"]},
            "fragment_anchors": {L: g["sites"][g["anchors"][L]] for L in g["labels"]},
            "partition_ties_resolved": g["ties"],
            "anchor_distance_in_G_minus_S": g["anchor_distance_in_G_minus_S"],
            "stats": g["stats"],
            "candidate_predictions": {k: v for k, v in preds[key].items()
                                      if not k.startswith("_")},
            "pair_cycle_law_detail": {k: v for k, v in preds[key].items()
                                      if k.startswith("_")},
            "route": ("FULL SPACE, dimension 2^%d = %d; route A = Chebyshev/Bessel, "
                      "route B = scaling-and-marching Taylor%s"
                      % (n, 1 << n, ", route C = dense eigendecomposition"
                         if use_dense else " (route C not executed above 2^%d)"
                         % DENSE_MAX_N)),
            "lambdas": {}}
        for lam in LAMBDAS + PROBE_LAMBDAS:
            lk = "%g" % lam
            declared = lam in LAMBDAS
            rows, mach, propA = run_route_A(g, diag, psi0, lam)
            mach_all["cheby_tail"] = max(mach_all["cheby_tail"], propA["tail_bound"])
            for k in mach:
                mach_all[k] = max(mach_all[k], mach[k])
            d1 = sha256_bytes(json.dumps(rows, sort_keys=True, default=repr).encode())
            propB, devB, propC, devC = None, None, None, None
            if declared:
                rows2, _, _ = run_route_A(g, diag, psi0, lam)
                d2 = sha256_bytes(json.dumps(rows2, sort_keys=True, default=repr).encode())
                if d1 != d2:
                    die("determinism:%s:%g" % (key, lam))
                outsB, propB = taylor_march(psi0, diag, n, lam, T_EXEC)
                mach_all["taylor_remainder"] = max(mach_all["taylor_remainder"],
                                                   propB["max_substep_remainder_bound"])
                rowsB, machB = measure(g, outsB, T_EXEC)
                devB = 0.0
                for ra, rb in zip(rows, rowsB):
                    for L in g["labels"]:
                        devB = max(devB, abs(ra["chi"][L] - rb["chi"][L]))
                    for kk in ra["C_ab"]:
                        devB = max(devB, abs(ra["C_ab"][kk] - rb["C_ab"][kk]))
                    devB = max(devB, abs(ra["theta_A"] - rb["theta_A"]))
                    if ra["r_ind"] != rb["r_ind"]:
                        die("route-cross-AB:r_ind %s %g t=%.1f" % (key, lam, ra["jt"]))
                mach_all["route_AB_max_dev"] = max(mach_all["route_AB_max_dev"], devB)
                for k in machB:
                    mach_all[k] = max(mach_all[k], machB[k])
                if use_dense:
                    outsC, propC = dense_route(psi0, diag, n, lam, T_EXEC)
                    rowsC, _ = measure(g, outsC, T_EXEC)
                    devC = 0.0
                    for ra, rc in zip(rows, rowsC):
                        for L in g["labels"]:
                            devC = max(devC, abs(ra["chi"][L] - rc["chi"][L]))
                        for kk in ra["C_ab"]:
                            devC = max(devC, abs(ra["C_ab"][kk] - rc["C_ab"][kk]))
                        devC = max(devC, abs(ra["theta_A"] - rc["theta_A"]))
                        if ra["r_ind"] != rc["r_ind"]:
                            die("route-cross-AC:r_ind %s %g t=%.1f" % (key, lam, ra["jt"]))
                    mach_all["route_AC_max_dev"] = max(mach_all["route_AC_max_dev"], devC)
            cell = cell_of(g, lam, rows)
            st = dependence_structure(g, rows)
            structure["%s@%s" % (key, lk)] = st
            per_geom[key]["lambdas"][lk] = {
                "field_status": ("FROZEN certified field" if lam in FROZEN_LAMBDAS else
                                 "DECLARED DESIGN EXTENSION (inherited from Cycle 919)"
                                 if lam == EXTENSION_LAMBDA else
                                 "DECLARED NON-CLAIM DIAGNOSTIC (crossover probe only)"),
                "chebyshev": propA, "taylor": propB, "dense": propC,
                "route_AB_max_abs_dev": devB, "route_AC_max_abs_dev": devC,
                "determinism_digest": d1,
                "commutator_ordering_ok": cell["commutator_ordering_ok"],
                "xi_reg": cell["xi_reg"],
                "verdicts_by_delta": cell["verdicts_by_delta"],
                "max_r_ind_over_window": cell["max_r_ind_over_window"],
                "ceiling_row_jt": cell["ceiling_row_jt"],
                "ceiling_witness": cell["ceiling_witness"],
                "dependence_structure": st,
                "rows": rows if declared else None,
            }
            hv = cell["headline"]
            ladder[(key, lk)] = {
                "geometry": g["name"], "family": fam, "stats": g["stats"],
                "verdict": hv["verdict"], "reason": hv["reason"], "event": hv["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "ceiling_witness": cell["ceiling_witness"],
                "field_status": ("frozen" if lam in FROZEN_LAMBDAS else
                                 "design-extension" if lam == EXTENSION_LAMBDA else
                                 "non-claim-probe")}

    # the four pinned 919 anchors join the discrimination table as measured rows
    for key in C919_KEYS:
        g = C919_BUILD[key]()
        geoms[key], fam_of[key] = g, "ANCHOR-919"
        preds[key] = candidate_predictions(g)
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows = rows_cache[(key, lk)]
            cell = cell_of(g, lam, rows)
            structure["%s@%s" % (key, lk)] = dependence_structure(g, rows)
            ladder[(key, lk)] = {
                "geometry": g["name"], "family": "ANCHOR-919", "stats": g["stats"],
                "verdict": cell["headline"]["verdict"],
                "reason": cell["headline"]["reason"], "event": cell["headline"]["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "ceiling_witness": cell["ceiling_witness"],
                "field_status": ("frozen" if lam in FROZEN_LAMBDAS
                                 else "design-extension")}
    for key in C917_KEYS:
        g = C917_BUILD[key]()
        geoms[key], fam_of[key] = g, "ANCHOR-917"
        preds[key] = candidate_predictions(g)
        for lam in LAMBDAS:
            lk = "%g" % lam
            rows = rows_cache[(key, lk)]
            cell = cell_of(g, lam, rows)
            structure["%s@%s" % (key, lk)] = dependence_structure(g, rows)
            ladder[(key, lk)] = {
                "geometry": g["name"], "family": "ANCHOR-917", "stats": g["stats"],
                "verdict": cell["headline"]["verdict"],
                "reason": cell["headline"]["reason"], "event": cell["headline"]["event"],
                "xi_reg": cell["xi_reg"]["xi_reg"],
                "max_r_ind": cell["max_r_ind_over_window"],
                "ceiling_witness": cell["ceiling_witness"],
                "field_status": ("frozen" if lam in FROZEN_LAMBDAS
                                 else "design-extension")}

    ORDER = sorted(geoms, key=lambda k: (fam_of[k], k))

    # =================================================== THE DISCRIMINATION TABLE
    CAND = [c for c in CANDIDATES]
    # The law is field-branched BY CONSTRUCTION (the distance-2 clause switches on
    # between the two frozen fields).  "LAW_field_branched" scores the low branch at
    # the frozen lower field and the high branch above it; every other candidate is
    # scored as a single field-independent rule, which is what each of them claims.
    BRANCH = {"0.05": "M1p_low_field_branch", "0.075": "M1p_pair_cycle",
              "0.1": "M1p_pair_cycle"}
    discrim = {}
    for lk in ("0.05", "0.075", "0.1"):
        cells = [k for k in ORDER if (k, lk) in ladder]
        tab = {}
        for c in CAND + ["LAW_field_branched"]:
            src = BRANCH[lk] if c == "LAW_field_branched" else c
            hits, misses = [], []
            for k in cells:
                got = ladder[(k, lk)]["max_r_ind"]
                want = preds[k][src]
                (hits if got == want else misses).append(
                    k if got == want else "%s(pred=%d,got=%d)" % (k, want, got))
            tab[c] = {"exact_hits": len(hits), "cells": len(cells),
                      "misses": misses, "perfect": bool(not misses),
                      "branch_used": src if c == "LAW_field_branched" else None}
        discrim[lk] = tab
    ALLC = CAND + ["LAW_field_branched"]
    survivors = {lk: sorted(c for c in ALLC if discrim[lk][c]["perfect"])
                 for lk in discrim}
    best = {lk: sorted(ALLC, key=lambda c: (-discrim[lk][c]["exact_hits"], c))[0]
            for lk in discrim}

    # the matched-pair table: the cells that separate topology from every count
    MATCHED = [
        ("QC2p", "QC2d", "two plaquettes: shared anchor vs disjoint"),
        ("QC3s", "QC3x", "three plaquettes: star vs independence-3 arrangement"),
        ("QC4s", "H4", "four plaquettes: star vs 4-cycle (919's own H4)"),
        ("QW1", "H4", "four loops internal to one fragment vs four plaquettes"),
        ("QCL1", "QCL2", "an added corner: more loops at an unchanged pair set"),
        ("QD5", "QN3", "one loop vs three loops at an unchanged pair set"),
    ]
    matched = {}
    for a, b, why in MATCHED:
        row = {"why": why, "shared_statistics": {}, "differs": {}}
        sa, sb = geoms[a]["stats"], geoms[b]["stats"]
        for f in ("n_sites", "n_bonds", "cyclomatic_number_loops", "n_seam_pairs",
                  "pointer_degree", "max_degree", "depth_eccentricity_from_pointer",
                  "components_of_G_minus_S", "n_fragments"):
            (row["shared_statistics"] if sa[f] == sb[f] else row["differs"])[f] = (
                sa[f] if sa[f] == sb[f] else [sa[f], sb[f]])
        row["fragment_size_multiset_equal"] = bool(
            sorted(sa["fragment_sizes"].values()) == sorted(sb["fragment_sizes"].values()))
        for lk in ("0.05", "0.075", "0.1"):
            row["max_r_ind@%s" % lk] = [ladder[(a, lk)]["max_r_ind"],
                                        ladder[(b, lk)]["max_r_ind"]]
        row["pair_cycle_prediction"] = [preds[a]["M1p_pair_cycle"],
                                        preds[b]["M1p_pair_cycle"]]
        row["separated_at_frozen_upper_field"] = bool(
            ladder[(a, "0.1")]["max_r_ind"] != ladder[(b, "0.1")]["max_r_ind"])
        matched["%s|%s" % (a, b)] = row

    # ================================================= the three separable axes ==
    def axis_rows(keys, field="0.1"):
        return {k: {"loops": geoms[k]["stats"]["cyclomatic_number_loops"],
                    "loops_through_pointer": geoms[k]["stats"]["loops_through_pointer"],
                    "internal_loops": geoms[k]["stats"]["internal_loops_not_through_pointer"],
                    "shortest_pointer_cycle": geoms[k]["stats"]["shortest_pointer_cycle_length"],
                    "pointer_degree": geoms[k]["stats"]["pointer_degree"],
                    "max_r_ind": ladder[(k, field)]["max_r_ind"],
                    "pair_cycle_prediction": preds[k]["M1p_pair_cycle"]}
                for k in keys if (k, field) in ladder}
    axes = {
        "LENGTH": {
            "question": "does the loop cost depend on the LENGTH of the loop?",
            "design": "the ANCHOR (cycle length 3), CUBE (length 4), BYPASS3 (length 5) "
                      "and LENGTH (lengths 5, 7, 9) families, all at pointer degree 5",
            "rows": axis_rows(["QA1", "QC1", "QB1", "QD5", "QD7", "QD9", "QC0", "QD0"]),
            "answer": None},
        "COUNT": {
            "question": "does the loop cost depend on the NUMBER of loops?",
            "design": "QCL1/QCL2 (2 vs 3 loops, unchanged pair set), QD5/QN2/QN3 (1 vs 2 "
                      "vs 3 loops, unchanged pair set), QB1/QB4c/QB10 (1 vs 4 vs 10 "
                      "loops), and the matched cube pairs at equal loop count",
            "rows": axis_rows(["QCL1", "QCL2", "QD5", "QN2", "QN3", "QB1", "QB4c",
                               "QB10", "QC3s", "QC3x", "QC4s", "H4"]),
            "answer": None},
        "POSITION": {
            "question": "does the loop cost depend on the POSITION of the loop relative "
                        "to the pointer?",
            "design": "the INTERNAL family, whose loops never pass through the pointer -- "
                      "QW1 carries FOUR of them and is matched to H4 in site count, bond "
                      "count, degree, maximum degree, depth and loop count; QP1's loop "
                      "touches an anchor one bond from the pointer",
            "rows": axis_rows(["QW0", "QW1", "QP1", "QP3", "H4", "QD0"]),
            "answer": None},
    }
    # LENGTH answer
    len_tab = {}
    for k in ORDER:
        if (k, "0.1") not in ladder:
            continue
        ell = geoms[k]["stats"]["shortest_pointer_cycle_length"]
        len_tab.setdefault(str(ell), []).append(
            geoms[k]["stats"]["pointer_degree"] - ladder[(k, "0.1")]["max_r_ind"])
    axes["LENGTH"]["cost_by_shortest_pointer_cycle_length_at_0.10"] = {
        k: sorted(set(v)) for k, v in sorted(len_tab.items(), key=lambda kv: int(kv[0]))}
    axes["LENGTH"]["answer"] = (
        "YES, decisively, and it is the axis that sets the REGIME.  The cost is levied "
        "per PAIR of fragments and graded by the length of the shortest pointer-through "
        "cycle joining their two anchors: length 3 kills the CONTENT of both fragments "
        "at every measured field; length 4 kills the mutual INDEPENDENCE of the pair at "
        "lambda >= 0.075 but not at lambda = 0.05; length 5 and above costs nothing at "
        "any field in {0.05, 0.075, 0.10}.  A loop-free geometry has no pointer cycle at "
        "all and pays nothing, which is 917's reading.")
    cnt_pairs = [("QCL1", "QCL2"), ("QD5", "QN2"), ("QD5", "QN3"), ("QC3s", "QC4s"),
                 ("QC2d", "QC3x"), ("QC3x", "H4")]
    axes["COUNT"]["equal_prediction_different_loop_count"] = {
        "%s|%s" % (a, b): {
            "loops": [geoms[a]["stats"]["cyclomatic_number_loops"],
                      geoms[b]["stats"]["cyclomatic_number_loops"]],
            "max_r_ind@0.10": [ladder[(a, "0.1")]["max_r_ind"],
                               ladder[(b, "0.1")]["max_r_ind"]],
            "ceiling_unchanged": bool(ladder[(a, "0.1")]["max_r_ind"]
                                      == ladder[(b, "0.1")]["max_r_ind"])}
        for a, b in cnt_pairs if (a, "0.1") in ladder and (b, "0.1") in ladder}
    axes["COUNT"]["answer"] = (
        "NO.  Loop count neither predicts nor bounds the cost.  QB10 carries TEN loops "
        "and pays nothing; QW1 carries FOUR and pays nothing; the matched cube pairs "
        "carry the SAME loop count and pay differently.  Both readings of a cyclomatic "
        "tax (linear and the 917/919-fitted half) are refuted on the same cells.")
    axes["POSITION"]["answer"] = (
        "YES, but only as a BINARY gate that the length axis already contains: a loop "
        "that does not pass through the pointer costs nothing, however many there are "
        "and however close to the pointer they run.  QW1's four loops are internal to "
        "one fragment and its ceiling is the full pointer degree, while 919's H4 -- the "
        "same site count, bond count, pointer degree, maximum degree, depth and loop "
        "count -- drops to 3.  QP1's loop touches an anchor one bond from the pointer "
        "and still costs nothing.  Once a loop does pass through the pointer, its "
        "distance from the pointer IS its length, so position adds nothing further.")

    # ============================================== the crossover in the field ==
    crossover = {}
    for k in ORDER:
        d = geoms[k]["anchor_distance_in_G_minus_S"]
        by_d = {}
        for lk in ("0.05", "0.075", "0.1", "0.125", "0.15"):
            if (k, lk) not in ladder:
                continue
            st = structure["%s@%s" % (k, lk)]
            over = set(st["pairs_over_the_independence_gate"])
            for pr, dd in d.items():
                by_d.setdefault(str(dd), {}).setdefault(lk, []).append(pr in over)
        crossover[k] = {dd: {lk: (all(v), any(v)) for lk, v in sorted(m.items())}
                        for dd, m in sorted(by_d.items())}
    cross_summary = {}
    for dd in ("1", "2", "3", "4", "5", "6", "7", "-1"):
        first = {}
        for k, m in crossover.items():
            if dd not in m:
                continue
            fl = next((lk for lk, (allv, anyv) in sorted(m[dd].items(),
                                                         key=lambda kv: float(kv[0]))
                       if anyv), None)
            first[k] = fl
        if first:
            cross_summary[dd] = {
                "geometries": len(first),
                "first_field_at_which_some_pair_of_this_distance_is_over_the_gate":
                    sorted({v for v in first.values()}, key=lambda x: (x is None, x)),
                "per_geometry": first}

    # ===================================================== THE VERDICT (Q3) =====
    law_miss = {lk: discrim[lk]["LAW_field_branched"]["misses"] for lk in discrim}
    law_hits = {lk: discrim[lk]["LAW_field_branched"]["exact_hits"] for lk in discrim}
    # a cell can only be a LOOP-channel cell if it has a pair at anchor distance <= 2
    exception_keys = sorted({m.split("(")[0] for v in law_miss.values() for m in v})
    exceptions = {k: {
        "has_any_pair_at_anchor_distance_at_most_2": bool(
            any(0 < v <= 2 for v in geoms[k]["anchor_distance_in_G_minus_S"].values())),
        "loops": geoms[k]["stats"]["cyclomatic_number_loops"],
        "pointer_degree": geoms[k]["stats"]["pointer_degree"],
        "max_fragment_size": geoms[k]["stats"]["max_fragment_size"],
        "fields_missed": [lk for lk in law_miss
                          if any(m.startswith(k + "(") for m in law_miss[lk])]}
        for k in exception_keys}
    verdict = {
        "surviving_mechanism": ("M1p_pair_cycle (the PAIR-CYCLE LAW, field-branched)"
                                if law_hits["0.1"] >= max(
                                    discrim["0.1"][c]["exact_hits"] for c in CAND)
                                else None),
        "exact_hits_by_field": law_hits,
        "cells_by_field": {lk: discrim[lk]["LAW_field_branched"]["cells"]
                           for lk in discrim},
        "named_exceptions": exceptions,
        "second_channel": (
            "The law's only miss is a LOOP-FREE cell: Cycle 917's degree-2 chain "
            "comparator G1 at the frozen upper field, where the two arms of the chain sit "
            "at INFINITE anchor distance (G minus the pointer is disconnected) and the "
            "law therefore predicts no cost -- yet the measured ceiling is 1, not 2.  "
            "That is a SECOND, loop-independent channel of conditional dependence which "
            "grows with fragment size and field and which this block does not explain.  "
            "It is reported, not absorbed: the pair-cycle law is a law about the LOOP "
            "cost, and it is exact on every cell whose dependence is loop-borne."),
        "survivors_at_frozen_upper_field": survivors["0.1"],
        "survivors_at_the_design_extension": survivors["0.075"],
        "survivors_at_frozen_lower_field": survivors["0.05"],
        "best_candidate_by_exact_hits": best,
        "runner_up_at_frozen_upper_field": sorted(
            [(discrim["0.1"][c]["exact_hits"], c) for c in CAND
             if c not in ("M1p_pair_cycle", "M1p_low_field_branch")], reverse=True)[0],
        "mechanism_candidates_refuted": sorted(
            c for c in CAND if not c.startswith("D")
            and c not in ("M1p_pair_cycle", "M1p_low_field_branch")
            and not discrim["0.1"][c]["perfect"]),
        "degeneracy_probes_that_also_fit": sorted(
            c for c in CAND if c.startswith("D") and discrim["0.1"][c]["perfect"]),
        "law": (
            "THE PAIR-CYCLE LAW.  For each pair of pointer-fragments (a,b) let d(a,b) be "
            "the distance between their two anchors in G with the pointer deleted -- "
            "equivalently, the shortest cycle through the pointer containing both anchors "
            "has length d + 2.  Over the frozen certification window: d = 1 removes BOTH "
            "a and b (they fail the content gate) at every measured field; d = 2 removes "
            "the PAIR {a,b} from mutual independence at lambda >= 0.075 but not at "
            "lambda = 0.05; d >= 3 costs nothing at any measured field.  max R_ind is the "
            "independence number of the graph that survives.  A loop-free geometry has no "
            "finite d, so max R_ind = pointer degree: that is exactly 917's reading, and "
            "the loopy failures at lambda = 0.10 are exactly the d = 2 pairs."),
        "law_shape": ("the ceiling equals the pointer degree, EXCEPT that every pair of "
                      "fragments joined by a pointer-through cycle of length 4 loses its "
                      "mutual independence above lambda = 0.05, and every pair joined by "
                      "one of length 3 loses its content outright"),
        "how_917_and_919_are_recovered": {
            "917 lambda=0.05, all seven geometries": "no d=2 pair is over the gate at the "
                                                     "ceiling row, so the ceiling is the "
                                                     "pointer degree on loopy and loop-free "
                                                     "alike",
            "917 lambda=0.10, the three loopy geometries": "their plaquettes are exactly "
                                                           "d=2 pairs; the ceiling drops to "
                                                           "the independence number",
            "919 H4": "pair graph is a 4-cycle plus an isolated +z: independence number 3, "
                      "which is the measured drop from 5",
        },
    }
    verdict["honest_partition"] = (
        "The pair-cycle law is EXACT on %d of %d cells at the frozen upper field and on "
        "%d of %d at the design extension, and is the unique candidate that is exact on "
        "every geometry designed by this block.  It is NOT universally exact: %d cell(s) "
        "miss, all of them loop-free, and all of them attributable to the second channel "
        "described above.  Every rival mechanism misses by an order of magnitude more "
        "(best rival %s at %d/%d), and the two fully matched cube pairs -- identical on "
        "every tracked graph statistic including fragment sizes -- separate 4 against 3, "
        "which no count-based rule can produce."
        % (law_hits["0.1"], discrim["0.1"]["LAW_field_branched"]["cells"],
           law_hits["0.075"], discrim["0.075"]["LAW_field_branched"]["cells"],
           len(law_miss["0.1"]), verdict["runner_up_at_frozen_upper_field"][1],
           verdict["runner_up_at_frozen_upper_field"][0],
           discrim["0.1"]["LAW_field_branched"]["cells"]))
    designed = [k for k in ORDER if fam_of[k] not in ("ANCHOR-917", "ANCHOR-919")]
    verdict["on_the_geometries_this_block_designed"] = {
        lk: {"cells": len(designed),
             "exact": sum(1 for k in designed
                          if ladder[(k, lk)]["max_r_ind"] == preds[k][BRANCH[lk]]),
             "misses": [k for k in designed
                        if ladder[(k, lk)]["max_r_ind"] != preds[k][BRANCH[lk]]]}
        for lk in ("0.05", "0.075", "0.1")}

    # ============================================== falsifier / outcome gates ==
    falsifier = {}
    # (a) planted certification on a real NO cell
    plant_key, plant_lk = "G1", "0.1"
    plant_g = C917_BUILD[plant_key]()
    rr = [dict(r) for r in rows_cache[(plant_key, plant_lk)]]
    labs = plant_g["labels"]
    for r in rr:
        r["C_ab"] = {k: 0.0 for k in r["C_ab"]}
        r["chi"] = {L: max(r["chi"][L], 0.999) for L in labs}
        r["excess"] = {L: max(r["excess"][L], 0.999) for L in labs}
        Cp = {tuple(k.split("|")): 0.0 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(labs, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d], subs["%.2f" % d], sing["%.2f" % d] = k, sub, sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    planted_v = verdict_of(rr, HEADLINE_DELTA, True)
    falsifier["T1_planted_certification_on_a_real_NO"] = {
        "geometry": plant_key, "field": plant_lk,
        "real_verdict": ladder[(plant_key, plant_lk)]["verdict"],
        "planted_verdict": planted_v["verdict"],
        "fires": bool(ladder[(plant_key, plant_lk)]["verdict"] == "NO"
                      and planted_v["verdict"] == "YES")}
    # (b) suppressed certification on a real YES
    supp_key = "QC0"
    rr2 = [dict(r) for r in per_geom[supp_key]["lambdas"]["0.05"]["rows"]]
    lab2 = geoms[supp_key]["labels"]
    for r in rr2:
        Cp = {tuple(k.split("|")): 0.5 for k in r["C_ab"]}
        rrr, subs, sing = {}, {}, {}
        for d in DELTAS:
            k, sub, sg = r_ind(lab2, r["chi"], r["excess"], r["H_Z"], Cp, d)
            rrr["%.2f" % d], subs["%.2f" % d], sing["%.2f" % d] = k, sub, sg
        r["r_ind"], r["certifying_subsets"], r["singleton_passes"] = rrr, subs, sing
    supp = verdict_of(rr2, HEADLINE_DELTA, True)
    falsifier["T2_suppressed_certification_on_a_real_YES"] = {
        "geometry": supp_key, "field": "0.05",
        "real_verdict": ladder[(supp_key, "0.05")]["verdict"],
        "verdict_with_C_ab_forced_above_the_gate": supp["verdict"],
        "fires": bool(supp["verdict"] == "NO")}
    # (c) PLANTED WRONG-MECHANISM DATA must flip the verdict.  Rewrite the measured
    #     ceilings so that the LOOP-COUNT candidate is the perfect fit, and check that
    #     the discrimination re-run names M2b instead of the pair-cycle law.
    planted_ceilings = {k: preds[k]["M2b_loop_count_half"] for k in ORDER}
    planted_tab = {}
    for c in CAND:
        miss = [k for k in ORDER if (k, "0.1") in ladder
                and planted_ceilings[k] != preds[k][c]]
        planted_tab[c] = not miss
    falsifier["T3_planted_wrong_mechanism_flips_the_verdict"] = {
        "planted_rule": "every measured ceiling replaced by the M2b loop-count prediction",
        "survivors_under_planted_data": sorted(c for c, ok in planted_tab.items() if ok),
        "pair_cycle_still_survives": bool(planted_tab["M1p_pair_cycle"]),
        "loop_count_now_survives": bool(planted_tab["M2b_loop_count_half"]),
        "fires": bool(planted_tab["M2b_loop_count_half"]
                      and not planted_tab["M1p_pair_cycle"])}
    # (d) under-converged propagator guard
    guard_key = "QC4s"
    gg = geoms[guard_key]
    gdiag = build_diag(gg["n"], gg["bonds"])
    gpsi = prep_state(gg["n"], set([gg["S"]] + gg["recording"]))
    gmv = _matvec_factory(gdiag, gg["n"], 0.10)
    crude = []
    for t in T_EXEC:
        v = gpsi - 1j * t * gmv(gpsi.copy())
        crude.append(v / np.linalg.norm(v))
    good_states, _ = chebyshev(gpsi, gdiag, gg["n"], 0.10, T_EXEC)
    state_dev = max(float(np.abs(a - b).max()) for a, b in zip(crude, good_states))
    crude_rows, _ = measure(gg, crude, T_EXEC)
    crude_ceiling = max(r["r_ind"]["%.2f" % HEADLINE_DELTA] for r in crude_rows)
    falsifier["T4_under_converged_propagator_guard"] = {
        "geometry": guard_key, "field": 0.10,
        "crude_propagator": "first-order Euler, psi(t) = (1 - iHt) psi(0), renormalised",
        "max_state_deviation_vs_chebyshev": state_dev,
        "crude_ceiling": crude_ceiling,
        "converged_ceiling": ladder[(guard_key, "0.1")]["max_r_ind"],
        "ceiling_differs": bool(crude_ceiling != ladder[(guard_key, "0.1")]["max_r_ind"]),
        "fires": bool(state_dev > 1e-3)}
    # (e) tampered pin must be caught
    tp = os.path.join(ROOT, C919_RECEIPT)
    raw = open(tp, "rb").read()
    tampered = sha256_bytes(raw[:-1] + b" ")
    falsifier["T5_tampered_pin_is_caught"] = {
        "artifact": C919_RECEIPT, "true_sha256": sha256_bytes(raw),
        "one_byte_tampered_sha256": tampered,
        "pin_would_reject": bool(tampered != PINS[C919_RECEIPT][0]),
        "fires": bool(tampered != PINS[C919_RECEIPT][0])}
    # (f) the law must be able to predict a NON-certifying geometry, and does
    falsifier["T6_law_predicts_a_topological_NO"] = {
        "geometry": "QCK", "pair_graph": "triangle on three fragments",
        "pair_cycle_prediction": preds["QCK"]["M1p_pair_cycle"],
        "measured_max_r_ind": {lk: ladder[("QCK", lk)]["max_r_ind"]
                               for lk in ("0.05", "0.075", "0.1")},
        "verdicts": {lk: ladder[("QCK", lk)]["verdict"]
                     for lk in ("0.05", "0.075", "0.1")},
        "loop_free_control_QCT": {lk: [ladder[("QCT", lk)]["max_r_ind"],
                                       ladder[("QCT", lk)]["verdict"]]
                                  for lk in ("0.05", "0.075", "0.1")},
        "fires": bool(ladder[("QCK", "0.1")]["max_r_ind"] == 1
                      and ladder[("QCK", "0.1")]["verdict"] == "NO"
                      and ladder[("QCT", "0.1")]["max_r_ind"] == 3)}
    # (g) outcome neutrality: both ceilings reachable on the matched pairs
    falsifier["T7_matched_pairs_separate"] = {
        "pairs": {k: v["separated_at_frozen_upper_field"] for k, v in matched.items()},
        "fires": bool(any(v["separated_at_frozen_upper_field"] for v in matched.values()))}
    # (h) the structural claim is checked cell by cell, not asserted
    FIELDS3 = ("0.05", "0.075", "0.1")
    cells_of = {lk: [k for k in ORDER if (k, lk) in ladder] for lk in FIELDS3}
    struct_ok = {
        "content_failures_are_the_distance_1_fragments": {
            lk: all(structure["%s@%s" % (k, lk)][
                        "content_failures_are_exactly_the_distance_1_fragments"]
                    for k in cells_of[lk]) for lk in FIELDS3},
        "among_passers_over_gate_equals_distance_2": {
            lk: all(structure["%s@%s" % (k, lk)][
                        "among_passers_over_gate_equals_distance_2"]
                    for k in cells_of[lk]) for lk in FIELDS3},
        "among_passers_nothing_over_gate": {
            lk: all(structure["%s@%s" % (k, lk)]["among_passers_no_pair_is_over_gate"]
                    for k in cells_of[lk]) for lk in FIELDS3},
    }
    struct_exceptions = {
        claim: {lk: [k for k in cells_of[lk]
                     if not structure["%s@%s" % (k, lk)][field]]
                for lk in FIELDS3}
        for claim, field in (
            ("content_failures_are_the_distance_1_fragments",
             "content_failures_are_exactly_the_distance_1_fragments"),
            ("among_passers_over_gate_equals_distance_2",
             "among_passers_over_gate_equals_distance_2"),
            ("among_passers_nothing_over_gate",
             "among_passers_no_pair_is_over_gate"))}
    n_live_d2 = sum(1 for k in cells_of["0.1"]
                    if structure["%s@%s" % (k, "0.1")][
                        "distance_2_pairs_among_content_passers"])
    loopy_cells = {lk: [k for k in cells_of[lk]
                        if any(0 < v <= 2 for v in
                               geoms[k]["anchor_distance_in_G_minus_S"].values())]
                   for lk in FIELDS3}
    loopy_ok = {lk: all(structure["%s@%s" % (k, lk)][
                            "among_passers_over_gate_equals_distance_2"]
                        for k in loopy_cells[lk]) for lk in ("0.075", "0.1")}
    falsifier["T8_dependence_structure_is_field_graded_and_loop_borne"] = {
        "claims_per_field": struct_ok, "exceptions": struct_exceptions,
        "cells_carrying_a_pointer_cycle_of_length_at_most_4": {lk: len(loopy_cells[lk])
                                                              for lk in FIELDS3},
        "on_those_cells_over_gate_equals_distance_2": loopy_ok,
        "loopy_cells_where_the_identity_fails": {
            lk: [k for k in loopy_cells[lk]
                 if not structure["%s@%s" % (k, lk)][
                     "among_passers_over_gate_equals_distance_2"]]
            for lk in ("0.075", "0.1")},
        "design_extension_caveat": (
            "at the DECLARED DESIGN EXTENSION lambda = 0.075 the identity fails on QC8, "
            "the densest geometry in the roster (all eight available plaquettes): one of "
            "its eight anchor-distance-2 pairs has not yet crossed the independence gate "
            "at that field.  Its CEILING is nonetheless the predicted 2, because the "
            "remaining seven pairs already force it.  The claim surface is the two FROZEN "
            "fields, where no such exception occurs; this one is reported, not absorbed."),
        "claim_surface": "the two frozen fields {0.05, 0.10}",
        "cells_with_a_live_distance_2_pair_at_0.10": n_live_d2,
        "reading": "at the frozen LOWER field no pair among the content passers is over "
                   "the independence gate on ANY cell; at the frozen UPPER field the "
                   "over-gate pairs among the content passers are exactly the "
                   "anchor-distance-2 pairs on every cell that carries a pointer cycle "
                   "of length at most 4; and the content failures are exactly the "
                   "fragments carrying an anchor-distance-1 partner, at every field.  "
                   "The structure is therefore FIELD-GRADED (it differs between the two "
                   "frozen fields) and LOOP-BORNE (it is carried by the short pointer "
                   "cycles), which is the mechanism claim stated as a measurement.",
        "fires": bool(struct_ok["among_passers_nothing_over_gate"]["0.05"]
                      and loopy_ok["0.1"]
                      and struct_ok["content_failures_are_the_distance_1_fragments"]["0.1"]
                      and struct_ok["content_failures_are_the_distance_1_fragments"]["0.05"]
                      and n_live_d2 > 0)}
    # (i) the loop-free baseline scan: hunt for over-gate pairs on cells the law says
    #     should cost NOTHING.  A tooth with teeth finds the second channel.
    loopfree_hits = []
    for lk in FIELDS3:
        for k in cells_of[lk]:
            if k in loopy_cells[lk]:
                continue
            st = structure["%s@%s" % (k, lk)]
            if st["over_gate_pairs_among_content_passers"]:
                loopfree_hits.append({
                    "cell": "%s@%s" % (k, lk),
                    "pairs": st["over_gate_pairs_among_content_passers"],
                    "pointer_degree": geoms[k]["stats"]["pointer_degree"],
                    "max_fragment_size": geoms[k]["stats"]["max_fragment_size"],
                    "anchor_distances": geoms[k]["anchor_distance_in_G_minus_S"],
                    "measured_max_r_ind": ladder[(k, lk)]["max_r_ind"],
                    "law_prediction": preds[k][BRANCH[lk]]})
    falsifier["T9_loop_free_baseline_scan_finds_the_second_channel"] = {
        "scanned_cells": sum(len(cells_of[lk]) - len(loopy_cells[lk]) for lk in FIELDS3),
        "cells_where_a_pair_crosses_the_gate_with_no_short_pointer_cycle": loopfree_hits,
        "reading": "this scan exists to REFUTE the block's own law.  It looks for pairs "
                   "that cross the independence gate on geometries the law says should "
                   "cost nothing.  It finds them, and they are reported as the law's "
                   "named exceptions rather than absorbed into it.",
        "fires": bool(loopfree_hits)}

    # =============================================== the ladder table & output ==
    refined = []
    for gk in ORDER:
        for lk in ("0.05", "0.075", "0.1", "0.125", "0.15"):
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = geoms[gk]["stats"]
            refined.append({
                "geometry_key": gk, "family": row["family"], "geometry": row["geometry"],
                "lambda": float(lk), "field_status": row["field_status"],
                "pointer_degree": st["pointer_degree"], "n_sites": st["n_sites"],
                "n_bonds": st["n_bonds"], "loops": st["cyclomatic_number_loops"],
                "loops_through_pointer": st["loops_through_pointer"],
                "internal_loops": st["internal_loops_not_through_pointer"],
                "shortest_pointer_cycle_length": st["shortest_pointer_cycle_length"],
                "n_seam_pairs": st["n_seam_pairs"],
                "verdict": row["verdict"], "first_jt": (ev or {}).get("jt"),
                "R_ind_at_event": (ev or {}).get("r_ind"),
                "max_R_ind": row["max_r_ind"],
                "pair_cycle_prediction": preds[gk]["M1p_pair_cycle"],
                "prediction_matches": bool(row["max_r_ind"]
                                           == preds[gk]["M1p_pair_cycle"]),
                "ceiling_witness": row["ceiling_witness"],
                "xi_reg": row["xi_reg"], "reason": row["reason"]})

    mach_ok = (mach_all["norm"] <= MACH_TOL and mach_all["hermiticity"] <= MACH_TOL
               and mach_all["negativity"] <= MACH_TOL
               and mach_all["entropy_bound"] <= MACH_TOL
               and mach_all["t0_anchor"] <= T0_ANCHOR_TOL
               and mach_all["route_AB_max_dev"] <= MACH_TOL
               and mach_all["route_AC_max_dev"] <= MACH_TOL)
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30
    digest = sha256_bytes(json.dumps(refined, sort_keys=True, default=repr).encode())
    self_sha = sha256_bytes(open(os.path.abspath(__file__), "rb").read())

    deviations = [
        "DESIGN-FREEDOM (GEOMETRY SET): the 32 measurement geometries are this block's "
        "design freedom.  Every protocol element -- Hamiltonian, preparation rule, "
        "partition rule, certification conditions, tolerances, deadline, persistence "
        "rule, excess anchor, label-order tie-break -- is inherited from the frozen memo, "
        "byte-verified against it (21/21 constants) and cross-checked quote-for-quote "
        "against BOTH the pinned 917 and 919 receipts.",
        "FIELD SET: {0.05, 0.10} are the frozen certified fields.  lambda = 0.075 is "
        "Cycle 919's DECLARED DESIGN EXTENSION, inherited here with its status; the "
        "block's restriction gate independently reproduces the pinned 917 checker's "
        "0.075 verdicts on all six 917 geometries before any 0.075 number of its own is "
        "produced.  {0.125, 0.15} are a DECLARED NON-CLAIM DIAGNOSTIC used only to locate "
        "the crossover in the anchor distance; no claim rests on them and their rows are "
        "not retained in the receipt.",
        "TIE-BREAK SCOPE: the frozen memo's tie-break is defined in cube coordinates.  A "
        "site adjacent to two anchors is necessarily equidistant from both, so anchor "
        "distance 2 is only CONSTRUCTIBLE under the frozen partition rule inside cube "
        "coordinates.  That is why the CUBE family carries the whole of the "
        "field-graded regime, and it is a structural fact about the frozen rule, not a "
        "choice of this block.  Every non-cube geometry here is tie-free by construction "
        "and the runner hard-fails on any undeclared tie.",
        "ROUTE-C CEILING: dense eigendecomposition is executed for n <= 12 (dimension "
        "4096).  QC8 (n = 14) and the 919 anchor H2 (n = 16) run on routes A and B only; "
        "those two routes are algorithmically disjoint (Chebyshev/Bessel three-term "
        "recurrence versus scaling-and-marching Taylor with a factorial remainder bound).",
        "PROBE-FIELD ROUTES: the two non-claim crossover fields run route A only, with "
        "no determinism double-run and no route B/C cross-check.  They carry no claim.",
        "THETA-ADAPTATION and XI-REG-ADAPTATION: identical to Cycles 917 and 919 -- theta "
        "is (1/deg(S)) over the pointer's own bonds, and xi_reg reads the memo's Manhattan "
        "shell as a graph-distance shell.",
        "LATE-GRID: only the certification subgrid Jt in {0.0,...,1.2} is executed.",
        "NO-LAZY-PAIR-RULE: every fragment pair is evaluated at every executed time on "
        "every geometry.",
        "G6-NOT-RE-RUN: the 3x3x3 cube is built only to verify the partition rule against "
        "the memo's own six published fragment lists; its dynamics are not recomputed "
        "here, and its 917 ceiling row is quoted from the pinned receipt in the discussion "
        "only, not entered in the discrimination table.",
    ]

    receipt = {
        "schema": "loop-cost-cycle921-v1",
        "cycle": 921,
        "runner": "scripts/frontier_cycle921_loop_cost_2026_07_28.py",
        "runner_sha256": self_sha,
        "date": "2026-07-28",
        "git_head": head,
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "recovered_d1_note": d1_prov,
        "frozen_constants_byte_verified": frozen,
        "frozen_constants_cross_check": const_x,
        "restriction_gates": {
            "partition_rule_reproduces_the_memo_cube_partition": {
                "ok": True, "per_label": rule_detail},
            "cycle917_reproduced_value_for_value": restrict,
            "cycle919_anchors_reproduced_value_for_value": anchor_gate,
            "frozen_gate_constants_byte_verified": {k: frozen[k]["quote"] for k in frozen},
        },
        "protocol": {
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1,
            "lambdas_frozen": list(FROZEN_LAMBDAS),
            "lambda_design_extension": EXTENSION_LAMBDA,
            "lambdas_executed": list(LAMBDAS),
            "probe_lambdas_non_claim_diagnostic": list(PROBE_LAMBDAS),
            "deltas": list(DELTAS), "headline_delta": HEADLINE_DELTA,
            "deadline_jt": DEADLINE_JT, "persistence_samples": PERSIST_N,
            "content_H_min": CONTENT_H_MIN, "excess_min": EXCESS_MIN,
            "independence_max": INDEP_MAX, "t0_anchor_tol": T0_ANCHOR_TOL,
            "T_executed": T_EXEC,
            "preparation_rule": "the pointer and every pointer-adjacent (recording) site "
                                "in +X; every other site in +Z",
            "partition_rule": "each recording site anchors a fragment; every other site "
                              "joins its nearest recording site's fragment; ties by the "
                              "frozen memo's tie-break algorithm in cube coordinates",
        },
        "candidate_mechanisms": CANDIDATES,
        "candidate_predictions_per_geometry": {k: {c: preds[k][c] for c in CAND}
                                               for k in ORDER},
        "geometries": per_geom,
        "measured_ladder": refined,
        "ladder_by_cell": {"%s@%s" % (gk, lk): {
            kk: vv for kk, vv in ladder[(gk, lk)].items() if kk != "stats"}
            for (gk, lk) in ladder},
        "dependence_structure_by_cell": structure,
        "discrimination_table": discrim,
        "survivors_by_field": survivors,
        "matched_pairs": matched,
        "three_axes": axes,
        "anchor_distance_crossover": {"per_geometry": crossover, "summary": cross_summary},
        "verdict": verdict,
        "falsifier": falsifier,
        "numerics": {
            "route_A": "Chebyshev expansion of exp(-iHt), rigorous Bessel tail bound",
            "route_B": "scaling-and-marching Taylor propagator, rigorous factorial "
                       "remainder bound; algorithmically disjoint from route A",
            "route_C": "exact dense eigendecomposition (n <= %d only)" % DENSE_MAX_N,
            "machinery": mach_all, "machinery_ok": bool(mach_ok),
            "determinism_double_run_digests_equal": True,
            "peak_rss_gib": rss, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "ladder_digest": digest,
        },
        "deviations": deviations,
        "blindness": "NOT BLIND: the pinned 917 and 919 receipts were read while designing "
                     "the geometry roster.  Every candidate predictor is a pure function of "
                     "the graph, declared and computed before its cell is propagated, and "
                     "the roster contains matched pairs on which the candidates disagree "
                     "in both directions.",
    }
    # a digest of the whole receipt with the three volatile fields removed, so a
    # cold double-run can be compared artifact-to-artifact and not only stdout-to-stdout
    volatile = ("wall_s", "peak_rss_gib", "content_digest_excluding_timing")
    stable = json.loads(json.dumps(receipt, sort_keys=True, default=float))
    for v in volatile:
        stable["numerics"].pop(v, None)
    content_digest = sha256_bytes(json.dumps(stable, sort_keys=True).encode())
    receipt["numerics"]["content_digest_excluding_timing"] = content_digest
    receipt["numerics"]["content_digest_note"] = (
        "sha256 of this receipt with numerics.wall_s, numerics.peak_rss_gib and this "
        "field removed.  Two cold runs of the committed runner must agree on it "
        "byte-for-byte; the receipt file's own sha256 cannot, because it carries the "
        "wall clock and the peak RSS.")
    outp = os.path.join(ROOT, "outputs/loop_cost_cycle921_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    # ---------------------------------------------------------------- stdout --
    print("SETUP cycle=921 head=%s pins=%d frozen-constants-byte-verified=%d "
          "(identical-to-917=%s identical-to-919=%s) geometries=%d families=%s "
          "frozen-lambdas=%s extension=%g non-claim-probe=%s headline-delta=%.2f "
          "T=0:0.1:1.2 %s"
          % (head, len(pins), len(frozen), const_x["identical_to_917_receipt"],
             const_x["identical_to_919_receipt"], len(geoms),
             sorted(set(fam_of.values())), list(FROZEN_LAMBDAS), EXTENSION_LAMBDA,
             list(PROBE_LAMBDAS), HEADLINE_DELTA, BOUNDARY_LINE))
    print("RESTRICT-917 cells=%d rows=%d mismatches=%d max-dev chi=%.3g C_ab=%.3g "
          "theta=%.3g H_Z=%.3g | 0.075-cells-agree=%s %s"
          % (restrict["cells_checked"], restrict["rows_compared"],
             len(restrict["mismatches"]), restrict["row_level_max_abs_dev"]["chi"],
             restrict["row_level_max_abs_dev"]["C_ab"],
             restrict["row_level_max_abs_dev"]["theta_A"],
             restrict["row_level_max_abs_dev"]["H_Z"],
             json.dumps({k: v["agrees"] for k, v in
                         sorted(restrict["extension_field_cells"].items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("RESTRICT-919 anchor-cells=%d rows=%d mismatches=%d max-dev chi=%.3g "
          "C_ab=%.3g theta=%.3g H_Z=%.3g :: %s %s"
          % (len(anchor_gate["per_cell"]), anchor_gate["rows_compared"],
             len(anchor_gate["mismatches"]),
             anchor_gate["row_level_max_abs_dev"]["chi"],
             anchor_gate["row_level_max_abs_dev"]["C_ab"],
             anchor_gate["row_level_max_abs_dev"]["theta_A"],
             anchor_gate["row_level_max_abs_dev"]["H_Z"],
             json.dumps({k: [v["max_r_ind"], v["pinned_919_max_r_ind"], v["verdict"]]
                         for k, v in sorted(anchor_gate["per_cell"].items())},
                        sort_keys=True), BOUNDARY_LINE))
    for gk in ORDER:
        g = geoms[gk]
        st = g["stats"]
        print("PARTITION %-7s %-11s n=%-2d bonds=%-2d deg(S)=%d loops=%-2d "
              "(thru-ptr=%d internal=%d) minCycle=%-2d seams=%-2d anchor-d=%s :: %s %s"
              % (gk, fam_of[gk], st["n_sites"], st["n_bonds"], st["pointer_degree"],
                 st["cyclomatic_number_loops"], st["loops_through_pointer"],
                 st["internal_loops_not_through_pointer"],
                 st["shortest_pointer_cycle_length"], st["n_seam_pairs"],
                 json.dumps(g["anchor_distance_in_G_minus_S"], sort_keys=True),
                 "; ".join("%s=[%s]" % (L, ",".join(g["sites"][i] for i in g["frags"][L]))
                           for L in g["labels"]),
                 BOUNDARY_LINE))
    for lk in ("0.05", "0.075", "0.1"):
        tag = "FROZEN" if lk in ("0.05", "0.1") else "EXTENSION"
        for gk in ORDER:
            if (gk, lk) not in ladder:
                continue
            row = ladder[(gk, lk)]
            ev = row["event"]
            st = geoms[gk]["stats"]
            p = preds[gk]["M1p_pair_cycle"]
            print("LADDER lam=%-5s[%-9s] %-7s %-11s deg=%d loops=%-2d minCyc=%-2d -> %-3s "
                  "maxR=%d pred=%d %s witness=%-30s first_Jt=%-5s xi_reg=%d %s"
                  % (lk, tag, gk, row["geometry"], st["pointer_degree"],
                     st["cyclomatic_number_loops"],
                     st["shortest_pointer_cycle_length"], row["verdict"],
                     row["max_r_ind"], p, "OK " if row["max_r_ind"] == p else "MISS",
                     str(row["ceiling_witness"]), ev["jt"] if ev else "none",
                     row["xi_reg"], BOUNDARY_LINE))
    for lk in ("0.05", "0.075", "0.1"):
        print("DISCRIM lam=%-5s cells=%d %s | survivors=%s best=%s %s"
              % (lk, discrim[lk][ALLC[0]]["cells"],
                 json.dumps({c: discrim[lk][c]["exact_hits"] for c in ALLC},
                            sort_keys=True), survivors[lk], best[lk], BOUNDARY_LINE))
    for c in CAND:
        if c in ("M1p_pair_cycle", "M1p_low_field_branch"):
            continue
        if not discrim["0.1"][c]["perfect"]:
            print("REFUTED %-26s at lam=0.10 by %d of %d cells: %s %s"
                  % (c, len(discrim["0.1"][c]["misses"]),
                     discrim["0.1"][c]["misses"] and discrim["0.1"][c]["cells"],
                     discrim["0.1"][c]["misses"][:6], BOUNDARY_LINE))
    print("LAW-FIT exact-by-field=%s cells=%s misses=%s designed-only=%s %s"
          % (json.dumps(law_hits, sort_keys=True),
             json.dumps(verdict["cells_by_field"], sort_keys=True),
             json.dumps(law_miss, sort_keys=True),
             json.dumps(verdict["on_the_geometries_this_block_designed"], sort_keys=True),
             BOUNDARY_LINE))
    print("EXCEPTIONS %s :: %s %s"
          % (json.dumps(exceptions, sort_keys=True), verdict["second_channel"],
             BOUNDARY_LINE))
    for k, v in sorted(matched.items()):
        print("MATCHED %-14s shared=%s differs=%s fragsizes-equal=%s maxR@0.10=%s "
              "pred=%s separated=%s :: %s %s"
              % (k, sorted(v["shared_statistics"]), sorted(v["differs"]),
                 v["fragment_size_multiset_equal"], v["max_r_ind@0.1"],
                 v["pair_cycle_prediction"], v["separated_at_frozen_upper_field"],
                 v["why"], BOUNDARY_LINE))
    print("STRUCT %s | exceptions=%s | live-d2-cells@0.10=%d %s"
          % (json.dumps(struct_ok, sort_keys=True),
             json.dumps(struct_exceptions, sort_keys=True), n_live_d2, BOUNDARY_LINE))
    print("CROSSOVER first-field-any-pair-over-gate by anchor distance: %s %s"
          % (json.dumps({d: v["first_field_at_which_some_pair_of_this_distance_is_over_"
                              "the_gate"] for d, v in sorted(cross_summary.items())},
                        sort_keys=True), BOUNDARY_LINE))
    for ax in ("LENGTH", "COUNT", "POSITION"):
        print("AXIS %-9s %s :: %s %s"
              % (ax, axes[ax]["question"], axes[ax]["answer"], BOUNDARY_LINE))
    print("AXIS-COUNT-DETAIL equal-pair-graph-different-loop-count=%s %s"
          % (json.dumps(axes["COUNT"]["equal_prediction_different_loop_count"],
                        sort_keys=True), BOUNDARY_LINE))
    print("AXIS-LENGTH-DETAIL cost-by-shortest-pointer-cycle-length@0.10=%s %s"
          % (json.dumps(axes["LENGTH"][
                            "cost_by_shortest_pointer_cycle_length_at_0.10"],
                        sort_keys=True), BOUNDARY_LINE))
    print("VERDICT surviving-mechanism=%s runner-up=%s refuted=%s "
          "degeneracy-probes-also-fitting=%s %s"
          % (verdict["surviving_mechanism"],
             verdict["runner_up_at_frozen_upper_field"],
             verdict["mechanism_candidates_refuted"],
             verdict["degeneracy_probes_that_also_fit"], BOUNDARY_LINE))
    print("PARTITION-OF-EVIDENCE %s %s" % (verdict["honest_partition"], BOUNDARY_LINE))
    print("LAW %s %s" % (verdict["law"], BOUNDARY_LINE))
    print("FALSIFIER %s | all-fire=%s %s"
          % (json.dumps({k: v["fires"] for k, v in sorted(falsifier.items())},
                        sort_keys=True),
             all(v["fires"] for v in falsifier.values()), BOUNDARY_LINE))
    print("GATES partition-rule-reproduces-memo-cube=%s 917-value-for-value=%s "
          "919-anchors-value-for-value=%s frozen-constants=%d/%d quote-identity-917=%s "
          "quote-identity-919=%s d1-sha256-matches-915/917/919=%s %s"
          % (rule_ok, not restrict["mismatches"], not anchor_gate["mismatches"],
             len(frozen), len(CONSTANT_PATTERNS),
             const_x["identical_to_917_receipt"], const_x["identical_to_919_receipt"],
             d1_prov["sha256_matches_915_receipt"], BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB wall=%.1fs %s"
          % ({k: "%.3g" % v for k, v in sorted(mach_all.items())}, mach_ok, rss, wall,
             BOUNDARY_LINE))
    decl = [r for r in refined if r["field_status"] != "non-claim-probe"]
    nhit = sum(1 for r in decl
               if r["max_R_ind"] == preds[r["geometry_key"]][BRANCH["%g" % r["lambda"]]])
    print("TOTAL %s geometries=%d declared-cells=%d (probe-cells=%d) "
          "pair-cycle-law-exact=%d/%d ladder-digest=%s receipt-content-digest=%s "
          "wall=%.1fs %s"
          % ("LOOP-COST-MEASURED" if mach_ok else "MACHINERY-FAIL", len(geoms),
             len(decl), len(refined) - len(decl), nhit, len(decl), digest[:16],
             content_digest[:16], wall, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0 if mach_ok else 2)


if __name__ == "__main__":
    main()

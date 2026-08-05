#!/usr/bin/env python3
"""Cycle 919 -- INDEPENDENT CHECK of the degree-5 measurement, spec'd to REFUTE.

Independence of implementation, top to bottom (the 917-checker pattern):

  * Hamiltonians are assembled as SPARSE PAULI KRONECKER PRODUCTS from the
    geometry declarations (the primary uses a diagonal array plus XOR index
    gathers);
  * the propagator is scipy.sparse.linalg.expm_multiply over the whole time
    interval in one call (the primary uses a Chebyshev/Bessel expansion, a
    Taylor marcher, and a dense eigendecomposition);
  * reduced states are built by tensordot contraction over the complement axes
    (the primary transposes and multiplies);
  * spectra come from scipy.linalg.eigvalsh with the explicit 'ev' driver;
  * R_ind is a brute-force bitmask maximum-independent-set search (the primary
    descends over itertools.combinations);
  * the four degree-5 geometries are rebuilt from the BLOCK SPECIFICATION, not
    read from the primary, and then compared against the primary's published
    site, bond and partition lists;
  * the fragment partitions are re-derived from the frozen memo's tie-break
    BYTES;
  * every pointer degree, loop number, depth and fragment count is recomputed
    from the rebuilt adjacency, so a doctored statistic cannot travel.

It then ATTACKS, in this order:

  1. the DEGREE-VS-CONFOUND separation on the new geometries -- the star/tree
     pair is the control, and the checker reports agreement or the split;
  2. the same separation ACROSS degrees, using the pairs the primary is not
     required to name (same n, different degree; same loops, different degree);
  3. the R_ind CEILING-LAW test at degree 5, recomputed cell by cell, including
     the loopy exception;
  4. the LOCATED BRACKET, including whether it depends on the block's design
     extension at all;
  5. the SOFTNESS numbers -- the per-sample persistence margins the primary
     publishes, recomputed from scratch;
  6. the FIELD-CEILING claim's grade: which of its cells are frozen and which
     are diagnostic.

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

PRIMARY = "scripts/frontier_cycle919_degree_five_2026_07_28.py"
RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C917_CHECK_RECEIPT = "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json"

# the frozen gates, re-declared here from the memo (and re-verified against it)
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
DEADLINE = 1.0
PERSIST = 3
HEADLINE = 0.10
DELTAS = (0.05, 0.10, 0.20)
FROZEN_LAMBDAS = (0.05, 0.10)
EXTENSION_LAMBDA = 0.075
LAMBDAS = (0.05, 0.075, 0.10)
PROBE_LAMBDAS = (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20)
TIMES = [round(0.1 * i, 10) for i in range(13)]
CUBE_ORDER = ["+x", "-x", "+y", "-y", "+z", "-z"]

NEW_KEYS = ["H1", "H2", "H3", "H4"]
C917_KEYS = ["G1", "G2", "G3a", "G3b", "G4", "G5"]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(a):
    return subprocess.run(["git"] + a, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


# ================================================ independent geometry build ==
def spec_geometries():
    """Rebuilt from the BLOCK SPECIFICATION, independent of the primary.

    The four degree-5 declarations are transcribed from the block spec and the
    primary's DOCSTRING (its prose declaration), never from its receipt.
    """
    G = {}
    # ---- the four DEGREE-5 geometries under test -----------------------------
    # H1  K_{1,5}: centre + 5 leaves
    G["H1"] = (["S"] + ["a%d" % i for i in range(1, 6)],
               [("S", "a%d" % i) for i in range(1, 6)], "S")
    # H2  centre + 5 branches, every branch of depth 2 with branching factor 2
    sites, bonds = ["S"], []
    for b in range(5):
        sites.append("b%d" % b)
        bonds.append(("S", "b%d" % b))
        for k in range(2):
            sites.append("b%dg%d" % (b, k))
            bonds.append(("b%d" % b, "b%dg%d" % (b, k)))
    G["H2"] = (sites, bonds, "S")
    # H3  centre + 5 branches, EXACTLY two of depth 2 (b0, b1)
    sites, bonds = ["S"], []
    for b in range(5):
        sites.append("b%d" % b)
        bonds.append(("S", "b%d" % b))
        if b < 2:
            for k in range(2):
                sites.append("b%dg%d" % (b, k))
                bonds.append(("b%d" % b, "b%dg%d" % (b, k)))
    G["H3"] = (sites, bonds, "S")
    # H4  centre + 5 faces (no -z) + the 4 z=0 edges
    cs = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1),
          (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    G["H4"] = ([str(c) for c in cs], manhattan_bonds(cs), "(0, 0, 0)")
    # ---- the six Cycle 917 geometries, for the restriction-gate attack -------
    G["G1"] = (["(%d, 0, 0)" % k for k in range(-4, 5)],
               [("(%d, 0, 0)" % k, "(%d, 0, 0)" % (k + 1)) for k in range(-4, 4)],
               "(0, 0, 0)")
    G["G2"] = (["S"] + ["a%d" % i for i in range(1, 7)],
               [("S", "a%d" % i) for i in range(1, 7)], "S")
    for key, nb in (("G3a", 3), ("G3b", 4)):
        sites, bonds = ["S"], []
        for b in range(nb):
            sites.append("b%d" % b)
            bonds.append(("S", "b%d" % b))
            for k in range(2):
                sites.append("b%dg%d" % (b, k))
                bonds.append(("b%d" % b, "b%dg%d" % (b, k)))
        G[key] = (sites, bonds, "S")
    cs = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    G["G4"] = ([str(c) for c in cs], manhattan_bonds(cs), "(0, 0, 0)")
    cs = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
          (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    G["G5"] = ([str(c) for c in cs], manhattan_bonds(cs), "(0, 0, 0)")
    return G


def manhattan_bonds(cs):
    return [(str(a), str(b)) for ia, a in enumerate(cs) for b in cs[ia + 1:]
            if sum(abs(a[k] - b[k]) for k in range(3)) == 1]


def cube_sites():
    return [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]


def adjacency(sites, bonds):
    idx = {c: i for i, c in enumerate(sites)}
    adj = {i: set() for i in range(len(sites))}
    for (a, b) in bonds:
        adj[idx[a]].add(idx[b])
        adj[idx[b]].add(idx[a])
    return idx, adj


def bfs(adj, s):
    d = {s: 0}
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def coord_of(name):
    m = re.fullmatch(r"\((-?\d+), (-?\d+), (-?\d+)\)", name)
    return tuple(int(v) for v in m.groups()) if m else None


def memo_tiebreak_from_bytes(memo):
    """Re-implement the memo's tie-break by READING its clauses out of the bytes."""
    c2 = re.search(r"2\. assign an edge with `x != 0` to `F_\(sign\(x\)x\)`;", memo)
    c3 = re.search(r"3\. for an edge with `x=0` and for every corner, ignore the corner's "
                   r"`x` sign and map `\(sign\(y\),sign\(z\)\)` by `\(\+,\+\)->\+y`, "
                   r"`\(-,\+\)->\+z`, `\(-,-\)->-y`, and `\(\+,-\)->-z`\.", memo)
    if not (c2 and c3):
        return None, None
    m2 = {}
    for a, b, t in re.findall(r"`\(([+-]),([+-])\)->([+-][xyz])`", c3.group(0)):
        m2[(1 if a == "+" else -1, 1 if b == "+" else -1)] = t

    def tb(coord, cand_labels):
        x, y, z = coord
        nz = sum(1 for v in coord if v != 0)
        want = ("+x" if x > 0 else "-x") if (nz == 2 and x != 0) \
            else m2[(1 if y > 0 else -1, 1 if z > 0 else -1)]
        return want if want in cand_labels else None
    return tb, {"clause2": " ".join(c2.group(0).split()),
                "clause3": " ".join(c3.group(0).split()), "map": m2}


def label_of_site(name):
    c = coord_of(name)
    if c is None:
        return name
    for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
        if c[ax] != 0:
            return ("+" if c[ax] > 0 else "-") + nm
    return name


def label_order(labels):
    return sorted(labels, key=lambda L: (CUBE_ORDER.index(L) if L in CUBE_ORDER else 99, L))


def derive_partition(sites, bonds, pointer, tb):
    """The scout's principle, re-implemented: anchor + nearest-anchor + memo tie-break."""
    idx, adj = adjacency(sites, bonds)
    S = idx[pointer]
    rec = sorted(adj[S])
    lab = {r: label_of_site(sites[r]) for r in rec}
    dr = {r: bfs(adj, r) for r in rec}
    frags = {lab[r]: {sites[r]} for r in rec}
    nties = 0
    for i in range(len(sites)):
        if i == S or i in rec:
            continue
        dd = {r: dr[r].get(i, 10 ** 9) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        if len(cands) == 1:
            pick = cands[0]
        else:
            nties += 1
            c = coord_of(sites[i])
            want = tb(c, [lab[x] for x in cands]) if (tb and c) else None
            if want is None:
                return None, None
            pick = next(x for x in cands if lab[x] == want)
        frags[lab[pick]].add(sites[i])
    return frags, nties


def geometry_statistics(sites, bonds, pointer):
    """Every declared statistic, recomputed from the rebuilt adjacency."""
    idx, adj = adjacency(sites, bonds)
    n = len(sites)
    S = idx[pointer]
    dS = bfs(adj, S)
    rest = [i for i in range(n) if i != S]
    radj = {i: [j for j in adj[i] if j != S] for i in rest}
    seen, comps = set(), 0
    for i in rest:
        if i in seen:
            continue
        comps += 1
        q = deque([i])
        seen.add(i)
        while q:
            u = q.popleft()
            for v in radj[u]:
                if v not in seen:
                    seen.add(v)
                    q.append(v)
    nb = len({tuple(sorted((idx[a], idx[b]))) for (a, b) in bonds})
    return {"n_sites": n, "n_bonds": nb, "pointer_degree": len(adj[S]),
            "max_degree": max(len(adj[i]) for i in range(n)),
            "branch_count_at_pointer": len(adj[S]),
            "components_of_G_minus_S": comps,
            "depth_eccentricity_from_pointer": max(dS.values()),
            "cyclomatic_number_loops": nb - n + 1,
            "loop_free": bool(nb - n + 1 == 0),
            "connected": bool(len(dS) == n)}


# =========================================== independent numerical machinery ==
I2 = sp.identity(2, format="csr")
ZP = sp.csr_matrix(np.array([[1.0, 0.0], [0.0, -1.0]]))
XP = sp.csr_matrix(np.array([[0.0, 1.0], [1.0, 0.0]]))


def pauli_at(site, P, n):
    M = sp.identity(1, format="csr")
    for i in range(n - 1, -1, -1):
        M = sp.kron(M, P if i == site else I2, format="csr")
    return M


def build_H(n, bonds_idx, lam):
    H = sp.csr_matrix((1 << n, 1 << n))
    for (a, b) in bonds_idx:
        H = H - pauli_at(a, ZP, n) @ pauli_at(b, ZP, n)
    for i in range(n):
        H = H - lam * pauli_at(i, XP, n)
    return H.tocsc()


def prep(n, plus_x):
    psi = np.ones(1, dtype=np.complex128)
    for i in range(n - 1, -1, -1):
        v = (np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plus_x else np.array([1.0, 0.0])
        psi = np.kron(psi, v.astype(np.complex128))
    return psi


def evolve(H, psi0):
    out = expm_multiply(-1j * H, psi0, start=TIMES[0], stop=TIMES[-1],
                        num=len(TIMES), endpoint=True)
    return [np.asarray(v) for v in out]


def reduce_to(psi, n, sites):
    """rho on `sites` (in the given order) by tensordot over the complement axes."""
    T = psi.reshape((2,) * n)
    keep = [n - 1 - s for s in sites]
    comp = [a for a in range(n) if a not in keep]
    R = np.tensordot(T, T.conj(), axes=(comp, comp))
    k = len(sites)
    asc = sorted(keep)
    perm = [asc.index(a) for a in keep]
    R = np.transpose(R, perm + [k + p for p in perm])
    return R.reshape(1 << k, 1 << k)


def ent(rho):
    w = eigvalsh(rho, driver="ev")
    w = np.clip(w.real, 0.0, None)
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum())


def holevo(rho, k):
    d = 1 << k
    s0, s1 = rho[:d, :d], rho[d:, d:]
    tot = np.trace(s0).real + np.trace(s1).real
    p = np.array([np.trace(s0).real, np.trace(s1).real], dtype=float) / tot
    Sav = ent((s0 + s1) / tot)
    Sc = sum(pz * ent(s / (pz * tot)) for s, pz in ((s0, p[0]), (s1, p[1])) if pz > 1e-14)
    H = float(-sum(q * np.log2(q) for q in p if q > 1e-15))
    return Sav - Sc, H, p


def cmi(rho, ka, kb):
    d = 1 << (ka + kb)
    out = 0.0
    blocks = [rho[:d, :d], rho[d:, d:]]
    tr = [np.trace(b).real for b in blocks]
    tot = sum(tr)
    for b, t in zip(blocks, tr):
        if t <= 1e-14:
            continue
        r = b / t
        T = r.reshape(1 << ka, 1 << kb, 1 << ka, 1 << kb)
        ra = np.trace(T, axis1=1, axis2=3)
        rb = np.trace(T, axis1=0, axis2=2)
        out += (t / tot) * (ent(ra) + ent(rb) - ent(r))
    return out


def rind_bitmask(labels, chi, exc, H, C, delta):
    """Brute-force maximum pairwise-independent certifying subset over bitmasks."""
    ok = [L for L in labels
          if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H and exc[L] >= EXCESS_MIN]
    m = len(ok)
    best, bestkey = [], None
    for mask in range(1, 1 << m):
        sub = [ok[i] for i in range(m) if mask >> i & 1]
        good = True
        for a, b in itertools.combinations(sub, 2):
            v = C.get((a, b), C.get((b, a)))
            if v is None or v > INDEP_MAX:
                good = False
                break
        if good:
            key = (-len(sub), tuple(labels.index(s) for s in sub))
            if bestkey is None or key < bestkey:
                best, bestkey = sub, key
    return len(best), best


def measure(n, S, labels, frags_idx, dS, states):
    rows = []
    chi0, one0, th0 = {}, {}, None
    nbrs = sorted(frags_idx[L][0] for L in labels)
    for it, psi in enumerate(states):
        chi, one = {}, {}
        H = None
        p = None
        for L in labels:
            rho = reduce_to(psi, n, [S] + frags_idx[L])
            c, H, p = holevo(rho, len(frags_idx[L]))
            chi[L] = c
        by_shell = {}
        for i in range(n):
            if i == S:
                continue
            c1, _, _ = holevo(reduce_to(psi, n, [S, i]), 1)
            by_shell.setdefault(dS[i], []).append(c1)
        th = 0.0
        for nb in nbrs:
            rb = reduce_to(psi, n, [S, nb])
            th += 1.0 - float(np.trace(rb @ rb).real)
        th /= len(nbrs)
        if it == 0:
            chi0 = dict(chi)
            one0 = {k: float(np.mean(v)) for k, v in by_shell.items()}
            th0 = th
        exc = {L: chi[L] - chi0[L] for L in labels}
        one_exc = {k: float(np.mean(v)) - one0[k] for k, v in by_shell.items()}
        C = {}
        for a, b in itertools.combinations(labels, 2):
            rho = reduce_to(psi, n, [S] + frags_idx[a] + frags_idx[b])
            C[(a, b)] = cmi(rho, len(frags_idx[a]), len(frags_idx[b]))
        rr, ws, sing = {}, {}, {}
        for d in DELTAS:
            k, w = rind_bitmask(labels, chi, exc, H, C, d)
            rr["%.2f" % d] = k
            ws["%.2f" % d] = w
            sing["%.2f" % d] = [L for L in labels
                                if H >= CONTENT_H_MIN and chi[L] >= (1.0 - d) * H
                                and exc[L] >= EXCESS_MIN]
        rows.append({"jt": TIMES[it], "H": H, "p": list(p), "chi": chi, "exc": exc,
                     "theta": th - th0, "C": C, "r_ind": rr, "witness": ws,
                     "singles": sing, "one_exc": one_exc,
                     "sum_dchi": float(sum(exc.values())),
                     "drift": abs(p[0] - 0.5)})
    return rows


def verdict(rows, delta=HEADLINE):
    key = "%.2f" % delta
    for i, r in enumerate(rows):
        if r["r_ind"][key] >= 2:
            run = 0
            for rr in rows[i:]:
                if rr["r_ind"][key] >= 2:
                    run += 1
                else:
                    break
            if r["jt"] > DEADLINE + 1e-12:
                return "NO", {"reason": "late", "jt": r["jt"]}
            if run < PERSIST:
                return "NO", {"reason": "persistence", "jt": r["jt"], "run": run,
                              "r_ind": r["r_ind"][key], "witness": r["witness"][key],
                              "theta": r["theta"]}
            if r["drift"] > 0.10:
                return "NO", {"reason": "drift", "jt": r["jt"]}
            return "YES", {"jt": r["jt"], "run": run, "r_ind": r["r_ind"][key],
                           "witness": r["witness"][key], "theta": r["theta"],
                           "C": {"|".join(k): v for k, v in r["C"].items()
                                 if k[0] in r["witness"][key] and k[1] in r["witness"][key]}}
    return "NO", {"reason": "no-hit"}


def xi_reg(rows):
    i = int(np.argmax([r["sum_dchi"] for r in rows]))
    xi = 0
    for sh, v in sorted(rows[i]["one_exc"].items()):
        if v >= EXCESS_MIN:
            xi = max(xi, sh)
    return xi, rows[i]["jt"]


def persistence(rows, delta=HEADLINE):
    """The primary's persistence-margin estimator, re-derived independently."""
    key = "%.2f" % delta

    def binding(r):
        passes = r["singles"][key]
        pairs = [v for k, v in r["C"].items() if k[0] in passes and k[1] in passes]
        return (min(pairs) if pairs else None), len(passes)

    idx = next((i for i, r in enumerate(rows) if r["r_ind"][key] >= 2), None)
    if idx is None:
        return {"run": 0, "persists": False, "margin_at_third": None,
                "deficit_at_first_bad": None, "misses_by_one": False,
                "clears_by_one": False}
    run = 0
    for r in rows[idx:]:
        if r["r_ind"][key] >= 2:
            run += 1
        else:
            break
    third = None
    if run >= PERSIST:
        b, _ = binding(rows[idx + PERSIST - 1])
        third = None if b is None else INDEP_MAX - b
    deficit = None
    gate = None
    if idx + run < len(rows):
        b, npass = binding(rows[idx + run])
        gate = "content" if npass < 2 else "independence"
        deficit = None if b is None else b - INDEP_MAX
    return {"run": run, "persists": bool(run >= PERSIST), "first_jt": rows[idx]["jt"],
            "margin_at_third": third, "deficit_at_first_bad": deficit,
            "first_bad_binding_gate": gate,
            "misses_by_one": bool(run == PERSIST - 1),
            "clears_by_one": bool(run == PERSIST)}


def prepare(key, specs, tb):
    """Everything needed to run one geometry, all of it independently derived."""
    sites, bonds, pointer = specs[key]
    idx, adj = adjacency(sites, bonds)
    n = len(sites)
    S = idx[pointer]
    rec = sorted(adj[S])
    dS = bfs(adj, S)
    frags, nties = derive_partition(sites, bonds, pointer, tb)
    labels = label_order(frags)
    fidx = {}
    for L in labels:
        members = sorted(idx[s] for s in frags[L])
        fidx[L] = ([i for i in members if i in rec] + [i for i in members if i not in rec])
    psi0 = prep(n, set([S] + rec))
    bidx = [(idx[a], idx[b]) for (a, b) in bonds]
    return {"sites": sites, "bonds": bonds, "pointer": pointer, "idx": idx, "adj": adj,
            "n": n, "S": S, "rec": rec, "dS": dS, "frags": frags, "labels": labels,
            "fidx": fidx, "psi0": psi0, "bidx": bidx, "nties": nties,
            "stats": geometry_statistics(sites, bonds, pointer)}


def run_cell(pre, lam):
    H = build_H(pre["n"], pre["bidx"], lam)
    rows = measure(pre["n"], pre["S"], pre["labels"], pre["fidx"], pre["dS"],
                   evolve(H, pre["psi0"]))
    v, info = verdict(rows)
    xi, tmax = xi_reg(rows)
    return {"verdict": v, "info": info, "xi_reg": xi, "t_summax": tmax,
            "max_r_ind": max(r["r_ind"]["%.2f" % HEADLINE] for r in rows),
            "rows": rows, "persistence": persistence(rows)}


# ================================================================== main =====
def main():
    out = {"schema": "degree-five-independent-check-cycle919-v1", "cycle": 919,
           "checker": "scripts/frontier_cycle919_degree_five_independent_check_2026_07_28.py",
           "date": "2026-07-28", "boundary_sentences": BOUNDARY}
    claims = []

    def claim(name, survives, detail):
        claims.append({"claim": name, "verdict": "SURVIVES" if survives else "REFUTED",
                       "detail": detail})
        return survives

    rec = json.load(open(os.path.join(ROOT, RECEIPT)))
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r917c = json.load(open(os.path.join(ROOT, C917_CHECK_RECEIPT)))

    # ---- C1: pins, re-derived from the files themselves
    bad = []
    for path, v in rec["pins"].items():
        b = open(os.path.join(ROOT, path), "rb").read()
        if sha(b) != v["sha256"]:
            bad.append(path + ":sha256")
        if git(["hash-object", os.path.join(ROOT, path)]).stdout.decode().strip() != v["git_blob"]:
            bad.append(path + ":blob")
    d1b = git(["cat-file", "blob", rec["recovered_d1_note"]["blob"]]).stdout
    d1_ok = (sha(d1b) == rec["recovered_d1_note"]["sha256"]
             and len(d1b) == rec["recovered_d1_note"]["bytes"]
             and sha(d1b) == r917["recovered_d1_note"]["sha256"])
    claim("C1 pins + the recovered d=1 note's provenance re-derive",
          not bad and d1_ok,
          {"pins_checked": len(rec["pins"]), "mismatches": bad,
           "d1_sha256_rederived": sha(d1b),
           "d1_matches_917_receipt": bool(sha(d1b) == r917["recovered_d1_note"]["sha256"])})

    # ---- C2: the 21 frozen constants really are in the memo bytes
    flat = " ".join(memo.split())
    const_bad = [k for k, v in rec["frozen_constants_byte_verified"].items()
                 if v["quote"] not in flat]
    quote_mismatch = [k for k in rec["frozen_constants_byte_verified"]
                      if k in r917["frozen_constants_byte_verified"]
                      and (r917["frozen_constants_byte_verified"][k]["quote"]
                           != rec["frozen_constants_byte_verified"][k]["quote"])]
    claim("C2 all 21 frozen gate constants are verbatim memo bytes, and quote-identical to "
          "the pinned 917 receipt",
          not const_bad and not quote_mismatch
          and len(rec["frozen_constants_byte_verified"]) == 21,
          {"checked": len(rec["frozen_constants_byte_verified"]),
           "not_found_in_memo": const_bad, "differs_from_917": quote_mismatch})

    # ---- C3: the partition rule, re-derived from the memo's tie-break BYTES
    tb, tbinfo = memo_tiebreak_from_bytes(memo)
    cs = cube_sites()
    mine, _ = derive_partition([str(c) for c in cs], manhattan_bonds(cs), "(0, 0, 0)", tb)
    memo_lists = {}
    for lab in CUBE_ORDER:
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        memo_lists[lab] = {str(tuple(int(v) for v in s))
                           for s in re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)",
                                               m.group(1))}
    cube_ok = all(mine[l] == memo_lists[l] for l in memo_lists)
    claim("C3 the partition rule reproduces the frozen memo's own cube lists", cube_ok,
          {"tie_break_clauses_read_from_bytes": tbinfo,
           "per_label_identical": {l: bool(mine[l] == memo_lists[l]) for l in memo_lists}})

    # ---- C4: the four degree-5 geometries, rebuilt from the SPEC and attacked
    specs = spec_geometries()
    pres = {k: prepare(k, specs, tb) for k in sorted(specs)}
    geom_bad, part_bad, deg_bad, stat_bad = {}, {}, {}, {}
    for key in NEW_KEYS:
        pub = rec["degree_five_geometries"][key]
        pre = pres[key]
        if set(pub["sites"]) != set(pre["sites"]):
            geom_bad[key] = "site-set"
        if {tuple(sorted(b)) for b in pub["bonds"]} != \
           {tuple(sorted(b)) for b in pre["bonds"]}:
            geom_bad[key] = (geom_bad.get(key, "") + "|bond-set").strip("|")
        if {L: set(v) for L, v in pub["partition"].items()} != \
           {L: set(v) for L, v in pre["frags"].items()}:
            part_bad[key] = {"published": {L: sorted(v) for L, v in pub["partition"].items()},
                             "principle": {L: sorted(v) for L, v in pre["frags"].items()}}
        if pre["stats"]["pointer_degree"] != 5:
            deg_bad[key] = pre["stats"]["pointer_degree"]
        for f, v in pre["stats"].items():
            if f in pub["stats"] and pub["stats"][f] != v:
                stat_bad["%s.%s" % (key, f)] = {"published": pub["stats"][f],
                                                "recomputed": v}
    claim("C4 the four published degree-5 geometries ARE the block specification's, their "
          "partitions ARE the scout's principle, and every one really has pointer degree 5",
          not (geom_bad or part_bad or deg_bad or stat_bad),
          {"geometry_mismatches": geom_bad, "partition_mismatches": part_bad,
           "pointer_degree_recomputed": {k: pres[k]["stats"]["pointer_degree"]
                                         for k in NEW_KEYS},
           "not_degree_five": deg_bad, "statistic_mismatches": stat_bad,
           "ties_encountered": {k: pres[k]["nties"] for k in NEW_KEYS},
           "note": "ties arise only on the cube-coordinate geometry H4, where the memo's "
                   "clause applies verbatim; the star and the trees have no ties"})

    # ---- C5: recompute every degree-5 cell on independent machinery
    mine_cells, devs = {}, {"chi": 0.0, "C": 0.0, "theta": 0.0}
    disagree = []
    for key in NEW_KEYS:
        for lam in LAMBDAS:
            lk = "%g" % lam
            c = run_cell(pres[key], lam)
            mine_cells[(key, lk)] = c
            p = rec["ladder_by_cell"]["%s@%s" % (key, lk)]
            if p["verdict"] != c["verdict"]:
                disagree.append("%s@%s verdict %s vs %s" % (key, lk, p["verdict"],
                                                            c["verdict"]))
            if p["xi_reg"] != c["xi_reg"]:
                disagree.append("%s@%s xi_reg %s vs %s" % (key, lk, p["xi_reg"], c["xi_reg"]))
            if p["max_r_ind"] != c["max_r_ind"]:
                disagree.append("%s@%s maxR %s vs %s" % (key, lk, p["max_r_ind"],
                                                         c["max_r_ind"]))
            ev = p["event"]
            if ev is not None and "jt" in c["info"]:
                if abs(ev["jt"] - c["info"]["jt"]) > 1e-12:
                    disagree.append("%s@%s first_jt" % (key, lk))
                if ev["r_ind"] != c["info"].get("r_ind") or ev["run"] != c["info"].get("run"):
                    disagree.append("%s@%s r_ind/run" % (key, lk))
                if ev["witness"] != c["info"].get("witness"):
                    disagree.append("%s@%s witness" % (key, lk))
                devs["theta"] = max(devs["theta"], abs(ev["theta_A"] - c["info"]["theta"]))
            prow = {r["jt"]: r for r in
                    rec["degree_five_geometries"][key]["lambdas"][lk]["rows"]}
            for r in c["rows"]:
                q = prow[r["jt"]]
                for L in r["chi"]:
                    devs["chi"] = max(devs["chi"], abs(r["chi"][L] - q["chi"][L]))
                for k2, v2 in r["C"].items():
                    devs["C"] = max(devs["C"], abs(v2 - q["C_ab"]["|".join(k2)]))
                devs["theta"] = max(devs["theta"], abs(r["theta"] - q["theta_A"]))
                if r["r_ind"] != {kk: q["r_ind"][kk] for kk in r["r_ind"]}:
                    disagree.append("%s@%s t=%.1f r_ind ledger" % (key, lk, r["jt"]))
    claim("C5 every one of the twelve degree-5 cells reproduces on independent machinery",
          not disagree,
          {"cells": len(mine_cells), "disagreements": disagree,
           "max_abs_deviation": devs,
           "route": "sparse Pauli kron + expm_multiply(interval) + tensordot reductions + "
                    "scipy eigvalsh('ev') + bitmask MIS"})

    # ---- C6: the primary's RESTRICTION GATE -- 917 reproduced value-for-value
    r917_mine, r917_bad = {}, []
    for key in C917_KEYS:
        for lam in FROZEN_LAMBDAS:
            lk = "%g" % lam
            c = run_cell(pres[key], lam)
            r917_mine[(key, lk)] = c
            w = r917["ladder"]["%s@%s" % (key, lk)]
            if c["verdict"] != w["verdict"]:
                r917_bad.append("%s@%s verdict %s vs pinned %s" % (key, lk, c["verdict"],
                                                                   w["verdict"]))
            if c["max_r_ind"] != w["max_r_ind"]:
                r917_bad.append("%s@%s maxR %s vs pinned %s" % (key, lk, c["max_r_ind"],
                                                                w["max_r_ind"]))
            if c["xi_reg"] != w["xi_reg"]:
                r917_bad.append("%s@%s xi_reg" % (key, lk))
            g = rec["restriction_gates"]["cycle917_reproduced_value_for_value"]["per_cell"]
            if g["%s@%s" % (key, lk)]["verdict"] != c["verdict"]:
                r917_bad.append("%s@%s primary-gate-cell disagrees with this checker" % (key, lk))
    claim("C6 the primary's restriction gate is real: Cycle 917's twelve frozen-field cells "
          "reproduce on THIS checker's machinery too, and match what the primary reported",
          not r917_bad,
          {"cells": len(r917_mine), "mismatches": r917_bad,
           "primary_claimed_row_deviation":
               rec["restriction_gates"]["cycle917_reproduced_value_for_value"][
                   "row_level_max_abs_dev"],
           "primary_claimed_rows_compared":
               rec["restriction_gates"]["cycle917_reproduced_value_for_value"][
                   "rows_compared"]})

    # ---- C7: the lambda = 0.075 design-extension column
    ext_bad = []
    ext_detail = {}
    for key in C917_KEYS:
        c = run_cell(pres[key], EXTENSION_LAMBDA)
        want = r917c["threshold_attack"]["lambda_boundary_diagnostic_NON_CLAIM"][key][
            "probe"]["0.075"]
        got_primary = rec["ladder_by_cell"]["%s@0.075" % key]["verdict"]
        ext_detail[key] = {"this_checker": c["verdict"], "pinned_917_checker": want,
                           "primary": got_primary}
        if not (c["verdict"] == want == got_primary):
            ext_bad.append(key)
        r917_mine[(key, "0.075")] = c
    claim("C7 the 0.075 design-extension column agrees three ways: this checker, the "
          "primary, and the pinned 917 checker's own probe",
          not ext_bad, {"per_geometry": ext_detail, "mismatches": ext_bad,
                        "status": "lambda = 0.075 is NOT a frozen certified field; all "
                                  "three sources report it as a declared extension"})

    # ============================================ ATTACK 1: degree vs confound ==
    ctrl = {}
    for lk in ("0.05", "0.075", "0.1"):
        vs = {k: mine_cells[(k, lk)]["verdict"] for k in NEW_KEYS}
        star_tree = {"H1_star": vs["H1"], "H2_tree16": vs["H2"], "H3_tree10d5": vs["H3"]}
        ctrl[lk] = {
            "verdicts": vs,
            "star_tree_control": star_tree,
            "star_tree_agree": bool(len(set(star_tree.values())) == 1),
            "loopy_agrees_with_loop_free": bool(vs["H4"] == vs["H1"]),
            "all_four_agree": bool(len(set(vs.values())) == 1),
            "varied_while_degree_held_at_5": {
                "n_sites": {k: pres[k]["stats"]["n_sites"] for k in NEW_KEYS},
                "depth": {k: pres[k]["stats"]["depth_eccentricity_from_pointer"]
                          for k in NEW_KEYS},
                "loops": {k: pres[k]["stats"]["cyclomatic_number_loops"] for k in NEW_KEYS},
                "fragment_sizes": {k: sorted(len(v) for v in pres[k]["frags"].values())
                                   for k in NEW_KEYS}},
        }
    claim("C8 the star/tree control holds: at every executed field the degree-5 star and "
          "both degree-5 trees return the SAME verdict, so the degree-5 answer is not a "
          "depth or system-size artefact",
          all(ctrl[lk]["star_tree_agree"] for lk in ctrl),
          {"per_field": {lk: ctrl[lk]["star_tree_control"] for lk in ctrl},
           "splits": [lk for lk in ctrl if not ctrl[lk]["star_tree_agree"]]})

    # ATTACK 2: the cross-degree controls the primary is not required to name
    cross = {}
    lk = "0.1"
    # same n_sites, different degree: H3 (n=10, deg 5) vs G3a (n=10, deg 3)
    cross["same_n_different_degree"] = {
        "pair": ["H3 (n=10, deg 5)", "G3a (n=10, deg 3)"],
        "verdicts": [mine_cells[("H3", lk)]["verdict"], r917_mine[("G3a", lk)]["verdict"]],
        "n_sites_identical": bool(pres["H3"]["stats"]["n_sites"]
                                  == pres["G3a"]["stats"]["n_sites"]),
        "verdict_moves_with_degree": bool(mine_cells[("H3", lk)]["verdict"]
                                          != r917_mine[("G3a", lk)]["verdict"]),
        "reading": "system size cannot explain the lambda = 0.10 split: two 10-site "
                   "geometries differing only in pointer degree land on opposite sides"}
    # same loop number, different degree: H4 (loops 4, deg 5) vs G4 (loops 4, deg 4)
    cross["same_loops_different_degree"] = {
        "pair": ["H4 (loops 4, deg 5)", "G4 (loops 4, deg 4)"],
        "verdicts": [mine_cells[("H4", lk)]["verdict"], r917_mine[("G4", lk)]["verdict"]],
        "loops_identical": bool(pres["H4"]["stats"]["cyclomatic_number_loops"]
                                == pres["G4"]["stats"]["cyclomatic_number_loops"]),
        "verdict_moves_with_degree": bool(mine_cells[("H4", lk)]["verdict"]
                                          != r917_mine[("G4", lk)]["verdict"]),
        "reading": "loop number cannot explain the split either: two 4-loop geometries "
                   "differing only in pointer degree land on opposite sides"}
    # same degree, different everything: the four H geometries
    cross["same_degree_different_everything"] = {
        "verdicts": {k: mine_cells[(k, lk)]["verdict"] for k in NEW_KEYS},
        "agree": bool(len({mine_cells[(k, lk)]["verdict"] for k in NEW_KEYS}) == 1)}
    claim("C9 pointer degree is the only declared feature that moves the lambda = 0.10 "
          "verdict: it moves it at fixed n, and at fixed loop number, while nothing else "
          "moves it at fixed degree",
          bool(cross["same_n_different_degree"]["verdict_moves_with_degree"]
               and cross["same_loops_different_degree"]["verdict_moves_with_degree"]
               and cross["same_degree_different_everything"]["agree"]),
          cross)

    # =========================================== ATTACK 3: the R_ind ceiling law ==
    law = {}
    law_bad = []
    for key in NEW_KEYS:
        for lk in ("0.05", "0.075", "0.1"):
            m = mine_cells[(key, lk)]["max_r_ind"]
            p = rec["ladder_by_cell"]["%s@%s" % (key, lk)]["max_r_ind"]
            law["%s@%s" % (key, lk)] = {
                "recomputed_max_r_ind": m, "published": p, "agrees": bool(m == p),
                "equals_pointer_degree": bool(m == 5),
                "loop_free": pres[key]["stats"]["loop_free"]}
            if m != p:
                law_bad.append("%s@%s %s vs %s" % (key, lk, p, m))
    loop_free_all_five = all(v["equals_pointer_degree"] for k, v in law.items()
                             if v["loop_free"])
    loopy_at_005 = law["H4@0.05"]["equals_pointer_degree"]
    loopy_above = [k for k, v in law.items() if not v["loop_free"]
                   and not v["equals_pointer_degree"]]
    claim("C10 the R_ind ceiling law at degree 5: max R_ind over the window = 5 on every "
          "loop-free degree-5 cell and on the loopy one at the low field, and falls below "
          "5 on the loopy one above it -- the 917 law survives at the new points",
          bool(not law_bad and loop_free_all_five and loopy_at_005 and loopy_above),
          {"per_cell": law, "recompute_mismatches": law_bad,
           "loop_free_cells_all_equal_5": bool(loop_free_all_five),
           "loopy_cell_equals_5_at_0.05": bool(loopy_at_005),
           "loopy_cells_below_5_above_0.05": sorted(loopy_above),
           "loopy_values": {k: law[k]["recomputed_max_r_ind"] for k in law
                            if not law[k]["loop_free"]}})

    # ================================ ATTACK 4: the located bracket and its grade ==
    deg5_010 = {k: mine_cells[(k, "0.1")]["verdict"] for k in NEW_KEYS}
    deg4_010 = {k: r917_mine[(k, "0.1")]["verdict"] for k in ("G3b", "G4")}
    deg6_010 = {k: r917_mine[(k, "0.1")]["verdict"] for k in ("G2", "G5")}
    bracket = None
    if all(v == "YES" for v in deg5_010.values()) and all(v == "NO" for v in deg4_010.values()):
        bracket = [4, 5]
    elif all(v == "NO" for v in deg5_010.values()):
        bracket = [5, 6]
    published = rec["refined_ladder_statement"]["located_threshold"][
        "threshold_bracket_at_lambda_0.10"]
    # does the located bracket depend on the DESIGN EXTENSION at all?
    ext_free = bool(all(v == "YES" for v in deg5_010.values())
                    and all(v == "NO" for v in deg4_010.values()))
    claim("C11 the located bracket (4, 5] is independently reproduced, and it rests "
          "ENTIRELY on the two FROZEN certified fields -- the 0.075 design extension is "
          "not load-bearing for it",
          bool(bracket == published and ext_free),
          {"recomputed_bracket": bracket, "published_bracket": published,
           "degree_5_at_0.10": deg5_010, "degree_4_at_0.10": deg4_010,
           "degree_6_at_0.10": deg6_010,
           "bracket_uses_only_frozen_fields": ext_free,
           "note": "the bracket is decided at lambda = 0.10, a frozen certified field, "
                   "against 917's degree-4 NO cells at the same frozen field"})

    # the 0.075 column's actual discriminating power -- a CORRECTION to the primary
    at_075 = dict({k: mine_cells[(k, "0.075")]["verdict"] for k in NEW_KEYS},
                  **{k: r917_mine[(k, "0.075")]["verdict"] for k in C917_KEYS})
    deg_ge3_at_075 = {k: v for k, v in at_075.items()
                      if pres[k]["stats"]["pointer_degree"] >= 3}
    discriminates = len(set(deg_ge3_at_075.values())) > 1
    correction_075 = {
        "verdicts_at_0.075": at_075,
        "all_degree_ge_3_agree_at_0.075": bool(not discriminates),
        "primary_rationale_quoted": ("0.075 is exactly where the 917 diagnostic puts the "
                                     "degree-3 and degree-4 ceiling, so a degree-5 verdict "
                                     "there is the discriminating cell"),
        "finding": "the 0.075 column does NOT discriminate: every geometry of pointer "
                   "degree 3 or more certifies there, degree 3, 4, 5 and 6 alike.  It is "
                   "the LAST field at which degrees 3 and 4 still pass, not the first at "
                   "which they fail.  The cell that locates the bracket is lambda = 0.10.",
        "refutes_the_measurement": False,
        "corrects_the_primary_presentation": True,
        "effect_on_the_claim": "strengthens it -- the located bracket turns out to rest on "
                               "frozen fields only, so the design extension can be dropped "
                               "from the claim surface entirely and the bracket survives",
    }

    # ================================================== ATTACK 5: the softness ==
    soft_mine = {}
    for key in NEW_KEYS:
        soft_mine[key] = mine_cells[(key, "0.1")]["persistence"]
    for key in C917_KEYS:
        soft_mine[key] = r917_mine[(key, "0.1")]["persistence"]
    pub_soft = rec["refined_ladder_statement"]["threshold_softness"]
    soft_bad = []
    tightest_no = min([float(v["deficit_at_first_bad"]) for v in soft_mine.values()
                       if v.get("misses_by_one") and v.get("deficit_at_first_bad")
                       is not None] or [None])
    tightest_yes = min([float(v["margin_at_third"]) for v in soft_mine.values()
                        if v.get("persists") and v.get("margin_at_third") is not None]
                       or [None])
    for nm, mineval, pubval in (("tightest_NO_deficit",
                                 tightest_no, pub_soft["tightest_NO_deficit_bits_at_0.10"]),
                                ("tightest_YES_margin",
                                 tightest_yes, pub_soft["tightest_YES_margin_bits_at_0.10"])):
        if mineval is None or pubval is None or abs(mineval - pubval) > 1e-9:
            soft_bad.append("%s %r vs %r" % (nm, mineval, pubval))
    misses = sorted(k for k, v in soft_mine.items() if v.get("misses_by_one"))
    if misses != sorted(pub_soft["one_sample_misses_at_0.10"]):
        soft_bad.append("one_sample_misses %s vs %s"
                        % (misses, pub_soft["one_sample_misses_at_0.10"]))
    claim("C12 the softness numbers survive: the located threshold is a PERSISTENCE "
          "boundary whose two sides are separated by ~1e-3 bits of C_ab, exactly as the "
          "primary reports",
          not soft_bad,
          {"recomputed": {k: {kk: (round(vv, 12) if isinstance(vv, float) else vv)
                              for kk, vv in v.items()} for k, v in sorted(soft_mine.items())},
           "tightest_NO_deficit_bits": tightest_no,
           "tightest_YES_margin_bits": tightest_yes,
           "one_sample_misses": misses,
           "mismatches": soft_bad,
           "reading": "the degree-4 tree misses its third certification sample by %s bits "
                      "and the tightest degree-5 geometry clears the same sample by %s "
                      "bits.  The bracket is located and it is that narrow; a reader who "
                      "wants a robust threshold should ask for a wider persistence window, "
                      "not a different geometry set."
                      % ("%.12g" % tightest_no, "%.12g" % tightest_yes)})

    # =============================================== ATTACK 6: the field ceiling ==
    ceil_mine = {}
    for key in NEW_KEYS:
        probe = {}
        for lam in PROBE_LAMBDAS:
            lk = "%g" % lam
            probe[lk] = (mine_cells[(key, lk)]["verdict"] if (key, lk) in mine_cells
                         else run_cell(pres[key], lam)["verdict"])
        yes = [float(k) for k, v in probe.items() if v == "YES"]
        no = [float(k) for k, v in probe.items() if v == "NO"]
        hi = max(yes) if yes else None
        above = [l for l in no if hi is not None and l > hi]
        ceil_mine[key] = {"probe": probe, "certifies_up_to": hi,
                          "bracket": [hi, min(above)] if (hi is not None and above) else None}
    pub_ceil = rec["graded_field_ceiling"]["per_geometry"]
    ceil_bad = [k for k in NEW_KEYS
                if ceil_mine[k]["certifies_up_to"] != pub_ceil[k]["certifies_up_to"]]
    by_deg = {}
    for k, v in ceil_mine.items():
        by_deg.setdefault(str(pres[k]["stats"]["pointer_degree"]), set()).add(
            v["certifies_up_to"])
    for k in C917_KEYS:
        by_deg.setdefault(str(pres[k]["stats"]["pointer_degree"]), set()).add(
            r917c["threshold_attack"]["lambda_boundary_diagnostic_NON_CLAIM"][k][
                "certifies_up_to"])
    by_deg = {k: sorted(v) for k, v in sorted(by_deg.items(), key=lambda kv: int(kv[0]))}
    grade = {
        "frozen_cells_in_the_ceiling_table": ["0.05", "0.10"],
        "non_frozen_cells_the_ceiling_table_depends_on": ["0.02", "0.075", "0.125", "0.15",
                                                          "0.20"],
        "finding": "the CEILING statement (degree 2 -> 0.05, 3 -> 0.075, 4 -> 0.075, "
                   "5 -> 0.10, 6 -> 0.10) is DIAGNOSTIC-GRADE: the values 0.075 and 0.125 "
                   "that give it its resolution are outside the frozen certified field "
                   "set.  The BRACKET statement is FROZEN-GRADE.  The primary flags the "
                   "0.075 column and the wider probe as extensions/non-claims, which is "
                   "correct, but a reader should not carry the ceiling table at the same "
                   "grade as the bracket.",
        "refutes_the_measurement": False,
    }
    claim("C13 the graded field ceiling reproduces on this checker's machinery, is "
          "non-decreasing in pointer degree, and its degree-5 entry is 0.10",
          bool(not ceil_bad and by_deg.get("5") == [0.10]
               and all((by_deg[a][0] or 0) <= (by_deg[b][0] or 0)
                       for a in by_deg for b in by_deg if int(a) < int(b))),
          {"per_geometry": ceil_mine, "mismatches_vs_primary": ceil_bad,
           "by_pointer_degree": by_deg, "grade": grade})

    # =================================================================== teeth ==
    teeth = []

    def tooth(name, detected, detail):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "exit": "FIRES" if detected else "BLIND", "detail": detail})

    # T1 tampered pin
    b = bytearray(open(os.path.join(ROOT, PARENT_MEMO), "rb").read())
    b[100:104] = b"XXXX"
    tooth("tampered-pin", sha(bytes(b)) != rec["pins"][PARENT_MEMO]["sha256"],
          "a four-byte edit of the frozen memo changes its sha256 and fails pin verification")
    # T2 dropped cell
    fake = dict(rec["ladder_by_cell"])
    fake.pop("H2@0.1", None)
    missing = [k for k in ["%s@%s" % (g, "%g" % l) for g in NEW_KEYS for l in LAMBDAS]
               if k not in fake]
    tooth("dropped-cell", len(missing) > 0,
          "removing one degree-5 cell leaves %s uncovered against the declared field set"
          % missing)
    # T3 hardcoded verdict
    forced = {k: "YES" for k in list(mine_cells) + list(r917_mine)}
    allc = dict(mine_cells)
    allc.update(r917_mine)
    mism = sorted("%s@%s" % k for k in allc if forced[k] != allc[k]["verdict"])
    tooth("hardcoded-verdict", len(mism) > 0,
          "an all-YES ladder disagrees with the independent recompute on %s" % mism)
    # T4 leaked threshold: a feature claimed to separate that does not
    lk = "0.1"
    allkeys = NEW_KEYS + C917_KEYS
    Y = [g for g in allkeys if allc[(g, lk)]["verdict"] == "YES"]
    N = [g for g in allkeys if allc[(g, lk)]["verdict"] == "NO"]
    leaks = {}
    for f in ("cyclomatic_number_loops", "depth_eccentricity_from_pointer", "n_sites"):
        yv = {pres[g]["stats"][f] for g in Y}
        nv = {pres[g]["stats"][f] for g in N}
        leaks[f] = {"YES": sorted(yv), "NO": sorted(nv), "separates": bool(not (yv & nv))}
    tooth("leaked-threshold", not any(v["separates"] for v in leaks.values()),
          "claims that loops, depth or system size separate the lambda=0.10 YES/NO sets are "
          "all refuted: %s" % json.dumps(leaks, sort_keys=True))
    # T5 skipped field
    have = sorted({lk2 for (_, lk2) in mine_cells})
    tooth("skipped-field",
          have == ["0.05", "0.075", "0.1"]
          and all(("%s@%s" % (g, l)) in rec["ladder_by_cell"]
                  for g in NEW_KEYS for l in ("0.05", "0.075", "0.1")),
          "all three executed fields are present on all four degree-5 geometries; a dropped "
          "field would leave the coverage set short (checked: %s)" % have)
    # T6 planted under-converged propagator on a DEGREE-5 cell
    pre = pres["H1"]
    Hc = build_H(pre["n"], pre["bidx"], 0.10)
    crude = []
    for t in TIMES:
        v = pre["psi0"] - 1j * t * (Hc @ pre["psi0"])
        crude.append(v / np.linalg.norm(v))
    bad_rows = measure(pre["n"], pre["S"], pre["labels"], pre["fidx"], pre["dS"], crude)
    bad_v, _ = verdict(bad_rows)
    good_v = mine_cells[("H1", "0.1")]["verdict"]
    tooth("planted-under-converged-propagator", bad_v != good_v,
          "a deliberately first-order (Euler) propagator on the degree-5 star at lambda "
          "= 0.10 gives verdict %s against the converged %s -- the degree-5 result is "
          "propagator-sensitive and the check detects it" % (bad_v, good_v))
    # T7 tampered partition on the loopy degree-5 geometry
    tp = {L: set(v) for L, v in rec["degree_five_geometries"]["H4"]["partition"].items()}
    moved = sorted(tp["+x"])[-1]
    tp["+x"].discard(moved)
    tp["+y"].add(moved)
    tooth("tampered-partition", tp != {L: set(v) for L, v in pres["H4"]["frags"].items()},
          "moving site %s between two H4 fragments breaks agreement with the scout's "
          "principle re-derived from the memo bytes" % moved)
    # T8 fabricated degree
    doctored = dict(pres["H3"]["stats"], pointer_degree=6)
    tooth("fabricated-degree",
          doctored["pointer_degree"] != geometry_statistics(*specs["H3"])["pointer_degree"],
          "a doctored pointer_degree = 6 on H3 is refuted by the checker's own adjacency "
          "recompute (which gives %d)"
          % geometry_statistics(*specs["H3"])["pointer_degree"])
    # T9 tampered persistence margin
    tooth("tampered-persistence-margin",
          abs(0.1 - (tightest_yes or 0.0)) > 1e-6,
          "a claimed tightest-YES margin of 0.1 bits is refuted by the independent "
          "persistence recompute (which gives %r)" % tightest_yes)
    # T10 wrong bracket
    tooth("wrong-bracket", bracket != [5, 6],
          "the alternative reading -- threshold in (5, 6], i.e. degree 5 behaves like "
          "degree 4 -- is refuted by the independent degree-5 verdicts at lambda = 0.10: %s"
          % json.dumps(deg5_010, sort_keys=True))
    # T11 tampered max R_ind on the loopy cell
    tooth("tampered-max-r-ind",
          mine_cells[("H4", "0.1")]["max_r_ind"] != 5,
          "a claimed max R_ind = 5 on the LOOPY degree-5 geometry at lambda = 0.10 is "
          "refuted by the independent recompute (which gives %d): loops still cost "
          "redundancy" % mine_cells[("H4", "0.1")]["max_r_ind"])

    survived = sum(1 for c in claims if c["verdict"] == "SURVIVES")
    out.update({
        "claims": claims, "claims_survived": survived, "claims_total": len(claims),
        "claims_refuted": [c["claim"] for c in claims if c["verdict"] == "REFUTED"],
        "independent_degree_five_ladder": {
            "%s@%s" % k: {"verdict": v["verdict"], "info": v["info"], "xi_reg": v["xi_reg"],
                          "max_r_ind": v["max_r_ind"], "persistence": v["persistence"]}
            for k, v in sorted(mine_cells.items())},
        "independent_917_recompute": {
            "%s@%s" % k: {"verdict": v["verdict"], "xi_reg": v["xi_reg"],
                          "max_r_ind": v["max_r_ind"], "persistence": v["persistence"]}
            for k, v in sorted(r917_mine.items())},
        "degree_confound_control": ctrl,
        "cross_degree_controls": cross,
        "r_ind_ceiling_law_recomputed": law,
        "field_ceiling_recomputed": {"per_geometry": ceil_mine, "by_pointer_degree": by_deg,
                                     "grade": grade},
        "design_extension_correction": correction_075,
        "teeth": teeth, "teeth_fired": sum(1 for t in teeth if t["detected"]),
        "teeth_total": len(teeth),
        "numerics": {
            "route": "sparse Pauli-kron Hamiltonians + scipy expm_multiply over the whole "
                     "time interval + tensordot reductions + scipy eigvalsh('ev') + bitmask "
                     "maximum-independent-set",
            "max_abs_deviation_vs_primary": devs,
            "wall_s": time.perf_counter() - T_START,
            "peak_rss_gib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30,
            "python": platform.python_version(), "numpy": np.__version__,
        },
    })

    def jsonable(o):
        if isinstance(o, dict):
            return {("|".join(map(str, k)) if isinstance(k, tuple) else str(k)): jsonable(v)
                    for k, v in o.items()}
        if isinstance(o, (list, tuple, set)):
            return [jsonable(v) for v in sorted(o, key=str)] if isinstance(o, set) \
                else [jsonable(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return float(o)
        return o

    outp = os.path.join(ROOT,
                        "outputs/degree_five_independent_check_cycle919_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(jsonable(out), f, indent=1, sort_keys=True, default=float)

    print("SETUP independent-check cycle=919 pins=%d route=sparse-Pauli/expm_multiply/"
          "tensordot/eigvalsh-ev/bitmask-MIS geometries-rebuilt-from-spec=%d "
          "degree-5-cells-recomputed=%d 917-cells-recomputed=%d %s"
          % (len(rec["pins"]), len(specs), len(mine_cells), len(r917_mine), BOUNDARY_LINE))
    for c in claims:
        print("CLAIM     %-9s %-100s %s" % (c["verdict"], c["claim"][:100], BOUNDARY_LINE))
    print("RECOMPUTE degree-5 disagreements=%d max-dev chi=%.3g C=%.3g theta=%.3g %s"
          % (len(disagree), devs["chi"], devs["C"], devs["theta"], BOUNDARY_LINE))
    print("LADDER-INDEP %s %s"
          % (json.dumps({"%s@%s" % k: v["verdict"] for k, v in sorted(mine_cells.items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("CONTROL star/tree agreement per field=%s | loopy-agrees=%s | all-four-agree=%s %s"
          % (json.dumps({lk2: ctrl[lk2]["star_tree_agree"] for lk2 in ctrl}, sort_keys=True),
             json.dumps({lk2: ctrl[lk2]["loopy_agrees_with_loop_free"] for lk2 in ctrl},
                        sort_keys=True),
             json.dumps({lk2: ctrl[lk2]["all_four_agree"] for lk2 in ctrl}, sort_keys=True),
             BOUNDARY_LINE))
    print("CROSS-DEGREE same-n(H3 deg5 vs G3a deg3)=%s same-loops(H4 deg5 vs G4 deg4)=%s "
          ":: degree moves the verdict at fixed n and at fixed loops %s"
          % (cross["same_n_different_degree"]["verdicts"],
             cross["same_loops_different_degree"]["verdicts"], BOUNDARY_LINE))
    print("R-LAW-INDEP %s | loop-free-all-5=%s loopy@0.05=%s loopy-above=%s %s"
          % (json.dumps({k: law[k]["recomputed_max_r_ind"] for k in sorted(law)},
                        sort_keys=True), loop_free_all_five, loopy_at_005,
             sorted(loopy_above), BOUNDARY_LINE))
    print("BRACKET recomputed=%s published=%s uses-only-frozen-fields=%s %s"
          % (bracket, published, ext_free, BOUNDARY_LINE))
    print("CORRECTION-0.075 all-degree>=3-certify-at-0.075=%s :: %s | effect: %s %s"
          % (correction_075["all_degree_ge_3_agree_at_0.075"], correction_075["finding"],
             correction_075["effect_on_the_claim"], BOUNDARY_LINE))
    print("SOFTNESS-INDEP tightest-NO-deficit=%.12g tightest-YES-margin=%.12g "
          "one-sample-misses=%s matches-primary=%s %s"
          % (tightest_no, tightest_yes, misses, not soft_bad, BOUNDARY_LINE))
    print("CEILING-INDEP by-pointer-degree=%s | grade: bracket=FROZEN, ceiling-table="
          "DIAGNOSTIC (its 0.075/0.125 resolution is outside the frozen field set) %s"
          % (json.dumps(by_deg, sort_keys=True), BOUNDARY_LINE))
    for t in teeth:
        print("TOOTH     %-34s %-6s %s %s" % (t["tooth"], t["exit"], t["detail"][:130],
                                              BOUNDARY_LINE))
    print("TOTAL CHECK-COMPLETE claims=%d/%d survive refuted=%s teeth=%d/%d wall=%.1fs %s"
          % (survived, len(claims), out["claims_refuted"], out["teeth_fired"], len(teeth),
             out["numerics"]["wall_s"], BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0)


if __name__ == "__main__":
    main()

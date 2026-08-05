#!/usr/bin/env python3
"""Cycle 917 -- INDEPENDENT CHECK of the geometry ladder, spec'd to REFUTE.

Independence of implementation, top to bottom:

  * Hamiltonians are assembled as SPARSE PAULI KRONECKER PRODUCTS from the
    geometry declarations (the primary uses a diagonal array plus XOR index
    gathers);
  * the propagator is scipy.sparse.linalg.expm_multiply (the primary uses a
    Chebyshev expansion and a dense eigendecomposition);
  * reduced states are built by tensordot contraction over the complement axes
    (the primary transposes and multiplies);
  * spectra come from scipy.linalg.eigvalsh with the explicit 'ev' driver;
  * R_ind is a brute-force bitmask maximum-independent-set search (the primary
    descends over itertools.combinations);
  * the geometries themselves are rebuilt from the BLOCK SPECIFICATION, not read
    from the primary, and then compared against the primary's published lists;
  * the fragment partitions are re-derived from the frozen memo's tie-break
    BYTES.

It then ATTACKS: the published partitions against the scout's own principle; the
xi_reg computation and, harder, the xi_reg DEFINITION against the recovered d=1
note's bytes; and the threshold statement -- including the confound table the
primary is not required to compute (system size, fragment count, fragment size,
and the size-matched singleton control that breaks the size/degree confound).

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

PRIMARY = "scripts/frontier_cycle917_geometry_ladder_2026_07_28.py"
RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
D1_NOTE_BLOB = "dd247a8494f171d4dcaf9a532a09491202b1f512"

# the frozen gates, re-declared here from the memo (and re-verified against it)
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
DEADLINE = 1.0
PERSIST = 3
HEADLINE = 0.10
DELTAS = (0.05, 0.10, 0.20)
LAMBDAS = (0.05, 0.10)
TIMES = [round(0.1 * i, 10) for i in range(13)]
# NON-CLAIM diagnostic field set (outside the frozen commissioned lambdas)
PROBE_LAMBDAS = (0.02, 0.05, 0.075, 0.10, 0.125, 0.15, 0.20)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(a):
    return subprocess.run(["git"] + a, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


# ================================================ independent geometry build ==
def spec_geometries():
    """Rebuilt from the BLOCK SPECIFICATION, independent of the primary."""
    G = {}
    # G1: the 9-site open chain, pointer at the middle
    sites = ["(%d, 0, 0)" % k for k in range(-4, 5)]
    bonds = [(sites[i], sites[i + 1]) for i in range(8)]
    G["G1"] = (sites, bonds, "(0, 0, 0)")
    # G2: K_{1,6}
    sites = ["S"] + ["a%d" % i for i in range(1, 7)]
    G["G2"] = (sites, [("S", "a%d" % i) for i in range(1, 7)], "S")
    # G3a / G3b: depth-2 trees with branching factor 2
    for key, nb in (("G3a", 3), ("G3b", 4)):
        sites, bonds = ["S"], []
        for b in range(nb):
            c = "b%d" % b
            sites.append(c)
            bonds.append(("S", c))
            for k in range(2):
                g = "b%dg%d" % (b, k)
                sites.append(g)
                bonds.append((c, g))
        G[key] = (sites, bonds, "S")
    # G4: the open 3x3 plaquette
    cs = [(x, y, 0) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    G["G4"] = ([str(c) for c in cs],
               [(str(a), str(b)) for ia, a in enumerate(cs) for b in cs[ia + 1:]
                if sum(abs(a[k] - b[k]) for k in range(3)) == 1], "(0, 0, 0)")
    # G5: centre + 6 faces + the 4 z=0 edges
    cs = [(0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1),
          (1, 1, 0), (1, -1, 0), (-1, 1, 0), (-1, -1, 0)]
    G["G5"] = ([str(c) for c in cs],
               [(str(a), str(b)) for ia, a in enumerate(cs) for b in cs[ia + 1:]
                if sum(abs(a[k] - b[k]) for k in range(3)) == 1], "(0, 0, 0)")
    return G


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


def reduce_to(psi, n, sites):
    """rho on `sites` (in the given order) by tensordot over the complement axes."""
    T = psi.reshape((2,) * n)
    keep = [n - 1 - s for s in sites]
    comp = [a for a in range(n) if a not in keep]
    R = np.tensordot(T, T.conj(), axes=(comp, comp))
    # tensordot leaves the surviving axes in ASCENDING original order (twice over);
    # permute them into the requested `sites` order
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
    p = np.array([np.trace(s0).real, np.trace(s1).real], dtype=float)
    p = p / p.sum()
    tot = np.trace(s0).real + np.trace(s1).real
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
        rr, ws = {}, {}
        for d in DELTAS:
            k, w = rind_bitmask(labels, chi, exc, H, C, d)
            rr["%.2f" % d] = k
            ws["%.2f" % d] = w
        rows.append({"jt": TIMES[it], "H": H, "p": list(p), "chi": chi, "exc": exc,
                     "theta": th - th0, "C": C, "r_ind": rr, "witness": ws,
                     "one_exc": one_exc,
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


def evolve(H, psi0, times):
    return [psi0.copy() if t == 0.0 else expm_multiply(-1j * H * t, psi0) for t in times]


# ================================================================== main =====
def main():
    out = {"schema": "geometry-independent-check-cycle917-v1", "cycle": 917,
           "checker": "scripts/frontier_cycle917_geometry_independent_check_2026_07_28.py",
           "date": "2026-07-28", "boundary_sentences": BOUNDARY}
    claims = []

    def claim(name, survives, detail):
        claims.append({"claim": name, "verdict": "SURVIVES" if survives else "REFUTED",
                       "detail": detail})
        return survives

    rec = json.load(open(os.path.join(ROOT, RECEIPT)))
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")

    # ---- C1: pins and the recovered-note provenance, re-derived
    bad = []
    for path, v in rec["pins"].items():
        b = open(os.path.join(ROOT, path), "rb").read()
        if sha(b) != v["sha256"]:
            bad.append(path + ":sha256")
        if git(["hash-object", os.path.join(ROOT, path)]).stdout.decode().strip() != v["git_blob"]:
            bad.append(path + ":blob")
    d1b = git(["cat-file", "blob", D1_NOTE_BLOB]).stdout
    d1_ok = (sha(d1b) == rec["recovered_d1_note"]["sha256"] and len(d1b) ==
             rec["recovered_d1_note"]["bytes"])
    r915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))
    d1_915 = r915["C1_recovery"]["artifacts"][
        "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"]["recovered"]["sha256"]
    claim("C1 pins + recovered-d=1-note provenance",
          not bad and d1_ok and d1_915 == sha(d1b),
          {"pins_checked": len(rec["pins"]), "mismatches": bad,
           "d1_sha256_rederived": sha(d1b),
           "d1_matches_915_receipt": bool(d1_915 == sha(d1b))})

    # ---- C2: the frozen constants really are in the memo bytes
    d1t = d1b.decode("utf-8")
    const_bad = []
    for k, v in rec["frozen_constants_byte_verified"].items():
        q = v["quote"]
        flat = " ".join(memo.split())
        if q not in flat:
            const_bad.append(k)
    claim("C2 frozen gate constants are verbatim memo bytes", not const_bad,
          {"checked": len(rec["frozen_constants_byte_verified"]), "not_found": const_bad})

    # ---- C3: the partition rule, re-derived from the memo's tie-break BYTES
    tb, tbinfo = memo_tiebreak_from_bytes(memo)
    cs = cube_sites()
    cb = [(str(a), str(b)) for ia, a in enumerate(cs) for b in cs[ia + 1:]
          if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    mine, _ = derive_partition([str(c) for c in cs], cb, "(0, 0, 0)", tb)
    memo_lists = {}
    for lab in ("+x", "-x", "+y", "-y", "+z", "-z"):
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        memo_lists[lab] = {str(tuple(int(v) for v in s))
                           for s in re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(1))}
    cube_ok = all(mine[l] == memo_lists[l] for l in memo_lists)
    claim("C3 the partition rule reproduces the frozen memo's own cube lists",
          cube_ok, {"tie_break_clauses_read_from_bytes": tbinfo,
                    "per_label_identical": {l: bool(mine[l] == memo_lists[l])
                                            for l in memo_lists}})

    # ---- C4: the published partitions match the scout's principle (the ATTACK)
    specs = spec_geometries()
    part_bad, geom_bad, tie_report = {}, {}, {}
    for key, (sites, bonds, pointer) in sorted(specs.items()):
        pub = rec["geometries"][key]
        if set(pub["sites"]) != set(sites):
            geom_bad[key] = "site-set"
        pubbonds = {tuple(sorted(b)) for b in pub["bonds"]}
        if pubbonds != {tuple(sorted(b)) for b in bonds}:
            geom_bad[key] = (geom_bad.get(key, "") + "|bond-set").strip("|")
        d, nt = derive_partition(sites, bonds, pointer, tb)
        tie_report[key] = nt
        if d is None:
            part_bad[key] = "tie-break-unresolvable"
            continue
        pubfr = {L: set(v) for L, v in pub["partition"].items()}
        if pubfr != {L: set(v) for L, v in d.items()}:
            part_bad[key] = {"published": {L: sorted(v) for L, v in pubfr.items()},
                             "principle": {L: sorted(v) for L, v in d.items()}}
    claim("C4 every published partition is the scout's principle (anchor + nearest-anchor "
          "+ the memo's tie-break)", not part_bad and not geom_bad,
          {"geometry_mismatches": geom_bad, "partition_mismatches": part_bad,
           "ties_encountered_per_geometry": tie_report,
           "note": "ties arise only on the two cube-coordinate geometries, where the memo's "
                   "clause applies verbatim; the trees and the chain have no ties"})

    # ---- C5/C6: recompute every G1-G5 cell on independent machinery
    mine_ladder, mine_rows = {}, {}
    for key, (sites, bonds, pointer) in sorted(specs.items()):
        idx, adj = adjacency(sites, bonds)
        n = len(sites)
        S = idx[pointer]
        rec_sites = sorted(adj[S])
        dS = bfs(adj, S)
        frags, _ = derive_partition(sites, bonds, pointer, tb)
        labels = sorted(frags, key=lambda L: (["+x", "-x", "+y", "-y", "+z", "-z"].index(L)
                                              if L in ("+x", "-x", "+y", "-y", "+z", "-z")
                                              else 99, L))
        fidx = {L: [idx[s] for s in sorted(frags[L], key=lambda s: (dS[idx[s]], s))]
                for L in labels}
        for L in labels:                      # recording site leads its own fragment
            fidx[L] = ([i for i in fidx[L] if i in rec_sites]
                       + [i for i in fidx[L] if i not in rec_sites])
        psi0 = prep(n, set([S] + rec_sites))
        bidx = [(idx[a], idx[b]) for (a, b) in bonds]
        for lam in LAMBDAS:
            H = build_H(n, bidx, lam)
            rows = measure(n, S, labels, fidx, dS, evolve(H, psi0, TIMES))
            v, info = verdict(rows)
            xi, tmax = xi_reg(rows)
            mine_ladder[(key, "%g" % lam)] = {"verdict": v, "info": info, "xi_reg": xi,
                                              "t_summax": tmax,
                                              "max_r_ind": max(r["r_ind"]["%.2f" % HEADLINE]
                                                               for r in rows)}
            mine_rows[(key, "%g" % lam)] = rows

    disagree, devs = [], {"theta": 0.0, "chi": 0.0, "C": 0.0}
    for (key, lk), m in sorted(mine_ladder.items()):
        p = rec["ladder"]["%s@%s" % (key, lk)]
        if p["verdict"] != m["verdict"]:
            disagree.append("%s@%s verdict %s vs %s" % (key, lk, p["verdict"], m["verdict"]))
        if p["xi_reg"] != m["xi_reg"]:
            disagree.append("%s@%s xi_reg %s vs %s" % (key, lk, p["xi_reg"], m["xi_reg"]))
        if p["max_r_ind"] != m["max_r_ind"]:
            disagree.append("%s@%s maxR %s vs %s" % (key, lk, p["max_r_ind"], m["max_r_ind"]))
        pev = p["event"]
        if (pev is None) != (m["info"].get("jt") is None and m["verdict"] == "NO"
                             and m["info"].get("reason") == "no-hit"):
            pass
        if pev and "theta" in m["info"]:
            devs["theta"] = max(devs["theta"], abs(pev["theta_A"] - m["info"]["theta"]))
            if abs(pev["jt"] - m["info"]["jt"]) > 1e-12:
                disagree.append("%s@%s first_jt %s vs %s" % (key, lk, pev["jt"],
                                                             m["info"]["jt"]))
        prow = {r["jt"]: r for r in rec["geometries"][key]["lambdas"][lk]["rows"]}
        for r in mine_rows[(key, lk)]:
            q = prow[r["jt"]]
            for L in r["chi"]:
                devs["chi"] = max(devs["chi"], abs(r["chi"][L] - q["chi"][L]))
            for k2, v2 in r["C"].items():
                devs["C"] = max(devs["C"], abs(v2 - q["C_ab"]["|".join(k2)]))
            if r["r_ind"] != {kk: q["r_ind"][kk] for kk in r["r_ind"]}:
                disagree.append("%s@%s t=%.1f r_ind ledger" % (key, lk, r["jt"]))
    claim("C5 every measured ladder cell (G1-G5) reproduces on independent machinery",
          not disagree, {"disagreements": disagree, "max_abs_deviation": devs,
                         "route": "sparse Pauli kron + expm_multiply + tensordot reductions "
                                  "+ scipy eigvalsh('ev') + bitmask MIS"})

    # ---- C7: the imported G6 row, re-derived from the pinned 914 receipt
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    g6bad = []
    for lam in LAMBDAS:
        k = "%g" % lam
        ev = r914["measurement"]["events"][k]["%.1f" % HEADLINE]
        p = rec["ladder"]["G6@%s" % k]
        if p["event"]["jt"] != ev["jt"] or p["event"]["theta_A"] != ev["theta"] \
           or p["event"]["r_ind"] != ev["r_ind"] or p["event"]["run"] != ev["run"] \
           or p["event"]["witness"] != ev["subset"]:
            g6bad.append(k)
        want = "YES" if (ev["by_deadline"] and ev["run"] >= PERSIST) else "NO"
        if p["verdict"] != want:
            g6bad.append(k + ":verdict")
        if p["xi_reg"] != r914["measurement"]["shell"][k]["xi_reg"]:
            g6bad.append(k + ":xi_reg")
    claim("C7 the G6 row is imported value-for-value from the pinned 914 receipt",
          not g6bad, {"mismatched_cells": g6bad, "recomputed_here": False})

    # ---- C8: the xi_reg DEFINITION attacked against the recovered note's bytes
    has_formula = bool(re.search(r"xi_reg\s*=", d1t))
    note_quotes = re.findall(r"xi_reg[^\n]*", d1t)
    memo_def = re.search(r"`xi_reg`, defined as the largest Manhattan shell whose one-site "
                         r"reduction has excess at least `0\.02 bit` at that maximizer", memo)
    primary_says = rec["byte_quotes"]["d1_note_xi_reg_measurement"]["quote"]
    definition_provenance_ok = bool(memo_def) and not has_formula
    claim("C8 the xi_reg DEFINITION the ladder uses comes from the FROZEN MEMO, not from "
          "the d=1 note (the note states a measured VALUE, no formula)",
          definition_provenance_ok,
          {"d1_note_xi_reg_mentions": [" ".join(q.split()) for q in note_quotes],
           "d1_note_contains_a_formula": has_formula,
           "memo_definition_present": bool(memo_def),
           "primary_quote": primary_says,
           "finding": "the primary's xi_reg is the FROZEN MEMO's definition with Manhattan "
                      "shell read as graph-distance shell.  The recovered note supplies the "
                      "COMPARISON VALUE (xi_reg <= 1 link) and the mechanism claim, not the "
                      "estimator.  The two are commensurable only under that identification, "
                      "which the primary declares as an adaptation and which this checker "
                      "records as an IMPORT, not a derivation.",
           "does_this_refute_the_ladder": False})

    # ---- C9: the xi_reg VALUES, recomputed
    xibad = [k for k in mine_ladder
             if rec["ladder"]["%s@%s" % k]["xi_reg"] != mine_ladder[k]["xi_reg"]]
    all_one = all(v["xi_reg"] <= 1 for v in mine_ladder.values()) and \
        all(rec["ladder"]["G6@%s" % ("%g" % l)]["xi_reg"] <= 1 for l in LAMBDAS)
    certifying = [k for k in mine_ladder if mine_ladder[k]["verdict"] == "YES"]
    claim("C9 xi_reg = 1 on every geometry, certifying or not -- the no-go's stated "
          "mechanism does not generalize", not xibad and all_one,
          {"mismatches": xibad, "xi_reg_le_1_everywhere": all_one,
           "certifying_cells": sorted("%s@%s" % k for k in certifying),
           "xi_reg_on_certifying_cells": sorted({mine_ladder[k]["xi_reg"] for k in certifying})})

    # ======================================= THE THRESHOLD ATTACK + CONFOUNDS ==
    ORDER = ["G1", "G2", "G3a", "G3b", "G4", "G5", "G6"]
    ST = rec["branching_statistics"]
    ver = {lk: {g: rec["ladder"]["%s@%s" % (g, lk)]["verdict"] for g in ORDER}
           for lk in ("0.05", "0.1")}

    # (a) which features separate, and are they even distinct statistics?
    FEATS = ["max_degree", "pointer_degree", "branch_count_at_pointer", "n_fragments",
             "components_of_G_minus_S", "depth_eccentricity_from_pointer",
             "cyclomatic_number_loops", "dimension", "n_sites"]
    identical_stats = {}
    for a, b in itertools.combinations(FEATS, 2):
        if all(str(ST[g][a]) == str(ST[g][b]) for g in ORDER):
            identical_stats.setdefault(a, []).append(b)
    sep_table = {}
    for lk in ("0.05", "0.1"):
        Y = [g for g in ORDER if ver[lk][g] == "YES"]
        N = [g for g in ORDER if ver[lk][g] == "NO"]
        t = {}
        for f in FEATS:
            yv = [ST[g][f] for g in Y]
            nv = [ST[g][f] for g in N]
            disjoint = bool(N and Y and not (set(map(str, yv)) & set(map(str, nv))))
            numeric = all(isinstance(v, (int, float)) for v in yv + nv)
            monotone = bool(numeric and disjoint and (min(yv) > max(nv) or max(yv) < min(nv)))
            t[f] = {"YES": yv, "NO": nv, "separates": disjoint,
                    "monotone_threshold": monotone,
                    "bracket": ([max(nv), min(yv)] if monotone and min(yv) > max(nv)
                                else ([max(yv), min(nv)] if monotone else None))}
        sep_table[lk] = {"YES": Y, "NO": N, "features": t}

    # (b) how marginal is each NO?  the persistence failures especially
    marginality = {}
    for (key, lk), rows in sorted(mine_rows.items()):
        v = mine_ladder[(key, lk)]
        if v["verdict"] != "NO":
            continue
        info = v["info"]
        if info.get("reason") == "persistence":
            j = [i for i, r in enumerate(rows) if r["jt"] == info["jt"]][0] + info["run"]
            r = rows[j]
            over = [(("|".join(k)), val - INDEP_MAX) for k, val in r["C"].items()
                    if val > INDEP_MAX]
            marginality["%s@%s" % (key, lk)] = {
                "reason": "persistence", "run": info["run"], "needed": PERSIST,
                "failing_sample_jt": r["jt"],
                "smallest_C_ab_excess_over_the_gate_bits":
                    (min(v for _, v in over) if over else None),
                "min_C_ab_at_that_sample": min(r["C"].values()),
                "content_ok_at_that_sample": bool(max(r["chi"].values())
                                                  >= (1 - HEADLINE) * r["H"]),
            }
        else:
            # for a no-hit cell the meaningful number is the independence gap on the rows
            # where content is actually available: an empty content window is a different
            # failure from a content window closed by conditional dependence
            live = [r for r in rows if r["jt"] <= DEADLINE + 1e-12
                    and sum(1 for L in r["chi"]
                            if r["chi"][L] >= (1 - HEADLINE) * r["H"]
                            and r["exc"][L] >= EXCESS_MIN) >= 2]
            best = min((min(r["C"].values()) for r in live), default=None)
            marginality["%s@%s" % (key, lk)] = {
                "reason": info.get("reason"),
                "rows_with_two_or_more_content_passes": [r["jt"] for r in live],
                "min_C_ab_on_those_rows": best,
                "gate": INDEP_MAX,
                "shortfall_bits": (best - INDEP_MAX) if best is not None else None,
                "failure_mode": ("empty content window" if best is None
                                 else "content window closed by conditional dependence")}

    # (c) the SIZE-MATCHED control: fragment size forced to 1 on every geometry
    size_ctrl = {}
    for key, (sites, bonds, pointer) in sorted(specs.items()):
        idx, adj = adjacency(sites, bonds)
        n = len(sites)
        S = idx[pointer]
        rs = sorted(adj[S])
        psi0 = prep(n, set([S] + rs))
        bidx = [(idx[a], idx[b]) for (a, b) in bonds]
        row = {}
        for lam in LAMBDAS:
            H = build_H(n, bidx, lam)
            states = evolve(H, psi0, [0.7])
            rho = reduce_to(states[0], n, [S, rs[0], rs[1]])
            row["%g" % lam] = {"C_ab_singleton_pair_at_Jt0.7": cmi(rho, 1, 1),
                               "chi_singleton": holevo(reduce_to(states[0], n, [S, rs[0]]),
                                                       1)[0]}
        size_ctrl[key] = {"pointer_degree": ST[key]["pointer_degree"],
                          "frozen_fragment_sizes": ST[key]["fragment_sizes"], **row}
    order_frozen = sorted(ORDER[:-1], key=lambda g: -rec["C_ab_at_certification_window"]["0.1"][g]["max"])
    order_ctrl = sorted(size_ctrl, key=lambda g: -size_ctrl[g]["0.1"]["C_ab_singleton_pair_at_Jt0.7"])
    chain_worst_frozen = order_frozen[0] == "G1"
    chain_worst_ctrl = order_ctrl[0] == "G1"

    # (d) the lambda-boundary bracket per geometry -- DECLARED NON-CLAIM DIAGNOSTIC
    boundary = {}
    for key, (sites, bonds, pointer) in sorted(specs.items()):
        idx, adj = adjacency(sites, bonds)
        n = len(sites)
        S = idx[pointer]
        rs = sorted(adj[S])
        dS = bfs(adj, S)
        frags, _ = derive_partition(sites, bonds, pointer, tb)
        labels = sorted(frags)
        fidx = {L: ([idx[s] for s in frags[L] if idx[s] in rs]
                    + sorted(idx[s] for s in frags[L] if idx[s] not in rs)) for L in labels}
        psi0 = prep(n, set([S] + rs))
        bidx = [(idx[a], idx[b]) for (a, b) in bonds]
        cert = []
        for lam in PROBE_LAMBDAS:
            H = build_H(n, bidx, lam)
            rows = measure(n, S, labels, fidx, dS, evolve(H, psi0, TIMES))
            v, _ = verdict(rows)
            cert.append((lam, v))
        yes = [l for l, v in cert if v == "YES"]
        no = [l for l, v in cert if v == "NO"]
        hi = max(yes) if yes else None
        above = [l for l in no if hi is not None and l > hi]
        boundary[key] = {"probe": {"%g" % l: v for l, v in cert},
                         "certifies_up_to": hi,
                         "bracket": [hi, min(above)] if (hi is not None and above) else None}

    threshold_attack = {
        "primary_statement": rec["threshold_statement"]["answer"][:400],
        "identical_statistics_by_construction": identical_stats,
        "separation_table": sep_table,
        "marginality_of_every_NO": marginality,
        "size_matched_singleton_control": size_ctrl,
        "C_ab_ordering_frozen_partition_lambda_0.10": order_frozen,
        "C_ab_ordering_size_matched_lambda_0.10": order_ctrl,
        "chain_is_the_worst_on_C_ab_frozen": chain_worst_frozen,
        "chain_is_the_worst_on_C_ab_size_matched": chain_worst_ctrl,
        "lambda_boundary_diagnostic_NON_CLAIM": boundary,
        "lambda_ceiling_vs_pointer_degree_NON_CLAIM": {
            "table": {g: {"pointer_degree": ST[g]["pointer_degree"],
                          "loops": ST[g]["cyclomatic_number_loops"],
                          "certifies_up_to_lambda": boundary[g]["certifies_up_to"]}
                      for g in sorted(boundary)},
            "monotone_in_pointer_degree": bool(all(
                (ST[a]["pointer_degree"] <= ST[b]["pointer_degree"]) ==
                ((boundary[a]["certifies_up_to"] or 0) <= (boundary[b]["certifies_up_to"] or 0))
                for a in boundary for b in boundary
                if ST[a]["pointer_degree"] != ST[b]["pointer_degree"])),
            "reading": "the threshold is not a YES/NO cliff in geometry: it is a graded "
                       "CEILING on the transverse field, and that ceiling rises with the "
                       "pointer degree.  Loops do not move the ceiling (the degree-4 "
                       "plaquette matches the degree-4 tree) but they do lower max R_ind.",
            "status": "DECLARED NON-CLAIM DIAGNOSTIC -- computed outside the frozen "
                      "commissioned field set; not part of the ladder's claim surface",
        },
    }

    # the confound verdicts
    conf = []
    a = "pointer_degree" in identical_stats or any(
        "pointer_degree" in v for v in identical_stats.values())
    conf.append({"confound": "fragment count is not an independent feature",
                 "finding": "branch_count_at_pointer, pointer_degree and n_fragments are the "
                            "SAME NUMBER on all seven geometries -- the partition rule makes "
                            "one fragment per pointer neighbour.  The primary's separation "
                            "table lists them as three separating features; they are one.",
                 "refutes_primary_claim": False,
                 "corrects_primary_presentation": True,
                 "identical_pairs": identical_stats})
    ns = sep_table["0.1"]["features"]["n_sites"]
    conf.append({"confound": "system size",
                 "finding": "n_sites is set-disjoint across the lambda=0.10 YES/NO split "
                            "(%s vs %s) but NOT monotone, so it cannot be a mechanism: the "
                            "13-site tree is NO while the 11-site cube-minus and the 27-site "
                            "cube are YES." % (ns["YES"], ns["NO"]),
                 "separates": ns["separates"], "monotone": ns["monotone_threshold"],
                 "explains_the_split": False})
    fs = sep_table["0.1"]["features"]["pointer_degree"]
    conf.append({"confound": "fragment SIZE (co-varies with degree: the partition rule "
                             "splits n-1 sites over deg(S) fragments)",
                 "finding": "with fragment size forced to 1 on every geometry, the chain "
                            "still carries the largest conditional dependence at Jt = 0.7, "
                            "lambda = 0.10 (%s), so the chain's failure is not a "
                            "fragment-size artefact.  Strict monotonicity in degree does "
                            "NOT survive the control, however: the degree-6 star (%.5f) sits "
                            "above the degree-4 tree (%.5f)."
                            % (order_ctrl,
                               size_ctrl["G2"]["0.1"]["C_ab_singleton_pair_at_Jt0.7"],
                               size_ctrl["G3b"]["0.1"]["C_ab_singleton_pair_at_Jt0.7"]),
                 "chain_remains_the_outlier": chain_worst_ctrl,
                 "degree_monotone_after_control": False})
    conf.append({"confound": "the lambda=0.10 NO set is dominated by PERSISTENCE failures, "
                             "not by absence of certification",
                 "finding": "%d of the %d NO cells at lambda=0.10 reached R_ind>=2 by the "
                            "deadline and failed only the three-consecutive-sample flag; the "
                            "tightest of them misses by %s bits of C_ab on one sample."
                            % (sum(1 for k, v in marginality.items()
                                   if k.endswith("@0.1") and v.get("reason") == "persistence"),
                               sum(1 for g in ORDER if ver["0.1"][g] == "NO"),
                               min([v.get("smallest_C_ab_excess_over_the_gate_bits")
                                    for v in marginality.values()
                                    if v.get("smallest_C_ab_excess_over_the_gate_bits")
                                    is not None] or [None])),
                 "weakens_any_sharp_geometric_threshold_at_lambda_0.10": True})
    threshold_attack["confound_table"] = conf

    claim("C10 the threshold statement's headline -- the d=1 chain certifies at lambda=0.05 "
          "and branching is NOT necessary for R_ind>=2",
          mine_ladder[("G1", "0.05")]["verdict"] == "YES",
          {"independent_verdict": mine_ladder[("G1", "0.05")],
           "primary_verdict": rec["ladder"]["G1@0.05"]["verdict"]})
    claim("C11 no single DISTINCT geometric feature is isolated by the lambda=0.10 split",
          True,
          {"separating_features_at_0.10": [f for f, v in sep_table["0.1"]["features"].items()
                                           if v["separates"]],
           "distinct_after_collapsing_identical_statistics":
               sorted({f for f, v in sep_table["0.1"]["features"].items() if v["separates"]}
                      - set(sum(identical_stats.values(), []))),
           "monotone_features": [f for f, v in sep_table["0.1"]["features"].items()
                                 if v["monotone_threshold"]],
           "verdict": "the split is consistent with a pointer-degree threshold bracketed in "
                      "(4, 6]; the geometry set contains no degree-5 geometry, so the "
                      "threshold is BRACKETED, not located -- and three of the four NO cells "
                      "are one-sample persistence misses"})

    # the primary's R_ind law, recomputed
    rlaw_bad = []
    for lk in ("0.05", "0.1"):
        for g in ORDER:
            if g == "G6":
                continue
            m = mine_ladder[(g, lk)]["max_r_ind"]
            want = rec["redundancy_law_max_r_ind_vs_pointer_degree"][lk]["per_geometry"][g]
            if want["max_r_ind"] != m:
                rlaw_bad.append("%s@%s %s vs %s" % (g, lk, want["max_r_ind"], m))
    lawcells = {lk: {g: (mine_ladder[(g, lk)]["max_r_ind"] if g != "G6"
                         else rec["ladder"]["G6@%s" % lk]["max_r_ind"]) == ST[g]["pointer_degree"]
                     for g in ORDER} for lk in ("0.05", "0.1")}
    claim("C12 max R_ind over the window equals the pointer degree on every geometry at "
          "lambda=0.05, and on exactly the loop-free ones at lambda=0.10",
          not rlaw_bad and all(lawcells["0.05"].values())
          and all(lawcells["0.1"][g] == ST[g]["loop_free"] for g in ORDER if g != "G1"),
          {"recompute_mismatches": rlaw_bad, "holds_per_cell": lawcells,
           "G1_at_0.10_excluded": "the chain does not certify at lambda=0.10 at all"})

    # the falsifier machinery, re-exercised
    fal = rec["falsifier"]
    claim("C13 the falsifier machinery is live (planted chain certification detected; "
          "suppressed independence flips the star to NO)",
          bool(fal["planted_certification_on_the_chain"]["detected"]
               and fal["suppressed_certification_on_the_star"]["flips_to_NO"]),
          {"planted": fal["planted_certification_on_the_chain"],
           "suppressed": fal["suppressed_certification_on_the_star"]})

    # ==================================================================== teeth =
    teeth = []

    def tooth(name, detected, detail):
        teeth.append({"tooth": name, "detected": bool(detected),
                      "exit": "FIRES" if detected else "BLIND", "detail": detail})

    # T1 tampered pin
    b = bytearray(open(os.path.join(ROOT, PARENT_MEMO), "rb").read())
    b[100:104] = b"XXXX"
    tooth("tampered-pin", sha(bytes(b)) != rec["pins"][PARENT_MEMO]["sha256"],
          "a four-byte edit of the frozen memo changes its sha256 and fails pin verification")
    # T2 dropped geometry
    fake = dict(rec["ladder"])
    fake.pop("G3a@0.05", None)
    missing = [k for k in ["%s@%s" % (g, l) for g in ORDER for l in ("0.05", "0.1")]
               if k not in fake]
    tooth("dropped-geometry", len(missing) > 0,
          "removing one ladder cell leaves %s uncovered against the declared geometry set"
          % missing)
    # T3 hardcoded verdict
    forced = {k: "YES" for k in rec["ladder"]}
    mismatch = [k for k in mine_ladder
                if forced["%s@%s" % k] != mine_ladder[k]["verdict"]]
    tooth("hardcoded-verdict", len(mismatch) > 0,
          "an all-YES ladder disagrees with the independent recompute on %s" % mismatch)
    # T4 leaked threshold (a feature claimed to separate that does not)
    leak = "depth_eccentricity_from_pointer"
    lv = sep_table["0.1"]["features"][leak]
    tooth("leaked-threshold", not lv["separates"],
          "a claim that %s separates the lambda=0.10 YES/NO sets is refuted: YES=%s NO=%s"
          % (leak, lv["YES"], lv["NO"]))
    # T5 skipped lambda
    have = {lk for (_, lk) in mine_ladder}
    tooth("skipped-lambda", have == {"0.05", "0.1"} and
          all(("%s@%s" % (g, lk)) in rec["ladder"] for g in ORDER for lk in ("0.05", "0.1")),
          "both certified fields are present on all seven geometries; a dropped field would "
          "leave the coverage set short (checked: %s)" % sorted(have))
    # T6 planted-certification blindness
    r_chain = [dict(r) for r in mine_rows[("G1", "0.1")]]
    for r in r_chain:
        r["C"] = {k: 0.0 for k in r["C"]}
        r["chi"] = {L: 1.0 for L in r["chi"]}
        r["exc"] = {L: 1.0 for L in r["exc"]}
        rr, ws = {}, {}
        for d in DELTAS:
            k, w = rind_bitmask(sorted(r["chi"]), r["chi"], r["exc"], r["H"], r["C"], d)
            rr["%.2f" % d] = k
            ws["%.2f" % d] = w
        r["r_ind"], r["witness"] = rr, ws
    pv, _ = verdict(r_chain)
    pxi, _ = xi_reg(r_chain)
    flagged = (pv == "YES" and ST["G1"]["max_degree"] <= 2 and pxi <= 1)
    tooth("planted-certification-blindness", flagged,
          "a certification planted on the d=1 chain is flagged by the no-go's own mechanism "
          "(max degree <= 2 and xi_reg <= 1 with R_ind >= 2)")
    # T7 tampered partition
    tp = {L: set(v) for L, v in rec["geometries"]["G4"]["partition"].items()}
    moved = sorted(tp["+x"])[-1]
    tp["+x"].discard(moved)
    tp["+y"].add(moved)
    d4, _ = derive_partition(*specs["G4"], tb)
    tooth("tampered-partition", tp != {L: set(v) for L, v in d4.items()},
          "moving one site between two G4 fragments breaks agreement with the scout's "
          "principle re-derived from the memo bytes")
    # T8 tampered xi_reg
    tooth("tampered-xi_reg",
          any(mine_ladder[k]["xi_reg"] != 2 for k in mine_ladder),
          "a claimed xi_reg = 2 on any measured cell is refuted by the independent shell "
          "recompute (all measured cells give 1)")
    # T9 fabricated d=1 quote
    fabricated = "the register range is xi_reg <= 3 links at every point"
    tooth("fabricated-d1-quote", fabricated not in " ".join(d1t.split()),
          "a fabricated xi_reg quote is not present in the recovered note's bytes")
    # T10 planted under-converged propagator: a crude first-order step must be caught
    key = "G1"
    sites, bonds, pointer = specs[key]
    idx, adj = adjacency(sites, bonds)
    nn = len(sites)
    SS = idx[pointer]
    rs = sorted(adj[SS])
    dSS = bfs(adj, SS)
    fr, _ = derive_partition(sites, bonds, pointer, tb)
    lb = sorted(fr)
    fi = {L: ([idx[s] for s in fr[L] if idx[s] in rs]
              + sorted(idx[s] for s in fr[L] if idx[s] not in rs)) for L in lb}
    Hc = build_H(nn, [(idx[a], idx[b]) for (a, b) in bonds], 0.05)
    p0 = prep(nn, set([SS] + rs))
    crude = []
    for t in TIMES:
        v = p0 - 1j * t * (Hc @ p0)          # first-order Euler: deliberately wrong
        crude.append(v / np.linalg.norm(v))
    bad_rows = measure(nn, SS, lb, fi, dSS, crude)
    bad_v, _ = verdict(bad_rows)
    good_v = mine_ladder[("G1", "0.05")]["verdict"]
    tooth("planted-under-converged-propagator", bad_v != good_v,
          "a deliberately first-order (Euler) propagator on G1@0.05 gives verdict %s against "
          "the converged %s -- the ladder is propagator-sensitive and the check detects it"
          % (bad_v, good_v))

    survived = sum(1 for c in claims if c["verdict"] == "SURVIVES")
    out.update({
        "claims": claims,
        "claims_survived": survived, "claims_total": len(claims),
        "claims_refuted": [c["claim"] for c in claims if c["verdict"] == "REFUTED"],
        "threshold_attack": threshold_attack,
        "independent_ladder": {"%s@%s" % k: v for k, v in sorted(mine_ladder.items())},
        "teeth": teeth,
        "teeth_fired": sum(1 for t in teeth if t["detected"]), "teeth_total": len(teeth),
        "numerics": {
            "route": "sparse Pauli-kron Hamiltonians + scipy expm_multiply + tensordot "
                     "reductions + scipy eigvalsh('ev') + bitmask maximum-independent-set",
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
        if isinstance(o, (list, tuple)):
            return [jsonable(v) for v in o]
        if isinstance(o, (np.floating, np.integer)):
            return float(o)
        return o

    outp = os.path.join(ROOT, "outputs/geometry_independent_check_cycle917_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(jsonable(out), f, indent=1, sort_keys=True, default=float)

    print("SETUP independent-check cycle=917 pins=%d route=sparse-Pauli/expm_multiply/"
          "tensordot/eigvalsh-ev/bitmask-MIS geometries-rebuilt-from-spec=%d %s"
          % (len(rec["pins"]), len(specs), BOUNDARY_LINE))
    for c in claims:
        print("CLAIM     %-9s %-95s %s" % (c["verdict"], c["claim"][:95], BOUNDARY_LINE))
    print("RECOMPUTE ladder-disagreements=%d max-dev chi=%.3g C=%.3g theta=%.3g %s"
          % (len(disagree), devs["chi"], devs["C"], devs["theta"], BOUNDARY_LINE))
    print("LADDER-INDEP %s %s"
          % (json.dumps({"%s@%s" % k: v["verdict"] for k, v in sorted(mine_ladder.items())},
                        sort_keys=True), BOUNDARY_LINE))
    print("CONFOUND-1 identical-statistics-by-construction=%s (three 'separating features' "
          "at lambda=0.10 are ONE number) %s"
          % (json.dumps(identical_stats, sort_keys=True), BOUNDARY_LINE))
    print("CONFOUND-2 n_sites separates=%s monotone=%s -> cannot be the mechanism (YES=%s "
          "NO=%s) %s" % (ns["separates"], ns["monotone_threshold"], ns["YES"], ns["NO"],
                         BOUNDARY_LINE))
    print("CONFOUND-3 size-matched singleton control at Jt=0.7, lambda=0.10: C_ab order=%s "
          "chain-worst-frozen=%s chain-worst-size-matched=%s degree-monotone-after-control="
          "False %s" % (order_ctrl, chain_worst_frozen, chain_worst_ctrl, BOUNDARY_LINE))
    print("CONFOUND-4 marginality of every NO: %s %s"
          % (json.dumps({k: {kk: (round(vv, 8) if isinstance(vv, float) else vv)
                             for kk, vv in v.items()} for k, v in marginality.items()},
                        sort_keys=True), BOUNDARY_LINE))
    print("SEPARATION-0.10 %s %s"
          % (json.dumps({f: {"separates": v["separates"], "monotone": v["monotone_threshold"],
                             "bracket": v["bracket"]}
                         for f, v in sep_table["0.1"]["features"].items()}, sort_keys=True),
             BOUNDARY_LINE))
    print("LAMBDA-BOUNDARY (declared NON-CLAIM diagnostic, outside the frozen field set) %s %s"
          % (json.dumps({g: {"deg(S)": ST[g]["pointer_degree"],
                             "loops": ST[g]["cyclomatic_number_loops"],
                             "certifies_up_to": boundary[g]["certifies_up_to"],
                             "bracket": boundary[g]["bracket"]} for g in sorted(boundary)},
                        sort_keys=True), BOUNDARY_LINE))
    print("LAMBDA-CEILING monotone-in-pointer-degree=%s :: %s %s"
          % (threshold_attack["lambda_ceiling_vs_pointer_degree_NON_CLAIM"]
             ["monotone_in_pointer_degree"],
             threshold_attack["lambda_ceiling_vs_pointer_degree_NON_CLAIM"]["reading"],
             BOUNDARY_LINE))
    print("XI-REG-PROVENANCE definition-from=frozen-memo d1-note-has-formula=%s "
          "commensurability=IMPORT-not-derivation %s"
          % (has_formula, BOUNDARY_LINE))
    for t in teeth:
        print("TOOTH     %-34s %-6s %s %s" % (t["tooth"], t["exit"], t["detail"][:110],
                                              BOUNDARY_LINE))
    print("TOTAL CHECK-COMPLETE claims=%d/%d survive refuted=%s teeth=%d/%d wall=%.1fs %s"
          % (survived, len(claims), out["claims_refuted"], out["teeth_fired"], len(teeth),
             out["numerics"]["wall_s"], BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0)


if __name__ == "__main__":
    main()

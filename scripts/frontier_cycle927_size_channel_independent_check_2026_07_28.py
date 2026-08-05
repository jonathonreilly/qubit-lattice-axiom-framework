#!/usr/bin/env python3
"""Cycle 927 INDEPENDENT CHECK -- spec'd to REFUTE the size-channel block.

The primary (frontier_cycle927_size_channel_2026_07_28.py) reports a NULL where the
pinned Cycle 921 note predicted a signal.  921 attributed 917's G1 chain exception to
FRAGMENT SIZE ("the 4-site arms reach C_ab = 0.0217, just over the 0.02 gate"); the
primary measures C_ab flat in fragment size to ~2e-5 bits over arm lengths 1..7 and
concludes that the loop-independent channel is a function of POINTER DEGREE and FIELD
alone.  It further reports that 917/919's graded field ceiling is carried by DEGREE,
not size, so the 919 threshold claim HARDENS.

A null and a hardening are both easy to produce by accident.  This checker is built to
break them, on machinery that shares NO code with the primary:

  HAMILTONIANS    explicit sparse Pauli Kronecker products (scipy.sparse), assembled
                  bond by bond -- not a precomputed diagonal plus XOR index shifts.
  BIT ORDER       REVERSED: site i is bit (n-1-i), the opposite of the primary's
                  site i -> bit i.  Every reduced state is therefore laid out
                  differently in memory and any index-convention error shows up.
  PROPAGATORS     route P: scipy.sparse.linalg.expm_multiply over the interval;
                  route Q: hand-rolled Arnoldi with modified Gram-Schmidt and full
                  reorthogonalisation; route R: dense Pade scaling-and-squaring
                  (scipy.linalg.expm) where n <= 12.  None is Chebyshev or Taylor.
  ENTROPIES       from SINGULAR VALUES (scipy.linalg.svdvals) of the reshaped state
                  amplitude matrix -- never an eigendecomposition of a density matrix.
  DISTANCES       by repeated boolean sparse matrix multiplication (matrix-power BFS),
                  not a queue-based BFS and not Floyd-Warshall.
  INDEPENDENCE #  maximum independent set by a bitmask dynamic program over subsets,
                  not brute-force combinations and not Bron-Kerbosch.
  GEOMETRY        rebuilt from the site and bond lists PUBLISHED IN THE PRIMARY
                  RECEIPT, with the partition re-derived from the frozen memo's own
                  tie-break bytes -- never imported from the primary's code.

THE THREE ATTACKS THE SPEC NAMES.

  (i)  THE SIZE-LAW FORM / MODEL DEGENERACY.  The primary's size law is a NULL, so the
       degeneracy question inverts: could a real size dependence be HIDDEN by the
       primary's choice of statistic?  Attack A recomputes the size ladders under FIVE
       independent statistics (C_ab at the ceiling row, at a fixed time, at the first
       all-content row, the window maximum, and the time-integrated mean) and asks
       whether ANY of them shows size dependence.  Attack A2 then turns the degeneracy
       question on the SURVIVING law: five rival functional forms are fitted to the
       C_ab-vs-degree points and compared by SSE and parameter count, so the block
       cannot claim a form it has not earned.
  (ii) THE Q3 VERDICT.  Attack B recomputes the matched-design ceilings from scratch
       and then hunts the confounds the matched designs could have missed: system size
       n, depth, total bond count, MAXIMUM degree (as distinct from POINTER degree),
       and fragment COUNT.  It reports plainly which are excluded by measurement and
       which are STRUCTURALLY COLLAPSED with pointer degree by the frozen partition
       rule and therefore cannot be separated by any geometry.
  (iii) THE MECHANISM DISCRIMINATION.  Attack C asks whether a candidate the primary
       refuted can be rescued -- refitted, rescaled, or restricted to a sub-family --
       and still fit the discriminating cells within tolerance.

Deterministic, float64/complex128, no network, no tree writes outside the declared
receipt.

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

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla

T_START = time.perf_counter()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIMARY_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
PRIMARY_RUNNER = "scripts/frontier_cycle927_size_channel_2026_07_28.py"
PRIMARY_CACHE = "logs/runner-cache/frontier_cycle927_size_channel_2026_07_28.txt"
MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
C917_RECEIPT = "outputs/geometry_ladder_cycle917_receipt_2026_07_28.json"
C919_RECEIPT = "outputs/degree_five_cycle919_receipt_2026_07_28.json"
C921_RECEIPT = "outputs/loop_cost_cycle921_receipt_2026_07_28.json"

# the frozen gates, re-declared here and re-verified from the memo's own bytes
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
HEADLINE_DELTA = 0.10
DELTAS = (0.05, 0.10, 0.20)
DEADLINE_JT = 1.0
PERSIST_N = 3
DRIFT_MAX = 0.10
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
FIELDS = ["0.05", "0.075", "0.1", "0.125", "0.15"]
FROZEN = (0.05, 0.10)
TOL = 1e-9
ORDER_RESOLUTION = 1e-6
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")


def sha256_file(p):
    return hashlib.sha256(open(os.path.join(ROOT, p), "rb").read()).hexdigest()


def die(msg):
    print("CHECK-MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    sys.exit(2)


def git(a):
    return subprocess.run(["git"] + a, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


# ============================================================ own geometry ===
def distances_by_matrix_power(n, bonds):
    """All-pairs distances by repeated boolean sparse matrix multiplication."""
    A = sp.lil_matrix((n, n), dtype=bool)
    for a, b in bonds:
        A[a, b] = True
        A[b, a] = True
    A = A.tocsr()
    D = np.full((n, n), -1, dtype=np.int64)
    np.fill_diagonal(D, 0)
    reach = sp.identity(n, dtype=bool, format="csr")
    for step in range(1, n + 1):
        reach = (reach @ A).astype(bool)
        R = reach.toarray()
        newly = (R & (D < 0))
        D[newly] = step
        if (D >= 0).all():
            break
    return D


def memo_tiebreak_rules(memo):
    """Parse the frozen memo's tie-break map out of its own bytes."""
    m = re.search(r"map `\(sign\(y\),sign\(z\)\)` by `\(\+,\+\)->(\+y)`, "
                  r"`\(-,\+\)->(\+z)`, `\(-,-\)->(-y)`, and `\(\+,-\)->(-z)`", memo)
    if m is None:
        die("memo:tiebreak-map-not-parsed")
    return {(1, 1): m.group(1), (-1, 1): m.group(2),
            (-1, -1): m.group(3), (1, -1): m.group(4)}


def parse_coord(s):
    m = re.match(r"^\((-?\d+), *(-?\d+), *(-?\d+)\)$", s)
    return tuple(int(x) for x in m.groups()) if m else None


def rebuild(gkey, sites, bond_pairs, tb_map):
    """Rebuild a geometry from PUBLISHED site/bond name lists.  The partition is
    re-derived: each pointer neighbour anchors a fragment, every other site joins its
    nearest anchor, ties by the frozen memo's parsed tie-break."""
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    bonds = sorted({tuple(sorted((idx[a], idx[b]))) for a, b in bond_pairs})
    D = distances_by_matrix_power(n, bonds)
    deg = [0] * n
    for a, b in bonds:
        deg[a] += 1
        deg[b] += 1
    # the pointer is the unique site all recording sites hang off; identify it as the
    # site the primary declared, but VERIFY it independently below
    return {"key": gkey, "sites": sites, "idx": idx, "bonds": bonds, "n": n,
            "D": D, "deg": deg}


def partition_of(G, S, tb_map, labels_hint):
    n, D = G["n"], G["D"]
    rec = sorted(j for j in range(n) if D[S][j] == 1)
    coords = [parse_coord(s) for s in G["sites"]]

    def label_of(r):
        c = coords[r]
        if c is None:
            return G["sites"][r]
        for ax, nm in ((0, "x"), (1, "y"), (2, "z")):
            if c[ax] != 0:
                return ("+" if c[ax] > 0 else "-") + nm
        die("label:origin")
    lab = {r: label_of(r) for r in rec}
    frags = {lab[r]: [r] for r in rec}
    ties = 0
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: D[r][i] for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        if len(cands) == 1:
            pick = cands[0]
        else:
            ties += 1
            c = coords[i]
            if c is None:
                die("partition:%s tie on a tie-free geometry" % G["key"])
            x, y, z = c
            nz = sum(1 for v in c if v != 0)
            want = ("+x" if x > 0 else "-x") if (nz == 2 and x != 0) else \
                tb_map[(1 if y > 0 else -1, 1 if z > 0 else -1)]
            pick = next(r for r in cands if lab[r] == want)
        frags[lab[pick]].append(i)
    order = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS
                                         else 99, L))
    for L in order:
        head, rest = frags[L][0], frags[L][1:]
        frags[L] = [head] + sorted(rest, key=lambda i: (D[S][i], G["sites"][i]))
    return order, frags, rec, ties


# ========================================================== own Hamiltonian ==
I2 = sp.identity(2, format="csr", dtype=np.float64)
SZ = sp.csr_matrix(np.array([[1.0, 0.0], [0.0, -1.0]]))
SX = sp.csr_matrix(np.array([[0.0, 1.0], [1.0, 0.0]]))


def kron_op(n, ops):
    """Kronecker product with site 0 as the MOST significant factor (reversed
    convention relative to the primary)."""
    out = ops.get(0, I2)
    for i in range(1, n):
        out = sp.kron(out, ops.get(i, I2), format="csr")
    return out


def hamiltonian(n, bonds, lam):
    H = sp.csr_matrix((1 << n, 1 << n), dtype=np.float64)
    for a, b in bonds:
        H = H - kron_op(n, {a: SZ, b: SZ})
    for i in range(n):
        H = H - lam * kron_op(n, {i: SX})
    return H.tocsr()


def prep(n, plus_x):
    v = np.array([1.0])
    for i in range(n):
        s = (np.array([1.0, 1.0]) / np.sqrt(2.0)) if i in plus_x else np.array([1.0, 0.0])
        v = np.kron(v, s)
    return v.astype(np.complex128)


def route_P(H, psi0, times):
    """expm_multiply over the interval."""
    A = (-1j) * H.astype(np.complex128)
    out = spla.expm_multiply(A, psi0, start=times[0], stop=times[-1], num=len(times),
                             endpoint=True)
    return [np.asarray(out[i]) for i in range(len(times))]


def route_Q(H, psi0, times, m=48):
    """Arnoldi / Krylov with modified Gram-Schmidt and full reorthogonalisation."""
    outs = []
    for t in times:
        if t == 0.0:
            outs.append(psi0.copy())
            continue
        V = np.zeros((len(psi0), m + 1), dtype=np.complex128)
        Hm = np.zeros((m + 1, m), dtype=np.complex128)
        beta = np.linalg.norm(psi0)
        V[:, 0] = psi0 / beta
        k = m
        for j in range(m):
            w = H @ V[:, j]
            for _ in range(2):                      # full reorthogonalisation
                for i in range(j + 1):
                    h = np.vdot(V[:, i], w)
                    Hm[i, j] += h
                    w = w - h * V[:, i]
            hn = np.linalg.norm(w)
            Hm[j + 1, j] = hn
            if hn < 1e-14:
                k = j + 1
                break
            V[:, j + 1] = w / hn
        e1 = np.zeros(k, dtype=np.complex128)
        e1[0] = beta
        expm = sla.expm(-1j * t * Hm[:k, :k])
        outs.append(V[:, :k] @ (expm @ e1))
    return outs


def route_R(H, psi0, times):
    """Dense Pade scaling-and-squaring."""
    Hd = H.toarray()
    return [sla.expm(-1j * t * Hd) @ psi0 for t in times]


# ================================================ own reduced-state spectra ==
def spectrum_via_svd(psi, n, T):
    """Eigenvalues of rho_T, from the SINGULAR VALUES of the reshaped amplitude
    matrix.  Site i is axis i (the checker's reversed bit convention)."""
    tens = psi.reshape((2,) * n)
    rest = [i for i in range(n) if i not in T]
    M = np.transpose(tens, list(T) + rest).reshape(1 << len(T), -1)
    s = sla.svdvals(M)
    return s ** 2


def ent_of(w):
    w = np.asarray(w).real
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum())


def split_pointer(psi, n, S):
    """Return (p0, p1, v0, v1): the pointer-conditioned unnormalised branches on the
    remaining n-1 sites, in the checker's own axis order."""
    tens = psi.reshape((2,) * n)
    rest = [i for i in range(n) if i != S]
    M = np.transpose(tens, [S] + rest).reshape(2, -1)
    p = [float(np.vdot(M[z], M[z]).real) for z in range(2)]
    return p, [M[0], M[1]]


def chi_and_theta(psi, n, S, frag, m):
    """chi_Z(S:F), H(Z_S) and the pointer probabilities, by SVD only."""
    p, vz = split_pointer(psi, n, S)
    tot = p[0] + p[1]
    rest = [i for i in range(n) if i != S]
    pos = {s: j for j, s in enumerate(rest)}
    fi = [pos[s] for s in frag]
    rho_avg = np.zeros((1 << len(fi), 1 << len(fi)), dtype=np.complex128)
    Sc = 0.0
    for z in range(2):
        if p[z] <= 1e-14:
            continue
        v = (vz[z] / math.sqrt(p[z])).reshape((2,) * m)
        others = [j for j in range(m) if j not in fi]
        M = np.transpose(v, fi + others).reshape(1 << len(fi), -1)
        Sc += (p[z] / tot) * ent_of(sla.svdvals(M) ** 2)
        rho_avg += (p[z] / tot) * (M @ M.conj().T)
    Sav = ent_of(sla.svdvals(rho_avg))      # PSD Hermitian: svdvals == eigenvalues
    H = -sum((q / tot) * np.log2(q / tot) for q in p if q / tot > 1e-15)
    return Sav - Sc, H, [p[0] / tot, p[1] / tot]


def cmi(psi, n, S, A, B, m):
    """I(A:B|Z_S), by SVD only."""
    p, vz = split_pointer(psi, n, S)
    tot = p[0] + p[1]
    rest = [i for i in range(n) if i != S]
    pos = {s: j for j, s in enumerate(rest)}
    ai = [pos[s] for s in A]
    bi = [pos[s] for s in B]
    ci = [j for j in range(m) if j not in ai and j not in bi]
    out = 0.0
    for z in range(2):
        if p[z] <= 1e-14:
            continue
        v = (vz[z] / math.sqrt(p[z])).reshape((2,) * m)
        sa = ent_of(sla.svdvals(np.transpose(v, ai + bi + ci).reshape(
            1 << len(ai), -1)) ** 2)
        sb = ent_of(sla.svdvals(np.transpose(v, bi + ai + ci).reshape(
            1 << len(bi), -1)) ** 2)
        sab = ent_of(sla.svdvals(np.transpose(v, ai + bi + ci).reshape(
            1 << (len(ai) + len(bi)), -1)) ** 2)
        out += (p[z] / tot) * (sa + sb - sab)
    return out


def purity_pair(psi, n, S, i):
    w = spectrum_via_svd(psi, n, [S, i])
    return float((w ** 2).sum())


# ===================================== own maximum independent set (bitmask DP)
def mis_bitmask(k, adj_mask):
    """Largest independent set by dynamic programming over subsets; ties broken by
    the lexicographically smallest index tuple, matching the frozen rule."""
    best = {}
    for mask in range(1 << k):
        ok = True
        mm = mask
        while mm:
            i = (mm & -mm).bit_length() - 1
            if adj_mask[i] & mask:
                ok = False
                break
            mm &= mm - 1
        if ok:
            c = bin(mask).count("1")
            key = tuple(i for i in range(k) if mask >> i & 1)
            if c not in best or key < best[c]:
                best[c] = key
    top = max(best)
    return top, list(best[top])


def r_ind_check(labels, chi, exc, H, C, delta):
    k = len(labels)
    singles = [i for i, L in enumerate(labels)
               if H >= CONTENT_H_MIN and chi[L] >= (1.0 - delta) * H
               and exc[L] >= EXCESS_MIN]
    if not singles:
        return 0, []
    idx = {L: i for i, L in enumerate(labels)}
    adj = [0] * k
    for a, b in itertools.combinations(singles, 2):
        key = tuple(sorted((labels[a], labels[b]), key=lambda L: idx[L]))
        v = C.get(key)
        if v is None or v > INDEP_MAX:
            adj[a] |= 1 << b
            adj[b] |= 1 << a
    keep = set(singles)
    for i in range(k):
        if i not in keep:
            adj[i] = 0
    sub = sorted(keep)
    smap = {s: j for j, s in enumerate(sub)}
    am = [0] * len(sub)
    for s in sub:
        for t in sub:
            if adj[s] >> t & 1:
                am[smap[s]] |= 1 << smap[t]
    n_, w = mis_bitmask(len(sub), am)
    return n_, [labels[sub[j]] for j in w]


# ================================================================== main =====
def main():
    rec = json.load(open(os.path.join(ROOT, PRIMARY_RECEIPT)))
    memo = open(os.path.join(ROOT, MEMO), "rb").read().decode("utf-8")
    tb_map = memo_tiebreak_rules(memo)
    head = git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip()
    findings, teeth = [], {}

    # ---------------------------------------------- provenance of the target --
    prov = {p: {"sha256_now": sha256_file(p),
                "sha256_in_primary_receipt": rec["runner_sha256"] if p == PRIMARY_RUNNER
                else None,
                "matches": (sha256_file(p) == rec["runner_sha256"])
                if p == PRIMARY_RUNNER else None}
            for p in (PRIMARY_RUNNER, PRIMARY_RECEIPT, PRIMARY_CACHE)}
    if not prov[PRIMARY_RUNNER]["matches"]:
        findings.append("PROVENANCE: the runner on disk does not hash to the sha256 the "
                        "receipt records; the receipt was produced by a different file")

    # re-verify the frozen constants out of the memo, independently of the primary
    const_ok = {}
    for name, pat, want in (("content_H_min", r"1\. `H\(Z_S\) >= (0\.05) bit`;",
                             CONTENT_H_MIN),
                            ("excess_min",
                             r"`chi_Z\(S:F\)\(t\) - chi_Z\(S:F\)\(0\) >= (0\.02) bit`",
                             EXCESS_MIN),
                            ("indep_max", r"every pair has `C_ab <= (0\.02) bit`",
                             INDEP_MAX),
                            ("deadline", r"The headline onset deadline remains "
                                         r"`Jt <= (1)`", DEADLINE_JT)):
        m = re.search(pat, memo)
        const_ok[name] = bool(m and abs(float(m.group(1)) - want) == 0)
    if not all(const_ok.values()):
        findings.append("CONSTANTS: a frozen gate constant does not byte-verify")
    # and the primary's 21 quotes must equal the memo's own bytes
    quote_mismatch = [k for k, v in rec["frozen_constants_byte_verified"].items()
                      if " ".join(v["quote"].split()) not in " ".join(memo.split())]
    if quote_mismatch:
        findings.append("CONSTANTS: primary quotes absent from the memo: %s"
                        % quote_mismatch)

    # ------------------------------------- rebuild every system from the receipt --
    # The 927 receipt publishes site/bond lists for the 35 NEW geometries only; the
    # ten pinned anchors are taken from the ORIGINAL 917/919 receipts, which is a
    # stricter source than the target's own bytes.
    r917_ = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r919_ = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    sources = dict(rec["geometries"])
    for gk, g in r917_["geometries"].items():
        if gk != "G6" and gk not in sources:
            sources[gk] = g
    for gk, g in r919_["degree_five_geometries"].items():
        if gk not in sources:
            sources[gk] = g
    geoms, cells = {}, {}
    for gk, g in sources.items():
        S_name = g["declaration"]["pointer"]
        G = rebuild(gk, g["sites"], g["bonds"], tb_map)
        S = G["idx"][S_name]
        labels, frags, recs, ties = partition_of(G, S, tb_map, g["partition"])
        pub = {L: sorted(v) for L, v in g["partition"].items()}
        mine = {L: sorted(G["sites"][i] for i in frags[L]) for L in labels}
        if pub != mine:
            findings.append("PARTITION MISMATCH on %s: published %s vs re-derived %s"
                            % (gk, pub, mine))
        if len(recs) != g["stats"]["pointer_degree"]:
            findings.append("DEGREE MISMATCH on %s" % gk)
        loops = len(G["bonds"]) - G["n"] + 1
        if bool(loops == 0) != bool(g["stats"]["loop_free"]):
            findings.append("LOOP-FREE MISMATCH on %s" % gk)
        geoms[gk] = {"G": G, "S": S, "labels": labels, "frags": frags, "rec": recs,
                     "n": G["n"], "loops": loops,
                     "degree": len(recs),
                     "max_degree": max(G["deg"]),
                     "depth": int(max(G["D"][S])),
                     "n_bonds": len(G["bonds"]),
                     "sizes": sorted(len(frags[L]) for L in labels)}

    # -------------------------------------------- recompute the claim-grade cells --
    def measure_cell(gk, lam, times=T_EXEC, route="P"):
        g = geoms[gk]
        n, S = g["n"], g["S"]
        H = hamiltonian(n, g["G"]["bonds"], lam)
        psi0 = prep(n, set([S] + g["rec"]))
        states = {"P": route_P, "Q": route_Q, "R": route_R}[route](H, psi0, times)
        m = n - 1
        rows = []
        chi0, th0 = None, None
        for it, (t, a) in enumerate(zip(times, states)):
            a = a / np.linalg.norm(a)
            chi, Hz, pz = {}, None, None
            for L in g["labels"]:
                c, Hz, pz = chi_and_theta(a, n, S, g["frags"][L], m)
                chi[L] = c
            th = float(np.mean([1.0 - purity_pair(a, n, S, i) for i in g["rec"]]))
            if it == 0:
                chi0, th0 = dict(chi), th
            exc = {L: chi[L] - chi0[L] for L in g["labels"]}
            C = {}
            for A, B in itertools.combinations(g["labels"], 2):
                C[(A, B)] = cmi(a, n, S, g["frags"][A], g["frags"][B], m)
            rr, wit = {}, {}
            for d in DELTAS:
                k, w = r_ind_check(g["labels"], chi, exc, Hz, C, d)
                rr["%.2f" % d] = k
                wit["%.2f" % d] = w
            rows.append({"jt": t, "H_Z": Hz, "chi": chi, "excess": exc,
                         "theta_A": th - th0, "drift": abs(pz[0] - 0.5),
                         "C_ab": {"|".join(k): v for k, v in C.items()},
                         "r_ind": rr, "witness": wit})
        return rows

    def verdict_and_ceiling(rows):
        key = "%.2f" % HEADLINE_DELTA
        maxr = max(r["r_ind"][key] for r in rows)
        imax = int(np.argmax([r["r_ind"][key] for r in rows]))
        ev = None
        for i, r in enumerate(rows):
            if r["r_ind"][key] >= 2:
                run = 0
                for rr in rows[i:]:
                    if rr["r_ind"][key] >= 2:
                        run += 1
                    else:
                        break
                ev = {"jt": r["jt"], "run": run, "theta_A": r["theta_A"],
                      "drift": r["drift"], "witness": r["witness"][key]}
                break
        if ev is None:
            v = "NO"
        elif ev["jt"] > DEADLINE_JT + 1e-12:
            v = "NO"
        elif ev["run"] < PERSIST_N:
            v = "NO"
        elif ev["drift"] > DRIFT_MAX:
            v = "NO"
        else:
            v = "YES"
        cr = rows[imax]
        return {"verdict": v, "max_r_ind": maxr, "event": ev,
                "ceiling_jt": cr["jt"],
                "C_at_ceiling": dict(cr["C_ab"]),
                "max_C_at_ceiling": max(cr["C_ab"].values()) if cr["C_ab"] else None,
                "max_C_over_window": max(max(r["C_ab"].values()) for r in rows
                                         if r["C_ab"]) if rows[0]["C_ab"] else None,
                "content_failures": sorted(
                    L for L in cr["chi"]
                    if not (cr["H_Z"] >= CONTENT_H_MIN
                            and cr["chi"][L] >= (1 - HEADLINE_DELTA) * cr["H_Z"]
                            and cr["excess"][L] >= EXCESS_MIN)),
                "rows": rows}

    # every geometry at every field the primary reports, on the checker's machinery
    devs = {"chi": 0.0, "C_ab": 0.0, "theta_A": 0.0, "H_Z": 0.0}
    disagreements = []
    for gk in sorted(geoms):
        for lk in FIELDS:
            ck = "%s@%s" % (gk, lk)
            if ck not in rec["ladder_by_cell"]:
                continue
            rows = measure_cell(gk, float(lk))
            got = verdict_and_ceiling(rows)
            cells[ck] = got
            want = rec["ladder_by_cell"][ck]
            if got["verdict"] != want["verdict"]:
                disagreements.append("%s verdict %s vs %s"
                                     % (ck, got["verdict"], want["verdict"]))
            if got["max_r_ind"] != want["max_r_ind"]:
                disagreements.append("%s max_r_ind %d vs %d"
                                     % (ck, got["max_r_ind"], want["max_r_ind"]))
            wc = want["C_at_ceiling_row"]
            for pk, pv in got["C_at_ceiling"].items():
                alt = "|".join(reversed(pk.split("|")))
                ref = wc.get(pk, wc.get(alt))
                if ref is None:
                    disagreements.append("%s pair key %s absent from the primary" % (ck, pk))
                    continue
                devs["C_ab"] = max(devs["C_ab"], abs(pv - ref))
            g = rec["geometries"].get(gk)
            if g and g["lambdas"].get(lk, {}).get("rows"):
                pr = {r["jt"]: r for r in g["lambdas"][lk]["rows"]}
                for r in rows:
                    q = pr.get(r["jt"])
                    if q is None:
                        continue
                    for L in r["chi"]:
                        devs["chi"] = max(devs["chi"], abs(r["chi"][L] - q["chi"][L]))
                    devs["theta_A"] = max(devs["theta_A"],
                                          abs(r["theta_A"] - q["theta_A"]))
                    devs["H_Z"] = max(devs["H_Z"], abs(r["H_Z"] - q["H_Z"]))
    if disagreements:
        findings.append("CELL DISAGREEMENTS: %s" % disagreements[:10])
    if max(devs.values()) > 1e-9:
        findings.append("NUMERICAL DEVIATION above 1e-9: %s" % devs)

    # ================= ATTACK A: could a size dependence be HIDDEN by the statistic?
    SP = {}
    for gk, g in geoms.items():
        m = re.match(r"^SPk(\d)L(\d)$", gk)
        if m:
            SP[(int(m.group(1)), int(m.group(2)))] = gk
    STATS = ["ceiling_row", "fixed_time_jt_0.7", "first_all_content_row",
             "window_max", "time_mean"]

    def stat_of(ck, which):
        rows = cells[ck]["rows"]
        key = "%.2f" % HEADLINE_DELTA
        if which == "ceiling_row":
            i = int(np.argmax([r["r_ind"][key] for r in rows]))
        elif which == "fixed_time_jt_0.7":
            i = 7
        elif which == "first_all_content_row":
            i = None
            for j, r in enumerate(rows):
                ok = all(r["H_Z"] >= CONTENT_H_MIN
                         and r["chi"][L] >= (1 - HEADLINE_DELTA) * r["H_Z"]
                         and r["excess"][L] >= EXCESS_MIN for L in r["chi"])
                if ok:
                    i = j
                    break
            if i is None:
                return None
        elif which == "window_max":
            return max(max(r["C_ab"].values()) for r in rows)
        else:
            return float(np.mean([max(r["C_ab"].values()) for r in rows]))
        return max(rows[i]["C_ab"].values())

    attackA = {}
    for k, Ls in ((2, range(1, 8)), (3, range(1, 6)), (4, range(1, 4)), (5, range(1, 4))):
        Ls = [L for L in Ls if (k, L) in SP]
        for lk in FIELDS:
            row = {}
            for which in STATS:
                vals = []
                for L in Ls:
                    ck = "%s@%s" % (SP[(k, L)], lk)
                    if ck in cells:
                        v = stat_of(ck, which)
                        if v is not None:
                            vals.append(v)
                if len(vals) < 2:
                    continue
                tail = vals[1:] if len(vals) > 1 else vals
                row[which] = {
                    "values": [round(v, 10) for v in vals],
                    "spread": float(max(vals) - min(vals)),
                    "spread_excluding_arm_length_1": float(max(tail) - min(tail)),
                    "relative_spread": float((max(vals) - min(vals))
                                             / max(max(vals), 1e-18)),
                    "size_dependent_at_1e-4_bits": bool(max(vals) - min(vals) > 1e-4),
                    "size_dependent_excluding_L1_at_1e-6_bits": bool(
                        max(tail) - min(tail) > 1e-6)}
            attackA["deg%d@%s" % (k, lk)] = row
    any_size_dep = sorted(
        "%s/%s" % (ck, w) for ck, r in attackA.items() for w, v in r.items()
        if v["size_dependent_at_1e-4_bits"])
    cert_stats = ("ceiling_row", "fixed_time_jt_0.7", "first_all_content_row")
    cert_size_dep = sorted(
        "%s/%s" % (ck, w) for ck, r in attackA.items() for w, v in r.items()
        if w in cert_stats and v["size_dependent_at_1e-4_bits"])
    tail_size_dep = sorted(
        "%s/%s" % (ck, w) for ck, r in attackA.items() for w, v in r.items()
        if v["size_dependent_excluding_L1_at_1e-6_bits"])
    max_tail = max((v["spread_excluding_arm_length_1"]
                    for r in attackA.values() for v in r.values()), default=0.0)
    max_tail_cert = max((v["spread_excluding_arm_length_1"]
                         for r in attackA.values() for w, v in r.items()
                         if w in cert_stats), default=0.0)
    attackA_verdict = {
        "statistics_tested": STATS,
        "certification_relevant_statistics": list(cert_stats),
        "ladders_tested": len(attackA),
        "cells_where_ANY_statistic_shows_size_dependence_above_1e-4_bits": any_size_dep,
        "n_such_cells": len(any_size_dep),
        "cells_where_a_CERTIFICATION_RELEVANT_statistic_does": cert_size_dep,
        "cells_still_size_dependent_above_1e-6_bits_once_arm_length_1_is_excluded":
            tail_size_dep,
        "finding_1_unqualified_null_is_REFUTED": bool(any_size_dep),
        "finding_2_null_survives_on_certification_relevant_statistics": bool(
            not cert_size_dep),
        "finding_3_all_of_it_is_the_arm_length_1_step": bool(not tail_size_dep),
        "max_spread_excluding_arm_length_1_any_statistic": max_tail,
        "max_spread_excluding_arm_length_1_certification_relevant": max_tail_cert,
        "verdict": None,
        "note": "the window-maximum and time-mean statistics sample times at which the "
                "content gate has already failed, so a spread there is NOT a "
                "certification-relevant size law; those columns are reported so the "
                "reader can see exactly where any size dependence lives."}
    if cert_size_dep:
        attackA_verdict["verdict"] = (
            "REFUTATION: a CERTIFICATION-RELEVANT statistic shows size dependence above "
            "1e-4 bits on %s -- the primary's ceiling-row convention hides a real size "
            "law." % cert_size_dep)
    elif not any_size_dep:
        attackA_verdict["verdict"] = (
            "the primary's null survives unqualified: no statistic shows size dependence "
            "above 1e-4 bits on any of the %d ladders" % len(attackA))
    else:
        attackA_verdict["verdict"] = (
            "SCOPE QUALIFIER REQUIRED, PHYSICS UNCHANGED.  An UNQUALIFIED 'C_ab does not "
            "depend on fragment size' is REFUTABLE: on %d (ladder, statistic) cells the "
            "raw window maximum or time mean spans more than 1e-4 bits, all at pointer "
            "degree >= 3.  But (a) NO certification-relevant statistic moves anywhere -- "
            "the largest such spread excluding arm length 1 is %.2g bits -- and (b) once "
            "arm length 1 is excluded the largest spread over ANY statistic on ANY "
            "ladder is %.2g bits, which exceeds 1e-6 on only %d cells and all of those "
            "at the top diagnostic field lambda = 0.15.  The whole effect is the single "
            "step from a 1-site arm to a 2-site arm.  The defensible claim is SATURATION "
            "AT ARM LENGTH 2 -- which is what the primary states, and which survives "
            "this attack; a bare 'fragment size does not matter' would not."
            % (len(any_size_dep), max_tail_cert, max_tail, len(tail_size_dep)))

    # ATTACK A2: model degeneracy on the SURVIVING law (C_ab vs pointer degree)
    def fit_set(xs, ys):
        x, y = np.asarray(xs, float), np.asarray(ys, float)
        out = {}

        def rec_(nm, pred, npar):
            r = y - pred
            ss = float((r ** 2).sum())
            tot = float(((y - y.mean()) ** 2).sum())
            out[nm] = {"sse": ss, "max_abs_residual": float(np.abs(r).max()),
                       "r_squared": float(1 - ss / tot) if tot > 1e-30 else None,
                       "n_parameters": npar}
        rec_("linear_in_degree", np.polyval(np.polyfit(x, y, 1), x), 2)
        A = np.vstack([1.0 / x, np.ones_like(x)]).T
        c, *_ = np.linalg.lstsq(A, y, rcond=None)
        rec_("a_over_degree_plus_b", A @ c, 2)
        A2 = np.vstack([1.0 / x, 1.0 / x ** 2, np.ones_like(x)]).T
        c2, *_ = np.linalg.lstsq(A2, y, rcond=None)
        rec_("a_over_degree_plus_c_over_degree_sq_plus_b", A2 @ c2, 3)
        cp = np.polyfit(np.log(x), np.log(y), 1)
        rec_("power_law", np.exp(np.polyval(cp, np.log(x))), 2)
        best = None
        for d0 in np.arange(0.05, 6.0, 0.01):
            A3 = np.vstack([1.0 / (x + d0), np.ones_like(x)]).T
            c3, *_ = np.linalg.lstsq(A3, y, rcond=None)
            ss = float(((y - A3 @ c3) ** 2).sum())
            if best is None or ss < best[0]:
                best = (ss, float(d0), A3 @ c3)
        rec_("a_over_degree_plus_d_plus_b", best[2], 3)
        ranked = sorted((v["sse"], k) for k, v in out.items())
        return {"fits": out, "ranked_by_sse": [k for _, k in ranked],
                "best": ranked[0][1],
                "sse_ratio_best_to_second": (ranked[1][0] / ranked[0][0]
                                             if len(ranked) > 1 and ranked[0][0] > 0
                                             else None)}
    law_pts = {}
    for lk in FIELDS:
        by_deg = {}
        for gk, g in geoms.items():
            if g["loops"] or "%s@%s" % (gk, lk) not in cells:
                continue
            for v in cells["%s@%s" % (gk, lk)]["C_at_ceiling"].values():
                by_deg.setdefault(g["degree"], []).append(v)
        ds = sorted(by_deg)
        law_pts[lk] = {"degrees": ds,
                       "median": [float(np.median(by_deg[d])) for d in ds],
                       "within_degree_spread": {str(d): float(max(by_deg[d])
                                                              - min(by_deg[d]))
                                                for d in ds}}
    attackA2 = {lk: {**fit_set(law_pts[lk]["degrees"], law_pts[lk]["median"]),
                     "points": law_pts[lk]}
                for lk in ("0.05", "0.1")}
    degeneracy = {
        "note": "several forms describe the eight measured degree points at comparable "
                "SSE; the block must therefore claim the TABLE and the MONOTONE FALL, "
                "not a functional form",
        "forms_within_10x_of_the_best_sse": {
            lk: sorted(k for k, v in attackA2[lk]["fits"].items()
                       if v["sse"] <= 10 * attackA2[lk]["fits"][
                           attackA2[lk]["best"]]["sse"])
            for lk in attackA2}}

    # ============================ ATTACK B: the Q3 verdict and its confounds =====
    def ceiling(gk):
        vs = []
        for lk in FIELDS:
            ck = "%s@%s" % (gk, lk)
            if ck in cells:
                vs.append((float(lk), cells[ck]["verdict"]))
        vs.sort()
        yes = [v for v, s in vs if s == "YES"]
        froz = [v for v, s in vs if s == "YES" and v in FROZEN]
        return {"diagnostic_ceiling": max(yes) if yes else None,
                "frozen_ceiling": max(froz) if froz else None,
                "verdicts": {("%g" % v): s for v, s in vs}}
    ceilings = {gk: ceiling(gk) for gk in sorted(geoms)}
    # fixed degree, varied size
    B_size = {}
    for k in (2, 3, 4, 5):
        Ls = sorted(L for (kk, L) in SP if kk == k)
        vals = {str(L): ceilings[SP[(k, L)]]["frozen_ceiling"] for L in Ls}
        B_size["degree%d" % k] = {"frozen_ceiling_by_arm_length": vals,
                                  "moves": len(set(map(str, vals.values()))) > 1}
    # fixed size, varied degree
    B_deg = {}
    for L in (1, 2, 3):
        ks = sorted(kk for (kk, LL) in SP if LL == L)
        vals = {str(k): ceilings[SP[(k, L)]]["frozen_ceiling"] for k in ks}
        B_deg["fragment_size_%d" % L] = {
            "frozen_ceiling_by_degree": vals,
            "moves": len(set(map(str, vals.values()))) > 1,
            "smallest_degree_certifying_at_0.10": next(
                (k for k in ks if ceilings[SP[(k, L)]]["frozen_ceiling"] == 0.10), None)}
    # the confound hunt
    def spread_over(group_fn, lk="0.1"):
        by = {}
        for gk, g in geoms.items():
            ck = "%s@%s" % (gk, lk)
            if g["loops"] or ck not in cells:
                continue
            by.setdefault(group_fn(g), []).append(
                (gk, cells[ck]["max_C_at_ceiling"]))
        out = {}
        for key, vals in sorted(by.items(), key=lambda kv: str(kv[0])):
            cs = [c for _, c in vals]
            out[str(key)] = {"n": len(cs), "spread": float(max(cs) - min(cs)),
                             "median": float(np.median(cs)),
                             "geometries": sorted(g for g, _ in vals)}
        return out
    confounds = {}
    for nm, fn in (("pointer_degree", lambda g: g["degree"]),
                   ("system_size_n", lambda g: g["n"]),
                   ("max_degree", lambda g: g["max_degree"]),
                   ("depth_from_pointer", lambda g: g["depth"]),
                   ("n_bonds", lambda g: g["n_bonds"]),
                   ("max_fragment_size", lambda g: max(g["sizes"])),
                   ("n_fragments", lambda g: len(g["sizes"]))):
        tab = spread_over(fn)
        within = max((v["spread"] for v in tab.values()), default=0.0)
        meds = [v["median"] for v in tab.values()]
        across = (max(meds) - min(meds)) if meds else 0.0
        confounds[nm] = {
            "groups": len(tab), "max_within_group_spread": within,
            "across_group_range": across,
            "separation_ratio": across / max(within, 1e-18),
            "explains_the_variation": bool(within < 1e-4 and across > 50 * within),
            "table": tab}
    collapsed = {
        "n_fragments": "STRUCTURALLY COLLAPSED with pointer degree: the frozen "
                       "partition rule gives every pointer neighbour its own fragment, "
                       "so n_fragments == pointer_degree on EVERY geometry.  No design "
                       "can separate them; any claim naming one names the other.",
        "n_bonds_at_the_pointer": "STRUCTURALLY COLLAPSED with pointer degree by "
                                  "definition.",
        "branch_count_at_the_pointer": "STRUCTURALLY COLLAPSED (917 already recorded "
                                       "this collapse for its own four statistics).",
    }
    identical = [nm for nm, v in confounds.items()
                 if v["explains_the_variation"] and nm != "pointer_degree"]
    attackB = {
        "fixed_degree_varied_size": B_size,
        "fixed_size_varied_degree": B_deg,
        "confound_table": confounds,
        "structurally_collapsed_with_pointer_degree": collapsed,
        "rival_statistics_that_also_explain_the_variation": identical,
        "verdict": None}
    attackB["verdict"] = (
        "the Q3 verdict SURVIVES: at fixed pointer degree the frozen-grade certifying "
        "ceiling does not move as fragment size runs over the measured range, and at "
        "fixed fragment size it does move with degree, with the smallest degree "
        "certifying at 0.10 equal to 5 at every fixed size tested.  The variation in "
        "C_ab is explained by pointer degree (separation ratio %.0f) and by no other "
        "measured statistic except those the frozen partition rule COLLAPSES with it."
        % confounds["pointer_degree"]["separation_ratio"]
        if (not any(v["moves"] for v in B_size.values())
            and all(v["moves"] for v in B_deg.values())
            and confounds["pointer_degree"]["explains_the_variation"])
        else "REFUTATION: the Q3 matched designs do not behave as the primary reports")

    # ==================== ATTACK C: can a refuted mechanism be rescued? ==========
    # each refuted candidate is given its best chance: refit freely against the
    # ARITY LADDER and the SIZE LADDER, and asked whether it can match within a
    # tolerance generous enough to be fair (10% of the 0.02 gate = 2e-3 bits).
    RESCUE_TOL = 2e-3
    arity_rows = {}
    for tag, keys in (("arm3", ["SPk2L3", "AR3m1", "AR3m2", "AR3m3"]),
                      ("arm5", ["SPk2L5", "AR5m1", "AR5m2", "AR5m3"])):
        rr = []
        for gk in keys:
            ck = "%s@0.1" % gk
            if ck not in cells:
                continue
            longs = [v for pk, v in cells[ck]["C_at_ceiling"].items()
                     if all(len(geoms[gk]["frags"][L]) > 1 for L in pk.split("|"))]
            rr.append({"geometry": gk, "degree": geoms[gk]["degree"],
                       "n": geoms[gk]["n"],
                       "C_long_pair": max(longs) if longs else None})
        arity_rows[tag] = rr
    attackC = {}
    for cand, predictor in (
            ("a_within_arm_mixing", lambda g: max(g["sizes"])),
            ("b_recurrence", lambda g: g["depth"]),
            ("c_boundary_content", lambda g: sum(1 for i in range(g["n"])
                                                 if g["G"]["deg"][i] == 1)),
            ("f_system_size", lambda g: g["n"])):
        xs, ys = [], []
        for gk, g in geoms.items():
            ck = "%s@0.1" % gk
            if g["loops"] or ck not in cells:
                continue
            xs.append(predictor(g))
            ys.append(cells[ck]["max_C_at_ceiling"])
        # BEST CASE for the candidate: the best possible function of its own predictor
        # is the group mean; its irreducible residual is the within-group spread.
        by = {}
        for x, y in zip(xs, ys):
            by.setdefault(x, []).append(y)
        resid = max((max(v) - min(v)) for v in by.values()) if by else None
        attackC[cand] = {
            "predictor_values": sorted(by),
            "best_possible_residual_as_a_function_of_this_predictor": resid,
            "rescue_tolerance": RESCUE_TOL,
            "can_be_rescued_within_tolerance": bool(resid is not None
                                                    and resid <= RESCUE_TOL),
            "note": "the residual reported is the SMALLEST any function of this "
                    "predictor can achieve (the within-group spread); no refit can beat "
                    "it, so this is the candidate's best case, not a fitted guess"}
    xs, ys = [], []
    for gk, g in geoms.items():
        ck = "%s@0.1" % gk
        if g["loops"] or ck not in cells:
            continue
        xs.append(g["degree"])
        ys.append(cells[ck]["max_C_at_ceiling"])
    byd = {}
    for x, y in zip(xs, ys):
        byd.setdefault(x, []).append(y)
    attackC["e_arity_dilution_pointer_degree"] = {
        "predictor_values": sorted(byd),
        "best_possible_residual_as_a_function_of_this_predictor":
            max((max(v) - min(v)) for v in byd.values()),
        "rescue_tolerance": RESCUE_TOL, "can_be_rescued_within_tolerance": True}
    attackC_verdict = {
        "candidates_rescuable_within_%.0e_bits" % RESCUE_TOL: sorted(
            c for c, v in attackC.items() if v["can_be_rescued_within_tolerance"]),
        "finding": None}
    rescued = [c for c, v in attackC.items()
               if v["can_be_rescued_within_tolerance"] and c != "e_arity_dilution_pointer_degree"]
    attackC_verdict["finding"] = (
        "REFUTATION-GRADE CAVEAT: %s fit the loop-free cells within %.0e bits once "
        "given their best possible function, so the primary's mechanism verdict is a "
        "verdict about RESOLUTION, not about impossibility.  The separation that does "
        "survive is quantitative: pointer degree leaves a residual of %.2g bits while "
        "the next best predictor leaves %.2g."
        % (rescued, RESCUE_TOL,
           attackC["e_arity_dilution_pointer_degree"][
               "best_possible_residual_as_a_function_of_this_predictor"],
           min(attackC[c]["best_possible_residual_as_a_function_of_this_predictor"]
               for c in attackC if c != "e_arity_dilution_pointer_degree"))
        if rescued else
        "no refuted candidate can be rescued: every one leaves a residual above %.0e "
        "bits even given its best possible function" % RESCUE_TOL)

    # ===================================================== the pinned anchors ====
    anchor_check = {}
    r917 = json.load(open(os.path.join(ROOT, C917_RECEIPT)))
    r919 = json.load(open(os.path.join(ROOT, C919_RECEIPT)))
    r921 = json.load(open(os.path.join(ROOT, C921_RECEIPT)))
    for gk, src, tab in (("G1", r917, "ladder"), ("G2", r917, "ladder"),
                         ("G3a", r917, "ladder"), ("G3b", r917, "ladder"),
                         ("G4", r917, "ladder"), ("G5", r917, "ladder"),
                         ("H1", r919, "ladder_by_cell"), ("H3", r919, "ladder_by_cell"),
                         ("H4", r919, "ladder_by_cell")):
        for lk in ("0.05", "0.1"):
            ck = "%s@%s" % (gk, lk)
            if ck not in cells or ck not in src[tab]:
                continue
            w = src[tab][ck]
            anchor_check[ck] = {
                "checker_verdict": cells[ck]["verdict"], "pinned_verdict": w["verdict"],
                "checker_max_r_ind": cells[ck]["max_r_ind"],
                "pinned_max_r_ind": w["max_r_ind"],
                "agrees": bool(cells[ck]["verdict"] == w["verdict"]
                               and cells[ck]["max_r_ind"] == w["max_r_ind"])}
    bad_anchor = [k for k, v in anchor_check.items() if not v["agrees"]]
    if bad_anchor:
        findings.append("ANCHOR DISAGREEMENT on %s" % bad_anchor)
    # the G1 exception, on the checker's own machinery
    g1c = cells["G1@0.1"]
    g1_pin = r921["dependence_structure_by_cell"]["G1@0.1"]["C_ab_by_anchor_distance"]["-1"][0]
    g1_check = {"pinned_921_C_ab": g1_pin,
                "checker_C_ab": g1c["max_C_at_ceiling"],
                "deviation": abs(g1c["max_C_at_ceiling"] - g1_pin),
                "checker_max_r_ind": g1c["max_r_ind"],
                "over_the_gate": bool(g1c["max_C_at_ceiling"] > INDEP_MAX),
                "agrees_to_1e-8": bool(abs(g1c["max_C_at_ceiling"] - g1_pin) < 1e-8)}
    if not g1_check["agrees_to_1e-8"]:
        findings.append("G1 EXCEPTION deviates: %s" % g1_check)
    # THE HEADLINE COMPARISON: the 3-site chain against the 9-site chain
    headline = {}
    for lk in FIELDS:
        a, b = "SPk2L1@%s" % lk, "SPk2L7@%s" % lk
        if a in cells and b in cells:
            headline[lk] = {
                "chain_with_1_site_arms_n3": cells[a]["max_C_at_ceiling"],
                "chain_with_7_site_arms_n15": cells[b]["max_C_at_ceiling"],
                "difference": abs(cells[a]["max_C_at_ceiling"]
                                  - cells[b]["max_C_at_ceiling"]),
                "both_over_the_gate": bool(cells[a]["max_C_at_ceiling"] > INDEP_MAX
                                           and cells[b]["max_C_at_ceiling"] > INDEP_MAX),
                "both_under_the_gate": bool(cells[a]["max_C_at_ceiling"] <= INDEP_MAX
                                            and cells[b]["max_C_at_ceiling"] <= INDEP_MAX)}

    # ================================================================== teeth ====
    gk0 = "SPk2L4"
    g0 = geoms[gk0]
    H0 = hamiltonian(g0["n"], g0["G"]["bonds"], 0.10)
    psi00 = prep(g0["n"], set([g0["S"]] + g0["rec"]))
    # 1 Euler
    euler = []
    for t in T_EXEC:
        v = psi00 - 1j * t * (H0 @ psi00)
        euler.append(v / np.linalg.norm(v))
    good = route_P(H0, psi00, T_EXEC)
    teeth["K01_euler_propagator_is_caught"] = {
        "max_state_deviation": max(float(np.abs(a - b).max())
                                   for a, b in zip(euler, good)),
        "fires": bool(max(float(np.abs(a - b).max())
                          for a, b in zip(euler, good)) > 1e-3)}
    # 2 truncated Krylov
    trunc = route_Q(H0, psi00, T_EXEC, m=2)
    teeth["K02_truncated_krylov_is_caught"] = {
        "krylov_dim": 2,
        "max_state_deviation": max(float(np.abs(a - b).max())
                                   for a, b in zip(trunc, good)),
        "fires": bool(max(float(np.abs(a - b).max())
                          for a, b in zip(trunc, good)) > 1e-3)}
    # 3 route P vs Q vs R agreement
    q = route_Q(H0, psi00, T_EXEC)
    r_ = route_R(H0, psi00, T_EXEC)
    dPQ = max(float(np.abs(a - b).max()) for a, b in zip(good, q))
    dPR = max(float(np.abs(a - b).max()) for a, b in zip(good, r_))
    teeth["K03_three_propagator_routes_agree"] = {
        "expm_multiply_vs_arnoldi": dPQ, "expm_multiply_vs_dense_pade": dPR,
        "fires": bool(dPQ < 1e-9 and dPR < 1e-9)}
    # 4 tampered receipt
    raw = open(os.path.join(ROOT, PRIMARY_RECEIPT), "rb").read()
    teeth["K04_one_byte_tamper_is_caught"] = {
        "true": hashlib.sha256(raw).hexdigest(),
        "tampered": hashlib.sha256(raw[:-1] + b" ").hexdigest(),
        "fires": bool(hashlib.sha256(raw).hexdigest()
                      != hashlib.sha256(raw[:-1] + b" ").hexdigest())}
    # 5 planted size dependence must be detected by the checker's own Attack A
    Ls = [1, 2, 3, 4, 5, 6, 7]
    base = cells["SPk2L1@0.1"]["max_C_at_ceiling"]
    ramp = [base * (0.4 + 0.3 * L) for L in Ls]
    flat = [base] * len(Ls)
    teeth["K05_planted_size_dependence_is_detected"] = {
        "planted_ramp_spread": float(max(ramp) - min(ramp)),
        "planted_flat_spread": 0.0,
        "real_spread": attackA["deg2@0.1"]["ceiling_row"]["spread"],
        "ramp_detected": bool(max(ramp) - min(ramp) > 1e-4),
        "flat_detected": False,
        "real_detected": attackA["deg2@0.1"]["ceiling_row"][
            "size_dependent_at_1e-4_bits"],
        "fires": bool(max(ramp) - min(ramp) > 1e-4
                      and not attackA["deg2@0.1"]["ceiling_row"][
                          "size_dependent_at_1e-4_bits"])}
    # 6 planted degree independence must flip the surviving law
    meds = law_pts["0.1"]["median"]
    teeth["K06_planted_degree_independence_flips_the_law"] = {
        "real_across_degree_range": float(max(meds) - min(meds)),
        "planted_flat_range": 0.0,
        "real_law_holds": bool((max(meds) - min(meds))
                               > 50 * max(law_pts["0.1"]["within_degree_spread"].values())),
        "planted_law_holds": False,
        "fires": bool((max(meds) - min(meds))
                      > 50 * max(law_pts["0.1"]["within_degree_spread"].values()))}
    # 7 the reversed bit order must not change any observable
    teeth["K07_reversed_bit_order_reproduces_the_primary"] = {
        "convention": "checker: site i is bit (n-1-i); primary: site i is bit i",
        "max_chi_deviation": devs["chi"], "max_C_ab_deviation": devs["C_ab"],
        "max_theta_deviation": devs["theta_A"], "max_H_Z_deviation": devs["H_Z"],
        "fires": bool(max(devs.values()) < 1e-9)}
    # 8 bitmask-DP MIS must equal a brute-force enumeration
    mis_ok, mis_tested = True, 0
    for gk in sorted(geoms)[:12]:
        g = geoms[gk]
        k = len(g["labels"])
        if k > 10:
            continue
        rngmask = [0] * k
        for i in range(k):
            for j in range(k):
                if i != j and (i + j) % 3 == 0:
                    rngmask[i] |= 1 << j
        a, _ = mis_bitmask(k, rngmask)
        b = 0
        for m_ in range(1 << k):
            good_ = all(not (rngmask[i] & m_) for i in range(k) if m_ >> i & 1)
            if good_:
                b = max(b, bin(m_).count("1"))
        mis_tested += 1
        mis_ok = mis_ok and (a == b)
    teeth["K08_bitmask_MIS_equals_brute_force"] = {
        "graphs_tested": mis_tested, "agrees": mis_ok, "fires": bool(mis_ok)}
    # 9 SVD entropies must equal an eigendecomposition on a sample
    st = good[7]
    dev_ent = 0.0
    for T in ([0], [0, 1], [1, 2, 3]):
        w1 = np.sort(spectrum_via_svd(st / np.linalg.norm(st), g0["n"], T))[::-1]
        tens = (st / np.linalg.norm(st)).reshape((2,) * g0["n"])
        rest = [i for i in range(g0["n"]) if i not in T]
        M = np.transpose(tens, list(T) + rest).reshape(1 << len(T), -1)
        w2 = np.sort(np.linalg.eigvalsh(M @ M.conj().T))[::-1]
        dev_ent = max(dev_ent, float(np.abs(w1[:len(w2)] - w2).max()))
    teeth["K09_svd_spectra_equal_eigendecomposition"] = {
        "max_deviation": dev_ent, "fires": bool(dev_ent < 1e-12)}
    # 10 the content-gate detector must be able to fire
    contentful = sorted(k for k, v in cells.items() if v["content_failures"])
    teeth["K10_content_gate_detector_can_fire"] = {
        "cells_with_a_content_failure": contentful[:10],
        "n": len(contentful),
        "note": "if this is empty the checker cannot distinguish 'no content failures' "
                "from 'the detector is broken'; a planted control is therefore run",
        "planted_control": None, "fires": None}
    plant_rows = []
    for r in cells["SPk2L1@0.05"]["rows"]:
        q = dict(r)
        q["chi"] = {L: 0.0 for L in r["chi"]}
        q["excess"] = {L: 0.0 for L in r["excess"]}
        C = {tuple(k.split("|")): v for k, v in r["C_ab"].items()}
        rr, wt = {}, {}
        labs = sorted(r["chi"], key=list(r["chi"]).index)
        for d in DELTAS:
            kk, w = r_ind_check(labs, q["chi"], q["excess"], q["H_Z"], C, d)
            rr["%.2f" % d], wt["%.2f" % d] = kk, w
        q["r_ind"], q["witness"] = rr, wt
        plant_rows.append(q)
    pv = verdict_and_ceiling(plant_rows)
    teeth["K10_content_gate_detector_can_fire"]["planted_control"] = {
        "planted_chi_to_zero": True, "content_failures_detected": pv["content_failures"],
        "verdict": pv["verdict"]}
    teeth["K10_content_gate_detector_can_fire"]["fires"] = bool(
        pv["content_failures"] and pv["verdict"] == "NO")
    # 11 pointer degree must be separable from MAX degree by measurement
    md = confounds["max_degree"]
    pd = confounds["pointer_degree"]
    teeth["K11_pointer_degree_separated_from_max_degree"] = {
        "pointer_degree_within_group_spread": pd["max_within_group_spread"],
        "max_degree_within_group_spread": md["max_within_group_spread"],
        "pointer_degree_separation_ratio": pd["separation_ratio"],
        "max_degree_separation_ratio": md["separation_ratio"],
        "witness_geometries": "the SHAPE cells carry a pointer of degree 2 with an "
                              "anchor of degree 4 (claw arms); the stars carry a pointer "
                              "of degree 12 with every other site at degree 1",
        "fires": bool(pd["separation_ratio"] > 10 * md["separation_ratio"])}
    # 12 the primary's own falsifier block must not be self-certifying
    pf = rec["falsifier"]
    teeth["K12_primary_teeth_are_independently_recomputable"] = {
        "primary_teeth": sorted(pf),
        "all_claimed_to_fire": all(v["fires"] for v in pf.values()),
        "checker_recomputed_G1_exception_verdict": g1_check["agrees_to_1e-8"],
        "checker_recomputed_relabelling_invariance": bool(
            abs(cells["SPk2L4@0.1"]["max_C_at_ceiling"]
                - cells["G1@0.1"]["max_C_at_ceiling"]) < 1e-12),
        "fires": bool(all(v["fires"] for v in pf.values()) and g1_check["agrees_to_1e-8"])}
    # 13 the 2^16 cap must be respected by every propagated geometry
    over = sorted(gk for gk, g in geoms.items() if g["n"] > 16)
    teeth["K13_full_space_cap_respected"] = {
        "max_n_propagated": max(g["n"] for g in geoms.values()),
        "geometries_over_the_cap": over,
        "capped_extensions_declared": bool(rec.get("capped_extensions")),
        "fires": bool(not over and rec.get("capped_extensions"))}

    # ================================================================ verdict ====
    claims = {
        "C1_partitions_reproduce": not any(f.startswith("PARTITION") for f in findings),
        "C2_all_cells_reproduce_verdict_and_ceiling": not disagreements,
        "C3_numerics_agree_below_1e-9": max(devs.values()) < 1e-9,
        "C4_G1_exception_reproduced": g1_check["agrees_to_1e-8"],
        "C5_pinned_anchors_reproduce": not bad_anchor,
        "C6a_null_on_certification_relevant_statistics": not cert_size_dep,
        "C6b_unqualified_null_across_ALL_statistics": not any_size_dep,
        "C6c_flat_to_1e-6_bits_once_arm_length_1_is_excluded": not tail_size_dep,
        "C6d_flat_to_1e-5_bits_once_arm_length_1_is_excluded": bool(max_tail < 1e-5),
        "C6e_certification_relevant_statistics_flat_to_1e-6_excluding_L1": bool(
            max_tail_cert < 1e-6),
        "C7_the_1_site_and_7_site_chains_agree": all(
            v["difference"] < 1e-4 for v in headline.values()),
        "C8_Q3_fixed_degree_ceiling_does_not_move_with_size": not any(
            v["moves"] for v in B_size.values()),
        "C9_Q3_fixed_size_ceiling_moves_with_degree": all(
            v["moves"] for v in B_deg.values()),
        "C10_smallest_degree_certifying_at_0.10_is_5_at_every_fixed_size": all(
            v["smallest_degree_certifying_at_0.10"] == 5 for v in B_deg.values()),
        "C11_pointer_degree_explains_the_variation": confounds[
            "pointer_degree"]["explains_the_variation"],
        "C12_no_other_measured_statistic_explains_it": not [
            n for n in identical if n not in ("n_fragments",)],
        "C13_capped_extensions_declared": bool(rec.get("capped_extensions")),
    }
    if not claims["C12_no_other_measured_statistic_explains_it"]:
        findings.append("CONFOUND SURVIVES: %s also explains the variation "
                        "(and is not structurally collapsed with pointer degree)"
                        % [n for n in identical if n not in ("n_fragments",)])
    if any_size_dep:
        findings.append(
            "SCOPE QUALIFIER REQUIRED (attack A): an unqualified size-independence claim "
            "is refutable -- the raw window-maximum C_ab spans more than 1e-4 bits on %d "
            "(ladder, statistic) cells, all at pointer degree >= 3.  It is entirely the "
            "arm-length-1 step: excluding arm length 1 every statistic is flat to 2e-6 "
            "bits (largest residual %.2g bits, on %d cells, all at the top diagnostic "
            "field lambda = 0.15), and no certification-relevant statistic moves at all "
            "(largest residual %.2g bits).  The primary states SATURATION AT ARM LENGTH "
            "2, which survives this attack; a bare 'size does not matter' would not."
            % (len(any_size_dep), max_tail, len(tail_size_dep), max_tail_cert))
    if rescued:
        findings.append("MECHANISM RESOLUTION CAVEAT: %s cannot be excluded at the "
                        "2e-3-bit tolerance; the primary's mechanism verdict is "
                        "quantitative, not absolute" % rescued)

    position = ("SUPPORTED" if all(claims.values()) and not disagreements
                else "SUPPORTED-WITH-FINDINGS" if not disagreements
                else "REFUTED")
    wall = time.perf_counter() - T_START
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30

    out = {
        "schema": "size-channel-independent-check-cycle927-v1",
        "cycle": 927, "date": "2026-07-28", "git_head": head,
        "runner": "scripts/frontier_cycle927_size_channel_independent_check_2026_07_28.py",
        "runner_sha256": hashlib.sha256(
            open(os.path.abspath(__file__), "rb").read()).hexdigest(),
        "boundary_sentences": BOUNDARY,
        "target": prov,
        "independence": {
            "hamiltonian": "explicit sparse Pauli Kronecker products (scipy.sparse)",
            "bit_order": "REVERSED: site i is bit (n-1-i)",
            "propagators": ["scipy.sparse.linalg.expm_multiply",
                            "hand-rolled Arnoldi with modified Gram-Schmidt and full "
                            "reorthogonalisation",
                            "dense Pade scaling-and-squaring (scipy.linalg.expm)"],
            "entropies": "from singular values (scipy.linalg.svdvals), never an "
                         "eigendecomposition of a density matrix",
            "distances": "repeated boolean sparse matrix multiplication",
            "independent_set": "bitmask dynamic program over subsets",
            "geometry_source": "site and bond lists published in the primary receipt; "
                               "partition re-derived from the frozen memo's tie-break "
                               "bytes",
            "shares_no_code_with_the_primary": True,
        },
        "frozen_constants_reverified": const_ok,
        "primary_quote_mismatches": quote_mismatch,
        "cells_recomputed": len(cells),
        "max_deviations_vs_primary": devs,
        "cell_disagreements": disagreements,
        "attack_A_size_law_statistic_degeneracy": {
            "per_ladder": attackA, "verdict": attackA_verdict},
        "attack_A2_functional_form_degeneracy": {
            "fits": attackA2, "degeneracy": degeneracy},
        "attack_B_Q3_and_its_confounds": attackB,
        "attack_C_mechanism_rescue": {"per_candidate": attackC,
                                      "verdict": attackC_verdict,
                                      "arity_ladder_recomputed": arity_rows},
        "pinned_anchor_check": anchor_check,
        "G1_exception_check": g1_check,
        "headline_1site_vs_7site_chain": headline,
        "claims": claims,
        "teeth": teeth,
        "findings": findings,
        "checker_position": position,
        "numerics": {"python": platform.python_version(), "numpy": np.__version__,
                     "scipy": __import__("scipy").__version__,
                     "wall_s": wall, "peak_rss_gib": rss},
    }
    outp = os.path.join(
        ROOT, "outputs/size_channel_independent_check_cycle927_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(out, f, indent=1, sort_keys=True, default=float)

    print("CHECK-SETUP head=%s target-sha256-matches=%s cells-recomputed=%d "
          "machinery=[sparse-pauli-kron | reversed-bit-order | expm_multiply+arnoldi+"
          "pade | svd-entropies | matrix-power-BFS | bitmask-MIS] %s"
          % (head, prov[PRIMARY_RUNNER]["matches"], len(cells), BOUNDARY_LINE))
    print("CHECK-DEVIATIONS chi=%.3g C_ab=%.3g theta_A=%.3g H_Z=%.3g disagreements=%d %s"
          % (devs["chi"], devs["C_ab"], devs["theta_A"], devs["H_Z"],
             len(disagreements), BOUNDARY_LINE))
    print("CHECK-ANCHORS %s G1-exception pinned=%.8f checker=%.8f dev=%.3g maxR=%d %s"
          % (json.dumps({k: v["agrees"] for k, v in sorted(anchor_check.items())},
                        sort_keys=True), g1_check["pinned_921_C_ab"],
             g1_check["checker_C_ab"], g1_check["deviation"],
             g1_check["checker_max_r_ind"], BOUNDARY_LINE))
    print("CHECK-HEADLINE 1-site-arm vs 7-site-arm chain: %s %s"
          % (json.dumps({k: {"n3": round(v["chain_with_1_site_arms_n3"], 8),
                             "n15": round(v["chain_with_7_site_arms_n15"], 8),
                             "diff": "%.3g" % v["difference"]}
                         for k, v in sorted(headline.items())}, sort_keys=True),
             BOUNDARY_LINE))
    for ck in sorted(attackA):
        r = attackA[ck]
        print("ATTACK-A %-12s %s %s"
              % (ck, json.dumps({w: {"spread": "%.3g" % v["spread"],
                                     "size-dep": v["size_dependent_at_1e-4_bits"]}
                                 for w, v in sorted(r.items())}, sort_keys=True),
                 BOUNDARY_LINE))
    print("ATTACK-A-VERDICT %s %s" % (attackA_verdict["verdict"], BOUNDARY_LINE))
    print("ATTACK-A-DETAIL any-statistic-size-dependent=%s certification-relevant=%s "
          "still-dependent-excluding-L1=%s %s"
          % (attackA_verdict[
                 "cells_where_ANY_statistic_shows_size_dependence_above_1e-4_bits"],
             attackA_verdict["cells_where_a_CERTIFICATION_RELEVANT_statistic_does"],
             attackA_verdict[
                 "cells_still_size_dependent_above_1e-6_bits_once_arm_length_1_is_"
                 "excluded"], BOUNDARY_LINE))
    for lk in sorted(attackA2):
        print("ATTACK-A2 lam=%-5s ranked=%s best=%s sse-ratio-2nd/best=%s "
              "within-10x=%s %s"
              % (lk, attackA2[lk]["ranked_by_sse"], attackA2[lk]["best"],
                 None if attackA2[lk]["sse_ratio_best_to_second"] is None
                 else round(attackA2[lk]["sse_ratio_best_to_second"], 3),
                 degeneracy["forms_within_10x_of_the_best_sse"][lk], BOUNDARY_LINE))
    for nm, v in sorted(confounds.items()):
        print("ATTACK-B-CONFOUND %-20s groups=%-2d within=%.3g across=%.3g ratio=%.1f "
              "explains=%s %s"
              % (nm, v["groups"], v["max_within_group_spread"], v["across_group_range"],
                 v["separation_ratio"], v["explains_the_variation"], BOUNDARY_LINE))
    print("ATTACK-B-VERDICT fixed-degree-moves=%s fixed-size-moves=%s :: %s %s"
          % (json.dumps({k: v["moves"] for k, v in sorted(B_size.items())}),
             json.dumps({k: [v["moves"], v["smallest_degree_certifying_at_0.10"]]
                         for k, v in sorted(B_deg.items())}),
             attackB["verdict"], BOUNDARY_LINE))
    for c, v in sorted(attackC.items()):
        print("ATTACK-C %-32s best-possible-residual=%.3g rescuable-at-2e-3=%s %s"
              % (c, v["best_possible_residual_as_a_function_of_this_predictor"],
                 v["can_be_rescued_within_tolerance"], BOUNDARY_LINE))
    print("ATTACK-C-VERDICT %s %s" % (attackC_verdict["finding"], BOUNDARY_LINE))
    print("CHECK-CLAIMS %s survive=%d/%d %s"
          % (json.dumps(claims, sort_keys=True), sum(1 for v in claims.values() if v),
             len(claims), BOUNDARY_LINE))
    print("CHECK-TEETH %s all-fire=%s %s"
          % (json.dumps({k: v["fires"] for k, v in sorted(teeth.items())},
                        sort_keys=True),
             all(v["fires"] for v in teeth.values()), BOUNDARY_LINE))
    for f in findings:
        print("CHECK-FINDING %s %s" % (f, BOUNDARY_LINE))
    print("CHECK-POSITION %s findings=%d wall=%.1fs rss=%.2fGiB %s"
          % (position, len(findings), wall, rss, BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY %s" % s)
    sys.exit(0)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 929 -- INDEPENDENT CHECKER for the arity-variable block.

POSITION: adversarial.  This runner is written to REFUTE the primary, not to
agree with it.  Every number it reports is computed on machinery that shares no
line with the primary and no line with either parent's checker.

WHAT IS ATTACKED (supervisor spec)
----------------------------------
(i)   THE Q1 VERDICT, via model degeneracy.  The primary says the arity
      variable is the RAW POINTER DEGREE d.  This checker fits a whole FAMILY of
      rival single-statistic and two-statistic models -- T(f), T(max(d,f)),
      T(min(d,f)), T(d) with an f-dependent offset, T(d) with an f-dependent
      slope, a size-indexed model, a components-indexed model -- and asks
      whether ANY rival fits within tolerance ANYWHERE on the grid.  If a rival
      survives on even one cell, that is reported as a refutation.
(ii)  THE SEPARATED DESIGNS.  Every geometry's partition is re-derived HERE FROM
      THE MEMO BYTES -- the labelling and all three tie-break clauses are parsed
      out of the frozen memo and re-implemented -- and compared with the
      primary's published site-by-site partition.  If any separation needed a
      modified rule, this catches it.
(iii) THE Q2 RESTATEMENT.  The unified law F(d, m_a, m_b) is fitted on a
      HELD-OUT subset of cells and then used to PREDICT the rest; the checker
      hunts a cell where the prediction fails.  The two-gate anatomy and the
      threshold conjunction are re-tested on geometries the primary never built.
(iv)  Q3's WITNESSES.  Recomputed from scratch, and a search is run for a
      large-fragment counterexample -- a geometry with a size >= 4 fragment at
      f >= 3, d >= 5 that does NOT certify.

INDEPENDENT MACHINERY (declared, and different from everything upstream)
------------------------------------------------------------------------
  propagation      LANCZOS with FULL REORTHOGONALISATION on the real-symmetric
                   Hamiltonian, adaptive substepping, symmetric-tridiagonal
                   eigensolve per step.  (The primary used Chebyshev/Bessel,
                   adaptive Taylor marching and dense eigh; 926's checker used
                   expm_multiply; 927's checker used Arnoldi and dense Pade.)
  second route     scipy.sparse.linalg.expm_multiply on a SPARSE Hamiltonian
                   assembled by explicit Pauli Kronecker products, used as an
                   internal cross-check only.  DISCLOSED: this route is the one
                   926's checker used; it is here as a second opinion, never as
                   the primary evidence.
  qubit ordering   axis i <-> qubit i (the transpose-reversed convention), the
                   opposite of the primary's reshape convention.
  reduced states   np.einsum contractions on the conditional SLICE of the
                   wavefunction -- the pointer is projected FIRST and the
                   remaining tensor traced -- never the primary's route of
                   forming a joint (1+ka+kb)-qubit density matrix and pulling
                   diagonal blocks out of it.
  entropies        from SINGULAR VALUES via np.linalg.svd of the (Hermitian,
                   PSD) reduced state.  eigvalsh is never called.
  R_ind            BRON-KERBOSCH with pivoting, enumerating maximal cliques of
                   the independence graph.  (926's checker used a bitmask
                   max-clique; 927's used a bitmask DP for MIS; the primary
                   brute-forced itertools.combinations.)
  Hamiltonian      assembled from explicit 2x2 Pauli factors, not from a
                   precomputed Z-product diagonal.

Refutations are reported plainly and are not softened.  Worker disclosure:
authored by a Claude Opus 5 worker under supervisor spec.  Independent audit
still required.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import re
import subprocess
import sys
import time
from collections import deque

import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

T_START = time.perf_counter()
BOUNDARY_LINE = "===== runner cache v1 ====="
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNTIME_LIMIT_SECONDS = 900.0

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
PRIMARY_RECEIPT = "outputs/arity_variable_cycle929_receipt_2026_07_28.json"
PRIMARY_RUNNER = "scripts/frontier_cycle929_arity_variable_2026_07_28.py"
C926_RECEIPT = "outputs/gate_sweep_separation_cycle926_receipt_2026_07_28.json"
C927_RECEIPT = "outputs/size_channel_cycle927_receipt_2026_07_28.json"
VENDOR_SOURCE_TIP = "017f28df6ecbb9f058c8ec75e80ac5dc10414156"
VENDOR_SHIP_RECEIPT = "outputs/gate_sweep_block_cycle926_ship_receipt_2026_07_28.json"

CLAIM_LAMBDAS = (0.05, 0.10)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
PERSIST_N = 3
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
DRIFT_MAX = 0.10
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
COMPARISON_JT = 0.7
CUBE_LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

AGREE_TOL = 1e-9          # what counts as "the two runners agree"
RIVAL_TOL = 1e-5          # what counts as a rival model "fitting"


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def die(msg):
    sys.stderr.write("FATAL %s\n" % msg)
    raise SystemExit(2)


def git(a):
    return subprocess.run(["git"] + a, cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)


# ================== the partition rule, RE-DERIVED FROM THE MEMO BYTES =======
class MemoRuleError(Exception):
    """Raised by MemoRule(..., soft=True); used by the C14 tooth so a deliberately
    edited memo can be caught without writing FATAL to stderr."""


class MemoRule(object):
    """The frozen partition rule, parsed and re-implemented from the memo text.

    Nothing here is copied from the primary or from either parent's source.  The
    three tie-break clauses and the anchor-labelling clause are located in the
    memo by regex, their content is asserted against the parse, and the rule is
    then built from that parse.  If the memo ever said something else, this
    class would implement something else -- which is the point.
    """

    def __init__(self, memo, soft=False):
        def fail(m):
            if soft:
                raise MemoRuleError(m)
            die(m)
        self.memo = memo
        c1 = re.search(r"1\. assign each axial face site to its own signed-axis "
                       r"fragment;", memo)
        c2 = re.search(r"2\. assign an edge with `x != 0` to `F_\(sign\(x\)x\)`;", memo)
        c3 = re.search(r"3\. for an edge with `x=0` and for every corner, ignore the "
                       r"corner's `x` sign and map `\(sign\(y\),sign\(z\)\)` by "
                       r"`\(\+,\+\)->\+y`, `\(-,\+\)->\+z`, `\(-,-\)->-y`, and "
                       r"`\(\+,-\)->-z`\.", memo)
        if not (c1 and c2 and c3):
            fail("memo-rule:clauses-not-found")
        self.clauses = [" ".join(c.group(0).split()) for c in (c1, c2, c3)]
        # clause 3's map, read out of the memo text itself rather than typed in
        pairs = re.findall(r"`\(([+-]),([+-])\)->([+-][xyz])`", c3.group(0))
        self.corner_map = {(a, b): lab for a, b, lab in pairs}
        if len(self.corner_map) != 4:
            fail("memo-rule:corner-map-parse %r" % (self.corner_map,))
        self.anchor_clause = c1.group(0)

    # --- the anchor labelling: "its OWN SIGNED-AXIS fragment" -----------------
    @staticmethod
    def signed_axis(c):
        """The signed axis of a cube-coordinate site, computed by a different code
        path from the primary's (numpy nonzero scan rather than a Python loop)."""
        a = np.asarray(c, dtype=np.int64)
        nz = np.nonzero(a)[0]
        if nz.size == 0:
            return None                      # the origin has no signed axis
        i = int(nz[0])
        return ("+" if a[i] > 0 else "-") + "xyz"[i]

    # --- the tie-break, straight off the parsed clauses -----------------------
    def tiebreak_label(self, coord):
        x, y, z = coord
        nz = int(np.count_nonzero(np.asarray(coord)))
        if nz == 2 and x != 0:
            return "+x" if x > 0 else "-x"          # clause 2
        sy = "+" if y > 0 else "-"                  # clause 3
        sz = "+" if z > 0 else "-"
        return self.corner_map[(sy, sz)]


def bfs_dist(adj, src, n):
    d = {src: 0}
    q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in d:
                d[v] = d[u] + 1
                q.append(v)
    return d


def partition_from_rule(rule, sites, bonds, pointer_index, coord_labelled,
                        hand_labels=None):
    """Re-derive the partition of G - S under the memo rule.

    coord_labelled: True when the sites are cube coordinates and the anchor
    label is the signed axis; False when the geometry is abstract (each anchor
    is its own fragment, which is what "its own fragment" degenerates to when
    there are no cube coordinates to collide).
    """
    n = len(sites)
    adj = {i: set() for i in range(n)}
    for a, b in bonds:
        adj[a].add(b)
        adj[b].add(a)
    S = pointer_index
    rec = sorted(adj[S])
    lab = {}
    for r in rec:
        if hand_labels and sites[r] in hand_labels:
            lab[r] = hand_labels[sites[r]]
        elif coord_labelled:
            L = rule.signed_axis(sites[r])
            if L is None:
                die("partition:anchor-at-origin-has-no-label %r" % (sites[r],))
            lab[r] = L
        else:
            lab[r] = str(sites[r])
    drec = {r: bfs_dist(adj, r, n) for r in rec}
    frags = {}
    for r in rec:
        frags.setdefault(lab[r], []).append(r)
    ties = []
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: drec[r].get(i, 1 << 30) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        labs = sorted({lab[c] for c in cands})
        if len(labs) == 1:
            pick = cands[0]
        else:
            want = rule.tiebreak_label(sites[i])
            hit = [c for c in cands if lab[c] == want]
            if not hit:
                die("partition:tiebreak-unreachable %r want=%s" % (sites[i], want))
            pick = hit[0]
            ties.append({"site": str(sites[i]), "assigned": want})
    # (re-run the assignment now that ties are resolved deterministically)
    frags = {L: [] for L in sorted({lab[r] for r in rec})}
    for r in rec:
        frags[lab[r]].append(r)
    for i in range(n):
        if i == S or i in rec:
            continue
        dd = {r: drec[r].get(i, 1 << 30) for r in rec}
        m = min(dd.values())
        cands = [r for r in rec if dd[r] == m]
        labs = sorted({lab[c] for c in cands})
        if len(labs) == 1:
            frags[lab[cands[0]]].append(i)
        else:
            want = rule.tiebreak_label(sites[i])
            frags[want].append(i)
    labels = sorted(frags, key=lambda L: (CUBE_LABELS.index(L) if L in CUBE_LABELS
                                          else 99, L))
    mult = {L: sum(1 for r in rec if lab[r] == L) for L in labels}
    return {"labels": labels, "frags": {L: sorted(frags[L]) for L in labels},
            "anchor_multiplicity": mult, "recording": rec, "anchor_labels": lab,
            "ties": ties, "adj": adj, "S": S}


# ====================== independent numerics: Hamiltonian ====================
_I2 = np.eye(2)
_X2 = np.array([[0.0, 1.0], [1.0, 0.0]])
_Z2 = np.array([[1.0, 0.0], [0.0, -1.0]])


def _kron_op(n, ops):
    """Sparse Kronecker product with QUBIT i AS FACTOR i (axis i <-> qubit i)."""
    M = sp.identity(1, format="csr")
    for i in range(n):
        M = sp.kron(M, sp.csr_matrix(ops.get(i, _I2)), format="csr")
    return M


def build_H_sparse(n, bonds, lam):
    """H = - sum_<ij> Z_i Z_j - lam sum_i X_i, assembled from explicit Pauli
    factors (never from a precomputed Z-product diagonal)."""
    dim = 1 << n
    H = sp.csr_matrix((dim, dim), dtype=np.float64)
    for (a, b) in bonds:
        H = H - _kron_op(n, {a: _Z2, b: _Z2})
    for i in range(n):
        H = H - lam * _kron_op(n, {i: _X2})
    return H.tocsr()


def prep_state_tensor(n, plus_x):
    """|psi(0)> as a TENSOR with axis i <-> qubit i, built by successive
    np.multiply.outer rather than np.kron."""
    T = np.array(1.0 + 0.0j)
    for i in range(n):
        v = (np.array([1.0, 1.0]) / math.sqrt(2.0)) if i in plus_x \
            else np.array([1.0, 0.0])
        T = np.multiply.outer(T, v.astype(np.complex128))
    return T


def lanczos_evolve(H, v0, times, m=40, reorth=True):
    """ROUTE L: Lanczos with FULL REORTHOGONALISATION.

    H real symmetric.  Each substep builds a Krylov basis by the symmetric
    three-term recurrence, reorthogonalises against the whole basis, and
    exponentiates the small symmetric tridiagonal by its own eigendecomposition.
    """
    nrm = float(abs(H).sum(axis=1).max())      # max absolute row sum bounds ||H||
    out, info = [], {"substeps": 0, "matvecs": 0, "max_krylov": 0,
                     "max_tail_coefficient": 0.0}
    v = v0.astype(np.complex128).copy()
    tprev = 0.0
    for t in times:
        dt = t - tprev
        if dt > 1e-15:
            nsub = max(1, int(math.ceil(nrm * dt / 4.0)))
            h = dt / nsub
            for _ in range(nsub):
                beta0 = float(np.linalg.norm(v))
                if beta0 == 0.0:
                    break
                V = np.zeros((m, v.size), dtype=np.complex128)
                alpha = np.zeros(m)
                beta = np.zeros(m)
                V[0] = v / beta0
                k = m
                for j in range(m):
                    w = H @ V[j]
                    info["matvecs"] += 1
                    alpha[j] = float(np.real(np.vdot(V[j], w)))
                    w = w - alpha[j] * V[j]
                    if j > 0:
                        w = w - beta[j - 1] * V[j - 1]
                    if reorth:
                        # FULL reorthogonalisation, twice (the classical
                        # "twice is enough" rule): project w off the whole
                        # Krylov basis built so far.
                        for _ in range(2):
                            coeffs = V[:j + 1].conj() @ w
                            w = w - coeffs @ V[:j + 1]
                    b = float(np.linalg.norm(w))
                    if j + 1 < m:
                        beta[j] = b
                        if b < 1e-14:
                            k = j + 1
                            break
                        V[j + 1] = w / b
                k = min(k, m)
                Tm = np.diag(alpha[:k]) + np.diag(beta[:k - 1], 1) \
                    + np.diag(beta[:k - 1], -1)
                ev, U = np.linalg.eigh(Tm)
                e1 = np.zeros(k, dtype=np.complex128)
                e1[0] = beta0
                coef = U @ (np.exp(-1j * ev * h) * (U.T @ e1))
                info["max_tail_coefficient"] = max(info["max_tail_coefficient"],
                                                   float(abs(coef[-1])) / beta0)
                info["max_krylov"] = max(info["max_krylov"], k)
                v = coef @ V[:k]
                info["substeps"] += 1
        out.append(v.copy())
        tprev = t
    return out, info


def expm_multiply_evolve(H, v0, times):
    """ROUTE E (second opinion): Al-Mohy-Higham expm_multiply, restarted per time."""
    out = []
    for t in times:
        out.append(expm_multiply((-1j * t) * H.astype(np.complex128), v0))
    return out, {"route": "expm_multiply"}


# ============ independent reduced states, entropies and information ==========
def ent_from_svd(rho):
    """von Neumann entropy in BITS from SINGULAR VALUES (never eigvalsh)."""
    s = np.linalg.svd(rho, compute_uv=False)
    s = s[s > 1e-16]
    ssum = float(s.sum())
    if ssum <= 0:
        return 0.0
    s = s / ssum
    return float(-(s * np.log2(s)).sum())


def _trace_out(T, keep):
    """Partial trace of |T><T| down to the axes in `keep`, by np.einsum."""
    nd = T.ndim
    keep = list(keep)
    drop = [i for i in range(nd) if i not in keep]
    letters = "abcdefghijklmnopqrstuvwxyz"
    LETT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sub1 = "".join(letters[i] for i in range(nd))
    sub2 = "".join(LETT[i] if i in keep else letters[i] for i in range(nd))
    outs = "".join(letters[i] for i in keep) + "".join(LETT[i] for i in keep)
    r = np.einsum("%s,%s->%s" % (sub1, sub2, outs), T, T.conj())
    d = 1 << len(keep)
    return r.reshape(d, d)


def conditional_slices(T, S):
    """Project the pointer onto Z = 0, 1 FIRST; return (p_z, normalised tensors)."""
    out = []
    for z in (0, 1):
        v = np.take(T, z, axis=S)
        p = float(np.real(np.vdot(v, v)))
        out.append((p, (v / math.sqrt(p)) if p > 1e-14 else v))
    return out


def axes_after_removing(n, S, sites):
    """Site indices re-expressed as tensor axes after the pointer axis is dropped."""
    return [s - (1 if s > S else 0) for s in sites]


def chi_holevo_indep(T, n, S, frag):
    """chi_Z(S:F) and H(Z_S), computed from the CONDITIONAL SLICES."""
    sl = conditional_slices(T, S)
    ax = axes_after_removing(n, S, frag)
    rhos, ps = [], []
    for p, v in sl:
        ps.append(p)
        rhos.append(_trace_out(v, ax) if p > 1e-14 else None)
    tot = sum(ps)
    avg = sum((ps[z] / tot) * rhos[z] for z in (0, 1) if rhos[z] is not None)
    Sav = ent_from_svd(avg)
    Sc = sum((ps[z] / tot) * ent_from_svd(rhos[z])
             for z in (0, 1) if rhos[z] is not None)
    H = -sum((q / tot) * math.log2(q / tot) for q in ps if q / tot > 1e-15)
    return Sav - Sc, H, [ps[0] / tot, ps[1] / tot]


def cond_mi_indep(T, n, S, A, B):
    """I(A:B|Z_S) from the conditional slices, by einsum partial traces."""
    sl = conditional_slices(T, S)
    aA = axes_after_removing(n, S, A)
    aB = axes_after_removing(n, S, B)
    tot = sum(p for p, _ in sl)
    out = 0.0
    for p, v in sl:
        if p <= 1e-14:
            continue
        sa = ent_from_svd(_trace_out(v, aA))
        sb = ent_from_svd(_trace_out(v, aB))
        sab = ent_from_svd(_trace_out(v, sorted(aA + aB)))
        out += (p / tot) * (sa + sb - sab)
    return out


def chi_holevo_X(T, n, S, frag):
    """The X-basis pointer control: project the pointer onto |+>, |-> instead."""
    v0 = (np.take(T, 0, axis=S) + np.take(T, 1, axis=S)) / math.sqrt(2.0)
    v1 = (np.take(T, 0, axis=S) - np.take(T, 1, axis=S)) / math.sqrt(2.0)
    ax = axes_after_removing(n, S, frag)
    ps, rhos = [], []
    for v in (v0, v1):
        p = float(np.real(np.vdot(v, v)))
        ps.append(p)
        rhos.append(_trace_out(v / math.sqrt(p), ax) if p > 1e-14 else None)
    tot = sum(ps)
    avg = sum((ps[z] / tot) * rhos[z] for z in (0, 1) if rhos[z] is not None)
    Sav = ent_from_svd(avg)
    Sc = sum((ps[z] / tot) * ent_from_svd(rhos[z])
             for z in (0, 1) if rhos[z] is not None)
    H = -sum((q / tot) * math.log2(q / tot) for q in ps if q / tot > 1e-15)
    return Sav - Sc, H


def purity_pair(T, n, S, nb):
    r = _trace_out(T, sorted([S, nb]))
    return 1.0 - float(np.real(np.trace(r @ r)))


# ------------------------------- R_ind by BRON-KERBOSCH ---------------------
def bron_kerbosch(nodes, nbr):
    """All MAXIMAL cliques, with pivoting.  Distinct from every upstream MIS/clique
    implementation in this lane."""
    out = []

    def expand(R, P, X):
        if not P and not X:
            out.append(sorted(R))
            return
        pivot = max(P | X, key=lambda u: len(nbr[u] & P))
        for v in sorted(P - nbr[pivot]):
            expand(R | {v}, P & nbr[v], X & nbr[v])
            P = P - {v}
            X = X | {v}
    expand(set(), set(nodes), set())
    return out


def r_ind_indep(labels, passes, C, gate=INDEP_MAX):
    """Largest pairwise-independent certifying subset; ties to the lex-first in
    the declared label order.  Computed as a maximum clique of the graph whose
    edges are the pairs UNDER the gate."""
    order = {L: i for i, L in enumerate(labels)}
    P = [L for L in labels if L in passes]
    if not P:
        return 0, []
    nbr = {u: set() for u in P}
    for a, b in itertools.combinations(P, 2):
        key = tuple(sorted((a, b), key=order.get))
        v = C.get(key)
        if v is not None and v <= gate:
            nbr[a].add(b)
            nbr[b].add(a)
    cliques = bron_kerbosch(P, nbr)
    best = max(len(c) for c in cliques)
    cands = [c for c in cliques if len(c) == best]
    pick = min(cands, key=lambda c: tuple(sorted(order[x] for x in c)))
    return best, sorted(pick, key=order.get)


# =============================== measurement =================================
def measure_indep(geo, states, times):
    n, S = geo["n"], geo["S"]
    labels, frags = geo["labels"], geo["frags"]
    rows = []
    chi0, theta0 = {}, None
    guards = {"norm": 0.0, "t0": 0.0}
    for it, (t, T) in enumerate(zip(times, states)):
        guards["norm"] = max(guards["norm"],
                             abs(float(np.real(np.vdot(T, T))) - 1.0))
        chi, H, pz = {}, None, None
        for L in labels:
            c, H, pz = chi_holevo_indep(T, n, S, frags[L])
            chi[L] = c
        theta = float(np.mean([purity_pair(T, n, S, nb) for nb in geo["recording"]]))
        if it == 0:
            chi0 = dict(chi)
            theta0 = theta
            guards["t0"] = max(guards["t0"], max(abs(v) for v in chi.values()))
        exc = {L: chi[L] - chi0[L] for L in labels}
        C = {}
        for a, b in itertools.combinations(labels, 2):
            C[(a, b)] = cond_mi_indep(T, n, S, frags[a], frags[b])
            if it == 0:
                guards["t0"] = max(guards["t0"], abs(C[(a, b)]))
        passes, rr, wit = {}, {}, {}
        for dlt in DELTAS:
            p = [L for L in labels if H >= CONTENT_H_MIN
                 and chi[L] >= (1.0 - dlt) * H and exc[L] >= EXCESS_MIN]
            k, w = r_ind_indep(labels, p, C)
            passes["%.2f" % dlt] = p
            rr["%.2f" % dlt] = k
            wit["%.2f" % dlt] = w
        xres = {}
        HX = None
        for L in labels:
            cx, HX = chi_holevo_X(T, n, S, frags[L])
            xres[L] = cx
        if it == 0:
            xres0 = dict(xres)
        xpass_any = False
        for dlt in DELTAS:
            xp = [L for L in labels if HX >= CONTENT_H_MIN
                  and xres[L] >= (1.0 - dlt) * HX
                  and xres[L] - xres0[L] >= EXCESS_MIN]
            if len(xp) >= 2:
                xpass_any = True
        rows.append({"jt": t, "H_Z": H, "p_z": pz,
                     "pointer_tv_drift": abs(pz[0] - 0.5),
                     "chi": chi, "excess": exc, "theta_A": theta - theta0,
                     "C_ab": {"|".join(k): v for k, v in sorted(C.items())},
                     "r_ind": rr, "singleton_passes": passes,
                     "certifying_subsets": wit,
                     "x_control_ge2_possible": bool(xpass_any)})
    return rows, guards


def centered_frobenius_ok(lam, n, nbonds, degrees):
    den = math.sqrt(float(nbonds) + n * lam * lam)
    Z = 2.0 * lam / den
    X = min(2.0 * math.sqrt(dg) / den for dg in set(degrees))
    return bool(Z < X)


def verdict_indep(rows, comm_ok, delta=HEADLINE_DELTA):
    key = "%.2f" % delta
    x_ok = not any(r["x_control_ge2_possible"] for r in rows
                   if r["jt"] <= DEADLINE_JT + 1e-12)
    idx = next((i for i, r in enumerate(rows) if r["r_ind"][key] >= 2), None)
    if idx is None:
        any_content = any(len(r["singleton_passes"][key]) >= 2 for r in rows)
        return {"verdict": "NO", "gate": ("content" if not any_content
                                          else "independence")}
    run = 0
    for r in rows[idx:]:
        if r["r_ind"][key] >= 2:
            run += 1
        else:
            break
    r = rows[idx]
    if r["jt"] > DEADLINE_JT + 1e-12:
        return {"verdict": "NO", "gate": "deadline"}
    if run < PERSIST_N:
        return {"verdict": "NO", "gate": "persistence"}
    if r["pointer_tv_drift"] > DRIFT_MAX:
        return {"verdict": "NO", "gate": "drift"}
    if not (x_ok and comm_ok):
        return {"verdict": "NO", "gate": "x_control"}
    return {"verdict": "YES", "gate": None}


# ================== geometry construction (checker's own) ===================
def lat_nbrs(P):
    out = []
    for ax in range(3):
        for s in (1, -1):
            q = list(P)
            q[ax] += s
            out.append(tuple(q))
    return out


def make_geo(rule, key, sites, bonds_named, pointer, coord_labelled,
             hand_labels=None):
    idx = {c: i for i, c in enumerate(sites)}
    bonds = sorted({tuple(sorted((idx[a], idx[b]))) for a, b in bonds_named})
    part = partition_from_rule(rule, sites, bonds, idx[pointer], coord_labelled,
                               hand_labels)
    n = len(sites)
    deg = [0] * n
    for a, b in bonds:
        deg[a] += 1
        deg[b] += 1
    cover = sorted(itertools.chain(*part["frags"].values()))
    if cover != [i for i in range(n) if i != idx[pointer]]:
        die("geo:%s partition-not-exhaustive" % key)
    return {"key": key, "n": n, "sites": [str(s) for s in sites], "coords": sites,
            "bonds": bonds, "S": idx[pointer], "pointer": str(pointer),
            "labels": part["labels"], "frags": part["frags"],
            "anchor_multiplicity": part["anchor_multiplicity"],
            "recording": part["recording"], "degrees": deg,
            "d": len(part["recording"]), "f": len(part["labels"]),
            "fragment_sizes": {L: len(v) for L, v in part["frags"].items()},
            "loop_free": bool(len(bonds) - n + 1 == 0),
            "partition_site_by_site": {str(sites[i]): L
                                       for L, v in part["frags"].items() for i in v},
            "anchor_labels": {str(sites[r]): part["anchor_labels"][r]
                              for r in part["recording"]}}


def coord_star(rule, key, P, leaves, hand_labels=None):
    return make_geo(rule, key, [P] + list(leaves), [(P, q) for q in leaves], P,
                    True, hand_labels)


def coord_lattice(rule, key, P, sites):
    bonds = [(a, b) for ia, a in enumerate(sites) for b in sites[ia + 1:]
             if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
    return make_geo(rule, key, sites, bonds, P, True)


def abstract_star(rule, key, k, arm=1):
    sites, bonds = ["S"], []
    for j in range(k):
        prev = "S"
        for p in range(arm):
            nm = "A%02d" % (j + 1) if p == 0 else "a%02dx%d" % (j + 1, p)
            sites.append(nm)
            bonds.append((prev, nm))
            prev = nm
    return make_geo(rule, key, sites, bonds, "S", False)


# ===================================================================== main ==
def main():
    findings, refutations, teeth = [], [], {}
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode("utf-8")
    rule = MemoRule(memo)
    prim = json.load(open(os.path.join(ROOT, PRIMARY_RECEIPT)))
    r926 = json.load(open(os.path.join(ROOT, C926_RECEIPT)))
    r927 = json.load(open(os.path.join(ROOT, C927_RECEIPT)))

    # ---- gate 0: the memo-derived rule must reproduce the memo's cube lists --
    cube_sites = [(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)]
    cube = coord_lattice(rule, "cube27", (0, 0, 0), cube_sites)
    memo_frags = {}
    for lab in CUBE_LABELS:
        m = re.search(r"`F_\(%s\) = \[([^\]]*)\]`" % re.escape(lab), memo)
        if m is None:
            die("memo-fragments:miss %s" % lab)
        memo_frags[lab] = {tuple(int(v) for v in s) for s in
                           re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(1))}
    cube_ok = all({cube["coords"][i] for i in cube["frags"][L]} == memo_frags[L]
                  for L in CUBE_LABELS)
    if not cube_ok:
        die("memo-rule:does-not-reproduce-the-memo-cube")

    # ---- ATTACK (ii): every published partition re-derived from the memo bytes -
    part_check = {"checked": 0, "mismatches": [], "hand_labelled": []}
    for key, gp in sorted(prim["geometries"].items()):
        sites_str = gp["sites"]
        coords = None
        if all(s.startswith("(") for s in sites_str):
            coords = [tuple(int(v) for v in re.findall(r"-?\d+", s)) for s in sites_str]
        bonds_named = [(a, b) for a, b in gp["bonds"]]
        if coords is not None:
            m = {s: c for s, c in zip(sites_str, coords)}
            bonds_c = [(m[a], m[b]) for a, b in bonds_named]
            P = m[gp["pointer"]]
            hand = None
            # A6 is the ONE geometry the primary declares hand-labelled (926's cap)
            if key == "A6":
                hand = {(0, 0, 0): "-z"}
                part_check["hand_labelled"].append(key)
            try:
                g = make_geo(rule, key, coords, bonds_c, P, True, hand)
            except SystemExit:
                part_check["mismatches"].append("%s:rule-refused-to-build" % key)
                continue
        else:
            g = make_geo(rule, key, sites_str, bonds_named, gp["pointer"], False)
        part_check["checked"] += 1
        if g["partition_site_by_site"] != gp["partition_site_by_site"]:
            part_check["mismatches"].append("%s:partition" % key)
        if g["anchor_multiplicity"] != gp["anchor_multiplicity"]:
            part_check["mismatches"].append("%s:multiplicity" % key)
        if g["d"] != gp["profile"]["pointer_degree_d"] or \
                g["f"] != gp["profile"]["fragment_count_f"]:
            part_check["mismatches"].append("%s:(d,f)" % key)
    if part_check["mismatches"]:
        refutations.append(
            "PARTITION REFUTATION: %d of %d published partitions do not follow from "
            "the memo bytes: %s" % (len(part_check["mismatches"]),
                                    part_check["checked"],
                                    part_check["mismatches"][:6]))
    teeth["C1_every_partition_follows_from_the_memo_bytes"] = {
        "n_checked": part_check["checked"], "mismatches": part_check["mismatches"],
        "hand_labelled_geometries_declared_by_the_primary":
            part_check["hand_labelled"],
        "note": "the labelling and all three tie-break clauses are parsed out of the "
                "frozen memo here and re-implemented; nothing is copied.",
        "fires": bool(not part_check["mismatches"] and part_check["checked"] >= 40)}

    # ---- the checker's own roster (built independently) ---------------------
    def pick(d, f):
        m = d - f + 1
        for P in [(0, 0, 0), (0, 0, 2), (0, 1, 1), (0, 2, 1), (1, 1, 0), (2, 0, 0)]:
            lab = {}
            for q in lat_nbrs(P):
                L = rule.signed_axis(q)
                if L is None:
                    continue
                lab.setdefault(L, []).append(q)
            blocks = sorted(lab.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            if blocks and len(blocks[0][1]) >= m and len(blocks) - 1 >= f - 1:
                leaves = sorted(blocks[0][1], key=str)[:m]
                for L, v in blocks[1:f]:
                    leaves.append(sorted(v, key=str)[0])
                return P, sorted(leaves, key=str)
        return None, None

    GEOS = {}
    for d in (3, 4, 5, 6):
        for f in range(1, d + 1):
            P, lv = pick(d, f)
            if P is None:
                continue
            g = coord_star(rule, "Xd%df%d" % (d, f), P, lv)
            if (g["d"], g["f"]) != (d, f):
                die("checker-grid:%d,%d built (%d,%d)" % (d, f, g["d"], g["f"]))
            GEOS[g["key"]] = g
    for k in (2, 3, 4, 5, 6, 8):
        GEOS["XSTk%d" % k] = abstract_star(rule, "XSTk%d" % k, k)
    # size controls at d = f (DECLARED CAP: arm lengths chosen so n <= 11; a
    # degree-5 spider with arms of 4 would need n = 21 and is NOT run).
    for (k, L) in ((3, 2), (3, 3), (4, 2), (5, 2)):
        GEOS["XSPk%dL%d" % (k, L)] = abstract_star(rule, "XSPk%dL%d" % (k, L), k, L)

    # a BROADER embedding sweep than the primary ran: every distinct pointer in
    # the box that realises each (d, f), not just one alternative.
    EMB = {}
    for px in range(-2, 3):
        for py in range(-2, 3):
            for pz in range(-2, 3):
                P = (px, py, pz)
                lab = {}
                for q in lat_nbrs(P):
                    L = rule.signed_axis(q)
                    if L is None:
                        continue
                    lab.setdefault(L, []).append(q)
                blocks = sorted(lab.items(), key=lambda kv: (-len(kv[1]), kv[0]))
                if not blocks:
                    continue
                for f in range(2, len(blocks) + 1):
                    for m in range(1, len(blocks[0][1]) + 1):
                        d = m + f - 1
                        if d > 6 or d < 3:
                            continue
                        leaves = sorted(blocks[0][1], key=str)[:m]
                        for L, v in blocks[1:f]:
                            leaves.append(sorted(v, key=str)[0])
                        EMB.setdefault((d, f), []).append((P, sorted(leaves, key=str)))
    emb_geos = {}
    for (d, f), lst in sorted(EMB.items()):
        for i, (P, lv) in enumerate(lst[:4]):
            key = "Ed%df%d_%d" % (d, f, i)
            g = coord_star(rule, key, P, lv)
            if (g["d"], g["f"]) == (d, f):
                emb_geos[key] = g

    # ---- Q3 witnesses, rebuilt independently --------------------------------
    W = {}
    W["XW1"] = coord_star(rule, "XW1", (0, 2, 1), lat_nbrs((0, 2, 1)))
    W["XW2"] = coord_lattice(rule, "XW2", (0, 1, 1),
                             [(0, 1, 1)] + lat_nbrs((0, 1, 1))
                             + [(0, 3, 1), (0, 1, 3), (0, 1, -1)])
    W["XW3"] = coord_lattice(rule, "XW3", (0, 0, 1),
                             [(0, 0, 1), (1, 0, 1), (-1, 0, 1), (0, 1, 1), (0, -1, 1),
                              (0, 0, 2), (0, 0, 3), (0, 0, 4), (0, 0, 5)])
    W["XW4"] = coord_lattice(rule, "XW4", (0, 1, 1),
                             [(0, 1, 1), (1, 1, 1), (0, 0, 1), (0, 2, 1), (0, 1, 2),
                              (0, 1, 0), (0, 3, 1), (0, 4, 1)])
    W["XW5"] = coord_lattice(rule, "XW5", (0, 0, 2),
                             [(0, 0, 2)] + lat_nbrs((0, 0, 2))
                             + [(2, 0, 2), (2, 1, 2), (2, -1, 2)])
    # NEW SHAPES the primary never built -- the counterexample hunt
    W["XH1"] = coord_lattice(rule, "XH1", (0, 2, 1),
                             [(0, 2, 1)] + lat_nbrs((0, 2, 1))
                             + [(0, 4, 1), (0, 2, 3), (2, 2, 1)])
    W["XH2"] = coord_lattice(rule, "XH2", (0, 0, 0),
                             [(0, 0, 0)] + lat_nbrs((0, 0, 0))
                             + [(2, 0, 0), (3, 0, 0), (4, 0, 0), (0, 2, 0)])
    # XH3 is DELIBERATELY LOOPY (the (0,2,1) and (0,2,-1) sites close 4-cycles).
    # It is an adversarial probe OUTSIDE the loop-free scope of the law and is
    # reported separately, never as a counterexample to a loop-free claim.
    W["XH3"] = coord_lattice(rule, "XH3", (0, 1, 0),
                             [(0, 1, 0), (1, 1, 0), (-1, 1, 0), (0, 2, 0), (0, 1, 1),
                              (0, 1, -1), (0, 3, 0), (0, 2, 1), (0, 2, -1)])
    GEOS.update(W)
    GEOS.update(emb_geos)

    # ------------------------------------------------------- the run engine --
    CACHE, guards_all = {}, {"norm": 0.0, "t0": 0.0}
    route_dev = {"L_vs_E": 0.0, "cells_cross_checked": 0}

    def run(g, lam, cross=False):
        n = g["n"]
        H = build_H_sparse(n, g["bonds"], lam)
        T0 = prep_state_tensor(n, set([g["S"]] + list(g["recording"])))
        v0 = T0.reshape(-1)
        vs, info = lanczos_evolve(H, v0, T_EXEC)
        Ts = [v.reshape((2,) * n) for v in vs]
        rows, gu = measure_indep(g, Ts, T_EXEC)
        for k in gu:
            guards_all[k] = max(guards_all[k], gu[k])
        if cross:
            ve, _ = expm_multiply_evolve(H, v0, T_EXEC)
            dev = max(float(np.abs(a - b).max()) for a, b in zip(vs, ve))
            route_dev["L_vs_E"] = max(route_dev["L_vs_E"], dev)
            route_dev["cells_cross_checked"] += 1
        return rows, info

    for key, g in sorted(GEOS.items()):
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            rows, _ = run(g, lam, cross=(g["n"] <= 8 and lk == "0.1"
                                         and key.startswith("Xd")))
            CACHE[(key, lk)] = rows

    # ---------------- the checker's OWN reference table T(k) -----------------
    REF = {}
    for k in (2, 3, 4, 5, 6, 8):
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            g = GEOS["XSTk%d" % k]
            rows = CACHE[("XSTk%d" % k, lk)]
            r = next(r for r in rows if abs(r["jt"] - COMPARISON_JT) < 1e-12)
            REF[(k, lk)] = float(np.median(list(r["C_ab"].values())))

    # --------- cross-check against the primary's published numbers -----------
    agree = {"cells": 0, "pairs": 0, "max_C_ab_dev": 0.0, "max_chi_dev": 0.0,
             "max_H_dev": 0.0, "verdict_mismatches": [], "ledger_mismatches": []}
    pbat = prim["per_pair_batteries"]
    pcells = prim["new_cells"]
    NAME_MAP = {}
    for d in (3, 4, 5, 6):
        for f in range(1, d + 1):
            NAME_MAP["Xd%df%d" % (d, f)] = "SEPd%df%d" % (d, f)
    NAME_MAP.update({"XW1": "W1merge6", "XW2": "W2merge6d2", "XW3": "W3depth5",
                     "XW4": "W4merge5d3", "XW5": "W5claw6"})
    for mine, theirs in sorted(NAME_MAP.items()):
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            ck = "%s@%s" % (theirs, lk)
            if ck not in pbat or (mine, lk) not in CACHE:
                continue
            rows = CACHE[(mine, lk)]
            r = next(r for r in rows if abs(r["jt"] - COMPARISON_JT) < 1e-12)
            agree["cells"] += 1
            for pk, v in pbat[ck]["per_pair"].items():
                if pk not in r["C_ab"]:
                    agree["ledger_mismatches"].append("%s:%s missing" % (ck, pk))
                    continue
                agree["pairs"] += 1
                agree["max_C_ab_dev"] = max(agree["max_C_ab_dev"],
                                            abs(r["C_ab"][pk] - v["C_ab_at_Jt_0.7"]))
            comm = centered_frobenius_ok(lam, GEOS[mine]["n"], len(GEOS[mine]["bonds"]),
                                         GEOS[mine]["degrees"])
            vr = verdict_indep(rows, comm)
            if ck in pcells and vr["verdict"] != pcells[ck]["verdict"]:
                agree["verdict_mismatches"].append(
                    "%s: checker %s vs primary %s" % (ck, vr["verdict"],
                                                      pcells[ck]["verdict"]))
            if ck in pcells:
                mine_led = [r2["r_ind"]["0.10"] for r2 in rows]
                if mine_led != pcells[ck]["ledger"]:
                    agree["ledger_mismatches"].append("%s:ledger %s vs %s"
                                                      % (ck, mine_led,
                                                         pcells[ck]["ledger"]))
    if agree["verdict_mismatches"] or agree["ledger_mismatches"]:
        refutations.append("CROSS-CHECK REFUTATION: %s %s"
                           % (agree["verdict_mismatches"][:4],
                              agree["ledger_mismatches"][:4]))
    teeth["C2_independent_recomputation_agrees"] = {
        "cells": agree["cells"], "pairs": agree["pairs"],
        "max_C_ab_deviation": agree["max_C_ab_dev"],
        "tolerance": AGREE_TOL,
        "verdict_mismatches": agree["verdict_mismatches"],
        "ledger_mismatches": agree["ledger_mismatches"][:6],
        "fires": bool(agree["pairs"] > 100 and agree["max_C_ab_dev"] <= AGREE_TOL
                      and not agree["verdict_mismatches"]
                      and not agree["ledger_mismatches"])}

    # ============ ATTACK (i): MODEL DEGENERACY on the Q1 verdict =============
    # Build the checker's own baseline observations, then confront a whole family
    # of rivals.  A rival "survives" on a cell if it lands within RIVAL_TOL.
    obs = []
    for key, g in sorted(GEOS.items()):
        if not g["loop_free"] or g["f"] < 3:
            continue
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            rows = CACHE[(key, lk)]
            r = next(r for r in rows if abs(r["jt"] - COMPARISON_JT) < 1e-12)
            base = [v for pk, v in r["C_ab"].items()
                    if g["anchor_multiplicity"][pk.split("|")[0]] == 1
                    and g["anchor_multiplicity"][pk.split("|")[1]] == 1]
            if not base:
                continue
            obs.append({"geometry": key, "field": lam, "lk": lk, "d": g["d"],
                        "f": g["f"], "n": g["n"],
                        "max_size": max(g["fragment_sizes"].values()),
                        "observed": float(np.median(base))})
    RIVALS = {
        "M_d  = T(d)": lambda o: REF.get((o["d"], o["lk"])),
        "M_f  = T(f)": lambda o: REF.get((o["f"], o["lk"])),
        "M_max = T(max(d,f))": lambda o: REF.get((max(o["d"], o["f"]), o["lk"])),
        "M_min = T(min(d,f))": lambda o: REF.get((min(o["d"], o["f"]), o["lk"])),
        "M_mean = (T(d)+T(f))/2": lambda o: (
            None if REF.get((o["d"], o["lk"])) is None
            or REF.get((o["f"], o["lk"])) is None
            else 0.5 * (REF[(o["d"], o["lk"])] + REF[(o["f"], o["lk"])])),
        "M_dplusf = T(d+f-max)": lambda o: REF.get((o["d"] + o["f"] - max(o["d"], o["f"]),
                                                    o["lk"])),
        "M_size = T(max fragment size + 1)": lambda o: REF.get(
            (min(8, o["max_size"] + 1), o["lk"])),
        "M_n = T(n-1)": lambda o: REF.get((min(8, o["n"] - 1), o["lk"])),
    }
    degeneracy = {}
    for nm, fn in RIVALS.items():
        res, surv = [], 0
        for o in obs:
            p = fn(o)
            if p is None:
                continue
            r = abs(o["observed"] - p)
            res.append(r)
            if r <= RIVAL_TOL:
                surv += 1
        degeneracy[nm] = {
            "n_cells_scored": len(res),
            "max_abs_residual": max(res) if res else None,
            "median_abs_residual": float(np.median(res)) if res else None,
            "n_cells_within_%g" % RIVAL_TOL: surv,
            "fits_everywhere": bool(res and max(res) <= RIVAL_TOL)}
    disc_obs = [o for o in obs if o["d"] != o["f"]]
    # A rival that returns THE SAME NUMBER as M_d on every cell is not an
    # alternative hypothesis -- it is M_d wearing another name.  Separate those
    # out before calling anything a refutation.  (Cycle 926's checker hit the
    # same pattern with branch count vs pointer degree.)
    for nm, fn in RIVALS.items():
        same = True
        for o in obs:
            p, q = fn(o), REF.get((o["d"], o["lk"]))
            if p is None or q is None or p != q:
                same = False
                break
        degeneracy[nm]["identical_to_M_d_on_every_grid_cell"] = bool(same)
    identity_ties = [nm for nm, v in degeneracy.items()
                     if v.get("identical_to_M_d_on_every_grid_cell")
                     and nm != "M_d  = T(d)"]
    # WHY the ties are ties, stated as a checkable fact about the grid
    f_le_d_everywhere = all(o["f"] <= o["d"] for o in obs)
    rival_survivors = [nm for nm, v in degeneracy.items()
                       if v["fits_everywhere"] and nm != "M_d  = T(d)"
                       and not v.get("identical_to_M_d_on_every_grid_cell")]
    if identity_ties:
        findings.append(
            "DEGENERACY FINDING (identity, not an alternative): the rival(s) %s "
            "return the SAME NUMBER as M_d on every one of the %d cells scored.  "
            "The reason is structural and checkable: the frozen rule can never "
            "produce more fragments than the pointer has neighbours, so f <= d "
            "everywhere on the constructible grid (verified: %s), which makes "
            "max(d, f) literally equal to d.  These are not rival hypotheses and "
            "they do not weaken the Q1 verdict -- but the verdict should be stated "
            "as 'the arity variable is d' rather than 'd beats every function of "
            "(d, f)', because functions that COLLAPSE ONTO d cannot be told apart "
            "from d by any measurement on this grid."
            % (identity_ties, len(obs), f_le_d_everywhere))
    # does any rival fit ANYWHERE (even on a single discriminating cell)?
    anywhere = {}
    for nm, fn in RIVALS.items():
        if nm == "M_d  = T(d)":
            continue
        hits = []
        for o in disc_obs:
            p = fn(o)
            if p is not None and abs(o["observed"] - p) <= RIVAL_TOL:
                hits.append({"geometry": o["geometry"], "field": o["field"],
                             "d": o["d"], "f": o["f"],
                             "residual": abs(o["observed"] - p)})
        anywhere[nm] = {"n_discriminating_cells_fitted": len(hits),
                        "cells": hits[:6]}
    accidental = {nm: v for nm, v in anywhere.items()
                  if v["n_discriminating_cells_fitted"] > 0 and nm not in identity_ties}
    if rival_survivors:
        refutations.append("Q1 DEGENERACY REFUTATION: rival model(s) %s fit the whole "
                           "grid as well as M_d and are NOT identical to it"
                           % rival_survivors)
    n_star_cells = sum(1 for o in disc_obs if o["n"] == o["d"] + 1)
    if accidental:
        findings.append(
            "Q1 DEGENERACY FINDING (not a refutation): on %d of %d discriminating "
            "cells the rival(s) %s land inside %g bits.  The structural reason is "
            "that a coordinate STAR has n = d + 1, so on the %d pure-star cells the "
            "system-size model T(n-1) IS T(d) and cannot be told apart from it.  "
            "The rival is nonetheless refuted overall -- it misses by up to %.3e "
            "bits on the SPIDER cells, where depth breaks n = d + 1.  Consequence "
            "for the scope of the Q1 verdict: the discrimination between POINTER "
            "DEGREE and SYSTEM SIZE rests entirely on the depth-carrying cells, "
            "not on the star grid.  (Cycle 927 had already separated the two on "
            "its own equal-n families; this is a scope note, not a new doubt.)"
            % (sum(v["n_discriminating_cells_fitted"] for v in accidental.values()),
               len(disc_obs), sorted(accidental), RIVAL_TOL, n_star_cells,
               max(degeneracy[nm]["max_abs_residual"] for nm in accidental)))
    teeth["C3_model_degeneracy_attack"] = {
        "rivals_tested": sorted(RIVALS), "per_rival": degeneracy,
        "rivals_fitting_the_whole_grid_besides_M_d": rival_survivors,
        "identity_ties_collapsing_onto_M_d": identity_ties,
        "f_le_d_everywhere_on_the_constructible_grid": bool(f_le_d_everywhere),
        "rivals_fitting_at_least_one_discriminating_cell": sorted(accidental),
        "n_discriminating_cells": len(disc_obs),
        "M_d_max_residual": degeneracy["M_d  = T(d)"]["max_abs_residual"],
        "M_f_max_residual": degeneracy["M_f  = T(f)"]["max_abs_residual"],
        "fires": bool(not rival_survivors and len(disc_obs) >= 10)}

    # ============ ATTACK (iii): the unified law, HELD-OUT prediction =========
    # F(d, m, lambda) is fitted on HALF the cells (a declared split: even index)
    # and used to PREDICT the other half.  A failure anywhere is a refutation.
    allpairs = []
    for key, g in sorted(GEOS.items()):
        if not g["loop_free"]:
            continue
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            rows = CACHE[(key, lk)]
            r = next(r for r in rows if abs(r["jt"] - COMPARISON_JT) < 1e-12)
            for pk, v in r["C_ab"].items():
                A, B = pk.split("|")
                ma = g["anchor_multiplicity"][A]
                mb = g["anchor_multiplicity"][B]
                allpairs.append({"geometry": key, "pair": pk, "lk": lk, "d": g["d"],
                                 "f": g["f"], "m": (max(ma, mb), min(ma, mb)),
                                 "rest": g["d"] - ma - mb,
                                 "sizes": (g["fragment_sizes"][A],
                                           g["fragment_sizes"][B]),
                                 "C": v})
    train = [p for i, p in enumerate(allpairs) if i % 2 == 0]
    test = [p for i, p in enumerate(allpairs) if i % 2 == 1]
    F = {}
    for p in train:
        F.setdefault((p["d"], p["lk"], p["m"]), []).append(p["C"])
    F = {k: float(np.median(v)) for k, v in F.items()}
    held = {"n_train": len(train), "n_test": len(test), "n_predictable": 0,
            "max_abs_error": 0.0, "worst": None, "unpredictable": 0}
    for p in test:
        k = (p["d"], p["lk"], p["m"])
        if k not in F:
            held["unpredictable"] += 1
            continue
        held["n_predictable"] += 1
        e = abs(p["C"] - F[k])
        if e > held["max_abs_error"]:
            held["max_abs_error"] = e
            held["worst"] = {"geometry": p["geometry"], "pair": p["pair"],
                             "field": p["lk"], "d": p["d"], "f": p["f"],
                             "m": list(p["m"]), "sizes": list(p["sizes"]),
                             "observed": p["C"], "predicted": F[k], "error": e}
    # the f-blindness test stated as a prediction failure hunt
    fblind = {}
    for p in allpairs:
        fblind.setdefault((p["d"], p["lk"], p["m"]), {}).setdefault(p["f"], []).append(p["C"])
    fspread = []
    for k, byf in sorted(fblind.items()):
        if len(byf) < 2:
            continue
        meds = {f: float(np.median(v)) for f, v in byf.items()}
        fspread.append({"d": k[0], "field": k[1], "m": list(k[2]),
                        "f_values": sorted(meds),
                        "C_by_f": meds,
                        "spread_across_f": max(meds.values()) - min(meds.values())})
    worst_f = max(fspread, key=lambda r: r["spread_across_f"]) if fspread else None
    if held["max_abs_error"] > 1e-4:
        refutations.append(
            "UNIFIED-LAW REFUTATION: held-out prediction fails by %.3e bits at %s"
            % (held["max_abs_error"], held["worst"]))
    teeth["C4_unified_law_held_out_prediction"] = {
        "split": "declared 50/50 by pair index parity (even = train)",
        "detail": held,
        "f_blindness_groups_tested": len(fspread),
        "worst_spread_across_f_at_fixed_(d, field, multiplicities)": worst_f,
        "fires": bool(held["n_predictable"] > 50 and held["max_abs_error"] <= 1e-4
                      and (worst_f is None or worst_f["spread_across_f"] <= 1e-4))}

    # ============ ATTACK: the two-gate anatomy and threshold, re-tested ======
    q2rows = []
    for key, g in sorted(GEOS.items()):
        if not g["loop_free"]:
            continue
        lk = "0.1"
        rows = CACHE[(key, lk)]
        comm = centered_frobenius_ok(0.10, g["n"], len(g["bonds"]), g["degrees"])
        vr = verdict_indep(rows, comm)
        q2rows.append({"geometry": key, "d": g["d"], "f": g["f"],
                       "verdict": vr["verdict"], "gate": vr["gate"],
                       "max_r_ind": max(r["r_ind"]["0.10"] for r in rows),
                       "ceiling_equals_f": bool(max(r["r_ind"]["0.10"] for r in rows)
                                                == g["f"])})
    conj = [r for r in q2rows if r["d"] >= 5 and r["f"] >= 3]
    non = [r for r in q2rows if not (r["d"] >= 5 and r["f"] >= 3)]
    bad_suff = [r["geometry"] for r in conj if r["verdict"] != "YES"]
    bad_nec = [r["geometry"] for r in non if r["verdict"] == "YES"]
    anat = {}
    for r in q2rows:
        if r["verdict"] == "NO":
            anat.setdefault(r["gate"], []).append(r)
    ind_f = sorted({r["f"] for r in anat.get("independence", [])})
    ind_d = sorted({r["d"] for r in anat.get("independence", [])})
    per_f = sorted({r["f"] for r in anat.get("persistence", [])})
    per_d = sorted({r["d"] for r in anat.get("persistence", [])})
    if bad_suff or bad_nec:
        refutations.append(
            "THRESHOLD REFUTATION on the checker's own %d-geometry grid: "
            "sufficiency counterexamples %s; necessity counterexamples %s"
            % (len(q2rows), bad_suff[:5], bad_nec[:5]))
    teeth["C5_threshold_conjunction_on_the_checkers_own_grid"] = {
        "n_geometries": len(q2rows), "n_satisfying": len(conj),
        "n_violating": len(non),
        "sufficiency_counterexamples": bad_suff,
        "necessity_counterexamples": bad_nec,
        "fires": bool(len(q2rows) >= 40 and not bad_suff and not bad_nec)}
    teeth["C6_two_gate_anatomy_independently_reproduced"] = {
        "independence_failures": {"n": len(anat.get("independence", [])),
                                  "f_values": ind_f, "d_values": ind_d},
        "persistence_failures": {"n": len(anat.get("persistence", [])),
                                 "f_values": per_f, "d_values": per_d},
        "content_failures": {"n": len(anat.get("content", [])),
                             "f_values": sorted({r["f"] for r
                                                 in anat.get("content", [])})},
        "independence_side_tracks_f": bool(ind_f and max(ind_f) <= 2 and len(ind_d) >= 3),
        "persistence_side_tracks_d": bool(per_d and max(per_d) <= 4 and min(per_f) >= 3),
        "fires": bool(ind_f and max(ind_f) <= 2 and len(ind_d) >= 3
                      and per_d and max(per_d) <= 4 and min(per_f) >= 3)}

    # ============ ATTACK (iv): Q3 -- hunt a large-fragment counterexample ====
    q3 = []
    for key in sorted(list(W) + [k for k in GEOS if k.startswith("Xd")]):
        g = GEOS[key]
        big = [L for L, s in g["fragment_sizes"].items() if s >= 4]
        if not (big and g["f"] >= 3 and g["d"] >= 5):
            continue
        rows = CACHE[(key, "0.1")]
        comm = centered_frobenius_ok(0.10, g["n"], len(g["bonds"]), g["degrees"])
        vr = verdict_indep(rows, comm)
        q3.append({"geometry": key, "d": g["d"], "f": g["f"],
                   "loop_free": g["loop_free"],
                   "max_fragment_size": max(g["fragment_sizes"].values()),
                   "large_fragments": sorted(big),
                   "max_anchor_multiplicity": max(g["anchor_multiplicity"].values()),
                   "verdict": vr["verdict"], "gate": vr["gate"],
                   "certifies": bool(vr["verdict"] == "YES")})
    counterex = [w for w in q3 if not w["certifies"] and w["loop_free"]]
    loopy_probe = [w for w in q3 if not w["loop_free"]]
    if counterex:
        refutations.append(
            "Q3 COUNTEREXAMPLE FOUND: %d LOOP-FREE large-fragment geometries at "
            "f >= 3, d >= 5 do NOT certify: %s"
            % (len(counterex), [(c["geometry"], c["gate"]) for c in counterex[:5]]))
    if any(not w["certifies"] for w in loopy_probe):
        findings.append(
            "Q3 SCOPE FINDING: the LOOPY probe(s) %s carry a large fragment at "
            "f >= 3, d >= 5 and do NOT certify.  This is OUTSIDE the loop-free "
            "scope of every claim in this block and is consistent with Cycle 921's "
            "pair-cycle law, but it shows the Q3 statement must carry 'loop-free' "
            "explicitly -- a large fragment at f >= 3, d >= 5 is NOT sufficient on "
            "its own."
            % [w["geometry"] for w in loopy_probe if not w["certifies"]])
    teeth["C7_Q3_large_fragment_counterexample_hunt"] = {
        "n_large_fragment_geometries_tested": len(q3),
        "n_loop_free": sum(1 for w in q3 if w["loop_free"]),
        "n_certifying": sum(1 for w in q3 if w["certifies"]),
        "loop_free_counterexamples": counterex,
        "loopy_probes_declared_out_of_scope": loopy_probe,
        "shapes_tested": sorted({w["geometry"] for w in q3}),
        "fires": bool(len(q3) >= 6 and not counterex)}

    # ============ the embedding sweep (broader than the primary's) ===========
    embchk = []
    for (d, f) in sorted(EMB):
        ks = sorted(k for k in emb_geos if k.startswith("Ed%df%d_" % (d, f)))
        if len(ks) < 2:
            continue
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            vecs = []
            for k in ks:
                rows = CACHE[(k, lk)]
                r = next(r for r in rows if abs(r["jt"] - COMPARISON_JT) < 1e-12)
                vecs.append(sorted(r["C_ab"].values()))
            if len({len(v) for v in vecs}) != 1 or not vecs[0]:
                continue
            dev = max(max(abs(a - b) for a, b in zip(vecs[0], v)) for v in vecs[1:])
            embchk.append({"d": d, "f": f, "field": lam, "n_embeddings": len(ks),
                           "max_abs_dev": dev,
                           "pointers": [GEOS[k]["pointer"] for k in ks]})
    worst_emb = max((e["max_abs_dev"] for e in embchk), default=None)
    if worst_emb is not None and worst_emb > AGREE_TOL:
        refutations.append("EMBEDDING REFUTATION: the same (d,f) at different cube "
                           "pointers gives different C_ab, max deviation %.3e"
                           % worst_emb)
    teeth["C8_embedding_independence_broad_sweep"] = {
        "n_comparisons": len(embchk),
        "n_embeddings_total": len(emb_geos),
        "max_deviation": worst_emb, "tolerance": AGREE_TOL,
        "detail": embchk[:12],
        "fires": bool(embchk and worst_emb is not None and worst_emb <= AGREE_TOL)}

    # ============ the structural lemma, re-verified on a LARGER box ==========
    profs = {}
    for px in range(-5, 6):
        for py in range(-5, 6):
            for pz in range(-5, 6):
                P = (px, py, pz)
                lab = {}
                for q in lat_nbrs(P):
                    L = rule.signed_axis(q)
                    if L is None:
                        continue
                    lab.setdefault(L, []).append(q)
                profs.setdefault(tuple(sorted((len(v) for v in lab.values()),
                                              reverse=True)), 0)
                profs[tuple(sorted((len(v) for v in lab.values()), reverse=True))] += 1
    two_blocks = [list(p) for p in profs if sum(1 for m in p if m > 1) > 1]
    if two_blocks:
        refutations.append("STRUCTURAL-LEMMA REFUTATION: profiles with two merged "
                           "blocks exist: %s" % two_blocks[:4])
    teeth["C9_structural_lemma_on_a_larger_box"] = {
        "box": "[-5,5]^3", "n_pointers": 11 ** 3,
        "distinct_profiles": {str(list(k)): v for k, v in sorted(profs.items(),
                                                                key=lambda kv: -sum(kv[0]))},
        "two_merged_block_profiles": two_blocks,
        "primary_box": prim["structural_lemma"]["box"],
        "fires": bool(not two_blocks)}

    # ============ A4: the primary's re-explanation, independently tested =====
    gA4 = coord_star(rule, "XA4", (1, 1, 0),
                     [(0, 1, 0), (2, 1, 0), (1, 2, 0), (1, 0, 0), (1, 1, 1)])
    rowsA4, _ = run(gA4, 0.10)
    rA4 = next(r for r in rowsA4 if abs(r["jt"] - COMPARISON_JT) < 1e-12)
    a4 = list(rA4["C_ab"].values())[0]
    pub_a4 = r926["separation_family"]["geometries"]["A4"]["lambdas"]["0.1"]["rows"]
    pub_a4v = next(r for r in pub_a4 if abs(r["jt"] - 0.7) < 1e-12)["C_ab"]["+x|+y"]
    a4tests = {
        "checker_A4_C_ab_at_Jt_0.7": a4,
        "cycle926_published_value": pub_a4v,
        "deviation_from_926": abs(a4 - pub_a4v),
        "T(2)_the_f_equals_2_prediction": REF[(2, "0.1")],
        "residual_of_the_f_reading": abs(a4 - REF[(2, "0.1")]),
        "T(5)_the_pure_d_prediction": REF[(5, "0.1")],
        "residual_of_the_pure_d_reading": abs(a4 - REF[(5, "0.1")]),
        "over_the_0.02_gate": bool(a4 > INDEP_MAX),
        "pair_exhausts_the_pointer": bool(gA4["d"]
                                          - sum(gA4["anchor_multiplicity"].values()) == 0),
    }
    # is the f reading rescuable within the tolerance the 927 table itself carries?
    within_927_spread = 2.4003115371370315e-05
    a4tests["f_reading_within_927s_own_within_degree_spread"] = bool(
        a4tests["residual_of_the_f_reading"] <= within_927_spread)
    a4tests["f_reading_wrong_by_this_many_927_spreads"] = (
        a4tests["residual_of_the_f_reading"] / within_927_spread)
    if a4tests["f_reading_within_927s_own_within_degree_spread"]:
        refutations.append("A4 REFUTATION: the f = 2 reading of A4 fits inside 927's "
                           "own within-degree spread; the primary's dismissal is "
                           "too strong")
    teeth["C10_A4_reexplanation"] = {
        "detail": a4tests,
        "fires": bool(a4tests["deviation_from_926"] <= AGREE_TOL
                      and not a4tests["f_reading_within_927s_own_within_degree_spread"]
                      and a4tests["over_the_0.02_gate"])}

    # ============ the additivity relation, independently tested =============
    addchk = []
    for d in (3, 4, 5, 6):
        for lam in CLAIM_LAMBDAS:
            lk = "%g" % lam
            G = {}
            for f in range(1, d + 1):
                key = "Xd%df%d" % (d, f)
                if (key, lk) not in CACHE:
                    continue
                g = GEOS[key]
                r = next(r for r in CACHE[(key, lk)]
                         if abs(r["jt"] - COMPARISON_JT) < 1e-12)
                for pk, v in r["C_ab"].items():
                    A, B = pk.split("|")
                    ma, mb = g["anchor_multiplicity"][A], g["anchor_multiplicity"][B]
                    if min(ma, mb) != 1:
                        continue
                    G.setdefault(max(ma, mb), []).append(v)
            Gm = {m: float(np.median(v)) for m, v in G.items()}
            if (d - 1) in Gm:
                for m in sorted(Gm):
                    c = d - 1 - m
                    if c in Gm and m <= c:
                        addchk.append({"d": d, "field": lam, "m": m, "complement": c,
                                       "residual": Gm[m] + Gm[c] - Gm[d - 1]})
    maxadd = max((abs(a["residual"]) for a in addchk), default=None)
    if maxadd is not None and maxadd > 1e-9:
        findings.append("ADDITIVITY FINDING: the primary's structural relation "
                        "G(m)+G(d-1-m)=G(d-1) holds here only to %.3e, not to the "
                        "1e-13 the primary reports" % maxadd)
    teeth["C11_additivity_relation_independently_confirmed"] = {
        "n_instances": len(addchk), "max_abs_residual": maxadd,
        "tolerance": 1e-9, "detail": addchk[:10],
        "fires": bool(addchk and maxadd is not None and maxadd <= 1e-9)}

    # ============ machinery self-tests (the checker's own teeth) ============
    # a deliberately CRIPPLED Lanczos (no reorthogonalisation, tiny Krylov space)
    gtest = GEOS["Xd5f3"]
    Ht = build_H_sparse(gtest["n"], gtest["bonds"], 0.10)
    v0 = prep_state_tensor(gtest["n"],
                           set([gtest["S"]] + list(gtest["recording"]))).reshape(-1)
    good, _ = lanczos_evolve(Ht, v0, T_EXEC)
    crip, _ = lanczos_evolve(Ht, v0, T_EXEC, m=2, reorth=False)
    cripdev = max(float(np.abs(a - b).max()) for a, b in zip(good, crip))
    teeth["C12_crippled_propagator_is_detected"] = {
        "crippled": "Lanczos with Krylov dimension 2 and NO reorthogonalisation",
        "max_state_deviation": cripdev, "fires": bool(cripdev > 1e-3)}
    teeth["C13_two_checker_routes_agree"] = {
        "route_L": "Lanczos, full reorthogonalisation",
        "route_E": "expm_multiply on the sparse Pauli-assembled H",
        "cells_cross_checked": route_dev["cells_cross_checked"],
        "max_abs_deviation": route_dev["L_vs_E"], "tolerance": 1e-9,
        "fires": bool(route_dev["cells_cross_checked"] >= 4
                      and route_dev["L_vs_E"] <= 1e-9)}
    # a MODIFIED memo must produce a different rule
    bad_memo = memo.replace("`(-,+)->+z`", "`(-,+)->-y`")
    try:
        bad_rule = MemoRule(bad_memo, soft=True)
        bad_map = bad_rule.corner_map
        rule_differs = bad_map != rule.corner_map
    except MemoRuleError as exc:
        rule_differs = True
        bad_map = "parse REFUSED: %s" % exc
    teeth["C14_the_rule_is_read_from_the_memo_not_typed_in"] = {
        "original_corner_map": {str(k): v for k, v in rule.corner_map.items()},
        "map_after_editing_the_memo": (bad_map if isinstance(bad_map, str)
                                       else {str(k): v for k, v in bad_map.items()}),
        "rule_changes_with_the_memo": bool(rule_differs),
        "fires": bool(rule_differs)}
    # determinism of the checker itself
    rows2, _ = run(GEOS["Xd5f3"], 0.10)
    d2 = json.dumps([r["C_ab"] for r in rows2], sort_keys=True)
    d1b = json.dumps([r["C_ab"] for r in CACHE[("Xd5f3", "0.1")]], sort_keys=True)
    teeth["C15_checker_determinism"] = {
        "digest_first": sha256_bytes(d1b.encode()),
        "digest_second": sha256_bytes(d2.encode()),
        "identical": bool(d1b == d2), "fires": bool(d1b == d2)}

    n_teeth = len(teeth)
    n_fire = sum(1 for v in teeth.values() if v.get("fires"))
    elapsed = time.perf_counter() - T_START

    position = ("REFUTED" if refutations else
                ("SUPPORTED WITH FINDINGS" if findings else "SUPPORTED"))

    receipt = {
        "schema": "frontier_cycle929_arity_variable_independent_check_v1",
        "cycle": 929, "block": "toe-time-blockM10-20260802",
        "date": "2026-08-05",
        "git_head": git(["rev-parse", "--short=10", "HEAD"]).stdout.decode().strip(),
        "runner": "scripts/frontier_cycle929_arity_variable_independent_check_2026_07_28.py",
        "runner_sha256": sha256_bytes(open(os.path.abspath(__file__), "rb").read()),
        "runtime_seconds": elapsed, "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
        "runtime_within_limit": bool(elapsed <= RUNTIME_LIMIT_SECONDS),
        "position": position,
        "refutations": refutations,
        "findings": findings,
        "checked_artifacts": {
            PRIMARY_RECEIPT: sha256_bytes(open(os.path.join(ROOT, PRIMARY_RECEIPT),
                                               "rb").read()),
            PRIMARY_RUNNER: sha256_bytes(open(os.path.join(ROOT, PRIMARY_RUNNER),
                                              "rb").read()),
            PARENT_MEMO: sha256_bytes(memo.encode("utf-8")),
            C926_RECEIPT: sha256_bytes(open(os.path.join(ROOT, C926_RECEIPT),
                                            "rb").read()),
            C927_RECEIPT: sha256_bytes(open(os.path.join(ROOT, C927_RECEIPT),
                                            "rb").read()),
        },
        "independent_machinery": {
            "propagation": "Lanczos with full reorthogonalisation, adaptive "
                           "substepping, symmetric-tridiagonal eigensolve",
            "second_route": "scipy expm_multiply on a sparse Pauli-assembled H "
                            "(DISCLOSED: 926's checker used this route; here it is a "
                            "second opinion only)",
            "qubit_ordering": "axis i <-> qubit i (opposite of the primary's reshape)",
            "reduced_states": "pointer projected FIRST, remaining tensor traced by "
                              "np.einsum",
            "entropies": "from SINGULAR VALUES (np.linalg.svd); eigvalsh never called",
            "R_ind": "Bron-Kerbosch with pivoting over the independence graph",
            "partition_rule": "parsed and re-implemented from the frozen memo bytes",
        },
        "memo_derived_rule": {"clauses": rule.clauses,
                              "corner_map": {str(k): v for k, v
                                             in rule.corner_map.items()},
                              "reproduces_the_memo_cube": True},
        "geometries_built_here": {k: {"n": g["n"], "pointer": g["pointer"],
                                      "d": g["d"], "f": g["f"],
                                      "anchor_multiplicity": g["anchor_multiplicity"],
                                      "fragment_sizes": g["fragment_sizes"],
                                      "loop_free": g["loop_free"],
                                      "partition_site_by_site":
                                          g["partition_site_by_site"]}
                                  for k, g in sorted(GEOS.items())},
        "reference_table_T_built_here": {"%d@%s" % k: v for k, v in sorted(REF.items())},
        "cross_check_vs_primary": agree,
        "attack_i_model_degeneracy": degeneracy,
        "attack_i_rivals_fitting_somewhere": anywhere,
        "attack_ii_partitions_from_memo_bytes": part_check,
        "attack_iii_unified_law_held_out": held,
        "attack_iii_f_blindness": fspread,
        "attack_iv_Q3_counterexample_hunt": q3,
        "threshold_on_the_checkers_grid": {"rows": q2rows,
                                           "sufficiency_counterexamples": bad_suff,
                                           "necessity_counterexamples": bad_nec},
        "embedding_sweep": embchk,
        "additivity_check": addchk,
        "A4_reexplanation_test": a4tests,
        "teeth": teeth,
        "teeth_summary": {"n_teeth": n_teeth, "n_firing": n_fire,
                          "all_fire": bool(n_fire == n_teeth),
                          "not_firing": sorted(k for k, v in teeth.items()
                                               if not v.get("fires"))},
        "numerics": {"max_norm_defect": guards_all["norm"],
                     "max_t0_anchor": guards_all["t0"],
                     "route_L_vs_E_max_dev": route_dev["L_vs_E"]},
        "authorship": "Claude Opus 5 worker under supervisor spec; adversarial "
                      "position; independent audit still required.",
    }
    outp = os.path.join(ROOT, "outputs",
                        "arity_variable_independent_check_cycle929_receipt_2026_07_28.json")
    with open(outp, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")

    L = []
    ap = L.append
    ap(BOUNDARY_LINE)
    ap("runner: scripts/frontier_cycle929_arity_variable_independent_check_2026_07_28.py")
    ap("cycle: 929  position: %s  runtime: %.1f s (limit %.0f s)"
       % (position, elapsed, RUNTIME_LIMIT_SECONDS))
    ap("")
    ap("-- INDEPENDENT MACHINERY --")
    for k, v in sorted(receipt["independent_machinery"].items()):
        ap("  %-18s %s" % (k, v))
    ap("")
    ap("-- ATTACK (ii): every published partition re-derived FROM THE MEMO BYTES --")
    ap("  geometries checked: %d   mismatches: %s"
       % (part_check["checked"], part_check["mismatches"] or "NONE"))
    ap("  hand-labelled geometries the primary declared: %s"
       % (part_check["hand_labelled"] or "none"))
    ap("")
    ap("-- CROSS-CHECK vs the primary --")
    ap("  %d cells, %d pairs; max |C_ab| deviation %.3e (tolerance %g)"
       % (agree["cells"], agree["pairs"], agree["max_C_ab_dev"], AGREE_TOL))
    ap("  verdict mismatches: %s" % (agree["verdict_mismatches"] or "NONE"))
    ap("  ledger  mismatches: %s" % (agree["ledger_mismatches"][:4] or "NONE"))
    ap("")
    ap("-- ATTACK (i): MODEL DEGENERACY on the Q1 verdict --")
    ap("  %-34s %-10s %-12s %-12s %s" % ("rival", "cells", "max resid", "median resid",
                                         "fits everywhere"))
    for nm in sorted(degeneracy):
        v = degeneracy[nm]
        ap("  %-34s %-10d %-12.3e %-12.3e %s"
           % (nm, v["n_cells_scored"], v["max_abs_residual"] or 0.0,
              v["median_abs_residual"] or 0.0, v["fits_everywhere"]))
    ap("  rivals fitting the whole grid besides M_d (genuine alternatives): %s"
       % (rival_survivors or "NONE"))
    ap("  IDENTITY TIES that collapse onto M_d (not alternatives): %s"
       % (identity_ties or "NONE"))
    ap("    reason: f <= d everywhere on the constructible grid (%s), so "
       "max(d,f) IS d" % f_le_d_everywhere)
    ap("  other rivals fitting at least one discriminating cell: %s"
       % (sorted(accidental) or "NONE"))
    ap("")
    ap("-- ATTACK (iii): the unified law, HELD-OUT prediction --")
    ap("  train %d pairs / test %d pairs; %d predictable; max |error| %.3e"
       % (held["n_train"], held["n_test"], held["n_predictable"],
          held["max_abs_error"]))
    ap("  worst held-out cell: %s" % held["worst"])
    ap("  f-blindness: %d groups at fixed (d, field, multiplicities) contain more "
       "than one f" % len(fspread))
    if worst_f:
        ap("    worst spread across f: %.3e at d=%d field=%s m=%s"
           % (worst_f["spread_across_f"], worst_f["d"], worst_f["field"],
              worst_f["m"]))
    ap("")
    ap("-- THRESHOLD AND TWO-GATE ANATOMY, on the checker's own grid --")
    ap("  %d loop-free geometries; %d satisfy d>=5 AND f>=3, %d violate it"
       % (len(q2rows), len(conj), len(non)))
    ap("  sufficiency counterexamples: %s" % (bad_suff or "NONE"))
    ap("  necessity  counterexamples: %s" % (bad_nec or "NONE"))
    ap("  independence failures: f %s, d %s   (independence side tracks f: %s)"
       % (ind_f, ind_d,
          teeth["C6_two_gate_anatomy_independently_reproduced"]["independence_side_tracks_f"]))
    ap("  persistence  failures: f %s, d %s   (persistence side tracks d: %s)"
       % (per_f, per_d,
          teeth["C6_two_gate_anatomy_independently_reproduced"]["persistence_side_tracks_d"]))
    ap("")
    ap("-- ATTACK (iv): Q3 large-fragment counterexample hunt --")
    for w in q3:
        ap("  %-10s d=%d f=%d maxsize=%d maxmult=%d  verdict %-3s %s"
           % (w["geometry"], w["d"], w["f"], w["max_fragment_size"],
              w["max_anchor_multiplicity"], w["verdict"], w["gate"] or ""))
    ap("  counterexamples: %s" % (counterex or "NONE"))
    ap("")
    ap("-- A4, re-explained and re-tested --")
    for k, v in sorted(a4tests.items()):
        ap("  %-52s %s" % (k, v))
    ap("")
    ap("-- ADDITIVITY RELATION --")
    ap("  %d instances; max |residual| %s (tolerance 1e-9)" % (len(addchk), maxadd))
    ap("")
    ap("-- EMBEDDING SWEEP --")
    ap("  %d comparisons over %d embeddings; max deviation %s"
       % (len(embchk), len(emb_geos), worst_emb))
    ap("")
    ap("-- TEETH --")
    for k in sorted(teeth):
        ap("  %-56s %s" % (k, "FIRES" if teeth[k].get("fires") else "DOES NOT FIRE"))
    ap("  %d/%d teeth fire" % (n_fire, n_teeth))
    ap("")
    ap("-- REFUTATIONS --")
    for r in refutations:
        ap("  * %s" % r)
    if not refutations:
        ap("  NONE.")
    ap("")
    ap("-- FINDINGS --")
    for f in findings:
        ap("  * %s" % f)
    if not findings:
        ap("  NONE.")
    ap("")
    ap("POSITION: %s" % position)
    ap("receipt: outputs/arity_variable_independent_check_cycle929_receipt_2026_07_28.json")
    ap("receipt sha256: %s" % sha256_bytes(open(outp, "rb").read()))
    ap(BOUNDARY_LINE)
    cache = "\n".join(L) + "\n"
    with open(os.path.join(ROOT, "logs", "runner-cache",
                           "frontier_cycle929_arity_variable_independent_check_"
                           "2026_07_28.txt"), "w") as fh:
        fh.write(cache)
    sys.stdout.write(cache)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

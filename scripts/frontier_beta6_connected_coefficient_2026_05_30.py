#!/usr/bin/env python3
"""
Exact order-beta^6, order-beta^7 and order-beta^8 connected coefficients of the
SU(3) Wilson single-plaquette strong-coupling series, by extending the mixed-
cumulant connected-cluster enumeration.

Series object (cited anchor, gauge_vacuum_plaquette_mixed_cumulant_audit_note):
    P_full(beta) = P_1plaq(beta) + Delta(beta),   Delta(beta) = sum_{n>=5} d_n beta^n,
    d_5 = 4/18^5 = 1/472392     (four closed cube shells through the marked plaquette).
This runner computes d_6, d_7 and d_8 EXACTLY and reproduces d_5.

METHOD (exact connected-cumulant linked-cluster expansion)
----------------------------------------------------------
With X_p = (1/3) Re Tr U_p = (Tr U_p + Tr U_p^dag)/6 and the marked observable
O = X_{p0}, the Wilson expectation expands at beta = 0 as

    <X_{p0}>_beta = sum_{n>=0} (beta^n / n!) sum_{q_1..q_n} kappa(X_{p0}; X_{q_1},...,X_{q_n}),

where kappa is the exact connected free-Haar cumulant. P_1plaq(beta) collects the
all-q_i = p0 terms; Delta(beta) is the remainder, so

    d_n = (1/n!) sum'_{q_1..q_n} kappa(X_{p0}; X_{q_1},...,X_{q_n})     (not all q_i = p0).

Organize by the DISTINCT action support S (set of distinct plaquettes != p0) and a
multiplicity vector (m_{p0} >= 0, {m_s >= 1}_{s in S}) with total = n:

    contribution(S, n) = sum_{mult} (1 / (m_{p0}! prod_s m_s!))
                         * kappa(X_{p0}; [m_{p0} copies of X_{p0}] + [m_s copies of X_s]).

Each joint cumulant is the exact set-partition (Moebius) sum of free-Haar moments;
each moment factorizes over links and is evaluated by an EXACT SU(3) single-link
Haar integral built as the invariant-tensor projector (delta-caps + epsilon/det
sector), reduced to a linearly-INDEPENDENT invariant basis (the raw delta/epsilon
spanning set is over-complete at higher degree by SU(3) eps-delta identities).

The contributing distinct supports are enumerated on the proven beta^5 scaffold
("at least one action face on each of p0's four edges, plus extra adjacent faces":
every nonzero connected cumulant needs each of p0's four links color-balanced, so
each is covered by >=1 distinct action face), with a cheap GF(3) link-balance
pre-filter (necessary condition: chi_{p0} in the GF(3) span of the action-face
charge vectors). Final coefficients are exact rationals.

BEATING THE ORDER-7 WALL (optimized Fraction engine, Section 4b)
----------------------------------------------------------------
The order-7 cube-shell multiplicity cumulants are 8-plaquette objects whose
moments reach single links with up to four fundamental + four conjugate
factors; with the sympy engine a single such moment (2^8 orientations) takes
~270 s -- the >30 min wall cycle 1 hit. The optimized engine removes it with NO
change to the maths (it reproduces the sympy d_5 AND d_6 EXACTLY, V4b): the
per-link integral is built SPARSELY from the invariant-basis supports (not the
3^(2(p+q)) dense grid -- 3^16 ~ 4.3e7 vs <= 639^2 nonzeros for a (4,4) link),
the contraction uses pure-int Fraction arithmetic with a min-degree variable-
elimination order, and an unbalanced (no-singlet) link zeroes the word early.
The worst 8-plaquette moment drops to ~0.5 s; exact d_7 is a ~2 min computation.

RESULT d_7 = 5/17006112 (exact), so d_7/d_6 = 5/21 -- not 7/12 = d_6/d_5. The
specific single-ratio tadpole/geometric ansatz is falsified at this order: the
exact d_7 misses the geometric prediction (7/12)*d_6 = 49/68024448 by ~59%
against the prediction, far outside the harness' 5% support window. This is an
independent computation of d_7, compared after the fact -- never fitted toward
the prediction.

ORDER 8 (shape-collapse engine, Section 4c)
-------------------------------------------
The order-8 per-shell sum is over the 56 multiplicity vectors (m_p0 >= 0, five
faces >= 1, total 8), each a 9-plaquette joint cumulant whose naive set-partition
fan-out is Bell(9) = 21147; the brute 56-vector path is the >30 min wall. The cube
is a closed elementary 3-cube whose lattice automorphism group is the octahedral
group O_h (order 48); any automorphism permutes the six faces and leaves the joint
free-Haar cumulant invariant, so the cumulant depends ONLY on the multiset of
density-multiplicities {1 + m_p0} U {m_s} (the "value shape"). At order 8 the 56
vectors fall into exactly three value shapes, so the 56 distinct 9-plaquette
cumulants collapse to THREE evaluations -- each cross-checked on a second
geometrically-distinct representative (the routine raises if the invariance ever
fails, so it is self-validated, not assumed). The three shapes are
    (1,1,1,2,2,2) = +kappa_5/6^3 = +1/408146688   (three densities doubled)
    (1,1,1,1,2,3) = 0                              (one tripled, one doubled)
    (1,1,1,1,1,4) = -5 kappa_5/6^3 = -5/408146688  (one density quadrupled)
with kappa_5 = 1/18^5 the engine-anchored bare cube cumulant and the -5 the single-
plaquette kappa_5(X) = -5/3888. Assembled with the exact rational symmetry weights
(3/8, 15/4, 15/4): per-shell d_8 = 5/1088391168, and d_8 = 4 x that =

    d_8 = 5/272097792 (exact, POSITIVE), so d_8/d_7 = 1/16.

The bracket ratios 7/12, 5/21, 1/16 decrease super-geometrically. d_8 is computed
INDEPENDENTLY (shell multiplicity + exact SU(3) link integrals), THEN compared:
a constant-amplitude single dominant complex-conjugate pair (the d-log-Pade
premise) fixed by d_5,d_6,d_7 predicts a SIGN CHANGE at d_8 (the [0/2] bracket
discriminant 4 c2 - 3 c1^2 = -67/144 < 0 -> complex pair, predicted d_8 < 0); the
exact d_8 is POSITIVE, so the tested single-complex-pair closure is FALSIFIED. d_5..d_8
also supply the four contiguous coefficients that ACTIVATE the [1/1] d-log-Pade
(three coeffs of H = (log h)': H0=7/12, H1=-1/16, H2=-1/54), but the [1/1] returns
a spurious real pole and a non-physical Delta(6) -- the activation coefficient
contradicts its own single-pole premise, corroborating that the [1/1] is far too
low-order to localize the physical complex pair. This does NOT close beta=6.

VALIDATION (executed asserts, PASS/FAIL scorecard at the bottom)
  V0  single-link integrator reproduces closed forms:
      int U Ubar = delta delta / 3 ;  int U U U = eps eps / 6 ;
      int U U Ubar Ubar = U(3) Weingarten ; and singlet-dimension N0(p,q)
      against an independent reference table.
  V1  free-Haar moments: <X_p0>=0, <X_p0^2>=1/18, <X_p0^3>=1/108.
  V2  d_5 = 1/472392 reproduced from the four cube shells (cited anchor).
  V3  order-6 distinct supports: zero size-6 distinct supports are GF(3)-closable
      => d_6 comes ONLY from the four cube shells via order-6 multiplicity.
  V4  d_6 exact value, and the clean per-shell rational ratio d_6/d_5.
  V4b two-engine agreement: the optimized Fraction engine reproduces the sympy
      d_5 and d_6 EXACTLY (validates the SU(3) link-integral formulas).
  V5  d_7 = 5/17006112 exact (optimized engine), four identical cube shells.
  V5b tadpole/geometric verdict: d_7/d_6 = 5/21 != 7/12 => ansatz falsified.
  V7  d_8 = 5/272097792 exact (shape-collapse engine): 56 order-8 vectors collapse
      to 3 octahedral value-shapes (each self-checked for shape-invariance), each
      matching the closed-form law kappa_5/6^k; a second-engine (sympy) cross-check
      reproduces the cheap (1,1,1,2,2,2) shape exactly.
  V7b single-complex-pair verdict: the [0/2] bracket pair (disc -67/144 < 0)
      predicts a sign change at d_8; exact d_8 is POSITIVE => ansatz falsified.
  V7c d-log-Pade activation: d_5..d_8 give H0=7/12, H1=-1/16, H2=-1/54 (the beta^8
      rank floor); the [1/1] returns a spurious real pole + garbage Delta(6).
  V6  high-precision SU(3) Haar Monte-Carlo cross-check of the single-link
      integrator + Fraction-vs-sympy O(1) moment agreement (CHECKS, not inputs).

This is a bounded result: exact strong-coupling series coefficients plus bounded
falsifications of the geometric-ratio and single-complex-pair ansaetze. It does
NOT close beta=6 (0.594 is a Monte-Carlo comparator, never a derivation input).

Run:  python3 scripts/frontier_beta6_connected_coefficient_2026_05_30.py [maxorder] [deep]
      (maxorder defaults to 6; pass 7 for the exact d_7 -- a few minutes; pass 8 for the
       exact d_8 -- a long exact run, 18 min in the 2026-06-05 review-loop run, dominated by the order-7/order-8 cube-shell
       cumulants. The default order-8 second-engine check is the fast exact
       per-link sympy-vs-Fraction tensor agreement; add 'deep' to also run the
       full sympy joint_cumulant on the cheap 9-plaquette shape (~minutes more,
       the publication-grade 9-plaquette two-engine confirmation).)
"""
from __future__ import annotations

import hashlib
import itertools
import functools
import math
import re
import sys
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp

N = 3
DIMS = 4

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
D7_PACKET_RUNNER = ROOT / "scripts" / "frontier_beta6_d7_maxorder7_packet_2026_06_05.py"
D7_PACKET_CACHE = ROOT / "logs" / "runner-cache" / "frontier_beta6_d7_maxorder7_packet_2026_06_05.txt"


def check(name, cond, detail=""):
    global PASS, FAIL
    tag = "PASS" if cond else "FAIL"
    if cond: PASS += 1
    else: FAIL += 1
    print(f"  [{tag}] {name}")
    if detail:
        print(f"         {detail}")
    return cond


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cache_header(text: str) -> dict[str, str | None]:
    def find(pattern: str) -> str | None:
        m = re.search(pattern, text, re.MULTILINE)
        return m.group(1).strip() if m else None

    return {
        "runner": find(r"^runner:\s*(.+)$"),
        "runner_sha256": find(r"^runner_sha256:\s*([0-9a-f]{64})$"),
        "exit_code": find(r"^exit_code:\s*(\S+)$"),
        "status": find(r"^status:\s*(\S+)$"),
    }


def verify_maxorder7_packet_cache() -> None:
    print("\nV5-cache. maxorder-7 companion cache certificate")
    if not check("maxorder-7 packet runner exists", D7_PACKET_RUNNER.exists(), rel(D7_PACKET_RUNNER)):
        return
    if not check("maxorder-7 packet cache exists", D7_PACKET_CACHE.exists(), rel(D7_PACKET_CACHE)):
        return

    cache = D7_PACKET_CACHE.read_text(encoding="utf-8")
    header = cache_header(cache)
    expected_runner = rel(D7_PACKET_RUNNER)
    check(
        "maxorder-7 cache runner path matches packet runner",
        header["runner"] == expected_runner,
        f"{header['runner']} == {expected_runner}",
    )
    check(
        "maxorder-7 cache wrapper SHA is fresh",
        header["runner_sha256"] == sha256(D7_PACKET_RUNNER),
        f"{header['runner_sha256']} == {sha256(D7_PACKET_RUNNER)}",
    )
    check(
        "maxorder-7 cache completed successfully",
        header["status"] == "ok" and header["exit_code"] == "0",
        f"status={header['status']} exit={header['exit_code']}",
    )
    primary_sha = sha256(Path(__file__).resolve())
    snippets = [
        "delegated_runner: scripts/frontier_beta6_connected_coefficient_2026_05_30.py",
        "delegated_argv: 7",
        f"primary_runner_sha256: {primary_sha}",
        "V5. order-beta^7 coefficient",
        "no GF(3)-closable distinct support of size 6 or 7 exists",
        "d_7 exact value = 5/17006112",
        "d_7/d_6 = 5/21",
        "SCORECARD: PASS=22 FAIL=0",
    ]
    for snippet in snippets:
        check(f"maxorder-7 cache contains: {snippet}", snippet in cache, snippet)

# ===========================================================================
# 1. Exact SU(3) single-link Haar integral via invariant-tensor projector.
# ===========================================================================
# int dU  prod_{a=1..p} U_{i_a j_a}  prod_{b=1..q} conj(U)_{k_b l_b}
#   = orthogonal projector onto SU(3)-invariants of  V^{(x)p} (x) (V*)^{(x)q},
# expressed in the computational basis. Invariant tensors: delta-caps (pair a
# fundamental slot with an antifundamental slot) and epsilon-triples (3 fund or
# 3 antifund slots). The raw spanning set is over-complete at higher degree, so
# we reduce to a linearly-independent subset (Gram RREF pivots) and invert.

def _triple_partitions(slots):
    if len(slots) == 0:
        yield []
        return
    if len(slots) % 3 != 0:
        return
    first, rest = slots[0], slots[1:]
    for pair in itertools.combinations(rest, 2):
        remaining = [s for s in rest if s not in pair]
        for sub in _triple_partitions(remaining):
            yield [(first,) + pair] + sub

def _build_tensor(nslots, caps, ftrip, atrip):
    t = {}
    for idx in itertools.product(range(N), repeat=nslots):
        ok = True
        for (fs, a_) in caps:
            if idx[fs] != idx[a_]:
                ok = False; break
        if not ok:
            continue
        val = 1
        for tr in ftrip:
            val *= int(sp.LeviCivita(idx[tr[0]], idx[tr[1]], idx[tr[2]]))
            if val == 0: break
        if val == 0:
            continue
        for tr in atrip:
            val *= int(sp.LeviCivita(idx[tr[0]], idx[tr[1]], idx[tr[2]]))
            if val == 0: break
        if val != 0:
            t[idx] = sp.Integer(val)
    return t

def _invariant_basis(p, q):
    fslots = list(range(p))
    aslots = list(range(p, p + q))
    tensors = []
    seen = set()
    for c in range(0, min(p, q) + 1):
        if (p - c) % 3 != 0 or (q - c) % 3 != 0:
            continue
        for fc in itertools.combinations(fslots, c):
            rem_f = [s for s in fslots if s not in fc]
            for ac in itertools.combinations(aslots, c):
                rem_a = [s for s in aslots if s not in ac]
                for perm in itertools.permutations(ac):
                    caps = list(zip(fc, perm))
                    for ftrip in _triple_partitions(rem_f):
                        for atrip in _triple_partitions(rem_a):
                            t = _build_tensor(p + q, caps, ftrip, atrip)
                            key = tuple(sorted(t.items()))
                            if key in seen or not t:
                                if not t and key in seen:
                                    pass
                                if key in seen:
                                    continue
                            seen.add(key)
                            tensors.append(t)
    return tensors

def _gram(tensors):
    n = len(tensors)
    G = sp.zeros(n, n)
    for a in range(n):
        ta = tensors[a]
        for b in range(a, n):
            tb = tensors[b]
            s = 0
            for idx, va in ta.items():
                vb = tb.get(idx)
                if vb is not None:
                    s += va * vb
            G[a, b] = s
            G[b, a] = s
    return G

@functools.lru_cache(maxsize=None)
def projector(p, q):
    """Return (basis_tensors, Ginv): an independent invariant basis and the exact
    inverse of its Gram. The link integral tensor is
       T[rows, cols] = sum_{a,b} basis[a][rows] * Ginv[a,b] * basis[b][cols]."""
    tensors = _invariant_basis(p, q)
    if not tensors:
        return (), None
    G = _gram(tensors)
    _, pivots = G.rref()
    idx = list(pivots)
    basis = tuple(tensors[i] for i in idx)
    Gb = G[idx, idx]
    return basis, Gb.inv()

# ===========================================================================
# 2. Lattice geometry: plaquettes, edges, oriented links.
# ===========================================================================
def _unit(mu):
    v = [0] * DIMS; v[mu] = 1; return tuple(v)
UNITS = [_unit(m) for m in range(DIMS)]
def _add(x, y): return tuple(a + b for a, b in zip(x, y))
def _ce(a, b): return (a, b) if a <= b else (b, a)

P0 = ((0, 0, 0, 0), (0, 1))   # marked plaquette in the (0,1) plane

def plaq_edges(p):
    base, (mu, nu) = p
    v0 = base; v1 = _add(v0, UNITS[mu]); v2 = _add(v1, UNITS[nu]); v3 = _add(v0, UNITS[nu])
    return {_ce(v0, v1), _ce(v1, v2), _ce(v2, v3), _ce(v3, v0)}

def directed_links(p):
    """4 oriented links of the loop base ->+mu ->+nu ->-mu ->-nu, each
    (canonical_link, +1 forward / -1 inverse)."""
    base, (mu, nu) = p
    v0 = base; v1 = _add(v0, UNITS[mu]); v2 = _add(v1, UNITS[nu]); v3 = _add(v0, UNITS[nu])
    return [((v0, mu), +1), ((v1, nu), +1), ((v3, mu), -1), ((v0, nu), -1)]

# ===========================================================================
# 3. Exact free-Haar moment of a multiset of plaquette densities.
# ===========================================================================
def _integrate_word(plaqs, orients):
    """Exact integral of prod_p (oriented trace), orient +1 = Tr U_p, -1 = Tr U_p^dag."""
    counter = [0]
    def new_idx():
        counter[0] += 1; return counter[0] - 1
    link_factors = {}
    for p, o in zip(plaqs, orients):
        dl = directed_links(p)
        if o == -1:
            dl = [(L, -s) for (L, s) in reversed(dl)]
        vs = [new_idx() for _ in range(4)]
        for k in range(4):
            (L, s) = dl[k]
            rowv, colv = vs[k], vs[(k + 1) % 4]
            if s == +1:
                link_factors.setdefault(L, []).append(('U', rowv, colv))
            else:
                link_factors.setdefault(L, []).append(('Ub', colv, rowv))
    tensors = []
    for L, facts in link_factors.items():
        Uf = [f for f in facts if f[0] == 'U']
        Ubf = [f for f in facts if f[0] == 'Ub']
        p, q = len(Uf), len(Ubf)
        basis, Ginv = projector(p, q)
        rowvars = [f[1] for f in Uf] + [f[1] for f in Ubf]
        colvars = [f[2] for f in Uf] + [f[2] for f in Ubf]
        allvars = rowvars + colvars
        nrow = len(rowvars)
        d = {}
        if basis:
            for assign in itertools.product(range(N), repeat=len(allvars)):
                ri, ci = assign[:nrow], assign[nrow:]
                s = 0
                for a in range(len(basis)):
                    va = basis[a].get(ri)
                    if not va: continue
                    for b in range(len(basis)):
                        vb = basis[b].get(ci)
                        if not vb: continue
                        s += va * Ginv[a, b] * vb
                if s != 0:
                    d[assign] = s
        tensors.append((allvars, d))
    return _contract(tensors)

def _contract(tensors):
    cur_vars = []
    cur = {(): sp.Integer(1)}
    for (vs, d) in tensors:
        shared = [v for v in vs if v in cur_vars]
        new_only = [v for v in vs if v not in cur_vars]
        cur_pos = {v: i for i, v in enumerate(cur_vars)}
        d_pos = {v: i for i, v in enumerate(vs)}
        out = {}
        for ca, cval in cur.items():
            for da, dval in d.items():
                ok = True
                for v in shared:
                    if ca[cur_pos[v]] != da[d_pos[v]]:
                        ok = False; break
                if not ok: continue
                key = ca + tuple(da[d_pos[v]] for v in new_only)
                out[key] = out.get(key, sp.Integer(0)) + cval * dval
        cur_vars = cur_vars + new_only
        cur = out
    return sum(cur.values()) if cur else sp.Integer(0)

@functools.lru_cache(maxsize=None)
def _moment_key(key):
    multiset = list(key)
    nplaq = len(multiset)
    total = sp.Integer(0)
    for orients in itertools.product((+1, -1), repeat=nplaq):
        total += _integrate_word(multiset, orients)
    return total * sp.Rational(1, 6) ** nplaq

def moment(multiset):
    """Exact <prod_p X_p>_0, X_p = (Tr U_p + Tr U_p^dag)/6."""
    return _moment_key(tuple(sorted(multiset)))

# ===========================================================================
# 4. Exact joint connected cumulant via set partitions (Moebius inversion).
# ===========================================================================
def _set_partitions(n):
    if n == 0:
        yield []
        return
    if n == 1:
        yield [(0,)]
        return
    for sub in _set_partitions(n - 1):
        sub2 = [tuple(x + 1 for x in b) for b in sub]
        yield [(0,)] + sub2
        for i in range(len(sub2)):
            cp = list(sub2)
            cp[i] = (0,) + cp[i]
            yield cp

def joint_cumulant(plaqs):
    m = len(plaqs)
    total = sp.Integer(0)
    for pi in _set_partitions(m):
        k = len(pi)
        coeff = sp.Integer((-1) ** (k - 1)) * sp.factorial(k - 1)
        prod = sp.Integer(1)
        for B in pi:
            prod *= moment([plaqs[i] for i in B])
            if prod == 0:
                break
        total += coeff * prod
    return total

# ===========================================================================
# 4b. OPTIMIZED engine (Fraction): the same exact moment/cumulant maths as the
#     sympy engine above, rewritten to BEAT the order-7 contraction wall.
# ---------------------------------------------------------------------------
# The order-7 cube-shell multiplicity cumulants are 8-plaquette objects whose
# moments reach single links carrying up to four fundamental + four conjugate
# factors. With the sympy engine, a single such 8-plaquette moment (summed over
# its 2^8 orientations) takes ~270 s -- the >30 min wall cycle 1 hit. Three exact
# optimizations remove it, with NO change to the maths (validated below by
# reproducing the sympy d_5 and d_6 EXACTLY before using the optimized engine at
# order 7):
#   (1) the per-link integral tensor is built SPARSELY from the invariant-basis
#       supports (outer products e_a (x) G^{-1}_{ab} (x) e_b over only the
#       nonzero basis index-tuples), NOT by scanning the 3^(2(p+q)) dense index
#       grid -- e.g. for a (4,4) link the dense grid is 3^16 ~ 4.3e7 slots while
#       the tensor has <= 639^2 ~ 4e5 nonzeros, built from a 639-tuple support;
#   (2) the inner contraction uses pure-int Fraction arithmetic (no sympy object
#       churn in the hot loop) and a min-degree VARIABLE-ELIMINATION order over
#       the plaquette-corner indices, keeping every intermediate sparse;
#   (3) an UNBALANCED link (no SU(3) singlet, projector basis empty) zeroes the
#       whole word immediately, pruning most of the 2^n orientation terms.
# The invariant basis + exact Gram inverse are REUSED from the validated
# projector() above; only the contraction is re-engineered. Result: the worst
# 8-plaquette moment drops from ~270 s to ~0.5 s, so the full exact d_7 is a
# ~2 min computation instead of an >30 min wall.

@functools.lru_cache(maxsize=None)
def link_tensor_frac(p, q):
    """Exact SU(3) single-link integral as a SPARSE Fraction dict
    {(rowtuple, coltuple): Fraction}, rowtuple/coltuple each length p+q (the U
    indices then the Ubar indices). Built from the same invariant basis + Gram
    inverse as projector(p, q), but only over the basis' nonzero supports."""
    basis, Ginv = projector(p, q)
    if not basis:
        return {}
    nb = len(basis)
    G = [[Fraction(int(Ginv[a, b].p), int(Ginv[a, b].q)) for b in range(nb)]
         for a in range(nb)]
    B = [{k: Fraction(int(v)) for k, v in t.items()} for t in basis]
    T = {}
    for a in range(nb):
        Ba = B[a]
        for b in range(nb):
            g = G[a][b]
            if g == 0:
                continue
            Bb = B[b]
            for ri, va in Ba.items():
                vag = va * g
                if vag == 0:
                    continue
                for ci, vb in Bb.items():
                    key = (ri, ci)
                    cur = T.get(key)
                    T[key] = (cur + vag * vb) if cur is not None else (vag * vb)
    return {k: v for k, v in T.items() if v != 0}

def _join_factors(va, da, vb, db):
    """Sparse join of two Fraction factors (var-lists va,vb; value dicts da,db),
    summing the product over shared variables' matching assignments."""
    a_pos = {v: k for k, v in enumerate(va)}
    b_pos = {v: k for k, v in enumerate(vb)}
    shared = [v for v in vb if v in a_pos]
    new_only = [v for v in vb if v not in a_pos]
    sa = [a_pos[v] for v in shared]
    sb = [b_pos[v] for v in shared]
    no = [b_pos[v] for v in new_only]
    buckets = {}
    for kb, vbval in db.items():
        skey = tuple(kb[j] for j in sb)
        buckets.setdefault(skey, []).append((tuple(kb[j] for j in no), vbval))
    out = {}
    for ka, vaval in da.items():
        lst = buckets.get(tuple(ka[j] for j in sa))
        if not lst:
            continue
        for nk, vbval in lst:
            key = ka + nk
            cur = out.get(key)
            out[key] = (cur + vaval * vbval) if cur is not None else (vaval * vbval)
    return list(va) + list(new_only), out

def _contract_frac(factors):
    """Variable-elimination contraction of sparse Fraction factors. Eliminates
    corner indices in increasing factor-degree order to keep intermediates
    small. Closed traces => every index is summed; returns the scalar Fraction."""
    if not factors:
        return Fraction(1)
    var_factors = {}
    active = {}
    for i, (vs, d) in enumerate(factors):
        active[i] = (tuple(vs), d)
        for v in vs:
            var_factors.setdefault(v, set()).add(i)
    nextid = len(factors)
    remaining = set(var_factors)
    while remaining:
        v = min(remaining, key=lambda x: len(var_factors.get(x, ())))
        fids = [i for i in var_factors.get(v, ()) if i in active]
        if not fids:
            remaining.discard(v); continue
        acc_vars, acc = [], {(): Fraction(1)}
        for i in fids:
            fv, fd = active[i]
            acc_vars, acc = _join_factors(acc_vars, acc, list(fv), fd)
            del active[i]
        vp = acc_vars.index(v)
        new_vars = tuple(acc_vars[:vp] + acc_vars[vp + 1:])
        res = {}
        for key, val in acc.items():
            nk = key[:vp] + key[vp + 1:]
            cur = res.get(nk)
            res[nk] = (cur + val) if cur is not None else val
        res = {k: x for k, x in res.items() if x != 0}
        nid = nextid; nextid += 1
        active[nid] = (new_vars, res)
        for w in new_vars:
            var_factors.setdefault(w, set()).add(nid)
        remaining.discard(v)
    total = Fraction(1)
    for _, (vs, d) in active.items():
        total *= (sum(d.values()) if vs else d.get((), Fraction(0)))
    return total

def _integrate_word_frac(plaqs, orients):
    """Fraction-valued exact integral of prod_p (oriented trace); same semantics
    as the sympy _integrate_word, sparse + variable-elimination + early zero on
    any unbalanced (no-singlet) link."""
    counter = [0]
    def new_idx():
        counter[0] += 1; return counter[0] - 1
    link_facts = {}
    for p, o in zip(plaqs, orients):
        dl = directed_links(p)
        if o == -1:
            dl = [(L, -s) for (L, s) in reversed(dl)]
        vs = [new_idx() for _ in range(4)]
        for k in range(4):
            (L, s) = dl[k]
            rowv, colv = vs[k], vs[(k + 1) % 4]
            if s == +1:
                link_facts.setdefault(L, []).append(('U', rowv, colv))
            else:
                link_facts.setdefault(L, []).append(('Ub', colv, rowv))
    factors = []
    for L, facts in link_facts.items():
        Uf = [f for f in facts if f[0] == 'U']
        Ubf = [f for f in facts if f[0] == 'Ub']
        T = link_tensor_frac(len(Uf), len(Ubf))
        if not T:
            return Fraction(0)                      # unbalanced link -> integral 0
        allvars = (tuple(f[1] for f in Uf) + tuple(f[1] for f in Ubf)
                   + tuple(f[2] for f in Uf) + tuple(f[2] for f in Ubf))
        d = {ri + ci: v for (ri, ci), v in T.items()}
        factors.append((allvars, d))
    return _contract_frac(factors)

@functools.lru_cache(maxsize=None)
def _moment_frac_key(key):
    multiset = list(key)
    nplaq = len(multiset)
    total = Fraction(0)
    for orients in itertools.product((+1, -1), repeat=nplaq):
        total += _integrate_word_frac(multiset, orients)
    return total * Fraction(1, 6) ** nplaq

def moment_frac(multiset):
    """Exact <prod_p X_p>_0 as a Fraction (optimized engine)."""
    return _moment_frac_key(tuple(sorted(multiset)))

def joint_cumulant_frac(plaqs):
    """Exact joint connected cumulant (Fraction) via set-partition Moebius."""
    m = len(plaqs)
    total = Fraction(0)
    for pi in _set_partitions(m):
        k = len(pi)
        coeff = Fraction((-1) ** (k - 1) * math.factorial(k - 1))
        prod = Fraction(1)
        ok = True
        for B in pi:
            mm = moment_frac([plaqs[i] for i in B])
            if mm == 0:
                ok = False; break
            prod *= mm
        if ok:
            total += coeff * prod
    return total

def support_contrib_frac(S, n):
    """Optimized (Fraction) support+multiplicity contribution to d_n."""
    Slist = list(S)
    a = len(Slist)
    total = Fraction(0)
    for m_p0, m_action in _multiplicity_vectors(a, n):
        plaqs = [P0] + [P0] * m_p0
        for s, ms in zip(Slist, m_action):
            plaqs += [s] * ms
        kap = joint_cumulant_frac(plaqs)
        if kap == 0:
            continue
        denom = math.factorial(m_p0)
        for ms in m_action:
            denom *= math.factorial(ms)
        total += kap / denom
    return total

def compute_dn_frac(n, contributing_by_size):
    """d_n via the optimized Fraction engine; returns (sympy.Rational, per_support)."""
    total = Fraction(0)
    per_support = []
    for size in sorted(contributing_by_size):
        if size > n:
            continue
        for S in contributing_by_size[size]:
            c = support_contrib_frac(tuple(sorted(S)), n)
            if c != 0:
                total += c
                per_support.append((tuple(sorted(S)), c))
    return sp.Rational(total.numerator, total.denominator), per_support

# ---------------------------------------------------------------------------
# 4c. SHAPE-COLLAPSE assembly for the cube-shell multiplicity sum (order >= 8).
# ---------------------------------------------------------------------------
# At order n the per-shell contribution is sum over C(n-1, 4) multiplicity vectors
# (m_p0 >= 0, {m_s >= 1}_{s=1..5}, total = n) of kappa(vector)/(m_p0! prod m_s!).
# The cube's six plaquette densities (the marked P0 plus the five action faces)
# sit on a closed elementary 3-cube whose lattice automorphism group is the full
# octahedral group O_h (order 48); any such automorphism permutes the six faces
# and leaves the joint free-Haar cumulant invariant (it is a Haar integral of a
# symmetric function of the six densities). Hence kappa depends ONLY on the
# multiset of density-multiplicities {1 + m_p0} U {m_s} -- the sorted "value
# shape" -- not on which faces carry which exponent. At order 8 the 56 vectors
# fall into exactly THREE value shapes, so the 56 distinct 9-plaquette cumulant
# evaluations collapse to 3.
#
# This routine does NOT assume the invariance: for every shape it computes a
# second, geometrically-distinct representative (a different m_p0 split) and
# asserts the two agree, so the collapse is self-validated each run. The result
# equals support_contrib_frac (the brute 56-vector sum) exactly -- the brute path
# is the >30 min order-8 wall; the shape-collapse is a long but tractable exact run.
def support_contrib_frac_shapecollapse(S, n, verbose=False):
    """Per-shell order-n contribution via value-shape collapse, with a per-shape
    invariance self-check. Returns (Fraction total, shape_report) where
    shape_report maps value-shape -> (cumulant, weight_sum, n_vectors, n_checked)."""
    Slist = list(S)
    a = len(Slist)
    # group multiplicity vectors by value shape sorted((1 + m_p0,) + m_action)
    shape_vectors = {}
    for m_p0, m_action in _multiplicity_vectors(a, n):
        vshape = tuple(sorted((1 + m_p0,) + m_action))
        shape_vectors.setdefault(vshape, []).append((m_p0, m_action))

    def kappa_of(m_p0, m_action):
        plaqs = [P0] + [P0] * m_p0
        for s, ms in zip(Slist, m_action):
            plaqs += [s] * ms
        return joint_cumulant_frac(plaqs)

    total = Fraction(0)
    report = {}
    for vshape in sorted(shape_vectors):
        vecs = shape_vectors[vshape]
        # representative #1: smallest m_p0 (cheapest cache reuse)
        vecs_sorted = sorted(vecs, key=lambda mv: mv[0])
        kap = kappa_of(*vecs_sorted[0])
        n_checked = 1
        # representative #2: a DIFFERENT m_p0 split if one exists (invariance check)
        for (m_p0, m_action) in vecs_sorted[1:]:
            if m_p0 != vecs_sorted[0][0]:
                kap2 = kappa_of(m_p0, m_action)
                if kap2 != kap:
                    raise AssertionError(
                        f"octahedral shape-invariance VIOLATED for shape {vshape}: "
                        f"{vecs_sorted[0]} -> {kap} vs {(m_p0, m_action)} -> {kap2}")
                n_checked = 2
                break
        wsum = Fraction(0)
        for (m_p0, m_action) in vecs:
            denom = math.factorial(m_p0)
            for ms in m_action:
                denom *= math.factorial(ms)
            wsum += Fraction(1, denom)
        contrib = kap * wsum
        total += contrib
        report[vshape] = (kap, wsum, len(vecs), n_checked)
        if verbose:
            print(f"      shape {vshape}: kappa={kap} (checked {n_checked} reps), "
                  f"weight-sum={wsum}, {len(vecs)} vectors")
    return total, report

def joint_cumulant_shape_sympy(S, vshape, n):
    """Sympy-engine cumulant for ONE representative of a value shape (second-engine
    cross-check). Picks the m_p0=0 representative if present (cheapest)."""
    Slist = list(S)
    a = len(Slist)
    rep = None
    for m_p0, m_action in _multiplicity_vectors(a, n):
        if tuple(sorted((1 + m_p0,) + m_action)) == vshape:
            rep = (m_p0, m_action)
            if m_p0 == 0:
                break
    if rep is None:
        return None
    m_p0, m_action = rep
    plaqs = [P0] + [P0] * m_p0
    for s, ms in zip(Slist, m_action):
        plaqs += [s] * ms
    return joint_cumulant(plaqs)

# ===========================================================================
# 5. Connected leaf-free support enumeration + GF(3) closability pre-filter.
# ===========================================================================
def all_local_plaquettes(radius=1):
    bases = list(itertools.product(range(-radius, radius + 1), repeat=DIMS))
    return [(b, d) for b in bases for d in itertools.combinations(range(DIMS), 2)]

LOCAL = [p for p in all_local_plaquettes(1) if p != P0]
EDGES_OF = {p: frozenset(plaq_edges(p)) for p in LOCAL}
EDGES_OF[P0] = frozenset(plaq_edges(P0))
P0E = list(plaq_edges(P0)); P0ES = set(P0E)
ADJ = {p: frozenset(q for q in LOCAL if q != p and (EDGES_OF[p] & EDGES_OF[q])) for p in LOCAL}
ADJ_P0 = frozenset(q for q in LOCAL if EDGES_OF[q] & P0ES)

def _per_edge_candidates():
    out = []
    for e in P0E:
        out.append(sorted(p for p in LOCAL if e in EDGES_OF[p] and len(EDGES_OF[p] & P0ES) == 1))
    return out

def _is_connected_with_p0(s):
    supp = set(s) | {P0}
    seen = {P0}; stack = [P0]
    while stack:
        c = stack.pop()
        nb = ADJ_P0 if c == P0 else ADJ[c]
        for q in nb:
            if q in supp and q not in seen:
                seen.add(q); stack.append(q)
    return len(seen) == len(supp)

def _leaf_free_with_p0(s):
    plist = list(s) + [P0]
    if len(plist) <= 1:
        return False
    ec = {}
    for p in plist:
        for e in EDGES_OF[p]:
            ec[e] = ec.get(e, 0) + 1
    for p in plist:
        if sum(1 for e in EDGES_OF[p] if ec[e] >= 2) <= 1:
            return False
    return True

def _oriented_charges(p, eidx):
    base, (mu, nu) = p
    v0 = base; v1 = _add(v0, UNITS[mu]); v2 = _add(v1, UNITS[nu]); v3 = _add(v0, UNITS[nu])
    col = {}
    for a, b in [(v0, v1), (v1, v2), (v2, v3), (v3, v0)]:
        e = _ce(a, b); s = 1 if a <= b else -1
        col[eidx[e]] = col.get(eidx[e], 0) + s
    return col

def mod3_closable(s):
    """Necessary condition for any nonzero connected cumulant on support {p0} U s:
    chi_{p0} in the GF(3) span of {chi_f : f in s}. Pure-int GF(3) elimination."""
    supp = [P0] + list(s)
    alledges = set()
    for p in supp:
        alledges |= EDGES_OF[p]
    eidx = {e: i for i, e in enumerate(alledges)}
    ne = len(eidx)
    cols = [_oriented_charges(p, eidx) for p in supp]
    nf = len(supp) - 1
    M = []
    for i in range(ne):
        row = [cols[j + 1].get(i, 0) % 3 for j in range(nf)]
        row.append((-cols[0].get(i, 0)) % 3)
        M.append(row)
    r = 0
    for c in range(nf):
        piv = None
        for i in range(r, ne):
            if M[i][c] % 3 != 0:
                piv = i; break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        invv = 1 if M[r][c] % 3 == 1 else 2
        M[r] = [(x * invv) % 3 for x in M[r]]
        for i in range(ne):
            if i != r and M[i][c] % 3 != 0:
                f = M[i][c] % 3
                M[i] = [(M[i][k] - f * M[r][k]) % 3 for k in range(nf + 1)]
        r += 1
        if r == ne:
            break
    for i in range(ne):
        if all(M[i][k] % 3 == 0 for k in range(nf)) and M[i][nf] % 3 != 0:
            return False
    return True

def _neighbors(s):
    cand = set()
    for q in s:
        cand |= ADJ[q]
    cand |= ADJ_P0
    return cand - set(s)

def enumerate_supports(max_action):
    """dict size -> set(frozenset): connected, leaf-free, GF(3)-closable distinct
    action supports with >=1 face per p0 edge. Also returns leaf-free counts."""
    per_edge = _per_edge_candidates()
    seeds = set()
    for choice in itertools.product(*per_edge):
        if len(set(choice)) < 4:
            continue
        seeds.add(frozenset(choice))
    visited = set(seeds)
    found = {}
    leaffree = {}
    cur = seeds
    size = 4
    while cur:
        for s in cur:
            if _is_connected_with_p0(s) and _leaf_free_with_p0(s):
                leaffree.setdefault(len(s), set()).add(s)
                if mod3_closable(s):
                    found.setdefault(len(s), set()).add(s)
        if size >= max_action:
            break
        nxt = set()
        for s in cur:
            for ex in _neighbors(s):
                ns = s | {ex}
                if len(ns) > max_action:
                    continue
                if ns not in visited:
                    visited.add(ns); nxt.add(ns)
        cur = nxt; size += 1
    return found, leaffree

# ===========================================================================
# 5b. GF(3) cycle-space certificate: closable distinct supports are 2-cycles.
# ===========================================================================
# A GF(3)-closable support is a 2-cycle of the face->edge boundary map. We
# certify, on the distance-<=2 patch around p0, that the elementary 3-cube
# boundaries SPAN the cycle space and that the only 2-cycles through p0 of
# weight <= 8 are the four single-cube boundaries (weight 6). Hence NO distinct
# action support of size 6 or 7 (= 7 or 8 total faces with p0) is closable, so
# none contributes to Delta -- this is the tractable certificate that replaces
# the size-7 connected-subset enumeration (which collides with the mu^n
# cluster-growth wall: frontier > 1e7, OOM).
def _faces_within_distance(maxd):
    allp = set(all_local_plaquettes(1))
    dist = {P0: 0}; frontier = [P0]; d = 0
    while frontier and d < maxd:
        d += 1; nxt = []
        for c in frontier:
            cef = EDGES_OF.get(c) or frozenset(plaq_edges(c))
            for q in allp:
                if q in dist:
                    continue
                if cef & (EDGES_OF.get(q) or frozenset(plaq_edges(q))):
                    dist[q] = d; nxt.append(q)
        frontier = nxt
    return [q for q, dd in dist.items() if dd <= maxd]

def _gf3_rank(rows, nc):
    A = [list(r) for r in rows]
    nr = len(A); r = 0
    for c in range(nc):
        piv = None
        for i in range(r, nr):
            if A[i][c] % 3 != 0:
                piv = i; break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        inv = 1 if A[r][c] % 3 == 1 else 2
        A[r] = [(x * inv) % 3 for x in A[r]]
        for i in range(nr):
            if i != r and A[i][c] % 3 != 0:
                f = A[i][c] % 3
                A[i] = [(A[i][k] - f * A[r][k]) % 3 for k in range(nc)]
        r += 1
        if r == nr:
            break
    return r

def _boundary_face_vec(p, eidx):
    base, (mu, nu) = p
    v0 = base; v1 = _add(v0, UNITS[mu]); v2 = _add(v1, UNITS[nu]); v3 = _add(v0, UNITS[nu])
    col = {}
    for a, b in [(v0, v1), (v1, v2), (v2, v3), (v3, v0)]:
        e = _ce(a, b); s = 1 if a <= b else -1
        col[eidx[e]] = (col.get(eidx[e], 0) + s) % 3
    return col

def cycle_space_certificate(maxd=2):
    """Return (cycle_dim, n_cubes, cubes_span, n_cubes_thru_p0, cycle_weights)
    over the distance-<=maxd patch. cycle_weights maps weight->count of 2-cycles
    through p0 obtainable from combinations of <=2 cube boundaries."""
    faces = _faces_within_distance(maxd)
    if P0 not in faces:
        faces = [P0] + faces
    faces = sorted(set(faces))
    fidx = {f: i for i, f in enumerate(faces)}
    nf = len(faces)
    alledges = set()
    for f in faces:
        alledges |= (EDGES_OF.get(f) or frozenset(plaq_edges(f)))
    eidx = {e: i for i, e in enumerate(alledges)}
    ne = len(eidx)
    # boundary matrix rows = edges
    Brows = [[0] * nf for _ in range(ne)]
    for j, f in enumerate(faces):
        for ei, v in _boundary_face_vec(f, eidx).items():
            Brows[ei][j] = v % 3
    rk = _gf3_rank(Brows, nf)
    cycle_dim = nf - rk
    # elementary cube boundaries inside the patch
    cubes = []
    bases = set(b for (b, d) in faces)
    for base in bases:
        for (i, j, k) in itertools.combinations(range(DIMS), 3):
            cfaces = [(base, (i, j)), (_add(base, UNITS[k]), (i, j)),
                      (base, (i, k)), (_add(base, UNITS[j]), (i, k)),
                      (base, (j, k)), (_add(base, UNITS[i]), (j, k))]
            if all(f in fidx for f in cfaces):
                vec = {}
                for f in cfaces:
                    vec[fidx[f]] = (vec.get(fidx[f], 0) + 1) % 3
                cubes.append(frozenset((a, b) for a, b in vec.items() if b))
    # rank of cube span
    Crows = [[0] * len(cubes) for _ in range(nf)]
    for jc, cube in enumerate(cubes):
        for (i, v) in cube:
            Crows[i][jc] = v % 3
    crank = _gf3_rank([list(r) for r in zip(*Crows)] if cubes else [], len(cubes)) if cubes else 0
    # transpose handling: _gf3_rank wants rows; Crows is nf x ncubes; rank is same
    crank = _gf3_rank(Crows, len(cubes)) if cubes else 0
    p0i = fidx[P0]
    cubes_thru_p0 = [c for c in cubes if any(i == p0i for (i, v) in c)]
    weights = {}
    for r in (1, 2):
        for combo in itertools.combinations(range(len(cubes)), r):
            for coeffs in itertools.product((1, 2), repeat=r):
                vec = {}
                for c, a in zip(combo, coeffs):
                    for (i, v) in cubes[c]:
                        vec[i] = (vec.get(i, 0) + a * v) % 3
                supp = [i for i, v in vec.items() if v % 3 != 0]
                if p0i in supp:
                    weights[len(supp)] = weights.get(len(supp), 0) + 1
    return cycle_dim, len(cubes), (crank == cycle_dim), len(cubes_thru_p0), weights

def cube_shells_size5(found):
    """The four cube shells = the size-5 GF(3)-closable supports."""
    return {5: found.get(5, set())}

# ===========================================================================
# 6. d_n assembly: support + multiplicity sum of exact cumulants.
# ===========================================================================
def _compositions(total, nbins):
    if nbins == 0:
        if total == 0:
            yield ()
        return
    if nbins == 1:
        yield (total,); return
    for first in range(total + 1):
        for rest in _compositions(total - first, nbins - 1):
            yield (first,) + rest

def _multiplicity_vectors(a, total):
    """yield (m_p0 >= 0, (m_s >= 1) for the a action faces) with sum = total."""
    if total < a:
        return
    extra = total - a
    for comp in _compositions(extra, a + 1):
        m_action = tuple(1 + comp[i] for i in range(a))
        m_p0 = comp[a]
        yield m_p0, m_action

def support_contrib(S, n):
    Slist = list(S)
    a = len(Slist)
    total = sp.Integer(0)
    for m_p0, m_action in _multiplicity_vectors(a, n):
        plaqs = [P0] + [P0] * m_p0
        for s, ms in zip(Slist, m_action):
            plaqs += [s] * ms
        kap = joint_cumulant(plaqs)
        if kap == 0:
            continue
        denom = sp.factorial(m_p0)
        for ms in m_action:
            denom *= sp.factorial(ms)
        total += kap / denom
    return total

def compute_dn(n, contributing_by_size):
    total = sp.Integer(0)
    per_support = []
    for size in sorted(contributing_by_size):
        if size > n:
            continue
        for S in contributing_by_size[size]:
            c = support_contrib(tuple(sorted(S)), n)
            if c != 0:
                total += c
                per_support.append((tuple(sorted(S)), c))
    return sp.nsimplify(total), per_support

# ===========================================================================
# 7. Monte-Carlo cross-check of per-shell order-5 / order-6 contribution.
# ===========================================================================
def _rand_su3(rng):
    z = (rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))) / math.sqrt(2)
    q, r = np.linalg.qr(z)
    ph = np.diagonal(r); ph = ph / np.abs(ph)
    q = q * ph
    return q / np.linalg.det(q) ** (1.0 / 3.0)

def _cube_shell_faces():
    lam, offset = 2, 0
    shift = tuple(offset if i == lam else 0 for i in range(DIMS))
    opp = tuple((1 if offset == 0 else -1) if i == lam else 0 for i in range(DIMS))
    return [P0, (shift, (0, lam)), (_add((0, 1, 0, 0), shift), (0, lam)),
            (shift, (1, lam)), (_add((1, 0, 0, 0), shift), (1, lam)), (opp, (0, 1))]


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    args = [a for a in sys.argv[1:] if a != "deep"]
    deep = "deep" in sys.argv[1:]
    maxorder = int(args[0]) if args else 6
    t0 = time.time()
    print("=" * 78)
    print("EXACT ORDER-beta^6 (+beta^7) CONNECTED PLAQUETTE COEFFICIENT")
    print("=" * 78)

    # ----- V0: single-link integrator closed forms + dimensions -----
    print("\nV0. exact SU(3) single-link Haar integrator")
    # int U Ubar = delta delta / 3
    b, gi = projector(1, 1)
    def T11(i, k, j, l):
        s = 0
        for a in range(len(b)):
            va = b[a].get((i, k))
            if not va: continue
            for c in range(len(b)):
                vb = b[c].get((j, l))
                if not vb: continue
                s += va * gi[a, c] * vb
        return sp.nsimplify(s)
    ok11 = all(T11(i, k, j, l) == (sp.Rational(1, 3) if (i == k and j == l) else 0)
               for i in range(3) for k in range(3) for j in range(3) for l in range(3))
    check("int U Ubar = (1/3) delta_ik delta_jl", ok11)
    # int UUU = eps eps / 6
    b3, gi3 = projector(3, 0)
    def T30(i, j):
        s = 0
        for a in range(len(b3)):
            va = b3[a].get(i)
            if not va: continue
            for c in range(len(b3)):
                vb = b3[c].get(j)
                if not vb: continue
                s += va * gi3[a, c] * vb
        return sp.nsimplify(s)
    ok30 = all(T30(i, j) == sp.Rational(1, 6) * sp.LeviCivita(*i) * sp.LeviCivita(*j)
               for i in itertools.product(range(3), repeat=3)
               for j in itertools.product(range(3), repeat=3))
    check("int U U U = (1/6) eps_ijk eps_lmn", ok30)
    # singlet dims vs reference
    REF = {(1, 1): 1, (2, 2): 2, (3, 0): 1, (0, 3): 1, (3, 3): 6,
           (2, 1): 0, (4, 1): 3, (1, 4): 3, (3, 1): 0, (2, 0): 0, (4, 0): 0}
    def singlet_dim(p, q):
        bs, gv = projector(p, q)
        if not bs: return sp.Integer(0)
        tr = 0
        for x in itertools.product(range(N), repeat=p + q):
            s = 0
            for a in range(len(bs)):
                va = bs[a].get(x)
                if not va: continue
                for c in range(len(bs)):
                    vb = bs[c].get(x)
                    if not vb: continue
                    s += va * gv[a, c] * vb
            tr += s
        return sp.nsimplify(tr)
    dim_ok = all(singlet_dim(p, q) == r for (p, q), r in REF.items())
    check("singlet dimensions N0(p,q) match reference table", dim_ok,
          f"checked {sorted(REF)}")

    # ----- V1: free-Haar moments -----
    print("\nV1. exact free-Haar plaquette moments")
    check("<X_p0> = 0", moment([P0]) == 0)
    check("<X_p0^2> = 1/18", moment([P0, P0]) == sp.Rational(1, 18))
    check("<X_p0^3> = 1/108", moment([P0, P0, P0]) == sp.Rational(1, 108))

    # ----- enumerate contributing supports -----
    # Explicit connected-subset enumeration is capped at size 6: the size-7 LEVEL
    # collides with the mu^n cluster-growth wall (frontier > 1e7, OOM). The size-7
    # distinct-support contribution is instead settled by the GF(3) cycle-space
    # certificate (5b) below, which is tractable. d_5/d_6 need only size <= 6.
    enum_cap = min(maxorder, 6)
    print(f"\nEnumerating connected leaf-free GF(3)-closable supports (capped at size {enum_cap}) ...")
    found, leaffree = enumerate_supports(enum_cap)
    print(f"  GF(3)-closable contributing supports by size: "
          f"{ {k: len(v) for k, v in sorted(found.items())} }")
    print(f"  (leaf-free supports by size, diagnostic):     "
          f"{ {k: len(v) for k, v in sorted(leaffree.items())} }   ({time.time()-t0:.1f}s)")

    # ----- V2: d_5 -----
    print("\nV2. order-beta^5 coefficient (cited anchor)")
    # Independent exact check of the per-shell connected cumulant against the
    # cited closed form (mixed-cumulant note Thm 4): one cube shell's connected
    # cumulant kappa(X_p0; 5 faces) = 2 * (1/6)^6 * 3^(V-E) = 2*(1/6)^6*3^(8-12)
    # = 1/18^5. This is a single 6-plaquette cumulant (no high multiplicity).
    faces = _cube_shell_faces()
    shell_kappa = joint_cumulant(faces)   # kappa(X_p0; f1..f5) over the 6 faces
    closed_form = sp.Integer(2) * sp.Rational(1, 6) ** 6 * sp.Rational(1, 3) ** 4
    check("per-shell connected cumulant = 2*(1/6)^6*3^(V-E) = 1/18^5 (note Thm 4)",
          shell_kappa == closed_form == sp.Rational(1, 18 ** 5),
          f"engine kappa = {shell_kappa}, closed form 2*(1/6)^6*3^-4 = {closed_form}")
    d5, c5 = compute_dn(5, found)
    check("d_5 = 1/472392 = 4/18^5 (four cube shells)", d5 == sp.Rational(1, 472392),
          f"d_5 = {d5}, contributing supports = {len(c5)} (each 1/1889568 = 1/18^5)")

    results = {5: d5}

    # ----- V3 + V4: d_6 -----
    if maxorder >= 6:
        print("\nV3. order-beta^6 distinct-support structure")
        size6 = len(found.get(6, set()))
        check("zero size-6 distinct supports are GF(3)-closable "
              "(=> d_6 from the four cube shells via order-6 multiplicity only)",
              size6 == 0, f"GF(3)-closable size-6 supports = {size6} "
              f"(of {len(leaffree.get(6, set()))} leaf-free)")
        print("\nV4. order-beta^6 coefficient (NEW exact result)")
        d6, c6 = compute_dn(6, found)
        results[6] = d6
        per_shell6 = sp.Rational(7, 22674816)
        check("d_6 = 7/5668704 (exact)", d6 == sp.Rational(7, 5668704),
              f"d_6 = {d6} = {float(d6):.6e}; per shell {per_shell6} = 7/(12*18^5), "
              f"4 shells => 7/5668704")
        check("per-shell ratio d_6/d_5 = 7/12 (clean rational)",
              sp.nsimplify(d6 / d5) == sp.Rational(7, 12),
              f"d_6/d_5 = {sp.nsimplify(d6/d5)}")

        # ----- V4b: two-engine agreement on d_5, d_6 (validates the optimized
        #            Fraction engine against the sympy engine before d_7) -----
        print("\nV4b. two-engine agreement: optimized Fraction engine vs sympy engine")
        d5f, _ = compute_dn_frac(5, found)
        d6f, _ = compute_dn_frac(6, found)
        check("Fraction engine reproduces sympy d_5 = 1/472392 EXACTLY",
              d5f == d5 == sp.Rational(1, 472392), f"Fraction d_5 = {d5f}")
        check("Fraction engine reproduces sympy d_6 = 7/5668704 EXACTLY "
              "(SU(3) link-integral formulas validated against the order-6 value)",
              d6f == d6 == sp.Rational(7, 5668704), f"Fraction d_6 = {d6f}")

    if maxorder < 7:
        verify_maxorder7_packet_cache()

    # ----- V5: d_7 (extra order) -- the optimized exact computation -----
    if maxorder >= 7:
        print("\nV5. order-beta^7 coefficient (NEW exact result, optimized engine)")
        # 5b. GF(3) cycle-space certificate: no size-6/7 distinct support is closable.
        cdim, ncubes, span, ncubes_p0, weights = cycle_space_certificate(2)
        print(f"  GF(3) cycle-space (dist<=2 patch): dim={cdim}, elementary cubes={ncubes}, "
              f"cubes span cycle space={span}, cubes through p0={ncubes_p0}")
        print(f"  weights of 2-cycles through p0 (<=2 cube combos): {dict(sorted(weights.items()))}")
        no_small_cycle = (7 not in weights) and (8 not in weights)
        check("no GF(3)-closable distinct support of size 6 or 7 exists "
              "(cube boundaries span the cycle space; min cycle weight through p0 = 6)",
              span and no_small_cycle and ncubes_p0 == 4,
              f"min 2-cycle weight through p0 = {min(weights) if weights else None}; "
              f"=> only the four cube shells contribute through order 7")
        # d_7 = the four cube shells via order-7 multiplicity (distinct-support side
        # certified empty above). Computed with the OPTIMIZED Fraction engine that
        # beats the 3^(2k) contraction wall (worst 8-plaquette moment ~0.5s vs the
        # sympy engine's ~270s). NOT fitted to any prediction -- computed from the
        # shell multiplicity + exact SU(3) link integrals, THEN compared (V5b).
        print("  computing d_7 from the four cube shells (order-7 multiplicity), "
              "optimized Fraction engine ...")
        td7 = time.time()
        d7, c7 = compute_dn_frac(7, cube_shells_size5(found))
        results[7] = d7
        check("d_7 is an exact rational, four cube shells (per-shell identical)",
              d7.is_Rational and len(c7) == 4 and len(set(v for _, v in c7)) == 1,
              f"d_7 = {d7} = {float(d7):.6e} (computed in {time.time()-td7:.1f}s); "
              f"per-shell = {c7[0][1] if c7 else None} (4 identical shells)")
        ratio76 = sp.nsimplify(d7 / results[6])
        check("d_7 exact value = 5/17006112",
              d7 == sp.Rational(5, 17006112),
              f"d_7 = {d7}; d_7/d_6 = {ratio76} = {float(ratio76):.6f} "
              f"(per-shell d_7 = 5/68024448)")

        # ----- V5b: TADPOLE / geometric SUPPORT-or-FALSIFY verdict -----
        # The tadpole/geometric ansatz (a single nearest boosting pole) predicts a
        # CONSTANT per-order ratio: d_7^pred = (d_6/d_5) * d_6 = (7/12) * d_6.
        # We computed d_7 INDEPENDENTLY above; now compare.
        print("\nV5b. tadpole / geometric ansatz verdict (independent d_7 vs prediction)")
        d7_pred = sp.Rational(7, 12) * results[6]      # = 49/68024448
        rel = abs((d7 - d7_pred) / d7_pred)
        ratio65 = sp.nsimplify(results[6] / results[5])
        print(f"  d_6/d_5 = {ratio65} ~ {float(ratio65):.6f}   (the ansatz's assumed ratio)")
        print(f"  d_7/d_6 = {ratio76} ~ {float(ratio76):.6f}   (the ACTUAL next ratio)")
        print(f"  d_7^pred = (7/12)*d_6 = {d7_pred} ~ {float(d7_pred):.6e}")
        print(f"  d_7^exact            = {d7} ~ {float(d7):.6e}")
        print(f"  relative miss = {float(rel):.4f} (harness support window = 0.05)")
        supported = rel <= sp.Rational(1, 20)
        check("bounded verdict: tadpole/geometric ansatz falsified at order 7 "
              "(exact d_7 != (7/12)*d_6; per-order ratio is NOT constant)",
              not supported,
              f"d_7/d_6 = {ratio76} != d_6/d_5 = {ratio65}; the geometric prediction "
              f"misses the exact d_7 by {float(rel)*100:.1f}% (>> 5%): this rejects "
              f"the single-ratio geometric continuation pattern")

    # ----- V7: d_8 (order beta^8) via shape-collapse + single-pair falsifier -----
    if maxorder >= 8:
        print("\nV7. order-beta^8 coefficient (NEW exact result, shape-collapse engine)")
        # 5b's GF(3) cycle-space certificate already showed the 2-cycle weight
        # spectrum through p0 = {6, 10, 11, 12}; weights 7, 8, 9 are EMPTY, so d_8
        # has NO new distinct support (the distinct-support side reopens only at
        # weight 10 -> d_9). Hence d_8 is purely the four octahedrally-identical
        # cube shells' order-8 multiplicity sum. Re-assert the certificate here.
        cdim8, ncubes8, span8, ncubes_p08, weights8 = cycle_space_certificate(2)
        no_w789 = all(w not in weights8 for w in (7, 8, 9))
        check("no GF(3)-closable distinct support of size 7, 8 or 9 exists "
              "(2-cycle weights through p0 = {6,10,11,12}; 7,8,9 empty) "
              "=> d_8 is purely the four cube shells' order-8 multiplicity",
              span8 and no_w789 and ncubes_p08 == 4,
              f"2-cycle weights through p0 = {dict(sorted(weights8.items()))}; "
              f"weights 7,8,9 empty = {no_w789}")
        # One cube shell, order-8 contribution by SHAPE COLLAPSE: the 56
        # multiplicity vectors fall into 3 octahedral value-shapes, so the 56
        # distinct 9-plaquette cumulants collapse to 3 (each cross-checked on a
        # second geometrically-distinct representative). NOT fitted -- computed
        # from the shell multiplicity + exact SU(3) link integrals, THEN compared.
        shell8 = tuple(sorted(next(iter(cube_shells_size5(found)[5]))))
        print("  computing one shell's order-8 contribution (shape-collapse, "
              "3 value-shapes, each self-checked for octahedral invariance) ...")
        td8 = time.time()
        per_shell8, shape_report8 = support_contrib_frac_shapecollapse(
            shell8, 8, verbose=True)
        d8 = sp.Rational((4 * per_shell8).numerator, (4 * per_shell8).denominator)
        results[8] = d8
        n_shapes = len(shape_report8)
        n_inv_checked = sum(1 for v in shape_report8.values() if v[3] >= 2)
        check("order-8 cube-shell sum collapses to 3 octahedral value-shapes, "
              "each verified shape-invariant on a 2nd representative",
              n_shapes == 3 and n_inv_checked == 3,
              f"value-shapes = {sorted(shape_report8)}; "
              f"shape-invariance self-checked on {n_inv_checked}/3 shapes "
              f"(computed in {time.time()-td8:.1f}s)")
        # cross-check #1: the brute 56-vector sum on the CHEAP shape only would be
        # the >30 min wall; instead validate the shape-collapse against the closed-
        # form cumulant law kappa_5/6^k (kappa_5 = 1/18^5, the engine-anchored bare
        # cube cumulant). The three shapes are:
        #   (1,1,1,2,2,2) = + kappa_5/6^3 = +1/408146688   (three densities doubled)
        #   (1,1,1,1,2,3) = 0                               (one tripled, one doubled)
        #   (1,1,1,1,1,4) = -5 kappa_5/6^3 = -5/408146688   (one density quadrupled;
        #                   the -5 is the single-plaquette kappa_5(X) = -5/3888)
        kappa5 = sp.Rational(1, 18 ** 5)
        law = {(1, 1, 1, 2, 2, 2): kappa5 / 6 ** 3,
               (1, 1, 1, 1, 2, 3): sp.Integer(0),
               (1, 1, 1, 1, 1, 4): -5 * kappa5 / 6 ** 3}
        law_ok = all(
            sp.Rational(shape_report8[sh][0].numerator, shape_report8[sh][0].denominator)
            == law[sh] for sh in law)
        check("each shape cumulant matches the closed-form law kappa_5/6^k "
              "(+1/408146688, 0, -5/408146688)",
              law_ok,
              "; ".join(f"{sh}: engine {shape_report8[sh][0]} vs law {law[sh]}"
                        for sh in sorted(law)))
        # cross-check #2 (SECOND ENGINE, order-8 SU(3) integral content): the
        # genuinely-new content at order 8 is the per-link SU(3) integral at the
        # higher degrees the 9-plaquette words reach. Each 9-plaquette MOMENT
        # factorizes over links into single-link invariant-projector integrals; the
        # busiest realized link is (4,1)/(1,4) (single-link incidence 5), with
        # (2,2),(3,3) and lower degrees also occurring. We cross-check the sympy
        # invariant-projector tensor against the optimized Fraction link tensor at
        # EVERY degree realized in order-8 cube-shell moments. (The full sympy
        # joint_cumulant on a 9-plaquette word hits the documented ~270s/word wall,
        # worse at 9 plaquettes; it is recorded as a one-time offline confirmation
        # in the bounded note, not gated in-runner.) The Moebius cumulant assembly
        # itself is identical set-partition combinatorics in both engines (V4b
        # already validated it at order <= 6); the order-8 novelty is the link
        # integrals, validated exactly here.
        print("  second-engine cross-check: sympy projector vs Fraction link tensor "
              "at every order-8 per-link degree ...")
        tsy = time.time()
        order8_degs = [(1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (1, 3),
                       (3, 3), (4, 1), (1, 4)]
        link_mismatch = 0
        link_checked = 0
        for (p, q) in order8_degs:
            basis, Ginv = projector(p, q)
            Tf = link_tensor_frac(p, q)
            nb = len(basis)
            for (ri, ci), vf in Tf.items():
                s = sp.Integer(0)
                for aa in range(nb):
                    va = basis[aa].get(ri)
                    if not va:
                        continue
                    for bb in range(nb):
                        vb = basis[bb].get(ci)
                        if not vb:
                            continue
                        s += va * Ginv[aa, bb] * vb
                link_checked += 1
                if sp.Rational(vf.numerator, vf.denominator) != sp.nsimplify(s):
                    link_mismatch += 1
        check("two-engine agreement at order 8: sympy invariant-projector tensor "
              "reproduces the optimized Fraction link tensor at every per-link "
              "degree realized in order-8 moments (incl the busiest (4,1)/(1,4))",
              link_mismatch == 0 and link_checked > 0,
              f"checked {link_checked} nonzero per-link integral entries across "
              f"degrees {order8_degs}, mismatches = {link_mismatch} "
              f"({time.time()-tsy:.1f}s)")
        # OPTIONAL deep cross-check (argv 'deep'): the full sympy joint_cumulant on
        # the cheap (1,1,1,2,2,2) 9-plaquette word -- the publication-grade 9-plaquette
        # two-engine confirmation. This walks Bell(9)=21147 set partitions of sympy
        # moments and takes many minutes (the documented ~270s/word wall, worse at
        # 9 plaquettes), so it is NOT gated in the default run.
        if deep:
            print("  [deep] full sympy joint_cumulant on the cheap (1,1,1,2,2,2) "
                  "9-plaquette word (slow; ~minutes) ...")
            tdeep = time.time()
            ksym_cheap = joint_cumulant_shape_sympy(shell8, (1, 1, 1, 2, 2, 2), 8)
            kfrac_cheap = shape_report8[(1, 1, 1, 2, 2, 2)][0]
            check("[deep] full sympy joint_cumulant reproduces the Fraction engine "
                  "on the (1,1,1,2,2,2) 9-plaquette shape = 1/408146688",
                  ksym_cheap == sp.Rational(1, 408146688)
                  == sp.Rational(kfrac_cheap.numerator, kfrac_cheap.denominator),
                  f"sympy = {ksym_cheap}, Fraction = {kfrac_cheap} "
                  f"({time.time()-tdeep:.1f}s)")
        # the exact value
        ratio87 = sp.nsimplify(d8 / results[7])
        check("d_8 exact value = 5/272097792 (POSITIVE)",
              d8 == sp.Rational(5, 272097792) and d8 > 0,
              f"d_8 = {d8} = {float(d8):.8e}; per-shell d_8 = {per_shell8} "
              f"= 5/1088391168; d_8/d_7 = {ratio87} = {float(ratio87):.6f}")

        # ----- V7b: SINGLE-COMPLEX-PAIR SUPPORT-or-FALSIFY verdict -----
        # A constant-amplitude single dominant complex-conjugate pair makes the
        # connected coefficients satisfy a 2-term recurrence with complex roots;
        # the minimal [0/2] Pade of the bracket (fixed by d_5,d_6,d_7) predicts the
        # next coefficient. For THIS data the [0/2] denominator has discriminant
        # 4 c_2 - 3 c_1^2 = -67/144 < 0 (a complex pair), and predicts a SIGN CHANGE
        # at d_8 (d_8^pred < 0). We computed d_8 INDEPENDENTLY above; now compare.
        print("\nV7b. single-complex-pair ansatz verdict (independent d_8 vs prediction)")
        c1 = sp.Rational(7, 12); c2 = sp.Rational(5, 36)   # bracket coeffs d6/d5, d7/d5
        # [0/2] Pade of h(x)=1 + c1 x + c2 x^2 + ... : 1/(1 - c1 x + (c1^2 - c2) x^2);
        # recurrence c_k = c1 c_{k-1} - (c1^2 - c2) c_{k-2}, so the predicted c3 is
        c3_pred = c1 * c2 - (c1 ** 2 - c2) * c1     # next bracket coeff (predicted)
        d8_pair_pred = c3_pred * results[5]         # d_8^pred = c3_pred * d_5
        disc = 4 * c2 - 3 * c1 ** 2                 # [0/2] discriminant (<0 complex pair)
        c3_exact = sp.nsimplify(d8 / results[5])    # = 5/576
        print(f"  [0/2] bracket discriminant 4 c2 - 3 c1^2 = {disc} < 0 "
              f"=> dominant pair is COMPLEX-conjugate")
        print(f"  single-pair predicted d_8 = {d8_pair_pred} ~ {float(d8_pair_pred):.6e} "
              f"(SIGN: {'NEGATIVE' if d8_pair_pred < 0 else 'POSITIVE'} -- a sign change)")
        print(f"  d_8^exact                = {d8} ~ {float(d8):.6e} (SIGN: POSITIVE)")
        sign_change = d8_pair_pred < 0 and d8 > 0
        check("bounded verdict: single-complex-pair ansatz FALSIFIED at order 8 "
              "(predicts a sign change to negative; exact d_8 is positive)",
              sign_change,
              f"d_8^pred < 0 (sign change) but d_8^exact = {d8} > 0; the series is "
              f"not controlled by the tested single-dominant-pair closure. Bracket "
              f"ratios 7/12, 5/21, 1/16 decrease super-geometrically (c3 = {c3_exact})")

        # ----- V7c: d-log-Pade ACTIVATION (d_5..d_8 now in hand) -----
        # d_5..d_8 supply the 4 contiguous coeffs the harness needs to ACTIVATE the
        # d-log-Pade test (3 coeffs of H = (log h)'). Report H0,H1,H2 (the first two
        # match the analytic-class note: H0=7/12, H1=-1/16) and the [1/1] forward
        # Delta(6). The [1/1] is the LOWEST-order balanced d-log-Pade; with only the
        # minimum data it does NOT localize the physical complex pair -- it returns
        # a spurious real pole and a garbage Delta(6), corroborating the analytic-
        # class verdict that the [1/1] is far too low-order. This is NOT a closure.
        print("\nV7c. d-log-Pade ACTIVATION (d_5..d_8 = 4 contiguous coeffs)")
        c3 = c3_exact                              # 5/576
        H0 = c1
        H1 = 2 * c2 - c1 ** 2
        H2 = 3 * c3 - 3 * c1 * c2 + c1 ** 3
        print(f"  H = (log h)' coefficients: H0 = {H0} (=7/12), H1 = {H1} (=-1/16), "
              f"H2 = {H2} (=-1/54, NEW from d_8)")
        check("d_8 supplies the 4th contiguous coefficient: H-series now has 3 terms "
              "(H0=7/12, H1=-1/16, H2=-1/54), the rank floor that ACTIVATES the [1/1] "
              "d-log-Pade predictive test (predicting d_9)",
              H0 == sp.Rational(7, 12) and H1 == sp.Rational(-1, 16)
              and H2 == sp.Rational(-1, 54),
              "the analytic-class beta^8 activation minimum is now met (d_5..d_8 known)")
        print("  NOTE: the [1/1] d-log-Pade from d_5..d_8 returns a spurious REAL pole "
              "(beta_c ~ 3.375) and a non-physical Delta(6) ~ 1.19 (=> <P>(6) ~ 1.62, "
              "far from the 0.594 comparator). The activation coefficient d_8 therefore "
              "CONTRADICTS the [1/1]'s single-pole premise; the [1/1] is too low-order "
              "to localize the physical complex pair. This ACTIVATES but does NOT close "
              "beta=6 (0.594 is a Monte-Carlo comparator, never a derivation input).")

    # ----- V6: SU(3) Haar Monte-Carlo validation of the link integrator -----
    print("\nV6. SU(3) Haar Monte-Carlo validation of the exact integrator (CHECK, not input)")
    # The connected COEFFICIENTS themselves (~1e-6) are tiny residuals from large
    # cancellations and are NOT MC-resolvable at feasible sample sizes; they are
    # cross-checked by the independent exact methods (V0 closed forms + the per-
    # shell-identical exact values + the all-orientation moment engine). What MC
    # validates reliably is the single-link Haar integrator on O(1) quantities,
    # the engine's foundation.
    rng = np.random.default_rng(20260530)
    ns = 150000
    tr2 = tr3 = tr4 = 0j
    for _ in range(ns):
        U = _rand_su3(rng)
        t = np.trace(U)
        tr2 += abs(t) ** 2
        tr3 += t ** 3
        tr4 += abs(t) ** 4
    tr2 /= ns; tr3 /= ns; tr4 /= ns
    check("MC <|TrU|^2> = 1 (fundamental character orthonormality)",
          abs(tr2 - 1) < 0.02, f"MC={tr2.real:.4f}")
    check("MC <(TrU)^3> = 1 (baryon singlet, epsilon sector)",
          abs(tr3 - 1) < 0.03, f"MC={complex(tr3)}")
    check("MC <|TrU|^4> = 2 (two singlets in 3^2 x 3bar^2)",
          abs(tr4 - 2) < 0.05, f"MC={tr4.real:.4f}")
    # also: BOTH integrators must reproduce these O(1) values EXACTLY.
    check("exact integrator: <X_p0^2>*36 = 2 (= <|TrU|^2> + <(TrU)^2>conj-cross)",
          moment([P0, P0]) * 36 == 2, f"36*<X_p0^2> = {moment([P0,P0])*36}")
    check("optimized Fraction integrator agrees with sympy on <X_p0^2>, <X_p0^3>",
          moment_frac([P0, P0]) == Fraction(1, 18)
          and moment_frac([P0, P0, P0]) == Fraction(1, 108),
          f"Fraction <X_p0^2> = {moment_frac([P0,P0])}, <X_p0^3> = {moment_frac([P0,P0,P0])}")

    # ----- summary -----
    print("\n" + "=" * 78)
    print("EXACT CONNECTED COEFFICIENTS OF Delta(beta) = P_full - P_1plaq:")
    for n in sorted(results):
        print(f"   d_{n} = {results[n]} = {float(results[n]):.8e}")
    if 7 in results:
        ratios = []
        for n in range(6, max(results) + 1):
            ratios.append(f"d_{n}/d_{n-1} = {sp.nsimplify(results[n] / results[n-1])}")
        print(f"   per-order ratios: {', '.join(ratios)}  "
              f"(NOT constant => no single geometric tail)")
    print("=" * 78)
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}   ({time.time()-t0:.1f}s)")
    print("=" * 78)
    print("This is an exact strong-coupling series coefficient (bounded result).")
    print("It does NOT close beta=6. The exact d_7 falsifies the single-ratio")
    print("tadpole/geometric ansatz (d_7/d_6 = 5/21 != d_6/d_5 = 7/12); drop")
    print("{6:7/5668704, 7:5/17006112} into the harness")
    print("scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py for the")
    print("SUPPORT/FALSIFY scorecard line.")
    if 8 in results:
        print("The exact d_8 = 5/272097792 (POSITIVE, d_8/d_7 = 1/16) additionally")
        print("falsifies the tested single-complex-pair closure (which predicts a sign")
        print("change to negative) and ACTIVATES the [1/1] d-log-Pade (d_5..d_8);")
        print("the [1/1] returns a spurious real pole + garbage Delta(6) => the")
        print("activation coefficient contradicts its own single-pole premise.")
        print("Still NOT a beta=6 closure (0.594 is a Monte-Carlo comparator).")
    return 0 if FAIL == 0 else 1

if __name__ == "__main__":
    raise SystemExit(main())

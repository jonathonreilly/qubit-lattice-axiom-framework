#!/usr/bin/env python3
"""Staggered-Dirac kinetic-class forcing -- two-flux-class collapse + P-SD.

Companion runner for
    docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md

Deterministic, no network, no randomness, runtime << 5 min.

What is computed (nothing load-bearing is asserted without computation):

  [A]  Two-flux-class theorem (kinetic-class collapse).  On the adjacency-licensed
       Q-conserving nearest-neighbor bilinear surface over the qubit-reframe-closed
       per-site C^2, covariance under the lattice automorphism group
       (translations + the 24 proper cubic rotations, each up to
       site-local U(1) frame) collapses the kinetic family to EXACTLY
       TWO frame classes on simply connected regions:
           K0 = flux(+1)  (representative t == 1, scalar tight-binding)
           K1 = flux(-1)  (representative eta^0, Kawamoto-Smit class).
       Certified by: edge/plaquette transitivity, frame invariance of
       flux, the orientation-reversing C2 stabilizer (forces flux real),
       GF(2) cohomology at scale (flux determines the frame class:
       nullity(d1) = rank(d0) on boxes), an exact integer rank
       certificate for the U(1) case, and exhaustive enumeration of all
       2^12 sign systems on the unit cube.

  [B]  Absorbing-frame theorem (P-SD discharge on the K1 branch).  (i) No-spectator:
       CAR(2) is simple with unique 4-dim irrep, so the minimal-Qubit
       one-site qubit carrier C^2 has no room for a per-site 2-component spinor; any
       site-local realization of the naive-Dirac kinetic structure must
       absorb the Cl(3) vector vertex into site-local unitary frames
       (the scalarization condition, derived not declared).
       (ii) Existence: T(x) = s1^x1 s2^x2 s3^x3 absorbs, exactly.
       (iii) Rigidity: gamma anticommutation forces plaquette holonomy
       -1, so the absorption image is exactly K1, never K0.
       (iv) Uniqueness: the absorbing frame is unique up to
       T(x) -> g(x) T(x) V (site-local U(1) gauge x one global frame).

  [C]  Sharpness / countermodel.  K0 (t == 1) passes every imposed
       constraint and every cited separator tested (hermiticity,
       exact translation + 24-rotation covariance, F1 parity grading,
       Q conservation); the frame-invariant flux separates K0 from K1;
       spectral witness: K1 has an L-independent set of 8 isolated
       (Dirac) zeros, K0 an extensive zero surface.  Hence the specified
       constraint set does NOT force K1: the surviving content of P-KIN is exactly
       the one-bit flux selector phi = -1 (the kinetic-order bit).

  [D]  Falsification legs (drop a constraint, the family grows):
       D1 anisotropic flux pattern  -> rejected by cubic covariance;
       D2 uniform complex flux i    -> rejected by cubic covariance;
       D3 NNN hopping               -> adjacency license load-bearing;
       D4 pairing term              -> Q-conserving scope load-bearing;
       D5 spectator surface (qubit-reframe closure dropped): the Wilson family
          M_mu(r) = sigma_mu + r*I is O-equivariant for EVERY r, and
          single-mode absorption kills it for every r != 0; the full
          12-complex-parameter O-equivariant NN family reduces to
          {a*I + b*sigma_mu} (2 params) and absorption collapses it to
          the two rays a=0 / b=0  ==  the two classes of [A].

Exit code 0 iff FAIL == 0.
"""

import re
import sys
from itertools import product
from pathlib import Path

import numpy as np
import sympy as sp

_pass = 0
_fail = 0


def check(num, tag, desc, ok, extra=""):
    global _pass, _fail
    status = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{status}] [{tag}] {num:2d}. {desc}"
    if extra:
        line += f"  |  {extra}"
    print(line)
    return bool(ok)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


# ======================================================================
# shared lattice machinery
# ======================================================================

EYE = sp.eye(2)
S1 = sp.Matrix([[0, 1], [1, 0]])
S2 = sp.Matrix([[0, -sp.I], [sp.I, 0]])
S3 = sp.Matrix([[1, 0], [0, -1]])
SIG = [S1, S2, S3]

E_UNIT = [np.array(v) for v in ((1, 0, 0), (0, 1, 0), (0, 0, 1))]


def cubic_rotations():
    """All 24 proper rotations of the cube, generated from C4z and C3[111]."""
    c4z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    c3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])  # e1->e2->e3->e1
    group = {tuple(np.eye(3, dtype=int).flatten())}
    frontier = [np.eye(3, dtype=int)]
    while frontier:
        nxt = []
        for g in frontier:
            for h in (c4z, c3):
                m = h @ g
                t = tuple(m.flatten())
                if t not in group:
                    group.add(t)
                    nxt.append(m)
        frontier = nxt
    return [np.array(t, dtype=int).reshape(3, 3) for t in sorted(group)]


ROTS = cubic_rotations()


def eta0(x, mu):
    """Kawamoto-Smit sign system: eta_1=1, eta_2=(-1)^x1, eta_3=(-1)^(x1+x2)."""
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0] % 2)
    return (-1) ** ((x[0] + x[1]) % 2)


class PhaseSystem:
    """t_mu(x) on the directed +mu edges of a centered open box
    {-m..m}^3 (simply connected).  Values: python complex (unit phases)."""

    def __init__(self, m, fn):
        self.m = m
        self.t = {}
        rng = range(-m, m + 1)
        for x in product(rng, rng, rng):
            for mu in range(3):
                y = tuple(np.array(x) + E_UNIT[mu])
                if max(abs(c) for c in y) <= m:
                    self.t[(x, mu)] = complex(fn(x, mu))

    def edges(self):
        return self.t.keys()

    def flux(self, x, mu, nu):
        """plaquette x -> x+mu -> x+mu+nu -> x+nu -> x."""
        xa = np.array(x)
        t = self.t
        a = t[(tuple(xa), mu)]
        b = t[(tuple(xa + E_UNIT[mu]), nu)]
        c = t[(tuple(xa + E_UNIT[nu]), mu)]
        d = t[(tuple(xa), nu)]
        return a * b * np.conj(c) * np.conj(d)

    def all_fluxes(self):
        out = {}
        m = self.m
        rng = range(-m, m + 1)
        for x in product(rng, rng, rng):
            for mu in range(3):
                for nu in range(mu + 1, 3):
                    xa = np.array(x)
                    if (max(abs(c) for c in xa + E_UNIT[mu] + E_UNIT[nu]) <= m):
                        out[(x, mu, nu)] = self.flux(x, mu, nu)
        return out

    def gauge(self, g):
        """t'_mu(x) = conj(g(x)) t_mu(x) g(x+mu)."""
        new = PhaseSystem.__new__(PhaseSystem)
        new.m = self.m
        new.t = {}
        for (x, mu), v in self.t.items():
            y = tuple(np.array(x) + E_UNIT[mu])
            new.t[(x, mu)] = np.conj(g(x)) * v * g(y)
        return new

    def rotate(self, R):
        """Pushforward under x -> Rx.  Edge (y,nu) of the image pulls
        back to the (possibly reversed) edge of the source; reversal
        conjugates.  Restricted to edges whose preimages lie in the box."""
        Rinv = np.linalg.inv(R).astype(int)
        new = PhaseSystem.__new__(PhaseSystem)
        new.m = self.m
        new.t = {}
        m = self.m
        rng = range(-m, m + 1)
        for y in product(rng, rng, rng):
            for nu in range(3):
                y2 = np.array(y) + E_UNIT[nu]
                if max(abs(c) for c in y2) > m:
                    continue
                xa = Rinv @ np.array(y)
                d = Rinv @ E_UNIT[nu]
                if max(abs(c) for c in xa) > m or max(abs(c) for c in xa + d) > m:
                    continue
                mu = int(np.flatnonzero(d)[0])
                if d[mu] == 1:
                    key = (tuple(xa), mu)
                    if key in self.t:
                        new.t[(tuple(y), nu)] = self.t[key]
                else:
                    key = (tuple(xa + d), mu)
                    if key in self.t:
                        new.t[(tuple(y), nu)] = np.conj(self.t[key])
        return new


def solve_gauge(sysA, sysB):
    """Find g with sysB = gauge transform of sysA on the common edge set
    (spanning-tree propagation from the origin + full verification).
    Returns dict g or None."""
    common = sorted(set(sysA.t) & set(sysB.t))
    if not common:
        return None
    ratio = {e: sysB.t[e] / sysA.t[e] for e in common}
    g = {(0, 0, 0): 1.0 + 0j}
    # BFS over the undirected graph of common edges
    adj = {}
    for (x, mu) in common:
        y = tuple(np.array(x) + E_UNIT[mu])
        adj.setdefault(x, []).append((y, (x, mu), +1))
        adj.setdefault(y, []).append((x, (x, mu), -1))
    frontier = [(0, 0, 0)]
    while frontier:
        nxt = []
        for v in frontier:
            for (w, e, sgn) in adj.get(v, []):
                if w in g:
                    continue
                # ratio_e = conj(g(x)) g(x+mu)  on edge e=(x,mu)
                if sgn == +1:  # v = x, w = x+mu
                    g[w] = ratio[e] * g[v]
                else:          # v = x+mu, w = x
                    g[w] = g[v] / ratio[e]
                nxt.append(w)
        frontier = nxt
    for (x, mu) in common:
        y = tuple(np.array(x) + E_UNIT[mu])
        if x not in g or y not in g:
            return None
        if abs(np.conj(g[x]) * sysA.t[(x, mu)] * g[y] - sysB.t[(x, mu)]) > 1e-9:
            return None
    if any(abs(abs(v) - 1) > 1e-9 for v in g.values()):
        return None
    return g


# GF(2) machinery on the open box {0..L-1}^3 -----------------------------

def box_complex(L):
    sites = list(product(range(L), repeat=3))
    sidx = {s: i for i, s in enumerate(sites)}
    edges = []
    for x in sites:
        for mu in range(3):
            y = tuple(np.array(x) + E_UNIT[mu])
            if max(y) <= L - 1:
                edges.append((x, mu))
    eidx = {e: i for i, e in enumerate(edges)}
    plaqs = []
    for x in sites:
        for mu in range(3):
            for nu in range(mu + 1, 3):
                y = np.array(x) + E_UNIT[mu] + E_UNIT[nu]
                if max(y) <= L - 1:
                    plaqs.append((x, mu, nu))
    return sites, sidx, edges, eidx, plaqs


def gf2_rank(rows):
    rows = [r for r in rows if r]
    rank = 0
    for bit in range(max(rows).bit_length() if rows else 0):
        piv = None
        for i in range(rank, len(rows)):
            if (rows[i] >> bit) & 1:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i] >> bit) & 1:
                rows[i] ^= rows[rank]
        rank += 1
        rows = [r for r in rows if r]
        if rank >= len(rows):
            break
    return rank


def gf2_matrices(L):
    sites, sidx, edges, eidx, plaqs = box_complex(L)
    d0 = []
    for x in sites:
        row = 0
        for mu in range(3):
            for (base, off) in ((x, 0),):
                pass
        d0.append(row)
    # d0 rows are per-site columns; build as edge-rows of vertex-vectors
    # instead: represent d0 as list over EDGES of vertex-bitmasks
    d0 = []
    for (x, mu) in edges:
        y = tuple(np.array(x) + E_UNIT[mu])
        d0.append((1 << sidx[x]) | (1 << sidx[y]))
    d1 = []
    for (x, mu, nu) in plaqs:
        xa = np.array(x)
        es = [(tuple(xa), mu), (tuple(xa + E_UNIT[mu]), nu),
              (tuple(xa + E_UNIT[nu]), mu), (tuple(xa), nu)]
        row = 0
        for e in es:
            row |= 1 << eidx[e]
        d1.append(row)
    return sites, edges, plaqs, eidx, d0, d1


# ======================================================================
print("=" * 72)
print("staggered-Dirac kinetic-class forcing check  (2026-06-10)")
print("=" * 72)

# ----------------------------------------------------------------------
print("\n--- [S] source dependency guard: U4 renaming is provenance-only")

n = 0
n += 1
note_path = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md"
)
note_text = note_path.read_text(encoding="utf-8")
u4_markdown_dep = re.search(
    r"\]\(U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20\.md\)",
    note_text,
)
u4_yaml_dep = re.search(
    r"(?m)^\s*-\s+u4_closes_under_qubit_reframe_narrow_theorem_note_2026-05-20\s*$",
    note_text,
)
u4_plain_context = (
    "audited-renaming/provenance context for older U4 language only" in note_text
)
minimal_qubit_context = (
    "current minimal Qubit axiom" in note_text and "check 10" in note_text
)
check(
    n,
    "S",
    "source note carries no load-bearing U4 markdown/YAML dependency; "
    "U4 remains plain-text renaming provenance, while the C^2 "
    "no-spectator input is sourced from the minimal Qubit axiom, "
    "retained Cl(3) classification, and CAR(2) dimension check",
    (
        u4_markdown_dep is None
        and u4_yaml_dep is None
        and u4_plain_context
        and minimal_qubit_context
    ),
)

# ----------------------------------------------------------------------
print("\n--- [A] Two-flux-class theorem: two-flux-class collapse on the licensed surface")

n = 0

# A: direction transitivity of the 24 proper rotations
n += 1
dirs = set()
for R in ROTS:
    for s in (+1, -1):
        for mu in range(3):
            dirs.add(tuple(s * (R @ E_UNIT[mu])))
ok = (len(ROTS) == 24 and len(dirs) == 6
      and all(tuple(v) in dirs for v in
              [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0),
               (0, 0, 1), (0, 0, -1)]))
check(n, "A", "lattice automorphisms: 24 proper cubic rotations generated "
              "(C4z, C3[111]); rotations act transitively on the 6 edge "
              "directions, translations on sites => |t| uniform on edges",
      ok, f"|O| = {len(ROTS)}, direction orbit size = {len(dirs)}")

# A: flux is frame-invariant
n += 1
m = 2
sysKS = PhaseSystem(m, eta0)


def gdet(x):
    return 1j ** ((x[0] + 2 * x[1] + 3 * x[2]) % 4)


sysKSg = sysKS.gauge(gdet)
f0 = sysKS.all_fluxes()
f1 = sysKSg.all_fluxes()
ok = all(abs(f0[k] - f1[k]) < 1e-12 for k in f0)
check(n, "A", "plaquette flux is invariant under site-local U(1) frame "
              "change (deterministic complex gauge, all plaquettes, "
              "centered 5^3 box)", ok, f"{len(f0)} plaquettes")

# A: orientation-reversing C2 stabilizer forces flux real
n += 1
phi = 1j


def t_uniform_flux(x, mu):
    if mu == 0:
        return 1
    if mu == 1:
        return phi ** (x[0])
    return phi ** (x[0] + x[1])


sysI = PhaseSystem(m, t_uniform_flux)
fl = sysI.all_fluxes()
uniform_i = all(abs(v - 1j) < 1e-12 for v in fl.values())
C2x = np.diag([1, -1, -1]).astype(int)
sysIr = sysI.rotate(C2x)
flr = sysIr.all_fluxes()
# C2 about e1 reverses the orientation of every plaquette whose plane
# CONTAINS the axis (plane classes (e1,e2) and (e1,e3)) and preserves the
# orientation of the perpendicular class (e2,e3):
conj_ok = True
for k, v in flr.items():
    x, mu, nu = k
    if 0 in (mu, nu):  # axis-containing plane: orientation reversed
        conj_ok = conj_ok and abs(v - np.conj(fl[k])) < 1e-12
    else:              # perpendicular plane: orientation preserved
        conj_ok = conj_ok and abs(v - fl[k]) < 1e-12
mismatch = any(abs(flr[k] - fl[k]) > 1e-12 for k in flr)
no_gauge = solve_gauge(sysI, sysIr) is None
check(n, "A", "C2 rotation about e1 reverses the orientation of every "
              "axis-containing plaquette (pushforward flux i -> -i there), "
              "so covariance up to frame requires phi = conj(phi): cubic "
              "covariance forces flux real, phi in {+1,-1}; the uniform "
              "flux-i witness is rejected (no gauge to its own C2 image)",
      uniform_i and conj_ok and mismatch and no_gauge,
      "axis-containing planes conjugated, perpendicular plane preserved")

# A: GF(2) cohomology at scale -- flux pattern determines the frame class
for L in (2, 3, 4):
    n += 1
    sites, edges, plaqs, eidx, d0rows, d1rows = gf2_matrices(L)
    rk_d1 = gf2_rank(list(d1rows))
    rk_d0 = gf2_rank(list(d0rows))
    nullity_d1 = len(edges) - rk_d1
    # eta^0 exponent vector solves d1 e = all-ones (flux -1 everywhere)
    e_ks = 0
    for (x, mu) in edges:
        if eta0(x, mu) == -1:
            e_ks |= 1 << eidx[(x, mu)]
    all_minus = all(
        bin(row & e_ks).count("1") % 2 == 1 for row in d1rows)
    ok = (nullity_d1 == rk_d0) and all_minus and rk_d0 == len(sites) - 1
    check(n, "A", f"GF(2) cohomology on the {L}^3 box: nullity(d1) = "
                  f"rank(d0) (= |V|-1), so each flux pattern carries EXACTLY "
                  f"one frame class; eta^0 realizes the all-(-1) pattern",
          ok, f"V={len(sites)} E={len(edges)} P={len(plaqs)} "
              f"rank(d1)={rk_d1} rank(d0)={rk_d0}")

# A: U(1) certificate on the unit cube (integer linear algebra, exact)
n += 1
sites, edges, plaqs, eidx, d0rows, d1rows = gf2_matrices(2)
# integer boundary matrix d1 (plaquettes x edges) with orientation signs
D1 = sp.zeros(len(plaqs), len(edges))
for p, (x, mu, nu) in enumerate(plaqs):
    xa = np.array(x)
    D1[p, eidx[(tuple(xa), mu)]] += 1
    D1[p, eidx[(tuple(xa + E_UNIT[mu]), nu)]] += 1
    D1[p, eidx[(tuple(xa + E_UNIT[nu]), mu)]] -= 1
    D1[p, eidx[(tuple(xa), nu)]] -= 1
D0 = sp.zeros(len(edges), len(sites))
sidx = {s: i for i, s in enumerate(sites)}
for e, (x, mu) in enumerate(edges):
    y = tuple(np.array(x) + E_UNIT[mu])
    D0[e, sidx[x]] -= 1
    D0[e, sidx[y]] += 1
rkD1 = D1.rank()
rkD0 = D0.rank()
ok = (rkD1 == 5 and rkD0 == 7 and len(edges) - rkD1 == rkD0
      and (D1 * D0).is_zero_matrix)
check(n, "A", "U(1) case, unit cube, exact integer certificate: "
              "rank(d1)=5, rank(d0)=7, d1*d0=0, nullity(d1)=rank(d0): "
              "U(1) phase systems are classified by their fluxes up to "
              "frame; with flux uniform and real => exactly two classes",
      ok, f"E={len(edges)} rank(d1)={rkD1} rank(d0)={rkD0}")

# A: exhaustive enumeration of all 2^12 sign systems on the unit cube
n += 1
nE = len(edges)
nP = len(plaqs)
plaq_masks = d1rows
cnt_plus = cnt_minus = cnt_other = 0
ks_vec = 0
for e, (x, mu) in enumerate(edges):
    if eta0(x, mu) == -1:
        ks_vec |= 1 << e
ks_in_minus = False
for v in range(1 << nE):
    fluxes = [bin(rowmask & v).count("1") % 2 for rowmask in plaq_masks]
    if all(f == 0 for f in fluxes):
        cnt_plus += 1
    elif all(f == 1 for f in fluxes):
        cnt_minus += 1
        if v == ks_vec:
            ks_in_minus = True
    else:
        cnt_other += 1
# gauge orbit size = 2^rank(d0) = 128 -> each uniform bucket is ONE orbit
orbit = 1 << gf2_rank(list(d0rows))
ok = (cnt_plus == 128 and cnt_minus == 128 and cnt_other == 3840
      and orbit == 128 and ks_in_minus)
check(n, "A", "exhaustive: all 4096 sign systems on the unit cube; uniform "
              "flux(+1): 128 = one gauge orbit; uniform flux(-1): 128 = one "
              "gauge orbit (contains eta^0); 3840 non-uniform rejected by "
              "covariance", ok,
      f"counts = ({cnt_plus}, {cnt_minus}, {cnt_other}), orbit = {orbit}")

# A: both representatives realize their class
n += 1
sys1 = PhaseSystem(m, lambda x, mu: 1)
fl1 = sys1.all_fluxes()
flK = sysKS.all_fluxes()
ok = (all(abs(v - 1) < 1e-12 for v in fl1.values())
      and all(abs(v + 1) < 1e-12 for v in flK.values()))
check(n, "A", "representatives: t==1 has flux +1 on every plaquette; "
              "eta^0 has flux -1 on every plaquette (centered 5^3 box) "
              "=> both classes are realized; Two-flux-class theorem: EXACTLY TWO "
              "kinetic classes", ok)

residual("Two-flux-class theorem is stated on simply connected regions; finite tori "
         "carry extra wrap-holonomy data (PBC/APBC conventions) -- "
         "boundary B-H, mirroring the Kawamoto-Smit note's B4.")
residual("surface scope: Q-conserving nearest-neighbor bilinears "
         "(adjacency-licensed kinetic surface).  Legs D3/D4 show NN and "
         "Q-conservation are load-bearing scope declarations, not "
         "derived exclusions.")

# ----------------------------------------------------------------------
print("\n--- [B] Absorbing-frame theorem: P-SD discharged on the flux(-1) branch")

_B_results = []

# B: CAR(2) needs per-site dim 4 -- no spectator spinor on the minimal-Qubit C^2 carrier
n += 1
# JW rep of two modes on C^4
a1 = sp.Matrix(np.kron(np.array([[0, 1], [0, 0]]), np.eye(2)))
a2 = sp.Matrix(np.kron(np.array([[1, 0], [0, -1]]),
                       np.array([[0, 1], [0, 0]])))
car_ok = ((a1 * a2 + a2 * a1).is_zero_matrix
          and (a1 * a1).is_zero_matrix and (a2 * a2).is_zero_matrix
          and (a1 * a1.H + a1.H * a1 - sp.eye(4)).is_zero_matrix
          and (a2 * a2.H + a2.H * a2 - sp.eye(4)).is_zero_matrix
          and (a1 * a2.H + a2.H * a1).is_zero_matrix)
# generated *-algebra spans all of M_4(C)
gens = [sp.eye(4), a1, a2, a1.H, a2.H]
basis = []
frontier = list(gens)
seen_words = list(gens)
for _ in range(4):
    new = []
    for w in seen_words:
        for g in gens:
            new.append(w * g)
    seen_words = new
    frontier += new
    if len(frontier) > 400:
        break
vecs = [sp.Matrix(w).reshape(16, 1) for w in frontier]
Mb = sp.Matrix.hstack(*vecs)
dim_alg = Mb.rank()
ok = car_ok and dim_alg == 16
_B_results.append(check(n, "B", "no-spectator lemma: CAR(2) is exactly verified on C^4 and "
              "generates the full M_4(C) (dim 16, simple => unique faithful "
              "irrep has dim 4 > 2): the minimal-Qubit per-site C^2 "
              "carries NO 2-component spinor; site-local frame absorption "
              "(the P-SD scalarization) is the only site-local route",
      ok, f"computed algebra dim = {dim_alg}"))

# B: canonical absorption exists, exactly
n += 1
def Tmat(x):
    out = sp.eye(2)
    for mu, p in enumerate(x):
        out = out * (SIG[mu] ** (p % 2))
    return out


ok = True
for x in product(range(-1, 2), repeat=3):
    for mu in range(3):
        y = tuple(np.array(x) + E_UNIT[mu])
        lhs = sp.simplify(Tmat(x).H * SIG[mu] * Tmat(y))
        if not (lhs - eta0(x, mu) * EYE).is_zero_matrix:
            ok = False
_B_results.append(check(n, "B", "existence: T(x) = s1^x1 s2^x2 s3^x3 absorbs the Cl(3) vector "
              "vertex site-locally: T(x)^dag sigma_mu T(x+mu) = "
        "eta^0_mu(x) I exactly (3^3 window, all directions, sympy)",
      ok))

# B: rigidity -- absorbed holonomy is -1, always
n += 1
ok = True
for mu in range(3):
    for nu in range(3):
        if mu != nu:
            w = sp.simplify(SIG[nu] * SIG[mu] * SIG[nu] * SIG[mu])
            if not (w + EYE).is_zero_matrix:
                ok = False
_B_results.append(check(n, "B", "rigidity: gamma anticommutation forces plaquette holonomy "
              "sigma_nu sigma_mu sigma_nu sigma_mu = -I for every pair: "
              "EVERY absorption of the Cl(3) hopping lands in the "
              "flux(-1) class K1; absorption into K0 (flux +1) is "
              "impossible (flux is frame-invariant, check [A]2)", ok))

# B: uniqueness -- stabilizer of the scalarization is g(x) * T(x) * V
n += 1
s00, s01, s10, s11 = sp.symbols("s00 s01 s10 s11", complex=True)
S0 = sp.Matrix([[s00, s01], [s10, s11]])
# propagation consistency: the two paths to x+mu+nu agree identically
consist = True
for mu in range(3):
    for nu in range(mu + 1, 3):
        lhs = sp.expand(SIG[mu] * (SIG[nu] * S0 * SIG[nu]) * SIG[mu])
        rhs = sp.expand(SIG[nu] * (SIG[mu] * S0 * SIG[mu]) * SIG[nu])
        if not sp.simplify(lhs - rhs).is_zero_matrix:
            consist = False
# closed form: S(x) = T(x) S(0) T(x)^dag solves S(x+mu) = sigma_mu S(x) sigma_mu
closed = True
for x in product(range(0, 2), repeat=3):
    Sx = Tmat(x) * S0 * Tmat(x).H
    for mu in range(3):
        y = tuple(np.array(x) + E_UNIT[mu])
        Sy = Tmat(y) * S0 * Tmat(y).H
        if not sp.simplify(Sy - SIG[mu] * Sx * SIG[mu]).is_zero_matrix:
            closed = False
ok = consist and closed
_B_results.append(check(n, "B", "uniqueness: any two absorbing frames with the same phases "
              "differ by S(x) with S(x+mu) = sigma_mu S(x) sigma_mu; the "
              "general solution is exactly S(x) = T(x) V T(x)^dag (4 "
              "complex parameters = one global frame V), i.e. "
              "T'(x) = T(x) V; with the U(1) gauge g(x) this is the full "
              "stabilizer T -> g(x) T V", ok))

# B: gauge freedom moves eta within the class (one explicit example)
n += 1
gz2 = lambda x: (-1) ** (x[0] % 2)
sysKSg2 = sysKS.gauge(gz2)
flg = sysKSg2.all_fluxes()
ok = (all(abs(v + 1) < 1e-12 for v in flg.values())
      and solve_gauge(sysKS, sysKSg2) is not None)
_B_results.append(check(n, "B", "the local U(1)/Z2 gauge freedom moves the absorbed phase "
              "system within K1 (example g(x)=(-1)^x1: fluxes all -1, "
              "gauge function recovered)", ok))

n += 1
check(n, "B", "Absorbing-frame theorem assembled: P-SD holds as a THEOREM on the K1 "
              "branch -- the absorbing frame exists, is unique up to "
              "site-local gauge x one global frame, and its image is "
              "exactly the flux(-1) class", all(_B_results),
      f"B-section results = {_B_results}")

residual("Absorbing-frame theorem derives P-SD GIVEN the K1 branch of Two-flux-class theorem; "
         "non-site-local realizations (blocked/thinned multi-site "
         "spinors) are outside the site-local scope and remain the "
         "declared boundary B-SL.")

# ----------------------------------------------------------------------
print("\n--- [C] sharpness: the flux(+1) countermodel (P-KIN residual bit)")


def torus_hop(L, tfun):
    """single-particle hopping matrix on the L^3 torus (PBC)."""
    sites = list(product(range(L), repeat=3))
    sidx = {s: i for i, s in enumerate(sites)}
    h = np.zeros((L ** 3, L ** 3), dtype=complex)
    for x in sites:
        for mu in range(3):
            y = tuple((np.array(x) + E_UNIT[mu]) % L)
            h[sidx[y], sidx[x]] += tfun(x, mu)
            h[sidx[x], sidx[y]] += np.conj(tfun(x, mu))
    return h, sites, sidx


L = 4
h0, sites4, sidx4 = torus_hop(L, lambda x, mu: 1.0)
h1, _, _ = torus_hop(L, eta0)

# C: K0 passes hermiticity + exact translation + all 24 rotations
n += 1
herm = np.allclose(h0, h0.conj().T)
ok = herm
for a in range(3):
    P = np.zeros((L ** 3, L ** 3))
    for s in sites4:
        y = tuple((np.array(s) + E_UNIT[a]) % L)
        P[sidx4[y], sidx4[s]] = 1
    ok = ok and np.allclose(P @ h0 @ P.T, h0)
for R in ROTS:
    PR = np.zeros((L ** 3, L ** 3))
    for s in sites4:
        y = tuple((R @ np.array(s)) % L)
        PR[sidx4[y], sidx4[s]] = 1
    ok = ok and np.allclose(PR @ h0 @ PR.T, h0)
check(n, "C", "countermodel K0 (t==1, scalar tight-binding) passes every "
              "imposed constraint: Hermitian, exactly translation "
              "invariant, exactly invariant under all 24 rotations "
              "(4^3 torus)", ok)

# C: K1 passes the same constraints up to frame
n += 1
ks_shift_ok = True
g1 = {s: (-1) ** ((s[1] + s[2]) % 2) for s in sites4}
for x in sites4:
    for mu in range(3):
        y = tuple((np.array(x) + E_UNIT[mu]) % L)
        lhs = eta0(tuple((np.array(x) + E_UNIT[0]) % L), mu)
        rhs = g1[x] * eta0(x, mu) * g1[y]
        if lhs != rhs:
            ks_shift_ok = False
# rotation covariance up to frame, on the simply connected centered box
rot_ok = True
for R in ROTS:
    img = sysKS.rotate(R)
    flx = img.all_fluxes()
    if not all(abs(v + 1) < 1e-12 for v in flx.values()):
        rot_ok = False
        continue
    if solve_gauge(sysKS, img) is None:
        rot_ok = False
check(n, "C", "K1 (eta^0) passes the same constraints up to frame: "
              "translation by e1 implemented by g(x)=(-1)^(x2+x3) "
              "(exact, torus); all 24 rotation images have flux -1 and an "
              "explicit gauge function on the centered box",
      ks_shift_ok and rot_ok)

# C: cited fermion-parity grading does not separate
n += 1
def fock_ops(nsites):
    dims = 2 ** nsites
    aa = []
    for i in range(nsites):
        ops = [np.eye(2)] * nsites
        mat = np.array([[0, 1], [0, 0]])
        z = np.array([[1, 0], [0, -1]])
        facs = [z] * i + [mat] + [np.eye(2)] * (nsites - i - 1)
        out = np.array([[1.0]])
        for f in facs:
            out = np.kron(out, f)
        aa.append(out)
    return aa


cells = list(product(range(2), range(2), range(1)))
cidx = {c: i for i, c in enumerate(cells)}
aa = fock_ops(len(cells))
Q = sum(a.conj().T @ a for a in aa)
F = np.diag((-1.0) ** np.round(np.diag(Q)).real)
edges22 = []
for c in cells:
    for mu in range(2):
        y = tuple((np.array(c) + E_UNIT[mu])[:3])
        y = (y[0] % 2, y[1] % 2, 0)
        if y != c:
            edges22.append((c, y, mu))
H0F = sum(aa[cidx[y]].conj().T @ aa[cidx[c]]
          + aa[cidx[c]].conj().T @ aa[cidx[y]] for (c, y, mu) in edges22)
H1F = sum(eta0(c, mu) * (aa[cidx[y]].conj().T @ aa[cidx[c]]
          + aa[cidx[c]].conj().T @ aa[cidx[y]]) for (c, y, mu) in edges22)
ok = (np.allclose(F @ H0F, H0F @ F) and np.allclose(F @ H1F, H1F @ F)
      and np.allclose(H0F @ Q, Q @ H0F) and np.allclose(H1F @ Q, Q @ H1F))
check(n, "C", "fermion-parity grading does NOT separate the "
              "classes: both Fock bilinears commute with (-1)^Q and with "
              "Q (2x2 cell, exact to machine precision)", ok)

# C: the frame-invariant flux separates the classes
n += 1
ok = solve_gauge(sys1, sysKS) is None
check(n, "C", "K0 and K1 are NOT frame-equivalent: fluxes +1 vs -1 on "
              "every plaquette (frame-invariant), and no gauge function "
              "exists (spanning-tree search fails)", ok)

# C: spectral witness -- isolated Dirac zeros vs extensive zero surface
n += 1
zero_counts = {}
for LL in (4, 8):
    hh0, _, _ = torus_hop(LL, lambda x, mu: 1.0)
    hh1, _, _ = torus_hop(LL, eta0)
    e0 = np.linalg.eigvalsh(hh0)
    e1 = np.linalg.eigvalsh(hh1)
    zero_counts[LL] = (int(np.sum(np.abs(e0) < 1e-9)),
                       int(np.sum(np.abs(e1) < 1e-9)))
(z0_4, z1_4), (z0_8, z1_8) = zero_counts[4], zero_counts[8]
ok = (z1_4 == z1_8 == 8 and z0_8 > z0_4 > 8)
check(n, "C", "spectral witness: K1 has exactly 8 zero modes at L=4 AND "
              "L=8 (isolated Dirac points, L-independent); K0 has an "
              "extensive zero set (grows with L): the two classes are "
              "physically distinct kinetic orders", ok,
      f"zeros: K0 (L=4,8) = ({z0_4},{z0_8}); K1 (L=4,8) = ({z1_4},{z1_8})")

residual("P-KIN residual: the one-bit flux selector phi = -1 (equivalently "
         "the first-order/Dirac kinetic order) is NOT forced by the "
         "specified constraint set -- K0 is the computed countermodel.  This is the "
         "same residual the index-pairing no-go names as the "
         "kinetic-order selector; the RP authority is "
         "staggered-scoped and cannot select the class without "
         "circularity.")

# ----------------------------------------------------------------------
print("\n--- [D] falsification legs: drop a constraint, the family grows")

# D1: anisotropic flux pattern admissible without cubic covariance
n += 1
def t_aniso(x, mu):
    return (-1) ** (x[0] % 2) if mu == 1 else 1


sysA = PhaseSystem(m, t_aniso)
flA = sysA.all_fluxes()
pat = {}
for (x, mu, nu), v in flA.items():
    pat.setdefault((mu, nu), set()).add(round(v.real))
aniso_ok = (pat[(0, 1)] == {-1} and pat[(0, 2)] == {1} and pat[(1, 2)] == {1})
C3m = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
sysAr = sysA.rotate(C3m)
rej = solve_gauge(sysA, sysAr) is None
check(n, "D", "drop cubic covariance: anisotropic pattern (flux -1 on "
              "(1,2)-plaquettes only) is Hermitian + translation-covariant "
              "but its C3[111] image is not frame-equivalent => rejected "
              "only by [A]; without it the family grows", aniso_ok and rej)

# D2: uniform complex flux admissible without cubic covariance
n += 1
trans_ok = True
for a in range(3):
    sh = PhaseSystem(m, lambda x, mu, a=a: t_uniform_flux(
        tuple(np.array(x) + E_UNIT[a]), mu))
    common_ok = solve_gauge(sysI, sh) is not None
    trans_ok = trans_ok and common_ok
check(n, "D", "drop cubic covariance: uniform flux i (Landau-type) is "
              "Hermitian + translation-covariant up to frame (all three "
              "axes, gauge functions found) but fails the C2 reality "
              "test of [A]3 => a U(1) continuum of classes appears",
      trans_ok and uniform_i)

# D3: drop the adjacency (NN) license -> NNN family
n += 1
nnn = set()
for R in ROTS:
    v = R @ (E_UNIT[0] + E_UNIT[1])
    nnn.add(tuple(v))
ok = len(nnn) == 12
hNNN = np.zeros((4 ** 3, 4 ** 3))
sites_, sidx_ = sites4, sidx4
for x in sites_:
    for v in nnn:
        y = tuple((np.array(x) + np.array(v)) % 4)
        hNNN[sidx_[y], sidx_[x]] += 0.5
for R in ROTS:
    PR = np.zeros((4 ** 3, 4 ** 3))
    for s in sites_:
        y = tuple((R @ np.array(s)) % 4)
        PR[sidx_[y], sidx_[s]] = 1
    ok = ok and np.allclose(PR @ hNNN @ PR.T, hNNN)
ok = ok and np.allclose(hNNN, hNNN.conj().T) and np.linalg.norm(hNNN) > 0
check(n, "D", "drop the adjacency license: the 12-vector NNN hopping is "
              "Hermitian and exactly cubic+translation invariant => "
              "on the enlarged surface a (t, t') continuum survives; "
              "the Lattice-axiom NN license is load-bearing", ok)

# D4: drop Q-conservation -> pairing terms
n += 1
# one term per unordered pair with a fixed orientation (the two
# orientations of the same pair would cancel by anticommutation)
pairs22 = sorted({tuple(sorted((c, y))) for (c, y, mu) in edges22})
Hp = sum(aa[cidx[v]] @ aa[cidx[u]] + (aa[cidx[v]] @ aa[cidx[u]]).conj().T
         for (u, v) in pairs22)
ok = (np.allclose(Hp, Hp.conj().T) and np.linalg.norm(Hp) > 1e-9
      and not np.allclose(Hp @ Q, Q @ Hp)
      and np.allclose(F @ Hp, Hp @ F))
check(n, "D", "drop Q-conservation: the NN pairing bilinear is Hermitian, "
              "parity-even, nonzero, and does not conserve Q => outside "
              "the declared surface; the Q-conserving scope is "
              "load-bearing, not derived", ok)

# D5a: Wilson family is O-equivariant for every r (spectator surface)
n += 1
r = sp.symbols("r", real=True)
Vc4 = sp.cos(sp.pi / 4) * EYE - sp.I * sp.sin(sp.pi / 4) * S3
Vc3 = sp.cos(sp.pi / 3) * EYE - sp.I * sp.sin(sp.pi / 3) * (S1 + S2 + S3) / sp.sqrt(3)
M = [SIG[k] + r * EYE for k in range(3)]
# C4z: 1 -> 2, 2 -> -1, 3 -> 3 ; M_{-mu} on the spectator surface = M_mu^dag
eq1 = sp.simplify(Vc4 * M[0] * Vc4.H - M[1]).is_zero_matrix
eq2 = sp.simplify(Vc4 * M[1] * Vc4.H - (M[0].H).subs(sp.conjugate(r), r)
                  ).is_zero_matrix
eq2 = sp.simplify(Vc4 * M[1] * Vc4.H - (-SIG[0] + r * EYE)).is_zero_matrix
eq3 = sp.simplify(Vc4 * M[2] * Vc4.H - M[2]).is_zero_matrix
eq4 = sp.simplify(Vc3 * M[0] * Vc3.H - M[1]).is_zero_matrix
eq5 = sp.simplify(Vc3 * M[1] * Vc3.H - M[2]).is_zero_matrix
eq6 = sp.simplify(Vc3 * M[2] * Vc3.H - M[0]).is_zero_matrix
check(n, "D", "drop qubit-reframe closure (2-modes/site spectator surface): the Wilson family "
              "M_mu(r) = sigma_mu + r I is O-equivariant under the spin "
              "lift for EVERY real r (C4z and C3[111] checked exactly): "
              "a one-parameter continuum of kinetic classes survives "
              "all spectator-surface symmetry constraints",
      all([eq1, eq2, eq3, eq4, eq5, eq6]))

# D5b: single-mode absorption kills the Wilson continuum
n += 1
MtM = sp.expand((SIG[0] + r * EYE).H * (SIG[0] + r * EYE))
off = sp.simplify(MtM[0, 1])
sols = sp.solve(sp.Eq(off, 0), r)
prop_unitary_only_r0 = (sols == [0])
comm = sp.expand(M[0] * M[1] - M[1] * M[0])
comm_zero_only_r_any = sp.simplify(comm - 2 * sp.I * S3).is_zero_matrix
lam = sp.symbols("lam")
proj = sp.expand(M[0] * M[1] - lam * M[1] * M[0])
sols_proj = sp.solve([proj[0, 0], proj[0, 1], proj[1, 0], proj[1, 1]],
                     [r, lam], dict=True)
proj_only = all(s.get(r, 0) == 0 for s in sols_proj)
check(n, "D", "single-mode absorption (qubit-reframe) kills the Wilson "
              "continuum: M(r) is proportional-to-unitary iff r = 0, and "
              "the projective plaquette commutation M_mu M_nu = "
              "lam M_nu M_mu has scalar solutions only at r = 0 "
              "(lam = -1): the continuum collapses to its endpoints",
      prop_unitary_only_r0 and comm_zero_only_r_any and proj_only,
      f"solve(off-diag=0) = {sols}, projective sols = {sols_proj}")

# D5c: full 12-parameter O-equivariant reduction on the spectator surface
n += 1
cs = sp.symbols("c0:12", complex=True)
Ms = []
for k in range(3):
    Ms.append(cs[4 * k] * EYE + cs[4 * k + 1] * S1
              + cs[4 * k + 2] * S2 + cs[4 * k + 3] * S3)
eqs = []
# C3: M_1 -> M_2 -> M_3 -> M_1
for k in range(3):
    Dm = sp.expand(Vc3 * Ms[k] * Vc3.H - Ms[(k + 1) % 3])
    eqs += [Dm[i, j] for i in range(2) for j in range(2)]
# C4z: M_1 -> M_2,  M_3 -> M_3, and M_2 -> M_{-1} = reversed edge.
# On the spectator surface the reversed-edge matrix of M = a I + b.sigma
# is a I - b_perp.sigma ... encode via the exact pushforward used in [A]:
# the reversed +1 edge carries M_1^dag with conjugated coefficients; to
# stay in the holomorphic linear system use the C2 about z (proper, maps
# 1 -> -1, 2 -> -2, 3 -> 3) combined with C4z twice; equivariance under
# the generated group is captured by C3 above plus C4z^2 (= C2z):
Vc2z = sp.simplify(Vc4 * Vc4)
for k, tgt in ((2, 2),):
    Dm = sp.expand(Vc2z * Ms[k] * Vc2z.H - Ms[tgt])
    eqs += [Dm[i, j] for i in range(2) for j in range(2)]
# C2z: M_1 -> M_{-1}: reversed edge => Hermitian-conjugate hopping matrix.
# Imposing the reversed-edge identification M_{-mu} = M_mu^dag together
# with C2z gives the antiholomorphic constraint V M_1 V^dag = M_1^dag.
# Split into real/imaginary parts: write c = u + i v.
us = sp.symbols("u0:12", real=True)
vs = sp.symbols("v0:12", real=True)
subs_ri = {cs[i]: us[i] + sp.I * vs[i] for i in range(12)}
eqs_ri = []
for e in eqs:
    e2 = sp.expand(e.subs(subs_ri))
    eqs_ri += [sp.re(e2), sp.im(e2)]
Mrev = sp.expand((Vc2z * Ms[0] * Vc2z.H).subs(subs_ri))
M1dag = sp.expand(Ms[0].subs(subs_ri)).H
Dm = sp.expand(Mrev - M1dag)
for i in range(2):
    for j in range(2):
        e2 = sp.expand(Dm[i, j])
        eqs_ri += [sp.re(e2), sp.im(e2)]
allvars = list(us) + list(vs)
Amat, _b = sp.linear_eq_to_matrix(eqs_ri, allvars)
null = Amat.nullspace()
dim_family = len(null)
# verify the surviving family is exactly {a I + b sigma_mu}, a real, b real*i?
# expected: 2 real parameters after the reversed-edge reality constraint
sol_basis = []
for nv in null:
    coeffs = {allvars[i]: nv[i] for i in range(24)}
    Msol = [sp.expand(Ms[k].subs(subs_ri).subs(coeffs)) for k in range(3)]
    sol_basis.append(Msol)
diag_form = True
reality_form = True
for Msol in sol_basis:
    for k in range(3):
        c_id = sp.simplify(sp.trace(Msol[k]) / 2)
        c_sg = sp.simplify(sp.trace(SIG[k] * Msol[k]) / 2)
        rem = sp.expand(Msol[k] - c_id * EYE - c_sg * SIG[k])
        if not rem.is_zero_matrix:
            diag_form = False
        # reversed-edge Hermiticity forces a real (scalar ray) and
        # b purely imaginary (Dirac ray: hopping vertex prop to i*sigma_mu)
        if sp.im(c_id) != 0 or sp.re(c_sg) != 0:
            reality_form = False
check(n, "D", "full reduction: the 12-complex-parameter NN family {M_mu} "
              "under O-equivariance (C3, C2z) + reversed-edge Hermiticity "
              "collapses to M_mu = a I + i b sigma_mu (a, b real: the "
              "scalar ray and the Dirac ray, 2 real parameters); with "
              "[D]26 the single-mode constraint then leaves exactly the "
              "two rays a=0 (Cl(3) vector = K1) and b=0 (scalar = K0) -- "
              "the same two classes as Two-flux-class theorem",
      dim_family == 2 and diag_form and reality_form,
      f"surviving real dimension = {dim_family}")

residual("the kinetic surface is the bilinear (quadratic) sector by the "
         "definition of 'kinetic term'; quartic and higher interaction "
         "terms are out of scope here.")

# ----------------------------------------------------------------------
print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
if _fail == 0:
    print("VERDICT: Two-flux-class theorem (two-flux-class collapse) and Absorbing-frame theorem")
    print("         (P-SD discharged on the flux(-1) branch) VERIFIED on")
    print("         the finite instantiation; the flux(+1) countermodel")
    print("         certifies that the final one-bit kinetic-order")
    print("         selector is NOT forced by the specified constraint set.")
sys.exit(0 if _fail == 0 else 1)

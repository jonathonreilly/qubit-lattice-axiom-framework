"""Forcing certificate for the Kawamoto-Smit phase gauge class.

Companion: docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md
Loop: staggered-dirac-realization-gate-20260507
Role: staggered-Dirac substep 2

What this runner certifies (2026-06-10 science-fix; supersedes the older
instantiate-and-check runner, which only verified the canonical solution
plus one gauge transform and therefore certified consistency, not forcing):

A. Canonical construction (exact sympy, retained from the original runner):
   T(x) = sigma_1^{x_1} sigma_2^{x_2} sigma_3^{x_3} scalarizes
   T(x)^dag sigma_mu T(x+mu) = eta^0_mu(x) I_2 with the Kawamoto-Smit
   phases eta^0_1 = 1, eta^0_2 = (-1)^{x_1}, eta^0_3 = (-1)^{x_1+x_2},
   on all 8 sites x 3 directions of the unit cell; omega = i I_2.

B. Exhaustive forcing certificate (Theorem 2(i)-(ii) on the unit cube):
   enumerate ALL 2^12 = 4096 sign systems on the 12 edges of the
   {0,1}^3 box and DECIDE scalarizability for each by the explicit
   path-product transport construction (Lemma 3): set T(0)=I, transport
   T along edges via T(x+mu) = eta_mu(x) sigma_mu T(x), then check the
   scalarization condition on every edge. Certify:
     - exactly 128 = 2^7 sign systems are scalarizable;
     - the scalarizable set EQUALS the set satisfying the Clifford -1
       plaquette cocycle (the iff of Theorem 2(i));
     - the scalarizable set EQUALS the Z2 gauge orbit of eta^0
       (exactly one gauge class, Theorem 2(ii)); -eta^0 is the
       epsilon-gauge transform of eta^0 and lies in the same class.

C. GF(2) cohomology certificate at scale (L = 3, 4, 5 boxes):
   over GF(2), solutions of the -1 cocycle form the affine space
   e^0 + ker(d1) and Z2 gauge orbits are cosets of im(d0); the runner
   computes rank(d1) by GF(2) elimination and certifies
   nullity(d1) = |V| - 1 = rank(d0), hence exactly one gauge class,
   and that eta^0 satisfies every plaquette condition at scale.

D. Falsification legs: the all-plus sign system and all 12 single-edge
   perturbations of eta^0 are rejected by the transport decision
   procedure on the unit cube; a flipped interior edge on the 4^3 box
   violates the cocycle at scale.

E. Gauge remarks: a nontrivial Z2 gauge transform of eta^0 scalarizes
   with T'(x) = g(x) T(x) and the gauge function is recovered by path
   products (Remark R3 / Lemma 4 transport); the argument runs verbatim
   in U(1) — a complex local phase gauge transform scalarizes and the
   recovery returns the same real representative eta^0 (Remark R2).

Deterministic, no network, no randomness. Exit code 0 iff FAIL = 0.
"""
from __future__ import annotations

from collections import deque
from itertools import product
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

import sympy as sp

Vec = Tuple[int, int, int]
Mat = Tuple[Tuple[complex, complex], Tuple[complex, complex]]

# ----------------------------------------------------------------------
# Exact 2x2 matrix arithmetic over Gaussian integers (Python complex on
# small integer values is exact; all entries stay in {0, +-1, +-i}).
# ----------------------------------------------------------------------

I2: Mat = ((1 + 0j, 0j), (0j, 1 + 0j))
S1: Mat = ((0j, 1 + 0j), (1 + 0j, 0j))
S2: Mat = ((0j, -1j), (1j, 0j))
S3: Mat = ((1 + 0j, 0j), (0j, -1 + 0j))
SIGMA: Dict[int, Mat] = {1: S1, 2: S2, 3: S3}


def mat_mul(a: Mat, b: Mat) -> Mat:
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def mat_dag(a: Mat) -> Mat:
    return (
        (a[0][0].conjugate(), a[1][0].conjugate()),
        (a[0][1].conjugate(), a[1][1].conjugate()),
    )


def mat_scale(c: complex, a: Mat) -> Mat:
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def neighbor(x: Vec, mu: int) -> Vec:
    return (x[0] + (mu == 1), x[1] + (mu == 2), x[2] + (mu == 3))


def canonical_eta(x: Vec, mu: int) -> int:
    """Kawamoto-Smit representative eta^0."""
    if mu == 1:
        return 1
    if mu == 2:
        return (-1) ** x[0]
    return (-1) ** (x[0] + x[1])


def epsilon(x: Vec) -> int:
    """Sublattice parity (-1)^{x_1+x_2+x_3}."""
    return (-1) ** (x[0] + x[1] + x[2])


# ----------------------------------------------------------------------
# Box combinatorics: vertices {0..L-1}^3, edges, plaquettes.
# ----------------------------------------------------------------------

def box_vertices(L: int) -> List[Vec]:
    return [(a, b, c) for a in range(L) for b in range(L) for c in range(L)]


def box_edges(L: int) -> List[Tuple[Vec, int]]:
    verts = set(box_vertices(L))
    return [(x, mu) for x in box_vertices(L) for mu in (1, 2, 3)
            if neighbor(x, mu) in verts]


def box_plaquettes(L: int) -> List[Tuple[Vec, int, int]]:
    """Plaquettes (x, mu, nu) with mu < nu and all four edges inside the box."""
    verts = set(box_vertices(L))
    plaqs = []
    for x in box_vertices(L):
        for mu in (1, 2, 3):
            for nu in (1, 2, 3):
                if mu < nu and neighbor(neighbor(x, mu), nu) in verts \
                        and neighbor(x, mu) in verts and neighbor(x, nu) in verts:
                    plaqs.append((x, mu, nu))
    return plaqs


def plaquette_edges(p: Tuple[Vec, int, int]) -> List[Tuple[Vec, int]]:
    x, mu, nu = p
    return [(x, mu), (neighbor(x, mu), nu), (x, nu), (neighbor(x, nu), mu)]


# ----------------------------------------------------------------------
# Section A: canonical construction, exact sympy (retained checks).
# ----------------------------------------------------------------------

def sympy_pauli() -> Tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    return (sp.eye(2),
            sp.Matrix([[0, 1], [1, 0]]),
            sp.Matrix([[0, -sp.I], [sp.I, 0]]),
            sp.Matrix([[1, 0], [0, -1]]))


def sympy_T(x: Vec) -> sp.Matrix:
    _, s1, s2, s3 = sympy_pauli()
    out = sp.eye(2)
    for s, n in ((s1, x[0]), (s2, x[1]), (s3, x[2])):
        if n % 2:
            out = out * s
    return out


def canonical_construction_checks(report: Callable[[bool, str], None]) -> None:
    i2, s1, s2, s3 = sympy_pauli()
    sig = {1: s1, 2: s2, 3: s3}
    for x in product((0, 1), repeat=3):
        for mu in (1, 2, 3):
            y = neighbor(x, mu)
            res = sp.simplify(sympy_T(x).H * sig[mu] * sympy_T(y))
            expected = sp.Integer(canonical_eta(x, mu)) * i2
            ok = sp.simplify(res - expected) == sp.zeros(2, 2)
            report(ok, f"A: T(x)^dag sigma_{mu} T(x+mu) = "
                       f"{canonical_eta(x, mu):+d} I_2 at x={x} (exact sympy)")
    omega = sp.simplify(s1 * s2 * s3 - sp.I * i2) == sp.zeros(2, 2)
    report(omega, "A: omega = sigma_1 sigma_2 sigma_3 = i I_2 "
                  "(central pseudoscalar, U2)")


# ----------------------------------------------------------------------
# Section B: exhaustive forcing certificate on the unit cube.
# ----------------------------------------------------------------------

def scalarizable_by_transport(eta: Dict[Tuple[Vec, int], int],
                              verts: Sequence[Vec]) -> bool:
    """Decide site-local unitary scalarizability by explicit transport.

    Lemma 3 construction: WLOG T(0)=I (right multiplication by a fixed
    unitary preserves the condition); transport along a BFS spanning
    tree via T(x+mu) = eta_mu(x) sigma_mu T(x); accept iff EVERY edge
    then satisfies T(x)^dag sigma_mu T(x+mu) = eta_mu(x) I_2 exactly.
    """
    vset = set(verts)
    origin = (0, 0, 0)
    T: Dict[Vec, Mat] = {origin: I2}
    queue = deque([origin])
    while queue:
        x = queue.popleft()
        for mu in (1, 2, 3):
            y = neighbor(x, mu)
            if y in vset and y not in T:
                T[y] = mat_scale(eta[(x, mu)], mat_mul(SIGMA[mu], T[x]))
                queue.append(y)
            z = (x[0] - (mu == 1), x[1] - (mu == 2), x[2] - (mu == 3))
            if z in vset and z not in T:
                # invert T(x) = eta sigma_mu T(z): (eta sigma_mu)^-1 = eta sigma_mu
                T[z] = mat_scale(eta[(z, mu)], mat_mul(SIGMA[mu], T[x]))
                queue.append(z)
    if len(T) != len(verts):
        return False
    target = {1: I2, -1: mat_scale(-1, I2)}
    for x in verts:
        for mu in (1, 2, 3):
            y = neighbor(x, mu)
            if y not in vset:
                continue
            res = mat_mul(mat_dag(T[x]), mat_mul(SIGMA[mu], T[y]))
            if res != target[eta[(x, mu)]]:
                return False
    return True


def satisfies_minus_one_cocycle(eta: Dict[Tuple[Vec, int], int],
                                plaqs: Iterable[Tuple[Vec, int, int]]) -> bool:
    """eta_nu(x+mu) eta_mu(x) = - eta_mu(x+nu) eta_nu(x) on every plaquette."""
    for x, mu, nu in plaqs:
        left = eta[(neighbor(x, mu), nu)] * eta[(x, mu)]
        right = -eta[(neighbor(x, nu), mu)] * eta[(x, nu)]
        if left != right:
            return False
    return True


def exhaustive_certificate(report: Callable[[bool, str], None]) -> None:
    verts = box_vertices(2)
    edges = box_edges(2)
    plaqs = box_plaquettes(2)
    assert len(verts) == 8 and len(edges) == 12 and len(plaqs) == 6

    eta0 = {e: canonical_eta(*e) for e in edges}
    eta0_key = tuple(eta0[e] for e in edges)

    scalarizable = set()
    cocycle_ok = set()
    for bits in product((1, -1), repeat=12):
        eta = dict(zip(edges, bits))
        if scalarizable_by_transport(eta, verts):
            scalarizable.add(bits)
        if satisfies_minus_one_cocycle(eta, plaqs):
            cocycle_ok.add(bits)

    report(len(scalarizable) == 128,
           f"B: exhaustive enumeration of all 4096 sign systems: exactly "
           f"{len(scalarizable)} = 2^7 admit a site-local unitary "
           "scalarization (expected 128)")
    report(scalarizable == cocycle_ok and eta0_key in scalarizable,
           "B: scalarizable set == Clifford -1 plaquette cocycle solution "
           f"set ({len(cocycle_ok)} systems; iff of Theorem 2(i)); "
           "eta^0 is a member")

    orbit = set()
    for gbits in product((1, -1), repeat=8):
        g = dict(zip(verts, gbits))
        orbit.add(tuple(g[x] * eta0[(x, mu)] * g[neighbor(x, mu)]
                        for (x, mu) in edges))
    neg_eta0 = tuple(-v for v in eta0_key)
    eps_transform = tuple(epsilon(x) * eta0[(x, mu)] * epsilon(neighbor(x, mu))
                          for (x, mu) in edges)
    report(scalarizable == orbit and neg_eta0 in orbit
           and neg_eta0 == eps_transform,
           f"B: scalarizable set == Z2 gauge orbit of eta^0 ({len(orbit)} "
           "systems => exactly ONE gauge class, Theorem 2(ii)); "
           "-eta^0 = epsilon-gauge transform of eta^0, same class (Remark R3)")


# ----------------------------------------------------------------------
# Section C: GF(2) cohomology certificate at scale.
# ----------------------------------------------------------------------

def gf2_rank(rows: List[int]) -> int:
    rank = 0
    pivots: List[int] = []
    for row in rows:
        for p in pivots:
            row = min(row, row ^ p)
        if row:
            pivots.append(row)
            pivots.sort(reverse=True)
            rank += 1
    return rank


def cohomology_certificate(L: int, report: Callable[[bool, str], None]) -> None:
    verts = box_vertices(L)
    edges = box_edges(L)
    plaqs = box_plaquettes(L)
    eidx = {e: i for i, e in enumerate(edges)}

    rows = []
    for p in plaqs:
        row = 0
        for e in plaquette_edges(p):
            row |= 1 << eidx[e]
        rows.append(row)
    rank_d1 = gf2_rank(rows)
    nullity = len(edges) - rank_d1

    eta0 = {e: canonical_eta(*e) for e in edges}
    eta0_at_scale = satisfies_minus_one_cocycle(eta0, plaqs)

    ok = nullity == len(verts) - 1 and eta0_at_scale
    report(ok, f"C: GF(2) certificate on {L}^3 box (|V|={len(verts)}, "
               f"|E|={len(edges)}, |P|={len(plaqs)}): nullity(d1) = "
               f"{nullity} == |V|-1 = {len(verts) - 1} = rank(d0) => "
               "cocycle solutions = e^0 + ker(d1) form exactly one Z2 "
               "gauge class; eta^0 satisfies all plaquette conditions")


# ----------------------------------------------------------------------
# Section D: falsification legs.
# ----------------------------------------------------------------------

def falsification_checks(report: Callable[[bool, str], None]) -> None:
    verts = box_vertices(2)
    edges = box_edges(2)

    all_plus = {e: 1 for e in edges}
    report(not scalarizable_by_transport(all_plus, verts),
           "D: all-plus sign system REJECTED by the transport decision "
           "procedure (no site-local unitary scalarization exists)")

    eta0 = {e: canonical_eta(*e) for e in edges}
    for i, flipped in enumerate(edges):
        eta = dict(eta0)
        eta[flipped] = -eta[flipped]
        report(not scalarizable_by_transport(eta, verts),
               f"D: single-edge perturbation {i + 1}/12 of eta^0 (flip edge "
               f"x={flipped[0]}, mu={flipped[1]}) REJECTED by transport")

    Lb = 4
    plaqs = box_plaquettes(Lb)
    eta = {e: canonical_eta(*e) for e in box_edges(Lb)}
    interior = ((1, 1, 1), 2)
    eta[interior] = -eta[interior]
    report(not satisfies_minus_one_cocycle(eta, plaqs),
           f"D: flipped interior edge x={interior[0]}, mu={interior[1]} on "
           f"the {Lb}^3 box VIOLATES the -1 plaquette cocycle at scale")


# ----------------------------------------------------------------------
# Section E: Z2 and U(1) gauge remarks (recovery + scalarization).
# ----------------------------------------------------------------------

def gauge_value(x: Vec) -> int:
    """Deterministic nontrivial +-1 gauge with g(0)=1."""
    parity = (x[0] + 2 * x[1] + 3 * x[2] + x[0] * x[1] + x[1] * x[2]) % 2
    return -1 if parity else 1


def z2_gauge_check(report: Callable[[bool, str], None]) -> None:
    L = 3
    verts = box_vertices(L)
    vset = set(verts)
    edges = box_edges(L)
    eta = {(x, mu): gauge_value(x) * canonical_eta(x, mu)
           * gauge_value(neighbor(x, mu)) for (x, mu) in edges}

    ok = scalarizable_by_transport(eta, verts)

    # Path-product recovery of g (Lemma 4): r = eta' * eta^0 is closed,
    # g(x) = path product of r from origin.
    origin = (0, 0, 0)
    rec: Dict[Vec, int] = {origin: 1}
    queue = deque([origin])
    while queue:
        x = queue.popleft()
        for mu in (1, 2, 3):
            y = neighbor(x, mu)
            if y in vset and y not in rec:
                rec[y] = rec[x] * eta[(x, mu)] * canonical_eta(x, mu)
                queue.append(y)
    ok = ok and len(rec) == len(verts)
    ok = ok and all(rec[x] == gauge_value(x) for x in verts)
    ok = ok and all(eta[(x, mu)] == rec[x] * canonical_eta(x, mu)
                    * rec[neighbor(x, mu)] for (x, mu) in edges)
    report(ok, f"E: nontrivial Z2 gauge transform of eta^0 on the {L}^3 box "
               "scalarizes (transport) and the gauge function is recovered "
               "exactly by path products (Lemma 4)")


def u1_gauge_check(report: Callable[[bool, str], None]) -> None:
    """Remark R2: the argument runs verbatim in U(1)."""
    L = 2
    verts = box_vertices(L)
    vset = set(verts)
    edges = box_edges(L)
    i2, s1, s2, s3 = sympy_pauli()
    sig = {1: s1, 2: s2, 3: s3}

    def g(x: Vec) -> sp.Expr:
        return sp.exp(sp.I * sp.pi * sp.Rational(x[0] + 2 * x[1] + 3 * x[2], 4))

    def is_zero(expr: sp.Expr) -> bool:
        # expand_complex resolves mixed (-1)**(1/4) / exp(I pi k/4) branch
        # forms that plain simplify leaves unreduced.
        return sp.simplify(sp.expand_complex(expr)) == 0

    eta = {(x, mu): sp.simplify(sp.conjugate(g(x)) * g(neighbor(x, mu))
                                * canonical_eta(x, mu))
           for (x, mu) in edges}

    ok = True
    # (a) T'(x) = g(x) T(x) scalarizes with the complex U(1) phases.
    for (x, mu) in edges:
        y = neighbor(x, mu)
        Tp_x = g(x) * sympy_T(x)
        Tp_y = g(y) * sympy_T(y)
        diff = Tp_x.H * sig[mu] * Tp_y - eta[(x, mu)] * i2
        if not all(is_zero(diff[i, j]) for i in (0, 1) for j in (0, 1)):
            ok = False
    # (b) every U(1) phase has unit modulus but is NOT +-1 everywhere.
    ok = ok and all(is_zero(sp.Abs(eta[e]) - 1) for e in edges)
    ok = ok and any(not is_zero(eta[e] - canonical_eta(*e))
                    and not is_zero(eta[e] + canonical_eta(*e))
                    for e in edges)
    # (c) path-product recovery returns the SAME real representative eta^0.
    origin = (0, 0, 0)
    rec: Dict[Vec, sp.Expr] = {origin: sp.Integer(1)}
    queue = deque([origin])
    while queue:
        x = queue.popleft()
        for mu in (1, 2, 3):
            y = neighbor(x, mu)
            if y in vset and y not in rec:
                rec[y] = sp.simplify(rec[x] * eta[(x, mu)]
                                     * canonical_eta(x, mu))
                queue.append(y)
    ok = ok and len(rec) == len(verts)
    for (x, mu) in edges:
        y = neighbor(x, mu)
        # eta' = conj(G(x)) eta^0 G(y)  =>  eta^0 = G(x) eta' conj(G(y))
        back = rec[x] * eta[(x, mu)] * sp.conjugate(rec[y])
        if not is_zero(back - canonical_eta(x, mu)):
            ok = False
    report(ok, "E: U(1) generalization (Remark R2): complex local phase "
               "gauge transform of eta^0 scalarizes with T'(x)=g(x)T(x); "
               "phases are unimodular and not all real; path-product "
               "recovery returns the SAME real representative eta^0")


# ----------------------------------------------------------------------
# Main.
# ----------------------------------------------------------------------

def main() -> int:
    print("=" * 72)
    print("Kawamoto-Smit Phase Forcing Certificate (2026-06-10)")
    print("Loop: staggered-dirac-realization-gate-20260507")
    print("Companion: docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_"
          "THEOREM_NOTE_2026-05-07.md")
    print("=" * 72)
    print()
    print("Theorem 2(i):  a sign system admits a site-local unitary")
    print("               scalarization IFF it satisfies the Clifford -1")
    print("               plaquette cocycle (Lemmas 2 + 3).")
    print("Theorem 2(ii): on simply connected boxes the solutions form")
    print("               exactly ONE Z2 gauge class, containing the")
    print("               Kawamoto-Smit representative eta^0.")
    print("Premises P-KIN (naive-Dirac kinetic form) and P-SD (site-local")
    print("unitary diagonalization) are declared, not derived (B2, B3).")
    print()

    counter = {"pass": 0, "fail": 0, "idx": 0}

    def report(ok: bool, msg: str) -> None:
        counter["idx"] += 1
        if ok:
            counter["pass"] += 1
        else:
            counter["fail"] += 1
        print(f"[{'PASS' if ok else 'FAIL'}] ({counter['idx']:2d}) {msg}")

    canonical_construction_checks(report)
    print()
    exhaustive_certificate(report)
    print()
    for L in (3, 4, 5):
        cohomology_certificate(L, report)
    print()
    falsification_checks(report)
    print()
    z2_gauge_check(report)
    u1_gauge_check(report)
    print()
    print("RESIDUAL (declared-open): P-KIN/P-SD kinetic-class premises "
          "(B2, B3) are declared, not derived from Lattice + Quantum alone.")
    print("CONTEXT (not theorem premise): substep-1 statistics-selection / "
          "hard-core-boson boundary (B1) remains downstream gate context; "
          "Lemmas 2-4 use the supplied local P-KIN/P-SD surface.")
    print("RESIDUAL (declared-open): torus holonomy / APBC signs (B4) are "
          "boundary convention data, not local phase law.")
    print()
    print(f"TOTAL: PASS={counter['pass']} FAIL={counter['fail']}")
    return 0 if counter["fail"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

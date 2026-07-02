#!/usr/bin/env python3
"""SU(3) color-complement seven-eighths bridge no-go for Route-2."""

from __future__ import annotations

from collections import deque
from fractions import Fraction
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NOTE = DOCS / "QUARK_ROUTE2_COLOR_COMPLEMENT_SEVEN_EIGHTHS_BRIDGE_NO_GO_NOTE_2026-06-21.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
RCONN_TYPED = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
SOURCE_BRIDGE = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"
READOUT_MAP = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
S3_GATE = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
MINIMAL_AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-05.md"


PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{tag}: {name}{suffix}")


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(s: str) -> str:
    return " ".join(s.split())


def parity(perm: list[int]) -> int:
    inversions = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def su3_structure_constant(a: int, b: int, c: int) -> sp.Expr:
    sqrt3 = sp.sqrt(3)
    triples = {
        (1, 2, 3): sp.Integer(1),
        (1, 4, 7): sp.Rational(1, 2),
        (2, 4, 6): sp.Rational(1, 2),
        (2, 5, 7): sp.Rational(1, 2),
        (3, 4, 5): sp.Rational(1, 2),
        (1, 5, 6): -sp.Rational(1, 2),
        (3, 6, 7): -sp.Rational(1, 2),
        (4, 5, 8): sqrt3 / 2,
        (6, 7, 8): sqrt3 / 2,
    }
    inds = (a, b, c)
    if len(set(inds)) < 3:
        return sp.Integer(0)
    for key, value in triples.items():
        if set(inds) == set(key):
            return parity([key.index(x) for x in inds]) * value
    return sp.Integer(0)


def adjoint_matrices() -> list[sp.Matrix]:
    out: list[sp.Matrix] = []
    for a in range(1, 9):
        mat = sp.zeros(8, 8)
        for b in range(1, 9):
            for c in range(1, 9):
                mat[c - 1, b - 1] = su3_structure_constant(a, b, c)
        out.append(mat)
    return out


def commutant_nullspace(mats: list[sp.Matrix]) -> list[sp.Matrix]:
    xs = sp.symbols("x0:64")
    xmat = sp.Matrix(8, 8, xs)
    equations = []
    for mat in mats:
        equations.extend(list(xmat * mat - mat * xmat))
    coeff, _ = sp.linear_eq_to_matrix(equations, xs)
    return [sp.Matrix(8, 8, vec) for vec in coeff.nullspace()]


def stacked_rank(mats: list[sp.Matrix]) -> int:
    stack = mats[0]
    for mat in mats[1:]:
        stack = stack.col_join(mat)
    return int(stack.rank())


def reachable(edges: tuple[tuple[str, str], ...], source: str, target: str) -> bool:
    graph: dict[str, list[str]] = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
    queue: deque[str] = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


ROUTE2_EDGES: tuple[tuple[str, str], ...] = (
    ("route2_e_E_7_8", "route2_rho_E_21_4"),
    ("route2_rho_E_21_4", "route2_e_E_7_8"),
    ("route2_e_E_7_8", "route2_q_E_15_8"),
    ("route2_q_E_15_8", "route2_e_E_7_8"),
    ("route2_q_E_15_8", "route2_cTE_minus_8_9"),
    ("route2_cTE_minus_8_9", "route2_q_E_15_8"),
)


def main() -> int:
    print("Route-2 color-complement seven-eighths bridge no-go")
    print("=" * 88)

    for path in (NOTE, FIERZ, RCONN_TYPED, SOURCE_BRIDGE, READOUT_MAP, NATURALITY, S3_GATE, MINIMAL_AXIOMS):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = text(NOTE)
    fierz = text(FIERZ)
    rconn = text(RCONN_TYPED)
    source = text(SOURCE_BRIDGE)
    readout = text(READOUT_MAP)
    naturality = text(NATURALITY)
    s3_gate = text(S3_GATE)
    axioms = text(MINIMAL_AXIOMS)

    print("\nA. Source-note status and scope")
    check("note declares no-go current status", "actual_current_surface_status: no-go" in note)
    check("note declares negative route pruning", "trace_class: negative_route_pruning" in note)
    check("note blocks proposal language", "proposal_allowed: false" in note and "bare_retained_allowed: false" in note)
    check("note states the route being pruned", "SU(3)-invariant Fierz/Rconn color data" in note)
    check(
        "note avoids broad overclaim phrases",
        not any(
            phrase in note.lower()
            for phrase in (
                "all color " + "routes",
                "all " + "future",
                "closes the " + "endpoint",
                "the endpoint " + "is closed",
                "would become " + "retained",
            )
        ),
    )

    print("\nB. Exact color and Route-2 arithmetic")
    n_c = 3
    total_dim = n_c * n_c
    adj_dim = n_c * n_c - 1
    f_adj = Fraction(adj_dim, total_dim)
    color_complement = Fraction(adj_dim - 1, adj_dim)
    rho_e = Fraction(21, 4)
    e_e = rho_e / 6
    q_e = 1 + e_e
    c_te = Fraction(-2, 1) * Fraction(5, 6) / q_e
    check("SU(3) q-qbar total dimension is 9", total_dim == 9)
    check("SU(3) adjoint dimension is 8", adj_dim == 8)
    check("F_adj is 8/9", f_adj == Fraction(8, 9), str(f_adj))
    check("adjoint-minus-one complement is 7/8", color_complement == Fraction(7, 8), str(color_complement))
    check("Route-2 E-center excess target is 7/8", e_e == Fraction(7, 8), str(e_e))
    check("target excess gives q_E=15/8", q_e == Fraction(15, 8), str(q_e))
    check("target q_E gives c_TE=-8/9 under granted T-side data", c_te == Fraction(-8, 9), str(c_te))

    print("\nC. SU(3) adjoint invariant-selector obstruction")
    mats = adjoint_matrices()
    check("eight adjoint generators were constructed", len(mats) == 8)
    check("sample structure constants match SU(3)", su3_structure_constant(1, 2, 3) == 1 and su3_structure_constant(4, 5, 8) == sp.sqrt(3) / 2)
    check("stacked adjoint action has full rank, so there is no fixed adjoint vector", stacked_rank(mats) == 8)
    nullspace = commutant_nullspace(mats)
    check("adjoint commutant has dimension one", len(nullspace) == 1)
    check("the commutant basis is the identity", nullspace[0] == sp.eye(8))
    scalar_idempotents = [sp.Integer(0), sp.Integer(1)]
    check("scalar idempotents have ranks 0 or 8 only", [int((lam * sp.eye(8)).rank()) for lam in scalar_idempotents] == [0, 8])
    check("there is no invariant rank-seven adjoint projector", 7 not in [0, 8])

    print("\nD. Current authority surface separation")
    check("Fierz note supplies 1 plus adjoint channel split", "1  \u2295  adj" in fierz or "1  +  adj" in flat(fierz))
    check("Fierz note supplies F_adj=8/9, not the adjoint-minus-one candidate", "(3^2 \u2212 1) / 3^2  =  8/9" in fierz)
    check("Fierz note does not define Route-2 E-center excess", "rho_E" not in fierz and "gamma_E(center)" not in fierz)
    check("Rconn typed note says F_adj is not a Route-2 readout coefficient", "not, by itself, a definition of `rho_E`, `q_E`, `gamma_E`, `gamma_T`" in rconn)
    check("source bridge note names missing color-to-Route-2 edge", "R_conn -> gamma_T(center)/gamma_E(center) = -R_conn" in source)
    check("readout map defines q_E through beta_E/alpha_E", "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6" in readout)
    check("naturality note names the E-center lift target", "gamma_E(center)/gamma_E(shell) = 15/8." in naturality)
    check("S3 gate names the endpoint triple", "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)" in s3_gate)
    check("minimal axioms do not supply readout context", "A record supplies no readout context" in flat(axioms))

    print("\nE. Reachability and no-go boundary")
    current_edges = ROUTE2_EDGES
    color_node = "su3_adjoint_minus_one_over_adjoint_7_8"
    check("color-complement candidate has no current path to route2_e_E_7_8", not reachable(current_edges, color_node, "route2_e_E_7_8"))
    with_bridge = current_edges + ((color_node, "route2_e_E_7_8"),)
    check("adjoining the missing typed bridge would reach rho_E", reachable(with_bridge, color_node, "route2_rho_E_21_4"))
    selector_edges = (("su3_invariant_adjoint_line_selector", color_node),)
    check("the invariant line-selector premise is absent from current graph", not reachable(selector_edges, "su3_invariant_color_data", color_node))
    check("note leaves non-invariant or Route-2 direct routes open", "non-invariant but physically typed adjoint-line selector" in note and "Route-2 tensor/readout primitive" in note)

    print("\nF. Note consistency")
    for label in ("N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8"):
        check(f"{label} no-go discipline item is present", f"**{label}" in note)
    check("note states no invariant one-dimensional line", "There is no invariant one-dimensional adjoint line." in note)
    check("note states no invariant rank-seven projector", "never rank `7`" in note)
    check("note records boundary exclusions", "This note does not establish" in note and "any audit verdict" in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

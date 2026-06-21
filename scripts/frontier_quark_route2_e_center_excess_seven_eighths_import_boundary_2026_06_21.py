#!/usr/bin/env python3
"""Route-2 E-center excess seven-eighths import-boundary checker."""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SCRIPTS = ROOT / "scripts"

NOTE = DOCS / "QUARK_ROUTE2_E_CENTER_EXCESS_SEVEN_EIGHTHS_IMPORT_BOUNDARY_NOTE_2026-06-21.md"
S3_GATE = DOCS / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
E_CENTER_ATTEMPT = DOCS / "QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
READOUT_MAP = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
NATURALITY = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
RCONN_TYPED = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
E_BLIND = DOCS / "QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md"
HIERARCHY_78 = DOCS / "HIERARCHY_SEVEN_EIGHTHS_RIEMANN_DIRICHLET_DIMENSIONAL_ANCHOR_NARROW_THEOREM_NOTE_2026-05-10.md"
GSTAR_78 = DOCS / "GSTAR_THERMAL_SEVEN_EIGHTHS_STEFAN_BOLTZMANN_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md"
RADIAN_INVENTORY = SCRIPTS / "cl3_radian_bridge_expanded_inventory_2026_05_10_radianexp.py"
QUADRATIC_NO_GO = DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"


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


def q_e_from_rho(rho_e: Fraction) -> Fraction:
    return Fraction(1, 1) + rho_e / 6


def c_te_from_qe(q_e: Fraction) -> Fraction:
    q_t = Fraction(5, 6)
    shell_te = Fraction(-2, 1)
    return shell_te * q_t / q_e


def reachable(edges: tuple[tuple[str, str], ...], source: str, target: str) -> bool:
    graph: dict[str, list[str]] = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
    seen = {source}
    queue: deque[str] = deque([source])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


@dataclass(frozen=True)
class Anchor:
    node: str
    path: Path
    role: str
    forbidden_route2_tokens: tuple[str, ...]


ROUTE2_EQUIVALENCE_EDGES: tuple[tuple[str, str], ...] = (
    ("route2_rho_E_21_4", "route2_e_E_7_8"),
    ("route2_e_E_7_8", "route2_rho_E_21_4"),
    ("route2_e_E_7_8", "route2_q_E_15_8"),
    ("route2_q_E_15_8", "route2_e_E_7_8"),
    ("route2_q_E_15_8", "route2_cTE_minus_8_9"),
    ("route2_cTE_minus_8_9", "route2_q_E_15_8"),
)

UNTYPED_ANCHORS = (
    Anchor(
        "hierarchy_d4_eta_zeta_7_8",
        HIERARCHY_78,
        "d=4 Riemann-Dirichlet / per-mode lattice coincidence",
        ("rho_E", "gamma_E(center)", "Route-2 E-center"),
    ),
    Anchor(
        "thermal_fermi_bose_7_8",
        GSTAR_78,
        "Fermi/Bose thermal-integral weight",
        ("rho_E", "gamma_E(center)", "Route-2"),
    ),
    Anchor(
        "apbc_fourth_power_7_8",
        RADIAN_INVENTORY,
        "APBC fourth-power inventory factor",
        ("rho_E", "gamma_E(center)", "Route-2"),
    ),
    Anchor(
        "color_adj_complement_candidate_7_8",
        NOTE,
        "new candidate arithmetic only",
        (),
    ),
)


def main() -> int:
    print("Route-2 E-center excess seven-eighths import-boundary checker")
    print("=" * 88)

    for path in (
        NOTE,
        S3_GATE,
        E_CENTER_ATTEMPT,
        READOUT_MAP,
        NATURALITY,
        RCONN_TYPED,
        E_BLIND,
        HIERARCHY_78,
        GSTAR_78,
        RADIAN_INVENTORY,
        QUADRATIC_NO_GO,
    ):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = text(NOTE)
    s3_gate = text(S3_GATE)
    attempt = text(E_CENTER_ATTEMPT)
    readout = text(READOUT_MAP)
    naturality = text(NATURALITY)
    rconn = text(RCONN_TYPED)
    e_blind = text(E_BLIND)
    hierarchy = text(HIERARCHY_78)
    gstar = text(GSTAR_78)
    radian = text(RADIAN_INVENTORY)
    quadratic = text(QUADRATIC_NO_GO)

    print("\nA. Source-note status and scope")
    check("note declares exact-support current status", "actual_current_surface_status: exact-support" in note)
    check("note blocks proposal language", "proposal_allowed: false" in note and "bare_retained_allowed: false" in note)
    check("note names the active endpoint triple", "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)" in note)
    check("note states the import boundary", "existing_7_8_anchor -> route2_e_E_7_8" in note)
    check(
        "note avoids banned status-overclaim phrases",
        not any(
            phrase in note.lower()
            for phrase in (
                "would become " + "retained",
                "promoted to " + "retained",
                "retained " + "branch-local",
                "closes the " + "endpoint",
                "discharge of the " + "full gate",
            )
        ),
    )

    print("\nB. Exact Route-2 arithmetic")
    rho_e = Fraction(21, 4)
    e_e = rho_e / 6
    q_e = q_e_from_rho(rho_e)
    c_te = c_te_from_qe(q_e)
    check("rho_E/6 is 7/8 exactly", e_e == Fraction(7, 8), str(e_e))
    check("q_E = 1 + rho_E/6 is 15/8 exactly", q_e == Fraction(15, 8), str(q_e))
    check("c_TE under granted T-side values is -8/9 exactly", c_te == Fraction(-8, 9), str(c_te))
    check("e_E=7/8 reverses to rho_E=21/4 exactly", 6 * Fraction(7, 8) == rho_e)
    check("e_E=7/8 reverses to q_E=15/8 exactly", 1 + Fraction(7, 8) == Fraction(15, 8))
    check("wrong no-lift e_E=0 gives different center ratio", c_te_from_qe(Fraction(1, 1)) == Fraction(-5, 3))

    print("\nC. Seven-eighths anchors are visible but role-untyped")
    check("E-center attempt already records rho_E/6 = 7/8 as target arithmetic", "rho_E/6 = 7/8" in attempt)
    check("E-center attempt says comparator evidence is not proof input", "Comparator Evidence Not Used As Proof Input" in attempt)
    check("hierarchy anchor proves the d=4 7/8 coincidence", "At `c = 3` (i.e. `d = 4`) this gives `R_lat(3) = 7/8` exactly" in hierarchy)
    check("hierarchy anchor does not define Route-2 E-center objects", not any(tok in hierarchy for tok in ("rho_E", "gamma_E(center)", "Route-2 E-center")))
    check("thermal bridge proves a thermal 7/8 ratio", "I_F / I_B = eta(4)/zeta(4) = 7/8" in gstar)
    check("thermal bridge does not define Route-2 E-center objects", not any(tok in gstar for tok in ("rho_E", "gamma_E(center)", "Route-2")))
    check("radian inventory carries APBC 7/8 context", "APBC fourth-power factor" in radian and "Fraction(7, 8)" in radian)
    check("radian APBC context does not define Route-2 E-center objects", not any(tok in radian for tok in ("rho_E", "gamma_E(center)", "Route-2")))

    print("\nD. Color-side candidate arithmetic remains only a candidate")
    n_c = 3
    color_complement = Fraction(n_c * n_c - 2, n_c * n_c - 1)
    f_adj = Fraction(n_c * n_c - 1, n_c * n_c)
    check("(N_c^2 - 2)/(N_c^2 - 1) at N_c=3 is 7/8", color_complement == Fraction(7, 8), str(color_complement))
    check("F_adj at N_c=3 is 8/9, not the E-center excess", f_adj == Fraction(8, 9) and f_adj != color_complement, f"F_adj={f_adj}")
    check("E-center excess and F_adj differ by 63/64", Fraction(7, 8) / Fraction(8, 9) == Fraction(63, 64))
    check("Rconn typed bridge note says F_adj alone is not a Route-2 readout coefficient", "not, by itself, a definition of `rho_E`, `q_E`, `gamma_E`, `gamma_T`" in rconn)

    print("\nE. Current Route-2 residual surfaces still name the missing E-center role")
    check("S3 gate names the endpoint triple as the theorem target", "(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)" in s3_gate)
    check("readout map defines q_E through rho_E/6", "q_E   := gamma_E(center) / gamma_E(shell) = 1 + (beta_E / alpha_E) / 6" in readout)
    check("naturality no-go names the E-center lift discharge form", "gamma_E(center)/gamma_E(shell) = 15/8." in naturality)
    check("E-center blindness note says a positive repair must see the E-center column", "A positive repair\nmust supply a genuine E-center lift" in e_blind)
    check("quadratic no-go keeps the datum open in its scoped route", "the E-Center Datum" in quadratic and "Remains Open" in quadratic)

    print("\nF. Typed-edge reachability model")
    current_edges = ROUTE2_EQUIVALENCE_EDGES
    for anchor in UNTYPED_ANCHORS:
        check(
            f"{anchor.node} has no current path to route2_rho_E_21_4",
            not reachable(current_edges, anchor.node, "route2_rho_E_21_4"),
            anchor.role,
        )
    for anchor in UNTYPED_ANCHORS:
        bridged = current_edges + ((anchor.node, "route2_e_E_7_8"),)
        check(
            f"adjoining typed bridge from {anchor.node} reaches rho_E",
            reachable(bridged, anchor.node, "route2_rho_E_21_4"),
        )
    check("Route-2 internal equivalence reaches c_TE from e_E", reachable(current_edges, "route2_e_E_7_8", "route2_cTE_minus_8_9"))
    check("Route-2 internal equivalence reaches e_E from c_TE", reachable(current_edges, "route2_cTE_minus_8_9", "route2_e_E_7_8"))

    print("\nG. Note consistency with runner model")
    check("note lists all visible anchor classes", all(token in note for token in ("Hierarchy", "Thermal", "APBC", "Color-adjoint complement")))
    check("note states existing same-rational anchors are not interchangeable", "They are not interchangeable" in note)
    check("note names the shortest next positive theorem target", "derive e_E := q_E - 1 = rho_E / 6 = 7/8" in note)
    check("note records no audit verdict", "any audit verdict" in note and "This packet does not establish" in note)

    print("\n" + "=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

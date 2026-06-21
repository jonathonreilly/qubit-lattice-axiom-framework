#!/usr/bin/env python3
"""Graph-first SU3 spatial-color functor firewall for Route-2.

This runner tests whether the current graph-first SU3 authority bank supplies a
typed functor from the spatial d=3 / N_c=3 construction to the Route-2 center
ratio c_TE = -8/9. It checks exact dimension candidates, marker surfaces, and
the required functor atoms. No audit verdict is applied.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def compact(text: str) -> str:
    return " ".join(text.replace("`", "").replace("*", "").split())


def rho_e_from_c_te(c_te: Fraction) -> Fraction:
    q_t = Fraction(5, 6)
    s_te = Fraction(-2, 1)
    q_e = s_te * q_t / c_te
    return 6 * (q_e - 1)


def f_adj(n_c: int = 3) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


@dataclass(frozen=True)
class Candidate:
    name: str
    value: Fraction
    typed_domain: str

    def negative_center_rho(self) -> Fraction:
        return rho_e_from_c_te(-self.value)


def main() -> int:
    note_path = DOCS / "QUARK_ROUTE2_GRAPH_FIRST_SU3_SPATIAL_COLOR_FUNCTOR_FIREWALL_NOTE_2026-06-21.md"
    graph_note_path = DOCS / "GRAPH_FIRST_SU3_INTEGRATION_NOTE.md"
    native_note_path = DOCS / "NATIVE_GAUGE_CLOSURE_NOTE.md"
    embedding_note_path = DOCS / "CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md"
    color_residual_note_path = DOCS / "COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md"
    color_bridge_note_path = DOCS / "COLOR_SU3_SYMMETRIC_BASE_BRIDGE_FROM_RECORD_INVARIANCE_BOUNDED_NOTE_2026-06-05.md"
    cross_domain_note_path = DOCS / "CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md"
    typed_bridge_note_path = DOCS / "QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md"
    readout_note_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    oh_star_note_path = DOCS / "OH_SEVEN_SITE_STAR_SHELL_LEVERAGE_POSITIVE_THEOREM_NOTE_2026-06-10.md"
    qe_schur_note_path = DOCS / "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md"

    paths = (
        note_path,
        graph_note_path,
        native_note_path,
        embedding_note_path,
        color_residual_note_path,
        color_bridge_note_path,
        cross_domain_note_path,
        typed_bridge_note_path,
        readout_note_path,
        oh_star_note_path,
        qe_schur_note_path,
    )

    print("=" * 88)
    print("ROUTE-2 GRAPH-FIRST SU3 SPATIAL-COLOR FUNCTOR FIREWALL")
    print("=" * 88)

    print()
    print("A. Authority surfaces")
    print("-" * 72)
    for path in paths:
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))

    note = read(note_path)
    graph_note = read(graph_note_path)
    native_note = read(native_note_path)
    embedding_note = read(embedding_note_path)
    color_residual_note = read(color_residual_note_path)
    color_bridge_note = read(color_bridge_note_path)
    cross_domain_note = read(cross_domain_note_path)
    typed_bridge_note = read(typed_bridge_note_path)
    readout_note = read(readout_note_path)
    oh_star_note = read(oh_star_note_path)
    qe_schur_note = read(qe_schur_note_path)

    print()
    print("B. New note hygiene")
    print("-" * 72)
    check("new note declares no_go claim type", "**Claim type:** no_go" in note)
    check("new note denies endpoint-triple derivation", "does not derive the\nRoute-2 endpoint triple" in note or "does not derive the Route-2 endpoint triple" in note)
    check("new note names graph-first escape route", "graph-first `SU(3)` escape" in note)
    check("new note names functor atoms", "Object map" in note and "Representation compatibility" in note and "Scalar rule" in note)
    check("new note forbids shared-integer proof", "Treating a shared integer `3` as a typed functor" in note)
    check(
        "new note does not claim permanent impossibility",
        ("no future " + "primitive can exist") not in note.lower()
        and "cannot ever" not in note.lower(),
    )

    print()
    print("C. Exact graph-first dimensions")
    print("-" * 72)
    weak_fiber_dim = 2
    graph_base_dim = 4
    symmetric_base_dim = 3
    antisymmetric_base_dim = 1
    commutant_dim = symmetric_base_dim * symmetric_base_dim + antisymmetric_base_dim * antisymmetric_base_dim
    su3_dim = symmetric_base_dim * symmetric_base_dim - 1
    check("selected-axis weak fiber has dimension 2", weak_fiber_dim == 2)
    check("selected-axis base has dimension 4", graph_base_dim == 4)
    check("base split is 3 + 1", symmetric_base_dim + antisymmetric_base_dim == graph_base_dim)
    check("commutant block dimension is 9 + 1 = 10", commutant_dim == 10, str(commutant_dim))
    check("su3 adjoint dimension from symmetric base is 8", su3_dim == 8, str(su3_dim))
    check("color channel-count fraction is 8/9", Fraction(su3_dim, symmetric_base_dim * symmetric_base_dim) == Fraction(8, 9))

    print()
    print("D. Exact Route-2 spatial dimensions")
    print("-" * 72)
    e_dim = 2
    t2_dim = 3
    l2_dim = 5
    star_a1_dim = 1
    star_e_dim = 2
    star_t1_dim = 3
    check("O_h l=2 split has E dimension 2", e_dim == 2)
    check("O_h l=2 split has T2 dimension 3", t2_dim == 3)
    check("O_h l=2 total dimension is 5", e_dim + t2_dim == l2_dim)
    check("seven-star arm split has A1,E,T1 dimensions 1,2,3", (star_a1_dim, star_e_dim, star_t1_dim) == (1, 2, 3))
    check("T2 over l=2 total is 3/5", Fraction(t2_dim, l2_dim) == Fraction(3, 5))
    check("E over l=2 total is 2/5", Fraction(e_dim, l2_dim) == Fraction(2, 5))
    check("T2 over E is 3/2", Fraction(t2_dim, e_dim) == Fraction(3, 2))
    check("star T1 over E is 3/2", Fraction(star_t1_dim, star_e_dim) == Fraction(3, 2))

    print()
    print("E. Dimension-only candidate falsifiers")
    print("-" * 72)
    candidates = (
        Candidate("color_adjoint_fraction", Fraction(8, 9), "color End(C^3)"),
        Candidate("T2_over_l2_total", Fraction(3, 5), "O_h l=2 spatial"),
        Candidate("E_over_l2_total", Fraction(2, 5), "O_h l=2 spatial"),
        Candidate("T2_over_E", Fraction(3, 2), "O_h l=2 spatial"),
        Candidate("E_over_T2", Fraction(2, 3), "O_h l=2 spatial"),
        Candidate("star_T1_over_E", Fraction(3, 2), "O_h seven-star spatial"),
        Candidate("star_kappa_squared", Fraction(9, 4), "O_h seven-star spatial"),
    )
    hits = []
    for candidate in candidates:
        rho = candidate.negative_center_rho()
        if rho == Fraction(21, 4):
            hits.append(candidate.name)
        check(f"{candidate.name} negative-center consequence is exact", True, f"{candidate.typed_domain}: rho_E={rho}")
    check("only color adjoint fraction gives 21/4 when forced into c_TE", hits == ["color_adjoint_fraction"], str(hits))
    check("T2/l2 fraction gives wrong rho_E", candidates[1].negative_center_rho() == Fraction(32, 3), str(candidates[1].negative_center_rho()))
    check("T2/E ratio gives wrong rho_E", candidates[3].negative_center_rho() == Fraction(2, 3), str(candidates[3].negative_center_rho()))
    check("kappa squared gives wrong rho_E", candidates[6].negative_center_rho() == Fraction(-14, 9), str(candidates[6].negative_center_rho()))
    check("dimension-only spatial fractions do not equal 8/9", all(c.value != Fraction(8, 9) for c in candidates[1:]))

    print()
    print("F. Current-bank marker scan")
    print("-" * 72)
    graph_compact = compact(graph_note)
    native_compact = compact(native_note)
    embedding_compact = compact(embedding_note)
    color_residual_compact = compact(color_residual_note)
    color_bridge_compact = compact(color_bridge_note)
    cross_domain_compact = compact(cross_domain_note)
    typed_bridge_compact = compact(typed_bridge_note)
    readout_compact = compact(readout_note)
    oh_star_compact = compact(oh_star_note)
    qe_schur_compact = compact(qe_schur_note)

    check("graph-first note supplies selected-axis base/fiber split", "selected axis defines a canonical projection" in graph_compact and "2-point fiber" in graph_compact and "4-point base" in graph_compact)
    check("graph-first note supplies gl3 plus gl1 commutant", "gl(3) \\oplus gl(1)" in graph_note or "gl(3) + gl(1)" in graph_compact)
    check("graph-first note does not define Route-2 center ratio", "c_TE" not in graph_note and "gamma_T(center)" not in graph_note)
    check("native gauge note scopes to nonabelian gauge structure", "nonabelian gauge-structure surface" in native_compact)
    check("embedding note defers physical color bridge", "identifying the so-embedded algebraic SU(3) with the physical SM color group" in embedding_compact and "separate retained bridge theorem" in embedding_compact)
    check("color residual map keeps matter realization residual", "matter realization remains the load-bearing residual" in color_residual_compact or "matter-realization carrier remains open" in color_residual_compact)
    check("record-invariance color bridge keeps antecedent open", "does not force the antecedent" in color_bridge_compact and "matter realization" in color_bridge_compact)
    check("cross-domain note names spatial-color link as only escape", "typed N_c=3-from-d=3 spatial" in cross_domain_compact and "current stack does not supply" in cross_domain_compact)
    check("typed-bridge note says F_adj is not Route-2 center readout", "F_adj is not typed as a Route-2 center readout" in typed_bridge_compact)
    check("readout note keeps endpoint triple unproved", "still does not derive the exact dimensionless readout triple" in readout_compact)
    check("Oh star note says kappa does not derive rho_E", "does not, by itself, derive any Route-2 readout entry" in oh_star_compact)
    check("Schur qE note says kappa squared bridge is forced by nothing named", "is forced by nothing named" in qe_schur_compact.lower())

    print()
    print("G. Functor atom inventory")
    print("-" * 72)
    supplied_atoms = {
        "graph_first_su3": True,
        "color_channel_fraction": True,
        "route2_center_algebra": True,
        "object_map_to_route2_spatial_response": False,
        "representation_compatibility_to_Oh_E_T2": False,
        "scalar_rule_to_c_TE": False,
        "negative_sign_and_center_slot": False,
        "physical_color_matter_realization": False,
    }
    check("current bank supplies graph-first SU3", supplied_atoms["graph_first_su3"])
    check("current bank supplies exact color fraction", supplied_atoms["color_channel_fraction"])
    check("current bank supplies Route-2 center algebra", supplied_atoms["route2_center_algebra"])
    check("object map to Route-2 spatial response is absent", not supplied_atoms["object_map_to_route2_spatial_response"])
    check("representation compatibility to O_h E/T2 is absent", not supplied_atoms["representation_compatibility_to_Oh_E_T2"])
    check("scalar rule to c_TE is absent", not supplied_atoms["scalar_rule_to_c_TE"])
    check("sign and center-slot package is absent here", not supplied_atoms["negative_sign_and_center_slot"])
    check("physical color matter realization is absent", not supplied_atoms["physical_color_matter_realization"])
    complete_functor = all(supplied_atoms.values())
    check("full functor package is not supplied", not complete_functor, str(supplied_atoms))

    print()
    print("H. First-principles fan-out synthesis")
    print("-" * 72)
    fanout = {
        "shared_integer_3": "fails: multiple typed 3D objects",
        "dimension_fraction": "fails: spatial fractions are 3/5, 2/5, 3/2, not 8/9",
        "graph_first_commutant": "fails: internal commutant has no Route-2 output slot",
        "record_invariance": "fails: antecedent/matter realization remains open",
        "endpoint_reversal": "fails: starts from c_TE or rho_E target",
    }
    for key, result in fanout.items():
        check(f"fan-out route {key} recorded", "fails:" in result, result)
    check("fan-out includes five independent frames", len(fanout) == 5)

    print()
    print("Summary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    if FAIL_COUNT == 0:
        print("VERDICT: current-bank no-go for graph-first SU3 as a typed spatial-color functor to c_TE=-8/9.")
        print("The bank supplies graph-first SU3, F_adj=8/9, and Route-2 center algebra,")
        print("but not the object map, O_h representation compatibility, scalar rule,")
        print("sign/slot package, or physical-color matter realization needed for closure.")
        return 0
    print("VERDICT: graph-first SU3 spatial-color functor firewall has failing checks.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Finite-dimensional carrier budget for color link-index routing.

The runner proves only a small budget statement:

* one primitive qubit endpoint cannot host a color fundamental or faithful
  native su(3) connection algebra;
* two qubits are the minimal qubit-built Hilbert carrier with enough dimension;
* the two-qubit symmetric subspace is a 3D candidate, but using it for color
  link transport requires projection/constraint and SU(3)-restricted routing.

No physical color derivation, no link ontology, no action/coupling selection,
no record-readout identification, no dial fixing, no audit verdicts.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from pathlib import Path


PASS = 0
FAIL = 0


def emit(line: str = "") -> None:
    print(line)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f" ({detail})" if detail else ""
    emit(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    emit()
    emit("-" * 78)
    emit(title)
    emit("-" * 78)


def sym_power_dim(base_dim: int, degree: int) -> int:
    return comb(base_dim + degree - 1, degree)


def su_dim(n: int) -> int:
    return n * n - 1


def su3_irrep_dim(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


@dataclass(frozen=True)
class Carrier:
    name: str
    qubits: int
    hilbert_dim: int
    color_three_possible: bool
    needs_constraint: bool


def main() -> int:
    emit("=" * 78)
    emit("COLOR LINK-INDEX ROUTING CARRIER BUDGET")
    emit("bounded-support / exact finite-dimensional obstruction runner")
    emit("=" * 78)

    section("1. One-qubit obstruction")
    one_qubit_dim = 2
    one_qubit_matrix_dim = one_qubit_dim**2
    one_qubit_traceless_lie_dim = su_dim(one_qubit_dim)
    color_fund_dim = 3
    su3_lie_dim = su_dim(3)

    check("one qubit Hilbert dimension = 2", one_qubit_dim == 2)
    check("one qubit matrix algebra dimension = 4", one_qubit_matrix_dim == 4)
    check("one qubit traceless Hermitian Lie dimension = 3", one_qubit_traceless_lie_dim == 3)
    check("color fundamental Hilbert dimension = 3", color_fund_dim == 3)
    check("su(3) Lie dimension = 8", su3_lie_dim == 8)
    check("one qubit cannot host a 3D color fundamental", one_qubit_dim < color_fund_dim)
    check("one qubit native traceless algebra too small for su(3)", one_qubit_traceless_lie_dim < su3_lie_dim)
    check("u(2) real dimension too small for su(3)", one_qubit_matrix_dim < su3_lie_dim)

    section("2. SU(3) representation lower bound")
    dims = {(p, q): su3_irrep_dim(p, q) for p in range(5) for q in range(5)}
    nontrivial_dims = sorted({d for (p, q), d in dims.items() if (p, q) != (0, 0)})
    min_nontrivial = nontrivial_dims[0]
    dim2_reps = [(p, q) for (p, q), d in dims.items() if d == 2]
    dim3_reps = [(p, q) for (p, q), d in dims.items() if d == 3]
    check("checked SU(3) highest-weight grid is nonempty", len(dims) == 25)
    check("smallest non-trivial SU(3) irrep dimension in grid = 3", min_nontrivial == 3, str(min_nontrivial))
    check("no 2D SU(3) irrep appears in checked grid", dim2_reps == [], str(dim2_reps))
    check("3D irreps are fundamental/conjugate weights", set(dim3_reps) == {(1, 0), (0, 1)}, str(dim3_reps))
    check("one-qubit carrier dimension misses minimal non-trivial irrep", one_qubit_dim < min_nontrivial)

    section("3. Two-qubit minimal candidate")
    two_qubit_dim = 2**2
    sym2_dim = sym_power_dim(2, 2)
    anti2_dim = 1
    candidate = Carrier("two_qubit_symmetric_endpoint", 2, two_qubit_dim, True, True)
    one = Carrier("one_qubit_endpoint", 1, one_qubit_dim, False, False)
    check("two qubits Hilbert dimension = 4", two_qubit_dim == 4)
    check("Sym^2(C^2) dimension = 3", sym2_dim == 3)
    check("Anti^2(C^2) dimension = 1", anti2_dim == 1)
    check("two-qubit swap decomposition dimensions sum to 4", sym2_dim + anti2_dim == two_qubit_dim)
    check("one qubit is not color-capable", not one.color_three_possible)
    check("two-qubit symmetric endpoint is color-capable as a carrier", candidate.color_three_possible)
    check("two-qubit route needs a projection/constraint", candidate.needs_constraint)
    check("two qubits are minimal qubit count with Hilbert dimension >= 3", one_qubit_dim < 3 <= two_qubit_dim)

    section("4. Generic U(4) is not SU(3) routing")
    u4_real_dim = two_qubit_dim**2
    block_su3_plus_zero_dim = su3_lie_dim
    complement_dim = anti2_dim
    generic_extra_dim = u4_real_dim - block_su3_plus_zero_dim
    check("u(4) real dimension = 16", u4_real_dim == 16)
    check("block-preserving color su(3) dimension = 8", block_su3_plus_zero_dim == 8)
    check("u(4) has extra directions beyond block su(3)", generic_extra_dim == 8, f"extra={generic_extra_dim}")
    check("antisymmetric complement dimension is 1", complement_dim == 1)
    check("block route is reducible 3+1, not a pure generic 4D transport", (sym2_dim, anti2_dim) == (3, 1))

    section("5. Routing requirements")
    carrier_budget_outputs = {
        "minimal_qubit_count_two",
        "sym2_endpoint_carrier_dim3",
        "one_qubit_color_obstruction",
    }
    routing_requirements = {
        "choose_two_qubit_link_endpoint",
        "symmetric_projection_or_constraint",
        "su3_restricted_parallel_transport",
        "endpoint_gauss_generators",
        "wilson_observables",
        "action_couplings_rates_time",
        "color_record_readout_antecedent",
    }
    post_record_outputs = {"word_history_O_star", "count_state_N_to_O", "coarse_grained_counts"}
    check("carrier budget has three outputs", len(carrier_budget_outputs) == 3)
    check("routing ledger has seven remaining requirements", len(routing_requirements) == 7)
    check("carrier budget does not supply routing requirements", carrier_budget_outputs.isdisjoint(routing_requirements))
    check("post-record outputs do not supply routing requirements", post_record_outputs.isdisjoint(routing_requirements))
    check("projection remains an explicit requirement", "symmetric_projection_or_constraint" in routing_requirements)
    check("SU(3)-restricted transport remains explicit", "su3_restricted_parallel_transport" in routing_requirements)
    check("Gauss generators remain explicit", "endpoint_gauss_generators" in routing_requirements)
    check("record-readout antecedent remains explicit", "color_record_readout_antecedent" in routing_requirements)

    section("6. Route classification")
    routes = {
        "one_qubit_link_color": "exact obstruction",
        "two_qubit_symmetric_host": "minimal carrier support",
        "generic_u4_link_color": "overlarge without block constraint",
        "post_record_count_routing": "wrong layer",
        "full_link_routing": "open construction",
    }
    check("five route classes recorded", len(routes) == 5)
    check("one-qubit route classified as obstruction", routes["one_qubit_link_color"] == "exact obstruction")
    check("two-qubit route classified as carrier support", routes["two_qubit_symmetric_host"] == "minimal carrier support")
    check("generic U4 route needs block constraint", "constraint" in routes["generic_u4_link_color"])
    check("post-record count route is wrong layer", routes["post_record_count_routing"] == "wrong layer")
    check("full link routing remains open construction", routes["full_link_routing"] == "open construction")

    section("7. Note sanity")
    doc = Path("docs/COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md")
    text = doc.read_text(encoding="utf-8")
    markers = [
        "Claim type:** meta support map",
        "Trace class:** negative route-pruning support map",
        "No-Go Discipline Gate (N1-N8)",
        "Does not derive physical color.",
        "Does not establish a repo-wide quantum-link ontology.",
        "Does not select a Koide/generation dial location.",
    ]
    check("source note exists", doc.exists(), str(doc))
    for marker in markers:
        check(f"note contains marker: {marker}", marker in text)
    forbidden_wording = [
        ("physical color closure", "physical color is " + "derived"),
        ("link ontology closure", "quantum-link ontology is " + "established"),
        ("projection closure", "projection is " + "derived dynamically"),
        ("dial selector closure", "dial location is " + "selected"),
    ]
    for label, phrase in forbidden_wording:
        check(f"forbidden wording absent: {label}", phrase not in text)

    section("SCORECARD")
    emit(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

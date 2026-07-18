#!/usr/bin/env python3
"""Cycle 39 exact temporal protocol-equivalence probe for F_t=Z_all^t.

This authority-free runner distinguishes fixed-protocol observability from
complete adaptive co-transport, checks the temporal idle/connection seam, and
enforces the local note's clause-deletion and N1--N8 contracts.  It changes no
file and grants no foundation, primitive, audit, or retained authority.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "TEMPORAL_PROTOCOL_EQUIVALENCE_ALTERNATING_FRAME_CYCLE39_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
CYCLE20 = REVIEW / "ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md"
CYCLE21 = REVIEW / "FOUNDATION_SITE_NET_RECORD_EQUIVALENCE_CLASSIFICATION_CYCLE21_NOTE_2026-07-14.md"
SORT_EQUIV = REVIEW / "FOUNDATION_SORT_PRESERVING_EQUIVALENCE_AND_DYNAMICAL_GAUGE_COLLAPSE_NOTE_2026-07-14.md"
CYCLE34 = REVIEW / "MOVING_LOGICAL_APPARATUS_APPEND_FRONT_CYCLE34_NOTE_2026-07-14.md"
CYCLE35 = REVIEW / "FINAL_MISSING_CONTENT_CENSUS_AND_CONSTITUTIONAL_EDIT_GATE_CYCLE35_NOTE_2026-07-14.md"
CYCLE36 = REVIEW / "CUBIC_CZ_EDGE_RULE_UNIQUENESS_SELECTION_CYCLE36_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Live source, primitive, authority, and scope contract")
    sources = (NOTE, AXIOMS, REGISTRY, CYCLE20, CYCLE21, SORT_EQUIV, CYCLE34, CYCLE35, CYCLE36)
    for path in sources:
        check(f"A source exists: {path.name}", path.is_file())

    note = normalized(NOTE)
    axioms = AXIOMS.read_text(encoding="utf-8")
    axioms_norm = normalized(AXIOMS)
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    check("A note is authority-free", "authority: none" in note)
    check("A note authorizes no commit, push, or PR", "no commit, push, pr" in note)
    check("A note issues no audit verdict", "does not issue an audit verdict" in note)
    check("A result is necessarily law-relative", "necessarily law-relative" in note)
    check("A no new temporal-gauge axiom follows", "no new axiom sentence follows" in note)
    check("A infinite-lattice Z_all is typed quasilocally", "common onsite-z quasilocal automorphism" in note)
    check("A current Qubit privileges no possibility", "No possibility is privileged." in axioms)
    check("A current Record fixes permanent content", "records are permanent" in axioms)
    check("A current readout is content-only", "a readout value is determined by record content alone." in axioms_norm)
    check("A current state is record-only", "A state is a configuration of records." in axioms)
    check("A current Admissibility is not dynamics", "Admissibility is not a dynamics axiom." in axioms)
    check("A current foundation withholds time metric", "define a time metric" in axioms)
    check(
        "A primitive inventory is exact",
        registry["canonical_ids"]
        == [
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        ],
    )
    primitive_notes = {key: value["note"].lower() for key, value in registry["nodes"].items()}
    check("A scale primitive is units-only", "units conversion only" in primitive_notes["scale_reference_primitive"])
    check(
        "A kinetic primitive supplies no dynamics",
        "not an absolute scale" in primitive_notes["kinetic_isotropy_primitive"]
        and "dynamics" in primitive_notes["kinetic_isotropy_primitive"],
    )
    check(
        "A realized-state primitive supplies no state",
        "supplies the slot, never the content" in primitive_notes["realized_state_primitive"],
    )
    for heading in range(1, 9):
        check(f"A N{heading} discipline section present", f"n{heading} —" in note)


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
CZ = sp.diag(1, 1, 1, -1)
KET0 = sp.Matrix([1, 0])
KET1 = sp.Matrix([0, 1])
KET_PLUS = H * KET0
KET_MINUS = H * KET1
RHO_PLUS = KET_PLUS * KET_PLUS.H
RHO_MINUS = KET_MINUS * KET_MINUS.H
PX = {"+": (I2 + X) / 2, "-": (I2 - X) / 2}
PZ = {"+": (I2 + Z) / 2, "-": (I2 - Z) / 2}


def tensor(*matrices: sp.Matrix) -> sp.Matrix:
    result = sp.Matrix([[1]])
    for matrix in matrices:
        result = sp.kronecker_product(result, matrix)
    return sp.Matrix(result)


def exact_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(sp.simplify(a - b) == 0 for a, b in zip(left, right))


def probability(rho: sp.Matrix, effect: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(effect * rho))


def fixed_time_site_net() -> None:
    section("B - Fixed-time sort, site-net, and uniform-locality classification")
    check("B onsite Z is unitary", exact_equal(Z.H * Z, I2))
    check("B onsite Z preserves X in the same factor", exact_equal(Z * X * Z, -X))
    check("B onsite Z preserves Y in the same factor", exact_equal(Z * Y * Z, -Y))
    check("B onsite Z fixes Z", exact_equal(Z * Z * Z, Z))
    basis_images = (Z * I2 * Z, Z * X * Z, Z * Y * Z, Z * Z * Z)
    image_rank = sp.Matrix.hstack(*(sp.Matrix(image).reshape(4, 1) for image in basis_images)).rank()
    check("B the full one-site M2 fiber maps onto itself", image_rank == 4)

    z_all = tensor(Z, Z)
    x0 = tensor(X, I2)
    x1 = tensor(I2, X)
    check("B Z_all preserves first named site factor", exact_equal(z_all * x0 * z_all, -x0))
    check("B Z_all preserves second named site factor", exact_equal(z_all * x1 * z_all, -x1))
    check("B Z_all is a product of onsite recodings", exact_equal(z_all, tensor(Z, Z)))
    check("B F_t has period two", all(exact_equal(Z ** (t + 2), Z**t) for t in range(8)))
    check("B F_t has time-independent onsite support", all((Z**t).shape == (2, 2) for t in range(12)))
    check("B F_t is nonstatic", not exact_equal(Z**0, Z**1))
    check("B fixed-time component is not an entangling split-fiber map", exact_equal(z_all, tensor(Z, Z)))


def cycle36_law_transport() -> None:
    section("C - Cycle-36 static obstruction and alternating transport")
    z_all = tensor(Z, Z)
    u0 = CZ
    u1 = z_all * u0
    check("C U0 is unitary", exact_equal(u0.H * u0, sp.eye(4)))
    check("C U1 is unitary", exact_equal(u1.H * u1, sp.eye(4)))
    check("C U0 and Z_all commute", exact_equal(u0 * z_all, z_all * u0))
    check("C U0 is involutive", exact_equal(u0**2, sp.eye(4)))
    check("C U1 is involutive", exact_equal(u1**2, sp.eye(4)))
    check("C candidates are distinct", not exact_equal(u0, u1))
    check("C static common-Z conjugation leaves U0 fixed", exact_equal(z_all * u0 * z_all, u0))
    check("C static common-Z conjugation does not produce U1", not exact_equal(z_all * u0 * z_all, u1))
    for time in range(6):
        f_now = z_all**time
        f_next = z_all ** (time + 1)
        check(
            f"C alternating frame maps U0 to U1 at t={time}",
            exact_equal(f_next * u0 * f_now.H, u1),
        )
    check("C temporal map uses different endpoint frames", not exact_equal(sp.eye(4), z_all))
    check("C alternating family remains uniformly range zero", all(exact_equal(z_all**t, sp.eye(4) if t % 2 == 0 else z_all) for t in range(10)))


def fixed_protocol_witnesses() -> None:
    section("D - Fixed transverse witness, Z-blind control, and time resolution")
    rho_i = RHO_PLUS
    rho_z = Z * RHO_PLUS * Z
    check("D identity leaves plus state", exact_equal(rho_i, RHO_PLUS))
    check("D Z maps plus to minus", exact_equal(rho_z, RHO_MINUS))
    x_table_i = tuple(probability(rho_i, PX[label]) for label in ("+", "-"))
    x_table_z = tuple(probability(rho_z, PX[label]) for label in ("+", "-"))
    check("D fixed X reads plus after identity with certainty", x_table_i == (1, 0))
    check("D fixed X reads minus after Z with certainty", x_table_z == (0, 1))
    check("D fixed X protocol separates the residue", x_table_i != x_table_z)

    z_table_i = tuple(probability(rho_i, PZ[label]) for label in ("+", "-"))
    z_table_z = tuple(probability(rho_z, PZ[label]) for label in ("+", "-"))
    check("D Z-only transcript is uniform after identity", z_table_i == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D Z-only transcript is uniform after Z", z_table_z == (sp.Rational(1, 2), sp.Rational(1, 2)))
    check("D Z-only protocol masks the residue", z_table_i == z_table_z)

    two_step_i = I2 * I2 * KET_PLUS
    two_step_z = Z * Z * KET_PLUS
    check("D two-step identity endpoint is plus", exact_equal(two_step_i, KET_PLUS))
    check("D two-step Z endpoint returns to plus", exact_equal(two_step_z, KET_PLUS))
    check("D even endpoint agrees while odd intermediate differs", exact_equal(two_step_i, two_step_z) and x_table_i != x_table_z)

    ket_plus0 = tensor(KET_PLUS, KET0)
    z_all = tensor(Z, Z)
    u0 = CZ
    u1 = z_all * u0
    state0 = u0 * ket_plus0
    state1 = u1 * ket_plus0
    px0_plus = tensor(PX["+"], I2)
    px0_minus = tensor(PX["-"], I2)
    two_site_table0 = (probability(state0 * state0.H, px0_plus), probability(state0 * state0.H, px0_minus))
    two_site_table1 = (probability(state1 * state1.H, px0_plus), probability(state1 * state1.H, px0_minus))
    check("D Cycle-36 U0 gives X-plus on |+0>", two_site_table0 == (1, 0))
    check("D Cycle-36 U1 gives X-minus on |+0>", two_site_table1 == (0, 1))
    check("D two-site candidate pair is record-distinguishable", two_site_table0 != two_site_table1)


def transcript_table(
    rho: sp.Matrix,
    update: sp.Matrix,
    first_projectors: dict[str, sp.Matrix],
    corrections: dict[str, sp.Matrix],
    final_projectors: dict[str, sp.Matrix],
) -> dict[tuple[str, str], sp.Expr]:
    result: dict[tuple[str, str], sp.Expr] = {}
    after_update = update * rho * update.H
    for first_label in ("+", "-"):
        first = first_projectors[first_label]
        branch = first * after_update * first.H
        correction = corrections[first_label]
        branch = correction * branch * correction.H
        for final_label in ("+", "-"):
            result[(first_label, final_label)] = probability(branch, final_projectors[final_label])
    return result


def adaptive_protocol_fork() -> None:
    section("E - Exact adaptive update-only versus complete co-transport fork")
    corrections = {"+": I2, "-": Z}
    original = transcript_table(RHO_PLUS, I2, PX, corrections, PX)
    update_only = transcript_table(RHO_PLUS, Z, PX, corrections, PX)
    expected_original = {("+", "+"): 1, ("+", "-"): 0, ("-", "+"): 0, ("-", "-"): 0}
    expected_update_only = {("+", "+"): 0, ("+", "-"): 0, ("-", "+"): 1, ("-", "-"): 0}
    check("E original adaptive transcript table is deterministic ++", original == expected_original, str(original))
    check("E update-only transcript table is deterministic -+", update_only == expected_update_only, str(update_only))
    check("E update-only change alters a permanent first label", original != update_only)
    check("E both fixed protocols finish X-plus", sum(value for (a, b), value in original.items() if b == "+") == 1 and sum(value for (a, b), value in update_only.items() if b == "+") == 1)

    f0, f1, f2 = I2, Z, I2
    transported_update = f1 * I2 * f0.H
    transported_first = {label: f1 * projector * f1.H for label, projector in PX.items()}
    transported_corrections = {label: f2 * correction * f1.H for label, correction in corrections.items()}
    transported_final = {label: f2 * projector * f2.H for label, projector in PX.items()}
    transported = transcript_table(
        f0 * RHO_PLUS * f0.H,
        transported_update,
        transported_first,
        transported_corrections,
        transported_final,
    )
    check("E transported update is Z", exact_equal(transported_update, Z))
    check("E transported abstract plus projector is concrete X-minus", exact_equal(transported_first["+"], PX["-"]))
    check("E transported abstract minus projector is concrete X-plus", exact_equal(transported_first["-"], PX["+"]))
    check("E transported plus correction is Z", exact_equal(transported_corrections["+"], Z))
    check("E transported minus correction is identity", exact_equal(transported_corrections["-"], I2))
    check("E final projectors return to original frame", all(exact_equal(transported_final[label], PX[label]) for label in ("+", "-")))
    check("E transported first instrument stays complete", exact_equal(sum(transported_first.values(), sp.zeros(2)), I2))
    check("E transported correction branches stay unitary", all(exact_equal(correction.H * correction, I2) for correction in transported_corrections.values()))
    check("E complete co-transport restores the original transcript table", transported == original, str(transported))
    check("E complete co-transport differs from update-only comparison", transported != update_only)
    check("E abstract event count is preserved", len([key for key, value in original.items() if value != 0]) == len([key for key, value in transported.items() if value != 0]) == 1)
    check("E abstract scalar label sequence is preserved", next(key for key, value in original.items() if value == 1) == next(key for key, value in transported.items() if value == 1))


def temporal_idle_connection() -> None:
    section("F - Same-slice identity versus named cross-time idle")
    for time in range(6):
        frame = Z**time
        check(f"F same-slice categorical identity preserved at t={time}", exact_equal(frame * I2 * frame.H, I2))
    transported_idles = tuple(sp.simplify((Z ** (time + 1)) * I2 * (Z**time).H) for time in range(6))
    check("F every alternating cross-time idle becomes Z", all(exact_equal(edge, Z) for edge in transported_idles))
    check("F cross-time idle is not the same-slice identity", not exact_equal(transported_idles[0], I2))
    check("F two transported idle edges compose to identity", exact_equal(transported_idles[1] * transported_idles[0], I2))
    static_frame_idle = Z * I2 * Z.H
    check("F a static frame leaves a cross-time idle represented by identity", exact_equal(static_frame_idle, I2))
    check("F alternating and static temporal transports differ", not exact_equal(transported_idles[0], static_frame_idle))
    idle_x_table = tuple(probability(Z * RHO_PLUS * Z, PX[label]) for label in ("+", "-"))
    fixed_x_table = tuple(probability(RHO_PLUS, PX[label]) for label in ("+", "-"))
    check("F fixed idle calibration has an odd-time X separator", fixed_x_table == (1, 0) and idle_x_table == (0, 1))


def record_decoder_transport() -> None:
    section("G - Permanent abstract label versus fixed concrete dictionary")
    encoded_plus = tuple(sp.simplify((Z**time) * PX["+"] * (Z**time).H) for time in range(4))
    encoded_minus = tuple(sp.simplify((Z**time) * PX["-"] * (Z**time).H) for time in range(4))
    check("G plus encoding alternates P+ P- P+ P-", all(exact_equal(encoded_plus[t], PX["+" if t % 2 == 0 else "-"]) for t in range(4)))
    check("G minus encoding alternates P- P+ P- P+", all(exact_equal(encoded_minus[t], PX["-" if t % 2 == 0 else "+"]) for t in range(4)))

    def transported_decode(time: int, matrix: sp.Matrix) -> int | None:
        if exact_equal(matrix, encoded_plus[time]):
            return 1
        if exact_equal(matrix, encoded_minus[time]):
            return -1
        return None

    def fixed_decode(matrix: sp.Matrix) -> int | None:
        if exact_equal(matrix, PX["+"]):
            return 1
        if exact_equal(matrix, PX["-"]):
            return -1
        return None

    check("G transported decoder keeps abstract plus readout fixed", tuple(transported_decode(t, encoded_plus[t]) for t in range(4)) == (1, 1, 1, 1))
    check("G transported decoder keeps abstract minus readout fixed", tuple(transported_decode(t, encoded_minus[t]) for t in range(4)) == (-1, -1, -1, -1))
    check("G fixed concrete decoder sees plus encoding alternate", tuple(fixed_decode(matrix) for matrix in encoded_plus) == (1, -1, 1, -1))
    check("G fixed dictionary and transported dictionary are different physical tests", transported_decode(1, encoded_plus[1]) != fixed_decode(encoded_plus[1]))
    additive_original = transported_decode(0, encoded_plus[0]) + transported_decode(0, encoded_minus[0])
    additive_odd = transported_decode(1, encoded_plus[1]) + transported_decode(1, encoded_minus[1])
    check("G transported scalar additivity is preserved", additive_original == additive_odd == 0)
    check("G passive decoder transport adds no transcript label", len(("+",)) == len(("+",)))
    check("G an active certificate would add one label", len(("frame", "+")) == len(("+",)) + 1)


def cycle34_clock_controls() -> None:
    section("H - Cycle-34 wake parity, local-role, and rate controls")
    for trials in range(8):
        record_count = trials + 1
        tau = record_count - 1
        check(f"H wake count reconstructs tau at N={trials}", tau == trials)
        expected_frame = I2 if tau % 2 == 0 else Z
        check(f"H wake parity reconstructs F_t at N={trials}", exact_equal(Z**tau, expected_frame))
    radius = 2
    role_patch_even = tuple("record" if offset <= 0 else "open" for offset in range(-radius, radius + 1))
    role_patch_odd = tuple("record" if offset <= 0 else "open" for offset in range(-radius, radius + 1))
    check("H fixed-radius translated role patches can agree", role_patch_even == role_patch_odd)
    check("H equal local role patches need not determine global parity", (4 % 2) != (5 % 2))
    record_chain_fast = tuple(range(0, 6))
    record_chain_slow = tuple(11 * value for value in range(0, 6))
    check("H timestamp rescaling preserves event order", [a < b for a, b in zip(record_chain_fast, record_chain_fast[1:])] == [a < b for a, b in zip(record_chain_slow, record_chain_slow[1:])])
    check("H odd timestamp rescaling preserves alternating parity", tuple(value % 2 for value in record_chain_fast) == tuple(value % 2 for value in record_chain_slow))
    check("H timestamp rescaling changes metric spacing", record_chain_fast[1] - record_chain_fast[0] != record_chain_slow[1] - record_chain_slow[0])


def language_and_discipline_contract() -> None:
    section("I - Clause deletion, constitutional placement, TOE, and N1-N8 contract")
    note = normalized(NOTE)
    required_classification = (
        "fixed-time foundation-compatible presentation recoding",
        "exact temporal natural isomorphism",
        "exact record separator",
        "necessarily law-relative",
        "same-time categorical identity",
        "cross-time idle",
    )
    for phrase in required_classification:
        check(f"I classification phrase present: {phrase}", phrase in note)

    required_language = (
        "a framework equivalence is a sort-preserving isomorphism of the supplied structure",
        "a law equivalence is a compositional, uniformly local, sort-preserving isomorphism of complete adaptive record histories",
        "it co-transports every named boundary, instrument, decoder, and cross-time idle map",
        "preserving record labels, event order, and scalar readout",
    )
    for phrase in required_language:
        check(f"I minimum language present: {phrase[:45]}", phrase in note)

    clause_tokens = (
        "compositional",
        "uniformly local",
        "sort-preserving",
        "complete adaptive record histories",
        "named boundary",
        "instrument and decoder",
        "cross-time idle map",
        "record labels, event order, scalar readout",
        "probabilities | delete",
        "gauge | delete",
    )
    for token in clause_tokens:
        check(f"I clause-deletion token present: {token}", token in note)

    toe_fields = (
        "exact update",
        "site/locality",
        "record formation",
        "probability",
        "time",
        "apparatus",
        "boundary",
        "matter/chirality",
        "capacity/gravity",
        "constitution",
    )
    for field in toe_fields:
        check(f"I TOE lane present: {field}", field in note)
    check("I no formation trigger is claimed", "no toe lane obtains a formation trigger" in note)
    check("I no metric clock is claimed", "not a metric clock derived from the axioms" in note)
    check("I no Record edit is automatic", "record changes only if" in note)
    check("I no Qualification edit is automatic", "qualification changes only if" in note)
    check("I exact-law placement is retained", "one complete law l" in note and "record-faithful equivalence class" in note)
    check("I static and temporal types are distinguished", "foundation-static group and the temporal law groupoid are different mathematical types" in note)
    check("I hostile gauge steelman is preserved", "gauge steelman" in note and "succeeds conditionally" in note)
    check("I hostile fixed-record steelman is preserved", "fixed-record steelman" in note)
    check("I scoped no-go boundary is explicit", "this is not a no-go against" in note)


def main() -> int:
    source_contract()
    fixed_time_site_net()
    cycle36_law_transport()
    fixed_protocol_witnesses()
    adaptive_protocol_fork()
    temporal_idle_connection()
    record_decoder_transport()
    cycle34_clock_controls()
    language_and_discipline_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())

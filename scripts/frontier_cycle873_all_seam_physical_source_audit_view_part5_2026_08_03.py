#!/usr/bin/env python3
"""Byte-exact readable audit view of Cycle 873 all seam physical source, part 5/5."""

TARGET_SOURCE = "scripts/frontier_cycle873_recurrent_f17_all_seam_physical_core_2026_08_03.py"
PART_ORDINAL = 5
PART_COUNT = 5
FIRST_SOURCE_LINE = 1934
LAST_SOURCE_LINE = 2038
TOTAL_SOURCE_LINES = 2038
SOURCE_FINAL_NEWLINE = True
EXPECTED_SOURCE_SHA256 = "8f0f23d86cc83c433be3e86a66e719631c70da7fbd8a1adf6b85b65815448ad7"

# Payload rows are fixed UTF-8 source bytes before LF.  The acceptance runner
# validates every absolute line number and reconstructs the target byte-for-byte.
# C873SRC 001934|                "+pi/2 zero-site scalar restores the exact FSWAP representative"
# C873SRC 001935|            ),
# C873SRC 001936|            "grouping_boundary": (
# C873SRC 001937|                "the augmented factor is the complete grouped emitted M2 word; no "
# C873SRC 001938|                "claim is made that its four individual seam rotations separately "
# C873SRC 001939|                "preserve the affine star code before the group is complete"
# C873SRC 001940|            ),
# C873SRC 001941|        },
# C873SRC 001942|        "schedule_input_boundary": {
# C873SRC 001943|            "parity_origin": (
# C873SRC 001944|                "the owner-coordinate residues mod2 are computed relative to a "
# C873SRC 001945|                "supplied lattice parity origin"
# C873SRC 001946|            ),
# C873SRC 001947|            "color_traversal": (
# C873SRC 001948|                "the deterministic order of the 24 color templates is supplied "
# C873SRC 001949|                "compiler schedule phase"
# C873SRC 001950|            ),
# C873SRC 001951|            "proved": (
# C873SRC 001952|                "collision freedom, landed factor-order reconstruction, and the "
# C873SRC 001953|                "reported proper-frame/color transport on the three fixtures"
# C873SRC 001954|            ),
# C873SRC 001955|            "not_proved": (
# C873SRC 001956|                "unit-translation/origin-shift equivalence, physical-law translation "
# C873SRC 001957|                "compatibility, or host-free autonomous recurrence"
# C873SRC 001958|            ),
# C873SRC 001959|        },
# C873SRC 001960|        "primitive": primitive_certificate(),
# C873SRC 001961|        "semantics": (semantic_certificate(1), semantic_certificate(-1)),
# C873SRC 001962|        "semantic_mutations": semantic_mutation_certificate(),
# C873SRC 001963|        "persistent_recurrence": persistent_recurrence_certificate(),
# C873SRC 001964|        "unary_projector": unary_projector_certificate(),
# C873SRC 001965|        "secondary_optional_evidence": {
# C873SRC 001966|            "closure_role": "reported but excluded from collect_primary_failures",
# C873SRC 001967|            "Cycle714_coexistence": packet_join_certificate(),
# C873SRC 001968|        },
# C873SRC 001969|        "computational_basis_path_history_witness":
# C873SRC 001970|            computational_basis_path_history_witness(),
# C873SRC 001971|        "signed_transport": signed_transport_certificate(),
# C873SRC 001972|        "fixtures": fixtures,
# C873SRC 001973|        "coordinate_covariance": coordinate_covariance_certificate(catalog),
# C873SRC 001974|        "structural_route_deletions": structural_route_deletion_certificate(maximum_distance),
# C873SRC 001975|        "primary_supplied": (
# C873SRC 001976|            "one-hot initialization of every persistent 17-M2 F17 rail bank",
# C873SRC 001977|            "the bounded projector/domain restriction P1 and any enforcement",
# C873SRC 001978|            "typed G=n+/-div family and matched alpha=+/-1 polarity",
# C873SRC 001979|            "lawful Cycle870 encoded matter and signed local coframes",
# C873SRC 001980|            "a lattice parity origin and ordered 24-color traversal/schedule phase",
# C873SRC 001981|            "recurrence invocation, admission controls, and arbitrary returned-route substrate",
# C873SRC 001982|        ),
# C873SRC 001983|        "primary_derived": (
# C873SRC 001984|            "zero-unintended-overlap 20-M2 F17-only local banks",
# C873SRC 001985|            "exact ell->ell+alpha(n_u-n_v) on the supplied one-hot sector",
# C873SRC 001986|            "clean q_u/q_v/current work after every augmented seam",
# C873SRC 001987|            "unchanged Cycle870 seam/nonseam factors apart from the inserted F17 word",
# C873SRC 001988|            "24-color recurrent seam-stage route schedule with exact returned transit",
# C873SRC 001989|            "proper-frame endpoint swap, rail k->-k, and typed-polarity normalization",
# C873SRC 001990|        ),
# C873SRC 001991|        "open_nonclaims": (
# C873SRC 001992|            "no autonomous F17-bank genesis, one-hot projection, leakage correction, or reset",
# C873SRC 001993|            "no autonomous packet allocation, occurrence, admission, or clock law",
# C873SRC 001994|            "no unit-translation covariance or origin-shift equivalence theorem for the "
# C873SRC 001995|            "parity-color schedule, and no host-free recurrence law",
# C873SRC 001996|            "no source/charge sign identification and no mass-to-source map",
# C873SRC 001997|            "no gravity, Regge, backreaction, continuum, or downstream response claim",
# C873SRC 001998|            "authority and audit verdict remain unset",
# C873SRC 001999|        ),
# C873SRC 002000|    }
# C873SRC 002001|    failures = collect_primary_failures(report)
# C873SRC 002002|    secondary_failures = collect_secondary_optional_failures(report)
# C873SRC 002003|    report["primary_failures"] = failures
# C873SRC 002004|    report["secondary_optional_failures"] = secondary_failures
# C873SRC 002005|    report["secondary_optional_status"] = (
# C873SRC 002006|        "pass" if not secondary_failures else "diagnostic_fail"
# C873SRC 002007|    )
# C873SRC 002008|    report["failures"] = failures
# C873SRC 002009|    report["status"] = "pass" if not failures else "fail"
# C873SRC 002010|    output.write_text(json.dumps(json_safe(report), indent=2, sort_keys=True) + "\n")
# C873SRC 002011|    print(json.dumps({
# C873SRC 002012|        "status": report["status"],
# C873SRC 002013|        "base_commit": EXPECTED_BASE_COMMIT,
# C873SRC 002014|        "expected_base_is_ancestor_of_head": base_is_ancestor,
# C873SRC 002015|        "receipt": str(OUT.relative_to(ROOT)),
# C873SRC 002016|        "failures": failures,
# C873SRC 002017|        "secondary_optional_status": report["secondary_optional_status"],
# C873SRC 002018|        "secondary_optional_failures": secondary_failures,
# C873SRC 002019|        "fixtures": [{
# C873SRC 002020|            "shape": row["shape"],
# C873SRC 002021|            "seams": row["seams"],
# C873SRC 002022|            "F17_only_bank_union_M2": row["F17_only_all_seam_bank_union_M2"],
# C873SRC 002023|            "F17_only_logical": row["F17_only_total_macro_logical_instructions"],
# C873SRC 002024|            "F17_only_routed": row["F17_only_total_macro_routed_gates"],
# C873SRC 002025|            "colors": row["active_colors"],
# C873SRC 002026|            "F17_only_parallel_depth": row["F17_only_fixed_schedule_parallel_routed_depth"],
# C873SRC 002027|            "F17_only_route_union": row["F17_only_route_touched_union_M2"],
# C873SRC 002028|            "F17_only_support_union": row["F17_only_assigned_plus_route_support_union_M2"],
# C873SRC 002029|        } for row in fixtures],
# C873SRC 002030|    }, indent=2, default=json_default))
# C873SRC 002031|    return int(bool(failures))
# C873SRC 002032|
# C873SRC 002033|
# C873SRC 002034|if __name__ == "__main__":
# C873SRC 002035|    parser = argparse.ArgumentParser()
# C873SRC 002036|    parser.add_argument("--output", type=Path, default=OUT)
# C873SRC 002037|    arguments = parser.parse_args()
# C873SRC 002038|    raise SystemExit(main(arguments.output))

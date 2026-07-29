trace_class: direct_blocker_closure
target_claim_id: meson_gauge_invariant_os_transfer_representation_bounded_note_2026-05-30
target_blocker_text: "add an independent fixed-configuration four-field Wick/minor computation using the same finite M whose determinant weights the gauge average"
source_of_blocker_text: audit_ledger
reachability_to_target: closes
artifact_role: runner_certificate
next_trace_action: "independent audit should re-run the primary runner and inspect full_grassmann_packet plus meson_correlator_full_berezin"

# Reachability

The repaired runner forms `M`, `M^{-1}`, and `slogdet(M)` once per gauge background;
extracts both raw cross-reflection blocks and their temporal eigenvectors; evaluates the
full `2 x 2` Wick determinant minus its disconnected term; and compares it with the
independent Fock loop before and after the same determinant weights. This is the exact
artifact named by the blocker, not upstream support or frontier-only work.

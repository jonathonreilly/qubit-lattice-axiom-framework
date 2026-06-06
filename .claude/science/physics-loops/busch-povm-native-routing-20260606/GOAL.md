# Goal

Repair the conditional blocker on
`busch_povm_extension_on_qubit_lattice_narrow_theorem_note_2026-05-20`
without retagging the audit ledger.

The blocker asks for the Busch 2003 / CFMR 2004 theorem authority, or a
retained standard-math import node, with hypotheses matching the parent
POVM-additivity assumptions. This branch takes the framework-native route:
wire the parent note to the existing `M_2(C)` effect-Gleason bridge, add the
missing runner cache, and spell out the multi-site projection/spectral
extension.

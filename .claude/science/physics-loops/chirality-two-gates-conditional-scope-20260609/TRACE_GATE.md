# Trace Gate

Target:
`chirality_gate_is_two_independent_gates_dirac_vs_generation_scoping_note_2026-06-08`

Blocker:
`missing_bridge_theorem: add a retained bridge deriving the separate L/R gamma_5 and spin-statistics use from the Cl(3,1) extension, or narrow the note to the conditional tensor-product separation only.`

Repair:
This PR takes the narrowing path. The source claim is now a bounded conditional
finite-dimensional theorem: given `(generation R^3) x (L+R)`,
`gamma_5 = I_3 x sigma_3`, `beta = I_3 x sigma_1`, and
`Gamma_chi = (2/3)J-I`, Dirac/spinor chirality and Koide/generation chirality
are independent gates.

Non-claim:
The PR does not derive `gamma_5` from `Cl(3,1)` and does not prove the
spin-statistics use of that grading.

# Trace Gate

Target:
`fixed_gbare_interacting_existence_ir_target_reframing_bounded_note_2026-06-08`

Blocker:
`dependency_not_retained: close the G_BARE_DERIVATION_NOTE.md parent re-audit gate and either cite a retained RG/asymptotic-scaling authority or narrow/remove the two-loop ratio diagnostic.`

Repair:
The current ledger records `g_bare_derivation_note` as `retained_bounded`,
`audited_clean`, and `bounded_theorem`. This PR takes the second repair path:
it removes the old two-loop/asymptotic-scaling diagnostic from the retained
surface and narrows the packet to a framework-native fixed-`g_bare=1` target
clarification.

Guard:
The runner now fails if the source note reintroduces the old load-bearing RG
diagnostic strings (`b_1=26`, two-loop/one-loop diagnostic, finite
dimensional-transmutation scale, or `mu_conf/mu_lattice`).

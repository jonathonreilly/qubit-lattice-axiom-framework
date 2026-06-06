# Goal

Repair the U(1) sign-convention inconsistency in
`axiom_first_lattice_noether_theorem_note_2026-04-29`.

The audit row reports that the note's Step 4a convention used `-i` to convert
the imaginary-generator current to the real charge current, but the displayed
formula requires `+i`. This branch fixes the convention text and strengthens
runner E5 with a nonzero scalar guard for the sign.

# Goal

Repair the Choi normalization convention conflict in
`kraus_choi_representation_on_qubit_lattice_narrow_theorem_note_2026-05-20`.

The audit row reports that the note used both normalized and unnormalized
maximally entangled vector conventions while keeping an inverse formula that
is only correct without the normalized-vector factor. This block makes the
source convention unnormalized throughout and adds a runner that checks the
factor explicitly.

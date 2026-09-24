# Narrow correction to the frozen general target note

Root acceptance of independent comparison feedback, 2026-09-23.

The frozen BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md, bound by
GENERAL_TARGET_AUTHOR_SEAL.json SHA256
630f063e8fd546c844dba720943198070c49573d9de1c3870531ec40791e373f,
contains at line97 the overbroad sentence:

> All displayed operators are self-adjoint.

Read that sentence instead as:

> Both Hamiltonian coefficients H2^C and H4^C are self-adjoint.

The raw graph-coordinate fourth coefficient is generally non-Hermitian when
[M,C0] is nonzero, and B_j is generally not self-adjoint. The adjacent
canonical-normalization derivation already distinguishes the graph matrix
from the canonical Hamiltonian. No equation, assumption, proof estimate or
claimed effective generator changes. The original source remains immutable;
this correction must accompany it in publication and downstream use.

The independent PRE report and exact noncommuting-block controls identified
this wording issue during authorized post-PRE source comparison. That PRE seal
is 0504a3fc90cca1b0f9b7bab3a1aa346b11e0889bc25abf55bd65966965375a46.
The root accepted the correction; final comparison evidence is pending when
this correction was written. This is not a formal audit disposition.

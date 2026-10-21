# Finite affine-chart CP comparison under supplied pairing

**Type:** bounded_theorem
**Status:** supplied-model conditional result; physical path/selection open
**Primary runner:** `scripts/frontier_abcc_cp_phase_no_go_theorem.py`

The companion computes the pin and two locally fitted candidate matrices under the supplied row pairing (2,1,0); Basin X is fitted under (2,0,1) and then read under (2,1,0). It compares their sine readouts against the historical supplied threshold 0.247. These are finite conditional comparisons, not a complete basin search or current experimental confidence statement.

## Inertia does not force CP sign

For a Hermitian H with simple eigenvalues and fixed row/column ordering, conjugation preserves eigenvalues, determinant and inertia while conjugating its eigenvectors. The Jarlskog quartet changes to its conjugate, so its imaginary part changes sign. A nonzero J therefore cannot be determined by inertia alone. The runner checks this using the supplied pin and its conjugate. The conjugate flips the chart's fixed imaginary source sign; this is not asserted to be a second solution inside that restricted positive-gamma chart. A chart-specific sign theorem would need an additional proof.

The printed pin and two candidate signs remain numerical results. They do not show that every negative-determinant chart point has positive J. The pairing convention and displayed candidates are explicit inputs; neither is physically selected here.

## Comparison boundary

The old T2K/NuFit labels and significance claims are not independently revalidated by this repair. The runner retains their numeric cuts only as supplied historical comparators. Translating a phase confidence region into a sine region requires its full interval and ordering conventions; this note makes no new experimental exclusion. A future observation could test the specified chart, pairing and selected point jointly, not falsify an entire framework merely from these finite examples. Physical source selection and exhaustive basin coverage remain open.

## Recovery and context

Original source is recoverable at Git `f24d17d97d372df977476e4a69674577f31af575` under this path. Related notes are context/definitions, not blanket retained authority:

- [sigma_hier_uniqueness_theorem_note_2026-04-19](SIGMA_HIER_UNIQUENESS_THEOREM_NOTE_2026-04-19.md)

# Fix list

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

A row appears here only when the note is wrong or overclaims. One finding, one later repair. This file does not change claim status.

## Note 1737

- Path: `docs/QUARK_CP_SMALL_CORRECTION_BOUNDARY_NOTE_2026-06-17.md`
- Defect: The shipped complex 1-3 carriers are not a small correction to the Schur base. Caps at 1, 2, and 5 exclude the shipped fit.
- Evidence: On the printed digits, `|xi_u| / |c13_u(base)|` agrees with 101.908728437 and `|xi_d| / |c13_d(base)|` agrees with 6.643337509. Relative square error is below 1e-8. Both ratios sit above 5. Printed inputs: `xi_u = +0.340735147 - 0.063202935 i`, `xi_d = +0.078186196 + 0.108371050 i`, `c13_u(base) = 3.400565729750e-03`, `c13_d(base) = 2.011510840850e-02`.
- Edit: Stop calling the shipped fit a small correction inside those caps. State the ratios and that the caps exclude it.
- How this row was made: extracted from the prior read. The ratio check was repeated. The rest of the note was not re-read in this pass.

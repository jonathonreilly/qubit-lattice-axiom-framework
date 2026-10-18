# Review of the spin-½ / spin-1 common-cone lane note

Provenance: a fresh-context reviewer of the same model family. It wrote its own code, by different routes. Saved by the supervisor from the hand-back.

**Verdict:** needs changes, all small (scoping and wording). No claim is wrong.

## Results

| Run | Result | Time |
|---|---|---|
| Runner default | PASS=65 | 152 s |
| Runner `--full --diag` | PASS=73 | 879 s wall (532 s CPU) |
| `chk_continuum.py` (reviewer) | 15/15 | — |
| `chk_lattice.py` (reviewer) | 12/12 | — |
| `chk_stag_generator.py` | diagnostic | — |

## Confirmed by different routes

- **N1:** field-space commutators of affine generators. New: any constant symmetric g₀ also closes.
- **N2:** generic quadratic vector fields, with a sign control. The remainder vanishes for conformal Killing fields.
- **X5/X6:** a ker(div) nullspace (dimension 129 at L = 4), and a separate sampler.
- X8–X10.
- **X12b:** a separate sparse Poisson engine; closes only at (1,1) on a 3×3 grid.
- Y7, Y8, Y9 (full O_h).
- **Staggered diagnostic:** a doubler-momentum part 1.5–2.0× the smooth part.

**Tests that cannot fail:** Y3 (it solves g − κI = 0), W5's arithmetic parts, X13 (automatic), and X12's 2κ (linearity).

## Required edits

- R1: a constant anisotropic g₀ also closes {G, G}. So structure-function isotropy is supplied, or comes from cubic covariance.
- R2: "conformal Killing".
- R3: make Y3 non-tautological.
- R4: frame X13 as automatic.
- R5: replace the "Not checked by anyone independent" text with this review.
- R6: Isham–Kuchař citation corrected; arXiv:2305.10097 marked unverified.

**Optional:** the runner times, "Maxwell mode" rather than "photon", and the W5 assembly sentence.

All edits were sent to the note writer, together with the B19 check's status.

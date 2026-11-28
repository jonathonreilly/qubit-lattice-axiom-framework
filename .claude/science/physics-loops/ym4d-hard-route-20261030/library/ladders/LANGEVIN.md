# Ladder LANGEVIN: large-N clustering at bare order-one coupling by Langevin tangents (row 1709)

Target (row 1709, library/gap-largen-build-astra62.md): for lambda = g^2 N in [1, 2], exponential clustering uniform in volume and rank for N >= N0(lambda), and a transfer gap. Theorem 4 (PROVED, unchecked) reduces it to one finite polynomial inequality (6): a positive bounded-range quadratic form Q on tangent data whose energy decreases under the leading generator with a positive margin.

| Rung | Statement | Status | Row | Gate |
|---|---|---|---|---|
| LV1 | Theorem 4 and the identities (1)-(5), (13), (14), (18), (21), (23), (24) | PROVED (unchecked) | 1709 | check 1731 |
| LV2 | A positive local form Q satisfying (6) at one lambda in [1, 2]: must use matrix (colour-plane) weights, not scalar trace weights (Lemma 5), and survive the expansion (24) of planes chosen after observation | in progress | 1732 | form written, inequality proved or certified exactly |
| LV3 | Certified search for Q: (6) is a finite polynomial inequality, so a sum-of-squares certificate in exact arithmetic (Lemma OU of row 1682 for rounding) can prove it; Lean-check the certificate | open | | Lean kernel |
| LV4 | Running coupling: carry the comparison to a blocked action (row 1709 section 8) | open | | |

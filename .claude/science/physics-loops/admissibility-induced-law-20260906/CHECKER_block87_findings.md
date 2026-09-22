# Block 87 — control and findings (2026-09-22)

1. Disjoint machinery (`specs/supervisor_control_block87_wall_cost.py`): floating-point spectra on rings and tori, zone sums; the runner is exact symbolic algebra and an exact quadratic form.
2. **A level rule found and then checked exactly (supervisor).** Executed wall energies on rings were length-independent to six places; the rule "two sharp walls replace `±δ, ±1` by `0, 0, ±√(1 + δ²)`" was then verified as an exact multiset identity on rings of 4, 8, 12. A general proof is missing and said so.
3. **Sign of the tension by concavity**, not by numerics; the control's first tension formula had the wrong sign and a factor of two and was corrected against the direct three-dimensional difference (agreement to six places at `δ ≥ 0.3`).
4. **The law's reward checked coupling by coupling**: only `α` changes at a slip; confirmed by a local count and on `8³` with random couplings.
5. Finding: the domain criterion along the balance is a condition on the split of block 59's stiffness (walls iff `β` carries less than about `0.004–0.023` of `κ` between `κ = 0.125` and `0.09`).
6. Decimal literals in message strings tripped the float scan in a first draft; replaced by fractions.

# BLEAK-1 report: set B's RP-safe gravity bridge and the matter light cone

**Author.** Claude Opus 5.5. Same model family as the rest of the exercise; not refereed. The supervisor saved this file from the worker's final message, because the harness would not let the worker write REPORT.md.

## Reading: LEAK-PLANCK

**Result.** In R19-33's reflection-positive D2 realization (spatial-TT graviton plus instantaneous bridge), one graviton loop moves a massless scalar off the grid light cone by exactly

**δc = (π/6)·(ℓ_P/a)²**

At a = ℓ_P that is 0.524, about 5.7 decades above the 10⁻⁶ line.

- **Proved:** the closed form.
- **Checked, four ways:**
  1. 4D brute force with Richardson extrapolation: 0.523597;
  2. an exact time integral plus a 3D grid, reaching −1/96 to 10 digits;
  3. finite-p with full vertices;
  4. identity checks.

**Caveat (reading).** At a = ℓ_P the expansion parameter G/a² is 1, so the one-loop number is an exact coefficient, not a controlled prediction.

## The control premise was wrong

TESTS.md assumed K2's exactly conserved stress would give zero through the same loop. It does not: through the TT + bridge loop it gives the same π/6 as D2.

- **Why:** the identity "TT + bridge = covariant exchange on conserved sources" does not hold inside the loop, because the internal matter line is off shell (proved). Only the fully covariant graviton gives zero, and that graviton fails reflection positivity.
- **Mechanism:** the vertex divergence is proportional to the internal inverse propagator. The foliated-minus-covariant difference therefore cancels the matter propagator and leaves a UV contact term, ∝ G/a², whose coefficient depends on the chosen time axis.
- **Contributions:**
  - the spatial-TT gravitons contribute exactly 0;
  - D2's order-a² stress change contributes 0 at dimension 4 (it enters at O(p⁴));
  - the leak comes entirely from the instantaneous bridge.
- **What would cancel it:** a two-graviton–two-matter seagull vertex. R19-33's realization has none, and K2 showed that exact O(κ²) closure is impossible for strictly local matter.

## Plain words

- Set B's selling point was that the 90° time–space turn puts every particle on one light cone.
- To make gravity reflection-positive, R19-33 split it into wave gravitons plus an instantaneous Newton-type pull. That split picks out a time axis.
- The leak comes from the instantaneous part, so it is the price of having a time axis, not of D2's lattice detail.
- **Fermions leak too, by a different amount.** A Wilson fermion comparator, using the worker's own point-split stress choice, gives about 0.85·(ℓ_P/a)². Because the shifts differ between species, this is not just a redefinition of c.

**Grid scales that would pass:**

| Bound on \|δc\| | Grid spacing needed | Energy scale |
|---|---|---|
| 10⁻⁶ | a ≥ 724 ℓ_P | 1/a ≤ 1.7e16 GeV |
| 10⁻¹⁵ | a ≥ 2.3e7 ℓ_P | 1/a ≤ 5.3e11 GeV |
| 10⁻²¹ | a ≥ 2.3e10 ℓ_P | 1/a ≤ 5.3e8 GeV |

The alternative is one tuned counterterm per species per loop order, which is set C's bill.

**Consequence (reading).** R19-28's "charge block = 0 by W(B4) at all orders" does not survive reflection-positive gravity. Because the leak is a local term, this is a price, not a wall.

## Results table (δc in units of G/a²)

| Case | Stress | Kernel | One-loop row |
|---|---|---|---|
| C0, pure W(B4) | K2 | covariant | 0 (proved; checked ≤ 6e-17) |
| C1, "conserved control" | K2 | TT + bridge | π/6 |
| M1, target | D2 | TT + bridge | π/6 (identical to C1 at dimension 4) |
| M2, diagnostic | D2 | covariant | 0 at dimension 4 |
| Wilson fermion, covariant | point-split stress | covariant | ≤ 3e-13 |
| Wilson fermion, foliated | point-split stress | TT + bridge | 0.850 (stress-choice dependent; no RP bridge for fermions exists on record) |

**Closed form.** After the exact time integral and cubic averaging, the difference integrates to 1/32 − 1/24 = −1/96, and Watson's constant cancels.

## Scope and deviations

- **Not established:**
  - the photon's and graviton's own one-loop rows;
  - m > 0;
  - other zero-mode prescriptions;
  - two loops;
  - link reflection positivity.
- **Memory:** one run (`b1_row.py`, 2¹⁷ chunk) peaked at 443 MB, over the 0.4 GB cap. It was rerun at 245 MB with identical results.
- **PREREG timestamp:** the header says "~21:25Z" but the file time is 21:20:22Z. Both are before the first run (21:22:09Z), and the file was not edited afterwards.
- **Additions not named in PREREG:**
  - the exact-time-integral route, added for the closed form;
  - the fermion comparator, which PREREG allowed "if time remains".

## For panel D

This matches the gravity panelist's own decision table: "D3 → set C firmly; set B survives only with a sub-Planckian grid."

## Files

`PREREG.md` and `scripts/`:
- `b1_core.py`
- `b1_checks` (`.py` / `.out`)
- `b1_row` (`.py` / `.out` / `.time`), plus the rerun
- `b1_semi` (`.py` / `.out`)
- `b1_finite_p` (`.py` / `.out`) and `b1_mem.out`
- `b1_wilson` (`.py` / `.out`)
- `b1_richardson.out`

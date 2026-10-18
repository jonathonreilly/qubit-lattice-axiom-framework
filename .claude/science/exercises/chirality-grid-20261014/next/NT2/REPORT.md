# NT-2 report: is the hard plaquette bound |arg U_p| < δ reflection-positive in 3D pure U(1)?

**Author.** Claude Opus 5.5 test agent NT-2, 20:44–21:19Z. Same model family as everything else; not refereed. The supervisor saved this report from the worker's final message, because the worker's tool refused to write the file.

## Reading: PG3-NEG

In 3D pure U(1) with no fermions, the flat bound |arg U_p| < δ is **not** reflection-positive under link reflection:
- **proved exactly** on the 2×2 periodic slice and on the 1×2 open strip;
- **quadrature-converged negative** on the open 2×2 block, using smooth test functions.

## Memory incident

- **First run.** `t22_ring.py unres 0.4 32 32` (PID 26910) was launched with no size estimate. Its main array was about 10 GB, and the supervisor killed it at 5.2 GB.
- **Guard added.** After that, a size guard and an RSS watchdog (`capped.sh`) were in place.
- **Watchdog kills.** The watchdog killed the plane-pool runs at 458 MB (under 0.2 s over the cap) and `o22_check` at 317 MB.
- **Reported runs.** No reading uses a killed run. Every reported run peaked at or below 0.36 GB.

## Plain words

1. **The 2×2 periodic slice (T22) is proved not positive.**
   - **The witness:** six admissible configurations — a checkerboard flux s ∈ {−0.55, 0, 0.55}, with both row Wilson lines at 0 or 0.05.
   - **The proof:** exact rational arithmetic gives inertia (5, 1), and an explicit vector gives −27/12500·(2π)⁻³.
   - **Range:** because the kernel is homogeneous, this holds for every 0 < δ < π/4.
2. **Mechanism.** In 3D, the coefficient of the Wilson-line cusp is a flux kernel, B(σ) = (2δ)² − σ²/2, which has one negative direction. In 2D the cusp only added positive weight (K2c's "masking"). So a test function that is odd in the Wilson line and curved in the flux goes negative at first order.
3. **The open slices fail too:**
   - O12: proved for all δ < π/3 (exact inertia (15, 1));
   - O22: converged;
   - 1×3, 1×4 and 1×5 strips: negative, growing from −1.8e-6 to −3e-5 relative.
4. **This answers the K2c referee's open point.** Restricting the boundary spatial plaquettes does not rescue positivity.
5. **What it means for the price P-X3d.**
   - X3's hard measure already fails OS positivity in its gauge sector, independently of the overlap.
   - Keeping the support |θ| < δ but using a positive-type profile (for example the triangle 1_{δ/2} ⋆ 1_{δ/2}) restores pure-gauge reflection positivity on every lattice (Osterwalder–Seiler).
   - The profile is law data, not an axiom change: AX:63-73 reads "admissible" as support.
   - It does not rescue set B, because the overlap fails under positive-type weights as well (K2c; panel D lattice lens).

## Verdicts

| Item | Verdict |
|---|---|
| T22 (primary) | NEG (proved: exact inertia (5,1); scaling in δ; checked on several pools) |
| O22 (primary) | NEG (checked: λ_min −1.6e-3 to −5.7e-3, error estimate ≤ 7e-7) |
| O12 (secondary) | NEG (proved: exact inertia (15,1)) |
| O13/O14/O15 | NEG (checked) |
| All four Wilson lines matched | PSD (proved: Fourier transform sinc⁴ ≥ 0) |
| Plaquettes fixed, Wilson lines varying; holonomy-charge-0 sector | PSD (proved) |
| Random and hill-climb pools | PSD, low power |
| **Overall** | **PG3-NEG** |

## Key numbers

| Pool | Relative λ_min/λ_max | Error estimate |
|---|---|---|
| T22 R-line ring | −9.8e-3 | 2.5e-8 |
| T22 independent builder | −1.6e-3 | 1.1e-14 |
| T22 octahedron grid | −5.6e-3 | 3.6e-8 |
| T22 at δ = 0.3 / 0.45 / 0.75 | about −1.5e-3 | — |
| O12, 16² grid | −3.0e-6 | — |
| O22, smooth test functions | −1.2e-5 to −2.9e-5 | ≤ 7e-7 |

Controls:
- the 2D proxy reproduces K2c to all printed digits;
- unrestricted configurations give power references;
- the smooth-test-function code reproduces the exact O12 eigenvalue.

## Scope

- Finite 3D lattices, link reflection, β_g = 0, flat indicator.
- O12's structure also covers two perpendicular plaquettes in a 4D slice.
- Larger tori, full 4D slices, infinite volume and non-abelian groups are not tested; non-reflection-positivity there is **suggested**.

## Corrections owed

- K2c and its referee say the bound is "3D/4D suggested not RP". For 3D this should now read "not RP": proved on the 2×2 torus and the 1×2 strip, converged on the open 2×2 block.
- K2c's report should also say that the 2D even-Lx positivity does not carry over to 2D slices in 3D.

## Files

`PREREG.md` (with dated follow-up F1) and `scripts/` (all `.py` and `.out` files, each recording its peak memory).

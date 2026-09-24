---
claim_id: uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Layer units form uniform ice on infinite prisms in the zero-flux sector (landed, PR 8740) by the exact law P(v'|v) = T(v', v) psi(v') / (lam_0 psi(v)), with T the symmetric layer transfer and psi its top vector; the law of one layer is psi^2, and all the non-locality sits in psi. A Gaussian divergence-free field gives ln psi = const - G(v)/4 with G(v) = sum_q |E_q|^2 / (A S_q), E the staggered field over the layer and S_q = sqrt(Q/(Q+4))/K (open PR 8871). On 2 x 4, 2 x 6, 2 x 8 and 4 x 4 (computed by row transfer, landed PR 8859): the law sums to 1 at 200 sampled layers per shape (deviation below 1e-9); with S_q measured from psi^2, ln psi is linear in G with weighted R^2 of 0.9974 to 0.9989 and slope -0.2318 to -0.2464 (-1/4 within 8%, within 2% on the square); with the predicted kernel from K = 2 c(2) alone, R^2 is 0.9795 to 0.9901 on the strips and 0.9989 on the square, with slope within 3% of -1/4. The Gaussian law, proportional to T(v', v) exp(-G(v')/4) with the predicted kernel, is within 1.3% of the exact law in total variation at every sampled layer, and within 0.24% on the square. The kernel K sqrt((Q+4)/Q) tends to 2K/|q|, and on a 2048 x 2048 layer its transform U satisfies (U(r) - U(2r)) 2 pi r / K = 1 within 1e-3 along an axis and 5e-3 along the diagonal for r = 8, 16, 32: a 1/r flux interaction within the layer. No limit beyond the computed cross-sections is claimed for the Gaussian form. No constant is compared with an outside value. No reading, rule, alphabet, unit or order law is adopted."

upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.py
---

# Uniform ice: the layer vacuum is a Gaussian flux functional, so the layer-unit law carries a 1/r flux interaction

**Date:** 2026-09-23
**Type:** bounded_theorem
**Campaign:** second next-steps campaign. The landed layer-unit note (PR
8740) forms uniform ice exactly on every infinite prism, layer by layer, in
the zero-flux sector. An open edge of the assembly asks what exact
formation by layer units becomes on an infinite cross-section. This block
identifies the exact law's form.

## Result up front

1. **Where the non-locality sits.** With T the symmetric layer transfer
   and ψ its top vector (eigenvalue λ_0), the exact law of a new layer v′
   given the layer v below is

   P(v′ | v) = T(v′, v) ψ(v′) / (λ_0 ψ(v)).

   The law of one layer is ψ². T is local: a product of row tensors. All
   the non-locality of the law sits in the vacuum amplitude ψ.

2. **What a Gaussian field predicts for ψ.** A Gaussian divergence-free
   field gives a layer the weight exp(−(1/2) Σ_q |E_q|²/(A S_q)). Here E is
   the staggered field (−1)^(x+y)(2v − 1) over the layer, E_q its
   transform, and S_q = √(Q/(Q + 4))/K its equal-layer correlation (open
   PR 8871). Since the layer law is ψ²,

   ln ψ = const − G(v)/4,   G(v) = Σ_q |E_q|²/(A S_q).

3. **The vacuum is Gaussian.** On 2 × 4, 2 × 6, 2 × 8 and 4 × 4, computed
   by the row transfer of the landed note of PR 8859:
   - with S_q measured from ψ², ln ψ is linear in G: weighted R² from 0.9974
     to 0.9989, slope from −0.2318 to −0.2464. The slope approaches −1/4 as
     the cross-section grows and is within 2% of it on the square;
   - with the kernel predicted from K = 2c(2) alone, R² is 0.9795 to 0.9901
     on the strips and 0.9989 on the square, with slope within 3% of −1/4.

4. **The formation law has a closed form.** The Gaussian law,
   proportional to T(v′, v) exp(−G(v′)/4) with the predicted kernel, is
   within 1.3% of the exact law in total variation at every sampled layer.
   On the square it is within 0.24%. So the exact layer-unit law is a local
   transfer times a Gaussian flux functional, with nothing fitted beyond
   the flux cost.

5. **The functional is long-ranged.** The kernel K√((Q + 4)/Q) tends to
   2K/|q| at small q. Its transform U in the plane falls as K/(πr): on a
   2048 × 2048 layer, (U(r) − U(2r)) · 2πr/K equals 1 within 1e-3 along an
   axis and within 5e-3 along the diagonal for r = 8, 16 and 32. The
   functional is a 1/r interaction between flux elements of the formed
   layer.

6. **What this means for the open edge.** On every computed prism the
   exact layer-unit law is local transfer times the photon's Gaussian
   vacuum functional. The functional's kernel has the 1/|q| form of a free
   field's vacuum, and in the layer it is a 1/r interaction. In the Gaussian
   reading, the law on an infinite cross-section therefore has the same
   closed form: a local transfer times a 1/r flux interaction within the new
   layer, with its strength fixed by the flux cost. This is consistent with
   the landed result that finite joint cell units reach rows but not blocks
   (PR 8720): the law asks every flux element of the new layer to feel every
   other, falling off as 1/r. It is the gapless chain of the landed note of
   PR 8864, seen within one layer.
   No constant is compared with an outside value.

## Machine status and trace

- **Runner:**
  `scripts/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.py`
- **Result:** `TOTAL: PASS=5 FAIL=0`, about 59 s, stdout 1213 characters,
  peak about 745 MB.
- **Cache:**
  `logs/runner-cache/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.txt`
- **Arithmetic:** exact integer row tensors; the vacuum and flux-sector
  tops by Lanczos iteration (tolerance 1e-12); weighted least squares for
  the vacuum fit; the formation law column by column at 200 layers per
  shape drawn from ψ² with a fixed seed; the kernel's transform by FFT on a
  2048 × 2048 grid.

## Premises and declared objects

- **Layer units:** the landed note
  `UNIFORM_ICE_BY_LAYER_UNITS_ON_INFINITE_PRISMS_IS_EXACT_IN_THE_ZERO_FLUX_SECTOR_THAT_LONG_PRISMS_SELECT_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  (PR 8740).
- **Row transfer and flux cost:** the landed notes
  `UNIFORM_ICE_FLUX_STIFFNESS_ON_A_SQUARE_CROSS_SECTION_BY_ROW_TRANSFER_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  (PR 8859) and
  `UNIFORM_ICE_LAYER_TRANSFER_FLUX_SECTORS_CARRY_A_GAUSSIAN_STIFFNESS_INVERSE_IN_THE_CROSS_SECTION_BOUNDED_THEOREM_NOTE_2026-09-23.md`
  (PR 8746). T maps the flux S of a layer to −S, so a flux sector is
  |S| = s.
- **Gaussian flux functional:** G(v) as defined, with the predicted kernel
  from open PR 8871.
- **Comparison field:** built from the Z^3 graph Laplacian of the landed
  note
  `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`.

## Prior art and what is new

- Landed PR 8740: the layer-unit law is exact on every prism.
- Landed PR 8864: the layer chain is gapless.
- Open PR 8871: one stiffness sets the flux cost and the correlations.
- New here: the vacuum amplitude as a Gaussian flux functional; the
  layer-unit law as local transfer times that functional, to 0.24% on the
  square; and the functional's 1/r tail within the layer.

## Theorem — The layer-unit law on the computed prisms

On 2 × 4, 2 × 6, 2 × 8 and 4 × 4, the exact layer-unit law, its vacuum
amplitude and the Gaussian functional stand in the stated relations with the
stated R², slopes and total-variation distances. The kernel's tail is
computed as stated. No limit is claimed for the Gaussian form beyond the
computed cross-sections.

## No-Go Discipline Gate

- **N1 alternative routes.** Larger squares are the direct extension and
  are beyond this machine.
- **N2 wall independence.** The predicted kernel uses only the flux cost;
  the vacuum comes from the zero-flux top vector.
- **N3 hidden walls.** Floating-point eigenvectors with stated tolerance;
  sampled layers with a fixed seed.
- **N4 residual matching.** Nothing is fitted in the formation-law test;
  the vacuum fits report their slopes against −1/4.
- **N5 rhetoric audit.** "Is a Gaussian flux functional" means the stated
  R² and total-variation bounds on the computed prisms.
- **N6 partial-closure paths.** Total variation grows with the number of
  degrees of freedom, as it does on the strips. A per-mode comparison on
  larger squares is the next measure.
- **N7 steelman.** Against: the strips' total variation rises from 0.7% to
  1.1% with length. For: the square, whose two directions are equivalent,
  is at 0.24%, and every fit improves with the cross-section. Both are
  recorded.
- **N8 cross-cycle echo.** Landed PRs 8740, 8746, 8859 and 8864 and open
  PR 8871 are cited.

## Falsifiers

- A sampled layer at which the Gaussian law departs from the exact law by
  more than the stated total variation.
- A computed shape on which ln ψ is not linear in G to the stated R².

## Boundaries and non-claims

- The computed cross-sections 2 × 4, 2 × 6, 2 × 8 and 4 × 4.
- No limit of large cross-sections is claimed for the Gaussian form.
- No reading, rule, alphabet, unit or order law is adopted.
- Nothing here grades, unlocks or audits any other claim.

## Imports

The minimal axioms, landed PRs 8740, 8746, 8859 and 8864, open PR 8871,
and the landed lattice-Green note are cited. No audit grade, no new axiom,
no new primitive, no new comparator and no new framing is imported.

## Review record

- **Seat:** one Opus 5.5 seat; no subagents; runner and note by the same
  seat.
- **Independence sources:** the exact layer-unit law; the predicted kernel
  from the flux cost alone; the kernel's transform on a large grid.
- **Mutation census** (caught means at least one FAIL line or a nonzero
  exit; the runner exits nonzero on any FAIL):

| Mutant | Change | Result |
|---|---|---|
| layer law without the vacuum ratio | law made local | caught (2 FAILs) |
| Gaussian weight with the wrong sign | functional reversed | caught (1 FAIL) |
| Gaussian weight of ψ² in place of ψ | exponent doubled | caught (1 FAIL) |
| continuum kernel 2K/\|q\| in place of the lattice kernel | kernel changed | caught (2 FAILs) |
| field without the staggered sign | occupation for field | caught (3 FAILs) |
| stiffness read as c in place of 2c | factor 2 dropped | caught (2 FAILs) |
| kernel tail without the square root | 1/q² kernel | caught (1 FAIL) |
| flux sector S = s in place of \|S\| = s | sector changed | caught (nonzero exit) |
| wrap links not identified | wrap dropped | caught (3 FAILs) |
| two occupied links per vertex | rule changed | caught (3 FAILs) |

  10 of 10 are caught.
- **Vacuity guard:** every slope, R², total-variation distance and tail
  ratio is printed.
- **Budget:** 5 checks, stdout 1213 characters (ceiling 6000), about 59 s
  (ceiling 900 s), peak about 745 MB.

## Verification

```bash
python3 scripts/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.py
```

Expected summary line: `TOTAL: PASS=5 FAIL=0`; the runner exits nonzero
if any check fails. Cached output:
`logs/runner-cache/uniform_ice_layer_vacuum_is_a_gaussian_flux_functional_and_the_layer_unit_law_carries_a_one_over_r_flux_interaction_2026_09_23.txt`.

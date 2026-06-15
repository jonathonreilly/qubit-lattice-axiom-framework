# Transfer Trace Correspondence Fixes Kernel Normalization on the Retained Surface

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome; later status is assigned only by the independent audit lane.
**Source-note proposal disclaimer:** this note is a source-note proposal; audit verdict and downstream status are not set here.
**Primary runner:** `scripts/frontier_transfer_trace_correspondence_fixes_kernel_normalization_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_transfer_trace_correspondence_fixes_kernel_normalization_2026_06_12.txt`

## Boundary

This note proves T1-T4 on the retained free staggered surface only: `1+1d`, `U = 1`, one Grassmann component per site, the 2-step blocked construction, and the retained canonical pair measure.

It does not select an occupancy cell and does not fix or select `r`; the occupancy binary stays open. It does not claim that the corner/generation transfer structure exists or is retained. It does not derive physical time, edit registries, introduce a new axiom, primitive, admission, or normalization rule, or add an empirical comparator. The canonical measure used below is the retained substep1 normalization, not a new choice. No route is terminated by this note.

## The Retained Surface Used

The transfer side is the retained free staggered 2-step surface. The source statement used here is the RP note's claim that the 2-step blocked transfer matrix satisfies `T_hat^2 = T_odd T_even = B^dag B`, with single-particle 2-step kernel `t1^(2)(p) = e^{-2 E(p)}` and `E(p) = arcsinh( sqrt(m^2 + sin^2 p) )`. The runner reuses the same staggered phases, the same `m = 0.5` anchor, and the same decaying-channel selection from `T_odd T_even`.

The Berezin side uses the retained substep1 canonical pair measure. The source statement used here is `Z_F[M] = int prod_x dchibar_x dchi_x exp(-sum_{x,y} chibar_x M_xy chi_y) = det(M)` for the single-pair Grassmann candidate. This note applies that normalization to the anti-periodic 2-step trace kernel; it does not add a second normalization convention.

## The Theorem

**Theorem (trace correspondence fixes the kernel normalization).** On the retained free staggered surface (`1+1d`, `U = 1`, the 2-step blocked construction):

**(T1) Canonical operator side.** The Fock-space trace `Z_op(N) = Tr (T_hat^2)^N` is determined by the retained construction with no free normalization. The modes satisfy canonical anticommutation relations and the second-quantized trace obeys `Tr Gamma(t) = det(1 + t)` for the single-particle 2-step kernel `t`. The runner builds `Gamma(t)` explicitly on the occupation basis and verifies `N = 1` and `N = 2` exactly at `L_s = 2`, with `L_s = 3` robustness. Runner tags: `A1-A4`, `A10-A10b`.

**(T2) Berezin side, canonical measure.** The Grassmann/Berezin representation of the same object with the canonical pair measure reproduces `Z_op(N)` exactly. At `L_s = 2`, `N = 1`, the runner constructs the anti-periodic two-slice quadratic kernel for the trace formula and evaluates it by genuine Grassmann expansion: truncated exponential, exterior multiplication, and top-monomial extraction. It separately checks that this Berezin-side computation is not a determinant substitute. Runner tags: `A5-A5c`, `A10c`.

**(T3) Lambda is forced.** Rescaling the Berezin quadratic kernel by `lambda != 1` multiplies the Berezin side by `lambda^k`, with `k` the rank of the anti-periodic trace kernel. Since the operator trace is already fixed by `Gamma(t)`, the equality with `Z_op(N)` over `lambda > 0` forces `lambda = 1` exactly. The runner extracts the exponent symbolically, solves the positive-real equation, and gives the `lambda = 2` breaking witness. Runner tags: `A6-A8`.

**(T4) Localization.** Wherever a 2-step transfer/trace correspondence is retained, the occupancy-class kernel freedom is fixed by the operator trace on that surface. For the corner/generation realization, the open object is the retained extension of this correspondence to that surface, not a new normalization principle. What that extension's mode pairing would select between the occupancy cells is not determined here. Runner tag: `A9`.

## Consequence For The Occupancy Kernel Route

The companion `KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md` records that the corner Berezin measure alone leaves a kernel rescaling `lambda` free. This note reproves the relevant scaling fact on the retained transfer surface: `det(lambda K) = lambda^k det(K)`, and the genuine Berezin expansion gives the same exponent for the anti-periodic trace kernel.

The consequence is narrow. On a surface where the transfer/trace correspondence is retained, `lambda` is no longer free because the canonical operator trace fixes it. For the corner/generation setting, the refined prerequisite is therefore the retained extension of this transfer/trace correspondence to that surface. The route remains live: the corner-extension object, its mode pairing, and its occupancy-cell implication are open.

## What This Note Does Not Claim

This note is not a statement about the generation/corner surface. The free staggered surface here is `1+1d` with one Grassmann component per site; the generation/corner surface is not this surface.

It does not select an occupancy cell. It does not fix `r`. It does not say what a future corner correspondence would select. It does not claim that such a corner correspondence exists. It does not import physical time or a measured-mass readout. It does not add a comparator or a new normalization rule. The occupancy binary stays open.

## Dependencies

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md) — the retained transfer structure: `T_hat^2 = B^dag B`, the reused `T_even/T_odd` construction, and T1's operator-side authority.
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md) — the canonical pair measure `Z_F[M] = det(M)`, used as T2's measure authority.

Context, not load-bearing links: `KOIDE_OCCUPANCY_KERNEL_COEFFICIENT_NOT_FIXED_BY_RETAINED_CORNER_MEASURE_BOUNDED_NOTE_2026-06-12.md` supplies the in-review lambda-freedom prompt, with the lambda-scaling fact reproven here; `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md` is an occupancy-independence scoping companion; `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md` is a static-readout scoping companion.

**No-promotion statement:** this note does not promote, demote, or set the audit/retention status of any existing note, companion route, open gate, or registry row. It records only the bounded theorem on the retained free staggered 2-step transfer surface, and leaves the corner/generation extension and the occupancy binary open.

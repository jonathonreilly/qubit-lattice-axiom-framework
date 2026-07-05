# Corner-Axis Free Transfer Extension: Per-Channel Construction, Trace Correspondence, and the Mode-Set Fork

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. Runner `PASS=18 FAIL=0`.
**Status authority:** independent audit lane only. This note does not edit any
registry, ledger, queue, publication-status surface, axiom, primitive,
admission, or comparator.
**Primary runner:** `scripts/frontier_corner_axis_free_transfer_extension_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_corner_axis_free_transfer_extension_2026_06_12.txt`
**Authority role:** free (`U = 1`) corner-axis transfer-structure extension on
the supplied positive-mass channel domain, reusing the cited per-channel
staggered two-step transfer construction and reproving the trace-normalization
facts inside the runner.

## Boundary

This note establishes the five items below on the free corner-axis surface over
the supplied positivity domain only. It does not select an occupancy cell, does
not fix `r`, and does not adopt or favor OO or R-D. The fork is exhibited, not
resolved; the occupancy binary stays open.

The result is free (`U = 1`) and per-channel. It does not claim a gauge
extension, a full-dynamics corner theorem, physical-time derivation, a
positive-mass derivation, a selector for the registered doublet mode set, or a
route resolution beyond the stated free construction. The positive-real mass
orientation is consumed as a supplied-domain condition and cross-referenced to
`STRONG_CP_THETA_ZERO_NOTE.md`; this note does not derive that condition. It
adds no axiom, primitive, admission, comparator, or registry edit.

## The supplied surface

Let `C` be the three-cycle matrix on the internal generation triplet. The
supplied circulant mass class is

```text
H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,
```

with `a, B` real. In the circulant eigenbasis its three real channel masses are

```text
lambda_k(delta) = a + 2 B cos(delta + 2 pi k / 3),     k = 0,1,2.
```

The domain is stipulated as the positive-real supplied-domain where all
`lambda_k(delta) > 0`; for example `a > 2B > 0` is a sufficient supplied
subdomain. The same positive-mass orientation is the one tracked on the
strong-CP side in `STRONG_CP_THETA_ZERO_NOTE.md`; this note uses the domain,
not a derivation of it.

The per-channel transfer engine is the cited free staggered `1+1d` two-step
construction: for a positive mass `m`, the two-step one-particle kernel is
`t(p) = exp(-2 E(m,p))`, with
`E(m,p) = arcsinh(sqrt(m^2 + sin^2 p))`, and the many-body two-step transfer is
`T_hat^2 = Gamma(t) = B^dag B`, positive Hermitian.

## The theorem

> **Theorem (corner-axis free transfer extension).** Take the free staggered
> `1+1d` action of the cited construction, with the internal generation
> triplet carried by the supplied circulant mass term `H(delta)` above, on the
> supplied positivity domain where all three channel masses are positive. Then:

**Channel decomposition.** The circulant eigenbasis
diagonalizes the internal triplet, so the action splits into three decoupled
staggered channels with masses `lambda_k(delta)`. Each channel inherits the
cited two-step construction verbatim:

```text
T_k^2 = Gamma(t_k) = B_k^dag B_k,
t_k(p) = exp(-2 E(lambda_k,p)).
```

**Corner transfer structure.** The corner transfer is the
tensor product

```text
T_corner^2 := tensor_k T_k^2.
```

It is positive Hermitian on the tensor Fock space. This exhibits the named
free per-channel prerequisite: a time-slicing / transfer structure for the
corner realization on the supplied positivity domain.

**Trace correspondence.** For
`t = direct_sum_k t_k`,

```text
Tr Gamma(t) = det(1 + t) = product_k det(1 + t_k).
```

The canonical-pair Berezin representation gives the same value by finite
Grassmann expansion. If a positive scalar kernel normalization is inserted on a
chosen mode set, the Berezin side is multiplied by that scalar to the number of
canonical pairs in the set while the operator trace is unchanged; equality
therefore forces normalization `1` on this surface, per mode set and within
each branch of the mode-set fork.

**K-covariance.** K/CPT conjugation sends
`delta -> -delta` and swaps the doublet channels:

```text
lambda_2(delta) = lambda_1(-delta).
```

The unordered channel spectrum is K-invariant, the singlet channel is fixed,
and `t_1(delta)` is relabeled to `t_2(delta)` under K. Therefore
`T_corner^2` is K-covariant and the two doublet channels form one K-orbit.

**Mode-set fork -- exhibited, not resolved.** The
canonical construction counts channel modes, so the doublet contributes two
Fock factors. The registrable readout class is additive over disjoint records
and constant on K/CPT orbits, so its registered content is a function of the
unordered K-orbit content. Whether the registered Fock occupancy of the
doublet is per-channel or per-K-orbit is exactly the orbit-occupancy premise,
localized here as one explicit fork in the corner transfer structure's mode
bookkeeping.

Both branches map through the runner-rechecked bookkeeping
`rho = (pi/g)/Z_d`, `r = 1/(2 rho)`: per-channel counting gives the two-slot
cell `r = 1`, while per-K-orbit counting gives the one-slot cell `r = 1/2`.
The admissible fork set is the full binary `{1, 1/2}`. The trace
correspondence fixes the kernel normalization inside each branch; it does not
select between branches.

## Consequence

At the free per-channel level, the runner exhibits a transfer structure for the
corner-axis realization on the supplied domain, checks the trace correspondence
and kernel-normalization constraint on it, and localizes the remaining
occupancy binary to the mode-set fork. The follow-on directions are the
gauge/full-dynamics extension of this transfer structure and an independent
resolution of the registered mode-set rule.

## What this note does NOT claim

- It does not select an occupancy cell, fix `r`, adopt OO, adopt R-D, or favor
  either horn of the fork.
- It does not treat the fork as evidence for either branch. The fork is
  exhibited as the localization of the OO premise, not as a derivation of it.
- It does not claim the per-channel free construction is the full corner
  dynamics.
- It does not claim a gauge or `U`-integrated extension, a Wilson-sector
  transfer theorem, or a determinant-weight theorem.
- It does not derive the positive-real mass orientation; that condition is
  consumed as supplied-domain input.
- It does not derive physical time, add a new axiom or primitive, introduce a
  new admission or comparator, edit any registry, or set audit status.

## Dependencies

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  -- the per-channel engine for the channel decomposition and corner transfer;
  the construction is reused.
- [`STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`](STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md)
  -- the canonical pair measure used on the Berezin side of the trace
  correspondence.
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)
  -- the registrable-readout class used in the mode-set fork: additive over
  disjoint records and constant on K/CPT orbits.

Context, not dependency links:

- `TRANSFER_TRACE_CORRESPONDENCE_FIXES_KERNEL_NORMALIZATION_ON_RETAINED_SURFACE_BOUNDED_NOTE_2026-06-12.md`
  -- trace-normalization context; the small trace facts are reproven by this
  runner.
- `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`
  -- OO premise statement and prior rho-map bookkeeping; the rho-map facts are
  reproven here.
- `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md`
  -- static-readout scoping companion for the unresolved occupancy selector.
- `I1_NATIVE_QUADRATIC_STATIC_SOURCE_NORMALIZATION_BRIDGE_2026-06-08.md`
  -- kernel-scoping companion; not used as a transfer proof.
- `STRONG_CP_THETA_ZERO_NOTE.md` -- positive-mass orientation tracking context;
  the condition is consumed, not derived here.

## No-promotion statement

This note does not promote, demote, or set the audit status of any dependency
or consumer. The independent audit lane remains the only status authority.

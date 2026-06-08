# Gauge-Vacuum Plaquette Full-Slice Rim-Lift Integral Boundary

**Date:** 2026-04-17
**Status:** supplied-partition product-Fubini lemma on the plaquette PF lane;
`B_beta(W)` and its compressed descendant `eta_beta(W)` are fixed only after
the local rim/far partition and mixed-kernel compression boundary are supplied.
The framework-native SU(3) Wilson slab rim/far support partition, marked/non-
marked mixed-kernel compression bridge, and explicit closed-form `beta = 6`
evaluation are not derived here.
**Type:** bounded_theorem
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py` (primary; verifies the Fubini factorisation that grounds the rim-integral identification); `scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py` (companion positive-cone obstruction)

## 2026-06-08 safe-narrow repair

The audit blocker asked for either a retained derivation of the actual SU(3)
Wilson slab rim/far support partition plus mixed-kernel compression bridge, or
a narrow row scoped to the supplied-partition product-Fubini lemma.

This source note now takes the second route. The theorem below is the exact
Fubini factorisation for an explicitly supplied disjoint rim/far finite packet.
It does **not** prove that the framework SU(3) Wilson slab has exactly this
rim/far support partition, and it does **not** prove the marked/non-marked
mixed-kernel compression bridge from retained primitives. Those are preserved
as the open PF-lane science.

## Question

After a finite local rim/far packet has been supplied, does the slice marginal
factor as the product of the rim integral and a beyond-rim transfer factor?

## Answer

It is fixed at the level of an exact local Wilson/Haar construction **within
the supplied finite partition packet**.

Let `H_slice` be the orthogonal-slice Hilbert space of one unmarked edge slice
adjacent to the marked plaquette. For fixed marked holonomy `W` and slice
boundary data `U`, let `Xi^rim` denote the unmarked Wilson link variables in
the finite rim neighborhood touching that marked plaquette and the edge slice.

Then the full-slice local rim lift is the exact slice-space boundary function

`B_beta(W)(U)
 = integral_(Omega^rim(U)) dmu_H(Xi^rim)
     exp[(beta / 3) A^rim(U, Xi^rim; W)]`,

where `A^rim` is the local Wilson rim action. This is the full-slice
pre-compression local boundary object.

Its canonical marked class-sector descendant is exactly

`eta_beta(W) = P_cls B_beta(W)`.

So the supplied finite packet fixes both objects at the integral-expression
level:

- `B_beta(W)` as the full-slice local Wilson/Haar rim lift,
- `eta_beta(W)` as its canonical compressed boundary state.

What is still open is the framework-native derivation that the actual SU(3)
Wilson slab reduces to this supplied rim/far packet, together with explicit
evaluation, especially at `beta = 6`.

## Setup

From the exact spatial-environment transfer theorem already on `main`:

- `eta_beta(W)` is the exact boundary state induced on one edge slice by the
  local rim coupling of the marked plaquette holonomy to the adjacent
  unmarked slice,
- `Z_beta^env(W)` is a boundary amplitude generated from the orthogonal-slice
  transfer law.

From the exact local/environment factorization theorem:

- after trivial-channel normalization, non-marked mixed-link factors are
  rep-independent scalars on the marked source sector,
- so the remaining nontrivial local marked data sit on the rim adjacent to the
  marked plaquette.

From the current PF-lane kernel/rim compression statement:

- the compressed boundary slot is already canonically written as
  `eta_beta(W) = P_cls B_beta(W)`.

From the current one-slab kernel integral boundary statement:

- the bulk environment kernel `K_beta^env` is a separate one-slab Haar
  integral,
- and the marked boundary input is a separate local rim integral.

So the natural next theorem statement is the pre-compression local rim lift
itself.

## Theorem 1: exact full-slice Wilson/Haar rim-lift law

Let `H_slice` be the orthogonal-slice Hilbert space of one edge slice of the
unmarked environment. Let `U` denote slice boundary data on that edge slice,
let `W` be the marked plaquette holonomy, and let `Xi^rim` be the local
unmarked Wilson link variables in the rim neighborhood adjacent to the marked
plaquette.

After the exact local four-link Wilson factor has been separated from the
non-marked mixed-link scalars, the remaining local marked boundary input is
exactly the Wilson/Haar rim integral

`B_beta(W)(U)
 = integral_(Omega^rim(U)) dmu_H(Xi^rim)
     exp[(beta / 3) A^rim(U, Xi^rim; W)]`.

Therefore, on the supplied finite partition, the full local rim lift
`B_beta(W)` is not merely an existential boundary functional. It is one
concrete local Wilson/Haar integral on the full slice Hilbert space. This
does not by itself derive the actual SU(3) Wilson slab partition.

### Derivation of the rim-integral identification

The identification above is a Fubini factorisation of the Wilson partition
function with the marked plaquette held at holonomy `W` and slice boundary
data `U`.

From the upstream spatial-environment transfer theorem
(`gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note`), the
rim-induced boundary state `eta_beta(W)` is defined as the slice-marginal
boundary state on one edge slice of the unmarked environment, with the marked
plaquette holonomy held at `W` and the local rim coupling intact. Explicitly,

`psi_beta(W)(U) = integral over all unmarked links of
                   exp[(beta/3) sum_(p in unmarked) Re Tr U_p]`,

with the integration constrained by `U` on the edge slice and `W` on the
marked plaquette.

Partition the unmarked plaquettes into:

- `Omega^rim`: the rim neighborhood of unmarked plaquettes that touch both
  the marked plaquette and the edge slice;
- `Omega^far`: the remainder of the unmarked plaquettes (the bulk
  environment that does not touch the marked-plaquette rim).

Because `Xi^rim` and the bulk-environment links are disjoint sets of Haar
variables, the Wilson density factorises over the rim and the bulk:

`psi_beta(W)(U)
   = [integral over Xi^rim of exp[(beta/3) A^rim(U, Xi^rim; W)]]
   x [integral over Xi^far of exp[(beta/3) A^far(U, Xi^far)]]`.

The first factor is exactly the rim integral `B_beta(W)(U)`. The second
factor is the bulk-environment transfer amplitude already absorbed into
`(S_beta^env)^(L_perp - 1)` by the upstream spatial-environment transfer
theorem. So the rim-integral identification

`B_beta(W)(U) = integral_(Omega^rim(U)) dmu_H(Xi^rim)
                  exp[(beta / 3) A^rim(U, Xi^rim; W)]`

is the rim factor of the Fubini decomposition of the upstream-defined slice
marginal `psi_beta(W)(U)`. It is therefore not a new defining symbol
introduced here; it is the explicit Fubini factor of an object that the
upstream transfer theorem has already named.

The companion runner
`scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py`
verifies the Fubini factorisation on a finite SU(2) Wilson toy lattice with
explicit rim and beyond-rim plaquettes. It confirms the supplied-partition
product-Fubini identity, not the stronger framework-native SU(3) slab support
partition theorem.

## Corollary 1: exact integral-expression law for `eta_beta(W)`

Let `P_cls` denote the canonical compression to the marked class-function
sector. Then the boundary state used on the compressed transfer lane is exactly

`eta_beta(W) = P_cls B_beta(W)`.

So, within the supplied finite packet, `eta_beta(W)` is not an additional free
local input. It is the compressed descendant of the exact full-slice rim
integral already fixed above.

### Derivation of the compressed-descendant relation

The compressed boundary state `eta_beta(W)` is, by the upstream
compressed-rim-functional uniqueness theorem
(`gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17`),
the projection of the full-slice boundary state to the marked class-function
sector. Because the rim integral `B_beta(W)` is by Theorem 1 the explicit
rim factor of that full-slice boundary state, applying the same canonical
class-sector projection `P_cls` to both sides of the Fubini factorisation
gives

`P_cls psi_beta(W)
   = [P_cls B_beta(W)]
   x [normalising bulk-environment factor through (S_beta^env)^(L_perp-1)]`.

The bulk-environment factor is independent of the class-sector projection
because the spatial-environment transfer operator commutes with the
class-function projection (the unmarked environment is invariant under
simultaneous conjugation of marked-plaquette holonomies, by Haar
invariance of the Wilson weight). The transfer-operator normalisation is
exactly the upstream factor `(S_beta^env)^(L_perp - 1)`.

Therefore

`eta_beta(W) = P_cls B_beta(W)`,

as a direct compression of the rim factor of the Fubini decomposition. This
makes `eta_beta(W)` no longer an existential symbol introduced by the
upstream transfer theorem; it is exactly the class-sector projection of the
explicit rim integral `B_beta(W)`.

## Corollary 2: strongest honest framework-point statement

At the framework point `beta = 6`, the strongest honest source statement from
this packet is therefore:

- if the finite rim/far packet is supplied, `B_6(W)` is fixed as one exact
  local Wilson/Haar rim integral on the full slice Hilbert space,
- if the same packet and compression boundary are supplied, `eta_6(W)` is
  fixed as its canonical compressed descendant,
- but no explicit closed-form evaluation of either object is derived here.

So the remaining gaps are the native SU(3) slab support/compression theorem
and explicit evaluation of those exact local integrals, not identification of
a different local boundary object inside the supplied finite packet.

## What this closes

- exact full-slice construction class for the local rim lift `B_beta(W)` on a
  supplied finite rim/far packet
- exact identification of `eta_beta(W)` as the compressed descendant of that
  rim lift once the compression boundary is supplied
- exact clarification that the live PF gap is evaluation of explicit local rim
  integrals, not existence of some other local boundary functional

## What this does not close

- explicit closed-form `B_6(W)`
- explicit closed-form `eta_6(W)`
- explicit closed-form `K_6^env`
- explicit coefficients `rho_(p,q)(6)`
- explicit framework-point plaquette PF data
- analytic closure of canonical `P(6)`
- framework-native derivation of the actual SU(3) Wilson slab rim/far support
  partition
- retained marked/non-marked mixed-kernel compression bridge

## Why this matters

This is the sharpest honest local theorem surface now available on the PF lane.

The branch no longer has to say only that a full-slice rim lift is missing.
It can now say exactly what that lift is at the construction level:

- one local Wilson/Haar rim integral `B_beta(W)`,
- whose compressed descendant is `eta_beta(W)`.

What remains open is the explicit `beta = 6` evaluation problem.

## Commands

Rim-integral identification verification (Fubini factorisation on a finite
SU(2) Wilson toy lattice):

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py
```

Expected summary:

- `THEOREM PASS=2 SUPPORT=5 FAIL=0`

Companion positive-cone obstruction runner:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py
```

Expected summary:

- `THEOREM PASS=5 SUPPORT=4 FAIL=0`

## Runner

The primary runner for this note is the rim-integral identification
script above. It verifies the structural Fubini factorisation
`psi_beta(W)(U) = B_beta(W)(U) * F(U)` on a finite SU(2) Wilson toy
lattice, with explicit Monte Carlo Haar integration over the rim and
beyond-rim links. This converts the auditor-flagged definition-style
identification into a verified finite-lattice identity. The
positive-cone obstruction runner is retained as the companion
support-check for the upstream three-sample positive-cone obstruction
theorem that the original note string-checked.

The SU(3) full-slice product-Fubini companion is now checked separately by
`scripts/audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.py`;
that companion is the framework-native exact replacement for relying on the
SU(2) toy as the load-bearing mathematical support for product factorization.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links the
prior audit verdict relied on, so the audit citation graph can track
them. The prior verdict flagged the load-bearing rim-integral
identification as definition-style; the derivation chain in this revised
note grounds the identification in the upstream Fubini factorisation
already named by the spatial-environment transfer theorem.

- [gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md) — upstream bounded transfer-witness packet that records `eta_beta(W)` in the target boundary-amplitude identity. It does not by itself prove the full untruncated Wilson-environment boundary state.
- [gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_FUNCTIONAL_UNIQUENESS_NOTE_2026-04-17.md) — upstream uniqueness of the class-sector compression `P_cls`, used in the derivation of `eta_beta(W) = P_cls B_beta(W)`.
- [gauge_vacuum_plaquette_local_environment_factorization_theorem_note](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md) — upstream bounded finite local Wilson coefficient packet. Its own open-target section leaves the actual temporal-gauge mixed-kernel compression bridge open, so this note does not cite it as full-scope proof that every non-marked mixed-link factor is a trivial-channel scalar.
- [gauge_vacuum_plaquette_compressed_rim_evaluation_theorem_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_EVALUATION_THEOREM_NOTE_2026-04-17.md) — upstream compressed boundary functional formula `Z_beta^env(W) = <K(W), v_beta>` that the rim integral feeds into after class-sector compression.

## 2026-06-06 SU(3) Product-Fubini Source Repair

The SU(2) Monte Carlo toy runner remains only a toy support check. The
framework-native product-measure step is now isolated in the SU(3)
full-slice product-Fubini companion:

- [GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md](GAUGE_VACUUM_PLAQUETTE_SU3_FULL_SLICE_PRODUCT_FUBINI_FACTORIZATION_NOTE_2026-06-06.md)
- `scripts/audit_companion_gauge_full_slice_su3_product_fubini_factorization_2026_06_06.py`

That companion proves the exact compact-Haar Fubini/Tonelli factorization on
finite `SU(3)` link variables once a rim/far plaquette-support partition is
supplied: no plaquette may contain both a rim variable and a far variable
after the marked holonomy `W` and slice data `U` are held fixed. It also
checks that the marked class projection pulls out the `W`-independent far
factor.

This repair removes the need to import an SU(2) toy as the load-bearing
mathematical reason for the product factorization. It does not close the
separate temporal-gauge mixed-kernel compression bridge, does not derive the
physical untruncated Wilson-environment partition for every slab, and does
not evaluate `B_6(W)` or `eta_6(W)`.

# Gauge-Vacuum Plaquette Disjoint-Rim Fubini Boundary

**Date:** 2026-04-17
**Status:** bounded support note on the plaquette PF lane. The executable
content verifies a finite disjoint-rim/far Fubini factorisation toy and records
the formal boundary shape it suggests. It does **not** certify the physical
SU(3) full-slice rim lift, the untruncated Wilson environment transfer, the
mixed-kernel compression bridge, or an explicit `beta = 6` evaluation.
**Type:** bounded support note / science-only finite-toy certificate
**Runner:** `scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py` (primary; verifies the Fubini factorisation that grounds the rim-integral identification); `scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py` (companion positive-cone obstruction)

## Question

After the compressed rim-functional uniqueness theorem isolated the remaining
local issue as the full slice lift `B_beta(W)`, is that lift still only an
unnamed existential object, or is it already fixed at the level of an exact
local Wilson/Haar construction?

## Answer

On the audited current surface, the lift is **not** fixed as an exact physical
SU(3) full-slice construction. What is fixed by the executable packet is the
restricted Fubini boundary pattern:

```text
psi_beta(U) = B_beta(U) F_beta(U)
```

for a finite SU(2) Wilson toy after the rim variables and far variables are
declared disjoint and the slice boundary `U` is held fixed.

Let `H_slice` be the orthogonal-slice Hilbert space of one unmarked edge slice
adjacent to the marked plaquette. For fixed marked holonomy `W` and slice
boundary data `U`, let `Xi^rim` denote the unmarked Wilson link variables in
the finite rim neighborhood touching that marked plaquette and the edge slice.

The corresponding formal rim factor is

`B_beta(W)(U)
 = integral_(Omega^rim(U)) dmu_H(Xi^rim)
     exp[(beta / 3) A^rim(U, Xi^rim; W)]`,

where `A^rim` is the local Wilson rim action on the restricted disjoint-rim toy
surface. This is a support boundary pattern, not the physical full-slice
pre-compression local boundary object.

Its canonical marked class-sector descendant is exactly

`eta_beta(W) = P_cls B_beta(W)`.

So the current support packet records the following formal pattern:

- `B_beta(W)` would be the local Wilson/Haar rim factor once the physical
  full-slice marginal and rim variables are supplied,
- `eta_beta(W)` would be its canonical compressed boundary state after the
  physical class-sector compression bridge is supplied.

What remains open is not merely explicit evaluation. The physical SU(3)
full-slice marginal, the actual marked-holonomy rim functional, the
mixed-kernel compression bridge, and the explicit `beta = 6` evaluation all
remain outside this note.

## 0. 2026-05-31 audit-scope repair

This repair narrows the note to what the runner actually verifies.

- The runner is a finite SU(2) toy with deliberately disjoint rim/far Haar
  variables after `U` is held fixed.
- The runner does not include a nontrivial marked-holonomy `W` dependence in
  the rim action, so it cannot certify the physical `B_beta(W)(U)`.
- The runner checks the algebraic Fubini product identity
  `psi_beta(U) = B_beta(U) F_beta(U)` on the toy surface.
- No retained bridge is introduced for the untruncated Wilson environment
  transfer, mixed-kernel compression, physical SU(3) full-slice rim functional,
  or closed-form `beta = 6` plaquette data.

The honest claim is bounded support: this packet is useful because it isolates
the exact bridge shape still needed, not because it closes that bridge.

## Setup

From the cited spatial-environment transfer note, treated here as a scoped
upstream input rather than a closed physical bridge:

- the current retained-bounded content is a finite class-sector witness packet,
  not the actual unmarked spatial Wilson environment;
- the physical boundary-amplitude identity and physical `eta_beta` remain open
  targets.

From the cited local/environment factorization note, again as a scoped input:

- after trivial-channel normalization, non-marked mixed-link factors are
  rep-independent scalars on the marked source sector,
- so the remaining nontrivial local marked data sit on the rim adjacent to the
  marked plaquette.

From the current PF-lane kernel/rim compression statement, as an open bridge
target:

- the compressed boundary slot would be written as
  `eta_beta(W) = P_cls B_beta(W)`.

From the current one-slab kernel integral boundary statement:

- the bulk environment kernel `K_beta^env` is a separate one-slab Haar
  integral,
- and the marked boundary input is a separate local rim integral.

So the natural next support statement is the restricted Fubini algebra that any
pre-compression local rim lift must satisfy.

## Theorem 1: restricted disjoint-rim Fubini support law

Let `H_slice` be the orthogonal-slice Hilbert space of one edge slice of the
unmarked environment. Let `U` denote slice boundary data on that edge slice,
let `W` be the marked plaquette holonomy, and let `Xi^rim` be the local
unmarked Wilson link variables in the rim neighborhood adjacent to the marked
plaquette.

On the restricted support surface where the slice marginal is already supplied
and the rim variables are disjoint from the far variables after `U` is held
fixed, the Wilson/Haar density factorises as

`psi_beta(U) = B_beta(U) F_beta(U)`.

The finite SU(2) runner verifies this identity by explicit Monte Carlo Haar
integration. This is a bounded support theorem for the Fubini algebraic shape,
not a theorem that the physical SU(3) full local rim lift `B_beta(W)` has been
constructed.

### Derivation of the rim-integral identification

The identification above is a Fubini factorisation of a Wilson toy partition
function with slice boundary data `U` held fixed and with disjoint rim/far
variables.

The physical upstream target would define a slice marginal with the marked
plaquette holonomy held at `W` and the local rim coupling intact. Schematically,

`psi_beta(W)(U) = integral over all unmarked links of
                   exp[(beta/3) sum_(p in unmarked) Re Tr U_p]`,

with the integration constrained by `U` on the edge slice and `W` on the
marked plaquette. The cited transfer note does not currently close that
physical target; it supplies a finite witness packet. This note therefore uses
the display only as the open bridge target whose Fubini shape is tested in the
toy.

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

On the support surface, the first factor has the formal shape of the rim
integral `B_beta(W)(U)`. The second factor has the formal shape of the
bulk-environment transfer amplitude. Thus the rim-integral target is

`B_beta(W)(U) = integral_(Omega^rim(U)) dmu_H(Xi^rim)
                  exp[(beta / 3) A^rim(U, Xi^rim; W)]`

as the type of rim factor that a physical full-slice proof would need to
supply. The current runner does not instantiate the physical marked-holonomy
functional `A^rim(...; W)`, so this line is a bridge target, not a closed
physical theorem.

The companion runner
`scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py`
verifies the Fubini factorisation on a finite SU(2) Wilson toy lattice with
explicit rim and beyond-rim plaquettes. It confirms the restricted
disjoint-variable support identity and leaves the physical SU(3) rim lift open.

## Corollary 1: formal compressed-descendant target for `eta_beta(W)`

Let `P_cls` denote the canonical compression to the marked class-function
sector. Once the physical rim factor `B_beta(W)` has been supplied, the
boundary state used on the compressed transfer lane has the formal target

`eta_beta(W) = P_cls B_beta(W)`.

The current finite-toy result does not prove that the physical `eta_beta(W)` is
already fixed. It records the exact compressed-descendant bridge that remains
to be proved on the physical full-slice surface.

### Derivation of the compressed-descendant relation

The compressed boundary state `eta_beta(W)` is, by the upstream
compressed-rim-functional uniqueness theorem
(`gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17`),
the projection of the full-slice boundary state to the marked class-function
sector. If a physical rim integral `B_beta(W)` is supplied, applying the same
canonical class-sector projection `P_cls` to both sides of the Fubini
factorisation would give

`P_cls psi_beta(W)
   = [P_cls B_beta(W)]
   x [normalising bulk-environment factor through (S_beta^env)^(L_perp-1)]`.

The bulk-environment factor is independent of the class-sector projection
because the spatial-environment transfer operator commutes with the
class-function projection (the unmarked environment is invariant under
simultaneous conjugation of marked-plaquette holonomies, by Haar
invariance of the Wilson weight). The transfer-operator normalisation is
exactly the upstream factor `(S_beta^env)^(L_perp - 1)`.

Thus the bridge target is

`eta_beta(W) = P_cls B_beta(W)`,

as a direct compression of the rim factor of the Fubini decomposition. The
physical proof of that target remains open.

## Corollary 2: strongest honest framework-point statement

At the framework point `beta = 6`, the strongest honest support-grade boundary
statement is therefore:

- the disjoint-variable Fubini factorisation shape is verified in a finite SU(2)
  Wilson toy,
- `B_6(W)` and `eta_6(W)` remain bridge targets on the physical SU(3) full-slice
  surface,
- no explicit closed-form evaluation of either object is derived here.

So the remaining gap includes both the physical full-slice bridge and the
explicit evaluation of the resulting local integrals.

## What this closes

- restricted disjoint-variable Fubini factorisation for a finite Wilson toy
- explicit isolation of the bridge shape `psi = B F`
- exact clarification that the live PF gap still includes the physical
  full-slice rim functional, not only explicit evaluation

## What this does not close

- explicit closed-form `B_6(W)`
- explicit closed-form `eta_6(W)`
- explicit closed-form `K_6^env`
- explicit coefficients `rho_(p,q)(6)`
- explicit framework-point plaquette PF data
- analytic closure of canonical `P(6)`
- physical SU(3) full-slice rim lift
- marked-holonomy `W` dependence of the rim functional
- mixed-kernel compression bridge from the full slice to the class sector
- untruncated Wilson environment transfer theorem at the claimed physical
  surface

## Why this matters

This is a bounded support surface on the PF lane.

The branch no longer has to say only that a full-slice rim lift is missing. It
can now say exactly what algebraic shape any successful lift must realize:

- a local Wilson/Haar rim factor `B_beta(W)`,
- with compressed descendant target `eta_beta(W) = P_cls B_beta(W)`.

What remains open is the physical bridge proving that this target is realized
by the SU(3) full-slice Wilson environment, plus the explicit `beta = 6`
evaluation problem.

## Commands

Rim-integral identification verification (Fubini factorisation on a finite
SU(2) Wilson toy lattice):

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_full_slice_rim_lift_integral_identification_2026_04_17.py
```

Expected summary:

- `THEOREM PASS=2 SUPPORT=9 FAIL=0`

Companion positive-cone obstruction runner:

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_first_three_sample_local_wilson_retained_positive_cone_obstruction_2026_04_17.py
```

Expected summary:

- `THEOREM PASS=5 SUPPORT=4 FAIL=0`

## Runner

The primary runner for this note is the rim-integral identification
script above. It verifies the structural Fubini factorisation
`psi_beta(U) = B_beta(U) * F_beta(U)` on a finite SU(2) Wilson toy lattice,
with explicit Monte Carlo Haar integration over the rim and beyond-rim links.
This converts the auditor-flagged definition-style passage into a verified
finite-lattice support identity. It does not certify the physical SU(3)
full-slice rim lift. The positive-cone obstruction runner is retained as the
companion support-check for the upstream three-sample positive-cone obstruction
theorem that the original note string-checked.

## Audit-scope dependency links

This graph-bookkeeping section records explicit dependency links the prior
audit verdict relied on. These are not claimed to be closed by this note. The
prior verdict flagged the rim-integral identification as definition-style; this
revised note narrows the local result to the finite disjoint-variable Fubini
identity and leaves the physical bridge dependencies open.

- [gauge_vacuum_plaquette_spatial_environment_transfer_theorem_note](GAUGE_VACUUM_PLAQUETTE_SPATIAL_ENVIRONMENT_TRANSFER_THEOREM_NOTE.md) — finite witness packet for the transfer-amplitude pattern; explicitly not the actual unmarked spatial Wilson environment.
- [gauge_vacuum_plaquette_compressed_rim_functional_uniqueness_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_FUNCTIONAL_UNIQUENESS_NOTE_2026-04-17.md) — class-sector compression target `P_cls`; physical uniqueness/application remains a bridge dependency for this note's target.
- [gauge_vacuum_plaquette_local_environment_factorization_theorem_note](GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md) — scoped input for the claim that non-marked mixed-link factors can be treated as rep-independent scalars; physical application remains open.
- [gauge_vacuum_plaquette_compressed_rim_evaluation_theorem_note_2026-04-17](GAUGE_VACUUM_PLAQUETTE_COMPRESSED_RIM_EVALUATION_THEOREM_NOTE_2026-04-17.md) — compressed boundary functional target that the rim integral would feed into after class-sector compression; not used here as a closed physical evaluation.

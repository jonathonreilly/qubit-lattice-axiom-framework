# Charged-Lepton Phase/Modulus Separation Boundary and Narrow No-Go

**Date:** 2026-06-06
**Type:** no_go
**Claim type:** no_go
**Claim scope:** the standalone structural fact that, for the Brannen/circulant
charged-lepton sqrt-mass spectrum `sqrt(m_k) = a(1 + 2 sqrt(r) cos(delta + 2 pi
k/3))`, the Koide modulus `r = |b|^2/a^2` and the Brannen phase `delta = arg(b)`
live on separate spectral invariants. The `e2`/Koide-modulus content is
delta-blind, while the spectral determinant carries `delta` only through
`cos 3delta`. The old universal claim that every real `C3`-invariant scalar action
cannot stationarize `delta=2/9` is withdrawn: a general real `C3` scalar may also
depend on `Im z^3`, and even the conjugation-even/spectral subclass has a
degenerate `W_X=0` target-encoding branch. The surviving source claim is therefore
only the narrow branch no-go: a **nondegenerate** conjugation-even/spectral scalar
with `W_X != 0` cannot stationarize `delta=2/9`, because it forces
`delta in {0, pi/3, 2pi/3, ...}`. The `C3`-covariant `eta`/holonomy = chirality
route remains untouched and open.
**Status authority:** independent audit lane only. Source note; later status is
set by the audit pipeline.
**Runner:** [`scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py`](../scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py)
(`TOTAL: PASS=20 FAIL=0`, exact `sympy`).

```yaml
actual_current_surface_status: demotion
target_claim_type: no_go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "exact no-go only for the nondegenerate conjugation-even/spectral scalar branch W_X != 0"
proposal_allowed: false
proposal_allowed_reason: "Demotes the old universal scalar-action no-go; preserves only the narrow active spectral-scalar branch obstruction and leaves delta=2/9 open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Provenance

From the `delta = 2/9` fresh-angle hunt (workflow `wa0o7fje5`, Lens 1), run with an
explicit AVOID-list of the worked routes (the six `(N-1)/N^2` mechanisms, APS-`eta`,
Fisher-Rao, `L(N;1)` holonomy, the two logged `koide_delta_*` no-gos). The hunt
found **no fresh derivation** of `delta=2/9`; its durable off-AVOID-list content is
the phase/modulus separation and the nondegenerate spectral-scalar boundary
recorded here. The stronger universal scalar-action no-go did not survive audit
review and is explicitly demoted.

## Statement

For the circulant generation mass operator `Y = a I + b C + conj(b) C^2` with
`z := b/a = sqrt(r) e^{i delta}` (so `|z|^2 = r`,
`Re z^3 = r^{3/2} cos 3delta`, and
`Im z^3 = r^{3/2} sin 3delta`):

**(N1) The elementary symmetric functions of the sqrt-mass spectrum separate
`r` from `delta`** (exact, runner Section S):
```text
e1 = 3 a                                         (scale)
e2 = 3 a^2 (1 - r)            -- delta-BLIND; e2 = (3/2) a^2 <=> r=1/2 <=> Q=2/3 (the entire Koide content)
e3 = a^3 (1 - 3r + 2 r^{3/2} cos 3delta)         -- the ONLY carrier of delta, solely via cos 3delta
```

**(N2) Narrow nondegenerate spectral-scalar obstruction** (exact, runner Section
W). In the restricted conjugation-even/spectral subclass
`W(|z|^2, Re z^3) = W(r, r^{3/2} cos 3delta)`, stationarity factorizes as
`dW/ddelta = W_X * (-3 r^{3/2} sin 3delta)`. On the nondegenerate active branch
`W_X != 0`, one must have `sin 3delta = 0`, i.e.
`delta in {0, pi/3, 2pi/3, ...}`. `delta = 2/9` is not among them
(`2/9 = n pi/3` needs `n = 2/(3 pi)`, non-integer). Thus this branch can support
a modulus extremum but cannot by itself be a nondegenerate derivation of the
phase `delta=2/9`.

**(N2b) Why the old universal scalar no-go is false** (exact, runner Section F).
`C3` invariance alone permits both `Re z^3` and `Im z^3`. A real scalar
`W(r, Re z^3, Im z^3)` can be built with a supplied minimum at
`delta=2/9`, for example by squaring the distance from
`(r^{3/2} cos(2/3), r^{3/2} sin(2/3))` in the `(Re z^3, Im z^3)` plane. The
runner verifies that this scalar is `C3`-invariant and stationary at the supplied
phase. This is a target-encoded selector, not a derivation, but it disproves the
previous "any real `C3` scalar" wording.

**(N2c) Why even/spectral scalars still have a degenerate target branch.** Even
inside `W(r, Re z^3)`, the branch `W_X=0` can stationarize a supplied phase:
`W=(Re z^3 - r^{3/2} cos(2/3))^2` has a local stationary point at `delta=2/9`.
Therefore the exact no-go is not "no spectral scalar can stationarize the phase";
it is only "no nondegenerate active spectral-scalar branch with `W_X != 0` forces
that phase."

**(N3) Convergence with the register-not-read partition map.** The genuine
register-not-read license (the central-sector partition map `D = sum_k P_k M P_k`)
delivers the **weight ratio `r`** (the `e2`-content), never the **within-block
phase `delta`** (the `e3`/`z^3` content). The partition route therefore lands on
the modulus object. A phase value still needs a genuine phase selector, a
covariant holonomy, or an explicitly supplied target; the partition map does not
provide it.

**Consequence.** This note does not prove that `delta = 2/9` is impossible or that
it must be the same gate as chirality. It proves a cleaner boundary: the Koide
modulus and the phase live on different spectral data, the register-not-read
partition map supplies the modulus side, and a scalar phase target requires either
a target-encoded extremum or an additional phase/covariant selector.

## Tested fresh candidates and branch outcomes

| candidate (fresh-hunt) | exactly 2/9? | native? | verdict |
|---|---|---|---|
| nondegenerate conjugation-even/spectral scalar with `W_X != 0` | no (forced to `C3`-rational) | yes | **(N2) forbids** |
| general real `C3` scalar using `Im z^3` | yes if target encoded | yes as an invariant, no as a derivation | **allowed; exposes old overclaim** |
| even/spectral `W_X=0` target branch | yes if target encoded | yes as an invariant, no as a derivation | **allowed; exposes old overclaim** |
| native `C3`-orbit Berry phase on the circulant | 0 (eigenvector rigidity, retained) | yes | gives 0, not 2/9 |
| native `Z^3` plaquette / staggered-`eta` holonomy | roots of unity / `Z2` | yes | quantized, not 2/9 |
| Hirzebruch `G`-signature defect of `L(3;1)` | **exactly `-2/9`** (`(N-1)(N-2)/3N`, distinct family) | **no** (curved imported `S^3/Z_3`) | APS-`eta` (AVOID-list); already on main (`Z_N_ASYMMETRY_RESIDUAL_1`); + radian-bridge no-go |

The combinatorial space of future mechanisms is not exhaustive in principle. Within
the active nondegenerate spectral-scalar branch, (N2) is a complete obstruction;
outside that branch, this note records the open or target-encoded routes instead
of pretending they are closed.

## No-Go Discipline Gate

**Status: PASS for demotion plus the narrow active spectral-scalar no-go only.**
The claim closed is not "`delta=2/9` is underivable" and not "no real
`C3`-invariant scalar action can stationarize it." It is the narrower statement:
in the conjugation-even/spectral subclass `W(r, Re z^3)`, the nondegenerate branch
`W_X != 0` cannot stationarize `delta=2/9`; the `W_X=0` and `Im z^3` branches are
open or target-encoded rather than derivations.

- **N1 — alternative routes:** active spectral scalar (forbidden, N2);
  general real `C3` scalar with `Im z^3` (allowed if target encoded, not a
  derivation); even/spectral `W_X=0` target branch (allowed if target encoded, not
  a derivation); partition map (delivers `r` not `delta`, N3); native
  Berry/holonomy (0 or roots of unity); `C3`-covariant `eta`/holonomy (not closed).
- **N2 — wall independence:** the symmetric-function separation (N1) and the
  restricted branch stationarity (N2) are exact algebra; the counter-branch checks
  (N2b/N2c) independently show why the old universal claim fails.
- **N3 — hidden-wall scan:** load-bearing inputs are the circulant structure
  (A1+A2) and exact symmetric-function/Wirtinger algebra (runner). The old hidden
  assumptions are now explicit: omitting `Im z^3` requires a conjugation-even or
  spectral restriction, and excluding `W_X=0` requires a nondegeneracy condition.
- **N4 — residual matching:** matches the `delta=2/9` open gate
  (`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE`) and the session's partition-map
  result; the `G`-signature `-2/9` is cited (already on main), not re-derived.
- **N5 — rhetoric audit:** "provably cannot" now appears only for the
  nondegenerate spectral-scalar branch. The broader scalar statement is withdrawn.
- **N6 — partial-closure:** the open paths are named without declaring them axioms:
  supplied-target scalar extrema, genuine phase/covariant selectors, and
  `eta`/holonomy-style routes.
- **N7 — steelman:** the strongest objection - a cleverly chosen scalar functional
  might still hit `2/9` - is accepted and fenced. Such a scalar can stationarize
  the supplied target; it is not a first-principles derivation unless the target
  value is derived elsewhere.
- **N8 — cross-cycle echo:** this does not re-open the worked `(N-1)/N^2`/APS-`eta`
  routes, and it no longer asserts that the lepton phase gate has already collapsed
  into any other retained gate.

## What this note does NOT claim

- Does **not** close `delta = 2/9` (it stays `open_gate` / Tier-A admission).
- Does **not** foreclose the `C3`-covariant `eta`/holonomy route.
- Does **not** foreclose general real `C3` scalar actions using `Im z^3`; it shows
  those can stationarize a supplied target and therefore are not no-go targets.
- Does **not** foreclose even/spectral `W_X=0` target extrema; it records them as
  target-encoded rather than derived.
- Does **not** derive `r=1/2` (it states `r` is the modulus a scalar action *can*
  reach; the lepton occupancy of `r=1/2` is matched, per the dial discipline).
- Does **not** re-derive the `G`-signature `-2/9`, the six `(N-1)/N^2` routes,
  APS-`eta`, Fisher-Rao, or `L(N;1)` holonomy (all on main / the AVOID-list).
- Sets no audit status.

## Load-bearing references

- [`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md`](LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md)
  (open_gate) -- the `delta=2/9` gate this prunes one route of.
- [`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md`](KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31.md)
  (retained_bounded) -- the native `C3`-orbit Berry phase is 0
  (eigenvector rigidity).
- [`Z_N_ASYMMETRY_RESIDUAL_1_FINITE_VS_CONTINUUM_NOTE_2026-05-31.md`](Z_N_ASYMMETRY_RESIDUAL_1_FINITE_VS_CONTINUUM_NOTE_2026-05-31.md)
  (retained_bounded) -- the `G`-signature defect `-2/9` (cited, not
  re-derived).
- [`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
  (retained_no_go) -- the dimensionless-to-radian bridge wall, i.e. why a
  rational `-2/9` is not yet a radian.
- [`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md`](REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06.md)
  -- the partition map delivers `r` not `delta` (N3 convergence).

## Forbidden imports check

- No PDG values consumed; the masses do not enter (the no-go is structural algebra
  on the circulant). No literature comparators; no fitted selectors; no new axiom.
- The `G`-signature `-2/9` is cited as the existing on-main object, not introduced.

## Validation

`scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py` (`PASS=20 FAIL=0`,
exact sympy): Section S (the `e1/e2/e3` separation; `e2` delta-blind, `e3` via
`cos 3delta`), Section W (nondegenerate spectral-scalar branch forces
`delta = n pi/3`; `2/9` excluded), Section F (`Im z^3` and `W_X=0` counter-branches
explicitly stationarize a supplied `delta=2/9` target), Section C (partition-map
convergence: modulus not phase), Section B (scope: demotion plus narrow branch
no-go).

## Reading rule

This note is the claim boundary for: charged-lepton `r` (modulus) and `delta`
(phase) live on separate spectral data; the register-not-read partition map
delivers the modulus, not the phase; and the only scalar-action no-go kept
here is the nondegenerate conjugation-even/spectral branch `W_X != 0`. General
real `C3` scalars and even/spectral `W_X=0` extrema can stationarize a supplied
phase target, so they are open/target-encoded routes rather than forbidden
routes. The note does not close `delta = 2/9`.

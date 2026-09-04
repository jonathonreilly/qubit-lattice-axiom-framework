# Color Composition Rule From Matter-Bilinear Polar Transport: Conditional Bounded Theorem

**Date:** 2026-07-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set, predict, or apply an audit outcome.
**Primary runner:** [`scripts/color_composition_rule_matter_bilinear_polar_transport_2026_07_06.py`](../scripts/color_composition_rule_matter_bilinear_polar_transport_2026_07_06.py)
**Cache:** [`logs/runner-cache/color_composition_rule_matter_bilinear_polar_transport_2026_07_06.txt`](../logs/runner-cache/color_composition_rule_matter_bilinear_polar_transport_2026_07_06.txt)

## Summary
This bounded theorem note gives a conditional composition and transport rule for a cross-site matter bilinear after a `C^3` color carrier has already been supplied at each endpoint. It does not derive that carrier, does not derive a gauge dynamics, and does not close the bonded-pair arena transport residual.
The named premises are:
```text
SUPPLIED-C3:
at each site under discussion, a three-complex-dimensional color carrier is
supplied as endpoint data.

SUPPLIED-BILINEAR:
a full-rank cross-site bilinear map M(x,y): C_x^3 -> C_y^3 between the
supplied carriers is itself supplied data. No fermion fields, CAR algebra,
occupancy structure, local field operators, or physical matter ontology are
derived or imported; "matter bilinear" names the supplied map's intended
role, not a derivation.
```
The four axioms supply neither premise. (Non-load-bearing pointer only: the
bonded-pair arena is a candidate arena for such a carrier; the
identification is the open realization bridge, and nothing here uses it.)
The exact content is:
```text
SUPPLIED-C3
AND full-rank cross-site matter bilinear M(x,y): C_x^3 -> C_y^3
  => polar unitary U(x,y) with exact endpoint-frame covariance.
```
The result is a carrier/composition-rule statement. It supplies no generator, no rate, no action, no probability, and no weight.

## The texts in play
The current axiom memo sets the admission discipline:

> "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise."

Thus the lattice, one-site qubit possibility domain, local admissibility rule, and fixed records do not by themselves name a `C^3` color carrier or a cross-site color bilinear.
The June 8 cross-site bilinear note is quoted as unaudited target/context only:

> "**Precondition (load-bearing):** the construction is defined **only when the cross-site bilinear is full rank**."

It also states:

> "Full rank still requires three independent occupied color directions."

and:

> "This is a *kinematic* carrier/routing existence result."

This note does not consume that row as authority. The polar covariance and rank exhibits below are recomputed self-contained by the runner.
The June 8 non-autonomy note is also quoted as unaudited target/context only:

> "The non-autonomy exhibit is a bounded route constraint, not a no-go against all gauge dynamics."

It leaves open:

> "Alternative routes left open: carry `(U_eff,Q)` or `M` rather than `U_eff` alone; restrict to the minimal-occupancy sector; seek coarse-grained slaving of hidden data; use non-quadratic or record-coupled matter dynamics; use a different compression or connection-level variable."

This note consumes those sentences only as target/context for the boundary. It does not import the June 8 model Hamiltonian, increment law, trajectory evidence, or audit status.
The July 6 factor-preservation note is used as a format exemplar: named premise discipline, exact runner verification, audit-gated citation language, and residuals that are not converted into T-claims. No technical claim from that note is consumed here.

## T1 -- Exact polar covariance for the matter-bilinear link
**T1 (exact, runner-verified):** Assume SUPPLIED-C3 at sites `x` and `y`. Let
```text
M = M(x,y): C_x^3 -> C_y^3
```
be a full-rank complex `3 x 3` cross-site matter bilinear. By the standard finite-dimensional polar decomposition theorem, there is a unique factorization
```text
M = U P,
P = (M^dagger M)^(1/2) > 0,
U = M (M^dagger M)^(-1/2),
```
with `U` unitary and `P` positive definite.
Under independent endpoint frame changes by unitary matrices `g_x` and `g_y`,
```text
M -> M' = g_y M g_x^dagger.
```
Then
```text
(M')^dagger M' = g_x (M^dagger M) g_x^dagger.
```
The positive square root therefore transforms as
```text
P' = g_x P g_x^dagger.
```
Consequently
```text
M' = (g_y U g_x^dagger)(g_x P g_x^dagger),
```
where the first factor is unitary and the second factor is positive. By uniqueness of the polar decomposition,
```text
U' = g_y U g_x^dagger,
P' = g_x P g_x^dagger.
```
This is an exact conditional frame-transport lemma for the SUPPLIED carriers: the supplied bilinear induces a frame-comparison map between the endpoint `C^3` carriers, conditional on SUPPLIED-C3, SUPPLIED-BILINEAR, and full rank.
The runner verifies this with an exact rational witness:
```text
M = U0 D,
U0 = signed permutation,  D = diag(1,2,4).
```
Then
```text
M^dagger M = D^2,
P = D,
U = U0,
```
with no irrational square roots. It also verifies exact covariance of this witness under signed-permutation endpoint frame changes, and seeded numerical covariance controls under generic unitary frames with singular-gap assertions.
Relation to bonded-pair arena R5: this proves a DIFFERENT conditional frame-transport lemma -- for supplied `C^3` color carriers -- not the comparison of qubit-domain presentations across sites that R5 concerns. The relation between the two is open; R5 is not addressed, not closed.

## T2 -- Determinant reduction, Z_3 ambiguity, and Wilson traces
**T2 (exact consequence of T1):** Since `U` is unitary,
```text
abs(det U) = 1.
```
Choosing a cube root `r` with
```text
r^3 = det U
```
gives
```text
U_SU = U r^(-1),
det(U_SU) = 1.
```
The choice of `r` has exactly a `Z_3` ambiguity: the three cube roots differ by multiplication by the three cube roots of unity, and the resulting determinant-reduced matrices differ by the corresponding center element. No canonical resolution of this center choice is supplied here. This is residual R-z3-center, not a hidden convention.
Determinant reduction applies to the POLAR UNITARY. On the main witness the
polar factor is `U0` itself with `det(U0) = 1` exactly -- already on the
determinant-one branch (`det(D) = 8` is a property of `P`, irrelevant to the
reduction). The runner exhibits the ambiguity on an odd signed permutation
`U1` with `det(U1) = -1`: the rational cube root `r = -1` gives
`U_SU = -U1` with `det(-U1) = +1` exactly, and the remaining two branches
differ by the complex cube roots of unity -- the `Z_3` ambiguity as an exact
algebraic fact, with the rational branch represented exactly.
Wilson statement and convention: the Wilson trace in this note uses the polar-unitary links `U`, before determinant reduction. With the column-vector convention of T1, the path `x -> y -> z -> x` is evaluated by composed transport:
```text
W_xyz = tr(U(z,x) U(y,z) U(x,y)).
```
Under the T1 transformation law the interior frames cancel and the trace is
conjugated by the remaining endpoint frame:
```text
U'(z,x) U'(y,z) U'(x,y)
  = g_x U(z,x) g_z^dagger g_z U(y,z) g_y^dagger g_y U(x,y) g_x^dagger
  = g_x (U(z,x) U(y,z) U(x,y)) g_x^dagger,
```
so `W_xyz` is invariant under all local endpoint frame changes. (No other
ordering is claimed; under this arrow convention the order is forced by
composition of maps.) Reverse orientation is a stipulation, not a
consequence: `U(y,x) = U(x,y)^dagger` holds only if the reverse bilinear is
defined by `M(y,x) = M(x,y)^dagger` or the reverse link is defined as the
inverse; this note adopts that definition explicitly where a reverse link is
needed. These closed-loop traces are algebraic endpoint-frame invariants of
supplied polar links (Wilson-form), NOT lattice-gauge observables: no gauge
field, action term, path-integral weight, positivity, area law, confinement
claim, measure, or dynamics is asserted. The same invariance holds for a
fixed branch choice of determinant-reduced `SU(3)` links, still subject to
the separate `Z_3` branch bookkeeping.
The runner verifies Wilson invariance with seeded numerical full-rank links and singular-gap assertions, and with an exact signed-permutation witness.

## T3 -- Full-rank precondition and rank boundary
**T3 (precondition honesty, runner-verified):** The construction is defined only where `M(x,y)` is full rank. The exact full-rank witness is the same rational case:
```text
M = U0 diag(1,2,4),
rank(M) = 3.
```
A rank-deficient exact witness is:
```text
M0 = diag(1,2,0),
rank(M0) = 2.
```
At such a point `(M0^dagger M0)^(-1/2)` is not defined on the null direction, so the polar transport rule used in T1 is not defined as a full unitary transport on `C^3`.
The boundary is also discontinuous as a unitary transport rule along these paths (no claim beyond these witness paths is made). The two full-rank rational families
```text
diag(1,1,epsilon)
and
diag(1,1,-epsilon)
```
approach the same rank-deficient limit as `epsilon -> 0`, but their polar unitary factors -- COMPUTED exactly by the runner at `epsilon = 1/2, 1/4, 1/8, 1/64` -- are constantly `I_3` and constantly `diag(1,1,-1)`. Thus no single continuous full-unitary extension exists at the rank-deficient limit along these paths.
This note does not derive which physical sectors satisfy full rank. That is residual R-rank-selection, and it carries the June source's sharper occupancy wording as target context: "Full rank still requires three independent occupied color directions" -- lower occupancy does not carry the composite link. A possible relation to FERMI-FILL is an open pointer only, not a claim and not consumed here.

## Non-autonomy boundary and untouched walls (scope, not a T-claim)

The induced link is state-dependent: it is a polar compression of the supplied bilinear, not an autonomous primitive link variable. This section is scope/boundary metadata quoting unaudited June-8 context; it is NOT theorem content and carries no claim weight. The June 8 non-autonomy note is used only for its unaudited boundary language:

> "The non-autonomy exhibit is a bounded route constraint, not a no-go against all gauge dynamics."

and its open-route sentence:

> "Alternative routes left open: carry `(U_eff,Q)` or `M` rather than `U_eff` alone; restrict to the minimal-occupancy sector; seek coarse-grained slaving of hidden data; use non-quadratic or record-coupled matter dynamics; use a different compression or connection-level variable."

This note supplies only the carrier/composition-rule content of the polar map. It does not touch the generator/rate/action package, the ST1/ST2 wall, or any graded-constraint port-3/port-4 split. It supplies no dynamics, no weights, no transition probabilities, no path measure, and no record-production rule.

## Residuals and scope boundary (not a T-claim)
- R-supplied-c3: SUPPLIED-C3 itself is open. (Pointer: the bonded-pair arena is a candidate; the identification is the open realization bridge.)
- R-supplied-bilinear: SUPPLIED-BILINEAR itself is open -- no derivation that any local/covariant field operator supplies it, and no matter ontology is imported.
- R-no-selection (carried from the June source's own caveat): nothing here claims the framework's physical link IS this composite; this is a kinematic composition-rule statement about supplied data.
- R-rank-selection: this note requires full-rank `M(x,y)` and does not derive which physical states or sectors supply it.
- R-z3-center: determinant reduction to `SU(3)` has an exact `Z_3` cube-root ambiguity. No canonical branch is supplied.
- R-non-autonomy: the induced link remains matter-state-dependent. The dynamics wall is not closed.
- R5-transport: NOT addressed. T1 is a different conditional transport lemma (supplied color carriers, not qubit-domain presentations); the relation between them is open.
- R-chiral: inherited unchanged from the factor-preservation note. Nothing here supplies chiral weak coupling.
- R-hypercharge: inherited unchanged from the factor-preservation note. Nothing here identifies a physical hypercharge direction.

## Honest boundary
This note does not derive the `C^3` color carrier, does not derive the cross-site bilinear (no derivation that any physical sector supplies full rank, and no derivation that the bilinear is a local/covariant field operator), does not derive color from the four axioms, does not identify the bonded-pair arena with physical color, does not close R5, does not select physical full-rank sectors, does not choose a `Z_3` center branch, does not derive a gauge action, does not supply dynamics, does not supply a generator, rate, action, path integral, probability, or weight, does not assert Wilson positivity or confinement, does not add an axiom, does not add a primitive, does not create Tier-A content, does not apply an audit verdict, and does not decide a landing.

## Citation contract

Citation is gated by the standard discipline: this note is Class C source material with no premise weight until audit ratification; after ratification, citation is at the audited claim scope exactly. Within that gate:

Downstream rows may cite this note for T1's exact polar algebra:
```text
full-rank M(x,y)
=> unique polar decomposition M = U P
=> U transforms as g_y U g_x^dagger
=> P transforms as g_x P g_x^dagger.
```
Downstream rows may cite T2 for determinant bookkeeping and closed-loop trace (Wilson-form) endpoint-frame invariance at the stated normalization, orientation stipulation, and convention:
```text
unitary polar links have abs(det U)=1;
SU(3) determinant reduction has a Z_3 branch ambiguity;
closed path-ordered Wilson traces are locally frame invariant.
```
Downstream rows may NOT cite this note for: a derived `C^3` carrier; R5 closed; physical color identification; a full-rank sector theorem; canonical center-branch selection; gauge dynamics; generator/rate/action content; Wilson positivity; confinement; chiral weak coupling; hypercharge; or any audit-status upgrade.

## Dependencies table
| dependency | status/boundary used here | consumed content |
|---|---|---|
| [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) | current axiom memo; axioms are premises, not bounded-status sources | quoted premise-discipline sentence; no `C^3` carrier imported |
| `COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md` | unaudited target/context only | quoted boundary sentences; polar covariance and rank witnesses recomputed here |
| `INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md` | unaudited target/context only | non-autonomy boundary and open-route quotes only; no dynamics consumed |
| `GAUGE_FACTOR_PRESERVATION_RECORD_TYPED_SELECTOR_CONDITIONAL_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-07-06.md` | process reference only -- NOT a scientific dependency | formatting/discipline conventions; no technical claim consumed |

See-also: none needed for this source note.

## Runner verification map
The runner verifies the exact rational polar witness, exact signed-permutation covariance, determinant and `Z_3` bookkeeping, path-ordered Wilson invariance, full-rank and rank-deficient exhibits, and the rank-boundary discontinuity witness. It also runs seeded numerical covariance and Wilson controls with singular-gap assertions.
The runner text-audits every quoted sentence from the two June 8 source rows used above, and performs an AST self-scan for no-network/no-subprocess discipline. Expected output shape:
```text
[PASS] ...
DECLARATION premise=SUPPLIED-C3; untouched_walls=...
EXACT ...
NUMERIC ...
TOTAL PASS=... FAIL=0
```
The cache linked in the header is generated from this runner's output.

## Source-note boundary
Hypothesis set: the four current framework axioms as context; the named conditional premises SUPPLIED-C3 and SUPPLIED-BILINEAR; full rank of the supplied bilinear; independent endpoint unitary frame changes; the explicit reverse-orientation stipulation; and standard finite-dimensional polar decomposition. Orientation note: this note's `M(x,y): C_x -> C_y` is a deliberately reoriented map relative to the June-8 source's convention; the transformation law is stated for this note's arrow convention.
Forbidden imports: no derived carrier, no bonded-pair arena carrier landing, no rank-sector selection, no center-branch convention, no dynamics, no generator, no rate, no action, no probability, no weight, no Wilson positivity, no confinement, no chiral bridge, no hypercharge bridge, no new axiom, no primitive, no Tier-A admission, no parent-row verdict, and no audit decision is imported. This note is a bounded conditional source note for independent review.

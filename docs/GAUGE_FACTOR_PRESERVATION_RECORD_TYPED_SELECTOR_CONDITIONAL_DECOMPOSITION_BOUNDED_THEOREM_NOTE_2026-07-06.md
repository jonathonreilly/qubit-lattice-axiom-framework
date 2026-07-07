# Gauge Factor Preservation From Record-Typed Selector: Conditional Decomposition Bounded Theorem

**Date:** 2026-07-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set, predict, or apply an audit outcome.
**Primary runner:** [`scripts/gauge_factor_preservation_record_typed_selector_2026_07_06.py`](../scripts/gauge_factor_preservation_record_typed_selector_2026_07_06.py)
**Cache:** [`logs/runner-cache/gauge_factor_preservation_record_typed_selector_2026_07_06.txt`](../logs/runner-cache/gauge_factor_preservation_record_typed_selector_2026_07_06.txt)

## Summary
This note records a bounded-theorem conditional decomposition for the
factor-preservation surface. It is not a derivation of gauging, not a
derivation of the carrier, and not a derivation of a factor-preservation rule
from the four axioms.
The exact content is:
```text
supplied C^6 = C^3 tensor C^2
AND preservation of M_3 tensor I_2 and I_3 tensor M_2
  => the stabilizer inside u(6) is exactly the factorwise algebra.
```
T1 is exact and runner-verified over integers/Fractions after real/imaginary vectorization. No floating rank is used as evidence.
The bridge content is premise-named:
```text
REGISTERED-FACTOR (named premise, introduced here):
the record/readout structure registers a fixed factor subalgebra of the local domain; equivalently, the split
  M_3 tensor I_2 / I_3 tensor M_2
is record-typed data.
```
The four axioms do not supply REGISTERED-FACTOR. The Record axiom's content-only, site-local readout makes record-typed data the natural candidate supplier, but that is a candidate bridge, not axiom content. Under REGISTERED-FACTOR, record-compatible transformations normalize the registered factor split, and T1 gives the factorwise algebra exactly.
REGISTERED-FACTOR plays the same role for gauging selection that MARGINAL-READ
plays for readout in the singlet-record factorization note: both are
record-as-structure bridges. Whether one derives the other is an open
residual, not a claim.

## The texts in play
The current axiom memo states:
> "Only records are readable. A readout value is determined by record content alone."
It also sets the admission discipline:
> "Further physical structure requires derivation, bridge, explicit admission, or approved primitive registration before use as a premise."
Thus Record supplies content-only readout, but it does not name a `C^3 tensor C^2` carrier, a factor split, a gauging principle, or chiral weak coupling.
The June 18 normalizer note is quoted as unaudited target/context only:
> "It proves the exact finite statement that, once a factor-algebra preservation rule is supplied on the same `C^3(base) x C^2(fiber)` carrier, the algebraic normalizer is uniquely the factorwise `su(3) + su(2) + u(1)` surface rather than full `u(6)`."
It also states the open-source boundary:
> "This note proves its consequence; it does not make that rule an axiom or a retained primitive."
and, for chirality:
> "The finite normalizer theorem is blind to vector versus left-handed weak coupling."
This note does not consume that row as authority. The runner recomputes the
load-bearing algebra self-contained.
The June 16 no-go note is also quoted as unaudited target/context only. Its no-go statement is:
> "Thus any selector depending only on conjugation-invariant algebraic data of the carrier, or on irreducibility/scalar-commutant criteria, cannot select the specific factorwise `su(3)+su(2)+u(1)` embedding."
Its escape statement is:
> "Selecting it requires additional non-invariant structure: the factorization/gauging principle, `MR_color`, and the chiral weak-coupling bridge."
It leaves non-invariant typed routes live:
> "This is not a broad no-go against deriving gauge selection. It leaves live:"
and names:
> "a future retained theorem deriving chiral `su(2)_L`"
The same note explains why a factor-typed selector is outside the invariant-data route:
> "Factor-locality or operator-Schmidt rank could distinguish the embedding, but only by consuming the supplied `C^3 x C^2` tensor split, which is exactly the extra structure the route was trying not to import."
and:
> "A future local-dynamics theorem could privilege a tensor factor, a link representation, or a chiral coupling by non-conjugation-invariant structure."
REGISTERED-FACTOR is precisely such non-invariant typed data. This note does not claim that it is derived.

## T1 -- Exact factor-preservation reduction inside u(6)
**T1 (exact, runner-verified):** Work on the supplied model surface
```text
C^6 = C^3 tensor C^2.
```
Represent `u(6)` by antihermitian `6 x 6` matrices. The runner uses the standard real basis: six imaginary diagonal generators, plus real antisymmetric and imaginary symmetric off-diagonal generators. Exact real/imaginary rank gives:
```text
dim u(6) = 36.
```
The factorwise candidate is the image of
```text
u(3) direct-sum u(2) -> u(6)
(A, B) |-> A tensor I_2 + I_3 tensor B.
```
The domain has dimension `9 + 4 = 13`. The exact image rank is `12`. The missing dimension is the center overlap:
```text
i I_3 tensor I_2 = I_3 tensor i I_2 = i I_6.
```
Equivalently, `(i I_3, -i I_2)` spans the one-dimensional kernel, so
```text
dim(u(3) tensor I_2 + I_3 tensor u(2)) = 9 + 4 - 1 = 12.
```
For the stabilizer characterization, solve for `X in u(6)` satisfying
```text
[X, M_3 tensor I_2] subset M_3 tensor I_2,
[X, I_3 tensor M_2] subset I_3 tensor M_2.
```
The runner imposes all conditions over `Q`: zero off-fiber blocks and equal fiber-diagonal blocks for `M_3 tensor I_2`; zero off-base blocks and equal base-diagonal `2 x 2` blocks for `I_3 tensor M_2`.
The exact stabilizer nullity inside `u(6)` is `12`. The factorwise algebra is contained in the stabilizer, and the stabilizer is contained in the factorwise algebra by exact combined-rank equality:
```text
rank(factorwise span + stabilizer span) = 12.
```
The decomposition bookkeeping is:
```text
su(3) tensor I_2       dim 8,  traceless
I_3 tensor su(2)       dim 3,  traceless
semisimple part        dim 11
abelian image          dim 1,  generated by i I_6
```
The factor-identity pair space has two formal directions before quotienting, but the relative identity pair maps to zero on `C^3 tensor C^2`:
```text
i I_3 tensor I_2 - I_3 tensor i I_2 = 0.
```
Thus, in this tensor-product carrier image, there is no second
central/factor-identity `u(1)` image. The only central abelian image
direction is the global `u(1)` generated by `i I_6`, whose trace is `6i` and
is not traceless. (Cartan directions inside `su(3)` or `su(2)` are of course
traceless abelian subalgebras; the statement concerns factor-identity/central
directions only.)
Structure verification (not dimension bookkeeping alone): the runner
verifies exactly, over `Q`, that the 11 traceless generators close under Lie
brackets within their own span, that every cross-bracket between the
`su(3)`-lift and the `su(2)`-lift vanishes identically (direct sum), that the
global abelian direction commutes with all of them (central), and that the
Killing form on the 11-dimensional traceless part is block-diagonal across
the two factors and has nonzero exact determinant (nondegenerate). This
upgrades "semisimple part is exactly su(3) + su(2)" from dimension counting
to verified Lie structure.

Formalization caveat: "factor preservation" is formalized here as the ordered
infinitesimal condition that `ad_X` maps each named factor subalgebra into
itself. Equivalence to preserving the Hilbert-space tensor factorization
itself is not proven here; factor-swapping maps are excluded on this carrier
simply because the factors have different dimensions (`3 != 2`), and that
exclusion is by dimension mismatch, not by theorem.

Conclusion T1: GIVEN the supplied split and factor preservation in the stated
ordered sense, the stabilizer inside `u(6)` is exactly the factorwise algebra
of dimension `12`, whose semisimple part is the verified direct sum
`su(3) + su(2)`, with the one central abelian direction stated above. This is
exact stabilizer bookkeeping on a supplied model surface, not a physical
gauge selection.

## T2 -- REGISTERED-FACTOR as the named conditional supplier
**T2 (conditional on REGISTERED-FACTOR; a compatibility convention, not a
derived theorem):** stated plainly first: the chain "registered split +
compatibility with registered structure => split preservation" is
DEFINITIONAL -- compatibility with a registered split just means preserving
it. The four axioms supply no transformation group and no independent
definition of "record-compatible," so T2's content is a bookkeeping
convention that makes the premise's consequence exact via T1, not a selection
theorem. What T2 contributes is the pairing: IF the split is record-typed
data (REGISTERED-FACTOR), THEN the transformations compatible with that data
normalize the two registered factor subalgebras:
```text
M_3 tensor I_2
and
I_3 tensor M_2.
```
By T1, the infinitesimal algebra of such transformations is exactly the factorwise algebra: under REGISTERED-FACTOR, the supplied split's stabilizer has semisimple part `su(3) + su(2)` with the central abelian direction stated in T1.
The honesty point is decisive: REGISTERED-FACTOR is not axiom content. The four axioms name the lattice, one-site possibility domain, local admissibility, and fixed records. They do not name a `C^6` carrier, a `C^3 tensor C^2` split, or a factor-preservation rule.
The Record axiom is nevertheless the natural candidate source because it makes readout depend on record content alone. If record content is typed by a factor subalgebra, then the type is non-invariant structure. That places REGISTERED-FACTOR among the non-invariant inputs the June 16 no-go's escape text names as the live route -- it is ONE such input, not the whole of that escape (which also names the gauging principle, `MR_color`, gauge-action/connection selection, and chiral `su(2)_L`).
This note therefore proves only:
```text
REGISTERED-FACTOR
AND supplied C^3 tensor C^2 model surface
  => exact factorwise-instead-of-u(6) algebra selection.
```
It does not prove REGISTERED-FACTOR.

## Residuals and scope boundary (not a T-claim)
- R-registered-factor: REGISTERED-FACTOR itself is open. The four axioms do not supply it. Its relation to MARGINAL-READ is also open.
- R-which-factor: this note does not choose which subalgebra is registered. It computes the consequence once a split is supplied; it does not assume color versus weak physical meaning.
- R-chiral: chiral `su(2)_L` is outside scope. The June 16 no-go leaves live "a future retained theorem deriving chiral `su(2)_L`", and the June 18 normalizer note says, "The finite normalizer theorem is blind to vector versus left-handed weak coupling."
- R-hypercharge: the abelian image is hypercharge-like only. It is one global `u(1)` direction on this tensor-product carrier image, not a physical hypercharge identification.
- R-u6-embedding: the `C^6` here is a supplied model surface, `C^3 tensor C^2`, used as standard base-times-fiber bookkeeping. This note does not derive that the physical local domain is `C^6`.

## Honest boundary
This note does not derive gauging, a gauge action, connection, dynamics,
couplings, anomaly-complete matter content, or electroweak matching. The four
axioms supply no independent definition of "record-compatible
transformations"; T2 is a compatibility convention, and REGISTERED-FACTOR
alone does not supply `MR_color`, gauging, gauge dynamics, chirality, or a
physical carrier. It does not choose the registered factor, identify `C^3` with physical color, identify `C^2` with physical weak structure, identify the abelian remainder with hypercharge, supply chiral structure, claim the local physical domain is `C^6`, resolve REGISTERED-FACTOR, add an axiom, add a primitive, create Tier-A content, apply an audit verdict, or decide a landing.

## Citation contract

Citation is gated by the standard discipline: this note is Class C source
material with no premise weight until audit ratification; after ratification,
citation is at the audited claim scope exactly. Within that gate:

Downstream rows may cite this note for T1's exact algebra:
```text
factor preservation inside u(6)
=> factorwise algebra of dimension 12
=> semisimple part su(3) + su(2)
=> one-dimensional abelian image on this carrier.
```
Downstream rows may cite T2 only as a conditional bookkeeping statement under the named premise REGISTERED-FACTOR (never as evidence toward a retained bridge; T1 is the only reusable exact algebra result here), with the June 16 escape context quoted: invariant carrier data cannot select the embedding, while additional non-invariant structure is the live route, of which REGISTERED-FACTOR is one named input.
Downstream rows may NOT cite this note for: gauging selection as derived; REGISTERED-FACTOR as established; a physical color or weak landing; chiral `su(2)_L`; physical hypercharge; a physical `C^6` local-domain derivation; or any audit-status upgrade.

## Dependencies table
| dependency | status/boundary used here | consumed content |
|---|---|---|
| [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) | current axiom memo; axioms are premises, not bounded-status sources | quoted Record/content and premise-discipline sentences; no factor split imported |
| `GAUGE_FACTOR_LOCAL_SELECTOR_NORMALIZER_THEOREM_NOTE_2026-06-18.md` | unaudited | target/context quotes only; algebra recomputed here |
| `GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md` | unaudited | no-go and escape-route quotes only; not consumed as authority |

| `COLOR_SINGLET_RECORDS_G2_FACTORIZATION_SITE_LOCAL_LOCKING_BOUNDED_THEOREM_NOTE_2026-07-06.md` | format exemplar only | premise-naming discipline and citation-contract style; no technical claim consumed |
See-also (non-load-bearing, not a dependency):
`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`
(parent open-gate context; not read and not consumed by this note).

## Runner verification map
The runner verifies the axiom, June 18, and June 16 quoted sentences against their source files. It computes `dim u(6) = 36`, the factorwise image dimension `12`, the one-dimensional center overlap, the stabilizer nullity `12`, both containments by exact rank, and the decomposition bookkeeping:
```text
su(3) dim 8, traceless
su(2) dim 3, traceless
semisimple dim 11
abelian image dim 1
relative factor-identity kernel dim 1
```
It verifies the Lie-structure block exactly over `Q`: bracket closure of the
11 traceless generators within their span, vanishing of every cross-bracket
between the two factors, centrality of the global abelian direction, and the
Killing form's block-diagonality and nonzero exact determinant on the
traceless part.

It also performs an AST self-scan for read-only/no-network/no-subprocess discipline. Expected output shape:
```text
[PASS] ...
DECLARATION premises=minimal_axioms_context; REGISTERED-FACTOR(...)
DIMENSIONS u6=36 factorwise=12 stabilizer=12 ...
TOTAL PASS=8 FAIL=0
```
The cache linked in the header is generated from this runner's output.

## Source-note boundary
Hypothesis set: the four current framework axioms as context; the named conditional premise REGISTERED-FACTOR; the supplied `C^3 tensor C^2` model surface; the two registered factor subalgebras `M_3 tensor I_2` and `I_3 tensor M_2`; and standard finite-dimensional matrix algebra recomputed exactly by the runner.
Forbidden imports: no new axiom, primitive, Tier-A admission, physical carrier
landing, registered-factor derivation, chiral weak bridge, hypercharge
identification, gauge dynamics, parent-row verdict, or audit decision is
imported. This note is a bounded conditional source note for independent
review.

# Native coupling between large features and their environment

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_feature_interactions.py](../scripts/native_feature_interactions.py)

The existing one-qubit interaction produces a local coupling between extended
features, with no added scalar interaction. Its checked diagonal bulk term
depends on shared plaquette parities. A larger rectangular feature does not
therefore acquire an automatically universal coupling proportional to its
unperturbed energy.

## Derive the coupling from the microscopic interaction

Use the supplied anisotropic Hamiltonian and the previously checked local
normal form. Far from longitudinal endpoints, its fourth-order orientation
density is -kappa sum Bp, with kappa=Jz lambda^4/128. Bp is the four-column
plaquette parity; this coefficient follows directly from the native virtual
edge sequence.

For a flipped transverse set F, let boundary(F) contain plaquettes with an
odd number of F sites. In a locally ordered background, the change per layer
is 2kappa sum over boundary(F) of Bp. For two disjoint feature sets F,G whose
longitudinal intervals overlap, their connected interior energy is

    Delta E_FG = -4kappa |I intersect J|
                       sum over boundary(F) intersect boundary(G) of Bp.

This is a derived environment-dependent coefficient, not a new interaction.
The background remains conditional. Endpoint terms require separate treatment;
the displayed term is not a scattering amplitude or proof of binding.

For F={(0,0),(2,0)} and G={(0,1),(2,1)}, each feature changes eight plaquettes
and they share four. On the uniform background their connected contribution
is -16kappa times overlap length. Other backgrounds can change its sign.
The coefficient interaction is local in the transverse geometry; no long-range
universal force follows.

## Why wide rectangles have a corner cost

A nonwrapping rectangular cross section produces exactly four bad plaquettes,
regardless of area A. Its fourth-order interior tension is therefore
Jz lambda^4/16, whereas its two longitudinal ends cost 4Jz A at order zero.
These are diagonal configuration energies, not an established particle mass
and charge.

This geometric cancellation extends coefficient by coefficient. The actual
local normal-form construction preserves the exact plane symmetries. Its
diagonal orientation polynomial has even incidence in every transverse row
and column. A local monomial can detect a flipped rectangle only near a
corner, where it crosses both transverse boundaries. At each fixed order,
with all corners farther apart than the coefficient range, the bulk cost has
no area or perimeter term. Exact size independence uses a homogeneous
background; arbitrary backgrounds retain corner support but can give different
corner values.

No convergent all-orders or growing-order assertion is made. Endpoints,
periodic seams, short rectangles and off-diagonal dynamics require their own
analysis. Even-by-even rectangular cross sections admit plane-neutral flip
operators, but symmetry permission does not prove a collective eigenmode.

## Evidence and next obstacle

The root proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9769/FEATURE_INTERACTION_PROOF.md`)
uses the direct fourth-order coefficient and the equivariance of the actual
local construction. Independent checks cover inclusion-exclusion, signs,
geometry and the finite-order corner law. Exact enumeration tests rectangular
and irregular sets and general row/column-even local monomials.

Subsystem-symmetric plaquette models are established prior art; see
[Rayhaun and Williamson](https://arxiv.org/abs/2112.12735).
This is an application to the current native Hamiltonian, not a new claim
about fractons in general.

The next obstacle is dynamical: native lower-order terms can mix these
configurations before the fourth-order interaction determines a mode.
No stable bound state, fermion identification, gravitational coupling or
cosmological scalar has been derived here. No empirical calibration or
independent observational test is claimed.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.

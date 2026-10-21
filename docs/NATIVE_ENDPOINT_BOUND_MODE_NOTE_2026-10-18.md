# A collective endpoint mode from the native one-qubit interaction

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/native_endpoint_bound_mode.py](../scripts/native_endpoint_bound_mode.py)

Four neighboring column ends bind collectively in the native first-order
coefficient Hamiltonian. Their kinetic motion, bound dispersion and original
readout vertex can all be derived without adding an interaction. The result
uses a specified one-wall-per-column boundary sector; it is not yet a bound
particle of the full microscopic Hamiltonian.

## Retain the shape dynamics instead of assuming a rigid feature

Put one similarly oriented longitudinal wall in each of four columns forming
a transverse unit square. All exterior columns are uniform. In the infinite
longitudinal geometry, a transverse spin flip preserves the total wall count
only when it moves two existing walls. This makes the fixed-column height
sector invariant under K1=P_N V P_N.

The native rules are simple. Equal neighboring heights can rise or fall
together; heights differing by one can swap. X bonds have amplitude -Jx.
Y bonds have +Jy for equal-spin pair motion and -Jy for a mixed-spin swap.
These rules come from the physical Pauli matrix elements.

A flat large rectangle is not invariant under these motions. For area>2,
its squared first-order coupling out of the rigid chart is
4[Jx²(nx-1)ny+Jy²nx(ny-1)]. This does not exclude collective binding: it
requires the shape degrees of freedom to be solved, as follows.

## Exact bound state and dispersion

After quotienting common height translations, the flat configuration connects
to four half-lines of relative heights and two diagonal contact configurations.
A derived combination of the four rays cancels the diagonal contacts. With
physical center R=(h1+h2+h3+h4)/4 and gamma=cos(k/2), this channel has hopping
-2gamma and flat-to-first-site coupling -4gamma, in units Jz lambda.

Its exact lower bound state has

    epsilon_b(k)=-8cos(k/2)/sqrt(3),
    relative-height decay r=1/sqrt(3),
    flat-configuration probability=1/3.

At k=0 the continuum starts at -4; the bound value is approximately
-4.6188021535. The state stays isolated near zero momentum. The physical
first-order endpoint energy is 8Jz+Jz lambda epsilon_b(k). No independent
mass, spring constant or collective field has been supplied.

The state is even under the combined axial quarter-turn of lattice and spin.
This limited lattice symmetry is not full rotational or Lorentz scalar
behavior. The half-angle band formula is local in momentum; global fiber
labels carry a gauge twist.

## Derive the original readout coupling

Use the localized excess of the longitudinal distance-two Fourier readout.
One wall at h contributes -4cos(p/2)exp[ip(h+1/2)]. The derived bound state
therefore gives

    F(p)=4(1+cos(p/2))/(5-3cos(p/2)),
    V(p)=-4cos(p/2)exp(ip/2)F(p).

This is an unnormalized matrix element transferring center momentum between
nearby bound states. At zero momentum V=-16 is a constant, so it does not
excite an internal mode. At finite momentum the vertex is nonzero. No new
source coefficient was added.

It is a response within the supplied excited boundary sector, not vacuum
creation or a derived experimental detector. A finite droplet has two ends;
for long single-column intervals its uniform bare readout is likewise
constant until dressing or other configurations are included.

## Checks and remaining work

The root proof (`outputs/neutral_continuation5_review_2026_10_18/proofs/pr9770/ENDPOINT_BOUND_MODE_PROOF.md`)
and independent height/graph/momentum checks establish the exact coefficient
result. Numerical cutoffs check the analytic wavefunction, dispersion and
source form factor. These are model-development checks, not observations.

Finite paired endpoints, higher-order native mixing, larger cross sections
and physical preparation remain to be solved. The result establishes a
native collective binding mechanism and readout vertex in this sector;
it does not identify a fermion, gravitational scalar or cosmological field.


## Source and execution boundary

The full mathematical sources and owning-head helpers are portable literal inputs. Supplied Hamiltonian, state and momentum families, observable interpretation and limits remain explicit. The primary performs only its stated finite controls, with an enforced aggregate cap, immediate child diagnostics and fresh isolated outputs. Historical saved numbers and reviewer verdicts are provenance, never fresh execution or audit authority. No full-H pole, lifetime, universal force or empirical identification follows merely from a finite control.

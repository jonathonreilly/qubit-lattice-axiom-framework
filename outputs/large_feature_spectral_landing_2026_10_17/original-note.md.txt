---
claim_id: large_feature_spectral_reconstruction_2026_10_17
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied twelve-corner Bloch matrix, fixed pi/zero/pi/pi flux and specified momentum and ordered spectral chamber, its three distinct excitation gaps reconstruct the three hopping coefficients with a fixed sign branch. Common gap scaling implies common hopping scaling on that chamber, hence homogeneous scaling of its full Bloch dispersion. A conditional clock/ruler response identity follows; no physical scalar, stable extended particle, homogeneous fine-grid rule or empirical identification is derived."
upstream_dependencies: []
runner: scripts/large_feature_spectral_response.py
---

# Reconstructing a large-feature model from three excitation gaps

**Type:** bounded_theorem. **Status:** conditional-support, unaudited.

## Question and result

The user's one-qubit-per-site, large-feature proposal suggests working backward
from excitation spectra to interactions. Here that inverse problem is solved
exactly for a supplied three-parameter corner hopping model. Three spectral
splittings reconstruct all three coefficients within a specified branch.
Their dimensionless ratios constrain two shape parameters, leaving a common
energy scale. This is an observation-facing reconstruction formula, not a fit
to observations: the inputs exercised below are synthetic spectra.

The next scalar-coupling question becomes sharper. Along the common-scale
path, both gaps and band curvature scale by the same factor. Under an
additional conformal matter interpretation, consistency specifies a relation
between effective ruler and clock responses. That relation is a target for a
microscopic derivation; choosing it would not derive it.

## Supplied model and exact provenance

This note gives a self-contained calculation for the matrix below; it does
not depend on adopting the unmerged qubit, statistics or symmetry claims.
The starting construction is PR9671, frozen head
`16ae120ee46a1186b5ca81cd7d393396089e77d6`, source
`corner_fermion_large_fermion_effective_theory_and_one_qubit_block_embedding_2026_10_17.py`,
Part 2. The complete relevant graph/flux/Bloch definitions are included in
[this runner](../scripts/large_feature_spectral_response.py).

There are twelve corner labels, unordered pairs of perpendicular directions
from {+x,-x,+y,-y,+z,-z}. Each corner has four intra-cell cuboctahedron edges
and two inter-cell links. The latter send {d,e} at cell v to {-d,e} at v+d,
and similarly exchange e. The Bloch hopping on an oriented edge with cell
shift h has amplitude `-t sigma exp(i k.h)`, plus its Hermitian conjugate,
where t=a on intra-cell edges and t=b on inter-cell links. Each outward
oriented corner triangle additionally has amplitude `i c sigma` along its
orientation and its Hermitian conjugate in reverse. Thus

    H(k;a,b,c) = a H_on(k) + b H_link(k) + c H_chiral(k).

The real signs sigma are +/-1. Their products have flux pi on squares,
plaquettes and tubes and zero on triangles. The runner specifies all cycles
and solves the finite GF(2) system with free bits zero, fixing the gauge.
This precisely defines the matrix, including momentum convention. It uses
no external file or live PR input at execution. Different gauge labels need
not use the same coordinates for the selected momentum.

The provisional parent embeds its 48 coarse-cell qubits in a 5x5x5 fine block,
with one qubit per fine site, 77 frozen spectators and interactions reaching
nine fine spacings. It explicitly supplies this block pattern and does not
derive one-site translation invariance. Its large feature is a broad
wavepacket, not a proved self-bound object of selected size. Those are
context and prospective applicability, not conclusions of this theorem.

## Exact spectrum and reconstruction

Fix `k=(-1,1,-1) pi/2` in the runner's gauge. Exact symbolic determinant gives

    det(z I-H) = [z^2+2az-2a^2-2(b+c)^2]^4
                 [(z-2a)^2-2(b-2c)^2]^2.                 (1)

Equation (1) is checked on the symbolic twelve-by-twelve matrix, not fitted
from numerical eigenvalues. Put

    q = sqrt(2)(b-2c), r = sqrt(3a^2+2(b+c)^2).

The theorem's chamber is

    q>0, b+c<0,
    0 < -3a+q-r < 2q < -3a+q+r.                         (2)

These are strict conditions; no level crossing or sign-branch crossing is
included. They hold at `(a,b,c)=(-1,1/10,-1/2)`. In this chamber the ordered
levels and multiplicities at this momentum are

    2a-q (2), -a-r (4), 2a+q (2), -a+r (4).

Define the three distinct gaps above the lowest level:

    D1=-3a+q-r, D2=2q, D3=-3a+q+r.

Then

    a=(D2-D1-D3)/6,
    q=D2/2, r=(D3-D1)/2,
    v=-sqrt((r^2-3a^2)/2), u=q/sqrt(2),
    b=(u+2v)/3, c=(v-u)/3.                              (3)

Proof: sums and differences of the gaps recover a,q,r; the negative square
root fixes the declared v=b+c branch; solve u=b-2c and v=b+c. Substitution
recovers all three gaps. The inverse is smooth for b+c<0. Its forward
Jacobian is

    det d(D1,D2,D3)/d(a,b,c) = -72 sqrt(2)(b+c)/r.        (4)

Thus this is a genuine local inverse, not a parameter count. Away from the
chosen chamber there may be different labels or sign branches; no global
uniqueness claim is made. A scalar identity shift of H leaves gaps unchanged
and is outside the stated three-parameter family. Absolute creation energy
is not determined by this reconstruction.

## Finite response paths, including the kinetic response

Let two points remain in chamber (2) and have `D_j'=g D_j` for all j and g>0.
Every expression in (3) is positively homogeneous, so

    (a',b',c')=g(a,b,c),   H(k;a',b',c')=g H(k;a,b,c)     (5)

at every momentum. Conversely (5) scales all gaps by g and preserves (2).
This is a finite-path statement, stronger than a first-order null vector.
Any differentiable selected band, or its smooth degenerate effective matrix,
has curvature tensor `K'=g K` at its corresponding stationary momentum.
Positive scaling preserves stationary points and their ordering. This note
does not need or prove uniqueness of the global minimum; the reference
curvature is numerically positive and isotropic.

A gap is a band splitting, not automatically a clock transition or a particle
rest mass. To test a conformal interpretation one must additionally identify
these gaps with internal matter energy differences, identify translational
curvature with inverse inertial mass, and specify clock/ruler standards.
For universal conformal factor A with fixed reference standards, the
nonrelativistic expansion of a relativistic energy gives

    E(p)=A m + p^2/(2 A m)+..., Delta_j'=A Delta_j,
    K_phys'=K_phys/A.                                   (6)

Equation (6) is a conditional comparator. The supplied band model has not
been shown to be relativistic, nor are its splittings identified with
observed species. Accordingly the following is a consistency target, not an
exclusion of that model or of extended fermions.

Let L be the ratio of effective physical cell lengths and U the ratio of
physical tick durations, using a fixed external reference. With hbar fixed,
(5) gives

    Delta_phys'/Delta_phys=g/U,
    K_phys'/K_phys=g L^2/U.

If (6) is required, then necessarily and sufficiently for these two scaling
relations

    A=g/U,    L=U/g=1/A.                                (7)

Indeed the whole dispersion then has the identity
`E_phys'(p)=A E_phys(p/A)` under the same momentum-origin convention.
This identity preserves any original nonrelativistic or anisotropic shape;
it does not create Lorentz invariance. At fixed fine spacing and tick,
L=U=1, the computed changes are instead gap g and reciprocal-curvature
inertial parameter 1/g. A varying effective L is a physical metric/response
hypothesis, not a change of the number of qubits per site, and must not be
introduced as a state-dependent unit convention to manufacture agreement.
The approved fixed scale conversion and kinetic-form isotropy primitive do
not supply a microscopic state-dependent L or U for this model.

## Numerical and adversarial evidence

At the reference point the gaps are
`(2.7335482028, 3.1112698372, 6.3777216344)` in model energy units.
The trace-average curvature is approximately `0.04322337` in dimensionless
crystal momentum. The runner uses full Hessians at three step sizes,
40 seeded nearby parameter triples, finite positive scalings 0.7,1.3,2,
and a link-only perturbation that changes gap ratios. Those are development
controls, not independent empirical tests or certified floating-point bounds.

The exact determinant and inverse controls pass. Three intentionally wrong
algebraic alternatives (chiral sign in the determinant, onsite inverse
normalization, reciprocal curvature scaling) are detected. These are formula
controls, not a source-mutation campaign. The runner has 99 passing controls
in its initial recorded execution. Independent reconstruction of the matrix
and inverse is recorded in the loop pack; it also checked 100 spectra and
30 full-momentum scaling cases. Independent checks do not ratify physical
identifications.

An early exploratory calculation evaluated curvature at the other affine
fixed momentum and obtained negative curvature. Selecting the lower of the
two at the reference point fixed that labeling error; the failed probe is
preserved in the pack. No logarithm of negative curvature is used here.

## Relation to existing work and open test

Inverse tight-binding reconstruction and effective masses are established
methods; e.g. [D'Amico et al.](https://arxiv.org/abs/1608.05685) gives primary
context on tight-binding Hamiltonians and their derivatives (abstract
consulted only). No general novelty claim is made. The contribution here is
the explicit inverse (3) for this corner model and its finite-path coupling
test (7). Current-main search at `f389e89fe84e2584ee85047f08da88c1443eb163`
and frozen PR9671 source found the forward spectrum and embedding but not
this inverse calculation. The endpoint/readout PRs9672–9680 concern different
finite transfer constructions and are not dependencies.

The next useful physical test is to derive one slowly varying collective
lattice mode and compute its effects on (a,b,c), L and U from the same local
rule. Equations (3) and (7) then test that mode, rather than defining it to
pass. Source/detector spectral data, if those transitions can be physically
identified, would calibrate the local coefficients; independently reserved
kinetic or spatial response would test the bridge. No measured data were
opened, fitted, or used to select the reference parameters here.

## Premises and claim boundary

Supplied: the corner graph, flux sector, hopping family, sign/ordering
chamber and chosen reference point (inherited development point, not measured
calibration). Conditional comparator: universal conformal matter and
observable/metric identification. Mathematical tools: finite characteristic
polynomial, elementary inversion, homogeneous matrix scaling. No axiom or
primitive is added. No scalar dynamics, stable feature radius, environmental
boundary value, tensor gravitational coupling, or physical fermion is
established by this note. These remain research targets, not negative
obstruction theorems. No formal audit is performed.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: exact inverse within the supplied spectral chamber
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: finite matrix reconstruction and conditional response identities
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: null
target_blocker_text: derive source and detector coupling to a cosmological scalar
source_of_blocker_text: user_goal
artifact_role: theorem
next_trace_action: derive a collective mode and test its hopping, clock and ruler responses
```

## Reproduction

`python3 -B scripts/large_feature_spectral_response.py`

[Results](../outputs/large_feature_spectral_response/result.json).
The runner reads no external scientific files and writes only this result.
Its source contains the complete supplied model. Standard NumPy and SymPy
are needed; the audit timeout is 120 seconds.

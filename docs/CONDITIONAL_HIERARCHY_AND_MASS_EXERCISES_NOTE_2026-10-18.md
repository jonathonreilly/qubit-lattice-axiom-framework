# Conditional algebra for hierarchy and mass exercises

**Status:** bounded-support.
**Claim type:** bounded_theorem.
**Primary runner:** [scripts/conditional_hierarchy_mass_exercises_2026_10_18.py](../scripts/conditional_hierarchy_mass_exercises_2026_10_18.py)

This record retains mathematical results for explicitly supplied finite matrices,
representations, flows and noise channels. It does not identify their eigenvalues
with physical generations or derive a hierarchy of measured masses from the
framework axioms. The original exploratory comparisons and complete arguments
remain recoverable; the corrected statements below control wherever an earlier
report used stronger quantifiers. Historical referee labels and saved outputs
are not present-day evidence. Recalled masses, mixing angles, coupling values and
anomaly claims are comparators, not premise authority or independently validated
observations. No new primitive or audit verdict is introduced.

## First-exit scaling for a specified expanding coordinate

Suppose a supplied discrete flow has a positive transverse coordinate u and,
until its first exit from 0<u<rho, satisfies u_(n+1)>=lambda u_n, lambda>1.
For u_0=delta in (0,rho), let n_exit be the first index with u_n>=rho.
Then n_exit<=ceil(log(rho/delta)/log(lambda)), and in particular
n_exit<=log(rho/delta)/log(lambda)+1. Indeed, if the orbit had not exited by
the ceiling index, induction would give u_n>=lambda^n delta>=rho, a
contradiction. The harmless +1 is essential when replacing the integer bound
by a real logarithm: u'=2u, delta=1/10, rho=1/4 exits at index 2.

If a separately supplied scale relation is xi<=b^(n_x+n_exit) xi_triv with
b>1 and fixed entry time n_x, then

    xi <= b^(n_x+1) xi_triv (rho/delta)^(log(b)/log(lambda)).

This is conditional on the actual expanding-coordinate and scale relation.
It is not a theorem excluding other critical flows, marginal directions,
nonlinear constraints, dynamics, or nonperturbative scale generation.

## Sign bound for supplied two-loop coefficients

For integer N>=2 and a supplied number n_f of fundamental Dirac flavors,
use b0=(11N-2n_f)/3 and
b1=34N²/3-(13N/3-1/N)n_f. Let B=8pi²/(15 log(10))<23/10.
If b0<=B, then n_f>=(11N-3B)/2; the coefficient multiplying n_f in b1 is
negative, so

    b1 <= -25N²/2+11/2+B(13N-3/N)/2
       < -25N²/2+(299/20)N+11/2
       <= -(201/20)N+11/2 <= -73/5 < 0.

The second line uses B<23/10 and drops the negative -3B/(2N) term; the
third uses N²>=2N. For example pi<22/7 and log(10)>23/10 establish the
stated bound on B. This proves a sign property of these coefficients for
all N in the stated domain, replacing the original finite N<=100 scan.
Any fixed point inferred from a truncated two-loop beta function remains a
truncated-flow result; no confinement or nonperturbative no-scale conclusion
is inferred.

## Endpoint timing in the mass-bracket identity

Take a single directed hopping block T from i to j and an on-site mass
matrix m beta. Assign the hop in H[N] the weight
w_N=t N_i+(1-t)N_j and the mass at i the weight m N_i.
The mass-linear ij block of [H[N],H[M]] is

    m [(N_i w_M-M_i w_N) beta T
       +(w_N M_j-w_M N_j) T beta]
      = m D [(1-t) beta T+t T beta],
    D=N_i M_j-M_i N_j.

Thus for {beta,T}=0 this convention gives mD(1-2t)beta T, zero at
endpoint-mean timing; for [beta,T]=0 it gives mD beta T, independent of t.
Reversing the convention for which endpoint receives t replaces t by 1-t.
The identity follows by multiplying the two block matrices, with no continuum
limit. The Wilson-type commuting term is a counterexample to a blanket mass
cancellation statement. It is present in the original source checks, despite
an earlier report calling that arm untested.

## Finite representation and nearest-neighbor operator identities

For the supplied scalar action on the period-two X-star at momenta pi e_i,
translations act as independent diagonal signs and cubic rotations permute the
three labels. The image consists of the 48 signed permutation matrices.
A matrix commuting with all diagonal signs is diagonal; commuting also with
all permutations makes it scalar. Its commutant is therefore one-dimensional.
The eight period-two corners split into Hamming-weight orbits of sizes
1,3,3,1. These are statements about this representation image. Finite
translation groups obtained modulo a period are quotients/images of Z³,
not finite translation subgroups of torsion-free Z³. Other internal actions,
states and momentum placements require their own construction.

For arbitrary matrix-valued nearest-neighbor symbol
H(k)=A+sum_j(T_j exp(ik_j)+T_j^dagger exp(-ik_j)), put
Gamma=0, R=(pi,pi,pi), X_i=pi e_i, M_i=R-X_i. Direct substitution gives

    H(X_i)+H(M_i)=H(Gamma)+H(R),
    H(X_i)-H(X_j)=2[partial_i²H(Gamma)-partial_j²H(Gamma)].

These are operator identities. They do not equate physical masses or establish
species, state, readout or kinetic bridges.

## Residual symmetries, invariant families and angular mass algebra

If Hermitian mass-squared matrices share a unitary residual with three distinct
one-dimensional eigenspaces, both are diagonal in that residual basis. For
nondegenerate masses their mixing matrix is a permutation up to phases.
Degenerate mass eigenspaces allow basis freedom and must be treated separately.
More generally, an unrestricted invariant Hermitian family allows arbitrary
real eigenvalues on inequivalent scalar blocks; symmetry alone fixes neither
their values nor a mass ratio. Additional nonlinear or dynamical conditions
are outside that statement.

Equivariance implies that an image inherits the stabilizer of its source
state; the converse fails. In particular independent residuals of two output
matrices need not be residuals of the pair-state. Applying Schur to a group
generated by both residuals requires those elements actually to leave the
state, or both matrices, invariant. This corrects the original joint-vacuum
inference without discarding the valid common-stabilizer result.

For real e=(x,y,-x-y), define the supplied real symmetric matrix

    M=m0 I+mJ(J-I)+mu1 diag(e)+mu2 Off(e),
    Off(e)_23=e1, Off(e)_13=e2, Off(e)_12=e3,

with symmetric opposite entries and zero diagonal. Its trace is 3m0 and

    tr(M²)=3m0²+6mJ²+(mu1²+2mu2²)|e|².

The only angular term in tr(M³) at fixed |e| is
3(mu1-mu2)²(mu1+2mu2)xyz. Consequently the characteristic polynomial is
angularly constant on the lines mu1=mu2 or mu1=-2mu2, for all real signatures.
For the separate fermion-energy function f(z)=-sqrt(S+z²), S>0,
f'''(z)=3Sz/(S+z²)^(5/2). The fixed-sign divided-difference argument for
angular monotonicity therefore uses a definite spectrum. Numerical complex
or indefinite samples do not extend that proof. Concavity of a fermionic
energy as an infimum of affine functions does not prevent a supplied bosonic
potential from stabilizing a total energy.

## A supplied truncated plaquette block

On the specific link register spanned by 1 and sqrt(3) U_ij, normalized Haar
orthogonality gives the compressed multiplication matrix
P U_ab P=|ab><0|/sqrt(3). The four-link oriented trace is
T=(1/9)sum_(a,c)|u_ac><w_ac|, where each u_ac and w_ac is a sum of three
orthogonal product basis vectors. The nine u vectors and nine w vectors are
mutually orthogonal within each family, have norm sqrt(3), and occupy
disjoint link-flux sectors. Thus T is nine orthogonal rank-one maps of
singular value 1/3, and (T+T^dagger)/6 has maximum eigenvalue 1/18.
This concerns this register and observable, not every encoding. A different
register or isolated gauge-invariant character truncation is a different
operator problem; its dimension estimates are not universal qubit bounds.

## Conditional suppression, symmetry and channel examples

For an explicitly assumed splitting Delta gamma(ell)=c exp(-y ell), y>0,
its integral over 0<=ell<=L is c(1-exp(-yL))/y. The absolute integral is at
most |c|/y. This is not evidence that every possible flavor-splitting operator
has y>0, nor that L or c has been derived.

A symmetry preserving a specified code, perturbation class and the mapping
between two labeled logical transitions bijects the allowed perturbative
words. Their minimal nonzero order is equal when coefficients/denominators
also transform covariantly. This is a conditional word-counting statement,
not an identification of record permanence with quantum-code distance or a
catalogue of every native code. Equal distances alone need not fix unequal
coefficient sums when the operator family lacks that covariance.

A Pauli noise channel with Pauli-frame recovery remains diagonal in the
logical Pauli basis and has real eigenvalues. Near identity, positive
eigenvalues have zero phase; a negative real eigenvalue instead has phase pi.
Decay and a coherent mass identification are separate questions. Relative
entropy contraction for a channel with an invariant reference permits damped
rotations; it does not forbid spirals in arbitrary coupling coordinates.
General peripheral/recovery claims need their support and reversibility
hypotheses rather than a blanket assertion that every peripheral channel is
a unitary on the entire Hilbert space.

## Scope of the remaining complete exercise arguments

The accompanying mathematical-source collection preserves the supplied
localization, clockwork, finite tunneling, periodic XOR, integer-balance,
Poisson-dependence, finite representation, overlap and conditional channel
arguments, with a section-specific correction register. Transitivity fixes
a nondegenerate eigenvector's density or a spectral projector's diagonal,
not every vector in a degenerate flat band. The proposed all-width Gaussian overlap inequality remains a historical
finite diagnostic/conjecture, with only a suggested leading-order argument;
it is not promoted even as a theorem within the Gaussian family. Taylor singular-value orders require
nonzero jets and nondegenerate placements. An isolated slowest exponential
requires separation from the other rates and the p_max log N prefactor term in
its dominance estimate. The recorded equal-rate counterexample supersedes
the broader original claim. The finite-support classification
{1,2,4,8,infinity} for uniform backgrounds lacks a complete lower-bound proof
in the source layer argument and remains historical/unverified here. The
three slow-passage cases concern stated normal forms, not arbitrary beta
functions. The local Poisson covariance estimate needs the
stated independent clocks/marks, initial product data and finite dependence;
it is not an automatic theorem about every renormalization map.

Historical optimizer hits, finite-library maxima, saturation ranks, apparent
vacua, ensembles and recalled-data comparisons remain labeled exploratory
observations. In particular an absolute-Hessian stiffness surrogate is not
a local-minimum response; a grid minimum with parabolic interpolation is not
an exact global minimum; finite equivariant ranks through degree seven do
not prove an all-order classification. Singular values of a node-pair block
are not generally excitation gaps: tensor components can shift nodes or
produce nodal rings. The original comparator representation also lacks the
actual projective symmetry action in some variants. No mass census is
promoted from those singular-value scans. The span of degree-one and
-degree-three coefficients does not determine higher-order singular-value
orders: [[epsilon,epsilon^3],[epsilon^3,0]] has a smaller singular value of
order epsilon^5. The canonical runner checks that explicit distinction. No historical HIT becomes a new
physical claim. Terminal exclusions of all hierarchy/generation mechanisms,
all encodings, all RG routes or nonperturbative scales remain deferred, with
the missing carrier/state/dynamics/observable bridges listed as obligations.
The branch and exact originals must remain recoverable for that deferred work.

## Source and execution record

The primary enforces an aggregate 120-second deadline before numerical imports,
rejects optimized Python, streams every successful predicate and fails at the
first failed check. Its five printed resolution statements bound the actual
finite controls. It imports no archived exercise helper, reads no old result,
and generates no repository output. The owning fresh capture, when performed,
is separate from this source package; this authoring pass did not execute it.

The controlling corrections are in
`outputs/conditional_hierarchy_mass_review_2026_10_18/CORRECTION_REGISTER.md`.
Exact original recovery uses
`archive/conditional_hierarchy_mass_review_2026_10_18/manifest.json`.
The following complete argument sources remain live under those corrections:

- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H1/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H2/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/scale-ladder/H3/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/K/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/LEE/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R1/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R2/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R3/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/R4/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/T/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/hierarchy-models/T2/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/FP/derivations/generations-from-lattice-symmetry-2026-10-18.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/K/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R1/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R2/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R3/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R4/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/R5/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T3/REPORT.md`
- `outputs/conditional_hierarchy_mass_review_2026_10_18/mathematical_sources/mass-models/T4/REPORT.md`

# Focused independent check of compatible native cells

Completed 2026-09-30. This is a proof and finite-control check, not formal
milestone review, audit, retained status, an EOS theorem or a phase result.

The complete author REPORT (588 lines), SHA256
04e13444b4414477b450c6e5d5e760018993af00ef55d24724f58d4bf1d1736b,
and PERIODIC_CELL_BRIDGE (184 lines), SHA256
b99af6fadd993c672c1a624ee5d4863836a25b53bff2815b47940234a7de7f7e,
were read and checked against their actual premises. The main native operator
at30a9461ee19a49b99fa6628fe942f08e504e8903 has source hash
7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0.
Its positive identity, full-carrier isolation estimate, full15 threshold
definition and preceding Neumann/upper proofs were already independently
checked by root; the source bindings in the author packet match those inputs.
No new numerical threshold estimate is used here.

PRECOMPARISON.md, hash
a55c63f334cd23121ea7dcd98d1ff98c878e92d2024bb411c197e0c6430c1eb9,
was frozen before the new proofs were read. The disclosed author briefs had
already exposed the map, proposed gap/trial constants, Schur idea and boundary
counterexample. Root independently reconstructed the physical complement
argument, projected frame, finite Schur bounds and Husimi identity before
comparison. The controls below were written after reading the proofs; they
import no author code. Thus this is a focused independent reconstruction with
brief exposure, not an unexposed theorem search.

## Exact representation and guard cost

For every occupation, selected R-isolated graph edges are disjoint and unique.
Their endpoints together with the entire retained environment reconstruct the
occupation. Deleting a selected edge does not change any other isolation test:
all remaining particles were farther than R from both deleted sites. In
particular it cannot release a previously obstructed edge in the environment.
This proves the basis isometry and the annihilation intertwining. It proves
normal-ordered correlation identities, not physical CCR or a creation
intertwining. The author correctly takes number squares before compression.

For an actual removal output eta, the guard is exactly the indicator that
both removed sites are farther than R from eta. The row split (7) follows
from the squared triangle inequality and Cauchy. The actual nine-bond rows
have weighted incidence at most15:12 from gradients,2 for an axial singlet
or3 from the two plane-center families. Unequal guards lie in a distance
interval of length at most4. Every contributing small-radius isolated edge
uses two particles outside the larger-radius selected set. That factor two
cancels the row-split factor two. This gives the fixed-radius cost15 B_(R+4)
and the averaged cost60 B_(2r+4)/r. The stated C_R and C_g follow from the
actual isolation constant C_B=28000322. The improved r-squared estimate
requires a state-dependent radius choice; it is not a uniform operator bound
at every radius. All necessary small-radius and torus-size conditions hold
at the declared asymptotic scales.

The Neumann cell argument is valid for actual positive rows: mean-zero
variance is at most ell-squared/4 times the gradient form; the full S symbol
has norm at most2mu and its constant high component has energy2mu. Keeping
one-layer-interior centers gives the factor27 and then the stated17ell-squared
bound. It does not cut the occupation-dependent D term. Averaging translated
anchor cubes loses at most3ell/L of the selected count. Packing b-isolated
anchors gives M, and n>2M implies n<=2(n-n_b), yielding the B_b cutoff bound.
The auxiliary cap commutes with soft and nonsoft number. These arguments
allow a fluctuating total number and an extensive bad environment.

The positive-matrix gentle bound follows by decomposing a pure vector into
its P and (1-P) parts, then convexity and Cauchy. The two-body leakage is at
most2K times the nonsoft occupation. Summing gives exactly the claimed
2K sqrt(Nmean Exc), with the factor Nmean/2 from selected pair count.
This only controls uniformly bounded kernels in the explicitly normalized
coarse functional; it does not control an arbitrary microscopic contact
kernel with norm growing as ell-cubed.

## Full internal channels and normalization

The coherent-sphere moment identity can be derived directly by integrating
monomials against Haar measure and commuting two annihilators through two
creators. On ordered tensors its four one-body terms are precisely the
symmetrized gamma1 tensor identity contribution. The trace is
n(n-1)+2n(d+1)+d(d+1)=(n+d)(n+d+1). At d=5 the stated27n error is valid,
including n=2, and n=0,1 cause no issue for the lower bound. This elementary
check does not require importing a dilute-gas theorem or a literature premise.

In an orthonormal symmetric-matrix basis, the channel annihilator has the
required1/sqrt2. On z-to-the-n its amplitude is sqrt(n(n-1)/2), so the
physical coarse W_T has leading coefficient t_coh(T)rho-squared/8. The
number-cap/Jensen step occurs in the auxiliary state, where it is valid.
The error exponents at the declared r,ell,b,K are respectively13/16,1/8,
1/32,1/8; the more general two-body compression costs rho^(1/32). Volume
is taken first. No small fixed-particle limit with incompatible scales is
silently substituted. No polarization or condensation hypothesis enters.

## Actual finite periodic cell

Constant soft modes have a common uniform spatial factor even for arbitrary
internal entanglement. The probability that a given pair of anchors is too
close is at most(2R+9)^3/L^3. The union bound is therefore an operator Gram
bound on the entire Sym^n C5 space. Mutually isolated physical edges admit
no competing pairing, so the polar frame has rank binom(n+4,4).

For the compression gap, use the auxiliary projection P0 onto empty
environment and all n pairs in the constant soft modes. On the fixed physical
N=2n image,1-P0 is bounded by B_R+N_exc. The periodic first gradient
eigenvalue is at least16/L-squared. Decomposing into the constant mean and
mean-zero component proves N_exc<=L-squared J_guard. Hence
H_N>=Delta(1-I_R* P0 I_R). The pulled-back positive contraction has range
P, the actual polar-frame subspace, and is at most P. This proves the full
operator inequality H_N>=Delta Q, including cross terms. It is stronger
than simply guessing a gap for QH_NQ. For odd N, empty environment is
impossible and the simpler stated positive lower bound follows separately.

On the projected frame D vanishes identically. Every actual removal is
from one selected edge, since two different edges are farther apart than
the graph range. Fixing an admissible residual set leaves a constant U-valued
annihilation vector multiplied by its guard. Its residual squared norms
sum to at most n. Every unguarded constant row vanishes. The squared row
estimate therefore has no extra factor two. Shell anchors per orientation
are at most2|eta|[(2R+9)^3-(2R-7)^3], with |eta|=2(n-1) physical sites.
Weighted incidence15 gives60(n-1)s_R, and summing residuals gives B1.
Polar normalization divides by1-delta. The shell identity
s_R=48(2R+1)^2+1024 and all torus-size conditions are correct.

Min-max with H>=Delta Q and frame energy at most theta gives exactly
binom(n+4,4) levels below Delta when theta<Delta. Every vector in that low
band has Q probability at most theta/Delta. Fixed R and n<=K yield the
stated delta=O(rho^(13/16)) and theta/Delta=O(rho^(1/16)). This is an actual
finite periodic-cell statement; the cell size and constants are explicit.

The finite Schur completion is exact and positive. Writing C=QHQ,
B=QHV_n and A=V_n*HV_n, positivity gives B*C^-1 B<=A<=theta. Functional
calculus yields
0<=B*[(C-lambda)^-1-C^-1]B<=lambda theta/(Delta-lambda).
Inertia and eigenvalue monotonicity then give
lambda_j<=s_j<=[1+theta/(Delta-theta)]lambda_j,
including zero levels and degeneracies by continuity. This agrees with
the independently reconstructed multiplicative bound. No entries of the
finite Schur matrix, much less its threshold asymptotics, were evaluated.

## Actual counterexample and finite controls

For the actual N4 E1 incoming vector, a far axial removed edge has amplitude
1/sqrt2 in the stated normalization. For the residual axial edge at0,2e1,
its forbidden anchor region is exactly[-R-2,R+2] times[-R,R]^2. Direct
nearest-neighbor cut counting gives24R-squared+56R+22. Its contribution to
the guarded form is half that, with V distinct translated residual outputs.
The previously checked actual incoming energy is V(104mu+240tau). Thus the
claimed R-squared lower ratio is valid. Normalizing the incoming vector
cancels from the ratio. This rules out a radius-independent kinetic
intertwining constant for this guard, not the desired EOS or another method.

The independent standard-library runner checked1875 exact ordered complex
Husimi entries across n=2,3,5 using direct tensor partial traces and sphere
moments;12288 literal occupation encodings at R=14,17,20;14592 selected
removal identities;8940 cases with both selected edges and a nonempty bad
environment; and literal guard cuts at R=2,5,14,20. All assertions passed on
the first run. Actual cost4.238361 CPU seconds,4.245819 wall seconds and
32,899,072 bytes peak RSS, within the frozen30-second/150MiB price. Deadline
and STOP were checked. The author runners were neither read nor imported.
These finite controls supplement the proof; they do not prove the all-state
bounds or evaluate a many-body spectrum. The author's separate numerical
trial-frame results were read as author evidence, not independently rerun.

No error requiring a source correction was found. The remaining full-T0
many-pair expansion and the lower physical boundary/cell comparison are
separate, substantive missing lemmas. The coarse observable reduction,
periodic band and Schur operator do not imply either one. No current axiom
inconsistency, physical law selection, ODLRO or complete TOE follows.

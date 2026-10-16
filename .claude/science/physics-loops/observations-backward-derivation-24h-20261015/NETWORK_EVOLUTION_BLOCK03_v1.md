# Neighborhood orientation transport and the missing intermediate path

Author: /root, personally, 2026-10-16. Exploratory conditional mathematics.
Status: conditional-support; not a physical selector, empirical test, novelty
claim or formal audit result. Earlier network blocks remain separate.

## Observation and question

Interference can change after a cycle of intermediate orientations even when
the final orientation equals the initial one. Geometric phase is established
prior art, not a new prediction of this campaign. Berry's 1984 paper supplies
the historical reference (DOI 10.1098/rspa.1984.0023). Kwiat and Chiao's 1991
primary experiment reports polarization-cycle phase in heralded single-photon
interference (DOI 10.1103/PhysRevLett.66.588). Its publisher abstract was read;
no raw data or detector likelihood was opened or fitted here. These published
observations motivate retaining the intermediate route, rather than asserting
that endpoint labels exhaust the physical relation. They do not establish the
candidate dynamics below or replace quantum mechanics with a classical model.

Question: within a declared local orientation-transport class, do symmetry and
reversibility select the intermediate update? If they do, does that selection
survive dependence on a third neighbor? Work out both before interpreting a
phase as something merely hidden by incomplete knowledge.

## Explicit conditional class

Let a,b be oriented unit vectors in R^3, with b != -a; A=a.sigma and B=b.sigma
are Pauli matrices. D is the connected domain of these ordered non-antipodal
pairs. A candidate T(a,b) belongs to U(2), is continuous, and obeys:

1. T A T^dagger = B (oriented-axis transport).
2. It depends on this pair only, not a third neighbor, path history or time.
3. T(Ra,Rb)=S_R T(a,b) S_R^dagger for every proper rotation R, with S_R any
   spin lift. Its sign cancels in conjugation.
4. T(b,a)=T(a,b)^dagger as an equality of phase-sensitive matrices.
5. T(a,a)=I, including the phase.

These are supplied hypotheses. The Minimal Axioms' M2(C) algebra accommodates
these matrices but does not select a unitary transport law, continuous SO(3)
covariance, phase comparison, pair-only dependence, orientation labels,
preparation or cadence. Cubic spatial covariance alone is weaker than item 3.
Projective reversibility of channels is weaker than item 4. None of these
differences can be erased by calling T a local relation.

## Conditional uniqueness, without assuming determinant one

Define c=a.b and

    U0(a,b) = (I + B A) / sqrt(2(1+c)).

The Pauli relation gives BA=c I-i(a cross b).sigma. Thus U0 is a unitary with
positive trace and determinant one. Since (I+BA) A=B(I+BA), it transports A
to B. It is continuous on D, covariant, reciprocal and equal to I diagonally.

To prove uniqueness within the U(2) class, set K=U0^dagger T. Then K commutes
with A. Because A has simple eigenvalues, K=k_plus P_a+ + k_minus P_a-, with
|k_plus|=|k_minus|=1 and P_a±=(I±A)/2. Simultaneous SO(3) rotations have exactly
one orbit of ordered non-antipodal pairs for each c. Equivariance therefore
makes both eigenvalues functions of c only. In particular they are the same
for the reversed pair; reversal does not relabel the oriented plus eigenstate.

Transport by U0 maps P_a± to P_b±. Hence K(b,a)=U0 K(a,b) U0^dagger, and

    T(b,a)=U0^dagger K(b,a)=K(a,b) U0^dagger,
    T(a,b)^dagger=K(a,b)^dagger U0^dagger.

Exact reciprocity forces K=K^dagger, so k_plus and k_minus lie in {+1,-1}.
Continuity on the connected interval -1<c<=1 and K(a,a)=I force both to +1.
Thus T=U0. Determinant one follows within these hypotheses; it was not separately
postulated. The result is a conditional classification of already unitary
transport, not a derivation of unitary evolution or of a physical update law.

At an antipodal pair, rotations around a leave (a,-a) fixed. Equivariance would
force T to commute with A, contradicting T A T^dagger=-A. Thus no pair-only
SO(3)-equivariant unitary assignment exists there. The excluded point is a
genuine obstruction for this class, not removable just by changing a formula.

## What happens when an assumption is relaxed

Phase-blind reversal is insufficient. For any real continuous chi(c) with
chi(1)=0, exp(i chi(c)) U0 has the same axis transport, covariance and diagonal
identity. Its induced channel is exactly the U0 channel and is reciprocal.
Generally its matrices are not exactly reciprocal. The phase-sensitive clause
therefore selects information that an isolated M2(C) conjugation channel cannot
measure. A relative phase needs a coherent comparison path and a justified
composition/readout law; that is an additional physical bridge.

A third neighbor defeats pair-only uniqueness while keeping the other clauses.
Let n be another oriented unit vector, transformed along with a,b, and define

    tau(a,b,n)=a.(b cross n),
    T_kappa(a,b | n)=U0(a,b) exp[-i kappa tau(a,b,n) A/2].

For every real kappa this is continuous, unitary, simultaneously covariant,
axis-intertwining, and equal to I at a=b. Because tau(b,a,n)=-tau(a,b,n),
T_kappa(b,a|n)=T_kappa(a,b|n)^dagger when the same n is retained on reversal.
The last identity follows by transporting A to B, not by commuting all factors.
Kappa is an arbitrary new candidate parameter, not derived. More generally an
antisymmetric SO(3)-invariant twist depending on the full neighborhood remains
available. Nearest-neighbor locality does not imply pair-only dependence.

This is the decisive limit of the uniqueness result: restricting the local
context selects the shortest-rotation connection, but allowing more of the
actual neighborhood restores a free law even with the same symmetry and exact
reversal. The counterfamily is useful for challenging a selector, not evidence
that nature uses a nonzero kappa.

## Exact loop and endpoint comparison

For z=(0,0,1), x=(1,0,0), y=(0,1,0), traverse z->x->y->z. In chronological
matrix order the product is

    L0 = U0(y,z) U0(x,y) U0(z,x)
       = diag(exp(-i*pi/4), exp(+i*pi/4)).

It returns the oriented z axis to itself but does not equal I. A z-plus spinor
therefore acquires phase -pi/4 relative to a comparison path with identity
transport. With the third neighbor fixed to n=z, only the middle edge has
tau=1. Axis transport moves the inserted twist back to the starting z axis,
giving

    L_kappa = diag(exp[-i(pi/4+kappa/2)], exp[+i(pi/4+kappa/2)]).

Thus a closed endpoint relation can conceal both intermediate geometry and
neighborhood-dependent transport. These phases are meaningful only within the
declared coherent amplitude-comparison class. Taking the norm of either final
spinor alone does not observe them. An ideal balanced comparison junction would
have flux fraction (1+cos(pi/4+kappa/2))/2, but identifying that fraction with
event probabilities or count frequencies requires the unresolved detector law
in block02. It is not independently derived here.

Reversing every edge in reversed order, holding the same n, gives L_kappa^dagger
and cancels the forward loop exactly. A network with drifting n need not obey
that echo relation; such drift is a different protocol, not a reciprocity
violation of the fixed-context candidate.

For contrast, on the chart a,b != -z choose F(a)=U0(z,a) and
T_flat(a,b)=F(b) F(a)^dagger. It transports axes, is reciprocal and gives identity
around every chart loop by telescoping. It selects a reference z and fails
full pair-only SO(3) covariance. Consequently endpoint composition can be
enforced by a different imported rule. The nontrivial loop is not a consequence
of axis transport and reversal alone.

## Causal and observational boundary

The orientation variables and their changing neighborhood roles can be inputs
to local sequential operations, with products retaining the route history.
No formed record is rewritten by this algebra. Permanently storing a classical
which-path label would introduce a further physical operation; it is not
equivalent to retaining a contextual orientation in the apparatus. Projecting
onto each intermediate spin state and calling the product unitary would be a
different, generally lossy process. The present calculation does not identify
those operations or derive their respective record statistics.

No field action, initial network state, energy scale, neighbor orientation
distribution, formation event, uncertainty rule, unitary hardware, nearest-
neighbor lattice realization, Lorentz limit or detector response is derived.
No scalar-gravity bridge is inferred. Existing framework induced SU(3) link
holonomy and conditional one-qubit walk results are adjacent prior surfaces;
their proof certificates are not premises of this independent 2x2 calculation.

The proposed next diagnostic holds the endpoints and coherent comparison fixed,
varies the intermediate orientation path, then changes only a calibrated third
context and applies a reversal echo. A pair-only U0 law predicts geometric-path
dependence and zero third-context effect; T_kappa predicts an extra twist.
But calling n an independently manipulable physical neighbor, separating its
ordinary dynamical phase, and calibrating a phase-sensitive reversal all remain
experimental design obligations. This is a research direction, not a prediction
already checked against data or a replacement explanation for superposition.

## Computation boundary and provenance

probe_orientation_transport_v1.py checks exact Pauli algebra on representative
axes, generic symbolic orbit representatives, the loop and twist identities,
and counterexamples to weakened premises. Numerical grids do not establish
global uniqueness; the proof above does. Synthetic controls are development
data. The note and runner hashes are recorded in its JSON output and execution
receipt, with real errors preserved if encountered.

Primary literature: https://doi.org/10.1098/rspa.1984.0023 and
https://doi.org/10.1103/PhysRevLett.66.588 . Geometric phase, spinor transport
and gauge freedom are prior art. No novelty search is claimed complete.

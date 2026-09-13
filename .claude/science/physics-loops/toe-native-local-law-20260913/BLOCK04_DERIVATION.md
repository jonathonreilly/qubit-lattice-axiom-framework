# Physical program calibration: conditional derivations

Written before the finite checks, 2026-09-13. This is a campaign research
checkpoint, not an independently reviewed result or axiom amendment.
Main revision b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf. The target contract is
in BLOCK04_GOAL.md. All channels, quantum program states, Born interpretation,
settings compilation and supplied apparatuses below are additional model
premises. A general M2 framework Record is not assumed to be a density matrix.

## 1. Exact permanence and nonorthogonal pure programs

Let a fixed CPTP processor act on data S and program P, with arbitrary output
data, classical result and environment. Suppose its returned program marginal
is exactly |p><p| for every data input whenever its input program is |p>.
One common Stinespring isometry V then has

    V(|psi>|p>) = |p> V_p|psi>.

Purity gives factorization, and linearity in psi makes V_p an isometry.
Preservation of inner products for two allowed programs gives

    <p|q> I = <p|q> V_p^* V_q.

If <p|q> is nonzero, V_p^*V_q=I, so
(V_p-V_q)^*(V_p-V_q)=0 and V_p=V_q. Their complete output channels, including
the outcome and arbitrary reference systems, coincide. Equality propagates
along the nonorthogonality graph. Thus the coherent programs |n>^tensor k,
for all directions n and any fixed finite k, cannot select distinct channels
while being returned exactly. Their graph is connected even though antipodal
pairs are orthogonal. This applies to approximate as well as sharp target
measurements: with exact return these programs select one common channel.

Distinct exact sharp observables already require orthogonal pure programs
without a return requirement, when a single fixed apparatus and fixed outcome
interpretation are used. A self-contained qubit proof uses its joint effect
0<=F<=I. If program p realizes P_n and q realizes P_m, then F fixes
|n,+>|p> and annihilates |m,->|q>. Their inner product vanishes. For n!=m,
<m,-|n,+> is nonzero, so <q|p>=0. For mixed exact programs, extremality of a
sharp observable implies each pure component implements it; supports of
distinct programs are consequently orthogonal.

This second fact is established prior mathematics, not new TOE evidence:
Heinosaari and Tukiainen, *Notes on Deterministic Programming of Quantum
Observables and Channels*, Proposition 4,
https://arxiv.org/pdf/1412.0419v2 (statement and proof read); D'Ariano and
Perinotti, https://arxiv.org/pdf/quant-ph/0410169, equations (4)-(7).
Program-dependent external postprocessing would supply another setting source
and must be counted. Preservation of a selected mixed-state marginal, allowing
correlations, does not imply the pure-state theorem's factorization.
For example, a CNOT from a diagonal program diag(p,1-p) to a blank outcome
bit preserves that mixed program marginal while supplying an outcome whose
law depends on p. Its joint output is correlated. These overlapping mixed
programs are an explicit escape from the pure-state argument, but their
coin outputs are not arbitrary exact sharp measurements of the data.

An immediate quantitative warning follows without a new optimality theorem.
The labelled instruments for antipodal directions have diamond distance 2.
One program-independent channel within epsilon of both requires epsilon>=1
by the triangle inequality. This excludes arbitrarily accurate realization
from exactly returned connected pure quantum programs under these premises.
It does not exclude classical program banks or changed quantum programs.

## 2. Exact distance between labelled qubit Lüders instruments

For a unit vector n define P_n^a=(I+a n.sigma)/2 and

    L_n(rho) = sum_(a=+,-) |a><a| tensor P_n^a rho P_n^a.

The labels have the same meaning for both instruments. If theta is the angle
between n and m, put kappa=(1+n.m)/2=cos(theta/2)^2 and
s=sqrt(1-kappa^2). The proposed exact formula is

    ||L_n-L_m||_diamond = 2 sqrt(1-cos(theta/2)^4).       (D1)

Here is a proof independent of sampling or numerical optimization. Use the
unnormalized vectorization Choi convention. In flag block a the Choi difference
is D_a=|P_n^a>><<P_n^a|-|P_m^a>><<P_m^a|. Both vectors have norm one and
inner product kappa. For s>0 its nonzero eigenvalues are +s,-s, so
|D_a|=D_a^2/s. Direct multiplication and partial trace give

    Tr_output sum_a |D_a| = 2s I.

In obtaining this equality use sum_a(P_n^a+P_m^a)=2I and
sum_a(P_n^a P_m^a+P_m^a P_n^a)=2 kappa I; transpose the input matrices in the
chosen vectorization convention. The positive and negative Choi parts define
CP maps whose sum has adjoint identity 2s I. The complete trace norm of their
difference is at most 2s: equivalently use the CP-order diamond upper bound,
or a common Stinespring representation of their sum followed by the signed
environment observable of norm one. On a normalized maximally entangled input,
the output trace norm is (1/2) sum_a ||D_a||_1=2s. The limits s=0 and theta=pi
give 0 and 2. This is an instrument bound, including quantum backaction,
not only an outcome probability metric. Computational checks will challenge
the Choi square and partial-trace identities and the entangled lower witness.
The reduction of a Hermitian-preserving diamond norm to pure input states
with a data-sized reference is Theorem 3.51 in John Watrous, *The Theory of
Quantum Information*, https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf, printed
pages176-177; its statement and proof were read together with Lemma3.50.
This ordinary quantum-information theorem also justifies the optimization in
section4. It is an explicit mathematical import with its finite-dimensional
and Hermitian-preserving hypotheses satisfied, not a physics premise derived
from the lattice axioms.

## 3. Permanent finite classical banks: a useful but restricted escape

For K supplied directions m_j, orthogonal programs |j> permit one controlled
isometry sum_j |j><j| tensor W_j, where
W_j|psi>=sum_a |a>_C|a>_E P_mj^a|psi>. It returns each definite |j> exactly
and implements L_mj on all data/reference states. K=4 therefore fits two
program qubits for the four CHSH directions in the provisional benchmark.
This removes an alleged finite-setting programming obstruction, without
deriving program genesis, the event carrier, Born law or nearest-neighbor
compilation. It is already structurally covered by finite controlled-program
constructions on current main; no fresh milestone is claimed for it.

For a deterministic bank of K sharp directions and an externally supplied
nearest-setting compiler, (D1) gives error<=epsilon exactly when

    cos(theta) >= 2 sqrt(1-epsilon^2/4)-1.

For 0<epsilon<2, the corresponding spherical cap fraction is
a_epsilon=1-sqrt(1-epsilon^2/4). A covering needs

    K >= 1/a_epsilon ~ 8/epsilon^2.                       (D2)

This area lower bound is ONLY for this deterministic bank of sharp labelled
instruments. With q<=6 program qubits, D<=64 and K<=D imply that this bank's
worst-case error is at least 2 sqrt(2/D-1/D^2); at D=64 this is sqrt(127)/32.
Diamond norm is twice the operational trace-distance convention. General
quantum processors and randomized classical programs are outside (D2).
In particular, mixing nearby sharp bank settings can cancel first-order
direction errors; this note makes no optimality assertion for such mixtures.

A constructive sufficient bank comes from a maximal angular delta-separated
set. Its delta caps cover and its delta/2 caps have disjoint interiors, so
K<=2/[1-cos(delta/2)]. Compactness supplies a finite maximal set (greedy
packing terminates under this same area bound). Taking
delta=2 asin(epsilon/(2 sqrt(2))) ensures (D1)<=epsilon, and gives
K<=2/[1-sqrt(1-epsilon^2/8)]. This is O(epsilon^-2) with explicit, loose
constants. A bank may be padded to the next power of two.

For N events, arbitrary reference systems and adaptive controls that are
common to the exact and approximate protocols, the channel telescoping
identity and complete contractivity give a full-history diamond bound
sum_j epsilon_j. Choosing epsilon_j=epsilon_history/N and the above bank is
a sufficient q=2 log2(N/epsilon_history)+O(1) resource estimate. It is not a
necessary history-resource bound. Postselection probabilities are not
automatically controlled relatively when rare histories occur.

## 4. Consumable covariant reference: full instrument, not just its POVM

Take a supplied spin J=k/2 coherent reference |J,n>, realized in the symmetric
subspace of k program qubits. On data spin 1/2 and this irreducible space, use
the two total-spin projectors

    Pi_+ = [(J+1) I + J_vector.sigma]/(2J+1), Pi_-=I-Pi_+.

This is the construction in D'Ariano and Perinotti, equations (24)-(26).
It has a program dimension k+1 in its irreducible representation; physically
embedding it in k qubits uses a much larger ambient 2^k space. Restricting the
input to the symmetric subspace is an explicit preparation premise. The
processor is completed arbitrarily as a CPTP instrument on its orthogonal
complement. No selected nonsymmetric inputs are claimed to implement it.

To specify the backaction, choose joint Lüders readout of Pi_+,Pi_- and trace
out the program. Set alpha=1/(k+1), beta=sqrt(alpha(1-alpha)). At n=z the four
data Kraus operators, grouped by label, are

    K_+0=diag(1,alpha),  K_+1=beta |up><down|,
    K_-0=diag(0,1-alpha), K_-1=-beta |up><down|.          (D3)

They follow from Pi_+|up,J>=|up,J> and
Pi_+|down,J>=alpha |down,J>+beta |up,J-1>.
The POVM is E_+=P_up+alpha P_down, E_-=(1-alpha)P_down; its worst outcome
L1 error from the sharp measurement is 2alpha. That fact alone says nothing
about repeated postmeasurement states. The following candidate exact
instrument distance does:

    ||I_(k,n)-L_n||_diamond
       = [2alpha/(4-alpha^2)]
         [4-3alpha+2 sqrt(5-6alpha+2alpha^2)].            (D4)

Derivation: unitary covariance about z permits a diagonal input marginal
rho=diag(t,1-t) for diamond optimization. To justify this, the trace norm on
a purification of a marginal rho is concave in rho: purify a convex mixture
with an extra flag, and dephase that flag to get the convex average, which
cannot increase trace norm. Purifications with the same marginal are related
by reference isometries, so larger purifying spaces make no difference.
Average around z and use channel covariance. For this purification the
positive-label difference has a positive singleton beta^2(1-t) and the
two-by-two block

    [[0, alpha sqrt(t(1-t))],
     [alpha sqrt(t(1-t)), alpha^2(1-t)]].

The negative-label block has absolute trace (3alpha-2alpha^2)(1-t).
The complete output trace norm is therefore

    alpha [ (4-3alpha) u + sqrt(4u-(4-alpha^2)u^2) ],
    u=1-t, 0<=u<=1.                                    (D5)

Write B=4-alpha^2 and C=4-3alpha. Completing the ellipse gives the maximum
2alpha(C+sqrt(C^2+B))/B, attained at
u*=2[1+C/sqrt(C^2+B)]/B. For 0<alpha<=1, u* is in [0,1]: the function is
concave and its derivative at u=1 is -2(alpha-1)^2/alpha, with positive
derivative near u=0. Since C^2+B=4(5-6alpha+2alpha^2), this proves (D4).
It scales as (2+sqrt(5))/(k+1), and hence in particular is O(1/k), with
backaction and arbitrary reference inputs included. This is a derivation of
the particular joint Lüders implementation, not an optimality theorem for
all programmable instruments. The known measurement-only dimension bounds
in Perez-Garcia, https://arxiv.org/pdf/quant-ph/0602084, concern a different
metric and do not by themselves prove (D4) or a permanence-compatible bound.

This reference is not permanent. For data |down> its returned program after
discarding the outcome has population 2alpha(1-alpha) on |J,J-1>, and only
1-2alpha(1-alpha) on its original vector. For a general data state the loss
of overlap with |J,J> is 2alpha(1-alpha) rho_down,down. This is a literal
program disturbance, even though it becomes small with k. Reusing the same
reference without renewal is not justified by (D4), which assumes a fresh
coherent input at every use. It would require a separate correlated
sequential-instrument analysis.

## 5. What this changes, and what it does not

The actual physical-calibration question must distinguish permanent semantic
M2 contents, orthogonal classical programs and consumable quantum references.
The selected projective-history law does not yet provide this identification.
There is no axiom contradiction here: all restrictive channel/program
premises are additional, and finite settings and finite precision have live
constructions. A supplied apparatus direction, variable-time sequential
controller, larger spatial program, probabilistic success route or non-Hilbert
Record interpretation changes the premises and remains outside the negative
statement. Only the alternatives actually derived above receive conclusions.

The connected pure-program result and (D1)-(D5) are candidate author proofs.
The finite checker completed in1.290seconds with265 checks on2026-09-13;
the analytic proofs were cold-read after that run. The checker challenges
Choi partial traces, complex measurement directions, the ellipse optimum and
actual entangled witnesses, and independently reconstructs the spin apparatus
from literal symmetric-qubit input columns. Random samples are falsification
probes, not quantified proofs. No independent reviewer has checked the result.
The known no-programming theorem
and finite classical-bank construction do not warrant another standalone
science PR by themselves. A value decision after checking should determine
whether the new full-instrument estimates deserve later synthesis, or whether
the campaign should pivot to the reciprocal-source obstruction.

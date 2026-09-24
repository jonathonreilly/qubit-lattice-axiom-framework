# Coherent fuel for one actual star output: exact bounds and a restricted witness

Personal conditional calculation, 2026-09-24; independent reconstruction
pending. This note asks what an explicitly energy-conserving operation would
need to produce one of the actual star outputs already derived from the
original microscopic formation law. It does not replace that law, construct
its full instrument on arbitrary inputs, or derive its waiting-time process.

## 1. Inputs and relation to existing machinery

Use the lambda=0 compensated star, the exact zero-energy dressed input d, and
one normalized actual marked output phi from the star energy note. The full
microscopic Hamiltonian is H. Its output has two nonzero spectral weights:

`phi=sqrt(1-p) l + sqrt(p) h`,

`H l=0`, `H h=Omega h`, `<l,h>=0`,

`Omega=delta epsilon^-4(1+3epsilon²)`,

`p=c epsilon²/(1+3epsilon²)`, `c in {2,1,3/2}`.          (1)

Here l and h are the normalized low/high projections of phi; d is orthogonal
to both because it belongs to N=1 and they belong to N=3. The three c values
are respectively plus resolved, minus resolved and coherent edge marks. For
all epsilon>0 they obey 0<p<1. These are physical eigenvectors in the complete
Gauss sector, not an assumed field-only reduction.

Energy-preserving interactions with an energy-stationary environment induce
time-translation covariant operations. This standard connection is reviewed
in [Lostaglio, Korzekwa, Jennings and Rudolph, section III.A](https://arxiv.org/pdf/1410.4572).
The elementary argument below needs stationarity, not a thermal Gibbs state;
the specific star bounds and transfer matrix are derived explicitly here.
No catalytic reuse result is imported.

## 2. What an energy-stationary supply can reproduce

Suppose a proposed system/environment operation starts from dd* tensor eta,
where eta is stationary under H_R, and its unitary U commutes with the free
sum H+H_R. Assume also that the recorded outcome is read using an environment
effect commuting with H_R. The initial joint state is invariant under the joint
time translations. U and the outcome readout preserve that invariance. Taking
the partial trace then makes every nonzero normalized conditional system output
sigma stationary under H. This includes arbitrary energy degeneracies.

For every normalized stationary sigma, the sharp trace-norm bound is

`||phi phi* - sigma||_1 >= 2 sqrt(p(1-p))`.              (2)

To prove it, use `X=|l><h|+|h><l|`, which has norm one. Stationarity gives
`tr(X sigma)=0`, whereas `tr(X phi phi*)=2sqrt(p(1-p))`. Trace-norm duality
gives the lower bound. It is attained by

`sigma_*= (1-p)|l><l|+p|h><h|`,

since the difference has eigenvalues `+sqrt(p(1-p))` and its negative on
span(l,h), and zero elsewhere. The trace norm, not half that norm, is used
throughout this note. An arbitrary subnormalized stationary candidate for a
success branch of target probability q has distance at least
`2q sqrt(p(1-p))`, by the same witness X.

The result does not assume that energy supply is small. A stationary reservoir
can have enough mean energy and still lack the required phase relation. An
energy-noncommuting measurement, an external coherent drive, initial system
coherence, or a coherent environment changes the hypotheses and is not excluded.

For this star,

`2sqrt(p(1-p))=2sqrt(c)epsilon+O(epsilon³)`,

while `mean(H)=p Omega=c delta/epsilon²`. The stationary-output distance tends
to zero even while the energy requirement diverges. Thus (2) is an exact
finite-epsilon distinction, not an obstruction to reproducing the limiting
density with an O(epsilon) error.

## 3. A matching finite coherent-fuel witness

Introduce a two-level energy carrier with basis |0>,|1> and Hamiltonian
`H_R=Omega |1><1|`, prepared in

`beta=sqrt(1-p)|0>+sqrt(p)|1>`.

This is an explicit additional resource, not a derived reservoir state. Its
mean energy is p Omega, exactly the marked output mean. Its energy variance
also equals that of phi. Consider four mutually orthonormal joint vectors

`a0=d tensor |0>`, `b0=l tensor |0>`,
`a1=d tensor |1>`, `b1=h tensor |0>`.

The first pair has total free energy zero; the second has total free energy
Omega. Define U to swap a0 with b0 and a1 with b1, and to be the identity on
the orthogonal complement. Explicitly,

`U=I-sum_(i=0,1)(|ai><ai|+|bi><bi|)`
`     +sum_(i=0,1)(|ai><bi|+|bi><ai|)`.                   (3)

The swapped pairs are complete orthogonal eigenvectors of H+H_R, so
`U*=U`, `U²=I`, and `[U,H+H_R]=0` on the entire joint Hilbert space.
It produces exactly

`U(d tensor beta)=phi tensor |0>`.                     (4)

The carrier ends in its zero-energy state. Conservation and H_R>=0 require
initial mean energy at least p Omega for any deterministic transfer from d
to this phi; this witness attains that mean-energy bound. It consumes the
prepared coherent fuel. It is not a catalytic or repeatable source.

If beta is replaced by its energy-dephased mixture, the same U produces
sigma_* tensor |0><0|. That carrier has the same initial energy distribution
and mean energy but a different phase resource. Equation (2) is attained in
this concrete energy-preserving comparison. This distinguishes energy supply
from coherence without asserting that either is free.

The construction uses the physical system's full low/high output vectors. It
can be embedded as the identity outside their span and d, so it is not merely
a six-state calculation inconsistent with the remaining star states. All
system vectors remain within the fixed physical Gauss/total-charge sector.
No locality, coupling-strength bound or natural implementation is inferred
from the spectral definition of U.

## 4. A precise coherence resource inequality

For finite-dimensional energy carriers define energy dephasing Delta_R by
spectral pinching, retaining coherence within degenerate energies, and let
`C_R(eta)=||eta-Delta_R(eta)||_1`. The analogous system quantity uses H.
Starting from stationary d, an energy-preserving joint unitary followed by
partial trace defines a covariant channel from the carrier to the system.
It intertwines the two energy dephasings. Trace-norm contraction therefore gives

`||rho_out-Delta_H(rho_out)||_1 <= C_R(eta)`.

For a deterministic output phi this requires

`C_R(eta) >= 2sqrt(p(1-p))`.                            (5)

The two-level beta attains equality. A complete covariant outcome instrument
with a zero-energy classical flag gives the weighted inequality
`sum_j q_j C_H(rho_j) <= C_R(eta)`; it follows by applying the same argument
to the flagged channel and adding the trace norms of its orthogonal flag
blocks. A single specified success branch thus contributes at least q times
the right-hand side of (2). These inequalities concern the stated finite-
dimensional dephasing maps. No continuous-spectrum time-average limit is
silently assumed.

A classical selector can choose among the three or six star marks and their
corresponding fuel states with the already derived conditional mark weights.
A controlled version of (3) then reproduces the normalized first-event output
ensemble for this particular preparation, with mean supplied energy
`3delta/(2epsilon²)`. The selector is zero-energy and its outcome can be read
without supplying an additional energy phase. Its fuel preparation remains
an explicit correlated ensemble, and its timing is not specified.

## 5. What this witness does and does not settle

The source inequalities admit an explicit finite-resource transfer for each
fixed epsilon, with resources growing as epsilon tends to zero. The required
fuel gap scales as epsilon^-4, its excited probability as epsilon², its mean
energy as epsilon^-2, and the trace-norm coherence in (5) as epsilon. A claim
that all energy-conserving accounts are impossible would be contradicted by
this restricted witness.

This is fixed-input state preparation matching an actual documented conditional
output. It is not a dilation of the complete original linear jump map on
arbitrary system inputs. It does not generate the Poisson waiting law, the
no-event dynamics, irreversible record formation, reservoir replenishment,
repeated births, or a spatially local common matter/field law. Calling (3) an
energy-preserving operation does not establish all those autonomous dynamics.
The clock and prepared fuel remain physical obligations. No new primitive is
adopted, no native selection is derived, and no TOE or audit status is claimed.

The companion exact control checks the complete six-dimensional transfer,
commutation with total free energy, fuel/output means, the dephased comparison,
and its physical star embedding for all three mark types at three rational
epsilon values. The analytic projection and swap argument establishes the
all-epsilon result. The control uses the pinned root star matrices only for
embedding checks and is author consistency evidence. A wrong transfer that
leaves the excited carrier occupied violates the conservation check.

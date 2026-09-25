# Actual ground-state heating and the required energy source

Personally derived conditional candidate, 25 September 2026. This composes
the sealed but not yet independently checked root37 microscopic theorem
with the existing exact number balance. It is NOT an independent proof of
root37. No new interaction, bath, axiom, or physical identification is adopted.

The proposed physical identification being tested is that an energetic
minimum of the supplied full matter/field Hamiltonian is a persistent vacuum
under that SAME original formation law. The test uses the actual microscopic
Hamiltonian mean above its own minimum, rather than a selected-jump mean,
an effective energy proxy, or a field-only postbirth approximation.

## 1. Exact premises and the provisional imported estimate

Use the full original compensated spin model on an even degree-six cubic
torus of side L>=6. Set n=L^3/2. Keep K, delta, kappa positive, at a fixed
K/delta sufficiently small for the explicitly imported common-law bound.
Then let S tend to infinity with

    C=S(S+1),  epsilon^2 C=delta/K,
    H_S=delta epsilon^-4(W+epsilon T_S+epsilon^2 C_S),
    L_(j,S)=sqrt(kappa) epsilon^-1 j_S.

The entire compensation bracket remains vacancy gated. All physical charges,
electric fields, and resolved signs or the specified unnormalized coherent
instrument are retained. Denote Gamma_S=sum_j L_(j,S)*L_(j,S) and

    E0_S=min spectrum H_S,
    e_*=inf spectrum h_rotor.

Finite-spin physical spaces are finite dimensional. Root37 provisionally
establishes E0_S->e_* and, for every fixed upper energy cap Ecap, a remainder
r_S(Ecap)>=0 tending to zero such that EVERY microscopic density with
Tr H_S rho<=Ecap obeys

    Tr Gamma_S rho >= (16/5) kappa n
          -(4 kappa/(5 delta))(Tr H_S rho-e_*)-r_S(Ecap).     (1)

Its uniformity over energy-capped states is essential. Fixed-time weak
convergence of energy distributions would not supply (1). The common-law
energy/activity estimate and its half-filling trial are upstream dependencies,
not independent conclusions of this note. The order of limits is fixed L,
fixed small K/delta, then spin resource. No volume-uniform threshold is assumed.

On the full charge space the original operators satisfy exactly

    [N,H_S]=0,  [N,L_(j,S)]=2 L_(j,S),
    d Tr N rho(t)/dt=2 Tr Gamma_S rho(t).                    (2)

Total Gauss charge is sum_x q_x=n, and n_x=|q_x| for the hard-core local
charges. Hence N>=n. Occupancy gives N<=2n. These bounds hold outside P
as well. Because n is even on these tori, the upper bound is compatible
with the total-charge parity; the proof needs only the upper bound.
Integrating (2), for every initial microscopic density and every T>=0,

    integral_0^T Tr Gamma_S rho(t) dt
       =(Tr N rho(T)-Tr N rho(0))/2
       <=(2n-Tr N rho(0))/2 <=n/2.                         (3)

Equation (3) is exact at each S for the full original dynamics, including
all quantum coherences. It is not a count-rate approximation.

## 2. Total residence time near the actual microscopic minimum

Fix alpha with 0<alpha<4, and define the excitation-energy region along an
arbitrary actual trajectory by

    A_(S,alpha)={t>=0: Tr H_S rho(t)-E0_S <= alpha delta n}.

Since E0_S->e_*, all states in this region have a common upper energy cap
for sufficiently large S, for example Ecap=e_*+(alpha+1)delta n. Put

    eta_S=r_S(Ecap)+(4 kappa/(5 delta)) |E0_S-e_*|,
    gamma_(S,alpha)=(4 kappa n/5)(4-alpha)-eta_S.             (4)

Then eta_S->0 and gamma_(S,alpha)>0 eventually. Applying (1) to each
state in A_(S,alpha) gives Tr Gamma_S rho(t)>=gamma_(S,alpha).
Outside the region, Gamma_S remains nonnegative. Integrating this
pointwise inequality and using (3) proves

    |A_(S,alpha) intersect [0,T]|
       <=(2n-Tr N rho(0))/(2 gamma_(S,alpha)),              (5)

where |.| is Lebesgue time measure. Letting T increase gives the SAME bound
on total residence time over the entire infinite future, including any
number of returns. All functions are continuous at finite S; there is no
measurability or domain issue. No assumption that energy is monotone is used.

In particular, uniformly over arbitrary initial-state families,

    limsup_(S->infinity) |A_(S,alpha)|
       <= 5/[8 kappa (4-alpha)].                          (6)

The sharper numerator in (5) uses the actual initial expected N. The
uniform-time conclusion comes from an exact balance plus a state-uniform
inequality. We have not extrapolated a fixed-time approximation to infinity.
There is still no quantitative resource threshold: r_S is an asymptotic
remainder with fixed-graph constants from root37.

## 3. A full mean-energy gain from any ground-state input

Now take ANY initial density supported on the ground eigenspace of H_S,
including mixtures of number sectors and coherences inside a degeneracy.
Its initial mean is exactly E0_S. Define the first hitting time

    T_(S,alpha)=inf{t>=0: Tr H_S rho(t)-E0_S >= alpha delta n}.

Before this time the trajectory is in A_(S,alpha). If the time were infinite,
(5) would be contradicted. Thus it is finite for sufficiently large S and

    T_(S,alpha) <= (2n-Tr N rho(0))/(2 gamma_(S,alpha)),
    limsup_(S->infinity) T_(S,alpha)
       <= 5/[8 kappa (4-alpha)].                          (7)

Continuity implies that the full system mean energy gain at the first
hitting time is alpha delta n. For the useful concrete choice alpha=2,

    full mean-energy gain = 2 delta n,
    limsup first hitting time <= 5/(16 kappa).             (8)

These statements concern the actual H_S and actual rho(t), not a rotor
proxy or a postselected output. Every ground input is covered, so no
nondegeneracy assumption or explicit many-body ground vector is needed.
This does NOT assert a positive instantaneous energy derivative at t=0:
successive jumps may initially move within a degenerate ground space.
It also does not give a monotone energy curve, a final equilibrium, an
individual trajectory's energy measurement, or a temperature.

The n in (8) is the number of A sites in a fixed finite graph. It is not
yet a measured volume. The supplied delta and kappa are not calibrated
joules and seconds. A physical interpretation of a persistent energetic
vacuum must confront (7) after those identifications and finite-resource
errors are justified; the present statement alone is not an experimental
exclusion or an observed heating prediction.

## 4. What an energy-conserving implementation would have to supply

The positive difference in (8) is a system internal-energy gain for the
supplied Hamiltonian. The generator itself does not specify a reservoir
ledger, so calling it heat, work, absorbed light, or energy created from
nothing would add an unsupported interpretation.

A precise compatibility test can nevertheless be made. Suppose a proposed
implementation has an additional semibounded Hamiltonian H_R, and the
initial and readout energies are the additive H_S+H_R, with no omitted
interaction energy or externally supplied work between those endpoints.
If its total evolution conserves that additive total energy, then

    Delta <H_R> = -Delta <H_S>.                            (9)

Consequently an implementation reproducing (8) must provide at least
2 delta n of reservoir/other-system excitation energy above its lower bound
by that time. Interaction energy or externally supplied work could instead
account for it, but must then be included in the ledger. No implementation
has been constructed by writing (9).

In particular a system ground input and an environment also supported on
its ground subspace cannot reproduce (8) through an exactly energy-conserving
channel for H_S+H_R. Indeed

    H_S-E0_S >=0,  H_R-E0_R >=0.

The initial total excitation mean is zero. Conservation and positivity force
both excitation means to remain zero. Equivalently, a unitary commuting with
H_S+H_R leaves the total ground subspace invariant. Such a channel preserves
the system ground subspace, contradicting (7)-(8).

This is a test of a ZERO-EXCITATION environment with the stated endpoint
energy accounting. Passivity alone is not sufficient: a finite-temperature
passive reservoir has energy that can heat a ground-state system. A prepared
excited reservoir, externally driven apparatus, stored interaction energy,
or another justified state-selection mechanism is not excluded. None is
introduced as a new primitive here.

## 5. Verification and claim boundary

This is an analytic composition. No new numerical experiment or independent
confirmation is claimed. Source identities bind the existing exact number
balance and the root37 candidate. The algebra is displayed so that the
state-uniform remainder, capacity factor two, ground-energy reference, and
order of quantifiers can be reconstructed separately. The root37 microscopic
controls do not numerically establish (6)-(8) on cubic tori.

N1: the tested route is an energetic ground-state vacuum under the unchanged
original birth-only generator. Other physical preparations remain open.
N2: (1) is an explicit provisional import, not a second independent proof.
N3: fixed graph, positive couplings, small K/delta, charge background and
finite spin before the resource limit are load-bearing.
N4: the resource remainder is uniform on a chosen energy cap, not on volume,
couplings or every physical laboratory scaling.
N5: total occupation time is bounded; a pointwise relaxation or monotone
heating law is not inferred.
N6: actual microscopic mean energy gain is distinguished from heat/work and
from a selected detector mark's energy distribution.
N7: driven preparations, constrained sectors, dark stationary states and
reservoir energy remain live alternatives. The main already contains
unsaturated stationary states and homogeneous number balance; neither is
claimed as new here.
N8: physical scale, preparation, readout identification and error calibration
remain open. No observed fit, whole-framework no-go, retained audit verdict,
new axiom, or TOE completion follows.

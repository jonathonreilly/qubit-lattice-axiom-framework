# Finite-time star energy and a conditional supply bound

Personal extension, 2026-09-24; independent review pending. This note extends
the sealed exact-star construction. It keeps the supplied Hamiltonian and
original birth instrument. The conclusion is a quantitative energy requirement
under explicit conservation/positivity hypotheses, not a universal reservoir
no-go or an adoption of those hypotheses as new framework axioms.

## 1. Closed no-event calculation

Use the four-site physical star and its exact dressed zero-energy preparation
from `../microscopic_birth_energy_author/EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH.md`.
Let `|s>=(|1>+|2>+|3>)/sqrt(3)` and let epsilon, delta, kappa be positive.
The physical N=1 loss operator for either instrument is exactly

`sum_j j†j = 4 W`.

For a basis state with the old record on leaf b, either of the other two leaves
can form with either sign; their output words are distinct for a fixed mark.
There are no off-diagonal input matrix elements in this loss. In N=3 there is
no state with both the A vertex and a B leaf empty, so all microscopic formation
marks vanish there. There can be only one birth.

The no-event evolution preserves the span of A and s. In that orthonormal
basis its generator is

`G = -i H1 - (2 kappa/epsilon²) diag(0,1)`,

`H1 = delta [[3/epsilon², -sqrt(3)/epsilon³],`
`            [-sqrt(3)/epsilon³, 1/epsilon⁴]]`.

The initial column is `ell=(1,sqrt(3)epsilon)/sqrt(a)`, `a=1+3epsilon²`.
Write `v(t)=exp(tG)ell` and `P_b(t)=1-||v(t)||²`. This is exactly the
probability that a birth has occurred by time t, because no further birth is
possible and the GKLS trajectories exhaust the two number sectors.

## 2. Exact finite-time energy decomposition

Every possible jump time samples a no-event state `x(t)A+y(t)s`. Each resolved
mark annihilates its A component and selects the same two equal-amplitude old
record paths from s. Thus the normalized actual output for a fixed mark is
independent of jump time whenever that mark has nonzero density. The six
resolved marks have equal instantaneous probabilities. Their conditional
microscopic energies are the three values `2delta/epsilon²` and the three
values `delta/epsilon²` from the first note. The three coherent marks each have
energy `3delta/(2epsilon²)` and twice the resolved-mark intensity.

After a birth the N=3 state evolves unitarily under its fixed H3. Its energy is
therefore unchanged until the observation time, even though its density need
not be stationary. Summing the exact one-jump integral gives

`E_total(t) = E_no(t) + [3delta/(2epsilon²)] P_b(t)`,       (1)

`E_no(t) = <v(t), H1 v(t)> >= 0`.

The same identity holds for both instruments. It refers to the full microscopic
GKLS state, not an effective-energy derivative or a reset approximation. In
particular

`E_total(t) >= [3delta/(2epsilon²)] P_b(t)`               (2)

for every epsilon and t>=0. The initial total energy is exactly zero. The
positive no-event contribution is retained rather than discarded.

## 3. Fixed-time singular limit

The characteristic polynomial of G, after multiplying by epsilon⁴, is

`epsilon⁴ z² + [i delta(1+3epsilon²)+2kappa epsilon²] z`
`             + i6kappa delta = 0`.

With eta=epsilon², the root near `z=-6kappa` is analytic at eta=0: the derivative
of this polynomial with respect to z is `i delta`, which is nonzero there.
Direct coefficient comparison gives

`z_s=-6kappa + (18kappa-12i kappa²/delta)epsilon² + O(epsilon⁴)`.

The other root is the trace of G minus z_s and has imaginary part of order
`-delta epsilon^-4`. Both have nonpositive real part, because
`G+G†=-(4kappa/epsilon²)W` is negative semidefinite.

To check that a small coefficient multiplying this fast eigenvalue is actually
controlled, use the orthonormal low/high columns

`ell=(1,sqrt(3)epsilon)/sqrt(a)`,
`r=(sqrt(3)epsilon,-1)/sqrt(a)`.

In these coordinates G has diagonal entries
`-6kappa/a` and `-2kappa/(epsilon²a)-i delta a/epsilon⁴`, and both off-diagonal
entries are `2sqrt(3)kappa/(epsilon a)`. The slow eigenvector with low component
one has high component

`[z_s+6kappa/a]/[2sqrt(3)kappa/(epsilon a)]=O(epsilon³)`.

The fast eigenvector with high component one has low component O(epsilon³),
as follows from its first row. Their inverse change-of-basis matrix is bounded
for small epsilon. Decomposing the initial column (1,0) in this eigenbasis gives
fast coefficient O(epsilon³). Contractivity of the two scalar exponentials
therefore yields, uniformly on each fixed interval [0,T],

`<r,v(t)>=O_T(epsilon³)`,
`<ell,v(t)>=exp(-6kappa t)+O_T(epsilon²)`.

It follows that

`P_b(t)=1-exp(-12kappa t)+O_T(epsilon²)`,

`E_no(t)=[delta a/epsilon⁴]|<r,v(t)>|²=O_T(epsilon²)`.

Consequently, for each fixed t>0,

`epsilon² E_total(t) -> (3delta/2)[1-exp(-12kappa t)] > 0`.       (3)

This sharp result can also be checked against the parent's density/finite-count
limit for the birth probability, but the two-by-two derivation supplies its own
moment estimate. It is not a limit uniform in delta, kappa, t(S), or graph size.
Under `epsilon² S(S+1)=delta/K`, equation (3) is equivalently

`E_total(t)/[S(S+1)] -> (3K/2)[1-exp(-12kappa t)]`.

The rare high spectral component is thus present in a finite-time ensemble
with a strictly positive limiting birth probability. The effect is not confined
to an instantaneous derivative or a zero-probability conditioning event.

## 4. What energy conservation would require

Consider, as an additional proposed accounting construction, a system plus an
environment with nonnegative Hamiltonian H_R, initially in the dressed
zero-energy system state and an environment state of finite energy E_R(0).
Suppose a joint unitary U(t) preserves the free total energy H_system+H_R,
and its reduced system state reproduces the microscopic GKLS state at time t,
including the energy expectation. Then positivity and conservation give

`E_R(0) >= E_total(t) >= [3delta/(2epsilon²)] P_b(t)`.      (4)

This follows directly by taking the expectation of the conserved sum; no
Markov approximation or special reservoir spectrum is used in the inequality.
Under the joint scaling, its required initial supply grows at least linearly
in S(S+1) with the positive coefficient in (3). Resources allowed to grow in
this way are not excluded.

A slightly different explicit hypothesis permits an interaction energy:
`H_tot=H_system+H_R+V`, with H_R>=0, autonomous conservation of H_tot, and a
bounded self-adjoint interaction `||V||<=v_*`. The same initial preparation
then gives the weaker necessary condition

`E_R(0)+2v_* >= E_total(t)`.

This bound assumes the displayed decomposition and conservation; it does not
justify them for the supplied GKLS law. An interaction norm or reservoir supply
that itself diverges with epsilon can pay the bound. Shifting the system energy
by a large number-dependent term changes the energy model and must be analyzed
as a new supplied Hamiltonian. No such shift is silently made here.

Trace-distance reproduction alone is insufficient for (4). Small high-energy
populations can change energy moments while making a vanishing trace-distance
error, as this star explicitly demonstrates. A construction reproducing only
the limiting target density need not reproduce the energy bill above. A
modified microscopic instrument may also have a different bill; the present
note retains the original j throughout.

## 5. Controls, limits and open work

`star_finite_time_energy.py` verifies the complete loss matrix and the two-by-two
polynomial/rotation exactly. It compares (1) with direct evolution by the full
16-state, 256-dimensional superoperator in nine finite parameter/time cases;
the largest observed energy difference is recorded in the JSON, with tolerances
stated in code. This consistency control imports the pinned personal exact-star
builder and is not an independent reconstruction. A 70-digit two-by-two
calculation follows the integer-spin joint scaling through S=64. It illustrates
the proved limit; sampling alone would not prove (3).

The root has not constructed a reservoir, derived an external supply law,
selected a physical compensation or proved a general-graph coefficient. The
statements (1)–(4) concern this supplied positive star Hamiltonian and explicit
zero-energy preparation. The star has only one formation. The original cube,
repeated formation and volume questions retain their separate obligations.

# Independent PRE: energy coherence required for one actual star output

September 24, 2026 UTC. This is a bounded mathematical reconstruction using
only the previously checked compensated-star model. The sibling author packet,
campaign CHECKPOINT and external autonomous-reservoir material were not read.
The result is a conditional resource statement and an explicit fixed-input
construction; it is not an implementation of the full original instrument.

## 1. Exact input/output data and target

The prior independent packet supplies the complete physical star Hilbert
space, its positive Hamiltonian H, and the exact dressed initial state d.
For epsilon,delta>0 and every integer S>=1,

    Hd=0,   ||d||=1.

Fix one actual normalized resolved or coherent first-birth output phi.
Let a=1+3epsilon² and let

    E = delta epsilon^-4 a,
    p = m epsilon²/a,

where m=2 for a resolved plus mark, m=1 for a resolved minus mark, and
m=3/2 for a coherent edge mark. The full microscopic spectral projectors
give normalized vectors l and h such that

    H l=0,   H h=E h,
    phi=sqrt(1-p) l + sqrt(p) h.                       (1)

Here l,h belong to N=3, whereas d belongs to N=1; thus d,l,h are
orthonormal. For each finite epsilon>0, 0<p<1 and E>0. These vectors
are actual projections of the original jump output, not a replacement
of that output by its low-energy projection. Their microscopic moments are

    <H>_phi=pE=m delta/epsilon²,
    Var_phi(H)=p(1-p)E².                              (2)

The target question is whether one can obtain this particular normalized
state from d using a joint unitary preserving H+H_R. The initial preparation,
reservoir Hamiltonian/state and readout specified below are additional
accounting/construction assumptions, not consequences of the star law.

## 2. Stationary reservoirs and compatible readouts cannot supply this exact coherence

Let H_R be self-adjoint, and let omega_R be a normalized trace-class
reservoir state stationary under exp(-itH_R) for every real t. Let U be
a unitary commuting with exp[-it(H+H_R)] for every t. Take the input

    |d><d| tensor omega_R.

Let a selected reservoir-only readout have effect 0<=M<=I that commutes
with exp(-itH_R) for every t. Its unnormalized conditional system state is

    Gamma_M(omega_R)
      = tr_R[(I tensor M) U(|d><d| tensor omega_R) U*].  (3)

This effect formula is independent of the particular reservoir-only
measurement realization once its Kraus effects sum to M: partial-trace
cyclicity gives (3). The effect need not be a projector. Normalize (3)
only if its success probability r=tr Gamma_M(omega_R) is positive.

The joint input is invariant under the total free time evolution, and U
preserves that invariance. Conjugating (3) by exp(-itH), moving the
reservoir time evolution past M, and using invariance of partial trace
shows that Gamma_M(omega_R) is invariant under exp(-itH). Thus

    [rho_success,H]=0.                                (4)

This proof permits reservoir degeneracies, coherence within a degenerate
reservoir eigenspace, arbitrarily small nonzero r, and arbitrary
energy-conserving U. It does not assume a finite reservoir dimension or
nonnegative reservoir energy. Those are not premises of (4). A pure
system marginal d also leaves no initial-correlation loophole: positivity
forces any joint state with that pure marginal to have support only in
span(d) tensor H_R, and hence to factor as the displayed input.

Equation (1) has nonzero coherence between two different microscopic
energies. It therefore cannot equal a state satisfying (4).
An exact implementation of the full original marked instrument within
this stationary/compatible class would fail already on d. This does not
exclude implementations using other resource assumptions.

## 3. Exact sharp trace-norm approximation bound

Let rho_phi=|phi><phi|. Define the Hermitian witness

    X=|l><h|+|h><l|.

Its operator norm is one. For every normalized stationary sigma, including
states with arbitrary degeneracy-internal coherence or support outside
span(l,h), tr(X sigma)=0. In contrast,

    tr(X rho_phi)=2sqrt(p(1-p)).

Trace-norm duality therefore gives

    ||rho_phi-sigma||_1 >= 2sqrt(p(1-p)).               (5)

The block-dephased state

    sigma_*=(1-p)|l><l|+p|h><h|                        (6)

attains (5): rho_phi-sigma_* has eigenvalues
plus/minus sqrt(p(1-p)) and zero on the orthogonal complement. Thus

    min_([sigma,H]=0, sigma>=0, tr sigma=1)
      ||rho_phi-sigma||_1
        = 2epsilon sqrt(m[1+(3-m)epsilon²])/(1+3epsilon²). (7)

This is the unhalved trace norm; trace distance defined with a factor
one-half is half this value. The bound holds for every positive conditional
success probability; a rarer herald does not lower the normalized bound.

The minimum is physically attainable within the permitted stationary
class when the reservoir and U may be chosen: the stationary mixture
diag(1-p,p) in the two-level construction below produces (6). Thus
sharpness is not merely minimization over an inaccessible mathematical
set. A separately prescribed reservoir may of course have fewer
accessible stationary outputs.

Under epsilon² S(S+1)=delta/K, write C=S(S+1). Then

    p=m delta/(KC+3delta),
    minimum norm error
      =2sqrt(m delta[KC+(3-m)delta])/(KC+3delta)
      =2sqrt(m delta/K) C^-1/2+O(C^-3/2).              (8)

The exact finite-parameter obstruction therefore does not give a
positive limiting trace-error floor. A stationary construction can
approximate the desired conditional density increasingly well while
its microscopic energy remains large.

## 4. An explicit finite nonstationary reservoir supplies the exact output

Choose a two-level reservoir with orthonormal states |0>,|1> and

    H_R=E|1><1|,
    eta=sqrt(1-p)|0>+sqrt(p)|1>.                       (9)

The state eta is nonstationary for 0<p<1. In the full system/reservoir
space define four orthonormal vectors

    A=d tensor |0>,    B=l tensor |0>,
    C=d tensor |1>,    D=h tensor |0>.

A and B both have total energy zero. C and D both have total energy E.
Define the complete unitary

    U=I-|A-B><A-B|-|C-D><C-D|.                        (10)

It swaps A with B and C with D, and is the identity on their orthogonal
complement. Consequently U*=U, U²=I, and [U,H+H_R]=0 exactly. Its action is

    U(d tensor eta)=phi tensor |0>.                  (11)

The reservoir ends in its vacuum without residual system/reservoir
correlation. The energy-compatible readout M=I, or the final reservoir
vacuum projector, has success probability one. This is a finite
two-dimensional reservoir at each fixed epsilon, with a conserving
unitary on the full 32-dimensional star/reservoir space.

The resource accounting is explicit:

    initial reservoir mean = pE = m delta/epsilon²,
    initial reservoir variance = p(1-p)E²,
    final reservoir energy and variance = 0.

All free-total-energy moments are preserved: the reservoir's initial
energy probabilities 1-p,p are transferred to the system. The
off-diagonal entry of its initial energy density is sqrt(p(1-p)); its
trace-norm coherence between distinct energy eigenspaces is
2sqrt(p(1-p)), exactly that of the system output. The vacuum has no such
coherence. Replacing eta by the stationary mixture with the same energy
probabilities gives (6), with exactly the same energy moments as phi.
Energy moments alone therefore do not establish that the necessary
phase coherence has been supplied.

The state eta is an explicit resource premise. This construction does
not prepare it from stationary resources, restore it for repeated use,
or derive its phase from the record model. "Finite" here means finite
dimension and finite energies for fixed parameters. Along the joint
resource scaling,

    E=K²C²/delta+3KC,       <H_R>=mKC,

so neither the gap nor the mean energy is uniform in S.

## 5. Sharp heralded resource accounting

For a finite-dimensional reservoir define energy dephasing by its
distinct spectral projectors,

    Delta_R(omega)=sum_e Pi_e omega Pi_e,
    C_1(omega)=||omega-Delta_R(omega)||_1.

Degeneracy-internal coherence is retained by Delta_R. The same definition
applies to the finite star's H.

The map Gamma_M in (3) is completely positive and trace-nonincreasing.
Because d is stationary, energy conservation and compatibility of M give
the covariance identity

    Gamma_M(e^-itH_R omega e^itH_R)
      =e^-itH Gamma_M(omega) e^itH.

Taking finite-dimensional Cesaro time averages, which remove precisely
the distinct-energy off-diagonal blocks, gives
Gamma_M Delta_R=Delta_H Gamma_M. If Gamma_M(omega)=r rho_phi, then

    r C_1(rho_phi)
      =||Gamma_M(omega-Delta_R omega)||_1
      <=||omega-Delta_R omega||_1.                    (12)

The inequality follows from trace-norm contraction on Hermitian inputs:
write an input as its positive and negative parts, use positivity, and
bound each output trace by its input trace. Therefore any such exact
heralded preparation needs

    C_1(omega)>=2r sqrt(p(1-p)).                       (13)

If H_R>=0 and the initial mean energy is finite, conservation and H>=0
also give the necessary mean-energy bound

    E_R(0)>=r pE.                                    (14)

Indeed the unconditioned system state is the sum of the positive selected
branch and its positive complement. Its energy is at least r pE, while
conservation bounds its energy above by E_R(0). A conditional output
energy pE does not by itself imply an unconditional initial supply of
pE when r<1.

Both bounds are jointly sharp for this fixed-input task. Add a
zero-energy reservoir failure flag |f>, orthogonal to |0>,|1>, and use

    omega_r=r|eta><eta|+(1-r)|f><f|,
    H_R=E|1><1|,       0<r<=1.

Use (10) on the success subspace, the identity on the flag subspace,
and read out M=|0><0|+|1><1|. The selected branch is exactly r rho_phi,
the other branch is (1-r)|d><d|, and M commutes with H_R. The initial
reservoir mean is r pE and C_1 is 2r sqrt(p(1-p)), saturating both
(13) and (14).

Choosing r is a specification of a single heralded preparation. It
does not derive an original microscopic jump rate or waiting-time law.

## 6. Why the readout premise matters

A stationary reservoir can produce phi conditionally if the readout is
allowed to mix its energies. Start the same two-level reservoir in |1>.
Within the total-energy-E subspace a conserving unitary can map

    d tensor |1>
      -> sqrt(1-p) l tensor |1> + sqrt(p) h tensor |0>.

Such a unitary is explicit: swap the incoming vector with the normalized
right-hand vector and act as the identity on their orthogonal complement.
They are orthogonal because their system parts have different record
numbers and share the same total energy.

Project the reservoir onto |+>=(|0>+|1>)/sqrt(2). The unnormalized
conditional system density is rho_phi/2. This succeeds with probability
one-half, but |+><+| does not commute with H_R. It supplies a
phase-sensitive readout, outside the premises of (4), (12) and (13).
Thus stationarity of the initial reservoir alone would be insufficient.

## 7. Fixed-input preparation is not the original instrument or GKLS process

The conserving swap was tailored to the known input d and one specified
normalized output phi. Its other actions are not the original birth map.
For example, (10) maps l tensor |0> back to d tensor |0>, although every
original microscopic birth annihilates the N=3 state l. With the actual
resource eta, input l returns to the N=1 sector with probability 1-p.
This is an explicit failure of identifying the constructed unitary with
the original birth instrument on arbitrary inputs.

Nothing here implements all marks, the unnormalized jump operation for
general input states, the no-event operation, or the continuous event-time
law. In particular kappa cancels from each normalized target, and no
time parameter or clock is supplied by (10). The construction also
does not establish an autonomous generator for the original GKLS process.
Its positive result is exact single-output reachability with stated
energy/coherence resources for the fixed dressed input.

## 8. Proof status and independent control

All covariance, sharp-distance, resource and unitary claims above are
proved explicitly. The completed deterministic control uses exact SymPy
arithmetic. A generic three-state system support and two-/three-level
reservoir verify the conserving unitary, both sharp resource equalities,
the stationary minimizer, the dual witness and the incompatible-readout
escape. The full previously reconstructed 16-state star checks all six
resolved and all three coherent outputs at epsilon=1/2, delta=7/5,
including full 32-state unitarity/conservation and the reverse-input
failure of instrument identification.

Run 01 completed 139 checks without failure. Finite parameter samples
corroborate the all-parameter analytic construction; they are not its
proof. No existing new author code was imported or read. The reused
star engine and its final packet are hash pinned. The scoped alternative
route and N1–N8 review is in NO_GO_DISCIPLINE_CHECKLIST.md; no formal
landing-schema PASS or audit verdict is asserted.

# Independent PRE: apparatus energy coherence for one selected cube birth

Prepared before seeing any new root argument, root checkpoint or new checker
packet. Only the three allowed, unchanged model notes and the specified QFI
reference were used. Exact source pins are in `SOURCE_PINS.json`. This is
conditional mathematics for the supplied model and operational realization
class; it is not an audit verdict, native law, bath model or continuum-time
realization.

## 1. Target, convention and result

At each finite integer S let `epsilon^2 S(S+1)=delta/K`, with fixed positive
parameters and the supplied lambda=0 compensated cube Hamiltonian H. Let

    psi_e = U_e Omega,
    p_e = alpha^2 ||j_i psi_e||^2,
    phi_e = j_i psi_e/||j_i psi_e||,
    target selected output = p_e |phi_e><phi_e|.

Alpha>0 is a fixed admissible Kraus amplitude. It is not identified with an
exact continuum time step, jump duration or energy-supply rate. The target is
this selected subnormalized output on this one canonical zero-field input;
other outcomes are unrestricted. A construction below does not claim to
implement `alpha^2 j_i(.)j_i^*` on arbitrary inputs.

The realization starts with the product state
`|psi_e><psi_e| tensor rho_A`, where rho_A is arbitrary mixed. All auxiliary
phase references belong to A. Its unitary V exactly conserves the additive
energy, meaning

    V exp[-it(H tensor I+I tensor H_A)]
       = exp[-it(H tensor I+I tensor H_A)] V

for every real t. The outcome is read from a zero-energy flag by a readout
commuting with the apparatus energy. A purported additional noncovariant
readout would have to include its reference in A as well. The remaining
apparatus is discarded. No constraint is imposed on the final apparatus,
the other system outcome, locality of V or apparatus dimension/capacity.

Use the time-orbit SLD quantum Fisher information (QFI), in units hbar=1:

    F_H(rho)=2 sum_{a,b:lambda_a+lambda_b>0}
        (lambda_a-lambda_b)^2/(lambda_a+lambda_b) |H_ab|^2.

For finite-dimensional states this is well-defined, is invariant under
energy-conserving unitaries, is additive on independent systems with additive
Hamiltonians, is monotone under covariant channels, and equals `4 Var(H)`
for pure states. These basic identities agree with equation (2) and the
following properties paragraph of
[Marvian, arXiv:2112.04694v1](https://arxiv.org/pdf/2112.04694v1).
No iid conversion, clock-bit rate or periodicity theorem from that paper is
used. Sections 2 and 4 derive the operational inequalities needed here.

For an exact realization the necessary apparatus requirement is

    F_HA(rho_A) >= p_e F_H(phi_e)-F_H(psi_e).              (1)

The right side is positive for all sufficiently small epsilon. For the three
actual marks, with `(b_i,r_i,ell_i)=(2,4,2),(2,2,1),(4,6,3/2)`, it implies

    liminf epsilon^4 F_HA(rho_A)/(4 alpha^2 delta^2) >= r_i. (2)

The leading QFI lower coefficients are respectively
`16,8,24` times `alpha^2 delta^2 epsilon^(-4)`. A conservative swap
construction reaches the same leading coefficient. The conditional output
QFI alone scales as epsilon^(-6); omitting the success probability would give
a false stronger requirement.

For an entirely unrestricted mixed apparatus, a finite-time fidelity inequality
below is valid without finite moments or a differentiability assumption. It
implies the same bound for the lower Bures curvature of its energy orbit.
Whenever the usual energy-orbit QFI exists as that curvature, including the
finite-dimensional case and the extended value +infinity, (1)-(2) apply to
that QFI. This states explicitly how an apparatus outside ordinary SLD-domain
hypotheses is treated, rather than silently imposing finite apparatus variance.

## 2. Why the single-input target is enough for a QFI bound

Let the final system plus classical flag state at the given input be

    X = p_e |phi_e><phi_e| tensor |s><s|
          +(1-p_e) rho_f tensor |f><f|.

The joint processing of S+A into S+flag is covariant. In particular, rotating
*both* initial system and apparatus by their respective Hamiltonians rotates
X by H on the system and identity on the zero-energy flag. Its success
probability is unchanged. This follows from conservation and the covariant
readout; it does not require the simulation to match the original mark on
other system inputs with the apparatus held fixed.

For finite-dimensional QFI, the product input has total QFI
`F_H(psi_e)+F_HA(rho_A)`. Discarding the residual apparatus and making the
classical readout cannot increase QFI. Orthogonal flags with constant
probabilities give exactly

    F_(H tensor I)(X) = p_e F_H(phi_e)+(1-p_e)F_H(rho_f).

The nonnegative failure contribution can be dropped, giving (1).
The direct-sum identity follows immediately from the displayed spectral QFI
formula: inside a block of weight p both its numerator and denominator acquire
respectively p^2 and p; cross-block Hamiltonian matrix elements vanish.
Product additivity can also be checked directly, since a nonzero matrix element
of `H tensor I+I tensor H_A` changes only one product eigenindex at a time.

Here is a version valid for an arbitrary apparatus Hilbert space and mixed
state. Write root fidelity as `f(rho,sigma)=||sqrt(rho)sqrt(sigma)||_1` and

    f_A(t)=f(rho_A, exp(-itH_A)rho_A exp(itH_A)),
    f_psi(t)=|<psi_e,exp(-itH)psi_e>|,
    f_phi(t)=|<phi_e,exp(-itH)phi_e>|.

Product multiplicativity, unitary invariance and CPTP monotonicity of root
fidelity, followed by the orthogonal-flag direct sum, give

    f_psi(t) f_A(t)
       <= p_e f_phi(t)+(1-p_e) f(rho_f,rho_f(t))
       <= 1-p_e[1-f_phi(t)].                              (3)

Here the states are trace class and the Hamiltonians generate unitary groups.
Fidelity data processing follows from a Stinespring isometry and partial-trace
monotonicity in its purification variational characterization; it requires no
energy moment. The block-diagonal flag formula follows directly by taking the
square roots separately on the two orthogonal flag blocks.

For all sufficiently small t, `f_psi(t)>0`, so equivalently

    1-f_A(t) >=
       {p_e[1-f_phi(t)]-[1-f_psi(t)]}/f_psi(t).             (4)

This is an exact operational energy-coherence constraint without any apparatus
moment hypothesis. Each system is finite-dimensional at the fixed finite S,
and for a pure system state `1-f(t)=Var(H)t^2/2+o(t^2)`. Thus (4) implies

    8 liminf_{t->0} [1-f_A(t)]/t^2
          >= 4p_e Var_phi(H)-4Var_psi(H).                 (5)

The t->0 operation is performed at each fixed S before the spin asymptotics;
no derivative of a limiting density is substituted for a microscopic derivative.
A stationary apparatus has `f_A(t)=1`, so it cannot realize the exact target
for sufficiently small epsilon. Input independence and accounting for every
reference are essential: otherwise the product resource identity used here
would not describe the actual initial resource.

## 3. Microscopic input, success probability and output scales

The allowed actual-birth source gives the canonical output coordinates,
uniformly in S, in the Hermitian W clusters:

    (phi_e)_0 = beta_i+O(epsilon^2),
    (phi_e)_1 = epsilon R_i/sqrt(b_i)+O(epsilon^3),
    (phi_e)_2 = O(epsilon^2),
    D beta_i=0.

The supplied cluster expansion gives

    H_low = K D+delta H4_S+O(epsilon^2),
    H_r = delta epsilon^(-4)[r I+O(epsilon^2)], r=1,2.

The uniform leading canonical column is
`U_e Omega=Omega+epsilon F Omega+O(epsilon^2)`. Since the mark kills P,
and W parity makes its squared norm even in epsilon,

    p_e=alpha^2 epsilon^2 b_i+O(epsilon^4).                (6)

The grade-one part contributes
`delta^2 epsilon^(-6)ell_i+O(epsilon^(-4))` to the output second moment.
The grade-two contribution is O(epsilon^(-4)). The low energy vector is O(1):
`Q_S beta_i=0`, the low coordinate error is O(epsilon^2), and
`delta epsilon^(-2) Q_S` applied to that error is O(1).
Consequently

    <H>_phi = delta epsilon^(-2)ell_i+O(1),
    Var_phi(H) = delta^2 epsilon^(-6)ell_i+O(epsilon^(-4)). (7)

No ordinary positive-time result or unallowed new publication is used here;
these are the initial canonical cluster estimates in the pinned sources.

The canonical input is coherent, even though Omega has zero electric field.
It must not be treated as an energy eigenstate. On N=4,

    H4_S = -(M_S Q_S+Q_S M_S)/2-Z_S^*Z_S/2,
    M_S Omega=12 Omega,
    Q_S Omega=0.

Direct physical-word paths give

    H4_S Omega = -84 Omega-2 sum_{12 oriented cube faces} |face>,

with twelve mutually orthogonal nonzero circulation words. Every traversed
link in this computation is `0 <-> +/-1`, with unit actual normalized spin
amplitude for every S>=1. This is also consistent with the rotor formula in
the allowed local-compensation note. Therefore the canonical input has

    <H>_psi=-84 delta+O(epsilon^2),
    Var_psi(H)=48 delta^2+O(epsilon^2),
    F_H(psi_e)=192 delta^2+O(epsilon^2).                   (8)

The fresh primitive-word control reconstructs these values and the three B/R
norm pairs. Its source imports no campaign builder.

Combining (6)-(8),

    p_e F_H(phi_e)
       =4 alpha^2 delta^2 r_i epsilon^(-4)+O(epsilon^(-2)). (9)

Subtracting the finite input QFI in (1) proves (2). This is a requirement on
initial apparatus energy-orbit sensitivity per stipulated operation. It does
not give a resource consumption rate per laboratory time.

## 4. Approximation with an explicit growing-Hamiltonian bound

Suppose instead that the actual selected subnormalized output is sigma_e,
with q_e=Tr(sigma_e), and assume the unhalved trace-norm error

    ||sigma_e-p_e |phi_e><phi_e|||_1 <= eta_e.             (10)

Then `|q_e-p_e|<=eta_e`. Put
`M_e=inf_{c in R}||H-cI||`, using the Hamiltonian on the entire finite system
output space permitted to this approximate device. This centering makes the
bound independent of the energy zero. In the supplied fixed cube,
`M_e=O(epsilon^(-4))`.

For a finite-dimensional normalized state rho, its SLD L_sld obeys
`dot rho=(rho L_sld+L_sld rho)/2`. Cauchy-Schwarz applied to any Hermitian
observable of norm at most one gives

    ||[H,rho]||_1 <= sqrt(F_H(rho)).

For a pure target, writing `H phi=<H>phi+xi` with xi perpendicular to phi
shows exactly

    ||[H,|phi><phi|]||_1=2||xi||=sqrt(F_H(phi)).

The triangle inequality and (10) consequently yield

    ||[H,sigma_e]||_1
        >= [p_e sqrt(F_H(phi_e))-2M_e eta_e]_+.           (11)

If q_e>0, success-weighted monotonicity and homogeneity give

    F_HA(rho_A)+F_H(psi_e)
        >= q_e F_H(sigma_e/q_e)
        >= [p_e sqrt(F_H(phi_e))-2M_e eta_e]_+^2/q_e
        >= [p_e sqrt(F_H(phi_e))-2M_e eta_e]_+^2/(p_e+eta_e). (12)

The final lower bound remains valid for q_e=0: then eta_e>=p_e and its
positive-part numerator vanishes because `sqrt(F_H(phi_e))<=2M_e`.
For an apparatus not covered by ordinary SLD regularity, replace its QFI by
the lower Bures curvature from (5); the finite-system selected state in (12)
causes no derivative-domain problem.

Here `p_e sqrt(F_H(phi_e))` is of order epsilon^(-1), whereas
`M_e eta_e` is O(epsilon^(-4)eta_e). Thus

    eta_e=o(epsilon^3)

retains the complete leading lower bound (2). If the success probability is
matched exactly and the conditional state error is xi_e in unhalved trace
norm, eta_e=p_e xi_e; the sufficient condition is `xi_e=o(epsilon)`.
These are scale-sensitive statements. Merely eta_e->0, or merely conditional
trace error tending to zero without its rate, does not preserve the divergent
QFI requirement when the Hamiltonian grows.

Equation (12) retains finite error constants; it does not say every nonzero
constant times epsilon^3 eliminates the bound. Sufficiently small constants
can still force a positive fraction of the exact leading requirement. Section 6
shows that errors of order epsilon^3 can remove that requirement, establishing
the relevance of the exponent rather than an optimal cube constant.

## 5. Exact conservative realization: leading coherence cost, bounded mean

Let A contain an isomorphic copy of the whole finite system, with Hamiltonian
`H_A=H` on that copy, and a zero-energy binary flag. Choose a normalized
terminal N=8 state zeta; its energy is exactly zero. Prepare the mixed apparatus

    rho_A = p_e |phi_e><phi_e| tensor |s><s|
              +(1-p_e)|zeta><zeta| tensor |f><f|.          (13)

The system and this apparatus are initially independent. Swap the system
with the apparatus copy and read the flag. The swap commutes exactly with
`H tensor I+I tensor H_A`. Its selected system output is exactly
`p_e |phi_e><phi_e|`; the remaining branch is unrestricted as permitted.
All target coherence is already counted in the initial apparatus. No hidden
phase reference is invoked by this covariant unitary construction.

Since the flags are orthogonal and zeta is stationary,

    F_HA(rho_A)=p_e F_H(phi_e).                            (14)

This meets the necessary bound up to the bounded input QFI. In particular it
achieves the same leading coefficient in (2), for the single-input target.
It is an existence construction with an epsilon-dependent apparatus spectrum
and capacity, not a claim that an arbitrary fixed apparatus with this QFI is
sufficient or that the whole original instrument has been implemented.

Its initial apparatus mean and variance are

    <H_A>=p_e <H>_phi = alpha^2 delta r_i+O(epsilon^2),
    Var(H_A)=p_e Var_phi(H)+p_e(1-p_e)<H>_phi^2.           (15)

Thus its initial mean is O(1), while its variance is of order epsilon^(-4).
The finite graph's low Hamiltonian is bounded below uniformly along the
sequence, because KD>=0 and H4 is uniformly bounded; the high bands are positive
for sufficiently small epsilon. If a nonnegative apparatus Hamiltonian is
desired, a fixed O(1) scalar shift of the copy makes it nonnegative and leaves
the swap, QFI and variance unchanged. Its mean above its ground energy remains
O(1). Therefore **no divergent apparatus mean-energy requirement follows from
this single-output task**, even though the necessary QFI diverges. Constant
mean-energy requirements depending on spectral lower bounds and energy balance
are not excluded by that statement.

For any finite-variance mixed apparatus, the spectral QFI formula gives
`F_HA(rho_A)<=4 Var_rho_A(H_A)` after shifting H_A by its mean. Hence (1) also
forces a variance lower bound of leading order
`alpha^2 delta^2 r_i epsilon^(-4)`. The converse is false: a diagonal mixture
can have arbitrarily large energy variance and zero QFI. Variance alone does
not establish the energy coherence needed by (1).

## 6. A cube approximation of order epsilon^3 removes the divergent QFI cost

This sensitivity is not merely a weakness of the commutator estimate. Let P_r
be the exact Hermitian N=6 spectral clusters, r=0,1,2, and dephase only between
those clusters:

    Delta_band(|phi_e><phi_e|)
       = sum_r P_r |phi_e><phi_e| P_r.

Replace the success state in apparatus (13) by this mixed state, retaining
exactly the same success probability p_e, and perform the same conservative
swap. The selected output is now `p_e Delta_band(|phi_e><phi_e|)`.
The actual output's grade amplitudes in section 3 give

    ||p_e Delta_band(|phi_e><phi_e|)-p_e|phi_e><phi_e|||_1
       = 2 alpha^2 sqrt(b_i r_i) epsilon^3+O(epsilon^4).   (16)

The leading trace norm is the two singular values of the low/first-high
coherence; terms involving the second-high amplitude are O(epsilon^4) after
success weighting. Thus the probability is preserved and the conditional
state error still tends to zero, at order epsilon.

Yet the apparatus QFI in this construction is uniformly O(1). To see it
without assuming a finite-time limit, write `v_r=P_r phi_e` and use the exact
orthogonal-block QFI identity, with arbitrary energy centers c_r:

    p_e F_H(Delta_band(|phi_e><phi_e|))
       <=4p_e sum_r ||(H-c_r)v_r||^2.                    (17)

Take c_0=0, c_1=delta epsilon^(-4), c_2=2delta epsilon^(-4).
The low norm on the right is O(1), as already established at birth. The
first-high norm is O(epsilon^(-1)), since its amplitude is O(epsilon) and its
centered Hamiltonian has norm O(epsilon^(-2)). The second-high norm is O(1)
from its O(epsilon^2) amplitude. Multiplication by `p_e=O(epsilon^2)` proves
that (17) is O(1). No strengthened second-band cancellation, new ordinary-energy
note or external checker result is needed.

Dephasing between spectral bands preserves both `<H>` and `<H^2>` exactly.
Therefore this approximate apparatus has precisely the same initial mean and
energy variance as (13), including its divergent variance, while its QFI is
only O(1). This is a model-specific witness separating variance from energetic
coherence. It also shows why a bare vanishing trace-error condition cannot
justify the exact QFI lower scaling.

At a still coarser tolerance, the always-failure device has zero selected
output, error eta_e=p_e=O(epsilon^2), and needs no apparatus coherence at all.
Success probability must therefore remain visible in any approximation claim.

For additional perspective, even the exact apparatus (13) can approach an
energy-incoherent state in trace norm: full energy dephasing changes it by at
most 2p_e=O(epsilon^2). Its energy-weighted QFI can nevertheless diverge because
its energy scale grows. No divergent relative-entropy coherence, number of
clock bits, iid formation cost or fixed-bandwidth clock resource follows from
(2). The exact construction has growing energy gaps; it does not supply a
bounded-capacity device.

## 7. Controls, limitations and next decision

`coherence_checks.py` is written directly from primitive cube hops and contains
no imported campaign builder. It exactly reconstructs the N=4 H4 action,
its variance 48, the input QFI coefficient 192, the three B/R norm pairs, and
unit amplitudes of every involved finite-spin path.

A separate finite two-level construction in the same program has target high
population epsilon^2, gap epsilon^(-4) and success probability epsilon^2.
An explicitly built swap conserves the total additive Hamiltonian exactly.
The program checks the selected subnormalized outputs, QFI identities and
trace-error lower bounds at three epsilon values and four dephasing fractions.
In that example the initial mean is exactly one, variance is
`epsilon^(-4)-1`, and complete dephasing gives zero QFI with selected error
`2 epsilon^3 sqrt(1-epsilon^2)`. Partial dephasing saturates the commutator
bound when the actual success probability is used. It rejects omission of
the success weight. A separate identity-operation example rejects omission
of initial system coherence. Fixed mixed-state checks corroborate additivity,
`||[H,rho]||_1^2<=F_H(rho)` and `F_H(rho)<=4Var(H)`.

The finite matrix controls are numerical consistency checks, not interval
proofs. The uniform cube expansions come from the pinned analytic cluster
hypotheses, and the arbitrary-apparatus statement is the exact fidelity
argument. Full logs and result JSON are retained. No source, axiom, audit,
publication or editable prompt file was changed. This PRE supplies a necessary
and leading-order sharp QFI requirement for the declared exact target, a
quantitative robust version, and explicit limits on stronger interpretations.
It does not construct a full GKLS reservoir or an autonomous continuous process.

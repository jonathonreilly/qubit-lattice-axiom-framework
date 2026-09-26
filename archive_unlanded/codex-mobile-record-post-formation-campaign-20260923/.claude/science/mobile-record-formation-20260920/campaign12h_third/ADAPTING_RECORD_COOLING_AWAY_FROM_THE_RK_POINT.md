# Adapting record cooling when the field Hamiltonian changes

Status: personal conditional analysis, independent check pending. Sections 1
and 2 concern the specified finite spin-half model. Sections 3 onward are an
exact calculation in a separately supplied Gaussian model; no derivation of
that dissipator from the microscopic spin-half jump is asserted.

## 1. Why preparation and the photon-phase step are separate

The preceding local-cooling theorem prepares the equal-amplitude RK vector
u in a connected finite plaquette component. The repo's adjacent photon
phase uses an additional effective-phase input when the flippability
potential changes away from RK. Keeping the old cooling jumps during that
change is a new dynamical model. This note checks it instead of assuming the
old ground-state preparation theorem still applies.

Write P_p for the flippable projector and X_p for the flip. Then

    H_RK = J sum_p (P_p-X_p) = 2J sum_p P_p^-,
    V_f = sum_p P_p,
    H_delta = H_RK - delta V_f,   delta real.

Here delta>0 corresponds to the usual V<J direction. The old jumps are
L_p=|s><d| summed over the disjoint p-pairs, with positive rates gamma_p.
V_f is diagonal with entry d(c), the number of flippable plaquettes in c.
This d(c) is not the occupation-monitoring strength in the earlier ring work.

## 2. Exact finite-spin compatibility test

Each L_p is nilpotent. For a pure stationary density, the purity derivative
requires every L_p to have the pure-state vector as an eigenvector. Its only
eigenvalue is zero. On the connected flip component the common kernel is
span(u). Therefore a pure stationary state of the unchanged-jump generator
must be |u><u|, and it is stationary exactly when H_delta u is proportional
to u. For delta nonzero this is equivalent to d(c) being constant over C.

For nonconstant d(c) and nonzero delta, the unchanged cooling generator has no
pure stationary state. This statement applies to this fixed jump family, even if all its
positive rates are changed. It says nothing against a different jump family,
turning the apparatus off, or another microscopic mechanism.

The residual at the formerly prepared state is quantitative:

    G_delta(|u><u|) = i delta [V_f,|u><u|],
    ||G_delta(|u><u|)||_HS^2 = 2 delta^2 Var_u(V_f).             (1)

An isolated flippable square has constant d=1 and is a positive exception.
Actual larger components need their own d(c), rather than an inference from
the existence of a plaquette. The companion controls compute that variance
on the selected open and cubic periodic components.

## 3. A specified Gaussian model for the compatibility question

The following is an independent effective-model diagnostic. For each nonzero
transverse momentum mode set s=4 sum_i sin^2(k_i/2), and use one real canonical
oscillator (q,p), [q,p]=i. There are two transverse polarizations on the cubic
lattice. Put

    H_U=(a p^2+b q^2)/2,
    a=K s,  b=U+W s,    K,W>0, U>=0,
    omega=sqrt(a b).

q represents the transverse electric amplitude in this convention; p is its
conjugate potential amplitude. The U=0 frequency is sqrt(KW)s. For U>0 it
becomes sqrt(KU)|k| at long wavelength. The quadratic effective Hamiltonian
is motivated by Hermele, Fisher and Balents, cond-mat/0305401, Sections III.B
and III.C, and by the repo's explicitly conditional phase-bridge note. This
motivation is not a new microscopic phase proof.

Keep the U=0 oscillator shape

    r=sqrt(K/W),
    b0=(q/sqrt(r)+i sqrt(r)p)/sqrt(2),
    L=sqrt(nu) b0,    nu=gamma s, gamma>0.                       (2)

At U=0 this bath prepares the RK-shaped vacuum with covariance
V0=diag(r/2,1/(2r)). Equation (2), including its s-dependent damping, is a
supplied Gaussian reservoir. Coarse-graining the microscopic local record
cooler into this reservoir is an open obligation; the results below do not
assume that obligation has been discharged.

Fresh record outputs can label jumps of (2) in an ideal quantum-jump
instrument. The count is conditional on that instrument and its fresh fuel,
not an automatically available record observable of the framework.

## 4. Exact covariance, mode poles, and energy

For zero first moments, let Q=<q^2>, P=<p^2>, C=<{q,p}>/2. Their covariance V
satisfies dot(V)=A V+V A^T+D with

    A=[[-nu/2,a],[-b,-nu/2]],
    D=(nu/2) diag(r,1/r).

All modes s>0 are stable. Define Z=nu^2+4ab and d0=a/r-br. The exact
stationary covariance is

    Q_inf=r/2+a d0/Z,
    P_inf=1/(2r)-b d0/Z,
    C_inf=nu d0/(2Z).                                         (3)

The drift poles are -nu/2 +/- i omega. Thus linear-in-|k| oscillation poles
can coexist with a state that is not the photon vacuum. A dispersion fit
alone does not determine the state or its occupation numbers.

The energy has an especially simple exact equation, for arbitrary states
with finite second moments, including their first-moment contributions:

    d<H_U>/dt = -nu(<H_U>-E_star),
    E_star=(br+a/r)/4.                                        (4)

If the initial state is the old RK-shaped vacuum, its energy after the
Hamiltonian change is already E_star, and remains that value at every time.
The fixed reservoir does not cool this energy toward omega/2. Its stationary
occupation relative to the new oscillator is

    n_U=E_star/omega-1/2
       =(br+a/r)/(4 sqrt(ab))-1/2.                            (5)

This energy and occupation are independent of every positive gamma. Making
the same bath weaker changes relaxation time, not its stationary energy.
At gamma=0 there is no attracting stationary state; limits in time and bath
strength must not be interchanged silently.

## 5. Long-wavelength and record-output consequences of this model

For fixed U>0 and s->0 through nonzero modes, equation (3) gives

    Q_inf -> r/4,
    s P_inf -> U r/(4K),
    C_inf -> -gamma r/(8K),
    E_star -> U r/4,
    sqrt(s) n_U -> sqrt(U/W)/4.                               (6)

The first two quadratures have leading classical equipartition energy
T_eff=U r/4. This is an infrared energy scale, not a claim that the complete
stationary state is a Gibbs state: finite-momentum squeezing/cross-covariance
remain. The true H_U vacuum instead has Q_ground=sqrt(a/b)/2, which vanishes
as sqrt(s). Thus the bath's constant small-s electric variance remains
different from the vacuum variance despite its linear oscillation frequency.

Its stationary rate of resolved jump records follows from

    <b0^dag b0>_inf=d0^2/(2Z),
    j_inf=nu d0^2/(2Z) -> gamma U/(8W).                        (7)

For any fixed finite collection of nonzero modes with U>0 this produces
records at a positive asymptotic rate and hence has infinite expected total
output over infinite time. That is a different resource requirement from
the finite expected number of jumps in the exactly matched RK preparation
theorem. It is not an argument that permanent records forbid a photon phase.

## 6. A positive matched-bath construction, with its locality cost exposed

For each mode replace r by r_U(s)=sqrt(a/b), and supply

    b_U=(q/sqrt(r_U)+i sqrt(r_U)p)/sqrt(2),
    L_U=sqrt(nu) b_U.                                         (8)

The same calculation now gives the exact pure H_U vacuum as the unique
stationary Gaussian state. In fact <b_U^dag b_U>(t) decays as exp(-nu t),
so its integrated expected jump output equals its initial mean occupation.
This is a concrete alternative, not a no-go for ground-state preparation.

Equation (8) changes the reservoir, not just its rate. At U>0 and small s,
r_U is proportional to sqrt(s); its coefficients have powers s^(-1/4) and
s^(1/4). Implementing the displayed mode-by-mode formula therefore requires
a momentum-dependent apparatus. This formula alone does not provide a
finite-range plaquette implementation. Spectral filtering, physical bath
dynamics, preparation followed by decoupling and an adiabatic Hamiltonian
change, or another local microscopic construction remain routes to examine.
No universal locality obstruction is claimed here.

## 7. Verification status and claim boundaries

The companion runner passed its first complete run, checking the finite-spin
criterion, the complete symbolic Lyapunov equation, energy/count identities,
limiting coefficients, and stationary truncated-oscillator controls assembled
directly from a Lindblad superoperator. The periodic864-state component has
mean flippability8 and variance16/3, hence squared residual(32/3)delta^2.
The one-square control stays pure after changing its constant potential;
the two-square and open-cube controls have mixed stationary states. Five
Gaussian parameter sets at Fock cutoffs32,64,96 converge to the symbolic
covariance (largest final error9.47e-8). Two matched-bath controls approach
the pure new ground state, with final covariance errors below1.2e-12.
All raw results and execution provenance are preserved. A finite oscillator
cutoff is a convergence control,
not the exact infinite-dimensional proof. The algebra above is the proof for
the specified quadratic model. The microscopic-to-Gaussian identification,
native record law, phase selection, and relativistic unification stay open.

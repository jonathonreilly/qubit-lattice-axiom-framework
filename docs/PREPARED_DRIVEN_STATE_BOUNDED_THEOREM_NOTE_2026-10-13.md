---
claim_id: prepared_driven_state_bounded_theorem_note_2026-10-13
claim_type: bounded_theorem
claim_scope: "Finite-form near-ground pulse work and actual excess; full driven density and separate free-energy limits, with original fixed-window hypotheses and scoped controls."
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
artifact_role: theorem
assembly_status: source_accepted_publication_scope_separately_gated
runner: scripts/prepared_driven_state_identity_2026_10_13.py
scientific_execution: no_mathematical_predicates_in_identity_tools
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: supplied-model conditional arguments with explicit provisional dependencies
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: complete conditional proof bodies preserved with two specifically authorized wording corrections across this source assembly
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: exact publication review and source integration, cumulative stack checks, then independent retained audit
upstream_dependencies:
  - bv_graph_energy_protocol_bounded_theorem_note_2026-10-13
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - bounded_interaction_ground_bounded_theorem_note_2026-10-12
  - adiabatic_ground_preparation_bounded_theorem_note_2026-10-12
  - excitation_pulse_response_bounded_theorem_note_2026-10-12
---

# Prepared-pulse robustness and driven-state sources

**Type:** bounded_theorem

Status: conditional-support. Root accepted the pinned source assembly for
publication preparation. Exact publication-wrapper and program acceptance is
recorded separately in the installed evidence packet; source acceptance alone
authorizes no execution. The filename date is not evidence of publication.

The two complete arguments below retain their own local notation, equation
labels, premises, controls and historical status/exposure statements. Each
source was frozen before its later source-exposed comparison. The assembly
does not create a new combined theorem by concatenating them. All original
bytes are recoverable from the content-addressed source archive.

The selected sources are `PREPARED_PULSE_ROBUSTNESS_INDEPENDENT.md` and `DRIVEN_STATE_ENERGY_LIMIT_INDEPENDENT.md`. Original phrases saying
that comparisons or root reads are pending describe their earlier freezes.
The later complete comparison reports are archived separately, and root reports
complete reads of the four independent bodies and four comparison reports.
This worker read those eight complete bodies during source assembly. Root
reused its complete body/comparison reads at unchanged hashes, read the six
new source wrappers and changed surrounding arguments, and mechanically
reconstructed all twelve complete diffs and 211 original aliases. Root did not
claim to manually reread every assembled unchanged line or complete diff.
The exact source acceptance record preserves those coverage limits. Publication
wrapper/program review is a separate gate. This chronology is not a new proof.

The derivation/comparison lineage is separate-context reasoning within the same
selected model family with shared parents, followed by source-exposed checks.
It is neither model-diverse checking, analytic Lean verification nor retained
audit. Current remains `open_gate`; every inherited conditional/open premise
remains explicit. No N1/N5 packet PASS or global no-go is assigned.

## First complete source body

# Pulse work from an imperfectly prepared actual ground

Status: conditional ordinary mathematical derivation in a separate context of
the selected model family. The scientific parents below were supplied; no root
prepared-pulse candidate or new independent candidate was read. This is neither
a formal verification nor an audit or a model-diverse check. The note is to be
frozen before source comparison. No novelty or optimal preparation-rate claim
is made.

The main estimate controls the actual work and actual final excess energy of
every normal state of finite form energy. Its leading preparation error is
proportional to the square root of the initial excess times the ground pulse
excitation amplitude. For fixed pulse resources, initial excess
`o(epsilon^2)` suffices to recover the ground quadratic coefficient. The
supplied ramp therefore gives the sufficient condition
`tau |epsilon| -> infinity`. An explicit family in the supplied actual chain
changes that coefficient at initial excess of order `epsilon^2`. This last
statement concerns unrestricted near-ground initial families, not necessity
for the particular linear-ramp outputs.

## 1. Supplied premises and notation

Let `H>=0` be selfadjoint, `V=V*` bounded with `||V||<=K`, `G=H+V`, and
let the actual normalized ground be `Omega`, with simple ground projection
`P=|Omega><Omega|`, ground energy `E_g`, and

    F=G-E_g>=g(I-P),       g>0.                               (R1)

Put `Pi=I-P`. The closed form domain is
`Q=D(F^(1/2))=D(H^(1/2))`; all unbounded state expectations below are spectral
or closed-form expectations. Finite `Tr rho F` is equivalent to finite
`Tr rho H`. No assumption that `A` or `V` preserves either energy domain is
made.

The pulse generator is `G-epsilon j(t)A`, where `A=A*`, `||A||<=a`, and
`j` is a real compact whole-line BV function, supported in `[0,T]`. Its
canonical right trace is used, and `nu=Dj` includes both endpoint atoms.
The initial energy is at `0-`, the final base energy at `T+`. Define

    J(t)=integral_0^t |j(s)|ds,      J=J(T),
    TV=|nu|([0,T]),                 k=a TV,
    B_j=integral_[0,T] J(t)|nu|(dt),
    C_j=integral_[0,T] J(t)^2|nu|(dt),
    h=|epsilon| k.                                             (R2)

The allowed BV parent proves, for the actual propagator `U=U_epsilon(T,0)`,
that `UQ=Q`, `UD(G)=D(G)`, and the following exact polarized form identity:

    q_F(Ux,Uy)-q_F(x,y)=<x,T_epsilon y>,       x,y in Q,
    T_epsilon=-epsilon integral_[0,T] U(t,0)* A U(t,0)dnu(t),
    T_epsilon=T_epsilon*,           ||T_epsilon||<=h.          (R3)

It is a bounded work operator, although `F` is unbounded. For a density of
finite form energy, the actual work is

    w_rho=Tr(U rho U* F)-Tr(rho F)=Tr(rho T_epsilon).            (R4)

Thus `|w_rho|<=h`. Set

    eta=Tr(rho F),       p=Tr(rho Pi),       p<=min(1,eta/g),
    D=D_epsilon=q_F(U Omega)=Tr(P T_epsilon)>=0.               (R5)

In the supplied full-Fock small-interaction model, the full gap is
`delta=m-2K>0`. An even source and the even ground give the ground-excitation
gap `Delta=2m-2K`. Therefore, independently of the input state's parity,

    D<=min(h, epsilon^2 C_g),
    C_g=a^2 min(2B_j,TV^2/Delta).                              (R6)

For unrestricted input use `g=delta` in R1. For input supported entirely in
the even sector one may use `g=Delta`. Merely commuting with parity does not
imply even-sector support. Without sector information, do not insert the
even gap into the initial-state estimate. In a general gapped model, replace
`Delta` in R6 by an actually established gap for the ground pulse trajectory.

The parent also gives, with `xi=(A-<Omega,A Omega>)Omega`,

    Q_j=integral omega |jhat(omega)|^2 <xi,1_domega(F)xi>,
    jhat(omega)=integral_0^T j(t)exp(i omega t)dt,
    |D-epsilon^2 Q_j|<=2|epsilon|^3 a^3 C_j.                  (R7)

Here `Q_j>=0`; no unfiltered positive spectral moment of `xi` is assumed.

## 2. Exact mixed-state decomposition in the form domain

Take a spectral decomposition `rho=sum_l lambda_l |psi_l><psi_l|` with
positive weights, unit vectors, and `sum lambda_l=1`. Finiteness of `eta`
implies every positive-weight `psi_l` lies in `Q`. Write

    psi_l=a_l Omega+z_l,       z_l=Pi psi_l in Q.

Then `sum lambda_l ||z_l||^2=p`,
`sum lambda_l |a_l|^2=1-p`, and
`sum lambda_l q_F(z_l)=eta`, because `F^(1/2)Omega=0`.
Apply R3 to `z_l` and sum:

    d=Tr(Pi rho Pi T_epsilon),       |d|<=h p,
    sum_l lambda_l q_F(Uz_l)=eta+d>=0.                       (R8)

This sum is finite. Indeed each nonnegative final form energy is bounded
above by its initial form energy plus `h||z_l||^2`.

In the Hilbert direct sum over the spectral decomposition, define

    u_l=sqrt(lambda_l) a_l F^(1/2)U Omega,
    v_l=sqrt(lambda_l) F^(1/2)U z_l.

Their squared norms are `(1-p)D` and `eta+d`, respectively. Both are finite;
consequently the sum of cross terms is absolutely convergent by
Cauchy-Schwarz. This proves, without ever pairing trace distance with `F`,

    E_f:=Tr(U rho U* F)=(1-p)D+eta+d+C,
    w_rho-D=d-pD+C,
    C=2 Re sum_l <u_l,v_l>,
    |C|<=2 sqrt((1-p)D(eta+d))
         <=2 sqrt((1-p)D(eta+h p)).                         (R9)

All expressions on the first two lines are independent of the chosen
spectral decomposition. In particular the theorem applies to mixed states
and coherent pure states that belong only to `Q`, not to `D(G)`.

The resulting finite-strength robustness estimate is

    |w_rho-D|<=R_p,
    R_p=p(D+h)+2 sqrt((1-p)D(eta+h p))
        <=R_g:=eta(D+h)/g+2 sqrt(D eta(1+h/g)).              (R10)

The final excess has the exact relation `E_f=eta+w_rho`, and therefore
`|E_f-D|<=eta+R_p`. The direct-sum triangle inequality also gives

    ( sqrt((1-p)D)-sqrt(eta+h p) )_+^2 <= E_f
       <=( sqrt((1-p)D)+sqrt(eta+h p) )^2.                  (R11)

Only the stated upper bound for `eta+d` is used in the lower bound here;
no sign of the work integrand is assumed. Positivity of `F` gives the
additional exact constraint `w_rho>=-eta`. Work can be negative; final
excess cannot. If `D=0`, the cross term vanishes and the stronger
`|w_rho|<=hp` follows. At zero pulse, `D=h=0`, `w_rho=0`, and `E_f=eta`.

For comparison, a short bounded-observable estimate is

    ||rho-P||_1<=2 sqrt(p),
    |w_rho-D|<=2h sqrt(p)<=2h min(1,sqrt(eta/g)).             (R12)

For each pure spectral component the rank-one trace formula gives twice
`||Pi psi_l||`; convexity and scalar Cauchy-Schwarz give the mixed formula.
R12 is used against the bounded `T_epsilon` only. One may take the minimum
of R10 and R12. R10 retains the more informative ground excitation `D`
and has the sharp leading coherence coefficient exhibited below.

The form-only class is nonempty even at a fixed actual spacing. Choose
normalized even `2n`-particle wavepackets whose individual mode energies
lie in one fixed finite energy interval. Such states can be chosen because
the actual one-particle momentum band is infinite dimensional. Their
energies are bounded above and below by positive multiples of `n`, and
their squared energies by multiples of `n^2`. A superposition over these
orthogonal particle sectors with squared amplitudes proportional to `n^-3`
is in `Q` and outside `D(H)`. Mixing coherently with the ground with any
small nonzero amplitude retains this property and gives arbitrarily small
positive form energy in the free `V=0` member. R8-R11 cover it directly.

## 3. Coherence, stationarity, passivity and mean caps

If `P rho Pi=0`, then the cross term in R9 is zero. This follows directly
by evaluating the bounded `T_epsilon` on the block diagonal density and
comparing R9; it does not require an unbounded functional on a Hilbert-norm
sum. Hence

    |w_rho-D|<=p(D+h).                                      (R13)

This is a condition on coherence between the ground and its complement.
It does not assert stationarity inside the excited block.

For a stationary state, meaning `exp(-itG)rho exp(itG)=rho` for all real
`t`, there is a further improvement. Put

    beta_t(A)=exp(itG)A exp(-itG),
    L=-integral_[0,T] beta_t(A)dnu(t).

The bounded interaction equation implies

    ||T_epsilon-epsilon L||<=2 epsilon^2 a^2 B_j.            (R14)

To verify it, `||S(t)-I||<=|epsilon|aJ(t)` for the interaction unitary,
so conjugating `beta_t(A)` costs at most `2|epsilon|a^2J(t)`; integrate
against `|epsilon||nu|`. Stationarity and `nu([0,T])=0` give
`Tr(rho L)=Tr(P L)=0`. Stationarity also implies `P rho Pi=0`, because
the ground is an isolated simple eigenspace. Thus `||rho-P||_1=2p`, and

    |w_rho-D|<=4 epsilon^2 a^2 B_j p.                       (R15)

Neither stationarity nor vanishing linear work establishes passivity.
Passivity is the additional assertion that work cannot be extracted by the
allowed cyclic operations. The actual ground has it for every finite-energy
unitary image because `F>=0`. The near-ground states in section 6 can have
negative work. R15 is a conditional estimate if nontrivial normal stationary
excited states exist; none is assumed to exist in a purely continuous
infinite-volume spectral sector.

The energy relations are different from a bound on the initial free mean.
If only `Tr rho H<=M` is supplied, then

    eta=Tr rho G-E_g<=M+K-E_g<=M+2K,
    Tr(rho_final,hold H)<=M+2K+w_rho<=M+2K+h.                (R16)

The first bound generally does not vanish. In the second line an arbitrary
subsequent autonomous `G` hold is allowed; it conserves `G` energy and
`|Tr rho V|<=K`. No new `2K` is accumulated per hold. Using actual near-ground
information instead gives

    Tr(rho_final,hold H)<=E_g+K+E_f<=2K+eta+D+R_p.           (R17)

The second inequality uses the supplied zero-energy free vacuum, which
implies `E_g<=K`; the first inequality applies in the general R1 setting.
For the actual band model, the same upper bound divided by `Lambda_c`
bounds `Tr rho N_H` and `Tr rho Q_H`. These are global free-energy and
high-occupation estimates, not local energy inequalities.

A positive fixed cap cannot select the ground: in the free actual model
choose an even normalized two-particle vector `chi` of finite energy
`E_chi>0`, orthogonal to vacuum, and a fixed `0<r<1`. The density
`(1-r)P+r|chi><chi|` has excess `r E_chi` and trace distance `2r`.
Choose `r E_chi<=M` for any prescribed positive cap. Conversely,
trace distance tending to zero need not make excess tend to zero: use
two-particle wavepackets with mean energies `E_n->infinity` and weights
`r_n=M/E_n`. Their mixtures converge in trace norm to vacuum but retain
energy `M`. The target has such high-momentum wavepackets; actual spacings
tending to zero may be chosen so each packet lies inside its actual low
band. These examples never add zero-energy outside-band modes.

## 4. Applying the supplied linear-ramp preparation

The supplied protocol starts in the exact free vacuum, switches
`H+(t/tau)V` for `0<=t<=tau`, then holds `G`. Write `rho_tau,w` for its
state after any waiting time `w>=0`. Its independently compared parent
gives, uniformly in actual spacing and in `w`,

    eta_tau<=D_*^2/tau^2,
    ||rho_tau,w-P||_1<=2e_tau,
    e_tau=min(1,C_ad/tau),       Tr rho_tau,w G<=K,
    Tr rho_tau,w H<=2K.                                      (R18)

Here, using the full gap `delta=m-2K`,

    C_ad=2K/delta^2+31K^2/delta^3,
    M_*=sqrt(m/(m-K)),
    a_*=K sqrt(2m-K)/delta^2,
    b_*=K^2[ sqrt(30(43m+4K))+sqrt(2m-K) ]/delta^3,
    D_*=(1+M_*)a_*+M_*b_*.                                  (R19)

These constants are supplied sufficient constants, not optimized constants.
An even interaction preserves the even sector, so R10 can use `g=Delta`
for these prepared states, while R19 continues to use its proved full-gap
constants. Combining R6 and R10 gives, at every finite amplitude and
`tau>0`,

    |w_tau,w-D|<=
      D_*^2 (epsilon^2 C_g+|epsilon|k)/(g tau^2)
      +2|epsilon| sqrt(C_g) D_*/tau sqrt(1+|epsilon|k/g).     (R20)

The separate direct bound `2h e_tau` is also available. Their minimum may
be used. Every bound is uniform in the waiting time, although the actual
work of a coherent imperfect preparation may depend on that time.

The final excess is `eta_tau+w_tau,w`; its difference from ground absorption
is at most `D_*^2/tau^2` plus the chosen work error. The stronger initial
`G` cap in R18 improves the final free cap to

    Tr(rho_after_pulse_and_hold H)<=2K+w_tau,w
                                      <=2K+D+work_error.    (R21)

This omits an unnecessary extra `eta_tau`. Ground pulse absorption is the
additional work of this pulse. It is not the work of the preceding switch;
the latter prepares a final `G` expectation `E_g+eta_tau` from initial
free energy zero. No relaxation, passive-error hypothesis, state-selection
law, or autonomous availability of the external switch is inferred.

## 5. Finite pulse continuum limits and joint weak-source limits

Keep `j,T,a,m,K` fixed. The permitted BV parent supplies, under its actual
common-CAR norm-orbit and static-ground hypotheses,

    |D_c(epsilon)-D_0(epsilon)|
      <=4 epsilon^2 a B_j [d_A,c(T)+a b_c],                 (R22)

where `d_A,c(T)->0` is the compact-time interacting source-orbit error and
`||P_g,c_hat-P_g,0_hat||_1<=2b_c`, with `b_c->0`. The ground target density
includes the high vacuum; observable extensions are unital. These distinct
embeddings are inherited without alteration.

For actual initial densities with excess `eta_c`, at any fixed finite
`epsilon`, R10 gives

    |w_rho_c-D_0|<=R_g,c+4 epsilon^2 a B_j[d_A,c(T)+a b_c],
    |E_f,c-D_0|<=eta_c+R_g,c
                              +4 epsilon^2 a B_j[d_A,c(T)+a b_c]. (R23)

Thus `eta_c->0` suffices for both conclusions at fixed finite strength.
In particular, the supplied ramp has this property for every
`tau(c)->infinity`, uniformly in any `w(c)>=0`. No comparison of complete
propagators on the diverging ramp or waiting interval occurs.

For clarity, actual total interacting energy is `E_g,c+E_f,c`. Its fixed
finite-strength limit also follows from the supplied static resolvent
comparison. If `mu>K` and `nu_c=||V_c_hat-V_0_hat||`, put

    r_c=(mu^2 c/v+nu_c)/(mu-K)^2.

The compressed interacting resolvents differ by at most `r_c`. Their top
eigenvalues are `lambda_c=1/(mu+E_g,c)` and `lambda_0`, both at least
`1/(mu+K)`. The variational top-spectrum inequality gives
`|lambda_c-lambda_0|<=r_c`, hence

    |E_g,c-E_g,0|<= (mu+K)^2 r_c.                           (R24)

Adding this to R23 proves convergence of the actual total `G` energy to
`E_g,0+D_0`. For arbitrary capped input, bounded work convergence alone
would leave an initial energy defect; here the separate `eta_c->0` and
R24 remove it. A free-`H` energy comparison also requires convergence of
the bounded final `V` expectation; the cap R17 by itself is not such a
comparison.

Now let nonzero `epsilon_c->0`. Under the parent's static filtered spectral
coefficient convergence `Q_j,c->Q_j,0`, R7 and R12 give the explicit estimate

    |w_rho_c/epsilon_c^2-Q_j,0|
      <=|Q_j,c-Q_j,0|+2|epsilon_c|a^3 C_j
        +2a TV sqrt(eta_c/g)/|epsilon_c|.                  (R25)

The sharper R10 may replace the last term. The final excess divided by
`epsilon_c^2` has the additional error `eta_c/epsilon_c^2`. Therefore

    eta_c=o(epsilon_c^2)
       ==> w_rho_c/epsilon_c^2 -> Q_j,0,
           E_f,c/epsilon_c^2 -> Q_j,0.                     (R26)

Uniform gaps and fixed resources are part of this statement. Static
coefficient convergence plus the uniform cubic remainder suffices for this
weak-source result; finite-strength R22 has its additional norm-orbit
premise. Dividing a generic finite-strength comparison by `epsilon_c^2`
without inspecting its amplitude factors would lose this distinction.

For the supplied ramp, the sufficient joint condition from its actual
energy rate is

    c->0, epsilon_c->0, tau_c |epsilon_c|->infinity.         (R27)

It works uniformly in the arbitrary pre-pulse waiting time and any final
autonomous hold. At `K=0`, the actual ramp is exact and `D_*=C_ad=0`, so
no preparation-duration condition is needed. More generally R27 is not
claimed necessary for one fixed ramp, one waiting schedule, or a pulse
with `Q_j,0=0`: special cancellations can improve it.

The normalizations matter. R26 concerns excess above each *actual*
`E_g,c`. To replace that reference by the target `E_g,0` after dividing by
`epsilon_c^2`, additionally require
`E_g,c-E_g,0=o(epsilon_c^2)`; R24 supplies the sufficient condition
`r_c=o(epsilon_c^2)`. Work itself and the actual-excess statement need no
such ground-energy-rate condition. A raw total energy is not a quadratic
absorption coefficient.

Different restrictions on the input give different work-only conditions.
For states with `P rho Pi=0`, R13 gives the sufficient
`eta_c=o(|epsilon_c|)` for work's quadratic coefficient. For stationary
inputs, R15 gives the sufficient `eta_c->0`, without a relative rate to
`epsilon_c`. Final excess still includes the initial `eta_c`; these
work-only improvements do not remove it. None supplies a positive work
sign for all excited inputs.

If profiles, windows, source norms, or gaps vary, use R2 and R10-R25 with
their actual values. Individually finite BV variation does not bound
`TV,B_j,C_j` uniformly; a gap tending to zero can also spoil the displayed
estimates. No growing-window or impulse-limit theorem is asserted.

## 6. Coherent sharpness families and an actual-chain realization

The following construction tests the bound using bounded work throughout.
It never Taylor-expands an unbounded energy expectation without control.
For a fixed model and pulse set

    B=integral_0^T j(t) beta_t(A)dt,
    v_j=jhat(F)xi,       n_j=||v_j||,
    B Omega=<Omega,A Omega>(integral j)Omega+v_j.            (R28)

The BV Fourier bound implies
`v_j in D(F)`, `||F v_j||<=a TV`, `n_j<=aJ`, and
`q_F(v_j)=Q_j`. Stieltjes integration against the complete cyclic measure
gives, with the source sign used here,

    L Omega=iF v_j.                                         (R29)

Indeed the ground scalar integrates to zero, and
`integral exp(i omega t)dnu(t)=-i omega jhat(omega)`.

For any fixed real `lambda` define the normalized initial vector

    psi_lambda,epsilon=(Omega-i lambda epsilon v_j)/N,
    N^2=1+lambda^2 epsilon^2 n_j^2.                         (R30)

It lies in `D(F)`, is even for an even pulse, and is an allowed normal pure
state. Its exact initial excess is

    eta_lambda,epsilon=lambda^2 epsilon^2 Q_j/N^2.          (R31)

In the bounded `T_epsilon` expectation, the ground term is `D`, the
leading cross term from R29 is `-2 lambda epsilon^2 Q_j`, and the excited
diagonal term is bounded by `lambda^2 |epsilon|^3 k n_j^2`.
Using R14 for the cross-term error and R7 for the ground term yields

    |N^2 w_lambda,epsilon-(1-2lambda)epsilon^2 Q_j|
       <=|epsilon|^3 K_lambda,
    K_lambda=2a^3 C_j+4|lambda|a^2 B_j n_j
                                      +lambda^2 k n_j^2.   (R32)

The finite normalizer is retained. Adding R31 therefore also gives

    |N^2 E_f,lambda,epsilon-(1-lambda)^2 epsilon^2 Q_j|
       <=|epsilon|^3 K_lambda.                             (R33)

For `Q_j>0`, any fixed nonzero `lambda` changes the work coefficient at
an initial excess of order `epsilon^2`. For `lambda>0`, the leading
negative cross term equals `-2|epsilon|sqrt(eta Q_j)` to leading order;
this attains the leading magnitude in R10. Values `lambda>1/2`
give negative leading work. With `lambda=1`, the leading final excess
vanishes. Values `lambda<0` give constructive addition instead. These
statements do not depend on declaring a coherent error passive.

There is also an exact finite-strength extraction control:

    rho_epsilon^rev=U_epsilon* P U_epsilon,
    U_epsilon rho_epsilon^rev U_epsilon*=P,
    w_rev=-eta_rev,       E_f,rev=0.                       (R34)

Domain preservation makes its actual initial energy finite. In the even
case the bounded commutator in the BV parent gives
`eta_rev<=h^2/Delta`. Its small-source coefficient is the same `Q_j`:

    |eta_rev-epsilon^2 Q_j|
       <=2|epsilon|^3 a^3 [C_j+TV J^2+2J B_j].              (R35)

Here is a bounded derivation of R35. Write `S=exp(iTG)U`. The interaction
equation gives `||S-I||<=s=|epsilon|aJ` and
`||S*-I+i epsilon B||<=s^2/2`. Since `U*Omega` differs from `S*Omega`
only by a scalar phase, R3 applied to `S*Omega` gives
`eta_rev=-<S*Omega,T_epsilon S*Omega>`.
Expand this bounded expectation about `Omega`. R29 makes the first cross
term `-2epsilon^2 Q_j`. The replacement of `S*Omega-Omega` by
`-i epsilon B Omega` costs at most `h s^2`, replacing `T_epsilon` by
`epsilon L` in the cross term costs at most
`4|epsilon|^3 a^3 J B_j`, and the quadratic vector-difference term costs
at most `h s^2`. R7 supplies the remaining `2|epsilon|^3 a^3 C_j`.
This proves R35 without taking an uncontrolled form-norm derivative of `S`.

To show that these are controls in the actual allowed family, rather than
two-level surrogates, take the permitted `V_c=V_0=0` model. Choose a real
normalized nonzero `f in C_c^infinity(R;R^2)` and a sufficiently far
translate `g(x)=f(x-L)` so their compact supports are disjoint. In the
target vacuum representation put

    A_0=i c(f)c(g),       ||A_0||=1,
    u=sqrt(2)P_+f,        z=sqrt(2)P_+g.                    (R36)

The real field convention is `c(f)=a*(u)+a(u)` with
`{c(f),c(g)}=2(f,g)_R`. Disjoint real supports make the two fields
anticommute, so `A_0` is selfadjoint and even. Translation commutes with
`P_+`, so `z(p)=exp(-ipL)u(p)`. The vector `u` is nonzero (its norm is
one), and its support has positive Lebesgue measure. A nonconstant
exponential cannot be constant on that support up to null sets. Therefore
`u,z` are complex-linearly independent, and

    xi_0=i a*(u)a*(z)Omega !=0                             (R37)

is the centered two-particle excitation of `A_0`.

Its energy spectral measure for `H_0=dGamma(E)` has no atoms. For each
fixed momentum `p`, the equation `E(p)+E(q)=omega` has at most two real
solutions in `q`, since `m,v>0`; Fubini makes each level set null in the
two-particle momentum plane. The two-particle wavefunction is square
integrable, so its spectral measure gives those sets zero mass.

Choose the rectangle `j=1_[0,T)` for any fixed `T>0`. It has
`TV=2`, `J=T`, `B_j=T`, `C_j=T^2`, and
`jhat(omega)=(exp(i omega T)-1)/(i omega)`. Its zeros at positive energies
form a discrete set. The nonzero, non-atomic measure in R37 therefore gives

    Q_j,0>0.                                                (R38)

At each sufficiently small actual spacing use
`A_c=i c_c(C_c f)c_c(C_c g)` and its actual even-spin representative.
The supports occupy disjoint cells, so it remains selfadjoint; `||A_c||<=1`.
The cell hull gives finite physical spin support. The parent's ordinary
cell norm-orbit comparison supplies `Q_j,c->Q_j,0>0`. These assertions use
Local sections 3, 5 and 6, especially L18 and L23-L24; they do not repeat
the synthesis's known erroneous attribution of support to L10.

Apply R30 at each actual spacing, with its actual `F_c`, ground, pulse
and filtered vector. For any nonzero `epsilon_c->0` and fixed `lambda`,
the uniform constants in R32-R33 give

    eta_c/epsilon_c^2 -> lambda^2 Q_j,0,
    w_c/epsilon_c^2   -> (1-2lambda) Q_j,0,
    E_f,c/epsilon_c^2 -> (1-lambda)^2 Q_j,0.                (R39)

Alternatively R34-R35 give initial coefficient `Q_j,0`, work coefficient
`-Q_j,0`, and exactly zero final excess. These states retain the actual
finite-spacing Hamiltonians and high branch, are normal and even, and
have finite operator-domain energy. With `V=0`, initial free mean equals
the displayed vanishing excess, so any fixed positive free cap is met
eventually. A declared bound `0<K<m/2` may bound the zero interaction if a
positive cap `2K` is specifically required.

This exhibits failure of a universal replacement of `eta=o(epsilon^2)`
by `eta=O(epsilon^2)` for arbitrary allowed coherent near-ground families.
It also changes the coefficient for every prescribed positive sufficiently
small leading excess constant by choosing a nonzero small `lambda`.
The state is allowed to depend on the known pulse. Neither R30 nor R34 is
asserted to be the output of the supplied fixed ramp. In this free member
that ramp actually prepares the exact vacuum. Necessity of R27 for a
particular nonzero-interaction ramp would be a different obligation.

## 7. No-Go Discipline Gate: restricted boundary scope

This section records the negative-claim scope checks, not a formal no-go
packet PASS. The mathematical witness R39 defeats a universally quantified
replacement of a small-o hypothesis by a big-O hypothesis. It does not
declare that every preparation, every pulse or every error at that scale
fails. No framework wall, retained-status judgment or exhaustive discovery
claim is made. The task's exact-source restriction excludes repository-wide
queue, checkpoint and prior-candidate scans.

**N1: actual alternative mechanisms tested.** The following are distinct
mathematical restrictions or mechanisms, rather than renamed artifacts.

| Attempted mechanism | Outcome within this derivation |
|---|---|
| Remove ground/excited coherence | R13 permits a weaker work-only error scaling; this is a live restricted route, not excluded by the coherent witness. |
| Impose complete stationarity | R15 removes the linear work baseline and needs only vanishing excess for work's coefficient; it does not remove initial energy from final excess. |
| Choose a spectrally dark pulse | `Q_j=0` can improve the leading behavior. The sharpness witness explicitly establishes `Q_j,0>0` in R38. |
| Restrict to the actual ramp's output manifold | This could permit cancellations absent in general near-ground states. Necessity of R27 on that smaller class remains open here. |
| Use parity as a protection | The family R30/R36 is entirely even, so even-sector support alone does not remove its coherent interference. |
| Enforce an initial mean cap or trace convergence | R31/R39 satisfy every fixed positive cap eventually and converge to the actual ground in trace norm; neither excludes the witness. |
| Reverse the actual finite pulse | R34 attains the exact lower work constraint `w=-eta`, with a domain-valid allowed state; no asymptotic sign argument is needed. |

These are attempts and live escapes, not five falsely labelled failed routes
with retained-authority citations. The supplied mathematical sources are
provisional. No formal five-failed-route submission certificate is claimed.

**N2: dependencies rather than an invented wall count.** Uniform actual gap,
finite pulse resources and the specified initial-state class are explicit
hypotheses. No pairwise independence of these hypotheses is asserted. The
ramp's `tau |epsilon|` condition is derived from its excess bound, not an
independent physical obstruction. The optional target-ground subtraction
rate in R24 is a separate normalization requirement, absent when subtracting
the actual ground.

**N3: hidden-condition scan.** The source was reread for unstated domains,
stationarity, parity, positive work, vacuum selection, pointwise source
values, and varying resources. All load-bearing uses are explicit in
sections 1-6. The actual source realization uses `m,v>0`, a fixed nonzero
translate, real normalized compact fields, a rectangle of positive finite
duration, actual cell comparison, and nonzero `Q_j,0`; none is universalized.
The word "canonical" concerns only the BV right-trace convention. It
supplies no physics or status premise.

**N4: residual matching.** No earlier negative theorem is used as a witness
against this new boundary. The allowed BV norm-limit warning concerns an
energy-passage shortcut; R8-R9 explicitly avoid it. The allowed preparation
rate supplies a sufficient actual energy estimate; it does not supply a
necessity theorem. The centered excitation and work response use exactly
the same source sign and cyclic endpoint measure.

**N5: resolution audit.** The estimates concern one bounded global pulse and
global actual energy, on full actual Fock and its stated even sector. R36-R39
use a finite physical cell hull at every spacing and the supplied full
continuum model. No per-site, per-mode or local-energy conclusion is drawn.
No scientific runner was executed, so no numerical or multi-resolution
execution certificate is invented.

**N6: possible partial closure.** Dephasing, stationarity, pulse spectral
zeros, or information about the actual ramp error direction can improve the
restricted conclusion. They are additional hypotheses or mathematical
controls, not matters settled by a naming convention. Nothing here says a
new physical axiom is required. No primitive-registry exclusion is asserted.

**N7: strongest objection.** The adversarial objection is that a prescribed
linear ramp may only generate a special coherent error vector, whose leading
overlap with the pulse transition vector vanishes, perhaps after a chosen
hold. The given `O(tau^-2)` bound does not determine this vector or its
phase. Prove its asymptotic pulse cross term for that protocol before claiming
necessity of R27. This objection is valid against that stronger claim, which
is not made. It does not refute the explicitly constructed general initial
families in R30 and R34.

**N8: prior-cycle scope.** Only the four authorized parents and necessary
named Local/Current sources were consulted. Broader prior-cycle and queue
searches were excluded by this independent contract. No global impossibility,
novelty, repository-wide exhaustion or no-go packet completion is claimed.
The conditional inequality and actual counterexample remain reviewable on
their stated mathematical premises without that broader process claim.

## 8. Evidence, coverage and remaining obligations

The four permitted scientific parents were read completely at these exact
identities, with no truncated body treated as complete coverage:

| Parent | SHA-256 | Coverage |
|---|---|---|
| `BV_PULSE_WORK_INDEPENDENT.md` | `0af3a48b0604b6dfd530dfc901d81e789a89ef65b89d43391ed351f6f0ac95d9` | All 545 lines |
| `BV_PULSE_WORK_CROSSCHECK.md` | `741b3d4a73f2091768087b5cf4e3a004980632a6644eda6a19e9247164ba32b3` | All 401 lines |
| `ADIABATIC_PREPARATION_SYNTHESIS.md` | `6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c` | All 888 lines in contiguous ranges |
| `ADIABATIC_PREPARATION_SYNTHESIS_REVIEW.md` | `fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245` | All 285 lines |

Necessary parent-source checks used the exact Local file
`b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa`,
lines 102-116, 184-235, 339-378, 409-481, plus targeted field/polarization
search extracts. This establishes the precise field normalization, cell
support and even-spin attribution used here. Current at
`763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff`
was identity-checked and searched for relevant field/polarization passages;
its complete proof was not reread. Its compact-time comparison is reused as
the explicit supplied premise written in synthesis P43. This is not a new
transitive review of the chain or its representation.

The plan and four initial identities were sealed before any scientific
parent body was read. Exact immutable input copies, instruction identities,
exposure/read coverage, source validation notes and final source hash are in
`prepared_pulse_robustness_independent/`. The installed physics-loop and
workhorse instructions matched the supplied checkout byte-for-byte, including
the three relevant references. Live-main freshness was not fetched or claimed:
the task expressly excluded Git actions. Governing workflow text supplies no
scientific premise.

Remaining obligations are root examination of this frozen argument and any
later focused comparison; the explicit provisional parent premises retain
their status. This task does not settle a ramp-specific necessary scaling,
optimal finite-strength constants, gap closing, growing-window or impulse
limits, autonomous preparation, native physical source identification or
formal verification. It makes no empirical prediction or retained claim.

Only this note and its assigned evidence directory were written. No forbidden
root probe, seal, outcome, new graph-energy/native candidate, checkpoint,
handoff or queue was opened. No scientific program, numerical/formal runner,
delegation, Git operation, installation, PR, audit, editable prompt or axiom
change occurred. Mechanical file hashes and source copies establish identity
and recovery paths, not mathematical correctness. The final freeze precedes
disclosure of the result for comparison.




## Second complete source body

The following driven-state argument is preserved in full. Its one tracked edit
requires the initial density to be supported in the even sector when invoking
the optional larger gap. Mere parity invariance is insufficient. No displayed
formula or constant is changed. This argument needs the BV work and prepared-
pulse premises; it does not import the graph-energy improvements.

# Complete driven density and separate free energy: independent consequence

Status: conditional mathematical consequence of the frozen parents, with an
actual growing-hold counterexample. This is a same-family derivation with shared
parents, not a formal audit, model-diverse check, or retained classification.
No scientific program was executed. The new driven-state root probe, its seal,
and the other prohibited new candidates have not been read before this freeze.

The neutral plan records that initial route consideration preceded its seal;
it is not described as a preregistration of the derivation. Exact inputs,
inherited coverage, additional targeted rereads, exposure, and final identity
are in `driven_state_energy_limit_independent/`.

## 1. Question, objects, and inherited premises

The complete density means the trace-class operator on the common carrier
\(\mathcal F_* = \mathcal F_L\otimes\mathcal F_H\), with the actual density
embedded by the Fock isometry \(\iota_c\). The continuum target includes the high
vacuum. In contrast, bounded observable comparisons use **unital** extensions,
with a low even target operator tensored with \(I_H\). These are different maps.

Write \(H_c\ge0\) for the actual free Hamiltonian, \(G_c=H_c+V_c\),
\(F_c=G_c-E_{g,c}\), and \(P_c\) for the simple actual ground projection.
Use subscript zero for the continuum, and hats for the respective embeddings.
The potentials are selfadjoint and even; their unital extensions reduce the
actual range, as in the supplied preparation premises.
Both \(\|V_c\|,\|V_0\|\le K<m/2\); the full gap is
\(g=m-2K>0\). An initial density supported in the even sector and an even pulse may instead use the inherited
even excited gap \(g_e=2m-2K\). Every gap is an actual-space gap. An auxiliary
Hamiltonian extension outside \(\Pi_c=\iota_c\iota_c^*\) may have zero modes;
it supplies observable automorphisms and is never used for a ground or gap.

The preparation synthesis, sections 1 and 9-10, supplies the following inputs.

* The actual free vacuum embeds as the common Fock vacuum. The actual bands are
  \(I_c=(-1/c,1/c)\), with
  \[
  E(p)=\sqrt{m^2+v^2p^2},\quad
  e_{c,L}^2=m^2+\frac{2v^2p^2}{1+\sqrt{1-c^2p^2}},\quad
  e_{c,H}^2=m^2+\frac{2v^2}{c^2}(1+\sqrt{1-c^2p^2}).                 \tag{1}
  \]
  On the actual range, \(H_c\ge H_0\otimes I_H\) and
  \(H_c\ge\Lambda_c Q_H\), \(\Lambda_c=\sqrt{m^2+2v^2/c^2}\).
* \(\nu_c=\|\widehat V_c-\widehat V_0\|\to0\). For any fixed \(\mu>K\), put
  \[
  r_c=\frac{\mu^2c/v+\nu_c}{(\mu-K)^2},\quad
  d_\mu=\frac{m-2K}{(\mu+K)(\mu+m-K)},\quad b_c=\min(1,r_c/d_\mu).
                                                                    \tag{2}
  \]
  The compressed interacting resolvents differ in norm by at most \(r_c\),
  and \(\|\widehat P_c-\widehat P_0\|_1\le2b_c\). Their highest eigenvalues
  are \((\mu+E_{g,c})^{-1}\), so
  \[
  |E_{g,c}-E_{g,0}|\le(\mu+K)^2r_c=:e_c^{\rm gs}.                    \tag{3}
  \]
  Indeed \(|E_{g,c}|\le K\), the top-eigenvalue difference is at most the
  resolvent norm difference, and inversion costs at most \((\mu+K)^2\).
* For the specified bounded selfadjoint even source \(A_c\),
  \(\|A_c\|,\|A_0\|\le a\), the free CAR orbit moduli obey, for each fixed \(L\),
  \[
  \nu_{X,c}(L)=\sup_{|t|\le L}
    \|\alpha_{c,t}(\widehat X_c)-\widehat{\alpha_{0,t}(X_0)}\|\to0,
          \qquad X=V,A.                                             \tag{4}
  \]
  The bounded cocycle proof in synthesis P40 gives the actual interacting
  observable comparison
  \[
  d_{A,c}(L):=\sup_{|t|\le L}
  \|\beta_{c,t}(\widehat A_c)-\widehat{\beta_{0,t}(A_0)}\|
  \le\nu_{A,c}(L)+2La\nu_{V,c}(L)\to0.                              \tag{5}
  \]
  A direct estimate of the left-hand modulus may be better. Always
  \(d_{A,c}(L)\le2a\). Ordinary compact real \(L^2\) cell averages and finite
  even polynomials supply (4), without a universal rate in \(c\). They do not
  supply (4) uniformly over arbitrary growing windows. The synthesis review
  corrects its local-spin citation: use Local sections 3 and 6, L23-L24,
  rather than attributing that support statement to Local L10.

For the linear ramp from the exact free vacuum, followed by any autonomous
pre-pulse hold, let \(\rho_c\) denote the state at the pulse start. The inherited
preparation bounds are
\[
 \eta_c=\operatorname{Tr}\rho_c F_c\le D_*^2/\tau^2,\quad
 \|\rho_c-P_c\|_1\le2e_\tau,\quad
 \operatorname{Tr}\rho_cG_c\le K,\quad
 \operatorname{Tr}\rho_cH_c\le2K.                                    \tag{6}
\]
Here \(e_\tau=\min(1,C_{\rm ad}/\tau)\),
\(C_{\rm ad}=2K/g^2+31K^2/g^3\), and the unchanged parent constant is
\[
 M_*=\sqrt{m/(m-K)},\quad a_*=K\sqrt{2m-K}/g^2,
\quad b_*=\frac{K^2[\sqrt{30(43m+4K)}+\sqrt{2m-K}]}{g^3},
\quad D_*=(1+M_*)a_*+M_*b_* .                                       \tag{7}
\]
These estimates are uniform in the pre-pulse hold; no comparison over its
duration is needed. For a general normal input of finite form energy use
\[
 \kappa_c=\min(1,\sqrt{\eta_c/g}),\qquad
 \|\rho_c-P_c\|_1\le2\kappa_c.                                     \tag{8}
\]
For the supplied preparation replace \(\kappa_c\) by the smaller of this
quantity and \(e_\tau\). The rank-one gap estimate and pure-reference trace
bound prove (8); they do not assert any reverse energy bound from trace norm.

## 2. Pulse bookkeeping and form-valid scalar controls

The pulse is \(G_c-\epsilon j(t)A_c\), \(0\le t\le T\), with a common fixed
real compact BV profile \(j\) and duration \(T\) throughout the stated limits.
Let \(\nu=Dj\) be its entire zero-extended cyclic derivative,
including endpoint jumps. Write
\[
 J(t)=\int_0^t|j(s)|ds,\quad J=J(T),\quad
 V_j=|\nu|([0,T]),\quad B_j=\int J(t)|\nu|(dt),\quad
 C_j=\int J(t)^2|\nu|(dt),\quad h=|\epsilon|aV_j.                    \tag{9}
\]
All constants remain meaningful if the profile or source is zero. A finite
pulse need not be weak. Denote its propagator by \(U_c(T)\), its ground work by
\(D_c\), and its input-state work by \(W_c\). The BV parents prove preservation
of the common form domain and the bounded polarized work identity. Thus
\[
 W_c=\operatorname{Tr}\rho_c\mathcal T_c,\quad
 \mathcal T_c=-\epsilon\int U_c(t)^*A_cU_c(t)\nu(dt),\quad
 \|\mathcal T_c\|\le h.                                             \tag{10}
\]
The same equality holds for every normal finite-form-energy state: diagonalize
the positive density; each vector of positive weight lies in the form domain.
Apply the vector identity and sum. The nonnegative final form energies have
sum at most \(\eta_c+h\), while the signed bounded term is absolutely summable.
Autonomous holds preserve that finite form sum. No vector in the operator
domain is silently assumed. The final actual excess is
\(\eta_c+W_c\ge0\). In particular \(W_c\ge-\eta_c\), not necessarily zero.

The frozen prepared-pulse result gives
\[
 0\le D_c\le\min(h,2\epsilon^2a^2B_j,h^2/g_e),\qquad
 |W_c-D_c|\le R_c,
\quad R_c=\frac{\eta_c(D_c+h)}g
              +2\sqrt{D_c\eta_c(1+h/g)}.                            \tag{11}
\]
The \(h^2/g_e\) term uses evenness; use \(g\) without that premise. The other
bounds and subsequent theorems do not need that refinement. Its mixed-state
proof splits each form vector into ground and orthogonal parts, estimates the
final form cross term by Cauchy-Schwarz, and sums the resulting direct-sum form
norms. This controls coherent input states and requires no unbounded moment
deduced from \(\|\rho-P\|_1\).

At fixed \(\epsilon\), the finite-pulse comparison and weak-source expansion are
\[
 |D_c-D_0|\le M_c:=4\epsilon^2aB_j[d_{A,c}(T)+ab_c],                 \tag{12}
\]
\[
 D_c=\epsilon^2Q_c+\mathcal R_c,\quad
 |\mathcal R_c|\le2|\epsilon|^3a^3C_j,\quad Q_c\to Q_0.             \tag{13}
\]
Here \(Q_c=\int\omega|\widehat j(\omega)|^2\mu_c(d\omega)\) is the
inherited ground spectral coefficient, with
\(\widehat j(\omega)=\int_0^Tj(s)e^{i\omega s}ds\). The BV filter, not an unfiltered
spectral first moment, makes it finite. Equations (10)-(13) are scalar energy
inputs; they do not themselves imply a complete density limit.

For an autonomous post-pulse hold of duration \(w\ge0\), define
\[
 \rho_c^{\epsilon,w}=e^{-iwG_c}U_c(T)\rho_cU_c(T)^*e^{iwG_c},\quad
 \sigma_0^{\epsilon,w}=e^{-iwG_0}U_0(T)P_0U_0(T)^*e^{iwG_0}.          \tag{14}
\]
Both have finite free form energy; autonomous evolution preserves the
\(G\)-form domain, equivalent to the free form domain under bounded \(V\).
The target is a driven **ground** state, not a continuum preparation at finite
\(\tau\). Section 5 separately compares complete finite protocols.

## 3. Full density from a bounded implementer

Put \(S_c(t)=e^{itG_c}U_c(t)\). Bounded interaction evolution gives
\[
 S_c'(t)=i\epsilon j(t)\beta_{c,t}(A_c)S_c(t),\quad S_c(0)=I,
 \qquad \|S_c(T)-I\|\le|\epsilon|aJ.                                \tag{15}
\]
The norm integral equation lies in the even CAR algebra because its
coefficient is point-norm continuous apart from the scalar BV profile.
Use that CAR equation to define the unital \(\widehat S_c\); its actual
restriction is \(S_c\). It is not the isometric zero extension of \(S_c\).
All unital extensions reduce the actual range. Define
\[
 B_c(w)=\beta_{c,-(T+w)}(S_c(T)).                                    \tag{16}
\]
Stationarity of \(P_c\) gives the exact embedded density identity
\[
 \widehat{e^{-iwG_c}U_c(T)P_cU_c(T)^*e^{iwG_c}}
       =\widehat B_c(w)\widehat P_c\widehat B_c(w)^*.                \tag{17}
\]
The shift of the **whole** interaction equation shows that \(B_c(w)\) is its
time-ordered unitary with coefficient
\(i\epsilon j(s)\beta_{c,s-T-w}(A_c)\). All its orbit times lie in
\([-T-w,0]\). Two unitary bounded evolutions with generators differing by
\(Y_c(s)-Y_0(s)\) differ in norm by at most
\(\int\|Y_c(s)-Y_0(s)\|ds\): differentiate the product of one inverse with
the other, or use the two-sided variation-of-constants identity. Consequently
\[
 \|\widehat B_c(w)-\widehat B_0(w)\|
       \le|\epsilon|Jd_{A,c}(T+w).                                  \tag{18}
\]
There is no operator-norm comparison of unbounded full propagators here.
Insert \(P_c\), use unitary invariance of the trace norm, then (17)-(18):
\[
 \boxed{\ \|\widehat\rho_c^{\epsilon,w}
                 -\widehat\sigma_0^{\epsilon,w}\|_1
       \le\delta_c(w):=\min\{2,\,2\kappa_c+2b_c
                    +2|\epsilon|Jd_{A,c}(T+w)\}.\ }                \tag{19}
\]
For every fixed \(\epsilon,T,W<\infty\), (19) tends to zero uniformly over
\(0\le w\le W\) as \(c\to0\) and \(\eta_c\to0\). In particular it does so
for every \(\tau(c)\to\infty\) and arbitrary pre-pulse waits. This is a full
trace norm assertion, proved from a trace-close ground and norm-close bounded
implementers; convergence of CAR expectations alone would not prove it.

If the desired target strength is fixed \(\epsilon_0\), while the actual
strength is \(\epsilon_c\), first use (19) at matching \(\epsilon_c\), then add
\(2aJ|\epsilon_c-\epsilon_0|\). Formula (19) also applies without taking any
limit and states the finite preparation error explicitly.

## 4. Separate actual free energy

For any density of finite free form energy, boundedness of \(V\) gives the
trace-of-forms identity \(E_G=E_H+\operatorname{Tr}\rho V\). Applying (10),
then the autonomous conservation law, gives exactly
\[
 E_{H,c}^{\epsilon,w}:=\operatorname{Tr}\rho_c^{\epsilon,w}H_c
       =E_{g,c}+\eta_c+W_c
                          -\operatorname{Tr}\rho_c^{\epsilon,w}V_c,
\quad
 E_{H,0}^{\epsilon,w}=E_{g,0}+D_0
                          -\operatorname{Tr}\sigma_0^{\epsilon,w}V_0.
                                                                    \tag{20}
\]
The free energy need not be constant during a \(G\)-hold. Its sum with the
potential expectation is constant. From (3), (11), (12), and (19),
\[
 \boxed{\ |E_{H,c}^{\epsilon,w}-E_{H,0}^{\epsilon,w}|
   \le e_c^{\rm gs}+\eta_c+R_c+M_c+K\delta_c(w)+\nu_c.\ }            \tag{21}
\]
Indeed the last two terms bound the difference of the two bounded potential
expectations on the common carrier. Thus the same fixed-window limits yield
convergence of the **separate actual free expectation**, without imposing an
energy moment on the source or inferring energy convergence from trace norm.
The exact work and ground-energy inputs are essential to this argument.

For the supplied preparation, its stronger initial mean bound gives
\[
 0\le E_{H,c}^{\epsilon,w}\le2K+W_c\le2K+\min\{h,D_c+R_c\},
 \qquad \operatorname{Tr}\widehat\rho_c^{\epsilon,w}Q_H
                                      \le(2K+h)/\Lambda_c.           \tag{22}
\]
The first inequality uses \(\operatorname{Tr}\rho_cG_c\le K\), not merely
\(\eta_c\le D_*^2/\tau^2\). The right side \(2K+W_c\) is necessarily
nonnegative for these inputs. A generic input with initial free mean cap
\(M\) has only \(E_H^{\epsilon,w}\le M+2K+W_c\le M+2K+h\).
Neither bound makes the low Fock carrier compact, nor proves (19) by itself.

For example in the free continuum take normalized even two-particle packets
\(\chi_n\) with mean free energy \(n+O(1)\), each supported in a finite
momentum annulus. Then
\((1-1/n)P_{\rm vac}+n^{-1}|\chi_n\rangle\langle\chi_n|\) tends to the
vacuum in trace norm but its free expectation tends to one. These are normal
finite-form-energy states with a bounded mean cap, not outputs asserted by
the preparation theorem: their excess fails to tend to zero. This elementary
countercontrol explains the role of (20), without weakening (6).

## 5. A stronger finite-protocol comparison at fixed preparation duration

For fixed \(\tau>0\), (19) alone leaves a nonvanishing preparation error
against a ground-input target. There is nevertheless a complete continuum
comparison with the **same finite ramp protocol** under the already supplied
free-orbit premises (4). This assertion does not replace its target by a ground.

Let the total duration be \(L=\tau+w_{\rm pre}+T+w_{\rm post}\), let
\(t_p=\tau+w_{\rm pre}\), and on \([0,L]\) write
\[
 g_\tau(s)=\min(s/\tau,1),\quad
 B_c(s)=g_\tau(s)V_c-\epsilon j(s-t_p)A_c,
 \qquad H_c+B_c(s).                                                  \tag{23}
\]
Here the scalar profile is zero away from its pulse interval. At any prefix
\(t\le L\), the interaction unitary relative to \(H_c\) obeys the bounded
equation with generator \(-i\alpha_{c,s}(B_c(s))\). Shift the whole equation
by \(\alpha_{c,-t}\). Since the free vacuum is stationary and common to all
embeddings, the resulting bounded implementer applied to that vacuum is the
exact full evolved vector, without a phase ambiguity from a changing ground.
Its orbit arguments \(s-t\) lie in \([-L,0]\). The same stability estimate as
(18), and \(\int_0^L g_\tau=L-\tau/2\), yield uniformly at every prefix
\[
 \|\widehat\rho_c(t)-\widehat\rho_0(t)\|_1\le\delta_c^{\rm prot}:=
 \min\{2,\,2[(L-\tau/2)\nu_{V,c}(L)+|\epsilon|J\nu_{A,c}(L)]\}.
                                                                    \tag{24}
\]
The target here is prepared, held, and pulsed at the same finite parameter
values. The finite-ramp parents give the operator-domain and work identity
on the ramp; the BV parents give it on the pulse. Initially \(E_H=0\), so
the final free expectation is exactly
\[
 E_{H,c}(L)=\frac1\tau\int_0^\tau\operatorname{Tr}\rho_c(s)V_c\,ds
  -\epsilon\int\operatorname{Tr}\rho_c(t_p+s)A_c\,\nu(ds)
  -\operatorname{Tr}\rho_c(L)V_c.                                    \tag{25}
\]
All endpoint jumps are in \(\nu\); state continuity makes the displayed
expectations unambiguous at them. There is no final switch-off of \(V\).
Termwise bounded expectation comparison gives
\[
 |E_{H,c}(L)-E_{H,0}(L)|
 \le(2K+h)\delta_c^{\rm prot}+2\nu_c
                    +|\epsilon|V_j\nu_{A,c}(0).                     \tag{26}
\]
Thus every fixed complete protocol has both full density and separate free
energy convergence. The stronger near-ground route (19)-(21) allows arbitrary
long preparation and pre-pulse waits without the factors or windows in (24).
For a growing complete protocol, making the bracket in (24) tend to zero is
another sufficient hypothesis; compact-time convergence alone assigns it no
rate. Equations (24)-(26) use a common exact initial vacuum. Arbitrary initial
states cannot be substituted without their own state and initial-energy data.

## 6. Growing holds: sufficient bounds and an actual failure of trace convergence

For bounded strengths \(\epsilon_c\), (19)-(21) remain valid at any specified
\(w_c\). In addition to vanishing preparation and static errors, the sufficient
new window condition is
\[
 |\epsilon_c|Jd_{A,c}(T+w_c)\longrightarrow0.                         \tag{27}
\]
At a fixed nonzero strength the factor \(|\epsilon_c|J\) can be removed when
\(J>0\). This is a sufficient comparison condition, not a necessary property
of every successful state family. Equation (5) supplies the more explicit
sufficient resource
\(|\epsilon_c|J[\nu_{A,c}(T+w_c)+2(T+w_c)a\nu_{V,c}(T+w_c)]\to0\).
It can be weaker to control the specific bounded implementer than its entire
source orbit. A diagonal choice of sufficiently slow \(W_c\uparrow\infty\)
with \(d_{A,c}(T+W_c)\to0\) exists from compact-time convergence: choose
successive spacing thresholds for integer windows and errors \(1/n\).
No rate or prescribed growing window follows from that argument.

For free energy alone, (20) gives a sharper logical distinction. If its scalar
ground, initial-excess, and pulse-work errors vanish, then convergence at a
growing hold is equivalent to convergence of the **bounded potential
expectation**. Full trace convergence is sufficient for that comparison but
is not necessary. No claim of its failure is inferred solely from a failure
of (27) or of the density comparison.

Here is an actual allowed counterexample to extending the full density theorem
to every growing hold at fixed pulse strength. It uses (1), not an unrelated
finite-level substitute. Set \(V_c=V_0=0\). Preparation and pre-pulse holds
then leave the exact vacuum for every \(\tau\). Use the already checked source
family from the prepared-pulse parent: real normalized smooth compact fields
\(f\) and its sufficiently far translate \(g\), with disjoint supports,
\[
 A_0=i\,c(f)c(g),\quad
 A_c=i\,c_c(C_cf)c_c(C_cg),\quad j=\mathbf1_{[0,T)}.                  \tag{28}
\]
For small \(c\) the two cell supports are disjoint, \(A_c\) is selfadjoint,
even, bounded by one, and has its physical finite-hull spin representative.
The existing ordinary orbit comparison applies. The frozen parent's complete
positive-response proof shows \(Q_0>0\): the pair vector is nonzero and its
energy spectral measure is nonatomic, whereas the rectangle filter has only
discrete zeros. Denote the nonzero filtered pair vector by
\[
 v_j=\widehat j(H_0)(A_0-\langle A_0\rangle_{\rm vac})\Omega,
 \qquad \chi=e^{-iTH_0}v_j\ne0.                                     \tag{29}
\]
The finite pulse vector \(\psi_\epsilon=U_0(T)\Omega\) has a nonzero vacuum
component and a nonzero excited component for every sufficiently small fixed
nonzero \(\epsilon\). Indeed its excited component is
\(i\epsilon\chi+O(\epsilon^2a^2J^2)\) in Hilbert norm by the bounded Dyson
equation, and \(\|\psi_\epsilon-\Omega\|\le|\epsilon|aJ\). This is a norm
expansion only; no energy is inferred from its remainder. For definiteness
the second-order vector remainder is at most \(\epsilon^2a^2J^2/2\), obtained
by inserting the exact unitary in the double integral of (15).

Fix \(t>0\) and choose the autonomous hold \(w_c=t/c^2\). The low dispersion
has, pointwise in fixed \(p\),
\[
 \frac{e_{c,L}(p)-E(p)}{c^2}\longrightarrow
       \phi(p)=\frac{v^2p^4}{8E(p)}.                                \tag{30}
\]
To check the coefficient, \(\sqrt{1-c^2p^2}=1-c^2p^2/2+O(c^4)\), whence
\(e_{c,L}^2=E^2+c^2v^2p^4/4+O(c^4)\); division by \(e_{c,L}+E\) gives
(30). Let \(L_\phi=d\Gamma(\phi)\) on the low Fock space. For
\(q_c=\Gamma(\mathbf1_{I_c})\), the relative low unitary satisfies
\[
 \exp[-iw_c(d\Gamma(e_{c,L})-H_0)]q_c
            \ \xrightarrow[\ c\to0\ ]{\rm strong}\ e^{-itL_\phi}.
                                                                    \tag{31}
\]
The left side means the actual in-band multiplication operator followed by
\(q_c\); it needs no invented outside-band Hamiltonian. On each finite
particle sector this follows by dominated convergence of the modulus-one
multipliers, since every fixed momentum configuration is eventually in-band.
The finite-sector truncations are dense and all operators have norm at most
one, which proves (31) on the whole Fock space. No moment of \(L_\phi\),
or membership of the driven vector in its domain, is needed.

At the pulse end, (18) with \(V=0\) and the common vacuum gives convergence
of the embedded vectors \(\widehat\psi_{c,\epsilon}\to
\psi_\epsilon\otimes\Omega_H\), with an actual fixed phase choice. Therefore
their high component tends to zero; it stays small under the free hold. Their
low part differs from \(q_c\psi_\epsilon\) by a vector tending to zero, an
error whose norm is also preserved during the hold. Using (31), the overlap
of the actual and target held vectors consequently tends to
\(\langle\psi_\epsilon,e^{-itL_\phi}\psi_\epsilon\rangle\). Thus
\[
 \lim_{c\to0}\|\widehat\rho_c^{\epsilon,w_c}
                         -\widehat\sigma_0^{\epsilon,w_c}\|_1
   =2\sqrt{1-|\langle\psi_\epsilon,
                              e^{-itL_\phi}\psi_\epsilon\rangle|^2}>0.
                                                                    \tag{32}
\]
For completeness, strict positivity is not guessed from a formal phase.
The function \(\phi\) is strictly increasing in \(|p|>0\); fixing all other
momenta, a level of \(\sum_{k=1}^n\phi(p_k)\) contains at most two choices of
the remaining momentum. Each non-vacuum sector therefore has an atomless
\(L_\phi\) spectral measure, by Fubini. A nonzero excited component has such
an atomless part. Modulus one of its characteristic function at \(t\ne0\)
would require the measure to be supported on a countable phase level set,
which is impossible. The additional vacuum component is harmless and also
makes the relative-phase interpretation explicit.

This family obeys the prescribed preparation, finite pulse, uniform small
potential bound, ordinary compact-time orbit comparisons, and actual finite
energy conditions. It proves failure of a universal growing-hold full-density
extension. It does **not** prove free-energy failure: here \(V=0\), so
\(E_{H,c}^{\epsilon,w_c}=D_c\to D_0=E_{H,0}^{\epsilon,w_c}\) for all holds.
An actual interacting counterexample to growing-hold free-energy convergence,
or an additional theorem ensuring it without the bounded-potential comparison,
is not supplied by this argument and remains a separate question.

## 7. Weak source: arbitrary holds and the distinction between absolute and relative limits

The isometric shift in (16) preserves (15). For arbitrary post-pulse holds,
including ones beyond every controlled continuum time window,
\[
 \|\widehat\rho_c^{\epsilon,w}-\widehat P_0\|_1
    \le\min\{2,\,2\kappa_c+2b_c+2|\epsilon|aJ\}.                   \tag{33}
\]
The target driven ground has distance at most \(2|\epsilon|aJ\) from its
ground, also uniformly in its hold. Thus if \(\epsilon_c\to0\),
\(\eta_c\to0\), and \(c\to0\), the actual output converges in full trace norm
to the continuum ground uniformly over all pre- and post-pulse holds. It also
converges to the matching weakly driven target at any chosen holds. This is
consistent with (19) and \(d_A\le2a\); no growing-window hypothesis is needed
for this unscaled collapse.

Moreover \(0\le\eta_c+W_c\le\eta_c+D_c+R_c\to0\). Let
\(E_{H,0}^{\rm gs}=\operatorname{Tr}P_0H_0\). Equation (20) gives
\[
 |E_{H,c}^{\epsilon,w}-E_{H,0}^{\rm gs}|
 \le e_c^{\rm gs}+\eta_c+D_c+R_c+\nu_c
           +K\min\{2,2\kappa_c+2b_c+2|\epsilon|aJ\}\ \longrightarrow0.
                                                                    \tag{34}
\]
This too is uniform in arbitrary holds. It is a separate free-energy theorem,
using scalar excess and a bounded potential, not trace convergence alone.

The stronger quadratic **interacting** energy law is the already frozen one:
if \(\eta_c=o(\epsilon_c^2)\), \(\epsilon_c\to0\) through nonzero values,
and \(c\to0\), then
\[
 \frac{W_c}{\epsilon_c^2}\to Q_0,\qquad
 \frac{\eta_c+W_c}{\epsilon_c^2}\to Q_0.                             \tag{35}
\]
It is unaffected by either hold because actual \(G_c\) energy is conserved
there. The supplied ramp has the sufficient scaling
\(\tau(c)|\epsilon_c|\to\infty\). No necessity claim about that particular
ramp follows from the coherent near-ground counterfamilies in the parents.
Referencing \(E_{g,0}\) instead of \(E_{g,c}\) after division by
\(\epsilon_c^2\) additionally costs \(e_c^{\rm gs}/\epsilon_c^2\).

Unscaled convergence (33) is not convergence of the leading driven density.
The free counterexample admits a quantitative weak-source version. For any
nonzero \(\epsilon_c\to0\), keeping \(w_c=t/c^2\), the first-order pulse vectors
converge by (5), their remainders are uniformly \(O(\epsilon_c^2)\), and (31)
gives, after removing the common first-order vacuum phase,
\[
 \frac{\|\widehat\rho_c^{\epsilon_c,w_c}
                   -\widehat\sigma_0^{\epsilon_c,w_c}\|_1}
        {|\epsilon_c|}
       \longrightarrow2\|(e^{-itL_\phi}-I)\chi\|>0.                 \tag{36}
\]
To see the trace coefficient directly, the difference of the two first-order
rank-one projections is \(i\epsilon(|z\rangle\langle\Omega|
-|\Omega\rangle\langle z|)\), with \(z\perp\Omega\), which has trace norm
\(2|\epsilon|\|z\|\). Here \(z=(e^{-itL_\phi}-I)\chi\); its norm is nonzero
by the atomless spectral argument. Time-zero source errors contribute
\(o(|\epsilon_c|)\), not a hidden fixed preparation error, since \(V=0\)
and the initial vacuum is exact. Thus (36) does not contradict (33)-(35).

## 8. Why separate free energy need not have the quadratic work coefficient

Even for the exact ground, bounded potential energy can exchange with free
energy at first order in the source. For a fixed actual model omit its index,
put \(C_w(s)=\beta_{s-T-w}(A)\), and define
\[
 r_1(w)=i\int_0^T j(s)\langle\Omega,[V,C_w(s)]\Omega\rangle ds,
\quad
 r_2(w)=-\int_{0<r<s<T}j(r)j(s)
            \langle\Omega,[C_w(r),[C_w(s),V]]\Omega\rangle drds.
                                                                    \tag{37}
\]
Bounded Dyson expansion of \(B(w)^*VB(w)\), with no unbounded derivative,
gives
\[
 \operatorname{Tr}\sigma^{\epsilon,w}V
     =\langle V\rangle_g+\epsilon r_1(w)+\epsilon^2r_2(w)+O(|\epsilon|^3),
 \quad |r_1(w)|\le2KaJ,\quad |r_2(w)|\le2Ka^2J^2.                  \tag{38}
\]
One sufficient uniform remainder bound is
\(\tfrac43K|\epsilon|^3a^3J^3e^{2|\epsilon|aJ}\), from the absolutely
convergent bounded conjugation series. The signs in (37) follow by expanding
\(B=I+i\epsilon\int jC-\epsilon^2\int_{r<s}j(s)j(r)C(s)C(r)+\cdots\).
The square cross term and its two ordered terms combine to the displayed
nested commutator. Therefore
\[
 E_H^{\epsilon,w}-E_H^{\rm gs}
       =-\epsilon r_1(w)+\epsilon^2[Q-r_2(w)]+O(|\epsilon|^3),        \tag{39}
\]
with a remainder uniform over all holds for the **same model**. The bounded
coefficient orbits may still fail to compare at growing continuum windows.
Free energy, total interacting energy, excess above its ground, and pulse
work are thus different quantities even at leading order.

Nonzero \(r_1\) occurs in an allowed model. Take the ordinary free pair
operator \(B=i c(f)c(g)\) from (28), let \(V=\lambda B\) with
\(0<\lambda<m/4\), and use \(A=V\), with its same cell-average family. This
is a bounded even small potential and source with the required orbit inputs.
Its interacting ground cannot be an eigenvector of \(V\): otherwise it would
be an eigenvector of \(H_0=G-V\) with eigenvalue of absolute value at most
\(2\lambda<m\), hence the free vacuum, contradicting the nonzero pair part
of \(B\Omega\). Accordingly the ground spectral measure \(\mu_V\) of
\((V-\langle V\rangle_g)\Omega_g\) is nonzero and supported above the gap.
For a rectangular pulse and \(w=0\), spectral calculus in the first formula
of (37) gives
\[
 r_1(0)=2\int\frac{1-\cos(T\omega)}\omega\,\mu_V(d\omega)>0          \tag{40}
\]
for almost every \(T>0\). Fubini proves the last assertion: for each positive
\(\omega\), its zero times are discrete. This proof does not require an
unfiltered energy moment of \(V\Omega_g\). It provides an actual obstruction
to identifying the separate free response with the quadratic work law (35).

For a general near-ground input at the same model and strength, comparing
absolute final free energies to the driven ground yields the uniform bound
\[
 |E_{H,\rho}^{\epsilon,w}-E_{H,g}^{\epsilon,w}|
        \le\eta+R+2K\kappa.                                        \tag{41}
\]
Thus \(\eta=o(\epsilon^2)\) alone controls interacting quadratic response but
does not make this bound negligible relative to \(\epsilon^2\). The stronger
sufficient requirements \(\kappa=o(\epsilon^2)\) and
\(\eta=o(\epsilon^2)\) do so. They are met, for example, by
\(\eta=o(\epsilon^4)\) or the ramp scaling \(\tau\epsilon^2\to\infty\).
They are not claimed necessary for any specific ramp. At \(K=0\) the
potential term vanishes and that stronger requirement is unnecessary.

There is a useful weaker comparison if one subtracts the **same input's
no-pulse evolution** at the same total hold time. Write
\(\Delta H_\rho=E_{H,\rho}^{\epsilon,w}-E_{H,\rho}^{0,w}\), and similarly
for a ground input. In the pulse interaction picture the potential difference
is \(S^*\beta_{T+w}(V)S-\beta_{T+w}(V)\), with norm at most
\(2K|\epsilon|aJ\). The interacting energy difference is exactly \(W_\rho\),
so
\[
 |\Delta H_\rho-\Delta H_g|
             \le R+4K|\epsilon|aJ\kappa.                            \tag{42}
\]
Now \(\eta=o(\epsilon^2)\) suffices for an \(o(\epsilon^2)\) preparation
error. The linear term and the distinct quadratic coefficient in (39) still
remain. Equations (41)-(42) distinguish absolute expectation from a matched
response; neither grants relative continuum rates automatically. For example,
using a continuum \(r_{1,0}\) in place of a spacing-specific \(r_{1,c}\) after
quadratic normalization additionally requires
\(r_{1,c}-r_{1,0}=o(|\epsilon_c|)\). Absolute static reference energies and
potential expectations likewise need their own errors small on that scale.

## 9. Disposition and exact scope

The established conclusions are the full density estimate (19), the separate
free-energy estimate (21), the finite complete-protocol estimates (24)-(26),
the sufficient growing-window condition (27), the actual density failures
(32) and (36), and the arbitrary-hold weak-source collapse (33)-(35).
Equations (37)-(42) identify which free-energy response is being measured and
which preparation or comparison errors would have to be resolved on a
quadratic scale. No trace or energy conclusion is attributed to CAR state
convergence alone.

No new smoothness, source energy-transfer moment, spatial compactness, or
operator-norm convergence of full propagators is needed for the fixed-time
claims. The actual embeddings, static ground trace/energy comparison, bounded
work identity, and specified orbit comparisons are genuine inputs. The latter
are already supplied for the ordinary cell class, but cannot be silently
replaced by time-zero convergence in a general varying-potential class.

Unresolved beyond the claims proved here: a prescribed growing-window rate
for general compact \(L^2\) data; an interacting actual-model obstruction or
general theorem for separate free-energy convergence when only its growing
bounded-potential expectation remains uncontrolled; and necessary scaling for
the specific linear-ramp preparation on any relative response scale. These
are not inferred from the free density counterexample or from general coherent
near-ground state families. Formal retained status and a source-exposed root
comparison remain outside this independent freeze.

Scientific parents, all previously read completely and reverified unchanged:

| Parent | SHA256 |
|---|---|
| BV_PULSE_WORK_INDEPENDENT.md | `0af3a48b0604b6dfd530dfc901d81e789a89ef65b89d43391ed351f6f0ac95d9` |
| BV_PULSE_WORK_CROSSCHECK.md | `741b3d4a73f2091768087b5cf4e3a004980632a6644eda6a19e9247164ba32b3` |
| ADIABATIC_PREPARATION_SYNTHESIS.md | `6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c` |
| ADIABATIC_PREPARATION_SYNTHESIS_REVIEW.md | `fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245` |
| PREPARED_PULSE_ROBUSTNESS_INDEPENDENT.md | `0096ba164586386693fe506863da477224d1327febe6afbe861bd70417a4ea68` |
| PREPARED_PULSE_ROBUSTNESS_CROSSCHECK.md | `3fe0db39de48bfe029c1d83d90ec7530fa0c25d49b489bad10625eba726fa1e1` |
| PREPARED_PULSE_ROBUSTNESS_ROOT_PROBE.md (old, authorized) | `cbcb38dff74b37dbb1612c223b74feee1e2bd8bc74cf19f74c0e47af1997bc8d` |

The two old independent/core freezes remain unchanged. Their instruction and
canonical-premise evidence is reused at recorded identities. No new external
source was required; this source-bounded symbolic derivation makes no claim
of a new literature review. The only scientific source reread in this phase
was the already authorized synthesis, targeted at its carrier and orbit
premises. The complete final note is author-read before freezing; that is
coverage, not an independent adjudication of its conclusions.


## Publication provenance and dependency scope

The installed [evidence map](../.claude/science/physics-loops/toe-energy-protocol-20261012/EVIDENCE_MAP.json)
indexes every accepted source-package member and all 211 original aliases.
The original/copy manifests, correction records, complete source diffs,
line-piece map and canonical-parent history remain losslessly archived.
The [publication map](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_EDITS.json)
records every new wrapper substitution and full publication diff. All four
accepted scientific bodies retain their exact bytes, including the two
previously accepted wording corrections. No further body edit is made.

The [source review](../.claude/science/physics-loops/toe-energy-protocol-20261012/ENERGY_PROTOCOL_SOURCE_ROOT_REVIEW.json)
and [root reconstruction](../.claude/science/physics-loops/toe-energy-protocol-20261012/ENERGY_PROTOCOL_SOURCE_ROOT_RECONSTRUCTION.json)
state the actual earlier read and mechanical coverage. The distinct
[publication acceptance](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_ROOT_ACCEPTANCE.json)
and [publication review](../.claude/science/physics-loops/toe-energy-protocol-20261012/PUBLICATION_ASSEMBLY_REVIEW.txt)
must be supplied by root before guarded integration can install this note.
The [identity tool](../scripts/prepared_driven_state_identity_2026_10_13.py) checks source bytes and reconstruction
only, with zero mathematical predicates. Its cache is integration evidence,
not a proof, analytic formal check, new independent review or audit.

The canonical source dependencies are the supplied [Current](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Concrete](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[Local](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[bounded interaction and ground](BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[preparation](ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md),
[response](EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md).
Energy-transfer sources remain inherited through their named parent roles;
time averaging belongs to the separate graph-energy argument.
`ACCEPTED_DEPENDENCY_MAP.json` in the installed packet distinguishes their actual roles for each source body.
In particular, time averaging is used by the graph-word argument; it is not
a premise of the driven-state theorem. The latter uses the BV body in the
paired [BV/graph note](BV_GRAPH_ENERGY_PROTOCOL_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and the complete prepared-pulse body above. That source-role statement does
not import every theorem in a cited combined note.

The finite-energy pulse core and comparison remain explicitly archived
provisional inputs; no absent canonical pulse note is silently replaced by
the different finite-energy sector-selection note. Local sections 3 and 6,
especially L23-L24, supply physical cell support; L18 fixes the field
normalization. Historical Local L10 support attributions in inherited sources
are corrected only in their already identified published copies or records.

The task used the checkout reported by root as clean at
`4ff0ff1d7868b24d7854428110512daed13530f9`, branch
`physics-loop/toe-energy-protocol-20261012`, stacked on regular PR9506.
Root reported main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`.
The source and publication-preparation workers ran no Git commands.
Exact file hashes were checked. Root execution must separately verify the
branch, exact base, clean state, parent identities and frozen source bytes. Front-matter dependency traversal
records the transitive source graph; it is not a complete proof or audit of
that graph. Existing parent status text and formal appendices confer no new
analytic verification on these arguments.

The supplied dynamics, representation, state/control/readout prescriptions,
actual gaps, support restrictions and stated convergence resources remain
hypotheses. Every counterexample retains its original actual-model or abstract
scope. No new low-block, phase-space/escape, energy-distribution/weighted-trace,
smooth-high-band or checkpoint/queue contents are included in this assembly.
The graph/native correction record is archived whole for byte preservation;
only its graph wording item 2 changes a selected body here.

At publication-preparation freeze, no scientific, numerical, symbolic or
formal program, proposed identity tool or publication driver had been run.
No checkout, checkpoint, queue, editable prompt, axiom, Git/PR or audit surface
was changed by either worker. The guarded program and new publication wrappers
require root review of their exact bytes before execution. Later execution
records report actual integration outcomes; formal retained status remains
with the independent audit path.

---
claim_id: initial_cube_energy_layer_and_exact_band_balance_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Original compensated cube from canonical N=4 input: initial epsilon^2 energy layer, uniform matched
  rare density and moments, exact coherent band balance, and fixed-C1 distributional net drift with an initial boundary
  contribution. No pointwise power, heat/work identification, physical selection or apparatus resource conclusion.'
upstream_dependencies:
- actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- full_original_cube_ensemble_energy_and_rare_matter_field_density_bounded_theorem_note_2026-09-24
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- minimal_axioms
- ordinary_microscopic_cube_energy_after_the_birth_layer_bounded_theorem_note_2026-09-24
- sharp_actual_rotor_cube_energy_tail_bounded_theorem_note_2026-09-24
runner: scripts/initial_cube_energy_layer_and_exact_band_balance_2026_09_24.py
---

# The initial cube energy layer and exact band balance

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

The full original cube's positive-time energy limit has a finite excess
which is absent at the prepared initial time. This note resolves its
epsilon^2 onset, gives one matched rare-density and moment approximation
on the entire fixed interval [0,T], and keeps the initial contribution in
the exact system-energy drift. The limit is conditional on the supplied
compensated model and canonical preparation; it does not select them.

The root sealed an initial-profile/band-balance argument before PRE.
The independent PRE added the uniform matched scalar expression, sharp
matching criterion, exact initial derivative and profile coefficients.
POST checked the released density and positive-carrier claims and clarified
that the exact coherence-containing loss has only a distributional scaled
limit here. A later root addendum extends the matched expression to the
trace-norm density using those already disclosed estimates; its final
review is a released-source check, not another blind reconstruction.

## 1. Fixed premises and provisional inputs

Fix delta,K,kappa,T>0. Keep the lambda=0 compensated cube with
A=(0,3,5,6), B=(1,2,4,7), twelve oriented A-to-B edges, hard-core
q=0,+1,-1 and div E=q-1_A. Take integer S to infinity with
epsilon^2 S(S+1)=delta/K. At every finite S use the original Hermitian

    H_e=delta epsilon^-4(W+epsilon T_S+epsilon^2 C_S),
    T_S=-(F_S+F_S*),
    C_S=P(F_S*F_S+D/[S(S+1)])P,  P=1_(W=0),

with the original sector definitions and gated compensation. The terminal
N=8 Hamiltonian is exactly zero as in the parent. The complete resolved
instrument has L_i=sqrt(kappa) epsilon^-1 j_i; the complete coherent
instrument retains j_++j_- inside each edge output. No field-only
postbirth restriction or replacement of coherent recycling is made.

Start from the canonical Hermitian low state U_(4,e)Omega, where Omega
has all A sites occupied by +1 and zero electric field. The full trace-one
ensemble retains N=4, N=6 and terminal N=8. Physical energy always means
the Hermitian H_e, not a no-event eigenvalue. Write m_e=Tr(H_e rho_e),
M2_e=Tr(H_e^2 rho_e), and v_e=M2_e-m_e^2.

Sources: [full ensemble energy and rare density](FULL_ORIGINAL_CUBE_ENSEMBLE_ENERGY_AND_RARE_MATTER_FIELD_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-24.md), [actual fast birth](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md), [local common limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md), [bounded compensation](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md), [ordinary postbirth energy](ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md), [sharp rotor tail](SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md). The full-energy parent is PR9109 at 28965d2737ee32b01bba972273fa51d399c594e4, stacked on PR9104/9057/9049. These are provisional conditional inputs, not independently retained audit conclusions.

## 2. Exact decomposition and the imported estimates actually used

Write V_(N,e)(t)=exp[t(-iH_(N,e)-kappa Gamma_(N,S)/(2epsilon^2))] and

```
chi4,e(s)=V_(4,e)(s) U_(4,e) Omega,
v_i,e(t,s)=V_(6,e)(t-s) j_i chi4,e(s),
rho6,e(t)=kappa epsilon^-2 sum_i integral_0^t
                         |v_i,e(t,s)><v_i,e(t,s)| ds.       (1)
```

These are unnormalized vectors and the actual first-birth intensity; there
is no division by a selected mark probability. Every birth increases N by
two. Thus the full energy moments consist exactly of the N=4 no-event
moment plus the N=6 source integral, with zero terminal moment.

Let P^H_(N,r) be the exact Hermitian cluster projector, V_N^H the canonical
all-cluster unitary, J_N the exact no-event Riesz intertwiner, and
a4,e(s)=Pi0 J_4^-1 chi4,e(s). Define

```
B_i=j_i F P4,                 R_i=(j_i F^2/2-F j_i F)P4,
R_i=-F_a j_i F_a P4           for a mark centered at a,
H_rot,N=K D_N-delta Z_N*Z_N/2,
u4(t)=exp(-24 kappa t) exp(-it H_rot,4) Omega,
L=-i delta G_1-kappa Gamma_1/2,
G_1=Pi1(FF*-F*F)Pi1,          Gamma_1=2 P_bright.            (2)
```

All rotor operators act on the complete physical charge/field space. In
particular L is not a chosen Fourier fiber. Put

```
S(tau,t)=sum_i ||exp(tau L) R_i u4(t)||^2,
I(t)=integral_0^infinity S(tau,t) d tau,
J(tau)=integral_0^tau S(u,0) du.                            (3)
```

The provisional full-energy parent gives a continuous bounded low ensemble energy E_low(t),
defined by the full low-ensemble source integral in that parent, and convergence of all microscopic low means
to it uniformly on [0,T]. Its N=4 high mean and N=6 second-high mean are
O(epsilon^2), uniformly there. All contributions to epsilon^4 M2 except
the N=6 first high band vanish uniformly. Its total ordinary mean is uniformly
bounded on [0,T]. These are estimates in its proof, not merely its headline
positive-time conclusion.

More specifically, its uniform source and age-tail estimates supply

```
r_i,e(s)=R_i,S a4,e(s) -> R_i u4(s), uniformly for 0<=s<=T,
y_i,e,1(t,s)
 =epsilon^2 exp[-i delta(t-s)/epsilon^4]
       exp[((t-s)/epsilon^2) A_e] r_i,e(s)+O_T(epsilon^4),   (4)
```

where y is the exact Hermitian first-high coordinate, A_e is the exact
phase-removed first-high no-event block, and the remainder is uniform on
the complete birth-time triangle. For every cutoff R>=1 the squared norm
integral of the principal fast-age term above R is bounded by

```
C_T(1+R)^(-3/2)+C_T epsilon^(1/2),                         (5)
```

uniformly in t in [0,T], whenever that tail is present. Its integral from
zero is uniformly bounded. The rotor tail has the analogous first term.
This imports a proved growing-age comparison and tightness estimate; no
compact-time approximation is extended by substitution to age t/epsilon^2.

## 3. Uniform matched expression including time zero

Define the truncated rotor integral

```
I_tr,e(t)=integral_0^(t/epsilon^2) S(tau,t) d tau.            (6)
```

Then, uniformly for 0<=t<=T,

```
m_e(t)=E_low(t)+kappa delta I_tr,e(t)+o(1),
epsilon^4 M2_e(t)=kappa delta^2 I_tr,e(t)+o(1),
epsilon^4 v_e(t)=kappa delta^2 I_tr,e(t)+o(1).              (7)
```

Here o(1) is an absolute error; no relative error at a shrinking or vanishing
profile is asserted.

Proof: from (4), change variables s=t-epsilon^2 tau and divide the first-high
vector by epsilon^2. The normalized error has norm O(epsilon^2); its squared
integral over at most T/epsilon^2 is O(epsilon^2). The principal term has
bounded squared integral, so its cross term with this error is O(epsilon).
Thus the normalized first-high source mass differs by o(1) from the integral
of ||exp(tau A_e)r_i,e(t-epsilon^2 tau)||^2.

On each bounded age interval this integrand converges uniformly to S(tau,t)
on the restricted triangle 0<=epsilon^2 tau<=t<=T. This follows from the
strong bounded-generator convergence and uniform convergence of sources,
plus uniform continuity of u4; no lower bound on t is used. Split at R.
Use this compact convergence below R and (5) and its rotor counterpart above
R. First send epsilon to zero, then R to infinity. This proves the uniform
comparison with (6), including intervals whose upper age is less than R.

The exact Hermitian high Hamiltonian is
`H_(6,e,1)=delta epsilon^-4[I+O(epsilon^2)]`. Hence its mean equals kappa
delta times this normalized mass up to o(1), and epsilon^4 times its second
moment equals kappa delta^2 times it. The imported remaining-band estimates
give the first two statements in (7). Uniform boundedness of m_e gives the
last one. This proof uses Hermitian spectral separation; it never calls
the no-event eigenvalues physical energies.

## 4. Initial layer, matching and noncommuting limits

The local compensation formula gives

```
E0=E_low(0)=<Omega,H_rot,4 Omega>=-84 delta,
m_e(0)->E0.                                                (8)
```

Indeed D_4 Omega=0 and ||Z_4 Omega||^2=168. For every finite U, uniformly in
0<=tau<=U, equation (7) gives

```
m_e(epsilon^2 tau) -> E0+kappa delta J(tau),
epsilon^4 M2_e(epsilon^2 tau), epsilon^4 v_e(epsilon^2 tau)
                         -> kappa delta^2 J(tau).          (9)
```

The source identities sum_i R_i*R_i=72I and Gamma_1<=2I give

```
S(0,0)=72,
S(tau,0)>=72 exp(-2 kappa tau),
I(0)>=36/kappa.                                           (10)
```

In particular J is increasing and J(infinity)=I(0)>0. The actual-input
sharp-tail theorem, summed over cube-related edges and the appropriate
original marks, gives

```
I(0)-J(tau)=Theta((1+tau)^(-3/2)).                         (11)
```

This is a two-sided order statement about the limiting initial profile,
not an asymptotic prefactor or a finite-spin relative estimate. The original
dark-source identity Gamma_1 R_i Omega=0 and the actual-birth cubic formula
also give, taking the rotor/compact-time limit first,

```
S(tau,0)=72-576 kappa delta^2 tau^3+O(tau^4),
J(tau)=72 tau-144 kappa delta^2 tau^4+O(tau^5).              (12)
```

These constants preserve the coherent source vectors. The equal total
coefficient 72 alone does not identify the entire resolved and coherent
curves I(t).

The same uniform argument covers moving observation times tending to zero:
if t_e/epsilon^2 tends to tau in [0,infinity), (9) holds with that tau;
if t_e/epsilon^2 tends to infinity while t_e tends to zero, its limits are
`E0+kappa delta I(0)` and `kappa delta^2 I(0)`. The latter follows by the
same compact-age/tight-tail split, not by applying (9) at an unbounded tau.

For each fixed t>0 the imported limit is

```
m_+(t)=E_low(t)+kappa delta I(t).
```

Its continuous right extension to t=0 has value E0+kappa delta I(0), whereas
the microscopic initial means tend to E0. The jump is

```
DeltaE_initial=kappa delta I(0)>=36 delta>0.                (13)
```

Thus the positive-time limit cannot hold uniformly down to zero. Conversely
m_e converges to m_+ in L^p(0,T) for each finite p>=1: convergence is uniform
away from zero and there is a common bound on [0,T]. The corresponding scaled
second moment and variance converge in every such L^p to kappa delta^2 I(t).
No L-infinity convergence on the full initial interval is implied.

More precisely, for lower endpoints 0<=a_e<=T, convergence to these
positive-time limit functions is uniform on [a_e,T] if and only if
a_e/epsilon^2 tends to infinity. Sufficiency follows from (7) and the uniform
rotor tail bound C_T(1+a_e/epsilon^2)^(-3/2). If this ratio does not tend to
infinity, a subsequence has a_e/epsilon^2 tending to a finite tau; at that
endpoint the missing high contribution tends to kappa delta[I(0)-J(tau)]>0,
and to kappa delta^2[I(0)-J(tau)] for the scaled second moment or variance.
This criterion concerns the full ensemble initialized before any birth.
The separate normalized N=6-start theorem has a different initial state and
does not supply this continuous-injection layer.

Neither (9) nor (12) supplies a relative asymptotic on every faster shrinking
time scale. In particular an absolute o(1) remainder cannot be divided by
an arbitrarily small tau_e. No limit with kappa tending to zero or T tending
to infinity is taken. H is not nonnegative, so (13) is a positive excess
above the initial/low mean, not a claim that the total mean is positive.

## 5. Exact net system-energy drift

At each finite spin define the exact GKLS drift P_e(t)=d m_e(t)/dt. Because
H_e is time independent, its Hamiltonian commutator contributes zero:

```
P_e(t)=kappa epsilon^-2 sum_i Tr[
  (j_i* H_e j_i - {j_i* j_i,H_e}/2) rho_e(t)]
 =kappa/(2epsilon^2) sum_i Tr[
  (j_i*[H_e,j_i]+[j_i*,H_e]j_i) rho_e(t)].                  (14)
```

These are exact identities for the complete ensemble. They retain both
first and second original births. In particular, the N=6-to-N=8 gain has
zero final Hamiltonian energy, while the N=6 anticommutator term remains.

An equivalent bare-operator identity helps expose possible cancellations.
Let D_j^* X denote the sum of the jump adjoints without kappa/epsilon^2.
Since [W,j_i]=-j_i and [W,Gamma]=0, D_j^* W=-Gamma. Therefore

```
P_e=kappa delta epsilon^-6[
 -Tr(Gamma rho_e)+epsilon Tr((D_j^*T_S)rho_e)
                         +epsilon^2 Tr((D_j^*C_S)rho_e)].   (15)
```

One cannot retain the W term or the injection term alone and call it net
energy drift. The compensation and hopping contributions are part of the
same exact Hermitian energy observable.

There is an independently justified initial derivative, stronger than merely
differentiating (9):

```
P_e(0)=72 kappa delta epsilon^-2+O(1).                     (16)
```

For proof, the initial selected first-high coordinate of j_i U4 Omega is
epsilon^2 R_i,S Omega+O(epsilon^4), and its high Hamiltonian center is delta
epsilon^-4. This gives total high injection 72 kappa delta epsilon^-2+O(1);
the zero-field squared R coefficients are exact at every integer S>=1.
The selected low coordinates are epsilon B_i,S Omega+O(epsilon^3), with
bounded low energy-vector action after division by epsilon, so their injection
is O(1). The second-high source gives at most O(1) here. Finally the initial
state and H applied to it both lie in the exact Hermitian low band. There
the compressed Gamma is O(epsilon^2), while the prepared energy-vector norm
is bounded by the weighted low expansion. Its anticommutator contribution
after the epsilon^-2 rate factor is O(1). This proves (16) without exchanging
a derivative and the compact-time limit.

## 6. Justified limits of the net drift

The limiting functions I and E_low are C^1 on every [0,T] for this finite-word
preparation. For I, use the weighted propagation argument at the fixed weight
w^4, w=1+sum E_e^2. The rotor u4'(t)=(-iH_rot,4-24kappa)u4(t) has a common
w^3 bound because H_rot,4 is diagonal quadratic plus bounded finite shifts.
Apply the imported smooth-source tail estimate to R_i u4 and R_i u4'. Their
norm product is bounded by C_T(1+tau)^(-5/2), so dominated differentiation
of (3) is justified. This uses only two fixed weights, not a common analytic
radius for all weights. For E_low, the no-event low energy derivative is
the Gamma_B anticommutator form. Bounded finite-hop Gamma_B preserves the
diagonal energy domain; the common weighted energy-vector bounds control
this form on the compact source-time triangle. Differentiating its source
integral is therefore legitimate. This also follows by graph-norm Duhamel.

For every C^1 test function phi on [0,T], the exact integration by parts and
the L^1 mean convergence give

```
integral_0^T phi(t) P_e(t) dt
 -> integral_0^T phi(t) [E_low'(t)+kappa delta I'(t)] dt
                           +kappa delta I(0) phi(0).      (17)
```

Indeed the finite-spin expression is
phi(T)m_e(T)-phi(0)m_e(0)-integral phi' m_e. Use positive-time convergence at
T, (8), and L^1 convergence, then integrate the C^1 right-limit function.
The initial boundary term is essential. Equivalently the net drift tends,
in this distributional sense, to m_+' plus an atom of weight (13) at zero.

For phi=1 this recovers the exact integrated energy change:

```
integral_0^t P_e(s) ds
 -> E_low(t)-E0+kappa delta I(t),             t>0 fixed.   (18)
```

On an interval bounded away from zero the analogous limit is simply the
difference of m_+ at its endpoints. Equations (17)-(18) do not prove pointwise
convergence of P_e, an L^1 bound on its absolute value, or weak convergence
against every continuous test function. No uniform total-variation bound for
these signed drift measures has been established here. A distributional
limit with a measure as its limit does not by itself supply that stronger
measure topology. Nor does uniform convergence of differentiable means on
positive intervals justify differentiating them pointwise.

## 7. Exact first-high gain and loss, with no coherence discarded

Extend Hband_e=H_(6,e)P^H_(6,1) by zero to the other record sectors and write
a_e(t)=Tr(Hband_e rho_e(t)). This is the actual Hermitian first-high energy,
not its scalar-center replacement. It is nonnegative for small epsilon,
uniformly bounded on [0,T], and a_e(0)=0. Define

```
G_e(t)=kappa epsilon^-2 sum_i Tr[
                       Hband_e j_i rho4,e(t) j_i*],
L_e(t)=kappa/(2epsilon^2) Tr[{Gamma_(6,S),Hband_e} rho6,e(t)].   (19)
```

Because Hband_e commutes with the exact Hamiltonian and the next birth is
terminal, the exact band balance is

```
a_e'(t)=G_e(t)-L_e(t).                                    (20)
```

The gain G_e is nonnegative. The term called loss in (19) is the full real
anticommutator contribution. In Hermitian band coordinates it includes
the off-diagonal blocks Gamma_(1,r) rho_(r,1), r!=1. It has not been replaced
by a positive diagonal block. Positivity of Hband_e and Gamma alone does not
make their anticommutator positive. For example A=diag(0,1), Gamma=[[1,1],[1,1]]
and the pure vector (sqrt(.99),-.1) give Re Tr(A Gamma rho)=-.0894987... .
This finite example does not assert negativity on the actual cube trajectory;
it identifies why a general positivity shortcut is invalid.

The uniform source expansion at zero age in (4), the exact high Hamiltonian
center and sum_i R_i*R_i=72I imply

```
epsilon^2 G_e(t) -> g(t)=72 kappa delta exp(-48 kappa t),   (21)
```

uniformly on [0,T]. No normalization by survival or birth probability is
made. Specifically G_e=kappa delta epsilon^-2 sum_i||R_i,S a4,e(t)||^2+O_T(1),
and the source norm sum converges uniformly to 72||u4(t)||^2.

Using only the exact balance (20) and bounded a_e, for every C^1 phi,

```
epsilon^2 integral_0^T phi(t) L_e(t) dt
                       -> integral_0^T phi(t) g(t) dt.    (22)
```

To prove it, subtract the same expression for G_e; the difference is
epsilon^2 times [phi(T)a_e(T)-phi(0)a_e(0)-integral phi' a_e], which vanishes.
For each fixed interval [a,b] subset [0,T] the scaled integrals of G_e and
L_e likewise both tend to integral_a^b g. This conclusion does not require
or claim nonnegativity of L_e, pointwise loss convergence, or a uniform
absolute-variation estimate.

The unscaled difference has the separate boundary-sensitive limit

```
integral phi(t)[G_e(t)-L_e(t)]dt
 -> kappa delta integral phi(t)I'(t)dt
                            +kappa delta I(0)phi(0).     (23)
```

Here a_e tends to kappa delta I away from zero, to zero initially, and is
uniformly bounded; the proof is the same integration by parts as (17).
Thus individually large leading band terms balance in the tested sense,
while leaving both a finite evolving high-energy contribution and its
initial boundary contribution. It is not valid to integrate just the large
gain as energy permanently retained by the system.

On the initial-layer clock, a_e(epsilon^2 tau) tends uniformly on compact
intervals to kappa delta J(tau). Consequently, on that clock,

```
epsilon^2 G_e(epsilon^2 tau) -> 72 kappa delta uniformly,
epsilon^2 L_e(epsilon^2 tau)
                  -> kappa delta[72-S(tau,0)] weakly,
epsilon^2 [G_e-L_e](epsilon^2 tau)
                  -> kappa delta S(tau,0) weakly.         (24)
```

“Weakly” in (24) means integration against C^1 functions on a fixed compact
tau interval, using (20) and the uniform primitive convergence. No atom is
present in this resolved initial clock because J(0)=0. A pointwise
microscopic loss-rate limit would need additional estimates; it has not
been inferred by differentiating the limiting profile. At the exact initial
time L_e(0)=0 and G_e(0)=72 kappa delta epsilon^-2+O(1), consistent with (16).


## 8. Uniform matched trace-norm density

Let U1,e=V6^H Pi1 be the canonical first-high isometry, and zero extend
its pulled-back coordinate densities into the common physical rotor space.
Define the limiting positive-time and initial profiles explicitly by

    Sigma(t)=kappa sum_i integral_0^infinity
       |exp(tau L)R_i u4(t)><exp(tau L)R_i u4(t)| d tau,
    Sigma_init(tau)=kappa sum_i integral_0^tau
       |exp(v L)R_i Omega><exp(v L)R_i Omega| dv.

Use the same original compensated cube, canonical input and scaling.
Let y_i,e,1(t,s) be the canonical Hermitian first-high coordinate of the raw
j_i first-birth path, with the prefactor kappa epsilon^-2 outside its density
integral. On 0<=tau<=t/epsilon^2 put

    f_i,e(t,tau)=epsilon^-2 exp(i delta tau/epsilon^2)
                      y_i,e,1(t,t-epsilon^2 tau),
    f_i,tr(t,tau)=exp(tau L) R_i u4(t).

Set both vectors to zero outside that interval and define

    Sigma_tr,e(t)=kappa sum_i integral_0^(t/epsilon^2)
       |exp(tau L)R_i u4(t)><exp(tau L)R_i u4(t)| d tau.

Then, uniformly for 0<=t<=T,

    ||epsilon^-4 U1,e* rho6,e(t) U1,e-Sigma_tr,e(t)||_1 ->0. (A1)

All coordinates are embedded in the same first-high physical rotor space.
Proof: the inherited uniform source remainder gives an O(epsilon^2) error
in f_i,e, with squared-age integral O(epsilon^2). The principal exact
profile has the common tail bound C_T(1+R)^(-3/2)+C_T epsilon^(1/2)
uniformly on the entire physical-time triangle. The truncated rotor profile
has the corresponding tail bound. Below a fixed R, uniform strong convergence
of the bounded fast generators, uniform source convergence and uniform
continuity of u4 give convergence uniformly on
0<=epsilon^2 tau<=t<=T, including t=0. Both profiles are zero outside this
same triangle; no discontinuity comparison of different cutoffs occurs.
Split at R, take epsilon->0, then R->infinity. This proves the uniform L2
vector comparison. The norm sums are uniformly bounded, so the integrated
rank-one inequality |||f><f|-|g><g|||_1 integrated <=
||f-g||_L2(||f||_L2+||g||_L2) proves (A1).

At t=epsilon^2 tau in a compact tau interval, (A1) gives the initial profile
Sigma_init(tau) by uniform continuity of u4 at zero. At any fixed positive
time its truncated upper limit can be removed by the rotor tail, giving
the parent Sigma(t). The latter step is uniform down to a_e precisely when
a_e/epsilon^2->infinity, as already shown for the scalar trace in section 4.
For density necessity, the missing tail is positive and its trace equals
its trace norm, so the same positive scalar gap applies at a finite-ratio
subsequence. This is an absolute matched statement, not a relative one on
every more rapidly shrinking clock or every additionally magnified observable.


## 9. A positive diagonal carrier and the full coherent loss

Let U1,e be the canonical first-high isometry used above and let
rho_high,e=U1,e* rho6,e U1,e. Set

    Ghat_e=U1,e* Gamma6,e U1,e,
    D_e(t)=kappa delta epsilon^-6 Tr(Ghat_e rho_high,e(t)). (C1)

This carrier is nonnegative. On every fixed positive compact time interval,
the preceding trace-norm density limit and uniformly bounded strong
convergence Ghat_e->Gamma1 give

    epsilon^2 D_e(t) -> kappa delta Tr(Gamma1 Sigma(t))
                     =72 kappa delta exp(-48 kappa t).   (C2)

To justify the expectation limit, approximate each trace-class Sigma(t)
by finite rank and use the common operator bound; compactness of the
continuous trace-class curve makes this uniform in t away from zero.
The canonical rotation tends to identity and the original finite-spin
loss converges strongly, which proves the stated convergence of Ghat_e.

The parent's frozen-source identity
L Sigma+Sigma L*=-kappa sum_i |R_i u4(t)><R_i u4(t)|
is legitimate in trace class. Taking its trace gives Tr(Gamma1 Sigma)=72S4
and Tr(P_bright Sigma)=36S4. This is an age balance with t fixed, not a
replacement for the physical-time identity in section 7.

The diagonal part of the exact L_e differs from D_e by O_T(1): its high
Hamiltonian differs from delta epsilon^-4 I by O(epsilon^-2), its density
has trace O(epsilon^4), and the loss rate is O(epsilon^-2). Its off-diagonal
interband terms are still present in L_e and have no pointwise estimate
here. Therefore (C2) does not make the exact L_e nonnegative or establish
its pointwise convergence. The gain and diagonal carrier are positive;
the exact coherent loss has the scaled integral/distributional limit (22).

The net GKLS drift is a change of system Hamiltonian expectation. Neither
the gain, exact loss, carrier nor initial boundary contribution is called
heat, work, reservoir consumption or a physical supply bill. Those require
an implementation and its energy observables. Pointwise power convergence,
uniform total variation and convergence against all continuous tests remain
unproved. Fixed C1 tests and absolute matched profiles are the scope here;
growing test norms or additional magnifications require additional error rates.

## 10. Computation and review limits

The self-contained primary embeds the disclosed independent primitive-word
control and the root's separate three-state cascade. This is explicit reuse,
not a fresh blind independent computation. The primitive code checks Gauss
after every hop, all 24 resolved and 12 coherent zero-field sources,
||F Omega||^2=12, ||F^2 Omega||^2=168, total B coefficient48, R coefficient72,
dark initial loss zero and sum_i||Gamma1^(1/2)G1 R_i Omega||^2=1728.
Removing the canonical half factor is computed and detected with residuals
10 or20. These are exact finite rotor words, not a large-spin evolution.

The separate trace-one three-state classical example records25initial-layer,
15physical-flow and5distribution-test rows. It checks its closed mean and
variance profile, exact injection-minus-depletion and the C1 test
phi(t)=(1-t/T)^2. The independent fast-age quadrature agrees with the closed
test integral to about1.6e-14. Omitting the initial contribution is an
evaluated wrong limiting formula, not a rerun of a modified microscopic law.
A separate positive-Gamma anticommutator example has negative band loss
-0.16619037896906005. It does not claim negative loss on the cube trajectory.
Neither toy proves the cube tail, uniform spin limit, matched density or
physical supply. Those conclusions rest on the displayed conditional proof.

The root proof and controls, blind PRE, separate released POST, subsequent
matched-density addendum and final publication comparison are preserved
with their identities. The original seals remain unchanged. Selective
review and focused mechanical checks do not apply retained audit status;
combined integration and landing/audit obligations remain separate.

## Landing-review boundary and No-Go Discipline Gate

N1: fixed model and complete ensemble over a fixed physical-time interval. N2: pointwise power and unrestricted continuous-test convergence remain open. N3: quantum dynamics, preparation, compensation and time are supplied. N4: all-age tail and source-order hypotheses come from the linked full-energy proof. N5: exact primitive profile coefficients and independent boundary/anticommutator controls support the analytic result. N6: distributional system-energy drift is not heat or apparatus supply. N7: the exact coherent loss need not be positive; the diagonal carrier is a different quantity. N8: matching is absolute and tested drift uses fixed C1 functions, with the initial boundary contribution retained.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Historical author checks remain provenance only. Complete originals remain recoverable at PR #9120's frozen head. No audit verdict or retained grade is applied.

---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: direct_blocker_closure
target_claim_id: real_control_autonomous_output_bounded_theorem_note_2026-10-17
target_blocker_text: "remove externally timed preparation"
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Package pinned premises and evidence for independent landing review; native Hamiltonian and state identification remain separate."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Fixed exact supplied Hamiltonian and delivered pure product seed; complete-output error on stated infinite and finite time domains."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---
# Real autonomous endpoint emission with a common complete-output operation

Status: proposed_retained
Claim type: bounded_theorem

## Reproducible sources

Primary runner: [exact local algebra and bound arithmetic](../scripts/real_endpoint_autonomous_output_2026_10_17.py).
Its declared inputs are pinned in the [artifact manifest](../outputs/real_endpoint_autonomous_output_2026_10_17_inputs/ARTIFACT_MANIFEST.json).

Load-bearing unchanged bare-ladder premises are the uniform interval in
[TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md](TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md)
and the physical-coordinate kernel in section 2 of
[EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md](EMITTER_COUPLING_FAMILY_BOUNDED_THEOREM_NOTE_2026-10-17.md).
Their original source/qualification bytes are frozen under `source_premises/`
in the input package. These are conditional dependencies on the unmerged
PR9667 ancestor stack, not independently re-audited certificates.
PR9667 at cbd23228ffb0b70f6b86f7d9ea03261fa6fb51f7 is the publication base;
its timed-control theorem is comparison context, not a runtime premise here.

The input package carries original proposals, both failed onset arguments and
their corrections, structural/quantitative/spectral/weighted reviews, and the
root qualification. Historical programs have `.py.txt` suffixes and are never
imported or replayed. Hash agreement records identity, not proof.

## Exact target and theorem

For the exact static positive nearest-neighbor qubit Hamiltonian and delivered
pure product seed specified below, the complete evolution approximates the
specified common-profile isometry with operator error <0.0013 for every
`t>=T=10^42` on the infinite output lead; the single finite apparatus with
`M=50T=5e43` output sites, fixed before delivery, has error <0.0023 for every
`t in [T,2T]`, after embedding into the infinite output space.

The checked weighted-profile and complete thin-strip refinement below gives
infinite error <.000058 for every t>=10^27, and finite error <.001058 on
[10^27,2*10^27] with M=5e28 fixed before delivery. It therefore also meets
the original .0013/.0023 tolerances at this earlier sufficient onset. The
prior T42 proof and T30/.003/.004 tradeoff are preserved as historical routes.
Each finite size denotes a separately fixed device; the infinite apparatus,
common waveform, seed and supplied physical premises are unchanged.

The bounds include arbitrary old inputs entangled with any passive reference,
all emitter/clock/source outputs, the actual common scalar, full complex output
phase, and old aging for the entire elapsed time. For the smaller-error T42 regime, complete
unhalved trace-distance bounds are <0.0026 and <0.0046; the T30 tradeoff
has bounds <.006 and <.008, respectively. The finite apparatus
has M+116 qubits. No apparatus of this size has been allocated or simulated.
The sufficient onset is not a minimum, linewidth estimate, or practical size.

This is a checked conditional mathematical implication, proposed for review,
not an audit verdict or framework derivation of the premises. It removes the
named externally timed preparation import of the earlier real-control model
by changing the supplied apparatus: after delivery no drive or switching is
used. The exact static Hamiltonian and the delivered pure emitter/blank-clock/
source product seed remain supplied. It is not a transfer of the old apparatus'
preparation, calibration-box, or runtime theorem.

## Imports and proof obligations

| Input | Role | Provenance | Framework bridge |
|---|---|---|---|
| Exact coefficients, signed positive cells, selective zero NN couplings and graph below | Defines the self-adjoint mathematical model | Frozen real endpoint construction; explicit decomposition below | Native Hamiltonian/coefficient supplier open |
| Unitary Hamiltonian evolution and its elapsed parameter | Dynamics used by spectral analysis | Supplied model convention | Physical Hamiltonian/time/energy identification open |
| Pure one-emitter head, blank other head qubits, sources in 00 | Initial condition | Delivered state assumption | Native pure-state/thermal supplier open |
| Bare ladder calibration residual d0, matching inverse and gap | Uniform scattering premises on the fixed interval | Pinned interval source and qualification | Conditional source result; not re-audited here |
| Retarded bare ladder kernel in physical coordinates | Exact gluing identity | Pinned family section 2 and qualification | Used only for unchanged bare ladder; no inherited emitter theorem |
| Complex W and reference phase convention | Mathematical comparator | Explicit definition and fixed bare reflection below | No physical Record/readout identification |

The scale reference primitive supplies units only; kinetic isotropy supplies its
registered structural normalization only; realized-state specialization does
not select this seed. None is being asked to derive the additional data above.
No new physical axiom or primitive is proposed.

The obligation graph is: pinned bare calibration/gap/kernel premises -> real
filter and shared-source two-port bounds -> terminated-port and full emitter
inverses -> local Stone representation and variance-controlled packet ->
positive spectral jump/reciprocity and integrated finite-core spectral mass ->
complete escape -> finite polynomial transfer. The displayed derivations prove
the intervening implications under the named premises. Independent same-model,
source-exposed checks reconstructed these steps; they did not independently
recertify all ancestral calibration computations. The strongest missing bridge
to an unconditional physical claim is derivation and identification of the
supplied Hamiltonian and delivered state from the framework; that bridge is
not a lemma asserted by this theorem.

The theorem fixes nonzero kappa=10^-12 and sigma=10^-6, threshold-free interval,
exact coefficients, four old columns and one open channel per selected
parity/energy. It makes no kappa=0, threshold, arbitrary-accuracy, calibration
perturbation, many-head, or arbitrary initial-source claim. Infinite point
spectrum is bounded in the seed remainder; the finite device's entire spectrum
is point spectrum, so the infinite projection statement is not transferred.

## Exact internal Hamiltonian and coefficients

Let n=(I-Z)/2, a=|0><1|, and write u_AB for the source interaction coefficient
to distinguish it from the filter's diagonal shift u below. On the old pair
and shared sources A,B,

    K=2I+Z1 Z2,
    Csrc=DeltaA nA+DeltaB nB+h(nA+nB-aA* aB-aB* aA)+u_AB nA nB,
    Gsrc=gA nA(I+X1)+gB nB(I+X2), B=K+Csrc+Gsrc,
    VA=lambdaA(I+XA)+mu0 I,
    VB=lambdaB(I+XB)-nu I,
    W=[(9+12i)I+(-16+12i)X1 X2]/25.

An asterisk on a creation/annihilation symbol denotes its adjoint. Every
entry in the following table is an exact terminating decimal.

| J | gA | gB | h |
|---:|---:|---:|---:|
| .030021107107032 | .996878563816670 | .599319315560298 | 3.999349697888060 |

| lambdaA | lambdaB | u_AB | mu0 |
|---:|---:|---:|---:|
| 3.801781381581202 | 2.575033765788497 | .544607276405587 | .321494607058201 |

| DeltaA | DeltaB | nu |
|---:|---:|---:|
| 2.192035527016003 | 2.186826508897014 | 1.459892813020969 |

Put q0=4.510351185997098 exactly, k0=2 arctan(1/q0),
C=cos(k0)=(q0^2-1)/(q0^2+1), S=sin(k0)=2q0/(q0^2+1), and
E(k)=2J(1-cos k), E0=E(k0). These C,S,E0 are exact rationals, saved in the
parameter object. B iota=iota K for iota x=x tensor |00>_AB, and
I<=B<20I. Parity X1X2 reduces all new and inherited blocks. Its two vacuum
old energies are b_j=1,3 and W eigenvalues are omega_+=(-7+24i)/25,
omega_-=1. No commutation of K with the full interacting Hamiltonian is used.

The physical one-head Hamiltonian is the finite/infinite clock graph defined
below, tensor I_internal, plus I_head tensor B, the four clock contacts
P_(c0,a) tensor VA and P_(c1,a) tensor VB (a=0,1), plus c_new I.
The emitter is a head position with diagonal E0; ordinary clock diagonals are
2J except the two filter sites. This describes the restriction of the fully
positive qubit Hamiltonian, not an effective higher-body substitute.

The complete new derivation follows. All displayed inequalities are uniform
on the fixed nonzero momentum interval unless stated otherwise.

## Target and fixed choices

Use the exact bare two-body ladder with B, VA, VB, J, E0, k0 and W from the
interval source. Preserve its positive central ceiling d0=1.76e-13. There
are four real vacuum old vectors u_j, indexed by energy b_j in {1,3} and
parity p in {+,-}; W u_j=omega_p u_j. On I=k0+[-sigma,sigma], sigma=1e-6,
use r=1/7, g=9/50, v=1/40, E2=2J, |r_j'|<=700,
||M16^-1||<166, ||T_g||<=206, ||alpha_closed||<=16. Let

    z=exp(ik), Q=zP+Qc, A=[J(Q-Q^-1)]^-1,
    ||A||<=40, ||Pc A||<=1/g, ||A^-1||<20,
    Gg(n,m)=A Q^|n-m|+Q^(n-1) T_g Q^(m-1), n,m>=2.

Here lambda_j(k)=b_j+E(k) is the energy after removing c_new,
P=|u_j><u_j|, Pc=I-P and Qc=sum_closed q_l P_l, with fixed real orthogonal
spectral projections of B. The decaying real roots satisfy
q_l+q_l^-1=(2J+b_l-lambda_j)/J, |q_l|<=1/7 and |q_l'|<=1/24.
Thus ||Q'||<=1. The coefficient T_g=E1* M16^-1 E1-A is the inherited
boundary Green coefficient; it is distinct from the later onset time T.

There are seven complementary directions in each parity, including the
other old energy. The last inverse bound follows from B in [1,20] and
|J(q-q^-1)|<|2J+b-lambda|<20 on closed channels, while the open inverse
entry has magnitude E'<2J<20. T_g need not commute with Q. B does commute
with Q, because Q is its spectral function at the chosen energy; the full
interaction need not commute with K.
The source supplies r_j(k) approximately r0(k) zeta omega_p, with r0=-z^2,
one exact scalar zeta=-exp(-4ik0)alpha, and uniform error d0+702sigma.

Here alpha is the exact unit-modulus bare reflection at site-1 reference
plane for (b=1,p=-1) at k0; equivalently alpha=z0^2 r_abs,(b=1,p=-1)(k0).
This defines one scalar from the exact bare matching problem, not four fitted
column phases. The bare physical matching matrix is

    M16=[[lambda-2J-B-VA, JI8],[JI8,-JQ^-1-VB]].

Its unit-incoming RHS at the second coordinate is (iE'/z)u_j. The pinned
calibration premise bounds the four absolute-site reflections relative to
r0 zeta omega_p with the stated strictly positive d0.

Choose a phase-filter position F=20, two arms ending at N=44, input stub
length ell=20, and endpoint coupling kappa=1e-12. No kappa family, calibration
box, inherited resonance onset, or externally timed preparation is imported.

## Two-port algebra and the phase filter

For U=2^-1/2[[1,1],[1,-1]], the exact two-arm scattering matrix is
U diag(r1,r2) U^T. Identical arms have zero transmission. A hopping sign
change is a gauge change on a tree and does not create the required minus
sign in a round-trip reflection.

For a scalar endpoint potential v, r_v=-(v+Jz)/(v+J/z). Two constant endpoint
potentials can satisfy r_v1=-r_v2 on an open interval only when v1+v2=0 and
v1*v2=-J^2. Thus v1=+/-J and v2=-/+J, an old-independent scalar example;
this is only a statement about that two-parameter ansatz.

Let C=cos(k0), S=sin(k0). Replace the bond between arm-1 sites F,F+1 by
hopping -t, and shift both their one-head diagonals by u, where

    u=-J/C, t=J S/C,
    V=[[u,J-t],[J-t,u]], w=||V||=J[1+(1-S)/C]<1/20.

The two-site filter is joined to free leads by -J. In its parity basis the
endpoint potentials are u-t and u+t. At k0 their reflections are iz0 and
-iz0; hence filter reflection a(k0)=0 and transmission b(k0)=iz0. A free
bond has transmission z0. The relative one-way filter phase is i, and the
relative round trip phase is -1. The earlier idea of setting b=i rather
than b=iz0 was corrected analytically before any execution: the free-bond
reference plane must be paid.

On I, sin(k)>2/5, so |r_v'|<=2/sin(k)<5, |a|<=5sigma and
|b/z-i|<=6sigma. For a scalar reflector r_g at the original absolute origin,
put q=r_g z^(2F). Exact concatenation gives

    r_scalar=z^-2(F+1) a + (b/z)^2 r_g/(1-aq).

Its denominator is at least 1-5sigma and
|r_scalar+r_g|<=5sigma+17sigma/(1-5sigma)<23sigma.

## Full closed-channel filter correction

At filter sites F,F+1, split Gg into P and Pc. Its blocks obey

    ||Gpc||,||Gcp||<=300 r^(F-1),
    ||Gcc||<=(1+r)/g+211 r^(2F-2).

The closed inverse Cc=(I-Gcc V)^-1 has norm <3/2. The free open two-site
matrix D0=I-Aopen[[1,z],[z,1]]V has inverse norm <10: its even denominator
has real part >1, and the magnitude of its odd denominator's imaginary part
is w tan(k/2)/(2J)>1/10. Here w>J and tan(k/2)>1/5 on I.
The image term is rank one. Its Sherman-Morrison denominator has modulus
at least 1-|a|. Consequently the scalar-background K0=I-Gpp V satisfies

    ||K0^-1|| <=10+400/(1-5sigma)<500.

The full open Schur correction has norm <338 r^(2F-2), giving Schur inverse
<1000 and the entire (I-Gg V)^-1 norm <2000. This is uniform, not a grid.
For a unit-incoming ladder column, the local P input norm is <3 and its
Pc input norm <17 r^(F-2). If xP0 denotes the scalar open solution, then

    ||xP0||<1500,
    ||xP-xP0||<10^8 r^(2F-3),
    ||xc||<5000 r^(F-2).

The exterior open rows of Gg have norms <120 on P and
<211 r^(F-1) on Pc. Therefore

    |r_modified-r_scalar|<10^9 r^(2F-3)<1e-20.          (A)

All seven Pc coordinates contribute. No scalar filter argument alone is
being substituted for the noncommuting physical ladder.

For later gluing, at n,m>=F+1 write the modified Green kernel as

    A Q^|n-m| + Q^(n-F-1) Ttilde Q^(m-F-1).

The original Ttilde=Q^F T_g Q^F. The update is Cfilter V(I-Gg V)^-1 Cfilter^T,
where ||Cfilter||<350. Thus ||Ttilde||<206+350^2*(1/20)*2000<1.3e7.
The transpose, not an adjoint, occurs because these retarded finite kernels
are complex symmetric in a real internal basis. Norm estimates are unchanged.

## Shared internal system and real junction

Use one old pair and one source pair A,B. Duplicate the clock contacts, not
the internal system. B occurs once and acts independently of the arm label.
In the one-head sector the arms before junction mixing are an exact direct
sum on head position times the same internal fiber. Mixing the two exterior
leads by U is an exact unitary change of head coordinates and commutes with
B. It does not require [H,K]=0.

The four junction edges realize hopping block -JU between two arm ends and
two port starts. They are the four edges of an ordinary cubic-lattice square;
one signed hopping is positive and the other three negative. Every magnitude
is J/sqrt(2). Diagonal compensation uses four positive vacancy terms
gamma(I-n), gamma=(sqrt(2)-1)J, giving diagonal 2J and scalar 4gamma.

At the two port origins the common reference-plane factor is z^(2(N+1)).
Define rho_g(k)=z^(2(N+1))r0(k)zeta=-zeta z^(2N+4). The exact open S matrix
is [[R_j,tau_j],[tau_j,R_j]], with

    |R_j|<eta=12sigma,
    |tau_j-rho_g omega_p|<delta_tau=d0+714sigma.         (B)

Equation (A) and the unitary U prove these; no equal magnitudes or opposite
phases were assumed. S is unitary by flux. The point is only approximately
reflectionless after closed-channel feedback; no exact interval cancellation
is asserted.

For m,n>=0 on the two exterior ports, the full kernel has the form

    G_ab(m,n)=delta_ab A Q^|m-n|+Q^m T_ab Q^n.

At each chosen old energy, T_ab,PP=Aopen S_ab. Since d=N-F=24,
||T_ab,PC||,||T_ab,CP||<=K_tail r^d and
||T_ab,CC||<=K_tail r^(2d), K_tail=1.3e7.
K_tail is a scalar kernel ceiling, distinct from the literal old operator K.
This pays the distance between the phase filter and the junction.

## Closing the input port and installing a real endpoint emitter

Keep input-port sites m=0,...,ell and remove site b=ell+1 and its outer tail.
The remaining output lead is infinite. The exact Dirichlet formula is
Gtr=G-G(.,b)G(b,b)^-1G(b,.). Write X=Q^ell T_aa Q^ell and
X0=Aopen R_j z^(2ell)P. Then

    ||X-X0|| <=3K_tail r^(d+ell)<1e-28,
    Gbb=A+QXQ, ||Gbb^-1||<22,
    Gtr(end,end)=(A+X)-(A+X)Q(A+QXQ)^-1Q(A+X).

For X0 this is diagonal: its open entry is

    g_j=-(z/J)(1+R_j z^(2ell))/(1+R_j z^(2ell+2)),

and its closed block is -Qc/J. The displayed matrix function is Lipschitz
with constant <10^6 on the radius-1e-28 neighborhood: the two unperturbed
factors have norm <41, the unperturbed inverse <21, and the perturbed inverse
<22. Hence the actual end Green matrix differs by <epsilon_G=1e-22,
has norm <35, and its PC and CP norms are <epsilon_G.

The open outgoing row toward the output lead satisfies the corresponding
identity L=Y[I-Q(A+QXQ)^-1Q(A+X)], Y=PT_ba Q^ell. Its scalar approximation is

    L0=-(tau_j/J)z^(ell+1)/(1+R_j z^(2ell+2)) P.

Using ||Y-Y0||<=K_tail r^(d+ell), ||Y0||<=40 and the preceding inverse bounds
gives ||L-L0||<epsilon_L=1e-21. These are full internal row/matrix estimates.

Attach one endpoint emitter with hopping -kappa, diagonal E0. Its positive
physical realization is Q(-kappa), (E0-kappa)n_e and (J-kappa)n_end, the
last term restoring clock endpoint diagonal 2J. Both onsite coefficients are
positive. The delivered seed is real product |1>_e|all clock zero>|00>_AB
times the arbitrary old/reference state. No drive acts after delivery.

The emitter Schur matrix is De=(lambda-E0)I-B-kappa^2 Gtr(end,end).
On Pc the bare gap is >g: the smallest source margin is at least
min(DeltaA,DeltaB)-2-2J*sigma>9/50, and the other vacuum energy is two away.
The perturbation has norm at most35*kappa^2, so the complementary emitter
block Dcc has inverse norm <6. The resonant scalar is

    Dj=E-E0-kappa^2 Gjj-kappa^4 Gjc Dcc^-1 Gcj.

Let Dref=E-E0+kappa^2 z/J. The absolute correction compared with
Im Dref=kappa^2 sin(k)/J gives both

    |Dj-Dref|<epsilon_D |Dref|,
    Im Dj>(1-epsilon_D)kappa^2 sin(k)/J>12kappa^2,
    epsilon_D=1/40000,
    ||De^-1||<1/(10kappa^2)=1e23.                       (C)

One must compare directly with Im Dref to justify its positive lower bound;
relative modulus alone would not do so. The inequality follows from
2eta/(1-eta)+2epsilon_G J/(sin(k))<epsilon_D. All seven emitter coordinates
are retained. These finite inverse constructions also exclude an in-band
normal eigenvector; out-of-band point spectrum is allowed.

## Spectral normalization, common outgoing profile, and aging

For real H use R+=(lambda+i0-H)^-1. The outgoing component of R+ seed is
Aout,j(k)exp(ikm). Stone's formula has sign
-(R+-R-)/(2pi i), hence the emitted outgoing coefficient in dk is
F_j=i E'(k) Aout,j/sqrt(2pi). The exact scalar reference is

    Fref(k)= i kappa E'(k) z^(ell+1)rho_g(k)
              /[sqrt(2pi)J Dref(k)].                    (D)

The scalar endpoint reference resolvent is 1/Dref. Its density in dk is
|Fref|^2=kappa^2 E'^2/(2pi J^2 |Dref|^2). Its seed has mean E0 and variance
kappa^2, so p0=int_I|Fref|^2 satisfies
1-(kappa/(v sigma))^2<=p0<=1. This uses the global spectral measure, not
completeness or Markov decay. Thus p0>=1-1.6e-9. Define f=Fref/sqrt(p0),
with positive normalization; f already includes the one common rho_g and
propagation phase. Actual apparatus parameters J,E0,kappa determine f.

The exact outgoing row and (B)-(C) give

    |F_j/Fref-omega_p|<epsilon_F=0.000752.              (E)

Indeed the leading relative error is bounded by
(delta_tau+eta+epsilon_D+eta epsilon_D)/[(1-eta)(1-epsilon_D)]<epsilon_F;
the extra epsilon_L term is <1e-21 and fits the strict margin.

For the actual product seed in column j, the mean is b_j+E0+c_new and
the variance is exactly kappa^2. Outside its own physical energy interval
c_new+b_j+E(I)
the amplitude is <=kappa/(v sigma)=4e-5, including point spectrum. No point
spectrum occurs inside that interval by the matching inverse just proved.
The local spectral jump is rank one: if Phi_j has unit incoming open wave,
the finite-core identity R+-R-=-(i/E')Phi_j Phi_j* gives measure
Phi_j Phi_j* dk/(2pi). This supplies normalization without assuming a complete
scattering basis on the whole spectrum. Hence replacing the actual seed by
the normalized exact outgoing packet with coefficient omega_p f costs
<0.000792002 per column. Two old-energy columns can overlap in their error
vectors within one parity; paying sqrt(2)<1.415 gives operator cost <0.001121.
Different parities are orthogonal. This extends to every passive reference.

The physical scalar is

    c_new=2nu+2beta+4gamma,
    beta=J[(1+S)/C-1], gamma=(sqrt(2)-1)J.                (F)

The full comparator at elapsed time t is exp(-ic_new t) beta_t on the output
lead, blank emitter/other clock/source, and exp(-itK)W on old/reference.
Here beta_t is the restriction to m>=0 of the Fourier integral with f and
phase exp(ikm-iE(k)t), normalized by its positive norm. No old aging is
removed, no setup time is hidden, and no per-column scalar is chosen.

## Complete spectral interface and improved escape

The physical finite-core inverse is a 113-by-113 matrix of eight-dimensional
blocks in each parity. Bare blocks are <250 from the <166 contact inverse and
free/image bounds <40 and <206. A two-site filter update costs at most
2*250^2*(1/20)*2000, yielding <1.3e7 per block. Orthogonal port mixing gives
<3e7 per physical block. Endpoint deletion costs at most 22*(3e7)^2, so every
background block is <2e16. Emitter elimination gives existing/existing blocks
<2e16+kappa^2*(2e16)^2*1e23<5e31, new/existing blocks <2e27 and new/new
blocks <1e23. Thus all blocks, including the new emitter, are <5e31 and the
core inverse norm is <113*5e31<6e33. These are finite-coordinate estimates,
not a continuous-spectrum whole-resolvent norm bound.

Let M denote this actual 904-dimensional matching matrix in one parity,
x=M^-1 iE' u its unit-incoming column, and R its reflection amplitude.
The core spectral jump derived below gives

    ||x||^2=-2E' Im tr(M^-1)
       <=2E' sum_(113 sites) 8||(M^-1)_ss||<1e34.

With ||M'||<=3J<.1, |E''|<.061 and fixed real u, differentiation gives
||x'||<6e33(.061+.1*1e17)<7e49. Because M is complex symmetric,
u^T M^-1=x^T/(iE') and R=u^T x-1, so exactly

    R'=(E''/E')(1+R)-x^T M' x/(iE'),  |R'|<5e34.

No adjoint replaces this transpose. The fixed physical basis avoids a hidden
k-dependent basis derivative. Removing the incoming/outgoing open waves from
the complete generalized column leaves C. Its finite part costs ||x||+2,
its derivative ||x'||+|R'|. Closed tails have multipliers
r/sqrt(1-r^2)<1/6 and (1/24)sqrt((1+r^2)/(1-r^2)^3)<1/20.
Thus every finite and evanescent coordinate is included in

    ||C||<C0=2e17, ||C'||<C1=2e50.

The exact normalized f has ||f||_1<.002, ||f||_infinity<4e10,
||f'||_infinity<3e32, and endpoint-inclusive variation Vedge(f)<7e26.
These follow from Im Dref>12kappa^2, |Dref'/Dref|<6e21, and the numerator's
phase derivative ell+1+2N+4=113; Cauchy-Schwarz gives its L1 bound.

Let Jcore be the fixed isometric inclusion of the 904 core coordinates,
distinct from the closed-channel projection Pc. The Stone density gives

    integral_I x x* dk/(2pi)=Jcore* E_H(c_new+b_j+E(I)) Jcore,
    integral_I ||x||^2 dk <=2pi*904.

The equality uses the established local absolutely continuous interval; the
upper bound also follows from the ac contribution alone, since a compressed
spectral projection is a positive contraction. It is a finite-rank trace, not
a trace on the infinite Hilbert space. The spectral-variable conversion
E'dk=d lambda cancels the inverse E' in the jump, and the rank is 904 per
parity, not 1808. Therefore the reciprocal identity implies

    integral_I |f||R'| <=2(.061/.025)*.002
          +(.1/.025)*(4e10)*2pi*904 <1e15,

using pi<10/3. This corrected bound remains an input to the weighted
variation argument below. Define Vedge(h)=|h(left)|+|h(right)|+integral|h'|;
both hard-cutoff endpoint values remain included.

### Weighted variation of the exact common profile

Write alpha_D=kappa^2/J (distinct from the bare reflection phase alpha),
Dref=E-E0+alpha_D exp(ik), X=Re Dref, Y=Im Dref. The exact numerator is

    f=A_f E' exp(i113k) zeta0/Dref,
    A_f=kappa/[sqrt(2pi)J sqrt(p0)]<17kappa, zeta0=-i zeta.

Here |zeta0|=1 and p0 is the fixed positive normalization over I, so neither
has a k derivative. The phase 113 is ell+1+2N+4 and is differentiated.
The bound on A_f follows from J>.03, sqrt(2pi)>2 and p0>=1-1.6e-9.
Normalization means integral_I |f|^2 dk=1; no second Fourier factor belongs
in that identity. The existing ||f||_1<.002 and sup|f|<4e10 are unchanged.

Since .03<J<.031, E'>.025, E'<.061 and sin(k)>.4,

    X'=E'-alpha_D sin(k)>.024,
    |Dref'|=|E'+i alpha_D exp(ik)|<.062,
    Y=alpha_D sin(k)>12kappa^2.

Thus X is strictly increasing and Dref has no zero on I. Substitution of X,
followed by enlargement of its image to the real line, gives

    integral_I dk/|Dref|^2
      <=(1/.024) integral_(X(I)) dX/[X^2+(12kappa^2)^2]
      <=pi/(.024*12kappa^2).

No assertion that X(I) crosses zero is needed; Y is bounded below rather
than replaced by a constant when differentiating Dref. Differentiating the
actual complex f gives all three terms

    f'=(E''/E'+i113)f
         -A_f E' exp(i113k) zeta0 Dref'/Dref^2.

Consequently

    integral|f'| <(.061/.025+113)*.002
       +17kappa*.061*.062*pi/(.024*12kappa^2)
       <.232+1/kappa.

For this last, different integral, pi<4 is sufficient because
17*.061*.062*4/(.024*12)=.257176/.288<1. This does not reinstate the
insufficient pi<4 citation for the earlier <1e15 reflection-derivative bound.
Adding both endpoint values gives Vedge(f)<.232+1e12+8e10<2e12.

For a_in=omega_p f/R, |R|=1 gives

    Vedge(a_in)<=Vedge(f)+integral|f||R'|<2e15.

Integration by parts at incoming output site m>=0, with s=vt>=1, gives

    |integral h exp(-imk-itE)dk|
       <=[Vedge(h)+(.061/v)||h||_1]/(m+s),
    sum_(m>=0)(m+s)^-2<=2/s.

The curvature contribution is <.00488. Including Fourier normalization gives
incoming norm <3e15/sqrt(pi vt). The corresponding negative-half-line
outgoing tail is <3e12/sqrt(pi vt). Full-line Fourier Parseval gives unit
norm; the cost of positive normalization of its positive-half-line restriction
is no greater than that tail. Open output fibers are orthogonal across old
columns, so these scalar bounds gain no sqrt(2).

### Weighted derivative of the entire localized column

The finite-rank spectral bound gives integral||x||^2 dk<=2pi*904<7232,
using pi<4 here. Cauchy-Schwarz with integral|f|^2 dk=1 gives

    integral|f|||x||<86,

since 7232<86^2. The fixed-coordinate equation x'=M^-1(iE''u-M'x) then gives

    integral|f|||x'||<6e33[.061*.002+.1*86]<5.2e34.

The finite-core remainder derivative costs ||x'||+|R'|. Its closed-tail
derivative costs at most ||x'||/6+||x||/20 by the same geometric bounds
above. These operator bounds include all seven closed directions; uniform
geometric decay justifies differentiating the Hilbert-space-valued tail.
There is only one infinite lead. Hence

    ||C'||<=(7/6)||x'||+|R'|+||x||/20,
    integral|f|||C'||<(7/6)*5.2e34+1e15+86/20<7e34.

This uses neither cancellation of absolute values nor an averaged inverse.
For the localized integral integration by parts differentiates a_in C/E'.
Its complete numerator, including endpoints and the derivative of 1/R, is

    L<=C0 Vedge(f)+integral|f|||C'||
          +C0 integral|f||R'|+(.061/v)C0||f||_1
      <4e29+7e34+2e32+9.76e14<8e34.

The third term is essential: moving the reflection phase into C would move
its derivative there, not remove it. The k-independent omega_p and elapsed
old phase exp(-it b_j) add no k derivative. Including the Fourier factor and
sqrt(2) for the two potentially overlapping localized columns per parity
bounds the complete localized operator by L/[sqrt(pi)vt]<1e35/(vt).
Parities remain orthogonal, and tensoring any passive reference preserves
this operator bound.

At T=10^42, vT=2.5e40 and sqrt(pi vT)>2e20. The incoming, outgoing
normalization and localized contributions are respectively <1.5e-5,
<1.5e-8 and <4e-6. Total escape is <1.9015e-5<2e-5 for every t>=T,
because all three ceilings decrease. Adding the unchanged preparation cost
<.001121 gives complete infinite error <.001141, hence <.0013. That
preparation cost still includes the off-band and point-spectrum residual.
The fixed apparatus, phase, seed, coefficients and error metric are unchanged.

## Geometry, positive blocks, and finite horizon

Take D=40, N=D+4. Old/source sites are old1=(0,0,0), old2=(1,0,0),
A=(0,1,0), B=(1,1,0). Arm0 is (n,1,1) for 0<=n<=D-4, followed by
(D-4,1,2),(D-4,1,3),(D-3,1,3),(D-2,1,3),(D-2,1,2),(D-2,1,1),
(D-1,1,1),(D,1,1). Arm1 is (n,1,-1) for 0<=n<=D+1, followed by
(D+1,2,-1),(D+1,2,0),(D+1,2,1). These are both 45-site paths.
The two port starts are out=(D+1,1,1) and in=(D,2,1), completing the
junction square. Output m is (D+1+m,1,1); input m is (D,2+m,1), with emitter
at input m=ell+1. All sites and installed edges are ordinary cubic NN.
An earlier provisional coordinate path that passed through the input port
was discarded before execution; the explicit path above is the candidate.

Every real hopping h uses Q(h)=|h|(n_x+n_y)+h(a_x* a_y+a_y* a_x), PSD on all
four two-qubit states, norm 2|h|. The filter replaces one bond by Q(-t) and
adds beta(I-n) at its two sites. Junction Q terms and gamma vacancies were
specified above. The exact bare source/old/contact positive blocks occur
once except both clock contacts and vacancy nu, which occur on both arms.
Arm entrances carry J n_c0; endpoint and emitter compensations were given
above. All runtime coefficients are static, so modeled slew is zero.

Added old loads stay 2gA and 2gB below 2; the existing old edge has norm 3.
Source A/B loads are 27.936224853155858 and 22.228906875353305. Boundary
c0/c1 loads are 8.015120691541701 and 6.730044773026091. Filter-site loads
are 2J+2t+beta<0.12, junction loads (1+3sqrt(2))J<0.16, emitter load
E0+kappa<0.006, input endpoint 3J+kappa<0.091, and ordinary clock load4J.
No all-site cap2 or native coefficient/vacuum supplier is asserted.

For finite output m=0,...,M-1 add J n_(M-1) to preserve diagonal2J. There
are M+112 head sites (including emitter), M+116 total qubits, and M+112
head-hopping edges. The finite core used above has 113 head positions.
The first omitted output site has head-graph distance d_M=M+ell+3=M+23
from the seed. Internal source mixing cannot shorten this distance.
The one-head spectral radius about c_new+10.5+2J is <18: use B in[1,20],
contact norm<7.926, the unperturbed clock in[0,4J], filter norm<.05,
emitter diagonal displacement <2J and emitter coupling kappa. Explicitly,

    9.5+2J+7.926+.05+2J+kappa<18.

This bound applies to the invariant one-head space. Compensated compression
preserves each degree-<d_M polynomial applied to
the seed subspace. Both spectra lie in the same radius-18 interval, so both
rescaled Chebyshev polynomials have norm <=1. The generating-function contour
of radius exp(1) gives |J_n(18t)|<=exp(18t sinh(1)-n). Canceling identical
low-degree terms in the Chebyshev expansion and summing its tail gives

    finite/infinite difference <=4 exp[-d_M+18t sinh(1)]/(1-exp(-1)).

With M=50T=5e43, T=10^42, this is <.001 for t<=2T. The same literal finite
Hamiltonian is chosen before delivery. It has complete error <.002141,
safely <.0023, only on [T,2T]. The comparator is the embedded infinite
output profile; no finite-waveform renormalization is substituted. All-future
finite halt, capture, reset, reuse, thermal preparation, practical cost,
native blocks, physical time/energy/Record identification and tolerance
composition remain outside scope.

## Details fixing the signs and complete spectral interface

For the phase filter, the direct two boundary rows, with one incoming wave
from the left, are

    [[u+J/z,-t],[-t,u+J/z]] [a;b] = [-(u+Jz);t].       (G)

They give a=0,b=iz at k0 directly: (u+J/z)iz=i(uz+J)=t and
-ti z=-(u+Jz). The free bond has b=z, not b=1. The independent
structural reconstruction uses these rows; historical author arithmetic also
corroborated them without replacing this identity.

For the uniform filter inverse, the even/odd eigenvalues of V are -beta and
-w. The free two-site Green eigenvalues have real parts +1/(2J), -1/(2J)
and imaginary parts -(1+cos k)/E', -(1-cos k)/E'. The even denominator has
real part 1+beta/(2J)>1. The odd denominator has imaginary magnitude
w tan(k/2)/(2J)>1/10. Adding the gate image is a rank-one update whose
Sherman-Morrison scalar is 1-r_j z^(2F)a(k); this follows by recognizing
A v^T V D0^-1 v as the filter's reflected wave. Thus its lower bound
1-|a| is an actual scattering identity, not a presumed inverse certificate.
The large constants in (A) keep the resulting complete inverse explicit.

In the terminated-port formula, use X0 as in the main derivation and D_b=A+QXQ.
The inverse difference obeys

    ||D_b^-1-D_b0^-1||<=22*21 ||X-X0||.

Expanding the three-factor product for Gtr gives the exact sufficient
Lipschitz constant 1+22*41+41*22*21*41+41*21=778386<10^6.
For Z=I-Q D_b^-1 Q(A+X), its scalar-reference norm is below3 and
||Z-Z0||<(22*21*41+21)||X-X0||. Thus ||Z||<4 and
||L-L0||<=4K_tail r^44+40(22*21*41+21)3K_tail r^44<10^-21. The spectral decomposition
of B is used only to prove inequalities; no uncertified eigenvectors enter.

For the installed emitter the outgoing retarded coefficient has the exact
form

    Aout,j=-kappa L De^-1 u_j.

Eliminating its seven complementary coordinates gives
De^-1 u_j=Dj^-1[u_j+kappa^2 Dcc^-1 Gcj]. The row L0 and the sign in this
formula produce (D), including its factor i from Stone's formula. In the
ideal R_j=0, tau_j=rho_g omega_p limit, reflection from the emitter-terminated
stub would be

    R_end=-z^(2ell+2) conjugate(Dref)/Dref,
    R_inst=tau_j^2 R_end
          =omega_p^2 Fref/conjugate(Fref).               (H)

This meets the real one-port phase relation. It explains why the new route
does not inherit the previous realifier's equal conjugate-sector failure:
the old operation is crossed twice in the final stationary reflection, but
once by the emitted outgoing packet. Equation (H) is a consistency check
of the ideal limit; bounds (A)-(E), not exact cancellation in (H), control
the actual apparatus.

For completeness, the finite core Schur matrix in the final one-output-lead
geometry, with Hcore the compression of Hphys-c_new I, is

    Mcore(k)=lambda_j(k)I-Hcore+J P_out Q(k) P_out*.

It is exactly904 by904 per parity, in orthonormal physical head/internal
coordinates. Its inverse equals the finite-coordinate retarded kernel used
above; this is not a norm bound on the whole continuous-spectrum resolvent.
The unit-incoming RHS is iE'(k) P_out u_j. Since the boundary jump is
Mminus-Mplus=-iE' P_out Pj P_out*, resolvent subtraction gives

    Rplus-Rminus=-(i/E') Phi_j Phi_j*  on finite coordinates.

The spectral measure is therefore Phi_j Phi_j* dk/(2pi). Extending through
the exact free-tail recurrence yields the complete generalized column,
including all finite emitter/source coordinates and closed tails. An in-band
normal state would have no open tail and would solve the homogeneous Mcore
system, which is invertible. The analytic finite-core inverse and threshold-free tail roots give smooth
finite-coordinate densities. Finite-support vectors are dense, excluding a
hidden singular-continuous component in this interval. Uniqueness of matching
with a nonzero unit incoming wave gives the local multiplicity-one synthesis
isometry. This justifies the local absolutely continuous spectral
representation while allowing arbitrary spectrum outside the band.

Let R_inst,j be the actual final one-channel reflection. For the real seed,
Stone's formula gives outgoing coefficient F_j and incoming coefficient
conjugate(F_j), consistently F_j=R_inst,j conjugate(F_j). The exact comparison
packet uses incoming coefficient omega_p f/R_inst,j. Its outgoing coefficient
is omega_p f. The L2 difference of these coefficients is the state norm
difference within the band. Adding the actual variance-bounded complement
gives the preparation-to-packet estimate, without presupposing a complete
scattering transform on the whole Hilbert space.

The actual infinite-apparatus point-spectrum amplitude on the entire old
input is at most sqrt(2)*4e-5<6e-5. Different old-energy residuals may overlap
within one parity, so the square-root factor is essential. For finite M the
whole spectrum is point spectrum; that infinite-operator projection statement
is not transferred to the finite system. Both errors are retained in the
full state comparison, not conditioned away.

The output comparator can be written explicitly as

    Uout(t)x = exp(-i c_new t) E_out(beta_t)
                 tensor [iota exp(-itK)W x],
    beta_t(m) = b_t(m)/||b_t||_(m>=0),
    b_t(m)=(2pi)^-1/2 integral_I f(k) exp(ikm-iE(k)t) dk.

E_out places the one head on the output lead and all other head sites,
including the emitter and both arms/input stub, in vacuum. It does not trace
them out. Tensoring with identity on any reference preserves every operator
bound. The ideal output profile uses the actual J,E0,kappa, path geometry
and the exact single ladder phase zeta; it is a specified common reference
profile whose full complex difference from every actual column is bounded
in (E). This is not an assertion that the actual four profiles are identical,
nor a stability theorem for a nominal waveform under calibration errors.

The clock phase E(k)t and old phase b_j t come from the same exact spectral
energy b_j+E(k). The physical c_new contributes separately. No traversal
delay is subtracted from old aging and no K evolution is commuted through
the source interaction. There is no five-unit control setup in this model.

## Finite geometry and resource accounting conventions

The temporary second infinite lead used for the scattering calculation is
only an analysis reference. The actual input side stops at m=ell; the emitter
occupies its next NN position. There is no unobserved open port, irreversible
sink, or discarded outward-emission branch. The denominators in the terminated
Green and emitter formulas retain all repeated returns and reabsorption.

The head edges number M+112 in the finite device. In addition, the old edge,
two old/source edges, shared source/source edge, and four source/clock edges
give eight distinct non-head NN pairs, or M+120 distinct two-body edges total.
Some pairs support more than one positive block. Counting positive blocks
separately, including onsite blocks, gives M+138 including K when J n_c0 and
mu0 n_c0 are kept as separate terms: head bonds M+112; source/old/contact
blocks11 including K; arm entrance/mu0/vacancy6; filter vacancies2;
junction vacancies4; emitter/input occupations2; finite output endpoint1.
Equivalently, there are M+137 added positive blocks excluding K. This is one
literal decomposition, not a minimized channel count. Combining onsite terms
would change the count, not their incident sum or the one-head Hamiltonian.

All these full-qubit blocks are positive. At an old site the pre-existing
K edge costs3 in addition to the displayed added load. At A and B the new
double contacts account for the large source loads. Exact static coefficient
installation, selective zero couplings on unused NN pairs, coherent signs
(one real pi-flux junction loop), and the initial blank product state remain
supplied resources. Zero runtime slew is not a claim of zero fabrication,
cooling, preparation, reset, or control-system cost.

The finite-horizon argument works in the invariant one-head space; it does
not bound the full many-head Hamiltonian norm by18. Positive blocks remain
defined on every full-qubit sector, and the initial one-head sector is exact
under the supplied number-conserving dynamics. The finite count is enormous
and is not claimed compatible with any thermal whole-sector preparation
bound from the earlier, different architecture.

## Review record and provenance

The frozen original endpoint route used T=10^136. The later positive-jump
candidate omitted the derivative of 1/R in its localized integral. Review
identified this omission; the corrected V2 restores it and supports T=10^78.
The integrated spectral-mass refinement then bounds the same term by
C0 integral|f||R'|. Its original citation of pi<4 was insufficient for the
printed <1e15 bound; pi<10/3 supplies the explicit repair used here. Neither
original failed argument is rewritten as having passed. The present result
uses the repaired proof, and preserves the original versions as provenance.

The integrated spectral-mass stage supported T=10^66, M=5e67, escape <9e-6,
infinite error <.001130 and finite error <.002130 on its own [T,2T] interval.
That valid intermediate stage remains preserved in `historical_author/THEOREM_NOTE_V1.md.txt` in the input package.
The present V2 adds the source-exposed independently checked weighted reference
variation and weighted finite-core derivative argument, giving T=10^42 and
M=5e43 with escape <2e-5, infinite error <.001141 and finite error <.002141.
It improves the sufficient onset without claiming a smaller error at the earlier
time or changing the apparatus. The weighted candidate and WEIGHTED_REVIEW.md
were read completely before integration. No additional scientific run was made during the weighted analytical check.

The earlier filter b=i reference-plane error was corrected to b=iz, and an
intersecting provisional coordinate path was replaced before the original
arithmetic execution. Identical arms/tree-sign changes are recorded as tried
shortcuts only. No general no-go for real Hamiltonians, endpoint seeds, or
other architectures is asserted.

The structural, quantitative, endpoint-spectral and onset checks are
same-model and source-exposed. They reconstruct distinct load-bearing steps;
they are not blind, model-diverse, retained audit, or independent recertification
of ancestral calibration certificates. The root qualification accepts their
combined implication on pinned sources. Historical author arithmetic and the
quantitative Fraction check corroborate substitutions and small algebra;
they are not whole-apparatus simulations. The canonical publication runner subsequently returned exit0 with151 scoped
checks;25 mathematical and4 integrity mutations failed in their intended
families under python -O. The full execution is recorded in
`outputs/real_endpoint_autonomous_output_2026_10_17_validation/README.md`,
its prelaunch/receipt files and canonical runner cache. No new full-device
simulation was performed. The original requested address-space cap failed;
its receipt preserves that failure and no memory-cap success is claimed.

The source package pins the unchanged mathematical interval/kernel premises,
complete proposal and correction history, and exposed review reports. The
initial publication cache bound its runner and43 declared inputs. The T30
runner declared49 inputs; its historical cache and separate
postexecution evidence preserves actual streams, caps and mutation failures.
Independent audit and combined current-main landing gates remain future work.
This regular review PR does not grant retained status or authorize a merge.

Negative-claim discipline: this is a positive conditional construction. The
historical failed equal-arm and reference-plane shortcuts are specific failed
routes, not an N1-N8-cleared impossibility theorem. No five-family search or
general negative verdict is claimed. Native supply, finite storage and reuse
are open obligations rather than proof of impossibility.

No native physical Hamiltonian, coefficient/state supplier, Record map,
robustness/tolerance composition, practical size, thermal preparation,
all-future finite halt, capture, reset, or reuse result is established here.
These are limits of the present positive theorem, not impossibility claims.


## Additional checked tolerance/runtime tradeoff

The following refinement retains the exact infinite model, kappa=10^-12,
sigma=10^-6, delivered product seed, old K/W, complex target f and beta_t,
scalar c_new, full elapsed aging and residual spectrum defined above. It
proves a different tolerance: complete operator error <.003 for every
`t>=T30=10^30`. The one fixed truncation `M30=50T30=5e31` has error <.004
only on [T30,2T30], with M30+116 qubits. Unhalved trace ceilings are .006
and .008. This does not assert the .0013/.0023 tolerance at the shorter time.

### Selected endpoint column and full emitter inverse

Before input termination, use the actual physical internal blocks
G(m,n)=A Q^|m-n|+Q^m T_aa Q^n, end=ell, b=ell+1 and
X=Q^ell T_aa Q^ell. Since A commutes with Q, without commuting T_aa,

    G(b,end)=Q(A+X), ||A+X||<41.

The previously proved <3e7 site-block ceiling includes every retained arm,
input and output-zero position against end and b. With ||Gbb^-1||<22,
Dirichlet deletion therefore gives, for every retained site s,

    ||Gtr(s,end)||<3e7(1+22*41)=2.709e10<3e10.

There are112 retained background head positions, each with eight internal
coordinates in one parity, before adding the emitter. Let R_bg be this
896-coordinate matching inverse with the unchanged output-tail self-energy,
and E the real endpoint inclusion C^8 -> C^896. The generic terminated
block bound <2e16 and the selected column bound give

    ||R_bg||<112*2e16=2.24e18,
    ||R_bg E||^2<112*(3e10)^2=1.008e23.

No factor eight belongs in these block-operator norms. The actual endpoint
compensation leaves its background diagonal2J: its remaining J bond plus
the new kappa bond and (J-kappa)n_end give2J. The emitter diagonal is E0.
Consequently the actual904-coordinate matching inverse is exactly

    M^-1=diag(R_bg,0)+V De^-1 V^T,
    V=[-kappa R_bg E; I8].

R_bg is complex symmetric in the fixed real physical basis; V^T is not V*.
Nevertheless ||V^T||=||V|| in Euclidean norm, and the separate positive
identity V*V=I+kappa^2(R_bg E)*(R_bg E) gives ||V||^2<1.1008. Using the full
eight-dimensional ||De^-1||<1e23, including complementary directions,

    ||M^-1||<2.24e18+1.1008e23=1.1008224e23<1.2e23.

The unchanged x'=M^-1(iE''u-M'x), ||M'||<.1 and spectral bound
integral|f|||x||<86 yield

    integral|f|||x'||<1.2e23(.061*.002+.1*86)<1.1e24,
    integral|f|||C'||<(7/6)*1.1e24+1e15+86/20<1.3e24.

This last C' still includes the derivative of the subtracted actual
reflected open wave and every closed tail. For pointwise C, each background
diagonal block of M^-1 is <2e16+kappa^2*(3e10)^2*1e23<1e20, while its
emitter diagonal is De^-1. The same positive spectral jump now gives

    ||x||^2<.122*8*(112*1e20+1e23)=1.085312e23<(4e11)^2,
    ||C||<(7/6)*4e11+2<5e11.

Here the factor eight is required for the trace. These are finite-coordinate
bounds, not whole continuous-spectrum resolvent norms.

### A different comparison packet with a paid outgoing discrepancy

For each real old basis column put g_j=omega_p f and a0,j=conjugate(g_j).
This is a scalar coefficient multiplying the same generalized column; no
arbitrary old-input amplitude is conjugated. Actual input coefficients are
conjugate(F_j). Their L2 difference from a0,j is

    <=epsilon_F sqrt(p0)+1-sqrt(p0)<.0007520016.

Adding the actual outside-band amplitude4e-5 and the same sqrt(2) within
parity gives the unchanged complete seed-to-packet bound <.001121.
The comparison packet is mathematical only; it is not newly prepared.

Set e_j=F_j/sqrt(p0)-g_j. The exact real-seed identity
F_j=R_j conjugate(F_j), |R_j|=1, implies

    R_j a0,j-g_j=e_j-R_j conjugate(e_j),
    ||R_j a0,j-g_j||_L2<2epsilon_F=.001504.

This discrepancy is paid once. Fourier evolution and positive-half-line
restriction are contractions, and distinct old columns have orthogonal
open output fibers. Thus .001504 is the operator bound without another
sqrt(2). The final target remains the original common g_j and beta_t.

### Pole-free incoming contour, including both cutoff sides

Write h=sigma/2, alpha=kappa^2/J and analytically continue the conjugate
real-axis coefficient by

    a0,j(z)=conjugate(omega_p zeta0) A_f E'(z) exp(-i113z)/Dbar(z),
    Dbar(z)=E(z)-E0+alpha exp(-iz), A_f<17kappa.

For z=x-iy with x in I and 0<=y<=h, its exact imaginary part is

    Im Dbar=-sin(x)[2J sinh(y)+alpha exp(-y)]<0.

The alpha term is exp(-y), not cosh(y); the latter was an incorrect
intermediate suggestion, corrected before independent review. This proves
holomorphicity with no denominator zero on the closed rectangle, including
y=0. It is not the non-holomorphic operation of conjugating f at complex z.
The full numerator/propagation phase obeys

    |exp[-imz-itE(z)-i113z]|<=exp[-(m+113+vt)y].

For y<=h, cosh(y)-1<=y^2 and |E'(z)|<=2J cosh(y)<.062. At both cutoff
sides x=k0+/-sigma, reverse triangle inequality gives

    |Re Dbar|>=v sigma-.061h^2-alpha>.024sigma.

Thus the coefficient without its phase is <44kappa/sigma on each side.
Keeping both vertical segments, their site-m integral is bounded by
88kappa/[sigma(m+113+vt)]. After Fourier normalization and the lattice sum,

    vertical norm<=88kappa/[sigma sqrt(pi vt)].

On the bottom |Dbar|>=2J sin(x)sinh(h)>vh, so the corresponding coefficient
is <44kappa/h. Its length2sigma and sum_m exp(-2mh) give

    bottom norm<=88kappa sigma exp(-vth)
                    /[h sqrt(2pi(1-exp(-2h)))]
               <88kappa exp(-vth)/sqrt(h)<1.3e-7 exp(-vth).

We used 1-exp(-2h)>=h and sqrt(2pi)>2. The numerical comparison follows by
squaring: (88e-12)^2/(5e-7)=1.5488e-14<1.69e-14. At t>=T30,
sqrt(pi vt)>2e14; the vertical term is <4.4e-19. Dropping the bottom's
decay still yields incoming norm <2e-7. No endpoint is set to zero, and no
resonance-pole location or outgoing-contour assertion is imported. Orthogonal
open fibers again prevent an extra old-column aggregation factor.

### Localized remainder and squared target normalization cost

The actual new localized integrand is a0,j C_j. Since |a0|=|f| and
Vedge(a0)=Vedge(f)<2e12, its integration-by-parts numerator is

    L0<=5e11 Vedge(f)+integral|f|||C'||+(.061/v)*5e11*.002
       <1e24+1.3e24+2.44e9<2.4e24.

There is no 1/R in this new coefficient; removing it without changing the
packet and paying the outgoing discrepancy would be invalid. The R' already
inside C' remains paid. Fourier normalization and sqrt(2) within parity give

    localized operator<2.4e24/[sqrt(pi)vt]<1.5e24/(vt)<6e-5.

For the unchanged full-line Fourier profile b_t, let p_t be its physical
restriction to m>=0 and q_t its negative-half-line norm. Parseval and the
existing tail bound give ||p_t||^2+q_t^2=1 and q_t<.015 at t>=T30.
The positive normalization of the target therefore costs exactly

    ||p_t-beta_t||=1-sqrt(1-q_t^2)
      =q_t^2/[1+sqrt(1-q_t^2)]<=q_t^2<.000225.

Only the physical target restriction is normalized; no actual state or
residual branch is conditioned. A separate linear q_t cost is not needed
because physical outgoing components already have m>=0 support.

The five complete operator costs sum to

    .001121+.001504+.000225+.000060+.0000002=.0029102<.003.

Every term is bounded uniformly for t>=T30. Tensoring passive references
preserves the operator bounds. All finite/internal/closed-channel outputs,
old aging exp(-itK)W and scalar exp(-ic_new t) remain included.

For the separately fixed M30=50T30 truncation, the unchanged polynomial
transfer has exponent <=-[50-36sinh(1)]T30-23<-6.8T30-23, hence difference
<.001 on[T30,2T30]. Adding it gives .0039102<.004. There is no all-future
finite-device guarantee, native supplier or practical-scale claim.

### Refinement review and execution scope

The endpoint-column and conjugate-packet proposals and separate reviews are
frozen under `review_sources/tradeoff/` in the input package. Proposal hashes
are08cf51274fce1209a92c551487ed168ddaf0a1a4eb2edbf99eb2602ab35cf78e and
c49c0f7cd3af2c939085cee80883f4a36024b4979992bba1ee7628eb4b8961ac; review hashes
arebc10c35ec7a16af2b9b218d7077a0f37bbe2dedcbdb807cfa3ca5cbfb62b1a47 and
5df64d41d870b25589e2c783151857c241c301eb2a37e22c054a9102e0322f34.
Root read the full proposals and reviews and qualified their conditional
composition. Checks were same-model and source-exposed, not blind,
model-diverse or retained audit. The corrected contour identity and earlier
failed derivative routes remain preserved. The primary runner adds only
bounded exact algebra/constant substitutions; it does not compute spectral
integrals or certify contour deformation. Current execution evidence is
recorded separately from the original151-check publication run.

The refinement execution passed 179 scoped arithmetic checks and the current
49-input integrity check (exit 0; 0.08790898323059082 seconds). Thirteen new
mathematical mutations failed at their intended checks under Python -O.
Full streams, runtime/source prelaunch identities and resource receipts are
preserved in `outputs/real_endpoint_autonomous_output_2026_10_17_tradeoff_validation/`.
The older mutation results remain historical evidence, not repeated runs.
No whole-apparatus simulation, retained audit or combined-main gate is claimed.

## Checked thin-strip continuation and weighted-profile improvement

The following two refinements retain the exact fixed kappa=1e-12, sigma=1e-6,
apparatus, delivered seed, common f/a0, old aging and all reference/output
conventions. They do not import any proposed coupling family. Original sources,
correction ledger and independent reviews are preserved separately. The complete
core argument and the scalar target argument received separate source-exposed
same-model checks. A distinct check reconstructed the weighted complex mismatch.
No retained audit or simulation is implied.

Set h=1e-23 and T27=1e27. The real-axis selected-column estimate above supplies
||M_j(x)^-1||<1.2e23 uniformly on the original interval. The purpose of the
next argument is to justify a thin continuation of the ACTUAL complete
localized vector; a scalar pole-free contour alone would not suffice.

### Physical matching analyticity and inverse

Use the exact fixed real physical core (113 sites, eight internal coordinates per parity), with all output exterior channels eliminated at the existing physical reference plane. Its energy-dependent entries are lambda(z)=b_j+E(z) on core diagonals and the outgoing lead self-energies J exp(iz) on the selected open direction, J q_l(z) on seven closed directions. Static contacts, emitter coupling and graph coefficients are unchanged. Thus no k-dependent basis is introduced; B spectral projections are fixed. The sign of the self-energy is immaterial for this norm bound but matches the source M. In exact form M_j(z)=(b_j+E(z))I-Hcore+J P_out Q_j(z) P_out*, with fixed spectral projectors in Q_j.

The closed half-line spectral separation can conservatively be bounded below by .17 throughout real I. For nonvacuum sources B>=1+Delta_min, hence their threshold minus b_j+E(k) is at least Delta_min-2-E(k)>.17 since E(k)<.0061. The other vacuum old energy is separated from its entire lead band by more than 1.8. Source excitation number is preserved by B and all added terms in Csrc/Gsrc are positive, so this lower bound is on the whole nonvacuum subspace, not a guessed eigenvalue. The original |q_l|<=1/7 still holds on I.

For |Im z|<=h, |E'(z)|<.062, so |E(z)-E(x)|<.062y. Resolvent analyticity for the closed free half-line, whose endpoint Green function equals -q_l/J up to convention, yields

 |q_l(z)-q_l(x)| <= J |E(z)-E(x)|/[.17(.17-|E(z)-E(x)|)] <2 |E(z)-E(x)|.

Therefore |q_l(z)|<1/6, uniformly, and the chosen decaying roots continue without branch ambiguity. The closed self-energy variation is <.004y. The open variation is J|exp(iz)-exp(ix)|<.031y. Since the boundary projection is orthogonal and there is only the actual output lead boundary, the full matching variation is

 ||M(z)-M(x)|| < (.062+.031)y <.1y.

The physical core includes the terminated stub and emitter; only the output tail m>=1 is eliminated at the retained output site m=0. Thus this energy-dependent boundary occurs exactly once.

Using the published real-axis ||M(x)^-1||<1.2e23, the perturbation norm is <.12 throughout the rectangle. Hence M(z) is analytic/invertible there and ||M(z)^-1||<1.2e23/(1-.12)<1.4e23. Define the analytically continued incoming column x(z)=M(z)^-1 i E'(z) u and reflection R(z)=u^T x(z)-1, with the same real constant u. Then ||x(z)||<9e21. No use is made of unitarity off the real axis.

The localized column C is obtained by subtracting the open incoming/outgoing waves and including all closed tails. On the core, even allowing the subtracted open component via |R|<=||x||+1 gives <=2||x||+2. The closed-tail map has norm <=r_c/sqrt(1-r_c^2)<1/5 for r_c=1/6, multiplying the boundary vector of norm<=||x||. Thus conservatively ||C(z)||<3||x||+4<4e22. This is a holomorphic vector in the fixed finite-core plus closed-tail Hilbert space: the tails are uniformly geometric in that space. This does not continue an infinite full resolvent across its spectrum; it continues a finite matching construction and its decaying closed tails.

### Localized integral

The published conjugate comparison coefficient is a0(z)=conj(omega*zeta0) A E'(z) exp(-i113z)/Dbar(z), A<17kappa, Dbar=E(z)-E0+(kappa^2/J)exp(-iz). For z=x-iy,

 Im Dbar = -sin x [2J sinh y+(kappa^2/J)exp(-y)].

There is no zero in this rectangle, and |Dbar|>12kappa^2. Also |exp(-i113z)|<=1. Thus |a0|<1e11 everywhere. On each vertical side the existing real-part margin gives |Dbar|>.024 sigma and |a0|<44kappa/sigma=4.4e-5. The much thinner h only improves that side estimate.

The time factor has modulus exp(t Im E(z))=exp[-2J t sin x sinh y]<=exp(-vty). A vector-valued rectangle deformation of (2pi)^-1/2 integral_I a0 C exp(-itE) dk is legitimate by the finite-matching and closed-tail analyticity above.

Bottom norm <=(2sigma/sqrt(2pi))*1e11*4e22 exp(-vth)<4e27 exp(-vth).

Two side norms combined <=(2/sqrt(2pi))*(4.4e-5)*(4e22)/(vt)<1.76e18/(vt).

At T=1e27, vTh=250. The bottom is negligible (even e^250>2^250 suffices for <1e-40); side <7.04e-8 per old column. Pay sqrt(2)<1.5 for the two potentially overlapping old-energy columns within parity; different parities remain orthogonal. A complete localized ceiling <3e-7 follows, for every t>=T. Reference tensoring preserves it. Both cutoff edges remain paid.

### Scalar target negative tail, separately

For the actual target f(z)=zeta0 A E'(z) exp(i113z)/Dref(z), the same thin rectangle remains above its reference resonance pole. Indeed

 Im Dref = sin x[(kappa^2/J) exp(y)-2J sinh y] >12kappa^2

at this h, because kappa^2/J>32kappa^2 whereas 2J sinh h<.061h=.61kappa^2. The sin x>.4 margin still leaves >12kappa^2. Thus |f(z)|<2e11 allowing exp(113h)<2. Side real-part margin remains >.024sigma, and the numerator phase can be retained in the time-decay rate vt-113 rather than dropped.

For negative integer m, the bottom geometric l2 sum yields a bound <1e17 exp(-vth), using 1-exp(-2h)>=h, h=1e-23, and 2sigma/sqrt(2pi)<sigma. The exp(113h) is already paid above.

For the vertical sides, integration gives coefficients at most (44kappa/sigma)/(|m|+vt-113), with Fourier factor1/sqrt(2pi), on each side. Since sum_(n>=1)(n+A)^-2<=1/A for A>0, their combined l2 norm <=88kappa/[sigma sqrt(2pi(vt-113))]. At T=1e27 this is <1e-16. Both sides and the bottom imply q_t<1e-16 after a loose margin (the side is actually far smaller than that ceiling). The exact target normalization cost is 1-sqrt(1-q_t^2)<=q_t^2, not postselection of actual output.


### Weighted static comparison on the same fixed apparatus

The next pointwise estimate improves the complete static cost while leaving
the localized coefficient a0=conjugate(omega_p f) and its analytic continuation
unchanged. Define (P) as |F_j/Fref-omega_p|<2e-13+750|k-k0| and (S) as the
combined preparation and outgoing discrepancy <5.68e-5. Both are derived below.

### 1. Preserve momentum distance through the filter

Put s=|k-k0|<=sigma=10^-6. Write r_g for the bare ladder reflection and r_m for the exact filtered-arm reflection, both at the common absolute arm origin. The supplied exact central filter values are a(k0)=0 and b(k0)/z0=i. Their derivative bounds on the unchanged full interval imply

    |a(k)|<=5s, |b(k)/z-i|<=6s.

These are direct fundamental-theorem-of-calculus estimates. They do not shrink the certified interval or treat s as a new parameter-family bandwidth. In the exact concatenation formula

    r_scalar=z^(-2(F+1))a+(b/z)^2 r_g/(1-a r_g z^(2F)),

the same algebra used by the published uniform bound gives

    |r_scalar+r_g| <=5s+17s/(1-5s)<=23s.

The last inequality is strict for s>0; at s=0 both sides vanish.

The complete physical closed-channel correction is still bounded uniformly by

    |r_m-r_scalar| <epsilon_A=1e-20.

It is NOT multiplied by s and is NOT set to zero at k0. This bound retains the seven complementary coordinates and the noncommuting filter response exactly as in the source. Thus

    |r_m+r_g| <23s+1e-20.                               (1)

### 2. Shared-system port reflection and transmission

After the exact Hadamard junction and common reference-plane shift, the diagonal reflection is half the sum and the transmission half the difference of the two arm reflections. Unit-modulus propagation factors change no norm. Equation (1) therefore gives

    |R_j| <=r(s):=11.5s+5e-21,
    |tau_j-z^(2(N+1))r_g| <=11.5s+5e-21.

The bare calibration estimate itself retains its pointwise distance:

    |r_g-r0 zeta omega_p| <=d0+702s.

This follows from its exact central allowance d0 and the supplied derivative bounds |r_g'|<=700, |r0'|=2. Hence

    |tau_j-rho_g omega_p| <=t(s):=d0+713.5s+5e-21.       (2)

In particular r(s)<12e-6 uniformly on I. The source's physical kernel/tail estimates, epsilon_G=1e-22 and epsilon_L=1e-21 continue to apply unchanged. No scalar scattering estimate replaces those full internal interfaces.

### 3. Full emitter denominator, including its nonzero floor

The scalar terminated-end reference is

    g_j=-(z/J)(1+R_j z^(2ell))/(1+R_j z^(2ell+2)),
    g_j+z/J=-(z/J)R_j z^(2ell)(1-z^2)/(1+R_j z^(2ell+2)).

The actual end Green matrix differs from that diagonal reference by <epsilon_G, and both off-diagonal P/Pc norms are <epsilon_G. Complementary emitter elimination is exact:

    D_j=E-E0-kappa^2 G_jj-kappa^4 G_jc D_cc^-1 G_cj,
    ||D_cc^-1||<6,
    Dref=E-E0+kappa^2 z/J.

Divide |D_j-Dref| by Im Dref=kappa^2 sin(k)/J, which is no larger than |Dref|. Using |1-z^2|=2sin(k) gives

    |D_j/Dref-1|
      <=2r(s)/(1-r(s))
          +(J/sin(k))[epsilon_G+6kappa^2 epsilon_G^2].

The second bracket explicitly includes the full complementary Schur term. With J<.031, sin(k)>.4, kappa^2=1e-24 and epsilon_G=1e-22, its contribution is <1e-23; the complementary part alone is <1e-67. Since r(s)<12e-6,

    2r(s)/(1-r(s))
      <=[23s+1e-20]/(1-12e-6).

Its slope is <24 and its constant plus1e-23 is <2e-20. Consequently

    |D_j/Dref-1| <=d(s):=24s+2e-20 <25e-6.             (3)

The same comparison to Im Dref, rather than modulus alone, preserves the positive imaginary-part lower bound. No resonance pole, central zero, complementary emitter removal or kappa-family continuation has been assumed.

### 4. Exact outgoing response and its residual row term

Let DeltaL=L-L0, ||DeltaL||<epsilon_L=1e-21, where

    L0=-(tau_j/J)z^(ell+1)/(1+R_j z^(2ell+2)) P.

Block elimination gives

    D_e^-1 u_j=D_j^-1(u_j+c_j),
    c_j=kappa^2 D_cc^-1 G_cj, ||c_j||<6kappa^2 epsilon_G,
    Aout,j=-kappa L D_e^-1 u_j.

Since L0 Pc=0, the complementary vector does not enter the leading row, but it DOES enter DeltaL(u_j+c_j). Including Stone's unchanged iE'/sqrt(2pi) factor, the normalized scalar ratio is exactly

    F_j/Fref = [tau_j/rho_g]
                 /[(1+R_j z^(2ell+2))(D_j/Dref)] + e_L,j.

All fixed complex phases cancel here only because Fref includes the original rho_g and z^(ell+1); no new per-column phase is chosen. The row remainder obeys

    |e_L,j| <= J epsilon_L (1+6kappa^2 epsilon_G)/(1-d(s))
             <3.2e-23.                               (4)

This pays epsilon_L and its complementary-emitter correction rather than hiding them in a zero central error.

For the leading ratio, subtract omega_p and use (2)-(3). The numerator difference is bounded by t(s)+r(s)+d(s)+r(s)d(s), and the denominator is at least (1-r(s))(1-d(s)). Since r(s)<12e-6 and d(s)<25e-6,

    (1-r)(1-d) > (1-12e-6)(1-25e-6) >.99996,
    r(s)d(s) <=12e-6[24s+2e-20].

It follows explicitly that

    |F_j/Fref-omega_p|
      < [d0+3e-20+2.4e-25+(749+.000288)s]/.99996
          +3.2e-23.

The coefficient of s is <750. The constant, with d0=1.76e-13, is <2e-13. This proves the bound (P) from the pinned source premises by a new analytic derivation. Each central floor remains strictly charged. The calculation establishes a bound on the full complex ratio, not just its modulus or phase separately.

### 5. Actual reference moment without a Lorentzian substitute

The scalar endpoint reference has normalized global emitter spectral measure mu_ref, mean E0 and variance kappa^2. On E(I), dmu_ref=|Fref(k)|^2 dk. Since E'>v on the interval containing k0,

    v^2 (k-k0)^2 <=(E(k)-E0)^2.

Integrating over this interval and using positivity of the omitted global measure yields

    integral_I (k-k0)^2 |f|^2 dk
      =p0^-1 integral_I (k-k0)^2 |Fref|^2 dk
      <=kappa^2/(p0 v^2).

No point mass or missing continuum is discarded to obtain equality of a full moment; only an inequality is used. The actual normalization satisfies p0>=1-1.6e-9, so

    ||(k-k0)f||_2 <=kappa/(v sqrt(p0)) <4.1e-11.

Multiplying (P) by |f| and applying the L2 triangle inequality gives

    delta_j:=||F_j/sqrt(p0)-omega_p f||_2
      <2e-13+750*4.1e-11=3.07502e-8<3.1e-8.           (5)

The hard cutoff and full actual reference shape remain; no small-linewidth asymptotic or infinite-Lorentzian second moment is used. Signed averaging of the complex mismatch would not establish (5).

### 6. Static full-output interface

Use the already published comparison coefficient a0,j=conjugate(omega_p f), multiplying the same actual unit-incoming generalized column. This is a linear basis-column construction and does not conjugate arbitrary old-input coefficients. Actual incoming coefficient is conjugate(F_j). From (5),

    ||F_j-omega_p f||_2
       <=sqrt(p0) delta_j+1-sqrt(p0)
       <3.1e-8+1.6e-9.

Add the unchanged actual off-band amplitude <=4e-5, including point spectrum. Two old-energy residuals within a parity may overlap; multiplying by sqrt(2)<1.415 gives

    preparation operator <1.415*(4e-5+3.1e-8+1.6e-9)
                         =5.6646129e-5<5.67e-5.

Distinct parities are orthogonal. No outside-band or actual-state normalization is changed.

For e_j=F_j/sqrt(p0)-omega_p f, reality and one-channel unitarity give exactly

    R_inst,j a0,j-omega_p f=e_j-R_inst,j conjugate(e_j).

Its L2 norm is <=2delta_j<6.2e-8. Fourier propagation and physical half-line restriction are contractions, and the four open internal output fibers u_j are orthogonal. Thus this is already the complete outgoing operator ceiling without a sqrt(2) multiplier. Summing the two costs gives <5.6762e-5<5.68e-5, proving interface (S).

No derivative estimate changes: the new argument only improves spectral mismatch and preparation. Full elapsed old phase exp(-itK), the original W, c_new and common complex f are unchanged; passive-reference tensoring preserves every operator bound.


### Complete weighted-strip composition and verification limits

The two checked improvements concern the same f, p0, a0, physical C_j and
seed. Weighted comparison replaces only preparation plus outgoing discrepancy;
it changes neither the contour integrand a0 C_j nor the target. With T27=1e27,
all complete operator costs are therefore

    static <5.68e-5,
    localized <3e-7,
    incoming <2e-7,
    positive target normalization <1e-32,
    total <.0000573+1e-32 <.000058.

The original finite transfer against the embedded infinite target adds<.001
on[T27,2T27] for fixed M=5e28, giving<.001058. No truncated target is
renormalized. Unhalved trace bounds are .000116/.002116. Both sharpened
operator bounds are below the original .0013/.0023 pair, at a sufficient
onset15 orders lower than T42. The sites are still astronomical and these
are sufficient bounds, not optimality or physical lower bounds.

The full core, scalar tail, weighted profile and compatibility reports are
frozen under `review_sources/weighted_strip/`. Root read each in full.
These are same-model/source-exposed checks with declared reused premises;
no blind/model-diverse review or retained audit is claimed. The core-only
V1 total .0026255 omitted explicit room for a tiny normalization allowance;
its preserved V2 uses .002626 before the distinct weighted improvement.
The composed .000058 ceiling explicitly has room for that allowance.

The primary runner corroborates scalar constants and exact fixtures only;
it does not establish analytic continuation, Hilbert-valued contour deformation,
spectral synthesis or a whole-apparatus simulation. Current execution and
mutation evidence is recorded separately from the earlier151/179-check runs.

The current weighted-strip execution passed214 scoped arithmetic checks and
59-input integrity, exit0 in .08302688598632812 seconds, with58,926 stdout bytes.
Nineteen new mathematical mutations failed in their intended families under
Python -O. Four current integrity cases rejected altered bytes, symlink file
and ancestor, and nonregular input; inert import produced no output. Complete
receipts, streams and failures are frozen in
`outputs/real_endpoint_autonomous_output_2026_10_17_weighted_strip_validation/`.
The first integration run used stale positional input-path constants; a second
run caught a copied incoming denominator1e13 where8e12 is justified. Both failed
runs are preserved and repaired; neither changes the reviewed theorem. Earlier
151/179-check evidence and mutation results remain separately historical.

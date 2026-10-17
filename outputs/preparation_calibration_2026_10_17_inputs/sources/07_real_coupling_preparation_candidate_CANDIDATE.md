---
title: Finite real preparation of the useful chiral rail sector
status: proposed conditional theorem; separate review required
source_realifier_status: pending separate review
execution_status: see separate EXECUTION.md and actual receipts
scope: exact supplied two-rail apparatus and classical preparation controls
---

# A physical product seed, real local pulses, and autonomous release

There is a concrete candidate route using only real, positive onsite and
ordinary nearest-neighbor two-qubit preparation blocks. It starts from one
excited physical emitter and all other auxiliary qubits blank. Nine local
isolation blocks and five pulse blocks, supported on eight already present
sites, prepare the useful chiral emitter sector and turn off in five units
of Hamiltonian time. The operator seed error is at most `sqrt(2) kappa`,
uniformly in the clock length. The old Hamiltonian remains literally
`K=2I+Z1 Z2` throughout, including both ramps and all three pulses.

The route is conditional on the supplied apparatus, exact initial product
seed and specified real classical control functions. Its transfer to the
halt theorem is also conditional on the pending realifier result. It does
not supply a native controller, thermal delivery, cooling, a phase reference
without cost, autonomous setup, reset or reuse. No postselection, subsystem
discard, old encoding or externally stopped runtime is used. No new complex
static coupling is introduced. Exact pulse areas are an explicit control
permission; they are not inferred from the framework axioms.

For the exact coupling family `10^-12 <= kappa <= 10^-8`, the qualified
resonance bound transfers to complete operator error below `0.00483202`
on the finite window `[T,2T]` after release, where `T=kappa^-2` and each
rail has `M=ceil(50T)` sites. The corresponding unhalved trace distance,
including arbitrary passive references, is below `0.00966404`. These are
conditional sufficient bounds, not measured performance or practical costs.
At the upper coupling endpoint the apparatus still has
`1,000,000,000,000,000,006` physical qubits.

## 1. Sources, exposure and precise inherited premises

The source manifest is [SOURCE_MAP.json](SOURCE_MAP.json). It records exact
copied bytes, original historical paths and capture metadata. Relevant pins:

| Source | SHA256 |
|---|---|
| Realifier ROUTE | c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018 |
| Realifier FREEZE | 16fa2cbf13386826cd6939cc412f66c9224a89eaadd133b2163c5b3130e5829b |
| Exact coupling-family body | 9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac |
| Family root acceptance | a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325 |
| Resonance-family body | 401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0 |
| Resonance-family root acceptance | bb280c96d290e28b42c45994cab3fe9871d671b0d20d39a36ae09d211ef98686 |
| Exact rational ladder parameters | a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251 |
| Earlier product thermal preparation | b7ef6e98b16bcffb609cbf8a9cca2aee03d4bb20ac6295e99c744f488ad14227 |
| Earlier product preparation qualification | 5e4cc2c916d9240ec5bb0b2a84559ae38fd2b20959e63c52d6b3c0bda04a2d69 |

The realifier body and its freeze were read before developing this pulse
route. The author previously authored or reviewed parts of the family,
source certificate, packet bridge and product preparation chain, with the
same model. This is source-exposed author work, not blind or model-diverse
review. The earlier product preparation supplies context for positive
complements and supported Duhamel estimates; its Gibbs construction is not
used here. No realifier checker/output or root's separate unshared pulse
idea was read. The forbidden `real_phase_preparation_idea` directory was
not accessed. The first recorded source exposure in this packet is
`2026-10-17T04:49:01.176316+00:00`.

The owner supplied baseline is PR9665 head
`0e3993770a7a2dd872018f9dd3c76c2d9a624db9`. No Git/remote freshness operation
was performed here. Current workflow and governing discovery/status/delivery
instructions were read at their recorded unchanged revisions. No editable
prompt, axiom, registry, shared checkpoint, repository or audit file changed.

Use the exact inherited constants, with every listed decimal exact:

| Constant | Value | Constant | Value |
|---|---:|---|---:|
| J | .030021107107032 | gA | .996878563816670 |
| gB | .599319315560298 | hAB | 3.999349697888060 |
| u | .544607276405587 | lambdaA | 3.801781381581202 |
| lambdaB | 2.575033765788497 | DeltaA | 2.192035527016003 |
| DeltaB | 2.186826508897014 | mu0 | .321494607058201 |
| nu | 1.459892813020969 | q0 | 4.510351185997098 |

Write `n=(I-Z)/2`, `a=|0><1|`, `Omega=|00>_AB`,
`iota x=x tensor Omega`, `k0=2 arctan(1/q0)`, `phi=2k0`,
`c=cos(phi)>0`, `s=sin(phi)>0`, `d=1+c+s<3`,
`E(k)=2J(1-cos k)`, `E0=E(k0)`, `L=12`, `sigma=10^-6`.
Here `E0>3*10^-8`, so `E0-kappa d` and `E0-kappa` are positive over
the whole closed coupling interval. The exact rational `c,s,E0` are
calculated from the pinned rational `cos(k0),sin(k0)`; no decimal fit is
used to establish a sign.

The literal old target and source are

    K=2I+Z1 Z2,
    W=[(9+12i)I+(-16+12i)X1 X2]/25,
    C=DeltaA nA+DeltaB nB
      +hAB(nA+nB-aA^dagger aB-aB^dagger aA)+u nA nB,
    G=gA nA(I+X1)+gB nB(I+X2), B=K+C+G.               (1)

Both `W*W=I` and `[W,K]=0`, and `B iota=iota K` exactly. Commutation of
K with the full interacting runtime is neither assumed nor true in general.

The inherited complex branch is

    Hg=h0 tensor I+B+P0 tensor VA+P1 tensor VB,
    h0=2J I-J(S+S*), VA=lambdaA(I+XA)+mu0 I,
    VB=lambdaB(I+XB)-nu I,
    V=|12>-exp(i phi)|14>,
    Hplus=[[Hg,kappa V],[kappa V*,B+E0]].              (2)

The finite version adds the positive far-end onsite needed to compress
`h0`. These are statements about the complete old/source/clock one-head
space; each old/source fiber has dimension 16.

## 2. The unchanged real apparatus and its geometry

For any real hopping h on an installed edge uv define

    Q_uv(h)=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u).
    spec Q={0,0,2|h|,2|h|}.                          (3)

Thus Q and `2|h| I_uv-Q` are real positive two-qubit matrices, each with
norm `2|h|`. Identity extension to all other qubits is implicit; none of
these identities is silently omitted from the physical Hamiltonian.

There are two clock rails `c_(n,q)`, `0<=n<M`, `q=0,1`, and physical
emitters e0,e1. Keep the original C,G,K once, without duplicating the old
pair or its source. Install on each rail all `Q(-J)` clock bonds, endpoints
`J n_(0,q)` and `J n_(M-1,q)`, and the positive contact terms

    lambdaA n_(0,q)(I+XA), mu0 n_(0,q),
    lambdaB n_(1,q)(I+XB), nu(I-n_(1,q)).              (4)

The six emitter hopping cells (3), in row-clock/column-emitter convention,
have coefficients

    e0--c12,0 : +kappa,      e1--c12,1 : +kappa,
    e0--c14,0 : -kappa c,    e1--c14,1 : -kappa c,
    e1--c14,0 : +kappa s,    e0--c14,1 : -kappa s.      (5)

Also retain, for q=0,1,

    (E0-kappa d)n_eq,
    kappa(I-n_(12,q)), kappa(c+s)(I-n_(14,q)).        (6)

The sum of (5)-(6) is exactly its six hopping operators plus
`E0(n_e0+n_e1)+2kappa d I` on the whole qubit space. The two vacancy
contacts in (4) contribute `2nu I`. On the invariant one-head sector the
physical runtime therefore satisfies

    HR=HRtilde+cR I, cR=2nu+2kappa d,
    HRtilde=A tensor I_rail+D tensor Jf,
    Hplus=A+iD, Jf=[[0,-1],[1,0]].                    (7)

The physical chiral state

    xi+=(|0>-i|1>)/sqrt(2), Jf xi+=i xi+              (8)

reduces HR exactly to `Hplus+cR I`, for either infinite or compressed
finite rails. This invariant-sector identity is the realifier dependency
being reused conditionally. Its negative conclusion for the unprepared
physical seed does not apply once the sector is prepared by active controls.

All controls below use existing edges. Put `m=c_(14,0)`. The eight touched
sites have coordinates

    e0=(8,2,1), e1=(9,3,1), m=(9,2,1),
    c12,0=(8,1,1), c12,1=(9,3,0), c14,1=(8,3,1),
    c13,0=(9,1,1), c15,0=(10,2,1).                   (9)

Both e0--m and m--e1 are ordinary NN edges. Every edge in (5), plus
m--c13,0 and m--c15,0, has Manhattan distance one. The full two-rail
embedding, source contacts and old/source square are the exact coordinates
in the realifier section 3. In particular old1=(0,0,0), old2=(1,0,0),
A=(0,1,0), B=(1,1,0). There are no new qubits, diagonal edges, crossings
interpreted as interactions, or three-body terms. Require M>=16 so c15,0
is present. All proposed horizon sizes satisfy this.

## 3. Nine local positive blocks isolate a three-position core

Let F be the eight installed edges consisting of all six edges (5) and the
two clock bonds incident to m. On each such edge h is its actual signed
runtime hopping. Add the time-controlled positive operator

    R=sum_(uv in F) [2|h_uv| I_uv-Q_uv(h_uv)]
                        +(E0-kappa)n_m.             (10)

There are eight two-qubit complements and one positive onsite pin. They
are real and use neither an old nor a source site. R is a full-space
operator, not a subtraction made only after restricting a sector.

Let E_a map an arbitrary literal old vector into old tensor source vacuum
and the single head at a. The three-position core is the range of
`E_S=(E_e0,E_m,E_e1)`. Put

    cseed=E0+cR,
    r=4J+3kappa d,
    Ciso=cseed+r=E0+2nu+4J+5kappa d.                 (11)

Then the exact supported intertwining is

    (HR+R) E_S = E_S [K tensor I_3+Ciso I].          (12)

Proof: the six emitter hoppings and both clock hoppings leaving m cancel
as full operators. The sum of their complement constants is
`Sb=4J+4kappa d`. In the one-head representation before adding those
constants, the emitter diagonal E0 loses kappa d. The m diagonal 2J loses
`2J+kappa(c+s)` and gains `E0-kappa`, also giving `E0-kappa d`.
Every core diagonal is therefore `cR+Sb+E0-kappa d=Ciso`. Source terms
vanish on Omega and no core head is at a source contact. Only literal K
acts on the old vector. This proves invariance as well as equality of the
three scalars, for every M>=16. The far endpoint at c15,0 when M=16 has
no effect because its head amplitude is zero in this core.

For either physical emitter the stronger supported identities are

    HR E_eq = E_eq(K+cseed I)+kappa Vq,
    R E_eq = r E_eq-kappa Vq,                       (13)
    V0=E_c12,0-c E_m-s E_c14,1,
    V1=E_c12,1+s E_m-c E_c14,1,
    (V0,V1)*(V0,V1)=2I_old tensor I_rail.            (14)

The cross term is `-cs+sc=0`, and each diagonal is `1+c^2+s^2=2`.
Thus V is a scaled isometry with Gram `2I`, not a unit isometry. For
every normalized rail vector z, `||Vz||=sqrt(2)`, simultaneously for
all old inputs and passive references. This is what makes the ramp error
independent of M. A bound using the extensive full-space norm of HR is
unnecessary and would miss this useful local property.

Omitting the pin in (10) fails: the m diagonal differs from either emitter
diagonal by `-(E0-kappa)`. This is a real obstruction to the simpler
eight-complement pulse calculation, not a no-go for other controls.

## 4. An explicit five-unit, finite-slew real schedule

All added controls are zero at the initial time and after time 5. The
installed HR remains literal at every time. Let

    q(x)=30x^2(1-x)^2, 0<=x<=1,
    u_up(x)=3x^2-2x^3, u_down(x)=1-u_up(x).          (15)

The pulse profile has integral 1, maximum 15/8, zero values and first
derivatives at both endpoints, and `max|q'|=10sqrt(3)/3`.
The ramps have integral 1/2 and maximum derivative magnitude 3/2.
Extension by the adjacent constant values makes all control coefficients
continuously differentiable. No ideal instantaneous quench is used.

During `[0,1]` use `H=HR+u_up(t)R`.
During `[1,4]` keep R fully on and apply the following three disjoint
unit-window pulses, with x the local time in that window:

| Window | Positive blocks added | Weight |
|---|---|---|
| [1,2] | `n_e0+n_m+hop(e0,m)` and `n_e1` | `w1=(pi/4)q(x)` on both |
| [2,3] | `n_m+n_e1-hop(m,e1)` and `n_e0` | `w2=(pi/2)q(x)` on both |
| [3,4] | `n_e1` | `w3=(pi/2)q(x)` |

Here `hop=a_u^dagger a_v+a_v^dagger a_u`. Each pair block is Q(+1)
or Q(-1); all weights are nonnegative real. The spectator onsite in the
first two windows is necessary for the common core phase below. During
`[4,5]` remove R using `H=HR+u_down(t-4)R`, with no pulse present.
After time 5 every new control and its first derivative is exactly zero;
only HR governs the subsequent evolution.

In core basis `(e0,m,e1)`, the three pulse generators are

    P1=I_3+X_(e0,m), P2=I_3-X_(m,e1), P3=|e1><e1|. (16)

The off-pair spectator entries of X are zero. On the exact invariant core
(12), the old factor and Ciso commute with these head operations. The
explicit pulse product gives

    exp[-i(pi/2)P3] exp[-i(pi/2)P2] exp[-i(pi/4)P1]|e0>
       =exp(-3pi i/4)(|e0>-i|e1>)/sqrt(2).          (17)

Indeed the first exchange creates `(e0-i m)/sqrt(2)` with common phase
`exp(-i pi/4)`. The negative second exchange sends m to `+i e1`, with
common phase `exp(-i pi/2)`, producing `(e0+e1)/sqrt(2)`. The final
positive onsite pulse multiplies e1 by `-i`. Reversing the sign of the
second exchange instead selects the orthogonal chirality; the sign is
load-bearing. No pulse generator is complex, although its real-time
unitary need not preserve real vectors.

## 5. Supported ramps, exact old aging and the complete seed bound

For any fixed normalized rail vector z and ramp u(t), the comparison
isometry

    A_z(t)=exp{-i integral_0^t[cseed+r u(v)]dv}
                            E_z exp(-itK)           (18)

has initial value E_z. Equations (13)-(14) imply the exact residual

    [H(t)A_z(t)-i dA_z(t)/dt]
       =kappa[1-u(t)] exp{-i integral[cseed+r u]}
                                      V_z exp(-itK).

Variation of constants and unitarity, without a bound on ||HR||, give

    ||U_u(t)E_z-A_z(t)||
       <=sqrt(2) kappa integral_0^t |1-u(v)|dv.       (19)

This is an operator norm statement on all old columns. It remains true
after tensoring any reference identity. For both unit ramps the integral
is 1/2, so each ramp costs `kappa/sqrt(2)`. The first actual ramp's
error is propagated through the later exact unitaries; the pulse calculation
is used only for the ideal comparison state. No claim that the leaked
part stays in the three-position core is needed.

Let Usetup be the actual full five-unit propagator. Let

    Echi=(E_e0-i E_e1)/sqrt(2),
    Phi=5cseed+4r+3pi/4.                             (20)

The ramps contribute `2cseed+r`, the three flat-core windows contribute
`3Ciso`, and the pulse common phase is `3pi/4`. Combining (17)-(19),

    ||Usetup E_e0-exp(-iPhi)Echi exp(-i5K)||
                         <=sqrt(2)kappa.             (21)

Every old energy has the same scalar Phi. The old aging is exactly five
units of K on the ideal branch, not a preparation-time reset or an
unproved commutation through the true dynamics. The error includes any
old/source entanglement and any clock/emitter leakage produced during
the ramps. No trace over those systems occurs.

If exact pulse areas or ramps are perturbed, a finite control tolerance
can be stated without redoing scattering: for actual added control
`A(t)+DeltaA(t)`, Duhamel adds `integral_0^5 ||DeltaA(t)||dt` to (21).
For errors supported on these finitely many blocks this bound remains
independent of M. Positivity/reality and slew must still be separately
maintained by an admissible perturbation; arbitrary perturbations are not
asserted to preserve the hardware class. No such tolerance is silently
included in the numerical error quoted above.

## 6. Transfer into the unchanged autonomous runtime

The new preparation theorem needs only this inherited runtime implication:
for the exact complex seed E and some complete common output isometry B_t,

    ||exp(-itHplus,M)E-zeta B_t exp(-itK)W||<epsilon_M(t). (22)

All embeddings into the common infinite comparison space are understood
as in the family/resonance statements. In particular the finite output
is compared with the same normalized infinite-half-line packet, not a
new finite truncation or renormalization.

The qualified resonance family provides (22) with
`epsilon_infinite(t)<.003832` for every `t>=T=kappa^-2` and
`epsilon_M(t)<.004832` on `[T,2T]` for `M=ceil(50T)`.
Its comparator uses the one actual normalized function

    b_t(n)=(1/sqrt(2pi)) integral_I
                     f_kappa(k)rho_kappa(k)exp[ikn-iE(k)t]dk,
    beta_kappa,t=b_t/||b_t||_(n>=0),
    zeta=-exp(-4ik0)alpha, |alpha|=1.                (23)

Here alpha is the exact inherited site-one reflection witness in channel
`s=-1,p=-1`; it is not rounded or fitted anew. One f_kappa rho_kappa is
shared by all four old columns, whose total scattering energies differ
with the old energies 1 and 3. The inherited spectral-mass, old-energy
channel, closed-tail, bound-state, derivative, normalization and finite
distance arguments are reused by their pinned identities and scope.
The nonzero central target residual `<1.76*10^-13` remains charged in
their reflection budget. This packet does not rerun or independently
reprove those scattering certificates.

Map B_t into the physical two-rail apparatus with fixed rail factor xi+,
empty e0/e1 and source vacuum, calling the result `B_t^R`. This map is an
isometry and retains every rail, emitter and source qubit. Equation (7)
transfers (22) with the extra phase `exp(-icR t)`. Compose it with (21)
and use `[W,K]=0` only on the ideal comparator to obtain

    ||exp(-itHR,M)Usetup E_e0
       -zeta exp[-i(Phi+cR t)] B_t^R exp[-i(t+5)K]W||
                  < epsilon_M(t)+sqrt(2)kappa.        (24)

This gives `<.00483202` for the stated finite window and `<.00383202`
for the infinite apparatus at all t>=T. The preparation and runtime
limits are conditional on (7) and the inherited exact-ladder runtime
premises. The parent realifier was frozen before the newer resonance
acceptance, so using the latter is an explicit new interface composition,
not a claim that the older realifier already contained its improved onset.
Alternatively its original family bound `<.004` infinite and `<.005`
finite transfers by exactly the same algebra, at its larger onset
`10^6/kappa^2` and clock size `ceil(50*10^6/kappa^2)`.

For any density matrix of the old pair and an arbitrary passive reference,
two isometries at operator distance eta induce unhalved trace distance
at most 2eta: expand `U rho U*-V rho V*` into two terms and use
`||AXB||_1<=||A||||X||_1||B||`. Tensoring a reference leaves the
operator distance unchanged. Thus the complete finite bound is
`<.00966404`. It includes the rail coherence as an output, even though
that coherence is independent of the old input in the ideal branch.

The delivered seed is an exact pure product across the old/reference
system and all ancillary sites, with only e0 occupied. An exact pure
auxiliary marginal would force the same factorization for any extension.
No finite-temperature claim is made. An independently supplied initial
state within unhalved trace distance delta of this product would simply
add delta by unitary invariance; deriving such delta from a Gibbs device
or a correlated delivery model is a separate obligation. It is not
provided by the preparation schedule here.

Total elapsed physical time is `5+t`. Relabeling t as time since release
does not reset the old pair or clock. No finite clock is asserted to work
forever; after release no control is used to stop or catch its evolution.
The static/coupling/calibration boxes outside this exact family are excluded.
No arbitrary-accuracy or exact-W limit follows from these fixed bounds.

## 7. Counts, incident loads and finite slew

For M sites per rail, the unchanged apparatus contains `2M+6` qubits,
one-head dimension `16(2M+2)`, and full dimension `2^(2M+6)`.
No such exponentially sized matrix is used in the argument or corroboration.
There are `2M+28` positive runtime blocks excluding K: `2M+12`
two-qubit blocks and 16 onsite blocks. Preparation adds 14 channels:
the nine in (10), two pair pulses, two spectator onsite pulses and one
onsite phase pulse. Counting separate time profiles separately gives
`2M+42` blocks excluding K; some onsite hardware can be shared but no
such economy is assumed. They use eight existing sites and eight existing
edges, and only e0--m--e1 participates in nontrivial pulse transfer.

The sum of the nine isolation block norms is

    Aiso=4J+4kappa d+E0-kappa <1/7.                  (25)

Its incident additions are `2kappa d` at either emitter;
`4J+2kappa(c+s)+E0-kappa` at m; `2kappa(c+s)` at c14,1;
`2kappa` at either c12; and `2J` at c13,0 and c15,0.
No old/source/boundary contact is altered. Each of those norms is an
actual full positive block norm; a scalar subtraction is never used to
discount an incident load.

The following are peak incident sums during the whole setup. Separate
pulse windows are maximized, not incorrectly added as if simultaneous:

| Site | Peak sum, excluding K at the old sites |
|---|---|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| A | 27.936224853155858 |
| B | 22.228906875353305 |
| either c0 | 8.015120691541701 |
| either c1 | 6.730044773026091 |
| m=c14,0 | `8J+E0+5kappa(c+s)-kappa+15pi/8` |
| e0 | `E0+3kappa d+15pi/16` |
| e1 | `E0+3kappa d+15pi/8` |
| c14,1 | `4J+5kappa(c+s)` |
| either c12 | `4J+5kappa` |
| c13,0 | `6J` |
| c15,0 | `6J`, or `5J` if M=16 |
| other interior clock site | `4J` |
| an untouched finite far end | `3J` |

The old edge has separate norm 3 and is unchanged. The original added
old-site cap two therefore holds through preparation as well as runtime;
there is no claim of a cap two at source/contact sites. The largest
source load remains below 28. The peak total norm sum of just the added
controls is bounded by `Aiso+45pi/16<9`.

For a site, define the control slew load as the sum of `||dA_b/dt||`
over incident added blocks b. During either ramp it is at most
`(3/2)Aiso<3/14`. During the pulses its largest value is
`10pi sqrt(3)/3<20`, from either of the active pair sites in the second
window. The onsite spectator has a smaller value. Thus a supplied
incident slew allowance 20 suffices, with finite strengths specified above.
The bound is independent of M and kappa in the stated interval.

At kappa=10^-8, T=10^16 and M=5*10^17, so the onset from initial
delivery is `5+10^16`, the compared window ends at `5+2*10^16`, and
the device has `10^18+6` qubits. These are Hamiltonian units, not seconds.
The five-unit setup reduces a static phase permission; it does not remove
the enormous existing runtime resource requirement.

## 8. Identity coefficients, energy and classical work

Full-space identity coefficients and supported scalar energies differ.
For the full Pauli expansion on the finite device, including K, the
coefficient of the global identity in HR is exactly

    alpha_R=2+(DeltaA+DeltaB+gA+gB)/2+hAB+u/4
              +2JM+lambdaA+lambdaB+mu0+nu+E0+2kappa d. (26)

Its positive block norm sum excluding K is

    S_M=DeltaA+DeltaB+2hAB+u+2(gA+gB)+4JM
            +4(lambdaA+lambdaB)+2mu0+2nu+2E0+4kappa d. (27)

These extensive quantities are not replaced by the much smaller seed
energy. For R the full-space identity coefficient is

    alpha_iso=2J+2kappa d+(E0-kappa)/2.               (28)

Pulse windows one and two add identity coefficient `3w_j/2`; window
three adds `w3/2`. Since R is ramped with total area four, the exact
integrated full-space identity coefficient during setup is

    5alpha_R+4alpha_iso+11pi/8.                      (29)

By contrast, the actual supported phase outside old K in (21) is Phi,
because nonidentity operators have nonzero action on the seed/core. The
identity part `2I` of old K remains inside `exp(-i5K)`; it is not omitted
or counted again in Phi. Equation (24) likewise keeps `cR t` and the
old aging separately. Equations (26)-(29) explicitly retain all positive
complement and vacancy constants even when an involved head site is empty.

For an arbitrary old/reference input, the initial physical mean runtime
energy is `Tr(K rho_old)+cseed`. For the ideal flat-core state during
pulses the mean base energy is `Tr(K rho_old)+Ciso`; pulse contributions
must additionally be included while their weights are nonzero. Those
ideal statements are not substituted for the actual ramped state's work.

Let A(t) be the entire added control and rho(t) the actual unitary state.
In a finite apparatus, its classical work, with the same Hamiltonian
energy units, obeys the exact identity

    Wsetup=integral_0^5 Tr[rho(t) dA(t)/dt]dt
          =Tr[HR rho(5)]-Tr[HR rho(0)],              (30)

because A(0)=A(5)=0. The onset ramp has nonnegative work at most Aiso;
the final ramp has nonpositive work of magnitude at most Aiso. Each
ideal isolated pulse has zero net work, but the actual leaked component
need not, so no zero actual pulse work is claimed. Independently of that
component and of M,

    |Wsetup| <= integral_0^5 ||dA/dt||dt
       <=2Aiso+6 max(w1)+6 max(w2)+2 max(w3)
        =2Aiso+165pi/16 <33.                        (31)

The pair-plus-spectator pulse has full-space norm at most 3w, yielding
the factors six for a smooth rise and fall. The bound uses actual full
block norms, not a one-head projection. It does not calculate the
controller's fabrication, heat, phase reference or reset cost. Those
remain supplied classical-control resources outside this conditional
unitary device model. Every modeled qubit and passive reference remains
in the complete output.

## 9. What is new, what is tested, and what remains conditional

The new load-bearing claims are the nine-block core identity (12),
supported Gram identity (14), explicit positive pulse product (17),
two length-independent ramp estimates (19)-(21), complete interface
composition (24), and finite resources/scalars/work (25)-(31).
The ordinary real positive cells and the exact two-rail decomposition
come from the pending realifier, with the new local algebra independently
reconstructed here. The spectral and finite-horizon claims retain the
qualified exact-ladder family/resonance premises. Neither another PASS
line nor this source-exposed author's calculation makes the whole chain
independent or retained.

The bounded checker is independently written for this route. It uses
exact rational/symbolic kappa algebra, at most 4x4 dense matrices, and
sparse Pauli action on twelve core basis columns for each M=16 and 17.
It checks the full local positive cells, pulse signs and scalar phase,
runtime/isolation identity coefficients, norm counts and incident loads,
and exact supported seed/core actions. It also checks that omitting the
pin destroys the flat core and that reversing the second exchange selects
the wrong chirality. These are corroborating discriminators, not an
optimizer, grid proof, huge-clock dynamics or inherited checker replay.
The all-M proof is the symbolic edge/diagonal cancellation in section 3,
and the all-time error proof is the operator Duhamel estimate, not the two
finite fixtures. Actual execution and any failures are recorded separately
in [EXECUTION.md](EXECUTION.md), with genuine prelaunch source/runtime
bindings and complete streams; see [RESOURCE_PLAN.json](RESOURCE_PLAN.json).

Before claiming this as a checked conditional theorem, separate review
should verify the supported scalar cancellation, signs and spectator phases,
all-M release error, literal old aging, complete output and realifier-to-
resonance interface. If those checks pass, the reduction obtained is from
complex installed hopping to real installed hopping plus finite supplied
real preparation controls. The missing native preparation/controller
supplier, exact pure seed delivery and enormous finite apparatus remain
explicit permissions. There is no claim of an autonomous real preparer,
thermal supply theorem, no-go for other real devices, arbitrary-accuracy
closure or physical identification of the framework.

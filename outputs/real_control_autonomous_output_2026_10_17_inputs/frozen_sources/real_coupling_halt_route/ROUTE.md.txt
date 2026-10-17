---
claim_type: exploratory_worked_failure
actual_current_surface_status: unqualified-author-candidate
independent_review: pending
general_real_coupling_no_go: false
native_phase_permission_closed: false
physical_axiom_changes: none
---
# A local realification and its complete gate/bypass output

The standard realification of the installed emitter can be implemented here
using two clock rails, real coefficients, positive ordinary-nearest-neighbor
two-qubit terms, and the literal old qubits. An explicit cubic embedding and
the full scalar and load costs are given below. It does **not** solve the
product-seed halt target. Its allowed seed, one excited physical emitter and
otherwise blank auxiliary qubits, has equal weights in two conserved conjugate
sectors. At late times one sector performs the target gate and the other emits
the identity operation. Both outputs are retained.

Conditional on the qualified exact-ladder family premises listed in section 1,
this construction's complete output has operator distance **greater than 0.53**
from every old-independent ancillary waveform times the target gate, for every
`t >= T=10^6/kappa^2` on the infinite graph. For two rails of
`M=ceil(50T)` sites it has distance **greater than 0.52** throughout `[T,2T]`,
under the stated embedding into the infinite output space. These are failure
bounds for this particular construction and preparation, not a prohibition on
all real Hamiltonians, other seeds, or earlier transient times.

Realification is established prior art, not a new architecture. The concrete
result of this attempt is the physical two-body realization and the quantitative
complete-output falsifier for applying that architecture to this exact emitter.
This is author work with one bounded exact corroboration, awaiting a separate
decisive check. It requests no audit status or publication.

## 1. Exact dependencies, target and prior exposure

Keep the literal old pair and gate

    K = 2I + Z1 Z2,
    W = [(9+12i)I + (-16+12i)X1 X2]/25.

For P=X1X2, the two gate eigenvalues are

    omega_plus=(-7+24i)/25,  omega_minus=1.                 (1)

In particular W is not scalar. Both parity sectors have a real old eigenvector
with K energy one: `( |01> +/- |10> )/sqrt(2)`. They will be a falsifier that
does not conflate different old aging phases.

`SOURCE_MANIFEST.json` records sixteen byte-preserved inputs and read coverage.
The controlling source is `inputs/family.md`, SHA256
`9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac`.
Its separate root acceptance is
`a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325`,
and qualification is
`27a4008d6588fef9f0a5ac1d231d71240c12468db93d50a36ac2ee02f6ab7814`.
Historical provisional labels in that unchanged body are not edited. The
qualification permits conditional reuse; it is not retained audit.

The exact installed, generic, moment, interval and local-emitter arguments
are reused by their pinned snapshots. Their complete relevant arguments had
already been authored or checked by this agent during this campaign. The
complete family argument and qualification were read, and all mathematical
sections used here were refreshed. This is substantial source exposure by the
same model, not blind or model-diverse review. No old scientific checker was
replayed. The newer resonance-family packet under separate review is not a
premise. Calibration and joint static boxes are excluded.

The parent supplied repository baseline is PR9665 head
`0e3993770a7a2dd872018f9dd3c76c2d9a624db9`. Current local workflow and relevant
wrapper bytes were read and hashed; there was no Git or remote freshness
operation. The primitive registry and realized-state primitive were read.
No registered primitive is treated as a missing axiom, and no primitive is
credited with supplying the specific blank/chiral state or Hamiltonian.

For clarity, the exact inherited apparatus is reproduced. Write `n=(I-Z)/2`,
`a=|0><1|`, source vacuum `Omega=|00>_AB`, and `iota x=x tensor Omega`:

    C = DeltaA nA + DeltaB nB
        + hAB(nA+nB-aA^dagger aB-aB^dagger aA) + u nA nB,
    G = gA nA(I+X1)+gB nB(I+X2),  B=K+C+G,
    VA=lambdaA(I+XA)+mu0 I, VB=lambdaB(I+XB)-nu I,
    Hg=h0 tensor I+B+P0 tensor VA+P1 tensor VB,
    h0=2J I-J(S+S*), E(k)=2J(1-cos k),
    V=|L>-exp(i phi)|L+2>,
    Hplus=[[Hg,kappa V],[kappa V*,B+E0]].                  (2)

All decimals below are exact, as in the inherited family:

| Coefficient | Value | Coefficient | Value |
|---|---:|---|---:|
| J | 0.030021107107032 | gA | 0.996878563816670 |
| gB | 0.599319315560298 | hAB | 3.999349697888060 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| DeltaA | 2.192035527016003 | DeltaB | 2.186826508897014 |
| u | 0.544607276405587 | mu0 | 0.321494607058201 |
| nu | 1.459892813020969 | q0 | 4.510351185997098 |

Set `k0=2 arctan(1/q0)`, `phi=2k0`, `E0=E(k0)`, `L=12`,
`sigma=10^-6` and `10^-12 <= kappa <= 10^-8`. In particular `B iota=iota K`
exactly, but K is not assumed to commute with the contact dynamics. The original
physical operator is `Hplus+(nu+2kappa)I`. Its real seed is `E x=|e> iota x`.

Here are the precise inherited estimates needed, with the same actual common
envelope f and absolute-site convention as the family:

    Gamma_t e_j=(1/sqrt(2pi)) integral_I f(k) Phi_j(k) e^(-itE(k)) dk,
    Phi_j(k,n)=[e^(-ikn)+R_j(k)e^(ikn)]u_j+C_j(k,n),
    exp(-itHplus)Gamma_0=Gamma_t exp(-it Db),
    Gamma_t*Gamma_t=I, ||E-Gamma_0||<0.003,
    ||f||2=1, f in H1_0(I), |R_j|=1,
    kappa^2 ||f'||2<1/100, |R_j'|<1000/kappa^2,
    ||localized packet||<3/[sqrt(2pi)kappa^2 v |t|],
    v=1/40<E', |E''|<=2J, 2J/v<5/2.                     (3)

The localized estimate includes both old energies in each parity, all seven
complementary emitter coordinates in that parity, the entire finite core and
all closed tails. It follows from the Hilbert-valued product bound in family
(49)-(50); its integration-by-parts proof works for both signs of t and after
entrywise conjugation. The seed bound includes any point spectrum and any
component outside the compared scattering range. No such component is removed.

For normalized `g in H1_0(I)`, the inherited position estimate gives the
unwanted half-line norm

    ||g'||2/(v t)+2J sigma/v,  t>0,                       (4)

for the incoming wave on `n>=0` and the outgoing wave on `n<0`. It is an
upper bound with a spread allowance, not a claim of a nonzero physical tail.
Exact packet normalization in (3) uses the separate decaying past-limit
argument, not this allowance. The forward family conclusion is

    ||exp(-itHplus)E
       - zeta beta_plus(t) tensor iota exp(-itK)W||<0.004,
    t>=T=10^6/kappa^2.                                  (5)

Here beta_plus is the actual normalized half-line Fourier wave of `f rho`,
and the fixed unit-modulus scalar `zeta=-exp(-4ik0)alpha` is inherited. Equation
(5) has removed only the known original physical scalar. No phase is fitted
separately to an old column.

## 2. Realification without encoding the old pair

All old/source matrices in (2) are real. Write `Hplus=A+iD`, where A is real
symmetric and D is real antisymmetric in the clock/emitter and real internal
basis. Only the two-contact hopping phase contributes to D. Double the
clock/emitter position label into rails q=0,1, while leaving the old/source
qubits literal. With the logical rail matrix

    Jf=[[0,-1],[1,0]],
    xi_plus=(|0>-i|1>)/sqrt(2),
    xi_minus=(|0>+i|1>)/sqrt(2),
    HRtilde=A tensor I + D tensor Jf,                    (6)

HRtilde is real symmetric and commutes with Jf. Its restrictions are Hplus
on xi_plus and `Hminus=conjugate(Hplus)` on xi_minus. The old Hilbert space
has not been real-encoded, conjugated or measured; (6) is a complex-linear
unitary block decomposition valid for arbitrary complex old/reference input.
The flag is a logical description of two physical head positions, not a free
physical qubit with unexplained controlled hoppings.

Put `c=cos(phi)>0`, `s=sin(phi)>0`, `d=1+c+s<3`. The hoppings, in row-clock,
column-emitter convention, are precisely

| Bond | Real hopping |
|---|---:|
| e0--c_(L,0), e1--c_(L,1) | +kappa |
| e0--c_(L+2,0), e1--c_(L+2,1) | -kappa c |
| e1--c_(L+2,0) | +kappa s |
| e0--c_(L+2,1) | -kappa s |

The two opposite cross signs matter. The exact six-dimensional check retains
the nonzero intertwining defect obtained by reversing the first cross sign.
Every bulk clock edge has hopping -J on its own rail. Source A is coupled
to both c_(0,q), source B to both c_(1,q), with their original coefficients.
The single old/source operator B is not duplicated.

## 3. Positive full-qubit terms, exact scalar and ordinary NN embedding

For every installed real hopping h between physical qubits u,v use

    Q_uv=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u).   (7)

Its full four-dimensional spectrum is `0,0,2|h|,2|h|`, so it is positive
with norm `2|h|`. In addition to the six cells above, use for each q

    (E0-kappa d)n_(e,q),
    kappa(I-n_(L,q)),
    kappa(c+s)(I-n_(L+2,q)).                            (8)

The exact rational center gives `E0>3*10^-8`, hence all emitter onsite
coefficients are positive throughout the declared interval. The sum of
(7)-(8) is the desired real emitter hopping plus the two emitter energies,
and **2 kappa d I**. This is an identity on the entire qubit space: occupation
coefficients cancel individually, not merely after setting head number to one.

On each rail use the ordinary positive clock bonds and `J n_(0,q)`;
use `lambdaA n_(0,q)(I+XA)+mu0 n_(0,q)` and
`lambdaB n_(1,q)(I+XB)+nu(I-n_(1,q))`. The two copies of the last vacancy
term give **2 nu I**, not nu I. Thus on the invariant one-head sector the
actual physical operator is exactly

    HRphysical=HRtilde+cR I,
    cR=2nu+2kappa(1+c+s).                               (9)

It differs from the original branch's physical scalar by
`nu+2kappa(c+s)`. Both the mean energy and the comparator phase retain (9).
All remaining C and G terms in (2) are positive two-qubit or onsite blocks
with real coefficients, and K is the unchanged positive old edge. The
full-qubit Hamiltonian conserves total clock/emitter head number. Equality
with (6) is claimed in its invariant one-head sector, not as an unrestricted
many-head realification. On the infinite graph the finite-number clock
restrictions are bounded selfadjoint positive operators; their orthogonal
direct sum, with the finitely many bounded contacts and internal terms,
defines the vacuum finite-excitation representation used here.

An explicit Z^3 embedding shows that no diagonal edges or three-body flag
controls were hidden. Put

    old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0),
    e0=(8,2,1), e1=(9,3,1).

Rail 0 has

    c0=(0,1,1), c1=(1,1,1), c2=(1,1,2), c3=(1,1,3),
    c_n=(n-2,1,3)                    for 4<=n<=10,
    c11=(8,1,2), c12=(8,1,1), c13=(9,1,1), c14=(9,2,1),
    c_n=(n-5,2,1)                    for n>=15.

Rail 1 has

    c_n=(n,1,-1)                     for 0<=n<=9,
    c10=(9,2,-1), c11=(9,3,-1), c12=(9,3,0),
    c13=(8,3,0), c14=(8,3,1),
    c_n=(8,n-11,1)                   for n>=15.           (10)

Every consecutive clock pair, each of the six emitter bonds, the old/source
square edges and all four clock/source contacts has Manhattan length one.
Coordinates are distinct. For the tails, rail 0 has x>=10,y=2,z=1, while
rail 1 has x=8,y>=4,z=1; neither intersects the core or the other tail.
Incidental nearest neighbors carry no extra interaction. A supplied device
may select which allowed edges are installed. This is not a derivation of
its fabrication or state supply from the framework axioms.

## 4. Product seed, resource costs and the forbidden shortcut

The allowed physical seed excites only e0. Every other clock/emitter qubit
and both source qubits are zero, in product with the arbitrary old/reference
state. In the logical rail description,

    |e,0> = (|e>xi_plus+|e>xi_minus)/sqrt(2).             (11)

Each conserved sector has weight one half. The same weights hold for any
normalized real rail vector at the emitter, since a real vector's expectation
of the antisymmetric Jf vanishes. This additional observation does not claim
that every such superposition is a physical product state.

Selecting only the successful sector would require the physical seed
`(|1_e0 0_e1>-i|0_e0 1_e1>)/sqrt(2)`. It is an entangled one-head state with
a prescribed relative complex phase, not the allowed one-qubit product seed.
If it were supplied, (6) would reduce exactly to the original branch; that
would move the open phase/preparation resource into the input. No autonomous
preparer for it is constructed here. Conservation of Jf prevents this HR
itself from changing (11)'s sector weights. This does not forbid another real
preparation Hamiltonian from doing so before an appropriate handoff; that is
a separate unproved architecture.

For a finite clock of M sites per rail, the device uses `2M+6` qubits: two
rails, two emitters, two old qubits and two source qubits. Its one-head
Hilbert dimension is `16(2M+2)`; the unrestricted qubit space has dimension
`2^(2M+6)`. Sector decomposition reuses both original 24-dimensional matching
blocks per parity; no new 48-dimensional numerical inverse is inferred from
the small corroboration below. Its positive-block incident norm sums are

| Site | Incident norm sum |
|---|---:|
| old1, added | 1.993757127633340 |
| old2, added | 1.198638631120596 |
| old edge, separate | 3 |
| A | 27.936224853155858 |
| B | 22.228906875353305 |
| either c0 | 8.015120691541701 |
| either c1 | 6.730044773026091 |
| ordinary clock | 4J=0.120084428428128 |
| either c12 | 4J+3kappa |
| either c14 | 4J+3kappa(c+s) |
| either emitter | E0+kappa d |
| finite far end | 3J |

In particular duplicating the source contacts increases A's load by
`2lambdaA=7.603562763162404` and B's by `2lambdaB=5.150067531576994`.
There is no all-site cap two. The full seed moment identities are

    ER* HRphysical ER=K+(E0+cR)I,
    ER* HRphysical^2 ER=[K+(E0+cR)I]^2+2kappa^2 I.        (12)

Indeed the three outgoing hoppings from e0 have squared sum
`kappa^2[1+c^2+s^2]=2kappa^2`, and `B iota=iota K`. Thus the modeled seed
variance is `Var(K)+2kappa^2`. These are not preparation, cooling or total
fabrication costs. Real coefficients, exact ladder values, clean blank
qubits and the excited product seed all remain supplied physical resources.
The fixed rational q0 gives exact rational c and s. No finite coefficient
precision or additional realifier calibration box is certified; the only
parameter interval here is the inherited kappa interval with the displayed
exact relations between its six hoppings.

## 5. The conjugate branch emits an identity output

Use a real Bell basis for the old input, so Db and the vacuum channel vectors
u_j are real. Because E and Db are real, conjugating the backwards version
of (3) gives, for every t,

    ||exp(-itHminus)E - conjugate(Gamma_-t) exp(-itDb)||
       = ||E-Gamma_0|| <0.003.                          (13)

This is an operator identity/bound, not an anti-linear operation performed
on an input. Entrywise conjugating the intertwining matrix produces a
complex-linear matrix from arbitrary old coefficients to the output. Passive
references remain arbitrary.

The open part of `conjugate(Gamma_-t)` in column j is

    (1/sqrt(2pi)) integral_I
      [conjugate(f)e^(ikn)
        +conjugate(f) conjugate(R_j)e^(-ikn)] e^(-itE) dk.
                                                               (14)

The first term is the same outgoing identity wave for every old column.
The second is an unwanted incoming wave. Unlike the forward output, no W
is present in the leading term. Define

    b_minus(t,n)=(1/sqrt(2pi)) integral_I conjugate(f)
                                   e^(ikn-itE) dk,
    beta_minus(t)=b_minus(t)/||b_minus(t)|| on n>=0.      (15)

Since `|R_j|=1`, the product weak derivative obeys

    ||(conjugate(f)conjugate(R_j))'||2
       <=||f'||2+sup|R_j'| <1001/kappa^2.               (16)

The incoming old-vacuum columns are orthogonal, so (4) and (16) use their
maximum, not an unjustified square sum reduction. For the complete localized
columns the within-parity square sum in (3) is retained. It applies equally
to the integrand `conjugate(f C_j)` at positive t. Finally the negative tail
of (15) is bounded with `||f'||2`; normalizing its retained half-line part
costs at most that tail bound. The zero endpoint trace is preserved under
conjugation and multiplication by R_j.

At `t>=T=10^6/kappa^2`, these four complete errors are bounded by

    seed:             0.003,
    incoming:         1001/(kappa^2 v t)+(5/2)sigma,
    normalization:    (1/100)/(kappa^2 v t)+(5/2)sigma,
    localized:        (3/2)/(kappa^2 v t),               (17)

where `sqrt(2pi)>2` and `2J/v<5/2` were used only for upward rounding.
The normalization tail is below one half, so beta_minus is defined. The
sum at T is exactly `215527/5000000=0.0431054<0.044`; time-dependent terms
decrease later. We have proved the new reverse-branch consequence

    ||exp(-itHminus)E
          -beta_minus(t) tensor iota exp(-itK)||<0.044.  (18)

This bound includes all complementary emitter/source coordinates, closed tails,
and seed point-spectrum error. It assumes neither decay law nor absence of
out-of-band point spectrum. It does not introduce a separate old-dependent
spectral fit. The physical scalar in the combined device will be (9).

## 6. A complete-output lower bound

Define normalized ancillary states, including source vacuum and empty emitters,

    a_t = zeta xi_plus beta_plus(t) tensor Omega,
    b_t = xi_minus beta_minus(t) tensor Omega.

They are orthogonal because their rail sectors are orthogonal, even though
their actual clock profiles need not agree. After taking out the common
physical scalar `exp(-it cR)` and literal old evolution `exp(-itK)`, the
device's output is within

    epsilon_R=sqrt[(0.004^2+0.044^2)/2]=sqrt(61)/250<0.032

of the isometry

    Vout x=(a_t tensor W x+b_t tensor x)/sqrt(2).         (19)

Orthogonality of the flag sectors justifies the squared combination of the
two branch errors; it does not discard either branch. For any proposed
common normalized ancillary vector eta_t, apply W* on the old output and
test the two real old vectors in (1). Their actual ancillary vectors in
(19) become

    eta_minus=(a_t+b_t)/sqrt(2),
    eta_plus=(a_t+conjugate(omega_plus)b_t)/sqrt(2).

Their separation is

    ||eta_plus-eta_minus||=|omega_plus-1|/sqrt(2)
                         =8/(5sqrt(2)).                (20)

The triangle inequality forces at least one of the two distances to eta_t
to be at least half of (20). It even holds for an unnormalized eta_t or an
eta_t outside the span of a_t,b_t. Consequently

    inf_(||eta||=1) ||exp(-itHRphysical) ER
      -exp(-it cR) eta tensor exp(-itK)W||
       >=4/(5sqrt(2))-epsilon_R >0.53,  t>=T.           (21)

For a rational check, `4/(5sqrt(2))>9/16` and `epsilon_R<8/250`, whose
difference is `1061/2000=0.5305`. The comparator in (21) allows **any**
common ancillary waveform, including emitter/source support; it is broader
than the requested empty-emitter, vacuum-source outgoing clock comparator.
A phase common to the old inputs is absorbed in eta. Separate per-old-input
phases are not permitted. No output is traced out, projected, measured,
postselected or stopped externally. Tensoring a passive reference does not
alter the operator bound. This is an isometry obstruction; it is not a claim
that every individual input has a large reduced-old-state error.

## 7. Finite clock, actual distance and horizon

The one-head spectrum of HRtilde is the union of those of Hplus and its
conjugate. Hence the inherited radius 19 about `2J+10.5` applies unchanged;
cR shifts only its center. Keep sites 0,...,M-1 on both rails and add
`J n_(M-1,q)` at each far end. This is the exact compression, not an absorber.
From e0, the first omitted sites c_(M,q) are both at head-graph distance

    dM=M-13.                                            (22)

Each rail has a direct e0--c14,q edge, and no edge reaches a larger clock
index. The two rails and onsite internal mixing cannot shorten (22).
Polynomials of degree below dM agree on the whole seed subspace. The known
Chebyshev coefficient estimate therefore gives

    ||embedded finite evolution-infinite evolution||
       <=4 exp[-dM+19t sinh(1)]/[1-exp(-1)].             (23)

At `M=ceil(50T)`, `Tobs=2T`, the buffer beyond exponent -9 is at least
`(22/5)T-22>0`; `sinh(1)<6/5` was retained. The remaining bound is

    (32/5)(3/8)^9=19683/20971520<0.001.                 (24)

Thus the embedded finite complete output remains at distance greater than
`0.5305-0.001=0.5295>0.52` from every common ancillary waveform times W
on `[T,2T]`. The same full scalar and old aging appear. At kappa=10^-8,
T=10^22 and M=5*10^23 per rail; at kappa=10^-12, T=10^30. These enormous
costs are a horizon for this worked failure, not a successful gate resource
estimate or an optimal time. No fixed finite device is analyzed for all
future times, and no resonance-scale improvement is assumed.

## 8. Other real routes and the exact remaining obligation

An initial real-contact shortcut explains why simply deleting the local loop
phase is not justified. For any finite set of real scalar contact weights v_n,
the two free-lead form factors are conjugates,

    g_+(k)=sum_n v_n exp(-ikn),
    g_-(k)=conjugate(g_+(k)),  |g_+|=|g_-|.             (25)

This loses the installed emitter's directional interference zero and does not
inherit its small-bypass proof. Equation (25) is not a proof that a redesigned
real emitter with gate feedback cannot work; it is the precise failure of that
particular free-lead substitution.

A second restricted compiler idea also has an exact boundary. If a finite
real symmetric Hamiltonian is split into P/Q coordinates and real energy E
is outside the eliminated Q spectrum, its Schur Hamiltonian is

    H_eff(E)=H_PP+H_PQ(E-H_QQ)^(-1)H_QP,                 (26)

which is real symmetric. Such a closed ancillary elimination cannot produce
a nonreal scalar loop hopping in the same physical basis. For an open
ancillary channel the retarded self-energy can be complex, but every new
output and its feedback must then be accounted for. Equation (26) does not
rule out encodings or real multiport gate architectures.

For a possible redesigned one-open-channel real emitter there is a useful
production-phase condition. If its real-energy matching problem is unique,
its unit-incoming column has `Phi=R conjugate(Phi)` by time reversal and
`|R|=1`. A real local seed therefore has overlap `y=R conjugate(y)`. The
outgoing spectral coefficient of that seed is proportional to y. If two old
columns have a common nonzero outgoing profile times omega_j, their reflection
ratio must satisfy

    R_j/R_l=(omega_j/omega_l)^2                         (27)

on that common profile's support, as well as common magnitudes and controlled
localized components. This elementary conditional identity is derived here;
no uniqueness or common-profile claim for a new apparatus is supplied. It
suggests a different target for a real reflection design instead of assuming
that the old W scattering certificate is sufficient for emission.

The following remain genuinely different live routes, not failed searches:

| Route | Required new result; present status |
|---|---|
| Real multiport transmission gate with a local product source | Realize the literal old two-qubit operation, retain reflected/rejected ports and all delay errors, and prove one common complete output. Not attempted here. |
| Real one-port emitter designed using (27) | Certify the required squared reflection ratio and common seed spectral magnitude with all closed coordinates. Not constructed here. |
| An autonomous real preparer feeding a single useful chiral sector | Break the conserved-Jf restriction during preparation and prove the full product-seed handoff, with local positive costs and no clock-age reset. Active preparation work is separate and was not inspected or appropriated. |
| An encoded real history/quantum-walk computer | Known real universal architectures exist, but an encoding, decoder, old-aging identity and unpostselected full halt bound for these literal qubits are missing. No impossibility asserted. |
| A different multi-excitation or conditional latch | Avoid this one-head conserved-sector decomposition and prove full seed and output control with two-body NN terms. Not attempted. |
| The existing real boundary-reflection apparatus | It already performs W with a supplied incoming packet and positive three-body boundary. Replacing both those permissions with the requested product-seed/two-body supply is the live bridge; it is not supplied by this failure result. |

The useful next discriminating question is whether a concrete real multiport
or real squared-reflection emitter can meet the complete common-profile
condition without the second branch in (19). It is not whether a real
Hamiltonian can ever generate a complex unitary: even elementary real
Hamiltonians can do that under time evolution.

## 9. Prior work and narrow negative-claim discipline

Primary-literature search and exact read scope are in
`literature/SEARCH_NOTES.md`. Cubitt, Montanaro and Piddock,
[Universal Quantum Hamiltonians, v4, sections 7.1-7.2](https://arxiv.org/pdf/1701.05182v4),
already give the complex/conjugate direct-sum realification and explain the
state-encoding issue for dynamics. Its general ancillary-flag representation
does not automatically preserve geometric locality. This packet gives the
explicit two-rail embedding for the present sparse imaginary edge and derives
its particular literal-old output failure. No general realification novelty
is claimed.

Childs, [Universal computation by quantum walk, v1](https://arxiv.org/pdf/0806.1972v1),
uses real adjacency and permits a single-vertex initial state, with filtering
and encoded wires. Its construction is an important counterweight to a broad
real-coupling impossibility claim. The inspected success/output protocol does
not by itself provide this literal-old, complete unpostselected comparator.
The existing reflection note is likewise a real target-gate mechanism, with
different explicit input and locality permissions. No theorem from either
source is silently imported as the requested two-body product-seed closure.

The no-go discipline was read and applied to this **scoped worked failure**:

1. **N1 alternatives:** the three actual analytical tests are (6)-(24),
   the real-contact substitution (25), and closed elimination (26). Six live
   families are listed above. They are not mislabeled as five completed
   failed attempts. The broad packet-PASS threshold of five ruled-out routes
   is not met, and no such PASS or general no-go is requested.
2. **N2 wall independence:** equal conjugate weights, the bypass branch and
   the common-output separation are one dependent mechanism, not three
   independent physical walls. The closed-elimination statement is narrower
   and is not counted as a prohibition on all real hardware.
3. **N3 hidden walls:** supplied exact coefficients, selected NN edges,
   positive blocks, high source loads, blank vacuum and infinite tails are
   explicit. The alleged cure by a chiral seed is identified as a changed
   resource. No primitive or axiom is used to supply it.
4. **N4 residual matching:** the bound is an operator-isometry error to the
   exact W, allowing arbitrary common full ancillary states, actual cR and
   full old age. It is not a zero-flux, reduced-state or one-column proxy.
5. **N5 accounting:** per_element: positive cells (7)-(8); per_site: the
   full load table; per_mode: both flags, both old energies, every complementary
   source/emitter coordinate; per_block: full-qubit positivity and invariant
   one-head equality distinguished; lattice_wide: two infinite rails or the
   declared `2M+6` finite horizon. These are written research accounting,
   not a claimed canonical no-go-runner or PR-conformance certificate.
6. **N6 partial closure:** ordinary NN realification is achieved. Product-seed
   gate closure fails for this apparatus. The omitted permission is not
   promoted to a new physical axiom or a demonstrated universal necessity.
7. **N7 steelman:** real transmission and real squared-reflection architectures
   could make all emitted branches carry the same W; a real preparer could
   also break the current conserved-sector structure. This proof does not
   exclude them. Known real quantum-walk computation prevents a blanket
   inference from time reversal to computational impossibility.
8. **N8 cross-cycle echo:** the pre-existing free-lead bypass warning is credited
   in (25); the new work is the installed full-output reverse-branch bound,
   physical realification resource accounting, and explicit finite horizon.
   The reflection/emitter scattering strategy itself is prior work.

## 10. Actual computation and remaining verification limits

`PLAN.md` preceded scientific work. The saved `RESOURCE_PLAN.json` added the
bounded exact corroboration before it ran: CPU soft/hard 20 seconds, external
wall 30 seconds, at most two attempts, matrix dimension at most six, graph
at most 64 vertices. One attempt ran. It exited zero in 0.083587125 seconds
of launcher wall time, with 0.033349 user and 0.011494 system CPU seconds;
macOS child peak RSS was 22,921,216 bytes. No OS memory cap is claimed.

`run01/PRELAUNCH.json` was serialized, flushed, fsynced, closed and its directory
fsynced before subprocess creation. It binds the executed copy, checker,
launcher, plans, exact scalar inputs, all sixteen source snapshots and seven
selected runtime files. All 31 byte/generation bindings and sixteen original
source/snapshot pairs matched afterward. This is a real prelaunch record,
not a post-run reconstruction. Runtime bindings are selected files, not an
assertion of a complete transitive binary dependency inventory.

The new exact-Fraction checker imports no inherited scientific implementation.
Its largest matrix is six by six and its finite geometry prefix has 46
vertices. It checks contact signs and flag intertwining, the literal target,
positive-cell identities and full number/scalar coefficients, NN supports,
seed moments, source loads, the reverse budget and error separation. Its
wrong-sign countercase is retained as a nonzero exact defect. Complete stdout,
empty stderr, executed source and receipt are preserved. No optimizer, grid,
quadrature or time evolution ran, and no scientific execution failed.

The small core matrices are evaluated exactly at kappa=10^-8. Extension of
their identities to every declared kappa is analytical linear homogeneity;
onsite positivity and resource ceilings use the displayed monotone inequalities.
The output field `scientific_parameter_samples: 0` means no parameter-sampling
study was run; it must not be read as symbolic-kappa execution. The geometry's
infinite extension and its general distance are proved in (10),(22), not by
checking one prefix alone. The program does not independently prove the
operator-domain, packet or inherited certificate arguments. This packet is
source-exposed author verification, not independent review.

A read-only lookup initially used a nonexistent `.claude/skills/.../DISCOVERY.md`
path; the correct `docs/ai_methodology/skills/...` span was then read. Large
aggregated reads and the broad repository search were sometimes truncated;
needed mathematical spans were recovered separately. The full search text is
saved, and no exhaustive result or complete reading of every lexical hit is
claimed. There are no hidden failed scientific streams or overwritten attempts.

The remaining decisive review is the new reverse-time packet implication,
its full operator constants, physical scalar/embedding and the common-output
lower bound. No current task claims to have independently checked itself or
to have closed native real phase permission. All writes are confined to this
packet directory. No source, worktree, Git, checkpoint, prompt, physical axiom,
audit record or other chat was changed; no subagent or model override was used.

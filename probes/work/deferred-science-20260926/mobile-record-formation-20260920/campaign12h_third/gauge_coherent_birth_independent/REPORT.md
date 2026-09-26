# Independent partial-hop completion and coherent-birth reconstruction

The sufficient completion criterion holds when its components are defined
using the specified **off-occupation-pattern** unitary block maps. It does
not require dephasing of individual field configurations. Both requested
open boxes satisfy this criterion by exhaustive integer enumeration. The
local birth loss leaves one coherence parameter undetermined; on the
specified four-cycle it changes terminal coherence but not the occupation
clock. A fresh neutral probe realizes the coherent instrument, with a real
resource and boundary-time distinction from a reused coherent probe.

These conclusions were reconstructed before accessing new author sources.
The calculations below are conditional finite-model results, not an audit
or native microscopic/energetic derivation.

## A. The block criterion and what its graph must mean

Let the finite-dimensional Hilbert space be the stated direct sum K_c.
Write s(c) for its occupation pattern, Q(c) for its number of holes, and
rho_cd for a density block. All generators are fixed, time-independent
finite matrices. The even-Q
sector is invariant because H and occupation monitoring preserve Q and
every birth jump satisfies [Q,J_mu]=-2J_mu. Full occupation is absorbing.

For any density,

    d Tr(Q rho)/dt = -2 Tr(Gamma rho),
    Gamma = direct_sum_c gamma_c I_(K_c).

If rho is stationary, positivity gives Gamma rho=rho Gamma=0. Equivalently,
every J_mu annihilates the support of rho, so the whole birth dissipator
vanishes. Pairing the remaining stationary equation with rho gives

    0 = -(1/2) sum_x d_x ||[n_x,rho]||_HS^2.

Consequently rho is block diagonal in the occupation patterns. Coherences
between different c blocks with the same pattern are still allowed.

Take one controlled off-pattern hop H_dc=tU from c to d. The (d,c) block
of [H,rho]=0 is exactly

    t U rho_cc - rho_dd t U = 0.

There are no other terms in this particular block: within this pair of
occupation patterns, partial bijectivity gives both the unique source of
d and the unique target of c. H0 contributes no off-pattern matrix element.
Therefore rho_dd=U rho_cc U^dagger and their traces agree, despite the
unmeasured same-pattern field coherences. If gamma_c>0 then rho_cc=0.
Propagating traces along a component containing such a c kills every
diagonal block in that component. Positivity kills the remaining associated
coherences. By the proposed hypothesis every even-Q sector with Q>=2 is
therefore absent from every stationary density.

This is a sufficient condition, not a necessary one. Additional H0 mixing
could help a model whose controlled hop graph fails the criterion. Crucially,
the graph used in the hypothesis must consist of the controlled off-pattern
maps, not arbitrary matrix elements of H0. Occupation dephasing need not
resolve the latter. Likewise, the hypothesis applies to the total
off-pattern Hamiltonian block after summing channels, not to separate
channel drawings that might interfere or violate partial bijectivity.

The independent four-state countercontrol shows the issue directly. Let
c1,c2 have the same two-hole occupation pattern, let d have another such
pattern, and let f be full. Set

    H = |d>(<c1|+<c2|) + adjoint,    J=|f><d|.

The configuration graph is connected and contains positive birth loss, but
(|c1>-|c2>)/sqrt(2) is stationary even with positive occupation monitoring
at every vertex. Its off-pattern map is not a partial bijection. If all
three nonfull states instead share one pattern and these couplings are
called H0, the same example shows why H0 edges cannot substitute for the
specified graph. Similarly a rank-deficient birth loss on an internal
block would not support the block-scalar positive-loss step of the proof.

### Time statement

Full-state probability is monotone. Finite-dimensional Cesaro limit points
are stationary, so the preceding result forces full-state probability to
one from every initial density in the even-Q sector. This statement includes
arbitrary field coherences and arbitrary permitted H0.

More quantitatively, the nonfull corner defines a completely positive,
trace-decreasing semigroup T_t. Its survival effect tends to zero in operator
norm. Choose t0>0 and a<1 with ||T_t0^*(I)||<=a. Then

    Pr(Q_t>0) <= a^floor(t/t0) Pr(Q_0>0),
    E[tau] <= t0 Pr(Q_0>0)/(1-a).

This is a finite-model exponential tail and finite mean. No uniform
constant in size or vanishing rates follows. The count statistics also
have a number-respecting quantum-jump interpretation: discarding an initial
Q measurement does not change them, by number-phase covariance. No classical
trajectory of unmeasured field configurations is assumed. The full density
itself need not converge, since H0 may keep acting within full occupation.

Finite dimension, the even-hole restriction, occupation-resolving dephasing,
the stated block-map property, block-scalar loss and the active-component
condition are sufficient hypotheses used by this proof. They are not a
classification of the weakest conditions for completion. Odd-hole sectors
cannot become full through pair births alone.

### Independent open-box control

For each internal positive-axis link let b_e=1 mean E_e=+1/2. Freeze all
exterior reference links at +1/2. Relative to the all-positive field,

    Q_x = sum_(outgoing e at x) (b_e-1)
          - sum_(incoming e at x) (b_e-1).

Each internal bit string with |Q_x|<=1 fixes a physical matter basis state.
Zero charge is vacancy. The internal divergence sums to zero, hence the
even-volume boxes have even hole count. A vacancy hop flips its link bit
and swaps the neighboring charges (one zero, one nonzero). A vacant edge
has exactly one allowed birth branch and positive loss beta_e, not 2 beta_e.

The independent code enumerates every bit string in Gray order, updating
integer divergences exactly, and constructs the complete legal hop graph
on all physical strings. The Gray-code toggle identity is asserted; direct
charge summation crosschecks every accepted cube state and 259 selected
larger-box states. Union-find only joins explicitly reconstructed legal
hops. All birth arcs are independently checked to reduce hole count by two.

| Box | Internal edges | Bit strings | Physical states | Nonfull hop components | Components without birth loss |
|---|---:|---:|---:|---:|---:|
| 2x2x2 | 12 | 4096 | 375 | 10 | 0 |
| 2x2x3 | 20 | 1048576 | 25386 | 34 | 0 |

There are respectively 516 and 67204 undirected hop edges, and 696 and
70824 directed birth arcs. The full-state counts are 18 and 200. The complete
component-size/hazard histograms are in `OPEN_BOX_RESULTS.json`, including
isolated nonfull configurations that already have a birth edge.

Here K_c is one-dimensional, but a general density on the physical space
can contain coherences between any field strings. For each two distinct
occupation patterns the differing sites fix a unique internal edge, whose
bit flip is a partial bijection. Nonzero hopping coefficients on every
internal edge and positive births on every internal edge therefore meet
the criterion. Optional physical elementary field loops, occupied-record
cycles and other H0 commuting with every n_x do not invalidate it. The
coherent birth families below also have the same scalar loss and qualify.
This proves completion for these two finite boxes through the reconstructed
criterion; it does not extrapolate to all boxes or periodic geometry.

## B. Local instrument and the complete four-cycle evolution

The two operators have orthogonal initial subspaces and orthogonal ranges:

    V_+^dagger V_+ = P_vac P_(E=-1/2),
    V_-^dagger V_- = P_vac P_(E=+1/2),
    V_+^dagger V_- = 0.

Thus for J_mu=a_mu V_+ + b_mu V_- the loss is beta P_vac exactly when

    sum_mu |a_mu|^2 = sum_mu |b_mu|^2 = beta.

For beta>0 define chi=beta^-1 sum_mu a_mu conjugate(b_mu). Cauchy-Schwarz
gives |chi|<=1. The recycling map is

    beta [ V_+ rho V_+^dagger + V_- rho V_-^dagger
          + chi V_+ rho V_-^dagger + conjugate(chi) V_- rho V_+^dagger ].

This 2x2 positive Gram matrix completely specifies the unmarked birth map.
Unitary/isometric changes of Kraus representation do not change it.
If the individual mu outcomes are resolved and retained, their refinement
can contain more information; it is not classified just by chi.

Edge reversal swaps V_+ and V_-. Covariance of the unmarked instrument,
with the stipulated fixed phase conventions, therefore requires chi real.
Conversely every chi in [-1,1] has the covariant representation

    J_s = sqrt(beta(1+chi)/2) (V_+ + V_-),
    J_a = sqrt(beta(1-chi)/2) (V_+ - V_-).

Reversal fixes J_s and negates J_a, which leaves both completely positive
outcome maps unchanged. The endpoints have one independent birth Kraus
operator; the interior has two. For beta=0 all coefficients vanish and chi
has no operational content. For beta>0 equal loss and event rates do not
fix the post-birth coherence. Phase conventions must be held fixed when
comparing chi; a genuine coherence measurement is needed to distinguish
the instruments. The cycle example supplies a gauge-invariant one.

### Exact C4 solution

Use four cyclically oriented reference links, so Q_i=b_i-b_(i-1). Every
one of the 16 link strings is physical. Let |v0>,|v1> be the all-zero and
all-one strings and let |cat>=(|v0>+|v1>)/sqrt(2). Let |i> be the string
with only bit i equal to one and |bar i> its complement. Let |A>,|B> be
the two alternating full strings (integer masks 5 and 10), and define
Xi=|A><B|+|B><A|. Local edge channels are separate Lindblad channels;
coherently summing different edges into one jump would be a different model.

For no ordinary hopping, common beta>0 and common real chi, set

    z = exp(-beta t),
    a(t) = (z-z^4)/3,
    F(t) = 1 - 4z/3 + z^4/3.

The complete density is

    rho(t) = z^4 |cat><cat|
      + (a(t)/2) sum_(i=0)^3 [ |i><i| + |bar i><bar i|
                            + chi(|i><bar i|+|bar i><i|) ]
      + (F(t)/2) [ |A><A| + |B><B| + chi^2 Xi ].

All coefficients are nonnegative on 0<=z<=1, and the component matrices
are positive for |chi|<=1. This formula solves the full 16-state density
equation, including off-diagonal elements, not a population truncation.
The independent exact script verifies L rho=-beta z partial_z rho,
unit trace and the initial/terminal conditions symbolically.

The total birth rate is 4 beta before the first birth, beta between the
first and second births, and zero afterward. Consequently

    Pr(tau>t) = (4 exp(-beta t)-exp(-4 beta t))/3,
    tau has the law Exp(4 beta)+Exp(beta) with independent summands,
    E[tau] = 5/(4 beta),
    E[N_record(t)] = 4 - (8/3) exp(-beta t) - (4/3) exp(-4 beta t).

The terminal density has off-diagonal entry chi^2/2 and
Tr(Xi rho_infinity)=chi^2. Thus occupation completion does not determine
the final gauge-invariant coherence. This particular terminal observable
does not distinguish chi from -chi; intermediate density coherences do.

Every summand has a fixed occupation pattern shared by its two coherent
branches. Hence occupation dephasing sqrt(d_x)n_x annihilates this complete
density for any nonnegative d_x. A real pure-field loop Hamiltonian is a
multiple of |v1><v0|+adjoint and commutes with the vacuum-cat block. The
occupied-record cycle on this cyclic-reference ring restricts to Xi; its
K+K^dagger convention is 2 Xi. A real multiple also commutes with the
terminal block. Adding these Hamiltonians and occupation monitoring therefore
leaves the displayed evolution unchanged.

This is a property of the specified initial cat and these real couplings,
not all interactions. Charge monitoring Q_0, for example, changes the
terminal Xi expectation at rate -2 d chi^2. A field-loop phase or an energy
splitting between coherent branches need not commute with the density.
Neither equal local loss nor this clock calculation makes different chi
instruments equivalent in general interacting histories.

## C. Fresh-probe unitary, channel, size and resource boundary

Write V=V_++V_-, P=V^dagger V=P_vac and R=VV^dagger. Here V^2=0,
P and R are orthogonal projections, and V is an isometry from P onto R.
Let |f>,|s> denote the pure neutral fuel/spent probe states, with

    C = V tensor |s><f| + V^dagger tensor |f><s|,
    M = P tensor |f><f| + R tensor |s><s|.

Then C^2=M and C^3=C, giving the exact unitary

    exp(-i theta C) = I + (cos(theta)-1) M - i sin(theta) C.

With a fresh |f> input its two Kraus operators are

    K_f = I-P + cos(theta) P,    K_s = -i sin(theta) V.

For 0<=theta<=pi/2 this is the finite-step chi=1 birth instrument with
formation probability alpha=sin^2(theta) on a vacant edge. It acts as
identity on already occupied local states. The independent full local
18-state construction checks the partial-isometry identities, Gauss and
number commutators, edge reversal, and the 36-state unitary/reduced Kraus
operators exactly.

If E_c denotes this channel with c=cos(theta), fresh-probe composition obeys
E_c2 E_c1=E_(c1 c2). The same composition law holds for a fixed real chi
in the generalized channel below. Thus with c=exp(-beta Delta t/2),

    E_c,chi = exp(Delta t L_beta,chi)

for the isolated local birth Lindbladian. Finite positive times have c>0;
c=0 is its infinite-time limit. Negative cosines introduce an additional
relative phase and are not this positive-time semigroup parametrization.
With other noncommuting local generators, finite ordered collision products
are not automatically their exact combined semigroup; a finite-system
Trotter limit supplies the usual summed generator.

The weak-collision scaling is theta^2~beta Delta t. Keeping a bounded
interaction strength while simply shortening its duration would instead
give theta=O(Delta t), and a vanishing formation rate in that limit. Fresh
fuel delivery, the interaction timing/scaling and discarding or resetting
the outgoing probe are supplied resources, not consequences of the matrix
identity.

### General real chi and minimal pure-probe dimension

For the full local input space, the finite-step instrument has no-birth
K_0=I-P+sqrt(1-alpha)P and birth Kraus operators

    K_s = sqrt(alpha(1+chi)/2) (V_++V_-),
    K_a = sqrt(alpha(1-chi)/2) (V_+-V_-).

Their vectorized supports show that K_0 is independent of both birth
operators. For 0<alpha<=1 the Choi rank, and hence the minimal pure-probe
dimension, is 2 for |chi|=1 and 3 for |chi|<1. For alpha=0 it is 1. These
statements include blocked input states; restricting the input to vacancy
and postselecting certain outcomes can lower a different problem's rank.
Preserving an arbitrarily specified finer classical mu record can require
more memory than this minimal coarse instrument.

A constructive three-state probe uses a fuel state and two orthogonal
spent states |s>,|a>. Put

    |e_+> = sqrt((1+chi)/2)|s> + sqrt((1-chi)/2)|a>,
    |e_-> = sqrt((1+chi)/2)|s> - sqrt((1-chi)/2)|a>.

Replacing V tensor |s><f| by
W=V_+ tensor |e_+><f|+V_- tensor |e_-><f| gives W^dagger W=P tensor P_f.
The same partial-isometry rotation then realizes the displayed Kraus
operators. The spent-state overlap is chi. Reversal may act with signs
+1 and -1 on the two spent states, making the construction covariant.
The rank lower bound was also checked exactly at chi=-1,0,1/3,1. Fresh
composition was checked on every matrix unit of a separate five-state
representation containing both birth branches and a blocked state.

### Conservation is not irreversible microscopic creation

Since [N_record,V]=2V,

    [N_record+2 P_fuel, C] = 0.

The generalized three-state probe has the same identity. With a supplied
rest energy omega per record and a fuel gap 2 omega, this conserves that
rest-energy operator. It says nothing by itself about gauge-field energies,
record interactions, switching work, an autonomous clock or a complete
interacting energy budget. Such terms require their own commutator and
resource analysis. Probe neutrality is consistent with Gauss because the
record pair plus link operator already preserves Gauss.

At boundaries between fresh collisions the reduced channel has no
record-removal transition, and a formed pair is unchanged by later fresh
fuel on this edge. During one coherent pulse, however, C also contains the
inverse conversion. An intermediate occupation measurement followed by
continued interaction does not turn that inverse into a permanent record.
For example, with theta=pi/2 a vacant edge plus fuel becomes an occupied
pair plus spent probe. Reusing the same probe for a second identical pulse
returns exactly to the original vacancy state up to phase. A second fresh
fuel instead leaves the pair present. The exact control verifies both.
More generally a reused probe gives sin^2(m theta), whereas m fresh probes
give 1-cos^(2m)(theta) for an initially vacant edge. Thus unconditional
intermediate-time permanence or an inexhaustible autonomous fuel supply
does not follow from this collision realization.

## Evidence and limitations

`open_box_check.py` and `coherent_instrument_check.py` are independently
assembled controls. The first exhausts the indicated finite configuration
spaces with integer arithmetic. The second uses exact symbolic matrices,
including the complete C4 density equation, local probe algebra, Choi ranks
and the coherence countercontrol to an overbroad graph criterion. Both
passed on their first execution; complete logs, empty stderr and receipts
are retained. There were no failed or discarded numerical attempts. A
harmless report-edit context mismatch is preserved in `EDIT_ATTEMPT.json`;
it changed no source bytes or scientific calculation.

No new author frontier note, script, result, seal or campaign checkpoint
was opened. The allowed prior monitoring/gauge sources were reused at
their previously verified identities, recorded in `READ_BOUNDARY.json`
and the seal. In particular this packet does not inspect the autonomous
scattering work. No outside theorem, large simulation or full open-box
Liouvillian diagonalization is used. The finite graph enumeration verifies
the theorem's sufficient hypothesis; the proof is what handles arbitrary
quantum densities. The conclusions do not imply thermodynamic completion,
unique internal state selection, general equivalence of birth instruments,
native site placement, full interacting energy conservation or formal
retained/audit status. Author-source comparison is a later, separately
authorized step after this pre-comparison seal.

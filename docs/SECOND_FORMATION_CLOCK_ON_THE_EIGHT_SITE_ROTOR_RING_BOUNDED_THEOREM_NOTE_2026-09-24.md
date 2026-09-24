---
claim_id: second_formation_clock_on_the_eight_site_rotor_ring_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical diagnostics alone do not prove the analytic limits or select physical dynamics."
upstream_dependencies:
  - minimal_axioms
  - exact_fast_spectrum_and_formation_outputs_on_rings_bounded_theorem_note_2026-09-24
  - finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/second_formation_clock_on_the_eight_site_rotor_ring_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The source argument below comes from the frozen submission, with the narrow corrections identified in the combined review receipt. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. The Hamiltonians, quantum state spaces, instruments, backgrounds and preparations are supplied model assumptions. Fresh canonical controls are distinguished from archived diagnostics; no numerical scan substitutes for the displayed proofs.

# A second formation clock with retained fast motion

Personally derived conditional result, 2026-09-23. Independent reconstruction
has not yet been requested for this unit. All dynamics here belong to the
supplied unit-rotor model; the simultaneous finite-spin electric-field limit
is a different, unresolved question.

## 1. Model, state and assertion

Use the oriented eight-site alternating ring, hard-core q=0,+1,-1,
Gauss law E_e-E_(e-1)+1_A(e)-q_e=0, and legal hopping amplitude -1.
The checked parent source is
`../../campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md`.
In its P sector, all four A sites are occupied. Its effective target is

    H_eta = eta H2 + delta H4,       eta=delta/epsilon^2,
    H2=-A^dagger A,
    H4=(A^dagger A)^2-Z^dagger Z/2,
    B_(e,sigma)=-P j_(e,sigma) Pi1 T P,                 (1)

where A=Pi1 T P, Z=Pi2 T Pi1 T P. The resolved jumps are sqrt(kappa) B;
the coherent edge jump is sqrt(kappa)(B_(e,+)+B_(e,-)). Fix delta>0,
kappa>0. An initial state has all A plus, B empty, and any normalized
trace-class density in the one independent integer field circulation.

After its first recorded mark there are six records, including one negative
record. Let S_eta(t) be the survival probability for no further formation,
starting from the actual normalized first-mark output. For either stipulated
instrument, every first mark, and every fixed normalizable initial field state,

    S_eta(t) -> S(t)=[exp(-2 kappa t)+exp(-4 kappa t)]/2 (2)

uniformly for t in each compact interval, as eta tends to infinity. In
particular this limiting second waiting time is not a single exponential.
The proof retains the complete H2 motion and H4 in (1). It requires no
prepared lowest band and no uniform angular spectral gap. The limit is not
uniform over eta-dependent field preparations concentrated near exceptional
angles. No convergence of waiting-time moments is inferred from (2).

## 2. Loss operator and the six word sectors

Write Q_adj for the diagonal projection onto adjacent occupied B pairs on
the contracted four-site B ring. Its complement Q_opp selects opposite pairs.
Both descriptions also apply to the two vacant B sites by complementation.

A particular second resolved mark can occur exactly when both B neighbors of
its A endpoint are vacant. The old A record must hop to the neighbor other
than the marked edge. This is a unique path. From a specified final charge
word and this mark one reconstructs its initial word and field shift uniquely;
thus the jump's Gram operator is the indicated configuration projection.
The two charge orientations have orthogonal output ranges, so their cross
Gram operators vanish and coherent and resolved total losses agree.
For each eligible A there are two marked edges and two charge choices.
With two B holes, exactly one A is eligible when the holes are adjacent,
and none is eligible when they are opposite. Consequently

    Gamma = kappa sum B^dagger B = 4 kappa Q_adj.       (3)

The exact reduction in
`../post_birth_ring_spectrum_author/EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS.md`
identifies the P fiber as a two-particle hard-core B ring coupled to a
six-dimensional weighted charge-word shift. Its eigenphases satisfy

    exp(i 6 alpha_s)=exp(i 4 theta),
    alpha_s=(4 theta+2pi s)/6,    s=0,...,5.

In each word sector, H2=-4I-C_alpha. Here C_alpha is the adjacency of
two hard-core particles on four sites, with boundary twist alpha. It only
connects the four adjacent-pair configurations to the two opposite-pair
configurations. In that decomposition write

    C_alpha = [ 0  D_alpha ; D_alpha^dagger  0 ].       (4)

The characteristic polynomial is

    det(xI-C_alpha)=x^2[x^4-8x^2+8-8cos(alpha)].        (5)

For example (5) follows by listing the four possible moves from each opposite
pair and forming the 2-by-2 D_alpha^dagger D_alpha; its trace is 8 and
determinant is 8-8cos(alpha). Thus D_alpha has rank two unless alpha=0
modulo 2pi. For a generic theta the kernel of C_alpha is two-dimensional
and entirely within Q_adj. The only exceptional theta are

    theta=0, pi/2, pi, 3pi/2 modulo 2pi.               (6)

Let P0(theta) project onto the full H2 eigenvalue -4 at a generic theta.
It has dimension twelve. The involution J=Q_adj-Q_opp anticommutes with
C=H2+4I (the sign chosen for C is immaterial here). If P_lambda is a
spectral projection of C at lambda!=0, then
2 lambda P_lambda J P_lambda=0. Therefore

    P_lambda Q_adj P_lambda=P_lambda/2  (lambda!=0),
    P0 Q_adj P0=P0.                                    (7)

This argument also covers degeneracies across word sectors. Pinching (3)
into the H2 eigenspaces consequently gives

    Gamma_bar = 2 kappa I + 2 kappa P0.                 (8)

## 3. Actual formation weights

Every first ring mark puts the two occupied B sites next to one another.
The resolved output has one definite charge word, and the coherent output
has the two stipulated charge orientations in a normalized superposition.
For any charge-word vector at a fixed adjacent B configuration, the P0
weight is one half at every nonexceptional theta.

To verify this, distribute the twist uniformly around the four-site ring by
a diagonal gauge. Translation is then a symmetry of C_alpha and is transitive
on the four adjacent-pair configurations. Its rank-two kernel lies entirely
in their span. Every corresponding diagonal entry of its projector is hence
2/4=1/2. Undoing the diagonal gauge leaves those entries unchanged. The
different word sectors are orthogonal, so the same identity holds for any
superposition of word vectors at that adjacent configuration. In particular,

    <P0(theta)>_actual_first_output=1/2.                (9)

The first mark includes a link-translation phase. It cannot change (9).
Mixed field states follow by linearity. The exceptional set (6) has zero
weight for every trace-class state on ell^2(Z), since its angle probability
measure has an L1 density. Thus (9) is a statement about all specified
normalizable outputs, not a proposed sharp-angle preparation.

At theta=0, for comparison, extra dispersive modes cross -4; the resolved
fiber projection at that energy has weight 13/24, not 1/2. The author
controls preserve this exception and its different fiber survival. It must
not be assigned positive quadrature or physical probability weight by hand.

## 4. Averaging with H4 retained

The no-event propagator at a fixed theta is

    V_eta(t)=exp[-it(eta H2+F)],
    F=delta H4-i Gamma/2.

It is a contraction, because Gamma>=0. Let F_bar=sum P_lambda F P_lambda,
with full H2 spectral projections, and X_eta(t)=exp(i eta H2 t)V_eta(t).
It solves X_eta'=-i F_eta(t) X_eta, where
F_eta(t)=exp(i eta H2 t) F exp(-i eta H2 t). Define

    R_eta(t)=integral_0^t -i[F_eta(s)-F_bar] ds.

For this fixed finite fiber,

 sup_t ||R_eta(t)|| <= (2/eta)
           sum_(lambda!=mu) ||P_lambda F P_mu||/|lambda-mu|.    (10)

Only distinct eigenvalues occur in the denominator. Duhamel followed by
integration by parts, using the contraction propagator for -i F_eta and
the contraction exp(-it F_bar), gives

 sup_(0<=t<=T) ||X_eta(t)-exp(-it F_bar)||
       <= (1+2T ||F||) sup_(0<=s<=T)||R_eta(s)||.        (11)

Indeed the integrated boundary term is R_eta(t)exp(-it F_bar); the two
derivative terms are bounded by ||F_eta|| ||R_eta|| and
||R_eta|| ||F_bar||. Pinching is norm contractive, so ||F_bar||<=||F||.
This supplies the finite-matrix averaging argument directly, without an
assumed Markov reset of fast phases or a uniform gap across theta.

The Hamiltonian part delta H4_bar commutes with P0, since it is block
diagonal in H2. By (8) it also commutes with Gamma_bar. Hence its unitary
factor drops out of the norm, and (9) gives exactly (2) at generic theta.
The norm difference in (11) is always at most two. Dominated convergence
against the initial angle density, including a pure-state decomposition of
any mixed trace-class input, upgrades pointwise fiber convergence to the
uniform compact-time survival statement. Exceptional fibers have measure
zero. No convergence of the full cross-angle density matrix in the original
Schrodinger picture is asserted.

This is standard finite-dimensional secular-averaging machinery. Related
primary context is Burgarth, Facchi, Nakazato, Pascazio and Yuasa,
[Generalized Adiabatic Theorem and Strong-Coupling Limits](https://arxiv.org/abs/1807.02036).
Only its abstract was used for context; (10)-(11) give the needed proof here.

## 5. First and second counts

Before the first event, the all-A-plus/B-vacant sector is one-dimensional
per field angle, H2=-8I, and the effective total loss is 16 kappa I. Every
resolved mark has loss kappa I; every coherent edge mark has loss 2 kappa I.
The first waiting time is therefore Exp(16 kappa), and its mark probabilities
are field independent. On this eight-site ring H4=24I; this scalar is not
needed for the first loss but also leaves the initial field state unchanged
apart from a common phase. Each first mark produces the family covered by
(2). There are at most two formations, since the second fills all eight sites.

Convolving the first-event density with (2) gives the limiting record-number
probabilities at time t, starting from four records:

    P4(t)=exp(-16 kappa t),
    P6(t)=(4/7)exp(-2 kappa t)+(2/3)exp(-4 kappa t)
                                  -(26/21)exp(-16 kappa t),
    P8(t)=1-(4/7)exp(-2 kappa t)-(2/3)exp(-4 kappa t)
                                   +(5/21)exp(-16 kappa t).    (12)

They are nonnegative by the survival-convolution construction and sum to one.
Uniform compact-time convergence follows from (2) and the bounded first
waiting density. In the limiting process the two waiting increments have
the specified exponential and exponential-mixture laws; the second law is
independent of the first time/mark and of the initial normalizable field.
The first-after-mark instantaneous hazard is 4 kappa at every eta, whereas
-S'(0)=3 kappa in (2). Compact-time convergence of continuous survival curves
allows this initial derivative boundary layer; it does not imply derivative
convergence.

The checked bounded-rotor microscopic approximation has trace-density error
O(epsilon) on fixed compact laboratory intervals relative to (1). Number
projections are bounded observables, so its unconditioned record-number
probabilities inherit (12) as epsilon tends to zero. This is a consequence
for fixed-time counts in the rotor microscopic model. It is not a new
uniform theorem for conditioned microscopic event times.

## 6. Scientific boundary and controls

The direct author probe builds all 168 six-record charge configurations,
their 36/96/36 W sectors, the legal-hop matrix and every resolved/coherent
formation map to the 28 fully occupied charge states. It checks Gauss shifts,
the full Gamma identity, the secular projection, actual outputs, H4 and
finite-eta survival. Generic and exceptional angles are both retained.
These numerical controls corroborate the proof; a phase grid cannot prove
the normalizable direct-integral limit by itself.

The normalizable-state numerical controls use uniform and 1+/-cos(theta)
angle densities (a single integer flux and the two adjacent-flux superpositions).
An initial 128-to-256 quadrature comparison failed the declared 1e-8 resolution
criterion at eta=320, t=.7. Its original values and a reproducing failed
assertion/receipt are preserved. Refining that case to 512 and 1024 points
gave maximum difference 2.45e-15 without changing the tolerance or formulas.
Those refined values, rather than the coarse-grid values, are the resolved
numerical corroboration. A separate guessed linear expression for H4 was
also rejected and is recorded; the proof does not use that expression.

This is a concrete repeated-formation result without a lowest-band projection.
It is still an eight-site, supplied quantum model. Taking normalized spins
to unit rotors first removes the generated electric E^2 term; the ring also
has no four-edge magnetic loop. Nothing here proves the simultaneous
epsilon^2 S(S+1)=delta/K field scaling after formation, a volume limit,
locality of a secular generator, native-axiom selection, or a TOE.


## Exact finite-parameter proof contribution

The following mathematical sections were originally authored in the same submission’s second-event reconstruction packet. They are retained here as source proofs, reviewed on their mathematical content. Their original label does not confer independent-review or audit authority. They supply the full block law needed by the tail-moment result.

## 1. Premises and new operator construction

The supplied canonical operators are

    A=Pi_1 T P, M=A^dagger A, Z=Pi_2 T Pi_1 A,
    H2=-M, H4=M^2-Z^dagger Z/2,
    B_(e,c)=-P j_(e,c) Pi_1 T P.

T assigns -1 to each legal vacancy hop, transporting its unchanged charge and
shifting its oriented edge by minus that transported charge. Thus each
effective B path has amplitude +1. A resolved birth creates c at the oriented
tail and -c at the head and shifts the birth edge by +c. A coherent edge
channel is B_(e,+)+B_(e,-), without a 1/sqrt(2) in the unnormalized jump.
Jumps in the generator are sqrt(kappa) times these operators.

`operators.py` independently enumerates matter words at each W level, actual
legal hops, integer link shifts and births. It builds A and Z on complete
sectors. It does not import a previous or author model builder. On the ring,
the independent circulation is E_7 and the Fourier multiplier of a shift of
that coordinate by m is exp(i m theta). On the cube all 12 integer field
shifts are retained, without a flux cutoff or numerical field truncation.

For any edge, j_(e,+)^dagger j_(e,-)=0: the two newborn matter patterns on that
edge are orthogonal. Consequently the total loss

    Gamma=sum_(e,c) B_(e,c)^dagger B_(e,c)

is identical to sum_e (B_(e,+)+B_(e,-))^dagger(B_(e,+)+B_(e,-)). Equality of
these losses does not assert equality of the recycling CP maps or of all
subsequent interacting histories.

## 2. Exact six-coordinate reduction on the eight-site ring

After one birth there are six records, charge four, four occupied A sites,
two occupied B sites and one minus record. The fiber has dimension 36. Reuse
the checked cyclic-word coordinate r=0,...,5 and its cut rotation V_theta.
Its eigenphases are

    alpha_j=(4 theta+2 pi j)/6, j=0,...,5.

The new operators preserve these word sectors. In a sector set z=exp(i alpha)
and order occupied B pairs as 01,02,03,12,13,23. Let P_adj project onto
01,03,12,23; P_opp projects onto 02,13. Direct legal-path enumeration gives

    H2=-4 I-C,       Gamma=4 P_adj,
    H4=12 I+4 C+Q,                                      (R2)

where, in the order (adjacent pairs; opposite pairs),

    C = [ 0  R ],       R = [ 1  z^-1 ],
        [ R* 0 ]           [ 1    1  ]
                           [ 1    1  ]
                           [ z    1  ],

    Q = diag(Q_adj,0),

    Q_adj = [  0   a*  -a*   0  ],   a=z-1,
            [  a    0    0   a* ]
            [ -a    0    0  -a* ]
            [  0    a   -a    0 ].

Here * denotes Hermitian adjoint or complex conjugation as appropriate.
These matrices are obtained by summing the W-paths 0->1->0 for M,
0->1->0->1->0 for M^2, and 0->1->2->1->0 for Z^dagger Z. This supplies a
finite exact check of all folded/normalization terms in the stipulated H4,
rather than guessing a fourth-order hopping coefficient. The full matrix and
the exact Laurent calculations are in `RING_EXACT_RESULTS.json`.

The loss identity has a simple local proof. When the two B vacancies are
adjacent on their four-cycle, the A between them can hop to either vacancy
and form on the other incident edge, with two charge choices per edge. Each
channel has a unique prior destination on the degree-two graph. There are
four contributions, each with Gram one. Opposite B vacancies have no common
A neighbor and cannot form immediately. The complement occupied B pair is
adjacent in precisely the first case. Thus Gamma is the diagonal 4 P_adj;
there is no uncounted interference in this loss.

Direct multiplication verifies

    Q C=C Q=0,   [Q,Gamma]=0,   [H4,H2]=0.               (R3)

The first mark has occupied B pair 03. Its resolved word is r=1 (or r=0 for
the opposite orientation); its normalized coherent word is (|0>+|1>)/sqrt(2).
Both orientations share the same shift of E_7. Hence the weights in word j are

    b_j^res=1/6,
    b_j^coh(theta)=[1+cos(theta-alpha_j)]/6.              (R4)

They sum to one. They refer to the actual mark output, not a prepared single
energy band.

## 3. Exact finite-eta survival, including H4

Set a_eta=eta-4 delta. By (R2),

    H_eta=(-4 eta+12 delta)I-a_eta C+delta Q.

The scalar phase and the unitary generated by delta Q drop out of no-event
norms, because Q commutes with both C and Gamma. H4 has therefore been
retained exactly: it changes the motion coefficient to a_eta and contributes
a commuting flat-subspace unitary. It was not discarded as a small term.

The nonzero singular values of R have squares

    s_+(alpha)^2=4+4 cos(alpha/2),
    s_-(alpha)^2=4-4 cos(alpha/2),                         (R5)

with their order exchanged when alpha is changed by 2 pi. Indeed

    R* R = [ 4          2+2 z^-1 ],
           [ 2+2 z      4        ].

For the initial adjacent coordinate 03, R*|03>=(1,1). An eigenvector of R*R
can be chosen proportional to (exp(-i alpha/2),+/-1). Its overlap squared
with (1,1) is 1+/-cos(alpha/2). Dividing by s_+/-^2 gives initial weight 1/4
in each bright adjacent singular coordinate. The remaining weight 1/2 is in
ker R* and has constant loss four. At a zero singular value the formulas
below extend continuously, rather than dividing by zero. Degenerate positive
singular values are harmless: the summed bright weight is basis independent.

Each bright pair (adjacent coordinate, opposite coordinate) evolves with
no-event matrix

    K_omega = [ -2 kappa   i omega ],
              [  i omega      0    ],
    omega=a_eta s.

Starting in its adjacent coordinate, define f_omega(t)=||exp(tK_omega)(1,0)||^2.
Writing w=sqrt(kappa^2-omega^2), F=sinh(wt)/w, with F=t at w=0, gives

    f_omega(t)=exp(-2 kappa t)
       { |cosh(wt)-kappa F|^2 + omega^2 |F|^2 }.           (R6)

In particular f_0(t)=exp(-4 kappa t). The exact fiber survival for either
specified mark is

    S_eta(theta,t)= (1/2)exp(-4 kappa t)
       +(1/4)sum_j b_j(theta)
          [f_(a_eta s_+(alpha_j))(t)
           +f_(a_eta s_-(alpha_j))(t)].                  (R7)

This identity holds also at exceptional angles, by continuity of the finite
matrix exponential. It retains the full motion, loss and stipulated H4. The
formula was checked against exponentials of complete independently assembled
36-dimensional matrices in 160 cases, including eta=4 delta, ordinary and
exceptional angles. Maximum discrepancy was below 9e-15.

Let g(theta) be the angle density of the pre-mark normalizable circulation
state, normalized with dtheta/(2pi). For a mixed trace-class density, use its
nonnegative summable eigenvector expansion to define this L1 angle density.
The Hamiltonian and loss are decomposable in theta, so the physical survival is

    S_eta(t)=integral g(theta) S_eta(theta,t) dtheta/(2pi). (R8)

No fixed-angle generalized vector is being treated as a normalizable state.
Off-diagonal circulation coherences can affect g and hence the finite-eta
survival. For example, for the normalizable field (|ell=0>+|ell=1>)/sqrt(2),
eta=20, delta=.7, kappa=.9, t=.2, quadrature of the exact formula gives
approximately .5881207087 after a resolved mark and .5855977964 after the
coherent mark. These numerical values corroborate the exact formula and
illustrate that loss equality alone does not equate the finite-time laws.

## 4. Limit, exceptional fibers, count and mean

For fixed omega/|a_eta| nonzero, (R6) converges uniformly in time to
exp(-2 kappa t) as |a_eta| grows. More explicitly, if |omega|>=2 kappa, put
nu=sqrt(omega^2-kappa^2). Then

    f_omega(t)=exp(-2 kappa t)
      [1-(kappa/nu)sin(2nu t)+2(kappa/nu)^2 sin^2(nu t)],

and its difference from exp(-2 kappa t) is at most 3 kappa/|omega|,
uniformly for t>=0. At all omega, both survivals are between zero and one.

The only angles with a zero singular value in some word branch are

    E={0,pi/2,pi,3pi/2} modulo 2pi.

If d(theta,E) is circle distance to this set, the smallest singular value
among all six branches is 2sqrt(2) sin[d(theta,E)/6], at least c d(theta,E)
with c=2sqrt(2)/(3pi). For 0<r<=pi/4 and |a_eta| c r>=2 kappa, (R7) yields
the explicit fixed-input bound

    sup_(t>=0) |S_eta(t)-S_infinity(t)|
      <= (1/2) integral_(d(theta,E)<r) g(theta) dtheta/(2pi)
         +3 kappa/(2 |a_eta| c r).                       (R9)

Absolute continuity of g and then r->0 prove (R1). Taking r proportional to
|a_eta|^-1/2 also proves convergence directly; for bounded g it gives a
sufficient O(|a_eta|^-1/2) bound, without claiming sharpness. Trace-norm
convergent initial density families inherit the same limit by contraction.
No density-independent convergence rate follows for arbitrary L1 g.

The exceptional sharp fibers have a different answer. Exactly one word
branch there has alpha=0 modulo 2pi. It has a dark opposite-coordinate vector,
but the specified mark has zero projection on that vector. Instead its
zero-frequency adjacent component decays at rate 4 kappa. The fiber limit is

    (1/2+b_*/4) exp(-4 kappa t)
      +(1/2-b_*/4) exp(-2 kappa t),                      (R10)

where b_*=1/6 for a resolved mark and b_*=(1+cos theta)/6 for the coherent
mark. At theta=0 the rate-four weight is 13/24 or 7/12, respectively. These
exceptional fibers have zero measure for any fixed normalizable input. The
lowest-band crossing angles theta=pi/4+j pi/2 are a different set; their
positive-frequency degeneracies cause no extra singularity in (R7).

Uniformity over eta-dependent normalizable preparations is false. Choose
g_eta constant on [-eta^-2,eta^-2] and zero elsewhere, with total mass one.
The corresponding square root is a legitimate L2 angle wavefunction. The
small singular frequency tends to zero while all other frequencies diverge,
so its survival tends to (R10) at theta=0, not (R1). Shrinking-packet controls
are preserved. Thus using a single fiber or interchanging arbitrary spectral
preparation and the eta limit is not justified.

After this next birth all eight sites are occupied. In this supplied effective
model T, H2, H4 and births then vanish. Let C_eta(t) be the number of further
births after the specified first mark. It is a zero-or-one process, with

    Pr[C_eta(t)=0]=S_eta(t),
    E N(t)=8-2S_eta(t),
    Var C_eta(t)=S_eta(t)[1-S_eta(t)].

The next-event distribution and all fixed finite lists of count observations
therefore converge to those of the mixture of Exp(4 kappa) and Exp(2 kappa),
with equal mixing weights. This conclusion concerns unmarked counts; it does
not specify the final marked quantum state or the second mark distribution.

For every finite eta, the mark output eventually forms the next pair with
probability one. This follows from (R6) for each bright pair, the decaying
flat adjacent part, and dominated convergence in theta. The mean can be
computed without a tail approximation. For omega!=0 the positive mean-time
matrix solving K_omega* X+X K_omega=-I is

    X = [ 1/(2 kappa)        -i/(2 omega) ],
        [ i/(2 omega)   1/(2 kappa)+kappa/omega^2 ].

Its initial adjacent-coordinate value is 1/(2 kappa). At omega=0 that value
is 1/(4 kappa), because the initially unpopulated opposite coordinate decouples.
For eta!=4 delta, zero frequencies occupy a null angle set, so Tonelli and
(R7) give the exact physical mean

    E T_next = (1/2)/(4 kappa)+(1/2)/(2 kappa)
             =3/(8 kappa).                              (R11)

At eta=4 delta all bright frequencies vanish and S_eta=exp(-4 kappa t).
The mean is then 1/(4 kappa). Complete-matrix Lyapunov controls at generic
angles independently reproduce (R11). This finite mean was proved for the
specified first-mark outputs; an arbitrary opposite-coordinate initial state
has a mean containing kappa/omega^2, so an all-state mean assertion would need
different hypotheses.

Several tempting replacements fail. The exact initial derivative is
S_eta'(0)=-4 kappa, whereas S_infinity'(0)=-3 kappa: differentiating the fast
limit at zero is invalid. Replacing the clock by Exp(4 kappa), or by any
single exponential matching the limiting slope, loses the two components.
Discarding the flat half of the actual formation output or replacing it by a
lowest-band state changes the input. The lack of a uniform nonzero bright
singular value also forbids inferring a field-uniform exponential tail from
finite-fiber diagonalizations.

## 5. Cube: all immediate marked Grams

The oriented edge order is

    01,02,04,13,15,23,26,37,45,46,57,67.

With q0=1_A, A={0,3,5,6}, Gauss gives div E=0 initially. The initial physical
field space is the integer divergence-free-flow Hilbert space (cycle rank
five), with no electric cutoff. Define W_square as the unitary translation by

    z_square=(0,1,-1,0,0,0,1,0,0,-1,0,0),

which is the oriented circulation 0->2->6->4->0. It preserves div E.

For first mark 01 and either resolved charge c, the old plus at A0 can move to
2 or 4. These give orthogonal intermediate matter words, with field shifts
c on 01 and -1 on 02 or 04. The unnormalized first Gram is 2I, so divide
the output by sqrt(2). For the coherent first channel, the four branches from
the two charge orientations are orthogonal in their 0,1 contents. Its first
Gram is 4I, so divide by 2.

Let V_1 denote any of these normalized first-mark isometries. For a second
resolved channel (f,d), the operator on the initial field is

    G_(f,d|1)=V_1^dagger B_(f,d)^dagger B_(f,d) V_1.

Its complete value is the following table, the same for d=+1 and d=-1 and
for each of the three specified first instruments.

| Second edge f | Resolved Gram for each d | Coherent second-edge Gram |
|---|---|---|
| 01,02,04,13,15 | 0 | 0 |
| 23,26,37,45,46,57 | I/2 | I |
| 67 | I+(W_square+W_square^dagger)/2 | 2I+W_square+W_square^dagger |

Summing either instrument gives (C1). For an initial density rho, the
conditional probability of that next mark in an infinitesimal interval dt is
kappa Tr(rho G_(f,d|1))dt+o(dt), at each fixed eta. The total derivative uses
kappa Tr[rho(8I+W_square+W_square^dagger)]. It lies between 6 kappa and
10 kappa. The endpoints are spectral bounds, not attained by a normalizable
eigenstate of the nontrivial bilateral flux translation.

The interference term has an elementary path explanation. If the old 0
record first went to 2, the empty B sites are 4 and 7; A5 and A6 can act next.
If it went to 4, the empty B sites are 2 and 7; A3 and A6 can act next. Each
of the six nonspecial second edges has exactly one of these histories. At
edge 67 there are two: old 0->2 followed by old 6->4, or old 0->4 followed
by old 6->2. The final matter contents agree for fixed newborn orientation.
Their field shifts differ by z_square, giving W_square and its adjoint in
the Gram. All amplitudes have the same positive sign. No two histories on
distinct resolved second marks are combined.

The first orientations remain distinguished by occupied contents at 0 and 1
during all these immediate second-event paths. Thus their cross terms vanish
in these Grams. This explains the equality between a resolved first output,
the resolved charge-erased mixture, and the coherent first superposition for
this particular immediate question. The newborn outcomes of the second
channel are likewise orthogonal in its last edge, giving the coherent-column
sums. Neither observation identifies their output density operators.

`cube_gram.py` enumerates all first and second paths, combines equal final
matter words, and computes every Laurent coefficient as an exact rational.
Every resulting field translation is checked to have zero divergence.
`cube_field_control.py` independently evaluates direct output-wavefunction
norms for physical finite-support initial fields. In particular

    |0>                         gives total rate 8 kappa,
    (|0>+|z_square>)/sqrt(2)      gives total rate 9 kappa,
    (|0>-|z_square>)/sqrt(2)      gives total rate 7 kappa,
    (|0>+i|z_square>)/sqrt(2)     gives total rate 8 kappa.

All marked probabilities in the table are checked as well. The 9 versus 7
controls are normalizable counterexamples to a universal constant cube
second-rate claim. They do not determine its subsequent ordinary-time
survival under eta H2+delta H4. No such cube dynamics was inferred or reviewed.



## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the stated graph, sector, preparation, observation topology and order of limits.
- **N2 — Alternatives:** other laws, preparations, graphs and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not repository axioms.
- **N4 — Dependencies:** companion arguments retain their explicit hypotheses and confer no audit grade.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate proofs; floating computations are not interval enclosures. Archived diagnostic tables remain historical observations.
- **N6 — Resolution:** fixed-time, shrinking-time, fixed-index, growing-index and volume statements must not be interchanged.
- **N7 — Remaining work:** native model selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** this source applies no audit verdict or retained grade.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied quantum model.
- [exact_fast_spectrum_and_formation_outputs_on_rings_bounded_theorem_note_2026-09-24](EXACT_FAST_SPECTRUM_AND_FORMATION_OUTPUTS_ON_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.
- [finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24](FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.

## Source and verification

Source PR #8831, frozen head `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`. Complete original path dispositions and recovery branches are retained in the combined receipt. Review and affected-fix confirmation use the same primary session without subagents; no formal audit is claimed.

```bash
python3 scripts/second_formation_clock_on_the_eight_site_rotor_ring_2026_09_24.py
```

The runner executes selected controls in a fresh temporary directory and includes generated result JSON in its authenticated stdout. Source history and deferred diagnostics remain recoverable from the original branch.

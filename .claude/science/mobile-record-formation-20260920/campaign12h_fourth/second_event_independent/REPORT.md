# Independent second-formation reconstruction

2026-09-23. This packet was derived before access to either new author packet.
It concerns the stipulated **unit-rotor effective generator**. It is not a
finite-spin joint-limit theorem, microscopic stopping-time theorem, publication
review, or formal audit. The preceding complete ring-spectrum reconstruction
and comparison, and the earlier L=3 example, were already known and are
explicit dependencies. No `second_event_author`, `finite_spin_post_birth_author`,
fourth-campaign working derivation, checkpoint, or registry was opened.

For the eight-site ring the next-event survival, for each fixed normalizable
pre-mark circulation density and either specified first instrument, tends to

    S_infinity(t) = [exp(-4 kappa t)+exp(-2 kappa t)]/2.       (R1)

The convergence is uniform in t>=0. It is not uniform over arbitrarily
eta-dependent input states. An exact finite-eta formula below retains H4 and
proves completion with finite mean from these mark outputs. For eta!=4 delta
the mean is exactly 3/(8 kappa); at eta=4 delta it is 1/(4 kappa).

On the cube, conditionally on the specified first mark, the total immediate
next-event Gram is

    8 I + W_square + W_square^dagger,                       (C1)

where W_square shifts flux around 0->2->6->4->0. Multiplication by kappa gives
the rate operator. The complete marked Grams are given below. They agree for
the two resolved first orientations and the normalized coherent first output,
while the coherent second-edge Gram is the sum of its two resolved Grams.
These are immediate operator identities, not an exponential cube waiting law.

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

## 6. Evidence, failures and source boundary

Exact source identities are in `SOURCE_BINDINGS.json`; PRE binds all evidence.
The seven direct dependencies are the third-campaign fast-target note and its
checked report/seal, plus the preceding independent ring report, PRE,
comparison and final seal. Key identities are:

| Dependency | SHA-256 |
|---|---|
| Fast-target note | `002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e` |
| Its independent report | `0a114dadc553ccbb4ef9bf15faf87a70f64a0d5719bf1d1743de86b94a0205b5` |
| Its final seal | `63ddf9823aa23d678e8f61863ddeedf36596918e2cb600f100fa334e6d1432db` |
| Prior ring report | `8bb9e330303d5b66e14c19031716d8fb8e7baa5a49d193759dbabce1f343b7b2` |
| Prior ring PRE | `cffc3495e440045bd73077e8be1a5e231ff39a07e53889a22336c204f60f5c37` |
| Prior ring comparison | `9fc278830ca7473f631139845b76e55c4ed72ab44b8e136759c22a481907a160` |
| Prior ring final seal | `6beaa587833b2d626154ffdd8fd2729ad844f164ee4be6b0c607b3f9b4402851` |

No external theorem import was needed. General statements here follow from
the displayed exact finite-coordinate identities, elementary two-state
evolution and the stated integral bound. Numerical quadratures are finite
controls; they do not prove the continuum of angle or eta limits.

Every scientific run uses the local `run_control.py`, retaining actual
stdout, stderr and a receipt binding the executed source. The exploratory
`ring_probe.py` reports absolute eigenvector amplitudes in its explicitly
qualified amplitude field, not probabilities. Those exploratory amplitudes
were not substituted for the analytic squared weights.

Two failed assertions are preserved with their original sources and logs:

1. `ring_exact.py` compared an unsimplified Laurent matrix product structurally
   to zero. Its entries cancel exactly. `RING_EXACT_FAILURE.json` records the
   expressions and the sole change in `ring_exact_repaired.py`: simplify the
   product before comparison. The exact operator identity was unchanged.
2. `ring_survival.py` guessed the wrong sign for the off-diagonal entry of the
   auxiliary mean-time matrix with the chosen +i omega convention. The exact
   Lyapunov assertion rejected it. `RING_SURVIVAL_FAILURE.json` records the
   failed and corrected left sides; `ring_survival_repaired.py` corrects the
   sign. The diagonal mean formula remained 1/(2 kappa) and was subsequently
   checked against the full physical matrices.

Successful substantive runs are `ring_exact_repaired.py` (symbolic identities
and complete operator residuals), `ring_survival_repaired.py` (160 full-matrix
time controls and fixed-density quadratures), `cube_gram.py` (all exact marked
Grams), `cube_field_control.py` (finite-support physical field controls), and
`limit_controls.py` (18 complete-matrix mean controls and shrinking packets).
Their full raw results are retained. The common builder is fully local to
this packet and has no author imports.

This result stops at the supplied unit-rotor effective process. It does not
establish a uniform joint finite-spin/eta approximation, infer a large-volume
law, identify a photon regime, or prove convergence of microscopic histories
conditioned on a first event. The cube statement is expressly immediate; the
ring count limit concerns the actual specified post-mark preparation. The new
author seal hash was received in a message, but its contents remain unopened.
The next step is an explicitly authorized source-bound comparison after this
PRE freeze.

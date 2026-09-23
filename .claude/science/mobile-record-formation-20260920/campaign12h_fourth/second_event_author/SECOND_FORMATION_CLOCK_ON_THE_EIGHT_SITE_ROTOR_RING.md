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

# Integrated global chart-sector ratios from buffered conditional rarity

Research derivation, 2026-11-09; independent check pending. This proof is
conditional on the unreviewed arbitrary-exterior/buffered-core suppliers pinned
below. It establishes an actual integrated compact-versus-chart sector ratio,
not disconnected factorization, a connected logarithm expansion, or mass gap.
Same fixed two-step SU(2) quotient, beta=u, both lambdas=kappa*u, fixed odd
L>=3, kappa>0, terminal V=I, periodic terminal-cell ownership and full normalized
kernels as in those suppliers. No numerical, network or Git operation; only
this new file is written. Earlier proof files remain unchanged.

The avoidance argument is the standard generalized lopsided local-lemma
method, written out here. Method credit: Nicholas J. A. Harvey and Jan Vondrak,
[arXiv:1711.06797](https://arxiv.org/pdf/1711.06797), equation (1), Lemma 1 and
Claim 3 with its proof, pp. 1–3. The supervisor reported checking these proof
windows and their conditional nonneighbor formulation (credited there to
Albert–Frieze–Reed beyond Erdos–Spencer). This worker independently supplies
the finite induction below; the cited method supplies neither the SU(2)
conditional-tail premise nor spatial clustering. No novelty claim for the
local-lemma argument is made.

## 1. Fixed chart events and the precise probability premise

Let Lambda be the finite terminal-cell set. Use exactly the fixed Cartesian
logarithm cube of `nonlinear-chart-response.md`: a retained link is chart-good
iff it has a logarithm z in that injective small chart with |z_r|<delta_ch
for r=1,2,3. The fixed delta_ch>0 is small enough that sqrt(3)delta_ch<pi.
This is a Borel subset of SU(2), independent of all sources and terminal V.
Outside it, any principal logarithm has norm at least delta_ch; at -I the
same conclusion holds independently of the chosen axis. Consequently

    link chart-bad => |a_e-I| >= delta_*=2 sin(delta_ch/2)>0.

Let E_x be the event that some retained link owned by cell x is chart-bad.
Let G_J=intersection_{j in J} E_j^c, G_empty=whole space. These events depend
only on the quotient coordinates owned by their indexed cells. The global
G_Lambda is exactly the supplier's product chart, up to measure-zero faces.
A product cap contained in that chart has positive product Haar measure.
Since the actual finite-volume density is strictly positive, P(G_J)>0 for
every J, before using any local lemma. Thus all conditional probabilities
below are well-defined. No volume-uniform lower bound is presumed here.

Use the buffered-core supplier with threshold delta_*. It fixes h independent
of u,volume,S,exterior and constants a>0,u0 such that for every nonempty
S subset Lambda, with R=N_h(S),

    P(intersection_{x in S} E_x | a outside R)
       <= eta^|S|,  eta=exp(-a*u), u>=u0.                    (H)

Indeed the left event is contained in the supplier's joint chord-rough event;
its arbitrary-exterior bound is exactly (H). The original compact posterior
is used here, with no chart conditioning. The conditional law selects every
whole factor reading R, including hidden outputs and all normalizers. A whole
torus R and its empty exterior cause no exception. The root input hashes
were checked before using (H).

Write B_h=(2h+1)^4. Periodic identifications give |N_h(S)|<=B_h|S|.
Make an undirected graph on Lambda by joining distinct i,j with j in N_h(i).
Its degree is at most D=B_h-1 (or any larger fixed bound). For i and
J subset Lambda\N_h(i), G_J is measurable outside N_h(i). Integrating (H)
against the normalized exterior law conditioned on G_J proves

    P(E_i|G_J)<=eta.                                        (L)

Similarly, for arbitrary S and J disjoint from N_h(S),

    P(intersection_{x in S}E_x|G_J)<=eta^|S|.                (L_S)

These tower-property consequences use the uniform pointwise exterior bound;
rare-set bounds without that hypothesis would not imply (L). No independence
of events, cells, or collars appears.

## 2. Finite avoidance induction, including all conditioning sets

Fix x0 in (0,1) such that

    eta <= x0 (1-x0)^D.                                    (7)

We prove P(E_i|G_J)<=x0 for every J not containing i, by induction on |J|.
The empty case follows from (L) and eta<=x0. For the inductive step, split
J=J_far disjoint union J_near, where J_near consists of neighbors of i and
J_far is outside N_h(i). If J_near is empty, (L) gives the result directly.
Otherwise, positivity and set inclusion give

    P(E_i|G_J)
       <= P(E_i|G_Jfar)/P(G_Jnear|G_Jfar).

Order J_near as j1,...,jk. The denominator equals the product, for r=1,...,k,
of 1-P(E_jr|G_{Jfar union {j1,...,j(r-1)}}). Each conditioning set excludes
j_r and has size |J_far|+r-1<=|J|-1. The induction hypothesis therefore bounds
this product below by (1-x0)^k. The numerator is at most eta by (L), and
k<=D. Thus P(E_i|G_J)<=eta(1-x0)^(-D)<=x0, completing the induction.
All avoidance denominators are positive by the cap argument above; alternatively
the same induction builds positivity by adding one good event at a time.

It follows, by ordering any A disjoint from B, that

    P(G_A|G_B)>= (1-x0)^|A|.                              (8)

Empty sets are covered with the usual value one. The assertion is finite
and uniform in the number of cells. It makes no claim that the E_i are
independent Bernoulli variables or that their conditional probabilities are
small when arbitrary neighboring fields themselves, rather than avoidance
events, are fixed.

## 3. Joint bad events under arbitrary good-event constraints

Let S,J be disjoint cell sets. Put R=N_h(S), J_in=J intersect R,
J_out=J\R. By (L_S), then (8),

    P(intersection_{x in S}E_x | G_J)
       <= P(intersection_{x in S}E_x | G_Jout)
                                  /P(G_Jin|G_Jout)
       <= eta^|S| (1-x0)^(-|J_in|)
       <= [eta (1-x0)^(-B_h)]^|S|.                       (9)

The first inequality retains the numerator's avoidance restriction only by
upper-bounding it by the unrestricted joint bad event. There is no assertion
of conditional independence. The geometric estimate for J_in is deliberately
conservative; S itself is excluded from J, but that improvement is unnecessary.
Equation (9) also holds for S empty, with probability one.

## 4. Actual global sectors and a released-region ratio

Let W(a,h;V) be the complete original chain density after exact forest
reconstruction. At zero sources it is independent of h and every kernel
normalizer remains in W. Define, against product probability Haar da dh,

    Z_S(V;s,t)=integral 1_{[all E_x, x in S] intersect G_(Lambda\S)}
                     W(a,h;V) exp(sF(U(a,h))+tG(U(a,h))),
    Z_empty(V;s,t)=integral 1_{G_Lambda}
                     W(a,h;V) exp(sF(U(a,h))+tG(U(a,h))).

Here F,G are bounded real original sources, independent of V; no gauge
invariance or orbit-covariance suppression is required. The full h integral
is retained. Events are fixed quotient-coordinate events as above. Write
R_S=Z_S/Z_empty, evaluated in probability estimates at zero sources, V=I.
The unnormalized total partition factor cancels, so this is exactly

    R_S=P(all E_x for x in S | G_(Lambda\S))
                           /P(G_S | G_(Lambda\S)).

Apply (9) to the numerator and (8) to the denominator to obtain

    0<=R_S<=epsilon(u)^|S|,
    epsilon(u)=eta (1-x0)^(-B_h-1).                       (10)

For S empty the ratio is exactly one. Every actual sector has positive
integral in this model: one can choose an open set with a chart-bad owned
link in each selected cell and all other cells chart-good. Positivity is
not needed for the derivative recurrence below if an empty sector is allowed,
since its integral and all derivatives are then identically zero.

For a region A define Z_release(A) by imposing chart goodness only on
Lambda\A. At zero sources and V=I, the exact ratio is

    Z_release(A)/Z_empty
       =1/P(G_A|G_(Lambda\A)) <=(1-x0)^(-|A|).           (11)

In particular Z_full/Z_empty<=(1-x0)^(-|Lambda|). This may grow exponentially
in volume: no uniform global-chart probability lower bound is claimed.
The exact sector decomposition is Z_full=sum_{S subset Lambda}Z_S; (10)
also gives Z_full/Z_empty<=(1+epsilon)^|Lambda|. These sums are ordinary
positive integral decompositions, not a polymer gas or factorization.

For sufficiently large u choose x0=2eta. In addition to u>=u0, require
2eta<1 and (1-2eta)^D>=1/2. Then (7) holds. Such a fixed threshold in u
exists for fixed D, including D=0. Formula (10) gives

    epsilon(u)=exp(-a*u)[1-2exp(-a*u)]^(-B_h-1) -> 0.

For large enough u it is, for example, at most 2exp(-a*u), after enlarging
the lower bound on u once more. All thresholds and graph constants depend
only on the fixed supplier/chart parameters. The local release logarithm
is bounded by -|A|log(1-2eta), hence O(eta|A|) in this same regime.

This proves the proposed integrated global normalization comparison under
(H). It does not assert a pointwise ratio of an arbitrary-exterior all-chart
regional integral to a compact regional integral. The avoidance conditioning
averages that exterior; changing it to a fixed rough exterior would change
the statement.

## 5. Complete distinct-label mixed jets of the sector ratio

Take the four labeled differentiation directions
(partial_s,partial_t,D_c,D_d), with distinct terminal links c,d and fixed
first tangent vectors v_c,v_d at I. Each label is used at most once.
The original F,G and all events are independent of V. At zero sources and
terminal identity the weight's four first log insertions are

    X=(F,G,A_c,A_d),
    A_c=kappa*u <v_c,M_{1,c}>,
    ell=(||F||_infinity,||G||_infinity,
                               kappa*u|v_c|,kappa*u|v_d|).

The log weight has no mixed derivatives between any distinct labels in this
list: different final-link factors depend on different terminal outputs;
normalizers have no output dependence; sources enter linearly and have no
V dependence. Thus for any subset I of labels and either sector T,
compact differentiation with the fixed indicator gives exactly

    D_I Z_T = integral_sector W exp(sF+tG) product_{i in I} X_i,
    |D_I Z_T| <= Z_T product_{i in I} ell_i                (12)

at the specified base point. The Haar orbit integral remains inside this
formula, so it retains every conditional source covariance. A source-independent
normalization of the original q_u is common and independent of these labels.
No derivatives of a cutoff or replaced intermediate Wilson law appear.

Differentiate Z_S=R_S Z_empty. For nonempty I,

    D_I R_S=(D_I Z_S)/Z_empty
       - sum_{K proper subset I}(D_K R_S)
                                (D_(I\K) Z_empty)/Z_empty. (13)

Induction on k=|I| using (12) proves

    |D_I R_S|<=C_k R_S product_{i in I}ell_i,
    C_0=1,  C_k=1+sum_{j=0}^{k-1} binom(k,j) C_j.         (14)

Explicitly (C_0,C_1,C_2,C_3,C_4)=(1,2,6,26,150). The recurrence avoids
any need to take log of a zero sector. For positive sectors it is equivalent
to differentiating exp(log Z_S-log Z_empty), whose log derivatives are the
complete sector cumulants. The order of distinct labels is irrelevant here;
(14) therefore covers their ordered mixed jets too. Combining with (10),

    |D_c D_d partial_s partial_t R_S|
      <=150 kappa^2 u^2 |v_c||v_d| ||F||_infinity||G||_infinity
                                                   epsilon(u)^|S|. (15)

For S empty the actual nonempty jets vanish since R_empty=1; the inequality
remains valid. A vanishing ell corresponds to an absent insertion and the
actual derivative vanishes. Repeated terminal-link derivatives would add
second derivatives of its score and are not covered. Equations (14),(15)
are estimates at V=I,s=t=0; their proof differentiates the integrals first,
then uses the zero-source sector rarity. No unproved uniform rarity in a
nonidentity terminal neighborhood is used.

## 6. Normalization boundary and recovery checkpoint

Every ratio above uses one common full global density with all fine action,
intermediate/final kernels and radial normalizers. The initial conditional
supplier cancels outside factors only after fixing the outside coordinates;
no such factor is dropped during the subsequent global exterior integration.
For an explicitly different normalized coarse conditional Q=N/D, the complete
response is the derivative of log N minus the derivative of log D. A common
overall factor cancels in R_S by construction; a different, parameter-dependent
coarse-conditional denominator must still be treated separately. In particular
(15) is a derivative of a sector ratio, not automatically a connected coarse
response or the fourth derivative of log(Z_full/Z_empty).

Closed conditional consequence: (H) implies the finite lopsided induction,
the integrated exact-sector comparison (10), local release (11), and complete
mixed ratio jets (14),(15), without independence. New unverified dependencies
remain the two pinned SU(2) suppliers and this argument's independent review.
No disconnected-sector product formula, connected spatial activity norm,
full-posterior cumulant decay, arbitrary boundary neighborhood, all-depth
estimate or mass-gap conclusion is supplied. No editable prompt changed.

Source identities, read from the root worktree:

| Source | SHA-256 |
|---|---|
| arbitrary-boundary-interior-moments.md | c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11 |
| buffered-core-conditional-ratio.md | 204f48f463fb69eebb6b309996c663698dadd5969728f2a311176e21b53b42c7 |
| nonlinear-chart-response.md (worker copy, chart definition) | 5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1 |

Reopen the proof if (H)'s all-exterior uniformity, ownership measurability,
fixed chart, terminal derivative labels, or full-factor conventions change.

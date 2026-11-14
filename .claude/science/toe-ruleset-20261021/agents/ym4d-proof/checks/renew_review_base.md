# RENEW — inherited roughness, persistent flux and the remaining renewal estimate

**The renewal lemma needed by LF-JMBR is OPEN.** A uniform loss of inherited
roughness does not follow from S4′ averaging or the normalized kernel's
restoring force. Below is an exact periodic SU(N) family, for every N>=2
and every odd L>=3, whose most likely coarse fields remain maximally rough.
Positive-measure neighborhoods persist for any prescribed finite number of
steps with conditional probability tending to one as those couplings grow.
This refutes a uniform *forward, pointwise-in-input* return mechanism. It
does not refute renewal after charging the original weight, changing the
matched reference or extracting relevant/marginal terms.

There is useful positive structure: localized **linear** curvature defects
dilute as L^(-2r) in sup norm, and an explicit finite-window operator bound
would combine exact reader integration with fresh-gap prices. That operator
bound on the actual all-cut reference remains the exact missing sub-lemma.
Clause 1 retains its finite algebraic PROVEN status; clauses 2–5 remain OPEN.

PROVEN denotes a written mathematical statement with the hypotheses below;
ARGUED denotes a proposed application; OPEN denotes an unmet obligation.
These labels confer no retained/audit status or Yang–Mills existence result.
Source identities, coverage, checks and review are in [RENEW_LOG.md](RENEW_LOG.md).

Credit: Tadeusz Balaban for large-field renormalization and recycling;
Jonathan Dimock for its exposition in [Large fields](https://arxiv.org/abs/1212.5562)
and [Convergence](https://arxiv.org/abs/1304.0705). These papers treat a scalar
model in three dimensions. They supply methods and attribution here, never
a four-dimensional gauge-model premise. Every load-bearing calculation
below is rebuilt. No memory-only [m] item is used.

## 1. Target, units and the reference that must survive

Fix finite compatible four-dimensional tori, N>=2, odd L>=3, probability
Haar measures and t_j=kappa u_j>0. All are supplied mathematical model data.
A block is B(X)=LX+{0,...,L-1}^4, with root c_X=LX+o, o=(L-1)/2 in every
coordinate. Decision 4 uses the same coordinate order at both ends:

    T_y^sigma=P^sigma(c_X,y) S_y P^sigma(c_(X+e_mu),y+L e_mu)^*,
    M_c=(24 L^4)^(-1) sum_(sigma,y in B(X)) T_y^sigma,
    h_M(V)=Re tr(V^*M)/N,
    k_t(V;M)=exp(t h_M(V))/Z_t(M),
    Z_t(M)=int_SU(N) exp(t h_M(W))dW.                    (R1)

Here ||M||op<=1. The arithmetic mean need not be group-valued. Every
normalizer in (R1) reads the same fine links as M and is retained.
The reference at an effective step is precisely

    R_h(V)=int rho_(j,h)(U) K_j(V,U)dU,
    Z_A(V)=int chi_A(U) b_j(U) K_j(V,U)dU,
    b_j=exp(-u_j sum_p s(U_p)),   s(W)=1-Re tr(W)/N,
    Q_h=R_h/Z_A.                                         (R2)

rho_(j,h) contains the actual earlier action, kernels and complete past
history, including absence predicates. It is not a fresh Wilson density.
Current failure records have been summed in R_h; a selected current record
must otherwise stay inside the integral. No history mass is divided out
and then reused as a rare-event price.

The consumer is LFPRICE §6 on RD4's D_*: the required fixed original-source
polydisc and specified coarse charts, uniform in volume, depth and an
explicit stable history/chart class. Its full norm is

    ||F||_mu=sup_x sum_(X contains x) e^(mu |X|) sup_(D_*)|F_X|. (R3)

Full supports retain original sources, inactive vertices, fixed exterior
readers, kernel denominators and connected hulls. A contracted geometric
shadow is not automatically the support in (R3). FR, KR and TC remain the
named coordinator inputs for domains, full interaction/prefactors and
original-law joint charging/tails, respectively; no extension of their
selected-sector scope is assumed.

Geometric roughness below means the selector's raw plaquette distance
||I-U_p||op. Multiplication by an inverse lattice-spacing squared changes
units and changes the corresponding threshold too. A dimensional factor
alone cannot convert a failed raw cut into a successful return.

## 2. Averaging: a sharp marginal bound and a localized gain

### R-LIN — PROVEN for the noncompact abelian linearization

Let A be a real periodic link 1-form and F=dA. Linearizing the paired
contours gives Q_root=Q_str-dh, where h is the average axial-path integral.
Indeed the initial axial leg contributes h(X), its reversed translate
contributes -h(X+e_mu), and the central legs contribute Q_str A. Therefore
dQ_root A=dQ_str A. Summing the four averaged links of a coarse plaquette
cancels their interior edges. With common y in its lower block, this is
exactly the sum of F through the translated L by L square:

    F'_munu(X)=L^(-4) sum_(y in B(X))
                     sum_(s,t=0,...,L-1) F_munu(y+s e_mu+t e_nu). (R4)

All weights are nonnegative. The row sum is L^2. The column sum is L^(-2):
for each pair s,t, a fixed fine plaquette determines exactly one block X
and one y; there are L^2 pairs, each weighted L^(-4). Periodic multiplicities
are counted. Thus weighted Cauchy–Schwarz, followed by the column sum, gives

    sum_P |F'(P)|^2 <= L^2 sum_(P,p) M_(P,p)|F(p)|^2
                    = sum_p |F(p)|^2.                    (R5)

The same argument in dimension d gives L^(4-d). In common physical units
F'/L^2 is a probability average, whose sup-norm bound is 1, not a strict
factor below 1. Constant curvature on a lifted local patch is reproduced.

The action constant 1 is sharp even for exact, zero-mean periodic fields.
Take fine side LT, T>2, k=2pi/(LT), and the complex notation
F_12(x)=exp(i k x_1), obtained from A_2=exp(i k x_1)/(exp(i k)-1).
Its real or imaginary part is a real example with the same norm ratio.
Equation (R4) multiplies this mode by (sum_(s<L)exp(i k s))^2, and the
coarse lattice has L^(-4) as many sites. Consequently

    ||F'||_2^2/||F||_2^2
       = [sin(L k/2)/(L sin(k/2))]^4  --> 1 as T --> infinity. (R6)

Amplitude rescaling can make the potential arbitrarily small without
changing this ratio. Removing the constant mode alone does not give a
volume-uniform strict contraction. This is a statement about this linear
operator, not the full extracted nonlinear RG map.

**Localized gain.** Iterated straight averages compose to the direct
straight average of side n=L^r: write its base-point offset and path offset
in base L to biject the nested sums with the direct sums. The axial
differences stay exact under further root averaging, since a gradient's
path integral is its endpoint difference. Hence (R4) at depth r has L
replaced by n. For a fixed coarse/fine plaquette pair, at most n^2 choices
of the two in-plane offsets contribute; its matrix entry is <=n^(-2).
For each orientation, and therefore with the total plaquette l1 norm,

    ||d Q_root^(r) A||_infinity <= L^(-2r) ||dA||_1.       (R7)

Take coarse side at least two to avoid any ambiguity about wrapping;
alternatively count all periodic multiplicities in the same direct sum.
In particular, s supported fine plaquettes of size <=b give <=s b L^(-2r).
A fixed curvature cut epsilon is passed once s b L^(-2r)<epsilon. For
varying cuts use the actual epsilon_r in this inequality. This is a
bounded-time deterministic return for that **linear localized** class.
It is not a bound uniform in the inherited l1 size or in the original
source-reader support, nor does it bound the kernel noise.

These calculations rebuild LINEAR_PACKAGE §2.2–2.3 rather than interpret
its action factor 1 as an irrelevant contraction. BFT_A §3.4–3.6 gains a
power from small-field oscillations in a derivative norm. BFT_B §22.3–22.8
uses a small-curvature refinement and the cancellation of Q-Q_ax on constant
curvature to bound a **residual**. Neither is an averaging theorem for
arbitrary inherited rough inputs. The cancellation of the averaging
defect on constant curvature leaves that curvature present, as (R4) shows.

## 3. An exact inherited rough family in the actual nonlinear kernel

### R-FLUX — PROVEN at every N>=2 and odd L>=3

Let all torus sides be even and compatible with the required number of
blockings; for a horizon R take fine side T L^R with even T>=2L. Set

    g=diag(-1,-1,1,...,1) in SU(N),   g^2=I,
    U_1^(a,b)(x)=g^(x_2+a),
    U_2^(a,b)(x)=g^b,    U_3=U_4=I,    a,b in {0,1}.      (R8)

The superscripts are sign labels; the subscripts in (R8) are directions,
not RG levels. Periodicity follows from the even side. Every 12 plaquette
equals g, so its distance from I is 2 and s(g)=4/N. Every other plaquette
is I. These are actual group fields, not an arbitrary prescribed mean.

Write y=LX+r, r_mu in {0,...,L-1}, and keep the actual offset root c_X.
All path matrices commute here, but the specified paired paths are still
used. For direction 1 the translated axial paths have identical link
values and cancel; the length-L leg gives g^(X_2+r_2+a). For direction 2,
translation by L changes each direction-1 link by a factor g. The signed
number of such steps in the axial path is r_1-o, so the whole contour is
g^(b+r_1-o). For directions 3 and 4 the translated paths cancel and the
straight leg is I. These formulas hold for every coordinate order,
including negative steps and wrap-around.

Since sum_(r=0)^(L-1)(-1)^r=1, put
P=diag(L^(-1),L^(-1),1,...,1). The exact arithmetic means are

    M_1(X)=g^(X_2+a) P,
    M_2(X)=g^(b+o) P,
    M_3=M_4=I.                                          (R9)

In particular none is singular; the smallest singular value is >=1/L.
For M=W H with W in SU(N) and H Hermitian positive definite, set A=W^*V.
Expanding and taking the trace gives

    h_M(W)-h_M(V)
       =tr[(I-A)^* H(I-A)]/(2N)
       >=lambda_min(H) ||V-W||op^2/(2N).                (R10)

Here tr(A^*HA)=tr H, so no commutation between A and H is assumed.
Equality to zero forces A=I. Thus W is the unique global maximizer.
Applied to (R9), the unique maximizing output configuration is

    U' = U^(a,b+o mod 2).                                (R11)

The label a is unchanged; b is fixed or alternates. Every 12 plaquette
is still g. Iterating gives an exact rough orbit at arbitrary finite depth,
with **zero kernel gap at every step** and nondegenerate means. In fact
k_t(W;M)>=1 because Z_t(M)<=exp(t h_M(W)); there is no exponential loss
at the maximizing Haar density. A point density alone is not a probability;
the next lemma supplies the positive-measure statement.

The quadratic restoring force therefore pulls toward a rough center in
this family. Equation (R10) controls fluctuation distance from W, not
curvature distance from I. The short-mean/Haar degeneracy M=0 is not needed
for this example. Finite seam costs of SOFTHARD G2 cannot turn (R10) into
a probability of leaving this rough center.

### R-TUBE — PROVEN finite-horizon persistence, with explicit quantifiers

First rebuild the gap bound used by JMBRB. Set D=2N^2. An operator-norm
Haar ball of radius 0<r<=1 has mass at least (1+4N/r)^(-D): subdivide
the real and imaginary matrix entries in [-1,1] into intervals of length
<=r/(2N). At most (1+4N/r)^D cells are needed; each occupied cell lies
in an r-ball about one group representative. Haar invariance and the
cover give the bound. Also h_M is 1-Lipschitz in operator distance.
The 1/t ball about a maximizer therefore proves, for t>=1,

    P_(k_t)(psi_M>=A) <= C_N(t) exp(-t A),
    psi_M=max h_M-h_M,    C_N(t)=e(1+4Nt)^D.             (R12)

Keep the bound at most 1 when using it as a probability. This proof
includes every normalizer and works for all arithmetic means.

Fix a finite horizon R, a compatible torus as above and epsilon_max<2
bounding the raw small-field cuts at these levels. Let U^j be the exact
orbit (R11), and T_j(delta_j) the product of open operator balls of radius
delta_j about all its links. Choose

    0<delta_R<=min(1/8,(2-epsilon_max)/8),
    p_L=5L-4,
    delta_j=delta_(j+1)^2/(8 N L p_L),  j=R-1,...,0.     (R13)

A paired contour has at most p_L links. Telescoping unitary products gives
||M(U)-M(U^j)||op<=p_L delta_j on T_j. For an output link V at distance
>=delta_(j+1) from the template W=U_c^(j+1), (R10) and two trace errors give

    psi_(M(U))(V) >= h_(M(U))(W)-h_(M(U))(V)
                   >=delta_(j+1)^2/(2NL)-2p_L delta_j
                    =delta_(j+1)^2/(4NL).              (R14)

The same lower bound covers directions 3 and 4, whose baseline H is I.
Union bound over E_(j+1), then condition successively on the past. Uniformly
over every starting U in T_0,

    P_U(U_j in T_j for all 1<=j<=R)
       >= 1-sum_(j=0)^(R-1) |E_(j+1)| C_N(t_j)
                         exp[-t_j delta_(j+1)^2/(4NL)].  (R15)

The right side may be negative at moderate couplings; it is a lower bound,
not a claim of effective smallness there. At fixed R and fixed finite
lattices it tends to one as min_j t_j tends to infinity. Every plaquette
product changes by <=4delta_j in a tube. Thus every 12 plaquette in T_j
has distance >=2-4delta_j>epsilon_max and stays cut-bad.

Moreover choose positive gap thresholds A_j with
t_j A_j-D log(1+4Nt_j) tending to infinity, for example
A_j=a_0 t_j^(delta-1), a_0>0, 0<delta<1. A further union bound from (R12)
shows that the probability of **any** such fresh-gap event during these
R steps tends to zero. Persistent roughness and absence of these priced
gap events therefore occur together with probability tending to one.

Consequently there is no R<infinity and p>0, both independent of arbitrarily
large coupling, such that every real inherited input has probability >=p
of a curvature-small return within R steps under the plain forward law.
Nor does that law uniformly contract the maximum raw plaquette distance
by a factor <1: take delta_R arbitrarily small in (R15). These conclusions
are about the specified uniform input class and kernels. They do not say
that a fixed-coupling finite system can never return, or that all-history
weights on (R2) fail to be summable.

### Measure and charge classification

The four exact configurations (R8) have Haar measure zero. Each T_0 in
(R13) is a nonempty product of open group balls and has strictly positive
Haar measure. At finite couplings the Wilson density and all kernel
densities are strictly positive, so the finite tube event has positive
original-chain mass. The conditional lower bound (R15) also holds after
averaging any starting law supported in T_0.

It is **not** a claim that these inputs are common under the original law.
On T_0, each of its |Lambda_0| distinct 12 plaquettes gives the elementary
one-time raw action charge

    u_0 sum_p s(U_p) >= u_0 (2-4delta_0)^2 |Lambda_0|/(2N). (R16)

This uses 2N s(W)=||I-W||HS^2>=||I-W||op^2, obtained by expansion.
Integrating all future kernels preserves this original charge once; it
does not renew it. A normalized Wilson or Z_A comparison still includes
its actual denominator and the uncharged integral. No TC theorem is
replaced by (R16). Hence the classification is: a positive-measure
counterexample to uniform conditional smoothing, with an available raw
creation charge whose required matched normalized cost is unproved here.

The example fills a region rather than proving persistence of an isolated
singleton with a uniformly good collar. A restricted stable history class
could exclude it, but must specify that restriction and estimate its
complement. It cannot be omitted as a null set. For any fixed R the same
local example can be embedded in a larger identity field by filling the
finite backward reader set of the chosen plaquette tower and every contour
that creates its ancestors; all means used for that tower are unchanged.
No claim of a depth-independent size for that backward set is made.

## 4. What bounded-time return does hold without a new estimate

### R-CAP — PROVEN finite-volume, finite-coupling curvature return

For any real input, |h_M|<=1 implies k_t>=exp(-2t). If all m output
links lie in the radius delta ball about I, every output plaquette has
distance <=4delta. For delta<min(1,epsilon/4), this cap is curvature-small
and, uniformly in the input,

    P_U(curvature-small at the next level)
       >=p(t,m,delta)
       :=exp(-2tm)(1+4N/delta)^(-Dm)>0.                 (R17)

This follows by multiplying the lower density and Haar-cap estimates.
For first return time tau to the chosen level-dependent good sets,
conditional expectation gives

    P_U(tau>r)<=product_(l=0)^(r-1)(1-p_l).             (R18)

Indeed on the event of no earlier return, the next input is still a real
field to which (R17) applies. This proves a genuine but nonuniform renewal
bound for curvature-good fields. The complete chart/completion return
requires its own selectors and is not inferred from this statement.

The lower bound p tends to zero with coupling or m; a smaller raw cut also
reduces it. Even if a uniform finite p were supplied, a placement cost B
requires B(1-p)<1 for the resulting one-step geometric majorant. Equation
(R17) does not meet the weak-coupling RG budget, while (R15) rules out a
coupling-uniform p on the full input class by any stronger proof.

The fresh-gap bound (R12) remains useful: distinct output links are
conditionally independent, and sequential conditioning multiplies prices
for new past-adapted gap events. A fixed future field or all-cut conditioning
tilts that law; the multiplier and denominator then remain inside the joint
estimate. No probability bound on a fixed bad V is asserted.

## 5. Combine exact reader integration with a renewal structure

### R-EXACT — PROVEN finite algebra, rebuilding clause 1

Set J_h=rho_(j,h)/b_j at real current fields. For a bad block set B, use
its G_2 components Y (sup-distance edges <=2). Allocate the original
factors as b_j K_j=W_out product_Y w_Y, where w_Y contains every Wilson
plaquette and output kernel reading the replaced interiors I(Y).
Separated components have disjoint radius-one collars and replacement
coordinates. Put

    C_Y(eta,V)=int chi_Y w_Y dU_I(Y),
    T_B J_h=(product_Y C_Y)^(-1)
       int zeta_B(Uhat) product_Y w_Y(Uhat;eta,V)
                      J_h(Uhat_I(B),eta)dUhat_I(B),
    dnu_A=chi_A b_j K_j dU/Z_A,
    Q_h=E_(nu_A) sum_(B subset A) T_B J_h.              (R19)

C_Y>0 for real exterior data and V: a small identity cap of the interior
links satisfies their interior plaquette cuts, and every retained density
is positive. For a B summand, integrate the old good interiors first;
their masses product C_Y cancel exactly. The new interiors are bad and
all other cuts remain good. Summing B applies product_Q(chi_Q+zeta_Q)=1.
This proves (R19) without dividing by a hard predicate or by a history mass.
Earlier fields in J_h and every failure/absence predicate remain intact.
Empty or zero-mass sectors stay zero. Fubini is valid at finite volume.

For reader integration, multiply *all* factors reading a variable before
integrating it; the new factor reads the union of their remaining readers.
Induction proves this rule exactly. In a directed kernel graph, for a
selected set of factors, close its integrated readers under all ancestors.
Remove the complement in reverse time order: each remaining unused output
has only its normalized creator and integrates to one. Two selected
components with disjoint complete closures factor under the resulting
product kernels. A cross edge would put an ancestor in both closures.
Fixed terminal V kernels are factors, not integrated creators. Shared
outside variables join groups before their later integration.

These identities perform the JMBRA elimination needed before a renewal
split. They do not say that nu_A is a product law or that T_B J_h factors
over Y. A complete closure may be large, and the inherited-versus-bare
density difference can retain bulk original-source readers.

### R-WINDOW — PROVEN conditional renewal lemma

Here is a precise sufficient replacement for pointwise curvature smoothing.
Let X_j be spaces of connected insertions with the full norm (R3), at
one invariant norm rate and the same original-source/coarse domain.
Suppose an exact matched construction, after complete reader grouping,
gives linear operators C_j for continuation without return, and S_j for
first return followed by the specified extraction of relevant/marginal
terms. These are operators on insertions about a fixed admissible sea;
nonlinear changes of that sea require a separate bound below.

For some integer m>=1, B>=1, D_ret>=0 and 0<=theta<1, suppose, uniformly in j,
volume, depth and the specified histories,

    ||C_(j+s-1)...C_j|| <= B             (0<=s<m),
    ||C_(j+m-1)...C_j|| <= theta,
    ||S_j|| <= D_ret.                                    (R20)

All norms already include the correct local reference, kernel normalizers,
complex total variations, boundary debits, rooted re-blocking costs and
complete original readers. The empty product is identity. Then

    sum_(r>=0) ||C_(j+r-1)...C_j|| <= m B/(1-theta),
    sum_(r>=0) ||S_(j+r) C_(j+r-1)...C_j||
                                      <=D_ret m B/(1-theta). (R21)

Proof: write r=qm+s, 0<=s<m. The ordered product consists of q consecutive
m-windows and one prefix of length s, so its norm is <=B theta^q.
Sum s and q, then multiply by D_ret. No stationarity or commuting
operators are required. Finite-depth truncations satisfy the same bound.
The first-return identity itself is the disjoint split into the first
successful sector at each time and the remaining all-failed sector;
linearity and Fubini give exactly these products. Every chart/completion
failure must occur in C_j unless it has another explicitly estimated
disposition. The identity does not remove a failed small component.

New source insertions with full norm <=e_* at each step therefore have
total continued linear contribution <=e_* mB/(1-theta) at a fixed output
step, and the corresponding first-return bound includes D_ret. This is
norm arithmetic, not an evaluation of e_*, B, D_ret or theta for (R2).

A fresh-gap estimate can help verify an m-window bound. Partition its
continuations disjointly by their first newly gap-priced event or by no
such event. If the **same matched joint norm** bounds the no-gap window
by theta_coh and the first-gap piece at time l by b_l exp(-q_l), then

    theta <= theta_coh+sum_(l=0)^(m-1) b_l exp(-q_l).     (R22)

Triangle inequality proves this statement. When b_l<=b and q_l>=q,
theta_coh+m b exp(-q)<1 is sufficient. The raw forward value
q_l=t_l A_l-log C_N(t_l) from (R12) is not automatically that matched
q_l. Future tilts, normalization and full-support costs remain to be paid.
The genuinely new requirement is theta_coh<1 after appropriate extraction
or original-weight charging; the coherent orbit forbids obtaining it as
an unweighted supremum of forward no-gap survival probabilities.

### R-GROUP — PROVEN sufficient passage to clauses 3–4

Suppose the actual finite representation, after separately removing any
specified nonzero empty-support prefactor, is

    Z=sum_(I subset of labels) c_I E[product_(i in I) f_i], c_empty=1.

Require normalized local cells or the complete ancestral factorization
just proved, holomorphic densities, atoms and coefficients on D_*, fixed
selectors and locally uniform integration envelopes. Require every full
support H_i to be nonempty and connected.
For every selected family I, including overlaps, suppose its COMPLETE
coefficient-weighted absolute integral is <=product_(i in I)alpha_i.
Coefficients factor across complete overlap components and read no
parameters outside those supports. If the full supports H_i satisfy

    Q=sup_x sum_(i:x in H_i) e^((mu+2)|H_i|) alpha_i<=1/4, (R23)

then integrate each selected overlap component jointly; disjoint components
factor before a log is taken. Their weights form an exact hard-core gas.
For completeness, put v_i=e^((mu+1)|H_i|)alpha_i and
b_i=e^((mu+2)|H_i|)alpha_i. The positive rooted-tree recursion
T_i=v_i exp(sum_(j:H_j meets H_i)T_j) has supersolution b_i because
the child sum is <=Q |H_i|. Iterating from zero bounds integrated connected
groups at rate mu+1 by Q. To bound the logarithm, order incompatibility
edges and assign each connected graph its Kruskal spanning tree. Graphs
with that tree form an interval of optional later edges; their alternating
sum has modulus <=1. The second tree recursion spends the remaining unit
of support exponent and bounds the log norm at rate mu by Q. Repeated
labels occur in this second expansion, and marking a root changes 1/n!
to 1/(n-1)!, as in the rooted-tree bound.

Multiply original atoms by z. The bounds converge for |z|<2 since 2Q<=1/2.
Near zero the exponential of the connected series equals the finite gas;
analytic continuation gives equality at z=1. This proves nonvanishing.
Holomorphy in D_* additionally uses the stated densities, coefficients,
fixed selectors and envelopes, not just this auxiliary z argument.

Long readers need not be truncated. For core weights a_gamma with supports
D_gamma and reader weights alpha_i with supports H_i, fix sigma>=0, eta>=0,

    q=sup_x sum_(i:x in H_i) e^((sigma+1+eta)|H_i|)alpha_i,
    d=sup_x sum_(gamma:x in D_gamma) e^((sigma+1)|D_gamma|)a_gamma,
    q+d<=1/2, q<1/2.                                    (R24)

Require the same mixed joint integral and factorization. The first tree
bound alone bounds integrated groups at rate sigma by their input budget.
If d>0, multiply core weights by R=(1/2-q)/d>=1 and reader weights by
e^(eta|H_i|). The total input becomes 1/2. Every core-containing group
gains at least R, hence its full-root norm is <=(1/2)/R=d/(1-2q).
For d=0 it vanishes. Roots on tails are included because the tree bound
marks the output root, not a core root. This rebuilds JMBRA's weighted
alternative. An extent r outside all core supports uses reader supports
of total size at least r, giving the additional factor exp(-eta r).

Apply this once: either (R20) already pays all readers, or use (R24) for
the readers still to be attached. Small-field and renewed-type budgets
must together meet (R23). Abstract renewal plus separate marginal event
probabilities is not a substitute for its mixed joint hypothesis.

## 6. Updated clauses and the exact remaining sub-lemma

| LF-JMBR clause | Status after this work | Actual advance / remaining obligation |
|---|---|---|
| 1. Exact representation and supported changes | **PROVEN, finite algebraic scope** | (R19) rebuilds the actual replacement identity and complete-reader elimination. No bounded cell size or uniform complex-domain statement is inferred. |
| 2. Joint charge, reference and boundary bound | **OPEN** | Fresh gaps have (R12); inherited rough centers can persist by (R8)–(R15). The one-time charge (R16) still needs the same-reference joint comparison. A positive finite G2 debit supplies no renewal loss. |
| 3. Common nonzero complex reference / local TV | **OPEN** | (R23) would construct nonvanishing if instantiated on D_*. Real forward survival and positivity do not control the different all-cut denominator or its complex variation. |
| 4. Integrated overlap types and full supports | **OPEN quantitatively; finite grouping PROVEN** | (R19), (R23) and (R24) retain complete readers. Neither their actual small joint weights nor uniform rooted history/type sums are supplied. |
| 5. Every small return, failed alternative and next step | **OPEN** | (R7) proves linear localized dilution; (R17)–(R18) give only nonuniform curvature return. (R20)–(R22) give a conditional finite-window renewal mechanism. Actual extracted operators, coherent continuation control and invariant budgets remain missing. |

**RENEW-MATCH(m) — OPEN, the exact remaining sub-lemma.** Exhibit an m
independent of volume/depth, a stable specified history/chart class and its
complement handling, the common D_* and full norm, and an exact paired
construction for (R2), with the following data:

1. On each complete selected reader group define the continuation with no
   fresh gap and no successful return, including every small completion
   failure. Retain inherited/bare reference differences and bulk sources.
   Specify the actual relevant/marginal extraction, including vacuum and
   coupling terms; do not replace it by subtraction of an unspecified mean.
2. Prove, in the same joint complex-reference norm, a no-gap m-window
   operator bound theta_coh and first-gap bounds b_l exp(-q_l) satisfying
   theta_coh+sum b_l exp(-q_l)<1, with uniform prefix and return bounds
   B,D_ret. Each original action fraction is allocated at most once.
3. Prove the mixed full-support budget (R23) or its weighted version,
   and an invariant nonlinear remainder bound. For example at window
   endpoints x'<=theta x+C x^2+e, for C,e>=0 and M>0, is invariant
   on 0<=x<=M if
   theta+C M<1 and e<=(1-theta-C M)M. Relevant/marginal coefficients have
   their own explicit recursion and are not hidden in x.

The last elementary implication follows from Cx^2<=CMx; induction gives
invariance. Its antecedents are not supplied by this note. FR/KR/TC may
provide parts only when their exact hypotheses match these integrals.
RENEW-MATCH is substantial constructive work overlapping clauses 2–5;
it is not a weaker solved reformulation or four independent new walls.

**ARGUED next attack.** Separate the coherent curvature into a specified
background/main action and test dilution only on a localized residual,
using (R7) as the linear benchmark. Build the matched conditioned reference
for that split, carrying the coherent sector's original weight and every
completion failure, then estimate its extracted m-window operator. The
other live option is an original-weight charge for persistent coherent
regions with verified full-reader sums. The flux witness is compatible
with both routes; it forbids dismissing the coherent branch as a rare
kernel fluctuation.

## 7. No-Go Discipline Gate — partial narrowing, no exhaustion certificate

**N1.** Actual mechanisms examined are (i) geometric averaging/dilution,
(ii) restoring-force/gap pricing and (iii) compact-kernel minorization.
Their distinct scopes and limitations are proved above. Weighted adapted
references with extraction and a joint original-action allocation remain
live, uncompleted alternatives. No five-exhausted-family packet PASS is
claimed. The output is partial narrowing with an honest residual, not an
all-route no-go.

**N2.** No independent-wall count is claimed. Let J be the actual joint
complex expansion on D_*, Z its nonvanishing/TV control, and I the invariant
renewal/extraction. Pairwise: J implies its nonvanishing part of Z by (R23);
the reverse is unresolved. I requires the matched J/Z bounds at successive
steps; their one-step versions do not here establish I. Relations between
other portions of J and Z remain unresolved. These are coupled obligations.

**N3.** Explicit conditions are supplied model/geometry, linearization in
§2, even compatible tori and the exact field in §3, finite horizon and
weak-coupling limit in (R15), and all operator/reference/analytic assumptions
in §5. A small-field background is not assumed for the flux witness. No
approved primitive is classified as a missing analytic estimate.

**N4.** LINEAR_PACKAGE action factor 1 matches (R5), not a nonlinear
all-history bound. BFT residual smoothing concerns a different quantity.
JMBRB B-GAP matches only (R12)'s forward gap event. JMBRA's reader theorem
matches the exact grouping, not smallness of its inputs. SOFTHARD G1 is
analytic smoothing of a density and G2 is a finite seam response; neither
asserts return of its kernel center. No prior negative headline carries
the counterexample proof.

**N5.** Per element/link: exact arithmetic means and gap (R9)–(R10).
Per site/plaquette: persistent g curvature and one-time raw charge.
Per mode: (R6) refutes strict uniform linear action contraction.
Per block: (R7) supplies localized linear dilution; the nonlinear witness
does not settle isolated-small-core completion. Lattice-wide: (R15) is a
finite-horizon conditional statement, (R21) a conditional norm summation.
No continuum, spectrum, mass-gap or actual Z_A divergence claim is made.

**N6.** A background/residual split, a matched reference, an extraction
projection or a compatible weighted norm is mathematics requiring proof,
not a new physical axiom. Nothing here asks to change Decision 4 or the
primitive registry.

**N7.** Strongest counter-route to a broad negative conclusion: the
coherent flux sector carries substantial original action, whereas a
bounded localized perturbation has the linear dilution (R7). Charge the
first sector once under a matched reference and extract the coherent
relevant/marginal response in the second. Establish the resulting joint
m-window estimate with all readers. JMBRA's exact grouping and JMBRB's
extracted-operator alternative leave this route open. The forward
counterexample cannot invalidate that weighted construction.

**N8.** The inspected lane already distinguishes constant reproduction,
localized impulse dilution, raw gap prices, cone cancellation and actual
reference ratios. This note does not revive LARGE55's withdrawn zero
boundary cost or treat its numerical impulse examples as a uniform
nonlinear tower theorem. Targeted main/lane searches are recorded in the
log; no exhaustive literature or open-PR novelty certification is claimed.

No numerical experiment was executed: the required nice priority was
denied, and no guard was weakened. The analytic proofs and fresh independent
review are the evidence, with review disposition recorded separately.

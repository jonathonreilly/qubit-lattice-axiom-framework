# RD4 — conditioning and large-field boundaries for the normalized step

**Neither Route C nor Route L closes uniform B2/B3 on the actual model.**
Both routes are probed below. Conditioning admits an exact local-predicate
factorization and a conditional expansion with the mandatory mass extracted
once. The direct conditioned-Haar instance fails a specific smallness
inequality. The large-field split admits a precise estimate through the
remaining integration, but its matched-reference, boundary and joint
factorization inputs are still unproved. These are partial constructive
results and technique diagnostics, not an obstruction to the RG theorem.

PROVEN labels the written statement under its displayed hypotheses; ARGUED
labels an uncompleted construction; OPEN labels a required estimate for the
actual step. Review and source identities are in [RD4_LOG.md](RD4_LOG.md).
No numerical physics experiment is used. All calculations below are written
proofs; no numerical PASS or inherited review verdict supplies a premise.

The small/large-field organization is due to Tadeusz Balaban. Jonathan
Dimock's [Part II](https://arxiv.org/abs/1212.5562) and
[Part III](https://arxiv.org/abs/1304.0705) explain it for scalar phi-four
theory in three dimensions. They provide methods and attribution only.
The probability, integration and connected-graph estimates used here are
rebuilt below. No memory-only [m] statement is load-bearing.

## 1. Fixed target, sources and admissible data

Use the exact finite SU(N) Wilson/Decision-4 chain, N>=2, odd L>=3,
normalized Haar, positive real u_j and kappa, and the original coefficient
sources of [RD](RD.md) R1–R10. The kernel parameters remain fixed when those
sources vary. These are supplied mathematical model data. This note does
not derive a physical identification from the repository's axiom set.

At stage k let h be RD R2/R3's recorded failures, H_k its inactive set,
B a current return region, eta **all** frozen current links and V the new
coarse field. Open the earlier fields in the actual denominator:

    D_h(z)=O_h(z)^(-1) int chi_B Xi_h W(z,x) dmu(x),
    W=rho_0^epsilon product_(j<=k) K_j,
    N_h(z)=O_h(z)^(-1) int zeta_B Xi_h W(z,x) dmu(x).     (4.1)

Here mu is the product Haar law in RD R10, O_h is RD R6's exact frozen
factor, and any additional numerator selector stays inside its integral.
No inherited density is replaced by a Wilson action. D_h/N_h are local
quotient objects; R_h, A_h, Z_A and Q_h=R_h/Z_A below are the distinct full
integration/reference objects of RD3 D8 and RC1–RC3.

Only fibres with D_h(0)>0 may use D_h(0) as reference. Zero-mass histories
remain zero summands in RD R8 and are never divided by their mass. The
concrete positive-fibre test used here is the failed history in RD3 D1: two
adjacent level-zero bad blocks, n_0=1, producing H_1={-1,0,1}^4 of size
81, with T>=7. Those illustrative cuts are not the consumer's small-chart
thresholds. An eventual uniform theorem needs a specified, stable
admissible history/chart class and its actual thresholds.

For connected full original-reader supports X in the ambient block graph,

    ||K||_mu = sup_v sum_(X contains v) exp(mu |X|) sup_D |K_X|,
    mu>=0,                 beta=mu+2.                    (4.2)

Inactive vertices and original source readers count in both the support
size and the root supremum. No contracted-hole distance is used.

The target domain has original-source radius rho_*>0 independent of
volume, level and admissible history, together with the complex coarse
domain required by STEP55. Write it as D_*=(source polydisc) times
(specified coarse charts/tubes). Its coordinates, gauge charts and
history selectors must refer to the same integral (4.1). A fixed polar
width and a width proportional to g_k/sqrt(kappa) are different demands;
the latter is STEP55's example. No choice is silently substituted.

The closest results are RD R15–R17's integrated hard-event expansion,
RD3's finite normalized step, LIB1's full-hole conversion, and corrected
CX-R. REVIEW_RD3 B2a/B2b/B3a/B3b remain the binding questions. FR, KR and
TC denote requested coordinator interfaces, with their scope specified in
section 6; they are not assumptions that the desired theorem holds.

## 2. Route C: extract the mandatory event once

### 2.1 Exact factorization of the actual history — PROVEN

Fix a past history prefix, hence its active set A_j. For each nonempty
G_2-connected Y subset A_j, let

    b_(j,Y) = [product_(Q in Y) zeta_(j,Q)]
              [product_(Q in N_2(Y) intersect A_j minus Y) chi_(j,Q)]
              (1-a_j(Y)).                              (C1)

N_2 is the closed graph neighbourhood in RD's G_2 (periodic sup-distance
at most two), not LIB1's face neighbourhood. The completion/size function
a_j(Y) is exactly RD R2; its completion variables and coarse-link readers
are included. The first two products say precisely that Y is a maximal
bad component. Consequently b_(j,Y)=1 precisely when it is a failing
component. For the prescribed F_j,

    I_(j,F_j|h) = product_(Y in F_j) b_(j,Y)
                 product_(Y notin F_j) (1-b_(j,Y)).       (C2)

The second product runs over **all** other nonempty connected candidates
in A_j. To prove (C2), evaluate a real configuration: only its actual bad
components can have b=1, and among them only the failing ones do. The
right side is one exactly when that failing list is F_j. This proves
the equality to RD R3, including configurations with successful singleton
components and incompatible/zero-mass records. Taking the product over
j<k proves the corresponding identity for Xi_h.

Thus set E_h=product of the mandatory b's, A_h^avoid=product of the
remaining (1-b)'s. The notation A_h^avoid is unrelated to RD3's mass A_h.
Each factor has its full source-free reader support in the opened chain;
choose connected hulls as in RD R10. They may be large. Overlapping
mandatory readers, including readers at different levels, must be merged.
The history has been factorized, not declared independent or small.

For any positive reference probability nu and p_h=nu(E_h)>0,

    int E_h A_h^avoid F dnu
        = p_h int A_h^avoid F dnu_(E_h),
    dnu_(E_h)=E_h dnu/p_h.                               (C3)

This extracts p_h once globally. It is the mass of the mandatory part,
not necessarily the probability of the whole history: the avoidance
factor remains. For normalization by the whole selected integral, its
mass is p_h times the last integral at the reference point. Neither mass
can subsequently be reused as the smallness of a normalized insertion.

For RD3's h, b_(0,Y_0) consists of two bad blocks and their G_2 good shell:
the size test already fails. It is independent of U_1 and has positive
Haar mass by RD3's explicit open cap. The factors excluding other failed
components are exactly the residual factors in (C2), including the
completion failures of other singletons. This is a genuine application
to that h, without imposing the stronger condition that every other
block be good.

**PROVEN actual mandatory-Haar mass.** In this RD3 example let
c=int chi_(0,Q) dHaar(U_(0,I(Q))), the same number for every old block.
The two adjacent blocks have a radius-two G_2 neighbourhood consisting
of 6*5^3=750 old blocks: its side lengths are 6 in their common direction
and 5 in each transverse direction. The old block torus has side LT>=21,
so these labels are distinct even if the displayed box crosses a periodic
seam. Its shell has 748 blocks. Interior-link coordinate sets of distinct
old blocks are disjoint; every chi_(0,Q) uses only that set. Therefore
under the lifted product-Haar reference,

    p_h=mu(b_(0,Y_0))=(1-c)^2 c^748.                    (C3a)

Let n_I=4L^3(L-1), delta=1/16 and use RD3's explicitly proved Haar-ball
lower bound m_delta=(1+4 sqrt(2) N/delta)^(-2N^2). The all-identity cap
in those n_I links lies in chi_Q=1. A cap around RD3's single marked
interior link g=diag(-1,-1,1,...,1) lies in chi_Q=0. Both cap products
have Haar mass at least m_delta^n_I. Hence

    0<p_h,       p_h >= m_delta^(750 n_I),
    -log p_h <=750 n_I log(1/m_delta).                  (C3b)

All these mandatory readers lie in the 81-block H_1 on the next block
graph: a radius-two displacement from an old block in v_0 reaches only
v_0 and its adjacent coarse blocks when L>=3. Thus one may choose H_1
as the one mandatory cell, with singleton cells elsewhere. The extracted
mass has zero original-source/terminal-V logarithmic variation and the
real conditional cell has TV=1. This is a volume-independent **Haar
reference** budget for this actual component. The weighted whole-history
mass includes the action, kernels and all avoidance factors, so (C3a)
does not estimate that different mass or D_h(0). The interaction test
below still fails despite this reference repair.

### 2.2 A conditional-cell expansion including complex measures — PROVEN implication

Here is a sufficient construction, with its cost in the required full
norm. Partition the ambient vertices into connected disjoint cells C.
Start from a product reference in the original integration coordinates.
Merge every overlapping mandatory support into one cell, enlarge to a
connected partition if needed, and leave the remaining vertices as
singletons. Let E_C collect the mandatory factors contained in C. For
fixed real product probabilities mu_C put

    p_C=int E_C dmu_C>0,       nu_C=E_C mu_C/p_C,
    P_h=product_C p_C,         nu_E=product_C nu_C.        (C4)

Empty mandatory lists have p_C=1. Product factorization gives exactly
p_h=P_h. For complex contour references use instead finite complex
measures mu_C(z), normalized to mass one, with fixed parameterization and
holomorphic densities with locally integrable envelopes. Any normalization
needed to obtain mass one goes separately in the full prefactor. Require
p_C(z)=int E_C dmu_C(z) nonzero
on D, and set nu_C(z)=E_C mu_C(z)/p_C(z). All measures/densities and
p_C must read only original z_C. Define

    tau_C=sup_D ||nu_C(z)||_TV >=1,
    tau(S)=product_(C subset S) tau_C,                    (C5)

where every support S is now a union of entire cells. In this complex
case the conditional integral is an algebraic normalization, not a
probability; its total variation is not set to one. Nonvanishing and
local logarithmic bounds for the p_C are input obligations, not a
consequence of writing (C4).

Close every interaction and residual-event reader support under the
partition, denoting the resulting connected support by S. Even an
interaction at a single vertex in a large cell carries that whole cell.
Include every remaining good-cut predicate chi_(k,Q), Q in B, in the
residual list as 1-zeta_(k,Q); include any further fixed-sector predicates
there too unless they were explicitly absorbed once into a cell reference.
Apply inclusion-exclusion to this list and the residual avoidance factors
of (C2).
For each overlap-connected collection J of distinct forbidden-event
labels put d_J=(-1)^|J| product_(i in J) b_i, with the union of their
closed supports S_J. Two such types are compatible when their supports
are disjoint. The unique overlap-component decomposition proves the
exact defect-gas identity; joint event masses are not products of their
one-event masses.

Require every mandatory and residual hard predicate to be fixed in the
analytic parameters z; a moving selector is outside this theorem unless
an exact holomorphic fixed-domain representation is separately supplied.
For an exact residual action sum U_S, require each U_S to be pointwise
holomorphic in its original z_S, measurable in the integration variables,
with the interaction and measure products locally dominated by integrable
envelopes. The same requirements apply to any substituted holomorphic
defect densities. Set f_S=exp(-U_S)-1. Define

    a_S=tau(S) sup_D,support |f_S|,
    delta_J=sup_D int |d_J| d product_(C subset S_J)|nu_C(z)|,
    q_C=sup_v [sum_(S contains v) e^(beta |S|) a_S
                +sum_(J:S_J contains v) e^(beta |S_J|) delta_J]. (C6)

If q_C<=1/4 uniformly on a fixed analytic domain D and the stated
locality/envelope hypotheses hold, then

    Z_C=int exp(-sum U_S) product_i(1-b_i) dnu_E
         =exp(sum_X F_X),             ||F||_mu<=q_C.      (C7)

The mandatory mass P_h sits outside Z_C. It is not a defect in (C6).

Proof of the nontrivial measure step: in any selected mixed collection,
defect types are disjoint unions of cells. Take absolute values and
remove each interaction by its supremum. Cells covered by a defect are
integrated in that defect's delta_J. Remaining visited cells cost tau_C;
each belongs to an interaction support, so the product of all tau(S)
over the interactions dominates their cost, since tau_C>=1. Unvisited
cells integrate to one **before** taking absolute values. This gives

    |int product f_S product_J d_J dnu_E|
                      <= product a_S product_J delta_J. (C8)

Disjoint closed supports involve disjoint cell measures, so their
integrals factor exactly, also for complex measures. Group selected
atoms by overlap components. Their union is connected and includes
every original parameter read. The first rooted-tree bound with weight
mu+1 uses v_i=e^((mu+1)|S_i|) times a_i or delta_i and the supersolution
T_i<=v_i e^|S_i|: its child sum is at most q_C |S_i|. Marking a root
vertex bounds the integrated gas at weight mu+1 by q_C. For its logarithm,
the alternating connected-graph sum is bounded by the spanning-tree
sum: ordering edges and partitioning by the Kruskal tree leaves intervals
whose alternating sum has modulus at most one. A second rooted-tree
bound spends the remaining unit of weight and gives ||F||_mu<=q_C.
Multiply each original interaction/defect atom by t. Both bounds converge
for |t|<=2 since 2q_C<=1/2; the finite connected identity near t=0
therefore continues to t=1. This proves (C7) and then zero-freeness.
Local uniform convergence and the envelopes prove holomorphy. No global
product of tau_C over untouched cells has been introduced.

This is the cell/complex-measure extension of RD R16's two-stage proof.
It is stronger than scalar normalization and is not asserted for an
arbitrary interacting reference. For fixed positive real cells tau_C=1.

Suppose the **complete** prefactor of D_h=P_h^full Z_C, including O_h^(-1),
has a specified logarithm p_const+sum_X p_X with ||p||_mu<=b_C,
where p_const is independent of all analytic parameters z. Then

    log[D_h(z)/D_h(0)]=sum_X K_X(z),
    K_X=p_X(z)-p_X(0)+F_X(z)-F_X(0),
    ||K||_mu<=2b_C+2q_C.                                (C9)

An unlocalized parameter-dependent scalar must remain separate; it cannot
be hidden in p_const. (C9) is after the integrations represented by Z_C.
If those do not include the remaining sea/terminal integration, (C9)
does not claim to estimate that later integral.

### 2.3 Probes of the actual and adapted references

**PROVEN technique failure for the direct conditional-Haar representation.**
Use (C4) for RD3's mandatory b_(0,Y_0), retaining the action and the
avoidance factors as the atoms above. On a sufficiently large torus
choose an original plaquette whose four links are outside the mandatory
reader cells. Their reference remains unrestricted Haar; chi_B in the
next quotient concerns U_1 and cannot restrict them. Set one of these
U_0 links to diag(-1,-1,1,...,1) and the others to identity. Then s=4/N.
The separately expanded Wilson atom at zero source satisfies

    ||e^(-u_0 s_p)-1||_infinity >= 1-e^(-4u_0/N),
    q_C >= e^beta (1-e^(-4u_0/N)) > 1/4
       if u_0 > -(N/4) log(1-e^(-beta)/4).               (C10)

An open neighbourhood gives the same supremum limit, so this also holds
for essential suprema. Closing supports under cells can only increase
the exponential weight. Other atoms add nonnegative terms to q_C.
This is an evaluated failure of (C6) in this exact, specified expansion,
not merely the failure of an upper bound to be small. Regrouping the
Wilson quadratic part into a Gaussian or interacting reference changes
the expansion and is not ruled out by (C10).

**PROVEN limit on the general conditioning inference.** On an m-vertex
connected path embedded in the block lattice let independent signs
s_i=+/-1 be fair, E={all signs equal}, and p=2^(1-m). After extracting p,

    E_(mu_E) exp(sum_i z_i s_i)=cosh(sum_i z_i),
    partial_(z_i) partial_(z_j) log Z(0)=1 (i!=j),
    Z(i pi/(2m),...,i pi/(2m))=0.                        (C11)

These follow by summing the two remaining configurations. The event can
be written as nearest-neighbour equality constraints, but they merge
into an m-site conditional cell. Thus extraction of an arbitrarily rare
mass, positivity, and tau=1 at real parameters do not alone give a
common product radius or small connected source correlations for
unbounded cells. This is a counterexample to that general inference,
not a Wilson/Decision-4 counterexample or a claim of zeros for RD3.

**ARGUED adapted reference.** Absorb the actual smooth action's quadratic
part and treat mandatory connected regions as cells. The selected-sector
FR/KR constructions are candidate suppliers. To use them here one must
prove that the pulled-back predicates are fixed on the analytic domain,
bound their conditional cell laws, and prove (C6) for the residual
interaction and all avoidance types. A globally dependent covariance or
background map requires its complete original-reader expansion before
assigning these supports. The source dependence of p_C and the inherited
terms still needs (C9)'s b_C. Replacing nu_E by the exact conditioned
interacting law makes the algebra trivial but leaves its connected
cumulants and complex zeros completely unestimated.

For example the actual positive-source derivative test remains
u_0^2 Cov_(nu_h)(s_p,s_q)=partial_p partial_q log D_h(0) (RD3 D21).
(C11) explains why a marginal price does not control this test. Passing
second derivatives would still not establish the all-order norm (C9).

## 3. Route L: large regions remain boundary data until integrated

### 3.1 Exact split and a matched-reference estimate — PROVEN

For a fixed real history open all variables in (4.1), split them into
x in its small-field complement and y in the large regions, collars and
other retained readers. Fubini gives the exact identity

    D_h(z)=O_h(z)^(-1) int d y W_h^out(y,z) S_h(y,z),
    S_h(y,z)=int d x W_h^in(x,y,z).                       (L1)

All factors are allocated once; any cross-boundary factor belongs to
W_h^in. A general joint indicator stays there if it reads both x and y.
The large fields y are boundary parameters during the small-field
integration. They are not inserted as normalized rare small atoms.
This identity is available with original Haar coordinates without a
chart or a contour deformation. It has no price or analyticity conclusion.

Suppose a small-field construction provides, on D_* and at each y,
a **matched** reference S_h^ref and local boundary logarithm G_h with
S_h=S_h^ref exp(G_h), after retaining any common bulk factors. The words
matched mean equality of all untouched measures, actions, cuts, gauge
maps and normalization factors. Terms whose actual readers touch a
large region remain in G_h, including its inactive/source-only terms.
For some actual reference integrand a_h^ref(y,z), write the resulting
integrated relative weight exactly as

    W_h^rel(z) = [int a_h^ref(y,z) L_h(y,z) exp(G_h(y,z)) dy]
                            / [int a_h^ref(y,z) dy],
    T_h(z) = int |a_h^ref(y,z)|dy / |int a_h^ref(y,z)dy|. (L2)

W_h^rel is a relative weight, distinct from RD3's unnormalized R_h.
This formula requires the denominator to be nonzero. It does not
equate that denominator with RD3's Z_A unless the displayed reference
actually is Z_A. L_h contains the large-region weight and every change
of reference not already allocated to G_h. It can be defined by a
density ratio where meaningful; obtaining a useful local bound is the
substantive next task.

If the large core has n blocks, its boundary reader set is Bdy_h, and

    |L_h| <= exp(-tau n+c_ref n),
    |G_h| <= b_partial |Bdy_h|,                           (L3)

uniformly over the same y,z, the triangle inequality proves, **after
the y integration**,

    |W_h^rel| <= T_h exp[-tau n+c_ref n+b_partial |Bdy_h|]. (L4)

The probability version for real positive a_h^ref has T_h=1. At complex
parameters T_h is essential. A price under a different reference law
does not prove (L3). A price only in average requires its joint
total-variation analogue with exp(G_h) inside, rather than a pointwise
interpretation of (L3).

A boundary logarithm can be obtained conditionally by comparing two
small-field expansions on the same product measure: if all atoms and
prefactor coefficients coincide away from Bdy_h and their norms are
at most q and b respectively, the connected series cancels coefficient
by coefficient off Bdy_h. Then its total absolute difference is at
most 2(q+b)|Bdy_h|. This is a proof of the input b_partial=2(q+b)
when that exact matching exists. Changing a reference cell measure
requires closing all its readers, as in (C5)–(C8); one cannot cancel
clusters only on the basis of their geometric location.

### 3.2 Price, entropy, contours and integration — PROVEN implication

Here is the quantitative cost ledger for a prospective regional
expansion. Suppose its **connected integrated region types**, not just
separate one-event marginals, have n>=1, full support size <=c_s n,
|Bdy_h|<=c_partial n and T_h<=exp(t_ref n). Any signed density is
estimated in total variation. Suppose their summed multiplicity at
each root and size n is at most A^n (or the same bound includes
nonnegative type coefficients).

If a positive raw kernel numerator has at most c_link n terminal
kernel readers, continuation V=W exp X with X Hermitian traceless,
||X||<=alpha costs at most

    exp[kappa u c_link (cosh(alpha)-1)n].                 (L5)

For completeness, writing A=W^(-1)M, ||A||<=1, its real exponent change
is (t/N) Re tr[(cosh X-I)A]. Since cosh X-I is positive semidefinite,
the change is <=t(cosh(alpha)-1). Multiply over kernels and integrate
absolute densities. This rebuilds LARGE55 KA at its reviewed raw-integral
scope. It supplies no denominator nonvanishing or signed cancellation.
If (L3) is already a complex-domain bound, omit (L5)'s debit to avoid
counting it twice; otherwise it belongs to the numerator continuation,
with all denominator/reference variation still in c_ref and t_ref.

Define the final price, after these debits, by

    nu_L = tau-c_ref-t_ref-c_partial b_partial
                  -kappa u c_link(cosh(alpha)-1),
    r_L = A exp(beta c_s-nu_L),
    q_L <= sum_(n>=1) r_L^n = r_L/(1-r_L),  r_L<1.       (L6)

This is a geometric-series estimate of a **full-root/full-support**
budget; boundary and inactive support sizes have already been paid.
It is uniform in volume only if all its inputs are uniform on the
same family. For a small-field interaction budget h_sf under a product
probability reference, its atom budget is at most e^(h_sf) h_sf. With a
complex reference require this bound after its TV factors have also been
paid. The sufficient mixed criterion is

    e^(h_sf) h_sf + r_L/(1-r_L) <= 1/4.                 (L7)

For example a preallocated small-field atom budget <=1/8 leaves the
condition r_L<=1/9, equivalently

    nu_L >= beta c_s + log A + log 9.                   (L8)

These thresholds are algebraic sufficient conditions, not measured
values for Yang–Mills. Their derivation uses no numerical experiment.

There is also an indispensable **gluing hypothesis**: the integrated
connected types must arise by exact overlap-component factorization
with local common references. A bound on each W_h^rel, or even a product
upper bound on all history probabilities, does not imply such a
factorization. If the regional construction supplies this identity and
the mixed majorant, expand small-field atoms together with regional
types, group connected overlaps and apply the two tree bounds proved
in section 2.2. It then gives a connected log with norm bounded by the
left side of (L7), after all regional integrations and the prescribed
history sum. This proves the conditional route and identifies exactly
where the joint reference input is used. It does not assume that a
list of scalar history prices is already a polymer gas.

### 3.3 Probes against the reviewed large-field machinery

**PROVEN price reservation.** If a real creation price is exp(-a u n)
but one-time normalization costs (C_0 u^d)^n, fix 0<a_eff<a. With
Delta=a-a_eff and d>0, differentiation of u^d exp(-Delta u) gives

    (C_0 u^d)^n exp(-a u n)
       <= [C_0 (d/(e Delta))^d]^n exp(-a_eff u n).        (L9)

For d=0 the bracket is C_0. Using a unchanged with a uniform constant
would require C_0 u^d bounded as u tends to infinity, which fails for
d>0. The new constant also enters A or c_ref in (L6), exactly once.
Thus the history cutoff must use the **final** price after all debits,
not the original action coefficient. In a scale sum with volume factor
L^(4r), per-level boundary cost L^(c_B r) and
u_(K-r)>=u_K+beta_- r log L-C, a fixed component size n is summable by
this bound only if n a_eff beta_->4+c_B. This is obtained by substituting
the lower bracket and summing its geometric ratio. It is sufficient
arithmetic, not an all-history theorem. Small completion-failed components
do not acquire a large size merely by being called frozen.

**PROVEN raw-cone scope.** In a forward-closed cone of Decision-4 kernels,
integrate free terminal outputs first: each kernel integrates to one.
Induct down the cone. The identity is valid only when the remaining
factor reads no removed variable. For a boundary insertion f reading
one such output, the same calculation gives int k(V;M)f(V)dV, not 1
or f at a chosen boundary value. For a fixed terminal field the first
integration cannot be made. This is precisely the reader condition of
LARGE55 COL, and is why (L2) is retained after the small-field expansion.

**OPEN actual price/reference budget.** Reviewed RLARGE is conditional at
SU(2), bad-only scope and needs future-tilt control under its stated law
(REVIEW_RLARGE_V3 S-1/S-2). LARGE55 MIS estimates a forward mismatch
tail, whereas RD3's required Y_0 is a size-failed fine-curvature component.
LARGE55 PRICE needs a consistent local action allocation with a boundary
debit; CODEX_REVIEW_LARGE F9 explicitly retains that requirement. Its
E13 retracts a zero boundary cost and leaves I5 argued. These statements
do not supply tau, c_ref, t_ref, b_partial, the connected multiplicities
or the gluing hypothesis for (L6) on the present all-cut reference.

For the concrete h, substitute RD3 RC1's actual real bound on Q_h=R_h/Z_A:

    Q_h(0,V) <= u_h m_delta^(-|E_1|)
                 exp(2u_1 P_(1,tot)+4t_1 |E_2|).         (L10)

Since u_h=exp(2t_0|E_1|) and m_delta<1, this upper majorant grows
exponentially with the surrounding volume at fixed core size two.
It cannot certify (L6) or a local boundary estimate uniform in volume.
Unlike (C10), this is a failing **sufficient upper bound**, not a lower
bound on Q_h or proof that a sharper price is impossible.

**ARGUED next construction.** Keep the complete small-field/boundary
cluster expansion under the same actual reference, attach each
cone-reading cluster to its original large region, and integrate the
resulting connected groups before taking their logarithm. A joint
total-variation price and reader/multiplicity estimate for those groups
would establish (L6)'s missing input. COL can remove only reader-free
remainders. This retains a possible Route L without assuming I5 or I6.

## 4. B3a: the required K after full integration, including holes

**PROVEN conditional norm transfer.** For Route C, (C9) gives the needed
unsaturated K only when its exact representation includes the whole
integration being compared. For two fully integrated matched objects
I and I_ref, with respective full prefactor/log bounds b,q and b_ref,q_ref,
their normalized ratio has

    K^ratio=K^I-K^ref,
    ||K^ratio||_mu <= 2(b+q+b_ref+q_ref).                (K1)

This is subtraction of constructed local logarithms. It is not an
interchange of logarithm with an integral. For the R8 comparison use
I=R_h, I_ref=Z_(k,A(h))^(cut,0) with its actual missing cuts. For the
terminal reference-weighted integral use the distinct A_h/Zbar_A of
RD3 RC3; apply an integrated theorem to those objects as well. A bound
for D_h alone does not prove either of these applications. If a
source-dependent normalization is divided out, subtract its full local
log and pay its norm too.

Let k_* denote the applicable right side of (C9) or (K1). For the actual
81-block hole, LIB1's map and RD3's direct geometry give

    ||K_inactive plus K'||_mu <= (1+297 exp(81mu)) k_*;
    alternatively <=730 ||K||_(649mu).                 (K2)

Recheck: saturation adds at most 81 vertices. An inactive root can be
charged to a vertex of the closed face-neighbourhood of the hole, whose
size is 3^4+8*3^3=297. An active output root already belongs to the input
support. Summing these rooted bounds and the unchanged inactive family
proves the first inequality. For the general bounded-hole conversion,
each input support meets at most 8|X| hole components of size <=81,
so its output has size <=649|X|; an inactive root has at most 9*81=729
input witnesses. Adding the inactive family proves the second.

For example a sufficient allocation certifying output budget k_out by
this estimate is

    2(b+q) <= k_out/(1+297 exp(81mu))                    (K3)

for a single normalized object; replace b+q by the four-term sum in
(K1) for its ratio. Smallness q<=1/4 alone does not imply (K3).

**OPEN actual input.** Neither probe above establishes b,q for the
fully integrated R_h and its different Z_A on D_*. Therefore (K2)
has no newly verified actual-model K input. This explicit limit is
part of the result, not a claim to close B3a by giving its desired norm
a name. With holes of size <=M the alternative cost is
(1+9M)||K||_((1+8M)mu). For growing/merged holes a uniform M is not
available from RD's recursion. In Route L a price still attached to an
**unnormalized** region can pay its full support in (L6). Once one
conditions on that region and divides by its mass, the same price
cannot pay (K2) a second time. Keeping unsaturated readers is a live
alternative only with an explicitly matching consumer norm.

## 5. B3b: quantitative closure and literal consumer accounting

An output must return to the input class, not just remain nonzero.
For a fixed invariant budget choice a sufficient closure would require
all of the following for every admissible child history:

    D_* subset next-step analytic domain;
    b_(k+1)<=b_*,  q_(k+1)<=q_*<=1/4;
    k_(k+1),full<=k_*;
    nu_(L,k+1)>=beta c_s+log A+log 9
       when allocating 1/8 of the next atom budget to large regions;
    normalized numerator norm <= the specified return budget. (I1)

Here the next q must be computed from the **new** exact effective action,
conditional cells or regional groups, not copied from the previous one.
Typically relevant vacuum/quadratic terms are extracted and one needs
an actual bound such as

    ||irrelevant_output||_beta
          <= lambda ||irrelevant_input||_beta + B_generated,
    lambda<1,       B_generated <=(1-lambda) h_*.        (I2)

(I2) is an explicit missing estimate, not a derived recurrence: this
note constructs no extraction map or constants lambda,B_generated.
Neither the two tree expansions nor (K2) imply it. Repeatedly multiplying
by a hole factor >=1 is not an induction proof. Norm rates and source
radii also require an invariant choice rather than indefinite Cauchy
or saturation losses. The finite algebraic recursion RD R4 remains
exact but supplies none of (I1)/(I2).

The complete selected-chart dictionary is as follows. In RD3 D24 write

    D_h=A_sel Z_sel+E_comp+E_side,
    A_sel=c_N^n(2pi sigma^2)^(d/2) e^(-S_0)
                    det Q^(-1/2) N_chi,
    d=(N^2-1)n, sigma^2=N/u_k,
    Z_sel=int Theta_h exp(-U) dmu_p.                    (I3)

| Literal consumer item | Route C / Route L placement and outstanding match |
|---|---|
| CX-R (ID): P, exp(-S_0), det K^(-1/2), N_chi, Z_red | P is c_N^n(2pi sigma^2)^(d/2) with any declared reference division. In the generic identity Q is the chosen positive Gaussian matrix; identification with STEP55's actual slice Hessian still needs proof, and any mismatch stays in U. Conditioning adds P_h once; a regional split keeps unnormalized core/reference factors. The exact identity for the chosen chart remains required. |
| Every Jacobian, gauge and inherited factor exactly once | The permitted tree gauge has unit gauge volume. The chart Jacobian remains in U. J=rho_h/b_k occurs in the insertion or in S_eff, never both. O_h distinguishes D_h from the full conditional denominator. |
| Nonzero linear term | ell^T sigma C W and any quadratic mismatch remain in U unless the critical point belongs to the exact normalized action, including log N_t. Neither route deletes them by definition. |
| Product white cut and original sources | mu_p is STEP55's fixed white-noise product cut. C's merged conditional cells change that reference and must satisfy (C6); this is an alternative proved cluster criterion, not a literal instance of CX-R's unconditioned mu_p. L must prove the small-field identity uniformly in its retained boundary data. Original-reader supports cannot be replaced by locality in substituted backgrounds. |
| CX-R (FULL)/(VAR) | Main, determinant, cut and reference logarithms have their separate b budgets. If Lemma O applies, its determinant budget is q_dim b_op/[2(1-r_op)]; its symmetry, local operator expansion and r_op<1 are inputs. Only the reduced cluster term has CX-R's 2h norm (or (C7)'s q_C). |
| Complements and contour sides | Retain E=E_comp+E_side. A local expansion of Log(1+E/(A_sel Z_sel)) is still needed if using (I3). A scalar relative-error bound alone does not provide its local norm. L may instead include every complementary region in its proved joint expansion. |
| STEP55 NZ-ret, section 5.4 plus S9 | The prospective RD quotient is N_h/[A_sel Z_sel+E], with full Gaussian/main factors retained. Identifying it with NZ-ret's particular history and denominator on the same complex coarse domain remains OPEN. A bound for the positive raw numerator from KA is insufficient; the normalized numerator budget must also match. |
| Histories and cuts | RD H12/R2/R3's completion/size convention must be identified with the consumer's convention or carried as an explicit alternative. RD3's cut=1 and n=1 are not silently substituted for STEP55's chart and white cut or RLARGE's sigma histories. |

For the last missing numerator budget, if a local region X has an
**actually established**, compatible denominator representation
D=P exp(sum F), sum ||F||<=q|X|, and
sup_D |N/P|<=n_X, then

    sup_D |N/D| <= n_X exp(q|X|).                        (I4)

This follows by the exponential lower bound and shows precisely which
numerator/reference estimate is needed. If P contains the mandatory
mass, N/P must contain the same mass division; no rare-price credit
survives automatically. RD3 D7 is a large finite estimate and does not
supply n_X of the required size. Inactive or exterior supports extending
beyond X must also be included before using the displayed |X| bound.

## 6. Status by obligation, named inputs and next decisions

| Obligation | Route C | Route L |
|---|---|---|
| B2a: uniform common domain | **OPEN.** C7 proves it conditionally on fixed predicates, holomorphic local cells, nonzero p_C and C6 on that domain. C11 refutes deriving it from mass extraction alone. RD3 retains only its finite germ. | **OPEN.** L1 is exact at real data. L5 is a raw envelope; the matched small-field/reference denominator and new hard selectors still need a common domain. |
| B2b: reference, interaction and failure budgets | **OPEN for actual model. PROVEN partial construction:** C1–C8 extract mandatory mass, retain no-other-failure predicates and include local total variations; C3a/C3b give this component's actual local Haar mass. The direct Haar atom test C10 **fails**. Adapted-reference construction is **ARGUED**. | **OPEN for actual model. PROVEN conditional accounting:** L2–L9 retain Peierls price, reference/TV/boundary/contour costs, entropy and the reduced exponent. Matched connected gluing is **ARGUED**, with no supplied actual constants satisfying L7. |
| B3a: local comparison after complete integration and K norm | **OPEN for actual model. PROVEN implication:** C9/K1 construct K only after the specified full integration, then K2/K3 pay D22/D23's full hole cost. Actual b,q for R_h and Z_A are missing. | **OPEN.** L4 estimates a scalar integrated ratio conditionally; L6/L7 plus exact joint gluing would construct K. L10's actual available majorant fails to certify this; a scalar ratio alone supplies no K. |
| B3b: invariant output estimates and STEP55/CX-R match | **OPEN.** I3 preserves the literal factors; the conditional-cell reference is not automatically STEP55's white cut. I1/I2/I4 and growing-hole control are unproved. | **OPEN.** Boundary-free raw kernels integrate, but reference readers and small completion-failed components remain. I1/I2/I4, price-preserving history sum and literal history/chart match are unproved. |

The required supplier outputs, without duplicating the coordinator lanes,
are: **FR** for fixed original-source and required coarse domains of the
actual selected or fixed-sector maps (plus the extension to these history
predicates); **KR** for the full allocated interaction and local prefactor
budgets on that domain (including inherited terms, not just a single
kernel remainder); **TC** for joint failures/regions under exactly the
chosen reference, with its exterior costs and complex total variation.
HANDOFF's reviewed selected-sector and original-law outputs are useful
at their stated scope. They do not by themselves prove these stronger
all-history interfaces. The related source-sea result is explicitly
coarse-integrated and leaves fixed-V connected logarithms open.

Next decision for C: build the conditioned covariance/background/reader
representation for C1's actual mandatory component while expanding its
avoidance types; attempt C6 with full cells and all prefactors. Next
decision for L: construct the common-reference boundary groups of L2
with a joint TV price and exact factorization, then evaluate L6 rather
than assuming a zero shadow cost. Neither proposal is a newly adopted
physical premise. Failure of C10 does not select L as proven; both
remain live. The terminal interfaces are of comparable, partly
overlapping strength to B2/B3, not minor lemmas or independent walls.

## 7. No-go discipline scope check

**N1 — real routes.** Two author-requested families were attempted:
conditional mandatory-event references, and action-priced large-region
boundaries. The direct Haar instance was tested within C, not counted
as a third independent family. Smooth partitions, conditional-cumulant
methods and a differently matched consumer norm remain untested options.
No five-family exhaustion or no-go packet PASS is claimed.

**N2 — dependence.** B2a/B2b can be obtained together from a matched
local expansion; B3a additionally integrates the correct reference;
B3b includes their reestablishment on the output. None of the six
pairwise relations is asserted independent: for pairs (a,b), (a,3a),
(b,3a), implications in either direction are unresolved at actual-model
scope; B3b explicitly requires a,b,3a on the next input class, while
their one-step versions do not here establish B3b. Thus there is no
independent-obstruction count.

**N3 — explicit assumptions.** Product/cell factorization, original-reader
closure, p_C nonvanishing, contour envelopes and tau_C, actual matched
references, joint regional gluing, price/entropy constants, admissible
charts and next-step norm contracts are all stated inputs to implications.
The actual-model instances remain OPEN. No small inherited action,
positivity of a signed activity or invisible boundary term is assumed.

**N4 — residual matches.** RD3 D16 attacks normalized mandatory-species
smallness; C3 removes that representation, so it is not evidence against
C. CODEX_REVIEW_LARGE F2/F9 attacks raw-cone/reference identification and
unspent creation prices; L2/L9 retain exactly those costs. LIB1 L23
attacks unrestricted full-support saturation, not the truth of a
price-weighted regional expansion. No mismatched prior no-go is used.

**N5 — scope.** C10 is one separately expanded Wilson atom under the
specified conditional Haar reference. C11 is a finite-sign-law
non-implication. L9 diagnoses reusing an exponent after a polynomial
cost. L10 diagnoses an extensive upper estimate. None is an actual-model
complex-zero theorem, an impossibility of alternative references or a
physical continuum/mass-gap statement.

**N6 — partial closure.** Extracting mass, retaining boundary fields,
changing a mathematical reference and reconciling support norms require
proofs and consumer matching, not new physical axioms. The registered
scale-reference, kinetic-isotropy and realized-state primitives are not
misclassified as missing analytic estimates or used to supply them.

**N7 — strongest counter-route to a negative conclusion.** An adapted
Gaussian/conditional reference could remove C10's order-one Wilson atom
while a reader-local small-field expansion groups cone-reading terms
with each charged large region. A proved joint TV comparison could then
pay L6's full support and connect C's local cell analysis with L's
history sum. RD's exact identities and the scoped selected-sector inputs
leave this possible. The missing proof is its actual matched conditional
interaction/reference estimate and stable next-step closure, not an
argument that rare events cannot be conditioned on.

**N8 — recovery.** This extends RD3's finite results without promoting
them. C1–C10 and L2–L9 specify concrete operations and debits; unchanged
RD/RD3 and their reviews remain recovery sources. No existing result is
deleted, no retained/audit status changes, and no process prompt is edited.

```yaml
actual_current_surface_status: open
target_claim_type: positive_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Both requested routes probed; exact mandatory-history factorization, conditional TV cell expansion and integrated regional price ledger proved; actual uniform B2/B3 and quantitative induction remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

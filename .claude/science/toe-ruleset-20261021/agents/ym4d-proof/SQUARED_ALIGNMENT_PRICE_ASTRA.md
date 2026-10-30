# Recovered linear threshold and an actual bare-step energy allocation

**Author proposal; fresh independent review required.** The squared alignment
inequality is already CS10, and the exact linear threshold below is already
proved in REVIEW55_ARS r55a-F10. This note recovers those results at JMBRB's
current interface and writes an explicit all-compact, simultaneous
coarse-curvature energy allocation with complete finite readers. It makes no
novelty claim for the alignment lemma or the linear threshold.

For the displayed original Wilson action and actual normalized paired kernel,
every prescribed set of coarse plaquettes with defect at least epsilon has
a raw joint energy budget proportional to `u epsilon^2` per label. On the
smooth-input branch there is also the ordinary forward kernel probability
bound. On the rough-input branch the budget belongs to the fine Wilson action.
Neither statement estimates the remaining integral relative to the actual
all-cut/history reference or proves a new price at later effective levels.
Full SU(N), d=4 existence and the physical continuum mass gap remain OPEN.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Bałaban and Dimock are credited for the large-field organization and the
normalization problem motivating this lane. Every mathematical step used here
is rebuilt below. The precise prior results are [CS8--CS14](CUT_SECTOR_COERCIVITY_ASTRA.md),
[OC1--OC3](OUTSIDE_CHART_RETURN_ASTRA.md),
[CODEX_REVIEW_KN F4](CODEX_REVIEW_KN.md), and
[REVIEW55_ARS r55a-F10](REVIEW55_ARS.md). The last already gives exactly
`min{epsilon/(2L^2),epsilon/(32 sqrt(N) A_L)}` and gap
`epsilon^2/(256N)`. [JMBRB B13--B18](JMBRB.md) uses the older, weaker trace-error estimate;
its statement about that particular estimate remains correct. Its quartic
bare threshold is not the best available bound on this one-step interface.

## 1. Supplied model, actual words, and all normalizers

Fix integers N>=2, odd L>=3, a coarse torus `(Z/TZ)^4` with T>=2, and the
fine torus `(Z/(LT)Z)^4`. Write h=(L-1)/2 and
`B_X=LX+{-h,...,h}^4`, with root LX. A positive link is labelled by its
starting site and direction. A plaquette is labelled by its starting site
and the ordered pair mu<nu. Every such unoriented geometric label is counted
once; inverse appearances in words do not introduce a second action term.
At T=2, different positive coarse-link labels remain different even when
their endpoint sets coincide.

Let U and V be arbitrary fine and coarse SU(N) link fields. For a positive
coarse link c=(X,mu), S_c(U) is the length-L straight root transporter.
For tau=(sigma,y), where sigma ranges over the 24 coordinate orders and
y ranges over B_X, let T_(c,tau) be the root-to-y axial path, the positive
length-L mu leg, and the inverse of the translated axial path at the other
endpoint. The SAME order sigma is used at both ends. These are the actual
Decision-4 transporters, and

    M_c=(24L^4)^(-1) sum_tau T_(c,tau),   ||M_c||op<=1.
    <A,B>_n=Re tr(A^* B)/N,   |A|_n=||A||HS/sqrt(N),
    s(Q)=1-Re tr(Q)/N=|I-Q|_n^2/2,
    h_M(Q)=<Q,M>_n,   m(M)=max_(Q in SU(N)) h_M(Q),
    psi_M(V)=m(M)-h_M(V)>=0.                              (SAP1)

No logarithmic or polar map replaces M_c. The kernel is well defined on all
compact fields, including singular means. For u>=1,
`0<kappa_-<=kappa<=kappa_+`, t=kappa u, and real original Wilson sources
`|e_p|<=rho<1`, the exact density is

    w_e(U,V)=exp[-u sum_p(1+e_p)s(U_p)] product_c k_t(V_c;M_c),
    k_t(V;M)=exp[-t psi_M(V)]/Ntilde_t(M),
    Ntilde_t(M)=int_SU(N) exp[-t psi_M(Q)]dQ,
    E^e=sum_p(1+e_p)s(U_p)+kappa sum_c psi_(M_c)(V_c),
    w_e=exp[-u E^e] product_c Ntilde_t(M_c)^(-1).           (SAP2)

All Haar measures are probability Haar. This uses the displayed JMBRB/CS
Wilson-coefficient convention u; no additional 2N is absorbed silently.
The identification t=kappa u is supplied model data. The proof does not
identify this u with a differently normalized bare coefficient elsewhere.
Original interior cuts, if present, multiply SAP2 unchanged.

Indeed the original kernel with numerator `exp[-t(1-h_M(V))]` has normalizer
`exp[-t(1-m(M))] Ntilde_t(M)`. Cancellation of the identical prefactors gives
SAP2 exactly. Every remaining field-dependent Ntilde is retained. E^e is a
nonnegative centered energy, not the complete finite-u negative log density.
No gauge fixing is needed here. The argument is gauge covariant, and the
fine/coarse fields and all their winding modes remain in the actual model.

## 2. Rebuilding the existing squared alignment inequality

Let M=sum_i lambda_i T_i be a finite convex average, where T_i belongs to SU(N), lambda_i>=0 and
sum_i lambda_i=1. For any S,V in SU(N), set
`d=|V-S|_n` and `q=sum_i lambda_i |T_i-S|_n^2`.
Convexity of the squared Hilbert norm gives `|M-S|_n<=sqrt(q)`. Since S is
an admissible competitor for m(M), and |S|_n=|V|_n=1,

    psi_M(V)>=<S-V,M>_n
             =d^2/2+<S-V,M-S>_n
             >=d^2/2-d sqrt(q)
             >=d^2/4-q.                                 (SAP3)

The middle identity is the exact chord identity
`<S-V,S>_n=1-<V,S>_n=|V-S|_n^2/2`. The last inequality follows from
`(d/2-sqrt(q))^2>=0`. Thus the proposed inequality is true for every N,
without a unique maximizer or a lower singular-value bound. This is precisely
CS10 rearranged. Its useful intermediate form also says

    sqrt(q)<=d/4  implies  psi_M(V)>=d^2/4.                (SAP4)

Nothing asserts positive psi for arbitrary geometric roughness at fixed
rough input; the right side of SAP3 can be nonpositive.

## 3. Actual ribbon fillings and complete one-step readers

For c=(X,mu), let B(c) be the lifted rectangular brick containing B_X,
B_(X+mu), and their single labelled common face. It contains only edges and
plaquettes inside this lift. At T=2 the extra far periodic seam of the
torus-induced graph is excluded. Every T_(c,tau) and S_c lies in B(c).

Move the length-L mu leg successively through the axial path from the root
to y. If that path step is parallel to mu, the resulting rectangle is a
backtracking word and cancels. A transverse step gives a 1-by-L rectangle,
which is an ordered product of L conjugated elementary plaquette holonomies
or their inverses. This elementary identity follows by inserting the common
edge transporter and its inverse between adjacent plaquettes; internal edges
cancel, leaving the rectangle boundary. Repeating the operation through the
axial path gives T_(c,tau) S_c^(-1) as a product of such conjugated plaquettes.
The axial path has at most 3h transverse steps. Therefore the total number
of attached plaquettes, with multiplicity, is at most

    A_L=3L(L-1)/2.                                        (SAP5)

All these faces stay inside B(c). The construction holds for negative axial
steps and for labelled paths crossing a periodic seam. It proves JMBRB B13
on the actual paired family; no commuting of matrix holonomies is used.

Choose this filling for every tau, write n_(c,tau,p) for the multiplicity
of p, and put `a_(c,p)=(24L^4)^(-1)sum_tau n_(c,tau,p)`. Then
`sum_p a_(c,p)<=A_L`, with support inside B(c). For any product of q unitaries,
telescoping in a unitarily invariant norm and Cauchy--Schwarz give
`|product_j Q_j-I|_n^2<=q sum_j |Q_j-I|_n^2`. The empty product has zero
defect. Thus, defining q_c on the ACTUAL transporter family,

    q_c=(24L^4)^(-1)sum_tau |T_(c,tau)-S_c|_n^2
        <=2 A_L sum_p a_(c,p)s(U_p)
        <=2 A_L^2 sum_(p in B(c))s(U_p),
    |V_c-S_c|_n^2<=4psi_c+4q_c
        <=4psi_c+8 A_L^2 sum_(p in B(c))s(U_p).             (SAP6)

Here and below `psi_c=psi_(M_c)(V_c)`. Under `||I-U_p||op<=eta` on the
brick, direct telescoping also gives
`||T_(c,tau)-S_c||op<=A_L eta`, hence `q_c<=A_L^2 eta^2`.
The conversion is `|A|_n<=||A||op`, so there is no missing sqrt(N).

For a coarse plaquette P based at X with directions mu<nu, let Sigma(P)
be its positive L-by-L fine square through the four roots. Successive row
attachments give its boundary S_P as a product of L^2 conjugated fine
plaquette holonomies. Define the following sets of ORIGINAL labels:

    C(P)=the four positive coarse-link labels on boundary P,
    F(P)=Sigma(P) union union_(c in C(P)) {fine plaquettes in B(c)},
    R(P)={X,X+mu,X+nu,X+mu+nu}.                            (SAP7)

F(P) conservatively includes every ribbon, not only plaquettes that happen
to survive cancellations. Retain every fine link occurring in its plaquettes
or in the complete words of the kernels C(P); retain the source e_p for
every p in F(P) and coarse data V_c for every c in C(P). The corresponding
normalizers read exactly those same complete means.

All these fine links and vertices lie in the four blocks R(P). For a finite
set A of distinct coarse plaquette labels, let F_A,C_A,R_A be their unions.
Then the complete reader bounds are

    |R_A|<=4|A|,  |C_A|<=4|A|,
    |F_A|<=24L^4|A|,
    number of original positive fine-link readers<=16L^4|A|. (SAP8)

To see the last two bounds, assign each fine positive plaquette or link to
its starting fine vertex. Each vertex owns six plaquettes and four links,
and the union has at most 4L^4|A| vertices. These bounds are on readers,
not a count of integration variables or an independence assumption. A hole
has not been filled into R_A by a diameter convention. If a later history
reads extra variables, those extra readers must be added by that consumer.

The incidence constants needed below are also explicit:

* A fine plaquette belongs to at most ONE Sigma(P). For its orientation
  mu<nu, its two transverse coordinates must be roots, and its two in-plane
  base coordinates lie in unique half-open intervals `[LX,LX+L)` modulo LT.
  This determines P. Projecting the labelled squares therefore creates no
  multiple coverage, including T=2.
* A positive coarse link belongs to SIX distinct coarse plaquette labels:
  for each of the other three directions there are two base choices. They
  remain distinct at T=2.
* A fine plaquette belongs to at most EIGHT labelled bricks B(c). If it is
  internal to a block, the only possibilities are the eight incoming/outgoing
  coarse faces incident to that block. If it crosses exactly one block face,
  only that labelled brick contains it. If it crosses two block faces, no
  two-block brick contains it. Opposite faces at T=2 have different labels;
  deleting the far seam in each lift is essential to this count.

Consequently one original fine plaquette can lie in F(P) for at most
`1+6*8=49` coarse plaquette labels. All repetitions inside the ribbon
fillings were already paid in A_L and a_(c,p).

## 4. The recovered linear dichotomy and the ordinary forward law

For 0<epsilon<=2 define

    gamma_NL=min{1/(2L^2),1/(32 sqrt(N) A_L)},
    eta_lin=gamma_NL epsilon,
    a_epsilon=epsilon^2/(256N).                            (SAP9)

Suppose `||I-V_P||op>=epsilon`. Either a fine plaquette p in F(P) has
`||I-U_p||op>=eta_lin`, or every such plaquette is strictly below eta_lin.
In the latter case the square filling and telescoping the four link
replacements imply

    epsilon<=||I-V_P||op
       <=||I-S_P||op+sum_(c in C(P))||V_c-S_c||op
       <L^2 eta_lin+sum_(c in C(P))||V_c-S_c||op.

Since L^2 eta_lin<=epsilon/2, some link has
`||V_c-S_c||op>epsilon/8`. For this link
`d_c=|V_c-S_c|_n>epsilon/(8 sqrt(N))` and
`sqrt(q_c)<=A_L eta_lin<=epsilon/(32 sqrt(N))<d_c/4`.
SAP4 gives `psi_c>a_epsilon`. In particular the weaker requested gap
`epsilon^2/(512N)` holds. If every fine defect is only <=eta_lin, the same
argument with non-strict comparisons gives `psi_c>=a_epsilon`.

The rough branch has the distinct original Wilson charge

    u(1+e_p)s(U_p)>=u(1-rho)eta_lin^2/(2N)
                   =[(1-rho)gamma_NL^2/(2N)]u epsilon^2.  (SAP10)

This is a pointwise action allocation on the original input. It is not a
conditional kernel probability for that fixed input. In particular an
interior-cut condition alone need not control all of F(P); the missing
crossing, square and ribbon readers must not be omitted.

For completeness, rebuild LF11/B11's normalization. Let D_amb=2N^2. A
matrix-entry grid of side r/(2N) covers SU(N) by at most
`(1+4N/r)^D_amb` occupied cells, each of HS diameter <=r/sqrt(2). Choose a
group representative in each cell. The corresponding operator r-balls cover
the group and have equal Haar mass, proving
`Haar(ball_r)>=(1+4N/r)^(-D_amb)` for 0<r<=1. Trace duality and ||M||op<=1
give `|h_M(Q)-h_M(W)|<=||Q-W||op`. A radius-1/t ball about any actual
maximizer, for t>=1, therefore gives

    Ntilde_t(M)>=exp(-1)(1+4Nt)^(-D_amb),
    P_(k_t)(psi_M>=a)<=min{1,exp[1+D_amb log(1+4Nt)-ta]}.
                                                               (SAP11)

For t>=1, fix U that is eta_lin-small on F_A. Under the PLAIN forward product law
K(dV|U), simultaneous epsilon-badness of A assigns one witness in C(P) to
each P. There are at most 4^|A| assignments and each uses at least |A|/6
distinct links by the six-plaquette incidence. Conditional independence of
those output links, not of the plaquettes, proves

    P_K(all P in A bad | U)<=min{1,4^|A| p_gap^(|A|/6)},
    p_gap=min{1,exp[1+D_amb log(1+4Nt)-t a_epsilon]}.       (SAP12)

For epsilon(u)=u^((delta-1)/2), 0<delta<1, the available per-plaquette
exponent, once the gap exponent is positive, is exactly

    q_geo(u)=kappa u^delta/(1536N)
                 -[1+D_amb log(1+4N kappa u)]/6-log 4.    (SAP13)

Thus JMBRB B18's coefficient is preserved while the fine threshold becomes
linear. This exponent is positive for sufficiently large u. SAP10 is also of
order u^delta for every delta>0. No asymptotic
uniformity in N or L is claimed: N,L,rho,kappa_- are fixed. A future or
history tilt is not part of the product law used in SAP12.

## 5. Direct all-compact joint energy allocation

There is a useful deterministic version requiring no small fine fields and
no choice of rough versus gap witnesses. For every finite A, define

    E_A^e=sum_(p in F_A)(1+e_p)s(U_p)+kappa sum_(c in C_A)psi_c,
    C_F^SAP=10L^2+1920 A_L^2,   C_psi^SAP=120,
    c_SAP=min{(1-rho)/C_F^SAP,kappa_-/120}>0.               (SAP14)

The following inequality holds for ALL U,V:

    sum_(P in A)|I-V_P|_n^2
       <=C_F^SAP sum_(p in F_A)s(U_p)+120 sum_(c in C_A)psi_c,
    E_A^e>=c_SAP sum_(P in A)|I-V_P|_n^2.                 (SAP15)

Proof: put b_P=|I-S_P|_n and d_c=|V_c-S_c|_n. Square filling and the
five-term Cauchy--Schwarz inequality give

    b_P^2<=2L^2 sum_(p in Sigma(P))s(U_p),
    |I-V_P|_n^2 <=(b_P+sum_(c in C(P))d_c)^2
                 <=5b_P^2+5sum_(c in C(P))d_c^2
                 <=10L^2 sum_(p in Sigma(P))s(U_p)
                    +20sum_(c in C(P))psi_c
                    +40 A_L^2 sum_(c in C(P))sum_(p in B(c))s(U_p).
                                                               (SAP16)

The first line again telescopes an ordered product of L^2 conjugated
plaquettes; inverse occurrences preserve the normalized HS norm. Sum SAP16
over A. The square term has incidence one, each kernel gap has incidence at
most six, and each fine plaquette in the last double sum has incidence at
most 6*8=48. The coefficients are therefore
`10L^2+40*48 A_L^2` and `20*6`, exactly those in SAP14. Finally
`1+e_p>=1-rho`, `kappa>=kappa_-` and nonnegativity of every term prove the
second line of SAP15.

In particular, on the simultaneous coarse event
`B_A(epsilon)={||I-V_P||op>=epsilon for all P in A}`,

    E_A^e>=c_SAP epsilon^2 |A|/N,
    u E_A^e>= (c_SAP/N)u^delta |A|,
           epsilon=u^((delta-1)/2).                      (SAP17)

The only norm conversion in this last step is
`|I-V_P|_n^2>=||I-V_P||op^2/N`. Constants are intentionally conservative.
The result is simultaneous at one bare step, including overlapping labels;
it does not allocate the same fine action again on a later step. For A empty
all sums and charges vanish and every assertion is trivial.

This is a direct composition of the existing compact alignment and actual
filling machinery. CS13--CS14 previously charge prescribed fine-curvature
and link-mismatch labels; SAP15 writes the coarse-plaquette consumer with
its square, brick and link incidences. It is not a claim that a new alignment
principle or a new physical model has been found.

## 6. Exact allocation keeps every original factor and leaves a real gap

For fixed A and any 0<theta<1, define the explicit remaining integrand

    R_(A,theta)^e(U,V)
       =exp[-u(E^e-theta E_A^e)] product_c Ntilde_t(M_c)^(-1).

Every Wilson numerator on F_A and centered kernel numerator on C_A retains
the fraction 1-theta of its original exponent; every numerator outside
those sets is unchanged. Every original Ntilde_t remains, at the ORIGINAL
t=kappa u. In particular this is not a normalized kernel with coupling
(1-theta)t: its normalizer has not been changed to Ntilde_((1-theta)t).
Exact factor splitting and SAP17 give

    1_(B_A) w_e
       =1_(B_A) exp[-theta u E_A^e] R_(A,theta)^e
       <=exp[-theta c_SAP u epsilon^2 |A|/N] R_(A,theta)^e. (SAP18)

Taking theta=1/2 is one fixed allocation retaining half of every charged
energy term. No probability estimate or lower-bound normalizer is needed
for SAP18. Any actual hard predicates and nonnegative measurable multiplier
H can be retained on BOTH sides and integrated over the same variables.
For complex original sources z with |z_p|<=rho, `|w_z|=w_(Re z)` and the
same raw envelope follows with |H|. This gives no complex normalized ratio.

The reader of the ratio `R_(A,theta)^e/w_e=exp(theta u E_A^e)` is contained
within the finite list SAP7--SAP8. The unchanged remainder of the original
integrand can still read the entire exterior. Thus a local density allocation
does not make its integrated remainder a local activity. If a consumer uses
several overlapping groups, it must allocate shared terms jointly or choose
fractions whose sum is at most one; SAP18 cannot be multiplied by charging
the same original term repeatedly.

For example, with any specified positive reference Z_ref, SAP18 gives only

    [int H chi 1_(B_A) w_e]/Z_ref
       <=exp[-theta c_SAP u epsilon^2 |A|/N]
                           [int H chi R_(A,theta)^e]/Z_ref. (SAP19)

Here H>=0 and chi contains the unchanged actual cuts. The second ratio is
UNESTIMATED. At fixed V, the event B_A is itself fixed; no claim of a small
conditional probability of that fixed coarse field is made. SAP19 is the
precise place a matched-reference construction must continue.

The next consumer is [LFPRICE section 6](LFPRICE.md), especially clause 2: construct and
estimate the joint remaining reference change, boundary insertions and
return factors relative to its actual all-cut denominator. It must include
the Ntilde factors, all original sources, any future/history tilt, and the
complete extended readers. Clauses 3--5 additionally require the appropriate
complex nonzero reference, integrated overlap expansion and next-step bounds.
SAP15 does not establish coercivity of the actual effective density obtained
after integration, and it supplies no Wilson representation for an inherited
effective action.

[RENEW R8--R15](RENEW.md) retains its full force: its actual rough flux orbit and open
tubes have persistent coarse roughness with no fresh priced kernel gap under
the plain forward law. The original creation charge R16 is paid once. Our
bare energy inequality charges that original rough input and is compatible
with that example; it neither supplies uniform renewal nor defeats RENEW's
quantified counterexample. RENEW-MATCH, full nonlinear RG control, continuum
existence and the physical gap remain OPEN.

[PROCESS_LIGHT](PROCESS_LIGHT.md) governs this unit. No scientific numerical
experiment is used. Only this note and `checks/squared_alignment_price_*`
are authored. The source is frozen before compact provenance metadata, then
handed to a different fresh reviewer. Author reconstruction and byte checks
are not independent review or audit.

# SRCREAL — real tilts and the separated all-order e hierarchy

Author sprint, 2026-10-30. **Conditional endpoint reached; actual RG inputs
remain open.** The literal cutoff-uniform MGF of the raw centered clover
observable is excluded in the reviewed flat-model scope. The proposed
replacement below uses positive real tilts of its **coarse conditional mean**,
plus bounds on all conditional insertion coefficients. It gives one E0′
triple

    s = 11,       beta = p + 3,       alpha = exp(C),

under the explicit outputs T, J and G below. Here p is the one factorial
growth exponent in G; C is constrained in Step 10. None of T, J or G is
asserted to follow from REALRGA's currently proved finite-jet algebra.
The argument does not construct a complex original-source neighborhood.

## Scope, status and recovery checkpoint

Only this file is an output. The 12 numbered steps are the status units:
**3 PROVEN, 6 DRAFTED, 3 GAP.** A step's label covers its displayed argument
and subcalculations. Definitions, receipts and the final interface table are
bookkeeping, not additional proof steps. DRAFTED means an author argument,
without independent review, even where it repeats a familiar calculation.

PROVEN(file) means the exact reviewed/admitted branch implication used here,
as defined in AUDIT.md's “meaning of status”; it does not mean a mainline
landing, retained audit grade, or verification of its hypotheses for YM.
The required lane files are absent from the cached origin/main tree.
REVIEW_REALONLY.md and REVIEW_REALRGA.md bind the current source hashes and
give LAND only at their conditional scopes. The REC_CONT review addendum
binds its current hash. No status is promoted by this note.

Worktree: `claude/q-S5`, HEAD
`b2c26b9a80785aab0b2538971b943f7235835107`.
Cached origin/main: `bcab5d2ee4a908fbb4e6025635fb878e6c157ebe`.
Cached planning ref: `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`.
Remote freshness is unverified; no fetch or Git mutation is performed.
SCIENCE_WORKFLOW and the repository physics-loop procedure govern the
proof discipline; the explicit author brief limits outputs and excludes a
new review, campaign, commit, audit or ledger operation. No editable prompt
file, platform instruction, physical axiom or primitive is changed.

Recovery state: the proof below is complete **conditional on T/J/G**. The
next actual scientific decision is whether a matched positive coarse-law
estimate T and a singleton-inclusive, separated marked-jet estimate J can
be proved with G's common growth constants. Do not restart with the raw
same-test MGF, omit conditional means, or replace a joint product bound by
individual exponential-regulator prices. E1/E2 on the resulting hierarchy
remain additional inputs to the continuation theorem.

Conventions: the supplied finite periodic Wilson SU(N) model, N>=2, and
normalized soft RG kernels are mathematical premises, not deductions from
foundation axioms. Use one fixed odd blocking factor L>=3, lattice spacing
0<a<=1 and the same prescribed cutoff/volume trajectory throughout. The
centered scalar is X_a(x)=e_a(x)-E e_a(x), with Z=1. Retain the reviewed
point bound |X_a(x)|<=C_X a^-4, C_X finite and independent of a and volume.
Points and tests lie in the interior isometric torus chart used by
OSLEAF55; compact supports are exhausted as the volume grows. Distances
below are Euclidean in that chart, not distances across a periodic seam.

## 1. PROVEN(REALONLY.md) — the literal raw tilt target has the wrong scope

**Consumes:** SRCCD55 Lemma V, including its corrected remainder, on its
specified even tori and weak-coupling/logarithmic trajectory; a fixed
nonzero real smooth compactly supported f; deterministic centering.

**Exact statements used** from REALONLY.md, “The clover/contact restriction”:

> Var O_a(f) >= c g_0^4 a^-4 (||f||_2^2-O_f(a)), c>0.

> This diverges along the stipulated logarithmic trajectory. Uniform R1
> for O_a(f)-c_a(f) would bound its variance by 2A p(f)^2/r^2, independently
> of deterministic centering. It therefore cannot hold in that scope.

And from the same paragraph:

> However, subtracting a nonlinear source counterterm from log Z does
> not generally leave a positive log-MGF.

**Produces:** the requested uniform two-sided MGF cannot be claimed for
the raw centered O_a(f) in that scope. This is the previously reviewed
restriction, not a new route-exhaustion result. It does not exclude bounds
for coarse conditional means, bounds with explicit separation-scale losses,
or other normalizations/geometries. A uniform bound conditional on every
coarse field for the *same raw variable* would still fail after averaging.
Positivity will therefore be used only for genuine laws, without nonlinear
contact subtraction. Review provenance: REVIEW_REALONLY.md items 1 and 3;
CODEX_REVIEW_SRCAN.md's variance and all-coarse corrections.

## 2. PROVEN(REALRGA.md) — what the real RG algebra actually supplies

**Consumes:** the actual normalized positive chain, with full history masses
and all sectors; original observable sources keeping every kernel and
normalizer fixed. Conditional statements apply only on admitted fibers.

**Exact statement used**, REALRGA.md §6, JETS:

> Carry the conditional original-source log
> Phi_j=log E[exp(sum z_i O_i)|U_j] and all its marked jets
> J_(j,B)=partial_B Phi_j(0;U_j).

> J_(j+1),B=sum_(pi partition B)
>                      kappa(J_j,C:C in pi | U_(j+1)).   (RGA19)

The section explicitly says:

> The output of H0–H5 is a real local finite-jet expansion. It is not by
> itself a matching theorem, a continuum limit or a symmetry proof.

**Produces:** an exact algebraic hierarchy, including singleton conditional
means. It supplies no estimate on its magnitude. HIER/RGA20 is an additional
OPEN all-order outer-cumulant hypothesis, not a consequence of the initial
q=4, field-order-six contract. This note does not assume HIER/RGA20 to
“derive” itself. Its alternative inputs T/J/G are stated below. Their
relationship to H2/RGA14, H3, H5 and H6 is part of the missing producer,
not another consequence of positivity. REVIEW_REALRGA.md confirms precisely
this split between algebra and actual-model estimates.

## 3. DRAFTED(high) — one positive law and exact insertion identities

**Most likely failure point:** using an RG sector or a different coarse law
in place of the complete normalized marginal stipulated here.

**Consumes:** Step 2's exact finite chain and a configuration of n>=2
distinct points with delta=min_(i<k)|x_i-x_k|>=c_* a, where c_*>=1 is fixed.
Put

    r_delta = min(delta,1),
    W(r) = min(r,1)^-4 [log(2+1/min(r,1))]^q,   q>=0 fixed.

Choose the largest available RG scale lambda=L^j a<=r_delta. The exact
chain is required to include scales up to this scale. Then
r_delta/L<lambda<=r_delta. One common j serves the whole configuration.
Let V=U_j and nu be its actual positive marginal, after all earlier
histories have been summed with their actual masses. If extra retained
data are used, specify the corresponding sigma-algebra and exact marginal
instead; every subsequent formula must use that same conditional law.

Define, with X_i=X_a(x_i),

    J_B(V) = kappa(X_i : i in B | V),        empty != B subset {1,...,n},
    Y_i(V) = J_{ {i} }(V) = E[X_i | V].                    (I)

These are finite conditional cumulants at each cutoff; boundedness of the
finite-lattice X_i suffices. In the finite ring z_i^2=0,

    E[ product_i (1+z_i X_i) | V ]
         = exp( sum_(B nonempty) J_B(V) product_(i in B) z_i ).

Extracting the coefficient of product_i z_i and then averaging proves

    E product_i X_i = sum_(pi partition [n]) E_nu product_(B in pi) J_B.
    E_nu Y_i = 0.                                        (II)

No complex analyticity or uniform source ball is used in this finite
identity. In particular, the product of conditional means alone would
drop every partition containing a nonsingleton block.

For lattice smearing, write ||f||_(1,a)=a^4 sum_x |f(x)| and

    e_j(f;V) = E[ a^4 sum_x f(x) X_a(x) | V ]
             = a^4 sum_x f(x) Y_x(V).                    (III)

This specifies the e observable to which the real tilt in Step 6 applies.
It is a coarse conditional image of the original field. Its linear tilt
nu(dV) exp(t e_j(f;V)) is not the pushforward of the original-source tilt:
the latter has density proportional to E[exp(t O_a(f))|V] and retains
all its conditional cumulants. Replacing these two densities by each other
would reintroduce Step 1's contradiction.

**Produces:** I–III under one positive law and one separation scale. Since
lambda>r_delta/L,

    W(lambda) <= C_Lq W(delta),
    C_Lq = L^4 (1+log(L)/log(3))^q.                       (IV)

Indeed 2+L/r<=L(2+1/r) for 0<r<=1, while log(2+1/r)>=log 3.
The use of the *global* minimum separation is deliberate. The estimate
below is weaker than R8's product of nearest-neighbor weights, but the
flat-test argument in Step 10 proves that it is sufficient.

## 4. GAP — output T: a positive terminal/coarse regulator price

**Consumes:** REALRGA H0/H2, RGA5's nonnegative owned energies, and a fully
matched RGA14-type reference, including exterior normalization and the
actual remaining coarse integration.

**Needed output T:** construct measurable nonnegative coarse control
functions E_(j,x)(V) and constants sigma>0, M_T>=1, independent of j,a,volume,
position and n, such that for the exact nu of Step 3,

    E_nu exp(sigma E_(j,x)) <= M_T.                      (T)

The functions must be explicitly identified by the producer, for example
by a bounded local collection of owned coarse energies if that collection
actually controls the marked coefficients in J. Merely calling an
unspecified function a regulator is not a construction. Put
H_x=1+E_(j,x). All H_x used in one product must be defined on the same nu.

The estimate must cover the full positive marginal, with large-field and
history contributions included, uniformly under translations. Conditional
bounds for each admitted history with the *same* sigma,M_T would suffice
after averaging; a statement on good histories alone does not. If a proof
uses several reference factors, T is a bound on their complete matched
normalized integral, not their separate numerators.

**Why the obvious approach fails:** RGA14 is a sufficient certificate for
integrated mixed jets when its joint regulator and differentiated-reference
bounds are supplied. It does not prove T under the outer coarse law.
Positive denominators and TV=1 do not give a uniform local exponential
price. A fixed small-field estimate, a bare Wilson denominator or a scalar
large-field probability does not control all the remaining conditional
amplitudes. T is an actual new RG obligation, not an evaluated constant.

## 5. GAP — output J: separated conditional insertions, including means

**Consumes:** the exact J_B of Step 3; the explicit H_x from T;
REALRGA's labelled real jets (RGA4), H3/H6's source terms and H5's complete
transition, with every source-dependent scalar and differentiated reference.

**Needed output J:** for each m>=1 a finite C_m, uniform in cutoff, volume,
translation, coarse scale and ambient n, such that for every nonempty
B subset [n], m=|B|,

    |J_B(V)| <= C_m W(lambda)^m product_(i in B) H_(x_i)(V)
               for nu-almost every V.                  (J)

For m=1 require this at every site and every admitted scale, including
the scales used in (III). For m>=2 use the configurations and common
scale in Step 3. Singleton means are not set to zero pointwise; only
their unconditional expectation vanishes. Bounds on individual atoms
must first be summed to obtain J for the exact conditional cumulant.
An empty-support source scalar contributes to J and cannot be discarded.

**Why the obvious approaches fail:** covariance telescoping and RGA19
are identities, not estimates. Separate one-insertion bounds do not bound
the higher conditional J_B. A real CD estimate supplies neither all mixed
derivatives nor their conditional large-field products. The q=4 contract
stops at four labels. A bound using only a fixed exponential regulator
exp(c m E) would require exponential moments at strengths growing with n;
T controls only strength sigma. J instead asks for polynomial degree one
in H per insertion, so Step 8 can pay higher powers by factorial moments.
No conversion of the existing exponential-regulator norm to J is proved.

J is deliberately a sufficient, potentially stronger output than necessary.
Failure to prove J would not rule out R9, SP_lambda, or other real routes.
It asserts no coincident-label derivative bound: the labels here occupy
distinct points in the separated regime. Repeated source derivatives at
one fixed point are outside J and are not licensed by its bookkeeping.

## 6. DRAFTED(high) — real MGF for the coarse e image

**Most likely failure point:** identifying the normalized coarse
conditional image with the raw observable.

**Consumes:** T, singleton J with C_1>0, exact E_nu Y_x=0, and any choice

    0<r<=sigma,       A=exp(r) M_T >=1.

Then E_nu exp(r H_x)<=A. Since |Y_x|<=C_1 W(lambda) H_x, put
Z_x=Y_x/[C_1 W(lambda)]. For every integer k>=0,

    E exp(r |Z_x|)<=A,     E |Z_x|^k <= A k! r^-k.

The exponential series is absolutely integrable for |u|<r. Its linear
term vanishes by centering. Thus, for |u|<=r/2,

    E exp(u Z_x)
      <= 1 + A sum_(k>=2) (|u|/r)^k
      <= exp( 2A u^2/r^2 ).                             (M1)

This gives the requested quadratic real MGF shape without importing a
uniform susceptibility theorem. Such a theorem could alternatively give
M1 by integrating the tilted variance twice, but it is not assumed here.

For real f!=0, let b_x=a^4 |f(x)|/||f||_(1,a). The b_x are nonnegative
and sum to one. Jensen's inequality applied pointwise to the finite convex sum
in (III), followed by (M1) with the sign of f(x), gives

    Q_lambda(f) = C_1 W(lambda) ||f||_(1,a),
    E_nu exp(t e_j(f))
       <= exp( 2A t^2 Q_lambda(f)^2/r^2 ),
    |t| Q_lambda(f) <= r/2.                             (M2)

The zero direction is identically zero. In particular, on Q_lambda(f)<=1,

    t_0=r/2,
    sup_(|t|<=t_0) E_nu exp(t e_j(f))
         <= exp( (A/2) Q_lambda(f)^2 ).                 (M3)

**Produces:** a genuine positive real tilt bound, uniform in cutoff and
volume with the displayed physical-scale norm and fixed normalized
t_0. At fixed lambda bounded away from zero this is cutoff-uniform for
bounded ||f||_(1,a). When lambda tracks a shrinking separation, W(lambda)
is retained explicitly. The bound does not have a radius uniform over
unnormalized arbitrarily large f. Nor does M2 alone control the fine-field
products: their missing conditional coefficients are exactly J.

## 7. GAP — output G: one factorial growth law for every order

**Consumes:** J's sequence C_m and the complete real RG transition at
all labelled orders, including localization, returns, field substitutions,
reference derivatives, large-field complements and source scalar terms.

**Needed output G:** one D>=max(1,C_1) and one p>=0, independent of m,n,
cutoff and volume, satisfying

    C_m <= D^m (m!)^p,            all m>=1.              (G)

The associated T, q, L and c_* must stay the same. Bounds separately for
each finite m with arbitrary constants do not give G. In REALRGA's
RGA17 notation, a proposed producer must also exhibit its actual invariant
budgets, for every required m, satisfying

    theta_m = lambda_m + B_m s_*m + eta_*m + C^RG_m M_m < 1,
    B_m e_*m <= (1-theta_m) M_m,
    x_(0,m) <= M_m,

and bound the resulting *full marked output* by G. Here C^RG_m is the
quadratic coefficient in RGA17, not the insertion constant C_m. Finite
invariance at each m does not bound growth of M_m or of the conversions
from that norm to J. Source-dependent substitutions may need more field
derivatives than order six; those derivatives must actually be carried.

**Why the obvious approach fails:** C_m=exp(m^2), for example, is finite
at every order but cannot satisfy G with finite D,p: m^2 dominates
m log D+p log(m!)<=m log D+p m log m. No finite four-source computation
or unevaluated all-order induction resolves this. No uniform numerical
RG tuple is invented here. G is separate from both a finite real radius
and a claim that all required orders exist algebraically.

## 8. DRAFTED(high) — mixed products and the complete moment hierarchy

**Most likely failure point:** changing the positive coarse law between
blocks of a partition, which would invalidate the common Hölder bound.

**Consumes:** I–II, T/J/G, IV, and the same fixed r,A as Step 6.
Since E exp(r H_i)<=A, positivity of the series gives
E H_i^n<=A n! r^-n. Generalized Hölder, with n equal exponents, yields

    E_nu product_(i=1)^n H_i <= A n! r^-n.              (P1)

This remains true with overlapping supports and with identical H_i;
it assumes no independence. For any partition pi of [n], J/G then give

    E_nu product_(B in pi) |J_B|
      <= D^n W(lambda)^n product_(B in pi)(|B|!)^p
                                   E_nu product_i H_i
      <= A (D/r)^n W(lambda)^n (n!)^(p+1).              (P2)

Here product_B |B|!<=n! because its quotient in n! is a multinomial
integer. There are at most n! partitions: map each block to the increasing
cycle on its elements, and obtain an injective map into permutations.
Using II, IV and A<=A^n proves

    |E product_i X_a(x_i)|
       <= A_0^n (n!)^(p+2) W(delta)^n,
    A_0 = A D C_Lq/r,           delta>=c_*a, n>=2.     (P3)

**Produces:** an unconditional separated point estimate with b_0=p+2,
including every product of conditional insertions and singleton means.
This directly estimates moments and does not need a separate estimate
of outer cumulants. At n=2, II reads E X_1 X_2=E(J_12+J_1 J_2); both
terms are present in P2. At every n, sum_B |B|=n ensures that each H_i
occurs once before Hölder; no partition silently spends an extra regulator.

No MGF of a product such as X_1...X_n is asserted. Arbitrary n means
arbitrarily many separated e insertions, not powers at a coincident point.
Other observables, including the larger OSLEAF dictionary, require their
own mixed J/G and scaling weights. They are not assigned e's dimension
four merely because there are finitely many labels.

## 9. DRAFTED(high) — source-order losses and compatible windows

**Most likely failure point:** interpreting a real derivative weight as
an actual original-source MGF interval.

**Consumes:** T/J/G and REALRGA's labelled source units. The target uses
distinct labelled derivatives at zero, so a weight rho_i=tau/W(lambda),
with tau>0, is only a norm convention. For m labels, J/G is equivalent to

    (product_(i in B) rho_i) |J_B| / product_(i in B) H_i
             <= (tau D)^m (m!)^p.                      (W1)

If an RG estimate has left side <=K_m, the exact conversion required
is K_m tau^-m<=D^m(m!)^p. A fixed tau can be absorbed into D. This
does not assert a source neighborhood in which repeated or coincident
derivatives are bounded. In particular it does not contradict Step 1.

An order-dependent tau_m=tau m^-v, v>=0, costs at most another v in p:

    m^(v m) <= exp(v m) (m!)^v,

because exp(m)>=m^m/m!. For example, if K_m<=K^m(m!)^p0,
one may take p=p0+v and D>=K exp(v)/tau. Faster losses must be audited
explicitly; they are not silently absorbed into a fixed factorial power.
This calculation uses each block's own order m. Any additional ambient-n
loss must be carried in P2, rather than hidden in the uniform C_m of J.
No step here obtains missing derivatives from values by finite differences.

For the regulator and real tilt, any positive sigma in T permits
r=min(1,sigma)/2, and then t_0=r/2>0. These choices satisfy r<=sigma,
are independent of n, and give finite A=exp(r)M_T. Thus T/J/G imply a
nonempty *consumer* window. If the producer uses an action reserve
sigma_av, it must actually satisfy

    sigma + sigma_other <= sigma_av,

with every reference, boundary, entropy and normalization debit included
in sigma_other. Neither sigma_av nor its strict remaining margin is
proved here. The RGA17 inequalities in Step 7 must hold simultaneously
with this reserve and W1 along one trajectory. Choosing a small r does
not fix a failed RG return or contraction margin.

**Produces:** explicit order and window accounting for P3. In particular,
separate bounds E exp(sigma E_i)<=M_T do not give E exp(sigma sum_i E_i)
<=M_T. The proof uses polynomial H_i and Hölder moments instead; it never
replaces the multiplicity of an overlapping exponential regulator by the
union of its supports. A bound separately at each tilt is not used as a
bound on E sup_t, either.

## 10. DRAFTED(high) — global-separation estimate to uniform E0′

**Most likely failure point:** applying the torus estimate outside the
interior Euclidean chart, where periodic distances require a new check.

**Consumes:** P3 with b_0=p+2>=0, the crude point bound C_X a^-4, fixed
q,c_*, and flat compact tests F on R^(4n). The seminorm is exactly

    |F|_k = max_(|gamma|<=k) sup_X
                     (1+|X|^2)^(k/2) |partial^gamma F(X)|.

Define S_n^(a,R)(F)=a^(4n) sum_(x_1,...,x_n) F(X) E product_i X_a(x_i),
with the sum restricted to the interior chart containing supp F. At a
coincidence F=0. For 0<delta<1 move a closest pair to its midpoint, giving
a point X^0 on a coincidence plane. The displacement has Euclidean norm
delta/sqrt(2) and l1 norm at most 2delta (only eight coordinates move).
Every point Z on that segment obeys

    1+|X|^2 <= 2(1+|Z|^2).

Indeed |X-Z|<=1/sqrt(2), and 1+|Z+(X-Z)|^2<=2+2|Z|^2.
Taylor's formula from X^0, using flatness to order M-1, therefore gives

    |F(X)| <= (2delta)^M/M! * 2^(5n/2) |F|_(M+5n)
                             product_i (1+|x_i|^2)^(-5/2).       (F1)

The product weight follows from
product_i(1+|z_i|^2)<= (1+sum_i |z_i|^2)^n; the segment comparison
is applied to the total squared norm before factoring. This avoids any
factor growing like n^(constant*n) in the displacement estimate.

Let C_lat be any fixed constant satisfying

    sup_(0<a<=1) a^4 sum_(x in a Z^4) (1+|x|^2)^(-5/2) <= C_lat.  (F2)

For a cube of side a centered at x, |y-x|<=a<=1 and
1+|y|^2<=3(1+|x|^2). Thus C_lat=3^(5/2) integral_R4
(1+|y|^2)^(-5/2) dy is one permissible finite choice. Restricting to the
torus chart only reduces this positive majorant.

Put C_q=sup_(0<d<=1) d[log(2+1/d)]^q<infinity. When c_*a<=1,
the three nonzero regions have the following bounds, obtained by F1/F2:

* delta>=1: W(delta)=(log 3)^q, and |F|_(5n) suffices. The coefficient
  is at most B_far^n(n!)^b0, B_far=A_0 (log 3)^q C_lat.
* c_*a<=delta<1: W(delta)^n<=C_q^n delta^(-5n). Set M=5n in F1
  and drop 1/M!<=1. The coefficient is at most B_sep^n(n!)^b0 with
  B_sep=A_0 C_q 2^(15/2) C_lat, at seminorm order 10n.
* 0<delta<c_*a: use the crude moment bound C_X^n a^(-4n) and M=4n+1.
  Then a^(-4n) delta^(4n+1)<=c_*^(4n+1) a. For n>=1 this region is
  bounded by a B_near^n |F|_(9n+1), where
  B_near=2 c_* C_X c_*^4 2^(13/2) C_lat.

The displayed B_near absorbs the one prefactor 2c_* into its nth power;
c_*>=1. If c_*a>1, a^-4<c_*^4, so the entire sum has the crude bound
B_coarse^n |F|_(5n), B_coarse=C_X c_*^4 C_lat. Thus one may choose

    C >= max(1, B_far+B_sep+B_near+B_coarse).            (F3)

All regions give, uniformly in a,R and n>=2,

    |S_n^(a,R)(F)| <= C^n (n!)^(p+2) |F|_(10n+1)
                   <= exp(C) (n!)^(p+3) |F|_(11n).     (E0)

The last inequality uses the nth term in exp(C), namely C^n<=exp(C)n!,
and 10n+1<=11n. Centering makes S_1=0, while S_0=1; alpha=exp(C)>=1
covers the normalized zeroth sector as well. No clustering or decay at
large distance is used: translation-uniform P3 and the integrable product
weight supply the required large-distance control.

**Produces:** the same s=11 and beta=p+3 for every n. This is a complete
adaptation of REALONLY's reviewed GROW argument to W(delta)^n. It does
not misidentify P3 with the stronger nearest-neighbor version of R8.
Near-collision control holds down to c_*a, with the remaining region paid
by the crude field bound; fixed positive separation alone would not suffice.
No shrinking-annulus loophole from CODEX_REVIEW_SRCAN is left in E0's
*conditional* hypotheses.

## 11. DRAFTED(high) — one common limit, with its precise limitations

**Most likely failure point:** failing to take one subsequence for the
complete hierarchy of tests.

**Consumes:** Step 10 on one sequence a_k->0, R_k->infinity, with all
T/J/G constants uniform on that sequence. At each fixed n choose a
countable dense subset of the compact flat test space in its induced
Schwartz topology; include rational linear combinations. Its completion
is the flat Schwartz space. Compact cutoffs approximate a flat Schwartz
test while preserving flatness. Separability follows by restricting the
second-countable topology of Schwartz space to this closed subspace.

The values on every one of these tests are bounded by E0 once its compact
support fits the chart. Successive subsequences and a diagonal selection
over the countable union for *all n* give convergence on that union.
For an arbitrary compact flat F and an approximating member F_l, E0
bounds uniformly

    |S_n^(a_k,R_k)(F-F_l)|
          <= exp(C)(n!)^(p+3) |F-F_l|_(11n).

Taking l large makes the sequence Cauchy on F, proves uniqueness of its
continuous extension for that chosen subsequence, and passes E0 to the
limit. The same bound extends the limiting functional to all flat
Schwartz tests. This proves a **common subsequential hierarchy**, not
uniqueness across subsequences or convergence of the entire trajectory.

**Produces:** S_0=1, S_1=0, reality, scalar permutation symmetry and E0′
with the same constants as E0. Reality and permutation symmetry pass
from the finite real scalar products by convergence on the same tests.
Full Euclidean rotational covariance E1 and reflection positivity E2 in
the exact OSLEAF test algebra still require their respective geometric
matching/limit arguments on this hierarchy. The current calculation
does not supply them, a nonzero witness, or a mass gap. In particular,
REALRGA's separate EUC/MATCH/FLOW obligations are not discharged by T/J/G.

## 12. PROVEN(REC_CONT.md) — exact downstream continuation interface

**Consumes:** the hierarchy of Step 11 **if it also satisfies full E1,
E2 and the other stated REC_CONT axioms on that same hierarchy**. The
scalar case has one component. No assertion that these remaining
actual-model assumptions have been established is made.

**Exact input statement used**, REC_CONT.md §1:

> |S_n(F)| ≤ alpha (n!)^beta ||F||_(sn),1,   n≥1,           (1.2)

> `s∈N`, `alpha,beta≥0` are a single triple for the entire hierarchy.
> The flat space consists of Schwartz tests whose every jet vanishes on every
> pair-coincidence plane. It is not the full Schwartz space. E1, E2, E3,
> ordinary component reality, and S_0=1 are retained. E4 is not assumed.

**Exact output statement used**, from the target quotation in that section:

> For each n and
> ordered label word a, there are holomorphic functions 𝒲_n^a on
>
>     𝒯_n={z∈C^(4n): Im(z_(j+1)−z_j)∈V_+, 1≤j<n},
>
> with 𝒲_0=1. Their restrictions to the Wick slice j(x_1),...,j(x_n)
> agree as distributions with S_n^a on compact tests with t_1<...<t_n.

Its output bound is exactly

> |𝒲_n^a(x+iy)| ≤ C_n(1+|x|+|y|)^B_n (1+d_n(y)^−1)^A_n,
> d_n(y)=min_(j<n){(y_(j+1)−y_j)^0−|(y_(j+1)−y_j)⃗|}.   (6.1)

The same source specifies n=1 is constant, common complex translation
invariance, d_1=1, and finite C_n,A_n,B_n independent of z and label word
but permitted to depend on n. Its continuation uses the hierarchy-wide
input triple, which is why G and the extra factorial in Step 10 are
load-bearing. The new coarse real tilts do not remove complex spacetime
from this downstream conclusion. Review identity: the final addendum in
checks/reccont2_review.md matches the REC_CONT hash recorded below.

## End-to-end interface and verification record

| Interface | Producer required or used | Exact consumer |
|---|---|---|
| Positive measure and exact conditional coefficients | Actual normalized chain, Step 2; algebra in Step 3 | Every expectation in T, M2 and P1–P3 uses the same nu |
| T | Actual outer/coarse exponential energy price; Step 4 GAP | Fixed r>0 and E exp(r H_i)<=A in Steps 6/8 |
| J | Actual separated conditional marked coefficients, including singletons; Step 5 GAP | Coarse MGF from C_1 and all products in P2 |
| G | Full coefficient growth C_m<=D^m(m!)^p; Step 7 GAP | Fixed p,D and the common exponent p+2 in P3 |
| M2 | Step 6, T + singleton J | Real coarse-e tilt; never substituted for the full fine hierarchy |
| P3 | Step 8, T/J/G + exact II | Global-separation bound down to c_*a in Step 10 |
| E0′ | Steps 10/11, crude point bound and common subsequence | s=11, beta=p+3, alpha=exp(C), C constrained by F3 |
| Continuation | Reviewed REC_CONT conditional theorem | E0′ plus E1/E2/E3/reality/S_0=1 on the same hierarchy |

Author verification: the complete new argument is checked end to end,
including the conditional-mean/raw-tilt distinction, all singleton terms,
partition and regulator multiplicities, scale-to-separation comparison,
Taylor derivative orders, volume exhaustion and n=0/1. The closest existing
arguments are REALONLY R-MOM/R8/R9 and OSLEAF GROW; the new conditional
interface is T/J/G with direct products and a global-separation weight.
This is not a novelty claim about exponential moments or the partition
formula. Source identities, labels, quotations and output scope are checked
deterministically. These are author/source checks, not independent review
or proof certification. No numerical experiment or test runner is needed
for these symbolic implications, and none is run.

The proposed RG inputs are not supplied by an external theorem. A primary
scope check of [Dimock's account of Balaban, II](https://arxiv.org/abs/1212.5562)
finds a scalar phi-four model in dimension three in its abstract. That
source is not used as a theorem for this four-dimensional gauge-law
insertion problem; only its abstract was checked here. No broader
literature-coverage or model-transfer claim is made.

The three weakest links are T's actual normalized coarse exponential
price, J's separated conditional insertions under that same law, and G's
uniform factorial growth after the complete RG transition. The first two
do not become estimates merely by naming them; the third is not implied
by proving any finite list of orders. Full E1/E2 remain distinct downstream
assumptions, rather than additional conclusions of the source bridge.

### Source identities

Required scientific inputs were read completely, including their relevant
corrections. Supplemental reviews were read at the reused theorem and
source-identity scopes. Source receipts below identify the revision used;
the cached refs above are not a claim of remote freshness.

| File | SHA-256 |
|---|---|
| REALONLY.md | `3856594faffe9b1c6beab42f38385c820f06ab7476c4cbdd6934b5bf30bac019` |
| SRCCD55.md | `80a347f5d2bc801fc0395b6d61aa5c0661dd098ae4430bcf760b874729761d03` |
| SRCAN55.md | `087c91361827dc41dbd4bb605d65f511009225d51fc5f9a88372bbf261febcad` |
| CODEX_REVIEW_SRCAN.md | `a3ec6ab90f36bbd567d9b4a739deb7e2f223b55c0fe5905ae8a1fe2a19a2ab52` |
| OSLEAF55.md | `c261a0c5eb300052445a05b3041b5ddf6e518445d3eacac36fc4421e60f66b78` |
| REC_CONT.md | `ac7ac0854fb320f183779f67be136063dfb750ee3f13b869acad10a7ac12a278` |
| REALRGA.md | `e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed` |
| AUDIT.md | `765abb796087032d950e0db436952c61bd08b100648fa55f2cedbe31a66c619e` |
| REVIEW_REALONLY.md | `2ab7111a8b5e433c3d215ce29de4ea9be8dc2d322c3654d6a8db60337d13bb3d` |
| REVIEW_REALRGA.md | `37f34b77fd487bc2eff8b3b624854cb636b8dd016c2e5d201a2a02a88fdac2d7` |
| checks/reccont2_review.md | `d5489fd797470a76479a4467beb844215489bc55a16dd34bf7a1d07d841e7b5c` |
| briefs_q/SRCREAL/AUTHOR.md | `9b06a1ec2f8a143d607f3f89e7f4147d0c19c7e7061b2efb71e02131e5fa6f0b` |

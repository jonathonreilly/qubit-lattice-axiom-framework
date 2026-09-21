---
claim_id: mobile_records_empty_start_motion_response_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "For the supplied finite permanent-record birth and reversible vacancy-hop model, initially empty, with six positive symmetric row-six pair weights: the first two birth-generator powers are stationary under motion, so the full law first can depend on mobility at time order four and a motion-conserved observable at order five. The leading population difference is kappa epsilon^4 D_2(b)t^5/60, where D_2 is the unnormalized two-record hazard Dirichlet energy. At fixed physical time the epsilon-four coefficient retains the entire motion semigroup and is nonnegative, increasing and concave in mobility. More generally, if m is the first occupied level with nonconstant motion-class hazard, the first actual population response is order epsilon^(m+2) with the stated positive semigroup integral; if no such level exists the empty-start law is independent of mobility. Unit-proposal cubic tori of side L>=6 have the stated explicit D_2 per volume, strictly positive for nonconstant W, with an explicit volume-uniform short-time remainder. Empty-start centered content correlations begin at adjacent sites at time order two. The finite-time epsilon remainder given here grows with volume; no finite-density closure, finite-epsilon all-time monotonicity, phase, force, physical clock or new axiom is claimed."
upstream_dependencies:
  - mobile_records_rare_formation_event_law_and_six_site_witness_bounded_theorem_note_2026-09-20
runner: scripts/mobile_records_empty_start_motion_response_2026_09_21.py
---

# Motion increases formation from an empty lattice at its first nonzero order

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** proposed_retained
**Author support:** conditional-support; no independent audit verdict.

The mechanism in the [preceding event-law note](MOBILE_RECORDS_RARE_FORMATION_EVENT_LAW_AND_SIX_SITE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-20.md)
allows a permanent record to leave a site and a new record to form there.
Starting entirely empty, neighboring contents become correlated before motion
changes the population. When motion first changes the expected population,
its contribution has a definite positive sign. It is controlled by how the
birth hazard varies along allowed two-record hops, rather than by an assumed
static ensemble or an initial seed bias.

The theorem also identifies when that first coefficient vanishes, how to find
the first actual coefficient, and how to retain the whole motion evolution
while expanding only in the formation intensity. A cubic-lattice calculation
and a conservative remainder show that the short-time density effect is not
just a small-window artifact. Neither bound controls the moderate-density
numerical experiments that motivated this question; those experiments are
not a claim of this note.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Does vacancy motion alter fresh formation from an empty lattice, and can its effect be distinguished from supplied initial ordering?"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Determine the lifetime of local activity and test finite-density response without replacing the growing ensemble by equilibrium."
conditional_surface_status: "Finite-generator identities, a positive first nonzero formation-intensity coefficient, a cubic geometry reduction, and a volume-uniform short-time bound."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Conditional proofs and independently checked exact finite-generator calculations; no physical identification or primitive adoption."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Supplied model and dependency status

The event-law note is a provisional, checked but unmerged dependency from
PR #8545 at `689941783bea870e08458e079ddb208257d0083d`. Its theorem and audit
status are not promoted here. The present proof restates the entire model it
needs and does not use the rare-birth limit as a finite-density law.

On a finite simple graph G with V vertices, a site is vacant (0) or holds one
of six immutable contents. A vacancy has bond weight one. For occupied
neighbors use a strictly positive symmetric six-by-six matrix W with row
sums six. The weight w(s) is the product of W over all occupied edges.
An occupied-vacant edge {x,y} exchanges its endpoints at rate
`kappa c_xy w(s')/[w(s)+w(s')]`, where c_xy>0 is a fixed symmetric proposal
intensity. At vacant x a record with content a forms at rate
`epsilon product_(occupied y~x) W_(a,s_y)`. Include the negative total exit
rate on each generator diagonal. There is no deletion, replacement, export,
or occupied-occupied exchange. The initial configuration is empty.

Here kappa,epsilon>=0 are supplied rates in an abstract time parameter. The
axiom memo does not select these rates, this stochastic evolution, or a
physical time conversion. Unit proposals and spatial geometry are imposed
only where stated. The row-six normalization is needed for the delayed-order
identities; arbitrary positive pair weights are not silently included.

Let H be the unscaled reversible vacancy-hop generator, B the unscaled birth
generator, and L=kappa H+epsilon B, acting on column observables. Row laws act
on the left. The graph is finite and simple, W is positive and symmetric with
every row sum six, and a vacancy has bond weight one. Let w(s) be the product
of occupied-edge weights, N(s) the number of records, b(s)=B N(s) the total
unscaled birth hazard, and delta_0 the initially empty law. The motion proposal
rates can vary across edges provided forward/reverse proposals are symmetric.

## 1. First two birth powers are invariant under motion

The only nonzero components of delta_0 B are its empty-state diagonal -6V
and coefficient one on each one-record configuration. They are stationary for
H, because a single record has w=1 and symmetric hops. Thus delta_0 B H=0.

Row normalization gives b(s)=6(V-1) on every one-record configuration: each
neighboring vacancy sums its single-neighbor weight to six, and each other
vacancy also has hazard six. Therefore delta_0 B^2 has components

```
N=0: 36 V^2,
N=1: -6(2V-1),
N=2: 2 w(s),
N>2: 0.
```

For N=2 the two insertion orders have the same product w(s). On every motion
communication class H is reversible for w. Each displayed stratum is therefore
stationary for H, even if a content-count sector is disconnected. Consequently
delta_0 B^2 H=0. No irreducibility or rare-birth limit is needed.

Successively multiplying on the right now gives the exact identities

```
delta_0 L   = epsilon delta_0 B,
delta_0 L^2 = epsilon^2 delta_0 B^2,
delta_0 L^3 = epsilon^3 delta_0 B^3,
delta_0 L^4 = epsilon^4 delta_0 B^4
                +kappa epsilon^3 delta_0 B^3 H.
```

Thus the full finite distribution agrees with the zero-motion process through
third order in physical time. A motion-conserved observable f, with Hf=0,
agrees through fourth order. This applies to total population and all functions
of the immutable content multiset. It does not assert equality at finite time.

## 2. First possible population correction has a definite sign

The N=3 component of delta_0 B^3 is 6w(s), since each of the six insertion
orders telescopes to w(s). The N=0 and N=1 components are constant within
their motion classes. The N=2 component is

```
-2 w(s) [6(2V-1)+b(s)].
```

Hence delta_0 B^3 H = -2 (w b on N=2) H. Let the unnormalized two-record
Dirichlet form be

```
D_2(b) = - sum_(s:N=2) w(s) b(s) (H b)(s)
       = (1/2) sum_(s,t:N=2) w(s) H(s,t) [b(t)-b(s)]^2 >= 0.
```

The equality uses detailed balance; the diagonal contributes zero. Expanding
one further derivative and using HN=0 gives

```
delta_0 L^5 N - epsilon^5 delta_0 B^5 N
 = kappa epsilon^4 delta_0 B^3 H B N
 = 2 kappa epsilon^4 D_2(b).
```

For each fixed finite model and fixed nonnegative kappa, epsilon, analyticity
of the finite matrix exponential proves

```
E_(kappa)[N_t] - E_(0)[N_t]
 = kappa epsilon^4 D_2(b) t^5 / 60 + O(t^6),  t -> 0.
```

If D_2(b)>0 and kappa,epsilon>0, motion increases expected population for all
sufficiently small positive times. This is the first nonzero coefficient in
that case, not a monotonicity theorem for later times. The coefficient vanishes
precisely when b is constant along all positive-rate motion edges in the
two-record strata. On W=1 it vanishes; the entire population process is already
independent of motion. The exact rational full-generator check gives D_2=14/5
on the three-site path and 224/5 on the four-cycle at raw (3,1,2), normalized
to W=(3/2,1/2,1). The same values occur for the opposite-content-favoring
(1/2,3/2,1) menu. Constant weights and complete two-/three-site graphs give
zero. Sixteen declared graph/menu cases are checked by the primary runner.

## 3. Two-record reduction to graph geometry

Write c_xy for the number of common neighbors of distinct occupied sites x,y,
and h_ab=(W^2)_ab-6. Every other vacant site's content sum is six unless it is
a common neighbor. Consequently

```
b(x,a;y,b)=6(V-2)+c_xy h_ab.
```

For each undirected proposed hop edge {x,x'}, spectator site y outside that
edge, and moving/fixed contents a,b, put u=W_ab if x is adjacent to y and
u=1 otherwise; put v=W_ab if x' is adjacent to y and v=1 otherwise. There is
one corresponding undirected two-record configuration edge. With unit proposal
rates its conductance is uv/(u+v), so

```
D_2(b)=sum_({x,x'} in E) sum_(y outside {x,x'}) sum_(a,b)
         [uv/(u+v)] h_ab^2 (c_x'y-c_xy)^2.
```

For a d-dimensional periodic hypercubic graph of side L>=6 this reduces to

```
D_2(b)/V = d sum_(a,b) h_ab^2 {
                 2(8d-7) W_ab/(1+W_ab) + (8d^2-14d+7) }.
```

To count it, fix a hop edge and one endpoint. Sites with a nonzero common-
neighbor count lie at graph distance two: 2d axial sites with c=1 and
2d(d-1) diagonal sites with c=2. Their total squared count is 2d(4d-3).
Among these, sites adjacent to the opposite endpoint contribute 1+8(d-1)
=8d-7. The rest contribute 8d^2-14d+7. The two endpoint families do not
overlap for L>=6. Combine the two sides with conductances W/(1+W) and 1/2,
then multiply by d edges per site. Small periodic sizes are excluded from this
count; their D_2 remains computable by the general graph formula.

In d=3 with W=(3/2,1/2,1), h_ab=(1/2) v_a dot v_b, so sum h_ab^2=3 and
sum h_ab^2 W_ab/(1+W_ab)=7/5. Thus D_2/V=2379/5 and the leading density
increment is `(793/100) kappa epsilon^4 t^5`.

For any nonconstant symmetric row-six W the displayed cube coefficient is
strictly positive. Indeed J denotes the all-ones matrix, A=W-J has AJ=JA=0,
and h=W^2-6J=A^2. Hence sum h_ab^2=tr(A^4)>0 whenever A!=0, and every
factor multiplying h_ab^2 in the cube formula is positive. This statement
does not require ferromagnetic contents or a positive vector eigenvalue.

## 4. A conservative remainder bound that is uniform in volume

For unit edge proposals, maximum degree z, u=max(1,max_ab W_ab), define
R_kappa=6 epsilon u^z+z kappa and K=2(z+1). Keep each local difference grouped
as `T_i f(s)=r_i(s)[f(s^i)-f(s)]`. A term is active only if its updated site
or sites intersect the observable's support; merely inspecting that support
through its rate does not make the term active. Each active term changes the
norm by at most twice its rate bound and adds at most K support sites. The
total rate bounds of terms updating support S sum to R_kappa |S| at most.
Apply this bound separately
to each term in the iterated expansion, rather than taking the union of all
possible supports. For a one-site observable f with ||f||_infinity<=1,

```
||L^k f||_infinity <= (2 R_kappa)^k product_(j=0 to k-1) (1+jK).
```

At each step an individual term's support has size at most 1+jK; summing the
norm bounds over its descendants proves the product estimate by induction.
The finite Markov semigroup contracts the supremum norm, so Taylor's integral
remainder through degree five is at most this k=6 bound times t^6/720.
Apply it to n_x in both the moving and immobile processes, then average sites.
With

```
C = [(2R_kappa)^6+(2R_0)^6] product_(j=0 to 5)(1+jK) / 720,
a = kappa epsilon^4 D_2/(60V),
```

the density difference satisfies `|rho_kappa(t)-rho_0(t)-a t^5| <= C t^6`.
The constants do not grow with V. On the above cube family with nonconstant W
and positive kappa,epsilon, a>0 is also volume independent; for 0<t<=a/(2C)
the density increase is at least a t^5/2 on every member of the family. This
bound is deliberately conservative and may certify only extremely short
times. It neither approximates the moderate-density runs nor proves a sign
for all times. It establishes that the startup effect is not caused solely
by a particular finite volume. An infinite-process construction is not needed
for this uniform finite-volume statement and is not claimed here.

## 5. Earliest spatial correlations do not require a supplied seed population

Let chi be centered with W chi=theta chi and nu=(1/6)sum_a chi(a)^2>0;
define chi(0)=0. Starting empty, for distinct sites x,y,

```
E[chi(s_x(t)) chi(s_y(t))]
 = 6 nu theta epsilon^2 t^2 1_(x adjacent y) + O(t^3).
```

At this order there must be two births. The two temporal orders cancel the
Taylor factor 1/2. On an edge the sum of their content products is
chi^T W chi=6nu theta; away from an edge the sum factorizes to zero. Motion
does not enter through this order, as proved above. At each site,

```
E[n_x(t)] = 6 epsilon t - 18 epsilon^2 t^2 + O(t^3),
E[chi(s_x(t))^2] = nu E[n_x(t)] + O(t^3).
```

For a nonzero fixed complex spatial vector u, F_u=sum_x u_x chi(s_x), the
normalized structure factor therefore obeys

```
E[|F_u|^2] / (nu E[sum_x |u_x|^2 n_x])
 = 1 + epsilon theta t (u^* A u)/(u^*u) + O(t^2).
```

On the above cubic family with side L>=6, for Fourier mode k this is
`1 + 2 epsilon theta t sum_i cos(k_i) + O(t^2)`. The unit-vector structure
factor sums three such component identities and has the same normalized
coefficient when all three content-coordinate functions are eigenfunctions
of W with the same theta, in particular for the j-family with theta=2j.
Positive theta thus creates nearest-neighbor correlations from
an empty initial state without assuming equilibrium or a one-site closure.
This local startup result supplies neither an infinite correlation length nor
a sustained ordered phase. The remainder here is for a fixed finite model;
the separate degree-five population bound above is volume uniform, but this
spectrum remainder has not been quantified here.


## 6. Dyson coefficient with motion treated exactly

The finite matrix exponential has the convergent Dyson expansion in epsilon,
with kth term an ordered time integral of k birth operators separated by
motion semigroups. Since delta_0 H=delta_0 B H=delta_0 B^2 H=0 and HN=0,
the coefficients of E[N] through epsilon cubed are independent of kappa.
At order four, after integrating the first two birth times, the difference
from the immobile process is

```
C_kappa(t) = integral_(0<=u<=v<=t) (u^2/2)
              delta_0 B^3 [exp(kappa (v-u) H)-I] b du dv.
```

Only the nonstationary two-record part of delta_0 B^3 contributes. It is
-2wb after removing terms constant on motion classes. Setting s=v-u gives

```
C_kappa(t) = (1/3) integral_0^t (t-s)^3
                <b,[I-exp(kappa s H)]b>_(w,N=2) ds,

E_kappa[N_t]-E_0[N_t] = epsilon^4 C_kappa(t)+O(epsilon^5).
```

The inner product is an unnormalized sum over every two-record configuration.
In particular, no partition function divides it. Reversibility makes -H
self-adjoint and nonnegative in this inner product, so C_kappa(t)>=0. For
t>0 and kappa>0 it is strictly positive exactly when the two-record hazard is
not constant along allowed hops. As a function of kappa>=0 it is increasing
and concave: each nonzero eigenmode contributes a nonnegative multiple of
1-exp(-kappa s lambda). This assertion concerns the epsilon-four coefficient,
not the full finite-epsilon population for all times.

Let P be the orthogonal projection onto ker H within the two-record strata,
V_2(b)=<b,(I-P)b>_w, and D_2(b)=<b,-H b>_w. Then

```
0 <= C_kappa(t) <= min{kappa t^5 D_2(b)/60, t^4 V_2(b)/12},
lim_(kappa->infinity) C_kappa(t) = t^4 V_2(b)/12.
```

The first upper bound uses 1-exp(-x)<=x. The second uses the projection away
from zero modes. They do not require one connected content-count sector.

Define psi(z)=integral_0^1 (1-x)^3[1-exp(-zx)] dx. Its stable definition is
the integral, with psi(0)=0. For z>0 an algebraic form is

```
psi(z)=1/4-1/z+3/z^2-6/z^3+6(1-exp(-z))/z^4,
psi(z)=z/20-z^2/120+O(z^3) near zero.
```

If -H has eigenvalues lambda_j and b has squared weighted projections a_j,
then C_kappa(t)=t^4 sum_j a_j psi(kappa t lambda_j)/3. Expanding in kappa t
recovers kappa D_2 t^5/60 from the separate short-time derivation.

For completeness, the Dyson series gives a finite-volume remainder: if
beta=||B||_(infinity->infinity)=2 max_s b(s), stochastic contraction of every
motion semigroup bounds the absolute difference remainder by
`2 V exp(epsilon beta t) (epsilon beta t)^5/120`. This is a conservative
finite-model bound and grows with volume. It is not a uniform justification
for a finite-density or infinite-volume approximation.

## 7. Closed three-site witness

On the three-site path at W=(3/2,1/2,1), positions of two records have weights
(g,1,g) for adjacent, separated, adjacent pairs, where g is their pair weight.
The common-neighbor indicator c is (0,1,0). Its centered part is an eigenmode
with decay lambda_g=(1+2g)/(1+g) and squared weighted norm 2g/(1+2g).
Only equal and opposite contents contribute to h_ab=(W^2)_ab-6; each has
h_ab^2=1/4 and six content assignments. Therefore

```
C_kappa(t) = (t^4/3) [ (9/8) psi(8 kappa t/5)
                            +(3/4) psi(4 kappa t/3) ].
```

The short-time coefficient is (7/150) kappa t^5. The fast-motion limit is
5t^4/32. A block-triangular coefficient evolution of the full finite generator
checks this formula without substituting it into the simulator.

## 8. Relative-position reduction on a torus

For a simple translation-invariant nearest-neighbor torus of volume V, with
side at least three and unit symmetric proposals, let r!=0 be the displacement
of the two records. Their relative generator H_g has rate
`2 w_g(r')/[w_g(r)+w_g(r')]` for each nearest-neighbor displacement step
r->r'!=0; w_g(r)=g when r is a nearest neighbor of zero, otherwise one.
The factor two counts motion of either endpoint. Its reversible weight is
w_g. Let c(r) be the number of common neighbors of zero and r. Then

```
C_kappa(t)/V = (1/6) sum_(a,b) h_ab^2 integral_0^t (t-s)^3
                   <c,[I-exp(kappa s H_(W_ab))]c>_(w_(W_ab)) ds.
```

The factor V/2 arises from ordered endpoint representations of each physical
two-record configuration. The primary check compares this reduction with a
full unordered-pair position generator in fifteen graph/weight cases, with
maximum absolute discrepancy 2.78e-16. The separately sealed calculation
covers the fixed-time coefficient and path formula, not this added reduction.

For the j-family W_ab=1+j v_a dot v_b, h_ab=2j^2 v_a dot v_b. The coefficient
therefore contains an explicit j^4 factor, while the relative motion kernel
still depends on j. It is O(j^4) as j->0 at fixed finite graph, t and kappa.
The earliest orientation pair correlation is instead linear in the vector
eigenvalue theta=2j. This is a hierarchy between two observables in the
supplied model; it does not identify a weak physical force or fix a constant.

## 9. First actual order when the two-record coefficient vanishes

The first-actual-order extension was found in the separate pre-source check.
The primary author reconstructed the following proof and carries its full
argument here, rather than using a report verdict as a premise.

For a row p write f=p/w, on every configuration. Detailed balance and the
telescoping insertion weight give the weighted row identities

```
(pH)/w=Hf,   (pB)/w=Df-bf,
Df(s)=sum_(occupied x) f(s with the record at x deleted).
```

D maps ker H to ker H. Across an allowed hop, pair the deleted spectator
records; their remaining configurations are connected by the same hop.
Deleting the moving record instead leaves identical parent configurations.
Thus corresponding values of f agree. This argument works on actual motion
classes without identifying them with content-count sectors.

Let m be the first occupancy level with H_m b nonzero, if one exists.
The pure-birth row delta_0 B^j has top-level density j! relative to w, and
zero density above j. Induct using D-b and the class constancy of b below m
to obtain delta_0 B^j H=0 for j<=m. At the next step, the only term outside
ker H is -m! b on level m. The first motion-dependent population coefficient
in epsilon is therefore

```
E_kappa[N_t]-E_0[N_t]=epsilon^(m+2) G_m(kappa,t)+O(epsilon^(m+3)),
G_m=(1/(m+1)) integral_0^t (t-s)^(m+1)
                       <b,(I-exp(kappa s H_m))b>_(w,N=m) ds.
```

The m earlier ordered insertion times give u^m/m!; the m! in the row cancels
that denominator. Integrating u from 0 to t-s gives the displayed factor.
For t,kappa>0 the coefficient is strictly positive and increasing and
concave in kappa. Writing D_m and V_m for the class Dirichlet energy and
centered variance gives

```
G_m <= min{ kappa t^(m+3) D_m/[(m+1)(m+2)(m+3)],
            t^(m+2) V_m/[(m+1)(m+2)] }.
```

Its short-time coefficient is kappa m! D_m/(m+3)!, consistent with the
separate time expansion. If there is no such level, induction keeps every
pure-birth row in ker H and the full finite empty-start law is independent
of kappa at every time. On the 4x4 rook graph m=3 for the neutral j=1/2
menu; the separately checked witness is recorded in the original independent
empty-start report. This extension has a proof and a delayed-level witness;
the separately sealed independent check has fifteen block-coefficient cases,
all with three sites. The portable primary runner has twelve such cases,
including one four-cycle; these are distinct suites.


## Witness for a delayed first actual order

On the 4x4 rook graph, vertices are pairs (i,j), and distinct vertices share
an edge if their row or column agrees. The degree is six and every pair of
distinct vertices has two common neighbors. Thus the two-record hazard is
constant on each fixed-content motion class and D_2=0. For the neutral menu
W=(3/2,1/2,1), put three identical records at (0,0),(0,1),(0,2). Their weight
is 27/8 and the unscaled total birth hazard is 159/2. Moving the last record
to (1,2) gives weight 3/2 and hazard 81; the hop rate is 4/13. This single
undirected contribution to D_3 is 243/104>0. Thus m=3: the full law first
changes at time order five, the population at time order six, and the
fixed-time population first changes at formation-intensity order five.
The graph's high degree and triangles are part of this witness, not the
cubic-lattice model in section 3.

## Scope, alternatives and falsifiers

The sign theorem is about the first nonzero coefficient. Later coefficients
can have either sign; it does not prove that increasing mobility raises the
population at every time and finite epsilon. Keeping tau=6 epsilon t or
density fixed while epsilon vanishes is a different limit from section 6.
The finite-volume Dyson remainder does not justify interchanging that limit
with volume. The volume-uniform Taylor bound in section 4 is a separate,
very conservative short-time statement; a checked example has a sufficient
time window of roughly 10^-17 in its chosen abstract units.

A nonconstant W need not favor equal contents: the population sign follows
from a squared hazard difference and reversibility. Positive vector-mode
correlation instead requires positive theta. Complete graphs and W=1 give
useful vanishing controls; the rook graph shows that vanishing D_2 is not a
complete mobility-independence criterion. Motion classes are never merged
merely because their content counts agree.

Decisive falsifiers include a nonzero delta_0 B^2 H under the stated
normalization, a negative first-actual semigroup coefficient, a failure of
the two-record graph formula, or a torus of side at least six whose exact
local geometry differs from section 3. Dropping row normalization, reversible
heatbath motion, the empty initial condition, or generator holding terms
changes the problem and is not a counterexample to these conditional claims.

## Evidence and source review

The portable primary runner assembles full rational generators, compares
actual generator powers, solves block-triangular coefficient evolution, and
compares full two-record position dynamics with relative-coordinate
reduction. Geometry counts use explicit finite graphs; the infinite family
and remainder estimates are proved above. Numerical matrix exponentials
are floating-point checks at declared tolerances, not exact arithmetic proofs.

Before seeing the primary startup derivation, a separate-context checker
constructed rational generators and the first-actual-order deletion argument.
Its report SHA-256 is
`fff040b1b6b3acc5929ab267fe04905bf3aed7d014b4733d615687f97a7bdb84`.
A narrow post-seal review independently checked the torus geometry and local
support estimate. Its clarification to count UPDATED sites has been applied.
The fixed-time extension then received another pre-source derivation and
fifteen complete-generator coefficient checks, report SHA-256
`1ed67a3f52776551660f78fc8df2358c0e4dfba9a825ecb0fb4bf08fa6bb9a6e`.
Those reports, their code, outputs and immutable seals are carried under
`.claude/science/mobile-record-empty-start-response-20260921/independent/`.
They use the same model family in a separate context and are not independent
audit verdicts. The primary author has read their complete arguments and code.

The complete-source review is recorded in
`.claude/science/mobile-record-empty-start-response-20260921/final_source_review/REPORT.md`
(SHA-256 `d7c29cbcb4455faf78e55416bad78c8009450b08d4fd126de50b9ac95bf49b5c`).
Its four narrow scope/evidence findings were corrected and confirmed; no
unresolved mathematical finding remained. The runner reproduced 57/0 and
all eight primary mutations failed in their intended families. A separate
metadata acknowledgment pins this completion reference without altering the
sealed review. This remains scientific scrutiny, not an audit verdict.
Standard finite Markov-generator calculus,
reversible Dirichlet forms, ordered Duhamel expansion and the spectral theorem
are used with their hypotheses given above; no claim of novelty is made for
those tools. No published equilibrium critical behavior is imported.

## Reproduction

```bash
python3 scripts/mobile_records_empty_start_motion_response_2026_09_21.py
python3 scripts/mobile_records_empty_start_motion_response_2026_09_21.py --list-mutations
```

No axiom, primitive, editable prompt, effective-retention surface or audit
verdict is changed. Full pipeline, strict audit lint and changed-evidence
integration remain gates for the eventual combined current-main candidate.

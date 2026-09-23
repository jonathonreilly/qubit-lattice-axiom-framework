---
claim_id: cubic_fourier_energy_and_gaussian_registers_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/fourier_gaussian_register_check_2026_09_15.py
upstream_dependencies: ["docs/SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md"]
claim_scope: "Bounded conditional Fourier energy and Gaussian register lemmas; supplied hypotheses and limit order retained in full proofs."
---

# Fourier energy and Gaussian register lemmas

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15](SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS_BOUNDED_THEOREM_NOTE_2026-09-15.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK4_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS

Original source identity: `BLOCK4_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Fourier energy and prescribed Gaussian/contact derivatives

Personal proof candidate, 2026-09-15. This extends the prescribed-contact
source estimate to derivatives of its complete Gaussian dressing. The scope
is a specified decorated signed loop on the infinite cubic kernel. Physical
connected graph summation and the full characteristic law remain open.

#### 1. A direct cochain energy estimate

Use ordinary counting inner products on oriented cubic r-cells of Z^4,
one positive representative per orientation. In a site-based Fourier gauge,
the coboundary symbol is exterior multiplication by
z(p)=(exp(ip_1)-1,...,exp(ip_4)-1), and its adjoint is contraction by the
conjugate vector. Their anticommutator on the exterior algebra is

    Delta_r(p)=lambda(p) I, lambda(p)=4 sum_mu sin^2(p_mu/2).

Cell-center phases change the gauge unitarily and do not change this scalar
symbol. Thus G_r is the multiplier 1/lambda on finite cochains; the point
p=0 has zero integration measure. For p in [-pi,pi]^4,

    4|p|^2/pi^2 <= lambda(p) <= 16.

Let j be any nonzero finite real cochain, m=||j||_1 and r=||j||_2<=m.
The notation r for a norm in the next formulas is unrelated to cell degree.
The vector Fourier transform obeys ||jhat(p)||_2<=m, and Parseval gives
integral ||jhat||_2^2 dp/(2pi)^4=r^2. Split at the ball of radius R,
where R^2=pi^2 r/m<=pi^2, so the entire ball lies in the Brillouin cube.
Its low-frequency contribution is at most

    (pi^2/4) m^2 integral_(|p|<=R) |p|^-2 dp/(2pi)^4
       =m^2 R^2/64.

The complement contributes at most pi^2 r^2/(4R^2). Consequently

    <j,G_r j> <= H m r,   H=1/4+pi^2/64 < 0.405.       (1)

As a separate normalization check, a unit plaquette boundary has Fourier
norm squared |z_mu|^2+|z_nu|^2. Symmetry of the four coordinate integrals
gives its exact infinite Green energy 1/2. On an N^4 momentum grid with
the zero mode removed, the corresponding sum is exactly (1-N^(-4))/2.

The zero cochain is immediate. No closure, connected support or integer
hypothesis is used in (1). Those enter the component interpretation and
activity reserve below. This improves the initially recorded R^2=r/m
constant by using a larger ball that still lies entirely in the cube.
The argument is elementary Fourier integration, not an imported HLS theorem.

For the stable Gaussian Gram feature

    psi(j)=sqrt(x) (G_r-I/32)^(1/2) j,

lambda<=16 ensures G_r-I/32 is positive on finite cochains. More precisely
these finite cochains lie in the square-root form domain by (1), defining
psi in the common l2 cochain Hilbert space. Thus

    ||psi(j)||^2 <= x H m r.                           (2)

This is an infinite-cubic statement. It is not automatically a bound for
finite free-boundary relative cochains or torus zero modes. A finite Fourier
sum below is a discretization check only; no boundary matching is inferred.

#### 2. Gaussian derivatives as feature-register contractions

Retain D(S)=product_u det S[I_u,I_u] and the complete Gaussian

    G_sigma(S)=exp[-1/2 sum_same i,j S_ij sigma_i sigma_j
                                           <psi_i,psi_j>],

including its diagonal. S is a fixed positive semidefinite unit-diagonal
matrix independent of the component labels/positions. For a specified set
E_G of distinct off-diagonal pair parameters,

    partial_(E_G) G_sigma
        =G_sigma product_((i,j) in E_G) [-sigma_i sigma_j <psi_i,psi_j>].

Pairs in different species give zero. Species Hilbert spaces can be placed
in orthogonal summands to implement this condition without changing norms.

For every edge use a register C|vac> direct-sum H_feature. In any total
vertex order, its first endpoint is the row <psi_i| from the feature sector
to vacuum and its last endpoint is the column |psi_j> from vacuum to the
feature sector; intermediate vertices act as identity on it. Vacuum
expectation gives exactly the inner product. Their operator norms are
||psi_i|| and ||psi_j||. A sign -sigma_i sigma_j splits into unit scalar
endpoint factors. The real Gaussian replica representation of G_sigma
adds local phases of modulus one, just as in the earlier source proof.
No trace over the feature Hilbert space is taken. In infinite dimension
the Gaussian is an isonormal family of scalar pairings with these features,
not a purported Hilbert-valued random vector with identity covariance.

Tensor these registers with the complete contact registers and their CAR
blocks from BLOCK2_CONTACT_REGISTER_SUM. For a fixed partition E=E_H union
E_G, let h_i,g_i be its incident contact/Gaussian degrees, d_i=h_i+g_i.
For one contact orientation the vertex norm is bounded by

    |A_i|^(h_i/2) ||psi_i||^(g_i).

The contact matching signs depend only on contact registers; the Gaussian
registers introduce no extra inversion sign. The scalar coefficient has
such a representation in EVERY cyclic order. Different realizations can
therefore be used for the different coincident-source boundaries of the
scalar three-lines proof. No commutation of one-sided maps is asserted.

#### 3. One activity reserve absorbs all vertex degrees

For integer currents |A_i|<=3m_i and r_i^2>=m_i. Choose the positive
weight, independent of the prescribed derivative graph,

    q_i=(2/384) exp(-x_i r_i^2/64) 2^|A_i|
                         exp(m_i+x_i r_i^2/512) exp(R|L_i|).     (3)

Set t=x r^2. The elementary maxima and d!>=(d/e)^d give

    m^(d/2) exp(-m) <= sqrt(d!) 2^(-d/2),
    t^(g/4) exp(-t/512) <= (g!)^(1/4) 128^(g/4).

The degree-zero cases use the evident upper bound one. Equations (2)-(3)
then yield the normalized vertex bound

    C_H^h C_G(x)^g sqrt(d!) (g!)^(1/4),
    C_H=sqrt(3/2), C_G(x)=sqrt(H/2) (128x)^(1/4).       (4)

Indeed x^(g/2) r^(g/2)=x^(g/4)t^(g/4). In particular (4) is at most
C(x)^d (d!)^(3/4), C(x)=max(C_H,C_G(x)). This preserves a smaller
factorial power than estimates based on powers of a filling area.

For |z|<=R and a<=min(sqrt(x_e),sqrt(x_m))/(128 C_f R), the existing
physical source bound gives R|L_i|<=x_i m_i/128. Thus (3) satisfies

    q_i <=(2/384) exp[-3x_i m_i/512+(3log2+1)m_i]
        <=(2/384) exp[-x_i m_i/256]

if x_i/512>=3log2+1. Both x_i>=32768 suffice. The previous anchored
moments, sine matrix norm rho<3.862e-33, and S4=Tr |L|^4 J^2=O(a^4)
therefore apply to this NEW weight as upper bounds. No limit of x or N
with a is taken.

#### 4. The precise prescribed-graph source consequence

Put q into the same scalar sine matrix J and let l be the protected loop
length. For fixed E_H,E_G and any placement of four source powers, the
complete contact-resource/orientation sum with Gaussian derivatives obeys

    |F_(E_H,E_G)| <= [product_i C_H^(h_i) C_G(x_i)^(g_i)
                                      sqrt(d_i!) (g_i!)^(1/4)]
                                rho^(l-2) S4.          (5)

As before, the factor 2^(-|E_H|) in each oriented CAR representation is
canceled by summing the 2^|E_H| contact orientations. Gaussian signs have
modulus one. Expectation over replicas and orientation signs preserves (5).
The same statement with two source powers uses S2=Tr |L|^2 J^2.

For the full derivative partial_E(D G_sigma), apply the ordinary Leibniz
partition of E. If C=max_species C(x), all 2^|E| terms give the uniform
bound

    (2 C^2)^|E| product_i (d_i!)^(3/4) rho^(l-2) S4.    (6)

Some cross-species terms vanish; (6) does not rely on counting that gain.
Taylor subtraction through quadratic order adds at most R^4 l^4/24.
At one fixed decorated graph, the earlier absolute graph/source estimates
justify the component-cutoff passage; extra Gaussian factors have the
existing polynomial filling bounds, and extra contact factors are local.
The operator bounds are uniform in that cutoff. No graph-order limit is
interchanged and no arbitrary forest sum is claimed here.

The remaining mixed pair factors are NOT replaced by arbitrary bounded
multipliers. The earlier counterexample rules out that shortcut. A separate
representation or summation for them, plus the actual physical graph
multiplicities and selected-state matching, is still required.


#### Author verification and personal review scope

The cochain wedge/contraction symbols match lambda I with maximum matrix
error 3.79e-15. The Fourier grids reproduce the exact single-plaquette
normalization and sample two other finite cochains; no numerical
infinite-volume error estimate is claimed. Explicit tensor registers in
576 graph/order fixtures reproduce feature inner products and endpoint
norms. Full determinant/Gaussian nilpotent jets match the Leibniz form,
and four generic graph fixtures satisfy all35 four-source placements,
including the sharper direct vertex-norm bound. The analytic reserve
extrema are checked for degrees through40.

An initial synthetic random feature exceeded the declared energy premise
and stopped the check before the source assertion. Its script and failure
record are preserved under review/block4_initial_fixture_failure. The
revised synthetic fixture explicitly rescales into that premise; this is
a setup correction, not a change of the theorem or evidence for arbitrary
random features. A product-of-derivatives substitution is rejected by a
nonzero discrepancy. All verification is by the author; no independent
review or retained-grade conclusion is claimed.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK4_TREE_COUNT_AND_DECORATED_CYCLE_NORMALIZATION

Original source identity: `BLOCK4_TREE_COUNT_AND_DECORATED_CYCLE_NORMALIZATION.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### The tree gain and the normalization it does not supply

Personal derivation, 2026-09-15. This checks how the new degree estimate
interacts with combinatorics. It gives an honest positive tree estimate
and identifies a divergent series of proposed diagram MAJORANTS. It does
not prove that the physical diagram series diverges, or rule out a regrouping.

#### A tree sum can absorb the three-quarter degree factorial

For labelled trees on n>=2 vertices, put

    Z_n(theta)=sum_T product_i (d_i(T)!)^theta, 0<=theta<1.

In the Prufer correspondence, a vertex of degree d_i occurs d_i-1 times
in the word of length n-2. Counting words with those occurrence numbers
gives exactly

    Z_n(theta)=(n-2)! [z^(n-2)] f_theta(z)^n,
    f_theta(z)=sum_(k>=0) ((k+1)!)^theta z^k/k!.

The coefficient ratios of f are (k+2)^theta/(k+1), tending to zero.
Hence f is entire. Its nonnegative coefficients give, at z=1,

    Z_n(theta)/n! <= f_theta(1)^n/[n(n-1)].             (1)

For theta=3/4 the bound can be made elementary and explicit. The k-th
coefficient has fourth power (k+1)^3/k!. Bound its first sixteen values
upwards by rationals with denominator1000, using integer fourth-power
comparisons. The coefficient ratio from k=15 onward is at most9/16:
17^3<9^4 and the ratio decreases with k. The exact rational sum and
geometric tail give

    f_(3/4)(1) <= 79781/7000 <11.398.                  (2)

Thus the new vertex cost is compatible with an exponential tree sum WHEN
the single labelled-tree normalization 1/n! is actually available. This
is a combinatorial statement; it does not provide a physical tree expansion.

#### A separately enumerated spanning cycle has already spent that factor

Fix r electric and r magnetic labelled vertices. The number of undirected
alternating Hamiltonian cycles is r!(r-1)!/2 for r>=2. Dividing by the
physical two-species labelling factor (r!)^2 leaves 1/(2r), the familiar
cycle factor. Now decorate every such cycle with one arbitrary labelled
tree on each species. These are specified cycle/forest objects; they are
not claimed to be the actual BKAR/cut expansion.

The undecorated tree counts alone give the remaining multiplicity

    r^(2r-4)/(2r).

Even restricting the added trees to paths does not fix the issue. There
are r!/2 undirected Hamiltonian paths on each set of r labels, leaving

    (r!)^2/(8r)                                       (3)

decorations after the cycle normalization. Added degrees are now at most
two and total graph degrees at most four. Consequently this problem is
not only the growth of high-degree vertex factorials.

For any fixed rho>0 and any fixed per-extra-edge cost eta>0, blindly
using one uniform loop majorant rho^(2r-2) eta^(2r-2) on all these
decorations gives terms at least

    (r!)^2/(8r) (rho eta)^(2r-2).

They do not tend to zero. The ratio of consecutive displayed terms is
r(r+1)(rho eta)^2. No matter how tiny the fixed norm constants are,
this particular series of upper bounds eventually grows. Dividing by
another (r!)^2 would change the enumerated coefficients without an identity.

There is no claim here that each actual physical contribution is bounded
BELOW by these terms. These are the values of an unsuccessful common
upper-bound prescription. Cancellations, forest-parameter integrals, an
identification that counts fewer objects, and regrouping into blocks remain
possible routes. The actual physical multiplicities and residual mixed
factors are still to be supplied. Formula (1) suggests using the tree
normalization at the level of a valid block expansion, but supplies no such
block construction by itself.

#### Verification scope

The runner enumerates Prufer words and independently extracts the generating
series coefficient through n=7. It separately enumerates alternating cycles
and paths for small r, and certifies (2) by rational fourth-power inequalities.
These finite challenges supplement the exact counting proofs. They do not
execute the full physical expansion or establish an axiom obstruction.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: fourier_gaussian_register_check_2026_09_15](../scripts/fourier_gaussian_register_check_2026_09_15.py); [current cache](../logs/runner-cache/fourier_gaussian_register_check_2026_09_15.txt).
- [Program: tree_count_check_2026_09_15](../scripts/tree_count_check_2026_09_15.py); [current cache](../logs/runner-cache/tree_count_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).

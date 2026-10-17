# Focused mathematical check: static boundary reflection

Completed 2026-10-16. Source-exposed review of a provisional conditional
construction, with a separate finite-readiness extension. This is not a
retained audit, a native-hardware derivation, or blind independent discovery.

## Finding and exact reviewed scope

**The narrow conditional theorem in CANDIDATE_V2.md is mathematically supported
by this check. I found no remaining mathematical defect in its stated
quantifiers, constants, complete-output comparison or qubit realization.**
The separately supplied FINITE_READINESS_ADDENDUM.md also checks out at its
stated finite-support and finite-observation-horizon scope. Its claims do not
turn a fixed finite apparatus into an all-future completion device.

One quantifier ambiguity in V1 was reported and corrected during this review.
Immediately before (6), “any absolutely continuous g vanishing at the band
endpoints” did not explicitly identify its support. If “band” were read as the
full spectral band (0, pi), the claimed derivative lower bound would be false:
for n=0, t=J=1 and k=pi/12, the derivative is 2 sin(pi/12), approximately
0.51764, below sqrt(3). All actual packet applications already have the needed
support. **V2's exact replacement explicitly requires support in
[k0-sigma, k0+sigma], contained in [pi/3, 2pi/3], with zero endpoint values.
That correction is sufficient.** The complete diff contains only this change;
no constant or subsequent argument needed alteration. V1 was preserved.

| Source | Bytes | SHA256 |
|---|---:|---|
| Original CANDIDATE.md | 13170 | `4bab49101d34d685ad130d53b65cd1cee8adaab66b72a42ed4276ea05a41e278` |
| Corrected CANDIDATE_V2.md | 13239 | `694484853b731991d97f11f5d9a3a012ff30b9badb7fe57a7c57f6fee7e2fd36` |
| FINITE_READINESS_ADDENDUM.md | 4856 | `ce01691b49abf924d2fc610cf2dd6c71c565c0c21df6f1bc39960ecb2c546a2f` |

Frozen copies are in `sources/`. `SOURCES.json` and
`V2_AND_ADDENDUM_SOURCES.json` contain the original absolute paths and all
source identities. Both prior-note hashes quoted in the proposal match their
actual Git blobs at PR9657 head
`c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc`:

- The product-source note is SHA256
  `b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d`.
  Its target and premise passages confirm the literal K and W used here.
- The prior half-line note is SHA256
  `87d8c6f4b98563cd827f0d8264ec2575c689ec4d7ac018fe5b87d89006181ed3`.
  Its sections 2–5 confirm the acknowledged outgoing-tail, positive-qubit and
  finite-horizon precedents.

I read the full new proposal, its complete correction, and the full addendum.
The prior notes were inspected for these target/premise and antecedent
sections; their entire other scientific arguments were not re-audited.
The selected workflow snapshot is SHA256
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.
The reviewer skill and necessary references were checked against the local
Git snapshot `5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`; the already read
installed copies were byte-identical. No network freshness check was made,
as the assigned scope prohibited network calls.

## Load-bearing mathematics

### Boundary sign, bound state and target phase

Inserting an incoming wave z^(-n) and outgoing wave r z^n, z=exp(ik), into
the actual row-zero equation gives

    (w+2J cos k)(1+r)=J(exp(-ik)+r exp(ik)).

Solving this equation yields exactly (2). The incoming sign is physically
consistent with group velocity -E'(k)<0; the reflected sign has group velocity
+E'(k)>0. At k=pi/2 the free coefficient is 1 and the nominal coefficient is
(-7-24i)/25. K commutes with X1 X2 because the two Pauli anticommutations
cancel. The W eigenvalues on the plus/minus sectors are exp(2i theta) and 1,
respectively, so the reflected operation is precisely exp(-2i theta) W.
There is no conjugation or omitted scalar phase.

There is also a direct check of the bound-state issue that does not assume
continuum completeness. For w>J set q=-J/w. The normalized bound vector is
sqrt(1-q^2) q^n and its energy, derived from the bulk recurrence, is
2J+w+J^2/w. For each k in the packet support its inner product with the
continuum eigenfunction is proportional to

    1/(1-q exp(-ik)) + r_w(k)/(1-q exp(ik)) = 0.

The two geometric-series terms cancel exactly after substituting the
reflection coefficient. Thus the exact continuum packet has no bound-state
component. This does **not** say that the prepared chi has none: its component
is bounded by its full vector distance to the continuum packet, as used in
(14). Under the same actual Hamiltonian this error is constant in norm at
all elapsed times. At w=J the formal q=-1 solution is not square summable;
the threshold causes no singularity on the compact packet support.

### Exact normalization without spectral completeness

The synthesis maps are restrictions of two full-integer Fourier maps and
are bounded. Multiplication by E(k) is bounded. Coordinatewise application
of the checked eigenfunction equation therefore gives a strong, norm
differentiable solution of the bounded selfadjoint half-line Hamiltonian.
Uniqueness of that bounded-operator evolution gives (11).

Parseval on the full integer line gives norm one for a_(-T). On its negative
sites, n=-m with m>=1, the phase becomes mk+E(k)T and is nonstationary. The
corrected tail estimate sends that negative-site norm to zero. The reflected
half-line packet b_(-T)^w also tends to zero. Hence the half-line norm of
psi_(-T)^w tends to one. Since that norm is conserved for every real time,
it is exactly one at every time. This establishes precisely the needed
family of normalized solutions; it makes no claim that this family spans
the entire clock Hilbert space.

### Tail constants and fixed static strength error

Direct integration gives the stated L2 normalization, F0 and F1. On the
corrected support, E'(k)>=sqrt(3)J=v and |E''(k)|<=2J. Integration by parts
has zero endpoint term and gives

    |integral g exp(i phi)/sqrt(2pi)|
      <= [||g'||_1+(2J/v)||g||_1]/[sqrt(2pi)(n+vt)].

For vt>=1, the square sum is bounded by (vt)^(-2)+(vt)^(-1)<=2/(vt).
These facts give (6)–(10), including all numerical factors, pointwise in
every permitted time. No time averaging or asymptotic sequence is used.

Writing x=w/J and c=cos k, the denominator obeys

    D/J^2=x^2+1+2xc >= x^2+1-x >= 1

for x in [1,5/3] and c in [-1/2,1/2]. The stated derivative numerator is
at most 2J^2(1+5/6), giving 11/3. The free derivative is 2. Thus the
17/3 quotient bound is valid. Differentiation in w gives 2J sin k/D<=2/J.
Integration in k and w proves (16). Restriction of the full-integer Fourier
transform cannot increase norm, so the same Delta bounds the outgoing
packet difference at **every** time.

This last mechanism is why the coefficient error need not grow as t times
|delta_w|. Both the exact continuum comparison and the actual prepared
state use the same faulty h_w. The only remaining strength dependence is
the reflection multiplier. The proof would not cover a fault in J, K,
clock disorder, a time-dependent perturbation or multi-head leakage; the
proposal explicitly excludes those extensions.

### Complete output, reference, phase and elapsed old age

From ||psi||=1, the reverse triangle inequality bounds |A_T-1| by the
initial reflected tail. Normalizing a_(-T) with a positive real scalar then
costs at most a second copy of that tail, proving (14). At the output,
|B_s-1|<=||a_s||, so removing the incoming tail and normalizing b_s^0 costs
at most 2||a_s||. Adding the initial error and the multiplier error gives
(18) exactly.

The errors for the two old sectors lie in orthogonal **old** subspaces.
Their clock vectors need not be orthogonal. Consequently the full
ready-input operator norm is the larger sector error, not their sum.
Factoring the unchanged old evolution gives exp(-itK) at actual elapsed
t=T+s, and the scalar exp(-2i theta) remains. This proves (19) for every
t>=2T. Tensoring an arbitrary passive reference preserves this operator
norm. The trace-norm estimate follows by writing the difference of the
two isometric density outputs as two terms; each has norm at most the
isometry error. Its unhalved bound is therefore 2 times that error, capped
at 2. No output subsystem is removed in this argument.

The schedule (20) allocates epsilon/2, epsilon/4 and epsilon/4 as claimed.
Both normalizations are strictly positive; each individual tail bound is
strictly less than epsilon/4 since both CA and CB are positive. The allowed
delta interval lies inside [J,5J/3]. The asymptotic T scale is
J^(-1) epsilon^(-3), and the coefficient tolerance has no readout-time
dependence. These are sufficient and quite conservative costs.

### Full-qubit positivity, strength and geometry

The clock-bond matrix on 00 is zero, on 11 is 2J, and on 01/10 is
J[[1,-1],[-1,1]]. Its spectrum is {0,0,2J,2J}. The boundary is the product
of two commuting projections with coefficient w>0; its spectrum is zero
and w. The literal old K has eigenvalues 1 and 3. These are positive
**blocks**, not assertions that every Pauli summand is positive.

More explicitly, each bond is bounded above by
2J(n_n+n_(n+1)). Including J n0, finite partial sums obey the uniform
upper bound 4JN in each fixed-number sector. Since they increase by
positive operators, their strong limit exists there and is bounded
selfadjoint. Taking the orthogonal direct sum supplies the stated positive
selfadjoint operator in the finite-excitation representation. Bounded
boundary and old terms preserve selfadjointness on that domain and preserve
positivity. This construction needs no infinite-density thermal state.

The block incident loads are 4J at an interior clock site, 3J+w at clock0,
and w additional at each old site. At J=3/16,w=1/4 these are 3/4, 13/16
and 1/4. The maximum faulty clock0 load is 7/8 and the old additional load
is at most 5/16. The old norm-three load remains additional. The boundary
expansion is (I-Zc0)(I-X1 X2)/16. The displayed chain embeds in Z^3; the
boundary block is a connected diameter-two triple, with three-body
support. No nearest-neighbor two-body synthesis has been established.

On the prepared one-head sector, 1<=H<=3+4J+w, yielding [1,4] at the
nominal dyadic choice. Conservation of total energy moments and K follows
from the static Hamiltonian and exact commutation. It does not price
preparation or the supplied infinite lattice.

## Separate finite-readiness and finite-horizon addendum

I checked all of (A1)–(A6), including integer and endpoint conventions.
No correction is required.

For n>=N with d=N-2JT>=max(1,2JT), the incoming phase derivative has
magnitude at least n-2JT, and its second derivative has magnitude at most
2JT. The integrated-by-parts numerator is therefore bounded by F1+F0.
Summing (d+m)^(-2) for m>=0 gives at most 2/d. This yields (A1) with
the stated 1/sqrt(pi d) factor. The ceiling in (A3) ensures every needed
real inequality after rounding. Its tail is at most eta_p/4. Together
with A_T>=3/4, this leaves retained norm at least 5/8 when eta_p<=1/2.
Indeed (A2) then bounds the normalized-state error by 2 eta_p/3, so the
addendum's weaker eta_p guarantee has slack. The claimed support-size
upper bounds follow from (F1+F0)^2=O(1/sigma) on the stated interval.

Adding J n_(M-1) gives diagonal 2J at the far endpoint. The finite matrix
is the actual compression of h_w. Both spectra lie in [0,17J/3], so
c=Rho=17J/6 gives selfadjoint contractions. From the last permitted input
site N-1, reaching the first removed site M requires exactly M-N+1 hops.
Diagonal entries do not move support. Thus degree k<M-N+1 polynomials
give identical vectors after embedding. The strict inequality and the
plus-one in d_M are both correct.

The Chebyshev expansion contributes a coefficient 2 to every k>=1 term;
the difference of two contraction images contributes a further factor 2.
This gives 4 times the Bessel tail. On the generating-function contour
|z|=exp(mu), coefficient extraction bounds

    |J_k(x)| <= exp[-mu k+x sinh(mu)]  (x>=0).

Its geometric tail is exactly the last expression in (A4). Replacing t
by Tobs bounds the exponential uniformly for 0<=t<=Tobs without asserting
monotonicity of individual Bessel absolute values. Solving this sufficient
bound for d_M gives (A5). If an explicit integer formula is desired, it
is M=max(N, N-1+ceil(the right-hand side of A5)); this is equivalent to
the stated pair of inequalities.

The finite/infinite comparison applies uniformly in both old sectors, and
exp(-itK) cancels from its norm. Adding preparation, propagation and gate
errors proves (A6), with the target in the explicitly identified common
half-line embedding. The far-end incident load is 3J. The full clock norm
does grow with M: the all-occupied finite clock has energy 2JM. This
does not change the bounded energy in the prepared one-head sector.

The exact small-matrix path check uses N=3,M=7,J=3/16,w=1/4 and Rho=17/32.
The first difference is at degree 5, solely at site 7, with rational
amplitude (-6/17)^5=-7776/1419857. Degrees 0–4 agree exactly. The length-12
surrogate cannot see its own far endpoint at these degrees, so these
particular path identities are exact infinite-half-line identities.

## Executed evidence and its limits

`check.py` constructs finite Jacobi matrices from the Hamiltonian and
evolves by tridiagonal eigendecomposition. It does **not** propagate by
inserting the candidate's continuum packet. That provides a distinct
implementation for the sign, target phase and old-aging check. The known
target and packet shape were exposed before implementation. No root author
diagnostic was read or reused.

At J=1, sigma=0.15, T=80, clock lengths 768 and 1024, quadrature order 768,
and s=80,160,240:

- Nominal full-joint operator errors at length 768 are approximately
  0.0729752, 0.0727879 and 0.0727475, equal to the maximum sector error.
- Omitting the common global phase gives about 1.6. Omitting actual old
  aging gives approximately 1.98776, 1.91782 and 1.23221. Conjugating the
  reflection gives row-zero residual 3.2 at the center, while the correct
  row residual is below 4.1e-16 on the sampled support.
- The nominal prepared bound-state amplitude is approximately 2.47123e-4;
  it is nonzero. The continuum-bound overlap is approximately 2.3e-18.
  The ready/continuum difference is about 0.00555, below twice the
  reflected ready tail, about 0.0111. The bound energy is 49/12 for J=1.
- Increasing the clock length changes the padded evolved vectors by
  about 5.78450e-4. Changing quadrature order from 384 to 768 changes the
  compared packet vectors by at most 1.46e-13. These are measured
  diagnostics, not certified numerical enclosures.

The diagnostic width/time is not the much more expensive sufficient
schedule (20). Some analytical error upper bounds exceed 2 at these
diagnostic parameters; numerical agreement with such loose bounds is not
decisive evidence for their constants. Their justification is the explicit
analytic argument above. The finite calculations instead discriminate
wrong signs/phases and show the bound component that must be controlled.

`check_addendum.py` also compares a 24-site finite chain with a 128-site
reference for an arbitrary normalized input supported on three sites,
J=3/16,w=1/4,Tobs=20. At t=20 the observed difference is about 1.54470e-9;
the stated contour upper bound is about 4.67310e-4. The Bessel tail printed
there is truncated at index 299 and the reference chain is finite; this
numerical example is not an infinite-volume certificate. The separate
integer-schedule rows evaluate the large sufficient N and M choices but
do not construct or evolve those large states.

Both complete stdout files and empty stderr files are retained. The
execution receipts record exact scripts, hashes, arguments, runtimes and
caps:

| Evidence | Scope |
|---|---|
| `EXECUTION.json`, `stdout.txt`, `stderr.txt`, `RESULTS.json` | Exact local identities; finite direct evolution; mutations; arithmetic schedule |
| `ADDENDUM_EXECUTION.json`, `addendum_stdout.txt`, `addendum_stderr.txt`, `ADDENDUM_RESULTS.json` | Exact path degree; finite propagation example; cutoff/horizon integer arithmetic |
| `check.py`, `run_check.py` | First run's actual executed sources |
| `check_addendum.py`, `run_addendum.py` | Extension run's actual executed sources |

The runtime was Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1 and SymPy 1.14.0
on macOS arm64, one numerical-library thread. The first run was capped at
120 CPU seconds and 180 wall seconds; the extension at 60 CPU seconds and
90 wall seconds. Recorded elapsed wall times were approximately 2.534 and
1.230 seconds. Maximum constructed numeric clock dimension was 1024,
full clock-spin dimension 64, and exact symbolic path dimension 12. Peak
reported resident sizes were approximately 155 MB and 87 MB. No hard RAM
limit was imposed; matrix dimensions and runtime were bounded explicitly.

This check shares the author's target and assumptions and is therefore
source-exposed. The boundary/geometric-series derivation and independent
matrix implementation give additional evidence, but they do not create
blind-discovery independence or formal verification. The all-future and
infinite-volume statements rest on the mathematical proofs, not finite
numerics. No literature novelty judgment, physical energy identification,
native packet preparation, two-body implementation, noise robustness,
reset/reuse or Record formation was established.

No prompt file, axiom, audit record, original candidate, shared checkpoint
or Git state was edited by this checker. All checker writes are within this
review directory. The parent made the single V2 support clarification in a
separate preserved candidate file. The appropriate disposition is a checked
conditional research result within its explicit added-apparatus premises;
formal retained status remains outside this review.

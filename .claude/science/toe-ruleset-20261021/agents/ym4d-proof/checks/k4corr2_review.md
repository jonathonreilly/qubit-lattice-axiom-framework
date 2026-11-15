# Independent hostile review of K4CORR2

**Disposition: HOLD for completion of the author brief.** The formal
coefficient, restricted finite diagram bounds, regulated bare bound and
conditional positivity implications pass at their stated scopes. No finite
uniform bound on the complete renormalized Yang–Mills coefficient is
supplied. The manuscript accurately leaves that central target OPEN. I
found no additional mathematical repair required to preserve the present
partial research result.

This is a fresh, independent **same-family Codex review**, not cross-family
review or an audit. I did not author the manuscript. I rebuilt the argument
from its displayed definitions and primary inputs, reran its registered
checker in memory, and independently checked the pairing table by weighted
multigraph enumeration. Only this review file was created or edited. The
active AUTHOR file whitelist controls over the separate REVIEW brief's
suggested top-level filename. No commits, ledger changes or audit actions
were performed. Balaban and Dimock retain credit for constructive RG;
their work supplies no implicit estimate in this review.

All manuscript line numbers below refer to the 559-line `K4CORR2.md`,
SHA-256:

`ac43da911379f72edf03e1efb3cc81eb89db9057737fc53957e87d3f0a9d3865`.

The reviewed and rerun `checks/k4corr2_exact.py` has SHA-256:

`e7ea27dd531baf36d6d08e1be125bd24be6625781ea7daa86a9642ce79f609c1`.

| Author item | Verdict and manuscript lines | Binding completion requirement |
|---|---|---|
| 1. Write the relative order-h² normalized correction with the separated tests and prior regularization | **PASS FORMAL / original-law identification OPEN**, 25–118. The five families and `c=D4/A4−2D2/A2` are correct. The preceding note does not actually specify a complete regulator; the new heat cutoff is explicitly a bare diagnostic. | B1: finish the renormalized prescription and its matching before identifying the diagnostic with the requested YM coefficient. |
| 2. Bound every class and supply an explicit uniform Cbar | **PARTIAL / HOLD**, 120–409. Equations (10), (12) bound only declared subfamilies; (13)–(15) bound all bare families at fixed cutoffs. The unsupplied `C_rem` in (20) is essential. | B1: bound the complete renormalized complement, including counterterms, intersecting collisions and both regulator limits, with explicit certified constants. |
| 3a. Combine the bound and rate into an explicit non-cancellation window | **PASS CONDITIONAL / requested uniform window OPEN**, 302–325 and 419–461. The bare window and the formula `1/(2 Cbar)` are correct, but the latter has no supplied uniform Cbar. | After B1, instantiate the uniform threshold in FLOW units. A cutoff-dependent threshold shrinking to zero does not complete this item. |
| 3b. Name the precise higher-order and nonperturbative estimate needed for actual YM | **PASS as a sufficient input statement**, 463–529. K4RATIO-REM, Q-LOW and the same-trajectory moment limit suffice. Their actual producers remain OPEN. | No new proof of these producers is demanded by this brief's request to name them. B2 below is required before claiming the corresponding actual-law positivity theorem. |
| Exact arithmetic, evidence and scope discipline | **PASS**, 531–559 and the checked artifacts. All 97 registered assertions reproduced; all 20 independent connected-count comparisons passed. | Preserve the distinction between these checks and the still-uncomputed YM coefficient. |

**R1. Observable, free constants and regulator provenance — PASS.**
Locations: 25–70, equations (1)–(3).

The temporal coordinate alone gives separation at least `1−2/10000`.
The trace-normalized plaquette expansion gives the ordered-plane density
`e=mathcal F²/(4N)` and action `u e/2=mathcal F²/(4g_std²)`; therefore
`g_std²=2N h²` and `e=h² F_can²/2`. This agrees with CUMUL 173–192
and FLOW 573–593. Differentiating `D=1/(4pi² r²)` gives the two-form
kernel `G=Lambda²(I−2zz^T/r²)/(pi²r⁴)`. Two quadratic vertices have
two Wick pairings; four have three cycles with sixteen leg assignments
each. Thus the free formulas in CUMUL 194–227 have exactly the stated
normalization.

At the centres the coefficient is `96(1/81+1/256+1/20736)=169/108`.
CUMUL 293–322 retains the support displacement `<=1/2500`, edge-matrix
error `<1/250`, and four-factor error `<1/60`, giving
`9971/6480<A<10309/6480`. Its covariance enclosure is
`12(2500/2501)^8<=B0<=12(2500/2499)^8`. These imply the manuscript's
`A>3/2`, `11<B0<13`, and `R0>3/(338d)` without substituting point
values for smooth tests.

K4CORR 304–309 expressly leaves the regulator, zero-mode/IR prescription,
subtractions and matching unspecified; REVIEW_K4CORR 200–203 and
295–304 confirm this. The heat kernel is LGF 60–72 with its lower time
limit changed to delta². Its Fourier singularity is locally integrable
in four dimensions. Compact interaction vertices give finite coefficient
integrals under the later majorant. The text correctly denies a Wilson-law
or gauge-identity identification for this regulator.

Fix: none to this specification. B1 remains necessary for its use as YM.

**R2. Vertices, connected normalization and first ratio coefficient —
PASS FORMAL.** Locations: 74–118, equations (4)–(6).

Expansion of `(f+s h C)²/4` gives action factors `s/2` and `s²/4`;
expansion of `(f+s h C)²/2` gives insertion factors `s` and `s²/2`.
Integration by parts of `bar c(−partial.D)c` gives the displayed ghost
vertex. Grassmann signs are retained. With the leading source tilt, the
h² logarithmic term is `<B_t>_t+kappa_t(A_t,A_t)/2`. Distinct-source
differentiation produces X2, two distinct X1s, X1 with −V1, −V2, and
two V1s. The first two cross orderings cancel the half; two identical
bulk V1s keep it. This proves all five terms for both n=2 and n=4.
Deterministic centring changes only the linear source coefficient.

Dividing `A4+h²D4` by `(A2+h²D2)²` gives exactly
`c=D4/A4−2D2/A2`. The full reversal symmetry, rather than the first
displayed vertices alone, is needed for the higher even-power notation.
The note retains that premise. Common multiplicative insertion factors
cancel because their powers are four in P and four in Q²; this cannot
cancel arbitrary graph or operator-mixing terms.

Fix: none at formal scope. Counterterms are symbolic inputs, not evaluated
coefficients. B1 must include their finite matched contribution.

**R3. Vertex majorants and connected pairing table — PASS.**
Locations: 122–174, equations (7) and its tables.

In the stated basis `||T^a||_HS=1/sqrt(2)`. The commutator estimate
`||[T^a,T^b]||_HS<=1` gives `|f^{abc}|<=sqrt(2)<=2`.
Expanding the ordered Lorentz sums and all derivatives gives
`(L0,L1,L2,T1,T2)=(32d,128Nd³,64Nd⁵,80Nd³,32Nd⁵)`.
The cubic action's 80 is 64 from gauge fields plus 16 from ghosts.
Using `s<=2N`, but the exact `s²=2N` for quartics, is valid for N>=2.

Every pairing splits uniquely into its vertex-connected components.
The logarithm of the finite moment polynomial therefore removes exactly
the disconnected pairings and yields (7). Inclusion-exclusion on internal
pairs gives the stated no-self formula. Even ghost vertices factor over
disconnected components; their permitted pairings form a subset of the
unsigned bosonic majorant. No positivity of ghost amplitudes is assumed.

For an implementation-independent check, I enumerated symmetric
nonnegative multigraph adjacency matrices with vertex degrees ell_i.
For loop counts a_ii and edge multiplicities a_ij their labelled weight is

    product_i ell_i! / [product_i (2^a_ii a_ii!) product_(i<j) a_ij!].

This follows by distributing each vertex's labelled half-edges to edges
and loops, then matching edge groups. Restricting to connected matrices,
and separately to zero diagonal, reproduces every count in 164–168:
for n=2 the pairs are `(12,0),(15,6),(90,36),(72,24),(720,360)`;
for n=4 they are `(576,288),(720,360),(7200,4176),(5760,3456),
(86400,55296)`. This is distinct from the checker's leg-pairing recursion
and partition/Mobius calculation.

Fix: none. These are majorant multiplicities, not evaluated YM tensors.

**R4. External-only and four-support star bounds — PASS AT STATED SCOPE.**
Locations: 178–248, equations (8)–(12).

For derivative orders 0,1,2, LGF (25), or direct differentiation, gives
the component bounds `4,32,384` at r>=1/2, all below H=512. Every
no-self external edge joins distinct supports. Multiplying the vertex
bounds, counts and edge bounds gives exactly
`B4=9·2^73 N(1+15N)d^8` and `B2=3·2^42 N²d^6`.
Dividing by the lower free coefficients with pi<4 yields the displayed
`C_ext=3·2^90 N(1+15N)d^7+(3·2^51/11)N²d^5`.

For the star there are `4!·2^4·3=1152` pairings. Each spoke has one
derivative and is bounded by `4r^-3`; the two external edges cost H².
In the cell nearest x_i every other distance is at least sigma/2=1/4:
otherwise its distance and the nearer r would sum to less than the
pair separation. On r<=1 the radial integral is at most `32·4^9`;
on r>1 it is less than `2pi²/8<4`. Summing four cells gives
`4(32·4^9+4)<2^26`. This proves the infinite-volume L1 bound, including
all four insertion neighborhoods. Substitution gives
`Bstar=9·2^84 N d^9` and `C_star=3·2^101 N d^8`.

Fix: none. These subfamilies omit self-contractions and most internal
topologies. `C_safe` cannot replace Cbar; the manuscript does not do so.

**R5. Complete bare majorant and regulated free denominators — PASS.**
Locations: 250–317, equations (13)–(17).

Integrating LGF (21) over t>=delta² after discarding its exponential
gives `16 delta^(-2−m)/(1+m/2)<=16 delta^(-2−m)` for m<=2.
There are respectively `n+1,n+1,n+2,n+2,n+3` edges and
`2n−2,2n−2,2n,2n,2n+2` derivatives. This gives UV exponents
`4n,4n,4n+4,4n+4,4n+8`. Multiplying the family multiplicities by
`n,binom(n,2),n,1,1/2` and the factors `1,1,V,V,V²` reproduces every
coefficient of M2 and M4. Internal pairs and both cubic species are
included; unspecified counterterms are expressly excluded.

For free curvature convergence, the missing second-derivative heat
integral is bounded by
`16 q^-2 integral_(t0)^infinity t exp(−t)dt
=16 q^-2(1+t0)exp(−t0)`.
For t0>=1, `exp(t0)>=t0^4/24` gives
`768 q^-5 delta^6<=768·32^5 delta^6<2^35 delta^6`.
Four scalar terms per curvature entry and six entries per row give the
operator error `E=2^40 delta^6`. The continuum norm is at most 16,
so the regulated norm is at most 17 on the declared delta interval.
Three cycles, four telescoping positions and trace dimension six cost
`48d·24E·17³<2^23 dE`; the covariance costs
`12d E(32+E)<2^9 dE`. Thus both errors in (14) and their half-margins
are correct for every `0<delta<=2^-20`, not merely the endpoint.

The resulting reciprocal factors are `2^18/(3d)` and `2^10/(11d)`
for D4 and D2 respectively, proving (15). Both leading regulated
coefficients are positive. Consequently (17) holds for the truncated
ratio polynomial. The distinction from the quotient of separately
truncated numerator and denominator is necessary and correctly stated.

Fix: none for the bare diagnostic. It neither bounds counterterms nor
defines the uniform renormalized coefficient.

**R6. Failed uniformization and local subtraction attempt — PASS AS
DIAGNOSTICS; COMPLETE SUBTRACTION OPEN.** Locations: 319–415.

All terms of M4 are positive monomials with UV powers at least 16,
including a nonzero term with power 24. Halving delta therefore grows
M4 by at least `2^16`, and the positive V and V² terms grow with volume.
This particular bound has no positive uniform window. It proves neither
divergence of the renormalized coefficient nor a no-go for subtraction.

Direct integration gives `D_delta(0)=1/(16pi²delta²)`. A self-pair in
the specified SU(2) quartic monomial leaves a quadratic field term;
centring removes its scalar expectation, not that term. Also
`sum_mu |partial_mu D(z)|²=1/(4pi^4 r^6)` and radial integration gives
exactly `(epsilon^-2−rho^-2)/(4pi²)`. The two ghost gauge legs can attach
to a path through all external quadratic insertions, so connectedness
does not remove this internal collision. These observations concern
unsubtracted absolute majorants, not the renormalized tensor sum.

Taylor expansion along tz bounds the remainder by
`|z|_1^(k+1) M_(k+1)/(k+1)!`, and `|z|_1<=2|z|` in four dimensions.
Polar integration then proves (19), with constants `64,64,128/3`.
The needed third-derivative bound in the k=2 case can fail uniformly
when another propagator is singular in the same region. No forest,
finite local terms, gauge identities or IR estimate has been supplied
to repair those intersections. Defining `c_rem=c−c_fin` after existence
of the matched coefficient is tautological bookkeeping, not its bound.

The two Pottel links resolve to the claimed author and topics:
[configuration-space BPHZ](https://arxiv.org/abs/1706.06762) and
[normal products and Zimmermann identities](https://arxiv.org/abs/1708.04115).
I checked their abstract pages for attribution only. No theorem from
either is needed for the elementary Taylor proof or imported to close
the missing gauge-theory calculation.

Fix: B1. The open complementary estimate is exactly the unresolved
scientific task, not a matter of changing an algebraic label.

**R7. Uniform hypothetical coefficient, FLOW rate and scale — PASS
CONDITIONAL.** Locations: 419–461, equations (21)–(24).

Given a matched `|c|<=Cbar`, `x<1/(2Cbar)` gives
`R^[1]>R0/2>3/(676d)`. FLOW 425–429 and 433–453 supply the stated
E_m only under their named hypotheses. If `v=b_*m` and E_m<=v/2,
then `u>=v−E_m` and
`|1/u−1/v|<=E_m/[v(v−E_m)]<=2E_m/v²`.
Multiplication by c proves (22). Since E_m=O(log m) and
`v=B log(1/lambda_m)`, (23) follows for the isolated first correction.
It is not an asymptotic estimate on an unbounded remainder.

The sufficient requirement `v>4 Cbar` implies the coupling window.
For L>=3, `pi²<16` and `log L>1` give `b_*>11N²/192`; thus
`m>768 Cbar/(11N²)` is sufficient for this requirement. The separate
E_m condition still needs the supplied FLOW constants. FLOW 4833–4851
retains open UNIV inputs, as the manuscript states.

Fix: after B1, supply the actual Cbar in this threshold. Keep all FLOW
conditions explicit and distinguish the isolated correction's rate from
the full ratio's error.

**R8. Named remainders and fixed-scale lower witness — PASS CONDITIONAL.**
Locations: 463–529, equations (25)–(29).

For x<=1/2, `log(1/x)<=1/x` gives
`Hx²[1+log(1/x)]<=(3H/2)x`. The positive exponential series gives
`Jexp(−S/x)<=2Jx²/S²<=(J/S²)x`. Hence the remainder is at most
`Tx+eta`; the thresholds in (27) bound it by 1/4 while bounding
`|c|x` strictly below 1/2. The ratio is therefore greater than R0/4.
Q-LOW independently gives `Q>=A2 x²/2`, so
`P=RQ²>A4x^4/16`. The factor 1/16 in (28) is correct.

At one fixed m_star the same trajectory's upper u bound produces the
strictly positive constant in (29). Along the common moment-convergent
sequence the limit has at least that constant, still positive; no
moving-scale witness or continuity of a ratio at Q=0 is used. CUMUL
392–425 and 526–556 supply precisely this conditional interface.
The fourteen conditional terms and terminal integration are required
by K4MATCH 107–140 and 159–174; the manuscript includes them in its
producer accounting. A positive fourth cumulant excludes Gaussianity
of the named e field, but not a free theory's quadratic composite e.

Fix: none to the sufficient formulation. B2 is necessary for an actual
YM conclusion, while the author brief only requests that this missing
remainder be named. No instanton action or nonperturbative bound is
assumed as an established input.

**R9. Evidence and resource controls — PASS WITH ALGEBRAIC SCOPE.**
Locations: 531–559 and `checks/k4corr2_*`.

All ten source hashes in `k4corr2_sources.json` match the current files.
All three source hashes in the recorded run receipt match the criteria,
checker and runner. Current timestamps place the criteria before the
checker and run. The saved stderr is empty; the saved result contains
97 passing assertions and separately marks both scientific targets
`OPEN / NOT PASSED`. The checker tests exact rational/combinatorial
identities; its scalar polynomial controls are not YM values.

At 2026-10-30T05:40:03Z I reran all registered assertions in memory.
Their full check records, graph records and scientific-completion fields
exactly matched the saved run. The additional independent multigraph
implementation checked the same registered count obligations, using
integer weights and no fitted or floating-point scientific decisions.
Its formula and all 20 resulting counts are recorded under R3 above.

The rerun used one serial numerical child, effective nice 20, all five
BLAS/OpenMP thread settings equal to one, and exclusive locks on
`k4corr2`, `k4corr`, `k4match`, `cumul` and `combo`, all opened read-only.
Native free memory was 53%; all load averages were below 2.781.
Combined peak RSS was 43,548,672 bytes, monitored by the parent and
the child's self checks. Pre/during/post guards passed. Elapsed time
was about 0.265 seconds. No pools, RLIMIT_AS, saved-output changes or
failed reviewer run occurred. Resource decimals are telemetry only.

Fix: none. Passing this evidence does not compute a renormalized graph
integral, supply a missing remainder, or confer an audit status.

**Binding fixes and unresolved producers.**

1. **B1 — complete the requested uniform coefficient enclosure.** At
   66–89, 273–275 and 389–409, specify and control the full renormalized
   prescription: tadpoles, insertion/bulk and bulk/bulk collisions,
   compatible intersecting subtractions, finite counterterms and
   symmetry restoration, the infrared limit, and matching to the original
   unflowed clover observable in FLOW units. Enclose the complete
   `D4/A4−2D2/A2`, or bound both coefficients sufficiently, with a finite
   explicit constant independent of the removed regulators and common
   short scale. A bounded `C_rem` in (20) would suffice, but it has not
   been provided. Then instantiate the uniform positive order-h² window.
2. **B2 — before asserting positivity for actual YM, produce the named
   original-law estimates.** Establish (25) and (26), or a sufficient
   alternative such as K4MATCH (24), on the same trajectory and common
   limit, including all source, mixed, terminal, background, large-field
   and exterior terms and the required moment convergence. This is an
   intentionally OPEN downstream obligation; merely naming it correctly
   already satisfies that portion of the present author brief.

The existing OPEN labels should remain. B1 is a substantive uncompleted
calculation, not an editorial fix. The restricted results are honest
partial progress, but they do not complete the requested uniform Cbar
or positive uniform Yang–Mills coupling window.

**Final-version confirmation, same reviewer and session.** The final
568-line manuscript has SHA-256
`f7af21719921a45f7ada8f82ab8a8f2bd1db5d37f86ba282d6b725a452323b25`.
Hashing its first 559 lines reproduces the original reviewed digest
`ac43da911379f72edf03e1efb3cc81eb89db9057737fc53957e87d3f0a9d3865`;
all original line references and scientific findings therefore remain
valid. The sole addition, lines 560–568, accurately links and summarizes
this review, its checks, binding B1 and the downstream remainder scope.
It correctly discloses same-family review and does not claim an audit
decision. This provenance-only addition requires no numerical rerun and
does not change the completion verdict.

VERDICT: HOLD

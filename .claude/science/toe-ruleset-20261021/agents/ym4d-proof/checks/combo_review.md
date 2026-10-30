# Independent hostile review of COMBO

Reviewed on 2026-10-30 UTC under `briefs_q/COMBO/AUTHOR.md` and
`PROCESS_LIGHT.md`. This is a **fresh-context, same-family Codex review**.
I did not author COMBO. Upstream review verdicts and the author's reported
formal-algebra passes were not used as mathematical premises.

Reviewed manuscript: **COMBO.md, 645 lines**, SHA256
`71d004611cbc4ae9cad182ef1ae9ea2982a0a28d74672899c90c8885afb48aed`.
This identity includes the explicit joint-space point-splitting paragraph
at lines 390–403, its positive-time displacement and `tau_split`
clarifications, and the distinction between `d_lat` and the colour count.
All COMBO line references below refer to this version.

**Disposition: LAND at the printed scope. Binding fixes: none.** The union
separator, counterexamples, finite-atomic closure example, limited
finite-moment obstruction, and conditional replacement contract survive
independent rederivation. No actual Yang–Mills estimate, owner contract
decision, unrestricted free-net theorem, existence theorem, or mass gap
is certified by this disposition.

I read the required briefs and manuscript; the relevant WITNESS definitions,
free-side proof, Gaussian example and YM contract with REVIEW_WITNESS;
CUMUL's comparator, reconstruction argument, free coefficient and matching
contract with REVIEW_CUMUL; NONFREE55's definitions, NG1/NG3, canonical
separator and errata with CODEX_REVIEW_NONFREE R2–R5, R7, R10 and R16;
ASSEMBLY55 N0/N1F/N5, PANEL_P1's assembly contract, and the exact consumed
REC_CONT/REC_LIB domains and reconstruction statements. This is an interface
check of the reconstruction library, not a new proof audit of every upstream
continuation lemma. The primary [Dütsch–Rehren paper](https://arxiv.org/pdf/math-ph/0209035)
was opened for terminology and attribution only; no imported assertion from
it supplies a step below.

**1. Same hierarchy, tests and normalization — confirmed.**
COMBO lines 30–105.

The bump's coordinate support radius is `epsilon=10^-4`; adjacent time
supports therefore have positive gap `1-2epsilon`. Every distinct-subset
tensor belongs to the compact off-diagonal part of the flat test space.
Evenness gives `theta f4=f1`, with f4 supported at times greater than one,
and `theta f3=f2`. Thus V_m and B use genuine centred OS norm pairings.
They are different pairs; COMBO keeps their weights distinct.

The cumulant is a polynomial in numerical separated moments. It introduces
no coincident field power. The seven centred coordinates, or all fifteen
nonempty-subset coordinates without centring, suffice. Deterministic
regulator-dependent mean subtraction changes no cumulant of order at least
two. Keeping the multiplicative normalization fixed is a separate condition,
and `Z(a)=1` is stated throughout.

**2. F1 and canonical-mixture exclusion — confirmed.**
COMBO lines 109–198.

For a term `z^(2n)(a_n+b_n log z)`, applying `z^2 d^2-z d` gives
`z^(2n)[4n(n-1)(a_n+b_n log z)+(4n-2)b_n]`. Comparison with the preceding
coefficient of `z^2Y` gives the printed recurrence, including `b1=a0/2`.
Its factorial denominators give convergent differentiated series; the two
choices of a0 and a1 give independent local solutions. Consequently the
actual heat-integral solution has this power/log structure without needing
an unproved selection of its second integration constant.

Finite differentiations, sums and Wick contractions retain integer powers
bounded below and a finite nonnegative maximum log degree. Cancellation can
change the leading power and its mass-dependent coefficient, but cannot
create an inverse logarithm. Scalar covariance removes angular dependence.
If every coefficient vanishes the separated analytic kernel is zero;
otherwise reflection positivity at reflected approximate point tests fixes
the leading sign. Uniform smearing over a fixed compact interval of positive
distances multiplies it by the strictly positive I_gamma.

For integer gamma at least eight, V_m cannot tend to zero. For gamma at
most seven, `lambda_m^(-1/2)V_m` tends to zero. These alternatives exhaust
the defined F1; the zero kernel also fails the AF lower clause. This proof
does not classify arbitrary fields relatively local to a free net.

For mixtures, direct subtraction of the mixed mean gives precisely
`C_mix=integral C_alpha dnu+Var(mu_alpha)`. The additional term cannot be
dropped. Nonnegative reflected pairings and Fatou exclude gamma_alpha at
least eight almost everywhere if V_m tends to zero. On the remaining
components, `r<1` and gamma_alpha at most seven make the common envelope
at most `D r^-7 |log r|^J`. Positive separated smearing and multiplication
by `lambda^(15/2)` give a bound tending to zero, including the finite
constant mean-variance term. Finite mixtures have a common envelope after
reducing r0. Neither arbitrary mixtures without ENV nor divergent mean
variance are included.

**3. Gaussian, affine, tensor and OS clauses — confirmed at their stated
scope.** COMBO lines 94–105, 162–174, 202–237.

In the ring with `z_i^2=0`, the Gaussian subset-moment polynomial is the
exponential of its singleton means and pair covariances. A k-block partition
occurs k! times in the logarithm's kth power, producing exactly the factor
`(-1)^(k-1)(k-1)!`. Its degree-four coefficient vanishes. This remains true
for zero covariance, arbitrary means, affine component mixing and any
Gaussian tensor family. F2 is deliberately elementary and contained in F3
at this generator-level scope. A Gaussian named e hierarchy is caught even
if someone supplies a second, composite description of it.

The transformations `V -> a^2 V` and `K4 -> a^4 K4` follow directly;
deterministic shifts affect only the linear formal-log term. Random shifts
and amplitudes are mixtures, not this affine invariance. Finite tensor
products of canonical theories enlarge the finite species list. For the
explicit Cartesian tensor extension, integration of the uniform angular
power/log expansion leaves either a first integer-power/log term or an
identically zero small-scale pairing. RP fixes the nonzero leading sign.
The separate tensor-envelope qualification is necessary and is present.

The exact common-triple E0' hypothesis matches REC_CONT section 1. For a
partition's continued moment, subtuple gaps are sums of future-cone gaps;
different blocks use disjoint variable slots. Their distributional boundary
products are therefore tensor products. The resulting finite analytic
cumulant has polynomial tube growth. Zero reconstructed boundary implies
zero analytic cumulant by REC_LIB's printed uniqueness theorem; zero on
the Euclidean slice gives the converse by totally-real analytic uniqueness.
This establishes the claimed OS contrapositive under the actual library
hypotheses. The tensor Wick conversion contributes the same invertible
factor to every partition term. No Gaussianity claim is inferred merely
from a two-point function, and no arbitrary-spin reconstruction is asserted.

**4. Finite Gaussian-mixture counterexamples — confirmed.**
COMBO lines 239–283 and 405–410.

Integrating the heat kernel in mass gives
`integral s^2 G_s(r) ds=192/(pi^2 r^8)`. Splitting at `s=r^-1` bounds
the low-mass contribution by `O(r^-5)` and the rest by
`O(r^-8/log^2(1/r))`. The two windows `s in [r^-2,2r^-2]` and heat
time in `[r^2,2r^2]` give the matching logarithmic lower bound. Thus q's
separated smears satisfy both AF clauses.

For amplitude T in {1,2}, the second and fourth amplitude moments are
5/2 and 17/2. Their variance difference is 9/4, yielding exactly (11)
with all three positive pair products. For an independent symmetric
constant T in {-1,1}, cumulant additivity gives `K4(q+T)=1-3=-2`,
while the connected covariance is Q+1. Its added AF contribution is
only lambda^8. Both are finite convex mixtures of affine Gaussian states
on the same hierarchy. Section 4's construction supplies the missing
all-order control: every Gaussian pairing has at most n/2 edges of
singularity degree eight, and bounded amplitudes or shifts only change
exponential combinatorial constants. RP is preserved by the finite
mixture. No clustering or unique-vacuum assumption is present to remove
the random invariant constant. These examples refute convex-hull exclusion,
not the literal union theorem.

**5. The GFF product, logarithmic estimate and K4 — confirmed.**
COMBO lines 287–326.

The heat representation gives
`integral G_s(r) ds=1/(pi^2 r^4)`. Since h is at most one, the part below
`r^-1` is bounded by `G_0(r) r^-1=O(r^-3)`. Above that cutoff, h is at
most a constant divided by log(1/r), proving the upper bound in (14).
On the stated mass/time windows, the heat exponential has a fixed positive
lower bound, t^-2 contributes order r^-4, the time interval contributes
r^2, the mass interval contributes r^-2, and h contributes order
1/log(1/r). This gives the lower bound. The low-mass upper term is smaller
than the logarithmic term for sufficiently small r.

Independence gives `S2^chi=H^2`, hence the smeared V_m lies between positive
multiples of `1/log^2(1/lambda_m)`. This tends to zero more slowly than
every positive power of lambda_m. At four distinct points, the raw moment
is the product of two Gaussian pairing sums, namely `(A+B0+C0)^2`.
Subtracting the three chi pair products removes exactly the three squares,
leaving `2(AB0+AC0+B0C0)>0`. Integration of this point-kernel identity over
the four slots is valid and retains strict positivity. Replacing those
terms by products of separately smeared H covariances would have been
incorrect; the manuscript explicitly avoids that replacement. Odd chi
moments vanish by the first species' sign symmetry.

**6. Right-endpoint approximation and the uniform E0' bound — confirmed.**
COMBO lines 328–368.

For every mass interval, monotonicity gives
`w_j G_(s_j)(r) <= integral_(I_j) h(s)G_s(r)ds` at its right endpoint.
Thus the entire approximant is dominated by H. To prove convergence,
first restrict to a fixed compact mass interval, use uniform continuity
of G_s there and mesh 1/ell, then bound the omitted tail by its integrable
positive H tail. Increasing total mass and endpoint mass errors do not
invalidate this argument. Each approximant uses ell^2 finite-mass
canonical scalars per species, with coefficients sqrt(w_j); their product
is an allowed finite Wick polynomial. Its growing species count and mass
range are allowed because F1 imposes finiteness on each state, not one
uniform bound on the entire class.

For n=2k the pairing count satisfies
`((n-1)!!)^2/n! = binomial(2k,k)/4^k <=1`. Every term has n H edges.
The universal H bound therefore gives (17), including configurations
where several pairs nearly collide.

For completeness, the constant in (18) survives a careful weight check.
Let P be the orthogonal projection making a closest pair coincide and
d=X-PX. Then `|d|=delta/sqrt(2)` and `|d|_1<=2delta`. Along
`Y=PX+t d`, orthogonality gives
`|X|^2-|Y|^2=(1-t^2)|d|^2<1/2`. Hence
`1+|X|^2<=2(1+|Y|^2)`. Every Taylor jet below order 4n vanishes at PX;
the integral remainder is bounded by `|d|_1^(4n)/(4n)!` times the maximum
derivative of that order. The seminorm at 9n controls that derivative
with the weaker weight exponent 5n/2, yielding exactly the printed
`2^(5n/2)` factor. An arbitrary displacement of length one alone would
not justify this particular factor; the projection geometry does.

Moreover
`product_i(1+|x_i|^2) <= (1+sum_i |x_i|^2)^n`, so the displayed weight
is bounded by the product of n integrable four-dimensional weights.
For delta at least one, the zeroth derivative supplies the same majorant.
These estimates give `D^n n! ||F||_(9n),1`, uniformly in ell. The elementary
inequality `D^n/n!<=exp(D)` gives (19) with one triple
`s=9, alpha=exp(D), beta=2`. S0 and S1 are separately fixed. The same
integrable majorant proves convergence on every E_n by dominated
convergence. No exchange of a singular coincident limit with an unbounded
mass integral is used.

**7. OS positivity and the joint free-composite realization — confirmed.**
COMBO lines 370–410.

For each canonical mass, the reflected covariance is the positive
Laplace-transform square printed in the text. Expanding Wick pairings
gives symmetric tensor Gram forms. Finite canonical composite insertions
have those forms on compact ordered positive-time tests; flat-space
continuity extends them to the admitted OS tests. All OS quadratic forms
are finite sums of moments, so the all-order convergence just established
preserves their positivity. Invariance, reality and permutations pass
termwise. The required common growth bound is supplied rather than assumed.

For the mixed family (psi1,psi2,chi), an insertion has at most two legs.
There are at most n edges and at most `(2n-1)!!<=2^n n!` matchings.
The same proof therefore works uniformly for every label word; the
REC_CONT sum norm over label words introduces no uncontrolled constant.
This supplies mixed RP, not merely separate RP for three fields.

The added point-splitting argument also resolves the possible distinction
between a joint extension and a realization inside the underlying Gaussian
space. On compact ordered positive-time supports choose the displacement
mollifier with positive time component and small enough support to keep
the two new insertions in their original time interval. At a split chi
vertex the two species cannot contract with each other. All same-species
contractions involve other vertices or reflected vertices at uniformly
positive distance. Thus the kernels for the split vector's norm, the chi
vector's norm, and their mixed inner product converge to the same value.
Their squared norm difference tends to zero. This works simultaneously
for finitely many chi insertions. Ordered-test density and the common
continuity bound extend it to every joint OS vector. The psi-only closed
subspace is consequently the whole joint space, and the chi-cyclic space
is a subtheory of the two independent Gaussian fields. The manuscript does
not assert an ordinary pointwise Euclidean random-distribution product.

**8. The finite-moment obstruction has the correct limited quantifier —
confirmed.** COMBO lines 412–438.

Every finite chosen list of separated moment coordinates converges from
chi_ell to chi, because convergence was proved on all E_n. A continuous
function of those coordinates which is zero on every F1 state must vanish
at chi. Since chi satisfies W, no such function can be nonzero at every
W-state. Each fixed ell fails AF's lower clause, while the limit satisfies
it; this also proves the stated discontinuity of an AF-indicator encoding
at this example.

The proof does not show that every OS hierarchy is approximable by F1,
and it does not settle NG1-prime or forbid a finite-moment witness using
additional YM-specific information. These limitations distinguish the
valid new obstruction from the excessive inference identified by
CODEX_REVIEW_NONFREE R16. They are explicit in the manuscript.

**9. N5-COMBO/N1F-COMBO closure — confirmed as a proposed conditional
replacement.** COMBO lines 429–481.

ASSEMBLY55 N5 and PANEL_P1 require one continuous finite-moment witness
null on the named class. K4 is null on elementary Gaussian generators but
not on F1. AF is a countable asymptotic condition. Thus the original N5
is not already met for the whole union; G-FIN precludes a universal
conversion based on W alone.

The replacement fixes the moment tests, bounds and scale before extraction.
For each fixed m, convergence passes the eventual inequalities to
`l_m<=V_m<=h_m` in the same limit state. The tail index may depend on m;
no uniform convergence in m is needed. Only after these coordinatewise
limits does m tend to infinity. Polynomial continuity passes the fixed
absolute cumulant margin. Applying the proved comparator theorem then
gives exclusion. This is not an assertion that non-freeness itself is
closed and does not use a moving scale m_j. Reconstruction and uniform
extension from the determining family remain required.

The optional ratio is continuous on B>0 and passes a limit with a positive
denominator margin. Scale invariance and continuity at the zero moment
tuple would force any globally defined such functional to be constant.
The unnormalized K4 avoids this obstruction. Adoption of the replacement
and of the comparator target is correctly left as an open contract decision.

**10. Shared inputs and incremental YM obligations — confirmed conditionally.**
COMBO lines 483–595.

The bounds `l_m=c_- U_+(m)^(-kappa')` and
`h_m=C_+ U_-(m)^(-kappa)` have the required behavior because U_± grow
linearly in m. The fixed reference coupling, source maps, normalization,
sequence, all-order hierarchy and reconstruction are genuinely shared.
The AF pair (1,4) cannot supply a lower bound for (2,3) without the
additional pair-specific estimate.

I checked the consumed free coefficient directly against CUMUL's
normalization and support argument. Expanding the Wilson trace gives
the quadratic action `u sum(dB)^2/2`; the clover counts give
`q=u^-1 sum_(a,mu<nu) :F_mu,nu^a F_mu,nu^a:`. Curvature covariance is
`Lambda^2(I-2zz^T/|z|^2)/(pi^2 |z|^4)`. A connected four-vertex Wick
graph is a cycle, with sixteen pairings per unoriented cycle and one
colour loop. At the centres the three edge weights are
1/81, 1/256 and 1/20736. Their coefficient is 169/108, but the smooth
coefficient is correctly retained as its integral A_sm. CUMUL's bound
of 1/250 on each normalized matrix perturbation makes the four-factor
relative trace perturbation smaller than 1/60, placing A_sm in
(3/2,5/3); the analogous radial eighth-power bound places B_sm in
(11,13). No point value is substituted for a smooth-test value.

Once the error bracket in (20) is at most one half at one fixed m_star,
`u_k<=U_+(m_star)` yields exactly the positive c4 in (21). With the
separate denominator matching, the lower numerator and upper denominator
give `2A4/(9A2^2)>1/(507d)`. The coupling cancels in this ratio; its own
convergence is unnecessary. These are implications from the matching
inputs, not proofs of those inputs.

The PL-1L sum retains terminal covariance. The four-source analogue is a
derivative of the logarithm of the normalized source integral, which
includes all disconnected subtractions and conditional mixed terms.
Covariance-increment orthogonality supplies no fourth-cumulant slice
decomposition. Four-factor telescoping produces order u^-5 from kernels
of order u^-1 and errors of order u^-2 under the stated uniform support
bounds. The additional PL-4C error gives a vanishing relative power via
U_-(m). The required original-law, source-image normalization, background,
terminal and large-field estimates remain open. LGF and the two-point
source estimates alone establish none of these connected lower bounds.

**11. Execution, provenance and landing boundary.**

No numerical experiment, symbolic-computation script or other scientific
workload was executed by this reviewer. The derivations above are written
mathematical checks; numerical preregistration and workload resource
guards were therefore not invoked. The author's reported 18/18 algebra
checks were not replayed and are not treated as evidence for the analytic,
OS, closure or YM claims. File reads and SHA256 identity bookkeeping were
the only local inspections. Only this review file was created or edited;
no commit, audit, ledger, axiom or coordinator action was performed.

The author added the explicit point-splitting paragraph during review;
the final version identified above was checked after that addition. It
makes the common Gaussian-space realization explicit. The `d_lat` change
also removes a notation collision with the colour count. No binding
mathematical flaw remains in this reviewed version.

The printed open boundaries are essential: arbitrary un-enveloped
canonical mixtures, unrestricted GFF composites, unmarked free-net
embeddings, the full YM observable algebra, actual YM estimates,
clustering, unique vacuum, scattering and a physical mass gap are not
established. Balaban and Dimock retain credit for the constructive YM
program; no estimate from that program has been silently supplied here.

VERDICT: LAND

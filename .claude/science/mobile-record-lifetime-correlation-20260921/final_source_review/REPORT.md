# Complete-source scientific review: lifetime activity and terminal correlations

The new arbitrary-initial tagged-record bounds (6)–(8) and the time-dependent-clock birth budget are mathematically sound under their stated hypotheses. I found two narrow torus-scope qualifications needed for the exact uniform-weight control and the torus-to-lattice limit. Neither finding changes the lifetime or covariance inequalities. No additional unresolved mathematical defect was found in the complete note or runner at the supplied hashes.

This is a source-bound scientific review, not an audit verdict or retention decision. The two qualifications below remain unresolved in this reviewed source; corrective edits have not yet been inspected.

## Findings and narrow corrections

**R1 — The exact uniform-weight departure identity needs the actual degree, or an explicit nondegenerate torus convention.** The model at [note line 45](/Users/jonreilly/Documents/Codex/mobile-record-lifetime-publication-20260921/docs/MOBILE_RECORDS_LIFETIME_ACTIVITY_AND_TERMINAL_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-21.md:45) calls z=2d a degree *bound*, then sets lambda=z kappa. The exact control at [line 314](/Users/jonreilly/Documents/Codex/mobile-record-lifetime-publication-20260921/docs/MOBILE_RECORDS_LIFETIME_ACTIVITY_AND_TERMINAL_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-21.md:314) states departures per site equal lambda(v0−v0²/2)/(12epsilon). This identity uses the actual degree, not merely its upper bound.

For the simple two-vertex periodic quotient in d=1, one undirected edge has rate kappa and actual degree one. Starting empty with W=1 and epsilon=kappa=1, a direct killed-generator reward calculation gives expected departures 1/24 per site. Substituting the declared bound z=2 gives 1/12. The runner tests a four-cycle, where actual degree and the bound agree, so it cannot expose this scope distinction.

**Narrow correction:** specify simple tori with each period at least three, so degree is exactly 2d, or write the exact identity with kappa times the actual degree. All inequalities remain valid with z as a bound. If parallel bonds on side-two tori are intended instead, explicitly define their multiplicities and proposal rates; that convention is not currently stated.

**R2 — State the limiting torus family for the local convergence claim.** [Note lines 307–309](/Users/jonreilly/Documents/Codex/mobile-record-lifetime-publication-20260921/docs/MOBILE_RECORDS_LIFETIME_ACTIVITY_AND_TERMINAL_CORRELATIONS_BOUNDED_THEOREM_NOTE_2026-09-21.md:307) need the qualification that every periodic side length tends to infinity, equivalently that the local injectivity radius diverges. Increasing volume alone is insufficient.

An exact control is W=1 with empty initial data on the 3-by-L tori. Terminal contents are independent uniform marks at distinct torus vertices. The two fixed Z² sites 0 and 3e1 project to the same vertex for every L, so the first-coordinate covariance of their pullbacks is 1/3. On Z² it is zero. Their finite-dimensional laws therefore cannot converge to the Z² law as L grows with the first period held at three.

**Narrow correction:** add “as the minimum periodic side length tends to infinity” to the convergence statement. If the intended family is only (Z/LZ)^d, define that family and state L→infinity. The finite-time coupling plus the uniform late-update estimate then proves the claimed terminal limit.

These are convention/quantifier corrections, not requests for new dynamics, weaker bounds or a new audit. The primary runner need not change to implement either prose correction, although retaining the scope controls would prevent future drift.

## Reconstruction of the new tagged-record argument

Let h_t be the tagged record's predictable accepted-hop intensity. Each move has unit graph length and h_t≤lambda. For a tag started at a specified site, its counting-process generator gives

\[
E[e^{N_t}]\leq e^{\lambda(e-1)t}.
\]

The estimate is valid for history-dependent rates; it does not require independent increments for N_t. With c=lambda(e−1)+gamma,

\[
\Pr(N_t>ct)\leq e^{-\gamma t}.
\tag{R1}
\]

When N_t≤ct, the tag is within graph distance floor(ct) of its starting site. Every possible vacancy destination then lies in the ball of radius floor(ct)+1. Its cardinality is bounded by (2floor(ct)+3)^d≤(2ct+3)^d, on Z^d and on the periodic quotient. Using the uniform marginal vacancy estimate with v_*=1, rather than conditioning a vacancy marginal on the tag location,

\[
\begin{aligned}
E[h_t]
&\leq\lambda\Pr(N_t>ct)
 +\lambda\sum_{y\text{ in destination ball}}\Pr(y\text{ vacant at }t)\\
&\leq\lambda\{1+A(2ct+3)^d\}e^{-\gamma t}.
\end{aligned}
\tag{R2}
\]

This proves (6). The factor counting possible destinations is necessary precisely because the tag and vacancy field can be dependent. The proof does not use a conditional vacancy-density bound at a random location. Its coefficient lambda is conservative: a direct sum over candidate destinations can in fact keep kappa in that term, but the displayed larger coefficient is valid.

Integrating (R2) and using integral_0^infinity t^k e^{−gamma t}dt=k!/gamma^{k+1} gives (7), including its separate lambda/gamma term. No sign or normalization error was found. The constants can be large without invalidating finiteness.

For the tail (8), a rate-lambda domination yields factorial moments E[(N_T)_m]≤(lambda T)^m, also valid for adapted intensities. Therefore

\[
\Pr(N_T\geq m)\leq\frac{(\lambda T)^m}{m!}
\leq\left(\frac{e\lambda T}{m}\right)^m.
\]

At T=m/(2e lambda) this is at most 2^{−m}. On the remaining event, N_infinity≥m requires at least one accepted tagged hop after T. Its probability is at most the expected number of such hops, bounded by the tail integral of (R2). This gives exactly (8). A displacement of m also requires at least m hops, so the stated maximal-displacement implication is valid.

For later records the restart must be at the site-indexed birth stopping times described in the note. The fixed-rate marked construction is strong Markov; conditional on the post-birth configuration, the same constants apply. Initial tags and these births form a countable family. Finite conditional expectations therefore imply finite hopping for every record simultaneously. This is a separate argument from site fixation, and the note correctly distinguishes them. The lambda=0 case is correctly separated.

The proof relies on the polynomial volume of the search ball and a uniform positive birth-hazard floor. It is not being extended here to arbitrary graphs of exponential growth, clocks without a floor, occupied-occupied motion or additional variables.

## Time-dependent clock budget

The extension at lines 126–135 is valid for its well-defined, translation-covariant finite-range capacity-one process with translation-invariant initial law, locally bounded-in-time rates, conservative motion and nonnegative insertion. On every finite time interval the local compensator identity applies. Translation cancels the expected conservative flux; reflection symmetry and a product law are unnecessary. If B_0(t) counts births at 0,

\[
E[B_0(t)]=v_0-v(t).
\]

The left side is nondecreasing and the right side is bounded by v0. Monotone convergence gives E[B_0(infinity)]=v0−lim_t v(t)≤v0. No positive floor or time integrability assumption is needed for this budget alone. Spatial translation covariance and the absence of removal/export/new capacity are load-bearing; a merely sitewise bound does not supply the flux cancellation in an inhomogeneous law.

A separate exact counterexample checks the note's separation from lifetime hopping. On a three-cycle start with a uniformly located vacancy and two permanent records, so v0=1/3 and the law is translation invariant. Set W=1, kappa>0, epsilon(t)=a on [0,1) and zero thereafter. Before the cutoff the vacancy's kill rate is the constant 6a. Thus

\[
v(\infty)=\tfrac13e^{-6a},\qquad
E[B_0(\infty)]=\tfrac13(1-e^{-6a}).
\]

With probability e^{−6a} there is still a vacancy at the cutoff. Thereafter the two labeled records and vacancy form an irreducible finite six-state hopping chain, and both records make infinitely many hops. The time-dependent birth budget holds while tagged fixation fails. This example satisfies the budget extension's local rate hypotheses and has no positive formation floor, exactly as the note distinguishes.

## Remaining source coverage

I read the complete 380-line note and 317-line runner at the stated hashes, including the model, scope exceptions, provenance and executable claims.

- The marked construction is local and has bounded branching at finite backward times. Its birth rejection rule produces epsilon times the correct local product; its hop rule uses only the endpoints and their neighbors. No infinite pair product is required.
- The translation-invariant vacancy derivative, per-site birth budget, incident-update count and mass-transport record bound are correctly normalized. In particular, the departure intensity in (5) needs only lambda v(t), while incident updates use 2lambda v(t).
- The killed vacancy-label exponential estimate is valid without independence of path and survival. The geometric sum is (1+4lambda/alpha)^d, and the chosen exponent gives gamma=alpha/2. The estimates and coordinate-displacement sums remain uniform on the tori as upper bounds, including cases of smaller actual degree.
- The dependence-path rate Lambda=(z+1)(beta+2z kappa) correctly overcounts birth and edge footprints. Backward steps have length at most two. The escape depth floor(R/2)+1, the choice R=floor((D−1)/2) and m=ceil(D/4) are consistent. Disjoint induced balls use independent inputs only for spatial product initial laws.
- Comparing moments and means gives the factor 8 in (9). The time choice and m≥D/4 yield the exponent gamma D/(8e Lambda) in (10). The trivial covariance bound M_f M_g is valid, including complex functions with the stated convention. Summability and the centered single-site/vector variance consequence follow from uniform bounded observables and polynomial shell growth.
- The uniform-weight product evolution, two-site site-reuse probability and geometric first-record hop count are correct with actual degrees. The shared-random-content example correctly separates translation invariance from spatial independence. The empty-start untouched-clock argument correctly rules out a finite global filling time on the infinite lattice. Fixed-parameter limits and the lack of a physical time/field identification are stated conservatively.
- The finite runner constructs the real full four-cycle generator and solves absorption equations. Grouping by content multiset is legitimate for that solve even if a motion sector were disconnected: positive killing at every nonfull state makes each solve well-defined. The reported residuals do not masquerade as a proof of an infinite-volume conclusion. The mutation branches are targeted controls, not independent mathematical evidence.

The axiom memo was read for the claimed clock/acceptance boundary; it does not supply this stochastic dynamics or a physical time conversion. No effective audit status or external PR state was inferred from this review.

## Executed evidence and limits

`PRIMARY_BASELINE.log` reproduces **24 passed, 0 failed**. The four-cycle neutral terminal covariances were approximately 0.05508072, 0.05484070 and 0.05446237 at kappa=0,1,5; the flat control was 3.45e−18. The largest displayed harmonic residual was 7.66e−15. I inspected the eight mutation branches but did not rerun the already reported mutation campaign.

`independent_check.py` imports no primary source. It builds a distinguished content-zero tag on a three-site induced path with all six insertion contents and a positive symmetric matrix without a row-sum constraint. Local edge-factor cancellation generates 147 states, of which 39 are transient. Exact reward equations and marked-count recursions give finite means and four exact tail thresholds for every initial tagged state. The largest mean is approximately 0.16102465; the theorem's conservative bound at those parameters is 43.35898. This finite inequality is not a certification of the infinite theorem; the reconstructed proof above is the load-bearing evidence. An exact two-site calculation separately recovers the geometric ratio 5/61 and mean 5/56, including six tail thresholds.

The independent suite also counts possible tag destinations, differentiates the explicit polynomial-exponential tail integral in dimensions one through three, verifies the cutoff-clock budget and residual motion chain, and supplies the two exact torus-scope witnesses above. All checks passed on Python 3.13.5 and SymPy 1.14.0. `INDEPENDENT_RESULTS.json` and `INDEPENDENT_RUN.log` are byte-identical.

The earlier activity and correlation reports match their sealed originals byte-for-byte. Their identities, the full primary source identities, instruction/reference identities and all review evidence hashes are recorded in `SEAL.json`. No primary source was changed. No independent audit, external literature/PR-status investigation, full timestamp/quantum-interface check or exhaustive new infinite-system certificate was performed or claimed.

The next required check is limited to the two affected torus qualifications and the final source hashes. The new tagged-record proof and the clock-budget extension do not require mathematical changes.

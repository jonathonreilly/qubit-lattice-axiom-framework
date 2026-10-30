**Independent hostile review of TQ2.md — 2026-10-30.**

The note can land as a **conditional research reduction with both route
verdicts UNDECIDED**. I found no blocking error in its pressure theorem.
It supplies neither the actual Wilson no-cusp estimate nor the extensive
source comparison. LAND does not certify H_Euc for Wilson theory,
Yang–Mills existence, a mass gap, or any formal audit status.

This review follows `briefs_q/TQ2/REVIEW.md` and PROCESS_LIGHT. All target
line numbers refer to the complete 650-line TQ2.md with SHA-256
`3d9342a392f01d3e705e5fe381ca88aed20e4dd06c8138751be23e768e96e38a`.
The workspace has no Git metadata; this is a filesystem-snapshot review.
I am a fresh same-family Codex reviewer, independent of authorship. The
author log disclosed an earlier review and its LAND disposition; I did
not read that report or use its verdict to establish any implication
below. This is not a claim of blinded or cross-family review.

| Item and TQ2.md lines | Verdict | Fix or disposition |
|---|---|---|
| Target, observable prescription and common domain, 30–93 | CONFIRMED, conditional | No fix. ALG/SEQ, matched subtractions and the all-order extension remain application inputs. |
| Proposition T and unbounded-observable qualification, 97–125 | CONFIRMED | No fix. Preserve both all-data suprema and the actual truncation/tail requirements. |
| Rotation/shape averaging and RP, 127–160 | CONFIRMED at the stated scope | No fix. AN is sufficient, and equivalence requires the same-limit Haar-average identification. |
| Bounded separated four-point example, 162–179 | CONFIRMED | No fix. It tests an abstract inference, not the Wilson premise set. |
| Extensive product source and pressure derivatives, 183–211 | CONFIRMED under LOC | No fix. Fixed-cutoff boundedness is not a uniform continuum source bound. |
| Period-independent pressure limit, 213–260 | CONFIRMED under LOC at fixed cutoff | No fix. The constants may diverge with the cutoff; local-moment independence does not follow here. |
| Surface-bias counterexample, 262–280 | CONFIRMED at its two-state scope | No fix. It does not establish Wilson phase coexistence or a Wilson obstruction. |
| NC/PC, common diagonal, Euclidean extension and torque implication, 284–390 | CONFIRMED, conditional | No fix. COMMON and the compatible free selection are essential; U-all is additionally needed for the torque conclusion. |
| IR response distinction, SUS and covariance normalization, 392–431 | CONFIRMED | No fix. SUS is only sufficient, and includes tilted, overlapping-support covariances. |
| Real-source admissibility and moving radii, 433–466 | CONFIRMED; optional wording clarification below | At 465–466, specify a thermodynamic cusp whose slope jump stays bounded away from zero along the cutoffs. This is not a binding change to MS or its theorem. |
| Clipped sources and TAIL, 468–485 | CONFIRMED, conditional | No fix. The tail condition must hold on the same diagonal in every compared orientation. |
| SP/VAC imply PC, 489–538 | CONFIRMED, conditional | No fix. Retain the source-dependent scalar difference and volume-uniform all-data bounds. |
| Incompatible separate limits and prescribed sequences, 540–559 | CONFIRMED | No fix. The proof selects a sequence; it does not repair an arbitrary preselected one. |
| Signed torque alternative and sphere comparison, 561–607 | CONFIRMED, conditional | No fix. Preserve REVIEW_N5B's HOLD and its actual-law versus uniformly conditional distinction. |
| Strength, open estimates and route/audit status, 3–26 and 609–650 | UNDECIDED/OPEN supported | No fix. No actual YM supplier, exhaustive obstruction, new axiom or audit promotion has been established. |

**Independent calculations supporting these verdicts.**

For the geometry in (1), change coordinates by Q inverse in the (Q,I)
regulator. This bijects links and plaquettes, preserves the Wilson action
and product Haar measure, changes the periods to RQ inverse Z^4, and
transports the prescribed F_Q approximant back to F. Adding and
subtracting its expectation gives exactly (1), including the sign of
the period term. For the chosen Q, R/a divisible by 10 makes these
period vectors integral and even. It does not make Q an isometry of the
original embedded cubic torus. In particular J(x+Rz)−Jx=RJz need not
vanish. The note correctly preserves the second comparison obligation.

The centering warning is substantive. Differentiating
E[product_i(X_i(s)−c_i(s))] contributes, besides the derivatives of X_i,
−sum_i c_i'(s) E[product_(k≠i)(X_k(s)−c_k(s))]. For two factors each
remaining expectation vanishes when c_i=EX_i. For three or more factors
there is no such general cancellation. Lines 87–93 avoid importing a
pair identity into the all-product pressure construction. LOC also
requires the approximant itself, not just its support, to be independent
of the volume/period prescription once embedded.

For Proposition T set d=log Z_1−log Z_2−c and let rho_2 be the normalized
second coarse density. Then

    rho_1/rho_2 = exp(d) / E_(rho_2)[exp(d)].

The assumption |d|≤delta_d bounds this ratio between exp(−2delta_d)
and exp(2delta_d). The expectation difference splits into the integral
of h_1−h_2 against rho_1 and the integral of h_2 against rho_1−rho_2.
Their bounds are delta_c and M(exp(2delta_d)−1), respectively. Summing
the per-block polymer norm yields delta_d≤N_b eta without a covariance
estimate. The hypotheses remain substantial: kernel normalization alone
does not prove either supremum. For truncations, add the two actual tail
expectations to the bounded comparison. The inequality
E[|Y|1_(|Y|>M)]≤M^(−delta) E|Y|^(1+delta) proves the stated sufficient
tail condition; separated-distribution bounds do not supply it.

Haar averaging gives invariance by a change of the group integration
variable. Conversely, an invariant S is unchanged by its Haar average,
so equality with that particular average is equivalent to invariance.
An independently invariant limit need not be this average: two distinct
invariant functionals already show why its invariance alone cannot make
AN necessary. Positivity and fixed-plane RP pass through an integral
of their respective nonnegative quadratic forms when every component
has those forms on the same domain. General rotations change the
reflection plane, so coordinate-plane RP alone does not justify this
argument. These are sufficient conditions, not an impossibility theorem
for every averaging construction.

For (3), each of the four axes contributes two atoms of mass 1/8.
Consequently E(v·X)^2=sum_i v_i^2 and E(v·X)^4=4 sum_i v_i^4.
At v=(3,4,0,0)/5 the latter is 4(81+256)/625=1348/625, whereas the
axis value is 4. For the averaged radius-2 law, reflection symmetry
kills the odd mixed terms. A 45-degree rotation yields mu=3nu, and
16=E|X|^4=4mu+12nu gives mu=2. Distinct spatial supports do not change
these moments for a constant field. Thus even isotropic pair moments
and bounded moments at every fixed order do not settle all orders.

The factors in (4)–(5) are correct. Write N=V/a^4 and A=a^4 sum_x Y_x.
At fixed cutoff all terms are bounded, so differentiation under the
finite Haar integral is valid. Translation invariance gives

    p'(0)=E[A]/V=a^4 N E[Y]/V=E[Y],
    p''(t)=(E_t[A^2]−E_t[A]^2)/V.

The real tilt remains translation invariant because A is. Sourcing the
whole product is what makes its n-point moment a first derivative.
There is no claim that differentiating a one-point pressure once can
recover that product, or that its real tilt lies in SRCCD's source norm.

I rebuilt the thermodynamic-limit argument, including the gauge-link
factorization. At fixed a,F, enlarge the interaction range d to include
the plaquettes. Assign each positively directed link variable to its
initial vertex. Inside a large period parallelepiped retain complete
axis-aligned b-cubes. Removing interactions crossing cube faces costs
at most a constant times L^4 d/b anchors; discarding the outer strip
costs a constant times (b+d)L^3. Fixed rationally tilted faces change
the constant, not the power of L. All retained interactions belong to
one cube, so the unconstrained link-Haar integral factorizes. Unused
link integrals are one. Gauge invariance imposes no additional constraint
on this original link integration.

Each removed interaction has bounded magnitude at fixed a and bounded
t. The sup bound on the action difference therefore bounds the log
partition-function difference. Applying it to both t and zero and
dividing by physical volume gives the error C(d/b+b/L) in (8), including
the missing-volume error. For each fixed b, the limsup and liminf of
the large-torus pressure lie within C d/b of the same free-cube
pressure. Their difference tends to zero as b grows. Comparing two
period orientations through this same cube proves equality of their
limits. Finally |p(t)−p(s)|≤M_(a,F)|t−s| upgrades pointwise convergence
to compact-t uniform convergence by finite nets. Nothing here controls
the growth of M or the boundary constants as a tends to zero.

For (9), the two partition sums are 2cosh(tV±H_R), normalized at t=0
by 2cosh H_R. Their derivatives at zero are ±tanh H_R. The
1-Lipschitz bound on log cosh gives the pressure difference at most
2H_R/V. Also

    |p_(±,R)(t)−|t|| ≤ 2H_R/V + 2 log(2)/V.

Thus both pressures converge to |t| while their zero-source moments
converge to opposite signs. This example tests the pressure-to-moment
inference. Its hard two-state constraint is outside the bounded
finite-coupling Wilson premise set, exactly as the text acknowledges.

The essential transfer in (11) and (13) is a convex secant sandwich,
not interchange of a derivative and two limits. For each fixed t>0,
convexity gives −p(−t)/t≤p'(0)≤p(t)/t. If two finite-volume pressures
are each within d_j of the same thermodynamic pressure q_j at both
signs, both derivatives belong to

    [−q_j(−t)/t−d_j/t, q_j(t)/t+d_j/t].

Their difference is at most [q_j(t)+q_j(−t)+2d_j]/t. This proves (11)
with d_j=1/j. Enumerating observable/frame/source triples imposes only
finitely many convergence thresholds at each a_j; a compatible cofinal
choice of R_j can exceed all of them and j. Every fixed triple is
eventually included. Taking j to infinity at each fixed t_l, and only
then l to infinity, is exactly NC's order of quantifiers.

For (13), transport of the entire anchor sum gives
p^Q_(a,F_Q)=p^I_(a,F). PC applied to F_Q bounds the thermodynamic
pressure of the rotated test on the I grid by that same p^I_(a,F),
up to epsilon_(j,F_Q) at each sign. Bounding the rotated derivative
above and the original below costs epsilon at +t; reversing the two
costs epsilon at −t. This is why the maximum of the two errors, rather
than two unexplained epsilon terms, suffices. The two finite-volume
errors still contribute 2/j. NC and PC then make the difference vanish
for every required product on the one selected diagonal.

COMMON must supply moment extraction, the actual completed test domain,
compatible covariant approximants and equicontinuity on this selection.
Subsequences preserve the endpoint equalities. To check the angle without
assuming a named number-theoretic result, define P_0(x)=2, P_1(x)=x,
P_(n+1)(x)=xP_n(x)−P_(n−1)(x). These are monic integer polynomials for
n≥1 and P_n(z+z^(−1))=z^n+z^(−n). If z=(3+4i)/5 had finite order n,
6/5 would solve the monic integer polynomial P_n(x)−2. Substitution of
a reduced rational p/q into such a polynomial forces q to divide p^n,
so q=1, a contradiction. Pigeonholing powers on the circle supplies
arbitrarily small nonzero angles; their integer multiples approximate
every angle. Hypercubic conjugations provide all coordinate-plane
circles, and successive plane rotations eliminate an orthogonal matrix
to a diagonal one. These generate SO(4); a reflection adds O(4).
Continuity extends the equalities to the full domain. Approximating a
fixed translation by lattice translations uses the stated equicontinuity.
Uniformity on compact test/motion families likewise requires that common
modulus; pointwise convergence alone would not suffice.

With U-all, integrating S_j'(s)+tau_j(s,r_F)=e_j(s,r_F) gives

    integral_0^theta tau_j ds
      = S_j(0)−S_j(theta)+integral_0^theta e_j ds.

This proves (14) at the one fixed admissible shell. The last integral
is bounded by theta times the remainder supremum. No convergence of
derivatives or intermediate-angle stresses was smuggled into this
endpoint argument. Without U-all, the pressure proof establishes only
the moment equalities, not the proposed stress representation.

For SUS, twice integrating p'' gives the triangular-kernel formula in
lines 411–413. Its kernel has total integral t^2, hence the secant width
is at most K_F t. Translation invariance under the tilt also gives

    Var_t(A)=a^8 sum_(x,y) Cov_t(Y_x,Y_y)
            =V a^4 sum_y Cov_t(Y_0,Y_y),

which verifies (15). Uniform absolute summability would indeed be a
stronger sufficient response estimate. It involves overlaps as well as
large distances, so separated SRC bounds cannot provide its full
content. For p(t)=|t|^(1+alpha), the secant width is 2t^alpha and the
second derivative away from zero is alpha(1+alpha)|t|^(alpha−1).
This verifies the stated analytic distinction without representing it
as a Yang–Mills pressure calculation. The unbiased constant-sign law
also verifies that an invariant state can retain a source cusp.

For the Gaussian tail warning, x^2≥1/t implies
t x^4−x^2/2≥t x^4/2. Thus the positive quartic real source is not
integrable although every polynomial moment is. Fixed-cutoff compactness
does not fix this continuum issue. In MS the same secant proof is valid
provided all pressures needed for F and F_Q are controlled at the
**actual radius t_(j,F)** with error at most t_(j,F)/j. At stage j this
is still a finite set, including both signs and the transported labels.
One must not use the potentially different radius assigned to F_Q
instead; lines 454–456 explicitly retain this requirement. Dividing the
SP/VAC bound by that radius is equally necessary.

The optional wording clarification concerns only the final sentence at
465–466. For a convex thermodynamic pressure, its symmetric secant width
is at least p'_+(0)−p'_−(0). A slope jump bounded below along the cutoffs
therefore obstructs MS at every choice of radii. A cusp appearing only
after the cutoff limit is different. For example, with delta_j decreasing
to zero, q_j(t)=delta_j log cosh(t/delta_j) converges to |t|, but at
t_j=delta_j^2 its symmetric secant width is
2 log cosh(delta_j)/delta_j≤delta_j, which tends to zero. The inequality
follows by integrating tanh x≤x. This analytic family is not a Wilson
example. Suggested wording: shrinking radii cannot overcome a
thermodynamic slope jump that stays bounded away from zero along a_j.
The note's actual cusp example (9) has exactly that property, and none
of the conditional conclusions relies on the broader interpretation.

Clipping preserves the local support and commutes with translations
and exact geometric transport of a real observable. It suffices to
enumerate integer clipping levels M in addition to the other labels.
For each fixed M the pressure theorem compares the clipped moments.
The original moment difference is bounded by that comparison plus
the two tail differences. Take limsup on the same diagonal and then
M to infinity; TAIL removes both remaining terms. Absolute uniform
integrability is sufficient but is not necessary for the signed
expectation condition displayed in the note. No clipping operation on
an unconstructed continuum algebra is used.

For the extensive comparison, let Q_G(t)=integral Z_G,t(V_c) dV_c.
Forward kernel normalization makes this the fine partition function
with the actual extensive source. SP implies

    log Q_I(t)−log Q_Q(t)=c(t)+r(t),  |r(t)|≤N_b eta(t).

Subtract the same formula at zero source and divide by V. The absolute
difference of the normalized pressures is at most

    |c(t)−c(0)|/V + (N_b/V)[eta(t)+eta(0)].

VAC gives (16) and its vanishing thermodynamic bound. A scalar depending
on the source survives this subtraction; discarding it would invalidate
the inference about moments. The proof needs no coarse covariance, but
SP is stronger source-level information than Proposition T for one
bounded observable. All coarse data, real-source domains, volume
uniformity and the observable prescriptions are left explicit. No
finite-volume RG result has been promoted to this new supplier.

The arrays aR and 1/(aR) have the two advertised separate limits and
product one. They therefore refute the general inference that those
limits always have a common vanishing diagonal. They are not Wilson
error estimates. The freely chosen volume-first sequence in section 4
is justified by its stronger assumptions, not by interlacing the old
cutoff-first statement without an overlap estimate.

For the torque alternative, write its exact fine shell as
sum_x a^4 c_(mu,nu)(x) T_(mu,nu)(x). The discrete product rule bounds
the coefficients independently of the large shell radius and gives
support in the enlarged annulus. Its physical lattice volume is O(r^4).
The displayed actual-site covariance bound then gives O(r^(−epsilon)),
uniformly on the rotation path. Integrating the Ward identity at each
fixed r and subsequently taking r large proves the sufficient endpoint
condition, with the corresponding U-all remainder estimates at those
fixed shells. Without distance information the same absolute counting
gives only O(r^4). This makes decay sufficient, not necessary; signed
cancellations remain possible.

For the sphere statement, apply total covariance successively along
the specified positive Markov chain:

    Cov(F,S)=sum_(i<k) E Cov(F_i,S_i | U_(i+1))
             +Cov(F_k,S_k).

For any scalar c, the terminal covariance is bounded by
||F_k−EF||_2 sup|S_k−c|. After the prescribed normalization this yields
delta(J)+C(J)tau_R(a,J). Choose J to make delta small, then a small
enough at that fixed J to suppress the other term. Neither a uniform
bound in J nor a moving-J rate follows. The L2 norm and fine covariance
sum are still averaged under the actual law. TQ2 correctly retains
REVIEW_N5B's distinction: all-data seam transparency does not turn
these two inputs into uniformly conditional estimates. Nor does this
observation prove that their averaged versions require infrared decay.
A global Killing field removes the continuum radial cutoff shell on
the sphere; it does not remove its regulator seam or identify its state
with a flat periodic Wilson selection.

**Source and scope checks.** The locators below were inspected in the
actual files, including the relevant corrections, rather than accepted
from status labels.

| Source | Passages relevant to the target |
|---|---|
| TQ.md | 28–153, 155–199, 203–313, 385–560: normalizations, fine identity, comparison, period transport, exact all-order endpoint target and scope. |
| REVIEW_TQ.md | 1–190 and 237–369: LAND is conditional; all-order U-all/TQ-min and the fixed-volume limitations survive. |
| UNIV55.md | 63–198 and 686–713: torus geometry, Proposition T, per-block factor and the unnormalized formulation. |
| CODEX_REVIEW_UNIV.md | 18–114, 196–212 and 482–497: comparison confirmed, necessity of summability rejected, conditional locality and the torus group caveat retained. |
| ROTDEF.md | 116–210, 278–439 and 647–679: prescribed clover observable, Haar identity, shell coefficients, original I5 clauses and E4–E6. |
| SRCCD55.md | 315–435, 921–956 and 990–1017: mixed insertion order at 358–359, SRC-E′, source norm, contacts and errata. |
| CODEX_REVIEW_SRCCD.md | 226–310: corrected averaged decay/rate, missing product-image moment and allowed contact. |
| ASSEMBLY55.md | 132–203, 275–316 and 499–504: common domain/sequence, all-product N4, limited N10/N11, OPEN N12/N14 and sphere F13. |
| N5B.md | 23–84, 126–213 and 475–583: actual seam, direct-cut hypotheses, ST/CD-K/IMG-K, open transfer and route status. |
| REVIEW_N5B.md | 1–168 and 379–436: HOLD is the advertised UV-only quantifier defect, not failure of the covariance inequality or a sphere NO-GO. |
| PANEL_P2.md | 25–69: fixed-plane RP convexity, explicit averaging failure and the coordinate-plane group argument. |
| AUDIT.md | 75–150 and 183–195: FT occurs in the five declared flat chains; SS/SP/SR are open sphere interfaces, and route counts are not independent obstruction counts. |

In particular, the brief's phrase about the coarse law not entering is
supported only in the qualified comparison sense explained in
CODEX_REVIEW_UNIV: no separate coarse-correlation estimate is used once
the all-data comparison hypotheses hold. TQ2 does not repeat the stronger
rejected claim that kernel normalization itself eliminates all long
modes. It does not use the refuted fine-moment SRC-E, silently promote
SRC-E′ into repeated-support bounds, or count SRC-κ's two further
insertions as an all-order Ward theorem. The source comparisons contain
no located quotation or substantive scope mismatch requiring repair.

The pressure inputs are named new mathematical hypotheses about the
supplied Wilson model, not adopted physical axioms. Their application
remains OPEN. Invariance of an already selected zero-source state does
not by itself bound responses to extensive tilts or conditional weights
at every coarse datum. Failure of NC, SUS or the particular comparison
supplier therefore would not exclude every flat selection or route.
The note appropriately retains signed-torque and same-state alternatives
and makes no claim that a mass gap is either proved or necessary.
Method credit to Tadeusz Balaban and Jonathan Dimock is preserved. No
external literature theorem or recalled result carries a proof step
in this review.

All 16 entries in `checks/tq2_sources.sha256` matched the inspected
snapshot. The 3,772 original regular files in the author manifest also
matched, and the only six additional files before this report were the
listed TQ2 author artifacts. The author log, validation receipt and
current target agree on its source hash. These are integrity checks,
not independent authentication of historical execution or scientific
evidence for NC/PC. No scientific numerical experiment, symbolic
program or old numerical runner was executed; the checks above are
written derivations. The read-only integrity process used nice -n 10,
python3 -B, all seven thread variables set to 1 and no pools. Its
observed load1 was 1.7271, free memory 51%, priority 20 and peak RSS
25,395,200 bytes. No address-space resource limit was set.

**Binding fixes: none.** The cusp wording refinement above is optional
and does not alter the theorem. The missing Wilson estimates remain
COMMON plus NC/PC, or the stated moving-radius/clipping variants with
their actual auxiliary conditions; SP/VAC are a proposed supplier of
PC. U-all is additionally required to identify TQ-min. These open
application inputs are not being turned into a requirement to solve
Yang–Mills before this conditional research note can land.

Only REVIEW_TQ2.md was created. No other file was edited, no commit or
landing action was performed, and no audit status was assigned.

VERDICT: LAND

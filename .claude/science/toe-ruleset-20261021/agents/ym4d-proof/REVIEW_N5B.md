# Independent hostile review of N5B

**Disposition: HOLD for the quantifier correction in item 1.** The sphere-route
verdict **UNDECIDED** is justified. The covariance reduction is valid, and the
missing Yang–Mills estimates are honestly OPEN. The defect is narrower: the
displayed averaged hypotheses do not establish the advertised description of
the whole reduction as using only integration below fixed reference scales.
This can be repaired by narrowing that description or explicitly stating its
stronger conditional hypotheses; proving the outstanding YM estimates is not
a condition of landing this scoped assessment.

I am a fresh, same-family Codex reviewer, independent of the authorship of
N5B and its checks. This is a review, not an audit or a retained-status grant.
The controlling instructions are briefs_q/N5B/REVIEW.md and PROCESS_LIGHT.md.
Only this report is written. There are no commits or source fixes.

All N5B line references below identify the 583-line file with SHA-256
317a1ba0a08ccd188e4c9c15bb7eeb8894e646a6521b3b4e8de6961e8d9693da.
The workspace has no Git metadata; this is a filesystem-snapshot review.
I checked the cited source passages, independently rebuilt the mathematical
implications below, inspected the finite-check implementation, and reran it.
The earlier checks/n5b_review.md was consulted after forming the present
findings; its LAND verdict is not evidence for a missing hypothesis.
Method credit remains with Tadeusz Balaban and Jonathan Dimock for the
constructive RG methods discussed in the packet. No external theorem or
recalled literature result carries a step of this review.

**1. UV-only characterization — HOLD; binding scope/quantifier fix.**

Attachments: N5B.md:3–9, 176–195, 217–237, 267–275, 495–506, 566.
Source checks: CODEX_REVIEW_SPHERE.md:186–204, especially 190, 194–196 and
204; SPHERE2_55.md:458–466; SEAM55.md:414–421 and 469–472.

The opening claims a conditional route “using only integration below fixed
reference scales.” However, (E) is an L² norm under the actual marginal of
U_k, and (D) and (7) are expectations under the actual full law. They are
valid sufficient inputs, but their statements still depend on that law.
The all-data seam estimate (T) does not remove this dependence from the
other inputs. N5B.md:193–195 correctly distinguishes a stronger sup version
of (E); that optional strengthening does not also strengthen (D).

This is an actual quantifier distinction. If P(B=1)=n^(-2) and Y=nB, then
||Y−EY||₂²=1−n^(-2), while inf_b sup_B|Y−b|=n/2. Replacing the marginal
by P(B=1)=1/2 changes the variance to n²/4 without changing the function Y.
Likewise, for a nonnegative conditional-covariance magnitude A=M1_B,
E[A]=M P(B) can be small while sup_B A=M is arbitrarily large. An
unconditional bound does not supply the conditional uniformity.
These examples test the logical inference, not a Wilson theory.

The cited operational definition of UV explicitly fixes every terminal
datum and integrates below it. SEAM55's N5-C has an expectation conditional
on V for every V; SPHERE2_55:466 retains that conditioning in its sufficient
example. N5B's (7) drops it. CODEX_REVIEW_SPHERE:196 also expressly warns
that an unconditional W3 estimate is not a sup-over-V estimate.

**Fix:** retain (4)–(8) as the theorem for the actual law and describe it as
requiring **no coarse-law decorrelation estimate**. That conclusion is
proved. If retaining the stronger UV-only label, explicitly add, for
k=n−J, sufficient premises such as

\[
 \inf_b\sup_{U_k}|F_k-b|\le C(J)Z_a^q,\qquad
 \sup_V E\!\left[\sum_{i<k}
  |\operatorname{Cov}(F_i,S_i\mid U_{i+1})|\ \middle|\ V\right]
 \le Z_a^q\delta(J),
\]

with the same cutoff/path uniformities and δ(J)→0. An every-V version of
(7) is one way to obtain the second premise. State these as OPEN
strengthenings, not consequences of (E)/(D). A claim that the entire
H_Euc package has this UV-only form must also specify the corresponding
conditional producer requirements for its bulk/observable Ward errors and
moment inputs. Otherwise narrow the opening and the “Fixed-R UV route”
status row. Do not infer that the averaged version needs infrared decay:
that necessity is not established either.

The prior N5B review itself acknowledges in item 3 that E/D remain
estimates for the actual law. That correct caveat needs to appear in the
target's characterization, rather than only in a supporting review.

**2. Regulator, current, Ward consumption and observable domain — CONFIRMED
as conditional statements.**

Attachments: N5B.md:25–84, 128–149.
Sources: SPHERE55.md:154–165, 223–250, 378–391, 479–490, 808–812;
SEAM55.md:328–339; CODEX_REVIEW_SEAM.md:134–142.

The incident-cell action and normalized shortest-path seam kernels are the
specified prism model. The chart-spacing bound does not assert a lower
mesh bound or a bound on every crossing chord; the C_geom requirement at
39–48 appropriately leaves that geometry/weak-coupling compatibility
explicit.

On the compact link configuration space, integrating
div(F exp(−S_action) Ξ) gives
E[ΞF]=E[F(ΞS_action−div Ξ)]. Taking F=1 centers the Ward insertion.
Writing it as B+𝔖 and defining the observable error gives equation (1).
For the quadratic Killing field the forward-difference product rule gives
the antisymmetric contribution
Σ_(μ<ν) w_(μν)[χ(x+a e_μ)−χ(x+a e_ν)]T_(μν), in agreement with E9.
The claim that the chosen B has controlled low-dimensional content needs
the matched current and W0/W1/W3; the identity alone does not supply it.
N5B correctly retains these inputs.

Divide the Ward identity by the fixed Z_a^q and integrate over a compact
path. Uniform vanishing of its three terms proves invariance of the tested
limiting moments. It does not prove their convergence or extension.
The contact distribution h(x)δ(x−y) pairs to zero with every disjoint
test pair even for nonconstant h. Thus the stated all-product/contact/
positivity bridge is substantive and correctly left OPEN. Separation
from the seam does not supply separation of repeated observable supports.

**Fix:** none to the identity or domain boundary; apply item 1 only when
describing these inputs collectively as conditional UV estimates.

**3. N5a/N5b and the repaired observable-image bound — CONFIRMED.**

Attachments: N5B.md:88–124, equations (2)–(3).
Sources: SPHERE55.md:428–439, 485–490, 813–831;
SEAM55.md:334–354.

Put H=E[F|W_s], M=E[𝔖|W_s]. Total covariance gives
Cov(F,𝔖)=E Cov(F,𝔖|W_s)+E[(H−EF)(M−c)] for any single scalar c.
The first term is bounded by Z_a^q A_s. Cauchy–Schwarz bounds the second
by ||H−EF||₂ ||M−c||₂, and
||M−c||₂²≤sup_V E[|M−c|²|V]. Infimizing gives (3). Absolute squares
make the estimate valid for complex observables with bilinear covariance.
A field-dependent c would invalidate the centering step.

The consumer is A_s+B_s τ_s→0, not just τ_s→0. Replacing the fine
variance by the conditional-image norm is mathematically valid, but does
not prove that norm is bounded in YM. Also, s proportional to sqrt(a)
turns a s^(-7/2) into a^(-3/4), so the reported withdrawal of the old
rate is correct.

**Fix:** none.

**4. Positive Markov decomposition and the fixed-J limit — CONFIRMED
CONDITIONAL; no missing terminal term.**

Attachments: N5B.md:155–213, equations (4)–(6).
Sources: SPHERE2_55.md:441–473;
CODEX_REVIEW_SPHERE2.md:73–85 and 118–132.

For a fine-field observable, past/future conditional independence gives
E[F_i|U_(i+1)]=F_(i+1), and the same for S. Apply total covariance to
F_i,S_i conditioned on U_(i+1), then sum:

\[
 \operatorname{Cov}(F,\mathfrak S)
 =\sum_{i<k}E\operatorname{Cov}(F_i,S_i\mid U_{i+1})
   +\operatorname{Cov}(F_k,S_k).
\]

This uses the Markov property, not nesting of single-level sigma-fields.
Positive backward kernels contract distance from a constant in sup norm;
conditional Jensen contracts the centered L² norm. Neither assertion
extends with constant one to arbitrary complex tilted measures.

At k=n−J, the last covariance is at most
Z_a^q C(J) inf_c sup|S_k−c|. Combining with (D) gives exactly (6).
Fix J so δ(J)<ε/2, then take a sufficiently small to satisfy its cutoff
threshold and C(J)τ(a,J)<ε/2. The C(J)=0 case is immediate.
No growth bound in J, moving-J rate, or radius-uniform Ward rate is
needed. An unbounded subsequence of fixed J values also suffices.

**Fix:** none to this proof. It proves N5 from the displayed hypotheses;
item 1 limits how their provenance can be characterized.

**5. Decay tail, coarse correlations and failed shortcuts — CONFIRMED.**

Attachments: N5B.md:217–282, equations (7)–(8).
Sources: CODEX_REVIEW_SEAM.md:40–48;
SPHERE55.md:657–663.

For i<n−J, j=n−1−i ranges from J to n−1. Then
h_(i+1)=ell_ref L^(−j) and L^(p(n−i))=L^(p(j+1)).
Extending the positive finite sum to j≥J gives (8). Its consecutive
term ratio L^p exp[−c(L−1)L^j] tends to zero for
c=m d_0/(2 ell_ref)>0, proving summability and vanishing tails.
The exponential at fixed j has no a dependence.

For independent uniform signs X,E,H,
Cov(X+E,X+H/3|X)=0 and Cov(X+E,X+H/3)=Var(X)=1.
Scaling the second conditional mean by ε_a instead gives ε_a, while
leaving the shared coarse variable correlated. This demonstrates both
why conditional decay alone is insufficient and why a small seam image
can suffice without coarse decorrelation.

SPHERE55's cited distance πR/2 occurs in its proposed failure scenario.
Distance alone establishes no necessity of an infrared estimate.
The tower moves a bound already proved at a finer fixed resolution; it
does not produce it or extend typical-data control to all data.

**Fix:** none to the proof or the rejection of necessity; use the
qualification in item 1 for the UV-only wording.

**6. Weighted tails and the separation of decay from a mass gap —
CONFIRMED at the stated abstract scope.**

Attachments: N5B.md:286–344, equation (9).

On G, |E[Hr1_G]|≤τ E|H|≤Cτ; on G^c, Cauchy–Schwarz gives
C||r1_(G^c)||₂. Hölder gives
||r1_(G^c)||₂≤||r||_(2p)P(G^c)^((p−1)/(2p)).
The rare-event calculation is exact:
Var(nB)=1−n^(-2), Cov(nB,B)=(1−n^(-2))/n, and
E[(nB)²1_(B=1)]=1. A small probability without an amplitude budget
therefore cannot close the remainder.

For K(t)=∫_0^1 E^5 exp(−Et)dE, the reflection quadratic form is the
integral of |Σ_i z_i exp(−Et_i)|² against E^5dE, hence nonnegative.
Multiplication by E has arbitrarily low positive energies on vectors
supported in (0,η). For t≥1, restricting the integral to (0,1/t)
gives exp(−1)/(6t^6); extending its upper endpoint to infinity gives
5!/t^6. Thus r^4K(r)→0 with no positive spectral gap.
This is a valid spectral counterexample to the general inference,
not a four-dimensional gauge model or a Wilson decay estimate.

**Fix:** none. The actual weighted tail remains a named OPEN input.

**7. Fixed-R geometry, moment limits and OS1 — CONFIRMED CONDITIONAL.**

Attachments: N5B.md:139–149, 348–380, 503–507.
Sources: SPHERE55.md:581–615; CODEX_REVIEW_SPHERE.md:255–269;
CODEX_REVIEW_SEAM.md:122–142; SPHERE2_55.md:547–576.

Substituting x=z/2 and c=e/(2R²) into the chart Killing field gives
v_R=e+(e·z)z/(2R²)−|z|²e/(4R²), as printed. The metric becomes
(1+|z|²/(4R²))^(−2)δ. In the Killing equation, the symmetric derivative
of v_R is (e·z)δ/R² and v_R applied to the logarithm of the metric
factor is −(e·z)/R², so they cancel. On bounded sets the field and all
its derivatives converge to the translation field. Finite-time flows
converge on the corresponding larger compact sets. Pole rotations and
coordinate reflections are exactly linear.

For each radius first choose the assumed continuum moments. For the jth
radius, approximate its first j required moments and Ward errors by a
sufficiently small admissible cutoff. Uniform local boundedness permits
countable diagonal extraction. Equicontinuity controls the contracting
flows and extends the identities on the specified common domain.
Enumerating all observable/group pairs is necessary; pairing only equal
indices would not establish invariance.

The complete finite support paths stay in the pole cap for large R.
No seam-contact estimate or clustering enters this passage. The common
observable maps, contact/positivity bridge, normalization and local
uniform bounds remain assumptions. Nothing here supplies H_int.

**Fix:** none to this conditional limit argument.

**8. F13 producer-to-consumer transfer — CONFIRMED OPEN, not a no-go.**

Attachments: N5B.md:384–405 and the F13 rows at 498–503, 534–536.
Sources: ASSEMBLY55.md:283–287, 475–489; SPHERE55.md:223–255, 548–559.
Direct producer checks: BFT4W55.md:397–408 and 620–630;
RLARGE.md:60–61 and 186–194; SRCCD55.md:80–94 and 116–124.

Integrating each forward kernel over its new link variable gives one.
That establishes the Markov representation on the stated graph, not a
Hessian bound or control of its normalized backward law. The checked
BFT construction uses product boxes embedded in tori and a small
complex coarse-field polydisc. RLF explicitly quantifies over hypercubic
tori and is itself an OPEN target. The SRC discussion identifies
coarse integrability/chessboard and coefficient-field requirements.
Those are not the sphere's shortest-path seam family, arbitrary crossing
data, or its variable-profile source domain.

The external-field example is exact:
Σ_y exp(Jxy+hy)=2cosh(Jx+h), and the normalized x mean is
tanh J tanh h. Equality of a local interaction therefore does not
identify its marginal after exterior integration. LOC-T and the
normalization/large-field estimates have real work to do.

The ordinary torus chessboard proof requires the translated reflection
structure absent from this regulator; RP at its symmetry planes alone
does not transfer that proof. This does not exclude an action-based or
other suitable estimate. N5B appropriately leaves the transfer OPEN.

**Fix:** none. No claim that all possible transfer methods fail is supported
or made.

**9. Physical mesh degeneration — CONFIRMED at the claimed scope.**

Attachments: N5B.md:407–425, equation (10).
Sources: SPHERE55.md:127–132 and 177–180;
CODEX_REVIEW_SPHERE.md:271–283.

The farthest corner of the cube centered at (m,0,0,0)a has squared
radius r_m²=m²+m+1. Expansion gives
q_m²−r_m²=(m+1)²/(4m²)>0. Moving the cube one unit outward raises its
farthest squared radius by 2m+2, exceeding that margin, so the indicated
vertex lies on the boundary. For m≥2 the displayed margin is strictly
between 0 and 1; q_m² is noninteger, whereas every half-grid vertex
has integer squared radius. These are generic radii.

Substitution into the actual crossing-chord formula gives the printed
ratio and asymptotic 1/(4m). At fixed R, a=R/q_m→0. This disproves a
uniform lower physical-edge comparison over this regulator family.
It does not disprove graph-based estimates or the possible usefulness
of a restricted cutoff selection.

**Fix:** none; retain the explicit limited conclusion at 423–425.

**10. Two-sided seam operator, gluing and kernel threshold — CONFIRMED
as algebra and obstruction to the quoted arguments.**

Attachments: N5B.md:429–473.
Sources: CODEX_REVIEW_SPHERE2.md:43–53 and 134–142;
CODEX_REVIEW_SPHERE.md:164–176.

Transporting both connections to one gauge frame makes their difference
J homogeneous. F^Σ is homogeneous too, so tr(J_i F^Σ_(ni)) is gauge
invariant. Its canonical dimension is 1+2=3. Reflection across the seam
changes the sign of each factor with a fixed signed normal; tangential
reflections change the two contracted components together. Choosing one
common Abelian direction gives the nonzero value 2jf tr(T²).
Thus a single-connection exclusion of Chern–Simons is not an exhaustive
classification on the stated two-sided field space.

For K>0, expanding the proposed square gives exactly
K||J||²+c<J,F>. The remaining coefficient is −c²/(4K).
Its smallness would require c²/K→0 and the stated coercivity and
integration/source controls. It is correctly ARGUED, not a proof of ST.
Strictly positive finite-cutoff densities preserve positive mass on
every open set of coarse mismatch data, excluding exact finite-step
gluing. Finally, differentiating At²+B(Δ−t)² gives
t=BΔ/(A+B), so comparing only the two endpoints misses the minimizer.
The alleged safe kernel interval does not follow; Hessian compatibility
is an additional requirement.

**Fix:** none. These arguments refute the specific shortcuts, not N5.

**11. Settling lemma and GO/NO-GO scope — CONFIRMED with item 1's
qualification on the word UV.**

Attachments: N5B.md:477–526, 558–577.

ST is exactly (T). With CD-K=(D) and IMG-K=(E), item 4 proves N5.
It is sufficient, stronger than the tested covariance conclusion, and
not sufficient alone for the full sphere construction. The target
expressly admits cancellations and weighted-tail alternatives.
Its “minimal” language is restricted to the additional seam input in
this chosen architecture, not necessity among all approaches.

For boosts, an equivariant chain sends the conditional image to its
negative under reflection. For any value x in this symmetric range,
max(|x−c|,|−x−c|)≥|x|; hence c=0 is optimal. More generally, any two
image values separated by η force radius at least η/2 about every
scalar. A nonzero constant image has radius zero and refutes nothing.
Consequently failure of ST, especially only at rare configurations,
does not by itself refute N5.

No nonvanishing normalized Ward covariance on the actual prism YM
sequence is supplied. Nor are ST/CD-K/IMG-K or F13 established.
Thus **UNDECIDED**, rather than GO or NO-GO, is the justified route
verdict. None of the PROVEN labels establishes a YM estimate or an
audit status.

**Fix:** preserve these verdicts and limitations; make item 1's narrow
description/premise correction.

**12. Comparison with the flat route — CONFIRMED at the stated scope.**

Attachments: N5B.md:530–556.
Sources: CODEX_REVIEW_TQ.md:98–195, 628–678 and 755–762;
ASSEMBLY55.md:279–281 and 503–504.

If a reference-scale annulus has at most Cr^4 sampled sites, weights
bounded uniformly in r, and the stated normalized covariance bound
C'(1+|x|)^(−4−η), its absolute sum is O(r^(−η)).
The pointwise sampled hypothesis avoids the invalid substitution of a
continuum radial envelope into arbitrary lattice samples.

With its source and convergence hypotheses, the flat Ward identity
gives a limiting torque −S'(t) for the specified two-point orbit.
Zero torque is equivalent to invariance of that orbit. This is not
full-algebra OS1, not a physical mass-gap equivalence, and not an
identification of sphere and torus state selections. The invalid
fine-variance premise SRC-E is not silently reintroduced.

**Fix:** none.

**13. Finite checks, provenance and review-status boundary — CONFIRMED
for current reproducibility; historical limits stated.**

Attachments: N5B.md:571–583; checks/n5b_criteria.md:8–39;
checks/n5b_checks.py:26–201; N5B_LOG.md and the two recorded executions.

The criteria cover finite rational identities and three deliberately
false shortcuts. The script enumerates all 81 histories of its positive
three-state, four-level chain, normalizes conditional laws separately,
and retains the terminal covariance. Independently, its initial
F,S tables give EF=0, ES=3/2 and E[FS]=−2, hence total covariance −2.
The general derivation in item 4 checks what those finite cases test.
The sign and Bernoulli controls agree with items 5–6.

I reran the unmodified script with python3 -B, nice -n 10 and all seven
specified thread environment variables set to 1. It exited 0 with
**26 PASS criterion/control reports**, including X1–X3, and final PASS.
Observed guards: priority 20, load1 1.87841796875, free memory 50%,
peak RSS 19,333,120 bytes, elapsed 0.007738 seconds. Its transient lock
directory was removed; no output file was rewritten. The three terminal
covariances were −5555/10336, −670179/14096992 and
−7611915/1413536768, agreeing with the supplied run.

The first recorded attempt failed in RSS-limit setup before mathematics.
The later implementation retains the preregistered measured-RSS and
runtime guards; removing an unsupported extra setrlimit call did not
alter a mathematical criterion. The log preserves this failure.
The present criteria and script match the completion hashes, and their
timestamps are consistent with the stated order. This fresh session
cannot independently authenticate historical pre-registration merely
from timestamps or an author's log.

All 3,341 original files listed in the author's source manifest matched
their recorded hashes when checked. The prior review matches the
reported target hash and documents the two earlier corrections now
visible in N5B. Its LAND is a historical review disposition, not an
audit result or a resolution of item 1. Numerical PASS supplies no
estimate for ST, F13, continuum existence, or a mass gap.

**Fix:** none to the finite checks or existing historical records. Record
this separate review without altering their outputs or claiming an
audit-status change.

**Binding fixes.** Resolve item 1 in N5B itself: distinguish the proved
averaged covariance reduction from a uniformly conditioned UV-only
version. Either narrow the opening and corresponding status language,
or explicitly add the stronger OPEN conditional premises and keep their
status distinct. The scientific route verdict remains UNDECIDED.
No other binding mathematical correction was found. Existing OPEN
analytic leaves are not being converted into a requirement to complete
the Yang–Mills construction before this assessment can land.

VERDICT: HOLD

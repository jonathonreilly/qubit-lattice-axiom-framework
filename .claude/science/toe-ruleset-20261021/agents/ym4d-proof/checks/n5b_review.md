# Independent hostile review of N5B

Reviewer: a context-separated, same-family Codex reviewer. I did not author
N5B or its check script. This is not cross-family review and not an audit.
The review follows PROCESS_LIGHT.md and briefs_q/N5B/AUTHOR.md. The author
whitelist controls the output location: this report is the only file edited
by the reviewer. No numerical job, commit, audit/ledger or axiom edit was made.

**Disposition: LAND the corrected conditional assessment.** Its conclusion
that the sphere route is **UNDECIDED** is supported. No verdict here proves
ST, F13 transfer, Yang–Mills existence, non-freeness or a physical mass gap.

## Frozen target and evidence boundary

The final N5B.md reviewed here has SHA-256
`317a1ba0a08ccd188e4c9c15bb7eeb8894e646a6521b3b4e8de6961e8d9693da`.
Line numbers below refer to that version. All ten inspected source/process
files matched their hashes in checks/n5b_source_manifest.json:
SPHERE55.md, SPHERE2_55.md, SEAM55.md, CODEX_REVIEW_SPHERE.md,
CODEX_REVIEW_SPHERE2.md, CODEX_REVIEW_SEAM.md, ASSEMBLY55.md,
CODEX_REVIEW_TQ.md, PROCESS_LIGHT.md and briefs_q/N5B/AUTHOR.md.
This is a filesystem-snapshot review; no commit identity or main-branch
comparison is asserted. Prior review verdicts were not used as proof.

The written derivations were reviewed independently. The finite check script
and its recorded outputs were inspected after they became available; they
were not rerun by this reviewer. Balaban and Dimock receive method credit in
the target. No literature theorem or recalled item supplies a missing step.

## Per-item findings

### 1. Exact consumer, normalization and domain — CONFIRMED

**Attachments:** N5B.md:25–149, especially (N5), (1) and the consumer table.
**Source checks:** SPHERE55.md:154–165 and 223–255 identify the actual prism
regulator, incident-cell weights and positive soft kernels; :378–391 and
:808–812 identify the Ward split and corrected current indices; :479–490
identify N5/N5a/N5b. SEAM55.md:328–339 supplies the all-separated-product
consumer. CODEX_REVIEW_SEAM.md:134–142 identifies the contact/algebra gap.

On a finite compact link configuration space, integration of
div(F exp(−S) Ξ) gives E[ΞF] = Cov(F, ΞS−div Ξ). Defining the observable
error and splitting the latter insertion as B+𝔖 gives (1). Integrating
the path derivative after dividing by the fixed positive Z_a^q proves
invariance when the three normalized errors vanish uniformly on that path.
No insertion bound follows from a small coefficient alone. The text correctly
keeps that bound, the matched current and the profile as inputs.

The contact counterexample h(x)δ(x−y) vanishes on separated pairs even when
h is not invariant. Thus the explicit full-domain/positivity bridge is
necessary for the stated passage to OS1; the target does not infer it from
two-point or all-separated-product symmetry.

**Fix:** none remaining. The physical-ceiling correction is recorded in item 9.

### 2. N5b and the coarse-image covariance bound — CONFIRMED

**Attachments:** N5B.md:88–124, (2)–(3).
**Source checks:** SPHERE55.md:485–490, :813–831; SEAM55.md:334–354;
CODEX_REVIEW_SEAM.md:21–38.

Total covariance gives
Cov(F,𝔖) = E Cov(F,𝔖|W_s) + E[(H_s−EF)(M_s−c)]
for a single scalar c. The first term is at most Z_a^q A_s. The second is
bounded by ||H_s−EF||₂ ||M_s−c||₂, and the last squared norm is at most
sup_V E[|M_s−c|²|V]. Taking the infimum proves (3). For complex quantities
the absolute-value Cauchy inequality gives the same result. A c depending
on W_s or V would invalidate the identity used for centering.

The actual requirement is A_s+B_s τ_s→0. The target correctly neither
drops B_s nor replaces it by an assumed harmless fine-field variance.
Also a s^(−7/2) at s proportional to sqrt(a) scales as a^(−3/4), so the
withdrawal of the old rate is substantive and correctly reported.

**Fix:** none.

### 3. Positive-chain direct cut and fixed-J limit — CONFIRMED CONDITIONAL

**Attachments:** N5B.md:155–213, (4)–(6).
**Source check:** CODEX_REVIEW_SPHERE2.md:118–132 is the correctly credited
prior direct-cut argument; :73–85 identifies the positivity boundary.

For F and 𝔖 measurable at U₀, the Markov property implies
E[F_i|U_{i+1}] = F_{i+1}, even though the single-level sigma-fields are
not nested. Applying total covariance to F_i,S_i conditioned on U_{i+1}
and telescoping proves (4), including the terminal covariance. The backward
conditional laws are positive probabilities, so averaging contracts sup
distance from any scalar; Jensen contracts the L² norm about EF. This
does not extend with constant one to complex tilted measures.

At k=n−J, Cauchy bounds the terminal covariance by
Z_a^q C(J) τ_R(a,J); (D) bounds the remaining sum by Z_a^q δ(J). Choose a
fixed J with δ(J)<ε/2, then choose sufficiently small a for the remaining
term and its allowed cutoff threshold. This proves N5 without controlling
growth of C(J), prescribing J(a), or imposing a radius-uniform Ward rate.
An unbounded subsequence of fixed J values works by the same argument.

**Fix:** none. This proves an implication, not the actual estimates (E),
(T) or (D). Law-averaged E/D bounds remain estimates for the actual law;
their notation alone is not a proof that they can be established by UV
methods. The stronger law-independent image form is explicitly distinguished.

### 4. Decay tail and failed conditional-decay shortcut — CONFIRMED

**Attachments:** N5B.md:217–261, (7)–(8).
**Source check:** CODEX_REVIEW_SEAM.md:40–48.

With j=n−1−i and i<k=n−J, j≥J, h_{i+1}=ell_ref L^(−j), and
L^{p(n−i)}=L^{p(j+1)}. Thus (7) gives exactly (8). The consecutive-term
ratio L^p exp[−c(L−1)L^j] tends to zero, so the series converges and its
tails vanish. At any fixed j its exponential has no cutoff dependence.

For independent mean-zero signs X,E,H, the conditional covariance of
X+E and X+H/3 given X is zero, while total covariance is Var(X)=1.
Replacing the second conditional mean by ε_a X changes that contribution
to ε_a while leaving the coarse variable completely correlated. These
examples distinguish conditional decay, conditional transparency and
coarse-law decorrelation. They do not model Yang–Mills.

**Fix:** none.

### 5. Original-law weighted tails and gap comparison — CONFIRMED

**Attachments:** N5B.md:286–344, (9).

Splitting E[Hr] over G and G^c gives Cτ on G and
C||r 1_{G^c}||₂ on the complement. Hölder gives the printed probability
power (p−1)/(2p) only with the accompanying ||r||_{2p} bound. For
P(B=1)=n^(−2), Var(nB)=1−n^(−2), Cov(nB,nB)=1−n^(−2), and
Cov(nB,B)=(1−n^(−2))/n. The amplitude, not just event probability, matters.
No original-law tail estimate is claimed proved.

For K(t), the displayed integral of an absolute square proves reflection
kernel positivity. Nonzero vectors supported in (0,η) have energy quotient
at most η, ruling out a positive lower spectral bound. Substitution u=Et
and integration over [0,1] or [0,∞) give respectively
e^(−1)/(6t^6) and 5!/t^6 for t≥1. Hence r⁴K(r)→0 with no positive gap.
The target restricts this to a spectral comparison, rather than claiming
a four-dimensional gauge-theory counterexample.

**Fix:** none.

### 6. Fixed-R symmetry and the flat moment diagonal — CONFIRMED CONDITIONAL

**Attachments:** N5B.md:348–380.
**Source checks:** SPHERE55.md:581–615; CODEX_REVIEW_SPHERE.md:255–269;
CODEX_REVIEW_SEAM.md:122–142; SPHERE2_55.md:547–576.

Substituting x=z/2 and c=e/(2R²) into
v_c=R²c+2(c·x)x−|x|²c gives exactly the target's v_R. On each fixed
compact set, the field and its derivatives approach the constant e;
bounded finite-time flows therefore approach translations. Rotations and
coordinate reflections act linearly. The relevant finite paths stay in
the pole cap for sufficiently large R.

For every radius, first obtain the assumed continuum moments and fixed-R
Ward identities. At increasing radii choose cutoffs approximating finitely
many moment and Ward tests. Uniform boundedness permits a diagonal
subsequence; equicontinuity passes from the countable Cartesian product
of observable/group families to the stated domain and controls the
contracting flows. This requires the common maps and full-domain bridge
listed in §1.3. It proves neither those hypotheses nor nontriviality.
No seam-contact Ward estimate is needed for these cap paths, and no
coarse clustering estimate is used in this conditional passage.

**Fix:** none.

### 7. F13 transfer and two-sided seam mechanism — CONFIRMED AT STATED SCOPE

**Attachments:** N5B.md:384–473.
**Source checks:** ASSEMBLY55.md:283–286, :475–484; SPHERE55.md:223–255,
:548–559; CODEX_REVIEW_SPHERE.md:271–283;
CODEX_REVIEW_SPHERE2.md:43–53 and :134–142.

Kernel normalization is geometry-independent, but supplies no Hessian,
large-field or source bound. The source statements really do distinguish
the prism contours/nonrectangular blocks from the hypercubic producer
domains. For the exterior-dependence example, summing over y gives
2cosh(Jx+h), and direct summation gives E[x]=tanh(J)tanh(h). Therefore
equality of local interaction formulas does not identify conditional laws.

For the shrinking-edge sequence, direct expansion gives
q_m²−r_m²=(m+1)²/(4m²), and the crossing-chord formula gives the stated
1/(4m) asymptotic. The farthest vertex of the claimed retained cube is
inside the ball; the next outward cube fails that test. Noninteger q_m²
ensures genericity. This defeats only uniform physical shape regularity,
not a combinatorial RG proof.

After transporting to a common frame, J transforms homogeneously, as does
F^Σ. Their traced contraction is gauge invariant and has dimension three.
Equatorial reflection makes both factors odd; tangential reflection changes
both contracted components together. The Abelian example is nonzero.
The completion of the square is exact for K>0 and a positive inner product,
but suppression of its residual requires c²/K→0 and the additional
coercivity/integration/source controls explicitly left OPEN. Positive finite
Wilson and soft-kernel densities preclude exact finite-step gluing. Finally,
minimizing At²+B(Δ−t)² gives t=BΔ/(A+B), so endpoint comparison does not
prove a safe stiffness interval.

**Fix:** none. F13 is an unfilled hypothesis mismatch, not an impossibility
theorem. The mixed operator refutes the exhaustive exclusion, not N5.

### 8. Settling lemma, flat-route comparison and route verdict — CONFIRMED

**Attachments:** N5B.md:477–577.
**Source checks:** CODEX_REVIEW_TQ.md:98–195, :628–678 and :755–765;
ASSEMBLY55.md:279–286 and :503–504.

ST, CD-K and IMG-K are exactly sufficient for the direct-cut inequality;
BULK/ALG remains necessary for the claimed assembly. The word “minimal”
is restricted to the additional seam input of that specified sup-norm
architecture, not a necessary characterization of N5: the target says
explicitly that covariance cancellations and weighted tails can suffice
without ST. At fixed R,J,v, persistent separation of two conditional image
values forces a nonvanishing radius about every scalar, and can refute ST.
For odd boosts, symmetry of the range makes zero an optimal center.
Failure of ST still need not produce a nonzero tested Ward covariance.

The flat annulus estimate follows from at most Cr⁴ sampled sites, bounded
weights and the assumed pointwise r^(−4−η) covariance envelope. A continuum
radial envelope alone would not justify those sampled bounds. The cited
flat Ward argument identifies the limiting torque with minus the derivative
of the specified two-point orbit, conditional on its source/convergence
hypotheses. It does not identify the full OS algebra or different regulator
selections. The SRC-E caveat is correctly retained.

Consequently neither GO nor NO-GO is supported. UNDECIDED is the warranted
route verdict, with a concrete settling contract and distinct open inputs.

**Fix:** none remaining; the scalar-centering correction is recorded below.

### 9. Binding corrections found during this review — FIXED AND RECHECKED

1. **Uncentered image versus ST.** The original sentence said a nonvanishing
   seam image at a rare datum refutes ST. S_k≡1 is an exact counterexample:
   its best global center is 1 and its ST radius is zero. Final
   N5B.md:509–516 now requires unavoidable oscillation along a cutoff
   sequence and explicitly permits subtraction of a nonzero constant.
   This fixes the diagnostic without changing any theorem.
2. **Physical UV ceiling.** The original exact 2 ell_ref ceiling bounded
   chart spacing but was also asserted for the physical hierarchy. The
   prism crossing chord is a separate quantity. At a scale h choose
   q²=(R/h)²=m²+m+2, m≥2. The cube centered at (m,0,0,0) is retained,
   while its neighbor centered at (m,1,0,0) is not. Its boundary vertex
   v/h=(m−1/2,1/2,1/2,1/2) has r²=m²−m+1. The crossing chord divided
   by h is 2q(2m+1)/(2m²+3)>2. Squaring the needed comparison leaves
   8m³+m²+9m−7>0. Genericity holds because four-dimensional half-grid
   squared radii are odd integers, whereas q² is even. Final
   N5B.md:39–48 now distinguishes chart spacing and requires an explicit
   geometry/contour factor for a global physical neighborhood ceiling.

No binding correction remains unresolved. The author made these edits;
the reviewer re-read the affected passages and their dependencies. No
unrelated source was changed by this review.

### 10. Exact finite checks and execution record — CONFIRMED LIMITED EVIDENCE

**Attachments:** checks/n5b_criteria.md:8–39; checks/n5b_checks.py:26–201;
N5B_LOG.md:51–100; checks/n5b_checks_out.txt and n5b_checks_err.txt;
checks/n5b_checks_run2_out.txt and n5b_checks_run2_err.txt.

The criteria were present before the script became available during this
review. The script uses exact Fraction arithmetic, normalizes conditional
laws separately, and retains the terminal covariance. Independently,
its C1 initial law gives EF=0, ES=3/2 and E[FS]=−2, matching total
covariance −2. At cut 1, its three F images are −20/19, 2/17, 3/2 and
its S images are 47/19, 10/17, 5/4, with masses 19/48, 17/48, 1/4.
Their covariance is −5555/10336, matching the recorded nonzero terminal
term. The general proof in item 3 covers the other cuts. X1–X3 target
the missing terminal term, the non-Markov tower and field-dependent
centering; the rare-event formulas agree with item 5.

The first execution failed during RSS-limit setup before mathematical
checks or lock acquisition; that failure is preserved rather than marked
PASS. The final script retains the preregistered measured-RSS, runtime,
nice, load, free-memory, single-thread and lock checks. Removing Darwin's
rejected optional setrlimit call did not alter mathematical thresholds.
The second output records 26 PASS reports, all three negative controls,
priority 20, load 1.94677734375, 50% free memory, peak RSS 19,595,264 bytes,
0.007454 seconds and final PASS; its stderr is empty. This is inspection
of a recorded author run, not an independent execution claim.

Frozen check identities:

- Script: `8d675d23178eda204e09681b536d7ad1e3c41ac443eed988db3ebd4d5110b4e0`.
- Criteria: `3e28cd892d78459af61b4a74073a95cccf2ee00fd17c5598c5e847bd7767a943`.
- Run-2 stdout: `0f3c4a66f7736be2cd779b1ecf5bc88cb22a9e2af6328223531c13a6cefe939b`.

**Fix:** none. These checks support only finite probability algebra. They
supply no estimate on ST, CD-K, IMG-K, F13, continuum limits or a mass gap.

VERDICT: LAND

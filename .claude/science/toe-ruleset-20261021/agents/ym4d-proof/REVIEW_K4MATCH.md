**Independent hostile review of K4MATCH.md — 2026-10-30**

**Disposition: HOLD.** The conditional fourth-cumulant reduction and its
order-h-squared algebra pass. AUTHOR item 3 is not completed: there is no
evaluated Yang–Mills correction, sign determination or uniform size/remainder
bound establishing non-cancellation. The manuscript reports this honestly.
Two narrower wording repairs are also required: identify the comparator for
the N5 invocation, and state the additional symmetry needed for the assertion
about *all* odd perturbative orders.

This is a fresh, same-family Codex review, not an audit grade. I did not write
the manuscript. I re-derived the identities and estimates below, checked the
source locations, and reran the registered algebra checks. The earlier review
was consulted afterward to verify provenance, not used as a mathematical
premise. No source, evidence, coordinator, audit or ledger file was edited;
this review is the sole output. No commits were made.

All manuscript line numbers below refer to the 607-line `K4MATCH.md` with
SHA-256 `2f795c75609075e6d48096abf5ba8572a80f6271a554889f7212c4be75827604`.

| Brief item | Verdict and manuscript locations | Required fix |
|---|---|---|
| Target: prove or reduce normalized lower matching | **PASS as a conditional reduction**, lines 20–74, 189–409. No interacting lower bound is proved. | Preserve the explicit original-law matching hypotheses and the fixed-m-then-cutoff limit order. Apply B2 to the N5 wording. |
| AUTHOR 1: exact additional estimates and shared inputs | **PASS**, lines 76–101, 292–302, 536–557. The new fourth-source estimates remain OPEN. | No mathematical repair to the input comparison; retain the conditional status of FLOW, K-dec's dependencies and quantum source matching. |
| AUTHOR 2: four-insertion representation and extra RG output | **PASS**, lines 103–187, 304–371. A fourth-order jet suffices; full multivariable analyticity is a sufficient alternative, not proved necessary. | Preserve triples, pair-pair terms, terminal terms and all-history normalization. Do not infer these estimates from a two-point upper bound. |
| AUTHOR 3: actual O(g²) correction, sign, size and non-cancellation | **HOLD / OPEN**, lines 411–534, especially 474–488 and 507–534. Formal insertion signs are not the sign of the YM coefficient. | B1: supply the matched YM calculation and a uniform controlled bound. B3: qualify the separate all-odd-orders statement. |

**R1. Observable, normalization and smooth free coefficient — PASS.**
Locations: lines 22–57, 150–154, 193–214.

Each unoriented plaquette occurs at four clover corners and twice in the
ordered plane sum. Thus its exact source weight is
`h_f(p)=(1/2) sum_corners f(x)`. The quadratic Wilson term is
`(1/2) sum_a F_p^a²`, giving `w_f=h_f/2`, as used here. This agrees with
TSE55 lines 129–144 and CUMUL lines 173–186; no factor of 2N is lost in
`u=2N/g_std²`.

For the one-colour continuum covariance,
`G(z)=Lambda²(I-2zz^T/|z|²)/(pi²|z|⁴)`. A connected pairing of four
quadratic vertices is one of three undirected cycles, with 16 pairings per
cycle and one colour loop. At the stated centres the two-form trace is 6,
so `96(1/81+1/256+1/20736)=169/108`. The corresponding point ratio is
`169/(15552d)`. These are not substituted for the smooth integrals.

I also checked the support-wise argument in CUMUL lines 293–322: an edge
perturbation has norm at most `1/2500`; the rescaled curvature matrix differs
from the centre matrix by less than `1/250`. Four-factor telescoping gives
trace error less than `6/60`. Multiplication by the three centre weights
gives `9971/6480<A<10309/6480`. The stated B0 bounds and division by positive
quantities give exactly the interval for R0 in (2).

Fix: none. Keep the distinction between the point coefficient and the exact
smooth-test integral.

**R2. Actual-chain fourth-cumulant increment — PASS.**
Locations: lines 105–146.

In the square-free source ring, the coefficient of `z1 z2 z3 z4` in
`log E exp C(z;Y)` is the sum over partitions of outer cumulants of the
conditional cumulants. The partition counts are `1,4,3,6,1` for types
`4`, `3+1`, `2+2`, `2+1+1`, `1+1+1+1`. Subtracting the last term leaves
exactly the fourteen terms in (5). The actual Markov property supplies
`E[G_i|U_(i+1)]=G_(i+1)`; summing the differences, including `D_K,4`,
recovers P. No sign or positivity of an individual increment is required.

For the stated variance mixture, `E T=2`, `E T²=5`, hence
`kappa4=3 E T²-3(E T)²=3`, although the conditional fourth cumulant is
zero. This correctly detects the missing pair-pair family.

Fix: none. An estimate of `E c_1234` alone would not estimate this increment.

**R3. Source jets and the additional information beyond PL-1L — PASS.**
Locations: lines 148–187, 362–371.

With the source-free normalized kernels held fixed, the tower identity gives
`Phi_(i+1)=log E[exp Phi_i|U_(i+1)]`. Extracting each square-free coefficient
gives (7), including the four triples and three pair-pair terms. This is the
explicit fourth-order form of SRCCD55 lines 588–604. SRCAN55 lines 129–147
confirm which conditional chain is held fixed. The jets of the original O
and the conditional cumulants of its first images are correctly distinguished.

SRC2_55 lines 198–228 really do formulate an all-n representation and derive
bounds *assuming* it. Its source radii and conditional upper estimates do
not establish (15). The finite laws `2^-4(1+t product x_i)` have zero
proper-subset mixed moments and fourth cumulant t, so lower-order moment
information does not determine the missing coefficient. This is an
information example, not an obstruction theorem for YM. CUMUL's vanishing
third cumulant, lines 235–253, is confined to separated continuum free
curvature and does not eliminate the conditional triple jets.

Fix: none to the identities or sufficiency claim. The fixed-kernel convention
is essential to the displayed conditional recursion; a different
source-dependent blocking convention would require its own derivative terms.

**R4. Gaussian mixed-slice reference — PASS.**
Locations: lines 191–214.

TSE55 lines 146–165 provide positive covariance slices with
`sum_i mathcal K_i=P_ex`. In the independent-slice Gaussian model, conditioning
on the tail changes a quadratic observable into its tail quadratic form plus
a deterministic constant. The latter drops out of a fourth cumulant.
Consequently `F4(H_i)-F4(H_(i+1))` is the actual Gaussian counterpart of the
increment, not an assumed fourth-order orthogonality identity. Expanding the
four edges assigns each scale tuple to its minimum index once. Mixed slices
and the all-terminal tuple survive.

Fix: none. Replacing this expression by a sum of same-slice cycles would be
incorrect; the registered mutation detects that replacement.

**R5. FLOW/LGF transfer and four-cycle error — PASS CONDITIONAL.**
Locations: lines 216–264.

For fine slices, FLOW-pw gives `u_i>=u-R_F>=u/2`; their contribution to the
kernel difference is bounded by
`C L^-4k u^-2 sum_(n>=1)(b_+ n+R_F)L^4n exp(-c L^n)`.
For coarse slices up to `n1=floor((u/2-R_F)/b_+)`, use the same denominator
bound and the convergent sum with `L^-4n`. After n1, use u_min; the remaining
geometric tail times a polynomial in u is bounded by a constant times
`u^-2`. The terminal slice satisfies the same coarse estimate. This proves
(9) from the named hypotheses, without importing an exact beta coefficient.

In each cycle, changing one of four scalar entries costs
`C1 L^-4k u^-2`; each other entry costs at most
`(C0+C1)L^-4k/u`. There are three cycles, four changes and the factor 16d.
Together with `sum_p w_r(p)<=12a^-4` and
`lambda^16 a^-16 L^-16k=1`, this reproduces
`C_AF,4=192d 12^4 C1(C0+C1)^3` and the power `u^-5` in (10).

LGF lines 488–542, especially (38) and (41), concern exactly the free
curvature kernel and the error `O(r^-5)+O(T^-4)`. On the separated rescaled
supports these become `O(L^-k)+O((lambda/R)^4)`. Fixed smooth bumps allow
the stated Riemann-sum and clover-shift errors, uniformly in m after
rescaling. The two-edge argument gives (12). No fourth spatial derivative
or interacting Green estimate is being silently imported.

Fix: none. K-dec and FLOW remain inputs with the conditional scopes recorded
in TSE55 lines 253–295 and FLOW lines 418–453.

**R6. Increment envelopes and summation — PASS CONDITIONAL.**
Locations: lines 266–302.

For i<k, telescope the four-factor tail difference so that one factor is
`a_i`; the remaining tail kernels have uniform cross-support bounds
`C L^-4k/u`. This yields the fine exponential in `p_i,4`. For i>=k, the
same near/far splitting starting at i bounds each tail by
`C L^-4i/u_i`. If u_i is below the splitting threshold, the fixed u_min
bound suffices after enlarging C. Four edges give the coarse exponent 16,
including i=K.

The fine sum in (13) converges supergeometrically. The near coarse sum is
bounded by `2^s u^-s/(1-L^-16)`; the far sum is bounded by
`u_min^-s L^-16(n1+1)/(1-L^-16)`, which is at most `C_s u^-s`.
Thus (14), *if proved for the interacting increments*, implies CUMUL's
PL-4C at lines 489–490. It does not follow from the free envelope. Any fixed
positive coarse decay exponent would suffice for this summation argument;
16 is a sufficient producer choice, not a necessary physical obstruction.

Fix: none. Retain all fourteen terms, the terminal cumulant and original-law
normalizers in the OPEN producer.

**R7. Free source radius, projection and Cauchy extraction — PASS CONDITIONAL.**
Locations: lines 308–371.

Positivity and `sum mathcal K_i=P_ex<=I` give `G_fine<=2I/u`.
Since `lambda^4 ||W_r||<=||f_r||_infinity`, the fine operator bound is
correct. Weighted Schur with weights `sqrt(w_r(p))` gives the coarse
bound in (15a); its near/far sum is uniformly bounded by FLOW. Equality
of the nonzero spectra of the two positive sandwiches then bounds each
`u lambda^4 sqrt(G_run) W_r sqrt(G_run)`. Choose fixed radii so that twice
the sum of these norm bounds times the radii is less than one. The finite
Gaussian log-determinant series is holomorphic there. This proves a
radius, not a uniform full trace bound, and says nothing about quantum
zero-freeness.

The sixteen-term projection kills monomials missing any source and preserves
the mixed coefficient. Its mixed derivative is
`u^4 lambda^16(kappa4-kappa4_run)=u^4(P-P_run)`. Four one-variable Cauchy
integrals therefore give (16) with `product rho_r^-1` and no 4!.
The factor-at-most-16 comparison with an unprojected supremum is also
correct. TSE55 lines 365–395 are the right source for the relative-radius
discussion; tree holomorphy does not propagate the quantum source error.

Fix: none. Both the quantum analytic input and the bound on the projected
difference must remain OPEN.

**R8. Conditional lower matching and passage to a fixed-scale limit — PASS;
N5 comparator wording requires B2.**
Locations: lines 373–409, 559–567.

Dividing the free and interacting absolute errors by A4 or A2 gives (17).
For real relative errors with `|delta2|<1`, subtracting one from
`(1+delta4)/(1+delta2)^2` gives (18). With both errors at most 1/4,
the ratio factors are exactly `12/25` and `20/9`; multiplying the former
by `3/(338d)` gives `18/(4225d)`. The separate lower bound on the raw
cumulant uses U_+(m_star), not U_-(m_star). Keeping m_star fixed and
assuming convergence of the seven centred coordinates passes the polynomial
lower bound and the positive denominator margin to the limit. No unbounded
moment convergence is inferred merely from weak convergence of laws.

However, the phrase “an N5 witness” at line 392 does not name its comparator.
CUMUL lines 337–350 explicitly require a comparator Gaussian **on e**.
COMBO lines 429–481 explicitly distinguish that witness from the current
single finite-moment N5 requirement for `F1 union F2 union F3`. The manuscript's
own positive free Maxwell-composite cumulant demonstrates the issue: this
polynomial need not vanish on F1. The disclaimer about *unrestricted*
free-net exclusion at lines 565–567 does not specify this narrower boundary.

Fix B2: call (19) the fixed-scale fourth-cumulant witness against fields
Gaussian on e, and say that the combined F1/F2/F3 exclusion additionally
uses AF-e and COMBO's stated interface. Qualify “final witness” at line 559
as the fourth-cumulant component. This is a scope repair, not a failure of
the inequalities or the conditional moment-limit argument.

**R9. Five-family order-h-squared formula — PASS FORMAL; all-odd wording
requires B3.** Locations: lines 415–470.

Expanding the normalized tilted logarithm gives
`h <A(t)>_t + h²[<B(t)>_t + kappa_t(A(t),A(t))/2]`, minus its t=0 value.
The coefficient of four distinct source labels contains: one X2 insertion;
two distinct X1 insertions; one X1 and one -V1 insertion; one -V2 insertion;
and two V1 insertions with factor 1/2. This reproduces all five terms of
(21), including their combinatorial factors and normalization subtractions.
The same derivation applies to the denominator pair. The bare/matched
coupling distinction at lines 425–431 is necessary and correctly retained.

The displayed parity assumptions prove that the coefficient of h vanishes.
To conclude that *all* odd powers vanish, as lines 463–464 state, one needs
the full formal identities `S_eff(-h,-A)=S_eff(h,A)` and
`X_r(-h,-A)=X_r(h,A)`, including every higher vertex and the integration
prescription. Parity of just V1,V2,Xr0,Xr1,Xr2 does not imply this. For
example, `S_eff(A,h)=A²/2+h³A²` and `X_r=A²` satisfy every listed
through-order-two parity condition, but their fourth cumulant is
`48(1+2h³)^-4=48-384h³+...`. This is a logical counterexample to the
truncated parity implication, not a YM counterexample.

Fix B3: explicitly assume and preserve the full field-reversal symmetry in
the matched scheme, or narrow the sentence to the order-h term actually
shown to vanish. The order-h-squared identity and the separately assumed
remainder inequality (24) survive either repair.

**R10. Actual perturbative sign, size and non-cancellation — HOLD / OPEN.**
Locations: lines 474–534; AUTHOR.md line 9.

The expansion of the ratio has coefficient `a-2b`, as stated. A common
running factor cancels exactly, and a common field factor shifts a and b
by 4z and 2z. These identities do not evaluate the remaining YM integrals.
The signs attached to V1 and V2 insertions are not signs of their joint
cumulants. FLOW's positive slope does not determine either a or a-2b.

The sufficient threshold in (24) is valid: `u>=16M_n` makes the first
correction at most 1/16, `u>=4 sqrt(H_n)` makes the remainder at most
1/16, and `eta_n<=1/8` gives total relative error at most 1/4. But none
of M2,M4,H2,H4 is supplied for the actual matched YM source. A finite
regulator coefficient, or its formal sign alone, would not provide a
uniform short-scale certificate. The manuscript acknowledges this at
lines 528–534 and in its opening disposition.

Fix B1: specify the actual matched action, four composite insertion
vertices, gauge/zero-mode prescription and counterterms; evaluate or
rigorously enclose the five families in (21), and the two-source families
needed for the normalized ratio; determine the actual correction's sign
and controlled size; and prove a uniform remainder bound sufficient to
place the original trajectory inside a non-cancellation threshold. Exact
or validated bounds must support any decisive numerical sign or margin.
A weaker uniform relative error would establish the lower-matching
implication but would not, by itself, answer the expressly requested
order-g² sign calculation. Proxy polynomial data cannot close this item.

**R11. Obligation table and status discipline — PASS with the scope repair
above.** Locations: lines 76–101, 536–567, 597–607.

WITNESS lines 532–595 and TSE55 lines 480–524, 639–643 support the
comparison with PL-1L and its P1–P6 ingredients. The table correctly adds
joint higher curvature information, source jets, product-source matching,
terminal/full-history control and the distinct denominator pair. The
stronger jet and source-norm formulations are alternatives, not independent
estimates that must both be assumed. The summed PL-4C remains the essential
unproved dynamical estimate; recognizing this is not a proof of it.

HANDOFF lines 450–465 and FIXED_SOURCE_RADIUS_ASTRA lines 3–7 support the
limited coordinator scopes. Their reviewed local or selected-sector
results are not used as a full original-law fourth-source estimate. No
GO, NO-GO or retained audit status is supported or claimed here. HOLD is
a completion verdict, not an obstruction to the YM matching problem.

Fix: retain the OPEN labels and prior HOLD disclosure. Do not promote
formal or conditional results to unconditional matching or an audit grade.

**R12. Evidence, attribution and reproducibility — PASS within algebraic
scope.** Locations: lines 569–607.

All 13 source digests in `checks/k4match_sources.json` match the current
files. All 17 final-file digests recorded in
`checks/k4match_verification.json` also match. The stored criteria precede
the stored checker by their preserved timestamps. Both failed run records
contain zero scientific assertions and the reported RSS-limit exception;
the later successful record contains 64 passing assertions. This supports
the reported failure/success distinction, not a YM result.

I reran the four registered assertion families by loading the existing
checker without its command-line writer, holding the three existing
numeric locks read-only, and using an external watchdog. All 64 assertions
passed; their complete normalized records equal the saved successful
records. Effective nice was 20, all five thread counts were 1, native free
memory was 50%, all load averages were below 2.346, and monitored combined
RSS peaked at 40,910,848 bytes. Elapsed time was about 0.112 seconds. There
was one serial numerical child and no pools, sampling or new scientific
test criteria. No saved check or receipt was overwritten.

The conditioning attribution is correct: Brillinger's original paper gives
the partition identity as equation (4) on printed page 215. The manuscript
rebuilds the needed finite version instead of importing it. See
[Brillinger, The Calculation of Cumulants via Conditioning](https://www.ism.ac.jp/editsec/aism/pdf/021_1_0215.pdf).
The stated scope of Dimock's reference is also accurate: its abstract
describes Balaban's method through a three-dimensional scalar phi-four
example, not a four-dimensional YM matching theorem. See
[Dimock, The Renormalization Group According to Balaban — I](https://arxiv.org/abs/1108.1335).
No literature coefficient or memory-only lemma is needed for the checked
identities. Balaban and Dimock retain the method credit given by the author.

The earlier `checks/k4match_review.md` ends HOLD and binds the same final
manuscript hash. That historical status is represented accurately. It does
not substitute for the present independent derivations or eliminate B1–B3.

**Binding fixes before landing the complete brief.**

1. **B1 — scientific completion:** supply the actual YM sign/size calculation
   and uniform non-cancellation control described in R10, or continue to
   mark AUTHOR item 3 incomplete. Relabelling the conditional certificate
   as a successful perturbative check is not an acceptable repair.
2. **B2 — comparator scope:** qualify lines 392–409 and 559–560 so that the
   fourth-cumulant polynomial is used only for the Gaussian-on-e N5 scope;
   refer combined-class consumers to AF-e plus COMBO's explicit interface.
3. **B3 — perturbative scope:** supply the all-order field-reversal symmetry
   for lines 463–464, or restrict that assertion to the first odd order
   proved by the displayed assumptions. Keep the sharper remainder in
   (23)–(24) conditional on its stated separate uniform input.

The conditional reduction can be retained as research progress. The
specified author deliverable remains incomplete, and neither the missing
calculation nor the narrower scope issues are repaired by passing the
finite algebra controls.

VERDICT: HOLD

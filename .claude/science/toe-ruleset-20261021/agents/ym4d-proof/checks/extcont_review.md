# Independent hostile review of EXTCONT — 2026-10-30

**LAND for the repaired conditional research note.** Three binding issues
were identified during review and repaired by the author. I checked the
affected arguments again; no binding mathematical defect remains at the
stated q=4 scope. The actual history-uniform selected-return and induction
theorems remain OPEN. This verdict is neither an audit classification nor
a claim that the requested Yang–Mills construction is complete.

This is fresh-context, same-family Codex review of Codex work. I did not
write EXTCONT or inherit its author conversation. The source arguments
were independently rebuilt rather than accepted from earlier LAND
verdicts. The author made the source corrections described below; my only
created or edited file is `checks/extcont_review.md`. No commits or new
numerical experiments were performed.

The complete reviewed source is `EXTCONT.md:1–654`, SHA256
`b10015bbd6be5fac97fd636fdc79f665800fe9921651575b9d03b0167b534b6e`.
Line numbers below refer to those final bytes unless explicitly described
as an earlier version. I read `briefs_q/EXTCONT/AUTHOR.md`, the reviewer
brief, and `PROCESS_LIGHT.md`. The task-specific allowed-file instruction
controls the review destination, so `REVIEW_EXTCONT.md` was not created.
There is no git/current-main certification in this supplied snapshot.

**Per-item verdicts.** PASS means the stated implication or diagnostic is
valid with its written hypotheses; it does not establish those hypotheses
for the actual model.

| Item and final lines | Verdict | Fix or required disposition |
|---|---|---|
| Source units, full norm and derivative dictionary, 32–71 | PASS. RGA3 carries total field order six and source order four, including order-ten words. REALRGB G1 is a different fourth-order, l1-direction norm with frozen exterior data. Observable differentiation keeps the prescribed kernels and couplings fixed. | No remaining fix. Do not transfer G1 bounds into RGA3 without the stated order, weight, exterior-field and coordinate-count costs. |
| Exact extraction and stored counterterms, 77–149 | PASS as conditional coordinate algebra. E2 assumes its infinite-volume bulk functional; E3 retains all quadratic tensors and all source-dependent scalar terms. E4 has constants four and five on the supplied coordinate balls. | The common evaluation point in E4 was clarified during repair. Actual gauge-compatible localization and a bounded closed counterterm system remain OPEN. |
| Physical localization and the beta-zero distinction, 153–177 | PASS at its ARGUED physical scope. The symmetry classification applies to the stated bulk sector; a spatial curvature-difference quadratic form has beta zero and nonzero field Hessian. | No remaining fix. Do not apply the bulk classification to a selected hole with fixed exterior data or replace beta-zero by P_2 F=0. |
| Full Taylor-sum contraction and actual return comparison, 181–242 | PASS after fix F2. The ideal map contracts the specified full coordinate norm by at most 8 L^-2. E7 remains an explicitly unproved comparison with the actual extracted operator. | F2 is resolved. Preserve the distinct coordinate/scaling, support reblocking, retained-reader and physical extraction obligations. |
| FLOW identities and coupling extraction, 248–276 | PASS at the cited scopes. E1 and E9 have the correct normalization and sign; E8 has FLOW's graph and Hessian units. None of the determinant identities supplies E7. | No remaining fix. The critical-background, admissibility, Pi-loc and remaining UNIV conditions are retained. |
| Differentiation of the selected normalized reference, 282–358 | PASS after fix F1. Ordered score bounds through the full mixed order, domination and a fixed measure space imply E11–E12; the denominator is differentiated. | F1 is resolved by separate scalar and labelled polynomials. Moving-domain transport still needs its exact Jacobian, transported insertion and required derivatives. |
| Actual selected-sector regularity and diagnostics, 362–394 | PASS. Discrete masks are uniformity parameters. The positive integral in E13 is not C1; the oscillatory family defeats acquisition of sixth derivatives from small values. Neither is claimed to be an actual gauge-sector singularity. | No remaining fix. All-history selected-return H1 remains OPEN; current selectors cannot be frozen or summed away while claiming an individual selected estimate. |
| Fixed-mask transfer and unweighted arbitrary-hole obstruction, 400–431 | PASS. E14 retains inactive roots and coefficients. The singleton/one-active-vertex family has exact ratio exp(mu(card(Gamma)-1)). | No remaining fix. Fixed-mask regrouping transports existing jets and acquires none. The obstruction concerns that unweighted map only. |
| Differentiated hole-volume payment, 435–500 | PASS conditional theorem, including the inactive-root multiplicity and necessary singleton jet price. The full touching components are paid, even where they already intersect X. | No remaining fix. Actual E15, its original-law allocation, and the complete rooted sum over history labels remain OPEN. |
| Conditional induction and renewal alternative, 508–614 | PASS after fix F3, now explicitly q=4. MS/SEL/HOLE/EXT/COEFF include the substantive transition estimates; E18–E19 close the residual ball once those inputs are supplied. | F3 is resolved. Other finite q require the expressly enlarged hierarchy. Matching, all-order, continuum and symmetry modules are separate, and MIXSMALL alone is not asserted to close induction. |
| Failure classifications and next targets, 620–649 | PASS. Actual operator counterexamples, failed sufficient majorants and missing estimates are distinguished. No all-route impossibility or actual-model contraction is claimed. | No remaining fix. Retain these scope restrictions when using the positive abstract lemmas. |

**Binding findings and their confirmed repairs.**

**F1 — labelled source multiplicities, resolved at 302–324.** The received
version defined T to include RGA4 but used the scalar factor `1/c!` in
the only displayed P polynomial. RGA4 sums subsets: with four labels
there are `binom(4,c)` terms of cardinality c and no source factorial.
The required repair was

    P_(6;[4])(B) = sum_(a+b<=6,c<=4)
                    binom(4,c) C_(a+b+c)(B)/(a! b!),

with every label weight incorporated in its score direction. The final
text supplies this polynomial and uses the norm-specific P_T in both
E11 and E12.

This was a mathematical defect, not just notation. An analytic control
uses two integration points sigma=+1,-1 with counting measure and

    H_sigma(f,c,J) = sigma b exp(f+c+J),
    b = B exp(-3 epsilon),  |f|,|c|,|J| < epsilon.

All included unit-direction score derivatives are at most B. Give the
four source labels the same J direction, which RGA4 expressly permits.
At the origin, the normalized densities are
`n_sigma=(1+sigma tanh(b exp(f+c+J)))/2`; each positive-order derivative
has absolute value `b/2+O(b^3)`. Put

    S_6=sum_(r=0)^6 2^r/r! = 331/45,
    E_4=sum_(c=0)^4 1/c! = 65/24.

The integrated labelled norm is
`1+b(16 S_6-1)+O(b^3)`, whereas the old scalar polynomial is
`1+2B(S_6 E_4-1)+O(B^2)`. The respective limiting linear coefficients
as epsilon tends to zero are `5251/45` and `4087/108`. The former is
larger, so a sufficiently small fixed positive epsilon and then small B
violate the old assertion. This is a written small-parameter expansion,
not a numerical experiment. The repaired subset polynomial bounds this
example and follows directly from the ordered Leibniz calculation.

**F2 — order of the domain supremum, resolved at 125–141 and 186–213.**
The earlier E5 proof used A_r described by derivative suprema on balls,
then bounded a sum of such separate suprema by the norm whose domain
supremum is outside the complete Taylor sum. That last step was not
justified: in general, the supremum of a sum is smaller than the sum of
the separate suprema. This was a gap in the displayed proof, not a
counterexample to the contraction itself.

The repair keeps A_r pointwise. Radial Taylor integration, followed by
the identity
`sum_(a+b=r) binom(i,a)binom(j,b)=binom(3,r)` for i+j=3, controls
the lower orders by `(1+3+3)L^-2 sup_D T(F)`. All orders three through
six are evaluated together at the single point L^-2 z, so contribute at
most `L^-2 sup_D T(F)`. Taking the domain supremum last proves precisely
`8 L^-2`, without replacing RGA7 by a larger norm. E4 now likewise
evaluates all its projection coefficients at the common point (0,J).

**F3 — finite-q quantifier, resolved at 508, 578–599.** The received
theorem fixed arbitrary finite q while E10–E12 supplied only the q=4
score hierarchy and polynomial. Those hypotheses do not provide higher
source jets. The binding repair was to restrict the theorem to q=4 or
explicitly strengthen every dependent assumption. The final statement
chooses q=4 and separately specifies the `6+q` mixed-word hierarchy and
`binom(q,c)` source multiplicities needed for any other finite q. No
all-order conclusion is inferred from those separate finite extensions.

**Independent derivations and source checks.**

1. **Jet algebra and projection.** An ordered derivative word distributes
   its positions between factors, retaining each induced order. Dividing
   the resulting convolution by a! b! c! proves submultiplicativity on
   the downward-closed index set. For labelled sources the labels are
   partitioned between factors instead. Reconstructing a degree-r field
   coefficient on the same unit balls multiplies its contribution by at
   most `sum_(k=0)^r binom(r,k)=2^r`. Summing degrees zero through two at
   the common reference point gives E4. The zero jets of P_2's remainder
   persist under all four source derivatives, so the radial proof in F2
   uses no seventh field or fifth source derivative. This agrees with
   `REALRGA.md:89–126,184–218,392–414`.

2. **Normalized derivative acquisition.** Iterating differentiation of
   exp(H) produces partitions with the original order inside each block,
   hence M_m. Positivity gives `abs(D_I Z)<=M_m Z`. In the identity
   `Z Z^-1=1`, isolate the highest derivative of the reciprocal; the
   remaining Leibniz terms give exactly the stated I_m recurrence.
   Applying Leibniz once more to w/Z gives C_m and the pointwise bound
   `T(n)<=P_T n`. This pointwise bound, not only its integrated version,
   justifies inserting the regulator G in E12. Domination licenses
   differentiation under the integral. The exponential matrix derivative
   is a sum of m! ordered-simplex integrals of unitary factors; their
   total volume is one. Thus the local source score costs
   `2u_0 sum r_p`, and b terminal derivatives cost at most
   `t_j n_c h_(j+1)^b`. Earlier retained fields and moving cuts are not
   covered by this terminal/source computation. The source comparison
   is `REALRGB.md:149–266`, not an inference that its G1 equals RGA3.

3. **Extraction, symmetry and FLOW units.** Expanding the Wilson term
   with `tr(T^a T^b)=delta_ab/2` gives coefficient u/(8N) after summing
   both ordered plane orientations, hence u=2N/g_std^2. Multiplying the
   stated standard slope 2b_0 by 2N gives E1; it does not derive a kernel
   universality theorem. Linearity of beta gives E2 and the sign in E9.
   In the bulk curvature bilinear, reflection of a coordinate in one
   plane but not the other kills each cross-plane coefficient; axis
   permutations equalize the six diagonal coefficients. Constant
   conjugation forces an invariant colour form and no invariant linear
   functional. This classifies only that bulk quadratic sector. The
   finite-difference curvature functional has the extra Fourier factor
   `sum_nu abs(exp(ip_nu)-1)^2`, so its potential Hessian begins at order
   p^4 while remaining nonzero.

   The polar correction is also retained correctly. Near the identity,
   for `M=average exp(Y_i)` with traceless anti-Hermitian Y_i, the linear
   trace of log M vanishes and its quadratic trace is real. Therefore
   `arg det M=O(Y^3)`. Comparing the SU(N) maximizer with
   `W exp(-i arg(det M)/N)` gives `0<=d(M)<=arg(det M)^2/(2N^2)`, hence
   d(M)=O(Y^6). Its cancellation in the normalized kernel is exact; a
   Hessian cannot detect the term that a sixth-order contract must keep.
   This checks `FLOW.md:115–153,573–593` and `HIST.md:880–919` without
   deriving tree regularity from the minimum operation.

   For E8, FLOW's count gives at most 16 cubes at the root link,
   `80^(2(n-1))` connected size-n supports, `4 M_block^4 n` possible
   links and distance weight `(M_block n)^2`. Their product yields the
   displayed `64 M_block^6 H` series; `kappa_p>log 6400` makes it finite.
   This uses the raw Hessian-entry premise and FLOW's *-connected graph,
   not a complex Cauchy estimate or an unmentioned conversion from the
   face graph. Checked against `FLOW.md:155–171` and
   `REALRGA.md:600`.

4. **The four FLOW identities.** In FP-exact, splitting the orbit and
   orthogonal slice and applying linear coarea gives the factor
   `abs(det chi Gamma)/sqrt(det(hh*))`; dropping either factor changes
   the background-dependent determinant. In T-tel, compress the
   covariance recursion by P, use `P_(k+1)T_k(1-P_k)=0`, then use the
   complementary-minor identity to cancel log det Y against the
   longitudinal determinant. The remaining transverse determinants
   telescope and leave the ghost term. Cartan-T follows by differentiating
   contour products and the SU(N) maximizing stationarity equation; the
   root-sector phase weights and denominator survive. SLICE-U writes
   A=Q-D(U)h, so its projection at that same U equals PQ. These steps
   establish the identities, not high-order local estimates of the
   selected nonlinear map. The exact statements and restrictions were
   checked at `FLOW.md:2606–2657,4376–4401,4662–4770,4824–4851`.

5. **Full-root hole estimate.** For every input meeting Lambda,
   `abs(R(X))-abs(X)<=S_X`. Submultiplicativity gives the per-input factor
   `A exp(-(tau-mu)S_X)`. At an active output root v, v must already lie
   in X. At an inactive root, its component H_v has size m, is included
   in the payment, and X meets N[H_v]. At most 9m input-root sums are
   required, giving `9A m exp(-(tau-mu)m)`. Taking the maximum and adding
   the unchanged inactive family proves E16. This uses no independence,
   geometry bound on m, or missing source-label projection. The singleton
   input proves E17 with the entire jet of w, not merely its value.
   For RD3's hole, `3^4+8*3^3=297`; its 81 vertices give E14's first
   constant, while `1+8*81=649` and `1+9*81=730` give the second.
   Source arguments: `LIB1.md:216–273,377–438` and
   `RD3.md:425–473`. A mandatory normalized indicator has integral one
   by `RD3.md:278–304`; it cannot pay this price again. The extensive
   remaining debits in `REALRGB.md:253–266,558–566` are upper-majorant
   failures, not lower bounds on actual local weights.

6. **Induction and continuation.** RGA-C first groups overlap-connected
   selected atoms and then expands the hard-core logarithm. Its positive
   rooted-tree recursion has supersolution
   `exp((mu+2)abs(H_i)) alpha_i`; the two stages consume the two support
   units separately. Ordered-jet submultiplicativity applies to both.
   Thus MS supplies H3 only when its complete new coefficients and
   regenerated reserve are actually provided. SEL, HOLE, EXT and COEFF
   explicitly supply the other transition obligations. A second activity
   derivative bounded by 2C gives the quadratic remainder by integrating
   `(1-t)D^2 R(tK)[K,K]`. With x<=M, `C x^2<=C M x`; E18–E19 then give
   `x_next<=theta M+B e_*<=M`. Exact source dependence and marked jets
   preserve only the finite H6 records claimed here. The final caveat
   correctly excludes the additional matching and all-order modules.

   For an m-window alternative, split a continuation length as km+s;
   uniform bounds on every starting level give `B_0 theta_win^k` and
   sum `m B_0/(1-theta_win)`. Return operators add D_ret. The scalar
   action inequality in `LINEAR_PACKAGE.md:124–138` has sharp constant
   one; `RENEW.md:79–145` supplies its long-wave witness and the separate
   localized L^-2r bound. The exact rough flux orbit and tube estimate
   at `RENEW.md:149–266` take the weak-coupling limit at fixed finite
   horizon and volume, excluding precisely a uniform plain-forward
   margin on all inputs. They exclude neither extracted nor weighted
   continuation. The conditional window statement was checked at
   `RENEW.md:398–452`, and H0–H6/RGA-C at
   `REALRGA.md:273–479,523–601`.

I also read the REALRGA and REALRGB reviews as requested. Their scope
warnings were checked against the primary arguments above; their verdicts
were not used as premises. Balaban, Dimock and Bauerschmidt–Brydges–Slade
receive methodological attribution in the note. No external lemma or
memory-only statement substitutes for a proof of the new estimates.

**Numerical evidence and limits.** The author supplied the checker and
receipts during this review. I statically read all of
`checks/extcont_check.py` and its criteria. The observed file hashes match
the receipt: criteria
`dad72c028c2776a9daddda0515ddac6b29905a859743959f9e71ae72004989f2`,
checker
`28ee2368d79bd813cb3ddb96b1294c104e4cd6605531e95436f6edc7350d9975`.
The result and stdout are byte-identical, and stderr is empty. The receipt
records five passing groups and rejection of the two shared-norm mutants
and the field-dimension mutant. Its 16 resource samples record niceness
20, all six thread variables one, maximum load below 8, free memory 51%
and peak RSS 22,691,840 bytes. The script contains the lock and before/
between/after resource checks, uses no pools, and does not set RLIMIT_AS.

These are existing author-run finite regressions, not an independent
execution. They check constant-coefficient finite graph payments,
monomial projection/scaling and formal derivative polynomials. They do
not test the full Taylor supremum argument, the labelled-source repair,
moving selectors, differentiated actual weights, E7, or E19. The author
log now preserves that distinction. Historical preregistration timing
cannot be reconstructed from this snapshot alone; the mathematical
verdict rests on the written derivations and the confirmed repairs.

**Remaining binding fixes: none.** The unresolved physical construction
is accurately marked OPEN, including selected-sector regularity, actual
all-history E15, a gauge-compatible extracted return satisfying E7,
uniform coefficient recursions, and the full inequality E19. No broader
claim is authorized by this review.

VERDICT: LAND

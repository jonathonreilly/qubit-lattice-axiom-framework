# Independent hostile review of ROUGH.md

Review date: 2026-10-30. Scope: `briefs_q/ROUGH/REVIEW.md`, including the
author brief's requested inherited-law joint moment, original-action
ownership, overlapping cores, four source labels and history entropy.

The partial research note is mathematically supportable at its stated
conditional scopes. I found no blocking defect. **The author brief's uniform
inherited-law estimate is not proved.** In particular, Q15 is a raw forward
integral with every output integrated; Q25 and the general complete-reader
history sum remain open. LAND below accepts this explicitly incomplete
research note, not an affirmative solution of the author brief, an audit
status, or permission to perform a Git operation.

## Source identity and independence

- Candidate HEAD: `688a8ddf958e6a5ba5402d6b7fdad4d283af56df`.
- Reviewed `ROUGH.md`: all 624 lines; SHA256
  `40423aa02e8759e0993c980ab396745abfd7321d7db7e92268a78f33ea58493d`.
- `ROUGH_LOG.md`: SHA256
  `e6dfb55e8b904f3198265fea8c2aacab14a496e53935feba01885c9b120613cb`.
- Review brief: SHA256
  `26cc5f02f474d5a4ef0b6caf390445c6fd69a96512adca9980c36c45bc27a23f`.
- Author brief: SHA256
  `9382b2f69a3c898bf48b287c9889a8cddbabdc7a538101968337f2d9d21637f0`.
- Input manifest `checks/rough_sources.sha256`: SHA256
  `46c1f594923ffa995cf55ad2801246e583e016dd2542bdf73b5950a58f6fda97`.
  All nine entries matched the files actually inspected.
- Packet manifest `checks/rough_final.sha256`: SHA256
  `54333e999c7eac79f750bc6567b45de6da071fdfb4a1816d6c2fb43fb9bf5c40`.
  All seven entries matched. These are identity checks, not mathematical
  validation.

The fetch of `main` and `ai/execution` succeeded during this review. The
methodology snapshot is `origin/main` at
`01589af3faf806b736c42dc2f3bd625e9edead9f`; the planning ref is
`56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. Planning grants no science status.
The installed physics-claim-reviewer skill has minor wording drift; its
complete diff against this main snapshot was inspected, and main's review
contract was used within the explicit one-file assignment.

This is fresh-context, same-family review: Codex reviewing Codex. I did not
write the candidate. I reconstructed the mathematical steps from the note
and primary local arguments before reading the complete earlier
`checks/rough_review.md`. Its favorable verdict was already disclosed by the
author log, so this is not a verdict-blind review. Neither that verdict nor
its PASS/readiness language is used as mathematical evidence. Shared model
family and source inputs limit independence; no cross-family or formal
verification is claimed.

## Itemized verdicts and fixes

Line references in this section refer to the frozen `ROUGH.md` above.

1. **Target, law and status — ACCEPT AS OPEN** (lines 3–25, 33–76,
   605–620; Q1–Q3). The numerator is the opened inherited density, whereas
   the all-cut denominator contains the stated current Wilson density.
   They are not identified. The requested joint inequality, complete
   rooted budget and separate factorization obligation match REALRGA and
   REFMATCH. No GO, mass gap, continuum conclusion or retained audit
   status is asserted. **Fix:** none; the OPEN qualification is essential.

2. **Arbitrary-field ribbon estimate — ACCEPT** (lines 78–101; Q4).
   Each transverse axial displacement contributes L plaquette occurrences,
   and there are at most `3(L-1)/2` such displacements. Nonabelian product
   telescoping works because every inserted plaquette is conjugated and
   HS norm is unitarily invariant. Writing `x_p=||I-U_p||HS/sqrt(2N)` gives
   `||T-S||HS^2/(2N) <= (sum_occ x_p)^2 <= n sum_p n_p f_p`.
   Averaging gives exactly W, and its row sum is the average of `n^2`,
   hence at most `A_L^2`. The identity defining d follows by expanding
   the squared distance of two unitaries; `delta<=d` follows because S
   is an admissible maximizer competitor. Multiplicities survive torus
   projection. **Fix:** none.

3. **Output-link and coarse-plaquette estimates — ACCEPT** (lines 103–129;
   Q5–Q6). The two averages in the squared triangle inequality are
   `delta+psi` and d, so its right side is
   `2psi+2delta+2d <= 2psi+4Wf`. A separate telescoping of the straight
   square has `L^2` plaquettes. Squaring its contribution together with
   the four link discrepancies produces five terms, hence coefficients
   `5L^2 q`, `20 sum_boundary W` and `10` per boundary occurrence.
   The row sum is at most `5L^4+80 A_L^2`. If the action term is below
   `epsilon^2/(4N)`, the gap term must be at least that large; four
   occurrences then give one gap at least `epsilon^2/(160N)`.
   This improves a current-level action threshold, without identifying
   that action with unused original action. **Fix:** none.

4. **Backward demand propagation — ACCEPT** (lines 131–155; Q7–Q8).
   For one step, collecting coefficients gives
   `xi_0+W_0^T eta_0+A_0^T xi_1` on f_0 and
   `eta_0+B_0^T xi_1` on psi_0. At two steps the f_0 coefficient is
   `xi_0+W_0^T eta_0+A_0^T xi_1+A_0^T W_1^T eta_1+A_0^T A_1^T xi_2`.
   This directly verifies the recursion's orientation and each type of
   demand; finite induction covers every R. Nonnegativity is necessary
   and present. Adding two atoms adds their demands, including all
   repeated readers. **Fix:** none.

5. **Original ownership and overlap price — ACCEPT CONDITIONALLY**
   (lines 157–181; Q9–Q11). For every original plaquette the combined
   prior use, propagated regulator demand and core allocations must fit
   into one unit. Equal sharing on a witness belonging to d_p cores
   spends `d_p(r_p/d_p)=r_p`, not d_p separate reserves. The lower price
   follows only from the supplied witness or allocated-sum lower bound.
   The note does not prove such a positive lower bound for every rough
   core, and says so. Q10 is a sufficient fluctuation-capacity restriction,
   not a necessity theorem for actual kernel moments. **Fix:** none;
   no positive witness charge may be inferred from ancestry alone.

6. **Tilted kernel price — ACCEPT** (lines 185–215; Q12–Q14).
   The ambient cubes have HS diameter `1/(sqrt(2)t)` and cover the group
   with at most `(1+4Nt)^(2N^2)` operator balls of radius 1/t. Haar
   invariance gives the stated mass bound. Since the arithmetic mean has
   operator norm at most one, trace duality makes h 1-Lipschitz. Thus
   `A_t>=e^-1(1+4Nt)^(-2N^2)`. The tilted-event numerator is at most
   `exp[-(1-b)t a_c]` for `0<=b<=1`, proving Q12. Directly collecting
   the original exponent gives `exp(bt) Z_((1-b)t)/Z_t`, and factoring
   its maxima gives Q14 with the positive `exp(bt delta)` expense.
   At `b=1` the bound need not decay; at `a=b=0` normalization gives
   exactly one. The remaining gap exponent in Q13 is correct.
   **Fix:** none; the original full gap price cannot also be spent.

7. **Joint forward-chain integration — ACCEPT CONDITIONALLY**
   (lines 217–246; Q15). Q8 and Q9 with `z=0` imply pointwise
   `-S_0+Ecal <= -sum_G D_G+sum_c b_c t_c psi_c`.
   Extract the supplied charges on E, discard E, and integrate the
   latest output first. The conditional product kernel and Q12 give
   the claimed factor uniformly in its inputs. Repeat backward until
   only probability Haar remains. This requires no independence of
   original fields or rough cores. Distinct gap ownership, all-output
   integration, `t_j>=1`, and the stated deterministic bounds for an
   adapted schedule are real hypotheses. The added real-source debit
   also has the correct factor `|sum_i J_i f_(i,p)|/u_0`.
   **Fix:** none. This proof cannot be substituted for the fixed-terminal
   quotient; lines 258–261 explicitly prevent that substitution.

8. **Physical history partition — ACCEPT** (lines 248–261; Q16).
   For common nonnegative F, the pointwise inequality
   `sum_h I_h w_h F <= exp(sn) F` proves the integral statement.
   It does not control separately optimized history suprema. A common
   envelope or an actual multiplicity bound is required after that
   change of order, as the text states. **Fix:** none.

9. **All quotient jets — ACCEPT CONDITIONALLY** (lines 263–307; Q17).
   Repeated product differentiation partitions ordered positions for
   the numerator exponential. For the inverse, an independent recurrence
   from `D D^-1=1` is
   `R_I <= sum_(nonempty S subset I) M_S^- R_(I\S)`, with `R_empty=1`.
   Unrolling orders the blocks of each set partition, giving `|pi|!`.
   At second order this is `I_12^-=M_12^-+2M_1^-M_2^-`, agreeing with
   the direct reciprocal derivative. The subsequent subset convolution
   is Leibniz for numerator times inverse. No same-species group
   derivatives have been commuted. The field factorials and all sixteen
   source subsets match the specified norm; total mixed order ten is
   retained. Path occurrence counts give the Wilson `4^r` and contour
   `ell^r` bounds, including inverses. The normalizer score polynomial
   is paid separately and every earlier read kernel remains present.
   Fixed sectors, positive denominators, uniform score bounds and
   dominated differentiation are necessary hypotheses, not consequences
   of positivity. **Fix:** none; moving-selector boundary terms remain
   an open input, not an application of this formula.

10. **Four original-source factors — ACCEPT** (lines 309–319; Q18).
    With kernels held fixed and a linear original tilt, differentiation
    gives exactly `(-1)^|B| product_(i in B) O_i w`. Summing subsets
    produces `product_i(1+r_i|O_i|)`, without a four-label factorial.
    The elementary maximum `sup_(x>=0) x exp(-epsilon x)=1/(e epsilon)`
    proves the stated absorption, consuming `sum_i epsilon_i` of the
    original reserve. It pays numerator jets only. **Fix:** none.

11. **Same-integral insertion and charge extraction — ACCEPT CONDITIONALLY**
    (lines 321–345; Q19–Q20). The downward-closed Taylor index set makes
    the norm submultiplicative: field binomials cancel against the
    factorials, and disjoint source subsets distribute among factors.
    Apply this before integration to get Q19. Regulators dominate already
    differentiated insertions and need not themselves be differentiated.
    On the selected sector `exp(sum D_G)>=exp(sum tau_G)`, proving Q20
    with the same denominator. C is neither a probability nor a
    demonstrated local bound. Separate marginal moments would not prove
    the displayed joint estimate. **Fix:** none.

12. **History envelopes and explicit entropy — ACCEPT CONDITIONALLY**
    (lines 347–414; Q21–Q24). Disjoint smooth bumps give the stated
    counterexample to interchanging a sum of suprema with a supremum
    of the sum. Q21 supplies the missing common masses. For the spatial
    count, a deterministic rooted tree traversal of `2(n-1)` steps
    determines its visited set, yielding at most `Delta^(2(n-1))`
    connected sets through a fixed vertex. The stipulated source-label
    encoding has `(n+1)^4<=16^n` choices. The assumed injective D^n
    encoding must include all remaining history and reader data. With
    the support-size bound these give r. The explicit root-cover premise
    then gives `C_root r/(1-r)`. Q23 implies
    `r<=1/(1+8 C_root)<1`, hence a budget at most 1/8. The other 1/8
    is separately required. None of these counting hypotheses is
    established for arbitrary inherited histories; Q24 retains the full
    sum when they fail. Factorization remains separate. **Fix:** none.

13. **Local inherited comparison — ACCEPT AS OPEN** (lines 418–430; Q25).
    The unknown C is exactly the quotient left by Q20, with all score,
    regulator, overlap and denominator costs still inside. A common
    bound of the stated strength would resolve a substantial part of
    the requested problem. The note correctly avoids calling this a
    solved or demonstrably weaker reduction. **Fix:** none for this
    research note. Completing the author target requires an actual
    same-law construction and estimate here, together with the joint
    majorants and complete history/root sum; renaming C is no fix.

14. **Extensive cap bill — ACCEPT AS A TECHNIQUE FAILURE**
    (lines 432–454; Q26–Q27). From `e^-2t<=k_t<=e^2t`, the last
    numerator kernels cost `8 kappa u_j n_j/L^4`. The matching denominator
    lower bound costs the same again. Its `4n_j` link caps cost
    `8N^2 log(1+4N/zeta)n_j`; its `6n_j` plaquettes have action at most
    `8u_j zeta^2` each. This gives exactly d_j. With fixed local data,
    the sufficient price test fails when `n_j/m` becomes large.
    No lower bound on the true Q_core follows, and jets still need their
    own estimates. **Fix:** none; preserve the technique-only conclusion.

15. **Depth-capacity failure — ACCEPT AT ITS STATED SCOPE**
    (lines 456–476; Q28). Following one nested straight-square occurrence
    contributes a nonnegative product at least `(5L^2)^R` to one entry
    of the backward transport. Terminal demand `a u_R` therefore forces
    the displayed necessary condition for Q9. Constant couplings, or
    only polynomial growth of `u_0/u_R`, violate it at large R.
    This is a lower bound on coefficients of an upper estimate, not on
    actual curvature or its moment. No RG trajectory is derived here.
    **Fix:** none; sharper transport or integration remains a live route.

16. **Zero-mean conditional obstruction and future tilt — ACCEPT**
    (lines 478–502; Q29). The periodic SU(2) field is admissible on the
    stated side lengths. In direction one, translation preserves the
    axial factors, which cancel in this commuting field. The remaining
    L-link leg averages L roots of unity and gives M=0. Thus `k_t=1`,
    `delta=1`, `psi=0`, and the integrand in Q29 is constant `exp(amt)`.
    Already m=1 excludes any finite t-independent C when a>0. This is
    an actual counterexample to that specific conditional bound. Its
    original curvature has positive action, so it does not refute a
    charged original-field integral or RM23's divided seminorm.
    Separately, `H=1_E` gives `K^H(E)=1` whenever `K(E)>0`; this rejects
    importing an unchanged gap price into arbitrary future conditioning.
    The note does not identify that artificial tilt with every Z_A.
    **Fix:** none; no general inherited-law obstruction is proved.

17. **Persistent flux and filled-family payment — ACCEPT WITH SOURCE SCOPES**
    (lines 504–541). On compatible even tori the actual sign sums give
    `M_1=g^(X_2+alpha)P`, `M_2=g^(beta+(L-1)/2)P`, and `M_3=M_4=I`.
    For directions 1 and 2, expanding the displayed trace uses
    `tr(A* P A)=tr P` for unitary A, without assuming A and P commute.
    Positivity of P gives the unique maximizer and
    `delta=1-tr(P)/N=2(1-1/L)/N` despite zero gap.
    The RENEW tube recurrence gives a strictly positive input radius
    at each fixed finite horizon; its finite union of complement bounds
    tends to zero as the couplings grow. No infinite-horizon probability
    statement follows. The original tube charge and geometric fractions
    reproduce CHARGE. Its real all-cut estimate still needs C10's
    coupling/cut/depth restrictions. For fixed terminal n_R, the ratio
    of successive `B^R exp[-lambda L^(4R)n_R]` terms is precisely the
    displayed expression. Uniform summability for `n_R>=1` follows by
    comparison with n_R=1. MS23 adds only the stated output/source jets,
    with earlier fields integrated. Arbitrary local ancestors, retained
    fine jets and weighted full-reader histories are not thereby paid.
    **Fix:** none binding. For precision, insert “for fixed terminal n_R”
    before the ratio calculation at lines 531–533.

18. **Negative-result discipline and final framing — ACCEPT**
    (lines 543–624). The three tried mechanisms are not presented as
    exhaustive route families or independent logical walls. Q27 and Q28
    are failed sufficient estimates; Q29 is an exact, narrow counterexample.
    The local-reference, integrated transport and extracted continuation
    alternatives remain open. Named FR/KR/TC conditions have not been
    promoted into global estimates or new physical premises. Numerical
    nonexecution is stated, not relabeled a PASS. **Fix:** none binding.
    To avoid confusion with formal status vocabulary, the section 7.4
    heading could say “RENEW's counterexample remains valid” instead of
    “RENEW is retained”; lines 21–23 already exclude an audit promotion.

## Source quotations, locators and import checks

The author brief's quoted open task matches REFMATCH's section 7 table,
line 625. The relevant source arguments were inspected directly:

- REFMATCH lines 33–107 keep the reference-identification gap explicit;
  RM7–RM13, lines 180–311, require actual matching and joint factorization;
  RM14–RM17, lines 313–385, supply the finite score polynomials;
  RM18–RM24, lines 411–536, retain original reserves and distinguish
  regulated seminorms from regulator integration. The full 649-line
  note was read. None supplies Q25.
- REALRGA lines 30–180 define the actual quotient, original-source units,
  ordered `(6;[4])` norm and multiplicity regulator. Lines 184–312 give
  the product/quotient calculus and fixed-sector restrictions. Lines
  314–479 keep the joint inequality and exact factorization as inputs.
- JMBRB B10–B12, lines 176–221, give the normalized forward gap argument;
  B13–B16, lines 228–273, give the actual paired ribbons and older linear
  threshold. Its connected construction, lines 479–590, requires joint
  coefficient bounds, complete readers and exact factorization before a
  logarithm. ROUGH does not silently import these as established model
  estimates.
- CHARGE C5–C14, lines 94–266, contain the one-use filled-tube charge,
  cap comparison and extensive local bill. C20–C23, lines 397–486, keep
  reference endpoints and future tilts. C25/C25a, lines 511–533, require
  both creation control and fixed-terminal accumulation; they remain
  proposed routes. The equations cited by ROUGH have the stated scope.
- RENEW's paired contours and conventions are at lines 31–70. Its flux
  orbit, R9–R11, and tube estimates, R13–R15, are at lines 147–291.
  The finite horizon, compatible even torus and conditional-probability
  restrictions are substantive and were checked, not inferred from its
  title or prior review.
- MIXSMALL MS1 and its finite jet proofs are at lines 25–178; its actual
  zero-mean field is at lines 180–231. MS20, lines 322–349, retains the
  future tilt. MS21–MS23, lines 351–417, use a V-independent mass envelope,
  a source window, the scalar comparison restrictions and the additional
  output-weight condition. MS23 does not supply fine/exterior jets of a
  partly integrated local quotient, or an arbitrary weighted-reader sum.

The literature links resolve to the attributed primary papers:
[Dimock, The Renormalization Group According to Balaban — II. Large fields](https://arxiv.org/abs/1212.5562)
and [Brydges–Slade, A renormalisation group method. I. Gaussian integration and normed algebras](https://arxiv.org/abs/1403.7244).
Their abstract records support the method attributions. No theorem from
either paper is needed as an unproved step here; no claim of an exhaustive
literature search or novelty certification is made.

## Binding fixes, verification limits and handoff

**Binding fixes: none for the frozen partial research note.** The two wording
clarifications in items 17–18 are nonbinding. No source fix was applied.
The open mathematical obligations are not editorial defects: actual joint
capacity/charge production, local Q25 control, complete history envelopes
and full-root summation still require new work before the affirmative
target can be claimed.

Verification was analytic, including coefficient collection, reciprocal
recursion, exact contour witnesses, endpoint cases and the entropy sum.
No mathematical numerical experiment or formal proof checker was run.
`checks/rough_resource.txt` records the author's denied nice preflight; I
did not retest or bypass it, and do not certify unmeasured resource guards.
The numerical criteria remain NOT RUN. This is not verification of unrelated
arguments in the source notes, of general FR/KR/TC estimates, or of a full
Yang–Mills construction.

Only `REVIEW_ROUGH.md` was created by this review. No science source,
editable prompt, audit/ledger file or existing evidence was edited; no
commit was made. Any later source or premise change requires an affected
review against the identities above.

VERDICT: LAND

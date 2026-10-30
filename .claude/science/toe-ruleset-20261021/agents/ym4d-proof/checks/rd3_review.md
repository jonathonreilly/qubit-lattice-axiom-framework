# Independent mathematical review of RD3

No binding mathematical correction was found in the stated finite-volume or
conditional results. This note is suitable to land as **partial research
support**, with its present OPEN headline. It is **not** a completed uniform
B2/B3 theorem, a closed quantitative RG induction, or an audit verdict.
Removing those qualifications would require new proofs, not editorial changes.

The reviewed final input is `RD3.md`, 654 lines, SHA256
`55274cfe3d6c90b6eb6e2f5412bdb5633660f6e47054e1db52f8a1ca9ac3d3cc`.
I first reviewed all 593 lines of the preceding frozen input,
`b5368aa2a5706b0c2dbbc2931dcac1baefe0da3831c807e78f2b367bc22fb03b`,
then checked the complete added all-cut-reference argument, its surrounding
comparison, the revised obligation, and the current downstream statements in
`7c3385467a4aa6771451c1bf204908daa0b55e93345c8d52849030c96f850b5b`.
The final change narrows the STEP55 wording at lines 512–520 as requested
below; I checked that correction and the unchanged D25 equation. Line
references below refer to the final input.

This is **same-family / fresh-context review: Codex reviewing Codex**, in a
separate reviewer agent context. I did not author the candidate. Earlier
review verdicts, prior PASS lines, and the author log were not used as proof
evidence. The decisive checks below are written derivations from the displayed
definitions. No numerical physics experiment or external theorem was used;
tool execution was limited to source inspection, deterministic hashing and
writing this report. Same-family context separation reduces author carryover;
it does not establish cross-family independence or formal verification.

Applicable procedure: `PROCESS_LIGHT.md`, the exact `briefs_q/RD3/AUTHOR.md`,
`SCIENCE_WORKFLOW.md`, and the repository physics-claim-reviewer procedure.
The repository procedure matches the locally available `origin/main` snapshot
`01589af3faf806b736c42dc2f3bd625e9edead9f`; no remote-freshness claim is made.
The installed reviewer copy differed in model-selection wording, so the
repository version and its same-revision references controlled the review.

| Exact scientific input | SHA256 | Passages checked |
|---|---|---|
| `RD.md` | `a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5` | 1–145; 249–891, including R1–R17 and the chart factors |
| `LIB1.md` | `1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1` | 68–126; 216–438, including the set map and full-norm proof |
| `RECOVERY_CLUSTER_ASTRA.md` | `9c9264bd4d92b60798e48ccd2eb0ff230e221c3ffd2107c0f6443ec86de563cf` | 344–393, actual-factor identity and logarithmic variations |
| `SOURCE_LOCAL_HISTORY_RETURN_ASTRA.md` | `d2e9c49eedceb14b654f5be640e2b55efc16b902fd789acbc3d73c2849b9a850` | 118–142; 264–292, exact readers and completion minimum |
| `STEP55.md` | `aa785cf1ba03a53e79b52e8b9eb677927d18abb26178c4c018c3c37e7e1af0ce` | 500–558, especially the conditional quotient statement at 530–542 |

The process and brief hashes are respectively
`b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab`
and `03cc14b2f20ae6a2e247b1e28cac64db7394aac8398707f3129baaca94ba2ca7`.

**Line-specific mathematical findings and independent checks.**

1. **Positive failed history, lines 23–96: correct at the displayed cuts.**
   The two negative eigenvalues give determinant one for every N≥2.
   For L≥3 each marked e1 link and every plaquette containing it lie wholly
   inside its block; the two marks are too far apart to occur in one
   plaquette. Thus each affected plaquette is g or its inverse and has
   operator distance 2. All other plaquettes start at identity. Perturbing
   the four unitary factors, including inverse factors, changes a plaquette
   by less than 4δ=1/4. The bad-block set therefore stays exactly Y0.
   Its unique size-two component fails n0=1 independently of U1; there are
   no other bad components on this cap. This verifies the full recorded
   indicator, including absence of other failures, rather than only one
   local bad event. Its image lies in one next block, giving the stated
   sup-distance collar of 3^4=81 vertices and the active neighbour v*.

   Independently, partitioning the ambient entry cube with side
   δ/(2√2 N) gives Euclidean diameter δ/2 and at most
   (1+4√2 N/δ)^(2N²) cells. Group representatives cover SU(N) by translates
   of an open operator-norm δ-ball. Haar invariance and the union bound
   give exactly the stated mδ. Since each Wilson term is in [0,2] and
   each normalized kernel lies between exp(−2t) and exp(2t), restricting
   the original links to the witness cap reproduces l_h and u_h in D2–D3.
   There is no claim of a Peierls price in this calculation.

2. **Actual quotient and finite normalization, lines 98–168: correct.**
   In R6, multiplying the local Wilson factor by J=ρ/b cancels only the
   plaquettes in P1(B); the residue is precisely the positive exterior
   inverse a_B. It is independent of I(B), remains in D_h, and cancels in
   N_h/D_h. The omitted-reader factor is a_B^(−1) times every external
   kernel, as in D5. This also checks that earlier kernel normalizers
   have not been cancelled twice.

   A singleton L-block has 4L³(L−1) internal links and at most eight
   incident coarse kernels. Putting its internal links in identity caps
   makes every cut plaquette good regardless of the frozen exterior.
   Combining this with D3 yields D6; dividing the numerator upper bound
   by that lower bound yields D7 with exp(4t1 c_B), not exp(2t1 c_B).
   The marked-link cap proves numerator positivity as well. At η=1 the
   identity completion makes all collar plaquettes flat and straight
   anchor paths identity, establishing the stated successful-return patch.
   Summing all F1 before integrating uses R3's exact partition. Integrating
   each output kernel then gives ∫R_h=A_h and ∫p_2,h=1. The selected past
   history's weight A_h/Z0 remains necessary in the unconditioned mixture.

3. **Common complex domain, lines 170–223: correct finite result.**
   Expanding the kernel exponent difference at Vbar exp Z gives two trace
   terms, each bounded by N(exp(||Z||)−1); their factor 1/(2N) gives the
   coefficient t1 in D12. The source contribution is at most
   2u0 Σ|ε_p|. D11 makes these two contributions each strictly below 1/4.
   Old hard predicates do not read the new V, and their source dependence
   is absent, so compact-domain integration preserves holomorphy.
   For |H|≤r<π/2, averaging e^H stays in the convex sector |arg|≤r and
   has real part at least exp(−r)cos r. The logarithm bound in D13 follows
   from |Re Log|≤r−log cos r and |Im Log|≤r. These checks establish the
   actual denominators' nonvanishing, with real η only. They establish
   neither a volume-independent source radius nor holomorphy of a new
   moving completion/failure selector; lines 180–181 and 220–223 say so.

4. **Hard-event expansion and normalization, lines 225–304: correct
   conditional and negative statements.** Inclusion-exclusion subsets
   partition uniquely into support-overlap components, giving each sign
   and joint event in D14 exactly once. Only after taking interaction
   suprema may the mutually disjoint defect-coordinate sets factor under
   the fixed product reference. This gives the L1 majorant, not an
   assertion of independence for overlapping events. Checking RD's two
   rooted-tree bounds with atom weights exp((μ0+1)|S|) times their
   majorants leaves the additional exp(|S|) supplied by β=μ0+2.
   The supersolution then gives the stated q1 norm bound; the second
   connected-graph expansion uses the remaining unit of size weight.
   The holomorphy and fixed-event hypotheses of RD R16 remain necessary.

   For a prescribed event of mass p, integration of |1_E/p| is exactly
   one. This independently verifies D16 and shows why a smaller p cannot
   repair this particular small-species representation. It does not
   exclude extracting p and changing to a conditioned reference. The
   proposed conditioning factorizes only between S_E and its complement;
   internal correlations and the no-other-failures condition remain
   unresolved, as the ARGUED paragraph expressly states. The geometric
   failure-budget sum is valid under the displayed size and rooted-count
   hypotheses. None of those hypotheses is proved for this actual h.

5. **Integrated comparisons, lines 306–423: correct at finite scope.**
   Normalize the complete positive zero-source integrands before forming
   expectations. Inserting Ξ_h changes the law to Ξ_hν*/p_h, so the ratio
   of normalized integrals is exactly D17. Taking the ratio of the two
   sector bounds gives exp(−2r)cos r and exp(2r)/cos r. Their argument
   difference is less than 2r<1 on D_fin, so the displayed logarithmic
   difference is compatible with the principal branch.

   The added RC1–RC3 argument compares to the actual R8 reference.
   R8 summed over F1 gives Q_h=R_h/Z_A, including all replacement terms.
   The full U1 cap gives Z_A≥mδ^|E1| exp(−2u1 P1,tot−2t1|E2|);
   its elementary upper bound is exp(2t1|E2|). Dividing D10 by these
   bounds gives exactly both bounds on Q_h in RC1. In RC2 the reference
   exponent H_A has only terminal-kernel variations, whereas H_R also
   has the original sources. Both obey the common sector estimate.
   Finally, normalizing the real measure Z_A(V)dV by its own total mass
   gives ∫Q_h Z_A/Zbar_A=A_h/Zbar_A. Integrating kernels first gives
   Zbar_A=∫χ_A b1 and its stated cap bounds. The history mass is retained.

   For a general complex reference the triangle inequality gives D19
   with T_ref=∫|w|/|∫w|. The two-point calculation yields
   1+(e^a−1)/d and correctly refutes omitting this factor. It is not
   an SU(N) counterexample. Twice differentiating the finite source
   integral yields the positive sign u0² Cov(s_p,s_q) in D21.
   These scalar estimates supply no local connected-correlation decay.

6. **Full-hole norm, lines 425–473: correct implication.**
   Applying LIB1's proved full-norm map with M=81 gives 9M=729 and
   1+8M=649. Keeping the inactive labelled family adds one, giving 730.
   Independently, this one hole has 81 internal vertices and 8·27=216
   exterior face neighbours, hence 297 possible roots. Saturation adds
   at most 81 vertices. An active output root must already belong to X;
   an inactive output root requires X to meet this 297-vertex set.
   Sum first over those input roots and then over their input supports:
   this gives 297 exp(81μ)||K||_μ and the additional inactive cost one.
   The singleton adjoining the hole really has saturated size 82.
   No active norm was substituted for the full norm, and no input bound
   on the actual integrated K was manufactured.

7. **Prefactor identity, lines 475–531: correct conditional accounting.**
   The real change a=σQ^(−1/2)W contributes the Jacobian
   σ^d det(Q)^(−1/2). Replacing Lebesgue Gaussian integration by a
   normalized Gaussian contributes (2π)^(d/2); the normalized cut
   contributes Nχ. Combining these with c_N^n and exp(−S0) reproduces
   D24. Keeping the linear term, quadratic mismatch, Haar Jacobian and
   the full inherited insertion is essential and is done explicitly.
   The oriented side term and real complement remain additive before
   taking the logarithm. D26 is valid only with the stated compatible
   nonzero factors and logarithm branches. A varying Gaussian quadratic
   form alone contributes −(1/2)Δlogdet Q even when the residual interaction
   is zero; this checks the required diagnostic directly from the Jacobian.
   The 48u1 L^4 exp(4μ) real plaquette budget follows by counting at most
   24L^4 incidences and multiplying by 2u1. It is not a bound for log ρ.
   STEP55's cluster hypotheses and returned-activity norm have not been
   instantiated by this accounting identity.

   **Resolved scope correction, lines 512–520.** The intermediate revision
   said that this was "the quotient in STEP55". Although the surrounding
   text kept uniform estimates open, that wording could imply an already
   established identification with a separately specified STEP55 history.
   I requested that the sentence identify the RD quotient and call STEP55
   a prospective application, with history-convention matching still
   required. The final revision makes exactly that change. No equation,
   domain, constant or mathematical conclusion was altered.

8. **Finite recursion and failed estimates, lines 533–641: correctly
   distinguished from quantitative closure.** The measurable finite
   partition, compact integrations and bounded kernels justify Fubini at
   each finite level. A zero-total-mass child has zero positive integrand
   almost everywhere and contributes zero to subsequent integrated
   levels; no division by that child is licensed. This proves exact
   recursion, not stability of a uniform analytic norm. The listed failures
   concern an insufficient estimate or a precisely specified false
   inference. They do not imply a physical no-go or exhaust alternative
   reference constructions. The final OPEN and conditional-support
   declarations agree with this mathematical content.

**Disposition of every requested brief item.**

| Brief item | Supported result | Remaining obligation |
|---|---|---|
| Real history with failure and hole | Positive-mass size-failed history; explicit 81-block hole | Extension to the consumer's other cuts or histories is unproved |
| B2 common source/coarse domain | D11–D13, common finite-volume germ for real frozen η | Fixed radius, required complex boundary domain, and moving selectors |
| B2 nonzero reference | D6, D10 and RC1–RC3, with explicit positive cap constants | Uniform local reference/logarithmic budgets |
| B2 local prefactors and interactions | Exact allocation and one crude real Wilson budget | Actual inherited-density local decomposition and small nonlinear norm |
| B2 hard-cut mismatch and failure majorants | Exact integrated species expansion; normalized-species obstruction | Matched-law joint failure masses and multiplicities; no Peierls estimate is established |
| B3 comparison after integration | D17–D20 and the actual all-cut RC1–RC3 comparisons | Uniform local strengthening controlling connected source correlations |
| B3 full source norm through holes | D22–D23 with the inactive family retained | Input K estimate and compatible constants for growing/merged holes |
| B3 effective/history induction | Exact normalized finite recursion | Quantitative preservation of all analytic, reference and activity bounds |
| CX-R / STEP55 prefactor match | Full conditional identity and displayed remainder terms | Actual cluster hypotheses, local budgets and returned-activity norm |
| Failed-bound reporting | Exact failures are separated from unproved estimates | No broad obstruction or uniform completion follows |

**Binding corrections:** the STEP55 scope correction has been applied and
verified; no further correction is required for this frozen partial note.
The binding scope of this recommendation is the finite and conditional
content stated above. In particular, D15 must not be reported as established for h, D23
must not be consumed without its input norm and hole geometry, RC1–RC3 must
not be promoted to a uniform local bound, and D24 must not be treated as an
instantiated small-interaction theorem. The current text already preserves
these restrictions. The requested uniform theorem remains OPEN.

VERDICT: LAND

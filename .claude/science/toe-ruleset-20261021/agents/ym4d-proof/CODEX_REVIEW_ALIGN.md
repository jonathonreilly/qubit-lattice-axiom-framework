# PRE-STATED hostile review of ALIGN55

UTC registration: 2026-10-29 04:26:35 UTC (deliverable birth timestamp; the initially entered minute, 04:27, was rounded and is corrected here). Written before deriving or testing any target claim; the heading index and both errata blocks have been read. Two earlier header-creation attempts failed before writing (missing `python`, then an unescaped format brace).

Scope: independently attack ALIGN55.md. Bare lane filenames below are relative to `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/`. No git commands; all writes are confined to this deliverable. Large sources are located by string and read in bounded ranges. Computational arithmetic is exact, using plain Python. Review-loop supplies review discipline only; the owner's narrower source and write restrictions control. No audit ledgers, snapshots, or whole PROOF.md reads.

Targets and pre-stated refutation conditions:

1. RED′: reconstruct (H), (P1′), (P2-tw), and five background estimates ⇒ GA (A1)–(A2). Refutation: an unjustified representative-to-quotient step, missing premise, wrong exponent/constant, nonuniform quantifier, or circular inference.
2. NEC-E: rebuild the dual witness on every permitted slot and exact cc_Z line current. Refutation: an admissible representation breaks witness boundedness, an index/scale error changes the lower bound, or the x_0-only extension fails.
3. HC-1: verify left inverse, nested restriction, interpolation, and transpose from definitions. Refutation: an exact counterexample or hidden noncommuting/normalization assumption.
4. AX-SEAM: reconstruct boundary/interior amplification and compare the precise Dimock gauge claims. Refutation: wrong powers, inadmissible fields, stale criteria, or misattribution of regularity.
5. HC regularity: test whether DET/HB, subdivision, and twisted-charge counts supply the uniform estimates. Refutation: a failed prerequisite, divergent sum, unproved upgrade, or gate incapable of failure. Examine L=3 versus the 5-adic P3 failure and weighted r^{-7} tails.
6. R2-glob♯: enumerate thirteen inputs and their meanings/statuses. Refutation: missing or mislabeled inputs, symbol collisions, stale minima/quantifiers, or tautological/vacuous/unsatisfiable checks.

Verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. Source status labels are not evidence. Locating strings accompany live file:line references. No PASS is reported without evidence.

## Findings (appended incrementally)

### F1 — RED′ repairs the quotient step, but contains a false intermediate identity

Verdicts: **CONFIRMED** for the corrected conditional reduction; **REFUTED** for the sentence claiming `(H_Z − H_1)x_E` satisfies `Ξ_1^Ty = −τ_Z(y)`. Claim status: **CONDITIONAL**.

Locations: `ALIGN55.md:218–232`, locating “Lemma RED′”, “which holds for y = (H_Z − H_1)x_E”; erratum `:560`, “direct bound”. Here `D := Ξ_Z−Ξ_1`, `Λ := Λ_W`, `Π := I+Ξ_1Λ`, `Υ := I−DΛ`.

Re-derivation: `ΥΞ_1=Ξ_Z`; hence `E_ΥΞ_1=0`. Put `x_E=Π_Ex`, `λ=Λx_E`, `u=Dλ`. Then `Υx_E=x_E−u`, `Υ^TH_Z=Π^TH_Z`, and `Π^TH_1=H_1`. Thus

`E_Υx = (H_Z−H_1)x_E − Λ^Tτ_Z(H_Zx_E) − H_Zu + Λ^Tτ_Z(H_Zu)`.

This uses `Ξ_1^T(H_Z−H_1)x_E=−τ_Z(H_Zx_E)`, NOT `−τ_Z((H_Z−H_1)x_E)`. The latter differs by `τ_Z(H_1x_E)` and has no stated reason to vanish. The four terms in the author's subsequent norm inequality are nevertheless the correct four terms.

Using the specified hypotheses gives exactly

`t_+ ≤ C_E(1+C_NCη+C_AC C_𝒞η)`,

`t_* ≤ 1+(C_NS+C_tw)η`,

`δ_Υ ≤ η C_E[C_HD+C_tw C_FW(1+C_NCη)+C_FW C_AC C_𝒞(1+(C_NS+C_tw)η)]`.

The reference bound `|||Π_Ex|||≤C_E[x]` now explicitly supplies the missing quotient-to-representative control; no bound on the W representative is needed. Invertibility follows directly from `||ΛDμ||_𝒞≤C_𝒞 C_ACη||μ||_𝒞<||μ||_𝒞`. This is the final erratum's condition. The original detour through Π_E would give `(C_𝒞 C_E+C_{E𝒞})C_ACη`, rather than `(C_𝒞+C_{E𝒞})C_ACη`; that route is unnecessary and has already been superseded by the final erratum. The hierarchy (H) is not used in RED′ itself; it supports construction of a candidate with the required completion bound. None of these algebraic deductions proves (P1′), (P2-tw), or the background bounds.

### F2 — HC-1 algebra survives independently

Verdict: **CONFIRMED**. Claim status: **PROVEN** for the finite-dimensional algebra under the stated interpolation/constant-reproduction hypotheses, not for uniform analytic bounds.

Location: `ALIGN55.md:293–306`, locating “Lemma HC-1 (algebra)”. Write `D_l=I−S_{0,l}R_l` (a detail projector, not the background D of F1). `R_lD_l=0` and `R_lS_{0,l}=I` imply `R_lλ_l=λ_{l+1}`. Descending induction gives nested restriction and pins λ_0 at level-k roots. For a gauge gradient, `Δ_l^{-1}d_l^*d_lν_l=ν_l−mean(ν_l)` and `D_l1=0`, so `μ_l=−ν_l+S_{0,l}ν_{l+1}` and `λ_l=−ν_l`. This proves the left inverse and hierarchy for every k.

Expanding the recursion and taking the actual transpose yields `c_m=−d_mΔ_m^{-1}(I−R_m^TS_{0,m}^T)S^{(m→0)T}q`. If q is supported on level-l sites and m<l, repeated `S_0^TR^T=I` leaves a charge in `Ran R_m^T`, annihilated by the detail transpose. Its mean is zero because the primal detail kills constants; the inverse Laplacian is therefore defined. No commutation of the Laplacian with interpolation was used. The commuting link scheme is an additional useful identity, not needed for these HC-1 conclusions.

Incremental checkpoint UTC: 2026-10-29 04:28:18 UTC

### F3 — NEC-E's witness and exponent are correct; the derivative-only pure-gauge example is not

Verdicts: **CONFIRMED** for DW, LC, and the obstruction with a nonzero sampled twisted charge; **REFUTED** for the purported sufficient example “every small pure gauge ... [∂_μg,v] ≠ 0 at y_0”. Claim statuses: the specified obstruction **PROVEN**; the wider example **GAP** until replaced by a finite-link condition.

Locations: `ALIGN55.md:146–194`, locating “Lemma DW”, “Lemma LC”, “Proposition NEC”, “Corollary NEC-E”; norm cross-check `COFUN_CC.md:130–135`, “Norms”.

For `x^φ=(dφ,0,...)`, `ddφ=0` kills every G slot; every j_l with l>0 and every r_l with l>0 also vanishes. Root covariance gives `r_0(x^φ)=d(ev^(1)φ)`. Thus for EVERY representation, not just the minimizing one,

`|y(x^φ)| ≤ 2d|v′| (L^(−3k)||j_0^c|| + L^(2−(2+θ)k)||s||_R)`.

The coefficient of the j term is no larger than that of the s term since `(1−θ)k+2>0`. Taking the infimum proves DW with its factor `2d` (8 in d=4). No representation-dependent cancellation can defeat this lower-bound witness.

For a closed covariant line, incoming transport equals the outgoing current; closure is exactly `Ad_hol v=v`. All covariant site charges therefore vanish, including at non-root sites. Its one-current representation costs at most `L^((3+θ)(k−l))|v|`. The exact local flat charge is `q(y)=j_in−Ad_Zin^(−1)j_in`.

For ANY level-0-only left inverse, `x^φ` and `Ξ_1φ` have the same level-0 field, so `Λx^φ=−φ`, provided y_0 is not a pinned root. The whole transformed cc_Z source pairs to `−<q(y_0),v′>`. Choosing v′ along that charge gives the exact statement

`t_* ≥ (|q(y_0)|/|v|) L^((2+θ)k−2−(3+θ)(k−l))/(2d)`.

At l=k−1, the exponent before expanding the charge is `(2+θ)k−5−θ`. Set `v̂=j_in/|v|` (or start the line at its incoming link). Since `z=z^c/L`, the leading bracket adds one inverse L, giving **`(2+θ)k−6−θ`**, as claimed. More precisely `1−exp(−ad_z)=F(ad_z)ad_z` with `F(A)=I−A/2+...`; therefore the norm ratio to the bracket is `1+O(||ad_z||)` uniformly even near a commuting direction. No independent c_N is needed. A fixed family with a nonzero top-link charge yields unbounded t_*; merely nonzero charges that shrink with k do not.

Counterexample to the derivative-only example: take `g(u)=ε sin(2πL(u_μ−a)) A` on an integer-side torus, with a the coordinate of a level-(k−1) site and `[A,v]≠0`. At every such site g=0, hence all sampled level-(k−1) links are identity and q=0. Nevertheless `[∂_μg(a),v]=2πLε[A,v]≠0`. L is fixed and ε may be arbitrarily small in any fixed smooth norm. Replace the derivative condition by the stated nonzero finite-link charge condition. This does not invalidate the obstruction: choose instead a fixed smooth pure gauge whose values at the two endpoints actually differ in a noncommuting direction.

The general NEC inequality controls a CHARGE PAIRING. A bare O(1) response value does not by itself lower-bound its sum: values constant around a line pair to zero because the flat line charges sum to zero. The unrestricted gloss at :185–186 requires a noncancellation hypothesis; it is **NOT-VERIFIED** as written. NEC's zero response test for hierarchical Λ proves a necessary test is passed, not (P2-tw).

Reproduction: `python3 -I -B checks/al55_nec.py` (from the lane path) produced all A1–A8 checks and C1–C5 controls successfully. Exact outputs reproduced: `q(y_0)=(-1328/4485,-112/69,10624/4485)`, pairing `−1712/897`; hierarchy pairing zero. These finite d=2 checks do not prove uniformity; the all-representation derivation above does the work.

### F4 — An uncorrected factor L² remains in the AC𝒞 display

Verdict: **REFUTED** for the displayed equality, not for its weaker upper bound or its q-cancellation. Claim status of the full (AC𝒞) estimate: **ARGUED**; its review verdict is **NOT-VERIFIED**.

Location: `ALIGN55.md:238–241`, locating “uniform in q exactly because”. The powers AFTER the printed prefactor add to

`(1+θ)q + q − (q+1) − (q+1) − θq = −2`.

The left side already contains `C p_L² L^(−2)`, so its full coefficient is **`C p_L² L^(−4)`**, not `C p_L² L^(−2)`. For L=3 the literal coefficients are **1/81 versus 1/9** after removing `C p_L²`. Independent Fraction calculations at θ=1/2, q=0,2,4 reproduced 1/81 each time. The clean power count starts with `C p_L²` (no extra L^(−2)); it then ends with `C p_L² L^(−2)`. The proposed bound remains a valid weakening of the literal smaller product, but the equality and provenance of its prefactor must be fixed.

The q-dependent factor for a gradient exponent β is indeed `L^((θ−β)q)`. That is sufficiency bookkeeping for this estimate, not a theorem that every possible GA alignment must have exactly that regularity.

### F5 — The subdivision arithmetic is reproducible; P3's failure is honestly disclosed

Verdict: **CONFIRMED** for the exact finite certificates and their stated L=3 scope. Claim status: **PROVEN** finite algebra; analytic reconstruction still consumes the specified subdivision regularity implication.

Locations: `ALIGN55.md:313–318`, `:352–363`, `:411`; `checks/al55_sub.py`, locating “c = {e: b*v”, “norm_iter”, “P3 s5”; `checks/al55_sub_criteria.md`, “Method”. I independently generated each mask by cubic Lagrange products, checked degree-0 through degree-3 reproduction at each residue, divided twice by σ using low-to-high elimination, and convolved exact Fraction masks. This differs from the author's hardcoded s3 mask/top-down polynomial division. No floating arithmetic was run. The original script does use floating conversions solely for displayed decimals; it was inspected, not executed.

For L=3, at n=5: `||S_c^5||=875065/14348907`, and `||S_c^5||²3^5=765738754225/847288609443<1`. At n=7: `||S_c^7||=122416585/10460353203`. Exact integer comparisons give `norm^500·3^(7·289)<1` and `norm^5·3^21>1`: the certificate exceeds **289/500 = 0.578**, but does not certify 3/5. Thus the θ≤1/2 assembly is within the certified window; there is no stale θ substitution here.

For L=5, n=1,...,5 give `norm²5^n` respectively `441/125`, `62001/15625`, `6456681/1953125`, `593848161/244140625`, `51447766041/30517578125`, all greater than 1. **P3 fails exactly as reported.** This is failure of this bounded-depth certificate, not proof that the scheme lacks regularity. These gates can fail and did; they are not tautologies. The source prints overall `all ok = False`, rather than hiding P3.

The analytic mechanism is also appropriately matched: with divided first differences `D_n=L^nΔf_n`, their differences propagate by `S_c`, `c=La/σ_L²` (a harmless monomial shift depends on the difference convention). A contracting n-step norm bounds differences of the derivative approximants geometrically. The local refinement difference is controlled by those differences, giving the C^{1,β} limit and finite-level bounds once the stable reconstruction is written out. This does not prove the Coulomb-detail bounds.

Incremental checkpoint UTC: 2026-10-29 04:33:19 UTC

### F6 — AX-SEAM: corrected interior area is right; the growth gate cannot certify a norm failure

Verdicts: **CONFIRMED** for the seam identity and corrected interior scaling; **NOT-VERIFIED** for the complete norm match needed by the bounded-input (P1′) obstruction; **REFUTED** for treating unnormalized output growth of the script's linear torus field as a test of boundedness. The curvature part at general cell boundaries is **NOT-VERIFIED** as a universal lower bound. Claim statuses: exact identities **PROVEN** and the complete norm obstruction **CONDITIONAL** on the norm matching stated below; a general nonzero curvature asymptotic requires geometric/noncancellation hypotheses.

Locations: `ALIGN55.md:257–277`, “Proposition AX-SEAM”; errata `:326–333`; `checks/al55_ax.py:57–72`, “curvature_chain”, and `:106–143`, X1–X4; `checks/al55_ax_criteria.md`, “Amendment A1”.

The recursion gives `λ_l=−Φ_l` and hence the representative `x_l(b)+Φ_l(y)−Φ_l(y′)` exactly. It is a curvature area only for a closed loop built from a single compatible field. For distinct top roots one must retain the open root-to-root chord, as the erratum now does. A fixed curvature tensor may pair to zero with a particular signed area; an arbitrary constant-curvature field is not a lower-bound witness on every seam.

Independent all-k calculation for the actual interior test (L=3, l=0): let `a=ρ_0=3^(−k)`, `b=ρ_(k−2)=1/9`, and `H=Σ_(i=0)^(k−3)ρ_i=(b−a)/2`. The two tested sites have balanced ternary displacements `(H,H)` and `(H+a,H)` from the top root. With `w=(0,u_1)`, the permutation-averaged path integrals are `Φ(y)=H²/2` and `Φ(y′)=bH−H²/2`. Therefore

`rep_own=−(b²−a²)/4`,

`rep^c=−(3^(k−4)−3^(−k))/4`.

This reproduces **0, −2/27, −20/81** at k=2,3,4 and predicts **−182/243** at k=5 by exact rational arithmetic. The asymptotic interior power is **k−4**, as the erratum says; at general level l it is **k−l−4**. The same scale conversion of a nonzero local fan area at s=k is `ρ_(k−1)²/ρ_l=L^(k−l−2)`, with the separate chord contribution. The obsolete uncorrected power **k−l−1** in :249/:269/:271 is not the corrected curvature-area power.

**The test's input norm is not bounded.** `curvature_chain` wraps the linear function around the torus. Across that wrap its coarse field derivative has magnitude `3^k−1` at level 0. Thus X3′ can pass while both input and output norms grow together; it does not decide failure of (P1′). Restricting the inspected links away from the wrap does not remove the wrap from the GLOBAL norm. The amendment replaces an incorrect exact-scaling equality by a discriminating finite growth comparison, but it does not add normalization. Its recorded pre-script date is documentary evidence only; actual creation chronology was not independently reconstructed. Re-running the script reproduced X1/X2/X4 at k=2,3,4, X3′, XC1 and ratio 10/3.

**A bounded-input obstruction, independent of that gate.** Take a constant su(N) component A in direction 1 at level k−1 only: `x_(k−1)(b)=A/L`; all other x_l=0 and x_k=0. The levelwise coarse C^{1,α} norm is |A|. All residuals vanish except the last two, which are spatial constants: `r_(k−2)=−A/L` and `r_(k−1)=A`. Thus residual Hölder parts vanish and every sharp residual weight is at a fixed distance from the top, independent of k. The N_res used in the named flat norm is a residual Hölder quantity (BGT55 “Corollary RW♯”); this witness needs that stated meaning, not any unintroduced norm on the gauge itself.

At the top detail level, `λ_(k−1)` takes consecutive values separated by `−A/L`. At every finer level the recurrence merely copies these values into descendant blocks. Across a fine link separating two adjacent such blocks, **`|∇^cλ_l|=|A|L^(k−l−1)`**, while the input norm stays bounded by an L,θ-dependent multiple of |A|. Under that stated residual-Hölder meaning of N_res, this proves failure of the all-x (P1′) assertion. The full definition of N_res was not present in the permitted source ranges, so this review does not independently certify that remaining norm match. It also makes the W representative's field norm unbounded, so (P1) fails. A one-dimensional exact recurrence (embedded unchanged in four dimensions) gave derivatives −3, −9, −27 at l=0, L=3, k=2,3,4, with A=1. This is a top-residual witness, not a correction to the curvature-area exponent.

The comparison with Dimock is **CONFIRMED in its stated limited sense**: §3.5 identifies the Landau/Feynman minimizer H_k, relates the axial minimizer by `H_k^x=H_k+dD_k`, and assigns regularity/decay to H_k. The source treats an abelian model and averaged-field constraints; it does not establish a four-dimensional nonabelian regularity theorem for this soft-chain transcription. [Dimock, Covariant Axial Gauge, §3.5, items following (84)](https://arxiv.org/html/1410.2798).

Incremental checkpoint UTC: 2026-10-29 04:37:12 UTC

### F7 — DET/HB and P2-tw are plausible conditional estimates, not a completed uniform analytic proof

Verdict: **NOT-VERIFIED** for the full all-k, all-T estimates (P1′), (P2-tw), and (AC𝒞). Claim status: **ARGUED**, with the explicit gaps below. Conditional power counting and summability are **CONFIRMED**. Locations: `ALIGN55.md:339–394`, “Lemma DET”, “Lemma HB”, “Proposition P2-tw(HC)”, “What is still missing for T3”; :235–242, “Why θ appears”.

**DET.** If the periodized detail kernel has the stated near/far estimates and annihilates affine 1-forms, its estimate follows. In four dimensions the corrected near sum is `Σ_(|n|≤2L)|n|^(−3)|n|^(1+α)`, bounded by a constant times `L^(2+α)`. The far sum is `L^4Σ_(|n|>2L)|n|^(−6+α)`, also of that order because its radial integrand is `r^(α−3)` and α<1. The added near-field term `CL^(−3)` contributes the same order. Multiplying by `ρ_l^(2+α)` gives `ρ_(l+1)^(2+α)`. Beyond physical distance one, the stated linear remainder bound gives `O(L^4ρ_l^4)||x||_C1`, which is smaller for ρ_l≤1 and 2+α<4.

What remains to prove is not just a decimal value for C_D: the torus-uniform Green derivative bounds, the treatment of periodization and zero mode, and the affine-annihilation/cutoff argument must be established for this specific interpolatory detail operator. An affine function is not a globally periodic torus datum; polynomial reproduction by itself does not discharge that limiting step. The source labels this ARGUED and names the missing Green bounds, appropriately. Its phrase “complete except ... bounds” understates the periodization/moment bookkeeping that accompanies them.

**HB.** Given the uniform finite-level basis estimates claimed at :354–355, the sum has no hidden level-count loss. With amplitude `Mρ_(m+1)^(2+α)`, its gradient is bounded by `CML^(2+α)Σρ_m^(1+α)`. For a Hölder quotient at separation h, coarse scales contribute `CML^(2+α)h^(β−θ)Σ_(ρ_m≥h)ρ_m^(1+α−β)` and fine scales contribute `CML^(2+α)h^(−θ)Σ_(ρ_m<h)ρ_m^(1+α)`. Both are bounded geometrically for β>θ and β<1<1+α; the latter is O(h^(1+α−θ)). These estimates require the actual stable finite-level/tensor reconstruction bounds, not merely one printed contraction number. The L=3 certificate has the right β margin; L=5 has no such certificate at the tested depths.

**P2-tw: locality is algebraic, size is additional.** HC-1 puts a level-l charge only in output levels m≥l. For point charges, bounded interpolation iterates and compact support give `||Q_m||∞≤C L^(4(m−l))a`. The transpose detail has moments through degree 3 if the primal interpolation reproduces them. Its Coulomb gradient has a summable far tail under the stated kernel estimates. For a divergence charge, the commuting pair transfers it to `d^T S_1^{T(m−l)}J`; the expected transpose column count is `L^(3(m−l))`: one factor L^(−(m−l)) in the differentiated direction, times a support volume L^(4(m−l)). Uniform stability of the normalized derived scheme is the missing bound behind that count. H8 alone establishes no such norm estimate.

The insertion of source sizes also needs SUMS over all input levels l≤m, not only an estimate for one slot. Keeping the discarded weights repairs this bookkeeping conditionally:

- j_l: the output weighted price is bounded by `Cη L^(−(1−θ)(k−m)) π_l(j_l)`. For l≥1, sum `π_l≤L^(−θ(k−l))||j||_Pc`; the geometric sum is finite for θ>0. Handle j_0 separately with its P0 norm.
- G_l divergence: retain `L^(−θ(m−l))` after using the Y weight `L^(θ(k−l))` (up to the fixed index shift in ω_l). This is summable. Curvature point charges have their own bound `C|F_l^c||G_l^c|L^(−(1−θ)(k−m))`; they should not be compared to |z| by dividing by |z|, which can vanish.
- s_l divergence: `|z_l||s_l|≤Cη L^(−(q+1))L^(−θ(q+1)−2q)||s||_R`, q=k−1−l. Multiplying by `L^(3(k−l))L^(θ(k−m))` yields **`Cη L² L^(−θ(m−l))||s||_R`**. Summing l≤m costs at most `(1−L^(−θ))^(−1)`.
- s_l point charges: the printed upper estimate contains `a_q L^(−(1+θ)q)`; a linear a_q is summable over q. Root placement at level l+1 can improve fixed L factors, and does not worsen that bound.

This confirms that the quoted exponents have room for a uniform result, conditional on the exact all-order slot decomposition and kernel/iteration bounds. Those analytic statements have not been proved by the scripts. In particular, the s-slot's phrase “has the CEN2 structure” is not itself a derivation of the all-order linearized residual. The lower-order power count cannot close (HD) after the earlier BCH identity was refuted.

**Weights.** A polynomial tail bound `r^(−7)` in dimension four is summable without exponential weights, but does not furnish an estimate against `exp(mr)` for m>0 uniformly in torus size. The weighted conclusion correctly stays **OPEN**. This is a limitation of the supplied estimate/construction, not proof that every exact hierarchical alignment lacks exponential locality. Likewise, an unspecified partition-of-unity construction cannot be ruled out merely by saying it loses linear reproduction; moment-preserving partitions/interpolants exist.

**Exact algebra witness supplement to F1.** Set `a=1/7`, `Ξ_1=(1,0)^T`, `Ξ_Z=(1,a)^T`, `H_1=diag(0,1)`, `H_Z=[[a²,−a],[−a,1]]`, `Λ=(−1,0)`, `x_E=(0,1)^T`. Both required kernel identities hold. But for `y=(H_Z−H_1)x_E=(−a,0)^T`, `Ξ_1^Ty=−1/7` and `−τ_Z(y)=0`; the corrected `−τ_Z(H_Zx_E)=−1/7`. This exact counterexample was executed with Fractions.

Incremental checkpoint UTC: 2026-10-29 04:39:26 UTC

### F8 — Gate audit: what can fail, and what cannot be inferred from a pass

Verdicts: **CONFIRMED** for the reproduced finite outcomes and the stated limited scope of most gates; **NOT-VERIFIED** for any promotion of these gates to uniform analytic estimates. **REFUTED** for the norm-failure interpretation of unnormalized X3′ (F6).

Locations: the four named `checks/al55_*_criteria.md` and corresponding scripts; locating strings are the exact gate identifiers below. No check script was allowed to write files. `al55_nec` and `al55_ax` were reproduced directly; subdivision arithmetic was independently rebuilt; `al55_hcg` code and its output were inspected, but its 27×27 exact elimination was NOT rerun on the shared machine. The proof of HC-1 in F2 is independent of that output.

| Gates | What can actually be falsified / limitation |
|---|---|
| nec A1, A2 | Transport direction, line closure, constant norm, and a nonzero unpinned flat charge. Curved-holonomy C1 supplies a real failure control. |
| nec A3, A4 | Left-inverse sign and the x_0-only response on the chosen forests. C2 changes normalization; C4 moves the witness to a pinned root. They test actual maps, but not S_E's Neumann construction. |
| nec A5, A6 | Summation by parts and the nonzero/zero pairings. These are algebraic consequences, not a numerical computation of the infimum defining N. The nonzero clause prevents a vacuous zero-current pass. C3 distinguishes hierarchical behavior. |
| nec A7a, A7b | Contour-root covariance and the two surviving slots. C5 shows deleting the s_0 term changes the answer. Random representations do not exhaust all representations; the dimension-free proof of DW supplies that quantifier. |
| nec A8 | The sampled hierarchical map ignores x_0 at level 1 and responds to a sampled change in x_1. It does not establish a norm bound. |
| hcg H1, H2 | Left inverse and actual restriction of λ_0 versus stored recursion levels. K1/K2/K3 are genuine failure controls; H2 is essential because stored level locality alone would be true by the program's recursion. |
| hcg H3, H4 | Structural hierarchy and a zero coarse response. They pass for many arbitrarily large operators with the same dependence pattern; no completion estimate follows. |
| hcg H5 | Transpose pairing and the vanishing lower-level currents; K4 detects omission of the coarsening transpose. It establishes no bound on nonzero currents. |
| hcg H6 | The homogeneous recursion when x_l=0. This is close to a direct check of the definition; it cannot test smoothness, moment bounds, or stability of its iterates. |
| hcg H7, H8 | Interpolation/reproduction and commuting discrete derivatives; K5 detects the wrong link mask. H8 is an identity, not the transpose column-norm estimate used in §6.2(B). |
| sub P1, P4a, P4b | Exact sum-rule/interpolation checks; independent polynomial tests in F5 additionally verify actual cubic reproduction. |
| sub P2, P3 | Finite-depth operator-norm thresholds. P3 really fails. C1 rules out certification of the linear hat scheme and C2 detects the perturbation. No conclusion about all larger depths is licensed. |
| ax X1, X2 | Left inverse, hierarchy, and unfolding of the same path recursion. XC1 checks sensitivity to permutation averaging. None computes a quotient norm or a background defect. |
| ax X3′, X4 | Two nonzero curvature outputs grow; pure-gauge outputs vanish. The wrap-dependent input norm is uncontrolled, so these gates cannot decide (P1′). |

The current filesystem metadata is consistent with the stated pre-script amendment: axial criteria birth **04:12:07 UTC**, modification **04:12:35 UTC**, axial script birth **04:17:33 UTC** on 2026-10-29. Subdivision criteria birth/modification **04:10:40 UTC**, script birth **04:11:08 UTC**, modification **04:11:32 UTC**. This supports the recorded chronology, without pretending metadata authenticates every prior draft. The failed P3 was not concealed by an amended acceptance gate.

### F9 — R2-glob♯ is an honest conditional reduction after repair, not a completed R2 theorem

Verdicts: **CONFIRMED** for the implication from the full uniform hypotheses (with F1's corrected identity); **NOT-VERIFIED** for their analytic realization. Claim status: **CONDITIONAL**, not PROVEN as an unconditional background-transfer result.

Locations: `ALIGN55.md:398–424`, locating “Theorem R2-glob♯”, numbered input table and its proof; `BGT55.md:172–193`, “Theorem GA”. The thirteen rows name the required layers. Several rows bundle more than one actual hypothesis; “13” is a table-row count, not an assertion of thirteen independent mathematical assumptions.

| Row | Input and review disposition |
|---|---|
| 1 | BFT-0 existence and global smallness `η=C_0ε`. **CONDITIONAL / NOT-VERIFIED here**. The three named BFT-0 premises remain assumptions. No existence theorem was rebuilt in this narrow review. |
| 2 | RW♯ flat inverse. **CONDITIONAL input** at exactly its stated source/quotient norms; earlier CODEX_REVIEW_BGT explains its named-input implication. This review does not promote its underlying flat analytic theorems. |
| 3 | GA, GA-slice and kernel inclusion at a critical background. GA's quotient argument was rebuilt below; GA-slice identities were rebuilt in F1. The critical-background Ward identity remains required. |
| 4 | RED′. **CONDITIONAL / CONFIRMED after F1's local proof correction**; its displayed t_+, t_*, δ_Υ constants survive. |
| 5 | S_E reference representative estimate. **CONDITIONAL input** in this review. The second, ARGUED Schauder half of (E) is unnecessary after the final invertibility erratum; do not silently require it through the old proof. |
| 6 | HC-1. **PROVEN / CONFIRMED** finite-dimensional algebra (F2). |
| 7 | SUB for L=3. **CONFIRMED** finite certificate, including the margin >289/500>1/2; regularity uses the standard implication spelled out in F5. No claim for L=5 at the registered depths. |
| 8 | DET + HB ⇒ P1′. **ARGUED / NOT-VERIFIED** as an unconditional uniform estimate. The exact missing kernel/reconstruction obligations are F7. |
| 9 | Twisted-charge completion. **ARGUED / NOT-VERIFIED**. Slot locality and CP are algebra; kernel norms, all-level sums and exact all-order residual bookkeeping are additional analytic obligations. |
| 10 | TR-1 at the actual critical background. **CONDITIONAL input / NOT-VERIFIED here**. Its source is explicitly a named-input implication; “CONFIRMED” in the prior review is not unconditional evidence for every new background. |
| 11 | AC𝒞. **ARGUED / NOT-VERIFIED**, with the literal prefactor equality refuted in F4. Need both flat and covariant sharp bounds, with the actual Jacobian/linearization conventions. |
| 12 | NC and HD on S_E representatives; NS; FW on all relevant fields. **ARGUED / NOT-VERIFIED**, with a substantive **GAP** in the all-order HD derivation. The admitted need to replace the false BCH-based term list cannot be discharged by the algebra of RED′. |
| 13 | Uniform smallness. **CONDITIONAL / CONFIRMED**, once the preceding constants and their domains really are independent of k,T and ε on a fixed neighborhood. |

Independent assembly: on `Q=X/Ran Ξ_1`, the flat hypothesis gives a bijective `h_1:Q→cc_1` with `||h_1^(−1)||≤C_♯`. Alignment and the two kernel identities make `E_Υ` descend to `e:Q→cc_1` with `||e||≤δ_Υ`. Thus `h_1+e=h_1(I+h_1^(−1)e)` is invertible for `C_♯δ_Υ<1`. Pulling the source back and the class forward gives **`C′_b=t_+t_*C_♯/(1−C_♯δ_Υ)`**, and invertibility of Υ gives `Ker H_Z=Ran Ξ_Z`. No relative Hessian bound or unproved kernel equality at Z was inserted.

Smallness can be chosen without a stale minimum. Fix an admissible η_0 and let

`A_0=C_E[C_HD+C_tw C_FW(1+C_NCη_0)+C_FW C_AC C_𝒞(1+(C_NS+C_tw)η_0)]`.

For η≤η_0, `δ_Υ≤A_0η`. Choose `η_b≤min(η_0,1/(2C_𝒞C_AC),1/(2C_♯A_0))` and `ε_b=η_b/C_0` (omit a reciprocal constraint if its denominator is zero). Both Neumann margins are then at most 1/2. This is a conditional parameter choice, not a fabricated numerical ε_b. Uniformity requires that η_0 and every constant already be fixed independently of the quantified k,T,V.

**Symbol/quantifier audit.** `ρ_l` is the mesh spacing at :68 but `ρ_l(z)` is the soft background residual at :235/:371/:382; these must not be interchanged. `q` is depth at :68/:382 and a charge at :162/:303; F3 uses q(y), F7 uses depth q. `S_0` is the scalar interpolation at :295, not a source component S_0 or the S_E slice. `C_♯` is the flat inverse constant (:84), `C_𝒞` the gauge regularity bound (:213), `C_E` the reference bound (:215), and `C_tw` the completion constant (:109/:367); none was substituted for another. κ_l is the penalty coefficient and κ_F the curvature action (:370). θ remains the residual/class exponent; the final assembly narrows it to θ≤1/2 and L=3. No stale β>θ assertion is used for all odd L. There are no explicit PROOF.md numerical line citations in the reviewed ALIGN55 claims to validate; no stale PROOF line number was assumed. The few PROOF string-search hits supplied no scientific authority.

The strong phrase “the source half forces hierarchical dependence” must be read only as NEC's quantitative pairing obstruction. Passing NEC is not equivalent to (P2-tw), and neither (H) nor a favorable transpose identity alone supplies a uniform source bound.

Incremental checkpoint UTC: 2026-10-29 04:41:15 UTC

### F10 — The axial erratum's distance bound is still L=3-specific

Verdict: **REFUTED** for the displayed distance bound when read over the file's declared odd L≥3 domain; **CONFIRMED** at L=3. Claim status of the general-L quantitative statement: **GAP** until the fixed-L factor is restored.

Locations: `ALIGN55.md:67`, “odd L ≥ 3”, and `:327–328`, “over a distance ≤ dρ_(s−1)”. A level-s block has level-(s−1) children with coordinate offsets `−(L−1)/2,...,(L−1)/2`. The longest permutation-axial path from its center has **`d(L−1)ρ_(s−1)/2`** steps in coarse distance, not `dρ_(s−1)`. At d=4,L=5 the maximum is **8ρ_(s−1)**, whereas the printed bound is **4ρ_(s−1)**. This is an exact lattice count, with no numerics or asymptotic assumption. At L=3 both expressions agree. Area prefactors may consequently contain `((L−1)/2)²`; for fixed L this does not change the corrected k−l exponents. The L=3 theorem is unaffected, but the erratum is not a uniform-in-L geometric calculation.

## Summary table

| Finding | Verdict | What survives / what changes |
|---|---|---|
| F1 RED′ | CONFIRMED reduction; REFUTED intermediate identity | Exact constants survive; replace τ_Z((H_Z−H_1)x_E) by τ_Z(H_Zx_E). Use the final direct invertibility argument. |
| F2 HC-1 | CONFIRMED | Left inverse, nested restriction, hierarchical transpose, homogeneous subdivision. No analytic norm bound follows from algebra alone. |
| F3 NEC-E | CONFIRMED finite-link obstruction; REFUTED derivative-only example; NOT-VERIFIED O(1)-value gloss | Exact dual witness and exponent `(2+θ)k−6−θ` survive. Require nonzero sampled charge with a k-independent lower size for the asymptotic assertion. |
| F4 AC𝒞 prefactor | REFUTED displayed equality | Printed product is `C p_L² L^(−4)`, not `C p_L² L^(−2)`; L=3: 1/81, not 1/9. Remove the redundant leading L^(−2) to obtain the intended upper bound. |
| F5 SUB | CONFIRMED | Exact L=3 certificate exceeds 289/500; registered L=5 P3 fails at all tested depths. |
| F6 AX-SEAM | CONFIRMED identity/interior scaling; REFUTED norm-test interpretation; NOT-VERIFIED full norm match | Exact interior formula and corrected powers survive; unnormalized script growth is insufficient. Top-only constant-field witness supplies an obstruction once the cited N_res definition is matched. |
| F7 HC analytic estimates | NOT-VERIFIED; conditional power counts CONFIRMED | DET/HB kernel and reconstruction estimates, completion norms and all-order background bookkeeping remain. Weighted result stays OPEN. |
| F8 gates | CONFIRMED finite outcomes; NOT-VERIFIED analytic upgrades | All gates were classified by what they can decide; no favorable algebraic gate certifies uniformity. |
| F9 R2-glob♯ | CONFIRMED conditional reduction; NOT-VERIFIED realized R2 | Thirteen rows account for the input layers, with named residual gaps. No constructive YM conclusion. |
| F10 general-L distance | REFUTED beyond L=3 | `dρ` → `d(L−1)ρ/2`; at d=4,L=5, 4ρ → 8ρ. L=3 assembly unaffected. |

**Most dangerous unverified item:** row 12's all-order **(HD)** estimate in the actual sharp/source norms and background chart. Its previous BCH derivation was refuted, and this file explicitly postpones replacement by the true linearization. RED′ transports this estimate if supplied; HC-1 and the four scripts cannot establish it. Until it is rebuilt with the correct covariant/chart bookkeeping, general-background R2 cannot be banked.

**Scope and execution record.** Read the explicitly directed science workflow, the review-loop skill (additional file 1), ALIGN55 in bounded ranges, the named prior BGT sources in selected ranges, the four named check families/criteria and selected outputs, and COFUN_CC (additional file 2) for the exact slot norms. PROOF was searched only for residual-norm locating strings; no full read or status propagation. Dimock §3.5 was checked at its primary arXiv page. No snapshot or audit ledger was read. No git command, subagent, heavy numerical library, long worker, or write outside this deliverable was used. All executed mathematical calculations used integers/Fractions. The original subdivision script's cosmetic float formatting was not executed.

Final review checkpoint UTC: 2026-10-29 04:45:54 UTC.

## Exactly what may be banked

1. **RED′ as a conditional algebraic reduction**, with the corrected source identity, the final direct invertibility condition `C_𝒞C_ACη<1`, and the displayed t_+, t_*, δ_Υ. S_E genuinely resolves the quotient-representative issue as a reference, assuming its stated reference bound.
2. **DW, LC and the exact NEC lower bound on every slot representation.** The resulting S_E/any-x_0-only obstruction holds on a fixed family of admissible backgrounds with a nonzero non-root sampled twisted charge. Its leading exponent is **`(2+θ)k−6−θ`**. Do not bank the derivative-only example or convert a merely nonzero k-dependent charge into fixed-size growth.
3. **HC-1's algebra**, including exact left inverse, nested restriction, hierarchical source support and transpose. These are distinct from (P1′)/(P2-tw).
4. **The exact L=3 subdivision certificate and the honest L=5 noncertificate at n≤5**; the corrected axial seam identity and the explicit all-k interior value `−(3^(k−4)−3^(−k))/4`. Bank the top-only-field obstruction conditionally on the specified residual-Hölder norm match; do not bank X3′ as a norm test or an unrestricted cell-boundary lower bound. Dimock's Landau-versus-axial comparison is correct within its abelian source scope.
5. **R2-glob♯ as the repaired implication from its full uniform inputs**, with `C′_b=t_+t_*C_♯/(1−C_♯δ_Υ)`. **Do not bank actual uniform Λ_HC regularity/completion, the all-order background estimates, weighted transfer, L≠3 generalization, or a constructive four-dimensional Yang–Mills theorem.**

lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T15:40Z

First failing step: none.

# um-gate: check of library/um.md (CA-I 4.2:lem-unmarked, step (*))

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, 2026-11-06. Repository pinned at `a999a972a`. The note checked is `library/um.md` at that commit (Codex, 2026-11-05). CA-I, CA-II, CA-III and `YM4_sketch_500.tex` were fetched at `31a47c543775`. Balaban CMP 109, 119 and 99b were read in `~/ym4d-papers`, from rendered pages where formulas matter (CMP 109 pp. 272, 281-282, 290-291; CMP 119 pp. 274-275). This is one line-by-line check, not an audit. It grants no status. No numerics were run.

Moves: CA-I `4.2:lem-unmarked` (L4031). Its status in their text is "stated; proof incomplete at (*)" (CA-I 4031-4032 and 4072, marker at 4084; status list 166617; CA-III 111368). It supplies the ceiling ε₁ᴵ ≤ c₀/(2C_rem) and the per-step bounds of `4.19:lem-flow-bounds`, which `4.19:prop-clause-zero` (clause (0), the coupling flow) reads at every level.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account and the statement checked here. Tadeusz Balaban for the estimates it cites. Codex wrote um.md.

## 0. Does their own text complete (*) later?

No. All three CA parts and the outline were searched.

- The label `4.2:lem-unmarked` occurs in CA-I only at 3603, 4019, 4022-4023, 4032, 56372, 56429, 56467, 163165 and 166617. After the statement, each occurrence is a use or a status line. CA-III 111368 is a status line. CA-II has no occurrence. This matches um.md §1.
- `C_{\mathrm{rem}}` occurs in CA-I only at the statement and its uses. CA-II 11543-11574 has a different `C_rem`, a remnant constant in (F_rem).
- β^𝔄 occurs in CA-I only at the definition (3837), the lemma and its uses (4024-4119), the split β = β^𝔄 + β^ℜ (32438-32461) and the flow lemma (56343-56398). The proposition at 32425-32470 bounds only the marked part β^ℜ, by a Cauchy estimate at running radii.
- The existence lemma `4.38:prf-polarisation-limit` (CA-I 58732-58988) allows C_h = C_h(j) (58780, 58846) and a radius a^♮ that depends on j. It does not give a uniform constant. This matches um.md §1.
- SA 20649-20704 states requirements (RF19)-(RF20). It proves nothing about this coefficient.

So this label is not stale, unlike those completed in ui.md and oc.md. A completion has value.

## 1. Steps checked

| um.md | Step | Source read | Result |
|---|---|---|---|
| §1 | Label census, existence-lemma constant, (2.41) transcriptions | CA-I, CA-II 70-100 and 3290-3310, 3438-3460 | Correct. CA-II 83-89 gives O(1)C₃ε₁; CA-II 3445-3456 adds α₆⁻¹. |
| §2 (1)-(3) | Four hypotheses; bound (3) on U^c | CA-I 4040-4058, 4136-4180; CMP 109 (1.11)-(1.19) | Correct. Theorem 4.3 gives (1.18) on the one-power class with the same constants, and (2.41) with factor ε₁ᴵ for the part other than the Gaussian part. |
| §2 (4)-(5) | Response bound in the four norms, uniform in l | CMP 109 pp. 281-282, 290 | Correct as cited. p. 282: the (4.4)-norm of the derivatives of H_j(□₀,·) is at most B₃∏\|B_i\|, with the factor exp(-δ₀ dist(X, supp B_i)). The free-boundary passage is sketched (F2). |
| §2 | Normalisation: no ξ⁻¹ loss | CMP 109 (3.13)-(3.14), (4.2)-(4.4) | Correct. (4.4) is Balaban's own norm for E^{(j)}(X, exp iξA) at U = 1, J = 0. |
| §3 (6)-(7) | Extension Ξ_l; F(1,A) quadratic, mesh-free | CMP 109 p. 272; CA-I 14083-14132 | Correct. At U = 1 the curvature factors vanish, so (4.5:eq-curvature-remainder-2) gives \|F(1,A)\| ≤ C_F N(A)² for N(A) ≤ 1. |
| §3 (8)-(10) | Ξ_l(A) in U^{Σ¹}_l(X; α₀, α₁) for N(A) < a | CA-I 16019-16151, 16216-16223, 32940-33135, 33839-33985; oc.md §4.1 | Correct. Clauses (i)-(iii) hold directly. C₁₄a < α₀ follows from C_IV ≥ 4C₁₄ (CA-I 16041) and a < α₀/(2C_IV). At each label (p, Z) the substitution (M/L, LB, μ-scaled radii, μA\|_Z) is the account's far-case substitution (4.8:eq-far-case-1) at background 1. The floors δ₀M ≥ 32L and M ≥ 2LR₁M₁ are standing floors (CA-I 11904, 31625, 34774). |
| §4 (11)-(12) | Identification with Definition 4.2, both slots | CMP 109 p. 272; CA-I 58733-58780, 58823-58855 | Correct. I re-derived it. Df(1,0) = 0 slot by slot, because an Ad-invariant linear form on sl_N vanishes. The Hessian kills (Dω, 0). RD*H = 0 gives (Δ - P₁)H = D*DH. So DΞ_l(0)H δ_x = h_∞ δ_x, and the D²Ξ_l term drops. |
| §4 (13)-(14) | Mixed Cauchy estimate | — | Correct. Radii a/(4q_x) and a/(4q_y) give N < a/2. The constant is 16C_H²a⁻²S. Every read and every label of the term lies in X. |
| §5 (15) | Auxiliary pointing | CA-I 60641-60662; CMP 119 pp. 274-275, 278 | Correct. See F1 and F3 for citations. |
| §5 (16)-(23) | Rooted sum and second moment | CA-I 3740-3761, 58877-58897 | Correct. I re-derived (18), (19), (20), (22) and the shell-sum bound n^m e^{-ρn} ≤ m!(2/ρ)^m e^{-ρn/2}. |
| §6 (24)-(26) | Constants and their order | CA-I 1468-1650; CA-II 3296-3306 | Correct. Stage 7 fixes α₁, α₀, α₂ (1614), then E₀ and α₄ (1630), then C_β, then ε₀ᴵ and ε₁ᴵ. C₃ = 4(L+2)⁴O(1)E₀C₁α₄⁻¹α₆⁻¹M^q̄ e^{C₂κ₁} as quoted. C_rem = C_ext A_R comes before ε₁ᴵ, and C_β = C_ext E₀ comes before γ. |
| §6 | Consumers | CA-I 4015-4030, 56342-56398, 56419-56481 | Correct. The flow lemma reads \|β^𝔄 - β⁰\| ≤ c₀/2 and \|β^𝔄\| ≤ C_β. The hypotheses use only g₀, …, g_{l-1}. |

## 2. Findings

None is fatal. Each one is a missing citation or a loose phrase, with the repair named.

**F1. um.md 402-413 (§5): the common lifts of the unpointed family are asserted without a source. Repairable.** The identification takes the torus limit on the unpointed side. It needs the non-wrapping unpointed terms to be independent of the torus ("The non-wrapping terms have the common lifts", line 413). This matters only if (1.18) and (2.41) are read as unpointed bounds. um.md cites nothing for this. CMP 119 p. 278 states it for the pointed terms only. The account supplies it. Its family clauses (CA-I 60641-60657) include a volume-consistency clause for the unpointed terms E_s(X,·), and the pointed terms sum over z ∈ X to E_s(X,·) (60660). `4.38:cor-volume-families` (60672-60718, unpointed series at 60709) carries this through the step, with CMP 116 (2.13) as the unpointed series. **Repair:** cite these lines. With "pointed terms sum to unpointed", the whole-lattice identity is Fubini at fixed l. The existence lemma's fixed-l bounds give absolute convergence, so the torus detour can go. Also, line 410 says "an early constant". Unless a torus form of (5) is cited, read it as "a constant free of ς; it may depend on l". That is enough for convergence to zero, as um.md itself says (lines 416-417).

**F2. um.md 194-204 (end of §2): the free-boundary passage of (5) for the P₁ member is sketched. Repairable.** CMP 109 p. 282 bounds P₁(□₀)H_j(□₀)B on X. It does not bound the kernel of P₁. The p. 290 sentence controls H_j(□₀) - H_j only "in a bound of the corresponding expression". To remove the truncation, the sketch needs exponential decay of the kernels of P₁(□₀) and P₁ (that is, of R = 1 - P of CMP 99b (3.25)), uniform in the domain. um.md calls this "the exponential majorant of the cited operator estimates" (line 201) but does not cite it. **Repair:** cite the walk expansions of CMP 99b Theorems 3.10 and 3.12. The account's own (*) sketch cites the same input for the same uniform bound (CA-I 4100-4111). This is an inherited Balaban input of the kind the note already retains. It is not a new hypothesis.

**F3. um.md 419-422 (§5): "This also follows from the original pointing identity CMP 119 (3.38)-(3.42)" is loose. No effect.** CMP 119 (3.40)-(3.42) applies a partition of unity h_z to the bond-indexed total before localisation. The localised pointed terms appear only at (3.47), p. 278. So the identity concerns totals. That is consistent with um.md's torus argument, but it gives no termwise pointing. **Repair:** cite CA-I 60660 (see F1) instead.

**F4. um.md §3 (lines 206-298): a shorter citation exists. Simplification, not a defect.** §3 proves at U = 1 what the account's far-case proposition `4.8:prop-far-case` (CA-I 33839-33886, part (b) at 33879) states for any half-radius Σ¹ representative. Part (b) says that (e^{iξA}**U**, **J**′) lies in U^{Σ¹}_j(X; α₀, α₁) for every **J**′ with \|**J**′\| < α₀. Take **U** = 1, take α₂ → a (allowed, since a < α₂), and take **J**′ = (Δ - P₁)A + F(1,A) with \|**J**′\| < 2a + C_F a². Then §3 reduces to one citation. That proposition rests on the same increment lemma that ui.md completed and ui-gate checked.

## 3. Verdict

**um.md, completion of CA-I 4.2:lem-unmarked at (*): ADVANCE.** This is a proof of a step their text leaves incomplete.

Under exactly the lemma's four hypotheses, and on the account's inherited analytic inputs, the note proves that for every l ≥ 1,

  |β_l^𝔄 - β_l⁰| ≤ C_rem ε₁ᴵ and |β_l^𝔄| ≤ C_β,

with C_rem = C_ext A_R fixed before ε₁ᴵ and C_β = C_ext E₀ fixed before γ. The proof works in Balaban's scaled norms. There, the response bound (5) and the analyticity ball of Ξ_l are both free of l, and the existence lemma's C_h(j)/a_j does not enter. This is exactly the cancellation that their (*) sketch asserts (CA-I 4100-4111).

The result is still an implication. It rests on these inherited inputs, none reopened here:

- (2.41) of CMP 116, as hypothesis 4. CMP 116 was not read, and is not in `~/ym4d-papers`.
- Balaban's B₃ bound, CMP 109 p. 282. It rests on the tree expansions of CMP 102 Section G.
- The walk expansions of CMP 99b, including (3.132), printed without proof (CA-I 13142-13173).
- The increment lemma as completed in ui.md, with its retained CMP 102 (189)-(190) and CMP 98 averaging inputs.
- The account's family clauses (volume-consistency, pointing).

F1-F3 are citation repairs. F4 is optional.

For the lead: the label is not stale (§0), so this is a real completion of their open step. Under How we work item 6, this check is check (1) of five: one model, line by line, first failing step none. Checks (2)-(5) have not been done.

Checked line by line by Claude (Mini worker).

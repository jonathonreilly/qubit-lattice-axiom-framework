## **Searches run.**

Read `ref/README.md` first. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`, including drafts, referee reports and `LIT_*.md`.

Initial terms: `least.change`, `maximum.entropy`, `Margenau`, `conditional independence`, `half.filled sea`, `sea.*transport`, `pure.hop`, `determinantal`. Follow-ups: `CONSOLIDATED`, `LW1-U_sea`, `LW1-U_hop`, `antiunitary`, `diagonal coupling`, symmetric half-ticks, equal odds, and source identifiers for #9876, #9893 and #10018.

Path abbreviations below:

- `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- `RB` = `ref/pr10124/docs/RECORDS_BORN_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `VC` = `ref/pr10127/docs/VACUUM_COSMOLOGY_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.
- `DP` = `ref/main/docs/RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md`.
- `DL` = `ref/main/docs/audit/data/ledger/re/record_statistics_of_the_half_filled_sea_are_determinantal_conditional_bounded_theorem_note_2026-09-03.json`.

The brief is at workspace-root `briefs/usea.txt`, not inside `T/`. Its target is “the support-respecting transport with fewest changes and then greatest specific entropy is unique.” — `briefs/usea.txt:2`.

## **Already in the repo.**

- **Finite supported transport and entropy selection.** #9893 supplies the same two-stage selection on finite Margolus models. Hall’s inequality establishes feasibility; entropy selects one plan. Scope: “exact finite results and numerical diagnostics in supplied models.” #9902 independently rederives feasibility, strict-concavity uniqueness and product separability. — `RB:63`, “max-flow/min-cut then gives a plan”; `RB:71`, “exact finite results”; `RB:75`, “uniqueness of the greatest-entropy plan by strict concavity.” These are author statements: `RB:11`, “Independent audit lane only.”

- **The freezing mechanism predates this lane.** #9876 states that a site-diagonal antiunitary reversing both half-ticks gives equal occupation laws and no least-change motion. Its 1D argument already uses symmetric half-step matrices and transposition. — `VC:56`, “the Floquet sea has the same odds at both half-ticks”; `VC:58`, “the pair unitaries are symmetric.” Scope includes a supplied 1D walk and a checked `8³` 3D torus, not this lane’s full infinite-volume parameter window. — `VC:39`, “checked on a 12-site 1D pair walk … and … an 8^3 torus.”

- **#10018 repeats the equal-odds identity selection.** It explicitly states uniqueness and zero record-on-change counts. — `VC:1236`, “the identity, and it is unique.” The consolidation limits this to the checked ticks without copy mass. — `VC:1337`, “holds for the ticks that #9876 and #10018 check, which do not include a copy mass.” Both sources are consolidation-kept inputs, not independently audited conclusions. — `VC:33`, “#9876 … kept results rely on”; `VC:11`, “These are author statements for review.”

- **Determinantal occupation laws already have exact finite instances.** The earlier supplied cube/block calculations establish determinant probabilities, inclusion marginals and normalization. — `DP:133`, “every … marginal … equals `det P_T`”; `DP:136`, “The sum … is exactly `1`.” Scope is expressly finite and conditional. — `DP:4`, “Conditional finite Slater/Born and encoded-readout mathematics.” Ledger: `DL:17`, `"claim_type": "bounded_theorem"`; `DL:29`, `"effective_status": "unaudited"`.

- **LW1 already supplies the lane’s existence and sea inputs.** Finite supported couplings exist; finite selection is unique; infinite invariant optimizers exist. — `T/LW1.md:259`, “is nonempty”; `T/LW1.md:272`, “exactly one least-change, greatest-entropy coupling”; `T/LW1.md:458`, “a nonempty compact convex set.” The free sea is already pure, stationary and symmetric, with positive-mass exponential decay. — `T/LW1.md:328`, “pure, stationary”; `T/LW1.md:329`, “exponentially” through the displayed exponential bound. Status: `T/LW1.md:5`, “FROZEN,” but “The LW1 target is not established.”

- **The earlier uniqueness draft contains useful positive cases.** Equal Born laws select the diagonal when the active cosine is nonzero. Active-cube product states have unique product transports, including their matching torus clause. Conditional cube-local laws also give uniqueness. — `T/LW1U_DRAFT.md:71`, “the single diagonal coupling”; `T/LW1U_DRAFT.md:83`, “including its torus clause”; `T/LW1U_DRAFT.md:308`, “Under (CL) … exactly one element.” The atomic boundary sea is covered separately. — `T/LW1U_DRAFT.md:322`, “At the boundary point `mu = 2 eps`.” Status remains pass 1: `T/LW1U_DRAFT.md:3`, “Not yet refereed.”

- **The general invariant-state claim already failed outside factor states.** The earlier counterexample gives an ergodic non-factor state with an entire segment of optimizers. It expressly excludes the vacuum from its conclusion. — `T/LW1U_DRAFT.md:28`, “ergodic (but not factor)”; `T/LW1U_DRAFT.md:32`, “What it does not touch. The vacuum.” The owner subsequently restricted the selection claim to factor states. — `T/TOE_ASSEMBLY.md:197`, “PS-3 selects one transport at factor states only.”

- **No-record formation is an independent prior result.** Free-sea records already fail to form under PS-3c, without needing transport uniqueness. — `T/LW1.md:295`, “starting from the free sea, no record forms.”

- **A moving-sea comparator exists on another supplied law.** The copy-massed patch calculation finds a particle-hole shuttle. Its status is logged and finite. — `VC:1408`, “logged”; “forced configuration motion is a period-2 particle-hole shuttle.” The consolidation explicitly separates this from the no-copy-mass freezing results. — `VC:1337`, “For the copy-massed tick the patch computation … finds motion.”

## **Failed attempts on file.**

- **Proportional shortfall switching.** It fails the required Born marginal on one Margolus block. — `RB:63`, “the worst inflow error is 0.317.”

- **Finite entropy strictness at infinite volume.** The distinguishing mixture entropy disappears per cell. — `T/LW1.md:480`, “specific entropy is affine.”

- **Torus-limit selection.** The missing step is a recovery sequence preserving exact marginals and supports while approaching both optima. — `T/LW1.md:481`, “no recovery sequence has been constructed.”

- **Local Gibbs duality.** Neither the required potential representation nor a uniform uniqueness estimate is supplied. — `T/LW1.md:482`, “no supplied summable-potential representation”; “no uniform Dobrushin-type uniqueness bound.”

- **Bernoulli/Ornstein reduction.** An isomorphism does not preserve the occupation-coordinate optimization problem. Unconstrained approximating couplings also violate cube-number support. — `T/LW1U_DRAFT.md:298`, “It does not carry the cost or the support”; `T/LW1U_DRAFT.md:300`, “they leave `S`.”

- **Number-conditioned finite-cube reduction.** The earlier draft reports numerical failure of (CL), rather than a general proof. — `T/LW1U_DRAFT.md:328`, “shown by computation, which may refute but does not prove.” The present lane supplies parameter-dependent failures, but its finer test excludes independence **together with** locality of the conditional laws. It does not establish conditional dependence alone. — `T/LW1U_SEA.md:90`, “the local-law condition … could fail separately.”

- **Symmetry and hidden-label counterexamples.** Averaging gives a symmetric optimizer, not two optimizers. Independent label randomization returns a product state; Markov labels remain unsettled; no determinantal rigidity mechanism is supplied. — `T/LW1U_DRAFT.md:332`, “contains a `g`-invariant element”; `T/LW1U_DRAFT.md:339`, “the optimum … absorbs it”; `T/LW1U_DRAFT.md:340`, “neither a proof nor a counterexample”; `T/LW1U_DRAFT.md:341`, “No mechanism is known.”

- **Margenau–Hill coupling on the hop segment.** Marginals and support hold, but positivity fails. — `T/LW1U_SEA.md:92`, “assigns `−1/648` to a supported pair.”

- **Continuation from the product point.** Uniqueness at the boundary supplies no uniform control inside the segment. — `T/LW1U_SEA.md:107`, “no uniform entropy deficit or contraction is established.”

## **Overlap with this lane’s results.**

The lane ran and froze. Its status is “FROZEN 2026-11-05 after pass 3”; hop-segment uniqueness remains open. — `T/LW1U_SEA.md:3`, `T/LW1U_SEA.md:5`, “uniqueness remains open.” Classifications below compare with earlier work, excluding the lane’s own pass-1 draft.

- **Theorem 1 — EXTENDS earlier finite determinant identities.** The occupation-minor identity overlaps `DP:133`, “equals `det P_T`.” The lane states it for general quasi-free covariance and adds Fock-lift transition determinants and covariance evolution. — `T/LW1U_SEA.md:23`, “A layer sends `G` to `WGW*`.”

- **Theorems 2 and 4 — EXTEND #9876/#10018.** The mechanism is already present: `VC:56`, “same odds at both half-ticks.” The lane adds the infinite-volume window, massless case, and precise exceptional segment. — `T/LW1U_SEA.md:27`, “also at `μ=0` … in infinite volume”; `T/LW1U_SEA.md:39`, “unless `2ε+μ=π`.” The full lane result is therefore not a duplicate of the earlier finite checks.

- **Theorem 3 — DUPLICATES Lemma 3.2 in its nonzero-cosine clause.** Prior: `T/LW1U_DRAFT.md:71`, “Assume `cos alpha != 0`.” Lane: `T/LW1U_SEA.md:35`, “`cos θ≠0` … diagonal singleton.” Its unsupported one-particle diagonal at zero cosine is an additional explicit boundary clause. — same line, “is unsupported.”

- **Theorem 5 — NEW torus-sea convergence statement in the searched work.** The earlier torus theorem concerns active-cube product states. — `T/LW1U_DRAFT.md:83`, “products over the active cubes.” The lane instead treats the specified periodic seas. — `T/LW1U_SEA.md:43`, “Its diagonal coupling converges locally.”

- **Theorems 6 and 9 — EXTEND the earlier numerical (CL) tests.** Prior: `T/LW1U_DRAFT.md:328`, “shown by computation.” Lane: `T/LW1U_SEA.md:51`, “fails on an open dense subset”; `T/LW1U_SEA.md:82`, “all but isolated points.” The stronger pass-1 conditional-dependence claim is explicitly dropped. — `T/LW1U_SEA.md:90`, “not used and is dropped.”

- **Theorem 7 — NEW segment support criterion and positive-cost bound.** It requires swapped parity-class counts and nonzero block determinants. — `T/LW1U_SEA.md:62`, “supported exactly when”; “at least `2ν_P(N_D odd)>0`.” This identifies the support exception to the older blanket identity wording, `VC:1236`, “transport between equal odds is the identity.” The consolidation limits the earlier result to its checked ticks. — `VC:1337`, “ticks … check.”

- **Theorem 8 — EXTENDS the earlier symmetry-averaging result.** Generic symmetric-optimizer existence was already stated. — `T/LW1U_DRAFT.md:332`, “contains a `g`-invariant element.” The exact segment identities and cube-local involution are new here. — `T/LW1U_SEA.md:72`, “`ZPZ=I−P`, `\bar P=YPY`.”

- **Theorem 10 — NEW exact positivity obstruction.** The signed candidate fails at a displayed supported pair and nearby parameters. — `T/LW1U_SEA.md:92`, “remains negative … for all sufficiently small `a>0`.”

- **Theorem 11 — DUPLICATES the product-optimizer construction of Theorem 3.4 at this boundary state; adds its non-diagonal character.** Prior: `T/LW1U_DRAFT.md:83`, “single coupling `pi* = ⊗_k lambda*`.” Lane: `T/LW1U_SEA.md:103`, “the product … one-cube coupling”; “It is not diagonal.”

- **Theorem 12 — EXTENDS the one-mode result to five-mode number/parity configurations.** Earlier five-mode work still listed these transport questions as open. — `T/LW1_5.md:299`, “remain open for the new alphabets.” The lane proves diagonal selection off the segment and forced motion on it, conditional on PS-3h5. — `T/LW1U_SEA.md:111`, “For either actual configuration.”

- **Theorem 13 — EXTENDS the freezing identity to a finite dressed setting.** Its additional scope is conditional on absent electric evolution and a specified density-matrix class. — `T/LW1U_SEA.md:117`, “If the electric layer is absent (`τ_E=0`)”; “a real function of `U_0`.” It does not identify VC1’s vacuum. — `T/LW1U_SEA.md:119`, “No identification … is made.”

## **Missed inputs.**

- **#9876 and #10018 should anchor attribution of the freezing mechanism.** They already combine half-step transposition/antiunitary symmetry, equal occupation laws and identity selection. — `VC:58`, “the pair unitaries are symmetric”; `VC:1236`, “the identity, and it is unique.” Using them changes the novelty description to an infinite-volume extension with a precise support exception. The lane’s source-context list instead names LW1 and the preceding uniqueness draft. — `T/LW1U_SEA.md:9`, “Context: `LW1.md` … `LW1U_DRAFT.md`.”

- **The consolidation’s copy-mass correction should accompany downstream use.** It prevents extending free-sea freezing to altered or gauged laws without another argument. — `VC:1337`, “do not include a copy mass”; “patch computation … finds motion.” This reinforces the lane’s own limit: `T/LW1U_SEA.md:125`, “no result for gauged vacua or other states.”

- **The exact finite DPP source supplies prior attribution for the determinant toolkit.** It changes the claimed provenance of that toolkit, without supplying sea-transport uniqueness. — `DP:133`, “every … marginal … equals `det P_T`”; `DP:4`, “No physical law, vacuum selection … is derived.” Its ledger remains unaudited. — `DL:29`, `"effective_status": "unaudited"`.

## **Consumers.**

- **LW1 consistency/selection.** The free-sea specialization needs only a singleton at its two half-tick states. It does not need the full factor-state theorem or its general torus clause. — `T/LW1U_DRAFT.md:349`, “names one state … and it drops the torus clause.” The remaining free-sea obligation is uniqueness on the hop segment. — `T/LW1U_SEA.md:76`, “Does `O_1` have exactly one element?”

- **LW1-5.** The weakest useful statement is supported diagonal uniqueness for site numbers on `L5-U` and site parities on `L5-O`, off the segment. Full flavour-resolved transport uniqueness is unnecessary for that conclusion. — `briefs/usea.txt:2`, “site numbers … or … site parities”; `T/LW1U_SEA.md:111`, “For either actual configuration … diagonal singleton.” Segment uniqueness remains open. — `T/LW1U_SEA.md:123`, “number and parity versions are also open.”

- **TM1.** Its formation question already consumes the weaker no-record result B8a. Constant actual histories sharpen the free-sea obstruction but do not resolve formation for the selected gauged vacuum. — `T/TM1.md:60`, “LW1 B8a … give the free-sea result”; `T/TM1.md:62`, “It does not establish the gauged vacuum.”

- **VC1.** For free-sea freezing, constant histories suffice. For the dressed identity, VC1 additionally needs to identify its vacuum with the specified functional-calculus density matrix under the finite, `τ_E=0` hypotheses. — `T/LW1U_SEA_REFEREE.md:336`, “Whether VC1’s vacuum is such a function stays VC1’s question.”

- **Record-count cosmology.** Zero occupation changes suffice for the earlier record-on-change obstruction; entropy uniqueness beyond zero-cost selection is unnecessary. — `VC:1236`, “Under record-on-change … the count is 0 and its variance is 0.” This consumer uses that earlier formation rule, while LW1’s rule separately gives no formation. — `T/LW1.md:295`, “under … PS-3c … no record forms.”

- **Direct YM-branch consumers:** none found in the repository searches above.
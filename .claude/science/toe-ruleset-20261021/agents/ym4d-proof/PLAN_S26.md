# PLAN_S26 — the lead's own review of the approach, and the next attack

Author: the lead, written 2026-10-28T22:19:59Z, by reading primary sources (PROOF.md §0/§L8-L9, HANDOFF.md, REVIEW_S22.md's BFT statement, EXISTENCE.md §0) — not worker summaries. Requested by the owner: a review of the approach and a plan for the next attack. This file states judgements; it proves nothing, and it changes no status in PROOF.md.

**Standing caveat.** A re-review of sessions 24-25 (SESSION25_RESULTS.md §SWEEP55) was running when this was written;
nothing below assumes any session-24/25 result survives it, except where noted as cross-family confirmed.

---

## 1. The first problem is the target, not any lemma

**What the lane is proving.** PROOF.md §0: *"T_OS (the owner's target). There is a state on an E(4)-covariant
algebra of gauge-invariant observables on R^4 … satisfies OS0-OS3 … not a free theory."* No mass gap.
(For the record: the Clay problem needs the mass gap too, so neither this target nor — by the lane's own
inference at PROOF.md "What the OpenAI claim must have done" — the OpenAI claim is the Clay problem.)

**What the lane already knows and has stopped looking at.** PROOF.md §0 item 3 and §L8-L9, written in
sessions 1-3: *"Euclidean invariance is the hard core. On T^4 it is false … On R^4 it cannot be obtained by
averaging over rotations … It needs either universality (… E7-type estimates) or a second, rotation-covariant
observable family."* And: the infrared growth of the coupling *"obstructs uniqueness … and, through (1), the
universality route to rotation invariance … so it may well obstruct existence of the OS theory itself."*
EXISTENCE.md §0 lists rotation invariance (OS1) under *"not delivered … OPEN (IR; need a gap or cluster
expansion)"*.

**HANDOFF.md's critical path does not contain OS1 at all.** All six items are layer-1 internals. So the
previous model spent two sessions on the inside of layer 1 while the item that decides whether T_OS is
reachable — OS1 on R^4 without uniqueness — had no attack and no owner. **Finishing every layer-1 item does
not finish T_OS.** That is the single most important fact in this file.

**Recommendation (OWNER DECISION): make the finishable target explicit.**
- **T_fin^OS (fixed physical torus).** For every physical torus side ℓ: continuum limits of lattice SU(N)
  Yang-Mills along an asymptotically free sequence of bare couplings exist, are consistent across
  resolutions, satisfy the torus OS structure (reflection positivity for block planes, torus translations,
  hypercubic covariance, gauge invariance, OS0 for smeared/flowed local observables), and are non-trivial.
- **R^4 / OS1 becomes a separately labelled open problem**, attacked only if someone has an idea for
  rotation invariance without uniqueness. No worker time on it by default.
- This is still a theorem nobody has, and it is the version that can actually be finished. The existence
  lane already delivers most of the torus OS structure "for free" by compactness (EXISTENCE §0 (a)-(b));
  its content is consistency, non-triviality and OS0, all of which rest on layer 1.

## 2. The architecture: what is right, and what was never checked

**2a. The composite route is the right shape — it is Balaban's shape.** Balaban's background field
(CMP 102, "The variational problem and background fields…") is the minimiser of the action under the
**k-fold** block constraint, and his propagators (CMP 95/96 "Propagators and renormalization
transformations…", CMP 99 "Propagators … in a background field") are controlled **uniformly in k**. The
lane's BFT (REVIEW_S22) — one contraction for the composite 𝔉_k, background-field clauses 0-5 — is the
soft-scheme analogue of exactly those papers. Keep it.

**2b. But the lane has never read those papers.** PROOF.md's global caveat: *"Every statement attributed to
Balaban below paraphrases the structure of his programme. The exact theorem statements … were not read."*
Only CMP 109 was read directly. **Every remaining paper-scale wall — (GAP-Z), (G♯_0-field), (N-bg)/(H-C),
FLOW's fine background-dependent inverse H_⊥(U)^{-1}, BFT-5 — is a "propagator / background-field bound at
a general background", i.e. the content of CMP 95/96/99/102.** The lane has been reconstructing them blind.
Some of these papers appear to be in open university repositories (UMich Deep Blue; Rutgers' scholarship
repository) — confirm access, keep PDFs local and out of the repo as with CMP 109, pay nothing.
**This is the cheapest high-value step available, and it should have been step one.**

**2c. Decision 4 (soft kernel instead of Balaban's hard constraint) has never been re-priced.** Its benefit
is real and lands in layer 2: an exact Markov chain with positive integrand, clean reflection positivity,
the soft OS structure. Its cost is that **no Balaban estimate transfers verbatim** — every one of the walls
in 2b must be re-proved in a different variational problem with soft penalty terms κ_jΣφ̂_c at each level.
Once Balaban's exact statements are in hand, decide with evidence between: (i) port his background-field
and propagator theorems to the soft scheme; (ii) run layer 1 in his hard scheme, import-and-reverify his
theorems, and bridge to soft variables only where layer 2 needs them. Neither is obviously right; what is
wrong is never having asked.

**2d. Most of sessions 24-25 was spent on bookkeeping that does not bear on truth.** Decade margins against
DX′, the ε_1 ladder, a_RS pricing, the 24-decade q-lever, symbol-rename campaigns. **A proof needs
constants that exist and are uniform in K (and in the coarse side T), and a smallness hierarchy that is
acyclic:** (N, L, κ_±) → all geometric/analytic constants → thresholds (ε_1, ε_0, …) → g_0. g_0 may be taken
as small as needed: it only sets the scale a_0 where the RG stops; on a fixed physical torus that just
fixes how many resolution-0 blocks the box has, and the remaining coarse integral is finite-dimensional.
**Whether g_0 must be below 10⁻⁵⁰ or 10⁻¹⁵⁰ is irrelevant to the theorem.** What matters is only (i) a
genuine cycle in the hierarchy, or (ii) a constant that grows with K or T. Replace every decade ledger with
**one dependency-DAG acyclicity check**. (The cross-family Codex review already showed a_RS is not consumed
by the live route at all — three sessions priced a dead quantity, which is what this kind of bookkeeping
produces.)

**2e. The one constants issue that is real: the level-count factor ≈ 25(k−1).** A linear-in-k loss is a
genuine non-uniformity (category (ii) above). In Balaban's scheme k-uniformity comes from random-walk
expansions with exponential decay, and a linear factor usually means sup-norm or absolute-value summation
over levels — which is also the diagnosis of the lane's per-level failures (CURV-F2: the proven recursion
compounds by Z_colZ_row² ≈ 1.3·10³ per level while the measured contraction is ≈ 0.12). Decisive and cheap:
**what exactly does 25(k−1) multiply, at what field scale, and does a level-dependent small-field threshold
(as Balaban uses, scaling with g_k) or exponential level decay absorb it.**

**2f. A ledger defect to fix on sight.** PROOF.md near its top (string: *"§N5 establishes a marginality
no-go, so CURV-F2 is unrepairable in the per-level form"*) still cites the §N5 no-go that REVIEW_NORMS_S1
withdrew as unestablished (tautological check n1-D, undefined term, vacuous part (i)). Either the ledger
asserts a withdrawn claim, or the withdrawal is wrong — REVIEW_NORMS_S1 is itself under
re-review (batch C4). Settle it there; do not edit PROOF.md on either reading until then.

**2g. The process was the bigger failure than any single estimate.**
- The lead's summaries were a corruption channel: lead-authored lines in PROOF.md/HANDOFF were wrong at
  least a dozen times in two sessions, and the next worker read them first.
- Targets were set from one worker's "smallest missing input" without reading the source; one such
  target turned out to be stale (already decided a session earlier in the same file).
- Same-family review passed things the first cross-family review broke on *form* (status comparisons used
  as proofs of non-identity).

## 3. What survives — deliberately not claimed here

The review sweep decides. The only session-24/25 items with an approved-setting cross-family check so far:
Codex confirmed the core of TUNIF's Theorem TU-3 (with a missing constant 𝔠_0 in its mean-subtraction
step), the convexity behind KN_ADOPT's H1 (with the degeneracy count corrected 633 → 475), that a_RS is not
consumed by the live route, and the refutation of (HESS-rel) (found independently by both families). Each
is still to be re-read in its final form by the sweep.

## 4. The next attack, in order

**Step 0 — owner: the target.** T_fin^OS on the torus (recommended), or keep T_OS on R^4.

**Step 1 — read Balaban (and Dimock) directly. Two workers, Opus 5.5 xhigh+.** Obtain CMP 95, 96, 99, 102
(then 98, 109, 116, 119, 122) legitimately; Dimock's "The renormalization group according to Balaban"
series is on arXiv. Deliverable **BALABAN_EXTRACT.md**: the exact statements — norms, hypotheses, constants,
which quantities are uniform in k — of (a) existence/regularity/analyticity of the k-fold-constrained
background field, (b) the background-field propagator bounds and their random-walk expansions, (c) how the
induction keeps constants from compounding across steps. No PDF or extracted text enters the repo.

**Step 2 — the wall map.** For each open wall — (GAP-Z), (G♯_0-field), (N-bg)/(H-C)'s C_♭ clause, FLOW's
H_⊥(U)^{-1} ((T-a1-M)/(T-b)), (SPD)/(W2), the k-factor — state which Balaban theorem covers it **in his
scheme**, and exactly which step changes in the soft scheme. One table. This replaces HANDOFF's critical
path.

**Step 3 — decision 4, re-priced with Step 2's evidence** (owner decision, with a recommendation).

**Step 4 — the k-factor question (2e). Does not wait for Steps 1-3.** One worker.

**Step 5 — the smallness DAG (2d).** One file, every threshold and constant as a node, every "≤" as an edge,
machine-checked for cycles and for K- or T-dependence. Retires the decade ledgers.

**Step 6 — the core attack: the general-background propagator/background-field bound**, in the scheme
chosen at Step 3, following Balaban's proof architecture. This is the one wall the others reduce to. Two
independent workers on different routes, plus a Codex astra-max checker on every PROVEN before it is banked.

**Step 7 — layer 2 on the torus**, in parallel once Step 6 has a statement to consume: consistency across
resolutions (E8*), non-triviality at the physical scale (the existence lane's (WC)/two-point lower bound plus
non-Gaussianity), OS0 for smeared or gradient-flowed observables.

**Prior art to check before Step 7 [m — from memory, unverified]:** Magnen, Rivasseau, Sénéor, "Construction
of YM4 with an infrared cutoff", Commun. Math. Phys. 155 (1993) — a finite-volume construction by a different
(gauge-fixed, regulator) method. The torus target must say precisely what it adds.

## 5. Rules from here

- Workers: **Claude Opus 5.5 at xhigh or max, model and effort set explicitly**, model ID printed as line
  one of every deliverable and checked; **Codex gpt-6-astra at max**, banner checked.
- **Nothing is banked as PROVEN without a cross-family check.** The lead writes no mathematical claim into
  PROOF.md or HANDOFF that a reviewer has not checked against its source.
- **Read the source before setting a target from someone's summary of it.**
- **Stopped:** decade/margin ledgers, q-tuning, rename campaigns beyond a single canonical symbol table,
  new constants work of any kind until Step 5's DAG says a constant is on a cycle or grows with K or T.
- Ledger entries become short: verdict, file, one sentence, pointer. The worker file is the record.

---

## 6. Owner decision: "Fixed torus" (2026-10-28)

**T_fin^OS is the target.** Precisely: PROOF.md §0's T_fin — on the torus T^4_M (side L^M in resolution-0
units), the lattice measures along a tuned asymptotically free sequence of bare couplings **converge** as
L^{-K} → 0 to a limit state on a gauge-invariant observable algebra, non-trivial, reflection positive, with
the torus symmetries — **plus** consistency across resolutions **plus** OS0-type regularity for a named
class of smeared or gradient-flowed local observables (the class is fixed at Step 7).

**One thing nobody may do silently.** T_fin says *converge* — the whole sequence. Subsequential limits are
free by compactness (EXISTENCE §0 (a)); convergence of the whole sequence needs uniqueness of the
finite-volume limit (the lane's estimate E7). If only subsequential limits turn out to be reachable, that is
a weaker theorem, **T_fin^sub**, and it must be labelled as such — not quietly substituted.

**What this changes, immediately.**
- R^4 / OS1: labelled OPEN, no default worker time.
- Volume-uniformity is still needed: inside one RG run on a fixed physical torus the intermediate coarse
  sides are L^{M+K-k}, unbounded as K → ∞. So T-uniformity work (TUNIF) stays relevant, pending its review.
- Infinite-volume items (EXISTENCE §0 (d), L8d) leave the critical path.
- Steps 1, 4 and 5 start as reviewer slots free; targets pre-stated in RTARGET §55.

---

## 7. CORRECTION to §6 — the owner's guidance is the FULL proof

**§6 is withdrawn.** The owner, verbatim: *"sorry i choose fixed torus only because you seem to think thats
the best direction here, obtain consensus. my guidence here is for you to get the full proof!"*

So: **the target is T_OS on R^4** (OS0-OS3, non-trivial, no mass gap claimed). The lead's §1 recommendation
to scale down was the lead's opinion, offered as a decision; it is withdrawn as a decision and goes to the
consensus panel as one view among several.

**What stays true regardless of route.** Every route to T_OS passes through layer 1 (uniform UV control) and
through finite-volume limits, so **T_fin is milestone 1**, and Steps 1, 4 and 5 of §4 are needed on every
route. Nothing about them changes.

**What changes.** OS1 on R^4 — E(4) invariance of an infinite-volume limit, which the lane recorded in
sessions 1-3 as needing uniqueness (IR control comparable to a mass gap) — **goes onto the critical path
now, with its own attack**, instead of being parked. The lead's claim that it is out of reach is exactly the
kind of claim this lane has repeatedly got wrong; it gets the same scrutiny as any no-go.

**The consensus panel (launched now).** Independent panellists from both model families, each given the
primary sources and the question, and asked to form a view **before** reading this file:
- **P1** — what T_OS actually requires, split UV vs IR; is "OS1 needs uniqueness" right; rank the routes.
- **P2** — adversarial: construct a route to OS1 in infinite volume **without** uniqueness or a gap.
- **P3** — audit the lane's infrared-obstruction analysis against the literature and against the lane's own
  inference about what the OpenAI claim did.
- **P4, P5** — Opus 5.5 panellists on the same questions, as Claude reviewer slots free, for cross-family
  agreement.
The lead synthesises; where the panel disagrees, the disagreement is recorded, not resolved by the lead's
preference.

---

## 8. Role split (owner, 2026-10-28): Opus 5.5 does the work, Codex reviews it

Owner: *"opus 5.5 is smarter than codex. assign work accordingly (maybe review with codex, work with opus?)"*
- **All derivation, proof attempts, route construction and synthesis: Claude Opus 5.5 at max effort.**
- **All checking: Codex gpt-6-astra at max**, as the cross-family reviewer of each Opus result before it is
  banked.
- In-flight exceptions, left to finish because stopping them would waste most of their work: the Opus 5.5
  re-review sweep (C1-C5, C7, C8), and the Codex panellists (their role in the consensus is now a second,
  critical opinion; the Opus panellists P4/P5 are the primary analysis). The completed Codex Step-4 analysis
  (KFACTOR55.md) is kept as a review input; Step 4 itself is re-run by Opus 5.5, independently first.

---

## 9. Consensus so far (Codex panellists P1, P3; Opus P4 running, P5 queued) — the lead's §1 was wrong

**Two independent panellists agree, and both disagree with the lead.**
- **OS1 does not logically require uniqueness** of the infinite-volume state. P1 PROVES it: a two-phase
  mixture satisfies OS0-OS3 and fails clustering. P3 adds: even a unique cutoff limit with coordinate RP and
  hypercubic symmetry need not be rotation invariant (explicit Gaussian example) — so uniqueness is neither
  necessary nor, alone, sufficient. **The lead's §1 claim that rotations need mass-gap-scale infrared control
  is not established** — it conflated several different uniqueness statements.
- **Route ranked first by both:** keep the Wilson lattice and its reflection positivity; make the UV RG
  volume-uniform with local gauge-invariant sources; take a **diagonal** limit a → 0, R → ∞; prove rotation
  invariance by a **quantified rotation-defect estimate** on the selected state sequence. P1 proves the
  assembly: four inputs (regularity, RP, rotation defect → 0, a calibrated non-freeness witness) give the full
  theorem, with no uniqueness, clustering or gap.
- **The hardest step, named by both:** nonperturbative rotation restoration on a renormalized local
  gauge-invariant algebra, uniform in volume after integrating the unrestricted coarse field. It may still
  need long-distance information — but nothing shows it needs a gap.
- **The torus is a useful milestone, not a necessary one**, and full-sequence torus convergence (T_fin) is
  not needed at all: a diagonal subsequence suffices. Every estimate should carry its volume dependence
  visibly from the start.
- **Non-freeness needs a calibrated local witness.** A nonzero connected 4-point of a composite observable
  proves nothing (Y = X² − 1 of a Gaussian has fourth cumulant 48); nor do tiny-torus Polyakov loops. This
  bears directly on the existence lane's non-triviality items.

**Consequence for §4.** Step R4 is now a concrete Opus 5.5 task — P3's "smallest discriminating artifact":
the rotation-defect identity for one renormalized local observable, proved uniform in volume or reduced to
the first term that needs coarse-law information. It goes first in the Opus queue. The synthesis is final
only after the Opus panellists report; disagreements will be recorded, not resolved by preference.

---

## 10. The consensus panel is complete (P1, P2, P3 Codex; P4 Opus 5.5)

**Unanimous.** (i) The full theorem T_OS on R^4 does **not** require uniqueness of the infinite-volume state
or a mass gap — P1 and P4 give proved counterexamples to the implication, P3 shows uniqueness is not even
sufficient. (ii) OS0, OS2, OS3, translations, the hypercubic group and non-freeness need only local,
volume-uniform ultraviolet bounds plus compactness; **only the non-lattice rotations can need more.**
(iii) The torus is a useful laboratory, not a necessary milestone. (iv) The lane's "two-family" route to OS1
and naive rotation averaging do not work as written (P4 proves averaging fails even for the best Gaussian).

**Split, recorded not resolved.** *Which finite volume.* The three Codex panellists rank first a flat-torus
rotation-defect estimate, whose boundary term P2 itself calls "infrared information". **P4 ranks first a round
4-sphere S^4_R** — reflection positivity across the equator at every cutoff (claimed proved), SO(5) invariance
reduced to **fixed-volume universality** (argued ultraviolet, not proved), R → ∞ by compactness with SO(5)
contracting to E(4). Costs: Balaban-type action bounds replace the torus-only chessboard large-field bounds;
a slowly varying bare coupling and an equatorial seam; and the owner must accept S^4 lattice regularizations
as "arising as such a limit". Under review by Codex (CODEX_REVIEW_P4.md).

**The consensus next target, shared by every route: rotated-lattice universality in bounded regions** — two
lattice regularizations differing by a rotation give the same local continuum correlations at fixed volume.
On the sphere route it is (nearly) sufficient; on the flat route it is necessary with a boundary term on top.
**Launched on Opus 5.5 (UNIV55.md)**, alongside the flat-route rotation-defect test (ROTDEF.md), so both
regulators are tested at once. Related literature found by the panel and verified to exist: T. Gantumur,
*Rotationally invariant dynamical lattice regulators for Euclidean QFT*, arXiv:2512.22072 (RP proved for a
gauge-invariant dynamical-lattice regulator) — a JHEP citation given for it could not be confirmed.

---

## 11. Step 1 is blocked; what it found anyway; one correction to this plan

**Blocked (BAL-F1, all twelve CMP papers).** The worker's fetch tool cannot read PDFs, and the hosts refuse it
(Deep Blue 403 / script page; Project Euclid's bot check, which may not be circumvented; Springer paywall).
**To finish Step 1 the owner must place local copies** (free, legitimately obtained, outside the repository, as
was done for CMP 109). BALABAN_EXTRACT.md §10 has the reading plan to section and equation.

**CORRECTION to §2e and RTARGET T56-4 (the lead's error):** Balaban does **not** absorb level-count factors with
a small-field threshold scaling with g_k. His thresholds are **fixed** (ε_0, ε_1). His mechanism: background
field, propagators and covariances defined once from the full k-step constraint and bounded directly at each k
(constants depend on L and M only), earlier levels re-evaluated at that single background, level remainders
geometric — all conditional on the effective coupling staying ≤ γ at every scale. Step 4 was told mid-run.

**Findings that move the critical path (from secondary sources; strong evidence, not proof):**
- **No readable Balaban paper proves the coupling flow** (CMP 122 II's main theorem is conditional on the
  couplings staying ≤ γ). The flow must be supplied in either scheme. **Launched: FLOW55.md (Opus 5.5) — the
  coupling flow via the trivial background plus Ward identities, Balaban's route, bypassing FLOW's
  H_⊥(U)^{-1} wall.**
- FLOW's fine inverse H_⊥(U)^{-1} is a wall of FLOW's own route, not a background-field wall.
- (N-bg) and (H-C) would come out as derivative bounds from analyticity of the composite background field.
- Choosing the hard scheme would not import CMP 102 for (0.4) as is; CMP 98 would need re-proving first.
- BAL-F2 (does k-uniformity need the hard constraint?) narrows to two items: exact absorption of sources in the
  range of Q_k^T, and the multiplier term matching the soft residual rows.
- 8 PROOF.md paraphrases of Balaban are wrong (BAL-F3), including CMP 99 cited as "CMP 95/96/102b" and an
  unsourced "β_j → 2b₀ ln L attributed to CMP 109".

---

## 12. Correction to §2d (the lead's overstatement), from CODEX_REVIEW_DAG

§2d said decade bookkeeping "does not bear on truth" and SMALLNESS_DAG went on to "retire the decade ledgers".
**That holds for one-sided constraints only.** Codex REFUTES unconditional retirement: **(TC), EXISTENCE's
Compatibility (K), and the complex-width interface are two-sided feasibility windows** — a quantity squeezed from
both sides, where the window must be non-empty and magnitudes therefore decide. (TC) is one, and it fails
(RLARGE_U55.md, running, is repairing it). Rule from here: magnitudes are irrelevant for one-sided bounds on later
choices and **essential for every two-sided window**; the DAG must tag each window and each must be checked
numerically. A cutoff-family edge n_♯ → SC_k was also missing from the graph.

---

## 13. The route to OS1 has a leader: the sphere (evidence, 2026-10-29)

Three results converge (none yet fully cross-checked; Codex reviews running):
- **Flat route needs a genuine infrared input** (TQ55): TQ ⇔ Λ = 0 for the Wilson measure; reflection positivity
  cannot supply it (exact "rotlet" counterexample: a symmetric conserved |x|⁻⁴ stress tensor that satisfies an
  infrared bound yet carries rotation charge). It fails exactly when rotations break spontaneously with gapless
  modes — weaker than a gap, but an infrared problem nothing available excludes.
- **Rotated-lattice universality is ultraviolet at fixed volume** (UNIV55, Proposition T); infrared information
  enters only to remove a number-of-blocks factor, which the sphere at fixed R does not need.
- **On S^4 rotations are exact global symmetries**: the Ward identity along a Killing field has no shell term, and
  SO(5) invariance at every finite R survives R → ∞ **even if rotations break spontaneously in flat space** —
  symmetry is imposed exactly, not selected.
**So the sphere route is the leading route to the full theorem with no infrared input.** Its open items are
ultraviolet: the construction and seam transparency (SPHERE55, running), universality's UV items N1-N5 / W0-W3,
the large-field comparison, and the reflection positivity across the equator (banked). The flat route stays as
the alternative; its single infrared input is now precisely named.

---

## 14. Correction to §13, from CODEX_REVIEW_TQ (2026-10-29)

Two sentences of §13 are stronger than what was checked. **"Reflection positivity cannot supply TQ"** is CONFIRMED only
for generic coordinate RP (which permits arbitrarily slow power-law reflected correlations); that RP *combined with the
Wilson-specific inputs* cannot give TQ is NOT-VERIFIED. **"TQ fails exactly when rotations break spontaneously with
gapless modes"** — the exclusive-Goldstone "iff" — is NOT-VERIFIED. What stands: TQ ⇔ Λ = 0 for the centred Wilson
two-point orbit; the rotlet shows conservation, symmetry and an infrared bound alone do not force TQ (it is not a
Wilson/RP-state counterexample); invariant sphere states need no shell argument, conditional on their construction.
The ranking (sphere route first) is unchanged: it rests on the sphere needing no infrared input, not on these two
sentences.

---

## 15. Corrections to §11, from CODEX_REVIEW_BALX (Codex checked BALABAN_EXTRACT against ten open arXiv expositions)

- **"Balaban's thresholds are fixed (ε_0, ε_1), not g_k-scaled" — REFUTED as a general account** (F2). The expositions
  use coupling-dependent integration cuts (Dimock I §3.2: p_k = (−log λ_k)^p; QED3: p(e_k) = (−log e_k)^p for the
  small/large-field split) alongside fixed deterministic regularity radii (Goswami's σ-model: ε_0, ε_1). Both kinds of
  object exist; §11 conflated them. A fixed CMP 109 background class may exist (not verified). Consequence: the
  coupling-scaled threshold option is not excluded; LARGE55 was told.
- **"No readable Balaban paper proves the coupling flow" — REFUTED as a negative inference** (F8). A theorem conditional
  on g_k ≤ γ is compatible with a separate theorem arranging that hypothesis (the QED3 papers do exactly that for their
  non-marginal parameters). What stands: **no verified 4D marginal-flow theorem is imported from the checked corpus**, so
  the flow must still be supplied here (FLOW55 → (UIR^♮), UIR55 running). The plan does not change; the sentence does.
- Of BALABAN_EXTRACT's eight refuted PROOF.md paraphrases (§11, "BAL-F3"), Codex supports 2 narrowly, rejects 2 and
  leaves 4 NOT-VERIFIED (F10). Do not cite "8 paraphrases are wrong".
- **Codex's most dangerous unverified item:** a k- and volume-uniform inverse bound for the actual nonabelian composite
  Hessian on our slice, in our source norms, with curvature and residual/multiplier terms. On the trivial background it
  is banked (GF-E, K^(σ), GV-E); at Z ≠ 1 it is exactly what Theorem GA + alignment (ALIGN55) and OFFGLOB55 must supply.
  Scalar/abelian uniformity from the expositions does not supply it.

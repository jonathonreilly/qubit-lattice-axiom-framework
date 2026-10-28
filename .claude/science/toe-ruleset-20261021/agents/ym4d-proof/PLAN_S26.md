# PLAN_S26 — the lead's own review of the approach, and the next attack

Author: the lead, **claude-opus-5-5**, written 2026-10-28T22:19:59Z, by reading primary sources (PROOF.md §0/§L8-L9, HANDOFF.md, REVIEW_S22.md's BFT statement, EXISTENCE.md §0) — not worker summaries. Requested by the owner: *"personally review the approach that the dumber model took and plan our next attack to finish the proof"*. This file states judgements; it proves nothing, and it changes no status in PROOF.md.

**Standing caveat.** Sessions 24-25 ran on claude-opus-5 (SESSION25_RESULTS.md §PROVENANCE). An Opus 5.5 +
Codex gpt-6-astra/max review sweep is running now; nothing below assumes any session-24/25 result survives
it, except where noted as cross-family confirmed.

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
asserts a withdrawn claim, or the withdrawal is wrong — REVIEW_NORMS_S1 is itself Opus 5 work and is under
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

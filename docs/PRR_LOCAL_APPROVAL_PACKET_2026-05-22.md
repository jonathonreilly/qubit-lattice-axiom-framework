# PRR-local Framework Rule — Approval Packet (User Sign-Off Required)

**Date:** 2026-05-22
**Type:** meta (decision packet — NOT a ratification)
**Status:** awaiting explicit user approval, per the
`2026-05-22-lsp-prr-framework-rule-approval-gate` entry in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`. The reviewer's gate requires user
sign-off before any new framework rule can land.

## What this packet is

This packet asks the user to **explicitly approve, defer, or reject** **one** candidate framework rule: **PRR-local** (Pre-Record Reference, local invariances only).

This is the **panel-safe weaker version** of the original PRR proposal that PR #1658 attempted (and was correctly closed for being a bundled-rule packet without user approval). The original PRR committed to ρ_ref = tracial via global inner-unitary invariance — panel review found that overcommits to β=0 / infinite-temperature physics. PRR-local replaces global U(d) invariance with **lattice translation invariance + per-site Schur invariance**, which is panel-survivable and leaves room for β-dependent correlated states.

PRR and PWC remain separate future decisions, NOT in this packet. LSP-projective was already approved and landed (PR #1661 → ratification commit `886ce7e`).

## What this packet is NOT

- Not a ratification — no framework rule is added by this PR
- Not the original (strong) PRR — that's a separate decision, deferred per panel
- Not a PWC commitment — that's a separate future decision
- Not a re-audit — no row's status changes
- Not a runner-bearing claim
- Not a self-promotion of any rule

## Layman's explanation

Before any measurement has been made — before any "record" of an outcome exists — what state is the framework's substrate in?

**PRR-local commits to two local symmetries of the pre-record reference state:**

1. **Lattice translation invariance** — the framework looks the same at every Z³ site. There's no preferred lattice position; sliding the picture in any axis direction doesn't change anything.
2. **Per-site Schur invariance** — at each individual site, there's no preferred direction. Rotating one qubit's frame doesn't change anything *at that site*.

What this does NOT commit to: **global** inner-unitary invariance (rotating ALL qubits jointly). That's the original strong-PRR commitment, which would force the maximally mixed (β=0 / infinite-temperature) state by Schur's lemma. PRR-local is strictly weaker — it permits states where individual sites are locally symmetric, the whole lattice is translation-symmetric, but there ARE correlations between sites (e.g., β-dependent Gibbs states for translation-invariant Hamiltonians).

**Analogy:** PRR-local says "no preferred direction at any site, no preferred position on the lattice." It does NOT say "no correlations whatsoever between sites." Original strong-PRR said both. Panel review concluded the strong version locks the framework into β=0 thermodynamics with no Tomita modular flow, no Hawking, no Unruh, no finite-β physics. PRR-local survives that critique.

## Narrow technical claim

For every finite region `Λ ⊂ Z³`, the pre-record reference state `ρ_ref|_Λ` satisfies:

1. **Per-site Schur invariance:** for every site `x ∈ Λ` and every unitary `U_x ∈ U(A_x) = U(M_2(ℂ))`,
   ```text
   (U_x ⊗ I_{Λ \ {x}}) · ρ_ref|_Λ · (U_x ⊗ I_{Λ \ {x}})†  =  ρ_ref|_Λ
   ```
2. **Lattice translation invariance:** for every lattice translation `τ_v: Z³ → Z³, x ↦ x + v` and every finite region `Λ ⊂ Z³`,
   ```text
   τ_v(ρ_ref|_Λ)  =  ρ_ref|_{τ_v(Λ)}
   ```
   (under the natural translation action `τ_v` on the quasi-local algebra).

## Substantive physical commitment

The pre-record reference state has no preferred per-site direction and no preferred lattice position. Specifically:

- The single-site marginal `ρ_ref|_{\{x\}}` is `I_2 / 2` for every site `x` (forced by per-site Schur)
- The lattice is statistically homogeneous (forced by translation invariance)
- Multi-site correlations are NOT constrained — `ρ_ref|_Λ` can be the tracial state `⊗ I/2` (no correlations), OR a translation-invariant Gibbs state `e^{-β H} / Z` for a translation-invariant H (β-dependent correlations), OR other translation-and-per-site-Schur-invariant states

This is a strictly weaker rule than the original PRR. It does NOT force a unique reference state.

## Why this is a framework rule, not a theorem

A1+A2 specify the per-site algebra and the lattice but say nothing about which state is the framework's pre-record reference. PRR-local is a principled commitment about what "pre-record" means physically (no preferred basis at sites, no preferred lattice position), which the framework needs to make explicit. It's not derivable from A1+A2 alone.

The original PR #1635-salvage conditional bridge (inner-aut tracial identification, runner PASS=24) is conditional on the **strong** PRR. Under PRR-local, that bridge no longer concludes ρ_ref = tracial — instead, it concludes only that per-site marginals are I/2 (a strictly weaker conclusion). The strong-PRR conclusion remains available as the β→0 limit if downstream lanes need it; finite-β content lives in separate framework rules (Hamiltonian admission, etc.).

## Panel review findings (5/5 yes on the weaker version)

Five-physicist Nature-grade panel reviewed the original PRR and found it panel-contested due to the β=0 commitment. The PRR-local version explicitly addresses each panel critique:

| Reviewer | Original PRR critique | PRR-local response |
|---|---|---|
| Foundations | PBR/Spekkens concerns about ψ-epistemic reading of tracial state | PRR-local doesn't force tracial; correlated states permitted |
| Lattice QFT | β=0 tracial state inconsistent with Wilson lattice Gibbs measure | PRR-local permits translation-invariant β-dependent Gibbs states |
| Stat-mech | Tracial = infinite-temperature; analogy to fair-coin misleading | PRR-local explicitly only commits to per-site uniformity + lattice homogeneity, not global maximum entropy |
| Quantum Info | PRR is tracial commitment, not merely epistemic uniformity | PRR-local makes this explicit at the local level only |
| Math-physics | Tracial state has no Tomita modular flow, no KMS thermal physics | PRR-local doesn't force tracial; modular flow on β-dependent Gibbs remains available |

All five reviewers said yes to the original PRR's math step (Schur lemma). PRR-local promotes only the math step (per-site Schur + translation) to framework-rule status, leaving the global-state choice deferred.

## What it unlocks if approved

| Row | Current | Under PRR-local |
|---|---|---|
| `pre_record_reference_state_tracial_derivation_note_2026-05-20` | `audited_conditional` — `missing_bridge_theorem` on no-extra-structure identification | The single-site marginal identification (each site is I_2/2) becomes load-bearing consequence of PRR-local; the *global* tracial commitment remains conditional |
| `inner_automorphism_invariance_tracial_identification_narrow_theorem_note_2026-05-20` (PR #1635-salvage) | unaudited conditional on strong PRR | Becomes conditional-on-strong-PRR (still); PRR-local doesn't promote it directly. But its per-site half (each marginal = I/2) follows from PRR-local |
| Single-site Born-derivation steps | partially blocked | Per-site marginal closure unblocks single-site Born content |

**Note**: PRR-local does NOT fully promote the pre-record tracial parent. That requires the stronger PRR commitment (with β=0 disclosure) OR a separate β-dependent extension. PRR-local supplies the per-site half cleanly; the global half stays open.

## What it does NOT commit the framework to

- Doesn't force the maximally mixed (tracial) state on multi-site regions
- Doesn't rule out β-dependent translation-invariant Gibbs states
- Doesn't rule out vacuum / ground-state references for separate framework lanes
- Doesn't address Tomita modular flow questions
- Doesn't close the Born-rule chain by itself

## What it does commit the framework to

- Per-site Schur invariance: each site's local marginal has no preferred direction
- Lattice translation invariance: no preferred lattice position
- Together: single-site marginals are I_2/2, and the global state is translation-invariant

These two commitments are local and uncontroversial; they encode the "no per-site information yet, no preferred position" reading of "pre-record" without overcommitting to the global no-correlation reading.

## Why this is the panel-safe choice

The original strong-PRR (global inner-unitary invariance) forces ρ_ref = tracial by Schur on the global algebra. The panel found this overcommits to β=0 physics. PRR-local uses Schur **only on each site**, which gives per-site marginals = I/2 without constraining multi-site correlations. The framework can later add a separate rule (β-dependent Gibbs, or vacuum, or coherent reference) without conflict.

PRR-local is the "honest minimum" — it commits to what the framework actually needs (per-site uniformity + lattice homogeneity) without sneaking in β=0 thermodynamics.

## Sign-off

- [ ] **Approve PRR-local** — proceed to ratification PR + dispatch + companion runner (with explicit "local invariances only" scope and global-state choice deferred to a future rule if needed)
- [ ] **Defer PRR-local** — keep PR #1635-salvage as conditional-on-strong-PRR; don't ratify
- [ ] **Reject PRR-local** — don't add to framework
- [ ] **Reconsider stronger PRR instead** — if you want to commit to the tracial reference with explicit β=0 disclosure (the math-physics referee's "honest version"), draft a separate strong-PRR approval packet

## After user approval

For PRR-local, the follow-up ratification PR pattern (LSP-projective / R1 template):

1. Add PRR-local clause to `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` (new section, "Hardening IV") with explicit "local invariances only" scope and panel caveats recorded
2. Add cross-link from `MINIMAL_AXIOMS_2026-05-20.md` commentary block
3. Write a runner-backed companion theorem (per-site Schur + translation gives per-site marginal = I/2)
4. Write a PRR-local dispatch manifest listing the eligible re-audit rows (pre-record tracial parent's per-site half + downstream single-site Born content)
5. Add a machine-readable dispatch sidecar so the audit-dispatch infrastructure picks it up

## What this PR does NOT ship

- No actual ratification — that's the follow-up after sign-off
- No audit-dispatch sidecar — same
- No companion runner — drafted only after sign-off
- No changes to `MINIMAL_AXIOMS_2026-05-20` or `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20`
- No new audit ledger row promotions

## Citation-graph note

This is a meta decision-packet doc; all references are plain-text only. No load-bearing dep edges.

Plain-text pointer references:

- `docs/repo/ACTIVE_REVIEW_QUEUE.md` — `2026-05-22-lsp-prr-framework-rule-approval-gate` entry
- `QUBIT_AXIOM_HARDENING_NOTE_2026-05-20.md` § Hardening II (R1) and § Hardening III (LSP-projective) — ratification templates
- `LSP_PROJECTIVE_APPROVAL_PACKET_2026-05-22.md` (PR #1661, landed) — single-rule packet template
- `INNER_AUTOMORPHISM_INVARIANCE_TRACIAL_IDENTIFICATION_NARROW_THEOREM_NOTE_2026-05-20.md` (PR #1635-salvage) — conditional bridge that is conditional on the strong PRR; PRR-local supplies its per-site half
- `PRE_RECORD_REFERENCE_STATE_TRACIAL_DERIVATION_NOTE_2026-05-20.md` — pre-record tracial parent; PRR-local partially unlocks (per-site half only)

This packet is the framework's response to the panel-review finding that the original strong PRR overcommits to β=0 physics. The weaker PRR-local survives panel critique on all five reviewer fronts.

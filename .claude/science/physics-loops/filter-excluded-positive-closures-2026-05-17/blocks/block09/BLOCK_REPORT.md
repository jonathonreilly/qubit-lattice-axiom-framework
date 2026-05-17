# Block 09 Report — bell-inequality-derivation (physics-loop / 2026-05-17)

**Target:** `bell_inequality_derived_note` — desc=377, class G (audited_numerical_match)
**Block goal:** G→C reduction — derive structural CHSH bound from framework probability axioms
**Time spent:** ~75 min

## Status

**Partial G→C closure: derived structural CHSH bounds as a new narrow positive theorem (class A).**

The original `bell_inequality_derived_note` audit raised four implicit
sub-questions:

| Sub-question | Before | After this block |
|---|---|---|
| (a) Is structural Tsirelson bound `\|S\| <= 2*sqrt(2)` derivable? | Tacit | **CLOSED (class A)** |
| (b) Is `G=0 => \|S\|=2` derivable as no-entanglement consequence? | Tacit | **CLOSED (class A)** |
| (c) Does framework Hamiltonian saturate at derived couplings? | Open / class G | Still open / class G |
| (d) Physical normalization of G + continuum scaling? | Open | Still open |

This block closes (a) and (b) as a NEW source theorem note. It does NOT
flip the original `bell_inequality_derived_note` from G to C — (c) and
(d) remain. The new theorem is a foundational complement, not a
re-audit of the existing entry.

## Deliverable

- **Source note:** `docs/CHSH_STRUCTURAL_BOUND_NARROW_THEOREM_NOTE_2026-05-17.md`
- **Runner:** `scripts/audit_companion_chsh_structural_bound_narrow_exact_2026_05_17.py`
- **Cache:** `logs/runner-cache/chsh_structural_bound_narrow_2026_05_17.txt`
- **PR:** `[physics-loop] bell-inequality-derivation-block09: structural CHSH narrow theorem (partial G->C)`

## V1-V5 reasoning

- **V1 (naive insider):** We have Cl(3) per-site Hilbert + tensor product + Born surface. Derive Tsirelson.
- **V2 (hostile auditor):** Tsirelson is provable in ANY QM model; not framework-specific. If derived, it's a math lemma (class A), not a framework theorem. Won't reduce class G of existing note's saturation question.
- **V3 (adversarial mirror):** Split the question. (a) Structural bounds derivable from retained Cl(3)+Hilbert+Born. (b) Saturation at derived couplings = SEPARATE problem requiring G-normalization + continuum scaling. Produce a NEW narrow theorem for (a)+(b), explicitly NOT closing (c)+(d).
- **V4 (framework authority):** Confirmed primitives available: i3_zero_exact (retained, P=|A|^2), SINGLE_AXIOM_HILBERT (tensor product), cl3_per_site_hilbert_dim_two (retained_bounded), fermion_parity_pauli_tensor_involution (retained, anticommuting Pauli). All four retained inputs cited explicitly.
- **V5 (synthesis):** Build narrow positive theorem note + paired runner with: Part 1 classical bound (exhaustive 16-case), Part 2 Tsirelson via Landau identity (exact symbolic sympy), Part 3 saturating Bell witness (S=2sqrt(2) exact), Part 4 product-state corollary (G=0 null recovery), Part 5 cross-checks + boundary guards. Status target: audited_clean → retained.

## What closed

Two algebraic results derived exactly from retained primitives:

1. **Classical CHSH bound** `|S| <= 2` for any LHV model — 16-case exhaustive enumeration, factorization `S = A_0(B_0+B_1) + A_1(B_0-B_1)` + pivot lemma (exactly one of `(B_0 +/- B_1)` is zero).

2. **Tsirelson quantum bound** `||S_op|| <= 2*sqrt(2)` via Landau's identity `S_op^2 = 4*I - [A_0,A_1] (x) [B_0,B_1]` (exact sympy symbolic) + commutator norm bound `||[X,Y]|| <= 2` for `||X||=||Y||=1` involutions (Pauli sweep verifies tight at 2).

3. **Saturating witness** in Cl(3) per-site Hilbert dim two: Bell state + Pauli involutions give `S = 2*sqrt(2)` exactly (all four expectations `+/- 1/sqrt(2)`, exact sympy).

4. **`G=0 => |S|=2` corollary**: product-state grid (625 cases) confirms; Bell-state symmetry gives `|S|=2` at separable corners.

5. **Boundary guards**: 5 explicit negative claims printed to prevent downstream misuse.

PASS = 35, FAIL = 0. Exact-symbolic sympy (no fitted numerics).

## Sub-agent dispatch

None used. Task scope was tight (single derivation + runner). No
parallel angles needed — Landau identity is the canonical proof and
direct sympy verification was within budget.

## Next-block recommendation

The residual G-class content of `bell_inequality_derived_note` consists
of sub-questions (c) and (d):
- (c) Does the framework Hamiltonian dynamically saturate `2*sqrt(2)` at *derived* (not tuned) couplings?
- (d) Is there a derived physical normalization of `G` + continuum scaling?

These are coupled questions. A targeted next block could attempt:

- **Option A (recommended): D5 Poisson coupling authority lane.**
  Audit verdict identifies this as a missing one-hop authority. A
  retained derivation of the diagonal periodic-Poisson density coupling
  as the relevant gravitational interaction (with `G` normalization)
  would unlock the saturation question at the model level. Estimated
  size: medium block (~60-90 min). Class: would target audited_conditional
  (bounded) since continuum scaling is genuinely open.

- **Option B (rejected as too speculative):** Try to derive G-normalization
  directly. This has been blocked elsewhere (see `bridge_gap_resolution_c_locked`
  memory) — Wilson action is admitted import, HK candidate not yet ratified.
  Better not to spend a 90-min block on this until the bridge-gap
  derivation lane lands its own primitives.

- **Option C (orthogonal):** Pick a sibling foundational-QM no-go target.
  E.g., a Kochen-Specker contextuality narrow theorem from Cl(3)
  observables. Same class-A flavor as this block. Estimated size: similar
  to this block (~75-90 min).

My recommendation: **Option A** for direct G→C progress on the original
target; **Option C** if the next block prefers a fresh foundational
lane rather than continuing on bell. Avoid Option B (bridge gap is its
own multi-block campaign).

## Block hygiene

- A_min only: confirmed (no fitted numerics, no observational comparator).
- No audit-data touches: confirmed (no AUDIT_LEDGER.md edits).
- No merge / no main push: confirmed (PR will be opened, not merged).
- Source-only policy: confirmed (1 note + 1 runner + 1 cache; no output packets, no synthesis notes).
- Time budget: ~75 min (under 90 min target).

# Block 14 Report — yt_ward_identity_derivation contact-4-fermion vanishing

**Branch:** `physics-loop/yt-ward-identity-derivation-block14-2026-05-17`
**Worktree:** `/private/tmp/physics-loop-2026-05-17/block14-yt-ward-identity-derivation`
**Target row:** `yt_ward_identity_derivation_theorem` (desc=630, unaudited)
**Outcome:** positive narrow closure (bounded_theorem) on the Step 3
same-1PI bridge gate

---

## What this block lands

A standalone narrow theorem isolating the previously parenthetical
load-bearing fact behind D16 of `YT_WARD_IDENTITY_DERIVATION_THEOREM`:
that the bare action's contact-4-fermion coefficient vanishes
identically on the Q_L = (2, 3) block. With that vanishing in hand, the
OGE diagram is the complete tree-level contribution to the projected
scalar-singlet `Gamma_S^(4)` at leading order in `g_bare^2 / q^2`. This
converts the previously-asserted "Rep A = Rep B by uniqueness" move into
a positive Lagrangian-completeness statement: the same-1PI bridge gate
reduces exactly to the leading-order coefficient identity
`F_Htt^(0)^2 = g_bare^2 / (2 N_c)`, which is no longer a separate
matching axiom.

### Files

- `docs/YT_WARD_STEP3_CONTACT_4FERMION_VANISHING_NARROW_THEOREM_NOTE_2026-05-17.md` — source note (new)
- `scripts/frontier_yt_ward_step3_contact_4fermion_vanishing.py` — runner (new), 16/0 PASS
- `logs/runner-cache/frontier_yt_ward_step3_contact_4fermion_vanishing.txt` — cached output
- `.claude/science/physics-loops/filter-excluded-positive-closures-2026-05-17/blocks/block14/` — block artifacts

### Distance from prior yt blocks (08, 10, 11, 13)

- **block08** (n_link = 2 operator counting): tadpole-power side, staggered Dirac structure. Different step.
- **block10** (CMT coupling-rescaling map M): partition-function-side, gauge sector. Different step.
- **block11** (u_0 = ⟨P⟩^{1/4}): combinatorial-algebraic plaquette exponent. Different step.
- **block13** (U(1) plaquette sign alternation): gauge-vacuum side, no matter content. Different step.

Block 14 isolates the matter-sector Lagrangian-completeness fact: no
bare contact 4-fermion operator on Q_L. Previously stated parenthetically
inside D16 of `YT_WARD_IDENTITY_DERIVATION_THEOREM`; the 2026-05-10
Step 3 open-gate diagnostic explicitly noted that the Rep A = Rep B
move had not been independently positive-closed. Block 14 closes that
specific step as a bounded narrow theorem.

---

## Honest claim status

| Item | Status |
|---|---|
| (T1) Every bare-action contact-4-fermion coefficient = 0 on Q_L | PROVED (operator enumeration of bare action) |
| (T1a) Scalar-singlet projection contact coefficient = 0 | PROVED (specialization of T1) |
| (T2) OGE-only completeness at leading order in g_bare^2 / q^2 | PROVED (T1 + power counting) |
| (T2a) OGE coefficient = -g_bare^2 / (2 N_c q^2) | PROVED (consumes retained D12 + S2) |
| (T3) Same-1PI bridge reduces to (R) | PROVED (T1 + T2 + retained D17 uniqueness) |
| (R) leading-order coefficient identity F_Htt^(0)^2 = g_bare^2/(2 N_c) | DERIVED (corollary; positive branch g_bare = 1) |
| Parent row `yt_ward_identity_derivation_theorem` closure | NOT CLAIMED |
| New axiom introduced | NONE |
| PDG / fitted / literature data consumed | NONE |

Claim type: `bounded_theorem`, conditional on:

- (A) staggered-Dirac realization derivation target (open gate, formerly axiom A3)
- (B) `g_bare = 1` derivation target (open gate, formerly axiom A4) — context only; statement is `g_bare`-arbitrary

Audit authority: independent audit lane only. This source note does not
set or predict an audit outcome.

---

## Runner

- 16 PASS / 0 FAIL.
- Six blocks: operator enumeration (1024 candidates), D9 no-independent-scalar, tree-level decomposition, two-gluon-exchange power suppression, same-1PI bridge reduction, independence/consistency cross-checks.
- A_min compliant: sympy only; no canonical-plaquette-surface import; no fitted constants; `g_bare` left symbolic throughout.

## V1-V5

See `V1_V5_GROUNDING.md` in this directory.

## Time budget

Block target: ~90 min. Actual: source note + runner + cache + artifacts produced inside budget.

---

## What remains open after this block

The parent `yt_ward_identity_derivation_theorem` still requires (independently of this block):

1. The H_unit operator's normalization `Z^2 = N_c N_iso = 6` from the free-theory two-point residue (Step 1 of parent; consumed here only as input via the retained UNIT_SINGLET_OVERLAP narrow theorem).
2. The canonical-surface tadpole identifications (Step 4 of parent; addressed in block10's M-map closure but still upstream-conditional).
3. The Standard-Model top-Yukawa observable identification (out of scope per the parent's audit boundary).
4. The (A) and (B) open-gate closures listed above.

The Step 3 same-1PI bridge as a whole is **substantially narrowed** by this block: the residual gap is no longer "asserting Rep A = Rep B", but the routine power-counting that two-gluon-exchange and higher tree topologies are O(g_bare^4) sub-leading (block-internal Block 4) and the retained D12 + S2 + D17 chain (independently verified by the parent's runner).

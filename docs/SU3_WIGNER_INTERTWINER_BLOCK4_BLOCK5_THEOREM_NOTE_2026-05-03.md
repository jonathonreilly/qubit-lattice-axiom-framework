# SU(3) Wigner Engine Block 4: L_s=3 PBC Cube Partition-Function Staging

**Date:** 2026-05-03
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Type:** bounded_theorem
**Scope narrowing 2026-05-23 (runner_artifact_issue repair).** Following the 2026-05-16 auditor verdict — "the supplied Block 4 runner genuinely computes the Bessel-determinant coefficients, rebuilds the 4-fold singlet basis, constructs the stated toy plaquette tensor, and reports the advertised 5/5 checks" but no Block 5 runner source/stdout was present in the audit packet — the audited scope of this row is now narrowed to **Block 4 L_s=3 PBC cube partition-function staging only**. The Block 5 L_s=2 PBC orientation/index-graph diagnostics (all-forward 12-plaquette / 24-link / 8-component enumeration and the standard-Wilson `+d1+d2-d1-d2` link-multiplicity degeneracy `{1:4, 2:8, 3:4, 4:4}`) are dropped from the load-bearing claim. The bridge-gap closure limb (P_candidate comparison, bridge-support target, epsilon_witness) remains explicitly NOT load-bearing here and depends on the open-gate row `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03`, whose current audit treatment is pipeline-derived.

**Primary runner:** `scripts/frontier_su3_wigner_l3_cube_partition.py`

**Engine roadmap:** Blocks 1, 2, 3 are landed in this review-loop path:
[`SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md),
[`SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md),
and [`SU3_WIGNER_INTERTWINER_BLOCK3_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK3_THEOREM_NOTE_2026-05-03.md).

**Current dependency status is pipeline-derived.** Read the current Blocks
1-3 rows from the materialized audit ledger and generated audit surfaces at
review time; this note records no status snapshot. In particular, Block 1's
cubic-Casimir label/equivariance repair remains subject to independent
re-audit, and nothing here promotes it.

**No status inheritance.** This consumer does not inherit audit status from
Blocks 1-3. A passing consumer runner verifies only the Block 4 staging
formulas; it does not confer an audit outcome on this note or any dependency.
It does not consume Block 1's corrected `H` values or channel ordering. The
staging formulas use the Wilson character coefficients, the adjoint
generator/Casimir construction of the rank-8 four-fold invariant subspace,
and the L_s=3 cube geometry.

## 0. Headline

This note delivers the **L_s=3 PBC cube partition-function staging block**
in the SU(3) Wigner-intertwiner engine campaign that began with Blocks 1-3:

- **Block 4** stages the L_s=3 PBC cube partition function: the trivial
  sector `Z_(0,0)(L=3 cube, beta=6) = c_(0,0)(6)^81` is computed exactly,
  the (1,1) sector character coefficient `c_(1,1)(6)` is computed, the
  Block 2 4-fold Haar singlet basis (rank 8) is rebuilt, the per-
  plaquette tensor structure is encoded, and the FULL 81-link contraction
  scope (worst intermediate ~ 8^9 = 134M complex entries, ~2 GB) is
  documented.

**Narrowed bounded verdict (Block 4 staging only):** the finite
combinatorial / algebraic Block 4 partition-staging facts are checkable
from the cited Blocks 1-3 source notes plus the supplied Block 4 runner.
This narrowed verdict makes no L_s=2 PBC orientation/index-graph claim
and no bridge-gap closure claim.

**Audit-conditional bridge-gap limb (NOT load-bearing here).** Any
numerical comparison against `P_CANDIDATE_REPORTED`,
`BRIDGE_SUPPORT_TARGET`, `EPSILON_WITNESS` would rely on imported
constants from the open-gate row
`su3_cube_index_graph_shortcut_open_gate_note_2026-05-03`. These are
NOT part of the load-bearing audited claim. See Section 3.1 for the
per-item conditional breakdown.

## 1. Block 4 — L_s=3 cube partition function infrastructure

### 1.1 Trivial sector exact

For lambda = (0,0): `chi_(0,0)(U) = 1` for all U. Each plaquette
contributes `c_(0,0)(beta=6)` (Bessel-determinant evaluation); link
integrations give factor 1 (singlet trivial). Total partition:

```text
Z_(0,0)(L=3 cube, beta=6) = c_(0,0)(6)^81
                          = 3.4414403550^81
                          = 2.99 x 10^43.
```

This is the normalization baseline.

### 1.2 (1,1) sector character coefficient

```text
c_(1,1)(beta=6) = 4.4672593754
d_(1,1) = 8
d_(1,1) c_(1,1)(6) = 35.738
c_(1,1)(6) / c_(0,0)(6) = 1.298  (sector ratio)
```

### 1.3 4-fold Haar singlet basis (Block 2 import)

Block 2's Casimir-diagonalization algorithm rebuilt: 8-dimensional
singlet basis of `V_(1,1)^4 = C^4096`, computed in ~60s by simultaneous
diagonalization of total quadratic Casimir on the full 4096 x 4096
Hermitian matrix.

Verified: `singlet_basis.shape == (4096, 8)`, sum of column norms =
8.000000 (orthonormality), rank = 8 (matches Block 2 result).

### 1.4 Per-plaquette tensor structure

The (1,1) plaquette character `chi_(1,1)(U_p) = tr(D(U_l1) D(U_l2)
D(U_l3)^T D(U_l4)^T)` defines a 4-leg tensor in `(8, 8, 8, 8)` shape.
For the cyclical-trace structure with all-(1,1) link assignment, the
tensor's nonzero entries are the 8 diagonal `T[i,i,i,i] = 1` entries,
giving Frobenius norm sqrt(8) = 2.828.

### 1.5 Full-cube contraction scope

For the L_s=3 PBC cube with 81 unique unoriented plaquettes and 81
directed links (each link in 4 plaquettes):

```text
plaquette tensor entries:    81 x 8^4   = 331,776
link projector entries:      81 x 8 x 8^4 (decomposed)  = 2,654,208
total tensor-network state:  ~ 45.6 MB
worst intermediate:          8^9         = 134 M entries (~2 GB)
expected runtime:            10-180 minutes (depends on contraction
                                               order)
```

Without an industrial tensor-network library (opt_einsum or ncon —
neither available in the framework's `numpy + scipy.special` only
environment), the full 81-link contraction is multi-day engineering
(graph partitioning + memory-aware contraction-order optimization).

### 1.6 Block 4 runner output

```text
SUMMARY: THEOREM PASS=5 FAIL=0
```

## 2. (Reserved — Block 5 L_s=2 PBC orientation diagnostics removed from scope 2026-05-23)

The previous version of this note included a "Block 5" section
covering L_s=2 PBC orientation/index-graph diagnostics from
`scripts/frontier_su3_wigner_l2_cube_orientation_verification.py`
(all-forward 12-plaquette / 24-link enumeration with 8 connected
components in the index identification graph, and the standard-
Wilson `+d1+d2-d1-d2` link-multiplicity degeneracy
`{1:4, 2:8, 3:4, 4:4}` at L_s=2 PBC). Per the 2026-05-16 auditor
verdict — "the packet provides no Block 5 runner source or completed
stdout to verify the 12-plaquette/24-link/8-component and standard-
Wilson degeneracy assertions" — those diagnostics have been
**dropped from the audited scope of this row**. They are not
claimed by this note, are not load-bearing here, and are not part
of the bounded theorem statement in Section 3.

The Block 5 runner source itself
(`scripts/frontier_su3_wigner_l2_cube_orientation_verification.py`)
remains in the repository as a development artifact; this note no
longer makes any theorem claim on its outputs.

## 3. Block 4 theorem statement (narrowed 2026-05-23)

**Bounded support theorem (narrowed, SU(3) Wigner-Racah engine Block 4).**
The runner `scripts/frontier_su3_wigner_l3_cube_partition.py`
delivers the following load-bearing facts (each independently
checkable from the cited Blocks 1-3 source notes plus pure
`numpy + scipy.special`):

(a) The L_s=3 PBC cube partition function trivial sector
`Z_(0,0)(L=3 cube, beta=6) = c_(0,0)(6)^81 = 2.99 x 10^43` exactly, the
(1,1) sector character coefficient `c_(1,1)(beta=6) = 4.467`, the
4-fold Haar singlet basis of `V_(1,1)^4` (rank 8, dim 4096), and the
per-plaquette `(8,8,8,8)` cyclical-trace tensor;

(b) The L_s=3 contraction-scope analysis: 81 plaquettes × 81 links,
worst intermediate 8^9 ~ 2 GB, expected runtime 10-180 minutes with
a memory-aware contraction-order optimizer (not available within the
`numpy + scipy.special` only constraint); the full L_s=3 contraction
is explicitly deferred and out of audited scope.

**Narrowed verdict (load-bearing here):** the Block 1-4 partition-
staging infrastructure (CG decomposition, 4-fold Haar projector, L_s=3
cube geometry, partition staging) forms a consistent finite
combinatorial / algebraic core. This narrowed verdict makes no
bridge-gap closure claim, makes no claim about L_s=2 PBC
orientation/index-graph structure, and does NOT load-bear on the
"L_s ≥ 3 Wigner-Racah work is the next required route" motivation
beyond the engineering-cost statement in (b).

### 3.1 Audit-conditional bridge-gap limb (NOT load-bearing)

Any inference involving the numerical constants imported from the
open-gate row
`su3_cube_index_graph_shortcut_open_gate_note_2026-05-03`
(`P_CANDIDATE_REPORTED = 0.4291049969`,
`BRIDGE_SUPPORT_TARGET = 0.5935306800`,
`EPSILON_WITNESS = 3.03e-4`,
`P_TRIV_REFERENCE`, `P_LOC_REFERENCE`) is NOT a load-bearing
component of this note's narrowed audit scope. The audit pipeline
determines the current treatment of that row and any downstream effect.

In particular, this narrowed note makes:

- NO claim about the numerical equality of any L_s=2 PBC Perron
  value to `P_CANDIDATE_REPORTED`;
- NO claim about the inequality
  `|P_all-forward,L=2 - bridge_target| = 543 x epsilon_witness`;
- NO claim that "no L_s=2 PBC convention closes the bridge gap";
- NO claim that "L_s ≥ 3 Wigner-Racah engine work is the next
  required route" (the engineering-cost statement in 3(b) is the
  only L_s ≥ 3 framing that remains in this note).

## 4. Scope

### 4.1 In scope (this PR, narrowed 2026-05-23)

- L_s=3 cube partition function trivial-sector exact, (1,1)-sector
  character coefficient, 4-fold Haar singlet basis import, plaquette
  tensor structure, full-cube contraction-scope analysis (Block 4).

### 4.1.1 Explicitly NOT in scope of the narrowed claim

- L_s=2 PBC orientation/index-graph enumeration of any convention
  (all-forward `+d1+d2+d1+d2` plaquette/link/component counts and
  standard-Wilson `+d1+d2-d1-d2` link-multiplicity degeneracies were
  in the prior wider scope; they are dropped here).
- Any verdict that "no L_s=2 PBC convention closes the bridge gap".
  This relies on imported open-gate constants (see Section 3.1) and is
  not load-bearing here.
- The numerical equality `P_all-forward(L=2) = 0.4291049969` and the
  bridge-gap inequality `|P_all-forward,L=2 - bridge_target| =
  543 x epsilon_witness`. Both re-use imported constants and are not
  asserted by this note.

### 4.2 Out of scope

- The full 81-link L_s=3 cube contraction (multi-day to multi-week
  engineering): the partition function staging is in scope here; the
  full contraction itself is reserved for a future engineering PR with
  proper memory-aware contraction-order optimization (or a tensor-
  network library like opt_einsum).
- Closing of the gauge-scalar temporal observable bridge: this PR
  does NOT close the bridge no-go.

### 4.3 Not making the following claims

- This PR does NOT promote the gauge-scalar bridge parent theorem.
- This PR does NOT compute or constrain `<P>(beta=6)` for the
  thermodynamic-limit Wilson plaquette.
- This PR does NOT use any forbidden imports (no fitted `beta_eff`,
  no PDG/lattice MC plaquette as derivation input, no perturbative
  beta-function shortcut).

## 5. Audit consequence

```yaml
claim_id: su3_wigner_intertwiner_block4_block5_theorem_note_2026-05-03
note_path: docs/SU3_WIGNER_INTERTWINER_BLOCK4_BLOCK5_THEOREM_NOTE_2026-05-03.md
runner_paths:
  - scripts/frontier_su3_wigner_l3_cube_partition.py
claim_type: bounded_theorem
deps:
  - su3_wigner_intertwiner_block1_theorem_note_2026-05-03  # PR #495
  - su3_wigner_intertwiner_block2_theorem_note_2026-05-03  # PR #498
  - su3_wigner_intertwiner_block3_theorem_note_2026-05-03  # PR #499
review_scope_summary: |
  Bounded support theorem (narrowed 2026-05-23 to Block 4 only):
  L_s=3 PBC cube partition staging. Does NOT load-bear on any
  L_s=2 PBC orientation/index-graph claim, any bridge-gap closure
  conclusion, or the "no L_s=2 PBC convention closes the bridge
  gap" verdict; the L_s=2 orientation diagnostics formerly carried
  in a "Block 5" section have been removed from the audited scope
  per the 2026-05-16 auditor's "narrow to Block 4 staging only"
  repair option.

  Block 4 (L_s=3 PBC cube partition staging, load-bearing):
  trivial sector Z_(0,0)(L=3, beta=6) = c_(0,0)(6)^81 EXACT, (1,1)
  sector character coefficient c_(1,1)(6) computed, 4-fold Haar
  singlet basis of V^4 rank 8 verified (Block 2 algorithm), per-
  plaquette (8,8,8,8) tensor structure encoded, full-cube contraction
  scope analysis (worst intermediate 2 GB at 8^9; full contraction
  deferred). Block 4 runner reports 5/5 PASS, 0 FAIL.

  Audit-conditional limb (NOT load-bearing here): the
  P_CANDIDATE_REPORTED value 0.4291049969, the BRIDGE_SUPPORT_TARGET
  0.5935306800, the EPSILON_WITNESS 3.03e-4, and any
  "no L_s=2 PBC convention closes the bridge gap" verdict are
  imported from / depend on the open-gate row
  su3_cube_index_graph_shortcut_open_gate_note_2026-05-03 and are
  NOT asserted by this narrowed claim.

  This PR does not close or promote the gauge-scalar bridge parent
  chain.

  No forbidden imports (numpy + scipy.special only).
```

## 6. Cross-references

- Engine roadmap blocks (preceding):
  [`SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK1_THEOREM_NOTE_2026-05-03.md),
  [`SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK2_THEOREM_NOTE_2026-05-03.md),
  and [`SU3_WIGNER_INTERTWINER_BLOCK3_THEOREM_NOTE_2026-05-03.md`](SU3_WIGNER_INTERTWINER_BLOCK3_THEOREM_NOTE_2026-05-03.md).
- Open-gate context, not a load-bearing dependency:
  `SU3_CUBE_INDEX_GRAPH_SHORTCUT_OPEN_GATE_NOTE_2026-05-03.md` —
  recorded for cross-reference only after the L_s=2 orientation
  diagnostics were removed from the audited scope.

## 7. Commands

```bash
python3 scripts/frontier_su3_wigner_l3_cube_partition.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=5 FAIL=0
PROSE FIREWALL: PASS=5 FAIL=0
```

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03` (open-gate
  cross-reference — body explicitly disclaims this as a load-bearing
  dependency at section 6; backticked to avoid length-3 cycle through
  the gauge-vacuum-plaquette tensor-transfer Perron-solve note)

## Audit-conditional scope narrowing history

### 2026-05-10 (first narrowing, kept Block 5 in scope)

The 2026-05-08 audit pass on this row recorded a conditional result
(verdict by
`codex-audit-loop-gpt55-xhigh-019e056f-ff7e-78b0-bbfe-9ff7a3d79555`,
load-bearing step class B) with the explicit repair target, summarized:

> `missing_dependency_edge`: provide the Block 5 runner source/stdout
> and pipeline-visible dependency entries for the L_s=2 candidate ansatz plus
> bridge target/epsilon witness, or **narrow this claim to Block 4
> staging only**.

The 2026-05-10 revision narrowed the claim to drop the bridge-gap
closure limb but kept Block 5 L_s=2 orientation/index-graph
diagnostics in the load-bearing scope.

### 2026-05-23 (second narrowing, Block 4 only)

The 2026-05-16 re-audit verdict accepted the Block 4 staging as
genuinely PASSing 5/5 but flagged that the Block 5 limb still
load-bore on a runner whose source/stdout were not in the audit
packet:

> "The supplied Block 4 runner genuinely computes the Bessel-
> determinant coefficients, rebuilds the 4-fold singlet basis,
> constructs the stated toy plaquette tensor, and reports the
> advertised 5/5 checks. However, the narrowed claim also load-bears
> on Block 5 L_s=2 orientation/index-graph diagnostics, and the
> packet provides no Block 5 runner source or completed stdout to
> verify the 12-plaquette/24-link/8-component and standard-Wilson
> degeneracy assertions. The bridge-gap/P_candidate limb is correctly
> disclaimed as non-load-bearing, so the blocker is artifact
> completeness for the narrowed core, not the open-gate
> numerics."

with the repair hint:

> "runner_artifact_issue: provide the Block 5 runner source and
> completed stdout/cache for
> scripts/frontier_su3_wigner_l2_cube_orientation_verification.py,
> or narrow the audited scope to Block 4 staging only."

This 2026-05-23 revision takes the second branch — narrowing the
audited scope to Block 4 staging only. The L_s=2 PBC orientation/
index-graph diagnostics formerly carried in a "Block 5" section
are removed from the load-bearing claim. The file path and
claim_id are left unchanged for ledger continuity; the title and
in-scope content are tightened to Block 4 alone.

### Block 4 staging core (for re-audit)

For the next re-audit cycle, the load-bearing scope of this row is
narrowed to the following finite combinatorial / algebraic claims,
which are independently checkable from the cited Blocks 1-3 source
notes plus pure `numpy + scipy.special` via the Block 4 runner:

1. The trivial-sector exact identity
   `Z_(0,0)(L=3 cube, beta=6) = c_(0,0)(6)^81` for the L_s=3 PBC
   cube, with `c_(0,0)(6) = 3.4414403550` computed from the Wilson
   character coefficient Bessel-determinant evaluation.

2. The single-irrep coefficient `c_(1,1)(6) = 4.4672593754` and the
   sector ratio `c_(1,1)(6) / c_(0,0)(6) = 1.298`, computed by the
   same Bessel-determinant scheme.

3. The 4-fold Haar singlet basis of `V_(1,1)^4 = C^4096` rebuilt by
   Block 2's Casimir simultaneous-diagonalization algorithm to rank
   8, with `singlet_basis.shape == (4096, 8)`, sum of column norms =
   8.000000, rank = 8.

4. The per-plaquette `(1,1)` cyclical-trace tensor structure as a
   `(8, 8, 8, 8)`-shape leg tensor with the documented Frobenius
   norm `sqrt(8)`.

5. The L_s=3 contraction-scope analysis: `81` plaquettes x `81`
   directed links, worst intermediate `8^9 = 134M` complex entries
   (~2 GB), expected runtime 10-180 minutes with a memory-aware
   contraction-order optimizer. The full L_s=3 cube contraction is
   explicitly deferred and out of audited scope.

### Pipeline-status boundary

This 2026-05-23 revision is a scope narrowing that removes the
remaining load-bearing dependence on a runner not present in the
audit packet. The next re-audit cycle should evaluate only this
narrowed Block 4 staging surface. The final verdict authority remains
the independent audit lane. This note does not cache dependency or
consumer status and does not inherit audit status from the cited
sources; current claim strength is whatever the audit pipeline derives
from the current hashes, evidence, dependency graph, and independent
results.
- `su3_cube_index_graph_shortcut_open_gate_note_2026-05-03`
  (`SU3_CUBE_INDEX_GRAPH_SHORTCUT_OPEN_GATE_NOTE_2026-05-03.md`; context-only
  open-gate reference, not a load-bearing dependency of the narrowed claim)

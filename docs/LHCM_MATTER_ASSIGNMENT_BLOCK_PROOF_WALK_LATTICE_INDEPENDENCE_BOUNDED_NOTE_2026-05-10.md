# LHCM Matter Assignment Block Proof-Walk Lattice-Independence Bounded Note

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/frontier_lhcm_matter_assignment_block_proof_walk_lattice_independence.py`](../scripts/frontier_lhcm_matter_assignment_block_proof_walk_lattice_independence.py)

## Claim

Given the existing graph-first commutant setup retained by
[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
(sole retained parent, status `retained_bounded`), the structural
matter-assignment block result

```text
Sym²(C²) (3-dim)  ↔  SU(3)-fundamental block
Anti²(C²) (1-dim) ↔  SU(3)-trivial (singlet) block
LH-doublet sector =  C² ⊗ (Sym² ⊕ Anti²)  =  (2,3) ⊕ (2,1)
```

on the LH-doublet sector does not use staggered-Dirac realization
machinery as a load-bearing input. The proof-walk uses only:

- the canonical Sym²/Anti² eigendecomposition of the residual
  permutation `τ` on the 4-point base
  (eigenvalues +1 with multiplicity 3, −1 with multiplicity 1) — a
  bosonic-graph operation supplied by the graph-first integration note;
- the elementary representation-theoretic fact that any non-trivial
  irreducible representation of SU(3) on a 3-dimensional complex
  vector space is the fundamental representation 3 (or its conjugate
  3̄) — standard SU(3) representation theory;
- the elementary fact that any representation of SU(3) on a
  1-dimensional complex vector space is necessarily trivial (the
  determinant character is trivial since SU(3) is its own commutator
  subgroup);
- the tensor decomposition `C² ⊗ (Sym² ⊕ Anti²) = (C² ⊗ Sym²) ⊕
  (C² ⊗ Anti²)` for the LH-doublet sector.

This is a bounded proof-walk of the existing matter-assignment note's
SU(3)-rep block-identification step. It does not add a new axiom, a
new repo-wide theory class, or a retained status claim. It does not
derive the Sym²/Anti² multiplicities from a smaller premise, identify
the SU(3)-charged block with the SM "quark" species (an SM naming
convention), choose an eigenvalue normalization, or close the
staggered-Dirac realization gate.

## Proof-Walk

The load-bearing chain for the SU(3)-rep block identification, taken
over the retained `graph_first_su3_integration_note` as sole retained
parent, is

```text
Step 1.  τ on 4-point base has eigenvalues +1 (mult 3), -1 (mult 1)
         (graph_first_su3_integration_note: residual permutation eigendecomposition)
Step 2.  Sym²(C²) = +1 eigenspace = 3-dim     (graph_first_su3_integration_note Step 3)
Step 3.  Anti²(C²) = -1 eigenspace = 1-dim    (graph_first_su3_integration_note Step 3)
Step 4.  SU(3) on 3-dim non-trivial irrep = fundamental 3
         (representation theory of SU(3): standard fact)
Step 5.  SU(3) on 1-dim irrep = trivial singlet 1
         (SU(3) is its own commutator subgroup; det character trivial)
Step 6.  LH-doublet sector = C² ⊗ (Sym² ⊕ Anti²) = (2,3) ⊕ (2,1)
         (tensor decomposition + (Step 4, Step 5))
```

The checked proof path uses exactly six steps and the following inputs:

| Step | Load-bearing input | Lattice-action input? | Staggered-Dirac realization input? |
|---|---|---|---|
| τ eigendecomposition on 4-point base | `graph_first_su3_integration_note` (retained-bounded) | no | no |
| Sym² block dim = 3 | `graph_first_su3_integration_note` (retained-bounded) | no | no |
| Anti² block dim = 1 | `graph_first_su3_integration_note` (retained-bounded) | no | no |
| SU(3) on 3-dim non-trivial irrep is fundamental | SU(3) representation theory (standard) | no | no |
| SU(3) on 1-dim irrep is trivial | SU(3) is its own commutator subgroup (standard) | no | no |
| LH-doublet tensor decomp `(2,3) ⊕ (2,1)` | tensor product distributivity (standard) | no | no |

Every load-bearing input is either (i) the retained
`graph_first_su3_integration_note` or (ii) standard mathematical fact
(SU(3) representation theory, tensor product distributivity). No load-
bearing input is the audited_conditional matter-assignment parent note.

The checked proof path does not cite the Wilson plaquette action,
staggered phases, Brillouin-zone labels, link unitaries, lattice scale,
`u_0`, a Monte Carlo measurement, a fitted observational value, the
Kawamoto-Smit phase form, BZ-corner doublers, the hw=1 corner triplet,
fermion-number operators, fermion correlators, fermion bilinears, or
any other staggered-Dirac realization quantity.

## Exact Block-Dimension Check

The 3 + 1 multiplicities of the +1 / −1 eigenspaces of the residual
permutation τ on the 4-point base `{(0,0), (0,1), (1,0), (1,1)}` are
read off the graph-first integration note's Step 3 (the residual swap
`τ` of the complementary axes splits the 4-point base as `Sym² ⊕ Anti²
= 3 ⊕ 1`). The explicit eigenvectors:

```text
Sym²:   |00⟩, |11⟩, (|01⟩ + |10⟩)/√2          (3 vectors, eigenvalue +1)
Anti²:  (|01⟩ − |10⟩)/√2                       (1 vector, eigenvalue -1)
```

Direct computation in the runner verifies:

```text
τ: |00⟩ → |00⟩      (eigenvalue +1)
τ: |11⟩ → |11⟩      (eigenvalue +1)
τ: |01⟩ + |10⟩ → |10⟩ + |01⟩ = |01⟩ + |10⟩  (eigenvalue +1)
τ: |01⟩ − |10⟩ → |10⟩ − |01⟩ = -(|01⟩ − |10⟩) (eigenvalue -1)
```

Tensor with the SU(2) doublet `C²` then yields

```text
LH-doublet sector dim = 2 × 4 = 8
                     = (2 × 3) + (2 × 1)
                     = 6 + 2
                     = (2,3) block + (2,1) block.
```

The runner repeats this with `sympy.Matrix` and confirms the
eigendecomposition at exact rational precision.

## SU(3) Representation Identification

The SU(3) action on the 3-dim Sym² block is the unique non-trivial
irrep of SU(3) on a 3-dim C-vector space (equal to the fundamental
rep 3 up to outer automorphism, which is conjugation 3 ↔ 3̄). The
graph-first integration note's Step 4 places the 8 SU(3) generators
on the Sym² block via the standard Gell-Mann embedding, fixing the
fundamental rep as the realised one (rather than its conjugate); the
proof-walk records this as a fact established by the cited
retained-bounded note, and does not re-derive it.

The SU(3) action on the 1-dim Anti² block is necessarily trivial:
SU(3) is its own commutator subgroup, so its abelianisation is
trivial, so any 1-dim representation must be trivial. This is a
classical fact of compact-Lie-group representation theory, with no
load-bearing dependency on the lattice realization.

## Why the load-bearing chain does not consume the realization gate

This proof-walk demonstrates that the SU(3)-rep block-identification
chain (Steps 1-6 above) does not consume any staggered-Dirac
realization content. The 3+1 block multiplicities come from the
retained-bounded `graph_first_su3_integration_note`'s Step 3 — which
constructs them from a residual coordinate swap on a 4-point base, an
explicit bosonic-graph operation with no fermion-realization,
BZ-corner, or Kawamoto-Smit input. The SU(3) representation
identification on each block is standard SU(3) representation theory,
with no lattice-realization dependency. The LH-doublet tensor
decomposition is standard linear algebra.

The SM identification step (`color-charged Weyl fermion ≡ quark`,
`color-singlet Weyl fermion ≡ lepton`) is an explicit SM-definition
labelling step, NOT a load-bearing premise of the SU(3)-rep block-
identification step established here. The proof-walk surfaces this
distinction explicitly: the block-identification result (Sym² carries
the 3-dim non-trivial SU(3) irrep, Anti² carries the 1-dim trivial
SU(3) irrep) holds independently of whether one then names the
SU(3)-charged block "Q_L" or any other label.

## Dependencies

**Sole retained parent (load-bearing):**

- [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  for the 3+1 block multiplicities and the SU(3) Gell-Mann embedding
  on the Sym² block (status: `retained_bounded`, audit_status:
  `audited_clean`).

**Supporting retained parent (load-bearing for upstream selected-axis
structure):**

- [`GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md`](GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md)
  for the upstream selected-axis structure (retained-bounded).

**Historical / contextual citation only (NOT load-bearing):**

- [`LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md`](LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md)
  is cited only as the historical predecessor that first articulated
  the block-identification statement in the LHCM family. Its effective
  status is `decoration_under_graph_first_su3_integration_note`. The
  proof-walk above does NOT consume any content from this note; all
  load-bearing inputs come from `graph_first_su3_integration_note` or
  standard mathematical fact.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This note does not close:

- the Sym² and Anti² block multiplicities themselves (these are
  established by the retained-bounded graph-first integration note,
  not derived again here);
- the SM-definition label `quark` for the SU(3)-charged Weyl fermion
  (this is a labelling convention, not a derivation, and is the
  remaining residual identified by the LHCM repair atlas);
- the SM-definition label `lepton` for the SU(3)-singlet Weyl fermion
  (same as above);
- specific eigenvalues `+1/3` and `−1` on the LH-doublet sector
  (a normalization choice that is the LHCM Y-normalization repair
  item (2), out of scope for the block-identification claim);
- identification with Standard Model hypercharge `Y` (out of scope);
- the charge formula `Q = T_3 + Y/2` (out of scope);
- any anomaly-cancellation result;
- the staggered-Dirac realization gate;
- derivation of the chiral matter content itself;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values;
- any follow-on proof-walk for other algebraic bookkeeping notes;
- any parent theorem/status promotion.

The matter-assignment note's `positive_theorem` author hint is not
changed: this proof-walk is itself a `bounded_theorem` and does not
propose a tier promotion for the cited matter-assignment note. The
audit lane's verdict on the cited matter-assignment note is the
authority for that note's classification; this proof-walk only
demonstrates that the load-bearing chain for the
block-identification step does not consume staggered-Dirac
realization machinery.

## 2026-05-18 audit-conditional repair: restated proof-walk with graph_first_su3_integration as sole retained parent

Per the 2026-05-17 audit verdict (`dependency_not_retained`), the LHCM
matter-assignment parent is itself audited_conditional and cannot
load-bear this bounded claim. This revision restates the proof-walk
using `graph_first_su3_integration_note` as the sole retained parent.
The LHCM reference is preserved as historical/contextual citation only,
not load-bearing.

Concretely:

- The **Claim** section now identifies `graph_first_su3_integration_note`
  as the sole retained parent and removes the framing of this proof-
  walk as "from [LHCM matter-assignment note]". The block-identification
  result is asserted directly on top of the retained graph-first
  integration.
- The **Proof-Walk** section's six-step chain has every load-bearing
  citation re-anchored at `graph_first_su3_integration_note` (Steps 1-3)
  or at standard mathematical fact (Steps 4-6). The dependency table is
  reheaded as "Step ↦ Load-bearing input" and explicitly drops the
  earlier "Step in the cited matter-assignment note" framing. An
  explicit closing paragraph states that no load-bearing input is the
  audited_conditional matter-assignment parent.
- The **Why the load-bearing chain does not consume the realization
  gate** section has the LHCM-parent contextualization stripped of any
  load-bearing role. The chain stands on the retained graph-first
  integration alone.
- The **Dependencies** section is restructured into (a) Sole retained
  parent (load-bearing): `graph_first_su3_integration_note`; (b)
  Supporting retained parent: `graph_first_selector_derivation_note`;
  (c) Historical / contextual citation only (NOT load-bearing):
  `LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02`,
  with effective_status `decoration_under_graph_first_su3_integration_note`
  noted explicitly.

The algebraic content of the proof-walk (the τ eigendecomposition giving
3⊕1, SU(3)-on-3-dim-non-trivial-irrep ↦ fundamental, SU(3)-on-1-dim-irrep
↦ trivial, and the (2,3) ⊕ (2,1) tensor decomposition) is unchanged.
The runner script is unchanged. Only the load-bearing dependency
architecture is restated to remove the audited_conditional parent from
the chain of authority.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_lhcm_matter_assignment_block_proof_walk_lattice_independence.py
```

Expected:

```text
TOTAL: PASS=N FAIL=0
VERDICT: bounded proof-walk passes; LHCM matter-assignment Sym²↔Q_L,
Anti²↔L_L block identification uses no lattice-action or staggered-
Dirac realization quantity as a load-bearing input.
```

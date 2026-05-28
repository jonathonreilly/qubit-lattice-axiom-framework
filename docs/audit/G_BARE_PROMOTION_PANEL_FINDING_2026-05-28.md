# g_bare Cluster Promotion Panel Finding — 2026-05-28

**Claim type:** meta
**Status:** read-only audit-strategy finding. This file is NOT an audit
verdict, does NOT retag the ledger, is NOT part of the audit citation graph,
and does NOT propagate retained-grade to any row. All claim references below
are plain text (not markdown links) and are therefore non-load-bearing.
**Propagates retained-grade:** no
**Proposes new claims:** no
**Lane:** audit-strategy / promotion triage.

## Purpose

A targeted multi-pronged review was run to decide whether the high-leverage
`g_bare` normalization cluster — ~9 critical rows at ~890–931 transitive
descendants each, all currently `audited_clean / retained_bounded` — can be
re-audited from `bounded_theorem` to `positive_theorem`, i.e. moved onto the
full (unbounded) `retained` surface, **without adding any new framework
axiom**.

This file records the finding so the audit lane does not spend fresh-context
audit cycles attempting a promotion that the review shows is not currently
available, and so the promotion effort can be redirected to rows that can in
fact move (see the companion dispatcher queue
`BOUNDED_TO_RETAINED_REAUDIT_QUEUE_2026-05-28`).

## The promotion question

The cluster argues `g_bare = 1` (bare lattice gauge coupling) via two routes
that both reduce to elementary algebra:

- Wilson matching: `beta * g_bare^2 = 2 N_c` with `N_c = 3`, `beta = 6`.
- Ward / two-representation 1PI route: `F^2 = c0` (constant in `g`) and
  `F^2 = g^2 / (2 N_c)`, hence `g^2 = 2 N_c c0`; at `c0 = 1/6`, `N_c = 3`
  this gives `g^2 = 1`.

The **pure-algebra skeleton of both routes is already fully `retained`** as
two standalone abstract narrow theorems:
`g_bare_constraint_vs_convention_restatement_abstract_identity_narrow_theorem_note_2026-05-10`
(the `beta * g^2 = K` admission-rank disambiguation) and
`g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note_2026-05-10`
(the `g^2 = 2 N c0` simultaneous-constraint forcing identity). The promotion
question is therefore **not** about the algebra. It is:

> Is the trace / generator normalization `N_F = 1/2`
> (canonical Gell-Mann `Tr(T_a T_b) = (1/2) delta_ab`), on which the
> physical pinning of `g_bare = 1` depends, **forced** by the framework
> axioms (A1: per-site qubit / Cl(3,0); A2: Z^3 lattice), or is it a free
> **convention**?

If `N_F = 1/2` is forced, the cluster promotes. If it is a free convention,
the cluster is correctly `retained_bounded` and must stay there.

## Method

Four independent read-only prongs, none of which edited any file:

1. **Assumptions exercise** — full enumeration and classification of every
   assumption in the `g_bare = 1` chain across the cluster source notes.
2. **First-principles exercise** — attempt to derive `N_F` from A1 + A2 plus
   the Cl(3) per-site structure alone.
3. **Literature search** — how lattice gauge theory / QFT treat the bare
   coupling and generator normalization.
4. **Mathematics search** — whether a concrete Cl(3) -> matrix embedding
   fixes the su(3) generator normalization absolutely or only up to scale.

## Finding 1 — assumption ledger (condensed)

| layer | content | classification |
|---|---|---|
| A1 | per-site qubit, Cl(3,0) ~ M_2(C) | AXIOM |
| A2 | Z^3 spatial lattice | AXIOM |
| L1 | Cl(3) -> End(V) embedding canonical up to finite outer automorphism | DERIVED (retained-grade) |
| L2 | the invariant trace form on su(3) is unique **up to one positive scalar** (Killing rigidity on simple su(3)) | DERIVED (retained-grade) |
| — | `N_c = 3` from `dim(Z^3) = 3` | DERIVED (retained-grade) |
| **L3** | **the overall scalar `N_F` (value 1/2)** | **CONVENTION — the single load-bearing admission** |
| L4 | `g_bare = 1` (and `beta = 6`) given L3 + Wilson matching | DERIVED *conditional on L3* |
| bridge | Wilson plaquette action form; continuum `(1/g^2)F^2` matching; H_unit-residue 1PI exhaustion | ADMITTED-BRIDGE |

The chain has exactly one load-bearing free scalar: the L3 normalization
`N_F`. Every "rigidity" result in the cluster operates **at fixed `N_F`**;
none derives the value of `N_F` itself.

## Finding 2 — the single blocking convention is `N_F = 1/2`

L2 (Killing rigidity) fixes the invariant form on simple su(3) only **up to
a positive scalar**, and `N_F` *is* that scalar. The framework's own
four-layer restatement note
(`g_bare_constraint_vs_convention_restatement_note_2026-05-07`) already
stratifies the argument this way and places `N_F = 1/2` at L3 as the single
admitted convention; the most recent bridge note
(`cl3_normalization_i3_accepted_premise_bridge_bounded_note_2026-05-27`)
explicitly registers `Tr(T_a T_b) = delta/2` as an **accepted premise (P1)**
and states it does not derive P1 from the one-qubit operator algebra on the
Z^3 substrate. The blocking convention is therefore already acknowledged
inside the cluster; this finding confirms it is irreducible under A1 + A2.

## Finding 3 — the 2026-05-17 L3 notes are invariance, not uniqueness

The four recent L3 / rigidity notes do **not** close the convention:

- `g_bare_l3a_trace_surface_invariance_narrow_theorem_note_2026-05-17`:
  the binary trace-surface choice {V_3, V} is **inert** for `g_bare`.
  Explicitly "does not close the L3a admission."
- `g_bare_l3b_overall_scalar_invariance_narrow_theorem_note_2026-05-17`:
  the continuous orbit `N_F in R_{>0}` is **inert** for `g_bare`
  (`d(g_bare^2)/d N_F = 0`). Explicitly "does NOT close the L3b admission."
- `g_bare_rigidity_canonical_normalization_algebra_narrow_theorem_note_2026-05-17`:
  at **fixed** `N_F = 1/2`, uniform dilation `T_a -> lambda T_a` is
  forbidden because it breaks the already-chosen Gram and Casimir. This
  presupposes the canonical pair it appears to protect.
- `g_bare_c_iso_convention_orbit_invariance_narrow_theorem_note_2026-05-17`:
  the lattice anisotropy `xi = a_s/a_tau` is **inert** for `g_bare`
  (orthogonal degree of freedom).

These are robustness/invariance theorems: they show `g_bare = 1` is
insensitive to three different convention degrees of freedom. They do not
show that any of those degrees of freedom is itself structurally forced.
That is the gap between `retained_bounded` and `retained`.

## Finding 4 — first-principles: the intrinsic scale exists only on the per-site sector

The strongest "forced" route is **not** Killing rigidity (which leaves the
scalar free) but the **per-site spin double cover**: on the per-site
Cl(3,0) ~ M_2(C), the bivectors give `T_a^site = sigma_a/2`, and the
Spin(3) -> SO(3) double cover (`R(2 pi) = -I`) fixes the factor `1/2` with
no continuous freedom — a genuine discrete/topological constraint. This is a
real intrinsic normalization, **but only on the per-site SU(2)**.

The gauge su(3) lives on `V_3 = C^3`, the symmetric base of the taste cube —
a downstream lattice construction, not the per-site C^2. Propagating the
per-site `1/2` to the su(3) on `V_3` requires the **bridge premise** that the
per-site Cl(3)-bivector SU(2) and the SU(2) sub-blocks of su(3) on `V_3`
carry the *same induced scale*. "Abstractly isomorphic" does not imply "same
induced scale," and the scale is exactly what is contested. Closing this is
gated on the still-open **staggered-Dirac realization gate** (former A3)
canonicalizing `V_3` as *the* physical trace surface; A1 + A2 alone do not
single out the matter content that would do so.

## Finding 5 — literature and mathematics corroborate "convention" (non-load-bearing context)

The following external context is recorded as **non-load-bearing**: it is
not consumed as a proof input, numerical comparator, or admitted convention
for any retained claim. It is methodological corroboration only.

- Lattice gauge theory treats the bare coupling `g_0` (via `beta = 2N_c/g_0^2`)
  as a tuned input parameter, not a derived number; the continuum limit is
  `g_0 -> 0`. (Standard Wilson-action references.)
- The generator normalization `Tr(T_a T_b) = (1/2) delta_ab` is the
  conventional Dynkin-index choice `T_F = 1/2`; rescaling `T_a -> lambda T_a`
  is always available.
- The field redefinition `A_mu -> A_mu/g` moves the coupling between the
  covariant derivative and the kinetic prefactor `1/g^2`; "`g_bare = 1`" is a
  units/normalization statement, not a basis-independent one. Only the
  *renormalized* coupling at a physical scale is convention-independent.
- On a simple Lie algebra the invariant bilinear form is unique only up to
  overall scale; a representation trace fixes the scale **relative to the
  chosen matrices**. A Clifford embedding supplies a representation, hence a
  scale-fixed form *relative to itself* — it does not single out a canonical
  scale on the abstract algebra. The "intrinsic Hilbert-Schmidt removes the
  scale" move is circular: the matrices were written with an implicit scale,
  and `Tr(T_a T_b)` reports that pre-chosen scale rather than deriving it.

## Verdict

**Do NOT promote the `g_bare` cluster to `positive_theorem` / full
`retained` at this time.** The unconditional statement "`g_bare = 1` from
A1 + A2" is not available: `N_F` is a genuine free convention under A1 + A2,
formally certified inert (not forced) by the framework's own L3b invariance
theorem. The cluster's `retained_bounded` status is correct.

What is already correctly retained:

- The **conditional** algebraic core — "given `N_F = 1/2`, `g_bare = 1`,
  `beta = 6`" — is captured at full `retained` grade by the two abstract
  narrow theorems named above. No further promotion is needed there.

## Closure gate (what would change this verdict)

The only non-circular route to forcing `N_F` is to make the per-site
spin-double-cover normalization propagate to the gauge su(3) **by derivation
rather than by the bridge admission**. That requires the staggered-Dirac
realization gate to first canonicalize `V_3` as the physical trace surface,
after which the intrinsic per-site `T = sigma/2` would propagate to
`N_F = 1/2` by Killing rigidity with no remaining freedom. Until that gate
closes, `N_F = 1/2` is irreducibly an admitted convention.

## Audit-lane recommendation

1. Leave the `g_bare` cluster at `retained_bounded`; do not queue it for
   bounded->positive re-audit.
2. If desired, the cluster source notes may add `N_F = 1/2` to an explicit
   `admitted_context_inputs` field to make the single convention maximally
   legible to a fresh-context auditor — a documentation move, not a
   promotion.
3. Redirect promotion effort to the genuinely-unblocked exact-algebra /
   finite-construction rows in `BOUNDED_TO_RETAINED_REAUDIT_QUEUE_2026-05-28`.

## What this finding does NOT claim

- Does **not** retag any ledger row or set any audit verdict.
- Does **not** assert `g_bare = 1` is false; it is true conditional on the
  named convention.
- Does **not** introduce any new axiom, numerical comparator, or admitted
  convention into any retained claim.
- Does **not** close or reopen the staggered-Dirac realization gate.

## Forbidden imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed as proof inputs (Finding 5 is
  explicitly non-load-bearing methodological context).
- No fitted selectors.
- No same-surface family arguments.
- All claim references are plain text, creating no citation-graph edges.

## Cross-references (non-load-bearing, plain text)

- Cluster source notes: `G_BARE_DERIVATION_NOTE`,
  `G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03`,
  `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03`,
  `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18`,
  `G_BARE_TWO_WARD_CLOSURE_NOTE_2026-04-18`,
  `G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19`,
  `G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19`,
  `G_BARE_RIGIDITY_THEOREM_NOTE`,
  `G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-05-09`,
  `G_BARE_HILBERT_SCHMIDT_RIGIDITY_THEOREM_NOTE_2026-05-07`.
- Already-retained conditional cores:
  `G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_ABSTRACT_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`,
  `G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10`.
- L3 invariance notes (2026-05-17): `G_BARE_L3A_TRACE_SURFACE_INVARIANCE...`,
  `G_BARE_L3B_OVERALL_SCALAR_INVARIANCE...`,
  `G_BARE_RIGIDITY_CANONICAL_NORMALIZATION_ALGEBRA...`,
  `G_BARE_C_ISO_CONVENTION_ORBIT_INVARIANCE...`.
- Accepted-premise bridge: `CL3_NORMALIZATION_I3_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-27`.
- Companion dispatcher queue: `docs/audit/BOUNDED_TO_RETAINED_REAUDIT_QUEUE_2026-05-28.md`.

# Axiom Minimality Policy

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** binding rule for the audit lane through completion of the full
repo audit.

`A_min` is fixed for this audit: `Cl(3)` on `Z^3`, finite Grassmann /
staggered-Dirac partition, and canonical `g_bare = 1` plaquette
normalization. Lane closure must close from `A_min` by derivation,
identification, bounded composition, or no-go boundary, not by amending it.

## 1. Disallowed moves
- Adding `Axiom*` or an equivalent primitive, including a `Cl_4(C)`
  carrier on `P_A H_cell` or any irreducible module structure presented
  as a new axiom.
- Rewording an existing `A_min` axiom to be more permissive or more
  restrictive to close a lane, including PR #113's axiom-3 reading question.
- Framing a result as "if we just accept X as primitive, lane Y closes"
  without recording X as an unmade science-level decision.

## 2. Allowed moves
- Identifying structures already present in `A_min` with Standard Model
  constructs. These are support-tier unless audited as class C; class E/F
  load-bearing identifications record `audited_renaming`.
- First-principles derivations from `A_min` that close without additional
  assumptions; these are the retained-tier path after class C audit.
- Bounded compositions with explicit named residuals.
- No-go boundary notes that state what is structurally unclosable from
  the current axiom set.

## 3. Precedents
- PR #186 / PR #196: `Axiom*` (`Cl_4(C)` on `P_A H_cell`) was declined as a
  forced extension; the proposed minimality theorem audit-failed at O2.
- PR #113: the axiom-3 permissive-reading amendment is declined. The
  work lands only as bounded no-go inventory for `(C2-X)` and its attack
  frames.

## 4. Workflow
If a physics-loop or science worker reaches "we need an extra axiom to close
this", the correct action is:
1. Land the work as a bounded no-go boundary note documenting what would
   close under the proposed axiom.
2. Record the proposed axiom as an explicit science-level decision
   waiting on human input.
3. Move to a different lane or a different attack frame.
Do not add the axiom and proceed.

## 5. Scope
This policy applies until the full repo audit is complete. After the audit,
axiom extension may be revisited as a separate decision. Until then, `A_min`
is fixed.

## 6. Recorded primitive decisions (owner science-level decisions)
Per §1 (third bullet) and §4, accepting a specific primitive is permitted when
it is recorded here as an explicit owner science-level decision. The framework
owner sets the minimality norm and may make such a decision. Recorded:

- **2026-05-30 — scale-reference primitive (the units import).** The single
  dimensionful scale reference `a^{-1}` is accepted as a framework primitive,
  registered in `docs/audit/data/axiom_premise_nodes.json` as
  `scale_reference_primitive` (source `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`).
  - **Why it is admissible and not a carve-out for laundering.** It is a units
    conversion, not a physics axiom. A dimensionful scale is irreducible by
    dimensional analysis: `A_min = Cl(3)` on `Z^3` carries zero dimensionful
    content, so exactly one dimensionful number must be supplied to fix the
    unit. The declaration contains **no dimensionless content**, so the
    axiom-premise carve-out cannot launder any dimensionless result — no mass
    ratio, coupling, or mixing angle can be derived by citing a pure unit
    declaration. `check_axiom_premise_clean.py` enforces that the doc stays
    pure.
  - **Scope.** This decision is narrow. It does **not** amend `A_min` (A1/A2
    unchanged), does **not** reopen the A1/A2 minimality audit, and does **not**
    assert `a/l_P = 1` — the self-consistency that the natural unit equals the
    Planck length remains the separate open gravity derivation. The general
    "`A_min` is fixed" rule of §5 is unchanged for all physics content; this
    records only the one units-conversion primitive.

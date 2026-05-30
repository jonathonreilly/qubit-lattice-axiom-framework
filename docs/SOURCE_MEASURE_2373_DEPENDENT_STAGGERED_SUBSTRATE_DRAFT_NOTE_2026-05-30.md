# Source-Measure Dependent Staggered / Substrate Draft Note

Status: draft-dependent impact map.  This note does not promote staggered
Dirac, substrate-realization, Grassmann, JW, or determinant rows.

Dependency: this draft may exit draft only if the source-measure
record-intervention line in PR #2373 receives a positive audit.  Even then,
the expected impact is support-only unless a row's only blocker is
source/readout semantics.

## Target Surface

The target surface is the small staggered/substrate subset where P1/P-cal or
source/measure wording appears.  The current inventory marks roughly one row as
a possible support candidate.

Most staggered/substrate rows are blocked by realization gates: Grassmann
forcing, Jordan-Wigner realization, determinant construction, boundary
conditions, or action selection.  Those are not addressed by PR #2373.

## Conditional Movement

If PR #2373 audits clean, it can support staggered rows only at the point where
a finite record-facing source/readout intervention is needed.  It does not
derive the staggered action or fermion determinant.

## Review Checklist

- Confirm whether the row's blocker is source/readout semantics or a staggered
  realization gate.
- Keep Grassmann/JW/determinant/action-selection blockers open.
- Confirm no substrate realization is inferred from source-measure closure.
- Use PR #2373 as support only unless the row-level audit identifies no other
  blocker.

## Non-Claims

This draft does not derive the staggered Dirac operator, Grassmann statistics,
Jordan-Wigner realization, determinant measure, Wilson action, or substrate
realization.  It only records a possible source/readout support dependency.

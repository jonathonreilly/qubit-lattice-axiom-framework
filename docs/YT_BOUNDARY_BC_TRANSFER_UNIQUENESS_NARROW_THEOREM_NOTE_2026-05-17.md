# yt Boundary BC-Transfer Finite-Grid Diagnostic (Backward-RGE)

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status:** conditional finite-grid implementation diagnostic only; not a
continuum uniqueness theorem, physical BC-transfer theorem, or parent
`yt_boundary_theorem` closure.
**Claim scope:** the standalone finite-grid numerical diagnostic that the
runner's backward-RGE map `y_t(v) -> y_t(M_Pl)` is finite on the sampled
trajectories, increasing on the runner's 33-point `X` grid, has finite
observed grid slopes, and gives stable bracketed `brentq` roots for the
runner's supplied Ward boundary target
`y_t(M_Pl) = g_lattice / sqrt(6) = 0.43577` near
`y_t(v) = X* = 0.97267 +/- 1e-10`, all conditional on the runner's
declared implementation inputs.

The scan interval `[0.5, 1.2]` is chosen physically: it is strictly below
the SM-EFT Yukawa Landau-pole-like onset, which the runner locates
empirically near `X ~ 1.28`. Within `[0.5, 1.2]` the map `Phi` stays
bounded; the trajectory `y_t(t)` does NOT exceed its initial value within
~3% across the working grid (no upward amplification on the segment, because
the asymptotically-free `-8 g_3^2` and EW gauge terms balance the
self-coupling `9/2 y_t^2` in this regime).

This is a numerical narrow well-definedness theorem about the **mathematical
device** asserted in claim (iv) of `YT_BOUNDARY_THEOREM.md`. It does NOT
re-derive Options A / B / C in the parent and it does NOT claim that the SM
EFT is physical at `M_Pl`. It establishes the strictly weaker but
prerequisite fact that the backward-extrapolation root-finder used to
implement Option A in `frontier_yt_boundary_consistency.py` is reproducible
and stable on the declared finite grid. It does not assert continuum
unique-root closure.

**Status authority:** independent audit lane only.

**Primary runner:** [`scripts/frontier_yt_boundary_bc_transfer_uniqueness.py`](../scripts/frontier_yt_boundary_bc_transfer_uniqueness.py)
**Cache:** [`logs/runner-cache/frontier_yt_boundary_bc_transfer_uniqueness.txt`](../logs/runner-cache/frontier_yt_boundary_bc_transfer_uniqueness.txt)

## 2026-06-20 Source-Boundary Repair (conditional finite-grid diagnostic; inputs I1-I5 admitted)

Prior boundary review named two possible paths:

> *"missing_dependency_edge: add direct retained-grade dependency edges or
> self-contained derivations for I1-I5; otherwise leave the row as a
> conditional finite-grid diagnostic."*

This repair takes the named alternative: the row is **left/narrowed as a
conditional finite-grid diagnostic**. No retained-grade dependency edges or
self-contained derivations for `I1`–`I5` are added.

Explicitly:

- The implementation inputs `I1`–`I5` (canonical plaquette constants, the Ward
  boundary target, the two-loop SM RGE coefficients/threshold procedure, the
  fixed threshold scales, and the EW initial-condition surface) are **supplied/
  admitted inputs**. None of them is retained-grade for this row and none is
  self-contained-derived here.
- Consequently the row's result is a **finite-grid numerical diagnostic
  conditional on `I1`–`I5`**, not a retained-grade theorem. The verified
  quantities (sampled globalness, 33-point grid monotonicity, finite observed
  slopes, bracketed `brentq` root stability, extension-scan onset) hold only
  on the runner's finite sample under the admitted inputs.
- The row asserts no retained-grade physical boundary-transfer theorem, no
  continuum monotonicity, no exact continuum uniqueness, no physical validity
  of the SM EFT at `M_Pl`, and no closure of the parent `yt_boundary_theorem`.

No derived value, axiom, import, comparator, or retained bridge is introduced
by this repair, and no downstream status, ledger tag, or publication status is set
here. Status authority remains the independent audit lane only.

## 2026-06-18 Conditional-Status Firewall

This row takes the source-boundary fallback path: it is a conditional finite-grid
implementation diagnostic over the declared runner inputs only. Its source
status is not theorem-grade physical boundary transfer.

The citable claim is restricted to the runner's finite sampled trajectories,
33-point finite-grid monotonicity check, finite observed slopes, bracketed
root stability checks, and extension scan under the declared implementation
inputs. It does not derive the Ward target, canonical plaquette constants,
SM RGE normalization, threshold seeds, or EW initial-condition surface from
framework primitives. It does not prove continuum monotonicity, exact
continuum uniqueness, physical validity of the SM EFT at `M_Pl`, or closure
of the parent YT boundary theorem.

No new axiom, retained bridge, downstream status, ledger tag, or publication
status is introduced by this firewall.

## 2026-06-07 Implementation-Input Boundary Retargeting

The direct claim is a bounded finite-grid diagnostic over the runner's explicit
implementation inputs. The canonical plaquette constants, Ward target, two-loop
SM RGE normalization, threshold scales, and EW initial conditions are not
load-bearing retained proof authorities for this row. They are visible
declared implementation inputs to the finite diagnostic.

The row therefore asks only whether the registered runner performs the stated
finite checks on the stated grid and brackets:

- finite trajectories on the sampled interval;
- positive forward differences on the 33-point grid;
- finite observed grid slopes;
- stable `brentq` root agreement across the declared brackets;
- extension-scan location of the blow-up-like onset above the working interval.

It does not claim continuum monotonicity, exact continuum uniqueness, physical
validity of the SM EFT at `M_Pl`, a lattice Ward theorem, or a parent
`yt_boundary_theorem` closure.

## 2026-05-28 Source-Boundary Repair (narrow to runner-verified measurement)

Prior review found that the source elevated grid monotonicity plus `brentq`
checks to continuum strict monotonicity and exact uniqueness on the whole
interval, while also importing canonical plaquette/coupling-surface inputs.
The source-boundary repair is to narrow this row to the completed finite-grid
numerical diagnostic under explicit imported-input assumptions unless a
retained interval/validated-numerics proof plus retained canonical
plaquette/coupling-surface and Ward-identity authorities are supplied.

This revision narrows the claim to exactly what the runner proves:

- **Load-bearing (in scope):** The finite-grid numerical diagnostic: strict monotonicity verified on a 33-point grid by positive forward differences, brentq root agreement across three subintervals to 1e-10, Lipschitz bound L_observed < 10 on the working grid, and empirical Yukawa-Landau onset located at X_pole ~ 1.275 — all under the explicit imported-input assumptions (I1)–(I5), with the canonical plaquette surface and Ward-identity target treated as visible implementation inputs rather than retained proof authorities for this row.
- **NON-load-bearing (non-binding interpretation):** Continuum strict monotonicity (that Phi is strictly monotone on the whole interval [0.5, 1.2] as a continuous mathematical fact, not just on the 33-point sample grid) and exact uniqueness (that no root exists outside the scanned interval). These elevate the grid check to a continuum statement that the finite runner evidence does not prove. Marked as non-binding interpretation unless a retained interval/validated-numerics proof authority is supplied.

No new axiom, import, or retained bridge is introduced. Only the exact finite
measurement is load-bearing; the broader mechanism reading is explicitly
non-binding.

## Authority role

The 2026-05-27 review recorded that the previous packet overstated two things:

- it elevated finite-grid monotonicity plus `brentq` checks to exact continuum strict monotonicity and exactly one root on the whole interval;
- it treated imported canonical plaquette/coupling values and the Ward boundary target as retained physical BC-transfer authority beyond the reviewed scopes of the cited rows.

This repair keeps the useful science and removes the overclaim. The row is now a bounded finite-grid numerical diagnostic for the coded 5-channel two-loop SM RGE setup. It is explicitly conditional on imported implementation constants and on the Ward target used by the runner. It does not assert a retained physical boundary-transfer theorem.

## Bounded Claim

For the runner implementation in `scripts/frontier_yt_boundary_bc_transfer_uniqueness.py`, define

```text
Phi(X) := y_t(M_Pl)
```

by integrating the coded `(g1, g2, g3, y_t, lambda)` two-loop SM RGE from `t_v = ln(v_derived)` to `t_Pl = ln(M_Pl)` with initial condition `y_t(v) = X`.

On the sampled interval `X in [0.5, 1.2]`, using the runner's imported constants from `scripts/canonical_plaquette_surface.py` and the runner's Ward target

```text
WARD_TARGET = g_lattice / sqrt(6),
```

the companion runner verifies the following finite diagnostics:

```text
(T1) sampled globalness: every sampled trajectory is finite on the integration segment.
(T2) finite-grid monotonicity: Phi is increasing on the 33-point X grid used by the runner.
(T3) finite-difference Lipschitz diagnostics: observed grid slopes are finite and bounded by the declared numerical thresholds.
(T4) bracketed root stability: brentq finds the same root near X = 0.97267 on the full interval and on three sign-changing subintervals.
(T5) extension-scan boundary: the sampled extension to X in [1.20, 1.30] shows a Yukawa-Landau-like onset above the working scan interval.
```

This is the whole source-side claim. The branch intentionally does not promote `(T2)` to continuum strict monotonicity and does not promote `(T4)` to exact uniqueness for all real `X` in `[0.5, 1.2]`.

## Imported Inputs

The following are declared/admitted implementation inputs for this bounded
diagnostic. None of `I1`–`I5` carries a retained-grade dependency edge and
none is self-contained-derived here; they are supplied inputs, and every
diagnostic below is conditional on them. They are not retained proof
authorities supplied by this note:

- **I1:** `CANONICAL_PLAQUETTE`, `CANONICAL_U0`, `CANONICAL_ALPHA_BARE`,
  `CANONICAL_ALPHA_LM`, and `CANONICAL_ALPHA_S_V` from
  `scripts/canonical_plaquette_surface.py`.
- **I2:** `WARD_TARGET = g_lattice / sqrt(6)` as the target boundary value
  used by the runner.
- **I3:** the two-loop SM RGE coefficients and threshold procedure copied
  into the runner from the existing YT consistency implementation.
- **I4:** the fixed threshold scales used by the runner (`M_T_POLE`,
  `M_B_MSBAR`, `M_C_MSBAR`) as numerical RGE seeds, not fitted proof
  targets.
- **I5:** the EW initial-condition constants at `M_Z` (`ALPHA_EM_MZ`,
  `SIN2_TW_MZ`) and derived initial `g1(v), g2(v)` surface.

No PDG observable is used as a fitted target or comparator. The threshold and
EW numerical values are declared implementation inputs for the coded
diagnostic, and the checks evaluate only that diagnostic.

## What This Row Does Not Claim

- It does not prove continuum strict monotonicity of `Phi` on every point of `[0.5, 1.2]`.
- It does not prove an exact unique root theorem on the continuum interval.
- It does not prove that the SM EFT is physical at `M_Pl`.
- It does not prove that the lattice Ward identity holds in the SM.
- It does not prove or import retained canonical plaquette/coupling-surface authority for the numerical constants used by the runner.
- It does not close the parent `yt_boundary_theorem` row.

## Runner Evidence

The runner performs 31 pass/fail checks:

- setup and imported-input consistency checks;
- finite trajectory checks on a coarse `X` grid;
- finite-grid monotonicity checks on a 33-point `X` grid;
- finite-difference slope / Lipschitz diagnostics;
- `brentq` root agreement across the full interval and three sign-changing subintervals;
- extension scan locating a blow-up-like onset above the working interval;
- root stability under multiple integrator `max_step` choices.

Expected result:

```text
Counts: 31 PASS, 0 FAIL
```

## Source Graph Hygiene

This repaired note intentionally has no markdown links to source-note authority rows for the imported plaquette or Ward values. The constants remain visible as imported implementation inputs, and the Python helper import remains visible through the registered runner path. Independent review can decide whether this bounded finite-grid diagnostic is useful, but the source graph should not treat upstream YT/plaquette rows as load-bearing retained authorities for a stronger theorem.

## Cross-References

Non-load-bearing context only:

- `docs/YT_BOUNDARY_THEOREM.md`
- `docs/YT_ZERO_IMPORT_AUTHORITY_NOTE.md`
- `scripts/frontier_yt_boundary_consistency.py`

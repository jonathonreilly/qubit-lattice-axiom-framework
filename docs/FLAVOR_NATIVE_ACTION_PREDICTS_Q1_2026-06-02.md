# Flavor — five finite spectral-action cutoffs do not select r=1/2

**Date:** 2026-06-02
**Type:** open_gate
**Claim type:** open_gate
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not set, predict, or edit any audit outcome.
**Primary runner:** [`scripts/flavor_native_action_predicts_q1_2026_06_02.py`](../scripts/flavor_native_action_predicts_q1_2026_06_02.py)
**Runner cache:** [`logs/runner-cache/flavor_native_action_predicts_q1_2026_06_02.txt`](../logs/runner-cache/flavor_native_action_predicts_q1_2026_06_02.txt)
**No-promotion statement:** This source note creates no promotion, no registry
edit, no audit verdict, and no downstream status change; status remains owned
by the independent audit lane.

## 2026-06-06 finite-scan scope repair

The 2026-06-06 repair narrows the load-bearing scope to what the runner
actually checks:

- the `C_3` ansatz `H = aI + b(C+C^2)`;
- the Hilbert-Schmidt block norms and equal-block `r=1/2` identity;
- the five displayed cutoff scans at the runner's explicit normalization
  (`a=1`, `b/a in [0,2]`, cutoff argument `lambda_i^2`);
- the spectrum and `Q=1` value at the finite-scan maximum near `b/a=1`;
- Hilbert-Schmidt orthogonality of the mass and hopping grades.

This note does **not** claim a theorem for arbitrary monotone cutoffs, a
Casimir/HK Brownian-time range theorem, or a Wilson/HK/Manton
action-form-degeneracy theorem. Those remain separate bridge obligations.

## Question
Does the framework's candidate **native** action (heat-kernel / Casimir / Connes spectral action,
where the Wilson term is only an admitted import) geometrically fix the charged-lepton mass:kinetic
weighting at `r=1/2` (`|b|/a = 1/√2`), or does it give the dimension default `r=1`, or leave it free?

## Result — the five tested cutoffs peak near r=1; none selects r=1/2
For `H = aI + b(C+C²)` (δ=0; Q is δ-independent), eigenvalues `{a+2b, a−b, a−b}`:

- For the five displayed cutoffs, the finite scan of
  `S(b) = Σ f(λᵢ²)` over `a=1` and `b/a in [0,2]` has its maximum at **|b|/a ≈ 1 (r=1)**:
  `exp(−x):1.00, exp(−x²):1.00, (1+x)⁻²:1.00, (1+x)⁻⁴:1.00,
  (1+x)⁻⁸:1.00` — **never near the target 1/√2 = 0.707**. At `b/a=1` the spectrum is `[0,0,3a]` (the
  doublet eigenvalue collapses to zero, where any decaying `f` peaks); this is the `r=1`,
  dimension/Plancherel point, `Q=1`. This is a finite cutoff-scan statement, not a theorem about every
  monotone cutoff or every native action.

## Orthogonality of the tested grades

The runner also checks that the on-site (`I`) and hopping (`C+C^2`) grades are
Hilbert-Schmidt orthogonal (`<mass,hop>_HS = 0`). Therefore a single quadratic
Hilbert-Schmidt norm on this two-grade ansatz does not by itself relate the two
amplitudes. This is the only action-form statement carried here; any
Wilson/HK/Manton degeneracy bridge is out of scope for this row.

## Consequence
The five tested finite spectral-action cutoffs do **not** supply `r=1/2`.
`r=1/2` is the equal-block Hilbert-Schmidt partition `3a^2 = 6b^2`, not a
maximum of the tested cutoff scans. This row does not claim a framework-native
action-sector prediction for all admissible actions.

## 2026-06-13 Downstream Boundary Alignment

The later occupancy-independence theorem
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
turns the residual named here into a single explicit atom: the doublet
occupancy/slot-degree rule. This action-axis row therefore should not be read
as a separate open search for "some native action" in general. Its safe use is
narrower:

- the five tested finite action cutoffs land on the dimension/sector-side
  `r = 1` horn;
- the equal-block `r = 1/2` horn remains the separate occupancy rule;
- the Record axiom explicitly declines to supply weighting/occupancy; and
- the downstream theorem exhibits both sector and orbit occupancy models as
  consistent with the checked current surface.

This update adds runner checks for that downstream boundary. It does not adopt
orbit occupancy, does not add an action principle, and does not edit audit
status.

## Dependencies

- [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
  (downstream occupancy/slot-degree boundary; bounded support).
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (Record axiom boundary and scope reference).

## The next paths this opens (not closing)
- The residual is one object — the trace/dimension (→ Q=1) vs sector/block-count (→ Q=2/3) weighting
  of the two C₃ isotypes. Whether any native principle (positivity, entropy, modular/KMS, records)
  selects block-count over dimension is the live question.
- The readout-class axis (signed Brannen vs singular-value Yukawa) is independent of the action axis
  and remains open.

## No-Go Discipline Gate

This gate is restricted to one route statement: the heat-kernel / spectral-action
axis tested here does not force the Koide `r=1/2` value.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Spectral-action extremum | Use the five displayed cutoff scans to choose `r`. | Finite-scan maxima land near `r=1`, not `r=1/2`. |
| Casimir / heat-kernel time | Use Brownian time to tune the ratio. | Out of scope here; needs a separate theorem/runner. |
| Equal-block Hilbert-Schmidt partition | Use equal sector power. | Gives `r=1/2`, but that is the extra block-count reading, not action stationarity. |
| Action-form degeneracy | Break Wilson / heat-kernel / Manton degeneracy. | Out of scope here; this row only checks HS orthogonality of `I` and `C+C^2`. |
| Orthogonality route | Couple mass and hopping through one norm. | Hilbert-Schmidt cross term is zero, so one norm cannot fix the ratio. |
| Future action principle | Add a new native variational rule. | Open, but not supplied by this action axis. |

### N2 - Wall Independence

The collapsed residual is the sector-weighting rule. Action stationarity and
block-count weighting are independent gates.

### N3 - Hidden-Wall Scan

"Native action" in this repaired row means only the five listed cutoff functions
checked by the runner. The note does not generalize to every possible future
action principle or to unproved Casimir/HK/Wilson/Manton bridges.

### N4 - Residual Matching

The residual is exactly `r=1/2` versus the finite-scan maximum near `r=1` on the
`C_3` singlet/doublet ansatz. It is not a readout-class, scale, or universal
native-action residual.

### N5 - Rhetoric Audit

The negative statement is route-local. It does not claim that no future native
principle can select block count.

### N6 - Partial-Closure Path Scan

A block-count admission, reference-state theorem, or new action principle could
still close the value residual. This note does not foreclose those paths.

### N7 - Steelman

A hostile reviewer can argue that the physically correct action is not one of
the five tested cutoff functions, or that a Casimir/HK/Wilson/Manton bridge
changes the allowed action surface. Those are real open routes; this is why the
claim is carried as an open gate rather than a universal no-go.

### N8 - Cross-Cycle Echo

Other flavor notes split the same form/value problem: native routes tend to
recover dimension weighting, while the Koide value requires a sector-weight
choice. This note adds the action-axis instance of that split.

**Gate result:** pass for the narrow action-axis boundary only.

## Provenance (verified 2026-06-02)
- HS block norms; equal-block <=> r=1/2; finite-scan maximum |b|/a ≈ 1 across five cutoffs;
  spectrum `[0,0,3a]` at b/a=1 => Q=1; mass/hop HS-orthogonality: verified directly by the runner.
- This note records only the finite five-cutoff scan and HS-orthogonality
  boundary. It does not carry the broader action-form degeneracy bridge.

# Single-Clock Antiperiodic Axis Datum S4-Transport Bounded Theorem

**Date:** 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome; effective status is pipeline-derived after
independent audit and dependency closure.

**Claim scope:** On an even cubic-symmetric staggered four-axis block, the
signed adjacent exchanges
`W_{a,a+1} = P_{a<->a+1} diag((-1)^{x_a x_{a+1}})` preserve the periodic
staggered hop and transport the single-antiperiodic-axis boundary datum from
axis `a` to axis `a+1`. Since adjacent transpositions generate `S4`, the
single-antiperiodic-axis label is one `S4` orbit on this declared Euclidean
block. The same runner verifies that the sublattice-parity grading is
`W`-invariant. Therefore a per-axis antiperiodic boundary condition breaks a
fixed chosen exchange, but its axis label is not an absolute axis supplier on
this surface.

This note does not derive a unique evolution axis, a time metric, a dynamics,
a generator, record-production dynamics, Lorentz structure, orientation, or a
second-clock exclusion. It only records the finite matrix transport theorem
above and the resulting boundary: a native one-parameter dynamics over the
fixed `Z^3` lattice is a separate open-gate input, not a consequence of this
Euclidean transport calculation.

**Runner:**
[`scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py`](../scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py)
(`TOTAL: PASS=22 FAIL=0`, deterministic, no RNG, runtime under one minute).

## Inputs and Boundary

The runner uses a finite even block `L = (4,4,4,4)` with the standard
time-first staggered phases and mass parameter `m = 0.3`. It also checks
robustness at `m = 1.7`, at `L = (6,6,6,6)`, and under an equivalent
staggered-phase convention.

The even-extent condition is load-bearing. The runner includes an odd-block
falsifier at `L = (3,3,3,3)`, where the signed exchange no longer preserves
the periodic staggered hop. The theorem is therefore scoped to even
cubic-symmetric staggered blocks, not all finite four-axis blocks.

Context and guardrails:

- `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
  for the existing single-clock evolution-axis premise surface whose axis-label
  component this note sharpens.
- `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
  only as the source of the previously named per-axis antiperiodic datum; this
  note recomputes the transport facts directly and does not import that
  note's audit status.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) for the
  guardrail that Lattice, Quantum, and Record do not supply a dynamics or
  time metric.

No fitted parameters, observed values, new axioms, primitive changes, Tier-A
admissions, or audit verdicts are introduced here.

## Computed Theorem

Let `M_per` be the periodic staggered hop on the even cubic-symmetric block.
Let `M_ap(a)` be the same operator with antiperiodic boundary condition in
axis `a` and periodic boundary conditions in the other axes.

For each adjacent pair `(a,a+1)` in `(0,1)`, `(1,2)`, `(2,3)`, the runner
computes:

```text
|| W_{a,a+1} M_per W_{a,a+1}^T - M_per || = 0,
|| W_{a,a+1} M_ap(a) W_{a,a+1}^T - M_ap(a+1) || = 0.
```

It also checks that the antiperiodic datum is genuinely moved, not fixed:

```text
|| W_{a,a+1} M_ap(a) W_{a,a+1}^T - M_ap(a) || = 16 > 1.
```

Since adjacent transpositions generate `S4`, the antiperiodic-axis label is
transportable around all four axes. A single-axis antiperiodic datum therefore
selects an axis only relative to an already chosen axis label.

The runner also verifies:

```text
|| W eps W^T - eps || = 0,
|| eps D eps + D || = 0,
```

for the staggered sublattice-parity grading
`eps(x) = (-1)^{sum_mu x_mu}` and massless hop `D`. This grading is
`W`-inert in the tested surface and carries no independent axis label.

## Open-Gate Boundary

The finite transport theorem does not decide how a physical one-parameter
time evolution is supplied. If time is instead introduced as a parameter of a
unitary group or CPTP semigroup over the fixed spatial Hilbert space
`tensor_{x in Z^3} C^2`, then the four-axis transport question has no object:
the parameter is not a fourth lattice coordinate. But the generator of that
one-parameter dynamics is not supplied by this calculation or by the minimal
axioms.

Thus the honest boundary is:

- the antiperiodic-axis datum is transportable on the declared Euclidean
  staggered surface;
- the tested parity grading is axis-label-free;
- a native one-parameter dynamics over `Z^3` remains a separate open gate.

This is a bounded theorem plus an open-gate localization, not a no-go over all
possible dynamics and not a derivation of a unique physical time axis.

## Reproduction

```bash
python3 scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py
python3 -m py_compile scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py
```

Expected summary:

```text
TOTAL: PASS=22 FAIL=0
```

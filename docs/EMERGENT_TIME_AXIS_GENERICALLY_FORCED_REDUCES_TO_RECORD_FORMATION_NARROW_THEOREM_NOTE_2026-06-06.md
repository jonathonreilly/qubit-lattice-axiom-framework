# The Unique Emergent Time AXIS is Generically Forced: the Open Object Reduces Exactly to Record Formation (R1) — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** bounded_theorem (the reduction + the genericity of R1; the *unconditional* version is the named residual)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/emergent_time_axis_generically_forced_runner.py`](../scripts/emergent_time_axis_generically_forced_runner.py)
**Cached output:** [`logs/runner-cache/emergent_time_axis_generically_forced_runner.txt`](../logs/runner-cache/emergent_time_axis_generically_forced_runner.txt)

## Audit context

The single-clock relocation result showed the staggered-η "no second clock" is convention-dependent
and that the unique clock **axis** is sourced by the records-arrow, leaving one named open object:
*"from Z³ + Record, a unique 4th time **axis** emerges (unconditionally)"* — with the suggested path
being record-accumulation as a Lieb-Robinson / causal-cone monotone. This note **resolves the open
object's structure**: it reduces **exactly** to **R1** ("does A_min force record formation?"), and
shows R1 is **generic** (decoherence einselects records), so the time axis is **generically — not
axiomatically — forced**.

Anchors:
[`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
(`retained_bounded`, the monotone),
[`POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06`](POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md)
(`retained_no_go`, the orientation residual),
[`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
(`retained_no_go`), and the Lieb-Robinson cone of
[`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01`](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md).

## Safe statement

**Theorem (reduction + genericity).**

1. **The open object reduces exactly to R1.** *"A unique emergent time axis from Z³ + Record"*
   holds iff records actually **form** (R1: a non-trivial, accumulating record structure exists).
   The remaining structure — once R1 holds — is forced (parts 2–4).

2. **Given R1, the axis is forced.** The additive non-negative record count `I` (`I(∅)=0`,
   additive over disjoint records, `I ≥ 0` as a count) is **non-decreasing along accumulation** and
   strictly increases (a non-trivial grading), so its constant-`I` level sets are **codim-1 spatial
   slices** (a foliation). The spatial `Z³` is **reversible** — each axis reflection `x_i ↦ −x_i`
   is an involution preserving the pairwise-distance multiset — so it carries **no** monotone; only
   the record-accumulation direction is timelike. The **unique time axis** is the `I`-gradient.

3. **The Lieb-Robinson cone makes the foliation causally consistent.** Any local A_min-consistent
   dynamics has a finite Lieb-Robinson velocity `v_LR` (the reconstructed `H = −log(T̂²)` is
   quasi-local; companion result), so the constant-`I` slices are **spacelike** — a causally
   consistent Cauchy foliation, with records registering within past cones.

4. **R1 is generic, but A_min has no dynamics axiom.** Under random local system–environment
   couplings the system's pointer-basis coherence is **suppressed and deepens with environment
   size** (`⟨coh⟩ = 0.31, 0.13, 0.07` for `n_env = 2, 5, 8`) — generic decoherence **einselects** a
   record; the no-record (coherence-preserving) case is **fine-tuned**. So R1 holds for **generic**
   A_min-consistent dynamics. But A_min (Lattice + Quantum + Record) contains **no dynamics axiom**
   pinning a specific record-production process, so the time axis is **generically** — not
   axiomatically — forced.

So the unique emergent time **axis** is **generically forced** by A_min: the open object reduces to
R1, R1 is generic, and given R1 the axis (foliation + spacelike slices + spatial reversibility) is
forced.

## The genuine open piece (the irreducible residual)

Two residuals remain, both precisely named:

- **The dynamics-axiom gap.** R1 is *generic* (decoherence) but not a *specific* A_min axiom — A_min
  has no dynamics axiom. Making the axis **unconditional** would require either a dynamics axiom or a
  proof that *every* A_min-consistent state/dynamics (not merely generic ones) produces records. This
  is the irreducible problem-of-time core.
- **The orientation.** Which `I`-direction is the future is **not** records-sourced (counts are
  word-reversal invariant —
  [`POST_RECORD_ARROW_ORIENTATION_FIREWALL`](POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md),
  `retained_no_go`); it is fixed only by the spectrum-condition `H ≥ 0` ⟺ a low-record past
  hypothesis.

## Boundary (honest)

- **Generically forced, not unconditional.** The axis is forced for *generic* dynamics; the
  unconditional version is the named dynamics-axiom residual. This is the honest strongest claim.
- **The genericity is a finite decoherence demonstration** (random local couplings, deepening
  suppression with environment size); it shows the no-record case is fine-tuned, not that *no*
  A_min-consistent state preserves coherence.
- **Axis, not linear clock or orientation.** This forces the time **axis** (the `I`-gradient /
  foliation); a fully linear single clock and the orientation carry their own (named) residuals.
- The monotone is the `retained_bounded` records-arrow; the LR cone is the companion quasi-local-`H`
  result; nothing rests on the `unaudited` single-clock note (whose axis-identity-via-η was shown
  convention-dependent in the relocation note).

## Forbidden imports check

No new axiom. A_min + standard decoherence/einselection (reproduced in the runner), the
`retained_bounded` records-arrow monotone, the Lieb-Robinson cone, and the spatial reversibility.
The unconditional axis and the orientation are named open, not asserted. Emergent time respected (no
time axiom; the axis is the intrinsic `I`-grading, not an imported coordinate).

## Runner check breakdown

Class A: (1) generic decoherence suppresses pointer coherence, deepening with environment size; (2)
the additive record count is a strict non-decreasing grading (codim-1 foliation); (3) the spatial
`Z³` is reversible (no monotone); (4) the reduction — given R1 the axis is forced (foliation +
spacelike slices + reversibility), and R1 is generic-not-axiomatic. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The open object reduces exactly to R1 (record formation): given a non-trivial accumulating record
structure, the additive monotone `I` foliates into codim-1 spatial slices, the Lieb-Robinson cone
makes them spacelike (causally consistent), and the reversible spatial `Z³` carries no monotone, so
the unique time axis is the `I`-gradient. R1 is generic — random local couplings einselect a record
with coherence suppression deepening as the environment grows — so the axis is generically forced;
but A_min has no dynamics axiom, so it is not unconditionally forced (the irreducible
problem-of-time residual), and the orientation needs the past hypothesis. The result is a clean
reduction + genericity, with the unconditional axis and the orientation named open. Effective status
remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/emergent_time_axis_generically_forced_runner.py
```

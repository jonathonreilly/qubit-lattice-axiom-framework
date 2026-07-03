# P3 (u_0 → α_LM) is Retention-Eligible Composition + One register-not-read Selection

**Date:** 2026-06-06
**Type:** coupling-side capstone / open-primitive reduction
**Claim type:** open_gate
**Status:** unaudited candidate. Reduces the hierarchy formula's open primitive
**P3** (the `u_0 -> α_LM` substitution) from "a free algebraic substitution" to
"an authority-inventoried composition packet + one isolated register-not-read
selection step." Sets no audit status; audit lane owns final classification.
`audit_required_before_effective_retained=true; bare_retained_allowed=false`.
**Runner:** [`scripts/p3_coupling_is_retention_eligible_composition_2026_06_06.py`](../scripts/p3_coupling_is_retention_eligible_composition_2026_06_06.py)
(`TOTAL` printed by the cached log).
**Cached log:** `logs/runner-cache/p3_coupling_is_retention_eligible_composition_2026_06_06.txt`

## Background

`HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10` lists **P3** among the four open
primitives: the `u_0^{16} -> α_LM^{16}` substitution in the determinant-to-`v`
map "equates a tadpole-improvement factor to a 16-th power of a coupling, an
**algebraic substitution** not a determinant identity." This note shows P3's
substitution `u_0 -> α_LM = α_bare/u_0` is an **authority-inventoried
composition packet**, isolating a single open step.

**One-hop authority repair:** 2026-06-08. This revision adds the authority
inventory and ledger-status guard requested by the audit lane, and it narrows
the note away from any claim that the whole P3 substitution is already retained.

## Statement (open-gate composition packet)

**(T1) Every quantity in the substitution is either an audited abstract algebra
input, a bounded canonical-surface input, or an explicitly conditional/open
input.**

| quantity | what it is | status |
|---|---|---|
| `α_bare = g_bare^2/(4π) = 1/(4π)` | native Coulomb coupling expression | `g_bare=1` is retained only as the abstract algebra forcing row; the `4π`/native-field-readout side is still conditional in the current audit ledger |
| `u_0` (~0.877) | canonical mean-field link from `canonical_plaquette_surface.py` (`<P>^(1/4)`) | bounded canonical-surface support; `PLAQUETTE_SELF_CONSISTENCY_NOTE` is `retained_bounded` and does not itself certify `0.5934` as a same-surface theorem |
| `α_LM = α_bare/u_0 = sqrt(α_bare·α_s)` | the **geometric mean** of bare & strong couplings | retained abstract algebra identity, conditional on separately supplied positive `(α_bare, u_0)` |
| `α_LM = α_bare/u_0^1` | the **tadpole-improved** coupling (vertex power 1) | retained abstract algebra identity, conditional on separately supplied positive `(α_bare, u_0)` |

So the substitution is: **tadpole-improve the native Coulomb coupling `α_bare` by
the native mean-field link `u_0`** -> the geometric-mean (physical) coupling
`α_LM`. With `g_bare=1`, `u_0~0.877`: `α_LM ~ 0.0907`, `1/α_LM ~ 11.0` — the
matched per-mode coupling on the bounded canonical surface. (Runner Sections A,
B.)

**(T2) The substitution is tadpole improvement plus retained identities, not a free relabeling.**
`α_LM = α_bare/u_0^1` is exactly the tadpole-improved coupling at vertex power 1,
and `α_LM = sqrt(α_bare·α_s)` is the retained abstract geometric-mean identity. The three
couplings `α_bare : α_LM : α_s` are a geometric progression with ratio `1/u_0`.
The substitution composes inventoried authorities rather than introducing a free
knob. (Section C.)

**(T3) The single remaining open step inside P3 (isolated): the magnitude reads the
PHYSICAL coupling, not the bare.** What is *not* yet derived is the **selection**:
the determinant-to-`v` map reads the physical (tadpole-improved, geometric-mean)
coupling `α_LM`, not the bare lattice factor `u_0` or the bare `α_bare`. This is
the register-not-read principle (the magnitude **registers** the physical/improved
coupling; the bare lattice `u_0` is a reconstruction). (Section D.)

This note also preserves the upstream conditional perimeter: the current audit
ledger still marks the `4π` native-coupling/readout bridge and the I1 static
readout relocation as conditional. Therefore this packet is not a retained P3
closure. Its repair target is a reauditable open-gate composition packet with
all load-bearing authorities visible.

## Honest meta-note (for the audit lane) — the register-not-read streak

**This is the 5th register-not-read application in this session's magnitude arc**
(`MAGNITUDE_TEMPORAL_FACTOR_IS_COUNT_NOT_RATE`,
`MAGNITUDE_READS_MINIMAL_RECORD_BLOCK`, `MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN`,
`I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION`, and this). They share the pattern
*the record registers the physical X; the bare/continuum/convention is a
reconstruction.* **register-not-read is now the load-bearing crux of the entire
magnitude account.** This note does not pretend that is settled — it explicitly
flags that the audit lane must adjudicate whether register-not-read genuinely
extends to mode-count, readout-scale, energy-readout, source-readout, and now
physical-vs-bare-coupling, or is being over-applied. The reduction in T1/T2 (every
authority-inventoried composition) holds independent of that adjudication; only
the T3 selection step rides register-not-read.

## What this delivers (the coupling side of the magnitude)

Combined with the temporal-factor and 4π results, the magnitude's structure is now
accounted for as:

```text
v/M_Pl = (7/8)^{1/4} · α_LM^16
  exponent 16        = native mode COUNT (8 spatial x 2 temporal)        [#3193/#3195]
  α_LM (per mode)    = tadpole-improve(coupling α_bare, canonical u_0)
                     = geometric mean sqrt(α_bare·α_s)   [retained abstract identity + this note]
  α_bare = 1/(4π)    = conditional native-coupling/readout bridge          [#3200 + I1 #3207]
```

So the **coupling side** (`α_LM`) is an authority-inventoried composition over
abstract retained algebra, bounded canonical-surface inputs, and conditional
readout bridges, with the single P3-local open step being the physical-vs-bare
*selection* (register-not-read).

## What this note does NOT claim

- Does **not** close the hierarchy magnitude or derive `v`. The physical-coupling
  selection (T3, register-not-read), the energy-readout bridge, the `(7/8)^{1/4}`
  selector, `u_0`'s specific value (sub-decade), and P4 (Higgs = condensate)
  remain.
- Does **not** settle the register-not-read principle — it flags the 5-application
  streak for collective audit.
- Does **not** upgrade the geometric-mean or tadpole rows; it composes them.
- Sets no audit status.

## Load-bearing dependency and context references

### One-hop authority packet for re-audit

The runner now verifies these ledger rows and note paths directly.

| role | claim id | note path | current effective status consumed here |
|---|---|---|---|
| geometric-mean identity | `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24` | [`ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md`](ALPHA_LM_GEOMETRIC_MEAN_IDENTITY_THEOREM_NOTE_2026-04-24.md) | `retained` abstract algebra only |
| tadpole vertex-power identity | `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10` | [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` abstract algebra only |
| abstract positive-branch `g=1` algebra | `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note_2026-05-10` | [`G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10.md`](G_BARE_FORCED_BY_WARD_REP_B_INDEPENDENCE_ABSTRACT_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` abstract algebra only |
| bounded plaquette surface / finite observable | `plaquette_self_consistency_note` | [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) | `retained_bounded`; not a same-surface theorem for the numerical `0.5934` value |
| native `4π`/coupling-readout bridge | `magnitude_4pi_is_native_coupling_not_gaussian_2026-06-06` | [`MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06.md`](MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06.md) | `audited_conditional`; not consumed as retained |
| I1 static readout relocation | `i1_static_readout_is_native_field_integration_2026-06-06` | [`I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md`](I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06.md) | `audited_conditional`; not consumed as retained |

- `alpha_lm_geometric_mean_identity_theorem_note_2026-04-24` supplies
  `α_LM = sqrt(α_bare·α_s)` only as an abstract positive-scalar identity.
- `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`
  supplies the one-link-power tadpole algebra only as an abstract identity.
- `g_bare_forced_by_ward_rep_b_independence_abstract_narrow_theorem_note`
  supplies the abstract positive-branch `g=1` forcing instance; it does not by
  itself close the physical Ward-route premises.
- `PLAQUETTE_SELF_CONSISTENCY_NOTE` and `scripts/canonical_plaquette_surface.py`
  supply the bounded canonical `u_0` surface used for the numerical sanity
  check; the note does not promote the canonical number to a retained
  same-surface plaquette theorem.
- `MAGNITUDE_4PI_IS_NATIVE_COUPLING_NOT_GAUSSIAN_2026-06-06` and
  `I1_STATIC_READOUT_IS_NATIVE_FIELD_INTEGRATION_2026-06-06` are intentionally
  listed as conditional upstream bridge rows, not as retained inputs.
- `record_outcome_observable_principle_canonical_proposal_note` (**meta**) — the
  register-not-read principle (T3).
- `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10` — the P3 primitive this reduces.

## Forbidden imports check

- No PDG observed values consumed (`v`/`α_LM`/`u_0` appear as labelled background,
  in no PASS condition).
- No new import introduced; the result inventories existing abstract retained
  rows, bounded canonical-surface support, and explicitly conditional coupling
  readout rows.
- No fitted selectors; no new axiom proposed.
- All cited statuses verified on the live ledger by the runner.

## Validation

`scripts/p3_coupling_is_retention_eligible_composition_2026_06_06.py`:
Section A (geometric-mean identity, geometric progression ratio `1/u_0`), Section B
(composition: native `α_bare` × native `u_0` -> `α_LM`; `α_LM~0.0907`, `1/α_LM~11`),
Section C (tadpole improvement vertex power 1; authority rows checked against
the live ledger),
Section D (the single open step = physical-vs-bare selection = register-not-read,
5th application, flagged).

## Reading rule

This note is the claim boundary for: P3's `u_0 -> α_LM` substitution is an
authority-inventoried composition (abstract retained algebra + bounded canonical
surface + explicitly conditional readout bridges) -- *not* a free algebraic
substitution -- with a single isolated P3-local open step: the magnitude reads
the physical (improved, geometric-mean) coupling, not the bare
(register-not-read, the 5th application in the arc, flagged for collective
audit). It does **not** close the magnitude and does **not** assert that P3 is
retained on the current surface.

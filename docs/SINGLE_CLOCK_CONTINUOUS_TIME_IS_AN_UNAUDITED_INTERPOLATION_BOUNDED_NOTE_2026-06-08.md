# The Single-Clock Theorem's Continuous Time `U(t)` Is an Unaudited Interpolation: No Retained Consumer Requires Non-Integer-`t` Evolution, so the Continuous-Time Velocity-Obstruction Surface Has No Retained Witness — Bounded Note

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a repo-internal consumer audit; demotes a surface's retained status)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_single_clock_continuous_time_load_bearing_audit_2026_06_08.py`](../scripts/frontier_single_clock_continuous_time_load_bearing_audit_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_single_clock_continuous_time_load_bearing_audit_2026_06_08.txt`](../logs/runner-cache/frontier_single_clock_continuous_time_load_bearing_audit_2026_06_08.txt)

---

## Role

The interacting velocity-anisotropy obstruction (`δv ≠ 0`, 12–21 orders over SME
bounds) lives on the `ξ → ∞` surface = spatial `Z³` + **continuous** time
`U(t) = exp(−itH)`. The claim that this continuous-time surface is the framework's
**derived physical** surface rests on
[`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
(live-ledger **unaudited**), whose **Step 1** builds `U(t)` as the **analytic
continuation** of the genuinely-derived **discrete** transfer `T^n`
(`T^n = U(−inτ)` at **integer** `n`) to non-integer `t`.

This note audits, mechanically, whether continuous `U(t)` at **non-integer `t`** is
load-bearing for any **retained** consumer. The result: **it is not.** Every retained
continuous-time consumer is integer-`T^n`-only, an `a → 0` **emergent** limit, or a
**supplied-context** input. So the continuous-time obstruction surface has **no retained
witness** — it is the unaudited Step-1 interpolation, and the discrete `T^n` (Euclidean
staggered `Z⁴`) is the equally-available default lattice reading. Runner: **12 PASS /
0 FAIL**.

## The audit

Classification of every retained / retained_bounded row that uses continuous-time
`U(t)` (verified by reading each note; runner Part 1):

| Retained consumer | Status | How it uses continuous time | Class |
|---|---|---|---|
| [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) | retained | retains `T^n = U(−inτ)` at **integer** `n`; its broader non-integer *continuity* headline was **demoted as "false as written"** | **integer-`T^n` only** |
| [`LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md`](LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md) / 3+1D | retained / retained_bounded | *"exact theorem on the continuum-limit free-scalar surface … in the continuum limit `a → 0`"* | **`a → 0` emergent limit** (= what `U(t)` is) |
| [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) | retained_bounded | the dim-6 `(E/M_Pl)²` IR dispersion isotropy | **IR/continuum emergent** |
| [`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) (#3121) | retained_bounded | continuous time is *"the context under test"* (a **supplied** input); the `c_t`-fixing uses the **equal-time CAR** (single-slice, preserved by the discrete unitary `T` too) | **supplied-context / integer** |
| RP / spectrum / cluster / microcausality / OS | retained / retained_bounded | the Euclidean transfer `T` at **integer** steps (slice reflection, per-step Lieb-Robinson) | **integer-`T^n` only** |

**Verdict (runner Part 2):** **zero** retained consumers evaluate `U(t)` at non-integer
`t` in a load-bearing way. The Lorentz boost covariance — the one place continuous
spacetime is genuinely needed — uses it **only** as the `a → 0` emergent limit, which is
exactly Route 1's reading of `U(t)` as an IR interpolation. So the continuous-time
obstruction surface (`ξ → ∞`) is **not** retained-witnessed; it is the unaudited
single-clock Step-1 analytic continuation.

## Verdict

**The obstruction horn is demoted to an unaudited interpolation.** The genuinely-derived
dynamics is the discrete positive transfer `T` and its integer powers `T^n`; continuous
`U(t)` at non-integer `t` is non-load-bearing decoration with no retained consumer. So
the velocity obstruction's claim to live on the framework's **derived** surface loses its
retained witness, and the discrete `T^n` (Euclidean staggered `Z⁴`) — on which the
canonical B₄-symmetric staggered action gives `δv = 0` (the supplied-Z⁴ B₄ boundary
note's surface) — is the equally-available default.

## Honest scope (this is a BOUNDED advance, not a closure)

- It **demotes** the obstruction horn (removes its claim to be the derived/retained
  surface); it does **not** establish `δv = 0` retained.
- The **discrete-surface temporal form** is the separate remaining realization question:
  the symmetric central-difference staggered tick gives `Σ_t = Σ_s` to `~5×10⁻¹⁸` (B₄,
  `δv = 0`), while the one-sided **forward** transfer `T = e^{−Ha_τ}` breaks B₄ to
  `~5×10⁻⁴`. The velocity self-energy is an object of the Euclidean **action** (the
  canonical staggered action is B₄-symmetric), but pinning that over the forward-transfer
  operator reading is the residual.
- It does **not** touch the **unbounded** gate: retention of `δv = 0` additionally needs
  the symmetric staggered action to be the physical loop object **and** the interacting
  U-integrated cone (open). This note is a bounded advance only.
- **No** new axiom, primitive, repo vocabulary, or class tag; sets **no** audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, repo-internal): the classification of every retained
  continuous-time consumer (each verified by reading the note); the verdict that zero
  require non-integer-`t` `U(t)`; the `T^n = U(−inτ)` integer-consistency and the
  demoted-as-false non-integer continuity of the Stone uniqueness note.
- **Cited** (comparator/scope only): none required (repo-internal audit).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. The cited
ledger statuses are recorded verbatim as of 2026-06-08.

- [AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) (`unaudited`)
- [SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) (`retained`)
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md) (`retained_no_go`)
- [LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md) (`retained`)
- [LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md) (`retained_bounded`)
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md) (`retained_bounded`)
- [TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md](TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the live-ledger statuses
of the single-clock theorem and its retained consumers; (3) the single-clock Step-1
construction (`U(t)` = analytic continuation of `T^n`). The result is a repo-internal
consumer audit: no retained row requires non-integer-`t` `U(t)`, so the continuous-time
obstruction surface is an unaudited interpolation. Bounded advance; not a `δv = 0`
closure.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag; no
fitted/PDG value; repo-internal only.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the single-clock theorem, the velocity-RG notes, the boost-covariance notes,
or any upstream row. The independent audit lane is the only status authority.

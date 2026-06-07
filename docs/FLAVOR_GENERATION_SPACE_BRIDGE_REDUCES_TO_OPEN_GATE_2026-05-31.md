# Flavor — the generation-space bridge to δ=2/9 reduces to a single named import (the intensive-summand-as-observable promotion), and the value-construction survives the anticommuting no-go

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** bounded characterization (a gap-reduction) + one new positive structural fact. Not a closure; not an import.
**Runner:** `scripts/flavor_generation_space_bridge_reduces_to_open_gate_2026_05_31.py` (SCORECARD 15/15).
**Source:** workflow `wf_d994df21-e74` — 5 attack routes + 3-lens adversarial verification + synthesis (18 agents).

## Question
Is the bridge **"the physical charged-lepton generation space IS the C₃[111] fixed locus, so the
native staggered Dirac's LOCAL equivariant Lefschetz density there (= 2/9) is the flavor-asymmetry
observable"** derivable from framework baseline+retained, or does it reduce to one named import?

This note refines the prior `FLAVOR_ASYMMETRY_IDENTIFICATION_PRINCIPLED_NOT_FORCED_2026-05-31`
verdict ("principled-but-not-forced, bridge undischarged") into a *precise* gap-reduction.

## Verdict: closed_modulo_one_named_import — and the gap is an EXISTING ledger row

The bridge does **not** close from framework baseline+retained, but the residual is now pinned to a single,
already-named premise rather than a diffuse "identification."

### Finding A (new positive content) — the value-CONSTRUCTION survives the anticommuting no-go
The retained wall `koide_z3_equivariant_anticommuting_no_go` (retained_bounded) forbids a single
C₃-equivariant operator that *anticommutes* with the chiral grading `Γ_χ=(2/3)J−I` — such an object
is block-**off**-diagonal (it must intertwine the +1 singlet `[111]` with the −1 transverse doublet),
and Schur kills it. **The local-density construction of 2/9 never invokes such an object.** It uses
only block-**diagonal**, *commuting* data:
- `[C, Γ_χ] = 0` and `[P₋, Γ_χ] = 0` to machine zero (`P₋` = projector onto the −1 doublet);
- the Atiyah-Bott local density is a pure C₃ **character/trace** number:
  `L₃(1,2) = (1/3) Σ_{k=1,2} 1/((ωᵏ−1)(ω²ᵏ−1)) = 2/9` exactly, with each nontrivial-element term
  `1/((ω−1)(ω²−1)) = 1/3` and transverse `det(1−dg) = (1−ω)(1−ω²) = 3`.

So **2/9 exists as a number requiring no Hermitian `H` with `{H,Γ_χ}=0`.** The no-go bounds the
*operator-realization* side (a single anticommuting `H`), **not** the *value-construction* side.
This sharpens the no-go's scope: it is a wall against one realization, not against the value.
(Confirmed independently by attack Routes 1, 2, 4; Route 1 verdict `open_unobstructed`, conf 0.88.)

The faithful transverse weight-tuple is `(1,2)` (the two nontrivial C₃ characters, `a₁+a₂=3≡0 mod 3`,
trace-free); the degenerate alternative gives `L₃(1,1) = 1/9`. The `J_cs` complex structure (forced
by Schur, prior campaign work) supplies the holomorphic/Dolbeault denominator form.

### Finding B (the single irreducible gap) — promoting an intensive summand of a vanishing total
Under framework baseline+retained the genuine equivariant-index **invariants** are **extensive** and **vanish** on
the retained C₃-equivariant native staggered Dirac: `Γ₅=(−1)^{x+y+z}` forces ± spectral pairing, so
the global η = 0, the signed global Lefschetz invariant = 0, and the Euler characteristic χ = 0. The
number 2/9 is a **per-fixed-point local density**. If one forms an unsigned same-orientation diagnostic
from `L` identical local summands, it scales as `L·(2/9)` (`L=3→2/3`, `L=8→16/9`), but that diagnostic
is not the signed global invariant. The invariant sum cancels after the retained `Γ₅` pairing. Thus
the 2/9 value survives **only by refusing the signed global sum** and selecting one intensive local
summand as the observable.

The one unforced step is therefore: **promote the intensive single-fixed-point local density 2/9 to
THE physical flavor-asymmetry observable**, rather than treating it as a contribution to the
(vanishing) extensive invariant. No cited equivariant-index theorem (Atiyah-Bott, ABBV/Berline-Vergne
localization, Vergne) licenses reading a single fixed-point summand as a free-standing physical ratio —
each summand is well-defined *as a term of the total*, never as an observable on its own.

**This promotion is not a new gate — it is an existing one.** It coincides exactly with:
- the `open_gate` row `lepton_brannen_bae_delta_two_ninths` (origin/main), and
- the `a=0` zero-section pick of the `retained_no_go` `koide_q_delta_residual_cohomology_obstruction`.

It also **cannot be discharged by exhibiting an equivariant operator**: any concrete `H` forcing the
local denominator `∏_j (ζ^{k a_j}−1)^{−1}` must *break* the C₃ orbit (the counting-vs-splitting
tension), which the retained counting structure (`three_generation_observable_theorem`) forbids on the
same orbit. So the gap is genuinely a *readout/promotion* premise, not a missing operator.

### Finding C (downstream, subsumed) — the 2/9 → Koide Q map needs the audited_failed readout-class
`2/9` is a Brannen **phase** datum. Mapping it to `Q = 1/3 + (2/3)r = 2/3` requires the **signed**
(`det_R`/Brannen) readout: at `r=1/2` the signed Q ≡ 2/3 δ-independently, whereas the singular-value
(Yukawa) Q is δ-dependent and ≤ 2/3 (runner E1: signed = 0.6667 const; singular-value range
[0.4094, 0.6667]). The signed readout-class is `audited_failed` on origin/main
(`koide_signed_eigenvalue_vs_singular_value_readout`). This is **subsumed inside the same open gate**,
not an independent second import.

## What this advances
- The bridge is reduced from a diffuse "generation-space identification undischarged" to **one named,
  pre-existing premise** (`lepton_brannen_bae_delta_two_ninths`), with its mechanism made explicit
  (intensive-summand-of-a-vanishing-extensive-invariant promotion).
- **New positive fact:** the value-construction of 2/9 is *unobstructed* by the anticommuting no-go;
  the wall constrains only the single-anticommuting-`H` realization. This separates two things the
  campaign had been conflating (the value vs. its operator realization).

## Dissent recorded (honest scope)
Attack Route 3 (`not_closed_obstructed`, conf 0.83) argues there are *two* unforced steps, not one:
besides the summand-promotion, it contests whether the `(1,2)` weight-tuple is operator-forced
(vs. imported from the trace-free character pattern) and whether the holomorphic/Dolbeault denominator
form is presupposed. The synthesis treats `(1,2)` as forced by *faithfulness* of the transverse C₃
action and the denominator form as supplied by the Schur-forced `J_cs`; this note records Route 3's
dissent so the gap is not under-stated — if those sub-steps are also unforced, the residual is wider,
but still routes through the **same** open gate (none of them closes the bridge).

## Stale-citation guard (verified vs origin/main ledger, 2026-05-31)
- `lepton_brannen_bae_delta_two_ninths` — **open_gate** (the residual gap; this note characterizes it).
- `koide_z3_equivariant_anticommuting_no_go` — **retained_bounded** (the no-go; Finding A shows its scope).
- `koide_q_delta_residual_cohomology_obstruction` — **retained_no_go** (the `a=0` zero-section coincidence).
- `koide_signed_eigenvalue_vs_singular_value_readout` — **audited_failed** (Finding C; downstream, subsumed).
- `axiom_first_z_n_equivariant_spectral_asymmetry_narrow`, `koide_aps_block_by_block_forcing` — **retained_bounded**.
- `three_generation_observable_theorem` (+ `_no_proper_quotient`, `_m3c_burnside`) — **retained** (the count side).
- Does **NOT** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route` (both **unaudited**).

## 2026-06-07 Source-Packet Repair: exact residual matching

The audit blocker asked this row to include the source packet for the named
residual gate. This branch supplies that restricted-packet visibility without
promoting the residual:

- [`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md`](LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md)
  is the audited-clean open-gate source packet for the conditional
  Brannen-BAE `delta = 2/9` comparator.
- [`scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py`](../scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py)
  is the paired runner.
- [`logs/runner-cache/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.txt`](../logs/runner-cache/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.txt)
  is the paired SHA-pinned cache, expected `TOTAL: PASS=17 FAIL=0`.

Raw restricted-packet paths:

- `docs/LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26.md`
- `scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py`
- `logs/runner-cache/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.txt`

This repairs the source-packet part of the restricted-packet blocker: the
downstream note now exposes the exact open-gate comparator packet it names as
the residual. It does **not** derive the phase `delta = 2/9`, the `sqrt(2)`
Brannen/BAE coefficient, the charged-lepton mass scale, or the physical rule
selecting one fixed-point summand as the charged-lepton asymmetry observable.

The remaining blocker is unchanged and explicit: a future source theorem would
still have to prove that the physical charged-lepton generation space is the
`C3[111]` fixed locus and that the readout consumes one intensive local
Lefschetz density rather than the vanishing signed global invariant or the
extensive sum.

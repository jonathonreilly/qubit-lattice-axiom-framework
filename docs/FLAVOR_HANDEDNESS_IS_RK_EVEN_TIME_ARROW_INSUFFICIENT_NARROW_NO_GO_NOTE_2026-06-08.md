# The Flavor Handedness Z₂ Is RK-Even — the Time-Arrow Alone Cannot Fix It

**Date:** 2026-06-08
**Claim type:** no_go (scoped located no-go + residual relocation)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_flavor_handedness_rk_even_arrow_insufficient.py`](../scripts/frontier_flavor_handedness_rk_even_arrow_insufficient.py)
**Cached log:**
[`logs/runner-cache/frontier_flavor_handedness_rk_even_arrow_insufficient.txt`](../logs/runner-cache/frontier_flavor_handedness_rk_even_arrow_insufficient.txt)
(TOTAL: PASS=14 FAIL=0)

## 0. The question, and the precise answer

A companion result (branch `science/koide-delta-phase-count-one-z2-orientation-2026-06-08`,
named in plain text) showed the generation **count** (`S_3 → C_3`) and the Brannen
**phase** chirality (`+δ_*` vs `−δ_*`) reduce to **one global Z₂** — the handedness
`sign(Δ)`, `Δ(p)=(p_0−p_1)(p_1−p_2)(p_2−p_0)` = the `Cl(3)` pseudoscalar / volume-form
orientation. The natural next question is whether the framework's only non-axiom temporal
input — the **arrow of record accumulation** (retained-bounded
[`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md))
— **fixes** that handedness.

**It does not, and this note says exactly why.** The handedness is **odd under both**
time-reversal `T = K` **and** the spatial axis-swap reflection `R` (an improper cubic-group
element), hence **even under `RK`**. The arrow breaks only `T`; the reflection `R` remains a
bare-lattice symmetry. So the arrow alone leaves the two orientations degenerate. The
handedness is intrinsically a **spatial-parity (reflection) datum**, `RK`-correlated with the
arrow but **not** `T`-fixed. This relocates the open input from "a chirality gate" to a
precise object: **the spatial-reflection (`R`) breaking** — with the staggered axis-ordering
as the natural candidate to supply it.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| handedness `sign(Δ)` = `S_3` sign-rep / `Cl(3)` pseudoscalar; governs count + phase | companion (plain-text), [`POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23`](POSITIVITY_BRIDGE_REQUIRES_ORIENTATION_SIGN_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | the object characterized |
| arrow = past-hypothesis boundary; `Θ = K` reverses it; microdynamics time-symmetric | [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md) | `retained_bounded` | the temporal input tested |
| `H = iD` real anti-Hermitian; `Θ_H = P K` commutes with `H` (T-symmetric dynamics) | [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained_bounded` | `T = K`, `K i K = −i` |
| emergent-time mechanism is conjugation-EVEN, blind to `arg(b)` | [`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md) | `retained_bounded` | corroborates: dynamics can't select the orientation |
| spatial inversion `P` is the identity on the generation triplet | [`PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23`](PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | why the relevant reflection is the axis-swap `R`, not `P` |
| quark-sector mass-orientation / θ_eff on the Wilson surface | [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md) | `unaudited` | context: the analogous mass-orientation lane |

No PDG value is load-bearing; PDG enters only the Section 5 comparator. No new axiom,
import, or vocabulary.

## 2. The handedness is T-odd and R-odd (RK-even)

Write the retained `C_3`-circulant generation operator `G = g_0 I + g_1 C + ḡ_1 C²`
(`C` the real cyclic shift `x→y→z`), with the Brannen phase `δ = arg(g_1)` and Born record
`p_k(δ)`. The handedness is `sign(Δ(p))`.

**(T) `sign(Δ)` is T-odd.** Time-reversal `T = K` (complex conjugation; `K i K = −i`,
retained CPT) acts on the circulant as `g_1 ↦ ḡ_1`, i.e. `δ ↦ −δ` (runner
`T_K_conjugates_..._minus_delta`). Since `δ → −δ` flips `sign(Δ)`
(`Δ(+2/9)=+0.0467`, `Δ(−2/9)=−0.0467`), `sign(Δ)` is **odd under `T`** (runner `T_*`).

**(R) `sign(Δ)` is R-odd.** Let `R` be a spatial **axis-swap reflection** — an **improper**
element of the cubic point group (`det R = −1`). It conjugates `R C Rᵀ = C²`, reversing the
3-cycle, so again `δ ↦ −δ` and `sign(Δ)` flips (runner `R_*`). By contrast the **proper**
3-fold rotation `C_3[111]` (`det = +1`, in `A_3`) **preserves** `sign(Δ)`
(`R_proper_rotation_preserves_orientation`). The relevant reflection is the axis-swap `R`,
**not** spatial inversion `P` — `P` is the identity on the triplet
(`PARITY_VIOLATION_..._TRIPLET`).

**(RK) `sign(Δ)` is RK-even.** `T = K` and the axis-swap `R` are **distinct** operations —
`K` antiunitary, `R` unitary (real orthogonal, improper) — that each flip the handedness;
only their product `RK` (antiunitary) fixes it (runner `RK_even`, `RK_R_is_unitary_distinct`).

## 3. The time-arrow alone cannot fix it

The framework dynamics `H = iD` is **time-symmetric**: `K H K = −H`, so the free evolution
`e^{Dt}` is real and `Θ_H = P K` commutes with `H` (retained CPT). The arrow is **not** in the
dynamics; it is a **past-hypothesis boundary datum** whose only role is to break `T` (pick the
low→high record direction; `T = K` reverses it — retained arrow note). The retained K-reality
note independently confirms the emergent-time mechanism is **conjugation-even, blind to
`arg(b)`** — it carries no information selecting the orientation.

Because `sign(Δ)` is **RK-even**, breaking `T` while the spatial reflection `R` is **unbroken**
leaves the two orientations exactly degenerate: `R` maps the realized record to its equally
admissible mirror. The bare cubic lattice **is** `R`-symmetric (the axis-swap is in `O_h`).
Therefore:

> **The arrow of record accumulation does not fix the flavor handedness.** Fixing it requires
> breaking the spatial axis-swap reflection `R` (spatial parity), which the time-arrow does
> not supply.

This is the sharp resolution of the standing "arrow-vs-symmetry tension": the arrow (temporal,
`T`) and the handedness (spatial-reflection, `R`) are **distinct Z₂'s**, correlated only
through the antiunitary product `RK`.

## 4. Where the handedness must come from (partial-closure path, not a closure)

This note does **not** claim the handedness is underivable — only that the *time-arrow alone*
is insufficient. The residual is now precise: an `R`-breaking (spatial-reflection / parity)
ingredient. The natural framework candidate is the **staggered phase choice** `η(x,μ)`, which
fixes an **ordering of the spatial axes** and so breaks the axis-swap `R` — converting the
`RK`-correlation into an actual handedness once the staggered axis-ordering is shown physical
(not a field-redefinition convention). That is the live next step: derive (or admit) the
`R`-breaking; with it, the `RK`-even handedness is fixed and `RK`-correlated to the arrow,
closing the count and the phase together. No new axiom is requested.

## 5. Scope — what this establishes and does not

**Establishes (exact, finite):**
- `sign(Δ)` is T-odd, R-odd, RK-even, with `R` the improper axis-swap and `C_3[111]` proper.
- `H = iD` is T-symmetric; the arrow breaks only `T`; `R` stays a bare-lattice symmetry.
- Hence the arrow alone cannot fix the handedness; the residual is `R`-breaking (parity).

**Does NOT establish (named, untouched):**
- It does **not** prove the handedness is underivable; the `R`-breaking (staggered
  axis-ordering) is a live partial-closure path.
- It does **not** select the magnitude `|δ| = 2/9 = L_3(1,2)` (separate; reproven cyclotomic).
- It does **not** force or touch the `r = 1/2` cone (`Q = 2/3`, held fixed for all `δ`).
- It does **not** resolve the quark-sector strong-CP mass orientation (the analogous
  `unaudited` lane), used only as context.

## 6. Honest verdict

The "derive the global handedness from the arrow" route does **not** close. The handedness is
an `RK`-even datum, and the time-arrow breaks only the `T` factor; the unbroken spatial
reflection `R` keeps the two orientations degenerate. The genuine content is the **relocation**:
the open flavor handedness — which governs both the generation count and the Brannen phase — is
specifically a **spatial-parity (axis-swap reflection) breaking**, `RK`-correlated with the
arrow but not fixed by it. The next lever is the staggered axis-ordering (spatial-`R`-breaking),
not the time-arrow. The magnitude `2/9` and the `r = 1/2` cone remain the separate, untouched
residuals.

## 7. No-Go Discipline Gate

**Status:** PASS for this scoped located no-go. It says the **time-arrow alone** does not fix
the handedness; it does **not** say the handedness is underivable, that `2/9` is unreachable,
or that the route is closed.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| time-arrow (`T`-breaking, past hypothesis) | ATTEMPTED | insufficient — `sign(Δ)` is RK-even, `R` unbroken |
| proper rotation `C_3[111]` | RULED OUT | `det=+1`, preserves orientation (both signs `C_3`-symmetric) |
| spatial inversion `P` | RULED OUT | identity on the triplet (`PARITY_..._TRIPLET`) |
| spatial axis-swap reflection `R` breaking | OPEN RESIDUAL / PATH | improper, flips `sign(Δ)`; staggered axis-ordering is the candidate |
| magnitude `2/9` | SEPARATE RESIDUAL | `L_3(1,2)` |

**N2 — Wall-independence.** The handedness *object* (companion), the `RK`-even *character*
(this note), the `R`-breaking *source*, the magnitude `2/9`, and the `r=1/2` cone are
independent; this note resolves only the character and the arrow-insufficiency.

**N3 — Hidden-wall scan.** The result uses only `T = K` (`K i K = −i`, retained), `R C Rᵀ = C²`
(`det R = −1`), and the definition of `Δ`. "Arrow", "parity", "staggered" name the
inputs/residual, not hidden premises.

**N4 — Residual matching.** The residual named is exactly the spatial-reflection (`R`/parity)
breaking, not the magnitude and not the cone.

**N5 — Rhetoric audit.** The claim is *time-arrow insufficiency for an RK-even datum*, proven by
the parity computation — not a general impossibility and not a derivation.

**N6 — Partial-closure path scan.** The legitimate next step is the staggered-axis-ordering
`R`-breaking (Section 4); with it the handedness is fixed and `RK`-correlated to the arrow. No
new axiom requested.

**N7 — Steelman.** A reviewer may argue CPT (`Θ_H = P K`) could lock `P` to `K` and thus the
arrow could reach a reflection. This note's `R` is the **axis-swap**, distinct from the
inversion `P` (which is trivial on the triplet); CPT's `P` does not supply the axis-swap
`R`-breaking. The steelman correctly identifies that *some* reflection breaking is needed —
which is exactly the named residual.

**N8 — Cross-cycle echo.** Consistent with the retained arrow note (arrow = boundary, `Θ=K`),
the retained CPT (`H=iD`, `Θ_H=PK`), the retained K-reality GAP A (conjugation-even
emergent-time), and the retained parity-trivial-on-triplet — connecting them without overruling
any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained/retained-bounded rows
  plus the circulant/Brannen algebra.
- **No PDG/fitted load-bearing input** (PDG only in Section 5 comparator); **no forcing of
  `r = 1/2`**; **no new transcendental constant.**
- The companion and the `unaudited` strong-CP note are named as context, not citation-graph
  dependencies.

## 9. Command

```bash
python3 scripts/frontier_flavor_handedness_rk_even_arrow_insufficient.py
```

Expected: `TOTAL: PASS=14 FAIL=0`. numpy + stdlib, deterministic, 3×3 / 3-vectors throughout
(memory-safe). The runner verifies the handedness `sign(Δ)`, its T-oddness (circulant
conjugation), its R-oddness (improper axis-swap, proper rotation preserving), RK-evenness with
distinct unitary/antiunitary factors, the T-symmetric `H=iD` dynamics, the arrow-breaks-only-T
relocation, the separate `L_3(1,2)` magnitude, and the phase-blind `Q=2/3` cone.

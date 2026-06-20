# Block 05 — Route R-DEFINABILITY (Beth/Svenonius independence theorem)

**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block05-20260620`
**Clauses:** N2b + N4 + N5 (all three B-AXIS open clauses at once)
**Runner:** `scripts/single_clock_definability_independence_2026_06_20.py`
**Cache:** `logs/runner-cache/single_clock_definability_independence_2026_06_20.txt`
**Result:** **TOTAL PASS=24 FAIL=0**
**Outcome:** `confirms_wall_sharper` — upgrades route-exhaustion to a definability
**independence theorem**; the crack check on all three approved primitives finds
**NO CRACK**; one sharpening of the block02 N4 wording is recommended.
**No new axiom / no new primitive.** A_min = Lattice + Quantum + Record + the four
approved primitives only. Independent audit lane is the sole status authority.

---

## 1. What this route does (and why it is no-lose)

Block02 discharges N2b / N4 / N5 by **route exhaustion**: the N1 gate enumerates
≥5 attack routes per clause and walls each. Route-exhaustion is honest but weak —
it cannot exclude a not-yet-tried route. This route upgrades it to a single
**independence theorem** using the semantic side of Beth definability (Svenonius):

> A quantity `q` is definable from a structure `𝔄` **iff** `q` is fixed by **every**
> automorphism of `𝔄`. (⇒ definitions are automorphism-invariant; ⇐ Svenonius.)

So instead of "we tried N routes", we write `Aut(𝔄)` **explicitly** and check,
symbol by symbol, which B-AXIS quantity each generator **moves**. Anything moved by
even one automorphism is **provably undefinable** — this closes ALL routes at once,
including unborn ones. The block02 `[τ-RESCALE]` and `[C-2CLK]` witnesses were
already, in model-theoretic language, **automorphisms that move `a_τ` and the
clock-ray**; this route names them as such and adds the missing third symbol (the
axis label, moved by the signed exchange / transitive `S₄`).

The route is **no-lose** by construction (MATH_SECTOR_SEARCH S-8): either it ships a
clean independence theorem, or the crack check discovers a primitive that
*shrinks* the automorphism group enough to **fix** a previously-free quantity (a
closure lead). Here: independence theorem ships, no crack.

## 2. The automorphism group `Aut(𝔄)`, written explicitly (Section A, 6/6 PASS)

`𝔄` is the concrete retained object: even cubic-symmetric `Z³ × Z_τ` block (Lattice),
staggered-Dirac hop `M_KS` (Quantum carrier), supplied two-step transfer
`T̂² = ⊗_p diag(1, e^{−2E(p)}) = exp(−2 a_τ Ĥ)` (the clock), the per-mode
occupations `{n_p}`, the additive Record scalar, and the dimensionful unit `a_τ`.
`Aut(𝔄)` factors into three explicitly enumerated generators, each verified to
preserve the structure (recomputed in-tree, not cited blind):

| gen | group | action | verified |
|---|---|---|---|
| **G1** | `R_{>0}` (τ-rescale) | `a_τ→c·a_τ, Ĥ→Ĥ/c, Q→Q/c` | `T̂²` invariant, max Δ `3.5e-17` |
| **G2** | `S_{L_s}` (factor permutation) | permute the `L_s` commuting per-mode clocks `{n_p}` | clocks commute (resid 0), span rank = `L_s` = 3 |
| **G3** | signed `B₄` → axis image `S₄` | signed exchange `W = P_{a↔b}·diag((−1)^{x_a x_b})` | axis orbit `{0,1,2,3}` transitive, `|image|=24`; unsigned swap NOT a symmetry (resid 22.6) |

## 3. Svenonius symbol-by-symbol (Section B, 5/5 PASS)

| B-AXIS symbol | moved by | undefinable because | witness |
|---|---|---|---|
| **N2b** absolute clock unit `a_τ` | **G1** | rescaled freely while the dimensionless invariant `E_p·a_τ` is fixed (Δ 0) | `a_τ` moves, `E_p·a_τ` fixed |
| **N4** time-axis **label** | **G3** | transitive `S₄` carries axis 0 onto axis 1, hop-invariant (resid 0) | explicit signed `W`, orbit `{0,1,2,3}` |
| **N5** preferred single **clock-ray** in `span_{≥0}{n_p}` | **G2** (+ non-gauge) | `S_{L_s}` maps the `n_0`-ray to the `n_1`-ray; relative flow non-gauge (`n_0` escapes `span{I,Ĥ}`, resid 1.37) | `L_s=3` commuting independent rays |

Each B-AXIS quantity is moved by an automorphism ⇒ **undefinable from A_min**
(Svenonius). This is the independence theorem in its bare-A_min form.

## 4. CRACK CHECK — re-derive `Aut(𝔄)` adjoining each primitive (Section C, 8/8 PASS)

The crucial test the route exists for: does adding an approved primitive as a
premise **shrink** `Aut(𝔄)` enough to **fix** a previously-free quantity?

### C1 — scale_reference (`a^{-1}=M_Pl`, units-only, SPATIAL anchor) — NO CRACK
G1 acts on `(a_τ, Ĥ, Q)`; scale_reference fixes the **spatial** lattice unit `a`.
The dimensionless object G1 would have to fix is the **spacing ratio `a_τ/a`** —
which the primitive note *explicitly disclaims* ("does not supply any dimensionless
quantity"; spacing ratios "live in their own derivation row"). With `a` held fixed,
`T̂²` is still invariant under `a_τ→c·a_τ, Ĥ→Ĥ/c` (Δ `3.4e-17`). **G1 survives;
`a_τ` stays undefinable.** Fixing `a_τ` would require the forbidden spacing-ratio
assertion `a_τ = a`. NO CRACK.

### C2 — kinetic_isotropy (`c_t = c_s`, the SYMMETRIC OS0 form) — NO CRACK (key result)
This closes the open lead flagged in `REFRAMING.md` row A1, which the block02
enrichment search (E1–E8) **never tested**. The runner computes the axis-permutation
image of the kinetic quadratic form `Q(p) = Σ_μ c_μ (lattice Laplacian)_μ` for both
coefficient choices:
- **anisotropic `c_t ≠ c_s`** (`c=[2.5,1,1,1]`): axis image is **S₃-fixing-one** —
  fixes exactly axis 0, permutes `{1,2,3}` transitively. So an anisotropic kinetic
  form WOULD be a genuine one-axis-selector (this is a real new enrichment, not in
  the E1–E8 table).
- **isotropic `c_t = c_s`** (`c=[1,1,1,1]`, **what the primitive actually grants**):
  axis image is **transitive S₄**, orbit `{0,1,2,3}` — fixes no axis.

**Decisive:** kinetic_isotropy supplies the *isotropic* form, i.e. the hypercubic-
symmetric case, which **preserves** `S₄` and selects no axis. The axis-selecting
datum is `c_t ≠ c_s`, which the primitive **does not** supply (and which would be
the emergent-Lorentz *output*, per the primitive note's own anti-circularity
clause). Adding kinetic_isotropy does NOT shrink the axis image. **NO CRACK.**

### C3 — realized_state (pointwise eval at one law-admissible state) — NO CRACK
This closes the open lead in MATH_SECTOR_SEARCH Probe B. The runner confirms Probe
B's facts and then applies the counterfactual policing clause:
- record at the **W-fixed diagonal** locus `(0,0,0,0)`: exchange **preserved**
  (control, resid `4.6e-15`);
- record at the **asymmetric** locus `(1,0,0,0)`: the realized state **does** break
  the exchange (resid 4.24);
- but the signed exchange `W` maps `P_{(1,0,0,0)}` exactly onto `P_{(0,1,0,0)}`
  (resid 0): the two asymmetric loci are **W-conjugate**, so the "selected axis"
  **varies over the law-admissible family** of record loci.

By the realized_state **counterfactual clause** (a number that changes under another
law-admissible state is **registered data, not derivation output**), the
state-dependent axis is **data, not a derived selector**. realized_state grants only
pointwise evaluation; it does not delete G3 from the *structure's* automorphism
group. **NO CRACK.**

## 5. Independence theorem (Section D, 4/4 PASS)

Each B-AXIS quantity is moved by an automorphism that **survives adjoining all three
primitives**:
- **N2b** `a_τ` — moved by G1, which survives scale_reference (spatial-only);
- **N4** time-axis label — moved by G3, whose `S₄` image survives kinetic_isotropy
  (isotropic form is `S₄`-transitive);
- **N5** clock-ray — moved by G2 (`S_{L_s}`), untouched by any primitive; the
  realized-state axis is data.

> **Theorem (R-DEFINABILITY).** On the retained even cubic-symmetric staggered-Dirac
> surface, the absolute clock unit `a_τ` (N2b), the evolution-axis label (N4), and
> the preferred single clock-ray (N5) are each **undefinable** (Beth/Svenonius) from
> `A_min + {scale_reference, kinetic_isotropy, realized_state}`, because each is
> moved by an automorphism of the observable structure that survives adjoining all
> three approved primitives.

**Scope falsifier** (binding on the exact-zero claims): on the **odd** block
`L=(3,3,3,3)` the signed exchange is not even a symmetry (no consistent sign field),
so the transitive-`S₄` fact — and therefore the N4 half — is scoped to **even
cubic-symmetric** blocks, exactly as block02 §10.1 requires.

## 6. Does this correct block02? (one recommended sharpening — not a contradiction)

**corrects_block02 = no** (the no_go's verdict and direction stand; nothing is
overclaimed in a way that flips a result). But the route surfaces **one sharpening**
that should be folded into the unified note's N4 treatment, because block02's E1–E8
enrichment table (§5.2) and its N4 wall wording **never tested the anisotropic
kinetic quadratic form**, and the REFRAMING A1 row explicitly nominated it as a
candidate crack:

> **Recommended sharpening (additive, not corrective):** The block02 headline
> "every A_min enrichment's joint stabilizer is either full-S₄ or trivial; NO A_min
> enrichment has a one-axis-selecting (S₃) stabilizer" is **true as stated for A_min
> enrichments**, but should be sharpened to record that **a one-axis-selecting (S₃)
> enrichment DOES exist** — the anisotropic kinetic form `c_t ≠ c_s` — and that it is
> excluded from the wall not because no S₃ enrichment exists, but because the
> *approved* kinetic_isotropy primitive supplies the **isotropic** `c_t = c_s` form,
> which is `S₄`-transitive. I.e. the N4 wall now rests on a positive premise-level
> fact ("the granted kinetic form is the symmetric one") rather than only on
> "no S₃ enrichment was found." This converts the N4 escape "a richer surface breaks
> W" into a closed statement: the one surface enrichment that *does* break W
> axis-asymmetrically is exactly the one the approved primitive sets to the
> symmetric value.

This makes the wall **stronger**, not weaker, and removes the only open lead
(REFRAMING A1) that the prior blocks left for N4 against the approved primitives.

## 7. Honest status

- **N4** time-axis label: undefinable (independence theorem), even adjoining
  kinetic_isotropy; the would-be crack (anisotropic form) is the value the primitive
  does NOT grant. **Wall confirmed, sharper.**
- **N2b** `a_τ`: undefinable, even adjoining scale_reference (spatial-only; the
  spacing ratio `a_τ/a` is not supplied). **Wall confirmed, sharper.**
- **N5** clock-ray: undefinable, even adjoining realized_state (the realized axis is
  registered data by the counterfactual clause). **Wall confirmed, sharper.**
- **NO CRACK** on any of the three approved primitives.
- This is a no-go about the **retained even-extent surface**, not an impossibility
  proof; each primitive remains a legitimate premise that chain-satisfies without
  bounding. Independent audit lane is the sole status authority.

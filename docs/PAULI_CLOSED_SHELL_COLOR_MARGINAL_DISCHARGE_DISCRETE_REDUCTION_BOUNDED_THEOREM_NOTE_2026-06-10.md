# Pauli/Filling Forces the Color Marginal `I₃/3` in Closed-Shell Sectors — and the Discrete Reduction of Admission (B)

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode attack on admission (B)'s purity core; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_pauli_closed_shell_color_marginal_discharge_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_pauli_closed_shell_color_marginal_discharge_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=16 FAIL=0`, exact, no MC.
A mandatory 4-lens adversarial panel returned `land_with_edits`; **all required edits are
applied**, including the decisive closed-shell narrowing below.

## The admission under attack

The gauge-dynamics campaign consolidated ADM-2's color-depolarization input onto two
admissions; **admission (B)** was *"global color-neutrality"* (blocks 08/09). Its
**orientation** half was retired (#3458); its **purity** half (`Tr ρ²_color = 1/3`,
block 04's order parameter) was shown irreducible to the past hypothesis (#3461). The
mechanism the campaign never used: **the matter is fermionic.**

## The theorems (exact — runner `PASS=16 FAIL=0`)

**(T1) Pauli forces the local singlet at exact full filling.** The 3-fermion sector of a
cell's three color modes is **one-dimensional** — no wavefunction choice exists — and
**all eight** `su(3)` charges annihilate the forced state (residual `0`); its one-body
color matrix is exactly `I₃`. This is the occupancy-forced, second-quantized sharpening of
the representation-theoretic baryon singlet
([`CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02`](CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md),
decoration under the retained `cl3_color_automorphism_theorem`). **"Singlet"/"neutrality"
language applies to this sector only.**

**(T2) Honest catch.** The exactly-full sector is **hopping-frozen** (the color-diagonal
hop annihilates it) — dynamically trivial.

**(T3) Closed-shell discharge (genuine many-body computation).** For the **named**
color-diagonal free hopping (`H = Σ_c h_spat ⊗ |c⟩⟨c|`; the framework's free hopping form,
block 01/#3441 lineage), when the per-color filling is a **closed shell** (non-degenerate
Fermi level — verified: many-body gap `3.0` in the runner's `L=3, n_f=1` instance), the
fixed-`N` ground state is **unique**, and the **measured** color-resolved one-body matrix
at every site — all nine entries, from the actual many-body ground state, nothing
hard-coded — has cross-color coherences **exactly zero** (`2.6×10⁻¹⁷`) and equal diagonal:
`ρ_color(x) = I₃/3` (`10⁻¹⁶`). **Block 04's necessary condition for ADM-2 holds in the
closed-shell sector with zero admissions** (necessary, not sufficient — stated). This is a
property of the *named closed-shell sea*, **not** a claim about which state the physical
vacuum is. Consistent with #3441: free dynamics cannot *create* depolarization; here the
closed-shell sea *is* depolarized and the free flow conserves it.

**(T3b) Open-shell failure — the earned caveat, and the Z³ genericity.** At a degenerate
Fermi level the forcing **fails**: the runner exhibits a state *in the degenerate ground
manifold* (degeneracy `20` in its instance) with per-color counts `(1.98, 1.21, 2.82)` and
`ρ_color(x) ≠ I₃/3` (dev `0.21`) **at the ground energy**. And on `Z³`, **half filling is
generically open-shell** (cubic Fermi-level degeneracies `12` at `L=3`, `20` at `L=4`,
documented in the runner) — the closed-shell discharge does **not** cover the generic `Z³`
half-filled sea. **The color-symmetric selection on the open-shell degenerate manifold is
an extra, weight-like condition: a named residual where the G3/r-dial guard re-opens. It
is not discharged here.**

**(T4) Discrete reduction — two conditions.** On **sharp-count** states (eigenstates of
the three color number operators — number/Cartan-diagonal eigenstates, the defensible
count reading), the color coherences vanish **exactly** (count selection rule), and
`ρ_color(x) = I₃/3` **iff** the registered color counts are **equal *and*** the per-color
local spatial profiles **agree**. Both teeth are exhibited (equal counts + unequal
profiles fails; unequal counts fails outright at dev `0.33`). The excitation residual of
(B)-purity thereby reduces from a continuous singlet/confinement admission to **two
discrete/derived-type conditions**. And — block 17's Fact 3, reproduced —
`ρ_color = I₃/3` is **strictly weaker** than global neutrality (`|F⟩ = Σ_i|i⟩|i⟩/√3` has
`ρ_A = I₃/3` with total `su(3)` charge residual `1.63`): this note forces only the
**marginal** condition, except at exact full filling (T1).

## The ledger for admission (B) after this note

```
orientation        RETIRED   (#3458, predictive equivalence)
purity, closed-shell sectors   DISCHARGED here (zero admissions; measured)
purity, exact full filling     FORCED (T1) — at the price of frozen dynamics (T2)
purity, open shells (generic Z³ half filling)
                   NAMED RESIDUAL: the degenerate-manifold selection — weight-like,
                   G3 guard re-opens; NOT discharged
purity, excitations (sharp-count)
                   REDUCED to: count equality AND profile agreement (discrete)
```

## What this does NOT claim

- **No ADM-2 sufficiency** (block 04's condition is necessary only; the step-measure
  question is the mapped wall). **No confinement derivation.** **No claim about which
  state the physical vacuum is** (the staggered realization gate is the existing separate
  lane). The symmetric-base→physical-SM-color bridge boundary is inherited exactly as the
  baryon-singlet note records it; the supplied `C³` carrier conditionality as throughout.
- The open-shell residual is **not** minimized: on `Z³` it is the *generic* case, and its
  resolution (a selection on the degenerate manifold) is exactly the kind of weight-like
  input the framework's G3 guard exists to police.
- No new axiom, primitive, measure, or weight is introduced. `r` is untouched (it lives in
  the generation factor; no part of this argument reaches it).

## Cross-references

- The admission attacked: blocks 08/09 (PRs #3445/#3449); orientation retirement #3458;
  purity irreducibility #3461; block 04's necessary condition #3431 (all on main).
- The representation singlet (sharpened by T1): [`CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02`](CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md)
- Free-hopping color conservation (consistent with T3): #3441 (on main).
- Pauli irrep support (retained): [`CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10`](CL3_PAULI_IRREP_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
- Standard math (method only): second quantization / Jordan–Wigner; Slater determinants;
  closed/open shells; number-operator selection rules.

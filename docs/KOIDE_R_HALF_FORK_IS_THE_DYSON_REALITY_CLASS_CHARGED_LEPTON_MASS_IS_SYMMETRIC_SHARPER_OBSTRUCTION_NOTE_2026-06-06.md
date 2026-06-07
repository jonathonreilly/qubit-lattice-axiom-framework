# The Koide r=1/2 Fork Is the Dyson Reality Class — the K/CPT-Real Charged-Lepton Mass Is Symmetric (Determinant, Not Pfaffian), So r=1 (Sharper Obstruction)

**Date:** 2026-06-06
**Type:** bounded obstruction note (sharper obstruction; relocation + foreclosure of the one open derivation lever)
**Claim type:** bounded_obstruction
**Status authority:** independent audit lane only. This source note does not assert an audit verdict or effective-status change.
**Runner:** [`scripts/audit_companion_koide_dyson_reality_class_sharper_obstruction_exact.py`](../scripts/audit_companion_koide_dyson_reality_class_sharper_obstruction_exact.py) (sympy, 12/12 exact)

## Result

The one genuinely open lever to **derive** the charged-lepton Koide magnitude `r = |b|²/a² = 1/2`
(`Q = 2/3`) — the multiplicity-stripped `det_C` / Kähler-Dirac index reading, localized but left **open**
in [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md) — is **foreclosed for charged leptons**. The fork `det_C`-vs-`det_R` is reframed,
and then closed, by the **Dyson reality class** of the doublet mass bilinear:

| reading | object | homogeneity degree | doublet counted | result | reality class |
|---|---|---|---|---|---|
| `det_R` | determinant | **2** | twice | `r = 1` (`Q = 1`) | **Dirac / symmetric** |
| `det_C` | Pfaffian `= √det` | **1** | once | `r = 1/2` (`Q = 2/3`) | **Majorana / antisymmetric** |

The decisive facts (all reproven from the C₃ primitive in the runner):

1. **The fork is discrete, not a measure.** `det_C` (count once, `r=1/2`) is the **Pfaffian**; `det_R`
   (count twice, `r=1`) is the **determinant**. They differ only in homogeneity degree (1 vs 2). The
   Pfaffian exists **only** for an **antisymmetric** bilinear (real-structure square `K² = −1`,
   quaternionic). This is a **discrete Z₂ / Dyson-class** distinction — untouched by the continuous
   `J_cs` measure-neutrality (`exp(θ J_cs) = SO(2)`) that forecloses every *continuous* selector.
   Runner (1).
2. **The physical mass is symmetric.** The K/CPT-real generation mass `M = aI + bC + b̄C²` is **Hermitian**
   with **distinct** real doublet eigenvalues `a − b_r ∓ √3·b_i` (distinct for `b_i ≠ 0` — exactly what
   gives `m_μ ≠ m_τ`), built along **`i·J_cs`**, the **Hermitian/symmetric** partner of the antisymmetric
   `J_cs`. A symmetric block has a **determinant** and **no Pfaffian**. Runner (2),(3),(4).
3. **No antisymmetric structure on the split doublet.** Any `J` commuting with `diag(λ₁,λ₂)`, `λ₁ ≠ λ₂`,
   is **diagonal**, so `J² ≥ 0` — never `−1`. The `K² = −1` (quaternionic/Pfaffian) ingredient that
   `det_C/r=1/2` needs **cannot live** on the distinct-eigenvalue doublet. The Pfaffian reading is not
   merely unselected — it is **undefined** for the physical mass operator. Runner (5).
4. **Electric charge forbids it outright.** A Majorana mass is a `ψᵀCψ` bilinear carrying `ΔQ = 2·Q`; for a
   charge `−1` charged lepton `ΔQ = −2 ≠ 0`, **forbidden by `U(1)_em`**. So the charged-lepton mass is
   **Dirac** (`ψ̄ψ`, symmetric) → `det_R` → `r = 1`, with **no freedom** for the `det_C/Pfaffian` (`r=1/2`)
   structure — **independent of the staggered realization**. Runner (6).
5. **Three convergent independent arguments.** The Coleman-Weinberg fluctuation modulus (rank-2 Hessian),
   the KO-mod-2 Dyson/Pfaffian parity (orthogonal `K²=+1` → even → no canonical √det), and the Berezin
   homogeneity degree (degree 2) **all** return the doublet's count-twice reading → `r = 1`, and **all**
   name the **same** missing ingredient: an antisymmetric/quaternionic `K² = −1` structure on the doublet,
   which (3) and (4) exclude. Runner (7).

## The reframe: what changed

The standing question was framed as a **dynamics** choice (`KOIDE_R_HALF_INDEX_READOUT`):

> Is the charged-lepton generation determinant **first-order** (a Dirac/Berezin / Kähler-Dirac index,
> count once → `r=1/2`) or **second-order** (the fluctuation modulus, count twice → `r=1`)? — *open,
> gated on the staggered-Dirac corner realization (`AC_φλ`).*

A multi-perspective reframing (ten distinct physicist/logician lenses — families-index/KO, Seiberg-holomorphy
skeptic, chirality/domain-wall, determinant-line-bundle, K/CPT-Wedderburn, readout-logic, staggered-rooting,
APS/η-spectral, well-posedness, contrarian) converged on a sharper object: **first-order-vs-second-order is the
Dyson reality class** of the doublet mass — Pfaffian (Majorana/antisymmetric) vs determinant (Dirac/symmetric).
That converts the open dynamics gate into a **finite, decidable, charge-determined** question, and the answer
is forced:

- The "first-order index / count once" `det_C` reading **is** the Pfaffian, which **needs** the antisymmetric
  structure;
- the K/CPT-real charged-lepton mass is **symmetric** and its split spectrum **excludes** any antisymmetric
  structure;
- and **electric charge forbids** the Majorana/antisymmetric mass for a charged lepton regardless of the
  lattice realization.

So the `AC_φλ` staggered realization cannot deliver `det_C/r=1/2` for the **charged** leptons: a charged
particle is Dirac by charge conservation, full stop. This is **consistent with and explains** the earlier
finding that chirality moves only the determinant **phase** `δ`, not the magnitude `r`
([`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](./KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)):
the magnitude lives on the **Dyson class** (the real-structure square `K²`), a **different** invariant from
the chirality grading `γ₅`, and charge fixes it to the symmetric/Dirac/`det_R` class.

## Scope — what this is and is not

- This is a **negative** result for the campaign goal. It does **not** derive `r = 1/2`; it **forecloses**
  the `det_C` lever that would have. The framework's native readout forces **`r = 1` (`Q = 1`)** for the
  charged leptons; the empirical **`Q = 2/3`** is the framework's **partial-falsification**, now **derived**
  (via the Dyson class + electric charge) rather than merely the "natural default readout."
- It is a **sharper obstruction**, not a metaphysical impossibility theorem. The honest residual is the
  formal `AC_φλ` staggered realization: a complete closure would exhibit the realized charged-lepton corner
  mass as a Dirac bilinear at the lattice level. But that residual **cannot** evade charge conservation — a
  charge `−1` field has no `ΔQ = −2` Majorana mass — so the residual is narrow and charge-foreclosed.
- It corrects an over-optimistic earlier salvage. The reading "`det_C` is natively available via the
  chirality grading, gated only on `AC_φλ`" (the `information-minimization` salvage; `KOIDE_R_HALF_INDEX_READOUT`)
  is **too strong**: even granting the chirality grading, `det_C` is the **Pfaffian**, which needs an
  antisymmetric structure the symmetric K/CPT-real mass lacks and charge forbids.
- It says nothing about **neutrinos**. Neutrinos are electrically neutral, so the charge foreclosure (4) does
  **not** apply to them — a Majorana/Pfaffian neutrino mass is `ΔQ = 0`-allowed. The Dyson-class reframe is
  therefore a **prediction surface** for the neutrino sector (whether the neutrino generation mass is
  Dirac/`det_R` or Majorana/`det_C`), not a foreclosure there.

## Forbidden-import / reprove-and-cite discipline

- The Dyson fork (Pfaffian = √det, degree 1 vs 2), `J_cs` antisymmetry and `J_cs² = −P_doublet`, the
  `i·J_cs` Hermiticity and `{−1,0,+1}` spectrum, the Hermiticity and distinct doublet spectrum of `M`, the
  no-antisymmetric-structure-on-a-split-doublet lemma, the electric-charge bookkeeping, and the Koide
  arithmetic are all **reproven** from the C₃ primitive in the runner (sympy, 12/12 exact).
- The **Dyson threefold-way** (orthogonal/unitary/symplectic real-structure classes), the
  **Majorana↔Pfaffian / Dirac↔determinant** fermion-path-integral facts, **McKean-Singer**, and
  **KO/Bott periodicity** are **comparators** only (named for provenance and cross-check), never derivation
  inputs.
- No PDG values appear. `Q = 2/3` (empirical) and `Q = 1` (framework-forced) are named only as the target
  and the forced value; this note does **not** derive `r = 1/2`.

## No-go discipline (routes explored)

The obstruction is reached by **four** independent arguments (Coleman-Weinberg modulus, KO-mod-2 Dyson
parity, Berezin homogeneity degree, electric charge) and was stress-tested across **ten** distinct
reframing lenses plus five adversarial derive-or-refute attacks; the two reframings that initially looked
like routes to `r=1/2` (Wedderburn reduced-norm; Berezin Pfaffian) were each shown to be undefined on the
non-degenerate physical operator (they require the degenerate `b_i = 0` limit, `m_μ = m_τ`) or to require
swapping the symmetric mass for a different antisymmetric action term. The steelman of `r=1/2` surviving —
a staggered realization producing a Majorana charged-lepton mass — is excluded by electric charge.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md`](./KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md)
- [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](./KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
- [`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`](./KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md)
- [`KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md`](./KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md)
- [`FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md`](./FLAVOR_RECORD_READOUT_FORM_NOT_WEIGHT_2026-06-02.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](./STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)

**Independent audit required.** This note asserts no effective-status change.

# Chirality Gate — Definitive Import Characterization

**Date:** 2026-06-05
**Claim type:** meta
**Status authority:** independent audit lane only. This note sets no audit
verdict, proposes no axiom/primitive/admission, and derives no Koide value. It
is a grounding characterization of an existing gate against the committed
`origin/main` ledger.
**Runner:** `scripts/audit_companion_chirality_gate_import_characterization_2026_06_05.py`
(SCORECARD: PART_A=PASS PART_B=PASS).
**Cached log:** `logs/runner-cache/audit_companion_chirality_gate_import_characterization_2026_06_05.txt`

## Purpose

State, precisely and with every status checked against the committed ledger, the
single irreducible import that the charged-lepton Koide result `r=1/2` (`Q=2/3`)
reduces to. This is grounding, **not** closure: the deliverable is a clean
audited characterization of what is missing, plus the open-vs-closed status of
every escape-hatch the no-go notes themselves flag.

## 1. Audited status of the gate spine (verified vs committed ledger)

All rows below were read from `docs/audit/data/audit_ledger.json` at
`origin/main` and re-checked by PART B of the runner.

| claim_id | effective_status | role |
|---|---|---|
| `koide_anticommuting_operator_derivation_theorem_note_2026-05-10` | **retained** | `{H,Γ_χ}=0` ⇒ `Q=2/3` (the sufficiency theorem) |
| `koide_circulant_value_derivation_2026-06-05` | unaudited | circulant `Q=1/3+(2/3)r`; `r=1/2 ⇒ Q=2/3` (the value formula) |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | **retained_bounded** | circulant trap: `[H,R]=0 ∧ {H,Γ_χ}=0 ⇒ H=0` |
| `flavor_emergent_chirality_no_transport_note_2026-05-30` | **audited_conditional** | the 4-candidate table; native fillings all fail |
| `flavor_generation_space_bridge_reduces_to_open_gate_2026-05-31` | **audited_conditional** | value-construction survives the no-go; gap = promotion premise |
| `flavor_chirality_gate_narrows_to_one_spin_statistics_import_2026-05-31` | **retained_bounded** | scope-repaired 2026-06-04; **disclaims** "single import closes flavor" |
| `staggered_axis_symmetry_is_s3_narrow_theorem_note_2026-05-23` | **retained_bounded** | spatial symmetry on generation corners is `S_3` |
| `parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23` | **retained_bounded** | spacetime parity is generation-blind |
| `lepton_brannen_bae_delta_two_ninths_open_gate_note_2026-05-26` | **open_gate** | the named residual the bridge reduces to |
| `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29` | **retained** | signed vs singular-value readout split (RE-AUDITED clean 2026-06-05) |
| `staggered_dirac_realization_gate_note_2026-05-03` | open_gate (`audited_renaming`) | canonical parent for the staggered-Dirac realization |
| `closure_c_staggered_dirac_gate_note_2026-05-10_cstaggered` | unaudited | staggered-Dirac gate child |
| `flavor_hw1_staggered_projection_democratic_r0_2026-06-02` | unaudited (`no_go`) | hw=1 staggered projection gives `r=0`, not `1/2` |
| `koide_factor_split_does_not_force_carrier_value_bridge_no_go_note_2026-06-02` | unaudited (`no_go`) | tensor-factor split does not force the carrier↔value bridge |

Stale-memory corrections found while grounding:
- **The "framework default gives `Q=1`" shorthand is imprecise.** Per the
  unaudited-but-committed `koide_circulant_value_derivation_2026-06-05`, the
  C₃-equivariant circulant gives the **one-parameter family** `Q=1/3+(2/3)r`.
  `Q=1` is only the `r=1` (Born/per-dimension) endpoint; `r=0` gives `1/3`;
  **`r=1/2` gives `2/3`.** The circulant default reaches `2/3` at one dial value.
- `koide_signed_eigenvalue_vs_singular_value_readout` is **retained**
  (`audited_clean`, 2026-06-05) — the `audited_failed` label cited by the
  2026-05-31 bridge note (Finding C) is **stale**.
- `anomaly_forces_time`, `a3_route3` (cited in older memory as "retained")
  are meta/unaudited — confirmed NOT load-bearing here.

## 2. The single import — stated precisely

The retained sufficiency theorem says `{H,Γ_χ}=0 ⇒ Q=2/3`, with
`Γ_χ=(2/3)J−I` (real-symmetric involution, signature **(1,2)**: `+1` on the
`(1,1,1)` singlet, `−1` on the transverse doublet). The framework supplies the
generation factor `R³` carrying the `C_3` regular representation
(`koide_generation_id_cl3_grade1_bridge`, retained_bounded) and a `K/CPT`-real
mass operator. What it does **not** supply is exactly one object. There are two
equivalent faces of it (runner PART A verifies both):

> **The lepton `r=1/2` result needs exactly THIS import: a single distinguished
> choice on the generation factor `R³` that lands the equal-Wedderburn-block
> point `a² = 2|b|²` (`r=|b|²/a²=1/2`) of the `K/CPT`-real generation mass
> operator — equivalently, a Hermitian off-block `Γ_χ`-anticommuting grading
> that intertwines the singlet and doublet eigenspaces. This object breaks
> `C_3`-equivariance and is absent from A1+A2+retained.**

Two faces, one missing object:

- **Anticommuting (operator) face** — a nonzero real-symmetric `H` with
  `{H,Γ_χ}=0`. Runner A3/A5: any such `H` is **purely off-block** (its
  block-diagonal part vanishes; it is a singlet↔doublet intertwiner) and lands
  `Q=2/3` via the eigenvector route `⟨v|Γ_χ|v⟩=0`. The circulant trap (A4,
  retained_bounded no-go) shows such `H` **must break `C_3`-equivariance**.
- **Dial-selection (value) face** — the circulant `Y=aI+bC+b̄C²`
  **commutes** with `Γ_χ` (runner A6b: `[Y,Γ_χ]=0`) and gives `Q=1/3+(2/3)r`.
  Selecting `r=1/2` (equal block power; the involution `r↦1/(4r)` fixed point)
  yields `Q=2/3` with no anticommutation. The missing object here is the
  **selection of the dial value `r=1/2`**, which is a free flavor input.

The faces are distinct operators (the off-block `H` vs. the commuting circulant
at `r=1/2`); they coincide only in the value `Q=2/3`. Either one, if supplied,
closes the lepton gate. **The minimal description of the import: a `C_3`-orbit-
splitting datum on `R³` — either the off-block grading or the `r=1/2`
dial-fix — that is not forced by lattice locality (A2), the qubit algebra (A1),
or any retained structure.**

## 3. Escape-hatches the notes flag — open vs closed

| hatch | source note | status |
|---|---|---|
| "wrong tensor factor": Connes-Lott `γ_CL=I₃⊗σ₃` on `R³⊗(H_L⊕H_R)` | emergent-chirality-no-transport (audited_conditional) | **CLOSED (inert)** — runner A7: `{G⊗σ₁, I₃⊗σ₃}=0` for *every* `G`; the grading places **zero** constraint on `R³`; the `C₃`-breaking is the hand-inserted `H_anti` import |
| emergent-time × emergent-chirality transport `Θ→slice→R³` | emergent-chirality-no-transport (audited_conditional) | **CLOSED** — the carrier factorizes `Ξ=Θ⊗V`; no generation index; acts as identity on `R³` |
| cube-volume / Hamming chirality `ε=(−1)^{x+y+z}` | emergent-chirality-no-transport; hw1-democratic (no_go) | **CLOSED** — `ε|hw1=−I₃` is scalar, commutes with `R` and `Γ_χ`; S₃-invariant, cannot split the orbit; hw=1 projection gives `r=0` |
| `C₃→S₂` transposition-broken operator on the same `R³` | emergent-chirality-no-transport (audited_conditional) | **OPEN but is the import itself** — it does anticommute and break `C₃`, but selecting the transposition `τ` is precisely the external import (not native) |
| tensor-factor split forces carrier↔value bridge | factor-split no-go (unaudited) | **CLOSED** — all four joint sign sectors nonempty; the bridge is an extra welding link, not a consequence of factorization |
| staggered-Dirac realization supplies a native chiral mass op | staggered-Dirac realization gate (open_gate); KS rescoping (unaudited) | **OPEN** — the canonical parent gate is unclosed; no native realization yet produces the off-block/`r=1/2` datum |
| equivariant APS-η / `Z_N` spectral-asymmetry route (`L₃(1,2)=2/9`) | generation-space-bridge (audited_conditional); `axiom_first_z_n_…` (retained_bounded) | **OPEN, named** — value-construction is unobstructed by the no-go, but reduces to the `open_gate` `lepton_brannen_bae_delta_two_ninths` (promote an intensive summand of a vanishing extensive invariant to an observable) |
| chiral/holomorphic supertrace counts complex `b` once → `r=1/2` | supertrace-index lead (unaudited, open_gate); `koide_r_reduces_to_chiral_vs_vector_yukawa_binary` (unaudited) | **OPEN, named** — gated by the same staggered-Dirac mass/Yukawa realization; does not yet show the framework determinant is chiral |

## 4. Verdict

The lepton `r=1/2` result needs exactly the import in §2: **a `C₃`-orbit-splitting
datum on the generation `R³` (off-block `Γ_χ`-anticommuting grading, equivalently
the `r=1/2` dial-fix on the commuting circulant), absent from A1+A2+retained.**
It is **irreducible against every CLOSED hatch** (the inert wrong-factor grading,
emergent-time transport, the S₃-invariant Hamming chirality, the factor-split
bridge). It remains **open via three named hatches** that are live but unclosed
on the surface: the **staggered-Dirac realization gate** (open_gate parent), the
**equivariant APS-η / 2/9 promotion** (reduces to `lepton_brannen_bae_delta_two_ninths`,
open_gate), and the **chiral-vs-vector supertrace** route (unaudited lead). None
of these is closed; each is a path the gate opens, not a wall around it.

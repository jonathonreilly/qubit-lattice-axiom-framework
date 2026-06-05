# Staggered-Dirac Realization Gate — Current-State Map & Two-Wall Airtight/Gap Audit

**Date:** 2026-06-05
**Claim type:** meta
**Status authority:** independent audit lane only. This is a navigation /
state-map note. It sets no audit status, derives no theorem, imports
nothing. All `effective_status` values below were read from
`git show origin/main:docs/audit/data/audit_ledger.json` (not from
memory) at `origin/main` SHA `a090bac38`.
**Runner:** none required (state-map note; the cited runners are the
load-bearing ones and all pass on `origin/main` — see §4).

---

## 0. One-paragraph answer

The staggered-Dirac realization gate is **kinetic-and-algebra-closed,
mass/Yukawa-open**. Substeps 1–3 (Grassmann forcing → Kawamoto-Smit
phases → 1+1+3+3 BZ-corner Hamming decomposition with hw=1 `M_3(C)`)
are a bounded chain on retained authorities; the open piece is
**substep 4**, which splits into (a) `AC_φλ`, the *species-label*
identification (which corner ↔ which lepton), a `no_go`-within-A_min
with three named external-input closure routes; and (b) the
**mass/Yukawa fluctuation-determinant readout** (chiral/holomorphic vs
vector/real), which is the bit that decides Koide `r=|b|²/a²`. The
kinetic operator is built; its **mass term is not** — and the r=1/2
question is *explicitly gated on that missing mass structure* (the
2026-06-04 holomorphic supertrace open lead). **Verdict:** the
staggered-Dirac gate genuinely IS the route that would close r=1/2 (not
a relabel of the same import), and **both walls have a precisely-named
gap, not airtightness** — though every *boundary/APS-eta/GW* escape
tried at finite level has so far returned neutral.

---

## 1. Current-state map (verified statuses)

### 1.1 The gate parent and the closure surface

| Note (CID) | claim_type | effective_status | role |
|---|---|---|---|
| `staggered_dirac_realization_gate_note_2026-05-03` | open_gate | **audited_renaming** (criticality=critical, step-class E, chain_closes=False) | canonical open-gate *parent identity*; pure-meta packaging |
| `closure_c_staggered_dirac_gate_note_2026-05-10` | open_gate | unaudited | C8 assembly + **order-one `D_F` selection** open piece (NCG framing) |
| `staggered_dirac_gate_closure_synthesis_theorem_note_2026-05-17` | bounded_theorem | unaudited | end-to-end bounded chain T2→T3→T4→T5 for substeps 1+2+3 |

### 1.2 The four substeps (the substantive content)

| Substep | Source note (CID) | effective_status |
|---|---|---|
| 1 Grassmann forcing | `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | **retained_bounded** |
| 1 Jordan-Wigner CAR bridge | `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | retained_pending_chain (decoration) |
| 1 statistics-agnostic discriminator | `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | **retained_no_go** |
| 2 Kähler-Dirac equivalence | `staggered_dirac_substep2_kahler_dirac_equivalence_narrow_theorem_note_2026-05-17` | **retained_bounded** |
| 3 BZ-corner Hamming orbit | `staggered_dirac_substep3_bz_corner_hamming_orbit_narrow_theorem_note_2026-05-17` | **retained** (positive_theorem) |
| 3 species-reduction bridge | `staggered_dirac_substep3_species_reduction_bridge_narrow_theorem_note_2026-05-16` | **retained_bounded** |
| 4 AC_λ simul-diag bridge | `staggered_dirac_substep4_ac_lambda_simultaneous_diagonalization_bridge_narrow_theorem_note_2026-05-17` | **retained** (positive_theorem) |
| 4 AC narrowing (bounded) | `staggered_dirac_substep4_ac_narrow_bounded_note_2026-05-07` | unaudited (criticality=critical) |
| 4 labeling no-go (`AC_φλ`) | `staggered_dirac_substep4_labeling_no_go_note_2026-05-17` | unaudited |

**So:** substeps 1, 2, 3 are largely **retained / retained_bounded**
positive content. **The open piece is substep 4**, and it has two
distinct residuals — not one.

### 1.3 The TWO substep-4 residuals (the load-bearing distinction)

1. **`AC_φλ` (species label).** "Is corner `c_α` the electron, the muon,
   or the tau?" Formal `no_go` within A_min via orbit-equivariance under
   `C_3`: π_A vs π_B (identity vs one-cycle relabeling) are
   A_min-indistinguishable; closure needs P1 (labeling convention,
   bounded/recommended), P2 (`C_3`-breaking dynamics, rejected within
   A_min by the 10-probe A3 campaign), or P3 (PDG, forbidden). **This is
   NOT the r=1/2 wall** — it is a permutation/naming residual.

2. **Mass/Yukawa fluctuation-determinant readout.** The Koide value
   `r=|b|²/a²` is set by *how the generation fluctuation determinant
   counts the complex doublet coefficient `b`*: a **chiral/holomorphic**
   count weights `b` once → `(1,1)` → r=1/2 → Q=2/3; a **vector/real**
   count weights `(Re b, Im b)` separately → `(1,2)` → r=1 → Q=1
   (`supertrace_index_holomorphic_route_to_koide_r_half_open_lead_note_2026-06-04`,
   unaudited open_gate; refined by `koide_r_reduces_to_chiral_vs_vector_yukawa_binary_*`).

**The r=1/2 ⇄ gate connection (Task-1 deliverable):** the chiral-vs-vector
readout is *explicitly gated on the open substep-4 staggered-Dirac
**mass/Yukawa** structure*. Quoting the open-lead note: the kinetic
`{ε,D}=0` chirality "is suggestive but does not by itself fix the
fluctuation determinant's holomorphy"; deciding it "requires the gated
staggered-Dirac mass/Yukawa structure (kinetic-only on main; mass at the
open substep-4 gate)." **The gate's open piece and r=1/2 are the same
gate.**

---

## 2. Wall W1 — "d=3+1 Dirac gapped → index 0 → no chirality grading"

**Where it actually lives:** not a standalone note. The mechanism is
`abj_residual_gw_not_necessary_narrow_theorem_note_2026-05-28`
(**retained_bounded**) + `axiom_first_lattice_wz_fujikawa_narrow_theorem_note_2026-05-26`
(**retained_bounded**), both resting on the sole load-bearing dep
`cpt_exact_note` (**retained**). The exact statement: with
`{ε,D}=0`, `K:=εD` Hermitian, `H(m)=K−mε` obeys the operator identity
`H(m)² = K² + m²I` ⇒ `min|spec H(m)| = |m|` ⇒ spectral flow `≡ 0`
(K¹/η index), and `A[1,U]=Tr[ε e^{−tD†D}] = 0` (χ=0 by ±pairing).

**Is it airtight in the FULL realization (emergent time, full operator)?**
The bulk-gap part is **dimension-robust**: the note's "Dimension
independence" section proves `H(m)² = K² + m²I` follows purely from
`{ε,D}=0`, `ε²=I`, `K=εD` Hermitian, so it holds for the physical d=3+1
(`Z³` space + emergent time) reading equally (`H(m)² = |k|² + m²`). So
the emergent-time structure does **not** by itself evade the bulk gap.

**But the wall is NOT airtight — it has a precisely-named gap.** The
retained note itself carries the open residual:

> **`(P1'-sharpened)`: exhibit a framework-internal background of
> nontrivial topology (`χ≠0`) or nonzero gauge topological charge
> (`Q≠0`) on which the staggered chiral index `A[1,U]` is non-zero.**

The index-0 result is proven **only on the free/flat background**. A
topologically nontrivial / nonzero-`Q` background is **untested**, and
the prior "must import overlap (GW)" attribution was *retracted* (GW is
sufficient, not necessary — Fukaya-η/`K¹` and Catterall Kähler-Dirac
both give a lattice index with no GW; Catterall's `U(1)→Z_4` 't Hooft
anomaly is exposed precisely in curved space, `χ≠0`).

**Two natural escapes were already tried at finite level and returned
neutral** (so the gap is real but narrow):
- **APS-η / boundary mode:** `signed_gravity_staggered_dirac_aps_boundary_realization_note`
  (unaudited; runner PASS=7) tested the *staggered* boundary operator
  `H_stag = Σ η_μ(x)(−i/2)[shift±] + m·ε(x)` on cycles/tori/open faces.
  Verdict **η-neutral** (`FINAL_TAG: ..._NOT_CONTAINED`). The tempting
  odd-open-face `η=±1` is **quarantined as a sublattice-imbalance
  artifact** (flips under one-site origin shift; dies under
  even/taste-compatible refinement). The Pfaffian sign is
  determinant-line orientation metadata, not a gauge-invariant `χ_η`.

**W1 verdict — HAS-A-NAMED-GAP.** Named gap = *a `χ≠0` / `Q≠0`
(topologically nontrivial / curved / nonzero-flux) background on which
the staggered chiral index is nonzero.* The flat/free index-0 is
airtight and dimension-robust; the boundary/APS-η escape is
finite-level-closed; the live opening is the nonzero-topological-charge
background — the framework HAS APS-η machinery but has not yet exhibited
the nonzero-χ instance.

---

## 3. Wall S3 — "ε=(−1)^{hw}=−1 uniform on hw=1 → can't grade generations"

**Where it actually lives:** `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16`
(**retained_bounded**), supported by `no_per_site_chirality_theorem_note_2026-05-02`
(**retained_no_go**: no γ₅ inside per-site `M_2(C)`). Exact statement:
`comm(R) ∩ anticomm(Γ_χ) = {0}` in `Sym(R³)`, where `R` is the cyclic
shift and `Γ_χ=(2/3)J−I`. Reason: `Γ_χ` is itself a circulant
(`=−⅓I+⅔R+⅔R²`), so any `C_3`-equivariant Hermitian `H` *commutes* with
it; anticommutation then forces `HΓ_χ=0`, and the invertible `Z_3`
Fourier transform kills it. (The S3-spatial-parity statement `ε=(−1)^{hw}`
uniform on the hw=1 orbit is the same obstruction in the spatial-parity
guise: a generation-grading must break the `C_3`/`S_3` symmetry the orbit
is built from.)

**Is it airtight given the FULL spin-taste structure?** **No — the
retained note names two explicit escape hatches, both OPEN:**
- **(I)** drop `C_3`-equivariance of `D` on the single `R³` factor (then
  the specific `h` becomes an external input);
- **(II)** a **multi-factor** Hilbert space where the spectral-triple
  γ-grading lives on a tensor factor *distinct* from where `Γ_χ` acts —
  e.g. `H = R³ ⊗ (H_L ⊕ H_R)`, `γ_CL = I₃ ⊗ σ₃`. The single-factor
  theorem does **not** apply; the off-diagonal Yukawa on `R³` is
  unconstrained by chirality anticommutation. **A separate bridge
  theorem connecting Connes-Lott anticommutation to the generation
  factor is needed and not built.** The spin-taste cube IS such a
  multi-factor structure (taste ⊗ generation), so this is exactly the
  unexplored door.

**Decisive 2026-06-04 reframe (changes the target of the wall):** the
S3/`C_3` argument constrains operators that would grade *magnitude* `r`.
But the frontier correction
`koide_fluctuation_modulus_gives_r_one_chirality_is_phase_only_frontier_correction_note_2026-06-04`
(unaudited no_go) found the *tested* Hermitian `C_3`-circulant modulus
is rank-2 vector → r=1, **and explicitly redirects the chiral/η
information toward `arg(b)=δ` (the phase) rather than the modulus `r`**:
"A phase effect such as an eta-invariant would affect determinant phase
/ `arg(b)`, not the tested modulus ratio." So the S3-uniform-parity
no-go may be addressing r through the *wrong channel*: in a holomorphic
(complex-mode-count) readout the doublet `b` is counted once → `(1,1)`
→ r=1/2 *without* a `C_3`-breaking Hermitian operator on `R³` — the
mechanism the no-go forbids is not the only mechanism on the table.

**S3 verdict — HAS-A-NAMED-GAP (two gaps).** (i) Multi-factor
spin-taste structure where the chiral grading lives on the taste factor,
not the generation `R³` factor (escape-hatch II; bridge theorem
unbuilt). (ii) The holomorphic/complex-mode-count readout, which reaches
`(1,1)` → r=1/2 without any `C_3`-equivariant anticommuting Hermitian
operator, so the `comm∩anticomm={0}` identity does not foreclose it.
The retained identity is airtight **only** for the literal single-factor
`γ=Γ_χ` + `C_3`-equivariant-Hermitian construction — exactly the scope
its own §4–§5 disclaim.

---

## 4. Honest top-line verdict

- **Is the staggered-Dirac gate the route that would close r=1/2, or does
  it reduce to the same import?** It is **genuinely the route** — not a
  relabel. r=1/2 is the chiral-vs-vector fluctuation-determinant binary,
  and that binary is *defined to be decided by* the gate's open substep-4
  **mass/Yukawa** structure (the kinetic operator alone, present on main,
  is insufficient: `{ε,D}=0` is suggestive but does not fix holomorphy).
  Closing the gate's mass realization is *exactly* what would supply the
  chiral-vs-vector verdict; the gate does not merely re-host the `AC_φλ`
  labeling import. (The `AC_φλ` labeling residual is a *separate*,
  permutation-only admission and does **not** carry the r=1/2 content.)

- **W1:** **HAS-A-NAMED-GAP.** Gap = a `χ≠0` / `Q≠0` topologically
  nontrivial (curved / nonzero-flux) background with nonzero staggered
  chiral index. Flat/free index-0 is airtight and d-3+1-robust; the
  APS-η boundary escape is finite-level-closed (η-neutral, odd-face
  quarantined); GW-necessity is *false*. The framework has APS-η /
  Fujikawa machinery but has not exhibited the nonzero-χ instance.

- **S3:** **HAS-A-NAMED-GAP.** Gaps = (i) multi-factor spin-taste
  construction (chiral grading on the taste factor, not generation `R³`)
  — escape-hatch II of the retained no-go, bridge unbuilt; (ii) the
  holomorphic/complex-mode readout that reaches r=1/2 without a
  `C_3`-equivariant Hermitian anticommutator, plus the 2026-06-04
  finding that η/chirality plausibly governs `arg(b)` not `r` — so the
  S3-uniform argument may target the wrong (modulus vs phase) channel.

**Neither wall is airtight in the full realization.** Both are airtight
*only within their stated narrow scope* (W1: flat/free background; S3:
single-factor `γ=Γ_χ` + `C_3`-equivariant Hermitian). The full
realization's open mass/Yukawa structure on a multi-factor spin-taste
Hilbert space, read holomorphically and/or on a nonzero-topological-charge
background, is the live target — which is precisely the still-open
substep-4 gate. These named gaps are what the parallel fresh attacks
should aim at; none is a closed search space.

---

## 5. Load-bearing runners (all PASS on origin/main `a090bac38`)

| Wall / piece | Runner | Result |
|---|---|---|
| W1 ε-gap + χ=0 | `scripts/abj_residual_gw_not_necessary_runner.py` | PASS=36 FAIL=0 |
| W1 finite Z4 grading | `scripts/frontier_lattice_wess_zumino_fujikawa_narrow_verifier.py` | PASS=58 FAIL=0 (per note) |
| W1 APS-η boundary escape | `scripts/signed_gravity_staggered_dirac_boundary_eta_realization.py` | PASS=7; `..._NOT_CONTAINED` |
| S3 `comm∩anticomm={0}` | `scripts/frontier_koide_z3_equivariant_anticommuting_no_go.py` | dominant_class A (verified) |

## 6. Cross-references (plain text; navigation only, not upstream deps)

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (parent gate)
- `STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md`
- `STAGGERED_DIRAC_SUBSTEP4_LABELING_NO_GO_NOTE_2026-05-17.md` (`AC_φλ`)
- `SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`
- `KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04.md`
- `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28.md` (W1 mechanism + `(P1')` residual)
- `AXIOM_FIRST_LATTICE_WZ_FUJIKAWA_NARROW_THEOREM_NOTE_2026-05-26.md`
- `SIGNED_GRAVITY_STAGGERED_DIRAC_APS_BOUNDARY_REALIZATION_NOTE.md` (APS-η escape, finite-level-closed)
- `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` (S3 mechanism, escape-hatches I/II)
- `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`

## Narrowing repair for the corner-forcing note and the three-generation observable note

Nothing was run and nothing was written. Everything was read from `origin/main` at 0485dc0738. The blast-radius classification comes from five read-only subagents that located excerpts by grep. I checked seven of their quotes against main (dependents #5, #20, #35, #39, #96, #98, #101) and all seven match.

Labels: **EXACT** means a proof is given here. **CHECKED** means I evaluated it by hand. **ARGUED** means the reasoning is not verified. **READ** means it comes from the source text.

### 0. Summary

- **The repair is warranted (EXACT).**
  - Both notes attach a correct finite algebra to the Kawamoto–Smit (KS) operator. The algebra is that diagonal characters plus a 3-cycle generate M_3(C) on hw=1.
  - The operators behind that algebra are plain one-site translations and a bare index cycle. These are not KS symmetries.
  - The true KS translation lifts ±S_a pairwise anticommute.
  - At most one plain translation is a symmetry in any representative.
  - A gauge transform (−1)^{c·x} inside the single Block 03 class relabels every corner n → n⊕c.
- **New point: in η⁰, the true KS C₃ symmetry does not preserve the hw=1 corner span (CHECKED by hand).**
  - Its image is W_C v₁₀₀ = ½(v₀₁₀ + v₀₀₁ + v₁₁₀ − v₁₀₁).
  - The bare cycle is a symmetry in the cyclic representative.
- **The review's reason for line 33 of the observable note is right for the corner modes but not for that note's own runner (READ + EXACT).**
  - `frontier_three_generation_observable_theorem.py` builds X1–X3 as the +1 eigenspaces of the 8×8 cell Bloch operator at cell momenta πe_a. These sit at |E| = 1 and are 4-dimensional each.
  - On that object, the diagonal characters belong to the two-site cell translations, which do commute with D. So the sentence is ambiguous rather than simply false, and the replacement names both objects.
- **Prior agreement already on main (READ):**
  - `STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`, 2026-06-10 repair record: "**That premise is false.** … the true invariances are `[D, T_μ²] = 0` for all μ and `[D, T_3] = 0`".
  - `FLAVOR_OPERATOR_REALIZATION_LOCAL_DENSITY_2026-05-31.md` finds that the bare cyclic permutation does not commute with D, and that a site-local Z₂ sign gauge repairs it.
- **Blast radius:** 107 direct dependents.
  - 14 lean on the KS-symmetry reading and need follow-up.
  - 26 are mixed: their conclusions are algebraic but they carry inherited species or symmetry wording.
  - 67 use the corner algebra, the count, or a provenance link, and are unaffected.

---

### 1. Sentence-by-sentence repair

#### 1a. Corner-forcing note, Step 1 (lines 70–73)

Current:
> By Block 03, the Kawamoto-Smit kinetic operator on Z³ APBC is
> diagonalized in momentum space at the **BZ corners** k_μ ∈ {0, π}.
> Each corner is labeled by a binary vector `n = (n_1, n_2, n_3) ∈ {0,1}³`
> with `k_μ = n_μ · π`. There are 2³ = 8 corners total.

Replacement:
> Take the Block 03 representative η⁰ (or any representative
> `η_μ(x) = ±(−1)^{ζ_μ·x}` with `η_μ` independent of `x_μ`). The
> Kawamoto-Smit operator `D` is not diagonal in momentum space: its
> direction-μ term multiplies a plane wave of momentum `k` by a factor
> proportional to `sin k_μ` and moves it to momentum `k + π ζ_μ`. Its
> square is diagonal: the −1 plaquette cocycle makes the three direction
> terms anticommute, so `D² = −Σ_μ sin² k_μ` on plane waves, which vanishes
> exactly at the eight **BZ corners** `k_μ ∈ {0, π}`. On periodic tori of
> even side these eight plane waves span the kernel of `D`. On APBC tori of
> even side the corner momenta are not allowed; the lowest modes sit at the
> allowed momenta nearest the corners (`|q_μ| = π/L`), where `D` couples
> corner label `n` to `n xor ζ_μ` with amplitude proportional to `sin q_μ`.
> Each corner is labeled by a binary vector `n = (n_1, n_2, n_3) ∈ {0,1}³`
> with `k_μ = n_μ · π`. There are 2³ = 8 corners total.

Justification: D maps k to k+πζ_μ and only D² is diagonal (EXACT). Under APBC with even L the corner momenta are excluded. In plane-wave gauges with (ζ_μ)_μ = 1 the zeros move to ±π/2, hence the restriction on η.

#### 1b. Step 3 (lines 111–125)

Current:
~~~
The three lattice translations `T_x, T_y, T_z` act on the hw=1 triplet
as:

```
T_x: diag(−1, +1, +1)
T_y: diag(+1, −1, +1)
T_z: diag(+1, +1, −1)
```

(distinct joint characters separating the three corners). Combined
with the `C_3[111]` cyclic generator that maps `(1,0,0) → (0,1,0) →
(0,0,1) → (1,0,0)`, these operators generate the full M_3(C) algebra
on `H_hw=1`.
~~~

Replacement:
~~~
The three plain one-site lattice translations `T_x, T_y, T_z`,
`(T_μ ψ)(x) = ψ(x + e_μ)`, preserve the span of the eight corner plane
waves and act on the three hw=1 corner labels as:

```
T_x: diag(−1, +1, +1)
T_y: diag(+1, −1, +1)
T_z: diag(+1, +1, −1)
```

(distinct joint characters separating the three corner labels). Combined
with the bare corner-label cycle `C_3[111]`, `(n_1, n_2, n_3) → (n_3, n_1, n_2)`,
which maps `(1,0,0) → (0,1,0) → (0,0,1) → (1,0,0)`, these operators
generate the full M_3(C) algebra on `H_hw=1`.

**Scope of these operators.** They are plain lattice operators acting on
corner plane-wave labels. They are not symmetries of the Block 03
Kawamoto-Smit operator `D`:

- In any representative of the Block 03 gauge class, at most one plain
  translation commutes with `D`: if `T_a` and `T_b` both did, every `η_μ`
  would be independent of `x_a` and `x_b`, and the `ab` plaquette would
  carry `+1` instead of `−1`. In `η⁰`, `T_z` commutes with `D`; `T_x` and
  `T_y` do not.
- The symmetries of `D` covering `T_a` are `±S_a`, `S_a = (−1)^{b^{(a)}·x} T_a`
  with `b^{(a)}_ν = (ζ_ν)_a` in a representative `η_μ = (−1)^{ζ_μ·x}` (in
  `η⁰`: `(−1)^{x_2+x_3} T_x`, `(−1)^{x_3} T_y`, `T_z`). The −1 cocycle gives
  `S_a S_b = −S_b S_a` for `a ≠ b`, so no nonzero vector is a joint
  eigenvector of two of them. They move corner labels, `n → n xor b^{(a)}`,
  instead of acting by characters.
- The two-site translations `S_a²` commute with `D` and with each other,
  but act as `+1` on all eight corner plane waves.
- The bare cycle is a symmetry of `D` in the cyclic representative
  `η_1 = (−1)^{x_2}, η_2 = (−1)^{x_3}, η_3 = (−1)^{x_1}`. In `η⁰` the
  symmetry covering it carries the factor `(−1)^{x_1x_2 + x_1x_3}` and does
  not preserve the hw=1 corner span. Since `C_3[111]` conjugates
  `T_x → T_y → T_z`, no representative makes all four of
  `T_x, T_y, T_z, C_3[111]` symmetries of `D`.

[Optional context sentence:] On the coin walker of the 2026-09-22
scalar-hop note (two amplitudes per site, zero-flux hopping) the plain
translations and the axis cycle, with its coin rotation, are symmetries
and the corner labels are momentum labels; there the algebra of this step
is a symmetry statement. On the Block 03 carrier it is a statement about
labels.
~~~

Justification: The runner's `translation_character` is (−1)^{n_μ} and its `c3_111` is the bare index cycle (READ).
- The plaquette argument, the S_a lift with its anticommutation, the action of S_a² on the corners, and the "no representative has all four" step are all EXACT.
- The η⁰ C₃ non-preservation is CHECKED by hand.

#### 1c. Step 4 (lines 136–146)

Current:
> If a quotient claims to preserve any exact retained operator, the
> observable-descent lemma forces its kernel to be invariant under that
> operator. In the present finite carrier, preserving the translation
> projectors forces any invariant subspace to be a coordinate subspace
> `span{X_i : i in S}`. Preserving the `C_3[111]` cycle forces `S` to be
> closed under the three-cycle. The only such subsets are the empty set and
> the full set `{1,2,3}`.
>
> Therefore **no proper nonzero subspace** and hence no proper exact quotient
> preserves both the translation-character separation and the `C_3[111]`
> cycle on hw=1.

Replacement:
> If a quotient of `H_hw=1` preserves an operator, the observable-descent
> lemma forces its kernel to be invariant under that operator. On the corner
> labels, preserving the three plain-translation character projectors forces
> any invariant subspace to be a coordinate subspace `span{X_i : i in S}`,
> and preserving the corner-label cycle `C_3[111]` forces `S` to be
> invariant under the three-cycle. The subsets with that property are the
> empty set and the full set `{1,2,3}`.
>
> Therefore **no proper nonzero subspace**, and hence no proper quotient,
> preserves both the plain-translation character separation and the
> corner-label cycle on hw=1. This is a statement about those plain
> operators. It does not show that a reduction of the Kawamoto-Smit carrier
> must preserve them, since by Step 3 they are not its symmetries. Nor is
> the hw=1 corner span invariant under the Kawamoto-Smit structure: in every
> plane-wave representative at least two of the `b^{(a)}` are nonzero and no
> nonzero `b ∈ {0,1}³` maps the hw=1 labels into themselves, so the
> translation symmetries `S_a` move it; and away from the exact zero modes
> the direction-μ term of `D` moves labels by `ζ_μ`, at least two of which
> are nonzero.

Justification: The descent lemma is unchanged. "Exact retained operator" was the step that attached the projectors to KS. The lemma that no nonzero b maps L₁ to itself, and the fact that at most one ζ_μ or b^{(a)} is zero, are EXACT.

#### 1d. Step 6 (lines 175–188)

Current:
> ### Step 6: Hamming-weight decomposition is unique
>
> The 8-corner spectrum and the Hamming-weight labeling are uniquely determined
> by:
> - Block 03's K-S kinetic structure
> - Z³ APBC convention (retained)
> - direct binary-corner enumeration in the runner
>
> There is no convention freedom in the Hamming-weight assignment to
> corners; it follows directly from the binary corner labeling under APBC.
> The position-space epsilon/chirality operation is separately fenced by the
> bit-complement check above and is not part of this theorem's positive
> claim.

Replacement:
> ### Step 6: Hamming weight is relative to a representative
>
> Given the representative η⁰ and the plane-wave basis, the Hamming-weight
> labeling follows from the binary corner labeling by direct enumeration in
> the runner. It is not invariant under the gauge freedom of Block 03. A Z₂
> gauge transform by `(−1)^{c·x}`, `c ∈ {0,1}³`, stays in the single Block 03
> gauge class (Lemma 4), replaces `η⁰_μ` by `(−1)^{c_μ} η⁰_μ`, and relabels
> every corner `n → n xor c`. For `c = (1,1,1)` this is Block 03 Remark R3
> (`−η⁰` is the ε-gauge transform of `η⁰`); by the bit-complement check of
> Step 2 it exchanges hw=1 with hw=2, so the same modes carry hw=1 labels in
> one representative and hw=2 labels in the other. For `c = (1,0,0)` the
> hw=1 labels map to `{000, 110, 101}`. What is invariant is the affine
> structure of the eight corner labels (the differences `n xor n'`); the
> 1+3+3+1 grading needs a base corner, and choosing the base corner is
> choosing a representative. The position-space epsilon/chirality operation
> is separately fenced by the bit-complement check above and is not part of
> this theorem's positive claim.

Justification: The relabeling holds because G_c v_n = v_{n⊕c} (EXACT), and it contradicts the old sentence through Block 03's own R3. This also keeps Step 2's firewall phrases intact (see §4).

#### 1e. Theorem 3 box (lines 196–208, the "UNIQUELY" sentence)

Current:
~~~
The Kawamoto-Smit staggered-Dirac kinetic operator on Z³ APBC has
8 BZ corners that decompose UNIQUELY by Hamming weight as

    1 (hw=0) + 3 (hw=1) + 3 (hw=2) + 1 (hw=3)

The hw=1 triplet carries the exact irreducible M_3(C) algebra with
no proper quotient preserving both the translation-character projectors
and the C_3[111] cycle. The physical species / SM-generation reading is
not asserted by this bounded source note, and BZ-corner Hamming parity is
not identified with position-space sublattice/chirality.
~~~

Replacement:
~~~
In the Block 03 representative η⁰, the eight corner momenta
k ∈ {0, π}³ (where the square of the Kawamoto-Smit operator vanishes)
carry labels n ∈ {0,1}³ that decompose by Hamming weight relative to
the base corner n = 000 as

    1 (hw=0) + 3 (hw=1) + 3 (hw=2) + 1 (hw=3)

The base corner, and with it every Hamming label, depends on the
representative: the gauge transform (−1)^{c·x} within the Block 03 class
relabels n → n xor c.

On the hw=1 labels, the plain one-site lattice translations act by three
distinct joint characters, and together with the bare corner-label cycle
C_3[111] they generate the irreducible algebra M_3(C), with no proper
subspace preserving both the character projectors and the cycle. These
plain operators are not symmetries of the Kawamoto-Smit operator: its
translation symmetries anticommute pairwise and have no joint characters,
and at most one plain translation commutes with it in any representative.
The physical species / SM-generation reading is not asserted by this
bounded source note, and BZ-corner Hamming parity is not identified with
position-space sublattice/chirality.
~~~

Justification: "UNIQUELY" fails by Step 6, "on Z³ APBC" fails by Step 1, and the algebra is re-attached to the operators that actually generate it. The algebra itself is untouched.

#### 1f. Observable note, line 33 (lines 33–39)

Current:
> On the current retained package surface, the three `hw=1` sectors are exact
> observable sectors of the Hamiltonian. More precisely:
>
> - the exact lattice translations separate `X1`, `X2`, `X3` by three distinct
>   joint characters
> - the exact induced `C3[111]` map cycles `X1 -> X2 -> X3 -> X1`

Replacement:
> On the finite carrier `H_hw=1 = C^3`, the three `hw=1` labels `X1`, `X2`,
> `X3` are separated by a diagonal translation triple and cycled by the
> induced `C3[111]` map, and these operators generate `M_3(C)`. This note
> does not assert that the three `hw=1` sectors are observable sectors of
> the staggered (Kawamoto-Smit) Hamiltonian near its zero modes. There the
> triple is the plain one-site translations acting on corner labels, which
> are not symmetries of that operator: its translation symmetries
> anticommute pairwise and have no joint characters, and away from the exact
> zero modes its direction-`mu` term moves corner labels by `zeta_mu` (in the
> taste-cube form `H(q) = sin q_1 Z_1 + sin q_2 X_1 Z_2 + sin q_3 X_1 X_2 Z_3`
> the `X_1` factor changes Hamming weight). The runner's `X1`, `X2`, `X3` are
> a different object: the `+1` eigenspaces of the cell Bloch operator at cell
> momenta `pi e_a`, four-dimensional each and at `|E| = 1`, not zero modes;
> there the triple is the two-site cell translations, which do commute with
> the operator. More precisely:
>
> - the diagonal translation triple separates `X1`, `X2`, `X3` by three
>   distinct joint characters
> - the induced `C3[111]` map cycles `X1 -> X2 -> X3 -> X1`

Justification:
- The taste-cube form follows from sin(πn_μ+q_μ) = (−1)^{n_μ} sin q_μ and η⁰_μ v_n = v_{n⊕ζ_μ} (EXACT).
- The runner reading is READ from its code: the Bloch phase e^{ik} is applied per cell crossing.
- (iD(K))² = Σ sin²k_μ = 1 at K = πe_a, and the trace is zero, giving the 4+4 split (EXACT).
- η⁰ is 2-periodic, so T_μ² commutes with D (EXACT).

#### 1g. Consequential edits (same PR, same narrowing)

Corner-forcing note:
- **Answer section.** Change "**Yes.**" to "**Yes, for the corner labels of η⁰ and the plain lattice operators acting on them; no symmetry statement about the Kawamoto-Smit operator follows (Step 3).**"
  - Item 1 becomes "Block 03's Kawamoto-Smit operator, whose square vanishes at the eight corner momenta in η⁰".
  - Items 4–5: replace "translations" with "plain lattice translations" and "`C_3[111]`" with "bare corner-label cycle `C_3[111]`".
- **Step 5 box.** Replace "The hw=1 BZ-corner triplet on the staggered-Dirac Z³ APBC carries an exact irreducible M_3(C) algebra, with no proper quotient." with "The hw=1 corner labels of η⁰ carry the irreducible M_3(C) algebra generated by the plain lattice translations and the bare corner-label cycle, with no proper quotient preserving both; this is not a symmetry statement about the Kawamoto-Smit operator."
- **Forcing chain.**
  - "Block 03 → unique K-S kinetic operator" becomes "Block 03 → one Kawamoto-Smit gauge class (labels relative to η⁰)".
  - "K-S kinetic on Z³ APBC → 8 BZ corners" becomes "zeros of D² in η⁰ → 8 corner momenta".
- **Premise rows M3 and NQ.** Add "(plain translations + bare cycle; not Kawamoto-Smit symmetries, Step 3)".

Observable note:
- **Theorem statement.** Change "the exact lattice translations act by three distinct joint characters" to "the diagonal translation triple (realizations in Safe statement) acts by three distinct joint characters".
- **Input surface item 2.** Append "(plain one-site translations on corner labels, or two-site cell translations on the runner's cell-momentum sectors)". Leave all grade words untouched.

---

### 2. Proposed claim_scope header lines

The ledger `claim_scope` is null for both rows and is pipeline-owned. These are proposed `**Claim scope:**` header lines in Block 03 style.

**Corner-forcing note:**
> **Claim scope:** For the Block 03 representative η⁰ of the Kawamoto-Smit gauge class, the eight corner momenta `k ∈ {0,π}³` (where `D²` vanishes) carry labels `n ∈ {0,1}³` that split by Hamming weight relative to the base corner `000` as `1+3+3+1`; on the three hw=1 labels the plain one-site lattice translations act by three distinct joint characters and, with the bare corner-label cycle `C_3[111]`, generate `M_3(C)` with no proper nonzero invariant subspace. These are statements about plain lattice operators on corner plane-wave labels, not symmetry statements about the Kawamoto-Smit operator: its translation symmetries anticommute pairwise and have no joint characters, at most one plain translation commutes with it in any representative, and a gauge transform `(−1)^{c·x}` within its class relabels the corners `n → n xor c`. No species, generation, or chirality reading is asserted.

**Observable note:**
> **Claim scope:** On `H_hw=1 = C^3` with the diagonal triple `T_x = diag(−1,+1,+1)`, `T_y = diag(+1,−1,+1)`, `T_z = diag(+1,+1,−1)` and the cycle `C3[111]: X1 → X2 → X3 → X1`, the character projectors and powers of `C3` give every matrix unit, the generated algebra is `M_3(C)`, it acts irreducibly, and by the observable-descent lemma no proper quotient preserves it. The triple is realized by the plain one-site translations on corner labels (not symmetries of the Kawamoto-Smit operator) or by the two-site cell translations on the runner's cell-momentum sectors (symmetries, at `|E| = 1`, not zero modes). No observable-sector statement about the Kawamoto-Smit operator near its zero modes, and no species or generation reading, is asserted.

---

### 3. Blast radius

Source: the ledger `deps` field in `docs/audit/data/ledger/**`, the repo's upstream-dependency edge list.
- The corner-forcing note has direct in-degree 41 (ledger 41) and 625 transitive descendants.
- The observable note has 93 rows found by the grep (ledger in-degree 94) and 1218 transitive descendants.
- The union is 107 direct dependents.

**Needs follow-up: relies on the KS-symmetry reading (14).**

| # | claim_id | cites | load-bearing use (READ) |
|---|---|---|---|
| 2 | a3_r2_review_confirms_exhaustion_note_2026-05-08_r2hr | corner | C₃ lifted to a symmetry of the staggered dynamics; corners as species |
| 3 | a3_r3_review_confirms_obstruction_note_2026-05-08_r3hr | both | C₃ orbit as a symmetry orbit; translation eigenvalues as physical decorations |
| 5 | a3_r5_review_confirms_obstruction_note_2026-05-08_r5hr | corner | "KS … restricted to hw=1 is exactly λ_KS · I … [H_KS, U_{C_3}] = 0 EXACTLY" |
| 7 | a3_route2_single_clock_c3_obstruction_note_2026-05-08_r2 | both | "`T` (and `H`) commute with `U_{C_3[111]}` … Restricted to `H_{hw=1}`" |
| 8 | a3_route3_anomaly_inflow_bounded_obstruction_note_2026-05-08_r3 | both | Hamming weight used as staggered chirality |
| 10 | a3_route5_no_proper_quotient_sharpened_obstruction_note_2026-05-08_r5 | both | bare KS operator C₃-symmetric on hw=1 |
| 11 | ac_phi_lambda_preserved_c3_structural_foreclosure_bounded_theorem_note_2026-05-10 | both | §8.1: KS block-diagonality via joint translation eigenvalues |
| 20 | charged_lepton_mass_hierarchy_review_note_2026-04-17 | obs | "Pure-APBC `D` commutes with each `T_k`" |
| 39 | generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06 | obs | generations = hw=1 corners separated by joint translation characters |
| 60 | koide_bae_probe_hw_sector_identification_bounded_obstruction_note_2026-05-09_probe27 | both | hw=1 vs hw=2 as distinct physical hosts (gauge-dependent labels) |
| 74 | koide_s_substep4_aclambda_new_science_note_2026-05-08_probes_substep4_aclambda | both | KS block-diagonality plus joint translation characters |
| 95 | staggered_dirac_physical_species_direct_theorem_note_2026-05-07 | both | "T_x, T_y, T_z are lattice translation operators in the represented framework dynamics" |
| 98 | substep4_ac_lambda_separate_closure_note_2026-05-10_aclambda | both | "The Kawamoto-Smit kinetic operator `K` commutes with all three lattice translations" |
| 101 | three_generation_chirality_boundary_note | obs | "Exact translation observables therefore separate the triplet sectors as physically distinct species" |

There is an internal conflict already on main. #20 and #98 assert the commutation that #96's 2026-06-10 repair record calls false.

**Mixed: conclusions algebraic, inherited wording (26).** For each, a wording check is enough.
- #4 a3_r4; #6 a3_route1; #9 a3_route4.
- #12 acphilambda_species_bridge (already names the hw=1↔hw=2 complementation class).
- #15 bae_max_entropy; #16 c3_symmetry_preserved_interpretation (meta).
- #21 charged_lepton_ue_identity; #25 dm_neutrino_microscopic_polynomial (no-go direction robust).
- #36 g_bare_structural_normalization (defines the triplet via joint lattice-translation characters).
- #37 g_star_sm_content; #38 generation_corner_hf_vq; #40 higgs_z3_charge.
- #41 hw1_second_order_return_shape (different carrier, C¹⁶).
- #46 koide probe17 (uses the plain-translation characters, which is fine after narrowing).
- #61 probe28; #62 probe23; #69 koide_delta_phase_generation_count; #72 koide_positive_paths.
- #76 probeU; #79 probeX; #81 probeZ (self-disclaims).
- #86 p_flux_point_zero_set and #87 p_flux_selection_from_matter_content. Their battery is satisfiable by plain translations that preserve the kernel, so the no-go is unaffected (ARGUED from the note text; their runners were not inspected).
- **#93 staggered_dirac_gate_closure_synthesis.** It recites Theorem 3 verbatim, so it must be synced with this PR or it re-asserts the withdrawn wording.
- #96 substep4ac (already repaired the commutation premise, but keeps hw-indexed corner-block wording).
- #97 substep4_labeling_no_go (premise of "commuting lattice translations"; its no-go is algebraic).

**Unaffected: corner algebra, count, or provenance only (67).**
- a3_option_c_brannen_rivero_optc, active_sector_grounded_mass_vs_k_sieve, axiom_first_sm_anomaly_cancellation_complete, canonical_harness_index, charged_lepton_koide_cone_algebraic_equivalence, charged_lepton_koide_value_full_chain_of_custody, closure_c_staggered_dirac_gate.
- dm_neutrino {bifundamental_invariance, info_geometric_selection, schur_scalar_baseline}; flavor {absolute_handedness, asymmetry_2over9, gauge_holonomy_character_suppression_kernel, gauge_holonomy_suppresses_r, gauge_representation_channel, gauge_representation_generation_uniform_core, idempotent_u1_collapses, max_record_entropy, operator_realization_local_density}.
- koide_a1: 11-probe meta, probe15, probe2, probe3, probe6, probe12, probe16, probe13, probe5, probe1, probe4, probe7, routes A/D/E/F.
- koide_bae: probe18, probe25, probe22, probe20, probe26.
- koide: c3_generator_rephasing, circulant_character_derivation, dimensionless_radian, one_scalar_obstruction_triangulation, q_reduced_carrier_physical_identification; probeT, probeV-maxent, probeV-s3, probeY.
- mass_mixing_subspace_disjointness, neutrino_dirac_z3_support_trichotomy, observable_principle_p1_bridge, p_flux_finite_species_density, pmns_from_dm_neutrino_source_h_diagonalization, quark_c3_oriented_ward_splitter, sm_gstar_from_framework_structure, sm_gstar_r_matter_residual, sphaleron_coefficient_28_79.
- staggered_dirac_hw1_three_eigenvalue_structure_positive, theorem_bae_newton_girard_unified, three_gen_z3_fourier_diagonalization, wilson_bz_corner_hamming_staircase, yt_class_6, yt_class_7, yt_generation_hierarchy_primitive_analysis, yt_h_unit_flavor_column, z_n_spectral_asymmetry_physical_identification.

The rows that take n_gen = 3 (#14, #37, #90–92) use the count |L₁| = 3, which the narrowing keeps.

**Adjacent rows, not dependents, consistent with the narrowing:**
- The substep-3 Hamming-orbit and substep-4 simultaneous-diagonalization narrow theorems are both abstract.
- `STAGGERED_DIRAC_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_BRIDGE_…_2026-07-05` explicitly uses plain translations on the 2×2×2 periodic representative.

---

### 4. Runner spec (not run)

**Files.**
- `scripts/staggered_dirac_corner_label_symmetry_scope_check_2026_10_01.py`
- cache `logs/runner-cache/staggered_dirac_corner_label_symmetry_scope_check_2026_10_01.txt`

**Run constraints.**
- Top-level `AUDIT_TIMEOUT_SEC = 60`, with the same value in the cache header.
- Pure Python integers (numpy int64 is acceptable), deterministic, single thread.
- Under 50 MB, under 5 s, and output under 6000 characters.
- `[PASS]` lines, then `TOTAL: PASS=N FAIL=0`; exit 0 iff FAIL = 0.

**Objects.**
- **Torus.** Sites x ∈ (Z₄)³, so 64 sites.
  - T_μ is the permutation (T_μψ)(x) = ψ(x+e_μ).
  - η_μ(x) = (−1)^{ζ_μ·x}.
  - 2D = Σ_μ (diag(η_μ) T_μ − T_μ⁻¹ diag(η_μ)), an integer 64×64 matrix.
- **Representatives.**
  - η⁰: ζ = (000, 100, 110).
  - Cyclic: ζ = (010, 001, 100).
  - Corner vectors v_n(x) = (−1)^{n·x}.
- **Corner carrier (8×8).**
  - J: C⁸ → C⁶⁴, (Jf)(x) = f(x mod 2), with JᵀJ = 8I.
  - Restriction O|₈ = JᵀOJ/8, an exact integer division.
  - Hadamard H₈[n,s] = (−1)^{n·s}.

**A. Construction (64).**
- Both representatives: 2D is antisymmetric, every entry ±1 or 0, 6 nonzeros per row.
- All 192 plaquettes give product −1.
- Every straight non-contractible loop has holonomy +1.
- (2D)² = Σ_μ (T_μ² + T_μ⁻² − 2I) exactly. So D is not diagonal in plane waves, but D² is.
- η_μ v_n = v_{n⊕ζ_μ} for all n and μ.
- 2D·J = 0: D vanishes on the corner carrier.

**B. Shift symmetries (η⁰).**
- S₁ = (−1)^{x₂+x₃}T₁, S₂ = (−1)^{x₃}T₂, S₃ = T₃.
- [S_a, 2D] = 0 for each a.
- S_aS_b + S_bS_a = 0 for a<b, at both 64 and 8.
- A breadth-first (BFS) link solve shows the sign fields s with [sT_a, D] = 0 are exactly ±s_a.
- S_a² commute with 2D and with each other, and S_a²J = J.
- S_a v_n = (−1)^{n_a} v_{n⊕b^{(a)}} with b^{(a)} = (011, 001, 000).
- For each of the 7 nonzero b: L₁⊕b ⊄ L₁.
- Meaning: PASS means no KS translation symmetry has joint characters. A failure means a construction error, since it would contradict the −1 cocycle.

**C. Plain translations.**
- η⁰: [T₃, 2D] = 0, while [T₁, 2D] and [T₂, 2D] are nonzero with max |entry| 2. This matches the substep-4 runner on main.
- Cyclic representative: all three [T_a, 2D] ≠ 0.
- On the corner carrier, H₈ T_μ|₈ H₈ = 8·diag((−1)^{n_μ}). The same operator gives the corner characters and is not a symmetry.
- All 64 plane-wave ζ (off-diagonal pair bits summing to 1, diagonal bits free):
  - each is a BFS gauge transform of η⁰ on the 4³ torus;
  - the number of commuting plain translations is 0 in 40 cases, 1 in 24, and 2 or more in 0;
  - in each, the S_a with b^{(a)}_ν = (ζ_ν)_a commute with D and pairwise anticommute.

**D. C₃.**
- Let P_C be the map x → (x₃,x₁,x₂).
- In the cyclic representative, P_C commutes with 2D and P_C³ = I. In the Hadamard basis, P_C|₈ is the bare cycle n → (n₃,n₁,n₂).
- In η⁰, P_C does not commute with 2D, but W_C = diag((−1)^{y₁y₂+y₁y₃})P_C does.
- In η⁰, 2·W_C v₁₀₀ = v₀₁₀ + v₀₀₁ + v₁₁₀ − v₁₀₁ (CHECKED by hand). So the hw=1 span is not W_C-invariant.

**E. Rotation characters.**
- For all 24 proper rotations, BFS-solve g_R with g_R(0) = 1 from W(2D)Wᵀ = 2D, where W = diag(g)·Π_R.
- Check the closed forms for the class representatives in this antisymmetric convention:

| rotation | x → | g_R(y) |
|---|---|---|
| C₄z | (−x₂, x₁, x₃) | (−1)^{y₁y₂+y₁} |
| C₂z | (−x₁, −x₂, x₃) | (−1)^{y₁+y₂} |
| C₃ | (x₃, x₁, x₂) | (−1)^{y₁y₂+y₁y₃} |
| C₂′(110) | (x₂, x₁, −x₃) | (−1)^{y₁y₂+y₃} |

  These differ from the review's real-hopping list by orientation signs (CHECKED by hand). The characters are the same.
- Group law W_RW_S = W_{RS} for all 576 pairs, computed by signed-permutation composition.
- Every g_R is 2-periodic.
- tr W_R|₈ by class (E, 8C₃, 3C₂, 6C₄, 6C₂′) = (8, 2, 0, 4, 0). The multiplicities from the O character table are A₁ 2, A₂ 0, E 0, T₁ 2, T₂ 0.

**F. Hamming labels.**
- ε(2D(η⁰))ε = −2D(η⁰), and ε v_n = v_{n⊕111}, so L₁ maps to L₂.
- For all 8 values of c: G_c 2D(η⁰) G_c = 2D(η^c) with η^c_μ = (−1)^{c_μ}η⁰_μ, the cocycle still −1, and G_c v_n = v_{n⊕c}.
- The Hamming multiset of L₁⊕c is {1,1,1} for c = 000, {0,2,2} for c ∈ L₁, {1,1,3} for c ∈ L₂, and {2,2,2} for c = 111.
- The difference set {n⊕n′ : n, n′ ∈ L₁} = {000, 011, 101, 110} is the same for every c.

**Changes to the existing runner** `probe_bz_corner_decomposition.py`:
- Docstring "decompose uniquely by Hamming weight" becomes "split 1+3+3+1 by Hamming weight relative to base corner 000".
- Replace the final "has unique 1+3+3+1 BZ-corner decomposition" print with one naming plain operators and pointing to the new runner.
- Keep the firewall markers "BZ-corner Hamming parity with the K-S" and "parity-to-chirality identification is a separate bridge", which Step 2 must keep verbatim.
- Add forbidden tokens "decompose UNIQUELY" and "There is no convention freedom in the Hamming-weight assignment".

---

### 5. PR

**Title:** `fix(generation): scope the hw=1 corner algebra to plain lattice maps` (68 characters)

**Body outline** (framework terms, no check indices):
1. **Physics first.** The M_3(C) and no-proper-quotient algebra on the three weight-one corner labels stands. It is generated by plain one-site lattice translations and the bare axis cycle acting on corner plane-wave labels, not by symmetries of the Kawamoto-Smit operator.
   - The operator's translation symmetries anticommute pairwise, so they have no joint characters.
   - At most one plain translation is a symmetry in any representative.
   - A sign gauge inside its single gauge class relabels the corners, so hw=1 and hw=2 trade places under Block 03's own global-sign remark.
   - The bare cycle is a symmetry in the cyclic representative but not in η⁰.
2. **What changes.**
   - Corner-forcing note: Steps 1, 3, 4 and 6, the theorem box, and the answer list.
   - Observable note: the safe-statement sentence, which now names its two realizations (corner labels with plain translations; the runner's cell-momentum sectors with two-site translations).
   - Existing runner: wording and firewall.
   - New exact integer runner plus cache.
3. **What does not change.** The finite algebra, the 1+3+3+1 count on {0,1}³, the epsilon bit-complement fence, the species disclaimers, and every status line. No audit verdict is set or predicted.
4. **Agreement already on main.** The 2026-06-10 repair record in the substep-4 narrow note, and the flavor operator-realization note (bare cycle fails in η⁰; a sign gauge repairs it).
5. **Downstream.** No dependent is edited here.
   - List the 14 rows whose arguments assume the translations or cycle are staggered symmetries or that hw labels are representative-free.
   - Flag the gate-closure synthesis for a wording sync, since it recites the old theorem box.
   - Note that two rows still assert the commutation that main already calls false.
6. **Verification.** Commands for both runners, with expected `TOTAL: PASS=N FAIL=0`, plus an own re-run.
7. Footer: 🤖 Generated with [Claude Code](https://claude.com/claude-code)

If the landing convention requires one note, one runner and one cache per PR, split it in two:
- PR A: corner-forcing note, existing-runner edit, new runner and cache.
- PR B: observable-note wording, citing PR A's runner.
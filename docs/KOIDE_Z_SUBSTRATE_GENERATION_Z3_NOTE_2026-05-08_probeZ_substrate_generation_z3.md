# Probe Z-Substrate-Generation-Z3 — Z^3 x C_3 Substrate Three-Orbit Bound (Source Note)

**Date:** 2026-05-10
**Claim type:** bounded_theorem
**Sub-gate:** substrate three-orbit cardinality bound
**Status authority:** independent audit lane only; effective status is
pipeline-derived.
**Source-note proposal disclaimer:** this note is a source-note proposal;
audit verdict and downstream status are set only by the independent
audit lane.
**Actual current-surface status:** bounded theorem. The finite
orbit-counting, Fourier, and no-proper-quotient algebra closes on the
Lattice axiom's `Z^3` surface plus named `C_3[111]` support; this note
does not derive the downstream SM species map or sector propagation.
**Trace class:** upstream_support
**Reachability to target:** supports
**Proposal allowed:** false
**Bare retained allowed:** false
**Audit required before effective retained:** true

**Primary runner:** [`scripts/cl3_koide_z_substrate_generation_z3_2026_05_08_probeZ_substrate_generation_z3.py`](../scripts/cl3_koide_z_substrate_generation_z3_2026_05_08_probeZ_substrate_generation_z3.py)
**Cached output:** [`logs/runner-cache/cl3_koide_z_substrate_generation_z3_2026_05_08_probeZ_substrate_generation_z3.txt`](../logs/runner-cache/cl3_koide_z_substrate_generation_z3_2026_05_08_probeZ_substrate_generation_z3.txt)

## 0. Probe context

A substrate-anomaly analysis can leave `n_gen = 3` **not** forced by
Standard Model anomaly cancellation alone. The reason is that
the SM gauge anomaly conditions (`SU(2)²U(1)`, `SU(3)²U(1)`, `U(1)³`,
gravitational-`U(1)`) are all **linear** in `n_gen`: they take the form
`n_gen × (per-generation contribution) = 0`, so any positive integer
`n_gen` that satisfies the per-generation cancellation also satisfies the
total cancellation.

This probe asks the dual bounded question:

> On the framework Lattice axiom's `Z^3` spatial surface plus the named
> `C_3[111]` structure, does the finite orbit-counting /
> character-theory packet force a three-element `hw=1` substrate carrier,
> even though anomaly cancellation alone does not force a generation count?

The current repo support relevant to this question provides:

1. **Lattice axiom `Z^3` spatial surface** (per
   [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)): the
   site set is `Z^3` with standard translation action and nearest-neighbor
   cubic adjacency. Dependencies on the stable `minimal_axioms` premise
   chain-satisfy without bounding downstream rows.
2. **BZ-corner structure** (per
   [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md)):
   `Z³` BZ corners are `{0, π}³`, partitioned by Hamming weight as
   `8 = 1 + 3 + 3 + 1`.
3. **`hw=1` triplet algebra** (per
   [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)):
   on `H_{hw=1} ≅ ℂ³`, the operators `{T_x, T_y, T_z, C_3[111]}`
   generate `M_3(ℂ)` and act irreducibly.
4. **`C_3` Fourier diagonalization** (per
   [`THREE_GEN_Z3_FOURIER_DIAGONALIZATION_THEOREM_NOTE_2026-05-03.md`](THREE_GEN_Z3_FOURIER_DIAGONALIZATION_THEOREM_NOTE_2026-05-03.md)):
   `C_3[111]` has exactly 3 distinct eigenvalues `{1, ω, ω²}` (cube
   roots of unity) on `ℂ³`.
5. **No-proper-quotient** (per
   [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)):
   no proper quotient of `H_{hw=1}` preserves both translation projectors
   and `C_3[111]`.
6. **Observable count = 3** (per
   [`THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md`](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md)):
   the multiplicity of the lightest non-zero-mass `hw=1` species is
   exactly three, and this count is observable-stable.
7. **Preserved-`C_3` interpretation** (per
   [`C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md`](C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md)):
   `C_3[111]` is fundamental and unbroken; species labels {electron,
   muon, tau} are convention.

This probe assembles items (1)–(7) into a single bounded three-orbit
substrate-cardinality claim. The closed chain is independent of anomaly
cancellation on the `Z^3`/`C_3[111]` surface.

### 0.1 Audit-scope repair (2026-06-18)

The prior conditional rationale identified missing accepted-premise
handling for the physical `Z^3` substrate premise. Current repo governance
handles Lattice through the stable `minimal_axioms` axiom-premise node.
This note therefore narrows the downstream claim boundary only: it does
not claim that three SM generations are fully derived, and it does not
close the physical species map. The claim is the exact finite algebra:

> Given the Lattice axiom's `Z^3` BZ-corner surface and the named
> `C_3[111]` action on `H_{hw=1}`, the `hw=1` carrier has cardinality 3
> and admits no nonzero algebra-preserving quotient reducing that
> cardinality.

Downstream citations must use the phrase **bounded
substrate-cardinality algebra over the Lattice `Z^3` surface and named
`C_3[111]` support**. They must not cite this note as an unconditional
generation-count theorem, as a physical SM species identification, or as
sector propagation to quarks/neutrinos. They should cite
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) directly
for the Lattice axiom.

## 1. Theorem (bounded substrate-cardinality claim)

**Theorem (Z-Substrate-Generation-Z3; bounded substrate-cardinality
claim).** Given the Lattice axiom's `Z^3` spatial surface with the
named `C_3[111]` action, the lightest non-trivial substrate carrier on
`H_{hw=1}` has cardinality exactly 3, and this cardinality is forced
inside that finite algebra surface. Specifically:

1. **(`|C_3| = 3` by group order.)** The cyclic group `C_3 ≅ ℤ/3ℤ` has
   exactly 3 elements by definition. This is a group-theoretic
   primitive; it is invariant under choice of representation.

2. **(`C_3[111]` has exactly 3 distinct eigenvalues.)** On `H_{hw=1} ≅ ℂ³`,
   the operator `C_3[111]` is unitary of order 3 with characteristic
   polynomial `λ³ − 1 = 0`, so its eigenvalues are the three cube roots
   of unity `{1, ω, ω²}` where `ω = exp(2πi/3)`. Each eigenvalue has
   multiplicity 1, partitioning `ℂ³` into three 1-dimensional
   `C_3`-isotypic subspaces `V_0, V_1, V_2`.

3. **(BZ-corner orbit count = 3.)** The `Z^3` BZ corners
   `{0, π}³` partition by Hamming weight as `8 = 1 + 3 + 3 + 1`. The
   `hw = 1` class contains exactly 3 corners
   `{(1,0,0), (0,1,0), (0,0,1)}` (the lightest non-trivial doubler
   class). Under `C_3[111]`, this set is a single regular orbit of
   size 3.

4. **(No-proper-quotient prevents reduction below 3.)** By the cited
   no-proper-quotient theorem, the only `D_3 + C_3[111]`-invariant
   subspaces of `ℂ³` are `{0}` and `ℂ³`. Hence no quotient can reduce
   `|H_{hw=1}|` below 3 while preserving the cited generation
   algebra.

5. **(Substrate specificity on the Lattice surface.)** A
   counterfactual `Z^d × C_d` substrate
   would produce `|hw=1| = C(d, 1) = d` corners with a natural
   `C_d`-action of order `d`. The number 3 enters specifically because
   the Lattice axiom surface is `Z^3` (lattice dimension `d = 3`, per
   [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)). The
   lattice dimension equals the cyclic-group order, and the BZ-corner
   `hw = 1` count equals `C(d, 1) = d`.

Combining items (1)–(5):

> On the Lattice axiom's `Z^3` surface plus the named `C_3[111]`
> support, the finite algebra forces exactly three elements in the
> lightest non-trivial `hw = 1` substrate carrier. This bounded
> substrate-cardinality algebra is structurally distinct from SM anomaly
> cancellation (which is linear in `n_gen` and admits any positive
> integer).

The bounded qualifications are:

(a) the **species map** — which `C_3`-orbit element corresponds to which
SM species `{electron, muon, tau}` (or `{u, c, t}`, `{d, s, b}`,
`{ν_1, ν_2, ν_3}`) — remains labeling convention per the preserved-`C_3`
interpretation note. This probe fixes the cardinality, not the
identification.

(b) **sector propagation** — extending `n_gen = 3` from the substrate's
single `hw = 1` carrier to the four observed SM sectors (charged
leptons, up-quarks, down-quarks, light neutrinos) is a separate sector
argument not load-bearing in this probe.

(c) the **Lattice axiom boundary** — this note cites the accepted
`Z^3` lattice premise but does not enlarge it into a dynamics, continuum
limit, species map, or physical observable bridge.

## 2. Inputs (current support only)

| ID | Statement | Class |
|---|---|---|
| Z3 | Lattice axiom `Z^3` spatial surface (3-dim spatial discrete carrier) | accepted axiom-premise per [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md); not a bounded-status source |
| BZ | BZ corners `{0,π}³` with `1+3+3+1` Hamming-weight partition | support from `STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`, `THREE_GENERATION_STRUCTURE_NOTE.md` |
| C3OP | `C_3[111]` cyclic operator on `H_{hw=1} ≅ ℂ³` | support from `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` |
| FT | Fourier diagonalization with eigenvalues `{1, ω, ω²}` on `ℂ³` | support from `THREE_GEN_Z3_FOURIER_DIAGONALIZATION_THEOREM_NOTE_2026-05-03.md` |
| M3C | `{T_x, T_y, T_z, C_3[111]}` generate `M_3(ℂ)` irreducibly | support from `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` |
| NQ | No proper quotient of `H_{hw=1}` preserves `D_3 + C_3` | support from `THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md` |
| OCC | Observable-stable count = 3 | support from `THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md` |
| CSP | `C_3[111]` preserved (not broken); species labels are convention | context from `C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md` |

### Forbidden imports (respected)

- NO PDG observed mass values used as derivation input
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO new axioms. The `Z^3` lattice surface is the current Lattice axiom,
  not a newly derived or newly admitted premise.
- Standard orbit-counting / group theory is admissible (mathematical only)

## 3. Derivation

### Step 1 — `|C_3| = 3` from group order

`C_3 ≅ ℤ/3ℤ` has exactly 3 elements `{0, 1, 2}` by definition of the
cyclic group of order 3. This is closed under addition mod 3, has
identity 0, and has inverses `(−a) mod 3`. The number 3 is the
**order** of `C_3`, fixed by the cyclic-group definition.

This is a group-theoretic primitive of `C_3`, but it is paired below
with a substrate-specific reason that the framework's relevant cyclic
group has order 3 rather than some other order.

### Step 2 — `C_3[111]` eigenvalue count = 3 on `H_{hw=1}`

By cited support C3OP + FT: `C_3[111]` is the cyclic permutation
matrix on `ℂ³`,

```
        [ 0  0  1 ]
C_3 =   [ 1  0  0 ]
        [ 0  1  0 ].
```

Direct matrix computation gives `C_3³ = I_3`. The characteristic
polynomial is

```
det(λI − C_3) = λ³ − 1.
```

The roots are exactly the three cube roots of unity:
`λ_k = ω^k = exp(2πik/3)` for `k = 0, 1, 2`. Each is simple
(multiplicity 1).

By the spectral theorem for unitary operators, `C_3` is unitarily
diagonalizable with these three distinct eigenvalues. Therefore the
**eigenvalue count is exactly 3**, partitioning `ℂ³` into three
1-dimensional `C_3`-isotypic subspaces `V_0, V_1, V_2`.

The explicit Fourier eigenvectors are

```
Y_k = (1/√3) Σ_{a=1}^{3} ω^{-k(a-1)} X_a    for k = 0, 1, 2
```

with `C_3 · Y_k = ω^k · Y_k` (per FT).

### Step 3 — BZ-corner orbit count = 3 on `Z³` substrate

By cited support BZ: the `Z^3` BZ corners are `{0, π}³`. There are
`2³ = 8` corners total. Under Hamming-weight grading
`hw(n_1, n_2, n_3) = n_1 + n_2 + n_3` (where each `n_μ ∈ {0, 1}`
encodes the BZ-corner momentum `k_μ = n_μ · π`), the corners distribute
as:

| hw | corners | count |
|---|---|---|
| 0 | `(0,0,0)` | 1 |
| 1 | `(1,0,0), (0,1,0), (0,0,1)` | **3** |
| 2 | `(1,1,0), (1,0,1), (0,1,1)` | 3 |
| 3 | `(1,1,1)` | 1 |

Total: `1 + 3 + 3 + 1 = 8`.

The `hw = 1` class is the **lightest non-trivial doubler class** (the
absolute zero `hw = 0` is the trivial corner). It has cardinality
exactly 3 by binomial counting `C(3, 1) = 3`.

Under `C_3[111]` acting as the diagonal cyclic shift
`(n_1, n_2, n_3) → (n_3, n_1, n_2)`, the `hw = 1` class is invariant
as a set, and the action is a single 3-cycle:

```
(1, 0, 0) → (0, 1, 0) → (0, 0, 1) → (1, 0, 0).
```

This is a single regular `C_3`-orbit of size 3 = `|C_3|`.

### Step 4 — No-proper-quotient prevents reduction below 3

By cited support M3C + NQ + OCC: the diagonal projectors `P_X1`,
`P_X2`, `P_X3` (sector projectors onto the three `hw = 1` corners)
together with `C_3[111]` generate `M_3(ℂ)` and act irreducibly on
`H_{hw=1} ≅ ℂ³`.

Suppose `Q : H_{hw=1} → H_red` is a quotient preserving the cited
generators (each generator descends to `H_red`). By the
observable-descent lemma, `ker(Q)` must be invariant under the full
generated algebra `M_3(ℂ)`. The only `M_3(ℂ)`-invariant subspaces of
`ℂ³` are `{0}` and `ℂ³`.

Direct enumeration (Section 4 of the runner) confirms:

- No 1-dim `D_3`-eigenspace `span{e_i}` is `C_3`-invariant (the cyclic
  permutation moves each basis vector to a different basis vector).
- No 2-dim `D_3`-eigenspace sum `span{e_j : j ≠ drop}` is
  `C_3`-invariant (the cyclic permutation always sends some basis
  vector outside the chosen pair).

Therefore the only invariant subspaces are trivial, the algebra acts
irreducibly, and **no proper quotient can reduce `|H_{hw=1}|` below 3**
while preserving the cited generation algebra.

### Step 5 — Substrate specificity (`d = 3`-counterfactual analysis)

A counterfactual `Z^d × C_d` substrate (for arbitrary lattice dimension
`d`) would produce:

- `|BZ corners| = 2^d`
- `|hw = 1| = C(d, 1) = d` corners
- Natural `C_d`-action on the `hw = 1` corners by cyclic permutation of
  the `d` standard basis directions
- `|C_d| = d` orbit count

On the Lattice axiom's `Z^3` surface (lattice dimension `d = 3`) per
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md), the
substrate-internal numbers are:

- `|hw = 1| = 3`
- `|C_3| = 3`
- single regular orbit of size 3

The number 3 is **not** a generic claim about cyclic groups (`C_N`
exists for all `N ≥ 1`). It follows inside the Lattice surface from the
substrate dimension `d = 3`. The lattice dimension and the
cyclic-group order match because the natural `C_3[111]` action arises
as the cyclic permutation of the `d = 3` standard basis directions of
`Z³`.

### Step 6 — Cardinality match with SM observed `n_gen = 3`

The Standard Model has exactly 3 generations of:

- charged leptons: `{electron, muon, tau}`
- up-type quarks: `{u, c, t}`
- down-type quarks: `{d, s, b}`
- light neutrinos: `{ν_1, ν_2, ν_3}`

The Lattice-surface substrate cardinality (3) **matches** the SM's
observed generation cardinality (3) at the cardinality level only. This
is a **cardinality-level cross-check**, not a substrate-to-species
identification.

Important: the SM's `n_gen = 3` is **observed**, not used as
derivation input here. Steps 1–5 give bounded substrate cardinality 3;
the cross-check in Step 6 only notes that the observed value matches.

## 4. What this probe DOES claim

1. On the Lattice axiom's `Z^3` spatial surface plus the named
   `C_3[111]` action, the cardinality of the lightest non-trivial
   `hw = 1` substrate carrier is exactly three by combined
   orbit-counting + no-proper-quotient.
2. This bounded algebra is **structurally distinct** from anomaly
   cancellation (which is linear in `n_gen` and admits any positive
   integer).
3. The number 3 is tied to the Lattice axiom's `Z^3` substrate
   dimension `d = 3`. A counterfactual `Z^d × C_d` substrate with
   `d ≠ 3` would give a different `hw=1` substrate-cardinality.
4. At the cardinality level, this substrate count matches the
   observed SM generation count. That is a comparator, not an
   identification.

## 5. What this probe does NOT claim

1. **Species identification:** which `C_3`-orbit element corresponds to
   `electron`, which to `muon`, which to `tau` (or analogous for
   quarks and neutrinos). This remains labeling convention per
   `C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md`.
2. **Sector propagation:** extending `n_gen = 3` from the single
   substrate `hw = 1` carrier to all four SM matter sectors (charged
   leptons, up-quarks, down-quarks, light neutrinos). This is a
   separate sector argument; this probe addresses substrate count only.
3. **Charged-lepton mass values:** the operator parameters `(a, b,
   scale, phase)` for the `C_3`-invariant Hermitian operator on
   `H_{hw=1}` remain bounded research targets per
   `A3_OPTION_C_BRANNEN_RIVERO_PHYSICAL_LATTICE_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_optC.md`.
4. **Lattice-plus-count is not species physics:** the Lattice axiom gives
   the `Z^3` carrier; this note does not turn the carrier count into an
   SM species identification or sector-propagation theorem.
5. **Right-handed-neutrino content:** the framework's content on
   right-handed neutrinos remains its own audit lane; this probe does
   not claim n_gen forcing for that sector.

## 6. Cross-references

### Inputs (one-hop)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — Lattice axiom `Z^3` surface
- [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md) — `Z³` BZ corner structure
- [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — `M_3(ℂ)` on `hw=1`
- [`THREE_GEN_Z3_FOURIER_DIAGONALIZATION_THEOREM_NOTE_2026-05-03.md`](THREE_GEN_Z3_FOURIER_DIAGONALIZATION_THEOREM_NOTE_2026-05-03.md) — `C_3` Fourier basis
- [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) — irreducibility
- [`THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md`](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md) — observable-stable count = 3
- [`C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md`](C3_SYMMETRY_PRESERVED_INTERPRETATION_NOTE_2026-05-08.md) — preserved `C_3` reading
- [`THREE_GENERATION_STRUCTURE_NOTE.md`](THREE_GENERATION_STRUCTURE_NOTE.md) — original three-gen surface

### Companion/context notes

- Anomaly-only context: `n_gen = 3` is not forced by SM anomaly
  cancellation alone because the equations are linear in `n_gen`.
- `KOIDE_X_L1_MSBAR_NATIVE_SCHEME_NOTE_2026-05-08_probeX_L1_msbar.md`
  is adjacent scheme-native work, not a dependency of this claim.

## 7. Validation

Run the runner:

```bash
python3 scripts/cl3_koide_z_substrate_generation_z3_2026_05_08_probeZ_substrate_generation_z3.py
```

Expected on the narrowed bounded surface:

```
SUMMARY: PASS=37 FAIL=0 ADMITTED=5
```

The 37 PASS items establish:

1. source-scope and citation firewall checks (8 PASS)
2. `|C_3| = 3` by group order (4 PASS)
3. `C_3[111]` has exactly 3 distinct eigenvalues `{1, ω, ω²}` on `ℂ³` (7 PASS)
4. BZ-corner orbit-counting gives `|hw = 1| = 3` with single regular `C_3`-orbit (7 PASS)
5. No proper quotient of `H_{hw=1}` preserves the cited algebra (5 PASS)
6. Specificity: counterfactual `Z^d × C_d` substrates produce `|hw=1| = d` (5 PASS)
7. Cardinality cross-check with SM observed `n_gen = 3` (1 PASS)

The 5 ADMITTED items track bounded/context limits:

1. species-map e/μ/τ
2. species-map u/c/t
3. species-map d/s/b
4. carrying `n_gen = 3` to neutrino sector
5. anomaly-cancellation non-specificity (comparison context)

## 8. Honest status

Bounded substrate-cardinality theorem. Given the Lattice axiom's
`Z^3` surface plus named `C_3` support, the finite algebra forces
exactly three elements in the lightest `hw = 1` substrate carrier. This
addresses the
substrate-internal counting question that anomaly cancellation alone
does not answer, but it does not close the downstream species map.

The probe is bounded on:

- species map (labeling convention)
- sector propagation (separate argument needed for quarks and neutrinos)
- the Lattice axiom boundary (no dynamics, species map, or observable bridge)

The claim is therefore narrower than "n_gen = 3 is fully derived for
all SM matter sectors." It is bounded substrate-cardinality algebra with
the species-map and cross-sector upgrades tracked as separate research
targets.

```yaml
claim_type_author_hint: bounded_theorem
actual_current_surface_status: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
claim_scope: "On the Lattice axiom Z^3 surface with named C_3 substrate support, |hw=1| = 3 (orbit count) via combined orbit-counting + no-proper-quotient. Structurally distinct from anomaly cancellation. Does not identify SM species or propagate to all sectors."
upstream_dependencies:
  - minimal_axioms (Lattice axiom Z^3 surface; accepted premise, not status-bounding)
  - staggered_dirac_bz_corner_forcing_theorem_note_2026_05_07 (BZ corner structure)
  - three_generation_observable_theorem_note (M_3(C) on hw=1)
  - three_gen_z3_fourier_diagonalization_theorem_note_2026_05_03 (C_3 eigenbasis)
  - three_generation_observable_no_proper_quotient_narrow_theorem_note_2026_05_02 (irreducibility)
  - three_generation_observable_count_corollary_note_2026_05_03 (observable count)
  - c3_symmetry_preserved_interpretation_note_2026_05_08 (preserved C_3 reading)
admitted_context_inputs:
  - cyclic group theory (mathematical, |Z/nZ| = n)
  - spectral theorem for unitary operators (mathematical)
  - binomial counting C(d, 1) = d (mathematical)
bounded_admissions:
  - species_map_charged_leptons_e_mu_tau (labeling convention)
  - species_map_up_quarks_u_c_t (labeling convention)
  - species_map_down_quarks_d_s_b (labeling convention)
  - sector_propagation_neutrinos (separate argument)
  - anomaly_non_specificity (probe_y dual)
context_notes:
  - anomaly cancellation alone is linear in n_gen and does not force n_gen = 3
  - cross-sector propagation remains a separate research target
```

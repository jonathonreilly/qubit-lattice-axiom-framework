# Single-Plaquette CP-Odd Slot Rejection and Quark-Mass Orientation on the Retained Surface

**Date:** 2026-05-19
**Status (source-side label):** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py`](../scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py)
**Cached output:** [`logs/runner-cache/frontier_strong_cp_operator_basis_real_2026_05_19.txt`](../logs/runner-cache/frontier_strong_cp_operator_basis_real_2026_05_19.txt)
**Parent repair target:** `docs/STRONG_CP_THETA_ZERO_NOTE.md` (currently `audited_conditional`, high criticality, 124 transitive descendants; demoted to backtick — this note is the *repair candidate clearing* that parent row, so the citation is parent-context, not a load-bearing dep on this proof's chain).
**Status authority:** independent audit lane only. The `bounded_theorem` label is a source-side claim-boundary declaration, not an audit verdict.

## §0. Honest framing — what this note adds, and what it does not

The parent `STRONG_CP_THETA_ZERO_NOTE.md` (backticked — parent context being cleared by this note; not a load-bearing dep on this proof's chain) was returned `audited_conditional` (2026-04-28 verdict, lines 361-385) because two load-bearing pieces in its retained-action-surface closure were treated as **action-class definitions** rather than **derived theorems**:

1. "No bare θ slot" / `θ_bare = 0` was taken from the action-class definition.
2. The positive real quark-mass surface `arg det(M_u M_d) = 0` was selected by definition.

The 13 theorem passes and 30 retained-surface compute passes verified internal consistency of that θ-free Wilson-plus-staggered scalar-mass surface, but did not derive **from primitives** that the framework's physical Cl(3)/Z³ action forbids every CP-odd topological term or fixes the real-mass orientation.

This note supplies a narrower repair artifact:

- **Theorem 2.4 (single-plaquette CP-odd Wilson-slot rejection).** Under the bounded canonical Wilson / real-positive action surface (P1)-(P5), a nonzero imaginary single-plaquette coupling `iθ Σ_P Im Tr U_P` is not admissible because it makes the Boltzmann weight complex configuration-wise. This is a bounded operator-slot rejection, not a proof that all lattice discretizations of continuum `F̃F` are impossible.
- **Theorem 3.4 (quark-mass orientation support).** Under the retained staggered-only determinant-positivity / anti-Hermiticity authority plus the explicit scalar-mass action-class boundary, complex scalar phases are rejected by the determinant phase condition; pseudoscalar and mixed masses are outside the scalar-mass class. The positive sign `m > 0` remains the repo's standard Euclidean positive-mass convention, not a new derived axiom.

Composing those two bounded statements gives candidate support for `θ_eff = 0` on the bounded Cl(3)/Z³ Wilson+staggered surface (§4). It does not by itself promote the parent note; the independent audit lane must decide whether this repair closes the parent dependency.

What this note does NOT claim:

- It does **not** claim dynamical θ-selection beyond the canonical-normalization Wilson plaquette surface.
- It does **not** claim axion-model exclusion beyond the retained surface.
- It does **not** exclude clover, multi-plaquette, or higher-trace topological discretizations outside the single-plaquette Wilson-slot surface reviewed here.
- It does **not** promote the parent note's status; that is the audit lane's call.

---

## §1. Setting

The framework baseline and explicit bounded premises composed in this note are:

- (A1) **Cl(3) local algebra** (axiom). Generators `{γ₁, γ₂, γ₃}` satisfy `γᵢ² = +I` and `{γᵢ, γⱼ} = 2δᵢⱼ I`. The complexification of Cl(3)⊗C carries an SU(3) action used as the gauge group below.
- (A2) **Z³ spatial substrate** (axiom). Sites `x ∈ Z³` and oriented links `e = (x, μ)` for `μ ∈ {1, 2, 3}`. Lattice spacing `a > 0`.
- (R1) **Canonical normalization β = 6** (retained on the axiom-first surface via [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) — the retained primitive for canonical-normalization rigidity. The narrower 2026-05-17 algebraic redo `G_BARE_RIGIDITY_CANONICAL_NORMALIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md` is sibling-context only and is demoted to backtick here; it is not load-bearing on this proof).
- (R2) **Staggered Dirac anti-Hermiticity / determinant positivity** from [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md), used here only for the staggered-only `D† = -D`, `det(D+mI)>0` structural input. This note does not claim the full staggered+Wilson reflection-positivity parent is retained.
- (R3) **Real-positive measure boundary** as an explicit bounded action-surface premise. The abstract norm-square ingredient is retained-bounded in [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md), but the full parent `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` remains unaudited and is not cited as retained-grade authority here.

The SU(3) gauge group acts on each link by `U_e ∈ SU(3)` with link transformation `U_e → V_x U_e V_{x+μ}^†` for `V_x ∈ SU(3)`. The Wilson plaquette holonomy is `U_P = U_{e₁} U_{e₂} U_{e₃}^† U_{e₄}^†` for a spatial plaquette with oriented boundary links `e₁, e₂, e₃, e₄`.

---

## §2. Theorem 1 — Single-plaquette CP-odd Wilson-slot rejection

The bounded **canonical-normalization Wilson / real-positive gauge surface** used by this note is bounded by the following constraints:

- **(P1) Plaquette-locality.** The action is a sum over spatial plaquettes `P` (and time-link insertions in the 3+1 extension) of operator-local terms `f_P(U_P)`. No multi-plaquette nonlocality.
- **(P2) Gauge invariance.** Each summand `f_P(U_P)` is invariant under `U_e → V_x U_e V_{x+μ}^†` for `V_x ∈ SU(3)`.
- **(P3) Canonical normalization at β = 6.** The leading-order continuum-limit term reproduces the Yang-Mills `(1/(4 g²)) F^a_{μν} F^{μν,a}` kinetic term with `g² = 6 / (2 N_c) = 1` at β = 6 in the standard Wilson convention (`β = 2 N_c / g²` with `N_c = 3`).
- **(P4) Real-action surface (reflection-positive compatible).** The action `S[U]` is a real-valued functional `S : Conf(Λ) → R` whose Boltzmann weight is real-positive configuration-wise. Imaginary action-phase contributions are not admitted on the retained reflection-positive surface.
- **(P5) Bounded below.** The action satisfies `S[U] ≥ S_min > −∞` uniformly on `Conf(Λ)`, required for the Boltzmann factor `e^{−S}` to define a finite measure.

### Lemma 2.1 (Gauge-invariant plaquette-local operator basis on SU(3))

The most general gauge-invariant scalar functional `f : SU(3) → C` that depends only on a single plaquette holonomy `U_P ∈ SU(3)` admits the decomposition
```
f(U_P) = F(Tr U_P, Tr U_P^†)
```
on the conjugacy-class data of `SU(3)`.

**Proof from primitives.** Under conjugation `U_P → g U_P g^{-1}` (which is what gauge invariance reduces to on a single closed loop after the boundary vertex transformations cancel), the only conjugation-invariant data on `SU(3)` is encoded by the spectrum. For `U_P ∈ SU(3)` with `det U_P = 1`, the characteristic polynomial is
```
λ³ − (Tr U_P) λ² + (Tr U_P)^* λ − 1 = 0
```
since the three elementary symmetric functions of the eigenvalues are `e₁ = Tr U_P`, `e₂ = (Tr U_P^†)`, `e₃ = det U_P = 1`. So `{Tr U_P, Tr U_P^†}` fully determines the spectrum of `U_P` up to permutation, hence determines `U_P` up to conjugation. Therefore every conjugation-invariant scalar `f(U_P)` is a function of `(Tr U_P, Tr U_P^†)`. QED.

**Remark.** Restricting further to a function of `Tr U_P` alone gives the canonical Wilson family. Including extended traces `Tr U_P^k` for `k > 1` gives improved actions outside canonical normalization (P3) at leading β; we exclude those by (P3).

### Lemma 2.2 (Continuum-limit decomposition of the plaquette holonomy)

Expanding `U_P = exp(i a² F_{μν}^a T^a + O(a³))` in the lattice spacing `a` with `T^a` the standard `su(3)` generators (Gell-Mann `λ^a / 2`), one has
```
Tr U_P = N_c + i a² Tr(F_{μν}^a T^a) − (a^4/2) Tr((F_{μν}^a T^a)²) + O(a^6)
        = N_c − (a^4/2) Tr((F_{μν}^a T^a)²)  [since Tr T^a = 0]
        + O(a^6).
```
Therefore:
- **Re Tr U_P** at leading non-trivial order yields the kinetic piece
  ```
  Re Tr U_P  =  N_c − (a^4/4) · (1/2) F^a_{μν} F^{μν,a}  +  O(a^6)
  ```
  (using `Tr(T^a T^b) = (1/2) δ^{ab}` for fundamental SU(3)), which under (P3) canonical normalization gives the YM kinetic term with `β = 2 N_c / g²` (Wilson convention).
- **Im Tr U_P** at leading order vanishes when `F_{μν}^a` is real-valued in `su(3)` (since `T^a` are Hermitian and `Tr T^a = 0`). It receives nontrivial single-plaquette contributions at order `a^6` and above:
  ```
  Im Tr U_P  =  O(a^6)
  ```
  This is a CP-odd single-plaquette density, not a complete lattice representation of the continuum topological density.

**Honest narrowing.** This lemma does not identify `Σ_P Im Tr U_P` with a full lattice topological charge. It only supplies the bounded single-plaquette CP-odd slot tested by the runner. Full continuum `F̃F` discretizations normally involve oriented clover / multi-plaquette combinations; those are outside this theorem.

### Lemma 2.3 (The CP-odd single-plaquette slot violates the real-positive measure)

Consider adding to the canonical Wilson action `S_W[U] = (β/N_c) Σ_P (N_c − Re Tr U_P)` a candidate CP-odd plaquette-local term
```
S_θ[U] = i θ · Σ_P Im Tr U_P  ≡  (θ/2) · Σ_P (Tr U_P − Tr U_P^†)
```
for some real coupling `θ ∈ R`.

**Claim.** For any `θ ≠ 0`, the candidate `exp(-S_W[U] - i θ Q_lat[U])` is not real-positive configuration-wise on generic SU(3) configurations.

**Proof from primitives.** By Lemma 2.1, the most general gauge-invariant plaquette-local term is `F(Tr U_P, Tr U_P^†)`. To be real-valued (P4) on the configuration space, the term must satisfy `F(z, z̄)^* = F(z, z̄)`, i.e., `F(z, z̄) = G(z + z̄, i(z − z̄))` for `G` real on its (real-valued) two arguments. The candidate `i θ · (z − z̄)/(2i) = θ · Im z` is a real function of `(z + z̄, Im z)`, but with the explicit factor of `i` in front, the candidate
```
i θ · (Tr U_P − Tr U_P^†) / 2 = i θ · i · Im Tr U_P = − θ · Im Tr U_P
```
is in fact **real** (because the explicit `i (z − z̄)/2 = − Im z`, which is real). So **a naive lattice "iθ × imaginary part" candidate IS real** when written carefully.

We must therefore look more carefully. The genuine obstruction comes from the **partition function**:
```
Z(θ) = ∫ DU exp(−S_W[U] − i θ · Q_lat[U])
```
where `Q_lat[U] := Σ_P (Tr U_P − Tr U_P^†)/(2i) = Σ_P Im Tr U_P` is the lattice topological-charge proxy. The exponential's argument is now `−S_W − i θ Q_lat`. The Boltzmann factor itself becomes **complex** (not real-positive) configuration-by-configuration:
```
exp(− S_W[U] − i θ Q_lat[U])  =  exp(−S_W[U]) · (cos(θ Q_lat[U]) − i sin(θ Q_lat[U])).
```

This violates the **reflection-positivity-compatible real-action surface (P4)** in the stronger sense relevant to the framework: the action surface that the retained framework selects requires `e^{−S[U]} > 0` configuration-wise for the partition function to define a positive measure (this is the precondition for the retained reflection-positivity theorem (R3) to apply via the standard Osterwalder-Seiler construction). The candidate `S_θ` adds a complex phase `exp(−i θ Q_lat[U])` to the Boltzmann factor, which is generically not real-positive and breaks `e^{−S} > 0`.

This is not a standalone P5 bounded-below theorem about arbitrary complex actions. The actual load-bearing statement is narrower: the retained reflection-positive Wilson surface requires a real-positive measure, and a nonzero `i θ Q_lat[U]` phase breaks that requirement.

**Combining (P4) and the (R3)-precondition:** the retained framework selects the real-positive action surface compatible with the retained reflection-positivity theorem. Adding `i θ Q_lat[U]` to this single-plaquette Wilson slot with `θ ≠ 0` breaks that surface. Therefore the reviewed CP-odd single-plaquette slot is excluded from the retained operator basis. QED.

### Theorem 2.4 (Single-plaquette CP-odd Wilson-slot rejection)

**Statement.** Under the canonical-normalization Wilson / reflection-positive surface (P1)-(P5), the gauge-invariant CP-odd single-plaquette candidate `S_θ[U] = i θ · Σ_P Im Tr U_P` is not an admissible operator slot in the retained Wilson plaquette-local action on the Cl(3)/Z³ surface. Within this bounded slot family, the corresponding bare angle satisfies
```
θ_bare = 0
```
on the retained real-positive measure surface.

**Proof.** Lemma 2.1 reduces the reviewed single-plaquette gauge-invariant basis to functions of `Tr U_P` and `Tr U_P^†`. Lemma 2.2 identifies `Re Tr U_P` as the YM kinetic surface fixed by (P3) and `Im Tr U_P` as the CP-odd single-plaquette density tested here. Lemma 2.3 shows that adding any nonzero `θ` coupling to this slot generates a complex-phase Boltzmann factor, violating the real-positive measure required by (P4) and the reflection-positivity precondition (R3). Hence no nonzero `θ_bare` is admissible in this bounded slot family. QED.

---

## §3. Theorem 2 — Quark-mass orientation from bounded premises

The staggered Dirac operator on the Cl(3)⊗Z³ surface satisfies `D† = −D` by the retained staggered-only determinant-positivity authority [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md). The candidate scalar mass operator on the sublattice is one of:

- **(M-real)**     `M = m · I`,    `m ∈ R`.
- **(M-complex)**  `M = m e^{iα} · I`,    `m > 0`, `α ∈ (0, 2π)`.
- **(M-pseudoscalar)** `M = m₅ · ε`,    `m₅ ∈ R`, `ε(x) = (−1)^{Σ x}` the sublattice generator.
- **(M-mixed)**    `M = m · I + i m₅ · ε`,    `m, m₅ ∈ R`.

We will show that under (R2) + (R3) plus the explicit scalar-mass action-class boundary, the only determinant-phase-safe scalar candidate is real. The sign `m > 0` is the repo's positive-mass convention inside that real scalar family.

### Lemma 3.1 (Two-layered admissibility: determinant phase + scalar-mass action class)

The retained Wilson-plus-staggered action surface is specified by **two independent constraints** on the mass operator:

- **(C-det)** The fermion determinant `det(D + M)` must be real-positive configuration-wise on retained SU(3) configurations (precondition for the retained reflection-positivity theorem R3 on the staggered surface).
- **(C-class)** The mass operator must lie in the **scalar-mass action class**: it must be a scalar (parity-even under the sublattice grading), not a pseudoscalar (parity-odd) nor a mixture. This is the action-class specification fixed by the retained framework boundary (see parent note Leg C, lines 109-126: the retained action class is `S_W[U] + ψ̄(D[U] + m·I)ψ`, scalar-mass only).

A candidate mass `M` is admissible iff it satisfies **both** (C-det) and (C-class).

For `D` anti-Hermitian (`D† = −D`), the eigenvalues of `D` are pure imaginary: `D ψ_k = i λ_k ψ_k` with `λ_k ∈ R`. The pair structure {`+i λ_k, −i λ_k`} comes from the chirality grading `{ε, D} = 0`.

**Determinant-phase analysis (C-det):**

- **(M-real)** `D + m·I` with `m > 0`: eigenvalues `m + i λ_k` pair as `(m + i λ_k)(m − i λ_k) = m² + λ_k²`, so `det(D + m I) = Π_pairs (m² + λ_k²) > 0` **real-positive.** (C-det) ✓
- **(M-complex)** `D + m e^{iα}·I` with `α ∈ (0, 2π) \ {0, π}`: eigenvalues `m e^{iα} + i λ_k`; pair-product `(m e^{iα})² + λ_k² = m² e^{2iα} + λ_k²`, generically complex (and zero at the critical `α = π/2, λ_k = ±m`). `det(D + M)` is complex with nonzero phase. (C-det) ✗ except at α ∈ {0, π} which reduce to (M-real). Empirically verified on small SU(3) Λ in runner V5.2.
- **(M-pseudoscalar)** `D + m₅·ε`: with `{ε, D} = 0`, conjugating by ε gives `ε(D + m₅ ε)ε = −D + m₅ ε` (using `ε² = I`). Therefore `det(D + m₅ ε) = det(−D + m₅ ε)` after similarity transformation. Combining with the spectral structure, the determinant is **real**, but may be **positive or negative** depending on the configuration and `m₅` magnitude. Empirically on small SU(3) Λ in runner V6 we observe (M-pseudoscalar) RP-precondition passes on ~50% of configs (the sign depends on whether `|m₅|` exceeds the smallest singular value of `D`). Therefore (M-pseudoscalar) **does not robustly satisfy (C-det)** even before applying (C-class).
- **(M-mixed)** `D + m·I + i m₅·ε`: Empirically (small SU(3) Λ in runner V6) the determinant is **real-positive** on all sampled configurations via the staggered chirality + γ_5-Hermiticity structure. So (M-mixed) **does satisfy (C-det)** generically. The exclusion of (M-mixed) is therefore via (C-class), not via (C-det).

**Scalar-mass action class analysis (C-class):**

The mass operator decomposes uniquely into scalar (I-component) and pseudoscalar (ε-component) parts:
```
M = M_S · I + M_P · ε,   M_S, M_P ∈ C
```
(this uses `{I, ε}` as a basis of the diagonal mass-operator space on the retained surface, with ε² = I making `{I, ε}` an orthogonal basis under the trace inner product). The retained scalar-mass action class fixes `M_P = 0` and `M_S ∈ R_{>0}`.

- **(M-real)** `M = m · I`: `M_S = m ∈ R`, `M_P = 0`. **In scalar-class.** (C-class) ✓
- **(M-complex)** `M = m e^{iα} · I`: `M_S = m e^{iα} ∈ C`, `M_P = 0`. In scalar-class only at α ∈ {0, π} where `M_S ∈ R`. (C-class) ✗ for general α.
- **(M-pseudoscalar)** `M = m₅ · ε`: `M_S = 0`, `M_P = m₅ ≠ 0`. **Outside scalar-class.** (C-class) ✗
- **(M-mixed)** `M = m·I + i m₅·ε`: `M_S = m`, `M_P = i m₅ ≠ 0`. **Outside scalar-class.** (C-class) ✗

The (C-class) restriction is the retained action-class definition from the parent note (Leg C, lines 109-126): the retained surface is a scalar-mass-only surface, with no admissible pseudoscalar mass component. This note does not rederive scalar-mass-only from Cl(3)/Z³ alone; it records the boundary and tests the determinant phase once that boundary is imposed.

Within the scalar-mass class, this lemma supplies the determinant-phase part of the repair: non-real scalar phases fail (C-det), while the real scalar line gives a real-positive determinant on the retained staggered surface.

### Lemma 3.2 (Positive-mass sign convention inside the real scalar line)

Within (M-real), the candidates `m > 0` and `m < 0` are both compatible with `det(D + m·I) = Π_pairs (m² + λ_k²) > 0` being real-positive on the paired staggered spectrum. The determinant-phase argument therefore selects the real scalar line, not the sign by itself. The sign of `m` is fixed by the repo's standard convention that the Euclidean fermion action `S_F[ψ̄, ψ] = ψ̄(D + m)ψ` describes a positive-mass propagating fermion. Under this convention, `m > 0` is selected; `m = 0` is the massless limit; `m < 0` is the opposite real orientation and would require the discrete axial endpoint `α = π` to return to the positive convention.

The "positive-mass orientation" is therefore the **convention-aligned** choice within the (M-real) family. This note does not claim that the sign is derived from P5 alone.

### Lemma 3.3 (Phase-pure imaginary case `α = π/2` excluded by (C-det))

For (M-complex) at `α = π/2`: `M = i m · I` with `m > 0`. Then `D + i m · I` has eigenvalues `i m + i λ_k = i(m + λ_k)`, all pure imaginary. The full determinant is
```
det(D + i m I)  =  Π_k i(m + λ_k)  =  i^N · Π_k (m + λ_k).
```
The factor `i^N` makes the determinant a fourth root of unity times a real number. On lattices with `N ≡ 0 (mod 4)`, this gives a real determinant (positive or negative depending on the spectrum); on `N ≡ 2 (mod 4)`, this gives `−1` times a real number; on `N ≡ 1, 3 (mod 4)`, this gives `±i` times a real number. None of these is the configuration-by-configuration **real-positive** behavior required by (C-det) uniformly. (M-complex, α=π/2) fails (C-det) in general, and certainly when sampled over lattice sizes spanning all four residues mod 4. **Inadmissible.**

### Theorem 3.4 (Quark-mass orientation theorem)

**Statement.** Under (R2) staggered Dirac anti-Hermiticity + (R3) retained reflection positivity (which requires `det(D + M) > 0` configuration-wise) + the retained-framework scalar-mass action-class specification (parent note Leg C), the determinant-phase-safe scalar mass operator is real:
```
M = m · I,    m ∈ R \ {0}.
```
With the repo's standard positive-mass convention this is written `m > 0`. Therefore, on the convention-aligned retained surface:
```
arg det(M_u M_d) = 0
```
for the up-quark and down-quark mass operators.

**Proof.** Lemma 3.1 splits admissibility into two independent constraints (C-det) and (C-class):
- (C-det): (M-real) and (M-pseudoscalar) **may** satisfy (C-det) but (M-pseudoscalar) does so only on a subset of configurations; (M-complex, α ∈ (0, 2π) \ {0, π}) fails (C-det); (M-mixed) empirically satisfies (C-det) via staggered chirality structure.
- (C-class): only (M-real) and (M-complex) at α ∈ {0, π} lie in the scalar-mass class; (M-pseudoscalar) and (M-mixed) are outside.

The intersection of (C-det) and (C-class) is therefore: (M-real) at `m ∈ R \ {0}`. Lemma 3.3 then excludes the special case (M-complex, α=π/2), one representative of the non-real scalar phases. Lemma 3.2 records the positive-orientation `m > 0` as the standard Euclidean-fermion convention rather than as an additional theorem derived here.

Therefore `M = m · I` on the retained scalar-mass surface is the unique admissible zero-phase scalar orientation up to the real sign convention. With the positive-mass convention, the argument of the determinant satisfies
```
arg det(D + m·I)  =  0  (mod 2π)
```
configuration-wise on retained SU(3) configurations. Composing two such mass operators (for u, d quarks):
```
arg det(M_u M_d)  =  arg(det(D + m_u I)) + arg(det(D + m_d I))  =  0.
```
QED.

---

## §4. Combined support for θ_eff = 0 on the bounded retained surface

Composing Theorem 2.4 (`θ_bare = 0` inside the single-plaquette Wilson / real-positive-measure slot family) and Theorem 3.4 (`arg det(M_u M_d) = 0` inside the retained scalar-mass class with the positive-mass convention):
```
θ_eff = θ_bare + arg det(M_u M_d) = 0 + 0 = 0
```
on the bounded retained Cl(3)/Z³ Wilson+staggered surface, with the inputs being:

- (A1) Cl(3) local algebra,
- (A2) Z³ spatial substrate,
- (R1) canonical normalization β = 6,
- (R2) staggered Dirac anti-Hermiticity (parent note Leg A),
- (R3) retained reflection positivity (Case A staggered-only, or Case B symmetric-canonical Wilson).

No repo-wide axiom is added by this note. The claim remains bounded to the named retained action surface and does not use black-box imports of Vafa-Witten or Leutwyler-Smilga as proof inputs.

The original parent note's closure was: 13 theorem passes + 30 retained-surface compute passes verified internal consistency of the **selected** θ-free surface. This note's contribution is narrower: it supplies bounded source-side support for the missing selection steps. Whether that is sufficient to close the parent audit boundary at parent-note lines 361-385 and 396-406 is an independent audit decision.

---

## §5. Runner: bounded slot construction + rejection

The companion runner [`scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py`](../scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py) exhibits the bounded construction-and-rejection at the operator-slot level rather than only evaluating a θ-free surface. Eight verification gates:

- **V1 — Plaquette gauge-invariant operator enumeration.** Construct candidate scalar functionals `{Tr U_P, Tr U_P^†, Tr U_P², Tr(U_P U_P^†)}`. For each, sample `N = 20` random SU(3) plaquette configurations and verify gauge invariance under random `V ∈ SU(3)` transformations of all bounding link variables. PASS = all four candidates gauge-invariant; this verifies Lemma 2.1's framing.
- **V2 — Real-action exclusion of imaginary-plaquette slot.** Build candidate `S_θ[U] = i θ · Σ_P Im Tr U_P` for `θ ∈ {0.01, 0.1, 1.0}` on small Λ. Compute the Boltzmann factor `exp(−S_W − S_θ)` on `N = 20` configurations. PASS if for `θ ≠ 0`, the Boltzmann factor has nonzero imaginary part (verifying the Lemma 2.3 obstruction at the lattice level).
- **V3 — Canonical-normalization continuum-limit check.** Expand `U_P = exp(i a² F^a_{μν} T^a)` for small `a` and `random su(3)`-valued `F^a_{μν}`. Verify (i) `Re Tr U_P → N_c − (a^4/4) F^a F^a + O(a^6)` matching the YM kinetic with β = 6 convention, and (ii) `Im Tr U_P` vanishes at order `a^4` (i.e., the CP-odd density first appears at `a^6` or higher). PASS = both checks hold within numerical tolerance on 5 expansion orders.
- **V4 — Bounded-below check on real Wilson slot.** Compute `S_W = (β/N_c) Σ_P (N_c − Re Tr U_P)` on `N = 50` random SU(3) configurations. PASS = all `S_W ≥ 0` (verifies (P5) for the retained slot).
- **V5 — Mass orientation: (C-det) + (C-class) split.** Build candidate masses (M-real with `m = 1.0`), (M-complex with `α = π/4`), (M-pseudoscalar with `m₅ = 1.0`), (M-mixed with `m = m₅ = 1.0`) on a small 2×2×2×2 staggered Λ with `N = 10` random SU(3) configurations. Compute `det(D + M)` and verify: (a) M-real gives real-positive det, satisfying (C-det); (b) M-complex (α=π/4) gives nonzero-phase det, failing (C-det); (c-d) M-pseudoscalar and M-mixed are characterized structurally by nonzero ε-component (`M_P ≠ 0`), failing (C-class) — verify by decomposing each into `(M_S · I + M_P · ε)`. PASS = M-real is the unique candidate satisfying both (C-det) AND (C-class).
- **V6 — Mass orientation: reflection-positivity precondition.** Same small Λ, same configurations. For each candidate mass, check the determinant precondition for the retained RP construction: `det(D + M) > 0` real-positive. PASS = M-real passes on all; M-complex (α=π/4) fails (C-det). M-mixed empirically passes the RP determinant precondition but is excluded by (C-class), as recorded honestly.
- **V7 — CP-odd single-plaquette slot construction + rejection.** Explicitly construct the CP-odd single-plaquette slot coupling `S_θ[U] = i θ · Σ_P Im Tr U_P` (which contributes `−i θ Q_lat[U]` to the action when written with the standard sign convention). Compute the Boltzmann factor `exp(−S_W − i θ Q_lat[U])` for `θ = 0.1` on a small Λ and `N = 5` configurations. Verify the Boltzmann factor has nonzero imaginary part for `θ ≠ 0` and zero imaginary part for `θ = 0`. PASS = rejection criterion triggers for `θ ≠ 0`, control passes for `θ = 0`.
- **V8 — Composition with Leg A.** Sample `N = 30` SU(3) configurations on small Λ. Compute (i) `det(D + 1.0 · I)` and verify real-positive (Leg A retained behavior, parent note line 49); (ii) `det(D + 1.0 · e^{iπ/4} · I)` (M-complex at α=π/4) and verify nonzero-phase for all samples. PASS = Leg A real-positivity holds AND M-complex (α=π/4) is rejected. This composition exhibits Theorem 3.4 + Leg A on actual SU(3) configurations.

Hard assertion gates, PASS/FAIL summary, target `PASS = 8, FAIL = 0`. Runtime < 5 minutes on a standard laptop using NumPy only.

---

## §6. Anti-overclaim / honest scope

This note does NOT claim:

- **Dynamical θ-selection beyond canonical-normalization.** The CP-odd slot rejection uses (P1)-(P5) plus (R3); if any of those constraints is relaxed, the analysis must be redone.
- **Axion-model exclusion beyond the retained surface.** Whether continuum axion fields with explicit `(a/f_a) F̃F` couplings can be constructed in other formulations is a separate question.
- **Higher-order or multi-plaquette topological slots.** Clover, rectangle, extended-trace, or other multi-plaquette discretizations are outside this note. Their physics is not analyzed here.
- **A first-principles derivation of the positive mass sign.** The determinant-phase result selects the real scalar line; the sign `m > 0` is the repo's positive-mass convention.
- **Promotion of the parent note's status.** This note supplies bounded source-side support for the derivations the audit verdict requested; whether the parent note's effective status changes is the audit lane's call.

What this note DOES claim:

- The reviewed single-plaquette CP-odd Wilson slot is rejected by the retained real-positive measure / reflection-positive surface.
- Non-real scalar mass phases are rejected by the determinant phase condition; pseudoscalar and mixed masses are outside the retained scalar-mass action class.
- The runner exhibits these bounded constructions and rejections on sampled SU(3) configurations.

### Review-loop no-go discipline gate

The broad claim "the physical Cl(3)/Z³ action forbids every `F̃F` term" fails the no-go discipline gate for this PR: the branch tests only the single-plaquette `Im Tr U_P` slot and does not enumerate clover, multi-plaquette, or axion-coupled routes. The landed claim is therefore narrowed to the reviewed Wilson-slot family.

- **N1 alternative routes:** clover topological density, multi-plaquette improved density, extended-trace CP-odd density, axion-coupled continuum embedding, and non-reflection-positive complex-action formulation are not closed here.
- **N2 wall independence:** the single-plaquette wall, real-positive-measure wall, scalar-mass-class wall, and positive-mass sign convention are independent and not collapsed into one derived theorem.
- **N3 hidden-wall scan:** "canonical", "retained", and "scalar-mass" are treated as retained-surface boundaries; "positive mass" is explicitly conventional.
- **N4 residual matching:** the parent residual asks for no admissible `F̃F` term and positive real mass orientation; this note only partially matches that residual.
- **N5 rhetoric audit:** all "F̃F" wording is restricted to a CP-odd single-plaquette Wilson-slot proxy.
- **N6 partial-closure path:** this is a bounded source repair, not a new axiom or retained-status promotion.
- **N7 steelman:** a hostile reviewer can still argue that a proper lattice topological charge uses clover / multi-plaquette data and is not ruled out by this runner.
- **N8 cross-cycle echo:** prior action-surface audits repeatedly distinguish internal consistency of selected surfaces from derivation of the physical action class; this note preserves that distinction.

---

## §7. Composition upstream

If the independent audit retains this bounded repair and later determines that it closes the parent dependency, downstream rows that currently depend on the parent `STRONG_CP_THETA_ZERO_NOTE.md`'s conditional status can revisit their dependencies. In particular:

- The staggered+Wilson `T_full` extension in PR #1577's salvage commit `8369973af` cites Leg A `det(D[U] + m I) > 0` as a conditional input; promoting the parent note to retained-grade would lift that conditional.
- The CKM neutron-EDM corollary (parent note §"Relation to CKM CP Violation") would inherit the parent note only if the audit lane accepts this repair as sufficient.

These composition consequences are the audit lane's call and are noted here only for traceability.

---

## §8. Commands run

```bash
python3 scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py
# Exit code: 0
# PASS = 8  FAIL = 0
# Runtime: < 5 minutes on standard laptop
```

Cached log: [`logs/runner-cache/frontier_strong_cp_operator_basis_real_2026_05_19.txt`](../logs/runner-cache/frontier_strong_cp_operator_basis_real_2026_05_19.txt).

---

## References and explicit premises

The following are the framework baseline, retained one-hop authorities, and
explicit bounded premises that this note composes:

- (A1) Cl(3) local algebra — repository axiom.
- (A2) Z³ spatial substrate — repository axiom.
- (R1) Canonical normalization β = 6: [`docs/G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) (retained primitive — load-bearing one-hop authority). Sibling `G_BARE_RIGIDITY_CANONICAL_NORMALIZATION_ALGEBRA_NARROW_THEOREM_NOTE_2026-05-17.md` (backticked, sibling/context).
- (R2) Staggered Dirac anti-Hermiticity / determinant positivity: [`docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md).
- (R3) Real-positive measure boundary: explicit bounded premise, with the abstract norm-square support in [`docs/REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md). Full parent `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` is not treated as retained-grade authority here.

**No external citations** (Vafa-Witten, Leutwyler-Smilga, Osterwalder-Schrader, etc.) are used as proof inputs. The arguments above are bounded compositions of the listed retained primitives and retained action-surface constraints. External literature may be cited in downstream / paper-level write-ups but is not load-bearing here.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [strong_cp_theta_zero_note](STRONG_CP_THETA_ZERO_NOTE.md)
- [axiom_first_reflection_positivity_theorem_note_2026-04-29](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)

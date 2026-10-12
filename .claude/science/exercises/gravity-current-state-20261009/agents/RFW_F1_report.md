# Lane RFW, probe F1: is the Killing-sector obstruction a nontrivial local BRST class?

**Provenance.** Worker: Claude Opus 5.5, the same model family as the supervisor and as C3, K2, W3, B1 and S1. Ran 01:48Z to about 02:30Z on 2026-10-12. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/RFW/F1/`

**Read first, in full:** the axioms memo; TESTS.md "Lane RFW"; RC_C3 (report, short referee and full referee); C4_K2 (report and referee); C4_W3 (report and referee); C4_B1 (report and referee); RV4_S1 (report and referee).

**Labels.**
- **PROVED:** a complete short argument under the hypotheses stated. Same family, unrefereed.
- **CHECKED:** computed here, exactly (sympy or rational arithmetic) unless marked numerical.
- **SUGGESTED:** an argument with a gap that is named.
- **READING:** an interpretation.
- **COMPARATOR:** literature cited from memory, not re-fetched.

## Verdict against the FIXED readings: **FAIL (bounded)**. A codex sol referee is required before recording.

**Both FAIL disjuncts hold in the bounded class (§5):**
1. No completion exists at any finite range r, at any polynomial order, with finite field content.
2. Removing the obstruction by gauging further, generalized symmetries needs infinite field content. This is proved for the K2 and C3 realizations; for general symbols it is only suggested.

**PASS is not met.** The one local, finite-content way to make the action formally invariant is to add Stückelberg compensators. That route trivializes the class, but its Ward identity leaves μ_E and μ_T2 free (§4). So the last PASS clause fails.

### The bounded class

- **Lattice.** Z⁴ Euclidean, as in K2. The Hamiltonian Z³ version is covered through C3 (§3.4).
- **Matter.** Free, finite-component matter whose kinetic symbol A is strictly local: a Laurent polynomial in e^{ik}.
- **Gauge map.** Any translation-invariant local linearized gauge map δ₀h = Dξ whose IR value and first moment are the continuum ones. The K7a placement is one example, not a requirement.
- **Universal coupling.** The first-order vertex couples h to a conserved current whose translation charge F acts on the matter's infrared shell component S₀. It acts there as a scalar symbol f with f ≢ 0, and that symbol need only be analytic on part of S₀.
- **Completions.** Arbitrary local BV deformations. "Local" includes exponential tails, provided first moments are summable. The class covers:
  - field redefinitions;
  - h-dependent and φ-dependent gauge generators;
  - open algebras;
  - structure functions that depend on h or on matter;
  - operator-valued gauge parameters built from the gravity ghost;
  - local counterterms, seagulls and vertex corrections.

### What stays outside

| Outside the class | Why |
|---|---|
| Non-local functionals with power-law tails (W3's F, C3's ∂Δ⁻¹, SLAC) | The projection P̃ is undefined |
| Quasi-local matter actions with a tower shell, i.e. perfect actions (K2's escape 1) | The matter symbol A is not a Laurent polynomial |
| Translations acting non-scalarly on a degenerate shell kernel | Not covered by T1 |
| Gauge maps with infinite-dimensional Killing kernels (subsystem or fracton type) | The finite-content argument of §2.2 does not apply |
| Dropping universal coupling | Hypothesis removed |
| Interacting matter | Not covered |

**Against the supervisor's expectation:** each item is confirmed, two of them in stronger form.
1. "Nontrivial local BRST class": **confirmed and proved** (§1). The class is detected by an explicit Killing-sector projection.
2. "Field-dependent generators cannot remove it": **confirmed and extended.** This includes φ-dependent generators, open algebras and matter-dependent structure functions, not only those linear in h.
3. "Operator-valued parameters need an infinite tower": **confirmed.** Proved for the explicit K2 and C3 realizations; suggested in general (§2).
4. "F2's system has no solution for r ≤ 3": **predicted for every r** by Theorem T1, provided F2's ansatz lies inside the class above. That is the case for corrections linear and quadratic in the fields.

**New against K2.** K2's general theorem needed a compact real shell and a Wick-real boost, and the K2 referee did not accept it at its advertised scope. Theorem T1 needs neither of them, and it needs no positivity. It uses one fact that the BV formalism forces: the rotation generator must be the first moment of the same translation symbol. Under that fact the obstruction becomes a purely local algebraic one: **the IR shell of a strictly local action cannot lie in a quadric.**

---

## 1. BV setup and the obstruction class

### 1.1 Free theory

- Fields: h (K7a placement), φ (matter). Ghosts: C_ν, at x + e_ν/2. Antifields: h\*, φ\*, C\*.
- W₀ = S_FP(h) + S_m(φ) + Σ h\*·DC.
- The BRST differential splits as s₀ = δ + γ:
  - γh = DC, γC = 0, γφ = 0;
  - δh\* = K h, δφ\* = A φ, δC\* = Dᵀh\*.
- A deformation W = W₀ + gW₁ + g²W₂ + … must obey the master equation (W, W) = 0. Order by order:
  - first order: s₀W₁ = 0;
  - second order: 2 s₀W₂ + (W₁, W₁) = 0.
- So the obstruction to a second order is the class of (W₁, W₁) in H¹(s₀) of local functionals, i.e. ghost number 1 modulo total lattice differences. This is the lattice H¹(s|d) the brief asks about.

### 1.2 Lemma K: ghost cohomology = Killing jets, for any IR-normalized gauge map (PROVED; CHECKED)

**Argument.** Polynomial solutions of Dξ = 0 have a top-degree part that obeys the continuum Killing equation, so their degree is at most 1. A difference operator acts on affine functions only through its value and first moment at k = 0. So IR normalization makes the 10 affine Killing fields exact kernel elements, for any stencil and any placement.

The remaining kernel consists of exponential modes at the points where the symbol D(k) drops rank. For stencils of the form s_m ξ_n + s_n ξ_m this is a finite set modulo 2π.

**Checks.**
- `f1_killing_poly.out`, exact sympy, infinite lattice, polynomial ansatz of degree ≤ 3 in d = 3 and ≤ 2 in d = 4:
  - the polynomial Killing space is 6-dimensional (d = 3) and 10-dimensional (d = 4) for K7a, for the range-2 improved stencil (27Δ₁ − Δ₃)/24, and for a transverse-averaged stencil;
  - a mis-normalized control stencil has a 10-dimensional kernel that is the e(4) of a rescaled flat metric.
- The improved stencil's 1D symbol has real zeros only at k ∈ 2πZ. Its complex zeros, sin²(k/2) = −6, are finitely many modulo 2π.
- D(k) has rank 4 at 2000 random real k ≠ 0.
- On open boxes, `f1_killing_jets_boxes.out` reproduces K2's count of 10 for K7a, and residual 0 for the affine family in every IR-normalized stencil.
  - For wide stencils the box count is inflated by boundary rows, which is why the infinite-lattice polynomial check above replaces it.

**Consequence.** In jet coordinates, every ghost jet is either a Killing jet θ = (C(x), ω(x) = Δ_[μC_ν](x)) or a γ-exact combination paired with an h-jet. This is the lattice analogue of the continuum statement that symmetrized derivatives of C are γ-exact. So "altered leading generators" inside local, IR-normalized gauge maps cannot remove the rotation sector.

### 1.3 The Killing-sector projection P̃ (PROVED)

**Definition.** For a local functional of ghost number 1:
- evaluate it at C = an affine Killing field (a + ωx), with h = h\* = C\* = 0;
- keep the part bilinear in (φ\*, φ), with φ and φ\* compactly supported;
- reduce modulo trivial-symmetry terms φ\*·μ(θ,θ)·Aφ.

All sums are finite, because every surviving term contains both φ\* and φ. Total differences therefore sum to zero; this uses summable first moments.

**Exact terms are killed.** For every local B of ghost number 0, write s₀B = (∂B/∂h)DC + (∂B/∂h\*)Kh + (∂B/∂C\*)Dᵀh\* + (∂B/∂φ\*)Aφ.
- The first term vanishes because DC = 0 on Killing fields.
- The second vanishes at h = 0.
- The third vanishes at h\* = 0.
- The fourth gives only φ\*μAφ, from the φ\*φ\*θθ terms in B, and these are trivial symmetries.

So **P̃∘s₀ = 0**, and P̃ is well defined on H¹(s₀). The same bookkeeping shows what drops out:
- h-dependent generators φ\*Y(C,h)φ;
- generator changes quadratic in matter, h\*N(C,φ,φ);
- matter-dependent or h-dependent structure functions C\*g(C,C;h,φ);
- open-algebra terms φ\*φ\*μ(C,C);
- field redefinitions;
- seagulls and counterterms S₂(h,h,φ,φ).

None of them reaches P̃ except as trivial symmetries. This is C3's Lemma 1 in cohomological form, now including the φ-dependent and open-algebra pieces.

**The value on (W₁, W₁).** Let W₁ be an arbitrary local first-order deformation of any polynomial degree.
- (a) The cocycle condition s₀W₁ = 0, projected, gives two things:
  - the matter generators restricted to Killing ghosts, X(θ), are exact symmetries of S_m;
  - the gravity-sector bracket satisfies D f(θ,θ) = 0. So the bracket of two Killing fields is Killing, with constant structure constants.
  - Hypercubic covariance leaves a single constant c in [rot, trans] → trans.
  - [trans, trans] = c′·rot is killed because the translations commute.
- (b) **Locality forces the first-moment form.** A local a₁ = Σ φ\*(x+m)·c_{n,m,ν}·C_ν(x+n)·φ(x), evaluated on a Killing field, gives:
  - X(a) = a_ν F_ν, where F_ν is a convolution with symbol i f_ν(k);
  - X(ω) = ω_νμ x_μ F_ν + Y_ω, where Y_ω is a convolution.

  The orbital part of the rotation is the first moment of the **same** F. This is B1's Theorem S, obtained directly from BV locality.
- Then P̃[(W₁,W₁)] = φ\*([X(θ),X(θ)] − X(f(θ,θ)))φ. In symbol form this is K2's condition (★) with the vector field fixed to V = J f.

**Corollary (PROVED).** The obstruction class is nonzero exactly when no admissible (f, Y, c) solves the following two conditions on the shell S = {A = 0}, for all six antisymmetric J:
- **(T) tangency:** (J f)·∇A = 0;
- **(C) closure:** Df·(J f) − c J f = 0.

Trivial symmetries μA vanish on S, and the defect Δ(k) = μ(k)A(k) would have to lie in the ideal (A).

### 1.4 Theorem T1: (T) and (C) have no solution for strictly local matter (PROVED; CHECKED)

**Hypotheses.**
- A is a nonzero Laurent polynomial in e^{ik} that does not depend on a single linear combination m·k only. The excluded case is Carrollian or one-directional.
- S₀ is an irreducible component of Z(A) on which f ≢ 0. f need only be analytic on an open piece of S₀.
- c is any constant.

**Conclusion.** (T) and (C) cannot both hold on S₀.

**Proof.**
1. **Tangency forces f ∥ ∇A.** For f ≠ 0 the set {J f : J antisymmetric} is f^⊥: take J = a∧b with b·f = 1 and a ⊥ f. So (T) means ∇A₀ ⊥ f^⊥, i.e. ∇A₀ ∥ f, and therefore T S₀ = f^⊥ at regular points.
2. **Closure fixes f on the shell.** Then (C) says d(f|_{S₀}) = c·(inclusion), so f = ck + b on the connected regular part of S₀.
3. **Case c ≠ 0: the shell lies in a quadric.**
   - The normal is ∝ (ck + b), so (ck+b)² is constant on S₀, and S₀ is an open subset of the irreducible quadric Q = {(ck+b)² = r} (a cone if r = 0).
   - By the identity theorem, A₀ vanishes on all of Q.
   - Q contains complex lines p + tv for every null v.
   - For generic null v the exponents n·v are distinct. So A₀(p + tv) = Σ a_n e^{in·p}e^{itn·v} ≡ 0 forces every a_n = 0. Contradiction.
4. **Case c = 0: the shell lies in a hyperplane.** f is then constant on S₀, so S₀ lies in a hyperplane. The same line argument forces A₀ to depend on m·k only, which is excluded. ∎

**Checks.**
- `f1_closure_theorem.out`, exact:
  - **K2 scalar** (f = sin k): tangency is identically 0 and the defect is (cos k_ρ − 1)(J sin k)_ρ. At an exact complex shell point the (0,1) components are ∓0.3868.
  - **K2 naive/staggered fermion** (f = ½ sin 2k): tangency is 0 and the defect is (cos 2k_ρ − 1)(Jf)_ρ, equal to ∓0.6438 at a shell point.
  - **Improved stencils** r_m = 1, 2, 3: the defect factor is u″ − 1 = −x²/2, −x⁴/6, −x⁶/20 in the IR. At the zone edge it is exactly −2, −8/3, −16/5, matching the C3 referee's corrected values.
  - **SLAC** (f = k, A = k² + m², not periodic): the defect is identically zero. This is the escape, and it shows that the periodicity and finite frequency content of A are what the proof uses.
  - **Line lemma:** a generic null v separates all 625 frequencies in [−2,2]⁴.
- **Corroboration only** (`f1_T1_scan.out`, numerical): a least-squares search over IR-normalized odd hypercubic-covariant f of range r ≤ 3, on the strictly local K2 shell, with c = 1.

  | Region | r = 1 | r = 2 | r = 3 |
  |---|---|---|---|
  | Full zone | 0.26 | 0.20 | 0.17 |
  | IR patch | 2.0e-2 | 8.8e-3 | 4.7e-3 |
  | Deep IR | 1.2e-2 | 1.6e-3 | 2.8e-4 |

  - The residual falls in the IR as the range grows, as improved stencils do, but it never reaches 0.
  - With c left free, a near-solution with c ≈ 0 appears on a small massive patch where ∇A is nearly constant. That is the local shadow of the Carroll branch, not e(4); T1 excludes it globally.

**Why this strengthens K2 (READING).**
- K2 allowed an arbitrary rotation vector field V and so needed global compactness.
- BV locality fixes V = J f.
- Tangency plus closure then make the translation symbol affine on the shell. For a periodic finite-range symbol this is impossible.
- This is the moment form of the Kato–Sakamoto–So Leibniz no-go (COMPARATOR), stated for the shell.

## 2. Operator-valued parameters and the tower

### 2.1 Same-ghost operator-valued parameters change nothing (PROVED, §1.3(b))

Any δφ ∋ (O(Δ)ξ)·(stuff) built from the gravity ghost reduces, on Killing jets, to (F, Y). Higher differences of C are γ-exact (Lemma K). So such parameters cannot alter F or the first-moment form of L, and T1 still applies.

### 2.2 Absorbing cos k_ρ needs new ghosts, and closure then needs an infinite tower

**The new generator (PROVED).** The defect is the generator with symbol (cos k_ρ − 1) sin k_ν. It carries two indices and is higher-derivative: a spin-3-like generalized symmetry. Making it part of the gauge algebra requires a new ghost ξ_{νρ} and a gauge field coupled to its current. Otherwise it is not gauged.

**Lemma (PROVED).** Finite field content, with gauge maps whose symbols lose rank only at finitely many points modulo 2π, gives a finite-dimensional Killing algebra 𝔨.

**Lemma (PROVED).** P̃ = 0 extends to all Killing ghosts. So X: 𝔨 → Sym/Triv is a Lie homomorphism, and its image is a Lie algebra containing F_ρ and L_J. That image contains the multiplication operators by the functions in

  Fspace = span{W_J^n f_ρ}, with W_J = (J f)·∇,

because [L_J, g] = W_J g.

**Fspace is infinite-dimensional.**
- **CHECKED, exact** (`f1_tower.out`): dim span{W^j f_c : j ≤ n} = 2, 4, 6, …, 14 for n = 0…6. The same counts hold for the K2 scalar or C3 scalar (f = sin k) and for the K2 fermion (f = ½ sin 2k). The continuum control f = k stays at 2.
  - Functions of (k₀, k₁) restrict injectively to the Z⁴ shell, so these counts hold modulo A.
- **PROVED for those realizations, and for the Hamiltonian Z³ class.** This covers any analytic single band with Hess u(0) > 0 in d ≥ 2, with p = ∇u.
  1. W is a real-analytic complete flow on 2-torus slices, with an elliptic fixed point at k = 0.
  2. Suppose its orbit period T were locally constant near 0. Then the time-T map would be the identity everywhere, by analyticity. That would be a nontrivial circle action on a torus with a fixed point, which B1's refereed lemma excludes (equivalently Borel / Conner–Raymond).
  3. So T varies. CHECKED: T/2π = 1.00025, 1.149, 1.373, 1.783, 3.23 as the level E falls from 1.999 to 0.05. That is ≈ 1 + k²/8 in the IR, diverging at van Hove.
  4. If Fspace were finite-dimensional, t ↦ g(Φ_t k) would be an exponential polynomial with exponents fixed by the matrix of W on Fspace. A T(k)-periodic exponential polynomial keeps only exponents λ with λT ∈ 2πiZ.
  5. Since T takes uncountably many values, g would be constant on almost all orbits, so W g = 0 near 0. That contradicts W f ≈ J k.
- **SUGGESTED for a general strictly local f on complex Z⁴ shells.** There is no real Hamiltonian slice in general, so the period argument does not apply.

**Conclusion.** Gauging generalized symmetries to close the algebra needs dim 𝔨 = ∞, i.e. infinitely many gauge fields. Finite field content is excluded.

**READING.** This is a lattice "higher-spin" tower. In the continuum, the free scalar's higher symmetries (Eastwood) contain Poincaré as a finite subalgebra that closes on its own. On the lattice, the subalgebra generated by the IR-normalized translations and rotations is already infinite. COMPARATOR: gauging spin-3 forces the full higher-spin algebra (Berends–Burgers–van Dam 1985; Fradkin–Vasiliev 1987; Bekaert–Boulanger–Sundell RMP 2012). Flat-space spin-3 coupling to gravity is obstructed (Aragone–Deser 1979).

## 3. Item 3: the Ward identity and μ_E = μ_T2; comparisons

### 3.1 No completion exists, so the PASS verification is vacuous

**Conditional link (PROVED).** Suppose closure held. In the Hamiltonian form, C3 shows closure forces Hess u = const. Then RV4's formula

  μ_h = −(1/8)⟨φ_h ψ_h / ω⟩, with ψ_h = h : Hess u ∝ tr h,

gives ψ_h ≡ 0 for traceless h. So μ_E = μ_T2 = 0, the unimodular cosmological-constant value. This agrees with RV4's Theorem D. In the other direction, μ_E − μ_T2 is a witness of the same defect.

### 3.2 The escapes

| Escape | What happens | Status |
|---|---|---|
| **SLAC** | Closure holds inside the zone. On the torus, Df for the sawtooth carries −2πδ(k_ρ − π), so the defect is concentrated on the zone faces. This is exactly RV4's face sink and source: μ_E^SLAC = 1.48e-2 ≠ μ_T2 = 0. So SLAC does not supply the Ward identity | PROVED from the sawtooth derivative; numbers are RV4's refereed ones |
| **Perfect actions** (quasi-local A; shell ∪ₙ(Q + 2πn)) | f = k + 2πn on each branch is consistent with periodicity, so T1's last step fails, as it must. A continuum-like Ward identity, and then μ_E = μ_T2, is plausible | SUGGESTED / COMPARATOR (Bietenholz–Wiese; Bahr–Dittrich). It is not finite range, and in transfer-matrix language it is an infinite band tower (I1) |
| **Stückelberg compensators** π_μ, with δπ = −ξ | Finite and local. Then C = γ(−π) is γ-exact in full, Killing part included, so P̃∘s₀ = 0 fails and the class trivializes. This is W2/W3's I − F | Not a PASS: the unitary-gauge action with any h-local mass terms is formally invariant after the Stückelberg substitution. Its Ward identity holds for every μ_E and μ_T2, so it fixes neither (PROVED). W3's F is the metric-non-local version of the same trivialization |

### 3.3 Continuum uniqueness theorems (COMPARATOR, from memory)

- **BBH and the uniqueness of Einstein–Hilbert.** Barnich–Henneaux (1993) and Barnich–Brandt–Henneaux (Phys. Rept. 2000): the second-order obstruction for gauging lives in "a₂ defines a Lie algebra, and a₁ represents it on the matter". Boulanger–Damour–Gualtieri–Henneaux (NPB 2001) give the uniqueness of Einstein–Hilbert as a deformation of Fierz–Pauli.
  - Poincaré-invariant continuum matter supplies that representation automatically, so the class vanishes and the deformation is unique.
  - On the lattice the matter carries no local representation of the Killing algebra (T1). The same class is therefore nonzero.
- **Boulware–Deser (1975) and Wald (1986).** Consistency forces the gauge algebra to be a deformation of the abelian one to the diffeomorphism Lie algebra, and requires the source to transform under it. Our obstruction is the failure of that requirement in its global (Killing) part, already at flat background.
- **Bahr–Dittrich** (0905.1670, 0907.4323). Regge diffeomorphism symmetry is exact on flat backgrounds at linear order, broken at higher order and on curved backgrounds, and restored only by non-local perfect actions.
  - Here the breaking appears at the first nonlinear order. It is sourced by strictly local matter on a flat background.
  - The only restorations are the same non-local, perfect-action class or trivialization by compensators.

### 3.4 The Hamiltonian Z³ version

The BFV projection works the same way:
- the Killing smearings are affine lapse and constant or rotational shift (C3's Gᵀξ = SᵀN = 0);
- the boost is forced to be the first moment of T₀₀ (B1 Theorem S);
- the condition becomes C3's boost theorem, Hess u = const. That theorem was refereed CONFIRMED for a single band, and is the Hamiltonian face of T1.

The Hamiltonian version of the tower is proved in §2.2.

## 4. Map to the FIXED readings

| Clause | Result |
|---|---|
| **PASS:** local, finite-content, finite-range completion with field-dependent gauge transformations, invariant through O(κ²) including the Killing sector, with a Ward identity fixing μ_E = μ_T2 | **Not met.** No such completion exists in the class (T1 with §1.3). The compensator route is invariant but its Ward identity does not fix μ (§3.2) |
| **FAIL:** proved that no completion exists in the stated class, or that one exists only with infinite field content | **Met (bounded).** No completion exists for any range or polynomial order with finite content (§1, T1). Gauging generalized symmetries needs infinite content (§2; proved for the K2/C3 realizations and the Hamiltonian class, suggested in general) |
| **INCONCLUSIVE** | Not applicable inside the class |

**Lane reading for F1: FAIL (bounded).**

## 5. Scope, hypotheses and negative-claim record

**Hypotheses.**
- **H1:** Z⁴ Euclidean, as in K2. Z³ Hamiltonian is covered through C3 and B1.
- **H2:** free finite-component matter, strictly local A, irreducible IR component S₀. F acts on ker A|_{S₀} as a scalar f ≢ 0. This holds for scalars and for F ∝ 1 (the naive and staggered fermions).
- **H3:** a local gauge map whose IR value and first moment are the continuum ones. Its other zeros are finitely many modulo 2π.
- **H4:** universal coupling, meaning the translation charge acts on the IR matter. It also means hypercubic-covariant constant structure constants, with a single c; T1 covers every c.
- **H5:** local BV functionals with summable first moments, polynomial in fields, ghosts and antifields.
- **H6:** classical master equation. The quantum master equation (Δ-terms) was not treated; on matter bilinears it adds c-numbers only (SUGGESTED).

**Not covered:**
- non-local, power-law functionals;
- quasi-local matter with tower shells (perfect actions);
- non-scalar translation action on degenerate kernels, i.e. non-abelian band structure;
- gauge maps with infinite-dimensional Killing kernels (subsystem or fracton type), which would allow an infinite 𝔨 with a finite number of fields;
- interacting matter;
- the general-symbol Z⁴ tower;
- abandoning universal coupling or the e(4) target (Carroll, preferred-frame algebras).

**N1–N8.**
- **N1, routes assessed:**
  1. h-dependent generators;
  2. φ-dependent generators and open algebras;
  3. field-dependent structure functions;
  4. field redefinitions and counterterms or seagulls;
  5. altered IR-normalized gauge maps;
  6. alternative translation symbols f (any analytic one);
  7. same-ghost operator-valued parameters;
  8. new generalized-symmetry ghosts;
  9. Stückelberg compensators;
  10. SLAC, perfect actions and non-local functionals.

  Routes 1–7 are closed by P̃ with T1. Route 8 needs infinite content. Route 9 trivializes the class without fixing μ. Route 10 lies outside locality.
- **N2:** routes 1–4 and 7 are one wall, P̃∘s₀ = 0. Routes 5 and 6 are T1. These are not independent walls.
- **N3:** hidden conditions are listed as H1–H6. The strongest are strict locality of A (used only in T1's last step) and scalar f.
- **N4:** the proof rests on:
  - §1.3, a short argument;
  - T1, a short argument;
  - `f1_closure_theorem.out` (instances and the SLAC control);
  - `f1_killing_poly.out` (Lemma K);
  - `f1_tower.out` (the tower).

  The scan in `f1_T1_scan.out` is corroboration only.
- **N5:** every negative is narrowed to H1–H6.
- **N6:** the escapes change dynamics or representation: a quasi-local tower action, compensators, or infinite gauge content. The axioms neither supply nor forbid them.
- **N7, strongest counterargument:** a perfect (RG-blocked) quasi-local matter action. Its shell is the 2π-periodized continuum hyperboloid, so f = k + 2πn holds branch by branch and Killing closure could hold. This is real, and it lies outside finite range. Whether it couples locally at O(κ²) is uncomputed.
- **N8, prior walls:**
  - C3's boost and rotation theorems (Hamiltonian face of T1);
  - K2's compact-shell theorem (superseded inside BV by T1);
  - B1's Theorem S (re-derived here from BV locality);
  - RV4 S1's Theorem D (the Ward identity that would follow);
  - W3's F (the non-local trivialization).

## Files (all in the scratch folder above)

| Script | Output | What it checks |
|---|---|---|
| `f1_killing_poly.py` | `.out` | Lemma K exactly, on the infinite lattice: polynomial Killing fields, symbol rank, zeros of the improved stencil |
| `f1_killing_jets.py` | `f1_killing_jets_boxes.out` | open-box kernels; the affine family is Killing for every IR-normalized stencil |
| `f1_closure_theorem.py` | `.out` | the T1 ingredients for the K2 scalar and fermion, improved stencils, the SLAC control, and the line lemma |
| `f1_T1_scan.py` | `.out` | numerical corroboration scan (not part of the proof) |
| `f1_tower.py` | `.out` | exact tower ranks and orbit periods |
| `F1_report.md` | — | this report |

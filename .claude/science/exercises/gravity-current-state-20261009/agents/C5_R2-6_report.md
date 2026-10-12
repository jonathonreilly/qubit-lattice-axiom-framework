# C5 Round 2, probe R2-6: Snyder coordinates (discrete space with exact Lorentz symmetry)

**Worker.** Claude Opus 5.5 (same family as the supervisor and O1–O5). Run 2026-10-12, 11:53Z to about 12:25Z. No repository file was edited. **Not refereed.** The no-go in §5 needs the codex referee before it is recorded.

**Scratch:** `.../scratchpad/C5/R2-6/`

| Script | Output | What it checks |
|---|---|---|
| `r26_spectrum.py` | `r26_spectrum.out` | (a) spectra, covariance, joint eigenvectors |
| `r26_composition.py` | `r26_composition.out` | (b) worldline velocity; (c) composition, soccer ball; (d) Lemma W test; (e) Lorentz covariance |
| `r26_symmetrised.py` | `r26_symmetrised.out` | (d) the commutative (symmetrised) variant |
| `r26_numbers.py` | `r26_numbers.out` | physical numbers at a = ℓ_P |

`r26_composition_lib.py` is the function part of `r26_composition.py`, so that `r26_symmetrised.py` can import it.

**Read in full:**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`;
- `TESTS.md:2302-2643` (C5, Round 1 results, Round 2, R2-6 at `:2615-2630`);
- `agents/C5_O5_synthesis.md`;
- `SUMMARY.md` §§15–21 (`:334-549`);
- `PRICE_NOTE.md`, including the v6 delta and its wrap-up (`:251-413`);
- `C5_O2_report.md`, `C5_O2_referee.md` and `C5_O2_referee_full.md`;
- `C5_O1_referee.md`;
- `C4_B1_report.md`, `C4_B1_referee.md` and `C4_B1_referee_full.md`.

**Labels.**
- **PROVED:** own, same family, unrefereed.
- **CHECKED:** a script output.
- **SUGGESTED:** argued only.
- **READING:** an interpretation.
- **COMPARATOR:** literature, from memory or abstract-level search.

## Prior art (counted once)

`git grep` over all 43,513 tracked files found no hit for Snyder, soccer-ball, κ-Poincaré, relative locality, Battisti or Meljanac outside this packet. The NCG hits in `docs/` are Connes spectral triples (Koide lanes), which are not relevant. Inside the packet:

- **O2's Snyder rows.** `C5_O2_report.md:166,224` mark Snyder "SUGGESTED: it violates Lemma W at the order of the deformation", plus the soccer ball. The referee confirmed SUGGESTED (`C5_O2_referee_full.md:282-284,331`). §5 below upgrades this to a conditional proof.
- **RB, Theorem R, torus only** (`C4_B1_referee.md:11`; `C4_B1_referee_full.md:133-141`). B1's 1D "soccer-ball in lattice form" (`C4_B1_report.md:109-111`) was narrowed by its referee (`C4_B1_referee_full.md:172-187`).
- **O1 class VI** (`C5_O1_report.md:213,268`: "they need non-additive momentum composition"). Its referee calls it "correctly left open" (`C5_O1_referee.md:66`).
- **O5 §2.6, set D** (`C5_O5_synthesis.md:430-433`).

## Reading against the FIXED lines (`TESTS.md:2626-2629`)

**FAIL (bounded): met, through the second disjunct.** "No consistent soft spin-2 coupling exists" is PROVED under hypotheses S1–S5 (§5):
- for Snyder's own composition law (the star-product/coset coproduct), at 2→2;
- for its commutative symmetrisation, at 2→3.

**The first disjunct (MICROSCOPE/LLR) is met only under mapping A,** where a macroscopic body composes and responds as a single Snyder particle at scale a:
- η(Ti,Pt) = 0.29, or the masses do not fall at all (§4).

**Under mapping B, EP passes.** In mapping B, composition happens only at local microscopic vertices:
- η ≲ 1e-39 at nucleon granularity, or 3.5e-35 at nucleus granularity;
- this is the "deformation scale depending on N" case, which the pre-registration classes as INCONCLUSIVE.

**PASS: not met.** (b) passes with infinite margin, but (d) fails whatever (c)'s resolution is, because the Lemma W defect sits at each elementary vertex, not in the N-body sum.

**Against the expectation** ("FAIL for per-constituent composition; INCONCLUSIVE if the scale grows with N"):
- The FAIL comes from the soft theorem, not from the soccer ball.
- It survives the N-scaling escape that the expectation left INCONCLUSIVE.

**Set D does not exist as a fourth minimal set** under Lemma W's hypotheses (§8).

## 0. In plain words

1. **What Snyder space is.** Snyder's space is "discrete" only in a narrow sense.
   - Each coordinate, measured alone, gives a whole multiple of the step a. That holds for every moving observer too.
   - The three coordinates cannot be sharp together. The only state where all three are sharp is the observer's own origin.
   - So there are no sites, and no grid of points.
2. **Light speed.** Exact Lorentz symmetry means light and all particles keep one speed at every energy. LHAASO's bounds are passed with infinite margin.
3. **The price is in how momenta add.** Adding two momenta depends on their order, and grouping three depends on the brackets.
4. **Heavy bodies.** If a macroscopic body adds momenta like one Snyder particle, it fails badly: a 0.4 kg mass would not fall at all (one ordering), or would fall about 10⁷ times too fast (the other). If only the microscopic collisions use the deformed rule, falling is fine to about 1e-39.
5. **The decisive point is the graviton.** Weinberg's soft theorem needs the graviton's charge (momentum) to add up exactly in every collision. Snyder's addition is not ordinary addition in any relabelling: it depends on order, and its symmetrised form depends on brackets. With exact Lorentz symmetry the graviton then cannot couple at all. The error per collision is tiny (about 1e-39 for nucleons), but Lorentz symmetry makes it a logical inconsistency, not a small effect that tuning could fix.
6. **The trade.** On a grid, boosts fail and momenta add. On Snyder space, boosts work and momenta do not add. The massless graviton needs both.

## 1. Hypotheses, stated before any title

- **(H-Sn) Snyder kinematics.** One-particle momentum space is dS₄ = SO(4,1)/SO(3,1), with radius 1/a.
  - Positions are x_μ = a·J_{μ4}; Lorentz is M_μν = J_μν, undeformed and acting linearly on momenta.
  - Plane waves e^{ik·x̂} = exp(W(k)) are coset exponentials (transvections).
  - Composition: g(k)g(q) = g(k⊕q)h, with h ∈ SO(3,1).
- **This is Snyder's coproduct.** It is the non-coassociative coproduct of Battisti–Meljanac (arXiv:1003.2108) and Girelli–Livine. COMPARATOR, abstract-level search.
- **Uniqueness.** The transvection section is the unique SO(3,1)⁺-equivariant section. Any equivariant h(k) commutes with the little group SO(3) of a timelike k, and the centralizer of SO(3) in SO(3,1)⁺ is trivial. PROVED, elementary.
- **Charts.** Other "realizations" relabel momenta by p = f(k²)k. Velocities p_i/p_0, invariant masses, and the tests in §5 are chart-independent.
- **a = ℓ_P,** with a⁻¹ = M_P = 1.22089e19 GeV (the repo convention, `PRICE_NOTE.md:85`).
- **Outside realizations this scope excludes:**
  - κ-Poincaré and other DSR with nonlinear boosts;
  - the commutative dS composition with deformed Lorentz action (Gubitosi et al., arXiv:1307.7988);
  - extended/tensorial Snyder with group-valued 10-momenta (Meljanac–Mignemi, arXiv:2007.13498);
  - generalized Snyder [x̂,x̂] = ia²ψ(a²p²)M with ψ ≠ 1 (only ψ ≡ 1 was computed);
  - anti-Snyder (AdS momentum space). It has continuous x_i and discrete time, so it is not "discrete space".

## 2. (a) Spectrum and covariance

**A2.1 (PROVED; CHECKED).**
- x_i = a·J_{i4} generates a rotation in the compact (i,4) plane. So exp(2πx_i/a) = ±1 in every unitary representation.
- Hence spec(x_i) = aℤ (single-valued representations; Snyder's scalar functions) or a(ℤ+½) (spinorial representations).
- t = a·J_{04} generates a boost, so spec(t) is continuous.
- CHECKED in finite so(4) irreducible representations, with x_i/a = A_i − B_i and L_i = A_i + B_i:
  - commutators to 1e-15;
  - spec(x₁/a) is integer for (j,j) and (2,1), half-integer for (½,0), (1,½) and (1.5,1) (`r26_spectrum.out`).

**A2.2 Covariance (PROVED; CHECKED).**
- For any spacelike unit n, n^μJ_{μ4} = ΛJ_{14}Λ⁻¹ with Λ ∈ SO(3,1). Residual 6e-16.
- In the 5D representation its eigenvalues are ±i at every rapidity, and exp(2πX) = 1 to 4e-54 (mpmath; the float64 residual at η = 6 is round-off).
- Timelike n gives eigenvalues ±1, i.e. non-compact.
- **Meaning for a moving observer.** Each inertial observer's spatial coordinates have spectrum aℤ, with no Lorentz contraction of the step. They do not commute with the rest frame's x or t. Time is continuous for everyone.

**A2.3 Only one sharp point (PROVED, elementary; CHECKED).**
- A joint eigenvector ψ of (x₁, x₂, x₃) has [x_i,x_j]ψ = ia²L_ijψ = 0. So ψ is SO(3)-invariant.
- Rotating the eigen-equation gives λ = Rλ for all R, so λ = 0.
- Then x_iψ = L_ijψ = 0, so ψ is SO(4)-invariant.
- (SO(4,1), SO(4)) is a Gelfand pair, so each irreducible representation has at most one such vector (COMPARATOR, standard).
- CHECKED: ker L is 1-dimensional in (j,j), and x_i acts on it with norm 1, 1.63 and 2.83 for j = ½, 1, 2. The kernel of x_i survives only in (0,0).
- **So "discrete space" is a spectrum, not a lattice.** Each observer has exactly one sharp point, the origin; every other position is fuzzy.

## 3. (b) Dispersion and LHAASO

- **CHECKED (sympy, C7).** With {x^μ, p_ν} = δ^μ_ν + a²p^μp_ν and the constraint p² + m², the worldline gives dx^μ/dτ = 2p^μ(1 + a²p²) (the C7 output prints the covariant components). So dx^i/dx^0 = p^i/p^0, undeformed.
- **PROVED for every Lorentz-covariant realization.** {x_μ, f(p²)} ∝ p_μ.
- **So the free one-particle mass shell is exactly Lorentz-invariant.** The dimension-5 and dimension-6 coefficients are exactly 0 at any a.
- LHAASO's E_QG,1 > 10 E_Pl and E_QG,2 > 6e-8 E_Pl (`C4_B1_report.md:233-236`; `C5_O1_referee.md:77`) both pass with infinite margin at tree level.
- **Loops.** A Lorentz-covariant star product plus a covariant regulator generates no LIV operator at any dimension. SUGGESTED (reading); not computed. Even so, F1 would be met by symmetry, which beats set B's dimension-6 margin of 7.76 decades.
- **COMPARATOR (search, abstracts).**
  - Mignemi–Samsarov (arXiv:1610.09692): no energy-dependent photon delay in Snyder.
  - Mignemi (arXiv:1308.0300): dS momentum space with metric-preserving addition.
  - Mignemi–Rosati (arXiv:1803.02134): residual relative-locality effects that are energy-independent and quadratic in 1/E_P.

## 4. (c) Composition and the soccer ball

**C4.1 Structure (CHECKED, `r26_composition.out`).**
- g(k)O equals the closed-form geodesic point (5e-16), and h fixes O.
- Lorentz covariance L(k⊕q) = Lk⊕Lq holds to 9e-16.
- k⊕q and q⊕k have equal mass and differ by h.

**C4.2 Order-a² law (CHECKED).**
- BCH gives k⊕q = k + q − (1/6)[X,[X,Y]] − (1/3)[Y,[X,Y]] (projected). The residual is O(a⁴), with ratio/a⁴ = 0.2555 constant.
- Non-commutativity: k⊕q − q⊕k = (a²/2)[((k+q)·k)q − ((k+q)·q)k] + O(a⁴). Fitted coefficient 0.49997, residual 7e-12.
- This difference is Minkowski-orthogonal to k+q. For equal masses it equals (a²/2)(k·q − m²)(q − k) ≠ 0, since k·q − m² ≤ −2m².
- Non-associativity: |(k⊕q)⊕r − k⊕(q⊕r)| ≈ 0.56a² in the test.
- **Collinear momenta add exactly** in normal coordinates (≤ 6e-14 at aM = 12).

**C4.3 Mapping A: the body as one Snyder particle (PROVED; CHECKED to 8 digits).**
- A body at rest of mass M receiving a soft spatial kick q gets:
  - v = aq/sinh(aM) for P⊕q;
  - v = aq·coth(aM) for q⊕P.
- So the inertial mass is sinh(aM)/a or tanh(aM)/a; for small aM, M(1 ± (aM)²/6 or /3).
- Derivation: a (0,4)-boost leaves the spatial ambient components unchanged; normal coordinates rescale them by χ/sinh χ.
- **Numbers (`r26_numbers.out`):**
  - MICROSCOPE masses (from memory, ~0.30 and ~0.40 kg): aM = 1.38e7 and 1.84e7.
    - Left: both factors are below 10^(−6,004,285), so the masses do not fall.
    - Right: η = 0.286 against ~1e-15.
  - LLR: aM(Earth) = 2.7e32 and aM(Moon) = 3.4e30. Right: η = 1.95 against ~1e-13. Left: neither body falls.
  - η < 1e-15 needs M < 1.8–2.6e-15 kg under mapping A.
- **So FAIL under mapping A**, conditional on that mapping.

**C4.4 Per-constituent ⊕-total of a body with Fermi motion (CHECKED; scaling SUGGESTED).**
- The setup: constituents k_i = (√(m²+κ_i²), κ_i), Σκ_i = 0, κ_F/m = 0.25/0.94, scaled units, aM ≤ 2.
- The composed total carries a spurious spatial momentum and an ordering ambiguity.
- Spurious velocity ≈ C·a²·m·κ_F·N^{3/2}:
  - fitted exponents 1.46 (sequential), 1.43 (ordering ambiguity), 1.43 (balanced tree);
  - C = 0.10–0.16.
- Random-walk argument for 3/2: SUGGESTED.
- At a = ℓ_P this reaches 1e-15 c at N ≈ 3e16 nucleons (5e-11 kg). It becomes non-perturbative at M_P (21.8 µg).
- **So the ⊕-total of a macroscopic body is physically meaningless** for every bracketing.

**C4.5 Mapping B: vertex-local composition only (SUGGESTED consistent).**
- Each constituent absorbs its own kick.
- A rigid body's constituent momenta are collinear, so their total is exactly additive (C4.2).
- The fall factor per absorber is (aμ)/sinh(aμ):
  - η_B ≲ (a·m_N)²/6 = 9.9e-40 at nucleon granularity;
  - 3.5e-35 at nucleus granularity.
- Internal collisions change the linear total by about a²m²κ_rel each. By isotropy the mean drift vanishes, and the random walk is negligible: ~1e-38 c per day for 0.4 kg (estimate, SUGGESTED).
- B is equivalent to a composite scale M_P,eff ≈ M_P·M/μ, and needs M_P,eff ≥ 1.3e7·M. In the pre-registration's terms this is the N-dependent deformation scale, so (c) alone reads INCONCLUSIVE.
- **Open in B:** B is consistent only if no physical quantity uses the composite's ⊕-total (C4.4), while Snyder's global translation charge is exactly that coproduct. Whether a Snyder QFT supports B is not shown.
- COMPARATOR: the soccer-ball debate is Hossenfelder (SIGMA 2014); AFKS (arXiv:1104.2019); Amelino-Camelia (arXiv:1407.7891, total momentum linear).

## 5. (d) The soft theorem: Lemma W-S (PROVED under S1–S5; no-go, needs referee)

**Hypotheses.**
- **S1.** Exact Lorentz invariance, acting linearly on one-particle momenta and as the tensor product on multi-particle states (Snyder: Lorentz primitive, `H-Sn`).
- **S2.** Hard amplitudes are supported on the ⊕-conservation surface and are non-zero on an open set of it (W5 of `C5_O2_report.md:57-63`). This holds for 2→2 and for 2→3 of identical particles.
- **S3.** W3 holds: soft emission is dominated by leg-local poles, and the q → 0 vertex and pole of leg i depend only on k_i.
- **S4.** The exact Ward-residue identity of Lemma W (`C5_O2_report.md:72-86`; refereed DERIVED conditional, `C5_O2_referee.md:5`).
- **S5.** The massless helicity-2 obeys W2. By S1 this is not an observational assumption: a Lorentz-invariant S-matrix requires pure-gauge decoupling (Weinberg).

**Step 1: the charge is ∝ k (PROVED).**
- By S1, the leg vertex is V^μν = A(k²)k^μk^ν + B(k²)η^μν.
- The pole is ΔD⁻¹ = (k⊕q)² − k² = 2(α + βk²)k·q + O(q²), since the Jacobian is E(k) = α + βkk^T by covariance.
- So Q(k) = κ̃(m)k. Any chart p = f(k²)k gives the same direction.

**Step 2: what decoupling requires (PROVED).**
- Lemma W requires Σ_in κ̃_i k_i = Σ_out κ̃_j k_j on the ⊕-support.
- At 2→2, the level sets of (k₁,k₂) ↦ k₁⊕k₂ must equal those of κ̃₁k₁ + κ̃₂k₂. Both maps are submersions with 2-dimensional fibres.
- So k₁⊕k₂ = H(κ̃₁k₁ + κ̃₂k₂), and covariance forces H(w) = h(w²)w.
- Writing k⊕q = Ak + Bq on shell, this needs A/B = κ̃(m_k)/κ̃(m_q), independent of k·q.
- For equal masses it needs k₁⊕k₂ = g(v²)(k₁+k₂). That form is commutative, and swapping momenta between e⁻ and e⁺ (equal masses by CPT) gives a configuration on the support.

**Step 3: Snyder's own composition fails (PROVED to O(a²); CHECKED).**
- k⊕q − q⊕k ≠ 0 (C4.2).
- On the ⊕-surface (C6, equal masses), |k₁+k₂−k₃−k₄| = 0.729a², and the component of k₁⊕k₂ perpendicular to k₁+k₂ is 0.576a², each constant across a = 0.2 … 0.025.
- Unequal masses: A/B varies with k·q (1.0017 → 1.0030; C6b).
- **Conclusion: κ̃ ≡ 0 for every species with a generic elastic channel.** If κ̃ ≠ 0, graviton exchange supplies one, so the contradiction is self-consistent.

**Step 4: the symmetrised variant fails one step later (PROVED given S2 at 2→3; CHECKED).**
- k⊕_s q = ½(k⊕q + q⊕k) is commutative. It passes Step 2 exactly: A/B is constant to 1e-15 at a = 0.05, 0.3 and 0.8 (`r26_symmetrised.out` S1).
- At 2→3 of identical particles, permutation symmetry puts both (k₃⊕k₄)⊕k₅ and k₃⊕(k₄⊕k₅) on the support (using commutativity).
- Lemma W then needs H((k₃⊕k₄)⊕k₅) = H(k₃⊕(k₄⊕k₅)). H = id + O(a²) is locally injective, so associativity is needed.
- ⊕_s is non-associative: 0.185a², constant across a = 0.2 … 0.025 (S2).
- No rescaling Q(k) = κ̃(m)k makes ⊕_s additive (S3: residuals 0.06a² to 1.8a² for the three natural charts).

**General form (PROVED; elementary).** Under S1–S5, an exact soft graviton requires the on-shell conservation law to be commutative and associative, with an additive Lorentz-vector charge. That is ordinary addition in rescaled labels.
- A group-valued momentum space (associative) needs Q to be a homomorphism G → (ℝ⁴,+), which factors through G/[G,G].
- For simple G = SO(4,1) (extended Snyder), Q = 0.
- For κ-Poincaré's AN(3), only a 1-dimensional (energy-type) Q exists. This is a scope remark: κ-Poincaré violates S1.

**Size.**
- The tree-level defect is O((aE)²), with E the collision energy scale including mass: 5.9e-39 for nucleons, 6.7e-33 at 1 TeV, 6.7e-17 at 1e11 GeV.
- That is invisible at tree level, like the grid's 2e-41 (`C5_O2_report.md:101-116`).
- The difference from the grid: by S1/S5 the failure is a logical inconsistency (Lorentz-invariant S-matrix ⇒ decoupling), not an observational one.

**Escapes (outside S1–S5).**
- A deformed gauge principle whose soft charges are not leg-local (violates S3). No construction is known (COMPARATOR: relative locality is the G → 0 regime).
- A massive graviton: m_g ≤ 1.27e-23 eV, plus vDVZ/Vainshtein. SUGGESTED cost.
- Theories whose S-matrix support uses a single bracketing with no identical-particle symmetrisation. Step 3 already kills the ordering law at 2→2.
- Gravity that is not a massless particle pole.

## 6. (e) The boost wall on dS momentum space

**Neither RB nor C3's one-particle obstruction applies (PROVED).**
- In Snyder, (M_μν, p_μ) obey the undeformed Poincaré algebra (the realization M = x̃∧p).
- p is unbounded on every mass shell, so Theorem U's bounded-sector hypothesis fails (`C4_B1_report.md:67-71`).
- dS₄ ≅ ℝ×S³ carries a global smooth linear Lorentz action fixing O (CHECKED, C1). Theorem R is specific to the torus (`C4_B1_referee_full.md:133-141`).
- C3's cos k factor (central differences) is absent: the translation symbol is p itself.

**Many-body (PROVED).**
- Lorentz is primitive and ⊕ is covariant, so a boost acts on any ⊕-total as a 4-vector.
- B1's lattice "many-body bracket is not F(H,P)" (`C4_B1_report.md:109-111`) has no Snyder analogue.

**Open.** A hypersurface-deformation (constraint) algebra for gravity coupled to Snyder matter: local energy densities in non-commutative space are not defined here. Not computed.

**READING.** Snyder moves the cost from the boost wall (grid) to the additivity wall (Lemma W-S).

## 7. (f) Finite M₂(C) fibre per site

**No (PROVED), but not because of Lemmas S, G or RS. Their hypotheses do not hold for Snyder:**
- S assumes exact undeformed Weyl translations; Snyder's are x̂ → x̂ + b + a²(b·p)p.
- G assumes a lattice QCA.
- RS assumes a local net on commutative spacetime.

**The two actual reasons:**
1. **There are no sites.** The only joint position eigenvectors are the SO(4)-invariant origin states (A2.3), so there is no ℤ³ to carry a per-site fibre.
2. **Each particle needs an infinite-dimensional space.** The one-particle space carries a unitary representation of the non-compact simple SO(4,1), whose non-trivial unitary representations are infinite-dimensional (COMPARATOR, standard).

**What survives.** M₂(C) can enter only as an internal factor per particle. With spinorial SO(4,1) representations, the coordinate spectra shift to a(ℤ+½): CHECKED for finite so(4) representations; READING for physical spin-½. This is set A's A2 structure (`C5_O5_synthesis.md:325`), not the Qubit axiom's per-site reading (`MINIMAL_AXIOMS_2026-06-29.md:45-53`).

## 8. Set D, named as prices (none adopted; it fails at D5)

| # | Price | Axiom text touched |
|---|---|---|
| D1 | Sites replaced by Snyder's non-commuting coordinates on a dS₄ momentum space of radius M_P. There are no sites; each observer has one sharp point | Lattice (`:37-41`) |
| D2 | M₂(C) only as an internal factor on an infinite-dimensional per-particle carrier | Qubit (`:47`) |
| D3 | The nearest-neighbour rule becomes a non-associative star-product rule (a-scale non-local), covariant under Lorentz and deformed translations | Admissibility (`:57-58`) |
| D4 | A record can lock one coordinate's spectral value at a time; a joint position record exists only at the origin | Record (`:79-82`) |
| D5 | **Blocking.** No exact massless soft spin-2 under S1–S5. The graviton decouples, or is massive (vDVZ), or needs a non-leg-local deformed gauge principle | none (a gravity primitive) |
| D6 | Composites must never be ⊕-composed as single Snyder particles (mapping B), or deformation scales must grow with N | none (a downstream rule) |

**READING.** D touches all four axioms, like A, and adds D5. If interaction vertices instead conserved the linear sum, Snyder's x̂ would be only an off-shell relabelling of A's coordinates. That would be "D collapses to A". SUGGESTED, not worked out: x̂ does not preserve a mass shell, and the projective chart covers half of dS.

## 9. Labels

| Item | Label |
|---|---|
| A2.1–A2.3 (spectra, covariance, one sharp point) | PROVED; CHECKED |
| (b) undeformed velocity, zero dimension-5/6 terms | PROVED; CHECKED |
| (b) no LIV in loops | SUGGESTED |
| (b) Mignemi et al. | COMPARATOR |
| C4.2 BCH law, non-commutativity coefficient ½ | CHECKED (analytic form from BCH) |
| Uniqueness of the equivariant section | PROVED |
| C4.3 mapping A factors aM/sinh(aM), aM·coth(aM) | PROVED; CHECKED |
| C4.3 EP numbers | CHECKED arithmetic; masses from memory |
| C4.4 N^{3/2} | CHECKED (fit 1.43–1.46); exponent argument SUGGESTED |
| C4.5 mapping B consistency | SUGGESTED |
| C4.5 η_B bounds | CHECKED arithmetic |
| Lemma W-S Steps 1–4 | PROVED under S1–S5 (S4 inherits Lemma W's conditional status) |
| Group-valued remark | PROVED, elementary |
| (e) RB/C3 do not apply | PROVED; HDA open |
| (f) | PROVED (two reasons above) plus COMPARATOR (unitary representations) |
| Set D prices; the trade reading | SUGGESTED / READING |

## 10. For the codex referee (no-go items)

1. **Lemma W-S Step 2.** Check the level-set argument: submersion ranks; that the swapped configuration lies in the generic support; e⁺e⁻ equal masses.
2. **Step 1.** Check Q ∝ k from Lorentz covariance with a deformed pole, including spinning legs at leading order.
3. **Step 4.** Check that identical-particle 2→3 symmetrisation puts both bracketings on the support. Check that H is locally injective at O(a²).
4. **S5.** Check the claim that exact Lorentz makes decoupling logically required (not observational) in a theory with a non-coassociative momentum coproduct but primitive Lorentz.
5. **A2.3.** The Gelfand-pair step.
6. **C4.3.** The left/right factors, and whether "mapping A" is a fair reading of per-constituent composition.

## Sources (search, abstract level)

- [Battisti–Meljanac, arXiv:1003.2108](https://web3.arxiv.org/abs/1003.2108)
- [Meljanac et al., arXiv:1608.06207](https://ar5iv.arxiv.org/html/1608.06207)
- [arXiv:1701.05862](https://ar5iv.arxiv.org/html/1701.05862)
- [Meljanac–Mignemi, arXiv:2007.13498](https://www.arxiv.org/pdf/2007.13498v2)
- [Mignemi–Samsarov, arXiv:1610.09692](https://arxiv.org/pdf/1610.09692)
- [Mignemi, arXiv:1308.0300](https://ar5iv.arxiv.org/html/1308.0300)
- [Mignemi–Rosati, arXiv:1803.02134](https://www.arxiv.org/pdf/1803.02134)
- [Freidel–Smolin, arXiv:1103.5626](https://arxiv.org/pdf/1103.5626)
- [arXiv:1307.7988](https://ar5iv.labs.arxiv.org/html/1307.7988)
- [AFKS, arXiv:1104.2019](https://arxiv.org/pdf/1104.2019)
- [Amelino-Camelia, arXiv:1407.7891](https://arxiv.org/pdf/1407.7891)
- [MICROSCOPE, arXiv:2209.15487](https://arxiv.org/pdf/2209.15487)

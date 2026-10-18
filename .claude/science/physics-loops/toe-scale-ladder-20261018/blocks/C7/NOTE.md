# C7: massive continuum limit of the supplied 3D two-qubit Dirac walk

**Block:** C7 of `toe-scale-ladder-20261018` (R2 → R3).
**Status:** worker note. Independently reviewed (REVIEW.md, verdict ready); unaudited.
**Runners:** `scripts/c7_exact.py` (sympy, exact identities) and
`scripts/c7_numeric.py` (numpy/mpmath, a different implementation). Logs are in `logs/`.
`scripts/run_all.sh` writes `logs/run_all.log`, which ends with the combined
`TOTAL:` line.

## 0. Premises (named, not derived)

- **P1. Supplied site.** Each site is C²(flavour, τ) ⊗ C²(spin, σ), and proper cubic
  rotations act as 1 ⊗ D(R). **Two qubits per site is outside the one-qubit Qubit axiom.**
  That axiom fixes the one-site algebra M₂(C). Enlarging it to M₄(C) is parked
  owner fork 4 (`docs/repo/DEFERRED_DECISIONS.md`), and this block does not adopt it.
- **P2. Supplied walk family.** This is the Clifford cell family of
  `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
  ("the parent"):
  U(k) = f + i(h₁τ₁ + h₂τ₂) + iτ₃⊗g·σ, with (f,h₁,h₂) = F φ(k),
  φ = (1, Σc, Σcc, c₁c₂c₃), c_a = cos k_a, g = b₀v₀ + b₁v₁ + b₂v₂ and FᵀF = G(b).
  From the parent I import Theorem 1 (unitarity and covariance) and Theorem 2
  (G(b) is unique, and F is unique up to O(3)). I also import the closed forms of the
  three TRIM cosines, which c7_exact.py re-derives.
- **P3. Declared scaling (a choice).** Lattice spacing a, tick τ = a (one walk step
  per tick), b held fixed, mass angle θ = m a with m fixed. Mass direction ĥ in the
  (τ₁,τ₂) plane, held fixed.
- **Named parameter points:** b* (s = 0.91442, the parent's explicit member),
  b_iso (s = √(2/3), k⁴-isotropic) and b_gold (s = 1, the light-speed member).
  The theorems hold for any admissible b, under the hypotheses each one states.

## 1. The massive walk is already in the family (exact)

Every member at fixed b is O F₀ with O ∈ O(3), where F₀φ₀ = e_f is a massless
member (U(0) = 1). Write O e_f = (cos θ, sin θ ĥ). Then

  **U_{θ,ĥ}(k) = M U₀(k) M,  M = exp(iθ ĥ·τ/2)**

(c7_exact: the identity M U₀ M = (R_θ F₀ member) holds symbolically). M is a constant
flavour coin. It commutes with 1⊗D(R), so covariance is preserved.
U(0) = exp(iθ ĥ·τ), which gives a rest mass θ/a = m. So **the mass is not a new
parameter**: it is the O(3)-orbit coordinate that the parent fixed to zero. The massive
walk is a symmetric Trotter step "half mass, massless step, half mass". The parent's
massless member carries a flavour Wilson vector W = C w, with
|W| = |s|√(1−s²) exactly (re-verified). Let **χ** be the angle between ĥ and W
(the twist angle). χ = 0 is a Wilson-aligned mass and χ = π/2 is maximal twist.

## 2. Vertex lemma: all nodes and gap minima sit at the 8 TRIMs (proved theorem)

**Lemma V.** For every member, f(k) is a multilinear polynomial in (c₁,c₂,c₃)
(exact check), and the bands are cos ω = f. A multilinear function on [−1,1]³ attains
its extrema at vertices, and the vertices are the TRIMs k_a ∈ {0,π}. Hence:

1. min ω and min (π − ω) over the whole Brillouin zone are attained at TRIMs. So a
   member has a node (ω = 0 or ω = π) iff some TRIM is a node of that type.
   *Node locations (review fix 2b).* Multilinearity fixes where the extremal values
   occur, not that they occur only at vertices. **Provided no two TRIMs adjacent on the
   cube (differing in one k_a) are nodes of the same type**, every node lies at a TRIM.
   If two such TRIMs are, f is constant along that edge, and the nodal set contains the
   whole edge. All three named points satisfy the hypothesis. At b*, b_iso and b_gold
   only Γ has f = 1. At b_gold the f = −1 set is the three X points, which pairwise
   differ in two coordinates. Every concrete statement in §2 and §5 therefore stands.
2. **Global dispersion bound:**
   1 − cos ω(k) ≥ (1 − cos θ) + c_θ Σ_a (1 − cos k_a), with
   c_θ = min_{K≠0} [cos θ − cos ω_K(θ)] / (2|K|), where |K| is the number of π
   entries. Proof: subtract the right side from the left. The difference is multilinear in
   x_a = 1 − c_a ∈ [0,2], vanishes at x = 0 and is ≥ 0 at the other vertices.
   At θ = 0 the X-vertex term equals s², which is exactly the cone coefficient.

This replaces the parent's 40³-grid statement "no other band touching" by a proof.
The parent's numerics are consistent with it.

**Node and doubler table** (massless member; TRIM cosines exact in b, and exact
algebraic numbers at b_iso and b_gold):

| point (mult.) | cos θ_K | b* | b_iso | b_gold | Weyl index of g (τ₃=+ block) |
|---|---|---|---|---|---|
| Γ (1) | 1 | node, ω=0 | node, ω=0 | node, ω=0 | sign s³ = + |
| X (3) | 1 − 2s² | 2.308 | 1.911 (cos = −1/3) | **π (massless π-mode)** | −sign s |
| M (3) | 1 − 8s(b₀−b₂) | 2.196 | 2.462 (cos = −7/9) | 2.665 (cos = 17−8√5) | sign(b₀−2b₁+b₂) = + |
| R (1) | 1 − 6(3b₀²+2b₀b₂+3b₂²−8b₁²) | 2.198 | 2.715 | 2.455 | −sign(b₀−2b₁+b₂) = − |
| c₀ (Lemma V) | | 0.2644 | 0.3184 | 0.2956 | |

The Weyl indices are signs of det ∂g at the 8 zeros of g (exact Jacobians:
J_Γ = s·1, J_X = diag(−s, b₀−b₂, b₀−b₂), and so on). They sum to 0 at every
point, which serves as a degree check. Every node is a Dirac node (τ₃ = ± blocks carry
opposite index), so the walk is vector-like, consistent with the parent's W₃ = 0.
The b* entries are floating-point values of explicit algebraic numbers, and their
margin from 0 and π is ≥ 0.83 rad. Treat them as numerical; they carry no formal certificate.

**π-modes at the chosen parameters (decided).** For b* and b_iso there are **no**
π-modes and no node other than Γ (exact by Lemma V: all TRIM cosines lie in (−1,1)).
For b_gold the axis triplet X consists of massless π-modes (cos θ_X = −1 exactly). Each
is a uniaxial Dirac cone with velocities (1, √5−2), as in the parent. The doublers
are massless only at s = ±1.

**Massive doublers (proved).** U(K) is a pure flavour element, because g(K) = 0. By
bi-invariance of the S³ metric, |ω_K(θ) − θ_K| ≤ θ for all K and ĥ. At b_gold,
U₀(X) = −1 gives U_θ(X) = −M² = −U_θ(0) exactly. The X triplet becomes three
massive π-modes with the *same* mass m, at quasienergy π − ma, that is, energy π/a − m.
Numerics confirm both statements (err 7e-15).

## 3. Exact lattice Hamiltonian and its O(a) term

**Theorem A (exact).** Wherever f > −1, U(k) = exp(−i a H_a(k/a)) with
H_a(p) = −(ω / (a sin ω)) X(ap), where X is the Clifford part, and
**H_a(p)² = (ω/a)² · 1** exactly. So the walk at integer times is an exact lattice
Hamiltonian evolution. ω/sin ω = arccos(c)/√(1−c²) is real-analytic at c = 1, so
H_a is real-analytic near the physical node.

**Theorem B (expansion; exact coefficients, analytic remainder).** Put α_a = −τ₃σ_a,
β = −ĥ·τ and H_D(p) = s α·p + m β. Then

  **H_a(p) = H_D(p) + (a/2)|p|² W·τ + R_a(p),  ‖R_a(p)‖ ≤ C₃ a² (|p| + m)³**

for a(|p|+m) ≤ κ₀. The coefficients are exact (c7_exact). In particular g = s k + O(k³),
∇φ(0) = 0, and h_θ = θĥ − (k²/2)W + O(3). C₃ and κ₀ exist by analyticity, which is
proved. Their values are **numerical**: the sample-maximum ratios (lower estimates of the sup; see §4 item 2) are C₃ ≈ 0.042 (b*),
0.033 (b_iso) and 0.051 (b_gold) on |p| ≤ 2, m = 1.

**Dirac identification (exact).** V = ((τ₁ − τ₃)/√2) ⊗ 1 is a constant unitary.
It maps α_a ↦ τ₁⊗σ_a and β = −τ₁ ↦ τ₃ (standard Dirac representation), and it
commutes with the coin 1⊗D(R). So the cubic spin action is the Dirac spinor rotation.
For other ĥ, first rotate with the gauge exp(iφτ₃/2), which fixes τ₃σ_a.

## 4. Continuum limit theorem

Take continuum momentum space L²(R³;C⁴) and the band-limited embedding
J_a: φ̂ ↦ ψ̂(k) = a^{−3/2} φ̂(k/a) (isometric onto ℓ²(Z³)⊗C⁴ from
supp φ̂ ⊂ (−π/a, π/a)³). Let P_a be the band-limit projection, and set
T_a(t) = (V J_a)* U_θ^{⌊t/a⌋} (V J_a) P_a.

**Theorem C (proved, conditional on P1–P3).**
1. *(Strong convergence.)* For every φ ∈ L², sup_{0≤t≤T} ‖T_a(t)φ − e^{−itH_D}φ‖ → 0
   as a → 0 (fibrewise convergence, the uniform bound 2, dominated convergence and
   P_a → 1). The same holds for lattice translations by ⌊x/a⌋ ↦ e^{−ip·x}.
2. *(Rate on the dense domain D_P = {supp φ̂ ⊂ |p| ≤ P}.)* For a(P+m) ≤ κ₀,
   ‖T_a(t)φ − e^{−itH_D}φ‖ ≤ [ a E_P + t( (|W|/2) a P² + C₃ a²(P+m)³ ) ] ‖φ‖,
   where E_P = sup‖H_a‖ ≤ √(m²+s²P²) + O(a). The first term is the floor
   (t − a⌊t/a⌋)‖H_a‖. The second comes from Duhamel, ‖e^{−itA} − e^{−itB}‖ ≤ t‖A−B‖.
   Since |W| = |s|√(1−s²), **the O(a·t) coefficient is s√(1−s²)P²/2, pinned to the
   axis-doubler gap.** It is 0.185 P² at b* and 0.236 P² at b_iso.
   *Quantifiers (review fix 3(i)).* Proved: there exist C₃, κ₀ > 0 such that this
   holds. The quoted C₃ ≈ 0.042, 0.033 and 0.051 (§3) are maxima over 120 sampled
   momenta with |p| ≤ 2, m = 1, a ≤ 0.04, that is, a(P+m) ≤ 0.12. They are lower
   estimates of the supremum on that sample, not certified bounds. **κ₀ has no computed
   value.** Items 3 and 4 inherit the same existential constants.
3. *(Light speed: O(a²).)* At b_gold, W = 0, so the error is a E_P + C₃ t a²(P+m)³
   for every twist.
4. *(Maximal twist: the O(a) error is removable by a p-dependent identification.)* At χ = π/2, W·τ = |W| Γ⊥, which
   anticommutes with α and β. The momentum-dependent chiral rotation
   V_a(p) = exp((φ/2) βΓ⊥) with tan φ = a|W|p²/(2m) commutes with α. It maps
   H_D + (a/2)|W|p² Γ⊥ to s α·p + √(m² + a²|W|²p⁴/4) β, which is exact. Hence
   ‖V_a U^n V_a* − e^{−itH_D}‖ = O(a²t(p⁴/m + (p+m)³)) + floor, with
   ‖V_a − 1‖ = O(a p²/m). The rate is not uniform as m → 0. This is the walk
   analogue of twisted-mass automatic O(a) improvement.
5. *(Wilson-aligned mass: the O(a) error is spectral.)* For cos χ ≠ 0 the spectrum
   itself shifts: E_a² = E² − a m|W| cos χ p² + O(a²). For unitary matrices the
   matching distance between spectra is bounded by the operator-norm distance
   (Bhatia–Davis): d(σ(A), σ(B)) ≤ ‖A − B‖. With A = V U^n V* for any unitary V,
   constant or p-dependent, the spectrum of A is {e^{∓inω}}, unchanged. Hence
   ‖A − e^{−itH_D}‖ ≥ |e^{−itE_a} − e^{−itE}| ≈ t·a m|W||cos χ| p²/(2E).
   *Non-aliasing qualifier (review fix 3(ii)):* this holds for t with |sin tE| bounded
   away from 0, so that e^{−itE_a} is not matched to e^{+itE}. In particular it holds
   in sup over t ∈ [0,T].

**Numerical confirmation** (t = 1, m = 1, |p| ≤ 2, 120 momenta, a = 0.04 → 0.005).
max‖U^n − e^{−itH_D}‖ has slope 1.00–1.02 for b* and b_iso at both twists. With
V_a(p), the slope is 2.00 at χ = π/2 and stays 1.01 at χ = 0. At b_gold the slope is
2.00. The bound in item 2 holds at every a, using the sampled C₃.

## 5. Doubler decoupling (proved)

- **Momentum sector.** For φ ∈ D_P, J_aφ has lattice momentum support |k| ≤ aP,
  and the walk conserves k. Its weight in any neighbourhood of a TRIM K ≠ 0 is
  therefore **exactly zero for all n**. A Gaussian packet of physical width Σ, with
  |φ̂|² ∝ e^{−2Σ²p²}, has weight ≤ 3 erfc(κ√2 Σ/a) outside |k_a| < κ. This is
  e^{−O(Σ²/a²)}, and the numerical FFT check agrees with the tail to < 3%.
- **Energy sector.** By Lemma V, every lattice momentum with some |k_a| ≥ π/2 has
  quasienergy ≥ arccos(1 − c_θ), so energy ≥ arccos(1 − c_θ)/a. Conversely, the
  spectral subspace with energy ≤ Λ lives in |p| ≤ (π/2)√((Λ² − m²)/c_θ) + O(a²)
  (using 1 − cos x ≥ 2x²/π² on [−π,π]).
  c_θ → c₀ > 0, with c₀ = 0.264, 0.318 and 0.296 for b*, b_iso and b_gold. **The
  doublers stay at distance ≥ π/(2a) in momentum and ≥ arccos(1−c_θ)/a in energy.**
  This holds at b_gold too: c₀ concerns ω near 0, not near π.
- **The π-modes at b_gold.** They sit at energy π/a − m → ∞ in the principal branch,
  and the decoupling above holds for every fixed φ. Caveat: on the X sector,
  U^n = (−1)^n e^{∓inθ}. For a two-tick clock (U²) the X triplet would sit at
  quasienergy −2ma and reappear as **three extra light Dirac species of mass m**.
  So the decoupling at b_gold depends on resolving the single-tick clock. These are
  temporal doublers. For b* and b_iso this caveat does not arise.

## 6. Emergent Lorentz violation

**Massive dispersion (exact symbolic, and confirmed numerically with O(ε⁵)
residual slopes):**

  E_a²(p) = m² + s²|p|² − a m|W| cos χ |p|² + a²[α|p|⁴ + β Σ_a p_a⁴ − (s²/3) m²|p|²] + O(a³),

with α = s(s³+3b₀−6b₁−9b₂)/12 and β = −s(b₀−b₁−2b₂)/3 (the parent's massless
coefficients). The m²p² term is new here.

- **Limiting speed:** s sites per tick (b*: 0.9144, b_iso: 0.8165, b_gold: 1).
  With τ = a this is the continuum c. Choosing τ = s a would set c = 1.
- **O(a):** −a m|W| cos χ p² is isotropic. For a single species it only renormalises
  the speed, c'² = s² − a m|W| cos χ. That is a **mass-dependent speed of light**: it
  violates Lorentz invariance only relative to other species, and it vanishes at
  maximal twist and at b_gold.
- **First genuine single-species violation is O(a²)**, the p⁴ terms. The cubic
  anisotropy coefficient is β: +0.0403 at b*, 0 at b_iso, and 7/6 − √5/2 = 0.0486
  at b_gold. The quartic coefficient along the axis vs the body diagonal is
  −0.0114 vs −0.0383 (b*), −0.0185 isotropic (b_iso), and 0 vs −0.0324 (b_gold).

## 7. Poincaré check

Take K_j = ½{x_j, H_a} with x = i∇_p, P = p, and J = L + ½σ.
**Lemma P (exact for any matrix function H(p); symbolic check):**
[K_j, P_l] = iδ_jl H, [K_j, H] = (i/2){H, ∂_jH}, and
[K_j, K_l] = −(½{H,∂_jH}∂_l − ½{H,∂_lH}∂_j + ¼[∂_jH, ∂_lH]).
For a Clifford fibre, {H, ∂_jH} = ∂_j(E_a²). With H = H_D this reproduces the
c = s Poincaré algebra: [K_j,H] = i s² p_j and [K_j,K_l] = −i s² ε_jlm J_m.
For H_a the defects are explicit:
- [K, P]: exact.
- [K, H]: (i/2)∇(E_a² − E²). This is O(a) (−i a m|W|cos χ p), and O(a²) at
  maximal twist or b_gold. Numerical slopes: 1.02 and 2.00.
- [K, K]: the orbital part is −½∇δE², while the spin part
  ¼([∂H_a,∂H_a] − s²[α,α]) = O(a|p|) from [sα, a p W·τ]. Generically O(a), even at
  maximal twist (slope 1.00), and O(a²) at b_gold (slope 2.00).
- Rotations: the O(a) term is rotation invariant. The O(a²) breaking comes only from
  the k³ anisotropy (b₁+2b₂−b₀)/6 · k_a³ of g (exact). So **[J, H_a] = O(a²)
  generically and O(a³) on the isotropy plane** (b_iso measured slope 3.00; b* and
  b_gold 2.00).

The strongest honest statement: on states with smooth, compactly supported momentum
wave functions, the Poincaré commutation relations hold up to defect operators of size
O(a)·(first-order differential operator), all listed above. **Group-level convergence
of lattice boosts is not proved here.** That would need an exponentiation argument of
the kind in the 1+1D note (`docs/GAPPED_CONTINUUM_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-12.md`),
which is open in 3D.

## 8. Literature: what is textbook and what is specific

I read only abstracts, via web search.

**Textbook or known:**
- Dirac QW/QCA continuum limits: Arrighi–Forets–Nesme, J. Phys. A 47 (2014),
  arXiv:1307.3524, 3+1D, fixed-time convergence with discrepancy O(ε²) for their walk.
- D'Ariano–Perinotti, PRA 90, 062106 (2014): bcc Weyl automata coupled into a Dirac
  automaton, Dirac recovered at small k and m, Lorentz distorted in the
  ultrarelativistic regime.
- Bisio–D'Ariano–Tosini, Ann. Phys. 354, 244 (2015): the 1D Dirac QCA, with
  channel-discrimination bounds and a dispersive wave-packet equation.
- Standard methods: the Duhamel/fibrewise strong-convergence argument and Wilson-term
  O(a) artifacts. Twisted-mass O(a) improvement is lattice QCD lore (Frezzotti–Rossi);
  I cite it from memory and did not check it.

**Specific here:**
1. The walk is one cubic-covariant tick on the simple-cubic 27-point cell with a
   two-qubit site. Its mass is the O(3)-orbit coordinate of the parent's Gram family.
2. Lemma V gives an exact, global node and gap certificate from multilinearity.
3. The O(a) coefficient is pinned to the doubler gap, |W| = s√(1−s²).
4. The twist dichotomy: O(a) is removable at χ = π/2 and spectral otherwise.
5. b_gold is O(a)-improved but carries massless or massive temporal (π) doublers.
6. Rotation breaking is O(a³) on the isotropy plane.

The arXiv:1307.3524 O(ε²) rate is not contradicted: different walks have different
W. Our b_gold is the analogue of their O(a²) case.

## 9. Finding in the parent runner (repaired 2026-10-18 under coordinator authorization)

`scripts/two_qubit_cubic_dirac_tick_2026_10_16.py`, function `omega2_series`, uses
arccos(1−u)² = 2u + u²/3 + **8**u³/45. The correct coefficient is **4/45** (sympy series,
and verified by hand inversion). This changes only the isotropic |k|⁶ coefficient of
parent Theorem 7:
- x(s) = s²(8s⁴−5s²+2)/360 → **s²(4s⁴−5s²+2)/360**;
- at b_iso, (1/243)|k|⁶ → **(1/1215)|k|⁶**.

The 60-digit direct evaluation of arccos²(f) agrees with 1/1215 along the axis and the
diagonal (c7_numeric). The anisotropic y = −s²/360, z, the "k⁶ anisotropy never
vanishes" claim and all orders ≤ k⁴ are unaffected. The parent's runner check passes
because both sides use the same series. The reviewer traced the origin of 8/45: it is the
y⁶ coefficient of arcsin(y)², quoted without the rescaling
arccos(1−u)² = 4 arcsin²(√(u/2)). The parent repair is recorded in §12.

## 10. Claim types

| claim | type |
|---|---|
| massive members = M U₀ M; mass is the O(3) orbit coordinate | proved (exact symbolic) |
| Lemma V, node locations, global dispersion bound, doubler mass bound, gold U(X) = −U(0) | proved theorem |
| TRIM table at b_iso and b_gold | exact algebraic |
| TRIM table at b* | numerical values of explicit algebraic numbers |
| Theorem A and Theorem B coefficients | exact |
| Theorem B: existence of C₃, κ₀ | proved (analyticity) |
| Theorem B: values of C₃ | numerical |
| Theorem C 1–5 | proved conditional on P1–P3, with C₃ as above |
| dispersion through O(a²) | exact symbolic, plus an independent numeric check |
| Poincaré Lemma P | exact |
| Poincaré defect scalings | exact leading order, numerical slopes |
| boost group convergence | not proved (open) |
| §9 parent coefficient | numerical (60-digit) plus exact series |

## 11. Load-bearing step for independent check

Theorem B's O(a) term (a/2)|p|² W·τ with |W| = s√(1−s²), and the sign
conventions α = −τ₃σ and β = −ĥ·τ. Together with the twist dichotomy (§4, items 4
and 5), they fix every O(a) statement here. A reviewer should re-derive H_a from
U = M U₀ M by a different route, for example a BCH expansion of the product
e^{iθΓ/2}U₀e^{iθΓ/2} rather than the O(3)-rotation identity. A second, cheaper item:
the multilinearity argument of Lemma V, and in particular that the vertex set is all 8
TRIMs including Γ.

## 12. Review dispositions (REVIEW.md, independent-code subagent review)

| review item | verdict | disposition |
|---|---|---|
| 1. O(a) term, signs, \|W\|, twist dichotomy | correct | none needed. The reviewer's independent routes are a direct log series of M U₀ M, \|W\| from the axis doubler with unitarity, and an eigenphase matching distance. |
| 2a. Lemma V extrema, dispersion bound, doubler bounds | correct | none needed |
| 2b. "every node of every member at a TRIM" | correct with fix | **applied**: adjacency hypothesis added in §2 item 1; the three named points are verified to satisfy it |
| 3(i). C₃ and κ₀ quantifiers | fix | **applied** in §4 item 2: existence is proved; the C₃ values are sample maxima (lower estimates); κ₀ is unquantified |
| 3(ii). Bauer–Fike → unitary matching distance, non-aliasing | fix | **applied** in §4 item 5 |
| 3(iii). item 4 is p-dependent | already stated | item 4 heading now says "removable by a p-dependent identification" |
| 4. parent 8/45 defect | correct (parent wrong) | **parent repaired** under coordinator authorization (§9; the runner and the Theorem 7 text are corrected, with a dated remark in the parent note) |
| 5. Lorentz coefficients | correct | none needed |
| not independently checked: Weyl indices, Lemma P and Poincaré slopes, literature | open | these remain single-author checks (exact symbolic and numeric in c7_exact and c7_numeric) |

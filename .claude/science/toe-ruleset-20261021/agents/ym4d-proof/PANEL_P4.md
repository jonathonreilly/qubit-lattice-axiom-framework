Reviewer model: claude-opus-5-5

# PANEL P4 — what T_OS on R^4 actually requires, and the best route to it

Panellist P4 (cross-family partner of Codex P1). Independent read: this file's §1-§7 were written
BEFORE reading PLAN_S26.md or any PANEL_*.md (§8 after PLAN_S26; §9 after the PANEL files). Labels: PROVEN (complete argument written here) /
ARGUED (convincing, identified hole) / CONDITIONAL (on a named input) / OPEN / [m] (from memory of
the literature, unverified). Every PROVEN/REFUTED label quoted from the lane is treated as an
unverified claim.

## PRE-STATED (written 2026-10-28T22:55:36Z, before reading any lane source beyond the brief)

**Question.** Decompose T_OS on R^4 (continuum limit of lattice SU(N) YM, OS0-OS3, not free, no mass
gap) into what is delivered by (i) UV control (uniform-in-cutoff bounds), (ii) compactness, (iii) IR
control. Assess the lane's early claim "OS1 on R^4 needs uniqueness of the infinite-volume state,
hence IR control comparable to a mass gap". Rank the routes. Say whether the finite-torus continuum
limit is a necessary milestone, a useful one, or a detour.

**Prior (stated now so it can be falsified by the sources; all literature items [m]).**
- P-a. Translations, the hypercubic group, RP (Osterwalder-Seiler lattice RP), OS3 symmetry, and
  temperedness should all pass to subsequential limits by compactness once local, volume-uniform UV
  bounds exist. Non-triviality should be a short-distance (UV) statement, because the running coupling
  is strictly positive at every finite scale.
- P-b. The only genuinely hard axiom is invariance under NON-lattice rotations. My prior is that the
  lane's claim is right in substance for the FLAT-LATTICE route (because SO(4)-averaging of a limit
  point destroys RP, and nothing else forces orientation-independence), but that it is stated too
  strongly as a law: (1) "uniqueness of the infinite-volume state" is neither exactly necessary nor, at
  fixed lattice spacing, sufficient — what is needed is that the selected limit not depend on the
  lattice orientation; (2) "comparable to a mass gap" is a difficulty estimate, not a logical
  implication (clustering with a polynomial rate, or convergence of a rotation-covariant scheme, would
  do); (3) the claim may have missed a route in which the rotation symmetry is EXACT at finite volume
  — a compact, maximally symmetric IR regulator (the round sphere S^4_R, isometry SO(5), RP across
  great spheres), where the R -> infinity limit by compactness inherits Euclidean invariance and RP
  without any uniqueness. I have not yet checked whether that route survives scrutiny; it moves the
  burden to UV universality (independence of the continuum limit from the cellulation), which every
  route needs anyway.
- P-c. The finite-torus continuum limit: prior = useful milestone, not logically necessary; useful only
  if its estimates are local (uniform in the torus size), otherwise partly a detour.

**What would change my mind.**
- On P-b(3): a concrete obstruction to reflection-positive lattice gauge theory on a cellulated S^4
  (e.g. RP needs a structure incompatible with every cellulation sequence whose continuum limit can be
  SO(5)-universal), or an argument that UV universality on a compact manifold already needs IR input.
  Or: finding that the lane already considered and rejected the sphere route for a reason I accept.
- On P-b(1)-(2): a lane argument showing that any route to rotation invariance must pass through
  uniqueness (not merely orientation-independence), or that the needed IR input provably implies
  exponential clustering.
- On P-a: evidence that local (volume-uniform) UV bounds are NOT available from the Balaban-type
  machinery even in principle (e.g. large-field regions force volume-dependent constants into local
  expectations), which would push OS0/compactness into the IR column too.
- On P-c: evidence that the torus estimates in the lane are intrinsically small-volume (coupling small
  at the torus scale), which would make the torus milestone a weaker stepping stone than I assume.

---

## 1. What the lane says (read by grep + sed; located by string, not line number)

- PROOF.md §0 ("## 0. Target, and how it decomposes"): T_fin on the torus T^4_M (side L^M in resolution-0 units, where g
  is small); T_OS = a state on an E(4)-covariant gauge-invariant algebra on R^4, "arises as such a limit", OS0-OS3, not
  free. Item 2: IR strong coupling "obstructs uniqueness ... Through uniqueness it also obstructs route γ1 to OS1 on R^4,
  so it may well obstruct existence of the OS theory itself." Item 3: OS1 "needs either universality (orientation
  independence, which rests on E7-type estimates) or a second, rotation-covariant observable family".
- PROOF.md "The obstruction, stated exactly": IR growth blocks "(1) uniqueness ... (4) through (1), the universality
  route to rotation invariance (L9b-β)" [the label should read γ1; L9b(β) is translations]; option "(C) prove uniqueness
  on R^4, which seems to require IR control comparable to a mass gap".
- PROOF.md L9b: (β) translations need E9.1 (a grid-offset comparison); (γ) R9.1 "averaging the limit over SO(4) gives
  invariance but destroys RP ... not a proof of impossibility"; γ1 universality "in infinite volume probably uniqueness";
  γ2 "A rotation-covariant family, e.g. gradient-flow observables ..., provides OS1. The block family provides OS2."
- PROOF.md L8a-L8c (compactness limits, lattice-translation/hypercubic invariance, RP preserved) and "L8d. Uniformity:
  OPEN" (E8 uniform in M).
- EXISTENCE.md §0 table rows (a),(b),(d): limit points, RP, L-adic translations, hypercubic symmetry, OS Hilbert space
  "from compactness alone"; not delivered: OS1, OS0 for local fields, uniqueness, OS4, gap. §4 X-ROT: OS1 needs H-rot
  "and, in infinite volume, probably H-uniq" or the two-family route. §5 X-IR: uniqueness etc. need "a gap or cluster
  expansion". §6 DAG line: "OS1: X-ROT [OPEN] ⇐ H-rot or (X-ARP + H-loc [OPEN])". X-SRC-GAP: OS0 for dimension-4
  composites is "UV stability with a position-dependent bare coupling g_0(x)".
- REVIEW_S22.md PART 5 (BFT): constants "depending only on (N, L, κ_±)", for "every torus whose level-k side is ≥ T_0
  (and every non-wrapping box ...)", with exponential locality BFT-3. So the layer-1 target is already stated in a
  volume-uniform, local form. Small-field only (max_P|log V| ≤ ε ≤ ε_0).
- literature/NOTES.md (lane's own transcription of open sources): Dimock's Balaban-type φ⁴₃ series proves stability bounds
  ∝ Vol(T_M) and states "Correlation functions: not proven"; Balaban CMP 109 is small-field only.
- I found NO mention of a sphere / S^4 / SO(5) / de Sitter regularization in PROOF.md, EXISTENCE.md, RTARGET.md or the
  literature notes (grep for "S^4", "S⁴", "SO(5)", "de Sitter", "sphere"; PANEL_* and PLAN_S26 excluded, unread).

---

## 2. Decomposition of T_OS on R^4

**Vocabulary (fixed here).** ℓ_0 = a fixed physical scale at which the running coupling is still small (the lane's
"resolution 0").
- **UV control** = cutoff-uniform bounds and comparisons for observables localised in a bounded region, obtained from the
  RG between the cutoff and ℓ_0 (every scale weakly coupled), holding *conditionally on, and uniformly in, the
  configuration outside* that region. Such bounds are automatically volume-uniform.
- **Compactness** = Tychonoff/Prokhorov/Banach-Alaoglu plus the fact that RP and invariance under an EXACT symmetry are
  closed conditions under weak limits.
- **IR control** = any statement about the state at distances ≫ ℓ_0: uniqueness, clustering, convergence (not just
  subsequential) of the infinite-volume limit, or independence of the infinite-volume selection from the regularisation.

| Ingredient of T_OS | UV control | Compactness | IR control |
|---|---|---|---|
| A limit state exists on R^4 | only for unbounded local fields (local moment bounds) | YES (L8a; block observables are bounded) | no |
| OS0 (tempered, with OS's linear-growth bound) | YES: position-uniform local exponential-moment bounds for the local fields (H-src'/H-src-flow) | passes bounds to the limit (X-MOM) | **no** (2.1) |
| OS2 RP | none for lattice-local observables; H-loc if flowed fields are used | YES (closed condition; L8c) | no |
| OS3 symmetry | — | — | no (automatic) |
| OS1: lattice translations, hypercubic group | — | YES (exact at every cutoff; L8b) | no |
| OS1: all translations | YES: equicontinuity in the shift (E9.1 / H-cont, a two-grid UV comparison) | YES (dense subgroup + continuity) | no |
| OS1: non-lattice rotations, FLAT route (tori, boxes) | YES: universality in bounded regions (rotated-grid comparison) | not enough (§3) | **YES**: the IR selection must be orientation-independent (§3-§4) |
| OS1: non-lattice rotations, SPHERE route (§5) | YES: universality on the compact S^4_R, plus two S^4-specific UV extensions | YES (R → ∞) | **no** |
| Not free | YES: a short-distance (scale δ ≪ ℓ_0) expansion with remainder, localised by conditioning on the field at a coarser weakly-coupled scale (the lane's (CE-cond) / L10) | passes a cutoff-uniform strict lower bound to the limit | no |
| (outside T_OS) OS4 clustering, unique vacuum, mass gap, independence of the subsequence, "the" YM theory | — | — | YES |

### 2.1 OS0 on R^4 needs no decay of correlations. PROVEN (implication)
Suppose, uniformly in the cutoff and in the position of a unit cube Q, E|Φ(f)|^n ≤ A^n (n!)^β N(f)^n for every f
supported in Q, where N is dominated by a Schwartz seminorm. For Schwartz f_1..f_n use a smooth partition of unity
f = Σ_Q fχ_Q with N(fχ_Q) ≤ C_k(1+|c_Q|)^{-k}|f|_{S,k}. Hölder, then Minkowski in L^n, gives
|E Π_i Φ(f_i)| ≤ Π_i Σ_Q (E|Φ(f_iχ_Q)|^n)^{1/n} ≤ (A C'_k)^n (n!)^β Π_i |f_i|_{S,k}, and Σ_Q (1+|c_Q|)^{-k} < ∞ for
k > 4. So S_n is a tempered distribution with OS's (n!)^β growth, and the bound passes to limit points (as in X-MOM).
Only position-uniform LOCAL moment bounds are used; no clustering. ∎ The input itself (local moment bounds for
dimension-4 composites or flowed fields) is UV (X-SRC-GAP: "UV stability with a position-dependent bare coupling
g_0(x)") and OPEN.

### 2.2 Non-triviality is a UV statement. ARGUED
Not-free is a statement at a scale δ ≪ ℓ_0 where g(δ) ∈ (0, g(ℓ_0)] is strictly positive along any AF-tuned sequence: some
local connected correlation of gauge-invariant fields differs from its free (N²−1 Maxwell copies) value by c·g(δ)^p +
o(g(δ)^p), c ≠ 0. Proving it needs a localised expansion (condition on the field at a coarser weakly-coupled scale and
bound the coarse-mediated part — the lane's SPEC-red / NG-red architecture), never decay beyond ℓ_0. The hole is the
UV input itself ((CE-cond), CE-loc), and the definitional choice of "the free theory" (EXISTENCE §21 already notes that
covariant-gauge Gaussian connections are not excluded by its witness). Not IR.

---

## 3. Why non-lattice rotations are different: three lemmas and a remark

### Lemma A (SO(4)-averaging destroys RP even with every symmetry a lattice limit point has). PROVEN
Let μ be the centred Gaussian measure on S'(R^4) with covariance Ĉ(p) = Π_{μ=0..3} (p_μ² + m²)^{-1}, m > 0.
- (i) μ is translation invariant, invariant under the hyperoctahedral group, and its covariance is RP for EVERY coordinate
  hyperplane: in the time representation C(t, p⃗) = (2m)^{-1}e^{-m|t|} Π_i (p_i² + m²)^{-1}, so for f supported in
  {x_0 > 0}, ⟨θf, Cf⟩ = (2m)^{-1}∫dp⃗ Π_i(p_i² + m²)^{-1} |∫_0^∞ e^{-mt} f̂(t, p⃗) dt|² ≥ 0; the other directions by
  symmetry. (A Gaussian measure with RP covariance is RP: standard [m: Glimm-Jaffe, Quantum Physics, Thm 6.2.2].)
- (ii) μ̄ := ∫_{SO(4)} R_*μ dR is translation and O(4) invariant, and is NOT RP for {x_0 = 0}.
- Proof of (ii). Its covariance is C̄(p) = F(|p|), F(r) = ⟨Π_μ (r²n_μ² + m²)^{-1}⟩_{n∈S³}. For each n some |n_μ| ≥ 1/2,
  so the product is ≤ (4/r²)Π_{ν≠μ}(r²n_ν² + m²)^{-1}; on the cap {|n_μ| ≥ 1/2} the normalised measure has density
  ≤ 2/|S³| in the other three coordinates (two caps per axis), each integral over R is π/(rm), so summing over 4 axes
  F(r) ≤ (64π³/|S³|) m^{-3} r^{-5} (4·2·4·2 = 64, checked in plain python); also
  F ≤ m^{-8}. Fix a real spatial test function g ≠ 0 and set c(t) := E_μ̄[φ_g(0)φ_g(t)] = (2π)^{-1}∫ e^{ip_0t}A(p_0)dp_0
  with A(p_0) = (2π)^{-3}∫|ĝ(p⃗)|² F(|(p_0, p⃗)|) dp⃗ ≥ 0. The bounds give ∫|p_0|A(p_0)dp_0 < ∞, so c is C¹ and even,
  c'(0) = 0, c(0) > 0, and c(t) → 0 (Riemann-Lebesgue). If μ̄ were RP, then for t_1, t_2 > 0 and Φ = aφ_g(t_1) + bφ_g(t_2)
  (sharp times reached by time-smearing and continuity of c), E[θ(Φ)Φ] = a²c(2t_1) + 2ab c(t_1 + t_2) + b²c(2t_2) ≥ 0,
  i.e. c(t_1 + t_2)² ≤ c(2t_1)c(2t_2). So c ≥ 0 on (0, ∞); a zero at t_0 > 0 forces c = 0 on (t_0/2, ∞), hence on
  (0, ∞), contradicting c(0+) > 0; so log c is midpoint convex and continuous, hence convex, on [0, ∞). Its right
  derivative at 0 is c'(0)/c(0) = 0, so log c(t) ≥ log c(0) for all t ≥ 0, contradicting c(t) → 0. ∎
- Consequence: R9.1's "not a proof of impossibility, only of the failure of the naive route" can be sharpened. The naive
  route fails for a state having ALL the symmetries a lattice limit point has (translations, hypercubic group, RP in all
  four directions). Any route must explain why the particular limit is rotation invariant.

### Lemma B (local rotation covariance + RP + translations do not force rotation invariance; and uniqueness is not needed for a symmetric selection). PROVEN for (i)-(ii); (iii)-(iv) standard [m]
Free Maxwell theory (one abelian copy), μ_0 its Euclidean measure on gauge-invariant observables (E(4)-invariant, RP
[m, standard]). Let F^(B) be the constant field F_12 = B ≠ 0 (other components 0), and μ_B the shift of μ_0 by a
potential of F^(B): F ↦ F + F^(B), W(γ) ↦ W(γ)·exp(iB·Area_12(γ)), with Area_12 the signed area of the projection of γ
onto the (1,2)-plane.
- (i) μ_B is translation invariant, but not invariant under the quarter turn in the (2,3)-plane:
  E_{μ_B}[F_12(f)] = B∫f ≠ 0 = E_{μ_B}[F_13(f)].
- (ii) μ_B is RP for {x_0 = 0}. F_12 carries no time index, so θF^(B) = F^(B). The shift T_B therefore commutes with θ
  and maps positive-time functionals to positive-time functionals, and
  E_{μ_B}[θ(G)Ḡ] = E_{μ_0}[θ(G∘T_B) · conj(G∘T_B)] ≥ 0. ∎
- (iii) μ_B obeys the same local conditional rules (DLR) as μ_0. For a Gaussian specification, shifting by an exact
  solution of the source-free field equations maps Gibbs states to Gibbs states, and a constant F solves ∂_μF_μν = 0.
- (iv) The periodic-torus limit of lattice Maxwell selects B = 0, because the flux per unit area is O(L^{-2}) [m].
- So a rotation-covariant local rule, RP and translation invariance together do not give a rotation-invariant state. The
  lane's worry about IR selection is therefore real, not an artefact. But (iv) shows that a rotation-invariant
  selection can happen WITHOUT uniqueness. (For SU(N), constant chromomagnetic backgrounds are unstable [m: Savvidy;
  Nielsen-Olesen], so this is an existence proof of the mechanism, not a prediction for YM.)

### Lemma C (a smooth regularisation with continuous time cannot be RP). PROVEN
Let ω be RP for θ and invariant under continuous time translations τ_t. Let Φ ∈ L²(ω) be a θ-invariant sharp-time-0
observable, and let c(t) := ω(Φ·τ_tΦ) be continuous. If c is differentiable at t = 0, then c is constant.
- Proof. Since ω(θ(τ_{t_1}Φ)·τ_{t_2}Φ) = c(t_1 + t_2), RP gives the 2×2 Hankel inequalities used in Lemma A.
- Cauchy-Schwarz gives |c| ≤ c(0). So log c is convex and bounded above on [0, ∞) (or Φ = 0), hence non-increasing.
- c is even, so c'(0) = 0, and convexity then gives c(t) ≥ c(0). So c is constant. ∎
- Consequence. Any regularisation with continuous Euclidean time whose sharp-time correlations are C¹ at coincident
  times violates RP unless its dynamics is trivial. Examples: momentum cutoffs, mollified or heat-kernel smoothing,
  regularisations defined through gradient flow.
- If the regularisation is also O(4)-invariant, every direction is a time direction. So no smoothing in any direction
  is compatible with RP. The dichotomy "lattice: RP but no rotations / smooth: rotations but no RP" is structural.
- Lattices escape because time is discrete. Cell-based random lattices are not excluded, since their cell structure
  produces cusps, but I know of no RP construction for them.

### Remark D (universality cannot be avoided in a lattice route). ARGUED, using Jordan's theorem [m]
- A lattice in R^4 has a finite point group, and a finite cellulation of S^4 has a finite symmetry group.
- An increasing union of finite subgroups of SO(5) is never dense. By Jordan, each one has an abelian normal subgroup
  of index ≤ J(5). A Hausdorff limit would then give the connected non-abelian group SO(5) a closed abelian subgroup of
  finite index, which is impossible.
- So every lattice route, on R^4 or on S^4, must prove that the limit does not depend on the orientation of the
  regularisation, at least in bounded regions. This is the UV core of the lane's γ1/H-rot. The difference between
  routes is whether an IR statement is ALSO needed.

---

## 4. The lane's claim: "OS1 on R^4 needs uniqueness of the infinite-volume state, hence IR control comparable to a mass gap"

### 4.1 Right in substance FOR THE FLAT ROUTE. ARGUED
If the IR regulator is flat (tori T^4_M, or boxes), no finite-volume approximant has a continuous rotation symmetry, so
rotations must be restored in the M → ∞ limit. Lemma A shows compactness cannot do it, and Lemma B shows local
covariance cannot force it. So some statement about the infinite-volume selection is unavoidable: an IR statement.
On this route the lane is correct, and I agree that it is the hard core.

### 4.2 But it is over-broad and mis-stated in four ways
- **(a) Scope.** Only NON-lattice rotations need it. Translations, the hypercubic group, RP, OS0, OS3 and
  non-triviality do not (§2). The lane agrees elsewhere (EXISTENCE §5 "Not needed for ..."); §0 item 2's "may well
  obstruct existence of the OS theory itself" is only about OS1.
- **(b) "Uniqueness" is not necessary.**
  - What the flat route needs is that the selected limit points do not depend on the orientation of the lattice.
  - Lemma B(iv) gives a gauge theory in which a symmetric selection happens without uniqueness.
  - §5 gives a route with no IR statement at all.
- **(c) "Uniqueness" is not sufficient alone either.**
  - Uniqueness of the infinite-volume Gibbs state at each fixed lattice spacing compares nothing across orientations.
    Rotation invariance also needs universality in bounded regions (H-rot, UV); see Remark D.
  - A correct flat-route statement is: [rotated-grid universality in bounded regions (UV)] + one of the following IR
    inputs:
    - (I1) uniqueness among TRANSLATION-INVARIANT Gibbs states of the limiting local specification;
    - (I2) torus limits converge independently of the orientation of the period lattice;
    - (I3) a unique vacuum, with stress-tensor correlations decaying faster than |x|^{-4}. This kills the flux at
      infinity in the rotation Ward identity, given a symmetric conserved T_μν from UV control.
  - All three are ARGUED sufficient, and none is shown necessary. Caveat on (I1): for gauge fields the "continuum
    specification" must be built at scale ℓ_0, where the block variables are hypercubic, so (I1) is the least clean.
- **(d) "Comparable to a mass gap" is a difficulty estimate, not an implication.**
  - (I3) needs clustering with a polynomial rate, not a gap.
  - Massless scaling limits with rotation invariance exist without a gap [m: critical 2D Ising, via discrete
    holomorphicity]. There the limit is identified by integrability, not by decay.
  - For 4D SU(N), though, every known way to get (I1)-(I3) at the confinement scale would also give a gap. As a
    practical estimate the lane's wording is fair; as logic it is not.

### 4.3 Incomplete: it missed a route class
- It missed compact, maximally symmetric IR regulators: the round S^4_R, whose isometry group SO(5) ⊃ SO(4) contracts to
  E(4). There, rotation invariance is a FINITE-VOLUME universality question (UV), and the IR limit R → ∞ is pure
  compactness (§5).
- It also treats "an RP and rotation-invariant regularisation" as merely unexplored. For smooth regularisations, Lemma C
  shows it is impossible.

### 4.4 Two concrete defects in the lane's text
- **γ2 / the EXISTENCE DAG line "OS1: X-ROT ⇐ H-rot or (X-ARP + H-loc)" is a non sequitur.**
  - A rotation-COVARIANT observable family is needed to even state OS1. Invariance of the STATE is a separate fact.
  - X-ARP + H-loc only place the covariant (flowed) family inside the RP structure. They say nothing about
    ω(R·F) = ω(F).
  - So γ2 is not an alternative to γ1. It is the algebra-side component that every route needs, and it still needs γ1
    (or §5) for invariance.
  - PROOF L9b's "A rotation-covariant family ... provides OS1" should read "provides the E(4)-covariant algebra on which
    OS1 can be stated".
- **PROOF §0 item 1(b) "uniqueness, i.e. convergence of the whole sequence (estimate E7)" conflates two different
  things.**
  - Cutoff convergence at fixed volume (E7_fin) is UV.
  - Independence of the infinite-volume selection (E7_∞) is IR.
  - For OS1 via §5, not even E7_fin is needed: a DIFFERENCE-form universality estimate suffices (§5.3, S2). Subsequential
    limits plus "the rotated and unrotated regularisations differ by o(1)" already force invariance of every limit
    point.
- Label slip: "The obstruction, stated exactly" item (4) cites "L9b-β" for the universality route; in L9b that route is
  γ1, and (β) is translations.

---

## 5. The missed route: the round sphere S^4_R as a symmetric IR regulator

### 5.1 Idea. ARGUED
Use the round 4-sphere of radius R as the IR regulator. Its isometry group O(5) contains the isotropy group O(4) at
every point, and as R → ∞ it contracts to E(4) [m: İnönü-Wigner].
- The volume is finite. So every finite-volume argument applies: the IR end of the RG is a compact, finite-dimensional
  integral, and no uniqueness question arises.
- After UV universality, rotations are an EXACT symmetry at each finite R. RP holds for every great sphere.
- R → ∞ is then pure compactness, and invariance and RP are closed conditions. No IR statement enters T_OS.

### 5.2 A concrete regularisation that is locally an ordinary Wilson lattice
- **Chart.** Stereographic projection maps a closed hemisphere onto the ball B_R ⊂ R^4 with metric Ω(x)²δ_μν, where
  Ω = 2R²/(R² + |x|²) ∈ [1, 2]. Classical 4D YM is conformally invariant (√g g^{μα}g^{νβ} = Ω^4Ω^{-4}δδ), so in this
  chart the classical action is the FLAT action.
- **Southern grid Λ_-.** The hypercubic grid aZ^4, restricted to a union of grid cubes that approximates B_R. The local
  physical spacing is aΩ(x).
- **Northern grid Λ_+ := θ_eq(Λ_-).** θ_eq is the equatorial reflection, which is the inversion x ↦ R²x/|x|² in this
  chart; in the northern chart Λ_+ is again a flat grid.
- **Seam ("prism layer").**
  - For every vertex v of the boundary layer of Λ_-, a crossing link v — θ_eq v.
  - For every boundary edge (v, w), a crossing plaquette (v, w, θw, θv).
  - Physical length O(a): a codimension-1 lattice-scale defect.
- **Action.**
  - The Wilson action on Λ_±, with a position-dependent bare coupling g_0(x) fixed by the two-loop AF function f:
    f(g_0(x)) = aΛ_phys Ω(x)/C_W, where C_W is the (position-independent) Wilson-action Λ-ratio. This makes the local
    Λ uniform in physical units, with the same Λ_phys for every R (a fixed physical renormalisation condition as R
    grows); corrections are O(g_0²) → 0.
  - Weights β_p ≥ 0 on the crossing plaquettes.
- Every cell away from the seam is a standard hypercube up to O(a/R) distortion. So the flat Wilson-lattice UV theory
  applies locally, with a slowly varying coupling.

### 5.3 Steps and their status
- **S1. RP for θ_eq at every cutoff: PROVEN.**
  - The crossing links form a matching (pairwise disjoint, no loop), so a gauge transformation on one side sets them to
    1.
  - Each crossing plaquette weight is then exp((β_p/N) Re tr(W_p θ(W_p)^†)) with β_p ≥ 0, and
    e^{-S} = e^{A_-}θ(e^{A_-}) Π_cross(...) with A_- real and Haar product measure.
  - L9a's computation ("Proof re-derived (link reflection ...)") uses only these properties, so it applies verbatim. ∎
- **S2. SO(5) invariance from universality in DIFFERENCE form: OPEN, UV-type (ARGUED).**
  - Required estimate: for g in a countable dense G_0 ⊂ SO(5) and O in a geometrically defined (covariant) local
    algebra, E_{𝒦_n}[O] - E_{g𝒦_n}[O] → 0.
  - Since E_{g𝒦}[O] = E_𝒦[g^{-1}·O] exactly, every subsequential limit μ_R satisfies μ_R(g^{-1}O) = μ_R(O). That gives
    G_0-invariance, hence SO(5)-invariance by continuity. **E7-type convergence is not needed.**
  - Why this is UV:
    - (i) At fixed R the coarse field at ℓ_0 is (R/ℓ_0)^4 compact variables, so its law is a density on a compact
      finite-dimensional space.
    - (ii) Compactness of SU(N) bounds the coarse curvature by O(ℓ_0^{-2}) for EVERY coarse configuration, including
      "large" ones. So the grid dependence of the conditional fine-field integrals is a weak-coupling lattice artefact,
      O((a/ℓ_0)^θ) per block. This is the step to verify.
    - (iii) The summed error is O((R/ℓ_0)^4 (a/ℓ_0)^θ) → 0 at fixed R. No decay of correlations is used.
  - The local content is the rotated-grid comparison in bounded regions that every lattice route needs (Remark D), plus
    scale covariance (a Möbius map is locally a rotation plus a dilation).
- **S3. RP for every great sphere: PROVEN given S2** (conjugate θ_eq by SO(5); RP is invariant under conjugation).
- **S4. Two S^4-specific UV extensions: OPEN, UV-type.**
  - (a) A slowly varying bare coupling. This is the same technology X-SRC-GAP needs for OS0 (a source for tr F² is a
    coupling variation). Gradient terms are irrelevant: pure YM has no gauge-invariant local operator of dimension < 4
    (dimension counting, ARGUED).
  - (b) The seam, a codimension-1 lattice-scale defect. It is irrelevant by the same counting: no gauge-invariant local
    operator of dimension ≤ 3 exists, and the parity-odd Chern-Simons density is excluded by θ_eq symmetry (ARGUED).
    Its rigorous form is a Balaban-type RG near a reflection-symmetric boundary layer.
- **S5. R → ∞: ARGUED, given volume-uniform local bounds (the L8d analogue).**
  - Pull back by the exponential map at a pole N.
  - SO(4) invariance is exact: isometries fixing N act linearly in normal coordinates.
  - RP for every hyperplane through 0 is exact: great spheres through N are totally geodesic, and their reflections act
    linearly.
  - Translations: the rotation moving N to exp_N(v) acts on a fixed bounded set as x ↦ x + v + o(1) as R → ∞.
    Invariance passes to the limit through equicontinuity of the Schwinger functions (OS0-type, UV).
  - So E(4) invariance and RP hold for all hyperplanes. Non-triviality as §2.2, OS0 as §2.1.
- **Output.** A state on R^4 satisfying OS0-OS3, not free, obtained as a limit of lattice gauge theories (locally
  hypercubic Wilson lattices with a slowly varying coupling). No uniqueness, clustering or gap is used.

### 5.4 Holes and costs, largest first
- **H1. The UV programme itself.** Large fields, the R-operation, correlation functions and local moment bounds. Shared
  with EVERY route, and the dominant risk.
- **H2. Rotated-grid universality in bounded regions** (difference form). Shared with every lattice route (Remark D).
- **H3. Loss of the chessboard shortcut (a real cost, specific to this route).**
  - The lane's large-field probability bounds use FILS chessboard estimates on even tori: PROOF E8.1 and E8*-red;
    EXISTENCE Theorem CB, and (LF-loc) "⇐ Theorem CB + ...".
  - Those need reflections through every plane of a periodic family. S^4_R has an exact lattice RP only for θ_eq.
  - The finite Coxeter groups of S^4 have fixed fundamental domains, so they give no cell-level chessboard.
  - So the sphere route needs unconditional large-field bounds of Balaban's own, action-based kind; the lane's E8** is
    "the probability-level form of" L5 + L6. Still UV, but harder than the torus shortcut.
- **H4. The S4(a)-(b) extensions.** UV and moderate; (a) is needed for OS0 anyway.
- **H5. A covariant local field algebra with RP.** Renormalised composites via S4(a), or flowed fields + H-loc. UV.
- **H6. A reading question for the owner.**
  - Does "a limit of lattice gauge theories on cellulations of S^4_R, R → ∞" meet T_OS's "arises as such a limit"?
  - The sphere-route state need not be a limit point of the flat-torus states; identifying the two is IR.
- **Precedent.** I know of no lattice construction in d ≥ 3 that used S^d to get Euclidean invariance without uniqueness
  [m, uncertain]. P(φ)₂ on S² (Euclidean de Sitter) is classical [m: Figari-Høegh-Krohn-Nappi, CMP 1975], but there
  rotation-invariant continuum regularisations exist, so the issue never arose.

---

## 6. Ranking of routes to the FULL T_OS, and the torus milestone

**Ranking, by likelihood of delivering T_OS (OS0-OS3 + not free on R^4).** Qualitative; every route shares H1, the UV
programme, which dominates the absolute odds.
1. **Sphere route (§5).** It is the only route with no IR step. Its extra costs over the shared core are UV:
   - H3: action-based large-field bounds without chessboard;
   - H4: a slowly varying coupling plus a seam;
   - H6: the owner's reading of "lattice".
   Conditional on the flat UV programme succeeding WITH conditional local bounds, the remaining risk sits in S2 (my
   least-sure step, §7) and the S4 extensions, and I rate it more likely than not. Unconditionally it is low, but
   strictly better than 2-5.
2. **Flat route + an IR input weaker than a gap.** One of:
   - (I1) uniqueness among translation-invariant states of the limiting specification;
   - (I2) torus limits independent of the period lattice's orientation;
   - (I3) a unique vacuum with polynomial stress-tensor clustering.
   Logically weaker than a gap, but no known non-perturbative 4D technique delivers any of them. Very low.
3. **Flat route + full IR control.** RG to the crossover, then a strong-coupling cluster expansion. This is the
   Millennium problem's hard part; if it worked it would also give the gap. Lowest of the "known architecture" routes.
4. **RP + Euclidean-invariant regularisation in flat space.** Smooth ones are excluded (Lemma C). Non-smooth ones
   (cell-based random lattices) are not excluded, but have no known RP construction and no UV theory. Very low.
5. **Stochastic quantisation / SPDE.** 4D YM is the critical dimension, outside subcritical SPDE theory [m]. Very low.
- **Not a route by itself: γ2 "two families"** (§4.4). It is the E(4)-covariant-algebra component of 1-3, and it
  needs γ1 or §5 for invariance.

**The finite-torus continuum limit T_fin: a useful milestone, not a necessary one; parts of it are a detour.**
- **Not necessary.** Route 1 uses S^4_R as its finite volume; nothing about T^4 enters T_OS.
- **Useful**, because S^4_R in stereographic charts is locally a flat hypercubic Wilson lattice. The flat UV machinery
  developed on the torus (Fourier-friendly, translation invariant) is exactly what route 1 re-uses. It is useful IF
  T_fin is built to deliver the reusable outputs:
  - (i) local, volume-uniform estimates (BFT is already stated this way: "every torus whose level-k side is ≥ T_0 ...
    and every non-wrapping box");
  - (ii) large-field bounds that are conditional / boundary-uniform, not only chessboard-global;
  - (iii) UV stability with a position-dependent coupling g_0(x) (OS0 sources, and S^4);
  - (iv) difference-form universality for grid offsets (E9.1) and for rotated grids in bounded regions (H2);
  - (v) an E(4)-covariant local field algebra with RP (H5).
- **Detour for T_OS:**
  - the torus-specific non-triviality machinery (toron moduli, spatial Polyakov loops, centre symmetry; EXISTENCE §18
    itself says "Physically a tiny box ... not progress on continuum non-triviality");
  - constants that grow with M;
  - chessboard-only large-field bounds, if route 1 is adopted. They are fine for T_fin and do not transfer.
- **Concrete recommendation.** Run two finite-volume targets in parallel:
  - T_fin(T^4), the UV laboratory, where the chessboard is allowed;
  - T_fin(S^4_R) with SO(5) invariance and great-sphere RP, which is the one that feeds T_OS.
  - Make S2 (rotated-grid universality in bounded regions, difference form) an explicit early lemma target, since every
    route needs it.

---

## 7. Short ranked conclusion (before reading PLAN_S26 or any PANEL file)

1. **What T_OS needs.**
   - OS0, OS2, OS3, translations, the hypercubic group and non-triviality need only UV control (local, conditional,
     cutoff-uniform bounds) plus compactness.
   - Non-lattice rotations are the only ingredient that can need IR control.
2. **The lane's claim** is right for the flat route (tori or boxes as IR regulators), and I agree OS1 is the hard core
   there. As a general statement it is wrong:
   - uniqueness is neither necessary nor sufficient by itself;
   - "comparable to a mass gap" is an estimate, not an implication;
   - it missed the compact symmetric regulator S^4_R, on which OS1 becomes finite-volume universality (UV) and
     R → ∞ is pure compactness.
3. **Lemmas proven here.**
   - A: SO(4)-averaging kills RP even for a state with all lattice symmetries.
   - B: a free gauge theory has RP, translation-invariant, rotation-breaking Gibbs states, yet its torus limit selects the
     symmetric one, so selection is real and uniqueness is not needed.
   - C: no smooth continuous-time regularisation is RP.
4. **Defects found.** The lane's DAG edge "OS1 ⇐ X-ARP + H-loc" (γ2) is a non sequitur, and E7 conflates fixed-volume
   convergence (UV) with infinite-volume uniqueness (IR).
5. **Route ranking.** Sphere > flat + weak IR input > flat + full IR (gap) > RP + rotation-invariant regularisation >
   SPDE.
6. **T_fin on the torus** is a useful laboratory, not a necessary milestone. Its small-box non-triviality and
   chessboard-only large-field bounds do not transfer.

**Least sure of.** That S2 (universality on S^4_R in difference form) is genuinely UV.
- The step "SU(N) compactness bounds the coarse curvature, so the grid dependence of conditional fine integrals is
  uniformly O((a/ℓ_0)^θ) over ALL coarse configurations" is ARGUED, not proven.
- It needs a common coarse space for two different grids: soft blocking onto a common grid, or grain-boundary hybrids.
- If S2 secretly needs IR input, route 1 collapses to route 2.
- Second: H3. The lane's large-field architecture leans on the chessboard, which S^4 does not have.

---

## 8. PLAN_S26 (the lead's view): agreement and disagreement

Read only after §1-§7 above were written: PLAN_S26 §1-§2 and §7. The §7 print range also showed §8 (role split); §9
("Consensus so far") was NOT read.

**Agree.**
- **§1, OS1 must be on the critical path.** "Finishing every layer-1 item does not finish T_OS" is right, and it is the
  most important sentence in the file. On the flat route OS1 is the IR crux. On the sphere route it is S2 plus the S^4
  extensions, and those are not layer-1 internals either.
  - The lead says HANDOFF.md's critical path has no OS1 item; I did not read HANDOFF.md and have not verified this.
- **§7, the claim gets no-go scrutiny.** "The lead's claim that it is out of reach is exactly the kind of claim this
  lane has repeatedly got wrong; it gets the same scrutiny as any no-go." My finding fits: the claim survives only for
  the flat route.
- **§1, what T_fin's content is.** The torus OS structure is mostly free by compactness (EXISTENCE §0 (a)-(b)); the
  content is consistency, non-triviality and OS0, all UV/layer-1. §2 above agrees.
- **§2b, read Balaban's primary papers.** It matters MORE on route 1: the sphere loses the chessboard shortcut (H3), so
  Balaban's own action-based large-field technology [m: CMP 116, 122] is what route 1 must import. In the lane's own
  words, E8** is "the probability-level form of" L5 + L6.
- **§2d, what a proof needs.** Acyclicity plus K- and T-uniformity is the right criterion. For route 1, add uniformity in
  R (sphere radius) and in the slowly varying coupling g_0(x).

**Disagree.**
- **§1's parking rule (withdrawn in §7, but its premise survives there).** "Attacked only if someone has an idea for
  rotation invariance without uniqueness": §5 is such an idea, so by the lead's own rule OS1 should be attacked.
- **§7's premise.** §7 restates OS1 "as needing uniqueness (IR control comparable to a mass gap)". That is route-
  dependent: true for flat IR regulators, false for S^4_R. It is also imprecise on the flat route (§4.2(b)-(d)).
- **§7, "Every route to T_OS passes through ... finite-volume limits, so T_fin is milestone 1".** Right if T_fin means
  "a finite-volume continuum limit"; not right if it means the TORUS.
  - Route 1's finite volume is S^4_R. The torus is a laboratory for the flat UV machinery, not a logical prerequisite.
  - Two of the torus programme's current deliverables do not transfer: small-box non-triviality via toron moduli, and
    chessboard-only large-field bounds.
  - I would make the milestone "T_fin(T^4) as the laboratory + T_fin(S^4_R) as the feeder", with the conditional
    (boundary-uniform) large-field bounds and the rotated-grid universality lemma S2 as explicit early targets.
- **§2c (soft vs hard scheme) misses one argument for the soft scheme.** A smooth blocking kernel can block a ROTATED
  fine grid onto an axis-aligned coarse grid, which gives the common coarse variables that S2 needs. Balaban's hard
  constraint (path averages inside aligned blocks, as in S4/S4') is tied to aligned blocks and does not do this
  naturally.
  - This is a concrete OS1-side benefit of Decision 4 that the re-pricing should include.
  - It is a design note (ARGUED), not a verdict on 2c.

**Outside my question.** §2a, §2e, §2f and §2g concern layer-1 internals and process; no view here.

---

## 9. Comparison with the Codex panellists P1, P2, P3 (read only after §1-§8 were written)

The three files were read by heading-grep + sed ranges. Their own labels are treated as unverified claims; I re-checked
only the arguments named below.

### 9.1 Points where all four of us agree
- **"OS1 needs uniqueness" is not a logical necessity.**
  - P1 §1 table and §2: uniqueness is "one sufficient mechanism, not an axiom".
  - P2 §1: "The necessity claim is too strong".
  - P3 §4: C "is neither necessary nor excluded by 'no mass gap'".
  - Mine: §4.2(b).
  - All four of us also say uniqueness ALONE is insufficient without regulator/universality input (P1 §2 "A second
    defect", P2 §7.1 "strength distinction", P3 §2 Gaussian with a unique cutoff limit and no O(4), mine §4.2(c)).
- **"Comparable to a mass gap" is an estimate, not an implication.**
  - P1 and P3 each give a gapless example with a unique vacuum or with clustering; P3 §7's clustering check is correct
    as written (|h|^{-2} cross-covariance).
  - P2's TORQUE needs only stress-channel decay |x|^{-4-η}; that is my (I3).
- **R9.1 is a warning, not a no-go, and the naive averaging route is nonetheless dead.**
  - P1 and P2 give averaged plane-wave scalar fields with an explicit negative RP form; their arithmetic is consistent.
  - My Lemma A is the strongest version of the hypotheses: the pre-averaged state has every lattice symmetry, including
    RP in all four coordinate directions.
  - P3 §2 uses the same covariance as Lemma A in position space, Π_μ e^{-|x_μ|}, for a different purpose: a unique
    cutoff limit with all lattice symmetries and no O(4). The two uses are complementary.
  - All four of us agree that averaging is legitimate GIVEN RP for every plane, which is sufficient (P1 §3, P2 §5,
    P3 §2); P2 §5 also gives a weaker sufficient criterion (a vanishing angularly averaged RP defect).
- **γ2 is a non sequitur as written.** P1 ("an intertwining identity, not invariance of the input law"), P2 §4
  ("equivariance does not imply invariance") and P3 §2 ("covariance of a map says nothing about invariance of its input
  law") agree with my §4.4. P2 §4 adds that fixed-t heat flow can destroy RP even for a free input; this is an instance
  of my Lemma C.
- **The torus milestone is useful, not necessary.** P1 §6, P2 §11 and P3 §7 agree. P1 (§6), P3 (§5) and I flag tiny-box /
  wrapping-holonomy non-triviality as non-transferable.
- **Non-freeness needs a calibrated free comparator.** P1 §4, P2 §8 and P3 §5 each show a Gaussian composite or a
  Gaussian mixture with a nonzero fourth cumulant; my §2.2 makes the same definitional point. It is not IR.
- **Volume-uniform local estimates are indispensable even without a gap.** P1 ("volume control") and P3 ("'no gap
  needed' must never be shortened to 'no volume-uniform estimates needed'") are right. In my vocabulary these are part
  of UV control, because I DEFINE it as conditional and local. The disagreement is terminological only.

### 9.2 The main disagreement: what should rank first
- **The Codex rank-1 routes all have the same structure.**
  - P1 rank 1, P2 rank 1 (S0-S4 with (D) + TORQUE) and P3 rank 1 all take a selected joint or diagonal sequence on FLAT
    regulators and prove a symmetry-defect estimate "η(a) + b(R) → 0".
  - I accept their selection lemmas as correct implications. P2's diagonal construction is clean; I checked its
    quantifier order.
- **But on flat regulators the b(R) term is the IR selection problem itself.**
  - P2 says so outright: TORQUE "is nevertheless infrared information: calling it 'UV locality' would be wrong".
  - P1's own covariance identity (§3, "Why irrelevant coefficients alone do not finish OS1") shows that an O(a^η)
    extensive perturbation acts through a^η∫_box Cov(F, O(x))dx, and that "phase selection can be sensitive to
    arbitrarily small extensive perturbations".
  - All three Codex panellists name exactly this as their least-certain step.
- **So their rank 1 = my rank 2.** It is a weaker-than-gap IR input on a flat route, and none of them has a mechanism
  for it.
- **The sphere route is the instance of THEIR selection lemma in which b ≡ 0.**
  - S^4_R is a closed manifold, and its SO(5) Killing fields are global.
  - So in P2's Ward form (W) the cut-off vector field χ_R·Jx is unnecessary and the boundary torque term does not exist.
  - The only defect is the regulator term. At fixed R it is a finite-volume quantity: P1's a^η∫Cov is bounded by
    a^η·Vol(S^4_R)·sup|Cov| → 0 with no volume uniformity needed, which is P2's "C(R) may grow".
  - The flat translation and rotation identities are then recovered as R → ∞ by compactness.
- **None of P1-P3 considered a compact homogeneous regulator.** P2 §7.3 considered BALLS and correctly noted that an
  origin-centred exhaustion gives neither translations nor RP at displaced planes. P2 §9 (N7) names "an exactly covariant finite-volume construction with
  controlled translations" as the strongest challenge to its own recommendation. S^4_R is such a construction: SO(5)
  contracts to E(4), so translations come from rotations moving the pole.
- **My recommendation stands.** Merge the two: the panel's selection lemma, instantiated on S^4_R, is rank 1. The flat
  version with TORQUE is rank 2.

### 9.3 Disagreements of detail
- **P1 rank 1, "Tori can serve as regulators throughout": disagree.** Tori are fine for UV and large-field work (the
  chessboard is available there, my H3), but not for the OS1 step (§4.1, §9.2).
- **P1 rank 2 / P3 route D (a continuum-covariant construction, then lattice identification).**
  - In infinite volume the identification of two regularisations' states is itself IR.
  - Done on S^4_R it is finite-volume universality (UV). So route D is best run on S^4_R too.
- **The "new isotropic regulator" (P2 §7.3 OPEN; P3's alternative D).**
  - My Lemma C sharpens P2's heat-flow example into a theorem: no continuous-time regulator with C¹ sharp-time
    correlations is RP.
  - So an isotropic RP regulator must be non-smooth, lattice- or cell-like.
  - P3 cites Gantumur, "Rotationally invariant dynamical lattice regulators ..." (JHEP 07 (2026) 036; abstract checked by
    P3, NOT by me; postdates my reliable memory). P3 reports finite-volume RP for a fluctuating-embedding regulator.
  - That would fall exactly in the loophole Lemma C leaves open. It raises my route 4 from "no candidate" to "one
    unaudited candidate", and should be audited before anyone builds on it.
- **P2 §11's soft-variable caveat** (independent kernel noise makes literal L² comparisons of different soft branches
  fail). It does not hit S2: S2 compares the LAWS of coarse variables blocked onto a common grid (densities on one
  compact space), or expectations of covariant observables, never two soft random variables pathwise.
- **P2's group lemma (H_4 + one spatial-plane rotation ⇒ O(4)) is correct and useful.** I adopt it: on the flat route it
  cuts the rotation work to one plane. On the sphere route the analogue is that the regulator's finite symmetry group
  plus a one-parameter subgroup generating SO(5) together with it suffices.

### 9.4 What the Codex files add that I missed or under-weighted
- **P3's literature audit.** Shen-Zhu-Zhu (strong-coupling lattice YM: uniqueness and exponential decay in an explicit
  regime) and Driver (U(1)₄ continuum limit, with a state-selection result) are reported by P3 with abstracts checked;
  I have not verified either.
  - Driver, if as reported, is a real precedent for my Lemma B(iv): selection without uniqueness in 4D gauge theory.
  - P1 and P3 both report checking that Gubinelli-Hofmanová leave rotations and clustering outside their result, which
    matches my [m].
- **P3 §1: partition-function control gives no normalised local moment.** Correct. It is why my §2 insists on CONDITIONAL
  local bounds.
- **P2 §5: RP is not hereditary under decomposition.** Correct, and relevant only to OS4, which is outside T_OS.

### 9.5 What none of the Codex files addresses, and which my route must still answer
The cost H3. The sphere has an exact lattice RP plane only for θ_eq, so the lane's FILS-chessboard large-field bounds
(E8.1, E8*-red, Theorem CB) do not transfer, and route 1 must use action-based (Balaban-type) unconditional large-field
bounds. The flat routes keep the chessboard. This is the one place where the flat routes are genuinely cheaper, and it
is UV-side.

**Post-panel ranked answer (unchanged in order; sharpened in content).**
1. **The panel's selection lemma on S^4_R.** b ≡ 0; the OS1 defect is finite-volume universality S2 (UV). Costs: H3
   (no chessboard) and S4 (varying coupling + seam).
2. **The same lemma on tori, with TORQUE** (polynomial stress-channel decay), an IR input weaker than a gap with no
   known mechanism.
3. **A covariant construction plus identification (route D),** best run on S^4_R; or an isotropic RP lattice-type
   regulator (Gantumur-type, unaudited).
4. **Averaging repaired by all-plane RP.**
5. **Uniqueness / clustering / gap first.**

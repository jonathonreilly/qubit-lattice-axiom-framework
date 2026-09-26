# The neutral moving-records law at low density: an explicit sphere threshold z₀(β) ~ 3/(80β⁵), and a β-dependent two-valued region

Task `J:derive:the-neutral-moving-records-law-between-low-and-high-density:a2` · worker `w-jonathonsmac4f50-j1c03` ·
model `claude-opus-5-5` · checker `check.py` (exact; about 1 s).

**Provenance.**
- Block 153 harvests probe #9260 (`w-macbookpro9927a-ja869`), which is Claude Opus 5.5 on another machine.
- This attempt reuses #9260's low-density architecture: cluster decoupling, occupation domination and the path count.
- It sharpens the occupation bound, and supplies the proof for the sphere menu that #9260 only remarked on.
- Same family, so a referee from another family is needed.
- This machine's earlier related units (#8588 moving-clumping bounds, #8834 record-gas chessboard) are on different
  laws and questions.

## (1) Statement

**Setting.** Block 126 as landed:
- each site is empty (weight 1) or holds a content, with a priori weight z times the menu's measure;
- the bond kernel is 1 with an empty end, and c e^{βs·s′} between contents;
- the lattice is an even periodic cubic torus.

The sphere menu is S² with the uniform probability measure, at the neutral scale c₀ = β/sinh β. For the two-valued
menu, t = tanh β.

**(S) Sphere menu, part (2).** Let F₆(β) = (β/sinh β)⁶ · sinh(6β)/(6β). For every β > 0 and every z with

    z < z₀(β) := 1/(5 F₆(β)),

and on every even torus:
- Σ_x ⟨σ₀·σ_x⟩ ≤ p + 6p²/(1 − 5p), with p = z F₆(β), where σ_x = n_x s_x;
- hence M_L² → 0 and the structure factor is bounded uniformly in k and L;
- **cluster decoupling survives**;
- asymptotically z₀(β) = 3/(80β⁵)·(1 + o(1)) as β → ∞, and z₀ → 1/5 as β → 0.

**(T) Two-valued menu, part (1).** The same conclusion holds for z < 1/(5[(1+t)⁶ + (1−t)⁶]). This region contains
block 153's z < 1/320 for every β. It is larger by the factor 64/[(1+t)⁶+(1−t)⁶], which is 32 at β → 0, 2.1 at β = 1,
and tends to 1 at β → ∞.

## (2) Steps

1. **PROVED + CHECKED S1 (the sphere average).**
   - ⟨e^{βs·v}⟩_{S²} = ½∫₀^π e^{β|v|cos θ} sin θ dθ = sinh(β|v|)/(β|v|).
   - Hence c₀⟨e^{βs·s′}⟩ = 1: on average an occupied neighbour weighs as much as an empty one, which is what "neutral"
     means.
2. **PROVED (occupation bound).** Condition on every other site, and let the occupied neighbours of x carry contents
   s₁, …, s_m with m ≤ 6. Put v = Σs_j, so |v| ≤ m. Then
   - P(x occupied | rest) = zS/(1+zS), with S = c₀^m ⟨e^{βs·v}⟩ = c₀^m sinh(β|v|)/(β|v|);
   - sinh(y)/y is increasing, so S ≤ c₀^m sinh(mβ)/(mβ) =: F_m(β).
3. **PROVED + CHECKED S2 (F_m increases with m).**
   - f(y) = log(sinh y/y) has f(0+) = 0 and f″ = 1/y² − 1/sinh²y > 0, because sinh y − y has positive Taylor
     coefficients.
   - A convex f with f(0) = 0 is superadditive, so F_{m+1}/F_m = exp(f((m+1)β) − f(mβ) − f(β)) ≥ 1.
   - Therefore P(x occupied | rest) ≤ zF₆(β) =: p, uniformly in the conditioning.
4. **PROVED + CHECKED S4 (cluster decoupling).**
   - Condition on the occupied set O. The contents have law ∝ Π_{bonds in O} c₀ e^{βs·s′} Π dμ(s). No bond joins two
     different clusters of O; bonds to empty sites have weight 1.
   - The law is therefore invariant under a rotation R applied to every content of one cluster C.
   - For x ∈ C and y ∉ C, ⟨s_x·s_y | O⟩ = ⟨Rs_x·s_y | O⟩ for all R ∈ SO(3). Averaging over Haar measure, with
     ∫R dR = 0 (SO(3) acts irreducibly on R³), gives 0.
   - Hence |⟨σ₀·σ_x⟩| ≤ P(0 ↔ x in O).
5. **PROVED + CHECKED S5 (domination and paths; #9260's steps, restated at this scope).**
   - Sample the sites in any order. The conditional occupation probability given the history is the average of
     P(x occupied | rest), so it is ≤ p. A monotone coupling therefore puts O inside Bernoulli(p) site percolation.
   - An open path of n steps needs n+1 open sites, and there are at most 6·5^{n−1} self-avoiding paths.
   - So Σ_x P(0 ↔ x) ≤ p + 6p²/(1−5p) for p < 1/5.
6. **CHECKED S3 (asymptotics).**
   - F₆/β⁵ → 16/3, so z₀ ~ 3/(80β⁵). This confirms the supervisor's prior β⁻⁵ and gives the constant.
   - #9260's remark bound (βe^β/sinh β)⁶ is larger than F₆ by a factor tending to 12β.

   | β | z₀ (this attempt) | #9260's remark |
   |---:|---:|---:|
   | 1 | 0.0157 | 0.00131 |
   | 5 | 1.20·10⁻⁵ | 2.0·10⁻⁷ |
   | 20 | 1.17·10⁻⁸ | 4.9·10⁻¹¹ |

7. **PROVED + CHECKED T1–T2 (two-valued menu).** #9260's coefficient comparison (L1) gives
   P(x occupied | rest) ≤ z[(1+t)⁶ + (1−t)⁶] at each β. G(t) = (1+t)⁶ + (1−t)⁶ increases from 2 to 64 on [0,1]. Keeping
   the β-dependence, instead of using G ≤ 64, gives the stated region.

## (3) Where it stops

- **The window between low and high density.** The high-density side (block 153 T2: the pattern polynomial and the
  chessboard estimate) is not improved here.
- **At large β the low-density bound cannot improve by this method.** The worst case, six aligned occupied
  neighbours, is attained. Going further needs an exploration argument that uses the neutral average for unrevealed
  neighbours, or a better connectivity bound than 5ⁿ paths. The known connective constant of ℤ³ is about 4.68; a
  rigorous bound below 5 improves the 1/5 only slightly.
- **The torus separation lemma A2** (task item 3) is not attempted.

## (4) What would finish more

- A cluster exploration using conditional neutrality, which could replace F₆ by something closer to the average weight 1.
- Rigorous SAW counts for ℤ³.
- For the sphere at high density: an infrared bound, as in #9260's route list.

## ASSUMED

- The supplied law, the menus and the neutral scale (block 126 as landed; block 40's scale).
- Haar measure on SO(3), with ∫R dR = 0.

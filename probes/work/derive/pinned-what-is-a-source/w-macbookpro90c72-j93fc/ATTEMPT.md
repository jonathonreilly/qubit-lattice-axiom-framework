# What is a source, and what is its strength, when records move? (pinned scale, sphere menu)

Attempt 3 of 5. Worker `w-macbookpro90c72-j93fc`, model `claude-opus-5-5`. Script: `check.py` in this directory; it prints 9 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.**
- At claim time the tool printed the first sentence of attempt a5 (`w-jonathonsmac4f50-j7bb7`, claude-opus-5, issue #8586, not refereed). I formed my plan before opening a5's file, and read a5's `ATTEMPT.md` afterwards.
- The machinery here is mine: the sphere-menu formation factor, an exact Dirichlet-principle bound, the pocket enumeration, and the massless `Z³` Green function from Bessel integrals. a5 used a massive torus.
- Section 3 lists where a5 and I agree and where I sharpen it.
- a5 and I are in the same model family.
- None of my earlier units in this session overlaps this one.

**Sources.**
- Block 39 (PR #8530): moving records, the law with vacancies, and the formation rate (T4).
- Block 40 (PR #8546): the neutral scale, and the law on windows without a cycle (T2).
- Block 41 (PR #8547): the symmetry lemma (T4) and the transit Laplacian (T5).

## 1. Statement attempted

**Setting.** This is the sphere menu at the pinned scale.
- A site is empty or holds a record `s ∈ S²`. The contents carry the uniform probability measure `dΩ/4π`.
- A record weighs `z`. A bond between records weighs `W = c₀ e^{βs·s'}`, with `c₀ = β/sinh β`. A bond with an empty end weighs `1`.
- An empty site `x` forms a record at rate `zZ_x`, with `Z_x = ∫ dΩ/4π ∏_{y∼x occupied} W(s, s_y)` (block 39 T4). The void value is `1`.
- Transit is block 41's: symmetric transit exactly, and pair-weight transit in the dilute far field.
- The ordered medium's transverse (massless) field is block 41's declared quadratic stand-in, `θ`, with weight `exp(−(κ/2)Σ(θ_x − θ_y)²)` on `Z³`. It is massless, with `G` the Green function of `−Δ_lat`.

**Claims.**
- **(E) Exact, on small systems.**
  - The formation factor next to records with contents `s_1…s_k` is

        Z = c₀^k sinh(β|S|)/(β|S|),    S = Σ_j s_j.

  - Its mean over independent contents is `1` (the neutral scale).
  - For agreeing contents, `Z_k = c₀^k sinh(kβ)/(kβ)` is log-convex in `k`, with `Z₀ = Z₁ = 1` and `Z₂ = β coth β`. So `Z_k > 1` exactly when `k ≥ 2`.
  - An opposite pair gives `c₀² < 1`.
  - On a window without a cycle, the content field of a pinned record `a` at path distance `d` is exactly `(ρL)^d e(a)`, with `L = coth β − 1/β` and `ρ = z/(1+z)`. It decays exponentially.
- **(a) A pinned record on the cubic lattice, in the stand-in.** It is a Dirichlet condition: `θ(y) = θ₀G(y)/G(0)`. The far field is `θ₀/(4πG(0)|y|) ≈ 0.315θ₀/|y|`. The charge is signed: it is the pinned tilt.
- **(b) A jammed aligned cluster `S` of `N` records.**
  - *Unpinned, aligned with the order.* It puts nothing into the transverse channel, at every order.
  - *Pinned at `θ₀`.* The far field is `θ₀ Cap(S) G(r)`, with `Cap(S) ≤ 48R` for `S ⊂ [−R, R]³`. This bound is exact. It grows with the linear size, not with `N`. Executed: `Cap(cube L) ≈ 8.3L`, so the field goes as `N^{1/3}`.
  - *Production channel.* Held in empty surroundings, the cluster produces excess records only at empty sites touching two or more of its records:

        Q = z Σ_{x∉S} (Z_{k_x} − 1).

    For a box, `Q = 0` exactly. For a discrete ball of radius `R` there are about `5.5R²` such sites, so the field grows like the surface. In an ordered medium, at tree level, the excess per face site is `z(1−ρ)²D > 0`: again the surface.
- **(c) A density excess.** It puts nothing into the transverse channel, at every order. Its occupancy field is the pair correlation of block 41 T3: short range, and exactly zero on windows without a cycle.
- **(d) A region of faster formation.** It puts nothing into the transverse channel. Its transit halo `QG(r)/κ` (block 41 T5) is additive in `Q`. For a held lump, `Q` is set by agreement pockets, not by `N`.
- **Answer to the task.** No candidate gives a far field proportional to `N` for a compact source. Proportionality to `N` occurs only for dilute pinned records, each contributing `θ₀/G(0)` (signed), and for internal pockets of a porous lump while they fill, which is transient. The coefficients in `β`, `ρ` and `c₀` are those in (E), (b) and P3.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — PROVED and CHECKED [E1].** `∫_0^π e^{βcos θ} sin θ dθ/2 = sinh β/β`, via the antiderivative `−e^{βcos θ}/β`. So `c₀ = β/sinh β` is the unique scale at which `∫dΩ/4π W(s, s') = 1`.

**S2 — PROVED and CHECKED [E2].**
- *The formula.* `∫dΩ/4π e^{βs·S}` depends only on `|S|`. Rotating `S` to the pole gives `sinh(β|S|)/(β|S|)`, which is S1 with `β → β|S|`. Multiplying by `c₀^k` gives `Z`.
- *The neutral mean.* By Fubini, averaging each neighbour's content first gives `∫dΩ_j/4π c₀ e^{βs·s_j} = 1` for every `s`. So `E[Z] = 1` for every `k`.
- *Log-convexity.* Let `φ(x) = log(sinh x/x)`. Then `φ'' = 1/x² − 1/sinh² x > 0`. So `a_k := log Z_k = k log c₀ + φ(kβ)` is strictly convex in `k`, with `a₀ = 0` and `a₁ = log c₀ + φ(β) = 0`. Hence `a_k > 0` and `a_k` increases for `k ≥ 2`.
- *Opposite pair.* `S = 0`, so `Z = c₀²`.
- *Values at `β = 2`.* `Z_2 … Z_6 = 2.075, 5.637, 17.228, 56.158, 190.685`.

**S3 — PROVED and CHECKED [E3].**
- *Occupancies.* On a window without a cycle, integrate the contents of each maximal occupied run from a leaf inward; each bond contributes `∫dΩ/4π c₀e^{βs·s'} = 1`, and this still holds when one site of the run is pinned. The occupancy law is therefore `∏ z^{n_x}`: independent, with density `z/(1+z)`.
- *One step.* `∫dΩ/4π c₀ e^{βa·s} s = L(β)a`. The `a`-component is `coth β − 1/β` (sympy), and the transverse components vanish by the azimuthal integral.
- *Along a path.* If all intermediate sites are occupied, the Markov property gives `E[e(s_d)] = L^d e(a)`. If any intermediate site is empty, the far content is independent of `a` and has mean zero. So `⟨n_d e(s_d) | s_0 = a⟩ = ρ^d L^d e(a)`.
- *Values at `β = 2`, `ρ = ½`.* `0.2687, 0.0722, 0.0194, 0.0052`.

**S4 — PROVED. Symmetry: (b) unpinned, (c) and (d).** This is block 41 T4's lemma, restated for a medium ordered along `n`. Fix the order by any condition invariant under rotations about `n` (boundary contents along `n`, or a vanishing field along `n`). Take a perturbation invariant under those rotations: extra or held records with contents along `n`, a changed fugacity or formation rate, or held records of unread content. Then the law is invariant under them. The transverse part of `⟨n_y e(s_y)⟩` is a vector in the plane `⊥ n` that is fixed by every rotation of that plane, so it vanishes. This holds exactly, at every order.

**S5 — ASSUMED.** The ordered sphere medium's transverse field is block 41's quadratic stand-in on `Z³`, which is massless. This is the model block 41 declares; it is not derived from the moving-records law.

**S6 — PROVED. Pinned set = Dirichlet condition.** For the massless Gaussian field `θ` on `Z³` (mean zero at infinity), the conditional mean given `θ = θ₀` on a finite set `S` is `θ₀h_S`, where

    h_S = Σ_{x∈S} q_x G(· − x),    q = G_S^{-1} 1.

`h_S` is harmonic off `S`, equals `1` on `S`, and tends to `0` at infinity; this is Gaussian conditioning. As `r → ∞`, `h_S(y) = Cap(S) G(y) + O(|y|^{-2})`, with `Cap(S) = Σ q_x`. For one site, `Cap = 1/G(0)`, and `G(0) = 0.2527310099` [C3].

**S7 — PROVED. The Dirichlet principle, at this scope.** Let `E(f) = Σ_edges (f_x − f_y)²`.
1. **The equilibrium potential attains `Cap(S)`.** Summation by parts gives `E(h_S) = Σ_x h_S(x)(−Δh_S)(x) = Σ_{x∈S} q_x = Cap(S)`. The boundary term on a sphere of radius `r` is `O(r²·r^{-1}·r^{-2}) → 0`.
2. **Every admissible `f` does at least as well.** Take `f` with `f = 1` on `S`, `f = O(1/r)` and `∇f = O(1/r²)`. Then `E(f) = E(h_S) + E(f − h_S)`. The cross term is `2Σ_x (−Δh_S)(f − h_S) = 2Σ_{x∈S} q_x·0 = 0`, again with a vanishing boundary term. So `Cap(S) = min E ≤ E(f)`.
3. **Monotonicity.** For `S ⊂ B`, any `f` admissible for `B` is admissible for `S`, so `Cap(S) ≤ Cap(B)`.

**S8 — CHECKED [C1, C2]. `Cap(S) ≤ 48R` for `S ⊂ [−R, R]³`.** Take `f_R = min(1, R/‖x‖_∞)`. It is admissible, and it is constant on each sup-norm shell.
- An edge changes `‖x‖_∞` by at most one. The edges leaving `[−m, m]³` number `6(2m+1)²` (enumerated for `m ≤ 6`, and each crosses exactly one face plane).
- Then

      E(f_R) = Σ_{m≥R} 6(2m+1)² R² (1/m − 1/(m+1))² = 6R² Σ_{m≥R} (1/m + 1/(m+1))²
             ≤ 6R²·4(1/R² + 1/R) = 24 + 24R ≤ 48R.

- Exact Fractions with a tail bound give `E(f_R)/R = 25.7, 24.5, …, 24.0` for `R = 1…8`.
- So a pinned compact cluster of `N ≈ (2R)³` records has far field at most `θ₀·48R·G(r)`, which is `O(N^{1/3})`, not `∝ N`.

**S9 — executed [C3]. Massless `Z³` capacities.**
- `G(x) = ∫_0^∞ ∏_i e^{-2t}I_{x_i}(2t) dt`. It checks `G(1) = G(0) − 1/6` to `1e-12`.
- *Cubes.* `Cap/L = 3.96, 5.55, 6.31, 6.74, 7.02, 7.21, 7.35, 7.46` for `L = 1…8`. The increments rise to `8.22`, approaching `4π × 0.6607 = 8.30` (the continuum cube capacitance, quoted as a comparator). `Cap/(N/G(0)) = 0.029` at `L = 8`.
- *Lines.* `Cap/L = 2.95, 2.31, 1.87, 1.56, 1.33` for `L = 2…32`, falling like `1/log L`.
- *Pairs.* At `d = 1, 2, 4, 8, 16`, `Cap/(2/G(0)) = 0.746, 0.855, 0.926, 0.962, 0.981`. Pinned records add only when dilute.
- Every value lies below the S8 bound.

**S10 — PROVED and CHECKED [P1]. Boxes have no pockets.**
- *Argument.* Let `x ∉ B` touch `x + σe_i ∈ B` and `x + τe_j ∈ B`. If `i = j`, then `x` lies between two points of `B` on one axis, so `x ∈ B`. If `i ≠ j`, every coordinate of `x` equals a coordinate of one of these two points of `B`, so `x ∈ B`. Both contradict `x ∉ B`.
- *Consequence.* Around an aligned box held in empty surroundings, every empty site has `k ≤ 1`, so `Z = 1` and the excess `Q` is zero.
- *Check.* All 216 boxes with sides `≤ 6`.

**S11 — CHECKED [P2]. Balls.** Discrete balls `|x|² ≤ R²` for `R² ≤ 144` have outside sites with `k = 2` or `3` only.
- The counts `(P₂, P₃)` are: `R² = 4`: `(24, 0)`; `R² = 25`: `(84, 56)`; `R² = 64`: `(228, 120)`; `R² = 144`: `(528, 272)`.
- `(P₂ + P₃)/R² ∈ [3.56, 6.00]`, which is surface scaling, and `(P₂ + P₃)/N` falls to `0.112`.
- So `Q(ball) = z[P₂(β coth β − 1) + P₃(Z₃ − 1)] = O(N^{2/3})`.

**S12 — PROVED. Excess production of a held lump in empty surroundings.** This is the instantaneous rate: every empty site `x` next to `S` forms at `zZ_{k_x}` instead of `z`, and every other empty site forms at `z`. So `Q = z Σ(Z_{k_x} − 1)`, and S10–S11 evaluate it.

**S13 — ASSUMED, then CHECKED [P3]. Tree level, ordered medium.**
- *Assumed.* Perfect alignment, and independent occupancies at density `ρ` around each empty site (the star of an empty site is cycle-free). Plaquette factors, which are large in the ordered phase (block 40 T3), are neglected.
- *Computed.* An empty face site has `1 + B₅` aligned occupied neighbours, against `B₆` in the bulk, where `B_m ~ Bin(m, ρ)`. Its excess is `z(1−ρ)²D`, with

      D = E[Z(1+B₅) − Z(B₅)] = 5ρ(β coth β − 1) + O(ρ²) > 0

  (sympy series; `D > 0` on a grid of `β` and `ρ`).
- *Consequence.* A box's halo in the ordered medium grows like its surface.

**S14 — cited.** Under symmetric transit, `d⟨n⟩/dt = κΔ⟨n⟩ + j`, and a steady excess `Q` gives the halo `QG(r)/κ` (block 41 T5; records are permanent, block 39, so the halo is unscreened).

**S15 — PROVED, from S4 and S6–S14. The conclusion.** The transverse channel carries either nothing (S4) or a capacity bounded by linear size (S8). The production channel carries agreement pockets (S10–S12) or, at tree level, a surface (S13). So no compact source of `N` records has a far field proportional to `N`. Dilute pinned records add, with signed charges `θ₀/G(0)` (S6, S9).

## 3. Agreement with a5, and where this differs

**Agreed:**
- (a) is a Dirichlet condition;
- (b) is not additive;
- (c) does not source the transverse mode;
- (d) is additive in `Q`.

**Differences and additions:**
- **The massless limit.** a5's numbers use `m² = ½` on a torus of side 7. Here the Green function is the massless one on `Z³`, and there is an exact upper bound: `Cap ≤ 48R` (S8), which a5 lists as open.
- **(c) at every order.** a5 stated (c) at linear order; S4 gives it at every order, for every rotation-invariant candidate.
- **(d) as a statement about lumps.** a5 says the halo is additive in `Q`. S10–S13 say what `Q` is for a lump at the pinned scale: zero for a box in empty surroundings, pockets `∝ R²` for a ball, and the surface in an ordered medium at tree level. So a lump's halo is not `∝ N` either.
- **The exact formation factor for the sphere menu** (S2) is new here. Block 41 T5 gave the six-axis version.

## 4. Where the route stops, and what would finish it

**Where it stops:**
- The transverse results rest on the quadratic stand-in (S5).
- The content amplitude `⟨s_⊥⟩ = Mθ` needs the medium's order parameter `M(β, ρ)`, which is not derived here. The sibling problem `pinned-sphere-order-and-stiffness` is where it lives.
- The ordered-medium production (S13) is tree level; the loop factors are not controlled.

**What would finish it:**
1. A lower bound `Cap(cube L) ≥ cL`, which would make the `N^{1/3}` law two-sided and exact. A route: `Cap(S) ≥ N²/(1ᵀG_S1)` together with `G(x) ≤ C/|x|`.
2. `M(β, ρ)` and the stiffness at `c₀`.
3. Production beyond tree level in the ordered medium.
4. A candidate that every record carries as a scalar, coupled linearly to a massless field. Within these channels none exists. The transverse charge is the content vector, which is signed, and the production is set by agreement, which is local to surfaces and pockets.

# Can the actual empty-start formation law prepare an inhomogeneous colour profile?

- **Task:** `J:derive:mobile-record-geometric-formation-waves:a1`
- **Worker:** `w-jonathonsmac4f50-jccaf`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The sources are Codex drafts, so this is a cross-family reading. The recovered fixed-rate formation statistics come from a Codex production run. They are used only as context and are not replayed here; the `C:recovered-fixed-rate-geometric-formation` tasks own that replay.
- **Prior attempts.** None existed on `ai/probes` at claim time.

## Sources

All sources were recovered at their frozen heads, and each SHA256 matches `SOURCE_MAP.json`. `origin/main` is `e37967e326`.

| PR | frozen head | note (SHA256) | runner (SHA256) |
|---|---|---|---|
| #8589 | `97c1522d46` | `…GEOMETRIC_FORMATION_SELECTION_AND_CLOCK…` `2f87af23…70206` | `939cd94b…0181b` |
| #8594 | `d0dec3ccac` | `…ALL_STAGE_FORMATION_CLOCK…` `e45dbe02…55ef6` | `0dae7189…eba1b` |
| #8600 | `3c6fea4be3` | `…MOVING_GEOMETRY_COLOR_WAVES…` `03b4434a…1f747` | `2d4cdcd4…fcf7e` |
| #8604 | `af45e32418` | `…EMPTY_START_QUANTITATIVE_WAVES…` `39a13571…a0b4e` | `5756e8d7…ecf839` |
| #8610 | `05ce3bed24` | `…SMOOTH_NONLINEAR_EULER…` `b0b1a4d5…aceb` | `5a496013…a87be7` |

**Read in full:** #8610 and #8604.

**Read for the definitions used here:**
- #8589: contents, birth density and slides.
- #8600, §1 and §7: the fourteen colours, and the birth law (19)–(20). The colour's conditional probability is `p_a`, "independent of delta and of all prior history".

**Not reconstructed:**
- #8594's all-stage injection and the empty-corridor comparison (used by #8604 §4). They are screened numerically below.
- The imported Jerrum–Sinclair and Taggi theorems.

## (1) Statements attempted

- **Target** (#8610 IV (1)). A preparation `μ_N(0)` of the joint geometry/colour process with `h_N(0) = H(μ_N(0) | ν_N^p(0)) = o(K)`, where:
  - `ν_N^p` means: draw the geometry from the actual marginal `ρ_N`, then independent colours with probabilities `p(0, u/N)` at the black sites;
  - `p` is a nontrivial (nonconstant) smooth interior profile.
- **Theorem O** (answers the research target: no).
  - The actual empty-start law is invariant under the even translations of the torus.
  - For every profile `p` and every law `μ` invariant in this way, with only full states and common one-site colour marginal `q`:

        H(μ | ρ × ⊗_u p(u/N))  ≥  Σ_u KL(q ‖ p(u/N))  ≥  (1/2) Σ_u |p(u/N) − p̄_N|²,

    where `p̄_N = K⁻¹ Σ_u p(u/N)`. This is `Θ(K)` for every nonconstant continuous `p`.
  - At every deterministic time the entropy is `+∞`.
  - No invariant law lies within total variation `< 1/2` of laws with `o(K)` entropy relative to a nonconstant profile.
  - So the empty-start → #8604 → #8610 chain reaches only the constant solution.
- **Lemma P** (a named proposed preparation, conditional).
  - Take position-dependent birth colours `p₀(x/N)`, and switch colour exchanges on at the first full time `F`.
  - Then `h(F) ≤ (Λ²/ε) N⁻² E Σ_u |β_u − u|²`, where:
    - `β_u` is the black birth site of the pair that ends at `u`;
    - `ε = min p₀`;
    - `Λ` is the Lipschitz constant of `p₀`.
  - The missing input is a displacement bound.
- **Inventory.** The conditional lemmas of #8604 Part I and Part III that survive this reading, with the finite checks run on them.

## (2) Steps

### Step 1 — the process is translation covariant (PROVED)

*The process* (#8589, #8600 §7, #8604 III), on the even `N`-torus:
- **Births.** At rate `β` on each vacant edge. The content density is `g0(n)[1 + ε n·δ]`. The colour `χ(n)` has conditional probability `p_a`, the same at every edge and in every history.
- **Slides.** At rate `κ` on each ordered path `(v0, v1, v2)` with `v2` vacant.
- **Routed pair exchanges.** At rates `k0/2 + h/4`. These use the four-context formula when all contexts exist, and `k0/2` otherwise.
- **Plaquette rotations.** At rate `ν` on full states.
- **Start.** Empty.

*Symmetry.* Every rate is a function of the configuration that commutes with lattice translations. The rates read only relative positions, local occupancies, colours and the direction vectors `δ`.

*Markov projection.* The colour/geometry projection, over partial and full states, is a finite Markov chain. The fine contents enter no rate:
- the birth colour law does not depend on `δ`;
- slides and exchanges do not read `n`.

*Invariance.*
- An even translation `τ` (`τ₁ + τ₂ + τ₃` even, so the parity of every site is preserved) acts on this finite state space. It commutes with the generator `L`, and the empty initial state is fixed.
- Hence `e^{tL}` preserves invariance, and the law at every deterministic time `t` is invariant.
- The first full time `F` is a translation-invariant functional of the path, so the law of `X_F` is invariant too.
- Even translations act transitively on the black sites. So every black site has the same one-site colour marginal `q`.

### Step 2 — the entropy lower bound (PROVED; ingredients CHECKED O1, O2, O5)

Let `μ` be an invariant law on full states, `ρ` its geometry marginal, and `P = ⊗_u p(u/N)`. Then:

- **(a) Data processing.** `H(μ | ρ × P) ≥ H(μ_col | P)`, because the colour marginal of `ρ × P` is `P`. This is the log-sum inequality on the fibres of the projection.
- **(b) Chain rule.** `H(μ_col | P) = H(μ_col | ⊗_u μ_u) + Σ_u KL(μ_u ‖ p(u/N)) ≥ Σ_u KL(q ‖ p(u/N))`. This is an exact identity on a finite space (O2 checks it symbolically).
- **(c) Pinsker.** `KL(q ‖ p) ≥ (1/2)|q − p|₁² ≥ (1/2)|q − p|₂²`.
  - With `A = {a : q_a > p_a}`, the log-sum inequality gives `KL(q ‖ p) ≥ KL((q(A), 1 − q(A)) ‖ (p(A), 1 − p(A)))`.
  - For the binary divergence, `g(r) = KL((s, 1−s) ‖ (r, 1−r)) − 2(s − r)²` has `g(s) = 0` and `g'(r) = (r − s)(1 − 2r)²/(r(1 − r))`, so `g ≥ 0` (O1).
  - Finally `2(q(A) − p(A))² = (1/2)|q − p|₁²`.
- **(d) The mean minimises.** `Σ_u |q − p_u|² ≥ Σ_u |p̄_N − p_u|²` for every `q`.

*Conclusion.* `h ≥ (1/2) Σ_u |p(u/N) − p̄_N|²`. For continuous `p`, `K⁻¹ ×` this sum tends to `∫|p − ∫p|²`, which is positive unless `p` is constant.

*Exact example (O6).*
- Take 14 colours, `p̄ = 1/14`, `v = e_{A,+1} − e_{A,−1}`, and `p(x) = p̄ + (1/28) v cos 2πx₁`.
- It is strictly positive, and `p̄_N = p̄` exactly.
- `h/K ≥ 1/1568` at every even `N ≥ 4`, for every invariant law, at every time.

### Step 3 — deterministic times give infinite entropy (PROVED)

- At any `t < ∞`, `P(empty at t) ≥ e^{−β m t} > 0`, with `m = 6K` edges. So the actual law charges states with vacancies.
- `ν_N^p` puts a colour at every black site, which is its full-state support. So `μ_N(t) ⊀ ν_N^p(t)`, and `h_N(t) = +∞`.
- This holds even for constant `p`. So #8604 III's deterministic-time conclusion, which is total variation `≤ η`, never meets #8610's hypothesis directly. It meets it only through #8604 III's reference process (Step 5).

### Step 4 — total-variation version (PROVED; ingredients CHECKED O3, O4)

*Claim.* Suppose `μ_N` are invariant, `ν_N` satisfy `H(ν_N | ρ'_N × ⊗p(u/N)) = o(K)` for a continuous `p`, and `limsup TV(μ_N, ν_N) < 1/2`. Then `p` is constant.

*Proof.*
- Fix a continuous `φ` with `|φ| ≤ B`, a colour `a`, and `Z_φ = K⁻¹ Σ_u φ(u/N) I_{u,a}`.
- **Concentration under the product law.** Hoeffding's lemma (O4: `ψ'' = q(1 − q) ≤ 1/4`) gives `P(|Z_φ − E Z_φ| ≥ δ) ≤ 2e^{−2Kδ²/B²}`.
- **Transfer to `ν_N`.** The Gibbs identity (O3) gives `ν(A) ≤ (H + log 2)/log(1/P(A))`. So `ν_N(|Z_φ − c_φ| ≥ 2δ) → 0`, with `c_φ = ∫φ p_a`, using the black-site Riemann sum.
- **Transfer to `μ_N`.** For large `N`, `μ_N(|Z_φ − c_φ| < 2δ) > 1/2`. The same holds for every translate `φ_s = φ(· + s)`, uniformly in `s`.
- **Use invariance.** Invariance gives `μ_N(|Z_{φ_{s_N}} − c_φ| < 2δ) > 1/2` for an even `τ_N` with `s_N = τ_N/N → s`.
- **Intersect.** Two events of probability `> 1/2` intersect, so `|c_φ − c_{φ_{s_N}}| < 4δ`.
- Letting `δ → 0` gives `∫φ(x)p_a(x) dx = ∫φ(x)p_a(x − s) dx` for all `φ` and all `s`. So `p` is constant. ∎

### Step 5 — consequence for the chain (PROVED from Steps 1–4 and #8604 III as read)

- #8604 III couples the actual state at `t_N` to a reference with an allowed geometry and iid colours `p^K`. The reference has `h = 0` exactly relative to its own geometry marginal.
- #8610 IV applied to the reference, followed by the `η`-coupling for bounded empirical observables, gives the Euler conclusion for the actual process, but only for the constant solution `p(t, x) ≡ p`. That conclusion is a law of large numbers with no wave content.
- By Step 4, no route through total variation can produce a nonconstant `p` from the actual law.
- Any inhomogeneity must be supplied as a symmetry-breaking ingredient: an inhomogeneous birth law, initial state or field. #8610 already says the inhomogeneous preparation "is supplied". Theorem O shows that the actual law cannot replace that supply.

### Step 6 — a named proposed preparation (Lemma P PROVED conditionally; first unresolved step named)

*The preparation `P_inh`.*
- #8600 (19) is changed only in its reference density: `g0_x` with colour masses `p₀(x/N)` at the black endpoint `x` of the birth edge, and `∫_{colour a} n g0_x dμ = 0`. So the colour's law given `δ` is still `p₀(x/N)`.
- Geometry: births and slides as before.
- No colour exchange and no plaquette motion before the first full time `F`. From `F` on, the full-state process of #8610 IV runs.
- The switch at `F` is a supplied global rule. #8600 deliberately avoids such switches.

*Lemma P.*
- The geometry is autonomous, and the colour draws enter no geometric rate. So, given the geometric history `𝒢`, the colours at `F` are independent, with the pair at black anchor `u` distributed as `p₀(β_u/N)`.
- Joint convexity of KL (averaging over `𝒢` given the final matching) gives `h(F) ≤ E Σ_u KL(p₀(β_u/N) ‖ p₀(u/N))`.
- KL is at most χ² (O5, with `log z ≤ z − 1`), and `χ² ≤ |Δp|²/ε`. So `h(F) ≤ (Λ²/(εN²)) E Σ_u |β_u − u|²`, with torus distance.
- Hence `h(F) = o(K)` if the mean squared birth-to-final displacement per pair is `o(N²)`.
- #8610 IV then applies from the stopping time `F`, by the strong Markov property. Its initial geometry law may be arbitrary.

*First unresolved step.* Prove `E Σ_u |β_u − u|² = o(N²K)` for the fixed-rate geometric birth/slide process.
- The recovered Codex statistics (`N = 16…128`, `κ = 1`, `β = 0.1, 1, 10`) show accepted slides per site growing slowly: 54, 68, 82, 96 at `β = 0.1`.
- That is consistent with an `O(K log N)` displacement sum, but it is not a proof and was not replayed here.

*Always-on exchange variant (the actual #8600 dynamics with position-dependent births).*
- The same statistics show mean filling time per site roughly constant in `N` (≈ 0.94, 0.12, 0.036 at `N = 128`). So formation lasts about `N²` Euler times.
- An always-on preparation would evolve under partial-matching exchanges for a divergent Euler time before `F`.
- This is recorded as an unproved obstruction to that variant. A proof would need a lower bound on `F` and a relaxation statement.

### Step 7 — inventory of the input chain

| Lemma (source) | Reading here | Finite check | Disposition |
|---|---|---|---|
| #8604 I §2 padded fibres and `R̂` | proof read; each fibre count re-derived | F1: exact counts, every class and rank, `R̂` formula, `R̂ ≤ U_j`, 10 (graph, stage) cases on `C6`, 2×3, 2×4, `Q3` | survives |
| #8604 I §3 comparison (6)–(8) | proof read (extension `F`, fibre masses, boundary energy via the complete-graph identity) | C1: (6) and (7) exact with random integer `g` on the same 10 cases; S2: (8) screened | survives (exact on small cases) |
| #8604 I §4 physical slides `gap(S_j) ≥ gap(B_j)/C_j` | imported from #8594; not reconstructed | S3: screened, and every slide layer connected | survives the screen; proof not re-read |
| Jerrum–Sinclair bound (4) | imported; hypotheses and normalization not re-derived | S1: screened (margins of 10⁶ or more on these graphs) | ASSUMED (import) |
| Taggi `R ≤ K²/6`; `p_j ≥ 6/K` | imported; not checked (cubic torus with `N ≥ 8` is out of reach) | none | ASSUMED (import) |
| #8604 I §5 killed-chain (9)–(10) | proof read (`p\|c\|² ≤ 2π(h\|f\|²) + 2m‖v‖²`; survival `≤ √n e^{−λt}`) | S4: screened at `β = 0.01, 1, 100` | survives |
| #8604 III deterministic-time coupling | proof read; valid as a total-variation statement (multinomial counts independent of the autonomous geometry; uniform-in-arrangement contraction) | — | survives; feeds #8610 only through the reference process (Step 3) |
| #8610 IV nonlinear Euler | only its hypothesis used | — | not reviewed here |

## (3) Where it stops

- Theorem O and Lemma P are complete as stated.
- The research target's positive side is open. What is missing is a local preparation that breaks translation symmetry with an entropy estimate of `o(K)`.
- The first unresolved step is the displacement bound in Step 6. The always-on variant stays open in both directions.
- The imports marked ASSUMED in Step 7 are not verified here.

## (4) What would finish it

- **(i)** A displacement estimate `E Σ_u |β_u − u|² = o(N²K)` for the fixed-rate geometric process. For example, `O(K log N)` from a bound on the hole-walk end game. With Lemma P this gives an explicit preparation with `h(F) = O(K log N/N²)`.
- **(ii)** A local replacement for the global switch at `F`. For example, an exchange rate that vanishes while vacancies are near and is bounded below on full neighbourhoods. The entropy route would then need re-checking.
- **(iii)** Independent reconstruction of #8594's empty-corridor comparison and of the imports, before the #8604 exponents are reused.

## ASSUMED

- The supplied model of #8589, #8600 and #8604: contents, colour map, rates, recognition and clock.
- The imports listed in Step 7.
- The Euler theorem of #8610 IV is used only as the consumer of `h_N(0)`.

Every other ingredient is re-proved above: data processing, the chain rule, Pinsker, Hoeffding's lemma, the Gibbs/entropy inequality, `KL ≤ χ²` and joint convexity.

## Reproduce

```bash
python3 probes/work/derive/mobile-record-geometric-formation-waves/w-jonathonsmac4f50-jccaf/check.py
```

The run takes about 1 s.

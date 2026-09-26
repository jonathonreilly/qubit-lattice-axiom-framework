# Local RK preparation: the attraction theorem reconstructed, and the ramp gap certified independently

- **Task:** `J:derive:deferred-20260926-local-rk-preparation:a1`
- **Worker:** `w-jonathonsmac4f50-j7dec`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The sources are Codex campaign12h_third files. This is a cross-family reading; Codex's own separate-context checks were same-family.
- **Prior attempts.** None existed on `ai/probes` for this problem at claim time. The related tasks (formation-packets, ring-limits) cover other obligations.

## Sources

**Packet:** `probes/work/deferred-science-20260926/mobile-record-formation-20260920/campaign12h_third/`.

| file | SHA256 |
|---|---|
| `LOCAL_GAUGE_RECORD_COOLING_TO_RK_STATES.md` | `7fa8e6b7…2791f` |
| `COHERENT_PREPARATION_AFTER_LOCAL_RECORD_COOLING.md` | `a45a2a3f…2b688` |
| `APPROACH_REGISTRY.md` | `3a6536bc…83ec` |
| `coherent_cubic_ground_ramp_check.py` | `bcb3f21c…07421` |
| `COHERENT_CUBIC_GROUND_RAMP_RESULTS.json` | `5d5711d1…662af` |

- **Other notes read.** The adaptation, finite-cubic and weighted notes were read for scope. The adaptation packet's `correction_ack` (the "δ ≠ 0 scope" prose repair) concerns that note only. It changes nothing here.
- **Reading rule.** The author's runner was consulted only for the seed convention (E = +1/2 on links whose base vertex has even transverse coordinate sum). Its certificate method was not reused.

## (1) Statements

**(a) The attraction theorem** (note §2), reconstructed at its stated premises.

*Premises.*
- `C` is a finite connected component of a plaquette-flip graph.
- For each plaquette `p`, every flippable pair `a → b` changes the link field by one fixed nonzero vector `z_p`.
- The pairs of one plaquette are disjoint.
- `L_p = Σ |s_ab⟩⟨d_ab|`.
- The generator is `G(ρ) = −i[H, ρ] + Σ_p γ_p D[L_p](ρ)`, with `H = Σ h_p P_p^−`, `γ_p > 0` and `h_p` real of any sign.

*Conclusion.* Every density matrix on `span(C)` converges exponentially to `|u⟩⟨u|`, where `u` is the uniform vector.

**(b) Registry obligation: the coherent ramp's certified gap.**
- The ramp is `H(δ) = J(D − A) − δD`, `J = 1`, `0 ≤ δ ≤ 1`, on the actual periodic `2×2×2` zero-flux component with 864 states.
- Its ground gap is at least `15120817128881/25429309500000 > 0.594622` along the whole ramp.
- This is an independent certificate. It confirms, and tightens, the note's bound `g ≥ 0.3821097`.

## (2) Steps

### Step 1 — the attraction theorem (PROVED; each step re-derived)

**(i) The loss operator.**
- With `K = Σγ_p P_p^−` and `R = K/2 + iH`, the generator is `G(ρ) = −Rρ − ρR† + Σγ_p L_pρL_p†`.
- `⟨v, Kv⟩ = ½ Σ_p γ_p Σ_pairs |v_a − v_b|²` vanishes only on constants, because `C` is connected. So `K > 0` on `u^⊥`.
- `Ru = R†u = 0` and `L_p u = 0`.

**(ii) The separating identity.**
- Take `F` diagonal with distinct values and `F(b) − F(a) = Δ_p` on every `p`-pair. This is where the fixed displacement is used.
- Let `v(t) = e^{tF}u`. On each pair, `⟨d|v⟩ = −tanh(tΔ/2)⟨s|v⟩`, so `P_p^−v = −tanh(tΔ_p/2) L_p†v` (A1, symbolic).
- The note's `F = Σ_l 3^l E_l` is one valid choice, since distinct link strings give distinct base-3 values. Only distinctness and constant `Δ_p` are used.

**(iii) No invariant subspace orthogonal to the target.**
- Suppose `W ⊂ u^⊥` is invariant under `R` and every `L_p`. Taking adjoints of `RP_W = P_W R P_W` gives `P_W R† = R_W† P_W`, and likewise for each `L_p`.
- Since `R† = Σ(γ_p/2 − ih_p)P_p^−`, (ii) gives `[R_W† + Σ(γ_p/2 − ih_p) tanh(tΔ_p/2) L_{p,W}†] P_W v(t) = 0`.
- At `t = 0` the bracket is `R_W†`, whose Hermitian part `P_W K P_W/2` is positive definite. So the bracket is invertible near `t = 0`.
- Hence the entire function `P_W e^{tF}u` vanishes on an interval, so `P_W F^n u = 0` for all `n`.
- The vectors `u, Fu, …, F^{D−1}u` span the space (Vandermonde: distinct eigenvalues, and `u` has every component nonzero). So `W = 0`.

**(iv) The semigroup step.**
- `R` is block-diagonal with respect to `P0 = |u⟩⟨u|` and `Q = 1 − P0`, and `L_p = [[0, a_p], [0, B_p]]`. So `σ = QρQ` evolves autonomously, with `d Tr σ/dt = −Σγ_p Tr(a_pσa_p†)`.
- Suppose the trace does not tend to 0. Cesàro averages then give a stationary `σ* ≥ 0` with trace `c > 0`.
- Zero leakage gives `a_p|_{range σ*} = 0`.
- The diagonal stationary equation, paired with any `x ⊥ range σ*`, gives `B_p range σ* ⊂ range σ*`.
- The off-block equation gives `R_Q range σ* ⊂ range σ*`, since `σ*` is invertible on its range.
- So `range σ*` would be a forbidden `W`. Hence `e^{tA} → 0` on the positive cone, hence everywhere, and the spectrum has negative real part.
- Finally `‖ρ(t) − P0‖₁ ≤ 2√Tr(Qρ(t))`.

**(v) Finite expected record output.** `E N_jump = ∫ Tr(Kρ(t)) dt < ∞`, because `KP0 = 0` and `Tr(Qρ)` decays exponentially.

**No defect found.** The fixed-displacement premise is load-bearing (A2).

### Step 2 — premises and controls on actual geometries (CHECKED G1, G2, A2, A3)

- **G1.** The note's seed generates, by plaquette flips, a component of exactly 864 states:
  - 24 links, 24 plaquettes, degrees 4 to 16;
  - Gauss charge 0 at every site and flux `(0,0,0)`;
  - closed under all eight translations.
- **G2.** Every clockwise → counterclockwise pair of plaquette `p` changes `2E` by `(2, 2, −2, −2)` on its four links and nothing else. So the displacement is fixed. The pairs of one plaquette are disjoint, 144 per plaquette.
- **A2** (the bad-orientation countercontrol). Take a 4-cycle with `L1` on `(0→1), (2→3)` and `L2` on `(1→2), (3→0)`.
  - The common dark kernel is the uniform vector.
  - The exact stationary space is two-dimensional. It contains a density orthogonal to `u` with purity exactly `1/2`.
  - So connectivity alone does not force attraction.
- **A3.** On an open cube, across all Gauss sectors, the largest flip component has 9 states. With `γ_p = p + 1` and signed `h_p = (−1)^p(p + 2)`, the exact Liouvillian has nullity one, spanned by `|u⟩⟨u|`. The rank is computed over ℚ from the real 162×162 block form.

### Step 3 — the ramp gap (PROVED; CHECKED C1–C3)

**The method** (disjoint from the author's rounded-eigenbasis and Weyl-residual certificate).
- The ramp commutes with the translations `Z₂³`, which preserve the component. Symmetrised orbit vectors split `H` into 8 character sectors, of dimensions 133, 107 (×3), 103 (×3) and 101, summing to 864.
- In each sector `B'x = λG'x`, with integer `B' = 16H(j/16)` blocks and diagonal positive `G'` (stabiliser sizes).
- By Sylvester's law, the number of eigenvalues below `τ` is the number of negative pivots of an exact rational `LDLᵀ` of `B' − 16τG'`, when all pivots are nonzero.
- At each grid point `δ = j/16` choose rationals `τ_B < τ_A`:
  - the trivial sector has exactly one eigenvalue below `τ_B` and exactly one below `τ_A`;
  - every other sector is positive definite at `τ_A` or at its own lower threshold.
- Then `gap(j/16) ≥ τ_A − τ_B` exactly (C1).

**Grid gaps.** They are 0.96962 (at `δ = 0`), then 1.04579, 1.12216, …, 2.23487, 2.22578 (at `δ = 1`). They agree with the author's floating gaps to 10⁻⁶.

**Covering the whole ramp** (C2).
- `H(δ) + 10δ = J(D − A) − δ(D − 10)`, and `‖D − 10‖ = 6`, since degrees run from 4 to 16. So every ordered eigenvalue is 6-Lipschitz and the gap is 12-Lipschitz.
- Every `δ` is within 1/32 of a grid point. So the whole-ramp gap is at least `0.96962 − 6/16 = 0.594622`.

**Comparison with the author.** The author's grid bounds were weakened by residual terms of 2η ≈ 0.07 to 0.29 (0.757 at `δ = 0`), giving 0.38211 overall.

**Endpoint** (C3, float). The ground energy at `δ = 1` is `−9.026720913531`, as in the note.

### Step 4 — the rest of the ramp note (PROVED or ASSUMED)

- **The conservative bound (2),** `gap ≥ 2J/[M ℓ d_max^{2ℓ}]`, re-derived:
  - the vertex inequality gives neighbour ratios at most `d_max`;
  - the ground-state transform gives the Dirichlet form;
  - the path-counting Poincaré inequality then gives the bound.
- **The adiabatic amplitudes**, re-derived:
  - linear ramp: `B = 2v/g² + 7v²/g³`, with `v = (d_max − d_min)/2`;
  - smoothstep: `B = 3v/g² + (42/5)v²/g³`, using `∫|6 − 12s| ds = 3` and `∫36s²(1 − s)² ds = 6/5`.
- **ASSUMED (import).** The Jansen–Ruskai–Seiler Theorem 3 is used as stated in the note.
- **Consequence.** With `g = 0.594622` and `v = 6`, the smoothstep amplitude is `B = 3·6/g² + (42/5)·36/g³ ≈ 1.49·10³`. So the theorem guarantees failure probability at most `B²/τ²` only for `τ ≳ 1.5·10³ J⁻¹`. The note's converged numerics are far better, as the note itself says.

## (3) Where it stops

- **No defect found.** The attraction theorem holds exactly as stated, and its premises hold on the actual 864-state geometry.
- **The certificate is for one finite component.** It gives no volume-uniform gap. The Lipschitz covering is loose: the smallest grid gap is at `δ = 0`.
- **Premises the note already lists as supplied.**
  - A volume-uniform rate for the cooler.
  - Compatibility with an adjacent field phase.
  - The fresh-record stream.
  - Native realisation.

## (4) Remaining obligations

- **(i)** A lower bound on the cooler's Lindbladian gap that is uniform in volume, or an obstruction to one.
- **(ii)** The same ramp certificate on larger components. The translation-sector method scales to about 10⁴ states with exact `LDLᵀ`. Beyond that, a structured approach is needed.
- **(iii)** Compiling the ramp with the live formation law.

## ASSUMED

- The supplied model of the notes: link qubits, flip couplings, fuel ancillas and controls.
- Jansen–Ruskai–Seiler Theorem 3.

## Reproduce

```bash
python3 probes/work/derive/deferred-20260926-local-rk-preparation/w-jonathonsmac4f50-j7dec/check.py
```

The run takes about 4 minutes, with 8 processes for the grid points.

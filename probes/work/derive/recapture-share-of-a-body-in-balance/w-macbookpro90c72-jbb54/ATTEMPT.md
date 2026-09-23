# J:derive:recapture-share-of-a-body-in-balance:a1

Worker `w-macbookpro90c72-jbb54` (claude-opus-5-5). This is attempt 1 of 3. There were no earlier attempts, and I formed my plan before reading anything else.

**Overlap.** Three of my earlier units used the same inertial clause and the same directed-walk visits:
- #8759, the shadow force (multinomial visit probabilities, emission terms);
- #8725, the capture rate of transparent bodies;
- #8758, the inertial gas.

The cosine-law hitting function and the shares below are new. The walk algebra is re-derived here.

**Definitions** come from blocks 44–49 (PRs 'ail44', 'ail45', 'ail47', 'ail48', 'ail49'; block 49 is #8559). The emission and the executed wind control are block 49's `supervisor_control_block49_wind.py` with `--pinned --balanced` and the `emit()` of `inertial_balanced.py`. The tick is `probes/lib/inertial.py`.

## (1) Exact statement

### The clause

This is a supplied clause of blocks 44–49 (sphere menu).
- **Moves.** A record of content `s` attempts moves about once per tick. Each attempt steps along `e_k` with probability `max(0, s·e_k)/√3`.
- **Targets.** An empty target is entered. An occupied target swaps contents. A solid target captures the record.
- **Scattering.** Bonds re-draw pairs of contents at rate `γ`.
- **Balance.** A body in balance keeps a store of captured records. Each tick, every stored record tries once to leave: a random body site, a random direction `k`, and — if the neighbouring site is free gas — a record there with content `v`, drawn from the cosine law about `e_k`. The body's momentum changes by `−v`.
- **Push per capture.** It is (captured minus emitted momentum)/(u × captures).

### (a) γ = 0, small density

In steady state, the share of a balanced body's captures that are its own emissions is

`f_B = mean over the free faces (x, k) of ∫ (cosine law about e_k) P(the directed walk from x + e_k with content v steps onto B)`.

- **The walk.** Each move goes along `sign(v_j) e_j` with probability `|v_j|/|v|₁`.
- **One site, or neighbours.** No emission ever returns to its own site or to a lattice neighbour of it. So one site has `f = 0`.
- **Values.**

  | body | `f` |
  |---|---|
  | 15 sites uniform in the lattice ball of radius 4 | `0.1337` (first order: `14 ḡ = 0.14987`) |
  | the executed bodies (each ball site with probability 0.06, `N ≥ 3`), capture weighted | `0.1441` |
  | the solid ball of radius 3 | `0.1086` |

- **The push.** The balanced body's wind captures equal the capture-only body's. Its own returns and its emissions carry no mean momentum. So its push per capture is `push_co (1 − share)`.
  - Over the executed 40-tick window the cumulative share is 0.1278.
  - The prediction is `0.97(1 − 0.1278) = 0.846`, against the executed `0.846 ± 0.032`.
  - For one site the prediction is `f = 0`, against the executed `0.966 ± 0.027` versus `0.999 ± 0.020`.

### (b), (c)

These are estimates with executed checks. See steps 7–8.

## (2) Steps

1. **PROVED (at γ = 0 an emitted content is a directed walk).**
   - With `γ = 0` and no other records, the content `v` never changes. Each move goes to `x + e_k` with probability `max(0, v·e_k)/√3`, so a move goes along `sign(v_j)e_j` with probability `|v_j|/|v|₁`, whatever the timing. The path is a monotone lattice path, and it ends when it first steps onto a body site (capture).
   - An exchange with another record moves the content on as if the target were empty. At small density this changes nothing. At density `ρ` a content can also be pushed back by another record's exchange; this is the density effect listed under ASSUMED.

2. **PROVED (no return to the emitting site or its neighbours). CHECKED A1.**
   - The emitted content has `v·e_k > 0`. So the `k`-coordinate of the walk never decreases from that of `x + e_k`.
   - The emitting site `x`, and every neighbour `x + e_j`, has either a smaller `k`-coordinate or is `x + e_k` itself, which is not a body site because the face is free.
   - Hence one site in balance recaptures nothing, and adjacent body sites never recapture each other's emissions: `g(e_j) = 0`.

3. **PROVED (the share equals the hitting probability; the push formula).**
   - **The share.** In balance, emissions equal captures in rate. At small density each emission returns independently with probability `f_B`, so the own share of captures is `f_B`. The emission is uniform over free faces: a rejected attempt is simply retried, and the gas occupancy of the neighbour is independent of the face.
   - **The wind captures.** At small density, emitted contents never block wind contents. So the balanced body captures exactly the wind contents the capture-only body captures, with the same momentum.
   - **The mean emission is zero.** The outward normals of the exposed faces of any finite union of cubes sum to zero. So the mean emitted content, `(2/3) × mean normal`, is zero for every body.
   - **The escaped emissions.** A returned content brings back exactly its `v`, so the net momentum per emission is `−v·1[escape]`. Its mean is `E[v·1[return]]`. That does not depend on the wind, and it vanishes over the reflection-symmetric ensemble of random bodies.
   - **Result.** Hence `push_balanced = push_co × W/(W + R) = push_co (1 − share)`, where `W` counts wind captures and `R` counts own returns.

4. **CHECKED (A2): the two-site function and the first-order share.**
   - **The cosine law in simplex coordinates.** Parametrise one octant of the cosine law by `q = |v|/|v|₁` on the simplex. Then `cos θ dΩ/π = (1/π) q_n |q|⁻⁴ d²q`, and the four octants sum to 1 (to `10⁻¹³`).
   - **The two-site function.** An emission reaches displacement `d` with probability
     `g(d) = (1/6) Σ_k (compatible octants) · multinomial(D) · J(D)`, with `D = d − e_k`,
     `J(m_n, m_a, m_b) = (1/π) ∫ q_n^{m_n+1} q_a^{m_a} q_b^{m_b} |q|⁻⁴`, and the octant count doubled for each zero transverse component.
   - **Its mean.** Over the 65,792 ordered pairs of the 257-site ball, the mean is `ḡ = 0.010705051406`. The 80- and 60-point rules agree to `10⁻¹²`.
   - **First order.** `f₁ = (N − 1)ḡ = 0.14987` for `N = 15`. It is an upper bound: it counts every body site a walk passes, not only the first.

5. **CHECKED (A3): all orders, by direct sampling of the walks, with exact DP on the same emissions.**
   - For a given body, face and content, the first-passage probability is an exact DP over monotone paths. The walk is also simulated step by step.
   - Results from 400,000 emissions each:

     | body | walk sampling | DP |
     |---|---|---|
     | uniform `N = 15` | `0.1341 ± 0.0005` | 0.1337 |
     | executed bodies, weighted by `N` | `0.1447 ± 0.0006` | 0.1441 |
     | one site | exactly 0 | 0 |
     | solid ball of radius 3 | `0.1083 ± 0.0005` | 0.1086 |

   - **Why weight by `N`.** The balanced body fills its shadow (block 49), so its capture rate is proportional to `N`. The executed ratio (Σ momentum over Σ captures across seeds) weights each body by its captures.
   - **The solid ball.** Its returns come from the lattice staircase: an emission from a face in a step can move sideways onto the protruding site. The mean path is 1.4 moves.

6. **CHECKED, as a floating-point model (A4): the 40-tick window.**
   - **The inputs.**
     - Hits need `m = 1, 2, 3, 4` moves with weights 0.286, 0.222, 0.169, 0.121 (exact DP, capture weighted).
     - Moves arrive as a Poisson stream of rate `|v|₁/√3` per tick: `L³` random attempts per tick.
     - A stored record leaves with probability `(1 − ρ)(free faces) ≈ 0.62–0.70` per tick.
     - The capture-only body's shadow forms with one extra move.
   - **The result.** The cumulative share over 40 ticks is 0.1278 (steady 0.1435), and the prediction is `0.97(1 − 0.1278) = 0.846`, insensitive to the leaving probability.

7. **ESTIMATE (b): scattering.**
   - **Mean free path.** At `ρ = 0.3` a record scatters at rate `6γρ = 1.8γ` per tick and moves about 0.87 sites per tick. So one mean free path is about `0.5/γ` sites. At `γ ≥ 1` an emitted content is re-drawn before it reaches another site: the walk becomes a diffusion.
   - **Return probability (capacity).** For a diffusing tracer released next to a body site, `P_ret ≈ 1 − 1/(G(0) + (N − 1)⟨G⟩)`. This uses the mean-field equilibrium measure of the body.
     - Lattice values: `G(0) = 1.516386`, `⟨G⟩ = 0.14154` over the ball's pairs.
     - So `P_ret ≈ 0.714` for `N = 15`, `R = 4`: 0.148 at its own site and 0.567 at the others. An isolated site gives `1 − 1/G(0) = 0.3405`.
   - **This is not the push deficit.** If returns stayed neutral, the push ratio would be about `1 − 0.71 ≈ 0.3`, not the executed `0.83/0.89 = 0.93`.
   - **Why.** Each scattering replaces half of a content's mean by its partner's, so a scattered return brings back the local gas's wind.
   - **The executed tagged control (INFO; `tagged_wind.py`, same seeds as block 49's control).** It reproduces the control exactly: push 0.8463, 0.8280, 0.7978 at `γ = 0, 1, 4`. Its shares of the balanced body's captures over 40 ticks:

     | `γ` | unscattered own contents | own-content weight `s_w` | own particles |
     |---|---|---|---|
     | 0 | 0.1255 | 0.1255 | 0.345 |
     | 1 | 0.0474 | 0.2193 | 0.369 |
     | 4 | 0.0397 | 0.2089 | 0.382 |

   - **The weight `s_w`.** Weights halve by averaging at each scattering and travel with the content.
   - **The push follows the own-content weight.** In every run, `push ≈ (1 − s_w) ũ`, where `ũ = 0.98–1.05` is the wind carried per unit of non-own content, which is the undisturbed wind.
     - At `γ = 1`: `(1 − 0.219) × 1.01 = 0.79`, executed 0.828.
     - The capture-only body's 0.896 is lower for a different reason: the wind is depleted around a sink.
   - **The 40-tick numbers are transient.** At `γ = 1` over 400 ticks (60 seeds) the shares grow: `s_w = 0.344` and own particles 0.554. The push falls to 0.692, and `(1 − s_w)ũ = 0.688`, so the push law still holds.
     - These long runs are inflated by the periodic box. An escaped content wraps around `L = 32` and can return after about 37 ticks.
     - The same length of run at `γ = 0` gives an own-content share of 0.190, against the no-wrap steady value 0.144.
     - The 40-tick values are essentially free of this.
   - **Long times.** The count share tends towards the capacity value 0.71, and the push keeps falling.
   - **Estimate.** The share relevant to the push is the own-content weight share: 0.22 at the executed 40 ticks, and towards the capacity value as the returns accumulate. The count share is about 0.37 at 40 ticks and 0.71 at long times.

8. **ESTIMATE (c): the solid ball of radius 3.**
   - **At `γ = 0`:** 0.109 of its emissions return (step 5).
   - **At `γ = 1`, long times:** a diffusing tracer released on a free neighbour returns with probability 0.80 (lattice SRW: 0.789 before radius 60, plus about `R_eff/60` from beyond). So in the long run about 0.8 of its gross captures are its own emissions by count.
   - **Tagged control, 40 ticks.** In the wind with the ball pinned: own particles 0.41, own-content weight 0.237, unscattered 0.055. The push is 0.734 against 0.862 for the capturing ball (ratio 0.851), and `(1 − 0.237) × 0.97 = 0.738`.
   - **The two-body runs.** Block 49's ratio is `0.75/0.92 = 0.815`. Its runs are longer (1500 warm-up ticks), consistent with a larger own-content share there: `(1 − s_w)ũ = 0.815 × 0.92` needs `s_w ≈ 0.25–0.3` relative to the undisturbed wind.
   - **Estimate.** Own emissions are 0.8 of the ball's gross captures by count at long times. By weight they are 0.25–0.3, which is what reduces the push.
   - **The 400-tick periodic runs (INFO).** Own-content weight 0.423, own particles 0.649, push 0.603 at `γ = 1`; at `γ = 0` the own share is 0.196. Wrap-around inflates these; the no-wrap `γ = 0` value is 0.109. They confirm only that the shares keep growing with time.

### ASSUMED

- **(a):** small density (independent records). At `ρ = 0.3` the executed balanced body collects 6% more wind captures than the capture-only body (134.4 against 127.0 per seed at `γ = 0`). This is within the push's error.
- **The 40-tick window:** the Poisson-attempt timing and the leaving probability.
- **(b), (c):** the simple-random-walk tracer, and the mean-field capacity of a sparse body.

## (3) Where the route stops

- **(a) is closed at small density.** The remaining gap is the density effect: exchanges push contents back, and emitted records sit in the gas that wind records pass through. It is a few per cent at `ρ = 0.3` (see ASSUMED).
- **(b) and (c) are estimates.** At `γ ≥ 1` the relevant share is the own-content weight, not the count of returns. Its growth in time is a momentum-diffusion problem that is not solved here.
- **The periodic box also matters, in two ways.**
  - Escaped contents wrap around and return after about 37 ticks.
  - It loses wind momentum to the pinned body: about 1% over 40 ticks and about 11% over 400 ticks.

  The 40-tick comparisons are nearly free of both. The 400-tick runs are qualitative only. Block 49's two-body runs use an open box with a reservoir, so they have neither problem.

## (4) What would finish it

- **(a):** a density expansion of the exchange corrections at `ρ = 0.3`.
- **(b), (c):** a hydrodynamic solution for the own-content weight near a balanced body. Momentum diffuses from the emitting faces and is re-absorbed; its long-time limit is the capacity return probability, with the viscous time scale fixing `s_w(t)`.
- **Executed controls with an open reservoir,** so that the wind is not depleted.
- **A referee from another model family.** Blocks 44–49 and this attempt are the same family.

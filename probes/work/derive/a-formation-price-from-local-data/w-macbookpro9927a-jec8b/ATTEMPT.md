# A formation price from local data — attempt 2 of 2

- **Worker:** `w-macbookpro9927a-jec8b` (claude-opus-5-5), unit `J-derive-a-formation-price-from-local-data-a2`.
- **Checks:** exact, in `check.py` in this directory. Family letters (Q, I, R, C, P, B) refer to it. It runs in about 15 s.
- **Prior attempts:** none were printed at claim time.

**Disclosure.**
- Block 116 (open hand-off PR #9159) harvests two probes attempts, #8653 and #8748.
  - #8748 is this machine's own (`sources-under-the-record-reading:a4`).
  - This machine's #8964 (`the-rest-energy-of-a-record:a1`) derived the same kept-ledger price independently.
- The question here, whether a local rule can set that price, is new. This attempt builds on block 116's T1 to T3, which Grok referees confirmed, and re-derives what it uses.

**Sources.** Each is pinned by commit and SHA-256 in family Q.
- **Block 116** (`…FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE…_2026-09-24.md`), read on its branch at `0981f09c` as the task directs. It is not on main. It works within blocks 55, 56 and 58 as landed.
- **Block 57** as landed on main (`…A_DELAY_FOR_THE_RATE_FIELD…_2026-09-21.md`), for (b).
- Nothing is adopted.

## 1. Statement attempted

### Setting (block 116's premises)
- **The box.** A held cube of odd side `n`. Its boundary layer is the wall, where `φ = 1`.
- **The law.** `k = γ/12`, and `g = (1 − A)⁻¹` on the interior with zero wall values.
- **The amplitude.** An amplitude `χ` with Hermitian `H` gives `K_xy = Re χ_x†H_xyχ_y` and `e = K1`.
  - Bodies at rest: `K = diag(m)`. Signed rest energies are realised by an on-site `σ₃` term, as in block 116's moving witness.
- **The two readings.**
  - *Amplitude sourcing*: `((1 − A) + kK)ψ = k e`, with `φ = 1 − ψ`.
  - *Records only*: `φ ≡ 1` before the event.
- **The event.** It replaces the amplitude by one record at rest at `y`, with bare energy `E'`. Block 116 T1 gives the ledger-keeping price `E' = Λ/(1 − kΛ g_yy)`, where `Λ = Σ e φ`.

### What a rule of radius R is
- A rule of radius `R` is any function of the data within Chebyshev radius `R` of `y`. Those data are the amplitude there (`χ` and `H`, hence `K`) and the pre-event rates `φ` there.
- A Chebyshev ball is used for definiteness. For another ball, replace `B_{R+1}` below by `B_R` together with its neighbours.
- The task places no bound on the amplitude's extent.

### Claims
- **(a1)** Records only: no rule of any radius `R` gives `E'` in every held box.
- **(a2)** Amplitude sourcing: no rule of any radius `R` gives `E'` in every held box.
- **(a3)** Amplitude sourcing, positive: whenever the effective source `s = Kφ` is *point-equivalent* at `y`, meaning `s − Qδ_y = (1 − A)f` with `f` finitely supported and `Q = Σ s`, the local rule `E' = Q/(φ_y + k f_y)` is exact in every held box. Here `f` is computable inside the window.
- **(b)** The kept-ledger condition under block 57's delayed law. This part is conditional.

## 2. Steps

**S1 (PROVED; CHECKED I). The ledger is the total effective source.**
- Since `K` is symmetric, `Λ = Σ_x e_xφ_x = (K1)ᵀφ = 1ᵀKφ = Σ_x s_x =: Q`, with `s := Kφ`.
- The static law reads `(1 − A)ψ = k(e − Kψ) = kKφ = k s`, so `ψ = k G_Ω s`.
- A record of bare energy `E'` at `y` has effective source `E'φ'_y δ_y`. Keeping the ledger means `E'φ'_y = Q`.
- Then the post-event field is `ψ' = kQ g(·, y)`, and **`E' = Q/φ'_y`**. With `φ'_y = 1/(1 + kE'g_yy)` this is block 116 T1(b).
- CHECKED: in the side-7 box, block 116's cube numbers are reproduced exactly:
  - `Λ = Q = 0.984627…`;
  - site prices `1.1054844`, `1.1067108`, `1.1081082`, `1.1097121` (corner, edge, face, centre);
  - `E'φ'_y = Λ`;
  - the post-event field `kΛ g(·, y)` solves the law exactly;
  - the uniform star's `1188/1091` in the boxes of side 7 and 9;
  - the distance-two cross's `1.1057730` (side 7) and `1.1050546` (side 9).

**S2 (PROVED; CHECKED R). Records only: no rule.**
- *The data carry no wall information.* Before the event `φ ≡ 1`. So the data within radius `R` are the amplitude there and constant rates, and they do not see the walls.
- *The price does.* `E' = E/(1 − kE g_yy)` is strictly increasing in `g_yy` whenever `0 < kE g_yy < 1`.
- *Monotonicity of `g` in the box.* Take held cubes `Ω ⊂ Ω'` that both contain `y`. Then `d := g_{Ω'}(·, y) − g_Ω(·, y)` is harmonic on the interior of `Ω`. On `Ω`'s wall it equals `g_{Ω'}(·, y) ≥ 0`, and it is `> 0` at interior points of `Ω'`, since `g_{Ω'} > 0` there by irreducibility. By the maximum principle `d > 0` on `Ω`'s interior, in particular at `y`.
- *Pairs for every R.* The same amplitude supported in `B_R(y)`, placed with `y` at the centre of the cubes of sides `n` and `n + 2` (`n ≥ 2R + 3`), gives identical data within radius `R` and different prices.
- CHECKED:
  - `g` at the centre is `1`, `22/17`, `136/99`, `79271956/56195761` for sides 3, 5, 7, 9.
  - `g_{n+2} > g_n` holds everywhere on the smaller interior for `n = 5, 7`.
  - The pairs `(3,5)`, `(5,7)`, `(7,9)` (`R = 0, 1, 2`, with `E = 1`, `γ = 1`) give prices `1.090909`, `1.120879`, `1.129278`, `1.133213`.

**S3 (PROVED; CHECKED C). Amplitude sourcing: no rule — the charged cage.**

*Lemma.* Fix `R`, a held box, and `y` at Chebyshev distance at least `R + 3` from the wall. Put

  `v := g(·, y)` outside `B_{R+1}(y)`, `v := 0` on `B_{R+1}(y)` and on the wall; `σ := (1 − A)v`.

Then:
- (i) `σ` is supported on the two layers at Chebyshev radius `R + 1` and `R + 2`.
- (ii) `G_Ω σ = v`, so the field of `σ` vanishes identically on `B_{R+1}` and equals `g(·, y)` outside.
- (iii) `Σ_x σ_x = 1`.

*Proof.*
- (i) Away from those layers, `v` is locally either `0` or `g(·, y)`. Both are annihilated by `1 − A`, because `y ∈ B_{R+1}`.
- (ii) `v` vanishes on the wall.
- (iii) `Σ_x ((1 − A)v)_x` equals the net outward flux of `v` through the wall. That is the same flux as `g(·, y)`'s, which equals `Σ_x ((1 − A)g(·, y))_x = 1`. ∎

*The pair.*
- Configuration 1 is any amplitude supported in `B_R(y)`, with field `ψ₁` and effective source `s₁`.
- Configuration 2 adds bodies at rest on the cage layers, with masses `m_x = c σ_x/φ₂(x)`, where `φ₂ := φ₁ − kc v`.
- Then `ψ₂ = ψ₁ + kc v` solves configuration 2's static law. On the cage, `(1 − A)ψ₂ = kcσ = k m φ₂`. Elsewhere nothing changes, since `v = 0` on the original amplitude.
- *Uniqueness.* For small `c` the operator is positive definite, so the solution is unique. Weyl's inequality gives `λ_min ≥ λ_min(1 − A) + k·min(m, 0)`, and `λ_min(1 − A) = 1 − cos(π/(n − 1)) ≥ x²/2 − x⁴/24` with `x = 3/(n − 1)`.
- *Every window datum is unchanged.* The cage lies outside `B_R`, and `v = 0` on `B_{R+1}`. So the amplitude and every rate within radius `R` agree.
- *The ledger moves.* `Λ₂ = Λ₁ + c`, so `E'` changes, because `E' = Q/(1 − kQ g_yy)` is strictly monotone in `Q`.

*CHECKED, with exact zero residuals:*

| Box side | `R` | `c` | Amplitude | Cage sites | Price without cage | Price with cage |
|---|---|---|---|---|---|---|
| 7 | 0 | 1/5 | a body at `y` | 80 | 0.5 | 0.729096 |
| 9 | 1 | 1/4 | an asymmetric two-body amplitude | 248 | 0.862167 | 1.175554 |
| 9 | 1 | −1/7 | a three-body amplitude | 248 | 1.088506 | 0.910129 |

The cage is the lattice form of a charged shell whose field vanishes inside. It is a Faraday cage around the window, with total charge 1.

**S4 (PROVED; CHECKED P). Amplitude sourcing: the local rule for point-equivalent sources.**

*Statement.* Suppose `s = Kφ` is supported in `B_R(y)` and `s − Qδ_y = (1 − A)f` with `f` finitely supported. Then, in every held box whose interior contains `B_R(y)`:
- `ψ = kQ g(·, y) + k f`;
- `φ'_y = φ_y + k f_y`;
- **`E' = Q/(φ_y + k f_y)`**.

*Proof.*
- The field: `ψ = kG_Ω s = kQ G_Ωδ_y + kG_Ω(1 − A)f = kQ g(·, y) + k f`, because `f` vanishes on the wall.
- By S1 the post-event field is `kQ g(·, y) = ψ − k f`. Hence `φ'_y = φ_y + k f_y`, and `E' = Q/φ'_y`.

*Locality of `f`.*
- Suppose `(1 − A)f = w` with `f` finitely supported. Take `z ∈ supp f` with maximal first coordinate. Then `w(z + e₁) = −f(z)/6 ≠ 0`, since every other neighbour of `z + e₁` lies beyond `supp f`.
- So the extent of `supp f` along each axis lies strictly inside that of `supp w`, and `f` lives in the bounding box of the source, inside `B_R`.
- `f` is unique, because a finitely supported harmonic function is zero by the same argument. It is found by one finite exact solve from the window data.

*CHECKED.*
- Three asymmetric point-equivalent sources, each realised by bodies at rest with `m = s/φ`: side 7 at the centre, and side 9 at `(4,3,5)` and at `(4,4,4)`. In each, the rule equals the exact price, and `φ'_y = φ_y + k f_y` holds exactly.

*Block 116's star.*
- Its source excess is `s₁(Σ_i δ_{n_i} − 6δ_y) = −6s₁(1 − A)δ_y`, so `f = −6s₁δ_y`.
- The rule `Q/(a − 6km₁b)`, with `a = b/(1 + km₀)`, reduces symbolically to block 116 T3's `c/(1 − kc)`.
- This is why the star's price ignores the walls in symmetric boxes. Symmetry makes the six arm charges equal, which is exactly point-equivalence.

*The obstruction.*
- If `w = (1 − A)f` with `f` finite, then `Σ_z P(z)w_z = 0` for every discrete harmonic polynomial `P` (sum by parts).
- `P = x⁴ − 6x²y² + y⁴ − 2z²` is discrete harmonic (CHECKED).
- It pairs to `0` with the star's excess, and to `48s₂` with the distance-two cross's.
- So the cross is not point-equivalent, and its price moves with the box, as block 116 T3(d) found.

**S5 (PROVED, conditional; CHECKED B). Part (b).**
- *The source is constant.* Imposing `E'(t)φ'_y(t) = Λ` makes the record's effective source the constant `Λδ_y` from the event on. The field is then driven by a step change of source, from `s₁` to `Λδ_y`.
- *The step response.* Block 57 T2's reduced law, as landed, says "A fixed source switched on at zero gives `(1 − cos(ω₀t))u_static`". Every mode shares the one frequency `ω₀ = w̄/√(γκ)`.
- *Consequence* (ASSUMED: this law, in the weak-field linear identification of its source with `kKφ` and its field with block 116's `ψ`). The offset from the pre-event field is `(1 − cos ω₀t)` times the static change. So:
  - the clock at `y`, and with it the self-consistent `E'(t) = Λ/φ_y(t)`, first reaches its post-event value at `t = π/(2ω₀)`;
  - it overshoots to twice the change at `t = π/ω₀`;
  - it oscillates undamped and never settles.
- In block 57's T3 wave model on a finite held box, energy is also conserved, and no settling occurs there either. The T3 case is not worked here.

## 3. Where the route stops

1. **Window-confined sources that are not point-equivalent, under amplitude sourcing.**
   - For a source supported inside the window, identical window data in two boxes would need `(G_{Ω₁} − G_{Ω₂})s = 0` on `B_R`. Generically that forces `s = 0`.
   - So S3's pairs must reach one layer beyond `B_{R+1}`. S3's amplitude therefore extends two layers past the window, to radius `R + 2`.
   - Whether some rule, necessarily one that decodes the box from the window field, exists for confined sources that are not point-equivalent is not settled here.
   - The walls enter through `φ'_y = φ_y + k[G_Ω(s − Qδ_y)]_y`, that is, through the wall response to the non-monopole part of the source.
2. **(b) is conditional.** It uses block 57's reduced model in a weak-field linear identification with block 116's held-wall law.

## 4. What would finish it

- **Confined sources.** Either injectivity of the map from box to window field, which would allow a (non-natural) rule, or explicit coincidences. A natural candidate is a two-site source in two cubes with `y` off-centre.
- **(b) exactly.** In block 57's T3 wave model with walls held: the step response of the kept-ledger source, and the energy radiated to the walls.
- **Both readings over a crowd.** When other records sit near the window, their fields add to the pre-event rates under either reading, and S2's pairs survive only with the same neighbourhood of records.

## Answers

- **(a)** Settled in the negative for the task's class, where the amplitude is unrestricted. Under either reading, no rule of any fixed radius `R` gives the price in every held box.
  - Records only: one amplitude placed in two boxes.
  - Amplitude sourcing: a charged Faraday cage just outside the window.
  - Positive: under amplitude sourcing, whenever the effective source is point-equivalent, `E' = Q/(φ_y + k f_y)` is exact in every held box. Block 116's star is such a case.
- **(b)** Under block 57's reduced law, the kept-ledger condition fixes the source. The clock at `y` first reaches the post-event value at `t = π/(2ω₀)`, overshoots by the full change, and never settles.

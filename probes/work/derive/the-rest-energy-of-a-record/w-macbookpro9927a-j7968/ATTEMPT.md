# The rest energy of a record: where E_rec comes from under a formation event that keeps the ledger

Attempt 1 of 2. Worker `w-macbookpro9927a-j7968` (Claude Opus 5.5, `claude-opus-5-5`). Checks: `check.py` in this directory. It is exact throughout (Fractions, sympy `DomainMatrix` over `QQ`, sympy series) and runs in about 15 s.

**Sources.** Definitions are read from the notes on the PR heads:
- block 53 (#8568, `c4e6a23f6c`): the rate clause and the record clause `w_x = κ F̃(neighbours)`;
- block 55 (#8571, `525c6500c5`): the ledger `⟨H_w⟩ + F`, T1–T4 and the corollary `log κ = −(γ/6)E/w̄`;
- block 56 (#8573, `d6c6e2572d`): the box, the exact law `((1 − A) + D)φ = 0`, the ledger `Σ m φ` and the one-body and pair formulas;
- block 58 (#8579, `e526d22c18`): the formation event;
- block 95 (#8860, `f9b34475df`): records on their own clocks;
- block 104 (#8931, `705d466f49`): T3.

`check.py` family Q confirms 13 quoted lines verbatim.

**Provenance and overlap.**
- Blocks 104 and 95 were written by a worker and supervisor of my model family (block 104 says so). Nothing here was refereed before this attempt, and no prior attempt existed at claim time.
- My earlier work on block 95's delayed clock (the-delayed-clock-and-the-pair-law, not landed) concerned one `κ` with a delay. T5 below concerns one `κ` per record with no delay, and reuses nothing from it.

## (1) The exact statement attempted

**Formation clause F (stated here; everything below is conditional on it).**
- **F1. The box.** Block 56's box: walls held at `φ = 1`, interior rates free. The static law holds at every instant, meaning the ledger `⟨H_w⟩ + F`, `F = (2/γ)Σ_bonds(φ_x − φ_y)²`, is stationary in every interior `u_x` (block 55 T2 with block 56's walls; no multiplier).
- **F2. Before.** One amplitude is alone in the box, at a static solution, with ledger `L := ⟨H_w⟩ + F`.
- **F3. The event.** At one instant the amplitude is replaced by one record at an interior site `y`.
  - The record acts on the rate field as one body at rest at `y` with a bare energy `m'`. This is block 58's "The record. One body at rest at `y` with bare energy `m'`".
  - It keeps `m'` from then on (records are permanent).
  - It carries a content `c` (the possibility it locks), from any alphabet.
  - Nothing else is in the box.
- **F4. The ledger is kept.** The ledger after the event equals `L`.

`G = (1 − A)⁻¹` on the interior (zero walls), `g_y = G(y, y)`, `t = γm/12`.

**T1 (a body is a block-53 record with block 56's mean; its κ is fixed by its bare energy).** In block 56's law, a body at rest at `y` with bare energy `m'` satisfies

`w_y = κ · M_½(w_{y+e})`, where `κ = (1 + γm'/12)⁻²` and `M_½(w) = ((1/6)Σ_e √w_{y+e})²`.

- This holds exactly, whatever else is in the box.
- An empty interior site has `κ = 1`. `M_½` is block 55 T4(d)'s "block 53's power mean of order 1/2", the member of block 53's class that block 56's empty-space law is.
- In the geometric-mean member this is false: `κ_geo` depends on the neighbourhood.

**T2 (the record's rest energy under F).**
- The record's bare energy is `m' = L/(1 − (γ/12)g_y L)`. It exists iff `L < 12/(γ g_y)` (block 58 T1, re-derived).
- Its clock is `φ_y = 1 − (γ/12)g_y L`.
- Its three energies (block 56 T2) are: bare `L/φ_y`, ledger `L`, in the field `Lφ_y`.
- Its `κ` is

`κ = (1 + γm'/12)⁻² = [(1 − (γ/12)g_y L)/(1 − (γ/12)(g_y − 1)L)]²`, and `log κ = −(γ/6)L − (γ²/144)(2g_y − 1)L² + O(γ³L³)`.

**T3 (what the rest energy comes from).**
- No quantity in T2 depends on the content `c`. A record's `m'` and `κ` are functions of `(L, g_y)` alone.
- For any amplitude with a static solution, `L = (2/γ)Σ_{wall bonds}(1 − φ)`. This counts rest energy and energy of motion alike.
- So an amplitude whose generator has no on-site term, with `L > 0`, forms a record with `m' > 0`.
- `L < 0` gives `m' < 0`, `κ > 1` and `φ_y > 1`.

**T4 (one κ for every record?).**
- (a) Two records formed under F have equal `κ` iff `L₁/(1 − (γ/12)g_{y₁}L₁) = L₂/(1 − (γ/12)g_{y₂}L₂)`. At equal `g` this means `L₁ = L₂`.
- (b) One species at rest, with bare `m` and weights `p`, gives
  - `m' = m(1 + t(g_y − ⟨G⟩_p)) + O(t²)`, with `⟨G⟩_p = Σ p_x p_{x'} G(x, x')`;
  - `log κ = −2t − t²(2(g_y − ⟨G⟩_p) − 1) + O(t³)`.

  Also `g_y − ⟨G⟩_p > 0` whenever `p` has two or more sites and `y` has the largest `g` on its support. Records of one species therefore differ by the spread of the amplitude they came from, at order `(γm)²`, and by the site, through `g_y`.
- (c) One `κ₀` for every record, together with a kept ledger, allows formation at `y` only from amplitudes of ledger exactly `L₀(y) = m₀/(1 + (γ/12)g_y m₀)`, where `m₀ = (12/γ)(κ₀^{−1/2} − 1)`.

**T5 (block 95's chain with one κ per record).** Give each record its own `λ_r = log κ_r` in block 95's P1–P4, so that `log w_z = 6Σ_r λ_r G₉₅(z − r)`, where `G₉₅` is block 95's zero-mean `G`.
- (a) For two records, every four-move cycle has `log(forward/backward) = 6(2a − 1)(λ₂ − λ₁)Δ`, with `Δ = G(x−u) − G(y−u) + G(y−v) − G(x−v)`. Detailed balance, and with it block 95's T2 pair law, needs `λ₁ = λ₂` (for `a ≠ 1/2`).
- (b) At `a = 1`, two records have the separation law `π(d) ∝ 1/(r₁(d) + r₂(d))`, where `r₁ = e^{6λ₁G(0) + 6λ₂G(d)}` and `r₂ = e^{6λ₂G(0) + 6λ₁G(d)}`. Its first order is `exp(−3(λ₁ + λ₂)G(d))`, so the coupling of a pair is the mean of its two sources.
- (c) The two records' mean velocities at separation `d` (`|d|₁ ≥ 2`) sum to `((1 − a)/2)(λ₂ − λ₁)Σ_e e G(d + e) + O(λ²)`.

## (2) Steps

**S0 — ASSUMED.**
- The clause F (F1–F4). In particular, a record acts on the rate field as block 56's body at rest, and it keeps its bare energy.
- Block 55's law and ledger, and block 56's box, law and bond energy, as supplied clauses. Nothing is adopted.

**S1 — T1 — PROVED, CHECKED (K).**
- At an interior site block 56's law reads `φ_y − (Aφ)_y + d_y φ_y = 0`, with `d_y = (γ/12)m_y` (block 56 T1). So `(Aφ)_y = (1 + d_y)φ_y`.
- Positive rates give `√w = φ`, so `M_½(w_{y+e}) = ((Aφ)_y)²` and `w_y/M_½ = φ_y²/((1 + d_y)φ_y)² = (1 + d_y)⁻²`.
- At an empty site `d = 0` and `κ = 1`: the empty-space law is `w = M_½(neighbours)`, the power mean of order ½, which is in block 53's class.
- So block 53's record clause, with `F̃ = M_½`, is exactly block 56's body, with `κ = (1 + γm'/12)⁻²`. It involves no other site, and it inverts to `m' = (12/γ)(κ^{−1/2} − 1)`.
- CHECKED (K):
  - three bodies (bare energies `3, 1/2, 7/5`, `γ = 1`) in the `5³` box, at all 125 sites;
  - in block 53's geometric mean, `κ_geo⁶ = φ_y¹²/Π_e φ_{y+e}²` changes (`0.0687 → 0.0724`) when a second body is placed next to the first. The exact dictionary belongs to block 56's member.

**S2 — the one-body solution and T2 — PROVED, CHECKED (F).**
- After the event only the record is present. Set `ψ = 1 − φ`, which vanishes on the walls. Since `(1 − A)1 = 0` at interior sites (walls at 1), `(1 − A)ψ = Dφ`, so `ψ = G D φ`.
- At `y`: `φ_y = 1 − g_y d φ_y`, so `φ_y = 1/(1 + (γ/12)g_y m')`.
- Its ledger is `m'φ_y` (S3 with `K = diag(m')`).
- F4 then gives `m'/(1 + (γ/12)g_y m') = L`, that is `m' = L/(1 − (γ/12)g_y L)`.
- For `L > 0` this is positive iff `L < 12/(γ g_y)`. The map is increasing, with supremum `12/(γ g_y)`, as in block 58 T1.
- `φ_y = L/m' = 1 − (γ/12)g_y L`. Also `1 + γm'/12 = (1 − (γ/12)(g_y − 1)L)/(1 − (γ/12)g_y L)`, which gives the `κ` of T2 through S1.
- The three energies are `m' = L/φ_y`, `m'φ_y = L`, and `m'w_y = m'φ_y² = Lφ_y`.
- The series: `log κ = 2log(1 − agL) − 2log(1 − a(g − 1)L)`, with `a = γ/12`, equals `−2aL − a²L²(2g − 1) + O(a³)`.
- `g_y ≥ 1`, since `G = Σ_n Aⁿ` with the `n = 0` term 1. So for `0 < L < 12/(γg_y)` both brackets are positive.
- CHECKED (F):
  - for a point, a pair `{y, y + e₁}` and a 7-site cross at the centre of the `5³` box (`m = γ = 1`, `g_y = 136/99`), the ledger computed as `Σ m_x φ_x`, as `⟨H_w⟩ + F` and as `(2/γ)×` wall flux agrees exactly;
  - re-solving the law with the record alone returns ledger `L` exactly, `φ_y = 1 − (γ/12)g_y L` exactly, and `κ` equal both as `(φ_y/(Aφ)_y)²` and as the closed form.
- CHECKED (S): the series.

**S3 — the ledger is the wall flux, for any amplitude — PROVED, CHECKED (F, M).**
- Block 56 T1's remark gives `⟨H_w⟩ = φᵀKφ` with `K_{xy} = Re χ_x†H_{xy}χ_y` for any hermitian `H`.
- Block 56 T1's computation of `∂F/∂u_x` gives stationarity in `u_x` as `(Kφ)_x + (12/γ)((1 − A)φ)_x = 0` at interior `x`.
- Write `(φ_x − φ_z)² = φ_x(φ_x − φ_z) + φ_z(φ_z − φ_x)` and sum over all bonds. Wall–wall bonds give 0. An interior site gives `6φ_x((1 − A)φ)_x`, and a wall site gives `Σ_{interior z∼wall}(1 − φ_z)`.
- Hence `F = −Σ_x φ_x(Kφ)_x + (2/γ)Σ_{wall bonds}(1 − φ)`, and `L = φᵀKφ + F = (2/γ)Σ_{wall bonds}(1 − φ)`.
- For bodies at rest this is block 56 T2(b)'s `Σ m φ`.
- The ledger does not move while the law holds (block 55 T2(a); with the walls held the sum runs over interior `u_x` only). So `L` is the amplitude's ledger at any instant.

**S4 — content — PROVED.**
- Blocks 53–56's rate law and ledger contain a body or amplitude only through `K` (for a body at rest, the diagonal bare energies). No term takes a content argument.
- By S2, F fixes `m'` from `(L, g_y)`. By S1, `κ` is fixed by `m'`. So `c` enters none of them.
- A record's content can matter only through `L`, the energy of the amplitude it was formed from: its band sign, its species' mass, its spread, its motion.
- Remark, not used: block 104 T2 gives content-dependent `κ` at contact from the rule's own clock (block 50), and block 104 T1 shows that such terms have no far field.

**S5 — T3, rest energy from an amplitude with no on-site term — PROVED (S3), CHECKED (M).**
- The amplitude: `χ_y = (0, 3/5)`, `χ_{y+e₂} = (4/5, 0)`, with `H = Σ_j σ_j p_j`, `(p_jψ)_x = (ψ_{x+e_j} − ψ_{x−e_j})/(2i)`.
- `K` has zero diagonal, and `K_{y,y+e₂} = K_{y+e₂,y} = 6/25`, so the energy at uniform rates is `12/25`.
- The static solution is positive, with `L = 0.463861…` (exact rational) `> 0`.
- The record it forms under F has `m' = 0.489874… > 0`, and the ledger is kept exactly.
- This is not in tension with block 104 T3(b) (a walker at rest has no on-site rest energy). Under F, a record's rest energy is the converted ledger, not an on-site term.
- CHECKED (T): `L = −1/2` gives `m' < 0`, `κ > 1` and `φ_y > 1`, with the ledger kept. The one-body solution is explicit and positive; block 56 stated `m_i > 0`, so negative records lie outside its stated scope and are covered here only for one body.

**S6 — T4(a) — PROVED.**
- `κ(m') = (1 + γm'/12)⁻²` is strictly decreasing on `m' > −12/γ`.
- `m'(L)` has derivative `(1 − (γ/12)g_y L)⁻² > 0`.
- So equal `κ` ⟺ equal `m'` ⟺ the stated equation. At `g_{y₁} = g_{y₂}` this is `L₁ = L₂`.

**S7 — T4(b) — PROVED, CHECKED (F, S).**
- For bare `m` with weights `p` on `S`, `D = tP`, and block 56 T3(b) gives `E = m·1ᵀ(P⁻¹ + tG_S)⁻¹1`.
- `(P⁻¹ + tG_S)⁻¹ = (1 + tPG_S)⁻¹P = P − tPG_S P + O(t²)`, so `E/m = 1 − t⟨G⟩_p + O(t²)`.
- Then `m'/m = (E/m)/(1 − t g_y E/m) = 1 + t(g_y − ⟨G⟩_p) + O(t²)`, and `log κ = −2log(1 + t m'/m) = −2t − t²(2(g_y − ⟨G⟩_p) − 1) + O(t³)`.
- Positivity:
  - `G` is positive definite, being the inverse of the positive definite `1 − A` on the interior.
  - Hence `G(x, x')² < g_x g_{x'}` for `x ≠ x'`, and `⟨G⟩_p < (Σ p_x √g_x)² ≤ max_S g ≤ g_y` for `p` with two or more sites.
- CHECKED (S): `E(t)` is computed as an exact rational function (`det(M + 11ᵀ)/det M − 1`, `M = P⁻¹ + tG_S`) for the pair and the cross. It equals the full 125-site law at `t = 1/12`. The three series and the positivity are exact.
- CHECKED (F):
  - `m' = 1`, `1.043834…`, `1.088909…` for the point, the pair and the cross (all at `m = 1`), with three distinct `κ`;
  - the pair's record formed one site over has `m' = 1.042414…`: same `L`, different `g_y`.

**S8 — T4(c) — PROVED, CHECKED (T).**
- `κ = κ₀` ⟺ `m' = m₀`, by S6.
- By F4 and S2, `m' = m₀` ⟺ `L = m₀/(1 + (γ/12)g_y m₀)`.
- With `κ₀` the point record's `κ`, the pair's and the cross's ledgers differ from `L₀(y)`, so they cannot form such a record at `y` with the books kept.

**S9 — T5(a) — PROVED, CHECKED (C).**
- Block 95's rate for a move `x → y` is `w_x^a w_y^{1−a} h/6`, with `log w_z(C) = 6Σ_r λ_r G(z − r)`.
- Take the cycle `C₀ = {1@x, 2@u} → {1@y, 2@u} → {1@y, 2@v} → {1@x, 2@v} → C₀`.
- The heat-bath factors contribute `W(C')/W(C)` per move, which telescopes around the cycle.
- Summing the log-rates forward minus backward:
  - the `G(0)` and self-pair terms cancel;
  - `λ₂` collects `(2a − 1)[G(x−u) − G(y−u) + G(y−v) − G(x−v)]`;
  - `λ₁` collects the negative of the same bracket (`G` even).
- If the chain were in detailed balance with a positive `π`, multiplying `π(C_k)q(C_k→C_{k+1}) = π(C_{k+1})q(C_{k+1}→C_k)` around the cycle would give ratio 1. So `λ₁ ≠ λ₂` with `a ≠ 1/2` and `Δ ≠ 0` excludes detailed balance, and therefore excludes block 95 T2's law.
- CHECKED (C):
  - `G` on `4³` by exact Fourier sums, matching block 95's `257/7680` and `29/7680`, the defining identity at all 64 offsets, and zero sum;
  - the identity symbolic in `λ₁, λ₂, a` for `x = 0`, `y = e₁`, `u = (2,1,0)`, `v = (2,0,0)`, with `Δ = 3/160`.

**S10 — T5(b) — PROVED, CHECKED (C).**
- At `a = 1` record `i` leaves at rate `r_i(d)/12` per allowed direction, with `d = x₁ − x₂`.
- For `π(x₁, x₂) = f(d)`, the inflow at `(x₁, x₂)` is `Σ_{e: d−e≠0} (f r₁)(d − e) + Σ_{e: d+e≠0} (f r₂)(d + e)`, and relabelling `e → −e` in the second sum gives `Σ_{e: d−e≠0} (f(r₁ + r₂))(d − e)`.
- The outflow is `f(d)(r₁ + r₂)(d)·#{e: d + e ≠ 0}`.
- `f = 1/(r₁ + r₂)` balances them, for any positive `r₁, r₂`.
- ASSUMED (classical): an irreducible finite chain has one stationary law. This is used only to call it "the" law.
- The first order is `log(r₁ + r₂) = log 2 + 3(λ₁ + λ₂)(G(0) + G(d)) + O(λ²)`.
- CHECKED (C): global balance with random positive rational `r₁, r₂` on all 4032 states of `4³`, and the first order symbolically.

**S11 — T5(c) — PROVED, CHECKED (C).**
- `v₁ = (1/12)Σ_e e w_{x₁}^a w_{x₁+e}^{1−a}`, with `log w_{x₁+e} = 6λ₁G(e) + 6λ₂G(d + e)`.
- `Σ_e e = 0`, and `Σ_e e G(e) = 0` because `G(e)` is the same for all six `e`.
- So `v₁ = ((1 − a)λ₂/2)Σ_e e G(d + e) + O(λ²)`, and likewise `v₂ = −((1 − a)λ₁/2)Σ_e e G(d + e) + O(λ²)` (`G` even).
- CHECKED (C): symbolic in `a`, at `d = (2,1,0)` on `4³`, where `Σ_e e G(d + e) ≠ 0`.
- This is block 104 T3(a)'s imbalance in block 95's kinetics, where each record's response is one unit per record.

## (3) Where the route stops

**First step that does not go through exactly: carrying T1–T4 into block 95's setting.**
- T1's dictionary is exact in block 56's member, `M_½`. Block 95's exact pair law is in the geometric member.
- Block 55 T4(d) shows that no weight-one bond energy has the geometric member's second order.
- So T5 carries a per-record `λ_r` into block 95's chain only through the first-order dictionary `λ = log κ = −(γ/6)m' + O(γ²)`, which the two members share.
- The exact moving-record chain in block 56's member is not treated.
- For one species of walker, records formed under F differ in `λ` only at order `(γm)²` (T4b). Species of different mass differ at first order (block 77 T4: with its scalar-hop coefficient `a₇₇ ≠ 0` the masses are `√(m² + 36a₇₇²)` and `√(m² + 4a₇₇²)`).

**Other limits.**
- F is a supplied clause (S0).
- `g_y` is the box's. The value in the bulk of large boxes, `1.51639` (block 56's premise), is not re-derived.
- Negative `m'` is treated for one body only.

## (4) What would finish it

1. **A formation clause that fixes `L` per event.** For example, a record forms only by converting exactly `L₀(y)` (T4c), which is a quantum of ledger per record. Or a response law under which a record's motion scales with its energy (block 55 T3's `S/E`), so that different `κ`s still pull equally.
2. **Block 95's chain in block 56's member.**
   - For two bodies in translation-invariant surroundings, block 56 T4 with `a = b = g` gives `φ₁ = (1 + d₂(g − c))/((1 + d₁g)(1 + d₂g) − d₁d₂c²)`, with `c = G(x₁ − x₂)`.
   - For equal `d` this is `1/(1 + dg + dc)`, a symmetric pair function, so the four-move cycle ratio at `a = 1` is 1.
   - For `d₁ ≠ d₂`, the ratio `(φ₁/φ₂)²` depends on `c`, and the same cycle argument applies. This is a direction, not checked here.
3. **The bulk limit `g_y → g₀`**, making `κ` a function of `L` alone off the walls.

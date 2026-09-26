# Mobile-record formation response: the decisive finite facts recovered independently

- **Task:** `J:derive:mobile-record-formation-response:a1`
- **Worker:** `w-jonathonsmac4f50-jea32`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The sources are Codex drafts #8545, #8551 and #8552, so this is a cross-family recovery.
- **Prior attempts.** None existed on `ai/probes` for this problem at claim time. The related `deferred-20260924-formation-packets` attempt covers other packets. The `formation-response-kernel` referee directories on this machine concern a different, admissibility, problem.

## Sources

Frozen heads, with SHA256 values matching `SOURCE_MAP.json`:

| PR | head | file | SHA256 |
|---|---|---|---|
| #8545 | `689941783b` | rare-formation event-law note | `8cc06519…e4e2` |
| | | its runner | `1f64e0a8…1c4d` |
| | | finite-rate note | `423eba32…d917` |
| #8551 | `4de7aa06bb` | empty-start motion-response note | `c23adc34…64d5` |
| | | its runner | `56aeb108…7156` |
| #8552 | `197c05b563` | lifetime/terminal note | `1bbcfc4e…ccad3a8` |

**Read in full:**
- #8545's event-law note;
- #8551's note, §§1–9, including the Dyson coefficient, the remainder and the first-actual-order extension.

**Consulted for scope only:** #8552 and #8545's finite-rate note.

The authors' runners were not used.

## (1) Statement (the task's decisive first check)

- **(a) The six-site witness.** On the 2×3 graph with the six-axis weights `(3/2, 1/2, 1)`:
  - the rare-formation event probability that three records agree right after the third birth is `2701/53880`;
  - the static three-record law gives `73/1440`;
  - the dynamic/static ratio is `444/449`, and the difference `−73/129312`.
- **(b) The finite-ε generator value.** At `ε = 1/1000` the exact value is `2851401694918427/56880888215238000`.
- **(c) The Dirichlet coefficient.**
  - `D₂(b) = 14/5` on the path of 3, `224/5` on the 4-cycle, `0` on the triangle, for both menus.
  - The torus formula `D₂/V = d Σ_ab h_ab² {2(8d − 7)W_ab/(1 + W_ab) + (8d² − 14d + 7)}` holds, with `2379/5` per volume in `d = 3`.
  - The generator-power identities give `E_κ[N_t] − E₀[N_t] = κε⁴D₂t⁵/60 + O(t⁶)`, exactly.
- **(d) What stays open.**
  - A volume-uniform remainder exists at short times. The note's §4 bound is re-derived below.
  - No finite-intensity, all-time response bound is established.
  - All-time mobility monotonicity is neither proved nor contradicted. A small-graph search found no sign change, which is not a no-go.

## (2) Steps

### Step 1 — the slow class process (CHECKED F1; PROVED as in #8545 §2)

- #8545's resolvent argument is re-read and holds as written:
  - the killed generator `Q_C − εD`;
  - the limit `v_ε(h) → π_C/(B̄_C + h)`;
  - the class-to-class rates `K_CD`.
- Implementation, independent of the author's:
  - motion classes are found by breadth-first search on content-preserving vacancy hops, with no sector-connectivity assumption;
  - the class-stationary law is `∝ w`;
  - `K_CD = Σ_s π_C(s) Σ_{t∈D} A(s, t) / B̄_C`;
  - the law is propagated from the empty class through three births.
- Result:
  - `P(E) = 2701/53880` and `μ_{N=3}(E) = 73/1440`;
  - ratio `444/449`: indeed `2701 = 37·73`, so the ratio is `37·1440/53880 = 444/449`;
  - difference `−73/129312`.

### Step 2 — the finite-ε value (PROVED and CHECKED F2)

**The law after the second birth is the static two-record law for every `ε > 0`.**
- The first birth is uniform over sites and contents.
- One record moves by symmetric hops, so its position stays uniform.
- Row sums six make every one-record hazard equal to `6(V − 1)`. So the second birth time is independent of that position.
- The second insertion at `x` next to content `c` has rate `εW(b, c)`, and `ε` otherwise. So each unordered two-record configuration arrives with probability `∝ w(s)`, from its two insertion orders.

**The third birth.** Given this law, the third birth from the two-identical class is `(37/180) · ε α(εD − Q)⁻¹ a_same`, on the 15 positions. At `ε = 1/1000`, exact rational linear algebra gives `2851401694918427/56880888215238000`, as quoted.

### Step 3 — the Dirichlet coefficient (PROVED as in #8551 §§1–3; CHECKED F3, F4)

**Re-derived.**
- `δ₀BH = δ₀B²H = 0`. The one-record hazard is constant, and the two-record stratum of `δ₀B²` is `2w`, which is `H`-stationary.
- Hence `δ₀Lᵏ = εᵏδ₀Bᵏ` for `k ≤ 3`, `δ₀L⁴ = ε⁴δ₀B⁴ + κε³δ₀B³H`, and `δ₀L⁵N − ε⁵δ₀B⁵N = 2κε⁴D₂(b)`.
  - This uses `HN = 0`, the `N = 2` part `−2w(6(2V − 1) + b)` of `δ₀B³`, and detailed balance for the Dirichlet form.

**Exact checks.**
- F4, on the path (343 states), symbolic in `κ` and `ε`: all four identities, with `δ₀L⁵N − ε⁵δ₀B⁵N = (28/5)κε⁴`.
- F3a: brute-force `D₂` gives `14/5`, `224/5` and `0` (triangle), with equal values for the opposite menu.
- F3b: the note's edge reduction, with `b = 6(V − 2) + c_xy h_ab` and conductances `uv/(u + v)`, equals brute force. The torus formula holds exactly on rings of side 6, 7, 8 and on the `6×6` and `7×7` tori, and gives `2379/5` per volume in `d = 3`.

### Step 4 — the ε⁴ coefficient at fixed time (PROVED in #8551 §6; float screen S1)

- `C_κ(t) = (1/3)∫₀ᵗ(t − s)³⟨b, [I − e^{κsH}]b⟩_w ds ≥ 0`. It is increasing and concave in `κ`, by the spectral argument.
- On the path, the closed form `(t⁴/3)[(9/8)ψ(8κt/5) + (3/4)ψ(4κt/3)]` agrees with Richardson-extrapolated full-generator differences, to within 2%.

### Step 5 — the uniform remainder (PROVED, as re-derived from #8551 §4)

- **Local terms.** Split `L` into local terms: births at a site read its `z` neighbours, and hops read the neighbours of both endpoints.
  - The terms that update a support `S` have total rate at most `R_κ|S|`, with `R_κ = 6εu^z + zκ`.
  - Each term enlarges the support by at most `K = 2(z + 1)`.
- **Consequence.** `‖Lᵏf‖_∞ ≤ (2R_κ)^k ∏_{j<k}(1 + jK)` for one-site `f`. Taylor's remainder and contraction then give `|ρ_κ − ρ₀ − at⁵| ≤ Ct⁶`, with `C` independent of `V`.
- **Scope.** This is a short-time statement only.

### Step 6 — the research target's alternative (float screen S2; exploratory)

- **Screened in the checker.** `E_κ[N_t] − E₀[N_t] ≥ 0` for `t ≤ 8` on the path, the star and the 4-cycle, for menus `(3/2, 1/2, 1)`, `(1/2, 3/2, 1)`, `(3, 1/5, 7/10)` and `κ = 1, 50`. No negative value is above rounding.
- **Exploratory, outside the checker.** A sparse scan of the 2×3 graph (117 649 states) was also run. For the ferro menu at `κ = 1` its smallest difference is `−2.3·10⁻¹²` at `t = 6.5`, which is at the integrator's resolution.
- **This is a finite search, not a no-go.**

## (3) Where it stops

- **Recovered, no defect found:**
  - #8545's slow law and six-site witness;
  - #8551's identities, `D₂`, the torus formula, the ε⁴ coefficient and the uniform short-time remainder.
- **The first unresolved step.** A finite-intensity population response bound that is uniform in volume and valid for all times. Equivalently, the sign of `E_κ[N_t] − E₀[N_t]` at all `t`, either proved or refuted by an explicit finite counterexample.
- **Why the note's bound does not reach it.** The Dyson remainder grows with `V`, and the short-time remainder certifies only `t ≤ a/(2C)`.
- **Not re-checked here:**
  - #8551 §5's correlation formulas;
  - §9's first-actual-order extension;
  - #8552's lifetime bounds and terminal correlations (including the positive formation-floor and product-initial-law hypotheses).

## (4) What would finish it

- **(i)** A coupling or monotonicity argument, for example attractiveness in the hazard. It should compare the mobile and immobile processes at all times on a finite graph. Alternatively, a larger exact search, for example exact rational Taylor enclosures on the 2×3 graph, looking for a negative interval.
- **(ii)** For volume uniformity at finite `ε`, a local cluster expansion like #8552's, but for the difference of the two processes.

## ASSUMED

The supplied model of #8545 and #8551: the menu, the row-six pair weights, the rates and the empty start.

## Reproduce

```bash
python3 probes/work/derive/mobile-record-formation-response/w-jonathonsmac4f50-jea32/check.py
```

The run takes about 20 s.

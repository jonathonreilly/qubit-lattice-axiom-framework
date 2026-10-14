# UV-1 report: is the overlap's RP failure a grid-scale effect?

**Reading: OPEN for both arms. The headline (primary arm) is OPEN.**

**Provenance.**
- Claude Opus 5.5 (xhigh), 21:20–22:48Z on 2026-10-14. Same model family as K2, K2c, NT-2 and the panel. Not refereed.
- The harness blocked the worker from writing this file. The supervisor saved it from the worker's final message, lightly condensed; every number and file reference is the worker's.
- **Code:** K2's `lat2d.py`, K2b's `k2b_lib.py` and K2c's `k2c_lib.py`, copied unchanged (sha1 matches), plus the `uv1_*.py` scripts.
- **Memory:** one process at a time, 2 threads, every run under a 0.4 GB watchdog. Largest peak 272 MB (`Bsel_d2_open.out:65`); no watchdog kills.

**Why OPEN.** It was forced, and it was registered in advance (PREREG §3). At finite gauge coupling on a torus, depth t₀ ≥ 2 means an 11- to 19-dimensional integral, and no convergence-checked computation of that fits the budget. All computed evidence points the same way: the negativity is not confined to the reflection plane's own slice. It shrinks steeply with depth but is still present, and converged, at t₀ = 3 and 4.

## 0. Plain words

1. **At the plane itself (t₀ = 1), the violation does not depend on the gauge coupling.**
   - Setup: tori Lt = 12 and 16, four W-matched pools, both arms, β_g = 0, 1, 4, 8.
   - Result: always quadrature-converged negative, at about −2.4e-6 to −6.3e-6 relative. It changes by less than 2% between β_g = 0 and 8.
   - Wilson and pure-gauge controls are PSD on every pool.
2. **One slice deeper (t₀ = 2, open-time proxy, finite β_g), it is still there.**
   - The same 6 witnesses were moved one slice off the plane, and the buffer slice was integrated with an exact-kink nested quadrature.
   - The kernel is negative at every β_g in both arms: −3.2e-6 to −3.4e-6 relative, with a sign margin of 32–800×. That is about 1/57 of the depth-1 value.
   - Integrating over the buffer gauge field barely smooths it: the β_g = 0 and β_g = ∞ values differ by 3%.
3. **On tori in the β_g → ∞ limit (flat field near the plane), it survives to t₀ = 3 and 4, falling fast.**
   - Relative λ_min/λ_max at Lt = 20: −7.8e-6 (t₀ = 1), −5.9e-7 (t₀ = 2), −1.4e-8 (t₀ = 3), −9.5e-11 (t₀ = 4).
   - All converged (E ≈ 3e-13 absolute) and confirmed by a second seed. K2c's independent explicit-link builder reproduces them to every digit.
   - The drop is roughly 13–300× per slice, against only 2.25× per slice for the free overlap's own matrix elements.
4. **What it means.**
   - The violation lives in the overlap determinant itself, not in gauge fluctuations, so it is present even for a flat field.
   - It is lattice-scale: the decay length is about 0.2–0.4 lattice spacings, independent of β_g.
   - It is never exactly zero at finite depth. At fixed lattice depth the data lean to **PERSISTS**, not to UV-ONLY's "vanishes by t₀ ≤ 3".
   - In physical units (t₀·m_S held fixed as β_g → ∞), it would vanish faster than any power (suggested).

## 1. Readings

| Arm | FIXED reading | Basis |
|---|---|---|
| **Primary:** triangle × e^{β(cos p−1)}, which is positive type for all β ≥ 0 (proved; NT-2 choice, PREREG §1) | **OPEN** | no finite-β torus kernel at t₀ ≥ 2 (PREREG §3) |
| **Secondary:** hard × e^{β(cos p−1)} | **OPEN** | same |

Supplementary labels (PREREG §6, F1, F2):

| Item | Result |
|---|---|
| Torus, t₀ = 1 | TORUS1-NEG at every β (0, 1, 4, 8), both arms, Lt 12 and 16, four pools (checked) |
| Open, t₀ = 2 | PROXY-NEG(2) in all 8 (arm, β) cells (checked) |
| β = ∞ comparator, tori | INF-NEG at t₀ = 1, 2 (Lt 12); 1, 2, 3 (Lt 16); 1, 2, 3, 4 (Lt 20) (checked). Robust at the deepest cells across two seeds. The 2-slice witness families (Lt 12 at t₀ = 3; Lt 16 at t₀ = 4) are PSD, with no power. |
| Continuity (proved by the worker; unrefereed) | For any pool whose β = ∞ kernel is negative at depth t₀, both arms' finite-β depth-t₀ kernels are non-PSD for every β above some β₀. |

**The continuity argument.**
- The weights concentrate at p = 0, since both profiles are 1 there and continuous.
- det D_ov is bounded and continuous at the flat point (min|eig H_W| ≥ 0.78 there).
- The diagonal entries tend to positive limits, and eigenvalues are continuous.

So "PERSISTS at fixed lattice depth for large enough β_g" holds in substance. But β₀ is not computed, so the literal FIXED reading stays OPEN.

## 2. What was computed

**Stage A (torus, t₀ = 1).**
- Pools: K2c's hard pools at Lt 12 and 16; the lattice panelist's triangle pool at Lt 12; a new β = 8 primary-arm search pool at Lt 12.
- One determinant pass per level covers every β and both arms. The nodes carry the union of both arms' kinks, which is an exact identity.
- Validation V0: hard β = 0 gives −1.4728e-4 (= K2c; `A12h_d1_torus.out:46`), and triangle β = 0 gives −1.4335e-4 (= panelist; `A12t_d1_torus.out:42`).

**Stage B (open Lt = 12, t₀ = 2).**
- Witnesses: the 6 K2c configurations with the largest weight in the negative eigenvector (indices 12, 16, 17, 19, 9, 10), shifted one slice deeper.
- Integration: slice 1 and its mirror are integrated over 4 buffer plaquettes plus the crossing angle.
- Each 1D integral is split at every kink of the inner integrated function (multiples of δ), so the integral is exact piecewise-analytic. Levels n = 2, 3, 4; the n = 3 and n = 4 polytope volumes agree exactly.
- Validation V-B0: the operator matches the direct builder to 0.0, plaquettes match exactly, and log det matches to 3.6e-15.

**Follow-ups F1 and F2.**
- **F1-a (β = ∞ comparator):** tori Lt 12, 16, 20 at t₀ = 1..4, with a W-matched greedy search per cell. The Polyakov integral uses levels nw = 8, 12, 16.
- **F2-a:** second seeds with K = 24 for the deepest cells.
- **F2-d (V-INF):** K2c's independent builder, copied verbatim, reproduces:
  - Lt 20, t₀ = 4: −1.50797e-9 (main code −1.5080e-9);
  - Lt 16, t₀ = 3: −1.53158e-8 (main code −1.5316e-8);
  - crossing plaquettes at 4e-16.
- **F2-b:** the free overlap's time locality is ν = 0.81 per spacing.

## 3. Key numbers

Values are relative λ_min/λ_max; E is the absolute error estimate.

**Torus, t₀ = 1** (`*_d1_torus.out:42-49`):

| Pool | Triangle, β = 0 → 8 | Hard, β = 0 → 8 |
|---|---|---|
| A12h | −6.195e-6 → −6.174e-6 | −6.332e-6 → −6.228e-6 |
| A12t | −6.162e-6 → −6.142e-6 | −6.291e-6 → −6.193e-6 |
| A16h | −5.005e-6 → −4.985e-6 | −5.131e-6 → −5.035e-6 |
| A12s8 | −2.414e-6 → −2.408e-6 | −2.448e-6 → −2.422e-6 |

- The smallest margins are about 11–12× (triangle arm, β = 8). They come from the conservative registered estimator E = k·(lo → hi change); the hi → third change q₃ is only 1.4e-9.
- Controls: W between +2e-15 and +3e-9; PG about −3e-15; all PSD.

**Open, t₀ = 2, same 6 witnesses** (`Bsel_d2_open.out:56-63`):

| Arm and β | Depth 1 | Depth 2 | E (depth 2) |
|---|---|---|---|
| Triangle, β = 0 | −1.92e-4 | −3.35e-6 | 2.8e-7 |
| Triangle, β = 8 | −1.91e-4 | −3.38e-6 | 6.3e-7 |
| Hard, β = 0 → 8 | about −1.93e-4 | −3.24e-6 → −3.31e-6 | — |
| β = ∞ comparator | −1.91e-4 | −3.45e-6 | — |

- The depth-2/depth-1 ratio is 0.0175–0.0177.
- Depth-2 controls: W between −1.6e-11 and +9.5e-11 (within E); PG −1e-15.

**β = ∞, tori** (`INF_torus_*.out:18`; second seeds in `INF2_*.out:26`):

| Lt | t₀ = 1 | t₀ = 2 | t₀ = 3 | t₀ = 4 |
|---|---|---|---|---|
| 12 | −5.11e-6 | −3.38e-8 | PSD (no power) | — |
| 16 | −4.81e-6 | −3.08e-7 | −9.82e-10 (seed 2: −2.77e-9) | PSD (no power) |
| 20 | −7.80e-6 | −5.92e-7 | −1.42e-8 (seed 2: −3.32e-8) | −9.46e-11 (seed 2: −1.52e-10) |

- E ≤ 5.2e-13 absolute everywhere; Wilson PSD everywhere.
- Per-slice rate κ at Lt = 20: 2.6, 3.7, 5.0. These come from searched pools, so they are indicative only.

**Against the qinfo panelist's frame** (`statement.md:276-281`).
- The violation falls with t₀, at a lattice-scale rate.
- It does **not** fall with β_g at fixed t₀ (β = 0 through ∞). So the scale that confines it is the overlap kernel's, i.e. the grid's, not the Schwinger length.
- **For set B (reading):** exact OS reconstruction fails at every depth in this proxy. An approximate transfer matrix for coarse-grained observables, with errors of order e^{−κt₀}, is plausible but not shown. The exact exits stay X3's: Π-W, or 5D fermions without PV fields.

## 4. Deviations

- **PREREG.** The main text was written 21:33–21:37Z, before any run. F1, F2 and F2-d were appended later and dated. Their header times ran a few minutes ahead of the clock; this is corrected inside the file.
- **Not in the original registration:** the β = ∞ comparator (F1-a) and the continuity argument. The headline OPEN rests only on registered items.
- **A bug, caught before use.** The depth-2 code subtracted the buffer x-link hops at angle 0. Validation V-B0 flagged a 6e-2 mismatch before any kernel was computed; the run was killed, fixed, and V-B0 then passed exactly. The killed output is kept as `Bsel_d2_open_KILLED_bugfound.out`.
- **Queue scripts.** `chainC.sh` and `chainD.sh` died silently. The Stage B child they had started finished normally under its watchdog, and the remaining jobs were run by hand.
- **Not run:**
  - the finite-β Lt = 20 search A20s8 (β = ∞ covers Lt = 20);
  - the B-rand pool;
  - the optional coarse torus run at t₀ = 2;
  - t₀ = 3 and 4 at finite β (infeasible, as registered).

## 5. Files (`panelwork/UV1/`)

- `PREREG.md`
- `scripts/`:
  - code: `uv1_lib`, `uv1_d1`, `uv1_d2`, `uv1_inf`, `uv1_inf_verify`, `uv1_search`, `uv1_locality` (`.py`), plus `capped.sh` and `chain*.sh`;
  - copied: `lat2d.py`, `k2b_lib.py`, `k2c_lib.py`;
  - outputs: `A12h/A12t/A16h/A12s8_d1_torus.out`, `Bsel_d1_open.out`, `Bsel_d2_open.out` (and the killed run), `INF_*.out`, `INF2_*.out`, `VINF_*.out`, `LOC_free_overlap.out`, `A12s8_search.out`;
  - pools: `pool_UV1_*.npz`, plus copies of the K2c and panelist pools.

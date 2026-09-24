# deferred-20260924-spin-packets, first pass: PR8839's saved high-spin vectors, provenance recovered and replay reproduced independently

Worker `w-macbookpro9927a-j9ca8` (`claude-opus-5-5`), unit `J-derive-deferred-20260924-spin-packets-a1`.

- origin/main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`.
- Landing snapshot `c288aa9cfe`; batch 13 landed in `d7a3aa92b0`.
- Status file: [`RECOVERY_STATUS.json`](RECOVERY_STATUS.json). It lists 12 deferred sources, each with its SHA256 re-verified from the frozen head `8ccef7097d`.

**Provenance and independence.**
- **The finding.** Batch 13's review finding U13-R3 (PR8839) reads: "The actual-output check consumed historical high-spin saved-vector files." Its resolution: "Explicitly defer saved-vector replay and identify its tables as historical diagnostics."
- **What I read.**
  - On origin/main, the landed notes *Controlled components and second-birth bounds for the actual first output* and *A prepared post-formation sector retaining electric dynamics and another birth*. The model's definitions come from the second.
  - Among PR8839's deferred files:
    - the follow-up's scope, script, results and the four vector files;
    - the actual-output author controls and stdout;
    - the initial probe's scope and script.
- **Related problem inspected.** `composite-bodies-rest-energy-without-a-larger-site-algebra` has a3 (other machine) and a4 (this worker machine, issue #8733). It concerns the rest energy of composite bodies and does not overlap this replay.
- **Independence of the rebuild.**
  - The model below is rebuilt from the landed notes' text.
  - The frozen builders (`finite_spin_dynamics_check.py`, `flat_band_spin_correction_probe.py`) and the table `FLAT_COMPRESSED_OPERATORS_RESULTS.json` are read only to check the provenance chain by hash. They are never imported or evaluated.

## 1. What is attempted

**Residual.**
- (i) The provenance of the saved vectors `PROPAGATED_S{64,96,128,192}.npz`.
- (ii) An independent reproduction of the actual-output diagnostic that the landed note quotes: "At S=192, t=1.2, K=.4, delta=.7, kappa=.3, the |f|<=2 flat-window density differs from its predicted component by about 2.06e-4 in trace norm; the complementary probability in that window is about 1.24e-8". The reproduction covers the whole deferred window table behind it.
- (iii) What these numbers add beyond the landed analytic bounds.

**Model, rebuilt from the prepared-flat-sector note.**
- **Sites and fields.** Sites are `0..7` on a ring, with `A` = even sites carrying Gauss background 1. A word is `(q, f)`, with `q_a ∈ {−1, 0, 1}` and circulation `f = E_7`. The fields are `E_e = f + Σ_{b≤e}(q_b − [b even])`.
- **Moves.**
  - A record hops to an empty neighbour with coefficient `−g_{S,k}(E)`, where `g = √[1 − E(E+k)/(S(S+1))]_+`, `k = −(direction)·charge`, and only `|E + k| ≤ S` is allowed.
  - A birth on a link with both ends empty places `σ, −σ` with amplitude `g_{S,σ}(E)`.
- **Sectors and operators.**
  - `P` is the six-record sector with every A site occupied. `Π_1` and `Π_2` have one and two A sites empty.
  - `A = Π_1TP` and `Z = Π_2TΠ_1TP`.
  - `H2 = −A†A` and `H4 = (A†A)² − Z†Z/2`.
  - `Γ = Σ_{e,σ}(j_{e,σ}A)†(j_{e,σ}A)`.
- **The generator.** `η(H2 + 4) + δH4 − iκΓ/2`, with `η = KS(S+1)` and `(K, δ, κ) = (.4, .7, .3)`.
- **The flat basis (4).**
  - `|C, r, f⟩` has the occupied B pair `C` on the B ring (`B_i` = site `2i+1`), and the minus at the `r`-th occupied site counted from `A0`.
  - `a_(r,f) = (|01,r,f⟩ − |23,r−1,f+c0(r)⟩)/√2` and `b_(r,f) = (|12,r,f⟩ − |03,r,f⟩)/√2`.
- **The limit.** `φ(t) = exp[−it(K P0D2P0 + δP0H4P0 − 2iκ)]φ(0)`, with the note's electric table and H4 action (6).
- **Window quantities.**
  - For `R_N`, the projection onto flat basis vectors with `|f| ≤ N`, the density error is `‖R_N|ψ_t⟩⟨ψ_t|R_N − R_N|φ_t⟩⟨φ_t|R_N‖₁ = √((a+b)² − 4|c|²)`.
  - The complementary weight is `‖R_N U_S(t)χ‖²`, where `χ = ψ − Fψ`.

**Claims.**
- **R1 (provenance; exact, hashes).**
  - The four vector files hash to the values recorded in `DECOMPOSITION_RESULTS.json`.
  - That file records the hash of `unprepared_decomposition_check.py`, whose source matches it.
  - The script asserts builder hash `5030a960…`, and the builder blob at the frozen head has that hash.
  - The builder asserts the flat-module hash `50df6b9c…`, which matches.
  - The script's seed line is `psi = |(0,3),1,1>`, and its parameters are `(K, δ, κ) = (.4, .7, .3)`.
- **R2 (the seed is the actual first output; exact).**
  - Start from the four-record all-A-plus state with every link zero. For the mark (link 0, σ = +1), the only hop-then-birth path is the hop `0 → 7` across the cut, then the birth on link `(0,1)`. Both amplitudes are 1.
  - The output is `|03,1,1⟩ = (+,−,+,0,+,0,+,+), f = 1`, for every `S ≥ 1`. The landed note says "for every sufficiently large S".
  - Its flat part is `−b_(1,1)/√2`, of weight exactly `1/2`.
- **R3 (the flat-sector algebra, independently; exact).** In my labelling, on all twelve types:
  - `A†A = 4`;
  - the H4 action (6) holds;
  - the electric compression is diagonal with the note's `d_a`, `d_b`;
  - `Γ = 4` on `P0`.
- **R4 (the replay; floating point).**
  - My P spaces equal the saved word sets, with dimensions 4584, 6888, 9192 and 13800.
  - My propagations equal the saved vectors to `≤ 10⁻¹²` at `t = 0, .4, .8, 1.2`.
  - All 48 finite-window rows of `ACTUAL_OUTPUT_CONTROLS.json` (S = 64..192, N = 1, 2, 8, four times) are reproduced: to relative `5·10⁻⁸` where the value is at least `10⁻¹²`, and to absolute `2·10⁻¹⁶` for the rounding-level rows at `t = 0`.
  - The headline row, at `S = 192`, `t = 1.2`, `N = 2`: trace-norm error `2.0556·10⁻⁴`, complementary weight `1.2398·10⁻⁸`.

**What the replay adds beyond the landed bounds.** The landed statements (2), (6) and (7) are limits as `S → ∞`, with no rate for the actual output. The replay gives their finite-S sizes at these four spins and times.
- The interference term is at most `4.3·10⁻⁵`.
- For windows with `N ≤ 2`:
  - the density errors are `10⁻⁴`–`10⁻³`;
  - the complementary weights are `10⁻⁹`–`3·10⁻⁶`, and at `N = 2` they are not monotone in `S` (`S = 128` is the largest).
- The `N = 8` window's complementary weight falls from `2.2·10⁻⁴` to `5.1·10⁻⁶`.

This is consistent with the landed limits. It gives no rate, no uniform bound and no limit law, and "historical vectors alone do not establish a uniform theorem". There is no new theorem here, so no HIT.

## 2. The steps

1. **CHECKED (Q): sources and the provenance chain.** The check covers:
   - the SHA256 of the 12 deferred sources in the status file;
   - the chain in R1;
   - the landed sentences (the S = 192 diagnostic and "The archived high-spin saved-vector replay remains a historical diagnostic");
   - the prepared note's basis, table and H4 lines;
   - the U13-R3 resolution.

2. **PROVED + CHECKED (X2): the seed.**
   - The state `(+,0,+,0,+,0,+,0)` with `f = 0` has every `E_e = 0`.
   - A birth on link `(0,1)` needs sites 0 and 1 empty. Site 0 must be vacated by a hop. Its only target that keeps site 1 empty is site 7, across the cut. That hop raises `f` from 0 to 1, with amplitude `g(0) = 1`.
   - After the hop, `E_0 = 1 + (0 − 1) = 0`, so the birth has amplitude `g(0) = 1`. Both moves need only `S ≥ 1`.
   - The landed note (§5) shows the pre-mark no-event dynamics on this input is scalar. So the normalized first output for this mark is this configuration.
   - Only `b_(1,1)` contains `|03,1,1⟩`, so `P0ψ = −b_(1,1)/√2`.
   - Checked with exact fractions at `S = 1, 2, 3, 8, 64, 96, 128, 192`.

3. **CHECKED (X1): the flat-sector algebra.** Integer path enumeration in my own labelling covers all twelve types at `f = −3, 0, 2, 5`:
   - `A†A = 4`;
   - H4 as in (6);
   - the electric compression equals `d_a`/`d_b`, with no other flat element within `f ± 3`;
   - `Γ = 4` on `P0`.

4. **CHECKED, floating point (N1): the replay.**
   - The build includes the physical Gauss intervals, and the hop is checked hermitian.
   - Propagation uses `scipy.sparse.linalg.expm_multiply` (centered generator, both columns `Fψ`, `χ`).
   - Comparison is by word keys with the saved vectors.
   - The flat limit is computed at cuts 48 and 64. They agree to `3.6·10⁻¹³`, the propagator's tolerance; the truncation tail is `~10⁻³²`.
   - Every window row is compared with the historical table.

5. **ASSUMED.**
   - The supplied model of the landed notes.
   - Floating-point propagation is not an interval enclosure. Agreement with the saved vectors to `10⁻¹²`, by an independent code path, is corroboration, not proof.

## 3. Where it stops

- The first step that fails, for turning the replay into a statement, is a rate.
  - The landed prepared-sector proof gives a nonoptimal `η^{−1/7}` bound for flat inputs.
  - Nothing bounds the actual output's window error or the complementary window weight at finite `S`.
  - The reproduced numbers are not monotone in `S`, so they do not even suggest a clean rate at these spins.
- **Not replayed.**
  - The initial `S ≤ 64` probe, including the coherent-instrument seed `(|03,1,1⟩ + |03,0,1⟩)/√2`.
  - The cube groups of PR8839.

## 4. What would finish it

1. **A quantitative window bound for the actual output.** For example, the prepared bound for `φ` plus a bound on `‖R_N U_S χ‖`. The replay would then check an explicit inequality rather than illustrate a limit.
2. **The same replay for the initial probe and the coherent seed.** This is cheap with the rebuilt model.
3. **PR8839's cube groups, then PR8831, PR8943 and PR8832,** as ranked in the status file.

## 5. Running it

```
python3 probes/work/derive/deferred-20260924-spin-packets/w-macbookpro9927a-j9ca8/check.py
```

- There are four checks. Q and X use exact integers and fractions; N is floating point.
- It runs in about 5 minutes, mostly the `S = 192` propagation.

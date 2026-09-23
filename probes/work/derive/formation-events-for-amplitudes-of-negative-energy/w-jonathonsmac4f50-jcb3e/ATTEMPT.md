# formation-events-for-amplitudes-of-negative-energy, attempt a2: the observation holds; negative amplitudes need several records

**Provenance.** Written by Claude Opus 5.5 (`claude-opus-5-5`), worker `w-jonathonsmac4f50-jcb3e`, task
`J:derive:formation-events-for-amplitudes-of-negative-energy:a2`. There were no prior attempts at claim time. Blocks 60, 67
and 71 were supervisor-run in the same model family. I read the three notes on their PR branches (block 71's T3, block 67's
T1–T3, block 60's member) before starting. The parked statistical postulate is neither used nor approached. No rule of
formation is assumed.

## 1. What is claimed

**Setting.** Blocks 60, 67 and 71 (supplied and not adopted):
- Bodies are at rest in a box with held walls.
- The lengths are `χ = 1 + Σ_x Q_x g_x`, with `g = (−Δ)⁻¹` and the walls at 0. The ledger is `8K ΣQ`.
- The field exists with positive rates iff `χ > 0` and `L = −Δ + Q/χ` is positive definite, walls held (block 71 T3(d)).

**(a) The supervisor's observation holds, and a many-body bound makes it a theorem.**
- **The bound (PROVED).** In any admissible field whose charges are all `≤ 0`, **every record has `Q_i > −1/(2g_ii)`**.
  This is block 71 T3's one-body bound, extended to many bodies.
- **The consequence.** A spread negative amplitude with `ΣQ_x < −1/(2g_yy)` for every `y` has no ledger-keeping single
  record. By block 67 T1 the record would need `Q' = ΣQ_x`, and that is inadmissible.
- **An exact example** on the 27 interior sites of a `5³` box: take `Q_x = −1/5` at every site.
  - Each charge is on its own admissible branch.
  - The amplitude's own field exists: `min χ = 71/85`, and all 27 leading minors of `L` are positive.
  - Its total `−27/5` is below every site's threshold. The lowest threshold is `−952/353 = −2.697`, at the corners.
  - No single record of charge `−27/5` is admissible at any site, which is checked directly.

The unit's HIT conditions are therefore **not** met. A single record would keep the ledger only if the amplitude's own
field failed to exist, and here it exists.

**(b) The best single record.**
- **The ledger.** The record must stay above its site's threshold, so the ledger **rises** by more than
  `8K(|ΣQ| − 1/(2g_min)) = 8K × 4771/1765 ≈ 21.6K`.
- **Lengths.** The walls see the monopole jump from `ΣQ = −27/5` to `Q' > −952/353` (block 67 T2(a) with `h = 1`).
- **Clocks.** The wall flux of the clocks, `P' = Q'/(1 + 2Q'g_yy)`, runs to `−∞` as `Q'` approaches the bound. That is
  block 71 T3's zero mode. The record that is best for the ledger is singular for the clocks.
- **The spread amplitude, by contrast,** has positive rates everywhere and a finite clock flux (`ΣP = −80563212984/13096947245 ≈ −6.15`).

**(c) How many records.**
- **The bound.** Summing the bound over records gives `|ΣQ| < Σ_i 1/(2g_ii) ≤ n/(2g_min)`. Keeping the ledger therefore
  needs **`n > 2g_min|ΣQ|`**.
- **In the example** that is `2.0023`, so at least 3 records are needed. Three records of charge `−9/5` at three corners
  are admissible (exact), so **the minimum is 3**.
- **In general** the count grows like `2g_min|ΣQ|`. A positive amplitude always needs just one (block 67 T1).

**(d) What the asymmetry means for the fork "which amplitudes are present".** No rule is proposed. The observation is
this:
- **Positive amplitudes can always be condensed.** A positive amplitude, however spread, can be condensed into a single
  record with the ledger kept.
- **Negative amplitudes cannot, past a size.** A negative amplitude whose total charge exceeds `1/(2g_min)` in magnitude
  cannot. It can be recorded, with the ledger kept, only as at least `2g_min|ΣQ|` separate records.

Whatever selects which amplitudes are present, that selection meets a sign asymmetry in how their energy can be booked as
records.

## 2. Steps

1. **ASSUMED — the setting.** Blocks 60, 67 and 71 as supplied: the member, the ledger, the rates' operator with walls held,
   and block 71 T3(d)'s positivity criterion.

2. **CHECKED (A1) — the example.** The Green function is an exact rational inverse. Positivity is checked on all 27 leading
   minors. The thresholds `−1/(2g_yy)` range from `−952/353` (the corners) to `−51/22` (the centre).

3. **PROVED (A2) — the many-body bound.** Let all `Q_x ≤ 0`, `χ > 0`, and `L` be positive definite.
   - **Test `L` on `g_i`.** `g_iᵀLg_i = g_iᵀ(−Δ)g_i + Σ_x (Q_x/χ_x)g_i(x)² = g_ii + Σ_x (Q_x/χ_x)g_i(x)² > 0`.
   - **Keep one term.** Every term of the sum is `≤ 0`, so dropping all but `x = i` gives `g_ii + (Q_i/χ_i)g_ii² > 0`. That
     is `Q_ig_ii > −χ_i`.
   - **Bound `χ_i`.** `χ_i = 1 + Σ_x Q_xg_xi ≤ 1 + Q_ig_ii`, because `g ≥ 0` and the other charges are `≤ 0`.
   - **Combine.** `Q_ig_ii > −χ_i ≥ −1 − Q_ig_ii`, so `Q_i > −1/(2g_ii)`. ∎
   - `g ≥ 0` is the discrete maximum principle for `(−Δ)⁻¹` with Dirichlet walls (standard; ASSUMED).
   - The identity for `g_iᵀLg_i` and `χ_i ≤ 1 + Q_ig_ii` are verified on the example at every site.

4. **PROVED / CHECKED (B1).** The jump bound follows from step 3 with `n = 1`. The divergence of `P'` is block 67 T3(d)'s
   formula at block 71's bound (sympy limit). The spread amplitude's rates are solved exactly.

5. **PROVED / CHECKED (C1).** Sum step 3 over the records. The three-corner field is checked exactly.

## 3. Where the route stops

- **Charges of both signs.** The bound needs all charges `≤ 0`. With some charges positive the test-vector argument loses
  its sign control, and mixed amplitudes are not treated.
- **Unequal splits and other boxes.** (c)'s minimum is exact for the example. The general count is stated as the bound
  `n > 2g_min|ΣQ|`, and whether it is always attained is open.
- **The walls' view.** It is taken through block 67's identities, which are carried to negative charges without new proofs
  beyond the monopole and the clock flux formula.

## 4. What would finish it

1. **The minimal record count in general.** Decide whether equal charges at the most separated sites always attain
   `⌈2g_min|ΣQ|⌉` (plus one when that is an integer). This is a covering problem for the thresholds.
2. **Mixed-sign amplitudes.** Do they have a ledger-keeping single record whenever their total is positive?

## 5. Running it

```
python3 probes/work/derive/formation-events-for-amplitudes-of-negative-energy/w-jonathonsmac4f50-jcb3e/check.py
```

It needs `sympy`. It runs 4 exact checks in about a second. There is no HIT line: the unit's HIT conditions are not met.

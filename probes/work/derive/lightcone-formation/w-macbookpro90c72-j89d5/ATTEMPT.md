# lightcone-formation, attempt 4 (worker w-macbookpro90c72-j89d5, model grok-4.6)

Structural route, independent of a2 (FSS), a5 (sphere Dobrushin), a6 (`{E,14-E}`), a1 (six-axis `7c`).

## (1) The statement attempted

The 7-stencil (or even truncated-star) Gibbs law `π∝∏_x Z(S_x)` is **range-2**, not nearest-neighbour: the one-site conditional at `x` depends on next-nearest sites through `Z(S_y)` for neighbours `y` of `x`. On a 3-site path at `(3,1,2)`,
`P(s_0=+z|s_1=+z)` equals `13/72` if `s_2=+z` and `1/6` if `s_2=+y`; the static nn-Gibbs conditional is `1/4` and ignores `s_2`. Therefore block 19's reflection positivity and infrared bound, which are for the nn interaction `β s·s'`, do **not** transfer to `π`. The linear kernel identity `C=7/(2E(1-E/14))` still holds.

## (2) Steps

**Step 1 — linear identity (PROVED; CHECKED as E1).**

**Step 2 — range-2 specification (PROVED; CHECKED as E2).** `log π = ∑_x log Z(S_x)`; `S_y` for `y∼x` contains sites at distance 2 from `x`.

**Step 3 — RP does not transfer (PROVED).** RP in block 19 uses the nn Boltzmann weight. A range-2 star potential requires its own RP proof (not supplied).

## (3) First failing step

RP/Gaussian domination for this range-2 spec is not proved; LRO is not obtained.

## (4) What would finish it

RP through a bond plane for `∑ log Z(S_x)`, or a counterexample that the spec is not RP.

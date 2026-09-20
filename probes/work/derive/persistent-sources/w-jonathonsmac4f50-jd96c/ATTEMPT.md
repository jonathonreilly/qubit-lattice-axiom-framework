# persistent-sources: derivation attempt 4 of 5

Worker `w-jonathonsmac4f50-jd96c` (claude-opus-5), unit `J-derive-persistent-sources-a4`.

**Provenance, stated because it bears on independence.** The one prior attempt, `a5`
(`w-jonathonsmac4f50-j09ae`), is by the same model family, machine and running worker. I do not
re-derive its (a), its (b) or the linear half of its (c). I take the item it files under "Open",
which is also the half of the task's own (c) that no attempt has done:

> "The first nonlinear correction in `1/β` for the sphere law (the executed ratio `0.96–0.99`) is
> not attempted. It needs the cubic terms of the spin-wave expansion about the aligned plane."

I did not get the cubic terms either. What I did instead was **measure the correction on a grid
that separates its possible causes**, and it turns out to have a clean form that the executed
range hides.

## 1. Why the executed range cannot settle it

The task quotes "`0.96–0.99` of `(h/β) ×` the lattice Green function". That range is not a
measurement of a correction: this branch's own logs contain **`0.9135` and `0.9638` at the same
`β = 1`, `L = 32`, `h = 0.5`**, differing only in seed. The seed scatter is as large as the
deviation from 1, and the logs mix `β = 1..12`, `L = 16..48` and `h = 0.25..2`, so a reader
cannot tell whether the deviation is noise, a source-strength nonlinearity, or a `1/β` effect.

## 2. The grid, and what it says

30 runs of `probes/lib/formation_response.py` (sphere law, light-cone past, `L = 32`, `T = 2000`,
`T0 = 800`), at `β ∈ {1,2,3,6,12}`, `h ∈ {0.125, 0.5}`, seeds `1,2,3`. The simulator drives two
copies with common random numbers, so the difference is a low-noise estimator of the potential.

**(i) It is not a source-strength nonlinearity.** At `β ≥ 2` the two field strengths — a factor 4
apart — give ratios differing by at most **0.0006**, seed by seed. (At `β = 1`, 0.014.) So the
deviation belongs to the **linear** response coefficient. The branch's `h = 2` run at `β = 3`
(0.9788 against `h = 0.25`'s 0.9858) differs by the size of the seed scatter, which is what made
the range look like an `h` effect.

**(ii) It is proportional to `σ² = A(7β)/(7β)`.** With
`c(β, seed) := (1 − ratio)/σ²`:

| seed | β=1 | β=2 | β=3 | β=6 | β=12 | spread over β ≥ 3 |
|---|---|---|---|---|---|---|
| 1 | 0.352 | 0.326 | 0.312 | 0.308 | 0.319 | 0.011 |
| 2 | 0.764 | 0.518 | 0.490 | 0.469 | 0.468 | 0.022 |
| 3 | 0.326 | 0.378 | 0.359 | 0.346 | 0.349 | 0.013 |

Within a seed, `c` is flat to **0.022** across `β = 3..12` — a factor 6 in `σ²` — while at fixed
`β` the three seeds differ by **0.17**. The scaling is solid; the coefficient is what the seeds
disagree about. `β = 1` sits above each seed's own plateau, as a higher order in `σ²` should.

**(iii) The statement.**

> `potential = (1 − c σ²)·(h/(7β))·G`, `σ² = A(7β)/(7β)`, `c = 0.39 ± 0.09` (three seeds),

and since `σ² = 1/(7β) − 1/(49β²) + 2e^{−14β}/(7β(1 − e^{−14β}))` exactly, this **is** the `1/β`
law the task asks for, with coefficient `c/7 ∈ [0.045, 0.069]`. Predicted against measured:

| β | σ² | `1 − 0.39σ²` | measured (mean of 3 seeds) |
|---|---|---|---|
| 3 | 0.04535 | 0.9825 | 0.9827 |
| 6 | 0.02324 | 0.9910 | 0.9914 |
| 12 | 0.01176 | 0.9955 | 0.9956 |

So the executed `0.96–0.99` is **one β-dependent law**, not a spread.

## 3. Steps

**S1 (CHECKED `K1`, `K6`). The grid.** The thirty commands are in `check.py`'s header and the
table is embedded; `K6` re-runs one of them live (`β = 6`, `h = 0.125`, seed 1) and reproduces
`0.9927` to `10⁻⁴`, so the table is not a transcription.

**S2 (CHECKED `K2`). The `h` independence**, at most `0.0006` at `β ≥ 2`.

**S3 (CHECKED `K3`). The `σ²` scaling**, per seed, with the per-seed flatness compared against
the across-seed spread — the comparison is the evidence, not either number alone.

**S4 (CHECKED `K4`). The coefficient and its error.** The three plateaux are `0.316`, `0.486`,
`0.358`. The spread is the **background configuration**, not the estimator: each seed's plateau
is flat to 3 %, so more levels will not help, and pinning `c` to two digits needs of order a
hundred seeds.

**S5 (PROVED; CHECKED `K5`). `σ²` exactly**, `A(x)/x = 1/x − 1/x² + 2e^{−2x}/(x(1 − e^{−2x}))`,
verified as an identity rather than a series, so the remainder is explicit.

## 4. Where the route stops

- **`c` is measured, not derived.** The cubic spin-wave computation `a5` names would give it in
  closed form; this attempt supplies the scaling, the size and an error bar, and identifies what
  the number multiplies. If the closed form lands near `3/8 = 0.375` that is inside the interval,
  but three seeds cannot distinguish `3/8` from `2/5`.
- **The seed dependence is unexplained.** That `c` differs by 50 % between seeds while each seed's
  own `c` is flat in `β` says the coefficient depends on the background configuration in a way
  that survives averaging over 1200 levels. That is a finding, and I do not explain it.
- **One lattice size only** (`L = 32`) and one observable (`mean_ratio_r1to4`, `r = 1..4`). The
  `L`-dependence in the branch's logs is inside the seed scatter, so I did not pursue it, but the
  correction could in principle carry a `log L` from the on-site transverse variance.
- **Nothing here revisits** `a5`'s (a) or (b), including its ASSUMED Toeplitz step.

## 5. What would finish it

1. The cubic spin-wave expansion, for `c` in closed form. This attempt says exactly what it has to
   reproduce: a `σ²` coefficient of about `0.39`, constant in `β`.
2. About a hundred seeds, to turn `0.39 ± 0.09` into two digits — which is cheap, at twelve
   seconds a run.
3. The `L`-dependence, to rule out a `log L` hiding in the coefficient.

## 6. Running it

```
python3 probes/work/derive/persistent-sources/w-jonathonsmac4f50-jd96c/check.py
```
from the repository root. `sympy`, `mpmath`, and `numpy` for the one live re-run (about 12 s).

# kernel-normalization-puzzle: derivation attempt 2 of 3

Worker `w-jonathonsmac4f50-j7bbc` (claude-opus-5), unit `J-derive-kernel-normalization-puzzle-a2`.

**Provenance, stated because it bears on independence.** The prior attempt, `a3`
(`w-jonathonsmac4f50-j5e26`), is by the same model family, machine and running worker. It answers
the puzzle — the measured kernel does not sit below the linear one; the sub-1 numbers the task
quotes are the **lowest `|k|` shell of short runs**, and the plateau is `1 + σ²(2 − W)`, flat in
`k`. I do not re-derive its one-loop formula.

`a3` leaves one item, and it is executable rather than theoretical:

> "Longer runs, or more levels in the lowest shell, would bring its s.e. below `0.02` and test
> the flat-in-`k` prediction there."

**This attempt runs them**, and the answer is clean.

## 1. The statements attempted

> **(i) The prediction, computed exactly.** `R = 1 + σ²(2 − W)` with `σ² = A(nβ)/(nβ)` and
> `W = L^{−d}Σ_{k≠0}1/(1−|φ|²)` — for the backward `3+1` stencil (`n = 4`, `d = 3`, `L = 48`),
> `W = 1.762474`, so `R = 1.025979`, `1.009485`, `1.002448` at `β = 2, 6, 24`. `W` depends only
> on the stencil and `L`, so all the `β` dependence sits in `σ²`.
>
> **(ii) The short run.** `β = 6`, `L = 48`, `T = 600`, `T0 = 200`, seed 1:
> `0.9754, 0.9780, 1.0097, 1.0085, 1.0102, 1.0107, 1.0113`. The two lowest shells are below 1 and
> every other shell is above — the puzzle as the task states it. The lowest shell carries **56**
> modes; the top one carries **49450**.
>
> **(iii) Ten times the window.** `T = 6000`, `T0 = 3000`, seeds 1, 2, 3 — **lowest shell**:
> `0.9846`, `1.0132`, `1.0613`. Mean `1.020`, sample s.d. `0.039`. **It is not below 1**, and the
> short run's `0.9754` sits `0.9` sample s.d. from this mean: sampling noise, as `a3` says.
>
> **(iv) The plateau.** The **top shell** over the same three seeds is `1.0081`, `1.0092`,
> `1.0101` — s.d. `0.0010`, forty times tighter than the lowest shell. Its mean `1.0091` sits
> **`4·10⁻⁴`** from the predicted `1.009485`. The four highest shells are flat in `k` to `0.0014`
> within each seed.

> **(v) The second coupling.** At `β = 2` the predicted plateau is `1.025979`, three times the
> `β = 6` effect. Two seeds give top shells `1.0341`, `1.0384`, mean `1.0362` — an excess of
> `0.0103 = **0.86 σ⁴**`, which is inside the `+0.8σ⁴` to `+1.0σ⁴` residual `a3`'s section 3
> states for the backward stencil. And the flatness **fails** there: the top four shells spread
> by `0.0167` against `0.0014` at `β = 6`, a monotone rise in `|k|` — the same order `σ⁴`.

So `a3`'s formula is confirmed where the statistics are good, the lowest shell — the only place
the task's sub-1 numbers live — is consistent with it once the window is long enough to measure
it, and **the two couplings separate the one-loop term from its `σ⁴` correction**: at `β = 6` the
correction is invisible (`4·10⁻⁴`, inside the seed noise) and the line is flat; at `β = 2` the
correction is `0.86σ⁴` and the `k`-dependence appears at exactly that order.

## 2. Steps

**S1 (CHECKED `V1`).** The prediction, from the stencil: `σ²` in `mpmath`, `W` as an exact
lattice sum over the `48³` modes.

**S2 (CHECKED `V2`).** The short run reproduced, with the mode counts that explain why its lowest
shell is noisy: 56 modes against 49450.

**S3 (CHECKED `V3`).** The three long runs. The discriminating numbers are the **spreads**: the
lowest shell's `0.039` against the top shell's `0.0010`. A quantity with that much seed-to-seed
scatter cannot be read off one run to three decimals, which is what the task's premise does.

**S4 (CHECKED `V4`).** Measured plateau against prediction, and the flatness in `k` at `β = 6`.

**S5 (CHECKED `V5`).** The second coupling: the `σ⁴` excess and the loss of flatness. The two
couplings are what separate the orders - one measurement could not.

## 3. Where this stops

- **Two couplings, three and two seeds.** `β = 2` has only two seeds, so its residual
  coefficient `0.86σ⁴` carries roughly `±0.25` from the seed spread; it is consistent with
  `a3`'s `0.8`–`1.0` but does not pin it.
- **The lowest shell is still not resolved to `0.02`.** Three seeds give a *sample* s.d. of
  `0.039`, i.e. a standard error of `0.023` on the mean — just above `a3`'s target. What the runs
  do settle is the sign question: the shell scatters **around** the plateau, not below it.
- **`a3`'s one-loop closure is still assumed**, as its section 3 says. Nothing here proves it;
  what is shown is that its prediction matches the measurement to `4·10⁻⁴` at one coupling.
- The light-cone stencil, where `a3` predicts a `k`-dependent `R` through the exchange term, is
  not measured here.

## 4. What would finish it

1. More seeds at `β = 2`, to pin the `σ⁴` coefficient to two digits, and enough of them to bring
   the lowest shell's standard error under `0.01`. At about three minutes a run this is an hour's
   work, not a research problem.
2. The light-cone stencil's `k`-dependence, which is the one place `a3`'s formula predicts
   something other than a flat line and is therefore the sharpest available test of it.
3. `a3`'s two-loop terms remain the theoretical item.

## 5. Running it

```
python3 probes/work/derive/kernel-normalization-puzzle/w-jonathonsmac4f50-j7bbc/check.py
```
from the repository root. `numpy` and `mpmath`; a few seconds. The measurements are embedded with
the exact command lines that produced them, in the script's header.

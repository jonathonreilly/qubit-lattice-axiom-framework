# kernel-normalization-puzzle, attempt 1 of 3 — the sine, priced exactly

Worker `w-jonathonsmac4f50-j00a2` (`claude-opus-5`), unit `J-derive-kernel-normalization-puzzle:a1`.

**Provenance.** Two prior attempts exist (`j5e26`, `j7bbc`), both the same model family, machine and
running worker as this one. I re-run neither. Their open items are the two-loop terms and more
seeds; **neither has priced the first candidate the unit lists** — that the lab-frame component is
`sin θ` and not `θ`. That one is exactly computable, has the right sign, and has the right
`β`-dependence. This attempt prices it and nothing else.

## 1. What is claimed

`probes/lib/formation_levelplane.py` takes lab-frame components `s·t₁, s·t₂` about the **initial**
direction. A unit record at polar angle `θ` from that direction has transverse components of
magnitude `sin θ`, not `θ`. So the estimator measures `⟨sin²θ⟩` while the linear theory predicting
ratio `1` is a statement about `⟨θ²⟩`.

> For an isotropic Gaussian transverse field with total variance `T = ⟨θ²⟩` per site,
>
> ```
> ⟨sin²θ⟩ / ⟨θ²⟩  =  1 − (2/3) T + (4/15) T² ,
> ```
>
> exactly, from `⟨(θ²)^m⟩ = (2v)^m m!` and `sin²θ = θ² − θ⁴/3 + 2θ⁶/45`. The leading deficit is
> **two thirds of the transverse variance**, a purely kinematic factor with no dynamics in it.
>
> With `T ≥ σ² = A(3β)/(3β)`, the deficit is `2/(9β) + O(1/β²)` — at least **3.0%** at `β = 2`,
> falling to **0.31%** at `β = 24`. That is the sign, the order in `1/β`, and the size of the
> backward table's `0.95–0.99` rising to `1.01`.

## 2. The steps

1. **PROVED + CHECKED (`N2`).** The moments `⟨(θ²)^m⟩ = (2v)^m m!` for `m = 1,2,3`, by direct
   integration; the series for `sin²θ`; and the assembled ratio in both `v` and `T = 2v` forms.
2. **CHECKED (`N3`).** `σ² = A(3β)/(3β)` at `β = 1,2,4,6,24`; the deficit falls monotonically, and
   `β·(2/3)σ² → 2/9` exactly, so the deficit is `2/(9β)` asymptotically. The `β = 2` bound puts the
   ratio at most `0.9700` and the `β = 24` bound at most `0.99691` — the two ends of the table.
3. `W ≥ 1` (the lattice factor the estimator's shells sum to) only makes the deficit **larger**, so
   everything above is the conservative end.

## 3. Where this stops

- **This is one of four candidates and the only one priced.** The unit lists three others — the
  wandering mean direction, the vMF variance at the fluctuating concentration `β|S_x|`, and the
  shifted pole from `g < 1`. None is touched here.
- **It cannot explain the values ABOVE 1.** At `β = 24` the deficit is `0.0031`, far too small to
  be overcome by anything in this calculation, yet the measurement is `1.01`; and the light-cone
  stencil is `1.01–1.09`. Those need a **positive** contribution from elsewhere. So this attempt
  splits the puzzle rather than solving it: a kinematic deficit that is now exact, and a smaller
  positive remainder that is not.
- **`T` is bounded, not computed.** I use `T ≥ σ²`, i.e. `W = 1`. The true `W` depends on the
  shells the estimator keeps and on `1/(1−|φ(k)|²)` summed over them; with it the numbers would be
  predictions rather than bounds. That is the single cheapest thing to do next.
- **The Gaussian assumption.** The ratio is exact *for an isotropic Gaussian transverse field*. At
  `β = 2` the field is not obviously Gaussian, and the `(4/15)T²` term is the first place that
  would show.
- **I have not run the estimator or read the logs.** The measured numbers are taken from the unit's
  own statement of them.

## 4. What would finish it

1. Compute `W` from the estimator's shells and turn the bound into a prediction; compare to
   `0.95–0.99` directly.
2. Price the remaining three candidates at order `1/β`, since the residual is now isolated: it is
   whatever must be **added** to `1 − 2/(9β)` to reach the table, and at `β = 24` that residual is
   about `+0.013`.
3. The light-cone stencil is the sharper test — it sits furthest above 1 — and `j7bbc` already
   names its `k`-dependence as the place a formula would be falsified.
4. Another family: three of three attempts on this problem are the same worker.

## 5. Running it

```
python3 probes/work/derive/kernel-normalization-puzzle/w-jonathonsmac4f50-j00a2/check.py
```

Standard library plus `sympy`; 10 checks, exact symbolic integration and high-precision evaluation
of `A(3β)/(3β)`.

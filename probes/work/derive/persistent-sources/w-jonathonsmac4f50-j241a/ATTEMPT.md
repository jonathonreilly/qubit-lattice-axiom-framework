# persistent-sources, attempt 3 of 5 — two pinned sources do not superpose

Worker `w-jonathonsmac4f50-j241a` (`claude-opus-5`), unit `J-derive-persistent-sources:a3`.

**Provenance.** Two prior attempts exist (`j09ae`, `jd96c`), both the same model family, machine and
running worker as this one. I re-run neither. Both leave the unit's part **(a)** — the two-source
linear problem — and go after the nonlinear coefficient instead. This attempt does (a).

## 1. What is claimed

The referee's correction states that a source pinned at *every* level is not a conditioning of the
stationary Gaussian at one time, and that the pinned process has stationary mean `α G(y)/G(0)` with
`G = (I − P)⁻¹`. For a pinned **set** `S`:

> **Theorem.** The stationary mean is `m(y) = Σ_i c_i G(y − x_i)` with
>
> ```
> c = M⁻¹ α ,        M_ij = G(x_i − x_j)          (the Green matrix of S).
> ```
>
> So the one-source formula is the `|S| = 1` case of a linear solve of size `|S|`, and **it does
> not superpose**. For two sources:
>
> - the naive sum of two single-source solutions overshoots the first pinning condition by exactly
>   `α₂ G(d)/G(0)`;
> - for **equal** charges the true coefficient is `α/(G(0) + G(d))` — each charge **screened** by
>   `G(0)/(G(0)+G(d)) < 1`, because each source sits in the other's field;
> - for **opposite** charges it is `α/(G(0) − G(d))` — **anti-screened** by `G(0)/(G(0)−G(d)) > 1`.
>
> The whole two-source interaction of the linear pinned process is carried by the single ratio
> `G(d)/G(0)`.

Verified exactly on a `4×4×4` torus with the 7-point light-cone stencil (`1 − P̂(k) = E(k)/7`) and
killing `1/10`, where `G(0) = 3337205782/2311505635 = 1.443736814` and, at separation 2,
`G(d) = 380959524/2311505635 = 0.164810121`: the overshoot is `95239881/1668602891 = 0.057077620`,
the true charge is `0.974649317` of the naive one, the screening factor is `0.897540993` and the
anti-screening factor `1.128865964`.

## 2. The steps

1. **CHECKED (`T1`).** `G = (I−P)⁻¹` built exactly; translation invariance and symmetry verified.
2. **CHECKED (`T2`).** One source: `m(x₁) = α` and `(I−P)m = 0` at *every* unpinned site — so the
   ansatz really is the stationary mean, not just a function matching at the source.
3. **CHECKED (`T3`).** Two sources: both pinning conditions hold exactly and `(I−P)m` vanishes off
   the pinned pair.
4. **CHECKED (`T4`).** The naive superposition fails by exactly `α₂G(d)/G(0)`, and the true charge
   ratio differs from 1.
5. **CHECKED (`T5`).** The equal- and opposite-charge coefficients, with both factors exact.

**The killing rate is a device.** A torus makes `I − P` singular on the constant mode, and on a
finite torus a single pinned site forces the *constant* solution — the interesting structure is a
statement about the infinite lattice, where transience of the 3D walk makes `G` finite. I use a
small killing rate to get an exactly invertible operator on a finite grid. **The structural
claims — the `M⁻¹α` form, the failure of superposition, the two screening factors — do not
depend on the killing**; only the printed numbers do.

## 3. Where this stops

- **The numbers are killed-walk numbers on a `4×4×4` torus**, not the `Z³` Green function. In
  particular `G(0) = 1.4437` here is not the transient-walk `G(0)`, and the screening factors would
  move. The algebra is what transfers.
- **No continuum limit, no Coulomb coefficient.** The unit's `7σ²/(8πr)` and the `(1+φ)` factor in
  `χ/C` are untouched; I do not connect `G(d)/G(0)` to the `1/r` tail.
- **Linear process only.** The executed nonlinear result (`0.96–0.99` of `(h/β)×`Green function)
  is what both prior attempts chase, and this says nothing about it.
- **Two sources only.** The `M⁻¹α` statement is general in `|S|`, but I check `|S| = 1, 2`.
- **I did not run `probes/lib/formation_response.py`.**

## 4. What would finish it

1. Take the killing to zero with the torus size to infinity and recover the `Z³` `G`, which turns
   the screening factors into numbers comparable with the simulator.
2. `M⁻¹` for a line or a plane of sources — the natural next case, and the one where a
   `G(d)/G(0)` expansion would show whether the interaction is `1/r` at leading order.
3. Check whether the nonlinear law's `0.96–0.99` is partly this effect: if the simulator pins more
   than one site, or pins a site while measuring near a boundary, the screening factor is exactly
   the sort of multiplicative deficit reported.
4. Another family: all three attempts on this problem are the same worker.

## 5. Running it

```
python3 probes/work/derive/persistent-sources/w-jonathonsmac4f50-j241a/check.py
```

`sympy` only; 12 checks, exact rational arithmetic throughout — every number in the summary is
interpolated from the computation, none typed.

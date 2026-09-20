# persistent-sources, attempt 1 of 5 — a line of sources, and who is screened most

Worker `w-jonathonsmac4f50-j89fe` (`claude-opus-5`), unit `J-derive-persistent-sources:a1`.

**Provenance.** Three prior attempts exist (`j09ae`, `jd96c`, `j241a`), all the same model family,
machine and running worker as this one. **`j241a` is mine**, finished minutes before this unit was
claimed (issue #8543): it proved the pinned-set stationary mean is `m = Σ_i c_i G(· − x_i)` with
`c = M⁻¹α`, `M` the Green matrix, and listed as item 2 *"`M⁻¹` for a line of sources"*. That is
this attempt. I do not re-run its two-source case.

## 1. What is claimed

> **(i)** The `c = M⁻¹α` form solves the pinned problem for `n = 2, 3, 4` collinear sources — every
> pinning condition holds **and** `(I − P)m` vanishes at *every* unpinned site.
>
> **(ii) The charge is position-dependent.** At `n = 3` the charges are symmetric end-to-end and
> the **interior** source carries strictly less than the ends — `0.447653871` against
> `0.528563241` — because an interior source is screened on both sides while an end is screened on
> one. **This is invisible in the two-source case, where every source is an end.**
>
> **(iii) The charge per source falls with the line's length**, from `0.692647...` for an isolated
> source (`α/G(0)`) to `0.562325833` at `n = 2`, `0.501593451` at `n = 3` and `0.439033578` at
> `n = 4`. A longer line is **cheaper per site** to hold at the same pinned value.
>
> **(iv)** On this `L = 4` torus `n = 4` **wraps**: the line closes into a ring, every source is
> translation-equivalent, and all four charges are equal. There are no ends on a ring, so that row
> is the closed-loop case and not a longer line — a finite-size feature the solve detects on its
> own.

## 2. The steps

1. **CHECKED (`U1`).** `G = (I−P)⁻¹` exact, symmetric.
2. **CHECKED (`U2`).** For `n = 2, 3, 4`: all pinning conditions and `(I−P)m = 0` off the line.
3. **CHECKED (`U3`).** The end/interior split at `n = 3`; the wrap at `n = 4`.
4. **CHECKED (`U4`).** Totals and per-source charges, with the monotone fall.

Exact rational arithmetic throughout; every number in the summary is interpolated from the
computation.

## 3. Where this stops

- **`L = 4` is small enough that `n = 4` already wraps.** So the line is only probed at `n = 2, 3`
  — two data points for a trend in `n`, which is why (iii) is stated as the numbers rather than as
  a law. A larger torus would need a larger exact inverse than I ran.
- **The killing rate is a device**, as in `j241a`: it makes `I − P` invertible on a finite torus.
  The structural claims do not depend on it; the numbers are not `Z³` numbers.
- **No asymptotics.** The natural question — whether the per-source charge tends to a positive
  constant or to zero as the line lengthens — is exactly what two points cannot answer, and it is
  the one thing that would connect this to a `1/r` interaction.
- **Linear process only**, and one direction of one lattice.

## 4. What would finish it

1. A bigger torus and a sparse exact solve, to get `n = 2..6` and settle the trend in (iii).
2. The same computation for a **plane** of sources, where the screening should saturate faster;
   that is the geometry closest to the simulator's boundary conditions.
3. The asymptotic question: per-source charge as `n → ∞`, which is a statement about the Green
   function's decay and therefore the place where `1/r` would enter.
4. Another family — all four attempts on this problem are now the same worker.

## 5. Running it

```
python3 probes/work/derive/persistent-sources/w-jonathonsmac4f50-j89fe/check.py
```

`sympy` only; 10 checks, exact rational arithmetic.

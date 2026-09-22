# one-cone-for-field-and-walker, attempt 1 of 2: the clauses leave K/α free; one cone is the owner's choice

Worker `w-jonathonsmac4f50-jf0e6` (`claude-opus-5-5`), unit `J-derive-one-cone-for-field-and-walker:a1`.

**Provenance.** There were no prior attempts. Block 62's T4 dispersion (PR #8592) is used as GIVEN. Blocks 54, 60 and 64 and the fork
probe supply the setting. All are the same model family as me.

## 1. What is claimed

> **(a)** The two transverse-traceless disturbances have `ω² = K w̄² p²/(4α)` in ambient time, with `p² = Σ_j 4 sin²(k_j/2)`
> (block 62 T4). At long wavelength their speed is `c_f = w̄ √(K/(4α))` in every direction. The walker's is `c_w = w̄`, since
> `ω² = w̄² Σ sin²k_j`.
>
> **(b)** The two cones coincide at long wavelength **iff `K = 4α`**. The two polarisations always share one speed, for every
> `α ≠ 0, α + β_kin ≠ 0`, because block 62 T4 gives a double root.
>
> **(c)** The supplied clauses do **not** fix `K/α`. Weight one, per-tick counting and blindness to the coin's axes each constrain
> the kinetic term `α ḣ²/w̄` and the potential `K w̄ |∇h|²` separately. Both have weight one for every `α` and `K`. So `(α, K)` and
> `(sα, K)` satisfy every clause for every `s > 0`. Whether the field's cone is the walker's is the owner's choice (fork 7).
> - *Comparator only, not used.* In the continuum, closure of the constraint algebra, which is per-tick counting read as
>   dynamics (the fork probe §4.5, DeWitt's `β = −α`, `K = 4α`), would fix `K = 4α`. That is not among the supplied clauses, and
>   its lattice form is untested.
> - **The unit's HIT condition** (the clauses fix `K/(4α) ≠ 1`) is not met.
>
> **(d) (exact).** At `K = 4α`, `ω_field² − ω_walker² = 4w̄² Σ_j sin⁴(k_j/2) ≥ 0`, because `sin²k = 4sin²(k/2) − 4sin⁴(k/2)`.
> The field is never slower, and the mismatch is fourth order in `k` in `ω²`. In speeds at second order:
> - along an axis, the phase speeds are `1 − k²/6` (walker) and `1 − k²/24` (field), a gap of `k²/8`;
> - along an axis, the group speeds are `cos k` and `cos(k/2)`, a gap of `3k²/8`;
> - along the body diagonal, the phase gap is `k²/24`.
>
> The mismatch depends on direction: the field's `2 sin(k/2)` and the walker's `sin k` differ at the lattice scale.

## 2. The steps

1. **CHECKED (A1).** The long-wavelength limits of `ω²/k²` for both dispersions along an arbitrary unit direction (symbolic).
2. **CHECKED (B1).** `c_f = c_w ⟺ K = 4α` (symbolic solve). Equal polarisation speeds: GIVEN from block 62 T4's factor
   `(p² − 4αX)²`.
3. **PROVED + CHECKED (C1).** Under a change of the unit of rate (`w → λw`, `t → t/λ`), both terms scale by `λ` for every `α` and
   `K`. Per-tick counting constrains the potential's form (block 60), and blindness selects block 64's curvature member. Neither
   relates it to the kinetic coefficient. So the clause set is invariant under `α → sα` at fixed `K`.
4. **CHECKED (D1, D2).** The trigonometric identity and the exact difference of the two squared dispersions (symbolic), and the
   second-order series of phase and group speeds along an axis and along the diagonal.

## 3. Where this stops

- **(c) covers the supplied clauses as stated.** A dynamical principle, such as the constraint algebra closing on the lattice, might
  tie `K` to `α`. It is not a clause and is not examined here. Doing so is the fork probe's open item §4.5.
- **The kinetic family is block 62's rotation-invariant one.** The cube-only kinetic terms that block 62 found have no single speed
  are outside it.

## 4. What would finish it

1. The owner's decision on fork 7: supply `K = 4α` (one cone) or leave it free.
2. Or the lattice constraint-algebra computation, which would show whether closure forces `K = 4α` and at which order in `p` it
   fails.

## 5. Running it

```
python3 probes/work/derive/one-cone-for-field-and-walker/w-jonathonsmac4f50-jf0e6/check.py
```

It uses sympy, has 5 checks, all exact, and runs in about a second.

# moving-what-fixes-the-scale, attempt 5 of 5 — `c₀` is a determinant, and block 39's two facts are one

Worker `w-jonathonsmac4f50-jc532` (`claude-opus-5`), unit `J-derive-moving-what-fixes-the-scale:a5`.

**Provenance.** The one prior attempt, `a1` (`w-jonathonsmac4f50-j882f`), is by the same model
family, machine and running worker as this one, so nothing here is independent confirmation of it.
`a1` settles (a), (c) and the *second* half of (b) — the identification with block 24's integrated
reading, which it closes as a no-go. I re-run none of that. Its §4 names three open items; this
attempt takes two of them: **(b)'s first half**, which `a1` calls "the only candidate that could
make `c₀` special for a spectral reason rather than an averaging one", and **(d)**, which it calls
what it would take next.

## 1. What is claimed

Write `T` for the pair-weight matrix of the law with vacancies on the seven states {six contents,
empty}: `T[a][b] = c·ω(a,b)` between records (`ω = p, q, r` for equal, opposite, orthogonal), and
`T = 1` on any bond with an empty end. Let `A₁ = p + q + 4r`, so `c₀ = 6/A₁`.

> **(b), first half — `c₀` is where the transfer operator degenerates.** The empty state couples
> to the six contents only through the all-ones direction, because every bond with an empty end
> weighs the same `1`. So `T` splits into the eigenspaces of `Ω` orthogonal to `1` — untouched by
> the vacancy — and a `2×2` block on `span{u, e_∅}`, `u = (1,…,1)/√6`:
>
> ```
> B = [[ c·A₁ , √6 ],
>      [  √6  ,  1 ]] ,      det B = c·A₁ − 6 ,
> ```
>
> and the whole determinant factors as
>
> ```
> det T  =  c⁵ (p − q)³ (p + q − 2r)² ( c(p+q+4r) − 6 ).
> ```
>
> Every factor is an eigenvalue with its multiplicity, and **the only factor that depends on the
> scale is the last**. So `c₀` is the unique scale at which `T` is singular, and there the kernel
> is `u − √6·e_∅`: **the empty state is exactly the uniform superposition of the six record
> states**, and the rank of `T` drops by one. That is "no state is privileged" as an operator
> identity rather than an average — at `c₀` the empty state is not a seventh state at all.
>
> **The two facts block 39 gives are one fact.** The averaging statement (an empty neighbour
> weighs what a uniformly random record weighs, `c·A₁/6 = 1`) and the reflection-positivity
> threshold are the same equation `c·A₁ = 6`, read once as a mean and once as a determinant.
>
> **Correction.** Bond-plane RP holds iff `T ⪰ 0`, and `T`'s eigenvalues are `p−q` (×3),
> `p+q−2r` (×2) and the two roots of `B` (trace `c·A₁ + 1 > 0`, determinant `c·A₁ − 6`). So
>
> ```
> T ⪰ 0   ⟺   c ≥ c₀   AND   p ≥ q   AND   p + q ≥ 2r,
> ```
>
> the last two being **scale-free**. Block 39's "reflection positive exactly for `c ≥ c₀`" is
> therefore incomplete. At `(5,2,4)` the second side condition fails (`7 < 8`), and **no scale**
> makes the law with vacancies reflection positive through a bond plane there.
>
> **(d) — formation and motion are consistent for no scale.** With `x, y` adjacent and empty, `x`
> having one occupied neighbour carrying `a` and `y` none: forming at `x` and then moving to `y`
> leaves content `s` with probability `∝ cω(a,s)/(1 + cω(a,s))`, while forming at `y` directly is
> uniform. Since `t ↦ ct/(1+ct)` is strictly increasing for every `c > 0`, the two agree only if
> `ω` is constant, i.e. `p = q = r`. **(d) constrains the weights, not the scale**: it has no
> solution in `c`, and at `c₀` the two routes' content laws differ in total variation by `7/132`
> at `(3,1,2)`.

## 2. The steps

1. **CHECKED (`D1`).** `Ω = (p−r)I + (q−r)J + r·11ᵀ` with `J` the antipodal swap; spectrum
   `p+q+4r` (once), `p+q−2r` (twice), `p−q` (three times), trace `6p`. Confirmed twice: by
   `sympy`'s eigenvalue routine *and* by exhibiting explicit eigenvectors, so nothing rests on a
   symbolic root-finder.
2. **PROVED (`D2`).** `T u = c·A₁·u + √6·e_∅` and `T e_∅ = √6·u + e_∅`, verified as vector
   identities — this is the `2×2` block. `det B = c·A₁ − 6`, whose unique root in `c` is `c₀`.
3. **PROVED (`D2`).** The factored `det T` above, verified identically in `p, q, r, c`. This is
   the whole claim in one line: the scale enters the determinant exactly once.
4. **PROVED (`D3`).** At `c₀` the kernel of `B` is one-dimensional and spanned by `u − √6 e_∅`.
   **CHECKED:** at `(3,1,2)`, `rank T = 4` at `c₀ = 1/2` against `5` at `c = 1` — a drop of
   exactly one, on top of the two ranks that `p+q−2r = 0` costs there at every scale. (The
   generic drop is `7 → 6`; `(3,1,2)` is degenerate for a scale-free reason.)
5. **CHECKED (`D4`).** The PSD table at `(3,1,2)`, `(5,2,4)`, `(7,3,5)`, `(4,1,1)`: `T` at `c₀`
   has a negative eigenvalue exactly when `p < q` or `p + q < 2r`. `(5,2,4)` is the case that
   fails. Note `(3,1,2)` and `(7,3,5)` both sit exactly on the boundary `p + q = 2r`.
6. **PROVED + CHECKED (`D5`).** The route comparison, with the monotonicity argument for the
   general statement and exact rational total variations at `(3,1,2)` (`7/132`) and `(5,2,4)`.
   `sympy` finds no positive `c` equalizing the equal-axis and orthogonal branches.

**ASSUMED.** (i) That bond-plane RP for this law is equivalent to `T ⪰ 0` — the standard
positive-type criterion for a reflection through a bond, used here at the scope of a single bond.
(ii) `a1`'s caveat carries over in full: the uniform prior over the six contents is a *choice*, and
it is what makes `c₀` come out as an arithmetic mean. It enters D2 through nothing at all — the
determinant is prior-free — but it is what licenses *calling* `c₀` "the averaging scale". (iii)
The motion rule in D5 is the unit's own: a record chooses between its position and an empty
neighbour in proportion to the pair weights it would have there.

## 3. Where this stops

- **(e) is not attempted** — the memo's open gate on the natural unit. Neither attempt has looked
  at it, so one of the five candidates remains untouched after five attempts.
- **The strict-contraction half of (b) is only half-answered.** I show where the operator is
  singular and what the kernel is. Whether `T` is a strict contraction on the complement of its
  top state — the unit's phrasing — needs the normalized operator and its second eigenvalue, which
  I did not compute. The zero eigenvalue is a sharper statement than a contraction, but it is not
  the same statement.
- **The RP correction is derived at one bond.** Full reflection positivity through a plane is a
  statement about the reflected half-space measure; I check the single-bond positive-type
  condition, which is what the plane criterion reduces to for a nearest-neighbour pair weight, but
  I have not re-derived that reduction here. If block 39 means something weaker by "reflection
  positive", the correction in D4 is aimed at the wrong target — but then the claim "exactly for
  `c ≥ c₀`" needs its own statement of what is being reflected.
- **Nothing dynamical.** `moving_gas.py` is not run. D5 compares two one-step routes, not the
  stationary law of the process.
- **`c` is still a primitive.** (b) makes `c₀` canonical *as the degeneracy point*, which is a
  much better reason than an average — but a degeneracy is not by itself a principle that selects
  it. Someone still has to say why the transfer operator should be degenerate.

## 4. What would finish it

1. Say what is wrong with `c ≠ c₀` in one sentence that is not circular. The candidates are now
   sharp: below `c₀` the operator is not positive (given the side conditions), above `c₀` it is
   positive and non-degenerate, and only at `c₀` is the empty state redundant. The last is the
   only one that is an *identity* rather than an inequality, and it is the one to argue from.
2. Settle the `(5,2,4)` case. Either the RP claim in block 39 is wrong there, or bond-plane RP
   means something other than `T ⪰ 0`; both are cheap to check and one of them is a correction to
   a landed note.
3. Candidate (e), which no attempt has touched.
4. Re-derive D2 and D4 with a different model family. Both prior results on this problem and this
   one are the same family.

## 5. Running it

```
python3 probes/work/derive/moving-what-fixes-the-scale/w-jonathonsmac4f50-jc532/check.py
```

Standard library plus `sympy`; 24 checks, exact symbolic and rational arithmetic throughout. Runs
in a few seconds.

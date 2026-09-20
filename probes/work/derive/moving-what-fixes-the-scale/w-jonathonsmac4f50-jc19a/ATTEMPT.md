# moving-what-fixes-the-scale, attempt 2 of 5 — "no state is privileged" is a one-bond statement

Worker `w-jonathonsmac4f50-jc19a` (`claude-opus-5`), unit `J-derive-moving-what-fixes-the-scale:a2`.

**Provenance.** Both prior attempts are **mine**: `a1` (`w-jonathonsmac4f50-j882f`) settled (a), (c)
and the second half of (b); `a5` (`w-jonathonsmac4f50-jc532`, issue #8534) showed `c₀` is the unique
scale at which the 7-state transfer operator is singular, with kernel `u − √6 e_∅`. Same model
family, machine and worker; no independent confirmation of either. I re-run neither route. `a5`'s
§4 item 1 asked for the one thing that would make its determinant a principle rather than a
restatement — *say what is wrong with `c ≠ c₀` without circularity*. The way to do that is to ask
how far the redundancy reaches, and the answer is: one bond.

## 1. What is claimed

Test "an empty site is not privileged" as a statement about the **measure**, not the operator: a
site `x` with `j` occupied neighbours carrying `a_1..a_j` weighs `1` when empty, and
`c^j (1/6) Σ_s Π_i ω(a_i,s)` when it carries a record whose content has been averaged away.

> **Degree 1.** The two agree at exactly one scale: `c(p+q+4r)/6 = 1`, i.e. `c = c₀`.
>
> **Degree 2.** The averaged-record weight takes **three different values** — `p²+q²+4r²` (equal),
> `2pq+4r²` (opposite), `2r(p+q)+2r²` (orthogonal) — so **no scale matches all three** unless
> `p = q = r`. The gap between branches is the content covariance that a shared empty site cannot
> reproduce. (`a1` found the same obstruction from block 24's side, on a bridge.)
>
> **Degree j, averaged.** Averaging over the *neighbours'* contents too gives exactly
> `[c(p+q+4r)/6]^j`, which is `1` at `c₀` for **every** `j`, because `Σ_a ω(a,s) = p+q+4r` for
> every `s`.
>
> **So:** the redundancy is exact at every degree **in mean**, and exact **pointwise only at
> degree ≤ 1**. `c₀` is the unique scale at which an empty site weighs what an averaged record
> weighs, and that identity is a one-bond statement. The principle cannot fix the scale by itself
> beyond degree one.
>
> **And one branch is fixed by the weights, not the scale.** At `c₀` the orthogonal degree-2 weight
> equals `1` exactly when
>
> ```
> 12r(p+q+r) − (p+q+4r)²  =  −(p+q−2r)²  =  0 ,      i.e.   p + q = 2r,
> ```
>
> which is **the same scale-free condition** that issue #8534 found bond-plane reflection positivity
> needs beyond `c ≥ c₀`. Two of the lane's three standard triples sit exactly on it — `(3,1,2)` and
> `(7,3,5)` — while `(5,2,4)` does not.

## 2. The steps

1. **PROVED + CHECKED (`R1`, `R2`).** The degree-`j` test, and `solve` returning `c₀` as the unique
   root at `j = 1`.
2. **PROVED + CHECKED (`R3`).** The three degree-2 sums, computed from the stencil; they collapse
   to a common value only at `p = q = r`.
3. **PROVED + CHECKED (`R4`).** `Σ_a ω(a,s) = p+q+4r` for every `s`, hence the fully averaged
   weight is `[c(p+q+4r)/6]^j`, checked equal to 1 at `c₀` for `j = 1,2,3,6`.
4. **PROVED + CHECKED (`R5`).** The factorization `12r(p+q+r) − (p+q+4r)² = −(p+q−2r)²`, verified
   identically, and the four triples classified by `p+q−2r`.

## 3. Where this stops

- **This does not derive `c₀`; it delimits what deriving it would mean.** The principle picks `c₀`
  uniquely at degree one and says nothing at higher degree, so anyone using "no state is
  privileged" to fix the scale is relying on the one-bond reading. That is a sharper objection than
  `a5` could make, but it is still an objection, not a derivation.
- **Candidate (e) remains untouched** after all five attempts — the memo's natural-unit gate. This
  is the third attempt in a row to leave it, and it is now the only candidate nobody has looked at.
- **The uniform prior over contents is assumed**, as in `a1` and `a5`. The whole "averaged record"
  reading rests on it, and a different prior moves `c₀`.
- **The link to #8534's RP condition is an identity, not an explanation.** I show the same
  polynomial `p+q−2r` governs both, and I have no argument for why the degree-2 orthogonal branch
  and the transfer matrix's axis-symmetric mode should be the same condition. It may be one fact
  seen twice, as the averaging/determinant pair was in #8534; I did not establish that.

## 4. What would finish it

1. Decide whether `p + q = 2r` is a coincidence of two computations or one structure. Both are
   statements about the axis-symmetric mode of the content space, so the natural attempt is to
   redo the degree-2 test in the eigenbasis used in #8534 and see whether the branches *are* the
   modes.
2. Candidate (e).
3. If the one-bond reading is accepted as the principle, state it as such in block 39, since the
   statement "an empty neighbour weighs what a random record weighs" is already exactly that, and
   its degree-2 failure should be recorded beside it.
4. Another model family on `a1`, `a5` and this — all three are the same worker.

## 5. Running it

```
python3 probes/work/derive/moving-what-fixes-the-scale/w-jonathonsmac4f50-jc19a/check.py
```

Standard library plus `sympy`; 15 checks, exact symbolic arithmetic.

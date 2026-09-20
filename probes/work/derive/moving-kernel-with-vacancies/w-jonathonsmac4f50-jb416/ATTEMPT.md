# moving-kernel-with-vacancies, attempt 3 of 4 — the stiffness is the bond density

Worker `w-jonathonsmac4f50-jb416` (`claude-opus-5`), unit `J-derive-moving-kernel-with-vacancies:a3`.

**Provenance.** No prior attempt existed on this problem at claim time, so nothing here checks
another worker's route. Two inputs come from elsewhere in this campaign and are **same model
family** (`claude-opus-5`), not independent: block 22's constant `3G(0) ∈ (0.75, 0.76)`, used as
given in step 5, and the six-axis contrast in step 2, which is my own result from
`J:derive:moving-what-fixes-the-scale:a5` earlier today.

## 1. What is claimed

Sphere menu with vacancies at fugacity `z`: a site is empty or carries a content `s ∈ S²`; two
records weigh `c·e^{βs·s'}`; a bond with an empty end weighs `1`; `ρ = ⟨1[occupied]⟩` and
`ρ₂ = ⟨1[both ends of a bond occupied]⟩`.

> **(a) What the twist twists.** The twisted partition function rotates *contents*. A bond with an
> empty end weighs `1` whatever the twist, so it contributes nothing, and the Gaussian-domination
> quadratic form is `β` times a sum over **occupied–occupied bonds only**.
>
> **(b) The infrared bound and the sum rule.** Hence
>
> ```
> ⟨|σ̂(k)|²⟩  ≤  1 / ( β ρ₂ E(k) ),      σ_x = s_x·1[x occupied],
> ```
>
> and since `|s|² = 1` on every content, the sum rule reads
>
> ```
> (1/N) Σ_k ⟨|σ̂(k)|²⟩  =  ρ          — not 1.  The vacancies take the rest.
> ```
>
> **(d) The stiffness.** The coefficient of `1/E(k)` is `1/(βρ₂)`: the stiffness is carried by the
> **bond** density, not the site density. That is the whole content of the vacancy modification —
> `β` is replaced by `βρ₂` everywhere block 19 used `β`.
>
> **(c) Long-range order, and the obstruction.** Combining,
>
> ```
> M²  ≥  ρ − 3G(0)/(β ρ₂) ,     so LRO holds once   β ρ₂ ρ > 3G(0).
> ```
>
> The only unconditional inequality between the two densities is `ρ₂ ≥ 2ρ − 1`, which is **sharp**
> and **vacuous at `ρ ≤ 1/2`**. So the explicit threshold is
>
> ```
> β  >  3G(0) / ( ρ (2ρ − 1) )      — and it exists only above half filling.
> ```
>
> At `ρ = 1` it is `β > 3G(0) = 0.76`, recovering block 19's full-lattice threshold exactly.
>
> **Also: `c₀` is a determinant here too.** The empty state couples to the contents only through
> the constant function, so on `span{1, e_∅}` the kernel is `[[c⟨e^{βs·s'}⟩, 1], [1, 1]]` with
> determinant `c⟨e^{βs·s'}⟩ − 1`, and `⟨e^{βs·s'}⟩ = sinh β/β` gives `c₀ = β/sinh β` — the value
> the unit quotes from block 39's T5, recovered as a determinant rather than as an average.

## 2. The steps

1. **PROVED + CHECKED (`K1`).** `⟨e^{βs·s'}⟩ = sinh β/β` over the sphere, via the explicit
   antiderivative `e^{βt}/(2β)` verified by differentiation (not `integrate`, which returns a
   `Piecewise` at `β = 0`). Hence `c₀ = β/sinh β`, and `1/cosh β` for the two-valued menu.
2. **PROVED (`K2`), one step ASSUMED.** The kernel's other modes are its expansion coefficients
   `a_l(β)` in `e^{βs·s'} = Σ_l a_l(β)P_l(s·s')`, and these are positive (modified Bessel
   functions of positive argument) — **ASSUMED, not re-proved**. Given that, the only route to
   losing positive semidefiniteness is the `2×2` block, so "RP exactly for `c ≥ c₀`" needs no side
   condition for the sphere menu. **CHECKED** in the two-valued case, where the expansion has two
   terms and the second is `sinh β > 0`. This is the contrast with the six-axis menu, whose modes
   `p−q` and `p+q−2r` can be negative — the *menu*, not the scale, decides whether the quoted
   statement is complete.
3. **PROVED (`K3`).** A bond with an empty end has weight `1` independent of the twist, so it
   drops out of the twisted form. **CHECKED** by enumerating all `3⁹` configurations of a `3×3`
   torus with two-valued contents at `e^β = 2`: the sum rule `(1/N)Σ_x⟨|s_x|²1[occ]⟩ = ρ` holds
   exactly (`ρ = 1168963/1279281`), and `ρ₂ = 9680611/11513529 < ρ`.
4. **PROVED + CHECKED (`K4`).** `ρ₂ ≥ 2ρ − 1` by inclusion–exclusion on one bond, verified on the
   torus, and **sharp**: for each `ρ` the explicit two-site law
   `(max(0,2ρ−1), ρ−max(0,2ρ−1), ρ−max(0,2ρ−1), 1−2ρ+max(0,2ρ−1))` is a probability law with both
   marginals `ρ` attaining it.
5. **PROVED given the inputs (`K5`).** The threshold table, decreasing in `ρ`, reducing to
   `3G(0)` at `ρ = 1`. `3G(0) ∈ (0.75, 0.76)` is **ASSUMED** from block 22 (PR #8156).

## 3. Where this stops

- **Gaussian domination itself is not re-proved.** I take block 19's argument as given and track
  what the vacancies change in it — which is exactly the bond restriction in step 3. The chessboard
  estimate and the domination inequality are inherited, not re-derived, and they are what make
  step (b) a theorem rather than a bookkeeping identity.
- **`ρ₂` is not computed from `z`.** The statement is conditional on the bond density, and the
  route from the fugacity to `ρ₂` — which is the actual physics question — is untouched. A
  correlation inequality (FKG on the occupation variables, if it holds here) would give a much
  better bound than `2ρ − 1` and is the obvious next step.
- **Below `ρ = 1/2` the route gives nothing**, and I want to be careful about what that means: the
  `2ρ − 1` bound is sharp *as an inequality between the two densities*, but the sharp example is
  not this law. Whether *this* law has `ρ₂` well above `2ρ − 1` at moderate density is open and is
  a question the simulator could answer; I did not run it.
- **The percolation remark is a remark.** That a transverse field on a non-percolating occupied set
  cannot order is stated, not proved, and the site threshold `0.3116` for `Z³` is quoted from
  outside. It bounds where an *answer* could live, not where this argument fails — this argument
  fails at `1/2` for its own reason.
- The exact enumeration is `3×3` in **two** dimensions with a two-valued content. It checks the
  identities (sum rule, `ρ₂ < ρ`, the inequality), not the three-dimensional physics.

## 4. What would finish it

1. A correlation inequality giving `ρ₂ ≥ f(ρ)` with `f(ρ) > 2ρ − 1` on `(0, 1/2)`. Everything else
   is in place; this single input moves the threshold down to wherever `f` allows and is the only
   thing standing between this and an answer at moderate density.
2. `ρ₂(z, β, c)` from the fugacity, at least as a bound, which makes the theorem a statement about
   the model's own parameters rather than about an observable of its solution.
3. Re-derive `3G(0)`'s bracket and step 2's Bessel positivity outside this model family.
4. Run `probes/lib/moving_gas.py` at `c = c₀` and densities either side of `1/2` and measure `ρ₂`
   against `2ρ − 1`. If the gap is large, item 1 is worth real effort; if it is small, the `1/2`
   floor is close to the truth for this law and the obstruction is physical.

## 5. Running it

```
python3 probes/work/derive/moving-kernel-with-vacancies/w-jonathonsmac4f50-jb416/check.py
```

Standard library plus `sympy`; 19 checks. The torus enumeration is exact rational arithmetic over
all `3⁹` configurations; the symbolic steps use explicit antiderivatives rather than `integrate`.
Runs in a few seconds.

# normal-ordering-as-a-rule, attempt 1 of 2: A and C fix the counter-term on uniform rates, and nowhere else

Worker `w-jonathonsmac4f50-jd669` (`claude-opus-5-5`), unit `J-derive-normal-ordering-as-a-rule:a1`.

**Provenance.** There were no prior attempts. Everything is built on blocks 53–56, 60 and 76 (open PRs; all supervisor-run by
the same model family as me). The sea numbers of block 76 (`c₀`, `κ`) I reproduced with my own code at `L = 6, 8, 10`, and they
agree. That is a same-family reproduction, not an independent confirmation.

## 1. What is claimed

Take block 54's walk `H = Σ_a σ_a ⊗ S_a` with `S_a = (T_a − T_a†)/(2i)` on the torus `(Z/L)³`, clocked as
`H_w = φHφ` with `φ = √w`. The sea is `E_sea[w]`, the sum of the negative eigenvalues of `H_w`. Set `c₀ := E_sea[1]/N`: exactly
`−(3 + 3√2 + √3)/8` on `4³`, and `−1.181, −1.190, −1.192` at `L = 6, 8, 10`, tending to `−1.193`. `Π(q)` is block 76's
polarisation: `E_sea` along the mode `u = ε cos(q·x)` changes by `Π(q) ε² N`.

> **(a) The rule, in the framework's vocabulary.** *The field's term of the ledger is the sea's energy minus, at each site, the
> sea's energy per site at that site's own rate, counted in that site's ticks:*
> `R[w] = E_sea[w] − c₀ Σ_x w_x`.
>
> **(b) Theorem 1 (with the counter-term).** `R` has weight one (clause A's requirement). It vanishes on **every** uniform rate.
> Its first variation at a uniform rate is zero identically, not only after the mean is removed. Its second variation along
> `q` is `Π(q) − c₀/4`: zero at `q = 0` (no volume part), tending to `(κ/4)|q|²_lat` at long wavelength. On the chessboard
> mode, `R = −c₀ N (cosh ε − 1) > 0` **exactly, at every amplitude**, so block 76's zero mode is removed. The linearised static
> law is attractive with `γ_ind = 1/κ`.
>
> **(c) Theorem 2 (what A and C force).** Let the ledger's field term have weight one and be translation invariant. If its
> stationarity law (C) has no mass term (A), then it **vanishes on uniform rates**. So A and C force the counter-term's
> uniform value: `T[w̄·1] = −E_sea[w̄·1] = −c₀ N w̄`.
>
> **Theorem 3 (what they do not force).** Consider two counter-terms:
> - the per-site `T_site = −c₀ Σ_x w_x`;
> - the per-bond `T_bond = −(c₀/3) Σ_bonds √(w_x w_y)`, which is the same sea energy at each bond's geometric-mean rate.
>
> Both have weight one, are covariant and nearest-neighbour, agree on every uniform rate, and satisfy A and C. Their second
> variations differ by the exact factor `1 − |q|²_lat/12`. Along the family `T_θ = θT_site + (1−θ)T_bond`, the long-wavelength
> stiffness is `κ + (1−θ)c₀/12` and the chessboard stiffness is `θ|c₀|/4`. The members therefore give **different static
> laws**:
> - With block 76's declared values, `γ_ind(θ) = 10.53` at `θ = 1` and `22.08` at `θ = ½`.
> - At `θ = 0` the chessboard stays an exact zero mode, and the long-wavelength stiffness is negative on every torus tested.
>
> Choosing `θ = 1` means counting the counter-term **per local tick** (block 60's form `Σ_x w_x G_x`, with `G_x` free of
> rates). That is fork (i), a supplied clause. **Answer to (c): the counter-term is supplied, not a consequence of A and C
> alone.** A and C fix only its value on uniform rates. The unit's HIT condition is therefore not met; the HIT line of
> `check.py` states this negative result and the exact counterexample.
>
> **(d) With the per-site counter-term.** The induced ledger matches block 56's member with `γ = 1/κ`, but only at second order
> and long wavelength. On the chessboard, `F_γ/R = 12κ/|c₀|`, which is `1140/1193 = 0.956` with the declared values. So block 56's
> exact strong field belongs to the sea reading only approximately. With `γ = 1/κ`:
> - The law is linear: `((1−A) + (γ/12)M)φ = 0`.
> - One body gives `φ₀ = 1/(1+x)` with `x = (γ/12) g₀ m`. This is checked exactly on a `5³` box with `γ = 200/19` and `m = 1`,
>   where `g₀ = 136/99` and `φ₀ = 0.453508`.
> - The saturation value is `12/(γ g₀) = 12κ/g₀`. On `Z³`, with `g₀ = 1.516386`, it is **`0.7518`** (`κ = 0.095`) or **`0.7534`**
>   (block 76's `κ = 0.0952`).

## 2. The steps

1. **CHECKED, exact (E1–E3).**
   - On `4³`, `H² = (Σ_a S_a²) ⊗ 1` (anticommuting coins, commuting differences), so the spectrum is `±√(Σ sin²k_a)` and
     `c₀(4) = −(3+3√2+√3)/8`.
   - The chessboard `φ = 2^{ε(x)}` gives `φHφ = H`: block 76 T1, re-checked.
2. **PROVED + CHECKED (E4, E5): Theorem 1.**
   - *Weight one.* `H_{λw} = λH_w`, so `E_sea[λw] = λE_sea[w]`, and `c₀Σw` also has weight one.
   - *Uniform rates.* `E_sea[w̄·1] = w̄ E_sea[1] = c₀Nw̄`, hence `R[w̄·1] = 0`.
   - *First variation.* At `w̄·1`, translation invariance and Euler (step 3) give `∂E_sea/∂u_x = E_sea[w̄·1]/N = c₀w̄`, which
     equals `∂(c₀Σw)/∂u_x`. So the first variation of `R` vanishes pointwise.
   - *Second variation.* `c₀Σw` contributes `c₀/4` per mode (E6), so `R`'s second variation is `Π(q) − c₀/4`. It is zero at
     `q = 0` because `R` vanishes along the uniform ray.
   - *Chessboard.* E3 gives `E_sea` unchanged and `Σw = N cosh ε`, so `R = −c₀N(cosh ε − 1)` exactly.
   - *Long wavelength.* `Π(q) − c₀/4 → (κ/4)|q|²`, with `κ` executed (block 76), and reproduced here (N2): `κ = 0.0807, 0.0884,
     0.0922` at `L = 6, 8, 10` for the smallest wavevector.
3. **PROVED + CHECKED (E7): the Euler lemma.** Let `E` have weight one and be translation invariant, and differentiate
   `E(e^t w) = e^t E(w)` at `t = 0`: `Σ_y ∂E/∂u_y = E`. Differentiating again in `u_x` at a uniform rate gives
   `Σ_y ∂²E/∂u_x∂u_y = ∂E/∂u_x = E[w̄·1]/N`. The row sum is the `q → 0` symbol of the Hessian. Checked exactly for both
   counter-terms on `2×2×2`.
4. **PROVED given a reading of A (Theorem 2).**
   - *A-rules have no mass term.* Under A a site's rate is a covariant weight-one function of its six neighbours' rates,
     `R(λ·) = λR(·)`. A static uniform empty lattice needs `R(1,…,1) = 1`. Linearising and applying Euler, the coefficients
     sum to `1`, which is the averaging law with no mass term (block 53's row 1, re-proved here in one line).
   - **ASSUMED:** the ledger's stationarity law (C) must be such an A-rule at weak field (the lane's row 10).
   - Given that, the Hessian's `q → 0` symbol must vanish, and by step 3 this is `E_field[w̄·1] = 0`.
5. **CHECKED, exact (E6, E8): Theorem 3.**
   - On `4³`, the second-order coefficient of `(1/3)Σ_bonds e^{(u_x+u_y)/2}` divided by that of `Σ_x e^{u_x}` is
     `1 − |q|²_lat/12` for six modes (`5/6, 2/3, 1/2, 2/3, 1/3, 0`). The per-bond term cancels the volume part at `q → 0`,
     cancels nothing at the chessboard, and leaves every mode in between partly uncancelled.
   - The family's stiffness `κ + (1−θ)c₀/12` and chessboard stiffness `θ|c₀|/4` follow.
   - With the declared values (`c₀ = −1193/1000`, `κ = 95/1000`) the stiffness is `95/1000`, `1087/24000` and `−53/12000` at
     `θ = 1, ½, 0`.
   - **NUMERIC (N2), on the actual sea:** the per-bond member's stiffness is `−0.0178, −0.0108, −0.0072` at `L = 6, 8, 10`,
     approaching zero from below. Its sign in infinite volume is **not** claimed; the exact part of the counterexample does not
     need it.
6. **PROVED: why the members all satisfy A and C.**
   - *A:* each has weight one and is covariant and nearest-neighbour, and by Theorem 2 each cancels the mass term, since they
     agree on uniform rates.
   - *C:* each gives a ledger and its stationarity law.
   - Requiring the law to determine every mode (a strict reading of C) excludes only `θ = 0`, which has the exact chessboard
     zero mode.
   - Every `θ ∈ (0, 1]` gives a law that is well posed, with a stiff chessboard. It is attractive at long wavelength for
     `θ > 1 − 12κ/|c₀|` (`= 53/1193` with the declared values).
   - These members differ in `γ_ind`. So no reading of A and C picks one.
7. **Arguing both ways (c).**
   - *For "consequence":* Theorem 2 forces the uniform value. C's source (block 55) is a site density, which suggests the
     site-local subtraction. Well-posedness excludes the per-bond extreme.
   - *For "supplied":* block 55's density is the derivative of the whole energy, not a rule for localising a subtraction; the
     per-bond localisation is equally "the sea's energy at the local rate". Theorem 3's family survives every constraint above,
     with different `γ`. The per-site form is exactly per-tick counting, fork (i), which block 76 and the fork probe found neither
     induced nor implied.
   - **The second is right.** The first failing step toward "a consequence of A and C alone" is selecting `θ = 1`.
8. **CHECKED, exact (E9, E10), and NUMERIC (N1): (d).**
   - *Second-order match.* Block 56's `F_γ = (2/γ)Σ_b(√w_x − √w_y)²` has second variation `(1/(2γ))Σ_b(u_x−u_y)²`. This
     matches `R`'s long-wavelength `(κ/2)Σ_b(u_x−u_y)²` iff `γ = 1/κ`.
   - *Chessboard mismatch.* `F_γ = (6/γ)N(c − 1/c)²`, while `R = (|c₀|/2)N(c − 1/c)²`. Their ratio is `12κ/|c₀|`, a first
     measure of how far `R` is from block 56's member.
   - *Block 56 re-derived.* Block 56's T1 and T3 hold with `γ = 200/19`. On a `5³` box with walls `φ = 1`, one body `m = 1`
     gives exactly `φ₀ = 1/(1 + (γ/12)g₀)`, with `g₀ = 136/99`, and its ledger lies below `12/(γg₀) = 0.8299`.
   - *On `Z³`.* `g₀` is the cubic walk's expected number of visits to the origin, `√6/(32π³) Γ(1/24)Γ(5/24)Γ(7/24)Γ(11/24)
     = 1.516386`, so `12κ/g₀ = 0.7518` or `0.7534`.

## 3. Where this stops

- **Step 4 relies on reading C's static law as an A-rule.** This is the lane's row 10. If A is read only as "weight one" and not
  as "the averaging form at weak field", then even the uniform value is not forced, and the volume term is simply allowed. The
  conclusion "supplied" only strengthens.
- **The sea's induced law is not a six-neighbour rule beyond second order.** On the chessboard `R`'s Hessian is `|c₀|/4`
  against the nearest-neighbour extrapolation `3κ` (ratio `12κ/|c₀| ≠ 1`). So strict A (six neighbours) is met only at long
  wavelength, with or without a counter-term.
- **Values.** `κ`, `c₀` (infinite volume) and the per-bond member's infinite-volume sign are executed values, not proved.
- **Scope.** This is a free, massless, filled sea with anticommuting composition, which block 78 found to be a comparator. The
  framework's sea, if any, is interacting.

## 4. What would finish it

1. A principle inside A–C that localises energies per site. None was found: block 55's density localises the derivative of
   the total, not a counter-term.
2. If fork (i) is supplied, the per-site counter-term follows from it: per-tick counting of a rate-independent density is
   `Σ_x w_x·const`. So the owner's single decision on fork (i) decides normal ordering too.
3. The infinite-volume stiffness `κ` (block 76: limit near `0.096–0.100`), which also decides the sign of the per-bond member's
   stiffness.
4. A referee from another model family.

## 5. Running it

```
python3 probes/work/derive/normal-ordering-as-a-rule/w-jonathonsmac4f50-jd669/check.py
```

It uses numpy, sympy and mpmath, and runs 12 checks in about 15 seconds. The walk identities compare dyadic-rational
floating-point arrays with `array_equal`. The counter-term, family and box statements use exact rationals. Items labelled
`NUMERIC` support no exact claim.

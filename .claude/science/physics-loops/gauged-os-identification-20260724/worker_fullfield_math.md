# Full (barred + unbarred) positive-time reflected Berezin Gram — construction and PSD decision

Worker report. Bounded piece only: mathematics + gate designs. No commits, no PRs, no
audit verdicts, no ledger edits. All source content read at `origin/main`
(`e6d1070adf fix: make flat-link census audit sources complete`).

**HEADLINE (stated up front so it cannot be mistaken):**

> The reflected Gram **IS positive semidefinite on the full barred+unbarred
> positive-time algebra** `A_+^full`. I could not find a negative minor, and I now
> have a *constructive* proof (an explicit Gram-of-vectors factorization verified
> exactly in sympy) that no negative minor exists. **The supervisor's prediction is
> confirmed.**
>
> **The sharp negative is somewhere else, and it is sharp.** On `A_+^full` the Gram
> is **not block-diagonal in Grassmann degree** — the constant mixes with the
> bilinears through the equal-time contact term — so the landed note's Theorem 4
> identity (Wick determinant = CAR-Fock exterior inner product) is **FALSE** on
> `A_+^full`, not merely unproven. The OS quotient has exact dimension `4^|Lambda|`,
> **not** the `2^|Lambda|` of the exterior algebra `Lambda^•(h)`. The naive full-field
> OS quotient is the GNS space of the one-slice *operator* algebra
> (`Fock (x) Fock*`, i.e. Hilbert-Schmidt operators on Fock), not Fock space.
> That is what the landed note was protecting against, and it is a positivity-safe
> but representation-fatal obstruction.

---

## 1. The landed unbarred construction, restated exactly

### 1.1 Action, chain operator, Berezin sign convention

The per-mode staggered temporal chain (spatial hop eigenvalue `i*lambda`), from
`docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:94-97`:

```text
    alpha_t psi_t + (1/2) psi_{t+1} - (1/2) psi_{t-1} = 0,
    alpha_t = m + i eta_1(t) sin(p) = m + i (-1)^t sin(p),
```

with the staggered phases fixed at
`docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:26`:
"the canonical staggered phases `eta_0 = 1` and `eta_1(t) = (-1)^t`".

The position-basis chain operator actually inverted by the landed runner is
`scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py:385-386`:

```text
    # Dense open chain D[(t,x),(s,y)] = (M I + (-1)^t H) delta_ts
    #                                  + 0.5 (delta_{s,t+1} - delta_{s,t-1}) I.
```

so the Euclidean action is `S = sum_{t,s} bar_chi_t D[t,s] chi_s`, i.e. in full,

```text
    S = sum_{t,x} bar_chi_{t,x} ( M chi_{t,x} + (-1)^t sum_y H[x,y] chi_{t,y} )
      + sum_{t,x} (1/2) ( bar_chi_{t,x} chi_{t+1,x} - bar_chi_{t,x} chi_{t-1,x} ),
```

with `H` the real anti-Hermitian staggered spatial hop
(`scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py:148-161`).
Realness/anti-Hermiticity is load-bearing and the note says so at line 441:
"real staggered hop (`H*=H`) | load-bearing carrier condition".

The Berezin/Wick sign convention is settled at
`scripts/mixed_os_transfer_representation_2026-05-30.py:105-106`:

```text
No ledger edits.  Settled Berezin sign convention
<chi_b bar_a>=+(M^-1)[b,a],   <bar_a chi_b>=-(M^-1)[b,a].
```

Write `G := D^{-1}` throughout, so `<chi_i bar_chi_j> = +G[i,j]`,
`<bar_chi_j chi_i> = -G[i,j]`, and `<chi chi> = <bar_chi bar_chi> = 0`.

### 1.2 Reflection and seam convention

`docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:286-287`:

> "Here reflection acts antimultiplicatively on Grassmann generators with the
> Osterwalder--Seiler sign convention `Theta(chi_t)=-bar-chi_(theta(t))`, as"

and the seam plane is fixed at
`scripts/mixed_os_transfer_representation_2026-05-30.py:244-248`:

```text
    OS reflection on the staggered Grassmann field across the plane between
    t=-1 and t=0:  theta(t)=(-1-t).  The Osterwalder-Seiler fermion reflection
    carries the gamma_0-type sign so that the reflected inner product is the
    physical (positive) metric:  Theta(chi_t) = - bar_chi_{theta t}  (and the
    overall sign is the OS convention, NOT a free parameter -- the OPPOSITE sign
```

So: `theta(t) = -1-t`, an involution reflecting through the **bond midpoint**
between `t=-1` and `t=0`. It is spatially local (`x` is untouched), and it **flips
the parity of `t`** — this is the whole reason two-step blocking works, see §2.3.

### 1.3 Block-time indexing

From `scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py:407-412`,

```text
        for b, tb in enumerate((0, 1)):
            tgt_row = (2 * (n - 1) + tb) + Nt
```

so cell (block time) `m` carries lattice times `(2m, 2m+1)`, even slot first;
block time `0` is `(0,1)` and its reflected image is cell `-1` = times `(-2,-1)`.
`theta` maps cell `m` to cell `-m-1` **and swaps the even/odd slots**
(`theta(2m) = 2(-m-1)+1`, `theta(2m+1) = 2(-m-1)`). That slot swap is exactly the
reordering hard-coded at lines 90-96 of the same runner.

### 1.4 The Gram definition actually computed

`scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py:85`
and `:127`:

```text
    """K_ab=<Theta chi_a chi_b>, a,b in {0,1}, theta(t)=-1-t.
...
            K[a, b] = G[target_shift + tb - tmin, (-1 - ta) - tmin]
```

i.e. `K[a,b] = G[t_b, theta(t_a)]`, with **no extra sign**, matching
`scripts/mixed_os_transfer_representation_2026-05-30.py:261`:

```text
            K[a, b] = -wick([('cb', idx(-1 - ta)), ('c', idx(tb))], Minv)
```

Unwinding: `wick([('cb',i),('c',j)]) = <bar_chi_i chi_j> = -G[j,i]`, so
`K[a,b] = +G[t_b, theta(t_a)]`. The two runners agree. In algebra terms

```text
    K_chi[a,b] = < Theta(chi_a) chi_b >
               = s_1 < bar_chi_{theta(t_a)} chi_{t_b} >
               = -s_1 G[t_b, theta(t_a)],        s_1 := sign in Theta(chi)= s_1 bar_chi,
```

so the runners' `+G[t_b, theta(t_a)]` **is** `s_1 = -1`. The landed result is then

`...NOTE_2026-07-12.md:109-126`:

```text
K_lambda
 = (2z/(1+z))
   [[1,             sqrt(z) b],
    [sqrt(z) b*,    z        ]]
 = 2z v_lambda v_lambda^dag,
...
K_lambda>=0,   rank K_lambda=1,   spec K_lambda={0,2z},
P_OS,lambda=K_lambda/(2z)=v_lambda v_lambda^dag.
```

and the restriction is stated at line 25: "positive-time unbarred block fields",
with the open residual at lines 362-364:

> "- reciprocal barred-field pole, contact/time-ordering terms, and a complete
>   all-field generating-functional identification beyond the positive-time
>   unbarred OS algebra proved here;"

---

## 2. How `Theta` acts on barred fields — enumeration, and what the action forces

Write the general convention (antilinear, antimultiplicative, spatially local,
`theta(t) = -1-t` fixed by §1.2):

```text
    Theta(chi_{t,x})     = s_1 bar_chi_{theta(t),x},
    Theta(bar_chi_{t,x}) = s_2 chi_{theta(t),x},
    Theta(c F) = conj(c) Theta(F),      Theta(F G) = Theta(G) Theta(F).
```

The landed note fixes `s_1 = -1` (§1.4). `s_2` is **not** written anywhere in the
landed note or either runner — this is genuinely an open convention slot, and it is
the crux the task names. Four sign choices exist; three independent constraints all
collapse to the *same* one.

### 2.1 Constraint A — involutivity

`theta(theta(t)) = -1-(-1-t) = t`, so

```text
    Theta^2(chi_t) = Theta(s_1 bar_chi_{theta t}) = conj(s_1) s_2 chi_t = s_1 s_2 chi_t
```

(`s_1` real). Hence `Theta^2 = id  <=>  s_1 s_2 = +1`. The alternative `s_1 s_2 = -1`
gives `Theta^2 = -1` on odd generators (a "`Theta^2 = (-1)^F`" convention).

### 2.2 Constraint B — Hermiticity of the Gram (**decisive, and computed**)

The reflected form `G(F,H) = <Theta(F) H>` must be Hermitian for "PSD" to even be a
meaningful question. Direct exact computation (scratch `probe3.py`, 16-dim
one-site full subalgebra of the `Ls=4` even torus, `M=1/2`):

| `(s_1,s_2)` | `max|G - G^dag|` | `min eig` |
|---|---|---|
| `(-1,-1)` | `1.67e-16` | `+6.976e-05` |
| `(-1,+1)` | `1.67e-16` | `+6.976e-05` |
| `(+1,+1)` | `1.67e-16` | `-7.625e-01` |
| `(+1,-1)` | **`1.19e+00`** | `-1.165e+00` |

So `s_1 s_2 = -1` **destroys Hermiticity outright**. Hermiticity of the reflected
Gram independently forces `s_1 s_2 = +1`.

### 2.3 Constraint C — the action's own `Theta`-covariance (the real derivation)

This is the constraint the task asks for: derived from the action, not posited.
Decompose the action into the terms

```text
    mass_hop(t) := sum_x bar_chi_{t,x}( M chi_{t,x} + (-1)^t sum_y H[x,y] chi_{t,y} ),
    bond(t)     := sum_x (1/2)( bar_chi_{t,x} chi_{t+1,x} - bar_chi_{t+1,x} chi_{t,x} ),
    S           = sum_t mass_hop(t) + sum_t bond(t).
```

**Mass/hop term.** Using antimultiplicativity,

```text
    Theta( bar_chi_{t,x} chi_{t,y} ) = Theta(chi_{t,y}) Theta(bar_chi_{t,x})
                                     = (s_1 bar_chi_{theta t, y})(s_2 chi_{theta t, x})
                                     = s_1 s_2  bar_chi_{theta t, y} chi_{theta t, x}.
```

Antilinearity conjugates the coefficient. The mass coefficient `M` is real. The hop
coefficient is `(-1)^t H[x,y]` with `H` **real antisymmetric**, and

```text
    conj( (-1)^t H[x,y] ) = (-1)^t H[x,y] = -(-1)^t H[y,x],
    (-1)^{theta(t)} = (-1)^{-1-t} = -(-1)^t,
```

so `conj((-1)^t H[x,y]) = (-1)^{theta(t)} H[y,x]`, which is precisely the coefficient
that multiplies `bar_chi_{theta t, y} chi_{theta t, x}` inside `mass_hop(theta(t))`.
Therefore

```text
    Theta( mass_hop(t) ) = s_1 s_2 * mass_hop( theta(t) ).                     (C1)
```

**The parity flip is doing all the work.** `theta` flips `(-1)^t`, and antilinearity
supplies the compensating conjugation. With the *single-step* reflection
`theta_1(t) = -t` one gets `(-1)^{-t} = +(-1)^t`, the two signs no longer cancel, and
(C1) fails for every `lambda != 0`. That is exactly the documented negative control
`scripts/mixed_os_transfer_representation_2026-05-30.py:268`:

```text
       Theta(chi_0)=+bar_{theta 0}.  Indefinite (the staggered eta_1 flip is not
```

**Bond term.** `Theta(bar_chi_{t,x} chi_{t+1,x}) = s_1 s_2 bar_chi_{-2-t,x} chi_{-1-t,x}`
and `Theta(bar_chi_{t+1,x} chi_{t,x}) = s_1 s_2 bar_chi_{-1-t,x} chi_{-2-t,x}`, so with
`u := -2-t` (so `u+1 = -1-t`),

```text
    Theta( bond(t) ) = s_1 s_2 * (1/2) sum_x ( bar_chi_{u,x} chi_{u+1,x}
                                             - bar_chi_{u+1,x} chi_{u,x} )
                     = s_1 s_2 * bond(-2-t).                                   (C2)
```

`t -> -2-t` maps `{t >= 0}` bijectively onto `{t <= -2}` and **fixes `t = -1`** — the
seam bond is `Theta`-invariant up to `s_1 s_2`.

**Conclusion.** `S` is `Theta`-covariant (`Theta` carries the positive-time action to
the negative-time action term-by-term) **iff `s_1 s_2 = +1`**.

Both (C1) and (C2) were verified **exactly in sympy** on the even torus `Ls=4`,
`M=1/2`, `Nt=2` (scratch `probe9.py`), returning `True` for every `t`.

### 2.4 The forced convention

Constraints A, B, C are independent and give the same answer; combined with the
landed note's `s_1 = -1`:

```text
    Theta(chi_{t,x})     = - bar_chi_{-1-t, x},
    Theta(bar_chi_{t,x}) = -     chi_{-1-t, x},          Theta^2 = id.
```

**The landed note's own reflection forces `s_2 = -1`.** There is no freedom left.

Residual freedom and its consequence: the simultaneous flip `(s_1,s_2) -> (+1,+1)`
preserves A/B/C but multiplies `Theta(F)` by `(-1)^{deg F}`; since the Gram is
block-diagonal in Grassmann-degree *parity*, this leaves the even sector untouched
and **negates the odd sector** (row 3 of the §2.2 table: `min eig = -0.7625`, which is
`-2z` up to the finite-`Nt` offset, `2z = 3-sqrt(5) = 0.763932`). So `s_1 = -1` is
load-bearing *only for the odd/fermionic sector*, and it is exactly the "NOT a free
parameter" claim of `mixed_os...py:247-249`.

---

## 3. The Gram on the enlarged basis

Let `A_+^full` = Grassmann algebra generated by `{chi_{t,x}, bar_chi_{t,x} : t >= 0}`.
`G(F,H) := <Theta(F) H>`, antilinear in `F`, linear in `H`.

### 3.1 Constant sector

`G(1,1) = <1> = 1` (normalised expectation). Nonzero — and this alone already breaks
the landed note's grade structure, see §3.4.

### 3.2 Linear sector — exactly block-diagonal, both blocks PSD

Because the measure is Gaussian with only a `bar_chi D chi` coupling, `<chi chi> = 0`
and `<bar_chi bar_chi> = 0`. Hence:

```text
  K_chi[a,b] := <Theta(chi_a) chi_b>     = -s_1 G[t_b, theta(t_a)] = +G[t_b, theta(t_a)],
  K_bar[a,b] := <Theta(bar_a) bar_chi_b> = +s_2 G[theta(t_a), t_b] = -G[theta(t_a), t_b],
  <Theta(chi_a) bar_chi_b> = s_1 <bar_chi_{theta a} bar_chi_b> = 0,
  <Theta(bar_a) chi_b>     = s_2 <chi_{theta a} chi_b>         = 0.
```

**The two cross blocks vanish identically** (verified numerically to
`0.00e+00`, exactly zero, scratch `probe6.py`). So on the linear sector

```text
    G|_linear = K_chi (+) K_bar          (orthogonal direct sum).
```

`K_chi` is the landed object. For `K_bar`, direct computation on the mode chain
(scratch `probe1.py`, `Nt=40`) gives, in the block basis `(chi_0, chi_1)` /
`(bar_chi_0, bar_chi_1)`:

| `(M,lambda)` | `K_chi` | `K_bar` |
|---|---|---|
| `(0.5, 0.7)` | `[[0.347859, 0.092776+0.129887i],[c.c., 0.073242]]` | `[[0.347859, -0.092776-0.129887i],[c.c., 0.073242]]` |
| `(0.37,-1.1)` | `[[0.242434, 0.028706-0.085341i],[c.c., 0.033441]]` | `[[0.242434, -0.028706+0.085341i],[c.c., 0.033441]]` |

i.e. **exactly**

```text
    K_bar = sigma_3 K_chi sigma_3 ,        sigma_3 = diag(1,-1),
```

a unitary similarity (the `sigma_3` is the even/odd slot swap that `theta` performs on
the cell, §1.3). Therefore

```text
    spec K_bar = spec K_chi = {0, 2z},     rank K_bar = 1,     K_bar >= 0,
    P_OS^bar = K_bar/(2z) = sigma_3 P_OS,lambda sigma_3.
```

Position-basis confirmation on the even torus `Ls=4`, `M=1/2`, `Nt=20`
(scratch `probe6.py`); both spectra are

```text
    {0, 0, 0, 0, 0.291796, 0.291796, 0.763932, 0.763932},
    spectral agreement K_chi vs K_bar: 5.55e-16,
```

and the exact `2z` values on that torus (`lambda = sin(2*pi*n/4) in {0,1,0,-1}`,
`M=1/2`) are

```text
    lambda = 0 :  2z = 3 - sqrt(5)   = 0.763932...
    lambda = 1 :  2z = 7 - 3 sqrt(5) = 0.291796...
```

each with multiplicity 2 — i.e. the **landed unbarred result is reproduced exactly**,
and the barred sector is its `sigma_3`-conjugate twin. Both have rank `dim h = 4`.

Operator form: since `K_chi = 2 U_pole Z U_pole^dag` (`...NOTE_2026-07-12.md:158-160`),
the barred block is

```text
    K_bar = 2 (sigma_3 (x) I) U_pole Z U_pole^dag (sigma_3 (x) I)
          = 2 U_bar Z U_bar^dag,      U_bar := [ Z^{1/2} B ; I ] (I+Z)^{-1/2},
```

which is `U_pole` with its two `dim h`-blocks interchanged. `U_bar^dag U_bar = I`,
so it is again an isometry and the barred OS quotient map is
`A_bar = sqrt(2) Z^{1/2} U_bar^dag`, `K_bar = A_bar^dag A_bar`.

### 3.3 Bilinear sector, and the exact small-torus Gram

Take the smallest exactly-computable arena: `L_s = 1`, `Nt = 2` (times `-2,-1,0,1`),
`M = 1/2`, so `A_+^full` is generated by `{chi_0, bar_chi_0, chi_1, bar_chi_1}` and is
16-dimensional. Exact rational Grassmann computation (scratch `probe7.py`, sympy,
no floats) gives `Z = det D = 5/16` and, ordering the basis
`1, X0, B0, X1, B1, X0B0, ...` (`X`=`chi`, `B`=`bar_chi`, subscript = block time),
the leading `6 x 6` principal block is **exactly**

```text
        1     0     0      0     0    4/5
        0    2/5    0     2/5    0     0
        0     0    2/5     0   -2/5    0
        0    2/5    0     2/5    0     0
        0     0   -2/5     0    2/5    0
       4/5    0     0      0     0    4/5
```

(row/col order `1, X0, B0, X1, B1, X0B0`). Note `G(1, chi_0 bar_chi_0) = 4/5`.

The exact full 16x16 spectrum is

```text
    0             multiplicity 12
    12/5          multiplicity 2
    (41 - sqrt(1105))/10   multiplicity 1
    (41 + sqrt(1105))/10   multiplicity 1
```

Both irrational eigenvalues are **exactly positive**: their sum is `41/5 > 0` and
their product is `(41^2 - 1105)/100 = 576/100 = 144/25 > 0`. So the exact spectrum is
`{0, 12/5, (41 ± sqrt(1105))/10}`, all `>= 0`, rank `4`.

### 3.4 The structural break: grade mixing / contact terms

In the **unbarred** algebra, `<Theta(chi_i) chi_j>` is the only nonvanishing
contraction pattern: same-side contractions vanish (`<chi chi> = 0` and
`<Theta(chi)Theta(chi)> = s_1^2 <bar_chi bar_chi> = 0`). Hence the Gram is *block
diagonal in Grassmann degree* and each block is a pure Wick determinant — which is
exactly `...NOTE_2026-07-12.md:290-295`:

```text
G_Berezin=det[ <xi_i,eta_j> ]
          =<xi_1 wedge ... wedge xi_q,
             eta_1 wedge ... wedge eta_q>_Fock.
```

In `A_+^full` this collapses. Same-side contractions no longer vanish:
`<chi_{t,x} bar_chi_{s,y}> = G[(t,x),(s,y)] != 0` for `t,s >= 0`. Explicitly
(scratch `probe5.py`, `Ls=4`, `M=1/2`, `Nt=20`, one-site subalgebra):

```text
  max |off-grade-diagonal entry| = 0.5962847988...
  G( 1 , X0B0 ) = +0.5962847928
  G( 1 , X0B1 ) = -0.4037152096
  G( 1 , X1B0 ) = +0.4037152096
  G( 1 , X1B1 ) = +0.5962847988
  G( 1 , X0X1B0B1 ) = -0.5185415282
  G( X0 , X0X1B1 ) = +0.3184725110
```

and the mechanism is transparent:

```text
    G(1, chi_{t,x} bar_chi_{s,y}) = <chi_{t,x} bar_chi_{s,y}> = G[(t,x),(s,y)],
```

the **equal-time / positive-time contact propagator**. Degree 0 pairs with degree 2.
This is precisely the "contact/time-ordering terms" residual named at
`...NOTE_2026-07-12.md:362-364`.

**Consequence:** `G|_{A_+^full}` is *not* a direct sum of exterior powers, and the
Theorem-4 identity `G_Berezin = det[<xi_i,eta_j>]` is **false** on `A_+^full`. It is
not "open"; it is refuted by the displayed `4/5` entry.

---

## 4. DECISION: PSD **HOLDS** on `A_+^full` — constructive proof

I searched hard for a negative minor (§4.4) and found none. Here is why none exists.

### 4.1 Arena remark (this is *not* an approximation)

The open temporal chain `t in [-N, N)` is **exactly** invariant under `theta(t) = -1-t`
(`t = -N |-> N-1`, `t = N-1 |-> -N`). So every finite open chain is an exact
reflection-symmetric arena, and the PSD question can be settled *exactly* there — no
appeal to the `N -> infinity` limit is needed. (The landed note's exponential-convergence
caveat at lines 331-339 concerns the *value* of `K_lambda`, not the positivity.)

### 4.2 The action splits with a manifestly OS seam

From (C1)+(C2) of §2.3 with `s_1 s_2 = +1`:

```text
    S_+     := sum_{t>=0} mass_hop(t) + sum_{t>=0} bond(t),
    Theta(S_+) = sum_{t<=-1} mass_hop(t) + sum_{t<=-2} bond(t),
    S_seam  := bond(-1) = (1/2) sum_x ( bar_chi_{-1,x} chi_{0,x} - bar_chi_{0,x} chi_{-1,x} ),

    S = S_+ + Theta(S_+) + S_seam.                                          (4.1)
```

Verified **exactly in sympy**, `Ls in {1,4}`, `Nt in {2,3}`, `M in {1/2, 3/4}`
(scratch `probe10.py`: `S = S+ + Theta(S+) + S_seam : verified exactly`).

Now invert the reflection on the seam. `Theta(chi_{0,x}) = -bar_chi_{-1,x}` gives
`bar_chi_{-1,x} = -Theta(chi_{0,x})`; `Theta(bar_chi_{0,x}) = -chi_{-1,x}` gives
`chi_{-1,x} = -Theta(bar_chi_{0,x})`. Substituting,

```text
  S_seam = (1/2) sum_x [ (-Theta(chi_{0,x})) chi_{0,x} - bar_chi_{0,x}(-Theta(bar_chi_{0,x})) ]
         = -(1/2) sum_x [ Theta(chi_{0,x}) chi_{0,x} + bar_chi_{0,x} Theta(bar_chi_{0,x}) ]   ... (i)
         = -(1/2) sum_x [ Theta(chi_{0,x}) chi_{0,x} + Theta(bar_chi_{0,x}) bar_chi_{0,x} ]   ... (ii)
```

step (i) -> (ii) uses that `bar_chi_{0,x}` and `Theta(bar_chi_{0,x})` are both odd, so
swapping them costs `-1`, cancelling the explicit minus. Hence

```text
    -S_seam = sum_{alpha} Theta(u_alpha) u_alpha ,
    u_alpha in { chi_{0,x}/sqrt(2), bar_chi_{0,x}/sqrt(2) : x in Lambda },     (4.2)
```

`|{alpha}| = 2|Lambda|`. (`Theta(c u) c u = |c|^2 Theta(u) u`, so the `1/2` is absorbed
by `c = 1/sqrt(2)`; the *positivity of that `1/2`* is load-bearing.) Verified exactly
in sympy for `Ls in {1,4}`, `Nt in {2,3}` (`-S_seam == (1/2) sum_alpha Theta(u_a)u_a : True`).

**This is the canonical Osterwalder-Seiler seam form, and the two-step staggered
action produces it with no extra sign.**

### 4.3 Seam expansion, the sign lemma, and the factorization

Each `w_alpha := (1/2) Theta(u'_alpha) u'_alpha` (bare generators `u'`) is even,
mutually commuting, and nilpotent (`w_alpha^2 = 0` since `u'^2 = 0`), so the
exponential terminates:

```text
    e^{-S_seam} = prod_alpha (1 + w_alpha) = sum_{A subset alpha} (1/2)^{|A|} Theta(U_A) U_A,
    U_A := u'_{alpha_1} ... u'_{alpha_k}   (A = {alpha_1 < ... < alpha_k}).     (4.3)
```

*Sign lemma* (needed for (4.3); induction on `k`): assume
`prod_{i<k} Theta(u_i)u_i = Theta(U')U'` with `U' = u_1...u_{k-1}` of degree `k-1`.
Then `Theta(U')U' Theta(u_k)u_k = (-1)^{k-1} Theta(U')Theta(u_k) U' u_k
= (-1)^{k-1} Theta(u_k U') U' u_k`, and `u_k U' = (-1)^{k-1} U' u_k = (-1)^{k-1} U_A`,
so `Theta(u_k U') = (-1)^{k-1} Theta(U_A)`, giving `(-1)^{2(k-1)} Theta(U_A) U_A
= Theta(U_A) U_A`. Base case `k=1` trivial. **All coefficients in (4.3) are `+(1/2)^{|A|} > 0`.**

Now insert (4.1) and (4.3) into `Z * G(F,H) = int dmu Theta(F) H e^{-S}`. Both
`e^{-S_+}` and `e^{-Theta(S_+)}` are even, hence central. Moving `Theta(U_A)` left past
`H` costs `(-1)^{|A||H|}`:

```text
  Z G(F,H) = sum_A (1/2)^{|A|} (-1)^{|A||H|} int dmu Theta(U_A F) (H U_A) e^{-S_+ - Theta(S_+)}.
```

The Berezin measure factorizes, `dmu = dmu_- dmu_+`, with `Theta` a bijection
`{+ generators} -> {- generators}`; `Theta(Y) e^{-Theta(S_+)}` lives entirely in the
`-` variables and `Y e^{-S_+}` entirely in the `+` variables. Define the **half-space
functional**

```text
    a(Y) := int prod_{i in P} dbar_chi_i dchi_i  [ Y e^{-S_+} ]   (a single number).
```

Then, for any positive-time `Y`,

```text
    Q(Y) := int dmu  Theta(Y) Y e^{-S_+} e^{-Theta(S_+)} = eps * |a(Y)|^2,      (4.4)
```

with `eps` a **universal constant** (independent of `Y`) — this is the
"reflection = complex conjugation on the Berezin measure" step, and it is where the
overall sign `s_1 = -1` is consumed. Taking `F = H` in the displayed line above,
`(-1)^{|A||F|}` appears twice (once from the reorder, once from
`F U_A = (-1)^{|F||A|} U_A F`) and cancels, leaving `Y_A := U_A F`. Therefore

```text
    G(F,H) = (eps/Z) * sum_A (1/2)^{|A|} conj( a(U_A F) ) * a(U_A H).           (4.5)
```

**(4.5) is an explicit Gram matrix of vectors** `v(H) := ( (1/2)^{|A|/2} a(U_A H) )_A`,
so `G >= 0` as soon as `eps/Z > 0`.

**Exact verification** (scratch `probe10.py`, `probe11.py`; sympy Rational, no floats):

| arena | `Z` | `Q(Y)=eps |a(Y)|^2`? | `eps` | `eps/Z` | (4.5) holds? |
|---|---|---|---|---|---|
| `Ls=1, Nt=2, M=1/2` | `5/16` | True (12 random complex-rational `Y`) | `1` | `16/5 > 0` | **True** (all 16x16 entries) |
| `Ls=1, Nt=3, M=1/2` | `13/64` | True | `1` | `64/13 > 0` | — |
| `Ls=1, Nt=2, M=3/4` | `205/256` | True | `1` | `256/205 > 0` | — |

`eps = 1` in every case. Hence:

```text
    G(F,H) = (1/Z) sum_A (1/2)^{|A|} conj(a(U_A F)) a(U_A H),     Z = det D > 0
    ==>  G >= 0  on A_+^full.                                                   QED
```

**Positivity of `Z`** is a genuine (small) side condition — it is the free-case
instance of the repo's separate determinant-positivity surface, named at
`docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:286-288`
("the determinant weight `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`").
I verified `Z > 0` only in the three exact cases above; see LIMITS.

### 4.4 Rank law — a sharp, falsifiable corollary, and it is exactly saturated

(4.5) writes `G` as a Gram of vectors indexed by subsets `A` of the `2|Lambda|` seam
generators. Hence, **independently of how many time slices `A_+^full` spans**,

```text
    rank G|_{A_+^full}  <=  2^{2|Lambda|} = 4^{|Lambda|}.                       (4.6)
```

This is a strong prediction: the algebra dimension is `4^{|Lambda| * n_slices}` but the
rank cannot grow with `n_slices`. Measured (scratch `probe6.py`, `M=1/2`):

| `|Lambda|` | `n_slices` | algebra dim | bound `4^{|Lambda|}` | **measured rank** |
|---|---|---|---|---|
| 1 | 2 | 16 | 4 | **4** |
| 1 | 3 | 64 | 4 | **4** |
| 1 | 4 | 256 | 4 | **4** |
| 2 | 2 | 256 | 16 | **16** |

**Exactly saturated in every case**, and flat in `n_slices` as predicted. The exact
`Ls=1,Nt=2` sympy Gram independently gives `rank = 4` with 12 exact zero eigenvalues
(§3.3). This is strong independent confirmation that (4.5) is the right factorization
and not an artifact.

### 4.5 Negative-minor search (what I actually tried, and it came up empty)

Systematic numeric sweep over the even torus `Ls=4` with the genuine nonzero staggered
hop, full Grassmann subalgebras built by literal Pfaffian/Wick contraction against a
dense inverse of the actual chain operator (scratch `probe5.py`):
`M in {0.2,0.5,1.0,2.0}` x `Nt in {4,6,10,20}` x site subsets
`{(0),(0,1),(0,2),(1,2)}`, plus a 4-slice run `slices=(0,1,2,3)`:

```text
    worst min-eigenvalue over the whole sweep:  -3.155e-15     (i.e. zero)
    4-slice runs, M in {0.5,1.0}, Nt in {6,10,16}: min_eig in [-8.7e-16, -2.5e-16]
```

No negative minor at any parameter. Combined with §4.3 I report this as a **proof of
PSD**, not merely an absence of counterexample.

---

## 5. Where positivity is tight, and what the real obstruction is

### 5.1 PSD holds everywhere, so "maximal subalgebra" is vacuous for positivity

There is no proper maximal subalgebra to identify: `G >= 0` on all of `A_+^full`.
The interesting maximal-subalgebra question is the *representation* one (§5.3).

### 5.2 The null directions are seam-blind, not "wrong-statistics"

The kernel is characterised by (4.5): `F` is null iff `a(U_A F) = 0` for every seam
subset `A`. Structurally the OS quotient is

```text
    A_+^full / ker G   ~=   (Grassmann algebra on the seam slice t=0)^*,
    dim = 4^{|Lambda|}   (exactly, §4.4).
```

So the null directions are exactly the positive-time observables that are invisible
to the `t=0` seam slice — everything that the half-space functional `a(.)` cannot
resolve. They are *not* wrong-statistics directions, and they are not seam-local
directions either; they are the complement of the seam-local directions. Concretely,
for `|Lambda|=1, n_slices=4` the algebra is 256-dimensional and the quotient is
4-dimensional: 252 null directions, all of them "deep positive time" combinations
already accounted for by the transfer semigroup.

In the linear sector the null space is the familiar one: `K_chi` has null vector
orthogonal to `v_lambda = (1+z)^{-1/2}[1, sqrt(z) b*]^T`
(`...NOTE_2026-07-12.md:116`) and `K_bar` has null vector `sigma_3` times that — i.e.
the *same* "orthogonal unphysical block-field combination" the landed note names at
line 177, once per sector.

### 5.3 The real obstruction: the quotient is `Fock (x) Fock*`, not `Fock`

Count. Per spatial site the staggered field has one Grassmann component, so the
one-slice Fock space of the transfer matrix has `dim F = 2^{|Lambda|}` and the
unbarred OS quotient is the exterior algebra:

```text
    unbarred:  quotient = Lambda^•(h) ~= F,          dim = 2^{|Lambda|},
    full:      quotient dim = 4^{|Lambda|} = (2^{|Lambda|})^2 = dim( F (x) F* ).
```

That is not a coincidence. The unbarred positive-time fields map to **creation
operators only**, whose GNS space over the vacuum is `F` itself — which is exactly why
the landed Theorem 4 gets a clean exterior-power answer. The full algebra maps onto
creation **and** annihilation operators, i.e. (a dense subalgebra of) `B(F)`, and its
GNS space over the reflection state is the Hilbert-Schmidt space
`HS(F) ~= F (x) F*`.

So the honest statement of the obstruction is:

> **The naive full-field OS quotient is positive but is the wrong object.** It is not
> a CAR-Fock space and it carries no exterior/`Gamma(Z)` structure; it is a
> *bimodule* (operator space). Any `A_+^full` analogue of
> `...NOTE_2026-07-12.md:290-295` must be a matrix-element statement about
> `Gamma(Z)^n` **conjugating** operators, not an exterior inner product of vectors.
> The `1 <-> chi bar_chi` contact term (`4/5` in the exact table of §3.3) is precisely
> the operator-trace direction that has no vector counterpart.

This is, I believe, exactly why the landed note stopped at the unbarred algebra, and
it is a *stronger* boundary than "we didn't get to it": the exterior identity is
**false** there, not unproven.

### 5.4 Two maximal "Fock-type" subalgebras, and they are incompatible

`G` is grade-diagonal with Wick-determinant blocks on exactly two subalgebras:

- `A_+^chi` (unbarred only) — the landed one. `<chi chi> = 0` and
  `<Theta(chi)Theta(chi)> = <bar bar> = 0` kill all same-side contractions.
- `A_+^bar` (barred only) — its `sigma_3`-conjugate twin. Same vanishing, with
  `K_bar = sigma_3 K_chi sigma_3` (§3.2), rank `dim h`, spectrum `{0, 2z}`.

Each is a maximal grade-diagonal subalgebra; their **join is all of `A_+^full`**, and
grade-diagonality fails immediately in the join (the degree-0/degree-2 contact term).
So "unbarred" is not an arbitrary restriction — it is one of exactly two maximal
choices, and the barred one is an equally good, physically conjugate alternative.

---

## 6. EXACT GATE DESIGNS (sympy, no float inputs)

All inputs rational; all comparisons exact (`==` on sympy expressions after
`simplify`, never `float`). Recall the memory lesson: sympy `==` is structural, so
compare via `simplify(expr) == 0` / zero-matrix identity, and never feed `Float`.

**Common fixture.** Even spatial torus `L_s = 4` (1D staggered ring; `L_s = 2` is
degenerate — nearest neighbours coincide and the hop vanishes identically, so `L_s=4`
is the smallest honest even torus), `H[x,y] = (1/2)(delta_{y,x+1} - delta_{y,x-1})`
exact rationals, mass `M = 1/2` (and a second point `M = 3/4`), open temporal chain
`t in [-N, N)`, `N in {2,3}`. Chain operator
`D[(t,x),(s,y)] = (M delta_xy + (-1)^t H[x,y]) delta_ts + (1/2)(delta_{s,t+1} - delta_{s,t-1}) delta_xy`,
`G = D^{-1}` by exact rational inversion.

**G0 — convention gate (forces `s_2`).** Assert all three, exactly:
1. `Theta^2 = id` on every generator  <=>  `s_1 s_2 = +1`.
2. `Theta(mass_hop(t)) - mass_hop(-1-t) == 0` and `Theta(bond(t)) - bond(-2-t) == 0`
   as Grassmann elements, for every `t`, at `s_1 s_2 = +1`; and assert **failure**
   for `s_1 s_2 = -1` (mutation control).
3. Reflected Gram Hermiticity: `G - G^dag == 0` at `s_1 s_2 = +1`, and
   `G - G^dag != 0` at `s_1 s_2 = -1` (this is the discriminator that measured
   `1.19e+00` numerically).
   Expected: `s_2 = -1` uniquely.

**G1 — linear-sector gate.** Build `K_chi`, `K_bar`, and the two cross blocks by
literal Berezin/Wick contraction against exact `G = D^{-1}`. Assert exactly:
- both cross blocks are the **zero matrix** (exact `0`, not a tolerance);
- `K_bar - sigma_3 K_chi sigma_3 == 0` (zero matrix), `sigma_3 = diag(1,-1)` per cell;
- `charpoly(K_chi) == charpoly(K_bar)`;
- eigenvalues of each are `{0 (mult 2|Lambda| - dim h), 2z_j}` with
  `2z_j` the exact algebraic numbers: on `L_s=4, M=1/2`,
  `2z in {3 - sqrt(5) (mult 2), 7 - 3 sqrt(5) (mult 2)}`.
  **This last line is the unbarred-sector regression gate against the landed note**
  (it reproduces `spec K_lambda = {0, 2z}`, `...NOTE_2026-07-12.md:123-124`, and
  `rank = dim h`, line 178, exactly and symbolically rather than at `1e-13`).
- Mutation control: replace `2z` by `2 e^{-E}` and assert the identity **fails**
  (mirrors the runner's control at line 536).

**G2 — grade-mixing gate (the sharp negative).** On the one-site full subalgebra,
assert **exactly** that
`G(1, chi_{0,x} bar_chi_{0,x}) = <chi_{0,x} bar_chi_{0,x}> = G[(0,x),(0,x)] != 0`,
and exhibit the exact rational value (`4/5` on the `L_s=1, N=2, M=1/2` fixture). Then
assert that the degree-0/degree-2 block of `G` is **not** zero, hence
`G != (+)_q (grade-q blocks)`, hence the Theorem-4 exterior identity
`G_Berezin = det[<xi_i,eta_j>]` **does not hold** on `A_+^full`. Report this as a
*refutation gate*, not a residual.

**G3 — seam-factorization gate (the PSD certificate).** Exactly:
1. `S - (S_+ + Theta(S_+) + S_seam) == 0` as a Grassmann element (`L_s = 4`, `N in {2,3}`).
2. `S_seam + (1/2) sum_{x,k} Theta(g_{k,0,x}) g_{k,0,x} == 0`, `k in {chi, bar_chi}`.
3. `e^{-S_seam} - sum_A (1/2)^{|A|} Theta(U_A) U_A == 0` (finitely many terms).
4. `Q(Y) - a(Y) conj(a(Y)) == 0` for a fixed list of complex-**rational**-coefficient
   test elements `Y` (assert the ratio is the *same* constant `eps` for all `Y`,
   and `eps == 1`).
5. `Z = det D` and assert `Z > 0` exactly (`Z = 5/16`, `13/64`, `205/256` on the small
   fixtures).
6. The identity (4.5) entrywise: `G - (1/Z) V^dag Delta V == 0` with
   `Delta = diag((1/2)^{|A|})`, `V[A,H] = a(U_A H)`.
   **Passing 1-6 is a proof certificate for `G >= 0`; no eigenvalue computation is
   needed and none should be used as the gate.**

**G4 — rank-law gate.** Assert `rank G = 4^{|Lambda|}` exactly, for
`(|Lambda|, n_slices) in {(1,2),(1,3),(1,4),(2,2)}` — in particular assert the rank is
**flat in `n_slices`** while the algebra dimension grows as `4^{|Lambda| n_slices}`.
Mutation control: assert that the *unbarred-only* subalgebra instead has rank
`2^{|Lambda|}` (its exterior-algebra dimension), exhibiting the `2^{|Lambda|}` vs
`4^{|Lambda|}` separation of §5.3 as an exact integer statement.

**G5 — single-step negative control.** Rerun G0/G1 with `theta_1(t) = -t`. Assert
`Theta(mass_hop(t)) != mass_hop(theta_1(t))` whenever `lambda != 0` (the `(-1)^{-t} = (-1)^t`
failure of §2.3) and that the resulting linear Gram is **indefinite** — reproducing the
repo's documented single-step no-go
(`docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:255`:
"`min eig = 0`, PSD), in direct contrast to the single-step naive Lagrangian Gram
(`min eig = -0.80`)"). This gate has teeth: it is the one place a negative minor
genuinely appears.

---

## 7. LIMITS (flagged, not smoothed)

1. **`eps = 1` and `Z > 0` are verified, not proved in general.** (4.4)-(4.5) were
   verified exactly only at `(L_s,N,M) in {(1,2,1/2), (1,3,1/2), (1,2,3/4)}`. The
   general statement "reflection = conjugation on the Berezin measure with a
   universal positive constant" is a standard Grassmann-measure fact but I did **not**
   rebuild it from primitives here. Per the repo's own standard (build cited algebra,
   do not just cite), a note shipping this must *derive* `eps` from the measure
   ordering, not assert it. **This is the single largest gap in my proof.**
2. **`Z = det D > 0`** is the free-case determinant-positivity side condition. I
   checked three fixtures. It is a genuine premise of (4.5), and it connects to the
   separate `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md` surface. Not
   established here for general `M`, `L_s`, `N`.
3. **`L_s = 1` and `L_s = 2` have identically zero 1D staggered hop** (nearest
   neighbours coincide mod `L_s`). All my *exact rational* computations — including
   the full 16x16 spectrum, `eps`, and the (4.5) identity — were done at `L_s = 1`,
   i.e. **at zero hop**. The nonzero-hop even torus (`L_s = 4`) was covered
   **numerically** (float `numpy`, dense chain inverse) and by **exact Grassmann
   identity checks** of (C1), (C2), (4.1), (4.2). The exact end-to-end (4.5)
   certificate at nonzero hop is **not** done — `L_s=4` with 2 slices needs a
   65536-dimensional Grassmann algebra.
4. **Rank saturation** `rank = 4^{|Lambda|}` is measured at `|Lambda| in {1,2}`, both of
   which have zero hop. The *bound* (4.6) is proved for all `|Lambda|`; **saturation at
   nonzero hop is untested.** The `L_s=4` runs I did are strict subalgebras where the
   bound is trivial (`4^4 = 256` >= algebra dimension), so they do not test it.
5. **3+1 vs 1+1.** I worked with the 1D spatial ring. The landed note's 3D lift
   argument (`...NOTE_2026-07-12.md:314-322`) is a per-mode + conjugate-eigenline
   argument that carries over verbatim for the *linear* sector, but the full-algebra
   rank law and the seam factorization were only computed in `d=1`. The seam
   factorization (4.1)-(4.2) is manifestly `d`-independent (it only uses the temporal
   bond structure and spatial locality of `theta`), so I expect no change; not verified.
6. **Free `U = 1` only.** Nothing here touches gauge links, `det M[U]`, or the
   `U`-integrated measure. The seam form (4.2) is where a gauge link would enter
   (`bar_chi_{-1} U_0 chi_0`), and temporal-gauge `U_0 = 1` is exactly what makes (4.2)
   come out with a real positive `1/2`. **Untested for `U != 1`.**
7. **Infinite temporal lattice.** I deliberately used the finite open chain because it
   is *exactly* reflection-symmetric (§4.1). The landed note's arena is the infinite
   lattice (lines 331-339). PSD on every finite `N` plus norm convergence gives PSD in
   the limit, but I did not write that limit argument out.
8. **`s_2` is my derivation, not a repo statement.** No landed note or runner records
   `Theta(bar_chi)`. §2 derives `s_2 = -1` three independent ways and I regard it as
   forced, but a reviewer could legitimately call it a new convention and demand it be
   landed explicitly before anything downstream cites it.
9. **What I did NOT do:** no interacting case, no continuum limit, no CAR-Fock
   *reconstruction* on `A_+^full` (I showed the exterior identity fails; I did **not**
   construct the correct `F (x) F*` replacement), no audit-pipeline run, no
   verification that `2^{|Lambda|}` is the right staggered one-slice Fock dimension
   under the repo's taste conventions (I used one Grassmann component per site, as in
   `AXIOM_FIRST_RP...NOTE_2026-05-28.md:25-26`).
10. **Numerics used floats.** Sections 3.2, 3.4, 4.4, 4.5 report `numpy` results
    (`1e-15`-level residuals). Only §2.2 (partly), §3.3, §4.2, §4.3 and the `eps`/`Z`
    table are exact rational/algebraic. The gate designs in §6 are specified to remove
    every float, but I did not implement them as a runner.

**Scratch artifacts** (not part of the repo, under the session scratchpad
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/`):
`gmach.py` (Pfaffian/Wick machine vs dense chain inverse), `gexact.py` (exact
symbolic Grassmann algebra), `probe1.py`, `probe3.py`, `probe5.py`, `probe6.py`,
`probe7.py`, `probe9.py`, `probe10.py`, `probe11.py`.

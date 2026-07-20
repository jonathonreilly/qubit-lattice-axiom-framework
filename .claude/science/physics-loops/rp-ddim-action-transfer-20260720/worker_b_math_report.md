# Worker B report — d-dimensional free-staggered two-step transfer identity

Role: bounded mathematics worker. Derivation only; no code run; no file
written but this report. Every displayed step is shown. Conventions are
taken verbatim from the three permitted sources and quoted where used.
Uncertainties and convention forks are flagged inline and collected in
LIMITS (item 6).

Source shorthands:
- **DISP** = `FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md`
- **RP** = `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`
- **CORNER** = `MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md`

---

## 0. Conventions quoted (the objects I rely on)

All from DISP unless tagged. Free `U = 1`, one Grassmann component per
site, `d` spatial axes, even spatial periods `L` per direction,
real `m > 0`.

DISP staggered phases and hop (DISP lines 82-90):

```text
    eta_0(t,x) = 1,
    eta_mu(t,x) = (-1)^(t + x_1 + ... + x_{mu-1}),   mu = 1,...,d,
    xi_mu(x)   = (-1)^(x_1 + ... + x_{mu-1}),
    H_hop = (1/2) sum_mu xi_mu(x) (tau_{+mu} - tau_{-mu}).
```

DISP mode equation and single-step matrices (DISP lines 97-105):

```text
    psi_{t+1} = -2 (m I + (-1)^t H_hop) psi_t + psi_{t-1},
    T_even = [[-2(m I + H_hop), I], [I, 0]],
    T_odd  = [[-2(m I - H_hop), I], [I, 0]],
    T_2    = T_odd T_even.
```

DISP two-site-cell fold (DISP lines 108-120): reduced momentum
`k in (-pi/2, pi/2]^d`, corner/taste label `r in {0,1}^d`, full momentum
`p_r = k + pi r`; the corner-shift vector `s_mu` has ones in slots `< mu`;

```text
    H_hop(k) = i sum_mu sin(k_mu) Gamma_mu,
    Gamma_mu |r> = (-1)^{r_mu} |r xor s_mu>,
    Gamma_mu^2 = I,   Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0 (mu != nu),
    H_hop(k)^2 = -(sum_mu sin^2 k_mu) I.
```

DISP calls the last line "the only dimension-dependent algebraic step"
(DISP line 135). DISP two-step scalar block (DISP lines 145-166):

```text
    a = m + i lambda,   lambda^2 = sum_mu sin^2 k_mu,
    T_even(lambda) = [[-2a, 1], [1, 0]],
    T_odd(lambda)  = [[-2 conj(a), 1], [1, 0]],
    T_2(lambda)    = [[4|a|^2 + 1, -2 conj(a)], [-2a, 1]],
    spec T_2(lambda) = { e^{+2E}, e^{-2E} },  E = arcsinh(sqrt(m^2 + lambda^2)),
    E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)).
```

Taste degeneracy (DISP line 52): `sin^2(k_mu + pi r_mu) = sin^2 k_mu`.

RP Step 3b projectors / selection (RP lines 146-169): reciprocal pair
`lambda_-(p)=e^{-2E(p)} in (0,1]`, `lambda_+(p)=e^{+2E(p)} >= 1`;

```text
    P_-(p) = (T2cl(p) - lambda_+ I) / (lambda_- - lambda_+),
    P_+(p) = (T2cl(p) - lambda_- I) / (lambda_+ - lambda_-),
    P_-^2=P_-, P_+^2=P_+, P_-P_+=0, P_-+P_+=I, T2cl P_- = lambda_- P_-;
```

"a forward solution with any `P_+` component grows like `lambda_+^N` over
`N` two-step blocks, so finite-action / finite-norm positive-time
propagation sets that coefficient to zero" (RP lines 159-161); one-mode
kernel `<bar z'|T_2|z> = exp(bar z' lambda_- z)` induces `diag(1,lambda_-)`
(RP lines 167-169).

RP Step 4 (RP lines 198-239): `Gamma(K)|vac>=|vac>`,
`Gamma(K) a_p^dag = lambda_p a_p^dag Gamma(K)`,
`T_hat^2 = Gamma(t1^(2)) = tensor_p diag(1,e^{-2E(p)}) = exp(-2 a_tau H_hat)`,
`H_hat = sum_p E(p) a_p^dag a_p`, `B = exp(-a_tau H_hat)`,
`H_hat = -log(T_hat^2)/(2 a_tau) >= 0`.

CORNER finite-mode theorem (CORNER lines 44-71). With
`F(H)=direct_sum_q wedge^q H`, `Gamma(A)=direct_sum_q wedge^q A`, and
`dGamma(X)` = sum of `X` over occupied slots:

```text
  (i)   Gamma(A) Gamma(B) = Gamma(AB)                     [functoriality]
  (ii)  Gamma(A) a^dag(f) = a^dag(Af) Gamma(A), Gamma(A)|vac>=|vac>
                                                          [canonical intertwiner]
  (iii) t>0:  Gamma(t)=exp(dGamma(log t)),  -log Gamma(t)=dGamma(-log t)
  (iv)  Tr_F Gamma(A) = det_H(1 + A)                      [trace]
  (v)   Gamma(direct_sum_k A_k) = tensor_k Gamma(A_k)     [direct sums]
```

CORNER also proves the pin is the intertwiner, **not** trace/positivity/
multiplication: `Gamma_tilde(A)=W Gamma(A) W^dag` (with `W` a nontrivial
number-preserving unitary inside a 2-particle sector) keeps (i),(iv) and
positivity but breaks (ii); for `t=diag(2,3,5)` it changes the entries of
`-log Gamma_tilde(t)` on the occupation states with eigenvalues 6 and 10
(CORNER lines 96-106). I use this counterexample as a discrimination probe
in item 5.

`a_tau` flag: DISP never introduces `a_tau` (its recursion has unit time
step). RP carries `a_tau` symbolically; CORNER writes
`-1/2 log T_k^2 = dGamma(E_k)`, i.e. `a_tau=1`. Per spec I set `a_tau=1`
and note that RP's `-log(T_hat^2)/(2 a_tau)` reduces to CORNER's
`-1/2 log T^2 = dGamma(E)` exactly at `a_tau=1`; a general `a_tau` only
rescales the generator (item 4, LIMITS L1).

---

## 1. Per-k classical structure from the action

**1.1 The corner matrix `S(k)` (honest match to the spec's `S(k)`).**
DISP works with `H_hop(k) = i sum_mu sin(k_mu) Gamma_mu`, whose square is
`-(sum_mu sin^2 k_mu) I`. Define the **Hermitian** corner matrix

```text
    S(k) := -i H_hop(k) = sum_mu sin(k_mu) Gamma_mu.
```

`S(k)` is Hermitian: `Gamma_1 = diag_r((-1)^{r_1})` is real diagonal, and
each `Gamma_mu` (`mu>=2`) is a real signed permutation that equals its own
transpose (verified in item 5, Gate A). Using
`Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 2 delta_{mu nu} I` (DISP: squares
are `I`, distinct ones anticommute):

```text
    S(k)^2 = sum_{mu,nu} sin k_mu sin k_nu Gamma_mu Gamma_nu
           = sum_mu sin^2 k_mu (Gamma_mu^2)  [cross terms cancel pairwise]
           = (sum_mu sin^2 k_mu) I
           = (sum_mu sin^2 p_mu) I           [sin^2(k_mu+pi r_mu)=sin^2 k_mu].
```

So `S(k)^2 = (sum_mu sin^2 p_mu) I`. **Flag (honest correction, not
forcing):** the spec calls this "diagonal with entries `sum_mu sin^2 p_mu`";
the note's algebra delivers the *stronger* fact that `S(k)^2` is that scalar
times the identity — all `2^d` diagonal entries equal, off-diagonal zero.
This scalar-square is exactly what collapses the block to a single 2x2
recursion and forces taste degeneracy (below). `S(k)` itself is generally
**not** diagonal (see 1.3).

**1.2 Dimension of the per-reduced-momentum two-step classical block.**
At fixed reduced momentum `k`, the amplitude on one time slice lives in the
corner space `C^{2^d}` (one component per taste corner `r in {0,1}^d`). The
classical transfer acts on the phase-space doubling
`V_t = (psi_t, psi_{t-1})`, so `V_t in C^{2^d} (+) C^{2^d} = C^{2^{d+1}}`.
Hence the per-`k` two-step classical block

```text
    T_2(k) : C^{2^{d+1}} -> C^{2^{d+1}},   dimension 2^{d+1} = 2 * 2^d.
```

(DISP reduces straight to 2x2 per eigenline; the `2^{d+1}` assembly is
mine, stated so the supervisor can size the runner objects.)

**1.3 Why the taste corners couple (d >= 2), and why d = 1 does not.**
The corner-shift `s_mu` has ones only in slots `< mu` (DISP line 113):

```text
    s_1 = (0,...,0)      -> Gamma_1 |r> = (-1)^{r_1} |r>          (diagonal),
    s_mu != 0 (mu>=2)    -> Gamma_mu |r> = (-1)^{r_mu} |r xor s_mu> (off-diag).
```

Physically (DISP lines 113-115): multiplication by the staggered phase
`xi_mu(x)` shifts the corner by `s_mu`, so a spatial hop in direction
`mu >= 2` connects corner `r` to the **different** corner `r xor s_mu`.
Therefore for `d >= 2` the matrices `Gamma_2,...,Gamma_d` are off-diagonal
and `S(k) = sum_mu sin(k_mu) Gamma_mu` mixes the `2^d` corners: the two-step
transfer is **not** corner-block-diagonal. In `d = 1` only `Gamma_1`
(diagonal) occurs, `S(k)=sin(k) diag(1,-1)` is already diagonal, and the two
corners `r in {0,1}` never mix — the coupling is the genuinely new `d>=2`
feature. It is exactly compensated by `S(k)^2 = (sum sin^2)I` (a scalar), so
despite the coupling the block still reduces to 2x2 pieces (1.5).

**1.4 The two-step block is a matrix function of `S(k)`.** Substitute
`H_hop(k) = i S(k)` into the block matrices and multiply the `2x2`-of-blocks
(each block `2^d x 2^d`):

```text
    T_even(k) = [[ -2(m I + i S(k)),  I ],
                 [        I,          0 ]],
    T_odd(k)  = [[ -2(m I - i S(k)),  I ],
                 [        I,          0 ]].
```

`T_2(k) = T_odd(k) T_even(k)`, block entries:

```text
  (1,1): (-2(mI - iS))(-2(mI + iS)) + I*I
        = 4(mI - iS)(mI + iS) + I
        = 4(m^2 I + i m S - i m S - i^2 S^2) + I
        = 4 m^2 I + 4 S(k)^2 + I  = (4 m^2 + 1) I + 4 S(k)^2,
  (1,2): -2(mI - iS) * I + I*0 = -2(mI - iS),
  (2,1): I*(-2(mI + iS)) + 0*I = -2(mI + iS),
  (2,2): I*I + 0*0 = I.
```

Hence, **manifestly a function of `S(k)`**,

```text
    T_2(k) = [[ (4 m^2 + 1) I + 4 S(k)^2 ,  -2(m I - i S(k)) ],
              [   -2(m I + i S(k)) ,               I         ]].
```

Using `S(k)^2 = lambda^2 I` with `lambda^2 = sum_mu sin^2 k_mu`, the (1,1)
block is `(4 m^2 + 4 lambda^2 + 1) I = (4|a|^2 + 1) I`, `a = m + i lambda`.

**1.5 Reduction to the d = 1 per-mode 2x2 recursion.** `S(k)` is Hermitian
with `S(k)^2 = lambda^2 I`, so it has exactly two eigenvalues `+lambda` and
`-lambda` (`lambda = sqrt(sum_mu sin^2 k_mu) >= 0`), each of multiplicity
`2^{d-1}` (trace `S(k)=0`: `Gamma_1` is traceless and each off-diagonal
`Gamma_mu` has no fixed corner). Pick an eigenvector `w` of `S(k)`,
`S(k) w = sigma w`, `sigma in {+lambda,-lambda}`. On the 2-dim line
`span{(w,0),(0,w)}` the block `T_2(k)` restricts to

```text
    T_2(sigma) = [[ 4 m^2 + 4 sigma^2 + 1,  -2(m - i sigma) ],
                  [   -2(m + i sigma),             1        ]]
               = [[ 4|a|^2 + 1,  -2 conj(a) ],
                  [   -2a,             1     ]],   a = m + i sigma,
```

which is **exactly DISP's `T_2(lambda)`** with the scalar `lambda -> sigma`
and `sin^2 p -> sum_mu sin^2 p_mu` (through `sigma^2 = lambda^2 =
sum sin^2 k_mu = sum sin^2 p_mu`). This is DISP's line 142 statement made
per-eigenline. Full displayed spectrum of this 2x2 (every step):

```text
    det T_2(sigma) = (4|a|^2+1)(1) - (-2 conj a)(-2a) = 4|a|^2 + 1 - 4|a|^2 = 1,
    tr  T_2(sigma) = (4|a|^2 + 1) + 1 = 2 + 4|a|^2 = 2 + 4(m^2 + sigma^2) =: 2 + 4R.
```

Characteristic equation `mu^2 - (tr) mu + (det) = 0`, i.e.
`mu^2 - (2+4R) mu + 1 = 0`:

```text
    mu = ( (2+4R) +/- sqrt((2+4R)^2 - 4) ) / 2,
    (2+4R)^2 - 4 = 4 + 16R + 16R^2 - 4 = 16 R (1 + R),
    sqrt(...) = 4 sqrt(R(1+R)),
    mu_+/- = 1 + 2R +/- 2 sqrt(R(1+R)).
```

Set `sinh E = sqrt(R)` (so `sinh^2 E = R`, `cosh^2 E = 1 + R`,
`sinh E cosh E = sqrt(R(1+R))`). Then

```text
    e^{+2E} = cosh 2E + sinh 2E = (1 + 2 sinh^2 E) + 2 sinh E cosh E
            = 1 + 2R + 2 sqrt(R(1+R)) = mu_+,
    e^{-2E} = 1 + 2R - 2 sqrt(R(1+R)) = mu_-,
    E = arcsinh(sqrt(R)),  R = m^2 + sigma^2 = m^2 + sum_mu sin^2 p_mu.
```

So `spec T_2(sigma) = { e^{+2E_d(p)}, e^{-2E_d(p)} }`,
`E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu))`.

**1.6 Taste degeneracy.** `R` depends on `sigma` only through
`sigma^2 = lambda^2`, identical for both eigenvalues `+lambda, -lambda`; and
`lambda^2 = sum_mu sin^2 k_mu = sum_mu sin^2 p_mu` for every corner
`r` (since `sin^2(k_mu + pi r_mu) = sin^2 k_mu`). Therefore all `2^d`
corner-eigenmodes at a fixed reduced momentum `k` share one and the same
`E_d`, and the full `2^{d+1}`-dim block spectrum is

```text
    { e^{+2E_d(p)} with multiplicity 2^d,  e^{-2E_d(p)} with multiplicity 2^d }.
```

The `2^d` decaying modes at reduced momentum `k` are the `2^d` full momenta
`p = k + pi r`; unfolding over the `(L/2)^d` reduced momenta gives one
decaying mode per full momentum, `L^d` total (item 4 mode count). This is
exactly the d = 1 recursion with `sin^2 p -> sum_mu sin^2 p_mu`,
taste-degenerate, as required.

---

## 2. Forward-channel selection at general d

I follow RP Step 3b verbatim-in-structure, per corner-eigenmode. Index the
modes by `(k, alpha)`, where `k` is the reduced momentum and `alpha` runs
over the `2^d` eigenvectors of `S(k)` (an eigenvalue `sigma_alpha in
{+lambda, -lambda}` with `lambda = sqrt(sum_mu sin^2 k_mu)`); each `(k,alpha)`
unfolds to one full momentum `p`.

**2.1 Explicit spectral projectors per mode.** On the 2x2 block
`T_2(sigma_alpha)` the two eigenvalues are the reciprocal positive reals

```text
    lambda_-(p) = e^{-2 E_d(p)} in (0, 1],   lambda_+(p) = e^{+2 E_d(p)} >= 1,
    lambda_-(p) lambda_+(p) = 1  (det T_2 = 1),  m > 0 => lambda_- < 1 < lambda_+
                                                     strictly unless p forces
                                                     sum sin^2 = 0, where
                                                     lambda_+- = e^{+-2 arcsinh m}.
```

Their Riesz projectors (RP lines 153-154, per block):

```text
    P_-(k,alpha) = (T_2(sigma_alpha) - lambda_+ I_2) / (lambda_- - lambda_+),
    P_+(k,alpha) = (T_2(sigma_alpha) - lambda_- I_2) / (lambda_+ - lambda_-).
```

Because `lambda_- != lambda_+` (guaranteed by `m > 0`, so the denominators
never vanish) these obey, by the standard two-eigenvalue calculation,

```text
    P_-^2 = P_-,  P_+^2 = P_+,  P_- P_+ = P_+ P_- = 0,  P_- + P_+ = I_2,
    T_2(sigma_alpha) P_- = lambda_- P_-,   T_2(sigma_alpha) P_+ = lambda_+ P_+.
```

(Proof of `P_-+P_+=I`: `[(T_2 - lambda_+ I) - (T_2 - lambda_- I)]/(lambda_- -
lambda_+) = (lambda_- - lambda_+)I/(lambda_- - lambda_+) = I`. Proof of
`T_2 P_- = lambda_- P_-`: `T_2 P_- = [(T_2 - lambda_+ I) + lambda_+ I]P_- =
0 + ... ` use `(T_2-lambda_-I)(T_2-lambda_+I)=0` Cayley-Hamilton, so
`(T_2-lambda_+I)` maps into the `lambda_-` eigenspace; explicitly
`(T_2 - lambda_- I)P_- = (T_2-lambda_-I)(T_2-lambda_+I)/(lambda_- -
lambda_+) = 0`. Idempotence and orthogonality follow from
`(T_2-lambda_-I)(T_2-lambda_+I)=0` likewise.)

**2.2 Finite-norm / finite-action argument killing the growing channel.**
Verbatim in structure from RP lines 159-161: a positive-time solution with a
nonzero `P_+` component multiplies that component by `lambda_+ = e^{+2E_d}`
at each two-step block, so after `N` blocks it carries the factor
`lambda_+^N = e^{+2 N E_d(p)}`, which diverges as `N -> infinity` because
`E_d(p) >= arcsinh(m) > 0`. Finite-action / finite-norm positive-time
propagation therefore forces the `P_+` coefficient to zero, and the forward
propagation runs on `P_-`. In the diagonal one-particle basis the forward
kernel of mode `(k,alpha)` is the surviving eigenvalue

```text
    K_2(k,alpha) = lambda_-(p) = e^{-2 E_d(p)}.
```

The growing reciprocal channel `lambda_+` is the inverse backward-time
solution, not the forward transfer kernel (RP lines 163-164).

**2.3 Assembly into the one-particle two-step kernel.** Collecting the
survivors over all `L^d` modes,

```text
    t1^(2)_d = diag over modes (k,alpha) of e^{-2 E_d(p)}
             = diag over full momenta p in (full BZ) of e^{-2 E_d(p)},
    E_d(p) = arcsinh(sqrt(m^2 + sum_mu sin^2 p_mu)),   (L^d) diagonal entries.
```

**2.4 Which sentence is dimension-blind, which needs the d-dim
decomposition.** This is the crisp separation the spec asks for.

- **Dimension-blind** (identical to d = 1, RP Step 3b, once you are on one
  2x2 block): the projector formulas `P_-+/-= (T_2 - lambda_-/+ I)/
  (lambda_-/+ - lambda_-/+)`; the reciprocal-eigenvalue structure
  `lambda_- lambda_+ = 1`; and the load-bearing selection sentence "*a
  forward solution with any `P_+` component grows like `lambda_+^N` over `N`
  two-step blocks, so finite-action / finite-norm positive-time propagation
  sets that coefficient to zero*" (RP lines 159-161). Nothing in this
  sentence knows `d`: it is a statement about the reciprocal spectrum of a
  single 2x2 monodromy block.

- **Needs the d-dim mode decomposition**: the step that *produces the 2x2
  blocks in the first place* — diagonalizing `S(k) = sum_mu sin(k_mu)
  Gamma_mu` on the `2^d`-dim corner space to split `T_2(k)` (dimension
  `2^{d+1}`) into `2^d` decoupled 2x2 blocks. This is DISP's Clifford
  algebra `S(k)^2 = (sum sin^2 k_mu)I`, "the only dimension-dependent
  algebraic step" (DISP line 135). The value `lambda^2 = sum_mu sin^2 k_mu`,
  the corner count `2^d`, and the identification of each eigenmode with a
  full momentum `p = k + pi r` are all d-dependent. Without this
  decomposition there is no per-mode 2x2 block for the d-blind selection
  argument to act on. In one sentence: **the selection is d-blind; the
  furnishing of the modes it selects on is where d enters.**

---

## 3. Per-mode coherent-state -> exterior bridge with C = 1

**3.1 The one imported fact.** The standard fermionic coherent-state
correspondence (Negele-Orland; the correspondence RP and CORNER both
assume): for one mode with `{a,a^dag}=1`, `n=a^dag a`, the Grassmann
coherent states satisfy `<bar z'|z> = e^{bar z' z}`, and for a
normal-ordered operator `:Omega(a^dag,a):`,

```text
    <bar z'| :Omega(a^dag,a): |z> = Omega(bar z', z) e^{bar z' z}.
```

In particular `<bar z'| n |z> = bar z' z e^{bar z' z}` and
`<bar z'| (1-n) |z> = e^{bar z' z} - bar z' z e^{bar z' z} =
(1 + bar z' z)(1 - bar z' z) = 1` (since `(bar z' z)^2 = 0`).

**3.2 Derivation of the induced operator `diag(1, lambda)` (both
directions).** The kernel `exp(bar z' lambda z)` conserves number (depends
only on `bar z' z`), so the induced operator is diagonal,
`T = T_0 (1-n) + T_1 n = diag(T_0, T_1)`. Its kernel is, using 3.1,

```text
    <bar z'| T |z> = T_0 <bar z'|(1-n)|z> + T_1 <bar z'| n |z>
                   = T_0 * 1 + T_1 * (bar z' z)
                   = T_0 + T_1 bar z' z.
```

Match to `exp(bar z' lambda z) = 1 + lambda bar z' z` (the series truncates,
`(bar z' z)^2 = 0`):

```text
    T_0 = 1,   T_1 = lambda   =>   T = diag(1, lambda).
```

Forward check (the other direction): `diag(1,lambda) = 1 + (lambda-1)
a^dag a` is already normal-ordered, so

```text
    <bar z'| diag(1,lambda) |z> = [1 + (lambda-1) bar z' z] e^{bar z' z}
        = [1 + (lambda-1) bar z' z][1 + bar z' z]
        = 1 + bar z' z + (lambda-1) bar z' z + (lambda-1)(bar z' z)^2
        = 1 + lambda bar z' z = exp(bar z' lambda z).   [checks]
```

So the induced operator on the 2-dim exterior algebra `wedge^0 (+) wedge^1`
is **exactly `diag(1, lambda)`**, matching RP line 169. (This routing
through `n` and `1-n`, whose kernels `bar z' z` and `1` are
sign-unambiguous, sidesteps the coherent-state sign convention that would
otherwise leave `+/- lambda` ambiguous; the sign fork is flagged in LIMITS
L3, and is physically inert here because `lambda = lambda_- = e^{-2E_d} > 0`
in all uses.)

**3.3 Vacuum matrix element = 1, explicitly (the C = 1 statement).** The
constant (Grassmann-scalar, `z=z'=0`) term of `exp(bar z' lambda z)` is
`exp(0) = 1`. Equivalently `<0| diag(1,lambda) |0> = T_0 = 1`. So the
vacuum->vacuum amplitude is exactly `1`, with **no scalar prefactor `C`**:
the induced operator is `diag(1,lambda)`, not `C * diag(1,lambda)`.

**3.4 Why this DERIVES the overall normalization (no scalar ambiguity).**
A generic quasi-free / Gaussian second quantization is a priori defined only
up to an overall scalar `C` (a Gaussian determinant/normalization). Here `C`
is pinned to `1`, not chosen, for two reinforcing reasons:

1. *Per mode*: the coherent kernel is an exponential `exp(bar z' lambda z)`
   whose constant term is `exp(0)=1`; there is no free multiplicative
   constant to carry, because a nonzero constant `C` would appear as
   `C exp(bar z' lambda z)` with constant term `C != 1`, contradicting the
   exponential form supplied by the action.
2. *Many-body*: once the many-body coherent kernel factorizes over modes
   (3.5), the vacuum->vacuum amplitude is the product of the per-mode vacuum
   terms, `prod_modes 1 = 1`. Hence `T_hat^2 |vac> = |vac>` exactly.

This is exactly CORNER's canonical intertwiner (ii): `Gamma(A)` **fixes the
vacuum**, `Gamma(A)|vac>=|vac>`. The `C=1` fact and the vacuum-fixing are the
same statement; and CORNER shows this vacuum-fixing / intertwiner is the
*pin* that trace + positivity + multiplication (items i, iv) do **not**
supply (the `W`-conjugate `Gamma_tilde` breaks exactly (ii)). So the
normalization is derived by the coherent-state kernel's constant term = 1,
which realizes the intertwiner's vacuum-fixing, not posited.

**3.5 Factorization of the blocked quadratic action's coherent kernel over
the `S(k)` eigenmodes.** The free `U=1` blocked action is quadratic. Written
in the mode basis `{(k,alpha)}` that diagonalizes `S(k)` (item 1.5) and after
forward-channel selection (item 2), the one-particle two-step kernel
`t1^(2)_d = diag over modes of lambda_{k,alpha}`,
`lambda_{k,alpha} = e^{-2 E_d(p)}`, is **diagonal**. Its coherent-state
kernel is the exponential of the associated diagonal quadratic form:

```text
    <bar z'| T_hat^2 |z> = exp( sum_{(k,alpha)} bar z'_{k,alpha}
                                     lambda_{k,alpha} z_{k,alpha} )
                         = prod_{(k,alpha)} exp( bar z'_{k,alpha}
                                     lambda_{k,alpha} z_{k,alpha} ).
```

**Cross terms `bar z'_m z_{m'}` (`m != m'`) vanish** precisely because the
quadratic form is diagonal in this basis: the modes are the eigenvectors of
`S(k)` (hence of the single-particle kernel), so `t1^(2)_d` has no
off-diagonal entries and the exponent has no mixed `m,m'` term. The
factorized exponential is a product of single-mode kernels each of the form
`exp(bar z' lambda z)`, so by 3.2 the induced many-body operator is the
tensor product

```text
    T_hat^2 = tensor_{(k,alpha)} diag(1, lambda_{k,alpha})
            = tensor_modes diag(1, e^{-2 E_d(p)}),
```

and by 3.3 each factor contributes vacuum term `1`, giving `C=1` for the
whole many-body operator (3.4). This is the DISP/RP object realized at
general `d`; the functorial packaging is item 4.

---

## 4. Assembly (using CORNER's finite-mode theorem)

Let `H_1 = C^{L^d}` be the one-particle space (one mode per full momentum
`p`, taste included), `t1^(2)_d : H_1 -> H_1` diagonal with entries
`e^{-2 E_d(p)} > 0`. `F(H_1) = direct_sum_q wedge^q H_1` is the fermionic
Fock space, dimension `2^{L^d}`. I invoke CORNER items by number.

**4.1 `T_hat^2_d = Gamma(t1^(2)_d) = tensor_modes diag(1, e^{-2E_d}) = B^dag B`.**
By item 3.5 the many-body two-step operator is `Gamma(t1^(2)_d)` (the
number-conserving second quantization). Since `t1^(2)_d = direct_sum_p
(e^{-2 E_d(p)})` is a direct sum of the `L^d` one-dimensional mode blocks,
CORNER (v) [direct sums] gives

```text
    T_hat^2_d = Gamma(t1^(2)_d) = Gamma(direct_sum_p e^{-2E_d(p)})
              = tensor_p Gamma(e^{-2E_d(p)}) = tensor_p diag(1, e^{-2E_d(p)}),
```

each single-mode `Gamma(e^{-2E_d(p)}) = diag(1, e^{-2E_d(p)})` from item 3.2.
Define `B = exp(-a_tau H_hat_d)` (item 4.2). Since every factor is real
diagonal,

```text
    B = tensor_p diag(1, e^{-a_tau E_d(p)}),
    B^dag B = tensor_p diag(1, e^{-2 a_tau E_d(p)}) = T_hat^2_d  (at a_tau=1),
```

so `T_hat^2_d = B^dag B` is manifestly positive Hermitian, `||T_hat^2_d|| = 1`
(the vacuum factor), matching RP line 235. (`a_tau` carried; `a_tau=1`
default, LIMITS L1.)

**4.2 `H_hat_d = -log(T_hat^2_d)/(2 a_tau) = dGamma(E_d) >= 0`.** Each
`e^{-2E_d(p)}` is strictly positive (`m>0` gives `E_d(p) >= arcsinh(m) > 0`,
so `e^{-2E_d(p)} in (0,1)`), so `t1^(2)_d` is strictly positive and CORNER
(iii) [positive logarithm] applies:

```text
    -log Gamma(t1^(2)_d) = dGamma(-log t1^(2)_d)
                         = dGamma(-log(e^{-2E_d})) = dGamma(2 E_d) = 2 dGamma(E_d).
```

Divide by `2 a_tau`:

```text
    H_hat_d := -log(T_hat^2_d) / (2 a_tau) = dGamma(E_d) / a_tau
             = dGamma(E_d)   (at a_tau = 1),
```

where `dGamma(E_d) = sum_p E_d(p) a_p^dag a_p` is the number-operator sum
(CORNER's `dGamma` = sum over occupied slots). Since `E_d(p) >= 0` for every
`p`, `dGamma(E_d) >= 0`, so `H_hat_d >= 0`. This is RP line 239 and CORNER's
`-1/2 log T^2 = dGamma(E)` at general `d`. Equivalently
`T_hat^2_d = exp(-2 a_tau H_hat_d)` (CORNER (iii) run forward).

**4.3 `Tr T_hat^2_d = det(1 + t1^(2)_d) = prod_modes (1 + e^{-2E_d})`.** By
CORNER (iv) [trace identity], `Tr_F Gamma(A) = det_{H_1}(1 + A)` with
`A = t1^(2)_d`:

```text
    Tr_F T_hat^2_d = det_{H_1}(1 + t1^(2)_d)
                   = prod_p (1 + e^{-2 E_d(p)})   [t1^(2)_d diagonal].
```

CORNER's own derivation (CORNER lines 80-83) is the occupation sum
`sum_{S} prod_{j in S} lambda_j = prod_j (1 + lambda_j)`; here
`lambda_j = e^{-2E_d(p_j)}`, product over the `L^d` modes.

**4.4 Mode count.** The reduced BZ has `(L/2)^d` momenta `k`; each carries
`2^d` taste corners `r`; unfolding `p = k + pi r` gives

```text
    (L/2)^d * 2^d = (L^d / 2^d) * 2^d = L^d,
```

one decaying forward mode per full momentum, matching `dim H_1 = L^d` and
`dim F(H_1) = 2^{L^d}`.

**4.5 The defining intertwiner at general `d` (displayed).** The object is
pinned (item 3.4, CORNER (ii)) by: `Gamma(t1^(2)_d)` fixes the vacuum and
intertwines the canonical creation operators. For any one-particle `f in
H_1`,

```text
    Gamma(t1^(2)_d) a^dag(f) = a^dag( t1^(2)_d f ) Gamma(t1^(2)_d),
    Gamma(t1^(2)_d) |vac> = |vac>,
```

and componentwise, with `a_p^dag` creating the (taste-labelled) full-momentum
mode `p` and `(t1^(2)_d f)(p) = e^{-2 E_d(p)} f(p)`,

```text
    Gamma(t1^(2)_d) a_p^dag = e^{-2 E_d(p)} a_p^dag Gamma(t1^(2)_d),   for every p.
```

These two relations determine `T_hat^2_d` on all occupation vectors (CORNER
(ii)); with the strict positivity of item 4.2 they give the full assembly

```text
    T_hat^2_d = Gamma(t1^(2)_d) = tensor_p diag(1, e^{-2E_d(p)}) = B^dag B,
    H_hat_d   = -log(T_hat^2_d)/(2 a_tau) = dGamma(E_d) >= 0,
    Tr T_hat^2_d = det(1 + t1^(2)_d) = prod_p (1 + e^{-2E_d(p)}),
    dim: (L/2)^d * 2^d = L^d modes.
```

---

## 5. Exact-gate designs (sympy; no floats as inputs)

All gates are symbolic in `m` (sympy `Symbol('m', positive=True)`) with
`E_d = asinh(sqrt(m**2 + Sigma))`, `Sigma = sum_mu sin^2 p_mu` an exact
rational-trig value (e.g. `0`, `1`, `2`), and `t = exp(-2*E_d)` carried
either as `exp(-2*asinh(sqrt(m**2+Sigma)))` or as a fresh positive symbol
`t` where only exponent bookkeeping is tested. No floats enter as inputs;
comparisons are `sympy.simplify(lhs - rhs) == 0` (or `.equals(0)`).
Useful closed forms (all exact):
`exp(asinh(x)) = x + sqrt(1+x**2)`, hence
`exp(-2*E_d) = (sqrt(1+m**2+Sigma) - sqrt(m**2+Sigma))**2` and
`exp(+2*E_d) = (sqrt(1+m**2+Sigma) + sqrt(m**2+Sigma))**2`; at `Sigma=0`
this is `(sqrt(1+m**2) -/+ m)**2`.

### Gate A — classical rebuild (symbolic)

**A0 (Clifford / corner algebra).** Build `Gamma_mu` on the `2^d`-dim corner
space from `Gamma_mu|r> = (-1)^{r_mu}|r xor s_mu>`, `s_mu` = ones in slots
`< mu`. For `d=2`, ordering `r=(r1,r2)` as `00,01,10,11`:

```text
    Gamma_1 = diag(1, 1, -1, -1),
    Gamma_2 = [[0,0,1,0],[0,0,0,-1],[1,0,0,0],[0,-1,0,0]].
```

For `d=3` build the 8x8 analogues (`s_1=000, s_2=100, s_3=110`). Check
symbolically: `Gamma_mu^2 = I`, `Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0`
(`mu != nu`), `Gamma_mu = Gamma_mu^dag` (Hermiticity), and
`S(k)^2 = (sum_mu sin^2 k_mu) I` with `sin(k_mu)` exact
(`sin(pi/2)=1`, `sin(0)=0`, `sin(pi)=0`).

**A1 (d=2, L=2 and d=3, L=2; degenerate spot).** At `L=2` all full momenta
have `p_mu in {0, pi}`, so `sin p_mu = 0`, `Sigma = 0`, `S(k)=0`. Build the
position-space `T_even, T_odd` on the `4` (d=2) or `8` (d=3) sites directly
from the staggered phases `eta_mu`, form `T_2 = T_odd T_even` (dimension
`2^{d+1} = 8` or `16`), and check its eigenvalues are
`{ (m+sqrt(1+m**2))^{+2} (mult 2^d), (m+sqrt(1+m**2))^{-2} (mult 2^d) }`
via `charpoly` factored symbolically. This is the classical anchor feeding
the Fock gates D/E (same `E = asinh(m)`).

**A2 (d=2, L=4 one-particle spot; the corner-coupling exercise).** Choose
reduced momentum `k = (pi/2, pi/2)`, so `sin k_1 = sin k_2 = 1`,
`S(k) = Gamma_1 + Gamma_2`, `S(k)^2 = 2 I` (nonzero, off-diagonal coupling
via `Gamma_2`). Build the `8x8` classical block
`T_2(k) = T_odd(k) T_even(k)` with `T_even(k) = [[-2(m I + i S(k)), I],[I,0]]`
(`I` = 4x4). Check symbolically:
- `S(k)^2 = 2 I` (so `lambda^2 = 2`, `Sigma = 2`);
- `spec T_2(k) = { exp(+2*asinh(sqrt(m**2+2))) (mult 4),
  exp(-2*asinh(sqrt(m**2+2))) (mult 4) }`;
- taste check: repeat at `k=(pi/2,0)` (`Sigma=1`, `S=Gamma_1` diagonal) and
  confirm the four corners `p=(pi/2 or 3pi/2, 0 or pi)` share
  `E=asinh(sqrt(m**2+1))`.

This is the only gate that exercises `S(k) != 0` (corner coupling); `L=2`
cannot (there `S=0`).

### Gate B — projector identities per mode (symbolic)

On a single 2x2 block `T_2(sigma) = [[4|a|^2+1, -2 conj a],[-2a, 1]]`,
`a = m + I*sigma` (sympy `I`), `sigma` a symbol (or `sqrt(2)` for the A2
spot). Set `Lp = exp(2*asinh(sqrt(m**2+sigma**2)))`,
`Lm = exp(-2*asinh(sqrt(m**2+sigma**2)))`, and

```text
    P_m = (T2 - Lp*eye(2)) / (Lm - Lp),
    P_p = (T2 - Lm*eye(2)) / (Lp - Lm).
```

Check (simplify to zero): `P_m**2 - P_m`, `P_p**2 - P_p`, `P_m*P_p`,
`P_m + P_p - eye(2)`, `T2*P_m - Lm*P_m`, `T2*P_p - Lp*P_p`, and
`Lm*Lp - 1` (reciprocity). Also `Lm` real-positive and in `(0,1]`
(`simplify(Lm) > 0`, and `<1` for `m>0`).

### Gate C — one-mode coherent -> exterior bridge (symbolic Grassmann/2x2)

Represent the single Grassmann product `bar z' z` by a nilpotent symbol `w`
with the rule `w**2 -> 0` (implement by truncating: multiply polynomials in
`w` and drop `w**k, k>=2`). Then:
- kernel `exp(lambda*w)` truncates to `1 + lambda*w`;
- operator side `diag(1, lambda) = eye(2) + (lambda-1)*Matrix([[0,0],[0,1]])`;
- normal-ordered kernel `(1 + (lambda-1)*w)*(1 + w)` truncated `= 1 + lambda*w`
  — check equals `exp(lambda*w)` truncation;
- inverse match: from `T0 + T1*w == 1 + lambda*w` read `T0=1, T1=lambda`,
  assert `Matrix([[T0,0],[0,T1]]) == diag(1,lambda)`;
- **vacuum element**: `diag(1,lambda)[0,0] == 1` (the `C=1` pin);
- discrimination stub: assert that `C*diag(1,lambda)` with `C != 1` has
  kernel `C*(1+lambda*w)` whose constant term is `C != 1`, i.e. is NOT of
  the form `exp(bar z' lambda z)` — so the exponential kernel forces `C=1`.

Keep `lambda` a symbol (later specialized to `exp(-2*E_d)`).

### Gate D — full Fock at d = 2, L = 2 (16-dim, dense exact)

`4` sites -> `n = 4` modes -> `F` dimension `2^4 = 16`. All modes degenerate
at `E = asinh(m)`, `t = exp(-2*E) = (sqrt(1+m**2)-m)**2`; kernel
`t1^(2) = t * eye(4)`. Build occupation basis indexed by subsets
`S subset {0,1,2,3}` (bit order fixed for Jordan-Wigner). Then:
- **Gamma from occupation action**: `Gamma(t1^(2))` is the `16x16` diagonal
  matrix with entry on `|S>` equal to `prod_{j in S} t = t**|S|`.
- **intertwiner vs each `a_j^dag` (dense exact)**: build the `16x16`
  Jordan-Wigner creation matrices `a_j^dag` (`j=0..3`) with signs
  `(-1)^{#{i<j : i in S}}`. Check
  `Gamma * a_j^dag - t * a_j^dag * Gamma == 0` (zero `16x16`) for each `j`,
  and `Gamma * vac == vac`. (Positive check that the canonical `Gamma`
  intertwines; degeneracy means it does NOT yet exclude the `W`-conjugate —
  see Gate F.)
- **`-log/(2 a_tau) = dGamma(E)` exact**: `Gamma` diagonal, so its matrix log
  is `diag(log(t**|S|)) = diag(-2 E |S|)`; check
  `-log(Gamma)/(2 a_tau) == dGamma(E)` where
  `dGamma(E) = E * sum_j n_j = diag(E*|S|)` (a_tau=1). Compare per-diagonal
  entry `-log(t**|S|)/2 == E*|S|` symbolically (avoids matrix-log routines).
- **trace = det exact**: `Tr Gamma = sum_S t**|S| = sum_{q=0}^4 C(4,q) t**q =
  (1+t)**4`; `det(eye(4) + t*eye(4)) = (1+t)**4`. Assert
  `simplify((1+t)**4 - Tr) == 0` and equal to the determinant.
- **`B^dag B` exact**: `B = diag(t**(|S|/2))` built as
  `tensor_j diag(1, sqrt(t))` (`sqrt(t) = exp(-E)`); check
  `B.conjugate().T * B - Gamma == 0` (`16x16` zero). Build `B` from the
  tensor construction and `Gamma` from the occupation action so the equality
  is a nontrivial cross-check, not `B**2` by fiat.

### Gate E — d = 3, L = 2 (256-dim): STRUCTURED gates only

`8` sites -> `n = 8` modes -> `F` dimension `2^8 = 256`, all degenerate at
`E = asinh(m)`, `t = exp(-2E)`. **No dense 256x256 matrix is ever formed.**
Represent every number-diagonal operator as a length-256 vector indexed by
subsets `S subset {0..7}`; represent creation operators by their *action*.
Exactly how:

- **diagonal occupation products**: `Gamma(t1^(2))` is the map
  `S |-> t**|S|` (a dict/array of 256 scalars). Never instantiate the matrix.
- **intertwiner via action on basis VECTORS**: for each mode `j in {0..7}`
  and each subset `S`:
    - if `j in S`: `a_j^dag |S> = 0`, both sides `0` — pass;
    - if `j not in S`: `a_j^dag |S> = eps * |S ∪ {j}>`,
      `eps = (-1)^{#{i in S : i < j}}` (JW sign). Then
      `Gamma * a_j^dag |S> = eps * t**(|S|+1) * |S ∪ {j}>` and
      `t * a_j^dag * Gamma |S> = t * (t**|S|) * eps * |S ∪ {j}> =
       eps * t**(|S|+1) * |S ∪ {j}>`. Assert the single nonzero component
      matches: same target `S ∪ {j}`, same sign `eps`, same scalar
      `t**(|S|+1)`. This is `256 * 8` scalar/index checks, each `O(1)`; no
      matrix product.
- **`-log/(2 a_tau) = dGamma(E)`**: per subset scalar,
  `-log(t**|S|)/(2 a_tau) == E*|S| == sum_{j in S} E`. 256 scalar checks.
- **trace = det**: `Tr = sum_{q=0}^8 C(8,q) t**q = (1+t)**8` (closed-form
  scalar sum over `q`, or sum the 256 diagonal scalars); `det` over the
  `8`-dim one-particle space `= (1+t)**8`. Assert equal — both computed
  without the 256-dim object.
- **`B^dag B`**: per subset, `B: S |-> exp(-E)**|S| = t**(|S|/2)`; check
  `(t**(|S|/2))**2 == t**|S|` for all `S` (256 scalar checks). Structured,
  no dense product.

### Gate F — canonical-pin discrimination (NON-degenerate, small)

Degenerate gates D/E verify the canonical `Gamma` satisfies the intertwiner
but CANNOT exclude the `W`-conjugate `Gamma_tilde = W Gamma W^dag`: at full
degeneracy every fixed-particle-number sector is a single eigenvalue, so
`W` (number-preserving) commutes with `Gamma` and `Gamma_tilde = Gamma`. To
make the intertwiner *discriminating*, replicate CORNER's counterexample on
a NON-degenerate diagonal kernel. Symbolic `n = 3` modes, distinct positive
diagonal `t1 = diag(l1, l2, l3)` (e.g. exact integers `diag(2,3,5)` per
CORNER, or three distinct symbolic positives); `F` dimension `8`. Let `W` be
the number-preserving unitary swapping the two 2-particle occupation states
`{modes 1,2}` (eigenvalue `l1 l2`) and `{modes 1,3}`... (any nontrivial
2-particle swap; CORNER swaps the states with eigenvalues `6` and `10`).
Check:
- `Gamma` and `Gamma_tilde = W Gamma W^dag` have EQUAL trace
  `= det(1+t1) = prod (1+l_j)` and both preserve functoriality/positivity —
  so trace/positivity/multiplication do NOT distinguish them;
- only `Gamma` satisfies `Gamma a_j^dag = l_j a_j^dag Gamma` for all `j`;
  `Gamma_tilde` FAILS it (exhibit one `(j,S)` where it breaks);
- `-log Gamma_tilde != dGamma(-log t1)` on the swapped occupation states.

This gate is the operational meaning of item 3.4 / CORNER's pin: the C=1
normalization AND the functor are fixed by the canonical intertwiner, not by
trace+positivity+multiplication.

### Discrimination probes — what mutation each gate catches

| Gate | Object | A mutation it catches |
|---|---|---|
| A0 | Clifford `Gamma_mu`, `S(k)^2` | drop the staggered phase `xi_mu` / wrong `s_mu` -> `Gamma`'s stop anticommuting -> `S(k)^2 != (sum sin^2)I`; making all `Gamma_mu` diagonal (miss corner coupling) |
| A1 | d=2/3 L=2 classical spectrum | wrong dispersion: `sin->cos`, missing `m^2`, factor-2 in `E`, or `2^d`-multiplicity wrong (dropped a taste corner) |
| A2 | d=2 L=4 `S(k)!=0` block | replacing `sum_mu sin^2 p_mu` by `sin^2(sum p_mu)` or by a single-axis `sin^2 p_1`; off-diagonal coupling error in `Gamma_2` -> `S^2 != 2I`; taste non-degeneracy |
| B | per-mode projectors | swap `lambda_+ <-> lambda_-` in numerators -> `P_m^2 != P_m`; non-reciprocal spectrum `lambda_- lambda_+ != 1`; picking the growing channel |
| C | one-mode bridge | `diag(1,lambda) -> diag(lambda,1)` (swap) or `-> C diag(1,lambda)`, `C!=1` (vacuum element `!=1`); sign `diag(1,-lambda)` fails `exp(bar z' lambda z)` |
| D | full Fock 16-dim | wrong occupation eigenvalue `t**|S|`; JW sign error (intertwiner breaks); factor/`a_tau` error in `-log`; `trace!=det` |
| E | structured 256-dim | same as D at scale, plus: JW sign in the structured action, occupation-exponent `|S|+1` bookkeeping, without dense algebra |
| F | canonical pin | the `W`-conjugate functor (trace-/positivity-preserving) — caught ONLY here, needs non-degenerate `t1`; catches "trace=det implies canonical `Gamma`" fallacy |

---

## 6. LIMITS (assumptions, forks, under-determination, weakenings)

**L1 — `a_tau` is a convention, not derived.** DISP never introduces
`a_tau` (its monodromy has unit time step); RP carries `a_tau` symbolically;
CORNER uses `a_tau = 1` implicitly (`-1/2 log T^2 = dGamma(E)`). I set
`a_tau=1` per spec. At `a_tau=1` all three agree and `H_hat_d = dGamma(E_d)`.
A general `a_tau` only rescales the generator (`H_hat_d = dGamma(E_d)/a_tau`)
and does not change positivity or the spectrum-set of `T_hat^2_d`. CORNER
explicitly states this identity "does not select physical time" (CORNER line
139); no dynamics/time-normalization is claimed. This is a convention fork,
not a gap.

**L2 — the classical block IS a genuine time-recursion monodromy, but the
monodromy is not itself the quantum one-particle transfer operator; the
bridge is the honest weak point (shared with d = 1).** DISP's mode equation
`psi_{t+1} = -2(mI + (-1)^t H_hop)psi_t + psi_{t-1}` is literally a classical
transfer recursion on amplitude 2-vectors, and `T_2(k)` is its two-step
monodromy — so the "monodromy" framing is correct, NOT weaker than d=1.
However, the passage monodromy `->` one-particle quantum transfer kernel is a
three-part finite-dimensional bridge, each part supplied and each identical
in structure to d=1: (a) forward-channel selection by finite-norm (item 2,
RP Step 3b, d-blind); (b) coherent-state `->` exterior correspondence (item
3, RP line 169); (c) the second-quantization functor (item 4, CORNER). The
d-dim identity is NOT weaker than the landed d=1 one: the ONLY d-dependent
input is the corner Clifford algebra `S(k)^2 = (sum sin^2 k_mu)I` (DISP,
"the only dimension-dependent algebraic step"), and everything downstream is
d-blind. The honest statement: this is a derivation *relative to* DISP's
classical result + RP's selection/bridge + CORNER's functor, all on the free
`U=1` surface — not a from-scratch construction of the many-body operator.

**L3 — coherent-state sign convention (`diag(1, lambda)` vs
`diag(1, -lambda)`).** The bare Grassmann-coherent-state eigen-relation
`a|z> = z|z>` and the placement of the minus in `|z> = |0> -/+ z|1>` fix a
sign that, taken naively, could give `diag(1, -lambda)`. My item-3.2
derivation routes through the number operators `n` and `1-n`, whose kernels
(`bar z' z` and `1`) are sign-unambiguous, yielding `diag(1, lambda)` in
agreement with RP/CORNER. Flag: a different textbook convention flips the
intermediate sign; it is physically inert because the surviving eigenvalue is
`lambda = lambda_- = e^{-2E_d} > 0` regardless. Gate C should assert the
positive-`lambda` branch.

**L4 — free `U = 1` only; NO gauge, NO U-integration, NO interacting.**
CORNER is explicit (CORNER lines 34-41, 142-156): the current source tree
does NOT supply `T_MB^2[U] = Gamma(t[U])` at a fixed gauge background;
fixed-background factorization "remains open." The d-dim identity here
inherits exactly that scope: it is the free specialization. No claim about
gauged, `U`-integrated, or interacting transfer, no Lieb-Robinson envelope,
no physical-velocity, no retained-grade status.

**L5 — even `L` per direction is required (spec + fold-exactness).** The
two-site-cell fold (DISP lines 108-120) needs even spatial periods for the
`{0,1}^d` corner labelling and `(L/2)^d` reduced-momentum count to be exact.
Odd `L` breaks the fold; the mode count `(L/2)^d * 2^d = L^d` and the taste
structure assume even `L`. Gates use `L in {2,4}` (even).

**L6 — `m > 0` is essential for the bounded logarithm and the strict
channel split.** `E_d(p) = asinh(sqrt(m^2 + sum sin^2 p_mu)) >= asinh(m) > 0`,
so `e^{-2E_d} in (0,1)` strictly, `1 + t1^(2)_d` is invertible, and CORNER
(iii) [needs strict positivity] applies. At `m = 0` the `p` with
`sum sin^2 p_mu = 0` (e.g. `p=0`) give `E_d = 0`, `e^{-2E_d} = 1`
(still positive, `log = 0`), but the strict projector split
`lambda_- < 1 < lambda_+` degenerates (`lambda_- = lambda_+ = 1`) and the
item-2 finite-norm selection loses its gap. Keep `m > 0` (matches all three
sources).

**L7 — `S(k)^2` is SCALAR x I, stronger than the spec's "diagonal."** Item
1.1: the note's algebra gives `S(k)^2 = (sum sin^2 p_mu) I`, all `2^d`
diagonal entries equal, not a generic diagonal with distinct entries. This is
what makes ALL `2^d` corners share one `E_d` (taste degeneracy) and collapses
the `2^{d+1}`-block to a single 2x2 recursion. I did not force the spec's
wording; I recorded the stronger true statement.

**L8 — taste multiplicity is inherited staggered doubling, not a defect, but
it is a structural feature to name.** Each reduced momentum carries `2^d`
degenerate modes (the taste corners). The identity is about the full `L^d`
modes; the `2^d`-fold degeneracy per reduced momentum is the standard
staggered-fermion taste doubling, exact here. Downstream physical
interpretation (species assignment) is out of scope (CORNER line 156).

**L9 — DISP's locality content (`C_d`, `h(z)`, contour bound) is NOT used.**
The transfer identity `T_hat^2_d = Gamma(t1^(2)_d)` is purely spectral /
algebraic. DISP's position-space kernel `h(z)`, even-offset rule, and
all-direction rate `arcsinh(m)/(2d)` (DISP lines 54-216) concern the
reconstructed-`H` quasilocality and are NOT inputs to the assembly. I used
only DISP's dispersion/Clifford content. Flag so the supervisor does not
expect a locality claim from this report.

**L10 — the `2^{d+1}` per-`k` block dimension and the eigenvalue
multiplicities are my assembly.** DISP reduces directly to 2x2 per eigenline
and does not display the full `2^{d+1}` block or the `2^d`-fold
multiplicities. Items 1.2/1.5/1.6 state these as the honest assembly of
DISP's per-eigenline result with the `2^d`-dim corner space; they are
verified by Gate A1/A2, not quoted from DISP verbatim.

**L11 — `dim H_1 = L^d` one-particle modes assumes one Grassmann component
per site.** Spec-given ("one Grassmann component per site"). The phase-space
doubling (`2 * 2^d` per `k`, total `2 L^d` classical) is the `(psi_t,
psi_{t-1})` structure; forward selection halves it to `L^d`. Consistent, but
recorded as an assumption.

---

## Summary

All six spec items are derived with full displayed algebra on the free
`U = 1` surface, in DISP's own conventions (quoted), bridged by RP's Step-3b
selection and CORNER's finite-mode functor. Item 1: per-`k` classical block
`T_2(k)` = explicit function of the Hermitian corner matrix `S(k) =
sum_mu sin(k_mu) Gamma_mu`, `S(k)^2 = (sum sin^2 p_mu)I` (scalar), reducing
to the d=1 2x2 recursion with `sin^2 p -> sum_mu sin^2 p_mu`, eigenvalues
`e^{+-2E_d}`, taste-degenerate; dimension `2^{d+1}`; corners couple for
`d>=2` via off-diagonal `Gamma_{mu>=2}`. Item 2: per-mode projectors +
finite-norm selection give `t1^(2)_d = diag e^{-2E_d}`; selection is d-blind,
mode-furnishing (Clifford diagonalization) is where d enters. Item 3:
`exp(bar z' lambda z) -> diag(1,lambda)`, vacuum term `=1` derives `C=1` (the
intertwiner's vacuum-fixing), kernel factorizes over `S(k)` eigenmodes (no
cross terms: diagonal quadratic form). Item 4: `T_hat^2_d = Gamma(t1^(2)_d) =
tensor_p diag(1,e^{-2E_d}) = B^dag B`, `H_hat_d = -log(T_hat^2_d)/(2 a_tau) =
dGamma(E_d) >= 0`, `Tr = det(1+t1^(2)_d) = prod_p(1+e^{-2E_d})`, mode count
`(L/2)^d 2^d = L^d`, intertwiner displayed. Item 5: seven symbolic gate
designs (A classical rebuild incl. d=2 L=4 spot; B projectors; C one-mode
bridge; D full Fock d=2 L=2 dense; E structured d=3 L=2 256-dim; F
non-degenerate canonical-pin discrimination) with a mutation table. Item 6:
eleven LIMITS, the load-bearing ones being L2 (monodromy->operator bridge is
relative to the three sources, not weaker than d=1), L4 (free `U=1` only),
L7 (`S(k)^2` is scalar, stronger than "diagonal"), and the item-5 finding
that degenerate `L=2` Fock gates do NOT test the canonical pin (Gate F
needed).

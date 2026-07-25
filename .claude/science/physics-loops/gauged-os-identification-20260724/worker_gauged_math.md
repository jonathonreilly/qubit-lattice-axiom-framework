# Worker report — gauged lift of the polar / CAR-Fock chain

**Worker:** bounded math executor under the workhorse split.
**Date:** 2026-07-24.
**Status authority:** none. This report sets and predicts no audit verdict, proposes no
primitive, and edits no repo file. It is worker input to the supervisor.
**Repo state:** `git fetch origin main` run first; `origin/main = e6d1070adf`. All quoted
`file:line` are from the worktree files, which are byte-identical to `origin/main` for the
four conventions sources (`git diff --stat origin/main -- docs/` reports exactly one
changed path, see §0.0).

**Bottom line.** The polar chain (`R`, `E`, `Z`, `B`) lifts to a fixed gauge background
**with no obstruction and with strictly fewer inputs than the free d-dimensional case**:
it consumes only `h^dag = -h`, `m > 0` real scalar, and finite dimension. It does **not**
consume realness, the momentum fold, the Clifford step, `d`, `N`, or evenness of the
periods. The reflected two-slice Gram also lifts, PSD intact, but **only after a
correction that the free note itself flags and that is invisible at `U = 1`**: at a
background the pole frame must be built from `h[Ubar] = conj(h[U])`, the hop at the
**complex-conjugate background**, not from `h[U]`. Building it from `h[U]` fails against a
direct dense chain inverse at order `10^-1` (§3.6). The operator identification
`T^2[U] = Gamma(t[U])`, `t[U] = Z[U]`, then goes through — but at **exactly the landed
conditional status, plus two further supplied inputs specific to the gauged case**
(static links, temporal gauge), plus one **strengthening** of a supplied input (one-mode
exponential coherent kernel -> multi-mode Gaussian kernel) that I flag as an open honesty
gap rather than paper over (§4.4). Every claim below that I could falsify, I tried to
falsify; the falsification attempts and their outcomes are recorded inline.

---

## 0. Sources, conventions, and one provenance flag

### 0.0 Provenance flag (read this before using anything downstream)

`docs/FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md`
is **NOT on `origin/main`**. It exists only on the current branch
(`physics-loop/rp-ddim-action-level-transfer-20260720`); `git diff --stat origin/main --
docs/` shows it as the single `+382` addition. I read it for conventions and I cite it
below, but every load-bearing structural fact I use from it I re-derived natively, and I
mark each such use. The other four sources
(`FREE_STAGGERED_3PLUS1_...CAR_FOCK...2026-07-12`, `CORNER_TRANSFER_...2026-06-12`,
`RP_P2_GAUGE_EXTENSION_...2026-05-28`, `MICROCAUSALITY_CORNER_CLASS_...2026-07-18`,
plus `FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_...2026-06-12`,
`AXIOM_FIRST_RP_TWO_STEP_...2026-05-28`, `RP_COUPLED_TWO_SLICE_GAUGE_...2026-07-10`)
are on `origin/main`.

### 0.1 The free polar chain, verbatim

`docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:54-60`:

```text
H^dag=-H,             M>0,
R=(M^2-H^2)^(1/2)>0,
E=asinh R,
Z=e^(-2E),            0<Z<I,
B=(M+H)R^(-1).
```

and `:62-67`:

> "All functions are finite-dimensional spectral functions. Since `H` commutes
> with `R`,
> ```text
> B^dag B=(M-H)(M+H)R^(-2)=I,
> ```
> so `B` is unitary."

The realness caveat is stated there too, `:79-85`:

> "The mode-level identities below need only finite
> dimension and `H^dag=-H`. The operator-level reflected-Gram identities
> additionally use that the hop is **real in the site basis** (`H*=H`, so
> complex conjugation maps `H=i lambda` eigenvectors to `H=-i lambda`
> eigenvectors); for a complex anti-Hermitian hop the same formulas hold with
> `H` replaced by `conj(H)` in the frames."

and again at `:441`:

> "real staggered hop (`H*=H`) | load-bearing carrier condition | required for the
> conjugate-eigenline operator binding; the canonical staggered hop is real, and a
> complex anti-Hermitian hop gets the `conj(H)` frames instead"

**This is the single sentence the whole gauged Gram section turns on.** A gauged hop is
not real. §3 executes that escape clause and identifies `conj(h[U])` concretely as
`h[Ubar]`.

### 0.2 The free reflected Gram and frames, verbatim

`:94-116` (mode level), `:150-160` and `:172-182` (operator level):

```text
D_lambda(zeta)
 = [[M+i lambda,          (1-zeta^(-1))/2],
    [(zeta-1)/2,          M-i lambda       ]],
Delta_lambda(zeta)
 = r^2+(2-zeta-zeta^(-1))/4
 = -(zeta-z)(zeta-z^(-1))/(4 zeta).
K_lambda
 = (2z/(1+z))
   [[1,             sqrt(z) b],
    [sqrt(z) b*,    z        ]]
 = 2z v_lambda v_lambda^dag,
v_lambda=(1+z)^(-1/2) [1, sqrt(z)b*]^T.
U_pole = [ I ; Z^(1/2) B ] (I+Z)^(-1/2),   U_pole^dag U_pole=I.
P_OS=U_pole U_pole^dag,      K_n=2 U_pole Z^n U_pole^dag.
A=sqrt(2) Z^(1/2) U_pole^dag,   K_1=A^dag A,   K_n=A^dag Z^(n-1) A.
```

and the index rule, `:141-148` (load-bearing; §3.4 shows the spatial-index swap in it is
not cosmetic):

> "Reading the reflected Gram as an operator kernel (row index = reflected
> first argument) places each mode Gram `K_lambda` on the **conjugate**
> carrier eigenline: ... and
> `K((a,x),(b,y)) = G((t_b,y),(theta(t_a),x))` dresses `K_lambda` with the
> conjugated mode."

Arena boundary, `:332-336`: "The theorem uses the vacuum/infinite temporal lattice ... On
an open temporal chain of length `2N`, the central seam Gram converges exponentially to
`K_lambda`; it is not exactly equal at finite `N` because of boundary images."

### 0.3 The gauged hop, verbatim

`docs/RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md:132-141`:

```text
h[U]_{x,y} = (1/2)(U_x delta_{y,x+1}
                         - U_{x-1}^dag delta_{y,x-1}).
```

> "For every such list, the forward block and backward block are
> minus-conjugate-transposes, so `h[U]^dag = -h[U]`."

That is `d = 1` and carries **no staggered phase** (correct, because the `d = 1` spatial
phase is identically `1`; see §1.1). Its input list, `:143-152`, is load-bearing for §3
and §4:

> "- the unitary-link carrier and its interpretation as a gauge background;
> - time independence of the same spatial matrix over the two slices;
> - the alternating matrices `A_even` and `A_odd`;
> - the recurrence coefficient `1/2` and companion-matrix convention; and
> - any identification of the recurrence roots with a Grassmann, Hilbert-space,
>   or Fock-space transfer operator."

and its firewall, `:224-226`: "- positivity of a Grassmann transfer kernel or its inner
product; - a second-quantized or many-body operator `Gamma(t1)`;".

### 0.4 The free d-dimensional phase convention, verbatim

`docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md:81-97`:

```text
    eta_0(t,x) = 1,
    eta_mu(t,x) = (-1)^(t + x_1 + ... + x_{mu-1}),      mu = 1,...,d.
    xi_mu(x) = (-1)^(x_1 + ... + x_{mu-1}),
    H_hop = (1/2) sum_mu xi_mu(x) (tau_{+mu} - tau_{-mu}).
```

> "The spatial term on time slice `t` is `(-1)^t H_hop`".

### 0.5 The finite-mode functor and the open prerequisite, verbatim

`docs/MICROCAUSALITY_CORNER_CLASS_FACTORIZATION_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-07-18.md:58-71`:

> "1. **Functoriality.** For arbitrary linear maps `A` and `B`,
>    `Gamma(A) Gamma(B) = Gamma(AB)`. No commutativity hypothesis is needed...
> 2. **Canonical intertwiner.** ... `Gamma(A) a^dag(f) = a^dag(Af) Gamma(A)`, and
>    `Gamma(A)` fixes the vacuum. These relations determine `Gamma(A)` on decomposable
>    occupation vectors.
> 3. **Positive logarithm.** If `t` is strictly positive, then
>    `Gamma(t) = exp(dGamma(log t))` and `-log Gamma(t) = dGamma(-log t)`.
> 4. **Trace identity.** `Tr_F Gamma(A) = det_H(1 + A)`. ...
> 5. **Direct sums.** ... `Gamma(direct_sum_k A_k) = tensor_k Gamma(A_k)`."

and the open prerequisite this report targets, `:34-41`:

> "The current source tree does not
> supply `T_MB^2[U] = Gamma(t[U])` at a general fixed gauge background. The
> conditional finite-matrix recurrence in
> `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`
> explicitly excludes a Fock-space second quantization, while
> `CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md`
> constructs classical fixed-background matrices and separately records a trace
> identity. Neither statement is an operator identification. Fixed-background
> factorization therefore remains open."

and the pin, `:104-107`:

> "Thus the exterior action or, equivalently, the canonical creation
> intertwiner is the pin. The trace/determinant correspondence by itself is not
> a Gaussian-factorization theorem."

and the fiber warning, `:152-154`:

> "**Matrix fibers:** if a future one-dimensional open-chain bridge supplies a
> block-operator-norm envelope with fixed fiber dimension `n_f`, the coarse
> activity expression carries the factor `n_f`; scalar-fiber constants do not
> transfer to a non-Abelian block kernel."

### 0.6 The background-conjugation law already in the repo, verbatim

`docs/CORNER_TRANSFER_EXTENDS_TO_FIXED_GAUGE_BACKGROUNDS_BOUNDED_NOTE_2026-06-12.md:99-105`:

> "**(N4) K and the complement at fixed background -- honest scope.** `K`/CPT
> conjugation acts on the background as `U -> conj(U)`."

§3.5 shows the gauged Gram frames land on exactly this map, from a completely
independent route (OS reflection + operator kernel reading). I flag this as a
**consistency cross-check between two landed surfaces**, not as a citation used to prove
anything.

### 0.7 Verification method used in this report

Two independent tools, both run by me in scratch (no repo file touched, no runner
committed):

* **sympy exact** — anti-Hermiticity, the phase-mutation, `conj(h[U]) = h[Ubar]`,
  `Pi h Pi = -h`, the residue/Gram mode algebra, and a fully rational closed-form gauged
  instance (§6.1 instance C, where `E = log 2` exactly).
* **numpy dense** — the position-space certificate: a full space-time chain operator at a
  static SU(2) / U(1) background, densely inverted, its reflected two-slice Gram extracted
  and compared to the closed form, **including the decisive `h[U]`-frame mutation**.

Floats appear only in my dense-inverse certificate. The **gate designs in §6 are exact and
float-free by construction** and are a different object; do not conflate them.

---

## 1. Anti-Hermiticity at a background

### 1.1 The convention, corrected against the repo

The task statement proposes

```text
h[U] "=" (1/2) sum_mu eta_mu(x) [ U_mu(x) tau_{+mu} - U_mu(x-mu)^dag tau_{-mu} ].
```

**This needs one correction and one clarification.**

*Correction.* `eta_mu` in this repo is a **space-time** phase, `eta_mu(t,x) =
(-1)^(t+x_1+...+x_{mu-1})` (`...DISPERSION_D_DIMENSIONAL...:83`). It is **not** the phase
that appears in `h`. The repo factors it as `eta_mu(t,x) = (-1)^t xi_mu(x)` and puts the
purely spatial `xi_mu(x) = (-1)^(x_1+...+x_{mu-1})` inside `H_hop`, leaving the `(-1)^t`
outside as the slice alternation: `...:90-93` defines `H_hop` with `xi_mu(x)` and `...:94`
says "The spatial term on time slice `t` is `(-1)^t H_hop`". Using `eta_mu(t,x)` inside
`h` would double-count the time alternation. **The correct object is `xi_mu`, not
`eta_mu`.**

*Clarification.* `xi_1(x) = (-1)^(empty sum) = 1`, so at `d = 1` the phase is absent —
which is exactly why `RP_P2...:132-135` displays a phase-free `h[U]`. The two landed
conventions are consistent; the `d = 1` one simply cannot see the phase.

**Corrected gauged d-dimensional staggered spatial hop (the object of this report).**
Spatial torus `Lambda = prod_mu Z_{L_mu}`, one Grassmann component per site, colour fiber
`C^N`, one-particle space `h = C^Lambda tensor C^N` of dimension `|Lambda| N`. Static
spatial links `U_mu(x) in SU(N)` (or `U(1)`, or any invertible matrices — see §1.4),
temporal gauge `U_0 = 1`. Then

```text
   (h[U] psi)(x) = (1/2) sum_{mu=1}^{d} xi_mu(x) [ U_mu(x) psi(x + e_mu)
                                                 - U_mu(x - e_mu)^dag psi(x - e_mu) ],

   xi_mu(x) = (-1)^{x_1 + ... + x_{mu-1}},        xi_1 = 1.                        (1.1)
```

Equivalently, in matrix elements on `h`,

```text
   h[U]_{x,y} = (1/2) sum_mu xi_mu(x) [ U_mu(x) delta_{y, x+e_mu}
                                      - U_mu(x-e_mu)^dag delta_{y, x-e_mu} ].      (1.2)
```

At `U = 1` this is `H_hop` of `...DISPERSION...:90-93` verbatim; at `d = 1, N` arbitrary it
is `h[U]` of `RP_P2...:132-135` verbatim. So (1.1) is the unique common lift, not a new
convention.

### 1.2 Theorem 1 (anti-Hermiticity) with complete algebra

I prove a **sharper** statement than needed, because the sharp version is what identifies
the consumed property.

**Theorem 1.** Let `c_mu(x) in C` be arbitrary and let `M_mu(x)` be arbitrary
(not necessarily unitary, not necessarily invertible) `N x N` matrices. Define

```text
   h_{x,y} = (1/2) sum_mu c_mu(x) [ M_mu(x) delta_{y,x+e_mu}
                                  - M_mu(x-e_mu)^dag delta_{y,x-e_mu} ].           (1.3)
```

Then `h^dag = -h` **if and only if**

```text
   conj( c_mu(x + e_mu) ) = c_mu(x)   for every mu and every x with M_mu(x) != 0.  (1.4)
```

*Proof.* Take adjoints entrywise: `(h^dag)_{x,y} = (h_{y,x})^dag`. From (1.3),

```text
   h_{y,x} = (1/2) sum_mu c_mu(y) [ M_mu(y) delta_{x,y+e_mu}
                                  - M_mu(y-e_mu)^dag delta_{x,y-e_mu} ],
```

so

```text
   (h^dag)_{x,y}
     = (1/2) sum_mu conj(c_mu(y)) [ M_mu(y)^dag delta_{x,y+e_mu}
                                  - M_mu(y-e_mu) delta_{x,y-e_mu} ].               (1.5)
```

Now resolve the two Kronecker deltas in terms of `y`:

* `delta_{x, y+e_mu}` forces `y = x - e_mu`, and then `M_mu(y)^dag = M_mu(x-e_mu)^dag`.
  This term contributes `+ (1/2) conj(c_mu(x-e_mu)) M_mu(x-e_mu)^dag delta_{y, x-e_mu}`.
* `delta_{x, y-e_mu}` forces `y = x + e_mu`, and then `M_mu(y-e_mu) = M_mu(x)`.
  This term contributes `- (1/2) conj(c_mu(x+e_mu)) M_mu(x) delta_{y, x+e_mu}`.

Hence

```text
   (h^dag)_{x,y}
     = (1/2) sum_mu [ conj(c_mu(x-e_mu)) M_mu(x-e_mu)^dag delta_{y,x-e_mu}
                    - conj(c_mu(x+e_mu)) M_mu(x)        delta_{y,x+e_mu} ].        (1.6)
```

And directly from (1.3),

```text
   -h_{x,y}
     = (1/2) sum_mu [ - c_mu(x) M_mu(x) delta_{y,x+e_mu}
                      + c_mu(x) M_mu(x-e_mu)^dag delta_{y,x-e_mu} ].               (1.7)
```

Compare (1.6) with (1.7) term by term. The `delta_{y,x+e_mu}` coefficients agree iff
`conj(c_mu(x+e_mu)) M_mu(x) = c_mu(x) M_mu(x)`; the `delta_{y,x-e_mu}` coefficients agree
iff `conj(c_mu(x-e_mu)) M_mu(x-e_mu)^dag = c_mu(x) M_mu(x-e_mu)^dag`, which is the same
condition shifted by `x -> x - e_mu`. Wherever `M_mu(x) != 0` these are exactly (1.4).
Conversely (1.4) makes (1.6) equal (1.7) identically. QED.

**Corollary 1 (the staggered case).** `c_mu = xi_mu` is real-valued with values `+-1`, so
(1.4) reduces to

```text
   xi_mu(x + e_mu) = xi_mu(x)   for every mu, x,                                   (1.8)
```

i.e. **`xi_mu` must not depend on `x_mu`**. The canonical staggered phase
`xi_mu(x) = (-1)^{x_1+...+x_{mu-1}}` omits `x_mu` from its exponent by construction, so
(1.8) holds identically, and `h[U]^dag = -h[U]` **exactly**, for every `d`, every `N`,
every link assignment, every set of periods.

### 1.3 What the proof consumes — the precise list

Consumed, and nothing else:

1. **`xi_mu` is independent of its own coordinate `x_mu`** (Corollary 1). This is the whole
   staggered-phase content of the proof. Not consumed: that `xi_mu` is `+-1`-valued
   beyond (1.4); not consumed: the specific product form `(-1)^{x_1+...+x_{mu-1}}`; not
   consumed: any relation between different `mu`; not consumed: the anticommutation
   `{Gamma_mu, Gamma_nu} = 0` that the free `d`-dim fold needs
   (`...DISPERSION...:124-127`). **The Clifford step is not used at all here.**
2. **The backward hop coefficient is the adjoint of the forward hop coefficient on the
   same link** (`U_mu(x-e_mu)^dag` opposite `U_mu(x-e_mu)`), with the relative minus sign.
3. Finite dimension (so that adjoint = conjugate transpose entrywise).

**Explicitly NOT consumed:** unitarity of `U_mu(x)`; `det U_mu(x) = 1`; the gauge group;
`N`; `d`; evenness of `L_mu`; staticity in time; `m`; the mass term at all. Theorem 1 is
strictly weaker in hypotheses than `RP_P2...:132-141`, which states the conclusion for
unitary links. Unitarity is needed downstream only for norm bounds (`||h[U]|| <= d`) and
for the `SU(N)` closure used in §3.5 — not for anti-Hermiticity.

### 1.4 What breaks if the phase depends on `x_mu` — sharp answer

Suppose the phase is `c_mu(x) = (-1)^{x_mu} xi_mu(x)` (any phase whose only extra
dependence is on its own coordinate, with even period so it is well defined on the torus).
Then `c_mu(x+e_mu) = -c_mu(x)`, so (1.4) fails maximally: instead of `(h^dag)_{x,y} =
-h_{x,y}` we get, repeating the (1.6)/(1.7) comparison with the sign flipped,

```text
   (h^dag)_{x,y} = + h_{x,y},     i.e.   h^dag = +h  (Hermitian, not anti-Hermitian).
```

**Verified exactly** (sympy, `d = 2`, `L = (4,2)`, `N = 2`, rational `SU(2)` links):
anti-Hermitian `False`, Hermitian `True`.

Downstream consequences, each of which is a separate breakage — this is why the mutation
is a good gate:

* `h^dag h = h^2`, so `R^2 = m^2 I + h^2`, which is **not** `m^2 I - h^2`. The identity
  `(mI+h)^dag(mI+h) = m^2 I - h^2` becomes `(mI+h)^2 = m^2 I + 2mh + h^2`, whose cross
  term `2mh` does **not** cancel. `B = (m+h)R^{-1}` is then **not** unitary.
* `T_odd = T_even^dag` fails: with `A_even = mI + h`, `A_odd = mI - h`, one has
  `A_even^dag = mI + h = A_even != A_odd`. So the two-step matrix `T_odd T_even` is no
  longer of the form `T^dag T` and the positivity argument of
  `RP_P2...:86-93` collapses at its first line.
* The spectrum of `h` becomes real instead of imaginary, so `spec(m^2 I + h^2)` can dip
  below `m^2` and, for `|h| > m`, go negative: `R` is then not even defined as a positive
  square root, and `E = asinh R` is not real.

For a *generic* `x_mu`-dependent phase (neither constant nor alternating along `mu`) one
gets neither `h^dag = -h` nor `h^dag = h`; `h` splits into a nonzero Hermitian plus a
nonzero anti-Hermitian part and the entire chain is undefined.

### 1.5 Two boundary cases I checked rather than assumed

* **`L_mu = 2` axis.** Then `x + e_mu = x - e_mu` on the torus and the two hop terms land
  on the *same* matrix entry; forward and backward partially cancel. The proof of
  Theorem 1 is a statement about matrix elements after summation, so it is unaffected —
  and I confirmed it exactly at `d = 2, L = (4,2), N = 2` with `SU(2)` links
  (anti-Hermitian, exactly). Note the contrast with the free case, where at `L_mu = 2` the
  hop **vanishes identically** (the two terms cancel exactly at `U = 1`); at a background
  it does not, because `U_mu(x) != U_mu(x-e_mu)^dag` in general. So `L = 2` is a
  *degenerate* instance in the free theory and a *live* one in the gauged theory.
* **Parity involution.** With `Pi psi(x) = (-1)^{x_1+...+x_d} psi(x)` (the free note's
  `:229`), each nearest-neighbour hop flips sign, so
  `Pi h[U] Pi = -h[U]` for **every** background. Verified exactly at `d = 2, L = (4,2),
  N = 2`, `SU(2)`. Consequence used in §5.3: `spec(h[U])` is symmetric under
  `i lambda -> -i lambda`, hence **every eigenvalue of `Z[U]` has even multiplicity.**

---

## 2. The polar chain over C

Throughout §2, `h` is **any** finite-dimensional anti-Hermitian operator, `h^dag = -h`, on
a complex Hilbert space `h` of dimension `n`; `m > 0` is a real **scalar**. Nothing in §2
knows about lattices, gauge fields, `d`, or `N`. In particular every statement applies
verbatim to `h = h[U]` of (1.1) at any background, by Theorem 1.

### 2.1 `R` is positive definite

```text
   h^dag h = (-h) h = -h^2,     so     m^2 I + h^dag h = m^2 I - h^2.               (2.1)
```

`h^dag h >= 0` always, so `m^2 I + h^dag h >= m^2 I > 0`: the operator is Hermitian
(`(h^dag h)^dag = h^dag h`) and positive definite with every eigenvalue `>= m^2`. A
positive-definite Hermitian operator has a unique positive-definite square root, so

```text
   R := (m^2 I + h^dag h)^{1/2} = (m^2 I - h^2)^{1/2},      R = R^dag,   R >= m I > 0. (2.2)
```

Concretely: `h` anti-Hermitian is normal, so `h = i A` with `A = A^dag` Hermitian (indeed
`A = -i h`, `A^dag = i h^dag = -i h = A`). Then `-h^2 = A^2 >= 0` and
`R = (m^2 I + A^2)^{1/2}`, with `spec(R) = { sqrt(m^2 + a_j^2) : a_j in spec(A) }`, all
`>= m`. Write `r_j := sqrt(m^2 + a_j^2)`.

### 2.2 `E` and `Z`

```text
   E := asinh(R),      spec(E) = { asinh(r_j) },   asinh(r_j) >= asinh(m) > 0,      (2.3)
   Z := e^{-2E},       spec(Z) = { e^{-2 asinh(r_j)} }.                             (2.4)
```

`asinh` is real, strictly increasing, and `asinh(0) = 0`, so `r_j >= m > 0` gives
`asinh(r_j) >= asinh(m) > 0` and therefore

```text
   0 < e^{-2 asinh(r_j)} <= e^{-2 asinh(m)} < 1,    i.e.   0 < Z <= e^{-2 asinh(m)} I < I. (2.5)
```

`E` and `Z` are Hermitian (real spectral functions of the Hermitian `R`), `E > 0`,
`0 < Z < I`. Note `sinh E = R` by construction, which is the identity used repeatedly
below.

*Float-free surrogate (used in §6).* `z = e^{-2E}` and `z^{-1} = e^{+2E}` are the two roots
of `zeta^2 - (2 + 4R^2) zeta + 1 = 0`, because
`z + z^{-1} = 2 cosh 2E = 2(1 + 2 sinh^2 E) = 2 + 4R^2` and `z * z^{-1} = 1`. Solving,
`z = 1 + 2R^2 - 2 sqrt(R^2(1+R^2))`. Then

```text
   z > 0  <=>  (1+2R^2)^2 > 4R^2(1+R^2)  <=>  1 + 4R^2 + 4R^4 > 4R^2 + 4R^4  <=>  1 > 0,
   z < 1  <=>  2R^2 < 2 sqrt(R^2(1+R^2)) <=>  R^4 < R^2(1+R^2)               <=>  R^2 > 0.
```

Both are **exact rational inequalities in `R^2 = m^2 I - h^2`**; no transcendental
function and no float is needed to certify `spec Z subset (0,1)`. The second one is where
`m > 0` enters (it fails at `R^2 = 0`, i.e. at `m = 0` with `h` singular).

### 2.3 `B` is unitary — with the cross term shown explicitly

Because `m` is a **real scalar**, `(m I)^dag = m I` and

```text
   (m I + h)^dag = m I + h^dag = m I - h.                                           (2.6)
```

Therefore, expanding fully with no step suppressed,

```text
   (m I + h)^dag (m I + h)
      = (m I - h)(m I + h)
      = m^2 I + m h - h m - h^2
      = m^2 I + m h - m h - h^2        [ h m = m h since m is a scalar ]
      = m^2 I - h^2
      = R^2.                                                                        (2.7)
```

The cross terms cancel **only** because `m` is a scalar; this is the single place where
"real scalar mass" is load-bearing (see §7, L5). Now

```text
   B := (m I + h) R^{-1},                                                            (2.8)
   B^dag B = R^{-1} (m I + h)^dag (m I + h) R^{-1} = R^{-1} R^2 R^{-1} = I.          (2.9)
```

For `B B^dag = I` one needs `[h, R] = 0` (proved in §2.4):

```text
   B B^dag = (m I + h) R^{-1} R^{-1} (m I - h)
           = (m I + h) R^{-2} (m I - h)
           = (m I + h)(m I - h) R^{-2}      [ R^{-2} commutes with h ]
           = (m^2 I - h^2) R^{-2}
           = R^2 R^{-2} = I.                                                        (2.10)
```

In finite dimension `B^dag B = I` already forces `B B^dag = I`, so (2.10) is a
consistency check rather than an extra hypothesis. **`B` is unitary.**

### 2.4 Did ANY step need `h` real? — No. Proof and the exact scope of the answer

**No step in §2.1–§2.3 uses `h* = h`.** Trace it: (2.1) uses `h^dag = -h`; (2.2) uses
Hermitian positivity and uniqueness of the positive square root; (2.3)–(2.5) use real
spectral calculus of the Hermitian `R`; (2.6) uses `m` real scalar; (2.7) uses `h^dag =
-h` and scalar `m`; (2.9)–(2.10) use (2.7) and §2.5. Complex conjugation never appears.

I state the converse precisely, because it is where the gauged lift really costs
something. Realness is used in the landed free note in exactly one place — the
**operator reading of the reflected Gram** (`...CAR_FOCK...:141-148`, `:441`), i.e. §3
below, not §2. So:

> **The polar chain is background-blind. The reflected Gram is not.**

### 2.5 Commutation — they all commute, with `h` and with each other

**Proposition.** `R`, `E`, `Z`, `B` all lie in the commutative unital algebra `C[h]`
generated by `h`. Consequently they commute with `h` and with one another.

*Proof.* `h^2` is a polynomial in `h`. `R^2 = m^2 I - h^2 in C[h]`. Since `R^2` is
Hermitian with finite spectrum `{r_j^2}` and `R` is the unique positive square root, `R`
is the value at `R^2` of the Lagrange interpolation polynomial `q` with `q(r_j^2) = r_j`
on the distinct points of `spec(R^2)`; hence `R = q(R^2) in C[h]`. Identically,
`E = asinh(R)` is `p_E(R)` for the interpolation polynomial `p_E` matching `asinh` on the
finite set `spec(R)`, so `E in C[h]`; and `Z = p_Z(E) in C[h]` for the interpolation
polynomial matching `t -> e^{-2t}` on `spec(E)`. Finally `R` is invertible
(`R >= m I > 0`), and `R^{-1}` is again a polynomial in `R` (Cayley-Hamilton), so
`B = (m I + h) R^{-1} in C[h]`. A polynomial algebra in a single element is commutative.
QED.

**So there is no counterexample: the answer is that they DO commute, unconditionally, at
every background.** Numerically confirmed on a `d = 1, L_s = 4, N = 2` `SU(2)` background:
`||[h,R]|| = 4.0e-16`, `||[B,Z]|| = 6.2e-17`, `||B^dag B - I|| = 8.9e-16`.

**Why this matters for the later Fock assembly, and what would break it.** Three things
ride on it: (i) `B B^dag = I` (2.10); (ii) the whole `T_2 W_stable = W_stable Z`
computation of §2.7, which moves `R`, `Z^{1/2}`, `B` past each other freely; (iii) the
statement that `Z` and `E` are simultaneously diagonalizable with `h`, so that a single
mode basis serves the classical block, the Riesz projectors, and the Fock assembly.

The commutation is **fragile in exactly one direction**: it requires `m` to be a scalar. If
`m` were promoted to a mass matrix `M` (flavour/taste-dependent mass, Wilson term,
background-dependent mass), then (2.7) becomes `(M^dag + h^dag)(M + h) = M^dag M + M^dag h
- h M - h^2`, whose cross terms cancel only if `[M, h] = 0` and `M^dag = M`. Then `R^2 =
M^2 - h^2` need not lie in `C[h]`, `B` need not commute with `R`, and (2.10) fails.
I flag this as a genuine boundary, not a hypothetical: it is exactly what a Wilson term or
a staggered taste-splitting mass would do.

### 2.6 The classical two-step block at a background

Following `RP_P2...:59-63` verbatim in structure, with `A_even = m I + h[U]`,
`A_odd = m I - h[U]`:

```text
   T_even = [[ -2(m I + h),  I ],
             [        I,     0 ]],       T_odd = [[ -2(m I - h),  I ],
                                                  [        I,     0 ]].            (2.11)
```

By (2.6), `A_odd = A_even^dag`, hence `T_odd = T_even^dag` and

```text
   T_2[U] := T_odd T_even = T_even^dag T_even >= 0.                                 (2.12)
```

Multiplying out the blocks (all four products written):

```text
   (T_even^dag T_even)_{11} = (-2(mI-h))(-2(mI+h)) + I*I = 4(m^2 I - h^2) + I = 4R^2 + I,
   (T_even^dag T_even)_{12} = (-2(mI-h))*I         + I*0 = -2(m I - h),
   (T_even^dag T_even)_{21} = I*(-2(mI+h))         + 0*I = -2(m I + h),
   (T_even^dag T_even)_{22} = I*I                  + 0*0 = I,
```

so

```text
   T_2[U] = [[ 4R^2 + I,   -2(m I - h) ],
             [ -2(m I + h),      I     ]].                                          (2.13)
```

Substituting `h = i S` recovers, symbol for symbol, the branch note's display
`T_2(k) = [[(4m^2+1)I + 4S(k)^2, -2(mI - iS(k))],[-2(mI + iS(k)), I]]`
(`...D_DIMENSIONAL_TWO_STEP_MANY_BODY...:92-93`), since
`4R^2 + I = 4(m^2 I - h^2) + I = (4m^2+1)I + 4S^2`. **Verified numerically** to `4.0e-15`
at a `d=1, L_s=4, N=2` `SU(2)` background.

**Structural observation worth recording.** In the free `d`-dimensional route the *only*
hard step is the Clifford collapse `S(k)^2 = (sum_mu sin^2 k_mu) I`
(`...DISPERSION...:135`: "This is the only dimension-dependent algebraic step"), needed
because the momentum fold produces a `2^d`-dimensional corner space that must be reduced
to `2 x 2` blocks. **At a fixed background that step is not needed and is not available.**
There is no fold, no reduced momentum, no corner space; `h[U]` is simply an anti-Hermitian
operator and (2.13) is an exact operator identity in the commutative algebra `C[h[U]]`.
The gauged lift of the *classical block* is therefore **strictly easier** than the free
`d`-dimensional lift, not harder. The difficulty in the gauged case lives entirely in §3
(reflection) and §4 (bridge inputs).

### 2.7 The stable frame — full algebra

Define, exactly as `...CAR_FOCK...:150-152, :205-206`,

```text
   U_pole   = [ I ; Z^{1/2} B ] (I+Z)^{-1/2},
   W_stable = [ Z^{1/2} ; B  ] (I+Z)^{-1/2}.                                        (2.14)
```

*Isometry.* `U_pole^dag U_pole = (I+Z)^{-1/2}[ I + B^dag Z B ](I+Z)^{-1/2}`. By §2.5,
`B^dag Z B = Z B^dag B = Z`, so the bracket is `I + Z` and `U_pole^dag U_pole = I`.
Identically `W_stable^dag W_stable = (I+Z)^{-1/2}[Z + B^dag B](I+Z)^{-1/2} = I`.

*Eigen-relation.* Claim `T_2 W_stable = W_stable Z`. Drop the common right factor
`(I+Z)^{-1/2}` (it commutes with `Z`) and compute the two block rows of
`T_2 [Z^{1/2}; B]`.

Row 1: `(4R^2 + I) Z^{1/2} - 2(m I - h) B`. Since `B = (m I + h)R^{-1}`,

```text
   (m I - h) B = (m I - h)(m I + h) R^{-1} = (m^2 I - h^2) R^{-1} = R^2 R^{-1} = R,
```

so row 1 `= (4R^2 + I) Z^{1/2} - 2R`. Using `R = sinh E`, `Z^{1/2} = e^{-E}`,
`Z^{-1/2} = e^{E}`:

```text
   4R^2 + I - 2R Z^{-1/2} = 4 sinh^2 E + 1 - 2 sinh E * e^{E}
                          = (2 cosh 2E - 2 + 1) - (e^{E} - e^{-E}) e^{E}
                          = (e^{2E} + e^{-2E} - 1) - (e^{2E} - 1)
                          = e^{-2E} = Z,
```

hence row 1 `= Z^{1/2}(4R^2 + I - 2R Z^{-1/2}) = Z^{1/2} Z`, which is the first block of
`[Z^{1/2}; B] Z`. Row 2: `-2(m I + h) Z^{1/2} + B = (m I + h)[ R^{-1} - 2 Z^{1/2} ]`, and

```text
   R^{-1} - 2Z^{1/2} = R^{-1}[ I - 2R Z^{1/2} ] = R^{-1}[ 1 - (e^{E}-e^{-E}) e^{-E} ]
                     = R^{-1}[ 1 - 1 + e^{-2E} ] = R^{-1} Z,
```

so row 2 `= (m I + h) R^{-1} Z = B Z`, the second block of `[Z^{1/2}; B] Z`. Therefore

```text
   T_2[U] W_stable = W_stable Z[U].                                                 (2.15)
```

**Verified numerically** to `1.2e-15` at the `SU(2)` background, and **exactly in sympy**
at the rational instance of §6.1C. Likewise `J_Z U_pole = W_stable Z^{-1/2}` with
`J_Z = diag(I, Z^{-1})`, since
`J_Z U_pole = [I; Z^{-1/2}B](I+Z)^{-1/2} = [Z^{1/2}; B](I+Z)^{-1/2} Z^{-1/2}` by §2.5.

**Spectrum.** By (2.15) and its reciprocal partner, `spec(T_2[U]) = { e^{+2E_j}, e^{-2E_j} }`
with `E_j = asinh( sqrt(m^2 + a_j^2) )`, `i a_j in spec(h[U])`. This is `RP_P2...:68-73`
verbatim, now with the frames attached. `m > 0` gives `E_j >= asinh(m) > 0`, so the
reciprocal pair is **strictly** split, `lambda_- < 1 < lambda_+`, at every background;
therefore the Riesz projectors
`P_-+ = (T_2 - lambda_-+ I)/(lambda_-+ - lambda_+-)` are well defined per eigenline. This
is used in §4.

### 2.8 Staticity is NECESSARY, not merely convenient

`RP_P2...:147` lists "time independence of the same spatial matrix over the two slices" as
an **input choice**. I can sharpen it to an iff:

**Proposition.** Let `h_even`, `h_odd` be the (anti-Hermitian) spatial hops on even and odd
slices, `T_even = [[-2(mI+h_even), I],[I,0]]`, `T_odd = [[-2(mI-h_odd), I],[I,0]]`. Then
`T_odd = T_even^dag` **iff** `h_odd = h_even`.

*Proof.* `T_even^dag = [[-2(mI+h_even)^dag, I],[I,0]] = [[-2(mI-h_even), I],[I,0]]` by
(2.6). Comparing with `T_odd` entrywise gives `mI - h_odd = mI - h_even`. QED.

So if the background is time-dependent (`U_mu(x,0) != U_mu(x,1)`), `T_2 = T_odd T_even` is
not of the form `T^dag T`, is not Hermitian, and can have genuinely complex spectrum.
**Falsification run:** `d = 1, L_s = 4, N = 1, U(1)` phases on slice 0 cyclically shifted
on slice 1, `m = 1/2` gives `||T_2 - T_2^dag|| = 3.00` and `max |Im spec T_2| = 2.46`.
The two-step positivity is destroyed, not merely inconvenienced. Everything in §3–§4
therefore carries **static background** as a hypothesis.

---

## 3. The reflected Gram at a background

### 3.1 Setup

Arena: infinite temporal lattice `t in Z`, finite spatial torus `Lambda`, temporal gauge
`U_0 = 1`, **static** spatial background `U_mu(x)` (§2.8), `m > 0`, one Grassmann component
per site, colour fiber `C^N`. Two-slice cells: cell `c` carries slices `(2c, 2c+1)`. OS
reflection `theta(t) = -1 - t`, so cell `c` reflects to cell `-1-c`; the positive-time half
is `t >= 0`.

The space-time operator whose inverse is the propagator is read off the mode equation
`(m I + (-1)^t h) psi_t + (1/2)psi_{t+1} - (1/2)psi_{t-1} = 0`
(`...DISPERSION...:96-97`, rearranged):

```text
   D_{t,t} = m I + (-1)^t h[U],     D_{t,t+1} = + (1/2) I,     D_{t,t-1} = - (1/2) I. (3.1)
```

Note `(-1)^t h[U]` uses the **same** `h[U]` on both slice parities (staticity), which is
what makes `D` a two-slice-periodic operator.

### 3.2 The Bloch block and its determinant — operator form

Fourier transform in the cell index with multiplier `zeta`; slices `(even, odd)` inside the
cell. The even slice couples forward within its own cell (`+1/2`) and backward into cell
`c-1` (`-1/2`, factor `zeta^{-1}`); the odd slice couples forward into cell `c+1` (`+1/2`,
factor `zeta`) and backward within its own cell (`-1/2`). Hence, with `h := h[U]`,

```text
   D(zeta) = [[ m I + h,          (1 - zeta^{-1})/2 * I ],
              [ (zeta - 1)/2 * I,        m I - h        ]].                          (3.2)
```

This is `...CAR_FOCK...:95-97` with the substitution `M + i lambda -> m I + h`,
`M - i lambda -> m I - h`, which is exactly right because the eigenvalues of `h` are
`i lambda`.

All four blocks of (3.2) lie in the commutative algebra `C[h]` (§2.5), so the block
"determinant" is unambiguous:

```text
   Delta(zeta) = (m I + h)(m I - h) - [ (1 - zeta^{-1})/2 ][ (zeta - 1)/2 ] I
               = (m^2 I - h^2) - (1/4)( zeta - 1 - 1 + zeta^{-1} ) I
               = R^2 + (2 - zeta - zeta^{-1})/4 * I.                                 (3.3)
```

Factorization: I claim `Delta(zeta) = -(zeta I - Z)(zeta I - Z^{-1}) / (4 zeta)`. Expand
the right side:

```text
   -(zeta^2 I - zeta(Z + Z^{-1}) + I)/(4 zeta)
      = [ (Z + Z^{-1}) - zeta I - zeta^{-1} I ] / 4.
```

Comparing with (3.3) `= [ 4R^2 + 2 I - zeta I - zeta^{-1} I ]/4` requires
`Z + Z^{-1} = 2 I + 4 R^2`, and indeed
`Z + Z^{-1} = e^{-2E} + e^{2E} = 2 cosh 2E = 2(1 + 2 sinh^2 E) = 2 I + 4 R^2` since
`sinh E = R`. **Exact, at operator level, at any background.** The inside root is `Z`
(spectrum in `(0,1)` by (2.5)); the outside root is `Z^{-1}`.

### 3.3 The cell-separation-one residue — exact mode computation

The mode-level computation is the honest way to get the coefficient, so I did it in sympy
with `lambda` symbolic and `Z` carried as the inside root (using
`r^2 = (Z + Z^{-1} - 2)/4`). With
`D^{-1} = Delta^{-1} [[ mI - h, -(1-zeta^{-1})/2 ],[ -(zeta-1)/2, mI + h ]]` and
`G_n := (1/2 pi i) oint dzeta zeta^{-n-1} D(zeta)^{-1}` (sum of the residues at
`zeta = Z` and `zeta = 0`), the exact result at `n = -1` is

```text
   G_{-1} = ( 2z/(1+z) ) [[ sqrt(z) b*,   1        ],
                          [ z,            sqrt(z) b ]],       b = (m + i lambda)/r.  (3.4)
```

(Derivation of the entries from the raw sympy output: the diagonal entries come out as
`4z^2(i lambda - m)/(z^2-1)` and `4z^2(-i lambda - m)/(z^2-1)`; using
`(1-z)/sqrt(z) = 2r`, i.e. `z^2 - 1 = -2 r sqrt(z)(1+z)`, these become
`2 z^{3/2}(m - i lambda)/(r(1+z)) = (2z/(1+z)) sqrt(z) b*` and
`(2z/(1+z)) sqrt(z) b`. The off-diagonals come out as `2z/(z+1)` and `2z^2/(z+1)`.)

The other Bloch sign, `n = +1`, gives the same matrix with the off-diagonal `1` and `z`
replaced by `-z` and `-1`; it does **not** assemble into a PSD Gram. **This is a genuine
convention fork and I flag it as such (§7, L8):** the residue algebra alone does not fix
the Bloch sign; the combination "(Bloch sign) x (index rule)" is what is pinned, and it is
pinned by the requirement that the assembled Gram reproduce the landed
`K_lambda = (2z/(1+z))[[1, sqrt(z)b],[sqrt(z)b*, z]]`.

### 3.4 The index rule — the spatial swap is load-bearing

Apply `...CAR_FOCK...:145`: `K((a,x),(b,y)) = G((t_b, y), (theta(t_a), x))` with
`t_0 = 0`, `t_1 = 1`, `theta(t) = -1-t`, so `theta(t_0) = -1` (cell `-1`, within-cell index
`1`) and `theta(t_1) = -2` (cell `-1`, within-cell index `0`). All four entries come from
the **same** cell-separation-one coefficient, with within-cell indices `(b, 1-a)`:

```text
   K_{ab} = (G_{-1})_{b, 1-a}.
```

Reading off (3.4): `K_{00} = (G_{-1})_{0,1} = 1`, `K_{01} = (G_{-1})_{1,1} = sqrt(z) b`,
`K_{10} = (G_{-1})_{0,0} = sqrt(z) b*`, `K_{11} = (G_{-1})_{1,0} = z`, all times
`2z/(1+z)`:

```text
   K_lambda = (2z/(1+z)) [[ 1,          sqrt(z) b ],
                          [ sqrt(z) b*, z         ]],                                (3.5)
```

which is `...CAR_FOCK...:110-114` **exactly**. And with `v = (1+z)^{-1/2}[1, sqrt(z)b*]^T`,

```text
   v v^dag = (1/(1+z)) [[ 1,            sqrt(z) b ],
                        [ sqrt(z) b*,   z |b|^2   ]],       |b|^2 = (m^2+lambda^2)/r^2 = 1,
```

so `K_lambda = 2z v v^dag`: rank one, spectrum `{0, 2z}`, PSD. `...CAR_FOCK...:120-125`
reproduced.

**The spatial swap in the index rule is not cosmetic.** I initially dropped it (kept the
slice reordering but not the `(y,x)` swap) and the dense-inverse certificate came out
**wrong by exactly a spatial transpose**: every "`h`-odd" matrix element had the opposite
sign, giving a `+-1` elementwise ratio against the closed form (residual `8.7e-2` at
`d=1, L_s=4, U=1, m=1/2`). Restoring `G((t_b,y),(theta(t_a),x))` gave machine precision.
I record the mis-step because it is the natural mistake and it is a good mutation gate
(§6, G7b).

### 3.5 Theorem 3 (gauged reflected Gram) — the conjugate-background frames

At a background, `h[U]` is **not** real in the site basis, so the free note's realness
route (`...CAR_FOCK...:144-146`: "the staggered hop is real, so complex conjugation maps
an `H=i lambda` eigenvector to an `H=-i lambda` eigenvector") is unavailable. Execute
instead the note's own escape clause (`:83-85`, `:441`): replace `H` by `conj(H)` in the
frames. The point is that `conj(h[U])` is not an abstract object:

**Lemma 3.1.** `conj( h[U] ) = h[ Ubar ]`, where `Ubar_mu(x) := conj(U_mu(x))`.

*Proof.* Conjugate (1.2) entrywise. `xi_mu(x)` is real. `conj(U_mu(x))` is `Ubar_mu(x)`.
And `conj(U^dag) = conj(conj(U)^T) = U^T = (conj U)^dag = Ubar^dag`, so the backward term
conjugates to `-(1/2) xi_mu(x) Ubar_mu(x-e_mu)^dag delta_{y,x-e_mu}`. Summing gives
`h[Ubar]`. QED. **Verified exactly** (sympy, `d=2, L=(4,2), N=2`, rational `SU(2)`).

`SU(N)` and `U(1)` are closed under entrywise conjugation (`Ubar in SU(N)` when
`U in SU(N)`; for `U(1)`, `Ubar = U^{-1}`), so `Ubar` is an admissible background of the
same group. This is the same map that
`CORNER_TRANSFER...:100` records: "`K`/CPT conjugation acts on the background as
`U -> conj(U)`" — reached here from OS reflection rather than from CPT. **Consistency
cross-check between two independent landed surfaces; not a citation used as proof.**

**Lemma 3.2.** `R[Ubar] = conj(R[U])`, `E[Ubar] = conj(E[U])`, `Z[Ubar] = conj(Z[U])`,
`B[Ubar] = conj(B[U])`; and since these are Hermitian (resp. unitary), conjugation equals
transposition, so `spec(Z[Ubar]) = spec(Z[U])`.

*Proof.* `R[U]^2 = m^2 I - h[U]^2` conjugates to `m^2 I - h[Ubar]^2 = R[Ubar]^2`. If
`P > 0` is Hermitian then `conj(P) = P^T > 0` is Hermitian, and `(P^T)^2 = (P^2)^T =
conj(P^2)`; uniqueness of the positive square root gives `R[Ubar] = conj(R[U])`. The same
argument (real spectral functions commute with conjugation of a Hermitian matrix) gives
`E`, `Z`. Then `B[Ubar] = (m I + h[Ubar]) R[Ubar]^{-1} = conj((m I + h[U])R[U]^{-1}) =
conj(B[U])`. Spectra: `spec(A^T) = spec(A)`. QED. **Verified numerically:**
`max |sort spec Z[Ubar] - sort spec Z[U]| = 0.0` at `d=2, L=(4,2), N=2, SU(2)`.

**Theorem 3 (fixed-background reflected two-slice Gram).** On the arena of §3.1, with
`h := h[U]` and the *conjugate-background* polar data
`Zc := Z[Ubar]`, `Bc := B[Ubar]`,

```text
   U_pole[Ubar] = [ I ; Zc^{1/2} Bc ] (I + Zc)^{-1/2},        U_pole[Ubar]^dag U_pole[Ubar] = I,

   K_n[U] = 2 U_pole[Ubar] Zc^{n} U_pole[Ubar]^dag                                   (3.6)
          = conj( 2 U_pole[U] Z[U]^{n} U_pole[U]^dag ),          n >= 1.
```

Equivalently, with `A[Ubar] := sqrt(2) Zc^{1/2} U_pole[Ubar]^dag` and
`W := U_pole[Ubar]^dag`, `C := Zc`:

```text
   K_1[U] = A[Ubar]^dag A[Ubar],      K_n[U] = A[Ubar]^dag Zc^{n-1} A[Ubar],
   K_n[U] = 2 W^dag C^n W,            P_OS[U] = U_pole[Ubar] U_pole[Ubar]^dag.        (3.7)
```

*Proof of the mode-to-operator step.* Write the propagator's spatial structure in the
eigenbasis of `h`: `G = sum_lambda K_lambda tensor |u_lambda><u_lambda|` with
`h u_lambda = i lambda u_lambda`. The index rule of §3.4 puts the *reflected* argument in
the row slot, i.e. the operator kernel is the spatial transpose of `G`:
`(|u><u|)^T = conj(|u><u|) = |ubar><ubar|`. Now `conj(h) ubar = conj(h u) = conj(i lambda u)
= -i lambda ubar`, i.e. by Lemma 3.1 `h[Ubar] ubar = -i lambda ubar`. On that eigenline,
`R[Ubar] ubar = r ubar` and

```text
   B[Ubar] ubar = (m I + h[Ubar]) R[Ubar]^{-1} ubar = ((m - i lambda)/r) ubar = b* ubar,
```

which is exactly the second component of the support column
`v = (1+z)^{-1/2}[1, sqrt(z) b*]^T` of (3.5). Hence the operator whose per-eigenline
value is `v` is `U_pole[Ubar]`, and assembling `K_lambda = 2 z v v^dag` over eigenlines
gives (3.6). The `conj(...)` form follows from Lemma 3.2, since
`U_pole[Ubar] = conj(U_pole[U])` blockwise. QED.

*Positive semidefiniteness.* Immediate from (3.7):
`K_n[U] = (Zc^{n/2} W)^dag (Zc^{n/2} W) >= 0`. Equivalently, from the `conj` form:
`conj` of a Hermitian PSD matrix is its transpose, which is Hermitian PSD. **So there is
no PSD obstruction: the gauged reflected Gram is PSD for every static background, every
`d`, every `N`, every `n >= 1`.** Moreover

```text
   rank K_n[U] = dim h = |Lambda| * N,        spec K_n[U] = {0}^{dim h} u { 2 z_j^n },
   P_OS[U]^2 = P_OS[U] = P_OS[U]^dag,         U_pole[Ubar]^dag P_OS[U] U_pole[Ubar] = I,
   U_pole[Ubar]^dag (K_1[U]/2) U_pole[Ubar] = Zc.
```

*Parity bridge.* §1.5 gives `Pi h[U] Pi = -h[U]` at every background, hence
`Pi Z[U] Pi = Z[U]` and `Pi B[U] Pi = B[U]^dag`, so with `boldPi = diag(Pi,Pi)` the free
note's relation `V = boldPi U_pole Pi` (`...CAR_FOCK...:236`) transfers verbatim to
each background, applied to the conjugate-background frames.

### 3.6 Numerical certificate and the decisive mutation

Method: build `D` of (3.1) densely on an open temporal chain `t in [-T, T)` at a static
background, invert, extract `K_n` by the §3.4 rule, compare to (3.6).

| instance | `n` | frames from `h[Ubar]` | frames from `h[U]` (MUTANT) | `min eig K_n` | rank |
|---|---|---|---|---|---|
| `d=1, L_s=4, N=2`, `SU(2)`, `m=1/2`, `T=30` | 1 | `4.1e-14` | `1.88e-1` | `-1.2e-16` | 8 |
| same | 2 | `8.3e-14` | `1.07e-1` | `-4.0e-17` | 8 |
| same | 3 | `2.4e-13` | `4.5e-2` | `-1.0e-17` | 8 |
| `d=2, L=(4,2), N=2`, `SU(2)`, `m=1/2`, `T=26` | 1 | `5.6e-16` | `8.3e-2` | `-2.0e-16` | 16 |
| `d=1, L_s=4, N=1`, `U(1)` (Gaussian-rational phases) | 1 | `3.6e-12` | — | `-4.7e-19` | 4 |

`spec K_1` at the `d=1, L_s=4, N=2` `SU(2)` instance came out
`{0 x 8, 0.296331 x 4, 0.730644 x 4}` against `2 spec(Zc) = {0.296331 x 4, 0.730644 x 4}`.
Rank equals `dim h = |Lambda| N` in every row.

**The `h[U]`-frame variant is a decisive mutation control** (residuals `10^-1`, six to
twelve orders above the correct frames), directly analogous to the free note's own
`V`-frame control (`...CAR_FOCK...:257-259`: "the `V`-frame variant of the same formulas
fails on the actual carrier by an order-`10^-2` residual"). At `U = 1` the mutation is
**invisible** (`h[Ubar] = h[U]`), which is exactly why this is the piece the gauged lift
had to supply.

Residuals are limited by the open-chain boundary, not by the identity: the landed arena
statement `...CAR_FOCK...:332-336` says finite open chains converge exponentially to the
vacuum Gram and are not exactly equal. My certificate is therefore "exact up to
exponentially small boundary images", consistent with that boundary, and I do **not**
claim finite-`T` exactness.

### 3.7 What I did NOT prove here — the honest scope of §3

* The object I computed is the **Gaussian/propagator-level** reflected Gram at fixed `U`:
  the two-point kernel of the fermion bilinears. It is **not** the full mixed
  gauge-times-fermion Haar-Berezin Gram of
  `RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md`
  (`:80-87`), which integrates over links and covers gauge-times-fermion entangled
  observables via `G_ij = sum kappa_gamma (C_f) conj(V) V` (`:280-283`). Those are
  different objects at different levels; mine is fixed-`U`, no Haar integration.
* I did **not** re-derive the Grassmann/Berezin sign convention. The overall sign and
  normalization of the reflected Gram are fixed by the reflection rule
  `theta(chi(x,t)) = -bar-chi(x,1-t)`, `theta(bar-chi(x,t)) = -chi(x,1-t)`
  (`RP_COUPLED...:60-64`) and the measure-ordering sign (`RP_COUPLED...:148-152`); that
  note pins them by an exact one-site Berezin computation giving
  `C_r = diag(1, 1/2, 1/2, 1/4)` (`:236-239`) and shows the unphased map yields `-1/2`
  diagonal entries (`:213-216`). **I take the propagator-level Gram as given and inherit
  that sign pinning; I do not re-prove it.** If the supervisor wants the Grassmann-level
  gauged statement, that is a separate piece of work.
* No `U`-integration, no Haar measure, no dynamical gauge. Every statement is
  config-by-config at fixed static `U`.

---

## 4. The identification `T^2[U] = Gamma(t[U])`

### 4.1 The supplied inputs, named before the theorem

I list these first so the theorem cannot be read as stronger than it is. Items (S1)–(S3)
are exactly the three the branch note names for the free case
(`...D_DIMENSIONAL_TWO_STEP_MANY_BODY...:191-196`: "the passage from the classical
monodromy to the quantum kernel has three supplied parts — the stable-half-line selection
prescription, the one-mode exponential kernel form, and the finite-mode functor").
Items (S4)–(S5) are **additional and specific to the gauged case**.

**(S1) Stable-half-line selection prescription.** `AXIOM_FIRST_RP_TWO_STEP...:156-164`,
verbatim:

> "The positive-time coherent-state transfer is the
> stable half-line channel on `P_-`: a forward solution with any `P_+`
> component grows like `lambda_+^N` over `N` two-step blocks, so finite-action /
> finite-norm positive-time propagation sets that coefficient to zero."

This is a prescription, not a theorem: on a finite time extent both reciprocal solutions
have finite norm. Its sentence is background-blind — nothing in it mentions `U`, `d`, or
the fiber — so it transfers verbatim; what changes is only the *furnishing* of the `2 x 2`
blocks it acts on, which §2.6–§2.7 supplies at operator level.

**(S2) Coherent-state kernel form.** `AXIOM_FIRST_RP_TWO_STEP...:166-169`, verbatim:

> "For a one-mode coherent-state kernel
> `<bar z'|T_2|z> = exp(bar z' lambda_- z)`, the induced operator on the
> finite exterior algebra is exactly `diag(1,lambda_-)`; across momenta this is
> the wedge product `Gamma(K_2)`."

The exponential form is **supplied, not action-derived**, at every `d` including the
landed `d = 1` (branch note `:150-155`, `:335-337`). §4.4 records that the gauged case
needs a **strictly stronger** version of this supply, and why.

**(S3) Finite-mode functor.** The five items of
`MICROCAUSALITY_CORNER_CLASS...:58-71` quoted in §0.5, plus the pin at `:104-107`.

**(S4) Static background.** `U_mu(x,0) = U_mu(x,1) = U_mu(x)`. Listed as an input choice
at `RP_P2...:147`; sharpened to a **necessary** condition in §2.8. Without it `T_2` is
not Hermitian and nothing downstream survives.

**(S5) Temporal gauge `U_0 = 1`.** Needed so the crossing fermion bilinear carries no
temporal link: `RP_COUPLED...:41-43`, verbatim: "There is no temporal link in the crossing
fermion bilinear: temporal gauge has removed it." Without it the two-slice cell operator
(3.2) acquires temporal link matrices in the off-diagonal blocks, which then fail to
commute with the diagonal blocks and (3.3) is no longer a scalar-block determinant.

### 4.2 What is DERIVED here (not supplied)

D1. `h[U]^dag = -h[U]` at any background, from the phase property alone (Theorem 1).
D2. `T_2[U] = T_even[U]^dag T_even[U] >= 0` with the explicit block form (2.13), at
    operator level, with no momentum fold and no Clifford step (§2.6).
D3. Strict reciprocal split `lambda_-(j) = e^{-2E_j} < 1 < e^{+2E_j} = lambda_+(j)` for
    `m > 0` at **every** background, hence per-eigenline Riesz projectors
    `P_-+ = (T_2 - lambda_-+ I)/(lambda_-+ - lambda_+-)` are well defined (§2.7). The
    float-free certificate is `(I + 2R^2)^2 - 4R^2(I+R^2) = I` and
    `R^2(I+R^2) - R^4 = R^2 > 0` (§2.2).
D4. `t[U] := Z[U]` is Hermitian, positive definite, `spec subset (0,1)` (§2.2).
D5. The change of Grassmann variables from the site basis to the `Z[U]`-eigenbasis is a
    **number-conserving unitary** `V`; the Berezin pair measure transforms by
    `det(V) det(conj V) = |det V|^2 = 1`, so the measure is invariant. (This matters for
    (S2): see §4.4.) Note the contrast with
    `CORNER_TRANSFER...:86-93`, which forces the Berezin pair normalization `lambda = 1`
    by the trace identity; here the invariance is under a unitary change of modes, a
    different statement.
D6. Everything in §4.3 that follows from (S3) is elementary finite-dimensional linear
    algebra, and I verified all of it directly at a gauged background (§4.5).

### 4.3 Theorem 4

**Theorem 4 (fixed-background operator identification).** Assume (S1)–(S5) and the
setup of §3.1. Let `t[U] := Z[U] = e^{-2E[U]}` be the selected forward two-step
one-particle kernel of D2–D4. Then, at `a_tau = 1`, on the fermionic Fock space
`F(h) = direct_sum_q wedge^q h` with `dim h = |Lambda| N`:

```text
   T^2[U] = Gamma( t[U] ),
   T^2[U] = B_F^dag B_F,        B_F = Gamma( t[U]^{1/2} ) = Gamma( e^{-E[U]} ),
   H[U]  = -(1/2) log T^2[U] = dGamma( E[U] ) >= 0,
   Tr_F T^2[U] = det_h( 1 + t[U] ) = prod_{j=1}^{|Lambda| N} ( 1 + e^{-2E_j[U]} ),
   Gamma(t[U]) a^dag(f) = a^dag( t[U] f ) Gamma(t[U])   for all f in h.               (4.1)
```

*Proof.* By D4, `t[U]` is strictly positive, so `log t[U] = -2E[U]` is a bounded
self-adjoint operator and item 3 of (S3) gives
`Gamma(t[U]) = exp(dGamma(log t[U])) = exp(-2 dGamma(E[U]))`, hence
`-(1/2) log Gamma(t[U]) = dGamma(E[U])`. `E[U] >= asinh(m) I > 0` by (2.3), and `dGamma`
of a positive operator is positive on every `wedge^q` (its eigenvalue on an occupation
vector is the sum of the occupied `E`-eigenvalues, all `>= asinh(m) > 0`), so `H[U] >= 0`
with equality only on the vacuum. Functoriality (item 1) with
`t[U] = t[U]^{1/2} t[U]^{1/2}` and `Gamma(A)^dag = Gamma(A^dag)` (immediate from
`wedge^q A^dag = (wedge^q A)^dag`) gives
`Gamma(t[U]) = Gamma(t^{1/2})^dag Gamma(t^{1/2}) = B_F^dag B_F >= 0`. Item 4 gives the
trace identity. Item 2 gives the intertwiner, and by (S3) item 2 the intertwiner **plus**
vacuum-fixing determines `Gamma(t[U])` uniquely — this is the pin, and it is what (S2)
supplies on the kernel side: given the exponential form, the induced one-mode operator is
exactly `diag(1, lambda)` with vacuum element `exp(0) = 1`, so a Gaussian prefactor
`C != 1` is excluded relative to the form. Item 5 (direct sums) gives the factorization
over the eigenmodes of `t[U]`. QED, **given (S1)–(S5)**.

**What (4.1) settles relative to the landed tree.** `MICROCAUSALITY_CORNER_CLASS...:34-41`
and `:143-145` name exactly this as unsupplied ("no current source identifies the
classical fixed-background recurrence matrix with a Fock-space `Gamma(t[U])`"). Theorem 4
supplies it **at the same conditional status as the landed free case**, plus (S4)–(S5),
plus the §4.4 strengthening. It is **not** a from-scratch derivation and must not be
described as one.

### 4.4 The honesty item the gauged case adds: one-mode form is not enough

The free construction gets away with the **one-mode** kernel form because the selected
kernel is diagonal in a background-independent basis (momenta / `S(k)`-eigenmodes). The
branch note states this explicitly (`...D_DIMENSIONAL...:159-161`): "The selected
one-particle kernel is diagonal in the `S(k)`-eigenmode basis, so the many-body coherent
kernel has no cross terms and factorizes over modes".

**At a fixed background there is no such basis.** `t[U] = Z[U]` is Hermitian positive
definite, hence diagonal in *its own* eigenbasis, but that eigenbasis is `U`-dependent and
is not the site basis in which the Grassmann integration variables are defined. Two routes,
which are the same supply written two ways:

* (i) Supply the **multi-mode Gaussian** coherent kernel
  `<bar z'| T_2 |z> = exp( sum_{ij} bar z'_i t[U]_{ij} z_j )` directly. This is strictly
  stronger than (S2) as landed.
* (ii) Keep the one-mode form (S2), but apply it in the `t[U]`-eigenbasis. This requires
  the extra declaration that the many-body kernel **factorizes over those modes**, i.e.
  that the multi-mode kernel is the product of one-mode kernels in that basis — which is
  precisely statement (i).

Route (ii) is legitimate as far as the measure goes: D5 shows the Berezin measure is
invariant under the number-conserving unitary change of modes, and `Gamma` is basis-free
(`Gamma(V t V^dag) = Gamma(V) Gamma(t) Gamma(V)^dag` by functoriality). So the *only*
cost is the strengthened supply, not a measure anomaly. But it **is** a cost, and the
landed free note's (S2) sentence does not cover it. I flag it as an open honesty gap:

> **Gauged supply gap.** Theorem 4 needs the multi-mode Gaussian coherent-kernel form.
> `AXIOM_FIRST_RP_TWO_STEP...:166-169` supplies only the one-mode form. Either the
> multi-mode form must be supplied explicitly (and named as supplied), or it must be
> derived from the quadratic action — which no source in the tree currently does, at any
> `d`, including `d = 1`.

### 4.5 The mismatch that only exists at a background: transfer side vs OS side

This is the sharpest finding in the report and it has a sign that is easy to miss.

* **Transfer side.** The action/monodromy at background `U` gives, via §2.6–§2.7 and
  Theorem 4, `T^2[U] = Gamma(Z[U])`, with `T_2[U] W_stable[U] = W_stable[U] Z[U]`.
* **OS side.** The reflected two-slice Gram at the *same* background gives, by Theorem 3,
  the quotient transfer `Z[Ubar]`, not `Z[U]`:
  `U_pole[Ubar]^dag (K_1[U]/2) U_pole[Ubar] = Z[Ubar]`.

The free note's intertwiner `L (K_1/2) = T_2 L` with `L = W_stable U_pole^dag`
(`...CAR_FOCK...:245-252`) therefore becomes, at a background,

```text
   L[U] := W_stable[Ubar] U_pole[Ubar]^dag,        L[U] ( K_1[U] / 2 ) = T_2[Ubar] L[U],  (4.2)
```

because `T_2[Ubar] W_stable[Ubar] = W_stable[Ubar] Z[Ubar]` by (2.15) applied at `Ubar`.
**The OS quotient of the background `U` is intertwined with the two-step transfer at the
conjugate background `Ubar`.** At `U = 1`, or at any `K`-real background (`Ubar = U`), the
two coincide and the mismatch is invisible — which is exactly why the free note never had
to face it.

The mismatch is **not** spectral. By Lemma 3.2, `spec Z[Ubar] = spec Z[U]` and
`det(1 + Z[Ubar]) = det(1 + Z[U])` (a determinant is transpose-invariant). Verified
numerically at `d=1, L_s=4, N=2, SU(2), m=1/2`:
`max|sort spec Z[Ubar] - sort spec Z[U]| = 0.0`, `det(1+Z[U]) = det(1+Z[Ubar]) =
6.038910171196345`, while `||Z[Ubar] - Z[U]||_max = 0.1476` against `||Z||_max = 0.2567`
(58% relative — genuinely different operators).

So the honest statement is a **three-tier** one, and it is a native re-derivation, from OS
reflection, of the structure that `CORNER_TRANSFER...:113-118` reached from `K`/CPT:

| level | same-background at general `U`? | reason |
|---|---|---|
| spectra, traces, `det(1+t)`, `Tr Gamma`, dispersion | **YES** | `Z[Ubar] = Z[U]^T` |
| operator identification `T^2 = Gamma(t)` on the transfer side | **YES** (Theorem 4, at `U`) | derived at `U` directly |
| identification of the **OS-quotient** transfer with the transfer-side operator | **NO in general; YES exactly on the `K`-real class `Ubar = U`** | (4.2) |

Compare `CORNER_TRANSFER...:113-118` verbatim: "On general backgrounds, the operator-level
statement is the conjugated-background statement: reading-1 data at `U` equal reading-2
data at `conj(U)`; operator-level unitary equivalence at the same background is asserted
only on the `K`-invariant class." and "**Registrable trace data are same-background
equivalent at EVERY fixed background.**" My tiers reproduce that split exactly, from an
independent route. I record this as agreement, not as a proof by citation.

The `K`-real class is concrete: for `U(1)`, `Ubar = U^{-1}`, so `K`-real means every link
is `+-1`; for `SU(N)`, `K`-real means every link lies in `SO(N) subset SU(N)`.

### 4.6 Verification of Theorem 4 at a gauged background

Built `Gamma(Z[U])` by exterior minors on subsets of the `n = |Lambda| N` one-particle
modes (`d = 1, L_s = 2, N = 2`, `SU(2)`, `m = 1/2`, Fock dimension `2^4 = 16`):

| check | residual |
|---|---|
| `Gamma(Z)` Hermitian | `0.0` |
| `min eig Gamma(Z) > 0` | `+1.36e-3` |
| `Tr Gamma(Z) - det(1+Z)` | `0.0` |
| `Gamma(Z) - Gamma(Z^{1/2})^dag Gamma(Z^{1/2})` | `5.6e-17` |
| `-(1/2) log Gamma(Z) - dGamma(E)` | `4.5e-16` |
| `Gamma(Z) - exp(-2 dGamma(E))` | `3.5e-17` |
| canonical intertwiner, all `f = e_j` | `2.8e-17` |

**Negative result I am obliged to report.** The `W`-conjugate pin mutation
(`MICROCAUSALITY_CORNER_CLASS...:96-103`) is **vacuous at this instance**: `spec Z[U]` came
out fully degenerate (`{0.19201276}^4`), so `Gamma(Z)` is scalar on each particle sector,
every occupation-swap `W` commutes with it (`||[W, Gamma]|| = 0.0` for all four swaps
tried), and the mutation cannot discriminate. Cause: `SU(2)` is the unit quaternions,
their real span is the quaternion algebra, and every quaternion `q` obeys
`q qbar = |q|^2 I` — so `-h[U]^2` comes out **scalar** on this carrier. This is the same
caveat the branch note states for the free case (`...D_DIMENSIONAL...:163-165`: "on fully
degenerate instances it cannot [discriminate], and the runner says so honestly"), but with
a *gauged-specific cause* that the free discussion does not name. §6 gives the fix.

On a non-degenerate instance (`d = 1, L_s = 4, N = 1`, `U(1)` with Gaussian-rational
phases, `spec Z = {0.16477203^2, 0.28745714^2}`) the pin gate does fire:
swapping two 2-particle occupation states with distinct `Gamma`-eigenvalues gives
**trace difference exactly `0.0`** and **intertwiner error `2.02e-2`**.

---

## 5. Fiber bookkeeping

### 5.1 Where `N` enters — exhaustive list

The one-particle space is `h = C^Lambda tensor C^N`, `dim h = |Lambda| N`.

1. **Dimension / mode count.** `dim h = |Lambda| N`. At `U = 1` the free `d`-dimensional
   count is `prod_mu (L_mu/2) * 2^d = prod_mu L_mu = |Lambda|` *per colour*
   (`...D_DIMENSIONAL...:178-180`), so the total is `|Lambda| N`. The `2^d` taste corners
   are **spatial-fold bookkeeping on a scalar fiber**; the colour `N` multiplies on top.
   Do not conflate them — the branch note is explicit that the corners are not a matrix
   fiber (`:197-200`, `:305-309`).
2. **Fock dimension.** `dim F(h) = 2^{|Lambda| N}`. This is the only place the fiber makes
   the object exponentially larger and it is what forces the structured (subset-indexed)
   assembly rather than dense matrices beyond very small carriers.
3. **Trace identity.** `Tr_F Gamma(t[U]) = det_h(1 + t[U]) = prod_{j=1}^{|Lambda| N}
   (1 + e^{-2E_j})` — the product has `|Lambda| N` factors, not `|Lambda|`. Same for
   `CORNER_TRANSFER...:84-86`'s `Tr Gamma(t[U]) = det(1 + t[U])`.
4. **Degeneracy structure.** Two sources, both fiber-relevant:
   * the parity involution `Pi h[U] Pi = -h[U]` (§1.5) forces `spec(h[U])` to be symmetric
     under `i a -> -i a`, so **every eigenvalue of `Z[U]` has even multiplicity at every
     background**;
   * for `N = 2` with `SU(2)` links the quaternion identity gives *extra* degeneracy
     (§4.6). Measured: `d=1, L_s=4, N=2`, `SU(2)`: only **2 distinct** eigenvalues of `R^2`
     out of 8. Replacing `SU(2)` by `U(2) = phase x SU(2)` gives **4 distinct** out of 8
     (the parity minimum). At `L_s = 2, N = 2`, `SU(2)` collapses to **1 distinct** value
     (fully scalar), while `U(2)` gives 2.
5. **Envelope / locality constants.** `N` appears **nowhere** in §1–§4, because no
   operator-norm envelope, decay rate, or Lieb-Robinson constant is used or produced
   anywhere in this report. If one is ever built, it carries the fiber factor per
   `MICROCAUSALITY_CORNER_CLASS...:152-154`, quoted in §0.5.

### 5.2 Do scalar-fiber results transfer? — split answer

**YES, unconditionally, for everything in §1–§4.** Every statement proved above is
**fiber-blind**: Theorem 1 uses only the phase property and the adjoint-pairing of the hop
coefficients (the `N x N` matrices `U_mu(x)` are never opened up); §2 uses only
`h^dag = -h`, `m > 0` scalar, and finite dimension; §3 uses only anti-Hermiticity plus the
conjugation Lemma 3.1 (which is entrywise and fiber-blind); §4 uses only (S1)–(S5) and
finite-dimensional exterior algebra. **The colour index rides along as extra one-particle
modes and nothing else.** I verified this by running the identical checks at `N = 1`
(`U(1)`) and `N = 2` (`SU(2)`, `U(2)`) with identical residual quality.

**NO for any envelope, rate, or norm constant** — exactly the corner note's warning. Also
**NO for degeneracy-dependent conclusions**: any statement whose gate relies on `spec Z`
being non-degenerate (in particular the canonical-intertwiner pin) must be re-checked per
fiber and per background, because the fiber can *create* degeneracy (§4.6, §5.1.4). This
is a real transfer failure and I would not have found it without running it.

---

## 6. Exact gate designs (float-free inputs)

Design rules I followed: (a) every input is an exact rational or a Gaussian rational of
modulus one; (b) positivity is certified by exact polynomial sign patterns, never by a
numerical eigenvalue; (c) every gate names the mutation it catches; (d) gates that
*cannot* discriminate at a given instance say so.

### 6.1 Backgrounds

**A — identity.** `U_mu(x) = I_N` for all `mu, x`. Any `d`, any even `L`, any `N`.
Role: free-collapse control. **Explicitly vacuous for G7c and G12** (`Ubar = U`); the gate
must assert that rather than pass silently.

**B — nontrivial `U(1)`.** `N = 1`, Gaussian-rational unit-modulus phases:
`(3+4i)/5`, `(5+12i)/13`, `(8+15i)/17`, `(7+24i)/25`.
* `d = 1, L_s = 4`: all four on the four links. **Warning I verified:** in `d = 1` the
  background enters only through the **total holonomy**. Measured: the spectrum of `R^2`
  for the four-phase background equals that of the single-link background carrying the
  same product to `4.4e-16`, and the uniform background `U_x = i` (holonomy `i^4 = 1`) has
  spectrum **identical to free**. So a `d = 1` `U(1)` gate must fix a holonomy `!= 1`, and
  cannot test anything beyond holonomy.
* `d = 2, L = (4,2)`: all links `1` except `U_1((0,0)) = (3+4i)/5` and
  `U_2((1,0)) = (5+12i)/13`, giving nonzero plaquette flux — the genuinely
  `d >= 2` instance.

**C — nontrivial `SU(2)`, fully closed-form rational (the workhorse instance).**
`d = 1, L_s = 2, N = 2, m = 1/4`,

```text
   U_1(0) = I_2,        U_1(1) = [[ 3i/5,  4/5 ],
                                  [ -4/5, -3i/5 ]].
```

`U_1(1)` is the unit quaternion `(0, 3/5, 4/5, 0)`; `U^dag U = I`, `det U = 1`, entries in
`Q(i)`. **Verified exactly in sympy:**

```text
   h^dag = -h  (exact),      -h^2 = (1/2) I_4  (exact),
   R^2 = m^2 I - h^2 = (9/16) I,     R = (3/4) I,     S := (I+R^2)^{1/2} = (5/4) I,
   Z^{1/2} = S - R = (1/2) I,        Z = (1/4) I,     E = asinh(3/4) = log 2,
   B = (4/3)(m I + h)   with   B^dag B = I  EXACTLY (rational),
   U_pole^dag U_pole = I  exactly,
   T_2 W_stable = W_stable Z  exactly,
   charpoly(T_2) = (lambda - 4)^4 (4 lambda - 1)^4 / 256,
      i.e. spec T_2 = { e^{+2E} = 4 (x4), e^{-2E} = 1/4 (x4) }.
   K_1 = 2 U_pole Z U_pole^dag = (2/5) [[ I, (1/2)B^dag ],[ (1/2)B, (1/4) I ]]  (rational),
      Hermitian, rank 4 = |Lambda| N, trace 2.
```

Construction recipe (so the supervisor can generate more): pick a rational `s`, set
`a = (1/s - s)/2`, `b = (1/s + s)/2`, so `b^2 - a^2 = 1` and `R = a`, `S = b`,
`Z^{1/2} = b - a = s`, `Z = s^2`, `E = -log s` are all rational/closed form. Then choose
`m` and the background so that `m^2 + |A|^2 = a^2` where `A = (1/2)(U_1(0) - U_1(1)^dag)`
and `|A|^2` is the quaternion norm; with `U_1(0) = I` one has
`|A|^2 = (2 - 2 Re q)/4` for `U_1(1) = q`. Instance C is `s = 1/2`, `a = 3/4`, `b = 5/4`,
`Re q = 0`, `|A|^2 = 1/2`, `m = 1/4`.

**D — general Cayley `SU(2)`.** `U = (I - K)(I + K)^{-1}` with
`K = [[ i a, b + i c ],[ -b + i c, -i a ]]`, `a,b,c in Q`. `K^dag = -K`, `tr K = 0`, so `U`
is unitary with `det U = 1` and entries in `Q(i)` (the inverse of `I + K` is rational
because `det(I+K) = 1 + a^2 + b^2 + c^2 in Q`). Use for randomized-but-exact regression
scans.

**E — `U(2)` degeneracy breaker.** `U_mu(x) = w_mu(x) V_mu(x)` with `w` a Gaussian-rational
unit phase and `V` from D. Needed because pure `SU(2)` is quaternionic and over-degenerates
(§4.6, §5.1.4). Measured degeneracy counts are in §5.1.4.

### 6.2 Gates

| # | gate | exact certificate | mutation it catches |
|---|---|---|---|
| **G1** | `h[U] + h[U]^dag = 0` | zero matrix over `Q(i)` | (M1) phase carries `x_mu` dependence, e.g. `xi_mu -> (-1)^{x_mu} xi_mu` — **verified**: `h` becomes exactly Hermitian; (M2) backward link `U^dag -> U`; (M3) backward link taken at `x` instead of `x - e_mu` |
| **G2** | `xi_mu(x + e_mu) = xi_mu(x)` for all `mu, x` | combinatorial identity, exact | isolates *which* property G1 consumes: any phase depending on its own coordinate |
| **G3** | `(mI+h)^dag(mI+h) - (m^2 I - h^2) = 0` | zero matrix over `Q(i)` | scalar mass replaced by a mass matrix `M` with `[M,h] != 0` (the §2.5 boundary) — cross terms no longer cancel |
| **G4** | `R > 0`: charpoly of `-h^2` has strictly alternating coefficient signs | exact integer/rational sign pattern (Hermitian ⟹ real roots; Descartes ⟹ no negative root) | M1 (`h` Hermitian ⟹ `-h^2 <= 0`, sign pattern flips) |
| **G5** | `spec Z subset (0,1)`: `(I + 2R^2)^2 - 4R^2(I + R^2) = I` **and** `R^2(I+R^2) - R^4 = R^2` with `R^2 = m^2I - h^2` invertible | two exact matrix identities over `Q(i)` + exact invertibility (`det != 0`) | `m = 0` with singular `h` ⟹ `R^2` singular ⟹ the `z < 1` certificate degenerates to `z = 1` at that mode |
| **G6** | `B` unitary | (a) G3; (b) symbolic one-mode `conj(b) b - 1 = 0` with `b = (m + i lam)/sqrt(m^2+lam^2)`, `lam` symbolic; (c) at instance C, `B = (4/3)(mI+h)` and `B^dag B - I = 0` exactly | `R` built from `m^2 I + h^2` (wrong sign) ⟹ fails. **Honest trap to record:** `B' = (mI - h)R^{-1}` is *also* unitary, so G6 does **not** catch a sign flip on `h` inside `B` — that is G8's job |
| **G7a** | mode-level residue: symbolic `G_{-1}` from `D(zeta)^{-1}`, then `K_lambda = 2z v v^dag` | sympy exact with `lam`, `z` symbolic | the other Bloch sign `n = +1` ⟹ diagonal `(-z, -1)` ⟹ negative trace ⟹ not PSD |
| **G7b** | index rule: `K((a,x),(b,y)) = G((t_b,y),(theta(t_a),x))` | exact rational finite-chain inverse at instance C, small `T` | dropping the **spatial** swap ⟹ result is the spatial transpose; every `h`-odd entry sign-flips (**verified**: elementwise ratio `+-1`, residual `8.7e-2` at the free instance) |
| **G7c** | frames from `h[Ubar]`, not `h[U]` | `K_n[U] - 2 U_pole[Ubar] Z[Ubar]^n U_pole[Ubar]^dag = 0` | `h[U]` frames ⟹ **verified** residuals `1.9e-1 / 1.1e-1 / 4.5e-2` at `n = 1,2,3`. **Vacuous at background A** — the gate must assert vacuity there rather than pass |
| **G8** | `T_2 W_stable - W_stable Z = 0` | exact at instance C (all rational) | `B -> (mI - h)R^{-1}` (the sign flip G6 misses); `T_odd -> T_even` (staticity dropped) |
| **G9** | `K_1 >= 0`, `rank K_1 = |Lambda| N` | charpoly of `K_1` has alternating signs with exactly `|Lambda| N` trailing zero coefficients | unphased reflection `theta(chi) = +bar-chi` ⟹ negative odd diagonal entries per `RP_COUPLED...:213-216` |
| **G10** | Fock: (i) `Gamma(A)Gamma(B) = Gamma(AB)` on two **noncommuting** exact rationals; (ii) `Gamma(t)a^dag(f) = a^dag(tf)Gamma(t)` for every basis `f`; (iii) `Tr Gamma(t) = det(1+t)`; (iv) `Gamma(t) = Gamma(t^{1/2})^dag Gamma(t^{1/2})`; (v) `-(1/2)log Gamma(t) = dGamma(E)` | exact at instance C (`t = (1/4)I`, `t^{1/2} = (1/2)I`) | `Gamma` built by trace matching only ⟹ (ii) fails |
| **G11** | **pin**: `Gamma_tilde = W Gamma W^dag`, `W` swapping two occupation states with **distinct** `Gamma`-eigenvalues | trace preserved exactly; intertwiner residual nonzero | **must NOT be run at instance C** — `spec Z = (1/4)I` is scalar there and the gate is vacuous (**verified**: `||[W,Gamma]|| = 0`). Run at instance B (`d=1, L_s=4, U(1)`): **verified** trace diff `0.0`, intertwiner error `2.02e-2`, or at instance E |
| **G12** | conjugate-background law | `conj(h[U]) - h[Ubar] = 0` exactly; `charpoly(Z[Ubar]) = charpoly(Z[U])` exactly; `Z[Ubar] - Z[U] != 0` exactly at a non-`K`-real background; `Z[Ubar] = Z[U]` exactly on the `K`-real class (`U(1)`: links `+-1`; `SU(N)`: links in `SO(N)`) | asserting same-background operator equality at a non-real background — **verified** `||Z[Ubar]-Z[U]|| = 0.148` vs `||Z|| = 0.257` |
| **G13** | staticity necessity | with `h_even != h_odd`: `T_2 - T_2^dag != 0` exactly, and `charpoly(T_2)` has non-real roots (exact Sturm/discriminant test) | silently assuming staticity — **verified** `||T_2 - T_2^dag|| = 3.00`, `max|Im spec| = 2.46` |
| **G14** | free collapse at background A | every gauged display reduces **exactly** to the landed free display; `h[Ubar] = h[U]`; G7c and G12 residuals are exactly `0` | a gauged formula that does not reproduce the landed free note; and (in the other direction) the gate records that A cannot discriminate G7c/G12 |
| **G15** | fiber counting | `dim h = |Lambda| N`; `dim F = 2^{|Lambda| N}`; `det(1+t)` has exactly `|Lambda| N` factors | dropping the colour fiber (`N -> 1`) ⟹ trace identity off by the wrong number of factors |
| **G16** | open-chain convergence, not exactness | exact rational residual `||K_1^{(T)} - K_1^{vacuum}||` at `T = 4, 6, 8` is **strictly decreasing** | claiming finite-`T` exactness — the landed arena statement `...CAR_FOCK...:332-336` forbids it |

### 6.3 Gate-sequencing note

G1–G6 are pure operator-algebra and need no chain inverse; G7–G9 need the finite chain;
G10–G11 need the Fock assembly (dense only at instance C, `2^4 = 16`; use subset-indexed
scalars beyond that); G12–G16 are controls. G7c and G11 are the two gates that carry the
genuinely new content and both are **vacuous at the naive instance choice** (background A
for G7c; instance C for G11). A runner that only used A and C would pass while testing
nothing.

---

## 7. LIMITS

Every assumption, convention fork, and under-determination I hit. I have made no attempt
to make this list short.

**L1 — Provenance.** `FREE_STAGGERED_D_DIMENSIONAL_TWO_STEP_MANY_BODY_TRANSFER_IDENTITY_NOTE_2026-07-20.md`
is **not on `origin/main`** (§0.0). Anything downstream that treats it as landed is
mistaken today.

**L2 — Convention correction, not a choice.** The task's `eta_mu(x)` inside `h` is wrong
for this repo; the correct phase is the purely spatial `xi_mu(x)`, with the `(-1)^t` living
outside as the slice alternation (§1.1). If a downstream note carries `eta_mu` inside `h`
it double-counts the time alternation.

**L3 — Static background is a hypothesis and it is necessary** (§2.8, G13). Not
"convenient", not "for simplicity". Time-dependent backgrounds destroy `T_odd = T_even^dag`
and with it Hermiticity and positivity of `T_2`.

**L4 — Temporal gauge `U_0 = 1` is a hypothesis** (S5). Outside temporal gauge the
two-slice block (3.2) acquires temporal links in the off-diagonal entries, which break the
commutativity that (3.3) uses.

**L5 — Scalar mass is load-bearing** (§2.3, §2.5). A mass matrix (taste-splitting, Wilson
term, background-dependent mass) breaks the cross-term cancellation (2.7) and the
commutation `[h, R] = 0`, and with them `B B^dag = I` and the whole `C[h]` argument.

**L6 — Unitarity of the links is NOT used for anti-Hermiticity** (§1.3), only the
adjoint-pairing of forward and backward hop coefficients. Unitarity *is* used for
`SU(N)`-closure of `U -> Ubar` (§3.5) and would be used for any norm bound. Do not
over-attribute.

**L7 — Realness is used in exactly one place and I replaced it, not removed it.** The free
note's operator-level Gram needs `H* = H` (`...CAR_FOCK...:79-85`, `:441`). The gauged
replacement is `h[Ubar] = conj(h[U])`. This is the note's own escape clause instantiated,
so it is not new mathematics — but it is new *content* in the sense that no landed note
executes it at a gauge background.

**L8 — Two convention forks in the Gram that the sources under-determine.**
(i) The **Bloch sign** (whether the cell-separation-one coefficient is `n = +1` or `n = -1`)
and (ii) the **index rule** (which argument of `G` is the row index, and whether the
spatial indices swap). Neither is fixed by the residue algebra alone; only the *combination*
is pinned, by the requirement that the result equal the landed
`K_lambda = (2z/(1+z))[[1, sqrt(z)b],[sqrt(z)b*,z]]`. I determined the pinning combination
by direct comparison against a dense chain inverse (§3.4) rather than by reading it off,
because the sources state the rule (`...CAR_FOCK...:145`) without deriving it.

**L9 — The Grassmann/Berezin sign convention is inherited, not re-derived** (§3.7). The
reflection phases `theta(chi) = -bar-chi`, `theta(bar-chi) = -chi` and the measure-ordering
sign are pinned by `RP_COUPLED...:60-64, :148-152, :199-216`. I take the propagator-level
Gram as the object and do not re-prove the Grassmann-level sign at a background. **A
gauged Grassmann-level re-derivation is not done here and should not be assumed.**

**L10 — Arena.** Everything is the vacuum / infinite temporal lattice with a finite spatial
torus. Finite open temporal chains converge exponentially and are **not** exactly equal
(`...CAR_FOCK...:332-336`); my numerical certificates inherit that and are exact only up to
boundary images. Finite temporal circles (thermal winding images) are untouched.

**L11 — The multi-mode kernel supply gap** (§4.4). Theorem 4 needs the multi-mode Gaussian
coherent-state kernel; the tree supplies only the one-mode form. This is a **new**
conditionality relative to the landed free case, not a restatement of it.

**L12 — The selection prescription remains a prescription** (S1). It is supplied at every
`d` and at every background. Nothing here upgrades it.

**L13 — `C = 1` is pinned only relative to the supplied kernel form.** Same status as the
branch note (`...D_DIMENSIONAL...:290-297`). Given the form, the constant term forces
`C = 1`; the form itself is supplied.

**L14 — OS-side / transfer-side mismatch** (§4.5). At a general background the OS quotient
transfer is `Z[Ubar]`, the transfer-side operator is `Z[U]`. They agree spectrally always,
and as operators exactly on the `K`-real class. **Any note that writes
`L (K_1[U]/2) = T_2[U] L` at a general background is wrong**; the correct statement is
(4.2) with `T_2[Ubar]`.

**L15 — Degeneracy traps** (§4.6, §5.2, G11). `SU(2)` links are quaternionic and can make
`-h^2` scalar (fully so at `L_s = 2, N = 2`); the parity involution forces even
multiplicity at every background. Any gate that relies on non-degeneracy must be run on a
`U(2)`/`SU(3)`/larger-lattice instance and must declare vacuity otherwise.

**L16 — `d = 1` `U(1)` backgrounds carry only holonomy** (§6.1B, verified to `4.4e-16`).
A `d = 1` `U(1)` gate with trivial holonomy is *identical to the free case* and tests
nothing gauged.

**L17 — `L_mu = 2` is a live instance gauged and a degenerate one free** (§1.5). The free
hop vanishes identically at `L_mu = 2`; the gauged one does not. Gate instances that reuse
free `L = 2` anchors will mis-read what they are testing.

**L18 — Not claimed, at all.** No `U`-integration; no Haar measure; no gauge-invariant
statement (everything is config-by-config at fixed `U`, and I have not checked covariance
of `K_n[U]` under a spatial gauge transformation `U_mu(x) -> g(x) U_mu(x) g(x+e_mu)^dag`,
though it should hold by conjugation of `h[U]` — **I did not verify it and do not assert
it**); no interacting or non-quadratic transfer; no locality, envelope, kernel-decay, or
Lieb-Robinson content; no continuum or infinite-volume limit; no single-step positivity
(false already at `d = 1`); no species/occupancy/taste selection; no physical time
(`a_tau = 1` is a convention); no anomaly, chirality, or determinant-weight statement; no
new axiom or primitive; no audit verdict.

**L19 — Things I checked and could not settle.** (i) Gauge covariance of `K_n[U]` (see
L18). (ii) Whether the multi-mode kernel form of §4.4 can be *derived* from the quadratic
action at fixed `U` — I did not attempt it, and the tree does not do it at any `d`.
(iii) Sharpness of anything: no constant here is claimed sharp. (iv) Whether the `K`-real
class `Ubar = U` is the *exact* class on which the OS/transfer operator identification
coincides, or only a sufficient one — I proved sufficiency, not necessity.

**L20 — Numerical certificates are floats.** §3.6, §4.6, §5.1.4 use numpy dense
inverses/eigendecompositions. They are evidence about the identities, not exact proofs;
the exact proofs are the displayed algebra, and the float-free gates are §6. Do not cite
the tables as exact results.

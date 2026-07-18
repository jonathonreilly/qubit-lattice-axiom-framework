# Worker A (scout) analysis: transfer-side bridge inventory for the quasilocal-class block

**Seat disclosure.** This scout ran as Opus 4.8 at max reasoning effort
(owner-directed substitution under the workhorse skill's substitution
clause; supervisor remains responsible). Read-only, exactly the five
files named in the spec.

**How to read this file.** For anything load-bearing I quote the note
verbatim with line context and put my own remarks outside the quotes.
Every place where I do arithmetic or sketch a route that is NOT in the
notes, I mark it `[SCOUT DERIVATION]` and flag its confidence. I set no
audit status for any note. LIMITS are at the end.

---

## Convention key (needed before the inventory — the notes disagree on metric)

The five notes do NOT share one distance/weight convention, and the
weighted hypothesis in the spec is metric-agnostic, so I fix vocabulary
first:

- **Note 1 (Combes-Thomas)** decays the one-particle kernel in the sup
  metric `||x - y||_inf` (its eq. (7)).
- **Notes 2 & 4** use the `l1` graph metric `d(x,y) = ||x-y||_1` and a
  per-site *overlap* norm.
- **Note 3 (free bilinear)** uses `l1` distance `d_1` for its weight but
  imports the kernel bound in `||z||_inf`, and pays for the mismatch with
  the conversion `||z||_1 <= d ||z||_inf` (this is why its finiteness
  condition is `d mu < eta`, not `mu < eta`).
- **Note 5 (fermionic CAR)** uses the `Z^3` graph distance and
  fixed nearest-neighbor walk constants (bonds per site 6, bond-adjacency
  degree 10).

The spec's weighted hypothesis
`sup_x sum_{S containing x} ||h_S|| |S| e^{mu diam S} <= kappa` does not
name a metric; any exact geometric sum over `Z^3` therefore has to fix
one, and the finiteness threshold on `mu` moves by a factor of `d`
between the `l_inf` and `l1` readings. I keep this explicit throughout.

---

## Note 1 — GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13

**(a) Object it controls: a ONE-PARTICLE kernel (single-particle sector),
on a fixed gauge background — NOT a many-body Hamiltonian, NOT yet a
bilinear generator.** Header, lines 7-8:

> "**Claim type:** bounded_theorem (fixed-background, single-particle
> sector; Combes-Thomas route)"

The object, lines 56-61:

> "The reconstructed single-particle Hamiltonian on the fixed background
> is the matrix function `h[U] = arcsinh( sqrt( D[U] ) )`"

with `D[U] = m^2 I + ( sum_{mu=1}^d s_mu[U] )^2` (eq. (1), lines 53). It
is a matrix indexed by lattice sites; the note works entirely with its
position-space kernel blocks `<x| h[U] |y>`. It never second-quantizes
`h[U]` into a Fock-space bilinear — that step is left to the consumer.

**(b) Decay/quasilocality form it proves.** The main result (G5), lines
150-162:

> "`|| <x| h[U] |y> ||  <=  Const(m, d) e^{-gamma_CT ||x - y||_inf}` ,
> `gamma_CT = min(1/2, (m^2/2) / (2 e (m^2 + d^2) B(2, d))) > 0 ,
> B(2, d) = 5^{d-1} * 6`"

with (line 159)

> "`Const(m, d) = (|Gamma|/2 pi) (sup_Gamma|f|) (2/eta)` finite, and
> **both `gamma_CT` and `Const` independent of the background `U` and of
> the volume**."

The gap that powers it is uniform (G1), lines 89-93:

> "`m^2 I  <=  D[U]  <=  (m^2 + d^2) I ,    i.e.
> spec(D[U]) subset [m^2, m^2 + d^2]` ... uniformly in `U` and volume,
> with `dist(spec(D[U]), (-inf, 0]) = m^2 > 0`."

Load-bearing hypotheses (lines 230-234): compact gauge group / unitary
links (`||S_mu|| <= 1`) and **mass gap `m > 0`** ("at `m = 0` the kernel
is a power law"). The rate is a *lower bound only* and not sharp — (G7),
lines 180-184:

> "`gamma_CT` is a **lower bound** on the true gauged rate and is
> generically not sharp; the true gauged rate is background-dependent and
> can **exceed** `arcsinh(m)`".

**(c) Declared open tasks relevant to a many-body quasilocal-class LR
bound.** Explicit, lines 314-316:

> "(iii) The full **many-body fermionic** transfer-matrix locality or a
> **Lieb-Robinson lightcone** — that needs the separate quasilocal-LR
> composition step (the free note's item 3), still a separate theorem."

Also open (lines 312-314): the `U`-integrated / dynamical case, and a
**sharp** gauged rate.

**(d) Does it supply / could it supply the weighted-norm hypothesis for a
bilinear generator from a decaying one-particle kernel?** It supplies the
**kernel input**, not the weighted norm itself. What (G5) gives is
exactly an *exponentially decaying one-particle kernel, uniform in the
gauge background and volume* — i.e. the `|h(z)|`-type bound that a
block08-style identification needs, but now for arbitrary fixed `U`
(where Note 3's Fourier route does not apply). It does NOT: (i) form the
Fock-space bilinear `sum_{x,y} <x|h[U]|y> c_x^dag c_y`; (ii) evaluate any
per-site weighted sum `sum_y ||<x|h[U]|y>|| e^{mu||x-y||}`; (iii) touch
the many-body commutator. So Note 1 is the natural **decaying-kernel
supplier for the gauged case**; the weighted-norm step and the
second-quantization are missing and would be block08's job. `[SCOUT
DERIVATION, high confidence]` Because the (G5) bound is a clean
exponential in `||x-y||_inf` uniform in `U`, the block08 shell-sum below
goes through with `K = Const(m,d)` and `eta = gamma_CT`; the only
caveats are that `gamma_CT` is conservative (so `mu < gamma_CT` is a
weaker window than the sharp `mu < arcsinh(m)` available at `U = 1`), and
that `<x|h[U]|y>` is a matrix block, so the second-quantized generator is
genuinely operator-valued (relevant to the fermionic route, Note 5, not
the scalar route, Note 3).

---

## Note 2 — EXP_DECAY_LIEB_ROBINSON_QUASILOCAL_BRIDGE_THEOREM_NOTE_2026-06-11

**(a) Object it controls: a general MANY-BODY Hamiltonian (arbitrary
support family), in the Hastings-Koma weighted-norm framework.** Lines
35-40:

> "A Hamiltonian is written as `H = sum_{Z subset Lambda} h_Z`, where
> each `h_Z = h_Z^*` acts trivially outside `Z`, and the sum is finite."

Not a one-particle kernel, not specifically bilinear — the general
support-family object. This is the note whose *shape* block07 must match.

**(b) Exact decay/quasilocality form.** The weight, lines 43-45:

> "`F_{mu,alpha}(r) = exp(-mu r) / (1+r)^alpha`"

The interaction norm, eq. (1), lines 49-54:

> "`||H||_{mu,alpha} := sup_{u,v in Lambda} F_{mu,alpha}(d(u,v))^{-1}
> sum_{Z contains u,v} ||h_Z||`"

with the more local diameter version, lines 57-62, that *implies*
finiteness of (1):

> "`sup_u sum_{Z contains u} ||h_Z|| / F_{mu,alpha}(diam Z)` ... implies
> finiteness of (1), because `d(u,v) <= diam Z` for every `u,v in Z` and
> `F_{mu,alpha}` is decreasing."

The reproducing constant, eq. (2), lines 66-69:
`C_alpha^{(d)} := 2^alpha S_alpha^{(d)}`,
`S_alpha^{(d)} := sum_{z in Z^d} (1+||z||_1)^(-alpha) < infinity` for
`alpha > d`. The LR bound (L3), eq. (4), lines 92-99:

> "`||[ exp(i t H) A_x exp(-i t H), B_y ]|| <= (2 ||A_x|| ||B_y|| /
> C_alpha^{(d)}) ( exp(2 C_alpha^{(d)} J_F |t|) - 1 ) F_{mu,alpha}(d(x,y))`"

and finite velocity (L4), eq. (5): `v(mu') = 2 C_alpha^{(d)} J_F / mu'`.

**The load-bearing obstruction to the spec's *pure* exponential (L1),
lines 17-31 / 75-81.** This is the single most important sentence in the
whole packet for reading the spec's weighted form:

> "so no volume-independent convolution constant exists for the pure
> exponential weight. This note uses the standard reproducing weight with
> a polynomial denominator and displays the finite constant."

and the mechanism, lines 27-29:

> "`sum_z G_mu(d(x,z)) G_mu(d(z,y)) / G_mu(d(x,y))  >=  R + 1`"

for `G_mu(r) = exp(-mu r)`.

**(c) Declared open tasks relevant to a many-body quasilocal-class LR
bound.** Lines 380-381:

> "A separate source would still be needed to prove exponential
> log-locality for a broader interacting transfer family from the
> framework premises."

The consumer corollary (L6, lines 125-131) is explicitly *conditional* on
a downstream source supplying finite `J_F = ||H_log||_{mu,alpha}`.

**(d) Does it supply / could it supply the spec's weighted hypothesis?**
Partly — and the mismatch is the crux. Note 2 proves a weighted-norm
many-body LR bound, which is *a* version of what block07 wants, but with
**two differences from the spec's stated hypothesis** that are
load-bearing:

1. **Weight form.** The spec asks for the *pure* exponential
   `e^{mu diam S}` (times `|S|`). Note 2's finite convolution constant
   exists only for the *polynomially corrected* `F_{mu,alpha}`, and its
   (L1) proves the pure-exponential reproducing constant is *unbounded*.
   So a block07 that literally uses the spec's pure-exponential weight
   **cannot** route through Note 2's reproducing-inequality method — it
   would have to use the *direct* weighted-path method instead (Note 3's
   Step 2), which pulls the `e^{-mu d(x,y)}` factor out up front and
   never forms the convolution ratio. `[SCOUT DERIVATION, medium-high
   confidence — see the (d) synthesis section for why the direct method
   evades L1; the exact per-step constant needs a runner.]`
2. **No `|S|` factor and no walk-expansion/all-time form.** Note 2's norm
   (1) is a two-point overlap `sum_{Z contains u,v}`, not the one-point
   `sum_{S containing x} ||h_S|| |S|` of the spec; and its bound is the
   `(exp(...) - 1)` Duhamel-series form, not the family's all-time
   volume-uniform walk-expansion form (Note 5).

So Note 2 **could** supply the weighted hypothesis's *consumer side*
(it is literally built to consume a finite weighted norm), but only in
its own polynomial-corrected convention; it does not supply, and by (L1)
warns against, the spec's pure-exponential convolution route.

---

## Note 3 — FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10

**(a) Object it controls: the MANY-BODY BILINEAR generator built FROM the
one-particle kernel — this is exactly the spec's target object, but only
for `U = 1`.** Claim scope, lines 6-10:

> "in the free (`U = 1`) bilinear staggered two-step sector, the exact
> reconstructed Hamiltonian `H = -log(T_hat^2)/(2 a_tau)` whose kernel is
> supplied by [transfer-matrix log-quasilocality] obeys a finite-velocity
> quasilocal Lieb-Robinson envelope."

The generator is the second-quantized bilinear, lines 46-52:

> "`H = sum_{x,y} h(x-y) a_x^dag a_y`,
> `|h(z)| <= (1/a_tau) C_d(eta,m) exp(-eta ||z||_inf)`"

for every `0 < eta < eta* := arcsinh(m)`, with
`C_d(eta,m) = sqrt(m^2 + (d-1) + cosh^2 eta)`. **This is the "bilinear
generator built from an exponentially decaying one-particle kernel" of
the spec's question (d), already constructed.**

**(b) Exact decay/quasilocality form.** The weighted norm, lines 77-79:

> "`W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))`."

**Note this is the spec's weighted hypothesis specialized to a two-body
support (`|S| = 2`, `diam S = d_1(x,y)`), up to the constant `|S| = 2`.**
Finiteness (B1), lines 81-92:

> "If `0 < d mu < eta < arcsinh(m)`, then `W_mu` is finite. Indeed ...
> `W_mu <= (C_d(eta,m)/a_tau) sum_{r>=0} [(2r+1)^d - (2r-1)^d]
> exp(-(eta - d mu) r)`, where the `r=0` shell is read as one site. The
> right-hand side converges because `eta - d mu > 0`."

The LR bound (B2), eq. (1), lines 96-99:

> "`||[alpha_t(A_x), B_y]|| <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu
> |t|)`."

with lightcone speed `v_mu = 4 W_mu / mu`. **Crucially, this bound uses
the PURE exponential weight** (no `(1+r)^alpha` correction), obtained by
the *direct* weighted-path method, Step 2, lines 138-145:

> "`prod_j ||Phi_{x_{j-1} x_j}|| <= exp(-mu d_1(x,y)) prod_j
> (||Phi_{x_{j-1} x_j}|| exp(mu d_1(x_{j-1},x_j)))`, by the triangle
> inequality. Summing over intermediate sites bounds the weighted path
> sum by `exp(-mu d_1(x,y)) W_mu^n`."

**(c) Declared open tasks relevant to a many-body quasilocal-class LR
bound.** Lines 22-23:

> "the gauged/interacting exact-log locality and full continuum
> microcausality are not claimed here."

Boundaries, lines 193-195: "It does not prove gauged/interacting
log-transfer locality." Mass gap required (`m = 0` gives power-law tails,
no positive `eta`).

**(d) Does it supply the spec's weighted hypothesis?** **For the `U = 1`
scalar bilinear, YES — it already IS the route the spec asks about**,
both halves:

- Its **(B1)** *is* the block08 identification for `U = 1`: it takes the
  exponentially decaying kernel and produces the finite pure-exponential
  weighted norm `W_mu`, with the exact `Z^d` shell sum
  `sum_r [(2r+1)^d - (2r-1)^d] e^{-(eta-d mu)r}`.
- Its **(B2)** *is* the block07 LR bound for the bilinear case, and it
  does so with the **pure** exponential — demonstrating in a landed note
  that the direct weighted-path method evades Note 2's (L1) obstruction
  when the interaction is two-body.

What it does NOT cover, and what a new block would add: (i) non-trivial
`U` (the gauged kernel of Note 1); (ii) the *fermionic* CAR realization
(Note 3 uses the commuting per-site ladder convention — see Note 4's
scope caveat below — not anticommuting `c`s); (iii) the general
`|S| > 2` support family; (iv) the all-time volume-uniform
walk-expansion *form* of the current family (Note 5). So Note 3 is the
strongest single piece of prior art for the proposed split, and the
split's novelty must be measured against it (overlap flags below).

---

## Note 4 — MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09

**(a) Object it controls: a general MANY-BODY support-family Hamiltonian
via a self-contained FINITE-RANGE LR lemma, plus its application to the
framework hopping bilinear.** The lemma object, support-family constants
(6), lines 168-172:

> "`q := max_{Z in F} |Z|` (largest support size), `R := max_{Z in F}
> diam(Z)` (largest support diameter), `W := max_{x in Lambda} Sum_{Z ∋
> x} ||h_Z||_op` (per-site overlap weight)"

Applied unconditionally to the hopping Hamiltonian `H_hop = Σ H_xy + m Σ
n̂_x` (F4), and *conditionally* to the exact reconstructed `H = -log(T)/a_τ`
(F5).

**(b) Exact decay/quasilocality form.** The proved lemma (F3-L1), eq. (7),
lines 266-268:

> "`|| [α_t(A), B] ||_op  ≤  2 ||A|| ||B|| · (|X|/q) · Σ_{n ≥ ⌈D/R⌉}
> (2 q W |t|)^n / n!`"

and the exponential lightcone (F3-L2), eq. (16)/(16b), lines 274-282:

> "`v_LR := 2 · e · q · W · R.`  ...
> `|| [α_t(A), B] ||_op  ≤  (2e/(e-1)) · ||A|| ||B|| · (|X|/q) ·
> exp( -(D - v_LR·|t|)/R )`."

Unconditional application to the hopping bilinear (F4), lines 302-304:
`v_LR ≤ 4 · e · (|m| + 2d)` (on `Z^3`, `≈ 65.24` at `m -> 0`). The
per-site weight here is **unweighted** (`W = max_x Σ_{Z ∋ x} ||h_Z||`,
no `e^{mu diam}`), and the lemma requires **strictly finite** `R`.

**(c) Declared open tasks relevant to a many-body quasilocal-class LR
bound.** This note *names the exact gap block07 would close*. (F5), lines
347-352:

> "Under the quasilocal restatement, the analogous lightcone follows from
> (F3-L2) applied to each truncation `H_R` (`q = 2`, `diam_l1 <= d·R`,
> `W <= W_H`) composed with Duhamel/interpolation control of the
> exponentially small tail `H - H_R`; that one-step composition theorem is
> not proved here or in the cited note."

and C1, lines 700-702:

> "The remaining missing step is exactly one hypothesis: non-perturbative
> finite-range/quasilocal control of `H = -log(T)/a_τ`."

**(d) Does it supply / could it supply the spec's weighted hypothesis?**
No — but it supplies the **proof template block07 upgrades**. Its `W` is
the *unweighted* per-site overlap, and its lemma is *finite-range*
(needs bounded `R`). The spec's `sup_x sum_{S containing x} ||h_S|| |S|
e^{mu diam S}` is precisely the *weighted* upgrade of this note's `W`
(the `|S| ~ q` and the `e^{mu diam S}` are exactly the two ingredients
the finite-range version drops). The self-contained iterated-commutator
proof (Steps 4-5, lines 490-596) — one-step inequality, chain-weight
counting `Σ_{chains, length k} ||h_{Z_1}||···||h_{Z_k}|| ≤ (|X|/q)(qW)^k`
(lines 552-555), reach constraint `k ≥ ⌈D/R⌉` — is the skeleton a
weighted block07 re-runs with `qW -> q·kappa` and the geometric decay
supplied by the weight instead of by the reach cutoff. `[SCOUT
DERIVATION, medium confidence]` The replacement is not purely mechanical:
in the finite-range proof the spatial decay comes from the reach
constraint `k ≥ D/R`; in the weighted version it comes from pulling out
`e^{-mu D}` (Note 3's move), so the two proofs share the chain-counting
but differ in where the decay is booked. block07 must choose one; I
recommend Note 3's direct booking (evades L1).

---

## Note 5 — MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18

**(a) Object it controls: a MANY-BODY FERMIONIC (CAR) bond Hamiltonian,
nearest-neighbor, in the family's all-time volume-uniform walk-expansion
form.** Hypotheses, lines 71-83:

> "A finite region `Λ ⊂ Z^3` with induced nearest-neighbor bond set
> `E(Λ)` ... the CAR algebra `CAR(Λ)` with generators `c_x, c_x^†` ... A
> supplied bond Hamiltonian `H = Σ_{b∈E(Λ)} h_b` with each `h_b`
> **even**, Hermitian, in `CAR(b)`, and `J = max_b ||h_b||`".

The one new load-bearing ingredient is the **graded locality lemma**,
lines 118-125:

> "`A·B = (−1)^{p·q} B·A`. By bilinearity: **even `A` commutes with every
> disjoint `B`** (any parity), and **odd-odd disjoint pairs anticommute**".

**(b) Exact decay/quasilocality form.** The theorem, lines 207-211:

> "`||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10) Σ_{k≥d}
> (20J|t|)^k / k!`
> `≤ ||[A, B]|| + 2||A|| ||B|| (n_X/10) · ((20J|t|)^d/d!) · e^{20J|t|}`,
> with `||[A, B]|| = 0` whenever `A` or `B` is even. Constants depend
> only on `||A||`, `||B||`, `n_X ≤ 6|X|`, `J`, `d` — not on `|Λ|`."

The walk combinatorics that fix `20J` (line 184):

> "the walk combinatorics (bonds per site `6`, bond-adjacency degree
> `10`, `|𝒲_k| ≤ n_X·10^{k−1}`, reach `k ≥ d`), the coefficient assembly
> `(2J)^k n_X 10^{k−1} = (n_X/10)(20J)^k`".

These constants (`6`, `10`, `20`) are **specific to the nearest-neighbor
bond set**; they are counts, not weighted sums. The `μ`-reweighted
exponential form and the `20eJ` readout carry over (lines 213-219).

**(c) Declared open tasks relevant to a many-body quasilocal-class LR
bound.** Non-Claims, lines 337-341:

> "Does **not** attempt the transfer-operator identification
> (Berezin/log-transfer) — the other half of the named bridge, still
> open."

plus sharp rate and the `U`-integrated statement (lines 342-343). The
note is also explicitly **background-free** and finite-range: the CAR
class is *supplied*, not derived, and the bonds are nearest-neighbor.

**(d) Does it supply / could it supply the spec's weighted hypothesis?**
Not as written (it is nearest-neighbor with uniform `J` and fixed
integer walk constants — no `e^{mu diam S}` weight). **But it supplies
the fermionic many-body *vehicle* the gauged bilinear route needs**, and
one structural fact makes it directly relevant: **a bilinear
`c_x^† c_y + h.c.` is an EVEN element** (two generators), so
long-range hopping/pairing terms built from a decaying kernel are exactly
"even Hermitian bond terms" — they fall under the graded locality lemma
already proved here. The motivation exhibit, lines 134-143, confirms the
lemma handles non-adjacent even bonds:

> "the even hop `h = c_1^† c_3 + c_3^† c_1` between JW-nonadjacent sites
> has JW image carrying `Z_2` ... Its CAR locality is nevertheless exact:
> it commutes with the odd site-2 generators `c_2, c_2^†` and with the
> even site-2 element `n_2` (gated) — precisely the graded lemma."

So the graded lemma is **already parity-correct for long-range even
bilinears**. What is missing to reach the spec's weighted hypothesis is
only the **walk combinatorics**: replace the nearest-neighbor
`bonds-per-site 6 / adjacency-degree 10 / (20J)` counting by a *weighted*
per-site activity `sup_x Σ_{b ∋ x} ||h_b|| e^{mu diam b}` and its walk
analog. `[SCOUT DERIVATION, medium-high confidence]` The graded lemma
(algebra side) transfers verbatim to long-range even bonds; only the
combinatorial/geometry side (the integer degrees) needs the weighted
re-derivation. That re-derivation is the fermionic instantiation of
block07.

---

## Central question (d): can the weighted hypothesis be supplied for a bilinear generator from a decaying kernel?

**Short answer: YES, and it is already done for the `U = 1` scalar case
(Note 3). The exact route and constants are below. What is genuinely
missing is the *assembly* into the family's walk-expansion form, plus the
gauged (Note 1 kernel) and fermionic-CAR (Note 5 algebra) upgrades.**

The spec's hypothesis is
`sup_x sum_{S containing x} ||h_S|| |S| e^{mu diam S} <= kappa`.

### The exact `Z^3` route with constants `[SCOUT DERIVATION]`

For a **bilinear** generator the only supports are singletons (onsite
density, `|S| = 1`, `diam = 0`) and pairs (`|S| = 2`, `diam S = ||x-y||`).
Write the decaying-kernel input as `||h_S|| <= K e^{-eta ||z||_inf}` for
the pair `S = {x, x+z}` — supplied exactly by **Note 3 (B1)** at `U = 1`
(`K = C_d(eta,m)/a_tau`, any `eta < arcsinh(m)`) or by **Note 1 (G5)** on
a fixed gauge background (`K = Const(m,d)`, `eta = gamma_CT`). Then the
per-site weighted sum at any site is, by translation invariance / uniform
bound,

```text
    kappa  <=  |h(0)|  +  2 K  Σ_{z != 0} e^{-eta ||z||_inf} e^{mu ||z||_metric}.
```

**Two exact readings depending on the metric fixed for `diam S`
(confidence: high — this is elementary shell counting):**

- **`l_inf` weight** (matches the kernel): threshold `mu < eta`; with
  `x := e^{-(eta - mu)} in (0,1)` and the exact `Z^3` `l_inf`-shell count
  `N_3(r) = (2r+1)^3 - (2r-1)^3 = 24 r^2 + 2` (`r >= 1`),

  ```text
      kappa  <=  |h(0)|  +  2 K [ 24 · x(1+x)/(1-x)^3  +  2 · x/(1-x) ].
  ```

- **`l1` weight** (matches Notes 2/4/5 and the `Z^3` graph metric):
  threshold `mu < eta/3` via `||z||_1 <= 3 ||z||_inf` (this is exactly
  Note 3's `d mu < eta` condition); same closed form with
  `x := e^{-(eta - 3 mu)}`.

Both are **rational in `x`** (finite combinations of
`Σ_{r>=1} r^2 x^r = x(1+x)/(1-x)^3` and `Σ_{r>=1} x^r = x/(1-x)`), so
`kappa` is exact / rational-parametrizable as the spec requires. The
`|S| = 2` factor of the spec appears as the literal `2` in front. This
**is** Note 3's `W_mu` shell sum
`Σ_{r>=0}[(2r+1)^d-(2r-1)^d] e^{-(eta - d mu)r}` (its (B1)),
re-summed in closed form and carrying the `|S|` factor — I claim no
originality for the sum, only for writing it against the spec's exact
weighted-norm predicate.

### Why the spec's PURE exponential is admissible here despite Note 2 (L1)

Note 2 (L1) proves the pure-exponential *reproducing/convolution*
constant `Σ_z e^{-mu d(x,z)} e^{-mu d(z,y)} / e^{-mu d(x,y)}` is unbounded
(`>= R+1`). **That obstruction does not bind the direct weighted-path
method.** `[SCOUT DERIVATION, medium-high confidence — reasoning below;
the leading O(1) walk constant must be pinned by a runner, not the decay
or the finiteness]` Along any chain of overlapping supports
`S_1, ..., S_k` from `x` to `y`, the triangle inequality gives
`d(x,y) <= Σ_i diam S_i`, hence
`Π_i e^{mu diam S_i} >= e^{mu d(x,y)}`, so
`Π_i ||h_{S_i}|| <= e^{-mu d(x,y)} Π_i (||h_{S_i}|| e^{mu diam S_i})`.
Summing over intermediate supports, each step contributes at most the
per-site weighted activity `kappa` (the `|S|` factor supplies the
branching/exit count), giving

```text
    ||[τ_t(A_x), B_y]||  <=  2 ||A_x|| ||B_y|| · e^{-mu d(x,y)} ·
                             Σ_{k >= d}  (c · kappa · |t|)^k / k!
```

with a convention-dependent O(1) `c` (Note 3 books `c = 2` giving its
`4 W_mu|t|` after a further factor; Note 5 books it into `20J`). The
decay factor `e^{-mu d(x,y)}` is pulled out *before* any convolution, so
the divergent ratio of (L1) is never formed. This is precisely why Note 3
(B2) is a landed pure-exponential bound — it uses this move (its Step 2,
quoted above). **The spec's pure-exponential `|S|`-weighted hypothesis is
therefore the RIGHT primitive for a walk-expansion block07; it is Note
2's reproducing-weight method, not the pure exponential itself, that
fails.** I flag this as the single most important disambiguation in the
packet.

### What is actually missing (precise)

Nothing in the *finiteness* or the *decay* is missing for the scalar
`U = 1` case — Note 3 has it. Missing are exactly:

1. **Family form.** Note 3's (B2) is the `(exp - 1)`/`4 W_mu|t|` Duhamel
   envelope, not the all-time volume-uniform walk-expansion form
   `Σ_{k>=d}(...)^k/k!` with `n_X <= 6|X|` reach discipline that the
   current family (Note 5) uses. Re-booking Note 3 into that form is
   mechanical but unwritten.
2. **Gauged kernel.** To go beyond `U = 1`, feed Note 1's (G5) kernel
   into the shell sum. Note 1 supplies the decay uniform in `U`; nobody
   has formed the second-quantized bilinear from `<x|h[U]|y>` or summed
   its weighted norm.
3. **Fermionic realization.** Note 3 uses commuting per-site modes (Note
   4 flags this: "A fermionic-anticommutation (Jordan-Wigner) realization
   ... is [not in scope]", lines 781-783). The CAR realization needs Note
   5's graded locality lemma — which already covers long-range even
   bilinears — but with the weighted (not nearest-neighbor) walk count.

---

## PROPOSED SPLIT

I propose the two blocks below, but the **overlap flags are large and I
lead with them** — for the `U = 1` scalar bilinear, both blocks are
*already proved* by Note 3, so the split is only defensible if each block
is scoped to its genuinely-new delta.

### block07 — weighted-norm quasilocal-class walk expansion (self-contained math)

**Would claim.** Abstract, algebra-generic: for a many-body Hamiltonian
`H = Σ_S h_S` on finite `Λ ⊂ Z^3` (qubit bond terms, or **even**-CAR bond
terms) whose support family satisfies the spec's weighted hypothesis
`sup_x Σ_{S ∋ x} ||h_S|| |S| e^{mu diam S} <= kappa` for some `mu > 0`,
an **all-time, volume-uniform** quasilocal LR bound holds, of the family
form `||[τ_t(A_x), B_y]|| <= ||[A,B]|| + 2||A||||B||·(prefactor)·
e^{-mu d(x,y)} Σ_{k>=d} (c·kappa·|t|)^k/k!`, with `c` an O(1) walk
constant and lightcone speed `v ~ c·kappa/mu`. Method: the *direct*
weighted-path booking (pull out `e^{-mu d}` first — evades Note 2 (L1)),
i.e. Note 4's Steps 4-5 chain-counting with `qW -> kappa`, in Note 5's
walk-expansion form.

**Sentences it would needle (as the named-open task it closes).**

- Note 4 (F5), lines 350-352: *"that one-step composition theorem is not
  proved here or in the cited note."* and C1, lines 700-702: *"The
  remaining missing step is exactly one hypothesis: non-perturbative
  finite-range/quasilocal control of `H = -log(T)/a_τ`."*
- Note 2 (L6)/closing, lines 380-381: *"A separate source would still be
  needed to prove exponential log-locality for a broader interacting
  transfer family from the framework premises."*
- Note 5 Non-Claims, lines 337-341 (its NN restriction and the still-open
  bridge) — block07's fermionic instantiation lifts NN to weighted
  long-range even bonds using Note 5's own graded lemma.

### block08 — identification: bilinear generator from a decaying kernel satisfies the weighted hypothesis

**Would claim.** For the bilinear generator
`H = Σ_{x,y} h(x-y) c_x^† c_y (+ h.c.)` (fermionic, even) or its
commuting-mode analog, built from a one-particle kernel with
`||h(z)|| <= K e^{-eta ||z||_inf}`, the block07 hypothesis holds with the
**exact `Z^3` shell-sum** `kappa` derived above
(`kappa <= |h(0)| + 2K[24 x(1+x)/(1-x)^3 + 2x/(1-x)]`), finite for all
`mu < eta` (`l_inf`) / `mu < eta/3` (`l1`). Instantiate `(K, eta)` from
the supplier: **Note 1 (G5)** for a fixed gauge background, **Note 3 (B1)**
for `U = 1`.

**Sentences it would needle.**

- Note 1 (G5), lines 154-162: *"`|| <x| h[U] |y> ||  <=  Const(m, d)
  e^{-gamma_CT ||x - y||_inf}`"* uniform in `U` and volume — the gauged
  decaying kernel block08 turns into `kappa`.
- Note 1 open task (iii), lines 314-316 (the "many-body ... Lieb-Robinson
  lightcone ... still a separate theorem"): block08+block07 is the
  fixed-background half of that composition.

### Overlap with existing notes (do they ALREADY prove parts? — quoted)

**YES, substantially. This is the load-bearing honesty flag for the
supervisor.**

- **Note 3 ALREADY proves block07 ∩ block08 for the `U = 1` scalar
  bilinear.** (B1), lines 81-92, is block08 (kernel -> finite weighted
  norm) and (B2), lines 96-99, is block07 (weighted norm -> LR bound):
  *"`W_mu := sup_x sum_y ||Phi_{xy}|| exp(mu d_1(x,y))`"* ... *"If
  `0 < d mu < eta < arcsinh(m)`, then `W_mu` is finite"* ... *"`||[alpha_t(A_x),
  B_y]|| <= 2 ||A_x|| ||B_y|| exp(-mu d_1(x,y) + 4 W_mu |t|)`"*. So a
  block07/block08 that does not *exclude* the `U = 1` scalar bilinear
  adds nothing over Note 3. The split is only new for: (gauged kernel) /
  (fermionic CAR realization) / (general `|S| > 2` support) / (the
  all-time volume-uniform *family form*).
- **Note 2 ALREADY proves a weighted-norm many-body LR bound** — (L3),
  lines 92-99 — in the *polynomial-corrected* weight `F_{mu,alpha}`.
  block07's delta over Note 2 is exactly (i) the **pure** exponential
  `|S|`-weight admitted via the direct method (Note 2 (L1) forbids it
  only for the reproducing method), and (ii) the all-time
  walk-expansion form. If block07 cannot articulate that delta crisply it
  risks being a cosmetic re-proof of Note 2.
- **Note 4 ALREADY proves the self-contained iterated-commutator lemma**
  block07 upgrades — (F3-L1), lines 266-268, and the chain-count
  `Σ_{chains, length k} ||h_{Z_1}||···||h_{Z_k}|| ≤ (|X|/q)(qW)^k` (lines
  552-555). block07 reuses this skeleton with `qW -> kappa`; it should
  cite Note 4 for the skeleton, not re-derive it.
- **Note 5 ALREADY proves the fermionic walk expansion + graded locality
  lemma** for nearest-neighbor even bonds — the graded lemma `A·B =
  (−1)^{p·q} B·A` (lines 118-125) already covers long-range even
  bilinears (its own motivation exhibit, lines 134-143). block07-fermionic
  reuses the graded lemma verbatim and re-derives only the *weighted*
  walk count in place of the integer degrees (`6`, `10`, `20J`).

**Net recommendation (scout opinion, not a directive).** Scope block08 to
the **gauged fixed-background** kernel (Note 1) — that is the clean,
non-overlapping new input, since `U = 1` is Note 3 (B1). Scope block07 to
the **weighted long-range even-CAR walk expansion in the family's
all-time volume-uniform form**, citing Note 4 (skeleton), Note 5 (graded
lemma + walk form), and Note 3 (the pure-exponential direct-path move) for
the parts already proved, and claiming only the weighted-long-range walk
count + the assembly as new. A block07 stated as a *generic* weighted LR
theorem would collide with Note 2 (L3) and Note 4 (F3-L1) and is likely to
draw a "cosmetic re-proof" objection.

---

## LIMITS

- **Read-only, five files only.** I did not open the cited upstream
  authorities (`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10`,
  the two `2026-07-18` sibling walk-expansion / nested-commutator notes,
  `MINIMAL_AXIOMS`, the hopping-bilinear note, RP notes). Anywhere I
  describe those (e.g. the sibling's `20J`/`20eJ` provenance, the exact-log
  kernel's sharpness) I am relaying Note 5/Note 3/Note 4's *quotes about
  them*, not the sources. The sharpness of `arcsinh(m)`, the value
  `W_H = 1.757278…`, and the sibling walk constants are asserted by these
  notes and not independently checked here.
- **My `[SCOUT DERIVATION]` arithmetic is sympy-spot-checked, not
  runner-gated.** I confirmed in a throwaway sympy session that the shell
  count `N_3(r) = (2r+1)^3-(2r-1)^3 = 24 r^2 + 2` and the closed form
  `Σ_{r>=1}(24r^2+2)x^r = 24 x(1+x)/(1-x)^3 + 2 x/(1-x)` are exact for
  `0 < x < 1` (symbolic difference `0`; numeric partial sum matches to
  machine precision at `x = 0.3`). That is a spot-check, not a committed
  runner; the *composed* `kappa` bound (with the `K`, `eta` supplier
  constants and the `|h(0)|` onsite term) should still be gated in a real
  runner before any note relies on it.
- **The evades-(L1) argument is a sketch, not a proof.** The claim that
  the direct weighted-path method admits the spec's pure-exponential
  `|S|`-weight is a reasoned route (and is *instantiated* by Note 3 (B2)
  for the bilinear case), but the exact O(1) walk constant `c`, the
  precise placement of the `|S|` factor (charge-on-entry vs
  charge-on-exit), and whether it survives *general* `|S| > 2` supports
  with the *same* constant are open bookkeeping I did not close. Treat
  "block07 works for general support families with the pure weight" as a
  conjecture pending a runner; only the **bilinear** case is
  note-backed.
- **Metric ambiguity is unresolved by the spec.** The finiteness
  threshold on `mu` differs by a factor of `d = 3` between the `l_inf`
  and `l1` readings of `diam S`. I reported both; a note must fix one.
- **Overlap risk is a judgement call.** My assessment that a generic
  block07 would "collide with Note 2/Note 4" is a scout opinion about
  reviewer reception, not a fact about the mathematics; the supervisor
  should weigh it.
- **No audit status asserted** for any of the five notes or for the
  proposed blocks, per the honesty bar. Several of the five carry
  `unaudited` / `audited_conditional` upstream provenance *in their own
  prose* (e.g. Note 1 lines 316-319); I neither confirm nor set those.
- **Not verified against `KEY_TERMINOLOGY.md` or the ledger** (out of the
  five-file scope): term usage (`quasilocal`, `support family`, `even`)
  is taken as each note defines it locally.


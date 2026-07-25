# Worker B11 math analysis — torus shells, d=3 assembly, envelope feed

> **SUPERSEDED SCAFFOLDING — historical record only.** This file was
> written before (a) the owner landed the rewritten blocks 03-10 on
> `origin/main` and (b) the review rounds that forced the alias lemma
> and the claim narrowing. Its quotations of "block10" are from the
> PRE-REWRITE stack drafts and do NOT appear in the landed
> corner-note; its "action-derived", "full-lane closure", "SAME
> constants", and "supplies both prerequisites" framings are all
> contradicted by the landed note. Read the landed note and
> `REVIEW_HISTORY_B11.md` for the actual claim boundary.

Self-contained execution of `worker_b11_math_spec.md`. Exact arithmetic; every step shown.
Brute-force / sympy cross-checks were run for all integer counts, the generating-function
coefficients, the envelope geometric sum, and the arcsinh closed forms (all pass; see items).

## Setup taken as GIVEN (per spec — not re-derived here)
- Weighted quasilocal class with activity
  `kappa = sup_x sum_{S ni x} ||h_S|| |S| e^{mu diam(S)}`, `diam` in the A graph metric.
- Chain lemma (sum of sub-diams >= d(X,Y)) and peeling (chain sums <= n_X^w kappa^{k-1})
  hold for ANY finite graph metric. **USED, not proven** (supervisor verifies separately).
- CT-style kernel bound `||k_xy|| <= K e^{-eta ||x-y||_inf}` on Z^3.
- Block08 feed on Z^3: `kappa <= K + 8K x(13+10x+x^2)/(1-x)^3`, `x = e^{-(eta-3mu)}`,
  via l_inf shells `24r^2+2` and `||z||_1 <= 3||z||_inf`.

## Notation and the torus metric
For `a in Z/L` write the **cycle (circular) distance**
```
|a|_L := min( a mod L , L - (a mod L) )   in {0,1,...,floor(L/2)}.
```
The torus `(Z/L)^d` with nearest-neighbour edges (one coordinate changes by +-1) is exactly the
Cartesian graph product of d cycles `C_L = C_L box C_L box ... box C_L`. For a Cartesian product
`d_{GboxH}((g,h),(g',h')) = d_G(g,g') + d_H(h,h')`, and `d_{C_L}(0,a) = |a|_L`. Hence the torus
graph (word) metric and its l_inf companion are
```
d^1_torus(0,z)   = sum_{mu=1}^d |z_mu|_L      (l^1 / word / A-graph metric)
d^inf_torus(0,z) = max_{mu=1}^d |z_mu|_L      (l^inf).
```
These two facts (product-metric decomposition; per-cycle distance `|a|_L`) are the only structural
inputs to items 1-4.

---

## Item 1 — Torus l^1 shell domination

**Claim.** For all `r >= 0`, `L >= 1`, `d >= 1`:
```
S^1_tor(r) := #{ z in (Z/L)^d : d^1_torus(0,z) = r }
           <= #{ w in Z^d   : ||w||_1 = r }  =: S^1_Z(r).
```

**Proof (explicit radius-preserving injection / minimal lift).**
Define `phi : (Z/L)^d -> Z^d` coordinatewise, sending each residue `z_mu in {0,...,L-1}` to its
minimal-absolute-value integer representative:
```
phi(z)_mu = z_mu        if z_mu <= floor(L/2)
          = z_mu - L    if z_mu >  floor(L/2).
```
(1) **Radius preserved.** The minimal representative realises the cycle distance, so
`|phi(z)_mu| = |z_mu|_L` for every mu. Summing,
```
||phi(z)||_1 = sum_mu |phi(z)_mu| = sum_mu |z_mu|_L = d^1_torus(0,z).
```
Thus phi carries the torus r-shell INTO the Z^d r-shell.
(2) **Injective.** Reduction mod L, `pi : Z^d -> (Z/L)^d`, satisfies `pi(phi(z)) = z`
(because `phi(z)_mu ≡ z_mu (mod L)`). A map with a left inverse is injective.
Hence the torus r-shell injects into the Z^d r-shell, giving `S^1_tor(r) <= S^1_Z(r)`.  ∎

**Covering reading.** `pi : Z^d -> (Z/L)^d` is a covering of Cayley graphs (local iso for the
generators +-e_mu), hence 1-Lipschitz and path-lifting; `phi` is the minimal-length lift of each
shell point. Distances can only shrink downstairs, which is exactly `|a|_L <= |a|` coordinatewise.

### Exact counts on (Z/6)^3

Per-coordinate profile for L = 6: `|a|_6` for `a = 0,1,2,3,4,5` is `0,1,2,3,2,1`, so the
degeneracies `n_6(k) = #{a : |a|_6 = k}` are
```
n_6(0)=1, n_6(1)=2, n_6(2)=2, n_6(3)=1   (and 0 for k>=4).
```
The torus l^1 shell sizes are the coefficients of the cube of the one-coordinate shell polynomial
```
p(q) = sum_k n_6(k) q^k = 1 + 2q + 2q^2 + q^3 = (1+q)(1+q+q^2).
```
`p(q)^2` coefficients (c_0..c_6): compute `c_k = sum_{i+j=k} p_i p_j`, `p=(1,2,2,1)`:
```
c_0 = 1
c_1 = 1*2 + 2*1                       = 4
c_2 = 1*2 + 2*2 + 2*1                 = 8
c_3 = 1*1 + 2*2 + 2*2 + 1*1           = 10
c_4 = 2*1 + 2*2 + 1*2                 = 8
c_5 = 2*1 + 1*2                       = 4
c_6 = 1*1                             = 1     (sum = 36 = 6^2 check)
```
`p(q)^3 = p^2 * p`, coefficient `d_r = sum_{j=0}^3 c_{r-j} p_j`:
```
d_0 = c_0 p_0                                     = 1*1                       = 1
d_1 = c_1 p_0 + c_0 p_1                            = 4*1 + 1*2                 = 6
d_2 = c_2 p_0 + c_1 p_1 + c_0 p_2                  = 8*1 + 4*2 + 1*2           = 18
d_3 = c_3 p_0 + c_2 p_1 + c_1 p_2 + c_0 p_3        = 10*1 + 8*2 + 4*2 + 1*1    = 35
```
(Full spectrum `d = 1,6,18,35,48,48,35,18,6,1`, palindromic, sums to `216 = 6^3` — checked.)

| r | torus (Z/6)^3 = d_r | Z^3 = 4r^2+2 | equal? |
|---|--------------------|--------------|--------|
| 1 | 6                  | 6            | YES    |
| 2 | 18                 | 18           | YES    |
| 3 | 35                 | 38           | NO (deficit 3) |

**Where the deficit comes from (r = 3 on L = 6).** Sort Z^3 shell r=3 (38 pts) by coordinate type:
```
(3,0,0): 3 positions x 2 signs = 6
(2,1,0): 3! arrangements x 2^2 signs on the two nonzeros = 6*4 = 24
(1,1,1): 1 arrangement x 2^3 signs = 8            total 6+24+8 = 38.
```
On (Z/6)^3 the value 3 is antipodal-self-identified (`+3 ≡ -3 mod 6`), while 1,2 are not
(`1≠5`, `2≠4 mod 6`). So the `(3,0,0)` sign pairs COLLAPSE: 6 -> 3 torus points. The
`(2,1,0)` (24) and `(1,1,1)` (8) survive distinct. Torus total `3 + 24 + 8 = 35`, deficit
`38 - 35 = 3`, exactly the collapsed antipodal axis pairs.

**Equality range.** The lift `phi` is always injective; equality `S^1_tor(r) = S^1_Z(r)` holds iff
`pi` is ALSO injective and norm-preserving on the Z^3 r-shell. If `r < L/2`: any `w` with
`||w||_1 = r` has each `|w_mu| <= r < L/2`, so `|w_mu|_L = |w_mu|` (no wrap shortening); and two
shell points colliding mod L would differ by a nonzero multiple of L in some coordinate, impossible
since `|w_mu - w'_mu| <= 2r < L`. Hence
```
equality for all r < L/2 ; first break at r = floor(L/2) (antipodal self-pairing at exactly L/2).
```
For L = 6: `L/2 = 3`, so equality at `r = 1,2` and the first strict drop at `r = 3`. Matches the table.

---

## Item 2 — Torus l^inf shell domination vs 24r^2 + 2

**Z^3 baseline.** The l^inf sphere count is
`#{z in Z^3 : ||z||_inf = r} = (2r+1)^3 - (2r-1)^3`. Expand:
```
(2r+1)^3 = 8r^3 + 12r^2 + 6r + 1
(2r-1)^3 = 8r^3 - 12r^2 + 6r - 1
difference = 24r^2 + 2.
```
So `24r^2+2` gives r=1,2,3 -> 26, 98, 218.

**Domination.** The same minimal lift `phi` (item 1) preserves the l^inf radius, since
`max_mu |phi(z)_mu| = max_mu |z_mu|_L = d^inf_torus(0,z)`, and is injective. Hence
```
#{ z in (Z/L)^d : d^inf_torus(0,z) = r }  <=  #{ z in Z^d : ||z||_inf = r } = 24r^2+2  (d=3).
```

**Exact counts.** With cumulative degeneracy `N_L(<=r) = #{ a in Z/L : |a|_L <= r }`, the l^inf
shell is `N_L(<=r)^3 - N_L(<=r-1)^3`.

L = 6: `|a|_6 = 0,1,2,3,2,1` gives `N_6(<=0)=1, N_6(<=1)=3, N_6(<=2)=5, N_6(<=3)=6`:
```
r=1: 3^3 - 1^3 = 27 - 1  = 26
r=2: 5^3 - 3^3 = 125 - 27 = 98
r=3: 6^3 - 5^3 = 216 - 125 = 91
(sum 1+26+98+91 = 216 = 6^3 check)
```
L = 8: `|a|_8 = 0,1,2,3,4,3,2,1` gives `N_8(<=0)=1, N_8(<=1)=3, N_8(<=2)=5, N_8(<=3)=7, N_8(<=4)=8`:
```
r=1: 3^3 - 1^3 = 26
r=2: 5^3 - 3^3 = 98
r=3: 7^3 - 5^3 = 343 - 125 = 218
(next r=4: 8^3-7^3 = 169; sum 1+26+98+218+169 = 512 = 8^3 check)
```

| r | (Z/6)^3 l^inf | (Z/8)^3 l^inf | Z^3 = 24r^2+2 |
|---|---------------|---------------|---------------|
| 1 | 26            | 26            | 26            |
| 2 | 98            | 98            | 98            |
| 3 | 91  (< 218)   | 218 (= 218)   | 218           |

Same threshold as item 1: l^inf equality holds for `r < L/2`. On (Z/8)^3, `r=3 < 4 = L/2`, so all
three shells equal `24r^2+2`; the first break is at `r = 4` (169 < 386). On (Z/6)^3, `r=3 = L/2`
already breaks (91 < 218). In all cases the domination `torus l^inf shell <= 24r^2+2` holds — this
is exactly what the block08 kernel feed needs.

---

## Item 3 — Metric conversion on the torus: d^1_torus <= 3 d^inf_torus

**Holds, exactly, with the same constant 3 = d.** Both torus metrics are built from the SAME
per-coordinate nonnegative reals `|z_mu|_L`:
```
d^1_torus(0,z)   = sum_{mu=1}^3 |z_mu|_L
d^inf_torus(0,z) = max_{mu=1}^3 |z_mu|_L.
```
For any 3 nonnegative numbers, `sum <= 3 * max`. Applying it to `(|z_1|_L, |z_2|_L, |z_3|_L)`:
```
d^1_torus(0,z) = |z_1|_L + |z_2|_L + |z_3|_L  <=  3 * max_mu |z_mu|_L = 3 d^inf_torus(0,z).   QED
```
No lift is needed — the inequality is the universal `l^1 <= d * l^inf` among d nonnegative reals,
and the torus l^1/l^inf metrics ARE the l^1/l^inf norms of the vector of cycle distances. This is
why the inequality is "quotient-stable": each `|z_mu|_L` is a bona-fide metric on the cycle `C_L`,
and the sum-vs-max relation is indifferent to what those d nonnegative numbers mean. The reverse
`d^inf_torus <= d^1_torus` (max <= sum) also holds, so the two torus metrics are equivalent with the
identical constants (1 and 3=d) as on Z^3. Translation-invariance of the torus makes both statements
basepoint-free: `d^*_torus(x,y) = d^*_torus(0, y-x)`.

**Refutation check (none needed).** The only way this could fail is if wrapping made some `|z_mu|_L`
NEGATIVE or made the max/sum decomposition break — neither happens; `|z_mu|_L in [0, floor(L/2)]`
is always a genuine nonnegative distance. So the inequality is not merely inherited "up to error":
it is exact on the torus.

---

## Item 4 — Consequence: block08 envelope is a valid upper bound on the torus, same constants

**Geometric-sum lemma (verified by series to order 12 + numerics).**
```
sum_{r>=1} (24 r^2 + 2) x^r
   = 24 * x(1+x)/(1-x)^3  +  2 * x/(1-x)                    [sum r^2 x^r = x(1+x)/(1-x)^3 ; sum x^r = x/(1-x)]
   = [ 24 x(1+x) + 2x(1-x)^2 ] / (1-x)^3
   = [ (24x + 24x^2) + (2x - 4x^2 + 2x^3) ] / (1-x)^3
   = [ 26x + 20x^2 + 2x^3 ] / (1-x)^3
   = 2x(13 + 10x + x^2) / (1-x)^3.        (valid for 0 <= x < 1)
```

**Exact chain of inequalities.** Fix a base site `x` on (Z/L)^3 (any L). For the two-body CT kernel,
the S ∋ x terms are the on-site singleton `{x}` and the kernel bonds `{x,y}`, y≠x, with
`||h_{{x,y}}|| = ||k_xy||`, `|S| = 2`, `diam_torus({x,y}) = d^1_torus(x,y)`:
```
kappa_torus(x)
 = ||h_{{x}}|| * 1 * e^{mu*0}  +  sum_{y!=x} ||k_xy|| * 2 * e^{mu d^1_torus(x,y)}
 <= K                          +  2K sum_{y!=x} e^{-eta d^inf_torus(x,y)} * e^{mu d^1_torus(x,y)}   [CT bound; ||h_{x}||<=K]
 <= K + 2K sum_{y!=x} e^{-eta d^inf_torus(x,y)} * e^{3 mu d^inf_torus(x,y)}                          [Item 3: d^1 <= 3 d^inf]
 =  K + 2K sum_{r>=1} #{y : d^inf_torus(x,y) = r} * x^r                    [group by r; x = e^{-(eta-3mu)}]
 <= K + 2K sum_{r>=1} (24 r^2 + 2) x^r                                     [Item 2: torus l^inf shell <= 24r^2+2]
 =  K + 2K * 2x(13+10x+x^2)/(1-x)^3                                        [lemma]
 =  K + 4K x(13+10x+x^2)/(1-x)^3
 <= K + 8K x(13+10x+x^2)/(1-x)^3.                                         [block08 given envelope; 4K <= 8K]
```
The last line is exactly the block08 feed. Every constant is IDENTICAL to Z^3: same `K`, `eta`,
`mu`, hence the same `x = e^{-(eta-3mu)}`; convergence needs the same condition `x < 1`, i.e.
`eta > 3mu = d*mu`. The bound is uniform in the base site `x` (torus is translation invariant) and
uniform in `L` (no `L` appears on the right). Therefore

> **The block08 envelope `kappa <= K + 8K x(13+10x+x^2)/(1-x)^3` remains a valid upper bound on the
> torus (Z/L)^3 with the SAME constants, for every L, via shell domination (Item 2) + metric
> conversion (Item 3) + the CT bound.**

**Bookkeeping flag.** My independent reconstruction lands the tighter `K + 4K x(...)/(1-x)^3`
(per-bond weight `||k_xy|| * |S| = 2K`). The block08 value has `8K`; the factor-2 gap is a `|S|` /
Hermitian-symmetrization convention in the block08 derivation (`k_xy` and `k_yx`, or a doubled bond
count). Since `4K <= 8K` term by term, the given `8K` envelope is a valid (looser) torus bound
regardless — nothing in this item breaks — but the supervisor should reconcile the prefactor against
the block08 note so the constant is not silently mismatched between blocks.

---

## Item 5 — d = 3 per-mode assembly and the discharge chain

Per-reduced-mode kernel and dispersion:
```
t_3(p) = e^{-2 E_3(p)} ,   E_3(p) = arcsinh( sqrt( m^2 + sum_{mu=1}^3 sin^2 p_mu ) ),   p = (p_1,p_2,p_3).
```

**(a) E_3 >= arcsinh(m) > 0 for m > 0 (monotonicity).**
`sum_{mu=1}^3 sin^2 p_mu >= 0`, so the radicand `m^2 + sum sin^2 p_mu >= m^2`, giving
`sqrt(...) >= m`. `arcsinh` is strictly increasing on [0,inf) because
`d/du arcsinh(u) = 1/sqrt(1+u^2) > 0`. Monotonicity applied to `sqrt(...) >= m >= 0`:
```
E_3(p) = arcsinh( sqrt(m^2 + sum sin^2 p_mu) )  >=  arcsinh(m).
```
And `arcsinh(m) = ln(m + sqrt(m^2+1)) > ln(1) = 0` for `m > 0` (since `m + sqrt(m^2+1) > 1`).
Hence `E_3(p) >= arcsinh(m) > 0`.  (Also `arcsinh(0) = 0`, so positivity is strict exactly for m>0.)

**(b) 0 < t_3 <= e^{-2 arcsinh(m)} < 1, with an exact upper value.**
From (a), `-2 E_3(p) <= -2 arcsinh(m) < 0`, and `exp` is positive and increasing:
```
0 < t_3(p) = e^{-2 E_3(p)} <= e^{-2 arcsinh(m)} < e^0 = 1.
```
Exact closed form (verified symbolically and numerically):
```
e^{arcsinh(m)} = m + sqrt(m^2+1)   =>   e^{-2 arcsinh(m)} = (m + sqrt(m^2+1))^{-2} = (sqrt(m^2+1) - m)^2,
```
using `(sqrt(m^2+1) - m)(sqrt(m^2+1) + m) = 1`. For `m > 0`, `(sqrt(m^2+1) - m)^2 in (0,1)`.
Numeric spot values: m=0.5 -> 0.381966..., m=1 -> 0.171573..., m=2 -> 0.055728... (all in (0,1)).

**Per-mode spectral band (d = 3).** Since `0 <= sum_{mu=1}^3 sin^2 p_mu <= 3`,
```
arcsinh(m) <= E_3(p) <= arcsinh( sqrt(m^2+3) ),
(sqrt(m^2+4) - sqrt(m^2+3))^2  <=  t_3(p)  <=  (sqrt(m^2+1) - m)^2   ⊂ (0,1).
```
So `t_3` is a bounded, strictly-positive, strictly-sub-unital multiplication operator in mode space:
its spectrum sits in a compact subinterval of `(0,1)`. This makes `log t_3` bounded and self-adjoint,
so every operator log below is well defined.

**(c) The discharge chain (second quantization).**
Let `Gamma(.)` be the Segal second-quantization functor on Fock space and `dGamma(.)` its generator.
Standard functorial identities (free / quasi-free sector):
```
(F1)  Gamma(e^{-B}) = e^{-dGamma(B)}          =>   -log Gamma(t) = dGamma(-log t)   for positive t,
(F2)  dGamma(c B) = c dGamma(B)               (linearity in the one-particle operator).
```
Write the one-particle Hamiltonian `h_3 := E_3` and the temporal spacing `a_tau`, so that
`t_3 = e^{-2 a_tau E_3}` (at `a_tau = 1` this is the given `e^{-2 E_3}`, and `-log t_3 = 2 E_3`).
Then:
```
-log Gamma(t_3)
   = dGamma( -log t_3 )                 [ (F1), t_3 a positive contraction with spectrum ⊂ (0,1) ]
   = dGamma( 2 a_tau E_3 )              [ -log t_3 = -log e^{-2 a_tau E_3} = 2 a_tau E_3 ]
   = 2 a_tau dGamma( E_3 )              [ (F2), pull scalar 2 a_tau out ]
   = 2 a_tau dGamma( h_3 ).             [ h_3 := E_3 ]
```
At `a_tau = 1`: `-log Gamma(t_3) = dGamma(-log t_3) = 2 dGamma(h_3)`, with `-log t_3 = 2 E_3`.
This is precisely the spec's chain `-log Gamma(t_3) = dGamma(-log t_3) = 2 a_tau dGamma(h_3)`.

**Factor tracking / d-dependence — FLAG: NONE.**
The two prefactors are:
- the `2` in `t = e^{-2E}` — the reflection/transfer doubling constant, identical to the 1d case;
- the `a_tau` — the temporal lattice spacing.
Neither depends on the spatial dimension d. The dimension enters ONLY through
`E_d = arcsinh( sqrt(m^2 + sum_{mu=1}^d sin^2 p_mu) )`, i.e. purely inside the ARGUMENT `h_d = E_d`
of `dGamma`, via the number of spatial sine terms (d of them). The scalar `2 a_tau` multiplying
`dGamma(h_d)` is the SAME in d=3 as in d=1. So the discharge factorizes identically across
dimension; d=3 is the d=1 chain with `h_1 = E_1` replaced by `h_3 = E_3`. No d-dependent factor
appears — confirming the "there should be none" expectation.

---

## Item 6 — Wrap-term status in the torus graph metric

**The wrap bond has diam 1, not L-1.** In the torus Cayley graph, the seam edge closing each cycle
(the nearest-neighbour bond between the residues `L-1` and `0` in one coordinate) is a genuine graph
edge. Its endpoints therefore sit at graph distance
```
d^1_torus(seam endpoints) = |(L-1) - 0|_L = |L-1|_L = min(L-1, 1) = 1.
```
A two-site term supported on that bond has `diam_torus = 1`, contributing
`||h_wrap|| * 2 * e^{mu * 1}` — a bounded, L-independent weight, identical to any other
nearest-neighbour bond.

**Contrast with block10.** The b10 exhibit measured the wrap term in the AMBIENT metric of an OPEN
embedding of the ring into Z (a line), where the two seam sites are at ambient distance `L-1`. That
gives weight `e^{mu(L-1)} -> infinity` as `L -> infinity`, which is why b10 had to impose the
open-boundary restriction (drop / forbid the wrap bond) to keep `kappa` finite and uniform. The blow-up
was an artifact of using the line metric on a periodic term, NOT an intrinsic feature of the periodic
system.

**What changes exactly (torus metric adopted).**
1. `diam(S)` is computed with `d^1_torus` (sum of cycle distances) instead of the ambient
   open-embedding `||x-y||_1`. Coordinatewise `|a|_L <= |a|`, so EVERY diam can only shrink or stay
   equal; in particular the wrap bond drops from `L-1` to `1`. Hence `kappa_torus <= kappa_ambient`
   term by term.
2. With the wrap bond now weight `e^{mu} `, no term diverges in `L`; the block10 open-boundary
   restriction is **no longer needed**. Periodic (torus) systems lie in the weighted quasilocal class
   with the SAME uniform `kappa` bound (Item 4).
3. The chain lemma + peeling are given to hold for ANY finite graph metric, so they apply verbatim to
   `d^1_torus`; the entire block07 LR/quasilocality machinery transfers to the torus with no new input.

**1d wrap blow-up — resolved too.** The b10 1d blow-up was the same phenomenon: a periodic bond scored
`L-1` because the ambient line metric was used. In the intrinsic cycle metric `d_{C_L}`, that bond has
`|L-1|_{C_L} = 1`, so the weight is `e^{mu}`, bounded uniformly in L. Thus switching to the intrinsic
torus/cycle metric removes the 1d wrap blow-up as well — the same one-line fix (`|a|_L <= |a|`, seam
distance = 1) does both d = 1 and d = 3.

**Interpretation caveat (FLAG).** In the torus metric the LR lightcone WRAPS: the maximal distance is
the torus diameter `d * floor(L/2)` (here `3 floor(L/2)`), and once the causal cone circumnavigates,
the distance-based bound saturates. This is physically correct (information may travel the short way
around the ring) and does not affect the uniform-in-L `kappa` bound; only the large-scale
interpretation of "distance" changes.

---

## Item 7 — LIMITS (assumed vs. must-be-independently-verified)

**Assumed / imported (used, not proven here):**
- **Metric-agnostic chain lemma + peeling.** Given by spec to hold for any finite graph metric; I
  apply them to `d^1_torus`. This is the single largest external reliance for items 4 and 6: if the
  peeling bound `chain sums <= n_X^w kappa^{k-1}` secretly used a property special to the Z^d metric
  (e.g. unbounded balls, or a specific isoperimetry), the torus transfer would need re-checking.
  **Supervisor must independently verify** the peeling/chain lemma is genuinely metric-agnostic (holds
  for the finite torus graph). The torus is finite, so balls saturate at the diameter — confirm the
  lemma statement tolerates that.
- **L-uniform finite-volume CT (Combes-Thomas) bound.** Item 4 assumes
  `||k_xy|| <= K e^{-eta d^inf_torus(x,y)}` holds ON the torus with the SAME `K, eta`, uniformly in L.
  On a finite periodic volume the CT resolvent estimate must be re-derived for the finite-volume
  kernel; it is standard that it transfers with L-independent constants for a gapped/decaying kernel,
  but this is an analytic input, **not proven here**. **Supervisor must verify the finite-volume CT
  bound is uniform in L** (the whole "same constants" claim rests on it).
- **Quasi-free assembly for the Gamma identity.** Item 5 uses `Gamma(e^{-B}) = e^{-dGamma(B)}`, valid
  when the many-body dynamics is the second quantization of the one-particle `t_3` (free / Gaussian /
  quasi-free sector, no genuine interaction). **Supervisor must confirm** the block's reduced-mode
  dynamics is quasi-free at this stage; a genuine interaction term would break `Gamma`-multiplicativity
  and the clean `-log Gamma = dGamma(-log)` discharge.
- **Convergence condition `eta > 3mu = d*mu`** (so `x < 1`), the same as the Z^3 feed. Assumed.
- **`a_tau = 1` normalization.** The chain was kept at general `a_tau` to expose the `2 a_tau` factor;
  the spec's `t_3 = e^{-2 E_3}` fixes `a_tau = 1`. No hidden d-dependence in `a_tau` or the `2`.

**Established here without further reliance (unconditional):**
- Items 1, 2 (torus l^1 and l^inf shell domination and the exact counts) are pure finite counting —
  brute-force confirmed. No dependence on the metric-agnostic peeling claim.
- Item 3 (`d^1_torus <= 3 d^inf_torus`) is the exact universal `l^1 <= d l^inf` inequality among the d
  nonnegative cycle distances; unconditional.
- The equality thresholds (`r < L/2`) and the first-break locations (r=3 for L=6; r=4 for L=8) are exact.

**Flags raised (for the supervisor):**
1. Block08 prefactor `8K` vs my reconstructed `4K` (Item 4) — a `|S|`/Hermitian-symmetrization
   convention gap; harmless for validity (`4K <= 8K`) but reconcile the constant across blocks.
2. The torus LR lightcone wraps; distance saturates at torus diameter `3 floor(L/2)` (Item 6
   interpretation caveat) — expected, but state it so the cone picture is not mis-read at large L.
3. All "same constants on the torus" claims are contingent on the L-uniform finite-volume CT bound
   (above) — the load-bearing analytic assumption.

**Torus sphere counts computed (headline numbers):**
```
l^1   (Z/6)^3  r=1,2,3 :  6, 18, 35     (vs Z^3  6, 18, 38 ; equal at r=1,2, break at r=3=L/2)
l^inf (Z/6)^3  r=1,2,3 : 26, 98, 91     (vs Z^3 24r^2+2 = 26, 98, 218 ; break at r=3=L/2)
l^inf (Z/8)^3  r=1,2,3 : 26, 98, 218    (= 24r^2+2 for all three ; break deferred to r=4=L/2)
```

END OF ANALYSIS.

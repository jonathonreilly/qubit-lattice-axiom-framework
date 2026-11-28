# Repo search

The lead's `prior/repo-search-2026-11-08.md` records a search of main and
PRs 10114, 10133, 10134 and 10141. Its targets are earlier RG interfaces,
not row 978's hypercontractive iteration. Its “R2” is healed restriction,
not the size claim checked here. No matching prior proof follows from it.
I fetched PR 10114 and read its nearest transfer-operator hit,
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–169`,
at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
It proves a positive one-step plaquette correlation and expressly makes
no gap lower bound. It supplies neither IHC nor a thermal-trace seed.
The lead's digest reports that this blob is identical on PR 10133;
that duplicate was not re-read. Main was fetched at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9` for its current rules.
No task-specific “Repo prior work” entry accompanies row 978.
The target-specific `prior/gap-ladder-check-astra.md` is absent at
`58524f2940d52f9220856742550df299c6c1d287`.

FINISH row 981 records a same-provider check of row 978. Its result was
visible during queue lookup. This requested cross-provider check used
the mathematical source, not that verdict as evidence. A same-provider
check does not complete the requested cross-provider task. The open registry
search found no owner for this check or the named IHC/CU statements.

Provenance: Codex, OpenAI, this session's configured model and effort;
2026-11-15; pinned source `58524f294`. Research text, not an audit.
This file grants no scientific or audit status. No numerical proof is used.

## Checkpoint

1. Read row 978's statements and the exact definitions they consume.
2. Check Lemma IHC and section 5.6(a) by written kernel identities.
3. Read the index, then the account passages for the torus bound (TH).
4. Check Corollary CU, its physical units and its quantifiers.
5. Check section 5.7 and claim (R2) by hand.
6. Record a verdict per statement and one final RESULT line.

Downloaded once, into a newly created empty directory:
`/tmp/sa-gap-ladder-check-astra.SIW0J8/sa_ym4.tex` and `sa_ca_I.tex`,
both at upstream revision `31a47c543775`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for all account and outline inputs used below.

Completed: the requested statements and their named interfaces are checked
below. No proof attack on HC-phys or the determinant comparison was made.

## 1. Lemma IHC: HOLDS

Source: `gap-ladder-max.md:117–128`; definitions checked against
`gap-direction-max.md:262–277,305–320`. Use the gauge-projected transfer
kernel, or equivalently the kernel on the quotient slice space. The trace
in (5.3) is the gauge-invariant trace. The unprojected temporal-gauge kernel
would not have the asserted invariance in its second argument.

Here is the calculation, with all four proof steps checked. Set
`q = 1 + exp(-2 alpha m)` and `A(u) = integral p_s(u,v)^2 nu(dv)`.
Symmetry and composition give
`p_(s+m)(u,.) = P^m p_s(u,.)`. For a probability density `g`, Hölder gives

```math
\int g^q\,d\nu
\le (\int g\,d\nu)^{2-q}(\int g^2\,d\nu)^{q-1},
\qquad
\|g\|_q^2\le(\int g^2\,d\nu)^{2(q-1)/q}.
```

Thus the assumed hypercontractive inequality bounds the new squared norm
by `A(u)^theta`, with `theta = 2(q-1)/q`. Integrating and using concavity
gives `Tr P^(2s+2m) <= (Tr P^(2s))^theta`. These traces are finite for
`s >= 1`; their logarithms give exactly (IHC). For `m = 0` it is equality.
The identity and exponential upper bound for `theta` are correct.
First failing step in the lemma: none.

The three remarks at lines 131–133 also hold. In particular,
`integral p_1(u,v)^2 nu(dv) <= sup p_1`, and
`S(t) >= exp(-E_1 t)` proves the stated necessity of the rate.

**Line 134, the sharpness remark: HOLDS AFTER CORRECTION.**
“At most” must be “at least”, with equality approached as the starting
time tends to infinity. In the notation of line 97, convexity of
`F(x) = -log(1-x)` gives `F(xy) <= y F(x)`.
Hence `theta F(x)/F(xy) >= 2/(1+y)`.
A hand counterexample to “at most” is `x = y = 1/2`:
the claimed upper bound would imply `log 2 <= 2 log(4/3)`, or `2 <= 16/9`.
This does not affect IHC.

## 2. Section 5.6(a): HOLDS

Source: `gap-ladder-max.md:182–186`. Only the functions `p_s(u,.)` enter
the argument above. The hypothesis for almost every `u` and every integer
`m >= 0` suffices; countability gives one full-measure set if needed.
No inequality for arbitrary slice functions is used. This establishes the
weaker trajectory implication, without asserting cutoff-uniform smoothing
from the informal sentence about lattice roughness.

## 3. Abstract Corollary CU: HOLDS AFTER CORRECTION

Source: `gap-ladder-max.md:139–152`. Require `t_0 >= 2`, even, and
`n >= 3`. Write `epsilon = a_iota` and `ell_iota = n epsilon`.
Then `m = floor(n/2) - t_0/2 >= 0`, and the exact estimate is

```math
X_\iota(n;B)
\le 2\Theta\exp[-M_H\epsilon(2\lfloor n/2\rfloor-t_0)]
\le 2\Theta\exp[-M_H(\ell-\tau_0-\epsilon)].
```

It proves the stated seed when `0 < s_* < 1/5041` and SIZE-phys holds
for every member of the family. The length bound is `ell_* = ell` without
rounding, or `ell + sup_iota epsilon` with upward rounding. For a sequence
with `epsilon -> 0`, these side and time restrictions hold on its tail.

The separate two-sided-stability implication at line 150 is correct:
divide its lower bound by `t`, let `t -> infinity`, and obtain
`log lambda_0 >= e_iota |B| - c_F |B| (epsilon/a_*)^4`.
Subtract this from the upper bound at `t_0`. The result is
`X(t_0) <= 2 c_F |B| t_0 (epsilon/a_*)^4`.
It is at most `16 c_F ell_iota^3 tau_0/a_*^4`.
With upward rounding, use `ell_iota <= ell + sup epsilon`; line 150's
unrounded value of Theta is otherwise too small.

Finally, “for every large ell” needs a rate that stays bounded below as
`ell` varies, and fixed `tau_0` with polynomially bounded `Theta(ell)`.
Uniformity in the cutoff on each single box does not imply that
uniformity in box size. The valid fixed-box statement is SIZE-phys itself.

## 4. (TH) from the account: HOLDS AFTER CORRECTION

The index was used before the source: `sa-index/chunk-02.md:96–104`
for the transfer trace, `chunk-22.md:18–33` for ST5, and
`obligations.md:129,1221,1500` for the normalization obligations.
The complete-account index, `ca-full/index.tsv:1132–1140`, locates
`8.22:lem-vacuum-energy-density` and its neighbouring statements.
Sources read at `31a47c543775`: outline 2313–2335 and 23767–23797;
CA-II 140880–140940 and 141276–141539. CA-II was downloaded once into
the same new scratch directory because the two assumptions are in Part II.
These inputs are Sussman and Alpoge's, with Claude and Codex as authors
of their text; the normalization construction is credited there to Balaban.

**Assumption (a), literally identifying the two vacuum numbers: FAILS.**
CA-II 140880–140888 defines the unnormalized Wilson partition function
with normalized Haar measure. At 140918–140924 it defines the full
constant, here called `V_m`, by
`Z_m(0) = exp(V_m) Ztilde_m(0)`.
The bounds at 140909–140910 and 140927–140933 give UV-Z with
`C_+ = E_+^sharp` and `C_- = C_low`, independent of the cutoff at fixed
reference data.

But CA-II 141279 expressly changes the meaning of `E_m` inside the
torus-independence lemma. Its hypothesis (a), 141286–141291, subtracts
the Gaussian normalizers. Write that reduced constant as `W_m`, and
write the sum of the removed logarithms as `G_m`. Then
`V_m = W_m + G_m`. The lemma controls `W_m`, not the full `V_m`.
Its proof at 141424–141431 explicitly relies on this exclusion.
This distinction was already recorded in `gap-exit-check-astra.md:480–497`
(row 877); it is reused here, not a new finding.

**Assumption (b), cutoff independence of delta-bar: HOLDS under the
lemma's hypotheses (a)–(c).** CA-II 141378–141386 gives

```math
\bar\delta_{\rm vac}
=2(E_0+1)K_*\sum_{u\ge0}L^{4u}
 \exp\!\left[-\frac\kappa2\left(\frac12L^{11}L^u-2\right)\right].
```

The proof at 141502–141519 replaces the finite scale sum by this convergent
series. Its parameters are fixed independently of `K`, as required by
hypothesis (b). This proves the claimed uniformity for `W_m` only.

The correction is to retain the separate bound

```math
\left|\frac{G_m}{(2L^m)^4}-\frac{G_{m'}}{(2L^{m'})^4}\right|
\le c_{\rm det}
```

with `c_det` independent of the cutoff and both torus sizes. CA-II
141531–141534 attributes an additional cutoff-independent constant in
the zero-source comparison to a “determinant lemma”. The display above
states the density bound needed here explicitly; those lines give no
label or proof of that comparison.
The named-statement index and the exact-phrase searches of downloaded
CA-I and CA-II did not identify its proof. This bounded search is not a
claim that no proof exists elsewhere. The comparison remains an explicit
input here; this check does not rebuild it.

With that input, the valid density error is
`delta = delta-bar_vac + c_det`. Thus set
`C = E_+^sharp + C_low + delta-bar_vac + c_det`.
Here is the full unit calculation in `gap-phys-seed.md:92`, whose abstract
implication **HOLDS**. Use `f_lat` per lattice site and
`f_phys = f_lat/epsilon^4`. At a fixed allowed physical side `L_0`, let
`k = L_0/epsilon`. The lower UV-Z bound along arbitrarily large allowed
symmetric tori gives `f_phys >= V_(L_0)/L_0^4 - delta - C_-`.
The limit along those tori equals the infimum defining `f_lat`: monotonicity
in each side compares any fixed torus to every sufficiently large cube.
Consequently

```math
\Delta(k^4)=F(k^4)-f_{\rm lat}k^4\le C L_0^4,
\qquad
X(k;(2n)^3)\le(2n/k)^3 C L_0^4
=8C\ell_\iota^3L_0.
```

The second inequality is the existing Proposition Delta
(`gap-mid-max.md:144–146`), with `k >= 3` and `2n >= k`.
For IHC also require `k` even. The account's compatible sides have this
property. Keep `L_0` above its torus floor, the reference coupling fixed,
and the account's first-passage length equal to the trajectory's physical
unit. With rounding, use `Theta = 8C(ell + sup epsilon)^3 L_0`.

The outline's ST5 is stated as a hypothesis, not a proof of its own
packages. The corrected reduction therefore retains those packages and
the normalizer comparison, in addition to HC-phys. The sentence
“the whole open content is (HC-phys)” at `gap-ladder-max.md:232` is not
justified by the account passages read here.

## 5. Section 5.7

### CU with (APR): HOLDS AFTER CORRECTION

At `gap-ladder-max.md:197–201`, retain Proposition Delta as a cited
input. Put `k = L_0/epsilon`, require `k >= 3` even and `2n >= k`, and
use `D(k; beta_iota) <= A`. Then
`X(k;(2n)^3) <= (2n/k)^3 A` exactly.
The unrounded formula for Theta and SIZE-phys follows. If `n` is rounded
up, replace `ell` in that prefactor by `ell_iota` or its uniform upper
bound. Section 3's time and size restrictions still apply. This conditional
implication uses APR, not the stronger BASE-Phi or MONO-Delta inputs.
Identifying APR as supplied by the account retains section 4's correction.

### Square-root calculation: HOLDS; universal exclusion: FAILS

Source: `gap-ladder-max.md:203`. The Gaussian constants agree with
`gap-fc-max.md:192–200`. For one positive-energy mode, the time-chain
precision is

```math
(Qx)_j=\beta(2\cosh\omega\,x_j-x_{j-1}-x_{j+1}).
```

Its lowest Fourier value is `rho_4 = 2 beta(cosh omega - 1)`.
The constant time mode attains it on a periodic chain; arbitrarily long
nearly constant vectors attain its infimum on the infinite chain.
Thus the best *single scalar constant for all space-time functions* is
`rho_4 = 4 beta sinh^2(omega/2)`.

Blindly restricting that scalar inequality to a single slice retains
rho_4. **If** it also supplies that constant for every bridge law, its
formal insertion into BR gives
`rho_4/(2 beta) = 2 sinh^2(omega/2)`.
For `omega = M epsilon`, division by epsilon gives
`M^2 epsilon/2 + O(epsilon^3)`, which vanishes. This is the valid
square-root loss. A scalar LSI or Poincare inequality on the original
space-time law does not by itself supply an inequality on a refined
bridge law; that extra premise must not disappear.

Two qualifications break the unqualified “at best” and “any proof”
sentences of line 203.

1. The full Gaussian law contains more information than its smallest
   Hessian eigenvalue. Its inverse is
   `C_j = exp(-omega |j|)/(2 beta sinh omega)`:
   direct substitution gives `(QC)_0 = 1` and `(QC)_j = 0` for `j != 0`.
   Therefore the one-slice marginal has variance
   `C_0 = 1/(2 beta sinh omega)` and precision `2 beta sinh omega`.
   Equivalently, the Gaussian covariance-form Poincare inequality
   `Var(F) <= E[grad F . Q^(-1) grad F]` reduces on `F(x)=h(x_0)`
   to this sharp slice constant. It is an inequality of the same
   space-time Gaussian law followed by restriction, using its covariance
   rather than discarding it for a scalar lower bound. This is a concrete
   reason the scalar loss does not exclude every proof using that law.
   The Poincare calculation needs no numerical step: for a normal variable
   of variance `v`, expansion in normalized Hermite polynomials gives
   `Var(h) = sum_(r>=1) |h_r|^2 <= sum_(r>=1) r |h_r|^2 = v E|h'|^2`.
   Linear functions attain equality. Tensorization and a linear change
   of Gaussian coordinates give the displayed covariance form.
2. The actual bridge precisions already computed in BR are
   `A_s = c/(1+c s) + c/(1+c s')`, with
   `c = beta(exp(omega)-1)` and `s+s'=1/beta`.
   Their minimum is `4 beta tanh(omega/2)` and their integral is `2 omega`.
   They have the correct small-omega order. Moreover, rho_4 is not even
   a lower bound for all bridge precisions at arbitrary omega:
   at `exp(omega)=5`, it is `16 beta/5`, while the midpoint precision is
   `8 beta/3`. For sufficiently small omega it is a valid but deliberately
   weaker bound. No blanket transfer to bridge laws has been proved.

**Corrected test: HOLDS AFTER CORRECTION.** A method which retains only
the scalar space-time constant rho_4, transfers no larger constant to
the bridge laws, and inserts that constant into BR has zero limiting
physical rate. The stated exclusion of every four-dimensional-measure
method, including their possible use of additional information, FAILS as
an inference from this calculation. If “in the link metric” is intended
to mean only an unweighted scalar inequality with no further information,
the narrowed statement is exactly the valid one above.
No conclusion about SU(2) beyond this test is proved here.

The numerical illustration is not needed. Its Gaussian value can be
checked by hand: the positive series for `cosh(13/10)-1`, through degree
six with its geometric remainder bound, lies between `0.9707` and `0.971`.
Thus the printed `0.97` is consistent. The quoted `K_30 = 0.811` is
the existing shape-four test (`gap-trajtest-opus.md:40–47`), not the
shape-twenty-four constant in the original Proposition HC. Its decimal
is not used to establish any verdict here.

### Defective form: HOLDS with its stated input

Source: `gap-ladder-max.md:205`. Squaring the factor `exp(D)` gives
`X(t_1) <= 2D + theta_m X(2s)`. If `X(2s) <= Theta` and
`theta_m Theta <= 1`, then `S(t_1) <= exp(2D+1)-1`.
For integers `n >= t_1`, spectral positivity gives
`S(n) <= exp(-E_1(n-t_1)) S(t_1)`.
The printed sufficient condition yields `S(n) < s_*`.
For a cutoff-uniform conclusion, D must also be uniform in the cutoff;
to cover varying boxes it must be uniform over those boxes.
This is a bounded thermal sum, not automatically a bound on the symmetric
Casimir excess Delta without the other hypotheses of Theorem ZD.

## 6. Claim (R2): HOLDS AFTER CORRECTION

Source: `gap-ladder-max.md:59,152,244,254`. Preserve the explicitly
assumed upper bound `E_1 <= M_+ epsilon`; this check supplies no such
bound for SU(2). Since a hypercontractive rate cannot exceed E_1, success
of the stated sufficient size test requires

```math
M_+\epsilon(n-2)\ge C_{\beta_\iota}+3\log n,
\qquad C_\beta=c_0+\log\beta.
```

This is incompatible with bounded `n epsilon` along the intended family
`epsilon -> 0`, `beta_iota -> infinity`. If n is unbounded, take a
subsequence with `n -> infinity`: the right side diverges and the left
side stays bounded. If n stays bounded on a subsequence, the left side
tends to zero while `C_beta` diverges. These two cases cover every
possible sequence of integer n. The proof in line 59 only addresses the
first case, and its `1+o(1)` also requires that case.

Keep the units explicit. The physical rate demanded by the test is
`K_n/epsilon`, not `K_n`. At fixed physical length `ell = n epsilon`,

```math
\ell\,\frac{K_n}{\epsilon}
=\frac{n}{n-2}\bigl(c_0+\log\beta_\iota+3\log n\bigr),
\qquad
3\log n=3\log(1/\epsilon)+3\log\ell.
```

This gives the stated logarithmic divergence at fixed physical size.
Line 152's “K_a times the physical seed size” should say
“the required physical rate K_n/epsilon times the physical seed size”.

If an actual rate `alpha = M epsilon` is supplied, the size condition is
exactly

```math
M(\ell-2\epsilon)
\ge 3\log(1/\epsilon)+\log\beta_\iota+3\log\ell+c_0.
```

The claimed leading size `(3/M) log(1/epsilon)` additionally requires
`log beta_iota = o(log(1/epsilon))`, and a rate bounded below by M on
the growing boxes. An upper bound on the gap alone proves no existence
of such a hypercontractive rate. Without those extra inputs, report the
displayed necessary constraint rather than an attained seed size.

This obstructs the particular sufficient test derived from Proposition
HC's crude prefactor. It does not refute SEED-phys, HC-phys, or another
estimate that uses more of the transfer operator.

## Verdicts and limits

| Statement | Verdict | Scope or correction |
|---|---|---|
| 5.1 Lemma IHC | HOLDS | Physical, gauge-projected kernel; first failing step none |
| 5.1 line 134 sharpness remark | HOLDS AFTER CORRECTION | “At least”, not “at most” |
| 5.2 abstract CU and its two-sided-stability implication | HOLDS AFTER CORRECTION | Positive start time, seed size, rounding, and box-size uniformity |
| 5.2 TH via 1.1.5(iii) | HOLDS AFTER CORRECTION | Full vacuum normalization and explicit determinant-comparison input |
| TH assumption (a), literal identification | FAILS | The density lemma removes the Gaussian normalizers |
| TH assumption (b), cutoff uniformity | HOLDS | For the reduced constant, under the account's hypotheses |
| 5.6(a) trajectory restriction | HOLDS | No full-function hypercontractive hypothesis is needed |
| 5.7 APR implication | HOLDS AFTER CORRECTION | Same time, integer and rounding restrictions as CU |
| 5.7 Gaussian scalar square-root loss | HOLDS AFTER CORRECTION | Bridge input must be supplied; scalar restriction is the tested method |
| 5.7 universal method exclusion | FAILS | The calculation does not cover methods retaining further information |
| 5.7 defective inequality and spectral tail | HOLDS | Uniform defect is an input, not a consequence |
| R2 | HOLDS AFTER CORRECTION | Separate bounded n; physical rate is K_n/epsilon; retain the gap upper bound |

The delivered consumer statement is an implication: a correctly normalized
uniform start bound, plus HC-phys at a box satisfying SIZE-phys, gives
SEED-phys. This check proves neither hypothesis for SU(2).
The determinant comparison was read as an asserted input, not verified.
No audit, numerical run, simulation, symbolic calculation, or computer
enumeration discharged a mathematical step. No Balaban paper was imported.
Only this report was changed; the source, registry and status files were
left to their owners. No remote write was made.

RESULT: IHC and 5.6(a) HOLD; CU, TH, the APR form, the Gaussian scalar square-root test and R2 HOLD AFTER CORRECTION; the literal vacuum identification and the universal method exclusion FAIL; the defective implication HOLDS; the determinant-comparison input, HC-phys and SEED-phys remain unproved by this check.

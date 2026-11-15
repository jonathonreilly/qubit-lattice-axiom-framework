## Repo search

The target-specific prior digest is absent at `2cdb35e78`.
The general lead digest `prior/repo-search-2026-11-08.md` concerns earlier
hard-route interfaces, not these new thermal-sum lemmas. It records searches
of main and PRs 10114, 10133, 10134 and 10141. Its relevant transfer-operator
hit was checked at source. The registry search for
`gap-unit`, Identity G, Lemma ORD, Lemma FLOOR, Route Z and Schwarz finds no
matching owner. Row 991 is an earlier same-provider check; this task expressly
requests the cross-provider check of the original row 988.

| Prior hit read at source | Closeness and use here |
|---|---|
| PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`, at `f76f6c649cff7dffbab664d8976e680e8f287fe9` | Earlier Codex/Astra normalized one-link convolution and simple-loop eigenvalue. Supplies the normalization and loop example; does not assert ORD or 7.1. This is the lead digest's hit at lines 395 and 487. |
| Same PR and directory, `MASS_GAP_CONSTRUCTION_ASTRA.md:84–163` | Earlier Codex/Astra transfer kernel, gauge projection, simple positive top eigenvalue, and isotropic rank-one point at zero. Reused as prior construction; it does not give Identity G's fixed-spatial-coupling integral. Located through `gap-transfer.md:7`. |
| Main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:20–80` | Prior positive character/plane-kernel statement on an open two-slice carrier. Related positivity input, not the thermal trace statement. No runner is used. |
| `gap-transfer.md:108–167` | Claude Opus 5.5's port of the finite Wilson transfer construction, with explicit Gram expansion. Reuse the expansion in the trace-norm check below. |
| `gap-crux-restate.md:29–45,90–108`; `gap-skeleton-max-b.md:289–308,343–359` | Existing thermal-sum inequality and Route Z. The latter already removes `(BD)` under its zero-free and shape hypotheses. Neither target is reopened. |

The narrow label search for `gap-unit-max`, `Lemma ORD`, `Identity G` and
`Lemma FLOOR` found no match outside this lane on the fetched main and PR
10114. That is a label search, not a proof of repository-wide absence.

The SA-index README, `chunk-02.md:87–102`, `chunk-04.md:80–90`, and the
matching obligations at `obligations.md:51–75,154–165` led to these reads:

| Published source read | Source status and use |
|---|---|
| SA 2197–2257 and 2315–2335 | GL3's Bessel eigenvalues and GL8's transfer trace are proved there. Port these inputs; they are not new results of row 988. |
| SA 4695–4729 | The normalized zero-free-disc lemma is proved, with a volume-dependent counterexample. Its bound assumes a modulus bound on the function and produces a small disc. It is not the common-domain hypothesis of 7.1. |
| CA-I 47814–47856, located through `ca-4.12-4.19/chunk-05.md:293–299` and neighboring rows | A conditional Schwarz comparison for local quadratic-form matrices. It is an existing use of the analytic method, not an ORD or thermal-sum theorem. |

Provenance: OpenAI/Codex, configured session model and effort; check of
`gap-unit-max.md` at `2cdb35e78e47e3ee645cce2d3e6148a2b508365c`.
Research text, not an audit; no status granted. No numeric proof or run.
Credit: Claude Fable 5.2 authored row 988. Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text, authored the cited outline
and complete account at `31a47c543775`.

### Checkpoint

All six planned steps are complete: sources, Identity G, ORD, FLOOR,
Schwarz/Borel–Carathéodory, and the corrected 7.1 consequence. The checks
below concern exactly the original source lines at the pinned commit.

Both requested source files were fetched once into the new empty directory
`/tmp/sa-gap-unit-check-astra.ZAGHBG/`. No source download enters this checkout.
Only this output file is changed. No numerical run, Lean run, audit, source edit,
registry edit, external post or push was performed. Uniform zero-freeness,
the physical seed, (U1) and (U2) remain open. Source searches are locators,
never proofs of absence.

## 1. Identity G — HOLDS AFTER CORRECTION of the time domain

Lines 199–210 are correct for a finite periodic spatial box, real fixed
`beta_s`, nonnegative real `beta_t`, and **integer** time `t >= 1`.
Line 40 introduced real time; the torus identity here needs integer time.
For a box with free spatial walls replace `3 |B|` by its number of spatial
links `N_E`. This is also its number of temporal plaquettes per time step.
Use the average over all those plaquettes, not a chosen orientation.

Let `W_s` be the spatial action, `A = exp(-beta_s W_s/2)`, and let `P_0`
project onto constants in normalized product Haar measure. At `beta_t=0`,
the **unnormalized Wilson** temporal convolution is `P_0`. Thus

```math
T(0)=A P_0 A=|A\mathbf1\rangle\langle A\mathbf1|,
\qquad \lambda_0(0)=\int e^{-\beta_s W_s}\,dU=Z_3(B)>0.
```

Temporal links integrate to one, including the periodic seam. Therefore
`Z_t(0)=Z_3(B)^t`, `S_t(0)=0`, and `X_t(0)=0`. This verifies lines 203,
206 without temporal gauge fixing or a missing Haar-volume factor.

Here is the derivative-limit justification in lines 207–210. Put
`p_t(s)=t^{-1} log Z_t(s)`. The transfer trace and the simple positive top
eigenvalue give `p_t(s) -> p(s)=log lambda_0(s)` at each real `s >= 0`.
The bounded finite-volume action gives

```math
p_t'(s)=-N_E\bar a_t(s),\qquad p_t''(s)=t^{-1}\operatorname{Var}_s(A_t)\ge0.
```

For `s>0` and small `h>0`, convexity gives

```math
\frac{p_t(s)-p_t(s-h)}h\le p_t'(s)
\le\frac{p_t(s+h)-p_t(s)}h.
```

First take lower and upper limits in `t`, then let `h` decrease to zero.
Analytic perturbation of the simple isolated eigenvalue makes `p`
differentiable. Hence `p_t'(s)->p'(s)`; this proves the existence of the
plaquette-average limit used in the identity. The derivative limit also has
a direct spectral check: at fixed `s>0`, write `T=lambda_0 Pi+R`. Cyclicity
gives

```math
p_t'(s)=\frac{\operatorname{Tr}(T^{t-1}\partial_sT)}{\operatorname{Tr}T^t}.
```

The numerator's top term is `lambda_0^(t-1) lambda_0'`, since
`Tr(Pi partial_s T)=lambda_0'`. Its remainder is bounded for `t>=2` by
`||R||^(t-2) ||R||_1 ||partial_s T||`. Since `||R||<lambda_0`, division by
the denominator gives the same limit `lambda_0'/lambda_0`. At `s=0`,
`R(0)=0`, so `partial_s Tr R(s)^t` vanishes for `t>=2`, giving the limit
there too. Since `0 <= abar_t <= 2`, no singular integral endpoint arises.
Consequently

```math
\partial_s X_t(s)=N_E t(\bar a_\infty(s)-\bar a_t(s)),\qquad
X_t(\beta_t)=N_Et\int_0^{\beta_t}
(\bar a_\infty(s)-\bar a_t(s))\,ds.
```

The analytic-family justification is supplied explicitly in the next section.
It is finite-volume; it gives no bound uniform in the size of `B`.

## 2. Lemma ORD — HOLDS AFTER CORRECTION

Lines 286–296 hold for **integer** `t >= 1`, with “order at least `4t`”.
The RESULT at line 369 must retain “at least”. The corrections below also
separate normalized convolution from the Wilson transfer operator and remove
the extra factor of `beta` in the spatial action notation.

**Trace-norm analyticity (lines 286–287).** Use the rank-one expansion already
in `gap-transfer.md:147–154,161–167`, not the recalled smooth-kernel assertion.
For `N_E` links set `p_alpha(U)` to a product of `k` fundamental matrix
entries. Its expansion and norm identity give, for complex `z`,

```math
C_E(z)=e^{-N_Ez}\sum_{k\ge0}\frac{(z/2)^k}{k!}
             \sum_{\alpha}|p_\alpha\rangle\langle p_\alpha|,
\qquad \sum_\alpha\|p_\alpha\|_2^2=(2N_E)^k.
```

Indeed, pointwise `sum_alpha |p_alpha(U)|^2=(2N_E)^k`, since each SU(2)
matrix has squared Hilbert–Schmidt norm two. The trace-norm series is bounded
on `|z|<=R` by `exp(2 N_E R)`. It converges locally uniformly in trace norm,
so is entire. Gauge projection and bounded analytic multiplication by `A`
preserve this property. This argument also supplies the family used in G.

**Normalization (line 291).** Port GL3, SA 2205–2229:

```math
c_j(z)=\frac{2e^{-z}}z I_{2j+1}(z),\qquad
c_0(0)=1,\qquad \rho_j(z)=c_j(z)/c_0(z).
```

All apparent singularities at zero are removable. On a small disc `c_0`
is nonzero. The source's `K_beta=sum_R rho_R P_R` is therefore
`Kbar=c_0^{-N_E} C_E` on the gauge-invariant Hilbert space. The original
transfer operator has the extra scalar `c_0^{N_E}`. It cancels from `S`
and `X`, but must be retained when differentiating the raw partition function
in Identity G. The Bessel series read at SA 2226–2229 shows that `rho_j`
has exact order `2j`.

**Gauge constraint (lines 292–293).** A nontrivial edge-label assignment
survives vertex gauge averaging only when the incident representations admit
an invariant tensor at each vertex. A vertex with one nonzero incident spin
does not admit one. Thus the support graph has minimum degree at least two.
Following edges without immediately reversing eventually produces a simple
cycle. On the periodic nearest-neighbor spatial graph with sides at least
four, there are no loops, parallel edges, or triangles. Every such cycle
has at least four edges. Hence `sum_e 2j_e >= 4` for every nonconstant
surviving label. Peter–Weyl projections preserve this gauge-invariant
subspace, and their finite sums are dense there. The first four Taylor
coefficients of `Kbar-P_0` vanish on that dense sum. They therefore vanish
as bounded operators and as trace-class operators. It follows that

```math
\overline K(z)=P_0+z^4 N(z),
```

where `N` is trace-norm analytic near zero. No uniform bound in `B` is
asserted or needed here.

**The moving rank-one part (lines 294–296).** Write `W_s` for the unweighted
spatial action. In the isotropic case put `A(z)=exp(-z W_s/2)`; in the
anisotropic case put `A(z)=exp(-beta_s W_s/2)`. Set

```math
Q(z)=A(z)P_0A(z),\qquad
q(z)=\int A(z)^2\,dU,\qquad
\overline T(z)=Q(z)+z^4 A(z)N(z)A(z).
```

At zero `q(0)>0`. Near zero `Q^2=qQ` and its nonzero spectral projection
is `P_Q=Q/q`. In particular, `Q` varies with `z` in the isotropic case;
it is not the fixed operator `T(0)`. This resolves the notation `T_0`
and `integral exp(-beta V)` in line 294, where line 200 had already put
the spatial coupling into `V`.

Choose a fixed contour enclosing `q(0)` but excluding zero. For small `z`
it separates the rank-one eigenvalue of both `Q(z)` and `Tbar(z)`.
The Neumann resolvent series defines analytic resolvents on that contour.
The resolvent identity, with `Tbar-Q=O_1(z^4)`, gives

```math
\Pi-P_Q=\frac1{2\pi i}\oint
(w-\overline T)^{-1}(\overline T-Q)(w-Q)^{-1}\,dw=O_1(z^4).
```

The contour projection `Pi` has rank one (it is norm-close to `P_Q`).
Its eigenvalue `lambda(z)=Tr(Tbar Pi)` is analytic and nonzero near zero.
With `R=Tbar(1-Pi)`, use `Q(1-P_Q)=0` to obtain

```math
R=(\overline T-Q)(1-\Pi)+Q(P_Q-\Pi)=z^4 H(z)
```

in trace norm. Since `R Pi=Pi R=0`, for every positive integer `t`,

```math
S_t(z)=\frac{\operatorname{Tr}R(z)^t}{\lambda(z)^t}
      =z^{4t}\frac{\operatorname{Tr}H(z)^t}{\lambda(z)^t}.
```

Trace-class operators form an ideal, so the last quotient is analytic.
This completes the load-bearing step without the two recalled perturbation
and trace-class assertions.

**Why the time correction matters.** At `beta_s=0`, a fundamental spin
around one plaquette is a gauge-invariant eigenvector with ratio
`rho_(1/2)(z)^4`, and `rho_(1/2)(z)=z/4+O(z^3)`. For positive real `z`,
the trace-norm bound just proved and positivity give, for any real `t>=1`,

```math
c_t z^{4t}\le S_t(z)\le
\|\overline K-P_0\|^{t-1}\|\overline K-P_0\|_1
\le C_t z^{4t}
```

near zero, with `c_t>0`. At `t=9/8` an analytic function cannot have these
bounds: its first nonzero Taylor degree would have to equal `9/2`.
Thus the real-time extension is **FAILS**, while the integer-time lemma
needed in 7.1 holds. The spin-network argument does not need a time torus
of side one; at `t=1` it is directly an operator-trace statement. A geometric
one-slice torus uses the based-plaquette counting convention.

## 3. Lemma FLOOR — HOLDS AFTER CORRECTION of the sector label

The positive-sum statement at lines 174–179 holds. Assume a nonzero positive
trace-class operator, a simple top eigenvalue `lambda_0>0`, and a closed
invariant subspace `H_*` containing its top eigenvector. For a positive
eigenvalue `lambda_i<lambda_0` in **that subspace**, set
`E_i=log(lambda_0/lambda_i)`. Whenever the thermal trace is finite,

```math
S_*(a)=\sum_{i\in H_*,\ i\ne0}e^{-aE_i}\ge e^{-aE_i}.
```

The inequality also holds with an infinite left side. Compactness ensures
that a nonempty positive excited spectrum has a largest eigenvalue below
`lambda_0`; its energy is the sector gap `m_*`. Consequently

```math
S_*(n)<1/5041\quad\Longrightarrow\quad
n m_*>\log5041=2\log71,\qquad (2n)m_*>4\log71>17.04.
```

If there is no positive excited eigenvalue, use `m_*=+infinity`.
For the full physical trace, `m_*` is the `m((2n)^3)` used in line 177.
For a restricted sector, that symbol must mean its **restricted** gap.
The inference to the full-space gap otherwise **FAILS**: take
`T=diag(1,1/2,1/100)`, trace on the first and third coordinates, and `n=2`.
Then `S_*(2)=1/10000<1/5041`, but the full-space gap gives
`n m=log4<log5041`. The floor alone never transfers a sector seed to the
full-state engine.

The decimal bound needs no numerical calculation. The positive series
`log x=2 sum_(k>=0) y^(2k+1)/(2k+1)`, `y=(x-1)/(x+1)`, gives

```math
\log2>\frac{842}{1215},\qquad
\log(71/64)>\frac{14}{135},\qquad
\log71>\frac{1726}{405}>\frac{213}{50}=4.26.
```

For the illustrative levels in lines 181–185, the arithmetic is consistent
if their recalled dispersions are supplied. A periodic energy `2pi/side`
has `nE=pi` and `side E=2pi`; a twisted energy `pi/side` has `nE=pi/2`
and `side E=pi`. These are different units from the `17.04` side-gap bound.
Also `log5=2log2+log(5/4)>130/81>11/7>pi/2`, so
`exp(-pi/2)>1/5` and `exp(-pi)>1/25`. Here `pi<22/7` follows, for example,
by integrating the positive function `x^4(1-x)^4/(1+x^2)` on `[0,1]`:
its integral is `22/7-pi`. None of this establishes the recalled interacting
or twisted spectra. They are not premises of the abstract floor.

## 4. Schwarz transport — HOLDS

Lines 298–300 hold on a proper simply connected plane domain `D` containing
zero, with the stated conformal map `phi:D->unit disc`, `phi(0)=0`, and
an integer `N>=0`. The existence of this map already excludes `D=C`.
For `M>0` put `f(w)=h(phi^(-1)(w))/M`. Since the conformal map has a simple
zero, `f` vanishes to order at least `N`. Thus `g(w)=f(w)/w^N` is holomorphic
at zero. On `|w|=r<1`, `|g|<=r^(-N)`. The maximum principle on that disc,
followed by `r` increasing to one, gives `|g|<=1` and hence

```math
|h(z)|\le M|\phi(z)|^N.
```

For `M=0` the claim is immediate. No boundary extension of `h` or `phi`
is needed. The source's one-line proof is this limiting argument, not an
application of the maximum principle to a nonexistent outer boundary trace.

## 5. Borel–Carathéodory step — HOLDS

Here is the missing argument requested at lines 302 and 351–352. Let `D'`
be simply connected and contain zero. Suppose `zeta(0)=1`, `zeta` is
holomorphic and zero-free there, and

```math
\log|\zeta(z)|\le c|z|V.
```

The branch `F=log zeta` with `F(0)=0` exists: integrate `zeta'/zeta` in
the simply connected domain and use `zeta(0)=1`. Fix any domain `D` with
compact closure in `D'`. If `D'` is proper, choose a conformal map
`psi:D'->unit disc` with `psi(0)=0`. Choose

```math
\sup_{z\in\overline D}|\psi(z)|\le r<R<1,
\qquad L_R=\max_{|w|\le R}|\psi^{-1}(w)|,
\qquad M=c L_R V.
```

The maximum defining `L_R` is finite by compactness. For
`u(w)=F(psi^(-1)(w))` on `|w|<R`, we have `u(0)=0` and `Re u<=M`.
If `M=0`, the harmonic maximum principle gives `u=0`. Otherwise set

```math
v(w)=\frac{u(w)}{2M-u(w)}.
```

The denominator cannot vanish, and
`|2M-u|^2-|u|^2=4M(M-Re u)>=0`. Hence `|v|<=1` and `v(0)=0`.
Schwarz on the radius-`R` disc gives `|v(w)|<=|w|/R`. Solving for `u`,

```math
|u(w)|=\left|\frac{2Mv(w)}{1+v(w)}\right|
\le\frac{2M|w|}{R-|w|},\qquad
\sup_D|\log\zeta|\le\frac{2cL_Rr}{R-r}\,V=:C_D V.
```

If `D'=C`, use a large disc containing `overline D` and zero instead.
Thus the constant depends only on the chosen domains and `c`, not on the
volume or the particular zero-free function. This is a direct proof of
the required Borel–Carathéodory bound.

For the Wilson tori, normalized Haar gives `Z(0)=1`. There are `6V`
based plaquettes, each with action in `[0,2]`. Compact integration gives
`|Z(z)|<=exp(12|z|V)`, so take `c=12`. The whole argument requires the
zero-free hypothesis; the extensive modulus bound does not supply it.

## 6. Consequence in 7.1 — HOLDS AFTER CORRECTION

Use integers `n>=2`, nonnegative real physical coupling, and one common
zero-free domain for the two torus families. Work on a proper simply
connected `D` with `0 in D` and `overline D` compact in `D'`. The conclusion
is a seed for every **fixed** such coupling once `n>=n_0(beta)`; it is not
a cutoff-uniform physical seed. On compact subsets the size threshold is
uniform. The following verifies every step of lines 302–309.

1. **The logarithms and the trace identity (302–304).** Set
   `Z_(1,n)=Z(n,2n,2n,2n)` and `Z_(2,n)=Z(2n,2n,2n,2n)`. Under zero-freeness
   in `D'`, choose their logarithms to vanish at zero and set
   `G_n=2 log Z_(1,n)-log Z_(2,n)`. Near zero, the same spatial box and
   the same analytic top eigenvalue occur in both traces. Thus

```math
G_n=2\log(1+S_n)-\log(1+S_{2n}).
```

   For positive real `beta`, nonnegative eigenvalue ratios `r_i<=1` give
   `S_(2n)<=S_n`. Hence

```math
0\le\log(1+S_n)\le
2\log(1+S_n)-\log(1+S_{2n})=\operatorname{Re}G_n.
```

   This checks the needed inequality directly; it is the first part of
   Theorem D(b), `gap-crux-restate.md:102–103`. There is no need for its
   subsequent comparison with the hypercubic `Phi`.

   The real part is deliberate. If `D'` contains the real segment from zero
   to `beta`, the normalized branches are real there and `Re G_n=G_n`.
   Simple connectivity alone need not put that segment in `D'`. In that
   general case `Re log Z=log|Z|=log Z` at a positive real coupling is
   enough. No global continuation of `lambda_0` is used.

2. **Order at zero (304).** The spatial sides `2n>=4` permit ORD. For each
   fixed `n`, `S_n=O(beta^(4n))` and `S_(2n)=O(beta^(8n))`. The logarithmic
   series above gives `G_n=O(beta^(4n))`. This is a local statement about
   Taylor coefficients; its neighborhood need not be uniform in `n`.

3. **Uniform bound (305).** The two volumes are `8n^4` and `16n^4`. Section 5
   gives the same domain constant for each, hence

```math
\sup_D|G_n|\le(2\cdot8+16)C_D n^4=32C_D n^4.
```

4. **Transport (305–306).** Apply section 4 to the analytic function `G_n`
   with its zero of order at least `4n`:

```math
0\le X_n(\beta)\le\operatorname{Re}G_n(\beta)
\le |G_n(\beta)|\le32C_D n^4|\phi_D(\beta)|^{4n}.
```

   With the Green-function convention `g_D(beta,0)=-log|phi_D(beta)|`,
   the final factor is `exp(-4n g_D(beta,0))`.

5. **Seed (306–307).** Fix `beta in D` with `beta>0`, and let
   `q=|phi_D(beta)|<1`. The ratio of consecutive terms of `n^4 q^(4n)`
   tends to `q^4<1`; therefore those terms tend to zero. Choose `n_0(beta)`
   so the bound in step 4 is less than `log(5042/5041)` for all `n>=n_0`.
   Then

```math
S(n;(2n)^3)=e^{X_n}-1<1/5041.
```

   At zero the seed is immediate. For a compact `K` in `D`, replace `q`
   by `max_K |phi_D|<1`. Zero-freeness for an unbounded sequence of these
   two shapes also suffices, with the conclusion along that sequence.

6. **What changed (307–309).** This argument needs no separately supplied
   `(SC)` expansion or `(BD)` bound. However, removing `(BD)` was already
   the point of Theorem Z, `gap-skeleton-max-b.md:343–359`; its proof used
   zero-freeness and a Borel–Carathéodory estimate. The present addition
   replaces the strong-coupling-circle input by ORD and avoids that
   theorem's `(TUBE)` shape condition. The comparison with Corollary 4's
   `r_0 -> 0` is methodological, not a proved literal limit of its different
   functions and hypotheses. The two-torus proof above is self-contained.

The uniform zero-free domain is still an assumption. This check does not
verify the claimed thin-tube obstruction at line 309, any free-wall
extension at line 310, or a continuum gap. In particular, as bare `beta`
varies toward the continuum limit, `q` may approach one and `n_0(beta)`
may diverge. Neither (U1) nor (U2) follows without further input.

## 7. Verdicts and limits

| Statement in `gap-unit-max.md` | Verdict | Required reading or correction |
|---|---|---|
| Identity G, 199–210 | HOLDS AFTER CORRECTION | Integer temporal extent for the torus formula; average all temporal plaquettes. The factor `3 |B|` is for periodic spatial boxes. |
| ORD, 286–296 | HOLDS AFTER CORRECTION | Integer time, normalized convolution, and the moving rank-one reference above. The real-time analytic extension FAILS. |
| FLOOR, 174–179 | HOLDS AFTER CORRECTION | Its gap is the gap of the traced sector. An inference to an excluded excitation FAILS. For the full trace its displayed numerical threshold holds. |
| Schwarz transport, 298–300 | HOLDS | Proper domain and the conformal map as stated; proof above needs no boundary regularity. |
| Borel–Carathéodory step, 302 and 351–352 | HOLDS | Normalized logarithm; compact inner domain; constant independent of volume. |
| Consequence 7.1, 302–309 | HOLDS AFTER CORRECTION | `n>=2`, nonnegative coupling, common domain, real-part convention, and `n_0(beta)` at fixed coupling. Removal of `(BD)` is prior work. |

These are checks of the original arguments, with the missing analytic steps
written out. They do not check the rest of row 988's direction proposals.
The earlier row-991 result was visible in FINISH during source discovery;
its report was not used to prove any statement here. Changing provider alone
is not an independent mathematical path: the added load-bearing work here
is the trace-norm Gram expansion with a contour-resolvent estimate, the
real-time and sector counterexamples, and the explicit normalized
Borel–Carathéodory proof. No model vote or run discharges a claim.

RESULT: Identity G, Lemma ORD, Lemma FLOOR and consequence 7.1 HOLDS AFTER CORRECTION as specified; Schwarz transport and the written Borel–Carathéodory step HOLDS. The real-time analytic extension of ORD and a restricted-sector inference to the full gap FAILS. The corrected implication yields a seed at each fixed nonnegative coupling from a common zero-free domain; that domain, the cutoff-uniform physical seed, (U1) and (U2) remain open. Research check only; no status granted and no computer-assisted step.

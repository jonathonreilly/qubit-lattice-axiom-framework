## Repo search

The target-specific prior file is absent at `4b9244e4e`.
`prior/repo-search-2026-11-08.md` records a search of main and PRs
10114, 10133, 10134 and 10141. It predates row 1000 and concerns other targets;
it supplies no prior check of this file. Two nearby hits were opened again:

| Source checked | Closeness |
|---|---|
| Main, `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A covariance lower bound for a noncompact Dirichlet Maxwell measure on a quotient. Different law and boundary; no BR or pinned-sheet result. |
| PR 10114, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | Earlier positive-type convolution and one-step plaquette witness. Related positivity method; no parameter-dependent RP or shifted-sheet domination statement. |

The current task names no further outside-lane prior hit. The local sources
`gap-hcphys-max.md`, `gap-fc-max.md` and `gap-tiltproof-max.md` are the direct
prior work checked below. The registry has no matching owner for this check.
No result found here duplicates the requested cross-provider reading.

Research check by Codex, gpt-6-astra, xhigh, against commit
`4b9244e4e78cb6dfcf673bdb7087634f6b039ecd`. This is not an audit and grants no status.
The source is Claude Opus 5.5 high's row 1000, `library/gap-d2-inputs.md`.
All line numbers below refer to that pinned revision unless qualified.
No numerical or computer-assisted proof is used.

Plan: (1) check prior work and source contracts; (2) check Step 2;
(3) check Step 4; (4) check RP/PT; (5) check GD/IR;
(6) check the Step 7 consumption table and record the result.

## Step 2: T3 and the proposed rule

Here and below, **FAILS** can mean a failing proof step, not a counterexample
to its unproved final conclusion. T3's nonlinear conclusion remains open.

| Source line | Verdict | Reason |
|---|---|---|
| 28, 30 | HOLDS AFTER CORRECTION | The raw count is insufficient for the gauge-invariant BR hypothesis. The proposed correction does not finish that check; it remains a linearised benchmark. |
| 34, (a) | HOLDS | BR integrates over length less than `1/beta_0`. Thus obtaining rate at least `M_H a_iota` requires `sup alpha_s >= 2 beta_0 M_H a_iota`. This is a necessary condition for this sufficient proof, not for hypercontractivity by every method. |
| 36, (b) | HOLDS AFTER CORRECTION | For a continuum Gaussian transverse mode with fixed stiffness, integrating `dp_0/(2 pi)` gives `1/(2 beta abs(p))`. With shell-dependent stiffness this is only an order comparison, needing bounds across the contributing temporal shells. It is not an exact covariance for the account's field. The test is invariant under the additive linearised gauge action, not the full SU(2) action used in BR. |
| 38, (c), variance algebra | HOLDS | The factor is `((1-lambda)^2+lambda^2+2 rho lambda(1-lambda)) sigma^2`, whose minimum is `(1+rho)sigma^2/2` for `0<=rho<=1`. Independent noise adds variance. |
| 38, application to `alpha_s` | HOLDS AFTER CORRECTION | This bounds a Poincare/LSI constant tested on the stated linear Gaussian class, provided that joint law and `rho>=0` are supplied. It does not bound BR's restricted constant without an admissible invariant test. |
| 40, (d) | HOLDS AFTER CORRECTION | The logarithmic ratio follows conditionally from the proposed upper estimate, fixed terminal stiffness and the stipulated one-loop running relation. Neither that upper estimate for BR nor an actual-model obstruction has been established. |
| 42, (e) | FAILS | No law meeting the claimed common premises is constructed. The text itself leaves the window truncation and sphere-valued model unmatched. Untruncated Gaussian sharpness cannot establish the displayed existential claim for (P1)–(P3) and BR. |
| 44, (f) | FAILS | The claimed Gaussian energy identity is false, and it does not force the dispersion or rule out running stiffness. See the exact one-mode check below. |
| 46 | FAILS | The required transfer-structure conclusion does not follow. One may record that this particular level-count estimate has not delivered a uniform rate. The text has not proved that every level-convexity route must fail or must use the named repair. |

The domain defect at line 36 is substantive. Write a colour test as
`f(A)=sum_b <w_b,A_b>`. The condition `w=d*psi` kills `A -> A+d chi`.
A constant SU(2) transformation also sends `A_b -> Ad_g A_b`.
For fixed nonzero colour `w`, choose `g` whose adjoint action rotates it.
Then `f(Ad_g A)` need not equal `f(A)`. Theorem BR requires invariance
under that action too (`gap-fc-max.md:142,146–147`). A suitable invariant
nonlinear or quadratic test and its estimates are not supplied here.

For line 44, use the same hand-solvable Gaussian mode already present in
`gap-fc-max.md:193–198`. Set `c=beta_0(e^E-1)>0`. Its endpoint density is

```math
J(dx\,dw) \propto
\exp\!\left[-\frac{\beta_0}{2}(x-w)^2
            -\frac c2(x^2+w^2)\right]dx\,dw.
```

Inverting this two-by-two precision matrix gives

```math
\rho=e^{-E},\qquad
\sigma^2=\frac{1}{2\beta_0\sinh E},\qquad
\sigma^2(1-e^{-2E})=\frac{e^{-E}}{\beta_0},
```

not `1/beta_0`. This can also be checked directly from the cited bridge:
`u_s(y)=y/(1+c s')`, so its integrated squared gradient is

```math
\int_0^{1/\beta_0}\frac{ds}{(1+c s')^2}
=\frac{1}{\beta_0+c}=\frac{e^{-E}}{\beta_0}.
```

The missing factor is the gradient of the conditional interpolant.
Even the small-`E` approximation determines covariance in terms of `E`,
not spatial momentum. A dispersion identification `E~|p|` is additional.
Choosing `E=(beta_K/beta_0)|p|` gives covariance of order
`1/(2 beta_K |p|)` at small `E`, with the bare kinetic coefficient unchanged.
This refutes the stated inference; it constructs no new Yang–Mills route.

Consequently `gap-hcphys-max.md:88,99,177` can retain a conditional
benchmark warning, not a proved exclusion. Its own line 113 leaves the
response-map estimate ARGUED. The independent-level TEL inequality
at lines 107–111 supplies a lower bound on an admissible LSI rate;
an upper bound requires a matching sharpness example in the tested class.
Line 115 does not supply that example and cannot fix a roughness exponent
from the integrated energy identity alone.

## Source comparison and credit

The outline index was used before the source: README instructions,
`chunk-03.md:15–29` and neighbouring rows, and `obligations.md:76–107`.
The source passages read were outline 2775–2795 and 2834–2883.
They already give the positive Gram expansion, crossing-kernel compression,
the integral-of-squares form and preservation by symmetric half-weights.
These are prior methods, not new results of row 1000 or this check.
They do not state this pinned slab's parameter-dependent sheet inequality.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, at source revision `31a47c543775`.
Also retain row 1000's credit to Osterwalder and Seiler;
Fröhlich, Israel, Lieb and Simon; and Fröhlich, Simon and Spencer.
The underlying proof techniques are theirs. This check verifies the written
finite-dimensional arguments, not bibliographic claims of novelty.

The complete-account index and neighbouring rows locate the general RP
results in CA-II, at 60440 and 60634, and the convexity inputs at 75164
and 81161. Those entries are locators, not proof evidence.
CA-I 545–579, 2703–2712 and 3190–3205 were read: they state the symmetry
conventions, defer RP to later chapters, and do not assert a mass gap.
The 4.12–4.19 index concerns the operator/stage interface, not the requested
BR or sheet inequality. The check treats (P1)–(P3) as the premises printed
in `gap-hcphys-max.md:46–54`; it does not redo their CA-II port.

## Step 4: the pinned slab and crossing variables

| Source line | Verdict | Check |
|---|---|---|
| 52 | HOLDS | This is the finite slab of D2 5.1, with the sheet constants retained. Use `beta>0` as stated at line 113; `b` may be any real number. |
| 68, 70 (T-a) | HOLDS | The two cuts have distinct crossing endpoints for every even `S>=4`. Their direction-2 links in slices 0 and 1 are already fixed. |
| 72–75 (T-b) | HOLDS | Condition on all crossing links. Each chosen endpoint is distinct, each other variable undergoes fixed left/right group translations, and product Haar is preserved. The gauge transformation is the identity at slices 0 and 1, so pinning and every shifted-sheet term are unchanged. Integrating the crossing variables then contributes mass one. |
| 77 (T-c) | HOLDS | The two crossing edges of a straddling plaquette become identities. The remaining pair gives the quaternion dot product. Layer-0 straddling time plaquettes are constants, so negative `b` never becomes a negative cross coefficient. |
| 79 (T-d) | HOLDS | Reflection preserves slice/layer labels. Thus both end coefficients `beta/2` match their partners. Reversed traces agree for SU(2). |
| 81 (T-e) | HOLDS | The remaining reference is a product, and inversion preserves Haar and the identity point masses. |
| 83 (T-f) | HOLDS | Exchanging coordinates 2 and 3 carries every object and pinning constraint in the preceding argument to the required one. |
| 85 | HOLDS AFTER CORRECTION | The resulting **two-half kernel** has Lemma RP's form. An arbitrary fixed nonsymmetric `h` need not itself define an RP measure. The required assertion is the mixed-field inequality proved in F5. |

The gauge-fixing statement is a conditional integration identity; it is
not an invertible map from all links onto fewer links with a Jacobian.
Line 74 correctly gives the former argument. It uses Haar on time links
outside layer 0, including those incident to slices 0 and 1.

## Step 5: RP and PT

| Source line | Verdict | Check |
|---|---|---|
| 54–58, Lemma RP | HOLDS | For each finite index list, the kernel is a Gram kernel of the integrated exponential features. No bound uniform in the entire index set is required. |
| 60 | HOLDS AFTER CORRECTION | `a_i=A+log F_i` represents only positive `F_i` with bounded logarithm. For arbitrary bounded signed tests use the signed-weight feature expansion at line 107. This extension is already proved there. |
| 92, proof (1) | HOLDS | Finitely many bounded features and a finite measure give the displayed integrable majorant. |
| 93–95, proof (2) | HOLDS | Pull back the second copy by the stated measure identification; swapping integration variables gives symmetry. |
| 96–98, proof (3) | HOLDS | The absolute exponential series has a uniform integrable bound for each pair. Fubini factorises each feature. |
| 99–101, proof (4) | HOLDS | Every coefficient is nonnegative, and the finite quadratic form is a convergent sum of squares. |
| 102, proof (5) | HOLDS | Positivity of the two-by-two Gram matrix implies its determinant is nonnegative, including a zero diagonal case. |
| 104 | HOLDS | Boundedness and finite mass suffice; compactness is not used in this lemma's proof. No formal Lean check was performed. |
| 106–107, Corollary PT | HOLDS | Symmetry makes the two means equal. Center first; the integrated positive-type expansion gives a sum of squares even though the centered test changes sign. The defined probability law presupposes nonzero `rho`. |
| 108, consumption | HOLDS | The same positive finite `m` measure appears at both ends, and `b>=0`. These are precisely PT's hypotheses. |

A direct operator check reaches the same load-bearing point. With
`v_alpha(u)=sqrt(c^alpha/alpha!) C(u)^alpha`, the cross kernel is
`<v(u),v(u')>`. Multiplication by each real test and integration produces
vectors whose inner products are the reflection form. For PT the vector
of the centered test has nonnegative squared norm. This checks the
centering and sign issue without assuming that the marginal is `rho`.

## Step 6: GD, (F1)–(F7), and IR

| Source line | Verdict | Check |
|---|---|---|
| 62, 111–113, Lemma GD | HOLDS AFTER CORRECTION | The conclusion holds for `beta>0`, every finite slab and every real `b`, with the constant-factor correction to F5 below. |
| 115 | HOLDS | Reversing a bond negates both gradients, leaving its squared norm and the count unchanged. |
| 117, F1 | HOLDS | Constants cancel from gradients. The integrand is strictly positive and the reference is a probability. |
| 119, F2 | HOLDS | The given `C_0` overcounts some constants, harmlessly. It bounds the integrand independently of `h` and provides domination for continuity. |
| 121, F3 | HOLDS | At a maximal-gradient bond use `norm(grad P)<=2`, with `D>=2` before squaring the lower bound. The other terms retain their uniform upper bounds. |
| 123, F4 | HOLDS | A torus path has length at most `S`; fixing `h(y_0)=0` bounds every coordinate by `S D`. The superlevel set is nonempty, closed and bounded in finite dimension. |
| 125–133, F5 | HOLDS AFTER CORRECTION | The quadratic split at 131 is exact, and the reflected fields give the two diagonal kernels. Retain the constant contribution of layer-0 straddling time plaquettes when asserting `Z(h)=K(f,g)`. |
| 135, F6 | HOLDS | A reflected field kills both cut gradients and copies each internal bond once. The two counts therefore sum to `2(N-N_x)` exactly. |
| 137, F7 | HOLDS | Each nearest-neighbour sheet bond crosses its own bisecting reflection. No power-of-two assumption on `S` is used. |
| 139, maximiser argument | HOLDS | Both reflected factors must equal the positive maximum. Their count average is strictly smaller whenever a crossing gradient is nonzero. Subtracting a constant returns either field to `H_0`. The minimal-count contradiction proves the conclusion. |
| 141, single-reflection remark | HOLDS | Split a crossing shift into opposite half-shifts `h/2` and `-h/2`; each diagonal kernel has zero relative shift. Its half-weight includes `A` or `B` respectively. This proves the quoted single-cut inequality, not the entire sheet iteration by itself. |
| 143–144, Corollary IR | HOLDS AFTER CORRECTION | The stated bound follows from corrected GD. Momenta mean nonzero characters of the finite torus, modulo `2 pi`; a nonzero reciprocal-lattice representative of the zero character is excluded. |
| 145, IR(i) | HOLDS | Bounded `X` justifies both derivatives. A maximum at zero gives `E X=0` and `E X^2<=c`. |
| 146, IR(ii) | HOLDS | Each unoriented bond occurs once. Collecting its two endpoint coefficients gives the positive graph Laplacian and its Dirichlet form. |
| 147, IR(iii) | HOLDS | Its eigenvalue is `2E(p)`. The displayed powers of `beta` and that eigenvalue give the claimed normalization. |
| 148, IR(iv) | HOLDS | Translation invariance makes the correlation even. The character sum distinguishes `2p!=0` from nonzero order-two characters. Both cases give the same bound. |
| 149 | HOLDS as a scope statement | The infinite-slab passage is a separate input. This check does not rebuild D2 5.1. |

The only missing term in F5 is explicit and harmless to the inequality.
Let `C_theta` be the sum of the constant exponents from straddling
layer-0 time plaquettes. Every such plaquette has value one; its contribution
is `b`, independently of `U` and `h`. Line 128 lists only coefficients
`beta` and `beta/2`, while line 127 includes only plaquettes inside a half.
Thus the written split omits `C_theta`. Either add `C_theta/2` to each
`a_f`, or write

```math
Z(h)=e^{C_\theta}K(f,g),\quad
Z(R_+h)=e^{C_\theta}K(f,f),\quad
Z(R_-h)=e^{C_\theta}K(g,g).
```

All factors cancel in Cauchy–Schwarz, even if `b<0`. This is the complete
correction, with no new hypothesis. It also explains why different
reflections may use different gauge fixings.

For a separate normalization check of IR, write `L=-Delta`. Differentiating
GD gives, for every real sheet test `h`,

```math
\mathbb E\!\left[\langle P,Lh\rangle^2\right]
\le \frac1\beta\langle h,Lh\rangle.
```

On a nonzero real Fourier eigenspace, `L=lambda I`, `lambda=2E(p)`.
Dividing by `lambda^2` gives the covariance-form upper bound
`1/(beta lambda)=1/(2 beta E(p))`. An order-two character has one real
component; other characters have the cosine/sine pair. Normalizing the
real test in either space yields exactly line 144.

## Step 7: consumption by D2

The following line numbers in the first column are in `gap-d2-inputs.md`.
The middle column identifies the actual consumer in `gap-tiltproof-max.md`.

| Source line | Consumer | Verdict and disposition |
|---|---|---|
| 155 | D2 204–207, tool 1 | HOLDS AFTER CORRECTION. Use the abstract RP kernel and the constant accounting above. A Wilson-only citation is insufficient for this modified slab. |
| 156 | D2 205–207, tool 2 | HOLDS. The constant crossing-shift version follows from RP; the full GD proof supplies the needed iteration. |
| 157 | D2 216–222, 5.2 | HOLDS AFTER CORRECTION. The nonconstant crossing terms have nonnegative coefficients. D2's literal “every plaquette” at 219–220 must except the constant layer-0 time plaquettes, already identified at source line 77. Absorb them into the half-weights. |
| 158 | D2 224–226, 5.3 | HOLDS AFTER CORRECTION. Corrected F5 proves GD. D2's definition drops the sheet constant `beta N_b`, whereas Setting S retains it; this common positive factor cancels in `Z(h)/Z(0)`. |
| 159 | D2 226–227 | HOLDS. The maximum already gives `E X=0`, hence `E X^2=Var X`. One need not assume the stronger statement `E P=0`. |
| 160 | D2 227–228 | HOLDS with torus momenta understood modulo `2 pi`. IR's two cases cover all nonzero characters. |
| 161 | D2 229 | HOLDS as a conditional passage. At fixed `S`, the expression is a finite sum of bounded continuous expectations. Convergence of the two-slice marginals, supplied by 5.1, suffices. That convergence is not newly proved here. |
| 162 | D2 235–236, 5.5 | HOLDS. PT supplies the nonnegative cross covariance for `b>=0`. |
| omitted between 162 and 163 | D2 237–238 | HOLDS AFTER CORRECTION. Preserve row 979's existing normalization correction: use `A^(-1/2) cos(p.y)e` when `p` is an order-two character; otherwise use `(2/A)^(1/2) cos(p.y)e`. The former also gives the zero-mode convention. |
| 163 | D2 240, finite subgroups | HOLDS for these imported tools. Left/right invariance of normalized counting measure replaces Haar, and the same quaternion features apply to Q_8 and 2T. The theorem's additional isotropy/irreducibility input is not proved by Steps 4–6. |
| 165 | aggregate “first failing line: none” | HOLDS AFTER CORRECTION for the RP/GD/PT/IR implications only. The literal kernel equality needs the constant correction. It does not support the separate T3 claims, and it does not check all of D2. |

The exceptional-mode correction is prior work, not a new finding:
`gap-tiltproof-check-opus.md:91` already states it. Directly,
`sum_y cos^2(p.y)=A` for order-two characters and `A/2` otherwise.
The old vector therefore has norm `sqrt(2)` in the exceptional case.
After the recorded normalization, equal slice laws and PT give

```math
\operatorname{Var}(s^{-1}f(x)+s'^{-1}f(w))
\ge (s^{-2}+s'^{-2})\operatorname{Var}(f(x))
= (s^{-2}+s'^{-2})\widehat G^e(p),
```

using D1's zero mean for the zero mode. No assertion about the floating
lattice sums is needed.

## Disposition

Checked line by line by Codex (gpt-6-astra, xhigh), from another provider.
The first unsupported actual-model inference is the existential benchmark
claim at line 42; the explicit false equality is at line 44.
Lines 36–38 only give a test in a linearised class. They do not discharge
the gauge-invariant BR requirement.

RP and PT hold. GD and IR hold with the explicit constant bookkeeping
correction and the finite-torus momentum convention. These supply D2's
specified finite-slab inputs. Preserve the already known normalization
correction in its 5.5. The broad summary at lines 171–172, 179 and 181
must not describe T3 or N2 as confirmed by this check.

No source note, rule, registry, FINISH row, status or audit record was edited.
No numerical run, enumeration, formal verification or new research attack
was performed. D2 5.1, 5.4 and its floating lattice sums were not rebuilt.
The report is the only output; downloads remain in
`/tmp/sa-gap-d2-inputs-check-astra.LSrdx0`.

RESULT: FAILS for Step 2's confirmation of T3/N2 (unsupported benchmark at L42; false Gaussian identity at L44); HOLDS for RP and PT; HOLDS AFTER CORRECTION for GD/IR and their D2 consumption (retain constant plaquettes, torus momentum convention, and row 979's mode normalization). Research check only; no status granted.

# Block 194 adversarial check: the `(m,c)` generality package

Date: 2026-08-25  
Status: **COMPLETE — REFUTED AS A GENERAL POSITIVITY PACKAGE AND REFUTED LITERALLY AT C1; all narrower exact invariances are reported below**

## Exact target contract

- Width/sign/Hodge: `T = 16`, wrap-edge antiperiodic sign, `shear_hodge(c,1)`.
- Required fresh fixtures: `(m,c)=(1/2,1/3)` and `(2/3,1/5)`.
- Required claims: C1--C4 exactly as dispatched; P1 uses at least two additional admissible rational points; P2 hunts an admissible exact counterexample; P3 reports exact traces and scale ordering/monotonicity over five grid points.
- Arithmetic restriction: SymPy exact `Rational`/`QQ` only. `nsimplify` is forbidden and will not be used. Floating approximations, if any are printed later for readability, are non-authoritative readings of exact results.
- Refutation rule: one exact matrix residual, polynomial mismatch, sign/discriminant failure, or admissible counterexample defeats the corresponding leg.

## Construction authority and provenance

The restricted construction packet is the landed b190/b191/b192 chain at repository `HEAD afb66fc43c8858cc6a1d4cf943a14085e45be3f1`:

- b190 width-family note SHA-256 `f9392f362084d2e8a407d8bde1b7ac555eda9884504efe501630bd011f3702e4`;
- b191 boundary-volume note SHA-256 `4f0a18d2254a1cd8d65dd0915506e83a7f7f123d648e925d3213cc06b500b7ec`;
- b192 hybridization-cutoff note SHA-256 `6acb524bb65d262ec441f20da5835cb1b76b2549467b3a5969ba080ee9e77d3e`.

No audit-ledger rationale, downstream summary, or block-194 candidate implementation is used as evidence.

## Executive verdict

- **C1:** the two fresh-point primitive factors, positivity, two-scale separation, and `[W,U]=0` are confirmed, but the displayed equalities are literally false because the monic characteristic polynomials require exact scalar denominators.
- **C2, C3, C4:** confirmed exactly at both fresh points.
- **P1:** three new points were run. The large-m control `(5,1/4)` passes the substantive C1--C3 package; `(1/20,9/10)` and `(5,4/5)` refute positivity while preserving palindromicity, commutation, parity, and the window-cell invariance.
- **P2:** a 204-point rational hunt found 192 fully admissible points; positivity failed at 98 of them. No parity, window, palindromicity, or commutant failure was found in that set.
- **P3:** at fixed `m=1/2`, `theta_heavy/theta_light` is rigorously strictly increasing on the five-point `c` grid reported below.

## Results

### Dispatched fresh fixtures: exact reconstruction

The independent downstream construction uses the displayed formula

`B(c,v) = diag(v, v g(c)^-1, 1/v)`, `g(c)=[[1,c],[c,1]]`,

and independently rebuilds the `64 x 64` action and inverse over `QQ`. At both points `nnz(Ps Q Ps - Q^T)=0`.

#### `(m,c)=(1/2,1/3)`

- **C1 REFUTED LITERALLY; intended primitive-factor reading PASS.** SymPy's characteristic polynomial is monic, so the exact identity is
  `charpoly(W) = (233 z^2 - 690 z + 233)^2 (739 z^2 - 7258 z + 739)^2 / 29648362969`,
  not the unnormalized integer product stated in C1. Independently, `product/charpoly(W)=29648362969` and the resulting polynomial residual is exactly zero. The two displayed quadratics are nevertheless exactly the primitive `QQ` factors with multiplicity two. Both are palindromic. Their discriminants are respectively `258944` and `50494080`, both positive; their coefficients obey `a>0`, `-b>2a`, so every root is real and positive; and constant/leading is exactly `1`, so roots occur in reciprocal pairs. The exact traces `2 cosh(theta)` are `690/233` (light) and `7258/739` (heavy). They are distinct because `7258*233 - 690*739 = 1181204 != 0`. Finally `nnz([W,U])=0` entrywise.
- **C2 PASS.** The primitive degree-eight characteristic-polynomial coefficient vectors at `t0=2` and `t0=3` are identical.
- **C3 PASS.** For the reflected volume profile with `v=4/5` on positive anchors `{2,3}`, `nnz(W_bump(t0=5)-W_1(t0=5))=0`; this is whole-matrix invariance, not merely isospectrality.
- **C4 PASS.** At `t0=4`,
  `(233 z^2 - 690 z + 233)^2 (739 z^2 - 7258 z + 739) (1098595 z^2 - 9936202 z + 1011691)`.
  Thus the multiplicities are exactly `(heavy)^1(light)^2(boundary)^1`. The boundary factor is non-reciprocal because `a-c=86904 != 0`; its discriminant is the positive integer `94282355488224`, with `a>0`, `-b>0`, `c>0`.

#### `(m,c)=(2/3,1/5)`

- **C1 REFUTED LITERALLY; intended primitive-factor reading PASS.** The exact monic polynomial is
  `charpoly(W) = (17099 z^2 - 159050 z + 17099)^2 (21709 z^2 - 81434 z + 21709)^2 / 137791066603200481`.
  Independently, `product/charpoly(W)=137791066603200481` with zero polynomial residual. The displayed integer quadratics are exactly the primitive `QQ` factors. Their discriminants are respectively `24127399296` and `4746373632`, both positive; both factors obey `a>0`, `-b>2a`, and constant/leading `=1`. The exact traces are `159050/17099` (heavy) and `81434/21709` (light), distinct because `159050*21709 - 81434*17099 = 2060376484 != 0`. Also `nnz([W,U])=0`.
- **C2 PASS.** The exact characteristic polynomials at `t0=2` and `t0=3` coincide.
- **C3 PASS.** `nnz(W_bump{2,3}(t0=5)-W_1(t0=5))=0` entrywise at `v=4/5`.
- **C4 PASS.** At `t0=4`,
  `(17099 z^2 - 159050 z + 17099) (21709 z^2 - 81434 z + 21709)^2 (209535268 z^2 - 1901760850 z + 204452743)`.
  This is again `(heavy)^1(light)^2(boundary)^1`. The boundary factor is non-reciprocal because `a-c=5082525 != 0`; its discriminant is `3445334089401362004 > 0`, with `a>0`, `-b>0`, `c>0`.

**Fresh-point verdict:** the intended primitive-factor/spectral package passes every substantive matrix and root leg at both points, but C1's two displayed equalities are false as literal equalities by the exact scalar contents above. The repair is narrow: write `charpoly(W) \propto ...` with primitive `QQ` factors, or include the displayed denominators.

### P1 — three new points, per leg

All selected points are outside the forbidden five-point set. Exact `QQ` inversions succeeded for all uniform and bumped actions (`rank(Q)=rank(Q_bump)=64`) and for every required core Gram (`rank(K_c)=8`), so all are admissible under the dispatch's stated criterion.

#### Extreme small-m / near-Hodge-edge point `(m,c)=(1/20,9/10)`

- **C1 analogue FAILS (substantively).** At `t0=3`,
  `charpoly(W) = [(727925 z^2 + 4222711 z + 727925)^2 (1418125 z^2 - 2842311 z + 1418125)^2] / 1065619837563410400390625`.
  Both primitive factors are palindromic and `nnz([W,U])=0`, but the first has discriminant `15711788967021>0`, product of roots `1`, and root sum `-4222711/727925<0`. Hence it has two distinct **negative** real reciprocal roots. The other factor remains positive: discriminant `34417758221>0` and `2842311>2*1418125`. Spectral positivity, and therefore the claimed positive two-scale reading, fails exactly.
- **C2 analogue PASS.** Exact `t0=2` and `t0=3` characteristic polynomials coincide.
- **C3 analogue PASS.** For bump `{2,3}` at `v=4/5`, `nnz(W_bump(t0=5)-W_1(t0=5))=0`, while `nnz(K_bump-K_1)=64`; the invariance is a nontrivial quotient cancellation.

#### Extreme large-m point `(m,c)=(5,4/5)`

- **C1 analogue FAILS (substantively).** At `t0=3`,
  `charpoly(W) = [(2551 z^2 + 24954 z + 2551)^2 (2789 z^2 - 24478 z + 2789)^2] / 50619511038121`.
  The first reciprocal factor has discriminant `596671712>0` and root sum `-24954/2551<0`, so its two roots are distinct, real, reciprocal, and strictly **negative**. The second remains positive (`568058400>0`, `24478>2*2789`). Also `nnz([W,U])=0`.
- **C2 analogue PASS.** Exact `t0=2`/`t0=3` parity independence survives.
- **C3 analogue PASS.** The bump `{2,3}`, `v=4/5`, again gives `nnz(W_bump(t0=5)-W_1(t0=5))=0`, with `nnz(K_bump-K_1)=64`.

#### Large-m control point `(m,c)=(5,1/4)`

- **C1 analogue PASS modulo the same explicit monic normalization issue.** At `t0=3`,
  `charpoly(W) = [(313 z^2 - 100570 z + 313)^2 (1361 z^2 - 97222 z + 1361)^2] / 181470036049`.
  Both factors are palindromic and squared. Their discriminants are `10113933024` and `9444708000`; `100570>2*313` and `97222>2*1361`, so all four distinct scale roots are positive and reciprocal. The exact traces are `100570/313` (heavy) and `97222/1361` (light), distinct because the cross-product difference is `106445284>0`. Also `nnz([W,U])=0`.
- **C2 analogue PASS.** Exact `t0=2` and `t0=3` characteristic polynomials coincide.
- **C3 analogue PASS.** The `{2,3}` bump at `v=4/5` gives `nnz(W_bump(t0=5)-W_1(t0=5))=0`, while the core Gram changes in all `64` entries.

### P2 — boundary hunt: exact counterexamples found

P2 succeeds: the two P1 points above are both admissible exact counterexamples to the positive-spectrum leg. The cleanest boundary witness is `(1/20,9/10)`:

- construction denominators are nonzero (`1-c^2=19/100`), `rank(Q)=64`, and required `rank(K_c)=8`;
- the deep polynomial remains palindromic and parity-independent and still commutes with `U`;
- nevertheless `(727925 z^2 + 4222711 z + 727925)` has two distinct negative reciprocal roots by the exact discriminant/product/sum test above.

Thus palindromicity, `[W,U]=0`, parity independence, and the window-cell cutoff do **not** imply spectral positivity throughout admissible `(m,c)` space. `(5,4/5)` supplies a second independent exact witness of the same failure class, while `(5,1/4)` shows that large mass alone does not force failure.

#### Searched set and census

The independent boundary seat searched the full Cartesian set

- `M = {1/100, 1/50, 1/20, 1/10, 1/5, 1/3, 1/2, 2/3, 1, 2, 5, 10}`;
- `C = {-99/100, -9/10, -3/4, -1/2, -1/5, 0, 1/5, 1/3, 1/2, 3/4, 9/10, 19/20, 99/100, 101/100, 6/5, 3/2, 2}`.

This is `12*17=204` exact rational candidates. The 12 points with `c=2` were excluded because baseline `Q` is exactly singular. The remaining `192` points had invertible baseline and bumped `Q` and all required invertible core Grams. On those 192:

| leg | exact census |
| --- | ---: |
| deep monic characteristic polynomial palindromic | `192/192` |
| `[W,U]=0` | `192/192` |
| `charpoly(W,t0=2)=charpoly(W,t0=3)` | `192/192` |
| bump `{2,3}` window invariance at `t0=5` | `192/192` |
| all roots positive real | `94/192` |
| positivity failure | **`98/192`** |

A separate exact witness from that sweep is `(m,c)=(1/100,3/4)`:

`charpoly(W) = [(57536 z^2 + 5175457 z + 57536)^2 (1322536 z^2 - 2645457 z + 1322536)^2] / 5790210286399072239616`.

The first factor has `Delta=26772113593665>0`, product `1`, and exact roots
`(-5175457 +/- sqrt(26772113593665))/115072`, both strictly negative. The second has `Delta=2036853665>0` and a positive reciprocal pair. Every one of the 12 searched masses at `c=3/4` fails positivity with one negative reciprocal pair. Four admissible points, `(m,c)=(1/2,+/-1/2)` and `(2,+/-1/2)`, have one palindromic quadratic split over `QQ` into reciprocal linear factors; the monic polynomial remains palindromic, so irreducible-factor degree alone is not a valid checker.

### P3 — scale ordering and five-point monotonicity grid

Use the dispatched fresh point `(1/2,1/3)` and hold `m=1/2` fixed while varying only
`c in {1/5, 1/4, 1/3, 2/5, 9/20}`. Following the b190 reading convention, define `theta_1=theta_heavy`, `theta_2=theta_light`, and `T=2 cosh(theta)=-b/a` for a primitive palindromic factor `a z^2+b z+a`.

| `c` | exact `T_heavy` | exact `T_light` | numerator certifying `T_heavy-T_light>0` |
| ---: | ---: | ---: | ---: |
| `1/5` | `63258/7619` | `28762/9629` | `389973604` |
| `1/4` | `6223/709` | `575/193` | `793364` |
| `1/3` | `7258/739` | `690/233` | `1181204` |
| `2/5` | `12922/1171` | `6298/2141` | `20291044` |
| `9/20` | `3084847/250021` | `1534683/525061` | `1236029872324` |

Every trace in the table is strictly greater than `2`. Since `acosh(T/2)` is positive and strictly increasing for `T>2`, the positive cross-product certificates prove `theta_heavy>theta_light>0` at every grid point.

The adjacent exact trace differences as `c` increases are:

| step | `Delta T_heavy` | `Delta T_light` |
| --- | ---: | ---: |
| `1/5 -> 1/4` | `2563115/5401871 > 0` | `-14391/1858397 < 0` |
| `1/4 -> 1/3` | `547125/523951 > 0` | `-805/44969 < 0` |
| `1/3 -> 2/5` | `1050240/865369 > 0` | `-9856/498853 < 0` |
| `2/5 -> 9/20` | `381584475/292774591 > 0` | `-21077875/1124155601 < 0` |

Therefore `theta_heavy` strictly increases and `theta_light` strictly decreases at every step. Because both are positive, `theta_1/theta_2 = theta_heavy/theta_light` is **rigorously strictly increasing on this five-point discrete `c` grid**. This is not a theorem of continuous monotonicity between grid points and not a physical dispersion theorem.

## Method, independence, and exactness controls

- The main probe independently assembles the `T=16` wrap-edge kernel, grade projectors, `d_K`, `Ps`, closed-half restricted raising set, glue, quarter-cell Hodge sum, `Q`, `G`, `K_c`, `L_2`, `W`, and `U`. It imports no function or expected coefficient table from the b190/b191/b192 runners.
- The displayed shear formula was compared entrywise with the landed Block-105 `shear_hodge(c,v)` at both `v=1` and `v=4/5` for all 17 shear values in the P2 grid: **34 exact matrix comparisons, zero mismatches**.
- Matrix inversion and rank use `DomainMatrix` over `QQ`; characteristic polynomials and factorization are exact SymPy polynomial operations. No floating value or tolerance enters any construction, comparison, root-sign proof, or monotonicity proof.
- The same-family clean legs C1--C4 received a separate fresh-context reconstruction that did not read this findings file; it independently reproduced the factors, residuals, scalar-normalization defect, C3's nontrivial Gram motion, and C4 boundary factors.
- Independence limit: both implementations are code-independent from the landed runners but remain CAS-dependent on SymPy's exact linear-algebra and polynomial primitives.

## Final adversarial conclusion

The proposed package does **not** survive as written or as a general positivity claim. C1 omits the exact scalar content required by a monic characteristic polynomial. More materially, admissible rational points with negative reciprocal monodromy pairs are abundant in the searched grid (`98/192`), including the exact interior-Hodge witness `(1/100,3/4)` and the extreme P1 witness `(1/20,9/10)`.

The strongest surviving statement is narrower: at the two dispatched fresh points, the stated primitive factors and all spectral sign/separation claims are correct; C2, C3, and C4 pass exactly; and across all 192 admissible searched points, palindromicity, `[W,U]=0`, parity independence, and the `{2,3}` window-cell invariance survive. Those invariances are substantially more general in this finite search than positivity is.

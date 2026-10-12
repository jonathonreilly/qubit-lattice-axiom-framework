# Independent review of the frozen composition packet

2026-10-12. **Mathematical source review: PASS under the declared hypotheses.**
I found no material error in the global CHSH proof, finite-visibility threshold,
explicit quantum observables, Legendre obstruction or counting algebra.
One nonblocking reproduction issue is retained below. This review does not
validate the parent experiment, adopt the conditional pair law, certify a
canonical audit runner, or confer retained status.

## Source identity and reading scope

The exact V1 freeze is `composition/RESULTS_FREEZE_V1.json`, SHA256
`35586385663854a0ab1b23ce9007512b3f50cc729310307b31a1f176b026f413`.
All ten listed source artifact hashes and byte counts match. The full
derivation, results prose, calculation code, input freezes and manifests were
read. Both large numerical JSON files were parsed in full; every stored
directional witness and every visibility table were independently evaluated.

| Artifact in `../composition/` | SHA256 |
|---|---|
| `DERIVATION.md` | `a09ef7b88399d8555c17c280e5cbdf214c716d746ea7f7866fa6a5a3f28629a8` |
| `RESULTS.md` | `461071a39327e59cd6f3aee0d163cea09c5c3e930ca8844d55ec6d71acb22b9b` |
| `COMPUTATION_RESULTS.json` | `6e44ab256920ccc63097fedfff7752008b5561c1cc6a7df1430e72a2381eb53b` |
| `finite_directions.json` | `80312cabadf10f164b020def0b98f8291115adb69585ecca3e705f1166eacc3c` |
| `composition_check.py` | `524c0618e4347d85cdaec7279f62e0895e04cc2f5de65a8e88e5a51a089b78d2` |

The authority/context revision is `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`.
The framework's premises were read earlier in this same review session; none
supplies the alternative setting-conditioned law or the additional common
Hilbert realization hypothesis. The full parent pair-law derivation was read,
and its source-error/fit limitations checked against the parent results.
Thirteen imported-source, parent-input and inspection-render hashes match
the author's manifest. Berg–Porcu v2, PDF page 8, Theorem 2.1 and equation (18)
were read; original Tsirelson 1980 pages 93–94 were visually inspected from
the pinned renders. Both imported results are used within their hypotheses.
The unsuccessful original Schoenberg retrieval is correctly excluded as
proof evidence.

The author conclusions were visible before my independent implementation.
This is source checking, not a blind prediction or independent claim of
historical novelty. No empirical input was fitted or reinterpreted.

## Global CHSH proof

Write `g(theta)=f_k(cos theta)`. An independent equivalent form is

```
g(theta) = [(pi-theta) exp(2k cos theta) - theta]
           / [(pi-theta) exp(2k cos theta) + theta].
```

It is continuous, decreasing on `[0,pi]`, and satisfies
`g(pi-theta)=-g(theta)`. On `[0,pi/2]`, put `u=1-2theta/pi` and
`q=atanh(u)+k cos(theta)`. Differentiating `g=tanh(q)` gives
`g''=(1-g^2)[q''-2g(q')^2]`. Substitution yields exactly the four nonpositive
terms in the author's formula because `g>=u>=0` and `k>=0`. Concavity extends
to both endpoints by continuity. This includes the linear `k=0` control.

For arbitrary unit settings, the path
`a1 -> b0 -> a0 -> b1 -> -a1` has total spherical length at least `pi`, and
its four `g` terms equal the signed CHSH sum. Componentwise shortening to
total length `pi` enlarges that sum; the shortened lengths need not form an
actual path because this is an upper-bound relaxation.

If all shortened lengths are at most `pi/2`, Jensen gives `4g(pi/4)`.
Otherwise exactly one is `z>pi/2`; with `3alpha=pi-z`, Jensen on the other
three gives `3g(alpha)-g(3alpha)`. Its derivative is
`3[g'(alpha)-g'(3alpha)]>=0`, so it is at most `3g(pi/6)`. Finally concavity
between `pi/6` and `pi/2`, where `g(pi/2)=0`, gives
`3g(pi/6)<=4g(pi/4)`. Thus the proof does cover the greater-than-`pi/2`
branch. The standard coplanar settings attain equality, and oddness supplies
the opposite sign. Therefore, exactly for every `k>=0`,

```
max |CHSH| = 4 tanh[atanh(1/2) + k/sqrt(2)].
```

The decimal prospective `k` and the exact quantum-calibration definition are
correctly distinguished. Decimal rounding does not turn this calculation into
an observed CHSH violation. The global conclusion rests on the proof above,
not the author's optimization or my finite scans.

## Gram obstruction and finite visibility

Under common projective quantum observables and exact anticorrelation,
`||(A_a+B_a)psi||^2=0` implies `B_a psi=-A_a psi`. Realifying the state
vectors then makes `f_k(a dot b)` a unit-vector Gram kernel. This establishes
the necessary PSD condition without assuming a particular local dimension.
The pairwise fair no-signaling tables alone do not establish that condition.

For the three fixed directions, `h=f_k(1/2)` and
`G=(1+h)I-hJ`. The uniform eigenvalue is `1-2h`, so the exact witness fails
precisely at `k>log(3/2)`. The tetrahedron coefficient and threshold are
correct. At `k=0`, the sign-function inner-product construction proves PSD.
For the full sphere, the coefficient normalization `(2ell+1)/2` agrees with
the S2 specialization of the pinned Schoenberg theorem.

The proof that `a3'(k)<0` is valid: `cP3(c)` changes sign once and integrates
to zero, while `1-f_k(c)^2` strictly decreases in `c`. Subtracting its value
at the sign change gives a strictly negative integral. Differentiation and
the `k->infinity` limit are dominated. The endpoints `a3(0)=7/64` and
`lim a3=-7/8` give a unique root. Its numerical location and the unverified
interval backend are honestly labeled. The midpoint error bound follows from
the displayed Lipschitz constant; the prospective interval is strictly
negative. No all-direction PSD conclusion is claimed from positive finite
samples below the root.

For `C=-VG` with `V<1`, the same-vector Gram inference would be invalid. The
author correctly replaces it with a bipartite factorization. The actual
candidate has `1/3<=h<1`; on this domain,

```
gamma2(G) = ||G||_* / 3 = max[1,(1+4h)/3].
```

Necessity follows from
`||XY^T||_* <= ||X||_F ||Y||_F <= 3 max_i||x_i|| max_j||y_j||`.
For `h>1/2`, `P=J/3`, `S=I-2P`, and
`|G|=(1+h)(I-P)+(2h-1)P` commute. The factors `L=|G|^(1/2)` and `SL`
have cross product `G` and identical squared row norm `t=(1+4h)/3`, attaining
the lower bound. For `h<=1/2`, `G` is PSD with unit diagonal and `t=1`.
Adding two mutually orthogonal slack coordinates gives unit vectors whenever
`Vt<=1`. Hence the sharp finite-table criterion is

```
C=-VG is quantum-feasible  <=>  V <= 1/max[1,(1+4h)/3].
```

The criterion concerns unrestricted finite binary quantum observables. It
does not assert feasibility for a preassigned set of physical spin-1/2 Pauli
observables along the geometric directions, or for the entire angular family.
The source explicitly preserves those distinctions.

## Explicit observables and measured functional

The five supplied gamma matrices are Hermitian, traceless and obey
`{Gamma_l,Gamma_m}=2 delta_lm I4`. Thus unit vectors give
`A_i=x_i dot Gamma`, `B_j=-(y_j dot Gamma)^T`, with squares `I4`.
On `Phi4`, the identity
`<A tensor B>=Tr(A B^T)/4` gives exactly `-x_i dot y_j=-VG_ij` and zero
marginals. Projectors `(I4 +/- A_i)/2` and `(I4 +/- B_j)/2` therefore produce
all four stated outcome probabilities. This is an actual finite quantum
realization; local dimension four is sufficient, not asserted minimal.

I also constructed the observables independently using spectral-coordinate
factors and a different Clifford basis,

```
(sigma_x tensor sigma_x, sigma_x tensor sigma_y,
 sigma_x tensor sigma_z, sigma_y tensor I2, sigma_z tensor I2).
```

Direct calculations on the 16-dimensional entangled state, including the
joint outcome projectors, agree. An explicit threshold example with real and
imaginary parts of all six observables is retained in the review result JSON.

The functional uses the orthogonal matrix `S=I-2J/3`:
`B=-sum S_ij C_ij`. Frobenius Cauchy–Schwarz gives `|B|<=3` for quantum
correlation vectors, including contractive binary observables. The same bound
holds classically: the two types of deterministic three-sign patterns give
`||Sb||_1=3` and `7/3`. The candidate value `V(1+4h)` crosses exactly the
sharp threshold above. This statement needs the stipulated common quantum
experiment, not a visibility estimate or exact anticorrelation.

The equal-cell variance, optimal-allocation variance, visibility derivative
and systematic coefficient `sum |S_ij|=5` are correct. These are conditional
counting forecasts, not power calculations, observed significance, or
complete experimental budgets. Endpoint verification, source stability,
setting/readout calibration, loss and nuisance uncertainty remain required.
The source does not promote its parent's problematic count-error profile into
an empirical exclusion.

## Execution evidence and one reproduction finding

An unmodified copy of the author script, with its two frozen inputs, ran in
the assigned runtime area in 5.19 seconds, using approximately 88 MB peak
child RSS. All result fields reproduce exactly except timestamps; direction
bytes reproduce exactly. Original author outputs were not overwritten.

The separate [independent checker](independent_checks.py) passes **6 check
families, zero failed**. It covers all 252 frozen eigenvector witnesses, all
35 visibility cases and 16 feasible stored constructions, all odd Legendre
coefficients through 31, and 15 additional quantum constructions including
visibility-boundary cases. Kernel evaluation uses the exponential form and
`atan2(cross,dot)` angles; Legendre integration uses the original `c` variable;
operator probabilities use direct state/projector products.

The largest frozen witness residual is `3.17e-15`. Independent adaptive
Legendre coefficients differ by at most `3.34e-14`; direct 60-digit `a3`
integrals agree to about `1.95e-62`. The largest stored-table/operator error
is `4.45e-16`. The CHSH relaxation scan includes 12,096 length quadruples with
a segment above `pi/2` for each of six selected parameters; no excess beyond
floating rounding occurs. These finite checks do not replace the proofs.

Six intentional result corruptions (CHSH value, `a3`, gamma2, probability,
quantum vector and directional witness) each fail their intended independent
check with nonzero exit status. Original and modified data, all stdout/stderr
and exact receipts remain preserved. There were no failed unmutated science
runs. Python 3.12.8, NumPy 2.4.1, SciPy 1.17.0 and mpmath 1.3.0 were used
with numerical threads limited to one.

**Reproduction finding (nonblocking for the mathematics):**
`composition_check.py:34-35` uses `write_text` beside the script;
lines 165 and 240 overwrite `finite_directions.json` and
`COMPUTATION_RESULTS.json`. The direct reproduction command in
`RESULTS.md:160` therefore changes frozen output bytes and invalidates V1
hashes, even though it leaves the freeze JSON itself unchanged. Minimal remedy:
instruct reproduction in a copied directory, or add a separate output-directory
argument when making a new portable version. Do not edit or restamp V1.
The script also retains a campaign path/expiry guard and produces calculation
records rather than an automatic PASS/FAIL assertion suite. Those are future
canonical-runner packaging concerns; this review certifies neither portability
nor audit-runner readiness. The independent checker accepts explicit input and
output paths and does not expire.

All V1 author hashes still match at final confirmation. No source edit,
commit, push, empirical fit, audit action or new physical premise was made.
The mathematical source verdict is reusable only for the exact frozen packet
and stated scope; changed assumptions or source require affected review.

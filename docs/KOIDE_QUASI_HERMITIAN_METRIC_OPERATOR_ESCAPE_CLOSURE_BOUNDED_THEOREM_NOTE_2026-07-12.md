# Quasi-Hermitian Metric-Operator Escape Closure — Positive Metrics on the Circulant Generator Select Exactly the K-Tie; Arbitrary Signature Has Four, Not Two, Spectral-Pairing Loci; the Two-Slice Factor Inherits Metrics Only One Way and Leaves a Coarser Positive-Spectral Remainder (Bounded Theorem, rhalf block 11)

**Date:** 2026-07-12
**Claim type:** bounded_theorem (exact finite-dimensional metric-intertwiner
classification, counterclassification of a proposed two-branch theorem, and
bounded escape-table refinement). This source note does not adopt any premise
and does not edit any registry or data file.
**Primary runner:**
[`scripts/frontier_quasi_hermitian_metric_escape_2026_07_12.py`](../scripts/frontier_quasi_hermitian_metric_escape_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_quasi_hermitian_metric_escape_2026_07_12.txt`](../logs/runner-cache/frontier_quasi_hermitian_metric_escape_2026_07_12.txt)
(SCORECARD: PASS=17, FAIL=0)

> **Not claimed:** a derivation of `r = 1` or `r = 1/2`, any change to the
> equipartition/dial residual, a positive records-only reconstruction from an
> indefinite metric, identification of the supplied two-slice Schur factor
> with a stronger full physical transfer operator, or a universal result
> beyond the stated circulant/two-slice scope. **Claimed (bounded):** for
> `W = aI+bC+cC²`, a positive-definite Hermitian metric `η` satisfying
> `ηW=W†η` exists **iff** `W=W†`, exactly the K-tie. An invertible Hermitian
> metric of arbitrary signature exists **iff** the Fourier spectrum is closed
> under conjugation; this is a **four-locus** union — the tie, the block-10
> all-real branch `R₀`, and two additional phase-twisted branches `R₁,R₂` that
> `P` swaps with each other but not with `R₀`. Metrics lift forward to the
> supplied two-slice factor `A₂(W)=W²+¼I`, but not backward: the exact witness
> `W=(i/10)I` has no nonzero metric while `A₂=(6/25)I` is positive Hermitian.
> Therefore the requested quasi-Hermitian closure is **partial**: positive
> metric on `W` closes to the tie; indefinite/Krein reconstruction remains
> open on three transposition branches; an `A₂`-only spectral condition is
> still coarser. Negative norms and the absence of a positive records-only
> inner product are costs, not a textual Record-axiom violation.

## Role — the block-10 escape this executes

This block starts from the two-branch records-only OS result in
[`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
and tests only its open weaker-than-OS spectral/quasi-Hermitian route. Block 10
proved, at its stated records-only two-slice grade, that the OS Gram is
Hermitian on the union

```text
K-tie:    a real, c = conj(b),
all-real: a,b,c real,
```

with OS positivity on the whole tie and only a strip of the all-real branch.
Its escape table left *"a weaker-than-OS spectral-positivity condition for
emergent time"* open. The present question is narrower than re-running OS:

> Does replacing the positive OS form by a metric-operator intertwining
> condition close that escape, and if positivity of the metric is dropped,
> exactly what Krein-space remainder survives?

The answer delivered by the algebra is a correction to two proposed targets.
The positive-metric target is true. The proposed arbitrary-signature
two-branch target is false because it omitted two Fourier pairings. At the
matrix factor directly supplied by block 10, the proposed converse lift is
also false because `z → z²+¼` is not injective.

## Target correction record — algebra honored, not forced

1. **T1 survives.** Positive metric on `W` is equivalent to the K-tie.
2. **Proposed T2 is withdrawn.** Arbitrary signature is not the block-10
   two-branch union; it is the four-locus union derived below (checks 8–10).
3. **The proposed global zero-space statement is narrowed.** Both supplied
   off-union probes have zero intertwiner space, but a partial spectral match
   can leave a nonzero **singular** intertwiner outside conjugation closure
   (check 11). What fails everywhere outside the four loci is invertibility.
4. **T3 is one-way.** A metric for `W` is a metric for every real-coefficient
   polynomial in `W`, including `A₂`; the converse fails exactly (checks
   12–15).
5. **T4 is consequently a partial closure.** The honest surviving weakening
   is larger than the proposed all-real Krein remainder.

All exact probe values are certificates, not derivation inputs: the locus
classification is solved symbolically before the points are evaluated.

## Setup — Fourier-normal circulant and metric convention

Let

```text
C = [[0,1,0],[0,0,1],[1,0,0]],       C³=I,
W = aI+bC+cC²,
ω = exp(2πi/3),
λ_k = a+bω^k+cω^(2k),                k=0,1,2.
```

The unitary Fourier matrix `U` diagonalizes every member of the family:

```text
U†WU = Λ = diag(λ₀,λ₁,λ₂).
```

The inverse map, used rather than assumed by the runner (check 2), is

```text
a = (λ₀+λ₁+λ₂)/3,
b = (λ₀+ω²λ₁+ωλ₂)/3,
c = (λ₀+ωλ₁+ω²λ₂)/3.
```

Throughout, a **positive metric** means a positive-definite Hermitian matrix
`η>0`; an **any-signature metric** means an invertible Hermitian `η`, with no
positivity condition. Both obey

```text
ηW = W†η       equivalently       W† = ηWη⁻¹.
```

“Positive metric” does not by itself mean that the spectrum of the represented
operator is positive; it makes the operator Hermitian in the `η` inner
product. Where strict spectral positivity is used below, it is said
explicitly.

## T1 — positive metric

> **T1.** A positive-definite Hermitian `η` satisfying `ηW=W†η` exists **iff**
> `W=W†`, equivalently **iff** `a` is real and `c=conj(b)`.

### Positive metric forces real spectrum

Let `S=η^(1/2)`, the positive square root. Then

```text
H = SWS⁻¹,
H† = S⁻¹W†S = S⁻¹ηWη⁻¹S = SWS⁻¹ = H.
```

Thus `W` is similar to a Hermitian matrix and has real spectrum. The runner
also proves this without invoking a matrix-square-root routine. In the Fourier
basis, `η̂=U†ηU` remains positive, so every `η̂_kk>0`; the diagonal
intertwining equations are

```text
η̂_kk (λ_k-conj(λ_k)) = 2i η̂_kk Im(λ_k) = 0.
```

Therefore all three `λ_k` are real (check 4).

### Real spectrum is exactly the tie

Substituting

```text
a=ar+i ai, b=br+i bi, c=cr+i ci
```

into the three equations `Im λ_k=0` and solving gives uniquely

```text
ai=0, cr=br, ci=-bi,
```

i.e. `a` real and `c=conj(b)` (check 3). Equivalently, the inverse DFT sends
three real eigenvalues to real `a` and conjugate `b,c`. Conversely, the tied
`W` is Hermitian and `η=I` works.

At the supplied tied point

```text
(a,b,c)=(4/5, 3/10+i/5, 3/10-i/5),
```

the exact nine-real-variable solve has a three-dimensional Hermitian
intertwiner family and contains `I` (check 5).

### General all-real off-tie obstruction — requested minors proof

For `a,b,c` real with `b≠c`, the full Hermitian solution, not merely the
solution at the two probes, is

```text
η = [[x₇,x₃,x₅],
     [x₃,x₅,x₇],
     [x₅,x₇,x₃]],                    x₃,x₅,x₇ real.
```

Its leading minors are

```text
m₁ = x₇,
m₂ = x₅x₇-x₃²,
m₃ = -(x₃+x₅+x₇) Q,
Q  = x₃²+x₅²+x₇²-x₃x₅-x₃x₇-x₅x₇
   = ((x₃-x₅)²+(x₃-x₇)²+(x₅-x₇)²)/2 ≥ 0.
```

If `η` were positive definite, Sylvester would give `m₁,m₂,m₃>0`.
The first two inequalities force `x₅,x₇>0`. The third cannot use `Q=0`,
because that would give `m₃=0`; hence it forces

```text
x₃+x₅+x₇<0  =>  x₃<-(x₅+x₇)<0.
```

Consequently

```text
x₃²>(x₅+x₇)²>x₅x₇,
```

contradicting `m₂>0`. Check 6 proves the family and factorization symbolically
and reproduces its three-dimensionality at both supplied real points
`(4/5,3/10,1/2)` and `(1/2,-4/5,3/10)`. At `b=c` the all-real branch meets the
tie, so this off-tie obstruction no longer applies and `η=I` is available.

This does not conflict with block 10's positive **OS Gram** inside the
all-real strip. Positivity of the reconstructed records-only Gram and
positive-definiteness of a metric intertwining the one-slice generator `W`
are different conditions.

## T2 — any-signature metric

> **T2 (corrected).** An invertible Hermitian `η` satisfying `ηW=W†η` exists
> **iff** `spec(W)` is closed under complex conjugation as a multiset. For the
> three-mode circulant this is the union of **four** spectral-pairing loci, not
> the block-10 two-branch union.

### Necessity and sufficiency

Necessity is immediate from similarity:

```text
W†=ηWη⁻¹  =>  spec(W†)=spec(W),
spec(W†)=conj(spec(W)).
```

For sufficiency, conjugation closure permits an involution `π` of the three
spectral labels such that

```text
λ_{π(i)}=conj(λ_i).
```

Let `R_π` be its permutation matrix. Then

```text
R_π=R_π†=R_π⁻¹,
R_πΛ=Λ†R_π,
η_π=U R_π U†
```

is an explicit invertible Hermitian metric. On three labels an involution is
either the identity or one of exactly three transpositions. This exhausts the
loci, including multiplicity-degenerate intersections (check 8).

### The four loci

Write `b=br+i bi`, `c=cr+i ci`; every locus below also has `a` real.

| name | spectral pairing | exact coefficient condition | simple metric |
|---|---|---|---|
| tie | all `λ_k` real | `c=conj(b)` | `I` |
| `R₀` (all-real) | `λ₀` real; `λ₂=conj(λ₁)` | `bi=ci=0` | `P₀` |
| `R₁` (phase-twisted) | `λ₁` real; `λ₂=conj(λ₀)` | `bi=√3 br`; `ci=-√3 cr` | `P₁` |
| `R₂` (phase-twisted) | `λ₂` real; `λ₁=conj(λ₀)` | `bi=-√3 br`; `ci=√3 cr` | `P₂` |

The runner solves all three transposition conditions from the DFT rather than
hard-coding them (check 9). With the same physical basis as block 10, explicit
fundamental symmetries are

```text
P₀ = [[1,0,0], [0,0,1],  [0,1,0]],
P₁ = [[1,0,0], [0,0,ω²], [0,ω,0]],
P₂ = [[1,0,0], [0,0,ω],  [0,ω²,0]].
```

Each transposition metric has eigenvalues `(1,1,-1)`. Away from its
intersection with the tie, its paired spectrum is genuinely non-real; T1 then
shows that **every** admissible invertible metric is indefinite, even though a
different representative can reverse or redistribute signs.

### Additional-locus question — found two, not `P`-images of `R₀`

An exact `R₁` witness is

```text
(a,b,c) = (4/3, 1/3+i√3/3, -2/3+2i√3/3),
spec(W) = (1+i√3, 2, 1-i√3).
```

Swapping `b,c` gives an exact `R₂` witness with spectrum
`(1+i√3,1-i√3,2)`. Both lie off the tie and off the all-real branch, both have
three-dimensional Hermitian intertwiner families, and `P₁,P₂` intertwine them
exactly (check 10).

The block-10 inversion `P=P₀` sends `b↔c` and `λ₁↔λ₂`. It maps `R₁↔R₂` but
maps the all-real locus `R₀` to itself. Therefore neither phase-twisted locus
is a `P`-image of `R₀`. No further relabeled locus exists: the identity and
the three transpositions exhaust involutions on three labels.

### What “zero off the union” can honestly mean

In the Fourier basis every solution obeys the entrywise support rule

```text
η̂_ij (λ_j-conj(λ_i))=0.                 (2.1)
```

At each supplied generic off-union point,

```text
(4/5+i/10, 3/10+i/5, 1/2-i/10),
(1, 1/3+i/7, 1/3-i/5),
```

there is no ordered equality `λ_j=conj(λ_i)`. The exact real-linear system has
rank 9 and nullity 0, reproducing the supervisor probes (check 7).

Outside the four conjugation-closed loci, **no invertible** metric can exist.
It is nevertheless false that the full intertwiner vector space is zero at
every such point. For the exact spectrum `(1,2+i,3+2i)`, only the real mode
matches its conjugate; the Fourier projector onto that mode is a nonzero
rank-one Hermitian intertwiner. It is singular, the full space has dimension
one, and the spectrum is not conjugation-closed (check 11). Equation (2.1),
not a blanket zero claim, is the general result.

## T3 — two-slice transfer level

The authorized block-10 note and runner explicitly supply the matrix-valued
two-slice Schur/overlap factor

```text
A₂(W) = W²+¼I,
Z = det A₂ = det [[-W,-½I],[+½I,-W]].
```

Because `W` is Fourier-normal,

```text
U†A₂U = diag(τ₀,τ₁,τ₂),
τ_k = f(λ_k),                    f(z)=z²+¼.
```

Check 13 proves these identities symbolically. Check 12 calls the block-10
engine rather than rebuilding its Grassmann/Berezin machinery. At the supplied
tied point, both supplied all-real points, and both supplied generic complex
points, it verifies exactly that the Berezin partition equals `det A₂`; it
also reproduces the expected Hermitian/non-Hermitian records-only Gram split.

### The metric lift is forward

For any polynomial `p` with real coefficients,

```text
ηW=W†η
  => ηWⁿ=(W†)ⁿη
  => ηp(W)=p(W†)η=p(W)†η.
```

Thus every positive or indefinite metric for `W` is a metric for `A₂`. Check
14 verifies the same metric at exact points on the tie, `R₀`, `R₁`, and `R₂`.
This is the exact sense in which the `W` classification lifts to the two-slice
factor.

### The lift is not reversible

The map `f(z)=z²+¼` is not injective. Consequently `A₂` can lose precisely the
spectral information needed to reconstruct a metric for `W`. The simplest
exact witness is

```text
W=(i/10)I,
spec(W)=(i/10,i/10,i/10),
A₂=(6/25)I,
spec(A₂)=(6/25,6/25,6/25).
```

For `W`, the intertwining equation reads

```text
(i/10)η=(-i/10)η,
```

so `η=0`; there is not even a nonzero singular Hermitian intertwiner. For
`A₂`, the identity is a positive metric and the spectrum is strictly positive.
The reused block-10 engine independently gives

```text
Z=(6/25)³=216/15625
```

while the complete records-only OS Gram remains non-Hermitian (check 15).
Thus reality or positivity of this determinant/factor does not restore OS.

The complete factor-level metric criteria are correspondingly coarser:

- `A₂` has a positive metric **iff** every `τ_k` is real. Since `A₂` is normal,
  this is equivalent to `A₂=A₂†`, and `I` works. Here
  `τ_k∈R` means `λ_k²∈R`, i.e. each `λ_k` is real or purely imaginary.
- If strict factor spectral positivity is additionally demanded, a purely
  imaginary `λ_k=i y_k` is allowed exactly when `|y_k|<1/2`; real `λ_k` always
  gives `τ_k=λ_k²+¼>0`.
- `A₂` has an invertible any-signature Hermitian metric **iff** the multiset
  `{τ₀,τ₁,τ₂}` is conjugation-closed. This is the preimage, under the
  non-injective `f`, of the same four pairing patterns in `τ`-space and is
  strictly larger than the four `W` loci.

> **T3.** Quasi-Hermiticity of `W` passes to the supplied two-slice factor;
> quasi-Hermiticity or even strict positive spectrum of that factor does not
> pass back to `W` and does not imply a Hermitian OS Gram.

This note deliberately calls `A₂` the **matrix-valued two-slice factor**. The
authorized inputs do not supply a stronger full physical transfer matrix whose
operator identification could be checked here. Treating `A₂` as that stronger
object would be a new premise, named as a residual below.

## T4 — bounded consequence and escape-table update

> **T4 (honest consequence).** The weaker-than-OS quasi-Hermitian escape is
> only partly closed. If imposed on `W` with a positive metric, it selects
> exactly the tie. If metric positivity is dropped, three non-tied
> transposition branches survive as Krein-space candidates: the block-10
> all-real `R₀` branch and the two phase-twisted `R₁,R₂` branches. If imposed
> only on `A₂`, even a positive metric and strictly positive factor spectrum
> survive outside the `W` classification. Nothing here derives `r=1` or
> `r=1/2`.

The requested statement *"any-signature metric reproduces exactly the
block-10 union"* therefore cannot be retained. The block-10 union remains the
classification of its records-only **OS Gram**, because that construction has
the specific record symmetry `P=P₀`. An abstract metric-operator condition is
weaker: it also allows the different fundamental symmetries `P₁,P₂`.

### What the Krein weakening costs

On every non-tied part of `R₀,R₁,R₂`, a nonreal conjugate spectral pair is
present. T1 excludes any positive metric there; the explicit fundamental
symmetries have a negative direction, and the general all-real minors proof
shows the obstruction without relying on the simple representative. A Krein
reconstruction therefore has:

- negative-norm vectors;
- no positive records-only inner product supplied by `η`;
- no probability interpretation or physical Hilbert completion without an
  additional positive structure/quotient, neither of which is supplied here.

This cost is **not** described as a violation of the Record axiom. At claim
scope, [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says
verbatim:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

That text states additivity and the empty-record value, but no readout
positivity, norm positivity, or Hilbert-space axiom (check 16). The Krein route
is left **OPEN with a stated reconstruction cost**, not rejected by importing
positivity into the axiom.

### Escape enumeration inherited and refined

| route inherited from block 10 | block-11 disposition | reason / cost |
|---|---|---|
| a non-conjugating “reflection” | **BLOCKED (inherited)** | block 10's antiunitary OS reflection intrinsically conjugates coefficients; this block does not reopen it |
| a larger record subalgebra | **BLOCKED at the inherited orbit-clause grade** | only the block-10 P-odd data separate its `W` from `PWP`; no new registrable class is supplied |
| a modified / non-OS emergent-time construction | **GENUINELY OPEN (unchanged)** | no such construction is supplied here |
| the alternating `W,W†` measure | **UNLICENSED in the inherited time-homogeneous scope** | it is arrow-dependent and pre-inserts the conjugate, exactly as block 10 states |
| weaker-than-OS spectral/quasi-Hermitian condition on `W`, `η>0` | **CLOSED to the K-tie** | T1; it supplies no non-tied escape |
| same condition on `W`, invertible Hermitian `η` of any signature | **OPEN KREIN REMAINDER on `R₀∪R₁∪R₂`** | T2; negative norms and no positive records-only inner product |
| condition only on the two-slice factor `A₂` | **OPEN, strictly coarser** | T3; `(i/10)I` is an exact positive-factor counterexample |
| all-real branch inside the OS strip with a degenerate registered pattern | **OPEN only if the named non-degeneracy element is dropped (inherited)** | the non-degeneracy element remains a labeled comparator/premise and is never thresholded here |

Check 17 encodes the dispositions. The split of the former single
weaker-than-OS row is the block's actual escape-table deliverable.

## Literature precedent — terminology only

The positive metric-operator/quasi-Hermitian framework is standard; see
[A. Mostafazadeh, *Metric Operator in Pseudo-Hermitian Quantum Mechanics and
the Imaginary Cubic Potential*, arXiv:quant-ph/0508195](https://arxiv.org/abs/quant-ph/0508195).
It is cited as precedent and inspiration only. No classification, locus,
metric, minor, transfer-factor claim, or witness is imported from it; every
step used here is reproven by the finite-dimensional companion runner.

## Residual Atoms

1. **Which operator bears the proposed condition.** `W` and the supplied
   `A₂=W²+¼I` have inequivalent converse classifications. A stronger full
   physical transfer operator is not supplied in the authorized inputs;
   identifying one is an additional operator bridge.
2. **Physical licensing of a fundamental symmetry.** Algebra supplies
   `P₀,P₁,P₂`, but it does not select an indefinite metric as physical or
   license the phase-twisted `P₁,P₂` as record symmetries. Any such selection
   would be new structure.
3. **Krein-to-probability bridge.** The Record axiom has no positivity clause,
   but neither does it provide the positive quotient, superselection rule, or
   probability functional needed to turn negative norms into a positive
   reconstruction.
4. **Degenerate intersections.** The four closed loci overlap when spectral
   values become real or degenerate. The union theorem includes those
   intersections; signatures quoted as unavoidable apply to the genuinely
   non-tied portions.
5. **Inherited time-homogeneity and record grade.** The block-10
   time-homogeneous two-slice law and its P-even/orbit-clause record scope are
   consumed at that note's declared grade, not rederived or enlarged here.
6. **The per-cell equipartition/dial law.** Entirely untouched. This note
   classifies metric intertwiners; it does not derive or choose `r=1` or
   `r=1/2`.
7. **Finite circulant scope.** The theorem is for the normal three-mode
   `C₃` circulant and the matrix factor explicitly present in block 10. It does
   not classify nonnormal, interacting, higher-dimensional, or
   beyond-bilinear transfer constructions.

## What This Does Not Claim

- **Not** a derivation of `r=1` or `r=1/2`; no occupancy, weighting,
  equipartition, or reading-section rule is adopted. The dial residual is
  unchanged.
- **Not** the originally proposed two-branch arbitrary-signature theorem. Two
  additional phase-twisted loci are exact and cannot be suppressed by calling
  them `P`-images of the all-real branch.
- **Not** that every off-locus intertwiner vector space is zero. Only
  invertible metrics are excluded globally; singular partial-match solutions
  can remain.
- **Not** that an indefinite metric yields a positive physical inner product.
  It yields a Krein form with negative-norm directions.
- **Not** that the Krein cost violates the Record axiom. Positivity is absent
  from the quoted Record sentences.
- **Not** that positive metric means positive operator spectrum. The
  `A₂=(6/25)I` witness is chosen to satisfy the stronger strict positivity too,
  so the factor-level counterexample does not rely on that distinction.
- **Not** that `A₂` is a fully identified physical transfer operator. It is the
  matrix-valued factor exactly exposed by the supplied block-10 construction.
- **Not** a change to block 10's OS-Gram theorem. The new phase-twisted metrics
  classify a weaker abstract intertwining condition, not its P-even OS Gram.
- **Not** an empirical selection. No mass value or other comparator is
  consumed; the inherited non-degeneracy element remains labeled and never
  thresholded.
- **Not** a premise or registry change. The note and runner are a bounded
  theorem/counterclassification pair only.

## Consumed premises and supplied elements (claim scope)

- **Block-10 two-slice construction and escape table** —
  [`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md):
  the circulant `W`, Fourier eigenvalues, time-homogeneous two-slice kernel,
  `P` action, records-only OS result, exact probe points, and the open
  weaker-than-OS row. Those supplied elements are named rather than enlarged.
- **Block-10 exact engine** —
  [`scripts/frontier_records_only_os_reconstruction_2026_07_11.py`](../scripts/frontier_records_only_os_reconstruction_2026_07_11.py):
  imported directly by check 1 and reused for checks 12 and 15. Its 24 checks
  must pass before this runner proceeds.
- **Record axiom** —
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): the exact
  quoted readout sentences and no positivity addition; check 16 reads the
  Record section directly.
- **Literature precedent only** — Mostafazadeh `quant-ph/0508195`, cited above;
  no result is consumed as a proof premise.

## Reprove-and-cite ledger

- **Reproven here (runner):** import/re-execution of the complete 24-check
  block-10 engine; unitarity and invertibility of the DFT; Fourier
  diagonalization; `all λ_k real` iff the tie; the positive-metric diagonal
  argument; the three-dimensional tied probe; the general all-real
  intertwiner family and its exact minors contradiction; nullity zero at both
  supplied generic probes; necessity/sufficiency of conjugation closure;
  enumeration of all four involutions; coefficient-space solves for
  `R₀,R₁,R₂`; explicit phase-twisted witnesses and metrics; the `P` mapping;
  the partial-match singular counterexample; `A₂=W²+¼I` and its spectrum;
  exact block-10 engine values at all five supplied probes; forward polynomial
  lift; the exact `(i/10)I` converse failure, positive `A₂` spectrum, partition,
  and non-Hermitian OS Gram; the exact Record-section wording; the refined
  escape enumeration.
- **Cited at declared grade:** block 10 for its records-only OS theorem,
  inherited escape rows, supplied kernel, and probe data; the minimal-axiom
  memo for Record wording; Mostafazadeh for terminology/precedent only.
- **Hard-code guard:** symbolic DFT solves and general real-linear ranks produce
  the loci. Exact points are evaluated only after those derivations and serve
  as certificates/counterexamples; no comparator or fitted threshold appears
  on a derivation path.

## Verification

```bash
python3 scripts/frontier_quasi_hermitian_metric_escape_2026_07_12.py
```

Expected: 17 numbered `[PASS]` lines, declared-open `RESIDUAL` lines, a short
verdict-first T1–T4 summary, `ADDITIONAL-LOCUS: FOUND TWO`, and
`TOTAL: PASS=17 FAIL=0`. Exit code 0 iff `FAIL=0`.

Regenerate the runner cache with

```bash
python3 scripts/precompute_audit_runners.py --push-mode none --force \
  --runners scripts/frontier_quasi_hermitian_metric_escape_2026_07_12.py
```

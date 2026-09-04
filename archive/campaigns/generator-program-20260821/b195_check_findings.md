# Block 195 adversarial check: OS reconstruction descent no-go

Status: **complete — broad no-go refuted; narrow prefix obstruction confirmed**.

## Audit contract

- Construction authority: commit `e75ad9f499`, source note
  `docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md`.
- Primary fixture: `m = 9/20`, `c = 5/13`.
- Non-control fixture: `m = 1/2`, `c = 1/3`.
- Arithmetic policy: SymPy exact `Rational` / `QQ` only; no `nsimplify` and no floating-point inference.
- Refutation standard: actively seek a working construction that evades the proposed quotient obstruction, or an exact counterexample to its measurements.
- Scope: scratch adversarial findings only; no audit-ledger mutation, source repair, commit, or push.

## Incremental log

1. Freshness check completed. The local `audit-loop` skill differs from the
   current `origin/main` copy, so this check follows the complete current
   `origin/main` procedure. The N1--N8 no-go discipline and proof-search
   governance are being applied as adversarial methodology.
2. The shared worktree is dirty with pre-existing user/campaign files. They are
   left untouched. All computation and the sole requested artifact remain in
   this scratchpad directory.

## Exact target contract

- Let `X_A` be the coordinate span of all positive slices
  `A = {1, ..., T/2-1}` and let `K_AA` be its reflected Gram.
- For `D = {1, ..., dmax}`, let `K_AD` be the full-row, `D`-column restriction,
  `N_D = ker(K_AD)`, and let `S_2: X_D -> X_A` be the literal two-slice shift.
  Then the stated matrix `M2` is exactly `K_AA S_2`.
- The raw descent question is whether `S_2 N_D` is contained in
  `rad(K_AA)`, equivalently whether `M2 N_D = 0`.
- The theta-side representative question is the transpose condition
  `N_D^T K_DA = 0`.
- A failure of raw descent does **not** by itself rule out an operator obtained
  after choosing an injective eight-dimensional frame/section of the quotient.
  The latter is a distinct compression construction and is tested separately.

Forbidden weakenings: no floating-point rank, tolerance, fitted prefactor,
`nsimplify`, or substitution of a different Hodge/volume/sign convention.

Completion witnesses: exact ranks/nullities, exact nonzero tests, exact
residual-map ranks and row-slice supports, plus explicit algebraic quotient and
compression consistency identities.

## First exact pass: primary fixture

The independent reconstruction reproduces the displayed unit-volume Hodge
entrywise:

```text
B(5/13,1) = diag(1,169/144,169/144,1),
B[1,2] = B[2,1] = -65/144.
```

It also gives `rank(K_AA)=8` and `K_AA-K_AA^T=0` at both `T=16` and
`T=20`, confirming C1.

### Important measurement defect in C2's wording

The quoted violation counts are reproduced **only for SymPy's default
nullspace basis**. They are not invariants of the kernel. Exact basis changes
give the following at `T=16`:

| `dmax` | `dim N_D` | default-basis violations | `rank(M2|N_D)` | adapted-basis violations | possible all-violating basis |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 12 | 8 | 2 | 2 | 12 |
| 4 | 8 | 6 | 1 | 1 | 8 |
| 3 | 4 | 2 | 1 | 1 | 4 |

The adapted basis is exact: take pivot columns of `M2*N` followed by a basis
of `ker(M2*N)` pulled back through `N`. An all-violating basis is then obtained
by adding one violating adapted vector to every joint-null adapted vector.
Thus the invariant obstruction is `rank(M2|N_D)>0`, not “exactly X kernel
vectors violate.” This breaks C2 as a basis-independent measurement while
leaving the existential obstruction intact.

For all three `T=16` depths, the residual column-space support meets every
positive row-slice `{1,...,7}`. The theta-side residual is exactly zero.

## Executive verdict

**REFUTED AS STATED; a narrower prefix-domain obstruction survives.**

Three distinct conclusions must not be conflated:

1. C1 is exactly correct.
2. The seam-anchored prefix domains in C2 do obstruct raw `tau^2` descent, so
   the existential core of C3 is correct for those domains. But C2's quoted
   counts are counts of one unspecified/default kernel basis, not invariants.
3. A nontrivial deep-window raw descent exists on the same compact carrier and
   same theta quotient, at both widths and both fixtures. Therefore the no-go
   cannot honestly be scoped merely as “`tau^2` descent on the compact
   carrier.” It must say **seam-anchored prefix presentation
   `D={1,...,dmax}`**. A broader “no descended operator” reading is false.

The deep-window operator is still not a completed OS reconstruction: its
natural core matrix is not self-adjoint in the OS Gram. Thus the construction
refutes the broad descent no-go, not the separate self-adjoint-semigroup wall.

## C1 — full-span reflected Gram

Independent exact reconstruction gives:

| fixture | `T` | shape of `K_AA` | exact rank | `nnz(K_AA-K_AA^T)` |
| --- | ---: | ---: | ---: | ---: |
| `(9/20,5/13)` | 16 | `28 x 28` | **8** | 0 |
| `(9/20,5/13)` | 20 | `36 x 36` | **8** | 0 |
| `(1/2,1/3)` | 16 | `28 x 28` | **8** | 0 |
| `(1/2,1/3)` | 20 | `36 x 36` | **8** | 0 |

For the primary fixture, an adjacent eight-coordinate frame has inertia
`(8 positive, 0 negative, 0 zero)` at both widths, and the exact full-span
Schur residual through that frame has zero nonzero entries. Hence the full
Gram is positive semidefinite of rank eight, not merely a symmetric rank-eight
matrix.

**C1 verdict: CONFIRMED.**

## C2 — prefix-domain obstruction and the basis-count defect

Write `N` for a matrix whose columns are SymPy's default exact basis of
`ker(K_AD)`. The direct reconstruction reproduces every quoted default-basis
count:

| `T` | `dmax` | `dim ker(K_AD)` | quoted/default violations | invariant `rank(M2 N)` | exact possible violation counts after basis change | residual row-slices |
| ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 16 | 5 | 12 | **8** | **2** | `2,...,12` | `{1,...,7}` |
| 16 | 4 | 8 | **6** | **1** | `1,...,8` | `{1,...,7}` |
| 16 | 3 | 4 | **2** | **1** | `1,...,4` | `{1,...,7}` |
| 20 | 7 | 20 | **14** | **2** | `2,...,20` | `{1,...,9}` |
| 20 | 6 | 16 | **12** | **1** | `1,...,16` | `{1,...,9}` |
| 20 | 5 | 12 | **8** | **1** | `1,...,12` | `{1,...,9}` |

The basis-change certificate is constructive. If `R=M2*N`, take the pivot
columns of `R` and then pull a basis of `ker R` back through `N`. Exactly
`rank R` vectors violate. Adding one violating vector to any chosen subset of
the joint-null vectors preserves linear independence and makes precisely that
subset violate; adding it to all of them gives an all-violating basis.

Consequently:

- the statement “the default SymPy nullspace basis has counts
  `8/6/2` and `14/12/8`” is true;
- the unqualified statement “kernel vectors violate in exactly those counts”
  is false;
- the invariant obstruction statement is `rank(M2|ker K_AD)>0`, with ranks
  `2/1/1` at each width;
- the row-slice union is invariant under kernel-basis change and is indeed all
  positive slices in every listed prefix case.

**C2 verdict: COUNT CLAIM REFUTED; EXISTENTIAL OBSTRUCTION AND ALL-SLICE
SUPPORT CONFIRMED.**

## C3 — the two quotient-consistency lemmas

Let `S2` be the literal two-slice shift from the chosen `D` coordinates into
the full positive span. Exact entrywise comparison gives

```text
M2 = K_AA * S2
```

with zero residual in every listed case.

### Theta-side

For `k in ker(K_AD)`, symmetry gives

```text
k^T K_DA = (K_AD k)^T = 0.
```

The direct matrices give zero nonzero entries for this residual in all six
primary cases and all six non-control cases. More generally, if the first
argument changes by a full null vector `n`, then
`n^T K_AA S2 g = 0`. Thus the first/`theta f` class is automatic.

### `g`-side

The pushforward

```text
[g] |-> [S2 g]
```

is well-defined exactly when `S2 ker(K_AD)` lies in `ker(K_AA)`, equivalently
when `K_AA S2 N = M2 N = 0`. The Riesz form

```text
B([f],[g]) = f^T K_AA S2 g
```

has exactly the same condition for independence of the representative of
`g`. The nonzero obstruction ranks above therefore prove that neither raw
pushforward nor the unmodified Riesz form descends for the six listed prefix
domains.

This consequence needs only nonzero obstruction rank; it does not need, and
does not inherit, the basis-dependent vector counts.

**C3 verdict: CONFIRMED FOR THE LISTED PREFIX DOMAINS.**

## P1(a) — image-side quotient

There are two inequivalent meanings of “range classes.”

1. **Ambient OS classes.** Use `R=S2 X_D` with the inner product inherited from
   `K_AA`, hence quotient `R/(R intersect ker K_AA)`. This is well-defined from
   `X_D/ker K_AD` iff `S2 ker K_AD` is ambient-null — exactly the failed C3
   condition. It therefore fails on all six prefix domains.
2. **Algebraic transported classes.** Use `R/S2(ker K_AD)`. The map
   `[g] -> [S2 g]` is then tautologically a bijection. But the ambient image
   Gram descends only if
   `S2^T K_AA S2 N=0`. It does not: its exact ranks are again `2/1/1`, with
   nonzero-entry counts `160/96/24` at `T=16` and `392/288/160` at `T=20`.
   A positive inner product can be transported by definition,
   `<[S2g],[S2h]>_tr := <[g],[h]>`; this yields a working isometry but replaces
   the ambient OS metric with new pullback data.

**P1(a) result:** natural image-side OS descent fails on the prefix domains;
an algebraic image quotient works only with a transported, non-ambient metric.

## P1(b) — exact section/compression construction

Choose an adjacent eight-coordinate core frame `E` and set

```text
Kc = E^T K_AA E,
Vsharp = Kc^-1 E^T K_AA,
P = E Vsharp.
```

At `T=16` (core 2) and `T=20` (core 3), exact QQ arithmetic gives:

```text
inertia(Kc) = (8,0,0)
rank(K_AA E) = 8
K_AA - K_AA E Kc^-1 E^T K_AA = 0
Vsharp E - I_8 = 0
P^2-P = 0
P^T K_AA-K_AA P = 0
K_AA(I-P) = 0.
```

Thus `E` is an exact isometric section/frame for the eight-dimensional OS
quotient. For the shifted frame `E2=S2 E`,

```text
Vsharp E2 = Kc^-1 E^T K_AA E2 = Kc^-1 L2 = W
```

with zero entrywise residual. This is a **working, exact rational sectioned
compression** `Vsharp tau^2 V`; at `T=20` its characteristic polynomial is

```text
(22569375 z^2 - 233631106 z + 22569375)^2
(39529825 z^2 - 109432706 z + 39529825)^2.
```

The boundary is equally exact:

- the raw core shift is not an isometry (`56` and `48` metric-defect entries
  at `T=16,20`);
- `Kc - E2^T K_AA E2` has inertia `(4,4,0)`, so the unscaled shift is neither
  a contraction nor an expansion;
- `Kc W-W^T Kc` has `32` nonzero entries at both widths, so this `W` is not
  self-adjoint in the OS Gram despite its positive spectrum at the deep
  `T=20` core.

**P1(b) result:** the sectioned compression exists and is exactly b190's
primitive `W`. It defeats any claim that quotient failure prevents every
well-defined operator construction, but it does not give a representative-free
action of `tau^2` on the whole quotient and does not complete OS transfer
reconstruction.

## P1(c) — working raw descent on deep windows

This is the decisive construction the prefix tests miss. Scan every contiguous
window `D` whose `+2` shift stays in the positive span. The following
**nontrivial** windows have nullity greater than zero and nevertheless satisfy
`M2 ker(K_AD)=0` exactly:

| width | successful `D` windows | nullity |
| ---: | --- | ---: |
| 16 | `{2,3,4}` | 4 |
| 20 | `{2,3,4}`, `{3,4,5}`, `{4,5,6}` | 4 each |
| 20 | `{2,3,4,5}`, `{3,4,5,6}` | 8 each |
| 20 | `{2,3,4,5,6}` | 12 |

The table is identical at `(9/20,5/13)` and `(1/2,1/3)`. Every successful
`K_AD` has rank eight, so its quotient is eight-dimensional and maps
isomorphically onto the full positive-span quotient. Therefore

```text
T2_D := q_A S2 q_D^-1
```

is a genuine representative-independent operator on the full quotient. No
transported metric is needed. At `T=20`, choosing the deep core frame recovers
the exact `W` factorization displayed above.

The failures are localized by the same scan. Every length-at-least-three
window touching the near seam (`start=1`) fails, and every such window whose
shift reaches the last positive slice (`end+2=T/2-1`) fails. All tested
interior windows satisfying `start>=2` and `end+2<=T/2-2` succeed. This is
consistent with b190's finite boundary-layer finding and contradicts an
interpretation of all-slice output support as a bulk no-go.

A further symmetrization test does not rescue the prefix: at `T=20`,
`D={1,...,5}`, the obstruction ranks for `tau^2`, `tau^-2`, their sum, and
their difference are `1,5,5,5`. On the deep `D={4,5,6}`, both directions
already descend separately.

**P1(c) result: WORKING CONSTRUCTION. This refutes the no-go's broad spirit
and any scope wider than the seam-anchored prefix domains.**

## P2 — non-control point `(1/2,1/3)`

The exact unit-volume Hodge is

```text
B(1/3,1) = diag(1,9/8,9/8,1),
B[1,2] = B[2,1] = -3/8.
```

At both widths the full Gram again has rank eight. For all six prefix domains,
the default-basis violation counts, invariant obstruction ranks, and all-slice
supports are **identical** to the primary fixture's table. Hence the prefix
obstruction is nonzero and output-bulk-distributed at the non-control point.

But the successful deep-window table is also identical. The non-control point
therefore supports generality of the **boundary-sensitive dichotomy**, not a
domain-independent no-go.

## C4 — honest scope

The supplied claims do not assert a curved-OS or reconstruction-in-general
impossibility; that part of C4 is confirmed. However, “`tau^2` descent to the
`theta_s` quotient on the compact carrier” is still too broad, because the
deep-window construction performs exactly such a descent on the same carrier.

The strongest honest scope is:

> At `T=16,20` and the stated fixtures, raw `tau^2` does not descend from the
> seam-anchored prefix presentations `D={1,...,dmax}` listed in C2 to the full
> positive-span `theta_s` quotient. This does not exclude interior-window
> descent, sectioned compression, a transported image metric, curved OS, or
> reconstruction in general.

**C4 verdict: GENERAL-RECONSTRUCTION FENCE CONFIRMED; PER-CONSTRUCTION SCOPE
MUST BE NARROWED TO THE PREFIX PRESENTATIONS.**

## No-Go Discipline Gate (N1--N8)

### N1 — alternative routes

| route | normalized family | exact attempt | outcome |
| --- | --- | --- | --- |
| R1 | numerical/finite case | rebuild `Q,G,K_AA,K_AD,M2` over `QQ` at both widths and both fixtures | C1 and nonzero prefix obstruction confirmed |
| R2 | algebraic rearrangement | change the kernel basis exactly and compute `rank(M2|N_D)` | quoted violation counts refuted as non-invariant |
| R3 | alternate carrier/sector | form ambient and transported image-side quotients | ambient metric fails; transported metric works with new data |
| R4 | symmetry/representation | construct the exact quotient frame projector `P=E Kc^-1 E^T K` and compression | well-defined `W` exists; raw shift remains non-self-adjoint/noncontractive |
| R5 | boundary/initial-condition | scan every admissible contiguous support window | multiple nontrivial interior windows give exact raw descent |
| R6 | alternate observable/readout | test `tau^2 +/- tau^-2` | no prefix cure; deep window already supports both separately |

All are `ATTEMPTED`. R2 and R5 are direct refutations of the claim as broadly
worded; N1 therefore fails for the proposed no-go rather than for lack of route
coverage.

### N2 — wall independence

The ambient image-metric failure is downstream of the raw null-transport wall:
`K_AA S2 N=0` automatically implies `S2^T K_AA S2 N=0`. They are not
independent walls and must be collapsed. The separate surviving wall is that
the working deep/core operator is not OS-self-adjoint; closing descent does not
close self-adjoint-semigroup reconstruction.

### N3 — hidden-wall scan

Three conditions must be explicit:

- the numerical vector counts assume SymPy's default nullspace basis;
- the negative construction assumes seam-anchored prefix domains;
- the natural image-side attempt assumes the ambient OS metric, excluding a
  transported metric or selected quotient frame.

The first two are load-bearing. Omitting either overstates the claim.

### N4 — residual matching

The decisive residual here is exactly `K_AA S2 N=M2 N`, not b190's separate
core asymmetry residual `L2-L2^T` and not the global commutator. The check uses
the direct residual, so no witness substitution is needed. The later
self-adjointness boundary is separately measured by `Kc W-W^T Kc`.

### N5 — rhetoric/resolution audit

- “exactly X kernel vectors” fails at the basis resolution;
- “bulk-distributed” is true only of output row support and false as a claim
  that every bulk-supported input presentation is obstructed;
- “no descended operator” is true for the listed prefixes and false across
  all presentations of the same quotient;
- no curved-OS or reconstruction-in-general impossibility is asserted.

### N6 — partial-closure paths

Interior support selection and the exact core-frame section close the descent
wall without a new axiom, primitive, or physical import. A transported image
metric is another algebraic closure, but changes the metric and must be labeled
as such. None closes the self-adjoint-semigroup wall.

### N7 — steelman against the no-go

The strongest counterargument is constructive: the same rank-eight quotient
has redundant coordinate presentations, and the obstruction comes from the
seam-anchored presentation rather than from `tau^2` intrinsically. At
`T=16`, `D={2,3,4}` has nullity four and zero obstruction; at `T=20`,
`D={2,...,6}` has nullity twelve and zero obstruction, at both fixtures.
Because each window still surjects onto the full quotient, its shifted class
defines a genuine operator on all of `H`. This steelman is exact and succeeds.

### N8 — cross-cycle echo

The b190 authority itself reports finite near- and far-seam boundary layers
while the step data stabilize in the interior. That earlier mechanism applies
directly: moving the spanning window off both seam layers retires the proposed
global descent wall. Treating all-slice residual output support as proof of a
bulk source obstruction would ignore the prior boundary-layer mechanism.

**No-Go Discipline status: FAIL for the broad no-go.** Required demotion:
`partial-narrowing` to the seam-anchored prefix-domain obstruction. The next
scientific wall is not descent existence but OS self-adjoint/semigroup
reconstruction for the working interior-window/core-compression operator.

## Final finding

- **C1:** confirmed.
- **C2:** default-basis numbers and all-slice support confirmed; exact-count
  claim refuted as basis-dependent. Correct invariant ranks are `2/1/1`.
- **C3:** correct for the six named prefix domains; false if read across all
  presentations of the quotient.
- **C4:** general-reconstruction fence is honest, but the per-construction
  scope needs the additional prefix-domain qualifier.
- **P1(a):** ambient image quotient fails on prefixes; transported metric
  works but changes the OS metric.
- **P1(b):** exact isometric section/compression exists and gives `W`; it is
  neither the raw quotient action nor an OS-self-adjoint contraction.
- **P1(c):** nontrivial deep-window raw descents work and refute the broad
  no-go.
- **P2:** both prefix obstruction and deep-window loophole persist unchanged
  at `(1/2,1/3)`.

The block-195 candidate is therefore publishable only as a **narrow
prefix-presentation obstruction**, not as a compact-carrier `tau^2` descent
no-go.

## Independent/authority cross-check

After the independent reconstruction and analysis above were complete, the two
decisive results were recomputed through the landed b190 implementation itself
(without reading the prior b190 adversarial findings):

```text
PASS authority deep window T 16 D (2, 3, 4) facts (8, 4, 0, 0)
PASS authority deep window T 20 D (2, 3, 4, 5, 6) facts (8, 12, 0, 0)
PASS authority prefix obstruction rank T 16 rank 2
PASS authority prefix obstruction rank T 20 rank 2
TOTAL: PASS=4 FAIL=0
```

The four-tuples are `(rank K_AD, nullity K_AD, rank(M2 N), nnz(M2 N))`.
This independently confirms both the working deep-window construction and the
corrected invariant rank of the largest prefix obstruction.

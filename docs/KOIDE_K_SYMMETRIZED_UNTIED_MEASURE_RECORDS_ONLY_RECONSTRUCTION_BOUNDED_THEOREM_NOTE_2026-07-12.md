# K-Symmetrized Untied Measure Records-Only Reconstruction — θ-Invariance Restores Hermiticity for Every Untied Coupling; Positivity Holds on a Nonempty Open Domain and Fails on Another; K-to-Measure Licensing and Many-Slice Transfer Remain Open; the Ordinary Doubled Gaussian Does Not Realize the Orbit Sum, and Uniform Doubling Preserves the Count-Once Comparator (Bounded Theorem, rhalf block 16)

**Date:** 2026-07-12
**Claim type:** `bounded_theorem` (exact two-slice Hermiticity theorem, exact
mixed-domain signature certificates, and bounded licensing/transfer
classification). This note adopts no premise, sets no audit status, and edits
no registry or audit-lane data.
**Primary runner:**
[`scripts/frontier_k_symmetrized_untied_measure_2026_07_12.py`](../scripts/frontier_k_symmetrized_untied_measure_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/frontier_k_symmetrized_untied_measure_2026_07_12.txt`](../logs/runner-cache/frontier_k_symmetrized_untied_measure_2026_07_12.txt)
(SCORECARD: PASS=19, FAIL=0)

> **T2 SIGNATURE VERDICT FIRST — MIXED DOMAIN.** On the block-10 registrable
> spanning set, the normalized K-symmetrized records-only Gram is exactly
> **positive definite at both required genuinely complex untied probes**, so
> positivity is not confined to the block-10 two-branch weight-reality set.
> It is exactly **indefinite** at `W=iI` and at twice the first probe, with
> strict negative rational principal minors; the second failure has
> `Z_sym>0`. Strict signs give nonempty open PD and indefinite neighborhoods.
> Thus the construction restores positivity **on a domain, not universally**.
> The complete six-real-dimensional boundary is not classified here.

> **Not claimed:** revival of the outcome-stage cell; licensing of K as an
> input to the weight; a positive probability measure; a Gaussian/local or
> many-slice transfer law; a global PSD-domain classification; a derivation or
> adoption of either `r` endpoint; a resolution of the equipartition/dial or
> formation-weight residues; a physical Krein reconstruction; or any premise,
> registry, or audit-status change. **Claimed (bounded):** T1–T4 below at the
> two-slice `C₃`-circulant and five-element registrable-spanning-set grade.

## Role — the genuinely open block-10/11 escape tested here

Block 10,
[`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md),
proved that the time-homogeneous **single Gaussian** untied measure has a
Hermitian records-only OS Gram only on its two K-real branches: the K-tie and
the all-real branch. It left a modified/non-OS emergent-time construction
genuinely open and rejected the alternating `W,W†` measure because choosing
which slice carries the conjugate needs an arrow and explicitly inserts K.

Block 11 (source branch
`origin/claude/science/rhalf-quasi-hermitian-escape-20260712`) closed a positive
metric-operator weakening on `W` exactly to the tie. It left an indefinite
Krein remainder on three transposition branches and a still coarser
two-slice-factor `A₂` remainder. Neither block tested the arrow-free orbit
average

```text
μ_sym(W) = 1/2 [ μ_W + μ_{W†} ]
         = 1/2 [ exp(χ̄ K(W,W) χ) + exp(χ̄ K(W†,W†) χ) ].          (0.1)
```

The same time-homogeneous coupling occurs on both slices inside each summand.
No choice assigns `W` to the future and `W†` to the past: (0.1) averages the
whole two-slice weight over the K-orbit `{W,W†}`. The question is whether this
conjugation-pairing move supplies a records-only positive form without paying
the block-10 arrow cost, and whether it supplies an emergent-time transfer
rather than only a two-slice functional.

## Setup and notation — raw forms kept separate from normalized forms

Use block 10's three-mode circulant and two-slice kernel,

```text
C = [[0,1,0], [0,0,1], [1,0,0]],       C³=I,
W = aI+bC+cC²,
K(W,W) = [[-W, -1/2 I], [+1/2 I, -W]].                       (0.2)
```

Let `B_W(O)` be the unnormalized Berezin functional with the first
exponential in (0.1), and write

```text
Z_W                 = B_W(1),
𝒢^W_ij               = B_W(θ(F_i) F_j),
{F_i}                = {1, N, TCsym, e₂, e₃},
B_sym(O)             = [B_W(O)+B_W†(O)]/2,
Z_sym                = B_sym(1),
𝒢^sym_ij             = B_sym(θ(F_i)F_j),
G^sym                = 𝒢^sym/Z_sym,             only if Z_sym ≠ 0.       (0.3)
```

This raw/normalized distinction matters. The raw symmetrized Gram is the
arithmetic average. The normalized `G^sym` is generally **not** the half-sum
of the separately normalized component Grams, because their partition
functions are complex conjugates rather than equal.

## T1 — θ-invariance gives Hermiticity exactly for every untied W

Block 10's reflection identity gives, before normalization,

```text
Z_{W†} = conjugate(Z_W),
𝒢^{W†}_ij = conjugate(𝒢^W_ji).                              (1.1)
```

Equivalently, `θ` exchanges the two measures in (0.1). By linearity,

```text
θ μ_sym = μ_sym,
𝒢^sym = [𝒢^W + (𝒢^W)†]/2 = (𝒢^sym)†,                       (1.2)
Z_sym = [Z_W+conjugate(Z_W)]/2 = Re Z_W.                   (1.3)
```

Therefore the raw records-only form is Hermitian for **every** untied `W`.
Where `Z_sym` is nonzero it is real, so division preserves Hermiticity. This
is an exact sufficiency theorem; unlike block 10's single-Gaussian result, it
does not require `W†∈{W,PWP}`.

Checks 3–4 verify (1.1)–(1.3) entrywise with the reused exact Berezin engine at
the two required probes:

```text
P1 = (a,b,c) = (4/5+i/10, 3/10+i/5, 1/2-i/10),
     Z_sym = 442243/1000000;

P2 = (a,b,c) = (1, 1/3+i/7, 1/3-i/5),
     Z_sym = 118339871223181/85766121000000.
```

Both are genuinely off the block-10 K-tie/all-real union and both normalize.

### The zero-mass locus is real and cannot be divided away

Equation (1.3) defines the normalization domain:

```text
𝒟_norm = { (a,b,c) : Re det(W²+1/4 I) ≠ 0 }.               (1.4)
```

Its complement is nonempty even where `Z_W` itself is nonzero. At the exact
scalar point

```text
W = (3/8+5i/8) I,
W²+1/4 I = (15i/32) I,
Z_W = (15i/32)³ = -3375i/32768 ≠ 0,
Z_sym = 0.                                                  (1.5)
```

The raw symmetrized form remains Hermitian there, but there is no normalized
expectation functional or normalized Gram. No assertion below crosses this
locus.

## T2 — decisive signature: positivity on a domain, failure on a domain

For a Hermitian `5×5` matrix, nonnegativity of all 31 principal minors is an
exact PSD criterion; strict positivity of the leading minors is Sylvester's
PD criterion. The runner evaluates every minor over Gaussian rationals.

### Exact PD at both required genuinely untied probes

At both `P1` and `P2`, **all 31 principal minors are strictly positive exact
rationals** (checks 6–7). In particular the full determinants are

```text
det G_sym(P1)
 = 2481178078125000000000000000
   /16916278917990800432294819443  > 0,

det G_sym(P2)
 = 41608903136082324823895797257801559519543346362471875000000000000000
   /23208948333223840320190645259090098573336248968791134439568823789159901
   > 0.                                                       (2.1)
```

Float minimum eigenvalues `≈0.0347416` and `≈0.00738361` are printed only as
scan context; they do not decide either verdict.

### Exact indefinite witnesses

Symmetrization is not universally positive. Two exact witnesses isolate both
the normalization-sign issue and a genuine positive-`Z_sym` failure:

| point | `Z_sym` | exact negative principal minor | verdict |
|---|---:|---:|---|
| `W=iI` | `-27/64` | `G_sym[N,N] = -44/3` | indefinite |
| `W=2P1` | `6467077/1000000` | `det G_sym[{TCsym,e₂}] = -7095906000000/41823084923929` | indefinite |

The second row has positive normalization, so failure is not an artifact of
dividing by a negative `Z_sym` (check 8).

### The exact domain statement, and no stronger one

Matrix entries are rational functions of the six real coupling coordinates
away from (1.4)'s zero set. Exact strict PD at `P1,P2` therefore persists on
open neighborhoods. Each strict negative minor likewise persists on open
neighborhoods of `iI,2P1`. Hence:

> **T2.** The K-symmetrized normalized records-only form is PD on a nonempty
> open domain and indefinite on another nonempty open domain. It is neither a
> universal positive reconstruction nor confined to the old K-real branches.

The block-10 controls are recovered exactly (check 10): on the tie the two
weights coincide; on the all-real branch the two components are related by
`P`, so their P-even record Grams coincide. The known all-real inside-strip
point remains PD and the known outside-strip point remains indefinite.

The deterministic six-real-dimensional scan is labeled coverage only. Every
coordinate component is sampled on a rational grid in `[-R,R]`; float
eigenvalue **sign**, with no fitted or tolerance threshold, is used only to
map the following pattern:

| box radius `R` | PD | indefinite | `Z_sym=0` | samples |
|---:|---:|---:|---:|---:|
| `1/10` | 24 | 0 | 0 | 24 |
| `1/5` | 19 | 5 | 0 | 24 |
| `1/2` | 8 | 15 | 1 | 24 |
| `3` | 0 | 48 | 0 | 48 |

This supports a bounded-domain reading and warns against extrapolating the two
favorable probes. It is **not** a theorem that failure is generic, that the
domain is connected, or that a simple strip controls all six coordinates.
The full semialgebraic boundary is a Residual Atom.

## T3 — what kind of law/measure this is, and what remains unlicensed

### (i) One answer versus an ensemble representation

For supplied `(W,K)`, equation (0.1) returns exactly one fixed Grassmann
integrand. On the extensional wording of the Qualification — a law gives one
answer wherever its supplied condition holds — it therefore satisfies the
**one-answer** clause. More precisely, it is:

- a finite Grassmann/Berezin **weight**;
- an unnormalized complex linear functional `B_sym`;
- a normalized expectation functional only on `𝒟_norm`;
- a θ-invariant Hermitian records-only form; and
- on the T2 PD domain, a positive form on the stated registrable spanning set.

It is **not** thereby:

- a positive probability measure;
- a normalized law on `Z_sym=0`;
- a Gaussian or a single exponential weight;
- the output of a landed single-step local bilinear rule;
- a landed many-slice history law; or
- a measure derived from the four Minimal Axioms.

It also has an ensemble decomposition at the raw-weight level: it is the
formal equal average of two component laws. That representation does not make
it a positive probabilistic mixture. At `P1`, rewriting the normalized
functional as a combination of the separately normalized component
functionals gives

```text
alpha = Z_W/(Z_W+Z_W†) = 1/2 + (128413/442243)i,
beta  = Z_W†/(Z_W+Z_W†) = 1/2 - (128413/442243)i,
alpha+beta=1.                                                (3.1)
```

The coefficients are conjugate but nonreal (check 13). “One weight” and
“formal ensemble representation” are therefore both correct at their stated
levels; “positive ensemble of normalized laws” is false at this probe.

### Non-Gaussianity is exact

Let `S=χ̄K(W,W)χ` and `T=χ̄K(W†,W†)χ`. Any single bilinear exponential matching
the constant and degree-two terms of (0.1) must have action `(S+T)/2`. At
Grassmann degree four,

```text
1/2(e^S+e^T) - exp[(S+T)/2]
    = (S-T)²/8 + higher Grassmann degree.                    (3.2)
```

At exact `P1`, `(S-T)²/8` is nonzero; the runner finds the first mismatch at
degree four (723 coefficient masks differ overall, check 12). Thus the
symmetrized construction is not a single three-mode Gaussian transfer rule at
the required genuinely untied point. Exceptional fixed points such as the tie,
where `S=T`, reduce to the original Gaussian as they must.

### (ii) Does the construction pre-insert K?

There are two honest readings.

**Canonical supplied-context reading.** K is stipulated as supplied
readout-context structure. Once it is supplied, the orbit `{W,W†}` and its
equal average are canonical. No representative and no time arrow is chosen;
`μ_sym(W)=μ_sym(W†)` exactly (check 14). This avoids the specific arrow defect
of the alternating measure.

**Measure-pre-insertion reading.** The construction explicitly applies that K
involution to the unregistered Berezin weight. The Minimal Axioms memo places
K/CPT orbit structure downstream of generic axiom content; it does not say
that readout-context K may generate or modify the measure. On this reading,
(0.1) promotes the very K structure sought at the outcome/record stage into
the dynamics and therefore pre-inserts it.

The algebra cannot choose between these readings. The question is retained as
the first-class Residual Atom **K-ORBIT-AVERAGE LAW/MEASURE LICENSING**. No
revival claim is available while it remains open.

### (iii) Two-slice homogeneity does not land a many-slice law

The average in (0.1) is global over the whole two-slice weight; it is not an
independent average on each slice. Each summand is time-homogeneous, but there
are at least two inequivalent extensions:

```text
quenched:  choose W or W† once for a complete N-step history,
           then average the two complete-history weights;

annealed:  average the orbit representative independently per step/link,
           producing a sum over 2^N assignments.                          (3.3)
```

For commuting scalar step weights `x,y`, the two prescriptions already give
`(x²+y²)/2=13/2` and `((x+y)/2)²=25/4` at `(x,y)=(2,3)` (check 15). Neither
extension is landed. The two-slice construction therefore supplies no single
transfer power or time-homogeneous many-slice law by itself.

## T4 — doubled carrier: conjugation closure is real, realization fails

### The six-mode carrier is Krein by construction

Put

```text
D = W ⊕ W†,
J = [[0,I₃],[I₃,0]].                                         (4.1)
```

Then exactly

```text
J D = D† J,      J²=I,      signature(J)=(3,3).              (4.2)
```

Thus `D` lies on block 11's any-signature conjugation-closed locus by
construction. This is not a positive-metric escape: at generic nonreal `W`,
the explicit carrier comes with three negative directions.

There is also a natural doubled **antiunitary**. Let `P` be block 10's real
generation inversion (`PCP=C²`) and put

```text
S = [[0,P],[P,0]],          K_D = S followed by scalar conjugation.
```

For the circulant, `W†=P conjugate(W) P`, so exactly

```text
S conjugate(D) S = D,       K_D²=1.                            (4.3)
```

The `K_D`-fixed real form is invariant under `D`. It must not be confused with
the **linear** positive-eigenvalue half of the indefinite metric `J`. At `P1`,
`[D,J]≠0`; with `P_J+=(I+J)/2`,

```text
(I-P_J+) D P_J+ ≠ 0.                                         (4.4)
```

Thus the K-real carrier is closed, but discarding the three negative `J`
directions does not supply a closed positive three-complex-mode transfer system
(check 16).

### A Gaussian direct sum produces a product, not the orbit sum

For Grassmann carriers,
`Λ(V⊕V̄) ≅ Λ(V)⊗Λ(V̄)`. The Gaussian with coupling `D` consequently factorizes:

```text
Z_D = Z_W Z_W† = |Z_W|²,                                    (4.5)
```

not `Z_sym=(Z_W+Z_W†)/2`. For the P-even registrable basis, the natural
K-paired additive lift of an already formed correlator `O` reduces to
`O_+=(O_W+O_W†)/2`, gives

```text
B_D(O_+) = [B_W(O) Z_W† + Z_W B_W†(O)]/2.                   (4.6)
```

The spectator partition factors in (4.6) are absent from (0.3). At exact
`P1`, the normalized doubled and symmetrized `5×5` forms differ in 24 entries;
the first difference, at `(1,N)`, is

```text
1523664567517428 / 4626542220828959 ≠ 0.                    (4.7)
```

So the ordinary six-mode doubled Gaussian **does not reproduce** the
K-symmetrized correlators, even on this natural K-paired additive lift
(check 17).

A direct-sum **superselection trace** with an exclusive one-of-two sector could
produce the sum rather than the product, but that requires a sector label and
a one-hot constraint. It is an ensemble realization added by hand, not the
Gaussian on `W⊕W†`, and it inherits the T3 licensing and many-slice questions.

### Counting: uniform doubling does not reinstate count-twice

The undoubled `C₃` carrier has one complex singlet plus a two-complex-mode
doublet: two and four real carrier degrees, respectively. The direct sum
doubles **both**:

```text
                 singlet real degrees    doublet real degrees
undoubled                 2                       4
W ⊕ W†                    4                       8.             (4.8)
```

Applying block 10's fork arithmetic without changing its grain rule makes the
uniform factor cancel. The count-once comparator is

```text
undoubled:       3 a² = eps,       6 b² = eps,
doubled:         6 a² = 2 eps,    12 b² = 2 eps,
both:            b²/a² = 1/2.                                  (4.9)
```

The doubled count-twice comparator would instead require

```text
6 a² = 2 eps,    12 b² = 4 eps       =>       b²/a² = 1.        (4.10)
```

Equation (4.10) does **not** follow from carrier doubling. It requires an extra
doublet budget or an asymmetric quotient that removes/identifies the duplicated
singlet without doing the same to the doublet. Either is a new
formation/equipartition grain rule. The antiunitary K-fixed real form halves
singlet and doublet uniformly, so it preserves the ratio; the linear `J=+1`
projection also halves both but, by (4.4), is not transfer-invariant.

> **T4.** Ordinary doubling pays a uniform factor-two carrier overhead and a
> `(3,3)` Krein form. It neither realizes `μ_sym` nor automatically changes
> the count-once fork comparator to count-twice. No physical `r` value is
> inferred from (4.9)–(4.10).

## Licensing consequence — algebraically live, not revived

T1 removes the block-10 Hermiticity obstruction. T2 does more than a purely
formal repair: there are exact genuinely untied complex points with a positive
records-only form, and positivity persists on open neighborhoods. But the
honesty gate for revival has two conjuncts: positivity **and** landed
licensing. Only the first is met on the T2 PD domain.

The outcome-stage cell is therefore **not revived**. Nor is the route closed
by a count-twice-doubling no-go: the honest uniform doubled arithmetic leaves
the count-once comparator unchanged. The bounded result is narrower and more
useful:

> the two-slice non-Gaussian orbit average is an algebraically viable positive
> records-only functional on a real domain, while K-to-measure licensing,
> law/ensemble status, and a many-slice transfer realization remain open; the
> naive doubled Gaussian is not that realization.

## Escape-table update relative to blocks 10 and 11

| route | disposition after block 16 | exact reason / remaining cost |
|---|---|---|
| modified/non-OS emergent time via `μ_sym` | **PARTIALLY REALIZED ALGEBRAICALLY** | T1 Hermitian for every `W`; T2 PD on a nonempty open domain, indefinite on another |
| K-orbit-average measure licensing | **OPEN — first-class Residual Atom** | supplied-context canonicality versus K-to-weight pre-insertion is not settled |
| many-slice extension of `μ_sym` | **OPEN** | quenched two-term history average and annealed `2^N`-term average are inequivalent |
| ordinary Gaussian on `W⊕W†` | **BLOCKED as a realization of `μ_sym`** | K-paired correlators still factor as a product; the K-real form is invariant but the positive `J` half is not; `(3,3)` Krein cost |
| exclusive-sector/direct-sum trace | **OPEN, additional structure** | reproduces a sum only by adding a one-hot sector law |
| alternating `W,W†` slice measure | **UNLICENSED (inherited)** | arrow-dependent placement and explicit K pre-insertion |
| positive metric on `W` | **CLOSED to the tie (block 11)** | no non-tied positive-metric escape |
| any-signature metric on `W` | **OPEN KREIN remainder (block 11)** | negative norms on the three non-tied transposition branches |
| condition only on `A₂=W²+1/4I` | **OPEN, strictly coarser (block 11)** | factor condition does not reconstruct the records-only OS form |
| `Z_sym=0` locus | **NO NORMALIZED CONSTRUCTION** | exact nonempty witness (1.5) |
| full T2 PSD boundary | **OPEN** | exact open regions landed; no global six-dimensional classification |

This table does not turn an open licensing question into a negative verdict and
does not let exact two-slice positivity masquerade as a transfer construction.

## Literature precedent — context only

Conjugation/CT organization of complex-action sign problems is standard
context; see P. N. Meisinger and M. C. Ogilvie,
[*The Sign Problem, PT Symmetry and Abelian Lattice Duality*,
arXiv:1306.1495](https://arxiv.org/abs/1306.1495). It is cited only as precedent
for treating conjugation-paired complex weights. No orbit-average formula,
Hermiticity statement, positivity domain, principal minor, doubled-carrier
claim, or licensing conclusion is imported; all results above are proved
repo-natively by the companion runner.

## Residual Atoms

1. **K-ORBIT-AVERAGE LAW/MEASURE LICENSING (first-class).** Whether supplied
   readout-context K may canonically act on the unregistered weight or thereby
   pre-inserts downstream structure. This is the load-bearing revival gate.
2. **The complete T2 PSD domain.** Exact open PD and indefinite regions are
   proved; connectedness, analytic boundary, and global genericity are not.
3. **The `Z_sym=0` set.** Its defining equation is exact and one nontrivial
   locus is witnessed; its full geometry is not classified.
4. **Law versus ensemble ontology.** The prescription is extensionally one
   answer and formally a raw orbit ensemble, but no positive probabilistic or
   physical ensemble interpretation is supplied.
5. **Many-slice time law.** Quenched and annealed extensions differ; neither is
   landed, and no transfer semigroup/power is identified.
6. **Exclusive-sector realization.** Reproducing a sum instead of the doubled
   Gaussian product requires a one-hot sector rule and its history behavior.
7. **Doubled-carrier grain.** Uniform doubling preserves the comparator;
   changing it requires a new asymmetric quotient or equipartition budget.
8. **Per-cell equipartition/dial and formation weight.** Entirely untouched;
   no physical `r` endpoint is derived or adopted.
9. **Finite spanning-set scope.** Positivity is established/falsified on
   `{1,N,TCsym,e₂,e₃}` for the two-slice `C₃` circulant. Full record-algebra,
   interacting, non-circulant, gauge, and higher-slice cases are not classified.
10. **Inherited block-11 remainders.** Krein reconstruction and the coarser
    `A₂` condition remain open at that note's stated costs and grades.

## What This Note Does Not Claim

- **Not** revival of the outcome-stage cell: T3 licensing is not landed.
- **Not** a derivation, selection, prediction, or adoption of `r=1/2` or
  `r=1`; equations (4.9)–(4.10) only compare the already named fork cells.
- **Not** a global positivity theorem. Strict exact witnesses prove a mixed
  domain; scans are labeled and never thresholded.
- **Not** that Hermiticity implies positivity: T2 supplies exact counterexamples.
- **Not** a positive probability measure or positive normalized component
  mixture; (3.1) is an exact obstruction at `P1`.
- **Not** a Gaussian or local transfer rule; (3.2) and T4 distinguish sum from
  product.
- **Not** that doubling restores count-twice. Uniform doubling doubles the
  singlet and doublet alike.
- **Not** that a superselection direct sum is forbidden. It is additional,
  unlanded structure rather than the tested Gaussian carrier.
- **Not** closure of the block-11 Krein or `A₂` remainders.
- **Not** premise adoption, empirical comparison, registry change, or audit
  verdict. No comparator is fitted or thresholded.

## Consumed premises and supplied elements (claim scope)

- **Block-10 two-slice construction and exact engine** —
  [`RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md`](RECORDS_ONLY_OS_RECONSTRUCTION_UNTIED_FIRST_ORDER_MEASURE_BOUNDED_THEOREM_NOTE_2026-07-11.md)
  and
  [`scripts/frontier_records_only_os_reconstruction_2026_07_11.py`](../scripts/frontier_records_only_os_reconstruction_2026_07_11.py):
  `W`, the two-slice staggered kernel, `θ`, reflection identity, registrable
  spanning set, exact probes, all-real strip controls, alternating-measure
  disposition, and the fork arithmetic. The engine is reused rather than
  replaced.
- **Block-11 metric-operator closure** — the note read once from
  `origin/claude/science/rhalf-quasi-hermitian-escape-20260712`: positive
  metrics close to the tie; any-signature conjugation closure has four loci;
  the non-tied Krein and coarser-`A₂` remainders remain open. Those results are
  cited at their declared grade and not reclassified here.
- **Minimal Axioms and Qualification** —
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md): a law gives
  exactly one answer on its supplied condition; a law may not depend on an
  unfixed choice unless admitted; K/CPT, probability, arrow, time metric, and
  formation rules are downstream, not generic axiom content.
- **Literature precedent only** — Meisinger–Ogilvie `arXiv:1306.1495`; no
  theorem content imported.

## Reprove-and-cite ledger

- **Reproven exactly by the runner:** block-10 engine determinant and toy-Gram
  controls; `Z_W†=conj Z_W`; raw Gram adjoint relation at both required probes;
  direct integration of the orbit half-sum; Hermiticity before and after valid
  normalization; exact zero-`Z_sym` witness; all 31 exact principal-minor signs
  at `P1,P2`; exact negative minors at `iI,2P1`; inherited tie/all-real controls;
  degree-four non-Gaussian obstruction; nonreal normalized component weights;
  K-orbit invariance and tied reduction; annealed/quenched inequivalence;
  doubled `J` intertwiner/signature, antiunitary K closure, and positive-`J`-half leakage; doubled
  product-versus-sum correlator mismatch; real-dimension and fork arithmetic;
  refined escape dispositions.
- **Floats used only for labeled coverage:** minimum-eigenvalue context at the
  exact probes and deterministic box scans. No float lies on a derivation path,
  supplies a threshold, or changes an exact verdict.
- **Cited at declared grade:** block 10 for the OS/reflection construction and
  inherited fork/escape rows; block 11 for metric and `A₂` dispositions; the
  Minimal Axioms memo for Qualification and downstream-structure scope;
  Meisinger–Ogilvie for literature context only.

## Verification

```bash
python3 scripts/frontier_k_symmetrized_untied_measure_2026_07_12.py
```

Expected: 19 numbered `[PASS]` lines, declared-open `RESIDUAL` lines, the T2
signature verdict first in the final summary, one-sentence T1/T3/T4 outcomes,
the doubled-carrier counting result, proposed claim scope, hostile-audit
uncertainties, and `TOTAL: PASS=19 FAIL=0`. Exit code 0 iff `FAIL=0`.

Regenerate the runner cache with

```bash
python3 scripts/precompute_audit_runners.py --push-mode none --force \
  --runners scripts/frontier_k_symmetrized_untied_measure_2026_07_12.py
```

**Independent supervisor review required.** This note asserts no effective-
status change.

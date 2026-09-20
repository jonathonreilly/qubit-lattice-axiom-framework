# Independent check: third birth on the six-site ladder

Completed independent mathematical/computational check, 2026-09-20. The exact
rare-birth probability is **2701/53880 = 0.05012991833704528**, whereas the static
law conditioned on three occupied sites gives **73/1440 =
0.050694444444444445**. Their ratio is **444/449**; static minus dynamic is
**73/129312 = 0.0005645261073991587**.

The primary agent's `probe.py`, `probe.json`, `CHECKPOINT.md`, candidate note,
and candidate runner have not been read at the time this report is sealed.
The initial handwritten derivation is preserved in `INITIAL_DERIVATION.md`.
This is same-family, separate-context scrutiny, not an audit or retention
decision. The independently written code imports no primary-agent artifacts.

## Analytic result derived before implementation

Let `g(s)` be the product of occupied-edge weights and let
`b(s;x,a) = g(s + (x,a))/g(s)`. Write `B(s) = sum_(x,a) b(s;x,a)`.
On a finite irreducible motion component `C`, motion has stationary law
`pi_C(s) = g(s)/Z_C`. The state immediately before a rare birth is instead

```
nu_C(s) = pi_C(s) B(s) / <B>_pi_C.
P(prestate=s, birth=(x,a)) = pi_C(s) b(s;x,a) / <B>_pi_C.
```

For a component entrance law `alpha`, the exact finite-epsilon joint law is
`epsilon [alpha (epsilon diag(B) - Q_C)^(-1)](s) b(s;x,a)`.
The rare-event expression follows because any subsequential limit of
`epsilon alpha (epsilon diag(B) - Q_C)^(-1)` is stationary for `Q_C`, while
its product with `B` has mass one. Positivity and finiteness bound the vector,
and irreducibility identifies the unique limit as `pi_C/<B>_pi_C`.

With one record, `B=30` and sites are uniform. The second record agrees with
the first with probability `(5 + (1/2)(14/6))/30 = 37/180`.

For two identical records, the pair placement partition sum is
`Z_aa = 7(3/2) + 8 = 37/2`. Of the eight nonadjacent pairs, two have one
common neighbor, four have two, and two have none. Adjacent pairs have no
common neighbor. Thus `B(s)=24 + m(s)/2` and

```
sum_s g(s) B(s) = 24(37/2) + (1/2)(2 + 8) = 449.
```

The 20 three-site subsets have respectively 0, 1, and 2 occupied edges with
multiplicities 2, 8, and 10. Hence `Z_aaa = 2 + 8(3/2) + 10(3/2)^2 = 73/2`.
Each all-identical triple can be reached by three deletions, giving
`sum_s g(s) sum_x b(s;x,a) = 3 Z_aaa = 219/2`. Therefore

```
P(all three identical immediately after third birth, epsilon -> 0)
  = (37/180) (219/898)
  = 2701/53880.
```

For the static law conditioned on three occupied sites, every induced graph
is a forest and every row of `W` sums to six. Summing over the leaf content
successively therefore gives 216 per occupied triple. The total partition
sum is `20*216=4320`; the identical-content weight is `6*(73/2)=219`.
Consequently the static probability is `73/1440`, and the dynamic/static
ratio is `444/449`.

All these calculations are confirmed by the exact enumeration and the
separate finite-epsilon absorption calculation below.

## Exact scope and sampling-law proof

The graph has vertices 0 through 5 and edges `(0,1),(1,2),(3,4),(4,5),(0,3),
(1,4),(2,5)`. A site is empty or contains one of six immutable contents.
The supplied weights are 3/2 for equality, 1/2 for antipodes `b=a xor 1`, and
1 otherwise; empty bonds weigh 1. Every edge rings at rate 1 and the hop rate
on a particle-vacancy edge is `w_destination/(w_source+w_destination)`.
Birth `(x,a)` has rate `epsilon b(s;x,a)`, and there is no removal.
All results are conditional on this stipulated process, not physical
identifications or new axioms. The event is evaluated at the stopping time
immediately after the third birth, with the graph and motion rates fixed
as `epsilon` tends to zero through positive values.

For a hop `s -> t`, global weight ratios give `g(t)/g(s)=w_destination/
w_source`; the reverse local weights interchange. Thus detailed balance
holds with `pi_C=g/Z_C` on every connected motion component. Rejected edge
rings are omitted from the continuous-time generator `Q_C`, as they change
no state. Continuous-time irreducibility is sufficient; a separate discrete
aperiodicity assumption is unnecessary here.

Put `D=diag(B)`, and take any probability entrance law `alpha` on a finite
irreducible component containing a vacancy. The killed motion semigroup is
`exp[t(Q_C-epsilon D)]`, so its integrated occupation vector is
`alpha(epsilon D-Q_C)^(-1)`. Multiplication by `epsilon b(s;x,a)` gives the
exact exit-channel probabilities stated above. Absorption is certain since
all birth rates and the finite state's total hazard are positive.

To justify the limit without assuming equilibrium at an event time, put
`v_epsilon=epsilon alpha(epsilon D-Q_C)^(-1)`. Then

```
v_epsilon B = 1,
v_epsilon Q_C = epsilon(v_epsilon D-alpha).
```

Because `B_min>0` here, the nonnegative vectors have total mass at most
`1/B_min`. Any subsequential limit is stationary for `Q_C`, hence a scalar
multiple of `pi_C`; its product with `B` is 1. The limit is therefore unique
and equals `pi_C/<B>_pi_C`, proving the event law. More generally the same
formula holds for nonnegative hazards with positive stationary mean: the
finite linear system consisting of the stationary equations and `vB=1`
has a unique solution at zero epsilon, giving continuity. A component with
zero total birth hazard has no next-birth law.

If motion has several components, average **inside each component**. For a
component entrance probability `beta(C)`, the pre-birth law is the mixture
`sum_C beta(C) pi_C(s) B(s)/<B>_pi_C`. Its component mass stays `beta(C)`:
each trajectory produces one next birth. Replacing this by one globally
normalized `pi(s)B(s)` wrongly reweights components by their mean hazards.
The embedded birth-chain transition to component `D'` is

```
K(C,D') = sum_s pi_C(s) sum_(births s->D') b(s;birth) / <B>_pi_C.
```

## Connectivity and exact enumeration

An exhaustive breadth-first search used legal occupied-vacant swaps,
independently of their positive numerical rates. Every connected component
was compared with the complete set sharing its six-component content-count
vector. The equivalence holds on all needed levels:

| Records | States | Motion components | Component sizes and multiplicities |
|---:|---:|---:|---|
| 0 | 1 | 1 | 1 x 1 |
| 1 | 36 | 6 | 6 x 6 |
| 2 | 540 | 21 | 15 x 6; 30 x 15 |
| 3 | 4320 | 56 | 20 x 6; 60 x 30; 120 x 20 |

Exact rational detailed balance was checked on respectively 0, 84, 2016,
and 18144 directed hops. Exact birth-weight ratios were checked for each
enumerated birth used in the calculation. The full birth-chain propagation
normalized to one at every level. It agrees with the static law after births
1 and 2 and differs after birth 3 by total variation `811/387936`.
All 20 three-site occupied subsets have content partition sum 216, and
their induced edge-count profile is exactly `{0:2,1:8,2:10}`.

The component claim must not be extended to arbitrary vacancy counts. On
this same graph, five distinct contents and one vacancy give 720 arrangements
with one content-count vector but **two** motion components of size 360.
This is also predicted by the invariant combining permutation parity of
five labeled contents plus the hole with the hole's bipartition parity:
one move flips both parities, preserving their product.

## Independent finite-epsilon absorption calculation

This calculation uses the motion generator, not the rare-event formula.
For every positive epsilon, the first birth has a uniform site and content.
With one record the total birth hazard is the constant 30 and the entrance
law is motion-stationary. Consequently the exact post-second-birth law is
`g(s)/540`, for every epsilon: each two-record state has two single-record
predecessors, each contributing `g(s)/(36*30)`. Conditional on two identical
records of a specified content, the pair entrance law is `pi_aa`.
The desired event can arise only from these identical-pair components.

For the 15 placements of two identical records, set `L(s)=sum_x b(s;x,a)`
for the common content `a`. The exact absorption success vector solves

```
(epsilon diag(B)-Q) h = epsilon L,
P_epsilon = (37/180) pi_aa h.
```

The graph's four automorphisms give six pair-placement orbits. Their order
is H: horizontal edges; R: `(0,2),(3,5)`; V: outer vertical edges; D:
`(0,4),(1,3),(1,5),(2,4)`; L: `(0,5),(2,3)`; M: `(1,4)`.
The generator's strong lumpability was checked exactly for every state in
each orbit. The resulting independently solvable six-state data are

```
Q = [ -6/5,   2/5,    0,   4/5,    0,    0;
       6/5, -11/5,    0,     0,    1,    0;
         0,     0, -4/5,   4/5,    0,    0;
       6/5,     0,  3/5, -29/10, 1/2,  3/5;
         0,     1,    0,     1,   -2,    0;
         0,     0,    0,   8/5,    0, -8/5 ]
B = (24, 49/2, 24, 25, 24, 24)
L = (11/2, 25/4, 5, 7, 6, 6)
pi = (12,4,6,8,4,3)/37.
```

For example, from pair `(0,1)` each of its three available hops changes an
occupied edge of weight 3/2 to no occupied edge, so each has rate 2/5;
one reaches R and two reach D. This verifies the first row directly.
Exact symbolic inversion gives `P_epsilon=N(epsilon)/D(epsilon)`, with

```
N(e) = 95366160000 e^5 + 41898708000 e^4 + 6758339400 e^3
       + 498976260 e^2 + 16928359 e + 210678
D(e) = 1905120000000 e^5 + 836593920000 e^4 + 134896320000 e^3
       + 9957002400 e^2 + 337738320 e + 4202640.
```

The symbolic harmonic-equation residual is identically zero. Both limits
are taken symbolically: at zero the result is `2701/53880`, and at infinity
it is `14717/294000`. Separate floating-point solves of the original
15-state system agree with this expression to absolute error below `1e-10`
at the nine tested epsilons from `1e-6` through `1e6`. Representative values:

| Epsilon | Exact-expression value (rounded) |
|---:|---:|
| 0.000001 | 0.05012991775755891 |
| 0.01 | 0.05012469853913531 |
| 0.1 | 0.05009990019869418 |
| 1 | 0.05006715262472315 |
| 10 | 0.05005888915437675 |

The largest absolute floating harmonic residual is `1.86e-9` at epsilon
`1e6` (where the coefficients are of order `1e7`); the small-epsilon residual
is about `2e-16`. These numerical checks support, but do not replace, the
exact symbolic identity.

## Adversarial controls and ensemble distinctions

* **No motion.** Each configuration is a singleton component and its next
  birth is selected by `b/B`. Exact growth enumeration gives
  `14717/294000 = 0.0500578231292517`, independent of epsilon. A direct
  combinatorial check is `(19/8 + 1/2 + 25/49 + 28/25)/90`. This agrees with
  the large-epsilon limit of the positive-motion generator. Counts cannot
  be used as components once motion is switched off.
* **Wrong pre-birth law.** Sampling `pi_aa` at the birth event would use
  `E_pi[L/B]` in place of `E_pi[L]/E_pi[B]`; here it gives the no-motion
  answer above and is rejected by the independent exact absorption result.
  Pooling all content counts into one motion component instead gives the
  static answer and is rejected too. Both intentionally wrong candidate
  values were required to fail the exact comparison.
* **Constant weights.** Separate full enumerations for `W=1` and `W=2`
  give `1/36` for all-identical contents under rare birth, no motion, and
  the static law. This follows independently because every content is
  equally likely at each birth when weights have no content dependence.
  With `W=2` the no-motion spatial distribution still differs from static
  (third-birth total variation `16900/422037`), so the content statistic
  alone does not test equality of entire laws.
* **Constant hazard.** Replacing the killing hazard by 1 while starting
  stationary leaves the sampled state stationary for every epsilon. Direct
  15-state solves had maximum absolute error `1.15e-14` for the four tested
  epsilons. Hazard bias is essential only when the hazard varies.

For the identical-pair component the genuine rare-event pre-birth law has
total variation `125/16613 = 0.0075242280142057425` from `pi_aa`. Thus making
births rarer does **not** make these two event-sampling laws coincide.
The quoted source's rare-formation remark is incorrect when “just before
each formation” means the actual next birth event under the supplied
state-dependent birth rates. This does not refute its motion detailed
balance theorem or its birth-death detailed balance calculation.

An externally sampled time after relaxation is different: within the
current component its limiting microscopic law is `pi_C`. On the slow
time `tau=epsilon*t`, component changes have rates
`sum_s pi_C(s) sum_(births s->D') b(s;birth)`; the embedded birth chain instead
normalizes those rates by the current component's mean total hazard.
At a deterministic slow time, conditioning on a record number also retains
the component holding-time selection; it need not give the event-indexed
mixture or the static mixture. Starting empty at fixed **physical** time
`t`, the probability of still being empty is exactly `exp(-36 epsilon t)`
and tends to one. None of the third-birth results is a fixed-time assertion.

## Reproduction, source identity, and limits

Run from `/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920`:

```bash
python3 .claude/science/mobile-record-formation-20260920/independent/check.py > .claude/science/mobile-record-formation-20260920/independent/RUN.log 2>&1
```

The successful command exited 0. `check.py` emits `results.json` (full exact
sums, quotient matrices, controls, and numerical evidence), `manifest.json`
(source paths, SHA-256 hashes, revisions, and package versions), and stdout
captured in `RUN.log`. No primary result is used as an expected constant.
The hand derivation, all-state rational enumeration, and symbolic
killed-generator solution are distinct calculation routes; the latter two
share this checker's explicit graph and weight definitions. They are not
claimed to be independent implementations of those input definitions.

Source identities used:

* Worktree HEAD and locally available `origin/main`:
  `5d784d8ccda5268f2b7c056fcdf0d81fdb703319`.
* Planning `origin/ai/execution`:
  `068e916ca37b004757ad3a3c082857a91dc37215`; its `AGENTS.md` SHA-256 is
  `b72ba953ee650b464b7987c71de3415de590be5aa42451240525a2b2585312e7`.
* Original PR 8530 head supplied in the handoff:
  `1c1a56df6c979401f94ff7191a5b18a1236f1b74`; the complete snapshotted
  moving-record note was read. Its SHA-256 is
  `3d1cd5f5f9101a2bd342c97e5f4fc14ca237cd60b13c275e9861ee2aaeb94cc8`.
* Local `AGENTS.md` SHA-256:
  `9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6`.
* `docs/ai_methodology/SCIENCE_WORKFLOW.md` SHA-256:
  `d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4`.
  Its Git blob matches the pinned main workflow.
* Workhorse skill SHA-256:
  `9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb`;
  the installed copy matches the pinned main skill blob. The freshness
  instruction SHA-256 is
  `b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0`.
* Executed independent `check.py` SHA-256:
  `f8412a6f6039e36e2c00324d38bb6b6c190f9a8fbcbd2089c139057354546295`.

Runtime: Python 3.13.5, NumPy 2.4.4, SymPy 1.14.0; SciPy 1.17.1 is
available but its solvers were not needed. No external literature was used.
The remote heads were not independently refreshed; the requested pinned
sources and locally resolved revisions identify this check. No source
files, prompts, audit records, branches, commits, or external services were
modified. Outputs are confined to the assigned independent directory.

This is a finite-graph result for the stipulated rates. It establishes no
infinite-volume limit, empirical prediction, universal ordering in other
models, or general content-count characterization at arbitrary densities.
The original note's other theorems and simulator claims were not audited.
Subsequent review of the primary candidate, if requested, belongs in a
separate source-bound report so this initial independence record remains
unchanged.

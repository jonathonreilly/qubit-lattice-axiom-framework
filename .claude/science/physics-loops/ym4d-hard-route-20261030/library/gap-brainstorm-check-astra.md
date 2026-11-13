# Repo search

Codex, OpenAI gpt-6-astra, xhigh; 2026-11-13; FINISH row 882. Source:
`gap-brainstorm-max.md` at `06200bc581915c89b21c057e360cd59be3660760`.
Cross-provider research check of Claude Fable 5.2 and Claude Opus 5.5's text;
not an audit, and no status granted. No numerical run supplies a proof.
Scope: the requested tube, strand, decoder, and thin-torus claims and seed
novelty. Other brainstorm ideas, simulations, and the Nishimori claim are
not checked. All relative paths below are inside this lane's `library/`.

The requested `prior/gap-brainstorm-check-astra.md` was absent. Read
`prior/repo-search-2026-11-08.md`; its targets concern the earlier ultraviolet
construction, not this decoder. No "Repo prior work" entry accompanies row
882. The workflow is absent in this sparse checkout; its map, rules and
check procedure were read from `origin/main`. The supplied pinned checkout
and sole-output instruction govern this task; no new campaign is launched.

Searches used the requested five refs in `/Users/jonreilly/Projects/Physics`:

| Ref | Revision read |
|---|---|
| origin/main | 993f5e4f6d11a7e20a1cab9612c5749a53bae073 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Terms: `SEED-DEC`, `TOP_j`, `tube.conditioned`, `hierarchical decoder`,
`homological percolation`, `strand.counting`, `twisted thin.torus`,
`chessboard.{0,35}(recurs|spin|signed)`, `twist.{0,30}covariance`, and
`4[.]684`. Each command was a bounded `git grep -n -i -E` over `*.md` and
`*.tex`, piped to `head`. An initial broad conserved-charge search reached
its cap with unrelated results and supplies no absence claim. Narrower
passes completed across all five refs. No exact decoder/seed target hit was
found; `seed-decoded` and a timestamp ending in `54.684` are false positives.

| Relevant source hit and lines read | Exact statement / closeness |
|---|---|
| pr/10134, lane `parts/hard-core--mapped.md:764–769` | "Unconditional chessboard on all-bad configurations" prices "a probability, not the odds at fixed V'". Prior use of the method, credited there to Froehlich, Israel, Lieb and Simon; no spin-cycle decoder theorem. |
| origin/main, `docs/work_history/repo/review_feedback/CYCLE703_LOCAL_CELLULAR_PLAQUETTE_DECODER_NOTE_2026-07-25.md:7–49,125–143` | A radius-one cellular rule solves lawful plaquette syndromes on finite **open** cubic boxes using a supplied coframe, corner and memory. "No periodic Wilson sector is present or tested." Related decoding vocabulary, different law, topology and objective. No SEED-DEC result is imported. |
| `gap-ext-astra.md:163–202`, (E5)–(E6) | For distinct disjoint representatives, the insertion-product mean is 1 for even cardinality and R for odd cardinality; covariance is exactly `1-R^2`. This is already the unconditioned tube calculation's input. Reuse it. |
| `gap-hs-max.md:100–113,168–170`; `gap-hs-check-astra.md:58–76,222–224` | Lemma OS expresses label probabilities by signed temporal-plaquette insertions. P1 identifies flux parity with cycle/cocycle pairing. The check preserves OS with its deletion-normalization repair and does not establish a general spatial-twist chessboard representation. These are inputs, not a decoder. |
| `gap-ac-lat.md:62–75`, Lemma B | For beta > 0 and even n >= 4, an explicit positive-half test has twisted reflection form `2(1-Z_0/Z_tw)<0`. This already covers Route 2's ordinary small-direction RP failure. Reuse it; no new attack on that result. |

Registry search: `seed-dec|top_j|brainstorm|decoder|homolog|twist|chessboard|spin.network`
in `open-registry.md` found no competing decoder/check owner. Its H-TREE and
PI-ADMIT hits concern Balaban polymer counting and background admission.
This check starts no attack on those rows, EXC, or any seed supplier.

Outline lookup came first: `sa-index/README.md`, `chunk-03.md:16–37` and
`obligations.md:74–85`. The latter requires positive bounded slab profiles.
Read the cited outline at `YM4_sketch_500.tex:2885–2942`, source revision
`31a47c543775`. Its (AM6) is the finite slab chessboard inequality, proved
there in detail, with slab-contained copied functions. Credit Ethan Sussman
and Levent Alpoge, with Claude and Codex as authors of their text, for this
existing argument, and Froehlich, Israel, Lieb and Simon for the method.
It supplies neither neighborhood-overlap bookkeeping nor a topological
decoder. No result of Tadeusz Balaban is newly imported here.

## 1. Tube covariance and conserved charge — HOLDS AFTER CORRECTION

Source lines 440–444; G1 at line 470. The covariance identity **HOLDS** for
the stated separated tubes. Use the already proved insertion algebra
`gap-ext-astra.md` (E5), rather than claim it as new. Write W and W' for
the two sheet ratios and F for the outside of both tubes. Locality gives
conditional independence of the two interiors, hence

```math
 E(WW'\mid F)=A_T A_{T'},\qquad
 E A_T=E A_{T'}=r,\qquad E(A_T A_{T'})=1.
```

Thus their covariance is `1-r^2` at every separation allowing this
conditional factorization. This is not a statement at coincident tubes;
`E A_T^2` need not equal 1.

For the transverse direction chosen as time, let C be the centre symmetry
which flips links of the other plaquette direction across a **spatial cut**.
Flipping every link on the slice is not the correct convention in general.
The sheet insertion is C in the transfer trace. With `rho=T^t/Tr T^t`,

```math
 C^2=1,\quad [C,T]=0,\quad
 r=\operatorname{Tr}(\rho C),\quad
 p=\operatorname{Tr}(\rho(1-C)/2),\quad
 \operatorname{Var}_{\rho}(C)=1-r^2=4p(1-p).
```

The trace with two C insertions at any time separation equals 1 after
normalization, by commutation and `C^2=1`. This is a different derivation
of the separation independence. Here p is the parity weight for the
chosen cut, not the union of all nonzero homology classes.

Correct the operator interpretation at lines 441–443: C **preserves** flux
sectors and commutes with the centre symmetry. Calling it "not flux-neutral"
is wrong if neutral means charge-preserving. It is a global sector
observable whose value differs between sectors. A_T is a positive
conditional likelihood ratio, not pointwise a random variable with values
plus or minus one. Equality of the displayed moments does not identify
these two objects as multiplication operators.

The sound conclusion is that these tubes do not give separation decay by
a within-sector clustering estimate alone. This is not a general theorem
that no additional tube estimate can constrain p. For translated identical
separated tubes, Cauchy–Schwarz gives `E A_T^2 >= 1`. Therefore
`Var(A_T)>=1-r^2`; the lower bound is not an upper bound on that variance.
The martingale statement at line 444 inherits the same qualification:
the bound applies while a translated disjoint tube with the same law fits.
Replace "every d below half the torus" by that geometric condition.

## 2. Strand threshold — FAILS as the stated numerical/universal claim

Source lines 665–666, repeated at 692 and 699. Separate three assertions.

**The two elementary chessboard facts HOLD on an admissible finite
chessboard.** Write `z_V(A)=P_V(all reflected cells satisfy A)^(1/N)`.
The chessboard inequality with one nontrivial factor gives `P_V(A)<=z_V(A)`.
For a union, expand the disseminated union into choices of events in each
cell. Apply the same inequality to each choice and sum. This gives
`z_V(union A_i)<=sum z_V(A_i)`. These are statements with one fixed torus,
cell partition, reflection rule, and compatible supports. They do not
supply a product estimate for arbitrary overlapping edge events.

**The symbolic SAW test HOLDS AFTER CORRECTION.** Assume separately the
required path estimate in a consistent norm,
`z_block(all edges of pi occupied)<=u^|pi|`, and the asserted inclusion of
bad blocks in long-path events. Let c_l count rooted nearest-neighbor
self-avoiding walks on Z^3, and let `mu_3=lim c_l^(1/l)`. For the particular
majorant `k_0^3 sum_{l>=k_0/2} c_l u^l`, convergence is equivalent to
`mu_3 u<1`. Indeed `c_(m+n)<=c_m c_n`, so `c_l>=mu_3^l`; at or above the
threshold its terms do not tend to zero. Below the threshold the root
test gives a geometric tail. If the same u satisfies `u>=p_edge`, this
majorant can work only if `p_edge<1/mu_3`.

This is a criterion for that majorant, not for every use of support
geometry or strand counting. It also presupposes the path norm inequality
and the bad-block inclusion; neither is proved for the proposed decoder.
An explicit hand bound is `c_l<=6*5^(l-1)` for l >= 1: six first steps,
then at most five choices after forbidding immediate reversal. It gives

```math
 k_0^3\sum_{l\ge m}c_l u^l
 \le {6k_0^3\over5}\,{(5u)^m\over1-5u},\qquad
 m=\lceil k_0/2\rceil,\quad 5u<1.
```

This is a sufficient condition, conditional on the path estimate, and
needs no numerical enumeration.

**The decimal 4.684 and the beta=2.3 exclusion do not HOLD as proofs.**
The source gives no exact value or rigorous bounds for mu_3, and no
source for making 4.684 an equality. Keep it, if desired, as GUIDE.
The density 0.267 is explicitly an unverified GUIDE. An upper bound of
0.5806 cannot establish a lower bound exceeding the proposed threshold.
Consequently this record establishes neither `p_edge>1/mu_3` at beta=2.3
nor the claimed failure of all support-based bounds there.

Density alone cannot prohibit successful use of geometry. On an even
periodic cubic lattice, tile each xy plane by disjoint four-edge unit
squares. Their union is the boundary of the sum of these plaquettes and
has V occupied edges among 3V edges. Average over translations and the
three orientations. Every edge has marginal 1/3, but every configuration
has zero homology and components of length four. This is a diagnostic of
the universal density inference, not a claim that this law is Wilson's.

## 3. Chessboard recursion and C_3 — FAILS under the stated premises

Source lines 638–646 (also G16). First failing step: applying a
one-cell chessboard product bound to the neighborhood-reading bad events,
then retaining exponent `2 N_(j+1)` "after the sublattice split".

**Signed insertions are not by themselves the problem.** By the corrected
Lemma OS, a bounded function f of finitely many edge labels has a signed
Wilson insertion F_f. For disjoint edge supports, `F_(fg)=F_f F_g`.
On supports contained in opposite spatial half-algebras, with compatible
reflections, bare Wilson RP therefore gives the label reflection form.
For beta finite the character sums converge absolutely: bound each
character by its dimension and use the finite sum `sum_j d_j^2 r_j`.
This justifies the observation for admissible separated supports on the
untwisted torus. It does not make arbitrary neighborhood events into
one-cell functions.

The multiplicative identification fails on shared edges. For the
half-integer event on one edge, its insertion is
`h(U)=(1-exp(-2 beta x(U)))/2`. The repeated label indicator is idempotent;
the repeated Wilson insertion is h squared, generally not h. For example,
at U=1 and beta>0, `0<h<1/2`. The proposed events read 3-fold
neighborhoods, and their neighbor-comparison clause reads still farther.
Two child centers separated by two block widths can have overlapping
reads. Neither TOP nor bare RP supplies the missing joint estimate.

**Explicit test of that inference.** Take independent fair bits X_x on a
3D periodic lattice of side `L=6r`. Product measure is reflection positive:
for a link-cut reflection the reflection form factors as the square of a
mean; for a site cut, condition on the fixed-plane bits first. Define the
reflection-covariant event

```math
 E_x=\{X_x=0;\ X_{x+e_i}=X_{x-e_i}=1\text{ for }i=1,2,3\}.
```

It reads a 3-cell neighborhood. Requiring E_x at every fine cell is
impossible, since neighboring centers demand both 0 and 1 at the same
site. Thus the source's all-cells norm is `z_0=0`.

Partition into 3-by-3-by-3 parent blocks. Use exactly the stated parent
rule: a parent is clean if its bad-child set has at most one star-connected
cluster of diameter at most one child width. Set X=0 precisely at
`3Z^3` and `3Z^3+(2,2,2)`, and X=1 elsewhere. No two zeros are nearest
neighbors: zeros of the same type have distance at least three, and
opposite types differ in all three coordinates modulo three. Hence E
holds at every zero and nowhere else. Each parent has two bad children,
at opposite corners, in separate star-clusters. Every parent is bad.
This single configuration has probability `2^(-L^3)`, so with
`N_1=(L/3)^3`,

```math
 z_{1,L}=P(\text{all parents bad})^{1/N_1}\ge 2^{-27}>0.
```

The bounds persist for every compatible L, and for any subsequential
limit used in place of the unproved limit. Therefore no finite constant
C can give `z_1<=C z_0^2` from RP and the separated-pair implication alone.
This tests the asserted probability lemma, not the existence of a Wilson
configuration with the author's as-yet unspecified filling event.

**What the constant would be with the missing hypothesis.** Suppose,
additionally, on every finite torus V and for every set S of distinct
child slots, one had the actual bound

```math
 P_V(\text{all slots in }S\text{ bad})\le u_{j,V}^{|S|}.
```

If every parent has 27 children and a bad parent requires two distinct
bad children, there are at most `binom(27,2)=27*26/2=351` unordered
witness pairs. Expand over one pair per parent. Distinct parents supply
`2 N_(j+1)` distinct child slots. Thus

```math
 P_V(\text{all parents bad})\le
 351^{N_{j+1}}u_{j,V}^{2N_{j+1}}.
```

With a compatible cell-local chessboard norm supplying that additional
bound, `C_3=351` works. This is an abstract corrected implication, not
the author's missing estimate. If a q-color support split retains only
`2N_(j+1)/q` witnesses, the direct estimate has exponent `2/q` in the
corresponding norm. A power loss cannot be replaced by a factor in C_3.
Changing to larger chessboard cells also changes the norm. The source
specifies neither repair and gives no actual C_3.

**Two further consumer mismatches.** A thermodynamic limit of all-bad
roots is not a finite-volume uniform estimate; its existence and finite
size control are not stated. Use finite-torus norms throughout, or supply
that comparison. Also even the corrected quadratic recursion gives only

```math
 u_J\le C^{-1}(C u_0)^{2^J}
 =C^{-1}\exp[-c(L/k_0)^{\log_3 2}]
```

when `L/k_0=3^J` and `C u_0<1`. This is stretched exponential in L.
Since `log_3 2<1`, it does not imply `C' L^p eta_*^(L/2)` for a fixed
`eta_*<1`, as required by (E17). The source's earlier single-scale
wrapping-animal criterion would have a different, linear-in-L exponent;
Stage A2 does not prove that criterion.

Finally the actual (E17) maximum includes magnetic backgrounds:
`gap-expose-astra.md:575–599` takes `max_(m_2=0,i=3,4) p_(m,i)`.
Untwisted spatial RP does not automatically cover that family. Lemma B
already disproves ordinary RP across a magnetic twist. A new comparison
or a different consumer is needed before this route supplies all of (E17).

## 4. Local filling argument and TOP_j

**Stage A1, line 634 — HOLDS AFTER CORRECTION of scope.** For each fixed
proper local block, a wrapping line can be put outside its read set.
Adding it changes the homology without changing that block's data. This
proves that one block cannot determine global homology. It does not give
two distinct configurations which agree "in every block" simultaneously;
blocks covering the torus determine all edges. Nor does it rule out a
single-scale collection of local tests with a global wrapping-cluster
criterion, which is exactly the earlier DEC_k proposal.

The relative filling assertion `H_1(B^3,S^2;Z_2)=0` is correct. The chain
area identity `|D+S|-|D|=|S|-2|S intersect D|` is also correct, with
addition modulo two. A density near one half makes this particular strip
cheap only when the density on that strip is near one half. A global
filling density alone does not prove that property for every strip.

**Stage A2, line 636 — FAILS as a proof; TOP remains OPEN.** The source
itself labels this a design sketch. Its first unsupported inference is
"the clean sub-blocks' local fillings patch". No compatible filling map,
chain equation on overlaps, or bound on the support of the correcting
chains is given. The stated cleanliness criterion is not yet an
unambiguous replacement for these data:

- "Modulo boundaries of 3-chains of diameter at most k_0/4" must specify
  whether it allows one such chain or their generated subgroup. The first
  relation need not be transitive: two separated small modifications have
  a union of large diameter. Allowing arbitrary sums loses that diameter
  control. The sketch does not choose or prove the control it uses.
- Local vanishing of `H_3` is not a gluing argument. A good cover of a
  torus has contractible intersections but the torus still has nonzero
  `H_1`. One must control the overlap data on its nerve. Moreover the
  fillings here are relative: `H_3(B^3,S^2;Z_2)=Z_2`, whereas
  `H_3(B^3;Z_2)=0`. The sketch gives no construction which licenses its
  choice of the latter group for the patching obstruction.
- The base event compares fillings with neighboring neighborhoods; the
  higher-level event merely counts bad sub-blocks. No induction carries
  a chosen relative filling, compatibility data, and controlled boundary
  traces from one definition to the next. At the last level the whole
  torus is not a ball. The final noncontractible seam cannot be discarded.

The elementary part does hold: for the stated cluster/diameter rule,
a bad parent contains two bad child blocks more than one block apart in
the block-index maximum norm. If there is one cluster of diameter above
one, choose diameter endpoints; if there are several clusters, choose
one member in each of two clusters. But this supplies neither disjoint
3-fold reads nor the asserted implication from nonzero homology to a
bad top block. It therefore does not repair section 3.

This verdict identifies a failed proof step, not a counterexample to a
fully specified Wilson TOP theorem. A chain-level construction with a
precise boundary and terminal rule is still required. This check does
not take over that open proof task.

## 5. Route 2: finite bound — HOLDS

Source lines 650–652. Use beta >= 0 and the periodic lattice convention
of the cited transfer construction. There are exactly n squared probe
plaquettes, and the background n_12 changes no sign on them. With
`X=sum_(p in Sigma_34) x_p`,

```math
 r=E_{12}e^{-2\beta X}\ge e^{-2\beta n^2}>0.
```

For the other side choose direction 3 as time. The magnetic n_12 seam
is part of a real spatial potential. Its half-weight is a bounded
positive multiplication operator A. The untwisted temporal convolution
K is positive and commutes with the gauge projection P, so the transfer
`T=A K P A` is positive. The direction-4 cut involution C commutes with
T: it preserves every spatial plaquette, including the n_12 ones.
The normalized trace of `C T^M` is the probe ratio. Hence

```math
 1-r={\operatorname{Tr}((1-C)T^M)\over\operatorname{Tr}T^M}
     =2{\operatorname{Tr}(P_-T^M)\over\operatorname{Tr}T^M}\ge0.
```

Pointwise positivity of the twisted integral supplies strict positivity
of r; positivity of T alone would not supply that part. Combining gives
`0<=-log r<=2 beta n^2`, with the stated constant 2. At beta=0, r=1.
No volume limit, mass gap, or semiclassical input is used.

## 6. Route 2: ordinary RP failure — HOLDS AFTER CORRECTION of scope

Source line 657. This result is already covered by `gap-ac-lat.md`,
Lemma B, lines 62–75. Stop the duplicate proof task and reuse its explicit
witness. For the singly twisted background, beta>0 and even n>=4,
it proves `Z_tw<Z_0` and constructs a positive-half test F with

```math
 E_{tw}[\theta F\,F]=2(1-Z_0/Z_{tw})<0.
```

This establishes failure of the specified ordinary link reflection
across the twist column. The source's alternating character coefficients
identify why the standard crossing-kernel proof fails; a negative
coefficient by itself should not replace this full-measure witness.
At beta=0 the measure is Haar and RP holds, so the failure is not a
statement for every beta including zero.

The long-direction RP assertion applies to **Z(n_12,0)**. Its seam is
spatial for time 3 or time 4 and is absorbed in A as above. It must not
also be asserted for **Z(n_12,n_34)**, whose probe seam crosses those
long-direction cuts. Likewise this says nothing about a modified
reflection with a compensating centre transformation. The ordinary
small-direction chessboard comparison of the stated twisted measures
is unavailable; no general comparison theorem is disproved here.

**Stage 1b, lines 654–655 — FAILS as a deduction from Stage 1a.**
The n-dependent constant bound on `-log r` does not show that r tends
to one with M. If sigma(n) is a Wilson-loop string tension, no converse
from its area law to the needed finite-torus vortex estimate is supplied.
If sigma(n) instead denotes a proved finite-volume electric-flux rate,
state that estimate, including its prefactor and size of onset. Only
such an additional estimate licenses the asserted decay of `1-r`.
An asymptotic at each fixed n also gives no uniform diagonal estimate
at M=n. Thus `Sigma=n^2 sigma(n)` is a proposed variable and MON' is
still a conjecture. Neither the `log 5041` hand-off nor the growth per
doubling is proved by the bound checked in section 5. The source already
labels the semiclassical/group comparisons ARGUED; they remain outside
this check and supply no substitute.

## 7. Is SEED-DEC new? — HOLDS AFTER CORRECTION to bounded novelty

Source lines 672–677. The specific proposed combination is new **within
the searched lane**: a filling-based decoder for the half-integer slice
cycle, with a chessboard smallness test. No earlier supplier of its event,
TOP, C_3, or seed was found. This is not a theorem of global priority.

The lane-library searches excluded the source and this report. Terms
`SEED-DEC|TOP_j|homological.percolation|Harrington|Kubica|Dennis.*Kitaev|local.stochastic.noise|minimal filling|relative filling`
returned no earlier matching statement. The same object terms in the
whole `sa-index/`, including its account index, returned no hit. This is
an index search, not a claim to have read the whole account anew.
A broader `decoder|decoding|Nishimori|self.avoiding` search found:

| Prior source | What it actually provides |
|---|---|
| `gap-rtail-check-opus.md:16–30`; `gap-rtailsos-opus.md:113–133` | Deterministic inverse codes for counting surfaces, not correction of slice homology. No duplicate SEED-DEC. |
| `gap-brainstorm2-max.md:146,477–484` | A parallel Nishimori idea and an explicit comparison with row 859's decoder; not a prior decoder proof. |
| `prior/gap-crux-lit-cross.md:69–75` | Paul Duncan and Benjamin Schweinhart's Potts-gauge / plaquette-percolation sharpness results, using a finite-coefficient random-cluster representation and FKG/Holley inputs. The digest expressly distinguishes this from SU(2). |
| `prior/gap-lit-grok.md:71–82` | The same Duncan–Schweinhart result, and finite-centre comparisons; no SU(2) decoder seed. |
| `prior/gap-lit-annealed.md:45–58` | Jan Swart, Réka Szabó and Cristina Toninelli's Toom-contour bounds concern monotone update noise; they do not supply the dependent Wilson slice event. |

The target itself credits Dennis–Kitaev–Landahl–Preskill, Harrington,
Gács, Kubica–Preskill, Gottesman, Froehlich–Israel–Lieb–Simon and Biskup
for decoding, hierarchical threshold arguments and chessboard estimates.
Those attributions are recalled there, not verified primary-source
comparisons. No original literature paper was fetched outside the user's
permitted source directories. The available literature digests support
"related methods already exist"; they do not establish that this exact
combination is absent from the literature. Literature novelty is therefore
**unestablished**, not certified NEW.

A final whole-repository follow-up on all five refs used
`(decod|chessboard).{0,60}(confin|spin.network|half.integer)` and its reverse,
plus `local.stochastic.noise|Harrington|Kubica.Preskill|Dennis.Kitaev.Landahl`.
It completed with only an unrelated "not confined ... decoding" match in
`docs/MENU_INDEPENDENCE_IS_INDEPENDENT_OF_THE_AXIOMS_AND_INSUFFICIENT_WITH_THEM_THE_BORN_FORM_NEEDS_MENU_ABUNDANCE_BOUNDED_THEOREM_NOTE_2026-09-03.md:25`.
Together with the concrete Cycle 703 comparison above, this found no
outside-lane supplier. It is a bounded textual search, not exhaustive
mathematical classification of every differently worded route.

The stronger novelty claim should be replaced by: "A candidate application
of known decoder and chessboard ideas to the SU(2) slice law, not previously
found in the searched lane. Its topology, probability bound, constant,
finite-volume/twist scope and exponential-rate bridge remain unproved."
Neither SU(2)-selectivity of this event nor smallness at a few correlation
lengths has been established. Thus SEED-DEC is not yet a proved alternative
finite-volume criterion or a proved reduction of SEED-FP/E17.

## Disposition

| Statement | Verdict |
|---|---|
| Separated tube covariance `1-r^2=Var(C)` | HOLDS; operator-neutrality and geometry language HOLDS AFTER CORRECTION |
| Cell-local chessboard domination and union inequality | HOLDS on the stated finite admissible board |
| Symbolic `mu_3 u<1` criterion for the displayed path majorant | HOLDS AFTER CORRECTION to the explicit conditional claim |
| Exact `1/4.684` threshold and beta=2.3/all-strand exclusion | FAILS as proved claims |
| Recursion from TOP's pair condition and bare RP; actual C_3 | FAILS; the overlapping-event inference has a hand counterexample |
| Single-block indistinguishability argument | HOLDS AFTER CORRECTION of its quantifiers and scope |
| TOP sketch | FAILS as a proof; the defined-and-proved theorem remains open |
| Route 2 `0<=-log r<=2 beta n^2` | HOLDS |
| Ordinary small-direction RP obstruction | HOLDS AFTER CORRECTION of scope; already Lemma B |
| Stage 1b's decay/diagonal hand-off from Stage 1a | FAILS as a deduction |
| SEED-DEC novelty | HOLDS AFTER CORRECTION: new candidate in searched lane; literature priority unestablished |

Completed the requested research check. No source note, registry, FINISH
row, audit record or remote was changed. No numerical proof or simulation
was run. The supplied SA source revision is recorded as provenance; the
source directory has no Git metadata, so its revision could not be
independently resolved with `git rev-parse`. This file is saved locally,
without a commit or push. The next decision is whether to develop a precise
cell-local decoder with an exponential-rate consumer, not to estimate a
seed for the currently invalid recursion.

RESULT: The tube identity and thin-torus finite bound survive, and the ordinary RP obstruction is prior work. The numerical strand exclusion and the stated chessboard recursion FAIL; C_3 is not supplied, TOP remains open, and even abstract squaring on tripling scales does not deliver E17. SEED-DEC is a new candidate packaging in the searched lane, with literature novelty unestablished; no mass-gap result or scientific status is granted.

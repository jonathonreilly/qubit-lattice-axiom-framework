# Geometric rare-birth selection: independent check

**The connectivity proof and the uniform first-full limit reconstruct. One
narrow prose correction, F1 below, remains in the reviewed source.** It
concerns subsequent observation times, not Eq. (5). No other mathematical
defect or prose/code drift was found within this bounded review. This is
scientific scrutiny, not a retained-status, audit or landing decision.

## F1 — qualify the post-filling observation rule

At note line 135, “Total-variation contraction makes any later observation
time at fixed N no worse than the initial discrepancy” needs a common-time
qualification. The valid statement is:

> At any common deterministic elapsed time after first filling, or after an
> independent random delay, the discrepancy from Uniform(F) cannot increase.

It does not cover state-dependent stopping/observation rules. A symmetric
two-full-matching flip chain started uniformly, then observed at its first
visit/return to a specified matching after a positive departure time, is
observed at that matching with probability one. Its TV discrepancy is 1/2
despite zero initial discrepancy. A deterministic absolute deadline also
requires treatment of the random filling time and any conditioning; it is
not automatically a common elapsed-time semigroup kernel.

The parent has acknowledged this intended scope and will make the narrow
correction after this report is sealed. The source examined here remains
unchanged. No repair to Eq. (5), the rates or the connectivity proof is needed.

## Reconstructed proof and precise hypotheses

Let G be finite, connected, k-regular, bipartite and simple, with k>0 and
K vertices per side. Connected regularity implies strict Hall expansion for
each nonempty proper subset S of either side. Equality in the degree count
would exhaust all incident edges and isolate S union N(S), contradicting
connectedness. The K=1 case has no nonempty proper subset and is harmless.

For a near-perfect matching M with vacancies l0,r0, direct l to l' when an
occupied neighbor r of l is partnered to l'. If S is reachable from l0,
every neighbor of S except possibly r0 is matched into S minus l0. Hence
|N(S)|<=|S|, forcing S to be the whole side. A shortest path has distinct
vertices and matched intermediates, so its slides remain legal and move
the L vacancy arbitrarily while fixing the R vacancy. The analogous R-side
operation then aligns both vacancies with those of a target matching.

The remaining symmetric difference is a union of alternating cycles. Take
a shortest vacancy path to one cycle. Its final matched R-L edge enters
the cycle; all earlier vertices lie outside. On reaching the cycle, the
entering R vertex is temporarily paired to the preceding external L vertex.
Follow the target alternating edges around the cycle, use that temporary
pair for the final slide back to the exterior, and reverse the earlier
approach slides. This flips exactly the cycle, restoring the outside edges
and both vacancies. Repeating connects every pair of near-perfect matchings,
including changes carried by winding cycles. It is a geometric argument,
not an assertion of ergodicity of the immutable marked configurations.

The geometric conservative generator S is therefore irreducible and has
uniform invariant measure pi. Fixed, finite, nonnegative symmetric extra
conservative channels on this matching space preserve that law and the
irreducible slide subgraph. Pair number must remain fixed. The essential
parameters are fixed kappa>0 and equal rate beta for each vacant birth edge;
the proof uses the matching projection whose validity was established in
the unchanged prerequisite.

At this penultimate level, a simple graph has at most one vacant birth edge.
Let h indicate its availability and a_F indicate completion to a specified
full matching F. The next-birth probability solves

    (-S+beta diag(h))u_beta=beta a_F,    0<=u_beta<=1.

Every subsequential beta-down-to-zero limit is S-harmonic and hence constant.
Multiplying the exact equation by pi determines that constant as
pi(a_F)/pi(h). Each perfect matching has exactly K one-edge deletions, and
each enabled near-perfect predecessor has one completion. The ratio is
therefore `1/number_of_perfect_matchings`. Finite state spaces make convergence
uniform over starting states and, consequently, over beta-dependent entrance
laws. The previous filling theorem and the strong Markov property extend it
to every initially nonfull matching without requiring equilibration at any
earlier pair count. An initially full state is correctly excluded.

This is the law at the random first-full event. It is not the configuration
at a fixed physical time with beta tending to zero, nor the beta=0 process.
The graph and conservative rates stay fixed; no error or mixing estimate
uniform in graph size has been proved. Even tori N>=4 meet the graph
hypotheses, so beta-down-to-zero followed by N-to-infinity is a permitted
ordered statement. Its existence does not identify the latter equilibrium
limit or justify a fixed-positive-rate thermodynamic law. Symmetric full-state
flips preserve uniformity even without communication across all full-state
components, subject to F1's observation rule.

## Independent controls and countercontrols

Before author-code access, the independent implementation checked all 106
labeled connected regular bipartite graphs with at most four vertices per
side and all 2381 near-perfect states. Every fixed-opposite-vacancy test and
slide-connectivity test passed. Explicit transformations of all ordered
near-perfect pairs on C6, C8, K3,3, K4,4 and the cube included 9074 cycle
excursions. Separate 4^3-torus examples flipped a distant plaquette and a
winding axis cycle; each required four approach slides and nine total slides,
with every outside edge and both vacancies restored. These finite controls
test the general proof; they do not replace it.

Exact killed-generator controls on C4 and C6 confirm uniform rare selection
from every near-perfect state. Countercontrols show why the qualifications
matter:

- Two disconnected C4 components are regular and bipartite, but an initial
  full matching in one component can remain fixed. A near-perfect initial
  state's rare full law is `(1/2,1/2,0,0)` on four targets, TV 1/2 from uniform.
- Nonregular P4 violates the intermediate fixed-opposite-vacancy reachability
  assertion. This does not claim regularity is necessary for every possible
  final-selection theorem.
- Asymmetric additional conservative rates or unequal per-edge birth rates
  give the C4 rare full law `(3/5,2/5)` instead of uniform.
- From a specified C4 near-perfect edge, the probability of its full extension
  is `(b+2)/(b+4)` at kappa=1. Thus zero slides give a point mass; holding
  beta/kappa=1 while sending both rates to zero retains 3/5, not 1/2. Starting
  already full also retains the initial first-full law.

The independently reconstructed cube harmonic problem gives exactly

    P_columnar(b)=(6 b^3+77 b^2+308 b+308)
                   /[7(b+6)(3 b^2+19 b+22)].

The ten-state automorphism quotient was checked on every matching, and its
lifted solution satisfies all 99 original transient equations and nine full
boundary values. It gives 699/2156 at b=1, slow limit 1/3 and fast limit 2/7.
For every b>0 its difference from 1/3 is
`-b(3 b^2+28 b+28)/[21(b+6)(3 b^2+19 b+22)]<0`.
The separate no-slide deposition process on the cube fills with probability
17/21 and has columnar probability conditional on filling 6/17. Its
unconditional columnar probability happens to be 2/7; that equality does
not identify it with the positive-kappa fast-birth limit, which eventually
fills almost surely.

## Author comparison, evidence and read limits

The complete 156-line note and 286-line author runner were read. Blind work
was frozen first in `PRE_COMPARISON_SEAL.json`, SHA-256
`f7fb9f89ffbf0e643b0136659a38cec7b15af484b3163731c5e23299fa2db665`.
All twelve pre-seal artifacts remain unchanged. The author implementation's
vacancy paths, cycle excursion, exact harmonic lift and fixed-graph killed
chain match the proof. The four recorded author groups and all four source
bindings match their complete successful stdout; stderr is empty.

After sealing, a separate comparison checker regenerated every cube
certificate row from this reviewer's matching rates. It also independently
recomputed the full 44-near-state by 9-target killed-chain absorption matrix
at beta=1,1/10,1/100,1/1000 and matched all four exact worst-start TV values.
The first is 1334/3791; the last is approximately 0.000643416. These values
are finite controls, not a uniform bound in graph size.

The author's exact chosen-path event/cycle counts and eight N=4,6,8,12
periodic path receipts were authenticated and their implementing code read,
but those histories were not replayed. Separate blind periodic excursions
provide the independent path checks. Author counts are not relabeled as
independent calculations. No author runner was imported or executed.

| Frozen primary source | SHA-256 |
|---|---|
| `GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md` | `b6ae15f48bdab91922f13ff610853646a7cf91c74391d55887af39b583584611` |
| `geometric_rare_birth_check.py` | `2b34607932623c47e8744203bb5da18b6cae7b42eea248c7e2043301ddff5a3b` |
| Prerequisite `GEOMETRIC_PARTNER_RECORD_FORMATION.md` | `1bc76bc39c672c7eec318fb4e999dc6e2b1f80aad9a058683dbeb7f7ae247969` |
| Prerequisite `geometric_partner_formation_check.py` | `3766230651e8e69c8f51228cd3c3e7ded55140e96bf4b28255042e28e87cb259` |

Parent-supplied commit `f75352c70e914cb167ee03a1113f11c6810a4e11` was not
queried by Git. `FINAL_SEAL.json` binds all reviewed sources, outputs,
prerequisites, procedures and review artifacts. The exact-content-recognition
gap and supplied rotation/rule/clock choices remain those of the prerequisite.
No production screen, phase, fixed-rate thermodynamic, marked-state ergodicity,
quantum or wave claim was inspected or inferred. No primary or prompt file
was edited, and no formal audit status was applied.

Reproduction in this directory:

```
python3 independent_check.py --out INDEPENDENT_RESULTS.json
python3 additional_controls.py --out ADDITIONAL_RESULTS.json
python3 comparison_check.py --out COMPARISON_RESULTS.json
```

All runs passed on their first attempt; full stdout/stderr and command/source
receipts are present. The checker imports only the unchanged previously
sealed independent matching primitives. The comparison authenticates frozen
source paths/hashes, so later source corrections need a separate acknowledgment
rather than rewriting this evidence. Detailed reconstruction remains in
`PRE_COMPARISON_DERIVATION.md`.

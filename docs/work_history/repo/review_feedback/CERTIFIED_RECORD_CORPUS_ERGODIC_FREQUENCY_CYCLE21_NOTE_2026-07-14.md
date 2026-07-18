# Certified Record Corpus and Ergodic Frequency — Cycle 21

**Date:** 2026-07-14

**Type:** weakest-positive frequency theorem, record-visible reset/close audit,
exact finite process tournament, primary-source boundary, and N1--N8
scoped-negative gate

**Authority:** none. This review-feedback note is not a retained theorem,
audit verdict, axiom proposal, primitive, probability law, reset rule,
stationary-state selection, exact-law registration, or owner ruling. It
changes no axiom, primitive, registry, audit, queue, policy, or retained
surface. It creates only this authority-free note and its exact companion
runner.

**Companion runner:**
`scripts/certified_record_corpus_ergodic_frequency_cycle21_2026_07_14.py`

## Result Up Front

The probability-to-frequency seam can close without IID and without a new
probability rule. The exact minimum is an ergodic-component statement about
the joint record law already extending Cycle 20's `W`.

Let visible reset/outcome/close records define an infinite sequence of trial
blocks, and let `X_n` be the record-defined indicator of one outcome in block
`n`. Suppose the exact law gives a projectively consistent stationary measure
`mu` on those blocks, with the Cycle-20 one-block weight

```text
E_mu[X_0]=q=Tr(sigma E).
```

For the block shift `T`, let `I_T` be the invariant sigma-algebra. Birkhoff's
ergodic theorem gives the strongest general result:

```text
F_N=(1/N) sum_(n=0)^(N-1) X_n
   -> E_mu[X_0 | I_T]                       mu-almost surely.
```

Therefore the empirical frequency converges to the Born/effect weight `q`
exactly when

```text
E_mu[X_0 | I_T]=q                           mu-almost surely.
```

Call this the **component-mean condition**. It is weaker than global
ergodicity: a nonergodic mixture can still satisfy it when every invariant
component has the same outcome mean `q`. Ergodicity is a clean sufficient
condition because it makes `I_T` trivial. IID, finite-state irreducible Markov
dynamics, mixing, and deterministic unique ergodicity are progressively
different sufficient routes, not definitions of probability.

The bare-metal certificate result is equally sharp:

> Visible certificates define blocks, not independence.

A reset record can certify that a named preparation map ran, if the exact law
gives it that ancestry. A close record can certify that a finite named input
interface is complete. From the record contents alone one can define the trial
index, outcome count, and finite empirical frequency. But identical visible
reset/close labels do not prove that old archive or sector information has
stopped influencing the next block.

The exact controls compare six stationary processes with the same one-shot
marginal `q=1/3` and the same reset/outcome/close skeleton:

| process | causal memory | limiting frequency |
|---|---:|---|
| IID Bernoulli | none | `1/3` almost surely |
| two-state irreducible aperiodic Markov | last outcome | `1/3` almost surely |
| exchangeable frozen mixture | one permanent bit | `0` or `1` |
| deterministic period-`001` cycle | phase modulo three | `1/3` for every phase |
| nonergodic IID/periodic equal-mean mixture | permanent component label | `1/3` almost surely despite nonergodicity |
| two permanent deterministic sectors | sector plus phase | `1/4` or `1/2` |

Every process is finite-state and causal-local. Every stationary slot has
one-shot marginal `1/3`. Their empirical limits differ. Thus stationarity plus
causal locality does not imply ergodicity.

The collapsed result is:

```text
operational definitions:
  trial block, outcome decoder, count, finite empirical frequency,
  and preparation/effect equivalence

law-owned or law-proved:
  certificate ancestry, endless recurrence/projective consistency,
  W-to-block marginal identity, stationarity, archive/sector coupling,
  and the component-mean condition

mathematical theorem:
  Birkhoff converts those clauses into the asymptotic frequency law

actual-member semantics:
  remains separate for a pointwise claim about the realized stochastic
  history; deterministic unique ergodicity can avoid this last seam by
  proving convergence for every orbit.
```

Strong predictive reset gives IID. A finite irreducible Markov law gives an
ergodic corpus without predictive reset. Deterministic unique ergodicity gives
pointwise frequencies without sampling. The component-mean condition is the
weakest stationary condition for the one declared outcome.

No axiom text is proposed. If `W` already means a complete, projectively
consistent global record-process law, this cycle adds no independent law
object: stationarity and component means are theorem obligations on `W`. If
`W` is only a one-experiment law, then its finite/infinite process extension is
the remaining law-owned content.

## 1. What a Record-Visible Trial Is

Fix three record roles:

```text
R_n = preparation/reset certificate for block n,
O_n = outcome record for block n,
K_n = close certificate for block n.
```

The exact spelling is not important. What matters is that the record contents
and their causal ancestry make the block boundaries readable. A finite corpus
is then

```text
(R_0,O_0,K_0),...,(R_(N-1),O_(N-1),K_(N-1)).
```

For a binary outcome decoder `x(O_n) in {0,1}`, define

```text
C_N=sum_n x(O_n),
F_N=C_N/N.
```

These are definitions on actual permanent records. They need no ensemble,
typicality statement, or external clock. The block count itself is a local
commit-count clock once the physical block event has been identified.

The definitions do not establish four physical claims:

1. that certificates recur indefinitely;
2. that every `R_n` has the claimed preparation ancestry;
3. that the conditional state after `R_n` is independent of prior blocks; or
4. that the joint block law is stationary or component-mean homogeneous.

The first two are exact-law occurrence/ancestry claims. The latter two are
joint-process claims.

## 2. Reset Certificate, Close Certificate, and Predictive Reset

The existing finite constructions already separate three roles.

### Preparation certificate

Cycle 14 appends its certificate `C` only after a local reset channel maps the
fresh triple to the declared target. Inside that candidate law,

```text
C present -> the reset map ran -> the declared local target was prepared.
```

This is genuine certificate semantics because the transition list supplies
the ancestry. The reset target, archive behavior, and occurrence rule remain
candidate-law content.

### Causal-close certificate

Cycle 16's `K` records prove that conserved proposal fronts have reached the
stops of two finite, explicitly named ports and that their wakes block later
same-port traffic. They certify finite-interface completion. They do not say
that a remote sector record was erased, that the next preparation is
independent of earlier outcomes, or that the entire universe has no relevant
memory.

### Strong predictive reset

The condition that actually gives IID is:

```text
P(X_n=x | X_0,...,X_(n-1), all prior block records)=p(x)
```

for every lawful prior transcript and every `n`. For the complete operational
version, the conditional law of **every future certified-block protocol**
after `R_n` must be the same preparation-class law, not only the next outcome
marginal.

The one-step equation and the chain rule give

```text
P(X_0=x_0,...,X_(N-1)=x_(N-1))=product_n p(x_n).
```

Thus strong predictive reset gives IID. It is a law theorem about what the
certificate means, not a consequence of printing the same certificate label.

Permanent records make this distinction unavoidable. The global
configuration after trial `n` contains a larger archive than after trial
`n-1`. A reset may still restore the **port's complete predictive equivalence
class** if the exact law proves archive decoupling. It cannot literally return
the whole universe to an earlier record configuration.

## 3. Stationary Certified-Block Law

Let `Omega` be the space of infinite certified outcome sequences and `T` the
one-block left shift. A measure `mu` is stationary when

```text
mu(T^(-1)A)=mu(A)
```

for every measurable transcript event `A`.

Stationarity says every block position has the same distribution. It does not
say distant blocks become independent, that invariant sectors are absent, or
that time averages equal the unconditional mean on each actual component.

Cycle 20's one-block law `W` gives, for an operational preparation `s` and
effect `E`,

```text
q=p(E|s)=Tr(sigma_s E).
```

The repeated-process link is the identity

```text
E_mu[X_0]=q.
```

If `W` is already a complete process law on every finite adaptive certified
protocol, this identity and the finite cylinder laws should be restrictions
of that same object. Projective consistency then makes the corpus a law-owned
process rather than a second probability postulate. If `W` was deliberately
one-experiment only, the consistent joint family remains to be supplied or
derived.

Stationarity can have three placements:

- forced by a unique invariant law/component;
- proved after a reset or Markov theorem; or
- selected by the actual boundary/initial ensemble when several invariant
  measures exist.

The word “stationary” should not hide which placement is used.

## 4. Weakest Stationary Frequency Theorem

Let

```text
X_n(omega)=X_0(T^n omega)
```

be a bounded record-defined outcome. Birkhoff's pointwise ergodic theorem
applied to `X_0` gives

```text
lim_(N->infinity) F_N(omega)
  = E_mu[X_0 | I_T](omega)
```

for `mu`-almost every `omega`, where `I_T` is the invariant sigma-algebra.

This gives the exact hierarchy.

### Observable-specific minimum

For this one outcome, the necessary and sufficient stationary condition for
the almost-sure limit to equal `q` is

```text
CM(q): E_mu[X_0 | I_T]=q almost surely.
```

Equivalently, almost every invariant/ergodic component has the same `X` mean
`q`. Other observables may still distinguish those components. This is why
global ergodicity is sufficient but not necessary.

### Ergodic sufficient condition

If the shift is ergodic, every invariant measurable function is constant, so

```text
E_mu[X_0 | I_T]=E_mu[X_0]=q.
```

No independence or mixing is needed.

### Mixing sufficient condition

Mixing implies ergodicity and can provide rates, variance bounds, and
concentration. It is stronger than the bare frequency theorem.

### IID sufficient condition

IID is stronger still. It gives the binomial law and familiar
`q(1-q)/N` frequency variance. Demanding IID when only a law of large numbers
is needed overprices the seam.

## 5. Exact Process Tournament at `q=1/3`

All six models below use binary outcomes and the same visible
reset/outcome/close skeleton. Every slot has marginal

```text
P(X_n=1)=1/3.
```

### 5.1 IID Bernoulli

```text
P(x_0,...,x_(N-1))
 = product_n (1/3)^(x_n) (2/3)^(1-x_n).
```

Every prior transcript gives the same next weight `1/3`. The count moments
are

```text
E[C_N]=N/3,
Var(C_N)=2N/9,
Var(F_N)=2/(9N).
```

This is the strong-reset route.

### 5.2 Finite-memory mixing Markov law

Use transition matrix

```text
P = [[3/4, 1/4],
     [1/2, 1/2]]
```

with stationary distribution `(2/3,1/3)`. The nontrivial eigenvalue is
`1/4`, and for the outcome indicator

```text
Cov(X_0,X_k)=(2/9)(1/4)^k.
```

Therefore

```text
Var(C_N)
 = (2/9)[N+2 sum_(k=1)^(N-1) (N-k)(1/4)^k],
```

and `Var(F_N)` vanishes. Every transition is positive, so the finite chain is
irreducible and aperiodic; its stationary path shift is mixing and hence
ergodic.

This process does **not** have strong predictive reset:

```text
P(X_(n+1)=1|X_n=0)=1/4,
P(X_(n+1)=1|X_n=1)=1/2.
```

It nevertheless has the required long-run frequency. A repeatable empirical
corpus is therefore more general than an IID reset corpus.

### 5.3 Exchangeable frozen mixture

Choose one permanent bit `B` with

```text
P(B=1)=1/3
```

and write `X_n=B` in every block. This law is stationary and exchangeable;
every finite permutation of trial labels leaves it unchanged. It is also
causal-local: the next outcome reads one persistent bit.

But

```text
F_N=B,
Var(F_N)=2/9
```

for every `N`. In de Finetti language, the directing parameter is
`Theta=B`; the one-shot weight is `E[Theta]=1/3`, while the empirical limit is
`Theta`, not its mean.

This is the exact failure of “exchangeable means repeated fair trials.”

### 5.4 Deterministic uniquely ergodic period-`001`

Take three phase states in one cycle and decode them as `0,0,1`. The unique
invariant measure is uniform on the phases. The transition is periodic and
does not mix, but every actual phase orbit obeys

```text
|F_N-1/3| <= 2/(3N).
```

Thus every orbit has frequency `1/3`. This route needs neither sampling nor an
almost-sure typicality step. The exact deterministic law, physical decoder,
and selected three-cycle component remain law/domain content.

### 5.5 Nonergodic equal-component-mean mixture

Attach a permanent component record selecting either:

- IID Bernoulli `1/3`; or
- the deterministic `001` cycle.

Mix the two stationary components equally. The component label is invariant,
so the full process is not ergodic. Yet both component means equal `1/3`, and
both component frequencies converge to `1/3`. Hence `CM(1/3)` holds.

This exact control proves that global ergodicity is not the minimum. The
frequency theorem is observable-specific.

### 5.6 Nonergodic permanent sectors with unequal means

Attach a permanent sector record selecting either:

- deterministic period `0001`, mean `1/4`, with sector weight `2/3`; or
- deterministic period `01`, mean `1/2`, with sector weight `1/3`.

The unconditional one-shot mean is

```text
(2/3)(1/4)+(1/3)(1/2)=1/3.
```

The actual limiting frequency is `1/4` or `1/2`. Its between-sector variance
is `1/72`, not zero. The sector bit and phase are finite local causal state;
stationarity and locality remain intact.

This is the permanent-record version of the component-mean failure. If the
sector record is included in the complete preparation class, `W` should be
conditioned on it and returns the sector-specific weight. If it is ignored,
the averaged `1/3` is not the actual component's repeated-trial frequency.

## 6. What Causal Locality Does and Does Not Buy

Causal locality is compatible with all six processes:

- IID uses no memory;
- Markov uses the previous outcome;
- frozen exchangeability uses one permanent sector bit;
- the deterministic cycle uses a local phase state;
- the equal-mean mixture uses one component bit plus its component state; and
- the permanent-sector mixture uses one sector bit plus a finite phase.

Locality bounds which state can affect the next block. It does not make that
state forgetful, irreducible, aperiodic, mixing, or component-mean homogeneous.

For a finite-state Markov candidate, irreducibility is the key law-of-large-
numbers property. Aperiodicity is needed for ordinary distributional mixing,
not for time-average convergence: a single deterministic finite cycle is
periodic but uniquely ergodic on its component.

For spatially extended local rules the gap is larger. Local interactions can
support multiple permanent phases or invariant sectors. A theorem about the
selected exact law must establish the relevant irreducibility, component
means, or unique ergodicity; the adjective local cannot substitute for it.

## 7. Trial Corpus: Definition Versus Physics

The jobs divide as follows.

| item | placement |
|---|---|
| `R/O/K` block grammar | operational definition once record roles and ancestry are fixed |
| trial index and denominator | definition by certified block count |
| outcome decoder | operational effect/record-role definition; completeness tested by future protocols |
| finite count and empirical frequency | exact function of actual records |
| equality of preparation procedures | operational equivalence definition using complete future statistics |
| certificate formation and legal ancestry | exact law theorem |
| reset target and archive decoupling | exact law theorem |
| indefinite recurrence/fairness of blocks | exact law or boundary theorem |
| consistent finite/infinite block law | exact law/process content if not already included in `W` |
| `W` one-block marginal equals stationary block mean | preparation/process-link theorem |
| stationarity | exact law theorem or selected invariant boundary/state |
| `CM(q)`, ergodicity, mixing, or unique ergodicity | exact law/component theorem |
| actual component or orbit | realized state/boundary unless uniquely derived |

Calling a corpus “trials” is harmless as a definition of blocks. Calling them
“repetitions of the same preparation” is a scientific claim unless complete
operational equivalence has been proved. Calling them “IID trials” is stronger
again.

## 8. Collapsed Minimum Law Condition

The raw list compresses into two statistical clauses and one actuality seam:

```text
C = certified-corpus process:
    the exact W-law supplies a projectively consistent stationary block
    process, recurrent delimiters, a fixed record decoder, and the one-block
    identity E[X_0]=q;

M = component mean:
    E[X_0 | I_T]=q almost surely;

A = actual-member/pointwise interface:
    needed only when the claim is that this realized stochastic infinite
    history, rather than mu-almost every history, has the limit q.
```

`T=C+M` is the true minimum frequency condition. It contains no second set of
probability weights: `q` comes from `W`, and Birkhoff is mathematical. `C` and
`M` are properties or extensions of the exact law.

Alternative discharge routes are:

```text
strong predictive reset -> IID -> C+M;
finite irreducible stationary Markov -> ergodic -> C+M;
mixing -> ergodic -> C+M;
stationary ergodic process -> C+M;
stationary nonergodic + equal component means -> C+M;
deterministic unique ergodicity + continuous decoder -> C+M and pointwise A
                                                       for the frequency claim.
```

This prevents two opposite mistakes: overpricing the seam as IID, and hiding
the seam inside the word stationarity.

## 9. Actual-Member Boundary

Birkhoff's theorem is almost sure. It does not say every member of a
stochastic path space has the stated limit.

Under IID Bernoulli `q=1/3`, the all-one infinite sequence has empirical
frequency `1`, while its length-`N` prefix has probability `(1/3)^N` and the
singleton infinite history has measure zero. The theorem correctly excludes
it only probabilistically.

The approved realized-state primitive supplies a pointwise reference to the
law-admissible realized state. It explicitly supplies no measure, typicality,
genericity, or probability rule. Therefore a measure-one theorem must not be
silently converted into a logical pointwise theorem about that primitive.

There are four honest placements:

1. retain the ordinary almost-sure empirical prediction as the statistical
   claim;
2. add a separately tested law-to-sample semantics saying the realized
   history is governed by `mu`;
3. prove the actual boundary/orbit is generic for the declared observable; or
4. use a deterministic uniform/unique-ergodic theorem that covers every
   allowed orbit.

The fourth route is why actual-member semantics remains separate rather than
being declared a universal new-law atom. Deterministic unique ergodicity gives
pointwise frequencies, but it still does not tell us which finite record is
actual at a given block unless the orbit/boundary is fixed.

Finite empirical frequencies need no typicality premise. They are read
directly from the actual finite corpus and compared with the law's predicted
finite or asymptotic behavior.

## 10. Consequence for Axiom and Exact-Law Language

This cycle gives no reason to add “IID,” “stationary,” “ergodic,” “typical,”
“reset,” or “close” to the Record axiom.

- Reset and close are operational roles whose truth is proved by an exact
  transition law.
- Stationarity and component means are properties of the law plus its
  boundary/domain.
- The probability number `q` is already the output of Cycle 20's effect law.
- The frequency representation is a mathematical ergodic theorem.

If the final exact law is global and complete, the clean target is:

> Prove that its record-certified block shift satisfies `CM(q)` for every
> physical effect outcome, with `q` the law's operational trace weight.

If that theorem lands, the trial/frequency import retires. No further
probability axiom is needed.

If the final law has strong predictive reset, the proof is IID and easy. If it
has finite memory, irreducible Markov or mixing machinery may suffice. If it is
deterministic, unique ergodicity or a direct discrepancy theorem may be
stronger because it closes the pointwise realized-history seam.

No axiom text is proposed. The law dossier should expose certificate ancestry,
corpus recurrence, preparation link, invariant components, and decoder rather
than putting statistical adjectives into constitutional prose.

## 11. Primary-Source Boundary

The external comparison uses primary sources. They are mathematical authority,
not framework authority.

| Primary source | Use here | Boundary |
|---|---|---|
| [Birkhoff, *Proof of the Ergodic Theorem*](https://doi.org/10.1073/pnas.17.12.656) | Stationary time averages converge to the invariant-component conditional expectation; ergodicity makes the limit the ensemble mean. | It consumes a measure-preserving process and yields an almost-sure, not every-member, theorem. |
| [de Finetti, *La prévision : ses lois logiques, ses sources subjectives*](https://www.numdam.org/item/AIHP_1937__7_1_1_0/) | Exchangeable Bernoulli laws are mixtures directed by a latent parameter; empirical frequency tracks that parameter rather than merely its mean. | Exchangeability does not force the directing measure to be a point mass. |
| [Hewitt and Savage, *Symmetric Measures on Cartesian Products*](https://doi.org/10.1090/S0002-9947-1955-0076206-8) | General primary-source extension of the exchangeable-mixture structure. | Symmetry under trial permutations is weaker than ergodicity or IID. |
| [Oxtoby, *Ergodic sets*](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-58/issue-2/Ergodic-sets/bams/1183516689.full) | Unique ergodicity on a compact dynamical system gives uniform time-average convergence for continuous observables. | The physical component and decoder must already be fixed; indicator functions need the relevant continuity/clopen condition. |
| [Pollock et al., *Non-Markovian quantum processes: complete framework and efficient characterisation*](https://arxiv.org/abs/1512.00589) | A multi-time process is an operational object only relative to a complete control family; correlations are part of the process, not one-time marginals. | Process reconstruction presupposes normalized statistics and does not prove reset. |
| [Pollock et al., *Operational Markov condition for quantum processes*](https://arxiv.org/abs/1801.09811) | Complete interventions are needed to distinguish genuine Markov/reset behavior from hidden memory. | A visible reset label or equal marginals is not the operational Markov condition. |

The finite Markov, cycle, exchangeable, and permanent-sector calculations are
recomputed exactly in the companion runner. No external numerical result is
used.

## 12. No-Go Discipline Gate

**No-Go Discipline gate status: PASS** for three narrow finite
non-entailments:

1. identical visible reset/close skeletons do not imply strong predictive
   reset;
2. stationarity plus finite causal locality does not imply `CM(q)` or
   ergodicity; and
3. an almost-sure frequency theorem is not an every-member pointwise theorem.

No claim is made that the final exact law cannot prove reset, mixing,
component-mean equality, unique ergodicity, or pointwise convergence.

### N1 — Alternative-route enumeration

| route | marker | exact outcome |
|---|---|---|
| visible `R/O/K` delimiter grammar | `ATTEMPTED` | succeeds in defining blocks, counts, and finite frequencies; all unequal process laws share it |
| Cycle-14-style certificate ancestry | `ATTEMPTED` | can prove that a named reset map ran; the target and archive decoupling remain law clauses |
| Cycle-16-style causal close | `ATTEMPTED` | proves finite-port completion but not predictive reset or sector erasure |
| strong predictive reset | `ATTEMPTED` | succeeds: the conditional equation and chain rule give IID |
| stationarity alone | `ATTEMPTED` | frozen and permanent-sector controls have marginal `1/3` with sector-valued limits |
| finite causal locality | `ATTEMPTED` | every positive and negative control is finite-state causal-local |
| finite irreducible Markov route | `ATTEMPTED` | succeeds without reset: the exact positive kernel is mixing and has frequency `1/3` |
| stationary ergodic/Birkhoff route | `ATTEMPTED` | succeeds and is strictly weaker than IID/mixing |
| observable component-mean route | `ATTEMPTED` | succeeds even for the nonergodic equal-mean mixture; it is the weakest stationary route tested |
| exchangeability/de Finetti route | `ATTEMPTED` | fails without a degenerate directing parameter; frozen mixture tends to `0` or `1` |
| deterministic unique-ergodic route | `ATTEMPTED` | succeeds pointwise for every phase of the `001` cycle |
| permanent-sector conditioning | `ATTEMPTED` | succeeds only after `W` is conditioned on the actual sector; the unconditioned mean need not be its frequency |

There are more than five distinct operational, probabilistic, Markov,
exchangeable, deterministic, and sector routes. Several close the target under
explicit conditions, so the conclusion is narrowed to the displayed finite
non-entailments.

### N2 — Wall-independence audit

After definitions and mathematical theorems are removed from the raw list,
the conditional set is `C,M,A`:

```text
C = W-linked stationary certified-corpus process;
M = component-mean equality for the declared outcome;
A = pointwise actual-member bridge when more than an almost-sure claim is made.
```

| pair | first closes second? / second closes first? | exact witness |
|---|---|---|
| `C-M` | no / no | frozen and permanent-sector laws satisfy `C` without `M`; an abstract component-mean table does not generate recurring certificates or a process law |
| `C-A` | no / no | one stationary measure admits many actual members; one actual finite/infinite word does not specify the stationary joint law |
| `M-A` | no / no | equal component means remain an almost-sure measure statement; one selected history does not prove every invariant component has mean `q` |

For the statistical theorem, `T=C+M` is the single minimum condition. `A` is
outside it unless a pointwise realized-history claim is requested. A global
exact `W` may own and derive `C+M`, collapsing every additional law field.

### N3 — Hidden-wall scan

The prescribed phrases and close variants were searched in the proof.

| phrase | classification |
|---|---|
| “we assume” | appears only in this checklist description; theorem inputs are named `C` and `M` |
| “by construction” | not used as a physics shortcut; displayed finite processes are labelled exact controls |
| “as is standard” | absent from load-bearing steps; Birkhoff, de Finetti/Hewitt--Savage, and Oxtoby are cited |
| “the framework provides” | absent; live Record and registered primitives are quoted only at their declared scope |
| “bridge context” | absent; preparation-to-stationary-marginal identity is explicit inside `C` |
| “background” | no background measure is imported; selected invariant state/boundary is explicit |
| “naturally” | absent from proof steps |
| “obviously” | absent from proof steps |
| “standard QFT” | irrelevant and absent from proof steps |
| “registered” | authority/primitive scope only; no registered trial law is claimed |
| “canonical” | no canonical corpus or stationary measure is silently selected |
| “reset” | split into visible role, preparation ancestry, and strong predictive reset |
| “stationary” | explicit shift invariance of the joint block measure |
| “causal local” | finite dependence state only; no irreducibility is inferred |
| “almost surely” | explicit measure-one result, not a pointwise realized-state theorem |

No hidden condition changes the collapsed `C,M,A` count.

### N4 — Exact residual matching

| cited witness | witness residual | present use | match? |
|---|---|---|---:|
| `MINIMAL_AXIOMS_2026-06-29.md`, Record/non-supply sections | permanent readable records and finite scalar additivity; no probability, process, or rate law | block records versus joint process law | yes |
| `OPERATIONAL_QUOTIENT_BORN_AFFINITY_CYCLE20_NOTE_2026-07-14.md`, Sections 8--10 | one-shot trace weight, reset corpus, frequency, and actual member separated | starting `W/T/A` seam | yes, authority-free predecessor |
| `SELF_WRITING_APPEND_ONLY_BELL_FRONT_CYCLE14_NOTE_2026-07-14.md`, preparation/certificate sections | certificate appended after supplied reset; archive/target law-owned | reset ancestry versus label | yes, authority-free predecessor |
| `DELAYED_LOCKING_CAUSAL_CLOSE_CYCLE16_NOTE_2026-07-14.md`, local-close sections | close certifies finite named ports, not global absence | close versus memory erasure | yes, authority-free predecessor |
| `RECORD_IID_TYPICALITY_FIREWALL_2026-06-06.md`, exact counterfamily | same one-step marginal, different IID/locked count laws | one-shot versus joint law | yes; finite pair recomputed |
| `RECORD_OCCURRENCE_THINNED_IID_FREQUENCY_BRIDGE_2026-07-01.md`, finite theorem | supplied IID reset and kernel give frequency algebra | strong-reset positive route | yes |
| `DETERMINISTIC_UNIQUE_EXTENSION_RECORD_SECTOR_NOTE_2026-07-14.md`, unique-ergodic section | selected component/decoder can derive frequencies; permanent sectors split measures | deterministic and sector controls | yes, authority-free predecessor |
| `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`, primitive/guardrails | pointwise reference, no measure or typicality | actual-member boundary | yes |

Authority-free predecessors are not treated as retained proof. The companion
runner independently recomputes every finite process distinction used in the
claim.

### N5 — Resolution and rhetoric audit

Tested resolutions are:

- per certificate record and per three-record block;
- per finite transcript and finite empirical count;
- per one-step marginal;
- per finite joint word through explicit horizons;
- per lag covariance in the two-state Markov law;
- per invariant component mean;
- per deterministic orbit phase; and
- per stationary path measure.

Birkhoff supplies the infinite almost-sure theorem externally. Oxtoby supplies
the compact continuous all-orbit theorem. The finite runner does not claim to
prove either general theorem. “Stationarity plus locality does not imply
frequency `q`” is licensed only by exact finite-state stationary process
families with unequal invariant-component means. It is not a statement about
all local quantum field theories, every lattice limit, or every observable.

“Actual-member semantics remains separate” means separate from a generic
measure-one theorem. The deterministic cycle explicitly shows that a
pointwise law can retire that seam.

### N6 — Partial-closure paths and primitive registry

The current primitive registry and all three primitive source notes were read.
The realized-state primitive supplies one pointwise law-admissible reference,
but no state, measure, weighting, probability, typicality, genericity, or
boundary. Scale reference and kinetic isotropy are irrelevant to the
frequency theorem.

Live non-axiom retirement paths are:

1. define trial blocks, decoder, counts, and finite frequency operationally;
2. prove a Cycle-14-style certificate has complete predictive-reset ancestry,
   yielding IID;
3. prove an irreducible Markov or mixing theorem for the certified block
   process;
4. prove stationary ergodicity and apply Birkhoff;
5. prove the weaker observable-specific component-mean equality;
6. condition `W` on every visible permanent sector and prove their means agree;
7. prove deterministic unique ergodicity or a direct discrepancy bound for
   every allowed orbit; and
8. define `W` globally on the consistent multi-time process so `C+M` are
   theorem obligations rather than another law object.

None is misclassified as “requires new axiom.” No proposed primitive is given
premise weight.

### N7 — Steelman

**Hostile steelman:** Cycle 20 may already have closed this seam in everything
but notation. Its `W` was described as an exact normalized law for every
physically legal finite adaptive record protocol. If that family is
projectively consistent and includes arbitrary repetitions of the visible
reset/close protocol, then all joint trial distributions are already values
of `W`; no new corpus law exists. Complete operational reset can be tested
inside `W`, and if it fails, Birkhoff's theorem needs only a property of the
same path law—component-mean equality—not new probability content. A final
deterministic uniquely ergodic `W` could even prove the limit on every orbit
and avoid typicality. Nothing in the paired controls excludes this integrated
closure. They show only that certificate shape, stationarity, and locality do
not prove the needed property without inspecting the exact `W`.

This steelman succeeds. The cycle therefore classifies `C+M` as a theorem
contract on a global `W` whenever possible, not as a demand for a separate
axiom or probability law.

### N8 — Cross-cycle echo

On 2026-07-14 the prescribed repository-equivalent `rg` searches were run for

```text
structurally undecidable | no retained primitive | requires new axiom |
cannot be derived from A_min
```

under `docs/`, followed by a walk of `.claude/science/physics-loops/**/
NO_GO_LEDGER.md`. No ledger entry named this exact certificate-to-component-
mean seam. Similar prior walls were nevertheless retired by mechanisms used
here:

- post-record counts became exact empirical definitions rather than a
  probability source;
- `PREP-FRAME` retired when preparation became its operational class;
- an IID import became a conditional finite-frequency theorem;
- deterministic unique ergodicity turned a supplied measure target into an
  orbit theorem inside one component; and
- actual boundary instances moved to realized-state/boundary data rather than
  generic constitutional prose.

The closest current echoes are the Cycle-20 operational probability note, the
IID firewall, the thinned-IID theorem, and the deterministic record-sector
probe. This cycle applies their retirement logic rather than recounting IID,
ergodicity, reset, and actual member as four new walls.

No `NO_GO_LEDGER.md` is edited because this note has no audit or retained
authority.

## Verification

Run:

```bash
python3 scripts/certified_record_corpus_ergodic_frequency_cycle21_2026_07_14.py
```

Expected result:

```text
PASS=207 FAIL=0
```

The runner verifies authority/source boundaries, exact certificate parsing,
predictive-reset versus label identity, projective stationarity, common
one-shot marginals, IID moments, Markov eigenvalue/covariance decay,
exchangeability and frozen variance, deterministic cycle uniqueness and
pointwise discrepancy, equal-component-mean nonergodicity, permanent-sector
limit variance, the actual-member separator, and the N1--N8 scope contract. It
applies no status mutation.

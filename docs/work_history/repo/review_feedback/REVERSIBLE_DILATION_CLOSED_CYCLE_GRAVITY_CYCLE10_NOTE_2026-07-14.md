# Reversible Dilation and Closed-Cycle Gravity — Cycle 10

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exercise packet of exact finite and symbolic
probes. It is not an axiom proposal, framework premise, audit verdict,
retained theorem, empirical gravity result, or claim that the universe is a
computer. It changes no axiom, primitive, premise registry, review queue, or
audit surface.

Companion runner:

```text
scripts/reversible_dilation_closed_cycle_gravity_cycle10_2026_07_14.py
```

Every dynamics below is a **conditional probe law**. The supplied framework
remains only the four axioms and three approved primitives listed in the live
premise registry.

## Framework Refresher Read

Before this cycle, the current versions of the following surfaces were read:

- `docs/MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit, Admissibility, and
  Record, including the explicit statement that Admissibility is not dynamics
  and that formation rule, weighting, rate, time metric, and persistence
  dynamics remain outside the axioms;
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` and
  `docs/audit/data/axiom_premise_nodes.json`;
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`,
  `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, and
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`;
- the current `origin/main` `review-loop/SKILL.md`, including its axiom versus
  approved-primitive distinction, Record guardrails, no-go discipline, and
  review/audit authority split; and
- `docs/repo/CONTROLLED_VOCABULARY.md`.

The exercise skill itself was freshness-checked against `origin/main`; the
worktree was deliberately not moved because it contains shared user work.

Those surfaces supply no stochastic clock, Hamiltonian, update channel,
source, resource carrier, scheduler coupling, probability rule, or metric
tensor. None is silently added here.

## Result Up Front

Cycle 9's scalar resource-gravity construction survives one deep attack and
fails another in a useful way.

First, its exact lazy nearest-neighbor diffusion step

```text
P = I - L/12
```

does have a small translation- and proper-cubic-covariant unitary dilation.
Use seven direction labels, one for `0` and six for `+/- x,+/- y,+/- z`, in a
three-qubit `M8` coin. Prepare the invariant coin state with probabilities

```text
p(0)=1/2,                 p(+/- e_i)=1/12,
```

apply the controlled nearest-neighbor shift, and trace the coin. The diagonal
position state evolves by exactly Cycle 9's `P`. A local symmetric edge
averaging step likewise has an exact one-ancilla-qubit Fredkin dilation. Thus
there is no one-step incompatibility between the Markov law and finite local
unitarity.

Second, that is not an autonomous all-time completion. Reuse the same coin and
the direction remains coherently correlated across steps. The mean-square
radius grows as `t^2/2`, not `t/2`; on a finite torus the joint unitary recurs.
Fresh independent coins reproduce the Markov powers, but the simple exact
implementation then uses a fresh seven-way path slot per tick. More generally:

> A fixed finite environment, initialized once and evolved by one fixed finite
> unitary, cannot reproduce every power of a genuinely mixing finite Markov
> channel for all integer times.

The proof is short: every reduced expectation under a finite fixed unitary is
a finite trigonometric polynomial in time. If such a sequence has a limit, it
is constant. A primitive Markov channel has nonconstant decaying modes that
converge. The two behaviors cannot be identical for all times. This boundary
does **not** cover an infinite lattice environment, an ever-growing local
ancilla tape, a time-dependent unitary, or an autonomous reversible QCA that
exports which-path information to infinity.

Third, Cycle 9's ideal birth/death reservoirs can be replaced by a closed local
token-number cycle. Give each token two internal layers: outward debt `D` and
return credit `C`. Both diffuse locally. At endpoint `a`, convert `C -> D`; at
endpoint `b`, convert `D -> C`, with reverse conversions allowed. The total
token is exactly conserved, and the stationary debt layer obeys

```text
kappa L d = j (delta_a-delta_b).
```

So the same Green response occurs without deleting tokens at a boundary. But
the nonzero current is present exactly when the conversion cycle has nonzero
affinity

```text
A = log[(f_a f_b)/(r_a r_b)].
```

At detailed balance, `A=0`, the current and nonconstant Green amplitude vanish.
The boundary reservoir has therefore been replaced, not derived away: the new
cost is a supplied time-oriented nonequilibrium conversion bias. The finite
law is a closed Markov process, not a reversible/unitary microscopic closure.

Fourth, a positive stationary **formation** current cannot run forever in a
finite permanent one-record-per-site archive. It saturates after at most `N`
new records on `N` sites. A reread current can recur without archive growth,
but that is a different source law. An infinite archive front can evade finite
saturation, but needs unbounded carrier volume and local information transport.

Finally, Cycle 9's common scalar scheduler does prove universal local clock-gap
rescaling inside that clause, but does not fix transport or gravity. Two local
Hamiltonians can have identical onsite clock blocks and different edge
couplings. In the standard weak-metric comparator

```text
ds^2 = -(1+2 Phi) dt^2 + (1-2 gamma_PPN Phi) d x^2,
```

the same Newtonian lapse gives light deflection

```text
alpha = 2(1+gamma_PPN) GM/b.
```

Pure lapse (`gamma_PPN=0`) gives `2GM/b`; the GR value
(`gamma_PPN=1`) gives `4GM/b`. Clock redshift and leading Newtonian attraction
therefore do not determine spatial curvature or lensing.

The bare-metal implication is narrow but important: “the clock locks it” is
not yet a mechanism. A scalar clock can label or rescale an update, but it
cannot by itself select an outcome. There are two honest foundations. The
commit may be a genuinely irreversible primitive law, in which case that new
physics should be said directly. Or the underlying law may remain reversible,
in which case a reader that locks must correlate the outcome with a fresh
distinguishable carrier or export the unused branch information into an
unbounded environment. If those degrees are not records, the state description
is wider than records; if they are permanent records, finite storage saturates.
That is the real fork the final axiom language must not hide.

## Exercise Zero — The Precise Wall

The target is not “derive GR from a computer metaphor.” It is smaller:

1. retain Cycle 9's local conservative origin for a Poisson/Green field;
2. determine whether its dissipative update and maintained current can arise
   from finite local reversible `M2` blocks without an external stochastic
   clock, reset operation, or unrecorded environment;
3. keep permanent record identity, working resource, and a probe coexistent;
4. identify which gravity claims follow from a scalar scheduler and which need
   independent tensor/spatial dynamics.

Progress means an explicit dilation or a sharply scoped obstruction with a
countermodel. Decisive closure would be one autonomous translation- and
proper-cubic-covariant local law on the existing one-qubit lattice that
produces records, exact Markov relaxation, sustained current, universal matter
coupling, and the tensor weak-field limit without hidden fresh capacity.
Nothing in this cycle achieves that full closure.

## Exercise One — Assumptions From Axioms Up

| ID | Layer | Assumption | Explicit/implicit | Why needed | What if wrong / failure opened | First test | Confidence |
|---|---|---|---|---|---|---|---|
| F1 | framework | Four axioms exactly as currently written | explicit supplied premise | ontology and covariance baseline | a future axiom rewrite changes the target surface | live-text needles | high |
| F2 | framework primitive | scale reference is units only | explicit supplied primitive | prevents importing gravity strength from `M_Pl` | dimensionless coupling remains open | registry/source-note check | high |
| F3 | framework primitive | `c_t=c_s` is kinetic-form isotropy only | explicit supplied primitive | prevents importing scheduler dynamics | time law remains open | registry/source-note check | high |
| F4 | framework primitive | realized-state access is pointwise only | explicit supplied primitive | prevents a state or probability selector from entering | weights and initial state remain open | registry/source-note check | high |
| D0 | foundational fork | microscopic record formation is reversible | optional route hypothesis, not supplied | motivates a dilation rather than a primitive commit map | if false, irreversibility itself is the new axiom-grade law | compare primitive commit and dilation routes | open |
| D1 | probe definition | Cycle 9 lazy channel is `P=I-L/12` | explicit conditional law | object to dilate | another local diffusion kernel may have a different carrier cost | exact matrix identity | high |
| D2 | representation | a seven-label coin is embedded in three qubits | explicit conditional construction | finite Stinespring carrier | embedding leaves one unused basis label and does not prove a lattice block code | dimension count | high |
| D3 | representation | tracing a coin is an allowed reduced description | implicit physical bridge | creates the mixed Markov step | without discard, the joint state remains coherent | reused-coin countermodel | high |
| D4 | dynamics | fresh coin state is available each independent step | implicit in Markov iteration | obtains `P^t` exactly | finite reused environment recurs instead of mixing | two-step and variance probe | high |
| C1 | closed current | tokens have `D/C` internal layers | explicit conditional law | closes source/export bookkeeping locally | one layer requires an external sink | full generator | high |
| C2 | closed current | endpoint conversion rates have nonzero cycle affinity | explicit law value | sustains nonzero current | detailed balance kills the Green amplitude | affinity ablation | high |
| C3 | clock | continuous-time Markov generator supplies event ordering | implicit imported dynamics | defines rates and stationarity | reversible microscopic time needs a dilation/fuel account | finite-unitary boundary | high |
| R1 | record | every source event forms a new permanent record | optional source identification | connects current to formation | finite archive saturates; rereading is a distinct route | capacity counter | high |
| R2 | carrier | blank, record-0, record-1 are orthogonal states if records are unitary carrier data | conditional representation choice | reversible coexistence count | if record status is external ontology, the Hilbert budget changes but unitary completion is not supplied | dimension lower bound | medium |
| G1 | gravity | debt field reduces one common scheduler | explicit conditional law | attractive scalar lapse and local universality | species-dependent coefficients break equivalence | paired couplings | high |
| G2 | gravity | local gap scaling controls spatial propagation | implicit and challenged | needed to move from clocks to trajectories | same clocks permit different transport | paired Hamiltonians | high |
| G3 | gravity | scalar lapse fixes lensing | implicit and refuted by comparator | needed for GR claim | spatial curvature remains an independent dial | `gamma_PPN` factor-two test | high |
| B1 | boundary | finite torus with antipodal source/sink | explicit runner fixture | exact covariance and solve | infinite-volume construction may evade recurrence and saturation | grow-volume family | high |
| B2 | physical bridge | mass sets conversion/formation current | still absent | required to call source “matter” | field amplitude remains uncalibrated | paired mass states | low/open |

The most likely hidden assumptions are D3/D4: “trace it out” and “prepare a
fresh coin” are often treated as harmless bookkeeping, but together they are
the irreversibility and storage supply. The most expensive assumptions are G2
and B2 because they stand between a scalar resource field and actual gravity.

## One-Step Cubic Unitary Dilation

Let the coin basis be labelled by

```text
D = {0, +e_x, -e_x, +e_y, -e_y, +e_z, -e_z}.
```

Prepare

```text
|c> = sqrt(1/2)|0> + (1/sqrt(12)) sum_{d != 0} |d>.
```

Define the controlled shift

```text
U |x,d> = |x+d,d>.
```

This is a range-one permutation unitary. Lattice translations commute with it.
A proper cubic rotation acts simultaneously as `x -> Rx` and `d -> Rd`, so it
also commutes with the joint action. The coin state is invariant because the
six nonzero directions have equal amplitudes.

Tracing the coin after one step gives

```text
E(rho) = (1/2) rho
       + (1/12) sum_{d != 0} T_d rho T_d^dagger.
```

For diagonal position states this is exactly

```text
P = I-L/12.
```

A localized input has reduced purity

```text
(1/2)^2 + 6(1/12)^2 = 7/24,
```

so the mixedness is precisely information retained in the direction coin.
The runner checks the joint permutation, range, every proper cubic rotation,
translation covariance, weights, purity, and `I-P=L/12`.

### Local edge exclusion step

For two resource qubits, let `S` be SWAP. The channel

```text
E_edge(rho) = (rho + S rho S)/2
```

has a one-qubit dilation: initialize an ancilla in `|+>`, apply controlled
SWAP, and trace the ancilla. The Fredkin unitary commutes with total edge
occupation. This closes one local random edge choice, not the full continuous
SSEP semigroup. Selecting overlapping edges at rates still needs a schedule,
Poisson clocks, a partitioned circuit, or an autonomous environment carrying
that schedule.

## Finite-Environment Repeated-Mixing Boundary

Consider finite Hilbert spaces `H_S,H_E`, one fixed environment state `sigma`,
and one fixed unitary `U` on `H_S tensor H_E`. For a system state `rho` and
observable `A`,

```text
f(t) = Tr[(A tensor I) U^t (rho tensor sigma) U^(-t)]
```

is a finite sum of terms `c_jk exp[i(theta_j-theta_k)t]`. Suppose `f(t)` has a
limit. Taking time-averages of `|f(t+1)-f(t)|^2` eliminates unequal
frequencies and leaves a sum of nonnegative coefficients. A zero limiting
difference forces every nonzero-frequency coefficient to vanish. Therefore
`f(t)` is constant.

The finite Markov matrix `P=I-L/12` on a connected torus has one constant
mode and nonzero modes with `|lambda|<1`. Perturb the full-rank stationary
state slightly along one real decaying mode and choose an observable that
detects it. Its Markov expectation is nonconstant and converges. It therefore
cannot equal the finite-unitary `f(t)` for every `t`.

This proves only:

```text
fixed finite S+E + fixed U + one initial sigma
    cannot exactly realize every P^t for all t.
```

It does not prove that diffusion is incompatible with quantum mechanics or
that an infinite reversible local substrate cannot look Markovian in a finite
window.

The concrete runner shows the same issue without asymptotics. Reusing the
direction coin gives one fixed direction for all steps,

```text
E[r^2]_reuse = t^2/2,
```

whereas independent direction labels give

```text
E[r^2]_fresh = t/2.
```

The former is ballistic and recurrent; the latter is diffusive. A simple
fresh path-tape implementation has `7^T` orthogonal histories after `T` ticks.
That is a sufficient implementation cost, not a proof that `7^T` is the
minimal finite-horizon Stinespring dimension after histories with the same net
displacement are compressed.

Primary literature is used only as proof-pattern and scope support:

| Source | What it contributes | Repo translation | Import risk |
|---|---|---|---|
| Frederik vom Ende and Gunther Dirr, [Unitary Dilations of Discrete-Time Quantum-Dynamical Semigroups](https://arxiv.org/abs/1804.00918) | constructs unitary dilations of channel semigroups; auxiliary space is generally not finite, with partially finite room for cyclic channels | motivates checking all-time rather than one-step dilation; the finite obstruction above is proved directly | no theorem is imported as framework authority |
| Todd Brun, Hilary Carteret, and Andris Ambainis, [The quantum to classical transition for random walks](https://arxiv.org/abs/quant-ph/0208195) | multi-coin walk retains quadratic variance except in the new-coin-per-step limit; decoherence yields linear variance | the runner reproduces the ballistic/fresh-coin split for the cubic Cycle 9 weights | model differs; qualitative precedent only |
| Peter Love and Bruce Boghosian, [From Dirac to Diffusion: Decoherence in Quantum Lattice Gases](https://arxiv.org/abs/quant-ph/0507022) | obtains quantum/classical walk limits through a particle-bath interaction | makes the bath/reset content explicit rather than calling diffusion bare unitarity | bath state and coupling are external to current axioms |

## Closed Internal Return Cycle

Let `d_x` and `c_x` be probabilities for the outward debt and return credit
layers of one conserved token. Both diffuse with rate `kappa`. At source `a`,

```text
C_a --f_a--> D_a,        D_a --r_a--> C_a,
```

and at return endpoint `b`,

```text
D_b --f_b--> C_b,        C_b --r_b--> D_b.
```

Every transition is local and total token probability is conserved. At a
stationary state,

```text
j = f_a c_a-r_a d_a = f_b d_b-r_b c_b,
kappa L d =  j(delta_a-delta_b),
kappa L c = -j(delta_a-delta_b),
d+c = constant.
```

The side-four exact fixture uses antipodal endpoints, which are fixed under all
24 proper cubic rotations. The runner verifies covariance, generator column
sums, positivity, stationarity, equal endpoint current, both Poisson equations,
and the exact mean-zero Green fit.

The cycle affinity is

```text
calA = log[(f_a f_b)/(r_a r_b)].
```

With `f_a=f_b=1` and `r_a=r_b=1/3`, both `calA` and `j` are positive. With all
four rates equal, detailed balance holds, `j=0`, and the nonconstant Green
profile disappears. Reversing the four forward/reverse rates reverses `j`.

This construction removes an **ideal token sink**, not the arrow. The arrow is
now the supplied affinity. A finite reversible dilation of that stationary
Markov current needs the same fresh-information/fuel account as repeated
mixing. A coherent finite unitary may sustain a persistent current, but it
does not thereby converge to the unique diffusive Green state.

## Archive, Resource, Probe, and Coin Coexistence

If blank status and the two possible locked qubit contents must all be encoded
as mutually orthogonal Hilbert states, archive status needs at least three
labels and hence two `M2` factors. Add one resource qubit and one probe qubit:

```text
archive status + resource + probe = 2+1+1 = 4 qubits = M16.
```

The seven-label direction coin needs three more qubits, so one-step coexistence
has enough dimension in

```text
7 qubits = M128.
```

This is a room count only. It does not prove that seven fundamental sites can
be grouped into a non-overlapping finite block without choosing an origin or
breaking unit-translation covariance. Nor does it prove that Record's blank
versus present status must be Hilbert encoded; if record status is an external
ontic label, this dimension lower bound does not apply, but then the proposed
unitary completion is no longer a complete state description.

### Permanent-archive saturation

On `N` finite sites with at most one permanent record each, a one-to-one map

```text
successful source event -> newly formed record
```

can fire at most `N` times. Any positive stationary formation rate reaches
capacity in finite time no later than `N/j`. The resource token may circulate
forever, but the archive cannot keep accepting new records.

There are three honest evasions, each changing the physical claim:

1. source events reread existing records rather than form new ones;
2. records move outward to fresh sites on an infinite lattice while their old
   content remains represented; or
3. many events are compressed into one record, abandoning event identity.

Only the first is finite, but it makes active gravity a read/processing current,
not a record-formation current. The second is the strongest bare-metal route
left open. The third needs a theorem saying which information can be erased or
identified without violating permanence.

## Paired Scheduler Countermodels

Cycle 9 used

```text
K_s(x) = q(x) K_s^0.
```

Inside this clause every local energy gap of every species scales by the same
`q`. Adding `h_s(x) I` changes no gap, so species-dependent identity terms are
gauge-like for local clocks. But two small changes destroy universality:

```text
K_s(x) = [1-gamma_s phi(x)] K_s^0,
K_s(x) = q(x)^(p_s) K_s^0.
```

Different `gamma_s` or `p_s` gives different fractional clock shifts while
leaving the resource field unchanged. Those parameters are not supplied by
the diffusion law.

Even common onsite clock scaling does not fix motion. The runner builds two
position-plus-internal Hamiltonians with the same onsite blocks

```text
diag(q_x) tensor K_internal
```

but different symmetric edge amplitudes: constant edges versus
`sqrt(q_x q_y)`-weighted edges. Their local clocks agree exactly; their
transport spectra and neighbor transfer amplitudes differ.

The weak-metric lensing comparator exposes the same missing sector. For
`Phi=-GM/r`, the transverse integral is exactly

```text
integral b dz/(b^2+z^2)^(3/2) = 2/b.
```

The temporal potential contributes one copy and spatial curvature contributes
`gamma_PPN` copies, giving `2(1+gamma_PPN)GM/b`. A scalar scheduler can fix the
temporal copy while leaving `gamma_PPN` undetermined. This is why Cycle 9's
attractive sign and universal local lapse remain scalar gravity support, not a
tensor/lensing closure.

## Exercise Four — Mathematics-Sector Search

| Sector | Concrete reframe/tool | Small object | What it tests next |
|---|---|---|---|
| finite groups/representation theory | treat the seven direction labels as the invariant rest label plus the six-direction permutation representation of the proper cubic group | `C^7` coin and 24 signed permutation matrices | classify all invariant coin amplitudes and whether a smaller covariant Kraus carrier exists |
| operator algebras | Stinespring dilation and finite almost-periodic dynamics | one finite channel `P` and fixed `U` | minimum finite-horizon environment rank; all-time finite obstruction |
| category/universal properties | identify “discard” as the noninvertible morphism in unitary-plus-trace factorization | controlled shift followed by partial trace | whether Record supplies a native discard/commit map or only readable fixed output |
| topology/cohomology | current as a cycle and affinity as its circulation | two-layer graph with one fundamental `D/C` loop | whether a local exact cocycle can derive the orientation rather than supply it |
| spectral graph theory | Green response as inverse on the zero-sum Laplacian sector | cubic torus `L` | finite/infinite convergence and source multipoles |
| convexity/optimization | covariant Kraus-rank minimization as semidefinite/intertwiner constraints | seven shift Kraus operators | search for a smaller `M2` block or certify the conditional carrier lower bound |
| probability/information | detailed balance versus stationary entropy-producing current | four endpoint rates | quantify the fuel/information rate required by `calA != 0` |
| dynamical systems/ergodic theory | mixing eigenmodes versus finite-unitary almost periodicity | `P^t` against `U^t` | sharpen local finite-window approximation bounds |
| PDE/functional analysis | diffusion-to-Poisson stationary reduction | `kappa L d=j(delta_a-delta_b)` | continuum tensor completion and nonlinear backreaction |
| number theory/lattices | exact torus recurrences of permutation shifts | side-`m` controlled translation | recurrence periods and finite-volume false stationarity |
| logic/model theory | paired-law independence | common versus species clocks; pure lapse versus spatial curvature | identify which proposed axiom sentence is genuinely underdetermined |

The best immediate mathematical route is not a larger gravity simulation. It
is a covariant finite-horizon Stinespring-rank search followed by an infinite
QCA construction attempt. That directly tests whether fresh information can be
routed through existing lattice sites rather than introduced as a hidden tape.

## Exercise Five — Reframes

| Reframe | What moves | What becomes simpler | What becomes harder | First decisive test |
|---|---|---|---|---|
| locking is information export | “collapse” becomes a unitary correlation plus inaccessible branch carrier | one-step channel and storage accounting | why/when that carrier becomes permanently unreadable except as one record | infinite local QCA probe |
| clock is capacity turnover | time rate becomes the rate fresh carrier slots cross a commit front | connects clock and resource limitation | finite stationary systems saturate | count new orthogonal slots per tick |
| reading is source, not formation | repeated processing can sustain current without new records | avoids finite archive exhaustion | gravity source no longer equals formation rate | compare equal archive/different reread rates |
| closed Markov cycle | boundary sink becomes an internal return layer | exact conservation and Green profile | nonzero affinity/fuel remains supplied | reversible dilation with fuel register |
| scalar lapse plus independent spatial law | clocks and transport are separated | honest local universality theorem survives | lensing and tensor dynamics remain open | derive or measure `gamma_PPN` analogue |

## N1 — Alternative Routes

The negative boundaries above were tested against these distinct routes:

1. one-step finite Stinespring dilation — succeeds;
2. a fresh finite coin per tick — succeeds for any fixed finite horizon, with
   growing tape;
3. reuse one finite coin under one unitary — fails to mix and becomes
   ballistic/recurring;
4. exact local Fredkin edge dilation — succeeds per selected edge, leaving the
   edge schedule open;
5. a closed two-layer Markov return cycle — succeeds for conservation and
   Green response, imports affinity and irreversibility;
6. a coherent finite unitary current — can persist but does not mix to the
   unique Green state;
7. a fundamental irreversible append-only commit map — evades the dilation
   wall by taking actualization itself as new physics;
8. an infinite reversible QCA exporting which-path information — not tested to
   closure and remains open;
9. rereading existing records — avoids archive growth but changes source
   identity;
10. an expanding permanent archive front — avoids finite saturation at the
   cost of unbounded carrier and transport;
11. tensor/spatial edge dynamics independent of the scalar scheduler — remains
    required for lensing.

## N2 — Wall-Independence Audit

The walls are not aliases:

| Wall | Countermodel showing independence |
|---|---|
| finite repeated mixing | fresh coins give mixing while archive/source questions remain |
| maintained closed current | the driven `D/C` cycle gives current and Green response while remaining irreversible |
| permanent archive capacity | rereads sustain events without new records even though no formation current exists |
| universal matter coupling | common scheduler gives universal local gaps with either finite or infinite archive |
| tensor/lensing content | two metrics with the same lapse and different `gamma_PPN` give different bending |

Therefore “storage”, “clock”, “current”, “equivalence”, and “tensor gravity”
must not be compressed into one missing sentence.

## N3 — Hidden-Wall Scan

The constructions additionally assume or expose:

- preparation of the invariant coin state;
- partial trace/discard as a physical reduction;
- a schedule for overlapping edge operations;
- a finite `M2` block encoding and an unused coin basis state;
- a nonzero conversion affinity and initial token sector;
- source/sink endpoint data (covariant when transformed, not selected by the
  homogeneous law);
- finite-volume boundary conditions;
- the mass-to-current bridge;
- the debt-to-scheduler sign and coefficient;
- the common-species scheduler clause;
- a weak-metric/PPN comparator for lensing; and
- no proof yet of a translation-covariant non-overlapping archive/resource/
  probe block code on the one-qubit lattice.

## N4 — Residual Matching

The exact finite-environment boundary matches only the residual “where does
the information required by indefinite Markov relaxation go?” It does not
solve probability or select a record outcome. The closed cycle matches only
the ideal reservoir residual. It does not remove the arrow; affinity replaces
the reservoir drive. Archive saturation matches only one-new-record source
laws. The scheduler countermodels match the equivalence/tensor residual, not
record formation.

## N5 — Rhetoric and Resolution

Safe statements are per channel, per finite environment, per archive, and per
weak-field comparator. Unsafe statements rejected here include:

- “unitarity cannot produce diffusion”;
- “a finite environment can never approximate diffusion”;
- “closed systems cannot carry stationary current”;
- “gravity is storage exhaustion”;
- “universal redshift proves the equivalence principle”; and
- “the scalar Green field is GR.”

## N6 — Partial-Closure Paths

No axiom change is needed to retain the one-step dilation or closed-cycle
construction as conditional probes. An axiom would be implicated only if the
framework chooses to make a commit/actualization rule fundamental. The two
live constitutional routes are therefore explicit primitive irreversibility,
or a reversible infinite-carrier theorem. Before choosing between them, the
cheapest science path is:

1. search a covariant infinite reversible QCA that exports branch information;
2. make its archive/read interface explicit;
3. determine whether the clock is derived from information flux or supplied as
   a schedule; and
4. only then test minimal constitutional wording.

The existing scale, kinetic-isotropy, and realized-state primitives do not
supply any missing step.

## N7 — Steelman

The strongest surviving bare-metal model is an infinite, homogeneous,
reversible local automaton. A commit front entangles a local alternative with
fresh lattice degrees, carries the unused branch information outward, and
leaves behind a stable record. A finite observer traces the outward carrier
and sees a Markov channel. The same outward flux could supply a local resource
deficit and clock rate. No external bath is needed because the rest of the
infinite lattice is the bath, archive, and return path.

This steelman evades the fixed-finite-environment theorem and finite archive
saturation. It is not yet a result. It must still preserve one-qubit local
algebra, exact translation/proper-cubic covariance, permanent readable records,
nonzero formation without a privileged seed, probability statistics, closed
resource accounting, universal matter coupling, and tensor lensing.

## N8 — Cross-Cycle Echo

- Cycle 7 found that a cubic quantum walk can support relativistic dispersion
  only after a law/branch choice.
- Cycle 8 repaired exact cubic covariance but retained kernel freedom.
- Cycle 9 showed that local conservative relaxation can generate a Green
  field and scalar attractive lapse, while naming reservoir, renewal,
  reversible-dilation, and tensor costs.
- This cycle closes the one-step dilation and ideal-token-sink costs, but turns
  them into two sharper residuals: fresh-information capacity and nonzero cycle
  affinity. It also proves by paired models that scalar clock universality does
  not close transport or lensing.

The repeated pattern is not “the route fails.” It is that each successful
local construction prices one more independent law clause. The job before any
axiom edit is to discover whether the infinite reversible export steelman
unifies those clauses or merely hides them.

## Axiom-Language Consequence, Not an Axiom Proposal

These probes do not force verbatim axiom text. They do impose four tests on any
future sentence:

1. “read” cannot be a magic verb. The sentence must either name a fundamental
   irreversible commit, or distinguish readable record content from the fresh
   carrier that makes alternatives locally irreversible under a reversible
   completion.
2. “the clock locks it” cannot mean that a scalar time label selects an
   outcome. The clock must name a physical commit/capacity event, or the
   selection mechanism remains absent.
3. A formation clause must say whether each event consumes a fresh permanent
   slot, may reuse an old record, or exports information to an unbounded
   carrier. These are inequivalent sciences.
4. Markov weights, event rates, resource affinity, common scheduler coupling,
   and tensor geometry should remain separate conditional law clauses unless a
   later theorem derives them. None follows from “records form” or from a
   one-step unitary dilation.

The likely bare-metal decomposition is therefore two-stage:

```text
reversible local correlation/transport
    -> append-only commit into fresh distinguishable capacity
    -> later readout of the committed content.
```

Whether the middle arrow is axiom content, a retained theorem from an infinite
QCA, or a named conditional import is still the central open decision.

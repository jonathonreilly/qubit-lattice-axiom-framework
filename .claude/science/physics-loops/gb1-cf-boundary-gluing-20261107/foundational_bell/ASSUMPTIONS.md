# Assumption ledger for the Bell record test

Scope: one finite four-event probability protocol, followed by two alternative
physical-model comparisons. None of the added assumptions below is adopted as
an axiom, primitive or established physical identification. Mathematical
definitions are distinguished from claims that laboratory devices realize them.

## Supplied framework content

| Source | What is used | What is not supplied by it |
|---|---|---|
| Lattice | Actual Z3 adjacency, translations and proper cubic rotations | A time unit, light cone, propagation rate, detector separation protocol |
| Qubit | Full one-site M2(C) possibility domain and algebraic distinctions | A multi-site Hilbert state, tensor composition, Born weights, an entangled preparation |
| Admissibility | One fixed covariant neighborhood content distribution that varies with conditions | Its numerical form; the formation-site/rate rule; independence or factorization of joint outcomes |
| Record | One supported permanent content per recorded site, content-only readout, unreadability of absence | A detector dictionary, trial pairing, a stochastic causal mechanism, prepared apparatus or settings |
| Qualification | State is the record configuration; laws give one answer on their supplied domains | A preferred initial state or a selected physical law |

The registry and all three primitive source notes were checked on current
main. Scale reference supplies units; kinetic isotropy supplies its stated
kinetic-form ratio; realized-state reference supplies pointwise evaluation.
They are approved primitives, not missing imports. We do not use them in the
dimensionless four-record construction. Their source declarations do not
choose its probability table, Born readout or causal factorization.

## A. Define an observable before assigning physics

| Assumption (alias) | Added item | Role and consequence if it is not available |
|---|---|---|
| Recorded roles (O1) | Four identifiable record roles x,y,a,b; two values per role | Defines a CHSH protocol. The axioms do not themselves name this experiment. |
| Content dictionary (O2) | Fixed binary postprocessing of actual contents P and I-P; a fixed trial-pairing convention | Defines numerical observations. Identity readout of the matrix can be used first; absence is never read as an outcome. A lab implementation requires calibration. |
| Joint probability protocol (O3) | A joint probability law with P(x,y)>0 for each setting pair | Makes all four conditional expectations defined. One-site distributions alone do not specify this joint law. |
| Trial population (O4) | The same declared population is used for all correlators, without setting/outcome-dependent rejection | Needed for the causal/quantum comparisons. A changed selection rule must be modeled; no fair-sampling claim is silently assumed. |
| Frequency inference (O5) | For empirical estimation, an actual repeated-trial mechanism and a justified statistical method | The exact theorem is about probabilities. IID repetition is one sufficient option, not a requirement of Bell theory; memory-aware inference needs its own justification. No frequencies or confidence intervals are asserted here. |

O1-O3 define the mathematical question. They are not consequences of the
axioms. O4-O5 state how an empirical use would need to be justified.

## B. Explicit mathematical witness, not a selected law of nature

| Assumption (alias) | Added item | Role and counterfactual |
|---|---|---|
| Chosen kernel (W1) | The complete algebraic kernel F of the existing program theorem | A particular compatible rule, unchanged across the executed r examples. The separate analytical variant fixes the r=1 preparation and explicitly varies F_v through q_v(p)=(1-v)/2+vp; each model still has one fixed rule. |
| Prepared records (W2) | Forty-six permanent initial matrix records: program/buddy pairs, triggers and rigid frame; blank output/path sites | A supplied apparatus/initial condition. Its genesis and precision are not derived. Removing a buddy can destroy old-record support. |
| Probability programs (W3) | All fifteen binary-tree programs, including p_4=[1+r(-1)^(a+xy)]/2 | Stores the desired correlation in preparation. The algebra permits these matrices; it does not select r. The tested r values are declared examples, not fitted data. The fixed-preparation variant instead puts v into the law; no selector for it is derived. |
| Formation routing (W4) | Fixed next-site routing reconstructed from current records, one append at a time, with fresh draws from F | Supplies formation occurrence and order. It consults previous settings/outcomes globally; no local causal actuator or physical clock is asserted. |
| Legal domain (W5) | The lawful domain consists of all spatial translates/proper rotations of these prepared configurations and legal prefixes | A supplied law-domain condition allowed by the qualification. Support is proved on it; no arbitrary preexisting matrix mosaic is assumed legal. |
| Repeated preparations (W6) | Optional independent fresh prepared apparatus copies if used for many trials | Additional apparatus/resource and legal-domain assumptions; the finite construction itself only supplies one trial per preparation, not a composition theorem for many copies. Permanent sites cannot be reused by erasing them. |

For rational examples only rational diagonal matrices are needed. The whole
r in [-1,1] family is an analytic statement allowing exact real program
entries; the finite numerical diagnostic does not exhaust that continuum.
Neither hidden tensor amplitudes nor Born weighting is used in the witness.
The initial parameter/table is a conditional input, not a framework prediction.

## C. Additional hypotheses yielding the classical bound

| Assumption (alias) | Added item | What it does |
|---|---|---|
| Causal mechanism (C1) | A finite causal DAG covering every formation, scheduler, routing and stopping variable; each non-setting variable is a function of its parents and exogenous inputs | Gives a complete classical causal mechanism; permanence of records alone does not supply it. |
| Causal separation (C2) | No path from either chosen setting to the opposite outcome during the trial | Excludes communication that could create the Bell correlation. Arbitrarily many relays outside this forbidden path are allowed. |
| Setting independence (C3) | In the DAG proof, x,y are exogenous setting inputs jointly independent of ALL non-setting exogenous inputs, including preparation, scheduler inputs and private random noise; all setting pairs occur | Supplies one setting-independent distribution of the complete inputs. Internal correlations among those inputs are allowed. Actual setting generators require a justified reduction to this form. Mutual independence of x and y is not needed. |
| Local response form (C4) | P(a,b given x,y)=integral rho(d lambda) P_A(a given x,lambda) P_B(b given y,lambda), with the same rho for all choices | Derived from C1-C3 by taking lambda to include all non-setting inputs; alternatively this factorization can be assumed directly in place of that sufficient DAG derivation. It is stronger than unchanged single-wing marginals. |
| Selection control (C5) | O4, or an explicitly justified selection treatment preserving C1-C4 | Prevents conditioning on later records from silently changing the source distribution. |

C1-C3 are one sufficient structural route, not claimed necessary conditions
for every local model; C4 plus C5 already suffices for the inequality. Merely
requiring settings independent of common outcome ancestors can miss private
inputs correlated with the setting generator. SOURCE_CHECK.md preserves an
explicit counterexample to that weaker formulation.

Under these conditions S<=2 is proved, independently of lattice spacing,
neighborhood radius or the number of intermediary steps. To call C2
spacelike separation requires a physical event/clock/metric/propagation bridge,
which the four axioms do not state. W4 fails C2. Its output marginals still
obey no-signalling; internal program/readout access does not.

This tests a particular classical causal completion of the axioms. It does
not classify every possible record-state or joint-formation law.

## D. Additional hypotheses yielding the quantum bound and its saturation

| Assumption (alias) | Added item | Bound or saturation? |
|---|---|---|
| Composite model (Q1) | A common Hilbert/operator model with commuting wing algebras; tensor composition is sufficient | Needed for the operator calculation. One-site M2 alone does not establish the operational composite. |
| State and observables (Q2) | Self-adjoint dichotomic observables A_x,B_y and a normalized positive state | Needed for the norm/expectation bound. A qubit-valued record content is not automatically such an observable or state. |
| Born readout (Q3) | E_xy=Tr(rho A_x B_y), implemented by the actual measurements and record content dictionary | Born/measurement bridge. Without it the operator bound is not a statement about the record statistic. |
| Common preparation (Q4) | A common preparation rho across setting choices and O4 | Avoids selecting a different ensemble for each setting pair. |
| Saturating apparatus (Q5) | Preparation of Phi+ and calibrated Z,X,(Z+X)/sqrt2,(Z-X)/sqrt2 settings | Needed to attain 2sqrt2, not to prove the upper bound. Noise and calibration errors require explicit bounds for an experiment. |
| Physical realization (Q6) | Physical implementation, causal timing and a trial protocol establishing the intended Bell scenario | Needed for empirical interpretation. An algebraic no-signalling identity does not establish physical implementation. |

Q1-Q4 give S<=2sqrt2; Q5 attains it ideally. The value is selected by the
supplied quantum model. It has not been inferred solely from the record axioms.

## Existing autonomous model: exact accounting

The earlier autonomous-runtime construction supplies a record-indexed initial
density, quantum instruments, Born weights, scalar jump rates, permanent phase
sites and atomic gate/tick jumps with apparatus-dependent finite range. This
removes an external phase counter on its prepared domain. It leaves Q1-Q6's
physical identifications and C1-C4's causal applicability unproved. A phase
record sufficient for mathematical prediction is not a proof of Bell locality.

No wall count, exhaustive reconstruction impossibility or required axiom
amendment follows from this ledger. A motivated candidate joint law may be
studied conditionally; choosing it must remain visible until justified.

The independent checker also gives a scalar 0/I output extension with 131
records at most, resolving the bit-label issue for that extension without
a preferred projector in the final readout. Its proof is in INDEPENDENT.md,
sections 2.4-2.5; it was hand-checked, not numerically replayed here. The
executed 103-record witness uses one constant P menu throughout, so it does
not infer a global bit label for arbitrary history-dependent projectors.

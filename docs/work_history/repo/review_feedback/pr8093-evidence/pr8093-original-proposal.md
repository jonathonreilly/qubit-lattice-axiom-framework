# TOE Derivation Campaign: Axiom Sufficiency By Underdetermination Witnesses

**Date:** 2026-09-13

**Type:** meta

**Claim type:** meta

**Baseline:** the four axioms in `docs/MINIMAL_AXIOMS_2026-06-29.md` (last
changed on `origin/main` at `f1d08841be`, 2026-08-14) together with the three
approved primitives `scale_reference_primitive`, `kinetic_isotropy_primitive`,
and `realized_state_primitive`. This note asserts no theorem, grants no
status, and proposes no axiom, primitive, import, or framing.

## Authority disclaimer

```yaml
actual_current_surface_status: |
  Audit ledger at origin/main b8c9d9d819 (2026-09-13): 4755 rows, 0 retained
  (bounded_theorem 3112, positive_theorem 684, meta 375, no_go 355,
  open_gate 221, decoration 8). Every derivation body on main and in the 81
  open pull requests #8010-#8090 supplies at least one of: a Hamiltonian or
  action, a carrier or encoding, a clock, a formation unit, a rate or an
  order, Born weights, a Gauss kernel, or a readout instrument. No result
  on main is a consequence of the four axioms and three primitives alone.
proposal_allowed: false
proposal_allowed_reason: |
  This note designs a campaign. It adopts no axiom, primitive, import,
  comparator, or framing. Where a block ends in a clause candidate, the
  clause is recorded as an owner decision together with the witness that
  makes the decision necessary; it is not adopted here. Readings of axiom
  text used to define blocks are hypotheses to be tested against the text.
```

## The physical question

Do the four axioms, with the three approved primitives, fix one physics? Or
are there two worlds that satisfy every sentence of the axiom text and still
disagree about what the records say?

If the second, the axioms are underdetermined at that point, and the
smallest clause that separates the two worlds is the axiom change the theory
needs there. If the first, a derivation exists and the task is to find it.
Nothing on `main` presently settles this either way for any physical target:
every derivation body supplies extra structure before it computes, so the
ledger's zero retained rows measure the supplied structure, not a failure of
the axioms.

The campaign therefore does not start from a Hamiltonian, a carrier, or a
tick. It starts from the axiom text and asks, target by target, whether the
text forces the answer. Its two outputs are:

- **Derivations**: theorems whose premises are the axiom text, the three
  primitives, and nothing else.
- **Witnesses**: pairs of models that satisfy the axiom text and the
  primitives and differ on a named target. Each witness is paired with the
  minimal clause that would separate the pair, phrased in the axiom
  document's own register, and left to the owner.

`docs/ai_methodology/SCIENCE_WORKFLOW.md` requires exactly this: a claim of
underdetermination needs witnesses or a proof under matching premises, and a
failed search is neither an obstruction nor an underdetermination.

## The method: witnesses, not surveys

A target `T` is a function of the record statistics (or of the structure the
axioms are read to supply). A **witness for `T`** is a pair of models
`(W_1, W_2)` such that

1. each satisfies every sentence of the Lattice, Qubit, Admissibility, and
   Record axioms as written, and the three primitives as registered;
2. `T(W_1) != T(W_2)`;
3. the difference is exhibited by an exact finite computation (a runner
   printing `TOTAL: PASS=N FAIL=0`), not by a description.

A witness proves that `T` is not a consequence of the axioms. The **minimal
separating clause** is the shortest sentence, in the axiom document's
register, whose addition excludes one of `W_1`, `W_2`. Distinct clauses
excluding the same member are recorded side by side; choosing between them is
owner content.

The precedent on `main` is
`docs/ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13.md`:
two covariant conditional laws (`P_central`, `P_axis`) both satisfy the
Admissibility text, differ on internal symmetry, and the note "selects
neither rule as the framework's physical law." The campaign generalises that
move to every load-bearing target and, for each, either derives or names the
clause.

## What the audit found the axioms already say, and what they do not

Read against the text alone, without any supplied reconstruction:

- **Admissibility supplies a formation law, not a static law.** Reading
  note (2) of the axiom document frames the distribution as "which
  possibility a forming record locks, conditional on formation at that
  site." The static Gibbs or Markov random field used across the repository
  as "the law" is a reconstruction. The open admissibility-rule pull
  requests #8011, #8034, #8035, #8037, #8039, #8065, #8084, and the note
  `docs/ADMISSIBILITY_RULE_INFINITE_STRIP_ROW_SWEEP_FORMATION_LAW_VERSUS_STATIC_LAW_BOUNDED_THEOREM_NOTE_2026-09-06.md`
  on `main`, show the two disagree on every finite window with an edge and
  agree only in a bulk limit.
- **Admissibility supplies no order, clock, unit, or rate.** The axiom
  document says so in its reading note (2) and in "Relation To Dynamics."
- **Record supplies no readout context, weight, or probability.** Only
  records are readable; the formation order is not a record.
- **The realized-state primitive supplies no measure over alternatives.**
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`: "no averaging over
  alternatives, no typical or generic claim, and no quoting a number that
  would differ had another law-admissible state been realized." A quantity
  that changes with the realized formation order is registered data, not
  derivation output, unless the rule is blind to the order.
- **Qubit supplies the one-site algebra and a symmetry sentence.** "No
  possibility is privileged. Possibilities are distinguished by the supplied
  algebraic structure alone." The parallel sentence for sites is read
  throughout the repository as lattice covariance of the rule. The
  possibility sentence has not been read as covariance of the rule under the
  automorphisms of `M_2(C)`; the sigma-linear classification note
  `docs/SIGMA_LINEAR_ADMISSIBILITY_CLASSIFICATION_CYCLE872_BOUNDED_THEOREM_NOTE_2026-07-28.md`
  states that its own "admissible" label "does not invoke and is not
  derived from the framework Admissibility axiom."
- **The `Cl(3,0)` sentence has two readings.** "A `Cl(3,0)`-compatible
  real-algebra presentation may be used equivalently and adds no further
  primitive structure." Either the real three-space generating `Cl(3,0)` is
  the lattice's three-space (so Pauli axes are soldered to lattice axes), or
  the presentation is an isomorphic description of `M_2(C)` with no
  soldering. `main` treats soldering as supplied:
  `docs/ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-14.md`
  says "Retain that block's supplied spatial-to-Pauli soldering." No note
  outside the axiom document interprets the sentence.
- **Lattice lists proper rotations only.** A rule that differs from its
  mirror image is lattice-covariant. Whether it is Qubit-covariant depends
  on whether complex conjugation (the antilinear Clifford involution, the
  one rotation-equivariant automorphism of `M_2(C)` besides the identity)
  counts as "supplied algebraic structure."

These are the seams along which the axioms can be underdetermined. Each
campaign block sits on one seam.

## Formation-order covariance and order-blind rules

**Target and quantified domain.** For every finite window `Lambda` of `Z^3`
and every covariant formation rule `r(v_x | v restricted to A_x)` (with
`A_x` the recorded nearest neighbours of `x`), the dependence of the joint
law `mu_sigma(v) = prod_k r(v_{x_k} | v restricted to A_{x_k})` on the
formation order `sigma`.

**Current main revision and source/claim identifiers.** `origin/main`
`b8c9d9d819`; the Admissibility axiom's reading note (2); pull request
#8035 finding G2 ("The precision depends on the order only through the
recorded sets; the monotone class of a rectangle gives one law") and G3
("the formation law is never the static law on a window with an edge");
`docs/A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md`
("Order independence is a separately supplied comparison requirement …
Sequential Lueders satisfies it by the commuting-projector Born chain
rule").

**Accepted premises and separately supplied conditions.** Lattice, Qubit,
Admissibility, Record as written; `realized_state_primitive`. Nothing else.

**Closest existing result and exact missing obligation.** #8035 G2 shows
that within a monotone class the order is invisible and across classes it is
not. Missing: (i) the covariance lemma that no sequential order can be
covariant; (ii) the characterisation of rules for which `mu_sigma` does not
depend on `sigma` at all.

**New construction, proof mechanism, or discriminating test.**

- *Lemma (formation-order covariance).* No total order on `Z^3` is invariant
  under a proper cubic rotation `R` of finite order `m > 1` about a site
  (if `x < Rx` then `x < Rx < R^2 x < … < R^m x = x`). Hence a sequential
  single-site formation process is never covariant in the sense of the
  Lattice axiom. Three covariant alternatives remain: joint formation on
  covariant sets; a random order with a covariant order law; or an
  order-blind rule, for which the order is physically idle.
- *Order-blind characterisation.* `mu_sigma` is independent of `sigma` for
  all `sigma` if and only if the rule satisfies a local exchange identity on
  every adjacent pair: `r(a | S) r(b | S + a) = r(b | S) r(a | S + b)` for
  all recorded sets `S` and values `a, b` (a detailed-balance identity on
  the formation graph). The block proves this exactly on finite windows,
  and characterises the order-blind rules in the binary, ternary, and
  Bloch-vector alphabets. The quantum reconstruction of an order-blind rule
  is a commuting family of record projectors, which connects the block to
  the sequential-Lueders finding above.
- *Order-mixture computation.* For the binary rule family, compute on the
  `2x3`, `3x3`, and `2x2x2` windows with exact rationals: the uniform
  order mixture `mu_bar = (1/n!) sum_sigma mu_sigma`; the static law `mu`;
  the monotone-class laws `mu_P`; and the spread across orders. The mixture
  is a witness-generating device, not a candidate law: the realized-state
  primitive supplies no measure over orders, so `mu_bar` is licensed only
  if a clause supplies it.

**Success witness / counterexample / inconclusive outcome.** Success: the
lemma and the exchange characterisation land as theorems, and the
order-blind class is exhibited (possibly trivial: it may contain only
product rules, which is itself the decisive finding). Witness: a rule with
`mu_sigma != mu_sigma'` for two orders on `2x3`, exhibited exactly.
Inconclusive: none; the computations are finite.

**Downstream question this would resolve, or frontier-discovery value.**
Whether any record statistic computed anywhere in the repository from a
static law is derivation output or registered data. If the physical rule is
order-blind, the static reconstruction is licensed; if not, every
order-dependent quantity is registered data until a clock or unit clause is
added (the clock-and-rate and formation-unit blocks).

**Next decision and condition for reopening an exhausted route.** No owner
decision is required to execute this block. It runs first.

## Possibility covariance and the soldering fork

**Target and quantified domain.** The symmetry group under which the
Admissibility rule must be covariant on the possibility side, and the set of
rules it permits. Domain: all rules `r(p | q_1, …, q_6)` with `p, q_i` in
the one-site state space (Bloch ball `B^3`, with the pure states `S^2` as a
sub-case) and empty slots marked unrecorded.

**Current main revision and source/claim identifiers.** `origin/main`
`b8c9d9d819`; the Qubit axiom's "No possibility is privileged" sentence and
its `Cl(3,0)` sentence; the barycenter selector note (supplied soldering);
the Q8 law-pair note (`P_axis` needs an axis, `P_central` does not);
`docs/INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`
("coming from the Clifford universal property are the same operators").

**Accepted premises and separately supplied conditions.** Lattice and Qubit
as written. Two readings of the `Cl(3,0)` sentence are carried as named
hypotheses, not as premises:

- *Unsoldered reading.* The rule is covariant under `Aut(M_2(C))`, the
  inner automorphisms, acting as `SO(3)` on the Bloch ball, independently of
  lattice rotations. If complex conjugation counts as supplied structure,
  the group is `O(3)`.
- *Soldered reading.* The three generators of `Cl(3,0)` are the lattice
  axes, so a lattice rotation acts simultaneously on sites and on Bloch
  vectors, and the rule need only be covariant under the diagonal action.

**Closest existing result and exact missing obligation.** The barycenter
note proves selection theorems given soldering. The Q8 note exhibits the
law pair. Missing: the classification of rules under each reading, and the
consequences each reading forces without further input.

**New construction, proof mechanism, or discriminating test.**

- *Invariant-theory classification.* Under the unsoldered reading a rule is
  a function of the `SO(3)` invariants of the seven Bloch vectors (the Gram
  entries `p.q_i`, `q_i.q_j`, the norms, and, if the group is `SO(3)`
  rather than `O(3)`, the triple products) that is also symmetric under the
  proper cubic permutations of the six slots. Under the soldered reading the
  additional invariants `p.e_a`, `q_i.e_a` (Bloch component along a lattice
  axis) are available and the barycenter compiler `D(d) = [I + d.sigma/3]/2`
  becomes expressible.
- *Empty-neighbourhood law.* With no recorded neighbours, an
  `Aut`-covariant distribution on the pure states is the uniform (Haar)
  measure on `S^2`; on the Bloch ball its radial profile is free. Any
  antipodal two-outcome menu therefore has weights `1/2, 1/2`. This is the
  "fair coin" that
  `docs/THE_BORN_PRICE_WORDINGS_HOMOGENEITY_IS_PAYABLE_ON_THE_CONTINUUM_LAW_AS_IT_STANDS_THE_COLLINEAR_MENUS_NEED_A_SCALE_READING_RULE_THE_FOUR_OUTCOME_MENU_PAYS_WITH_NO_CLAUSE_AND_NONE_REMOVES_THE_FAIR_COIN_BOUNDED_NOTE_2026-09-05.md`
  found no clause removes; under the unsoldered reading it is derived.
- *Witness for the fork.* Two rules, one depending on `p.e_z` and one
  depending only on invariants, both covariant under the diagonal action,
  differ on record statistics. The pair satisfies the soldered reading;
  only the second satisfies the unsoldered reading. This is the exact
  content of the fork.

**Success witness / counterexample / inconclusive outcome.** Success: the
two classifications land as exact statements with finite exhibits; the
Haar consequence lands. Counterexample: none possible at this level, the
block is a classification. Inconclusive: none.

**Downstream question this would resolve, or frontier-discovery value.**
Every emergent-symmetry lane on `main` (Lorentz at the Dirac point, the
internal-external `SU(2)` merger, the `Cl(3)` carrier lanes) presupposes the
soldered reading. Under the unsoldered reading the internal `SU(2)` is a
separate symmetry, which changes what the framework predicts about spin.

**Next decision and condition for reopening an exhausted route.** Owner
decision: which reading of the `Cl(3,0)` sentence is intended, or whether
the sentence should be refined to state one. The precedent for a refinement
is the 2026-08-05 Admissibility second-sentence change recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md`. Until decided, both readings run
as named conditionals.

## Handed-rule census (triple-product chirality)

**Target and quantified domain.** Whether a covariant Admissibility rule may
differ from its mirror image in a way that leaves a handed trace in record
statistics; the domain is the Bloch-vector alphabet on nearest-neighbour
windows of `Z^3`.

**Current main revision and source/claim identifiers.** `origin/main`
`b8c9d9d819`;
`docs/A_MIRROR_ASYMMETRIC_ADMISSIBILITY_RULE_REGISTERS_ITS_OWN_PARITY_ODD_TEXTURE_AND_NOTHING_ELSE_THE_EMERGENT_FERMIONS_MOVERS_ARE_TIME_REVERSAL_IMAGES_WITH_IDENTICAL_RECORD_LAWS_BOUNDED_NOTE_2026-09-05.md`
(all 40320 cube orders give `max|chi4| = .088127`, the uniform average
vanishes, mirrored orders have opposite signed correlators);
`docs/A_TIME_DIRECTED_FORMATION_SWEEP_REGISTERS_THE_DIRECTION_OF_MOTION_AT_ORDER_ONE_AND_ITS_SCREW_SENSE_REGISTERS_NOTHING_THE_RECORD_SIDE_IMAGE_OF_A_CURRENT_NOT_A_CHIRALITY_BOUNDED_NOTE_2026-09-05.md`
(binary alphabet; all 729 profiles under 24 proper rotations);
`docs/DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md`
and
`docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md`
(all emergent matter content so far is vector-like).

**Accepted premises and separately supplied conditions.** Lattice (proper
rotations only) and Qubit as written; the possibility-covariance block's two
readings as named hypotheses.

**Closest existing result and exact missing obligation.** The mirror note
shows order-induced handedness in the binary alphabet averages to zero
under a supplied uniform order and is a time-reversal image, not a
chirality. No note on `main` constructs a rule with a pseudo-scalar term.
Missing: the census of pseudo-scalar invariants available to a covariant
rule, and the record statistics they leave.

**New construction, proof mechanism, or discriminating test.** With
`d_a = q_{+a} - q_{-a}` the opposite-neighbour differences along the three
axes, the scalar `T = det[d_x, d_y, d_z]` is invariant under proper cubic
rotations (which act on the triple by a signed permutation of determinant
`+1`) and under internal `SO(3)`, and odd under improper lattice rotations
and under internal reflections including complex conjugation. A rule with
a `T`-dependent term is therefore lattice-covariant, Qubit-covariant under
the `SO(3)` reading, and not Qubit-covariant under the `O(3)` reading. The
block: (i) enumerates the pseudo-scalar invariants of lowest degree under
each reading; (ii) computes, on `2x2x2` and `3x3x3` windows with an
order-blind base rule (formation-order block), the parity-odd record correlators a
`T`-term produces; (iii) exhibits the witness pair (a `T`-rule and its
`T`-free part) and states the separating clause: whether the Qubit
symmetry sentence means `SO(3)` (proper automorphisms) or `O(3)`
(automorphisms and conjugation).

**Success witness / counterexample / inconclusive outcome.** Success: a
`T`-rule leaves a nonzero parity-odd record correlator on a finite window,
exhibited exactly, and the same rule's mirror leaves the opposite sign.
Counterexample: every `T`-term's parity-odd trace vanishes on the record
side for order-blind rules (then rule-handedness is invisible and chirality
must come from elsewhere). Inconclusive: none.

**Downstream question this would resolve, or frontier-discovery value.**
The standing chirality gap (Koide chirality gate, the weak sector's
handedness, the vector-like taste census). Under an order-blind rule,
order-induced handedness is absent and rule-handedness is the one remaining
law-level source; whether it is admissible is a one-word clause on the
Qubit axiom.

**Next decision and condition for reopening an exhausted route.** Owner
decision on the Qubit symmetry group follows from the possibility-covariance decision.
The parked structuralist reading in `docs/repo/DEFERRED_DECISIONS.md` §2
is not re-raised here; this block supplies one of its named wake
conditions if the antilinear recoding question is settled by the census.

## Menus from neighbours and the Born overlap function

**Target and quantified domain.** The support and the weights of the
formation law at a site with one to six recorded neighbours; whether the
Born form `r(p | q) = (1 + p.q)/2` on antipodal menus is forced.

**Current main revision and source/claim identifiers.** `origin/main`
`b8c9d9d819`; the Born-price wordings note above;
`docs/COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md`;
`docs/BORN_FORM_MENU_OUTCOME_THRESHOLD_AND_MIXED_PROJECTIVE_FORCING_BOUNDED_THEOREM_NOTE_2026-07-17.md`
(Busch 2003, Caves-Fuchs-Manne-Renes 2004, Wright-Weigert 2019 as
context-only comparators).

**Accepted premises and separately supplied conditions.** Qubit and
Admissibility as written; the unsoldered reading of the
possibility-covariance block as a named hypothesis. No additivity or non-contextuality clause is assumed.

**Closest existing result and exact missing obligation.** The Born lanes
prove the Born form conditional on a supplied menu and a supplied
additivity or homogeneity clause; the four-outcome menu pays with no clause.
Missing: whether the menus themselves can be generated by the recorded
neighbours rather than supplied.

**New construction, proof mechanism, or discriminating test.** Under
`Aut`-covariance no site-independent finite menu is admissible (a finite
subset of `S^2` is not `SO(3)`-invariant), so a finite support must be
selected by the recorded neighbours: with one recorded neighbour `q` the
covariant supports are unions of `SO(2)_q`-orbits, of which `{q, -q}` is
the smallest with two points and the circle `p.q = 0` the smallest
continuous one. The block classifies the covariant supports for one, two,
and three recorded neighbours in general position and on the cubic axes,
and asks which overlap functions `f(p.q)` are consistent with the exchange
identity of the formation-order block (order-blindness). If the exchange identity together
with covariance forces `f` affine, the Born form is derived on antipodal
menus with no additivity clause; if not, the witness is a non-affine `f`
and the separating clause is an additivity sentence (owner content, since
it is a Busch-type import).

**Success witness / counterexample / inconclusive outcome.** Success: `f`
is forced affine by covariance plus order-blindness (Born derived).
Witness: an explicit non-affine covariant order-blind `f` (Born needs a
clause; text recorded). Inconclusive: none.

**Downstream question this would resolve, or frontier-discovery value.**
Whether quantum probabilities are law content or clause content in this
framework; the register-not-read admission class.

**Next decision and condition for reopening an exhausted route.** No owner
decision is needed to run the classification; the clause candidate, if
reached, is an owner decision.

## Continuum-alphabet readability

**Target and quantified domain.** Identifiability of the rule `r(p | q)`
from the record statistics of finished windows, in the Bloch-vector
alphabet, for order-blind rules (formation-order block) and for order-dependent rules
under a supplied order law.

**Current main revision and source/claim identifiers.** `origin/main`
`b8c9d9d819`;
`docs/THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md`
(nearest-neighbour binary tables are all-permissive; "What buys it its
economy is the alphabet, not the geometry"); the readability lane's
Stipulation R ("an additional static protocol, not a consequence of Record
permanence").

**Accepted premises and separately supplied conditions.** Record as
written (only records are readable, formation order is not a record).

**Closest existing result and exact missing obligation.** The binary
alphabet cannot expose the rule at nearest-neighbour range. Missing: the
same question for the continuum alphabet the Qubit axiom actually
supplies.

**New construction, proof mechanism, or discriminating test.** Fisher
information of the finished-window law with respect to the parameters of a
covariant rule family; rank deficiency marks the unreadable directions.
Computed exactly (symbolic) on `2x3` and `2x2x2` for polynomial rule
families in the invariants of the possibility-covariance block.

**Success witness / counterexample / inconclusive outcome.** Success: full
rank for order-blind rules (the law is readable from records alone).
Witness: rank deficiency exhibited, with the unreadable direction named.

**Downstream question this would resolve, or frontier-discovery value.**
Whether the framework's law is in principle an observable of its own
records.

**Next decision and condition for reopening an exhausted route.** None
required.

## Clock-and-rate clause witness

**Target and quantified domain.** Whether any finished-window statistic
depends on the formation-rate law, for covariant rate laws (uniform;
neighbour-count dependent; neighbour-value dependent) on `2x3`, `3x3`,
`2x2x2`.

**Accepted premises and separately supplied conditions.** Admissibility as
written (supplies no rate); `realized_state_primitive` (supplies no measure
over orders).

**New construction, proof mechanism, or discriminating test.** Independent
exponential clocks with a covariant rate law induce an order law; different
rate laws induce different order laws and, unless the rule is order-blind,
different finished-window laws. Exhibit the pair exactly. Separating clause
candidates, recorded not adopted: (a) "records form at a rate that does
not depend on the nearest-neighbour conditions"; (b) "records form at a
rate determined by the nearest-neighbour conditions"; (c) no clause, and
every rate-dependent statistic is registered data by the realized-state
primitive.

**Success witness / counterexample / inconclusive outcome.** Witness
expected unless the formation-order block finds the physical rule order-blind, in which case
the block reports that no clause is needed.

**Downstream question this would resolve, or frontier-discovery value.**
Whether time enters the theory only as record count (emergent, as the
owner holds) or needs a rate sentence.

**Next decision and condition for reopening an exhausted route.** Owner
decision among (a), (b), (c) after the witness is exhibited.

## Formation-unit clause witness

**Target and quantified domain.** Single-site formation ("for each site" in
the Admissibility text) against joint formation on a covariant set, on the
finished-window law.

**Current main revision and source/claim identifiers.**
`docs/THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_OF_THE_SUPERLATTICE_ROLE_PATTERN_THE_EIGEN_SET_CRITERION_IS_ONE_PARTICLE_AND_ITS_MINIMAL_SETS_ARE_THE_PARITY_CLASSES_BOUNDED_NOTE_2026-09-04.md`;
`docs/JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md`;
the relaxation-tick note ("Simultaneous recording is unnecessary" for
commuting projectors).

**New construction, proof mechanism, or discriminating test.** For an
order-blind rule, sequential single-site and joint formation agree (the
commuting-projector chain rule). For a rule that is not order-blind, the
joint law on a covariant set differs from every sequential law. The witness
is that difference on the smallest covariant set (a site and its six
neighbours). Separating clause candidates: keep "for each site" (single
site is the unit) or refine to "for each admissible set of sites."

**Success witness / counterexample / inconclusive outcome.** As in the
clock-and-rate block.

**Downstream question this would resolve, or frontier-discovery value.**
The owner's 2026-09-03 design intuition that neighbourhood conditions move
as units (glued, breakable, free) becomes a statement about the formation
unit; the support-rule block gives the glued case.

**Next decision and condition for reopening an exhausted route.** Owner
decision after the witness.

## Record-process dynamics: unrecorded sites carry no law-level state

**Target and quantified domain.** Whether any evolution law for unrecorded
sites is a consequence of the axioms.

**Current main revision and source/claim identifiers.**
`docs/U1_DYNAMICS_CLASS_AXIOM_ADJUDICATION_BOUNDED_NOTE_2026-09-05.md`
("The four axioms do not currently select that class. In particular, they
do not state real linear first-order evolution, energy conservation,
minimal (E,B) payload, or continuous time");
`docs/U1_RADIUS_ONE_ONSITE_UNITARY_MINIMAL_MAXWELL_TICK_BOUNDED_NO_GO_NOTE_2026-09-03.md`.

**Accepted premises and separately supplied conditions.** All four axioms;
`realized_state_primitive` (no boundary condition, no default state).

**New construction, proof mechanism, or discriminating test.** The witness
is on `main`: two unitary tick classes both consistent with the axiom text.
The campaign's construction is a reframing to be tested, not adopted: the
one dynamics the axioms describe is record formation, so the photon and
every propagating mode must appear as a statistic of the finished record
field under the formation law, not as a unitary tick on unrecorded sites.
Test: on `main`'s half-filled staggered sea, compute the record-side
two-point function of the formation law (formation-order through
menus-and-Born blocks) and compare its
long-wavelength form with the lattice Laplacian's Green function (the
gravity lane's `G(r) -> 1/(4 pi r)`) and with a transverse (curl-type)
kernel. A transverse record correlator with no supplied Maxwell tick would
be the frontier finding.

**Success witness / counterexample / inconclusive outcome.** Success: a
transverse or Laplacian kernel appears in record statistics with no tick
supplied. Counterexample: the record-side correlators of every covariant
order-blind rule are short-ranged (then long-range fields need a clause,
and the clause candidates are those of the clock-and-rate and
formation-unit blocks).

**Downstream question this would resolve, or frontier-discovery value.**
Whether "dynamics" is a fifth axiom in disguise or a corollary of record
statistics.

**Next decision and condition for reopening an exhausted route.** None
required to run; the reframing is not adopted by running it.

## Composition and law selection

**Target and quantified domain.** Cross-site composition (tensor against
graded) and its relation to the choice of rule.

**Current main revision and source/claim identifiers.**
`docs/COMPOSITION_DISCRIMINATOR_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-02.md`
(PASS=19; graded zeros are the patterns fixed by a lattice automorphism
with `chi(sigma) sgn(sigma|_S) = -1`); pull request #7834 (a three-space
point fermion on `Z^3`, one qubit per site, translation-invariant law, via
the superfast encoding on the coarse lattice `2Z^3`).

**Accepted premises and separately supplied conditions.** All four axioms;
the owner's rulings of 2026-09-02 that the lattice is physical and that
fermions are not the sites.

**Closest existing result and exact missing obligation.** The witness is
on `main`: both products satisfy every axiom sentence, and record
statistics separate them. #7834 shows tensor composition on `Z^3` supports
an emergent fermion once a specific law is chosen. The obligation
therefore moves from composition to law selection: which covariant rule's
record statistics carry the graded zeros of the discriminator theorem. The
block tests the order-blind rules of the formation-order block against the discriminator's
selection rule on `2x2x2`.

**Success witness / counterexample / inconclusive outcome.** Success: a
covariant order-blind rule reproduces the graded zero pattern (the fermion
is a consequence of the rule, not of a composition clause). Witness: no
such rule exists in the classified families (then a composition or
encoding clause is needed; text recorded).

**Downstream question this would resolve, or frontier-discovery value.**
Whether matter is law content.

**Next decision and condition for reopening an exhausted route.** None
required to run.

## Glued groups as support rules (Gauss law)

**Target and quantified domain.** Whether a covariant rule's zero-probability
set (its support complement) implements a local constraint on finished
records whose free part carries a gauge structure, on `2x2x2` and `3x3x3`.

**Accepted premises and separately supplied conditions.** Admissibility
reading note (3) of the axiom document: "'available'/'admissible' denotes
its support."

**New construction, proof mechanism, or discriminating test.** A support
rule is a constraint satisfaction problem on records. The block classifies
the covariant support rules in the binary and ternary alphabets whose
satisfying configurations form a group under a local operation (`Z_2` and
`Z_3` cases), identifies which are Gauss-type (a divergence condition on
edge variables built from adjacent record pairs), and computes the finished
record statistics of the order-blind rules restricted to the support. The
owner's glued groups (2026-09-03) are exactly configurations that cannot be
separated without leaving the support.

**Success witness / counterexample / inconclusive outcome.** Success: a
covariant support rule whose free part is a `Z_2` gauge theory on records
appears in the classified family. Counterexample: no nearest-neighbour
covariant support rule has a Gauss-type zero set (then gauge structure needs
the next-nearest window, which the owner allows for operational blocks).

**Downstream question this would resolve, or frontier-discovery value.**
Gauss's law as an instance of gluing; the `U(1)` and `SU(3)` lanes'
carriers.

**Next decision and condition for reopening an exhausted route.** None
required to run.

## Candidate assembly and gravity downstream

**Target.** The connected proposed derivation with named gaps that
`docs/ai_methodology/SCIENCE_WORKFLOW.md` defines as the candidate theory.
Nodes: the formation law (formation-order, possibility-covariance, and
menus-and-Born blocks); the record alphabet and menus (menus-and-Born
block); chirality (handed-rule block); dynamics as record statistics
(record-dynamics block); matter (composition block); gauge structure
(support-rule block); gravity (`(kappa, nu) = (1,
1)` conditional; the exact Regge result of pull request #8085; the Ward
scalar bound of #8086). Each node is labelled `derived`, `conditional` (on
which named clause), or `clause-needed` (with its witness). The gravity node
takes as input the covariant scalar record statistic whose two-point
function on the formation law is the lattice Green function; that statistic
is a record-dynamics block output.

**Success witness.** A directed graph in which every edge is a landed
theorem or a named clause, with no unlabelled edge. No percentage or
completion figure is attached to it.

## Axiom-change verdict table (to be filled by execution)

Each row records, for a target, whether execution found it derivable from
the axiom text, or exhibited a witness and a minimal separating clause. The
"witness status" column distinguishes witnesses already on `main` from
those to be computed.

| Target | Attack | Clause candidate if a witness stands | Witness status |
|---|---|---|---|
| Covariance of a sequential formation order | Lemma (formation-order block) | none; a theorem | to land |
| Order-dependence of finished-window statistics | Exchange characterisation (formation-order block) | clock or unit clause, or accept registered-data status | to compute |
| Static versus formation law | Reconstruction status (formation-order block) | none; the static law is a bulk limit | on `main` (#8035, strip note) |
| Internal-to-lattice soldering | Two readings of `Cl(3,0)` (possibility-covariance block) | refine the `Cl(3,0)` sentence to one reading | to compute |
| Empty-neighbourhood law, fair coin | Haar on `S^2` (possibility-covariance block) | none under the unsoldered reading | Born-price note |
| Rule handedness | Pseudo-scalar census (handed-rule block) | Qubit symmetry: `SO(3)` or `O(3)` | to compute |
| Born overlap function | Covariance plus order-blindness (menus-and-Born block) | additivity sentence (owner content) | Born lanes (conditional) |
| Menus | Neighbour-generated supports (menus-and-Born block) | none if derived | to compute |
| Law readability | Fisher rank (readability block) | none; a property | binary no-go on `main` |
| Formation rate | Rate-law pair (clock-and-rate block) | rate sentence, or registered data | to compute |
| Formation unit | Single-site against joint (formation-unit block) | "for each site" against "for each admissible set" | to compute |
| Evolution of unrecorded sites | Record-statistics reframing (record-dynamics block) | none proposed | on `main` (U1 adjudication) |
| Composition | Law selection (composition block) | none if a rule carries the graded zeros | on `main` (#7833, #7834) |
| Gauss constraint | Support-rule classification (support-rule block) | none if a support rule is Gauss-type | to compute |

## Execution cadence

The formation-order, handed-rule (census part), readability, composition,
and support-rule blocks require no owner decision and run first, in that
order, each as a source-only triple (one note in `docs/`,
one runner in `scripts/` printing `TOTAL: PASS=N FAIL=0` under 6000
characters of output, one cache in `logs/runner-cache/`), on a fresh branch
off `origin/main` per block, with milestone pull requests. The possibility-covariance and
menus-and-Born blocks run as classifications with both readings carried as named conditionals.
The clock-and-rate and formation-unit blocks run as witness computations
and end in owner decisions. The record-dynamics block runs as a test of a
reframing, not an adoption. The assembly block is assembled last from
landed nodes only.

Runner budgets: exact rational arithmetic on windows of at most 27 sites;
no dense many-body state spaces above `2^11`; every number printed is a
bound check or an exact rational, not a noise digit.

## What this note does not do

It does not grade any result, does not adopt any reading of the axiom
text, does not register any clause, and does not attach a completion figure
to the theory. Each block's outcome lands in its own note with its own
runner and is graded by the audit lane.

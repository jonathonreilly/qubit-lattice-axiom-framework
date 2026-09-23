---
claim_id: admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN a supplied clause, not adopted: (C1) every site of Z^3 has a positive tick rate w_x; (C2) the rate at a site is determined by the rates at its six nearest neighbours by one rule, covariant under translations and proper cubic rotations; (C3) the rule is scale covariant: multiplying every rate by t multiplies the answer by t, because without a master clock only ratios of rates mean anything. The axioms memo defines no time metric; the clause is a candidate filling of that open gate and is not derived from the axioms. (T1) A linear nearest-neighbour law for u = log w that is covariant and admits the shift u -> u + const is c_0 (u_x - (1/6) sum over the six neighbours) = s_x, that is minus c_0/6 times the lattice Laplacian: the 24 rotations are transitive on the six directions and fix only the constant coefficient vector. (T2) Any rule w_x = F(six neighbouring rates) with F symmetric under the rotations, homogeneous of degree one and equal to one on uniform rates has all six first derivatives equal to 1/6 at the uniform point, so every such rule has the law of T1 as its weak-field form; the second order is not universal ((p - 1) d^2/6 for the power mean of order p); the geometric mean is exactly linear in u; the product of the six rates has degree six, is not scale covariant, and its symbol 1 - 2 sum cos k_i changes sign. (T3) On a torus the law has rank L^3 - 1: only the part of the source with zero sum enters and u is fixed up to a constant, which no ratio of rates can see. (T4) A clause that gives a record an absolute rate is not scale covariant; a covariant clause gives it a ratio kappa to its neighbours' mean, that is the source log kappa at the record: the field of any arrangement of records is exactly the sum of single fields, the pair term is symmetric, and with kappa < 1 clocks run slow near records. One number, kappa, is left. (T5) A test record whose symmetric hops are timed by the clock of the site it sits on has the stationary law 1/w_x = exp(-u_x): it gathers where clocks run slow; this is a drift, not an acceleration. CORRESPONDENCE (of form, no gravitational claim): the three supplied pieces of the weak-field packet on main (operator minus lattice Laplacian with the zero mode projected out; a local additive source; response L(1 - phi)) are what T1 to T4 give with phi = -u and the record count of block 41 as the source. NOT claimed: the clause itself, the value of kappa, the non-linear completion, inertia (acceleration), any delay of the field, any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_no_master_clock_neighbour_determined_scale_covariant_tick_rate_lattice_laplace_equation_additive_sources_2026_09_21.py
---

# No master clock: a neighbour-determined, scale-covariant tick rate obeys the lattice averaging equation, its zero mode is unobservable, and records enter as additive sources

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about every law of a supplied class; the class is a supplied clause, not derived from the axioms; nothing adopted or registered; unaudited)

This note works within a supplied clause for local tick rates; it reports what field equation, what zero mode and what kind of source the clause forces; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Blocks 41 to 52 (decision record, PR #8555) ended with: the record layer supplies the source, the record count, and not the carrier. The weak-field packet on `main` has three supplied pieces: a field equation, a source, and a response in which the potential is a shift of a local rate (`S = L(1 − φ)`). Its field equation is supplied, not derived. The axioms memo defines no time metric: rates, update laws and the time metric are open gates.

This note takes the response law at its word — the potential is a local tick rate — and asks what law such a rate can obey when there is no master clock.

**The clause (supplied).** Every site has a positive tick rate. The rate at a site is determined by the rates at its six nearest neighbours, by one rule covariant under translations and proper cubic rotations — the form the Admissibility axiom has for the odds. And only ratios of rates mean anything, so multiplying every rate by the same number must multiply the answer by that number.

1. **The field equation is forced.** Every such rule, linear or not, has the same weak-field form: `u_x` equals the average of `u` over the six neighbours, `u = log w` (T1, T2). That is the lattice Laplacian, the operator the packet supplies. It has no mass term because a mass term would single out a value of the rate, that is, a master clock.
2. **The zero mode is unobservable.** On a closed lattice only the part of the source with zero sum enters, and `u` is fixed up to a constant that no ratio of rates can see (T3): the packet's projection.
3. **Records enter as additive sources.** A clause that gives a record an absolute rate needs a master clock. A covariant clause gives it a ratio `κ` to the mean of its neighbours' rates, which is a source `log κ` at the record. The field of any arrangement of records is then exactly the sum of single fields, the pair term is symmetric, and with `κ < 1` clocks run slow near records (T4). One number is left: `κ`.
4. **What a record does in such a field.** A test record whose hops are timed by the clock of the site it sits on is found with probability proportional to `1/w = exp(−u)`: it gathers where clocks run slow (T5). That is a pull on the record count with steady masses, exactly additive, the same in every direction at long range — none of the three defects of the capture picture's pull — but it is still a drift and not an acceleration.

So, within the clause: **the packet's operator, its zero-mode projection and the additivity of its source follow from "there is no master clock", and what remains supplied is one number and the law of motion.** Acceleration needs a record whose phase, not only whose waiting time, is timed by the local clock: the amplitude layer. That is the next block.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "decision record (PR #8555), revised recommendation: 'the carrier has to come from the amplitude layer, where the gravity lane's field equation is at present supplied rather than derived; the next work is the source link'; record-pair source note on main: 'a local lattice conservation/attachment law, including cadence and zero mode' and 'an independently fixed ... coupling' are missing"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "within the clause the operator, the zero-mode projection and the additive record source of the weak-field packet are forced, and one number kappa is left; next: a record whose phase is timed by the local clock (a walk with the qubit as coin) and whether it accelerates in the field; the value of kappa; the non-linear completion; a delay of the field"
conditional_surface_status: "T1, T2 exact statements about every law of the supplied class (T2 at first order); T3, T4 exact for the linear law on tori, and on the infinite lattice by superposition of lattice potentials; T5 exact for one test record; the class itself is a supplied clause"
hypothetical_axiom_status: "the clause C1-C3 (local tick rates; neighbour-determined, covariant; scale covariant), the ratio clause for records, and for T5 the timing of a record's hops by the local clock; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) is used through the Lattice axiom, through the covariance sentence of Admissibility ("covariant under lattice translations and proper cubic rotations"), and through its statement that Admissibility does not "define a time metric": rates and the time metric are open gates outside the axioms. Nothing here fills that gate by derivation. Block 41 (open PR #8547) supplies the record count as the only local additive invariant density of the record layer; blocks 45 to 52 and the decision record (open PRs #8553 to #8564, #8555) are the context. The weak-field packet is `docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md` on `main`; it is used as a statement of what is to be obtained, not as a premise.

- **Tick rate.** A positive number `w_x` per site; `u_x = log w_x`. Only ratios `w_x/w_y = exp(u_x − u_y)` are taken to be observable: over any stretch, the numbers of ticks at two sites stand in that ratio.
- **The class of laws.** `w_x = F(w_{x+e_1}, …, w_{x−e_3})` at every site, `F` positive, differentiable, unchanged by the 24 permutations of its arguments induced by the proper rotations of the cube, and homogeneous of degree one. `F(1, …, 1) = 1`, so that uniform rates solve the law in empty space.
- **Record clause.** At a record, `w_x = κ F̃(neighbours)` with `F̃` of the same class; `κ` is the ratio of the record's rate to the mean of its surroundings.
- **Test record.** A single record that hops to each neighbour at the rate `w_x/6`.

The equation `u_x` = average of its neighbours is the lattice form of the equations of Laplace and, with a source, of Poisson; its inverse is the lattice function of Green; solvability on a closed lattice only for sources of zero sum is the alternative of Fredholm; the degree-one identity is Euler's for homogeneous functions. That the potential of gravitation is a local rate of clocks is the content of the redshift of Einstein (1907, 1911), and a scalar theory of that kind is Nordström's; the insolubility of the static equation for a uniform density of sources is the paradox of Seeliger. A stationary law proportional to the inverse of a site-dependent jump rate is elementary for processes named after Markov. None is used as authority.

## Prior art and what is new

Every ingredient is classical. What is new is the argument inside the framework's vocabulary: that the absence of a time metric in the axioms, read as "only ratios of rates mean anything", together with the form the Admissibility axiom already has (determined by nearest neighbours, covariant), forces the operator and the zero-mode projection that the weak-field packet supplies; that the same premise excludes records that pin an absolute rate and so forces additive sources; and that it leaves exactly one number. It is a conditional derivation of a supplied piece, not a gravitational claim.

## Exact target and obligation graph

Target: what law a local tick rate can obey without a master clock, and how records can enter it. Obligations: (O1) linear laws; (O2) all laws at first order, and what is not forced; (O3) the zero mode; (O4) how records enter, additivity; (O5) what a record does in the field. T1–T5 discharge them.

## Theorem T1 — linear laws

Let `c_0 u_x + Σ_e c_e u_{x+e} = s_x` hold at every site, `e` over the six neighbour directions. Covariance under the proper rotations of the cube about a site requires `c_{ge} = c_e`; the 24 rotations are transitive on the six directions, and the coefficient vectors they leave unchanged form a one-dimensional space, so `c_e = c_1`. The law admits the shift `u → u + const` exactly when constants solve its homogeneous form, `c_0 + 6c_1 = 0`. Then it reads `c_0(u_x − (1/6)Σ_e u_{x+e}) = s_x`, which is `−(c_0/6)` times the lattice Laplacian applied to `u`. ∎

Without the shift symmetry the law `u_x = c_1Σu_{x+e} + s_x` with `6c_1 ≠ 1` is allowed; it has a mass term, and its uniform solution singles out a value of the rate.

## Theorem T2 — every law of the class, at first order; what is not forced

By homogeneity of degree one, `Σ_i w_i ∂F/∂w_i = F`. At the uniform point the six derivatives are equal, because the rotations permute the arguments transitively and leave both `F` and the point unchanged; they sum to `F(1, …, 1) = 1`. So each is `1/6`, and to first order `δu_x = (1/6)Σ_e δu_{x+e}`: the law of T1. ∎

The second order is not forced. With one neighbour at `1 + d` and the opposite one at `1 − d` the power mean of order `p` gives `1 + (p − 1)d²/6 + …`; at `d = 1/10` the arithmetic, harmonic, contraharmonic and pair-ratio laws give `1 + 0`, `1 − 1/298`, `1 + 1/300`, `1 − 1/1500`. The geometric mean is multiplicative, hence exactly linear in `u` at every field strength. The product of the six rates — the form the campaign's rule has for unnormalized weights — is homogeneous of degree six: it is not scale covariant, and on a torus of side 4 its symbol `1 − 2Σcos k_i` runs from `−5` to `7`, where the averaging law's symbol `1 − (1/3)Σcos k_i` is non-negative with a single zero at `k = 0`. The rule of the campaign fixes normalized odds; a law for rates is a separate clause.

## Theorem T3 — the zero mode

On the torus `(Z/L)³` the operator `u_x − (1/6)Σ_e u_{x+e}` annihilates exactly the constants and has rank `L³ − 1`; its range is the set of sources with zero sum. So a source enters only through its part of zero sum, and `u` is determined up to a constant, which no ratio of rates contains. (On the `3×3×3` torus: rank 26; a source that sums to one has no solution; a source that sums to zero has one, and its shifts are solutions.) On the infinite lattice the field of finitely many sources is the sum of their lattice potentials, which vanish at infinity, again up to the constant. ∎

Records all enter with the same sign (T4), so on a closed lattice their uniform part is exactly what the law cannot hold; it is the projection the weak-field packet applies and calls the total or background sector.

## Theorem T4 — records enter as additive sources

A clause that gives a record a fixed rate `w_x = U` is not scale covariant: after `w → tw` it fails. A scale-covariant, rotation-covariant clause for a record has the form `w_x = κF̃(neighbours)` with `F̃` of the class; by T2 its first order is `u_x − (1/6)Σ_e u_{x+e} = log κ`. With the record count `n_x` of block 41 the law is

`u_x − (1/6)Σ_e u_{x+e} = (log κ) n_x`,

linear, so the field of any arrangement of records is exactly the sum of the single fields, whatever the shape or density of the arrangement; the lattice potential is symmetric, so the field of one record at the site of another equals the converse. With `κ < 1` the field is lowest at the record: clocks run slow near records. (On the `4×4×4` torus with `log κ = −3/10`: three records, sum exact; `u = −4551/12800` at a record, mean zero.) ∎

`κ` may depend on the record's content and on its occupied neighbours; block 50's local clock `1/π_x` is such a ratio. That changes the strength of a source by contact terms and not the form of the law.

## Theorem T5 — a test record in the field

Let a record hop to each of its six neighbours at the rate `w_x/6`. The law `m_x ∝ 1/w_x` satisfies `m_x w_x/6 = m_y w_y/6` on every bond, so it is stationary, with detailed balance. The record is found with probability proportional to `exp(−u_x)`: more often where clocks run slow, that is near other records when `κ < 1`. If instead the hop across a bond were timed by the mean of the two rates, the stationary law would be uniform. ∎

This pull acts on the record count with steady masses, adds exactly, has a symmetric pair term and, at long range, the same strength in every direction (refuting pass: the field's slope against `1/r` between `r = 5` and `10` is `−0.1467` along an axis and `−0.1413` along a body diagonal, against `6 log κ/(4π) = −0.1432`; block 51's wind differed by 30 per cent between those directions). It is a drift: the record's mean velocity, not its acceleration, follows the gradient, as in block 48.

*Corrigendum (2026-09-23): the record's mean velocity.* The sentence above is wrong for T5's own timing. A record whose hops are timed by the clock of the site it sits on hops to each empty neighbour at the same rate `w_x/6`, so its expected displacement is zero away from contact: its mean velocity does not follow the gradient. What follows the gradient is the flux of its probability, `(m_x w_x − m_y w_y)/6` across a bond. The record lingers where clocks run slow; it is not carried there, as block 48's bodies are carried by a wind. Where this note calls T5's pull "a drift" (in the result up front, here and under Boundaries), read: where the record is found shifts towards slow clocks through its waiting times, with no mean velocity. Block 95 (#8860) proves this and extends T5 to records that are both sources and movers. Text-only; no theorem, check or number changed.

## The correspondence with the weak-field packet (of form)

| weak-field packet on `main` (supplied) | within the clause |
|---|---|
| operator `H = −Δ_lat`, from a posited quadratic action | forced by nearest-neighbour determination, cubic covariance and scale covariance (T1, T2) |
| source projected off the zero mode, `P₀ρ` | the constant of `u` is the unit of rate, which no ratio contains (T3) |
| source `ρ = |ψ|²` | the record count (block 41), entering as `log κ` per record because an absolute rate would need a master clock (T4) |
| response `S_test = L(1 − φ)` | the ratio of ticks accumulated at two sites is `exp(u_x − u_y) = 1 + (u_x − u_y) + …`: `φ = −u` up to the constant |
| coupling and units | one number, `κ` |

## No-Go Discipline Gate

The note's negative sentences: a law of the class has no mass term; a record cannot pin an absolute rate; the product of the six rates is not a law of the class; the pull of T5 is not an acceleration.

### N1 — Routes by which the sentences could fail
1. *A master clock* — if rates have an absolute meaning, scale covariance goes, `6c_1 ≠ 1` is allowed and the field is screened. The axioms name no clock; a clause that supplies one is possible and is outside this note.
2. *A law that reads further than nearest neighbours* — covariant, shift-symmetric linear laws of finite range have a symbol that vanishes at `k = 0` and is proportional to `|k|²` there; the operator changes at short distance, the long range does not. Not worked beyond this remark.
3. *Records that set a rate relative to something other than their neighbours* — any covariant ratio is of T4's form at first order; a record that reads a distant rate is not a nearest-neighbour clause.
4. *Inertia* — a record whose phase advances with the local clock is a wave in a medium of varying rate and refracts towards slow clocks; whether that gives the acceleration T5 lacks is the next block, not this one.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The whole note is conditional on the clause C1–C3. "Tick rate" is not an object of the axioms; the clause is a candidate filling of the open gate on rates and the time metric, supplied and named as such. T2 assumes differentiability at the uniform point. T4 and T5 on the infinite lattice use the lattice potential of finitely many sources.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice and its rotations; the covariance sentence; the absence of a time metric | yes (premise; the absence motivates C3 and does not prove it) |
| block 01 (`main`) | the campaign's rule, for the remark on its product form | placement |
| block 41 (open PR #8547) | the record count as the source | yes for T4's identification (restated) |
| blocks 45–52, decision record (open PRs #8553–#8564, #8555) | the defects of the capture picture that T4 and T5 are compared with | placement |
| weak-field packet (`main`) | the three supplied pieces the correspondence is drawn with | target, not premise |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "covariant shift-symmetric linear laws are the averaging law; every degree-one covariant rule has it as first order; rank `L³ − 1`; records are sources `log κ`, exactly additive; a test record has the law `1/w`" | executed: the 24 rotations, their orbit, the invariant coefficient vectors; first derivatives of four rational laws by exact dual numbers | executed: ratio law against pinned law under a change of unit; the law `1/w` at 27 sites | executed: symbols of the averaging and product laws on a torus of side 4 | executed: rank 26 and solvability on the `3×3×3` torus; additivity and symmetry for three records on the `4×4×4` torus | T1, T2 for every law of the class; T3, T4 exact on tori and by superposition on the infinite lattice; T5 for one test record; the clause, `κ`, inertia and delay not derived |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not supply the clause: `scale_reference_primitive` is a conversion of units and says nothing about rates varying from site to site; `kinetic_isotropy_primitive` grants only the equality `c_t = c_s` of a kinetic form; `realized_state_primitive` grants evaluation at a supplied state. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You chose the clause to get the answer." Reply: the clause has two parts. The first copies the form of the Admissibility axiom (one covariant rule, nearest neighbours). The second says that a quantity the axioms do not define cannot have an absolute value. What follows is then forced for every rule of the class, not for a chosen one, and the note names what is not forced: the second order, `κ`, inertia, delay. Second objection: "A static law acts at a distance." Reply: yes; the note derives a constraint of the kind the weak-field packet posits and says nothing about how a change of the sources is communicated; block 43's finding that record-layer fields settle by diffusion is about processes, and no process is posited here.

### N8 — Cross-cycle echo
Block 39 found that the rule cannot see the overall scale of its weights; block 42 that the odds of unformed sites obey a lattice field equation that is massless only on a tuned surface; block 49 that a long range needs a field protected by a conservation law or a symmetry, not by tuning; block 50 that keeping the rule's law under streaming sets a record's clock by a ratio. Here the symmetry is the freedom of the unit of rate, and it protects the long range without tuning. One consequence is recorded for block 50: under this note's premise its global clock `1/π(C)`, which multiplies every rate by one factor, is a change of the unobservable unit; what its stationary law means for an observer who can only compare rates is not resolved here.

## Falsifiers

- A linear nearest-neighbour law, covariant under the proper rotations and admitting the shift, other than a multiple of the averaging law; a rule of the class whose first derivatives at the uniform point are not all `1/6`.
- A source of non-zero sum for which the law has a solution on a torus; an arrangement of records whose field is not the sum of single fields.
- A scale-covariant clause that gives a record an absolute rate.
- A test record timed by the local clock whose stationary law is not `1/w`.

## Boundaries and non-claims

The clause is supplied, not derived; the axioms define no tick rate. `κ` is not derived and its sign is not fixed by the clause (`κ > 1` would make clocks run fast near records and the drift of T5 point away). The non-linear completion is not fixed. The law is static: nothing is said about how the field follows a change of its sources. T5 is a drift in the record layer; acceleration is not obtained. The relation between a law for rates and the campaign's rule for normalized odds is not established; the rule's product form is not of the class. The correspondence with the weak-field packet is one of form. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom, the covariance sentence of Admissibility, and the memo's statement that no time metric is defined. Block 01 (on `main`): the rule's product form; proposed, unaudited. Block 41 and the decision record (PRs #8547, #8555, open): restated or placed. The weak-field packet on `main`: the target of the correspondence.
- Named standard imports at definition level: the identity of Euler for homogeneous functions; the rank of the averaging operator on a connected finite graph; superposition for linear equations; detailed balance.
- Reference only: Laplace, Poisson, Green, Fredholm; Einstein (1907, 1911) and Nordström for a potential that is a rate of clocks; Seeliger for uniform sources; Markov.

## Review record
Corrigendum (2026-09-23, supervisor): T5's remark on the record's mean velocity corrected; found while building block 95 (#8860). Text-only; no theorem, check or number changed.

Supervisor-run block, the first after the 12-hour campaign, on the owner's instruction "ok lets work the source link into the amplitude layer". Foundations read first: the axioms memo and the parked-decisions registry were read in full before any framing. Lens pass, in writing, by the supervisor (the campaign's no-subagent rule): a rigour lens (the theorem is short; the content is in the clause — hence the clause is split into the part that copies the Admissibility axiom's form and the part that follows from the absence of a time metric, and what is not forced is listed); a lattice lens (static only, no delay; the symbol and its single zero); a foundations lens ("tick rate" is not an axiom object; pins need an absolute rate, which selected the source form and removed a capacity argument the supervisor had first found attractive); a strategy lens (what the block gives the lane: three supplied pieces reduced to one number and a law of motion, with the amplitude layer's task named). Refuting pass (`specs/supervisor_control_block53_refuter.py`, machinery disjoint from the runner's): W1 symbolic solution of the covariance and shift conditions; W2 the power mean with symbolic order; W3 a sparse solve on a `41³` box: slope of the field against `1/r`, axis against body diagonal; W4 twelve records on a `16³` torus by transform; W5 a simulated test record. All pass. Two findings folded: the first form of W3 compared `u r` with the infinite-lattice value and failed by 30 per cent because walls at distance 20 shift the field near the centre by a nearly constant amount; differences of the field are compared instead. The runner's first geometric-mean check scaled the sixth roots where it meant to scale the rates. Mutation census: 10 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_master_clock_neighbour_determined_scale_covariant_tick_rate_lattice_laplace_equation_additive_sources_2026_09_21.py
```

Expected: `TOTAL: PASS=16 FAIL=0`.

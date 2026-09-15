---
claim_id: admissibility_handed_rule_pseudoscalar_invariant_census_and_parity_odd_record_correlators_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "On the six Bloch-axis alphabet over the nearest-neighbour cross of Z^3, under three readings of the Admissibility covariance clause (unsoldered with proper internal cubic group, unsoldered with full internal cubic group, soldered cubic action), the exact census of covariant nearest-neighbour rule terms that are odd under improper lattice operations: Burnside dimensions, lowest handed degree per reading, the unique degree-two soldered handed term v.A_DM with A_DM = sum_i r_i x q_i, explicit strictly positive rules W_0 and W_X with mirror images W_-X, and the exact parity-odd record correlators these rules leave on the seven-site window under the centre-last, static and order-mixture laws. The separating clauses are recorded as decision points, not adopted."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
  - a_mirror_asymmetric_admissibility_rule_registers_its_own_parity_odd_texture_and_nothing_else_the_emergent_fermions_movers_are_time_reversal_images_with_identical_record_laws_bounded_note_2026-09-05
runner: scripts/admissibility_handed_rule_pseudoscalar_census_2026_09_13.py
---

# Finite six-axis-menu witness rules may be handed under each declared cubic action; the lowest handed term is a lattice curl when soldered and degree five or six when unsoldered, and each handed rule leaves an exact parity-odd trace in record statistics that its mirror image negates

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained
**Audit:** unset; the independent audit lane owns any verdict.
**Primary runner:**
[`scripts/admissibility_handed_rule_pseudoscalar_census_2026_09_13.py`](../scripts/admissibility_handed_rule_pseudoscalar_census_2026_09_13.py)
**Pinned cache:**
[`logs/runner-cache/admissibility_handed_rule_pseudoscalar_census_2026_09_13.txt`](../logs/runner-cache/admissibility_handed_rule_pseudoscalar_census_2026_09_13.txt)
(`TOTAL: PASS=46 FAIL=0`, exact rationals throughout, about 22 s).

## Result up front

The Admissibility axiom asks for one fixed nearest-neighbour rule, covariant
under lattice translations and proper cubic rotations. It does not say whether
the rule may differ from its mirror image. This note studies supplied finite-menu rules inspired by that sentence. It
does not construct a complete axiom/primitive model or a continuous-domain
extension; it records distinctions between the declared finite readings.

1. **Handed rule terms exist in every reading of the covariance clause.** On
   the six-letter axis alphabet (one Bloch axis vector per arm of the
   nearest-neighbour cross), the space of covariant rule terms that change sign
   under every improper cubic operation has dimension 90 when the qubit label
   carries the proper internal cubic subgroup of `SO(3)` and is not tied to the lattice, 43 when the
   internal group is the full cubic subgroup of `O(3)`, and 4540 when the
   label is soldered to the lattice frame (`Cl(3,0)` reading). These are exact
   Burnside counts for finite cubic groups. Canonical direct-orbit crosschecks
   cover the separate slot, internal and soldered arm actions only.

2. **The lowest handed term depends on the reading.** Unsoldered with `SO(3)`:
   no handed term of total degree at most four; the first is `T (v.s)` at
   degree five, with `T = det[d_x, d_y, d_z]`, `d_a = q_{+a} - q_{-a}`, and
   `s` the arm sum. Unsoldered with `O(3)`: odd total degree is excluded by
   the central inversion, and the first handed term is `D4 (v.s)` at degree
   six, `D4` the alternating cubic sum of `(q_{+x}.q_{+y})(q_{-x}.q_{+z})`.
   Soldered: the handed terms of total degree two form a one-dimensional
   space spanned by `v.A_DM`, `A_DM(q) = sum_i r_i x q_i`, the discrete curl of
   the recorded arm field around the centre (a Dzyaloshinskii-Moriya-type
   coupling); no handed term exists at degree one, and none at degree two
   built from `v` alone.

3. **Explicit admissible rules.** `W_0(v|S) = (1 + v.s_S/14)/6` is covariant,
   strictly positive, varies with the neighbour condition, and is mirror-even
   in every reading. `W_X = W_0 + P_X/(6 E_X)` on fully recorded crosses, with
   `P_X = X(q)(v.s)` for `X` in `{T, D4, Omega}`, `P_DM = v.A_DM`, and
   `E_X = 2(max|P_X| + 1)` in `{18, 34, 18, 10}`, is normalised and strictly
   positive on all 279,936 pairs; its mirror image is exactly `W_-X`.

4. **The handed trace in record statistics is exact and reading-graded.** With
   the centre recorded last, `E^{W_X}[P_X]` equals `32/243`, `320/1377`,
   `2/27`, `2/15` for `T, D4, Omega, DM`; under the static (Gibbs) law it equals
   `1387678/10609137`, `94240/408969`, `1778/24057`, `196/1485`. `W_0` gives
   zero for every texture under both laws; `W_-X` gives exactly the negative;
   the even statistic `E[v.s]` is identical for `W_X` and `W_-X`. Any formation
   order in which some arm is unrecorded when the centre forms carries zero
   handed trace, so the uniform order mixture over the seven-site window
   equals one seventh of the centre-last value. `T` and `D4` are each
   orthogonal to every other texture; `Omega` and `DM` overlap (`2/81`, `2/45`).

5. **Which rules are handed is a function of the reading.** `T` is handed only
   in the unsoldered `SO(3)` reading, fails covariance under internal
   conjugation in the `O(3)` reading, and is achiral when soldered. `D4` is
   handed in all three readings. `Omega` and `DM` are covariant only when
   soldered, and handed there.

6. **Witness pairs and the recorded clauses.** In each reading a pair of
   finite-menu rules (`W_0/W_T`, `W_0/W_D4`, `W_0/W_DM`) satisfies the
   declared finite covariance and probability conditions and differs on a
   parity-odd record statistic. These are finite-menu witness pairs only. The minimal separating data are recorded
   here as decision points, not adopted: the qubit symmetry (`SO(3)` versus
   `O(3)`), the frame relation (soldered versus unsoldered), and either a
   parity-fixing clause or a registered handedness of the realized branch.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the Admissibility sentence fixes covariance under proper cubic rotations only; whether the realized rule is mirror-symmetric is not stated, and the axioms do not select a qubit symmetry group or a frame relation between the label and the lattice"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "carry the degree census to the 3x3x3 window and to the continuum Bloch alphabet (readability block); test whether the emergent-fermion parity notes of 2026-09-03 and 2026-09-05 are consistent with a soldered handed rule of lattice-curl type"
conditional_surface_status: "if a clause fixed the qubit symmetry group and the frame relation, the census below gives the handed rule space on the declared finite menu exactly; if in addition a parity-fixing clause were supplied, every handed term would be excluded and the record correlators of this note would vanish identically"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "every statement is scoped to finite computation or the stated symmetry proofs; numerical covariance checks are sampled; the remaining content is an exact finite computation on declared alphabets, groups, windows and rules, or an algebraic corollary of such a computation (Burnside, invariant-tensor completeness up to arm degree three); no continuum limit and no dynamics is claimed"
```

## Premises and declared objects

**Axiom sentences used (quoted from `docs/MINIMAL_AXIOMS_2026-06-29.md` on
`origin/main`).** Lattice: sites are `Z^3` with six nearest neighbours,
standard translations and proper cubic rotations. Qubit: the one-site algebra
is `M_2(C)`; a `Cl(3,0)`-compatible real presentation is equivalent.
Admissibility: "one fixed nearest-neighbor admissibility rule, covariant under
lattice translations and proper cubic rotations. For each site, the
probability distribution over the possibilities is determined by, and varies
with, the nearest-neighbor conditions." Record: a record locks exactly one
admissible local possibility, one per site, permanent; only records are
readable. The `realized_state_primitive` concerns a supplied law-admissible realized
state; this note neither derives such a global state nor verifies a full
primitive model.

**Alphabet.** The six axis Bloch vectors `+x, -x, +y, -y, +z, -z` as the
possibilities at every site (the six-projector menu inside `M_2(C)` used by
the formation-order note and the 2026-09-05 mirror note). The centre's
neighbour condition is the arm configuration `q = (q_{+x}, ..., q_{-z})`, one
letter per arm of the nearest-neighbour cross; there are `6^6 = 46,656` such
configurations and `279,936` pairs `(v, q)` with `v` the centre's letter.

**The cubic group and its three actions.** The 48 signed permutation matrices
`M` form the full cubic group; 24 are proper (`det M = +1`), 24 improper.
Three actions on `(v, q)` are declared. *Slots:* `M` permutes the arms
(`r_i -> M r_i`) and leaves every letter fixed. *Internal:* `M` acts on every
letter (`q_i -> M q_i`, `v -> M v`) and leaves the arms fixed. *Soldered:* both
at once, the label riding with the lattice frame. The following `SO(3)`/`O(3)` labels abbreviate their finite cubic
subgroups throughout all census tables and runner output:

- **unsoldered, internal `SO(3)`:** the lattice group acts by slots; the
  label carries its independent proper cubic subgroup (24 letter rotations);
  a rule term is covariant when it is invariant under proper slot operations
  and under the internal group; it is *handed* when in addition it changes
  sign under every improper slot operation;
- **unsoldered, internal `O(3)`:** as above with the internal group enlarged
  by the antipodal map `q -> -q`, giving 48 letter operations. Complex
  conjugation itself reflects the Bloch y coordinate; together with proper
  rotations it generates a group containing the antipodal map;
- **soldered:** the lattice group acts by the soldered action only; handed
  means invariant under proper and negated under improper soldered elements.

In the two unsoldered readings the internal covariance is imposed under the
cubic subgroup of the internal group (48 or 24 letter operations), not under
the continuous group; the explicit unsoldered witness polynomials use dots and determinants
and have continuous internal invariant formulas. This does not extend an
arbitrary finite rule table to a continuous possibility domain; the Burnside counts in the unsoldered readings are
counts of cubic-invariants and are upper bounds on dimensions of restrictions to this finite alphabet of
continuously invariant functions (not dimensions of continuous-domain function spaces). This is stated as a limitation in the Boundaries section.

**Pseudo-scalar textures.** Four label-dependent functions of the arm
configuration are used throughout: `T(q) = det[d_x, d_y, d_z]` with
`d_a = q_{+a} - q_{-a}` (degree three); `D4(q)`, the sum over the 48 cubic
operations of `det(M)` times the soldered image of `(q_{+x}.q_{+y})(q_{-x}.q_{+z})`
(degree four); `Omega(q) = sum_a (q_{+a} x q_{-a}).e_a` (degree two, soldered
only); and the lattice curl `A_DM(q) = sum_i r_i x q_i` (a vector, degree one).
Their extreme values on the alphabet are `max|T| = 8`, `max|D4| = 8`,
`max|Omega| = 3`, `max ||A_DM||_infinity = max_{q,v}|v.A_DM| = 4`, with `14,832`, `14,592` and `22,016`
configurations on which `T`, `D4`, `Omega` respectively are nonzero.

**Rules.** A rule is a table `W(v|q)` of probabilities over the six letters
at the centre, one row per arm configuration, extended to partially recorded
crosses by the base rule. The base rule is
`W_0(v|S) = (1/6)(1 + v.s_S/14)` with `s_S = sum_{i in S} q_i` over the
recorded arms; at one recorded neighbour with letter `a` it is `(14 + a.v)/84`.
The handed rules add `P_X/(6 E_X)` when all six arms are recorded, with
`P_X = X(q)(v.s)` for `X` in `{T, D4, Omega}`, `P_DM = v.A_DM(q)`, and
`E_X = 2(max|P_X| + 1)`, so `E_T = 18`, `E_D4 = 34`, `E_Omega = 18`,
`E_DM = 10`. All entries are integers over `84 E_X`.

**Laws on the seven-site window.** Three ways of turning a rule into record
statistics on the centre plus its six arms are computed exactly: *centre-last*
(the six arms form first under the empty-background rule `1/6` each, then the
centre under `W`); *static* (the Gibbs law with weight
`n_X(v|q) prod_i (14 + q_i.v)`, the product form of the pairwise base
factors); and the *uniform order mixture* over the seven formation orders
classified by how many arms are recorded when the centre forms.

## Prior art and what is new

**Landed.** The 2026-09-05 note
`a_mirror_asymmetric_admissibility_rule_registers_its_own_parity_odd_texture_and_nothing_else_the_emergent_fermions_movers_are_time_reversal_images_with_identical_record_laws_bounded_note_2026-09-05`
works on ternary label-blind profiles: "The 729 profiles have 57 proper and
56 full cubic orbits: 55 achiral orbits and one chiral pair"; "The explicitly
redeclared label-equivariant class has 24 ternary digits and 3^24 tables, all
mirror-symmetric." Its handedness lives in *which slots are recorded*, not in
the recorded letters; a label-equivariant table there cannot be handed. The
2026-09-03 note
`docs/DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md`
treats parity of a supplied fermion model on the coarse cube ("There are two
kinds of mirror on this lattice"), not of the Admissibility rule.
`docs/CL3_CENTRAL_PSEUDOSCALAR_SCHUR_SEPARATOR_NARROW_THEOREM_NOTE_2026-05-17.md`
identifies the central pseudo-scalar of `Cl(3,0)` as a Schur separator inside
the one-site algebra; it says nothing about the rule between sites.
`docs/FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_PHYSICAL_NARROW_THEOREM_NOTE_2026-06-08.md`
and
`docs/FLAVOR_HANDEDNESS_IS_RK_EVEN_TIME_ARROW_INSUFFICIENT_NARROW_NO_GO_NOTE_2026-06-08.md`
concern flavour-space handedness of a supplied mass texture.
`docs/PHYSICAL_LEVEL_SET_ORBIT_LAW_IMPROPER_CENTER_IDENTITY_CYCLE719_NOTE_2026-08-02.md`
concerns the improper centre of a gravity orbit law. The parked structuralist
reading in `docs/repo/DEFERRED_DECISIONS.md` section 2 ("whether the Qubit
sentence ... carries flip-invariance of *rule dependence* (making every
availability set provably achiral and chirality non-definable)") has standing
default "not adopted, either way"; this note supplies a wake condition for
it, not a resolution.

**New here.** (i) The handedness is carried by the *letters*: label-dependent
pseudo-scalars of the arm configuration, invariant under proper cubic
operations, are exhibited and counted, and they are nonzero on
label-equivariant rules, which is exactly the class the 2026-09-05 note found
mirror-symmetric in the label-blind setting. (ii) The count is done under
three readings of the covariance clause and the answer differs by reading,
so the answer depends on the supplied group action. (iii) The lowest handed
term is identified in each reading, with a completeness argument, and in the
soldered reading it is the lattice curl `v.A_DM`. (iv) The handed trace is
carried through to exact record correlators on the seven-site window under
three laws, including the order-mixture result that any unrecorded arm at the
centre's formation kills the trace. (v) The witness pairs and the separating
clauses are stated in the form the campaign design note requires.

## Exact target and obligation graph

**Target.** Within the declared finite-menu model, can a covariant
nearest-neighbour rule differ from its mirror image, and does that difference
leave a trace under the supplied finite record laws?

**Obligations.** O1: exhibit the pseudo-scalar textures and grade them under
the three actions (S2). O2: count the handed rule terms in each reading and
cross-check the separate arm actions by direct orbits (S3, S4a). O3: identify the lowest handed degree
per reading with a completeness argument (S4b). O4: construct explicit
normalised, strictly positive, condition-dependent rules `W_0` and `W_X`,
verify covariance, grading and the mirror identities (S4c). O5: compute the
parity-odd record correlators exactly under three laws (S5). O6: classify
each texture's handedness against the finite cubic product reading group and exhibit one
witness pair per reading (S6). O1 to O6 combine the runner with the algebraic proofs below. S4b/S4c
covariance uses 400 sampled arm configurations; S6 uses 120. These samples
are checks of the identities, not exhaustive covariance proofs.

**Cross-window rationale.** The seven-site window (centre plus six arms) is
the smallest on which every texture is defined: the open `2x2x2` cube has
no opposite arm pairs, so `T` and `Omega` vanish identically there; the
periodic `2x2x2` cube identifies `+a` with `-a`, so `d_a = 0`. The `3x3x3`
window (`6^27` configurations) exceeds the block budget and is not run; the
seven-site window is exhaustive at `6^6` configurations.

## Theorem 1 (grading and Burnside census)

**Statement.** Under the slot action `T` and `D4` are odd and `Omega` is
mixed; under the internal action `T` is odd, `D4` even, `Omega` mixed; under
the soldered action `T` is even, `D4` odd, `Omega` odd. The dimension of the
span of lattice-odd polynomials on the arm alphabet is `0, 1, 1` at degrees
`2, 3, 4` (unsoldered `SO(3)`, dots and determinants), `0, 0, 1` (unsoldered
`O(3)`, dots only), and `0, 3` at degrees `1, 2` (soldered, with `Omega`
among the degree-two spanners). Counting rule terms as functions on
`(v, q)` invariant under the proper part of the reading group and negated by
its improper part, Burnside's lemma gives

| reading | invariants on `q` | odd on `q` | invariants on `(v,q)` | odd on `(v,q)` | handed rule terms | achiral rule terms |
|---|---|---|---|---|---|---|
| unsoldered `SO(3)` | 98 | 26 | 468 | 116 | 90 | 370 |
| unsoldered `O(3)` | 81 | 13 | 338 | 56 | 43 | 257 |
| soldered | 1138 | 896 | 6276 | 5436 | 4540 | 5138 |

where the handed count is the odd count on `(v, q)` minus the odd count on
`q` alone (terms independent of `v` do not vary the centre's law), and the
achiral count is the difference of the invariant counts.

**Proof.** Exact enumeration: the gradings are checked on all `46,656`
configurations under all 48 elements of each action; the degree spans are
computed by exact rank over the rationals on the orbit representatives (two
dot products, two determinants, nine dot-dot products; two degree-one and
fourteen degree-two soldered monomials); the Burnside counts are sums of
fixed-point counts weighted by the sign character. Direct orbit enumeration
in the canonical runner checks the separate slot, internal and soldered arm
actions, not the unsoldered product actions or centre-plus-arm census. The soldered odd count at degree two (`3`) is
bounded above by the soldered odd Burnside count on `q` (`896`), as it must
be. Runner S2 (seven checks), S3 (nine), S4a (two); all pass. Also verified there: `T` equals one sixth of the alternating slot projection of `det[q_{+x}, q_{+y}, q_{+z}]`; every determinant monomial is odd under the antipodal map, so the `O(3)` reading has no degree-three term; `Omega` is not invariant under proper unsoldered slot rotations.

## Theorem 2 (lowest handed degree per reading, with completeness)

**Statement.** (a) In both unsoldered readings there is no handed rule term of
total degree at most four in `(v, q)`. (b) Unsoldered `SO(3)`: `T(q)(v.s)` is
handed, of total degree five. (c) Unsoldered `O(3)`: every odd total degree
is excluded by the antipodal map, and `D4(q)(v.s)` is handed, of total degree
six. (d) Soldered: there is no handed term of total degree at most one and no
handed term of degree two built from `v` alone; the handed terms of total
degree two form a one-dimensional space spanned by `v.A_DM(q)`, with
`A_DM(q) = sum_i r_i x q_i`; `v.A_DM` is proper-invariant and improper-odd
on the whole window, and sums to zero over `v`.

**Proof of (a), completeness.** A rule term of total degree at most four is
a polynomial in `v` and the six letters, covariant under the internal group
and the proper slot group, of degree at most four in all variables together.
For the proper internal cubic group, its 180-degree rotations force the
counts of each Cartesian component index to have the same parity. Through
rank four, permutation symmetry leaves the rank-two delta, rank-three
epsilon, pairwise products of deltas, and the all-equal-axis rank-four
delta. These are internal component-index tensors, not arm-position tensors.
With at least one centre factor, reduction by the axis-alphabet identities
gives F1, F2, F3, F3' and F4; centre-only terms and terms involving at most
two arm slots vanish by the improper coset-parity sums. The runner constructs every
family these tensors generate at total degree at most four (`F1` to `F4` and
the `E`-component family `F3'`), projects each onto the odd part under the
improper slot operations, and finds every projection zero. (b) and (c) are
direct: `T(v.s)` is nonzero and slot-odd; under `O(3)` the antipodal map acts
as `(-1)^degree`, so odd degrees are not covariant, and `D4(v.s)` is nonzero,
internal-even and slot-odd. (d) The soldered average `sum_M det(M) M^T` over
the 48 signed permutation matrices vanishes, so no degree-one term survives
the odd projection; the coset-parity sums over ordered slot pairs vanish, so
no `v`-only degree-two term survives; the `v`-linear, arm-degree-one
pseudovector projections over the five orbit representatives of `(slot,
component)` pairs have rank one, adding `A_DM` keeps the rank at one, and
`max ||A_DM||_infinity = max_{q,v}|v.A_DM| = 4`; covariance of `A_DM` is verified on 400 configurations
against all 48 soldered elements; the window grading also uses those 400
samples, while the zero centre sum is checked exhaustively. The vector
Euclidean squared norm has maximum 20; the bound 4 is a component/projection
bound, not a Euclidean norm bound. Runner
S4b, six checks.

**Reading.** In the soldered reading the first place a covariant rule can be
handed is a coupling of the centre's letter to the *curl* of the recorded arm
field around it, `v . sum_i r_i x q_i`. This is the lattice form of a
Dzyaloshinskii-Moriya coupling; it is not a scalar of the letters alone, and
it needs the label to ride with the frame. The unsoldered readings push the
first handed term to degree five or six, where it is a product of a letter
pseudo-scalar with the even coupling `v.s`. In every reading the coupling to
`v` is what makes the term a rule term rather than a function of the
neighbours alone; a pseudo-scalar of the arms that does not multiply a
`v`-dependent factor does not vary the centre's law and is not a handed rule.

## Theorem 3 (explicit admissible rules and their mirrors)

**Statement.** `W_0` and the four `W_X` (and the four `W_-X`) are each
normalised over the six letters on all `46,656` arm configurations, strictly
positive on all `279,936` pairs, and vary with the neighbour condition; at
one recorded neighbour with letter `a` the base rule is `(14 + a.v)/84`. `W_0`
is covariant and mirror-even in every reading. The handed part of each `W_X`
has the following (proper-covariant, improper grading) under the slot,
internal and soldered actions: `T`: (cov, odd), (cov, odd), (cov, even);
`D4`: (cov, odd), (cov, even), (cov, odd); `Omega`: (not covariant, mixed),
(not covariant, mixed), (cov, odd); `DM`: (not covariant, mixed), (not
covariant, mixed), (cov, odd). The slot mirror image of `W_T` is `W_-T` and of
`W_D4` is `W_-D4`; the soldered mirror image of `W_D4`, `W_Omega`, `W_DM` is
`W_-X`; the soldered mirror image of `W_T` is `W_T` itself.

**Proof.** Exact integer tables over `84 E_X` exhaustively check
normalisation, positivity, condition dependence and the stated mirror
identities. Covariance/gradings are sampled on 400 configurations and follow
algebraically from the dot, determinant and cross-product transformation laws. Runner S4c, nine checks.

**Why the coupling is needed.** An earlier construction in this block added
`X(q)` to the centre's law without a `v`-dependent factor; that addition has centre sum `6 X(q)` and therefore fails normalisation
when nonzero. It was discarded before landing. The coupling `v.s` (or `v.A_DM`) is the minimal
covariant carrier.

## Theorem 4 (parity-odd record correlators are exact and mirror-negated)

**Statement.** Let a seven-site window be filled under one of three formation
laws built from a rule `W`: *centre-last* (the six arms recorded uniformly,
then the centre drawn from `W(.|arms)`), *static* (the Gibbs law with weight
`n_X(arms, v) prod_i (14 + q_i . v)` over the whole window), and the
*order mixture* (the centre placed at a uniformly random position in the
formation order, with the arms recorded before it as the only condition).
Write `E^W[P_Y]` for the expectation of the pseudo-scalar record statistic
`P_Y` (Section "Premises"). Then, with rows `X` (the rule) and columns `Y`
(the statistic), all exact:

| centre-last `E^{W_X}[P_Y]` | `T` | `D4` | `Omega` | `DM` |
|---|---|---|---|---|
| `W_T` | `32/243` | `0` | `0` | `0` |
| `W_D4` | `0` | `320/1377` | `0` | `0` |
| `W_Omega` | `0` | `0` | `2/27` | `2/81` |
| `W_DM` | `0` | `0` | `2/45` | `2/15` |

Static (Gibbs) diagonal: `T`: `1387678/10609137`; `D4`: `94240/408969`;
`Omega`: `1778/24057`; `DM`: `196/1485`. Further: (i) `W_0` gives zero for
every `Y` under every law; (ii) `W_-X` gives exactly the negative of every
entry; (iii) when the centre is recorded before the full cross (arm subsets
`S` any proper subset of the six arms) every `P_Y` trace vanishes, so the
order-mixture trace equals the centre-last trace divided by seven; (iv) the
even statistic `E[v . s]` is equal for `W_X` and `W_-X`.

**Proof.** Centre-last: `E^{W_X}[P_Y] = 6^{-6} sum_q sum_v W_X(v|q) P_Y(q,v)`.
Since `W_0` is even under every improper element of the relevant reading
group while `P_Y` is odd, the `W_0` part sums to zero, leaving the Gram
identity `E^{W_X}[P_Y] = (1/(6 E_X)) 6^{-6} sum_{q,v} P_X(q,v) P_Y(q,v)`; the
matrix is therefore the Gram matrix of the four handed terms over the window,
scaled by `1/(6 E_X)` row-wise. `T` is orthogonal to the other terms by internal inversion parity.
`D4(v.s)` is internally invariant, while `Omega(v.s)` and `v.A_DM` have
zero internal cubic average (their axial vectors average to zero), proving
the remaining orthogonality. `Omega` and `DM` overlap because both are
soldered-odd and neither slot- nor internal-covariant separately; the ratio of
the two cross entries, `(2/81)/(2/45) = 5/9 = E_DM/E_Omega`, is the ratio of
the row normalisations, as the Gram identity requires. For a proper subset `S` of arms recorded before the centre, the law has
weight proportional to `(14 + v.sum_{i in S}q_i) prod_{i not in S}(14+q_i.v)`.
It is internally cubic invariant. Internal inversion kills `T(v.s)`; averaging
the axial vectors kills `Omega(v.s)` and `v.A_DM`. For `D4(v.s)`, every subset
of the six slots has an improper slot stabilizer: an empty or doubly occupied
axis permits reflection of that axis; if all three axes are singly occupied,
a signed transposition of two axes preserves the selected signs. That
stabilizer preserves the law and negates `D4(v.s)`. Thus all proper subsets
give zero, without assuming an unrecorded arm is uniform. The runner checks
three representatives (empty, one arm, five arms); this symmetry argument
covers every subset. The static diagonal is
a direct `6^7`-term exact sum. The historical author recomputation is described in the Review record; it
is not presented as fresh independent evidence. Runner S5, five checks.

**Reading.** A handed rule does not merely exist; it leaves a *measurable*
parity-odd trace in the record stack, and the mirror-image rule leaves the
negative. Any record statistic even under the mirror is blind to the choice
(`E[v . s]` is equal for `W_X` and `W_-X`), so the handedness is invisible to
scalar-only readouts and visible only to pseudo-scalar ones. The traces
depend on the formation law (centre-last and static differ), so the
clock-and-rate and formation-order blocks of this campaign interact with the
handed census through the *magnitude* but not the *sign* of the trace.

## Theorem 5 (witness pairs and the recorded separating clauses)

**Statement.** Under each full finite cubic product reading group, the
sampled classification (120 configurations) of the four handed terms is:

| reading | `T` | `D4` | `Omega` | `DM` |
|---|---|---|---|---|
| unsoldered `SO(3)` | handed | handed | not covariant | not covariant |
| unsoldered `O(3)` | not covariant (internal-odd) | handed | not covariant | not covariant |
| soldered `Cl(3,0)` | achiral | handed | handed | handed |

Hence the pairs `(W_0, W_T)` (unsoldered `SO(3)`), `(W_0, W_D4)` (unsoldered
`O(3)`) and `(W_0, W_DM)` (soldered) are finite-menu witnesses: two
rules satisfying the declared finite conditions, agreeing on
every mirror-even record statistic, and differing on an exact parity-odd
record statistic.

**Recorded separating clauses (decision points, not adopted).** (1) whether
the internal group of the Qubit sentence is `SO(3)` or `O(3)` (conjugation
included), which decides whether `T` is handed or excluded; (2) whether the
Admissibility covariance clause is read soldered or unsoldered, which decides
whether the lowest handed term is a degree-two lattice curl or a degree-five
or six product; (3) whether the axioms fix the parity of the rule (a
parity-fixing clause) or whether the realized branch registers a handedness
(the `sign(Psi_9)` reading of `DEFERRED_DECISIONS` section 2). Under (3) with
the second alternative, both `W_X` and `W_-X` are admissible rules, and which
one the record stack exhibits is registered, not derived; no full framework-model or continuous-domain existence claim follows
from these finite witnesses. Runner S6,
five checks.

## No-Go Discipline Gate

The negative content of this note is Theorem 2(a) and 2(d): no handed rule
term below the stated degrees. The gate is applied to that content.

- **N1 (alternative routes).** A handed term could enter through (a) a
  letter-only pseudo-scalar without a `v` factor, (b) a `v`-dependent factor of
  higher degree in `v`, (c) a coupling to a second window, or (d) a
  non-polynomial rule. (a) does not vary the centre's law and is not a rule
  term (Section "Theorem 2, Reading"); (b) is covered up to total degree four
  and excluded by the completeness argument; (c) lies outside the one-window
  scope (Boundaries); (d) is covered in so far as every function on the finite
  alphabet is a polynomial of bounded degree, so "degree" here is the total
  degree minimized over all polynomials representing that function on the
  finite axis alphabet. A unique multilinear Cartesian representative is not
  assumed.
- **N2 (wall independence).** The census uses only the finite alphabet, the
  cubic group and its three actions; no landed no-go is load-bearing.
- **N3 (hidden walls).** The one hidden assumption is that internal
  covariance is imposed under the cubic subgroup of the internal group. For the
  full continuous groups the invariant tensor list used in Theorem 2(a) is a
  superset of the continuous one, so the exclusion is stronger, not weaker,
  under the full group; the Burnside counts of Theorem 1 bound dimensions of restrictions to this
  finite alphabet of continuously invariant functions, not the unrestricted
  continuous-domain function spaces.
- **N4 (residual matching).** The residual the census leaves is exactly the
  three recorded clauses of Theorem 5; each is matched to a witness pair.
- **N5 (resolution).** Per element: exact six-letter tables; per site: one
  centre and six arms; per mode: three finite actions with 400 sampled
  S4b/S4c configurations and 120 S6 configurations; per block: exact Burnside
  sums and seven-site correlators; lattice-wide: neither `3x3x3` nor a
  continuous alphabet was executed. Within these bounds, The note claims a lowest degree per reading and the
  existence of handed rules; it does not claim that the framework's rule is or
  is not handed, and it does not claim any reading is the realized one.
- **N6 (partial closure).** If the campaign later fixes the reading (for
  example soldered `Cl(3,0)` through the possibility-covariance block), the
  lowest handed degree is then fixed at two and the lattice-curl form is the
  unique candidate; this is a partial closure path, recorded in the trace.
- **N7 (steelman).** "A parity-fixing clause is already implicit in 'one
  fixed rule': fixing the rule fixes its parity." Answer: the witnesses show
  that fixing *a* rule does fix its parity, but the sentence does not fix
  *which* rule; `W_X` and `W_-X` are both single fixed covariant rules. The
  strongest form of the objection is that "covariant under proper cubic
  rotations" was written with the intent of excluding improper elements, so
  that handedness is permitted by construction; the finite witnesses show that proper covariance alone does not force
  mirror symmetry in this declared menu, without deciding a full axiom model.
- **N8 (cross-cycle echo).** The 2026-09-05 mirror note found one chiral pair
  among 57 orbits of ternary profiles with every label-equivariant table
  mirror-symmetric; the present census recovers the same structure (the
  unsoldered `O(3)` reading, the closest analogue of "label-equivariant", has
  the smallest handed count and no handed term below degree six) and extends
  it to the readings where handed terms appear at low degree.

## Falsifiers

- Any covariant unsoldered rule term of total degree at most four that is odd
  under the improper slot operations (a nonzero projection in the `F1` to
  `F4`, `F3'` families) refutes Theorem 2(a).
- A second linearly independent degree-two soldered handed term (rank two in
  the S4b pseudovector projection) refutes the uniqueness in Theorem 2(d).
- A rule `W_X` whose mirror image is not `W_-X` for the stated reading, or
  whose centre-last trace `E^{W_X}[P_X]` differs from the Gram value, refutes
  Theorem 3 or 4.
- A configuration on which `A_DM` fails soldered covariance, or on which `T` is
  improper-odd in the soldered reading, refutes the classification.

## Boundaries and non-claims

- Alphabet: six axis Bloch vectors only; the continuum alphabet (all unit
  vectors) is the readability block's business. Window: one seven-site cross;
  the `3x3x3` census (`6^27` configurations) was not run.
- Internal covariance is imposed under the cubic subgroup only; Burnside
  counts bound dimensions of restrictions to this finite alphabet of
  `SO(3)`- or `O(3)`-invariant functions, not continuous-domain dimensions.
- The S6 classification is on 120 sampled configurations against the full
  finite cubic product reading group; S4b/S4c gradings use 400 samples.
- No dynamics, clock, formation unit or continuum limit is used or claimed;
  the three formation laws are the same finite devices as in the
  formation-order note.
- No claim about which reading the framework realizes, and no claim that any
  emergent-fermion parity result is affected; the trace names that test.
- The rule constants `E_X` are chosen for positivity, not derived; the trace
  magnitudes depend on them (through `1/(6 E_X)`), the vanishing and
  negation statements do not.

## Imports

None beyond the upstream dependencies in the front matter. The standard-form
cubic invariant tensor completeness is established algebraically in Theorem 2;
the runner verifies the listed finite projections.

## Review record

Historical author report (not the current independent review): single seat (Fable 5.1), no subagents; the campaign design permits low-effort
readers for status comprehension only, and none were used for this block.
Historically reported controls (external scripts are not preserved here): (a) the runner computes every number by exact
enumeration from the definitions; (b) a standalone script, written after the
runner and sharing no code with it, rebuilt the 48 signed permutation
matrices, the four textures and the four rules from the definitions in this
note and reproduced `E_T, E_D4, E_Omega, E_DM = 18, 34, 18, 10` and every
diagonal and `Omega`/`DM` cross entry of the centre-last matrix exactly; (c) a
mutation census: five external source copies of the runner, each with one
substitution, were run (not a runner flag); each failed at least one check.
Substitutions and outcomes: slot mirror of `W_T` asserted equal to `W_T`
(1 failure, S4c mirror identity); the handed traces asserted zero (1 failure,
S5 positive trace); `A_DM` replaced by the plain arm sum `sum_i q_i` (12
failures, S4b uniqueness, grading and covariance); the `SO(3)` reading
enlarged to the full `O(3)` (2 failures, S6 witness pairs and `T`
classification); `W_T` used as the soldered witness (1 failure, S6 witness
pairs). A sixth intended substitution (the slot grading of `T` asserted even)
did not match any source line after a rename and was skipped. All quoted
values outside (b) are regression pins of the runner's own output.

## Verification

```bash
python3 scripts/admissibility_handed_rule_pseudoscalar_census_2026_09_13.py
```

Check families and counts: S1 alphabet and group (3); S2 textures and gradings
(7); S3 orbit representatives, odd spans, coset parity (9); S4a Burnside
census (2); S4b lowest handed degree and completeness (6); S4c explicit rules,
positivity, gradings, mirror identities (9); S5 record correlators (5); S6
classification and witness pairs (5). Total 46, about 22 s, exact rationals
throughout, stdout under 6,000 characters.

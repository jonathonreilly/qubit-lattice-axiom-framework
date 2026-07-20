# Boost-Cone and Antiperiodic-Boundary Sign Routes: Exact Finite Counterchecks and Open Bridges

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`.

**Date:** 2026-06-23
**Claim type:** bounded_theorem
**Type:** partial-narrowing (exact finite route checks; no exhaustive no-go)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. Any `audit_status` and `effective_status` fields
are pipeline-derived.

**Primary runner:**
[`scripts/boost_cone_apbc_sign_neutral_2026_06_23.py`](../scripts/boost_cone_apbc_sign_neutral_2026_06_23.py)
**Cached runner output:**
[`logs/runner-cache/boost_cone_apbc_sign_neutral_2026_06_23.txt`](../logs/runner-cache/boost_cone_apbc_sign_neutral_2026_06_23.txt)

## What this is

Companion to [RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md](RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md),
which showed the checked record-tick channels are signature-neutral and named
one harder candidate route to the Lorentzian sign `eps = e_4^2 = -1`: after
supplying a Lorentzian metric, its standard non-compact boost stabilizer could
be compared with a candidate causal cone, and one might hope to source the
needed bridge from the per-axis `Z_2` **antiperiodic-`tau` boundary datum**
(fermionic APBC on the temporal circle vs PBC on spatial circles). Neither the
Lorentzian metric nor an emergent record-causal cone is established by that
proposal. This note records exact results for the explicitly instantiated boost, base-scalar
boundary, exchange-map, peripheral-phase, and on-site-action checks. It does
not classify the full cone automorphism group, the full cyclic group generated
by the APBC shift, projective/Clifford lifts, matter attachments, or emergent
record dynamics. It does **not** reduce, amend, narrow,
retire, or re-approve any registered primitive or derivation obligation, and
adds no axiom/import. If the lane uses `eps = -1`, that sign remains a separate
explicit conditional input.

## Runner-Checked Facts (`PASS=17 FAIL=0`, memory-trivial)

**(A) The compared stabilizer route is circular.** For the two signatures
explicitly compared by the runner, Euclidean `diag(+,+,+,+)` has `0`
opposite-sign mixing generators, while the target one-time Lorentzian choice
`diag(-,+,+,+)` has `3`. Invoking the latter stabilizer as the source of the
one-time sign already chooses the target signature. No classification of all
indefinite signatures is claimed.

**(B) The selected standard coordinate boost fails on the chosen discrete
reachability polytope.** [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)
supplies only the finite-graph recursion `C_t`; it does not identify that set
with a record-causal, Lieb-Robinson, metric-speed, or physical-spacetime cone.
After separately choosing the nearest-neighbor `Z^3` relation and a tick index,
the cumulative reachability sets have the combinatorial polytope form
`{t >= 0, ||x||_1 <= t}` in edge/tick coordinates. The Hamiltonian-side
bound, when used, belongs to
[AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_NOTE_2026-05-17.md](AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_NOTE_2026-05-17.md).
At the runner's chosen rapidity `eta = 0.7`, the standard `t-x_1` boost sends
an off-plane boundary ray outside the `l1` cone in spatial dimensions `2` and
`3`; it is therefore not an automorphism of that chosen polytope. Signed
spatial axis permutations form one checked finite subgroup. They are not
claimed to exhaust the automorphism group. In particular, positive dilations
`(t,x) -> (lambda t,lambda x)` preserve the cone and form a non-compact
`R_{>0}` subgroup; they are explicitly outside the Lorentz-boost question.
Discrete tick translation is likewise not a linear apex-preserving cone
automorphism. No full or projectivized extreme-ray classification is supplied.

**(C) The instantiated base-scalar checks do not themselves supply the sign
bridge.** The selected `L = 6` wrap operator (`C^L = -I`) has eigenvalues
**exactly on the unit circle**
(`max||lambda|-1| ~ 1e-15`) — a compact `U(1)/Z_2` phase, not an off-circle
boost. The scalar subgroup `{+1,-1}` has **no element squaring to `-1`**. This
does not exhaust the cyclic matrix group `<C>`: for this even-`L` example,
`(C^3)^2 = -I`. Whether a projective/Clifford representation and a faithful
matter attachment can turn that matrix fact into the temporal generator is an
explicitly open bridge. In the checked base-scalar reading, the Lorentzian sign
belongs to a different object, the **Clifford fiber** (the `i` in
`gamma^j = i gamma^E_j`, per
[WICK_ROTATION_COMPACT_SO4_TO_LORENTZIAN_DIRAC_DOUBLING_ORIENTATION_NOTE_2026-06-07.md](WICK_ROTATION_COMPACT_SO4_TO_LORENTZIAN_DIRAC_DOUBLING_ORIENTATION_NOTE_2026-06-07.md)).
The time↔space exchange map `W` is **real-orthogonal** (`W W^T = I`,
`det = +/-1`), so it preserves the Euclidean `(+,+,+,+)` form and transports
APBC across axes carrying **which axis wraps**, never **what signature** — fully
consistent with, and within the axis-supply scope of,
[`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md`](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md)
(axis-supply scope). The particular thermal-trace reinterpretation
`beta` = inverse temperature → `Tr e^{-itH}` presupposes `tau -> it`, the Wick
answer; the distinct projective/attachment routes named above remain open.

**(D) The sampled `SO(2)` matrix is not the sampled `SO(1,1)` boost.** At the
declared angle/rapidity, the first matrix has eigenvalues on the unit circle
and the second has eigenvalues off it. This finite comparison distinguishes
the two displayed matrices. It does not assign a signature to every
peripheral block, exclude coupled/projective representations, or classify all
possible readout maps.

**(E) Independent corroboration.**
[`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
shows the on-site boost is not forced by the local algebra: a
scalar `S(eta) = exp(eta) I_2` is a valid spin-blind action on `C^2`, and the
faithful `K = -i sigma/2` (which closes `so(3,1)`) requires the explicit `i`
plus a matter-attachment selector. The runner reproduces both.

## Consequence and honest boundary

`eps = e_4^2 = -1` remains a separate conditional input on this checked surface
if the lane uses the Lorentzian sign. The tested base-scalar, real-exchange,
sampled-phase, and coordinate-boost instances do not themselves construct the
needed bridge. They do not rule out the full `<C>` representation, a
projective/Clifford lift, a matter selector, a Wick/readout map, or emergent
record dynamics. The conditional input supplies no premise weight. With
[RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md](RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md)
and this note, the checked boundary-datum sub-lane is mapped.

- This is a **partial-narrowing / finite-instance** result. It does not derive
  `eps = -1`, does not close any derivation obligation, and touches no
  primitive.
- The boundary datum is **out of scope** of the axis-supplier no-go on the
  *signature* question — a genuine crack-shaped gap exists there — but the
  instantiated scalar subgroup and real exchange do not fill it (facts C
  above); the full cyclic/projective representation route remains open.
- A remaining firewall-clean opening — the next path this leaves, not a wall —
  is an *emergent* non-compact symmetry of the record-formation
  **dynamics** (a Hermitian, indefinite-form-preserving one-parameter generator
  over `Z^3`, not a Euclidean boundary datum), the open gate named in
  [SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md](SINGLE_CLOCK_ANTIPERIODIC_AXIS_DATUM_S4_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-06-17.md).
  That relocates the question to the record-formation-dynamics lane and is
  owner-framing-gated; it is orthogonal to the static cone, the boundary datum,
  and the peripheral-phase machinery checked here.
- No new axioms / imports / comparators; signature-agnostic inputs only.

## No-Go Discipline Gate — partial-narrowing applied

The former broad no-go does not survive the hostile review. The only negative
claim shipped here is the finite-instance statement that the explicitly tested
objects do not, by themselves, construct the Lorentz-sign bridge. The full
generated-group, projective/Clifford, matter-selector, Wick/readout, cone-
classification, and record-dynamics routes remain open.

### N1 — alternative-route enumeration

1. **ATTEMPTED — compared diagonal stabilizers.** The runner compares the
   Euclidean and one-time Lorentzian diagonal forms; using the latter's
   non-compact stabilizer already chooses its sign (A). This closes only that
   circular proposal, not all indefinite-form mechanisms.
2. **ATTEMPTED — standard coordinate boost on the chosen `l1` polytope.** The
   explicit `eta=0.7`, `t-x_1` matrix sends an off-plane extreme ray outside
   the cone in dimensions `2` and `3` (B). Positive dilations and a full
   projectivized automorphism classification are not identified with this
   boost and remain outside the claim.
3. **ATTEMPTED — base scalar APBC subgroup.** Direct enumeration of
   `{+1,-1}` finds no scalar square root of `-1` (C). The full matrix group
   `<C>` is not collapsed to that subgroup; indeed `(C^3)^2=-I` at `L=6`, so
   its representation/attachment route remains open.
4. **ATTEMPTED — real exchange map.** The displayed `W` is exactly
   real-orthogonal and transports an axis label without changing the Euclidean
   form (C). Projective or Clifford-valued exchange maps are not tested.
5. **ATTEMPTED — sampled peripheral versus boost matrices.** At the declared
   sample, the `SO(2)` eigenvalues lie on the unit circle while the `SO(1,1)`
   eigenvalues lie off it (D). Coupled blocks and arbitrary readout maps remain
   open.
6. **ATTEMPTED — on-site Pauli action.** The scalar action is spin-blind, while
   the faithful displayed `K=-i sigma/2` explicitly consumes `i` and a matter
   attachment (E), matching
   [the boost-faith note](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md).

These routes differ in primary object: metric stabilizer, cone matrix action,
scalar holonomy, exchange map, peripheral spectrum, and on-site matter action.

### N2 — wall-independence audit

| raw pair | implication / collapse |
|---|---|
| one-time metric sign / its non-compact stabilizer | co-specified on the compared diagonal target; invoking that stabilizer presupposes the sign, so this is one circular route rather than two walls |
| Clifford `i` / faithful matter selector | coupled representation-and-attachment bridge; not counted as independent closures |
| chosen static polytope / record-formation dynamics | independent; the static counterexample does not constrain an emergent dynamical generator |

No multi-wall impossibility is claimed after this collapse. The remaining
items are explicit open routes, not a count of independent no-go walls.

### N3 — hidden-condition scan

The runner choices are explicit: coordinate boost, rapidity `0.7`, spatial
dimensions `1`–`3`, `L=6`, scalar subgroup `{+1,-1}`, one real exchange map,
one peripheral angle, positive spatial signs, and one Pauli realization. Cone
automorphisms are not normalized or classified. “By construction” refers only
to these declared matrices and carries no retained authority.

### N4 — residual-matching table

| cited surface | cited residual | current residual | use |
|---|---|---|---|
| `LATTICE_NN_LIGHT_CONE_NOTE.md` | finite-graph support recursion | chosen `l1` coordinate polytope | context only; not proof of a metric cone |
| `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_NOTE_2026-05-17.md` | Hamiltonian Lieb-Robinson bound | combinatorial boost counterexample | non-matching context; dropped as no-go evidence |
| `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md` | axis supply | signature/representation bridge | non-matching context; explicitly does not close signature |
| `QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md` | local algebra does not force faithful boost action | displayed on-site action needs `i` plus attachment | matching corroboration for route E only |

### N5 — rhetoric and resolution audit

The checks are per displayed matrix, per selected cone ray, per scalar subgroup,
and per sampled block. They do not cover every group power, mode, projective
representation, coupled matter block, boost direction, cone automorphism, or
lattice-wide record dynamics. The prose is restricted to the tested
resolutions and names every broader resolution as open.

### N6 — partial-closure paths

No new-axiom requirement is asserted. A full `<C>` representation, a
projective/Clifford lift with matter attachment, a Wick/readout rule, or an
emergent record-dynamics generator could supply a bridge. Existing registered
primitives do not automatically settle those mappings.

### N7 — hostile steelman

The strongest objection defeats the former broad no-go: the APBC translation
operator already has complex spectral structure, and in the runner's even
`L=6` example `(C^3)^2=-I`. A projective spin/Clifford lift coupled through a
faithful matter selector might map that datum to a temporal complex structure
without the base scalar subgroup containing `i`. The terminal obligation is
to prove or disprove such a framework-native representation-and-attachment
bridge without importing the target Lorentzian sign. This note does not close
that obligation, which is why it ships only the finite counterchecks.

### N8 — cross-cycle echo

| prior surface | retirement/splitting mechanism | application here |
|---|---|---|
| [minimum-time campaign](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md) | separated combinatorial support from physical clock/metric identification | separates the chosen `l1` counterexample from a record-causal cone claim |
| [boost-faith lane](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md) | separated local algebra from faithful matter attachment | leaves the Clifford/matter selector open instead of calling the base datum exhaustive |
| [APBC axis-supplier lane](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md) | confined its result to axis supply | keeps signature and representation outside that prior no-go |

**Disposition:** `PASS` for the partial-narrowed finite-instance exclusions;
the former exhaustive no-go is withdrawn and its concrete broader routes are
open.

## Reproduce

```
python3 scripts/boost_cone_apbc_sign_neutral_2026_06_23.py
# expect: TOTAL: PASS=17 FAIL=0   (memory-trivial, single process)
```

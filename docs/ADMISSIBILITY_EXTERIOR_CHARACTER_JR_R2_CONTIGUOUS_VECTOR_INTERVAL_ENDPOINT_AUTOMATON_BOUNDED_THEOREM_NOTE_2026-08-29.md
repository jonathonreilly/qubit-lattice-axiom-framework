---
claim_id: admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_bounded_theorem_note_2026-08-29
final_path: docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_CONTIGUOUS_VECTOR_INTERVAL_ENDPOINT_AUTOMATON_BOUNDED_THEOREM_NOTE_2026-08-29.md
claim_type: bounded_theorem
claim_scope: "For the supplied retain-every-two physical Haar isometry on the actual original-link O(3) ladder, classify the complete distinct-state quadratic response on the orthonormal coarse family consisting of the vacuum and one contiguous merged defining-vector Wilson loop. Prove for every finite q that an offdiagonal entry can be nonzero only when one interval is obtained from the other by adding or removing one endpoint cell; derive the exact vacuum-singleton and occupied endpoint-extension weights; and encode all q^2 unordered candidate edges with a q-independent six-state weighted automaton. This does not classify diagonal histories, prove the interval span invariant, include product-loop or multirun words, give the full vector kernel, select the action, or identify physical time, continuum, Lorentz, gravity, metric/source, or matter currents."
depends_on:
  - admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29
  - admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28
  - minimal_axioms
dependency_roles:
  admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29: "reviewed exact occupied-background endpoint coefficient, global 1/9 Haar factor, physical Q, and t_V^8 dressing"
  admissibility_exterior_character_jr_temporal_spatial_semigroup_defect_generated_interaction_bounded_theorem_note_2026-08-28: "supplied finite action, temporal multipliers, original-link ladder, physical J_2/Q, and vacuum-singleton coefficient"
  minimal_axioms: "framework boundary only; no axiom or approved primitive is edited"
runner: scripts/admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_2026_08_29.py
independent_checker: scripts/admissibility_exterior_character_jr_r2_contiguous_vector_interval_endpoint_automaton_independent_2026_08_29.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: null
trace_class: direct_blocker_closure
target_claim_id: admissibility_exterior_character_jr_r2_nested_merged_vector_interval_response_bounded_theorem_note_2026-08-29
target_blocker_text: "Use the exact t_V^8 interval dressing to seek a fixed-memory multicell vector automaton, then test non-merged product-vector backgrounds where additional V tensor V channels occur."
source_of_blocker_text: next_trace_action
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Resolve the minimal adjacent product-vector background into the scalar, axial-vector, and spin-two shared-rung channels; do not claim that this offdiagonal interval automaton is a closed transfer operator."
conditional_surface_status: "exact finite-memory offdiagonal endpoint-extension law on the supplied r=2 contiguous merged-vector interval family"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the arbitrary-q support selector, q^2 interval graph, exact parent-normalized endpoint weights, and constant-memory recognizer are finite mathematical results on a fully disclosed supplied carrier"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Contiguous-vector interval endpoint automaton at `r=2`

**Date:** 2026-08-29

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — author-side proposal label only.  The actual
current surface is `conditional-support`; independent audit and closure of the
stacked dependencies remain required.

## Result and boundary

On an open ladder with `q` retained cells, let `Omega=1` and

```text
Phi_[a,b]=chi_V(delta_b ... delta_a),   0<=a<=b<q.  (1)
```

For the selected vector part of
`R_epsilon=(1/2)partial_lambda^2 D_epsilon(0)`, two distinct states in
this family couple only when one interval is obtained from the other by adding
or removing one endpoint cell.  If `I` is the shorter interval, `ell=|I|`, and
`c` is the added cell, then

```text
<Phi_I,R_epsilon Phi_(I union {c})>
 =a_(2c)a_(2c+1) * {
    beta_0,                    ell=0,
    beta_1 (t_V^8)^(ell-1),   ell>=1,               (2)
  }

beta_0=epsilon^2(c_V^(n))^2/6
       (1+t_V^4)(t_V^4+t_V^6),                      (3)

beta_1=epsilon^2(c_V^(n))^2/36
       t_V^14(1+4t_V^2+t_V^4+2t_V^6).              (4)
```

The matrix is symmetric.  There are exactly `q^2` unordered candidate edges,
and a six-state weighted recognizer evaluates every one with memory independent
of `q`.

This is the complete distinct-state offdiagonal block on the displayed
orthonormal family.  It is not a proof that the interval span is invariant:
diagonal histories and product-loop backgrounds allow the scalar,
axial-vector, and spin-two pieces of `V tensor V`.  It is not the full vector
kernel or a physical interpretation.  No axiom or approved primitive changes.

## Authorities and imported inputs

| Input | Role here | Not proved here |
|---|---|---|
| [Block 234 nested merged-vector interval theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_NESTED_MERGED_VECTOR_INTERVAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md) | supplies the exact occupied-background local entry, including the `1/9` Haar factor, `Q`, and temporal exponents | the arbitrary-interval selection graph and automaton |
| [Block 232 temporal--spatial compression-defect theorem](ADMISSIBILITY_EXTERIOR_CHARACTER_JR_TEMPORAL_SPATIAL_SEMIGROUP_DEFECT_GENERATED_INTERACTION_BOUNDED_THEOREM_NOTE_2026-08-28.md) | supplies the action, temporal crossing, ladder, `C J_2=J_2 C_c`, `[C,Q]=0`, and vacuum-singleton entry | action selection, physical time, or continuum interpretation |
| [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | fixes the framework boundary | any new axiom or primitive |

## Orthonormal interval family

Each state (1) is a residual-gauge-invariant coarse Wilson-loop character and
has norm one by character orthogonality.  Two distinct intervals differ at an
endpoint.  On at least one exclusive upper or lower rail, one original-link
state therefore carries `V=(1,-)` while the other is trivial.  Linkwise
Peter--Weyl orthogonality gives

```text
<Phi_I,Phi_J>=delta_(I,J),    Phi_emptyset=Omega.   (5)
```

Thus (2) consists of actual matrix entries in an orthonormal subspace, not a
nonorthogonal word dictionary.

## Complete original-link selector

Write the fine plaquette boundary as

```text
P_p={u_p,v_p,h_p,h_(p+1)},      0<=p<2q.           (6)
```

Encode a coarse interval `I` by the repeated fine parity word `iota_2(I)`,
which has bits `2c,2c+1` set exactly when `c in I`.  Do not assume the action
insertions are vectors.  For an arbitrary `O(3)` action irrep `rho`, let
`eta(rho)=1` for negative inversion parity and `0` for positive parity.
Parity matching of insertions `(p,rho)` and `(k,sigma)` first requires

```text
iota_2(I) xor eta(rho)e_p
 =iota_2(J) xor eta(sigma)e_k.                    (7a)
```

For distinct `I,J`, both `eta=0` would force `I=J`, while exactly one
`eta=1` would equate a repeated-bit word to one fine bit.  Both cases are
impossible.  Hence both action irreps have negative parity, and (7a) reduces
to

```text
iota_2(I triangle J)=e_p xor e_k.                 (7b)
```

The left side of (7b) repeats every changed coarse bit twice.  The right side
has exactly two distinct fine bits.  Therefore (7b) holds exactly when
`I triangle J={c}` and `{p,k}={2c,2c+1}`.  For two intervals this singleton
difference is necessarily an endpoint extension or shrink.  Consequently the
only ordered placements are

```text
(p,k)=(2c,2c+1), (2c+1,2c).                       (8)
```

Shifted intervals, nested length jumps greater than one, and any pair differing
in two or more cells have no quadratic entry in this selected vector block.
This is an arbitrary-`q` proof; the runners also exhaust every interval pair
through `q=7` on the actual `6q+1` original links.

The parity census is only the necessary first step.  On the fine plaquette
belonging to the shorter-interval side, an exclusive upper or lower rail
presents `rho` against the longer interval's background `V`; Peter--Weyl
orthogonality forces `rho=V`.  On the opposite fine plaquette, the shorter
side is trivial while the longer side carries `V tensor sigma`; its scalar
channel exists exactly when `|1-ell_sigma|=0` and `(-1)p_sigma=+1`, hence
only when `sigma=V=(1,-)`.  Thus no action irrep was assumed in deriving the
support selector.  The primary runner exhausts both parity choices before
this irrep step and separately enumerates the parent's explicit `n=1` menu
`V`, `det tensor V`, and `det`; only `(V,V)` survives.  The arbitrary-ell
argument uses no sampled irrep cutoff.

## Local physical entry

For `ell=0`, equations (7a)--(8) are the reviewed one-cell
vacuum-to-vector calculation.  Its normalized global Haar overlap is `1/3`
and its exact weight is (3).

For `ell>=1`, translate the changed endpoint cell to zero and reflect the open
ladder if the common interval lies to its left.  The actual original-link
incidence is then precisely Block 234 with span `s=ell`.  Its four first-order
histories have zero conditional mean at fixed `delta_c`, so they lie in
`ker Q`; `C J_2=J_2 C_c` and `[C,Q]=0` preserve this after temporal crossing.
The two matched orientations each have global Haar overlap `1/9`.  Substituting
`s=ell` in that exact result gives

```text
epsilon^2(c_V^(n))^2 a_(2c)a_(2c+1)/36
 t_V^(8ell+6)(1+4t_V^2+t_V^4+2t_V^6)

=a_(2c)a_(2c+1) beta_1(t_V^8)^(ell-1),            (9)
```

which proves (2).  Reflection merely exchanges the two matched orientations,
so left and right endpoint extensions agree after reflecting their local
amplitudes.

At `t_V->1`, all nonvacuum endpoint extensions have coefficient
`2 epsilon^2(c_V^(n))^2 a_(2c)a_(2c+1)/9`; the vacuum edge retains the distinct
one-cell coefficient.  At `t_V=0` every displayed entry is zero.  Positivity
requires positive amplitude product and positive supplied crossing; signed
amplitudes give the corresponding matrix-entry sign.

## Exact edge count

There are `q` vacuum--singleton edges.  Among nonempty intervals, extending
the right endpoint contributes

```text
sum_(length=1)^(q-1) (q-length)=q(q-1)/2
```

edges, and left extension contributes the same number.  Hence the total is

```text
q+q(q-1)=q^2.                                      (10)
```

## Constant-memory weighted automaton

Order each candidate pair as shorter word `y` and longer word `z`, and scan
the cell alphabet

```text
00=(0,0),       U=(0,1),       11=(1,1).           (11)
```

The live states are `B` (before support), `U` (unique cell seen before a
common run), `C0` (common run before the unique cell), `C1` (common run after
the unique cell), and `D` (accepted/done), plus a rejecting dead state.  The
nonzero transitions are

| From | Symbol / weight | To |
|---|---|---|
| `B` | `00 / 1` | `B` |
| `B` | `U / A_c` | `U` |
| `B` | `11 / beta_1` | `C0` |
| `U` | `11 / beta_1` | `C1` |
| `U` | `00` or end `/ beta_0` | `D` |
| `C0` | `11 / t_V^8` | `C0` |
| `C0` | `U / A_c` | `D` |
| `C1` | `11 / t_V^8` | `C1` |
| `C1` | `00` or end `/ 1` | `D` |
| `D` | `00 / 1` | `D` |

Here `A_c=a_(2c)a_(2c+1)`.  Every omitted transition goes to the dead state.
The accepted words are exactly

```text
00* U 00*,       00* U 11+ 00*,       00* 11+ U 00*. (12)
```

They receive respectively `A_c beta_0` and
`A_c beta_1(t_V^8)^(ell-1)`.  The independent runner implements (11)--(12) as
exact symbolic `6x6` transition matrices rather than the primary
state-machine path.

## What remains open

- diagonal interval histories and whether `R_epsilon` preserves the interval span;
- product-loop and multirun vector words, whose shared rungs carry all three
  channels in `V tensor V=(0,+) direct-sum (1,+) direct-sum (2,+)`;
- a fixed-memory representation of the full vector response kernel;
- `r>2` multicell vector words and other exterior irreps;
- selected action, physical time, refinement/continuum, Lorentzian, gravity,
  metric/source, or matter-current identification.

The exact recognizer is valuable because it replaces an `O(q^4)` table of
possible interval pairs by a fixed-memory rule.  It does not turn a selected
offdiagonal coordinate into a closed physical transfer operator.

## No-Go Discipline Gate

This is a positive conditional theorem.  Vanishing entries are proved only for
distinct states inside the explicitly displayed interval family.

### N1 — live alternative routes

| Route | Attempt this cycle | Outcome and authority | Marker |
|---|---|---|---|
| diagonal interval block | Insert both histories against the same occupied loop. | Doubled edges can retain all `V tensor V` channels; no diagonal closure is imported. | `ATTEMPTED` |
| product-loop words | Replace one merged character by a product of neighboring coarse characters. | The shared retained rung needs scalar, axial-vector, and spin-two multipliers; this is the immediate next calculation. | `ATTEMPTED` |
| multirun merged words | Allow two disjoint intervals. | The repeated-bit selector still constrains changed cells, but recoupling between runs is not classified. | `ATTEMPTED` |
| arbitrary `r` | Repeat endpoint extension for wider retained blocks. | Block233 supplies the one-cell width law, not the multicell background recoupling. | `ATTEMPTED` |
| full vector kernel | Add arbitrary coarse spin networks. | No complete state alphabet or invariant subspace is yet proved. | `ATTEMPTED` |
| physical geometry/source reading | Interpret `t_V^8` as distance or a propagator. | No retained map identifies this selected perimeter dressing with physical distance, gravity, or a source response. | `ATTEMPTED` |

### N2 — independence and collapse

The proof collapses if the repeated-bit identity (7), the distinct `1/3` versus
`1/9` recouplings, or the parent `Q` identities fail.  The independent runner
rebuilds the selector with integer masks and the automaton with symbolic
matrices; it does not import the primary support sets or state transitions.

### N3 — scanned authority

The scan is restricted to the two declared parent theorems, their runners,
the current minimal axioms, and the current controlled vocabulary.  Generic
finite automata and compact-group orthogonality are prior art, not novelty.

### N4 — named residual

The hard residual is closure beyond distinct single-interval states.  In
particular, diagonal and product backgrounds can carry nontrivial shared-edge
fusion channels that the six-state language recognizer does not encode.

### N5 — coverage certificate

| Scale | Checked | Not checked |
|---|---|---|
| `per_element` | every original-link incidence and arbitrary-ell exclusive-rail selector | arbitrary spin-network insertions |
| `per_site` | every interval endpoint and both open boundaries | diagonal local recoupling |
| `per_mode` | all distinct pairs in the vacuum-plus-one-interval family | product-loop, multirun, and other-irrep bases |
| `per_block` | `r=2`, every finite `q`, exact q-independent recognizer | `r>2` multicell closure |
| `lattice_wide` | arbitrary-q interval language | norm, thermodynamic, continuum, or physical locality statement |

### N6 — mutation and falsifier ledger

The runner corrupts interval incidence, admits a two-cell difference, admits a
mixed-parity action pair, conflates
the vacuum recoupling, changes the `t_V^8` ratio, breaks reflection, changes a
temporal exponent, accepts a second unique cell, invents a nonvector irrep,
drops orthogonality, and claims diagonal closure.  Each mutation must fail
exactly one check.  Shifted intervals `[0]<->[1]`, `[0,1]<->[1,2]`, and
`Omega<->[0,1]` are explicit zero controls.

### N7 — hostile steelman

The strongest positive extension is that the shared-rung fusion alphabet may
remain finite, allowing a larger automaton for product words.  The current
theorem supports testing that route but cannot prove it because its interval
states never place `V tensor V` on a shared rung as an independent temporal
channel.

### N8 — cross-cycle echo

Block233 replaced fixed-width enumeration with a three-state arbitrary-`r`
transfer, and Block234 supplied the first occupied multicell datum.  This note
uses the same constructive lesson: exact incidence plus a small boundary state
can remove volume-growing enumeration.  The determinant four-state automaton
is design precedent only; none of its Boolean recoupling is imported as vector
physics.

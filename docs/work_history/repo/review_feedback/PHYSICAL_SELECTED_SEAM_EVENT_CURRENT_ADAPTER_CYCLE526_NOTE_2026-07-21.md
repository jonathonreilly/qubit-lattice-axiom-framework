# Physical selected-seam event/current adapter — Cycle 526 (2026-07-21)

Authority: none
Audit: unset
Constitutional effect: none

Runner:
`scripts/physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py`

## Result

Cycle 526 constructs the first bounded direct bridge from the actual Cycle-522
selected physical two-cell FSWAP seam to the Cycle-504 one-hot `K` carrier.
It does not equate a compiler schedule, `K` transition, or update opportunity
with physical time.

On the complete two-cell all-Fock code, let `a` be the pre-seam occupation of
the left boundary mode and `b` the pre-seam occupation of the right boundary
mode.  The physical FSWAP gives post-seam boundary occupations `(b,a)`.  The
adapter derives

```text
EDGE_PASSED = a XOR b,
J_plus      = a AND NOT b,
J_minus     = NOT a AND b,
J           = J_plus - J_minus,
delta N_left  = -J,
delta N_right =  J,
delta N_left = -delta N_right.
```

`EDGE_PASSED` is a coherent event-ready carrier.  It is **not occurrence**,
not a physical close, not a commit, not a Record, not an interval, not a
rate, and not time.  The signed occupation current is a local number-flow
ledger.  It is not energy, stress, a source, gravity, or backreaction.

The selected code is first augmented by two persistent endpoint occupation
shadows:

```text
E'|ell> = E|ell> tensor |a(ell),b(ell)>.
```

Cycle-523's local ANF prepares/constrains these values **before** the two cell
representatives are multiplied and reduced.  The physical seam is

```text
(A_E(FSWAP) tensor SWAP_shadow) E' = E' FSWAP.
```

The dense native block retains the fermionic sign; the ordinary shadow SWAP
updates only the two occupation labels.  The runtime work sequence then uses
two blank M2, `P` and `w`:

```text
P <- shadow_left(pre)
w <- P
apply selected A_E(FSWAP) and ordinary SWAP_shadow
w ^= shadow_left(post)            # w = actual boundary change
EDGE_PASSED ^= w
J_plus  ^= w AND P
J_minus ^= w AND NOT P
advance the physical one-hot K word under control w
w ^= shadow_left(post)
w ^= P
P ^= shadow_right(post)           # shadow_right(post)=shadow_left(pre)
```

Both work carriers finish blank.  The retained outputs are `EDGE_PASSED`,
the two signed-current rails, and the advanced one-hot `K` carrier.  The
complete relation is coherent and reversible; it does not measure or select
a branch.

The Cycle-219 coin changes endpoint occupations coherently, so a coin acting
only on the old native factor would violate the persistent-shadow constraint.
Cycle 526 therefore tests the full supplied order with the explicit augmented
code-space completions

```text
A_E'(C) = E' C E'^dagger + I - E'E'^dagger,
A_E'(T) = E' T E'^dagger + I - E'E'^dagger,
G_data  = A_E'(T) (A_E(FSWAP) tensor SWAP_shadow) A_E'(C).
```

These dense augmented coin/contact blocks are supplied algebraic operators,
not new primitive recurrent M2 laws.  Direct tests show that the coin updates
the shadows consistently, the actual native-plus-shadow seam transports them,
and contact preserves the terminal augmented code.

On the declared augmented code,

```text
E_aug G_coarse = G_physical E_aug.
```

This is a factorized code-image proof, not a claim that one giant physical
matrix was materialized.  The runner proves the `E'` coin, actual
native-plus-shadow FSWAP, and `E'` contact factors separately and in their
composed order; it then exhausts all 65,536 blank-output data-by-`K` adapter
columns and constructs the 524,288-column reversible logical extension over
arbitrary retained event/current bits.

For the full supplied free-plus-contact order, `G_coarse` means the Cycle-219
coin, this event-augmented FSWAP seam, and the Cycle-230 contact in their
retained order.  The actual event/current output is computed around the FSWAP,
not around a host label.

## Three decoder levels and the selected repair

Cycle 523 proved the single-cell selected-native-shell formula

```text
q_d = c_d XOR i_d XOR (c_d AND f)
      XOR (c_bar AND i_d) XOR (c_bar AND f)
```

on all 160 valid local selected patterns.  Cycle 526 separates three levels:

1. **Single-cell term ANF.**  This remains exact before joint multiplication.
   Applying the same formula naively to the combined two-cell reducer word is
   falsified: it gives 18,528 failures among 51,200 endpoint/nonzero-row tests
   at both L5 and held L=6.
2. **Diagonal joint-ray readout.**  The selected `E` has 25,088 occupied rows
   and 25,600 nonzeros.  Exactly 512 rows are reused.  Every reused row
   conflicts for the left `d=0` and right `d=1` seam occupations, with 1,024
   supported entries on each conflict set.  The other ten cell/direction bits
   have zero conflicts.  The unsigned XOR is constant on the reused rows, but
   signed current is not.  Thus a diagonal seam-occupation/current readout
   does not exist on the reduced shell.  The exact boundary-pair histogram is
   6,144 singleton rows of each of `00`, `01`, `10`, and `11`, plus 256 reused
   `00/11` rows and 256 reused `01/10` rows.  Thus each individual endpoint
   bit conflicts on 512 rows, unsigned `EDGE_PASSED` survives on every row,
   and signed direction conflicts on exactly the 256 `01/10` rows.
3. **Dense code-space observable.**  `E n_d E^dagger` and its coherent
   off-code completion always exist and are tested as a bounded algebraic
   fallback.  They are not primitive local decoders and are not used by the
   runtime adapter.

The constructive repair retains the local ANF values as two persistent
shadows in `E'`.  Those two bits split all 512 conflicting rows: the augmented
encoding has 25,600 occupied rows for 25,600 nonzeros and no row reuse.  After
the native dense FSWAP and ordinary shadow SWAP, the local constraints hold on
the output code and `P,w` erase exactly.

The result remains algebraic because shadow preparation/routing and the dense
selected native stream are supplied.  Cycle-523 nearest-neighbor routing from
the native roles to the persistent shadows is not synthesized, and Cycle-522's
dense selected completion is not decomposed into a primitive recurrent M2
law.

## Physical clock transition and local constraints

The `K` word is the actual 16-M2 one-hot carrier from Cycle 504.  Its fifteen
descending adjacent controlled swaps are applied with `w` as their common
control.  Exhaustively,

```text
K_k -> K_(k+EDGE_PASSED mod 16),  k=0,...,15.
```

This includes the physical `K15 -> K0` transition.  Deleting the first
controlled Fredkin changes lawful one-hot columns.

The finite seam carries local bounded constraints:

- a 16-M2 one-hot `K` code constraint;
- blank-input and blank-terminal constraints for the two work M2;
- a two-M2 exclusion of `J_plus=J_minus=1`; and
- a three-M2 consistency check
  `EDGE_PASSED=J_plus XOR J_minus`.

All are constant-size around one tested seam.  This is not a claim of
arbitrary-volume fresh history-carrier genesis.

## Exact domains, covariance, and resources

The data domain is the complete 4096-dimensional two-cell Fock space,
including every number sector `n=0,...,12`.  The auxiliary input domain uses
one lawful one-hot `K` state and blank event, current, and work carriers.  The
runner additionally builds the full 524,288-dimensional reversible extension
over arbitrary event/current bits and all one-hot `K` positions.

At L5 and held L=6 it regenerates the Cycle-522 selected encoder:

- 4096 logical columns;
- 25,088 physical reduced rays;
- 25,600 nonzero amplitudes;
- 83 inherited M2 in the selected seam patch; and
- 23 new adapter M2, for a bounded total of 106 M2.

The 23 new M2 are two persistent endpoint shadows, two work carriers, one
retained `EDGE_PASSED`, two retained signed-current rails, and the 16-M2
one-hot `K` word.  The resolved runtime after the shadows are prepared uses
seven work/event CNOTs, one ordinary shadow SWAP, two current Toffolis, and
fifteen controlled Fredkins: 297 bare one-/two-M2 calls after the supplied
Toffoli decomposition.  Preparing the two persistent shadows has a separate
94-call algebraic upper bound before routing.  Both counts exclude the
still-supplied dense native stream and unresolved native-to-shadow routing.
The largest supplied dense completion acts on the 83 native seam M2 plus the
two shadows (85 M2); the largest resolved adapter gate has support three M2
before the supplied Toffoli decomposition and two M2 afterward.

`EDGE_PASSED` and `K` are proper-cubic scalars.  Under an endpoint-preserving
frame the current rails are unchanged; under endpoint reversal
`J_plus <-> J_minus` and the two persistent shadows exchange endpoint roles.
The runner checks all 24 proper-cubic frames on every logical Fock label,
twelve preserving and twelve reversing the endpoint role, including the
shadow constraints, plus all 93,312 inherited endpoint-action group products.

## Mass and contact boundary

The Cycle-219/Cycle-522 mass parameter remains `0.4534056541748851`, the
supplied contact retains its 4,047 nontrivial columns, and the full augmented
coin-native-plus-shadow-FSWAP-contact physical intertwiner is rechecked at L5
and held L=6.  On the `E'` data code itself, the uniform one-particle ray is an
actual eigenfixture of this full supplied update, with residual below the
declared tolerance and the same extracted mass.

Appending retained `EDGE_PASSED`, current, and `K` outputs generally entangles
that ray; the larger history-output adapter is not claimed to define a new
mass eigenstate.  Calling that entangled output a new history-unitary mass
eigenstate would overstate the result.

## Deletion, leakage, inverse, and lawful-domain controls

- The runner now executes every displayed XOR/AND/clock/cleanup operation on
  all 65,536 blank-output data-by-`K` columns for the full seam and three
  deletion variants; none of the following counts is a hard-coded outcome.
- Deleting native FSWAP while retaining shadow SWAP falsely emits and advances
  `EDGE_PASSED/K` on 32,768 unequal-occupation columns.  It has 32,768
  gate-faithfulness and continuity failures and 32,768 terminal native/shadow
  constraint failures.  Both work bits nevertheless clear; claiming work
  leakage for this half-deletion would be false.
- Deleting shadow SWAP while retaining native FSWAP suppresses the event/K
  transition on those same 32,768 moving columns.  It has 32,768
  gate-faithfulness, continuity, terminal-constraint, and terminal-`P`
  failures, while `w` clears.
- Deleting both halves produces no event and preserves the native/shadow
  equality, but the displayed cleanup still leaves `P` dirty on all 32,768
  unequal-occupation columns.  The native-only and shadow-only maximum basis
  residuals are respectively `2` and `sqrt(2)` from the full sequence.
- Deleting the event copy or either current rail gives a moving-basis residual
  `sqrt(2)`.
- Deleting the first controlled K Fredkin changes lawful clock columns.
- Deleting any of the five ANF monomials gives respectively
  `48,48,8,16,8` failures on each single-cell direction's 160 valid
  preparation patterns at both L5 and held L=6.
- Deleting contact has operator residual greater than one.
- The full augmented adapter is a signed permutation; its inverse is its
  adjoint.
- Zero-hot/two-hot `K`, malformed occupation labels, invalid axes, and
  nonblank work inputs are rejected or outside the declared code.

The half-deletion failures are exposed rather than repaired by host control.
Undefined inputs are not coerced to a no-event result.

## Supplied structure and novelty boundary

Supplied:

1. Cycle 522's selected representative grammar, 83-M2 seam encoder, cell and
   edge roles, dense `A_E(S)`, off-code identity completion, preparation, and
   full coin/contact coefficients at commit
   `ff3f5973c76f2faffecfdcf70ce607a49d6fff43`; Cycle 526's full-order test
   additionally supplies the dense augmented `A_E'(C)` and `A_E'(T)`
   completions;
2. Cycle 523's exact single-cell on-pattern ANF decoder and bare Toffoli
   decomposition at commit `1343f635a9624679141128fd857330bb792f2b68`;
3. Cycle 504's 16-M2 one-hot `K` word and fifteen controlled swaps;
4. blank work/output carriers, finite boundary, noiseless gates, and the
   declared factor order; and
5. Cycle 235/315 proper-cubic frame and endpoint-role actions.

Cycle 525 commit `b17202a622ad46f9b3f19c125124be7d86464cff` is pinned as
the current shared-cell recurrence comparator but is not imported into this
one-seam construction.

The runner enforces strict SHA-256 equality, before accepting the certificate,
for every directly imported load-bearing predecessor:

| predecessor | runner SHA-256 |
|---|---|
| Cycle 219 | `ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a` |
| Cycle 235 | `dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34` |
| Cycle 269 | `c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35` |
| Cycle 315 | `52c18f96a1f8db9b79e4d0fba5ff76905170e6a8dc8c3e818fdf69984a1778c3` |
| Cycle 522 | `d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b` |
| Cycle 523 | `d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d` |

Commit ancestry and semantic-fragment checks remain supplementary; neither
can substitute for these byte-exact gates.  Cycle 525 remains an
ancestor-pinned comparator only and is explicitly not imported.

New in Cycle 526:

1. the two-shadow augmented code that splits all 512 seam-bit row conflicts;
2. the coherent pre/post boundary-change calculation around the actual
   selected physical seam;
3. the persistent-shadow cleanup under the native-plus-shadow seam;
4. the retained signed current and exact continuity ledger;
5. direct event-controlled advancement of the physical Cycle-504 `K` word;
   and
6. the augmented-code intertwiner, covariance, deletion, and all-Fock tests.

No global Jordan–Wigner ordering, nonlocal parity service, preferred axis,
measurement, host event callback, or host-selected clock transition is used.

## Exact result summary

The final fresh certificate completed in `121.52763400005642` seconds with
maximum resident memory `1445117952` bytes, zero process swap, and summary
`PASS=11 FAIL=0`.  The complete reversible logical-adapter SHA-256 is
`26aaedf19d426961fac0444b8ea1f365ce86774b9201d5e9036af93a19663b0c`.
The L5 and held-L6 augmented `E'` encodings have the same canonical SHA-256,
`3a03c4ecbf514b2413d672aceea98bd2808cc75073a538db756b65afb52985aa`.

At both sizes every thresholded operator residual for the augmented coin,
native-plus-shadow seam, stream-after-coin, full contact-stream-coin update,
terminal code leakage, terminal Gram matrix, and inverse roundtrip is exactly
zero.  Representative unthresholded maxima are `3.608226296050023e-16` for
coin intertwining, `4.44130712525147e-16` after seam-on-coin,
`6.246931686687982e-16` for the full update, and
`2.38700219543983e-15` for the inverse roundtrip.  The augmented uniform
one-particle eigenfixture residual is `4.071343396803175e-16`, and its mass is
`0.45340565417488515`.  Deleting coin or contact gives operator residuals
`1.9989857246018434` and `1.9911502010803097`, respectively.

## No-go-discipline N1–N8

The current `origin/main` no-go-discipline skill and proof-search governance
were read after a freshness fetch.  Cycle 526 makes no broad event, compiler,
time, source, or gravity impossibility claim.  N1–N8 constrain only the named
residual boundaries.

### N1 — normalized alternative routes

| normalized family | honesty | disposition |
|---|---|---|
| persistent endpoint shadows prepared before joint reduction and transported with the dense native seam | **ATTEMPTED** | succeeds on the bounded complete-Fock seam and splits all 512 row conflicts |
| retain complete pre and post occupation snapshots, compare, then erase both | **ATTEMPTED** | algebraically succeeds but uses more work M2 than the `P,w` route |
| pre-seam occupation parity alone as an event tag | **ATTEMPTED** | fails the Cycle-255 gate-faithfulness deletion because it survives omission of FSWAP |
| actual pre/post left-occupation XOR | **ATTEMPTED** | succeeds on the terminal constrained native-plus-shadow seam; deleting both halves suppresses the event but leaves `P` dirty, while either half-deletion violates the native/shadow constraint |
| two-rail signed current from pre/post occupation | **ATTEMPTED** | succeeds with exact local continuity |
| naive Cycle-523 single-cell ANF applied after joint reduction | **ATTEMPTED** | fails 18,528/51,200 endpoint row tests; only pre-reduction shadow preparation is retained |
| dense coherent `E n E^dagger` decoder | **ATTEMPTED** | succeeds algebraically but remains a supplied dense block, so it is a fallback rather than the selected route |
| Cycle-523 private direct-occupation shadows | **ATTEMPTED** | value interface is explicit, but its direct outer-edge stream has the separate norm-2 sign residual; no stream success is imported here |
| Cycle-504 host-cadence comparator | **RULED OUT BY PRIOR** | Cycle 504's exact comparator lacks the physical `EDGE_PASSED` receipt required here |

Still live and not used to support a negative are a primitive routed native
decoder, a primitive selected-stream law, a persistent link/Majorana carrier,
fresh recurrent event banks, and a formation/Record law.

### N2 — wall-independence audit

The collapsed open set is:

- `W_primitive`: nearest-neighbor decoder routing and primitive selected
  stream plus augmented coin/contact synthesis;
- `W_recur`: fresh-output genesis and compatible shared-cell recurrence;
- `W_form`: occurrence, physical close, actualization, and Record formation;
- `W_clock`: relational interval matching and metric/rate calibration; and
- `W_source`: identify a lawful energy/stress source and response law.

| wall A | wall B | A closes B? | B closes A? | independent? |
|---|---|---:|---:|---:|
| W_primitive | W_recur | no | no | yes |
| W_primitive | W_form | no | no | yes |
| W_primitive | W_clock | no | no | yes |
| W_primitive | W_source | no | no | yes |
| W_recur | W_form | no | no | yes |
| W_recur | W_clock | no | no | yes |
| W_recur | W_source | no | no | yes |
| W_form | W_clock | no | no | yes |
| W_form | W_source | no | no | yes |
| W_clock | W_source | no | no | yes |

Primitive routing does not create fresh history cells, actualize an event,
calibrate a clock, or identify a source.  Conversely, supplying any downstream
map does not decompose the dense seam or route the decoder.

### N3 — hidden-condition scan

The selected grammar, reference/Wilson sector, dense stream/coin/contact
coefficients, decoder
completion off valid patterns, factor order, blank carriers, one-hot `K`,
initialization, finite boundary, output freshness, coupling, coin parameter,
and frame role are explicit supplied inputs.  “Actual” means pre/post
occupation change under the displayed FSWAP on the code; it does not mean
actualized history.  “Physical” means carriers are assigned bounded M2 sites;
it does not mean the dense blocks have primitive genesis.

### N4 — residual matching

| witness | witness residual | Cycle-526 use | match? |
|---|---|---|---:|
| Cycle 522 | complete selected two-cell Fock `E`, dense FSWAP/full-update lift, edge role | same selected physical seam and code | yes |
| Cycle 523 | exact single-cell selected-pattern occupation value decoder; routing/dynamics still open | same ANF before joint reduction; naive post-reduction use is separately falsified | yes for preparation values; no for diagonal joint readout |
| Cycle 243 | event-ready support is upstream of occurrence/commit/Record/time | types `EDGE_PASSED` only | yes |
| Cycle 255 | fixed pre-event tag survives FSWAP deletion and is not a faithful close | pre-only comparator is rejected; actual XOR replaces it | yes |
| Cycle 504 | physical `EDGE_PASSED` advances one-hot `K`; `K` count is not time | same 16-M2 word and controlled-swap transition | yes |

The Cycle-523 direct-stream sign residual is not evidence against the selected
Cycle-522 seam; it is only an alternate-route boundary.

### N5 — rhetoric/resolution audit

| phrase | tested resolution | untested resolution |
|---|---|---|
| “single-cell decoder is exact” | all 160 selected local patterns, both sizes, all frames | naive joint-ray use is false; invalid patterns and routed noisy hardware remain open |
| “event is actual change” | one selected two-cell FSWAP seam, all 4096 Fock labels | occurrence, actualization, Records, recurrent lattice history |
| “current is conserved” | signed boundary occupation ledger per basis column and coherently by linearity | energy-momentum, stress, source, gravity, continuum current density |
| “K advances physically” | explicit 16-M2 one-hot controlled-swap circuit | elapsed duration, clock calibration, rate, proper time |
| “local/bounded” | one 106-M2 finite seam patch | nearest-neighbor routing depth and arbitrary recurrent volume |

Every negative phrase is restricted to its typed boundary.  No per-seam
result is promoted to a lattice-wide impossibility.

### N6 — partial-closure paths

Cycle 526 is an import-retirement step: the previously abstract event input is
now derived from the selected physical seam without an axiom edit.  Live next
paths are to route the native decoder, decompose the selected dense stream,
synthesize the augmented coin/contact completions, feed fresh local event
receipts from a reversible conveyor, and separately
supply an occurrence/close/Record law.  A later stress/source law may consume
the signed ledger, but naming it “source” would not derive that law.

### N7 — hostile steelman

A hostile reviewer should say that this is still an algebraic composition of
supplied interfaces: Cycle 522 installs a dense selected-shell FSWAP, and the
two persistent shadows are prepared from Cycle 523's local decoder before
joint reduction without a nearest-neighbor route.  Their addition repairs the
512 row conflicts but changes the declared code content rather than deriving
a diagonal readout from the old reduced shell.  The two fresh work bits, three
retained outputs, and 16-bit `K` word are prepared blank, and a new bank is
needed for recurrent history.  The full-order consistency test also supplies
dense augmented coin/contact completions; their primitive synthesis and a
constraint-preserving intermediate path remain open.  The actionable
challenge is a fully routed
primitive shadow preparation plus native seam whose intermediate states
preserve the constraints, followed by two adjacent seams sharing a cell and a
recyclable/fresh event conveyor.  This blocks promotion to a primitive
recurrent event law; it does not undo the exact bounded augmented intertwiner.

### N8 — cross-cycle echo

Cycle 243 separated event-ready support from occurrence, commit, Record, and
time.  Cycle 255 attached a fixed Record-DAG tag to an actual FSWAP but exposed
its failure under gate deletion.  Cycle 504 made `EDGE_PASSED` the physical
input to a one-hot `K` transition while leaving that event input supplied.
Cycle 522 then supplied the lawful selected full-Fock physical seam, and Cycle
523 supplied its exact occupation-value decoder while retaining a dynamic
interface gap.  Cycle 526 closes the near/far-side value-to-event-to-K seam on
one bounded edge by transformed-output cleanup.  The history shows successive
constructive retirement, not a shared obstruction or axiom pressure.

Gate disposition: **PASS** for the bounded algebraic selected-seam event and
current adapter.  **FAIL / DO NOT SHIP** for a primitive recurrent compiler,
occurrence/Record law, physical-time claim, source/gravity identification,
shared obstruction, minimum-content theorem, or axiom pressure.

## Dependency ledger

| wall | Cycle-526 movement | remaining obligation |
|---|---|---|
| `C_ref` | event identity is derived from pre/post local occupation rather than a host label | selected law/reference and blank-output preparation remain supplied |
| `C_num` | complete two-cell all-Fock occupation change and signed continuity are exact | recurrent multi-edge/full-volume number flow |
| `C_wrap` | physical `K15 -> K0` transition is included | interval matching, finite-bank renewal, and physical-time interpretation |
| `C_int` | actual selected FSWAP now drives coherent event/current outputs while the augmented coin/contact code image remains exact | primitive dense stream/augmented coin/contact synthesis and recurrent shared-cell process |
| `C_local` | bounded 106-M2 augmented seam, local constraints, L5/L6, all-frame covariance | persistent-shadow preparation routing and size-uniform recurrence |
| `C_source` | signed local occupation flow is retained as a later interface | energy/stress identification and source/response/gravity law remain open |

There is no shared obstruction and no axiom pressure.

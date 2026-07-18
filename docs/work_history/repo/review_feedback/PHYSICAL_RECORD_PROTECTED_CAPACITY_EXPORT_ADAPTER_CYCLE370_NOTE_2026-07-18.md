# Physical Record-to-protected-capacity export adapter — Cycle 370

Date: 2026-07-18

Authority: none

Audit: unset

Constitutional effect: none. This cycle changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface. It
does not draft axiom language or select the Cycle-364 hypothesis.

Companion runner:

```text
scripts/physical_record_protected_capacity_export_adapter_cycle370_2026_07_18.py
```

## Result up front

There is an exact bounded common-state adapter from an already formed
conditional Cycle-364 site/content Record plus its simultaneous Cycle-368
member/link metadata into the Cycle-335 protected append/export mechanics.
Unlike Cycle 335's abstract register layouts, the new adapter has a connected
nearest-neighbor physical M2 embedding.

The source bank is immutable at every primitive gate boundary. A reversible
nearest-neighbor basis-copy circuit uses a dedicated blank bus corridor to
stage a separate protected carrier replica in a supplied blank incoming
carrier. Every source lane is a CNOT control only; no primitive targets or
swaps a source lane. The bus is uncomputed to blank before the declared
endpoint. The replica then enters, crosses every protected slot, and reaches
the export boundary with exact site, 30-M2 content, predecessor, member, and
reciprocal-link identity. The source Record is unchanged. The carrier replica
is not called a Record.

On the endpoint code space, the exact diagrams are

```text
D E = identity

E G_ingress_common = G_ingress_physical E
E G_append_common  = G_append_physical E
E G_export_common  = G_export_physical E
E G_refresh_common = G_refresh_physical E

G_physical^{-1} G_physical E = E.
```

`G_refresh` is one exchange with a separately supplied external blank. It
relocates a blank and has net blank creation `0`. It is a boundary refresh,
not renewal. A second refresh is rejected after that external carrier becomes
occupied. Indefinite autonomous renewal is not built; that is explicit
law/implementation incompleteness, not an obstruction.

The runner is green at trained `(L=3,N=6)` and `(L=3,N=12)`, held
`(L=6,N=18)`, and all 24 proper-cubic frames. Every primitive physical gate
has support `2 M2` on adjacent sites. No shared obstruction, no-go,
minimum-content result, or axiom pressure is claimed.

## 1. Exact common-state contract

The common state is

```text
CapacityCommonState(
  source         = one fixture-lawful Cycle-368 LinkedFormationState,
  ordered_sites  = one explicit linear embedding,
  external       = one supplied boundary-refresh carrier,
  exported       = one export-boundary carrier,
  slots          = L protected carriers,
  incoming       = one ingress carrier,
)
```

The `source` field is built by the conditional Cycle-368 reference adapter. Every
source site therefore has:

- one conditional Cycle-364 `SiteContentRecord`;
- one Cycle-368 member bit equal to `1`; and
- for each non-root linear predecessor, two reciprocal link bits equal to
  `1` and bound to the exact predecessor/member sites.

Every occupied movable carrier must equal one source-bank envelope exactly.
The adapter rejects site/content/link splicing. Duplicating an already formed
basis value into a blank carrier is a reversible copy operation. It does not
form another Record and does not alter the immutable source object.

Ingress is declared only on computational-basis Record/metadata codewords and
an all-zero target carrier. The CNOT schedule is not asserted to clone an
unknown or arbitrary quantum state. There is no arbitrary-state
quantum-cloning claim.

Cycle 364 remains an unselected falsifiable downstream hypothesis. This cycle
does not compile Cycle-364 formation or Cycle-368 link genesis into physical
gates; it begins after their conditional common state exists.

## 2. Physical carrier and embedding

Each source or movable carrier occupies exactly `79 M2`:

| field | M2 |
|---|---:|
| protected occupancy repetition word `000/111` | 3 |
| signed source-site coordinate, 7 bits per axis | 21 |
| complete Cycle-342 content word | 30 |
| predecessor-present bit | 1 |
| signed predecessor coordinate, or all-zero root field | 21 |
| member plus two reciprocal-link bits | 3 |
| **total** | **79** |

The signed coordinate codec is explicitly bounded to `[-64,63]^3`; it is
supplied adapter structure, not a full-lattice completion. The tested
Cycle-368 chains through `N=18` and their proper-cubic transforms fit this
domain.

The physical patch has three connected parts:

```text
fixed source bank:     source[N][79] at z=1
blank ingress bus:     bus[N][79] at z=0
movable capacity tape: incoming -- slot[L-1] -- ... -- slot[0]
                       -- export -- external
```

The bus has one blank M2 per source/lane pair. The full patch contains
`(2N+L+3)*79 M2`, hence `3555 M2` in the held `L=6,N=18` case. The overhead is
constant: `79 M2` for each source carrier plus `79 M2` for its bus column, and
`79 M2` for each movable carrier. All sites form one connected nearest-
neighbor patch. Rotating the patch by any of the 24 proper-cubic frames
preserves adjacency.

Ingress is a remote CNOT from each source-bank lane to the corresponding blank
incoming lane. It first computes the source basis bit down that lane's blank
bus by nearest-neighbor CNOTs, copies the last bus bit into the blank incoming
target, and reverses the bus CNOTs. The fixed source lane is never a target;
the bus returns all zero. Append and export are exact carrier permutations
decomposed into adjacent block swaps; each block swap is itself decomposed
into elementary adjacent M2 SWAPs. Intermediate movable-carrier microstates
need not be endpoint carrier codewords, but every primitive remains binary,
every source Record lane remains unchanged, and every declared update returns
the bus and movable carriers exactly to their endpoint code spaces.

The source bank and tape layout are included in `E`; no scaffold payload is
used. `D` reconstructs the source `LinkedFormationState`, ordered sites, and
all movable carriers from the physical bits and rejects malformed occupancy,
payload, predecessor, or metadata fields.

## 3. Enter, traverse, and export

For each of `L=3` and held `L=6`, the runner begins with a blank movable patch,
stages the last already formed source Record as one carrier replica, and
applies the Cycle-335 export permutation `L+1` times.

| control | `L=3,N=6` | held `L=6,N=18` |
|---|---:|---:|
| steps from incoming to exported | 4 | 7 |
| occupied movable carriers at every step | 1 | 1 |
| site/content/member/link residual | 0 | 0 |
| source Record residual | 0 | 0 |
| full inverse residual | 0 | 0 |

At the occupancy projection,

```text
P G_export_common = G_Cycle335 P
```

for every trajectory step. This uses the same Cycle-335 nearest-neighbor swap
permutation on a partial-occupancy sector. It does not infer a time observable
from the number of steps.

## 4. Finite append, exhaustion, and external refresh

The finite append route consumes one blank carrier when ingress copies one
source value. The following append is only a swap between that occupied
incoming carrier and a blank protected slot, so it does not change the blank
count. After `L` such writes, the protected window is full.

The first additional replica can be staged, but append to an occupied slot is
rejected. The already supplied blank export boundary then permits the
Cycle-335 moving-export permutation. That operation exports the oldest
replica, installs the incoming replica, and relocates the export blank to the
incoming carrier. It does not renew capacity.

One separately supplied blank `external` carrier can next swap with the
occupied export carrier. This moves the blank back to the export boundary and
moves the exported replica into the external carrier. Net blank count is
unchanged. After one more ingress and export, both `external` and `exported`
are occupied; another refresh is rejected unless another external blank is
supplied.

The exact movable-resource ledger is:

| boundary state | occupied, `L=3` | blank, `L=3` | occupied, held `L=6` | blank, held `L=6` | net blank-count change |
|---|---:|---:|---:|---:|---:|
| initial supplied patch | 0 | 6 | 0 | 9 | 0 |
| finite window full | 3 | 3 | 6 | 3 | 0 |
| first over-capacity replica staged | 4 | 2 | 7 | 2 | `-1` blank consumed by copy |
| moving export complete | 4 | 2 | 7 | 2 | 0 |
| supplied external blank exchanged | 4 | 2 | 7 | 2 | 0 |
| next replica staged | 5 | 1 | 8 | 1 | `-1` blank consumed by copy |
| next export complete | 5 | 1 | 8 | 1 | 0 |

The source bank remains at `N=6` or `N=18` immutable Records throughout and
is accounted separately from movable replicas. Every row satisfies

```text
occupied movable carriers + blank movable carriers = L + 3.
```

Thus neither export nor external refresh creates capacity. The only decreases
in blank count are exactly the supplied targets consumed by reversible copy.
No autonomous capacity-renewal law, environmental sink, erasure law,
thermodynamic resource, or indefinite external sector is constructed.

## 5. Frames, held size, faults, and inverse controls

| control | exact result |
|---|---:|
| `(L,N,frame)` cases | 72 |
| trained cases | `(3,6)`, `(3,12)` |
| held cases | 24 copies of `(6,18)` |
| proper-cubic frames | 24 |
| `D E` residual | 0 |
| `E G_common = G_physical E` residual | 0 |
| physical inverse residual | 0 |
| source/code leakage residual | 0 |
| connected-NN failures | 0 |
| primitive gate boundaries audited | `6,268,176` |
| source-lane value mutations | 0 |
| primitive gates targeting/swapping source lanes | 0 |
| bus cross-lane or endpoint leakage | 0 |
| maximum primitive support | `2 M2` |
| ingress occupancy-CNOT deletion survivors | 0 |
| internal bus-CNOT deletion survivors | 0 |
| export carrier-swap deletion survivors | `0/4` |
| append carrier-swap deletion survivors | `0/5` |
| protected single-replica fault survivors | 0 |
| malformed-domain acceptances | `0/10` |

The ten domain attacks include metadata splice, staging into occupied ingress,
append to an occupied slot, export overwrite, refresh without an occupied
export, improper frame, malformed bit/coordinate lengths, coordinate overflow,
and ordered-embedding splice. A source-identity splice remains visible even
when both source values are lawful.

Deletion counts are counts of required carrier-level permutation steps. Each
such step is fully decomposed into nearest-neighbor M2 gates. The ingress
deletion removes a physical occupancy-lane CNOT and is rejected by the `111`
repetition constraint. Deleting one internal bus CNOT leaves one bus M2
nonzero and is rejected; the nominal bus has zero source mutations, zero
source-target gates, exact target content, and a blank endpoint.

## 6. Supplied structure and semantic firewall

The positive result supplies rather than derives:

1. the unselected Cycle-364 formation hypothesis and its fixture;
2. the Cycle-368 simultaneous member/link metadata and explicit linear site
   embedding;
3. the 7-bit signed coordinate codec and finite `L/N` bounds;
4. the connected source-bank/blank-bus/capacity layout and fixed
   ingress/append/export/refresh gate schedules;
5. the append phase, export boundary, proper-cubic frame, and source-bank
   index selected for copying;
6. one initial export blank, one external boundary-refresh blank, and every
   blank carrier consumed by ingress; and
7. every external sector beyond the one declared refresh as absent from this
   implementation.

Semantic boundaries:

- only the Cycle-364 source object is a conditional framework Record;
- a reversible copy, protected pointer, moved carrier, or exported packet is
  not another Record;
- ingress copies only declared computational-basis fields into a blank M2
  carrier and makes no arbitrary-state quantum-cloning claim;
- the realized-state reference supplies no content, member, carrier, phase,
  blank, or export choice;
- no recurrence, physical layer, gate count, append phase, or export count is
  time, interval, rate, or proper time;
- no carrier phase or wrapped quantity is physical energy;
- no blank count is promoted to energy, stress, active source, or gravity;
- no occurrence, member selector, history sampler, measure, probability, Born
  weight, or empirical frequency is introduced;
- external refresh is not autonomous renewal; and
- authority remains none and audit remains unset.

## 7. Canonical law-completeness and dependency ledger

Cycle 370 conditionally advances the `RECORD` continuation and `RESOURCE`
interfaces in the canonical law-completeness contract. It gives an exact
finite physical continuation that preserves identity/content while a separate
carrier traverses protected capacity. It does not select `ATOMIC_LAW`, prove
Cycle-364 formation physical, establish indefinite continuation, complete the
full-lattice domain, or fill `ACTUALITY` or `STATISTICS`.

| wall | Cycle-370 movement | still open |
|---|---|---|
| `C_ref` | unchanged; conditional formed source identity is preserved exactly through the adapter | actual law selection and state-dependent realized content |
| `C_num` | unchanged | coefficient selection and numerical grade |
| `C_wrap` | exact finite append/export/refresh ledger; no copy is mislabeled a Record | autonomous renewal, permanence beyond the conditional source law, named clock/interval/rate |
| `C_int` | unchanged | no interaction occurrence is derived |
| `C_local` | connected-NN M2 circuit-level embedding with primitive-boundary source preservation and blank-bus uncomputation; all frames, held size, deletion, inverse, leakage | framework-law compiler for formation/link genesis, arbitrary/full-lattice completion |
| `C_source` | exact blank bookkeeping only | thermodynamic resource, energy/stress source, lapse, or gravity response |

The result narrows a concrete implementation gap: after conditional formation,
Record identity and Cycle-368 metadata are compatible with a bounded physical
capacity/export substrate. The remaining autonomous renewal gap is law and
implementation incompleteness. It is not route-independent evidence and
creates no axiom pressure.

## 8. Prior-art and novelty boundary

Reversible CNOT copying of computational-basis data, repetition codes,
adjacent-SWAP routing, shift registers, append buffers, and exported boundary
registers are standard mechanisms. No global novelty priority is claimed for
them.

The repository-specific retained result is their exact typed composition with
the actual Cycle-364 site/content object, Cycle-368 member/link metadata, and
Cycle-335 capacity mechanics, together with one common-state encoder/decoder,
proper-cubic physical embedding, exact blank ledger, held-size controls, and
semantic separation between Record and replica.

Thirring machinery is neither used nor compared.

## 9. Optimal next campaign and verification

The optimal resource-side continuation is to replace the supplied one-carrier
external refresh with an explicit finite environment/export sector and a
declared autonomous law, then test whether reusable blank capacity can recur
without undoing exported history or hiding erasure. That campaign must keep
thermodynamic resource, source response, and time observables separately
typed. A failure to build it would remain implementation evidence unless
multiple constructive routes and the full N1-N8 discipline support a broader
statement.

Run from the repository root:

```text
python3 -m py_compile \
  scripts/physical_record_protected_capacity_export_adapter_cycle370_2026_07_18.py

python3 \
  scripts/physical_record_protected_capacity_export_adapter_cycle370_2026_07_18.py
```

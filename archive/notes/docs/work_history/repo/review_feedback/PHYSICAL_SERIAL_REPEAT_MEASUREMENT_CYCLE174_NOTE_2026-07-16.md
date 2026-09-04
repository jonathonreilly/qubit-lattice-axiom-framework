# Physical serial repeat measurement — Cycle 174

**Outcome:** partial exact interface result.

**Runner:**
[`scripts/physical_serial_repeat_measurement_cycle174_2026_07_16.py`](../../../../scripts/physical_serial_repeat_measurement_cycle174_2026_07_16.py)

## Result

Cycle 174 has one positive result and one bounded compiler obstruction.

The positive result is the **positive 96-row two-witness ingress**:

> If the two opposite neighbors of an open site carry the same signed-row
> role and the other four faces are open, the site writes that row role.

This is one generic relational schema instantiated over the existing 32
signed-row roles. Proper-cubic closure gives 96 raw rows, three opposite-axis
presentations per row. Those rows are disjoint from the Cycle-169 unified
101,708-row law, merge to 101,804 rows with zero deterministic conflict, and
add no onsite role.

The bounded obstruction is the **stock P two-port/MARK line**. Cycle 166's
measured-row source is not the same interface as its generator sources. The
stock two-port reader fixes the source's lower face to `MARK`/`FRAME`, and its
four lower fork paths use that same line as local cable furniture. Removing
the line for a second opposite row witness and asking the retained cable
solver to reroute the same paths leaves exactly 40 segment domains with no
legal guide choice.

That is an exact failure of this composition:

```text
bare opposite-row ingress
        +
stock Cycle-166 P two-port source reader
```

It is **not a serial-composition no-go**. It is not evidence that two-witness
formation is wrong, that repeatability is impossible, or that a new axiom is
needed. An exterior row-decoder/fanout recompile remains live and is the target
of Cycle 176.

## What the finite probe establishes

| Surface | Exact result |
|---|---:|
| signed rows covered | 32 |
| opposite-pair canonical schemas | 32 |
| proper-cubic ingress raw rows | 96 |
| overlap with Cycle 169 unified law | 0 |
| merged law rows | 101,804 |
| merged deterministic conflicts | 0 |
| new onsite roles | 0 |
| stock lower P fork departures using the common guard | 4 |
| empty cable domains after protecting the lower witness corridor | 40 |
| bare orthogonal-pair raw rows | 384 |
| bare orthogonal-pair overlaps/conflicts | 12 / 12 |
| marked opposite-pair raw rows | 384 |
| marked opposite-pair conflicts | 0 |

The marked opposite-pair check is intentionally retained as a live
compiler clue, not promoted as formation language. It shows that the
obstruction is contextual interface composition, not an inability of the
law family to host two-copy relations.

## Bare-metal reading

The useful conceptual distinction is now sharper:

1. Two matching physical copies can be a sufficient local write condition.
2. A later apparatus may already be spending one of those local faces as
   readout infrastructure.
3. When that happens, the readout must be recompiled around the write
   interface; the constitutional sentence should not encode the accident of
   the old readout layout.

The two source witnesses are not the same thing as a third payload-only
ancestry leaf. In the live Cycle-176 route, deleting either witness must stall
source formation. Deleting the payload-only leaf must leave source formation
available while stalling only downstream payload use.

## Why no full serial counts appear

The direct blueprint fails before final cage construction. Reporting a fixed
record count, dynamic record count, causal depth, or min/max schedule width
for a cage that was never lawfully assembled would be false precision.

Cycle 170 already proved that rigid zero-cost serial gluing is unavailable for
the exact Cycle-166 ports and that visible transport must be counted. Cycle
174 adds a different, narrower fact: after transport is admitted, the stock P
readout interface still cannot accept the bare second witness without a
readout recompile.

## No-Go Discipline Gate

The latest `no-go-discipline` skill was read from `origin/main` on 2026-07-16.
This gate is applied to prevent the bounded stock-interface failure from being
inflated into a general no-go.

### N1 — Alternative route enumeration

| route | status | result |
|---|---|---|
| R1: rigidly identify first outputs with second sources | RULED OUT BY PRIOR | Cycle 170 computes unequal source/output separations. Zero-cost rigid gluing fails for these exact ports, but routed composition remains live. |
| R2: attach one ordinary row cable to every stock source | ATTEMPTED | The source sites have no honest single-parent cable face; generator readers occupy four side faces, the row tap occupies `+z`, and a backstop/readout structure occupies `-z`. |
| R3: use the clean opposite-row ingress at `+z/-z` while retaining the stock P reader | ATTEMPTED | The 96-row ingress is positive, but the P reader requires `-z=MARK/FRAME`; the two roles cannot occupy one site. |
| R4: remove the P lower MARK line and re-solve the same four forks | ATTEMPTED | The retained cable solver reports 40 `no-guide-option-against-fixed-records` segment domains. |
| R5: use two bare orthogonal witnesses instead | ATTEMPTED | Its 384 raw images overlap the Cycle-169 law in 12 signatures and all 12 are deterministic conflicts. |
| R6: retain a perpendicular MARK with an opposite witness pair | ATTEMPTED | Positive compiler clue: 384 raw images, zero overlap, zero conflict. It is not yet the preferred bare formation interface because it includes layout context. |
| R7: move P readout outside the source and decode/fan the row there | ATTEMPTED AT DESIGN LEVEL / LIVE | This removes the stock lower-port competition and is exactly the Cycle-176 target. It defeats a broad no-go. |
| R8: align or recompile all second-stage source/readout ports | RULED LIVE BY PRIOR | Cycle 170 explicitly leaves aligned recompilation and reusable adapters open. |

At least five genuinely distinct routes were enumerated. R6–R8 remain live,
so a broad no-go fails this item.

### N2 — Wall-independence audit

The raw attempt exposed two candidate walls:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| W1 physical source/output separation vs W2 stock P lower-guard collision | no | no | yes |

W1 is retired by ordinary visible transport; it is not a wall for Cycle 176.
The collapsed wall set for the narrow Cycle-174 statement therefore contains
only W2: incompatibility of the bare opposite-row ingress with the stock P
two-port lower-guard layout.

### N3 — Hidden-wall scan

The note avoids “we assume,” “as is standard,” “naturally,” and “obviously.”

- “By construction” is not used as proof.
- “Framework provides” is replaced by exact module and row counts.
- “Canonical” appears only in the non-load-bearing count of canonical
  signatures.
- “Background” appears nowhere as a hidden condition.
- The 101,708-row base is cited to the Cycle-169 physical law, not silently
  treated as an axiom.

No hidden condition is promoted to a second wall.

### N4 — Residual matching

| cited witness | witness residual | Cycle-174 residual | match? |
|---|---|---|---:|
| [`RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md`](RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md) | zero-cost rigid port identification | physical transport requirement | yes, for W1 only |
| [`PHYSICAL_TWO_PORT_ROW_FOUR_FORK_CYCLE158_NOTE_2026-07-15.md`](PHYSICAL_TWO_PORT_ROW_FOUR_FORK_CYCLE158_NOTE_2026-07-15.md) | derived bit needs two physical departure ports | why the stock P lower port exists | yes, as architecture provenance; not a no-go witness |
| [`PHYSICAL_THREE_ROW_DUAL_COMMUTATION_BIND_CYCLE159_NOTE_2026-07-15.md`](PHYSICAL_THREE_ROW_DUAL_COMMUTATION_BIND_CYCLE159_NOTE_2026-07-15.md) | measured row reused in two commutators | stock P two-port consumption | yes, as architecture provenance; not a no-go witness |
| [`PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP_CYCLE169_NOTE_2026-07-16.md`](PHYSICAL_ROW_NATIVE_SIGNED_MEMBERSHIP_CYCLE169_NOTE_2026-07-16.md) | exact unified signed-row law | deterministic merge base | yes |

Cycle 170 is not cited as evidence for W2. Cycles 158/159 explain W2 but do
not prove that alternative readout compilers fail.

### N5 — Rhetoric audit

The negative statement is intentionally resolution-limited:

| resolution | tested? | result |
|---|---:|---|
| one local P source interface | yes | bare `+z/-z` witnesses conflict with the stock lower guard |
| all four stock lower P fork departures | yes | each consumes the common lower guard |
| protected re-solve of the stock three-row apparatus paths | yes | 40 segment domains empty |
| arbitrary readout recompilers | no | no negative claim |
| arbitrary signed-row instruments | no | no negative claim |
| lattice-wide serial measurement | no | no negative claim |
| universal record formation | no | no negative claim |

The phrase used is “the stock Cycle-166 P two-port interface does not compose
directly with the bare opposite-row ingress,” not “serial measurement is
impossible.”

### N6 — Partial-closure path scan

Three ordinary compiler paths remain:

1. The clean marked opposite-pair interface: finite and deterministic, but
   carries a layout marker and therefore needs a minimality comparison.
2. Exterior row-decoder/fanout: remove source-local two-port reuse and perform
   the duplicated read downstream. This is Cycle 176.
3. A port-aligned second update: already left open by Cycle 170.

None is a convention reframe or a new axiom. No claim that “a new axiom is
required” is made. No primitive-registry conclusion is needed because the
residual is a compiler interface.

### N7 — Steelman

**Hostile reviewer:** “Your obstruction is self-inflicted by preserving the
Cycle-158 two-port reader at the exact site where you now want a second row
witness. The retained law already transports, splits, and decodes full signed
rows. Move the duplicate readout downstream: let two row copies form the
source, route another descendant to exterior decoders, and feed the same
commutator inputs from there. Cycle 159 itself retired an earlier
measured-row-reuse gap by changing the compiler, while Cycle 170 explicitly
keeps adapters and aligned recompilation live. Until that exterior-decoder
construction fails under exact cage and deletion controls, you have no general
no-go.”

This steelman is convincing. Therefore the broad no-go is premature.

### N8 — Cross-cycle echo

The closest echo is the Cycle-159/Cycle-161 measured-row reuse campaign. An
apparent reuse obstruction was retired by inventing the two-port producer and
then composing it physically. The mechanism was a compiler/interface change,
not an axiom.

Cycle 170 supplies a second echo: exact rigid gluing failed, but the note
explicitly preserved visible transport, reusable adapters, and aligned
recompilation. Again, an exact interface failure did not become a universal
no-go.

The same retirement mechanism applies here. Cycle 176 must try the exterior
decoder/fanout interface before any stronger negative statement is eligible.

**Status: FAIL for a broad no-go. PASS for the narrow partial exact interface
result.**

## Scope

This cycle does not complete a physical serial repeatability run. It does not
derive Born weights, an occurrence law, general Lüders projection, metric
time, or a universal two-witness formation theorem. It does not choose final
axiom language.

No axiom, primitive, registry, policy, or audit edit follows.

## Next probe

Cycle 176 should:

1. reuse the ported-P interface being validated in Cycle 173 where compatible;
2. form the second P source from two physical same-row witnesses;
3. route separate same-ancestry leaves to exterior row decoders/fanout and to
   payload use;
4. prove that removing either source witness stalls source formation;
5. prove that removing only the payload leaf stalls downstream payload use but
   not source formation;
6. preserve one original physical P ancestry across both update stages;
7. run exact min/max schedules, terminal-clean checks, seam checks, and causal
   depth including transport.

# Signed-row egress and membership seam — Cycle 167

Status: parked constructive result and exact interface narrowing on the single
bare-metal compiler PR.

Authority: none. This note changes no axiom, primitive, registry, policy, or
audit surface.

## Question

Can the candidate record law carry the sign of a physical signed-Pauli row
into downstream computation, and does that close commuting signed membership
without host-supplied literals?

## Result

The sign can be carried physically, but the original 97,388-row law did not
contain a usable sign-output interface.

Two exact zero-delta attempts fail:

1. the Cycle-153 fifth-bit output has all six neighboring sites occupied, so
   no later nearest-neighbor write can descend from that terminal; and
2. the proposed open-port sign neighborhood at the Cycle-165 tap site is
   exactly the already-assigned whole-row tap neighborhood. All 768
   proper-cubic images already output the 32-valued row role, so assigning
   `H0/H1` there would make the law nondeterministic.

Those are exclusions of two specified interfaces, not a sign-egress no-go.

A distinct generic sign reader closes the local interface:

```text
Cycle-165 candidate law                         97,388
new sign-reader canonical rows                      32
new sign-reader proper-cubic rows                  768
raw overlap                                           0
raw conflicts                                         0
sign-reader candidate law                        98,156
new onsite roles                                      0
```

All 32 signed rows pass in all 24 proper-cubic orientations, for 768
one-write graphs. The output face remains empty, and all 160 direct-parent
deletions suppress the sign write.

The stronger causal composition also passes. One original row record drives:

```text
whole-row tap -> downstream sign decoder -> H0/H1 cable
```

All 768 row-orientation executions close under the same 98,156-row law. Each
has six reachable causal states, five append edges, maximum frontier one, an
open terminal port, and no parasitic write. Ten direct-parent controls per row
give 320 deletion checks with zero failure.

The sign family is also disjoint from the Cycle-166 joint-update additions:

```text
Cycle-166 joint-update law                      100,652
sign-reader delta                                   768
raw overlap                                           0
raw conflicts                                         0
unified candidate law                           101,420
```

Under that unified law, all 768 downstream decoder graphs retain the same
causal shapes and zero parasitic enables.

This is real physical ancestry for signed information. It is not yet complete
row-native membership.

## Why membership remains open

The factorized membership calculation is exact at component level:

- a five-cell total-status chain compares supplied five-bit literals;
- three equality flags distinguish `g1`, `g2`, and `g1*g2`;
- the retained binary ALU combines the flags; and
- all 2,160 supported/opposite transcripts over 360 valid ordered bases are
  classified correctly.

But that factorized probe still:

- supplies the five literal inputs;
- enumerates `g1*g2` on the host;
- reconnects host equality bits to a separate ALU run; and
- executes the components under retained subsets rather than one routed joint
  law.

Its licensed status is therefore a literal-input component certificate. The
next closure must physically route the Cycle-164 product and five row-derived
bits into three comparator lanes, then route their terminal records into one
OR network under the unified law.

A direct row-role equality architecture is also positive in scratch, but its
signed-domain reduction is not yet packaged and its tested candidate is larger
than the generic sign reader. It is evidence against architectural
impossibility, not yet a replacement theorem.

## Bare-metal meaning

The row record is not merely a label the host can inspect. Under the enlarged
candidate law, its sign can become a separate permanent record with a causal
chain back to the original row and an open face for later computation.

That matters to the TOE interfaces in bounded ways:

- **O:** deterministic quantum support can now consume the sign carried by a
  physical record rather than a host tuple;
- **T:** the chain supplies causal order only, not duration or rate;
- **I:** it strengthens signed rows as physical information carriers, not as
  derived matter or particle species;
- **B:** a supplied candidate outcome can now leave a record-native signed
  transcript, but its occurrence remains supplied; and
- **G:** the extra rows and records are compiler costs until an independent
  physical resource map is derived.

## No-Go Discipline Gate

Status: **FAIL for a general no-go; PASS for the two exact interface
exclusions stated above.**

### N1 — alternative routes

1. **ATTEMPTED:** attach a cable to the Cycle-153 fifth-bit terminal. It fails
   because all six neighboring sites are occupied.
2. **ATTEMPTED:** reuse the Cycle-165 tap neighborhood for `H0/H1`. It fails
   because all 768 images are already assigned the whole-row output.
3. **ATTEMPTED AND POSITIVE:** move sign decoding to a distinct ported
   five-parent signature. It closes with 32 canonical / 768 raw rows.
4. **ATTEMPTED AND POSITIVE:** copy the row, decode sign downstream, then
   cable it. The full causal chain closes in all 768 row-orientation runs.
5. **ATTEMPTED AND POSITIVE IN SCRATCH:** compare row roles directly and avoid
   literal sign extraction. The packaged signed-domain theorem remains open.
6. **LIVE:** wider-patch decoding and separate scalar-sign ancestry remain
   unexcluded.

A universal sign-egress no-go therefore fails N1.

### N2 — wall independence

Terminal occupancy and tap-signature collision concern different exact
geometries, but neither remains a general wall after the positive reader.
The collapsed open condition is end-to-end membership composition.

### N3 — hidden-condition scan

The word `impossible` is licensed only with all of these qualifiers: the exact
tested site, exact neighborhood, deterministic single-output law,
preservation of the Cycle-165 tap assignment, and zero new rule rows.

### N4 — residual matching

Cycle 153 supports only the sealed-terminal statement. Cycle 165 supports only
the whole-row tap assignment. Neither supports a universal sign-egress
obstruction.

### N5 — rhetoric audit

This note does not say `sign egress is impossible`. It says that one terminal
has no port and one preassigned tap signature cannot also output a sign while
preserving determinism.

### N6 — partial closure and axiom classification

The positive +768 repair holds the four axioms fixed and changes only finite
candidate-law/compiler content. That is direct evidence against treating the
interface gap as missing constitutional physics.

### N7 — strongest hostile steelman

A hostile reviewer defeats any broad no-go by moving the decoder, adding the
disjoint generic sign family, transporting the complete row before decoding,
or comparing row roles directly. That steelman succeeds, so only the narrow
interface exclusions survive.

### N8 — cross-cycle echo

Cycle 158 already retired a supposed one-port obstruction by redesigning the
producer. The same mechanism succeeds here; terminal geometry is an
architecture constraint, not a universal law.

## Scope

Nothing here derives outcome occurrence, probability, prepared-state identity,
general quantum mechanics, local time, matter, continuum dynamics, gravity, or
law selection.

No axiom, primitive, registry, policy, or audit edit follows.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_signed_row_egress_collision_probe_2026_07_16.py
PYTHONPATH=scripts python3 scripts/physical_ported_sign_reader_probe_2026_07_16.py
PYTHONPATH=scripts python3 scripts/physical_downstream_signed_row_decoder_probe_2026_07_16.py
PYTHONPATH=scripts python3 scripts/factorized_commuting_signed_membership_probe_2026_07_16.py
```

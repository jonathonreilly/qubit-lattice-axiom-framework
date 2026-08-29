# Independent Checker Return

## Final verdict

```text
FALSE-GREEN
SCOUT-FAILED-TO-CONSTRUCT-FROZEN-SIGNED-RAY-FAN-GRAMMAR
```

The final independent reviewer inspected the complete frozen primary source
at pre-falsifier SHA-256
`0c8f4cfab03869e2fd0fa0dcf25b56839dbccbad9f30f43a027b8b502e053b16`,
replayed its `11/11` checks and `32/32` original mutation rejections, and then
audited payload provenance, operation typing, and new mutations. No files were
edited during that review.

## Exact structure that passed

- all `596` expected route skeletons are present: `73` conflict, `43` blank,
  `438` broadcast, `12` predicate, and `30` obstacle;
- every route has the expected nearest-neighbor outward and return edge
  sequence, for `2,388` explicit onsite handoffs;
- no literal target aliases occur within one layer;
- all `258` private writer preparations are present, with `24` `P143` and
  `234` Bell preparations;
- the six-direction Clifford orbit is correct;
- the declared barrier/commit/lock ordering is exact at layers `47/48/49` and
  `107/108/109--113`;
- the resource arithmetic derives `4,253` route bits and elementary depth
  `114`.

Those are useful geometry, ordering, and resource facts. They do not prove an
executable payload circuit.

## Decisive false greens

### 1. Unsourced route requests

All `43` blank routes, `12` predicate routes, and `30` obstacle routes begin
with `SWAP(seed, root_lane)`, but no emitted gate produces those `85` seeds.
Only conflict and branch-broadcast seeds are sourced.

### 2. Operations are not bound to compatible exact maps

- `2,388` `ONSITE_SCATTER` handoffs name two one-bit lanes while the registered
  map is dimension `64`;
- `170` QND endpoint operations and `85` endpoint `CNOT` operations name three
  binary targets while their registered maps are dimension `4`;
- `146` `INC7`/`DEC7` events include a lane control absent from their
  dimension-`128` maps.

Thus the route-event labels and isolated map catalogue do not compose into
the advertised circuit.

### 3. Eight new mutations survive

Both the old schedule and resource certificates accept all of the following:

1. an edge opcode changed to `CNOT`;
2. an endpoint query changed to `CNOT`;
3. a handoff changed to `CNOT`;
4. one fresh-`A2` cleanup deleted;
5. one candidate QND unquery deleted;
6. one writer purifier miswired;
7. one six-state writer commit stage miswired; and
8. the controller affine preparation disconnected from candidate staging.

## Disposition of the earlier independent runner

The earlier independently written runner returned `10/10` and rejected
`58/58` of its own mutations, but represented the circuit as a macro-level
typed dependency graph. It did not expose the primary's missing request
producers or bind the exact gate maps to the literal emitted payloads. Its
positive terminal is therefore rejected and its cache is not landing
evidence.

The same applies to the alternate `14/14` backup implementation: it was a
macro-labeled DAG, not the requested executable compiler.

## Final primary response

The primary was converted into a failure certificate rather than repaired a
second time. It now independently computes the `85` missing seeds, the three
load-bearing map-binding families, and all eight surviving mutations, while
preserving the valid geometry, channel algebra, resource arithmetic, and
strict-`M2` quotient subcertificate.

Final primary SHA-256:

```text
a2e9eee43e5bd0f7f44bdf6d5a7007effeec557726b88124e7feee5cf10606e2
```

The failure is restricted to the frozen signed-ray/fan candidate. Other
finite compilers, carrier realizations, and pure-Record process laws remain
live. No axiom update, audit verdict, obligation retirement, or TOE movement
follows.

# Compact five-literal membership bind — Cycle 183

Date: 2026-07-16

Status: construction-scoped negative; current custom endpoint branch rejected.

## Authority and freeze

Cycle 183 consumes the retained Cycle-180 spacing-12 compact bundle:

```text
predecessor commit          02e981979a753b66d38c19f9b8208d37c0c4f0db
Cycle-180 runner hash       6395239ffe1ded603d9c0d97bad9919bb2460ac1613f384761bd1a23405277c7
Cycle-180 note hash         2ea6be500f31587eaa8ae662b2d26dfc33d710969d19b507e547d8c23e0fbc61
```

No foundation, axiom, primitive, registry, queue, policy, audit, predecessor,
commit, push, or PR surface is changed.

## Intended construction

The attempted apparatus begins at the five generated Cycle-180 endpoints. It
adds:

1. one value-neutral status branch per endpoint;
2. one value-preserving `H0/H1` branch per endpoint;
3. a binary status tree with first joins `(0,1)` and `(2,3)`;
4. one final `MEMBER5` status with all-five intended ancestry; and
5. one ordered five-port literal consumer, with one terminal `H0/H1` record
   per lane.

The candidate never reconstructs a 32-valued payload. It prices exactly three
fresh apparatus roles:

```text
MEMBER5             dynamic value-neutral status
MEMBER5_FRAME       supplied status-path structure
LITERAL_FRAME       supplied literal-path structure
```

The final candidate price is:

```text
compiled canonical rows                         21
proper-cubic raw rows                           330
merged full-law rows                        102,326
fresh onsite roles                                3
supplied frame records                         2,739
intended generated records                       715
  status records                                 320
  literal-path records                           390
  final consumer records                           5
raw-law conflicts                                  0
```

The intended dependency graph is local and acyclic. It has no unintended
adjacent dynamic pair. Its first cross-bit ancestry occurs only at the two
declared joins:

```text
J01       (-35,  9, 0)
J23       (-35, 33, 0)
J0123     (-50, 21, 0)
JFINAL    (-65, 40, 0)
```

At the graph-specification level, `JFINAL` and all five consumer ports have
ancestry `{0,1,2,3,4}`. Those are surviving construction facts, not a promoted
physical theorem, because the full-law execution fails earlier.

## Two repairs tested

The first geometry put supplied frame records within the unused open face
`endpoint - z`. That face acquired a rotated literal-leaf signature and wrote
a parasitic `H0/H1`.

Repair 1 placed a sterile frame halo around every unused face. This works:

```text
unused site       (-26, y_i, -2)
local signature   {+z : H0} or {+z : H1}
full-law output   none
orientations      24 / 24 sterile
```

Repair 2 made the literal branch wait on the same-lane status leaf before
turning away from the recurrent endpoint. This preserves the intended
single-lane ancestry, but it does not make the branch executable. It exposes
the two exact residual seam defects below.

## Exact residual defects

Let the recurrent endpoint be `(-26, y_i, -1)` and its literal leaf be
`(-26, y_i+1, -1)`.

### R1 — inherited H0-only flip

After an `H0` literal leaf forms, the site

```text
(-25, y_i+1, -1)
```

sees:

```text
{-x : H0, -y : H0}
```

The unchanged Cycle-180 base law maps that signature to `H1`. The two inputs
are the new literal leaf and the prior recurrent payload record. This occurs
on all five lanes for `H0`. The corresponding two-`H1` signature has no base
output.

### R2 — new-delta self-copy

For either literal value, the site

```text
(-26, y_i+1, -2)
```

sees:

```text
{-z : LITERAL_FRAME, +z : H0} -> H0
{-z : LITERAL_FRAME, +z : H1} -> H1
```

This is a proper-cubic image of the candidate literal-leaf rule. It therefore
creates an unintended second literal write on all five lanes for both values.

Both residuals are exact in all 24 proper-cubic orientations. R1 belongs to
the inherited full law; R2 belongs to the new 330-row delta. Removing either
does not remove the other.

## Full-history result

All 32 five-bit words fail the composed full-history certificate before the
status tree can be consumed. Every first failure is confined to the two named
endpoint-seam site classes above.

This means the following requested positive gates cannot be claimed:

- all-32 carrier-to-membership-to-consumer closure;
- schedule confluence of the completed apparatus;
- absence and wrong-phase controls for a completed apparatus; or
- a physically executed all-five membership record.

The direct causal-edge test itself is clean: deleting the generated endpoint
from either immediate leaf premise removes that write in all
`32 × 5 × 2 = 320` cases. That fact does not rescue the apparatus because the
baseline branch already writes parasitic records.

## What survives, and what does not

Survives as bounded construction evidence:

- a deterministic three-role candidate delta;
- a local 715-node join/consumer dependency graph;
- a value-neutral intended `MEMBER5` tree;
- first intended cross-bit ancestry only at `J01` and `J23`;
- all-five intended ancestry at `JFINAL` and the five literal ports;
- no 32-valued payload role; and
- 320 exact endpoint-to-leaf local deletion checks.

Does not survive as physics:

- no generated membership theorem;
- no terminal consumer theorem;
- no bound moving object;
- no particle identity;
- no matter theorem; and
- no evidence that proximity alone binds the five recurrent worldlines.

## Shortest next constructive route

Do not add another custom `H0/H1` copy rule at the embedded recurrent
endpoint.

The shortest live route is to bind the retained typed literal cable and its
terminal/egress pattern to one generated endpoint port, carry one literal stem
outside the recurrent support, and split into status and consumer branches
only there. The typed literal cable is already present in the common law, so
this route attacks both seam defects without adding a new literal-transport
alphabet. The value-neutral join tree can then be reused downstream.

Other live routes are an endpoint-terminal redesign, a staggered egress
direction, or two explicit bit-specific intermediate roles. Those are
law/interface probes with an explicit price, not axiom questions.

No axiom addition follows.

## TOE-lane reading

- **Information:** the intended five-literal membership graph is coherent,
  but the physical branch into it is not.
- **Quantum:** no coherent-state or tensor-product theorem is involved; the
  domain remains the generated finite-composition domain.
- **Matter:** open. This result is not particle identity and not a matter
  theorem.
- **Time:** unchanged from the recurrent `1/13` causal ratio.
- **Probability:** untouched.
- **Gravity:** untouched.
- **Formation/readout:** the exact open item is now an executable endpoint
  egress into a retained literal consumer, not a missing formation axiom.

## No-Go Discipline Gate

The negative is only: this exact custom three-role endpoint branch does not
compose with the unchanged Cycle-180 full law. It is not a universal binding
no-go.

### N1 — Alternative route enumeration

1. **Sterilize the unused endpoint face — ATTEMPTED.** The halo removes the
   original third-face firing in all 24 orientations, but R1 and R2 remain.
2. **Make the literal branch wait on the status leaf — ATTEMPTED.** The bridge
   preserves same-lane ancestry but exposes the inherited R1 and self-copy R2
   signatures.
3. **Use only the `H1` branch — ATTEMPTED.** R1 disappears for `H1`, but R2
   still writes an unintended `H1`, so even the all-`H1` word fails.
4. **Use only the `H0` branch and absorb its extra write — ATTEMPTED.** `H0`
   produces both R1 (`H1`) and R2 (`H0`) at distinct sites; treating one as a
   desired continuation leaves the other immutable parasitic record.
5. **Rotate the apparatus away from the seam — ATTEMPTED.** Both residual
   signatures are proper-cubic law orbits and remain exact in all 24
   orientations.

The retained typed-cable egress, a redesigned endpoint terminal, and new
bit-specific intermediate roles are deliberately untested live routes.

### N2 — Wall-independence audit

The current candidate has exactly two residual defects:

| Pair | Does closing the first close the second? | Reverse? | Independent? |
|---|---:|---:|---:|
| R1 inherited H0 flip / R2 new self-copy | no | no | yes |

R1 is absent for `H1` while R2 remains, which is a direct independence
witness. R2 is a new-delta orbit; removing it does not remove the inherited
R1 row.

### N3 — Hidden-wall scan

The law, endpoint geometry, frame roles, expected graph, and supplied
scaffold are explicit. “Candidate” and “retained” identify exact code
surfaces, not hidden physical premises. No appeal to standard physics,
background binding, natural grouping, or an unnamed framework provision is
used.

### N4 — Residual matching

| Witness | Witness residual | Cycle-183 residual | Match? |
|---|---|---|---:|
| Cycle 180, binding-status section | five compact rails have no generated common membership target | attempted local join remains unreachable because endpoint egress writes parasitic records | yes |
| Cycle 154 typed literal cable | executable typed `H0/H1` path and terminal pattern | proposed next egress route, not evidence for the present negative | not used as a no-go witness |

No unrelated failed campaign is cited as evidence.

### N5 — Rhetoric audit

The failure is tested at one exact local seam, for five translated copies,
both literal values, all 32 words, and all 24 proper-cubic signature images.
It is not lifted to every endpoint geometry, every cable construction, every
local law, the full lattice, or nature’s ability to bind records.

### N6 — Partial-closure path scan

Repair 1 already retires one defect without new physics. The retained typed
literal cable offers a second direct import-retirement path: reuse existing
law content rather than declare a new axiom. A new endpoint terminal or
bit-specific intermediate roles would be explicit bounded law prices. None is
an automatic axiom need.

### N7 — Steelman

A hostile reviewer should reject any broad no-binding conclusion. The
candidate invents a custom literal copy beside a recurrent endpoint even
though the common law already contains a typed literal cable and terminal
machinery designed to prevent exactly this kind of parasitic face firing.
Moving one literal stem outside the recurrent support before splitting could
preserve the entire downstream value-neutral join tree. That steelman
succeeds, so the result is demoted to the exact construction-scoped negative
stated here.

### N8 — Cross-cycle echo

Cycle 172’s nonphysical 32-role carrier was repaired in Cycle 178 by changing
representation, and Cycle 178’s wide geometry was repaired in Cycle 180 by
changing placement. Those successful redesigns are direct warnings against
promoting the present seam failure into a universal no-go. The next cycle
should change the egress representation, not the axioms.

Gate status: **PASS for the narrow custom-branch failure; FAIL for any
universal density, binding, particle, or matter no-go.**

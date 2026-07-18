# R_B01 orientation-13 phase-chain alias — Cycle 127

Date: 2026-07-15

Authority: none

Disposition: exact bounded negative for one literal phase-chain layout

Write scope: runner + review note only

Companion runner:

```text
scripts/r_b01_orientation13_phase_chain_alias_cycle127_2026_07_15.py
```

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited here. No commit, push, or PR is made. Cycle 125 is the
exact preceding bounded negative; its bad candidate law is not inherited.

## Exact result

Cycle 127 tests the bounded object

```text
R_B01_ORIENTATION13_G0_G4_LITERAL_CHAIN
```

against the official Cycle-124 terminal. Proper-cubic orientation 13 maps the
old Cycle-119 port onto the fresh `R_B01` port. The relevant transformed sites
are:

```text
D1   = (6,3,-3)
D2   = (5,2,-3)
D4   = (6,2,-3)
D7   = (6,1,-3)
JOIN = (5,1,-3)

G0 = (5,1,-3)
G1 = (6,1,-3)
G2 = (7,1,-3)
G3 = (7,2,-3)
G4 = (7,3,-3).
```

Thus `G0` is exactly the transformed JOIN coordinate and `G1` is exactly the
transformed D7 coordinate. A phase-only reading permanently occupies two
required writer sites. The attractive dual-use reading—G0 as a phase-labelled
join and G1 as physical D7=H1—also fails exactly.

G0 is well anchored: its source local is two perpendicular `L6` records. But
proper-cubic closure makes that row fire at five source sites, not only G0.
More decisively, once any chosen G0 role is present at the intended site, G1
and D2 each see exactly one G0-role neighbour. Their directions differ, but
their canonical locals are identical under proper cubic rotation. The literal
word requires

```text
G1/D7 -> H1
D2    -> H0.
```

One single-valued covariant local row cannot do both.

The onsite alphabet was exhausted rather than sampled:

```text
phase roles tested                           153
roles conflicting with a live unary law      18
roles already carrying unary -> H1             1
roles that could add unary -> H1              134
nonconflicting roles that still write D2=H1  135
G0 source co-images                            5
```

For the absent representative phase role `R_C01`, forming all five anchored
co-images leaves nineteen pure-unary shell sites. Both G1 and D2 are in that
same shell. Including all co-images therefore exposes the conflict rather than
repairing it.

G2 cannot be the missing prior parent: it is downstream of G1 in the proposed
chain. G3 does neighbour D4 and G4 neighbours D1, but those later guards do not
alter the first G0-to-G1/D2 unary fork. The exact literal `G0..G4` chain is
therefore closed as proposed.

## Smallest live frontier

The smallest current collision is one unary phase orbit trying to assign
different contents to two perpendicular neighbours of G0. A live repair must
change the local inputs before either target is exposed. The two most direct
options are:

- use relocated D7 and JOIN sites, leaving G0/G1 phase-only, then give the new
  G1 step a second parent that D2 does not see and force that parent to exist
  before G0 can expose either unary target;
- keep a dual-use D7 only after a separate provenance strand supplies a second
  G1 parent and causally gates D2 through a downstream adjacent token.

The first option—**relocated D7 and JOIN** plus a two-parent phase step—is the
cleaner geometric next target, but the second parent must be causally forced
before either unary target becomes available.  An independently enabled or
broad parent is not enough.  Other clean orientations and a fully nonliteral
writer geometry remain live.

A post-Cycle-127 diagnostic scratch screen makes that warning concrete.  It
finds 304 role pairs that distinguish G1 from D2 after both parent orbits are
fully present, but the best partial-subset compilation still exposes nine
unexpected targets before that complete context is guaranteed.  Those numbers
are a follow-up scratch result, not a retained Cycle-128 theorem and not part
of the Cycle-127 companion-runner contract.  They show only that static
two-parent separation does not establish every-schedule causal closure.

This is **not a no-go against every orientation-13 redesign**.
It is **not a no-go against an R_B01 writer**. It is only an exact negative for the literal
coordinate assignment and chain order above. **No axiom addition follows**
from this local alias.

## Bare-metal meaning

The failure sharpens what provenance must do. Naming a phase role is not
enough. The local neighbourhood must contain enough already-written structure
to distinguish candidate directions under the same covariant law, and that
structure must be causally prior—not merely scheduled earlier in one preferred
history. Neither a read, a clock, nor a global storage counter fixes an
isotropic unary fork.  A causally prior second local parent, forced to exist
before either unary target becomes available, may distinguish them; an
independently enabled parent does not yet do so.

## N1–N8 no-go-discipline gate

Status: **PASS only for the literal orientation-13 `G0..G4` bounded negative;
FAIL for a universal orientation-13 no-go, R_B01-writer no-go, recurrence
no-go, or axiom-need claim.** The current `origin/main` no-go-discipline body
governs this note.

### N1 — Alternative routes

| route | marker | result |
|---|---|---|
| literal G0=JOIN and G1=D7 dual use | `ATTEMPTED / NEGATIVE` | all 153 roles leave the exact unary G1/D2 content conflict |
| literal G0/G1 phase-only | `ATTEMPTED / NEGATIVE AS LITERAL REUSE` | permanently occupies transformed JOIN/D7, requiring relocation |
| relocated D7 and JOIN plus causally prior two-parent G1 | `LIVE / SHARPENED` | removes the static coordinate alias and can distinguish the full G1 context, but the 304-pair scratch screen leaves at least nine unexpected partial-subset targets unless precedence is enforced |
| gate D2 through a downstream provenance token | `LIVE` | may preserve D7 dual use if the token is forced before the unary fork |
| choose clean orientation 20 with anchored tail redesign | `LIVE` | Cycle 125 closed only the unanchored D5/R_C01 patch |
| rail-attached two-strand provenance cage | `LIVE` | supplies directional context without unary propagation |
| abandon literal Cycle-121 geometry | `LIVE` | permits a third writer optimized for the new boundary |
| branch-local commits and later join | `LIVE` | changes the completion geometry entirely |

At least six materially distinct routes remain. No universal negative ships.

### N2 — Residual independence

| pair | first closes second? | second closes first? | treatment |
|---|---|---|---|
| coordinate alias vs unary content alias | relocation closes the first, not automatically the second | a full two-parent local can distinguish the second, but not its unsafe prefixes | two genuine but related local obligations |
| full two-parent distinction vs partial-subset safety | no: full context does not force parent precedence | yes: a causally safe start includes the full-context distinction | one causal-order obligation, not two independent walls |
| causally prior two-parent phase start vs complete R_B01 writer | necessary but not sufficient | writer includes it | one ordered construction |
| third word vs finite grammar | evidence, not sufficient | grammar includes it | one downstream chain |
| finite grammar vs unbounded recurrence | necessary, not sufficient | recurrence includes it | one downstream chain |
| writer existence vs exact-law selection | no | no | independent residuals |

The word/grammar/recurrence items remain one dependency chain.

### N3 — Hidden-condition scan

The official source, Cycle-124 terminal, orientation index, coordinate shift,
five proposed chain sites, transformed writer sites, 153-role alphabet,
proper-cubic quotient, five G0 co-images, and nineteen-site representative
shell are explicit. “Same local” means equal after the exact proper-cubic
canonicalization used by the candidate law. No preferred direction, scheduler,
reader, clock, or unregistered phase bit distinguishes G1 from D2.

### N4 — Residual matching

| cited witness | witness residual | Cycle-127 residual | match and use |
|---|---|---|---|
| Cycle-124 reuse probe | clean orientations need an earlier phase guard | orientation-13 G0..G4 literal guard | exact proposed follow-up, closed only in literal form |
| Cycle-125 negative | unanchored tail and unary aliases | anchored G0 but unary G1/D2 fork | same provenance genus, different exact local |
| generic orientation-13 redesign | any relocated/caged writer | one fixed coordinate assignment | no match; not closed |
| generic R_B01 writer | any finite append-safe word | one failed phase start | no match; not evidence for a no-go |

Nonmatching residuals constrain rhetoric rather than support a larger wall.

### N5 — Resolution and rhetoric

Tested: one exact orientation and translation, all 153 onsite roles, all
proper-cubic images of the G0 and unary rows, every source G0 match, and a
representative complete unary shell. Not tested: relocated D7/JOIN coordinates,
every possible second-parent site, other redesigned orientations, long bridges,
or the complete space of writers.  The separate 304-pair scratch screen tests
full-context role separation and reports a best nine-target partial-subset
warning; it is not a completed append graph or a retained next-cycle result.
“Literal chain fails” cannot become “orientation 13 fails” or “phase
provenance fails.”

### N6 — Partial-closure paths and axiom discipline

Relocating D7/JOIN and adding a **causally prior** second G1 parent is a named,
finite constructive path.  Merely adding an independently enabled broad parent
has now failed the partial-subset screen and is not credited as closure.  A
rail-attached two-strand cage is another live way to enforce precedence.  Both
operate wholly inside the existing nearest-neighbour, append-only candidate
framework. The alias is what covariance should expose; it is not evidence for
a new formation axiom.

### N7 — Strongest hostile steelman

A hostile reviewer should object that the G-chain proposal silently reused
two data/cage coordinates and treated a directional sketch as if covariance
would preserve its direction. Once all rotations are included, the anchor
fires five times and its unary successor cannot tell D7 from D2. That kills the
literal sketch before a full writer graph is relevant. But the same reviewer
cannot promote this to a writer no-go.  Relocation removes the coordinate
alias, while a causally forced second parent may remove the unary alias; the
304-pair/nine-target warning proves that full-context separation alone is not
enough.  Rail-attached or otherwise precedence-enforcing strands remain live.

### N8 — Cross-cycle echo

Cycle 121 rejected a generic FRONT orbit on a corrupt boundary and repaired it
with causal provenance. Cycle 125 rejected a cosmetic phase label because its
tail had an empty local. Cycle 127 rejects a unary phase fork because rotation
erases the intended direction. The repeated lesson is constructive and local:
phase must be encoded by multiple prior records, not by role names or preferred
drawings.  The partial-subset warning sharpens this again: multiple records
must have enforced causal order, not merely coexist in the intended final
context.  That supports a causally prior two-parent repair target, not
constitutional promotion.

## Verification

```text
python3 scripts/r_b01_orientation13_phase_chain_alias_cycle127_2026_07_15.py
```

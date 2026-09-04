# `CFSI-QH11`: Homogeneous Record-Decoded Quantum Front Probe

**Date:** 2026-07-14

**Type:** meta

**Scope:** finite-range homogeneous local decoder, collision arbitration,
append-only microstage memory, mixed-frame transport, and record-Markov
sufficiency for a declared finite Bell repertoire

**Authority:** none. This is a bounded candidate-law construction and
acceptance probe, not the physical law, an axiom proposal, an audit verdict,
or a retained theorem. It changes no axiom, registry, or audit surface.

## Result In Plain Language

The hand-enumerated ray and cell schedule in `CFSI-Q7` can be removed. A
single finite local decoder can inspect permanent boundary/program records,
recognize the same coherent Bell process wherever it occurs on `Z^3`, and
advance it without an absolute origin, preferred direction, or simulator
order. Call the eleven-site construction **`CFSI-QH11`**.

The new content is not another quantum formula. It is exact process plumbing:

- the cell's direction and transverse axis are inferred from an asymmetric
  local record motif;
- the same decoder is translation-covariant and covariant under all 24 proper
  cubic rotations;
- overlapping candidate motifs are resolved by an immutable local
  strict-priority rule;
- two append-only stage records—a prepared certificate and a propagated
  certificate—make every coherent microstage reconstructible from records;
- disjoint admitted events commute, so their execution order is bookkeeping;
- a recorded relational link transports Bob's local frame into the source
  frame; and
- for the declared binary phase, binary link, and two-setting Bell repertoire,
  equal complete record configurations imply equal future transcript laws.

This is a positive construction, not a derivation of the physical law. It
still supplies a finite program alphabet, boundary motifs, collision
priorities, exact gates, exact measurement angles, trace weights, and one
actual branch sample. A priority tie blocks both colliding motifs. That is an
exact covariant answer, but not evidence that nature uses priority tokens or
permits deadlocked program collisions.

The bare-metal gain is sharper than a new formation slogan: coherent process
memory need not be an unrecorded clock. The permanent record configuration
contains enough certificates to reconstruct whether a motif is blank,
prepared, propagated, or committed. The rule advances that decoded stage.
There is no hidden program counter and no hand-written list of cell addresses.

## One Homogeneous Eleven-Site Motif

At every lattice anchor `o`, and for every ordered pair of orthogonal cubic
unit vectors `(d,t)`, define

```text
u = d cross t.
```

Proper cubic rotations preserve this orientation relation. The candidate
looks for the following role-tagged records and open work sites:

```text
priority record:             o-d-t
phase record:                o-d
relational-link record:      o-d+t

source A work site:          o
source B work site:          o+t
front A work/record site:    o+d
front B work/record site:    o+d+t

setting A record:            o+d-t
setting B record:            o+d+2t

prepared certificate:       o+u
propagated certificate:      o+d+u
```

The eleven sites are distinct. The motif has finite Manhattan diameter five.
The coherent source pair, both propagation edges, and both certificate writes
are nearest-neighbor local. Measurement reads a fixed finite neighborhood.

Each immutable program record contains a role, a local nonce/color, and its
finite value. The declared values are:

```text
phase s in {0,1},
settings x,y in {0,1},
link ell in {0,1},
priority q in a supplied finite ordered alphabet.
```

The nonce prevents accidental hybrid motifs assembled from nearby programs.
It is reusable outside the finite conflict neighborhood; it is not an
absolute site name. The finite role/value alphabet has an injective encoding
by distinct rank-one elements of `M_2(C)`. Those elements need not be mutually
orthogonal. This is an algebraic law encoding, not a claim that a laboratory
can perfectly distinguish arbitrary nonorthogonal qubit records by an
unrestricted read.

The allowed program-boundary class includes a local nonce-separation
condition: two distinct program packets inside one decoder neighborhood do not
reuse a nonce. Because that neighborhood has bounded degree, a finite local
color alphabet can satisfy the condition. This construction supplies such a
coloring; it does not derive or autonomously generate it. Without the
condition, records from different packets could synthesize a spurious hybrid
motif.

The decoder examines every phase-role record and every local ordered cubic
frame. It accepts a motif only when all five program-role records with the
same nonce occupy the relative positions above. Therefore translating the
record configuration translates the decoded programs. For every proper cubic
rotation `R`,

```text
(o,d,t,u) -> (Ro,Rd,Rt,Ru),
```

and the same program is decoded. No coordinate parity, lexicographic site
order, ray number, or global clock is consulted.

## Exact Collision Rule

Two detected motifs conflict when their complete eleven-site footprints
intersect. A motif is admitted exactly when its recorded priority is strictly
greater than the priority of every conflicting detected motif.

This is a finite local test: intersecting fixed-diameter footprints have
anchors within a fixed finite distance. It has three exact consequences:

1. every two admitted motifs have disjoint full footprints;
2. a unique local priority maximum wins every tested overlap; and
3. equal-priority colliders are both blocked.

Priorities and program records are permanent, so arbitration does not change
mid-process. A lower-priority rejected motif cannot become active after the
winner writes a stage certificate. Distant disjoint motifs remain independent.
Translations and proper cubic rotations preserve footprint intersection and
priority comparison, so the winner transforms covariantly.

This is deliberately conservative. In a chain of conflicts, a motif can lose
to another motif that is itself rejected. Choosing one optimum independent set
would require a more global rule or more recorded arbitration data. The local
strict-priority construction establishes existence of a homogeneous exact
collision semantics; it does not select the best one.

## Record-Reconstructible Microstages

For an admitted motif, the same fixed rule decodes one of four stages from
record presence.

### Stage 0: blank

All five program records are present. Both certificate sites and both front
sites are open. The derived work representation is

```text
|0000>_(source A,source B,front A,front B).
```

The first atomic microevent applies on the source pair

```text
U_prepare(s) = Z_A^s CNOT_(A->B) H_A
```

and appends the prepared certificate at `o+u`.

### Stage 1: prepared

The prepared certificate is present and the propagated certificate is open.
The complete records reconstruct

```text
|Phi_s>_source tensor |00>_front.
```

The next atomic microevent applies the two disjoint nearest-neighbor swaps

```text
SWAP_(source A,front A) SWAP_(source B,front B)
```

and appends the propagated certificate at `o+d+u`.

### Stage 2: propagated

Both certificates are present and both front sites are open. Records now
reconstruct

```text
|00>_source tensor |Phi_s>_front.
```

The setting, phase, and relational-link records reconstruct one normalized
local Bell instrument. Exactly one joint outcome is sampled, and both front
outcome records are appended as one atomic commit.

### Stage 3: committed

Both certificates and both outcome records are present. The outcome records,
settings, phase, and link reconstruct the normalized branch state. Later
admitted operations preserve the outcome sectors. The source pair remains
blank.

Every transition appends records and leaves every older record byte-for-byte
unchanged. A torn configuration with only one front outcome is invalid and
does not silently decode as a physical stage. Thus atomicity has a precise
meaning: each of the three listed finite-support transitions is indivisible,
while the boundaries between them are permanent and readable. Internal gate
factorizations are calculations of one microevent, not extra exposed states.

## Causal Order Without A Synchronous Front

Within one motif, record dependencies give the order

```text
program -> prepared certificate -> propagated certificate -> outcomes.
```

Across admitted motifs, full footprints are disjoint. Their branch maps
commute, and their joint probabilities multiply. Any linear extension of the
resulting event partial order gives the same finite record distribution.

For a pathwise coupled test, the runner attaches a randomizer coordinate to
the physical motif event rather than consuming one global simulator stream.
Executing two commits in opposite orders then produces the same final records.
The invariant physical claim needs only equality of the joint distribution;
event-addressed coupling is one exact realization of it.

This construction incorporates the acceptance rule in
`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md`:
the total execution order is removable, but causal inputs must be recoverable
from records and the rule. Here the append-only certificates are those causal
inputs.

## Mixed-Frame Transport

Let the source/Alice frame be the reference coordinates of one motif. Bob's
setting record names an observable in Bob's local frame. The relational-link
record contains, for the declared finite control,

```text
L_0 = I,              L_1 = S = diag(1,i).
```

The physical Bob observable in source coordinates is

```text
B_y^(ell) = L_ell B_y L_ell^*.
```

If Bob changes local matrix coordinates by `V`, then

```text
B_y -> V B_y V*,      L -> L V*,
```

and the transported physical effect is unchanged. This is a genuine
relational datum, not a basis privileged by bare `M_2(C)`.

For `ell=0`, the standard settings give exact

```text
CHSH = 2 sqrt(2).
```

For `ell=1`, the same local setting names have a quarter-turn relative to the
source and give exact

```text
CHSH = sqrt(2).
```

Both laws normalize and remain no-signalling. The link therefore has an
operational transcript discriminator.

One shared pointer axis is not enough to recover this link: `S Z S*=Z`, while
`S X S*=Y`. The minimum for this **two-member** link family is one binary link
bit. Geometrically, it supplies the otherwise invisible twist around the
pointer axis. For unrestricted frames, the required relation is a full
`PSU(2)`/`SO(3)` frame transform, or an equivalent pair of noncommuting
reference axes; the one-bit result is not generalized beyond the finite
control.

## Conditional Record-Markov Sufficiency Theorem

Fix a finite record configuration in the declared program alphabet and a
finite set of well-formed motifs. Assume every physical microevent is one of
the three exact transitions above. Then the complete record configuration is
a predictive Markov state for this repertoire.

The proof is direct:

1. motif detection is a deterministic finite function of records;
2. collision admission is a deterministic finite function of detected
   footprints and recorded priorities;
3. each admitted motif's stage is a deterministic function of certificate
   and outcome-record presence;
4. phase, settings, and relational link reconstruct its work-state
   representation and next branch instrument;
5. admitted supports are disjoint, so their branch maps and scalar weights
   commute; and
6. induction on the remaining finite stages therefore makes every finite
   future cylinder probability a function of complete records alone.

Consequently, for equal complete records `C=C'` and the same declared future
intervention domain,

```text
P(future transcript | C) = P(future transcript | C').
```

The runner checks equal decoders, equal stages, equal work states, equal next
tables, a sixteen-branch two-motif joint law, exact marginalization, and
opposite execution orders. It also checks the necessary finite memory:

- deleting phase merges opposite coherent preparations;
- deleting the relational link merges distinct relative-frame laws;
- deleting stage certificates merges blank and prepared work states; and
- deleting priorities merges configurations with opposite collision winners.

This theorem is limited to the declared finite program family. It does not
cover arbitrary continuous phase, arbitrary `SU(2)` links, arbitrary quantum
channels, overlapping noncommuting instruments, program self-generation, an
infinite active event set, or a continuum limit.

## Exact Law Value Still Does Not Follow

Hold fixed the same homogeneous decoder, motif, collision rule, stage
certificates, phase/settings/link records, causal order, outcome support,
sample instruction, and append permanence. Change only the prepared Werner
visibility:

```text
rho_v = v |Phi+><Phi+| + (1-v) I/4.
```

Both `v=1` and `v=1/2` are normalized and have full support in every tested
context, but

```text
CHSH(v=1)   = 2 sqrt(2),
CHSH(v=1/2) = sqrt(2).
```

One event-addressed sample coordinate separates their records. The companion
`COMPLETE_SAMPLED_LAW_PAIR_AXIOM_UNDERDETERMINATION_NOTE_2026-07-14.md`
changes a different kernel value under an otherwise complete sampled-append
surface. Homogenizing the process therefore does not derive the exact law
value.

## What Was Closed And What Remains

| interface | `CFSI-QH11` result | remaining physics |
|---|---|---|
| placement | local motif decoder replaces enumerated ray/cell addresses | origin of actual program records |
| spatial symmetry | exact translation and 24-proper-cubic covariance | no claim of boost or continuum covariance |
| collisions | local strict-priority winner; ties block | why nature uses that arbiter; liveness under arbitrary programs |
| microstage | two permanent certificates reconstruct four stages | why these atomic maps are physical |
| causal schedule | disjoint event-order invariance | interacting/overlapping quantum events |
| frame | exact `I/S` relational link transport | unrestricted locally generated frame transport |
| state | finite-repertoire record-Markov theorem | full quantum preparation/effect completeness |
| probability | exact trace branch weights and one sample | derivation or selection of those values |
| capacity | each programmed motif reserves finite fresh support | autonomous program growth and indefinite allocator |
| clock | certificate depth orders events | physical duration and rate |
| matter/gravity | no result | all field, mass, chirality, and curvature lanes |

The rule is homogeneous but not self-originating. Boundary/program records
still say which experiments exist, which directions they face, which settings
they use, and which colliding program wins. Removing a hand schedule is not
the same as deriving a cosmological boundary or a universal Hamiltonian.

## Constitutional Consequence

This construction strengthens the law-reference route and weakens the case
for adding witness, read, clock, program-counter, collision, or frame prose to
the Record axiom. All of those process jobs can be outputs of one exact local
record-conditioned law.

A compact interface sentence consistent with the construction is:

```text
From the complete record configuration, one fixed finite-range causal
instrument law determines every local record-forming transition; exactly one
supported branch forms its records, and every later transition preserves
them.
```

But that sentence still does not distinguish visibility `1` from `1/2`, or
one normalized instrument from another. It is an interface, not a complete
physical axiom. A genuine constitutional add would have to identify the exact
canonical law referent, for example in schematic form:

```text
Local possibilities and record-forming transitions are exactly those of L.
```

where `L` is a stable extensional specification that fixes all finite record
transcript laws or a proved unique operational-equivalence class. `CFSI-QH11`
is not yet suitable for `L`: its boundary alphabet, collision priority,
binary link set, exact quantum values, and sample instruction are constructed,
not forced.

## No-Go Discipline: Narrow Claim

The only negative claim licensed here is:

> In the declared link family `{I,S}`, deleting the relational-link record
> violates record-Markov sufficiency: the remaining program records can be
> identical while a future Bell transcript changes. One binary link bit is
> necessary and sufficient for this two-member control.

This is not a no-go for global common-frame laws, dynamically generated
frames, gauge-quotient states, or richer relational records.

### N1 — Alternative-route enumeration

| route | status | result |
|---|---|---|
| restrict every motif to one common frame | `POSITIVE CONDITIONAL` | removes mixed-frame link data by narrowing the law domain |
| one persistent `I/S` link bit | `POSITIVE IN DECLARED FAMILY` | reconstructs both exact transcript tables |
| two noncommuting reference axes | `POSITIVE GENERALIZATION ROUTE` | fixes the twist left open by one pointer axis |
| full `PSU(2)` edge transport | `LIVE` | natural unrestricted link object; exact local generation not supplied |
| global boundary frame | `POSITIVE BUT NONLOCAL INPUT` | predicts relations if transport to every event is proved |
| gauge/operational quotient | `POSITIVE SEMANTIC ROUTE` | removes coordinate copies but not physically distinct relative orientations |
| apparatus compensation using the link | `POSITIVE CONTROL ROUTE` | can realize one desired common-frame effect in different local coordinates |
| infer link from one `Z` pointer record | `NEGATIVE IN EXACT CONTROL` | `I` and `S` act identically on `Z` |
| infer link using an additional `X` reference | `POSITIVE IN EXACT CONTROL` | `SXS*=Y` separates the twist |
| absorb link into an independent wavefunction | `POSITIVE BUT OUTSIDE LIVE STATE TYPE` | predicts correctly only by widening state unless reconstructed from records |

### N2 — Wall-independence audit

The link wall is held separate from three other process-memory jobs:

| datum | exact job | independent control |
|---|---|---|
| phase | which coherent Bell preparation | opposite `XX` response with fixed link |
| stage certificates | which work-state microstage | blank versus prepared state with fixed program |
| priority | which overlapping motif may advance | opposite winners with identical nonpriority records |
| relational link | how Bob's local effects sit in source frame | `2 sqrt(2)` versus `sqrt(2)` with fixed phase/stage/priority |

None is counted as a separate proposed axiom. One exact law and its ordinary
record alphabet may supply all four.

### N3 — Hidden-wall scan

The motif roles, nonce, phase, settings, link, priority, two certificates,
outcomes, work-site blank decoder, atomic transitions, trace weights,
randomizer coupling, and allowed finite alphabet are explicit. Spatial
orientation comes from record geometry. The construction does not credit its
program records, local nonce coloring, or exact quantum response as derived
from the current four axioms.

### N4 — Exact residual matching

The link omission is separated by exact CHSH and individual transcript
probabilities. The phase omission matches the finite `Phi+`/`Phi-` residual in
`CFSI_Q_BELL_COHERENT_CAUSAL_FRONT_LAW_NOTE_2026-07-14.md`. The causal-input
acceptance condition matches
`CAUSAL_SCHEDULE_EQUIVALENCE_WOLFRAM_INSPIRATION_PROBE_NOTE_2026-07-14.md`.
The visibility ablation matches the exact-law-value job independently. None
is used to claim a result about metric time, matter, mass, or gravity.

### N5 — Resolution and rhetoric audit

All matrix and probability checks are exact symbolic calculations. “One bit”
is confined to the two-member link family. “Homogeneous” means one
translation/rotation-covariant local decoder, not an unprogrammed cosmology.
“Record-Markov theorem” is confined to finite well-formed motifs and the
declared finite Bell repertoire.

### N6 — Partial-closure paths

The positive link record closes the finite mixed-frame discriminator. The two
stage certificates close the exposed microstage counter. Static arbitration
closes overlapping support without a global site order. A common-frame domain
could remove the link atom; a full edge-connection law could generalize it;
and a self-propagating program could remove boundary enumeration. These are
preserved as live routes.

### N7 — Strongest steelman

A final quantum cellular law could generate local frames and their connection
from ordinary record geometry, prove flat-holonomy or curvature laws, derive
collision resolution from its algebra, reconstruct every open-process state
from records, and select its Bell/Born values uniquely. Such a law could use
no explicit binary link token and still satisfy record-Markov completeness.
This probe gives it an exact finite acceptance test; it does not rule it out.

### N8 — Cross-cycle echo

`CFSI-Q7` already exposed phase, setting, and causal-program memory. Those are
not counted again. This cycle positively removes the hand-enumerated ray,
makes the microstage certificates executable, and adds one independent finite
residual: a mixed-frame twist invisible to one pointer axis but visible in a
future Bell transcript. The visibility pair repeats the exact-value wall only
as a regression control.

## Verification

Run:

```bash
python3 scripts/cfsi_qh11_homogeneous_local_decoder_probe_2026_07_14.py
```

The PASS count contains related checks and is not a count of independent
scientific facts.

Expected terminal result:

```text
PASS=98
FAIL=0
```

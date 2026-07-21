# Physical three-star shared parity overlap — Cycle 520 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

## Result

Cycle 520 tests the preferred recurrent interpretation of the Cycle-519 tag:
one shared tag for each coarse center,

\[
\tau_A=N_A\pmod2,
\]

reused on every seam incident on that center.  The smallest lawful L5 overlap
is a bent three-center path

\[
A=(1,1,1),\qquad B=(2,1,1),\qquad C=(2,2,1).
\]

Its three seven-cell stars have a sixteen-cell union.  The alternative
straight path has seventeen cells, but at L5 its two outer leaves acquire one
extra periodic edge in every one of the 24 proper-cubic placements.  Cycle
520 therefore uses the bent path at train L5 and held L6 and retains the
straight L5 geometry as a rejection control.

The result has a positive half and a narrow negative half:

1. Three independently appended shared logical tags give an exact bounded
   isometry on the sixteen-cell union, are covariant over the complete
   proper-cubic orbit, and are preserved by the exhaustive logical
   free-plus-contact update.  The direct tagged one-particle mass and contact
   controls pass.
2. The Cycle-519 seven-M2 factor-local parity descriptor does not become
   three simultaneous constraints after the actual Cycle-311/516 cell
   factors are multiplied.  Moreover, no Pauli product in the complete
   retained reference-stabilizer span decodes any center's logical parity on
   this product grammar.  This is a finite-span negative result, not a no-go
   for non-Pauli constraints, new auxiliaries, changed representatives, or a
   staggered implementation.

No axiom is edited and no axiom pressure is inferred.

## Exact three-tag Gram theorem

The bent union has 96 logical modes and

\[
1+96+\binom{96}{2}=4,657
\]

logical configurations through global total number two.  Quotienting only
the sixteen independent vacuum-role toggles gives the exact seed census:

| item | L5 | held L6 |
|---|---:|---:|
| excitation seeds | 433,441 | 433,441 |
| native quotient fibers | 433,399 | 433,399 |
| native singleton fibers | 433,357 | 433,357 |
| native doubleton fibers | 42 | 42 |
| three-tag quotient fibers | 433,441 | 433,441 |
| three-tag singleton fibers | 433,441 | 433,441 |
| maximum tagged fiber | 1 | 1 |

Each center tag equals one on 54,060 seeds.  Across the 42 native doubletons,
the three-bit tag differences are

| XOR mask \((\tau_A,\tau_B,\tau_C)\) | doubletons |
|---|---:|
| `011` | 18 |
| `110` | 18 |
| `111` | 6 |

The displayed bit strings use the runner's integer order, with the least
significant bit assigned to center A.  Every collision therefore differs in
the middle-center tag.  A tag-subset deletion control finds 42 duplicates
with no tags, 18 with A alone, 18 with C alone, and zero with B alone or with
any two tags.  Three tags are not claimed minimal for this finite Gram; all
three are retained because the recurrent architecture assigns one parity tag
to every center and must transport all three independently.

The native branch grammar and amplitudes are unchanged.  The exact branch
inventory is:

| sector | excitation seeds | expanded branches |
|---|---:|---:|
| vacuum | 1 | 65,536 |
| one particle | 960 | 31,457,280 |
| same-cell two particle | 480 | 15,728,640 |
| split-cell two particle | 432,000 | 7,077,888,000 |
| total | **433,441** | **7,125,139,456** |

Per logical column the branch count and squared branch weight are respectively
\(65,536\) and \(1/65,536\) in vacuum, \(327,680\) and
\(1/327,680\) at number one, \(65,536\) and \(1/65,536\) for a
same-cell pair, and \(1,638,400\) and \(1/1,638,400\) for a split pair.
Every column therefore has norm one.  Tagged quotient uniqueness then lifts
through every vacuum-role expansion, so all 7,125,139,456 analytic rows are
unique and

\[
E_{ABC}^\dagger E_{ABC}=I_{4657}
\]

exactly at L5 and held L6.  The runner does not materialize the seven-billion
row set and uses no magnitude cutoff.

## Geometry and all proper-cubic placements

The bent ordered path has a 24-element proper-cubic orbit.  At both sizes,
each placement has sixteen distinct cells and exactly 22 induced geometric
nearest-neighbor edges, with zero extra periodic edges and zero missing
edges.  All 576 products of the 24 frames close.  The straight ordered path
has a six-element orbit; it has 24 raw induced edges, but L5 has 25 torus
edges in every frame.  At L6 the extra edge disappears.  This is why the
straight path is rejected at the required training size rather than treated
as a failed recurrent compiler.

The physical covariance audit maps every native local \(n=0,1,2\) gauge term
on every one of the sixteen cells through every proper frame.  It checks
35,328 local term/frame rows per size, 70,656 across L5 and L6.  Target
lookup, auxiliary transport,
reference-stabilizer normalization, and amplitude covariance have zero
failures.  The center-number tags are scalars under these anchored maps and
move with their centers.  This proves covariance of the bounded tagged
construction; it does not synthesize the frame operation from primitive M2
gates.

## Simultaneous gauge constraints: exact failure of the seven-M2 shortcut

For an isolated Cycle-311 factor, the complete local M64 grammar has 256
terms.  On the sixteen cells, Cycle 520 checks 4,096 factor terms per size
through \(n=0,\ldots,6\).  The parity of the six owned port M2s equals the
factor's logical number parity in every case.  Deleting any one port produces
72 failures on each tagged center.  The Cycle-519 relation

\[
Z_{\tau_A}\prod_{v\in A}Z_v=+1
\]

is therefore an exact seven-M2 factor-local descriptor.

It is not a constraint on the final overlapping product.  Neighboring
Cycle-311/516 representatives also act on a center's nominal port M2s.  Across
the complete \(N\leq2\) local-term grammar, the runner executes 4,416
source-term/target-center tests per size and finds exactly 270 violations:
18 ordered source/target incidences, each contributing 15 failures.  The
three center-owned port sets are pairwise disjoint; target overlap is not the
cause.  The failure comes from cross-factor action on those owned ports.

The exact 433,441-seed census gives the stronger product-shell count:

| failed simultaneous constraints | seeds |
|---|---:|
| none (`000`) | 290,773 |
| A only (`001`) | 44,088 |
| B only (`010`) | 43,890 |
| A and B (`011`) | 3,600 |
| C only (`100`) | 44,088 |
| A and C (`101`) | 3,402 |
| B and C (`110`) | 3,600 |
| all three (`111`) | 0 |

Thus exactly **142,668 / 433,441** seeds violate at least one proposed final
seven-M2 relation at each size.  The mismatch is structural and the L5/L6
histograms agree exactly.

The older physical constraints

\[
D_v=B_vZ_{\mathrm{port}(v)}=+1
\]

remain sound.  The runner checks all 26,496 term/center/port commutators per
size with zero failures.  These constraints make face occupation and its
port tag relationally agree, but they do not isolate one factor's logical
number after overlapping factors are multiplied and hence do not enforce
\(\tau_A=N_A\bmod2\).

## Complete retained Pauli-stabilizer decoder search

Cycle 520 tests whether a corrected Pauli constraint can be assembled from
the full retained reference stabilizer group.  The generator list is
complete for the supplied reference: every local check, all three Wilsons,
every physical \(B_v\) occupation stabilizer, and every port-Z reference
stabilizer.  It contains 2,878 generators at L5 and 4,971 at L6.

For each center, each of the 1,472 local \(N\leq2\) terms supplies a GF(2)
character equation.  Terms are compared with their own cell's canonical
vacuum term, allowing an arbitrary fixed per-cell reference sign.  A solution
would be a retained reference stabilizer whose commutation character is odd
exactly for odd terms of the selected center and even for every other factor.

At both sizes and for all three centers, the coefficient matrix has **rank
147** and the augmented system has **augmented rank 148**.  Explicit reduced
equation combinations of weight five, five, and six give coefficient XOR zero
and right-hand-side XOR one.  Therefore no Pauli product in the complete
retained reference-stabilizer span decodes a center's logical parity on this
sixteen-cell native product grammar.

This statement is deliberately narrow.  It does not cover a non-Pauli local
projector, a new protected auxiliary register, a changed representative, a
different factor schedule, or a constraint supported outside the retained
reference-stabilizer group.

## Shared-tag free-plus-contact update

The union has sixteen physical stream seams: the union of the six seams
incident on each center, with the two center-center seams counted once.  The
32 endpoint modes are all distinct.  A seam FSWAP updates the tag at each
endpoint that is one of the three tagged centers by

\[
\tau_A\longmapsto\tau_A\mathbin\oplus n_a\mathbin\oplus n_b.
\]

The coin exterior lift preserves the number in each cell.  The onsite contact
is diagonal in occupation.  Both therefore preserve every center tag.

The runner exhausts all 4,657 logical configurations through total number two:

- 74,512 single-seam checks with zero tag failures;
- exactly 190 tag-word changes on each of the sixteen seams;
- 4,657 full sixteen-seam schedules with zero tag failures and 2,456 changed
  tag words;
- 4,470,720 pairwise-order checks over all 120 seam pairs, all 4,657
  configurations, and all eight input tag words, with zero final occupation,
  tag, or FSWAP-phase differences.

This is exact logical transport, not a native-shell primitive decomposition.

## Direct mass and contact controls

On the 96-mode one-particle sector, the runner constructs the complete common
Cycle-219 coin followed by all sixteen FSWAPs.  Its unitarity residual is below
the numerical tolerance, the uniform eigenvector residual is below tolerance,
and every nonzero coefficient carries the correct output tag word.  The
recovered mass is

```text
0.45340565417488515
```

against the Cycle-219 fixture

```text
0.4534056541748852,
```

a residual of \(5.55\times10^{-17}\).  Contact is identity at number one.  At
number two it is active on exactly \(16\binom62=240\) same-cell configurations;
deleting the supplied \(g=0.37\) contact gives residual
`0.36789306705608243`.  Contact preserves all three parity tags.

These are direct tagged logical/direct-occupation controls.  They are not a
primitive physical mass retest inside the Cycle-515/516 Wilson branch shell.

## Exact physical candidates versus bookkeeping

Three constructions must not be conflated.

### Fixed postprocessing of the collided native encoding

Cycle 465 supplies the semantics of six CNOTs that compute and uncompute the
parity of six direct occupation M2s.  But applying any fixed unitary \(W\) to
the already-collided native encoding and blank auxiliaries obeys

\[
\bigl(W(E\otimes|0\rangle)\bigr)^\dagger
 W(E\otimes|0\rangle)=E^\dagger E.
\]

It therefore preserves Cycle 518's exact \(1/400\) Gram residual and cannot
write different tags onto one identical native physical row.  A CNOT compute
after native factor multiplication is not the Cycle-519 repair.

### Dense native-shell candidate

For the independently tagged isometry, the bounded algebraic unitary

\[
A_\tau=E_{ABC}GE_{ABC}^\dagger+I-E_{ABC}E_{ABC}^\dagger
\]

is exact, unitary, and satisfies the desired intertwiner on the declared code.
It is the native-shell `G_physical` candidate.  It imports the dense code
projector, branch-shell matrix units, off-code identity completion, and tag
preparation before factor information is lost.  It is therefore a supplied
bounded physical-shell completion, not a primitive M2 compiler.

### Protected-shadow block-local candidate

A more constructive route appends six private occupation M2s to each coarse
cell and one shared tag M2 per center.  Let

\[
W=\prod_A\prod_{d=0}^5\operatorname{CNOT}(q_{A,d}\rightarrow\tau_A).
\]

On the direct occupation register, define

\[
G_\tau=W\,(G_{\rm direct}\otimes I_\tau)\,W^\dagger.
\]

This is an exact block-local circuit identity: uncompute the old parities,
apply the cell coins, sixteen seam FSWAPs, and fifteen contact phases per cell,
then compute the new parities.  The three parity blocks use 18 CNOTs.  Deleting
any one compute CNOT corrupts exactly 96 of the 4,657 valid configurations;
deleting its matching uncompute leaves the same number of tag errors.

This candidate is genuinely more than logical tag bookkeeping on the direct
occupation/shadow register.  It is not yet the requested native Wilson-shell
compiler.  It adds six protected M2s per cell, does not synchronize those
shadows with the Cycle-515/516 branch shell, and the Cycle-219 six-mode coin
still lacks an explicit bare one- and two-M2 gate decomposition and routing
trace.  Cycle 465 supplies parity-compute semantics, not those missing pieces.

## Lawful domain, leakage, deletion, and resources

The lawful theorem is the bent three-center path at L5 and held L6, the
sixteen-cell union, all 24 proper-cubic placements, and global total number at
most two.  The runner rejects the straight path at L5, determinant--1 frames,
duplicate or non-neighbor path steps, and number above two.  No boundary or
thermodynamic-limit inference is made.

Deletion controls include:

- all three tags deleted: 42 quotient duplicates;
- A alone or C alone: 18 duplicates; B alone or any two tags: zero;
- any factor-local port deleted: 72 descriptor failures;
- fixed postprocessing CNOT: the native \(1/400\) Gram residual remains;
- any protected-shadow parity CNOT deleted: 96 valid-configuration errors;
- contact deleted: residual `0.36789306705608243` on 240 active pair states;
- straight path forced at L5: one extra periodic edge in each frame.

The literal 7,125,139,456-row census is not executed.  The target has a hard
1,200-second wall, a 3 GB checkpoint ceiling, and a zero-swap gate.  Partial
in-memory rows are not durable across an OS kill or process OOM.  The final
target runs each heavy exact stage in a fresh interpreter so allocator history
cannot masquerade as simultaneous scientific memory demand.  It passes all
11 certificate predicates in 231.006 seconds; the largest per-stage RSS is
307,232,768 bytes and every stage reports zero swap.

## Supplied structure and exact claim boundary

The complete supplied inventory is:

| supplied object | Cycle-520 use | unresolved import |
|---|---|---|
| Cycle-311/315 common M64 factors | native representatives, carrier/variant grammar, amplitudes | primitive preparation and factor application |
| Cycle-515 all-order shell | exact finite product grammar and dense on-image completion | dense projector, matrix units, lawful role preparation |
| Cycle-516 Koszul frame bridge | physical term transport and proper-frame reference repair | primitive frame correction |
| corrected Cycle-519 semantics | independent logical tag; seven-M2 relation only factor-local | recurrent constraint and native-shell tag preparation |
| Cycle-465 parity control | six-CNOT compute/use/uncompute semantics | nearest-neighbor routing and native-shell applicability |
| Cycle-219 coin | common six-mode matrix and mass fixture | bare one-/two-M2 decomposition |
| Cycle-230/Cycle-269 contact | \(g=0.37\), fifteen commuting pair factors | full recurrent native-shell assembly |
| fixed-Wilson reference | stabilizer span and vacuum phase reducer | absolute preparation |
| global \(N\leq2\) cutoff | exact finite code domain | full-number extension |

Cycle 520 hash-binds the stable Cycle-515, 516, and 518 runner/note pairs.  It
does not freeze the concurrently corrected Cycle-519 files.  Instead it gates
on their corrected semantic contract: the parity descriptor is factor-local,
the final overlapping seven-M2 constraint is not claimed, and fixed-unitary
postprocessing does not repair the native Gram.

The strongest exact statement is:

> On the bent sixteen-cell, global-\(N\leq2\) three-star union at L5 and held
> L6, three shared center-number parity tags give 433,441 singleton quotient
> fibers, 7,125,139,456 unique analytic rows, and exact Gram
> \(I_{4657}\).  The tags transform over all 24 proper-cubic placements and
> are preserved by the exhaustive logical free-plus-contact schedule, mass,
> and contact controls.  The factor-local seven-M2 descriptor fails on
> 142,668 seeds after native factor multiplication, and the complete retained
> reference-stabilizer Pauli span has rank 147 versus augmented rank 148 for
> every center at both sizes.

This does not establish a primitive native-shell
\(G_{\rm physical}\), a globally enforced local tag constraint, full number,
or recurrent volume beyond three centers.

## N1–N8 no-go discipline

Gate status for a broad impossibility, minimum-content, or axiom-pressure
claim: **FAIL / DO NOT SHIP**.  The disposition is
`partial-attempt-with-named-untested-routes`.  Only the complete retained
reference-stabilizer Pauli family is exhaustively closed.

### N1 — alternative-route map

The normalized approach families differ in primary object and terminal proof
obligation:

1. **Naive seven-M2 final constraint — ATTEMPTED.**  It is correct on all
   4,096 isolated factor terms but fails on 142,668 final-product seeds.
2. **Complete retained reference-stabilizer Pauli decoder — ATTEMPTED.**  The
   full GF(2) system is inconsistent with rank 147 and augmented rank 148 at
   both sizes.
3. **Dense non-Pauli code projector — ATTEMPTED.**  The displayed
   \(A_\tau\) is an exact bounded algebraic completion, but primitive support
   and enforcement are supplied.
4. **Protected-shadow auxiliary gauge — ATTEMPTED.**  The 18-CNOT conjugation
   gives an exact direct-register candidate; synchronization with the native
   shell and the bare coin decomposition remain untested.
5. **Staggered compute/use/uncompute tag — UNTESTED / LIVE.**  A transient tag
   written before neighboring factors act may avoid a final static Pauli
   decoder, but coherent schedule closure and terminal isometry must be shown.
6. **Changed representative/opposite carrier — UNTESTED / LIVE.**  It can
   remove the native collision before tagging but must re-earn dense-star,
   frame, contact, mass, and recurrence fixtures.
7. **Non-Pauli bounded local constraint — UNTESTED / LIVE.**  A projector or
   subsystem-gauge relation outside the stabilizer span may decode parity on
   the overlapping shell and needs an explicit primitive decomposition.

The live mechanisms make a broad no-go premature.  The finite-span statement
survives because the runner exhausts every member of precisely that span.

### N2 — wall-independence audit

The surviving walls collapse to:

- **W_constraint:** a simultaneously enforceable local correlation between
  each tag and native overlapping-shell logical parity;
- **W_native-update:** a primitive tagged update and off-code completion on
  the native Wilson shell, including the physical mass retest;
- **W_coin:** a bare one-/two-M2 decomposition and routing trace for the
  supplied six-mode coin;
- **W_volume:** compatibility of shared tags and schedules beyond the tested
  three-center overlap.

The protected-shadow/native synchronization question belongs to
W_native-update.  The physical mass retest is downstream validation of the
same wall rather than a fifth independent wall.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| W_constraint / W_native-update | no | no | yes |
| W_constraint / W_coin | no | no | yes |
| W_constraint / W_volume | no | no | yes |
| W_native-update / W_coin | no | yes, if “native update” includes a bare decomposition | no; W_coin is collapsed into a strict native-update claim |
| W_native-update / W_volume | no | no | yes |
| W_coin / W_volume | no | no | yes |

For clarity, the final collapsed set is **W_constraint, W_native-update,
W_volume**; W_native-update explicitly includes the coin decomposition and
physical mass validation.  The table records why W_coin is not reported as an
independent wall.

### N3 — hidden-wall scan

The proof uses no silent parity service, factor ordering, host-selected seam,
or continuum bridge.  “Supplied” items are listed in the inventory.  The
terms “constraint,” “physical candidate,” “primitive,” “covariant,” and
“mass” are resolved separately for the factor, final product, direct shadow
register, dense native shell, and bare-gate levels.  Cycle 519 is read through
its corrected factor-local semantic contract rather than a moving file hash.
The only contextual uses of “reference” name the explicitly supplied
fixed-Wilson stabilizer state and its complete generator span.

### N4 — residual matching

| cited witness | witness residual | Cycle-520 residual | match? |
|---|---|---|---|
| Cycle 518 compressed Gram | native adjacent-star overlap \(1/400\) | fixed-unitary postprocessing cannot alter that same Gram | yes |
| corrected Cycle 519 overlap countercontrol | factor-local parity fails as final two-star constraint | same failure tested on the larger three-star product | yes, extended rather than substituted |
| Cycle 515 | dense bounded \(A_\pi\) supplied, primitive synthesis open | dense \(A_\tau\) versus primitive native update | yes |
| Cycle 516 | bounded proper-frame shell, dense correction supplied | all-frame term transport, no primitive frame synthesis | yes |
| Cycle 465 | direct Q1 six-CNOT parity control | protected direct-register candidate only | yes; not evidence for native-shell CNOT synthesis |
| Cycle 269 contact | fifteen physical projector factors | direct contact and deletion control | yes for contact; no claim about full update assembly |

No source, response, time, Record, Born, or gravity residual is cited against
the overlap constraint.

### N5 — rhetoric audit

“No Pauli decoder” means no product in the complete retained
reference-stabilizer span for one selected center on this sixteen-cell
\(N\leq2\) grammar.  It does not mean no per-mode operator, no non-Pauli
projector, no enlarged block constraint, and no lattice-wide construction.
“Not a simultaneous constraint” is tested at factor, local-term product, and
complete seed resolutions at L5/L6; it is not extrapolated to changed
representatives.  “Physical candidate” is qualified as dense native-shell or
protected direct-register.  Neither is called a completed primitive recurrent
compiler.

### N6 — partial-closure path

The independently appended three-tag encoding already closes the static Gram
and logical transport without an axiom change.  The protected-shadow route
gives a second explicit partial closure with constant overhead and a CNOT
conjugation identity.  A non-Pauli projector or transient staggered tag can
retire W_constraint while keeping the same falsifiable substrate.  No
definition refactor is being promoted as physics, and no new axiom is required
by the evidence.

### N7 — hostile steelman

A hostile reviewer should reject any recurrent-obstruction claim.  The GF(2)
certificate closes only Pauli products drawn from one supplied stabilizer
group.  Cycle 515 already demonstrates that dense transported projectors can
enforce code relations that role-only constraints miss, while the protected
shadow construction gives an actionable local alternative: allocate six
private occupation M2s per cell, use the explicit 18-CNOT parity conjugation,
decompose the common coin into bounded two-M2 gates, and synchronize the
shadow with the Wilson shell.  The terminal obligations are concrete—an
explicit local projector or synchronization circuit, its off-code completion,
and a four-or-more-center recurrence test—so the broad negative is premature.

### N8 — cross-cycle echo

Cycles 311 and 315 repaired local and adjacent-cell collisions by retaining
carrier, stream, and relational roles.  Cycles 515 and 516 repaired role-only
and bare-frame failures with transported code projectors and the Koszul
character.  Cycle 519 repaired the adjacent-star Gram with an independently
appended logical tag, then corrected its seven-M2 statement to factor-local.
Those precedents show that a failed simple stabilizer is often repaired by a
larger relational shell.  Cycle 520 therefore keeps non-Pauli, protected
shadow, staggered, and changed-representative routes live and reports no
shared-substrate obstruction.

## Dependency impact and next campaign

| wall | Cycle-520 change | remaining obligation |
|---|---|---|
| \(C_{\rm ref}\) | unchanged; fixed-Wilson reference and stabilizer span remain supplied | absolute preparation or replacement |
| \(C_{\rm num}\) | advanced: three shared center parities are exact through \(N\leq2\) | full number and primitive tag initialization |
| \(C_{\rm wrap}\) | sharpened: bent path is lawful at L5/L6; straight L5 has one extra edge per frame | larger-volume and boundary controls |
| \(C_{\rm int}\) | advanced: sixteen-seam transport, contact, order independence, and direct mass pass | primitive native-shell update and physical mass retest |
| \(C_{\rm local}\) | split result: three-tag isometry/covariance closes, simple simultaneous Pauli constraint fails exactly | non-Pauli or protected-shadow local enforcement |
| \(C_{\rm source}\) | unchanged | autonomous source/response prediction bridge |

The optimal next campaign is a two-route primitive tournament.  Route A
should construct the smallest non-Pauli bounded projector or subsystem gauge
that correlates \(\tau_A\) with native logical parity while preserving all
three overlapping centers.  Route B should implement the protected-shadow
candidate, including an explicit Givens/two-M2 decomposition of the common
coin and a synchronization map to—or principled replacement of—the Wilson
shell.  Both routes should extend to a four-center plaquette/tree fragment,
retain all proper frames, rerun the complete Gram and leakage controls, and
perform the primitive physical mass/contact retest.

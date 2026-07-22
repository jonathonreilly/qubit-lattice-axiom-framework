# Physical same-code higher-form fermion encoding tournament — Cycle 622

Date: 2026-07-22
Authority: none
Audit: unset
Constitutional effect: none
Classification: partial-attempt-with-named-untested-routes

Cycle 622 is a constructive compiler tournament, not a constitutional edit.
It changes no axiom, foundation, Qualification, primitive, registry, policy,
queue, or audit surface. There is no axiom pressure.

## Exact target contract

The target is one common physical code on M2 sites—the same code for every
route—one concrete encoding
`E`, and one physical update `G_physical` such that

`E G_coarse = G_physical E`

for the complete Cycle-230 six-mode Fock space. The quantifier includes
odd/even coherent superpositions and every finite-density local occupation,
not merely an even algebra or a fixed number sector. The physical word must
have constant overhead, literal support-two nearest-neighbor primitives,
locally enforced auxiliaries, all 24 proper-cubic frames, all 576 frame
conjugations, L3/L6/L7 seams, and the pinned one-particle mass, contact, seam,
factor order, deletion, malformed, leakage, and held-size controls.

The following do not count as closure: an abstract rank match; a direct sum
over unselected Wilson sectors; a basis permutation without CAR phases; a
geometric word in a different encoding; or a reversible preparation that
only moves syndrome information into archive garbage.

## Frozen shore and common register

The accepted Cycle-610 and Cycle-617 runners, notes, receipts, and cold
transcripts are byte-pinned. Their authority remains none and audit remains
unset.

All three new routes are embedded in one declared frame-free 31 M2 role
register per 129^3 coarse supercell:

- six data roles on the radius-64 face shell;
- six preparation-syndrome roles on radius 63;
- six syndrome-archive roles on radius 62;
- six redundant edge-gauge roles on radius 24;
- six redundant face-gauge roles on radius 32;
- one scalar cell-parity role at the center.

The role sets are closed under all 24 frames and all 576 products. Each
syndrome/archive pair is a literal nearest-neighbor edge. Edge and face gauge
bits use covariant half roles paired across cell boundaries; their bounded
paths contain at most 82 and 66 sites respectively. No 24-one-hot orientation
is used. This is covariance of supplied radial role shells, not derived role
genesis: the coarse centers, shell labels, and initial blank M2s remain
imports.

## Route A — standard cubic Z2 edge/face higher form

### Constructive local charge isometry

Route A first builds a genuine local both-parity isometry

`|n_0...n_5>|0> -> |n_0...n_5>|sum_i n_i mod 2>`.

All 64 occupation words, including 32 even and 32 odd words, pass. A random
odd/even coherent state retains norm. The opposite-parity malformed center
bit is detected for all 64 words, and deleting one parity-copy gate fails on
exactly 32 words.

For every direction and every one of the 4096 two-cell occupation words, the
physical endpoint swap is accompanied by the four local parity toggles
needed to update the two cell-center parity bits. The occupation and cell
parity update intertwines exactly and is its own inverse. The endpoint swap is
literal nearest neighbor. Each of the four parity-CNOT descriptors has an
explicit move/apply/restore nearest-neighbor path through the common geometry;
the longest such path contains 66 sites. This establishes bounded
support-two primitive routing, not a compiled full-CAR gate. The blank center
bit is still an explicit initial-state import.

This is a stronger constructive result than Cycle 617 at occupation/parity
resolution. It is not yet the fermionic phase part of `E`.

### Edge/face complex and Wilson sectors

The attempted sign substrate is the standard periodic cubic Z2 chain
complex

`C3 --d3--> C2 --d2--> C1 --d1--> C0`.

The runner constructs every incidence row and checks `d1 d2 = 0` and
`d2 d3 = 0`. For `N=L^3` on L3, L6, and L7 it obtains

- `rank(d1)=N-1`;
- `rank(d2)=2N-2`;
- `rank(d3)=N-1`;
- `dim H1=3` and `dim H2=3`.

The three axis Wilson cycles have support `[L,L,L]`, are closed, and increase
the local face-boundary span by exactly three. Local face constraints
therefore preserve all eight H1 flux sectors but fail to select one. This is
not a failure of local checkability: face boundaries have weight four and
cube boundaries weight six. It is the exact topological-sector residual of
this standard cubic Z2 family.

The complete L3 vertex/edge/face/cube action is tested under all 24 frames and
all 576 compositions; L6/L7 here check the exact chain ranks, compositions,
and Wilson support rather than rerunning the full frame enumeration. Each
logical edge or face bit is represented by equal directed half roles in its
two neighboring cells; that redundant constraint family is also covariant and
has a literal bounded support-two routing.
Preparing it still imports one blank target half. Deleting one equality admits
64 explicit malformed boundary-star words. Across all 4096 assignments of the
six current-cell halves and their six distinct neighbor halves, 4032 malformed
words are detected; the same exhaustive control applies separately to the
edge and face families.

Disposition: retain the local charge `E`, reversible occupation update, and
exact H1/H2 census. Route A does not furnish the common full-CAR `E` or `G`:
it neither identifies the eight Wilson sectors locally nor supplies the
missing fermionic stream phase.

This result is scoped only to the standard cubic Z2 cellular complex;
non-Abelian and higher-group constructions remain live.

## Route B — occupation-diagonal non-Pauli/qudit dressing

Route B attacks the Cycle-617 sign residual without assuming the direct basis
is final. Let `S=B A` be the exact one-particle stream. For a diagonal encoding
phase `(-1)^q`, exact conjugacy of the intrinsic exterior lift and a physical
two-layer swap word requires

`q(n)+q(Sn)=p_Gamma(S)(n)+p_physical(n) mod 2`.

The runner decomposes every unordered mode pair into its exact orbit under
`S` and solves this cocycle equation orbit by orbit. Mode permutations preserve
algebraic-normal-form degree. Because the target is quadratic and its
zero/one-particle terms agree, its degree-two equation is an independent
necessary block; whenever that block is soluble, the quadratic solution alone
solves the full target. Exhausting every pair coefficient therefore decides
existence for an arbitrary occupation-diagonal phase, not only for a guessed
quadratic ansatz.

The four phase choices are tested explicitly:

1. ordinary A swap and ordinary B swap;
2. ordinary A swap and B fSWAP;
3. A fSWAP and ordinary B swap;
4. A fSWAP and B fSWAP.

The two residuals are kept separate.

- On even L6, all four choices have exactly 216 inconsistent pair orbits.
  The XOR of the required phase around each witness orbit is one, so no
  diagonal occupation-basis dressing exists for those tested words at L6.
- On odd L3 and L7, the equal-phase choices are algebraically consistent, but
  the smallest possible maximum torus separation in `q` is respectively 3
  and 9. The required separation reaches the torus diameter and grows with
  held size. The mixed-phase choices are already inconsistent: 81 orbits on
  L3 and 1029 on L7.

Deleting one selected pair phase changes its explicit two-particle witness.
All four choices preserve the one-particle action, and diagonal phases commute
with the onsite contact. The onsite coin conjugation is not reached on L6;
on odd sizes the dressing is already lattice-scale and does not give a
bounded coin word.

Disposition: retain the exhaustive four-choice orbit classification. The
L6 algebraic inconsistency and the odd-size non-bounded separation are
route-specific diagnostics. They are not a general non-Pauli/qudit
obstruction; non-diagonal matrix-valued auxiliaries remain UNTESTED_LIVE.

## Route C — autonomous local code-preparation QCA

Route C tests a literal one-layer preparation primitive on the same role
register. Six simultaneous support-two nearest-neighbor swaps implement

`|s>|0_archive> -> |0_syndrome>|s_archive>`.

All 64 syndrome words, their coherent superpositions, the inverse, number
conservation, all 24 frames, all 576 products, and L3/L6/L7 pass. Deleting one
swap leaves an explicit nonzero syndrome. Every one of the 63 nonblank
malformed archive inputs leaks back into the syndrome shell.

The map is reversible precisely because all archive garbage is retained. The
inverse gives renewal of the blank archive only by restoring the malformed
syndrome. A proposed reset that kept the syndrome blank and also erased the
archive would map 64 orthogonal inputs to one output; its Gram residual is
`sqrt(64*63)`, so it is not the tested unitary QCA. A dissipative reset or
entropy sink would be a new explicit resource import, not something generated
by this schedule.

Disposition: retain the exact reversible transfer and its physical compiler.
Route C does not autonomously prepare the common code from arbitrary M2
states, and it does not preserve unknown matter while renewing every
auxiliary. The blank archive remains an import.

This result is scoped only to one reversible archive construction;
open-system and resource-bearing preparation routes remain live.

## Prior-art and novelty boundary

No literature novelty is claimed for periodic cubic cellular homology,
occupation-diagonal cocycle conjugation, repetition encoding, or reversible
swap-to-archive schedules as mechanism classes. The Cycle-622 contribution is
the executable conjunction at this campaign's exact contract: one declared
31-role M2 layout, exact L3/L6/L7 orbit counts for the four phase words,
route-scoped all-24/all-576 covariance controls, and the explicit refusal to
join the three partial constructions into a compiler. No external prior-art
engine is used as a premise of the finite calculations.

## Fixtures, factor order, and supplied structure

The byte-pinned Cycle-610 one-particle mass, local contact, and Cycle-230 seam
fixtures pass. The accepted order remains

`onsite coin -> A -> B -> onsite contact`.

Factor deletion and noncommutation witnesses remain nonzero. The local coin
and contact are unitary, and contact is identity on the zero/one-particle
sector. These are preservation checks, not new selections of beta, contact
coupling, factor order, or angle precision.

The complete import inventory is:

- 129^3 supercell centers and radial role-shell labels;
- blank parity, gauge, syndrome/archive, and routing M2s;
- the Cycle-230 CAR target, beta, contact coupling, factor order, and angle
  precision;
- periodic boundary conditions and the L3/L6/L7 size labels;
- initial/boundary-state selection;
- any reset bath, dissipative sink, or measurement resource.

Factorization stages are not interpreted as time, wrapped phase is not called
physical energy, no generator element is called a rate, and no syndrome
archive is called a Record.

## Same-code disposition

The common register exists, but the routes do not supply one common code
isometry. Route A supplies local occupation/parity `E` but no Wilson-sector
identification or CAR phase. Route B supplies no bounded held-size diagonal
phase `E`. Route C transfers syndrome into nonblank archive rather than
preparing and renewing the full auxiliary state. Therefore the strict
`E G_coarse = G_physical E` compiler is not claimed.

The strongest constructive result is the combined but unjoined package: a
bounded both-parity local charge isometry and reversible occupation stream,
an exact covariant H1/H2 census, and an exhaustive diagonal stream-cocycle
classification. Calling those one compiler would repeat the false-join error
that the Cycle-622 contract forbids.

## Updated dependency ledger

- `C_ref`: unchanged; role-shell centers, reference, and phase conventions
  remain supplied.
- `C_num`: advanced at local both-parity occupation/charge resolution; the
  full CAR phase isometry remains open.
- `C_wrap`: the seam fixture passes; Wilson/spin-structure selection remains
  open.
- `C_int`: contact passes; beta, coupling, factor order, and precision remain
  supplied.
- `C_local`: sharpened by exact H1/H2 and diagonal-cocycle residuals; one
  same-code local fermion compiler remains open.
- `C_source`: unchanged; no reset bath or autonomous preparation source law
  is derived.

Maturity remains operational quantum/records 3.0, causal time 2.0,
inertia/matter 3.5, gravity/source 2.5, and Born/probability 1.5.

## Fresh no-go discipline

The origin/main no-go-discipline skill is newer than the installed copy and
is followed here. Approach families are normalized by mathematical object,
mechanism, and terminal obligation.

### N1 — normalized alternative families

Three families are ATTEMPTED here: the standard cubic Z2 cellular complex,
occupation-diagonal phase dressing, and reversible archive QCA. The prior
rough-terminal Pauli subsystem and direct endpoint encoding are RULED OUT BY
PRIOR only at their exact Cycle-617 scopes. Two materially different families
remain UNTESTED_LIVE: non-diagonal non-Abelian/higher-group link auxiliaries,
and dissipative or measurement-reset preparation with an explicit resource
law. Therefore the N1 gate for a negative theorem fails.

### N2 — wall-independence audit

The collapsed current walls are Wilson/flux handling, full-Fock phase,
renewable preparation, literal same-code NN composition, and physical role
genesis. All ten pairs are recorded. At current evidence none automatically
closes another.

### N3 — hidden-condition scan

“Standard cubic Z2” is an explicit family restriction. Frame-free radial
shells promote role genesis to an explicit wall. Blank archive promotes
renewal to an explicit wall. Supplied beta, coupling, order, and precision
remain named imports outside the novelty claim.

### N4 — residual matching

Cycle 617's three Wilson selectors match Route A's three H1 generators.
Cycle 617's direct B-sign residual does not exactly match Route B's full-S
diagonal cocycle and is not used as its proof. Cycle 312's higher-number sign
residual is also only a cross-cycle echo, not a matching witness.

### N5 — resolution audit

Route A covers one standard Z2 cellular complex, not all higher-form theories.
Route B covers every occupation-diagonal phase for four physical phase words
at L3/L6/L7, not non-diagonal qudits. Route C covers one reversible archive
QCA, not open-system preparation. Every negative sentence is narrowed to
those resolutions.

### N6 — partial-closure paths

A non-Abelian/higher-group auxiliary link field and a resource-accounted local
reset channel are live constructive paths. They are possible bounded imports
with retirement audits, not automatic requests for a new axiom.

### N7 — steelman

A hostile reviewer can combine a non-diagonal matrix-product or PEPS fermion
encoding with dynamical spin-structure auxiliaries, then use a
resource-accounted local dissipative encoder to prepare the gauge state. The
terminal obligation is an explicit 31-M2-or-smaller `E` and `G` whose tensors
satisfy the stream cocycle and whose reset channel has a framework
source/resource law. Cycle 622 does not test that mechanism.

### N8 — cross-cycle echo

Cycles 248, 251, 261, 276, 312, and 617 recur on parity, Wilson, and sign
residuals. But Cycle 617 already retired the exactly-one restriction at
even-algebra resolution. That history demonstrates partial retirement, not a
route-independent obstruction.

The N1 negative gate is FAIL, as it should be. Cycle 622 ships only as a
partial-attempt-with-named-untested-routes. It asserts no no-go, minimum
content, shared obstruction, or axiom pressure.

## Optimal next campaign

Construct one non-diagonal matrix-valued link/qudit encoding with dynamical
spin-structure auxiliaries on the same literal layout. Require a complete
tensor/isometry, exact local CAR-even update, all 24/all 576 covariance, and
L3/L6/L7 odd/even coherent tests. If preparation requires reset, specify the
local quantum channel and its source/resource law and keep the reset import
visible rather than claiming autonomous archive renewal.

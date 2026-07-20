# Physical elementary divide-six nearest-neighbor compiler — Cycle 467 note (2026-07-19)

**Authority: none. Audit: unset.**

## Frozen question and bounded answer

Can the exact word block left unsynthesized by Cycle 463 be compiled literally:
six retained **249-bit** neighbor words plus the central `D=6^96` source term,
exact division by six on the lawful code, XOR into the retained target, complete
work reset, an explicit inverse, and nearest-neighbor routing within the existing
scale-40 physical-M2 supercell?

Cycle 467 gives a bounded positive answer at the declared input ports.  It
enumerates a complete NOT/CNOT/Toffoli circuit, streams every routed elementary
event through a nearest-neighbor verifier and digest, and carries that full
schedule through all 24 proper-cubic frames.  The arithmetic uses **762
computational work** M2; the unused 763rd bit means the existing **763-M2
allowance** suffices without enlargement.

The result retires Cycle 463's precise primitive arithmetic-synthesis gap.  It
does not derive the Jacobi law, `D`, a source interpretation, a field law, or a
clock/gravity relation.  Six neighbor words, the source bit, and the retained
target are declared ports, not extra work.  Transport from canonical word
storage in adjacent supercells to these ports remains outside this runner.

Iteration count and circuit depth are not time.  The source bit, wrapped phase,
gate count, and generator elements are **not energy, stress, lapse, metric,
proper time, backreaction, or gravity**.  No axiom, foundation, Qualification,
primitive, registry, policy, queue, or audit-status file is changed.

## Complete logical compiler

Write `B=249`, `W=B+3=252`, and retain Cycle 463's `D=6^96`.  The live
computational work is:

| register | M2 |
|---|---:|
| `W`-bit accumulator | 252 |
| `B`-bit source mask | 249 |
| three shared high-zero addend pads | 3 |
| Cuccaro carry | 1 |
| division remainder | 3 |
| `W`-bit quotient scratch | 252 |
| clean multi-control synthesis auxiliaries | 2 |
| **computational total** | **762** |
| unused bit in Cycle 463 allowance | 1 |
| **declared allowance** | **763** |

The `W`-bit accumulator cannot overflow for the declared inputs because the
numerator is below `7*2^B`, while `2^W=8*2^B`.  Each of the six neighbor words
and the source-mask word is added with a Cuccaro ripple adder.  The adder uses

```text
MAJ(a,b,c) = CNOT(a,b); CNOT(a,c); TOFFOLI(c,b,a)
UMA(a,b,c) = TOFFOLI(c,b,a); CNOT(a,c); CNOT(c,b)
```

from low to high bit and back.  It restores the addend and carry exactly.
The source bit CNOT-loads the one bits of `D` into a blank mask, the mask is
added as the seventh operand, and the mask is unloaded.

### Totalized division step

Long division scans the 252 accumulator bits from most significant to least.
For lawful incoming remainder `r in {0,...,5}`, retained input bit `x`, and
blank quotient bit `q=0`, it maps

```text
t = 2*r + x
(r, x, 0) -> (t mod 6, x, floor(t/6)).
```

The 12 required rows are completed to this explicit permutation of all 32
five-bit basis states:

```text
(0,2,4,16,18,20,1,3,9,11,13,25,27,29,5,6,
 7,8,10,12,14,15,17,19,21,22,23,24,26,28,30,31)
```

The completion is not a new physical law.  It is a deterministic reversible
totalization off the Cycle 463 exact-divisibility code.  Gray-path basis
transpositions synthesize the permutation.  Each four-control NOT is decomposed
into five Toffoli gates with two clean auxiliaries; negative controls are
implemented by surrounding NOT gates.  The resulting fixed step has **1,191**
elementary gates: 656 NOT, zero CNOT, and 535 Toffoli.  The executable tests
**all 32** input states and both auxiliary outputs.

After all 252 steps, the low 249 quotient bits CNOT into the target.  Reversing
all division gates clears quotient and remainder; reloading the source mask,
reversing the seven additions, and unloading the mask clears the remaining
work.  Thus the declared map is

```text
|n0,...,n5,s,t,0_work> ->
|n0,...,n5,s,t XOR floor((sum ni + D*s)/6),0_work>.
```

On the lawful Cycle 463 code the remainder is zero, so floor division equals
exact division.  The exact inverse is the complete gate list in reverse order,
because NOT, CNOT, and Toffoli are self-inverse.

The full-width logical transcript contains:

| item | count |
|---|---:|
| NOT | 330,624 |
| CNOT | 14,657 |
| Toffoli | 276,696 |
| **total / sequential depth** | **621,977** |
| ASAP dependency depth | 377,010 |
| trace SHA-256 | `22926a2f0a308f514a299008568a837a064f62bb2cb7c3711b2e6eabc3d9adb5` |
| inverse-trace SHA-256 | `ba225b701b32df6d869e5c3073697c557cbb3ce100fddc34eb05207419e07005` |

These counts are construction counts, not minima.

## Nearest-neighbor physical route

The route places the 1,494 read-only neighbor-port bits, source, 249-bit target,
and 763 declared work bits—2,507 logical wires/ports in total—on the first
2,507 vertices of a Hamiltonian snake through one `40^3=64,000` M2
supercell.  Consecutive snake vertices are cubic nearest neighbors.

Each nonlocal CNOT is routed by adjacent SWAPs, applied on one edge, and routed
back.  Each Toffoli's three wires are stably gathered onto a consecutive
three-vertex path, applied there, and returned.  Every SWAP is explicitly
expanded into three adjacent CNOTs.  To prevent repeatedly moving the five-bit
division head across the full tape, the head is block-swapped through one bit
cell after each forward step, then block-swapped back during uncomputation.
This leaves the canonical physical placement exactly restored.

The runner emits and checks every resulting primitive event; the route is not
only a macro count:

| routed quantity | value |
|---|---:|
| NOT | 330,624 |
| nearest-neighbor CNOT | 12,111,893 |
| connected-path Toffoli | 276,696 |
| **elementary events** | **12,719,213** |
| adjacent SWAPs before decomposition | 4,032,412 |
| routed ASAP dependency depth | 8,120,016 |
| adjacency failures | 0 |
| final placement failures | 0 |
| routed transcript SHA-256 | `4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457` |

The route uses the existing physical sites, not extra computational work
registers.  In Cycle 463's target supercell the six staged input ports add
1,494 occupied routing sites to the prior 44,627-site active inventory, for
46,121 occupied sites, below 64,000.  Port staging begins and ends in its
declared code placement; the physical communication process that places
neighbor words at those ports is still an explicit residual.

The inverse routed program is the routed event stream in reverse order.  A
separate width-one exhaustive test executes the expanded nearest-neighbor
trace itself for every input/source/target state, rather than inferring its
semantics from the router bookkeeping.

## Proper-cubic covariance

The Hamiltonian route is defined inside coordinates `[0,39]^3`.  For a signed
proper-cubic permutation, positive axes map `p -> p` and negative axes map
`p -> 39-p`; this is the affine action about the supercell center.  The runner
constructs all 24 determinant-`+1` frames and checks every edge of the occupied
Hamiltonian path under every frame.  Each image stays in the scale-40 cube and
remains a nearest-neighbor edge.  A Toffoli on three consecutive path vertices
therefore remains a Toffoli on a connected three-vertex path.

Every one of the 12,719,213 events is carried by this fixed affine map.  The
runner records 24 distinct frame manifests derived from the complete routed
transcript, event count, and frame matrix.  Gate covariance is not inferred
from invariant scalar output.

## Exact tests and residuals

The cold runner demands:

1. the five-bit divider permutation is bijective and its 1,191-gate synthesis
   matches every one of all 32 states with both clean auxiliaries reset;
2. the complete compiler is exhaustive at widths one and two, including every
   one of 256 and 32,768 neighbor/source/target combinations, all six possible
   remainders, arbitrary target seeds, and final work reset;
3. the literal expanded nearest-neighbor width-one circuit matches all 256
   states and has zero work leakage;
4. **every 14,592** actual Cycle 463 train/held local operation—2,592 train and
   12,000 held—passes the same fixed compiled long-division permutation with
   zero quotient mismatch and zero divisibility remainder;
5. six representative actual 249-bit rows spanning train/held, early/middle/
   late schedule positions execute the entire 621,977-gate logical circuit and
   inverse with exact E/G output, input retention, and blank work;
6. seeded invalid numerators with remainders 1 through 5 totalize to the correct
   floor quotient/remainder and clean up exactly, while Cycle 463's strict
   decoder refuses each one;
7. the complete full-width nearest-neighbor route has zero adjacency and final
   placement failures in all 24 carried frames.

The all-row replay uses the same explicit 32-state permutation synthesized and
exhaustively checked at elementary-gate level; it does not execute 12.7 million
routed primitives 14,592 separate times.  The literal full-width representatives
and literal routed small-width test keep this performance distinction visible.

The Cycle 463 actual-row digest is
`ba563e6f623fb6ff57b4506dfb83e4ebc5a33241e54c714e1ff3e04554e65519`.
All actual quotient mismatches, remainders, logical work leakage, inverse
failures, routed adjacency failures, and routed placement failures are zero.

## Prior-art and novelty boundary

Cuccaro et al.'s ripple-carry adder, reversible compute/copy/uncompute,
Gray-path transposition synthesis, and clean-ancilla multi-control decompositions
are established reversible-circuit machinery.  Cycle 467 does not claim those
algorithms as new, and it does not claim gate-count or work optimality.

The new repository result is the exact bounded composition against the frozen
Cycle 463 object: the explicit 32-state divide-six totalization, the complete
249-bit transcript and inverse, the constructive 762-bit fit inside the prior
763-bit allowance, all 14,592 frozen-row checks, the complete scale-40 nearest-
neighbor transcript, and the all-24 carried schedule audit.  This is compiler
novelty within the framework, not a claim of new arithmetic or new physics.

## Supplied/imported inventory

Supplied here:

1. six retained 249-bit neighbor input ports, one local source bit, a retained
   target, and blank work/target code constraints;
2. `D=6^96`, addition of `D*s`, division by six, `B=249`, and `W=B+3`;
3. the computational-basis word interpretation and acceptance of floor-division
   totalization outside the lawful exact-divisibility code;
4. one scale-40 supercell and a Hamiltonian-path placement convention;
5. the serial logical program and the particular deterministic off-code
   completion of the divider permutation;
6. finite Cycle 463 train/held domains, retained histories, and source data;
7. explicit wall/RSS caps for this executable.

Constructed here: the full NCT arithmetic trace, inverse, work-reset proof by
execution, nearest-neighbor route, gate/depth/capacity counts, exhaustive
small-width tests, all-row frozen-fixture replay, invalid-domain controls, and
proper-cubic carried manifests.

Still not derived: inter-supercell delivery to the declared ports; why the
six-neighbor relaxation, division, precision, source scale, boundary, or 96
layers are physical; a dynamical source law; matter/energy-stress identification;
clock duration; occurrence or Records; Born weights; infinite-volume or
continuum limits; lapse, metric, curvature, backreaction, or gravity.

## TOE dependency ledger

| wall | Cycle 467 disposition |
|---|---|
| `C_ref` | unchanged; arithmetic compilation selects no vacuum, sea, phase origin, or preparation |
| `C_num` | unchanged; binary integer ports do not select a physical number reference or superselection law |
| `C_wrap` | unchanged; neither 96 iterations nor 8,120,016 routed depth is a causal interval or retained winding |
| `C_int` | unchanged; the supplied addition/division law is compiled, not dynamically selected, protected, or assigned a rate |
| `C_local` | constructively narrowed for the Cycle 463 arithmetic sub-obligation: bounded NCT and nearest-neighbor compilation now exists within the prior work/capacity budget; inter-supercell port transport and broader physical-law compilation remain open |
| `C_source` | implementation-only narrowing: the supplied `D*s` term is computed locally, but no energy/stress/source meaning, conservation law, or backreaction is derived |

No pair of walls collapses.  In particular, an arithmetic compiler does not
select its law or source, and a source interpretation would not by itself
compile ports or arithmetic.

## Full no-go discipline

The result is positive but bounded by named walls, so the full gate is retained.

### N1 — Alternative route enumeration

| normalized route family | object / mechanism / terminal obligation | status |
|---|---|---|
| ripple plus totalized long division | binary words / Cuccaro plus five-bit permutation / complete bounded NCT compiler | **ATTEMPTED — SUCCEEDS** |
| restoring divider | binary words / reversible subtract-and-restore / same exact quotient and cleanup | **OPEN — NOT ATTEMPTED** |
| carry-save or redundant arithmetic | redundant digits / local compressor network / lower-depth bounded compiler | **OPEN — NOT ATTEMPTED** |
| lookup or arithmetic automaton | finite control plus word tape / locally propagated transition table / same law | **OPEN — NOT ATTEMPTED** |
| Fourier/phase arithmetic | phase registers / reversible spectral arithmetic / same basis-word output | **OPEN — NOT ATTEMPTED** |
| direct inter-supercell streaming | retained neighbor words / moving head or link buffers / port-free seven-cell block | **OPEN — NOT ATTEMPTED** |

The successful route defeats any impossibility claim.  The unattempted routes
also prohibit a minimum-depth, minimum-work, or unique-content claim.

### N2 — Wall-independence audit

Collapse implementation details into `Wa` arithmetic trace/routing, `Wp`
inter-supercell port transport, `Wl` finite law/precision/boundary selection,
`Ws` source meaning and conservation, `Wc` causal clock interpretation, and
`Wg` metric/backreaction/gravity.  No one closes another: a complete adder does
not deliver ports or select a law; port transport does not identify energy;
source conservation does not turn gate depth into time; clock interpretation
does not imply curvature; gravity interpretation does not synthesize the local
circuit.  They remain pairwise independent at the tested level.

### N3 — Hidden-wall scan

The scan exposes blank work and target code, six basis-word ports, supplied
`D`, divisor, width and serial schedule, the deterministic invalid-code
completion, scale-40 Hamiltonian placement, computational-basis interpretation,
and missing inter-supercell transport.  “Compiler” is restricted to these
declared ports.  No standard-method phrase carries a physics conclusion.

### N4 — Residual matching

The witness matches Cycle 463's named missing item exactly: a complete
Toffoli/CNOT/nearest-neighbor arithmetic trace.  The 762-bit allocation and
full transcript answer that residual.  It does not match the finite-law,
source-meaning, clock, continuum, or gravity residuals and is not cited against
them.

### N5 — Rhetoric audit

Evidence exists at five-bit step, small-width full circuit, actual frozen-row,
representative full-width, routed-event, supercell, and carried-frame levels.
Claims stop at the bounded local basis permutation.  “Exact” means integer and
basis-state equality on the declared code.  No optimality, continuum,
universality, energy, time, or gravity statement is promoted.

### N6 — Partial-closure path scan

Cycle 463 named primitive synthesis as absent.  Cycle 467 supplies it without
editing an axiom or importing a new physical law.  The next constructive path
is port transport and then law/source selection, not a declaration that the
remaining walls require new axioms.

### N7 — Steelman

A hostile reviewer can reasonably demand a shallower carry-save/restoring
divider, an explicit seven-supercell port network, coherent tests beyond basis
fixtures, less retained history, a source derived from matter dynamics, and a
continuum/backreaction limit.  All are actionable.  The present 12.7-million-
event route is deliberately a witness, not a good architecture.

### N8 — Cross-cycle echo and claim gate

Cycle 463's narrow unsynthesized-trace echo is closed.  Its separate warnings
against calling iteration time, source bits energy/stress, or finite response
gravity remain fully active.  Earlier `C_local`, `C_wrap`, and `C_source`
ledgers concern wider terminals than this arithmetic block.  This cycle does
not reuse a route-specific compiler success as constitutional evidence.

**No-go claim: FAIL. Minimum-content claim: FAIL. Axiom-pressure claim: FAIL.**
There is **no axiom pressure**.  The admissible result is the positive bounded
compiler and its explicit residuals.

## Frozen executable disposition

Retention requires a cold run with zero failures, the hashes/counts above, and
resource use below the declared 240-second / 1,536-MiB caps.  The runner and
this note are Cycle 467 artifacts only.  They carry authority none and audit
unset and do not authorize a merge or audit verdict.

The final cold execution reports `RESULT pass=12 fail=0`, takes 36.826 seconds,
and peaks at 126.31 MiB.  Runner SHA-256:
`7e562949be71a647d410c8a9624eb5cf5fdf2be30777fab93c6ed55824a5e402`.

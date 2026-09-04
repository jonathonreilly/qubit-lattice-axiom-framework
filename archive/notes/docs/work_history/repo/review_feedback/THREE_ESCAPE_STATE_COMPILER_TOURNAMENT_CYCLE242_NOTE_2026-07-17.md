# Three-escape physical-M2 state-compiler tournament — Cycle 242

**Date:** 2026-07-17

**Type:** adversarial synthesis of three independently executed constructive
routes

**Status:** substantial conditional constructions; no complete physical-M2
state compiler; no shared no-go and no axiom pressure

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

**Packaging:** existing draft PR #5389 on
`codex/bare-metal-mvp-probes-20260713` only; do not merge

Companion runner:

```text
scripts/three_escape_state_compiler_tournament_cycle242_2026_07_17.py
```

This cycle changes no foundation, axiom, Qualification, primitive, registry,
policy, queue, or audit surface. It synthesizes Cycles 239, 240, and 241 only
after their actual notes and runners were independently reviewed and rerun.

## Decisive result

None of the three routes supplies one bounded local state encoding `E` and
one physical update `G_physical` satisfying

```text
E G_coarse = G_physical E
```

on the full Cycle-230 Fock code while also meeting constant physical-`M2`
overhead, local constraints, no global parity/ordering/controller service,
all-24 proper-cubic covariance, and the one-particle plus rank-73 fixtures.

That negative is a tournament disposition, not a compiler impossibility.
Each route closes a different part of the interface:

1. **Distinguishable antisymmetric walkers (Cycle 239)** give an exact
   fixed-particle state isometry and exact free/contact dynamics, including
   mass, seam, leakage, deletion, and all 24 frames. The published variable-
   particle realization requires `N_max=6L^3` replicated particle types and
   therefore `36L^3` physical qubits per coarse cell. Its antisymmetrizer and
   first-`n` label convention are global supplied structure.
2. **Measurement/feedforward gauging (Cycle 240)** measures every bounded
   square-pyramid Gauss check in 30 abstract quantum subrounds with 11
   temporary syndrome qubits per cell. An explicit Gaussian decoder then
   prepares the fixed even vacuum deterministically. The decoder, syndrome
   outcome collection, and Wilson-sector corrections are global; the odd
   one-particle and sea states remain absent.
3. **QCA/isometry (Cycle 241)** finds a proper-cubic equal-Wilson rank
   completion with exactly the full-Fock dimension and one common parity
   slot. It also rejects the verbatim full-algebra flux dictionary and clean-
   product Clifford-QCA preparation of that closed code. It does not construct
   the needed non-Clifford/subalgebra isometry, odd-sector operator map, or
   sector preparation.

The strongest combined scientific statement is therefore:

> Bounded proper-cubic physical operators and constant-overhead local even-
> algebra dynamics are constructive. A constant-round local projection into
> the even gauge family is constructive. Both required odd fixtures fit one
> cubic-invariant common-Wilson parity label at the rank level. No construction
> yet joins those facts into one locally prepared all-parity state compiler.

The sentence deliberately does not splice the global antisymmetrizer, the
measurement decoder, and the equal-Wilson schema into a fictitious `E`.

## Route-by-route exact disposition

| Contract | Antisymmetric walkers | Measurement/feedforward | QCA/isometry |
|---|---|---|---|
| constant physical overhead | **fail for published full-Fock realization** | **pass for data plus syndrome layer** | **pass at architecture/rank level** |
| bounded physical update | exact at fixed sector, but local cell grows | exact even-algebra update inherited | exact even algebra inherited; new QCA unbuilt |
| bounded local state map | global antisymmetrizer | local projection, global decoder | non-Clifford/subalgebra map unbuilt |
| both parity sectors | exact if `N_max=M` | no; closed code is total-even | common-Wilson slot has correct count; map unbuilt |
| one-particle mass | exact, conditional on code state | state absent | odd slot exists; no intertwiner |
| rank-73 seam | exact, conditional on code state | state absent | odd slot exists; no intertwiner |
| all 24 frames | exact fixed-sector dynamics | local instrument/target exact; decoder is not | architecture and rank schema exact; QCA unbuilt |
| host/global service | labels and antisymmetrizer | outcomes, decoder, Wilson membranes | sector/marker/resource preparation |
| full compiler | **no** | **no** | **no** |

## Exact retained numbers

### Cycle 239 — algebra succeeds, resource law fails

For `M=6L^3` and exact full-Fock capacity `N_max=M`:

| `L` | qubits/cell | total QCA qubits | overhead ratio | pair gates/cell | pair-only depth floor |
|---:|---:|---:|---:|---:|---:|
| 3 | 972 | 26,244 | 162 | 13,041 | 161 |
| 4 | 2,304 | 147,456 | 384 | 73,536 | 383 |
| 5 | 4,500 | 562,500 | 750 | 280,875 | 749 |

The `L=3,4` law `36L^3` predicts held-out `L=5` value `4500` exactly.
Fixed-sector residuals remain machine zero: free exterior-power intertwining
below `1.5e-15`, pair-contact intertwining below `2e-15`, seam contraction
`1.22e-16`, all-frame residual below `7e-16`, and identical-lane leakage
below `7e-16`. Asymmetric contact and deleted-lane controls leak nontrivially.
The two-separated-site antisymmetric assignment has Schmidt values
`(1/sqrt(2),1/sqrt(2))` and product-state distance floor
`sqrt(2-sqrt(2))`.

### Cycle 240 — projection succeeds, autonomous decoding does not

For `L=3,4,5`, the face counts are `405,960,1875`; local Gauss ranks are
`241,574,1123`; ranks after three Wilson constraints are `244,577,1126`.
Every local check has weight at most 28 and every data qubit participates in
at most 11 checks. Bipartite edge coloring gives 28 interaction subrounds;
ancilla preparation and readout give 30 abstract bounded subrounds total.

The selected Gaussian decoder has zero syndrome residual but maximum
correction weights `90,152,314`. These are costs of that decoder, not lower
bounds for all decoders. Fixed-spin correction uses noncontractible `L x L`
membranes of weights `9,16,25`; syndrome aggregation and broadcast radii grow
with `L`. The complete all-plus postselection masses are
`2^-244,2^-577,2^-1126`, while Wilson-only postselection after local decoding
has conditional mass `1/8`. These are standard supplied instrument weights,
not a Born-law or occurrence derivation.

All measured signs are independent/uniform on the clean zero input at their
rank resolution and every measured operator commutes with every cell flux.
Thus the deterministic global protocol really prepares the fixed even vacuum.
It still requires actualized syndrome outcomes or a coherent global decoder,
and syndrome pointers are not automatically framework Records.

### Cycle 241 — cubic rank completion is real but not yet an encoder

The closed square-pyramid code has exponents

```text
local Gauss only:              6L^3 + 2,
two equal-Wilson relations:    6L^3,
three fixed Wilson relations:  6L^3 - 1.
```

The two relations `W_x W_y=+1` and `W_y W_z=+1` leave labels `000` and `111`,
which are invariant under every proper-cubic frame. The remaining bit has the
right dimension to carry total parity, and both required fixtures are odd.
This is necessary rank/covariance compatibility, not a constructed parity
operator map.

The exact verbatim map `Z_t -> W_t` cannot be a full tensor-algebra QCA:
`product_t W_t=I`, and every finite face-Pauli commutation syndrome has an
even number of flux endpoints, so no singleton conjugate exists. The clean-
product Clifford-QCA image also fails for the rank-matched closed code: `9L^3`
ancilla stabilizers are needed, only `9L^3-2` independent stabilizers are
bounded Gauss products, and the two missing directions are noncontractible.
Displayed Wilson-pair weights are `18,24,30,42` at `L=3,4,5,7`.

The complete `2^15` one-cell translation-orbit Pauli census finds 1,024 closed
templates at every held size. Odd `L=3,5` realize all eight homology labels;
even `L=4` realizes only the trivial label. No fixed template leaves the same
nonzero Wilson class at all sizes. Larger-period, non-Pauli, data-dependent,
and non-Clifford completions remain live.

## Shared-wall audit

All three routes expose a state/sector interface, but they do not establish
one route-independent mathematical obstruction:

- Cycle 239 fails through replicated label multiplicity and a global
  antisymmetrizer while carrying both parities exactly.
- Cycle 240 has bounded quantum measurement and constant overhead, but its
  displayed correction/controller is global and its closed algebra is even.
- Cycle 241 rules out only a clean-product **Clifford** QCA and one exact flux
  dictionary. Non-Clifford subalgebra gauging isometries remain a real class.

The Cycle-238 conditional preparation obstruction still applies if `E` is
required to be a bounded-depth local two-body unitary from product inputs.
Cycle 240 explicitly leaves that class by measurement, and Cycle 241
explicitly leaves it by nontrivial QCA/isometry. Therefore the tournament has
no general state-compiler no-go, no minimum-content theorem, and no axiom
pressure.

## N1–N8 no-go-discipline synthesis

The claim under review is only:

> None of the three executed Cycle-239/240/241 constructions meets the full
> physical-M2 compiler contract as written.

**N1 — alternatives.** Executed alternatives are distinguishable walkers,
local measurement plus four correction variants, verbatim flux QCA, product-
ancilla Clifford QCA, and fixed translation-orbit Pauli dressings. Live
alternatives include a bounded cellular syndrome decoder, measurement-
resource state, non-Clifford 3-D QCA, parity-subalgebra gauging isometry,
open/infinite charge sector, topological input resource, and larger-period
completion. Broad impossibility therefore fails N1.

**N2 — independence.** The surviving walls are: lawful full/code isometry,
odd-charge/topological label, preparation/controller, and covariance of the
actual encoder. Update locality is downstream and already constructive. A
solution to any one surviving wall does not automatically solve the others.

**N3 — hidden conditions.** Closed tori, exact full Fock capacity, clean
product inputs, Clifford restriction, projective measurements, actualized
outcomes, classical communication, selected Wilson/marker sector, and source
mode ordering are all explicit where used.

**N4 — residual matching.** Each conclusion is tied to its own runner:
volume-growing label counts and exact fixed-sector residuals; syndrome ranks,
decoder supports, Wilson membranes, and branch exponents; flux-boundary rank,
stabilizer deficit, homology census, and marker/frame tests. No source theorem
is promoted beyond its hypotheses.

**N5 — rhetoric.** The synthesis says the three attempts do not yet close the
contract. It does not say fermions cannot emerge from qubits, topological
codes cannot be prepared, or non-Clifford QCAs cannot solve the fixture.

**N6 — partial closures.** Retain the exact fixed-sector walker as an algebraic
control; retain the 30-subround projection layer; retain the equal-Wilson
rank completion and the bounded even-algebra compiler.

**N7 — steelman.** A Haegeman-style parity-sector gauging isometry can preserve
local symmetric observables while producing a topological gauge state. A
nontrivial 3-D QCA is strictly outside finite-depth Clifford circuitry. A
translation-covariant cellular decoder could make the measurement route
autonomous. These are credible constructive classes, not rhetorical loopholes.

**N8 — cross-cycle echo.** Cycles 232, 235, 236, 237, and 238 repeatedly
separate local update algebra from state preparation and sector selection.
Cycles 239–241 instantiate three distinct routes rather than converting that
recurrence into a theorem. No retired primitive supplies the missing map.

N1–N8 therefore passes the narrow route dispositions and rejects a broad
no-go, uniqueness/minimality, or axiom-pressure claim.

## Supplied-structure inventory

Across the three routes, the following remain supplied somewhere and cannot
be hidden by cross-route synthesis:

1. Cycle-219 coin and mass calibration;
2. Cycle-230 contact value, sea phase cut, torus, and update order;
3. particle-type multiplicity, first-`n` convention, mode-sign bookkeeping,
   and antisymmetric code declaration in Cycle 239;
4. projective measurement instrument, branch weights, actualized syndrome
   outcomes, Gaussian pivot choices, classical collection/broadcast, and
   Wilson membranes in Cycle 240;
5. square-pyramid cellulation/framing, equal-Wilson proposal, closed sector,
   clean product ancillas in the rejected Clifford route, and any future
   topological/QCA resource in Cycle 241; and
6. period-16 marker seed, selected marker phase, macro origin, and physical
   preparation of the marker/resource state.

None is promoted to an axiom or treated as derived.

## TOE dependency ledger after Cycle 242

| Wall | Change | Remaining dependency |
|---|---|---|
| `C_ref` | marker, spin/Wilson, label, outcome, and sea inputs are now separated route by route | physical phase/sector/sea preparation and realized reference remain supplied |
| `C_num` | both parities are exact in the high-overhead walker route; a cubic common-Wilson parity slot exists at rank level | no bounded physical derivation of number/parity or all-size odd-sector state map |
| `C_wrap` | unchanged | phase, QCA index, Wilson label, measurement round, and compiler layer are not time or winding history |
| `C_int` | exact fixed-sector contact and exact bounded even-algebra contact survive | selection, value, protection, odd-fixture state map, and phase-to-physical-rate bridge remain open |
| `C_local` | materially narrowed | local even update and local projection are constructive; all-parity state isometry, autonomous bounded decoder, sector preparation, and actual QCA covariance remain open |
| `C_source` | unchanged | no physical energy, stress/action, resource source, or gravitational response is selected |

Maturity remains:

```text
operational quantum / records: 2/5
causal time:                    1/5
inertia / matter:               3/5
gravity / source:               2/5
Born / probability:             1/5
```

## Three-dimensional substrate and derived-time firewall

The current axioms supply the `Z^3` spatial lattice, its proper-cubic action,
and one-site `M_2(C)` possibility algebra. They do not supply a time metric.
QCA range, circuit depth, measurement subround, marker phase, macrostep, and
update count are compiler coordinates only.

Repository time results require a separate bridge: the physical law must
first identify local occurrence/commit events; a named permanent commit chain
can then define ordinal clock count; comparisons of physical clock chains and
calibration are still required for metric duration and relative rate. Thus a
future compiler-to-time bridge must connect update support to law-generated
event order and then to record-faithful clock comparisons. It cannot rename a
gate schedule as time, a contact phase as a rate, or a QCA light cone as a
metric cone.

## Optimal next campaign

Run two independent constructive discriminators:

1. search for a translation- and proper-cubic local cellular decoder/sign
   frame for every lawful Cycle-240 syndrome, including Wilson bits, with
   bounded radius independent of `L`; and
2. instantiate a parity-sector gauging isometry or non-Clifford symplectic/
   off-code QCA completion on the equal-Wilson schema, checking both
   Heisenberg locality directions, the one-particle and rank-73 fixtures, and
   actual encoder covariance.

In parallel, type the separate spatial-compiler-to-causal-time bridge so that
later matter velocities and interaction phases acquire physical rate meaning
only after event and clock theorems, not by convention.

## Verification

```text
python3 scripts/three_escape_state_compiler_tournament_cycle242_2026_07_17.py
```

Expected result: all three predecessor runners pass and every synthesis check
passes. No `E G_coarse = G_physical E` success is claimed.

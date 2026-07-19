# Physical nearest-neighbor grade-table admission — Cycle 395 (2026-07-18)

Status: **positive bounded local reversible table admission; authority: none;
audit: unset.** This cycle does not alter axioms, foundation, Qualification,
primitives, registries, policies, queues, or audit status. It makes no no-go,
minimum-content, obstruction, constitutional, or axiom claim. There is no
axiom pressure.

Runner:
`scripts/physical_nn_grade_table_admission_cycle395_2026_07_18.py`

## Strongest constructive result

Cycle 395 constructs a bounded reversible loader and admission oracle for the
two exact denominator-48 tables declared in current-campaign Cycle-388. One
supplied selector M2 controls loading into a 54-M2 grade-table register. One
admission M2 flips exactly when the selector and all 54 table bits match one
of the two declared pairs. The largest equality branch has 55 controls and is
decomposed with 53 clean work M2.

The resulting primitive circuit is routed on a connected 109-M2
nearest-neighbor line. It contains 46,153 explicit X, CNOT, Toffoli, and SWAP
operations. Maximum primitive support: 3 M2. The actual routed forward
schedule loads and admits both selected tables, the reversed schedule returns
both to the blank table/admission/work state, and the admission-only schedule
rejects both selector/table mismatches. This is exact forward/inverse E/G on
the declared code space.

Operational table admission is not a law selecting Nature's grade. Selector
preparation remains supplied, as do the two candidate tables and the
truth-table primitive layer. The result shows that the finite admission step
can be represented locally and reversibly once those inputs are supplied; it
does not explain why either selector value is prepared in Nature.

## Declared tables and code space

The two current-campaign Cycle-388 numerator tables are

```text
A = (12, 36,  8, 16, 24, 24, 20, 28, 16)
B = (18, 30, 12, 14, 22, 24,  7, 41, 16)
```

Each entry occupies six M2 and each table is therefore a 54-M2 computational
word. Both tables pass the exact Cycle-388 denominator-48 menu normalization
checks. This cycle neither derives those values nor expands the candidate
set.

The connected line has sites 0 through 108 and all 108 edges

```text
(0,1), (1,2), ..., (107,108).
```

Its boundary register inventory is:

| Register | Sites | M2 |
|---|---:|---:|
| supplied table selector | 0 | 1 |
| nine six-bit grade numerators | 1–54 | 54 |
| admission output | 55 | 1 |
| clean equality work | 56–108 | 53 |
| total line | 0–108 | 109 |

The declared input code space has a binary selector, nine valid six-bit table
words, a binary admission bit, and all 53 work M2 blank. Clean work is a
boundary requirement; internal conjunctions may populate work sites and the
circuit uncomputes them before returning to the boundary.

## Reversible loader and equality oracle

Let the selector be (s\in\{0,1\}\), and write the two 54-bit tables as
(T_0=A\) and (T_1=B\). The loader implements the reversible XOR

\[
  (s,t,a,0^{53})\mapsto(s,t\mathbin{\oplus}T_s,a,0^{53}).
\]

For table bits that are one in both candidates, it applies X. For bits that
change from zero to one between A and B, it applies selector-controlled CNOT.
For bits that change from one to zero, it temporarily complements the
selector, applies selector-controlled CNOT, and restores the selector. The
loader is self-inverse.

The admission oracle has one equality branch per selector. A branch
temporarily complements every zero-pattern table bit and, for selector zero,
the selector itself. It then applies a 55-control X to the admission M2 and
restores all temporary complements. Consequently

\[
  (s,t,a,0^{53})\mapsto
  (s,t,a\mathbin{\oplus}[t=T_s],0^{53}).
\]

A 55-control X is compiled as a forward chain of Toffoli conjunctions, the
target Toffoli, and the reversed uncomputation chain. It uses exactly 53
clean work M2 and no larger primitive than Toffoli.

## Exact forward/inverse E/G

Let (E_{395}\) be the computational-basis encoding of the declared selector,
table, admission, and clean-work registers. Let (G_{\rm coarse}\) map a blank
table and blank admission bit to the selector's declared table and admission
one. Let (G_{395}\) be the explicit loader-plus-admission routed schedule.
For selectors zero and one the runner executes and verifies

\[
 E_{395}G_{\rm coarse}=G_{395}E_{395}.
\]

The exact outputs are:

```text
selector 0 -> (A, admission 1, clean work)
selector 1 -> (B, admission 1, clean work)
```

Exact E/G failures are 0. Explicit routed inverse failures are 0: reversing
all 46,153 self-inverse primitives returns each selected output to its blank
table, blank admission, and blank-work source. On already supplied candidate
tables, the admission-only truth vector in order `(0,A), (0,B), (1,A),
(1,B)` is `(1,0,0,1)`.

This equality is restricted to the declared two-table code space. It is not
a universal grade-law compiler and does not establish table genesis.

## Explicit nearest-neighbor schedule

For each logical X, CNOT, or Toffoli, stable adjacent SWAPs bring its operands
into one contiguous line window. The logical primitive is executed there,
then the SWAP list is reversed so the declared layout is restored before the
next primitive.

| Quantity | Exact result |
|---|---:|
| logical primitives | 387 |
| routed primitives | 46,153 |
| X | 150 |
| CNOT | 23 |
| Toffoli | 214 |
| SWAP | 45,766 |
| maximum primitive support | 3 M2 |
| maximum primitive span | 2 line edges |
| non-nearest-neighbor failures | 0 |

The explicit schedule digest is

```text
1d277cb916bb50ad148f64bbb2a1df3183b33b573950bb5175938f6cc89089ce
```

Every admitted primitive is a computational-basis permutation, so the local
unitarity residual is exactly zero. The line order is a supplied local patch
layout, not a global Jordan–Wigner string, nonlocal parity service, or
preferred ordering of the cubic lattice.

The schedule is not time. Its order and gate count supply neither a physical
clock nor a duration, rate, causal-time law, or physical-energy claim.

## Physical spectator controls

The Cycle-395 line is scalar under spatial proper-cubic action and acts on no
matter operand. The current-campaign Cycle-391 primitive compiler supplies
the nearest-neighbor basis/routing precedent, while the landed Cycle-317,
Cycle-321, and Cycle-323 substrate supplies the accepted matter encoding,
contact, mass fixture, physical carrier, and proper-cubic checks.

The actual Cycle-395 runner re-executes the inherited controls at (L=3\) and
held L=6 and certifies every one of the 46,153 new primitive boundaries by
the spectator tensor factor:

| Control | L=3 | held L=6 |
|---|---:|---:|
| boundaries certified | 46,153 | 46,153 |
| maximum matter leakage | (2.6803154833\times10^{-16}\) | (2.6803154833\times10^{-16}\) |
| maximum matter role-constraint residual | 0 | 0 |
| Cycle-230 contact intertwiner residual | 0 | 0 |
| port/local/Wilson failures | 0 | 0 |

All 24 proper-cubic frames pass: carrier branch failures are 0, maximum
carrier covariance residual is 0, and the scalar admission-line frame
commutator is 0. The one-particle mass relative residual remains
(2.2204460493\times10^{-16}\).

The accounting is a 172-M2 compiled envelope:

```text
62 inherited one-use physical matter/pointer M2
 1 inherited Cycle-384 registration M2
109 Cycle-395 admission-line M2
---------------------------------------------
172 M2 compiled envelope
```

Installed accounting overhead is 139 M2 per cell
((23+3+3+1+109\)), independent of (L\). The line attaches through the
supplied program/registration apparatus interface. This is bounded patch
accounting, not a derivation of the interface or layout.

## Deletion, attack, and lawful-domain controls

The runner detects three independent deletions:

- deleting the first loader logical gate fails to produce the admitted A
  output for selector zero;
- deleting the complete admission macro loads A but leaves admission zero;
  and
- deleting the first routed primitive changes the declared output.

It also flips each of the 54 table bits independently for each matched
selector/table candidate. All 108 one-bit attacks produce zero false
admissions. All 10 malformed-domain calls reject. They cover invalid
selector, wrong table width, a numerator outside its six-M2 register, dirty
work preparation, unknown primitive, wrong primitive arity, repeated
primitive site, excessive multi-control work demand, wrong state width, and
a disconnected line.

## Provenance and novelty boundary

- Landed Cycles 317, 321, and 323 supply the accepted physical matter code,
  contact, one-particle mass fixture, fixed-program carrier, support
  accounting, and proper-cubic covariance.
- Current-campaign Cycle-388 supplies the two exact denominator-48 tables,
  their fixed menu classes, and the normalization reference.
- Current-campaign Cycle-391 supplies the explicit nearest-neighbor
  X/CNOT/Toffoli/SWAP compilation and routing precedent. Cycle 395 imports it
  as current-campaign evidence, not as landed authority.

Cycle 395 adds the selector-conditioned reversible table loader, two-branch
equality oracle, 53-work-M2 decomposition, connected 109-M2 layout, explicit
routed schedule and inverse, selector/table mismatch tests, bit-flip attacks,
and physical spectator accounting. It does not derive either grade table,
select between them, derive the selector state, derive the primitive truth
tables, or promote admission into occurrence.

## Complete supplied-structure inventory and semantic boundary

The following remain supplied:

- selector preparation remains supplied: one binary M2 state;
- the Cycle-388 candidate tables and denominator 48 remain supplied;
- the blank table, blank admission, and 53 clean work M2 remain supplied;
- primitive basis, layout, work preparation, admission, and schedule remain
  supplied;
- the adjacency router and local interface to the inherited apparatus remain
  supplied;
- primitive physical gate genesis below the admitted truth-table layer
  remains supplied; and
- the restriction to exactly two table candidates remains supplied.

What is derived is operational equality admission for exactly the matching
selector/table pairs and a reversible loader for a supplied selector. The
law selecting Nature's grade is `None`; selector genesis, new-table genesis,
primitive-gate genesis, physical clocking, and a wider law over candidate
tables are all absent.

The grade is not probability and there is no Born law. Admission is not
occurrence, actuality, sampling, a Record, permanence, frequency, or realized
history. There is no actuality or frequency inference. Nothing here derives
a source/gravity law.

## Dependency-ledger effect

- `C_ref`: unchanged.
- `C_num`: narrowed constructively only at the fixed two-table interface. A
  supplied selector can now load and equality-admit A or B through an exact
  local reversible circuit. The grade tables, denominator, candidate-set
  restriction, selector preparation, and law choosing Nature's grade remain
  supplied, so no probability law is added.
- `C_wrap`: unchanged; no actuality, occurrence, Record, permanence, or
  history selection is introduced.
- `C_int`: preserved, not advanced; the inherited mass and contact fixtures
  remain green under the spectator audit.
- `C_local`: narrowed for this admission operation: the two supplied tables
  have an explicit bounded nearest-neighbor loader/equality circuit. Primitive
  basis, line layout, clean-work preparation, interface, admission, and
  ordered schedule remain supplied.
- `C_source`: unchanged.

Cold-run command:

```text
python3 scripts/physical_nn_grade_table_admission_cycle395_2026_07_18.py
```

Expected summary: `SUMMARY PASS=6 FAIL=0`.

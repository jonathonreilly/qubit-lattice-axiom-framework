# Clean row-alphabet component replacement — Cycle 175

Date: 2026-07-16

Authority: none

Disposition: constructive bounded closure; audit unset

Companion runner:

```text
scripts/clean_row_alphabet_component_replacement_cycle175_2026_07_16.py
```

No foundation, axiom, primitive, registry, queue, policy, audit, predecessor,
commit, push, or PR surface is changed.

## Result

Cycle 175 closes the exact type-alias residual left by Cycle 171 without a new
onsite role and without typed carrier furniture.

The replacement keeps the 25 signed-row labels already clean on the recurrent
carrier and changes only the seven inherited executable aliases:

| Signed row | Old role | Replacement role |
|---|---|---|
| `(0,0,0,1,1)` | `A_0_1` | `PAIR` |
| `(0,0,1,0,0)` | `A_0_2` | `Z0` |
| `(0,1,1,0,1)` | `BTG` | `Z_A` |
| `(0,1,1,1,1)` | `BTQ` | `Z_C` |
| `(1,0,0,0,0)` | `B_0_2` | `RING` |
| `(1,0,0,1,0)` | `COMP6` | `R_A02` |
| `(1,0,1,1,1)` | `DONE` | `R_A00` |

These are the seven lowest-exposure non-row roles among the carrier-clean
Cycle-171 census. None has an inherited unary firing. The resulting 32-role
codebook is injective.

This is a **component replacement**, not duplicate semantics. Every retained
raw family parameterized by the old row codebook is removed, recompiled under
the one replacement codebook, and merged back exactly once.

The rebuilt laws are deterministic and retain their exact sizes:

```text
Cycle-166 replacement law                 100,652 raw rows
Cycle-169 replacement union               101,708 raw rows
deterministic conflicts                          0
```

All four Cycle-166 hard stabilizer-update fixtures reproduce exactly modulo the
declared row-label substitution. The Cycle-169 signed-membership hard fixture
reproduces exactly under both minimum and maximum schedules. Finally, all 32
replacement row values traverse the Cycle-171 recurrent carrier through
`G1`, `G2`, and `G3` on the replacement Cycle-169 union:

```text
replacement carrier delta                   3,168 raw rows
replacement union plus carrier             104,876 raw rows
deterministic conflicts                          0
row values closing G1-G3                     32 / 32
```

The licensed result is:

> The seven Cycle-171 carrier failures were codebook aliases, not a missing
> formation principle. One injective replacement alphabet closes the retained
> row-processing fixtures and the bounded all-32 recurrent carrier on the
> existing onsite role pool.

This is a compiler/law-architecture result. No axiom addition follows.

## Exact replacement accounting

The Cycle-166 rebuild removes the 32,352-signature unique union of 13
row-parametric families and adds the corresponding 32,352-signature mapped
union. The Cycle-169 rebuild includes the sign reader, removing and adding a
33,120-signature unique union across 14 families.

The family sums are larger because the Cycle-165 tap and Cycle-166 integrated
gate share 1,536 raw signatures:

```text
Cycle-166 family sum                        33,888
Cycle-166 unique replaced support           32,352
shared family support                        1,536
old-only signatures removed                  7,926
new-only signatures added                    7,926
same signature, changed output                1,032
unchanged signatures                         23,394

Cycle-169 family sum                        34,656
Cycle-169 unique replaced support           33,120
shared family support                        1,536
old-only signatures removed                  8,094
new-only signatures added                    8,094
same signature, changed output                1,032
unchanged signatures                         23,994
```

Every old component signature is present in the source law before removal.
The rebuilt laws have the same total sizes as their sources, so the result is
not obtained by retaining the old families beside mapped copies.

| Atomic family | Lane | Raw rows | Rows referencing one of the seven changed labels |
|---|---|---:|---:|
| Cycle 149 tableau row gate | tableau | 3,072 | 1,056 |
| Cycle 151 commuting multiplier | multiplication | 6,528 | 2,988 |
| Cycle 152 pivot router | routing | 4,896 | 1,008 |
| Cycle 153 row-to-literal fanout | reading | 960 | 210 |
| Cycle 155 ported row reader | reading | 3,072 | 672 |
| Cycle 158 two-port row reader | reading | 3,072 | 672 |
| Cycle 162 row transport | transport | 1,536 | 336 |
| Cycle 163 mux gate | mux | 3,840 | 840 |
| Cycle 163 mux join | mux | 768 | 168 |
| Cycle 163 mux terminal | mux | 768 | 168 |
| Cycle 165 payload tap | tap | 768 | 168 |
| Cycle 166 row splitter | joint update | 768 | 168 |
| Cycle 166 integrated gate | joint update | 3,840 | 840 |
| Cycle 167 sign reader | sign | 768 | 168 |

The Cycle-169 membership comparator contributes 288 literal-bit rows and
contains no row-role reference. It requires semantic fixture replay, but zero
raw-row replacement.

This is the explicit price of the compiler-table reset: 14 atomic families and
33,120 unique raw signatures are treated as one codebook-dependent unit. The
size is evidence that the old law architecture duplicated its data alphabet
across many interfaces. It is not evidence for a new physical postulate.

## Hard-fixture reproduction

### Cycle 166

The four retained pivot cases remain green. Counts are exactly unchanged:

| Case | States | Frontier visits | Maximum frontier | Source records | Dynamic records |
|---|---:|---:|---:|---:|---:|
| `(0,0)` | 30,634 | 269,149 | 16 | 379,288 | 30,633 |
| `(0,1)` | 30,638 | 268,513 | 16 | 379,288 | 30,637 |
| `(1,0)` | 30,704 | 269,499 | 16 | 379,288 | 30,703 |
| `(1,1)` | 30,832 | 269,435 | 16 | 379,288 | 30,831 |

The only changes in the complete fixture transcripts are the declared
substitutions—for example, selected `A_0_2` becomes `Z0` and selected `B_0_2`
becomes `RING`. Products, case selectors, output choice, terminal closure, and
all counts are preserved.

### Cycle 169

The retained hard membership fixture is:

```text
g1       (0,1,0,0,0)
g2       (1,0,0,0,1)
measured (1,1,0,0,1)
```

It remains exact:

| Schedule | States | Frontier visits | Maximum frontier | Source records | Dynamic records | Output |
|---|---:|---:|---:|---:|---:|---|
| minimum | 132,542 | 2,261,261 | 27 | 1,587,398 | 132,541 | `H1` |
| maximum | 132,542 | 1,685,913 | 23 | 1,587,398 | 132,541 | `H1` |

The equality pattern remains `(0,0,1)`, the support bit remains one, and the
terminal is quiet in both schedules.

## All-32 recurrent carrier

The same 132 canonical carrier rows used by Cycle 171 are recompiled against
the replacement codebook. They expand to 3,168 proper-cubic raw rows and merge
conflict-free with the replacement Cycle-169 union.

Every replacement value passes the complete bounded causal certificate:

- 230 states including the initial state;
- 515 load-bearing direct dynamic edges;
- exact minimum and maximum frontier replay;
- zero adjacent unordered dynamic pairs;
- exactly two declared terminal continuation exits; and
- an unbroken seed ancestry chain through `G1`, `G2`, and `G3`.

This closes the exact seven-value residual from Cycle 171. It does not turn
three generations into an unbounded recurrence theorem.

## What changed—and what did not

Changed:

- one explicit 32-value role codebook;
- 13 Cycle-166 row-parametric raw families;
- the Cycle-167 sign-reader family in the Cycle-169 union; and
- every fixture's row-role resolution through that codebook.

Unchanged:

- the onsite role pool;
- the four minimal axioms and registered primitives;
- the Cycle-166 and Cycle-169 law sizes;
- literal `H0/H1` algebra and the 288 membership comparator rows;
- fixture geometries, source records, dependency graphs, and schedules;
- recurrent carrier geometry, record cost, and causal depths; and
- all unrelated control meanings of the seven retired row labels.

The old labels still exist as control/rail roles where the inherited law uses
them. They are retired only from the signed-row data codebook.

## Scope and TOE-lane reading

- **Information:** positive and bounded. One common 32-value codebook survives
  retained reading, multiplication, routing, mux, update, sign, membership,
  and three recurrent carrier generations.
- **Matter:** not established. The apparatus copies permanent row records; no
  conserved active continuation, particle identity, collision law, dispersion,
  or excitation spectrum is shown here.
- **Time:** the carrier has causal commit depths, but no duration or rate is
  derived.
- **Quantum:** row algebra and signed membership remain physical conditional
  computations. Occurrence, preparation, probability, and Born weights remain
  outside this result.
- **Gravity:** the result changes a compiler codebook, not a resource-to-energy
  or resource-to-curvature map.
- **Formation:** no new formation content is needed to repair the seven
  aliases. This probe does not by itself settle constitutional formation
  language.

Cycle 175 demonstrates that the previous all-32 carrier wall was an interface
namespace defect. It does not show that the present law is fundamental, unique,
or optimally compressed.

## Next exact probe

Use the all-32 recurrent carrier as a matter-lane kinematics target:

1. distinguish the one active continuation from its permanent record trail;
2. test whether that continuation defines a conserved causal worldline;
3. derive propagation speed from load-bearing causal depth rather than lattice
   distance alone;
4. place two separated carriers in parallel and require independent closure;
5. construct the first exact collision or junction geometry; and
6. report any additional role, law family, or interface needed without calling
   data copying a particle.

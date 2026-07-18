# C135 six-guard H0 factorized full graph — Cycle 136

Date: 2026-07-15

Authority: none

Disposition: executable bounded guarded-successor construction with open output fork

Write scope: runner + review note only

Companion runner:

```text
scripts/c135_six_guard_h0_factorized_full_graph_cycle136_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, audit, or git state is
edited. No commit or push is made.

## Result

One tested `L4 + L6 -> R_C30` row produces six proper-cubic guard records. All
six are explicit outputs. Together with the Cycle-135 H1, the two guards local
to `(5,-1,-2)` make this five-parent H0 local:

```text
BIT H1 + prior base H1 + prior base H0 + R_C30 + R_C30 -> H0.
```

The three non-guard entries are causally prior Cycle-135 base-variable records,
not supplied fixed records.

The H0 target is unique. The 9,278-row union is single-valued; its 142-output,
143-condition full compiler has zero unexpected targets. The directly
enumerated eight-write factor has 144 states, 496 edges, one terminal, and no
bad transition. H0 never precedes H1 or either local guard; deleting any one
of its five parents disables it.

The eight-write factor's completion barrier covers BIT H1 and the two guards;
its source already contains the other two base parents. The full-product joint
layer gate below proves that all three base parents are present before H0.

The stricter expected-target wrong-value screen finds 24 affected targets and
40 full condition fingerprints, all inherited unchanged from Cycle 135. Each
fingerprint retains the target, coordinate-normalized present set,
coordinate-normalized neighbourhood set, and value set; equality is not based
on collapsed target/value summaries or raw bit indexes. None is at BIT H1, a
guard, or the new H0; the new-output screen is empty. Cycle 135's exhaustively
enumerated full graph has zero bad transition, so none of those 40 conditions
is encountered while its target remains open. The dependency firewall below
proves the extension cannot
change an old still-open target neighbourhood or make one of those inherited
conditions newly reachable.

## Exact factorized full graph

The full graph is **not directly enumerated**. Its size is too large for the
ordinary append-graph runner, but its dependency product is exact and checked:

- each of the six guards neighbours source L4/L6 records only;
- no guard neighbours a variable Cycle-135 output or another guard;
- H0 neighbours exactly three prior Cycle-135 variables and the two local
  guards; all five are required by its row;
- H0 has exactly one compiled condition, with all five variable neighbours
  present and no alternate partial-parent H0 signature;
- the remaining four guards are not adjacent to H0;
- all 181 old nonparent condition fingerprints are exactly unchanged;
- the three parent conditions are exactly the Cycle-135 conditions with H0
  absent from the newly modeled neighbour slot; no parent condition has H0
  present;
- the ignored-target condition and its value are exactly unchanged.

These checks form the reachability firewall for the 40 inherited static
conditions: guards touch no base-variable target, while H0 touches only the
three base parents that its own row requires to be occupied first. The full
coordinate-normalized wrong-condition fingerprint is exactly equal before and
after the extension, with no new or lost entry. The stronger all-condition
comparison also excludes a new correct-valued condition enabling an old target
early.

Thus the pre-H0 graph is Cycle 135 times the six-bit guard cube `Q6`; the
H0-present layer is the joint-parent layer times `Q4`. An independent exact
traversal of all 6,936,208 Cycle-135 states counts the joint layer in which all
three H0 base parents are present:

```text
joint states       J_S = 65,792
joint old edges    J_E = 389,824
joint terminals          1
bad transitions          0.
```

With `S=6,936,208` and `E=53,907,076`, the checked decomposition is:

```text
states = 64 S + 16 J_S
edges  = 64 E + 192 S + 48 J_S + 16 J_E.
```

It gives:

```text
states       444,969,984
edges      4,791,200,000
terminals              1
terminal outputs      142.
```

The terminal count explicitly consumes Cycle 135's single terminal. At any
putative incomplete terminal, each missing guard remains enabled from its
source-only local; once all guards are present, H0 is the sole non-ignored
enabled action. After H0 forms, no non-ignored action remains. This is an exact
factorized census, not a capped enumeration, subtraction guess, or
extrapolation.

## Output control

Replacing the guarded H0 output with H1 leaves the unexpected-target screen
and 144/496 terminal factor clean, but it does **not** pass the stricter
expected-target wrong-value screen: one new alias appears at the prior BIT H1
site. Its full-history reachability is not tested.
Therefore the **output fork remains open**, but the swapped branch is not a
clean symmetric control. Cycle 136 establishes causal formation and completion
discipline for the H0 row; it does not yet derive H0 from geometry alone. No
wrong-value product or factorized-full-graph check is claimed for the swapped
H1 branch.

This is **not an eight-bit word** and **not an R_B01 writer**. Six later bits,
physical completion, and writer recurrence remain open. **No axiom addition follows**.

## N1–N8 no-go-discipline gate

Status: PASS for this bounded guarded-successor construction and exact product
census; FAIL for uniqueness, output selection, byte, writer, recurrence, or
axiom-need claims.

### N1 — Alternatives

The unguarded direct and unary routes failed in Cycle 135. The tested six-image
R_C30 guard is executable. Other guard roles, non-nearest paths, relocated
data geometry, and alternate outputs remain live.

### N2 — Residual independence

This construction separates a formation/order result from an unresolved
bit-value question; it does not prove that those questions are physically
independent. The H0 graph closes the former while the swapped-H1 control
exposes an unresolved static wrong-value alias. Two bits do not close eight-bit
payload, completion, writer reuse, or exact-law selection.

### N3 — Hidden conditions

All six guard coordinates, two local guards, H1/H0 coordinates, source-only
guard neighbourhoods, pairwise guard nonadjacency, three causally prior base
parents, the four guards nonadjacent to H0, 142 outputs, 143 conditions, factor
states, exact joint-layer traversal, product formula, all-condition and
wrong-value fingerprints, ignored-target safety, terminal enablement, and the
output swap's one new alias are explicit. No scheduler, supplied guard,
overwrite, clock, or reader is assumed.

### N4 — Residual matching

Cycle 135 names this exact guard candidate. Cycle 136 consumes it with every
co-image modeled. A generic byte or writer has a larger residual and is not
matched. A direct enumeration residual is replaced only because structural
independence proves the exact product.

### N5 — Resolution and rhetoric

Tested: exact raw rows, unexpected-target, all-condition, ignored-target, and
expected-target/wrong-value screens, complete eight-write factor, parent
deletions, dependency adjacency, independent 6.9-million-state joint-layer
traversal, exact state/edge product, terminal enablement, inherited-alias
reachability firewall, and an H1 output swap at compiler/factor scope. Not
tested: the swapped branch's
wrong-value reachability or full factorized graph, every guard, direct
enumeration of 444 million states, later bits, completion, or recurrence.
“Factorized graph closes” cannot become “Nature selects H0.”

### N6 — Partial closure and axiom discipline

The next finite step is a census for the third physical bit using the new H0
and modeled guard orbit. This remains within the same nearest-neighbour,
proper-cubic, append-only candidate framework and selects no axiom or import.

### N7 — Hostile steelman

A hostile reviewer should demand proof that factorization is exact, because a
compiler alone does not prove schedules and zero unexpected targets does not
exclude wrong values at expected targets. The runner checks both compiler
screens plus all old conditions and ignored values, proves no inherited bad
condition is encountered at an open target in Cycle 135, checks the
neighbourhood firewall, independently
enumerates the exact joint parent layer, and proves terminal enablement. The
reviewer should still refuse a bit-value or writer claim; that restriction is
adopted.

### N8 — Cross-cycle echo

Cycles 129, 132, and 135 progressively made provenance, cage closure, and the
first bit executable. Cycle 136 shows that covariant guard co-images can be
modeled rather than discarded, but also exposes a genuine output-selection
fork. The result sharpens the next science question without constitutional
promotion.

## Verification

```text
python3 scripts/c135_six_guard_h0_factorized_full_graph_cycle136_2026_07_15.py
```

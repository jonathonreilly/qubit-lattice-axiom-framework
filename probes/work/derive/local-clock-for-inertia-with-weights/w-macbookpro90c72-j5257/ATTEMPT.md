# J:derive:local-clock-for-inertia-with-weights:a1

Worker `w-macbookpro90c72-j5257` (claude-opus-5-5). This is attempt 1 of 4.

**Independence.** The claim tool printed the summary line of attempt a2 (`w-jonathonsmac4f50-j42a0`, claude-opus-5, unrefereed), which reported the three-record sector as feasible. I built my own machinery and results before opening its file. When I read it afterwards I found it had also reported the three- and four-record sectors together as infeasible on `3³`. It did not do the unit's part (c), and it stayed on the `3³` torus.

**Agreement with a2.**
- Three-record feasibility on `3³`.
- The distinct-equation counts: 332 at `c = 1` and 334 at `c₀`.
- The joint infeasibility on `3³`.

**New here:**
1. exact rules on the `4³` and `5³` tori too;
2. exact one-configuration certificates that the natural rules fail — local-clock moves, and unit moves — whatever the exchange rates, plus a certificate that no rule balances record by record;
3. the four-record obstruction needs no three-record rows at all;
4. part (c): the family enlarged by the head-on re-draw on the momentum class is still infeasible, with exact certificates;
5. the four-record obstruction on `Z³` itself, from compact clusters whose equations are the same on the `6³` and `9³` tori.

**Definitions** come from block 50 (#8562: its runner and `specs/supervisor_control_block50_refuter.py`), reproduced exactly in A1.

## (1) Exact statement

### Objects

These are block 50's objects.
- **Records and weights.** Six-axis contents `0..5 = ±x, ±y, ±z` on the `L³` torus. `π(C) = Π` over adjacent occupied pairs of `c ω(a, b)`, with `ω = p, q, r = 3, 1, 2`. We take `c = 1` and the neutral scale `c₀ = 1/2`.
- **Streaming.** The record at `x` with content `s` targets `x + e_s`. It enters the target if empty and exchanges contents if it is occupied.
- **A local rate.** Any nonnegative function of the canonical environment: the contents and occupancies of the 12 sites within distance one of `x` or of its target (11 on `3³`), taken up to the 8 lattice symmetries that fix the event.
- **The enlarged family (part (c)).** In addition, a head-on pair (the target holds `−s`) re-draws on its momentum class to `(a, −a)`, with `a` transverse to `s`, at its own local rates. A "nothing happens" event is a self-loop and cannot change stationarity.
- **The problem.** Find rates with every move rate `≥ 1` (positive, by scaling) and exchanges `≥ 0`, such that for every configuration `C` the flow of `π` out equals the flow in: `Σ_{events of C} π(C) r = Σ_{events into C} π(C'') r`.

### Theorem

Scope: the objects above, and exact rational arithmetic throughout.

1. **Three records: feasible.** Local rules exist on the `3³`, `4³` and `5³` tori at `c = 1` and at `c₀ = 1/2`. Exact rational rules are given, and every three-record configuration balances:
   - `3³`: 274 rate classes, 70,200 configurations;
   - `4³`: 353 classes, 421,848 configurations;
   - `5³`: 353 classes, 1,647,216 configurations.
2. **The natural rules fail, even at three records (on `3³`).**
   - (a) Local-clock moves: with every move at the local clock `1/π_x`, no choice of exchange rates balances the sector. One configuration is the witness at `c = 1` (two at `c₀`).
   - (b) Unit moves: the same holds with every move at rate 1. One configuration is the witness.
   - (c) No local rule balances each record's event against its own predecessor (record-wise balance). Five configurations at `c = 1`, six at `c₀`.
3. **Four records: infeasible.** On `3³` no local rule balances the four-record sector: 81 four-record configurations suffice at `c = 1`, 83 at `c₀`. That remains true with head-on pairs re-drawing on their momentum class: 81 and 110 configurations. So no local rule balances the three- and four-record sectors together. **On `Z³`** (step 6) the same holds: 74 and 50 compact four-record clusters for the base family, 73 and 33 with re-draws.
4. **Conservation.** Every event (move, exchange, head-on re-draw) conserves the number of records and the total content vector, whatever its rate.

**So:** a local rule exists for three records, but it is not a clock. Rule (1) is one vertex of a polytope of solutions, with no closed form found. From four records on, no rule of this locality survives, on `3³` or on `Z³`, even with the momentum-class re-draw.

## (2) Steps

1. **CHECKED (A1): the machinery is block 50's.**
   - On the `3³` torus at `c = 1` there are 70,200 three-record configurations with a record at the origin.
   - Every configuration has three events out and three in, so the global clock balances.
   - The local clock `1/π_x` fails at 3,168 configurations, with largest defect 3. These are block 50's numbers.

2. **PROVED (the linear feasibility problem).**
   - A configuration's balance is linear in the rates of the environments of its events out and of the events into it. The latter are found by the predecessor map: the record from the site behind, or the two contents exchanged back.
   - **Rates are translation- and symmetry-covariant.** So the configurations with a record at the origin give every equation, and symmetric configurations give identical equations: 332 or 334 distinct equations on `3³`, 484 on `4³`.
   - Everything is homogeneous, so "moves positive" can be normalised to "moves `≥ 1`".
   - **Farkas.** `{r : A r = 0, r ≥ ℓ}` (with `ℓ = 1` on moves and `0` on exchanges) is empty iff some `y` has `Aᵀy ≥ 0` and `y·Aℓ > 0`.
   - An LP solver (HiGHS) proposes. Exact rational arithmetic verifies (`check.py`; the proposals are made by `make_data.py` and `exactify.py`).

3. **CHECKED (A2): the three-record rules, exactly.**
   - **How they were found.** A vertex of the feasible set was found by LP. The equations were then re-solved in rationals on the solver's active set.
   - **The verified rules** (every configuration balanced, moves `≥ 1`, exchanges `≥ 0`):

     | torus | classes | moves | exchanges | largest rate |
     |---|---|---|---|---|
     | `3³` | 274 | 228 | 46 | 21 (`c = 1`), 9 (`c₀`) |
     | `4³` | 353 | 293 | 60 | 21 (`c = 1`), 31/2 (`c₀`) |

   - On `5³`: 353 classes and 571 distinct equations; all 1,647,216 configurations balance.
   - Classes that never appear in a non-trivial equation cancel in every balance and may take any rate.

4. **CHECKED (A3, A4): the natural rules are impossible.**
   - **Local clock, `c = 1`.** The witness is three `+y` records at `(0,0,0)`, `(0,0,1)` and `(0,1,0)` on `3³`. Its only exchange swaps two equal contents and cancels, so its balance, with moves at the local clock, involves no exchange class and is violated. No exchange rates can repair it.
   - **Local clock, `c₀`.** Two configurations suffice, and they involve two exchange classes with a certificate of one sign.
   - **Unit moves.** One configuration at each scale. At `c = 1` it is three `+x` records filling a line along `z`: each record's predecessor stood one site behind, where it touched nothing.
   - **Record-wise balance** (each record's outgoing flux equal to its own predecessor's): the equations are infeasible with 5 configurations (`c = 1`) and 6 (`c₀`).
   - **What this means.** Any local balance must trade flux between different records.

5. **CHECKED (A5): four records, exactly.**
   - **The base family.** The joint LP on the three- and four-record sectors of `3³` has 3,439,800 configurations and 3,733 environment classes (up to three other records). It is infeasible. The solver proposed a minimal-`ℓ₁` Farkas vector. On its support the active constraints are then solved exactly; the solution is unique, and every `(Aᵀy)_j ≥ 0` holds exactly with `y·Aℓ = 1`.
   - **The support is four-record rows only:** 81 at `c = 1` and 83 at `c₀`. So the four-record sector alone admits no local rule.
   - **With head-on re-draws** (4,505 classes, including 772 re-draw classes), still infeasible: 81 and 110 four-record configurations.

6. **CHECKED (A7): the obstruction on `Z³`.**
   - **The rows.** On the `6³` torus take every three- and four-record configuration with a record at the origin and the others in the box `[0,2]³`. That gives 3,439,800 configurations, with 4,907 classes (5,860 with re-draws).
   - **The certificates.** The LP on this subset of rows is infeasible for both families at both scales. The exact certificates use four-record clusters only: 74 and 50 for the base family, 73 and 33 with re-draws.
   - **Why these are `Z³` equations.** Every supporting row is recomputed on the `9³` torus and is identical: the same environment classes and the same coefficients. So no wrap-around enters, and these are equations of the problem on `Z³`.
   - **Conclusion.** A certificate for a subset of the equations excludes every rate function. So on `Z³` no radius-one rule, with or without the head-on re-draw, keeps `π` stationary on the four-record sector.

7. **CHECKED (A6): conservation.**
   - Moves and exchanges keep the number of records and the content multiset. A head-on re-draw `(s, −s) → (a, −a)` keeps the total `0`.
   - So number and momentum are conserved event by event for any rates. Stationarity is the only question.

### INFO

- The feasible set on `3³` is a polytope. The minimal-sum vertex is irregular: 180 of the 228 move rates exceed 1. No closed form was found, and a2 reports the dimension of the solution space as 58.

### ASSUMED

- Only block 50's definitions and the locality class stated by the unit: sites within distance one of the two sites of the event, up to the event's symmetries.
- Rates outside the classes that occur are unconstrained.

## (3) Where the route stops

- **Tori.** The three-record feasibility is established on `3³`, `4³` and `5³` only, not on `Z³`. A `Z³` statement at three records needs the non-wrapping constraints of larger tori.
- **The four-record obstruction** is exact on `3³`, and on `Z³` through compact clusters (step 6). The three-record sector on `Z³` is open: feasibility needs all its equations, not a subset.
- **A larger locality class** (distance two) is not tried. It might dissolve the four-record obstruction.

## (4) What would finish it

- The three-record sector on `Z³`: compact clusters on a non-wrapping torus, as in step 6, but for feasibility.
- A larger locality class at four records.
- A closed form, if any, on the three-record polytope.
- A referee from another model family, particularly for the certificates. Block 50, a2 and this attempt are the same family.

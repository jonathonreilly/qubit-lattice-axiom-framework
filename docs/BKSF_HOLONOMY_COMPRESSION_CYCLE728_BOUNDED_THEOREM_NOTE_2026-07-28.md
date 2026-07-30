# Cycle 728: an exact marked-edge GF(2) telescope on a finite reference ring

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Primary runner:

- [`frontier_cycle728_bksf_holonomy_compression_2026_07_28.py`](../scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py)

Independent check:

- [`frontier_cycle728_holonomy_independent_check_2026_07_28.py`](../scripts/frontier_cycle728_holonomy_independent_check_2026_07_28.py)

Load-bearing bounded inputs:

- the [recurrent two-rail controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
  supplies the finite ring programs and the rail permutation used in the
  pullback check;
- the [per-station refusal wrapper](REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md)
  fixes the still-unintegrated enforcement context; and
- the [radius-one refusal guard](LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md)
  is the immediate bounded parent whose global one-token condition remains
  supplied rather than locally enforced.

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. The three linked inputs are themselves unaudited bounded claims.

## Exact conditional result

Fix a finite periodic binary ring with sites `s`, two rail bits `A_s,B_s`,
one supplied reference bit `r_s` per site, a chosen marked edge
`s* -> s*+1`, and one supplied auxiliary bit `h`. Define

```text
L_s    = A_s XOR B_s XOR r_s XOR r_(s+1),             s != s*
L_s*   = A_s XOR B_s XOR r_s XOR r_(s+1) XOR h.
```

The package proves the following statements for this declared row system.

- **Correction of the first proposed expression.** The XOR of consecutive
  reference agreements is
  `XOR_s (1 XOR r_s XOR r_(s+1)) = n mod 2`. It is a state-independent
  affine translate of the difference coboundary, whose own closed-ring XOR
  is zero; it is not itself a coboundary on odd rings and is not a variable
  reference degree of freedom. Exhaustive reference censuses give the single
  value zero on all 1,024 ring-10 states and one on all 2,048 ring-11 states.
- **Telescope identity.** Direct GF(2) cancellation gives
  `XOR_s L_s = parity(A XOR B) XOR h`. The primary verifies the coefficient
  identity on the held 11-, 35-, and 130-site programs and exhaustively over
  all `2^22` ring-11 rail assignments; the independent checker reconstructs
  it without importing the primary.
- **The solution-set quantifiers are different in the two directions.**
  For every full assignment `(A,B,r,h)`, `L_s=0` for every `s` implies
  `parity(A XOR B)=h`. At fixed `r` and fixed `h`, exactly `2^11=2,048`
  ring-11 rail assignments satisfy every row. Conversely, after existential
  projection over the supplied reference chain, every rail assignment with
  `parity(A XOR B)=h` has exactly two satisfying reference extensions,
  related by global reference complement. Thus the projected ring-11 set is
  exactly the `2^21=2,097,152`-state parity sector, with 4,194,304 satisfying
  `(A,B,r)` extensions per `h`. No fixed reference chain realizes that whole
  projected sector.
- **Correctly quantified radius-one counterpairs.** On the 11-site ring,
  each of the nine radius-one raw-data windows that excludes the marked edge
  has its own satisfying pair with different `h` and identical
  `(A,B,r)` data on that window:
  `for every eligible W, there exists a W-dependent pair`. The frozen
  center-8 representative is `(A,r,h)=(0,0,0)` versus `(4,6,1)`. It is
  indistinguishable on seven of the nine eligible windows, not all nine.
  Therefore each tested radius-one window individually fails to determine
  `h` on this row solution set. This is not an arbitrary-radius statement.
- **Conditional controller pullback.** With the imported controller rail
  permutation and static `r,h`, the individual row family is not permuted,
  while total rail parity and `parity(A XOR B) XOR h` are invariant. The
  frozen counterexample and basis checks distinguish these two facts.

Within this specified periodic incidence-row presentation, the parity
obstruction is one-dimensional and one auxiliary binary twist datum is
sufficient to represent both parity sectors. The theorem makes no claim that
a separately localized bit is unique or minimal across other presentations.

## Supplied, derived, and open

### Supplied conditions

- the finite mode graph and periodic binary ring;
- the clean reference chain, the marked edge, and the auxiliary bit `h`;
- static references and `h` during the imported controller pullback;
- the linked controller inventory and its supplied one-token initial
  condition.

These are explicit conditions of the theorem, not derived framework facts.

### Derived statements

- the state-independence of the proposed agreement XOR and the zero telescope
  of the difference coboundary;
- the marked-edge row telescope;
- the universal implication on full assignments and the converse after
  existential reference-chain projection, including exact ring-11 counts;
- the `for every window, there exists a window-dependent pair` radius-one
  census on the 11-site ring;
- the conditional rail-pullback and total-parity invariance results.

### Non-authoritative terminology

The chosen edge and the bit `h` are a presentation convention. Calling `h`
a “holonomy” or identifying it with a controller-level physical remainder is
not part of this theorem. The legacy artifact filenames retain that historical
label only as stable repository identifiers.

### Open

- integrating these rows into the refusal wrapper as an enforced admission
  condition;
- preparing the reference chain and `h` autonomously;
- testing antiperiodic boundary labels, moved or distributed seams,
  larger-radius or multiscale constraints, reversible parity accumulators,
  preparation/admission dynamics, and other auxiliary-field presentations;
- occurrence, physical time, Record formation, Born weighting, and source
  meaning at their inherited scopes.

## Negative-claim boundary

The formula-level correction is only the exact finite-ring identity
`XOR_s(1 XOR r_s XOR r_(s+1))=n mod 2`; it does not refute other holonomy
definitions. The locality result is only the nine eligible radius-one windows
on the 11-site declared row ansatz and has the explicit `for every window,
there exists a pair` quantifier. The live alternative presentations listed
above are not ruled out. No new-axiom, route-independent no-go, arbitrary
bounded-window, controller-completion, or encoding-minimality claim is made.

## Verdict

The retained result is a conditional finite-ring GF(2) lemma: a chosen
marked-edge bit yields an exact telescope and an exact parity-sector
projection for the specified rows. The first proposed agreement expression
is corrected to a state-independent affine ring-size-parity constant. The
controller-level label, autonomous preparation, enforcement integration, and
representation-independent minimality remain open.

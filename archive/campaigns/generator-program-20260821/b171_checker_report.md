# Block 171 — DISJOINT CHECKER report

INERTIA CONVENTION, with teeth: every triple below is `(n_+, n_-, n_0)`, the b165 `real_symmetric_inertia`
order, written `(a,b,c)(n+,n-,n0)[b165]`.

MACHINERY DISJOINTNESS. `block171_solve.py` was read as TEXT ONLY, never imported or executed. Every number
below comes from `$S/_ck_lib.py` + `$S/_ck_c{1,23,4,56,68,7b}.py`, which take the committed fixture / region pin
/ carrier map / descent / quotient / holonomy-dial constructor from the LANDED `scripts/` chain (b170 -> b168 ->
b166 -> b165) and then use an INDEPENDENT route: complex inverse via the real `2N x 2N` embedding
`[[Re,-Im],[Im,Re]]` solved over `QQ` (never `DomainMatrix` over `QQ_I`, never LU on the complex matrix);
inertia via my own symmetric-pivoting congruence on that embedding, halved, cross-checked against Sylvester
leading minors. Grams are built at FULL `N x N` then compressed — the solve builds them at block scope,
deliberately the other way round. Exact rationals; no float; no `nsimplify`. NO repo edits, no git writes (the one dirty tracked file, the campaign handoff note, was already dirty on arrival). Logs: `_ck_c{1,23,4,56,68}.txt`.

## VERDICT VECTOR

| C1 positivity theorem | **CONFIRMED** |
|---|---|
| C2 trilemma table / winning set / twin separation | **CONFIRMED** |
| C3 S1+S2 and the record-blindness corollary | **CONFIRMED** |
| C4 K2 failure = slot-order premise | **CONFIRMED-WITH-CORRECTION** (x3) |
| C5 pre-census | **CONFIRMED** (counted twice, independently) |
| C6 the two null fixtures | **REFUTED as stated** |
| C7 machinery gate | **CONFIRMED-WITH-CORRECTION** |
| C8 quantifier hygiene | 5 defects, one of them arithmetic |

## C1 — THE POSITIVITY THEOREM. **CONFIRMED.**

The printed identity is TRUE as printed. My derivation, three lines, no entries: `Q^-1 herm(Q) Q^-dag =
(1/2)(Q^-1 Q Q^-dag + Q^-1 Q^dag Q^-dag) = (1/2)(Q^-dag + Q^-1) = herm(Q^-1)`, using `Q^dag Q^-dag = 1`. So
`herm(Q^-1)` is literally a CONGRUENCE `X herm(Q) X^dag` with `X = Q^-1`, and Sylvester gives PD -> PD.
Nonsingularity is not an extra hypothesis: `herm(Q) > 0` forces it, since `Qv = 0` would give `v^dag herm(Q) v =
Re(v^dag Q v) = 0`. Verified on a generic symbolic complex `2x2` (adjugate inverse, full simplify), on three
exact random complex `5x5`, then entry for entry on the committed action at both extents.

PD measured entry-independently by my congruence route, at the probe carrier, `s_x = 3/5`, `s_t = 0`, `sigma =
3/5`: `herm(Q)` at `m = 1` and `m = 3`, `herm(Q^-1)`, and `Q^dag herm(Q)^-1 Q` are all
`(24,0,0)(n+,n-,n0)[b165]` at 12x4 and all `(16,0,0)(n+,n-,n0)[b165]` at 8x4. Sylvester leading minors on
`herm(Q)` agree — a second route. The W10 identity and `A^dag = -A` check entry for entry at both extents; the
RS compressed blocks of W6, W7, W9, W10 are all `(4,0,0)(n+,n-,n0)[b165]`. The "census, not a theorem in `m` and
the moduli" hedge is correct and correctly placed.

## C2 — THE TRILEMMA TABLE. **CONFIRMED.**

I rebuilt legs (i)/(ii)/(iii) for ALL SEVEN battery rows at 12x4 RS. Winning set = `{W6, W7, W9, W10}` exactly
as claimed; deep-memory subset (moved by a record at the FARTHEST free level) = `{W9, W10}` exactly as claimed.
Anchors reproduce: W1 measures `same` on ALL FIVE dials at BOTH scopes (leg iii F — the margin theorem's
prediction); W5 is `undefined` at connection-off (leg i F) and `same` on the `s_x` dial (the degree-2
homogeneity signature); at SC scope all seven rows have an EMPTY mover set (leg ii F, 7 of 7).

Leg (iii) at `T_phys = 6` under the general complex holonomy dial `(g_re, g_im) = (1/3, 1/4)`, records fixed:
**the W9 profile MOVES on both holonomy dials**, by exact rationals (`holo_t` max coordinate move: 179-digit
numerator over 181-digit denominator, full value in `_ck_c23.txt`). **Its shim twin `W2 = herm(Q)^-1` does not
move at all** — and the separation is STRONGER than the solve claims: I measured it at the MATRIX level, not the
profile level. `herm(Q_holo_t) = herm(Q_holo_x) = herm(Q)` entry for entry, so `herm(Q)^-1` is invariant under
the general complex holonomy, not merely under `s_t`/`s_x`. Both directions of the anti-shim separation hold.
`W2 ==` the connection-off covariance entrywise: reproduced.

## C3 — S1 / S2 AND THE COROLLARY. **CONFIRMED.**

Symbolic, my route, both extents. S1: at `s_t = 0` on the region, `Q[c,k] = Q[k,c] = 0` for every `k` outside
slice `c`, in all free symbols. S2: `Q[c,c]`'s symbols are exactly `{m, s_x, n_(0,.), n_(1,.), u_(0,.)}` (14 of
them), disjoint from `free_shears` (16 at 12x4, 8 at 8x4). Scope probe I added: with `s_t` LEFT FREE the block-
diagonality FAILS at both extents — S1 is an `s_t = 0` fact, not a region-pin fact alone, as the findings say.

The functional-calculus step is AIRTIGHT for the ratio-of-functionals weights actually used, and normalization
does NOT leak slice-c dependence back in. Two measurements: (a) `f(Q)_cc == f(Q_cc)` entry for entry for all
seven of `W1, W2, W5, W6, W7, W9, W10` at both extents; (b) each of `W2, W6, W7, W9, W10` is ITSELF block-
diagonal w.r.t. slice `c`, so the denominator `tr(B)` is a sum over slice-`c` entries only — numerator and
denominator are both functionals of `Q_cc` alone. No cross-slice normalizer exists anywhere in the battery, so
there is no leak channel. Leg (ii) at SC: mover set empty for all 7 rows, both extents.

## C4 — K2 FAILURE / SLOT-ORDER PREMISE. **CONFIRMED-WITH-CORRECTION.**

Reproduced with my own record-extension map: at 12x4 the two slot orders give `1518449.../19572883...` and
`820524.../11139337...`, defect `15283437.../38996599...` — matching the solve's printed rationals DIGIT FOR
DIGIT, likewise at 8x4. K1 (G-A) holds; K1 (G-B) defect nonzero at both extents (193-digit numerator over
192-digit denominator at 12x4), each of the four ratios in `(0,2)` so the sum sits near `|A_v| = 4` —
structural, confirmed. K2 at the action level (disjoint-cell substitutions commute, free symbols surviving)
confirmed at both extents.

**THE PREMISE IS REAL — I could not dissolve it.** I built a genuine G-A chain the solve did not run: slots =
two DISTINCT free time levels, records implemented as the DECLARED disconnection pin `sigma -> 0` (N1), class
read AT THE SLOT BEING FILLED rather than always at `t*`. It is order-dependent too, by an exact nonzero
rational at BOTH extents. The honest G-B chain (value alphabet, by-fiat normalization) is likewise order-
dependent at both extents. Three corrections to how the premise is stated:

1. **The solve's own K2 witness is mis-wired and should not be the exhibit.** Both records sit at level `t*`,
which IS the read slice; under CM-SITE the two class events at one slice are the mutually ORTHOGONAL `Pi_0,
Pi_1` (`Pi_0 Pi_1 = 0`), so their "joint" is 0 in any projective reading and the product of two same-slice
conditionals is not a joint of the declared class map at all. My distinct-slot chain is the exhibit that carries
the claim.
2. **The witness mixes wirings.** Record VALUES `1/5` and `2/5` are the G-B CM-VALUE alphabet while the class
INDEX is the site (G-A/CM-SITE) — contradicting N1, "the recording rule IS the disconnection rule".
3. **The failure belongs to the CHAIN-RULE construction, not to the weight.** The equally natural one-shot
(Gibbs) joint over the two link slots, `J(s1,s2) = W({L1:s1,L2:s2}) / sum_{u1,u2} W({L1:u1,L2:u2})`, depends
only on the record SET and is EXACTLY invariant under re-enumeration — verified exact at both extents. So the
honest statement is not "the generator is order-dependent" but: *the forward (Ionescu-Tulcea) construction the
owner's "no completed future" directive forces is order-dependent, and the order-independent alternative is the
one-shot family, which is exactly what K1 (G-B) kills.* Same owner-visible premise, correctly rooted — the root
is the failure of Kolmogorov consistency, and the slot order is its price.

Also: **K1 (G-A) is true but content-free.** With `Pi_a` the `L_x` DIAGONAL site projectors, `sum_a tr(G Pi_a) =
tr(G)` says "the diagonal entries sum to the trace" — true for every `4x4` matrix, Hermitian or not, for every
`G`, action and trail. Calling it a theorem that "lifts by induction to every `T`" is accurate but overstates
its work: the Ionescu-Tulcea normalization hypothesis is discharged by the DEFINITION of the ratio, not by this
identity.

## C5 — THE PRE-CENSUS. **CONFIRMED** (verdict-critical, so counted twice).

(a) Recounted from `b171_profile_table.py` by pure `Fraction` arithmetic: at 12x4, **16 of 16 distinct weight
profiles; 10 of 16 distinct frequency profiles; 0 weight profiles carrying two frequency profiles; 6 of the 10
frequency profiles carrying TWO distinct weight profiles.** Identical at 8x4. Every profile sums to 1 exactly
and is strictly positive. (b) Rebuilt **22 of the 32 rows** from the committed action with my own route (all 16
at 12x4, plus 6 at 8x4): **zero mismatches**, entry for entry. Recomputed the 12x4 census from MY rebuild alone:
16/16, 10, 6 — same. The `(0,1)`/`(1,0)` collision has exact separation `max_i |p_i - q_i| =
2422366.../2565726...` (121-digit numerator over a 127-digit denominator).

The "10" is forced combinatorially and needs no run: the frequency profile of a length-2 trail is its multiset,
`C(5,2) = 10` multisets, `C(4,2) = 6` doubly covered. Collisions exist as soon as the 16 weights are pairwise
distinct, which they are. **B2's zero-collision branch is unreachable on this alphabet: CONFIRMED, and the
original census leans to AXIOM.**

## C6 — THE NULL FIXTURES. **REFUTED as stated.**

Confirmed parts: graded `x`-homogeneity is true and trivial (`(3t+5x) mod 5 = 3t mod 5`, checked over every
`(t,x)`, both extents); the `x`-inhomogeneous probe carrier IS inside the positive region — `[rQ]_(S,S) =
(4,0,4)(n+,n-,n0)[b165]` at both extents by my own inertia route (landed graded carrier: same triple).

REFUTED: "*so on it EVERY site profile is exactly `(1/4,1/4,1/4,1/4)` at both scopes for every construction in
the battery*" — the same wording is shipped into `b171_profile_table.NULL_FIXTURES`, which is what B2 will read.
The solve measured 2 of the 14 (weight, scope) cells (`W1` at SC, `W9` at RS); I measured all 14 at both
extents. **On BOTH claimed null carriers, `W5`, `W6` and `W7` have NON-UNIFORM RS profiles at both extents.**
Counter-computation, 12x4:

    flat   RS W6 = Q^dag Q         (123983/487832, 119933/487832, 123983/487832, 119933/487832)
    flat   RS W7 = herm(Q)+A^dag A (24977/97883, 47929/195766, 24977/97883, 47929/195766)
    flat   RS W5 = A^dag A         (953/3587, 1681/7174, 953/3587, 1681/7174)
    graded RS W6                   (4661387/18216248, 4446737/18216248, 4661387/18216248, 4446737/18216248)
    graded RS W7                   (307001/1192229, 578227/2384458, 307001/1192229, 578227/2384458)
    graded RS W5                   (36467/133943, 61009/267886, 36467/133943, 61009/267886)

(8x4 likewise; the flat-carrier triples coincide at the two extents; full list in `_ck_c68.txt`.) `W6` and `W7`
are half the declared winning set, so "nothing may be benched there" is wrong for half of it. CORRECTION, exact:
*flat and graded are null fixtures for the `herm(Q)`- and inverse-derived weights (`W1, W2, W9, W10`) at both
scopes and for every battery weight at SC scope; they are NOT null for the `A^dag A`-carrying weights (`W5, W6,
W7`) at RS scope, where the profile is x-PERIOD-2, not constant.* No trilemma verdict moves — the candidate W9
IS null on both carriers, so the probe carrier's disclosure remains necessary — but the note handed to B2
licenses skipping a control B2 needs.

## C7 — THE MACHINERY GATE. **CONFIRMED-WITH-CORRECTION.**

The agreement is real, and I reproduced it where it matters: on holonomy-dialled actions (`g_re = 1/3, g_im =
1/4`, both `holo_t` and `holo_x`) the solve's `DomainMatrix.to_field().inv()` agrees with my real-embedding
inverse ENTRY FOR ENTRY at 8x4 AND 12x4, and my inverse satisfies `Q Q^-1 = 1` exactly at every point used (12x4
`holo_t`: mine 0.40 s, `DomainMatrix` 0.06 s). CORRECTION: the solve's own gate is measured in the wrong place —
it compares `DomainMatrix` against the landed LU route only on the COMMITTED action (`s_t = 0`), exactly where
LU was never in doubt; on the dialled action, the only place `exact_inv` is load-bearing, nothing is gated. I
confirm the docstring's premise from the other side: landed `sp.inv(method="LU")` on the DIALLED action did not
terminate at 8x4 (16x16) after 7.5 minutes, so the gate as designed could not have run there.

## C8 — QUANTIFIER HYGIENE SWEEP

1. **ARITHMETIC ERROR (findings section 2).** "16 at 12x4, 8 at 8x4 (`2 L_x (T_phys - 2)`)": counts right,
formula wrong — `2 L_x (T_phys-2)` gives 32 and 16. Correct closed form `L_x (T_phys - 2)`; measured 16 and 8.
(The solve's check compares against the literals, so it passed while carrying the wrong formula in its own
statement string.)
2. **Over-quantified and false** — the null-fixture sentence, see C6.
3. **Two different predicates called `iii = P` in one table.** W1..W10 score leg (iii) as `conn_off AND s_x AND
holo_t AND holo_x` all "differ"; the W8 row's leg-(iii) check tests only `conn_off` and `s_x`. W8's "leg (iii)
P" is not the table's `iii = P`.
4. **Unmeasured cell.** W3/W4 is printed `P F F`, but leg (i) for W3/W4 is never measured. I measured it:
`(4,0,0)(n+,n-,n0)[b165]` at both extents — correct, but asserted rather than measured.
5. **Two of the four leg-(iii) dials leave the positive region, undisclosed.** My 12x4 measurement of
`[rQ]_(S,S)`: bench `(4,0,4)(n+,n-,n0)[b165]`; `s_t = 1/8` `(4,4,0)`; `holo_t` `(4,4,0)`; `holo_x` `(4,0,4)`.
`herm(Q)` is `(24,0,0)` and the W9 RS block `(4,0,0)` at all four, so leg (i) survives everywhere; the verdict
survives too, since `conn_off`, the `s_x` dial and `holo_x` are all in-region and W9 differs on all three. But
the findings assert "the region pin's remaining job is to define the alphabet" in the very section where two
dials silently leave the region.
6. No float, no `nsimplify` in the solve text or the findings (grep: the only decimal literals are
`f"{elapsed:.1f}s"` runtime stamps). Every separation I re-derived came out an exact rational. No `T = 4`-only
verdict-bearing statement found; 8x4 is carried as a disclosed cross-check everywhere.
7. Pre-registration, worth naming: scouting fixed the `s_x` and connection-off columns before registration, and
the registered 12x4 verdict list is `{W2, W5, W7, W10}` — so the CANDIDATE W9's own `s_x` and connection-off
entries are scouted, not pre-registered. Disclosed, but that is the one row where it matters most.

## DISCOVERED LEMMAS

**L1. `herm(Q)` is exactly invariant under the FULL complex holonomy dial** — not merely "carries no `s_t`,
`s_x`" (S3). `herm(Q_holo_t) = herm(Q_holo_x) = herm(Q)` entry for entry at the bench, including the real part
`g_re = 1/3` (while `[rQ]_(S,S)` flips to `(4,4,0)(n+,n-,n0)[b165]` under `holo_t`). So every weight in the
closure of `{herm(Q), herm(Q)^-1}` under sums, products and inverses is blind to the general complex holonomy,
and the W9/W2 separation is a separation against that whole invariant subalgebra, not against one dial.

**L2. Carrier `x`-homogeneity buys PERIOD 2, not uniformity.** On both `x`-homogeneous carriers the RS site
profiles of `W5, W6, W7` are exactly `(a,b,a,b)` with `a != b`, both extents: the residual spatial symmetry of
the committed construction is translation by 2 (the chart lattice of `connection_gen`'s `ORIGINS`), not by 1.
Uniformity is an extra fact about the `herm(Q)`-derived weights, not a consequence of the carrier. **This is the
correct null control for B2:** on an `x`-homogeneous carrier the null hypothesis is "2-periodic in `x`", and a
census testing exact uniformity will mis-classify every `A^dag A`-carrying weight.

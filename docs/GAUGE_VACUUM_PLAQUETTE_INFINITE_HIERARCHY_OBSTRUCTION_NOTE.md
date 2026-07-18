# Gauge-Vacuum Plaquette Infinite-Hierarchy Obstruction

**Date:** 2026-04-16
**Status:** support - exact obstruction theorem on the finite Wilson source surface; explicit connected-hierarchy closure at `beta = 6` still open
**Script:** `scripts/frontier_gauge_vacuum_plaquette_infinite_hierarchy_obstruction.py`

## Question

After identifying the remaining gap as the explicit connected plaquette
hierarchy, can that hierarchy close exactly at some finite order?

## Answer

No.

On both the local one-plaquette block and the full finite Wilson source
surface, the diagonal source generator is exactly nonpolynomial. Therefore the
connected hierarchy cannot truncate at any finite order.

This does not close analytic `P(6)`. It proves only that, within the diagonal
Taylor/cumulant representation, exact closure cannot be literal finite-support
truncation. Finite-dimensional recurrences, differential equations,
nonpolynomial parameterizations, and other exact representations remain
unrestricted.

## Setup

For the finite Wilson source surface define the diagonal generator

`K_L(t) = W_L[t 1; 0] = log Z_L(t) - log Z_L(0)`

where `1` is the uniform plaquette-source vector. Then

`K_L'(t) = N_plaq P_L(t)`.

Similarly for the one-plaquette block,

`K_1(t) = log Z_1plaq(t) - log Z_1plaq(0)`,

so

`K_1'(t) = P_1plaq(t)`.

The exact connected hierarchy on the diagonal source surface is encoded in the
Taylor coefficients of these generators.

If the diagonal hierarchy truncated exactly at order `N`, then `K(t)` would be
a polynomial of degree at most `N`.

## Theorem 1: polynomial truncation is impossible for the local one-plaquette block

The local exact plaquette satisfies:

- `P_1plaq(0) = 0`,
- `0 <= P_1plaq(t) < 1` for finite `t`,
- `P_1plaq(t) -> 1` as `t -> infinity`.

Suppose the local diagonal hierarchy truncated at finite order. Then
`K_1(t)` would be a polynomial, so `P_1plaq(t) = K_1'(t)` would also be a
polynomial.

But any polynomial with a finite limit as `t -> infinity` is constant.
Therefore `P_1plaq(t)` would have to be constant.

That contradicts `P_1plaq(0)=0` and `lim_(t->infinity) P_1plaq(t)=1`.

So:

> the local one-plaquette connected hierarchy does not truncate at any finite
> order.

## Theorem 2: polynomial truncation is impossible for the finite Wilson surface

On every finite periodic Wilson `L^4` surface,

- `P_L(0) = 0`,
- `0 <= P_L(t) < 1` for finite `t`,
- `P_L(t) -> 1` as `t -> infinity` by compact Laplace concentration on the
  maximum-action gauge orbit.

If the full diagonal connected hierarchy truncated at finite order, then
`K_L(t)` would be a polynomial and therefore `P_L(t) = K_L'(t)/N_plaq` would
also be a polynomial.

Again, any polynomial with a finite limit at infinity is constant. So `P_L`
would have to be constant, contradicting `P_L(0)=0` and `lim_(t->infinity)
P_L(t)=1`.

Therefore:

> the finite Wilson diagonal connected plaquette hierarchy does not truncate at
> any finite order.

## Corollary: what remains open

Within the diagonal Taylor representation, the remaining analytic gap is not
an exact finite-support coefficient list. The source surface here is only the
finite periodic Wilson surface defined above; no physical identification is
used.

This rules out one tempting hope:

> analytic plaquette closure cannot come from an exact finite-order connected
> cumulant truncation.

This statement does not restrict finite recurrences, Picard-Fuchs or other
differential descriptions, spectral-measure generators, or nonpolynomial
closed forms.

## What this closes

- exact obstruction to finite-order diagonal connected-hierarchy truncation
- exact obstruction to finite-order polynomial closure of the diagonal source
  generator
- sharper identification of the remaining plaquette gap

## What this does not close

- an explicit nonpolynomial solution of the connected hierarchy
- an explicit closed form for `chi_L(beta)`
- analytic closure of `P(6)`
- repo-wide repinning of the canonical plaquette

## No-Go Discipline Gate

The negative claim is the narrow mathematical statement that the diagonal
connected-cumulant Taylor series cannot have literal finite support. It is not a
claim that all finite-dimensional or exact closure representations fail.

### N1 — alternative attacks on the narrow claim

1. **Polynomial cancellation (`ATTEMPTED`).** A nonconstant polynomial
   derivative cannot remain bounded with a finite limit on the positive real
   axis, so cancellations cannot reconcile finite support with the two
   endpoints.
2. **Complex zeros of `Z` (`ATTEMPTED`).** The proof uses real analyticity and
   continuation along the positive real axis only; no zero-free complex
   logarithm is assumed.
3. **Periodic `L = 2` identifications (`ATTEMPTED`).** They can change higher
   Taylor coefficients but not compactness, nonconstancy, or the endpoint
   contradiction used here.
4. **Degenerate maximum-action configurations (`ATTEMPTED`).** Compact Laplace
   concentration needs only that every maximizer has `S_L/N_plaq = 1`; it does
   not require a unique maximizing configuration.
5. **Inverse-coordinate reparameterization (`ATTEMPTED`).** The defined
   coordinate rewrites `P_L`; it does not make `K_L` a finite-degree polynomial
   and therefore does not evade the finite-support contradiction.

### N2–N6 — walls, imports, and rhetoric

- **N2:** there is one claimed obstruction, literal finite Taylor support; no
  independent wall count is asserted.
- **N3:** compactness, Haar measure, analyticity on the real axis, and endpoint
  limits are explicit proved inputs. No hidden framework or bridge premise is
  used.
- **N4:** no prior no-go is used as a load-bearing witness. The linked companion
  notes supply analytic premises only.
- **N5:** the rhetoric is restricted to the diagonal Taylor/cumulant
  representation at every occurrence.
- **N6:** finite recurrences, differential equations, spectral measures, and
  other nonpolynomial representations remain explicit partial-closure paths;
  no new axiom is declared necessary.

### N7 — steelman

A finite-dimensional Picard-Fuchs system, a compact spectral measure, or
another exact nonpolynomial generating object could close the Wilson response
without truncating a single connected cumulant. That is a strong route against
any broad “infinite hierarchy means no finite closure” claim, so the theorem is
deliberately narrower: it excludes only literal finite-support truncation.

### N8 — cross-cycle echo

The [low-rank Picard-Fuchs](SU3_LOW_RANK_IRREP_PICARD_FUCHS_ODES_NOTE_2026-05-05.md)
and [compact spectral-measure](GAUGE_VACUUM_PLAQUETTE_SPECTRAL_MEASURE_THEOREM_NOTE.md)
notes in this same plaquette lane exhibit precisely the kinds of nontruncating
finite descriptions that broad obstruction rhetoric would miss. Their
existence confirms the narrowing above; neither is ruled out by this theorem.

**Gate result:** `PASS` for the narrow literal-finite-support obstruction.

## Commands run

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_infinite_hierarchy_obstruction.py
```

Expected summary:

- `THEOREM PASS=4 SUPPORT=3 FAIL=0`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

The earlier conditional verdict flagged the asserted endpoint/asymptotic Wilson-surface premises (`P_L(0) = 0`, `lim_(t -> infinity) P_L(t) = 1` by compact Laplace concentration on the maximum-action set). The finite-volume compact-Laplace argument and both response endpoints are proved in:

- [gauge_vacuum_plaquette_reduction_existence_theorem_note](GAUGE_VACUUM_PLAQUETTE_REDUCTION_EXISTENCE_THEOREM_NOTE.md) — supplies the finite Wilson endpoint proof. This note does not consume the defined inverse-coordinate equality as a reduction mechanism, and no source note sets the upstream audit status. The local algebra here (finite Taylor support implies polynomial `K(t)`) is unchanged by that uplink.
- [gauge_vacuum_plaquette_hierarchy_obstruction_lemmas_bounded_note_2026-05-10](GAUGE_VACUUM_PLAQUETTE_HIERARCHY_OBSTRUCTION_LEMMAS_BOUNDED_NOTE_2026-05-10.md) — companion bounded note added 2026-05-10 supplying the four analytic premises flagged by the 2026-05-02 audit verdict (one-plaquette endpoints `P_1plaq(0) = 0`, `P_1plaq(t) → 1`; finite-periodic Wilson endpoints `P_L(0) = 0`, `P_L(t) → 1`; finite Taylor support ⟺ polynomial `K(t)` globally on `R`; global-vs-formal convention check). The four lemmas are proved from textbook compact-Lie-group analysis admissions (Haar orthogonality, compact Laplace concentration, entire partition representation, analytic continuation of finite-support Taylor series) listed there as bounded admissions `(BA-1)–(BA-4)`. This companion is itself `bounded_theorem` and will be audited on its own row; the local algebra of this note is unchanged by registering it.

# DM Leptogenesis PMNS Relative-Action Selector Independence

**Date:** 2026-04-16 (initial); 2026-07-12 exact selector-independence
repair.
**Status:** exact negative boundary; independent audit is required before any
retained-grade effect.
**Claim type:** no_go
**Primary runner:**
[`scripts/frontier_dm_leptogenesis_pmns_relative_action_selector_independence.py`](../scripts/frontier_dm_leptogenesis_pmns_relative_action_selector_independence.py)
**Conditional operational calculator:**
[`scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`](../scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py)

## Claim boundary for independent audit

The exact claim is narrow:

> The current Lattice, Qubit, Admissibility, and Record foundation does not
> entail that the physically selected positive off-seed source is the
> minimizer of the seed-relative action on the favored-column closure set.
> This remains true for an explicit conservative extension in which a static
> seed, a non-singleton finite closure set, and the log-det Legendre packet are
> granted but no selector orientation is supplied.

This is a no-go for the implication **Legendre-dual functional therefore
physical constrained-minimum selector** on the current premise surface. It is
not a no-go against a future dynamics or record-formation theorem that supplies
that implication.

The previous version of this note made precisely that invalid implication. Its
numerical optimization was real, but the word “effective action” was used to
orient a physical selection law that had not been derived.

## Minimal premises and strengthening grants

The load-bearing foundation is the current
[Minimal Framework Axioms](MINIMAL_AXIOMS_2026-06-29.md). It explicitly leaves
log-det readout, source/action identification, weighting, probability,
dynamics, and state-selection outside the four axioms. The registered
[realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md) grants
pointwise evaluation at a supplied realized state and explicitly supplies no
state-selection rule. The approved
[scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) and
[kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
also explicitly supply no selector; the proof grants their complete narrow
content and does not treat either as an import or bounded-status source.

To make the negative result stronger, the proof grants without deriving:

1. a positive seed matrix `H_seed` and positive source matrix `H_e`;
2. the normalized matrix
   `Y = H_seed^(-1/2) H_e H_seed^(-1/2)`;
3. the generator `W(K) = log det(I+K)` and its Legendre dual;
4. an abstract favored column `i_*`, comparator `eta_obs`, two positive source
   points, and a closure readout taking the value `eta_obs` on both points.

These strengthening grants are explicit hypotheses of the finite countermodel
and are instantiated locally rather than imported as authority dependencies.
The proof shows that even this enlarged static packet does not contain the
missing physical selector bridge.

## Exact algebra that does close

For positive `Y`,

`S_rel(Y) = Tr(Y) - log det(Y) - n`

satisfies

`S_rel(Y) = sup_{K>-I} [log det(I+K) - Tr(KY)]`

with unique dual stationary source

`K_* = Y^(-1) - I`.

If `lambda_a` are the eigenvalues of `Y`, then

`S_rel(Y) = sum_a (lambda_a - log(lambda_a) - 1) >= 0`,

with equality only at `Y=I`. Equivalently, the unique unconstrained minimum is
`H_e = H_seed`, and its dual source is `K_*=0`.

This is the exact positive-cone result. It determines the functional and its
source-response relation. It does not state which source is physically
realized.

## Exact selector-independence theorem

Define the explicit finite static countermodel by

- `H_seed = I_3`;
- source domain and closure set `F = {Y_a,Y_b}`;
- `Y_a = diag(2,1,1)` and `Y_b = diag(3,1,1)`; and
- a supplied closure readout with
  `eta_{i_*}(Y_a) = eta_{i_*}(Y_b) = eta_obs`.

The closure set contains exactly the two positive matrices

`Y_a = diag(2,1,1)` and `Y_b = diag(3,1,1)`.

Their relative actions are

`S_rel(Y_a) = 1-log 2 < 2-log 3 = S_rel(Y_b)`.

Consider two completions of the same static packet:

- `L_min` selects the unique `argmin_F S_rel`;
- `L_max` selects the unique `argmax_F S_rel`.

The finite domain makes both extrema existent and unique. Both laws are
deterministic functions of the supplied condition, invariant
under simultaneous basis changes, and give exactly one answer. They agree on
the four axioms, every approved primitive, `H_seed`, `F`, `W`, `S_rel`, the
Legendre identity, the static closure readout, and the closure predicate. They differ
only in the selector orientation. Therefore the shared premise packet cannot
entail `L_min`: if it did, `L_max` could not be a completion of the same
packet.

This is an abstract conservative-extension countermodel. It does not assert
that `Y_a` and `Y_b` are points of the numerical PMNS closure surface. The
conditional PMNS calculator below separately demonstrates off-seed solutions;
none of those calculations is load-bearing for the exact logical result.

The exact runner also closes a stronger naturality objection. On the
two-point feasible set

`Y_c = diag(1/10,1,1)`, `Y_d = diag(2,2,1)`,

relative action uniquely prefers `Y_d`, while the positive, seed-zero,
basis-invariant, direct-sum-additive Frobenius divergence

`D_F(Y) = Tr[(Y-I)^2]`

uniquely prefers `Y_c`. Thus positivity, seed normalization, spectral
naturality, basis invariance, and independent-block additivity do not select
the relative-action objective either.

## Consequence for the reported off-seed PMNS source

The old operational calculator minimizes `S_rel` only after imposing

`eta_{i_*}(H_e)/eta_obs = 1`.

On that imported transport surface, the seed gives

`eta/eta_obs = (0.433077252873, 0.719082664368, 0.719082664368)`,

so favored-column-0 closure excludes the unique source-free action minimum.
The reported off-seed point has

- `S_rel = 0.240906701369`;
- generalized eigenvalues approximately `(0.645736, 0.853724, 1.641616)`; and
- `||K_*||_F approximately 0.695054`, hence a nonzero dual source.

It is therefore an `eta_obs`-conditioned projection on the supplied closure
surface, not the zero-source consequence of the Legendre identity and not a
prediction of `eta_obs`. The calculator remains useful as a conditional
answer to:

> If the relative-action minimization law, the transport packet, and the
> observed closure condition are supplied, which local source does the stated
> optimizer return?

It must not be cited as a derivation of the supplied law or comparator.

The conditional calculator additionally consumes `PLAQ_MC = 0.5934` as a
measured lattice input, `G_WEAK = 0.653` as fitted phenomenology, standard
sphaleron/thermal/entropy factors, the approved scale-reference units
conversion, and the helper transport/projector machinery. These inputs affect
only the conditional numerical replay and are not proof inputs for the no-go.

## Route audit

Five first-principles routes were tested:

1. **Legendre/Fenchel duality:** derives the functional and `K_*`, not a
   realized-source rule.
2. **Convexity and KKT stationarity:** prove a conditional constrained
   minimizer once an objective and constraint are chosen; unconstrained
   convexity selects the non-closing seed.
3. **Bregman or minimum-information projection:** requires a probability,
   covariance, conditioning, or update principle absent from the foundation.
4. **Naturality and invariance:** fail to choose the objective, as the exact
   preference-reversal witness shows.
5. **Least-action or equilibrium language:** requires an oriented dynamics,
   Gibbs/large-deviation measure, or record-formation rule; none follows from
   static Admissibility or Record additivity.

Favored-column extremality selects an index, not a source. Exact equality to
the observed comparator defines a target surface, not a formation law.

## What would falsify this no-go

The no-go is retired by a retained theorem on the current framework surface
that derives the physical selector orientation under the supplied closure
condition—for example, a theorem that supplies both:

1. an identification of the static source functional with the physical
   record-formation or persistence law;
2. an orientation principle such as a derived Gibbs or large-deviation weight
   with fixed sign and a controlled concentration limit.

A non-observational derivation of the closure condition is additionally
required for a full baryon-ratio prediction, but it is not required merely to
falsify this selector-independence no-go.

Merely renaming a Legendre dual “the effective action,” proving local
stationarity, or finding a unique numerical constrained minimum does not
falsify the theorem.

## What this note does not claim

This note does not claim that no future PMNS source selector can be derived. It
does not invalidate the Legendre identity or the conditional optimizer. It
does not prove global properties of the full PMNS closure manifold. It does
not treat `eta_obs`, the fixed seed, transport normalization, or helper
machinery as framework-derived inputs.

## Verification

```bash
python3 scripts/frontier_dm_leptogenesis_pmns_relative_action_selector_independence.py
PYTHONPATH=scripts python3 scripts/frontier_dm_leptogenesis_pmns_observable_relative_action_law.py
```

The first command tests the exact no-go witnesses. The second replays the
conditional numerical calculator and is not a proof of physical selection.
The cached primary-runner transcript is
[`logs/runner-cache/frontier_dm_leptogenesis_pmns_relative_action_selector_independence.txt`](../logs/runner-cache/frontier_dm_leptogenesis_pmns_relative_action_selector_independence.txt).

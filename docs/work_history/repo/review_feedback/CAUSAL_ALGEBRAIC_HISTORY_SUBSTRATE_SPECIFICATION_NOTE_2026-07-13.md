# Causal Algebraic History Substrate: Common Comparison Specification

**Date:** 2026-07-13

**Type:** meta

**Purpose:** common comparison language and executable conformance surface

**Authority:** none. This is a language for comparing candidate laws. It is
not a fifth axiom, a primitive, a physical rule, or an audit authority.

**Runner:**
[`scripts/causal_algebraic_history_substrate_conformance_2026_07_13.py`](../../../../scripts/causal_algebraic_history_substrate_conformance_2026_07_13.py)

## Goal

Use one common language to ask whether a substrate derives the missing
foundation atoms or merely embeds them in its definitions. It directly covers
candidates admitting a state/context/atomic-answer encoding: deterministic,
branching, stochastic, unitary, and algebraic-refinement models. A genuinely
non-Markov whole-history constraint fits only after an explicit history-state
encoding or a separate global-law interface; that translation is substantive,
not neutral syntax.

## Typed Surface

A candidate model supplies some or all of the tuple

```text
(Lambda, A, iota, Sigma, R, Kappa, L, K, mu, h, Q).
```

| symbol | type | comparison meaning |
|---|---|---|
| `Lambda` | graph | physical sites and adjacency; here the target is `Z^3` |
| `A` | finite-region algebra family | candidate joint possibility/operation algebras `A_F` |
| `iota` | local embeddings | maps each one-site `M_2(C)` into `A_F` |
| `Sigma` | state set | complete inputs accepted by the candidate law |
| `R(s)` | record map | site/content pairs readable in state `s` |
| `Kappa` | context/intervention set | actual compatible local question or operation; incompatible contexts are not silently joined |
| `L(s,k)` | atomic law answer | nonempty lawful successors, a kernel, amplitudes, or one successor for state/context `(s,k)` |
| `K(s)` | continuation closure | states physically reachable by repeated lawful atomic answers |
| `mu` | optional statistics | normalized context-conditioned history/test law, if present |
| `h` | optional actuality data | selected/realized history semantics, if present |
| `Q` | optional resource/action data | conserved flow, action, capacity, or response maps, if present |

The syntax deliberately keeps `mu`, `h`, and `Q` optional. A deterministic
model can derive `h`; a uniquely ergodic model can derive frequencies; a
stochastic model can include a normalized kernel. The conformance surface does
not equate these routes.

## Syntax Versus Physics

The following are **syntax only**:

- naming a state set;
- exposing contexts instead of a joint incompatible context;
- representing records as site/content pairs;
- taking transitive closure after an atomic physical relation is supplied;
- defining operational equivalence from complete record statistics.

The following are **physical content unless proved**:

- which joint algebra is physical and whether local copies generate it;
- whether `Sigma` is exhausted by record configurations;
- the extensional table/equation `L` and its lawful context set;
- which local menus have actual successors;
- whether records are invariant under every physical successor;
- whether one history is actual and how;
- any probability/frequency law;
- any time metric, action, resource, source, or continuum response.

Putting one of these in a data type makes a well-typed conditional model. It
does not derive the physical statement.

## Executable Conformance Questions

For each finite witness the runner asks:

1. **total law:** every state/context in the declared domain has a nonempty
   atomic answer;
2. **declared generated-composition metadata:** whether the witness declares
   equal joint dimension and local-product rank. This conformance runner does
   not compute an algebra span; explicit matrix generation is checked in the
   separate category-relative composition theorem runner;
3. **record-state sufficiency:** states with identical record maps have
   identical finite-horizon future record behavior in every context;
4. **record invariance:** every successor preserves all existing site/content
   pairs;
5. **menu support:** every declared available value occurs in a successor in
   that same source context;
6. **actuality:** a unique successor or an explicit sampled-history semantics
   returns one realized successor;
7. **statistics:** every declared branching kernel is normalized, or a stated
   finite frequency theorem is verified;
8. **context discipline:** incompatible tests remain separately indexed.

Finite conformance is a feasibility certificate only. A constitutional
retirement claim additionally needs a full-lattice theorem, controlled limit,
or exact no-go at the required scope.

## Six Reference Families

| family | exact finite witness | what closes internally | what is imported or absent |
|---|---|---|---|
| monotone append closure | one open site branches to immutable `0/1` records | complete local support, record-state sufficiency, permanence | quantum composition, actuality, weights, coherent dynamics |
| reversible QCA/CNOT | two-qubit generated algebra and deterministic reversible copy | generated carrier and deterministic evolution on the enriched quantum state | tensor carrier is supplied; record-only state fails; inverse erases the copy; no frequencies |
| record-generated refinement | dephasing/refinement plus context-sensitive future test | conditional post-record invariance while pre-record phase remains visible | quantum state/carrier and activation map are supplied; no actual branch or weights |
| quantum instrument | projective `Z/X` instrument | branch support, normalized Born kernel, sampled outcome semantics, repeatability | state, effects, tensor carrier, pointer, trace pairing, and stochastic semantics are supplied |
| measured history tree | append-only binary histories with a normalized branch measure | record-state sufficiency, permanence, normalized history statistics | no quantum carrier and no actual-history selector |
| deterministic periodic history | immutable prefixes of a fixed three-symbol cycle | complete record state, permanence, unique history, exact finite visit frequencies | pattern is supplied; no quantum composition or Born-context theorem |

No reference family closes the complete six-atom ledger without importing a
load-bearing item. This is not a universal no-go; it defines the constructive
target for the tournament.

## Target Hybrid

The strongest language-level candidate combines, without yet asserting:

```text
generated quasilocal M2 algebra
+ complete persistent record configuration with physical phase references
+ context-indexed local covariant update
+ dynamically increasing invariant record algebra
+ unique contextual history/frequency theorem.
```

If one exact rule realizes this tuple, Qubit composition, Admissibility
continuation/support, Record permanence, Qualification state sufficiency,
actuality, and Born statistics can all become theorem outputs. The next stage
must construct or sharply obstruct that rule; restating the tuple is not
progress.

## Boundary

This specification makes no axiom recommendation. It prevents a candidate
from receiving credit merely because its family name conventionally includes
tensor products, Born weights, a clock, a state vector, or a stochastic
outcome.

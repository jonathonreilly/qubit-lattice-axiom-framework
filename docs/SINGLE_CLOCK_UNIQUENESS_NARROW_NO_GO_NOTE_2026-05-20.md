# Single-Clock Uniqueness Narrow No-Go: No Spatial RP, No Second Clock

**Date:** 2026-05-20
**Type:** no_go (narrow theorem)
**Status:** source-side proposal — independent audit lane owns the verdict
**Closes (proposed):** the uniqueness gap on
[`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
flagged in the
[`D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`](D3_RETENTION_CLOSURE_PLAN_2026-05-20.md)
review-loop disposition: *"the no-spatial-reflection-positivity /
no-second-clock uniqueness claim is a broad negative claim with
unaudited dependencies and no no-go-discipline checklist."* This
revision puts the claim in proper narrow-no-go format with explicit
N1–N8 discipline.

**Supersedes:** the rejected `SINGLE_CLOCK_UNIQUENESS_NOTE_2026-05-20.md`
(submitted in PR #1603, not landed).

## Narrow claim

On the framework's qubit-lattice substrate
([`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
A1 = qubit at every site = `M_2(ℂ) ≅ Cl(3,0)`; A2 = `Z^3`), with
retained primitives microcausality, Lieb-Robinson finite propagation,
cluster decomposition, and reflection positivity on the temporal
codimension-1 hyperplane, the following augmentations of the
single-clock codimension-1 evolution structure are **blocked**:

- **(R1) Adding a spatial reflection positivity** on a hyperplane
  normal to any spatial direction `ê_i ∈ {ê_1, ê_2, ê_3}`.
- **(R2) Adding a second independent timelike codimension-1
  foliation** with its own RP and unitary evolution.
- **(R3) Adopting an equivariant pair of clock directions** related
  by a discrete `Z_2` symmetry, with separate unitaries.
- **(R4) Adopting a continuous one-parameter family of clock
  directions** with the family acting as a Lie group on the
  substrate.

Each of (R1)–(R4) is blocked by at least one independent wall;
their conjunction is overdetermined. The narrow theorem is that
**no extension of single-clock codimension-1 evolution within
(R1)–(R4) can hold on the retained primitive surface**.

The narrow theorem **does not** claim:
- That single-clock evolution itself is forced (existence of the
  single clock is the load-bearing content of
  `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`;
  this note adds uniqueness against the four attack routes above).
- That any structure outside (R1)–(R4) is blocked. The route
  enumeration is bounded; alternative augmentations are out of
  scope for this narrow no-go.
- That spatial symmetries (translation, rotation, reflection) are
  not allowed — those preserve the time direction and are fully
  compatible with single-clock evolution.

## The four independent walls

**(G1) Microcausality-vs-spatial-RP wall.** The retained
microcausality / Lieb-Robinson primitive
([`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md))
forces `[A(x), A(y)] = 0` for spacelike-separated `x, y`. The
Osterwalder-Schrader inner product `⟨A · (θ A^†)⟩` across a
hyperplane normal to `ê_i` reduces to the standard Hilbert-space
norm when `A(x)` and `A(y)` commute on opposite sides. This
reduction makes spatial-RP a tautological positivity (no non-trivial
Wick-rotation reconstruction along the spatial direction). Spatial
RP carries no Hilbert-space content beyond what's already in the
local algebra.

**(G2) Ultrahyperbolic-Cauchy wall.** Two independent timelike
codimension-1 foliations on a substrate of dimension 4 (3 spatial
+ 2 putative time) give a `(+, +, +, −, −)` signature — the
ultrahyperbolic case. Courant-Hilbert and Tegmark established
that the Cauchy problem is ill-posed for ultrahyperbolic
signatures: small perturbations of initial data do not propagate
continuously. The retained cluster-decomposition primitive
([`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md))
requires a well-posed notion of spacelike infinity; ultrahyperbolic
signatures lack a unique spacelike causal cone, contradicting
cluster decomposition.

**(G3) Distinct-causal-cones-vs-cluster wall.** An equivariant pair
of timelike directions `ê_τ, ê_τ'` related by `Z_2` symmetry induces
two distinct causal cones on the substrate. A point spacelike
under one cone may be timelike under the other. The retained
cluster decomposition requires a single notion of "spacelike
infinity" (used to assert that connected correlations vanish
asymptotically). Two cones violate this uniqueness.

**(G4) Lieb-Robinson-effective-single-clock wall.** For a
continuous one-parameter family of putative clock directions
acting as a Lie group on the substrate, Lieb-Robinson finite
propagation forces every direction in the family to have the
same finite propagation velocity bound. The maximum-velocity
direction defines an effective single clock; the rest of the
family becomes a redundant Lie-group reparameterization, not an
independent dynamical clock. The retained Lieb-Robinson bound
collapses the family to single-clock effective dynamics.

## Wall coverage of attack routes

| Attack route | Walls that block it |
|---|---|
| (R1) Spatial RP on hyperplane ⊥ `ê_i` | (G1) |
| (R2) Second independent timelike foliation | (G2), (G3) |
| (R3) Equivariant `Z_2` clock pair | (G3) |
| (R4) Continuous Lie-group clock family | (G4) |

Each route has at least one independent wall; (R2) is blocked by
two independent walls (overdetermined).

## 7. No-go discipline gate (N1–N8)

**N1 — Alternative route enumeration.** The tested attack routes
are:

1. **(R1)** Add spatial RP across a hyperplane normal to `ê_i ∈ {ê_1, ê_2, ê_3}`. Outcome: blocked by (G1), microcausality reduces the OS inner product to the trivial Hilbert-space norm; no non-trivial spatial Wick-rotation reconstruction.
2. **(R2)** Add a second independent timelike codimension-1 foliation with its own RP and Heisenberg evolution. Outcome: blocked by (G2) ultrahyperbolic Cauchy obstruction and (G3) distinct-causal-cones-vs-cluster conflict.
3. **(R3)** Adopt an equivariant `Z_2`-related pair of clock directions. Outcome: blocked by (G3); two cones violate cluster-decomposition uniqueness.
4. **(R4)** Adopt a continuous one-parameter Lie-group family of clock directions. Outcome: blocked by (G4); Lieb-Robinson velocity bound collapses the family to single-clock effective dynamics.

No other augmentation routes were tested within this narrow no-go.

**N2 — Wall-independence audit.** The four walls are independent:

- (G1) is **operator-algebraic** (OS inner product reduction under microcausality on the local C*-algebra).
- (G2) is **PDE-theoretic** (ultrahyperbolic-Cauchy ill-posedness).
- (G3) is **measure-theoretic / asymptotic** (cluster-decomposition uniqueness of spacelike infinity).
- (G4) is **operator-theoretic** (Lieb-Robinson finite-velocity bound).

Closing any one of (G1)–(G4) — e.g., by abandoning microcausality, or
by abandoning cluster decomposition, or by abandoning Lieb-Robinson —
does not close the others. The walls cover disjoint axiomatic
content.

**N3 — Hidden-wall scan.** The proof promotes all bridge context
to explicit walls: microcausality (G1, G4), cluster decomposition
(G2, G3), Lieb-Robinson (G4), and ultrahyperbolic Cauchy theory
(G2). No "standard QFT", "canonical foliation", or
spacetime-tangent-vector premise is used as hidden closure. The
retained primitives are each cited by name with their canonical
notes.

**N4 — Residual matching.** The prior submitted note
`SINGLE_CLOCK_UNIQUENESS_NOTE_2026-05-20.md` (PR #1603, not landed)
attempted a two-step argument (spatial RP triviality + ultrahyperbolic
obstruction) without enumerating attack routes (R3), (R4) and
without wall-independence audit. This V2 covers the same two
walls as (G1) and (G2)+(G3), and additionally treats (R3), (R4)
via (G3), (G4). The narrow claim is preserved; the discipline is
tightened.

**N5 — Rhetoric audit.** The claim is not:
- "Time is unique in general physics" — only within (R1)–(R4) attack
  routes on the framework's specific retained-primitive surface.
- "Spacetime is forced to be 3+1" — that requires the separate
  conditional `anomaly_forces_time_theorem` to close.
- "Multi-time theories are inconsistent" — only on the framework's
  retained-primitive surface (specifically, given cluster
  decomposition + Lieb-Robinson + microcausality). Theories that
  abandon those primitives are not addressed.
- "Spatial symmetries are forbidden" — translation, rotation, parity
  preserve the time direction and are compatible with single-clock
  evolution; they are not in (R1)–(R4).

**N6 — Partial-closure path scan.** No new axiom is required or
proposed. Possible partial-closure paths are concrete science
artifacts:
- A retained-grade derivation of `Lieb-Robinson` on a broader
  surface (currently retained as
  `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10`).
- A retained-grade derivation of cluster decomposition (currently
  retained as `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`).
- A new derivation that augments (R1)–(R4) by a fifth attack route
  the present note has not enumerated.

None of these are required for the present narrow claim; they would
extend or tighten the claim's scope.

**N7 — Steelman.** The strongest counterargument is that an
**asymmetric** clock pair (not `Z_2`-equivariant) with a tiny
velocity offset between the two clock directions could pass (G3)
by having the "secondary" cone be a small perturbation of the
"primary" cone, with cluster decomposition holding approximately
on the primary cone and the secondary clock acting as a small
perturbation. The response: Lieb-Robinson finite-velocity bounds
are *exact* operator bounds, not approximate; any independent
secondary clock direction with non-zero velocity must itself
satisfy a Lieb-Robinson bound, and the cluster-decomposition
argument applies to the *exact* tail of correlations, not the
leading-order tail. An asymmetric pair therefore still falls under
(G3) on the exact retained-primitive surface. The steelman gives a
*tighter* version of the same wall; it does not block the present
narrow claim.

**N8 — Cross-cycle echo.** Round-1 (PR #1603 V1, not landed)
attempted a Step-1/Step-2 proof with two implicit walls. Round-2
(this V2) attempts the four-wall narrow-no-go format with explicit
N1–N8 discipline. The contributions are additive: V1's two
arguments map to (G1) and (G2)+(G3) here; V2 adds (R3), (R4) attack
routes and the (G4) Lieb-Robinson wall.

## Admitted inputs

1. **Retained microcausality**: `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10` (retained).
2. **Retained Lieb-Robinson finite-propagation bound**: same.
3. **Retained cluster decomposition**: `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29` (retained).
4. **Retained reflection positivity** (temporal, Cases A and B):
   `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29` (retained).
5. **Ultrahyperbolic Cauchy ill-posedness** (Courant-Hilbert,
   Tegmark) — standard PDE-theoretic result; named non-derivation
   import.
6. **Single-clock codimension-1 evolution existence**:
   `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`
   (audited_conditional). The present note adds *uniqueness* against
   (R1)–(R4); the existence side remains conditional on the parent
   row's audit closure.

## Risk classification

This is a `no_go` (narrow theorem) candidate. Within the
enumerated (R1)–(R4) routes and the four-wall structure (G1)–(G4),
the negative conclusion follows from standard operator-algebraic
+ PDE-theoretic content. The narrow contribution is the explicit
N1–N8 discipline applied to the single-clock uniqueness question
on the framework's retained-primitive surface.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links so the citation graph records them as deps):

- [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) — supplies the qubit-form A1+A2 on which the no-go applies
- [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) — supplies the existence of the single-clock structure that this note adds uniqueness against
- [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md) — supplies microcausality and Lieb-Robinson (walls G1, G4)
- [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md) — supplies cluster decomposition (walls G2, G3)
- [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md) — supplies the temporal RP that defines the foliation single-clock evolution lives on
- [`D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`](D3_RETENTION_CLOSURE_PLAN_2026-05-20.md) — tracking note identifying this as the named uniqueness gap to close

**Upstream standard-math imports** (named non-derivation; not framework rows):

- Courant-Hilbert *Methods of Mathematical Physics* Vol II — ultrahyperbolic Cauchy ill-posedness
- Tegmark `gr-qc/9702052` — multi-time dimensionality / Cauchy-problem reference for the framework's substrate context

**Plain-text pointer references** (NOT load-bearing deps):

- `SINGLE_CLOCK_UNIQUENESS_NOTE_2026-05-20.md` (V1, rejected) — superseded by this V2 with the N1–N8 discipline
- `ANOMALY_FORCES_TIME_THEOREM.md` — adjacent lane on dimensionality forcing; not load-bearing for this uniqueness claim

## What this file is not

- Not a derivation of single-clock *existence* (that's the parent `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`).
- Not a closure of the broader D=3+1 chain (anomaly-forces-time + Lorentz repairs remain gate-dependent).
- Not a claim that multi-time physics is generally impossible — only that the four enumerated routes are blocked on the framework's retained-primitive surface.
- Not a numerical-prediction change.
- Not a unilateral retagging. The narrow-no-go candidacy depends on independent audit acceptance of the four-wall structure and the (R1)–(R4) route enumeration.

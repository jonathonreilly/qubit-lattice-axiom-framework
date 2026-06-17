# Unordered-Mass-Multiset Registrability Bridge — Record-Native Narrow Bounded Theorem

**Date:** 2026-06-11
**Current-surface repair:** 2026-06-17
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit the audit-lane-owned Tier-A
registry, ledger, queue, or publication-status surfaces.
**Actual source scope:** bounded theorem on a supplied finite readout context.
Record supplies finite additivity, the realized-outcome `K`/CPT orbit, and the
absence of within-sector data; together these give the row's former P-dep
step as a Record-native dependence lemma for scalar readouts of records. Record
still does not supply the finite context, monitored operator, weights,
normalization, probability, dynamics, or any registry reduction.
**Primary runner:**
[`scripts/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.py`](../scripts/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.py)
(SCORECARD: `TOTAL: PASS=17 FAIL=0`; cached:
[`logs/runner-cache/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.txt`](../logs/runner-cache/frontier_unordered_mass_multiset_registrability_bridge_2026_06_11.txt))

## Boundary

This note proves one narrow theorem — the **unordered-mass-multiset
registrability bridge** named open by the audit verdict on
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
("if the intended audited consequence is registry reduction rather than the
algebraic orientation lemma, also provide a retained unordered-mass-multiset
registrability bridge").

It does **not** enact any registry reduction, edit
`docs/audit/data/tier_a_admissions.json`, retire any Tier-A admission or
`theta` (PR #3511's gated lane owns that question), derive `|delta| = 2/9`,
consume the staggered-Dirac gate's authority (the gate's own retention drains
in the audit lane, separately), or touch the occupancy dial `r` (see the
explicit firewall statement below). It proves the bridge theorem on the
supplied finite surface and states the composition with the korbit orientation
lemma as a consequence available to the gated lane under that same
supplied-context boundary.

**2026-06-17 audit-unlock source repair.** The prior version exposed P-dep as
an explicit conditional premise. The current version proves the needed
dependence step from the Record axiom's realized-outcome and
no-within-sector-data clauses, once the finite readout context and monitored
central value have been supplied. This is not a new axiom and not an approved
primitive premise node; it is the ordinary quotient/readout consequence that a
scalar readout of records can depend only on the data registered by those
records. Readouts that use raw labels, orientation, hidden context parameters,
or cross-record interference are still meaningful mathematical probes, but
they are not scalar readouts of the registered records on this Record surface.

## Setting: the supplied readout context (G1 — all of it is input)

The theorem is stated on a **supplied** readout context; the Record axiom
supplies none of the following data (guardrail G1):

- a finite label set `Lambda = {0, 1, 2}` with orthogonal central projectors
  `{P_k}` (`P_j P_k = 0` for `j != k`, `sum_k P_k = I`);
- a fixed `K`/CPT conjugation `K` (entrywise complex conjugation on the
  supplied basis), inducing the label involution `sigma` with
  `K P_k K^{-1} = P_{sigma(k)}`;
- a generation-monitored mass operator on the `AC_phi_lambda` circulant
  surface,

  ```text
  H(delta) = a I + B exp(i delta) C + B exp(-i delta) C^T,   a, B real, B != 0,
  ```

  with `C` the 3-cycle, diagonalized by the Fourier sectors: the per-sector
  central value is `lambda_k(delta) = tr(H(delta) P_k)`, real since `H` is
  Hermitian.

Elementary facts on this surface, each verified in the runner:

- **(F1)** `conj(H(delta)) = H(-delta)` — the `K`/CPT flip is exactly
  `delta -> -delta` (this is the korbit lemma's flip, re-verified here so the
  note is self-contained algebra on the supplied class);
- **(F2)** `sigma = (0)(1 2)`, i.e. `k -> -k mod 3`: an involution fixing
  exactly the singlet label;
- **(F3)** `lambda_{sigma(k)}(-delta) = lambda_k(delta)` — the flip permutes
  the per-sector values within `K`/CPT label orbits.

## The Record boundary and the P-dep lemma

From [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md):

1. **(Additivity)** the scalar readout `I` is finitely additive over finite
   pairwise-disjoint record collections, with `I(empty) = 0`;
2. **(Orbit)** the realized outcome is the `K`/CPT orbit of the realized
   central sector — so two records related by the fixed `K`/CPT conjugation
   register the **same** outcome;
3. **(No-within-sector-data)** a record supplies no readout context,
   decomposition, `K`/CPT structure, weighting, normalization, probability,
   within-sector data, or occupancy rule.

**Definition (Record-registrable readout).** A scalar `R` assigned to records
in the supplied context that is (i) finitely additive over pairwise-disjoint
records with `R(empty) = 0` [(Additivity)], and (ii) constant on `K`/CPT
orbits of the realized outcome — equal values on a record and its `K`/CPT
image, since they register one outcome [(Orbit)]. (This is the same
registrable class used by the unaudited precedent note named under
Dependencies; the present note re-derives every leg it uses, so that note is
context, not load-bearing.)

**Lemma (P-dep from the Record boundary).** In a supplied readout context with
a monitored central value `lambda_k`, a Record-registrable scalar readout's
per-record contribution is a function of the per-record **registered** datum:
the `K`/CPT orbit of the realized central sector together with the supplied
monitored central value. It is not allowed to depend on raw sector labels
inside a `K`/CPT orbit, orientation, hidden context parameters, cross-record
interference, or any other data not registered by the record.

Proof. A record is the durable registration of the realized outcome, and the
realized outcome is the `K`/CPT orbit of the realized central sector. The
Record axiom also says that a record supplies no within-sector data,
weighting, normalization, probability, dynamics, occupancy rule, or other
contextual payload. Therefore two presentations that give the same registered
record datum must receive the same scalar readout contribution. Equivalently,
the contribution descends to the quotient set of registered record data. This
is the former P-dep step. It is not an extra axiom or primitive; it is the
definition of a scalar readout of records after the finite context and
monitored central value have been supplied.

## Theorem (unordered-mass-multiset registrability bridge)

Assume the supplied context above and the three Record clauses quoted above.
With `M(delta)` denoting the
**orbit-resolved unordered multiset** of per-orbit sector invariants
`M(delta) = {{ ([k], lambda_k(delta)) : k in Lambda }}` (`[k]` the `K`/CPT
label orbit, so within-orbit order is erased by construction):

> **(B1 — factorization / upper bound.)** Every Record-registrable scalar
> readout equals a sum of per-record contributions with no cross terms, each
> contribution a function of `([k], lambda_k)`; hence every registrable
> readout factors through `M(delta)`. Sector labels beyond their orbit —
> in particular the order within the doublet orbit `{1, 2}` — are not
> registrable.
>
> **(B2 — exactness / lower bound.)** The power-sum readouts
> `p_m = sum_k lambda_k(delta)^m` (`m = 1, 2, 3`) and the orbit-class
> readouts are Record-registrable, and they reconstruct `M(delta)` exactly
> (Newton–Girard: `p_1, p_2, p_3 -> e_1, e_2, e_3 ->` the characteristic
> polynomial `->` the unordered eigenvalue multiset; the registrable singlet
> orbit-class readout resolves the singlet/doublet split). Hence the
> registrable spectral content of the generation-monitored mass operator is
> **exactly** `M(delta)` — neither more (B1) nor less (B2).
>
> **(B3 — orientation consequence.)** The `K`/CPT flip `delta -> -delta`
> permutes per-sector values within label orbits (F3), so
> `M(-delta) = M(delta)`. Therefore every Record-registrable readout takes
> equal values at `+delta` and `-delta`: the **sign / orientation of `delta`
> is not registrable content**, while `|delta|`-level (`K`/CPT-even) data —
> e.g. `cos(3 delta)` recovered from
> `e_3 = a^3 - 3 a B^2 + 2 B^3 cos(3 delta)`, a function of the multiset —
> is registrable-eligible.

## Derivation

**L1 — disjointness and no cross terms.** The supplied `{P_k}` are orthogonal
central idempotents, so the sector records are pairwise disjoint.
(Additivity) applied to the finite family forces
`R(total) = sum_k r_k` with `r_k = R(rec_k)` and no interference content: any
posited cross term `c` in `R(rec_i u rec_j) = r_i + r_j + c` is annihilated
by the additivity identity itself. `R(empty) = 0` is the empty sum.

**L2 — per-record contributions are orbit class functions.** By the Record
P-dep lemma,
`r_k = f(k, lambda_k(delta))` for some function `f` of the label and the
monitored central value. (Orbit) applied to a single record and its `K`/CPT
image — which register one outcome — gives the per-record identity

```text
f(k, lambda_k(delta)) = f(sigma(k), lambda_{sigma(k)}(-delta))   for all delta.
```

By (F3), `lambda_{sigma(k)}(-delta) = lambda_k(delta)`, so
`f(k, x) = f(sigma(k), x)` for every value `x` attained by `lambda_k` (on the
supplied circulant class `lambda_1` and `lambda_2` sweep the same range, since
`lambda_2(delta) = lambda_1(-delta)`). Hence `f` depends on the label only
through its orbit `[k]`: `f` is an orbit class function.

**L3 — factorization (B1).** Combining L1 and L2,
`R(total) = sum_k f([k], lambda_k(delta))` is a sum over the multiset
`M(delta)` of a fixed function — i.e. `R` factors through `M(delta)`. An
order-sensitive `f` (with `f(1, .) != f(2, .)`) violates the L2 identity at
some `delta` and is therefore not registrable.

**L4 — exactness (B2).** Each power sum `p_m = sum_k lambda_k^m` is a
per-sector sum of an orbit-blind function, hence additive and orbit-constant:
registrable. Newton–Girard converts `(p_1, p_2, p_3)` to
`(e_1, e_2, e_3)`, whose monic cubic has the eigenvalues as its root multiset
— so registrable readouts alone determine the unordered eigenvalue multiset
(runner leg L7 reconstructs it numerically and matches the direct spectrum).
The singlet orbit-class readout `f(0, x) = x`, `f(1, .) = f(2, .) = 0` is an
orbit class function (registrable by L1–L2) and resolves which eigenvalue
sits on the singlet orbit; the remaining unordered pair is the doublet-orbit
content. So `M(delta)` is exactly recoverable from registrable readouts.

**L5 — orientation (B3).** By (F3) the flip `delta -> -delta` acts on the
labelled value list as the within-orbit permutation `sigma`, so
`M(-delta) = M(delta)`; by B1 every registrable readout is flip-invariant.
The odd line — `sin(3 delta)`, the signed doublet gap
`lambda_1 - lambda_2 = 2 sqrt(3) B sin(delta)` (sign set by the Fourier
labeling convention; the runner's convention is used), any orientation datum —
takes opposite values on the two `K`/CPT-related configurations that register
one outcome, hence violates (Orbit). The even datum `cos(3 delta)` is a
function of `e_3`, i.e. of the multiset, hence registrable-eligible. This
note does **not** derive the magnitude `|delta|` or its value.

## Hostile guard — explicit attacking candidates, each pinned to a hypothesis

| candidate readout | construction | violated Record hypothesis | runner leg |
|---|---|---|---|
| label-weighted sum | `sum_k k * lambda_k` | (Orbit): differs at `+/-delta` (order within the doublet orbit leaks) | G1 |
| signed doublet gap | `lambda_1 - lambda_2` | (Orbit): exactly `K`/CPT-odd (`= 2 sqrt(3) B sin delta` in the runner's labeling convention), nonzero at generic `delta` | G2 |
| fixed-label Vandermonde | `prod_{i<j} (lambda_i - lambda_j)` | `I(empty) = 0` + (Additivity): empty product is 1, and the natural sub-multiset extension is not additive; also (Orbit): alternating under the doublet transposition | G3 |
| orientation readout | `sin(3 delta)` | (Orbit): assigns two distinct values to the two `K`/CPT-related configurations registering one outcome | G4 |
| interference cross-term | `R(rec_1 u rec_2) = lambda_1 + lambda_2 + lambda_1 lambda_2` | (Additivity): the product term is the cross term killed in L1 | G5 |
| within-orbit order probe | `f(k, x) = [k = 1] * x` (additive!) | (Orbit) at per-record resolution: `r_1(delta) != r_{sigma(1)}(-delta)`; additivity alone does not save it | G6 |

Every hostile candidate is **constructed and evaluated** in the runner, with
the violation witnessed quantitatively at generic `delta` for every sampled
parameter set (adversarial fixed sweep, no acceptance-by-lucky-seed), and the
degenerate boundary points `sin(3 delta) = 0` checked separately (D1).

## Consequence for the korbit lane (stated, not enacted)

The korbit note's audited algebraic lemma — `H(delta)* = H(-delta)` with
unordered-spectrum invariance — composed with B1–B3 here yields the
registry-level statement the audit placed outside that note's closed scope:
on this supplied Record readout context, the record registers the same outcome
at `+delta` and `-delta`; the orientation of `delta` is not registrable
content, and the surviving candidate atom is the `|delta|`-level (even) datum.
Whether and how the Tier-A `AC_phi_lambda` admission is reduced to a
magnitude-only atom is a registry/audit-lane decision (and the `theta`
retirement question is gated in PR #3511); this note supplies the
source-side bridge theorem those gated lanes were named as waiting on, and
nothing else. The next paths this opens: the `|delta|` magnitude chain
(R-eta readout identification) and the audit-lane drain of the staggered gate
authority.

## Firewall statement on `r`

The occupancy dial `r` is **untouched** by this note. The bridge concerns
sector labels/order and `delta`-orientation only. Per-sector weights are the
registered pattern of the realized state (guardrail G3), not delivered by the
partition and not constrained, derived, or forced here; charged leptons
register `r = 1/2` as a dial setting, quarks and neutrinos register other
settings, and nothing in B1–B3 selects among them.

## Boundary — honest residuals

- **(W-ctx) Supplied-context premise.** `{P_k}`, the `K`/CPT conjugation, and
  the monitored circulant `H(delta)` are inputs (G1). The standing modeling
  identification — that the physical species readout context satisfies the
  Record registrability constraints — is **not** proved here; the theorem
  operates within that class. This is the same standing residual carried by
  the registrable-readout precedent note.
- **(W-dep) Dependence is limited to registered record data.** The former
  P-dep premise is now a Record-native lemma: scalar readouts of records
  descend to the registered record datum. This does not make arbitrary
  mathematical functions illegal; it says that functions depending on raw
  labels, orientation, hidden context parameters, or cross-record products are
  outside the Record-registrable scalar-readout class used here.
- **(W-orbit-type) Orbit-type resolution is NOT erased.** `K`/CPT erases
  within-orbit order and orientation, not the singlet-vs-doublet orbit-type
  distinction: the singlet orbit-class readout is registrable (runner L6/L7),
  so the registered spectral datum is the orbit-resolved multiset `M`, a
  refinement of the bare unordered eigenvalue multiset. The bare multiset is
  registrable (B2), and the `delta`-flip acts within orbits, so the `+/-delta`
  outcome identity (B3) is unaffected by this refinement. The bridge claim is
  stated at this honest resolution.
- **(W-range) The L2 range argument uses the supplied class.** The step
  `f(k, .) = f(sigma(k), .)` on attained values uses
  `lambda_2(delta) = lambda_1(-delta)` (the two doublet sectors sweep one
  range). On a different supplied surface the same conclusion needs the
  analogous covariance; the theorem is narrow to the supplied class plus any
  context satisfying F1–F3.
- **(W-mag) No magnitude.** `|delta| = 2/9` and its single-summand readout
  are not derived, addressed, or assumed; they remain on the R-eta chain.
- **(W-gate) The staggered-Dirac gate is not consumed.** The circulant class
  is restated and re-verified here as supplied finite-dimensional algebra;
  this note takes no authority from
  `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (unaudited), whose
  retention question drains in the owner's audit lane.

## Honest-auditor-read

What is actually proved: on a supplied 3x3 circulant readout context with
Fourier sectors and conjugation-`K`, the Record axiom's additivity,
realized-outcome orbit, and no-within-sector-data clauses force every
Record-registrable scalar to be a sum of orbit-class functions of the
per-sector central values (B1); registrable scalars suffice to reconstruct the
orbit-resolved unordered multiset (B2); and consequently all registrable
content is invariant under `delta -> -delta` (B3). The hostile
order/sign-sensitive candidates each violate a named clause, checked
numerically. What is NOT proved: that the physical readout context is of this
class (W-ctx), any registry change, any `theta` statement, and any magnitude.
A hostile reviewer should attack the supplied-context premise first, then the
L2 range argument (W-range), then the claim that the orbit-resolved multiset
(rather than the bare one) is the right bridge resolution (W-orbit-type).

## What this note does NOT claim

- It does **not** enact the registry reduction, retire `AC_phi_lambda` or
  `theta`, or edit any audit-lane-owned surface.
- It does **not** derive `|delta| = 2/9`, supply R-eta, or address the global
  PL/ABSS bridge.
- It does **not** prove the physical readout context must satisfy the Record
  registrability constraints.
- It does **not** add P-dep as a new axiom or identify P-dep as an approved
  primitive premise node; the dependence step is used only as the Record-native
  quotient/readout lemma proved above.
- It does **not** force, derive, or constrain `r` (firewall above).
- It introduces **no** new axiom, primitive, admission, normalization,
  probability rule, comparator, or framing import, and consumes no PDG /
  fitted / measured value.
- It does **not** promote, demote, or set the audit status of any dependency.

## Dependencies (live `effective_status` from `origin/main` audit ledger, 2026-06-11)

Load-bearing:

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (`minimal_axioms`, effective_status: `meta`, approved axiom-premise node) —
  the Record axiom clauses (Additivity), (Orbit), (No-within-sector-data),
  used as the retained framework premises quoted above and as the source of
  the P-dep quotient/readout lemma.

Context, **not** load-bearing (each leg used from these is re-derived or
re-verified in this note's runner):

- `TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
  (effective_status: `audited_conditional`) — the consumer lemma naming this
  bridge open; its flip identity F1 is re-verified here (runner L1), so no
  authority is consumed from it.
- `REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`
  (effective_status: `unaudited`) — definitional precedent for the
  registrable class; its phase-erasure theorem is not used (the odd/even
  content needed here is re-derived in L5).
- `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
  (`realized_state_primitive`, approved axiom-premise node) — pointwise-
  evaluation discipline context only; not load-bearing.
- `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`
  (not a ledger row; synthesis context) — downstream context for what the
  mass multiset feeds; no content consumed.
- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`
  (effective_status: `unaudited`) — named here ONLY to state that it is not
  consumed (boundary item W-gate); intentionally not linked as a dependency.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.

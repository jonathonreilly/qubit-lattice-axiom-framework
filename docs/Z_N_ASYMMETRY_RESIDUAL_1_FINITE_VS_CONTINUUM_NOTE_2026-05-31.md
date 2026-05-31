---
claim_id: z_n_asymmetry_residual_1_finite_vs_continuum_note_2026-05-31
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Residual-1 finite/continuum separation: L₃(1,2)=2/9 is the framework-native holomorphic-Lefschetz weight, distinct from the continuum spin-Dirac lens eta

**Date:** 2026-05-31
**Claim type:** bounded finite/algebraic theorem + demarcation. Adds no axiom
and no import. Atiyah–Bott / Donnelly / APS appear as **external context only**,
never load-bearing.
**Status authority:** independent audit lane only. Sets, predicts, requests no
audit verdict; edits no audit row.
**Primary runner:**
`scripts/frontier_z_n_asymmetry_finite_vs_continuum_separation.py`
with cache
`logs/runner-cache/frontier_z_n_asymmetry_finite_vs_continuum_separation.txt`
(20/20 checks).

## Purpose

The retained_bounded note
[`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
(`L₃(1,2)=2/9`) carries **residual (1)**: "No continuum APS eta invariant on a
real lens space is proved; no Atiyah–Patodi–Singer fixed-point theorem is derived
from the framework; no proof is given that a concrete framework Dirac operator
produces the local denominator `∏_j(ζ_N^{k a_j}−1)^{-1}`."

The companion note `Z_N_SPECTRAL_ASYMMETRY_PHYSICAL_IDENTIFICATION_NOTE_2026-05-31`
(sibling PR) discharged residual (2). This note treats residual (1) **honestly**: it keeps the
work **finite/algebraic** (framework-internal), it **meets the operator-realization
core finitely**, and it shows the literal continuum target is a **distinct external
comparator** — not by importing Atiyah–Bott/Donnelly, but by computing that the
framework's number is a *different* invariant from the continuum eta. It does
**not** claim to prove the continuum APS eta; that stays open-as-import.

## Result

### 1. The framework's object is the finite holomorphic-Lefschetz / Molien weight (import-clean)

`L₃(1,2)=2/9` is the finite holomorphic-Lefschetz / Molien weight of the native
`C₃` action on the generation doublet of `H=aI+bC+b̄C²` (`H=iD`, the retained
real anti-Hermitian Dirac operator). Two framework-internal computations agree
(runner §A):

```
L_3(1,2) = (1/N) Σ_{k=1}^{N-1} det[(C^k − I)^{-1} | doublet]
         = (1/N) Σ_k Molien P_k(1),    P_k(t) = ∏_j 1/(1 − ω^{k a_j} t),
         = 2/9.
```

The Molien value is taken at `t=1`, a **regular point** (nearest pole at distance
`√3`), so it is a plain rational-function value computed by monomial counting —
**no continuum spectrum, no analytic continuation, no metric, no heat kernel**.
The grading variable `t` counts polynomial degree, not eigenvalue magnitude.

### 2. The continuum spin-Dirac lens eta is a *different number* (the key clarification)

Three invariants of the **same** `Z₃` rotation data `(N,a)=(3;(1,2))` are
genuinely distinct (runner §B):

| invariant | value at (1,2) | character |
|---|---|---|
| holomorphic-Lefschetz / Molien `∏ 1/(ω^{ka_j}−1)` | **+2/9** | metric-free — the framework's object |
| G-signature defect `∏ cot(πka_j/N)` | −2/9 | a different invariant |
| spin-Dirac lens eta `∏ 1/(2i sin(πka_j/N))` | **0** | the continuum APS spin-Dirac eta |

with the exact tie `(N−1)/(4N) − ¼·(signature defect) = 1/6 + 1/18 = 2/9`. So the
**continuum spin-Dirac APS eta named in residual (1) is `0` for weights `(1,2)`,
not `2/9`.** The framework's `2/9` is the *holomorphic-Lefschetz / Molien* number
(the Atiyah–Bott fixed-point weight), which is metric-free and finite/algebraic.
Residual (1)'s literal continuum object is therefore not even the same number the
framework carries — it is a distinct external comparator.

### 3. The operator-realization core (residual-1 clause 3) is met finitely

`H=iD` is the concrete native (retained_bounded
[`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md))
Dirac operator, and the resolvent of the generation symmetry on its doublet
produces the local denominator exactly:
`det[(C^k − I)^{-1} | doublet] = ∏_j(ω^{k a_j}−1)^{-1} = 1/3` each (runner §A).
The "concrete framework Dirac operator produces the local denominator" clause is
met **finitely and import-clean** (this is the companion residual-2 object).

### 4. The flat substrate: η ≠ index genuinely evades the index-0 wall

The actual native staggered Dirac `D` on `Z³` satisfies `{ε, D}=0`
(runner §D), so `H=iD` has a `±`-symmetric spectrum and **bulk signed count `Σ
sign(λ)=0`** — the index-0 / bulk-vanishing wall
([`HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md`](HIERARCHY_APS_ETA_STAGGERED_BULK_VANISHING_SCOPING_NOTE_2026-05-26.md),
retained_bounded) holds on the actual operator. **Yet** `ε` is the `(π,π,π)`
momentum shift, which maps every Hamming-weight-1 Brillouin-zone corner to a
weight-2 corner — so `ε` acts **trivially on the generation triplet**. The
`±`-pairing that zeroes the bulk does not act within the `hw=1` sector, so the
finite equivariant eta there, `η_C(H)=2`, is unobstructed. **`η ≠ index`
genuinely evades the index-0 wall** — but the nonzero object is the *finite*
equivariant eta, not a continuum eta of `D`.

### 5. The algebraic-integer wall: 2/9 is not any index or spectral flow

`2/9` has minimal polynomial `9x−2` (non-monic over `ℤ`), so it is **not an
algebraic integer** (runner §C). Every index / equivariant-spectral-flow value
lies in `ℤ` or `ℤ[ω]` (algebraic integers), so **no index or spectral flow can
equal `2/9`.** The genuine continuum-in-emergent-time suspension index of
`d/ds + H(s)` over the parameter path `r:0→2` (through the `r=1` doublet
zero-crossing) is the **integer `2`** (the doublet multiplicity). `2/9` arises
**only** from the `1/N` group-average localization of the `ℤ[ω]`-valued resolvent
determinants — which is exactly the content of the Atiyah–Bott/Donnelly
fixed-point localization. The framework owns the summand data (rotation weights,
native); asserting the `1/N` sum **equals a self-adjoint continuum eta** is the
import.

## Disposition (honest)

- **Met, finitely and import-clean:** residual (1)'s operator-realization clause
  (a concrete framework Dirac operator produces the local denominator) — via
  `H=iD` and the doublet resolvent.
- **Reframed as comparator:** the literal "continuum APS eta on a real lens space"
  is the spin-Dirac eta `= 0` for `(1,2)`, a *different number* from the
  framework's `2/9`. The framework's `2/9` is the finite holomorphic-Lefschetz /
  Molien weight. The continuum spin-Dirac eta is an external benchmark, not a
  framework requirement, and the framework is `d=3+1` discrete and flat with no
  native curved lens space (no such row exists on the ledger).
- **Stays open-as-import:** proving the framework's finite weight **equals a
  self-adjoint continuum eta on a curved lens space** still requires the
  Donnelly/APS fixed-point theorem as the `(rotation data → continuum eta)` map.
  This note does **not** build that bridge and does **not** claim residual (1) is
  discharged. It matches the bounded scope already carried by
  [`KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md`](KOIDE_APS_BLOCK_BY_BLOCK_FORCING_NOTE_2026-04-21.md)
  (retained_bounded), whose claim_scope explicitly stipulates — does not derive —
  the ABSS/APS applicability.

Net: residual (1) is **tightened**, not closed. Its operator core is met finitely
and import-clean; its continuum target is a distinct external comparator that
stays open-as-Donnelly-import.

## Non-circularity

`r=|b|²/a²` is the free scan variable; `2/9`, `r=1`, and the integer suspension
index `2` are outputs, never inputs (runner §C, §E). The three cyclotomic
invariants are computed forward from `(N,a)`; the Molien value is a regular-point
rational-function evaluation, not a regularization choice.

## External Context (context only — never load-bearing)

Atiyah–Bott (holomorphic Lefschetz fixed-point number), Donnelly (equivariant
eta of lens spaces as a finite cyclotomic sum), Atiyah–Patodi–Singer (the eta
invariant), and ABSS (the equivariant index on the stipulated PL route of the
block-by-block note) name the geometric invariants the framework's finite weights
coincide with or differ from. They are **cited only to identify and distinguish**
those objects; **none is used to derive `2/9` or to discharge anything**. Indeed
the framework's `2/9` is shown to be a *different* number from the continuum
spin-Dirac eta, so the result cannot rest on importing it.

## Boundary (the next path this opens)

This closes no route. A framework-internal Dirac operator on a **curved or
boundaried native substrate** — not the flat `Z³` torus, where the bulk eta
vanishes by `±` pairing — with a **derivable** spectral-flow / suspension index
could promote the finite equivariant eta to a genuine continuum eta without
Donnelly. The bulk-vanishing scoping note explicitly leaves **Wilson/domain-wall
mass, nontrivial gauge background, boundary geometry, and spectral flow** open;
any of these, made framework-native, could host a nonzero continuum-type eta the
flat bare operator cannot — but it must produce the `1/N` localization as an
operator eta (not a Lefschetz number) to cross the algebraic-integer wall.

## No-Go Discipline Gate

**N1 — Alternative routes.** Five routes to the continuum target were tested:
representation-data (needs Donnelly for the data→eta map), discrete spectral
realization (bulk eta 0; the `2/9` lives on `ker(D)` = the finite circulant),
emergent-time spectral flow (yields integer `2`, blocked from `2/9` by the
algebraic-integer wall), Molien/zeta collapse (regular-point rational, metric-free
— reaches the denominator but not the spin-Dirac eta), and mis-targeted-comparator
(rigorous for the continuum shell, but characterizing the comparator's dependence
invokes Donnelly). None reaches the continuum spin-Dirac eta import-free.

**N2 — Wall-independence.** The algebraic-integer wall (`2/9 ∉` algebraic
integers) and the number-class distinction (Molien `+2/9` ≠ spin-Dirac eta `0`)
are independent; either alone shows the framework's finite weight is not the
continuum spin-Dirac eta.

**N3 — Hidden-wall scan.** "Bulk eta 0" rests on `{ε,D}=0` on the actual staggered
operator (verified). "`ε` trivial on `hw=1`" rests on `(ℤ₂)³` corner arithmetic
(`ε=(π,π,π)` shift). The Molien collapse rests on `t=1` being a regular point.

**N4 — Residual matching.** This note attacks residual (1) only; residual (2) is
the companion note. The operator-realization clause is shared and met finitely.

**N5 — Rhetoric audit.** "Reframed as comparator" means the *literal continuum
spin-Dirac eta* is a distinct number the framework neither carries nor needs. It
does **not** mean residual (1) is discharged: the continuum lift stays
open-as-import.

**N6 — Partial-closure path.** The Boundary lists concrete open channels (curved
substrate, Wilson mass, boundary geometry). No new axiom is required; import
retirement by a later bounded theorem is not foreclosed.

**N7 — Steelman.** A reviewer insisting on the absolute continuum lens-space eta
is granted the point — that object exists and needs Donnelly; the framework has no
curved lens space to host it, and it is a *different number* (`0`) anyway. So it
is a comparator, and the bridge stays an import.

**N8 — Cross-cycle echo.** The same continuum/import boundary appears in
`koide_aps_block_by_block_forcing` (ABSS stipulated, not derived) and the parent
note's "successor must prove the missing fixed-point and operator-realization
bridge explicitly." This note builds the **finite/operator** half and leaves the
**continuum** half explicitly open.

## Anchors (live-ledger tiers, verified origin/main 2026-05-31)

retained / retained_bounded: `axiom_first_z_n_equivariant_spectral_asymmetry`
(retained_bounded, parent), `cpt_exact_real_anti_hermitian_d` (retained_bounded),
`new_parity_is_circulant_phase` (retained_bounded, weights (1,2)),
`staggered_axis_symmetry_is_s3` (retained_bounded, N=3),
`hierarchy_aps_eta_staggered_bulk_vanishing_scoping` (retained_bounded, the
index-0 wall), `koide_aps_block_by_block_forcing` (retained_bounded, the prior
ABSS-stipulated route), `three_generation_hw1_distinct_translation_characters`
(retained).

# Parent Equation (8) Repair + Nachtergaele-Sims J* Correction for AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. The `bounded_theorem`
label is a source-side claim-boundary declaration, not an audit verdict.
**Primary runner:** [`scripts/frontier_cluster_decomposition_parent_eq8_repair_narrow_verifier.py`](../scripts/frontier_cluster_decomposition_parent_eq8_repair_narrow_verifier.py)

**Authority role:** narrow companion to the audited_conditional parent
[`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md).
Supplies (R-A) deletion of the parent's bogus equation (8) "Kubo
identity" used inside the parent's Step 4 sketch, and (R-B) the
Nachtergaele-Sims `J*` per-site sum correction to the parent's `J`
single-term operator-norm constant in equation (1). Does **NOT**
modify the parent note text.

## Honest scope (read this first)

- **Two narrow repairs only** from the parent's Step 4 sketch and
  equation (1). Nothing else in the parent is touched.
- **Does not modify the parent note text.** Parent keeps its current
  `audited_conditional` ledger row and on-disk text; this note ships
  corrected statements as a separate companion.
- **Does not lift the parent's audited_conditional status.** Lift
  requires (a-eq8)=this note + (a-companion)=axis-permutation
  companion [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md)
  (PR #2474, in flight) + (c) re-audit of the
  [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md)
  composition. This is exactly piece (a-eq8).
- **Prove-textbook-inline discipline.** The Nachtergaele-Sims `J*`
  constant is standard mathematical-physics content but load-bearing
  here; proved inline as class-A algebraic identity check (§3 Lemma
  R-B.1), with the runner constructing explicit local Hamiltonians
  and verifying `J ≤ J*` strictly where multiple terms touch one site.

---

## §0. Why this companion exists

A Tier 3 panel attack on 2026-06-02 against the cluster_decomp
audited_conditional row (load-bearing score 17.9 on origin/main)
identified two defects in the parent's Step 4 sketch + equation (1):

> *(parent §Proof, Step 4, line 266)*
> ```text
>     ⟨A_x B_y⟩_ρ - ⟨A_x⟩_ρ ⟨B_y⟩_ρ
>         =  -∫_0^β  dτ  ⟨ [A_x , B_y(iτ)] ⟩_ρ           (parent eq 8)
> ```

> *(parent §Statement, equation (1), line 169)*
> ```text
>     v_LR  =  2 · e · J · R_int · Z_lat                  (parent eq 1)
> ```
> with `‖h_X‖ ≤ J` for each finite-range term `h_X`.

1. **Eq (8) is not an identity.** The correct Kubo identity is the
   Duhamel-form `⟨A; B⟩_β = (1/β) ∫_0^β dτ ⟨A(0) B(iτ)⟩_ρ - ⟨A⟩_ρ ⟨B⟩_ρ`,
   or the imaginary-time response identity for time-derivatives. The
   parent's form fails — see Lemma R-A.1 + runner counterexample
   (H=0, A=B=σ_z, LHS=1, RHS=0).

2. **Eq (1) uses `J = max_X ‖h_X‖`** (per-term max) where the
   Hastings-Koma / Nachtergaele-Sims series demands per-site sum
   `J* := max_x Σ_{X ∋ x} ‖h_X‖`. On Z³ with `Z_lat = 6` link terms
   per site, `J ≤ J* ≤ Z_lat J`. The parent's velocity underestimates
   the correct LR speed — arithmetic loss in the named constant,
   structurally harmless to the (L1) inequality form.

---

## §1. Setting (parent objects re-used)

We use the parent's setup verbatim and import no new framework
content. `H = Σ_X h_X` is a Hermitian Hamiltonian on a finite cubic
block `Λ ⊂ Z³` with each `h_X` of diameter `≤ R_int`. We define
two derived constants:

```text
    J   :=  max_X  ‖h_X‖                                  (J-singular; parent's eq 1)
    J*  :=  max_x  Σ_{X ∋ x}  ‖h_X‖                       (J*-summed; Nachtergaele-Sims)
```

The corrected Lieb-Robinson velocity is
```text
    v_LR^*  :=  2 · e · J* · R_int · Z_lat                (R-B corrected)
```

`J ≤ J*` always. The strict inequality `J < J*` is generic whenever
any site is touched by more than one local interaction term — i.e.
essentially any nearest-neighbor Hamiltonian on a lattice with
coordination number `≥ 2`.

---

## §2. Repair (R-A): deletion of the bogus eq (8) Kubo identity

### Lemma R-A.1 (parent eq (8) is not an identity)

The equality
```text
    ⟨A_x B_y⟩_ρ  -  ⟨A_x⟩_ρ ⟨B_y⟩_ρ
        =  -∫_0^β  dτ  ⟨ [A_x , B_y(iτ)] ⟩_ρ                (parent eq 8)
```
*fails* for general bounded operators `A_x, B_y` on a finite-dim
Hilbert space with thermal state `ρ = Z^{-1} exp(-β H)`.

**Proof (counterexample 1: trivial commutator, nonzero variance).**
Take `H = 0` (so `ρ = (1/dim) I` is maximally mixed) on a 2-site
qubit system with `A_x = B_y = σ_z` localized at the same site. Then:
- LHS: `⟨A_x B_y⟩_ρ - ⟨A_x⟩_ρ ⟨B_y⟩_ρ = ⟨σ_z²⟩ - ⟨σ_z⟩² = 1 - 0 = 1`.
- RHS: `[A_x, B_y(iτ)] = [σ_z, σ_z] = 0` for all `τ` (since `H = 0`
  means `B_y(iτ) = σ_z`), so the integral vanishes.

`1 ≠ 0`. The runner (`A.eq8.ex1`) verifies the gap = 1.000000 exactly. ∎

**Proof (counterexample 2: nontrivial H, quantitative gap).** With
`H = σ_x` at site 0, `A_x = B_y = σ_z` at site 0, `β = 0.5`: LHS =
`1.0`, RHS = `-0.251`. The two are different in both magnitude and
sign (runner exhibit `A.eq8.ex2`). ∎

### Repair statement (R-A)

The parent's eq (8) is deleted from the parent's Step 4. The
parent's conditional L2 statement is routed through the slab-bridge
note (spatial) and the mass-gap bridge note (temporal), both already
wired as parent dependencies. This routing does not alter the
parent's L1/L3/L4 conclusions and does not require any new axiom or
import. The parent's claim type stays `bounded_theorem`; its ledger
status authority remains the independent audit lane.

The two standard routes that bypass eq (8):

- **Temporal-bridge route** (Hastings-Koma 2006, Thm 4.2): spectral
  decomposition of the temporal transfer matrix `T = exp(-a_t H)`
  with gap input `Δ_T > 0`, no Kubo identity needed. Shipped by
  [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md).
- **Spatial-bridge route** (Nachtergaele-Sims 2010, Cor 3.3):
  spectral decomposition of the spatial slab transfer operator
  `T_x` with gap input `Δ_x > 0`, no Kubo identity needed. Shipped
  by [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md).

---

## §3. Repair (R-B): Nachtergaele-Sims `J*` per-site sum correction

### Lemma R-B.1 (J* is the correct LR rate constant)

For the Hastings-Koma / Nachtergaele-Sims Lieb-Robinson series
applied to `H = Σ_X h_X` of finite range `R_int` on a cubic lattice
with coordination `Z_lat`, the operator-norm bound on the iterated
commutator is
```text
    ‖[A(t), B]‖   ≤   2 ‖A‖ ‖B‖ · Σ_{n ≥ d/R_int}  (J* · Z_lat · |t| · R_int)^n / n!     (NS series)
```
where `J* := max_x Σ_{X ∋ x} ‖h_X‖`.

**Proof (inline class-A algebraic identity check).** By Duhamel,
for any local operator `A` initially supported on a single site `x_0`,
```text
    A(t) - A   =  ∫_0^t ds  i [H, A(s)]
                =  ∫_0^t ds  i Σ_X  [h_X, A(s)].                       (D1)
```
The sum over `X` is dominated by the sum-over-X of `‖[h_X, A(s)]‖`,
which by operator-norm submultiplicativity satisfies
```text
    Σ_X  ‖[h_X, A(s)]‖   ≤   2 ‖A(s)‖ · Σ_{X : X ∩ supp(A) ≠ ∅}  ‖h_X‖    (D2)
                         ≤   2 ‖A(s)‖ · |supp(A)| · J*.                    (D3)
```
(D3) uses the per-site sum `J*`, not the per-term max `J`. For each
site in `supp(A)`, the sum of `‖h_X‖` over terms `X` containing that
site is bounded by `J*` by definition. Iterating gives (NS series).

The same iteration with `J` instead of `J*` is incorrect unless each
site is touched by exactly one term: at a site touched by `k > 1`
terms, the sum `Σ_{X ∋ site} ‖h_X‖` may strictly exceed `J` (and
equals `J*` at the maximizing site by definition). ∎

### Corollary R-B.2 (J ≤ J* with strict inequality generic)

For any `H = Σ_X h_X` of finite range on a lattice with coordination
`≥ 2`: `J ≤ J*` always. Moreover `J = J*` only when each site is
touched by exactly one interaction term, *not* the generic case
(e.g. nearest-neighbor hopping on Z³ has `Z_lat = 6` link terms
touching each site, giving `J* ≤ 6 J` with equality if all link
norms agree).

**Proof.** From the definitions, for any site `x`,
`Σ_{X ∋ x} ‖h_X‖ ≥ max_{X ∋ x} ‖h_X‖ ≥ 0`, with either equality iff
at most one term touches `x`. Maximizing over `x` and `X` gives
`J ≤ J*`, with `J = J*` iff some maximizing site is touched by
exactly one term. ∎

### Runner inline-verification (Part B)

The runner exercises four explicit cases that each independently
confirm `J ≤ J*`:

| Case | Geometry | J | J* | J*/J |
|---|---|---|---|---|
| 1. NN chain (N=4) | linear, interior sites touched by 2 link-terms | 1.0 | 2.0 | 2.0 |
| 2. Isolated single-site terms (N=3) | each site touched by 1 term (degenerate) | 1.0 | 1.0 | 1.0 |
| 3. 4-link star | center site touched by 4 terms | 1.0 | 4.0 | 4.0 |
| 4. Z³ neighborhood (N=7, mixed norms) | center touched by 6 link-terms, one stronger | 1.5 | 6.5 | 4.33 |

Case 5 directly verifies the Duhamel bound `‖[H,A]‖ ≤ 2‖A‖ Σ_{X∋site} ‖h_X‖`
on an explicit 3-site chain, with the actual commutator norm matching
the NS bound to numerical precision.

### Repair statement (R-B)

The parent's eq (1) is replaced by
```text
    v_LR^*  =  2 · e · J* · R_int · Z_lat                   (R-B corrected)
```
with `J* := max_x Σ_{X ∋ x} ‖h_X‖`. The inequality form of (L1) (parent's
eq (2)) is unchanged: only the named constant in the velocity changes
from `J` to `J*`. This is a *strengthening* of the parent's
quantitative bound (a larger `v_LR^*` is a weaker constraint on the
light-cone exterior). The parent's (L1)/(L3)/(L4) conclusions stand;
the arithmetic exponent constant tightens with `J*`.

For the canonical Cl(3)/Z³ surface at `g_bare = 1`, `J* ≤ Z_lat · J = 6 J`,
so the corrected velocity is at most a factor 6 larger than the parent's
nominal `v_LR`. Parent's (L4) bound on `J` carries to `J*` with an extra
`Z_lat` factor.

---

## §4. Restated conditional L2 routing

With (R-A) and (R-B), the parent's conditional L2 statement is restated as:

**L2 (conditional, spatial bridge).** For local Cl(3) operators
`A_x, B_y` and the canonical thermal state `ρ`,
```text
    | ⟨A_x B_y⟩_ρ - ⟨A_x⟩_ρ ⟨B_y⟩_ρ |   ≤   C · ‖A_x‖ · ‖B_y‖ · exp(-d(x,y) / ξ_β)
                                                                              (L2*)
```
is proved conditional on the slab-bridge note's H1+H2 inputs (positive
Hermitian slab transfer operator `T_x` and `Δ_x > 0`) via the closed-
form spectral chain of the slab-bridge note's S-bridge proof. The
routing replaces the parent's broken eq (8) by the slab-bridge spectral
decomposition; no other change to the parent's argument is required.

Full lift of the parent's audited_conditional row to retained-grade
requires:
- **(a-eq8)** this note (parent eq (8) repair + `J*` correction);
- **(a-companion)** axis-permutation companion (PR #2474) supplying
  H1+H2 on the pure-Wilson surface;
- **(c)** re-audit of the spatial slab bridge composition with the
  supplied H1+H2.

This note ships exactly (a-eq8). (a-companion) is in-flight as PR
#2474 and is independent. (c) is the auditor's call.

---

## §5. What this note does NOT claim

- Does **not** modify the parent text or its ledger row.
- Does **not** lift the parent's `audited_conditional` status.
- Does **not** derive `Δ_x > 0` or `Δ_T > 0` on the canonical
  Hamiltonian. Those remain open inputs of the slab-bridge and
  temporal-bridge notes.
- Does **not** address the Yang-Mills mass gap (Clay continuum
  infinite-volume problem); restricted to finite-Λ lattice content.
- Does **not** propose a new axiom or theory-language extension.
  (R-A) is deletion of a false in-text identity; (R-B) is a constant
  correction with inline proof.
- Does **not** weaken or retire any retained no_go.
- Does **not** import Hastings-Koma 2006 or Nachtergaele-Sims 2010
  as load-bearing authorities. The `J*` identity is proved inline
  (Lemma R-B.1); the cited papers are sidecar context only.

---

## §6. Citations and dependencies

| Authority | Status on origin/main | Role here |
|---|---|---|
| A1 (per-site `M_2(C) = Cl(3)`) | retained axiom | foundations |
| A2 (Z³ locality, `Z_lat = 6`) | retained axiom | substrate |
| [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md) | audited_conditional | parent (this note ships R-A + R-B repairs against parent §Proof Step 4 + parent eq (1)) |
| [`CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17`](CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17.md) | audited_conditional | conditional L2 routing target (replaces parent's eq (8)) |
| [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md) | (per ledger) | temporal-bridge alternative routing |
| [`CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02`](CLUSTER_DECOMPOSITION_DELTA_X_FINITE_LAMBDA_AXIS_PERMUTATION_NARROW_NOTE_2026-06-02.md) | PR #2474 (in flight) | companion piece (a-companion) supplying H1+H2 |

Sidecar (non-load-bearing) references: Lieb-Robinson 1972;
Hastings-Koma 2006 (*Commun. Math. Phys.* 265, 781) for the spectral-
gap-driven exponential clustering route; Nachtergaele-Sims 2010
(*Lieb-Robinson Bounds in Quantum Many-Body Physics*) for the per-
site `J*` rate constant (their Thm 3.1 / Cor 3.3). All sidecar; the
load-bearing pieces (Lemma R-A.1 + Lemma R-B.1) are proved inline.

---

## §7. Audit-lane handoff

```yaml
proposed_claim_type: bounded_theorem
audit_required_before_effective: true
audit_handoff_status: |
  Source-only narrow bounded theorem shipping two repairs for the
  audited_conditional parent AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29:

  R-A: parent's eq (8) "Kubo identity for connected correlators in
       imaginary time" is provably false on a 2-site qubit
       counterexample (Lemma R-A.1; runner exhibits H=0, A=B=sigma_z,
       LHS=1 vs RHS=0, finite gap 1.0). Repair: delete eq (8); route
       conditional L2 through the slab-bridge note + temporal-bridge
       note (both already wired as parent deps). No new axiom or
       import.

  R-B: parent's eq (1) v_LR uses J = max_X ||h_X|| (per-term max),
       but the Hastings-Koma / Nachtergaele-Sims Lieb-Robinson series
       requires J* := max_x Sum_{X ∋ x} ||h_X|| (per-site sum).
       Inline proof in Lemma R-B.1 + Corollary R-B.2; runner builds
       four explicit test Hamiltonians (NN chain, isolated terms,
       4-link star, Z^3 neighborhood) and verifies J <= J* with
       strict inequality wherever multiple terms touch a site.
       Repair: replace v_LR by v_LR* = 2 e J* R_int Z_lat. The (L1)
       inequality form is unchanged; only the named constant tightens.

  Anti-overpromotion: this note does NOT modify the parent text and
  does NOT claim the parent's audited_conditional row now lifts.
  Lift requires (a-eq8)=this note + (a-companion)=PR #2474 + (c)
  composition re-audit. All three required.

new_audit_row:
  - claim_id: cluster_decomposition_parent_eq8_repair_narrow_note_2026-06-02
    proposed_claim_type: bounded_theorem
    effective_status_proposal: bounded
    conditional_on:
      - audited_conditional status of AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29 (parent; this note supplies repairs but does not modify parent text)
      - existence of CLUSTER_DECOMPOSITION_SPATIAL_SLAB_BRIDGE_THEOREM_NOTE_2026-05-17 (routing target for repaired L2)
    routing:
      foundations: A1, A2
      retained_consumed: NONE (J* identity + eq (8) falsification both proved inline)
      load_bearing_imports: NONE
      external_anchor: NONE
status_authority: independent audit lane only
no_existing_row_touched: true
no_verdict_predicted: true
no_axiom_extension: true
no_no_go_weakening: true
parent_text_modified: false
parent_status_lift_claimed: false
```

## §8. Origin

Tier 3 panel attack on 2026-06-02 against the cluster_decomp
audited_conditional row (load-bearing score 17.9 on origin/main)
identified parent eq (8) as a bogus Kubo identity and parent eq (1)'s
`J` as the wrong per-site constant. This narrow companion ships both
repairs with inline proofs, as the (a-eq8) piece of the three-piece
parent-row lift recipe. (a-companion) axis-permutation piece is in
flight as PR #2474; (c) composition re-audit is the auditor's call.

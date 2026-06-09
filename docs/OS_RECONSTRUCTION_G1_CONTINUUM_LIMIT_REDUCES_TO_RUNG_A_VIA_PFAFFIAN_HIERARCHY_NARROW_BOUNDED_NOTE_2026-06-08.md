# The OS Reconstruction's Continuum-Limit Residual G1 Reduces to Rung A via the Pfaffian Hierarchy

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a residual reduction)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_os_g1_continuum_limit_reduces_to_rung_a.py`](../scripts/frontier_os_g1_continuum_limit_reduces_to_rung_a.py)
**Cached log:**
[`logs/runner-cache/frontier_os_g1_continuum_limit_reduces_to_rung_a.txt`](../logs/runner-cache/frontier_os_g1_continuum_limit_reduces_to_rung_a.txt)
(TOTAL: PASS=6 FAIL=0)

## 0. What closes

The keystone — the free emergent-time massive Dirac field — bottoms out in the
Osterwalder-Schrader→Wightman reconstruction `R`
([`FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30`](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md)).
That note **derives** OS2/reflection positivity directly (its E2: the fermionic Gram matrix
`γ_4·S(τ_i+τ_j,k)` is PSD) and establishes the Gaussian n-point hierarchy (its E5: `Pf² = det`),
but lists one residual open — **G1**: that the framework's free *lattice* fermion measure converges
(`a→0`) to the continuum Dirac Gaussian, "rung A's 2-point statement extended to the measure, not
established here beyond the 2-point."

This note closes that extension for the fermionic field: **G1 reduces to rung A**, and rung A is now
`retained_bounded`, so the continuum-limit residual closes at the retained-bounded tier.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| rung A — continuum SO(4) convergence of the free staggered-Dirac 2-point | [`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md) | `retained_bounded` | the target of the reduction |
| OS reconstruction `R`: E2 (OS2 derived), E5 (Pfaffian hierarchy), G1 open | [`FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30`](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md) | `bounded` | the residual this closes |
| rung B — lattice reflection positivity (two-step transfer) | [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md) | `retained_bounded` | corroborating RP |
| spectrum / spin-statistics (positive energy + microcausality) | companion `KEYSTONE_MASSIVE_DIRAC…_VIA_T1_2026-06-08` | (this session) | the spectrum piece |

No PDG value is load-bearing. No new axiom, import, or vocabulary.

## 2. The reduction

**For a fermionic (Grassmann/Berezin) theory, the "measure" is its correlator hierarchy.** There is
no probability measure to make tight; the theory is *defined* by its n-point functions. So
"convergence of the measure" means convergence of every n-point correlator.

**Every n-point correlator is a continuous function of the 2-point.** Fermionic Wick (E5): the
`2n`-point correlator is the Pfaffian of the antisymmetric 2-point matrix `C_{ij}=⟨ψ_i ψ_j⟩`, with
`Pf(C)² = det(C)` (verified for `2n ∈ {2,4,6,8}`). The Pfaffian is a polynomial in the matrix
entries, hence continuous and locally Lipschitz (verified: `|ΔPf| → 0` as `|ΔC| → 0`).

**Therefore G1 reduces to rung A.** If the 2-point converges, `C_a → C` (rung A), then every
Pfaffian converges, `Pf(C_a) → Pf(C)` (verified: monotone `→ 0`), so every n-point correlator
converges — i.e. the fermionic theory converges. The continuum limit of the free fermionic field is
fixed by the continuum limit of its 2-point. With **rung A `retained_bounded`**, G1 closes at the
retained-bounded tier.

```text
G1 (free-field measure convergence)
   ⇐ rung A (2-point continuum convergence, retained_bounded)
     + E5 (every n-point = Pfaffian of the 2-point)
     + Pfaffian continuity.
```

## 3. Where this leaves the keystone

With G1 reduced to rung A, the free emergent-time massive Dirac field — the keystone gating the
chirality gate, the `Q=2/3` mechanism, generation-ID, and the #1 `s3_time` gate — has every piece in
hand at the retained-bounded tier:

| Keystone piece | Status |
|---|---|
| chiral grading / partner chirality | retained (`Cl(3,1)`) + supplied (companion notes) |
| positive energy + microcausality | forced by T1/CAR (companion note) |
| OS2 / reflection positivity | derived (E2) |
| n-point hierarchy | established (E5) |
| **continuum-limit measure convergence (G1)** | **reduces to rung A (retained_bounded) — this note** |
| boost sector (G2) | rests on the textbook OS reconstruction theorem |

So the only remaining OS residual is **G2** (the full positive-spectrum Poincaré representation),
which the reconstruction note carries on the **textbook** OS theorem (Osterwalder-Schrader 1973/75)
— a methodology citation, not a framework-specific gap.

## 4. Scope — what this establishes and what remains

**Establishes (exact / finite):**
- The fermionic Wick hierarchy `Pf² = det` and Pfaffian continuity.
- For the fermionic field, n-point convergence = theory convergence (the Berezin "measure" is the
  correlator hierarchy; no tightness needed).
- Therefore G1 reduces to rung A; with rung A retained_bounded, the continuum-limit residual closes
  at the retained-bounded tier.

**Remains:**
- **Does not close rung A itself** — the actual 2-point continuum SO(4) convergence is rung A
  (`retained_bounded`); this note reduces G1 *to* it, not past it.
- **G2** (the boost sector / full Poincaré rep) rests on the textbook OS reconstruction theorem.
- **Interacting theory out of scope** — free `U=1` only (the reconstruction note's G5). The
  reduction is for the free Gaussian/Grassmann field.
- Does **not** touch the firewalled `r=1/2`.

## 5. Honest verdict

The OS reconstruction's one named-open free-field residual — that the lattice fermion measure
converges to the continuum Dirac Gaussian beyond the 2-point — **reduces to rung A**. The reason is
structural and fermion-specific: a Grassmann theory *is* its correlator hierarchy, every correlator
is a continuous (Pfaffian) function of the 2-point, so the whole theory's continuum limit is carried
by the 2-point's. With rung A `retained_bounded`, the keystone's continuum-limit piece closes at the
retained-bounded tier, leaving only the textbook-carried boost sector (G2). The program's deepest
object — the free emergent-time massive Dirac field — now stands built at the retained-bounded tier,
with no framework-specific residual beyond rung A and the standard OS reconstruction theorem.

## 6. No-Go Discipline Gate

**Status:** PASS for this bounded reduction. It does **not** close rung A, the boost sector, or the
interacting theory; it reduces G1 to rung A.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| G1 needs an independent measure-convergence proof | RULED OUT | fermionic theory = correlator hierarchy; convergence = n-point convergence |
| n-point convergence needs more than the 2-point | RULED OUT | every n-point = Pfaffian of the 2-point (E5), continuous |
| G1 reduces to rung A | ESTABLISHED | 2-point convergence ⇒ all-correlator convergence |
| close rung A / G2 / interacting theory | OUT OF SCOPE | rung A is retained_bounded; G2 textbook; interacting excluded |

**N2 — Wall-independence.** The reduction (this note) and rung A (the 2-point continuum) are
distinct; this note reduces the first to the second.

**N3 — Hidden-wall scan.** Uses only fermionic Wick (`Pf²=det`), Pfaffian continuity, and the
Berezin identity theory-=-correlators; no hidden probability-measure premise (and none is needed).

**N4 — Residual matching.** The residual is exactly rung A (the 2-point continuum convergence), plus
the out-of-scope G2 and interacting theory.

**N5 — Rhetoric audit.** The claim is a *reduction* (G1 → rung A) for the *free* field, not a
construction of the interacting continuum theory.

**N6 — Partial-closure path scan.** With G1 reduced, the next OS step is G2 (the boost sector) and,
beyond the free field, the interacting theory — neither claimed here.

**N7 — Steelman.** A reviewer may note that bosonic continuum limits need measure tightness, so the
reduction looks too cheap. Granted for bosons — but the framework's field is *fermionic*, where the
Berezin "measure" is the correlator hierarchy itself; there is no probability measure to make tight,
and convergence of all Pfaffian correlators is the convergence of the theory. The note is explicitly
scoped to the fermionic field.

**N8 — Cross-cycle echo.** Consistent with the reconstruction note's E2 (OS2 derived) and E5
(Pfaffian hierarchy), rung A (retained_bounded), rung B (retained_bounded), and the companion
spectrum/spin-statistics closure — connecting them without overruling any by prose.

## 7. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained-bounded / bounded rows plus
  fermionic Wick combinatorics and the Pfaffian identity.
- **No PDG/fitted load-bearing input; no new transcendental; no forcing of `r=1/2`.**

## 8. Command

```bash
python3 scripts/frontier_os_g1_continuum_limit_reduces_to_rung_a.py
```

Expected: `TOTAL: PASS=6 FAIL=0`. numpy + stdlib, deterministic, ≤8×8 Pfaffians (memory-safe). The
runner verifies `Pf²=det` for `2n ∈ {2,4,6,8}`, Pfaffian continuity, and the convergence
`Pf(C_a) → Pf(C)` as `C_a → C`.

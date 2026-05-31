---
claim_id: brannen_delta_spectral_asymmetry_convention_isolation_note_2026-05-31
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Brannen δ and the spectral-asymmetry weight: the structural tie and the one-π convention gap

**Date:** 2026-05-31
**Claim type:** structural-tie + no-go-sharpening (finite/algebraic). Adds no
axiom and no import; **adopts no radian convention**.
**Status authority:** independent audit lane only. Sets/requests no verdict;
edits no audit row. Advances (does not close) the open gate
`lepton_brannen_bae_delta_two_ninths`.
**Primary runner:**
`scripts/frontier_brannen_delta_spectral_asymmetry_convention_isolation.py`
with cache
`logs/runner-cache/frontier_brannen_delta_spectral_asymmetry_convention_isolation.txt`
(16/16 checks).

## Question

The charged-lepton CP / orientation phase `δ_Brannen = arg(b)` and the
spectral-asymmetry weight
`L_3(1,2)` ([`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md),
retained_bounded) are **both `2/9`** on the **same** native `C₃` generation
operator `H = aI + bC + b̄C²` (`H=iD`). Is `δ = 2/9 rad` therefore a *derived*
consequence — the spectral-asymmetry phase / APS-η holonomy of `H` — or is the
coincidence a radian-convention artifact? ("No coincidences": derive the tie, or
isolate exactly what is structural vs convention.)

## Result: the tie is structural as a number; the radian assignment is one factor of π

**Verdict: convention-bound.** The `2/9` is shared and structural; the radian
value `δ = 2/9 rad` is **not** forward-derived — the single gap is exactly one
factor of `π`.

### 1. Same operator, same doublet (not a bare coincidence)

`L_3(1,2) = (1/N) Σ_k det[(C^k − I)^{-1} | doublet] = 2/9` is the
holomorphic-Lefschetz / Molien **weight** of `H`'s doublet (runner §A). The phase
`δ = arg(b)` is the `SO(2)` angle on the same doublet's native complex structure
`Jcs = (C − C²)/√3` (`Jcs² = −P_doublet`, `exp((2π/3)Jcs) = C`, period `2π`), and
it is **Q-orthogonal** (`Q` depends only on `|b|/a`;
[`KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md`](KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md),
retained_bounded). So the two `2/9`s sit on the same `C₃` doublet operator — a
genuine structural tie, not a bare numerical pun. Empirically (PDG
charged-lepton masses, runner §B) the Brannen phase reduces to `δ = 0.22223 rad`,
matching the **bare** `2/9 = 0.22222` to `~1×10⁻⁵` (with `Q = 0.66666`).

### 2. The gap is exactly one factor of π

The framework's native angle carrying `2/9` is the Plancherel-step
`α₃ = (2/9)·π = 0.698 rad`
([`KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md`](KOIDE_DIMENSIONLESS_RADIAN_NATIVE_UNIT_SEPARATION_NARROW_THEOREM_NOTE_2026-05-25.md),
retained_bounded). The η-holonomy argument is `2π·(2/9) = 1.396 rad`. The
empirical `δ = 0.2222 rad` is the **bare** `2/9`. Exactly (runner §C):

```
α₃ = π · δ_empirical          (α₃ / δ_bare = 3.14159… = π)
```

Reaching the bare `0.2222 rad` requires reading the dimensionless `2/9` directly
as radians — the **period-1-rad vs 2π-rad** choice that the retained no-go
[`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)
(retained_no_go) already isolated as its sharpened residual. This note does **not**
adopt that convention.

### 3. The η-as-phase escape is falsified (it targets the wrong number)

A previously-floated route held that `δ` is the APS-η holonomy of `H` (η lives
mod ℤ → an intrinsic phase). It is **false**, three ways (runner §D):

- the genuine **spin-Dirac equivariant eta** of the rotation data `(1,2)` is
  `η_APS(Z_3;1,2) = 0` exactly (csc-product) — the mod-ℤ phase object is *zero*,
  not `2/9`;
- the **finite equivariant eta** `η_C(H)` is **integer-valued** `{0, 2}`
  (jumping across the `r=1` doublet zero-crossing) — also not `2/9`;
- `2/9` is **not an algebraic integer** (minpoly `9x−2`, non-monic), so **no**
  eta / index / spectral-flow / holonomy value can ever equal it. And the Berry
  connection of the circulant `H(θ)` is **identically 0** (the eigenvectors are
  the fixed θ-independent Fourier modes; `δ` is a free `SO(2)` *parameter*, not a
  geometric-phase *output*).

So `2/9` is the **Lefschetz/Molien weight**, not a phase; the η-as-phase bridge
does not close the radian gap.

### 4. The "(N−1)/N²" framing is a pun at N=3

The weight is `L_N(1,N−1) = (N²−1)/(12N)` (the second-moment / Bernoulli /
APS-defect / CFT-orbifold family), **not** `(N−1)/N²` (the Fisher / Burnside
rank-count family). The two are different functions of `N` that **coincide only
at `N=3`** (both `2/9`; e.g. at `N=5`, `2/5` vs `4/25`) (runner §E). So the
shared "`(N−1)/N²` mechanism" is a coincidence of the two families at `N=3`, not
a law tying the weight and the phase by one mechanism.

## Disposition (honest)

- **Structural (derived, retained_bounded):** the dimensionless value `2/9 =
  L_3(1,2)` as the Lefschetz/Molien weight of `H`'s doublet; the empirical
  Brannen `δ` is the bare `2/9` in radians on the same operator.
- **Convention-bound (the gap):** the radian assignment `δ = 2/9 rad` is the
  bare rational read as radians — exactly one factor of `π` from the native
  `α₃`. This is the period-1-rad vs 2π-rad convention, audit-decided per
  precedent (the radian-reclassification meta-note), **not** forward-derivable
  and **not** user-ratified.
- **Falsified:** the "`δ` is the APS-η holonomy" route (η is `0`, `η_C` is an
  integer, `2/9 ∉ ℤ[ω]`, Berry phase `0`).

Net: `δ = 2/9 rad` is **not** a coincidence and **not** a derivation — it is a
structural value plus one open period-normalization. This sharpens the retained
radian no-go and advances the open gate `lepton_brannen_bae_delta_two_ninths`.

## Non-circularity

`δ = 2/9` is never assumed: the empirical Brannen phase is reduced from PDG masses
and *compared* to `2/9`; the weight is computed forward from `H`; the native and
η-holonomy angles are computed and shown *not* to equal the empirical value
(runner §B–D).

## External Context (context only — never load-bearing)

Atiyah–Bott / Donnelly (Lefschetz/Molien weight), APS (the η invariant) name the
geometric objects the framework's finite weight coincides with or differs from;
the spin-Dirac lens eta is shown to be a *different* number (`0`), so nothing here
rests on importing it.

## Boundary (the next path this opens)

This closes no route. Two open paths to convert the dimensionless `2/9` weight
into the `2/9`-radian phase, **neither** touching any retained negative result:
(1) an **audit-decided period-1-radian adoption** via the meta convention
precedent (source-note + paired-runner + independent audit, `claim_type=meta`);
(2) an independent **Fisher–Rao dual-metric** route on the doublet that
canonicalizes the angle scale and — if it can also pin the *value* — could supply
`2/9 rad` under audit. Both are open; this note adopts neither.

## No-Go Discipline Gate

**N1 — Alternative routes.** Five tested: η-as-phase (η=0, falsified), Jcs
holonomy (Berry phase 0; native quanta all `q·π`), `(N−1)/N²` universality
(family pun at N=3), radian convention (the three native conventions give
`(2/9)π` or `2π(2/9)`, not bare `2/9`), and adjudication (value derived, radian
convention-bound). None forward-derives `δ = 2/9 rad`.

**N2 — Wall-independence.** The algebraic-integer wall (`2/9 ∉ ℤ[ω]`) and the
native-unit separation (every native angle is `q·π`; bare `2/9 ∉ ℚ·π`) are
independent; either alone blocks `δ = 2/9 rad` as a forced holonomy.

**N3 — Hidden-wall scan.** The empirical `δ` is reduced from PDG masses (no
framework input); the native `α₃` and the η-holonomy are forward computations;
the Berry phase 0 rests on the fixed-Fourier-basis diagonalization of `H(θ)`.

**N4 — Residual matching.** The lone residual is the period-1-rad vs 2π-rad
convention — identical to the sharpened residual of the retained radian no-go.

**N5 — Rhetoric audit.** "Convention-bound" means the *radian normalization* is a
unit convention; the *value* `2/9` is structural. It does not mean `δ` is
unrelated to `L_3` (it is the same `2/9` on the same operator) nor that a future
audited convention could not adopt it.

**N6 — Partial-closure path.** The Boundary lists two concrete open adoptions; no
new axiom is required.

**N7 — Steelman.** A reviewer may hold that the empirical agreement (`1×10⁻⁵`,
`2/9` inside the PDG 1σ band) *is* evidence for the period-1 reading. Granted as
motivation — but it does not *derive* the convention; the native angle remains
`(2/9)π`, off by exactly `π`.

**N8 — Cross-cycle echo.** The same period-1-rad vs 2π-rad residual appears in the
radian-bridge no-go and the native-unit-separation theorem. This note sharpens it
to the specific `δ ↔ L_3` tie without adopting a convention.

## Anchors (live-ledger tiers, verified origin/main 2026-05-31)

retained / retained_bounded / retained_no_go:
`axiom_first_z_n_equivariant_spectral_asymmetry` (retained_bounded),
`cpt_exact_real_anti_hermitian_d` (retained_bounded),
`koide_dimensionless_radian_native_unit_separation` (retained_bounded),
`koide_q_readout_factorization` (retained_bounded),
`koide_a1_radian_bridge_irreducibility` (retained_no_go),
`new_parity_is_circulant_phase` (retained_bounded). Open gate advanced:
`lepton_brannen_bae_delta_two_ninths` (open_gate). The unaudited
`koide_berry_phase_theorem` / `koide_readout_lane_demarcation` rows are **not**
cited as retained — the Berry-phase-0 and Q-orthogonality facts are reproduced
independently (runner §A, §D) / via the retained `koide_q_readout_factorization`.

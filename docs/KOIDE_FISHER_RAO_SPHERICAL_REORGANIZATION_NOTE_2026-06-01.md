---
claim_id: koide_fisher_rao_spherical_reorganization_note_2026-06-01
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Charged-lepton Koide on the Fisher-Rao sphere: cos²(θ_p)=1/(3Q), and why the azimuth value 2/9 is not Fisher-forced

**Date:** 2026-06-01
**Claim type:** bounded structural identity + demarcation. Adds no axiom and no
import; **adopts no records metric and no radian convention**.
**Status authority:** independent audit lane only. Sets/requests no verdict;
edits no audit row. Advances (does not close) the open gate
`lepton_brannen_bae_delta_two_ninths`.
**Primary runner:**
`scripts/frontier_koide_fisher_rao_spherical_reorganization.py`
with cache
`logs/runner-cache/frontier_koide_fisher_rao_spherical_reorganization.txt`
(14/14 checks).

## Question

The companion note `BRANNEN_DELTA_SPECTRAL_ASYMMETRY_CONVENTION_ISOLATION_NOTE_2026-05-31`
(sibling PR) found `δ_Brannen = 2/9 rad` to be convention-bound, one factor of `π`
from the native angle `α₃ = (2/9)π`. The named next path was the Fisher-Rao route. The
Brannen `√m` ansatz **is** the Fisher-Rao embedding `p ↦ √p` of the mass-fraction
distribution `p_k = m_k/Σm`, so both Koide data are coordinates of one point on
the Čencov-canonical sphere. Does Fisher-Rao **derive** `δ = 2/9 rad` — the
radian normalization *and* the value?

## Result: the reorganization is exact; the value is not Fisher-forced

**Verdict: normalization-only.** Fisher-Rao supplies a clean geometric stage and
dissolves the literal one-`π` framing, but does **not** force the value `2/9`.

### 1. Koide is exactly a Fisher-Rao polar angle (positive, import-clean)

Let `θ_p` be the Fisher-Rao geodesic polar angle of the `√m` point from the
democratic (`C₃`-singlet) axis `(1,1,1)/√3`. Then (runner §A, symbolic):

```
cos²(θ_p) = (Σ √m_k)² / (3 Σ m_k) = 1/(3Q),     Q = Σ m_k / (Σ √m_k)².
```

So `θ_p = π/4 ⟺ Q = 2/3` (`cos² = 1/2`), confirmed forward from PDG
(`θ_p = 0.78539`, `Q = 0.66666`). The Brannen phase `δ = arg(b)` is the Fisher-Rao
**azimuth** about that axis — definitional, since the ansatz
`√m_k/a = 1 + √2 cos(δ + 2πk/3)` is the `√p` sphere point in polar form (runner
§B). Thus `(Q, δ) = (polar π/4, azimuth)` of one Fisher-Rao point.

### 2. The Fisher carrier dissolves the literal (2/9)π framing (a real, partial gain)

The Fisher azimuth is a genuine **period-2π planar angle**, and the nearest-vertex
arc lands on the **bare** empirical `0.22223 rad` **directly** — not on
`α₃ = (2/9)π = 0.698 rad`, which overshoots by exactly `π` (runner §B). So the
specific `(2/9)π`-vs-bare-`2/9` ambiguity of the prior note is **dissolved on the
Fisher carrier**: there is no spurious `π` on this stage.

### 3. The value 2/9 is NOT Fisher-forced (decisive)

The Fisher-Rao metric about the democratic axis is the round-sphere metric
`g = dθ² + sin²θ dφ²`; `g_φφ = sin²θ` is **independent of `φ`**, so `∂_φ g = 0` —
`∂/∂φ` (rotation about the singlet axis) is a **Killing vector**, an exact Fisher
**isometry** (runner §C). The azimuth is therefore a **free isometry direction**;
the Čencov metric assigns **no preferred azimuth**. Concretely:

- **No Fisher invariant equals `2/9`:** the azimuthal arc length
  `sin(θ_p)·δ = 0.157`, the geodesic distance to the singlet is `π/4`; only the
  **bare coordinate** (the convention-bound quantity) is `≈ 2/9`.
- **The azimuth is an input, not an output:** it **drifts smoothly** with mass
  (runner §D); exact `2/9` requires `m_τ = 1776.97 MeV`, **0.9σ** off PDG
  `1776.86 ± 0.12`. A forced value would be mass-invariant.

So `δ = 2/9 rad` is **not** a Fisher-Rao prediction.

### 4. The normalization is relocated, not removed

Three residuals survive (runner §E): (i) a generation relabel (cyclic
permutation) shifts the azimuth by exactly `2π/3`, so the physical period is
`2π/3` and `2/9` is clean **only** as a period-1-rad count — the
period-1-vs-`2π` residual of the retained no-go
[`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md);
(ii) the azimuth **origin** = nearest (τ) vertex imports the generation
mass-ordering (the `O(2)` isometry makes the zero arbitrary; the three corners
give only a `C₃` triad); (iii) equating the geometric azimuth with the
dimensionless Lefschetz weight `L_3(1,2) = 2/9`
([`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md),
which itself disclaims any `δ` identification) is exactly the
Type-B-rational→radian primitive the radian-bridge no-go names as irreducible.

`α₃ = (2/9)π` and the Fisher azimuth `= bare 2/9` are two genuinely different,
equally-native angular objects differing by exactly `π`; which is "canonical" is
an audit-decided unit choice, not self-certifying.

### 5. The polar π/4 adds nothing to the value

`Q = 2/3` holds for **all** `δ` at amplitude `√2` (signed reading; `Σλ = 3`,
`Σλ² = 6`, runner §E), so `θ_p = π/4` is `Q = 2/3` **restated** — it constrains
only the `√2` amplitude (the counting-bit / `r = 1/2` gate, retained
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)),
orthogonal to the azimuth.

## Disposition (honest)

- **Derived, import-clean:** `cos²(θ_p) = 1/(3Q)` — Koide as a Fisher-Rao polar
  angle; and `δ` as the Fisher azimuth (definitional, period-2π).
- **Normalization gain (partial):** the Fisher carrier dissolves the literal
  `(2/9)π`-vs-bare-`2/9` framing — there is no spurious `π` on the sphere.
- **Not derived:** the **value** `2/9` (the azimuth is a free Killing direction;
  `2/9` is the observed, mass-drifting coordinate, not a Fisher invariant) and the
  **normalization uniqueness** (radian-vs-cycle is the universal convention; the
  origin imports mass-ordering; the value-bridge is the radian-bridge primitive).

Net: Fisher-Rao **reorganizes** charged-lepton Koide as the two spherical
coordinates of one `√m` point and **dissolves the literal one-`π` framing**, but
`δ = 2/9 rad` stays **open** — the metric provably cannot force a free isometry
direction. Advances `lepton_brannen_bae_delta_two_ninths` (still open_gate).

## Non-circularity and scope

`δ = 2/9` is never assumed: `θ_p` and the azimuth are computed forward from PDG
masses and compared to `π/4` and `2/9`. This note does **not** adopt Fisher-Rao
as the framework-native records metric — there is no retained ledger row for that
(the retained_bounded sharp-record Fisher-tangent theorem is audit-scoped and has
no azimuth content), so "Fisher azimuth in bare radians is the canonical native
angle" remains a candidate audit-decided unit proposal, not asserted here.

## Boundary (the next path this opens)

This closes no route. The value question reduces to one unbuilt object: a
**records/Born variational principle on the simplex that breaks the `O(2)`
isometry** about the democratic axis — a `C₃`-character-coupled action that
selects both the origin meridian (the heaviest-corner / mass-ordering) and a
specific longitude. The metric alone provably cannot do this (Killing symmetry);
only a non-isometric functional can pin the azimuth value. That is the concrete
structural bridge `δ = 2/9` now reduces to.

## No-Go Discipline Gate

**N1 — Routes.** Five tested: spherical-coordinate unification, is-azimuth-forced,
polar-π/4=Q, Čencov-canonicality, derivable-or-input. All return
normalization-only: the value is a free Killing direction.

**N2 — Wall-independence.** The Killing symmetry (value not forced) and the
period-1-vs-2π residual (normalization not unique) are independent; either alone
blocks `δ = 2/9 rad` as a Fisher derivation.

**N3 — Hidden-wall scan.** `cos²θ_p = 1/(3Q)` is symbolic-exact; the Killing
result is `∂_φ g = 0` symbolic; the mass-drift and `2π/3` relabel shift are
forward from PDG.

**N4 — Residual matching.** The lone value-residual is the Type-B-rational→radian
primitive (radian-bridge no-go); the normalization-residual is the universal
radian-vs-cycle convention plus the mass-ordering origin.

**N5 — Rhetoric audit.** "Normalization-only" means Fisher fixes the *stage* and
dissolves the literal `(2/9)π` framing, not that `δ` is derived. The value and the
normalization-uniqueness stay open.

**N6 — Partial-closure path.** The Boundary names the concrete open object (an
`O(2)`-breaking records/Born functional); no new axiom is required here.

**N7 — Steelman.** Granting Fisher-Rao-as-native (Čencov-unique on the Born
simplex) is defensible — but even granted, the metric is azimuthally isotropic and
cannot force the value; it only legitimizes the period-2π stage, audit-decided.

**N8 — Cross-cycle echo.** The same value/normalization residuals appear in the
radian-bridge no-go, the native-unit-separation theorem, and the δ
convention-isolation note. This note adds the exact Fisher polar=Q identity and
the Killing-symmetry proof that the azimuth value is free.

## Anchors (live-ledger tiers, verified origin/main 2026-06-01)

retained / retained_bounded / retained_no_go / open_gate:
`koide_circulant_q_two_thirds_algebraic` (retained),
`axiom_first_z_n_equivariant_spectral_asymmetry` (retained_bounded),
`koide_dimensionless_radian_native_unit_separation` (retained_bounded),
`koide_q_readout_factorization` (retained_bounded),
`koide_a1_radian_bridge_irreducibility` (retained_no_go),
`lepton_brannen_bae_delta_two_ninths` (open_gate, advanced). The unaudited
`yt_primitive_source_unit_fisher_normalization` is **not** cited as retained; the
Fisher computation here is first-principles and import-clean.

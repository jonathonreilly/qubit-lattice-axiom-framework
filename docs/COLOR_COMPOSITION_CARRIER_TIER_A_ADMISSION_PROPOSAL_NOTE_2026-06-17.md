# Color Composition-Carrier — Tier-A Admission PROPOSAL

**Date:** 2026-06-17
**Type:** meta / proposal
**Status:** **PROPOSAL ONLY.** This note proposes a third Tier-A admitted input for
the color/strong-gauge sector. It does **not** register the admission and does
**not** set any audit status. Audit status is set only by the independent audit
lane. Registration into `docs/audit/data/tier_a_admissions.json`
(`genuine_admitted_input_count` 2 → 3) and the required minimality-policy
approval (`docs/audit/AXIOM_MINIMALITY_POLICY.md`) are owner / audit-lane steps;
this note is the artifact for that lane to approve or reject.

**Proposes:** the admission `COMP` (working id
`color_composition_carrier_admission`), the formal registration of the existing
color matter-realization residual (`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md`,
"MR_color") as a named Tier-A admitted derivation target alongside
`AC_phi_lambda` and `theta`.

**2026-07-04 premise refresh:** the obstruction underlying this proposal was
established on the pre-reset three-axiom base. This note is restated against
the current four-axiom base (Lattice, Qubit, Admissibility, Record —
`docs/MINIMAL_AXIOMS_2026-06-29.md`, including the 2026-07-04 formation
sentence); see the carry-over argument opening §4. The restatement is
proposal-level rationale; audit status of every cited support note remains
audit-lane-owned.

---

## 1. The admission (minimum statement)

> **COMP.** The internal gauge-carrier medium (the structure on which matter's
> non-spacetime gauge degrees of freedom live) carries a **normed composition
> (division) algebra** structure, equipped with an **oriented / T-odd grading**.

Color `SU(3)` and one matter generation are then *consequences* of `COMP`, not
further admissions: the oriented maximal composition algebra is the octonions
`O`, with `SU(3) = Stab_{G2}(one imaginary unit)` inside `G2 = Aut(O)` and the
complex Clifford module `C^8 = 1 + 3 + 3bar + 1` supplying one generation's
color content. The medium acts as a **label** on the associative site carrier
(`M_2(C)`); it is **not** the operating algebra (see §4, defeater (c)).

## 2. Minimum decomposition (three named sub-admissions)

Mirroring the internal structure of `AC_phi_lambda` (which decomposes into three
sub-admissions), `COMP` decomposes into:

- **(i) composition-algebra hypothesis.** The internal carrier is a normed
  division (Hurwitz) algebra. This selects the `{R, C, H, O}` class; with (ii)
  it lands on `O` and hence on `SU(3)` color.
- **(ii) oriented / T-odd grading.** An orientation on the minimal closed cell
  (equivalently a complex structure that is *not* a spacetime/`O_h` datum),
  splitting the color triplet `3` from its conjugate `3bar` (the quark vs
  antiquark / `3 != 3bar` complex, handed structure). Without it the structure
  is real/self-conjugate and carries no `3 != 3bar`.
- **(iii) carrier-vs-label realization bridge.** The identification that this
  internal composition/label structure realizes *physical* `SU(3)` color on the
  associative matter carrier — the abstract-structure → physical-species bridge,
  analogous to `AC_phi_lambda`'s species-bridge sub-admission.

Bare color-name labels (red/green/blue) remain a vacuous convention, not a
derivation target.

## 3. Class, leverage, downstream scope

- **Class:** internal gauge-carrier / color-sector structural input.
- **Confers bounded status on:** the entire color/strong sector downstream —
  `SU(3)` color, the packaged one-generation content (`C^8 = 1+3+3bar+1`), and
  `beta = 6 = 2 N_c` (which follows once color exists; this is distinct from the
  separate `N_c = d = 3` / coordination-number numerology, which `COMP` does not
  rely on).

## 4. Why this is a genuine admission, not a theorem (support / no-go portfolio)

`COMP` is established as **non-derivable** from the framework axiom base. The
obstruction was established (2026-06-16/17) on the then-current three-axiom
base `{Lattice, Quantum, Record}`; it carries to the current four-axiom base
`{Lattice, Qubit, Admissibility, Record}` because the two subsequent
foundation changes supply none of the missing structure (restatement,
pending audit-lane re-check like every premise-hash dependent):

- **Admissibility (2026-06-29)** names one fixed nearest-neighbor availability
  rule, covariant under the lattice motions; per its recorded approvals it
  names no operator, kinetic class, selector, or carrier. The color
  obstruction is geometric — every framework-derivable multiplet is
  spatially covariant, while color requires a spatial-**singlet** internal
  arena of real dimension >= 6 — and a spatially-covariant availability rule
  cannot supply a spatial-singlet internal arena.
- **Record formation ("Records form.", 2026-07-04)** adds occurrence at axiom
  strength only; every formation rule (possibility, site, weight, rate)
  remains downstream — no internal carrier content.

The following landed notes set out the obstruction (their audit status is set
only by the audit lane):

- `COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md` — color sits at an
  irreducible matter-realization residual (MR_color); the Record axiom and the
  post-record layer *consume* color after it is supplied, they do not generate
  it.
- `CL3_SU3_SYMMETRIC_BASE_COMMUTANT_GELL_MANN_EMBEDDING_NARROW_THEOREM_NOTE_2026-05-27.md`,
  `COLOR_GENERATION_INDEPENDENT_Z3_STRUCTURES_2026-06-05.md`,
  `COLOR_LINK_INDEX_ROUTING_CARRIER_BUDGET_2026-06-05.md` — the framework's
  realized three-folds are spatially-covariant; a single qubit hosts only
  `su(2) + u(1)`.
- `G2_BRIDGE_C3_CURRENT_CANNOT_BEAT_GAP_A_NO_GO_NOTE_2026-06-06.md` — the `C_3`
  current does not close the gap to physical color.
- `CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md`,
  `CL3_BARYON_QQQ_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md`,
  `MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09.md`
  — given color, the framework's closure/Record machinery correctly *consumes*
  it (singlet selection, depolarization to the gauge-required `I_3/3`), the
  consumer side of MR_color.

Session-level analysis underlying the minimum statement (NOT landed; recorded
here as rationale only, audit status not asserted):

- A forcing test built in direct analogy to the local-tomography argument that
  forced the complex unit `i` inside the Qubit (then named "Quantum") carrier
  **failed** at high confidence. `{intrinsic i + Record-closure + minimality}` force only "a
  compact gauge group over `C`"; the step "compact group over C ⇒ normed
  composition algebra" is the single irreducible posit. Three independent
  defeaters of any attempt to *force* it:
  - **(a) category error:** loop/Wilson closure is multiplicativity of a *group*
    product; a composition algebra is multiplicativity of a *quadratic norm* on
    a bilinear carrier — different objects.
  - **(b) operationally false at the target:** the color carrier `C^3` has real
    dimension 6, which is **not** a Hurwitz dimension `{1,2,4,8}`; `SU(3)` is the
    unit group of no normed division algebra.
  - **(c) Jacobi excludes the octonion as the carrier:** gauge consistency (the
    Jacobi identity) requires associativity; the non-associative octonion can
    only ever be a *label* for `SU(3)`, never the operating algebra.

## 5. Why Tier-A admission, not axiom, not primitive

A two-panel placement review (framework-blind axiomatic-method / foundations /
operational-reconstruction experts) reached this at high confidence:

- **Not an axiom.** Axioms are *constitutive* (open a new fundamental category /
  slot) and are not derivation targets. `COMP` enriches the existing carrier
  slot, is selective/contentful (it fixes `SU(3)` + one generation), and its
  independence is non-derivability from a *failed forcing test*, not from
  answering a new constitutive question. The one defensibility hook —
  type-symmetry with the Qubit axiom's `C` (itself a composition algebra) — is
  analogy of form, not shared mechanism, and is actively refuted by the failed
  forcing test (the same kind of test that *demoted* `i` to a consequence). No
  logically defensible reason to elevate `COMP` to an axiom was found.
- **Not a primitive.** Approved primitives (`scale_reference`,
  `kinetic_isotropy`, `realized_state`) supply "a slot, not content" and confer
  no bounded status. `COMP` carries the heaviest dimensionless selector content
  in the matter sector (it selects the gauge group and particle content) —
  exactly what the primitive boundary forbids.
- **Is Tier-A.** Contentful + currently underivable + confers bounded status
  downstream; structurally parallel to `AC_phi_lambda` (primary admission +
  named sub-admissions). The framework's genuine admitted inputs would then form
  a clean triple, one per matter-sector fact it does not derive: flavor
  (`AC_phi_lambda`), strong-CP (`theta`), color-carrier (`COMP`).

## 6. Proposed registry entry (for the audit lane to apply — NOT applied here)

The following is the *proposed* shape of the `tier_a_admissions.json` entry. It
is reproduced here for review only; this note does not edit the registry.

```json
"color_composition_carrier_admission": {
  "label": "COMP",
  "statement": "the internal gauge-carrier medium is a normed composition (division) algebra with an oriented/T-odd grading; SU(3) color + one generation (C^8=1+3+3bar+1) follow as consequences; the medium is a label on the associative carrier, not the operating algebra (Jacobi). Bare color-name labels remain a vacuous convention.",
  "class": "internal gauge-carrier / color-sector structural input",
  "minimum_decomposition": [
    "composition_algebra_hypothesis",
    "oriented_T_odd_grading",
    "carrier_vs_label_realization_bridge"
  ],
  "no_go_portfolio": [
    "color_su3_matter_realization_residual_map_2026-06-05",
    "g2_bridge_c3_current_cannot_beat_gap_a_no_go_note_2026-06-06",
    "cl3_su3_symmetric_base_commutant_gell_mann_embedding_narrow_theorem_note_2026-05-27"
  ]
}
```

If approved, `genuine_admitted_input_count` moves 2 → 3 and
`canonical_ids` gains `color_composition_carrier_admission`.

## 7. Governance

Per the framework's separation of duties, this note is a **proposal**. The
session does not register Tier-A admissions, set audit status, or record
minimality-policy approval. Owner approval (recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md`) and the audit-lane registry edit are
the steps that would make `COMP` a registered Tier-A admission able to
chain-satisfy downstream rows.

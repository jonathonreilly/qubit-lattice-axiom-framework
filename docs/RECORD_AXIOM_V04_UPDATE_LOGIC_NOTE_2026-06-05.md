# Record Axiom v0.4 — Update Language and Logic (for review)

**Date:** 2026-06-05
**Type:** meta / axiom-update logic note
**Claim type:** meta
**Status authority:** independent audit lane only. This note states the logic
behind an **owner-approved Section 6** update to the Record axiom. It sets no
audit status and promotes no downstream row. Owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6 (entry 2026-06-05).
**Primary runner:** `scripts/record_axiom_v04_update_verifier_2026_06_05.py`
(SUMMARY: PASS/FAIL recorded in the cached log).
**New axiom memo:** `docs/MINIMAL_AXIOMS_2026-06-05.md` (supersedes
`MINIMAL_AXIOMS_2026-06-04.md`).

> **Frame statement, binding on the whole note.** This update does **not** force
> the charged-lepton Brannen modulus `r=1/2`. The goal is to make `r=1/2` a
> *stable, distinguished setting on a derived dial* where the charged-lepton
> sector sits — not forced, not exclusive. Any claim of universal `r=1/2`
> selection would be an overreach (it is falsified by the quark and neutrino
> Koide values) and is explicitly disclaimed throughout.

## 1. What changes, and why

The 2026-06-04 Record axiom stated finite scalar record additivity **only**,
and explicitly excluded "record production, persistence, measurement, ...,
time arrow, ...". The v0.4 update adds two clauses to the *content* of a record:

- a record is the **irreversible registration of which** sector is realized
  (clauses (a) irreversible-registration and (b) which-sector);
- the recorded alternatives are **real** (CPT-even) (clause (c)).

Additivity (clause (d)) is unchanged.

**Why update rather than keep additivity-only.** Additivity alone is silent on
*what a record is of*. The pressure-test arc (Section 6) established that the
genuinely new, framework-relevant content — the location of the
classical/quantum cut, and the structure of the generation measure dial —
follows from *what a record registers* (which real superselection sector), not
from additivity. The update makes that content explicit and auditable instead of
leaving it implicit and scattered across conditional notes.

**Governance.** Section 1 of the minimality policy forbids a *lane worker* from
rewording an `A_min` axiom to be more permissive. This update is **not** that:
it is an explicit **owner-approved Section 6 amendment**, recorded in the policy
and offered to the review-loop for language/logic review. The audit lane retains
sole authority over the `minimal_axioms` registry pointer and all downstream
status.

## 2. Constitutive vs assumed (the honest breakdown)

| Clause | Status | Justification |
|---|---|---|
| (a) irreversible | **constitutive** | A structure that can unform is not a record; persistence is part of the meaning of "record". |
| (b) registers *which* sector | **constitutive** | A record *of* something registers which alternative obtained; "which" is the record's content. |
| (b′) sector = center | **derived** | The frozen / classically-readable structure is the center of the local algebra (T2; `center(M_n)=scalars`, verified). |
| (c) real (CPT-even) | **assumed — the one adjective** | Classical = real is a stance, not forced; a `K`-odd record is logically consistent. This is the single assumed import, equal to the K-reality choice already named on the ledger. |
| (d) additive | unchanged | The 2026-06-04 premise. |

The update therefore introduces **exactly one new assumption** — clause (c),
reality — which is the already-named K-reality stance. Everything else is either
constitutive of recordhood or derived.

## 3. The three theorems (consequences, not axioms)

These are downstream of the axiom and are stated here, with honest status, so the
review-loop can see what the update buys. They are **not** part of the axiom
statement.

### T1 — time-ordering (partial)

Irreversibility (a) orients record-formation into an order; the formation order
is a direction. **Honest status: TOUCHES-CONSTRAINS.** It supplies the
*direction*, not a time metric, and does not supersede the existing
emergent-time line. Not load-bearing for the rest of this note.

### T2 — the classical/quantum cut (the genuine new content)

The recordable/frozen structure is exactly the **real Wedderburn center** of the
local algebra. Within-block (simple-factor interior) structure has center =
scalars, so it carries no finer recordable label: it is reversible/quantum and
unrecorded. **Honest status: DERIVED** (modulo clause (c), reality). The cut —
the location of the measurement boundary — is normally inserted by hand; here it
is the content of "a record registers which real superselection sector".

For the generation algebra `R[Z_3] = R (singlet) ⊕ C (doublet)`, reality fixes
**2** real blocks (vs `C[Z_3]=C^3`, 3 complex idempotents). The 2-block partition
is the recorded structure.

### T3 — the measure dial (where `r=1/2` lives, as a setting)

On the recorded 2-block partition, weighting the blocks by `dim^s` gives a
closed-form dial:

```
r(s) = 2^(s-1),     Q(s) = 1/3 + (2/3) r(s)
```

with two symmetry-distinguished settings:

- **`s=0` → `r=1/2` → `Q=2/3`**: block-count / equipartition. The **symmetric**
  setting (each real block weighted as one record; partition-only). This is the
  setting the charged-lepton sector occupies.
- **`s=1` → `r=1` → `Q=1`**: Born / dimension (each block weighted by its
  within-sector dimension). The framework **default** setting.

**Honest status: the dial structure is DERIVED; the per-sector occupancy `s` is
a standing input.** The axiom (via T2) supplies the partition and the two
distinguished settings; it does **not** supply which `s` a given sector takes.

## 4. The non-overreach guard (binding)

`r=1/2` is **not forced** by this axiom, in three independent senses, each
checked by the runner:

1. **It is one setting of a multi-valued dial.** `r(s)=2^(s-1)` is a continuum
   with `r=1/2` at `s=0` and `r=1` at `s=1`. The observed sectors sit at a
   *spread* of `s` (neutrinos `s<0`, charged leptons `s=0`, down quarks `s≈0.26`,
   up quarks `s≈0.63` — observational comparison only). A universal-`s` rule
   (all sectors at `r=1/2`) is **falsified** by that spread.
2. **The record default is `r=1`, not `r=1/2`.** The Born/dimension reading
   (`s=1`) is the within-sector-aware measure available to the record; `r=1/2`
   is the partition-only deviation. The axiom does not privilege `r=1/2` over
   `r=1`.
3. **`r=1/2` is distinguished by symmetry, not selected by the axiom.** It is
   the unique fixed point of the block-swap symmetry on the dial and the concave
   maximum of the 2-sector entropy — a *distinguished* point, occupied by the
   charged-lepton sector, not an axiom output.

The win is precisely: **`r=1/2` is a stable, symmetry-distinguished setting on a
derived dial; the charged-lepton sector occupies it; the framework derives the
dial and its settings but not the per-sector occupancy.**

## 5. What this update does NOT close

- **Per-sector dial occupancy `s`** (which setting each sector takes). Direction
  is structural (colorless → `s=0`; colored → `s>0`); magnitude is the standing
  Yukawa-texture / color-generation-bridge input.
- **Generation-factor chirality.** A Hermitian, off-block (`C_3`-orbit-splitting)
  grading. It is **orthogonal** to the dial (it commutes with the holomorphy /
  block structure), so the dial does not supply it and it does not affect the
  dial value.
- **Internal color SU(3) identification**, theta, `AC_phi_lambda` value, P2/
  modulus, log-det, source/action, Born within-sector weights, record-production
  dynamics, time metric, normalization/scale.

## 6. Provenance (how the content was localized)

The update is the distillate of a ~20-attack pressure-test series, each landed as
a meta note + runner on its own branch:

- **Holomorphy is not forced (Q1, four angles).** Reading the complex doublet by
  its division algebra (`det_C`, `r=1/2`) is *not* forced — restriction of
  scalars makes `det_R` (`r=1`) equally canonical; the "real" adjective, read
  literally, favors `det_R`. So `r=1/2` is not an algebraic forcing.
- **Holomorphy ⟂ chirality.** The holomorphy structure commutes with the
  chirality grading; they are two gates, not one.
- **Einselection fixes the partition, not the value.** The pointer map is a
  no-op on `r`; the `{r=0,1/2,1}` discreteness lives on the *measure* axis, not
  the pointer-basis axis. (Hostile-confirmed.)
- **Measure-from-the-cut: two settings, not a forcing.** The cut makes
  block-count the partition-only measure (`r=1/2`) and Born the within-sector
  measure (`r=1`); a hostile pass confirmed the record can also reach `r=1`
  (block dimension is a single-copy structural fact, and Darwinian redundancy
  reconstructs it), so `r=1/2` is the symmetric setting, **not forced**. This is
  the desired outcome under the frame.
- **The dial `r(s)=2^(s-1)` is derived; the sector spread is multi-lane,
  no overreach.**

Each of these is consistent with the retained ledger anchors
(`koide_frobenius_isotype_split_uniqueness` retained_no_go: weight ratio free;
`koide_z3_equivariant_anticommuting_no_go` retained_bounded). The v0.4 axiom
encodes the *positive* residue of that series — the cut and the dial — without
re-asserting any forcing the series ruled out.

## 7. What the review-loop is asked to evaluate

1. The **language** of the v0.4 Record axiom in `MINIMAL_AXIOMS_2026-06-05.md`
   (clauses (a)-(d); the scope of what it supplies / does not supply).
2. The **constitutive-vs-assumed** classification (Section 2) — in particular
   that reality (c) is the single assumed adjective.
3. The **honest status** of T1/T2/T3 (Section 3) and the **non-overreach guard**
   (Section 4).
4. That the update is correctly framed as an **owner-approved Section 6
   amendment**, not a lane-internal rewording, and that nothing here promotes or
   re-statuses a downstream row.

This note adopts no import beyond clause (c) (the named K-reality stance), claims
no closed gate, and sets no audit status.

# P1 I_S Revision Verification Note (Critical Review of the 3x Upward Revision Claim)

**Date:** 2026-04-17
**Status:** support - critical-review verification layer on top of the prior P1 citation note
(`docs/YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md`).
**Verdict (up front, Abstract §0):** this row verifies conditional arithmetic only.
The historical `1.92%` is reproduced under the separate `I_S = 2` convention, and
the supplied `I_S ∈ [4, 10]` bracket maps conditionally to
`P1 ∈ [3.85%, 9.62%]`. The row does not determine whether those two inputs describe
the same, additive, or superseding physical contribution.
**Runner:** `scripts/frontier_yt_p1_i_s_revision_verification.py`
**Log:** `logs/retained/yt_p1_i_s_revision_verification_2026-04-17.log`

> **2026-07-16 scope correction.** The current UV coefficient bridge does not
> contain or authorize the historical `delta_PT`, NLO, source-action, or
> canonical-`alpha_LM` prose previously cited by this note. Throughout the
> legacy discussion below, “continuum vertex-correction magnitude” is only a
> historical label for the conditional arithmetic
> `alpha_LM · C_F/(2 pi) = (alpha_LM/(4 pi)) · C_F · 2`. This row proves that
> arithmetic identity only. The identification `I_S = 2`, its source-action
> meaning, and any NLO matching interpretation remain open. Every numerical use
> of `alpha_LM` below is conditional arithmetic/provenance from the linked
> unaudited certificate, not retained physical/canonical authority. The
> same, additive, or superseding physical contribution remains open; this row
> does not select a physical relationship between the two inputs.

The historical `delta_PT` remains conditional arithmetic under the separate
historical `I_S = 2` convention.

---

## Authority notice

This note is a **verification / critical-review** layer. It does **not** modify:

- the master obstruction theorem (referenced in the prior citation note as
  `docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md`);
- the retained Ward-identity theorem
  (`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`), which is an exact tree-level
  algebraic identity with no precision claim attached;
- the historical packaged `delta_PT = 1.92%` comparator, which remains only
  conditional arithmetic under `I_S = 2`; no current source-action or
  continuum-vertex authority is claimed;
- the prior citation note
  `docs/YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md`, whose literature-
  bracket reading of `I_S ∈ [4, 10]` is internally consistent;
- the prior symbolic reduction
  `scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py` (21/21 PASS), whose
  structural result `I_1 = I_S` on the retained conserved-current surface is
  unchanged by this note.

What this note adds is narrower: a deterministic arithmetic comparison between
the historical `I_S = 2` convention and the supplied `[4, 10]` bracket. The
arithmetic factor-three relation is verified, while source-action, NLO,
operator-transfer, Ward-cancellation, and same/additive/superseding semantics
remain open.

---

## Abstract (§0 Verdict)

**Arithmetic disposition:** under the conditionally supplied
`alpha_LM = 0.09066784`,

```
    historical delta_PT(I_S = 2)   = 1.924%
    conditional map at I_S = 6     = 5.772%
    conditional map, I_S in [4,10] = [3.848%, 9.620%].
```

The historical expression is conditional arithmetic under the separate
historical `I_S = 2` convention and is not a lattice BZ result. The supplied
bracket is external conditional provenance for a nearby lattice operator/scheme.
The exact operator/scheme transfer remains open. The Ward-cancellation gate
remains open. No source-action, NLO, additive, superseding, or physical-selector
conclusion follows from the displayed arithmetic.

---

## 1. Retained foundations

This note inherits without modification:

- `C_F = 4/3`, `C_A = 3`, `T_F = 1/2` at `SU(3)` (D7 + S1);
- Conditional canonical arithmetic `⟨P⟩ = 0.5934`, `u_0 = 0.87768`,
  `α_LM = 0.09067`, `α_LM / (4π) = 0.00721` (from
  `scripts/canonical_plaquette_surface.py`; not a retained physical/canonical
  input in this row);
- Color-tensor decomposition `Δ_R = C_F · I_1 + C_A · I_2 + T_F n_f · I_3`
  (from the prior color-factor reduction, referenced by the citation note);
- Ward-identity tree-level identity `y_t_bare = g_bare / √6` from
  `docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md` (exact algebraic, no NLO claim);
- Conserved-current reduction `I_V = 0` on the retained staggered
  point-split current surface, hence `I_1 = I_S` (from
  `scripts/frontier_yt_p1_i1_lattice_pt_symbolic.py`, 21/21 PASS).

---

## 2. Reconstruction of the packaged `1.92%`

### 2.1 Conditional arithmetic, not current source authority

The canonical arithmetic certificate
[`CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md`](CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md)
records the displayed `alpha_LM` arithmetic only. Its current ledger row is
unaudited, so it is not retained authority for the physical/canonical choice.
Under the separate historical
convention `I_S = 2`, one obtains:

```
    C_F = (N_c^2 - 1) / (2 N_c) = 4/3
    delta_PT_historical = alpha_LM * C_F / (2 pi) = 1.92%
                        = (alpha_LM/(4 pi)) * C_F * 2
```

The equality is arithmetic. No current authority cited by this row derives
`I_S = 2` from the staggered source action, identifies the expression as the
governing NLO vertex correction, or promotes it to a precision claim.

### 2.2 What the packaged value is NOT

The packaged `delta_PT` is **not**:

- a lattice-to-MSbar BZ integral for any specific operator (no BZ domain is
  specified, no specific propagators are integrated);
- the matching coefficient of the lattice scalar density `ψ̄ ψ` (not an operator-
  specific quantity at all);
- the `C_F · I_S` term of the retained decomposition `Δ_R = C_F · I_1 + …`
  (`I_S` is a specific lattice BZ integral over staggered fermion and Wilson
  gluon propagators; the packaged `δ_PT` is not of this form).

It is only the displayed conditional arithmetic evaluated with the supplied
`α_LM` number. The historical “continuum vertex-correction” wording is a label,
not source-action or NLO authority.

### 2.3 Algebraic identity in `α/(4π)` convention

As a *consequence* of the standard vertex-correction formula
`α · C_F / (2π) = (α / (4π)) · C_F · 2`, one can algebraically rewrite:

```
    delta_PT  =  α_LM · C_F / (2π)  =  (α_LM / (4π)) · C_F · 2
```

The `2` on the right-hand side is a **conversion factor**, not a claimed BZ
integral value. The citation note (§1.6) reads this `2` as if it were
`I_S_standard = 2`. This reading is only correct if one asserts that the
packaged `δ_PT` is already in the form `(α/(4π)) · C_F · I_S` with some `I_S`
value. It isn't — the packaged `δ_PT` is in the form `(α / (2π)) · C_F`, and
the numerical coincidence with `(α / (4π)) · C_F · 2` is a trivial convention
identity that doesn't imply `δ_PT` is a BZ integration output.

**Conclusion of §2:** the packaged `1.92%` is conditional arithmetic under the
separate historical `I_S = 2` convention, not a lattice BZ result. The
arithmetic alone does not identify its source action or matching role.

---

## 3. Reconstruction of the cited `I_S ≈ 6`

### 3.1 Literal definition (from the prior citation note §2.1)

```
    Z_S^{lat → MSbar}(μ = 1/a)
        =  1  +  (α_s · C_F / (4π)) · I_S(β, tadpole_improvement, operator_form)
        +  O(α_s^2)
```

with `I_S` a pure BZ integral over the lattice Feynman rules (staggered
fermion propagator `D_ψ(k) = Σ sin²(k_μ a) / a²` and Wilson gluon propagator
`D_g(k) = (4/a²) Σ sin²(k_ρ a/2)`), evaluated specifically for the scalar
bilinear `ψ̄ ψ` on the 1-link staggered lattice.

This is an **operator-specific BZ integration**. The BZ domain is
`[-π/a, π/a]^4`, the propagators are the retained lattice Feynman rules, the
operator is the scalar density with `H_unit = (1/√6) Σ ψ̄ψ` normalization, and
the scheme is MSbar at `μ = 1/a` after subtracting the logarithmic divergence.

### 3.2 Literature values

The staggered lattice-QCD literature evaluates `I_S` (or the corresponding
named matching coefficient in various conventions) for the tadpole-improved
staggered scalar density on Wilson plaquette gauge action. The cited range is:

| Convention / scheme                         | `I_S` range        | Representative citations                     |
|---------------------------------------------|---------------------|-----------------------------------------------|
| Un-improved Wilson + staggered scalar       | `[10, 20]`          | Kilcup–Sharpe 1987, Sharpe 1994              |
| Tadpole-improved Wilson + 1-link staggered  | `[4, 10]`           | Bhattacharya–Sharpe 1998, BGKS 1999          |
| Historical arithmetic convention            | `2`                 | conditional reference point only              |

The tadpole-improved bracket `I_S ∈ [4, 10]` with literature-cluster central
`~6` is supplied external provenance from the citation note (§2.2–2.4), not
retained authority in this row.

### 3.3 What the cited `I_S` is NOT

The cited `I_S ≈ 6` is **not**:

- a framework-native derivation on the `Cl(3) × Z^3` canonical action — it is
  a lattice-QCD literature value for the *closest* analogue
  (tadpole-improved staggered scalar density at `β ≃ 6`), with explicit `O(1)`
  citation uncertainty per the prior note §2.4;
- evidence that the historical `I_S = 2` arithmetic and this supplied bracket
  are the same, additive, or superseding physical contributions;
- the full `Δ_R` — it is only the `C_F · I_1 = C_F · I_S` piece, with `C_A · I_2`
  and `T_F n_f · I_3` pieces still OPEN (citation note §7).

### 3.4 Transfer boundary

The cited operator, action, and scheme are nearby comparators, not the exact
framework source action. The exact operator/scheme transfer remains open.
Consequently the supplied bracket may be used only in the conditional arithmetic
map; it cannot by itself select the governing physical correction.

---

## 4. Comparison analysis: arithmetic only

The exact normalization identity is

```
    α / (2π) = 2 α / (4π).
```

Therefore the historical expression can be rewritten with a numerical factor
`2`, while the supplied bracket maps to factors in `[4, 10]`. This proves the
factor-three central arithmetic comparison. It does not decide whether the
historical expression and the supplied bracket are the same physical quantity,
different physical quantities, additive contributions, or alternative
descriptions. That selector requires source-action and operator-matching input
not supplied here.

### 4.1 Ward-cancellation gate

The Ward-identity theorem (Steps 3A–3E of
`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`) derives `y_t_bare = g_bare / √6`
as an exact **tree-level** algebraic identity in Representations A (direct
OGE computation) and B (direct matrix-element of `H_unit`). At 1-loop,
Representations A and B pick up independent loop corrections. The **ratio**
`y_t(M_Pl) / g_s(M_Pl) = 1/√6` is preserved only if the 1-loop corrections
CANCEL between the two representations.

The cited `I_S` enters Representation B (H_unit scalar-density matching on
the lattice). Representation A has its own 1-loop correction (OGE box
diagrams, gluon self-energy, etc.). In principle, the 1-loop corrections on
both sides could partially cancel, and the **net effect** on
`y_t(M_Pl) / g_s(M_Pl)` could be smaller than the `I_S` correction alone.

This is NOT established here. Neither the prior citation note nor this
verification note attempts a full 1-loop closure of both representations of
the Ward identity. The honest statement is:

> The supplied `I_S` bracket enters only the conditional Representation-B
> arithmetic map. The net effect on the Ward ratio depends on the independent
> Representation-A correction. The Ward-cancellation gate remains open, so
> no net P1 correction follows from this row.

This is a further caveat on top of the `O(1)` citation uncertainty.

---

## 5. Dimensional analysis cross-check

### 5.1 Packaged value

```
    delta_PT  =  α_LM · C_F / (2π)
              =  0.09066784 × (4/3) / (2π)
              =  0.01924
              =  1.9240 %
```

### 5.2 Cited interpretation (α/(4π) convention)

```
    P1(I_S)  =  (α_LM / (4π)) · C_F · I_S
             =  0.00721473 × (4/3) × I_S
             =  0.00961964 × I_S

    I_S = 2   :   P1 = 0.01924 = 1.92 %     (= packaged by convention identity)
    I_S = 4   :   P1 = 0.03848 = 3.85 %
    I_S = 6   :   P1 = 0.05772 = 5.77 %     (central cited)
    I_S = 8   :   P1 = 0.07696 = 7.70 %
    I_S = 10  :   P1 = 0.09620 = 9.62 %
```

### 5.3 Convention identity check

```
    α / (2π)  =  2 · α / (4π)
    α · C_F / (2π)  =  (α / (4π)) · C_F · 2
```

This identity is exact; both sides evaluate conditionally to `0.01924` with the
supplied `alpha_LM` arithmetic.
The "2" is a convention factor, not an `I_S` value in any physical sense.

### 5.4 Scope of the numerical comparison

The displayed expressions are dimensionless arithmetic. Their ratio is exactly
`3.0` at `I_S = 6` versus the historical `I_S = 2` convention. This numerical
comparison does not select a physical relationship between the two inputs.

---

## 6. Arithmetic-only disposition

Under the supplied inputs:

```
    historical delta_PT, I_S = 2  = 1.924%
    conditional central, I_S = 6  = 5.772%
    conditional range, I_S ∈ [4,10] = [3.848%, 9.620%].
```

The supplied bracket is external and has `O(1)` citation uncertainty. The
historical arithmetic has no independently supplied source-action or NLO
interpretation. Their same/additive/superseding relationship remains open.
The Ward-cancellation gate, exact operator/scheme transfer, `C_A` channel,
`T_F n_f` channel, and publication propagation all remain open.

---

## 7. Safe claim boundary

This note claims only the conditional arithmetic statements:

> With conditionally supplied `alpha_LM = 0.09066784`, the separate historical
> convention `I_S = 2` gives `1.924%`, while the supplied bracket
> `I_S ∈ [4, 10]` maps to `[3.848%, 9.620%]` with central `5.772%`.
> The historical value is not a lattice BZ result, and the arithmetic does not
> select a physical relationship between the two inputs.

It does **not** claim:

- that the conditional P1 map is framework-native (the cited `I_S` is external
  literature);
- that `I_S ≈ 6` is precise to better than `O(1)` (cited uncertainty remains);
- that the net 1-loop correction to `y_t(M_Pl) / g_s(M_Pl)` equals the
  conditional `5.77%` map (the Representation-A vs Representation-B
  cancellation at 1-loop is not established);
- that the historical and supplied inputs are the same, additive, or
  superseding physical contributions;
- that the master obstruction theorem or any publication-surface file should
  be modified on the basis of this verification note;
- that the `C_A` (`I_2`) or `T_F n_f` (`I_3`) channels of `Δ_R` are closed;
  they remain OPEN.

---

## 8. What is retained vs. cited vs. open

**Retained (framework-native, unchanged by this note):**

- `SU(3)` Casimirs `C_F = 4/3`, `C_A = 3`, `T_F = 1/2`.
- Color-tensor decomposition `Δ_R = C_F · I_1 + C_A · I_2 + T_F n_f · I_3`.
- Conserved-current reduction `I_1 = I_S` on the retained staggered surface.
- Ward-identity tree-level exact identity `y_t_bare = g_bare / √6` (no NLO
  claim attached).

**Conditional arithmetic/provenance (not retained physical/canonical authority):**

- `α_LM = 0.0907` and `α_LM/(4π) = 0.00721` from the unaudited bounded
  certificate.
- Historical `δ_PT = α_LM · C_F / (2π) = 1.924%` under the separate
  `I_S = 2` convention; not a lattice BZ result.

**Cited (external lattice-QCD literature, with `O(1)` uncertainty):**

- Tadpole-improved staggered scalar-density BZ matching coefficient
  `I_S ∈ [4, 10]` in the `α/(4π)` convention, central `~6`, as conditional
  comparison provenance.

**Open (not closed by this note or the prior citation note):**

- Framework-native 1-loop BZ evaluation of `I_S` on the retained
  `Cl(3) × Z^3` canonical action.
- Representation-A vs Representation-B cancellation at 1-loop on the Ward
  ratio `y_t(M_Pl) / g_s(M_Pl)` (the cited `I_S` may overcount the net
  effect on the ratio).
- `C_A` channel (`I_2`) and `T_F n_f` channel (`I_3`) of `Δ_R`.
- The exact operator/scheme transfer remains open.
- The same, additive, or superseding relationship between the historical
  arithmetic and supplied bracket remains open.
- Propagation of the conditional P1 map into any publication-surface table; no
  publication-surface file is modified by this note.

---

## 9. Validation

The runner `scripts/frontier_yt_p1_i_s_revision_verification.py` emits
deterministic PASS/FAIL lines and is logged under
`logs/retained/yt_p1_i_s_revision_verification_2026-04-17.log`. The runner
must return PASS on every check to keep this note on the retained surface.

The runner verifies:

- exact reproduction of the historical
  `δ_PT = α_LM · C_F / (2π) = 1.924%` under `I_S = 2`;
- convention identity `α/(2π) = 2 · α/(4π)` giving the algebraic form
  `(α/(4π)) · C_F · 2` — identifying the "2" as a convention factor, not a
  BZ integral value;
- conditional arithmetic at `I_S ∈ {2, 4, 6, 8, 10}`;
- the source firewall against stale UV-bridge attribution, retained-alpha
  wording, and unsupported semantic selectors;
- explicit open source-action, NLO, Ward-cancellation, operator-transfer,
  same/additive/superseding, and publication-propagation gates.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [yt_p1_i_s_lattice_pt_citation_note_2026-04-17](YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md)
- [yt_ward_identity_derivation_theorem](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
- `yt_uv_to_ir_transport_obstruction_theorem_note_2026-04-17`
  (master upstream authority; backticked to avoid length-3 cycle through
  yt_p1_rep_a_rep_b_cancellation_theorem — citation graph direction is
  *obstruction → rep_a_rep_b → this_revision_verification*)

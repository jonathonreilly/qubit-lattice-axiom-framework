# block02 — Section: SK-1 — derive B-AXIS N2b (`2 a_tau`) from
`scale_reference × kinetic_isotropy` (no-new-axiom crack attempt)

**Lane:** axiom-update-proposals, branch
`physics-loop/axiom-update-proposals-block02-20260620`.
**Target:** the no-new-axiom CRACK flagged SK-1 in
`docs/AXIOM_UPDATE_PROPOSALS_CONSOLIDATED_2026-06-20.md` §3 and
`.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md` §E:
derive B-AXIS **N2b** — the absolute blocked time-step `2 a_tau`, the Stone
generator unit — from the two ALREADY-APPROVED primitives
`scale_reference_primitive` (`a^{-1} = M_Pl`, fixes the absolute edge length)
and `kinetic_isotropy_primitive` (`c_t = c_s`, OS0 kinetic-form isotropy),
**without any new axiom or primitive**.
**Posture:** OWNER-authorized "don't believe the no-gos." A genuine crack here is
the highest-value outcome (it would retire candidate N2b entirely). I attacked
HARDER than the prior block's spacing-ratio route and report the result honestly.

**Deliverables**
- Runner: `scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py`
- Runner cache: `logs/runner-cache/sk1_baxis_n2b_kinform_scale_join_2026_06_20.txt`
  — **TOTAL: PASS=28 FAIL=0** (sympy + numpy; deterministic; no RNG in any
  load-bearing leg; clean under `python3 -W error`; no empirical import).

---

## 1. The target N2b and the prior wall

The Stone generator of the 2-step blocked staggered transfer
(`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28`) is

```text
    H_hat = - log( T_hat^2 ) / ( 2 a_tau ),     T_hat^2 = T_odd . T_even.
```

**N2b is the absolute value of the denominator `2 a_tau`** (the dimensionful
tick). `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` §"`T` alone does not
fix the clock unit" proves a fixed positive transfer `T` fixes only the
**product** `tau·H`, never `tau` alone (runner W2: the same `T` reconstructs for
`tau = 1, 2, 0.7` with `H ∝ 1/tau`). So `T` by itself cannot pin `2 a_tau`; N2b
is a genuine open clock-unit datum.

**Prior block (the route I had to beat).** The single-clock B-axis reassessment
route `R-KINFORM-N2b` tried the **spacing-ratio identity** `c_t / c_s =
a_tau / a_s`. The kinetic-isotropy NOTE **disavows** that identity: it grants
only kinetic-FORM isotropy, not the spacing ratio. That route walled. (The
exact `…2026-06-20` reassessment note / `single_clock_kinform_spacing_bridge_n2b`
script named in the task prompt do not exist in this checkout — verified by
`find`; the disavowal they rest on is the verbatim text of the landed
`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09`, quoted below.)

**The SK-1 push (different claim).** Do not use a spacing-ratio identity. Instead
ask whether `kinetic_isotropy`'s **"one tick is one edge in FORM"** + the
absolute edge length `a` from `scale_reference` **JOINTLY** pin `2 a_tau` by
treating the time edge as the **SAME edge object** as the space edge — so that
`a_tau = a` follows directly, with no separate spacing ratio invoked.

---

## 2. What the runner builds (functional-calculus-correct)

`scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py`, six blocks:

**Block A — construct `Q(p)` from the staggered action with EXPLICIT,
INDEPENDENT edges `a_tau`, `a_s` (sympy).** Restoring one `1/a` per lattice
difference, the dimensionful inverse propagator is
`G = (1/a_tau^2)(2-2 cos(a_tau ω)) + (1/a_s^2) sin^2(a_s k) + (m/a_tau)^2`. Its
small-momentum expansion gives the continuum kinetic FORM
`Q = c_t ω^2 + c_s k^2 + …` with **`c_t = 1`, `c_s = 1`** (A1, A2), mass term
`(m/a_tau)^2` (A3). The decisive computed fact (A4): the **form ratio
`c_t/c_s = 1` is a dimensionless pure number with `a_tau`, `a_s` ABSORBED into
the physical `ω, k`** — `free_symbols = []`. The OS0 isotropy condition
`c_t = c_s` therefore lives entirely in the dimensionless `(c_t,c_s)` plane.

**Block B — decisive disavowal test.** `c_t/c_s = 1` is verified to hold at a
**continuum** of temporal edges `a_tau ∈ {1/3, 1, 7/2, 10}` (a_s fixed) — all
ratios `= 1` (B1, B2). So kinetic-isotropy is a **single point**, satisfied for
EVERY `a_tau`; it cannot select one. By contrast the **spacing** condition
`a_tau/a_s = 1` is a *distinct* equation that selects exactly one `a_tau` (B3),
and the two are provably **different functions**: form ratio `≡ 1` (constant)
vs spacing ratio `a_tau/a_s` (varies with `a_tau`) (B4).

**Block C — the "same edge object" push, head-on.** "One tick is one edge in
FORM" = the temporal hop is **range-1 in time edges** (leg count 1), exactly as
the spatial hop is range-1 in space edges (leg count 1). This form-leg equality
`1 == 1` is **already satisfied with no metric input** (C1–C3). Crucially, the
range-1 **adjacency topology is identical** for `a_tau = a_s` and for
`a_tau = 10 a_s` — only the metric weight differs (C4, explicit NN adjacency
matrices). Hence "treating the time edge as the SAME FORM object" is true for
**every** `a_tau`; it does **not** force `a_tau = a_s` (C5). C6 makes the gap
explicit: the join `{scale_reference} × {kinetic_isotropy}` supplies
`{absolute anchor a^{-1}}` and `{form ratio c_t/c_s = 1}`, but **NOT** the
dimensionless spacing ratio `a_tau/a_s` — the exact object N2b needs.

**Block D — the `2 a_tau` denominator dissected.** The factor **2** is the
staggered **2-step block count**: the single-step transfer is non-positive
(D1, `min|Im eig| = 0.375` over the BZ — reproduces the no-go), so the physical
positive object is `T_hat^2 = T_odd·T_even` over **two** temporal edges; its
eigenvalues are `exp(±2E(p))` with `E = arcsinh√(m²+sin²p)` exactly (D2,
residual `5e-15`). So `2` is a **counted structural integer (derivable, no
axiom)**; `a_tau` is the metric edge multiplying it. D4 is the
functional-calculus-correct restatement of scope-boundary N2: for **every**
`a_tau`, `H_hat = -log(T²)/(2 a_tau)` reconstructs the *same* `T²` (log acts on
the positive spectrum), so the transfer fixes only `2 a_tau · H_hat`, never
`a_tau`.

**Block E — primitive disavowal ledger (verbatim).** Block F — verdict logic.

---

## 3. DECISIVE disavowal check (verbatim quotes)

> **`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09` grants vs disavows:**
> GRANTS: "the matter kinetic normalization is space-time isotropic, `c_t = c_s`
> … One tick is one edge in **form**, not only in spacing." "this primitive
> fixes only the one **dimensionless** graining ratio relating that emergent time
> to space."
> DISAVOWS (the SK-1 object): "It carries no dimensionless dynamical content";
> "the **absolute** scale belongs to the single approved scale-reference
> primitive"; "any **spacing** ratio or reachability claim lives in its **own
> derivation row**"; "It does not supply the absolute scale
> (`scale_reference_primitive`) or the **spacing ratio (derived from the
> no-diagonal clause)**; it supplies only the kinetic-**form** isotropy."

> **`SCALE_REFERENCE_PRIMITIVE_NOTE` grants vs disavows:**
> GRANTS: one dimensionful anchor, `a^{-1} = M_Pl`.
> DISAVOWS: "It carries **zero dimensionless content**"; "does not assert
> `a/l_P = 1` as a derived theorem."

The note phrase "**one tick is one edge in form, not only in spacing**" is the
exact text the SK-1 push leans on — but read in context it **distinguishes** the
form claim (granted) from the spacing claim (the "not only in spacing" reserves
spacing as a *separate* matter, immediately confirmed by "any spacing ratio …
lives in its own derivation row" and names a **different supplier**, the
**no-diagonal clause**, for it). The form/spacing words are deliberately split,
not fused.

---

## 4. Verdict — WALL STANDS (SK-1 does not crack N2b)

A CRACK would require `scale × kinetic_isotropy ⇒ a_tau/a_s = 1` (hence
`2 a_tau = 2a`). The runner shows the only path to `a_tau/a_s = 1` from these
two is to read `kinetic_isotropy`'s **granted FORM ratio** (`c_t/c_s`, a constant
`1` independent of the edges) **AS** the **disavowed metric SPACING ratio**
(`a_tau/a_s`, which varies with `a_tau`). B4 proves these are different
functions; F1/F2 record that identifying them **mis-cites the primitive** — citing
it for content it explicitly reserves to another row. That is exactly the
laundering the axiom-premise **purity guard** (`check_axiom_premise_clean.py`)
and the no-laundering discipline of `AXIOM_MINIMALITY_POLICY.md` §6 forbid: a
primitive chain-satisfies **only for what it grants**, and `kinetic_isotropy`
grants FORM, not spacing.

**Therefore SK-1 does NOT crack N2b from the approved surface. The wall stands,
and the absolute clock unit `2 a_tau` still needs either a separate
spacing-row derivation (the "no-diagonal clause" the note names as the spacing
supplier — an untested no-axiom lead, see §6) or a primitive.** This is the
**honest** difference from the two genuinely over-strong B-AXIS no_gos that the
campaign DID correct (the axis-label N4-LABEL crack): here the primitive note
**explicitly** disavows the needed content, so a "crack" would be a mis-citation.

### What DID move forward (partial, no axiom)

1. **The factor 2 is structural, not axiomatic.** `2 a_tau = (2) × (a_tau)` with
   `2` = the staggered 2-step block count (D1–D3, derived in-repo, single-step
   non-positive ⇒ two edges per positive block). N2b's only **axiom-bearing**
   residual is the single metric length `a_tau`, **not** the whole `2 a_tau`.
2. **The form/spacing separation is now computed exactly** (A4, B1–B4, C4–C6):
   kinetic-isotropy is a dimensionless point true for all `a_tau`; the form leg
   count is metric-blind. This sharpens *why* the spacing is a distinct datum and
   blocks any future "form=spacing" re-attempt at the algebra level.

---

## 5. Consequence for the proposal set

- **N2b is NOT removed by SK-1** (contrary to the SK-1 flag's optimistic
  reading in `WALL_TO_GATE_MAP.md` §E / consolidated §3, which said `2 a_tau`
  "may be derivable" and "likely removes N2b"). The flag was a *candidate* crack
  with an explicit ACTION ("attempt to derive `2 a_tau` … **before** proposing");
  attempting it shows it does not land. The consolidated note's own "Not in
  scope … the dimensionful tick `2 a_tau`" and its repeated "does NOT grant …
  the dimensionful tick value `2 a_tau`" minimality clauses are **vindicated** —
  SK-1's optimistic headline should be downgraded to "walls; the factor 2 is
  structural, `a_tau` is the residual."
- **The residual clock-unit datum** (a single dimensionful temporal edge `a_tau`,
  equivalently the dimensionless `a_tau/a_s`) is the genuine N2b content. Its
  natural home is a **spacing-row derivation** from the no-diagonal clause (the
  supplier the kinetic-isotropy note names) — a no-axiom lead worth a dedicated
  block — **or**, if that walls, the weakest sufficient primitive is a single
  **time-edge spacing** datum (one dimensionless number `a_tau/a_s`), strictly
  weaker than the C1 RP-DYN dynamics axiom and disjoint from the FORM content
  `kinetic_isotropy` already supplies.
- RP-DYN (C1) deliberately proposes only the **dynamics-side existence** of a
  step (a rate `γ` / well-defined half-life), **never** the dimensionful value
  `2 a_tau` (consolidated §2.1 minimality). SK-1's wall confirms that division
  of labor: the dynamics-side tick (C1) and the metric clock unit (N2b/`a_tau`)
  are genuinely separate residuals.

---

## 6. Honest open lead (not claimed here)

The kinetic-isotropy note names the **no-diagonal clause** as the supplier of the
spacing ratio "derived from the no-diagonal clause." I did **not** attempt that
derivation in this block (it is outside the `scale × kinetic_isotropy` join SK-1
specifies, and would need the staggered/no-diagonal geometry as input). If the
no-diagonal clause forces `a_tau = a_s` as a *theorem* on the current surface,
that — not SK-1 — would be the no-axiom crack for N2b. Flag for a follow-up block:
**"derive `a_tau/a_s` from the no-diagonal clause (no axiom)."**

---

## 7. Status discipline / policy

- `hypothetical_axiom_status` is not invoked: this section reports a **wall**
  (no axiom proposed, no candidate adopted) plus a partial no-axiom structural
  result (the factor 2).
- No bare `retained` / `promoted`; no audit verdict set; nothing written to
  `docs/audit/data/` (read-only this lane); no `axiom_premise_nodes.json` edit.
- The independent audit lane / owner is the sole status authority.

## 8. One-line outcome

SK-1 **walls**: `kinetic_isotropy` grants the dimensionless kinetic-FORM ratio
`c_t/c_s = 1` (a single point, true for every `a_tau`) and `scale_reference`
carries zero dimensionless content, so their join supplies the absolute anchor
and the form ratio but **not** the spacing ratio `a_tau/a_s` the clock unit
needs — both notes explicitly reserve that spacing to its own derivation row, so
reading FORM as SPACING would mis-cite a primitive; the factor 2 in `2 a_tau` is
no-axiom structural while the metric edge `a_tau` is the residual that walls
(runner `PASS=28 FAIL=0`).

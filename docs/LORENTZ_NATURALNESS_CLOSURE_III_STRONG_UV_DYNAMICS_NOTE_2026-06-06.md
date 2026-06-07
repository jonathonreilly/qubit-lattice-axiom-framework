# Lorentz Naturalness Closure (iii): New Strong UV Dynamics — Characterized, and Why the Framework Does Not Supply It

**Date:** 2026-06-06
**Claim type:** no_go (characterization of the required new physics)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary declaration.
**Primary runner:**
[`scripts/frontier_lorentz_naturalness_closure_iii_strong_uv_dynamics_2026_06_06.py`](../scripts/frontier_lorentz_naturalness_closure_iii_strong_uv_dynamics_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_naturalness_closure_iii_strong_uv_dynamics_2026_06_06.txt`](../logs/runner-cache/frontier_lorentz_naturalness_closure_iii_strong_uv_dynamics_2026_06_06.txt)

---

## Role

This note pursues the **last non-trivial escape** of the Lorentz-naturalness
obstruction [`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
(#3123): **closure (iii) — new strong UV dynamics**, i.e. a strong UV fixed point
with anomalous dimension `γ ≳ γ_crit ~ 1` for the speed-difference operator, which
would power-law-suppress the regenerated marginal Lorentz violation
`(μ/M_Pl)^γ` below the experimental bounds. (Closure (i), a hidden carrier
symmetry, was excluded systematically [#3129]; Record was excluded [#3126]; closure
(ii) is to postulate `c_t=c_s`, a new axiom.)

The decisive question is sharp: **does the framework's own structure
({axioms} + the `β=6` SU(3) lattice) supply such a strong UV fixed point, or is it
genuinely new physics?** The answer (runner **14 PASS / 0 FAIL**, order-of-magnitude
scaling) is **new physics** — and, constructively, the note pins down *exactly* what
new dynamics is needed and shows the most "natural-sounding" framework candidate
(Lifshitz `z>1` scaling) is **not realized**.

## The argument

### (A) The framework's `β=6` is on the *weak* side of the strong-coupling radius
The framework's own `β=6` plaquette campaign established the strong-coupling radius
`R_SC ≈ 5.39` (d-log Padé on the certified `d₅..d₁₁`; the
`UV_YUKAWA_STRONG_COUPLING_DOMAIN_EXCLUSION` / `BETA6_PLAQUETTE…RADIUS` results).
Since `β = 6 > R_SC`, `β=6` lies **outside** the strong-coupling expansion's
convergence — on the **weak / scaling side**. The bare coupling is `g² = 2N/β = 1`,
`α_s(M_Pl) = g²/4π ≈ 0.08` (moderate-weak), giving `γ = c_γ α_s ~ 0.08–0.24` — far
below `γ_crit ~ 1` (the #3123 gap). **The native gauge dynamics does not supply
closure (iii).**

### (B) Closure (iii) needs a strong fixed point `α_s* ~ 0.3–1`
`γ ≳ 1` requires `α_s* ~ 1/c_γ ~ 0.3–1.0` — **4–12×** the framework's `β=6`
coupling. That is a strong UV completion the framework does not have.

### (C) The Lifshitz (`z>1`) route is *not native* — the lattice dispersion flattens
The framework is spatial-lattice + continuous-time, hence **inherently
anisotropic** — so a Lifshitz (`z>1`) UV that suppresses LV is the obvious
framework-native candidate. **It fails.** The lattice dispersion
`E² = Σ_i sin²(p_i a)/a²` has local exponent `z_eff = d\ln E/d\ln p` decreasing from
`1` (IR) toward `0` at the BZ edge — the dispersion **flattens** (`z<1`), the
**opposite** of the `z>1` steepening a Lifshitz LV-suppression needs. So the
framework is not Lifshitz-`z>1`; a `z>1` window would require **adding**
higher-spatial-derivative (`p^{2z}`) terms — new physics — and a `z>1` Lifshitz
fixed point carries its **own** naturalness problem (the relevant lower-derivative
operators must be tuned — the Hořava issue).

### (D) The candidate new-strong-UV routes and their costs
- **(a)** a new strongly-coupled gauge/matter sector with `γ~1` (the interacting-
  fixed-point isotropization of Bednik–Pujolàs–Sibiryakov) — new fields, and it must
  not re-introduce the LV;
- **(b)** `z>1` Lifshitz higher-derivative terms — changes the action; own
  naturalness problem;
- **(c)** the framework's **gravity** strongly coupled at the Planck/lattice scale
  (asymptotic-safety-like; Weinberg–Reuter). This is the **most framework-adjacent**
  route: the lattice scale *is* the Planck scale (`a⁻¹=M_Pl`), and gravity is
  generically strong there, so a non-Gaussian gravitational UV fixed point could
  supply the `γ~1`. But the framework's gravity is currently **IR-emergent**, not a
  **UV-dynamical** sector — making this genuinely new work.

## Verdict

**Closure (iii) requires new strong UV dynamics absent from `{axioms + β=6}`.**
Neither a strong gauge fixed point (β=6 is weak-side of `R_SC`) nor a `z>1` Lifshitz
window (the lattice flattens, not steepens) is native. The most natural new-physics
route is **strongly-coupled Planck-scale gravity (asymptotic-safety-like)** — the
constructive forward pointer — but it is new (UV-dynamical gravity) and unproven (it
must deliver `γ ≳ 1` *without* re-introducing the LV). Closure (iii) is **open and is
genuinely new physics**, consistent with the field-wide quantum-gravity status (no
lattice/QG approach has cleanly closed Lorentz naturalness; the framework is not
special).

## The complete 3-closure map (this completes the Lorentz arc)

| closure | status | where it lives |
|---|---|---|
| **(i)** hidden carrier symmetry | **excluded** (#3129) | the `c`-operator is a Lorentz scalar; only `t↔x` forbids it = the absent 4th lattice axis |
| **(ii)** admitted `c_t=c_s` axiom | a **new postulate** | the 4D-hypercubic / SO(4) direction the `Z³` axiom denies |
| **(iii)** new strong UV dynamics | **new physics, open** (this note) | a `γ≳1` strong fixed point; most natural = strong Planck-scale gravity |

**None lies within `{axioms + β=6}`.** Emergent Lorentz is structurally,
tree-level, and IR-flow sound; the interacting UV naturalness is the framework's
standing "couplings not forced" residual (the action-form no-go, per #3126) at a
second operator dimension; and closing it requires **either a new axiom (ii) or new
physics (iii)** — rigorously, nothing in the existing structure (Record, Quantum,
Lattice, the `β=6` dynamics) does it.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only that Lorentz naturalness
  needs structure beyond `{axioms + β=6}`.
- It does **not** propose or adopt a new axiom or new field; it **characterizes** the
  required new physics and identifies the most framework-adjacent candidate.
- It does **not** contradict #3123/#3126/#3129/#3121 or the tree-level dissolution.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** fitted/PDG input
  (`β=6 → g²=1` is the framework's own bare-coupling convention; `R_SC` is the
  framework's own result; the LV bounds and the QG literature are comparators). It
  does **not** set or change any audit status.

## No-go discipline (N1–N8 summary)

- **N1 routes:** strong gauge fixed point (β=6 weak — excluded native); `z>1`
  Lifshitz (lattice flattens — excluded native; own naturalness if added); new strong
  sector / strong Planck-gravity (new physics — the open route). **N2:** independent
  walls (the coupling strength A/B; the dispersion shape C). **N7 steelman:** the
  Lifshitz anisotropy is the strongest native-sounding candidate and it is refuted by
  the dispersion flattening (C). **N3/N5/N6:** premises explicit (`R_SC≈5.39`,
  `α_s≈0.08`, `z_eff→0`); "new physics required" means precisely "no `γ≳1` fixed point
  in `{axioms+β=6}`", not an inconsistency.

## Reprove-and-cite ledger

- **Reproven here** (runner): `β=6 > R_SC≈5.39` (weak side) and `α_s≈0.08`,
  `γ~0.08–0.24`; the `α_s*~0.3–1` (4–12×) strong-fixed-point requirement; the lattice
  `z_eff` flattening from 1 to 0 (refuting native Lifshitz-`z>1`).
- **Cited** (comparator/scope only): the framework's `R_SC` radius result (#2851 /
  the `β=6` radius-evidence note) and `γ` (#3123); Collins et al *PRL* 93 (2004)
  191301; Bednik–Pujolàs–Sibiryakov *JHEP* 1311 (2013) 064; Hořava (Lifshitz
  gravity) and the Hořava-LV naturalness literature (arXiv:1805.10299);
  Weinberg / Reuter (asymptotic safety) as the candidate strong-gravity UV.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- `NO_HIDDEN_CARRIER_SYMMETRY_FORBIDS_LORENTZ_MARGINAL_NO_GO_NOTE_2026-06-06.md` (closure (i), #3129; not yet on main — backticked)
- `RECORD_CANNOT_PROTECT_LORENTZ_MARGINAL_COUPLING_NO_GO_NOTE_2026-06-06.md` (the Record exclusion, #3126; not yet on main — backticked)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the framework's `β=6`
SU(3) lattice (g²=1) and its own strong-coupling radius `R_SC≈5.39`; (3) the staggered
lattice dispersion; (4) the #3123 `γ` and `γ_crit`. The result is an order-of-magnitude
scaling characterization of the required new physics.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (strong-coupling radius, anomalous dimension, fixed point,
Lifshitz/dynamical exponent `z`, asymptotic safety). No fitted/PDG/`g_bare` value
consumed as a derivation input; `β=6` and `R_SC` are the framework's own.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3123, #3126, #3129, #3121, or any upstream row. The audit lane is the only
status authority.

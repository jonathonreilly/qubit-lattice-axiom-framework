# Lorentz Naturalness: a Quantified Obstruction — the Asymptotically-Free Gauge Anomalous Dimension is Too Small to Suppress the Regenerated Marginal LV

**Date:** 2026-06-06
**Claim type:** no_go (quantified obstruction)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.py`](../scripts/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.txt`](../logs/runner-cache/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.txt)

---

## 2026-06-09 surface-scope update

The obstruction quantified below is computed on a **non-isotropic** surface
(continuous-time / anisotropic regulator, `c_t != c_s` allowed). As of 2026-06-09
the approved `kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md))
supplies the OS0 kinetic-form premise `c_t = c_s`. Therefore this note remains
valid as a quantified obstruction to leaving the kinetic form anisotropic; it is
not, by itself, a live obstruction to the adopted OS0 kinetic-form surface. The
separate B4 note
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md))
handles the marginal anisotropy on that OS0 surface. No audit verdict is changed
by this pointer.

## Role

This note **resolves the open residual D** of the interacting emergent-Lorentz
result
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md),
which established that the velocity anisotropy is an **attractive** IR fixed point
but left open: *does the attractive flow + the `a⁻¹=M_Pl` hierarchy suppress the
power-divergent marginal Lorentz violation below the experimental bounds without a
custodial symmetry?*

**The answer is no — by 4 to 16 orders of magnitude.** This is the
Collins–Perez–Sudarsky–Urrutia–Vucetich (*PRL* **93** (2004) 191301) naturalness
problem, made **quantitative** for the framework. It is an honest, quantified
**obstruction**: the framework's gauge dynamics does **not** by itself solve Lorentz
naturalness; a custodial mechanism is **required**, and the framework does not
currently have one. Runner: **14 PASS / 0 FAIL** (order-of-magnitude scaling; O(1)
coefficients estimated, the qualitative gap robust).

This does **not** mean the framework is wrong. It means emergent Lorentz, at the
interacting level, is a sharp **open problem** with a precise target: either find a
hidden protecting symmetry in the framework's specific structure, or accept a
custodial admission.

## The argument

### (A) UV regeneration is not Planck-suppressed
The lattice's own dimension-6 anisotropy (coefficient `~a²`, the retained
emergent-Lorentz result) feeds the **marginal** velocity coefficient through a
spatial power-divergent loop, giving

```text
    δv|_UV ~ α_s(M_Pl)/(4π).
```

At the framework's bare coupling `β = 6` (SU(3) Wilson, `g² = 2N/β = 1`),
`α_s(M_Pl) = g²/4π ≈ 0.08`, so `δv|_UV ≈ 6×10⁻³` — loop-suppressed but **not**
Planck-suppressed (the Collins mechanism). Runner Part A.

### (B) The framework's anomalous dimension is small (asymptotic freedom)
The speed-difference operator's anomalous dimension is `γ = c_γ · α_s(M_Pl)` with
`c_γ ~ O(1–3)`, so `γ ~ 0.08–0.24`. Because the gauge sector is **asymptotically
free**, the coupling — and hence `γ` — is **weak exactly at the UV scale where the
regeneration occurs**. Runner Part B.

### (C) The required anomalous dimension
To suppress `δv|_UV` below an experimental bound over the Planck-to-observation
hierarchy, `(μ/M_Pl)^γ < bound/δv|_UV`, i.e.

```text
    γ_crit = log₁₀(δv|_UV / bound) / log₁₀(M_Pl/μ).
```

| observable | bound | γ_crit |
|---|---|---|
| photon (GRB/Fermi-LAT) | `10⁻²⁰` | **1.11** |
| electron (clock/Penning) | `10⁻²²` | **0.90** |
| nucleon (Hughes–Drever) | `10⁻²⁷` | **1.30** |
| quark/gluon (mesons, UHECR) | `10⁻¹²` | **0.51** |

The framework's `γ ≤ 0.24` is **below even the weakest** `γ_crit ≈ 0.51`. Runner
Part C.

### (D) The residual gap
With `γ ~ 0.1–0.3`, `δv|_IR(1 GeV) ~ 10⁻⁵ … 10⁻⁸` — leaving a **4–8 order** gap to
the weakest (colored-sector) bound and a **12–16 order** gap to the tight
photon/electron/nucleon bounds. Runner Part D.

### (E) What would close it — and why the framework lacks it
Closing the gap needs `γ ≳ 1`, i.e. a **strong-coupling fixed point** with an O(1)
anomalous dimension at the regeneration scale. Asymptotic freedom **precludes** this
near `M_Pl` (the coupling is weak there); the IR strong-QCD regime (`α_s ~ 1`) acts
over too few e-folds (~1 near `Λ_QCD`) to help (extra factor `~e⁻¹`, vs the `~10⁻¹⁴`
needed). A **custodial symmetry** (SUSY; Nibbelink–Pospelov, hep-ph/0502106) would
work but is **absent**; CPT (the split is CPT-even), `O_h` (permits it), and the
gauge Ward identity (does not tie `c_t` to `c_s`) do **not** protect the marginal
operator. Runner Part E.

## Verdict

**Quantified obstruction.** The framework's asymptotically-free gauge dynamics gives
`γ ~ 0.1–0.24`, far below the `γ_crit ~ 0.5–1.3` required to suppress the
UV-regenerated marginal Lorentz violation below experimental bounds. The attractive
IR flow of the interacting attractor note is real but **~10–15 orders too weak**.
Lorentz naturalness is
**not** closed by the gauge dynamics; a custodial mechanism (a strong-coupling fixed
point with `γ~1`, precluded by asymptotic freedom; or a custodial symmetry, absent)
is **required**. This is consistent with the field-wide Collins et al result — the
framework is not special here.

## Honest scope

- This is an **order-of-magnitude scaling** argument. The exact O(1) coefficient of
  the regeneration and the precise fixed-point `γ` require a full lattice
  perturbation-theory computation; they are the named **open inputs**. They do
  **not** change the qualitative no-go (`γ~0.2` vs `γ_crit~1` is a robust ~5×
  shortfall in the exponent, ~10⁺ orders in the observable).
- The steelman "all species share one `v*`, so no observable LV" **fails**:
  different gauge representations flow at different rates, and the observable is
  exactly the residual species-to-species speed difference `δv|_IR`.
- **Constructive targets** (what would overturn or close this): (i) a hidden
  symmetry of the spatial-lattice + continuous-time + Cl(3,0) structure that forbids
  the marginal operator (would make this obstruction evaporate); (ii) a
  framework-internal strong-coupling fixed point with `γ~1` near `M_Pl`; (iii) an
  honest custodial admission (a new principle). Absent these, emergent Lorentz at
  the interacting level remains an open obstruction.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only that emergent Lorentz
  has a quantified naturalness gap at the interacting level.
- It does **not** contradict the interacting attractor note (the attractive flow is
  real); it **quantifies** that note's open residual as a ~10–15 order gap.
- It does **not** contradict the tree-level dissolution (the marginal gate is absent
  on the native surface at tree level; this is the interacting/loop level).
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG-fit input
  (the LV bounds are used as comparators, not derivation inputs). Literature is
  comparator/scope only.
- It does **not** set or change any audit status.

## No-go discipline (N1–N8 summary)

- **N1 routes:** (a) gauge-flow suppression — *insufficient* (this note, ~10⁺ order
  gap); (b) strong fixed point `γ~1` — *precluded* by asymptotic freedom near `M_Pl`;
  (c) custodial symmetry — *would work, absent*; (d) hidden lattice symmetry —
  *open* (the constructive escape).
- **N2 wall-independence:** the gap survives varying `γ` (B), the bound/scale (C),
  and the sector (D).
- **N7 steelman:** the "common-`v*`" escape fails (residual species difference is the
  observable).
- **N3/N5/N6:** premises explicit (the regeneration `O(α_s/4π)`, the
  asymptotically-free `γ`, the hierarchy); "obstruction" means precisely the
  quantified `γ < γ_crit` shortfall, not an inconsistency proof.

## Reprove-and-cite ledger

- **Reproven here** (runner): `β=6 → g²=1 → α_s ≈ 0.08`; `δv|_UV ~ α_s/4π ≈ 6×10⁻³`;
  the framework `γ = c_γ α_s ~ 0.08–0.24`; the `γ_crit` thresholds for each bound;
  the residual `δv|_IR` and the order gaps; the strong-coupling/e-fold and
  custodial-symmetry analysis.
- **Cited** (comparator/scope only): Collins–Perez–Sudarsky–Urrutia–Vucetich *PRL*
  93 (2004) 191301; Chadha–Nielsen *Nucl. Phys.* B217 (1983) 125; Bednik–Pujolàs–
  Sibiryakov *JHEP* 1311 (2013) 064; Nibbelink–Pospelov hep-ph/0502106;
  Kostelecký–Russell SME data tables (LV bounds, comparators).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It
does not promote this note or change any audited claim scope.

- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the framework's
`β=6` SU(3) gauge coupling at the lattice scale; (3) the Collins regeneration
mechanism (lattice dim-6 → marginal coefficient, `O(α_s/4π)`); (4) the
asymptotically-free running and the one-loop velocity anomalous dimension of the
interacting attractor note;
(5) experimental LV bounds as comparators. The result is an order-of-magnitude
scaling estimate; the exact regeneration coefficient and fixed-point `γ` are open.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (anomalous dimension, asymptotic freedom, marginal operator,
RG suppression, custodial symmetry). The LV bounds are comparators, not derivation
inputs; no `g_bare`/fitted value is consumed as a derivation input (`β=6 → g²=1` is
the framework's own bare-coupling convention, used here only to set the UV scale).

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the interacting attractor note, the emergent-Lorentz notes, the no-go, or
any upstream row. The audit lane is the only status authority.

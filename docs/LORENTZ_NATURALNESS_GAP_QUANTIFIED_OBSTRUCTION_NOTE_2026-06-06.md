# Lorentz Naturalness: Supplied-Parameter Comparator Gap for Gauge-Flow Suppression

**Date:** 2026-06-06
**Claim type:** bounded_theorem (supplied-parameter comparator)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary
declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.py`](../scripts/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.txt`](../logs/runner-cache/frontier_lorentz_naturalness_gap_quantified_obstruction_2026_06_06.txt)

---

## 2026-06-09 surface-scope update

The comparator gap quantified below is computed on a **non-isotropic** surface
(continuous-time / anisotropic regulator, `c_t != c_s` allowed). As of 2026-06-09
the approved `kinetic_isotropy_primitive`
([`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md))
supplies the OS0 kinetic-form premise `c_t = c_s`. Therefore this note remains
valid as a quantified comparator against leaving the kinetic form anisotropic;
it is not, by itself, a live obstruction to the adopted OS0 kinetic-form surface. The
separate B4 note
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md))
handles the marginal anisotropy on that OS0 surface. No audit verdict is changed
by this pointer.

## Role

This note gives a **supplied-parameter comparator estimate** for open residual D
of the interacting emergent-Lorentz
result
[`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`](EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md),
which established that the velocity anisotropy is an **attractive** IR fixed point
but left open the physical-coefficient question: *if* a Collins-type
power-divergent marginal Lorentz-violation coefficient is regenerated at
`O(alpha_s/4pi)`, and *if* the relevant anomalous dimension is
`gamma = c_gamma alpha_s` with `c_gamma <= 3`, does the attractive flow plus
the `a^-1=M_Pl` hierarchy suppress that supplied coefficient below
representative LV comparator bounds?

**Under those supplied inputs, the answer is no, by 4 to 16 orders of
magnitude.** This is the Collins-Perez-Sudarsky-Urrutia-Vucetich (*PRL*
**93** (2004) 191301) naturalness problem, used here as comparator context.
It is not a first-principles derivation of the regeneration coefficient, the
physical anomalous-dimension range, or the absence of all possible hidden
protection mechanisms. Runner: **8 PASS / 0 FAIL**.

This does **not** mean the framework is wrong. It means emergent Lorentz, at the
interacting level, has a sharp **open coefficient/protection target**: derive
the actual regeneration coefficient and anomalous dimension from the framework,
or find a hidden protecting symmetry/custodial mechanism that invalidates the
supplied comparator estimate.

## The argument

### (A) Supplied UV regeneration is not Planck-suppressed
The lattice's own dimension-6 anisotropy (coefficient `~a²`, the retained
emergent-Lorentz result) feeds the **marginal** velocity coefficient through a
spatial power-divergent loop, giving

```text
    δv|_UV ~ α_s(M_Pl)/(4π).
```

At the framework's bare coupling `beta = 6` (SU(3) Wilson, `g^2 = 2N/beta = 1`),
`α_s(M_Pl) = g²/4π ≈ 0.08`, so `δv|_UV ≈ 6×10⁻³` — loop-suppressed but **not**
Planck-suppressed under the supplied Collins mechanism. Runner Part A.

### (B) The supplied anomalous-dimension estimate is small (asymptotic freedom)
The supplied speed-difference anomalous-dimension estimate is `γ = c_γ · α_s(M_Pl)` with
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

The supplied `γ ≤ 0.24` estimate is **below even the weakest** `γ_crit ≈ 0.51`. Runner
Part C.

### (D) The residual gap
With `γ ~ 0.1–0.3`, `δv|_IR(1 GeV) ~ 10⁻⁵ … 10⁻⁸` — leaving a **4–8 order** gap to
the weakest (colored-sector) bound and a **12–16 order** gap to the tight
photon/electron/nucleon bounds. Runner Part D.

### (E) What the supplied comparator would need
Closing the supplied-parameter gap needs `γ ≳ 1`, i.e. an O(1) anomalous
dimension across the hierarchy or a separate custodial/protection mechanism.
The runner checks the arithmetic threshold and the limited help from the last
strong-QCD e-fold. It does **not** derive the absence of every possible
framework-internal protection mechanism. Runner Part E.

## Verdict

**Supplied-parameter comparator gap.** Given `delta v_UV ~ alpha_s/4pi`,
`gamma = c_gamma alpha_s` with `c_gamma <= 3`, `beta=6`, and the listed LV
comparator bounds, the computed `gamma ~ 0.08-0.24` is below the
`gamma_crit ~ 0.5-1.3` required to suppress the supplied coefficient. The
attractive IR flow of the interacting attractor note is real, but this supplied
estimate remains **4-16 orders** above the representative bounds.

This note does not prove that Lorentz naturalness is impossible in the
framework. It identifies what the current supplied estimate fails to do and
what a future framework-native repair must derive or evade.

## Honest scope

- This is a **supplied-parameter order-of-magnitude scaling** argument. The exact O(1) coefficient of
  the regeneration and the precise fixed-point `γ` require a full lattice
  perturbation-theory computation; they are the named **open inputs**. They do
  not become framework-native derivations in this note.
- The steelman "all species share one physical readout, so no observable LV"
  is not closed here. Under the supplied representation-dependent running
  estimate, the comparator observable is the residual species-to-species speed
  difference `δv|_IR`; a future shared-readout theorem would evade this
  comparator.
- **Constructive targets** (what would overturn or close the comparator gap):
  (i) a hidden
  symmetry of the spatial-lattice + continuous-time + Cl(3,0) structure that forbids
  the marginal operator (would make this comparator gap evaporate); (ii) a
  framework-internal strong-coupling fixed point with `γ~1` near `M_Pl`; (iii) an
  honest custodial admission (a new principle). Absent these, the supplied
  comparator estimate remains an open target, not a retained no-go.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only that emergent Lorentz
  has a supplied-parameter naturalness gap at the interacting level.
- It does **not** contradict the interacting attractor note (the attractive flow is
  real); it **quantifies** that note's open residual as a ~10–15 order gap.
- It does **not** contradict the tree-level dissolution (the marginal gate is absent
  on the native surface at tree level; this is the interacting/loop level).
- It does **not** derive the Collins regeneration coefficient, the physical
  anomalous-dimension range, or absence of all hidden custodial/protection
  routes from retained framework primitives.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG-fit input
  (the LV bounds are used as comparators, not derivation inputs). Literature is
  comparator/scope only.
- It does **not** set or change any audit status.

## Comparator discipline

- **Routes separated:** (a) supplied gauge-flow suppression — *insufficient*
  (this note, 4-16 order gap); (b) O(1) anomalous dimension over the hierarchy
  — *not derived here*; (c) custodial/protection symmetry — *not ruled out
  here*; (d) hidden lattice symmetry — *open*.
- **Wall-independence:** the supplied gap survives varying `γ` (B), the bound/scale (C),
  and the sector (D).
- **Steelman preserved:** a future route may still derive a shared physical
  readout or a protection theorem; this note does not close that route.
- **Premises explicit:** the regeneration `O(α_s/4π)`, the
  asymptotically-free `γ`, the hierarchy); "comparator gap" means precisely
  the supplied `γ < γ_crit` shortfall, not an inconsistency proof.

## Reprove-and-cite ledger

- **Recomputed here** (runner): `beta=6 -> g^2=1 -> alpha_s ~= 0.08`;
  `delta v_UV ~ alpha_s/4pi ~= 6e-3`;
  the supplied `γ = c_γ α_s ~ 0.08–0.24` estimate; the `γ_crit` thresholds for each bound;
  the residual `delta v_IR` and the order gaps; the O(1)-gamma threshold and
  one-e-fold strong-QCD comparison.
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

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the supplied
`β=6` SU(3) gauge-coupling normalization at the lattice scale; (3) the Collins regeneration
mechanism (lattice dim-6 → marginal coefficient, `O(α_s/4π)`); (4) the
asymptotically-free running and the one-loop velocity anomalous dimension of the
interacting attractor note;
(5) experimental LV bounds as comparators. The result is an order-of-magnitude
scaling estimate; the exact regeneration coefficient and fixed-point `γ` are open.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (anomalous dimension, asymptotic freedom, marginal operator,
RG suppression, custodial symmetry). The LV bounds are comparators, not derivation
inputs; the `beta=6 -> g^2=1` normalization is part of the supplied comparator
surface, used here only to set the UV scale.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the interacting attractor note, the emergent-Lorentz notes, the no-go, or
any upstream row. The audit lane is the only status authority.

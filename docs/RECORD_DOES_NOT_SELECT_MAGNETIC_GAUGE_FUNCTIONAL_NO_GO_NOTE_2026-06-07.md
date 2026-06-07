# Record Does Not Select the Magnetic Gauge Functional — No-Go Note

**Date:** 2026-06-07
**Type:** named-obstruction no-go
**Claim type:** no_go
**Status:** no-go proposal. Strengthens the existing
[`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md):
*no record-derivable / first-principles selection principle* picks the magnetic
single-plaquette functional within the record-forced gauge-invariant-local
class. Adds no axiom, no fitted/imported value. Audit verdict and downstream
effective status are set only by the independent audit lane.
**Authority role:** no-go source proposal.
**Primary runner:**
[`scripts/audit_companion_record_does_not_select_gauge_functional_2026_06_07.py`](../scripts/audit_companion_record_does_not_select_gauge_functional_2026_06_07.py)
(SCORECARD PASS=7 FAIL=0, exact numpy).

## Context

[`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
forces the dynamics into the **gauge-invariant-local class** (leading terms:
plaquette + covariant hopping + mass) from record-preservation + locality +
Hermiticity, but states verbatim that it "does not derive the action" — the
residual is the couplings and the **functional within the class**. The landed
`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO` shows the retained *primitive stack*
does not select among Wilson, heat-kernel, and Manton. This note asks the
sharper question and answers it.

## Question

Does any **record-derivable / first-principles** selection principle — beyond
the bare primitive stack — pick the magnetic single-plaquette functional within
the forced class? Five candidates were tested: (i) KMS / Tomita–Takesaki
modular condition; (ii) convolution-semigroup / decoherence-as-group-diffusion;
(iii) (P4) real-positivity from the real-operator record (K-reality);
(iv) Osterwalder–Schrader reflection-positivity + Symanzik minimality;
(v) maximum-entropy / Jaynes.

## Answer

**NO.** None of the five selection principles picks the functional, and the
two that distinguish the functionals at all do so only via an imported
convention or a narrow pre-chosen ansatz:

| principle | why it does not select |
|---|---|
| KMS / modular | pins the *(generator, weight) pair*, never the action alone; pure group-diffusion's unique equilibrium is Haar |
| convolution-semigroup | **counter-witnessed** (below): the Lévy/Hunt class of reflection-positive convolution semigroups is infinite-dimensional |
| (P4) / K-reality | the real record forces only the sign / anti-imaginary half; Wilson, heat-kernel, Manton are equally K-real and reflection-positive |
| OS + Symanzik minimality | reflection positivity admits a convex family; "minimality" has inequivalent readings; none derivable from `{Lattice, Quantum, Record}` |
| max-entropy / Jaynes | a bijection `{energy observable} → {Gibbs weight}`; returns whichever functional (energy observable) is fed in |

## The load-bearing counter-witness (exact)

On `SU(2)`, write a bi-invariant single-plaquette weight as a class function
`w(U) = Σ_j c_j χ_j(U)`. A convolution **semigroup** has
`c_j(t) = (2j+1)·exp(−t·ψ(λ_j))` with `λ_j = j(j+1)` and `ψ` a valid Lévy
exponent (a Bernstein function of the Casimir); reflection positivity holds iff
all `c_j ≥ 0`. The single-plaquette expectation is `⟨P⟩ = ½·c_{1/2}/c_0`.

Two **distinct** exact convolution semigroups:

- pure-Gaussian **heat kernel**: `ψ_HK(x) = x` → `⟨P⟩ = e^{−3/4} ≈ 0.4724`;
- **Gaussian + bounded jump**: `ψ_GJ(x) = w·x + g(1 − e^{−τx})` with
  `w = ½, g = 1, τ = ½` (so `w + gτ = 1`) → `⟨P⟩ ≈ 0.5027`.

Both are reflection-positive (all `c_j ≥ 0`; analytically `e^{−tψ} > 0`),
**both** match the continuum leading-order slope (`ψ ∼ x` as `x → 0`), yet give
`⟨P⟩` differing by ~6%. Selecting the pure-Gaussian heat kernel requires the
extra premise "no jump part" (`g = 0`) — an **assumption**, not a derivation.

Cross-check against the landed no-go: at the framework's `SU(3)` `β = 6` the
three named functionals genuinely differ — Wilson `⟨P⟩ = 0.42253` (certified
single-plaquette Picard–Fuchs value), heat-kernel `e^{−2/3} = 0.51342`, Manton
`≈ 0.56` — a ~13% absolute spread. So the runner resolves the functionals; it
finds no record-derivable principle that picks one.

## What is and is not claimed

- **Is:** within the record-forced gauge-invariant-local class, the *magnetic
  single-plaquette functional* is an irreducible admission (an import-bridge):
  no record-derivable / first-principles condition tested selects it.
- **Is not:** this does **not** claim Wilson is wrong, nor that *no possible*
  principle could ever select it; it records that the five natural
  record/first-principles candidates do not, with an explicit
  reflection-positive convolution-semigroup counter-witness.
- It strengthens, and does not contradict, `BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO`
  (primitive-stack non-selection) and is consistent with
  `DYNAMICS_FORM_FROM_RECORD_PRESERVATION...` (which forces the class, not the
  functional within it).

## Forbidden imports

No PDG / fitted value is used as a derivation input. The `SU(3)` `β = 6`
functional values (Wilson / heat-kernel / Manton) appear **only** as a
comparator cross-check against the landed no-go, never as a derivation input.
The character-orthogonality, Casimir spectrum, and Bernstein/Lévy structure are
computed inside the runner.

## Cross-references

- [`BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`](BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md)
  — the primitive-stack non-selection this note strengthens.
- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  — forces the class; explicitly not the functional within it.

# One Chirality Grading ε Underlies Both Weak Parity Violation and the Flavor-Phase Mechanism (Narrow Structural Note)

**Date:** 2026-06-04
**Type:** structural_map
**Claim type:** narrow structural note — a single chirality grading `ε` is the common root of two
distinct features; the VALUES (δ=2/9, the chiral origin of SU(2)_L) are **not** derived here (gated).
**Claim scope:** the framework carries one chirality grading `ε = (-1)^{x+y+z}` — a **per-site** sign
(the staggered chirality, `{ε,D}=0`). The same `ε` underlies **(A)** the chiral weak coupling
`SU(2)_L` (parity violation) and **(B)** the chirality-graded determinant phase / η-invariant — the
mechanism the untried lead (#2624) ties to the Koide phase `δ`. In the **vector limit** (`ε → 𝟙`) both
vanish together: parity is restored *and* the η/graded-trace mechanism is identically the ungraded
one. **One chirality, two roles.** Crucially, **none of this uses the qulink (dynamical-link)
ontology** — `ε`, the on-site qubit `su(2)`, and the generation Yukawa are all **site/matter**
structures, so this stands on the existing `{Quantum, Locality, Record}`, not on the edge commitment.
**actual_current_surface_status:** structural map (6/6 numpy/sympy). **Solid:** ε is site-based (no
qulinks); parity violation requires ε; the η/graded-trace mechanism requires ε. **Not derived here
(gated/untried):** the value `δ=2/9` from the η computation, and *why* SU(2) couples chirally. Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_one_chirality_grades_weak_su2_and_flavor_phase_exact.py`](./../scripts/audit_companion_one_chirality_grades_weak_su2_and_flavor_phase_exact.py)

## Does this stand on qulinks? — No

The qulink result (#2679) was needed only to **gauge** `su(2)` (make it the link connection). Here:
- `ε = (-1)^{x+y+z}` is a **per-site** sign — site data, not a link;
- the weak `su(2)` is the **on-site qubit's own** `su(2)` (the framework's "su(2) double-use");
- the generation Yukawa lives on the **sites**.

So the chirality/δ program rests on the existing `{Quantum, Locality, Record}` + the staggered `ε`,
with **no dependence on the dynamical-link (qulink) ontology**.

## Statement (reproven, 6/6)

1. `ε` is a `Z₂` chirality involution (`ε²=𝟙`); `P_L=(𝟙+ε)/2`, `P_R=(𝟙-ε)/2` are complementary
   projectors.
2. **(A) Parity violation needs ε.** The chiral coupling `T^a ⊗ P_L` (su(2) on left-handed only) is
   **not** invariant under parity (`L↔R`); the vector coupling `T^a ⊗ 𝟙` is. So parity violation is
   exactly the `ε`-graded (chiral) coupling.
3. **(B) The η mechanism needs ε.** The chirality-graded ("super") trace `Str(O)=Tr(ε O)` gives the
   **index / η** (`Tr_L−Tr_R`, e.g. 0 for a balanced system) — distinct from the ungraded dimension
   (`Tr_L+Tr_R`). The η-invariant — the determinant phase that the #2624 lead identifies as the
   `δ`-selection mechanism — is therefore `ε`-dependent.
4. **Vector limit kills both.** At `ε→𝟙`: `P_L=𝟙` (no chirality) → the coupling is parity-conserving,
   **and** `Str=Tr` (the η mechanism is the trivial ungraded trace). Both features vanish together.
5. **The flavor-phase side.** The Koide phase `δ` is real-spectrum data of the (Hermitian) Yukawa;
   the vector/modulus potential `Σ log|λ_k(δ)|` is **even in δ** — stationary at the CP-conserving
   `δ=0`. Only a chiral (η, odd-in-δ) contribution can move the selected `δ` off `0`. So `δ`-selection
   rides on `ε`.
6. All of (1)–(5) are **site/matter** — no qulink ontology used.

## What this is, and is not

- **Is:** a structural map. The framework has **one** chirality `ε`, and it is the common root of weak
  parity violation and the η/δ mechanism. Parity violation and the flavor phase are therefore **not
  two independent inputs** — they are the same chirality, and a theory with `ε` has both while a vector
  theory has neither. And it costs **no new axiom** and **no qulink**.
- **Is not (gated/untried, flagged):** (i) the VALUE `δ=2/9` — that is the η-invariant computation on
  the gated staggered-Dirac mass structure, not done here; (ii) the ORIGIN of SU(2)'s chiral coupling
  — why `su(2)` couples to `P_L` rather than vectorially is the deep chiral-structure question, tied to
  the staggered `ε` and not derived here; (iii) the magnitude `r=1/2` (Koide `Q=2/3`) — the irreducible
  flavor admission, untouched and orthogonal.

## Trace gate

```yaml
trace_class: structural_unification_map
target_blocker_text: "weak parity violation and the charged-lepton phase delta are independent inputs"
source_of_blocker_text: standard_model
reachability_to_target: maps a single common root (the chirality grading eps); values gated
artifact_role: structural_map
next_trace_action: "the gated pieces: (i) compute the eta-invariant on the staggered-Dirac mass to test delta=2/9; (ii) derive the chiral (P_L) coupling of su(2) from the staggered eps. Magnitude r=1/2 stays the admission."
```

## Forbidden imports / reprove-and-cite

- Chirality projectors, parity action, and the graded/super-trace (index) are standard; reproven from
  Pauli primitives. The Koide-phase / η connection is the cited #2624 lead, not a derivation input. No
  PDG values; no fitted parameters.

## Cross-references

- `ELECTROWEAK_GAUGE_ALGEBRA_FROM_THE_QUBIT_LINK_NARROW_THEOREM_NOTE_2026-06-04.md` (#2679) — the
  electroweak gauge algebra whose SU(2)_L chirality is the (A) side here.
- The #2624 frontier correction — the η-invariant / determinant-phase → `δ` lead that is the (B) side.

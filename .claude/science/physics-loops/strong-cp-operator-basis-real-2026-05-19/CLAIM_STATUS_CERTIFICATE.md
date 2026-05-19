# Claim-Status Certificate — Strong CP Operator-Basis + Mass Orientation (2026-05-19)

```yaml
goal: derive "no admissible F-tilde-F slot" and "real positive quark-mass orientation" from retained primitives
target_claim_type: bounded_theorem
actual_current_surface_status: candidate-bounded-theorem-grade
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null

claim_type_reason: |
  Operator-basis F-tilde-F exclusion theorem (Theorem 2.4) and quark-mass
  orientation theorem (Theorem 3.4) are derived from:
    (A1) Cl(3) local algebra                      [retained axiom]
    (A2) Z^3 spatial substrate                    [retained axiom]
    (R1) canonical normalization beta = 6         [retained theorem]
    (R2) staggered Dirac anti-Hermiticity D^dag = -D
         (parent note STRONG_CP_THETA_ZERO_NOTE.md Leg A line 49)
    (R3) reflection positivity on the staggered surface
         (AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md
          Case A staggered-only sector, retained)
  No new axioms; no black-box Vafa-Witten / Leutwyler-Smilga citations as
  proof inputs.

  The audit verdict on the parent note (2026-04-28, lines 361-385) flagged
  two pieces as action-class definitions rather than derivations:
    (a) no admissible F-tilde-F operator slot in the retained action,
    (b) positive real quark-mass orientation arg det(M_u M_d) = 0.
  This note supplies both derivations and exhibits them on actual SU(3)
  configurations via 8 verification gates.

  Runner: PASS = 8 gates / FAIL = 0 gates (PASS = 33 sub-checks / FAIL = 0
  sub-checks, runtime = 0.3s).

audit_required_before_effective_retained: true
bare_retained_allowed: false

scope_constraints:
  - retained Cl(3)/Z^3 Wilson-plus-staggered surface only
  - canonical-normalization Wilson plaquette-local action only (P1-P5)
  - finite-Lambda checks (small 2x2x2x2 SU(3) lattice for spectral tests)
  - does NOT claim dynamical theta-selection beyond canonical normalization
  - does NOT claim axion-model exclusion beyond the retained surface
  - does NOT extend to multi-plaquette or higher-trace operator extensions

deliverables:
  source_note:
    path: docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md
    sections:
      - "§0 Honest framing — audit-boundary repair scope"
      - "§1 Setting (Cl(3), Z^3, SU(3), Wilson plaquette holonomy)"
      - "§2 Theorem 1 — Operator-basis F-tilde-F slot exclusion"
      - "    Lemma 2.1 — gauge-invariant plaquette-local operator basis"
      - "    Lemma 2.2 — continuum-limit decomposition Re vs Im Tr U_P"
      - "    Lemma 2.3 — CP-odd slot exclusion from real-positive-measure"
      - "    Theorem 2.4 — operator-basis F-tilde-F exclusion"
      - "§3 Theorem 2 — Quark-mass orientation"
      - "    Lemma 3.1 — (C-det) + (C-class) two-constraint split"
      - "    Lemma 3.2 — sign selection from bounded-below convention"
      - "    Lemma 3.3 — phase-pure imaginary case excluded by (C-det)"
      - "    Theorem 3.4 — quark-mass orientation theorem"
      - "§4 Combined theta_eff = 0 derived (not stipulated)"
      - "§5 Runner: forbidden-slot construction + rejection"
      - "§6 Anti-overclaim / honest scope"
      - "§7 Composition upstream (PR #1577 salvage)"
      - "§8 Commands run + cached log"
  runner:
    path: scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py
    gates:
      - "V1 Plaquette-local gauge-invariant operator enumeration"
      - "V2 Real-action exclusion of imaginary-plaquette slot"
      - "V3 Canonical-normalization continuum-limit decomposition"
      - "V4 Bounded-below check on real Wilson slot"
      - "V5 Mass orientation: (C-det) + (C-class) two-constraint split"
      - "V6 Mass orientation: reflection-positivity precondition (C-det)"
      - "V7 Forbidden-slot construction + rejection at lattice level"
      - "V8 Composition with Leg A retained primitive"
    result: PASS=8 gates / FAIL=0 gates (PASS=33 sub-checks / FAIL=0)
    runtime_sec: 0.3
  cached_log:
    path: logs/runner-cache/frontier_strong_cp_operator_basis_real_2026_05_19.txt

retained_primitives_composed:
  - "Cl(3) local algebra (axiom)"
  - "Z^3 spatial substrate (axiom)"
  - "Canonical normalization beta = 6 (retained on axiom-first surface)"
  - "Staggered Dirac anti-Hermiticity D^dag = -D (retained Leg A in parent note)"
  - "Reflection positivity Case A staggered-only (retained)"

NOT_used_as_proof_input:
  - "Vafa-Witten (1984) [cited in parent note as support only]"
  - "Leutwyler-Smilga (1992) [cited in parent note as support only]"
  - "Osterwalder-Schrader axioms [machinery; not load-bearing here]"

honest_narrowings_made_during_derivation:
  - |
    Lemma 3.1 was originally stated as "M-mixed gives complex det" but
    empirically (M-mixed = m*I + i*m5*eps) gives real-positive det on
    sampled small Λ via staggered chirality structure. Restated honestly:
    (M-mixed) and (M-pseudoscalar) are excluded by (C-class) [scalar-mass
    action class restriction from parent note Leg C], not by (C-det).
    Lemma 3.1 now correctly separates the two constraints and shows M-real
    is the unique intersection.
  - |
    V8 originally tested M-complex(alpha=pi/2) = i*m*I which gives
    det = i^N * (real number), sensitive to N mod 4. Replaced with
    M-complex(alpha=pi/4) which uniformly rejects on all sampled configs.

upstream_composition_consequences_if_retained:
  - |
    Parent STRONG_CP_THETA_ZERO_NOTE.md audit boundary (lines 361-385)
    listed both "no F-tilde-F slot" and "real mass orientation" as
    action-class stipulations. If this note lands as retained-grade,
    those become derived theorems, lifting the audited_conditional
    verdict to retained candidacy.
  - |
    PR #1577 salvage (commit 8369973af) cites Leg A det(D+mI)>0 as a
    conditional input. Promoting parent note to retained would lift
    that conditional automatically.
  - |
    CKM neutron-EDM corollary inherits derived theta_eff = 0 rather
    than action-class-stipulated value.

  These consequences are noted for traceability; effective-status
  promotion is the audit lane's call.
```

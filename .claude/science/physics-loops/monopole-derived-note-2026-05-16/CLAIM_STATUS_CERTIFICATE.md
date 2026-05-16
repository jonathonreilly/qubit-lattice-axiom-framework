# Claim Status Certificate — monopole-derived-note 2026-05-16

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: |
  The exact numerical prefactor (1.43 M_Pl) is conditional on a named
  one-loop SM RG bridge import for alpha_EM(M_Pl).
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: |
  The lattice Coulomb Green's function value c_lat = G_lat(0) = 0.2527 is
  closed lattice arithmetic on cubic Z^3. The mass-shape relation
  M_mono = c_lat * beta * (1/a) follows from the compact U(1) Wilson action
  by the standard Banks-Myerson-Kogut / Polyakov self-energy argument. The
  numerical prefactor depends linearly on the imported
  alpha_EM(M_Pl) ~ 1/72.1 (one-loop SM RG running from alpha_EM(M_Z)),
  which is not derived from the lattice axiom packet. The order-of-magnitude
  prediction M_mono ~ M_Planck is robust across the perturbative alpha band
  alpha^-1 in [30, 60].
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Status fields

- **Actual current-surface status:** `bounded-support`. The note's headline
  is a bounded numerical prefactor with an explicit, named, non-derivation
  import.
- **Target claim type:** `bounded_theorem`. The note documents a closed
  lattice derivation modulo three named imports (Wilson action, Planck
  pin, alpha_EM(M_Pl) one-loop SM RG running), and explicitly retracts the
  "direct numerical self-energy" framing of Step 4.
- **Hypothetical-axiom status:** null. No new axioms are introduced; the
  Planck-scale package pin is carried as an existing framework pin elsewhere,
  not as a new axiom of this note.
- **Admitted-observation status:** null. No experimental input is used as
  proof. Experimental bounds (Parker, MACRO, IceCube, MoEDAL) are referenced
  only as the prediction "flux = 0 with inflation" trivially satisfies them.

## Why this is not retained-grade

1. The numerical prefactor depends on an externally calibrated coupling
   `alpha_EM(M_Pl)`. That coupling is not derived from the lattice axiom
   packet; it is imported from one-loop SM RG running.
2. The Planck-scale package pin `a^(-1) = M_Pl` is carried elsewhere in the
   framework, not derived in this note.
3. Step 4 does not provide an independent quantitative numerical cross-check
   of c_lat. The bare Wilson action of the constructed Wu-Yang field is
   dominated by Dirac-string artifacts. Step 4's load-bearing content is now
   the topology check (integer charge, zero sum), which holds at every L.

For the note to become retained-grade, it would need either (a) a derivation
of `alpha_EM(M_Pl)` from the lattice axioms, or (b) a different framework-
native definition of the monopole mass that does not import a running gauge
coupling. Neither is in scope for this iteration.

## Review-loop disposition (self-review)

- **Local disposition:** `pass` with the narrowest honest status
  (`bounded-support`). The two audit complaints are addressed:
  (a) the alpha import is now explicitly labeled as a non-derivation
      bridge import; the headline distinguishes the conditional numerical
      prefactor from the import-robust order-of-magnitude statement.
  (b) Step 4 is re-scoped to a topology check; the order-of-magnitude
      mismatch between the bare Wilson action of the Wu-Yang configuration
      and the analytic c_lat is explicitly attributed to Dirac-string
      action and is no longer presented as an independent cross-check.
- **Audit required before effective retained:** YES. This certificate is
  branch-local self-review; an independent audit can re-evaluate the note
  on the updated text and runner.

## Dependency classes

- Derived (no import needed): Step 1 (integer charges), Step 2 (Dirac
  condition), Step 3 c_lat (lattice Coulomb GF on Z^3 — closed arithmetic),
  Step 3 mass shape (BKM/Polyakov on compact U(1) Wilson action).
- Bounded by named imports: Step 3 numerical prefactor (Wilson action,
  Planck pin, alpha_EM(M_Pl) one-loop SM RG), Step 5 cosmology (FRW,
  Kibble).
- Not derived: full two-loop SM RG plus threshold matching for
  alpha_EM(M_Pl); a true numerical measurement of c_lat (would require
  Monte Carlo free-energy sampling or DeGrand-Toussaint dual-lattice
  string subtraction); whether inflation actually occurred.

## Open imports (unchanged from prior iterations)

- `alpha_EM(M_Pl)` — load-bearing for the numerical prefactor.
- `a^(-1) = M_Pl` — Planck-scale package pin carried elsewhere.
- Wilson action choice — alternative compact actions shift c_lat by
  O(10%).

## Promotion / no-go gates

This iteration is a status alignment, not a promotion attempt and not a
no-go claim. No PR-opening Promotion Value Gate (V1-V5) is triggered;
no N1-N8 No-Go Discipline Gate is triggered. The PR opens a re-audit
opportunity on the corrected note.

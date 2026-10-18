# 12-hour goal: gravity on the scale ladder (started 2026-10-17 22:30 local)

Owner request: "run down gravity on the scale ladder idea … run a 12 hour goal on this,
make as much TOE progress as possible." Base: origin/main fa84175 + open PR #9702 (scale ladder note).

## Goal

Find out what fixes the graviton's leading form, its cone, its source and its first lattice
correction, as cross-rung invariants of the supplied 4D Kuhn-complex Regge model, and whether
gravity shares one light cone with the other fields. The open gravity items from #9702 are G1–G3
and the probe's two unrun probes: P-G2 (extract the full symbol) and P-G3 (Noether source).

## Milestones (each lands as a finite check, or goes to ai/probes if it is only probable)

- **M1. Symmetry census (done in the first hour).** Count invariant and gauge-invariant
  quadratic forms under B4, its proper part, the complex's own group K48 = S4 x inversion,
  and spatial-only groups.
- **M2. Metric universality of the Regge leading symbol.** Show that the K48 gauge-invariant
  leading forms are exactly linearised EH of K48-invariant flat metrics, and that Regge picks
  the metric of its edge lengths, with coefficient -(1/4) sqrt(det g0).
- **M3. A common cone.** Do a P1 scalar and a Whitney-form Maxwell field on the same complex
  share the edge-length metric's cone at leading order? Then compare the O(k^4) fingerprints
  across spins.
- **M4. Background selection.** Does tick reflection (OS-reflection compatibility) together
  with K48 force the isotropic background (b = 0)? Relate this to the approved
  kinetic_isotropy_primitive.
- **M5. k^4 census.** Under K48 plus gauge invariance, which on-shell TT k^4 shifts are allowed
  (birefringence, S4-only harmonics)? Explain Regge's B4-symmetric fingerprint.
- **M6. Source universality.** Couple the scalar to the edge-length perturbation. Test the
  lattice Ward identity (stress conservation) and whether gravity couples to every field
  through the one metric, which gives one G_N.
- **M7. Newtonian rung.** The static source gives a potential, and the cross-rung coefficient
  is carried from the lattice to 1/r.
- **M8. Land.** Write a source note, a runner and a cache for each valid result (PRs), send
  anything only probable to ai/probes, publish a report artifact, and record it in memory.

## Discipline
One numeric worker at a time, BLAS threads = 1, nice. Supplied-model framing throughout; no physical
identification; no new axioms; walls move.

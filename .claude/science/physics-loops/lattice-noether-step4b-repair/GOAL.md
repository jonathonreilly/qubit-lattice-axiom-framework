# Goal

Repair the lattice Noether Step 4b source surface so it no longer claims
that the canonical density (3) is derived from a site-dependent two-shift
Ward identity for arbitrary on-shell fields.

The honest target is a reviewable source PR that:

- narrows the `(2Z)^3` translation branch to the exact central two-step
  Ward identity;
- keeps the old density (3) as support-only unless a later audit-clean
  proof derives it;
- updates the runner with a field-level `L=6` localized-envelope check;
- regenerates the audit queue so the independent auditor can re-audit the
  edited row.

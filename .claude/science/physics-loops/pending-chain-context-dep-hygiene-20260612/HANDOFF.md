# Handoff

This PR removes three false context/meta dependencies from pending-chain source
notes:

- `START_HERE.md` on the lattice 3D Nyquist note;
- `MINIMAL_AXIOMS_2026-05-03.md` on the second-order Kubo note;
- `KOIDE_BAE_30_PROBE_CAMPAIGN_NOTE_2026-05-09.md` on the Koide r=1/2 no-go.

The replacement prose keeps each reference as plain text and says why it is not
load-bearing. Real retained scientific dependencies remain graph-visible
Markdown links.

Verification:

```text
in-memory citation graph: all three false blocker edges removed
git diff --check
lattice_3d_nyquist_diffraction_probe.py: pass
audit_companion_koide_r_half_not_symmetry_protected_exact.py: 6 PASS, 0 FAIL
linear_response_second_order_kubo.py: unchanged script; existing cache exit_code=0 elapsed_sec=574.52
```

No audit ledger, audit queue, generated audit data, or repo-wide authority file
is modified.

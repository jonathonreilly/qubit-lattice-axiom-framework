# Handoff

Branch: `physics-loop/atomic-jastrow-boundary-20260617`

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4176

Target row:
`work_history.atomic.hydrogen_helium_atomic_companion_note_2026-04-18`

What changed:

- The Jastrow contact-slope factor is now explicitly a supplied
  one-parameter finite-box trial-family boundary.
- The old wording that treated the cusp condition as derived from the retained
  Z3 kernel/self-adjointness was removed.
- The Jastrow runner now emits `cusp_guided_trial_ansatz_boundary`.
- The packet verifier requires that boundary and forbids the old hidden
  derivation phrasing.

What did not change:

- No audit data, audit ledger, audit queue, or repo-wide status surface was
  edited.
- No retained atomic theorem is claimed.
- No exact helium, continuum, volume-control, or eV spectroscopy bridge is
  claimed.

Reviewer next action:

Run the listed verification commands and decide whether to extract this source
repair for re-audit.

Verification already run on this branch:

- `python3 -m py_compile scripts/frontier_atomic_helium_jastrow_companion.py scripts/frontier_atomic_hydrogen_helium_companion_packet_verifier_2026_06_12.py`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/frontier_atomic_helium_jastrow_companion.py --check-only`
- `PYTHONPATH=scripts python3 scripts/cached_runner_output.py scripts/frontier_atomic_hydrogen_helium_companion_packet_verifier_2026_06_12.py --check-only`
- `python3 scripts/frontier_atomic_hydrogen_helium_companion_packet_verifier_2026_06_12.py`
- `git diff --check`
- `git diff -- docs/audit/data docs/audit/AUDIT_LEDGER.md docs/audit/AUDIT_QUEUE.md docs/audit/AUDIT_DISPATCH_QUEUE.md`

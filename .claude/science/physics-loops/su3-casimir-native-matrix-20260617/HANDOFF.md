# Handoff

This branch repairs `su3_casimir_fundamental_theorem_note_2026-05-02` by
retiring two textbook-math imports from the proof surface.

What changed:

- Schur's lemma is no longer needed to infer scalarity;
- the SU(N) Casimir formula is no longer needed to obtain the value;
- the note proves `C_2 = (4/3) I_3` by direct diagonal-square multiplication
  of the framework-supplied Gell-Mann matrices;
- the runner gates the direct matrix identity and centrality;
- textbook facts remain only as parallel context.

Checks to run:

- `python3 scripts/su3_casimir_fundamental_check.py`
- `python3 scripts/cached_runner_output.py scripts/su3_casimir_fundamental_check.py --refresh`
- `python3 scripts/cached_runner_output.py scripts/su3_casimir_fundamental_check.py --check-only`
- `python3 -m py_compile scripts/su3_casimir_fundamental_check.py`
- `git diff --check`

Remaining blockers:

- physical SM color identification remains downstream;
- perturbative QCD readout remains downstream;
- independent review/audit owns any status change.

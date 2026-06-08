# Handoff: DM Neutrino Vsel Trace-Dimension No-Go Repair

## What Changed

This PR repairs the audited conditional blocker for
`docs/DM_NEUTRINO_VSEL_CURVATURE_TASTE_TO_DIRAC_TRANSPORT_OBSTRUCTION_NO_GO_NOTE_2026-06-07.md`.

The prior source text and runner used the concrete Pauli `d=2` trace
normalization in T2/T3. The auditor correctly objected that the cited Dirac
authority does not make that trace dimension load-bearing for the note.

The repair replaces the load-bearing claim with the representation-independent
statement for `d = Tr(I)`:

```text
Tr M^(2n) = d |phi|^(2n)
Tr M^4 - (1/8)(Tr M^2)^2 = d(1-d/8)|phi|^4
Hess_e1 = diag(12c, 4c, 4c), c = d(1-d/8)
```

That keeps the negative result: the transported Dirac polynomial is radial for
any admissible trace dimension and cannot supply the taste-cube
`m_perp=32` axis-selector curvature.

## What It Does Not Do

- It does not edit `docs/audit/**`.
- It does not apply an audit verdict.
- It does not close the positive Schur suppression assembly.
- It does not admit a special trace convention for the Dirac family.

## Verification

```bash
python3 scripts/frontier_neutrino_vsel_curvature_transport_obstruction.py
# TOTAL: PASS=11 FAIL=0

python3 -m py_compile scripts/frontier_neutrino_vsel_curvature_transport_obstruction.py

python3 scripts/cached_runner_output.py --check-only scripts/frontier_neutrino_vsel_curvature_transport_obstruction.py
# fresh logs/runner-cache/frontier_neutrino_vsel_curvature_transport_obstruction.txt

git diff --check
git diff -- docs/audit
```

## Reviewer Note

This should be treated as a source-side no-go repair. Independent audit decides
whether the representation-independent T2/T3 form now satisfies the no-go row.

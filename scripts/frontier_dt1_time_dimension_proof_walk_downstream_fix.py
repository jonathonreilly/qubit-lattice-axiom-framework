#!/usr/bin/env python3
"""Documentary scope guard for the corrected DT1 source.

Checks explicit premise boundaries and recovery pointers only. It does not
prove the anomaly, Clifford, reconstruction or clock claims, and it does not
check or set audit status. The historical May17 prose layout is no longer the
current argument. Mathematical checks live in the named primary runner.
"""

# Bind actual documentary reads/existence checks to cache identity.
AUDIT_INPUT_PATHS = ['docs/DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md']
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/'docs/DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md'
def main():
    if not NOTE.is_file():
        print('[FAIL METADATA] DT1 source missing');return 1
    text=NOTE.read_text()
    required={
        'supplied spatial dimension':'supplied spatial dimension `d_s=3`',
        'separately supplied clock cap':'separately supplied clock cap `0 <= d_t <= 1`',
        'irreducible reconstruction restriction':'volume-grading/irreducible reconstruction surface',
        'doubled-carrier counterexample':'Centrality alone does not exclude all gradings on doubled representations.',
        'physical premise separation':'They do not establish either reconstruction or the clock cap.',
        'KS dependency source':'STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md',
        'KS supplied premises':'supplied P-KIN and P-SD',
        'withdrawal of full-chain independence':'withdraws the older full-chain assertion',
        'open dynamics bridge':'ONE_TIME_DIMENSION_DT1_REDUCES_TO_EMERGENT_DYNAMICS_GATE_OPEN_GATE_NOTE_2026-06-17.md',
        'primary arithmetic runner':'frontier_dt1_time_dimension_proof_walk_lattice_independence.py',
        'recovery revision':'f24d17d97d372df977476e4a69674577f31af575',
    }
    failed=0
    for label,token in required.items():
        ok=token in text;failed+=not ok
        print(f"[{'PASS' if ok else 'FAIL'} METADATA] {label}")
    print(f'{len(required)-failed} documentary checks pass; {failed} fail. No mathematical or status verdict.')
    return int(failed!=0)
if __name__=='__main__':sys.exit(main())

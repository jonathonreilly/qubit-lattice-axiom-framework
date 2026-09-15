#!/usr/bin/env python3
"""Portable supporting proof checks, standard library only."""
import argparse,hashlib,json,signal,time,resource,sys
import importlib.util
from pathlib import Path

AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = [
    'docs/NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md',
    'docs/NATIVE_CERTIFIED_LOCAL_GREEN_SCALARS_NOTE_2026-09-09.md',
    'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md',
    'docs/NATIVE_GAPFREE_GENERATOR_PROPAGATION_NOTE_2026-09-09.md',
    'docs/work_history/repo/review_feedback/pr8072-evidence/README.md',
    'docs/work_history/repo/review_feedback/pr8072-evidence/pr8072-LOCAL_GREEN_PROOF.md',
    'docs/work_history/repo/review_feedback/pr8072-evidence/pr8072-WARD_INSERTION_PROOF.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/SOURCE_MANIFEST.json',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/GENERATOR_PROOF.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/GENERATOR_REVIEW.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/POISSON_CONTROLS.json',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/POISSON_PATH_HISTORY.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/POISSON_PROOF.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/POISSON_REVIEW.md',
    'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/provenance/WARD_INSERTION_REVIEW.md',
    'scripts/native_gapfree_generator_propagation_2026_09_09_controls.py',
]

def main():
 start=time.monotonic();p=argparse.ArgumentParser(description=__doc__);p.add_argument('--json',action='store_true');a=p.parse_args()
 signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('30s support cap')));signal.alarm(30)
 root=Path(__file__).resolve().parents[1];manifest=root/'outputs/native_gapfree_generator_propagation_2026_09_09_inputs/SOURCE_MANIFEST.json';pins=json.loads(manifest.read_text())['inputs']
 for rel,h in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=h:raise ValueError('input identity '+rel)
 helper=root/'scripts/native_gapfree_generator_propagation_2026_09_09_controls.py';data=helper.read_bytes()
 spec=importlib.util.spec_from_file_location('supporting_controls',root/'scripts/native_gapfree_generator_propagation_2026_09_09_controls.py');module=importlib.util.module_from_spec(spec);exec(compile(data,str(helper),'exec'),module.__dict__);r=module.controls()
 if time.monotonic()-start>=30 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)>384*1048576:raise ValueError('support resources')
 r.update(claim_status='conditional-support',input_hashes=pins)
 if a.json:print(json.dumps(r,sort_keys=True,indent=2))
 (root/'outputs/native_gapfree_generator_propagation_2026_09_09.json').write_text(json.dumps(r,sort_keys=True,indent=2)+'\n')
 print('TOTAL: PASS=%d FAIL=0'%r['predicates'])
 print('per_element: small rational generator, local-resolvent and sign identities executed; no native operator evaluation')
 print('per_site: analytical local-source construction only; no sitewise native array execution')
 print('per_mode: Poisson sufficient-condition arithmetic executed; full native propagation remains uncomputed')
 print('per_block: finite synthetic first-action Gram control executed; physical leakage is an uncomputed hypothesis')
 print('lattice_wide: uniform analytical propagation statement is conditional on the stated ORIGINAL-domain leakage bound')
if __name__=='__main__':main()

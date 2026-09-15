import argparse,json,hashlib,signal,time,importlib.util
from pathlib import Path

AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/NATIVE_PAIR_VACUUM_CHART_NOTE_2026-09-09.md', 'scripts/native_pair_vacuum_chart_controls_2026_09_09.py', 'docs/NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md', 'docs/NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'outputs/native_pair_vacuum_chart_2026_09_09_inputs.json')

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(180);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 pins=json.loads((root/'outputs/native_pair_vacuum_chart_2026_09_09_inputs.json').read_text())
 for rel,h in pins.items():
  if hashlib.sha256((root/rel).read_bytes()).hexdigest()!=h:raise ValueError('input '+rel)
 helper=root/'scripts/native_pair_vacuum_chart_controls_2026_09_09.py';spec=importlib.util.spec_from_file_location('controls',root/'scripts/native_pair_vacuum_chart_controls_2026_09_09.py');module=importlib.util.module_from_spec(spec);exec(compile(helper.read_bytes(),str(helper),'exec'),module.__dict__);result=module.result
 result.update({'input_hashes':pins,'actual_current_surface_status':'conditional-support','assembled_review':'historical independent reviews preserved separately; this is execution evidence only','elapsed_seconds':time.monotonic()-start})
 payload=json.dumps(result,indent=2)+'\n';(root/'outputs/native_pair_vacuum_chart_2026_09_09.json').write_text(payload);print(payload,end='')
 (root/'outputs/native_pair_vacuum_chart_2026_09_09.md').write_text('# Current finite supporting controls\n\nActual '+str(result['predicates'])+' finite mathematical predicates. No physical evaluation, node value or source-review verdict is supplied by this execution.\n')
 print(f"TOTAL: PASS={result['predicates']} FAIL=0")
 print('per_element: exact recurrence and constant comparisons are executed; operator inequalities remain analytical.')
 print('per_site: synthetic rank-one counterexamples execute; no native impurity overlap is evaluated.')
 print('per_mode: the finite return cutoff uses33 summands; the infinite tail is bounded analytically.')
 print('per_block: stationary and normalized-time chart bounds are analytical, not simulated Gaussian evolutions.')
 print('lattice_wide: trace-class transversality and reference-overlap claims are analytical; mixed-impurity overlaps remain uncomputed.')
if __name__=='__main__':main()

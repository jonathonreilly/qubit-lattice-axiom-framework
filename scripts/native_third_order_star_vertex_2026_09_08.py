"""Portable exact saved-residual and two-mode checks; no physical solves."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE_2026-09-08.md',
 'scripts/native_third_order_star_vertex_replay_2026_09_08.py',
 'scripts/native_third_order_star_vertex_two_mode_2026_09_08.py',
 'docs/work_history/repo/review_feedback/pr8058-evidence/kept/pr8058-INPUTS-746fd36863573c71.json',
 'docs/work_history/repo/review_feedback/pr8058-evidence/kept/pr8058-RESULT-8a461aeeaa3aae41.json',
 'docs/work_history/repo/review_feedback/pr8058-evidence/kept/pr8058-SOLVE_VECTORS-8740fc5cfce5142d.json',
 'docs/NATIVE_WEAK_ELECTRIC_SPECTATOR_GAP_NOTE_2026-09-08.md',
)
def main():
 import argparse,json,hashlib,importlib.util,signal,time,resource,sys
 from pathlib import Path
 p=argparse.ArgumentParser();p.add_argument('--json',action='store_true');args=p.parse_args()
 signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS}
 spec=importlib.util.spec_from_file_location('vertex_replay',root / 'scripts' / 'native_third_order_star_vertex_replay_2026_09_08.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 replay=module.check(root)
 spec=importlib.util.spec_from_file_location('vertex_two_mode',root / 'scripts' / 'native_third_order_star_vertex_two_mode_2026_09_08.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 two=module.check()
 if replay['checks']!=32 or two['checks']!=7:raise ValueError('predicate group coverage')
 # Live cross-path comparison: direct CAR residual-derived weight vs two-mode inverse.
 from fractions import Fraction
 alpha=Fraction(two['direct_two_mode_cases'][0]['alpha'])
 if Fraction(replay['particle_weights']['1'])!=alpha*alpha or any(Fraction(replay['particle_weights'][str(k)]) for k in (3,5)):raise ValueError('independent vertex equality')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise RuntimeError('384MiB RSS')
 result=dict(status='PASS',checks=40,replay=replay,two_mode=two,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_bytes=rss,scope='39 helper predicate groups plus1 cross-path comparison; no new physical solve, bulk or full-sixth inference')
 (root/'scripts/native_third_order_star_vertex_2026_09_08.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
 if not args.json:
  print('per_element: exact saved rational residuals reconstructed from literal ordered CAR actions; no new physical solves.')
  print('per_site: the delivered one-star L4 active space and its recorded source/neighbor geometry are replayed.')
  print('per_mode: four quadratic-field inverse cases and two absolute coefficients are executed as declared.')
  print('per_block: thirty saved residual vectors, decomposition, singleton normalization and cross-path equality are checked.')
  print('lattice_wide: only the declared local L4 channel is replayed; general reconstruction is analytical, with no full-sixth or bulk conclusion.')
  print('TOTAL: PASS=40 FAIL=0')
if __name__=='__main__':main()

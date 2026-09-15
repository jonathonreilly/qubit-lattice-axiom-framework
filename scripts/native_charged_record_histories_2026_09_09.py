"""Portable exact finite controls; no physical stochastic run."""
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_CHARGED_RECORD_HISTORIES_NOTE_2026-09-09.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md',
 'scripts/native_charged_record_history_controls_2026_09_09.py',
 'scripts/native_charged_record_history_car_2026_09_09.py',
)
def main():
 import argparse,json,hashlib,time,signal,resource,sys,importlib.util
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(30);t=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in AUDIT_INPUT_PATHS};results=[]
 def load_helper(path):
  data=path.read_bytes()
  if hashlib.sha256(data).hexdigest()!=hashes[str(path.relative_to(root))]:raise ValueError('source changed')
  spec=importlib.util.spec_from_file_location(path.stem,path)
  module=importlib.util.module_from_spec(spec)
  spec.loader.exec_module(module)
  return module
 results=[
  load_helper(root / 'scripts' / 'native_charged_record_history_controls_2026_09_09.py').check(),
  load_helper(root / 'scripts' / 'native_charged_record_history_car_2026_09_09.py').check(),
 ]
 if results[0]['status']!='PASS' or results[0]['history_columns']!=736 or results[0]['omitted_phase_mutant_failures']!=80 or results[1]['checks']!=146:raise ValueError('coverage')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
 if sys.platform!='darwin':rss*=1024
 if rss>384*1048576 or time.monotonic()-t>=30:raise ValueError('resource cap')
 print(json.dumps(dict(status='PASS',actual_current_surface_status='conditional-support',controls=results,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-t,peak_rss_bytes=rss),indent=2))
 if not args.json:
  print('TOTAL: PASS=2 FAIL=0')
  print('per_element: executed 416 exact one-edge native carrier columns and 146 CAR/refinement checks; repeated structural predicates remain separately counted in the payload.')
  print('per_site: executed finite endpoint particle-hole conjugation, transported number, and dephasing-versus-discard controls.')
  print('per_mode: executed finite exact CAR algebra only; no spectral-mode census or continuum dynamics computed.')
  print('per_block: executed 736 two-edge history columns on the triangle, path and chorded square under both neighbor orders; the separate one-edge omitted-phase control rejects 80 columns.')
  print('lattice_wide: checked and not executed; the arbitrary finite-graph statement follows from the written algebra. No physical stochastic run, large lattice dynamics or empirical experiment executed.')
if __name__=='__main__':main()

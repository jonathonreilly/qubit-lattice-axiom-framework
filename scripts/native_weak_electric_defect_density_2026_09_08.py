"""Exact local controls for the supplied-model weak-electric density theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_WEAK_ELECTRIC_DEFECT_DENSITY_NOTE_2026-09-08.md',
 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'scripts/native_weak_electric_defect_density_controls_2026_09_08.py',
)
def main():
 import argparse,json,hashlib,importlib.util,signal,time,resource,sys
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 inputs={x:hashlib.sha256((root/x).read_bytes()).hexdigest() for x in AUDIT_INPUT_PATHS}
 spec=importlib.util.spec_from_file_location('density_controls',root / 'scripts' / 'native_weak_electric_defect_density_controls_2026_09_08.py');module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 result=module.check()
 if result['checks']!=107 or result['quadratic_checks']!=43 or result['thermal_checks']!=108 or result['total_checks']!=258 or result['ground_density_coefficient']!='102400/387' or result['thermal_density_coefficient']!='800':raise ValueError('claim-local controls')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise RuntimeError('384MiB RSS')
 result.update(input_sha256=inputs,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,scope='Exact local controls supporting the separate full analytical theorem; no perturbed-state solve or phase claim.')
 (root/'outputs/native_weak_electric_defect_density_2026_09_08.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
 if not args.json:
  print('per_element: executed exact local electric and rational inequality controls on the declared finite states.')
  print('per_site: incident-pair and defect-face multiplicities are checked on the stated local geometries.')
  print('per_mode: finite rational anticommutation-bound and quadratic-root controls are executed without state solves.')
  print('per_block: all258 named local, quadratic and thermal algebra controls are executed as declared.')
  print('lattice_wide: volume-uniform ground/Gibbs density bounds are analytical; no perturbed-state or Gibbs sampling run occurs.')
  print('TOTAL: PASS=258 FAIL=0')
if __name__=='__main__':main()

"""Exact controls for conditional supplied-model joint-defect theorems."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_WEAK_ELECTRIC_JOINT_DEFECT_BOUNDS_NOTE_2026-09-09.md',
 'docs/NATIVE_WEAK_ELECTRIC_DEFECT_DENSITY_NOTE_2026-09-08.md',
 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'scripts/native_weak_electric_joint_defect_controls_2026_09_09.py',
)
def main():
 import argparse,json,hashlib,signal,time,resource,sys,importlib.util
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args();signal.alarm(AUDIT_TIMEOUT_SEC);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 inputs={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
 path=root/'scripts/native_weak_electric_joint_defect_controls_2026_09_09.py';data=path.read_bytes();spec=importlib.util.spec_from_file_location('local_controls',root/'scripts/native_weak_electric_joint_defect_controls_2026_09_09.py');module=importlib.util.module_from_spec(spec);exec(compile(data,str(path),'exec'),module.__dict__);result=module.check()
 if result['status']!='PASS' or result['max_flipped']!=8 or result['face_terms']!=32:raise ValueError('claim binding')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise RuntimeError('memory cap')
 result.update(input_sha256=inputs,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,actual_current_surface_status='conditional-support')
 (root/'outputs/native_weak_electric_joint_defect_bounds_2026_09_09.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
 if not args.json:
  print(f"TOTAL: PASS={result['total_checks']} FAIL=0")
  print('per_element: exact local geometry and electric-pair face flips are checked on L4 and L6 tori.')
  print('per_site: every finite test face has its complete incident electric-pair count checked.')
  print('per_mode: no active-mode spectrum is computed; small commuting-projector selections are exact.')
  print('per_block: integer stopping thresholds and finite recursion controls use exact rational arithmetic.')
  print('lattice_wide: general joint bounds are analytical; no perturbed ground state or thermal sample is computed.')
if __name__=='__main__':main()

"""Portable exact support for the infinite native node calculation framework."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
'docs/NATIVE_INFINITE_STAR_NODE_REDUCTION_NOTE_2026-09-09.md',
'docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md',
'docs/NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md',
'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md',
'scripts/native_infinite_star_node_algebra_2026_09_09.py',
'scripts/native_infinite_star_node_shift_2026_09_09.py',
'scripts/native_infinite_star_node_gap_2026_09_09.py',
'scripts/native_infinite_star_node_orbits_tail_2026_09_09.py')
def main():
 import argparse,json,hashlib,signal,time,resource,io,contextlib,sys
 import importlib.util
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(180);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS};groups={}
 def execute_helper(spec,path):
  file=root/path;data=file.read_bytes();module=importlib.util.module_from_spec(spec);capture=io.StringIO()
  with contextlib.redirect_stdout(capture):exec(compile(data,str(file),'exec'),module.__dict__)
  groups[Path(path).stem]=json.loads(capture.getvalue())
 execute_helper(importlib.util.spec_from_file_location('controlled_helper',root/'scripts/native_infinite_star_node_algebra_2026_09_09.py'),'scripts/native_infinite_star_node_algebra_2026_09_09.py')
 execute_helper(importlib.util.spec_from_file_location('controlled_helper',root/'scripts/native_infinite_star_node_shift_2026_09_09.py'),'scripts/native_infinite_star_node_shift_2026_09_09.py')
 execute_helper(importlib.util.spec_from_file_location('controlled_helper',root/'scripts/native_infinite_star_node_gap_2026_09_09.py'),'scripts/native_infinite_star_node_gap_2026_09_09.py')
 execute_helper(importlib.util.spec_from_file_location('controlled_helper',root/'scripts/native_infinite_star_node_orbits_tail_2026_09_09.py'),'scripts/native_infinite_star_node_orbits_tail_2026_09_09.py')
 node,shift,gap,tail=groups.values()
 if node['status']!='PASS' or shift['status']!='PASS' or tail['status']!='PASS' or not gap['both_gap_lower_exceed_1_4']:raise ValueError('helper status')
 counts={'little_group':node['checks'],'shift_entries_and_vacuum':shift['entry_checks']+shift['two_inverse_vacuum_check'],'return_and_gap':5,'orbits_and_tail':tail['checks']}
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise ValueError('memory cap')
 out={'status':'PASS','checks':sum(counts.values()),'predicate_groups':counts,'groups':groups,'input_sha256':hashes,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':rss,'physical_runs':0,'actual_current_surface_status':'conditional-support','alpha_evaluated':False}
 payload=json.dumps(out,indent=2)+'\n';(root/'outputs/native_infinite_star_node_reduction_2026_09_09.json').write_text(payload);print(payload,end='')
 print(f"TOTAL: PASS={out['checks']} FAIL=0")
 print('per_element: finite integer Clifford and rational shifted-resolvent predicates are executed on declared fixtures.')
 print('per_site: exact ordered-pair symmetry orbits are enumerated; infinite node extraction remains analytical.')
 print('per_mode: exact return and logarithmic inequalities are checked; no native node scalar is evaluated.')
 print('per_block: finite rational gap and imaginary-time tail certificates execute, without pointwise kernel quadrature.')
 print('lattice_wide: infinite impurity gap and Gaussian GNS limits are analytical; no finite-size threshold or interacting phase is computed.')
if __name__=='__main__':main()

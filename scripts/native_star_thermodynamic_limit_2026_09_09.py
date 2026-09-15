"""Portable supporting controls for the uniform quasi-local star theorem."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md', 'docs/NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'docs/NATIVE_UNIFORM_CUBIC_FLUX_DEFECT_STIFFNESS_NOTE_2026-09-08.md', 'scripts/native_star_thermodynamic_controls_2026_09_09.py')
def main():
 import argparse,json,hashlib,signal,time,resource,sys
 import importlib.util
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(180);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
 helper=root/'scripts/native_star_thermodynamic_controls_2026_09_09.py';data=helper.read_bytes()
 spec=importlib.util.spec_from_file_location('controls',root/'scripts/native_star_thermodynamic_controls_2026_09_09.py')
 module=importlib.util.module_from_spec(spec);exec(compile(data,str(helper),'exec'),module.__dict__);out=module.check()
 if out['status']!='PASS':raise ValueError('claim binding')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise ValueError('memory cap')
 out.update(input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,actual_current_surface_status='conditional-support')
 payload=json.dumps(out,indent=2)+'\n';(root/'outputs/native_star_thermodynamic_limit_2026_09_09.json').write_text(payload);print(payload,end='')
 print(f"TOTAL: PASS={out['checks']} FAIL=0")
 print('per_element: exact finite CAR quadratic commutator predicates are executed on the declared three-mode matrices.')
 print('per_site: finite hopping-path boundary independence is executed for L8, L12 and L16 at the declared orders.')
 print('per_mode: finite exact weighted-tail arithmetic is executed; smooth coefficient-symbol convergence is analytical.')
 print('per_block: local Gaussian state and cocycle limits are analytical; no infinite-volume resolvent is numerically evaluated.')
 print('lattice_wide: the GNS core and wrong-pair gap argument is analytical; no interacting phase or nodal value is computed.')
if __name__=='__main__':main()

"""Supporting finite controls for the analytic full odd-star infrared theorem."""
AUDIT_TIMEOUT_SEC=30
AUDIT_INPUT_PATHS=('docs/NATIVE_FULL_STAR_INFRARED_RESPONSE_NOTE_2026-09-09.md', 'docs/NATIVE_STAR_THERMODYNAMIC_LIMIT_NOTE_2026-09-09.md', 'docs/NATIVE_UNIFORM_QUASILOCAL_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md', 'scripts/native_full_star_infrared_controls_2026_09_09.py')
def main():
 import argparse,json,hashlib,signal,time,resource,sys
 import importlib.util
 from pathlib import Path
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.parse_args();signal.alarm(30);start=time.monotonic();root=Path(__file__).resolve().parents[1]
 hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
 helper=root/'scripts/native_full_star_infrared_controls_2026_09_09.py';data=helper.read_bytes()
 spec=importlib.util.spec_from_file_location('controls',root/'scripts/native_full_star_infrared_controls_2026_09_09.py')
 module=importlib.util.module_from_spec(spec);exec(compile(data,str(helper),'exec'),module.__dict__);out=module.record
 if out['FAIL'] or out['PASS']!=1217:raise ValueError('supporting control count')
 rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)
 if rss>384*1048576:raise ValueError('memory cap')
 out.update(status='PASS',input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),elapsed_seconds=time.monotonic()-start,peak_rss_bytes=rss,actual_current_surface_status='conditional-support')
 payload=json.dumps(out,indent=2)+'\n';(root/'outputs/native_full_star_infrared_response_2026_09_09.json').write_text(payload);print(payload,end='')
 print(f"TOTAL: PASS={out['PASS']} FAIL={out['FAIL']}")
 print('per_element: exact finite CAR and graded-commutator predicates are executed on the declared four-mode fixture.')
 print('per_site: finite graded Gram and rational spatial-exponent controls are executed; all-volume spatial bounds are analytical.')
 print('per_mode: occupation counting and inverse-moment controls are executed; conical native mode counting is analytical.')
 print('per_block: one-particle subtraction and the one-sided filter are checked in the finite fixture, not on every native block.')
 print('lattice_wide: spectral limits and uniform singleton row bounds are analytical; no native physical or interacting calculation is run.')
if __name__=='__main__':main()

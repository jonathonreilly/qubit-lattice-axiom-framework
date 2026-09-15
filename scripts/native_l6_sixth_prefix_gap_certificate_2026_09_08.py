"""Complete exact declared-support certificate replay; no new solves."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 'docs/NATIVE_L6_SIXTH_PREFIX_GAP_CERTIFICATE_NOTE_2026-09-08.md',
 'docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md',
 'docs/NATIVE_ZERO_PENALTY_OPTIMAL_FLUX_DISPERSION_NOTE_2026-09-08.md',
 'scripts/native_l6_sixth_prefix_gap_arithmetic_2026_09_08.py',
 'scripts/native_l6_sixth_prefix_gap_geometry_2026_09_08.py',
 'docs/work_history/repo/review_feedback/pr8059-evidence/kept/pr8059-ADJACENT_CENSUS-678691e77473f39d.json',
 'docs/work_history/repo/review_feedback/pr8059-evidence/kept/pr8059-NONADJACENT_CENSUS-e1706553032432f1.json',
 'docs/work_history/repo/review_feedback/pr8059-evidence/kept/pr8059-ADJACENT_COMPLETE-1cbe308dc1f7dcc7.json',
 'docs/work_history/repo/review_feedback/pr8059-evidence/kept/pr8059-NONADJACENT_ROWS-3586b7f01bc15347.json',
 'docs/work_history/repo/review_feedback/pr8059-evidence/kept/pr8059-TARGETS-ff56893c03dca52b.json',
)
def main():
 import argparse,json,hashlib,importlib.util,signal,time,resource,sys
 from pathlib import Path
 from fractions import Fraction as F
 from math import isqrt
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');args=ap.parse_args()
 signal.alarm(175);start=time.monotonic();root=Path(__file__).resolve().parents[1];rows=[];current_case=None
 def guard():
  if time.monotonic()-start>=175 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024)>384*1048576:raise RuntimeError('175s384MiB supplemental guard')
 def read(i):return json.loads((root/AUDIT_INPUT_PATHS[i]).read_text())
 try:
  hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
  spec=importlib.util.spec_from_file_location('gap_arithmetic',root/'scripts/native_l6_sixth_prefix_gap_arithmetic_2026_09_08.py');core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)
  spec=importlib.util.spec_from_file_location('gap_geometry',root/'scripts/native_l6_sixth_prefix_gap_geometry_2026_09_08.py');geom=importlib.util.module_from_spec(spec);spec.loader.exec_module(geom)
  adj,non,old_adj,old_non,target=[read(i) for i in range(6,11)];cases=target['cases']
  if [int(c['mask']) for c in cases]!=sorted(int(c['mask']) for c in cases):raise ValueError('numeric target order')
  geometry=geom.check(adj,non,cases,old_adj,old_non);guard()
  B,R,bi,wi=core.baseline(adj);guard()
  for case in cases:
   current_case=case
   if case['singleton'] is not None:gap=F(2*isqrt(3*10**60),10**30);bits=None;method='fixed initial parity singleton'
   else:gap,bits=core.gap(int(case['mask']),case['center'],adj,B,R,bi,wi);method='exact full-trace Newton/Woodbury'
   equality=gap==F(case['gap_lower']);floor=gap>F(1,3)
   rows.append(dict(mask=case['mask'],center=case['center'],singleton=case['singleton'],gap_lower=str(gap),denominator_bits=bits,equality=equality,above_common_floor=floor,method=method))
   if not equality or not floor:raise ValueError('actual rational source equality/common floor')
   guard()
  if len(rows)!=6489:raise ValueError('full coverage')
  payload=dict(status='PASS',certificate_groups=6489,geometry=geometry,minimum=str(min(F(r['gap_lower']) for r in rows)),common_floor='1/3',native_units='|t|=1; scale gap by |t|, h=2|t|',rows=rows,input_sha256=hashes,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-start,rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*(1 if sys.platform=='darwin' else 1024),scope='six declared supports only; no coefficient, all-flux or bulk claim')
  (root/'outputs/native_l6_sixth_prefix_gap_certificate_2026_09_08.json').write_text(json.dumps(payload,indent=2)+'\n')
  print(json.dumps({k:v for k,v in payload.items() if k!='rows'},indent=2))
  if not args.json:
   print('TOTAL: PASS=6489 FAIL=0')
   print('per_element: exact prefix geometry covers only the six declared finite L6 supports.')
   print('per_mode: every declared proper mask has its fixed-parity rational denominator bound checked.')
   print('per_site: saved finite-support coverage is checked; no boundary ensemble is sampled.')
   print('per_block: no half-slab field or stochastic slab evolution is executed by this certificate.')
   print('lattice_wide: all6489 declared proper masks replay; no all-flux or all-volume enumeration.')
 except BaseException as e:
  print(json.dumps(dict(status='FAILED',error=repr(e),current_case=current_case,completed_or_failed_rows=rows,seconds=time.monotonic()-start)),flush=True);raise
if __name__=='__main__':main()

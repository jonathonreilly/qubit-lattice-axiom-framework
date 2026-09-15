"""Canonical full saved-candidate replay; no solves. Explicit readiness mode is historical only."""
import argparse,gzip,hashlib,importlib.util,json,os,resource,signal,sys,tempfile,time
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs'
PREFIX='native_l6_nonlinear_vertex_'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=('docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md', 'docs/NATIVE_L6_NONLINEAR_STAR_VERTEX_NOTE_2026-09-09.md', 'docs/NATIVE_L6_SIXTH_PREFIX_GAP_CERTIFICATE_NOTE_2026-09-08.md', 'docs/NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md', 'docs/NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/_objects/bbddcf8229a92a19408caa0a829ef716c44767985f8402af334c95c155b230f8.gz', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/_objects/c4300e00d5515452727a9697575ef4af531bf220d58c67f3a869f98281fc2a22.gz', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-adapted_frame-4eb81c02792f3306.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-four_solve-eff578cafd7f48f7.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-projection-e801411de605cecc.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_error-57d49d5cf78c0e3e.md', 'docs/work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_sign-c2692f5746303191.md', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/ADAPTED.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/BLOCKS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/COEFFICIENTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/LEDGER.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/SOURCE_MANIFEST.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/TRANSPORTS.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/VECTOR_MANIFEST.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/INDEPENDENT_REVIEW.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/RESULT.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/ROOT_ACCEPTANCE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/WORKER_COMPLETE.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/firstP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondO_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/secondP_candidate.json', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/chi_real.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/firstP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/secondP.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceO.npy.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.bin.gz', 'outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/vectors/sourceP.npy.gz', 'scripts/native_l6_nonlinear_star_vertex_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_envelope_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_fp_guard_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_geometry_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_review_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_transport_2026_09_09.py', 'scripts/native_l6_nonlinear_vertex_validate_coefficients_2026_09_09.py')

def require(x,s):
 if not x:raise ValueError(s)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pins():
 m=json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())
 for p,h in m.items():require(sha(ROOT/p)==h,'source '+p)
 return m

def load_canonical_geometry():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_geometry_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('canonical_geometry',ROOT/'scripts/native_l6_nonlinear_vertex_geometry_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['canonical_geometry']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def load_envelope():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_envelope_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('envelope',ROOT/'scripts/native_l6_nonlinear_vertex_envelope_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['envelope']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def load_transport():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_transport_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('transport',ROOT/'scripts/native_l6_nonlinear_vertex_transport_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['transport']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def load_fp_guard():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_fp_guard_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('fp_guard',ROOT/'scripts/native_l6_nonlinear_vertex_fp_guard_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['fp_guard']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def load_validate_coefficients():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_validate_coefficients_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('validate_coefficients',ROOT/'scripts/native_l6_nonlinear_vertex_validate_coefficients_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['validate_coefficients']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m

def load_canonical_replay():
 p=ROOT/'scripts/native_l6_nonlinear_vertex_review_2026_09_09.py';data=p.read_bytes()
 require(hashlib.sha256(data).hexdigest()==json.loads((INPUT/'SOURCE_MANIFEST.json').read_text())[str(p.relative_to(ROOT))],'verified source bytes')
 spec=importlib.util.spec_from_file_location('canonical_replay',ROOT/'scripts/native_l6_nonlinear_vertex_review_2026_09_09.py');m=importlib.util.module_from_spec(spec);sys.modules['canonical_replay']=m;exec(compile(data,str(p),'exec'),m.__dict__);m.P=INPUT
 return m


def claims(result, factor=F(1)):
 require(result.get('status')=='PASS' and result.get('scientific_pass') is True,'certificate passed')
 w=list(map(F,result['particle_intervals']['all_ge3']));w=[x*factor for x in w]
 require(F('0.001921920169')<w[0]<=w[1]<F('0.001921920178'),'rounded higher-sector enclosure')
 require(F('0.04383')**2<w[0] and w[1]<F('0.04384')**2,'distance enclosure')
 require(F(result['Echi'])<=F('0.00000000004825'),'rounded error')
 for n in ('3','5','7'):require(F(result['particle_intervals'][n][0])>0,'positive '+n)
 require([result[k] for k in ('full_vectors','fresh_residuals','transports','exact_norm_scans')]==[7,4,27,9],'full coverage')
 return {'squared_distance_strict_decimal':['0.001921920169','0.001921920178'],'distance_strict_decimal':['0.04383','0.04384'],'full_linear_modes':108,'positive_particle_sectors':[3,5,7]}

def execution_environment():
 np=sys.modules['numpy'];native={}
 for name,module in list(sys.modules.items()):
  origin=getattr(module,'__file__',None)
  if name.startswith('numpy.') and origin and Path(origin).suffix in ('.so','.dylib','.pyd'):
   native[origin]=sha(origin)
 return dict(python_executable=sys.executable,python_version=sys.version,python_sha256=sha(sys.executable),numpy_origin=np.__file__,numpy_version=np.__version__,numpy_sha256=sha(np.__file__),numpy_native_sha256=native)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--json',action='store_true');ap.add_argument('--verify',action='store_true');ap.add_argument('--readiness-only',action='store_true');args=ap.parse_args()
 require(not (args.verify and args.readiness_only),'incompatible verify/readiness flags')
 if not (sys.flags.isolated and sys.flags.dont_write_bytecode) or any(os.environ.get(k)!='1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')):
  env=dict(os.environ);env.update({k:'1' for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS')});os.execve(sys.executable,[sys.executable,'-I','-B',str(Path(__file__).resolve()),*sys.argv[1:]],env)
 require(sys.flags.isolated and sys.flags.dont_write_bytecode,'use -I -B')
 for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):require(os.environ.get(k)=='1','single thread '+k)
 start=time.monotonic();signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('audit timeout')));signal.alarm(AUDIT_TIMEOUT_SEC)
 output=ROOT/'outputs/native_l6_nonlinear_star_vertex_2026_09_09.json';stage='pins';diagnostics=Path(tempfile.mkdtemp(prefix='l6-replay-failure-'))
 try:
  candidate_diagnostics=Path(os.environ.get('REVIEW_CAPTURE_DIAGNOSTICS') or diagnostics).resolve()
  require(not candidate_diagnostics.is_relative_to(ROOT),'diagnostics must be outside repository input ancestors');candidate_diagnostics.mkdir(parents=True,exist_ok=True);diagnostics=candidate_diagnostics
  manifest=pins();geometry=load_canonical_geometry().check(INPUT)
  imported={}
  imported['envelope']=load_envelope()
  imported['transport']=load_transport()
  imported['fp_guard']=load_fp_guard()
  imported['validate_coefficients']=load_validate_coefficients()
  imported['canonical_replay']=load_canonical_replay()
  accepted=json.loads((INPUT/'accepted/INDEPENDENT_REVIEW.json').read_text())
  report=accepted
  receipt=json.loads((INPUT/'accepted/ROOT_ACCEPTANCE.json').read_text())
  require(receipt['accepted'] is True and receipt['status']=='PASS','root acceptance')
  for key,name in [('production_result_sha256','RESULT.json'),('independent_replay_sha256','INDEPENDENT_REVIEW.json'),('worker_complete_sha256','WORKER_COMPLETE.json')]:require(receipt[key]==sha(INPUT/'accepted'/name),'accepted binding '+key)
  require(receipt['Echi']==report['Echi'] and receipt['particle_intervals']==report['particle_intervals'],'accepted certificate binding')
  rounded=claims(report)
  if args.readiness_only:
   print(json.dumps({'status':'READINESS_ONLY','geometry':geometry,'rounded_accepted_evidence':rounded,'physical_replay_executed':False}));return
  with tempfile.TemporaryDirectory(prefix='l6-certificate-') as temp:
   folder=Path(temp)
   for p in (INPUT/'accepted').glob('*'):
    if p.name=='RESULT.json' or p.name.endswith('_candidate.json'):(folder/p.name).write_bytes(p.read_bytes())
   vm=json.loads((INPUT/'VECTOR_MANIFEST.json').read_text())
   rows=vm if isinstance(vm,list) else vm['files']
   for row in rows:
    source=INPUT/row['compressed'];require(sha(source)==row['gzip_sha256'],'compressed hash')
    target=folder/row['name']
    with gzip.open(source,'rb') as src,target.open('wb') as dst:
     for b in iter(lambda:src.read(1048576),b''):dst.write(b)
    require(target.stat().st_size==row['bytes'] and sha(target)==row['sha256'],'decompressed hash')
   def progress(s,**detail):
    nonlocal stage
    stage=s;(diagnostics/'PROGRESS.json').write_text(json.dumps(dict(stage=s,detail=detail,seconds=time.monotonic()-start),indent=2)+'\n')
   actual=imported['canonical_replay'].replay(folder,progress)
  require(actual['Echi']==report['Echi'] and actual['particle_intervals']==report['particle_intervals'],'accepted exact payload')
  rounded=claims(actual);require(pins()==manifest,'post source closure');peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
  if sys.platform!='darwin':peak*=1024
  require(peak<384*1048576 and time.monotonic()-start<180,'resource cap')
  output.write_text(json.dumps(dict(status='PASS',scope='finite L6 supplied-model vacuum image',runtime_environment=execution_environment(),diagnostics_path=str(diagnostics),geometry=geometry,replay=actual,claims=rounded,input_hashes=manifest,seconds=time.monotonic()-start,peak_bytes=peak),indent=2)+'\n');print(output.read_text())
  if not args.json:
   print('TOTAL: PASS=8 FAIL=0')
   print('per_element: actual saved-candidate replay is restricted to the declared finite L6 star support.')
   print('per_mode: the complete108-mode linear vacuum-action comparison is certified by the stated projection proof.')
   print('per_site: seven saved full vectors are replayed; no new candidate sampling or solve is performed.')
   print('per_block: no half-slab simulation is executed; four fresh residuals certify the saved vectors.')
   print('lattice_wide: the supplied finite L6 certificate is replayed; no all-volume interacting claim is tested.')
 except BaseException as e:
  failure=diagnostics/'FAILED.json';failure.write_text(json.dumps(dict(status='FAIL',stage=stage,error=repr(e),seconds=time.monotonic()-start),indent=2)+'\n');raise
 finally:signal.alarm(0)
if __name__=='__main__':main()

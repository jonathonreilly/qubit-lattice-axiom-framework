#!/usr/bin/env python3
"""Source-bound exact controls for the immutable transverse-curl theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_immutable_transverse_curl_limits_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-transverse-waves-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(
 ('immutable_transverse_maxwell_check.py','IMMUTABLE_TRANSVERSE_MAXWELL_RESULTS.json',38),
 ('maxwell_polar_axial_symmetry_check.py','MAXWELL_POLAR_AXIAL_SYMMETRY_RESULTS.json',13),
 ('maxwell_entropy_energy_check.py','MAXWELL_ENTROPY_ENERGY_RESULTS.json',15),
 ('maxwell_formation_full_occupancy_check.py','MAXWELL_FORMATION_FULL_OCCUPANCY_RESULTS.json',21),
 ('gauss_preparation_check.py','GAUSS_PREPARATION_RESULTS.json',3),
)
AUDIT_INPUT_PATHS=(NOTE,'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 *(CHECK_DIRECTORY+'/'+name for name,_,_ in SUITES))
# Mutations alter one load-bearing calculation or proposed formula. Each must
# be rejected by another identity; the control expectations are not rewritten.
MUTATIONS={
 'drop_context_term':(SUITES[0][0],'S2[i,l,a]+S2[i,a,r]-S2[i,l,z]-S2[i,z,r]','S2[i,l,a]-S2[i,l,z]-S2[i,z,r]'),
 'omit_current_mean_subtraction':(SUITES[0][0],'np.cross(e,Y)+np.cross(X,b))-2*XY','np.cross(e,Y)+np.cross(X,b))-0*XY'),
 'wrong_cube_normalization':(SUITES[0][0],'b=np.vstack((np.zeros((7,3),dtype=np.int64),cubes))','b=np.vstack((np.zeros((7,3),dtype=np.int64),2*cubes))'),
 'reverse_curl_sign':(SUITES[0][0],'expected[2:5,5:8]=-gamma*rA*CK/3','expected[2:5,5:8]=gamma*rA*CK/3'),
 'discard_static_modes':(SUITES[0][0],'polynomial.gen**10*(polynomial.gen**2-speed2)**2','polynomial.gen**8*(polynomial.gen**2-speed2)**2'),
 'polar_instead_of_axial':(SUITES[1][0],'R@e[a],determinant*R@b[a]','R@e[a],R@b[a]'),
 'omit_odd_triple_parity':(SUITES[1][0],'[1,1,1,1,1,-1,-1,-1,1,1,1,1,1,-1]','[1,1,1,1,1,-1,-1,-1,1,1,1,1,1,1]'),
 'wrong_energy_coefficient':(SUITES[2][0],'expected=3*(X.dot(X))/(2*rA)','expected=3*(X.dot(X))/rA'),
 'drop_stress_divergence_defect':(SUITES[2][0],'defect+electric*s.trace(dE)+magnetic*s.trace(dB)','defect'),
 'omit_formation_noise':(SUITES[3][0],'Q=beta*p0*s.eye(14)','Q=s.zeros(14)'),
 'wrong_full_occupancy_mode_count':(SUITES[3][0],'target=lam**9*','target=lam**10*'),
 'reverse_cross_covariance_sign':(SUITES[3][0],'off=s.I*s.sin(angle)*Ck/kmag','off=-s.I*s.sin(angle)*Ck/kmag'),
 'restore_conditioned_longitudinal_variance':(SUITES[4][0],'conditioned=s.eye(6)-G.T*(G*G.T).inv()*G','conditioned=s.eye(6)'),
}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main(args):
 identities={path:sha(ROOT/path) for path in AUDIT_INPUT_PATHS}
 identities[str(Path(__file__).resolve().relative_to(ROOT))]=sha(Path(__file__))
 note=' '.join((ROOT/NOTE).read_text().split())
 assert CLAIM_ID in note and 'no independent audit verdict' in note
 assert 'not a derivation from' in note and 'source-free' in note
 assert 'A site never carries more than one record; records are permanent.' in ' '.join((ROOT/AUDIT_INPUT_PATHS[1]).read_text().split())
 print('PASS: declared_sources_and_conditional_scope',flush=True)
 records=[];total=1
 with tempfile.TemporaryDirectory(prefix='immutable-transverse-controls-') as directory:
  temporary=Path(directory)
  for filename,resultfile,count in SUITES:
   if args.mutation and filename!=MUTATIONS[args.mutation][0]:continue
   source=(ROOT/CHECK_DIRECTORY/filename).read_text()
   if args.mutation:
    _,old,new=MUTATIONS[args.mutation]
    assert source.count(old)==1,(args.mutation,'nonunique mutation target')
    source=source.replace(old,new,1)
   copied=temporary/filename;copied.write_text(source)
   env=os.environ.copy();env['OPENBLAS_NUM_THREADS']='1'
   run=subprocess.run([sys.executable,str(copied)],cwd=temporary,env=env,text=True,capture_output=True,timeout=240)
   record=dict(suite=filename,source_sha256=identities[CHECK_DIRECTORY+'/'+filename],
               executed_source_sha256=sha(copied),returncode=run.returncode,stdout=run.stdout,stderr=run.stderr)
   records.append(record)
   if run.returncode:
    report=dict(claim_id=CLAIM_ID,identities=identities,mutation=args.mutation,passed=False,suites=records)
    if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print('FAIL:',filename,run.stderr.splitlines()[-1] if run.stderr else 'child exited unsuccessfully',flush=True)
    return 1
   data=json.loads((temporary/resultfile).read_text());record['results']=data
   assert data['source_sha256']==sha(copied)
   assert len(data['checks'])==count and all(c['passed'] for c in data['checks'])
   total+=count;print(f'PASS: {filename}: {count} exact controls',flush=True)
 assert identities=={path:sha(ROOT/path) for path in identities}
 report=dict(claim_id=CLAIM_ID,identities=identities,mutation=args.mutation,passed=True,
             control_count=total,suites=records,scope='Author finite and symbolic controls; not an independent audit or a replacement for the conditional proofs.')
 if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
 print(f'TOTAL: PASS={total} FAIL=0',flush=True)
 return 0

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output');parser.add_argument('--mutation',choices=tuple(MUTATIONS));parser.add_argument('--list-mutations',action='store_true')
 options=parser.parse_args()
 if options.list_mutations:print('\n'.join(MUTATIONS));raise SystemExit(0)
 try:raise SystemExit(main(options))
 except Exception as error:
  print('FAIL:',type(error).__name__,str(error),flush=True)
  raise SystemExit(1)

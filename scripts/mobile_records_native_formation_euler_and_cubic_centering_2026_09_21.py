#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the native formation and cubic-centering theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_native_formation_euler_and_cubic_centering_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-native-formation-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(
 ('admissibility_formation_euler_check.py','ADMISSIBILITY_FORMATION_EULER_RESULTS.json',11),
 ('native_formation_centering_check.py','NATIVE_FORMATION_CENTERING_RESULTS.json',7),
 ('native_formation_energy_centering_check.py','NATIVE_FORMATION_ENERGY_CENTERING_RESULTS.json',6),
)
AUDIT_INPUT_PATHS=(
    'docs/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/MOBILE_RECORDS_IMMUTABLE_CONTEXT_EXCHANGE_ACOUSTIC_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
    '.claude/science/mobile-record-native-formation-20260921/author_checks/admissibility_formation_euler_check.py',
    '.claude/science/mobile-record-native-formation-20260921/author_checks/native_formation_centering_check.py',
    '.claude/science/mobile-record-native-formation-20260921/author_checks/native_formation_energy_centering_check.py',
)
# Mutations alter one load-bearing calculation or proposed formula. Each must
# be rejected by another identity; the control expectations are not rewritten.
MUTATIONS={
 'wrong_reaction_power':(SUITES[0][0],'B=s.Matrix([beta*p0*m**6 for m in mp])','B=s.Matrix([beta*p0*m**5 for m in mp])'),
 'wrong_adjoint_vacancy_sign':(SUITES[0][0],'q[a]*p0/p[a]-q0','q[a]*p0/p[a]+q0'),
 'half_linear_vector_source':(SUITES[0][0],'expected=s.diag(-6*beta,12*beta','expected=s.diag(-6*beta,6*beta'),
 'half_quadrupole_source':(SUITES[0][0],'quadratic-30*beta','quadratic-15*beta'),
 'wrong_cubic_vector_source':(SUITES[0][0],'12*j*g+40*j**3*g**3+12*j**5*g**5','12*j*g+20*j**3*g**3+12*j**5*g**5'),
 'half_relative_diffusion':(SUITES[1][0],'drift=2*kappa*side*lap.astype(float)','drift=kappa*side*lap.astype(float)'),
 'half_pair_source':(SUITES[1][0],'s2=csr_matrix(((4*beta/3)','s2=csr_matrix(((2*beta/3)'),
 'half_cubic_reward':(SUITES[1][0],'reward=csr_matrix((6*beta*v0*pairs)','reward=csr_matrix((3*beta*v0*pairs)'),
 'reverse_full_generator_quadratic_birth':(SUITES[1][0],'coefficients=[1,first+second,first*second]','coefficients=[1,first+second,-first*second]'),
 'omit_time_dependent_entropy_weights':(SUITES[2][0],'s.diff(energy,rho)*lam*v+','0+'),
 'omit_second_birth_endpoint':(SUITES[2][0],'s.factor(2*endpoint-4*beta','s.factor(endpoint-4*beta'),
 'wrong_Green_time_normalization':(SUITES[2][0],'15*(2*g0)-3','15*g0-3'),
}
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

def main(args):
 identities={path:sha(ROOT/path) for path in AUDIT_INPUT_PATHS}
 identities[str(Path(__file__).resolve().relative_to(ROOT))]=sha(Path(__file__))
 note=' '.join((ROOT/NOTE).read_text().split())
 assert CLAIM_ID in note and 'no independent audit verdict' in note, 'claim identity or audit boundary missing'
 assert 'not a derivation from' in note, 'supplied-model boundary missing'
 assert 'A site never carries more than one record; records are permanent.' in ' '.join((ROOT/AUDIT_INPUT_PATHS[1]).read_text().split())
 print('PASS: declared_sources_and_conditional_scope',flush=True)
 records=[];total=1
 with tempfile.TemporaryDirectory(prefix='native-formation-controls-') as directory:
  temporary=Path(directory)
  for filename,_,_ in SUITES:
   (temporary/filename).write_bytes((ROOT/CHECK_DIRECTORY/filename).read_bytes())
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
   total+=count;print(f'PASS: {filename}: {count} declared controls',flush=True)
 assert identities=={path:sha(ROOT/path) for path in identities}
 report=dict(claim_id=CLAIM_ID,identities=identities,mutation=args.mutation,passed=True,
             control_count=total,suites=records,scope='Author symbolic and finite numerical controls; not an independent audit or a replacement for the conditional proofs.')
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

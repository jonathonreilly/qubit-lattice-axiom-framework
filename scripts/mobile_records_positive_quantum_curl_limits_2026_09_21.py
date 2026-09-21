#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for supplied positive quantum curl limits.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_positive_quantum_curl_limits_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-positive-quantum-curl-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_POSITIVE_QUANTUM_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=1200
PRIMARY_SOURCES=('DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md', 'DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md', 'DIMER_EDGE_FACE_ENERGY_AND_GAUSS_MOMENT_ADDENDUM.md', 'DIMER_LOCAL_DILUTE_QUANTUM_CURL_LIMIT.md')
CHECKER_DEPENDENCIES=()
SUITES=(('dimer_finite_qubit_curl_check.py', 'dimer_finite_qubit_curl_checks/RESULTS.json', 3), ('dimer_edge_face_gauss_check.py', 'dimer_edge_face_gauss_checks/RESULTS.json', 4), ('dimer_local_dilute_curl_check.py', 'dimer_local_dilute_curl_checks/RESULTS.json', 3))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_POSITIVE_QUANTUM_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/primary_sources/DIMER_FINITE_QUBIT_POSITIVE_CURL_LIMIT.md',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/primary_sources/DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/primary_sources/DIMER_EDGE_FACE_ENERGY_AND_GAUSS_MOMENT_ADDENDUM.md',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/primary_sources/DIMER_LOCAL_DILUTE_QUANTUM_CURL_LIMIT.md',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/author_checks/dimer_finite_qubit_curl_check.py',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/author_checks/dimer_edge_face_gauss_check.py',
 '.claude/science/mobile-record-positive-quantum-curl-20260921/author_checks/dimer_local_dilute_curl_check.py')
MUTATIONS={'halve_dilute_commutator_bound': ('dimer_local_dilute_curl_check.py',
                                   'assert maxerr<=2*m/V+2e-14',
                                   'assert maxerr<=m/V+2e-14'),
 'omit_occupation_depletion': ('dimer_finite_qubit_curl_check.py',
                               's.Rational(n[mode]*(K-sum(n)+1),K)',
                               's.Integer(n[mode])'),
 'wrong_incidence_adjoint': ('dimer_edge_face_gauss_check.py',
                             'right=np.block([[np.zeros_like(C),C.T],[-C,np.zeros_like(C)]])',
                             'right=np.block([[np.zeros_like(C),C],[-C,np.zeros_like(C)]])')}
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
 with tempfile.TemporaryDirectory(prefix='positive-quantum-curl-controls-') as directory:
  temporary=Path(directory)
  for filename in PRIMARY_SOURCES:
   (temporary/filename).write_bytes((ROOT/EVIDENCE/'primary_sources'/filename).read_bytes())
  for filename in CHECKER_DEPENDENCIES:
   (temporary/filename).write_bytes((ROOT/CHECK_DIRECTORY/filename).read_bytes())
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
   run=subprocess.run([sys.executable,str(copied)],cwd=temporary,env=env,text=True,capture_output=True,timeout=900)
   record=dict(suite=filename,source_sha256=identities[CHECK_DIRECTORY+'/'+filename],
               executed_source_sha256=sha(copied),returncode=run.returncode,stdout=run.stdout,stderr=run.stderr)
   records.append(record)
   if run.returncode:
    report=dict(claim_id=CLAIM_ID,identities=identities,mutation=args.mutation,passed=False,suites=records)
    if args.output:Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    print('FAIL:',filename,run.stderr.splitlines()[-1] if run.stderr else 'child exited unsuccessfully',flush=True)
    return 1
   data=json.loads((temporary/resultfile).read_text());record['results']=data
   bound=data.get('sources_sha256',data.get('sources'))
   if isinstance(bound,list):
    mapping={Path(row['path']).name:row['sha256'] for row in bound}
    assert all(sha(temporary/Path(row['path']).name)==row['sha256'] for row in bound)
   else:
    mapping=bound
    assert all(sha(temporary/name)==digest for name,digest in bound.items())
   assert mapping[filename]==sha(copied)
   expected={
    'dimer_finite_qubit_curl_check.py':('physical_occupation','discrete_curl','finite_block_limit'),
    'dimer_edge_face_gauss_check.py':('incidence','rotations','finite_qubit_algebra','squeezed_motif'),
    'dimer_local_dilute_curl_check.py':('physical_cells','one_particle_symbols','two_particle_dynamics'),
   }[filename]
   payload=data.get('groups',data)
   assert len(expected)==count and all(key in payload for key in expected)
   total+=count;print(f'PASS: {filename}: {count} complete control groups',flush=True)
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

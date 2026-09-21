#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the local-curl, quantum-interface and Born-formation theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_local_curl_quantum_interface_and_born_formation_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-local-curl-quantum-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_LOCAL_CURL_QUANTUM_INTERFACE_AND_BORN_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(('local_curl_native_formation_check.py',
  'LOCAL_CURL_NATIVE_FORMATION_RESULTS.json',
  13),
 ('late_state_canonical_check.py', 'LATE_STATE_CANONICAL_RESULTS.json', 7),
 ('fourteen_label_quantum_check.py', 'FOURTEEN_LABEL_QUANTUM_RESULTS.json', 13),
 ('fourteen_label_cubic_carrier_check.py',
  'FOURTEEN_LABEL_CUBIC_CARRIER_RESULTS.json',
  5),
 ('born_compatible_fourteen_formation_check.py',
  'BORN_COMPATIBLE_FOURTEEN_FORMATION_RESULTS.json',
  13))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_LOCAL_CURL_QUANTUM_INTERFACE_AND_BORN_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 '.claude/science/mobile-record-local-curl-quantum-20260921/suppliers/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 '.claude/science/mobile-record-local-curl-quantum-20260921/author_checks/local_curl_native_formation_check.py',
 '.claude/science/mobile-record-local-curl-quantum-20260921/author_checks/late_state_canonical_check.py',
 '.claude/science/mobile-record-local-curl-quantum-20260921/author_checks/fourteen_label_quantum_check.py',
 '.claude/science/mobile-record-local-curl-quantum-20260921/author_checks/fourteen_label_cubic_carrier_check.py',
 '.claude/science/mobile-record-local-curl-quantum-20260921/author_checks/born_compatible_fourteen_formation_check.py')
MUTATIONS={'alter_Born_event_probability': ('born_compatible_fourteen_formation_check.py',
                                  'effects=[(s.eye(2)+j*spin(v))/14 for v in '
                                  'rays]',
                                  'effects=[(s.eye(2)+j*spin(v))/13 for v in '
                                  'rays]'),
 'alter_minimax_witness': ('fourteen_label_quantum_check.py',
                           'w = j*(2-s.sqrt(3))/56',
                           'w = j*(2-s.sqrt(3))/28'),
 'alter_original_kernel_normalization': ('fourteen_label_quantum_check.py',
                                         'P = (s.ones(14)+j*T)/14',
                                         'P = (s.ones(14)+j*T)/13'),
 'drop_finite_count_correction': ('late_state_canonical_check.py',
                                  's.Rational(volume, volume-1)*C',
                                  'C'),
 'halve_Born_cross_reaction': ('born_compatible_fourteen_formation_check.py',
                               'expected[2:5,5:8]=8*s.sqrt(3)*h*s.eye(3)',
                               'expected[2:5,5:8]=4*s.sqrt(3)*h*s.eye(3)'),
 'halve_native_vector_gain': ('local_curl_native_formation_check.py',
                              'lam=12*beta*j*(1-rho)',
                              'lam=6*beta*j*(1-rho)'),
 'halve_native_wave_speed': ('local_curl_native_formation_check.py',
                             'speed=2*gamma*rho/7',
                             'speed=gamma*rho/7')}
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
 with tempfile.TemporaryDirectory(prefix='local-curl-quantum-controls-') as directory:
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

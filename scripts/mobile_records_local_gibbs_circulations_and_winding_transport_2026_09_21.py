#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the local Gibbs circulation and winding transport theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_local_gibbs_circulations_and_winding_transport_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-local-gibbs-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_LOCAL_GIBBS_CIRCULATIONS_AND_WINDING_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(('local_gibbs_record_circulation_check.py',
  'LOCAL_GIBBS_RECORD_CIRCULATION_RESULTS.json',
  12),
 ('gibbs_transport_1d_check.py', 'GIBBS_TRANSPORT_1D_RESULTS.json', 5))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_LOCAL_GIBBS_CIRCULATIONS_AND_WINDING_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 '.claude/science/mobile-record-local-gibbs-20260921/author_checks/local_gibbs_record_circulation_check.py',
 '.claude/science/mobile-record-local-gibbs-20260921/author_checks/gibbs_transport_1d_check.py')
MUTATIONS={'break_cycle_amplitude_invariance': ('local_gibbs_record_circulation_check.py',
                                      'rates_plus=nu*(1+eps*chi)*np.exp(HS)',
                                      'rates_plus=nu*(1+eps*chi)*np.exp(HS)*(1+states[:,0]/10)'),
 'drop_Perron_normalization': ('gibbs_transport_1d_check.py',
                               'v[d]/Lambda**3',
                               'v[d]/Lambda**2'),
 'halve_KLS_environment_rate': ('gibbs_transport_1d_check.py',
                                '(0,1):2*k*z/(1+z)',
                                '(0,1):k*z/(1+z)'),
 'reverse_Gibbs_energy_sign': ('local_gibbs_record_circulation_check.py',
                               'rates_plus=nu*(1+eps*chi)*np.exp(HS)',
                               'rates_plus=nu*(1+eps*chi)*np.exp(-HS)'),
 'reverse_incoming_Gibbs_ratio': ('gibbs_transport_1d_check.py',
                                  'rates[a,d]*z**(a-d)',
                                  'rates[a,d]*z**(d-a)'),
 'reverse_positive_birth_drift': ('local_gibbs_record_circulation_check.py',
                                  'birthLV=-float((q-1)*beta)*vac',
                                  'birthLV=float((q-1)*beta)*vac')}
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
 with tempfile.TemporaryDirectory(prefix='gibbs-record-controls-') as directory:
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

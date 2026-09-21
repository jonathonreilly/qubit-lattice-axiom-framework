#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the Gauss-loop, dilute-phase and formation-locality theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_gauss_loops_static_phase_and_formation_locality_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-gauss-loops-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_GAUSS_LOOPS_STATIC_PHASE_AND_FORMATION_LOCALITY_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(('microscopic_gauss_record_loop_check.py', 'MICROSCOPIC_GAUSS_RECORD_LOOP_RESULTS.json', 13),
 ('gauss_loop_fugacity_check.py', 'GAUSS_LOOP_FUGACITY_RESULTS.json', 6),
 ('gauss_loop_polymer_check.py', 'GAUSS_LOOP_POLYMER_RESULTS.json', 10),
 ('loop_birth_locality_check.py', 'LOOP_BIRTH_LOCALITY_RESULTS.json', 5))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_GAUSS_LOOPS_STATIC_PHASE_AND_FORMATION_LOCALITY_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 '.claude/science/mobile-record-gauss-loops-20260921/author_checks/microscopic_gauss_record_loop_check.py',
 '.claude/science/mobile-record-gauss-loops-20260921/author_checks/gauss_loop_fugacity_check.py',
 '.claude/science/mobile-record-gauss-loops-20260921/author_checks/gauss_loop_polymer_check.py',
 '.claude/science/mobile-record-gauss-loops-20260921/author_checks/loop_birth_locality_check.py')
# Mutations alter one load-bearing calculation or proposed formula. Each must
# be rejected by another identity; the control expectations are not rewritten.
MUTATIONS={'flip_one_loop_record': ('microscopic_gauss_record_loop_check.py',
                          'values=np.array((unit[0],unit[1],-unit[0],-unit[1]))',
                          'values=np.array((-unit[0],unit[1],-unit[0],-unit[1]))'),
 'half_collective_birth_bracket': ('microscopic_gauss_record_loop_check.py',
                                   'birth+=8*bet*direction*direction.T',
                                   'birth+=4*bet*direction*direction.T'),
 'half_fugacity_structure_factor': ('gauss_loop_fugacity_check.py',
                                    'target=8*(np.dot(sine,sine)',
                                    'target=4*(np.dot(sine,sine)'),
 'allow_both_species_in_one_slot': ('gauss_loop_fugacity_check.py',
                                    'factor=1+za*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in '
                                    'ta)+zb*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in tb)',
                                    'factor=(1+za*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in '
                                    'ta))*(1+zb*sum(s.exp(s.I*t)+s.exp(-s.I*t) for t in tb))'),
 'wrong_polymer_majorant': ('gauss_loop_polymer_check.py', 'bound=q**4/(100*(1-q))', 'bound=q**4/(200*(1-q))'),
 'wrong_tensor_off_diagonal': ('gauss_loop_polymer_check.py',
                               'if i==j else c*k[i]*k[j]',
                               'if i==j else 2*c*k[i]*k[j]')}
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
 with tempfile.TemporaryDirectory(prefix='gauss-loop-controls-') as directory:
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

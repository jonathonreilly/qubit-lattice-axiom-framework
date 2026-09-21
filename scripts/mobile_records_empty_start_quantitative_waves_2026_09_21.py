#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for quantitative record-color waves from empty initialization.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_empty_start_quantitative_waves_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-empty-start-quantitative-waves-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_EMPTY_START_QUANTITATIVE_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=1200
PRIMARY_SOURCES=('GEOMETRIC_ALL_STAGE_POLYNOMIAL_GAP_AND_FILLING.md', 'DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md', 'EMPTY_START_DETERMINISTIC_WAVE_PREPARATION.md', 'GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md', 'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md')
CHECKER_DEPENDENCIES=('dimer_routed_transport_check.py',)
SUITES=(('geometric_all_stage_polynomial_check.py', 'geometric_all_stage_polynomial_checks/RESULTS.json', 3), ('dimer_routed_quantitative_euler_check.py', 'dimer_routed_quantitative_euler_checks/RESULTS.json', 3))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_EMPTY_START_QUANTITATIVE_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MOBILE_RECORDS_ALL_STAGE_FORMATION_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/primary_sources/GEOMETRIC_ALL_STAGE_POLYNOMIAL_GAP_AND_FILLING.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/primary_sources/DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/primary_sources/EMPTY_START_DETERMINISTIC_WAVE_PREPARATION.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/primary_sources/GEOMETRIC_ALL_STAGE_FORMATION_CLOCK.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/primary_sources/GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/author_checks/geometric_all_stage_polynomial_check.py',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/author_checks/dimer_routed_quantitative_euler_check.py',
 '.claude/science/mobile-record-empty-start-quantitative-waves-20260921/author_checks/dimer_routed_transport_check.py')
MUTATIONS={'omit_birth_killing_scale': ('geometric_all_stage_polynomial_check.py',
                              'factor=2/(beta*p)+(1+2*m/p)/gap',
                              'factor=(1+2*m/p)/gap'),
 'omit_route_orientation_factor': ('dimer_routed_quantitative_euler_check.py',
                                   'assert value==2*cut*(L-cut)*L**2',
                                   'assert value==cut*(L-cut)*L**2'),
 'wrong_original_hole_fiber': ('geometric_all_stage_polynomial_check.py',
                               "'two_original':(h+1)**2*f0",
                               "'two_original':h**2*f0")}
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
 with tempfile.TemporaryDirectory(prefix='empty-start-wave-controls-') as directory:
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
   assert bound[filename]==sha(copied)
   assert all(sha(temporary/name)==digest for name,digest in bound.items())
   if 'groups' in data:
    assert len(data['groups'])==count and all(c['passed'] for c in data['groups'])
   elif filename=='dimer_routed_quantitative_euler_check.py':
    assert count==3
    assert len(data['open_cube_loads'])==3 and len(data['contracted_footprints'])==7 and len(data['linear_coefficients'])==3
   else:
    raise AssertionError('undeclared result schema')
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

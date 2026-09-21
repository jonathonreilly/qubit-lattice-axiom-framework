#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for moving-geometry record-color waves.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_moving_geometry_color_waves_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-moving-geometry-waves-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=1200
PRIMARY_SOURCES=('DIMER_ROUTED_RECORD_TRANSPORT.md', 'DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md', 'DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md', 'DIMER_ROUTED_DIFFUSIVE_GAP_COMPARISON.md')
CHECKER_DEPENDENCIES=()
SUITES=(('dimer_routed_transport_check.py', 'dimer_routed_transport_checks/RESULTS.json', 5), ('dimer_routed_preparation_check.py', 'dimer_routed_preparation_checks/RESULTS.json', 3), ('dimer_routed_moving_geometry_check.py', 'dimer_routed_moving_geometry_checks/RESULTS.json', 2), ('dimer_routed_diffusive_gap_check.py', 'dimer_routed_diffusive_gap_checks/RESULTS.json', 3))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/MOBILE_RECORDS_ALL_STAGE_FORMATION_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/primary_sources/DIMER_ROUTED_RECORD_TRANSPORT.md',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/primary_sources/DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/primary_sources/DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/primary_sources/DIMER_ROUTED_DIFFUSIVE_GAP_COMPARISON.md',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/author_checks/dimer_routed_transport_check.py',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/author_checks/dimer_routed_preparation_check.py',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/author_checks/dimer_routed_moving_geometry_check.py',
 '.claude/science/mobile-record-moving-geometry-waves-20260921/author_checks/dimer_routed_diffusive_gap_check.py')
MUTATIONS={'double_context_current': ('dimer_routed_transport_check.py',
                            'mass*(8+h)*((a==c).astype(int)-(b==c).astype(int))',
                            'mass*(8+2*h)*((a==c).astype(int)-(b==c).astype(int))'),
 'omit_endpoint_return_word': ('dimer_routed_diffusive_gap_check.py',
                               'word=edges+edges[-2::-1]',
                               'word=edges'),
 'wrong_plaquette_record_rotation': ('dimer_routed_moving_geometry_check.py',
                                     'new_ids = np.roll(ids[vertices], sense)',
                                     'new_ids = np.roll(ids[vertices], '
                                     '2*sense)')}
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
 with tempfile.TemporaryDirectory(prefix='moving-record-wave-controls-') as directory:
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
   elif filename=='dimer_routed_moving_geometry_check.py':
    assert count==2 and data['status']=='pass'
    assert len(data['geometry_and_dirichlet']['rows'])==9
    assert len(data['switched_energy']['rows'])==40
   elif filename=='dimer_routed_diffusive_gap_check.py':
    assert count==3
    assert len(data['physical_loads'])==2 and len(data['contracted_loads'])==6 and len(data['schedule'])==6
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

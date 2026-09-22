#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for smooth nonlinear permanent-color evolution.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_smooth_nonlinear_euler_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-smooth-nonlinear-euler-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_SMOOTH_NONLINEAR_EULER_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=1200
PRIMARY_SOURCES=('DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md', 'DIMER_NONLINEAR_INITIAL_DRIFT.md', 'DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md', 'DIMER_MOVING_GEOMETRY_SMOOTH_NONLINEAR_EULER.md', 'DIMER_MOVING_NONLINEAR_QUANTITATIVE_ADDENDUM.md', 'DIMER_ROUTED_RECORD_TRANSPORT.md', 'DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md', 'DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md', 'DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md')
CHECKER_DEPENDENCIES=()
SUITES=(('dimer_nonlinear_flux_check.py', 'dimer_nonlinear_flux_checks/RESULTS.json', 4), ('dimer_smooth_nonlinear_check.py', 'dimer_smooth_nonlinear_checks/RESULTS.json', 3), ('dimer_moving_nonlinear_check.py', 'dimer_moving_nonlinear_checks/RESULTS.json', 3))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_SMOOTH_NONLINEAR_EULER_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/MOBILE_RECORDS_MOVING_GEOMETRY_COLOR_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MOBILE_RECORDS_EMPTY_START_QUANTITATIVE_WAVES_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_NONLINEAR_COLOR_FLUX_AND_OPTICAL_DIAGNOSTICS.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_NONLINEAR_INITIAL_DRIFT.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_SMOOTH_NONLINEAR_EULER_LIMIT.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_MOVING_GEOMETRY_SMOOTH_NONLINEAR_EULER.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_MOVING_NONLINEAR_QUANTITATIVE_ADDENDUM.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_ROUTED_RECORD_TRANSPORT.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_ROUTED_MOVING_GEOMETRY_EXTENSION.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_ROUTED_QUANTITATIVE_EULER_BOUND.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/primary_sources/DIMER_ROUTED_POLYNOMIAL_COLOR_PREPARATION.md',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/author_checks/dimer_nonlinear_flux_check.py',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/author_checks/dimer_smooth_nonlinear_check.py',
 '.claude/science/mobile-record-smooth-nonlinear-euler-20260921/author_checks/dimer_moving_nonlinear_check.py')
MUTATIONS={'double_block_exponential_coefficient': ('dimer_smooth_nonlinear_check.py',
                                          'alpha=F(1,224)',
                                          'alpha=F(1,112)'),
 'omit_entropy_flux_half_M': ('dimer_nonlinear_flux_check.py',
                              '-eta*M-(0 if omit else M/2)',
                              '-eta*M'),
 'omit_geometry_marginal_entropy_derivative': ('dimer_moving_nonlinear_check.py',
                                               'np.log(mu/(rho[:,None]/D))',
                                               'np.log(mu*2*D)'),
 'omit_nonlinear_population_flux': ('dimer_nonlinear_flux_check.py',
                                    'e.cross(Y)+X.cross(b)-2*X.cross(Y)',
                                    'e.cross(Y)+X.cross(b)'),
 'omit_owner_boundary_coverage': ('dimer_moving_nonlinear_check.py',
                                  'np.all(cover==L**3+L**2)',
                                  'np.all(cover==L**3)')}
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
 with tempfile.TemporaryDirectory(prefix='smooth-nonlinear-controls-') as directory:
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
    'dimer_nonlinear_flux_check.py':('moment_fluxes','entropy_symmetrizer','optical_diagnostic','actual_initial_drift'),
    'dimer_smooth_nonlinear_check.py':('blocks','fixed_sector','entropy_algebra'),
    'dimer_moving_nonlinear_check.py':('geometry_entropy','owner_blocks','exponential_constants'),
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

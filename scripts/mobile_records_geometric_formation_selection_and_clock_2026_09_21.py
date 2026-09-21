#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the geometric record formation, selection and final-pair clock theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_geometric_formation_selection_and_clock_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-geometric-formation-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_GEOMETRIC_FORMATION_SELECTION_AND_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
PRIMARY_SOURCES=('GEOMETRIC_PARTNER_RECORD_FORMATION.md',
 'GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md',
 'GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md',
 'GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md',
 'GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md')
SUITES=(('geometric_partner_formation_check.py',
  'geometric_partner_checks/RESULTS.json',
  5),
 ('geometric_rare_birth_check.py',
  'geometric_rare_birth_checks/RESULTS.json',
  4),
 ('geometric_last_pair_clock_check.py',
  'geometric_last_pair_clock_checks/RESULTS.json',
  3),
 ('geometric_general_graph_check.py',
  'geometric_general_graph_checks/RESULTS.json',
  4),
 ('geometric_polynomial_relaxation_check.py',
  'geometric_polynomial_relaxation_checks/RESULTS.json',
  4))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_GEOMETRIC_FORMATION_SELECTION_AND_CLOCK_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 '.claude/science/mobile-record-geometric-formation-20260921/primary_sources/GEOMETRIC_PARTNER_RECORD_FORMATION.md',
 '.claude/science/mobile-record-geometric-formation-20260921/primary_sources/GEOMETRIC_RARE_BIRTH_UNIFORM_SELECTION.md',
 '.claude/science/mobile-record-geometric-formation-20260921/primary_sources/GEOMETRIC_LAST_PAIR_CLOCK_AND_MONOMERS.md',
 '.claude/science/mobile-record-geometric-formation-20260921/primary_sources/GEOMETRIC_TWO_VACANCY_GENERAL_GRAPH.md',
 '.claude/science/mobile-record-geometric-formation-20260921/primary_sources/GEOMETRIC_POLYNOMIAL_RELAXATION_AND_FORMATION.md',
 '.claude/science/mobile-record-geometric-formation-20260921/author_checks/geometric_partner_formation_check.py',
 '.claude/science/mobile-record-geometric-formation-20260921/author_checks/geometric_rare_birth_check.py',
 '.claude/science/mobile-record-geometric-formation-20260921/author_checks/geometric_last_pair_clock_check.py',
 '.claude/science/mobile-record-geometric-formation-20260921/author_checks/geometric_general_graph_check.py',
 '.claude/science/mobile-record-geometric-formation-20260921/author_checks/geometric_polynomial_relaxation_check.py')
MUTATIONS={'break_record_slide_permutation': ('geometric_partner_formation_check.py',
                                    'state[b]=first;state[c]=second',
                                    'state[b]=second;state[c]=first'),
 'break_trace_row_sum': ('geometric_polynomial_relaxation_check.py',
                         'LT=LS+np.diag(h)-A@A.T/K',
                         'LT=LS+np.diag(h)-A@A.T/(2*K)'),
 'double_killed_birth_hazard': ('geometric_rare_birth_check.py',
                                'U=(-S+rate*H).inv()*(rate*A)',
                                'U=(-S+2*rate*H).inv()*(rate*A)'),
 'miscount_monomer_normalization': ('geometric_last_pair_clock_check.py',
                                    'chi=s.Rational(sum(minors[0]),Z)',
                                    'chi=s.Rational(sum(minors[0]),2*Z)'),
 'omit_clock_schur_correction': ('geometric_last_pair_clock_check.py',
                                 'denominator=p-beta*C',
                                 'denominator=p'),
 'omit_cycle_return_path': ('geometric_rare_birth_check.py',
                            'for a,b,c in reversed(entrance[:-1]):',
                            'for a,b,c in []:'),
 'omit_general_graph_second_slide': ('geometric_general_graph_check.py',
                                     'for event in [(bp,b,a),(b,a,ap)]:',
                                     'for event in [(bp,b,a)]:'),
 'reverse_neighbor_birth_response': ('geometric_partner_formation_check.py',
                                     '1+eps*dot(v,m)/r',
                                     '1-eps*dot(v,m)/r')}
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
 with tempfile.TemporaryDirectory(prefix='geometric-record-controls-') as directory:
  temporary=Path(directory)
  for filename in PRIMARY_SOURCES:
   (temporary/filename).write_bytes((ROOT/EVIDENCE/'primary_sources'/filename).read_bytes())
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
   bound=data.get('sources_sha256',data.get('source_sha256'))
   assert bound[filename]==sha(copied)
   assert all(sha(temporary/name)==digest for name,digest in bound.items())
   assert len(data['rows'])==count and all(c['pass'] for c in data['rows'])
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

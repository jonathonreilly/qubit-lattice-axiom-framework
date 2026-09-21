#!/usr/bin/env python3
"""Source-bound symbolic and numerical controls for the cubic symbol classification and conditional Gauss closure theorem note.

The complete finite calculations live in declared auxiliary author sources.
They are copied into a temporary directory before execution, so this runner
never edits its inputs. Algebraic controls do not replace the proof arguments.
"""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile

ROOT=Path(__file__).resolve().parents[1]
CLAIM_ID='mobile_records_cubic_symbol_selection_and_gauss_closure_bounded_theorem_note_2026-09-21'
EVIDENCE='.claude/science/mobile-record-cubic-selection-20260921'
CHECK_DIRECTORY=EVIDENCE+'/author_checks'
NOTE='docs/MOBILE_RECORDS_CUBIC_SYMBOL_SELECTION_AND_GAUSS_CLOSURE_BOUNDED_THEOREM_NOTE_2026-09-21.md'
AUDIT_TIMEOUT_SEC=600
SUITES=(('cubic_entropy_symbol_check.py', 'CUBIC_ENTROPY_SYMBOL_RESULTS.json', 1),
 ('cubic_symbol_selection_check.py', 'CUBIC_SYMBOL_SELECTION_RESULTS.json', 1))
AUDIT_INPUT_PATHS=('docs/MOBILE_RECORDS_CUBIC_SYMBOL_SELECTION_AND_GAUSS_CLOSURE_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/MOBILE_RECORDS_IMMUTABLE_TRANSVERSE_CURL_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-21.md',
 '.claude/science/mobile-record-cubic-selection-20260921/author_checks/cubic_entropy_symbol_check.py',
 '.claude/science/mobile-record-cubic-selection-20260921/author_checks/cubic_symbol_selection_check.py')
MUTATIONS={'double_offdiagonal_Gram_weight': ('cubic_entropy_symbol_check.py',
                                    '(m*m+v*v/2)*r2*sp.eye(3)',
                                    '(m*m+v*v)*r2*sp.eye(3)'),
 'halve_microscopic_pair_tensor': ('cubic_entropy_symbol_check.py',
                                   'S = 15/2*target',
                                   'S = 15/4*target'),
 'omit_axial_reflection_sign': ('cubic_entropy_symbol_check.py',
                                '(det if t == "B" else 1) * Q @ v',
                                'Q @ v'),
 'omit_telescoping_term': ('cubic_entropy_symbol_check.py',
                           'h = S[l,a]+S[a,r]-S[l,d]-S[d,r]',
                           'h = S[l,a]+S[a,r]-S[d,r]'),
 'reverse_second_curl_readout': ('cubic_symbol_selection_check.py',
                                 'P[3:,:3]=-s.I*C',
                                 'P[3:,:3]=s.I*C'),
 'use_proper_group_for_full_count': ('cubic_entropy_symbol_check.py',
                                     'if proper_only and det < 0:',
                                     'if det < 0:')}
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
 with tempfile.TemporaryDirectory(prefix='cubic-symbol-controls-') as directory:
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
   if filename=='cubic_entropy_symbol_check.py':
    assert data['full_cubic_symmetric_symbol_dimension_exact']==5
    assert data['proper_cubic_symmetric_symbol_dimension_exact']==11
    assert data['explicit_family_dimension']==5
    assert data['group_covariance_max_abs_error']<1e-12
    assert data['exact_gram_formula']=='verified by symbolic polynomial expansion'
    assert (data['maxwell_nonzero_modes'],data['maxwell_zero_modes'])==(4,10)
    assert (data['generic_nonzero_modes'],data['generic_zero_modes'])==(6,8)
    assert data['microscopic_current_derivative_max_abs_error']<1e-7
    assert data['pair_tensor_row_sum_max_abs_error']<1e-12
    assert data['telescoping_residual_max_abs_error']<1e-12
    assert data['swap_antisymmetry_max_abs_error']<1e-12
   else:
    assert data['source_sha256']==sha(copied)
    assert data['exact_reversal_identity'] and data['curl_readout_evolution_residual_exact']
    assert data['raw_vector_Gauss_invariant_subspace_conditions']==['a1=0','a2=0','u=0','v=0']
    assert data['curl_readout_closed_conditions']==['u=0','v=0']
   total+=count;print(f'PASS: {filename}: {count} complete assertion suite',flush=True)
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

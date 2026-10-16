"""Inspect source integrity and refusal contracts; execute no scientific program."""
from pathlib import Path
import ast,copy,difflib,hashlib,json,re,runpy,sys
D=Path(sys.argv[1]).resolve();P=D/'proposal'
PK='.claude/science/physics-loops/toe-product-source-mediator-20261016'
NOTE='docs/PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md'
SCRIPT='scripts/product_source_mediator_2026_10_16.py'
api=runpy.run_path(str(P/SCRIPT),run_name='source_metadata_inspection')
read=lambda rel:(P/rel).read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
checked=api['verify_payload'](read)
maps=json.loads(read(PK+'/BODY_MAP.json'))['bodies'];note=read(NOTE)
for row in maps:
 original=(D.parent/row['source']).read_bytes()
 assert note[row['start_byte_inclusive']:row['end_byte_exclusive']]==original
 assert sha(original)==row['sha256']
source_rows=json.loads(read(PK+'/SOURCE_MANIFEST.json'))['sources'];source={r['source']:r for r in source_rows}
def expect_rejected(label,reader,phase='payload'):
 try:
  if phase=='payload':api['verify_payload'](reader)
  else:api['verify_actual_binding'](reader,checked)
 except (ValueError,FileNotFoundError) as exc:return {'name':label,'rejected':True,'reason':str(exc)}
 raise AssertionError('Metadata mutation accepted: '+label)
mutants=[expect_rejected('unbound_canonical_refusal',read,'binding')]
try:api['main']()
except ValueError as exc:
 assert str(exc).startswith('UNBOUND SOURCE-ONLY PROPOSAL:')
 default_refusal={'proposed_copy_entrypoint_refused':True,'reason':str(exc),'canonical_file_executed':False}
else:raise AssertionError('Unbound proposed primary main accepted')
targets={
 'altered_original_body':NOTE,
 'altered_root_qualification':source['product_source_mediator_root_review/QUALIFICATION.md']['recovery_path'],
 'altered_pauli_qualification':source['product_source_mediator_pauli_root_review/QUALIFICATION.md']['recovery_path'],
 'missing_main_capture':source['product_source_mediator_exposed_check/metadata/executed_source.py']['recovery_path'],
 'missing_compiler_review_stdout':source['product_source_mediator_exposed_check/finite_compiler_addendum/metadata/stdout']['recovery_path'],
 'missing_pauli_review_launcher':source['product_source_mediator_exposed_check/pauli_block_addendum/metadata/launcher_source.py']['recovery_path'],
 'missing_root_acceptance_capture':source['runs/product_source_root_acceptance/executed_source.py']['recovery_path'],
 'invented_dependency':PK+'/PARENT_BINDING.json',
 'invented_future_approval':PK+'/ACTUAL_BINDING.json',
}
for name,path in targets.items():
 def mutant(rel,path=path,name=name):
  if rel==path:
   if name.startswith('missing'):raise FileNotFoundError('Scoped metadata removal: '+name)
   if name=='altered_original_body':
    data=bytearray(read(rel));data[maps[0]['start_byte_inclusive']+10]^=1;return bytes(data)
   return read(rel)+b'\nSCOPED METADATA MUTANT\n'
  return read(rel)
 mutants.append(expect_rejected(name,mutant))
src=lambda alias:read(source[alias]['recovery_path'])
contracts=json.loads(read(PK+'/EXECUTION_CONTRACTS.json'))['receipts']
semantic=[]
for contract in contracts:
 for field in ['exit_code','argv','chronology','snapshot_bytes','missing_stream']:
  altered=copy.deepcopy(json.loads(src(contract['alias'])))
  if field=='exit_code':altered['exit_code']=1
  elif field=='argv':altered['argv']=altered['argv']+['unrecorded-argument']
  elif field=='chronology':
   if 'end_utc' in altered:altered['end_utc']=altered['start_utc']
   else:altered['finished_at']=altered['started_at']
  stream=next(r['alias'] for r in contract['files'] if r['alias'].endswith('/stderr'))
  def changed(alias,altered=altered,contract=contract,field=field,stream=stream):
   if alias==contract['alias']:return json.dumps(altered).encode()
   if field=='snapshot_bytes' and alias==contract['snapshot_alias']:return src(alias)+b'\nMUTANT\n'
   if field=='missing_stream' and alias==stream:raise FileNotFoundError('Missing complete stderr')
   return src(alias)
  try:api['verify_receipt'](changed,contract)
  except (ValueError,FileNotFoundError) as exc:semantic.append({'receipt':contract['alias'],'mutation':field,'rejected':True,'reason':str(exc)})
  else:raise AssertionError('Receipt predicate mutation accepted '+field)

# Four isolated current-parser functions, evaluated only on the proposed tree.
parser_path=D/'methodology/build_citation_graph.py';text=parser_path.read_text();tree=ast.parse(text)
names={'normalize_runner_path','runner_paths','first_runner_path','extract_runner'}
functions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
constants=[n for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id in {'RUNNER_LABEL_RE','RUNNER_PATH_RE','RUNNER_SECTION_RE','RUNNER_VERIFICATION_SECTION_RE','HEADING_RE'} for t in n.targets)]
ns={'Path':Path,'re':re,'REPO_ROOT':P}
exec(compile(ast.Module(body=constants+functions,type_ignores=[]),str(parser_path)+':isolated_runner_resolution','exec'),ns)
resolved=ns['extract_runner'](note.decode(),NOTE.removeprefix('docs/'));assert resolved==SCRIPT
parser_check={'parser_sha256':sha(parser_path.read_bytes()),'functions':sorted(names),'resolved_primary':resolved,
 'proposal_tree_only':True,'graph_build_executed':False,'canonical_graph_written':False}
function_rows=[];diffs=[]
for name in ['build_packet.py','primary_template.py','inspect_packet.py','record_metadata.py','seal_packet.py']:
 old=(D/'machinery_reference'/name).read_text();new=(D/name).read_text()
 a,b=ast.parse(old),ast.parse(new)
 old_functions={n.name:ast.get_source_segment(old,n) for n in ast.walk(a) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
 for n in ast.walk(b):
  if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef)):
   text=ast.get_source_segment(new,n);previous=old_functions.get(n.name)
   function_rows.append({'file':name,'function':n.name,'first_line':n.lineno,'last_line':n.end_lineno,
    'source_sha256':sha(text.encode()),'baseline_source_sha256':sha(previous.encode()) if previous is not None else None,
    'exact_source_reuse':text==previous,'ast_sha256':sha(ast.dump(n,include_attributes=False).encode())})
 diffs.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='machinery_reference/'+name,tofile=name))
 assert not any(line.rstrip()!=line for line in new.splitlines()),name
ast.parse((P/SCRIPT).read_text())
(D/'CODE_REUSE_MAP.json').write_text(json.dumps({'baseline':'weak_mediator_qualified_publication_draft',
 'scope':'Exact function source identity only; changed globals and full module logic need review.',
 'functions':function_rows},indent=2)+'\n')
(D/'CODE_FULL_DIFF.patch').write_text(''.join(diffs))
result={'kind':'source_integrity_and_metadata_mutants_only','checked':checked,'direct_original_interval_comparison':True,
 'scoped_metadata_mutants':mutants,'direct_receipt_predicate_mutants':semantic,'default_refusal':default_refusal,
 'graph_parser_primary_resolution':parser_check,'function_rows':len(function_rows),
 'exact_source_function_reuses':sum(r['exact_source_reuse'] for r in function_rows),
 'mathematics_tested_by_this_execution':False,'historical_scientific_replays':0,
 'canonical_primary_execution':None,'root_source_wrapper_review':None}
(D/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

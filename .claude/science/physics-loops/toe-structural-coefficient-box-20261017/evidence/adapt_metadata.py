"""One bounded metadata/transport adaptation; preserve frozen mathematical sources."""
from pathlib import Path
import ast
import copy
import datetime
import hashlib
import json

D = Path(__file__).resolve().parent
W = D.parents[1]/'correlation_worktree'
Q = W/'.claude/science/physics-loops/toe-structural-coefficient-box-20261017'
F = W/'outputs/structural_coefficient_box_2026_10_17_inputs'
primary = W/'scripts/structural_coefficient_box_2026_10_17.py'
helper = W/'scripts/structural_coefficient_box_check_2026_10_17.py'
note = W/'docs/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md'

def pin(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(W)), 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest()}

before=D/'pre_metadata_adaptation'
before.mkdir(exist_ok=False)
for p in (primary,helper,note,Q/'SOURCE_MANIFEST.json'):
    (before/p.name).write_bytes(p.read_bytes())

p=primary.read_text()
p='''"""Replay exact structural coefficient bounds and a separately written checker.

The frozen source calculations are transported into repository-local functions.
Only resource-report metadata within those calculation bodies is adapted: the
original author/reviewer limits are historical, while the canonical invocation
shares one 60-second CPU limit and runner-cache-enforced 60-second wall limit.
This program checks finite algebra, not the infinite-clock theorem by simulation.
"""\n'''+p
old="'independent_review': False, 'cpu_cap_seconds': 10,\n               'wrapper_wall_cap_seconds': 20"
new="""'independent_review': False,
               'historical_source_run_limits': {'cpu_cap_seconds': 10,
                   'external_wall_cap_seconds': 20},
               'actual_combined_process_limits': {'cpu_cap_seconds': 60,
                   'external_wall_cap_seconds': 60}"""
assert p.count(old)==1
p=p.replace(old,new)
p=p.replace('def main():\n', 'def main():\n    combined_started = time.monotonic()\n',1)
old="            'author':author,'independent':independent,\n"
new="""            'author':author,'independent':independent,
            'input_sha256': {name: hashlib.sha256((REPO/name).read_bytes()).hexdigest()
                             for name in AUDIT_INPUT_PATHS},
            'actual_combined_process_limits': {
                'cpu_soft_hard_seconds': list(resource.getrlimit(resource.RLIMIT_CPU)),
                'external_wall_cap_seconds': AUDIT_TIMEOUT_SEC,
                'wall_enforcement': 'Canonical runner_cache invocation; standalone callers must enforce an equivalent external limit.',
                'author_and_independent_calculations_share_one_process': True,
                'elapsed_seconds': time.monotonic()-combined_started},
"""
assert p.count(old)==1
p=p.replace(old,new)
primary.write_text(p)
h=helper.read_text()
h=h.replace('The mathematical body is unchanged from the separately written source.',
            'The mathematical body is unchanged except for resource-report metadata.\nOriginal source-run limits are historical; canonical execution shares the\nprimary process and its external runner-cache wall limit.')
old="{'cpu_cap_seconds':45,'external_wall_cap_seconds':60,"
new="""{'historical_source_run_limits': {'cpu_cap_seconds':45,
            'external_wall_cap_seconds':60},
        'actual_combined_process_limits': {'cpu_cap_seconds':60,
            'external_wall_cap_seconds':60},"""
assert h.count(old)==1
h=h.replace(old,new)
helper.write_text(h)

n=note.read_text().replace('wrapper_root_approval: separately_recorded','wrapper_root_approval: pending_separate_root_review')
n=n.replace('canonical_execution: separately_recorded','canonical_execution: see_source_bound_execution_record')
old='not retroactively alter either original receipt.\n'
new=old+'''
The original author limits were 10 CPU seconds and 20 wall seconds; the
original independent limits were 45 CPU seconds and 60 wall seconds. The
portable run shares one 60-second CPU cap and one externally enforced
60-second wall cap across both calculations. Its elapsed time and actual
result are recorded separately. These metadata changes do not alter a
coefficient, equation or scientific assertion in either calculation body.
'''
assert n.count(old)==1
n=n.replace(old,new)
note.write_text(n)

# Compare complete wrapped calculation ASTs after reversing only the exact
# two resource-metadata adaptations above. The initial wrapping AST check is
# independently repeated against the unchanged frozen source, not trusted.
def body(code,name,skip):
    f=next(x for x in ast.parse(code).body if isinstance(x,ast.FunctionDef) and x.name==name)
    assert isinstance(f.body[-1],ast.Return)
    return f.body[skip:-1]
author_src=(F/'author/check_bounds.py').read_text()
author_body='manifest = json.loads'+author_src.split('manifest = json.loads',1)[1].split("(ROOT / 'BOUNDS.json').write_text",1)[0]
helper_src=(F/'review/check_structural_box.py').read_text()
helper_body='pins = json.loads'+helper_src.split('pins = json.loads',1)[1].split('outpath.write_text',1)[0]

author_new=body(p,'run_author_checks',2)
author_old=ast.parse(author_body).body
helper_new=body(h,'run_independent_checks',1)
helper_old=ast.parse(helper_body).body
edits=[]
for label,new_body,old_body in [('author',author_new,author_old),('independent',helper_new,helper_old)]:
    assert len(new_body)==len(old_body)
    changes=[]
    for i,(a,b) in enumerate(zip(new_body,old_body)):
        if ast.dump(a,include_attributes=False)!=ast.dump(b,include_attributes=False):
            changes.append(i)
    assert len(changes)==1, (label,changes)
    i=changes[0]
    na=copy.deepcopy(new_body[i]); oa=old_body[i]
    assert isinstance(na,ast.Assign) and isinstance(oa,ast.Assign)
    if label=='author':
        assert isinstance(na.value,ast.Dict)
        nd=next(v for k,v in zip(na.value.keys,na.value.values) if isinstance(k,ast.Constant) and k.value=='limits')
        od=next(v for k,v in zip(oa.value.keys,oa.value.values) if isinstance(k,ast.Constant) and k.value=='limits')
    else:
        assert ast.unparse(na.targets[0])=="evidence['resources']"
        nd,od=na.value,oa.value
    oldkeys={k.value:v for k,v in zip(od.keys,od.values)}
    newkeys={k.value:v for k,v in zip(nd.keys,nd.values)}
    hist=newkeys.pop('historical_source_run_limits')
    actual=newkeys.pop('actual_combined_process_limits')
    assert ast.literal_eval(actual)=={'cpu_cap_seconds':60,'external_wall_cap_seconds':60}
    assert ast.literal_eval(hist)==({'cpu_cap_seconds':10,'external_wall_cap_seconds':20} if label=='author' else {'cpu_cap_seconds':45,'external_wall_cap_seconds':60})
    expected_removed={'cpu_cap_seconds','wrapper_wall_cap_seconds' if label=='author' else 'external_wall_cap_seconds'}
    assert set(newkeys)==set(oldkeys)-expected_removed
    assert all(ast.dump(v,include_attributes=False)==ast.dump(oldkeys[k],include_attributes=False) for k,v in newkeys.items())
    edits.append({'body':label,'statement_index_zero_based':i,
                  'original_statement_ast':ast.dump(oa,include_attributes=False),
                  'adapted_statement_ast':ast.dump(new_body[i],include_attributes=False),
                  'only_resource_metadata_changed':True,
                  'historical_limits':ast.literal_eval(hist),'actual_combined_limits':ast.literal_eval(actual)})
    nd.keys=copy.deepcopy(od.keys);nd.values=copy.deepcopy(od.values)
    assert ast.dump(na,include_attributes=False)==ast.dump(oa,include_attributes=False)

raw=note.read_bytes(); frozen=(F/'author/CANDIDATE.md').read_bytes()
begin=b'<!-- BEGIN FROZEN COEFFICIENT ARGUMENT -->\n'
end=b'\n<!-- END FROZEN COEFFICIENT ARGUMENT -->'
offset=raw.index(begin)+len(begin)
assert raw[offset:raw.index(end,offset)]==frozen
record={'scope':'Metadata-only calculation-body AST adaptations and output transport; no new science review.',
        'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'frozen_sources':[pin(F/'author/check_bounds.py'),pin(F/'review/check_structural_box.py')],
        'metadata_edits':edits,'all_other_calculation_statements_ast_identical':True,
        'frozen_argument_byte_identical':True,'body_offset_zero_based':offset,'body_bytes':len(frozen),
        'body_sha256':hashlib.sha256(frozen).hexdigest(),
        'canonical_primary':pin(primary),'canonical_helper':pin(helper),'note':pin(note)}
(D/'METADATA_ADAPTATION.json').write_text(json.dumps(record,indent=2)+'\n')
s=json.loads((Q/'SOURCE_MANIFEST.json').read_text())
s.update(canonical_primary=pin(primary),canonical_helper=pin(helper),note=pin(note),
         body_offset_zero_based=offset,body_bytes=len(frozen),
         metadata_adaptation='evidence/METADATA_ADAPTATION.json',
         source_implementation_changes='Frozen bodies remain byte-identical. Wrapped calculation ASTs differ only in two resource-report dictionaries: original limits are labeled historical and combined60CPU/60wall limits are added. All coefficients, equations, scientific assertions and other calculation statements are AST-identical. Outer transport adds a module docstring, combined process metadata, and declared-input hashes. No independent science verdict is supplied by packaging.')
(Q/'SOURCE_MANIFEST.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='metadata_edits'},indent=2))

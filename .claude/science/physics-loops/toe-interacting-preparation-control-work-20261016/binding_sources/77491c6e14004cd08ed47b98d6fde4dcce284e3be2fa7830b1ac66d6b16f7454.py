"""Source-only interacting-control integration proposal requiring an actual bound Git base. Root alone executes actions."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, ast, contextlib, difflib, gzip, hashlib, io, json, os, re
import shutil, subprocess, sys, time, traceback

OUT = Path(__file__).resolve().parent
ROOT_BINDING = None
BASE_BINDING = json.loads((OUT/'BASE_BINDING_INPUT.json').read_text())
N = OUT.parent
W = N.parent / 'correlation_worktree'
SOURCE = N / 'interacting_control_qualified_publication_draft'
D = N / 'publication_integration/interacting_control'
STAGE = D / 'canonical_source'
PACKET = '.claude/science/physics-loops/toe-interacting-preparation-control-work-20261016'
NOTE = 'docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md'
HELPER = 'scripts/interacting_preparation_control_work_2026_10_16.py'
PARENTS = ('docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md', 'docs/INHOMOGENEOUS_COMB_LOCAL_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-16.md')
EXTERNAL_INPUTS = ('docs/LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md', 'docs/INHOMOGENEOUS_COMB_LOCAL_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-16.md')
CLAIM = 'interacting_preparation_control_work_bounded_theorem_note_2026-10-16'
PARENT_CLAIMS = ('local_conserving_preparation_bounded_theorem_note_2026-10-16', 'inhomogeneous_comb_local_control_bounded_theorem_note_2026-10-16')
BASE = BASE_BINDING['base_head']
BASE_BRANCH = BASE_BINDING['base_branch']
BASE_PR = BASE_BINDING['base_pr']
BASE_PARENT_BRANCH = BASE_BINDING['base_parent_branch']
PHASE_ACTION_LABELS = {}
ROOT_REVIEW_RUN = None
FEATURE = 'physics-loop/toe-interacting-preparation-control-work-20261016'
REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
TITLE = '[physics-loop] toe-interacting-preparation-control-work: bounded_theorem / conditional-support'
PR_SPECS = (('base', BASE_PR, BASE, BASE_BRANCH, BASE_PARENT_BRANCH),)
SOURCE_FREEZE = 'a82254aa003e3de63109e532adca46c771ec122d910528e9f9ff0f9e2e8996e2'
ROOT_REVIEW = None
ROOT_REVIEW_SHA = None
ROOT_DECISION = None
REFRESH = None
DEADLINE = datetime(2026, 10, 16, 22, 40, 23, tzinfo=timezone.utc)
GRAPH = 'docs/audit/data/citation_graph.json'
GRAPH_MANIFEST = 'docs/audit/data/citation_graph_manifest.json'

EXPECTED_MAIN = None
EXPECTED_INSTRUCTIONS = '56c5c0ab64f532c5784e895b2f9aa6894fa334e0'
EXPECTED_ACCEPTANCE = {'interacting_ramp_bridge_root_review/QUALIFIED_ACCEPTANCE.json': '857b4ce85a3f1a826e4dfd0c4342df5845e4991e60d3c5f85b1d30e3b98d93fa', 'interacting_preparation_chronology_root_review/ACCEPTANCE.json': '0cbc3e8b6020894222319c43ae4f1deda6f75be8a020b886982dd445e669d6e8', 'interacting_local_fault_work_root_review/ACCEPTANCE.json': '10a4832688c81c227c74f29de239964a5d7d268000a4d7bf1babf6f8b441c4c8'}
EXPECTED_SOURCE_BODIES = {'bridge_original': '2d4294d7f5c33bcc459624857a473d28c2f7099755e376d27999830b2362e10e', 'bridge_exposed_review': '086f5d2e7a16d3d32563f64bd862d97c8c2ee14cf2f7b5767c17c67598ed0794', 'bridge_controlling_qualifications': '502b3af3f8c7e2bd2709bc75f14ab953196130e3d45c26cd2fc2a24dad130a51', 'preparation_original': 'ba2624d2819db440c6e378f37d53c90b6470c83bb98a84b050fb1073dacc4dfc', 'preparation_exposed_review': '5c6884db8a0a933f4c83f010c1ed25d3ce9f6aff3d7815a109b39234c23aac76', 'preparation_controlling_qualifications': 'a942ce74a8cafdd417c1a945bc73e400f419b2b489d84848c1752b21337d5d40', 'fault_work_original': 'c3bd7cdae9704e2bf6d867dd5f27bb433690c8b5028d2d069b63376ea5fd7ecd', 'fault_work_exposed_review': '9d5673aa82a5cbf61a3ee3a80ee485bb26e1241a7f91b012c816b590d90de9a8', 'fault_work_controlling_qualifications': '7085ae52c53237e42ef735fb0a8e0d057ce8f4a625da5a37a23de697be3c8212'}

def now(): return datetime.now(timezone.utc).isoformat()

def digest(data): return hashlib.sha256(data).hexdigest()

def pin(path):
    path = Path(path); data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': digest(data)}

def portable(path, rel): return {**pin(path), 'path': rel}

def read(path): return json.loads(Path(path).read_text())

def write(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n')

def same(path, row):
    current = pin(path)
    assert all(current[key] == row[key] for key in ('bytes', 'sha256')), str(path)

def active(): assert datetime.now(timezone.utc) < DEADLINE, 'Fixed campaign deadline reached'

def object_hash(value): return digest(json.dumps(value, sort_keys=True, separators=(',', ':')).encode())

def edge_hash(edges): return object_hash(sorted(edges, key=lambda row: json.dumps(row, sort_keys=True)))

def git(*args): return subprocess.check_output(['git', *args], cwd=W)

def clean_base():
    assert git('branch', '--show-current').decode().strip() == BASE_BRANCH
    assert git('rev-parse', 'HEAD').decode().strip() == BASE
    assert git('status', '--porcelain', '-z') == b''

def frozen_proposal():
    for row in read(OUT / 'FINAL_FREEZE.json')['files']: same(OUT / row['path'], row)

def run(label, argv, *, cwd=W, expected=(0,), timeout=60):
    active(); folder = D / 'runs' / label
    folder.mkdir(parents=True, exist_ok=False)
    argv = [str(arg) for arg in argv]
    source = None; input_record = None
    if Path(argv[0]).name.startswith('python'):
        tail = argv[1:]
        while tail and tail[0] in ('-B', '-u'): tail = tail[1:]
        if tail and not tail[0].startswith('-'):
            candidate = Path(tail[0]); candidate = candidate if candidate.is_absolute() else Path(cwd) / candidate
            if candidate.is_file():
                source = pin(candidate); (folder / 'executed_source.py').write_bytes(candidate.read_bytes())
                if candidate.name == Path(HELPER).name:
                    tree = ast.parse(candidate.read_bytes()); declared = None
                    for node in tree.body:
                        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in node.targets): declared = ast.literal_eval(node.value)
                    assert declared is not None
                    root = candidate.resolve().parents[1]
                    write(folder / 'INPUTS.json', {'declared_inputs': [pin(root / rel) for rel in declared]})
                    input_record = pin(folder / 'INPUTS.json')
    (folder / 'recorder_source.py').write_bytes(Path(__file__).read_bytes())
    launch = {'started_utc': now(), 'argv': argv, 'cwd': str(cwd), 'source_at_launch': source,
              'recorder': pin(__file__), 'inputs_at_launch': input_record, 'timeout_seconds': timeout, 'scientific_execution': False}
    write(folder / 'LAUNCH.json', launch)
    started = time.monotonic()
    try:
        result = subprocess.run(argv, cwd=cwd, capture_output=True, timeout=timeout)
        code, stdout, stderr = result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired as exc:
        code, stdout, stderr = 124, exc.stdout or b'', (exc.stderr or b'') + b'\nTimeout\n'
    (folder / 'stdout').write_bytes(stdout); (folder / 'stderr').write_bytes(stderr)
    write(folder / 'EXECUTION.json', {'start_utc': launch['started_utc'], 'end_utc': now(),
          'argv': argv, 'cwd': str(cwd), 'recorder': launch['recorder'], 'child_source_at_launch': source,
          'finished_utc': now(), 'exit_code': code,
          'elapsed_seconds': time.monotonic() - started, 'launch': pin(folder / 'LAUNCH.json'),
          'stdout': pin(folder / 'stdout'), 'stderr': pin(folder / 'stderr')})
    assert code in expected, str(folder)
    return stdout

def require_bound_base():
    binding=read(OUT/'BASE_BINDING_INPUT.json')
    assert binding['status']=='bound_actual_root_published_base'
    assert BASE=='7cce8eaa5a72862e0ba884028a21e792c04a6df7' and binding['base_head']==BASE
    assert ROOT_BINDING is not None and ROOT_BINDING['status']=='bound_actual_root_publication_review'
    same(ROOT_BINDING['_runtime_pin']['path'],ROOT_BINDING['_runtime_pin'])
    for key in ('review','execution','refresh','integration_review','integration_execution','integration_proposal'):same(ROOT_BINDING[key]['path'],ROOT_BINDING[key])
    publication=read(OUT/binding['root_publication_receipt'])
    assert publication['headRefOid']==BASE and publication['tree']==binding['base_tree']
    assert publication['number']==BASE_PR and publication['headRefName']==BASE_BRANCH and publication['baseRefName']==BASE_PARENT_BRANCH
    assert publication['isDraft'] is False and publication['state']=='OPEN'
    envelope=read(OUT/binding['root_attachment_receipt'])
    assert envelope['tool']=='mcp__codex_app__attach_artifact' and envelope['arguments']=={'artifact_type':'pull_request','url':publication['url']}
    result=envelope['actual_result'];assert result['isError'] is False
    assert any(json.loads(row['text'])=={'artifact_type':'pull_request','url':publication['url']} for row in result['content'] if row['type']=='text')
    refresh=read(ROOT_BINDING['refresh']['path'])
    assert refresh['refs']=={'HEAD':BASE,'origin/main':EXPECTED_MAIN,'origin/ai/execution':EXPECTED_INSTRUCTIONS}
    assert refresh['active_tree']==binding['base_tree'] and isinstance(EXPECTED_MAIN,str) and re.fullmatch('[0-9a-f]{40}',EXPECTED_MAIN)
    same(refresh['inventory']['path'],refresh['inventory'])
    assert refresh['actual_receipts']
    for row in refresh['actual_receipts']:
        same(row['path'],row);receipt=read(row['path']);assert receipt['exit_code']==0
        for key in ('stdout','stderr'):same(receipt[key]['path'],receipt[key])
    review=read(ROOT_REVIEW)
    assert review['source_freeze']['sha256']==SOURCE_FREEZE and review['disposition']==ROOT_DECISION
    assert review['scientific_executions']==0 and review['immutable_bodies']==9
    assert review['source_aliases']==219 and review['archive_objects']==120 and review['root_read_complete'] is True
    assert review['actual_canonical_acceptance'] is None and review['retained_audit'] is False
    same(SOURCE/'proposal'/NOTE,review['source_note']);same(SOURCE/'proposal'/HELPER,review['source_validator'])
    same(SOURCE/'proposal'/PACKET/'SOURCE_MANIFEST.json',review['source_manifest'])
    verify_actual_review_execution(ROOT_BINDING['review'],ROOT_BINDING['execution'])
    observed=read(OUT/'OBSERVED_SOURCE_REVIEW.json')
    same(ROOT_REVIEW,observed['review'])
    same(ROOT_BINDING['execution']['path'],observed['runs'][1])
    for row in observed['aliases']:same(OUT/row['recovery']['path'],row['recovery'])
    integration=read(ROOT_BINDING['integration_review']['path'])
    assert integration['kind']=='root_integration_source_review' and integration['root_read_complete_for_changed_implementation'] is True
    same(OUT/'FINAL_FREEZE.json',integration['proposal_freeze']);same(__file__,integration['common'])
    same(OUT/'proposed_primary_unbound.py',integration['primary_unbound']);same(ROOT_REVIEW,integration['source_publication_review'])
    same(OUT/'FINAL_FREEZE.json',ROOT_BINDING['integration_proposal'])
    verify_actual_review_execution(ROOT_BINDING['integration_review'],ROOT_BINDING['integration_execution'])
    for row in read(OUT/'EXECUTION_TOOL_PINS.json')['files']:same(W/row['path'],row)

def verify_actual_review_execution(review_row,execution_row):
    same(review_row['path'],review_row);same(execution_row['path'],execution_row)
    receipt=read(execution_row['path'])
    assert receipt['exit_code']==0 and receipt['start_utc']<=receipt['end_utc'] and receipt['cwd']==str(N.parent)
    assert len(receipt['argv'])>=2 and receipt['argv'][1]==receipt['child_source_at_launch']['path']
    assert receipt['source_capture']['path']!=receipt['child_source_at_launch']['path']
    for key in ('recorder','stdout','stderr','source_capture'):same(receipt[key]['path'],receipt[key])
    same(receipt['source_capture']['path'],receipt['child_source_at_launch'])
    assert Path(receipt['stderr']['path']).read_bytes()==b''
    observed=read(receipt['stdout']['path']);same(review_row['path'],observed['review'])
    if 'freeze' in observed:same(observed['freeze']['path'],observed['freeze'])
    return receipt

def parent_query(label):
    observed={}
    for role,number,head,branch,base_branch in PR_SPECS:
        row=json.loads(run(label+'_'+role,['gh','pr','view',str(number),'--repo',REPOSITORY,'--json','number,state,isDraft,headRefOid,headRefName,baseRefName,url']))
        assert row['state']=='OPEN' and row['isDraft'] is False and row['number']==number, 'Fixed-stack proposal requires live OPEN parent; separately review current-main transport after closure'
        assert row['headRefOid']==head and row['headRefName']==branch and row['baseRefName']==base_branch
        observed[role]=row
    return observed

def no_duplicate(label):
    result = json.loads(run(label, ['gh', 'pr', 'list', '--repo', REPOSITORY, '--state', 'all',
            '--head', FEATURE, '--json', 'number,state,headRefName,url']))
    assert result == [], 'Existing PR requires deliberate continuation, not another creation'

def installed():
    assert git('branch','--show-current').decode().strip()==FEATURE
    assert git('rev-parse','HEAD').decode().strip()==BASE
    original=read(D/'PREPARED.json')
    if (D/'BOUND_CANONICAL.json').exists():
        prepared=read(D/'BOUND_CANONICAL.json');same(D/'PREPARED.json',prepared['original_prepared'])
    else:prepared=original
    for path,row in prepared['canonical_files'].items():same(W/path,row)
    return prepared

def cache_module():
    sys.dont_write_bytecode = True; os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
    sys.path.insert(0, str(W / 'scripts'))
    import runner_cache
    return runner_cache

def repin(root):
    manifest_path=root/PACKET/'INPUT_MANIFEST.json';manifest=read(manifest_path)
    for row in manifest['inputs']:
        target=root/row['path']
        if not target.exists():
            assert row['path'] in EXTERNAL_INPUTS;target=W/row['path']
        row.update(portable(target,row['path']))
    write(manifest_path,manifest)
    helper=root/HELPER;text=helper.read_text()
    text,count=re.subn(r'^MANIFEST_SHA256\s*=.*$','MANIFEST_SHA256 = '+repr(pin(manifest_path)['sha256']),text,flags=re.M)
    assert count==1;helper.write_text(text.rstrip()+'\n')

def prepare(args):
    frozen_proposal();require_bound_base();clean_base()
    assert git('rev-parse','HEAD^{tree}').decode().strip()==BASE_BINDING['base_tree']
    assert args.reviewed_source_sha==SOURCE_FREEZE
    assert pin(SOURCE/'FREEZE.json')['sha256']==SOURCE_FREEZE
    freeze=read(SOURCE/'FREEZE.json')
    for row in freeze['members']:same(SOURCE/row['path'],row)
    assert {str(p.relative_to(SOURCE)) for p in SOURCE.rglob('*') if p.is_file()}=={r['path'] for r in freeze['members']}|{'FREEZE.json'}
    review=read(ROOT_REVIEW)
    same(SOURCE/'proposal'/NOTE,review['source_note']);same(SOURCE/'proposal'/HELPER,review['source_validator'])
    refresh=read(ROOT_BINDING['refresh']['path'])
    for ref in ('origin/main','origin/ai/execution'):
        assert git('rev-parse',ref).decode().strip()==refresh['refs'][ref], 'Reference changed; root must re-review and rebind'
    parent=parent_query('prepare_parent');no_duplicate('prepare_duplicates')
    local_head=run('prepare_local_base',['git','rev-parse','HEAD']).decode().strip();assert local_head==BASE
    assert not git('branch','--list',FEATURE).strip() and not STAGE.exists()
    shutil.copytree(OUT/'payload',STAGE)
    shutil.copytree(SOURCE,STAGE/PACKET/'frozen_source')
    canonical=(STAGE/NOTE).read_bytes();mapping=read(STAGE/PACKET/'BODY_MAP.json')
    source_body_pins=read(SOURCE/'proposal'/PACKET/'BODY_MAP.json')['bodies']
    assert len(source_body_pins)==9 and {r['name']:r['sha256'] for r in source_body_pins}==EXPECTED_SOURCE_BODIES
    for row,original in zip(mapping['bodies'],source_body_pins):
        raw=(SOURCE/'proposal'/NOTE).read_bytes()[original['start_byte_inclusive']:original['end_byte_exclusive']]
        assert canonical[row['start_byte']:row['end_byte_exclusive']]==raw and digest(raw)==row['sha256']
    for staged,preview in [(NOTE,'PROPOSED_NOTE.md'),(PACKET+'/BODY_MAP.json','PROPOSED_BODY_MAP.json'),
        (PACKET+'/SOURCE_MANIFEST.json','PROPOSED_SOURCE_MANIFEST.json'),
        (PACKET+'/CLAIM_STATUS_CERTIFICATE.md','PROPOSED_CLAIM_STATUS_CERTIFICATE.md')]:same(STAGE/staged,pin(OUT/preview))
    binding_spec=read(OUT/'PARENT_BINDING.json')
    assert read(STAGE/PACKET/'PARENT_BINDING.json')==binding_spec
    for row in binding_spec['direct_canonical_parents']:same(W/row['path'],row)
    def copy_blob(source):
        source=Path(source);raw=source.read_bytes();target=STAGE/PACKET/'binding_sources'/(digest(raw)+(source.suffix or '.blob'))
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==raw
        else:target.write_bytes(raw)
        return portable(target,str(target.relative_to(STAGE)))
    source_seal=copy_blob(SOURCE/'FREEZE.json')
    source_map=copy_blob(SOURCE/'proposal'/PACKET/'BODY_MAP.json');source_note=copy_blob(SOURCE/'proposal'/NOTE)
    source_manifest_pin=copy_blob(SOURCE/'proposal'/PACKET/'SOURCE_MANIFEST.json')
    source_state=copy_blob(SOURCE/'proposal'/PACKET/'PUBLICATION_STATE.json')
    receipt=read(ROOT_BINDING['execution']['path'])
    root_evidence={'review':copy_blob(ROOT_REVIEW),'review_text':copy_blob(ROOT_REVIEW.parent/'REVIEW.md'),
        'freeze':copy_blob(ROOT_REVIEW.parent/'FREEZE.json'),'execution':copy_blob(ROOT_BINDING['execution']['path']),
        'recorder':copy_blob(receipt['recorder']['path']),'stdout':copy_blob(ROOT_REVIEW_RUN/'stdout'),
        'stderr':copy_blob(ROOT_REVIEW_RUN/'stderr'),'source':copy_blob(ROOT_REVIEW_RUN/'executed_source.py')}
    def observation(label):
        folder=D/'runs'/label;e=read(folder/'EXECUTION.json')
        return {'execution':copy_blob(folder/'EXECUTION.json'),'recorder':copy_blob(e['recorder']['path']),
                'stdout':copy_blob(folder/'stdout'),'stderr':copy_blob(folder/'stderr')}
    parent_evidence=observation('prepare_parent_base');head_evidence=observation('prepare_local_base')
    write(D/'BASE_OBSERVATION.json',{'observed_commit':local_head,'source_revision_verified':True,'execution_evidence':head_evidence,
        'scope':'Actual clean stacked base checked at prepare; main/instructions independently pinned.'})
    base_observation=copy_blob(D/'BASE_OBSERVATION.json')
    receipt_paths=sorted({source_seal['path'],source_map['path'],source_note['path'],source_manifest_pin['path'],source_state['path'],base_observation['path']}|
        {r['path'] for r in root_evidence.values()}|{r['path'] for r in parent_evidence.values()}|{r['path'] for r in head_evidence.values()})
    support={'refresh':copy_blob(ROOT_BINDING['refresh']['path']),'root_binding':copy_blob(ROOT_BINDING['_runtime_pin']['path']),
        'integration_review':copy_blob(ROOT_BINDING['integration_review']['path']),'integration_proposal':copy_blob(OUT/'FINAL_FREEZE.json'),
        'base_publication':copy_blob(OUT/BASE_BINDING['root_publication_receipt']),'base_attachment':copy_blob(OUT/BASE_BINDING['root_attachment_receipt']),
        'inventory':copy_blob(refresh['inventory']['path']),'actual_refresh_receipts':[], 'integration_review_execution':{}}
    integration_execution=read(ROOT_BINDING['integration_execution']['path'])
    support['integration_review_execution']['execution']=copy_blob(ROOT_BINDING['integration_execution']['path'])
    for key in ('recorder','stdout','stderr','source_capture'):support['integration_review_execution'][key]=copy_blob(integration_execution[key]['path'])
    observed=read(OUT/'OBSERVED_SOURCE_REVIEW.json')
    support['source_review_recovery']={'manifest':copy_blob(OUT/'OBSERVED_SOURCE_REVIEW.json'),
        'original_aliases_and_recovered_blobs':[{'original':row['original'],'captured':copy_blob(OUT/row['recovery']['path'])} for row in observed['aliases']]}
    for row in refresh['actual_receipts']:
        e=read(row['path']);support['actual_refresh_receipts'].append({'execution':copy_blob(row['path']),
            'stdout':copy_blob(e['stdout']['path']),'stderr':copy_blob(e['stderr']['path'])})
    write(STAGE/PACKET/'ACTUAL_REFRESH_PROVENANCE.json',{'kind':'actual_root_refresh_provenance','evidence':support,
        'scope':'Actual root Git/source refresh; Git ancestry is not a mathematical dependency.'})
    actual={'kind':'root_reviewed_canonical_binding','utc':now(),'root_read_complete':False,'source_draft_read_complete':True,
        'canonical_parent_binding_complete':True,'note_sha256':digest(canonical),'git_base':BASE,'base_branch':BASE_BRANCH,
        'source_body_pins':source_body_pins,'raw_bodies':mapping['bodies'],'parent_binding':binding_spec,
        'source_proposal_freeze':source_seal,'source_draft_body_map':source_map,'source_draft_note':source_note,'source_draft_manifest':source_manifest_pin,'source_draft_state':source_state,
        'root_review_evidence':root_evidence,'canonical_review_evidence':None,'base_observation':base_observation,
        'parent_pr_observation':parent_evidence,'observed_parent_prs':parent,'receipt_paths':receipt_paths,
        'origin_main':EXPECTED_MAIN,'instruction_revision':EXPECTED_INSTRUCTIONS,'new_scientific_execution':False,'retained_audit':False}
    write(STAGE/PACKET/'ACTUAL_BINDING.json',actual)
    write(STAGE/PACKET/'CANONICAL_BINDING.json',{'kind':'actual_interacting_control_binding','canonical_parent_binding_complete':True,
        'root_read_complete':False,'source_draft_read_complete':True,'actual_checkout_head':BASE,'actual_git_base':BASE,
        'bound_note_sha256':digest(canonical),'receipt_paths':receipt_paths})
    (STAGE/PACKET/'PR_TITLE.txt').write_text(TITLE+'\n')
    manifest_path=PACKET+'/INPUT_MANIFEST.json'
    rows=[portable(p,str(p.relative_to(STAGE))) for p in sorted(STAGE.rglob('*')) if p.is_file() and str(p.relative_to(STAGE)) not in (HELPER,manifest_path)]
    rows.extend(portable(W/path,path) for path in EXTERNAL_INPUTS)
    write(STAGE/manifest_path,{'schema':'source_integrity_inputs_v1','inputs':rows,'scope':'Provenance only.'})
    helper=(OUT/'proposed_primary_unbound.py').read_text()
    for key,value in {'AUDIT_INPUT_PATHS':tuple(sorted({r['path'] for r in rows}|{manifest_path})),
        'EXPECTED_GIT_BASE':BASE,'EXPECTED_BASE_PR':BASE_PR,'EXPECTED_BASE_BRANCH':BASE_BRANCH,
        'EXPECTED_BASE_PARENT_BRANCH':BASE_PARENT_BRANCH,'EXPECTED_ROOT_REVIEW_SHA':ROOT_REVIEW_SHA,
        'EXPECTED_ROOT_REVIEW_COMMAND':tuple(receipt['argv']),
        'EXPECTED_ROOT_EXECUTION_SHA':ROOT_BINDING['execution']['sha256'],
        'EXPECTED_ROOT_RECORDER_SHA':receipt['recorder']['sha256']}.items():
        helper,count=re.subn(r'^'+key+r'\s*=.*$',lambda m:key+' = '+repr(value),helper,flags=re.M);assert count==1,key
    (STAGE/HELPER).parent.mkdir(parents=True,exist_ok=True)
    (STAGE/HELPER).write_text(helper.rstrip()+'\n');repin(STAGE);ast.parse((STAGE/HELPER).read_bytes())
    assert (STAGE/PACKET/'frozen_source/proposal'/PACKET/'PUBLICATION_STATE.json').read_bytes()==(SOURCE/'proposal'/PACKET/'PUBLICATION_STATE.json').read_bytes()
    delta=(OUT/'NOTE_FULL.diff').read_text()
    for path in sorted(STAGE.rglob('*')):
        if not path.is_file():continue
        name=str(path.relative_to(STAGE));old=OUT/'payload'/name
        if name.startswith(PACKET+'/frozen_source/'):old=SOURCE/name.removeprefix(PACKET+'/frozen_source/')
        if old.exists() and old.read_bytes()==path.read_bytes():continue
        delta+=''.join(difflib.unified_diff(old.read_text().splitlines(True) if old.exists() else [],path.read_text().splitlines(True),fromfile='draft/'+name,tofile='canonical/'+name))
    (D/'CANONICALIZATION.diff').write_text(delta)
    graph,manifest=read(W/GRAPH),read(W/GRAPH_MANIFEST)
    assert CLAIM not in graph['nodes'] and all(cid in graph['nodes'] for cid in PARENT_CLAIMS)
    write(D/'GRAPH_BASELINE.json',{'graph':pin(W/GRAPH),'manifest':pin(W/GRAPH_MANIFEST),'node_count':len(graph['nodes']),
        'edge_count':len(graph['edges']),'nodes_hash':object_hash(graph['nodes']),'edges_hash':edge_hash(graph['edges']),
        'roots_hash':object_hash(graph['roots']),'manifest_nodes_hash':object_hash(manifest['nodes'])})
    files={str(p.relative_to(STAGE)):pin(p) for p in sorted(STAGE.rglob('*')) if p.is_file()}
    write(D/'PREPARED.json',{'utc':now(),'canonical_files':files,'base_head':BASE,'planned_feature_branch':FEATURE,
        'diff':pin(D/'CANONICALIZATION.diff'),'binding':pin(STAGE/PACKET/'ACTUAL_BINDING.json'),
        'source_proposal_freeze':pin(SOURCE/'FREEZE.json'),'primary_executed':False,'scientific_programs_run':0})
    print(json.dumps({'prepared':pin(D/'PREPARED.json'),'review_diff':pin(D/'CANONICALIZATION.diff')}))
def install(args):
    clean_base(); prepared = read(D / 'PREPARED.json')
    same(D / 'CANONICALIZATION.diff', prepared['diff'])
    assert args.reviewed_diff_sha == prepared['diff']['sha256'], 'Root must inspect and supply the exact reviewed diff hash'
    for path, row in prepared['canonical_files'].items():
        same(STAGE / path, row); assert not (W / path).exists(), path
    write(D / 'ROOT_CANONICAL_REVIEW.json', {'utc': now(), 'root_supplied_reviewed_diff_sha256': args.reviewed_diff_sha,
        'scope': 'Root invocation acknowledges inspection of this exact canonicalization diff; the script does not manufacture independent scientific review.',
        'source_proposal_freeze': prepared['source_proposal_freeze'], 'retained_audit': False})
    run('create_branch', ['git', 'switch', '-c', FEATURE])
    for path in prepared['canonical_files']:
        (W / path).parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(STAGE / path, W / path)
    installed(); write(D / 'INSTALLED.json', {'utc': now(), 'files': prepared['canonical_files'], 'branch': FEATURE, 'base_head': BASE})

def cache(args):
    bind_canonical_review(args); installed(); run('primary_separate_streams', [sys.executable, '-B', HELPER], timeout=60)
    runner = cache_module()
    assert runner.declared_timeout_for(HELPER) == 60
    result, cache_path = runner.execute_and_write_cache(HELPER, timeout_sec=60)
    write(D / 'CANONICAL_RESULT.json', result)
    assert result['exit_code'] == 0 and result['status'] == 'ok' and cache_path
    assert runner.cache_status(HELPER) == 'fresh'
    summaries = [json.loads(line) for line in result['stdout'].splitlines() if line.startswith('{')]
    assert len(summaries) == 1; summary = summaries[0]
    assert summary['result'] == 'source_integrity_verified' and summary['scientific_programs_run_this_primary'] == summary['historical_programs_replayed'] == 0
    assert summary['mathematics_or_retention_certified'] is False
    scopes = [line for line in result['stdout'].splitlines() if line.split(':', 1)[0] in ('per_element', 'per_site', 'per_mode', 'per_block', 'lattice_wide')]
    assert len(scopes) == 5
    cached = Path(cache_path); cached = cached if cached.is_absolute() else W / cached
    write(D / 'CANONICAL_EXECUTION.json', {'utc': now(), 'primary': pin(W / HELPER), 'result': pin(D / 'CANONICAL_RESULT.json'),
        'cache': pin(cached), 'timeout_seconds': 60, 'cache_fresh': True, 'summary': summary, 'scope_lines': scopes,
        'scientific_programs_run': 0, 'child_stream_limit': 'runner_cache merges child stderr into stdout; result.stderr is not a separate child-stderr capture.'})
    installed()

def verify(args):
    prepared=installed();paths=sorted(prepared['canonical_files'])
    cases=[('baseline',None),('manifest_identity','Input manifest identity'),('source_identity','Input identity mismatch'),
        ('body_interval','Canonical body identity'),('unexpected_parent','Exact parent binding'),
        ('historical_outcome','Historical publication state'),('actual_note','Actual note/base linkage'),
        ('root_review_exit','Successful captured execution'),('root_source_at_launch','Input identity mismatch'),
        ('root_output_linkage','Actual review output linkage'),('base_command','Actual base observation command'),
        ('base_identity','Actual base PR identity'),('receipt_membership','Exact binding evidence membership'),
        ('canonical_review_identity','Exact canonical review identity'),('root_capture_schema','Explicit captured source required'),
        ('recovery_interval','Canonical recovery interval'),('root_capture_alias','Distinct original and captured source'),
        ('canonical_capture_alias','Distinct original and captured source'),('canonical_execution_identity','Exact canonical execution identity'),
        ('canonical_certificate','Canonical certificate identity'),
        ('wrapper_trailer','Canonical closing wrapper'),('source_packet_extra','Final packet inventory'),
        ('second_parent_identity','Input identity mismatch')]
    write(D/'MUTATION_PLAN.json',{'utc':now(),'primary':pin(W/HELPER),'cases':cases,'scope':'Provenance-only semantic guard probes with outer pins refreshed.'})
    results=[]
    for name,expected in cases:
        root=D/'mutation_scratch'/name;root.mkdir(parents=True,exist_ok=False)
        for path in paths+list(EXTERNAL_INPUTS):
            (root/path).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(W/path,root/path)
        def mutate(filename,fn):
            path=root/PACKET/filename;value=read(path);fn(value);write(path,value)
        def evidence_change(group,key,fn,link_stream=False):
            binding=read(root/PACKET/'ACTUAL_BINDING.json');row=binding[group][key];path=root/row['path']
            value=read(path);fn(value);write(path,value);binding[group][key]=portable(path,row['path'])
            if link_stream:
                erow=binding[group]['execution'];epath=root/erow['path'];receipt=read(epath)
                receipt[key].update({k:pin(path)[k] for k in ('bytes','sha256')});write(epath,receipt)
                binding[group]['execution']=portable(epath,erow['path'])
            write(root/PACKET/'ACTUAL_BINDING.json',binding)
        if name=='manifest_identity':
            path=root/PACKET/'INPUT_MANIFEST.json';path.write_bytes(path.read_bytes()+b' ')
        elif name=='source_identity':
            path=root/NOTE;path.write_bytes(path.read_bytes()+b' ')
        elif name=='body_interval':mutate('BODY_MAP.json',lambda v:v['bodies'][0].__setitem__('start_byte',v['bodies'][0]['start_byte']+1))
        elif name=='unexpected_parent':mutate('PARENT_BINDING.json',lambda v:v['direct_canonical_parents'].append({'path':'docs/unaccepted.md'}))
        elif name=='historical_outcome':mutate('PUBLICATION_STATE.json',lambda v:v.__setitem__('actual_new_publication',True))
        elif name=='actual_note':mutate('ACTUAL_BINDING.json',lambda v:v.__setitem__('note_sha256','0'*64))
        elif name=='root_review_exit':evidence_change('root_review_evidence','execution',lambda v:v.__setitem__('exit_code',1))
        elif name=='root_capture_schema':evidence_change('root_review_evidence','execution',lambda v:v.pop('source_capture'))
        elif name=='root_source_at_launch':evidence_change('root_review_evidence','execution',lambda v:v['child_source_at_launch'].__setitem__('sha256','0'*64))
        elif name=='root_output_linkage':evidence_change('root_review_evidence','stdout',lambda v:v['review'].__setitem__('sha256','0'*64),True)
        elif name=='base_command':evidence_change('parent_pr_observation','execution',lambda v:v['argv'].__setitem__(3,'0'))
        elif name=='base_identity':evidence_change('parent_pr_observation','stdout',lambda v:v.__setitem__('headRefOid','0'*40),True)
        elif name=='receipt_membership':mutate('ACTUAL_BINDING.json',lambda v:v['receipt_paths'].pop())
        elif name=='canonical_review_identity':evidence_change('canonical_review_evidence','review',lambda v:v.__setitem__('bound_note_sha256','0'*64))
        elif name=='recovery_interval':mutate('SOURCE_MANIFEST.json',lambda v:v['current_body_recovery_intervals'][0].__setitem__('start_byte',0))
        elif name in ('root_capture_alias','canonical_capture_alias'):
            evidence_change('root_review_evidence' if name.startswith('root') else 'canonical_review_evidence','execution',lambda v:v['source_capture'].__setitem__('path',v['child_source_at_launch']['path']))
        elif name=='canonical_execution_identity':evidence_change('canonical_review_evidence','execution',lambda v:v.__setitem__('unused_metadata_mutation',True))
        elif name=='canonical_certificate':
            path=root/PACKET/'CLAIM_STATUS_CERTIFICATE.md';path.write_bytes(path.read_bytes()+b' ')
        elif name=='wrapper_trailer':mutate('BODY_MAP.json',lambda v:v['trailer'].__setitem__('start_byte',v['trailer']['start_byte']+1))
        elif name=='source_packet_extra':(root/PACKET/'frozen_source/UNDECLARED.txt').write_text('explicit mutation\n')
        elif name=='second_parent_identity':
            path=root/EXTERNAL_INPUTS[1];path.write_bytes(path.read_bytes()+b' ')
        if name not in ('baseline','manifest_identity','source_identity'):repin(root)
        run('mutation_'+name,[sys.executable,'-B',root/HELPER],cwd=root,expected=(0,) if expected is None else (1,),timeout=60)
        receipt=D/'runs'/('mutation_'+name)/'EXECUTION.json'
        if expected:assert expected in (receipt.parent/'stderr').read_text(),name
        results.append({'case':name,'expected_failure':expected,'receipt':pin(receipt)})
    write(D/'MUTATION_RESULTS.json',{'utc':now(),'cases':results,'baseline_exit':0,'mutants_rejected':len(cases)-1,'scientific_programs_run':0})
    run('compile',[sys.executable,'-B','-c','import ast,pathlib,sys; ast.parse(pathlib.Path(sys.argv[1]).read_bytes())',HELPER])
    active_paths=[p for p in paths if '/archive/' not in p and '/binding_sources/' not in p and '/frozen_source/' not in p and Path(p).suffix in ('.md','.json','.py')]
    before={p:pin(W/p) for p in paths}
    run('vocab_fix',[sys.executable,'-B','scripts/vocab_lint.py','--fix',*active_paths])
    for path,row in before.items():same(W/path,row)
    run('vocab_report',[sys.executable,'-B','scripts/vocab_lint.py','--report-only',*active_paths])
    for path,row in before.items():same(W/path,row)
    index=git('ls-files','--stage','-z')
    focused=json.loads(run('changed_evidence',[sys.executable,'-B','docs/audit/scripts/check_changed_audit_evidence.py','--base','HEAD','--include-worktree','--json']))
    assert git('ls-files','--stage','-z')==index and not focused.get('failures') and not focused.get('control_failures')
    assert cache_module().cache_status(HELPER)=='fresh'
    write(D/'SOURCE_VERIFICATION.json',{'utc':now(),'primary':pin(W/HELPER),'mutations':pin(D/'MUTATION_RESULTS.json'),
        'focused_checker':focused,'index_preserved':True,'vocabulary_source_changes':False,'historical_bytes_untouched':True,
        'scientific_programs_run':0,'scope':'Source/provenance only; current-main/cumulative-stack and audit remain separate.'})
    installed()
def graph(args):
    installed();before=read(D/'GRAPH_BASELINE.json')
    same(W/GRAPH,before['graph']);same(W/GRAPH_MANIFEST,before['manifest'])
    run('graph_build',[sys.executable,'-B','docs/audit/scripts/run_citation_graph_build.py'],timeout=180)
    value=read(W/GRAPH);nodes=dict(value['nodes']);node=nodes.pop(CLAIM)
    assert object_hash(nodes)==before['nodes_hash'] and len(nodes)==before['node_count']
    assert node['path']==NOTE and node['runner_path']==HELPER and set(node['deps'])==set(PARENT_CLAIMS) and len(node['deps'])==len(PARENT_CLAIMS)
    edges=[{'from':CLAIM,'to':cid} for cid in PARENT_CLAIMS];remaining=list(value['edges'])
    for edge in edges:assert remaining.count(edge)==1;remaining.remove(edge)
    assert edge_hash(remaining)==before['edges_hash'] and len(remaining)==before['edge_count']
    assert CLAIM not in value['roots']
    assert object_hash(value['roots'])==before['roots_hash']
    assert len(value['nodes'])==before['node_count']+1 and len(value['edges'])==before['edge_count']+len(PARENT_CLAIMS)
    run('graph_manifest',[sys.executable,'-B','docs/audit/scripts/write_citation_graph_manifest.py'])
    manifest=read(W/GRAPH_MANIFEST);old_nodes=dict(manifest['nodes']);old_nodes.pop(CLAIM)
    assert object_hash(old_nodes)==before['manifest_nodes_hash']
    assert manifest['node_count']==len(value['nodes']) and manifest['edge_count']==len(value['edges'])
    assert git('ls-files','--',GRAPH)==b'';run('ignored_graph',['git','check-ignore','-v',GRAPH])
    write(D/'GRAPH_VERIFICATION.json',{'utc':now(),'old_nodes_preserved':before['node_count'],'old_edges_preserved':before['edge_count'],
        'new_node':node,'new_edges':edges,'old_roots_preserved':True,'new_roots':[],'graph':pin(W/GRAPH),'manifest':pin(W/GRAPH_MANIFEST),
        'baseline':pin(D/'GRAPH_BASELINE.json'),'method':'Canonical object digests preserve every old node/edge/root without copying full graphs.',
        'graph_json_ignored_not_staged':True})

def historical_attributes(paths):
    affected=[];added=read(W/PACKET/'ACTUAL_BINDING.json')
    bindings={row['path']:row for group in ('root_review_evidence','canonical_review_evidence','parent_pr_observation') for row in added[group].values()}
    for name in paths:
        if '/frozen_source/' not in name and '/binding_sources/' not in name:continue
        data=(W/name).read_bytes();original=SOURCE/name.removeprefix(PACKET+'/frozen_source/') if name.startswith(PACKET+'/frozen_source/') else Path('/__no_original_binding_source__')
        if original.exists():assert original.read_bytes()==data
        else:
            # Newly captured actual reviews are not falsely required to predate binding.
            manifest=read(W/PACKET/'INPUT_MANIFEST.json')
            rows=[r for r in manifest['inputs'] if r['path']==name];assert len(rows)==1;same(W/name,rows[0])
            assert digest(data)==Path(name).stem
        try:text=data.decode()
        except UnicodeDecodeError:continue
        if data.endswith(b'\n\n') or any(line.endswith((' ','\t')) or re.match(r'^ +\t',line) for line in text.splitlines()):affected.append(name)
    if not affected:return []
    attr=W/'.gitattributes';old=attr.read_bytes() if attr.exists() else b'';(D/'GITATTRIBUTES_BEFORE').write_bytes(old)
    attr.write_bytes(old+(b'\n' if old and not old.endswith(b'\n') else b'')+''.join('/'+name+' -whitespace\n' for name in sorted(affected)).encode())
    write(D/'HISTORICAL_ATTRIBUTES.json',{'utc':now(),'exact_paths':affected,'before':pin(D/'GITATTRIBUTES_BEFORE'),
        'after':pin(attr),'scope':'Exact immutable archive/captured evidence bytes only; active prose is not normalized.'})
    return ['.gitattributes']

def finish(args):
    prepared = installed(); runner = cache_module(); assert runner.cache_status(HELPER) == 'fresh'
    for name in read(OUT/'ARCHIVE_CLOSURE.json')['integration_files']:
        assert (D/name).is_file(), 'Missing exact finish closure member: '+name
    source = read(D / 'SOURCE_VERIFICATION.json'); graph_record = read(D / 'GRAPH_VERIFICATION.json')
    execution = read(D / 'CANONICAL_EXECUTION.json'); mutations = read(D / 'MUTATION_RESULTS.json')
    same(W / HELPER, execution['primary']); same(execution['cache']['path'], execution['cache'])
    same(W / GRAPH, graph_record['graph']); same(W / GRAPH_MANIFEST, graph_record['manifest'])
    for row in mutations['cases']:
        same(row['receipt']['path'], row['receipt']); receipt = read(row['receipt']['path'])
        assert receipt['exit_code'] == (0 if row['expected_failure'] is None else 1)
        for key in ('stdout', 'stderr'): same(receipt[key]['path'], receipt[key])
    packet = W / PACKET
    sections = read(OUT / 'INTEGRATION_SECTIONS.json')
    review = '# Actual focused integration review\n\n' + '\n\n'.join('## ' + str(i) + '. ' + title + '\n\n' + body for i, (title, body) in enumerate(sections, 1)) + '\n'
    (packet / 'INTEGRATION_REVIEW.md').write_text(review)
    run('vocab_integration_report', [sys.executable, '-B', 'scripts/vocab_lint.py', '--report-only', PACKET + '/INTEGRATION_REVIEW.md'])
    originals = {}; archive_paths = []
    closure=read(OUT/'ARCHIVE_CLOSURE.json')
    selected=[]
    for row in closure['proposal_files']:
        path=OUT/row['path'];same(path,row);selected.append(path)
    selected += [OUT/'FINAL_FREEZE.json',OUT/'ARCHIVE_CLOSURE.json']
    selected += [D/name for name in closure['integration_files']]
    allowed_runs=set(closure['runtime_run_labels'])
    assert {p.name for p in (D/'runs').iterdir() if p.is_dir()}==allowed_runs
    for label in sorted(allowed_runs):
        folder=D/'runs'/label
        assert {p.name for p in folder.iterdir()}<=set(closure['run_member_names'])
        selected += [p for p in folder.iterdir() if p.is_file()]
    for phase in ('prepare','install','cache','verify','graph'):
        folder=D/'actions'/PHASE_ACTION_LABELS.get(phase,phase)
        assert {p.name for p in folder.iterdir()}==set(closure['action_member_names'])
        selected += [folder/name for name in closure['action_member_names']]
    for path in sorted(set(selected)):
        row = pin(path); destination = PACKET + '/publication_evidence/' + row['sha256'] + '.gz'
        target = W / destination; target.parent.mkdir(parents=True, exist_ok=True)
        blob = gzip.compress(path.read_bytes(), mtime=0)
        if target.exists(): assert target.read_bytes() == blob
        else: target.write_bytes(blob)
        originals[str(path)] = {**row, 'stored_path': destination}; archive_paths.append(destination)
    write(packet / 'PUBLICATION_EVIDENCE.json', {'utc': now(), 'originals': originals,
        'scope': 'Selected actual source/provenance receipts, deduplicated by content. No full graph or recursive previous publication archives.'})
    record = {'utc': now(), 'branch': FEATURE, 'base_head': BASE, 'note': pin(W / NOTE), 'primary': pin(W / HELPER),
        'cache': execution, 'source_verification': source, 'graph': graph_record, 'mutations': mutations,
        'scientific_programs_run': 0, 'historical_programs_replayed': 0, 'editable_prompt_files_changed': [],
        'remaining': ['Integrated-current-main and independent audit remain separate. Literal interacting K, positive complements on actual supports, vacuum/isolation, complete controls and clocks remain supplied. All nine bodies, noncommuting ramp/preparation target order, full scalar, original F0 work, growing moment widths and coherent fixed-bandwidth runtime fault assumptions remain qualified. M=L+2 and sufficiently-large idle intervals control the fault example. Runtime fault bounds do not automatically cover preparation or arbitrary baths. One historical floating discriminator is not certified ODE or physical synthesis; later checks are analytical. No autonomous halt, microscopic supply or indefinite reuse claim.']}
    write(packet / 'FINAL_VERIFICATION.json', record)
    paths = sorted(set(prepared['canonical_files']) | set(archive_paths) | {PACKET + '/INTEGRATION_REVIEW.md', PACKET + '/PUBLICATION_EVIDENCE.json', PACKET + '/FINAL_VERIFICATION.json', GRAPH_MANIFEST, str(Path(execution['cache']['path']).relative_to(W))})
    paths += historical_attributes(paths)
    run('stage_exact', ['git', 'add', '--', *sorted(set(paths))])
    staged = set(git('diff', '--cached', '--name-only', '-z').decode().rstrip('\0').split('\0'))
    assert staged == set(paths)
    run('staged_whitespace', ['git', 'diff', '--cached', '--check'])
    assert git('diff', '--name-only', '-z') == b'' and git('ls-files', '--others', '--exclude-standard', '-z') == b''
    installed(); assert runner.cache_status(HELPER) == 'fresh'
    write(D / 'STAGED_VERIFICATION.json', {'utc': now(), 'paths': sorted(staged),
        'pins': {path: pin(W / path) for path in sorted(staged)}, 'primary': pin(W / HELPER),
        'base_head': BASE, 'index_sha256': digest(git('ls-files', '--stage', '-z')), 'root_binding': ROOT_BINDING['_runtime_pin'], 'proposal_freeze': pin(OUT/'FINAL_FREEZE.json'),
        'full_staged_whitespace_check': 'actual exit zero', 'scientific_programs_run': 0})
    link = 'https://github.com/' + REPOSITORY + '/blob/__COMMIT__/'
    body = (OUT / 'PR_BODY_TEMPLATE.md').read_text().replace('__BASE__', BASE).replace('__LINK__', link)
    (D / 'PR_BODY.md').write_text(body)
    print(json.dumps({'staged': pin(D / 'STAGED_VERIFICATION.json'), 'title': TITLE, 'body': pin(D / 'PR_BODY.md')}))
def publish(args):
    prepared = installed(); staged = read(D / 'STAGED_VERIFICATION.json')
    staged_review = require_staged_review(args, staged)
    assert git('diff', '--name-only') == git('ls-files', '--others', '--exclude-standard', '-z') == b''
    assert set(git('diff', '--cached', '--name-only', '-z').decode().rstrip('\0').split('\0')) == set(staged['paths'])
    for path, row in staged['pins'].items(): same(W / path, row)
    for row in read(W / PACKET / 'PUBLICATION_EVIDENCE.json')['originals'].values():
        data = gzip.decompress((W / row['stored_path']).read_bytes())
        assert len(data) == row['bytes'] and digest(data) == row['sha256']
    assert cache_module().cache_status(HELPER) == 'fresh'
    parent_query('precommit_parent'); no_duplicate('precommit_duplicates')
    run('commit', ['git', 'commit', '-m', 'Add conditional interacting preparation control and work theorem note'])
    head = git('rev-parse', 'HEAD').decode().strip(); tree = git('rev-parse', 'HEAD^{tree}').decode().strip()
    assert git('rev-parse', 'HEAD^').decode().strip() == BASE and git('status', '--porcelain') == b''
    run('committed_whitespace', ['git', 'diff', '--check', BASE + '..HEAD'])
    assert set(git('diff', '--name-only', '-z', BASE + '..HEAD').decode().rstrip('\0').split('\0')) == set(staged['paths'])
    write(D / 'COMMIT.json', {'utc': now(), 'head': head, 'tree': tree, 'base_head': BASE, 'branch': FEATURE, 'staged': pin(D / 'STAGED_VERIFICATION.json'), 'staged_review': staged_review})
    body_path = D / 'PR_BODY.md'; body = body_path.read_text()
    assert body.count('__COMMIT__') == 2
    body_path.write_text(body.replace('__COMMIT__', head))
    run('push', ['git', 'push', '--set-upstream', 'origin', FEATURE])
    url = run('create_pr', ['gh', 'pr', 'create', '--repo', REPOSITORY, '--head', FEATURE, '--base', BASE_BRANCH,
        '--title', TITLE, '--body-file', D / 'PR_BODY.md']).decode().strip()
    assert url.startswith('https://github.com/' + REPOSITORY + '/pull/')
    observed = json.loads(run('verify_pr', ['gh', 'pr', 'view', url, '--repo', REPOSITORY, '--json', 'number,state,isDraft,headRefName,headRefOid,baseRefName,url']))
    assert observed['state'] == 'OPEN' and observed['isDraft'] is False
    assert observed['headRefOid'] == head and observed['headRefName'] == FEATURE and observed['baseRefName'] == BASE_BRANCH
    write(D / 'PUBLICATION.json', {'utc': now(), **observed, 'tree': tree, 'base_head': BASE,
        'source_note': pin(W / NOTE), 'primary': pin(W / HELPER), 'body': pin(D / 'PR_BODY.md'),
        'science_merged': False, 'main_pushed': False, 'audit_applied': False, 'editable_prompt_files_changed': [],
        'attachment_status': 'Root must immediately call attach_artifact with this created PR URL.'})
    print(json.dumps(read(D / 'PUBLICATION.json')))
def main(phase):
    parser=argparse.ArgumentParser(description='Unexecuted proposal; root must review and acknowledge every binding before action.')
    parser.add_argument('--root-execute',action='store_true')
    for name in ('root-binding','root-binding-sha','reviewed-diff-sha','reviewed-source-sha','reviewed-staging-sha','staged-review-receipt','staged-review-sha','canonical-review-receipt','canonical-review-sha'):parser.add_argument('--'+name)
    args=parser.parse_args()
    if not args.root_execute:parser.error('No action without explicit --root-execute')
    assert BASE_BINDING['status']=='bound_actual_root_published_base' and isinstance(BASE,str) and re.fullmatch('[0-9a-f]{40}',BASE), 'Actual Git base remains unbound'
    active();frozen_proposal();bind_runtime(args);require_bound_base();previous=phase_guard(phase)
    folder=D/'actions'/PHASE_ACTION_LABELS.get(phase,phase);folder.mkdir(parents=True,exist_ok=False)
    (folder/'common_source.py').write_bytes(Path(__file__).read_bytes())
    entry=Path(sys.argv[0]).resolve();(folder/'entry_source.py').write_bytes(entry.read_bytes())
    write(folder/'LAUNCH.json',{'started_utc':now(),'phase':phase,'argv':sys.argv,'cwd':str(Path.cwd()),
        'common_source_at_launch':pin(__file__),'entry_source_at_launch':pin(entry),'proposal_freeze':pin(OUT/'FINAL_FREEZE.json'),
        'root_binding':ROOT_BINDING['_runtime_pin'],'previous_phase_receipt':previous,'scientific_execution':False})
    stdout,stderr=io.StringIO(),io.StringIO();code=0
    with contextlib.redirect_stdout(stdout),contextlib.redirect_stderr(stderr):
        try:globals()[phase](args)
        except Exception:traceback.print_exc();code=1
    (folder/'stdout').write_text(stdout.getvalue());(folder/'stderr').write_text(stderr.getvalue())
    write(folder/'EXECUTION.json',{'finished_utc':now(),'exit_code':code,'launch':pin(folder/'LAUNCH.json'),
        'stdout':pin(folder/'stdout'),'stderr':pin(folder/'stderr')})
    print(stdout.getvalue(),end='');print(stderr.getvalue(),end='',file=sys.stderr)
    print(json.dumps({'phase':phase,'actual_receipt':str(folder/'EXECUTION.json'),'exit_code':code}));raise SystemExit(code)
def bind_runtime(args):
    global ROOT_BINDING, ROOT_REVIEW, ROOT_REVIEW_SHA, ROOT_REVIEW_RUN, ROOT_DECISION, REFRESH, EXPECTED_MAIN
    assert args.root_binding and args.root_binding_sha, 'Actual root review binding and exact hash must be supplied'
    path = Path(args.root_binding).resolve()
    path.relative_to(D.resolve())
    assert pin(path)['sha256'] == args.root_binding_sha
    ROOT_BINDING = read(path)
    ROOT_BINDING['_runtime_pin'] = pin(path)
    assert ROOT_BINDING['status'] == 'bound_actual_root_publication_review'
    ROOT_REVIEW = Path(ROOT_BINDING['review']['path'])
    ROOT_REVIEW_SHA = ROOT_BINDING['review']['sha256']
    ROOT_REVIEW_RUN = Path(ROOT_BINDING['execution']['path']).parent
    ROOT_DECISION = ROOT_BINDING['decision']
    REFRESH = Path(ROOT_BINDING['refresh']['path']).parent
    EXPECTED_MAIN=read(ROOT_BINDING['refresh']['path'])['refs']['origin/main']

def phase_guard(phase):
    phases=('prepare','install','cache','verify','graph','finish','publish')
    index=phases.index(phase)
    if index==0:return None
    path=D/'actions'/PHASE_ACTION_LABELS.get(phases[index-1],phases[index-1])/'EXECUTION.json';receipt=read(path)
    assert receipt['exit_code']==0, 'Previous phase must have an actual successful receipt'
    for key in ('launch','stdout','stderr'):same(receipt[key]['path'],receipt[key])
    launch=read(receipt['launch']['path'])
    assert launch['phase']==phases[index-1]
    same(__file__,launch['common_source_at_launch']);same(OUT/'FINAL_FREEZE.json',launch['proposal_freeze'])
    assert launch['root_binding']==ROOT_BINDING['_runtime_pin']
    return pin(path)

def bind_canonical_review(args):
    prepared=installed();assert not (D/'BOUND_CANONICAL.json').exists()
    assert args.canonical_review_receipt and args.canonical_review_sha, 'Root canonical review evidence must be supplied before cache'
    path=Path(args.canonical_review_receipt).resolve();path.relative_to(D.resolve())
    assert path==D/'ACTUAL_ROOT_CANONICAL_REVIEW_INPUT.json', 'Use the exact canonical contract path archived by finish'
    assert pin(path)['sha256']==args.canonical_review_sha
    contract=read(path)
    for key in ('review','execution','source','recorder','stdout','stderr'):same(contract[key]['path'],contract[key])
    review=read(contract['review']['path']);receipt=read(contract['execution']['path'])
    assert review['root_read_complete'] is True and review['git_base']==BASE
    assert review['bound_note_sha256']==pin(W/NOTE)['sha256']
    assert review['canonical_body_pins']==read(W/PACKET/'BODY_MAP.json')['bodies']
    assert review['parent_binding']==read(W/PACKET/'PARENT_BINDING.json')
    assert review['source_draft_freeze_sha256']==SOURCE_FREEZE and review['source_draft_review_sha256']==ROOT_REVIEW_SHA
    same(W/HELPER,review['prebinding_primary']);same(__file__,review['integration_common'])
    assert receipt['exit_code']==0 and receipt['argv'][1]==receipt['child_source_at_launch']['path']
    assert receipt['source_capture']['path']!=receipt['child_source_at_launch']['path']
    for key in ('stdout','stderr','recorder'):same(contract[key]['path'],receipt[key])
    same(contract['source']['path'],receipt['child_source_at_launch']);same(contract['source']['path'],receipt['source_capture'])
    assert Path(contract['stderr']['path']).read_bytes()==b''
    result=read(contract['stdout']['path']);same(contract['review']['path'],result['review'])
    before={name:(W/name).read_bytes() for name in prepared['canonical_files']}
    def copy_blob(row):
        source=Path(row['path']);raw=source.read_bytes();target=W/PACKET/'binding_sources'/(digest(raw)+(source.suffix or '.blob'))
        target.parent.mkdir(parents=True,exist_ok=True)
        if target.exists():assert target.read_bytes()==raw
        else:target.write_bytes(raw)
        return portable(target,str(target.relative_to(W)))
    evidence={key:copy_blob(contract[key]) for key in ('review','execution','source','recorder','stdout','stderr')}
    actual_path=W/PACKET/'ACTUAL_BINDING.json';actual=read(actual_path)
    actual['canonical_review_evidence']=evidence;actual['root_read_complete']=True
    actual['receipt_paths']=sorted(set(actual['receipt_paths'])|{row['path'] for row in evidence.values()})
    write(actual_path,actual)
    canonical_path=W/PACKET/'CANONICAL_BINDING.json';canonical=read(canonical_path)
    canonical['root_read_complete']=True;canonical['receipt_paths']=actual['receipt_paths'];canonical['canonical_review']=evidence['review'];write(canonical_path,canonical)
    manifest_path=W/PACKET/'INPUT_MANIFEST.json';manifest=read(manifest_path)
    paths={row['path'] for row in manifest['inputs']}|{row['path'] for row in evidence.values()}
    manifest['inputs']=[portable(W/name,name) for name in sorted(paths)];write(manifest_path,manifest)
    helper=(W/HELPER).read_text()
    for key,value in {'EXPECTED_CANONICAL_REVIEW_SHA':contract['review']['sha256'],'EXPECTED_CANONICAL_REVIEW_COMMAND':tuple(receipt['argv']),
        'EXPECTED_CANONICAL_EXECUTION_SHA':contract['execution']['sha256'],
        'EXPECTED_PREBINDING_PRIMARY':review['prebinding_primary'],'EXPECTED_INTEGRATION_COMMON':review['integration_common'],
        'AUDIT_INPUT_PATHS':tuple(sorted(paths|{PACKET+'/INPUT_MANIFEST.json'}))}.items():
        helper,count=re.subn(r'^'+key+r'\s*=.*$',lambda match:key+' = '+repr(value),helper,flags=re.M);assert count==1,key
    (W/HELPER).write_text(helper);repin(W);ast.parse((W/HELPER).read_bytes())
    assert (W/NOTE).read_bytes()==before[NOTE] and (W/PACKET/'BODY_MAP.json').read_bytes()==before[PACKET+'/BODY_MAP.json']
    assert (W/PACKET/'PARENT_BINDING.json').read_bytes()==before[PACKET+'/PARENT_BINDING.json']
    names=set(prepared['canonical_files'])|{row['path'] for row in evidence.values()};diff=''
    for name in sorted(names):
        old=before.get(name,b'');new=(W/name).read_bytes()
        if old!=new:diff+=''.join(difflib.unified_diff(old.decode().splitlines(True),new.decode().splitlines(True),fromfile='prebinding/'+name,tofile='bound/'+name))
    (D/'CANONICAL_REVIEW_BINDING.diff').write_text(diff)
    write(D/'BOUND_CANONICAL.json',{'utc':now(),'original_prepared':pin(D/'PREPARED.json'),'canonical_files':{name:pin(W/name) for name in sorted(names)},
        'canonical_review_contract':pin(path),'canonical_review':contract['review'],'binding_diff':pin(D/'CANONICAL_REVIEW_BINDING.diff'),
        'note_and_bodies_unchanged':True,'primary_executed':False,'scientific_programs_run':0})
    installed()

def require_staged_review(args,staged):
    assert args.reviewed_staging_sha==pin(D/'STAGED_VERIFICATION.json')['sha256']
    assert args.staged_review_receipt and args.staged_review_sha
    path=Path(args.staged_review_receipt).resolve();path.relative_to(D.resolve())
    assert pin(path)['sha256']==args.staged_review_sha
    contract=read(path)
    verify_actual_review_execution(contract['review'],contract['execution'])
    review=read(contract['review']['path'])
    assert review['kind']=='root_staged_source_review' and review['root_read_complete'] is True and review['retained_audit'] is False
    same(D/'STAGED_VERIFICATION.json',review['staging']);same(OUT/'FINAL_FREEZE.json',review['proposal_freeze'])
    same(D/'BOUND_CANONICAL.json',review['bound_canonical'])
    assert review['canonical_membership_source']=='BOUND_CANONICAL.json'
    bound=read(D/'BOUND_CANONICAL.json');pre=read(D/'PREPARED.json')
    added=set(bound['canonical_files'])-set(pre['canonical_files'])
    assert set(review['added_canonical_evidence_paths'])==added
    assert set(bound['canonical_files'])<=set(staged['paths'])
    assert review['root_binding']==ROOT_BINDING['_runtime_pin']
    assert review['head']==staged['base_head']==BASE==git('rev-parse','HEAD').decode().strip()
    assert review['index_sha256']==staged['index_sha256']==digest(git('ls-files','--stage','-z'))
    return pin(path)

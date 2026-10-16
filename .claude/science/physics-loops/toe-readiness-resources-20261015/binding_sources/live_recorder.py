"""Unexecuted resource-integration proposal. All actions require --root-execute."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, ast, contextlib, difflib, gzip, hashlib, io, json, os, re
import shutil, subprocess, sys, time, traceback

OUT = Path(__file__).resolve().parent
N = OUT.parent
W = N.parent / 'correlation_worktree'
SOURCE = N / 'readiness_resources_publication_draft'
D = N / 'publication_integration/readiness_resources'
STAGE = D / 'canonical_source'
PACKET = '.claude/science/physics-loops/toe-readiness-resources-20261015'
NOTE = 'docs/READINESS_RESOURCE_ALTERNATIVES_BOUNDED_THEOREM_NOTE_2026-10-15.md'
HELPER = 'scripts/readiness_resource_alternatives_2026_10_15.py'
PARENTS = ('docs/MASS_SCALED_MEDIATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ROUTED_AUXILIARY_AND_JOINT_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md')
CLAIM = 'readiness_resource_alternatives_bounded_theorem_note_2026-10-15'
PARENT_CLAIMS = ('mass_scaled_mediator_transport_bounded_theorem_note_2026-10-15', 'routed_auxiliary_and_joint_readiness_bounded_theorem_note_2026-10-15')
BASE = 'b3a884425aa86e642172aef67c90fc1fe93ff942'
BASE_BRANCH = 'physics-loop/toe-joint-readiness-20261015'
FEATURE = 'physics-loop/toe-readiness-resources-20261015'
REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
TITLE = '[physics-loop] readiness-resources: bounded_theorem / conditional-support'
MASS_HEAD = '1fcff4c8e3cfe5b8ae5fae1a31ae882609ff5939'
SOURCE_FREEZE = '2ef4152f629f9985ee5872fcad1fa45811561b8e82b6bb0076a7366600995ce9'
ROOT_REVIEW = N / 'readiness_resources_root_publication_review/ROOT_REVIEW.json'
ROOT_REVIEW_SHA = 'b9dcc711130524ae3c254805cefc9b823411a1ac030e48a3440bbed5e8a125ea'
ROOT_DECISION = 'Publication interpretation accepted at existing conditional source scope; actual checkout binding/integration still pending.'
REFRESH = N / 'main_refresh_1545'
DEADLINE = datetime(2026, 10, 15, 21, 43, 9, tzinfo=timezone.utc)
GRAPH = 'docs/audit/data/citation_graph.json'
GRAPH_MANIFEST = 'docs/audit/data/citation_graph_manifest.json'

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
    write(folder / 'EXECUTION.json', {'finished_utc': now(), 'exit_code': code,
          'elapsed_seconds': time.monotonic() - started, 'launch': pin(folder / 'LAUNCH.json'),
          'stdout': pin(folder / 'stdout'), 'stderr': pin(folder / 'stderr')})
    assert code in expected, str(folder)
    return stdout

def parent_query(label):
    observed = {}
    for role, number, head, branch, base_branch in [
        ('stack',9607,BASE,BASE_BRANCH,'physics-loop/toe-mass-scaled-mediator-transport-20261015'),
        ('mass',9606,MASS_HEAD,'physics-loop/toe-mass-scaled-mediator-transport-20261015','physics-loop/toe-shared-mediator-programming-20261015')]:
        row=json.loads(run(label+'_'+role,['gh','pr','view',str(number),'--repo',REPOSITORY,'--json','number,state,isDraft,headRefOid,headRefName,baseRefName,url']))
        assert row['state']=='OPEN' and row['isDraft'] is False and row['number']==number
        assert row['headRefOid']==head and row['headRefName']==branch and row['baseRefName']==base_branch
        observed[role]=row
    return observed

def no_duplicate(label):
    result = json.loads(run(label, ['gh', 'pr', 'list', '--repo', REPOSITORY, '--state', 'all',
            '--head', FEATURE, '--json', 'number,state,headRefName,url']))
    assert result == [], 'Existing PR requires deliberate continuation, not another creation'

def installed():
    assert git('branch', '--show-current').decode().strip() == FEATURE
    assert git('rev-parse', 'HEAD').decode().strip() == BASE
    prepared = read(D / 'PREPARED.json')
    for path, row in prepared['canonical_files'].items(): same(W / path, row)
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
            assert row['path'] in PARENTS;target=W/row['path']
        row.update(portable(target,row['path']))
    write(manifest_path,manifest)
    helper=root/HELPER;text=helper.read_text()
    text,count=re.subn(r'^MANIFEST_SHA256\s*=.*$','MANIFEST_SHA256 = '+repr(pin(manifest_path)['sha256']),text,flags=re.M)
    assert count==1;helper.write_text(text.rstrip()+'\n')

def prepare(args):
    frozen_proposal();clean_base()
    assert args.reviewed_source_sha==SOURCE_FREEZE,'Root must inspect and acknowledge this exact frozen source proposal'
    for row in read(OUT/'SOURCE_PINS.json')['sources']:same(row['path'],row)
    assert pin(SOURCE/'FINAL_FREEZE.json')['sha256']==SOURCE_FREEZE
    draft_freeze=read(SOURCE/'FINAL_FREEZE.json')
    for row in draft_freeze['files']:same(SOURCE/row['path'],row)
    assert {str(p.relative_to(SOURCE)) for p in SOURCE.rglob('*') if p.is_file()}=={r['path'] for r in draft_freeze['files']}|{'FINAL_FREEZE.json'}
    review=read(ROOT_REVIEW)
    assert pin(ROOT_REVIEW)['sha256']==ROOT_REVIEW_SHA and review['kind']=='root_source_publication_review'
    assert review['root_read_complete'] is True and review['source_draft_freeze']['sha256']==SOURCE_FREEZE
    assert review['sealed_members_verified']==122 and review['decision']==ROOT_DECISION
    refresh=read(REFRESH/'REFS.json')
    for ref in ('origin/main','origin/ai/execution'):
        assert git('rev-parse',ref).decode().strip()==refresh['refs'][ref],'Reference changed; deliberate root rebind required'
    assert refresh['refs']['HEAD']==BASE,'Exact latest recorded refresh/base binding required'
    same(refresh['inventory']['path'],refresh['inventory'])
    parent=parent_query('prepare_parent');no_duplicate('prepare_duplicates')
    assert not git('branch','--list',FEATURE).strip() and not STAGE.exists()
    shutil.copytree(SOURCE/'proposal',STAGE)
    original=(STAGE/NOTE).read_bytes();mapping=read(STAGE/PACKET/'BODY_MAP.json')
    bodies={row['name']:original[row['start_byte_inclusive']:row['end_byte_exclusive']] for row in mapping['bodies']}
    prefix_end=min(row['start_byte_inclusive'] for row in mapping['bodies']);prefix=original[:prefix_end].decode()
    for old,new in read(OUT/'WRAPPER_REPLACEMENTS.json').items():
        assert prefix.count(old)==1,old;prefix=prefix.replace(old,new)
    canonical=prefix.encode()+original[prefix_end:];(STAGE/NOTE).write_bytes(canonical)
    for row in mapping['bodies']:
        body=bodies[row['name']];assert canonical.count(body)==1 and digest(body)==row['sha256']
        row['start_byte_inclusive']=canonical.index(body);row['end_byte_exclusive']=row['start_byte_inclusive']+len(body)
    write(STAGE/PACKET/'BODY_MAP.json',mapping)
    # The resource archive stores blobs; its body references are symbolic names, not stale offsets.
    sources=read(STAGE/PACKET/'SOURCE_MANIFEST.json')
    for row in sources['sources']:
        loc=row['recovery']
        if loc['kind']=='body_interval':assert row['sha256']==digest(bodies[loc['body_name']])
    deps=read(STAGE/PACKET/'DEPENDENCIES.json')['dependencies']
    assert [r['path'] for r in deps]==list(PARENTS)
    for row in deps:
        same(W/row['path'],row);b=row['accepted_body_interval'];raw=(W/row['path']).read_bytes()
        body=raw[b['start_byte_inclusive']:b['end_byte_exclusive']]
        assert len(body)==b['bytes'] and digest(body)==b['sha256'] and raw.count(body)==1
    status=STAGE/PACKET/'CLAIM_STATUS_CERTIFICATE.md';text=status.read_text()
    old="Canonical joint binding, proposed primary/cache, graph and publication are pending."
    assert text.count(old)==1
    status.write_text(text.replace(old,"Both canonical parent notes are pinned. This resource note's actual checkout binding is recorded separately in ACTUAL_BINDING; primary/cache, graph and publication require their own actual receipts."))
    receipt_paths=[]
    def copy_receipt(source,name):
        target=STAGE/PACKET/'binding_sources'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,target)
        receipt_paths.append(str(target.relative_to(STAGE)))
    copy_receipt(REFRESH/'REFS.json','REFS.json')
    copy_receipt(ROOT_REVIEW,'ROOT_SOURCE_REVIEW.json')
    copy_receipt(N/'run.py','historical_recorder.py')
    copy_receipt(Path(__file__),'live_recorder.py')
    historical=[('fetch',Path(refresh['actual_fetch_receipt']).parent),
                ('inventory',Path(refresh['actual_inventory_receipt']).parent),
                ('root_review',N/'runs/resource_source_root_review_1550')]
    for label,folder in historical:
        for name in ('EXECUTION.json','stdout','stderr'):copy_receipt(folder/name,label+'_'+name)
        if label=='root_review':copy_receipt(folder/'executed_source.py','root_review_executed_source.py')
    for label in ('stack','mass'):
        folder=D/'runs'/('prepare_parent_'+label)
        for name in ('LAUNCH.json','EXECUTION.json','stdout','stderr'):copy_receipt(folder/name,label+'_'+name)
    actual={'kind':'actual_root_canonical_binding','utc':now(),'canonical_parent_binding_complete':True,'root_read_complete':True,
        'note_sha256':digest(canonical),'parent_sha256':{r['path']:r['sha256'] for r in deps},
        'source_acceptances':{key:row['sha256'] for key,row in review['existing_source_acceptances'].items()},
        'git_base':BASE,'base_branch':BASE_BRANCH,'planned_feature_branch':FEATURE,'observed_parent_prs':parent,
        'origin_main':refresh['refs']['origin/main'],'instruction_revision':refresh['refs']['origin/ai/execution'],
        'historical_refresh_head':refresh['refs']['HEAD'],'raw_bodies':mapping['bodies'],'canonical_parents':deps,
        'receipt_paths':receipt_paths,'source_proposal_freeze':pin(SOURCE/'FINAL_FREEZE.json'),
        'root_source_review':pin(ROOT_REVIEW),'root_review_ack':{'utc':now(),'reviewed_source_sha256':args.reviewed_source_sha},
        'canonical_execution_not_yet_performed':True,'retained_audit':False}
    write(STAGE/PACKET/'ACTUAL_BINDING.json',actual)
    write(STAGE/PACKET/'CANONICAL_BINDING.json',{'kind':'actual_resource_source_binding','canonical_parent_binding_complete':True,
        'root_read_complete':True,'actual_checkout_head':BASE,'actual_git_base':BASE,'actual_branch_at_binding':BASE_BRANCH,
        'bound_note_sha256':digest(canonical),'receipt_paths':receipt_paths,'canonical_parent_sha256':actual['parent_sha256']})
    (STAGE/PACKET/'PR_TITLE.txt').write_text(TITLE+'\n')
    (STAGE/PACKET/'ACTUAL_HANDOFF.md').write_text('Actual resource note, both mathematical parents and stack/refresh/root-review observations are recorded in ACTUAL_BINDING. Fixed-duration preparation ages D under H0 for tau0; fast preparation compares unaged D while paying full-K drift over actual T_p. All five bodies, the original equality failure/full correction, scalar/channel/moment/support and full-output same-K qualifications remain unchanged. Historical draft null outcomes remain dated. Native suppliers, common caps, microscopic controller energy, full-program closure and retained audit remain open. Later primary/cache/mutation/graph/publication outcomes require separate actual receipts.\n')
    manifest_path=PACKET+'/INPUT_MANIFEST.json'
    rows=[portable(p,str(p.relative_to(STAGE))) for p in sorted(STAGE.rglob('*')) if p.is_file() and str(p.relative_to(STAGE)) not in (HELPER,manifest_path)]
    rows.extend(portable(W/path,path) for path in PARENTS)
    write(STAGE/manifest_path,{'schema':'source_integrity_inputs_v1','inputs':rows,'scope':'Source/body/recovery/binding structure only; no scientific execution.'})
    helper=(STAGE/HELPER).read_text();needle='    print(json.dumps({"result": "source_integrity_verified",'
    checks=(OUT/'binding_checks.txt').read_text().replace('__INTEGRATION_COMMON_SHA256__',pin(__file__)['sha256'])
    assert helper.count(needle)==1;helper=helper.replace(needle,checks+'\n'+needle)
    helper,count=re.subn(r'^AUDIT_INPUT_PATHS\s*=.*$','AUDIT_INPUT_PATHS = '+repr(tuple(sorted({r['path'] for r in rows}|{manifest_path}))),helper,flags=re.M)
    assert count==1;(STAGE/HELPER).write_text(helper.rstrip()+'\n');repin(STAGE);ast.parse((STAGE/HELPER).read_bytes())
    assert (STAGE/PACKET/'PUBLICATION_STATE.json').read_bytes()==(SOURCE/'proposal'/PACKET/'PUBLICATION_STATE.json').read_bytes()
    changed=[str(p.relative_to(STAGE)) for p in sorted(STAGE.rglob('*')) if p.is_file() and (not (SOURCE/'proposal'/p.relative_to(STAGE)).exists() or p.read_bytes()!=(SOURCE/'proposal'/p.relative_to(STAGE)).read_bytes())]
    delta=''
    for name in changed:
        old=SOURCE/'proposal'/name;before=old.read_text().splitlines(True) if old.exists() else []
        delta+=''.join(difflib.unified_diff(before,(STAGE/name).read_text().splitlines(True),fromfile='draft/'+name,tofile='canonical/'+name))
    (D/'CANONICALIZATION.diff').write_text(delta)
    graph,gm=read(W/GRAPH),read(W/GRAPH_MANIFEST)
    assert CLAIM not in graph['nodes'] and all(cid in graph['nodes'] for cid in PARENT_CLAIMS)
    write(D/'GRAPH_BASELINE.json',{'graph':pin(W/GRAPH),'manifest':pin(W/GRAPH_MANIFEST),'node_count':len(graph['nodes']),
        'edge_count':len(graph['edges']),'nodes_hash':object_hash(graph['nodes']),'edges_hash':edge_hash(graph['edges']),
        'roots_hash':object_hash(graph['roots']),'manifest_nodes_hash':object_hash(gm['nodes'])})
    files={str(p.relative_to(STAGE)):pin(p) for p in sorted(STAGE.rglob('*')) if p.is_file()}
    write(D/'PREPARED.json',{'utc':now(),'canonical_files':files,'base_head':BASE,'planned_feature_branch':FEATURE,
        'diff':pin(D/'CANONICALIZATION.diff'),'binding':pin(STAGE/PACKET/'ACTUAL_BINDING.json'),
        'source_proposal_freeze':pin(SOURCE/'FINAL_FREEZE.json'),'primary_executed':False,'scientific_programs_run':0})
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
    installed(); run('primary_separate_streams', [sys.executable, '-B', HELPER], timeout=60)
    runner = cache_module()
    assert runner.declared_timeout_for(HELPER) == 60
    result, cache_path = runner.execute_and_write_cache(HELPER, timeout_sec=60)
    write(D / 'CANONICAL_RESULT.json', result)
    assert result['exit_code'] == 0 and result['status'] == 'ok' and cache_path
    assert runner.cache_status(HELPER) == 'fresh'
    summaries = [json.loads(line) for line in result['stdout'].splitlines() if line.startswith('{')]
    assert len(summaries) == 1; summary = summaries[0]
    assert summary['result'] == 'source_integrity_verified' and summary['scientific_programs_run'] == summary['historical_programs_replayed'] == 0
    assert summary['publication_or_retained_status_certified'] is False
    scopes = [line for line in result['stdout'].splitlines() if line.split(':', 1)[0] in ('per_element', 'per_site', 'per_mode', 'per_block', 'lattice_wide')]
    assert len(scopes) == 5
    cached = Path(cache_path); cached = cached if cached.is_absolute() else W / cached
    write(D / 'CANONICAL_EXECUTION.json', {'utc': now(), 'primary': pin(W / HELPER), 'result': pin(D / 'CANONICAL_RESULT.json'),
        'cache': pin(cached), 'timeout_seconds': 60, 'cache_fresh': True, 'summary': summary, 'scope_lines': scopes,
        'scientific_programs_run': 0, 'child_stream_limit': 'runner_cache merges child stderr into stdout; result.stderr is not a separate child-stderr capture.'})
    installed()

def verify(args):
    prepared=installed();paths=sorted(prepared['canonical_files'])
    cases=[('baseline',None),('manifest_identity','Input-manifest identity'),('source_identity','Input identity mismatch'),
        ('body_interval','Input identity mismatch'),('parent_interval','Input identity mismatch'),
        ('dependency_role','Exactly two mathematical parents'),('historical_outcome','Historical null outcome must remain null:'),
        ('actual_note','Actual bound-note identity'),('live_exit','live observation exit/schema'),
        ('live_recorder','live recorder source identity'),('history_schema','historical observation schema'),
        ('root_ack','root reviewed source acknowledgment'),('receipt_membership','exact binding receipt membership'),
        ('failure_archive','original equality failure and full correction archive')]
    write(D/'MUTATION_PLAN.json',{'utc':now(),'primary':pin(W/HELPER),'cases':cases,
        'scope':'Bounded structural/provenance failure cases. Semantic cases repin outer identities; no scientific program or formula test.'})
    results=[]
    for name,expected in cases:
        root=D/'mutation_scratch'/name;root.mkdir(parents=True,exist_ok=False)
        for path in paths+list(PARENTS):
            (root/path).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(W/path,root/path)
        def mutate(filename,fn):
            path=root/PACKET/filename;value=read(path);fn(value);write(path,value)
        if name=='manifest_identity':
            p=root/PACKET/'INPUT_MANIFEST.json';p.write_bytes(p.read_bytes()+b' ')
        elif name=='source_identity':
            p=root/NOTE;p.write_bytes(p.read_bytes()+b' ')
        elif name=='body_interval':mutate('BODY_MAP.json',lambda v:v['bodies'][4].__setitem__('start_byte_inclusive',v['bodies'][4]['start_byte_inclusive']+1))
        elif name=='parent_interval':mutate('DEPENDENCIES.json',lambda v:v['dependencies'][1]['accepted_body_interval'].__setitem__('start_byte_inclusive',70025))
        elif name=='dependency_role':mutate('DEPENDENCIES.json',lambda v:v['dependencies'][1].__setitem__('path',NOTE))
        elif name=='historical_outcome':mutate('PUBLICATION_STATE.json',lambda v:v.__setitem__('primary_execution',True))
        elif name=='actual_note':mutate('ACTUAL_BINDING.json',lambda v:v.__setitem__('note_sha256','0'*64))
        elif name=='live_exit':mutate('binding_sources/stack_EXECUTION.json',lambda v:v.__setitem__('exit_code',1))
        elif name=='live_recorder':
            p=root/PACKET/'binding_sources/live_recorder.py';p.write_bytes(p.read_bytes()+b'# altered source\n')
        elif name=='history_schema':mutate('binding_sources/fetch_EXECUTION.json',lambda v:v.pop('start_utc'))
        elif name=='root_ack':mutate('ACTUAL_BINDING.json',lambda v:v['root_review_ack'].__setitem__('reviewed_source_sha256','0'*64))
        elif name=='receipt_membership':
            mutate('ACTUAL_BINDING.json',lambda v:v['receipt_paths'].pop())
            mutate('CANONICAL_BINDING.json',lambda v:v.__setitem__('receipt_paths',read(root/PACKET/'ACTUAL_BINDING.json')['receipt_paths']))
        elif name=='failure_archive':mutate('ARCHIVE_INDEX.json',lambda v:v.__setitem__('objects',[r for r in v['objects'] if r['sha256']!='b34df6b7479df5b3960b02bf383ff7954621a10b1efb6831a25c65466d8da783']))
        if name not in ('baseline','manifest_identity','source_identity'):repin(root)
        run('mutation_'+name,[sys.executable,'-B',root/HELPER],cwd=root,expected=(0,) if expected is None else (1,),timeout=60)
        receipt=D/'runs'/('mutation_'+name)/'EXECUTION.json'
        if expected:assert expected in (receipt.parent/'stderr').read_text(),name
        results.append({'case':name,'expected_failure':expected,'receipt':pin(receipt)})
    write(D/'MUTATION_RESULTS.json',{'utc':now(),'cases':results,'baseline_exit':0,'mutants_rejected':len(cases)-1,'scientific_programs_run':0})
    run('compile',[sys.executable,'-B','-c','import ast,pathlib,sys; ast.parse(pathlib.Path(sys.argv[1]).read_bytes())',HELPER])
    active_paths=[p for p in paths if '/source_recovery/' not in p and '/binding_sources/' not in p and Path(p).suffix in ('.md','.json','.py')]
    before={p:pin(W/p) for p in paths}
    run('vocab_report',[sys.executable,'-B','scripts/vocab_lint.py','--report-only',*active_paths])
    for p,row in before.items():same(W/p,row)
    index=git('ls-files','--stage','-z')
    focused=json.loads(run('changed_evidence',[sys.executable,'-B','docs/audit/scripts/check_changed_audit_evidence.py','--base','HEAD','--include-worktree','--json']))
    assert git('ls-files','--stage','-z')==index and not focused.get('failures') and not focused.get('control_failures')
    assert cache_module().cache_status(HELPER)=='fresh'
    write(D/'SOURCE_VERIFICATION.json',{'utc':now(),'primary':pin(W/HELPER),'mutations':pin(D/'MUTATION_RESULTS.json'),
        'focused_checker':focused,'index_preserved':True,'vocabulary_source_changes':False,'historical_bytes_untouched':True,
        'scientific_programs_run':0,'scope':'Source compatibility/provenance only; current-main/cumulative-stack and independent audit remain separate.'})
    installed()

def graph(args):
    installed();before=read(D/'GRAPH_BASELINE.json')
    same(W/GRAPH,before['graph']);same(W/GRAPH_MANIFEST,before['manifest'])
    run('graph_build',[sys.executable,'-B','docs/audit/scripts/run_citation_graph_build.py'],timeout=180)
    value=read(W/GRAPH);nodes=dict(value['nodes']);node=nodes.pop(CLAIM)
    assert object_hash(nodes)==before['nodes_hash'] and len(nodes)==before['node_count']
    assert node['path']==NOTE and node['runner_path']==HELPER and node['deps']==list(PARENT_CLAIMS)
    edges=[{'from':CLAIM,'to':cid} for cid in PARENT_CLAIMS];remaining=list(value['edges'])
    for edge in edges:assert remaining.count(edge)==1;remaining.remove(edge)
    assert edge_hash(remaining)==before['edges_hash'] and len(remaining)==before['edge_count']
    assert object_hash(value['roots'])==before['roots_hash']
    run('graph_manifest',[sys.executable,'-B','docs/audit/scripts/write_citation_graph_manifest.py'])
    manifest=read(W/GRAPH_MANIFEST);old_nodes=dict(manifest['nodes']);old_nodes.pop(CLAIM)
    assert object_hash(old_nodes)==before['manifest_nodes_hash']
    assert manifest['node_count']==len(value['nodes']) and manifest['edge_count']==len(value['edges'])
    assert git('ls-files','--',GRAPH)==b'';run('ignored_graph',['git','check-ignore','-v',GRAPH])
    write(D/'GRAPH_VERIFICATION.json',{'utc':now(),'old_nodes_preserved':before['node_count'],'old_edges_preserved':before['edge_count'],
        'new_node':node,'new_edges':edges,'roots_unchanged':True,'graph':pin(W/GRAPH),'manifest':pin(W/GRAPH_MANIFEST),
        'baseline':pin(D/'GRAPH_BASELINE.json'),'method':'Canonical object digests preserve every old node/edge/root without copying full graphs.',
        'graph_json_ignored_not_staged':True})

def historical_attributes(paths):
    affected = []
    for name in paths:
        if '/source_recovery/' not in name: continue
        data = (W / name).read_bytes()
        try: text = data.decode()
        except UnicodeDecodeError: continue
        lines = text.splitlines()
        if data.endswith(b'\n\n') or any(line.endswith((' ', '\t')) or re.match(r'^ +\t', line) for line in lines): affected.append(name)
    if not affected: return []
    attr = W / '.gitattributes'; old = attr.read_bytes() if attr.exists() else b''
    (D / 'GITATTRIBUTES_BEFORE').write_bytes(old)
    suffix = ''.join('/' + name + ' -whitespace\n' for name in sorted(affected)).encode()
    attr.write_bytes(old + (b'\n' if old and not old.endswith(b'\n') else b'') + suffix)
    write(D / 'HISTORICAL_ATTRIBUTES.json', {'utc': now(), 'exact_paths': affected,
        'before': pin(D / 'GITATTRIBUTES_BEFORE'), 'after': pin(attr), 'scope': 'Immutable historical source files only; active files and raw proofs are not normalized.'})
    return ['.gitattributes']

def finish(args):
    prepared = installed(); runner = cache_module(); assert runner.cache_status(HELPER) == 'fresh'
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
    selected = [p for p in OUT.iterdir() if p.is_file()]
    selected += [p for p in (OUT / 'metadata_runs').rglob('*') if p.is_file()]
    selected += [D / name for name in ('PREPARED.json', 'INSTALLED.json', 'ROOT_CANONICAL_REVIEW.json', 'CANONICALIZATION.diff', 'GRAPH_BASELINE.json', 'GRAPH_VERIFICATION.json', 'CANONICAL_RESULT.json', 'CANONICAL_EXECUTION.json', 'MUTATION_PLAN.json', 'MUTATION_RESULTS.json', 'SOURCE_VERIFICATION.json')]
    selected += [p for p in SOURCE.iterdir() if p.is_file()]
    selected += [p for p in (SOURCE / 'metadata_runs').rglob('*') if p.is_file()]
    selected += [p for p in (OUT / 'reference').rglob('*') if p.is_file()]
    selected += [p for p in (D / 'runs').rglob('*') if p.is_file()]
    selected += [p for p in (D / 'actions').rglob('*') if p.is_file() and 'finish' not in p.relative_to(D / 'actions').parts]
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
        'remaining': ['Integrated-current-main/cumulative-stack landing checks and independent retained audit.', 'Supplied independent pure memory, controls, full-clock family restrictions, endpoint support, phase/moment precision, same-K composition, common caps and microscopic energy/detector/reuse identification.']}
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
        'full_staged_whitespace_check': 'actual exit zero', 'scientific_programs_run': 0})
    link = 'https://github.com/' + REPOSITORY + '/blob/__COMMIT__/'
    body = (OUT / 'PR_BODY_TEMPLATE.md').read_text().replace('__BASE__', BASE).replace('__LINK__', link)
    (D / 'PR_BODY.md').write_text(body)
    print(json.dumps({'staged': pin(D / 'STAGED_VERIFICATION.json'), 'title': TITLE, 'body': pin(D / 'PR_BODY.md')}))

def publish(args):
    prepared = installed(); staged = read(D / 'STAGED_VERIFICATION.json')
    assert git('diff', '--name-only') == git('ls-files', '--others', '--exclude-standard', '-z') == b''
    assert set(git('diff', '--cached', '--name-only', '-z').decode().rstrip('\0').split('\0')) == set(staged['paths'])
    for path, row in staged['pins'].items(): same(W / path, row)
    for row in read(W / PACKET / 'PUBLICATION_EVIDENCE.json')['originals'].values():
        data = gzip.decompress((W / row['stored_path']).read_bytes())
        assert len(data) == row['bytes'] and digest(data) == row['sha256']
    assert cache_module().cache_status(HELPER) == 'fresh'
    parent_query('precommit_parent'); no_duplicate('precommit_duplicates')
    run('commit', ['git', 'commit', '-m', 'Add conditional fixed-duration and fast joint-readiness resource recipes'])
    head = git('rev-parse', 'HEAD').decode().strip(); tree = git('rev-parse', 'HEAD^{tree}').decode().strip()
    assert git('rev-parse', 'HEAD^').decode().strip() == BASE and git('status', '--porcelain') == b''
    run('committed_whitespace', ['git', 'diff', '--check', BASE + '..HEAD'])
    assert set(git('diff', '--name-only', '-z', BASE + '..HEAD').decode().rstrip('\0').split('\0')) == set(staged['paths'])
    write(D / 'COMMIT.json', {'utc': now(), 'head': head, 'tree': tree, 'base_head': BASE, 'branch': FEATURE, 'staged': pin(D / 'STAGED_VERIFICATION.json')})
    body_path = D / 'PR_BODY.md'; body = body_path.read_text()
    assert body.count('__COMMIT__') == 7
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
    parser = argparse.ArgumentParser(description='Unexecuted proposal; root must inspect before invoking an action.')
    parser.add_argument('--root-execute', action='store_true')
    parser.add_argument('--reviewed-diff-sha')
    parser.add_argument('--reviewed-source-sha')
    args = parser.parse_args()
    if not args.root_execute: parser.error('No action without explicit --root-execute')
    active(); frozen_proposal()
    folder = D / 'actions' / phase; folder.mkdir(parents=True, exist_ok=False)
    (folder / 'common_source.py').write_bytes(Path(__file__).read_bytes())
    entry = Path(sys.argv[0]).resolve(); (folder / 'entry_source.py').write_bytes(entry.read_bytes())
    write(folder / 'LAUNCH.json', {'started_utc': now(), 'argv': sys.argv, 'cwd': str(Path.cwd()),
        'common_source_at_launch': pin(__file__), 'entry_source_at_launch': pin(entry),
        'proposal_freeze': pin(OUT / 'FINAL_FREEZE.json'), 'scientific_execution': False})
    stdout, stderr = io.StringIO(), io.StringIO(); code = 0
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try: globals()[phase](args)
        except Exception:
            traceback.print_exc(); code = 1
    (folder / 'stdout').write_text(stdout.getvalue()); (folder / 'stderr').write_text(stderr.getvalue())
    write(folder / 'EXECUTION.json', {'finished_utc': now(), 'exit_code': code, 'launch': pin(folder / 'LAUNCH.json'),
        'stdout': pin(folder / 'stdout'), 'stderr': pin(folder / 'stderr')})
    print(stdout.getvalue(), end=''); print(stderr.getvalue(), end='', file=sys.stderr)
    print(json.dumps({'phase': phase, 'actual_receipt': str(folder / 'EXECUTION.json'), 'exit_code': code}))
    raise SystemExit(code)

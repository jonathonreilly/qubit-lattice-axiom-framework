import pathlib,json,hashlib,subprocess,gzip,importlib.util,sys
sys.dont_write_bytecode=True
r=pathlib.Path('/private/tmp/review-drain-20260915');s=r/'drain-author-slot'
def sh(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=s)
p=r/'drain8164-author-unit-draft-v1.json';assert sh(p.read_bytes())=='df0ca25933527b5c628c49b776ec80aecfdb2fd608d0331521e0e365f0fbc80f';d=json.loads(p.read_text());early=json.loads((r/'drain8164-author-prepared-v1.json').read_text());tree=d['source']['tree'];base=d['source']['base']
assert git('rev-parse','HEAD').decode().strip()==base
assert d['source']['paths']==early['files']
assert set(git('diff','--cached','--name-only').decode().splitlines())=={x['path'] for x in d['source']['paths']}
assert not git('diff','--name-only').strip()
# Exact tree index entries, without write-tree/index mutation.
idx={line.split('\t')[1]:line.split('\t')[0].split()[:2] for line in git('ls-files','--stage').decode().splitlines()}
tr={line.split('\t')[1]:[line.split()[0],line.split()[2]] for line in git('ls-tree','-r',tree).decode().splitlines()};assert idx==tr
for x in d['source']['paths']:
 assert sh((s/x['path']).read_bytes())==x['sha256']==sh(git('show',':'+x['path']))
for rows in d['inputs'].values():
 for x in rows:assert sh((s/x['path']).read_bytes())==x['sha256'],x
for x in d['reviewer']['references']:assert sh(pathlib.Path(x['path']).read_bytes())==x['sha256']
manifest=json.loads((s/'docs/work_history/review_loop/pr8164/manifest.json').read_text());inv={x['path']:x for x in json.loads((r/'drain8164-original-inventory.json').read_text())}
for x in manifest['paths']:
 o=inv[x['original_path']];assert sh(gzip.decompress((s/x['archive']).read_bytes()))==o['sha256'];assert (x['original_mode'],x['original_blob'])==(o['mode'],o['blob'])
spec=importlib.util.spec_from_file_location('dep_review8164',s/'scripts/audit_packet_script_deps.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
api=json.loads((r/'drain8164-author-cache-api-v1.json').read_text());found=[]
for row in api:
 helpers=mod.transitive_helpers(pathlib.Path(row['primary']).stem);assert {f'scripts/{h}.py' for h in helpers}==set(row['packet_transitive_helpers']);found.append({'primary':row['primary'],'discovered_helpers':sorted(helpers)})
plan=json.loads((r/'drain8164-capture-plan-v1.json').read_text());assert plan['concurrency']==1 and len(plan['programs'])==8
for i,x in enumerate(plan['programs']):
 assert x['runner']==early['runners'][i] and sh((s/x['runner']).read_bytes())==x['source_sha256'];assert x['timeout_seconds']==180;assert x['process_tree_rss_cap_bytes']==(1073741824 if i==6 else 402653184);assert x['expected_total']==[2,3,3,4,3,1,4,3][i]
result={'tree':tree,'base':base,'source_paths':196,'exact_index_tree_match':True,'same_as_early_prepared':True,'all_input_hashes_verified':True,'exact_archives':178,'actual_helper_discovery':found,'capture_plan_verified':True,'primaries_or_gates_executed':0}
out=r/'drain8164-cold-static-v1.json';assert not out.exists();out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

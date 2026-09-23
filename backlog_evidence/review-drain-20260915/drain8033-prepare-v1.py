from pathlib import Path
import ast,difflib,gzip,hashlib,json,re,shutil,subprocess,sys
sys.dont_write_bytecode=True
R=Path('/private/tmp/review-drain-20260915');W=R/'author-draft-slot';O=R/'drain8033-original';H=O/'head';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bh=lambda b:hashlib.sha256(b).hexdigest();ref=lambda p:dict(path=str(p),sha256=sha(p));git=lambda *a:subprocess.check_output(['git','-C',str(W),*a],text=True).strip()
assert json.loads((R/'author-draft-slot.json').read_text())['owner']=='PR8033-author';base=git('rev-parse','HEAD');assert base=='1bb8b7befb857852acaed93bcf2bb1e47925b013' and not git('status','--porcelain')
report=R/'drain8033-review-original.json';assert sha(report)=='e0a9a39b5a670fa9de4f0f3dd16277d182bcaf0f5868f3cfb9c22b3883c63d4f';review=json.loads(report.read_text());m=json.loads((O/'manifest.json').read_text());assert len(m['entries'])==84
files=[]
def write(rel,data,mode=0o644):
 p=W/rel;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('xb') as f:f.write(data if isinstance(data,bytes) else data.encode())
 p.chmod(mode);files.append(rel);return p
def save(name,data):
 p=R/name
 with p.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
 return p
arc='docs/work_history/repo/review_feedback/pr8033-evidence';entries=[];stored={}
for e in m['entries']:
 v=e['head'];raw=Path(v['snapshot']).read_bytes();assert bh(raw)==v['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==v['blob'];ext=Path(e['path']).suffix;key=(v['sha256'],ext)
 if key not in stored:
  plain=ext in ['.md','.py'] and not raw.endswith(b'\n\n') and all(l.rstrip(b' \t')==l for l in raw.splitlines())
  stem=re.sub('[^A-Za-z0-9_.-]','_',Path(e['path']).stem)[:75];dest='kept/pr8033-'+stem+'-'+v['sha256'][:16]+ext+('' if plain else '.gz');p=write(arc+'/'+dest,raw if plain else gzip.compress(raw,mtime=0),int(v['mode'],8)&0o777);stored[key]=(dest,sha(p),'raw' if plain else 'gzip')
 dest,digest,encoding=stored[key];entries.append(dict(original_path=e['path'],original_mode=v['mode'],git_blob=v['blob'],raw_sha256=v['sha256'],stored_path=dest,stored_sha256=digest,encoding=encoding))
delta=(O/'original.delta').read_bytes();assert bh(delta)==m['delta_sha256'];p=write(arc+'/pr8033-original.delta.gz',gzip.compress(delta,mtime=0));manifest=dict(original_head=m['head'],original_base=m['base'],entries=entries,delta=dict(path=p.name,stored_sha256=sha(p),raw_sha256=bh(delta)));write(arc+'/pr8033-archive-manifest.json',json.dumps(manifest,indent=2)+'\n')
N='docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md';P='scripts/gauge_wilson_finite_pw_static_energy_lower_controls_2026_09_07.py';parent='docs/GAUGE_WILSON_FINITE_PW_STATIC_SOURCE_ENERGY_UPPER_BOUND_BOUNDED_THEOREM_NOTE_2026-09-07.md';packet='.claude/science/physics-loops/finite-pw-static-lower-20260907/'
s=(H/N).read_text();changes=[]
def change(a,b):
 global s
 assert a in s,a;s=s.replace(a,b);changes.append(dict(old=a,new=b))
change('Let distinct endpoints x,y have graph distance d.','Let distinct endpoints x,y lie in the same connected component, with finite graph distance d=d_G(x,y)<infinity. If the endpoints are in different components, the center argument below makes the combined charged fixed space zero; no nonempty finite-energy sector is asserted in that case.')
change('imported and audited in the earlier uniform-gap and static-source results','explicitly imported in the linked uniform-gap and static-source arguments')
change('The [durable packet](../.claude/science/physics-loops/finite-pw-static-lower-20260907/PROOF_REVIEW.md) retains prospective contracts, both full proofs, all reviews, original parser-only failure and identical scientific port receipt.','The [exact historical recovery](work_history/repo/review_feedback/pr8033-evidence/README.md) retains every original proof, prospective contract, review, parser failure, flow fixture and output. Both complete positive proofs are given below. Historical reviews, audit/status records and prospective planning are not current theorem or execution authority.')
change('The complete native proof follows. Candidate information and preliminary source/envelope confirmations were exposed before root completed verification; no blind-discovery claim is made.','The complete finite-cutoff proof and alternative derivation follow. Their original writing and correction provenance remains in the exact historical recovery.')
change('2026-09-07. Written after the exposed candidate and prospective contract, before reading a completed root43 proof.','Here a>0 is the supplied temporal-scaling kinetic parameter, not a derived spatial spacing; v, the Wilson dynamics and the source tensor remain supplied model data.')
change('Actual full-irrep PW charged lower bound uniform in R>=1, volume and separation;','Actual full-irrep PW charged lower bound for distinct connected endpoints, uniform in R>=1, volume and separation;')
rootpath=packet+'evidence/root/ROOT_DERIVATION.md';ro=(H/rootpath).read_text();root=ro;root=root.replace('# Two-sided charged-energy control for the actual finite-PW model','# Appendix: complete alternative two-sided finite-cutoff energy proof');intro=root.split('\n\n')[1];root=root.replace(intro,'This alternative proof composes the linked charged-coordinate, uniform-gap and finite-cutoff upper-energy arguments for the same supplied lattice Hamiltonian. The full writing history is preserved in exact recovery.')
for a,b in [('of dimension9 as38','of dimension9 used in the charged-coordinate theorem'),('as in34/38','as in the uniform-gap and charged-coordinate arguments'),('already established in34/38','given in the linked uniform-gap and charged-coordinate arguments'),('just as in38','by the charged-coordinate argument'),('window,42 applies','window, the finite-cutoff upper-energy theorem applies'),('combining42 with(1)','combining the upper-energy theorem with(1)'),('nor42 supplies','nor the upper-energy theorem supplies'),('as in39','as in the selected-GNS construction'),('The42 finite normalized','The finite-cutoff upper theorem’s normalized')]:root=root.replace(a,b)
s+='\n\n'+root.rstrip()+'\n\n## Evidence scope and import boundary\n\nN1: This is a positive conditional energy theorem. Exact Ritz, ghost and boundary adverse examples do not establish an exhaustive negative classification or a five-route certificate.\n\nN2: No wall-independence count is asserted. Connected endpoints, full boundary Gauss action, weak coupling and acceptance are explicit related hypotheses.\n\nN3: The supplied Haar Wilson carrier, temporal kinetic parameter a, coupling v and external color sources are not selected by framework axioms or registered primitives.\n\nN4: Linked mathematical arguments, including the finite-cutoff upper-energy proof, are load-bearing; review verdicts are not theorem premises. The Yarotsky coordinate and GNS statements remain explicit mathematical imports.\n\nN5: All 18 finite controls remain: eight cube flow/connectivity/energy predicates, three ghost predicates, two boundary-Gauss predicates, four Ritz predicates and one retained-orientation predicate. No site-resolved dynamics or lattice-wide execution is claimed. The dimension-uniform and selected-sector arguments are analytical, not established by enumerating finite flows.\n\nN6: Original parser failure, raw fixtures and adverse outcomes remain recoverable. Resource and input guards are not mathematical check counts.\n\nN7: Better trials and other limiting mechanisms remain open; no impossibility or new-axiom necessity is inferred.\n\nN8: Both complete proofs remain live; historical and prospective campaign material has no current authority. Source review and finite controls do not confer an audit verdict.\n'
write(N,s)
parents=re.findall(r'^  - (.+)$',s,re.M);inputs=[N]+['docs/'+x.upper()+'.md' for x in parents]
# Pending parent is pinned to actual immutable mathematical source, never copied into this unit.
parent_snapshot=R/'drain8032-prepared-v2-source'/parent;assert sha(parent_snapshot)=='af043363c9ff1bb69829cb991c2ddd7f5bcde0ae9d57fc550ac55f58fccd71c6';assert not (W/parent).exists()
pins={p:sha(parent_snapshot if p==parent else W/p) for p in inputs}
inputcode='AUDIT_INPUT_PATHS = '+repr(inputs)+'\nEXPECTED_INPUT_SHA256 = '+repr(pins)+'\n_REPO_ROOT = Path(__file__).resolve().parents[1]\n_input_sha256 = {p: hashlib.sha256((_REPO_ROOT / p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}\nassert _input_sha256 == EXPECTED_INPUT_SHA256, "Declared scientific input drift"\n'
t=(H/P).read_text().replace('AUDIT_RSS_LIMIT_MIB = 180\n','AUDIT_RSS_LIMIT_MIB = 180\n'+inputcode)
sidecar="""    out['input_sha256'] = _input_sha256
    _sidecar = os.environ.get('AUDIT_RESULT_SIDECAR')
    if _sidecar:
        _result_path = Path(_sidecar)
        if not _result_path.is_absolute() or _result_path.resolve().is_relative_to(_REPO_ROOT.resolve()):
            raise ValueError('AUDIT_RESULT_SIDECAR must be an absolute path outside the repository')
        with _result_path.open('x') as _result_file:
            json.dump(out, _result_file, sort_keys=True, indent=2, allow_nan=False)
            _result_file.write('\\n')
"""
t=t.replace('    _finite(out)\n','    _finite(out)\n'+sidecar)
scopes={'per_element':dict(checks=1,scope='one finite cutoff-R=1 representation-label enumeration retaining both fundamental orientations'),'per_site':dict(checks=0,scope='checked and not executed — no site-resolved dynamics or observable measurement'),'per_mode':dict(checks=2,scope='two finite missing/complete boundary Gauss predicates'),'per_block':dict(checks=15,scope='eight predicates on two cube endpoint flow sets, three ghost-vacuum predicates and four abstract 3-by-3 Ritz predicates; center conservation is only necessary SU3 data'),'lattice_wide':dict(checks=0,scope='checked and not executed — finite cube flows and scalar/matrix examples do not execute arbitrary-volume coordinate estimates or the selected infinite-sector theorem')}
oldline=next(l for l in t.splitlines() if l.startswith('_emit(result,'));t=t.replace(oldline,'_emit(result, 18, '+repr(scopes)+')')
a=ast.parse((H/P).read_text());b=ast.parse(t)
def science(tree):
 started=False;out=[]
 for n in tree.body:
  if isinstance(n,ast.ImportFrom) and n.module=='itertools':started=True
  if not started:continue
  if isinstance(n,ast.Expr) and isinstance(n.value,ast.Call) and isinstance(n.value.func,ast.Name) and n.value.func.id=='_emit':continue
  out.append(ast.dump(n,include_attributes=False))
 return out
assert science(a)==science(b);compile(t,P,'exec');write(P,t)
readme='# PR8033 exact original recovery\n\nAll 84 original path/mode/blob/raw-hash identities and full binary delta are preserved. Equal historical payloads may share storage without merging their distinct original identities. Both complete positive arguments are live in the canonical note. Historical parser failures, flow fixtures, audits/status/PASS records and prospective unrelated planning remain exact history, not current science or authority.\n\n[Archive manifest](pr8033-archive-manifest.json) records raw and stored hashes and encodings. Compressed files decode to exact original bytes.\n\n'
for e in entries:readme+='- `'+e['original_path']+'`: [exact payload]('+e['stored_path']+').\n'
write(arc+'/README.md',readme)
for label,old,new in [('main',(H/N).read_text(),s),('alternative',ro,root)]:
 formula=[l for l in old.splitlines() if l.startswith(' ') and not l.startswith('  - ')];assert all(l in new.splitlines() for l in formula),label
existing=git('ls-tree','-r','--name-only','HEAD','--','docs').splitlines()
for p in files:
 if p.endswith('.md') and Path(p).name not in ['README.md','SKILL.md']:assert not any(Path(q).name.casefold()==Path(p).name.casefold() for q in existing),p
snap=R/'drain8033-prepared-v1-source';snap.mkdir();frozen=[]
for rel in sorted(files):
 p=W/rel;q=snap/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);frozen.append(dict(path=rel,sha256=sha(p),mode=oct(p.stat().st_mode&0o777),immutable_copy=str(q)))
freeze=save('drain8033-prepared-v1-source-freeze.json',dict(base=base,files=frozen))
lookup={e['original_path']:e for e in entries};mapping=[]
for e in review['original_dispositions']:
 e=dict(e);v=lookup[e['original_path']];e.update(recovery=arc+'/'+v['stored_path'],recovery_sha256=v['stored_sha256'],recovery_encoding=v['encoding']);e['final_path']=e['original_path'] if e['original_path'] in [N,P] else None;e['final_sha256']=sha(W/e['final_path']) if e['final_path'] else None;mapping.append(e)
save('drain8033-author-full-mapping-v1.json',mapping)
patch=[]
for rel in [N,P]:patch+=list(difflib.unified_diff((H/rel).read_text().splitlines(True),(W/rel).read_text().splitlines(True),fromfile='original/'+rel,tofile='prepared/'+rel))
with (R/'drain8033-author-correction-v1.diff').open('x') as f:f.writelines(patch)
save('drain8033-author-preservation-v1.json',dict(scientific_AST_identical=True,displayed_formula_lines_literal=True,connected_domain_repair='Main statement now agrees with original alternative proof; disconnected charged fixed space is zero',original_paths=84,unique_payloads=len(stored),full_delta_sha256=m['delta_sha256'],all_new_markdown_basenames_unique=True,scientific_executions=0))
save('drain8033-author-prepared-v1.json',dict(status='PREPARED ONLY; pending actual parent8032 landing and original same-session source confirmation',base=base,original_head=m['head'],original_base=m['base'],source_files=len(files),original_paths=84,note=dict(path=N,sha256=sha(W/N)),runner=dict(path=P,sha256=sha(W/P)),freeze=ref(freeze),archive_manifest=dict(path=arc+'/pr8033-archive-manifest.json',sha256=sha(W/arc/'pr8033-archive-manifest.json')),ordered_inputs=[dict(path=p,sha256=pins[p],state='PENDING parent8032 landing' if p==parent else 'present',immutable_prospective_source=str(parent_snapshot) if p==parent else None) for p in inputs],pending_parent=dict(path=parent,sha256=sha(parent_snapshot),source=ref(parent_snapshot),provenance=ref(R/'drain8032-author-unit-draft-v2.json'),boundary='Actual complete mathematical proof is prospective dependency. Its review verdict is not theorem authority and this unit does not duplicate its source.'),science_executions=0))
print(json.dumps(dict(files=len(files),freeze=ref(freeze),prepared=ref(R/'drain8033-author-prepared-v1.json')),indent=2))

from pathlib import Path
import ast,json,re,hashlib,subprocess,difflib
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';P=R/'drain8159-originals';d=json.loads((R/'drain8159-author-ownership-plan-v2.json').read_text());orig=json.loads((R/'drain8159-final366-original-dispositions.json').read_text());owners={int(k):v for k,v in d['owners'].items()};sha=lambda b:hashlib.sha256(b).hexdigest();nd=lambda n:owners[n]['canonical_note']
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD'])
parents={}
for f in range(1,7):parents[f]=[x['path'] for x in d['reviewed_parent_identities'] if x['family']==f and x['path'].startswith('docs/')]
# Resolved from original final366 actual_dependencies and family identities, not entire family membership.
deps={1:[parents[5][0]],2:[],3:[parents[5][1],parents[5][2]],4:[nd(2)],5:[],6:[parents[5][0]],7:parents[4],8:[nd(7),parents[4][1]],9:[parents[4][0],parents[4][2],parents[4][3]],10:[nd(9)],11:parents[6][:2],12:[parents[6][2]],13:[nd(11),parents[6][1]],14:[nd(11),nd(13)],15:parents[2],16:[parents[1][0]],17:parents[3],18:[nd(17)],19:[parents[1][1]],20:[parents[1][0]],21:[parents[1][1],nd(20)],22:[nd(20),nd(21)],23:[nd(20),nd(21),nd(22)],24:[parents[3][1]],25:[nd(9),nd(10)]}
# No graph edges are inferred from historical/context prose; explicit graph is one-way.
for n,ps in deps.items():
 for p in ps:assert p in [nd(k) for k in owners] or (W/p).exists(),p
runmap={Path(x['original']).name:Path(x['canonical_runner']).name for x in d['active_evidence_programs']};notemap={Path(p).name:(n,Path(nd(n)).name) for n,o in owners.items() for p in o['full_owned_appendices']}
changes=[];mapping=[];newfiles=[]
def put(p,s):
 f=W/p;assert not f.exists(),p;f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s);newfiles.append(p)
def normalize_note(s):
 # Internal original links become explicit textual provenance; actual dependencies are linked once in owner header.
 s=re.sub(r'\[([^\]]+)\]\((?!https?://)([^)]+)\)',lambda m:m[1]+' (`'+m[2]+'`)',s)
 s=re.sub(r'^(#{1,6}) ',lambda m:'#'*(min(6,len(m[1])+2))+' ',s,flags=re.M)
 return s
for n,o in owners.items():
 p=nd(n);title=o['logical_owner'].split(' ',1)[1] if o['logical_owner'].startswith('F') else o['logical_owner']
 s=f'''---\nclaim_id: {Path(p).stem.lower()}\nclaim_type: bounded_theorem\nrunner: {o['primary_runner']}\nupstream_dependencies: {json.dumps(deps[n])}\nclaim_scope: "Bounded conditional {title}; supplied hypotheses and limit order retained in full proofs."\n---\n\n# {title[0].upper()+title[1:]}\n\n**Type:** bounded_theorem\n\n```yaml\nactual_current_surface_status: conditional-support\nconditional_surface_status: conditional-support\ntrace_class: upstream_support\nreachability_to_target: supports\naudit_required_before_effective_retained: true\nbare_retained_allowed: false\nhypothetical_axiom_status: null\nadmitted_observation_status: null\n```\n\n## Scope and actual premises\n\nThe complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.\n\n'''
 if deps[n]:s+='Actual mathematical dependencies:\n\n'+''.join(f'- [{Path(x).stem}]({Path(x).name}).\n' for x in deps[n])+'\n'
 else:s+='The supplied definitions and complete argument are included in this owner; no additional repository theorem is imported by its context mentions.\n\n'
 if n==12:s+='This ground-cutoff construction is independent of the supplied continuum quartet/action.\n\n'
 if n==21:s+='The complete periodic harmonic-metric proof and its standalone evidence are owned below, with no autonomous reciprocal proof row.\n\n'
 if n in [16,17]:s+='Evidence correction: '+('the separate three-level search' if n==16 else 'the separate full-dense corroboration')+' mentioned in the original narrative has no recovered separate source/output. That ancillary narrative is unverified and supplies no numerical evidence here; the analytical proof and identifiable final program remain separately scoped.\n\n'
 for j,old in enumerate(o['full_owned_appendices'],1):
  raw=(P/old).read_text();body=normalize_note(raw);anchor=f'owned-argument-{j}'
  s+=f'<a id="{anchor}"></a>\n## Owned argument {j}: {Path(old).stem}\n\nOriginal source identity: `{Path(old).name}`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.\n\n'+body+'\n'
  mapping.append({'original':old,'original_sha256':sha(raw.encode()),'canonical_owner':p,'anchor':anchor,'proof_preservation':'Complete text; heading-depth/internal link presentation only. All original bytes separately archived.'})
 if n==2:
  raw=(R/'drain8159-block27-original-proof.md').read_text();s+='\n## Complete imported anchored-component proof\n\nHistorical mathematical import at `e3fc0b7707dce894ef98e7981a9feaf6041708f8`, SHA256 `7a0a953deb6b02a4b4c2f78a941013d30a61ad61ef6e5c0c278489c149c1c647`. The complete proof follows; its final pressure-identification and all-order obligations remain open.\n\n'+normalize_note(raw)+'\n'
 s+='\n## Canonical evidence and N1–N8 boundary\n\nThe route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.\n\n'
 for runner in o['programs']:s+=f'- [Program: {Path(runner).stem}](../{runner}); [current cache](../logs/runner-cache/{Path(runner).stem}.txt).\n'
 s+='\n[Exact source recovery](work_history/review_loop/pr8159/README.md).\n'
 put(p,s)
# Resource plans use source operations, actual fixtures and conservative operational caps; no measured RSS claims.
cost=[];programdiff=[];astchecks=[]
for x in d['active_evidence_programs']:
 old=(P/x['original']).read_text();t=ast.parse(old);n=x['owner'];p=x['canonical_runner'];src=old
 operations=[{'line':node.lineno,'expression':ast.get_source_segment(old,node)} for node in ast.walk(t) if isinstance(node,ast.Call) and any(k in ast.unparse(node.func) for k in ['eigh','eigsh','kron','zeros','meshgrid','product','leggauss','hermgauss','fftn','expm','roots_hermite'])]
 explicit={17:'Charged sector dense maximum1188 (complex matrix22MiB); full retained sector<=2310; Fourier625 matrix3MiB,513² density2MiB; eigh workspace multiple matrices, sequential fixtures.',19:'Six occupation masks times105 flux labels gives upper630 real dense matrix3.1MiB; symbolic12x12 ladder; sequential eigh and adverse comparisons.',21:'At g=.05, nq100,nt27:2*201*55=22110 complex sparse rows; local stencil; sparse LU fill-in may dominate. Full dense literal check only30x30.1GiB operational ceiling is not a proved fill-in bound.',22:'Imports21 builder; same22110 sparse rows; shift-invert plus expm_multiply vectors,192x192 curl matrices;1GiB cap includes sparse-factor workspace, not a proved peak.',4:'4D grids up to28^4 with four complex component registers (about39MiB per four-component complex field); multiple FFT/intermediate arrays and imported contact/cofactor work priced at1GiB.',6:'Finite cube N^5 configurations, Gaussian/image arrays and 160-node auxiliary quadrature; symbolic cochains small; no infinite-lattice execution.',2:'Finite partition/permutation/contact-register and cochain fixtures; SymPy/mpmath and dense Kronecker work. Combinatorial runtime is bounded by literal source loops, not asymptotic lattice claims.'}.get(n,'Finite deterministic fixtures with source operation inventory below; numerical/symbolic library overhead included. No empirical peak-RSS claim.')
 seconds=300 if n in [2,4,6,17,19,21,22] else 180;mem=1073741824 if n in [2,4,6,17,19,21,22] else 536870912
 cost.append({'runner':p,'original_sha256':x['sha256'],'time_cap_seconds':seconds,'process_tree_rss_cap_bytes':mem,'basis':explicit,'actual_operations':operations,'historical_seconds_not_new_measurement':x['historical_timing_fields'],'failure_policy':'One bounded sequential capture only after source/cheap gate; preserve cap failure and diagnostics; do not reduce fixtures or tolerances.'})
 # Portable original imports and path reads, retaining exact selected-AST behavior.
 for a,b in runmap.items():src=src.replace(a,b).replace(a[:-3],b[:-3])
 for a,(owner,newnote) in notemap.items():src=src.replace('notes/'+a,'docs/'+newnote)
 src=src.replace("root/'evidence/","root/'scripts/")
 src=src.replace("Path(__file__).with_suffix('.json')","_OUTPUT_JSON")
 src=re.sub(r"\(HERE\s*/\s*'[^']+\.json'\)","_OUTPUT_JSON",src)
 ins=list(dict.fromkeys([nd(n)]+deps[n]+x['local_helpers']))
 # Definitions precede every computational import; preserve module docstring/future placement.
 tree=ast.parse(src);after=0
 for z in tree.body:
  if (isinstance(z,ast.Expr) and isinstance(z.value,ast.Constant) and isinstance(z.value.value,str)) or (isinstance(z,ast.ImportFrom) and z.module=='__future__'):after=z.end_lineno
  else:break
 lines=src.splitlines(True)
 prefix=f'''\n# Canonical packaging; supplied scientific fixtures below are unchanged.\nAUDIT_TIMEOUT_SEC = {seconds}\nAUDIT_INPUT_PATHS = {ins!r}\nfrom pathlib import Path as _InputPath\n_REPO_ROOT = _InputPath(__file__).resolve().parents[1]\n_INPUT_TEXT = {{q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}}\nassert {Path(nd(n)).stem.lower()!r} in _INPUT_TEXT[{nd(n)!r}]\n_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/{Path(p).stem}.json'\n_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)\n'''
 src=''.join(lines[:after])+prefix+''.join(lines[after:])
 src+='''\nif __name__ == '__main__':\n    print('TOTAL: PASS=1 FAIL=0')\n    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')\n    print('per_element: only the literal finite algebraic/numerical elements in this companion were executed')\n    print('per_site: only the explicitly enumerated finite configurations; no additional spatial domain checked')\n    print('per_mode: only the finite spectral/Fourier fixtures in this companion; no uniform-mode execution claim')\n    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')\n    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')\n'''
 ast.parse(src);put(p,src);programdiff.extend(difflib.unified_diff(old.splitlines(True),src.splitlines(True),fromfile=x['original'],tofile=p))
 astchecks.append({'runner':p,'original_sha256':sha(old.encode()),'canonical_sha256':sha(src.encode()),'permitted_changes':'literal portable paths/import names; input/output/timeout declarations; completed-program TOTAL and five resolution outputs; no fixture/tolerance/formula rewrite','inputs':ins})
# Frozen whole owned set includes untouched archive and supplementary import recovery.
paths=subprocess.check_output(['git','-C',str(W),'ls-files','--others','--exclude-standard'],text=True).splitlines()
receipt={'status':'AUTHOR SOURCE DRAFT; NOT SCIENTIFIC ACCEPTANCE; COMPLETE COLD PACKAGING CHECKS PENDING','base':d['base'],'notes':[nd(n) for n in owners],'runners':[x['canonical_runner'] for x in d['active_evidence_programs']],'dependencies':deps,'helper_map_plan':d['registry_plan'],'files':[{'path':p,'sha256':sha((W/p).read_bytes())} for p in paths],'proof_mapping':mapping,'block27_reference':'drain8159-block27-import-recovery-v1.json','runtime_plan':astchecks,'resource_plan':'drain8159-author-resource-plan-v1.json','no_primary_execution':True}
(R/'drain8159-author-canonical-draft-v1.json').write_text(json.dumps(receipt,indent=2)+'\n');(R/'drain8159-author-runtime-corrections-v1.patch').write_text(''.join(programdiff));(R/'drain8159-author-resource-plan-v1.json').write_text(json.dumps(cost,indent=2)+'\n');(R/'drain8159-author-proof-mapping-v1.json').write_text(json.dumps(mapping,indent=2)+'\n');print(json.dumps({'notes':25,'programs':41,'proofs':len(mapping),'owned_paths':len(paths),'draft_sha256':sha((R/'drain8159-author-canonical-draft-v1.json').read_bytes())}))

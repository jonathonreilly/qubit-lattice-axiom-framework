from pathlib import Path
import ast,gzip,hashlib,json,re,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';J=json.loads((R/'drain8159-final366-original-dispositions.json').read_text());P=R/'drain8159-originals/.claude/science/physics-loops/toe-fixed-clock-field-20260915';sha=lambda b:hashlib.sha256(b).hexdigest()
assert json.loads((R/'review-draft-slot.json').read_text())['owner']=='PR8159-author';assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD'])
slug=['HYBRID_GENERATORS_INTEGRATED_RATES_AND_CURVATURE_WITNESS','SIGNED_FOREST_FIXED_ORDER_REMAINDERS_AND_RESTRICTED_LOOP_SUMS','SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS','CUBIC_FOURIER_ENERGY_AND_GAUSSIAN_REGISTERS','SUPPLIED_ALGEBRA_ACTION_AND_KERNEL_SUPPORT','POSITIVE_AUXILIARY_CURRENT_LAW_AND_REGULATOR_WITNESS','NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS','FINITE_NATIVE_WINDING_CURVATURE','POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD','LOCAL_SOURCE_DIAGONAL_SPECTRAL_BOUNDS','SUPPLIED_QUARTET_LINEAR_METRIC_FLOW','FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS','SUPPLIED_QUARTET_QUADRATIC_BACKREACTION','SUPPLIED_QUARTET_LEADING_DECAY_BOUNDS','NATIVE_MIXED_SIXTH_ORDER_COEFFICIENT','CYCLIC_EQUILIBRIUM_AND_INTEGER_GAUSS_LIMIT','FINITE_GRAPH_CYCLIC_WEAK_COUPLING_LIMITS','POSITIVE_ELECTRIC_GENERATOR_CONE_BOUNDS','CHARGED_RING_SLOW_SPECTRUM','FREE_WEYL_HOLONOMY_MINIMIZATION','FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC','ITERATED_LOCAL_MAXWELL_MATTER_STATE','SUPPLIED_MATCHED_FREE_CONE','EXACT_GAUGE_WARD_RESPONSE_IDENTITIES','REAL_OVERLAP_LOCAL_SOURCE_THRESHOLD']
owners={int(k):{'logical_owner':v,'canonical_note':'docs/'+slug[int(k)-1]+'_BOUNDED_THEOREM_NOTE_2026-09-15.md','full_owned_appendices':[],'programs':[]} for k,v in J['logical_owners'].items()};lookup={v['logical_owner']:k for k,v in owners.items()};active=[e for e in J['paths'] if '/evidence/' in e['path'] and e['path'].endswith('.py')];assert len(active)==41
program_names={Path(e['path']).stem:'scripts/'+re.sub(r'^block\d+_','',Path(e['path']).stem)+'_2026_09_15.py' for e in active};assert len(set(program_names.values()))==41
runtime=[]
for e in active:
 p=Path(e['recovery_path']);s=p.read_text();t=ast.parse(s);owner=lookup[e['canonical_owner']];local=[]
 for n in ast.walk(t):
  if isinstance(n,ast.ImportFrom) and n.module in program_names:local.append(n.module)
 for x in re.findall(r'[\"\']([a-z0-9_]+)\.py[\"\']',s):
  if x in program_names and x!=p.stem:local.append(x)
 local=sorted(set(local));evidence=p.with_suffix('.json');saved={}
 if evidence.exists():
  try:saved={k:v for k,v in json.loads(evidence.read_text()).items() if 'second' in k or 'rss' in k}
  except ValueError:pass
 data={'original':e['path'],'sha256':e['sha256'],'canonical_runner':program_names[p.stem],'owner':owner,'local_helpers':[program_names[x] for x in local],'source_dependency_lines':[{'line':i,'text':x} for i,x in enumerate(s.splitlines(),1) if any(z in x for z in ['read_text','read_bytes','spec_from','exec_module','source=root','from block','with_name','write_text'])],'declared_timeout':None,'historical_timing_fields':saved,'proposed_cap_seconds':300 if owner in [2,4,6,17,19,21,22] else 180,'proposed_memory_bytes':1073741824 if owner in [2,4,6,17,19,21,22] else 536870912,'resource_status':'Planning ceiling only, not execution authorization or measured current resource usage; full per-program cost confirmation before cold/capture','sidecars':'Original program writes same-stem JSON. Preserve complete structured output at canonical logs/runner-cache location; declare output separately, never treat as scientific input.','science_input_plan':[owners[owner]['canonical_note']],'fixtures':'Inline deterministic source fixtures; original source dependency lines above require final literal input closure.'}
 owners[owner]['programs'].append(data['canonical_runner']);runtime.append(data)
byrunner={x['canonical_runner']:x for x in runtime}
def closure(p,seen=None):
 seen=set() if seen is None else seen
 for h in byrunner[p]['local_helpers']:
  if h not in seen:seen.add(h);closure(h,seen)
 return sorted(seen)
for x in runtime:x['transitive_helpers']=closure(x['canonical_runner'])
# Deliberate primary selection from reviewed final programs, not failure variants.
primary_stems={1:'block1_hybrid_generator_check',2:'block2_phase_energy_check',3:'block3_record_pair_check',4:'block4_fourier_gaussian_register_check',5:'block5_algebra_naturality_check',6:'block6_positive_auxiliary_check'}
for n,o in owners.items():
 o['primary_runner']=program_names[primary_stems[n]] if n<=6 else next(p for p in o['programs'] if 'review_harmonic' not in p)
 o['additional_evidence_runners']=[p for p in o['programs'] if p!=o['primary_runner']]
 o['registry_helpers']=sorted(set(o['additional_evidence_runners'])|set().union(*(set(byrunner[p]['transitive_helpers']) for p in o['programs'])))
 o['ownership_rationale']='One bounded claim owner; every reviewed full derivation/route proof is an owned appendix. No reciprocal autonomous proof rows.'
for e in J['paths']:
 if '/notes/' in e['path'] and '/review/' not in e['path']:owners[lookup[e['canonical_owner']]]['full_owned_appendices'].append(e['path'])
parentrecords=[]
for family in range(1,7):
 f=R/f'drain8159-family{family}-parent-identities.json'
 if not f.exists():f=R/f'drain8159-family{family}-input-identities.json'
 if f.exists():
  raw=json.loads(f.read_text());rr=raw['parents'] if isinstance(raw,dict) else raw
  for e in rr:
   p=e['path'];expected=e.get('sha256',e.get('current_sha256',e.get('current_main_sha256')));current=sha((W/p).read_bytes()) if (W/p).exists() else None
   parentrecords.append({'family':family,'path':p,'reviewed_sha256':expected,'current_sha256':current,'matches':current==expected,'review_identity':str(f),'read_scope':e.get('read_scope'),'historical_revision':e.get('revision') if p.startswith('.claude/') else None})
for n,o in owners.items():
 refs=[]
 for p in o['full_owned_appendices']:
  s=(R/'drain8159-originals'/p).read_text()
  for match in re.finditer(r'(?:docs/)?[A-Z][A-Z0-9_]+\.md',s):refs.append({'source':p,'line':s[:match.start()].count('\n')+1,'literal':match.group()})
 o['actual_source_reference_occurrences']=refs
 o['dependency_status']='Exact source references retained for reviewer mapping; do not auto-promote context mentions or whole-family parents into load-bearing edges. Block12 independent; Block21 owns harmonic metric.'
archive='docs/work_history/review_loop/pr8159';manifest=[]
for i,e in enumerate(J['paths'],1):
 raw=Path(e['recovery_path']).read_bytes();assert sha(raw)==e['sha256'];assert subprocess.check_output(['git','-C',str(W),'cat-file','blob',e['blob']])==raw
 path=f'{archive}/originals/{i:03d}-{Path(e["path"]).name}.gz';p=W/path;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(gzip.compress(raw,mtime=0));assert gzip.decompress(p.read_bytes())==raw
 owner=lookup.get(e['canonical_owner']);dest=owners[owner]['canonical_note'] if owner else None
 manifest.append({k:e[k] for k in ['path','mode','blob','sha256','bytes','disposition','canonical_owner']}|{'archive':path,'archive_sha256':sha(p.read_bytes()),'encoding':'gzip; exact decoded original bytes','proposed_note_owner':dest,'recovery':J['head']+':'+e['path']})
(W/archive/'manifest.json').write_text(json.dumps({'head':J['head'],'delta_base':J['delta_base'],'paths':manifest},indent=2)+'\n')
(W/archive/'README.md').write_text('# PR8159 exact historical recovery\n\nThe [manifest](manifest.json) preserves all 366 original paths, modes, Git blobs and decoded SHA256 values. Each gzip payload decodes to its complete original bytes, including every proof, failure, intermediate source and saved output. The manifest and archived payloads preserve original source independently of branch retention.\n\nCanonical ownership is proposed, not accepted. Block12 retains independent ground-cutoff compactness ownership. The harmonic-metric proof belongs in the complete Block21 appendix. Historical outputs do not certify current canonical execution. In particular, Block16 separate three-level searches and Block17 separate full-dense corroboration remain untraced ancillary narrative; no recovered execution is claimed for them.\n\nThe full fixed-clock interacting field limit, full-foundation record nonselection, native phase identification, simultaneous continuum rates, interacting poles and thermodynamic transport remain unproved targets. Bounded positive lemmas do not discharge them.\n')
plan={'status':'AUTHOR OWNERSHIP/RUNTIME PROPOSAL ONLY; ORIGINAL REVIEWER CONFIRMATION REQUIRED BEFORE CANONICAL REWRITE','base':subprocess.check_output(['git','-C',str(W),'rev-parse','HEAD'],text=True).strip(),'original_head':J['head'],'original_delta_base':J['delta_base'],'archive_count':366,'archive_owned_paths':368,'canonical_notes_planned':25,'active_evidence_programs':runtime,'historical_python':[e['path'] for e in J['paths'] if e['path'].endswith('.py') and e not in active],'owners':owners,'reviewed_parent_identities':parentrecords,'registry_plan':{Path(o['canonical_note']).stem.lower():o['registry_helpers'] for o in owners.values() if o['registry_helpers']},'registry_targets':['scripts/audit_packet_script_deps.py','docs/audit/scripts/build_citation_graph.py'],'unproved_targets':J['genuinely_deferred_unproved_targets'],'remaining':['Original reviewer confirm primary/auxiliary assignments and full appendix destinations','Read full canonical-bound source and resolve per-owner mathematical parent edges; historical BLOCK27 premise needs explicit bounded owned proof destination or independently confirmed canonical equivalent, never opaque live personal input','Before cold source freeze make literal owner/parent/helper input reads and actual cache/API/helper closure; retain exact arithmetic and tolerances','Confirm each proposed resource ceiling against complete source cost; enforce PYTHONOPTIMIZE=0, sequential execution, no untraced numeric credit','Root guarded FF before any maps/staging; no primary executed'],'archive_manifest_sha256':sha((W/archive/'manifest.json').read_bytes()),'references':[{'path':str(R/'drain8159-final366-original-dispositions.json'),'sha256':sha((R/'drain8159-final366-original-dispositions.json').read_bytes())}]+J['family_reports']}
(R/'drain8159-author-ownership-plan-v1.json').write_text(json.dumps(plan,indent=2)+'\n')
print(json.dumps({'archive_count':366,'owned_untracked':368,'owners':25,'active_programs':len(runtime),'historical_python':len(plan['historical_python']),'registry_entries':len(plan['registry_plan']),'plan_sha256':sha((R/'drain8159-author-ownership-plan-v1.json').read_bytes()),'parent_mismatches':[p['path'] for p in parentrecords if not p['matches']]}))

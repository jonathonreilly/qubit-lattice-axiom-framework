from pathlib import Path
r=Path(__file__).resolve().parent
s=(r/'prepare_drain_candidate.py').read_text()
old="owners={};inputs={};reviews={};heads={}"
new="""owners={};inputs={};reviews={};heads={};supporting={}
# This local adapter admits only exact reviewed schema-2 supporting proofs.
for unit in collection['units']:
 name=unit.get('canonical_unit_record')
 if not name:continue
 assert name in unit['review_evidence_hashes'] and sha(out/name)==unit['review_evidence_hashes'][name]
 record=json.loads((out/name).read_text())
 if record['schema_version']!=2:continue
 runtime={x['path']:x['sha256'] for x in record['inputs']['runtime']}
 notes={n['path']:n for n in record['notes']}
 for proof in record.get('supporting_proofs',[]):
  path=proof['path'];owner=proof['canonical_note'];ref=proof['review_reference']
  assert path not in supporting and owner in notes
  assert path in unit['source_paths'] and runtime.get(path)==unit['source_paths'][path]
  ref_name=Path(ref['path']).relative_to(out).as_posix()
  assert unit['review_evidence_hashes'].get(ref_name)==ref['sha256'] and sha(out/ref_name)==ref['sha256']
  supporting[path]={'canonical_note':owner,'sha256':runtime[path],'unit_record':name,'review_reference':ref}
"""
assert s.count(old)==1;s=s.replace(old,new)
old="  if u.get('procedural_only'):"
new="""  if p in supporting:
   assert supporting[p]['canonical_note'] in u['source_paths']
   assert sha(root/p)==supporting[p]['sha256']
   continue
  if u.get('procedural_only'):"""
assert s.count(old)==1;s=s.replace(old,new)
s=s.replace("'owned_supporting_proof_bindings':", "'owned_supporting_proof_bindings':")
p=r/'prepare_drain_candidate_v2.py';assert not p.exists();p.write_text(s);compile(s,str(p),'exec')
s=(r/'finish_candidate_proofs.py').read_text().replace('owned_proofs={}','owned_proofs={};all_proof_bindings=[]')
s=s.replace("  if path not in owner['repository_dependencies']:continue\n",'')
needle="  bindings=[b for b in r['dependency_expectations'][note]['declared_authority_bindings'] if b['source_path']==path]"
assert needle in s
s=s.replace(needle,"""  all_proof_bindings.append({'canonical_note':note,'source_path':path,'sha256':bound[path],
    'unit_record':record_name,'unit_record_sha256':r['review_evidence_hashes'][record_name],
    'review_reference':ref,'role':'Current proof owned by this canonical claim; not an autonomous graph parent.',
    'load_bearing_parent_of_owner':path in owner['repository_dependencies']})
  if path not in owner['repository_dependencies']:continue
"""+needle)
s=s.replace("r['owned_supporting_proof_bindings']=list(owned_proofs.values())","r['owned_supporting_proof_bindings']=all_proof_bindings")
p=r/'finish_candidate_proofs_v2.py';assert not p.exists();p.write_text(s);compile(s,str(p),'exec')
s=(r/'drain-integration-phase.sh').read_text().replace('prepare_drain_candidate.py','prepare_drain_candidate_v2.py');p=r/'drain-integration-phase-v2.sh';assert not p.exists();p.write_text(s)
print('Prepared identity-only schema2 supporting-proof adapters; existing train72 files untouched')

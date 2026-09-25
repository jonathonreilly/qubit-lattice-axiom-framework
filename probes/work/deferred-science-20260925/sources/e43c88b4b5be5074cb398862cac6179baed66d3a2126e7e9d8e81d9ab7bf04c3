"""One-shot preserved-generation front qualification and real fresh primary run."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import hashlib, json, os, sys

E=Path(__file__).resolve().parent; P=E/'formation-response-publication'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
write=lambda p,x:p.write_text(json.dumps(x,indent=2)+'\n')
old=json.loads((E/'FORMATION_RESPONSE_PUBLICATION_FROZEN_SOURCES.json').read_text())
assert sha(E/'FORMATION_RESPONSE_GENERATION1_ROOT_REVIEW.json')
archive=E/'formation-response-publication-generation1'; assert not archive.exists(); archive.mkdir()
for rel,expected in old['files_sha256'].items():
    p=P/rel; assert sha(p)==expected; q=archive/rel; q.parent.mkdir(parents=True,exist_ok=True); q.write_bytes(p.read_bytes())
write(archive/'SOURCE_MANIFEST.json',old)
r=json.loads((E/'formation-response-sum-independent/publication_comparison/REQUIRED_FRONT_REPLACEMENT.json').read_text())
p=P/old['note']; assert sha(p)==r['publication_sha256']; text=p.read_text(); assert text.count(r['old'])==1
p.write_text(text.replace(r['old'],r['new']))
write(E/'FORMATION_RESPONSE_GENERATION2_REPAIR.json',{'at':datetime.now(timezone.utc).isoformat(),
 'old_note_sha256':r['publication_sha256'],'new_note_sha256':sha(p),'exact_replacement':r,
 'prior_publication_generation':str(archive),'prior_report_unchanged':True,
 'root_prior_review_sha256':sha(E/'FORMATION_RESPONSE_GENERATION1_ROOT_REVIEW.json')})
os.chdir(P); sys.path.insert(0,str(P/'scripts'))
import runner_cache
execution,cache=runner_cache.execute_and_write_cache(old['runner'],timeout_sec=120)
write(E/'FORMATION_RESPONSE_GENERATION2_CACHE_EXECUTION.json',execution)
assert execution['status']=='ok' and execution['exit_code']==0 and execution['stderr']==''
artifact=P/old['output_directory']/'RESPONSE_SUM_RESULTS.json'
def leaves(value,path=''):
    if isinstance(value,dict): return {k:v for a,b in value.items() for k,v in leaves(b,path+'/'+a).items()}
    if isinstance(value,list): return {k:v for a,b in enumerate(value) for k,v in leaves(b,path+'/'+str(a)).items()}
    return {path:value}
orig=json.loads((E/'formation-response-sum-personal/RESPONSE_SUM_RESULTS.json').read_text())
fresh=json.loads(artifact.read_text()); a=leaves(orig); b=leaves(fresh); assert a.keys()==b.keys()
diff=[{'path':k,'original':a[k],'fresh':b[k]} for k in a if type(a[k])!=type(b[k]) or a[k]!=b[k]]
assert len(diff)==1 and diff[0]['path']=='/elapsed_seconds'
new=json.loads(json.dumps(old)); new['generation']=2
new['previous_manifest_sha256']=sha(E/'FORMATION_RESPONSE_PUBLICATION_FROZEN_SOURCES.json')
new['front_qualification']=r
new['source_files_sha256']={rel:sha(P/rel) for rel in old['source_files_sha256']}
new['files_sha256']={rel:sha(P/rel) for rel in old['files_sha256']}
write(E/'FORMATION_RESPONSE_GENERATION2_FROZEN_SOURCES.json',new)
cache_text=(P/old['cache']).read_text()
fingerprint=next(line.split(': ',1)[1] for line in cache_text.splitlines() if line.startswith('input_fingerprint_sha256: '))
receipt={'at':datetime.now(timezone.utc).isoformat(),'all_leaf_count':len(a),'unchanged_leaf_count':len(a)-len(diff),
 'leaf_types':dict(Counter(type(v).__name__ for v in b.values())),'all_differences':diff,
 'source_files_sha256':new['source_files_sha256'],'input_fingerprint_sha256':fingerprint,
 'scientific_artifact_sha256':sha(artifact),'runner_result_sha256':sha(P/old['result']),
 'cache_sha256':sha(P/old['cache']),'outer_elapsed_seconds':execution['elapsed_sec'],
 'complete_geometry_groups':len(fresh['geometry']),'complete_charge_rows':len(fresh['rows']),
 'complete_flow_rows':sum(len(x['flows']) for x in fresh['rows']),
 'second_difference_checks':fresh['second_difference_checks'],'primitive_paths_checked':fresh['primitive_paths_checked'],
 'repair':r,'no_other_note_change':True,'runtime_and_wrapper_unchanged':True,
 'scope':'Personally witnessed fresh unchanged scientific source run after exact introductory qualification. No new independent reconstruction.'}
write(E/'FORMATION_RESPONSE_GENERATION2_PRIMARY_ROOT_VERIFICATION.json',receipt)
print(json.dumps(receipt,indent=2))

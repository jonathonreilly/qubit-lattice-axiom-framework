from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json
here=Path.cwd()
root=Path('/Users/jonBridger/.codex/worktrees/scalar-history-inverse-20261016/New Axioms Lets Go')
old=json.loads((here/'CANONICAL_SOURCE_SNAPSHOT_v2.json').read_text())
expected={
'docs/SCALAR_HISTORY_COMPATIBILITY_NOTE_2026-10-16.md':'e1cde04301073b42a9b4ec09247bc8c5da8908a836bfc24fc5f9b0e56267e45e',
'scripts/scalar_history_inverse.py':'b0fd9b26b2ebe21cb80ee212705cd39e5185ea64abfe3cd782ab137d111e33a5',
'scripts/scalar_history_inverse_math.py':'3709bd3426bc686fc444290901627dd7429f4fc9e6adafc6c0a7a83e3c0aca5b'}
sources={}
for name in old['sources']:
    raw=(root/name).read_bytes()
    sources[name]={'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'utf8':raw.decode('utf8')}
for name,pin in expected.items():
    assert sources[name]['sha256']==pin,(name,sources[name]['sha256'],pin)
changed=[name for name in sources if sources[name]['sha256']!=old['sources'][name]['sha256']]
assert changed==['scripts/scalar_history_inverse.py','outputs/scalar_history_inverse/result.json'],changed
primary='scripts/scalar_history_inverse.py'
previous=old['sources'][primary]['utf8'];current=sources[primary]['utf8']
old_line='"repository_reads": "Declared note/helper and primary runner for integrity binding only",'
new_line='"repository_reads": "Imported helper executes the algebra; explicit note/primary/helper byte reads bind integrity",'
assert old_line in previous
assert previous.replace(old_line,new_line)==current
rawdiff=''.join(difflib.unified_diff(previous.splitlines(keepends=True),current.splitlines(keepends=True),fromfile='canonical_attempt01_primary',tofile='canonical_final_primary')).encode('utf8')
change={'time_utc':datetime.now(timezone.utc).isoformat(),'scope':'Output metadata wording only; no mathematical or control change','changed_sources':changed,'from_sha256':old['sources'][primary]['sha256'],'to_sha256':sources[primary]['sha256'],'diff_bytes':len(rawdiff),'diff_sha256':hashlib.sha256(rawdiff).hexdigest(),'diff_utf8':rawdiff.decode(),'exact_one_string_replacement':True,'note_and_helper_unchanged':True}
snapshot={'time_utc':datetime.now(timezone.utc).isoformat(),'source_root':str(root),'phase':'Final metadata correction snapshot; v1 and v2 preserved as historical evidence','sources':sources}
for name,value in [('CANONICAL_SOURCE_SNAPSHOT_v3.json',snapshot),('CANONICAL_PRIMARY_METADATA_CHANGE_v1.json',change)]:
    target=here/name
    with target.open('x') as f:json.dump(value,f,indent=2);f.write('\n')
script=(here/'check_canonical_integration_v1.py').read_text()
script=script.replace('CANONICAL_SOURCE_SNAPSHOT_v2.json','CANONICAL_SOURCE_SNAPSHOT_v3.json').replace('check_canonical_integration_v1.py','check_canonical_integration_v2.py').replace('default="canonical_attempt01"','default="canonical_attempt02"')
needle='"successful_primary":code==0 and not timeout and bool(result) and result["failed"]==0,'
addition='"helper_role_disclosed":bool(result) and result["input_roles"]["repository_reads"]=="Imported helper executes the algebra; explicit note/primary/helper byte reads bind integrity",'
assert needle in script
script=script.replace(needle,needle+addition)
with (here/'check_canonical_integration_v2.py').open('x') as f:f.write(script)
print(json.dumps({'changed_sources':changed,'final_sources':{n:{k:v for k,v in s.items() if k!='utf8'} for n,s in sources.items()},'diff_sha256':change['diff_sha256']},indent=2))

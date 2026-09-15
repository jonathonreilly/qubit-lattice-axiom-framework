from pathlib import Path
import hashlib,json,gzip,subprocess
r=Path('/private/tmp/review-drain-20260915');repo=r/'author-slot-one';o=r/'check8097/original-8097';inv=json.loads((r/'check8097/inventory.json').read_text());h=inv['head'];sha=lambda b:hashlib.sha256(b).hexdigest()
dest='docs/work_history/repo/review_feedback/pr8097-evidence';m=json.loads((repo/dest/'archive-manifest.json').read_text());assert len(m['entries'])==181
for e in m['entries']:
 b=(repo/dest/e['stored_path']).read_bytes();assert sha(b)==e['stored_sha256'];b=gzip.decompress(b) if e['encoding']=='gzip' else b;assert b==(o/e['original_path']).read_bytes()
p=o/'.claude/science/physics-loops/native-local-quartic-20260913';primary=(o/inv['canonical'][1]).read_text();mut=json.loads((p/'MUTATIONS.json').read_text());assert len(mut['mutations'])==20
for x in mut['mutations']:
 d=p/'mutation_evidence'/x['name'];b=gzip.decompress((d/'source.py.gz').read_bytes());assert b.decode()==primary.replace(x['old'],x['new']);assert sha(b)==x['mutated_sha256'];err=gzip.decompress((d/'stderr.gz').read_bytes()).decode();assert err==x['stderr_tail'] or err.endswith(x['stderr_tail']);assert 'AssertionError:' in err and x['effective'] and x['returncode']==1
# Decode every original gzip (including historical earlier source and failed outputs) for recoverability.
for f in p.rglob('*.gz'):gzip.decompress(f.read_bytes())
rest=json.loads((r/'8097-historical-cache-restoration.json').read_text());assert gzip.decompress((o/rest['original_path']).read_bytes())==(repo/rest['restored_path']).read_bytes()
for path in inv['canonical']:assert (o/path).read_bytes()==(repo/path).read_bytes()
statuses=dict(line.split('\t',1)[::-1] for line in subprocess.check_output(['git','diff','--name-status',inv['original_base'],h],cwd=repo,text=True).splitlines());assert set(statuses)=={x['path'] for x in inv['paths']}
(r/'check8097/original-statuses.json').write_text(json.dumps(statuses,indent=2)+'\n')
result=dict(original_paths=184,archive_entries=181,canonical_source_exact_original=True,twenty_mutation_sources_and_assertion_receipts_verified=True,all_gzip_payloads_decode=True,cache_exact_decoded_original=True,source_loss='Generated citation manifest excluded; complete original history preserved, canonical note and primary unchanged; no original deleted paths.',primary_executions_by_reviewer=0)
(r/'check8097/history-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

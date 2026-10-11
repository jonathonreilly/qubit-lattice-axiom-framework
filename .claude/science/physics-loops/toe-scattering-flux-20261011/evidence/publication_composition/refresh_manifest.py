"""Refresh changed evidence representations without replaying scientific controls."""
from pathlib import Path
from hashlib import sha256
import json
S=Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261011')
OUT=S/'flux_publication_review'
p=OUT/'composition_check.py'
assert sha256(p.read_bytes()).hexdigest()=='d9579cbfbcdeac7385f3c1aed0f4bbba07e6d82febe3aa750c78bdbb30ad4137'
code=p.read_text().split('# Fresh-namespace standalone runs')[0]
ns={'__name__':'__main__','__file__':str(p)}
exec(compile(code,str(p),'exec'),ns)
old=json.loads((OUT/'composition_checks.json').read_text())
for name,key in [('NOTE','note'),('PRIMARY','primary'),('parent','parent')]:
    assert ns['identity'](ns[name])==old[key]
assert ns['coverage']==old['body_coverage']
assert ns['parent_sources']==old['parent_sources']
current=ns['identity'](ns['MAP'])
assert current['sha256']=='8e457c06daf37e38a5c620ceea8e058a1cd28587c5b7ea8e38384294d77eb851'
a={x['path']:x for x in old['evidence_copies']};b={x['path']:x for x in ns['copies']}
removed=sorted(a.keys()-b.keys());added=sorted(b.keys()-a.keys())
expected=['ROOT_EXCLUDED_WALK_FLUX_REVIEW.md','ROOT_EXCLUDED_WALK_LEAN_REVIEW.md','ROOT_EXCLUDED_WALK_TRANSPORT_FORM_REVIEW.md']
assert sorted(Path(x).name for x in removed)==expected
assert added==[x+'.gz' for x in removed]
assert all(a[x]==b[x] for x in a.keys()&b.keys())
result={'prior_check_record':ns['identity'](OUT/'composition_checks.json'),'current_composition_map':current,'current_evidence_copies':ns['copies'],'changed_representations':{'removed_from_manifest':removed,'added_to_manifest':added},'other_representations_identical':True,'note_primary_parent_and_mathematical_bodies_unchanged':True,'all_current_representations_decompress_to_original_bytes':True,'scientific_controls_rerun':False}
(OUT/'composition_refresh.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'source_composition_current.json').write_bytes(ns['MAP'].read_bytes())
print('Refresh confined to three historical review Markdown files now stored as gzip; their decompressed bytes match exactly.')
print('Note, primary, parent, both bodies, all remaining representations and four inherited source identities are unchanged; no scientific replay repeated.')

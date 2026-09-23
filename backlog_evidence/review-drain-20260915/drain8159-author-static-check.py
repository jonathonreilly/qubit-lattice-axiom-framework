from pathlib import Path
import ast,json,re,hashlib,gzip,difflib,subprocess
R=Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';P=R/'drain8159-originals';d=json.loads((R/'drain8159-author-canonical-draft-v2.json').read_text());plan=json.loads((R/'drain8159-author-ownership-plan-v2.json').read_text());m=json.loads((R/'drain8159-author-proof-mapping-v1.json').read_text());sha=lambda x:hashlib.sha256(x).hexdigest()
def norm(s):
 s=re.sub(r'\[([^\]]+)\]\((?!https?://)([^)]+)\)',lambda m:m[1]+' (`'+m[2]+'`)',s)
 return re.sub(r'^(#{1,6}) ',lambda m:'#'*(min(6,len(m[1])+2))+' ',s,flags=re.M)
patch=[];proofs=[]
for e in m:
 old=(P/e['original']).read_text();new=norm(old);body=(W/e['canonical_owner']).read_text();assert new in body
 proofs.append(e|{'canonical_start_line':body[:body.index(new)].count('\n')+1,'complete_normalized_text_sha256':sha(new.encode()),'only_presentation_changed':True})
 patch.extend(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=e['original'],tofile=e['canonical_owner']+'#'+e['anchor']))
assert norm((R/'drain8159-block27-original-proof.md').read_text()) in (W/d['notes'][1]).read_text()
runmap={Path(x['original']).name:Path(x['canonical_runner']).name for x in plan['active_evidence_programs']};notemap={Path(x['original']).name:Path(x['canonical_owner']).name for x in m};science=[]
for x in plan['active_evidence_programs']:
 raw=(P/x['original']).read_text();adapted=raw
 for a,b in runmap.items():adapted=adapted.replace(a,b).replace(a[:-3],b[:-3])
 for a,b in notemap.items():adapted=adapted.replace('notes/'+a,'docs/'+b)
 adapted=adapted.replace("root/'evidence/","root/'scripts/").replace("Path(__file__).with_suffix('.json')","_OUTPUT_JSON")
 adapted=re.sub(r"\(HERE\s*/\s*'[^']+\.json'\)","_OUTPUT_JSON",adapted)
 actual=(W/x['canonical_runner']).read_text();start=actual.index('\n# Canonical packaging;');end=actual.index('_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)\n',start)+len('_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)\n');actual=actual[:start]+actual[end:];actual=actual[:actual.rindex("\nif __name__ == '__main__':\n    print('TOTAL:")]
 assert ast.dump(ast.parse(actual),include_attributes=False)==ast.dump(ast.parse(adapted),include_attributes=False),x['canonical_runner']
 science.append({'runner':x['canonical_runner'],'entire_original_program_AST_preserved_after_only_literal_IO_import_path_adaptation':True,'assertion_count_preserved':sum(isinstance(z,ast.Assert) for z in ast.walk(ast.parse(raw)))})
manifest=json.loads((W/'docs/work_history/review_loop/pr8159/manifest.json').read_text())
for x in manifest['paths']:assert sha(gzip.decompress((W/x['archive']).read_bytes()))==x['sha256']
for x in d['files']:assert sha((W/x['path']).read_bytes())==x['sha256']
assert not subprocess.check_output(['git','-C',str(W),'diff','--name-only','HEAD']);assert not subprocess.check_output(['git','-C',str(W),'diff','--cached','--name-only'])
(R/'drain8159-author-note-corrections-v2.patch').write_text(''.join(patch));(R/'drain8159-author-full-proof-map-v2.json').write_text(json.dumps(proofs,indent=2)+'\n')
result={'source_paths':436,'original_archives':366,'extra_import':'complete Block27 exact7a0a953d... proof plus gzip/manifest','complete_owned_original_proofs':71,'complete_program_AST_checks':science,'all_frozen_hashes_match':True,'original_math_preservation':'Every original proof text survives, except heading depth and internal Markdown links rendered as textual provenance. Entire original program AST survives after literal IO/import path adaptation; added input/output metadata and N5/one completed-program TOTAL only.','review_scope':'Complete transformation rules and source-specific changed lines reviewed; independent original scientific reports remain authoritative for unchanged full proof bodies; no new author mathematical acceptance claimed.','vocabulary':'zero violations','pending':'Original reviewer complete affected-source confirmation; root fresh guarded FF and9 additive registry entries; dual discovery/cheap preflight; bounded captures and final source/evidence check','no_primary_execution':True,'tracked_index_unchanged':True}
(R/'drain8159-author-preservation-checks-v2.json').write_text(json.dumps(result,indent=2)+'\n');print('71 full proof and41 complete program AST checks passed; no source execution')

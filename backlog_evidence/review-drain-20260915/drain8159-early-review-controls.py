import pathlib,json,hashlib,re,ast,gzip,difflib,subprocess
R=pathlib.Path('/private/tmp/review-drain-20260915');W=R/'review-draft-slot';H=lambda b:hashlib.sha256(b).hexdigest();load=lambda p:json.loads(p.read_text());d=load(R/'drain8159-author-canonical-draft-v2.json');pm=load(R/'drain8159-author-full-proof-map-v2.json');op=load(R/'drain8159-author-ownership-plan-v2.json');h=load(R/'drain8159-author-prepared-handoff-v2.json')
meta=[dict(x,actual_sha256=H(pathlib.Path(x['path']).read_bytes()),matches=H(pathlib.Path(x['path']).read_bytes())==x['sha256']) for x in h['source_metadata_references']]
files=[dict(x,matches=H((W/x['path']).read_bytes())==x['sha256']) for x in d['files']]
# Compare all argument lines: headings may deepen; actual Markdown links may become explicit provenance. Record EVERY other change.
proof=[];corrupt=[]
for x in pm:
 old=(R/'drain8159-originals'/x['original']).read_text().splitlines();lines=(W/x['canonical_owner']).read_text().splitlines();start=x['canonical_start_line']-1;new=lines[start:start+len(old)]
 for j,(a,b) in enumerate(zip(old,new)):
  allowed=re.sub(r'^(#+) ',lambda m:'#'*(len(m[1])+2)+' ',a)
  allowed=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1]+' (`'+m[2]+'`)' if m[2].endswith('.md') or m[2].startswith(('http://','https://')) else m[0],allowed)
  if allowed!=b:corrupt.append({'original':x['original'],'original_line':j+1,'canonical':x['canonical_owner'],'canonical_line':start+j+1,'expected':allowed,'actual':b})
 proof.append({'original':x['original'],'canonical':x['canonical_owner'],'line_count':len(old),'same_line_count':len(new)==len(old)})
# All program math compared after ONLY explicit path/output-name adaptation, added metadata/footer removal.
name_map={pathlib.Path(x['original']).stem:pathlib.Path(x['canonical_runner']).stem for x in op['active_evidence_programs']};note_map={pathlib.Path(x['original']).name:x['canonical_owner'] for x in pm};programs=[];diffs=[]
for x in op['active_evidence_programs']:
 old=(R/'drain8159-originals'/x['original']).read_text();new=(W/x['canonical_runner']).read_text()
 new=re.sub(r'\n# Canonical packaging;.*?_OUTPUT_JSON.parent.mkdir\(parents=True, exist_ok=True\)\n','\n',new,flags=re.S)
 new=new[:new.rfind("\nif __name__ == '__main__':\n    print('TOTAL: PASS=1 FAIL=0')")]
 expected=old
 for a,b in name_map.items():expected=expected.replace(a,b)
 for a,b in note_map.items():expected=expected.replace('notes/'+a,b)
 expected=expected.replace("evidence/"+name_map['block9_polarized_word_check']+'.py',"scripts/"+name_map['block9_polarized_word_check']+'.py')
 expected=expected.replace("Path(__file__).with_suffix('.json')",'_OUTPUT_JSON')
 expected=re.sub(r"\(HERE/'[^']+\.json'\)",'_OUTPUT_JSON',expected)
 same=ast.dump(ast.parse(expected))==ast.dump(ast.parse(new))
 programs.append({'path':x['canonical_runner'],'same_complete_original_ast_after_enumerated_adaptation':same,'original_asserts':sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(old))),'original_sha256':H(old.encode()),'canonical_sha256':H((W/x['canonical_runner']).read_bytes())})
 if not same:diffs.append('\n'.join(difflib.unified_diff(expected.splitlines(),new.splitlines(),fromfile=x['original'],tofile=x['canonical_runner'])) )
b27=load(R/'drain8159-block27-import-recovery-v1.json');raw=gzip.decompress((W/b27['archive']).read_bytes());s=(W/b27['canonical_destination']).read_text();normalized=re.sub(r'^(#+) ',lambda m:'#'*(len(m[1])+2)+' ',raw.decode(),flags=re.M);b27exact=normalized.strip() in s
report={'metadata':meta,'files':files,'proof_checks':proof,'unpermitted_proof_changes':corrupt,'program_checks':programs,'block27':{'original_sha256_matches':H(raw)==b27['sha256'],'complete_heading_only_text_present':b27exact},'program_nonmatching_count':len(diffs)}
(R/'drain8159-early-review-controls.json').write_text(json.dumps(report,indent=2)+'\n');(R/'drain8159-early-review-program-differences.patch').write_text('\n'.join(diffs))
print('metadata',all(x['matches'] for x in meta),'files',len(files),all(x['matches'] for x in files),'proofchanges',len(corrupt),'program mismatches',len(diffs),'b27',report['block27']);print(json.dumps(corrupt,indent=1))

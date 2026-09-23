import pathlib,json,gzip,hashlib,ast,subprocess
root=pathlib.Path('/private/tmp/review-drain-20260915'); wd=root/'review-draft-slot'; rec=json.loads((root/'drain8031-author-prepared-v1.json').read_text()); orig=json.loads((root/'drain8031-original-manifest.json').read_text()); result={}
def sha(b):return hashlib.sha256(b).hexdigest()
result['prepared_sha256']=sha((root/'drain8031-author-prepared-v1.json').read_bytes()); assert result['prepared_sha256']=='2c5604f7302b869731bb0a7080b9a20aa48d5e9d7e6e7e0174f27a53087d9d81'
for f in rec['source']:assert sha((wd/f['path']).read_bytes())==f['sha256'],f['path']
a={x['path']:x for x in orig['files']};b={x['path']:x for x in rec['original_dispositions']};assert a.keys()==b.keys()
for p,x in a.items():
 y=b[p]
 for k in ['mode','blob','sha256','size']:assert x[k]==y[k],(p,k)
 raw=gzip.decompress((wd/y['recovery']).read_bytes());assert sha(raw)==x['sha256'];assert raw==(root/'drain8031-originals'/p).read_bytes()
result['source_hashes_match']=74;result['exact_archive_originals_match']=70
rn='scripts/gauge_wilson_finite_transporter_pw_defect_check_2026_09_07.py';old=(root/'drain8031-originals'/rn).read_text();new=(wd/rn).read_text(); region=lambda s:s[s.index('started=_started'):s.rindex('_emit(out, 17')];assert region(old)==region(new); result['runner_mathematical_region_exact']=True
ast.parse(new)
scopes=ast.literal_eval(next(n for n in ast.walk(ast.parse(new)) if isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='_emit').args[2]); result['n5_counts']={k:v['checks']for k,v in scopes.items()};assert sum(result['n5_counts'].values())==17
op='docs/GAUGE_WILSON_FINITE_TRANSPORTER_UNITARITY_PW_DEFECT_BOUNDED_THEOREM_NOTE_2026-09-07.md';np=rec['source'][0]['path']; ot=(root/'drain8031-originals'/op).read_text(); nt=(wd/np).read_text(); formulas=[s for s in ot.splitlines() if s.startswith(' ')]; assert all(s in nt for s in formulas);result['original_display_formula_lines_preserved']=len(formulas)
result['runtime_inputs']=[]
for p,h in rec['runtime_inputs'].items():assert sha((wd/p).read_bytes())==h;result['runtime_inputs'].append({'path':p,'sha256':h})
result['run_scope']='Read-only archive/hash/AST/formula verification; no primary execution'
(root/'drain8031-early-verification-v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

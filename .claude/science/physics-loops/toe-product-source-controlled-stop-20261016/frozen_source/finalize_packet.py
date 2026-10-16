"""Write review maps and one final immutable inventory; no science execution."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json
D=Path(__file__).resolve().parent
assert not (D/'FINAL_FREEZE.json').exists()
def pin(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(D)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def dump(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
primary=D/'proposal/scripts/product_source_controlled_stop_2026_10_16.py'
lines=primary.read_text().count('\n')
p=D/'proposal/packet_text/PR_BODY.md';p.write_text(p.read_text().replace('83-line',str(lines)+'-line'))
code=[]
for p in [D/'build_packet.py',primary,D/'record_metadata.py',Path(__file__)]:
 b=p.read_bytes();rows=b.splitlines(keepends=True);funcs=[]
 for node in ast.walk(ast.parse(b)):
  if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)):
   src=b''.join(rows[node.lineno-1:node.end_lineno]);funcs.append(dict(name=node.name,start_line=node.lineno,end_line=node.end_lineno,sha256=hashlib.sha256(src).hexdigest(),reuse='exact ident function from exposed review inspectors' if node.name=='ident' else 'new scoped metadata code; no scientific function reuse'))
 code.append(dict(**pin(p),functions=sorted(funcs,key=lambda x:x['start_line']),module_changes='all module setup/control flow new for this scoped packet'))
source=D.parent/'product_source_mediator_external_stop_exposed_check/inspect_sources.py'
a=source.read_bytes().splitlines(keepends=True)
node=next(n for n in ast.walk(ast.parse(source.read_bytes())) if isinstance(n,ast.FunctionDef) and n.name=='ident')
ref=b''.join(a[node.lineno-1:node.end_lineno])
for p in [D/'build_packet.py',primary]:
 a=p.read_bytes().splitlines(keepends=True);n=next(n for n in ast.walk(ast.parse(p.read_bytes())) if isinstance(n,ast.FunctionDef) and n.name=='ident')
 assert b''.join(a[n.lineno-1:n.end_lineno])==ref
reuse=dict(source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),function='ident',source_lines=[node.lineno,node.end_lineno],function_sha256=hashlib.sha256(ref).hexdigest(),exact_targets=['build_packet.py:ident',str(primary.relative_to(D))+':ident'],all_other_code='new bounded metadata bookkeeping; not copied or scientifically executed')
dump(D/'CODE_MAP.json',dict(files=code,reuse=reuse))
m=json.loads((D/'INPUT_MANIFEST.json').read_bytes())
maptext='\n'.join(f"- {x['label']}: note lines {x['start_line']}–{x['end_line']}, bytes [{x['start_byte']},{x['end_byte']}), SHA256 {x['sha256']}." for x in m['bodies'])
guide=f'''# Root read guide

The proposed note is `{m['note']['path']}` ({m['note']['bytes']} bytes, SHA256 {m['note']['sha256']}). The new wrapper is `wrapper.md`; the ten immutable appendices begin at note line {m['bodies'][0]['start_line']}. Source-science acceptance is real; wrapper approval remains null. Read both complete controlling qualifications after the four source/review pairs. The sole direct canonical parent is pinned in INPUT_MANIFEST; its complete 63,977-byte note was read in bounded chunks through the end. The parent eight-body packet is not copied.

The exact primary is `{primary.relative_to(D)}`, {lines} lines, SHA256 {pin(primary)['sha256']}. It checks source identities and historical metadata only. CODE_MAP.json lists every function with exact line intervals and hashes and proves the sole identical reused function, ident, against the frozen external-stop inspector. Every other function/module block is new scoped metadata code. No scientific function was imported, executed or changed. The full proposed source diff is PROPOSED_FILES.diff (all proposed note/script/packet text files versus /dev/null); UNCHANGED_BODY_DIFFS.txt records every unchanged input body. Diff repetition is a review view, not another source archive.

{maptext}

Read coverage: all four complete author addenda; all four complete exposed analytical reviews including the attributed tail appendix; both complete root decisions and qualifications; the entire direct canonical parent; all four actual inspector sources, the common launcher, both root execution sources, root recorder and complete stdout/stderr. Source coverage/reuse records are preserved exactly. The source-only wrapper is an author synthesis, not an independent check of its own sources. Metadata checks do not substitute for the analytical reads.

Recovery is selected and bounded: 59 original evidence aliases resolve to 40 content-addressed blobs. Current review freezes/manifests/coverage, actual sources, original receipts/streams, root decisions and parent publication/attachment records are included. Original older schemas are retained. Ten complete bodies live once in the note, recoverable by byte intervals. The full parent and recursively referenced ancestor archive members are pinned externally, not recopied. The helper verifies all 107 immediate members of the six selected original freezes; it does not recursively replay predecessor archives or science.

Actual commands: read-only `cat`, bounded `sed -n`, and `rg --files`/`rg -n` were used to discover and read the exact sources; two `python3 -B product_source_controlled_stop_publication_draft/build_packet.py` runs assembled the evolving source (no fabricated source-at-launch receipts are claimed for those assembly calls). Shell heredocs and inline Python wrote only this directory. `python3 -B product_source_controlled_stop_publication_draft/record_metadata.py source_check` exited 0. `python3 -B product_source_controlled_stop_publication_draft/record_metadata.py approval_refusal` exited 2 by design. Their actual child argv, executable/recorder captures, timing and complete streams are under metadata/. `python3 -B product_source_controlled_stop_publication_draft/finalize_packet.py` writes the maps/diff/freeze after the checks; no scientific execution or canonical command is part of that operation.

Preserved operational limitations: initial rg over the then-missing C1 directory returned exit 2; initial cat using guessed QUALIFIED_ACCEPTANCE.json/FINAL_QUALIFICATIONS.md returned exit 1, after which actual ACCEPTANCE.json/QUALIFICATION.md were found and read. A later rg including two nonexistent possible root directories also returned exit 2. One combined output was truncated; affected work/external-stop reviews were reread completely in a bounded untruncated call. C1 and final root stop/C1 records appeared during this task and were subsequently fully read/pinned. These were discovery/read issues, not scientific failures. CHECKPOINT.md preserves the earlier pending state as history; this guide and final manifest supersede it.

Integration is intentionally small: root may copy the unchanged helper and pass `--packet-root /absolute/path/to/this/frozen/packet`. The helper remains provenance-only; root separately retains actual base, canonical note/body binding, staged checks/review and publication evidence. Source byte offsets are not automatically canonical byte offsets. `--require-approved` cannot grant approval. No cache/graph/lock/Git/canonical/PR/audit action, physical axiom or editable prompt change occurred here.
'''
(D/'ROOT_READ_GUIDE.md').write_text(guide)
proposed=sorted(p for p in (D/'proposal').rglob('*') if p.is_file())
(D/'PROPOSED_FILES.diff').write_text(''.join(''.join(difflib.unified_diff([],p.read_text().splitlines(True),fromfile='/dev/null',tofile=str(p.relative_to(D/'proposal')))) for p in proposed))
for label,wanted in [('source_check',0),('approval_refusal',2)]:
 p=D/'metadata'/label;e=json.loads((p/'EXECUTION.json').read_bytes());assert e['exit_code']==wanted and not e['timed_out'] and e['scientific_executions']==0
 assert e['argv'][2]==e['child_source_at_launch']['path'] and Path(e['child_source_at_launch']['path']).read_bytes()==(p/'executed_source.py').read_bytes()==primary.read_bytes()
 for k in ['stdout','stderr','recorder','recorder_capture','source_capture']:
  q=Path(e[k]['path']);assert len(q.read_bytes())==e[k]['bytes'] and hashlib.sha256(q.read_bytes()).hexdigest()==e[k]['sha256']
 assert e['source_unchanged_during_run'] and (p/'stderr').read_bytes()==b''
assert json.loads((D/'metadata/source_check/stdout').read_bytes())['metadata_verification']=='verified'
assert json.loads((D/'metadata/approval_refusal/stdout').read_bytes())['approval']=='refused'
files=sorted(p for p in D.rglob('*') if p.is_file())
freeze=dict(schema='product_source_controlled_stop_source_only_freeze_v1',created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='author source-only proposal; actual source acceptance; wrapper/canonical/publication unbound',members=[pin(p) for p in files],scientific_executions=0,editable_prompt_files_changed=[])
dump(D/'FINAL_FREEZE.json',freeze)
print(json.dumps(dict(freeze=pin(D/'FINAL_FREEZE.json'),members=len(files),note=pin(D/m['note']['path']),primary=pin(primary),metadata_source_check_exit=0,approval_refusal_exit=2,scientific_executions=0),indent=2))

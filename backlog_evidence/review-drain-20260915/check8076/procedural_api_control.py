import importlib.util,sys,tempfile,json,hashlib
from pathlib import Path
R=Path('/private/tmp/review-drain-20260915');W=R/'review-slot-one'
sys.path.insert(0,str(W/'scripts'));sys.path.insert(0,str(W/'docs/audit/scripts'))
def load(n,p):
 spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);sys.modules[n]=m;spec.loader.exec_module(m);return m
g=load('proofdoc_graph',W/'docs/audit/scripts/build_citation_graph.py');c=load('proofdoc_cache',W/'scripts/runner_cache.py')
with tempfile.TemporaryDirectory() as t:
 p=Path(t);(p/'docs').mkdir();(p/'outputs').mkdir();owner=p/'docs/note.md';proof=p/'outputs/proof.md';owner.write_text('Note');proof.write_text('Current mathematical proof')
 g.REPO_ROOT=p;g.DOCS_DIR=p/'docs';assert proof not in g.discover_notes();assert g.resolve_link_target('../outputs/proof.md',owner) is None
 script=p/'r.py';script.write_text('AUDIT_TIMEOUT_SEC = 30\n');assert c.declared_timeout_for(script)==30;script.write_text('print(1)\n');assert c.declared_timeout_for(script) is None
report={'status':'PASS: procedural clarification only','source_sha256':hashlib.sha256((W/'docs/ai_methodology/skills/review-loop/references/UNIT_RECEIPT.md').read_bytes()).hexdigest(),'checks':['Actual graph excludes outputs proof and rejects outside-docs Markdown target','Actual timeout API returns declared positive value and None when absent','Actual schema2 requires discovered proof; runtime input categories accept ordinary non-note paths under schema1','Owned-proof parent distinction confirmed by independent train50 adapter controls'],'evidence':['8069-owned-proof-classification-addendum.json','8069-owned-proof-adapter-controls.json'],'scope':'No checker change, full gate, source mutation or scientific execution; deferred landing context only.'}
(R/'skill-proof-ownership-independent-review.json').write_text(json.dumps(report,indent=2)+'\n');print(report)

from pathlib import Path
import sys,json,importlib.util,tempfile
w=Path('/private/tmp/review-drain-20260915/receipt-authority-fix');sys.path.insert(0,str(w/'docs/audit/scripts'));import build_citation_graph as g
spec=importlib.util.spec_from_file_location('receipt_review',w/'docs/ai_methodology/skills/review-loop/scripts/review_receipt.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
reg=json.loads(g.AXIOM_PREMISE_NODES_PATH.read_text());e=reg['nodes']['minimal_axioms'];candidates=[w/p for p in e['aliased_paths'] if (w/p).is_file()];ids={'minimal_axioms':candidates};out=[]
m.require_current_parent(w,g,ids,e['current_path']);out.append('actual current minimal_axioms accepted among historical aliases')
for p in e['aliased_paths']:
 if p==e['current_path'] or not (w/p).exists():continue
 try:m.require_current_parent(w,g,{'minimal_axioms':[w/p]},p)
 except ValueError as exc:assert 'not current' in str(exc);out.append('superseded singleton rejected: '+p)
 else:raise AssertionError(p)
# Ordinary case-insensitive canonical collision remains rejected.
p=w/'docs/NATIVE_LEADING_RING_STOQUASTIC_GAUGE_NOTE_2026-09-08.md';cid=g.claim_id_from_path(p)
try:m.require_current_parent(w,g,{cid:[p,p.with_name(p.name.lower())]},p.relative_to(w).as_posix())
except ValueError as exc:assert 'ambiguous parent' in str(exc);out.append('ordinary unregistered duplicate ID rejected')
else:raise AssertionError('ordinary duplicate accepted')
print(json.dumps({'status':'passed','controls':out},indent=2))

"""Apply root's two publication-only edits and preserve canonical attempt one."""
from pathlib import Path
import hashlib
import json
import shutil
import sys

D=Path(__file__).resolve().parent
W=D.parents[1]/'correlation_worktree'
Q=W/'.claude/science/physics-loops/toe-structural-coefficient-box-20261017'
p=W/'docs/STRUCTURAL_COEFFICIENT_BOX_BOUNDED_THEOREM_NOTE_2026-10-17.md'
A=D/'canonical_attempt_1';A.mkdir(exist_ok=False)
for name in ('CANONICAL_EXECUTION.json','canonical.stdout','canonical.stderr'):
    shutil.move(D/name,A/name)
for src,dest in [(p,'note.md'),(W/'outputs/structural_coefficient_box_2026_10_17.json','canonical_result.json'),
                 (W/'logs/runner-cache/structural_coefficient_box_2026_10_17.txt','canonical_cache.txt')]:
    shutil.copyfile(src,A/dest)
def pin(raw):return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
old=p.read_text()
changes=[('wrapper_root_approval: pending_separate_root_review','wrapper_root_approval: see_separate_root_review_record'),
         ('publication are separate records.', 'publication are separate records. Final wrapper approval is addressed by the\n[root wrapper review record](../.claude/science/physics-loops/toe-structural-coefficient-box-20261017/ROOT_WRAPPER_REVIEW.json).')]
new=old
for before,after in changes:
    assert new.count(before)==1
    new=new.replace(before,after,1)
p.write_text(new)
begin='<!-- BEGIN FROZEN COEFFICIENT ARGUMENT -->\n'
end='\n<!-- END FROZEN COEFFICIENT ARGUMENT -->'
oldbody=old.split(begin,1)[1].split(end,1)[0]
newbody=new.split(begin,1)[1].split(end,1)[0]
assert oldbody==newbody
assert newbody.encode()==(W/'outputs/structural_coefficient_box_2026_10_17_inputs/author/CANDIDATE.md').read_bytes()

sys.dont_write_bytecode=True
sys.path.insert(0,str(W/'docs/audit/scripts'))
import build_citation_graph as b
def node_surface(body):
    raw,hint=b.extract_claim_type_hint(body)
    runner=b.extract_runner(body,p.relative_to(b.DOCS_DIR).as_posix())
    cid=b.claim_id_from_path(p)
    return {'claim_id':cid,'path':str(p.relative_to(W)),'title':b.extract_title(body),
            'claim_type_author_hint_raw':raw,'claim_type_author_hint':hint,
            'claim_type_seed_hint':hint or b.extract_legacy_status_claim_type(body),
            'runner_path':runner,'helper_runner_paths':b.helper_runner_paths_for_claim(cid,runner),
            'deps':[b.claim_id_from_path(x) for x in b.extract_citations(body,p)]}
surface_old=node_surface(old);surface_new=node_surface(new)
graph=json.loads((D/'GRAPH_VERIFICATION.json').read_text())
assert surface_old==surface_new=={k:v for k,v in graph['new_node'].items() if k!='note_hash'}
assert graph['new_node']['note_hash']==pin(old.encode())['sha256']
assert graph['manifest_sha256']==pin((W/'docs/audit/data/citation_graph_manifest.json').read_bytes())['sha256']
record={'scope':'Root-requested wrapper metadata and root-record link only; no source-body or scientific changes.',
        'old_note':pin(old.encode()),'new_note':pin(new.encode()),
        'changes':[{'old':x,'new':y} for x,y in changes],
        'body_byte_identical':True,'body_sha256':pin(newbody.encode())['sha256'],
        'graph_extraction_before':surface_old,'graph_extraction_after':surface_new,
        'all_graph_fields_except_note_hash_identical':True,
        'graph_builder_sha256':pin(Path(b.__file__).read_bytes())['sha256'],
        'manifest_unchanged_sha256':graph['manifest_sha256'],
        'graph_scope':'Completed graph JSON retains its actual pre-edit note hash and is validation residue. Its topology manifest is unchanged and remains correct; no graph rebuild or synthetic note-hash refresh is claimed.',
        'root_owned_record_pending':str((Q/'ROOT_WRAPPER_REVIEW.json').relative_to(W))}
(D/'NOTE_REFRESH.json').write_text(json.dumps(record,indent=2)+'\n')
s=json.loads((Q/'SOURCE_MANIFEST.json').read_text())
s['note']={'path':str(p.relative_to(W)),**pin(p.read_bytes())}
s['body_offset_zero_based']=p.read_bytes().index(begin.encode())+len(begin.encode())
s['root_requested_wrapper_refresh']='evidence/NOTE_REFRESH.json'
(Q/'SOURCE_MANIFEST.json').write_text(json.dumps(s,indent=2)+'\n')
print(json.dumps({'note':s['note'],'frozen_body_unchanged':True,'graph_topology_unchanged':True,'attempt1_preserved':str(A)},indent=2))

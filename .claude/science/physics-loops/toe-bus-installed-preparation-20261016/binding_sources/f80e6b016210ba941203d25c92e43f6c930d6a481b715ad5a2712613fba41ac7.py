"""Record completed root review and independently verify the source-only packet."""
from pathlib import Path
import ast,datetime,hashlib,json
O=Path(__file__).resolve().parent; N=O.parent
D=N/'bus_preparation_publication_draft'; P=D/'proposal'
M=P/'.claude/science/physics-loops/toe-bus-installed-preparation-20261016'
def sha(b):return hashlib.sha256(b).hexdigest()
def pin(p):
    b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=sha(b))
def read(p):return json.loads(p.read_text())
def check(p,row):
    b=p.read_bytes();assert len(b)==row['bytes'] and sha(b)==row['sha256'],str(p)
def write(p,obj):
    assert not p.exists(),str(p);p.write_text(json.dumps(obj,indent=2)+'\n')
def main():
    assert pin(D/'FINAL_FREEZE.json')['sha256']=='ed576446fcbf5f0aae92054730165082e2c68567b09baaf389d36b49f6d87278'
    f=read(D/'FINAL_FREEZE.json');assert len(f['members'])==138
    for x in f['members']:check(D/x['path'],x)
    actual={str(p.relative_to(D)) for p in D.rglob('*') if p.is_file()}
    assert actual=={x['path'] for x in f['members']}|{'FINAL_FREEZE.json'}
    assert not any(p.is_symlink() for p in D.rglob('*'))
    closure=read(D/'ARCHIVE_CLOSURE.json')['members']
    assert {x['path'] for x in closure}==actual-{'FINAL_FREEZE.json','ARCHIVE_CLOSURE.json'}
    for x in closure:check(D/x['path'],x)
    archive=read(M/'ARCHIVE_INDEX.json')['sources'];assert len(archive)==107
    by_original={x['original']:x for x in archive};assert len(by_original)==107
    for x in archive:
        check(Path(x['original']),x);check(P/x['recovery'],x)
        assert Path(x['original']).read_bytes()==(P/x['recovery']).read_bytes()
    manifest=read(M/'SOURCE_MANIFEST.json');count=0
    for item in manifest['freezes']:
        rows=read(Path(item['original']))[item['row_key']];count+=len(rows)
        assert len(rows)==item['member_count']
        paths=[]
        for row in rows:
            p=Path(row['path']);p=p if p.is_absolute() else Path(item['base'])/p
            check(P/by_original[str(p)]['recovery'],row);paths.append(str(p))
        assert paths==item['members']
    assert len(manifest['freezes'])==6 and count==85
    bmap=read(M/'BODY_MAP.json');note=(P/bmap['note']).read_bytes()
    assert note[:bmap['wrapper']['bytes']]==(D/'wrapper.md').read_bytes()
    assert len(bmap['bodies'])==7
    for row in bmap['bodies']:
        b=Path(row['original']).read_bytes();assert note.count(b)==1
        assert note[row['start_byte']:row['end_byte_exclusive']]==b
    primary=P/'scripts/bus_installed_preparation_2026_10_16.py'
    code=primary.read_text();tree=ast.parse(code)
    decl=[x for x in tree.body if isinstance(x,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='DECLARED_INPUTS' for t in x.targets)]
    assert len(decl)==1
    table=ast.literal_eval(decl[0].value);assert len(table)==86
    assert code==(D/'primary_template.py').read_text().replace('@@DECLARED_INPUTS@@',repr(table))
    assert {str(p.relative_to(P)) for p in P.rglob('*') if p.is_file()}==set(table)|{str(primary.relative_to(P))}
    for name,row in table.items():check(P/name,row)
    receipts=[]
    for label,expected in [('build_01',0),('integrity_01',0),('controls_01',0),('default_refusal_01',2),('inspection_01',0)]:
        r=D/'metadata_runs'/label;e=read(r/'EXECUTION.json');l=read(r/'LAUNCH.json')
        assert all(e[k]==v for k,v in l.items())
        assert e['exit_code']==expected==e['expected_exit'] and not e['timed_out']
        assert e['argv'][2]==str(r/'source_at_launch.py') and e['cwd']==str(D)
        for key in ['source_original','source_at_launch','recorder_at_launch','stdout','stderr']:check(Path(e[key]['path']),e[key])
        assert e['source_original']['sha256']==e['source_at_launch']['sha256']
        assert (r/'stderr').read_bytes()==b''
        receipts.append(dict(label=label,receipt=pin(r/'EXECUTION.json'),actual_exit=expected))
    controls=read(D/'metadata_runs/controls_01/stdout')
    assert len(controls['scoped_in_memory_corruptions_rejected'])==5
    verification=read(D/'VERIFICATION.json')
    assert verification['acceptance_reference_edges_checked']==18
    # Validate each acceptance reference against current source and archived original.
    relation_count=0
    for rel,fields in {
      'bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json':['candidate','candidate_freeze','exposed_review','review_freeze','root_reconstruction','root_reconstruction_freeze','controlling_qualifications','actual_scientific_execution','actual_provenance_execution'],
      'bus_bounded_slew_preparation_root_review/QUALIFIED_ACCEPTANCE.json':['proposal','proposal_freeze','review','review_freeze','controlling_qualifications','parent_acceptance','parent_qualifications','review_execution','source_manifest']}.items():
        a=read(N/rel)
        for k in fields:
            row=a[k];check(Path(row['path']),row);check(P/by_original[row['path']]['recovery'],row);relation_count+=1
    recovery=read(D/'INTERRUPTION_RECOVERY.json')['selected_partial_snapshot']
    assert len(recovery['files'])==8
    for row in recovery['files']:
        check(Path(row['original']['path']),row['original']);check(Path(row['captured']['path']),row['captured'])
    result=dict(reviewed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='source-only wrapper/code accepted for separately reviewed canonical integration; not retained audit',
        review=pin(O/'REVIEW.md'),source_freeze=pin(D/'FINAL_FREEZE.json'),source_note=pin(P/bmap['note']),source_primary=pin(primary),
        wrapper=pin(D/'wrapper.md'),frozen_members=138,selected_live_sources=107,immutable_bodies=7,declared_inputs=86,acceptance_reference_edges=relation_count,
        metadata_receipts=receipts,scientific_reexecutions=0,cluster_cap='OPEN conditional on canonical conformance',
        actual_canonical_acceptance=None,actual_new_publication=None,retained_audit=False,editable_prompt_files_changed=[])
    write(O/'REVIEW.json',result)
    write(O/'FREEZE.json',dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=[pin(p) for p in sorted(O.iterdir()) if p.is_file()]))
    print(json.dumps(dict(review=pin(O/'REVIEW.json'),freeze=pin(O/'FREEZE.json'),members=138,sources=107,bodies=7,scientific_executions=0)))
if __name__=='__main__':main()

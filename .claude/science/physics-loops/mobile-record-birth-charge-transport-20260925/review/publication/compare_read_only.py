"""Fresh publication42+43 correspondence checker. Reads files and prints only.

No scientific module, cache writer, prior verifier, or sealing writer is
imported or executed. All result leaves are compared, with exactly the root
elapsed_seconds scalar excluded. This is correspondence, not a science rerun.
"""
from pathlib import Path
from hashlib import sha256
from collections import Counter
import ast,json,re,stat

HERE=Path(__file__).resolve().parent
OWN=HERE.parent
EXT=OWN.parent
PUB=EXT/'birth-charge-transport-publication'
SNAP=HERE/'sources/publication'


def digest(path):return sha256(path.read_bytes()).hexdigest()


def observed(path):
    s=path.stat();raw=path.read_bytes()
    return dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw),mode=s.st_mode,
                dev=s.st_dev,ino=s.st_ino,mtime_ns=s.st_mtime_ns,ctime_ns=s.st_ctime_ns,nlink=s.st_nlink)


def compare(a,b,path=()):
    assert type(a) is type(b),(path,type(a).__name__,type(b).__name__)
    if path==('elapsed_seconds',):
        assert type(a) is float and a>0 and b>0
        return 0,[dict(path=list(path),historical=a,fresh=b)]
    if isinstance(a,dict):
        assert set(a)==set(b),(path,'key mismatch')
        count=0;differences=[]
        for key in a:
            n,d=compare(a[key],b[key],path+(key,));count+=n;differences+=d
        return count,differences
    if isinstance(a,list):
        assert len(a)==len(b),(path,'list length')
        count=0;differences=[]
        for i,(x,y) in enumerate(zip(a,b)):
            n,d=compare(x,y,path+(i,));count+=n;differences+=d
        return count,differences
    assert a==b,(path,a,b)
    return 1,[]


def literal_assignments(path):
    result={}
    tree=ast.parse(path.read_text())
    for node in tree.body:
        if isinstance(node,ast.Assign):
            for target in node.targets:
                if isinstance(target,ast.Name) and target.id in ('AUDIT_INPUT_PATHS','AUDIT_TIMEOUT_SEC','RUNTIMES','OUTPUT_DIRECTORY'):
                    result[target.id]=ast.literal_eval(node.value)
    return result,tree


def main():
    pins=json.loads((HERE/'SOURCE_PINS.json').read_text())
    mechanical=json.loads((HERE/'MECHANICAL_SOURCE_PINS.json').read_text())
    all_pins=pins['sources']+mechanical['sources']
    def check_origins():
        for row in all_pins:
            current=observed(Path(row['origin']))
            assert all(current[key]==row[key] for key in current if key!='path'),row['origin']
            copy=HERE/row['snapshot']
            assert digest(copy)==row['sha256'] and copy.stat().st_size==row['bytes']
    check_origins()
    prior=json.loads((HERE/'OWN_43_PRESERVATION_BEFORE.json').read_text())
    for row in prior['files']:assert observed(Path(row['path']))==row
    frozen=json.loads((HERE/'sources/external/BIRTH_CHARGE_TRANSPORT_FROZEN_SOURCES.json').read_text())
    root=json.loads((HERE/'sources/external/BIRTH_CHARGE_TRANSPORT_PRIMARY_ROOT_VERIFICATION.json').read_text())
    for rel,expected in frozen['files_sha256'].items():assert digest(SNAP/rel)==expected
    working=json.loads((HERE/'sources/external/BIRTH_CHARGE_TRANSPORT_PUBLICATION_WORKING_SOURCES.json').read_text())
    assert all(frozen[k]==v for k,v in working.items())

    note=(SNAP/frozen['note']).read_text()
    sections=[
        note.split('## Complete charge argument\n\n',1)[1].split('\n## Complete subsequent-dynamics argument\n\n',1)[0],
        note.split('## Complete subsequent-dynamics argument\n\n',1)[1].split('\n## Reproduction and observation boundary\n\n',1)[0]]
    originals=[
        HERE/'sources/author42/ORIGINAL_BIRTH_CHARGE_CLUSTERS_ROOT.md',
        HERE/'sources/author43/ORIGINAL_BIRTH_CLUSTER_TRANSPORT_ROOT.md']
    proof_results=[]
    for i,(path,body) in enumerate(zip(originals,sections)):
        original=path.read_text();presented=original;counts=[]
        for replacement in frozen['presentation_replacements'][i]:
            count=presented.count(replacement['old']);assert count==1
            presented=presented.replace(replacement['old'],replacement['new'])
            counts.append(dict(old=replacement['old'],new=replacement['new'],occurrences=count))
        presented=re.sub(r'^(#+)(?= )',lambda m:m.group(1)+'#'*frozen['heading_level_increment'],presented,flags=re.M)
        assert presented.strip()==body.strip()
        proof_results.append(dict(original_sha256=digest(path),complete_embedded_argument_exact=True,
                                  replacements=counts,heading_increment=frozen['heading_level_increment']))
    assert '**Type:** bounded_theorem' in note
    assert '**Status:** conditional mathematics with selective independent checks; no retained audit status.' in note
    assert 'S(k)=(4/3) sum_i (1-cos(k_i))' in note
    assert 'The all-sign average is essential in (8)-(10).' in note
    assert 'An actually occurring conditioned mark requires kappa>0.' in note
    assert 'not necessarily the range of the coherent output isometry' in note
    assert 'OVERLAPPING A-star pairs' in note

    runtime_results=[]
    originals_runtime=[
        HERE/'sources/author42/charge_cluster_controls.py',
        HERE/'sources/author43/cluster_escape_controls.py',
        HERE/'sources/author43/birth_geometry.py']
    for rel,old in zip(frozen['runtime'],originals_runtime):
        p=SNAP/rel
        assert p.read_bytes()==old.read_bytes()
        tree=ast.parse(p.read_text())
        runtime_results.append(dict(path=rel,sha256=digest(p),exact_original_bytes=True,
            functions=[x.name for x in tree.body if isinstance(x,ast.FunctionDef)],
            imports=[ast.unparse(x) for x in tree.body if isinstance(x,(ast.Import,ast.ImportFrom))]))
    assert (SNAP/frozen['runtime'][0]).read_bytes()==(SNAP/frozen['runtime'][2]).read_bytes()
    declarations,wrapper_tree=literal_assignments(SNAP/frozen['runner'])
    expected_inputs=(frozen['note'],*frozen['parent_paths'],*frozen['runtime'])
    assert declarations['AUDIT_INPUT_PATHS']==expected_inputs
    assert declarations['RUNTIMES']==tuple(frozen['runtime'])
    assert declarations['AUDIT_TIMEOUT_SEC']==120
    assert declarations['OUTPUT_DIRECTORY']==frozen['output_directory']
    assert len(set(expected_inputs))==7
    fp=sha256(b'runner-cache-input-fingerprint-v1\0')
    inputs=[];lexical=[]
    for rel in expected_inputs:
        p=Path(rel);assert not p.is_absolute() and '..' not in p.parts and p.as_posix()==rel
        current=PUB
        for piece in p.parts:
            current/=piece;s=current.lstat()
            assert not stat.S_ISLNK(s.st_mode)
            lexical.append([str(current.relative_to(PUB)),s.st_mode,s.st_dev,s.st_ino,s.st_size,s.st_mtime_ns,s.st_ctime_ns])
        raw=(SNAP/rel).read_bytes()
        assert raw==(PUB/rel).read_bytes()
        encoded=rel.encode();fp.update(len(encoded).to_bytes(8,'big'));fp.update(encoded)
        fp.update(len(raw).to_bytes(8,'big'));fp.update(raw)
        inputs.append(dict(path=rel,sha256=sha256(raw).hexdigest(),bytes=len(raw)))
    fingerprint=fp.hexdigest()

    result_path=SNAP/frozen['result'];result=json.loads(result_path.read_text())
    assert result['source_sha256']==digest(SNAP/frozen['runner'])
    assert result['all_assertions_passed'] is True
    assert result['runtime_sha256']=={rel:digest(SNAP/rel) for rel in frozen['runtime']}
    comparisons=[]
    for label,author in [('charge','author42'),('transport','author43')]:
        artifact=next(x for x in result['artifacts'] if x['label']==label)
        fresh_path=SNAP/artifact['path'];raw=fresh_path.read_bytes()
        assert len(raw)==artifact['bytes'] and sha256(raw).hexdigest()==artifact['sha256']
        assert artifact['exit_code']==artifact['stderr_bytes']==0
        assert (SNAP/frozen['output_directory']/(label+'.stderr.txt')).read_bytes()==b''
        old_path=HERE/'sources'/author/'attempt01/RESULT.json'
        assert old_path.read_bytes()==(old_path.parent/'stdout.log').read_bytes()
        old=json.loads(old_path.read_text());fresh=json.loads(raw)
        count,differences=compare(old,fresh)
        assert len(differences)==1
        expected_source=digest(originals_runtime[0 if label=='charge' else 1])
        assert fresh['source_sha256']==expected_source==artifact['runtime_source_sha256']
        if label=='transport':
            assert fresh['personal42_helper_sha256']==digest(SNAP/frozen['runtime'][2])
            summary=dict(sides=[r['L'] for r in fresh['results']],
                         relevant_rows=[len(r['all_relevant_pair_rows']) for r in fresh['results']],
                         matched_paths=[len(r['all_matching_primitive_paths']) for r in fresh['results']],
                         exact_coefficients=[r['exact_initial_target_probability_coefficients_in_delta_squared'] for r in fresh['results']])
        else:
            assert len(fresh['primitive_rows'])==8448 and len(fresh['rows'])==4260
            assert fresh['counts']==dict(primitive_paths=8448,negative_mark_ambiguity_controls=4224,
                edge_marks=852,charge_moment_controls=4260,complex_structure_factor_controls=852)
            assert [r['total_first_birth_rate_in_kappa'] for r in fresh['summaries']]==[48,1920,6480]
            summary=dict(counts=fresh['counts'],summaries=fresh['summaries'],
                         complete_primitive_rows=len(fresh['primitive_rows']),complete_moment_rows=len(fresh['rows']))
        comparisons.append(dict(label=label,exact_nontiming_scalar_leaves=count,
                                only_difference=differences[0],summary=summary,
                                old_sha256=digest(old_path),fresh_sha256=digest(fresh_path)))
    assert len(result['artifacts'])==2
    execution=json.loads((HERE/'sources/external/BIRTH_CHARGE_TRANSPORT_PRIMARY_EXECUTION.json').read_text())
    e=execution['execution'];assert e['runner']==frozen['runner']
    assert e['status']=='ok' and e['exit_code']==0 and e['stderr']==''
    assert e['timeout_sec']==120 and e['elapsed_sec']>0
    assert e['stdout']==result_path.read_text()+'TOTAL_PASS: 1\n'
    runner_sha=digest(SNAP/frozen['runner'])
    expected_cache=('===== runner cache v1 =====\n'
        f"runner: {frozen['runner']}\nrunner_sha256: {runner_sha}\n"
        f"input_fingerprint_sha256: {fingerprint}\ntimeout_sec: {e['timeout_sec']}\n"
        f"exit_code: {e['exit_code']}\nelapsed_sec: {e['elapsed_sec']:.2f}\nstatus: {e['status']}\n"
        f"----- stdout -----\n{e['stdout'][-200000:]}\n----- stderr -----\n{e['stderr'][-50000:]}\n")
    assert (SNAP/frozen['cache']).read_text()==expected_cache
    assert Path(execution['cache'])==PUB/frozen['cache']
    assert fingerprint=='deaba64df4916d8b08e577bb8105a0d9373a6a6fbdd01cc7250ed42c43c12fbd'

    old_graph=json.loads((HERE/'sources/base_citation_graph_manifest.json').read_text())
    graph=json.loads((SNAP/'docs/audit/data/citation_graph_manifest.json').read_text())
    old_ids=set(old_graph['nodes']);new_ids=set(graph['nodes'])
    assert old_ids<=new_ids and all(graph['nodes'][k]==old_graph['nodes'][k] for k in old_ids)
    claim_id=re.search(r'^claim_id: (.+)$',note,re.M).group(1)
    assert new_ids-old_ids=={claim_id}
    front=note.split('---',2)[1]
    deps=re.findall(r'^  - (.+)$',front,re.M)
    assert deps==[Path(p).stem.lower() for p in frozen['parent_paths']]
    links=re.findall(r'\]\(([^()\n]+\.md)\)',note)
    assert sorted(links)==sorted(Path(p).name for p in frozen['parent_paths'])
    dep_hash=sha256('\n'.join(sorted(deps)).encode()).hexdigest()[:12]
    assert graph['nodes'][claim_id]==dict(out_degree=3,deps_hash=dep_hash)
    assert graph['schema_version']==old_graph['schema_version']==1
    assert graph['node_count']==len(graph['nodes'])==old_graph['node_count']+1
    assert graph['edge_count']==sum(v['out_degree'] for v in graph['nodes'].values())==old_graph['edge_count']+3
    graph_result=dict(old_nodes_unchanged=len(old_ids),added_node=claim_id,added_edges=3,
        new_node=graph['nodes'][claim_id],dependencies=deps,old_node_count=old_graph['node_count'],
        new_node_count=graph['node_count'],old_edge_count=old_graph['edge_count'],new_edge_count=graph['edge_count'],
        base_revision=frozen['base_revision'],scope='Exact frozen topology-manifest delta; no graph rebuild or audit verdict')
    root_checks=dict(leaves=[c['exact_nontiming_scalar_leaves'] for c in comparisons]==
                     [c['all_non_timing_leaves_exact'] for c in root['comparisons']],
                     graph=root['old_graph_nodes_unchanged']==len(old_ids) and root['added_nodes']==1 and root['added_edges']==3,
                     cache_status=root['cache_status']=='fresh')
    assert all(root_checks.values())
    check_origins()
    for row in prior['files']:assert observed(Path(row['path']))==row
    return dict(scope='Bounded publication correspondence42+43; no primary/scientific rerun and no historical writer execution',
        verifier_sha256=digest(Path(__file__)),source_origins_checked=len(all_pins),own43_files_unchanged=len(prior['files']),
        complete_embedded_proofs=proof_results,runtime_correspondence=runtime_results,
        complete_fresh_scientific_payload_comparisons=comparisons,
        declared_inputs=inputs,input_fingerprint_sha256=fingerprint,cache_sha256=digest(SNAP/frozen['cache']),
        exact_cache_bytes_reconstructed=True,cache_identity_and_execution_status='fresh',
        primary_external_seconds=e['elapsed_sec'],primary_internal_seconds=result['elapsed_seconds'],
        publication_result_sha256=digest(result_path),lexical_declared_input_tokens=lexical,
        graph_manifest_delta=graph_result,root_receipt_cross_check=root_checks,
        preserved_root_packaging_failures=root['failed_bookkeeping_attempts'],
        author42_timestamp_scope='Original started_before_utc denotes an end time; copied unchanged.',
        proof_and_limit_judgments='Reported separately in PUBLICATION_COMPARISON.md; no retained verdict inferred.')


if __name__=='__main__':print(json.dumps(main(),indent=2))

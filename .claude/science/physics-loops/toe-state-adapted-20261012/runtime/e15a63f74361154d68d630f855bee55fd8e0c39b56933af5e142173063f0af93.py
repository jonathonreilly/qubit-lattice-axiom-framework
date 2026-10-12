from pathlib import Path
import datetime as dt
import difflib
import hashlib
import json
import math

S = Path(__file__).resolve().parent
D = S/'state_adapted_refinement'
R = S/'state_adapted_author_root_verification_v2'
R.mkdir(exist_ok=False)
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
js = lambda p: json.loads(Path(p).read_bytes())
assert sha(D/'final_manifest.json') == '8c670592a1dc131492ed0b464c6da23d1cf3da5b51d8ed6855687193af8d783e'
final = js(D/'final_manifest.json')
assert len(final['files']) == 83
for path, digest in final['files'].items():
    assert sha(path) == digest
note = S/'STATE_ADAPTED_REFINEMENT_PROBE.md'
core = D/'frozen/STATE_ADAPTED_REFINEMENT_PROBE.md'
assert sha(note) == '459868fcd7f80fa3063c9e7f7a6d62df393eb80f2edc72b221ecda533ba2a971'
assert sha(core) == '49cb5895c5d4b6b88256d5a7bdca471a0fd4c59d1a6c585b733007235a7a7f68'
assert note.read_bytes().startswith(core.read_bytes())
assert ''.join(difflib.unified_diff(core.read_text().splitlines(True),note.read_text().splitlines(True),fromfile='frozen/STATE_ADAPTED_REFINEMENT_PROBE.md',tofile='STATE_ADAPTED_REFINEMENT_PROBE.md')) == (D/'FINAL_APPENDIX.diff').read_text()
parents = js(D/'source_inventory.json')['parents']
assert len(parents) == 6
for row in parents:
    assert sha(row['source']) == row['sha256'] == sha(row['copy'])
anchors = {'execution_manifest.json':'fe78eeddf054677041919bddb3b77dcf3c8d8c7d59d6ef0ee669a48872c22ccf','half_angle_manifest.json':'0c382c55a8c30b1e273404432e504ad38889a3bda71b9e2e88eecc2f9b1f3de5'}
for name, rows in js(D/'EXECUTED_INPUT_RECOVERY.json').items():
    assert sha(D/name) == anchors[name]
    manifest = js(D/name)['files']
    assert len(rows) == len(manifest)
    assert {r['original']:r['sha256'] for r in rows} == manifest
    for row in rows:
        assert sha(row['recovery']) == row['sha256']
    expected = dict(manifest)
    old = expected.pop(str(note))
    expected[str(core)] = old
    reproduced = D/('reproduction_manifest.json' if name == 'execution_manifest.json' else 'half_angle_reproduction_manifest.json')
    assert js(reproduced)['files'] == expected
    for path,digest in expected.items():
        assert sha(path) == digest
jobs = {'baseline':(85,1),'wrong_frame_sign':(69,17),'omit_continuum_unrotation':(84,2),'half_angle':(2,0)}
allrows, receipts, counts = [], [], {}
for job, expected_counts in jobs.items():
    name = 'half_angle_manifest.json' if job == 'half_angle' else 'execution_manifest.json'
    manifest = js(D/name)
    for layer, limit in [('inner',60),('outer',70)]:
        path = D/'runs'/f'{job}_{layer}.receipt.json'
        r = js(path)
        assert r['expected_manifest_sha256'] == r['actual_manifest_sha256'] == anchors[name]
        assert r['source_before'] == r['source_after'] == manifest['files']
        assert r['source_unchanged'] and not r['timeout'] and r['timeout_seconds'] == limit
        assert r['returncode'] == int(bool(expected_counts[1])) and 0 <= r['elapsed_seconds'] < limit
        for stream in ['stdout','stderr']:
            assert sha(r[stream]) == r[stream+'_sha256']
        assert not Path(r['stderr']).read_bytes()
        receipts.append({k:v for k,v in r.items() if k not in ['source_before','source_after']})
    path = D/'runs'/f'{job}_inner.stdout.txt'
    rows, summaries = [], []
    for line, text in enumerate(path.read_text().splitlines(),1):
        if not text.startswith('{'):
            continue
        row = json.loads(text)
        if 'name' in row:
            assert type(row['passed']) is bool
            if 'value' in row:
                assert math.isfinite(row['value'])
                expected = row['value'] < row['tolerance'] if 'tolerance' in row else row['value'] > row['threshold']
                assert row['passed'] == expected
            elif 'minimum' in row:
                assert row['passed'] == (row['minimum'] >= 2-2e-10 and row['maximum'] <= 4+2e-10)
            elif 'squared_error_cutoff' in row:
                x=row['squared_error_cutoff'];tail=row['squared_tail_bound']
                assert row['passed'] == (-2e-10 <= x <= 4+2e-10)
                assert tail == 16/(math.pi*row['cutoff'])
                assert abs(row['norm_upper_diagnostic']**2-(max(x,0)+tail)) < 1e-14
            elif 'norm_upper_diagnostic' in row:
                assert row['passed'] == (row['norm_upper_diagnostic'] < row['threshold'])
            rows.append(row)
            allrows.append({'job':job,'raw_path':str(path),'raw_line':line,**row})
        elif row.get('summary'):
            summaries.append(row)
    assert len(set(row['name'] for row in rows)) == len(rows)
    actual = (sum(row['passed'] for row in rows),sum(not row['passed'] for row in rows))
    assert actual == expected_counts and len(summaries) == 1
    summary = summaries[0]
    assert summary['total'] == len(rows) and summary['passed'] == actual[0] and summary['failed'] == actual[1]
    counts[job] = {'passed':actual[0],'failed':actual[1]}
assert allrows == js(D/'row_inventory.json') and len(allrows) == 260
for stem, change in [('wrong_frame_sign',('FRAME_SIGN = -1','FRAME_SIGN = +1')),('omit_continuum_unrotation',('CONTINUUM_UNROTATE = True','CONTINUUM_UNROTATE = False'))]:
    source=(D/'candidate.py').read_text(); variant=(D/'variants'/f'{stem}.py').read_text()
    assert source.count(change[0]) == 1 and source.replace(*change,1) == variant
    diff=''.join(difflib.unified_diff(source.splitlines(True),variant.splitlines(True),fromfile='candidate.py',tofile=stem+'.py'))
    assert diff == (D/'variants'/f'{stem}.py.diff').read_text()
(R/'verified_receipts.json').write_text(json.dumps(receipts,indent=2)+'\n')
result={'utc':dt.datetime.now(dt.timezone.utc).isoformat(),'status':'stored_author_evidence_checked','source_files':83,'parent_pins':6,'complete_receipts':8,'complete_rows':260,'counts':counts,'science_rerun':False,'independent_check':False,'root_full_proof_helpers_appendix_and_all_raw_rows_read':True,'limitations':['original symbolic false rows preserved; exact supplemental check is post-observation','finite rings are diagnostics','finite Fourier quadrature not interval-certified','no boost numerical rerun','same-author evidence is not fresh review'],'pending':['fresh reviewer complete source and evidence integration']}
(R/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

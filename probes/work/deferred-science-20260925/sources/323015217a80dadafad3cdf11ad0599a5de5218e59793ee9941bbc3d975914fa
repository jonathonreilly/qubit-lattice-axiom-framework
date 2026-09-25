#!/usr/bin/env python3
"""Verify a hyperlink-only publication change and supplied rerun bindings."""
from pathlib import Path
import ast
import difflib
import hashlib
import json
import subprocess

OUT = Path(__file__).resolve().parent
BASE = OUT.parent
PUB = BASE / 'birth-coherence-publication'
SNAP = OUT / 'LINK_REPAIR_sources'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    frozen = json.loads((BASE / 'FIFTH_PUBLICATION_FINAL_SOURCES.json').read_text())
    repair = json.loads((BASE / 'FIFTH_CHECKLIST_LINK_REPAIR.json').read_text())
    runner = next(p for p in frozen['source_hashes'] if p.startswith('scripts/'))
    note = next(p for p in frozen['source_hashes'] if p.startswith('docs/'))
    cache_rel = next(p for p in frozen['source_hashes'] if p.startswith('logs/'))
    result_rel = next(p for p in frozen['source_hashes'] if p.startswith('outputs/'))
    tree = ast.parse((PUB / runner).read_text())
    inputs = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                  and any(isinstance(t, ast.Name) and t.id == 'AUDIT_INPUT_PATHS' for t in n.targets))
    sources = {f'external/{name}': BASE / name for name in
               ['FIFTH_PUBLICATION_FINAL_SOURCES.json', 'FIFTH_PUBLICATION_FINAL_CACHE_EXECUTION.json', 'FIFTH_CHECKLIST_LINK_REPAIR.json']}
    sources.update({f'publication/{rel}': PUB / rel for rel in set(frozen['source_hashes']) | set(inputs)})
    pins = {}
    for rel, src in sorted(sources.items()):
        data = src.read_bytes(); actual = sha(src)
        if rel.removeprefix('publication/') in frozen['source_hashes']:
            assert actual == frozen['source_hashes'][rel.removeprefix('publication/')]
        dest = SNAP / rel; dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists(): assert dest.read_bytes() == data
        else: dest.write_bytes(data); dest.chmod(0o444)
        pins[rel] = {'original': str(src), 'snapshot': str(dest), 'sha256': actual, 'bytes': len(data)}
    (OUT / 'LINK_REPAIR_SOURCE_PINS.json').write_text(json.dumps(pins, indent=2) + '\n')
    old_pub = OUT / 'PUBLICATION_sources/publication'
    old_note = (old_pub / note).read_text(); new_note = (PUB / note).read_text()
    assert sha(old_pub / note) == repair['previous_note_sha256']
    assert sha(PUB / note) == repair['new_note_sha256']
    assert old_note.count(repair['old_link']) == 1
    assert new_note == old_note.replace(repair['old_link'], repair['new_link'])
    delta = ''.join(difflib.unified_diff(old_note.splitlines(True), new_note.splitlines(True),
                                       fromfile='previous frozen note', tofile='final link-repaired note'))
    (OUT / 'LINK_REPAIR_NOTE_DIFF.patch').write_text(delta)
    unchanged = []
    for rel in list(frozen['source_hashes']) + list(inputs):
        if rel == note or rel.startswith(('outputs/', 'logs/')): continue
        assert (PUB / rel).read_bytes() == (old_pub / rel).read_bytes()
        if rel not in unchanged: unchanged.append(rel)
    branch = subprocess.check_output(['git', 'branch', '--show-current'], cwd=PUB, text=True).strip()
    remote = subprocess.check_output(['git', 'remote', 'get-url', 'origin'], cwd=PUB, text=True).strip()
    checklist = next(p for p in frozen['source_hashes'] if p.endswith('NO_GO_DISCIPLINE_CHECKLIST.md'))
    assert repair['new_link'] == remote.removesuffix('.git') + '/blob/' + branch + '/' + checklist
    execution = json.loads((BASE / 'FIFTH_PUBLICATION_FINAL_CACHE_EXECUTION.json').read_text())['result']
    assert execution['runner'] == runner and execution['status'] == 'ok' and execution['exit_code'] == 0
    assert execution['timeout_sec'] == 180 and execution['stderr'] == ''
    digest = hashlib.sha256(b'runner-cache-input-fingerprint-v1\0'); input_rows = []
    for rel in inputs:
        label = rel.encode(); body = (PUB / rel).read_bytes()
        digest.update(len(label).to_bytes(8, 'big')); digest.update(label)
        digest.update(len(body).to_bytes(8, 'big')); digest.update(body)
        input_rows.append({'path': rel, 'bytes': len(body), 'sha256': sha(PUB / rel)})
    fp = digest.hexdigest()
    expected_cache = ('===== runner cache v1 =====\n'
                      f'runner: {runner}\nrunner_sha256: {sha(PUB / runner)}\n'
                      f'input_fingerprint_sha256: {fp}\ntimeout_sec: 180\nexit_code: 0\n'
                      f'elapsed_sec: {execution["elapsed_sec"]:.2f}\nstatus: ok\n'
                      f'----- stdout -----\n{execution["stdout"][-200000:]}\n----- stderr -----\n\n')
    assert (PUB / cache_rel).read_bytes() == expected_cache.encode()
    old_result = json.loads((old_pub / result_rel).read_text())
    new_result = json.loads((PUB / result_rel).read_text())
    def drop_times(x):
        if isinstance(x, dict): return {k: drop_times(v) for k, v in x.items() if k != 'elapsed_seconds'}
        if isinstance(x, list): return [drop_times(v) for v in x]
        return x
    assert drop_times(old_result) == drop_times(new_result)
    decoder = json.JSONDecoder(); text = execution['stdout']; pos = 0; objects = []
    for _ in range(4):
        while text[pos].isspace(): pos += 1
        obj, pos = decoder.raw_decode(text, pos); objects.append(obj)
    assert objects[-1] == new_result and objects[:3] == new_result['actual_cube']['rows']
    old_execution = json.loads((OUT / 'PUBLICATION_sources/external/FIFTH_PUBLICATION_CACHE_EXECUTION.json').read_text())['result']
    assert text[pos:].strip() == old_execution['stdout'][old_execution['stdout'].index('per_element:'):].strip()
    assert new_result['source_sha256'] == sha(PUB / runner)
    seals = [('PRE_SEAL.json', 'df11a67f0f37956e98c407a5b50de3e670b939cf2274d2d798c27cc91e98fdc2'),
             ('POST_SEAL.json', '0094217873a5501e321a3cda4d82fa60cf26b391cee69c7ff8bb8b2ca10a6762'),
             ('PUBLICATION_COMPARISON_SEAL.json', '8ceaf41f560e60897aa3633d47d04ae71f152ceb36063cde9c536a89e6f86a8c')]
    counts = {}
    for name, expected in seals:
        assert sha(OUT / name) == expected
        entries = json.loads((OUT / name).read_text())['files_sha256']
        for rel, wanted in entries.items(): assert sha(OUT / rel) == wanted
        counts[name] = len(entries)
    for name in ['FIFTH_PUBLICATION_FROZEN_SOURCES.json', 'FIFTH_PUBLICATION_CACHE_EXECUTION.json']:
        assert (BASE / name).read_bytes() == (OUT / 'PUBLICATION_sources/external' / name).read_bytes()
    result = {'script_sha256': sha(Path(__file__)), 'one_exact_link_substitution_only': True,
              'branch': branch, 'origin': remote, 'new_link_matches_branch_and_checklist_path': True,
              'unchanged_source_files': unchanged, 'new_note_sha256': sha(PUB / note),
              'runner_sha256': sha(PUB / runner), 'declared_inputs': input_rows, 'fingerprint': fp,
              'cache_sha256': sha(PUB / cache_rel), 'exact_cache_bytes_match_supplied_execution': True,
              'execution_seconds': execution['elapsed_sec'], 'execution_exit': execution['exit_code'],
              'scientific_outputs_identical_except_elapsed_seconds': True,
              'complete_output_JSON_and_resolution_lines_match': True,
              'earlier_immutable_members_revalidated': counts,
              'original_frozen_manifest_and_execution_unchanged': True,
              'new_snapshots': len(pins),
              'scope': 'Evidence-binding addendum only; no scientific runner executed, no gate relaxation or audit verdict.'}
    (OUT / 'LINK_REPAIR_CHECK_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__': main()

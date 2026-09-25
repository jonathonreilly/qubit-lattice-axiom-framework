"""New publication-comparison source capture; writes only this new subpacket."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import os
import subprocess

HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent
EXT = PREVIOUS.parent
PUB = EXT / 'local-charge-observation-publication'
FROZEN = EXT / 'LOCAL_CHARGE_OBSERVATION_FROZEN_SOURCES.json'
EXPECTED_FREEZE = 'ab6385c5cde92eef0512a455934dc90600ac711dbb2e613c43b198a43848005d'


def identity(path):
    s = path.stat()
    return dict(sha256=sha256(path.read_bytes()).hexdigest(), bytes=s.st_size,
                mode=s.st_mode, dev=s.st_dev, ino=s.st_ino, mtime_ns=s.st_mtime_ns,
                ctime_ns=s.st_ctime_ns, nlink=s.st_nlink)


def write(name, data):
    with (HERE / name).open('x') as out:
        out.write(json.dumps(data, indent=2) + '\n')


def main():
    assert identity(FROZEN)['sha256'] == EXPECTED_FREEZE
    frozen = json.loads(FROZEN.read_text())
    previous = [dict(path=str(p), **identity(p)) for p in sorted(PREVIOUS.rglob('*'))
                if p.is_file() and HERE not in p.parents]
    assert len(previous) == 85
    for seal_name, count in [('PRE_SEAL.json', 39), ('POST_SEAL.json', 42)]:
        seal = json.loads((PREVIOUS / seal_name).read_text())
        assert len(seal['members']) == count
        for row in seal['members']:
            now = identity(PREVIOUS / row['path'])
            assert now['sha256'] == row['sha256'] and now['bytes'] == row['bytes']
    write('PRIOR_PRESERVATION_BEFORE.json', {'at_utc': datetime.now(timezone.utc).isoformat(), 'files': previous})
    sources = []

    def add(origin, snapshot, role, expected=None):
        before = identity(origin)
        if expected is not None:
            assert before['sha256'] == expected, str(origin)
        destination = HERE / 'sources' / snapshot
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open('xb') as stream:
            stream.write(origin.read_bytes())
        assert identity(origin) == before
        assert identity(destination)['sha256'] == before['sha256']
        sources.append(dict(origin=str(origin), snapshot=str(destination.relative_to(HERE)), role=role, **before))

    add(FROZEN, 'external/' + FROZEN.name, 'Authoritative frozen manifest', EXPECTED_FREEZE)
    for rel, expected in frozen['files_sha256'].items():
        add(PUB / rel, 'publication/' + rel, 'Exact frozen publication file', expected)
    for rel in ('scripts/runner_cache.py', 'docs/audit/scripts/write_citation_graph_manifest.py',
                'AGENTS.md', 'docs/ai_methodology/SCIENCE_WORKFLOW.md'):
        add(PUB / rel, 'publication/' + rel, 'Read-only mechanical helper or unchanged instructions')
    external = ['LOCAL_CHARGE_OBSERVATION_PUBLICATION_WORKING_SOURCES.json',
                'LOCAL_CHARGE_OBSERVATION_PRIMARY_EXECUTION.json',
                'LOCAL_CHARGE_OBSERVATION_PRIMARY_ROOT_VERIFICATION.json',
                'LOCAL_CHARGE_OBSERVATION_GRAPH_BUILD.stdout.txt',
                'LOCAL_CHARGE_OBSERVATION_GRAPH_BUILD.stderr.txt',
                'build_local_charge_observation_publication.py',
                'verify_local_charge_observation_publication.py',
                'local-charge-observation-publication-history/PREMATURE_GRAPH_DEPENDENCY_FAILURE.json',
                'local-charge-observation-publication-history/verify_publication_attempt01.py']
    for rel in external:
        add(EXT / rel, 'external/' + rel, 'Released build/execution/provenance evidence; no writer execution')
    for directory, note, program in [
        ('native-charge-current-noise-personal', 'CHARGE_CURRENT_AND_INITIAL_COVARIANCE_ROOT.md', 'current_noise_controls.py'),
        ('native-charge-finite-time-personal', 'LOCAL_CHARGE_FINITE_TIME_COVARIANCE_ROOT.md', 'local_support_controls.py')]:
        seal = json.loads((EXT / directory / 'AUTHOR_SEAL.json').read_text())
        hashes = {r['path']: r['sha256'] for r in seal['members']}
        for rel in ('AUTHOR_SEAL.json', note, program, 'attempt01/EXECUTION.json', 'attempt01/stdout.json', 'attempt01/stderr.txt'):
            add(EXT / directory / rel, directory + '/' + rel,
                'Author baseline for source/output correspondence; no execution', hashes.get(rel))
    directory = 'native-charge-current-noise-qualified'
    for name in ('CHARGE_CURRENT_AND_INITIAL_COVARIANCE_QUALIFIED.md', 'QUALIFICATION.md',
                 'QUALIFICATION_SEAL.json', 'WORDING_ONLY.diff'):
        add(EXT / directory / name, directory + '/' + name, 'Released Part I wording-only qualification; no checker packet followed')
    assert len(sources) == 44

    git_receipts = []
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')

    def git(*args):
        run = subprocess.run(['git', *args], cwd=PUB, env=env, capture_output=True)
        git_receipts.append(dict(command=['git', *args], exit_code=run.returncode,
                                 stdout=run.stdout.decode(), stderr=run.stderr.decode()))
        assert run.returncode == 0, git_receipts[-1]
        return run.stdout

    assert git('rev-parse', '--verify', 'HEAD').decode().strip() == frozen['base_revision']
    assert git('branch', '--show-current').decode().strip() == frozen['branch']
    git('rev-parse', '--verify', frozen['base_branch'])
    git('merge-base', '--is-ancestor', frozen['base_revision'], frozen['base_branch'])
    git('status', '--porcelain=v1', '--untracked-files=all')
    git('diff', '--name-status', frozen['base_revision'])
    graph_rel = 'docs/audit/data/citation_graph_manifest.json'
    base_graph = git('show', frozen['base_revision'] + ':' + graph_rel)
    base_path = HERE / 'sources/base_citation_graph_manifest.json'
    with base_path.open('xb') as stream:
        stream.write(base_graph)
    # Do not repeat the large graph body in a command log; bind its full saved bytes.
    git_receipts[-1]['stdout'] = {'snapshot': str(base_path.relative_to(HERE)),
                                  'sha256': sha256(base_graph).hexdigest(), 'bytes': len(base_graph)}
    parent_git = []
    for rel in [*frozen['parent_paths'], 'scripts/runner_cache.py',
                'docs/audit/scripts/write_citation_graph_manifest.py', 'AGENTS.md',
                'docs/ai_methodology/SCIENCE_WORKFLOW.md']:
        raw = git('show', frozen['base_revision'] + ':' + rel)
        h = sha256(raw).hexdigest()
        assert h == identity(PUB / rel)['sha256']
        git_receipts[-1]['stdout'] = {'sha256': h, 'bytes': len(raw), 'same_as_live_path': rel}
        parent_git.append(dict(revision=frozen['base_revision'], path=rel, sha256=h, bytes=len(raw)))
    write('GIT_SOURCE_EVIDENCE.json', {'commands': git_receipts, 'base_parent_and_helper_identities': parent_git})
    for row in previous:
        assert identity(Path(row['path'])) == {k: v for k, v in row.items() if k != 'path'}
    for row in sources:
        assert identity(Path(row['origin'])) == {k: row[k] for k in identity(Path(row['origin']))}
    write('SOURCE_PINS.json', {'at_utc': datetime.now(timezone.utc).isoformat(),
                              'frozen_manifest_sha256': EXPECTED_FREEZE, 'sources': sources,
                              'base_graph': {'revision': frozen['base_revision'], 'path': graph_rel,
                                             'snapshot': str(base_path.relative_to(HERE)),
                                             'sha256': sha256(base_graph).hexdigest(), 'bytes': len(base_graph)},
                              'protected_prior_files': 85, 'author_programs_executed': [],
                              'exposure': 'Full canonical note/wrapper and source metadata. Scientific scope Part II and branch-compression joins; Part I control payload correspondence only. No other checker packet or checkpoint.',
                              'interruption': 'Root reported interruption about 10:45 UTC; last tool call had completed. At 10:47:54 UTC the new subdirectory was absent and all 14 frozen hashes reverified. No partial execution or comparison files existed.'})
    print(json.dumps({'origins': len(sources), 'frozen_files': len(frozen['files_sha256']),
                      'protected_prior_files': len(previous), 'base_revision': frozen['base_revision'],
                      'branch': frozen['branch'], 'forbidden_execution': False}, indent=2))


if __name__ == '__main__':
    main()

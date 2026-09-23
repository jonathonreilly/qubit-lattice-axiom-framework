#!/usr/bin/env python3
"""Mechanical archive/check-out helpers. No scientific verdict or landing authority."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import fcntl
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import uuid


class Invalid(Exception):
    pass


def require(value, message):
    if not value:
        raise Invalid(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(repo, *args, binary=False):
    return subprocess.check_output(['git', '-C', str(repo), *args],
                                   text=not binary).strip() if not binary else subprocess.check_output(['git', '-C', str(repo), *args])


def plain(path):
    path = Path(path).absolute()
    require('..' not in path.parts, f'parent traversal: {path}')
    require(not any(p.is_symlink() for p in (path, *path.parents)), f'symlink: {path}')
    return path


def relative(path):
    p = Path(path)
    require(not p.is_absolute() and '..' not in p.parts and str(p) not in ('', '.'), f'not relative: {path}')
    return p


def save(path, value):
    path = Path(path)
    fd, name = tempfile.mkstemp(prefix=path.name+'.', dir=path.parent)
    with os.fdopen(fd, 'w') as out:
        json.dump(value, out, indent=2, sort_keys=True)
        out.write('\n')
    os.replace(name, path)


def archive(repo, revision, prefix, destination, keep, namespace):
    """Store each historical blob once; keep selected live targets as raw files.

    `keep` is an explicit list of paths relative to the frozen prefix. Callers
    must include every current proof/runtime/link target and review all mappings.
    This function never rewrites a consumer or decides what is historical.
    """
    repo = plain(repo)
    prefix = relative(prefix).as_posix().rstrip('/')+'/'
    destination = plain(destination)
    require(re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', namespace), 'invalid namespace')
    keep = {relative(p).as_posix() for p in keep}
    revision = git(repo, 'rev-parse', '--verify', revision+'^{commit}')
    raw = git(repo, 'ls-tree', '-r', '-z', revision, '--', prefix, binary=True)
    entries = []
    for entry in raw.split(b'\0'):
        if not entry:
            continue
        header, path = entry.split(b'\t', 1)
        mode, kind, blob = header.decode().split()
        path = path.decode()
        require(path.startswith(prefix), 'prefix mismatch')
        require(kind == 'blob' and mode in ('100644', '100755'), f'unsupported archive entry: {path}')
        entries.append((path, path[len(prefix):], mode, blob))
    require(entries, 'empty archive')
    require(keep <= {e[1] for e in entries}, 'keep target missing from frozen archive')
    require(not destination.exists(), 'destination exists; verify/reuse its manifest instead of overwriting')
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.review-archive-', dir=destination.parent))
    records, blobs = [], {}
    process = subprocess.Popen(['git', '-C', str(repo), 'cat-file', '--batch'],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        # One cat-file process, one read per unique original blob. No claim of
        # semantic equivalence for different bytes or different caller contexts.
        grouped = {}
        for entry in entries:
            grouped.setdefault(entry[3], []).append(entry)
        for blob, group in grouped.items():
            process.stdin.write((blob+'\n').encode()); process.stdin.flush()
            fields = process.stdout.readline().decode().split()
            require(len(fields) == 3 and fields[0] == blob and fields[1] == 'blob', 'invalid cat-file response')
            data = process.stdout.read(int(fields[2]))
            require(len(data) == int(fields[2]) and process.stdout.read(1) == b'\n', 'truncated blob')
            digest = sha(data)
            packed = gzip.compress(data, mtime=0)
            require(gzip.decompress(packed) == data, 'archive round-trip failed')
            object_name = f'_objects/{digest}.gz'
            for original, short, mode, _ in group:
                if short in keep:
                    suffix = Path(short).suffix
                    stem = Path(short).stem
                    target = f'kept/{namespace}-{stem}-{sha(short.encode())[:16]}{suffix}'
                    payload, encoding = data, 'identity'
                else:
                    target, payload, encoding = object_name, packed, 'gzip'
                output = stage/target
                output.parent.mkdir(parents=True, exist_ok=True)
                if output.exists():
                    require(output.read_bytes() == payload, 'storage collision')
                else:
                    output.write_bytes(payload)
                    if encoding == 'identity':
                        output.chmod(int(mode, 8) & 0o777)
                records.append(dict(original_path=original, original_mode=mode,
                                    git_blob=blob, raw_sha256=digest, raw_bytes=len(data),
                                    stored_path=target, encoding=encoding,
                                    stored_sha256=sha(payload)))
            blobs[blob] = dict(raw_sha256=digest, occurrences=len(group), raw_bytes=len(data))
        process.stdin.close()
        require(process.wait() == 0, 'cat-file failed')
        record = dict(schema_version=1, revision=revision, prefix=prefix,
                      entries=records, unique_blobs=blobs,
                      boundary='Historical payload storage only; original paths/modes and every disposition remain distinct. No review or audit verdict.')
        save(stage/'archive-manifest.json', record)
        (stage/'README.md').write_text(
            '# Historical evidence\n\nThe manifest maps every frozen original path and mode to its exact payload. '
            'Gzip objects decompress to the recorded raw SHA-256. Selected current targets remain plain files; '
            'all consumer updates require review. Original links inside historical copies retain their original layout. '
            'Equal bytes permit one payload read, not reuse of a scientific conclusion across different premises.\n')
        verify_archive(stage)
        os.rename(stage, destination)
        return record
    finally:
        if process.poll() is None:
            process.terminate(); process.wait()
        process.stdin.close()
        process.stdout.close()
        if stage.exists():
            shutil.rmtree(stage)


def verify_archive(directory, expected_manifest=None):
    directory = plain(directory)
    manifest = plain(directory/'archive-manifest.json').read_bytes()
    if expected_manifest is not None:
        require(sha(manifest) == expected_manifest, 'archive manifest changed')
    record = json.loads(manifest)
    require(record.get('schema_version') == 1, 'unknown archive schema')
    originals = set()
    checked = {}
    for row in record['entries']:
        relative(row['original_path'])
        require(row['original_path'].startswith(record['prefix']), 'original outside frozen prefix')
        require(row['original_mode'] in ('100644', '100755'), 'invalid original mode')
        require(row['original_path'] not in originals, 'duplicate original mapping')
        originals.add(row['original_path'])
        name = relative(row['stored_path'])
        path = plain(directory/name)
        require(path.is_file(), f'missing stored object: {name}')
        identity = (str(name), row['stored_sha256'], row['encoding'])
        if identity not in checked:
            data = path.read_bytes()
            require(sha(data) == row['stored_sha256'], f'changed stored object: {name}')
            require(row['encoding'] in ('identity', 'gzip'), 'unknown encoding')
            raw = gzip.decompress(data) if row['encoding'] == 'gzip' else data
            header = ('blob '+str(len(raw))+'\0').encode()
            checked[identity] = (sha(raw), len(raw), hashlib.sha1(header+raw).hexdigest(), sha(header+raw))
        require(checked[identity][:2] == (row['raw_sha256'], row['raw_bytes']), f'changed decoded object: {name}')
        require(row['git_blob'] in checked[identity][2:], f'original Git blob mismatch: {name}')
        if row['encoding'] == 'identity':
            require(path.stat().st_mode & 0o777 == int(row['original_mode'], 8) & 0o777, 'kept mode changed')
    require(originals, 'empty archive manifest')
    mapped = {row['stored_path'] for row in record['entries']} | {'archive-manifest.json', 'README.md'}
    actual = {p.relative_to(directory).as_posix() for p in directory.rglob('*') if p.is_file() or p.is_symlink()}
    require(actual == mapped, 'unmapped or missing archive files')
    return dict(mechanical_check='passed', manifest_sha256=sha(manifest), original_paths=len(originals), stored_objects=len(checked))


@contextmanager
def pool_lock(pool):
    pool = plain(pool); pool.mkdir(parents=True, exist_ok=True)
    with open(plain(pool/'.lock'), 'a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield pool


def fully_clean(path):
    # Include ignored files: old hidden inputs and failed-run evidence must not
    # leak into another unit. PYTHONDONTWRITEBYTECODE=1 avoids needless caches.
    return not git(path, 'status', '--porcelain', '--untracked-files=all', '--ignored')


def idle_git_state(path):
    require(subprocess.run(['git', '-C', str(path), 'symbolic-ref', '-q', 'HEAD'],
                           stdout=subprocess.DEVNULL).returncode == 1, 'checkout must remain detached')
    for name in ('rebase-merge', 'rebase-apply', 'sequencer', 'MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'BISECT_LOG', 'index.lock'):
        require(not Path(git(path, 'rev-parse', '--path-format=absolute', '--git-path', name)).exists(), 'unfinished Git operation: '+name)


def checkout(repo, pool, slot, owner, base=None, release=False, expected_head=None):
    require(re.fullmatch(r'[a-z0-9][a-z0-9-]{0,47}', slot), 'invalid slot')
    require(owner and len(owner) < 200, 'missing owner')
    repo = plain(repo)
    with pool_lock(pool) as pool:
        state_path = plain(pool/(slot+'.json')); path = plain(pool/slot)
        journal_path = plain(pool/'events.jsonl')
        state = json.loads(state_path.read_text()) if state_path.exists() else None
        common = str(Path(git(repo, 'rev-parse', '--path-format=absolute', '--git-common-dir')).resolve())
        if state:
            require(state.get('schema_version') == 1, 'unknown checkout schema')
            require(state['common_git_dir'] == common and state['path'] == str(path), 'foreign checkout')
            require(path.is_dir(), 'registered checkout missing; retain state for recovery')
            require(str(Path(git(path, 'rev-parse', '--path-format=absolute', '--git-common-dir')).resolve()) == common, 'checkout repository changed')
            idle_git_state(path)
        if release:
            require(state and state['owner'] == owner, 'owner mismatch')
            head = git(path, 'rev-parse', 'HEAD')
            require(expected_head == head, 'release head changed')
            require(fully_clean(path), 'dirty checkout retained with ownership for recovery')
            reference = 'refs/review-loop/preserved/'+slot+'-'+uuid.uuid4().hex
            git(repo, 'update-ref', reference, head)
            state.update(owner=None, head=head, preserved_ref=reference)
        else:
            target = git(repo, 'rev-parse', '--verify', base+'^{commit}')
            if state:
                require(state['owner'] is None, 'checkout already owned')
                require(fully_clean(path), 'idle checkout has residue; preserve it')
                require(git(path, 'rev-parse', 'HEAD') == state['head'], 'idle checkout head changed')
                require(git(repo, 'rev-parse', state['preserved_ref']) == state['head'], 'preserved checkout ref changed')
                git(path, 'checkout', '--detach', target)
            else:
                require(not path.exists(), 'unregistered path; inspect rather than reuse')
                git(repo, 'worktree', 'add', '--detach', str(path), target)
                state = dict(schema_version=1, path=str(path), common_git_dir=common)
            state.update(owner=owner, head=target)
        save(state_path, state)
        with open(journal_path, 'a') as journal:
            journal.write(json.dumps(dict(operation='release' if release else 'acquire', **state))+'\n')
        return state


def fetch_head(repo, repository, number, expected):
    require(re.fullmatch(r'[0-9a-f]{40,64}', expected), 'invalid expected SHA')
    require(number > 0, 'invalid PR')
    def view():
        return json.loads(subprocess.check_output(['gh', 'pr', 'view', str(number), '--repo', repository,
                          '--json', 'number,state,headRefOid,headRefName,baseRefName,isDraft'], text=True))
    before = view()
    require(before['state'] == 'OPEN' and before['headRefOid'] == expected, 'PR head changed')
    reference = f'refs/review-loop/fetched/{number}-'+uuid.uuid4().hex
    git(repo, 'fetch', 'origin', f'refs/pull/{number}/head:{reference}')
    require(git(repo, 'rev-parse', reference) == expected, 'fetched head differs')
    after = view()
    require(after == before, 'PR metadata changed during fetch')
    return dict(schema_version=1, metadata=after, fetched_ref=reference, commit=expected,
                boundary='Read-only head freeze; no review or acceptance of this PR.')


def main():
    p = argparse.ArgumentParser(description=__doc__); sub = p.add_subparsers(dest='command', required=True)
    a = sub.add_parser('archive'); a.add_argument('--repo', type=Path, required=True); a.add_argument('--revision', required=True); a.add_argument('--prefix', required=True); a.add_argument('--destination', type=Path, required=True); a.add_argument('--keep', action='append', default=[]); a.add_argument('--namespace', required=True)
    a = sub.add_parser('verify-archive'); a.add_argument('directory', type=Path); a.add_argument('--expected-manifest')
    for name in ('acquire', 'release'):
        a = sub.add_parser(name); a.add_argument('--repo', type=Path, required=True); a.add_argument('--pool', type=Path, required=True); a.add_argument('--slot', required=True); a.add_argument('--owner', required=True)
        a.add_argument('--base', required=name=='acquire'); a.add_argument('--expected-head', required=name=='release')
    a = sub.add_parser('fetch-head'); a.add_argument('--repo', type=Path, required=True); a.add_argument('--repository', required=True); a.add_argument('--number', type=int, required=True); a.add_argument('--expected', required=True)
    args = vars(p.parse_args()); command = args.pop('command')
    try:
        if command == 'archive': result = archive(**args)
        elif command == 'verify-archive': result = verify_archive(**args)
        elif command == 'fetch-head': result = fetch_head(**args)
        else: result = checkout(**args, release=command=='release')
        print(json.dumps(result, indent=2, sort_keys=True))
    except (Invalid, ValueError, OSError, subprocess.CalledProcessError) as error:
        p.exit(2, f'BLOCKED: {error}\n')


if __name__ == '__main__':
    main()

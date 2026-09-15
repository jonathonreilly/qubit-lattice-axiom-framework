from pathlib import Path
p=Path(__file__).with_name('review_receipt.py');s=p.read_text();mark='def evidence(ref):'
func='''def verify_index_bytes(repo, names, message):
    """Compare exact stage-0 bytes in bounded batches; keep no cross-check cache."""
    names = iter(names)
    pending = next(names, None)
    while pending is not None:
        chunk = []
        size = 0
        while pending is not None and len(chunk) < 64:
            length = repo_file(repo, pending).stat().st_size
            if chunk and size + length > 8 * 1024 * 1024:
                break
            chunk.append(pending)
            size += length
            pending = next(names, None)
        queries = b''.join((':' + name).encode() + b'\\0' for name in chunk)
        result = subprocess.run(['git', '-C', str(repo), 'cat-file', '--batch', '-z'],
                                input=queries, capture_output=True)
        require(result.returncode == 0, 'git cat-file failed: ' + result.stderr.decode(errors='replace').strip())
        output = result.stdout
        offset = 0
        for name in chunk:
            end = output.find(b'\\n', offset)
            require(end >= offset, f'missing index blob header: {name}')
            header = output[offset:end]
            match = re.fullmatch(rb'(?:[0-9a-f]{40}|[0-9a-f]{64}) blob ([0-9]+)', header)
            require(match is not None, f'missing or non-blob index entry: {name}')
            start = end + 1
            stop = start + int(match[1])
            require(stop < len(output) and output[stop:stop + 1] == b'\\n',
                    f'truncated index blob: {name}')
            require(output[start:stop] == repo_file(repo, name).read_bytes(), f'{message}: {name}')
            offset = stop + 1
        require(offset == len(output), 'unexpected trailing index batch output')


'''
assert mark in s;s=s.replace(mark,func+mark,1)
old="    for name in bound:\n        require(git(repo, 'show', ':' + name) == repo_file(repo, name).read_bytes(), f'staged/working mismatch: {name}')";assert old in s;s=s.replace(old,"    verify_index_bytes(repo, bound, 'staged/working mismatch')",1)
old="            require(git(repo, 'show', ':' + name) == repo_file(repo, name).read_bytes(), f'index changed during preflight: {name}')";assert old in s;s=s.replace(old,"        verify_index_bytes(repo, bound, 'index changed during preflight')",1)
p.write_text(s);compile(s,str(p),'exec')

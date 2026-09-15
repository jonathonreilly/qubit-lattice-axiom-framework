#!/usr/bin/env python3
"""Read-only identity and source preflight. Never issues a science verdict."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from copy import copy
import hashlib
import importlib
import json
from pathlib import Path
import re
import subprocess
import sys

CATEGORIES = ('runtime', 'helpers', 'parents', 'context', 'tooling')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def require_current_parent(repo, graph, ids, dependency):
    """Permit dated premise aliases only for the registry-selected current source.

    claim_id_from_path deliberately maps historical premise memos to one ID.
    The same registry's current_path selects authority (also used by the
    repository premise-clean guard); ordinary claim duplicates remain errors.
    Registry and exact linked bytes are already receipt-bound and rechecked.
    """
    parent_id = graph.claim_id_from_path(repo / dependency)
    registry_path = graph.AXIOM_PREMISE_NODES_PATH
    registry = read_json(registry_path.read_bytes()) if registry_path.exists() else {}
    nodes = registry.get('nodes', {})
    entry = nodes.get(parent_id)
    if entry is None:
        require(len(ids.get(parent_id, [])) == 1, f'ambiguous parent claim ID: {parent_id}')
        return
    aliases = entry.get('aliased_paths', [])
    require(dependency == entry.get('current_path') and dependency in aliases,
            f'parent is not current registered authority: {dependency}')
    require(sum(dependency in node.get('aliased_paths', []) for node in nodes.values()) == 1,
            f'ambiguous registered authority path: {dependency}')
    candidates = ids.get(parent_id, [])
    require(repo / dependency in candidates and
            all(path.relative_to(repo).as_posix() in aliases for path in candidates),
            f'ambiguous parent claim ID: {parent_id}')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f'duplicate JSON key: {key}')
        result[key] = value
    return result


def read_json(data):
    return json.loads(data, object_pairs_hook=unique_object)


def repo_file(repo, name):
    require(isinstance(name, str) and name and not Path(name).is_absolute(), 'expected repository-relative path')
    require(Path(name).as_posix() == name and '..' not in Path(name).parts, f'invalid path mapping: {name}')
    path = repo / name
    require(path.resolve().is_relative_to(repo), f'path escapes repository: {name}')
    require(path.is_file() and not path.is_symlink(), f'missing or symbolic file: {name}')
    return path


def git(repo, *args):
    result = subprocess.run(['git', '-C', str(repo), *args], capture_output=True)
    require(result.returncode == 0, f'git {args[0]} failed: {result.stderr.decode(errors="replace").strip()}')
    return result.stdout


def evidence(ref):
    path = Path(ref['path'])
    require(path.is_absolute() and path.is_file(), 'evidence path must identify an existing absolute file')
    data = path.read_bytes()
    require(digest(data) == ref['sha256'], f'evidence hash changed: {path}')
    return data


def pointer(value, location):
    require(isinstance(location, str) and location.startswith('/'), 'disposition json_pointer required')
    for token in location[1:].split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        value = value[int(token)] if isinstance(value, list) else value[token]
    return value


def repository_apis(repo):
    # One CLI invocation targets one repository. Never execute runner imports.
    for directory in (repo / 'scripts', repo / 'docs/audit/scripts'):
        sys.path.insert(0, str(directory))
    graph = importlib.import_module('build_citation_graph')
    cache = importlib.import_module('runner_cache')
    packet = importlib.import_module('audit_packet_script_deps')
    require(graph.REPO_ROOT.resolve() == repo and cache.REPO_ROOT.resolve() == repo and packet.REPO_ROOT.resolve() == repo,
            'repository API module collision; use a fresh CLI process')
    return graph, cache, packet



def generation(path):
    """Detect replacement, content changes and absent-to-present transitions."""
    try:
        stat = path.stat()
    except FileNotFoundError:
        return None
    return (stat.st_dev, stat.st_ino, stat.st_size, stat.st_mtime_ns, stat.st_ctime_ns)


@contextmanager
def memoized_discovery(repo, graph, cache, packet):
    """Cache actual parser results for this invocation, then restore every API.

    These APIs read only their source path and test scripts-directory entries.
    Track the directory as well as every parsed path, including missing paths.
    This is an execution optimization, not a persistent discovery authority.
    """
    observed = {repo / 'scripts': generation(repo / 'scripts')}
    originals = []
    statistics = {}

    def observe(path):
        token = generation(path)
        if path in observed:
            require(observed[path] == token, f'discovery input changed during preflight: {path}')
        else:
            observed[path] = token

    def install(module, name, label):
        original = getattr(module, name)
        originals.append((module, name, original))
        values = {}
        counters = statistics[label] = {'hits': 0, 'misses': 0}

        def cached(argument):
            path = Path(argument)
            if not path.is_absolute():
                path = repo / path
            observe(path)
            if path in values:
                counters['hits'] += 1
                return copy(values[path])
            counters['misses'] += 1
            value = original(argument)
            observe(path)
            values[path] = copy(value)
            return copy(value)

        setattr(module, name, cached)

    try:
        install(graph, '_parse_script_imports', 'graph_imports')
        install(packet, 'parse_script_imports', 'packet_imports')
        install(cache, 'declared_input_paths', 'declared_inputs')
        yield statistics, observe
        for path in observed:
            observe(path)
    finally:
        for module, name, original in reversed(originals):
            setattr(module, name, original)


def check(repo, record, require_cache=False):
    require(type(record['schema_version']) is int and record['schema_version'] == 1, 'unknown receipt schema version')
    require(isinstance(record['unit_id'], str) and record['unit_id'].strip(), 'unit_id required')
    source = record['source']
    for name in ('base', 'commit', 'tree'):
        oid = source[name]
        require(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', oid) is not None, f'full {name} object ID required')
        kind = 'tree' if name == 'tree' else 'commit'
        require(git(repo, 'rev-parse', f'{oid}^{{{kind}}}').decode().strip() == oid, f'invalid {name} object')
    require(git(repo, 'rev-parse', 'HEAD').decode().strip() == source['commit'], 'checkout commit changed')
    require(git(repo, 'write-tree').decode().strip() == source['tree'], 'staged tree changed')
    bound = {}
    def bind(rows, category):
        require(isinstance(rows, list), f'{category} must be an explicit list')
        local = set()
        for row in rows:
            name = row['path']
            require(name not in local, f'duplicate {category} path: {name}')
            local.add(name)
            actual = digest(repo_file(repo, name).read_bytes())
            require(actual == row['sha256'], f'input/source hash changed: {name}')
            require(name not in bound or bound[name] == actual, f'conflicting mapping: {name}')
            bound[name] = actual
        return local
    source_paths = bind(source['paths'], 'source')
    require(source_paths, 'source paths required')
    categories = {name: bind(record['inputs'][name], name) for name in CATEGORIES}
    require(not git(repo, 'diff', '--name-only').strip(), 'unstaged tracked changes remain')
    for name in bound:
        require(git(repo, 'show', ':' + name) == repo_file(repo, name).read_bytes(), f'staged/working mismatch: {name}')
    changed = set(git(repo, 'diff', '--name-only', '--no-renames', source['base'], source['tree']).decode().splitlines())
    deleted = set(git(repo, 'diff', '--name-only', '--diff-filter=D', '--no-renames', source['base'], source['tree']).decode().splitlines())
    require(set(source['deleted_paths']) == deleted, 'deleted source path map mismatch')
    require(source_paths == changed - deleted, 'source path map does not cover current-base delta exactly')
    for args in [('diff', '--check'), ('diff', '--cached', '--check'), ('diff', source['base'], '--check')]:
        git(repo, *args)
    require(record['constituents'], 'constituents required')
    for item in record['constituents']:
        require(item['id'], 'constituent id required')
        for key in ('head', 'delta_base'):
            oid = item[key]
            require(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', oid) is not None, f'full constituent {key} required')
            require(git(repo, 'rev-parse', f'{oid}^{{commit}}').decode().strip() == oid, f'invalid constituent {key}')
        ref = item['dispositions']
        rows = pointer(read_json(evidence(ref)), ref['json_pointer'])
        original = set(git(repo, 'diff', '--name-only', '--no-renames', item['delta_base'], item['head']).decode().splitlines())
        require(isinstance(rows, list) and len(rows) == len(original), 'disposition count mismatch')
        require({row['original_path'] for row in rows} == original, 'original disposition path mapping mismatch')
        removed = set(git(repo, 'diff', '--name-only', '--diff-filter=D', '--no-renames', item['delta_base'], item['head']).decode().splitlines())
        for row in rows:
            name = row['original_path']
            endpoint = item['delta_base'] if name in removed else item['head']
            require(digest(git(repo, 'show', endpoint + ':' + name)) == row['original_sha256'], f'original disposition hash mismatch: {name}')
            require(row['disposition'] and row['recovery'], f'disposition/recovery missing: {name}')
            target = row['final_path']
            require('final_sha256' in row, f'final hash field missing: {name}')
            require(target is not None or row['final_sha256'] is None, f'unmapped final hash: {name}')
            if target is not None:
                require(target in bound and row['final_sha256'] == bound[target], f'unbound final disposition: {target}')
    reviewer = record['reviewer']
    require(isinstance(reviewer['session'], str) and reviewer['session'].strip(), 'reviewer session required')
    evidence(reviewer['report'])
    require(isinstance(reviewer['references'], list), 'reviewer references must be explicit')
    for ref in reviewer['references']:
        evidence(ref)
    required_tools = {'docs/audit/scripts/build_citation_graph.py', 'docs/audit/scripts/static_pipeline_checkpoint.py', 'scripts/runner_cache.py', 'scripts/audit_packet_script_deps.py', 'docs/audit/scripts/ledger_io.py'}
    require(required_tools <= categories['tooling'], 'repository preflight API hashes must be bound as tooling inputs')
    for name in ('docs/audit/data/axiom_premise_nodes.json', 'docs/audit/data/doc_authority_registry.json'):
        if (repo / name).exists():
            require(name in bound, f'unbound preflight registry input: {name}')
    graph, cache, packet = repository_apis(repo)
    with memoized_discovery(repo, graph, cache, packet) as (discovery_statistics, observe_discovery):
        ids = {}
        all_notes = graph.discover_notes()
        for path in all_notes:
            observe_discovery(path)
            ids.setdefault(graph.claim_id_from_path(path), []).append(path)
        require(isinstance(record['notes'], list), 'notes must be an explicit list')
        seen = set()
        discovered = []
        for note in record['notes']:
            path = repo_file(repo, note['path'])
            require(note['path'] in bound and note['path'] not in seen, 'unbound/duplicate note')
            seen.add(note['path'])
            cid = graph.claim_id_from_path(path)
            require(cid == note['claim_id'] and len(ids.get(cid, [])) == 1, f'ambiguous/noncanonical claim ID: {cid}')
            body = path.read_text()
            declared = re.findall(r'^claim_id:\s*(\S+)\s*$', body.split('---', 2)[1] if body.startswith('---\n') else '', re.M)
            require(len(declared) <= 1 and note['declared_claim_id'] == (declared[0] if declared else None), f'declared-to-canonical claim ID mapping mismatch: {cid}')
            require(graph.extract_claim_type_hint(body)[1] == note['claim_type'] and note['claim_type'], f'Type extractor mismatch: {cid}')
            primary = graph.extract_runner(body, path.relative_to(repo / 'docs').as_posix())
            require(primary and primary == note['primary_runner'] and primary in bound, f'primary runner mismatch/unbound: {cid}')
            helpers = set(graph.helper_runner_paths_for_claim(cid, primary))
            packet_helpers = {'scripts/' + name + '.py' for name in packet.transitive_helpers(Path(primary).stem)}
            graph_transitive = set(graph.resolve_helper_runner_paths(primary))
            require(packet_helpers == graph_transitive, f'packet/graph helper discovery disagreement: {cid}')
            require(helpers == set(note['helpers']) and helpers <= categories['helpers'], f'undeclared/unbound packet helper: {cid}')
            for target in graph.LINK_RE.findall(body):
                if not re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:|#', target) and target.split('#')[0].endswith('.md'):
                    require(graph.resolve_link_target(target.split('#')[0], path) is not None, f'unresolved source citation: {target}')
            citations = {p.relative_to(repo).as_posix() for p in graph.extract_citations(body, path)}
            require(citations == set(note['citations']) and citations <= bound.keys(), f'citation path/hash mapping mismatch: {cid}')
            deps = set(note['repository_dependencies'])
            require(deps <= citations and deps <= categories['parents'], f'unlinked/unbound repository dependency: {cid}')
            for dependency in deps:
                require_current_parent(repo, graph, ids, dependency)
            require(isinstance(note['dependency_rationale'], str) and note['dependency_rationale'].strip(), 'dependency rationale required, including empty dependency lists')
            for runner in {primary} | helpers:
                require(cache.declared_timeout_for(runner), f'runner timeout missing: {runner}')
                declared_inputs = cache.declared_input_paths(runner)
                require(declared_inputs != (), f'invalid input declaration: {runner}')
                require(set(declared_inputs or ()) <= bound.keys(), f'undeclared receipt input: {runner}')
                require(cache.declared_input_fingerprint(runner) != '', f'unreadable declared input: {runner}')
            if require_cache:
                require(cache.cache_status(primary) == 'fresh', f'cache not fresh: {primary}')
                cache_path = cache.cache_path_for(primary).relative_to(repo).as_posix()
                require(cache_path in bound, f'cache bytes not bound: {cache_path}')
            discovered.append({'path': note['path'], 'claim_id': cid, 'primary_runner': primary, 'helpers': sorted(helpers), 'graph_transitive_helpers': sorted(graph_transitive), 'packet_transitive_helpers': sorted(packet_helpers), 'citations': sorted(citations)})
        # Check inventory closure independently of the caller's selected notes.
        # Historical/non-scientific discovered Markdown needs an explicit reviewer
        # disposition, never an inferred exception based on its directory name.
        exemptions = record['non_science_notes']
        require(isinstance(exemptions, list), 'non_science_notes must be explicit')
        exempt_paths = set()
        for item in exemptions:
            name = item['path']
            require(name in bound and name not in seen and name not in exempt_paths, 'unbound/duplicate non-science disposition')
            require(isinstance(item['rationale'], str) and item['rationale'].strip(), 'non-science rationale required')
            evidence(item['review_reference'])
            exempt_paths.add(name)
        affected = set()
        for path in all_notes:
            name = path.relative_to(repo).as_posix()
            if name in changed:
                affected.add(name)
                continue
            body = path.read_text()
            primary = graph.extract_runner(body, path.relative_to(repo / 'docs').as_posix())
            if primary:
                runners = {primary} | set(graph.helper_runner_paths_for_claim(graph.claim_id_from_path(path), primary))
                runners.update('scripts/' + name + '.py' for name in packet.transitive_helpers(Path(primary).stem))
                runner_inputs = set()
                for runner in runners:
                    runner_inputs.update(cache.declared_input_paths(runner) or ())
                if (runners | runner_inputs) & changed:
                    affected.add(name)
        require(affected <= seen | exempt_paths, 'uncovered changed/runner-affected notes: ' + ', '.join(sorted(affected - seen - exempt_paths)))
        require(exempt_paths <= affected, 'non-science disposition outside affected note closure')
        for name, expected in bound.items():
            require(digest(repo_file(repo, name).read_bytes()) == expected, f'input changed during preflight: {name}')
            require(git(repo, 'show', ':' + name) == repo_file(repo, name).read_bytes(), f'index changed during preflight: {name}')
        require(set(graph.discover_notes()) == set(all_notes), 'discovered note inventory changed during preflight')
        require(not git(repo, 'diff', '--name-only').strip(), 'unstaged tracked changes during preflight')
        require(git(repo, 'write-tree').decode().strip() == source['tree'], 'tree changed during preflight')
        require(git(repo, 'rev-parse', 'HEAD').decode().strip() == source['commit'], 'commit changed during preflight')
        for item in record['constituents']:
            evidence(item['dispositions'])
        evidence(reviewer['report'])
        for item in exemptions:
            evidence(item['review_reference'])
        for ref in reviewer['references']:
            evidence(ref)
        return {'schema_version': 1, 'mechanical_status': 'ok', 'authority': 'mechanical checks only; independent science review and combined integration gate remain separate', 'unit_id': record['unit_id'], 'tree': source['tree'], 'cache_checked': require_cache, 'notes': discovered, 'discovery_cache': discovery_statistics}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', required=True, type=Path)
    parser.add_argument('--record', required=True, type=Path)
    parser.add_argument('--cache', action='store_true', help='also require fresh, hash-bound primary caches')
    args = parser.parse_args()
    try:
        checker_hash = digest(Path(__file__).read_bytes())
        data = args.record.read_bytes()
        result = check(args.repo.resolve(), read_json(data), args.cache)
        require(args.record.read_bytes() == data, 'record changed during preflight')
        result['record_sha256'] = digest(data)
        require(digest(Path(__file__).read_bytes()) == checker_hash, 'checker changed during preflight')
        result['checker_sha256'] = checker_hash
    except (ValueError, KeyError, TypeError, OSError, IndexError, AttributeError) as error:
        print(json.dumps({'schema_version': 1, 'mechanical_status': 'invalid', 'error': str(error)}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

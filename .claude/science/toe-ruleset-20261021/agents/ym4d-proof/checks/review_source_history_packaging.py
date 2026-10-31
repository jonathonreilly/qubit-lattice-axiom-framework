#!/usr/bin/env python3
"""Read-only validation of this bounded review packet, not science certification."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

C = Path(__file__).resolve().parent
L = C.parent
ROOT = L.parents[4]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    checks = {}
    inputs = json.loads((C / 'review_source_history_inputs.json').read_text())
    for item in inputs['author_bound_records_verified']:
        p = ROOT / item['path']
        checks['frozen:' + item['path']] = (
            digest(p) == item['sha256'] and p.stat().st_size == item['bytes']
        )
    for key in ['target', 'author_receipt']:
        item = inputs[key]
        checks[key] = digest(ROOT / item['path']) == item['sha256']
    for item in inputs['consumed_science_inputs']:
        checks['consumed:' + item['path']] = digest(ROOT / item['path']) == item['sha256']
    for item in inputs['current_main_methodology']:
        data = subprocess.check_output(
            ['git', 'show', item['revision'] + ':' + item['path']], cwd=ROOT
        )
        checks['method:' + item['path']] = hashlib.sha256(data).hexdigest() == item['sha256']
    for item in inputs['installed_skills']:
        checks['skill:' + item['path']] = digest(Path(item['path'])) == item['sha256']
    review_files = sorted(C.glob('review_source_history_*')) + [
        L / 'REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md'
    ]
    local_links = []
    external_links = []
    syntax_count = 0
    for p in review_files:
        if not p.is_file():
            continue
        text = p.read_text()
        if p.suffix == '.py':
            compile(text, str(p), 'exec')
            syntax_count += 1
        if p.suffix in ['.py', '.md', '.json']:
            checks['whitespace:' + p.name] = text.endswith('\n') and all(
                line == line.rstrip() for line in text.splitlines()
            )
        if p.suffix == '.json':
            json.loads(text)
            checks['json:' + p.name] = True
        if p.suffix != '.md':
            continue
        text = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
        text = re.sub(r'`[^`]*`', '', text)
        for match in re.finditer(r'(?<!!)\[[^\]]+\]\((<[^>]+>|[^)]+)\)', text):
            target = match.group(1).strip('<>')
            if target.startswith(('https://', 'http://')):
                external_links.append({'document':p.name, 'url':target})
                continue
            target = target.split('#', 1)[0]
            dest = (p.parent / target).resolve()
            local_links.append({'document':p.name, 'target':target, 'exists':dest.is_file()})
    checks['all_local_markdown_links_exist'] = all(x['exists'] for x in local_links)
    counts = {}
    for name in ['geometry', 'identity_cluster', 'su2', 'literature_laplace']:
        stem = 'review_source_history_' + name
        data = json.loads((C / (stem + '_attempt01.json')).read_text())
        checks[stem + ':all_predicates'] = all(v is True for v in data['checks'].values())
        checks[stem + ':all_controls'] = all(v is True for v in data['negative_controls'].values())
        checks[stem + ':snapshot_identical'] = (
            digest(C / (stem + '.py')) == digest(C / (stem + '_attempt01.py'))
        )
        checks[stem + ':stderr_empty'] = (C / (stem + '_attempt01.stderr')).stat().st_size == 0
        counts[name] = {'checks':len(data['checks']), 'controls':len(data['negative_controls'])}
    initial = C / 'review_source_history_criteria_initial.md'
    checks['predeclared_initial_sha'] = digest(initial) == '4057f5366e3a33a03b198dbb711d83dc49975d6484484924205dfc5cccdac223'
    checks['predeclared_criteria_preserved'] = (C / 'review_source_history_criteria.md').read_bytes().startswith(initial.read_bytes())
    output = {
        'schema':'independent-source-history-packaging-v1',
        'checks':checks,
        'scientific_check_counts':counts,
        'python_files_compiled_without_bytecode':syntax_count,
        'local_markdown_links':local_links,
        'external_links_syntactic_inventory_only':external_links,
        'limitations':'No author diagnostic replay, broad PR check, theorem proof or network link re-fetch is performed by this validator.',
    }
    print(json.dumps(output, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())

#!/usr/bin/env python3
"""Document/source bookkeeping only; does not execute mathematical diagnostics."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
LANE = HERE.parent
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
                                  cwd=LANE, text=True).strip())


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


sources = json.loads((HERE / 'realrga_sources.json').read_text())
drift = [r['path'] for r in sources['sources']
         if digest(ROOT / r['path']) != r['sha256']]
links = []
table_rows = []
for p in [LANE / 'REALRGA.md', LANE / 'REALRGA_LOG.md']:
    source = p.read_text()
    for _, target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)', source):
        if '://' not in target:
            links.append({'source': p.name, 'target': target,
                          'exists': (p.parent / target.split('#')[0]).exists()})
    if p.name == 'REALRGA.md':
        for number, line in enumerate(source.splitlines(), 1):
            if (line.startswith('| ') or line.startswith('|---')) and line.endswith('|'):
                table_rows.append({'line': number,
                                   'cells': len(re.findall(r'(?<!\\)\|', line))-1})
untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard',
                                     '--full-name'], cwd=ROOT, text=True).splitlines()
prefix = str(LANE.relative_to(ROOT)) + '/'
unexpected = []
for path in untracked:
    rel = path[len(prefix):] if path.startswith(prefix) else ''
    if not (rel in ['REALRGA.md', 'REALRGA_LOG.md'] or
            rel.startswith('checks/realrga_') or rel.startswith('briefs_q/REALRGA/')):
        unexpected.append(path)
tracked = subprocess.check_output(['git', 'diff', '--name-only'], cwd=ROOT,
                                  text=True).splitlines()
staged = subprocess.check_output(['git', 'diff', '--cached', '--name-only'], cwd=ROOT,
                                 text=True).splitlines()
result = json.loads((HERE / 'realrga_result.json').read_text())
report = {
    'kind': __doc__,
    'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'source_revision': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                             text=True).strip(),
    'note_sha256': digest(LANE / 'REALRGA.md'),
    'source_drift': drift,
    'all_local_links_exist': all(r['exists'] for r in links),
    'local_links': links,
    'all_tables_three_columns': all(r['cells'] == 3 for r in table_rows),
    'table_cell_counts': sorted({r['cells'] for r in table_rows}),
    'tracked_changes': tracked,
    'staged_changes': staged,
    'unexpected_untracked': unexpected,
    'numerical_status': result['status'],
    'mathematical_checks_executed': len(result['checks']),
    'criteria_match_execution': digest(HERE / 'realrga_criteria.md') == result['criteria_sha256'],
    'checker_match_execution': digest(HERE / 'realrga_check.py') == result['script_sha256'],
    'stdout_matches_result': (HERE / 'realrga_stdout.json').read_bytes() ==
                             (HERE / 'realrga_result.json').read_bytes(),
}
assert not drift and not tracked and not staged and not unexpected, report
assert report['all_local_links_exist'] and report['all_tables_three_columns'], report
assert report['criteria_match_execution'] and report['checker_match_execution'], report
assert report['stdout_matches_result'] and report['mathematical_checks_executed'] == 0, report
(HERE / 'realrga_validation.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({k: v for k, v in report.items() if k != 'local_links'}, indent=2))

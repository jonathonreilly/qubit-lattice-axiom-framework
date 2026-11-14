#!/usr/bin/env python3
"""Source identity and file-scope bookkeeping; no numerical physics tests."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import resource
import subprocess
import sys


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


lane = Path(__file__).resolve().parents[1]
root = Path(subprocess.check_output(
    ['git', 'rev-parse', '--show-toplevel'], cwd=lane, text=True).strip())
manifest = json.loads((lane / 'checks/charge_sources.json').read_text())
checks = []
head = subprocess.check_output(['git', 'rev-parse', 'HEAD'],
                               cwd=root, text=True).strip()
local_main = subprocess.check_output(['git', 'rev-parse', 'origin/main'],
                                     cwd=root, text=True).strip()
for name, observed in [('head', head), ('local_main', local_main)]:
    checks.append({'kind': 'source_revision', 'name': name,
                   'expected': manifest[name], 'observed': observed,
                   'ok': observed == manifest[name]})
for row in manifest['sources']:
    path = root / row['path']
    observed = digest(path) if path.is_file() else None
    checks.append({'kind': 'source_identity', 'path': row['path'],
                   'expected': row['sha256'], 'observed': observed,
                   'ok': observed == row['sha256']})

tracked = subprocess.check_output(
    ['git', 'diff', 'HEAD', '--name-only'], cwd=root, text=True).splitlines()
checks.append({'kind': 'tracked_files_unchanged', 'observed': tracked,
               'ok': not tracked})
untracked = subprocess.check_output(
    ['git', 'ls-files', '--others', '--exclude-standard'],
    cwd=root, text=True).splitlines()
prefix = lane.relative_to(root).as_posix() + '/'
def allowed(path):
    if not path.startswith(prefix):
        return False
    rel = path[len(prefix):]
    return (rel in {'CHARGE.md', 'CHARGE_LOG.md'}
            or rel.startswith('checks/charge_')
            or rel in {'briefs_q/CHARGE/AUTHOR.md',
                       'briefs_q/CHARGE/REVIEW.md'})
unexpected = [p for p in untracked if not allowed(p)]
checks.append({'kind': 'untracked_scope', 'unexpected': unexpected,
               'baseline_user_inputs': ['briefs_q/CHARGE/AUTHOR.md',
                                        'briefs_q/CHARGE/REVIEW.md'],
               'ok': not unexpected})

note = lane / 'CHARGE.md'
for target in re.findall(r'\]\(([^)]+)\)', note.read_text()):
    if '://' in target or target.startswith('#'):
        continue
    path = note.parent / target.split('#', 1)[0]
    checks.append({'kind': 'local_link', 'target': target, 'ok': path.exists()})

review = lane / 'checks/charge_review.md'
review_text = review.read_text() if review.is_file() else ''
review_sha_matches = digest(note) in review_text
review_verdict = (review_text.rstrip().splitlines()[-1]
                  if review_text.strip() else 'PENDING')
checks.append({'kind': 'review_exact_candidate_identity',
               'sha256': digest(note), 'ok': review_sha_matches})
checks.append({'kind': 'review_disposition_present',
               'observed': review_verdict,
               'ok': review_verdict in {'VERDICT: LAND', 'VERDICT: HOLD'}})

rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
rss_bytes = rss if sys.platform == 'darwin' else rss * 1024
artifacts = [lane / 'CHARGE.md', lane / 'CHARGE_LOG.md']
artifacts += sorted(p for p in (lane / 'checks').glob('charge_*')
                    if p.is_file() and p.name != 'charge_validation.json')
whitespace = [f'{p.relative_to(root)}:{number}'
              for p in artifacts if p.suffix in {'.md', '.py', '.txt'}
              for number, line in enumerate(p.read_text().splitlines(), 1)
              if line.rstrip() != line]
checks.append({'kind': 'trailing_whitespace', 'observed': whitespace,
               'ok': not whitespace})
result = {
    'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'head': head,
    'kind': 'deterministic bookkeeping only; no scientific PASS is assigned',
    'checks': checks,
    'all_bookkeeping_checks_ok': all(c['ok'] for c in checks),
    'review_verdict': review_verdict,
    'bookkeeping_peak_rss_bytes': rss_bytes,
    'numerical_experiments': 'NOT RUN: mandatory nice priority denied',
    'artifacts': [{'path': str(p.relative_to(root)), 'sha256': digest(p),
                   'bytes': p.stat().st_size} for p in artifacts],
}
(lane / 'checks/charge_validation.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps({'bookkeeping_checks_ok': result['all_bookkeeping_checks_ok'],
                  'check_count': len(checks), 'review': review_verdict,
                  'peak_rss_bytes': rss_bytes,
                  'report': 'checks/charge_validation.json'}))
sys.exit(0 if result['all_bookkeeping_checks_ok'] else 1)

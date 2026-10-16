"""Metadata-only source capture. This is not a scientific runner."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

N = Path('/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023')
W = N.parent / 'correlation_worktree'
O = Path(__file__).resolve().parent

SOURCES = [
    ('author_derivation', N/'bus_memory_recovery_candidate/DERIVATION.md', '054fa44b0c189763bc264457e7e2f91e19e94549f3f95207e903fb384181ffa3', 'Complete current read, sections 1-8; reviewed independently of the prior root schedule.', True),
    ('author_freeze', N/'bus_memory_recovery_candidate/FREEZE.json', 'e30a9cf7396ad1e32ff10405006e1a34d361f529c8144a9989830b4a728d1415', 'Complete current read; all four listed members verified by bytes/hash only where not otherwise read.', True),
    ('author_exposure', N/'bus_memory_recovery_candidate/EXPOSURE.md', '506a43815458201822a151669c036bdecb3ad34605a2887394560e923076caa0', 'Complete current read; reported author exposure, not independent verification of its reading history.', True),
    ('author_manifest', N/'bus_memory_recovery_candidate/SOURCE_MANIFEST.json', '439866a222940a976ffb77c166fac6fce7cd3ff24514ef14ec42995c09c28ab5', 'Complete current read; source identity and reported coverage.', True),
    ('preparation_qualifications', N/'bus_preparation_root_review/FINAL_QUALIFICATIONS.md', '1c94a58239c1bd9d168c837cf961522264a1f2d1705f3897ef541a3c8ced788e', 'Complete read in immediately preceding frozen review reused at unchanged identity; accepted conditional premise.', True),
    ('slew_qualifications', N/'bus_bounded_slew_preparation_root_review/FINAL_QUALIFICATIONS.md', '1c3714faadd94da6cc7789eb3472406ea2a5195b453ad941dbb163bb606ecc25', 'Complete read in immediately preceding frozen review reused at unchanged identity; accepted evolved-memory/error/cap premise.', True),
    ('preparation_derivation', N/'bus_installed_preparation_candidate/DERIVATION.md', '71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29', 'Complete prior same-revision read reused; definitions lines 1-83 and 155-166 refreshed in immediately preceding review. No replay.', True),
    ('prior_root_sketch_review', N/'bus_memory_recovery_exposed_check/REVIEW.md', '5dc3f23e14468b73d4734846ccd78a5a8ec951e73118b7dec74e7bf4009379e4', 'Own earlier frozen review; complete current reread for explicit comparison only. Not new independent evidence for author proof.', True),
    ('prior_root_sketch_review_freeze', N/'bus_memory_recovery_exposed_check/FREEZE.json', 'a6e440713aaf7219621a58d8d2b0620b10ad14bdf1b9376aa27c9e8810588e3a', 'Identity only in this task; prior frozen packet preserved.', False),
    ('root_original_sketch', N/'bus_memory_recovery_root_proposal/PRE_RESULT_SKETCH.md', '43fc957f7c1937091d8755365eb4da550fc171cc02083f0c74d034901a9c3340', 'Complete earlier review read reused for exposure disclosure; no new root review files read.', False),
    ('preparation_acceptance', N/'bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json', '28bef1945c65f807be837286d6e795d888f3d8b9ebb75024ac26ee0084409641', 'Identity refresh only; controlling qualifications above are reused.', False),
    ('slew_acceptance', N/'bus_bounded_slew_preparation_root_review/QUALIFIED_ACCEPTANCE.json', 'b237e6550c7b500ff48cdaa2cd30e50cf4895205a610e8feb677da085bf82473', 'Identity refresh only; controlling qualifications above are reused.', False),
    ('canonical_bus', W/'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md', '1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b', 'Prior unchanged-revision mathematical-body reading reused; current identity check only. No new parent revalidation.', False),
    ('prior_slew_review', N/'bus_bounded_slew_preparation_exposed_check/REVIEW.md', 'a1b9ef4621b2a4a420d86f30c16449273d0a0a4bc46f22d078a4b2884cbda1d1', 'Own earlier review reused through accepted qualifications; current identity check only. Historical executions not replayed.', False),
]

def digest(data):
    return hashlib.sha256(data).hexdigest()

def main():
    dest = O/'sources'
    dest.mkdir(exist_ok=True)
    rows = []
    for key, path, expected, coverage, capture in SOURCES:
        data = path.read_bytes()
        actual = digest(data)
        if actual != expected:
            raise ValueError(f'Identity mismatch: {path}: {actual}')
        row = dict(key=key, source=str(path), bytes=len(data), sha256=actual, coverage=coverage)
        if capture:
            target = dest/(key+path.suffix)
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f'Refusing to overwrite changed capture: {target}')
            target.write_bytes(data)
            row['capture'] = str(target.relative_to(O))
        rows.append(row)
    freeze = json.loads((N/'bus_memory_recovery_candidate/FREEZE.json').read_text())
    members = []
    for member in freeze['members']:
        path = N/'bus_memory_recovery_candidate'/member['path']
        data = path.read_bytes()
        actual = digest(data)
        if len(data) != member['bytes'] or actual != member['sha256']:
            raise ValueError(f'Author freeze member mismatch: {path}')
        members.append(dict(path=member['path'], bytes=len(data), sha256=actual))
    record = dict(created_utc=datetime.now(timezone.utc).isoformat(), kind='metadata-only identity verification and source capture', scientific_executions=0, sources=rows, author_freeze_members_verified=members)
    (O/'SOURCE_IDENTITIES.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(dict(result='identities verified and exact captures saved', source_count=len(rows), captured_count=sum('capture' in row for row in rows), author_freeze_members=len(members), scientific_executions=0)))

if __name__ == '__main__':
    main()

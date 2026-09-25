"""Final hash refresh only; does not import or execute scientific code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    pins = read(HERE / 'PUBLICATION_SOURCE_PINS_INITIAL.json')
    for row in pins['sources']:
        origin = Path(row['origin'])
        assert digest(origin) == row['sha256']
        assert origin.stat().st_size == row['bytes']
        if row['snapshot'] is not None:
            snapshot = HERE / row['snapshot']
            assert digest(snapshot) == row['sha256']
            assert snapshot.stat().st_size == row['bytes']
    instructions = read(HERE / 'SOURCE_PINS.json')['instructions']
    for row in instructions:
        assert digest(Path(row['origin'])) == row['sha256']
        assert digest(HERE / row['snapshot']) == row['sha256']
    seals = [
        ('PRE31', HERE, 'PRE_SEAL.json'),
        ('POST31', HERE, 'POST_SEAL.json'),
        ('PRE32', BASE / 'number-offset-observation-independent', 'PRE_SEAL.json'),
        ('POST32', BASE / 'number-offset-observation-independent', 'POST_SEAL.json'),
        ('POST32_chronology', BASE / 'number-offset-observation-independent',
         'POST_CHRONOLOGY_ADDENDUM_SEAL.json'),
    ]
    verified_seals = []
    for label, directory, name in seals:
        document = read(directory / name)
        for row in document['members']:
            path = directory / row['path']
            assert digest(path) == row['sha256']
            assert path.stat().st_size == row['bytes']
        verified_seals.append({'name': label, 'path': str(directory / name),
                               'sha256': digest(directory / name),
                               'unchanged_members': len(document['members'])})
    for label in ['two-detector-coincidence-personal', 'number-offset-observation-personal']:
        directory = BASE / label
        document = read(directory / 'AUTHOR_SEAL.json')
        for name, row in document['files'].items():
            path = directory / name
            assert digest(path) == row['sha256']
            assert path.stat().st_size == row['bytes']
    public = BASE / 'count-interpretation-publication'
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=public,
                          capture_output=True, text=True, check=True).stdout.strip()
    assert head == '63c82141301f5fe3828b1ed4d385bd9696628e7b'
    status = subprocess.run(['git', 'status', '--short'], cwd=public,
                            capture_output=True, text=True, check=True).stdout
    pins['refreshed_utc'] = datetime.now(timezone.utc).isoformat()
    pins['unchanged_sources_and_snapshots'] = len(pins['sources'])
    pins['unchanged_instruction_origins'] = instructions
    pins['read_coverage'] = {
        'public_argument': 'Full Parts A/B/C and front/end claims',
        'root31': 'Full released argument and controls already read in unchanged own POST; full public diff newly read',
        'root32': 'Full newly released author argument/code, PRE/POST/chronology and all 172 scientific rows read',
        'combined_stdout': 'Expressly authorized; exact whole-byte match with complete result and TOTAL; root31 rows reused by exact identity',
        'earlier_energy_parents': 'Unchanged declared-input hashes only; no new scientific re-certification',
    }
    pins['prior_seals_preserved'] = verified_seals
    pins['publication_base'] = head
    pins['new_scientific_derivation_claim'] = False
    pins['other_active_packet_reads'] = False
    pins['author_or_primary_programs_imported_or_executed'] = 0
    (HERE / 'PUBLICATION_SOURCE_PINS.json').write_text(json.dumps(pins, indent=2) + '\n')
    report = {
        'verified_utc': datetime.now(timezone.utc).isoformat(),
        'source_refresh_sha256': digest(Path(__file__)),
        'source_manifest_sha256': digest(HERE / 'PUBLICATION_SOURCE_PINS.json'),
        'comparison_sha256': digest(HERE / 'PUBLICATION_COMPARISON.md'),
        'read_and_failure_log_sha256': digest(HERE / 'PUBLICATION_READ_AND_FAILURE_LOG.md'),
        'unchanged_scientific_evidence_anchor_origins': len(pins['sources']),
        'unchanged_instruction_origins': len(instructions),
        'prior_seals': verified_seals,
        'author_sealed_members_verified': [8, 8],
        'publication_head': head,
        'publication_status_read_only': status,
        'author_primary_runs_by_checker': 0,
        'scientific_repairs_required_for_pinned_publication': [],
        'limits': 'Released-source correspondence only; no new blind PRE, no applied audit verdict.'
    }
    text = json.dumps(report, indent=2) + '\n'
    (HERE / 'PUBLICATION_FINAL_BINDING_VERIFICATION.json').write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()

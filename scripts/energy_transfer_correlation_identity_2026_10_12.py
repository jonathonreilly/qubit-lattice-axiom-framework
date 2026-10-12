#!/usr/bin/env python3
"""Source bytes and publication reconstruction only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-energy-correlations-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-energy-correlations-20261012/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-energy-correlations-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-energy-correlations-20261012/SOURCE_REVIEW_STATUS.json', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/009043c543e809e4a19483bdc3d2932e61ff92170f1f76428cf8e851e3c48e57.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/0797320a95c5f0757e85b8f9b8c41a6bfbab4a758d4215ae037a1888d14f7284.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/0b6f580c6feacdfc0723dbe8922a7721af8d02efcac06220e3649f83e48ffa41.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/1104de3922002720beecb7eb2bd106b64025aea0afb1e11b8f86750dfb59e30d.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/2274b6e0a045a27d54f2888ce6f7482e466af956a76dbd33a48a630ca258ccf0.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/255d378681114973fb0c2bed0ddcfbcab668a256ff091f801f3d800989250042.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/3992a20d24b6ec932ff110d498fee482fb4f9b172dfd15b0c348e6a4f2245cd3.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/39e801fe02e14a70ef8e729a834eb0508fefa526b1de26ea88ce79b70c92cf5b.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/3c30599a04ee55ed51b3f1d6514b67e3015ab8a2e74d6ce464912944cd65fd73.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/43e18b4aea04768989d2e8a7cf31276653ca471a2af6259f4e47a044a532f80b.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/43f9e668cbe6b0487f78658b509dcd3bab4fe2ef8c1a2dbf21e9675a3ac08dcd.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/4e884446d31b9849bd81e55fa88b6a2bd6291ee86789c89f10a305b363dc221d.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/62792c4e3575d89b0c43b2307ff34c9294baf1e7f83f335f637f7330ca73c72d.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/648e61978fc5b7d7b84ec6ddc7cb4c6d506405827e7aad1fa80f99cf9211d52c.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/8d9d3852b98d3fc069e49a23717e9d01a9534384a1057c3e7e09225a075fc0a5.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/9b7a7a2dda5ce2f578635d51fa070515df052c0cf26b36d82f2bde39a0215d17.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/9e97053e6d5b9f22e061d7ca88ab6df9a55c054bc5785f02123f87714c3d0166.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/a78dea4566d2046c3cf1da57e2cff5e111d46e14bbed00edd01453e50935e610.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/ba2bb16f901d6a30f283bb6ce52b63aac1a96f66fd8ba15d4ec9c7b2485d2941.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/c829beaec0b901af93ee38f95fccd5a690c4092b08d5cb75ff04d57c60c0fbb2.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/d723600190361590cf18f934fd5719439b02fd4854adcbc5bc5f9319c87f5390.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/dc3a429afc045d6bf39564f1ada2c1dddfab056ce3c2ba5ad34f1f13a095d75a.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/e058ef395ffe717d2813a56e384091673eca0406ad2f5f2f7ecd57b2c5048c95.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/e0932643275551a7b67d74cf3d42f5b0cb12bdb690ed24c5967232228b965133.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/f322d9262724208ce26eea6f181e81eefef73cbbf162fdf3eb1af278ec71895b.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/f554bf91ca35673a30ca840c7b358ae8d19407c92a289e454cb43ac720dbcd8d.gz', '.claude/science/physics-loops/toe-energy-correlations-20261012/objects/f7d741217e0103e0db389f5cde6c41214819474fd747f40179bbaee411aa8972.gz', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOW_ENERGY_PHASE_RATE_OPTIMALITY_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-energy-correlations-20261012'
CLAIM = 'energy_transfer_correlation_bounded_theorem_note_2026-10-12'
MAP_SHA = '7bb3c25cc8f0b9a713d70cfc18de15f31a3f516b49655ce7a1b673af7da6be97'
EDITS_SHA = '00390d0e536798214aa13c42c9053d0a59e34fd0e86d4eef7fb94044b960c510'
PARENTS_SHA = '3802ccfcf2d192a45c2fb7bff37f44ec5d1c830f0ae2e35fac631986aab32997'
STATUS_SHA = '71448698b6b01290905cc2ccbf0b5cc37bf2d63a172fe126cf6d5f6f16c2f073'
SYNTHESIS_MANIFEST_SHA = 'd723600190361590cf18f934fd5719439b02fd4854adcbc5bc5f9319c87f5390'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def verify(root):
    reads = []
    def read(name):
        relative = PurePosixPath(name)
        need(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe declared input')
        path = root.joinpath(*relative.parts)
        need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),
             'Declared input missing or outside repository')
        reads.append(name)
        return path.read_bytes()
    raw_map = read(PACKET + '/EVIDENCE_MAP.json')
    need(sha(raw_map) == MAP_SHA, 'Archive map changed')
    objects = json.loads(raw_map)['objects']
    need(len({o['sha256'] for o in objects}) == len(objects) and
         len({o['path'] for o in objects}) == len(objects), 'Duplicate archive object')
    contents, origins = {}, {}
    for obj in objects:
        stored = read(PACKET + '/' + obj['path'])
        need(sha(stored) == obj['stored_sha256'], 'Compressed archive changed')
        data = gzip.decompress(stored)
        need(sha(data) == obj['sha256'] and len(data) == obj['bytes'], 'Archived source changed')
        contents[obj['sha256']] = data
        for origin in obj['origins']:
            need(origin['path'] not in origins, 'Duplicate original alias')
            origins[origin['path']] = obj['sha256']
    manifest = json.loads(contents[SYNTHESIS_MANIFEST_SHA])
    for row in manifest['files']:
        need(origins.get(row['path']) == row['sha256'] and
             len(contents[row['sha256']]) == row['bytes'], 'Frozen synthesis inventory does not reconstruct')
    raw_edits = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(raw_edits) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(raw_edits)['notes']
    need(len(edits) == 2 and {r['key'] for r in edits} == {'correlation', 'phase'}, 'Publication membership differs')
    for row in edits:
        original = contents[row['source_sha256']]
        removed = row['removed_metadata'].encode()
        need(original.startswith(removed) and len(original) == row['source_bytes'], 'Original source differs')
        body = original[len(removed):]
        need(sha(body) == row['body_sha256'] and len(body) == row['body_bytes'] and
             row['mathematical_body_edits'] == [] and row['citation_relocations'] == [],
             'Unchanged mathematical-body contract differs')
        published = read(row['note'])
        need(published == row['header'].encode() + body + row['appendix'].encode() and
             sha(published) == row['published_sha256'], 'Published source does not reconstruct')
    raw_parents = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(raw_parents) == PARENTS_SHA, 'Parent bindings changed')
    parents = json.loads(raw_parents)['parents']
    need(len(parents) == 3, 'Live parent membership differs')
    for row in parents:
        need(sha(read(row['path'])) == row['published_sha256'], 'Canonical parent bytes changed')
    raw_status = read(PACKET + '/SOURCE_REVIEW_STATUS.json')
    need(sha(raw_status) == STATUS_SHA, 'Review scope changed')
    status = json.loads(raw_status)
    need(status['no_go_packet_pass'] is False and status['N1'] == status['N5'] == 'pending',
         'Formal packet status changed')
    need(set(reads) == set(AUDIT_INPUT_PATHS) and len(reads) == len(set(reads)), 'Declared read closure differs')
    return {'result': 'source_identities_and_reconstruction_match', 'claim_id': CLAIM,
        'meaning': 'Integrity only; no mathematical calculation, proof or audit was executed.',
        'mathematical_operations_executed': False, 'mathematical_predicates_executed': 0,
        'scientific_mutations_executed': 0, 'independent_review_supplied_by_tool': False,
        'no_go_packet_pass_supplied_by_tool': False,
        'external_scientific_input_reads': [p['path'] for p in parents],
        'package_local_integrity_reads': sorted(set(reads) - {p['path'] for p in parents})}


def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]), sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no energy, probability or matrix-element inequality was computed.')
    print('per_site: checked and not executed — source integrity only; no spin or ordinary physical-cell correlation was computed.')
    print('per_mode: checked and not executed — source integrity only; no dispersion, phase-rate bound or packet asymptotic was computed.')
    print('per_block: checked and not executed — source integrity only; no CAR word, parity witness or scientific mutation was computed.')
    print('lattice_wide: checked and not executed — source integrity only; no Fock-form, normal-limit or correlation proof was executed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False}), file=sys.stderr)
        raise SystemExit(1)

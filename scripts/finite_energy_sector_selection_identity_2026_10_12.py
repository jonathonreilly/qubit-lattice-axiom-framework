#!/usr/bin/env python3
"""Source identities/reconstruction only; no mathematical predicates or proofs."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-finite-energy-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-finite-energy-20261012/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-finite-energy-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/03e769ea4fa24e3e06298814ad9188f2e69276328be886938ee46d4cff4af225.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/1104de3922002720beecb7eb2bd106b64025aea0afb1e11b8f86750dfb59e30d.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/14c5800674e390b259390417f4c47604e0061ab1040cdee5efb049aaaea9b3ea.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/1e66533611bbb5da2c2d88ad1350b93e9af9613a3c737cf2d9092a8c9d1433c2.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/25e48e92474605ef3c67c6a9c90334bb192bd3a2f385951fca5c76578c783bf1.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/3ac765cd07f6984a1fc39830563d72e3316fa409ccf24395e72aaf10307e8704.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/3b7591ce0d50c8a930fe8bf655491d5f9f8df4d832159ccd4300c9ab7479392e.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/4359b7ab209fb8dceb2587fb973ae0e6e7fc2816180603c305c72caaa015fe70.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/44272ea30d9a012b95719a5ecd03389f88a4088c1d6a8c4cbcdd820aeb197b71.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/50587a7c76b476c5e358873e1ab957923f6b27e7553bfcffec8e50c1c106142f.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/5450b7d602dc63a66c5a4fe1487df68f92839cbf69c9b46dc7c7b2e97f291b0e.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/59cf9e89cf82ea9238644f56a8ca1139e98459a47068274cf8e68087e50394a4.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/62bcb307335cec8e5ad8fde3c9b97fc83e188dc5f33e8208774607a5bb2d086c.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/648e61978fc5b7d7b84ec6ddc7cb4c6d506405827e7aad1fa80f99cf9211d52c.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/6dd065ae1cebc65bca579fe5e1330015afe46920012dc3f79a677356eadbd05c.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/6ed5e5ac2a0de15f0f3b025814502630de9da7b1b32e303ebdc1af227f5b2a7e.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/70c6eea076e39f442d7043d0d2b50a9a7ecadef8920b2fe4df04c161ead46976.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/7d0c75f18fd7715c994c4d1f4b009e80abf02311bd77157ba43cd0bc873fa8ea.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/82d059783d2143fc970b408343364546c06409d80a341d2a6667842a11296b65.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/848732c8688ff3099bc0ae7ad9beddf78665ce35530af8077dee7a680eebcac8.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/952d2615771eb67686da634b4343128ac37ed9700e7a358a6910b238ce1f4f86.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/9a7b1aa114de6e8ee595ac7c7bf873bc2e50cfc383fc26328aa58699041f7330.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/9fd655666ee11d05617ed41b5a7a6285eee496be6993a0f250ae7eebb8beb778.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/ab05958fa919e0d4165581b6b88a18706fd8b45bc72921c372ef33f02b21755c.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/bd82196b02fc9f634313ce2f3e68dfd0b58315679e4bd5a69dc73de89c6a85c6.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/bf105d4689ab6c9551de9e80543d0b4b28be08e5a7f9fea302b4a14d9181ac50.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/c1d01c472f0d5520fa575ea639e096ddd2884d97876e876bacdb3afee934f287.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/c1f4ec238082615307a8c3a0f2aabcf2ff1fa3b228765bbce24332ce25f51ab5.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/f4205553595de8e9f81e3fd49a0617ceafc162d01493b8ac9526c394faa0818f.gz', '.claude/science/physics-loops/toe-finite-energy-20261012/objects/f9909a91e370d3d21772d13cf0707dadbbd999c5fd7fa7ce8b5dbe5dff293f4f.gz', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/FINITE_ENERGY_SECTOR_SELECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-finite-energy-20261012'
NOTE = 'docs/FINITE_ENERGY_SECTOR_SELECTION_BOUNDED_THEOREM_NOTE_2026-10-12.md'
AUTHOR_SHA = '648e61978fc5b7d7b84ec6ddc7cb4c6d506405827e7aad1fa80f99cf9211d52c'
AUTHOR_MANIFEST_SHA = '848732c8688ff3099bc0ae7ad9beddf78665ce35530af8077dee7a680eebcac8'
MAP_SHA = '6e634d36f180a392ec2a17214a521e2702ce14d264c6709702829ca76328d2eb'
EDITS_SHA = 'ad29c40fb277a9360f7374c4cdd5ece425bfe02876c0311bf6b665c72ea7dc0e'
PARENTS_SHA = 'fed7e09aa22cc3ec32879125087f5e16020cf6b509cd311a26d63b6c991d4193'


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
    need(sha(raw_map) == MAP_SHA, 'Archive map identity changed')
    objects = json.loads(raw_map)['objects']
    need(len({o['sha256'] for o in objects}) == len(objects) and
         len({o['path'] for o in objects}) == len(objects), 'Duplicate archive object')
    contents, origins = {}, {}
    for obj in objects:
        stored = read(PACKET + '/' + obj['path'])
        need(sha(stored) == obj['stored_sha256'], 'Stored archive changed')
        data = gzip.decompress(stored)
        need(sha(data) == obj['sha256'] and len(data) == obj['bytes'], 'Archived source changed')
        contents[obj['sha256']] = data
        for origin in obj['origins']:
            need(origin['path'] not in origins, 'Duplicate original path alias')
            origins[origin['path']] = obj['sha256']
    manifest = json.loads(contents[AUTHOR_MANIFEST_SHA])
    need(manifest['source_sha256'] == AUTHOR_SHA, 'Original manifest target changed')
    for row in manifest['files']:
        need(origins.get(row['path']) == row['sha256'] and
             len(contents[row['sha256']]) == row['bytes'], 'Original author manifest does not reconstruct')
    author = contents[AUTHOR_SHA]
    need(author.startswith(b'---\n'), 'Author frontmatter absent')
    end = author.find(b'\n---\n', 4)
    need(end > 0, 'Author frontmatter delimiter absent')
    body = author[end + 5:]
    edits_raw = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(edits_raw) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(edits_raw)
    need(edits['author_sha256'] == AUTHOR_SHA and sha(body) == edits['body_sha256'],
         'Exact scientific body changed')
    need(edits['mathematical_body_edits'] == [] and edits['citation_relocations'] == [],
         'The reviewed byte-exact body contract changed')
    need(read(NOTE) == edits['header'].encode() + body + edits['appendix'].encode(),
         'Publication does not reconstruct exactly')
    parent_raw = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(parent_raw) == PARENTS_SHA, 'Published parent bindings changed')
    parents = json.loads(parent_raw)['parents']
    need(len(parents) == 3, 'Scientific parent scope differs')
    for parent in parents:
        need(sha(read(parent['path'])) == parent['published_sha256'], 'Published parent bytes changed')
    need(set(reads) == set(AUDIT_INPUT_PATHS), 'Declared read closure differs')
    return {'result': 'source_identities_and_reconstruction_match',
        'meaning': 'Integrity result only; mathematical correctness was not executed or established.',
        'mathematical_operations_executed': False,
        'independent_review_supplied_by_tool': False,
        'no_go_packet_pass_supplied_by_tool': False,
        'external_scientific_input_reads': [p['path'] for p in parents],
        'package_local_integrity_reads': sorted(set(reads) - {p['path'] for p in parents})}


def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]), sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no energy, probability or trace-distance calculation was executed.')
    print('per_site: checked and not executed — source integrity only; no spin or local-observable calculation was executed.')
    print('per_mode: checked and not executed — source integrity only; no positive-energy or branch-bound calculation was executed.')
    print('per_block: checked and not executed — source integrity only; no CAR coherence witness or scientific mutation test was executed.')
    print('lattice_wide: checked and not executed — source integrity only; no Fock-form, normal-state or dynamical-correlation proof was executed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False}), file=sys.stderr)
        raise SystemExit(1)

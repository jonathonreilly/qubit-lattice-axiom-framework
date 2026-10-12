#!/usr/bin/env python3
"""Source bytes and publication reconstruction only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-response-transfer-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-response-transfer-20261012/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-response-transfer-20261012/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-response-transfer-20261012/SOURCE_REVIEW_STATUS.json', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/04eef4960b18d6b0e4a7f81852ddceea7fc081c855360bf613aaf9124e141984.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/10c2bdb8e6e2ee65c0f85184cabc01f101f77b5b8ad1dcd3825e212fa9a9b185.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/12d36831f50b13518d6720cb52b3099366e21835a342d60f0341476aba7b92f2.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/172be2f4301d6f32edbf4f0bf55fdfb9e045098253c6a5b475fc4446816c6666.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/189654ab08f375859dce77254cf647ec2c5143f247b8f2b841531c73dbebbaee.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/19d1c72220146f2e271465083260f97f4d363fcf7fc5f6bf6be12115554a761a.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/221c6057b4bdadd013f91daf9ffa7036f82f2227555389189533980f666da766.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/23e377312f524aa58d2df00f615f2ba333df48e9bec3a951f3400dcd48445320.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/279a220a882eb0f4a5aaf99775e52650accfc87255f4689f798b89c920fa00fe.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2a2d5e11fdddfd60310cac0e43bf29ce622cc537cd23f731bc5310ba63825000.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2d14e4dafd48a4c130855bdfe28c9e2879416bc76d1df27dea2387ee616a8d6e.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2d28dbb7ef177e11cd200e9af8b95865945635776ba0631aba7eda45d5e50e16.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2f64f41973c76e1bafb877ef62243d0e5f041e124169296a284c88d3f167284e.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/2f8d27962f39525503d5c998d7f7a3d6346a3779b0e665e9ffeccec724e99816.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/353dd94c15b63b844fe359744c93e3c5401fdfcdde1de9e0b0475ebe04dc7b63.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/373f9a67537dbcd02893cd1c482e811741f5190f26d84167c576600341f66366.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/3be0730d252ce52280e50fb629e369b062b10a5b77cc036eac1bba9b65e001e6.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/404e39988aceb6f02bed244c3746213948a194098ce90049d7196f22b9126e4a.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/456603533ad279709026b9eeb32f31e4b98173cf615267e6c0235f3fedcaf9a1.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/46533eb1f57e866f4b3d7db23c1e41d69eac566ce16cf0eaaa489f58fccfc905.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/491670110d253a16024706ec7405d6e072c71cc970114cb23a9b704427324a23.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/4e3f26b6c4ad1a6d726d44cee1ca0b7acc27715192e07ef6029f52bffdf3f008.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/5ce736eaca68385d6c78e05d08d6869b064f1917fe05c5ff221b95095e932c2f.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/5d1b45c784602c98b85e366b25a330b8999139c09210d2f87afbd5ab1b8e1855.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/5f3cc5a7a13478b0c6ad41837c902a8c437b4d8993b6309734f90304a219e777.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/60684f3d3986a70314b34245f30ed5ee0c32d8f1cb67aa3e25c9df666afd53e8.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/6069d8ad2aecb1a12cd9a8b9a1d648c00bbc75fa16b454c0a40981781e9b0aff.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/60be3444c7e9e60090617944733f6c84dbd9184e3ca043d90bc71203ac2e1843.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/694e3962b6513089f7422e4c7f7f0a886488b2f2af81f2d8e04be9fea31247ce.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/6b1aea25cad1aba2f4513857419cea3cc726bef42c8f50cff1f603a93684fd4f.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/6b862329245e2cf3d6ee57beeb561ef5b4c07b7c4f43eaa3fa034e3a04d7593e.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/6d82cfece7f56a333c3583fa7e97b1b2e38edd5c414893ba128e70a74c60ba7c.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/70d2b98c6bae77667eca77cea792000262c37530704cb819b7a23f3a27e1abc6.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/730a6304650d43a27099c3047a4b796d4a7bf1907d8803c38f4368919fad7f47.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/778ea9d42eca6038b63b8dde6494b6cfe612f50a5686025523e1d94844648b68.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/7cf759efb2d56065cb87aa7d92f246ba3a05e95abf0b0088ed07e813fc774082.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/8449e2e2d363ce4da7c3d95f31705a8c169198fccca297241014674456e5db60.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/866d6fd25bbc1782b38ca8bd7298b0fddb26f1af79db4928ed1238d1bd6b6693.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/8ec701549533fa137dca3bfb4c360a3c322d08f2389067108672bb014453c335.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/8fdc997ce1735a7a132a2fe21732e5f9c9197ac386ea7dd0b4e4a1aa7269702e.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/9020ba5c2797d8f026ddb72871b13f18a18cad4e0ec326c0f4653ceb438751bc.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/946b220f8e79e1284dc0e91a8ff9621472219f65c22e52ef0ce29361b86619c5.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/9517f78583ad9a9913badc02260ce8f8f06166857b6bf289f5d89589ff4b2760.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/95f0a9c3864713fc71be444dc74401921ee6963fa3987a67b4edac9ca6d9373b.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/9dd1282ef285a9a5941f1a6466abbe5e053a865099274c37e729146a77548d08.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/a0ae57ca481a6a43508929eb5b85bf04d18d1c7d8b70ebcd21741cf9246a62e2.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/a541e1b453f0964f264e3335f8de2df7119fc2147bff8b9dd48dd3639ef8f77c.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/b32ade946f2b727d426d37fb584d3ed6aed396f3e912bb4dd48f1070676aa5e2.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/c4d569a0aa4d595e745874a0b9aab671bfc715a46452f2dab62aeb748f2e24eb.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/c50b1ac2b3c49fdf951c5729da1a17dbbda4c991cdb35342bd8d1a6a0882f16b.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/c9b168f645be3187a19d8a3f872ef3a0dadd82b540dc64e8bf6a592a5a85edae.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/ce644c7d6f8e71aa07821e41d2a076599015c62ee6c5e172e62be0fcdb8abcf4.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/cec3c31f76a38d014724c716341d4aa41fccb2392f3fbf37fac0603c73e60229.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/d51bb0961d55e5b336570784f4f2d19964bd9ff1cc07439146f31b24c3fbdcdf.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/d6107c80c7f4c40a1f95b73a403d78050ecd5e23753cee0076a935b457ba3e54.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/d63214a0d6365e1ae339f63caad67526bdd942130f76b064b13c2b7b2365b49c.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/da9ece938630ff631bb83d83781c346e578d455b9c08af5016bd6c19f592b803.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/dd2862222f8501620d97adbac6ff2c2f38751a24043e09c34acc8bc6c162dfca.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/df4e1a20357554d15f630faf5bab3c37f758097fe7c66e93572ac3b9b792ccae.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/e17d507de761cee97abb5af12ff29fc85ef8a3b8f9684972e6952f0b7472bb6d.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/e4a0f999ffc4cffd6ca53476a047acfd08de284444f02de8698f754cfa8a4d8d.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/f32c3df25c1a545c728b998a8ae79b4e7c4d5cd7e8869bb7deedcd26740dfee4.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/fcbace51cd838261a00fe5c8d8bbbbc24b452398a34e5e6f6c5b1e415487d63e.gz', '.claude/science/physics-loops/toe-response-transfer-20261012/objects/fe3aa3cde43c557609b66b589ac49d16c3f9f8207f0d75ff0ff3a1cf3d692245.gz', 'docs/ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/TIME_AVERAGED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-response-transfer-20261012'
CLAIM = 'time_averaged_energy_transfer_bounded_theorem_note_2026-10-12'
MAP_SHA = '02c4cfa50afb8b8d8778453b29f43631f77a57946469cfab12342f509b521bb2'
EDITS_SHA = '1f389bbf52f4351acb9e98d750ecde401a35e38af33109a7b9c738a5547fb878'
PARENTS_SHA = '0ada41cb3ff583310414b984967ef40ce54cf65259784b26a0c7511cd7b7bce6'
STATUS_SHA = '4675b9275035d9f68280bb5e24245207b93fe03e82e7435e4163b1aa4cef8cd0'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def manifest_rows(manifest, selector):
    if selector in {'files', 'members'}:
        return manifest[selector]
    need(selector == 'recursive_path_sha256', 'Unknown exact manifest selector')
    rows = []
    def visit(value):
        if isinstance(value, dict):
            if isinstance(value.get('path'), str) and isinstance(value.get('sha256'), str):
                rows.append(value)
            for item in value.values():
                visit(item)
        elif isinstance(value, list):
            for item in value:
                visit(item)
    visit(manifest)
    return rows


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
    evidence = json.loads(raw_map)
    objects = evidence['objects']
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
    for contract in evidence['contracts']:
        manifest = json.loads(contents[contract['manifest_sha256']])
        members = []
        for row in manifest_rows(manifest, contract['member_selector']):
            original = Path(row['path'])
            if not original.is_absolute():
                original = Path(contract['manifest_path']).parent / original
            data = contents[row['sha256']]
            need(origins.get(str(original)) == row['sha256'], 'Manifest source alias missing')
            if 'bytes' in row:
                need(len(data) == row['bytes'], 'Manifest source byte count differs')
            members.append(dict(path=str(original), sha256=row['sha256'], bytes=len(data)))
        need(members == contract['members'], 'Exact archived manifest inventory differs')
    raw_edits = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(raw_edits) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(raw_edits)['notes']
    need(len(edits) == 2 and {r['key'] for r in edits} == {'response', 'time_average'}, 'Publication membership differs')
    for row in edits:
        original = contents[row['source_sha256']]
        removed = row['removed_metadata'].encode()
        need(original.startswith(removed) and len(original) == row['source_bytes'], 'Original source differs')
        body = original[len(removed):]
        need(sha(body) == row['body_sha256'] and len(body) == row['body_bytes'] and
             row['mathematical_body_edits'] == [], 'Original body contract differs')
        for edit in row['citation_relocations']:
            old, new = edit['old'].encode(), edit['new'].encode()
            need(body.count(old) == 1, 'Exact citation source count differs')
            body = body.replace(old, new, 1)
        need(sha(body) == row['published_body_sha256'], 'Citation-only body differs')
        later = contents[row['later_source_sha256']] if row['later_source_sha256'] else b''
        need(len(later) == row['later_source_bytes'], 'Later companion source differs')
        published = read(row['note'])
        reconstructed = (row['header'].encode() + body + row['appendix'].encode() +
                         later + row['ending'].encode())
        need(published == reconstructed and sha(published) == row['published_sha256'],
             'Published source does not reconstruct')
    raw_parents = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(raw_parents) == PARENTS_SHA, 'Parent bindings changed')
    parents = json.loads(raw_parents)['parents']
    need(len(parents) == 5, 'Live parent membership differs')
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
    print('per_element: checked and not executed — source integrity only; no spectral response, pulse-work or transfer inequality was computed.')
    print('per_site: checked and not executed — source integrity only; no ordinary-cell or temporally averaged correlation was computed.')
    print('per_mode: checked and not executed — source integrity only; no spectral measure, energy moment or shrinking-window asymptotic was computed.')
    print('per_block: checked and not executed — source integrity only; no domain, commutator, formal theorem or scientific mutation was computed.')
    print('lattice_wide: checked and not executed — source integrity only; no unbounded-energy, continuum-limit or pulse-propagation proof was executed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False}), file=sys.stderr)
        raise SystemExit(1)

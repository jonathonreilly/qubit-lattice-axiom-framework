#!/usr/bin/env python3
"""Bind the two analytic sources and archived receipts; execute no mathematics."""
from pathlib import Path
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015'
NOTE = 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = '632ab55e02bc7c0c80265d5345f4f9314d8070677b9aff0467c259f7314dbd18'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/BINDING.json', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/013a87fe96779ed2a761a32f4cd8c51c6d3b26171660606be95a227a7cebd861.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/069208dfb52205f92641324aed9a19b68ece57b88e12a6954bd66f1b8c865225.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/06af98715f88a91ac9be94b88bb553debb04c53fadf7ff0cec04dfbd3fd484b6.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/092c01db96a4a51fe7582f3b5ff1f308a5f92ec2ce3baaf6340cb6ce48a7ee01.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/096eb10a4553ca1f9274d236cccf9bc62d905c6c7907e04fc88c0bca2bb2008e.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/09f2ae653bb3f0b634ce169e4894e5fc207f35a6b9906704dd8992488f7b8554.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/0aa93cd9adc680fa328443ba5d1e3b8eaf60ee44889a6d2d8718d317d79ef165.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/0b12b6acffa6a4f7786c249d1b746314e819f61aa30ce0269c7d51ce40276905.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/0cec848de750534e46fd93a58a2c19d5646a48fa200c7e01a4d69f9faead75f5.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/11b76b5397c14fe068d34111ad70bcccbe9656d79951cd78fb86fe6dd6a9b50f.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/156ae2054112b7c188fcfa92d478f295db420be254af9a4fd0c39cd1ed4a98c2.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/173ea599fc2cd586e8f0c2333a10c1a5681061184238d7e445c39686d7a27834.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/1d3ad95f052acb0fc44b597075e8efeccac5df027ca5b59f4f40987f74577c2b.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/1d87fb117e295c0934ef458b67cf9762357f319c6c8e8af9e4787344184a45ee.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/2307e77ab8f1496e8310d11ebb2c4db2adb4a725018fb34ca3146a214effc70c.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/26e59992fbabf647ebef955287699b2db1d03946bd1e008d3f3010844a29de07.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/297883d7195ca7cb8518057ac2ca3e0eca1703b83f1e03965acc0a73d0aabbf0.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/29ebe192d6dbc05ee260e5dca76e2af7ee8083b6ccf6cf96466771a166677ef3.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/2e842b1e50239330c4722ea6f64db8a669f5cf367377a897bd40020d1bdc9550.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/34b091b9a23ebea63054440b71779a51a80efa82de3d6df27fc76e3e44775689.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/352510d25ca74dc069c3ba3787e960b8c77758e7bd29efc86d63025406227140.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/389797bf2934f60113dc0e4ce0c3e41326eeae055273e06595008b4ad532b0bb.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/3a04bada9d6af8521f32682c0a1029f01c3992c407a1aa93448d1f427843643d.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/3f211d090dbb4fa531871d8c633de0f04d02a9b1020b0ebf09e2ca833c9efb11.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/412c320ed0d1993caa4793f79a84d1a86ff4385563bdf698866c1ae9a6a14da9.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/416f3c26eb0a4ad39b5d8a414806a9e83e202a7eb53021e8663fe238e06ddf75.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/49f50de5f77ad0889897fe45fefa117149ec7e2ca4472ca2bdd2cc3f90ef6469.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/5036e1c463765d721f48b28a6c0a16565339e4e3c951dd91ae60f173745d493b.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/51c6c77bf9714e87cddad8873cb3722028fe35059140e7280fd1b332f4b1fe70.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/526fcf65a657127537498ef753b91c83432577c2e62644085f183f9d6fcb8b13.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/540edaf2bbd5695c7d0b9afc78266c55b40f34d6ec5c42f590f700d62c9dbe00.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/5841cd38c043aad9469c5db44e5a5518bfb83344a8e9ec06803166254b8ccc30.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/58710974c5c6bd9c45695565e181dcda51a92aa4248280bd6f7528f3883950cc.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/611b377ba4d6a1062dc60b5da64a8586934feb1fcf334644cfb0679a7ddf36f2.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/6231914f28e1d5fe4c651cf298ed0c5efa23c9831878076e1352fbe2c19a81ee.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/67819d6a5aebfee0d7e741eae8456f7a2d0e275f9caa02d6b99cf74e11a4781e.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/6a3a6ef255ad349f9f43ba0e60b81dc781be5feaa91841a3d83ba66b68a5ac78.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/6c081f93b2b76910cd780b369fa1649813832a66139565a71d0801a9d4fab5da.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/6c37d577c999d873d170f43f3b7c331b7864d6003a91347b55c210e15b0a4716.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/6f805e541a3dde5909777507974a17a232ead647b5ca5cf30978089dcb996494.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/703aabfc091b53aafb7d73cbf5ccec54643c2754fa81c80f1b5f2aa823f873d6.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/72bcc07a4c541a5327bc8c3638b80c9ba85a84e609a69581cfb7b43914cff3b2.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/741c85d0232e8a472e0ceea258fb98c978f9b6479161a98aec09e7d8a8aa4e2a.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/798946b973d30854809d780c47e10b7e41a1bc7c095289c93572b45b85e04a88.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/79ca10e5c5d8aa248f374ed9cf78e00269eb204bd2cd7ba422772f9942de6b0b.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/800d61fbe7897079920276af8554b9e590f02c04a621a0aa84798455e0360319.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/8670135c7cf4b3c6725e36c3cbab1ad0f54bc847a54861ac009b1ae2c4f683cf.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/937f88da7f1db74dffd92a3f244402d96e222d5eea7edf03c92f3cbff524f07d.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/984edad79e7e2c506b4aacdb5c3db2940252e5217f1f7af1b81c2984b95bc7c0.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/9cfc7b475f26975e61de5c52d5c616098e0d5e34f86507a95cccffc9f47df21f.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/9dabe993db55fc9e2cc850321e3c8350a6d6491215c6333740f11a0371c8bdc8.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/9dfc7ffd4aff5520ddc708b1695b4065a2fa6e1023c0b6ad63bcb009ef71f3de.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/9f72b63fef6a5fa3af4deac77d38aa66441ff9be011a2b2929927902e40fecba.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/a1e659ba1e55729774e49407f709e44c5ce85ab4b6dd2cc777d87af2eb262dbd.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/a59701d1f6b2ce2f0ab48a26753602b69019b50d5a2aec6ce035bde7b98fab85.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/aa0bbf1ffa93146517b38032dc71359ef599de0ac051f668b0a4dae647eefa0a.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/aad34545308840f8b4b7bd72aca408d4fd61a908fbdc00887f4b4c1a3254cd8e.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ab10ff83640fc5ab0774594dff4051f627ccfec831cac22bf8ee832da35bb44a.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ace7c247a1fdea044550ecce4a612e17c4d5199dfa2c49996bfd21c84bf3692d.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/b1514dc2533da7d246cba88eeebf3faf991b32ce041ec1e5f9f1be0441baab2b.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/b1aadd18a918dd866f515a77483b9e96c8352d2ed2f4daa93c2c89e206ccb20b.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/bb3a4764729ad9c0fa73401b9dc0cce83bf8098e17380041d2e0494066eadd17.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/bebc7c9cfd218e50132533cccbf99b3733cf583d6fdf7c249154f3fadfaad58e.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/bf010d368f29ca643c7c4f2fb45ce5225b2964bab494add711c86e470eccdcb5.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/c70b10ebc737f22f222940831de32888dd5ca0095f48117c8550d58309e1f479.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/c7f5ea25d4f7143f10782f1ce6185fd387a9363f2dacf6f31b95234916892d85.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/cc375a24a7d019876a105edb11aedf00df712ab093165d619e7ac4a573025a7e.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ceb0052c1dff47a18f27666b258e40f552ece5b8ce28bfd24105ec0013c423ad.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/d27e37865eea2667d1b2caff45c68c3bf7299e7516e9477cc553b1ddbd469654.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/d4483a219d9574991b965031ac9fcc4e8d9acf017bb9646f9cba0496e94f65ab.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/d90ac1a6c5b936b4eedc4c42c6d2c827a5683eb766de68bda022d58f0e8bbf60.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ddfb0116988db95742aa861a466255e50d95c8329b028f1686116044870a07ea.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ded36ff401ab413c81db0df4783e9515de37df84d9d24833db98423ca5f39c0f.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/e5d6fa6a7b27d5f7b518625f365ad5cf9add596c12d0b4c99c86dbb6f0c22d69.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/e82890f82d46acda5b02aefcf5460e361d465ed935d6bd68af5aa11e2bd3b9bb.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/edb08699caed99a39e1d4e77c6ba4ab8bdabc343e6b577bdf37a8a7cd1c048d5.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/ef91d62b60611d0c77dac107aab189460c1e06115c279e89b1576a3946cbe566.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f02e80d2c69be61819c9fc43a8a3125cc1432f895c01b93a5e7081ec2b4d8755.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f178c0ba77b156f49e486de5a07e850ac853b983ae055e43a7298f3b79a93d9c.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f29bfe0831527d6153b11b199bac9f98bf740d1eaa942e88aeaacb96a5d46fda.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f49bcd50e634c451c0f3610f029ce3cded7a57f2d0b9cf700e6eab5eb824b3d0.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f53ded2bc3ed75dbbe5b00f945aa1384e952d294a8575851c0ad23f59250eef8.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/f70a2ca51d82385f1637943bc9dc5543d20d1b737570179a51d86b6f34d71441.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/fbd320924474db3e4cb79b4374031253a286f2d5d718c63d27797e7fff006253.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/fd60194c167ec4bd9abcf7441f7363fd6a9d198f2c2117951b05ed5ada24c2d6.gz', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/archive/fe12497ed164d94c1e45ca4c3e260d7a10fe5b0c0ef1a7aaa5c0c75dbedad319.gz', 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/SIMULTANEOUS_MULTI_PORT_THREE_PAULI_BOUNDED_THEOREM_NOTE_2026-10-14.md', '.claude/science/physics-loops/toe-local-pauli-clock-cell-20261015/INPUT_MANIFEST.json')
EXPECTED_PROOFS = {
    'local_clock_gate_domain_revision/AFTER.md': 'ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6',
    'local_clock_gate_independent/DERIVATION.md': '43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5',
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'local-pauli-clock-cell-inputs-v1'
    members = manifest['members']
    assert len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS) == set(members) | {MANIFEST_PATH}, 'declared input coverage'
    data = {}
    for path, row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b = (REPO/path).read_bytes()
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'input identity: '+path
        data[path] = b
    index = json.loads(data[PACKET+'/SOURCE_INDEX.json'])
    assert index['schema'] == 'local-pauli-clock-cell-archive-v1'
    originals = {}
    for alias, row in index['originals'].items():
        assert row['stored_path'] == PACKET+'/archive/'+row['sha256']+'.gz'
        b = gzip.decompress(data[row['stored_path']])
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'decoded original: '+alias
        originals[alias] = b
    body_map = json.loads(data[PACKET+'/BODY_MAP.json'])
    assert len(body_map['complete_proofs']) == 2
    assert {r['alias']: r['sha256'] for r in body_map['complete_proofs']} == EXPECTED_PROOFS
    for row in body_map['complete_proofs']:
        raw = originals[row['alias']]
        assert len(raw) == row['bytes'] and digest(raw) == row['sha256']
        assert row['end']-row['start'] == len(raw)
        assert data[NOTE][row['start']:row['end']] == raw and data[NOTE].count(raw) == 1, 'complete proof interval'
    binding = json.loads(data[PACKET+'/BINDING.json'])
    assert len(binding['exact_parent_clauses']) == 1
    row = binding['exact_parent_clauses'][0]
    assert (row['start'], row['end'], row['sha256']) == (
        8389, 32138, 'be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc')
    raw = originals[row['alias']]
    parent = data[row['canonical_path']]
    assert digest(raw) == row['sha256'] and parent[row['start']:row['end']] == raw and parent.count(raw) == 1, 'parent clause'
    assert binding['stage']=='root_bound_review_milestone' and not binding['root_runtime_freshness_and_feature_binding_pending']
    assert binding['source_head']==binding['observed_base_head']
    assert binding['branch']=='physics-loop/toe-local-pauli-clock-cell-20261015'
    assert binding['observed_base_head'] == 'f6ad0ea049d121fa698fd1adaf9f28913d22d819'
    assert binding['new_scientific_programs_run'] == 0
    assert binding['archived_scientific_runs'] == 2
    assert binding['base_is_mathematical_dependency'] is False
    return data, originals


def checked_archived_runs(data, originals):
    records = json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])['scientific_runs']
    assert len(records) == 2
    assert {r['id'] for r in records} == {'root_exact_and_float', 'independent_exact'}
    for row in records:
        receipt = json.loads(originals[row['receipt_alias']])
        assert receipt['exit_code'] == 0
        assert receipt[row['start_key']] < receipt[row['end_key']]
        for stream in ('stdout', 'stderr'):
            expected = receipt[stream]['sha256'] if row['stream_schema'] == 'nested' else receipt[stream+'_sha256']
            assert digest(originals[row[stream+'_alias']]) == expected, 'recorded stream: '+row['id']
        pre = json.loads(originals[row['preseal_alias']])
        assert pre[row['seal_time_key']] < receipt[row['start_key']]
        for member in pre['members']:
            alias = row['preseal_redirects'].get(member['path'], row['source_group']+'/'+member['path'])
            raw = originals[alias]
            assert digest(raw) == member['sha256'] and len(raw) == member['bytes'], 'preseal member: '+alias
    return len(records)


def main():
    data, originals = checked_inputs()
    archived_runs = checked_archived_runs(data, originals)
    print(json.dumps({'result':'analytic_source_binding_completed',
        'decoded_originals':len(originals), 'complete_proofs':2,
        'scientific_programs_run':0, 'archived_scientific_controls_not_replayed':archived_runs,
        'scope':'Identity/interval/recorded-receipt verification only. The two analytic derivations and prior selected controls are evidence; this runner does not prove their mathematics.',
        'limits':'Supplied vacant eligible cell, one-head product input, supported coefficients, full costs and endpoint timing. Distinct effective signs and phases; no word, entangler, native supplier, permanent record or retained audit.'},sort_keys=True))
    print('per_element: one original datum, six supplied fresh qubits and unchanged original K')
    print('per_site: eight ordinary-neighbor new edges with paid old and added local loads')
    print('per_mode: full-space penalty and positive-apparatus claims retain their distinct domains')
    print('per_block: complete old/reference prepared output, explicit scalar phase and endpoint error')
    print('lattice_wide: no occupied-bulk packing, complete word, common-cap or native claim')


if __name__ == '__main__':
    main()

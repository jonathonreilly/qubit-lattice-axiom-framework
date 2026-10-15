#!/usr/bin/env python3
"""Two scoped finite controls and immutable complete argument/evidence binding.

The numerical/structural fixtures are not proofs of all-M analytic estimates,
active-background dynamics, native apparatus supply or retained audit status.
"""
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import sys
import tempfile

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-dyadic-population-filter-20261014'
NOTE = 'docs/DYADIC_AUXILIARY_NUMBER_FILTER_BOUNDED_THEOREM_NOTE_2026-10-14.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = 'ae81a693159476550efad8e451b7a6b623294d3fe4cba626727baced379c71c2'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-dyadic-population-filter-20261014/BINDING.json', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/BODY_MAP.json', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/03f11dd379a66925400b756e8593917eab1f773b69693dedbf4ec57d7a06dacd.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/041d1b00192abd9a1f66cb141efe2efa0f8f8e28c5e951aaba7614860440364b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/05988464e33aaae9a776ba95011c41cbc9acad489cdbfa28a2706ee86956ae3e.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/0c9c7a37fa2cbcc8a7ccfb7aeda950272a196a6917e1d4951dac64a71529e085.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/0e75e69e573224265a60f86ab041f4c28faf6e35171cf7cb8c4386e1b2b5d482.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/1378f862a62350971dcc409d63603ccd8a3eadc4954b4ad53d47b0c845e914d1.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/252836f496963d3410d0d77369a85dd11c7f98990475d11fb5406d957bdbf973.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/27b331e13e43291b7bf27c4d583214f1d6f02d8e5ce4d5f80aec45dfc5eb6ae8.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/2ff726cff0bc9683d2d8ed3cbf2180b93053c57a746c1d0835897ec7b739d8db.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/30ec29fc05dfe1c9e4792746b89eea07decd921ef99e63f0faed3dc5aeb14486.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/31e4f129f84761b08c9b978a7ebbb9377aec0d2a675096e46fa2668bac207c3e.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/35b24a4efd5b9bf78e764a382dcde507dfbd61d114ef587410015a7f58268509.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/3799d5a4c763f8fec223425bbd438c99ecc57e4468381cac58f8f34a279d7edf.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/3dc4fbd01bb16363608c400dbc156cbd756d0b6bb42b232d25a7038f886bf84b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/46cc3d8e664329ff59e3ace8547d2038042bae674899577ca5bf91d545b7e1fc.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/471a2ea1884d894d8b3db2934e5377d63256d98df5e5d0f87605dd81a4c8dc9d.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/54747dffbdb9978fd9db66a0ddf5eae73ca1305e4de09841a2acd19c748fa561.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/54bce3887a165ef36d344a8a666b8c1ede51ee788747200e422756d58371e7f5.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/55e879133f4f109e914dacdb481e978eaf641b9ebc6c184183c95106d79cf70c.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/58f52fae54f8d8d4fbc8b2d08a3ab9ce1a4461fd5b6293e3ae5265dfecea3f4b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/592d8d85060e5dfe53a6dfa90a3f6702870b43e0ea7877241683f05b5fcf0aad.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/5a6cb94e147a124b9a12b8ed58c31db4312e979b8c27b64df1d94ea3595a3f69.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/5c6103c40fc8bfa013106a6fcd211e5d6ba008c9197be9b022abd70f41182558.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/5f0e49f04d308fceedbe2c291355eb03aed3ea47022d094b7217d0c8c1f2015f.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/6ae764c165a6d579d493697c136a02e9597bb4cce0876415ea14adadc8cf1378.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/6dcad9694d1cac4f3f4ebec28a49e428b93a7a2dae3373815819f920965145ec.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/72020ea7147e978ca7dc99ea2df910cc2f8db734b3343554baaad0fbc63b3a74.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/73f3c31b862b894446e0adbf7bbb7ddbd827faa238fdedcb299ba3574064f300.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/74552c388452bd2598d242dccb271ec9b62456d6142cc35ab574d8c9fc96e0ce.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/79d2388a7f6e2ce36d8b1055bd2ad80149a9e5375ff7f23248391d72bf5692ff.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/7bd0454eb42827486be61ef5d722880c2f5d8f8d0040f918c65b8493857c2725.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/7ded8e782945d1fa14eb0a2a6a22de9245e187137e4f0a535bfcf578940c2a07.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/7dee5bd6aab53961aed14143e4089fdc4b1190e2d00800a29a6e9e597abd9689.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/86f5b54dc2b085f4e533d7fb2fd4e1d360bdd703322c349b9f045b6eab689039.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/883e0c0ad7d31fc039de0d895fb586818c2562150acef528fb4c79c784f9441b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/8d3de83e97874aeab1ada0fc53af5b3a7c371c6080d8c411917ec1c59744fdbb.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/8d7856f444af09de87b73035a3fdc65cc2d0d6c74cdcd5dbb80e46e13c55a966.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/8d90981b93bf77f125deb04f6ff39aee352ca308e7cc046ae594849a19d633ff.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/91b9c3af4b8a4e3934a031e5a71a9018fb7124016fb9eb33a395b6451fd6dced.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/93810f0f117b7477e532cee968c594368704a018fe65b2e40245c184e812cb67.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/944200b6ba6cc206ebfefac7061e26af066702bc5b53501615e971518d317ba2.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a03c2ca9d34990fb5f71563d0dab816373d1d1ec0ec963126b63f5127a3fa5bf.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a04037e9b77e6f4c00f7d317e10398e975c63bca11372d7ae0c672e73c257617.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a068686d8f23c9170b8273b6552ceb781551eb420bdd9dbc0dd31ec9168be417.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a2c53528bb958c14a75093d165fa2e3d7879d14b09e2413e971d992a2680840f.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a2ef7eaba38e21f5551cf546cdda27b676f35bcbb68e28820a50d68af170cb25.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a4d3621110837e22ab24bd856b0cc28c6f38dd1408d9cbdfd516115ad8e01036.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/a6222821b8b784c4a924b2ce5b9a68506a886d53807753b73c2c620d8a37d3be.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/ab94eb79b8daf28ce554ab37abcdba066df72b161c31b11a9d4c586bcad97cde.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/abc29205c8c3ce215d78774b9c070960908492bad8e2c03abecfb283a61c48b6.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/aef87fc341f3a1b9117060abc24643823b25995484e035ae3ec9a0a69300ee03.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b0ebcd6e512e17c66d26729926f6fab920128b77859ced7e7e364c3bc1087609.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b16a47f4ddafc2a528fa4a2fe95b712fe9c4a8ed0a01c8c39201ed2eba3fde5f.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b1aadd18a918dd866f515a77483b9e96c8352d2ed2f4daa93c2c89e206ccb20b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b1e514dc7191496d186877ede7766f0f880f9df24fe0e456daf5bb0840522546.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b36d533e092602edd4fb6d0a7f4bebc34f7051712025d97a6d49e57c32bcef90.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b51c0a08a156cdf48e1fe67dccf7862eb3e564226d506df9b2c2b6bfcfa7039e.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b60f8be82fdea76d874c9edb56261fab9d99c0ec3969d44da37ff11c213dcc9b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/b646fb16bc22945f8521b0f0de76fa3cb6670da9fa1cb85b443c7e2070187450.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/c11ab3b1b73fa521a2ec8155228d3d4d16a791eb1b2ba181ff9a165080e17e70.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/c1308b2399f74e057a2c1be3b96e232a52505557959ba3594a958635bad1e8aa.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/c13d858a19b0c496fab8fd24fa874a5071848c265a0d2ae06dc873a8a9583472.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/ceaa6f2ed0f38f3575f4779eb7b2a568ad828f02f1b41c52d8ceb5ca8ef4c56d.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/cf3c7ebdc218fffe615753fcb2176cb213e082bc042ed724a9c9f18df31db113.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/d6c14f1fd5be414315c6fe4c8f8b21e69716dc1bcb4eb8b085d8a81405e62b46.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e3307d073d2718f8cd7c75f29823f9725aeb8bf2ad9440dd5dfd9d4e6882daac.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e4cf20725fc9ce0f3a1d9204f037e14c992090511a6f8adf5fc03d02d3e519a9.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e5ec2d166a24dd36c900d9d4032ae1b876ee838f5f92457ffc1a3e4979cb8351.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e6b59790c51a2aadb59a9d3fc6f2ca4faa7bfcc0fd0b4656a822552e7188bb84.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/e834df10c6d25a0421ca895a650dfca572c8d1d2065bf758086633d35e3db590.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/ee9d109bc62f105aa4aaec70495358160afdb118a6b1dbd378c5316c2c575e2b.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/archive/f5475e94ee4dcb7a226628995720bcce977b1cac16122063926d69fe4dc39c55.gz', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/implementation/selected_layout.py', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/implementation/selected_quantum.py', 'docs/CHAIN_PREPARATION_MOMENT_SCALING_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/DYADIC_AUXILIARY_NUMBER_FILTER_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md', '.claude/science/physics-loops/toe-dyadic-population-filter-20261014/INPUT_MANIFEST.json')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'dyadic-filter-inputs-v1'
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
    originals = {}
    for alias, row in index['originals'].items():
        b = gzip.decompress(data[row['stored_path']])
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'decoded original: '+alias
        originals[alias] = b
    body_map = json.loads(data[PACKET+'/BODY_MAP.json'])
    for row in body_map['complete_proofs']:
        raw = originals[row['alias']]
        a, b = row['start'], row['end']
        assert data[NOTE][a:b] == raw and data[NOTE].count(raw) == 1, 'complete proof interval'
    binding = json.loads(data[PACKET+'/BINDING.json'])
    for row in binding['exact_parent_clauses']:
        raw = originals[row['alias']]
        parent = data[row['canonical_path']]
        assert parent[row['start']:row['end']] == raw and parent.count(raw) == 1, 'parent clause'
    assert binding['science_head'] == 'bf3ecf67438816b28634282361428ad096245ed1'
    return data, originals


def module_from_path(name, relative):
    # Entire imported source is declared and pinned before module execution.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, REPO/relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    data, originals = checked_inputs()
    quantum = module_from_path('dyadic_selected_quantum', PACKET+'/implementation/selected_quantum.py')
    layout = module_from_path('dyadic_selected_layout', PACKET+'/implementation/selected_layout.py')
    print('BEGIN_SELECTED_N4_QUANTUM_CONTROL')
    quantum.main()
    print('END_SELECTED_N4_QUANTUM_CONTROL')
    old_argv = sys.argv[:]
    with tempfile.TemporaryDirectory(prefix='dyadic-filter-canonical-') as scratch:
        output = Path(scratch)/'outputs'
        sys.argv = [str(REPO/PACKET/'implementation/selected_layout.py'), str(output)]
        try:
            print('BEGIN_SELECTED_M5_ROUTING_CONTROL')
            layout.main()
            print('END_SELECTED_M5_ROUTING_CONTROL')
        finally:
            sys.argv = old_argv
        expected = {alias.rsplit('/',1)[1]:raw for alias,raw in originals.items()
                    if alias.startswith('dyadic_filter_chain_layout/run001/outputs/')}
        actual = {p.name:p.read_bytes() for p in output.iterdir() if p.is_file()}
        assert actual == expected, 'complete selected route artifacts differ from frozen originals'
        summary = json.loads(actual['SUMMARY.json'])
        assert summary['M'] == 5 and summary['k'] == 5
        assert summary['counts']['SWAP'] == 2100 and summary['counts']['PHASE'] == 100
    print(json.dumps({
      'result':'two_scoped_controls_and_source_binding_completed',
      'decoded_originals':len(originals), 'complete_proofs':4,
      'scientific_controls': ['floating n4 complete-outcome/literal-K/reference fixture',
                              'integer/Fraction M5 ordinary-NN route/label fixture'],
      'whole_selected_layout_outputs_compared':len(expected),
      'limits':'All-M operator/moment estimates and active-background prices remain analytic. Restricted phase errors, full input/readout contracts and growing resource assumptions remain explicit. No apparatus realization, optimum or retained audit.',
    },sort_keys=True))
    print('per_element: exact specified phase family; selected floating matrix/control residuals')
    print('per_site: ordinary-neighbor routed controls, eligible region and returned dirty factors')
    print('per_mode: no continuum or physical-mode identification')
    print('per_block: all outcomes and reference factors retained; successful branches use actual normalization')
    print('lattice_wide: finite M family with explicit resources; all-M estimates are analytical')


if __name__ == '__main__':
    main()

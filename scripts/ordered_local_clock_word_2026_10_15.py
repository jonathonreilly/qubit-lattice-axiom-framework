#!/usr/bin/env python3
"""Bind exact word sources and archived receipts; execute no mathematics."""
from pathlib import Path
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-local-clock-word-20261015'
NOTE = 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = 'bb2055c1b6c6325c98cb9941ed811438dbb394c26c3c7fde6dec6385d25d7075'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-local-clock-word-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/BINDING.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/0692d2a12bde13b518b41734d0add828f2de21afec5930dc96ae6b30c31696d2.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/088bbf9ad344e139e7f4bd309dd86074cbb7197cec4b0d73968d25088a5c787a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/08cff32851b0b6a8ebcd625a9cbc935ac14c4dd5ed89d66f4c9e59180d004c94.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/0b878b3e38dca1bbfd6312981cefe40869f46de1b3620ea08c7695179a324065.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/0e9dddedd952c0973f17753f65c6cac82794c91828f73ca0335f2b73aab79448.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/15827ae596ed17149780624c1ab269a4234a89d34df99c217718a961c546340e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/16bf920021062f3f26a12a72324b4a08eabdea85533284fed628f07f320f5970.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/186edb4d7c118be7168d1ab5d17a813121792a28e3bbca9618d0ef4b76fcad68.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/18df7a74393a264ae4b19f1bbc59c526ce73f335dd9d72c7e921f6fec2ad5cc1.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/1f7691b6584effc866e7b93264372d615ce1e20d6768278ccc6efda2138adad6.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2214320bbe9e551f6e15c36859374aa68e6b06c0a6ecb04c3cd82317fecf57ad.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/232ebba0b52e89f3649ee510dc0238816647da62804f25e5d662ee3fdae8b2b9.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/240f3453df3ed554f39f65970f03d075d9ea75321dda552a6acef534df4c2b52.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/24d0228d8b1dc64dc8a28dbc307dae44d4ea5218739a47f01b91aa45738f1337.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2a0d69b6171510cf2e1f5f83a28276d51279d1493efa6b34390d194bdac14656.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2ba94662c8cdafcf650eef9d1cee00d5742925b6869c9314c9cf394bda5484f7.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2beaaa6ecfd0a986cca7ea3c0521cab624bca6a71ef0967d91904c3cb88db4c5.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2db7bb279f318a7d52ffd2dce5a38b1cd9a42e3103ee1b5c1c7ee536220dc59e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2e5ee8f4c79340d5a54c0727842bfa2398242e23d0f447e0eba0d611f95b4ea9.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/2ef8ec43db1584741c74f8d10edd9d2243e69199ac233ef355ef489542caa6ee.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/345c0b0815fc3582d9e5ce3de1f95f951dfad22ee53baacf07526de2338d4153.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/3715076a9f09fc91015f719dc7f96242650c61957804d64641fe4baac29b862a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/409a22746a9760032d57299938e62864e6e9953100110dc998e29e5a17512c50.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4234912a810a44f29e91245e9226405b417761e41b57385f00db4b184c5b7b9c.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/467e48c48f046e51492ff6ee9b23f0be0e745070cfd365c2fb0406257acc6447.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4724fff5436aa3053813abe2a5a47ef6cfe28fdac09614d706164e4bce34623c.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4a056820f761743a3dcba4ab6a567a57d6ed98a749d7c8aa16c4240eabda4c0d.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4a53b862cb59b43d5af5019e2b5047c1f82b888081214c7c69ae23dea451851f.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4bc1694695537040d1eb946dd251a59e5bd4ebdd7dc0dc49696016c13f4e8b7a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/4e6d3b1adb44189a7dfd744b7c8d00abf9b544f20eb30cd77d99221913ce565d.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/540edaf2bbd5695c7d0b9afc78266c55b40f34d6ec5c42f590f700d62c9dbe00.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/56ba2cc91092735e9a1abb01cd096f40ea2631a98fff9299405839386a6d13dd.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/590e4e97075d05a151147e1e72fd0dfdea71ff367c8b0618097928a4a68dab63.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/5b1191605babb02cf13d211e324bb10483c9a0d4336942893702ba932ea9dd21.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/5cfbd5ee7f9b0df6b72176870cbd0674f041092d7a6932fc1f0ddbd8e97a0692.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/5f9670a56d1df911108ffe803cad6e4b7d75c64c79d40b5aa1d7fb6dd6aeeabf.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/6095716801c5497e066892e2dac0aa3a0c9c306c0e862241b66d3630c4fa986f.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/611b377ba4d6a1062dc60b5da64a8586934feb1fcf334644cfb0679a7ddf36f2.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/62e86f6ea238b2a9ef6cfaad123ce3fea402d7b5569623d1b9c3338a4eea9210.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/654d2a2d6c5846ba63b38457dbac6eef5872c78dc9087136b7e785c209e29c94.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/6da2dc570069ced7df2e61fe1ef9975b12c603188326499316e37ee803f9f87c.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/6e59cff11365747184c5d5ab5846af3b5058e2dcaa2ed712aa7451333d0f9373.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/725defe09a03fc7e36877b465976274a0c8c160899711300b83aa8f95b5f95cf.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/7473c3d8dad9dda2369f46ce6d6bdd8e828996c5092c9b0a6e09f50cd03e9869.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/7552997cf65231c5160efdbd52451b1a4a956ee0119ea8f0f129b6dc3fc8e443.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/79ca10e5c5d8aa248f374ed9cf78e00269eb204bd2cd7ba422772f9942de6b0b.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/7bccec3a1e36456eb7aefb43e9854ed52b08214d306b86748c7a703f8fee2e2e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/80fbc421a81d50a12ac70e07996ac59edf316b3795cd23c3a461dca151b6c5f8.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/84b2f4c4f1f9bfbb4de25918bfc9304dd05a5874e7f18187dd4a9c38623b7b80.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/8bfd8e5075554f0755346a3b7ad073ae33a464b3b2d64ecc2e932b9e8041174c.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9078553f3f0e4b464ac04f96644081ffb4f5fa71c93c5737ac6411a3ae3cbdce.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/922a48a1238d3cc5ae0e2a80f2d8c53f44c7d54781da3d9c6fc6cb84fcfd09b7.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/94cae9075769e8648e3145c39885a6ff367fcfb110cd3bc823b4fcdcbe6c3f7f.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/950ff867653d5578dab305b851a6b34b115033fa9b3ec1a8ab811bbd2c3ea0e7.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9760fb46179242057318eab67731e75dcccfffc16a1cc6221710867f9b4e644e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/983248350fd194bb7676b0da08745d5d92b2a31f605d57c6d7109bba91fb642e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/997f1f4738bc8724ca73da1b36ba4458d62fdcaf36d02272aa8837b55b3b3a77.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9b2011b480fd2fe2e7583ebcca39d2e3667d9445d773cc4ae681c3e7c905f54a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9b24aecc8808ca1de597146095cf2aca7c622a705b8a955ea5f5dab4c18e7e35.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9d0aec94b1597a1b1f5a2465052596b63c22055b942731494aa6710b3af0cd2a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9ea15e0450e59829b2c951ae562f55f7bb46e8fb1ca039c59f948329d19d9dfe.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/9f5ce535d3684b707d780d15b538255d7228669f0cfa2a6170c51c11bdd5674a.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/a139e56c3cb8906b60f68132b0e8172323b88810101db9b6a0da9565539b11b8.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/a3908a5fec53c806cdc7479c115977d2c67f56cd1b64e3dca6035405a856c0fb.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/a806462b98d2d9a87beb0ee1fe7e1aca75006ebbd38359a924fda254f0915673.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/ae07d406bf0bd61bb9ba81a201ded74f87e388b70392b5ce4ca81c93779b6d75.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/ae7f41c49233777a2cd065362db2178a9b29d5080c30f9a62734504e7e37a426.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b17508c1f6afafc3f18d15badd18a3a53e40f5dc04f9168b937d3455caab5ad5.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b50665d53cc4118cc810668c2c4ba1752905478245ed7839a1320e35e0b87312.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b56ca0220837f7fab180a5c36c85a38dd051283040ba54f78f519190d0ade09e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b5f1955a0bbf2e4d669bf6360c6d7c970fd9937ea6e7f596ba403c7fe0d2823b.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b62f3a659bf34185410bd98851107f13baa5ab541c9c8aba463f792ac7dd85fe.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b66afa7c4ff075800e6eec912ddeaa6783605a735cbc8464ec78ed810f7d5dc9.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b6893d1759135fb6bf767831cb93346fcb1f9078c2fdbdd31a87c36c907e0533.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/b8742a19c6978052777e60a7a65bee6e1d9ae8f1fc8cc98304cd574987eddee8.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/bb3a4764729ad9c0fa73401b9dc0cce83bf8098e17380041d2e0494066eadd17.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/bfbc1b8bf1d2fa6a826273b4cf7acbc6ce7fe3fc02a8a7dd9a8d4f5f46fbcb93.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/c164118926e77b7fcd4947254fbe39608e217a2c0190eb4952889f7ba6805e8d.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/c359366ee4cba225e8ed5557fbdf36bfc2cc9f00e7f8b11ecd5cc33b5448e2e1.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/c46b9efe9a512de581f592a8bc396d2d38e9a6b49315e7676aaa03706ef250a1.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/c7f3e7f365eab9d1961f66f1caa41329e7e980fccdc5bbeffda22b82a4b91a04.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/ca7da20b768551341622b19d4860dd0e07d14ebab2e714ea62f7597cd42be004.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/cf17c355fa01f01c8d8c860c86eed49ed603359d9cde41dc3f9b4f8e42fedd3e.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/d4669ec65e329159622cbc6047ed7d36de588ed2746c814c9cc7e0a7b4c1974f.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/d51463c017145cb2287eb7287587574c93fc8be0113fc2765a76fa8f10a1c891.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/d7fc8478b73af1612811b1dca652d87f31e72dab64bc517f387e24468b3d5ed7.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/d8bcb30eefbd9568de44ca128b19fafe140bdbbd8ce5c2d51c2c018600a69c39.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/dd0db9ce859765afa5ded1888cb2fd362f1c07c9cf5ac70f94dbca74fc6e8935.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/de6a4d20577f396461959032a7cd19b450d4c945892282f4d5edc6ca814518ae.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/dea852660a3d1638c74665c2a43684d6ad3f8024ed459a7b26fc74616a512172.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e19c68ff0adba0ffeab57d9d3bd463ba2874791b97fec547fc560c51d645e0c7.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e2870dbb3ac324a1f8f560f13fdd6733d2480f1501f132f63b509da0bdf9ad8c.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e330000f550df639feb72a12de1ad393ab03fc46f22f59e43072fcb494582897.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e3985930b9542d48a21e411b5e678b1422f1aa12ee7c095cc30627c246e00cec.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/e720165511bf1d7e24306618c04748b02309ee774ba44dcefdae971f1b2a5047.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/f1d9c59b3b15580ca0644ca93d346aad21b0b8492dd8e00a02303388c02bb643.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/f53ded2bc3ed75dbbe5b00f945aa1384e952d294a8575851c0ad23f59250eef8.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/f91d8066ff35fc29c8b9edf99aaffe1327caf847b07c6878db476527777a9705.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/fa509e29075503a57604f2c953dca5a4906070eb730fa974925fb719ea317ea4.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/fbf18a1b0c08e9a53b3592a5bd01684f42ddc7f538dc3ae1466826d40fd958aa.gz', '.claude/science/physics-loops/toe-local-clock-word-20261015/archive/ff5733effcea599f588a59b358325dd30625b12e679dee6f183c938a5115573a.gz', 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-local-clock-word-20261015/INPUT_MANIFEST.json')
EXPECTED_PROOFS = {
    'local_clock_word_candidate/DERIVATION.md':'de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd',
    'local_clock_word_independent/DERIVATION.md':'6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a',
}
EXPECTED_CLAUSES = {
    'premises/root_cell.md':('docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md',14202,25142,
                            'ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6'),
    'premises/independent_cell.md':('docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md',25189,52484,
                                   '43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5'),
}
EXPECTED_ACCEPTANCES = {
    'local_clock_word_root_review/ACCEPTANCE.md':'654d2a2d6c5846ba63b38457dbac6eef5872c78dc9087136b7e785c209e29c94',
    'local_clock_word_independent_root_review/ACCEPTANCE.md':'a3908a5fec53c806cdc7479c115977d2c67f56cd1b64e3dca6035405a856c0fb',
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw)==MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema']=='ordered-clock-word-inputs-v1'
    members = manifest['members']
    assert len(AUDIT_INPUT_PATHS)==len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS)==set(members)|{MANIFEST_PATH}, 'declared input coverage'
    data = {}
    for path,row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b = (REPO/path).read_bytes()
        assert len(b)==row['bytes'] and digest(b)==row['sha256'], 'input identity: '+path
        data[path] = b
    index = json.loads(data[PACKET+'/SOURCE_INDEX.json'])
    assert index['schema']=='ordered-clock-word-archive-v1'
    originals = {}
    for alias,row in index['originals'].items():
        assert row['stored_path']==PACKET+'/archive/'+row['sha256']+'.gz'
        b = gzip.decompress(data[row['stored_path']])
        assert len(b)==row['bytes'] and digest(b)==row['sha256'], 'decoded original: '+alias
        originals[alias] = b
    body_map = json.loads(data[PACKET+'/BODY_MAP.json'])
    assert len(body_map['complete_proofs'])==2
    assert {r['alias']:r['sha256'] for r in body_map['complete_proofs']}==EXPECTED_PROOFS
    for row in body_map['complete_proofs']:
        b = originals[row['alias']]
        assert len(b)==row['bytes'] and digest(b)==row['sha256']
        assert row['end']-row['start']==len(b)
        assert data[NOTE][row['start']:row['end']]==b and data[NOTE].count(b)==1, 'complete proof interval'
    binding = json.loads(data[PACKET+'/BINDING.json'])
    clauses = binding['exact_source_clauses']
    assert len(clauses)==2 and {r['alias'] for r in clauses}==set(EXPECTED_CLAUSES)
    for row in clauses:
        assert (row['canonical_path'],row['start'],row['end'],row['sha256'])==EXPECTED_CLAUSES[row['alias']]
        b = originals[row['alias']]
        parent = data[row['canonical_path']]
        assert digest(b)==row['sha256'] and parent[row['start']:row['end']]==b and parent.count(b)==1, 'source clause'
    assert binding['conditional_acceptances']==EXPECTED_ACCEPTANCES
    assert all(digest(originals[a])==h for a,h in EXPECTED_ACCEPTANCES.items())
    assert binding['binding_complete'] is True and binding['stage']=='root_bound_review_milestone'
    assert not binding['root_runtime_freshness_and_feature_binding_pending']
    assert binding['observed_base_head']==binding['feature_head']==binding['source_head']=='0393ca788f8bf87f9201e3f3dab911da9de162e7'
    assert binding['observed_base_tree']=='0b053f782429a021023ca7e6c78d7b55c17521b8'
    assert binding['base_pr']==9588 and binding['base_branch']=='physics-loop/toe-local-entangling-clock-cell-20261015'
    assert binding['branch']=='physics-loop/toe-local-clock-word-20261015'
    assert binding['publication_pr'] is None  # Dated prepublication source binding, not a live PR query.
    deps=json.loads(data[PACKET+'/DEPENDENCIES.json'])
    assert deps['publication_binding']=={'binding_complete':True,'base_branch':binding['base_branch'],
        'base_head':binding['observed_base_head'],'base_tree':binding['observed_base_tree'],
        'base_pr':binding['base_pr'],'feature_head':binding['feature_head'],'publication_pr':None}
    root_review=json.loads(data[PACKET+'/ROOT_SOURCE_REVIEW.json'])
    assert root_review['completed'] is True and root_review['scientific_programs_run']==0
    assert binding['new_scientific_programs_run']==0
    assert (binding['archived_selected_fixtures'],binding['archived_scientific_attempts'],
            binding['archived_successful_attempts'],binding['archived_failed_attempts'],
            binding['archived_failed_root_metadata_attempts'])==(2,2,2,0,1)
    assert binding['base_is_mathematical_dependency'] is False
    assert binding['optional_four_rail_word_instance_adopted'] is False
    return data,originals

def checked_archived_runs(data, originals):
    archive = json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])
    records = archive['scientific_attempts']
    assert len(records)==2 and {r['id'] for r in records}=={'root_shared_head_float','independent_exact'}
    for row in records:
        receipt = json.loads(originals[row['receipt_alias']])
        assert receipt['exit_code']==row['expected_exit_code']==0
        assert receipt['started_at_utc']<receipt['ended_at_utc']
        for stream in ('stdout','stderr'):
            b = originals[row[stream+'_alias']]
            assert digest(b)==receipt[stream+'_sha256'], 'recorded stream: '+row['id']
            if stream+'_bytes' in receipt:
                assert len(b)==receipt[stream+'_bytes']
        pre = json.loads(originals[row['preseal_alias']])
        assert pre[row['seal_time_key']]<receipt['started_at_utc']
        for member in pre['members']:
            rel = row['preseal_overrides'].get(member['path'],member['path'])
            b = originals[row['source_group']+'/'+rel]
            assert digest(b)==member['sha256'] and len(b)==member['bytes'], 'historical preseal member'
        assert Path(row['program_alias']).name in [m['path'] for m in pre['members']]
    expected = {'local_clock_word_candidate_seal':0,'local_clock_word_root_source_verification':0,
                'local_clock_word_independent_root_sources':1,'local_clock_word_independent_root_sources_retry':0}
    assert {r['label']:r['expected_exit_code'] for r in archive['root_metadata_attempts']}==expected
    for row in archive['root_metadata_attempts']:
        prefix = row['prefix']+'/'
        receipt = json.loads(originals[prefix+'EXECUTION.json'])
        assert receipt['exit_code']==row['expected_exit_code']
        for stream in ('stdout','stderr'):
            b = originals[prefix+stream]
            assert digest(b)==receipt[stream]['sha256'] and len(b)==receipt[stream]['bytes']
        child = originals[prefix+'executed_source.py']
        assert digest(child)==receipt['child_source_at_launch']['sha256']
        assert len(child)==receipt['child_source_at_launch']['bytes']
    group = 'local_clock_word_independent/'
    for name,before,after in [
        ('DRAFT_CLARIFICATION','history/DERIVATION.first_draft.md','history/DERIVATION.precontrol_a806462b.md'),
        ('PORT_DOMAIN_CLARIFICATION','history/DERIVATION.precontrol_a806462b.md','DERIVATION.md'),
    ]:
        record = json.loads(originals[group+name+'.json'])
        assert digest(originals[group+before])==record['before_sha256']
        assert digest(originals[group+after])==record['after_sha256']
        assert digest(originals[group+name+'.diff'])==record['diff_sha256']
    assert b'AssertionError' in originals['actual_runs/local_clock_word_independent_root_sources/stderr']
    return {'scientific_fixtures':2,'scientific_attempts':2,'failed_scientific_attempts':0,
            'root_metadata_attempts':4,'failed_root_metadata_attempts':1,
            'launch_limit':'Selected scientific receipts have no child launch pin; preseals and self-checking source are preserved without retroactive upgrade.'}

def main():
    data,originals = checked_inputs()
    attempts = checked_archived_runs(data,originals)
    print(json.dumps({'result':'analytic_source_binding_completed','decoded_originals':len(originals),
        'complete_proofs':2,'scientific_programs_run':0,'archived_attempts_not_replayed':attempts,
        'scope':'Source identity, complete intervals and recorded stream provenance only; zero mathematical execution.',
        'limits':'Two distinct ordered-word contracts; supplied compatible geometry and one-head input, unchanged arbitrary K, complete endpoint phase/reference and costs. No optional four-rail numerical word acceptance, arbitrary packing, stop, window, native reader or retained audit. Dated source binding is separate from later PR and retained-audit status.'},sort_keys=True))
    print('per_element: arbitrary old input/reference; specified ordered single-Pauli gates and compatible cells')
    print('per_site: root example 14 fresh sites/19 edges/all six neighbours; independent 11/16/five, +x unused')
    print('per_mode: full-space apparatus arguments separated from one-excitation prepared-domain estimates')
    print('per_block: distinct signs, endpoint phases, padding, positivity/gap and norm contracts retained')
    print('lattice_wide: no arbitrary occupied-bulk packing, common-cap efficiency or stopped/native computation')

if __name__ == '__main__':
    main()

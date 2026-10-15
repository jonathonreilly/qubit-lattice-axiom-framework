#!/usr/bin/env python3
"""PROPOSED source-identity primary. Never executes archived or mathematical code."""
from pathlib import Path
from datetime import datetime
import gzip, hashlib, json
REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015'
NOTE = 'docs/FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PARENT = 'docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
PARENT_SHA = 'bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a'
PROOF = 'local_clock_finite_reservoir_candidate/DERIVATION.md'
PROOF_SHA = '26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4'
MANIFEST_PATH = PACKET+'/INPUT_MANIFEST.json'
MANIFEST_SHA = '6f3034fbf34ff3adf50d6f80ddaccc7ca7583c0e069afaba269b18c6b1240a96'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/ACTUAL_STACK_BINDING.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/BINDING.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/EXPOSURE_AND_LIMITS.md', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/SOURCE_ROLES.md', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/03cd209918a9c4d4050399248bbf72d8c9c2ce0aba24e6b64b3377ece2f5cf9e.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/043c8c9e12273166f9f8f8a2039915b60b6fe2e66fb71bfe292c96d80c4581af.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/05f5808e728cb9bd716b7caad7e1be5bdfe0961135c78729977fd90f9663a32f.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/073760c4693aba071e6a8a967272969e523dead6a646060a7d290d4f4e7b71b5.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/093609920e9c2a7fc3dd2e92076804b0d9b7f275813ccdd486b680d1fa2698bb.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/0fa148f01dbb56444557ca88e213e2c5056ed01efe2dd47394ac98ee0e60dee4.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/10c86d1916e19b9fbbd08d85a690e18161eca6fb52428198ec67215c501d1b26.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/1578d11d066bed98cef633a4924ab2abdc592757a54517738aa3ac506db705ef.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/188275ad97d7edbf9012908d65a58cff476725bdebe8076226fdb4c4e944e43e.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/1d64ea512607da71f2f6ab53fcf9a2a6e87b9dd687f876927bd4d57dcea56afc.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/1fc235b9fec232f3f9fa487782af74e35b5240f769f888dc3c1ac1ffc30e30ee.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/20516174e638cb69ce28305a357420de05f4bcb1051b34484d619d2a40164e12.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/21daebcdba4a076a38348f024bf27ee4f208e57900c29be8a2dbb0aa9f8be97a.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/21e1f7bd71bf4d8a1391a6de908868d6db1a76ebb874b9447ccf7e1461ce7f6d.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/237778954c1bb337b0a1ee92e294d739a64837c3f944a9f37716cd3ae36fbad4.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/26220ec995a93bd6af725a6b3463d0b676b9d8a864b4867459bef7dd9560e9b4.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/2be647403f168c6f80d5b63c75914d33ddc8fbc9c1b3bbbcb5467b5a144c5699.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/2c9ce2811c1ae5bd51dae188f407894da4cdff8954da4fcbe6002974b7028591.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3074bbc8b14ffef058ea76e1df8c2e8046d32fdadaa6d5b3f5ec11f7663b5334.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3205f1c5568b9bfa96a66c042aee57f32a101a160a9c159b5e34e15c12f6c631.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/346016c5915a0b2c007a39d1325be2e1c7cc218e5a00c56ab9c96c6f9835d030.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3970540fba57e3a7ccfa2143aa6e25447eb489e99945c285e09c7461b89d3d11.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3bee26de8cd2b627cc52c27868025eb0c0f87f306f79e28e802950ce4d6a489d.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/3e12c0f802db2ada44a60d2c5ae8285ca820f1cd7f70351c2d317688813d4660.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/402c0c2a8e15a2054f030afd5c57951d34c1a3973a6d264feed6fe351325d0d3.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/44b4f0fbcf5648f2a1bf80cdb6255c53fad0a90e939b64b9ee2e7708f1b09c01.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/4921c6cdcce1fa77b34addcbf6cd1ef505dca7ec051c4c13e97c667431bbd333.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/4bd25e3afe941142840203da59eef1bb42a306914e7e217400ad4a754ebcd669.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/4e67377ed1a8a907fa93d4925ce4613967e13888d69baeb4a24ffa45f58d53e0.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/51a1622784a86aac00ef24e5a97af364ccf9034f323a532f8ca0938ddb516e2f.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/51feac4ded8b6fcb20e6d02014a2e1b2ea71db190d3632c3216190e3e84ba0f3.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/526a92c6f5239f18b07cf46697a14e0a04da5df4a7f55150b655c9908eadef48.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/53e090c42049a29d718c0da67bd2f82e5d832d4220c8b84792edfe8c1ba29b1b.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/551ea14252055b79d9bd00f31cc5e68d7b8c922d25e73135b36c1070ec18dec6.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/56f12c6eaa3baeecd6f905a800b05e077ff6604543df2728bc7b390ae84c0983.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/5d6e400bbb1988028a5ab1baf07ad04f4f8ce41bccdaed69e9756ac9d0382f15.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/5ef6d9d052d49d289a708c1f08e55c29860e30a398039b93fda40092546b0a01.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/605104ce5d867ec509b90f28a0bdfb051d556a787d49f930abf88134aa5ea8e3.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/6b4e48012140b8c5f7013f825aafb79b956e00780976b7d5cd1d4f128f6cb454.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/75e7f13a1815b52c5b727ff5fb84018c6a513ee6b94dd6602fb898bd148bcca3.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/80a68ef28c687f0102846603d71703f50037b47a9ae35aec815d91d2b39a854e.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/8437af7b2c4da9d70ea2dbd7485110ecf1726ad6f6f7d491eeefe637cddca32d.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/86253c61a645b191e89c8ce5dda7a4e0be181051dacff1ac2da3f4d2cade37b5.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/87aad64322238fd96f6700bd213de10c481e9c96d427a772c3c8132d2bc2c1a5.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/8cb6f9ef0b27b0976ab2f8b6d57ec7e3c1498bea57cd94761d05731bb5b302ce.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/93ff37d874eb3f5d4bccd3c4b1b8315554e8893654469bd868afe865b9743d9a.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/94b74d1cb544ded5cf6436dfb1bb8a57561818f1a67b145dc1c5c411a0ecfac6.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/95fbc8dddb92e732e76327546eeb2ec89ce0a673939c8135c5f160c72fa03825.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/96a8d86a6c8b668d11b663d185b3d976941ad3c315acbbaf6b1aa7aee792ea92.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/99dc402cc4712af3fbe3df392aada73964c85c7c110f1605fe9551773ddf2d47.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9c1d6f7766da2a51ca34279f5cc0b7dcbd10e437c268c1fcbcac168df976cf7b.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9c23375dbd9836947813ade194c935c6a2db1867e4864db9adc6bbc7fdb58749.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9c9e242fedeff45313dacf613000c5564101c14f6007aa85378c56a9f92fdeb9.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9d6e49392c3755ea2552f41584002ec28775d1c34313cdd61fb0b9bd4a597a69.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/9d7fae05a847679be328f0c38deabd7bebbe2aa84c606920c4de57620f686a45.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/a2ae7deaee56cb4371825748afb6fea29ffb0b801586c49eaf748adc8396a3de.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/a9510cc118551d8d753eeaa49b2d8d06e3900b4f47d92c461ec253929c112a05.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/aa924b57c91ebcbded01dccb4d17ecf65e3cc871de2a0ea73acbbc000bab7240.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/ab01824a069c3890e95fae3b6dd502cf6f5a00324ae501a5d85da2a78abf0969.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/aec4d59300e61cd4028193502673970a516be9b36607da5135c3511a14e64275.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b38a504e3cd0466fec14caff6004a5fe150f9de5ce1ea9179f611b10b6ef66ef.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b39e59da42a363a222ce37fdbc3e9c20c5d5d2414bc700866dc8e7817ec5dfff.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b4d2ef841dde3db400f9cab2bb1b5f12a52bbb365ae18eb406b2cfa5fd6bacbf.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b54aff33137b3f7e886629f3758b75a4a8dd301c79aa5631496d28461a1897aa.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b7e8079476fc1def6b1847b34e3aa0a791fc8c8b82569a9d2c8fdd76e2dea433.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/b886f6c7c9b2b074df8fe1aed07a2509dcb1e969643c28c1c2159b5274162db8.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/bc08f951f2912de840ff463f3db9549cb971f68ba22c5b1eea5c18bd721c83a9.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/be06f413be668dc757e44de52a6eacdcce3175be29ac84451e1757ac87f159ba.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/c7458ce37ea82c52104ee8cecc0d4bb7f797bf13e58eeb9231a3d0e9e4d9a187.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/c956d1c013e0242904e550ba2c77e160b0a7c0b5f1321107851454cfd0964ecb.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/c990122cac870743ef0fe68db9b76477fb473c34ba875df18adcf9c01ba3fc30.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/ca0f3805272b7b5fe50c4c95733c2b194fb0f0ccdab00f9eaad1f8b7a580d2c7.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/ca7ca8d53712e6a55963bfcb0f6bcae259b6b4a42dbd9f79e72daec6522d3b98.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/d49988bc59589f9ce612f59c911ed3a8f59d2b518221184b16a8637366bc4220.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/d4fb275b53fb212bb13bb5ae312ff8360c964f9ef710ef80463582ca276485ef.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/dc0afa6bd741f08fda9edd79031cda5106f9745dcc39f81871a662493841eaff.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/e1c34b5541cb4479beb7c0653916dab9824cd6ffe4661b9b52d5855e73a75507.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/e3d9612e694cdc974a89b773a85bd1d9a8ce0c8f53944ac5a4411625ef77ab12.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/e79a996a6e61bdb744247fad4bfd5f1c6ab44d8f26a67eda5c20064f12c35502.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/e84dae2e32c9522590e42c2cef2f850918a975f2b342c5433045af6f5afcf24c.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/ee5336ec3a3d30673020bff0c59e43862fc5dd224099e5c702ad172e59f65881.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/f44337b4164ca035922139946dd685ebf9c386ce030132a416af2569f8e66367.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/archive/fc581db2a8b9057e25c218b7200c3d1476e792d34be37e0d11e07d236085aaef.gz', 'docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-finite-reservoir-clock-preparation-20261015/INPUT_MANIFEST.json')

def digest(raw): return hashlib.sha256(raw).hexdigest()
def same(raw, row):
    assert len(raw) == row['bytes'] and digest(raw) == row['sha256']
def checked_groups(index, original):
    groups = index['source_groups']
    assert [g['complete_file_count'] for g in groups] == [50,76,9,4,4]
    for g in groups:
        prefix = g['group']+'/'
        assert len(g['aliases']) == len(set(g['aliases'])) == g['complete_file_count']
        assert set(g['aliases']) == {a for a in original if a.startswith(prefix)}
        if 'seal_alias' not in g: continue
        raw = original[g['seal_alias']]
        assert digest(raw) == g['seal_sha256']
        members = json.loads(raw)['files']
        assert len(members) == g['sealed_members']
        for rel, row in members.items():
            assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
            same(original[prefix+rel], row)
        assert {prefix+r for r in members}|{g['seal_alias']}|{prefix+r for r in g['explicit_extras']} == set(g['aliases'])

def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'finite-reservoir-inputs-v1'
    members = manifest['members']
    assert len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS) == set(members)|{MANIFEST_PATH}, 'declared input coverage'
    data = {}
    for path, row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        data[path] = (REPO/path).read_bytes(); same(data[path], row)
    index = json.loads(data[PACKET+'/SOURCE_INDEX.json'])
    assert index['schema'] == 'finite-reservoir-archive-v1'
    original, objects = {}, set()
    for alias, row in index['originals'].items():
        assert row['stored_path'] == PACKET+'/archive/'+row['sha256']+'.gz'
        objects.add(row['stored_path'])
        original[alias] = gzip.decompress(data[row['stored_path']]); same(original[alias], row)
    assert len(original) == 160 and len(objects) == 93
    assert objects == {p for p in members if p.startswith(PACKET+'/archive/')}
    checked_groups(index, original)
    mapping = json.loads(data[PACKET+'/BODY_MAP.json'])
    assert mapping['raw_body_modified'] is False
    row = mapping['complete_proof']
    assert row['alias'] == PROOF and row['sha256'] == PROOF_SHA
    body = original[PROOF]; same(body, row)
    assert row['end']-row['start'] == len(body)
    assert data[NOTE][row['start']:row['end']] == body and data[NOTE].count(body) == 1, 'complete proof interval'
    assert row['end'] == len(data[NOTE])
    binding = json.loads(data[PACKET+'/BINDING.json'])
    assert binding['publication_binding_complete'] is False
    assert binding['source_binding_complete'] is True and binding['stage']=='root_source_bound_prepublication'
    for name in ('publication_pr','primary_execution','cache','graph_execution'):
        assert binding[name] is None, name
    checked_stack_binding(data,binding)
    assert binding['root_acceptance_sha256'] == '51a1622784a86aac00ef24e5a97af364ccf9034f323a532f8ca0938ddb516e2f'
    assert digest(original['local_clock_finite_reservoir_root_review/ACCEPTANCE.md']) == binding['root_acceptance_sha256']
    assert digest(original['local_clock_finite_reservoir_decisive_check/REPORT.md']) == '188275ad97d7edbf9012908d65a58cff476725bdebe8076226fdb4c4e944e43e'
    clause = binding['parent_clause']
    assert clause['canonical_path'] == PARENT and clause['canonical_sha256'] == PARENT_SHA
    assert [clause['start'],clause['end']] == [62134,80595]
    assert clause['sha256'] == 'b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1'
    b = original[clause['alias']]
    assert digest(b) == clause['sha256'] and digest(data[PARENT]) == PARENT_SHA
    assert data[PARENT][62134:80595] == b and data[PARENT].count(b) == 1
    dependencies = json.loads(data[PACKET+'/DEPENDENCIES.json'])
    assert dependencies['direct_mathematical_parents'] == [PARENT]
    assert dependencies['expected_new_nodes'] == dependencies['expected_edges'] == 1
    assert dependencies['markov_reset_action_imported'] is False
    return data, original

def checked_receipts(data, original):
    archive = json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])
    attempts = archive['attempts']
    assert len(attempts) == 10 and sum(a['scientific'] for a in attempts) == 1
    assert archive['replayed'] is False
    for a in attempts:
        p = a['prefix']+'/'
        r = json.loads(original[p+a['receipt']])
        assert datetime.fromisoformat(a['start_utc']) <= datetime.fromisoformat(a['end_utc'])
        if a['kind'] == 'author':
            launch = json.loads(original[p+'LAUNCH.json'])
            assert all(r[k] == v for k,v in launch.items()) and r['returncode'] == a['exit_code'] == 0
            assert a['source_at_launch'] is None
            assert r['recorder_sha256'] == digest(original['local_clock_finite_reservoir_candidate/record.py'])
            assert a['start_utc'] == r['started_utc'] and a['end_utc'] == r['finished_utc']
            for s in ('stdout','stderr'): assert digest(original[p+s+'.txt']) == r[s+'_sha256']
        elif a['kind'] == 'review_metadata':
            launch = json.loads(original[p+'LAUNCH.json'])
            assert all(r[k] == v for k,v in launch.items()) and r['exit_code'] == a['exit_code'] == 0
            assert r['source'] == a['source_at_launch']
            assert a['start_utc'] == r['started_utc'] and a['end_utc'] == r['ended_utc']
            for s in ('stdout','stderr'): same(original[p+s], r[s])
            for key in ('source','recorder'):
                same(original['local_clock_finite_reservoir_decisive_check/'+Path(r[key]['path']).name], r[key])
        else:
            assert a['kind'] == 'root_metadata' and r['exit_code'] == a['exit_code'] == 0
            assert r['child_source_at_launch'] == a['source_at_launch']
            assert a['start_utc'] == r['start_utc'] and a['end_utc'] == r['end_utc']
            for s in ('stdout','stderr'): same(original[p+s], r[s])
            same(original[p+'executed_source.py'], r['child_source_at_launch'])
            same(original['actual_runs/recorder.py'], r['recorder'])
    prefix = 'local_clock_finite_reservoir_candidate/'
    pre = json.loads(original[prefix+'PRE_EXECUTION_SEAL.json'])
    assert len(pre['files']) == 8
    for path, row in pre['files'].items(): same(original[prefix+path], row)
    scientific = next(a for a in attempts if a['scientific'])
    assert scientific['prefix'] == prefix+'runs/selected_control_01'
    assert datetime.fromisoformat(pre['sealed_utc']) < datetime.fromisoformat(scientific['start_utc'])
    invocation = json.loads(original[archive['review_direct_seal']])
    same(original['local_clock_finite_reservoir_decisive_check/seal_review.py'], invocation['source'])
    return {'historical_attempts':10,'historical_scientific_attempts':1,'new_mathematical_executions':0}

def checked_stack_binding(data,binding):
    stack=json.loads(data[PACKET+'/ACTUAL_STACK_BINDING.json'])
    raw=stack['actual_binding_raw'].encode();same(raw,stack['actual_binding_pin'])
    b=json.loads(raw)
    assert b['binding_complete'] is True and b['stack_role']=='ancestry_only_reset_action_milestone'
    pubraw=stack['parent_publication_raw'].encode();same(pubraw,b['parent_publication']);pub=json.loads(pubraw)
    assert pub['state']=='OPEN' and pub['isDraft'] is False and pub['number']==b['parent_pr']
    assert (pub['headRefName'],pub['headRefOid'],pub['tree'])==(b['base_branch'],b['base_head'],b['base_tree'])
    for label in ('parent','existing'):
        receipt=stack[label+'_receipt'];assert receipt['exit_code']==0
        for stream in ('stdout','stderr'):same(stack[label+'_'+stream].encode(),receipt[stream])
    observed=json.loads(stack['parent_stdout'])
    assert all(observed[k]==pub[k] for k in ('number','state','isDraft','headRefName','headRefOid','url'))
    assert json.loads(stack['existing_stdout'])==[]
    assert binding['stack_parent']=={'pr':b['parent_pr'],'branch':b['base_branch'],'head':b['base_head'],'tree':b['base_tree'],'role':'ancestry only; not a theorem import'}
    assert binding['feature_branch']==b['feature_branch'] and binding['base_branch']==b['base_branch']
    assert binding['head']==b['base_head'] and binding['tree']==b['base_tree'], 'dated feature binding'
    feature=stack['feature']
    assert (feature['branch'],feature['source_head'],feature['source_tree'])==(b['feature_branch'],b['base_head'],b['base_tree'])
    assert feature['actual_binding']['sha256']==stack['actual_binding_pin']['sha256']
    review=json.loads(data[PACKET+'/ROOT_SOURCE_REVIEW.json'])
    assert review['completed'] is True and review['scientific_programs_run']==0
    assert review['actual_binding']['sha256']==stack['actual_binding_pin']['sha256']

def main():
    data, original = checked_inputs()
    receipts = checked_receipts(data, original)
    print(json.dumps({'result':'analytic_source_binding_completed','complete_proofs':1,
        'decoded_originals':len(original),'archived_receipts':receipts,
        'publication_binding_complete':False,'dated_source_binding_complete':True,'scientific_programs_run':0,
        'scope':'Exact bytes, complete parent/body intervals and historical source/stream provenance only.',
        'limits':'No archived code runs; no proof, physical supply, future publication or retained status is certified.'},sort_keys=True))
    print('per_element: arbitrary old/clock/passive-reference input; full transferred reservoir correlations retained')
    print('per_site: distinct supplied ordinary-neighbor memory sites and positive full-SWAP pulses; old K stays installed')
    print('per_mode: all initial clock sectors; one-entry preparation has its separate prepared-vector residual')
    print('per_block: full scalar, covariance, work, calibration and consumed pure-memory costs remain charged')
    print('lattice_wide: finite supplied driven endpoint; no Markov law, native preparation, reusable reset or classical reader')

if __name__ == '__main__': main()

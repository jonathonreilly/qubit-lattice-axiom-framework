#!/usr/bin/env python3
"""Exact scoped circuit replay plus immutable proof/evidence binding.

Finite arithmetic checks do not prove the quantified analytic theorem, supply
an apparatus, or grant retained audit status. Read the canonical note.
"""
from pathlib import Path
import gzip
import hashlib
import importlib.util
import json
import sys

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
PACKET = '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014'
NOTE = 'docs/HERALDED_AUXILIARY_VACUUM_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-14.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = '0d988a26ca2d0d10d1860ad802d3d90b5100a52bdf481c6ae1bc5ed00a2967b5'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/BINDING.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/BODY_MAP.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/02114cad25e20136c1a5d9983698995c7aea88bd4be45597fa3a1ec9f435881a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/03723a7083e41e75d8434bb0881830b8a3e261caf690f54d51ad254a098ecefd.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/069f1d19c5f0db47d3161c8c438158226d588d0e5c766b81cacc994f33339871.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/07ede3e644e593168df17ccb85cbcd3339589e457f5594691d47598d1d71a123.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/0840083464e69306992394f2175e95655b8c0054c5a3fd398c7ad6e77da79f95.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/08cd7aa0e9e0dbe0112b09d3b3a90d695aee715c93c57ffacf56ccc821bc77b0.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/0f4de989012cdd6ba51728bdefa6ef9a63b1c3802f719ef4d710e3a4d3911696.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/11bd8df0b11c0ccc1c504ad705f724fc2811d2165cb584a1e648ed236514e016.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/137146e229a677df3d07f06c08769220bdea3057e6967b8cba3582e869589e74.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/16324af3ddcee860458c9c75387745aaa4517bc92ec55cc5413b1dfc1cf0c1cc.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/1749cddfe755b21787856459bad410c3b5a30713356b08a254cb833784e2169d.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/1eef7a686836ec30db706849f4b19305154b87bcba62d4d6eafdcf23c828f2ac.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/1ffd740f134bbcfe638b668cb7e6e270d4ddae3c3da60034d3a462c74f683373.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/205f93b32a37ec06f6461ff0214b012c2baed2ed46351c1b512f4d2f3bcc989c.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/2722b030adb8b4b4acd061ec252ba9de819e7b26b055070bf1ef1ba14e14a403.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/2d01d27b1381fa733510f438a6a6463a4ebe1cf1badbabbd18b1968c75cd1d2d.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/3163b141c2df7ac22571bcb223339f2070613da6e0f8d8e6326b308d439224b8.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/340e306d5ed6d863723386aad107709f68b082c5ce07f3f7e88441e0c8b65fa1.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/36a823ad3ca6735cb0d5f7fb60b0aee1a53d101396c74a4eb0ddbaf252fb7913.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/3795816f377f34b502fec675cbd167b481f051c978161cad38ef1e820f25c3f8.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/3f4b3e0787bf435a20d677696c645807758f1d7a65e695db14467b3a463a6d30.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/3f9048d1500f181e3312b1501bdaa7a0a8d27e6b475c46b8f1f4c9716a0cad6e.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/42b8017b0cc8f0a43c5c890bd9fedde199d7d9fbb31580c4aab329fff0de3f1b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/5296d693de98289ef5777a225b65cb8d1b7fc753fa8c64513d9f294e31229d1d.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/55732c56e6b79bef62d720f35035c58e7993b873aaa71fe153346e791b94ae86.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/5a1ebccb723cc2ef5277d75480ef2e339fc5b9ae70ec77e0686f8b9a3b40f99b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/6202f1199ec392a75de23f39d7eb28ad4e18ca59c3a87e0334331e72450e2834.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/6560a1250282757ecf434005532af71251f3f651794693e2f4cad063be4a96f1.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/668f2be08fea81601296b315d92a5fc5382122cfb82277bd5e99ed36cac902cc.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/674078bbf0828cb14f75c7a63008a7221f93a33f963873913cb8fdddf146acd7.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/69af6458c62ed6afa54264f7b4851ee64bc8781184bc8b56e0a6508456c914f7.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/6e29f69581dd5d6221889ed773e0a28bc8c21e39a6d15e26fe61a363fd0aed29.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/72659e2309ef9dacdc45e987d0011f96b72c5dd96a2f4c1e05db96f92789e8ef.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/738a162d999143dc00ff124bb9696bf1e64d11d8129a38f57b089868f2b33bb4.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/785bc535da04fce31d63a7eafa473ff2bb8399b10e09606e638343571e6f46d6.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/79d2388a7f6e2ce36d8b1055bd2ad80149a9e5375ff7f23248391d72bf5692ff.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/84445cdedb3344f8c800ca738f479d8a9e5a027e9cf3beb05902780933083418.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/87cfd88157c8dcc1533988480adb5778962faf95ba11a6946da097fc2d9dd619.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/883e0c0ad7d31fc039de0d895fb586818c2562150acef528fb4c79c784f9441b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/88f60f60bc08dbb930810b371d404ac0d2efafddcf8ccf71e3bcfebedaa6694d.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/8be03f5137098eb5ae4ea88cb9031a4b39a3ba6f97ff8e3b65ba6adbd08cc088.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/8c09c49e0f2aa9a8289e1b84cf8a46f7e99b56e83f80aea568612bcb456a663a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/947a98e2b1fd07b02891269286b71d3192d5e4bb1a8350591a71cd4ea09f1966.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/95a41ee90945564581f59c39fbaecfd03fa8cc34d093720b2b1c9c26384f594a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/95ea97ee6ad11583790f31fe28b80ff097c19d635848c8dec60f339b952e2d15.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/999dbbdcf51a9e978c3046b6b053ad66810ef6d20d190032a8b56ce8adbca292.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/99dfacc7cdf903f0aa314413908d972252e5d0495380767566e3c2d33d785eb7.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/9cfc7b475f26975e61de5c52d5c616098e0d5e34f86507a95cccffc9f47df21f.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/9f3af056ddcb868f869b54964e116d39400bebb29f8baea37a28a64852ac6373.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/a275b3eced35ef9d32ad0498526dec720c79dd0e9684aeb633e0f6795bc12556.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/a522f018635a85ef9e852d465de15e064c3c9c7e86016087a91efbdf7626f94f.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/a5cee2bc3d8309324aa78f88b0382aa2f370d5e6f2224b4babfeccf468bdd281.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/a7041d8ada95360a0c8720d1fcc3948b381787edcb2eeab1d72b024d0eebee33.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/a7173098f7acaa4170c5b204791c41a13f575ff9ae455a311cca3bbf0987726b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/ae0cbec1281a1e8d0e0fa50fb611afcac0b211847f67128feb3bfd1b89903304.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/b19555c7602b7ccc01096c96b438f686e5f49636f917eb430b500586bdb8dec6.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/b1aadd18a918dd866f515a77483b9e96c8352d2ed2f4daa93c2c89e206ccb20b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/b2aaa9dc5c377c422e318481c7961e4994175e6608fa30f89175c685aa5a931a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/b59e405789a24ea9289630bc47403cc55cfc6445e1fc329bcaf4a22690a9189a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/ba235986f71f87b5f965e171ad8f14abbb1accbe402f7a0071dc1d6e52ebf167.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/bb173e0e2fa575e66cfd8bfb071220f0aea6407fced87b6f3624213b31131d30.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/bd2b0e294624e9dd9b445e4431f1b1463da8b0e597977bfe4ce03c893c3d74b5.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/be611f96e9e5223b0d2db76787013b3ef9780c6d92ae0fa5dffd3416869c988b.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c163db2da7ea4a26e8c4de0f097e645374e11485494c295d457e0a229c030a10.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c4eb9ad86f06e1e1b7a2fe91ef3fd6497762d88cc81250dbec0cdc880d1c7355.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c71a176f3500bdbcefc0ff9848a3f777a9cecb171b2e264253937320d573befb.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c788769855f9630b87463a6704859643a79cd3405f13a08ed3237318fda4ab3a.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/c7c926950084e72d5fc2c7b6201b5b00ffeccc85bff07e6ba7d9046cb9eb3657.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/cad8399b80adbbdeff5e45c61db5abffcb27c583a556abbd3daceb8f22fd3ca6.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/d02b4f8db6dcf13aec5cd51861a4a54f3c2b50e8f776047007fa0bf706668686.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/d6d8429511c95662c8c6cf53ed7b1bfb478e2e1e3b677a09ef808db87adc1e71.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/d8926e72e8b4966885d0f64765c7ca31ec2c42f378b0aaaf6576008f570650e9.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/d902b0588f1500a07e489934971f2905fe9c4bb31cb524192076fdc1c503ca07.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/dd027a9539db413772b196af330907b1d0f47beeab6769546e68bfc5ba85eed0.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/de39729d0f845994e04dd0b417ac7d05f90be14790c47d2183d7cb6ae24cd1c1.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/de7e79161faf1c35941285c9670e9cc421f798c51204da139575c36870ab9976.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/e23a1e9d7e69b6fe13f0f05bd5fe71176797328089c3363a026fb50ecc1d1379.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/e62de55f454bc3b57ffacad7aa770fd85fcfed747786553985ffe01cee680878.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/e7fef5086c3fe3ab4ff8282ea684570bf36907fa47403193d166f8dd696b0b3e.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/ea4f1ba7ea1d9ff0d7d0740d450adb24a82ab0ec3f72153f56299bfa16235d91.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/eb059561d4147d115adfb1eedd53b0bb1b9282c553759b01e061c10c72595c74.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/ee7d12568d5d4bc0fc1d2c103c88fc264667631432ca4a8140d85ab4bc690c0c.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/ee95545cdf99858491b9c34c0161e397b11825dcf9399b1343949c961f810ed0.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/f377096028172449af5dc93be1abda978fe6afde5d89386cf7cc328bdcf9b4c2.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/f9fb595ebcc67ba1e4c3ba84ae694973c06602c1558aaa2af093ca4dccbdd69e.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/fc3adb33069bd1678855c30576ca0daf3d0eb22bb754e9604e5f2758c1cafb38.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/fc8acdba1ea7d4552f32ed3ab72540c415696ba0c05c5187e6b9d7f74a8021ee.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/fd87b89e3bc0858cd641471e88948ee1e9a0d1ecd68f57d501600fd38d7ab839.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/archive/fe105be37bacc2d0e6a7f7c28d520a507c86b9e384005fafffb26f133bc2109e.gz', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/fixtures/word_M1.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/fixtures/word_M2.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/fixtures/word_M3.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/fixtures/word_M8.json', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/implementation/emitter.py', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/implementation/exact_circuit.py', 'docs/CHAIN_PREPARATION_MOMENT_SCALING_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/HERALDED_AUXILIARY_VACUUM_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/MULTI_PORT_PREPARATION_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-14.md', '.claude/science/physics-loops/toe-vacuum-preparation-certificate-20261014/INPUT_MANIFEST.json')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'heralded-vacuum-inputs-v1'
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
        body = originals[row['alias']]
        parent = data[row['canonical_path']]
        assert parent[row['start']:row['end']] == body and parent.count(body) == 1, 'parent clause'
    assert binding['science_head'] == '6708b30b3ae16610f7a5061301c38adc356aff75'
    return data, originals


def module_from_path(name, relative):
    # All imported bytes are pinned by checked_inputs before this function runs.
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(name, REPO/relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_gate(raw, wires):
    names = {'X':'x', 'T':'ccx', 'CX':'cx', 'CV':'cv', 'CVdg':'cv_dagger'}
    assert raw[0] in names
    sites = [wires[tuple(x)] for x in raw[1:]]
    assert len(sites) == len(set(sites))
    return tuple([names[raw[0]]] + sites)


def checked_word(data, m, emitter, quantum):
    packet = json.loads(data[PACKET+f'/fixtures/word_M{m}.json'])
    assert packet['M'] == m
    sites = [tuple(x) for x in packet['sites']]
    aux = [tuple(x) for x in packet['auxiliaries']]
    pointer, borrowed = tuple(packet['pointer']), tuple(packet['borrowed'])
    expected_geometry = emitter.geometry(m)
    assert (sites, aux, pointer, borrowed) == expected_geometry[:4]
    assert json.loads(json.dumps(expected_geometry[4])) == packet['cells']
    factors = aux + [borrowed, pointer]
    assert len(set(factors)) == 4*m+2
    wires = {p:q for q,p in enumerate(factors)}
    logical = [canonical_gate(g,wires) for g in packet['logical']]
    two_local = [canonical_gate(g,wires) for g in packet['two_local']]
    n = len(aux)
    if m <= 3:
        mask = (1<<n)-1
        oracle = lambda s: s ^ (int((s & mask)==0) << (n+1))
        columns = quantum.verify_permutation(logical,n+2,oracle)
    else:
        columns = 0
    # Every actual decomposition block is matched with the independently
    # phase-resolved primitive. Equality composes without a huge dense matrix.
    offset = 0
    toffolis = 0
    for gate in logical:
        if gate[0] == 'x':
            assert two_local[offset] == gate
            offset += 1
        else:
            assert gate[0] == 'ccx'
            a,b,t = gate[1:]
            expected = [('cv',b,t),('cx',a,b),('cv_dagger',b,t),('cx',a,b),('cv',a,t)]
            assert two_local[offset:offset+5] == expected, 'phase-resolved decomposition word'
            offset += 5
            toffolis += 1
    assert offset == len(two_local)
    assert toffolis == (10 if m==1 else 8*(n-3))
    assert sum(g[0]=='x' for g in logical) == 2*n
    # Consume every physical gate once, preserving direction and all factors.
    logical_coords = [tuple([g[0]]+[tuple(x) for x in g[1:]]) for g in packet['two_local']]
    physical = [tuple([g[0]]+[tuple(x) for x in g[1:]]) for g in packet['physical']]
    ranges = packet['route_offsets']
    assert len(ranges) == len(logical_coords)
    cursor = 0
    for gate,(start,end) in zip(logical_coords,ranges):
        assert start == cursor and start < end <= len(physical), 'route interval coverage'
        emitter.check_route(gate,physical[start:end],sites)
        cursor = end
    assert cursor == len(physical)
    assert len(physical) <= 8*m+5*toffolis*(2*m+9)
    return {'M':m,'sites':len(sites),'basis_columns':columns,
            'exact_Toffoli_decompositions':toffolis,'route_blocks':len(ranges),
            'physical_primitives':len(physical)}


def main():
    data, originals = checked_inputs()
    emitter = module_from_path('vacuum_emitter',PACKET+'/implementation/emitter.py')
    quantum = module_from_path('vacuum_exact_semantics',PACKET+'/implementation/exact_circuit.py')
    primitive = quantum.check_five_gate()
    generic_route = quantum.check_route(3)
    dirty = [quantum.check_ladder(m) for m in (1,2,3,6)]
    # Independent generator deliberately uses F as borrowed workspace.
    composed = [quantum.check_composed(n) for n in (4,5,8)]
    words = [checked_word(data,m,emitter,quantum) for m in (1,2,3,8)]
    result = {
      'result':'exact_scoped_circuit_and_source_checks_completed',
      'decoded_originals':len(originals),
      'whole_proofs_preserved':3,
      'five_gate_matrix_entries':primitive['entries_exact'],
      'generic_route_matrix_entries':generic_route['entries_exact'],
      'dirty_ladder_basis_columns':{str(r['m']):r['basis_columns_exact'] for r in dirty},
      'independent_predicate_columns':{str(r['n']):r['basis_columns_exact'] for r in composed},
      'actual_frozen_words':words,
      'targeted_wrong_interfaces_detected':['missing dirty ladder cancellation','missing final predicate block',
        'controlled-root relative phase','reversed routed operands','missing return swaps'],
      'limits':'Exact finite circuit checks and immutable-source binding; all-size algebra and state/moment inequalities are analytical. Supplied control, pointer, readout and full-reference error contracts remain premises. No native realization, optimality or retained audit.',
    }
    print(json.dumps(result,sort_keys=True))
    print('per_element: exact gate entries include phases; supplied net controls and pointer preparation')
    print('per_site: restricted cubic layout and eligible factors; no arbitrary recorded-site compiler')
    print('per_mode: no continuum, mode identification, or physical-energy identification')
    print('per_block: full old/reference conditional guarantee; retain failed outcomes and normalization')
    print('lattice_wide: finite M family with growing resources; all-M proof is not numerical extrapolation')


if __name__ == '__main__':
    main()

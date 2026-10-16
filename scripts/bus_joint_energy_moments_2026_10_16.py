"""Source-integrity only: no scientific calculation, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = 'docs/BUS_JOINT_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md'
PACKET = '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016'
PARENT_NOTE = 'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
EXPECTED_ACCEPTANCE = '530e64f0a12506eb1f99f84ceb4ac2ab3b55e2f9b518b4121a46f2e9f4cae74a'
EXPECTED_PARENT_ACCEPTANCE = 'cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726'
EXPECTED_BODIES = {'root_proposal': '86a830e180dae0afba7d13f64bb0d906096e307eb5e3dc5d6e43bf1b52d794c1', 'exposed_review': '498017c60000572ea30408602904cacbafde77e41dc167012a1fb66ac0d582b1'}
EXPECTED_PARENT_SHA256 = '1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b'
EXPECTED_GIT_BASE = '68c531309ac6dae96289aab964213b8c5f55969b'
EXPECTED_SOURCE_DRAFT_FREEZE = 'd0997db66b3b7465a8a02a233a6d0b8c56cb48af6571a3659fa49852cb28700f'
EXPECTED_ROOT_REVIEW_SHA = '0b71a5ba5117ffce4792ede1dc1c36f20f61b35025a62377254d05807b61c923'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_bus_joint_energy_publication_review/record_review.py')
EXPECTED_CANONICAL_REVIEW_SHA = 'aeb6d31ab418abad0e4813a2fa97cf8e9bed8d130fe4d123f17aef5c696d7cc1'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_bus_joint_energy_graph_recovery_review/record_canonical_review.py')
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/bus_joint_energy_moments_2026_10_16.py', 'bytes': 28297, 'sha256': 'd57b31938ab4383449743491b34c260c21ed179ccb77bd40bf8da51f11fecaf9'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bus_joint_energy_graph_recovery_proposal/recovery_common.py', 'bytes': 64260, 'sha256': 'e621a77af0844abb551bbc08135634b63dc3b90c34ad6ca283a69a97251aaedb'}

MANIFEST_SHA256 = '134de6116613655600e3594c34c5157c64b0d42819ce7f06dbf8a13fa3282082'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/BODY_MAP.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/CHECK_RECEIPTS.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/PARENT_BINDING.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/PR_BODY.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/PR_TITLE.txt', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/ROOT_ACCEPTANCE_EXECUTION.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/TRACE_GATE.md', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/1d967c035f607e14c34f548007e168677cc4e864da8f90088fc40c8cfd737d03.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/23df6cf042abb57a1fb67a5c65d2f7262cc492b80c979e3cce489c0f993b137c.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/2d47b5930fa0ecc86d994fc9369e1702922f6c2607b42bc6d349172024c99508.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/3e7accd4ddc80f38f086f75b052a59c2f22668ab59c96b97ce6e1714231ecde4.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/3e92b1e48d89b50326b8132d7c9948e2c93ea8edaf40809453dda2d90b9b35cc.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/498017c60000572ea30408602904cacbafde77e41dc167012a1fb66ac0d582b1.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/530e64f0a12506eb1f99f84ceb4ac2ab3b55e2f9b518b4121a46f2e9f4cae74a.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/642939d2592835977912371e7467d459350fe3d04d524a90772d19f2c23a347f.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/6a70e1335853cd8eb6f93fd19bc33cd53e109f29c29d66bcd8cd2a108209e186.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/84dca7aa9b867df860a855d30c0fb53be8faecdd67773a10308d1e6642dbcc5f.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/86a830e180dae0afba7d13f64bb0d906096e307eb5e3dc5d6e43bf1b52d794c1.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/87996647963fa851729571e2f554ccf4539623dc7a90f51293aeb0f90be5df6d.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/9d94e19bc4768df791242d45e1a1872ba1d84c191ed9109e641afca02f306fed.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/a182e0074ac9b8ed1d9e9e57627d289754252e2969446099ed502e229bf61880.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/bdb0e8d2b513a4b318ad54a6c2627ec4f911fd6f700a962dd659ef1338f2712f.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/cda68e9f414bbc5d5baac5fca8f88a9324691c4e38b5569589ecb81c478458e7.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/db4863ae8fa46cd1ef47fc9d22aa7ca3647432a28994d6942d08fafcf2d1c3b2.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/dd0fa71627a12cb68e4e95b345510cb2f906181b978aa6a056a61badcc8b2b1b.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/e249357df3420515161a5c2b94bea62cdd8ec9040164ddfbaa4b70c81ae39578.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/e606b072b006026700c4b951786636efd03bf1d973e77627ef342705fab0a29c.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/e6b59e5008c14ef15412f79e7a8bfb19526bad3d5d6a40626c7b510109b543fa.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/eb62d6dbf7e94b97631c3e4c1ed46d52bf1a2d4ad34c9092088c09b210bc4955.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/f2cbe56fcffae6606070a394f662eb555d4f251f4fef917659c0e95c66467c9c.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/archive/f5bddd08b5de3c2db3659a9b93fe8908cb0ee709857c866c50d1ea8e4835bca7.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/0581f1a77a8f83af44f5261259f3753941369c7c79b29334f6243fd2bb7dd985.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/08316446377bcffa3057cdcc22c75cee3a90373a32b53c6c6aba49c3f1525a79.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/0b71a5ba5117ffce4792ede1dc1c36f20f61b35025a62377254d05807b61c923.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/17207c45f37f7804dd14b0568df7a0dd7db1931e1e1abf7a7ae3188c707f3f9c.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/1cf758a98da9aac33f76629fa376906cf31c686298439ea2f4b6f96f473ab07e.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/2008797da421621cc4c0b64186a170f871cf17179c10415c3f68e3c66b2d87e0.py', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/26a90a28b3608fc5c18ce357d419e036b77b710195216d92879a599de2bf572e.py', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/3e6413269c7d8fe33fbfe5bc7ae7c47f715c6629712bfc9bd1c4bb024c9dda7a.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/3f053cb2c464ba6acefd2140d528950dfef74b695e034cb8fa8f40ae96e43374.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/47ae26fd1339331be3bc6b17b8d1b3d9d1b5d070c6ebf3b03e8f8eb6a07af764.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/7a35c9d91c8a6ce3e1a5d40273ce4a5d910b21f3d8397079b653b2c6f9f45bc6.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/7c3774886256d5a9761afe177611cc782d04e86181e904279263dbfa7bae1536.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/81dfe35faa968be4d406ea0e55c39846a511487a3dee4f46ac7bd20722ab05e8.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/84dca7aa9b867df860a855d30c0fb53be8faecdd67773a10308d1e6642dbcc5f.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/8f3ef7314395c2e857c013c33aa8ed72677b487355372dd8d8db5d096c734eb8.py', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/917e8648c54449b00be4f3d78d1eb44ce72ca94d672becf38f56ee0ccf6d689e.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/a09a714e022bb1f49c3852f48b5ed9e21e3202e2281a7a8a3f69c85f232bdbff.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/a9f7a242e3f7b8040d1d798f51c39a0508eda37adebc055a6e2e3c57b4bf95b7.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/abb3be119ee187f609f67cee0cb1a4a2b99a31de8ba4d68100166257ada089f3.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/aeb6d31ab418abad0e4813a2fa97cf8e9bed8d130fe4d123f17aef5c696d7cc1.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/bd7bf5ba30fed9837023c5b2ca91cc6544110e68b25d2adc61528e126b848f52.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/ca47a7093657550e706b5aab711953f3848d46a086e4464976ce2f5195c77327.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/d0997db66b3b7465a8a02a233a6d0b8c56cb48af6571a3659fa49852cb28700f.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/d0f70893a0d18bbc216adf741299ffc962c4f6956a49515c2717f8fd1fd5b538.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/d20de3d6266327cc7690d5f645308323033c4a9c63eccd2c693416b5ba674314.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/d5abcfa87df2658380d164b271c41b8fd648c21090e5f79b12d8f05e95b9d119.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/d77e3c7b2960aedd309d3a3cc4a0269b89de944bd284508b7d5b32df9f294233.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/db22483a6237eb3309555f5e2ff883cc056c3f31a053532b6e5a8e2c512d6239.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/f69c102cee953ae5b6cec0c1a4af30a262b1d18ab55a55c79f7a4eb2a4f1f817.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/f73fc1b270a074076f9ae266f22c92c58d1a4bde5a862fa7fd942a394d893846.json', '.claude/science/physics-loops/toe-bus-joint-energy-moments-20261016/binding_sources/fd0c1894c5c174bd9c43b147aec31f11b9a26ec5b83f2c23522d86e0cdc595d2.py', 'docs/BUS_JOINT_ENERGY_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-16.md', 'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md')
METADATA_CHECK_COUNTS = {'passed': 0, 'failed': 0}

def require(ok, message):
    METADATA_CHECK_COUNTS['passed' if ok else 'failed'] += 1
    if not ok:
        raise ValueError(message)

def digest(data):
    return hashlib.sha256(data).hexdigest()

def identity(data, row):
    require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'Byte identity mismatch')

def disk_read(rel):
    path = PurePosixPath(rel)
    require(not path.is_absolute() and '..' not in path.parts, 'Unsafe declared path')
    resolved = (REPO / rel).resolve()
    resolved.relative_to(REPO.resolve())
    return resolved.read_bytes()

def verify_payload(read):
    """Portable metadata checks, callable by the distinct draft inspector."""
    manifest_path = PACKET + '/INPUT_MANIFEST.json'
    raw = read(manifest_path)
    require(digest(raw) == MANIFEST_SHA256, 'Input manifest pin')
    manifest = json.loads(raw)
    require(manifest['schema'] == 'joint_moment_source_inputs_v1', 'Manifest schema')
    rows = manifest['inputs']
    paths = [row['path'] for row in rows]
    require(len(paths) == len(set(paths)), 'Unique declared inputs')
    require(set(AUDIT_INPUT_PATHS) == set(paths) | {manifest_path, PACKET + '/ACTUAL_BINDING.json', PARENT_NOTE}, 'Exact input closure')
    for row in rows:
        identity(read(row['path']), row)
    note = read(NOTE)
    header = note.split(b'---', 2)[1].decode().splitlines()
    for field in ('claim_type: bounded_theorem', 'actual_current_surface_status: conditional-support', 'audit_required_before_effective_retained: true', 'bare_retained_allowed: false'):
        require(field in header, 'Scope field: ' + field)
    require('upstream_dependencies: ["strongly_regular_bus_bounded_theorem_note_2026-10-15"]' in header, 'One actual mathematical parent')
    body_map = json.loads(read(PACKET + '/BODY_MAP.json'))['bodies']
    require({r['name']: r['sha256'] for r in body_map} == EXPECTED_BODIES and len(body_map) == 2, 'Exact two immutable body roles')
    for row in body_map:
        a, b = row['start_byte_inclusive'], row['end_byte_exclusive']
        require(row['container'] == NOTE and isinstance(a, int) and isinstance(b, int) and 0 <= a < b <= len(note), 'Body interval')
        raw = note[a:b]
        identity(raw, row)
        require(note.count(raw) == 1, 'Body occurs exactly once')
    sources = json.loads(read(PACKET + '/SOURCE_MANIFEST.json'))['sources']
    require(len({r['source'] for r in sources}) == len(sources), 'Unique source aliases')
    recovered = {}
    archive = json.loads(read(PACKET + '/ARCHIVE_INDEX.json'))['objects']
    require(len({r['sha256'] for r in archive}) == len(archive), 'Deduplicated archive')
    require({r['sha256'] for r in archive} == {r['sha256'] for r in sources}, 'Exact archive/source closure')
    for row in archive:
        identity(read(row['path']), row)
    for row in sources:
        raw = read(row['recovery_path'])
        identity(raw, row)
        recovered[row['source']] = raw
    def src(name):
        require(name in recovered, 'Known source alias: ' + name)
        return recovered[name]
    def historical_freeze(folder, key):
        freeze = json.loads(src(folder + '/FREEZE.json'))
        for row in freeze[key]:
            p = PurePosixPath(row['path'])
            alias = str(p) if not p.is_absolute() else str(p).split('/renewal_20261015_224023/', 1)[1]
            if not p.is_absolute():
                alias = folder + '/' + alias
            identity(src(alias), row)
    historical_freeze('bus_joint_energy_root_proposal', 'files')
    historical_freeze('bus_joint_energy_independent_check', 'members')
    historical_freeze('bus_joint_energy_root_review', 'files')
    acceptance = src('bus_joint_energy_root_review/QUALIFIED_ACCEPTANCE.json')
    require(digest(acceptance) == EXPECTED_ACCEPTANCE, 'Qualified source acceptance')
    accepted = json.loads(acceptance)
    require(accepted['retained_audit'] is False and accepted['native_realization'] is False, 'Accepted scope retained')
    for key in ('proposal', 'exposed_review', 'qualifications', 'bus_parent_acceptance'):
        row = accepted[key]
        alias = row['path'].split('/renewal_20261015_224023/', 1)[1]
        identity(src(alias), row)
    for row in accepted['actual_evidence']:
        identity(src(row['path'].split('/renewal_20261015_224023/', 1)[1]), row)
    rbase = 'bus_joint_energy_independent_check/exact_check/run_01/'
    launch = json.loads(src(rbase + 'LAUNCH.json'))
    receipt = json.loads(src(rbase + 'EXECUTION.json'))
    require(all(receipt[k] == v for k, v in launch.items()), 'Unchanged launch/result linkage')
    require(receipt['exit_code'] == 0 and receipt.get('timed_out', False) is False, 'Actual original result')
    require(receipt['argv'][1] == '-B' and len(receipt['argv']) == 3 and receipt['argv'][2] == receipt['source_at_launch'], 'Actual child argv with interpreter flag')
    require(Path(receipt['argv'][0]).name.startswith('python'), 'Historical Python interpreter')
    require(digest(src(rbase + 'check_joint_moments.at_launch.py')) == receipt['source_sha256'], 'Executed scientific source capture')
    require(digest(src(rbase + 'launcher.at_launch.py')) == receipt['launcher_source_sha256'], 'Original launcher capture')
    require(digest(src(rbase + 'SOURCE_MANIFEST.at_launch.json')) == receipt['source_manifest_sha256'], 'Launch-time source manifest')
    for key, filename in [('stdout', 'stdout.json'), ('stderr', 'stderr.txt')]:
        require(digest(src(rbase + filename)) == receipt[key + '_sha256'], 'Historical complete stream ' + key)
    require(src(rbase + 'stderr.txt') == b'', 'Historical empty error stream')
    require('-B' not in receipt['launcher_argv'], 'Historical secondary annotation remains uncorrected')
    disclosure = src('bus_joint_energy_independent_check/SOURCE_EXPOSURE.md')
    require(b'retrospective' in disclosure and b'python3 -B run_exact_check.py' in disclosure, 'Separate provenance disclosure retained')
    parents = json.loads(read(PACKET + '/PARENT_BINDING.json'))
    require(len(parents['canonical_parents']) == 1 and parents['transitive_premises'] == [], 'One direct parent; no unrelated imports')
    parent = parents['canonical_parents'][0]
    require(parent['path'] == PARENT_NOTE and parent['sha256'] == EXPECTED_PARENT_SHA256, 'Published canonical parent pin')
    identity(read(PARENT_NOTE), parent)
    require(digest(src('strongly_regular_bus_root_review/QUALIFIED_ACCEPTANCE.json')) == EXPECTED_PARENT_ACCEPTANCE, 'Parent qualification')
    publication = json.loads(src('publication_integration/strongly_regular_bus/PUBLICATION.json'))
    require(publication['number'] == 9631 and publication['headRefOid'] == '68c531309ac6dae96289aab964213b8c5f55969b' and publication['isDraft'] is False, 'Actual dependency regular-PR receipt')
    require(publication['source_note']['sha256'] == EXPECTED_PARENT_SHA256, 'Publication/parent source linkage')
    state = json.loads(read(PACKET + '/PUBLICATION_STATE.json'))
    require(all(state[k] is None for k in ('canonical_integration', 'current_base_observation', 'primary_execution', 'publication_action', 'retained_audit')), 'Historical draft placeholders stay null')
    require(state['scientific_programs_run_this_draft'] == 0, 'No scientific replay')
    verify_acceptance_execution(read)
    return {'body_map': body_map, 'parent_binding': parents, 'note_sha256': digest(note), 'source_count': len(sources), 'archive_count': len(archive)}

def verify_actual_binding(read, checked):
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40,'Actual base and root review are unbound')
    def blob(row):
        require(row['path'] in AUDIT_INPUT_PATHS,'Declared binding evidence')
        raw=read(row['path']);identity(raw,row);return raw
    def execution(evidence,python_source):
        receipt=json.loads(blob(evidence['execution']))
        require(receipt['exit_code']==0 and receipt['start_utc']<=receipt['end_utc'] and receipt['elapsed_seconds']>=0,'Captured successful execution required')
        for key in ('recorder','stdout','stderr'):identity(blob(evidence[key]),receipt[key])
        require(blob(evidence['stderr'])==b'','Captured empty error stream')
        if python_source:
            identity(blob(evidence['source']),receipt['child_source_at_launch']);identity(blob(evidence['source']),receipt['source_capture'])
            require(receipt['argv'][1]==receipt['child_source_at_launch']['path'],'Actual launched review source')
        else:require(receipt['child_source_at_launch'] is None,'Direct command has no invented Python source')
        return receipt,json.loads(blob(evidence['stdout'])) if python_source else blob(evidence['stdout'])
    actual=json.loads(read(PACKET+'/ACTUAL_BINDING.json'))
    require(actual['kind']=='root_reviewed_canonical_binding' and actual['root_read_complete'] is True,'Actual root canonical review required')
    require(actual['note_sha256']==checked['note_sha256'] and actual['git_base']==EXPECTED_GIT_BASE,'Canonical note/base linkage')
    require(actual['source_acceptance_sha256']==EXPECTED_ACCEPTANCE,'Current source decision linkage')
    seal_raw=blob(actual['source_proposal_freeze']);seal=json.loads(seal_raw)
    require(digest(seal_raw)==EXPECTED_SOURCE_DRAFT_FREEZE,'Exact frozen source draft')
    require(seal['scientific_programs_run_this_draft']==0 and seal['primary_execution'] is None,'Frozen draft scope')
    draft_raw=blob(actual['source_draft_body_map']);draft_map=json.loads(draft_raw)['bodies']
    rows=[r for r in seal['files'] if r['path']=='proposal/'+PACKET+'/BODY_MAP.json']
    require(len(rows)==1,'Unique original body map');identity(draft_raw,rows[0])
    ids=lambda rows:[(r['name'],r['bytes'],r['sha256']) for r in rows]
    require(ids(draft_map)==ids(checked['body_map']),'Original and relocated body identities')
    root_ev=actual['root_review_evidence'];root_raw=blob(root_ev['review']);root=json.loads(root_raw)
    require(digest(root_raw)==EXPECTED_ROOT_REVIEW_SHA,'Exact root review identity')
    receipt,result=execution(root_ev,True)
    require(tuple(receipt['argv'])==EXPECTED_ROOT_REVIEW_COMMAND,'Exact root review command')
    identity(root_raw,result['review'])
    require(root['kind']=='root_source_publication_review' and root['root_read_complete'] is True,'Actual substantive draft review')
    require(root['source_draft_freeze']['sha256']==EXPECTED_SOURCE_DRAFT_FREEZE and root['body_pins']==draft_map and root['parent_binding']==checked['parent_binding'],'Draft review source and parent linkage')
    require(root['scientific_programs_run_this_review']==root['primary_runs']==root['historical_programs_replayed']==0,'Source-only root review')
    canon_ev=actual['canonical_review_evidence'];canon_raw=blob(canon_ev['review']);canon=json.loads(canon_raw)
    require(digest(canon_raw)==EXPECTED_CANONICAL_REVIEW_SHA,'Exact canonical review identity')
    receipt,result=execution(canon_ev,True)
    require(tuple(receipt['argv'])==EXPECTED_CANONICAL_REVIEW_COMMAND,'Exact canonical review command')
    identity(canon_raw,result['review'])
    require(canon['root_read_complete'] is True and canon['bound_note_sha256']==checked['note_sha256'],'Canonical note review linkage')
    require(canon['canonical_body_pins']==checked['body_map'] and canon['parent_binding']==checked['parent_binding'],'Canonical body and parent scope')
    require(canon['source_draft_freeze_sha256']==EXPECTED_SOURCE_DRAFT_FREEZE and canon['source_draft_review_sha256']==EXPECTED_ROOT_REVIEW_SHA and canon['git_base']==EXPECTED_GIT_BASE,'Canonical draft/base linkage')
    require(canon['prebinding_primary']==EXPECTED_PREBINDING_PRIMARY and canon['integration_common']==EXPECTED_INTEGRATION_COMMON,'Canonical helper/common review linkage')
    base=json.loads(blob(actual['base_observation']))
    require(base['observed_commit']==EXPECTED_GIT_BASE and base['source_revision_verified'] is True,'Actual local base identity')
    receipt,stdout=execution(base['execution_evidence'],False)
    require([Path(receipt['argv'][0]).name,*receipt['argv'][1:]]==['git','rev-parse','HEAD'],'Actual base observation command')
    require(stdout.decode().strip()==EXPECTED_GIT_BASE,'Actual base observation stdout')
    receipt,stdout=execution(actual['parent_pr_observation'],False);parent=json.loads(stdout)
    require(parent['number']==9631 and parent['headRefOid']==EXPECTED_GIT_BASE and parent['isDraft'] is False,'Actual base PR identity')
    require(b'canonical_parent_binding_complete: true\n' in read(NOTE).split(b'---',2)[1],'Bound canonical header')
    require(actual['retained_audit'] is False and actual['new_scientific_execution'] is False,'No invented retention or science')

def main():
    checked = verify_payload(disk_read)
    verify_actual_binding(disk_read, checked)
    print(json.dumps({'result': 'source_integrity_verified', 'scientific_programs_run_this_primary': 0, 'historical_programs_replayed': 0, 'mathematics_or_retention_certified': False, **checked}, sort_keys=True))
    print('per_element: exact source identities only; no physical element executed')
    print('per_site: complete-space text preserved; no physical site measured')
    print('per_mode: same-installed-K moment contract retained; no science replay')
    print('per_block: historical executed source and unchanged streams verified only')
    print('lattice_wide: native suppliers and independent retained audit remain separate')



def verify_acceptance_execution(read):
    spec = json.loads(read(PACKET + '/ROOT_ACCEPTANCE_EXECUTION.json'))
    def blob(key):
        row=spec[key];require(row['path'] in AUDIT_INPUT_PATHS,'Declared acceptance evidence');raw=read(row['path']);identity(raw,row);return raw
    receipt=json.loads(blob('execution'))
    require(receipt['exit_code']==0 and receipt['start_utc']<=receipt['end_utc'] and receipt['elapsed_seconds']>=0,'Actual acceptance execution')
    require(receipt['argv'][1]==receipt['child_source_at_launch']['path'],'Actual acceptance source path')
    identity(blob('source'),receipt['child_source_at_launch']);identity(blob('source'),receipt['source_capture'])
    for key in ('recorder','stdout','stderr'):identity(blob(key),receipt[key])
    require(blob('stderr')==b'','Actual acceptance error stream')
    result=json.loads(blob('stdout'))
    identity(blob('acceptance'),result['acceptance']);identity(blob('freeze'),result['freeze'])
    require(digest(blob('acceptance'))==EXPECTED_ACCEPTANCE,'Actual acceptance decision output')



if __name__ == '__main__':
    try:
        main()
    except Exception:
        if METADATA_CHECK_COUNTS['failed'] == 0:
            METADATA_CHECK_COUNTS['failed'] += 1
        raise
    finally:
        print('metadata_check_counts_only: identities and provenance, not scientific proof')
        print(f"TOTAL: PASS={METADATA_CHECK_COUNTS['passed']} FAIL={METADATA_CHECK_COUNTS['failed']}")

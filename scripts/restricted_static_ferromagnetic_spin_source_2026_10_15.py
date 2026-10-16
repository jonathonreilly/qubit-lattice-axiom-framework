"""Source-integrity proposal only; no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015"
EXPECTED_PARENTS = {}
EXPECTED_BODIES = {'author_restricted_body': '47cda48195580320d92851332bce37d09f8703294acadb571b69d0dc23a48c15', 'independent_restricted_body': '687a28553a1588265906ca0e64a8a18c8caf18027003343aed5708b43b2a0222', 'exposed_reconciliation_body': '85b54da82b54f7accb199d9c4121e5701f229ab91176ed1b0d249e7ee9b448c9'}
EXPECTED_ACCEPTANCE = "32d142a282e1347449f9de98f5749c03f9d9a78dccca4c86608f472401ed7aa2"
EXPECTED_GIT_BASE = '23a84c17353ea13dab449ca9a37800b5e4defcb4'
MANIFEST_SHA256 = '06765f393bf3985a3910765b6f6c908066cdecce91690a9ec6d6a4ef83b351a6'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/CHECK_RECEIPTS.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PARENT_BINDING.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/17d55edc81a1ac58a2f837d45825b20cb772cd9264d60b33d4e4cdee283d6f6f.py', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/1924e6cf8eadbe4ed6e5a6259f3dee18107d820beba689fd5a252978aedb5062.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/1c2276e254cfaa6e45ac3f3e91e7bf31e6607a8dff62af0543e7b0c2c4c174b3.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/26d778ca184624a2017232b6b618b7f713f90f31b0502f41ef7c9b7bbb429405.py', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/2d1cc758f972302a865cbabc6f1ae9806a8d3908dfb10087a479e0678d783747.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/382fde32f249326d287662d4d43f96625f0dd6a5bf23b4102ae836335710e319.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/3bfc0337f29c12719238fbbbfecca939ec41da19d1707d76879b95371f7c259e.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/4cd2e1578fdc6069b3dbe75bafcd4d371cac378bb44a8f1da1ac93d05f821ba5.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/4eae7034bed1a87f8d8222877b1956fb670bb35fc0346ef021b8a5c830cf6ee8.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/4fa10f4ca90f7b34d7ab5a24ae77921b7ec4ee7ac7714a1f59575e64356c61cd.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/5093a239b1b0fca7570ef3e2a144f24a4e82d8a71d43b5c141a42dd530b5c4d4.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/5bfd0675f1f3d65d8c9fefd7a9a5c6e66570eb1923ba24324c9f418cb1e867b2.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/60f86037f608b8e22c9e98252c6df21821d2933ef7ed872927fd28da823b9130.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/61d51004f3c7510ccdf4a6d47562977fb83babede3cddb3de9163d986b0783d2.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/6de6c09b2600f6a328620f4cf38b83425d945934682df18083b971ec739948ba.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/74f063a0891de7e7b9b575f9d80ed3f875e14b7a332d72c41daeff28b535f985.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/8cf3a9a04b5ceb22e440f05da8b8d1fb3bf03ff92b9ca6342b770d859cf5a177.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/903419125264f0e6facf4e8f2d9b3db9c967e06606de646fa02bc2eddb002154.py', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/919a4ab1cc334b0fb8ba48ddcd6aedaad15bf5940d1d8a8c50d6c3d1c0948c10.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/92a27abfa0921598d9b1b53ee8c3616116b83da767af0412aed3092f7c4279e2.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/e11956017f7560a9a1de793ea82002f506748d1bd172615501065999833cf4f8.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/e9529b5bee27df7f1be98418f1b0781b29b4cde279ec348829413791267d6c64.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/e9f6b186a1268235bc54ccfbcfee2d2b928c4977870ae486c2db6e2e930b3e2b.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/binding_sources/f57f92c98a46c506d51269cd6791e45d71f6c3921d748a9a2d7184b3b4ad5394.json', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/29d85314d7f00e28733c345be0a04ceef436736dbd2552d0b1e174b6a3a1502b.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/317e24380e9f3c942d5a10c667c3c484ccf3108d69979cbc52799def5ba5dab5.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/32d142a282e1347449f9de98f5749c03f9d9a78dccca4c86608f472401ed7aa2.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/36a03f21a730ef935d3793251e75b31c99fe2691d346e30f507649607d7ce7d2.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/3c3de9fc9a949601697552c2e2e3a62346ef0126eaa0263763b64497ba35f4b0.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/46d0eeda39b7eddb7ade4984969d346dbb4c4a8112a5c7365bd63706226b828c.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/4793d0558db1789f613f5be6b6155feba1924fdb103e4b468c0cd710f67b2840.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/483fb05450002667a2deec90a7f42a22c001fc34dba400e7dbd0a9c83dd5c158.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/5491d4a68ba50bd555a6d42c438bb82df2f9639225829c30af69f6f7f5ac1679.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/8051d6d84e1f7f22b5633eb79f4e4c60827cb87e38f36fcbf8ae8ba2839fcf7a.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/95cbf2e175253d3e5f7e0e2b4122f81686385b18c7b0d84118883bc3d896a020.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/9d0edfb643c5744a429ebd83b482d9e573a9bde3a72a137081548b2524d41b8d.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/a94c5b95758e9444cf6caa198ef3a0b2be716aaea9c7f9f729dfd9b2c739eafb.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/af2d45e28f2dde8a97112bcbf62f1e456fa0a85687c9b34cc50ac1edfc3bd976.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/b814eb25e584e3369087d2b75f0265a352444fabae35dcb973231ce5e49221c2.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/bc39634701265ab7047f7497b209e5e4a3c9f246d628357e59092914baf5bb83.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/c4385aa27987e0c209a02fbe308cca33d9cf804b934df8407255fbb42305bd3a.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/cbbeb30362a70f320919ebc0cbb9c1b4672828a48b1d7222c96630f2f1a9ea3c.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/d33cd8e3bc3f93f9b12abf8dda65d2f21b99b4887f0ded3caa1fd76506eebc78.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/dcab7a72c287fe9cd06b2de4997d35051aa67e425be9d6c8703055edae44ba11.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/e88c31d5488b07bb1b15ec09bb2c08e0b92d9fd8c2a926d99d20dd4343e357f2.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/e9734acd5bfa0a21521fd1ada40710e6ebcda222c0b3ef52932cbe31468992b2.blob', '.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/source_recovery/f6b4883e8828851fca18434dda0b422aee137e88c499fe2818f28b17ed5de666.blob', 'docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md')
METADATA_CHECK_COUNTS = {"passed": 0, "failed": 0}

EXPECTED_ROOT_REVIEW_SHA = 'e9f6b186a1268235bc54ccfbcfee2d2b928c4977870ae486c2db6e2e930b3e2b'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_restricted_spin_publication_review/record_review.py')
EXPECTED_CANONICAL_REVIEW_SHA = '919a4ab1cc334b0fb8ba48ddcd6aedaad15bf5940d1d8a8c50d6c3d1c0948c10'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_restricted_spin_integration_review/record_canonical_review.py')
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/restricted_static_ferromagnetic_spin_source_2026_10_15.py', 'bytes': 37134, 'sha256': 'f71bc962a74626ba61eae7d95a6731daff6c4d271e0aeecf86d13ca374364e74'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/restricted_spin_integration_proposal/restricted_spin_common.py', 'bytes': 55630, 'sha256': '903419125264f0e6facf4e8f2d9b3db9c967e06606de646fa02bc2eddb002154'}
EXPECTED_BASE_PR = 9627
EXPECTED_BASE_BRANCH = 'physics-loop/toe-bounded-slew-compiler-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-autonomous-compiler-composition-20261015'
EXPECTED_REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
EXPECTED_PARENT_BINDING = {'canonical_parents': [], 'transitive_premises': [], 'preparation_release_intervals': [], 'scope': 'The accepted restricted theorem proves its finite spin gap and reduction in these bodies. Historical compiler, mediator and clock references in unaccepted architecture sections are context, not mathematical dependencies of this theorem. Supplied source preparation, geometry, timing and isolation remain assumptions, not parent theorems.'}
EXPECTED_DIRECT_PARENTS = ()
EXPECTED_SOURCE_BODY_PINS = [{'name': 'author_restricted_body', 'container': 'docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 18877, 'end_byte_exclusive': 50590, 'bytes': 31713, 'sha256': '47cda48195580320d92851332bce37d09f8703294acadb571b69d0dc23a48c15'}, {'name': 'independent_restricted_body', 'container': 'docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 50767, 'end_byte_exclusive': 67550, 'bytes': 16783, 'sha256': '687a28553a1588265906ca0e64a8a18c8caf18027003343aed5708b43b2a0222'}, {'name': 'exposed_reconciliation_body', 'container': 'docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 67727, 'end_byte_exclusive': 85060, 'bytes': 17333, 'sha256': '85b54da82b54f7accb199d9c4121e5701f229ab91176ed1b0d249e7ee9b448c9'}]
EXPECTED_SOURCE_MAP_SHA = '5bfd0675f1f3d65d8c9fefd7a9a5c6e66570eb1923ba24324c9f418cb1e867b2'
EXPECTED_SOURCE_FREEZE = 'e9529b5bee27df7f1be98418f1b0781b29b4cde279ec348829413791267d6c64'
EXPECTED_DRAFT_FILES = {'proposal/.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/BODY_MAP.json': {'bytes': 1136, 'sha256': '5bfd0675f1f3d65d8c9fefd7a9a5c6e66570eb1923ba24324c9f418cb1e867b2'}, 'proposal/.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PARENT_BINDING.json': {'bytes': 450, 'sha256': 'fb786eaf8226ff3ede70ce821e6e827f0924c65f95b4515d162faa1c6b8f7249'}, 'proposal/.claude/science/physics-loops/toe-restricted-static-ferromagnetic-spin-source-20261015/PUBLICATION_STATE.json': {'bytes': 491, 'sha256': 'b5f44e6c4523defa1dfcf61975fab4b5686308a08913863babfc30b1df557be3'}, 'proposal/docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 85060, 'sha256': '66648149374f77e7bfba4714abf3f379e0a372464ace5348084bbfdeb68fd3d2'}, 'proposal/scripts/restricted_static_ferromagnetic_spin_source_2026_10_15.py': {'bytes': 20971, 'sha256': '9f571d129b3769dc5d7657688ec3383ec7e7afd4915248408e3ef442ab5c6591'}}
EXPECTED_DRAFT_CANONICAL = {'proposal/docs/RESTRICTED_STATIC_FERROMAGNETIC_SPIN_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 85060, 'sha256': '66648149374f77e7bfba4714abf3f379e0a372464ace5348084bbfdeb68fd3d2'}, 'proposal/scripts/restricted_static_ferromagnetic_spin_source_2026_10_15.py': {'bytes': 20971, 'sha256': '9f571d129b3769dc5d7657688ec3383ec7e7afd4915248408e3ef442ab5c6591'}}
EXPECTED_PUBLICATION_STATE = {'kind': 'historical_source_only_draft', 'canonical_integration': None, 'git_base': None, 'root_publication_review': None, 'primary_execution': None, 'cache_execution': None, 'mutation_execution': None, 'graph_execution': None, 'publication_action': None, 'retained_audit': None, 'scientific_programs_run_this_draft': 0, 'historical_scientific_programs_replayed': 0, 'source_acceptance_sha256': '32d142a282e1347449f9de98f5749c03f9d9a78dccca4c86608f472401ed7aa2'}
EXPECTED_HELPER = 'scripts/restricted_static_ferromagnetic_spin_source_2026_10_15.py'
RECOVERY_TABLES = {'SOURCE_MANIFEST.json': 'sources'}
EXPECTED_HISTORICAL_LAUNCHES = ['d33cd8e3bc3f93f9b12abf8dda65d2f21b99b4887f0ded3caa1fd76506eebc78', 'b814eb25e584e3369087d2b75f0265a352444fabae35dcb973231ce5e49221c2']
EXPECTED_INDEPENDENT_OMISSIONS = ['cwd', 'process exit', 'resolved interpreter', 'exact process exit UTC']
EXPECTED_INDEPENDENT_QUALIFICATION = 'Command, cwd and tool exit are separately transcribed retrospectively; original launch record stays unchanged.'
EXPECTED_QUALIFICATIONS = 'dcab7a72c287fe9cd06b2de4997d35051aa67e425be9d6c8703055edae44ba11'

def require(ok, message):
    METADATA_CHECK_COUNTS["passed" if ok else "failed"] += 1
    if not ok: raise ValueError(message)
def digest(data): return hashlib.sha256(data).hexdigest()
def safe(rel):
    path=PurePosixPath(rel)
    require(not path.is_absolute() and ".." not in path.parts,"Unsafe package input path")
    result=(REPO/rel).resolve()
    result.relative_to(REPO.resolve())
    return result
def identity(data,row):
    require(len(data)==row["bytes"] and digest(data)==row["sha256"],"Input identity mismatch")
def read_json(rel): return json.loads(safe(rel).read_bytes())
def interval(row):
    data=safe(row["container"]).read_bytes()
    a,b=row["start_byte_inclusive"],row["end_byte_exclusive"]
    require(isinstance(a,int) and isinstance(b,int) and 0<=a<b<=len(data),"Invalid byte interval")
    raw=data[a:b];identity(raw,row)
    require(data.count(raw)==1,"Raw source must occur exactly once")
    return raw

def bound_blob(row):
    require(isinstance(row,dict) and row["path"] in AUDIT_INPUT_PATHS,"Binding evidence must be declared")
    raw=safe(row["path"]).read_bytes();identity(raw,row)
    return raw

def execution_evidence(evidence, python_source, expected_command=None):
    receipt=json.loads(bound_blob(evidence['execution']))
    require(receipt.get('exit_code')==0 and isinstance(receipt.get('argv'),list),'Captured successful execution required')
    require(isinstance(receipt.get('start_utc'),str) and isinstance(receipt.get('end_utc'),str) and receipt['start_utc']<=receipt['end_utc'],'Captured execution time schema')
    require(isinstance(receipt.get('elapsed_seconds'),(int,float)) and receipt['elapsed_seconds']>=0,'Captured execution duration')
    identity(bound_blob(evidence['recorder']),receipt['recorder'])
    stdout=bound_blob(evidence['stdout']);stderr=bound_blob(evidence['stderr'])
    identity(stdout,receipt['stdout']);identity(stderr,receipt['stderr'])
    require(stderr==b'','Unexpected evidence error stream')
    if python_source is True:
        if expected_command is None:
            expected_command=EXPECTED_ROOT_REVIEW_COMMAND if evidence['review']['sha256']==EXPECTED_ROOT_REVIEW_SHA else EXPECTED_CANONICAL_REVIEW_COMMAND
        identity(bound_blob(evidence['source']),receipt['child_source_at_launch'])
        identity(bound_blob(evidence['source']),receipt['source_capture'])
        require(tuple(receipt['argv'])==expected_command,'Exact root source-review command')
        require(Path(receipt['argv'][0]).name.startswith('python'),'Python root source-review command')
        require(len(receipt['argv'])>=2 and receipt['argv'][1]==receipt['child_source_at_launch']['path'] and receipt['argv'][1].endswith('.py'),'Root source-review script path')
    elif python_source=='git_head':
        require(receipt['child_source_at_launch'] is None and receipt['argv']==['git','rev-parse','HEAD'],'Actual local base observation command')
        return receipt,stdout
    else:
        require(receipt['child_source_at_launch'] is None,'Direct PR observation has no Python child source')
        require(receipt['argv']==['gh','pr','view',str(EXPECTED_BASE_PR),'--repo',EXPECTED_REPOSITORY,'--json','number,state,isDraft,headRefOid,headRefName,baseRefName,url'],'Actual base observation command')
    return receipt,stdout

def body_identities(rows):
    return [(row["name"],row["bytes"],row["sha256"]) for row in rows]

def reviewed_operation(evidence):
    raw=bound_blob(evidence["review"])
    _,stdout=execution_evidence(evidence,True)
    observed=json.loads(stdout)
    require(observed["review"]["sha256"]==digest(raw),"Captured review operation linkage")
    return json.loads(raw)

def recovered(row):
    recovery=row["recovery"]
    if recovery["kind"]=="blob":
        require(recovery["path"] in AUDIT_INPUT_PATHS,"Recovery blob must be declared")
        data=safe(recovery["path"]).read_bytes();identity(data,row);return data
    if recovery["kind"] in {"body_interval","external_body_interval"}:
        return interval({**recovery,"bytes":row["bytes"],"sha256":row["sha256"]})
    require(recovery["kind"]=="external_pinned" and recovery["path"] in EXPECTED_PARENTS,"Known external parent only")
    data=safe(recovery["path"]).read_bytes();identity(data,row);return data

def historical_receipt(row):
    launch=json.loads(recovered(row["launch"]))
    source=recovered(row["source"])
    if row["schema"]=="author_sanity_v1":
        receipt=json.loads(recovered(row["receipt"]))
        require(receipt["returncode"]==0,"Original author disposition retained")
        require(all(receipt[k]==v for k,v in launch.items()),"Original author launch/result linkage")
        require(launch["command"][1]==row["source"]["source"],"Original author captured source was the launched path")
        require(len(source)==launch["source_bytes"] and digest(source)==launch["source_sha256"]==receipt["source_after_sha256"],"Original author source identity")
        require(digest(recovered(row["recorder"]))==launch["launcher_sha256"],"Original author launcher identity")
        freeze=json.loads(recovered(row["freeze"]))
        for key in ["launch","receipt","source","recorder","stdout","stderr"]:
            part=row[key];matches=[r for r in freeze["files"] if r["path"]==part["source"]]
            require(len(matches)==1,"Author original freeze membership");identity(recovered(part),matches[0])
        require(recovered(row["stderr"])==b"","Original author error stream retained")
        require(row["scope"]=="finite_floating_point_author_sanity_only","Author scope")
    else:
        require(row["schema"]=="independent_program_launch_v1","Known original provenance schema")
        require(launch["argv"]==["finite_checks.py"],"Original incomplete argv retained")
        require("cwd" not in launch and "exit_code" not in launch and "returncode" not in launch,"Original launch omissions remain explicit")
        require(digest(source)==launch["script_sha256"],"Independent original source hash")
        for key,field in [("derivation_at_launch","derivation_sha256"),("exposure_at_launch","exposure_sha256")]:
            require(digest(recovered(row[key]))==launch[field],"Independent original input capture")
        require(recovered(row["results"])==recovered(row["full_log"]),"Original independent result/log equality")
        retrospective=json.loads(recovered(row["retrospective_manifest"]))["execution_record_retrospective"]
        require(retrospective["classification"]=="Retrospective transcription of existing tool messages; not a launch-time receipt; no replay.","Retrospective provenance label")
        require(retrospective["exec_arguments"]["cmd"]=="python3 finite_checks.py > FINITE_CHECK_FULL.log 2>&1","Actual retrospectively transcribed command")
        require(retrospective["exec_arguments"]["workdir"]==str(Path(row["launch"]["source"]).parent),"Actual retrospective cwd")
        require(retrospective["initial_result"]["session_id"]==retrospective["poll_arguments"]["session_id"]==27634 and retrospective["poll_result"]["exit_code"]==0,"Recorded session and exit preserved")
        require(retrospective["exact_process_exit_utc"]=="not recorded" and retrospective["resolved_interpreter_path"]=="not recorded by that execution; not reconstructed","Absent interpreter and exit time not fabricated")
        require(retrospective["original_launch_receipt_unchanged"] is True and row["scope"]=="finite_floating_point_independent_predicates_only","Original independent scope")

def check_receipt_members(value, sources):
    if isinstance(value, dict):
        if 'recovery' in value:
            require(value in sources, 'Historical check/source recovery linkage')
        for child in value.values():
            check_receipt_members(child, sources)
    elif isinstance(value, list):
        for child in value:
            check_receipt_members(child, sources)

def main():
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and all(c in '0123456789abcdef' for c in EXPECTED_GIT_BASE),'Actual Git base is unbound')
    require(isinstance(EXPECTED_ROOT_REVIEW_SHA,str) and len(EXPECTED_ROOT_REVIEW_SHA)==64 and isinstance(EXPECTED_ROOT_REVIEW_COMMAND,tuple),'Actual root wrapper review is unbound')
    manifest_path=PACKET+'/INPUT_MANIFEST.json';raw=safe(manifest_path).read_bytes()
    require(digest(raw)==MANIFEST_SHA256,'Input manifest identity');manifest=json.loads(raw)
    require(manifest['schema']=='source_integrity_inputs_v1','Input schema')
    rows=manifest['inputs'];require(len({r['path'] for r in rows})==len(rows),'Unique inputs')
    expected={r['path'] for r in rows}|{manifest_path,PACKET+'/ACTUAL_BINDING.json'}|set(EXPECTED_PARENTS)
    require(set(AUDIT_INPUT_PATHS)==expected and len(AUDIT_INPUT_PATHS)==len(expected),'Literal declared input closure')
    for row in rows:identity(safe(row['path']).read_bytes(),row)
    note=safe(NOTE).read_bytes();header=note.split(b'---',2)[1].decode().splitlines()
    for field in ['canonical_parent_binding_complete: true','claim_type: bounded_theorem','actual_current_surface_status: conditional-support','audit_required_before_effective_retained: true','bare_retained_allowed: false']:
        require(field in header,'Scope/binding field: '+field)
    bodies=read_json(PACKET+'/BODY_MAP.json')['bodies']
    require({r['name']:r['sha256'] for r in bodies}==EXPECTED_BODIES and len(bodies)==len(EXPECTED_BODIES),'Exact current source roles')
    by_name={r['name']:r for r in bodies}
    for row in bodies:require(row['container']==NOTE,'Current body container');interval(row)
    binding_spec=read_json(PACKET+'/PARENT_BINDING.json')
    require(binding_spec==EXPECTED_PARENT_BINDING,'Exact parent and preparation binding')
    parents=binding_spec['canonical_parents']+binding_spec['transitive_premises']
    require({r['path']:(r['bytes'],r['sha256'],r['claim_id']) for r in parents}==EXPECTED_PARENTS,'Exact direct and transitive parent identity')
    require(tuple(r['path'] for r in binding_spec['canonical_parents'])==EXPECTED_DIRECT_PARENTS,'Exact direct mathematical parents')
    for row in parents:
        identity(safe(row['path']).read_bytes(),row)
        for part in row['accepted_body_intervals']:require(part['container']==row['path'],'Parent interval container');interval(part)
    for part in binding_spec['preparation_release_intervals']:interval(part)
    sources=read_json(PACKET+'/SOURCE_MANIFEST.json')['sources']
    require({r['sha256'] for r in sources if r['role']=='qualified_source_acceptance'}=={EXPECTED_ACCEPTANCE},'Qualified source decision')
    require({r['sha256'] for r in sources if r['role']=='controlling_source_qualifications'}=={EXPECTED_QUALIFICATIONS},'Controlling source qualifications')
    for row in sources:
        recovered(row);loc=row['recovery']
        if loc['kind']=='body_interval':
            require(loc['name'] in by_name,'Source body-map linkage');body=by_name[loc['name']]
            require(all(loc[key]==body[key] for key in ('container','start_byte_inclusive','end_byte_exclusive')) and row['bytes']==body['bytes'] and row['sha256']==body['sha256'],'Source body-map linkage')
    for filename,key in RECOVERY_TABLES.items():
        if filename=='SOURCE_MANIFEST.json':continue
        for row in read_json(PACKET+'/'+filename)[key]:
            loc=row.get('recovery')
            if loc is not None:require(any(row['bytes']==r['bytes'] and row['sha256']==r['sha256'] and loc==r['recovery'] for r in sources),'Selected member/source recovery linkage')
    selection=read_json(PACKET+'/RECOVERY_SELECTION.json')
    for row in selection['selected_originals']:
        require(any(row['path']==source['source'] and row['role']==source['role'] and row['bytes']==source['bytes'] and row['sha256']==source['sha256'] for source in sources),'Selected original/source identity linkage')
    checks=read_json(PACKET+'/CHECK_RECEIPTS.json')['records']
    require([r['launch']['sha256'] for r in checks]==EXPECTED_HISTORICAL_LAUNCHES,'Exact historical check launch selection')
    for record in checks:
        check_receipt_members(record,sources)
        if record['schema']=='independent_program_launch_v1':
            require(record['missing_original_fields']==EXPECTED_INDEPENDENT_OMISSIONS and record['qualification']==EXPECTED_INDEPENDENT_QUALIFICATION,'Original incomplete provenance qualification')
        historical_receipt(record)
    archive=read_json(PACKET+'/ARCHIVE_INDEX.json')['objects']
    require(len({r['sha256'] for r in archive})==len(archive),'Deduplicated recovery')
    require({r['sha256'] for r in archive}=={r['sha256'] for r in sources if r['recovery']['kind']=='blob'},'Archive/source recovery membership')
    for row in archive:identity(safe(row['path']).read_bytes(),row)
    actual=read_json(PACKET+'/ACTUAL_BINDING.json')
    require(actual['kind']=='root_reviewed_canonical_binding' and actual['root_read_complete'] is True and actual['canonical_parent_binding_complete'] is True,'Actual root wrapper review required')
    require(actual['note_sha256']==digest(note) and actual['git_base']==EXPECTED_GIT_BASE,'Actual note/base linkage')
    require(actual['base_branch']==EXPECTED_BASE_BRANCH and actual['source_acceptance_sha256']==EXPECTED_ACCEPTANCE,'Actual source decision linkage')
    require(actual['source_body_pins']==EXPECTED_SOURCE_BODY_PINS and actual['raw_bodies']==bodies and actual['parent_binding']==binding_spec,'Original and relocated body binding')
    source_map_raw=bound_blob(actual['source_draft_body_map'])
    require(digest(source_map_raw)==EXPECTED_SOURCE_MAP_SHA,'Exact frozen draft body-map identity')
    source_map=json.loads(source_map_raw)
    require(source_map['bodies']==EXPECTED_SOURCE_BODY_PINS,'Exact frozen draft body map')
    require(actual['new_scientific_execution'] is False and actual['retained_audit'] is False,'Source binding cannot grant scientific retention')
    require(actual['source_proposal_freeze']['sha256']==EXPECTED_SOURCE_FREEZE,'Exact source proposal freeze')
    freeze=json.loads(bound_blob(actual['source_proposal_freeze']))
    require(freeze['scientific_programs_run_this_draft']==0 and freeze['primary_execution'] is None,'Original source-only freeze scope')
    for path,expected_pin in EXPECTED_DRAFT_FILES.items():
        matches=[r for r in freeze['files'] if r['path']==path]
        require(len(matches)==1 and all(matches[0][key]==expected_pin[key] for key in ('bytes','sha256')),'Historical proposal seal membership')
    evidence=actual['root_review_evidence'];raw_review=bound_blob(evidence['review'])
    require(digest(raw_review)==EXPECTED_ROOT_REVIEW_SHA,'Exact root review identity');review=json.loads(raw_review)
    require(review['kind']=='root_source_publication_review' and review['root_read_complete'] is True,'Actual source-publication review schema')
    require(review['source_draft_freeze']['sha256']==EXPECTED_SOURCE_FREEZE,'Actual review/source freeze linkage')
    require(review['body_pins']==EXPECTED_SOURCE_BODY_PINS and review['parent_binding']==binding_spec,'Reviewed body and parent scope')
    require(all(review[key]==0 for key in ('scientific_programs_run_this_review','primary_runs','historical_programs_replayed')),'Source review execution scope')
    for key,path in [('note','proposal/'+NOTE),('primary','proposal/'+EXPECTED_HELPER)]:
        require(all(review[key][field]==EXPECTED_DRAFT_CANONICAL[path][field] for field in ('bytes','sha256')),'Exact reviewed draft note/primary')
    review_freeze=json.loads(bound_blob(evidence['review_freeze']))
    require(any(row['sha256']==EXPECTED_ROOT_REVIEW_SHA and row['bytes']==len(raw_review) for row in review_freeze['files']),'Root review seal membership')
    _,observed=execution_evidence(evidence,True,EXPECTED_ROOT_REVIEW_COMMAND)
    observed=json.loads(observed)
    require(observed['review']['sha256']==EXPECTED_ROOT_REVIEW_SHA and observed['review']['bytes']==len(raw_review),'Actual review output linkage')
    require(observed['freeze']['sha256']==evidence['review_freeze']['sha256'] and observed['freeze']['bytes']==evidence['review_freeze']['bytes'],'Actual review freeze linkage')
    canonical_evidence=actual['canonical_review_evidence'];canonical_raw=bound_blob(canonical_evidence['review'])
    require(isinstance(EXPECTED_CANONICAL_REVIEW_SHA,str) and digest(canonical_raw)==EXPECTED_CANONICAL_REVIEW_SHA,'Exact canonical review identity')
    canonical_review=json.loads(canonical_raw)
    require(canonical_review['root_read_complete'] is True and canonical_review['bound_note_sha256']==digest(note),'Actual canonical note review')
    require(canonical_review['canonical_body_pins']==bodies and canonical_review['parent_binding']==binding_spec,'Actual canonical interval and parent review')
    require(canonical_review['source_draft_freeze_sha256']==EXPECTED_SOURCE_FREEZE and canonical_review['source_draft_review_sha256']==EXPECTED_ROOT_REVIEW_SHA and canonical_review['git_base']==EXPECTED_GIT_BASE,'Canonical review source/base linkage')
    require(canonical_review['prebinding_primary']==EXPECTED_PREBINDING_PRIMARY and canonical_review['integration_common']==EXPECTED_INTEGRATION_COMMON,'Canonical review prebinding implementation')
    _,canonical_observed=execution_evidence(canonical_evidence,True,EXPECTED_CANONICAL_REVIEW_COMMAND)
    canonical_observed=json.loads(canonical_observed)
    require(canonical_observed['review']['sha256']==EXPECTED_CANONICAL_REVIEW_SHA and canonical_observed['review']['bytes']==len(canonical_raw),'Canonical review operation linkage')
    local_base=json.loads(bound_blob(actual['base_observation']))
    require(local_base['observed_commit']==EXPECTED_GIT_BASE and local_base['source_revision_verified'] is True,'Actual local base identity')
    _,local_head=execution_evidence(local_base['execution_evidence'],'git_head')
    require(local_head.decode().strip()==EXPECTED_GIT_BASE,'Actual local HEAD receipt linkage')
    _,base=execution_evidence(actual['parent_pr_observation'],False)
    base=json.loads(base)
    require(base['number']==EXPECTED_BASE_PR and base['headRefOid']==EXPECTED_GIT_BASE and base['headRefName']==EXPECTED_BASE_BRANCH and base['baseRefName']==EXPECTED_BASE_PARENT_BRANCH,'Actual base PR identity')
    require(base['state'] in ('OPEN','MERGED') and base['isDraft'] is False,'Regular base PR observation')
    receipt_paths={actual['source_proposal_freeze']['path'],actual['source_draft_body_map']['path'],actual['base_observation']['path']}|{r['path'] for r in evidence.values()}|{r['path'] for r in canonical_evidence.values()}|{r['path'] for r in actual['parent_pr_observation'].values()}|{r['path'] for r in local_base['execution_evidence'].values()}
    require(set(actual['receipt_paths'])==receipt_paths and len(actual['receipt_paths'])==len(receipt_paths),'Exact binding evidence membership')
    state=read_json(PACKET+'/PUBLICATION_STATE.json')
    require(state==EXPECTED_PUBLICATION_STATE,'Historical proposal state must remain unchanged')
    require(state['primary_execution'] is state['publication_action'] is state['retained_audit'] is None,'Historical proposal nulls remain null')
    print(json.dumps({'result':'source_integrity_verified','scope':'exact bytes, recovery and captured binding metadata only','scientific_programs_run_this_primary':0,'historical_programs_replayed':0,'mathematics_or_retention_certified':False},sort_keys=True))
    print('per_element: source coefficient text retained; no physical element was executed')
    print('per_site: declared complete lattice interface retained; no hardware test was executed')
    print('per_mode: restricted plant and conditional lemma remain distinct; no propagation was executed')
    print('per_block: exact spin-source text and original/retrospective receipt metadata checked only')
    print('lattice_wide: native preparation, actual suppliers and independent audit remain separate')

if __name__=="__main__":
    try:
        main()
    except Exception:
        if METADATA_CHECK_COUNTS["failed"]==0: METADATA_CHECK_COUNTS["failed"]+=1
        raise
    finally:
        print("metadata_check_counts_only: source bytes and provenance assertions; no scientific proof or retained status")
        print(f'TOTAL: PASS={METADATA_CHECK_COUNTS["passed"]} FAIL={METADATA_CHECK_COUNTS["failed"]}')

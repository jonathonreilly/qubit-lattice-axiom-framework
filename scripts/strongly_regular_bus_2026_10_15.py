"""Source-integrity proposal only; no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-strongly-regular-bus-20261015"
EXPECTED_PARENTS = {}
EXPECTED_BODIES = {'author_bus_body': '855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2', 'exposed_review_body': 'cda68e9f414bbc5d5baac5fca8f88a9324691c4e38b5569589ecb81c478458e7'}
EXPECTED_ACCEPTANCE = "cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726"
EXPECTED_GIT_BASE = '058724b51948962713d764781fcb4b99802f5410'
MANIFEST_SHA256 = 'aebea94b4dff7377c9a1daffaa0341e0a7bcbd08a8e6b8475cc71156537570a8'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-strongly-regular-bus-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/CHECK_RECEIPTS.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PARENT_BINDING.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/0037211f97d82eb917cc091f8f320a0cc594b95d7992d88a7d550c73832ee145.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/2725b9a446618c12bffb1f098824c49c9a845e5eec587074b2f5f12fee1981fa.py', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/289547820e8b6fce01f30bfc3f014d1092ab950124031885e24465e25b78116e.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/3642b82459aa3c9cde31cc4fa2d37f277ef77c335df9e6a574015b456cd8fbb8.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/3f19d861fa38610a754f0f2ee4cfbf090c06ee58cd1f2654c88275cc135dc1bb.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/43d0935394d8d3dcc9d3e6f7094f730700ad3c5fea6a653d4b2dbf65b2983976.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/45b0437d14ac192026a4de9ada1bc561fdc5020bec81657d8a0a7fa87e6380c5.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/5c33c0692c4c3d48d406741d32dd3e99c98d3dee6aff1669ab26aee9311f32fe.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/5e6c1e181f121331983031ccff4736eb7270309f3a1019ed831d7ff4abbcf290.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/60e379cd3bbacc05677689e751744ad92f5955d81a0e2fef71092f6d94deea88.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/6130e3cc5a55ae9761dd52abfcc0756184f566de5cd973a3a6b25e0e7aa17b77.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/71d6aa8f22b83ac1ee6aaac0f6351c58ada14d4cbdc3bf80e44a8d5db719e42f.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/92b5db0a6ac7a8c8c3f31951c38a0657a47a9648e05caa67d2639d9d7c4b1ac7.py', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/933f98a30ca7bf4cd8b56dc71a0cfc1aeac22980cb4687f039d95e094c09650d.py', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/96b5f165e45f563c00cfdcccfd0aa284263431cbaf7a6014b19c093d96be3629.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/b32f06feab0594eb49844f8285084033cb581660621c36dc611c53d23a817ab8.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/b3cb8a32eedc9732d64b52614fc70ab0723ae41c13cedfd9a109c77a3882525e.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/d6f0f4337b62097d6428c4a77a7a1767772054c0b512b2e0f75830ac082e3bdd.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/da161cd410560c0785c603d5611792bc884a3450f148b1ecdaf3f8ec15c36725.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/dc185c8ed023cdac4ff9a4bb6c97bdf8ddd3408523ed8abc5cde1d18be451e0f.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/e0ea96413d28b25d0b8e8b718cac67969c54dea5d1855d3af42bba99b9416a52.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/e1111b0b3c6724c4bf74314393cb21859b8f73b45c0036949a9f4c7034bb4928.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/ec2478f76ada4505294879be2910537959c88462a34d425f978c4919681f9d21.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/binding_sources/f3136de966f2addffd5a8ebcc778f09fccbeeb052930ddcf0394e68689db5dc2.json', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/11812da3a16d13e5b9d901df300c02660202751ef72613f0e9cd435c0812298d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/185aa0c83c725e09e5ba10197dab16f1254f639d563e8d2993adc7df0e5ee0a4.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/1c4a00e0195c28bd36b68094442254967f75fe70dc587e6ce1d523f9b53d65e6.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/22bead85499930f151f128633db75522b7ea0fbf3a6b8777a124f1f3edf1502b.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/23ee618157a009a4cd0da974017c26e88bdb889fc4e3ef0de948409d8648ca93.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/2d47b5930fa0ecc86d994fc9369e1702922f6c2607b42bc6d349172024c99508.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/2dfa5c6176bbd310a517a0e47acf2da19c4443025705e3b09fa05d811cb183cb.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/36bd9d19c09262f539f72c7283756cfa86fbae065a435e13a2248f521e867632.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/3a2cc04468a5ce9c6f82762afbcaafd5f65bef4b965e67df9c4311dbd2158fbb.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/3e5e769880746b925f759afc412812fe6fec62486be760a11200d63a0a786de4.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/3e85a96b1d47e0d1c5c07de24161a1ee71efa99616ea414552d7a0698de1a27d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/3ebe4a1c40c4349c600f19ae7c9ccfef2eb79c4596855780ae634d20ecf2e67d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/411d9258730e4c15433cf9cc9e4c76fc024e6165ef5664ce6cc769f434637a74.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/425912c7abc039b9ac2155bc372c4dfa7b79f9676507fb48a4b5fa2b8684fe8f.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/43cc594c7ff61a84c99d38143dbc02d5798e991aa80c2d26a12662366b6a9d7f.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/45ba0b48b9a893b5504d51b8c61a52fab2c0bc485a4f0fbc7cd573d375ab065e.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/48055d1f9ad9443661ddebc31671fa23dcb8c6893c6e5b888923b4743b5a4c9c.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/4cbb550d2a2de48332a1de84fa73a118fba5a511dca931df185e41811e0e34bb.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/4e229757fc07bf0b3e3a3ec821adf1418643468040c2b1f9c258b6b3968a22d1.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/4e4d7b45524919525ffd79ccc9ad1b56f5ad111a4053db5278296d6bca5f0156.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/54bb75d961857cf33a6c5b5add71dd83ab1be8fef73de18003ff227f6eea02c4.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/5654254e4f4b1450ff7fbd0abcea8c63d36e867f93e6e19f84e40174c6a735b0.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/59b3872ce262cc54d31c7d828025b424d96225118efc14bbbacc1858c8ddd4d6.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/653ad5ead571418dcef88ebd2054327e74d406ccb5d59c6c3c53ca8ad3859995.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/6810cfdca40ae0cac56fa0ce0df932414ac48be43f5dd9c5017820a4ad9cb817.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/7bb08a0c201d2bdcb6c2a4e48cb4811eac7cbf116c2646b599349fce61dd55b1.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/7f9b00618c9ef581f352b9c3436e4a4dea131d9f87f08cf9216980674ab23427.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/7fe8d8b2f9102ad154a8557c57c3d5dfdafd26697124ca4d231b260c63279307.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/8d4fc51cb4d5663762171331f9b152a39782e75c6cbb4ff481b951655ae5b2f7.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/92f462e58668aa8a0b814a296a74c75ae8c55746f294170a5c3391b8658b4d28.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/9a27384ed80d3bde9abc7fc9dc45bca0ab1280abbdcd09242729ac101e13b7cb.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/a182e0074ac9b8ed1d9e9e57627d289754252e2969446099ed502e229bf61880.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/a35bafbce8e7b0be63333eab3e4f86957f485de8b9a84599d7c515618a71c2a0.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/a3a31a04928c48f69166ae7d6a6d224f7fe612887c84f6273baab253b1bdbb74.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/a6f9219e3f89689fee6963cf9991bad285ff74e0514e426213cb051a97362b1d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/a9cd83f3ee125484f62beab5fc10cc1c58b99ccaa992a3b9e05a155f418fd4ca.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/ab98ed0729a0e6e887c004a24ba5026a2762dc48f5ee3fa8d10386fbde78f4c8.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/acbdd13ac43bbfba39c2df75c35ae5d24b41d83b665381257176b0b08264318e.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/acd758dd676a2f9d214067c96faa3607983f3d5adffbbd2755aecf73e1c518bf.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b0f6aa9b09eb72979d3ae2ee13683822e51a73df03f7cd53f0aa94e600d0c3d7.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b1e6d47573519c9b39bd160d21f28c8ac15fbf382907c0e5dc61a818a8651292.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b21f0266b367944c93567c034ef9f247f777dc6dc564fb871475847644a17520.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b3237abd67a23b3d483461e612d5777e5a5c968cb0fe0bcb3d041ecb75d47c5c.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/b7c71dcc8552b5401fa904744d43a36c2f1560d25e63789558158f7625a5af67.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/bfe6eda1aa915e8447370c3c9a3b36b4cdb07dee469438253a7d4f996f8aa09d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/c086beea373f1ac550449fe863afab31d1b2efcc874750e9ac921f9f81dd7974.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/d49d18dbbb327cb75ce628e90039364dbd3486779fb61b410b6ddf427348b44e.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/d5d7bc4d5d41521644029df01494c69e480bb1e170374b006e6f682dcce70a0a.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/d9c25c69380bea27b2b113b94283631c7391cb277217851bc6ca4e3d3804e110.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/e18a228cd8008a663f82d9be789e2596eb214279cf3f3b91a3daaf2930b60f8d.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/e606b072b006026700c4b951786636efd03bf1d973e77627ef342705fab0a29c.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/e707445429c4f75422a2632a3f5c64d5e4f2900c1b8286730662cc9ea905b6f6.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/ef2d40abd03e90c628656b6054c92ad79af03ea95fe71f25d0371e9eba80df44.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/f37267310f011468fecddf6cffd621f679c8695cb0d4b43927c5d8d81f1476b4.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/f8ad695c6e8f5b6685bd9466184dfa4e8b7859a2edcdd9c449863cba6d248c71.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/fb8a61a0979c9413a91fd07e9d2b7345ba2d038132911df7974a2e247f12ae75.blob', '.claude/science/physics-loops/toe-strongly-regular-bus-20261015/source_recovery/fc4edf1baa103ac39bc875e113b7ff5801903513e949886653b33018c752043f.blob', 'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md')
METADATA_CHECK_COUNTS = {"passed": 0, "failed": 0}

EXPECTED_ROOT_REVIEW_SHA = '45b0437d14ac192026a4de9ada1bc561fdc5020bec81657d8a0a7fa87e6380c5'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_strongly_regular_bus_publication_review/record_review.py')
EXPECTED_CANONICAL_REVIEW_SHA = 'b32f06feab0594eb49844f8285084033cb581660621c36dc611c53d23a817ab8'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_strongly_regular_bus_integration_review/record_canonical_review.py')
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/strongly_regular_bus_2026_10_15.py', 'bytes': 42263, 'sha256': 'bf52b0f87f67e9f85d19dea780291a2a188891d0dc1c1d88b1ce0ccf3e2af27f'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/strongly_regular_bus_integration_corrected/strongly_regular_bus_common.py', 'bytes': 56447, 'sha256': '2725b9a446618c12bffb1f098824c49c9a845e5eec587074b2f5f12fee1981fa'}
EXPECTED_BASE_PR = 9630
EXPECTED_BASE_BRANCH = 'physics-loop/toe-correlated-energy-comparator-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-restricted-spin-source-20261015'
EXPECTED_REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
EXPECTED_PARENT_BINDING = {'canonical_parents': [], 'transitive_premises': [], 'preparation_release_intervals': [], 'mathematical_scope': 'The exact author body sections 2-11 proves the cone, routed geometry/full gap, source resolvent, connected second order, corrector, phases and resource inequalities. Prior compiler/mediator/source proposals are exposure/context only; their theorem conclusions are not imported. Simple spectrum, distinct positive gaps, nonzero port entries, computable spectral data and vacant geometry are supplied premises, not implications of earlier Lie certificates. Rational-M repair is separately attributed in exposed review section 6 and root qualifications. No unproved imported theorem was identified.', 'actual_current_git_observation': None}
EXPECTED_DIRECT_PARENTS = ()
EXPECTED_SOURCE_BODY_PINS = [{'name': 'author_bus_body', 'container': 'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 19745, 'end_byte_exclusive': 60245, 'bytes': 40500, 'sha256': '855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2'}, {'name': 'exposed_review_body', 'container': 'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 60414, 'end_byte_exclusive': 83847, 'bytes': 23433, 'sha256': 'cda68e9f414bbc5d5baac5fca8f88a9324691c4e38b5569589ecb81c478458e7'}]
EXPECTED_SOURCE_MAP_SHA = 'e0ea96413d28b25d0b8e8b718cac67969c54dea5d1855d3af42bba99b9416a52'
EXPECTED_SOURCE_FREEZE = '71d6aa8f22b83ac1ee6aaac0f6351c58ada14d4cbdc3bf80e44a8d5db719e42f'
EXPECTED_DRAFT_FILES = {'proposal/.claude/science/physics-loops/toe-strongly-regular-bus-20261015/BODY_MAP.json': {'bytes': 711, 'sha256': 'e0ea96413d28b25d0b8e8b718cac67969c54dea5d1855d3af42bba99b9416a52'}, 'proposal/.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PARENT_BINDING.json': {'bytes': 763, 'sha256': '9674ff9718ec664107f6e9d6027a237ed752a2a49fc91b6708e6e88d98f3302e'}, 'proposal/.claude/science/physics-loops/toe-strongly-regular-bus-20261015/PUBLICATION_STATE.json': {'bytes': 491, 'sha256': '9869067d8b733cf6a2472df6a560b5f90689d7bc8a91cddc390f7bd6a70ce141'}, 'proposal/docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 83847, 'sha256': 'ca5458cc82c78831338dac4bc999a17184f77d63b8ee2c65a084e569e3b032e9'}, 'proposal/scripts/strongly_regular_bus_2026_10_15.py': {'bytes': 26286, 'sha256': '0c5b65a6c92b4847372ec291fd3ad32bbf441c149d444f5ed560c0ace8d88bf9'}}
EXPECTED_DRAFT_CANONICAL = {'proposal/docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 83847, 'sha256': 'ca5458cc82c78831338dac4bc999a17184f77d63b8ee2c65a084e569e3b032e9'}, 'proposal/scripts/strongly_regular_bus_2026_10_15.py': {'bytes': 26286, 'sha256': '0c5b65a6c92b4847372ec291fd3ad32bbf441c149d444f5ed560c0ace8d88bf9'}}
EXPECTED_PUBLICATION_STATE = {'kind': 'historical_source_only_draft', 'canonical_integration': None, 'git_base': None, 'root_publication_review': None, 'primary_execution': None, 'cache_execution': None, 'mutation_execution': None, 'graph_execution': None, 'publication_action': None, 'retained_audit': None, 'scientific_programs_run_this_draft': 0, 'historical_scientific_programs_replayed': 0, 'source_acceptance_sha256': 'cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726'}
EXPECTED_HELPER = 'scripts/strongly_regular_bus_2026_10_15.py'
RECOVERY_TABLES = {'SOURCE_MANIFEST.json': 'sources'}
EXPECTED_HISTORICAL_RECORDS = [('author_bus_run_v1', '5654254e4f4b1450ff7fbd0abcea8c63d36e867f93e6e19f84e40174c6a735b0'), ('author_bus_run_v1', '3a2cc04468a5ce9c6f82762afbcaafd5f65bef4b965e67df9c4311dbd2158fbb'), ('author_bus_run_v1', 'a3a31a04928c48f69166ae7d6a6d224f7fe612887c84f6273baab253b1bdbb74'), ('author_bus_run_v1', 'a6f9219e3f89689fee6963cf9991bad285ff74e0514e426213cb051a97362b1d'), ('reviewer_bus_run_v1', '6810cfdca40ae0cac56fa0ce0df932414ac48be43f5dd9c5017820a4ad9cb817'), ('reviewer_bus_run_v1', 'bfe6eda1aa915e8447370c3c9a3b36b4cdb07dee469438253a7d4f996f8aa09d'), ('root_acceptance_metadata_v1', '9a27384ed80d3bde9abc7fc9dc45bca0ab1280abbdcd09242729ac101e13b7cb'), ('invalid_first_review_seal_v1', 'e18a228cd8008a663f82d9be789e2596eb214279cf3f3b91a3daaf2930b60f8d')]
EXPECTED_QUALIFICATIONS = 'a182e0074ac9b8ed1d9e9e57627d289754252e2969446099ed502e229bf61880'
EXPECTED_QUALIFICATION_SOURCE = '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/strongly_regular_bus_root_review/FINAL_QUALIFICATIONS.md'

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
    schema=row["schema"]
    if schema=="author_bus_run_v1":
        launch=json.loads(recovered(row["launch"]));result=json.loads(recovered(row["result"]));source=recovered(row["source"])
        require(launch["command"][1]==row["source"]["source"],"Actual author launched source path")
        require(len(source)==launch["source_bytes"] and digest(source)==launch["source_sha256"],"Actual author source bytes")
        require(result["returncode"]==row["expected_exit"] and result["timed_out"] is False,"Original success or failure retained")
        require(isinstance(launch["start_utc"],str) and isinstance(result["finished_utc"],str),"Original author timing fields")
        if row["launcher"] is None:
            search=json.loads(recovered(row["missing_launcher_search"]))
            require(launch["launcher_sha256"] in search["target_launcher_hashes"] and search["target_launcher_hashes"][launch["launcher_sha256"]]==[],"Missing failed launcher remains missing")
            require(search["reconstructed_missing_bytes"] is False and row["expected_exit"]==1,"No reconstructed launcher or erased failure")
        else:require(digest(recovered(row["launcher"]))==launch["launcher_sha256"],"Available actual successful launcher")
        recovered(row["stdout"]);err=recovered(row["stderr"])
        require(bool(err)==(row["expected_exit"]!=0),"Failure/success streams retained; hashes are frozen evidence, not absent receipt fields")
    elif schema=="reviewer_bus_run_v1":
        receipt=json.loads(recovered(row["receipt"]));source=recovered(row["source"])
        require(receipt["exit_code"]==0 and receipt["argv"][1]==row["source"]["source"],"Actual exposed reviewer command")
        if "source_at_launch" in receipt:
            for expected,item in zip(receipt["source_at_launch"],row["sources"]):
                require(item["source"]==str(Path(receipt["cwd"])/expected["path"]),"Reviewer helper source path")
                identity(recovered(item),expected)
            require(len(receipt["source_at_launch"])==len(row["sources"]),"All declared launch sources retained")
        else:require(len(source)==receipt["source_bytes"] and digest(source)==receipt["source_sha256"],"Reviewer main source identity")
        recovered(row["stdout"]);require(recovered(row["stderr"])==b"","Reviewer actual streams")
        require(row["exposure"]=="source_exposed_same_model","No blind independence inferred")
    elif schema=="root_acceptance_metadata_v1":
        receipt=json.loads(recovered(row["receipt"]));source=recovered(row["source"])
        require(receipt["exit_code"]==0 and receipt["argv"][1]==receipt["child_source_at_launch"]["path"],"Actual source-acceptance command linkage")
        identity(source,receipt["child_source_at_launch"]);identity(source,receipt["source_capture"])
        identity(recovered(row["recorder"]),receipt["recorder"])
        for key in ["stdout","stderr"]:identity(recovered(row[key]),receipt[key])
        require(recovered(row["stderr"])==b"","Root acceptance error stream")
        observed=json.loads(recovered(row["stdout"]));acceptance=recovered(row["acceptance"])
        identity(acceptance,observed["acceptance"])
        require(digest(acceptance)==EXPECTED_ACCEPTANCE and row["scope"]=="root_source_acceptance_metadata_only","Actual source decision metadata")
    else:
        require(schema=="invalid_first_review_seal_v1","Known historical schema")
        report=json.loads(recovered(row["post_verification"]));raw=recovered(row["stdout"]);seal=recovered(row["invalid_freeze"])
        require(len(report["changed_after_seal"])==1,"Original seal discrepancy retained")
        changed=report["changed_after_seal"][0]
        require(changed["path"]=="SEAL_EXECUTION.stdout.json" and changed["expected_bytes"]==0 and changed["actual_bytes"]==len(raw) and changed["actual_sha256"]==digest(raw),"Invalid seal captured a live output member")
        identity(seal,json.loads(raw)["freeze"])
        recovered(row["source"]);recovered(row["stderr"])
        require(row["valid_final_seal"] is False,"Invalid historical seal is not publication evidence")

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
        for part in row['accepted_body_intervals']+row.get('used_premise_intervals',[]):require(part['container']==row['path'],'Parent interval container');interval(part)
    for part in binding_spec['preparation_release_intervals']:interval(part)
    sources=read_json(PACKET+'/SOURCE_MANIFEST.json')['sources']
    require({r['sha256'] for r in sources if r['role']=='qualified_source_acceptance'}=={EXPECTED_ACCEPTANCE},'Qualified source decision')
    require({r['sha256'] for r in sources if r['source']==EXPECTED_QUALIFICATION_SOURCE and r['role']=='root_source_acceptance_provenance'}=={EXPECTED_QUALIFICATIONS},'Controlling source qualifications')
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
    check_packet=read_json(PACKET+'/CHECK_RECEIPTS.json')
    require(check_packet['blind_independent_execution'] is None,'No blind independent executable')
    checks=check_packet['records']
    require([(r['schema'],next(r[k]['sha256'] for k in ('launch','receipt','invalid_freeze') if k in r)) for r in checks]==EXPECTED_HISTORICAL_RECORDS,'Exact historical record selection')
    for record in checks:
        check_receipt_members(record,sources)
        if record['schema']=='author_bus_run_v1':require(record['scope']=='finite_author_floating_point_case_only','Finite author evidence scope')
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
    print('per_mode: exact-target existence and rational-target effectiveness remain distinct; no scientific program executed')
    print('per_block: exact bus text and historical success/failure/provenance metadata checked only')
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

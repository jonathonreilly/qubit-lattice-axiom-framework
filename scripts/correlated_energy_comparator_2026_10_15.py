"""Source-integrity proposal only; no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-correlated-energy-comparator-20261015"
EXPECTED_PARENTS = {'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md': (115781, 'd0c250c80d25065d7b2667f22d83d53ef43419088fa7484f1c157a6408ac177f', 'polynomial_path_mediator_bounded_theorem_note_2026-10-15'), 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md': (69312, 'baea95d22b229fad3c0aa166bff5608f9edfe7ea973ff0252fbc5cd9b1389007', 'autonomous_compiler_composition_bounded_theorem_note_2026-10-15')}
EXPECTED_BODIES = {'author_order14_body': '3189e031950d2613d1df69523260550f8d2da5c233a748dbf59144c525850c20', 'protected_order15_body': 'e23871d47ef5b3043a903c33deab317cf5a7c14bee86f06486baa699d14a3d93', 'exposed_reconciliation_body': '6d87cc9d686b895a4f5802b810943d9df6ea1304b3087cb08fa84b13272ef34d'}
EXPECTED_ACCEPTANCE = "4e3d3af077b3dd5df8b11c6a7955f960c670a39a2aa16e52f6a409fb09e78067"
EXPECTED_GIT_BASE = '7df015aee608443b47825d6d55f6cf2dbdb793a5'
MANIFEST_SHA256 = 'd9c3a8855a79f17ef08e0b46bcaf5ae026e1fe2766693e148f114320199dd2d3'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/CHECK_RECEIPTS.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PARENT_BINDING.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/02f27eb84a6f45bc7c7d0f4e13c26da0fb9c8a7e6c246ec976da68adf5ae169e.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/0477441716582a22a5ab76a517610fecda6b545e005ad7f3cdfebf75ee9c43cf.py', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/12817c7b77114788460ae71c987eeaee8f47dc08b32d40c7eb1c599defb8521a.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/46b22703af34c8ac721ee2ee1890571a1a2c6124960f5ca14f0b5cf556122170.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/48c1acf07b9b1c2a50e67dfa56902e7526d9e2fa079dc15cc281c0db6ab9d82f.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/4b77d68351eb84071ea10a3d609caf4f4f9b212b5d68ff2b5e9c4fbe68b5abf8.py', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/4e0bb14a5a730be018fd083699b7fac7017582ce2caf870ccc6a79cb6ae5e0e8.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/5af054d5e6b47d155f8c5d83884fab2e6f3741302696542deac14d396e279926.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/615f9d7e6551b9d74f0db29549d39d38aece0b7fb196d4ad4484cdd6a2c974a0.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/7ad79a528b186d70364642619eead22d2d667973e7d36033fd40e6da948dce05.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/81b55fa25f392bca9e2d64a4aea2221309490553acaee1a507eb104304c5fd7d.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/81ef0857a36d084bf7a6dd25b49ad01af6c88dd61678ee77db4c84a7f1da35be.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/821cfcff02db29906cd81c0e8821ccbdec9a1e54f970f934d57f42dad30a85e6.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/aa2f59bb5b55830d4a79e5253ccede43e289d6d5adfd90ae52a33a64285e0928.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/b366e2576f1ab4c53400b01a6d122c397c315d3017fe1840ccba141bcc405cea.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/b6a8463e6a8c4f36a1aca54fd981e71c05bb4f3302c2ecfcfd8f07148555467c.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/be61ba32b1f06c5a8de8562890a091edd31561163434f88a7869b898bbe17a6d.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/bf65f5763bcff09f0d8c2980dbef8a64d533658fd8878b74830283a6fe15b8fb.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/c722ca3f97343bd6fc3c2b24637f553b854cdc92c8ca372c4e31f595c78e56e4.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/c81b7ea79f1222580add42f8a646cd684c2a36511572ed704d6ccb46f0ea10b7.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/cf5dec3968299eef910b0ea1697361e2ca40f9ae46d1cfd2843d40cd866d3eaa.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/d49d3e8bc11b60a28e2ea8c390ee4dc958d9b972bbe0c097337a149e6db9cba2.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/d611cff48c82310504c9f9f69556c731ef0df69befd135d761ee3c542bf06522.json', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/binding_sources/e503206b6da20bdf90a9346a5e5ff3b83134d1edc57646025eaaa67f1bdb3cc3.py', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/0620fd7bd19b9b9244392ed62282b7ddf07d26a4bd01135557c0c097b147bccb.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/17539386deec97e1e5958db41aff028e8934f5bbe78767dcf962cce50013f5f0.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/1821d2cf74cc6abd4d450557ee8125f3a4437484c5c90a339c9338d4e4c1867a.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/24e6963abddbb227fe1f7a49c7cae1d8c4b2c3b7b446ca1463558dddbb9c5779.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/2715772159342739437f0eac6f9f7f28af5dec0bbb9dd644fa414ea4cbbf5011.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/27602e43a43294f441e7739ea7c5e40f9f42ccb6e2c446c67546f26e455be313.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/2d760de74266e08b122d0cab7f611ca831af8a3364538c235eb2ce79ca31b549.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/47f4a3525e784cd544caef0e18c43f7ed7b76bae25c51b3fbe662311064e379f.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/4e3d3af077b3dd5df8b11c6a7955f960c670a39a2aa16e52f6a409fb09e78067.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/50348e1514d9f12a8edbd5fbbcc6a2fccad6559dd5b14ee0f1e11900b3c0c503.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/509dbbd181927e0dc69108ecbc8cedf3ca9cf158880941f78db87a86f3d9702c.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/60f08894c45c110dbfda6013ab2425e660940bbcdec3d5302a3b3c5b5e5826b9.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/6348161ff21ce696cae626d7173ec26beae772a8cc45b26c08115adf4ab0924e.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/664046ae8e1b5cd4cee92e7d8ac3c4a34767573399f99242a5c20cb731143d59.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/66cf432a64e8158d8aa5c638563cb76976ef0530cad4276070d4d0d4be8c71c3.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/6ab51e0b1d83545d0ed1ccc0def8be768fb8e0fadb090df24309d427ee134a3c.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/73d8a4bbdae41d4a770ca6243bc1208d279717d311b9a7275a0be1751e3bcd7e.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/8690db6370059341f45e0af1c94de65d90800fc809008df85d6650bb43914ef5.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/8ac73726ce226a725d66b9324f4d155f64781d3e8c95144db08a37164f9cba7b.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/8f97592170c32780a1414977204916668b95f3a94492bcf857dac1cbcbcd6538.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/9a4cfd3f79fd0501a2a7c28b24d6439021bde79366ffdca78947097dbea0bb27.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/c2aa29e6a4aa83a33a8aba561622a23a655f92596b4f6c52c39e04281c4ac05d.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/d2df4ad0defa67c87db1c405b5140c6f2ce85d985648eadfb8bfb25b849decb2.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/f2a89628467327048052ae762fcf51bf2cfa07b9b99102e03a24e8b518799477.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/f809c11fdd39918565116058039de37b83ece2f23316e8e4a2055c049fb38ea6.blob', '.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/source_recovery/fe0c28c58dbd0fbdecb3dfc0936262917f0398ade5f23d584fea611402d4580b.blob', 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md')
METADATA_CHECK_COUNTS = {"passed": 0, "failed": 0}

EXPECTED_ROOT_REVIEW_SHA = '615f9d7e6551b9d74f0db29549d39d38aece0b7fb196d4ad4484cdd6a2c974a0'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_correlated_energy_publication_review/record_review.py')
EXPECTED_CANONICAL_REVIEW_SHA = 'c722ca3f97343bd6fc3c2b24637f553b854cdc92c8ca372c4e31f595c78e56e4'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_correlated_energy_integration_review/record_canonical_review.py')
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/correlated_energy_comparator_2026_10_15.py', 'bytes': 44092, 'sha256': '03b426602f51a6063fe3b136f565449b1fea266883b49b9868bbec9bbbd1c6a3'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/correlated_energy_integration_proposal/correlated_energy_common.py', 'bytes': 56424, 'sha256': 'e503206b6da20bdf90a9346a5e5ff3b83134d1edc57646025eaaa67f1bdb3cc3'}
EXPECTED_BASE_PR = 9629
EXPECTED_BASE_BRANCH = 'physics-loop/toe-restricted-spin-source-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-bounded-slew-compiler-20261015'
EXPECTED_REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
EXPECTED_PARENT_BINDING = {'canonical_parents': [{'path': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'bytes': 115781, 'sha256': 'd0c250c80d25065d7b2667f22d83d53ef43419088fa7484f1c157a6408ac177f', 'claim_id': 'polynomial_path_mediator_bounded_theorem_note_2026-10-15', 'role': 'direct_mathematical_parent', 'accepted_body_intervals': [{'name': 'root_mass_m3', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 30425, 'end_byte_exclusive': 48979, 'bytes': 18554, 'sha256': '45c211e6c44bb694cf01ac11e15ede8a85442b95baa125dd0b01519a031ee893'}, {'name': 'independent_mass_m2', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 49121, 'end_byte_exclusive': 84178, 'bytes': 35057, 'sha256': '0620431acdfc9b0c9e36f4ec1364cf2eaff8891ba2697aeadee37501b1e493a7'}, {'name': 'source_exposed_comparison', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 84326, 'end_byte_exclusive': 115781, 'bytes': 31455, 'sha256': '3cc7a9d32e0019edef91c1f699e396bf84dd31fbe0642d6a32170d14538b9067'}], 'used_premise_intervals': [{'name': 'used_lines_1_145', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 1, 'line_end': 145, 'start_byte_inclusive': 0, 'end_byte_exclusive': 10308, 'bytes': 10308, 'sha256': '18067bb3da3104539a50de407d227fea8196a0115d2588cfd6b49f81b8e5a5be'}, {'name': 'used_lines_364_584', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 364, 'line_end': 584, 'start_byte_inclusive': 31460, 'end_byte_exclusive': 48986, 'bytes': 17526, 'sha256': 'b9be606a0a1cd7ccbc24b3eeb19e67603e4d4fd9e589892022918c0eacd64610'}, {'name': 'used_lines_589_949', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 589, 'line_end': 949, 'start_byte_inclusive': 49121, 'end_byte_exclusive': 75079, 'bytes': 25958, 'sha256': '4055f7d2ea73ff417a4cb2617a0f64cb7343a36948c751306ab3f2fa9ea1f63b'}, {'name': 'used_lines_1139_1237', 'container': 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 1139, 'line_end': 1237, 'start_byte_inclusive': 96591, 'end_byte_exclusive': 102916, 'bytes': 6325, 'sha256': '326533c70a7d2eae7138e0c8b3a6472a052bd6fa33834cd6a7c4691b2d8c0ae2'}], 'use': 'Full auxiliary gap/inverse, physical coefficient/counterterm/reserve definitions, both recipe bounds, nominal norm and bare moments; no preparation/release import.', 'body_map': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/BODY_MAP.json', 'bytes': 1041, 'sha256': '6ab51e0b1d83545d0ed1ccc0def8be768fb8e0fadb090df24309d427ee134a3c'}, 'canonical_binding': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/CANONICAL_BINDING.json', 'bytes': 2401, 'sha256': '509dbbd181927e0dc69108ecbc8cedf3ca9cf158880941f78db87a86f3d9702c'}, 'source_revision_supplied': '23a84c17353ea13dab449ca9a37800b5e4defcb4', 'revision_evidence_limit': 'Root-supplied current source base and separately preserved historical observations; this drafting task ran no Git command.'}, {'path': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'bytes': 69312, 'sha256': 'baea95d22b229fad3c0aa166bff5608f9edfe7ea973ff0252fbc5cd9b1389007', 'claim_id': 'autonomous_compiler_composition_bounded_theorem_note_2026-10-15', 'role': 'direct_mathematical_parent', 'accepted_body_intervals': [{'name': 'root_runtime_body', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 16846, 'end_byte_exclusive': 24261, 'bytes': 7415, 'sha256': 'f077e6eb4e942362d5cbd9eb811d17e78272ade1ed236c8c79e9bf0568e41ad8'}, {'name': 'extended_body', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 24424, 'end_byte_exclusive': 51624, 'bytes': 27200, 'sha256': '9e97240607ed4598526da7bb00e07bcb74b4be85ee4de79fa29081686f210aa7'}, {'name': 'exposed_comparison_body', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 51797, 'end_byte_exclusive': 69312, 'bytes': 17515, 'sha256': 'd43f8ee3e438afc591a1f542c7d6d97b572199d6fbc8547bb8948841a8f9e691'}], 'used_premise_intervals': [{'name': 'used_lines_1_139', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 1, 'line_end': 139, 'start_byte_inclusive': 0, 'end_byte_exclusive': 15918, 'bytes': 15918, 'sha256': '6dacae62f6c6c9d28564838b5fe7e7f90fcec99eb19824bef7bc49b5a7daf901'}, {'name': 'used_lines_150_212', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 150, 'line_end': 212, 'start_byte_inclusive': 16846, 'end_byte_exclusive': 24268, 'bytes': 7422, 'sha256': 'e65ce8bafd8b7ab52a38b15bfed2664d35ae864f9bccba547fd98b6d58cc1f5f'}, {'name': 'used_lines_223_385', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 223, 'line_end': 385, 'start_byte_inclusive': 25689, 'end_byte_exclusive': 37295, 'bytes': 11606, 'sha256': '023ebdcf66b40103bed5b83547c1126d55032958bf00621458f7f76418be0410'}, {'name': 'used_lines_470_524', 'container': 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'line_start': 470, 'line_end': 524, 'start_byte_inclusive': 44043, 'end_byte_exclusive': 51631, 'bytes': 7588, 'sha256': '3b0ce37a60a946dec0d9e286a5583a5834f259571ebec86839d8067fce574eb3'}], 'use': 'Augmented H_P and uniform h_*, fixed-data nonempty runtime, actual tau-dependent R/I penalties and scalar/moment qualification; no preparation/release theorem imported.', 'body_map': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-autonomous-compiler-composition-20261015/BODY_MAP.json', 'bytes': 1064, 'sha256': '27602e43a43294f441e7739ea7c5e40f9f42ccb6e2c446c67546f26e455be313'}, 'canonical_binding': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-autonomous-compiler-composition-20261015/CANONICAL_BINDING.json', 'bytes': 4608, 'sha256': '8690db6370059341f45e0af1c94de65d90800fc809008df85d6650bb43914ef5'}, 'source_revision_supplied': '23a84c17353ea13dab449ca9a37800b5e4defcb4', 'revision_evidence_limit': 'Root-supplied current source base and separately preserved historical observations; this drafting task ran no Git command.'}], 'transitive_premises': [], 'preparation_release_intervals': [], 'mathematical_scope': 'Two direct accepted theorem interfaces. Clock, accuracy-scaled and protected-compiler history remains parent-owned transitive provenance in their exact bindings; this comparator imports no additional standalone transitive premise or preparation/release assertion. Git ancestry creates no scientific edge.', 'actual_current_git_observation': None}
EXPECTED_DIRECT_PARENTS = ('docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/AUTONOMOUS_COMPILER_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_SOURCE_BODY_PINS = [{'name': 'author_order14_body', 'container': 'docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 22100, 'end_byte_exclusive': 42170, 'bytes': 20070, 'sha256': '3189e031950d2613d1df69523260550f8d2da5c233a748dbf59144c525850c20'}, {'name': 'protected_order15_body', 'container': 'docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 42342, 'end_byte_exclusive': 65173, 'bytes': 22831, 'sha256': 'e23871d47ef5b3043a903c33deab317cf5a7c14bee86f06486baa699d14a3d93'}, {'name': 'exposed_reconciliation_body', 'container': 'docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 65350, 'end_byte_exclusive': 87254, 'bytes': 21904, 'sha256': '6d87cc9d686b895a4f5802b810943d9df6ea1304b3087cb08fa84b13272ef34d'}]
EXPECTED_SOURCE_MAP_SHA = 'cf5dec3968299eef910b0ea1697361e2ca40f9ae46d1cfd2843d40cd866d3eaa'
EXPECTED_SOURCE_FREEZE = 'd49d3e8bc11b60a28e2ea8c390ee4dc958d9b972bbe0c097337a149e6db9cba2'
EXPECTED_DRAFT_FILES = {'proposal/.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/BODY_MAP.json': {'bytes': 1068, 'sha256': 'cf5dec3968299eef910b0ea1697361e2ca40f9ae46d1cfd2843d40cd866d3eaa'}, 'proposal/.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PARENT_BINDING.json': {'bytes': 8802, 'sha256': '087534d44026519e14b268f3f03f3d9c7e6293635c65a3fd41f15b5374606100'}, 'proposal/.claude/science/physics-loops/toe-correlated-energy-comparator-20261015/PUBLICATION_STATE.json': {'bytes': 491, 'sha256': '98bdbeef104b00b4d05c323b72a1edecd4d2135326cf7c1d2b6ec6fbcf6bc340'}, 'proposal/docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 87254, 'sha256': '11d649d8c853143d2c68d31813c20639a80ae2ba3df693fb6ff9a8a2f2df125f'}, 'proposal/scripts/correlated_energy_comparator_2026_10_15.py': {'bytes': 21547, 'sha256': '02a48bb865b74a94628f5b1cb54e6b3998e8b9a76ec9ec80efc5bcfb0bc5cf2b'}}
EXPECTED_DRAFT_CANONICAL = {'proposal/docs/CORRELATED_ENERGY_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 87254, 'sha256': '11d649d8c853143d2c68d31813c20639a80ae2ba3df693fb6ff9a8a2f2df125f'}, 'proposal/scripts/correlated_energy_comparator_2026_10_15.py': {'bytes': 21547, 'sha256': '02a48bb865b74a94628f5b1cb54e6b3998e8b9a76ec9ec80efc5bcfb0bc5cf2b'}}
EXPECTED_PUBLICATION_STATE = {'kind': 'historical_source_only_draft', 'canonical_integration': None, 'git_base': None, 'root_publication_review': None, 'primary_execution': None, 'cache_execution': None, 'mutation_execution': None, 'graph_execution': None, 'publication_action': None, 'retained_audit': None, 'scientific_programs_run_this_draft': 0, 'historical_scientific_programs_replayed': 0, 'source_acceptance_sha256': '4e3d3af077b3dd5df8b11c6a7955f960c670a39a2aa16e52f6a409fb09e78067'}
EXPECTED_HELPER = 'scripts/correlated_energy_comparator_2026_10_15.py'
RECOVERY_TABLES = {'SOURCE_MANIFEST.json': 'sources'}
EXPECTED_HISTORICAL_RECORDS = [('author_exact_fixture_v1', 'fe0c28c58dbd0fbdecb3dfc0936262917f0398ade5f23d584fea611402d4580b'), ('root_acceptance_metadata_v1', 'd2df4ad0defa67c87db1c405b5140c6f2ce85d985648eadfb8bfb25b849decb2'), ('historical_head_correction_v1', '24e6963abddbb227fe1f7a49c7cae1d8c4b2c3b7b446ca1463558dddbb9c5779')]
EXPECTED_QUALIFICATIONS = '8ac73726ce226a725d66b9324f4d155f64781d3e8c95144db08a37164f9cba7b'
EXPECTED_QUALIFICATION_SOURCE = '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/correlated_energy_root_review/FINAL_QUALIFICATIONS.md'

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
    if row["schema"]=="author_exact_fixture_v1":
        receipt=json.loads(recovered(row["receipt"]));source=recovered(row["source"])
        require(receipt["exit_code"]==0 and receipt["elapsed_seconds"]>=0,"Original exact-fixture disposition")
        require(receipt["argv"][1]==row["launched_source"]["source"] and receipt["source_at_launch"]==row["source"]["source"],"Original launched path and distinct source capture")
        require(source==recovered(row["launched_source"]) and len(source)==receipt["source_bytes"] and digest(source)==receipt["source_sha256"],"Original fixture source identity")
        require(isinstance(receipt["started_at"],str) and isinstance(receipt["finished_at"],str),"Original fixture time fields")
        for key in ["stdout","stderr"]:
            require(receipt[key+"_path"]==row[key]["source"] and digest(recovered(row[key]))==receipt[key+"_sha256"],"Original fixture stream linkage")
        require(recovered(row["stderr"])==b"" and row["scope"]=="one_exact_gaussian_rational_degree14_fixture_only","Fixture scope")
    elif row["schema"]=="root_acceptance_metadata_v1":
        receipt=json.loads(recovered(row["receipt"]));source=recovered(row["source"])
        require(receipt["exit_code"]==0 and receipt["argv"][1]==receipt["child_source_at_launch"]["path"],"Actual source-acceptance command linkage")
        identity(source,receipt["child_source_at_launch"]);identity(source,receipt["source_capture"])
        identity(recovered(row["recorder"]),receipt["recorder"])
        for key in ["stdout","stderr"]:identity(recovered(row[key]),receipt[key])
        require(recovered(row["stderr"])==b"","Root acceptance error stream")
        observed=json.loads(recovered(row["stdout"]));acceptance=recovered(row["acceptance"])
        identity(acceptance,observed["acceptance"])
        require(digest(acceptance)==EXPECTED_ACCEPTANCE and row["scope"]=="root_source_acceptance_metadata_only","Source decision execution evidence, not new science")
    else:
        require(row["schema"]=="historical_head_correction_v1","Known historical evidence schema")
        protected=json.loads(recovered(row["protected_freeze"]))
        manifest=json.loads(recovered(row["exposed_manifest"]))
        old=manifest["head_provenance"]["historical_initial_observation"];new=manifest["head_provenance"]["new_exposed_observation"]
        require(old["returned_combined_output"].strip()==protected["source_head_verified"],"Historical HEAD identity retained")
        require(old["kind"]=="retrospective transcription from original tool result" and old["exact_process_timestamps_available"] is False and old["separate_streams_available"] is False,"Historical observation limits retained")
        require(new["kind"]=="fresh read-only observation during exposed comparison" and new["exact_process_timestamps_available"] is False and new["separate_streams_available"] is False,"Separate exposed observation limits")
        require(manifest["scientific_execution_count"]==0 and protected["scientific_execution"] is False,"No independent scientific executable inferred")
        require(row["scope"]=="source_identity_chronology_only","HEAD is provenance, not theorem or future integration base")

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
    require(check_packet['independent_scientific_execution'] is None,'No protected scientific executable')
    checks=check_packet['records']
    require([(r['schema'],(r['receipt'] if 'receipt' in r else r['protected_freeze'])['sha256']) for r in checks]==EXPECTED_HISTORICAL_RECORDS,'Exact historical record selection')
    for record in checks:
        check_receipt_members(record,sources)
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
    print('per_mode: order-14 and order-15 comparison definitions remain distinct; no propagation was executed')
    print('per_block: exact comparator text and historical source/receipt metadata checked only')
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

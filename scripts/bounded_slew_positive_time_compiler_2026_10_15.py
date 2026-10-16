"""Source-integrity proposal only; no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015"
EXPECTED_PARENTS = {'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md': (66336, 'c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2', 'accuracy_scaled_compiler_bounded_theorem_note_2026-10-15'), 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md': (97212, 'db922c9b3f67a603961f5a621a67eea7fa4894b793befbcdd3b7b034011e540a', 'conditioned_positive_time_compiler_bounded_theorem_note_2026-10-15')}
EXPECTED_BODIES = {'protected_weak_bump_body': 'c6bf17a1e80e05dd7121031c3497d8c2149198e24f7ba0e4e289270540f93ff5', 'root_full_unitary_variant': 'c46422d545bf1b8eaa72345ed4cffe293e073da1cc4aa1903661fd7ff3771e6e', 'exposed_comparison_and_minimum_time_corollary': 'cc263f5f842c4d0f955d2d14bff78dcfbae4df0d331ed61fdb4d6b698868977f'}
EXPECTED_ACCEPTANCE = "270985de36fb34e6b4a91260d7a546eea7d2b859906f1464217b4e856bbb6868"
EXPECTED_GIT_BASE = '9ca474a32b3a4799d2d14cfee7580d77750422b4'
MANIFEST_SHA256 = '8ee6b6d19caab867a2e44ae044a7ad482d35542cced661ca20446cb48056e3f7'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/CHECK_RECEIPTS.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PARENT_BINDING.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/0add271622a6912ce736e43f106f90a4c40e09ab3115cdc0ec0ea6b7a10fd06f.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/12692fdfe7ce32ed2968680510eaaadc2be2daf6285d1ad7a4a049dda85cd01f.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/1909d938a96545ee60a5624470df424348c20d72cbd1f23e9c1e3d6fc4ea9fc7.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/1c142431607f2aa5756aea7837c1c318a6845653b59431aa96eea9223743c9ae.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/21d2ed433190d525bed8fb67372943e37cd31a3b3f084f243caab29a084d8f1d.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/2e31d1a55341ac00a0ce2cf6bf3d37df5b5c6b6e001317018084343445665171.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/2f8eec322d80768e59e47f3232f83d40a7cd0eb3c63e1fd02b22545654ec161c.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/36976a446947543bb9b7b18a7ad1e487d6117ad0bf543767f74a488eb84ccb2b.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/4edfc8744d107900b883c5c0d910cff51ec1d3408adcc8f39a7cb95909ac668c.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/5e7ebdfae78ee5d1eea22022f0a0ef565e2db99f85a7a556e08cc7626ede02bc.py', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/65791cefb0ce1ed605e72f7ba2487343373ac64136bf141af3a309fba96db291.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/687b165fd7be31dbab93e7d854ab1755d84a51380ef93743419dc24947ef2b6d.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/77db636195c694110e353797fbd2da9c8f40e828c4b1214218a54c4b070777e1.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/8500a4ea92a5e9f25733504ccccd18eadfcc4026c35ea2a75397dd55ed69f956.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/91c7ad105285fe5b12bb99f8b3bf4a14734fe857d0881b8aaaba2679cc0350e4.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/9b58b1329d4eca12d802151ecd10f0b536fee45b665f97626386917c3d2d5ad1.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/ae4f0bce5744128bc06b97c551bb8a04329cd877b82ea36c3b3bbfcba19f53e7.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/b2161150997749c72ad1e0867a4fcf519ebdbfa07bd526d1faa552eb1f567428.py', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/b506680ca281808529a9a137646b2934a05765d362287a0c04b2fe4b82e8e79a.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/be708cea3ddb81371c4b47ca88d2648c2a01b727b441cd317bd68ca84662b81c.py', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/ccbe3903cd4231130db3a3aed1cb46227c273405edb59cd00b9919fd424f2603.py', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/da9577d8a249ca22584d70fa3ea86ebd11c1f777480f179d8c42a42818957416.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/e6180a226a0498b826249bce8e6b81e09947999cba22725aaa9c0a04645b79f3.json', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/e8c1ae2973483790e61e118ced6f53b6b81459682d09df5f78570048874acb9a.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/binding_sources/f1706af10835754541043f1cbfe34dfb9b8860b9606e4337f05e5a643dc2b948.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/04055accf8580a34501198d0afdc9929ed84cff4082589cff43912c6a13fcf8a.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/0655df53a9998bcc4d21331327134111be2c7775c7eace054b0bdca6f0c7d4f1.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/08a88b6c5a8f27cdf3f6cc62e2ad24232d592975cf4d4ab509af0045892af639.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/0fda1e787e39eb405291055b1d92f981627a819104ca2ed8a3b8723a342ed2f9.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/1a1dc0cdbc9b0a51b8f345b3a7a5e8a353375c24e536c507c495fbf25d984491.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/1ac34e79dc8e935e976faff9c30e6522a9789d0a60f69d7c51dffa00fb0739dc.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/270985de36fb34e6b4a91260d7a546eea7d2b859906f1464217b4e856bbb6868.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/278dc3607435a0f40acf56cb33d3a793083dac950d2631a44e194608e3846ba7.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/3780da2bf52f63fd6c9972fe5392921a8cd255f01aca5cdd426be81a1433316f.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/5491d4a68ba50bd555a6d42c438bb82df2f9639225829c30af69f6f7f5ac1679.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/57095124c667495dbff696c517cc0da2f950725cc95b25bc5aefcd67e3127b96.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/618e0082afc870c475736926a8e2ceb22bbdf1831acc0dbfdd5fcc32b6a9acc4.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/6beb1dfb5028302836342c8f53c28d29b74d1e67048ef02d29e55a4e9f5c0c16.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/76bb338ff6c3cf62ebba7d205588a970768942c184c44f7adc81c74a0140aa46.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/775c916b371db7faf8fc5545d05ed811c45e512b671e6b11ea85eaef4bca9226.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/7d526e7309c7676b75d492d6e7e81b3416f6f2bbc903b5f08508c146a1086e4f.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/8ac690365a806f10876cd3272c9e1ad6d731f67959403a1476b441d58b39d767.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/9932da872269a61dff350c846e438f9a69fae5a34694107a922a2a30afb9c55a.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/ba8cd3012b1166f7b307722ef33ebb7955d641d9651b5f182bb49b2c3038d0cc.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/bc6d975b98dd3c610b687ea3eb32b22f25197fe9b723047df00fdc2e5bce0fa6.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/c65e19954074bcae5a68a65fe4ca2fcb9f5a5166ed86d849ba0ef76ebde5e670.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/c82e13371f9f8326b73b7c0e1e777cd7ba829a5d63e2b238b24c049cb6779d47.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/c8d7d2178e400c19429b0e0c716212bda9274eb076d2255f5e91a25caf487b18.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/cf182b8f14d130ff4d845e78cf986e00ff625a33037b24c655470d3393479ee5.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/d0d4dc6619d9452b9b975612c973e13e3dac2faed3cdd5483801371aab7552bf.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/ddf30e6d5ba22aec6d9984aa848a62148929959c9b566ed4cedb04d730c7b84d.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/e161fa0ec167b09b15690bcdc8082d43fbfa052e32e0e2086145490f8698ac56.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/e7a57d12e5368a35cd25e3177f82ee9e869180db91fe33b18875525a90a67572.blob', '.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/source_recovery/f0c7c815f56be5a3db2aab5793830663517e6575364ec190fb0ce3c7749d4bc3.blob', 'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md')
METADATA_CHECK_COUNTS = {"passed": 0, "failed": 0}

EXPECTED_ROOT_REVIEW_SHA = '1909d938a96545ee60a5624470df424348c20d72cbd1f23e9c1e3d6fc4ea9fc7'
EXPECTED_ROOT_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_bounded_slew_publication_review/record_review.py')
EXPECTED_CANONICAL_REVIEW_SHA = '687b165fd7be31dbab93e7d854ab1755d84a51380ef93743419dc24947ef2b6d'
EXPECTED_CANONICAL_REVIEW_COMMAND = ('python3', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/root_bounded_slew_integration_review/record_canonical_review.py')
EXPECTED_PREBINDING_PRIMARY = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/bounded_slew_positive_time_compiler_2026_10_15.py', 'bytes': 39374, 'sha256': '8d59144ce3c87bfeedb9551dc7d245efe554abf4421a2a0a12a030c821ab1076'}
EXPECTED_INTEGRATION_COMMON = {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bounded_slew_integration_proposal/bounded_slew_common.py', 'bytes': 55814, 'sha256': 'be708cea3ddb81371c4b47ca88d2648c2a01b727b441cd317bd68ca84662b81c'}
EXPECTED_BASE_PR = 9624
EXPECTED_BASE_BRANCH = 'physics-loop/toe-autonomous-compiler-composition-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-accuracy-scaled-compiler-20261015'
EXPECTED_REPOSITORY = 'jonathonreilly/qubit-lattice-axiom-framework'
EXPECTED_PARENT_BINDING = {'canonical_parents': [{'path': 'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'bytes': 66336, 'sha256': 'c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2', 'claim_id': 'accuracy_scaled_compiler_bounded_theorem_note_2026-10-15', 'role': 'direct_mathematical_parent', 'accepted_body_intervals': [{'name': 'root_degree_D', 'container': 'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 19188, 'end_byte_exclusive': 31871, 'bytes': 12683, 'sha256': '6cae05fe6569b630041095b2cd44ad53a2cfedebdd0de30cd411975729f0186b'}, {'name': 'separately_attributed_k0_readout', 'container': 'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 32026, 'end_byte_exclusive': 33881, 'bytes': 1855, 'sha256': '899a28b936f5d8213ca2fbf28da6dc0bf0bc59534a64b97d8f2116db53ff9dc5'}, {'name': 'source_exposed_assessment', 'container': 'docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 34029, 'end_byte_exclusive': 66336, 'bytes': 32307, 'sha256': 'c9c098724bd13d87ce129f291ff7f75d7862651a85c17034a161de3ff0e124a8'}], 'body_map': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-accuracy-scaled-compiler-20261015/BODY_MAP.json', 'bytes': 1053, 'sha256': '57095124c667495dbff696c517cc0da2f950725cc95b25bc5aefcd67e3127b96'}, 'canonical_binding': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-accuracy-scaled-compiler-20261015/CANONICAL_BINDING.json', 'bytes': 2421, 'sha256': 'ddf30e6d5ba22aec6d9984aa848a62148929959c9b566ed4cedb04d730c7b84d'}, 'source_revision_supplied': 'd789fef0a544f91feceb20500a15bacc3374f08b', 'revision_evidence_limit': 'No Git command run; canonical bytes verified against existing local binding records.', 'source_head_supplied': '9ca474a32b3a4799d2d14cfee7580d77750422b4'}, {'path': 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'bytes': 97212, 'sha256': 'db922c9b3f67a603961f5a621a67eea7fa4894b793befbcdd3b7b034011e540a', 'claim_id': 'conditioned_positive_time_compiler_bounded_theorem_note_2026-10-15', 'role': 'direct_mathematical_parent', 'accepted_body_intervals': [{'name': 'independent_author', 'container': 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 39210, 'end_byte_exclusive': 70080, 'bytes': 30870, 'sha256': 'dd6cca8552a117d97f7be21c7b999ecd2276382f6cc762954bd97d00e3a6ff04'}, {'name': 'comparison', 'container': 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 70233, 'end_byte_exclusive': 97212, 'bytes': 26979, 'sha256': '227180a0822eab4e3dbfc002b6604d914af23589c29add9cca71e1a2f3ae2db0'}], 'body_map': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/BODY_MAP.json', 'bytes': 1063, 'sha256': '04055accf8580a34501198d0afdc9929ed84cff4082589cff43912c6a13fcf8a'}, 'canonical_binding': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/CANONICAL_BINDING.json', 'bytes': 2487, 'sha256': 'bc6d975b98dd3c610b687ea3eb32b22f25197fe9b723047df00fdc2e5bce0fa6'}, 'source_revision_supplied': None, 'revision_evidence_limit': 'No Git command run; canonical bytes verified against existing local binding records.', 'source_head_supplied': '9ca474a32b3a4799d2d14cfee7580d77750422b4'}], 'transitive_premises': [], 'preparation_release_intervals': [], 'scope': 'Only fixed complete plant, positive path/port interface, computable augmented polynomial certificate and parent scalar/actual-time ledger. No autonomous controller import. Source HEAD supplied, no Git command run here.'}
EXPECTED_DIRECT_PARENTS = ('docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_SOURCE_BODY_PINS = [{'name': 'protected_weak_bump_body', 'container': 'docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 15507, 'end_byte_exclusive': 34985, 'bytes': 19478, 'sha256': 'c6bf17a1e80e05dd7121031c3497d8c2149198e24f7ba0e4e289270540f93ff5'}, {'name': 'root_full_unitary_variant', 'container': 'docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 35160, 'end_byte_exclusive': 46641, 'bytes': 11481, 'sha256': 'c46422d545bf1b8eaa72345ed4cffe293e073da1cc4aa1903661fd7ff3771e6e'}, {'name': 'exposed_comparison_and_minimum_time_corollary', 'container': 'docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'start_byte_inclusive': 46836, 'end_byte_exclusive': 56503, 'bytes': 9667, 'sha256': 'cc263f5f842c4d0f955d2d14bff78dcfbae4df0d331ed61fdb4d6b698868977f'}]
EXPECTED_SOURCE_MAP_SHA = '8500a4ea92a5e9f25733504ccccd18eadfcc4026c35ea2a75397dd55ed69f956'
EXPECTED_SOURCE_FREEZE = '0add271622a6912ce736e43f106f90a4c40e09ab3115cdc0ec0ea6b7a10fd06f'
EXPECTED_DRAFT_FILES = {'proposal/.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/BODY_MAP.json': {'bytes': 1121, 'sha256': '8500a4ea92a5e9f25733504ccccd18eadfcc4026c35ea2a75397dd55ed69f956'}, 'proposal/.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PARENT_BINDING.json': {'bytes': 4685, 'sha256': '8493d537bb7ae2f4796339f629140b8df13d44db99754bd4de21f88a3ecb8b2e'}, 'proposal/.claude/science/physics-loops/toe-bounded-slew-positive-time-compiler-20261015/PUBLICATION_STATE.json': {'bytes': 491, 'sha256': '481769f173b46edafdfd6e11c3c583ff359fe963ce48c0a5e175c16aae8fa88a'}, 'proposal/docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 56503, 'sha256': '671eebdd3e4e234e3fa6467cc940c28c3499311f736b95ba681613701652438a'}, 'proposal/scripts/bounded_slew_positive_time_compiler_2026_10_15.py': {'bytes': 20509, 'sha256': 'fe766ef2c061c93a72d694162debb58f16dfe2d3d2b74cbdc2aca707c1fe8ab9'}}
EXPECTED_DRAFT_CANONICAL = {'proposal/docs/BOUNDED_SLEW_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md': {'bytes': 56503, 'sha256': '671eebdd3e4e234e3fa6467cc940c28c3499311f736b95ba681613701652438a'}, 'proposal/scripts/bounded_slew_positive_time_compiler_2026_10_15.py': {'bytes': 20509, 'sha256': 'fe766ef2c061c93a72d694162debb58f16dfe2d3d2b74cbdc2aca707c1fe8ab9'}}
EXPECTED_PUBLICATION_STATE = {'kind': 'historical_source_only_draft', 'canonical_integration': None, 'git_base': None, 'root_publication_review': None, 'primary_execution': None, 'cache_execution': None, 'mutation_execution': None, 'graph_execution': None, 'publication_action': None, 'retained_audit': None, 'scientific_programs_run_this_draft': 0, 'historical_scientific_programs_replayed': 0, 'source_acceptance_sha256': '270985de36fb34e6b4a91260d7a546eea7d2b859906f1464217b4e856bbb6868'}
EXPECTED_HELPER = 'scripts/bounded_slew_positive_time_compiler_2026_10_15.py'
RECOVERY_TABLES = {'SOURCE_MANIFEST.json': 'sources'}
EXPECTED_HISTORICAL_RECEIPTS = ['08a88b6c5a8f27cdf3f6cc62e2ad24232d592975cf4d4ab509af0045892af639', '1a1dc0cdbc9b0a51b8f345b3a7a5e8a353375c24e536c507c495fbf25d984491', '76bb338ff6c3cf62ebba7d205588a970768942c184c44f7adc81c74a0140aa46']

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
    receipt=json.loads(recovered(row["receipt"]))
    require(receipt["exit_code"]==row["recorded_exit_code"],"Original check disposition retained")
    source=recovered(row["source"])
    if row["schema"]=="root_run_v1":
        require(receipt["argv"][1]==receipt["child_source_at_launch"]["path"],"Original ramp source path linkage")
        identity(source,receipt["child_source_at_launch"])
        identity(recovered(row["recorder"]),receipt["recorder"])
        for field in ["stdout","stderr"]:identity(recovered(row[field]),receipt[field])
    else:
        require(row["schema"]=="symbolic_v1","Known original check schema")
        matches=[r for r in receipt["source_at_launch"] if r["path"]==receipt["argv"][1]]
        require(len(matches)==1,"Original symbolic source path linkage");identity(source,matches[0])
        require(len(row["captured_inputs"])==len(receipt["source_at_launch"]),"Complete original check capture list")
        for capture,original in zip(row["captured_inputs"],receipt["source_at_launch"]):identity(recovered(capture),original)
        for field in ["stdout","stderr"]:require(digest(recovered(row[field]))==receipt[field+"_sha256"],"Original check stream identity")
    require(row["scope"] in {"exact_scoped_symbolic_only","finite_floating_point_ramp_diagnostic_only"},"Historical checks retain narrow scope")

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
    require([r['receipt']['sha256'] for r in checks]==EXPECTED_HISTORICAL_RECEIPTS,'Exact historical check receipt selection')
    for record in checks:
        check_receipt_members(record,sources);historical_receipt(record)
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
    print('per_mode: weak-bump and full-phase ramp contracts remain distinct; no propagation was executed')
    print('per_block: exact compiler sources and historical/actual receipt metadata checked only')
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

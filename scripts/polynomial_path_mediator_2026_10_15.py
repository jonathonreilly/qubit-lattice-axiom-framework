"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-polynomial-path-mediator-20261015"
EXPECTED_PARENTS = {'docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md': (110611, '0c3f1b569d41b75fa1c23e815e55f8481af640a9b292469e056541f698702ed1', 'basis_state_waveform_clock_bounded_theorem_note_2026-10-15')}
EXPECTED_ACCEPTANCES = {"polynomial_path_mediator":"8f26be5fb28c966ea405bb97facb0a16f9abdbd75c110de23e96f875aa9a8df2"}
EXPECTED_PARENT_REVIEW = {'canonical_parent': 'docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'canonical_parent_sha256': '0c3f1b569d41b75fa1c23e815e55f8481af640a9b292469e056541f698702ed1', 'reviewed_body_sha256': {'root_author': '0fc2b7046b24c535ebd9549449601c42d8af6e3a9f95ca3e5a45a16eabb5eb46', 'independent_author': '84f03ca0de42477399e9a797f659b971e6beb88505d59fce6aaca5c6147acf39', 'comparison': '8c3ba783afdfa526e9da08df73760d8b6f0477c2598002b4c71fc042e480a2c2'}, 'records': [{'role': 'parent_conditional_source_acceptance', 'source': 'campaign/basis_state_clock_root_review/ACCEPTANCE.md', 'bytes': 2495, 'sha256': '174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0.blob'}}, {'role': 'parent_source_publication_wrapper_acceptance', 'source': 'campaign/basis_state_clock_publication_root_review/ACCEPTANCE.json', 'bytes': 12693, 'sha256': 'eb31fa43c503cfc659e3e5d18c7eafe3ed2927ee3efb45810c5ab4371a8d2708', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/eb31fa43c503cfc659e3e5d18c7eafe3ed2927ee3efb45810c5ab4371a8d2708.blob'}}, {'role': 'parent_actual_regular_publication', 'source': 'campaign/publication_integration/basis_state_clock/PUBLICATION.json', 'bytes': 1554, 'sha256': 'bb241ae264dce6f435563a7a145ec8d7969f8f5a5463ef22f25727d0d45b815a', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/bb241ae264dce6f435563a7a145ec8d7969f8f5a5463ef22f25727d0d45b815a.blob'}}, {'role': 'parent_actual_attachment', 'source': 'campaign/publication_integration/basis_state_clock/ATTACHMENT.json', 'bytes': 216, 'sha256': '397c9cfc4128971a4604f477b664dfd2748ea6c680ae052213b713c998041d9e', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/397c9cfc4128971a4604f477b664dfd2748ea6c680ae052213b713c998041d9e.blob'}}, {'role': 'parent_actual_staged_root_decision', 'source': 'campaign/publication_integration/basis_state_clock/ROOT_STAGED_REVIEW.json', 'bytes': 1698, 'sha256': 'af5534f36f81045da14e2203739c963c49b243893522c6148a6fa6453ddcfc99', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/af5534f36f81045da14e2203739c963c49b243893522c6148a6fa6453ddcfc99.blob'}}, {'role': 'parent_actual_canonical_body_map', 'source': 'repository/.claude/science/physics-loops/toe-basis-state-clock-20261015/BODY_MAP.json', 'bytes': 1032, 'sha256': 'd9b384259bc086aedd10b8bc5cdac3640d8d5dcc59344fa98ce4d6a38d4ac67e', 'recovery': {'kind': 'blob', 'path': '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d9b384259bc086aedd10b8bc5cdac3640d8d5dcc59344fa98ce4d6a38d4ac67e.blob'}}], 'gzip_reviews': [], 'publication': {'utc': '2026-10-15T20:45:07.261001+00:00', 'baseRefName': 'physics-loop/toe-local-gibbs-controller-source-20261015', 'headRefName': 'physics-loop/toe-basis-state-clock-20261015', 'headRefOid': 'aa4beefe822ee4564adaa48fd7ef5e3a5c033bf9', 'isDraft': False, 'number': 9619, 'state': 'OPEN', 'url': 'https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9619', 'tree': 'f6cd39bef5bd6c27b87e29f342a447890ab36f74', 'base_head': 'ce8e1842601b067f11141441aa73b1ccfd14476e', 'source_note': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'bytes': 110611, 'sha256': '0c3f1b569d41b75fa1c23e815e55f8481af640a9b292469e056541f698702ed1'}, 'primary': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree/scripts/basis_state_waveform_clock_2026_10_15.py', 'bytes': 27705, 'sha256': 'be56d6b12e89e981a92e672bae6e592f768383c69bd808d1057c4133586d1e86'}, 'body': {'path': '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261014_214309/publication_integration/basis_state_clock/PR_BODY.md', 'bytes': 3191, 'sha256': '2ae75f9a0f8fafcdc11b4e15c1601c8e62067eeee8f2af89dc22b731a9a44255'}, 'science_merged': False, 'main_pushed': False, 'audit_applied': False, 'editable_prompt_files_changed': [], 'attachment_status': 'Root must immediately call attach_artifact with this created PR URL.'}, 'scope': 'Exact parent bodies and actual supplied acceptance/publication evidence; provenance is not another theorem edge'}
EXPECTED_GIT_BASE = 'aa4beefe822ee4564adaa48fd7ef5e3a5c033bf9'
EXPECTED_BASE_PR = 9619
EXPECTED_BASE_BRANCH = 'physics-loop/toe-basis-state-clock-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-local-gibbs-controller-source-20261015'
MANIFEST_SHA256 = '6f743a62fbdde733625f2ceabb7e93279053867b7aa0b00ba7ba38f80f6ade29'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/HISTORICAL_SCIENCE.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/PARENT_REVIEW_BINDING.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/1044880b42acb6830366c27da99969c2e9b62de5904ef149dc03c92100e51bc3.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/2079ecf13e0a6008c736bc3ab76d3723901a8e1bf6039aeca344c850ae9f710c.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/2148b8810f6dac38b8b6b4fe0054124e82bcd22d7f626532ae6ceb3f0817bef1.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/267a03e415ed0bfa094fc89b3b201c6b17daf8b11df71744e0c0ac0b6fba035c.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/2e2cbd31fe6c8ed92c80286f9cf32ca2bf553ad37ad569f561c3d29340f995e6.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/397c9cfc4128971a4604f477b664dfd2748ea6c680ae052213b713c998041d9e.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/47f80d0950f11be804f0b67405fd2c46512164da57dae68befc80551e9be9ff0.py', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/6915958aa483d7d75f380a870e00e3b4150da0bf3a5d080c5f292b2c661348a2.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/922961127462c9856df7728d73e1c9eb885424d6675bb722eb3a99210fcdfb56.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/a7d5d8d63a9b26f49b6065d82cd62ad93146f3e2503aeb3fd90daa4d4ecd26e1.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/acac29fb6a92fcbf4a14cd375f8c80525c171d8d159a710c62a196b5863d8b12.py', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/b859501f0dec81dc34b1f3dd48bf0ebcad2f5ada77a2846164bb4498826f63f7.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/bb241ae264dce6f435563a7a145ec8d7969f8f5a5463ef22f25727d0d45b815a.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/d78856437e14673ea7c0a444c645527b2ca6a97fd4f99e81d9101b454cbff25f.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/d9603a48b4afcf830617821b535d830f87cad2d63f1302c4ad22ff86f2b55fe3.json', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/binding_sources/f2fac13228af7cce764dd69e4f1f1ca3e165cfc2acca26a4f57965bc73aefb1d.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/087617a8d82b8547f9c4fd1f0c3552002ab7c6530a28db8318cdc67900e3e435.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/182e580b13ee516fbc5e1f3ae4ca999bd47eba6b1cfe474542bab995f267cb91.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/1c4b0100775304f75e0fdd9ce110a702623c7e3785823caecc3e112da5bf6646.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/2764f24509514fd1cd07cc736276e6af179ad2f733deabd21ef6aa0df8171773.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/2a3310794f09b61c77122ca3e627544a3a677c61578712aafa891c13be8badd9.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/311d09793428b5a5ba64be3577a611d42b4671c60d1651718c8ab23e650e5a8f.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/31dcf82b746333e40360f276b95974b58d6c156c26b0e65cb371162b4096e70c.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/321c3aaa50591eb381bbbc9b51d4d00ee52f4ef7f6af86ab0b7e9358f1510654.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/397c9cfc4128971a4604f477b664dfd2748ea6c680ae052213b713c998041d9e.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/453e57ffafe5e58cf55c7b61238d4c42ca7e5496e754a1c44154f4329bfdb6e9.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/4d813dbb555a72794708ca914400734ba48c6354bb6e9abc63a6c8e93b0b7098.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/4e81647ca2654e8ff5442ebcd793060b525e0d8db561ef06efb1f750b29246fe.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/583375468e3b3c15a52ded16fa5732eb4f6fe320c5047fc2e441cca7195b6eba.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/5ceff7d58e226d50fe500293afecf5cdbb4d0cd17978a57df83a187d1e55c191.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/60389ac284bab6672606985a55b6ab9ea5d532ac1fcb24aa83c02cf6f411ff04.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/608a0efacdd96eeaedad95e976e3a4a50b4ef7ad8dde1f66a3ee571c33c5cd23.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/63c05ab4ddbe3f6acdfcf0efae70565d5b6230adaf1d3eef7b69f858525b836c.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/70eea76efd8e224e4d5143856f6e4af6949e17fcf032b54e700ee4b1bb4e77f5.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/733fc6879d9e0e8e43d3471699a820919ddecd7f8d922fb010e4bac0f07e9710.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/78ecb13acae41c653c96f3c5b2943f69aa4969022a7061f03318189b27cd88e2.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/7fca75e9786ccaa2a28ebd7c6935a40de8801c3a38b92dfc3b5027146c549d90.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/8ad3e890a822ac7b71b47789ec6e80b977a15a15f8adb48d1816c3d84164a8b9.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/8f26be5fb28c966ea405bb97facb0a16f9abdbd75c110de23e96f875aa9a8df2.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/8f29f1e4e660dad0aeb38aefa61883e4a96f6bd95fa3fff115b41893f57485a6.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/94de40add86a3ac93157648c55c7aac725b3407f7d54b33cb4baa0ad659c75ff.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/95b81f81469ddb965098152d03ec07fe4ff2314ae69f3b78ec77c126193d07ac.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/99dac9b9ee68e8c63c54a092925e3fe12dcdbb758d4376134b1136d1684587ed.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/a458606f9fd7c090166107f0da7636cd89abe0c7a2fcd08da3416d76c5465ac0.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/a5c757fdcb9e29ee12efb2681ceea5f3399cba93e5a04f36c153b8cbf3c5b48f.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/aa6733e334581dc4b8bb912eb868eb7d5dfb01d1947c7b72161957b00e5d9d86.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/ad256ec358c129c28dde34df661726e51a625db527b545fba51d46b719546b5b.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/ade7e28f58c4029eb4505cc29f1a951e7ee135db895928385aaf8699294c3d71.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/aeacc0be08481cd931d9875d9353bed27a0a553a5d1ae94fa8e19ddf0298bba4.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/af5534f36f81045da14e2203739c963c49b243893522c6148a6fa6453ddcfc99.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/b39e2d58c0e04fb6ef3c8f1d1574af1c647995221c0b4151fe12e65ff18a7da5.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/b3c1a64c5020981e8e87b55b3f121c65f16605fe1e8636e34c3269c91b4ea024.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/b4e8a005ae93e5d3de7f6b5b5b678ab47718a00fb4aaf3b20009881933815607.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/b9092f19da5da3c8ef92b35b4018179e06bf4d38b4813779a709b22e1d0d299a.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/bad4a15eae8d700a75d8f29092283818470fd2663fc107d4a03c92fb89220218.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/bb241ae264dce6f435563a7a145ec8d7969f8f5a5463ef22f25727d0d45b815a.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/c66b668c3d0edfb1351dc1f4c1a2da14850926b5ef7c7c5d830ae1964cc03e8e.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/c707dc710885a6c2b988454a98667abc9a0e0c364fe2dbcf6832489cff464e4a.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/cce2637c4993f041808aabb9ef9ba966091be8946d0b133fe4dd06033da2a88a.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/cf0caf28149b8b79a937bad165f5ea2994e3007debf19be9e7e99ca64aa3f4f4.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d67a3c92c02c0e672bb57ea6a026f49691677ef9fda0313a8ec97a7f46b3a011.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d6bf0d9f029926830734ddd3c8974b77dae947247ef92da601dc62c9f29c9383.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d9a97fd0afd0682c358025a2e6f19e2f450f3d95c55e8b5d46a71159dc875a2d.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/d9b384259bc086aedd10b8bc5cdac3640d8d5dcc59344fa98ce4d6a38d4ac67e.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/e3af5bfdd3d9685990e72c1e3ce547de8d25ad080188727eb6c4caead852bb8f.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/e8aa4c0c1c4201387604c7c384bfe3a745cfe05c9cd3df488a1cd02c91f66d8f.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/eb31fa43c503cfc659e3e5d18c7eafe3ed2927ee3efb45810c5ab4371a8d2708.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/eb5027b361fd91e2dfc944f39d86a448dbfc1d30994fc1a3e2a54e561f35eb32.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/f96a31e5e2369128cd1dd1129027d6c65af6aa6817f6c9cee4f22c4ea7e8d39d.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', '.claude/science/physics-loops/toe-polynomial-path-mediator-20261015/source_recovery/fc7026d4698947ad1d2ab52fdd2c8c44ddd1216df76f6ab072bc3ba747a3e95e.blob', 'docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/POLYNOMIAL_PATH_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'root_mass_m3': '45c211e6c44bb694cf01ac11e15ede8a85442b95baa125dd0b01519a031ee893', 'independent_mass_m2': '0620431acdfc9b0c9e36f4ec1364cf2eaff8891ba2697aeadee37501b1e493a7', 'source_exposed_comparison': '3cc7a9d32e0019edef91c1f699e396bf84dd31fbe0642d6a32170d14538b9067'}
EXPECTED_PARENT_BODIES = {'root_author': (23256, '0fc2b7046b24c535ebd9549449601c42d8af6e3a9f95ca3e5a45a16eabb5eb46'), 'independent_author': (29173, '84f03ca0de42477399e9a797f659b971e6beb88505d59fce6aaca5c6147acf39'), 'comparison': (34647, '8c3ba783afdfa526e9da08df73760d8b6f0477c2598002b4c71fc042e480a2c2')}

def require(ok, message):
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

def execution_evidence(evidence, python_source):
    receipt=json.loads(bound_blob(evidence["execution"]))
    require(receipt.get("exit_code")==0 and isinstance(receipt.get("argv"),list),"Captured successful execution required")
    require(isinstance(receipt.get("start_utc"),str) and isinstance(receipt.get("end_utc"),str),"Captured execution time schema")
    require(isinstance(receipt.get("elapsed_seconds"),(int,float)) and receipt["elapsed_seconds"]>=0,"Captured execution duration")
    identity(bound_blob(evidence["recorder"]),receipt["recorder"])
    stdout=bound_blob(evidence["stdout"]);stderr=bound_blob(evidence["stderr"])
    identity(stdout,receipt["stdout"]);identity(stderr,receipt["stderr"])
    require(stderr==b"","Unexpected evidence error stream")
    if python_source:
        source=bound_blob(evidence["source"])
        identity(source,receipt["child_source_at_launch"])
        require(len(receipt["argv"])==2 and Path(receipt["argv"][0]).name.startswith("python") and receipt["argv"][1].endswith(".py"),"Root source-review command")
    else:
        require(receipt["child_source_at_launch"] is None,"Direct PR observation has no Python child source")
    return receipt,json.loads(stdout)

def recovered(row):
    recovery=row["recovery"]
    if recovery["kind"]=="blob":
        require(recovery["path"] in AUDIT_INPUT_PATHS,"Recovery blob must be declared")
        data=safe(recovery["path"]).read_bytes();identity(data,row);return data
    if recovery["kind"] in {"body_interval","external_body_interval"}:
        return interval({**recovery,"bytes":row["bytes"],"sha256":row["sha256"]})
    require(recovery["kind"]=="external_pinned" and recovery["path"] in EXPECTED_PARENTS,"Known external parent only")
    data=safe(recovery["path"]).read_bytes();identity(data,row);return data

def historical_fixture():
    evidence=read_json(PACKET+"/HISTORICAL_SCIENCE.json")
    require(evidence["historical_scientific_programs"]==1 and evidence["executed_this_draft"] is False,"One historical fixture, no replay")
    require(evidence["comparison_checker_inspected_fixture"] is False and evidence["comparison_checker_notification_exposure"] is True,"Honest comparison exposure scope")
    receipt=json.loads(recovered(evidence["execution"]))
    require(receipt["exit_code"]==0 and receipt["argv"][1].endswith("polynomial_matrix_fixture_2008.py"),"Actual historical scientific execution")
    for role,key in [("source","child_source_at_launch"),("recorder","recorder"),("stdout","stdout"),("stderr","stderr")]:
        identity(recovered(evidence[role]),receipt[key])
    require(recovered(evidence["stderr"])==b"","Historical fixture error stream")
    require((evidence["source"]["bytes"],evidence["source"]["sha256"])==(5571,"ade7e28f58c4029eb4505cc29f1a951e7ee135db895928385aaf8699294c3d71"),"Exact historical fixture code, not executed")
    result_raw=recovered(evidence["results"]);result=json.loads(result_raw)
    require((evidence["results"]["bytes"],evidence["results"]["sha256"])==(8166,"311d09793428b5a5ba64be3577a611d42b4671c60d1651718c8ab23e650e5a8f"),"Exact historical fixture results")
    printed=json.loads(recovered(evidence["stdout"]));identity(result_raw,printed["result"])
    identity(recovered(evidence["source"]),result["source"])
    require(result["scientific_programs_run"]==1 and result["universal_proof"] is False and result["independent_derivation"] is False,"Finite exposed numerical scope")
    require({r["sha256"] for r in result["proof_sources"]}=={EXPECTED_BODIES["root_mass_m3"],EXPECTED_BODIES["independent_mass_m2"]},"Historical science source linkage")
    require(len(result["full_auxiliary_spectra"])==14 and len(result["response_checks"])==14 and len(result["full_auxiliary_one_clock_sector_correctors"])==4,"Saved fixture inventory only, not new mathematical checks")
    frozen=json.loads(recovered(evidence["freeze"]))
    require(frozen["scientific_programs_run"]==1 and len(frozen["files"])==6,"Historical scientific freeze scope")
    for row in frozen["files"]:
        candidates=[r for r in evidence.values() if isinstance(r,dict) and r.get("sha256")==row["sha256"] and r.get("bytes")==row["bytes"]]
        require(bool(candidates),"Historical fixture member recovery")
        identity(recovered(candidates[0]),row)
    recovered(evidence["interpretation"])

def main():
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and all(c in "0123456789abcdef" for c in EXPECTED_GIT_BASE) and isinstance(EXPECTED_BASE_PR,int) and EXPECTED_BASE_PR>0 and isinstance(EXPECTED_BASE_BRANCH,str) and bool(EXPECTED_BASE_BRANCH),"Future base not supplied: root must bind and review the actual head/PR/branch literals")
    mpath=PACKET+"/INPUT_MANIFEST.json"
    raw=safe(mpath).read_bytes()
    require(digest(raw)==MANIFEST_SHA256,"Input manifest identity")
    manifest=json.loads(raw)
    require(manifest["schema"]=="source_integrity_inputs_v1","Input schema")
    rows=manifest["inputs"]
    require(len({r["path"] for r in rows})==len(rows),"Duplicate input path")
    actual=PACKET+"/ACTUAL_BINDING.json"
    expected={r["path"] for r in rows}|{mpath,actual}|set(EXPECTED_PARENTS)
    require(set(AUDIT_INPUT_PATHS)==expected and len(AUDIT_INPUT_PATHS)==len(expected),"Literal declared-input closure")
    for row in rows: identity(safe(row["path"]).read_bytes(),row)
    note=safe(NOTE).read_bytes()
    header=note.split(b"---",2)[1].decode().splitlines()
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false",'upstream_dependencies: ["basis_state_waveform_clock_bounded_theorem_note_2026-10-15"]']:
        require(field in header,"Missing actual scope/binding field: "+field)
    body_map=read_json(PACKET+"/BODY_MAP.json")
    require(body_map["note"]==NOTE,"Body container")
    require({r["name"] for r in body_map["bodies"]}==set(EXPECTED_BODIES) and len(body_map["bodies"])==3,"Three immutable proof/comparison roles")
    for row in body_map["bodies"]:
        require(row["container"]==NOTE and row["sha256"]==EXPECTED_BODIES[row["name"]],"Immutable body identity")
        interval(row)
    parents=read_json(PACKET+"/DEPENDENCIES.json")["dependencies"]
    require(len(parents)==1 and {r["path"] for r in parents}==set(EXPECTED_PARENTS),"Exactly one direct mathematical parent")
    for row in parents:
        require((row["bytes"],row["sha256"],row["claim_id"])==EXPECTED_PARENTS[row["path"]],"Parent role or identity")
        identity(safe(row["path"]).read_bytes(),row)
        require(row["required_mathematical_body_names"]==list(EXPECTED_PARENT_BODIES),"Exact inherited proof roles")
        intervals=row["accepted_body_intervals"]
        require(len(intervals)==len(EXPECTED_PARENT_BODIES) and {r["name"] for r in intervals}==set(EXPECTED_PARENT_BODIES),"Parent body recovery roles")
        for r in intervals:
            require(r["container"]==row["path"] and (r["bytes"],r["sha256"])==EXPECTED_PARENT_BODIES[r["name"]],"Parent body identity")
            interval(r)
    parent_review=read_json(PACKET+"/PARENT_REVIEW_BINDING.json")
    require(parent_review==EXPECTED_PARENT_REVIEW,"Exact parent proof/review/publication binding")
    require(parent_review["canonical_parent"] in EXPECTED_PARENTS and parent_review["canonical_parent_sha256"]==EXPECTED_PARENTS[parent_review["canonical_parent"]][1],"Parent review canonical linkage")
    require(parent_review["reviewed_body_sha256"]=={k:v[1] for k,v in EXPECTED_PARENT_BODIES.items()},"All three inherited proof/review roles")
    for row in parent_review["records"]: recovered(row)
    require(parent_review["gzip_reviews"]==[],"Review is the inherited canonical comparison interval; no extra gzip edge")
    archive=read_json(PACKET+"/ARCHIVE_INDEX.json")["objects"]
    require(len({r["sha256"] for r in archive})==len(archive),"Recovery must be deduplicated by hash")
    for row in archive: identity(safe(row["path"]).read_bytes(),row)
    sources=read_json(PACKET+"/SOURCE_MANIFEST.json")["sources"]
    accepted={r["sha256"] for r in sources if r["role"]=="root_conditional_source_acceptance"}
    require(accepted==set(EXPECTED_ACCEPTANCES.values()),"Exact qualified polynomial-path acceptance")
    local_rows={r["name"]:r for r in body_map["bodies"]}
    external_rows={(r["container"],r["name"]):r for p in parents for r in p["accepted_body_intervals"]}
    for row in sources:
        loc=row["recovery"]
        if loc["kind"]=="body_interval":
            require(loc["body_name"] in local_rows,"Source body-map linkage")
            target=local_rows[loc["body_name"]]
            require(all(loc[k]==target[k] for k in ("container","start_byte_inclusive","end_byte_exclusive")) and row["bytes"]==target["bytes"] and row["sha256"]==target["sha256"],"Source body-map linkage")
        if loc["kind"]=="external_body_interval":
            require((loc["container"],loc["name"]) in external_rows,"External body-map linkage")
            target=external_rows[(loc["container"],loc["name"])]
            require(all(loc[k]==target[k] for k in ("container","start_byte_inclusive","end_byte_exclusive","bytes","sha256")) and row["bytes"]==target["bytes"] and row["sha256"]==target["sha256"],"External body-map linkage")
        recovered(row)
    archive_by_sha={r["sha256"]:r for r in archive}
    blob_sources={r["sha256"]:r for r in sources if r["recovery"]["kind"]=="blob"}
    require(set(archive_by_sha)==set(blob_sources),"Archive/source exact blob coverage")
    for digest_key,row in blob_sources.items():
        obj=archive_by_sha[digest_key]
        require(obj["bytes"]==row["bytes"] and obj["path"]==row["recovery"]["path"],"Archive/source semantic linkage")
    selection=read_json(PACKET+"/RECOVERY_SELECTION.json")
    signatures={(r["bytes"],r["sha256"],json.dumps(r["recovery"],sort_keys=True)) for r in sources}
    require(len({(r["freeze"],r["original"]) for r in selection["members"]})==len(selection["members"]),"Unique frozen source member rows")
    for row in selection["members"]:
        require(row["current_identity_verified"] is True,"Historical freeze member verification recorded")
        if row["recovery"] is None:
            require(row["selection_status"]=="not_selected_prior_source_snapshot" and isinstance(row["limit"],str),"Explicit omitted recovery scope")
        else:
            require((row["bytes"],row["sha256"],json.dumps(row["recovery"],sort_keys=True)) in signatures,"Selected member/source recovery linkage")
            recovered(row)
    historical_fixture()
    state=read_json(PACKET+"/PUBLICATION_STATE.json")
    require(state["kind"]=="dated_source_proposal_not_actual_binding","Historical state role")
    for field in ["canonical_binding","git_base","primary_execution","cache_execution","mutation_execution","graph_execution","publication_action","retained_audit"]:
        require(state[field] is None,"Historical null state must remain null: "+field)
    require(state["scientific_programs_run_this_draft"]==state["historical_programs_replayed"]==0 and state["historical_root_scientific_fixtures"]==1 and state["future_base_supplied"] is False,"Historical execution and pending-base scope")
    require(state["source_acceptances"]==EXPECTED_ACCEPTANCES,"Historical actual source decisions")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding required; source draft is unbound")
    require(binding["root_read_complete"] is True,"Actual root inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES and binding["git_base"]==EXPECTED_GIT_BASE,"Actual source decisions and requested base")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_polynomial_path_mediator_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
    require(canonical["bound_note_sha256"]==digest(note) and canonical["actual_git_base"]==binding["git_base"] and canonical["canonical_parent_sha256"]==binding["parent_sha256"],"Current binding identities")
    require(binding["raw_bodies"]==body_map["bodies"] and binding["canonical_parents"]==parents,"Actual body and parent structure")
    freeze=json.loads(bound_blob(binding["source_proposal_freeze"]))
    require(freeze["immutable_bodies"]==3 and freeze["mathematical_parents"]==1 and freeze["scientific_programs_run_this_draft"]==0 and freeze["historical_root_scientific_fixtures"]==1 and freeze["actual_binding"] is None,"Historical proposal seal scope")
    evidence=binding["root_review_evidence"]
    review_raw=bound_blob(evidence["review"]);review=json.loads(review_raw)
    require(review["kind"]=="root_source_publication_review" and review["root_read_complete"] is True,"Actual source-publication review schema")
    require(review["source_draft_freeze"]["sha256"]==binding["source_proposal_freeze"]["sha256"],"Reviewed proposal identity")
    require(review["decision"]=="Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.","Actual publication interpretation decision")
    require({r["name"]:r["sha256"] for r in review["body_pins"]}==EXPECTED_BODIES and review["parents"]==parents,"Root reviewed bodies and parent")
    require(review["parent_review_binding"]==parent_review,"Root reviewed exact parent review recovery")
    require({k:r["sha256"] for k,r in review["existing_source_acceptances"].items()}==EXPECTED_ACCEPTANCES,"Root reviewed source decisions")
    require(review["scientific_programs_run_this_review"]==review["primary_runs"]==review["historical_programs_replayed"]==0 and review["historical_root_scientific_fixtures"]==1,"Root source-review execution scope")
    _,result=execution_evidence(evidence,True)
    require(result["review"]["sha256"]==digest(review_raw),"Actual review output linkage")
    require(result["members"]==162 and result["sources"]==87 and result["exact_functions"]==27,"Actual reviewed source counts")
    review_seal_raw=bound_blob(evidence["review_freeze"]);identity(review_seal_raw,result["freeze"])
    review_seal=json.loads(review_seal_raw);require(len(review_seal["files"])==1,"Actual review seal membership")
    identity(review_raw,review_seal["files"][0])
    require(binding["scientific_programs_run_this_integration"]==binding["historical_programs_replayed"]==0 and binding["historical_root_scientific_fixtures"]==1,"Actual integration execution scope")
    receipt,observed=execution_evidence(binding["base_observation"],False)
    require(receipt["argv"]==["gh","pr","view",str(EXPECTED_BASE_PR),"--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual base observation command")
    require(observed["number"]==EXPECTED_BASE_PR and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]==EXPECTED_BASE_BRANCH and observed["baseRefName"]==EXPECTED_BASE_PARENT_BRANCH and observed["state"] in {"OPEN","MERGED"},"Actual base PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding["base_observation"].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(p in AUDIT_INPUT_PATHS for p in used),"Binding evidence literal closure")
    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and captured binding evidence only; no mathematical validation by execution","scientific_programs_run_this_primary":0,"historical_root_scientific_fixtures":1,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: exact coefficient text retained; no physical element or gate executed")
    print("per_site: fixed path and supplied isolation are preserved; no hardware test executed")
    print("per_mode: full-sector path proofs retained; historical fixture read only, no mode simulation executed here")
    print("per_block: three exact bodies, one parent and captured binding evidence checked")
    print("lattice_wide: source integrity only; native source, release hardware, compiler complexity and audit remain open")

if __name__=="__main__": main()

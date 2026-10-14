#!/usr/bin/env python3
"""Joint finite-interface source identities only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import difflib,gzip,hashlib,json,re,sys
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-joint-matter-link-20261014/ASSUMPTIONS_AND_IMPORTS.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CLAIM_REGISTRY_ADDITIONS.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CLAIM_STATUS_CERTIFICATE.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CONFORMANCE.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/DEPENDENCY_PLAN.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/EVIDENCE_MAP.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/FULL_SOURCE_REVIEW.txt',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/HANDOFF.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_INTERFACE_BRANCH_PLAN.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_INTERFACE_ROOT_ACCEPTANCE.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_SOURCE_ASSEMBLY_ACCEPTANCE.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/MARKDOWN_NOTATION_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/NO_GO_DISCIPLINE_CHECKLIST.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/NO_GO_LEDGER.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/PARENT_BINDINGS.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/PUBLICATION_EDITS.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/REVIEW_HISTORY.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/ROOT_FINAL_REVIEW.txt',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/ROOT_SOURCE_REVIEW.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_ASSEMBLY_SNAPSHOT.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_REVIEW_STATUS.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_WHITESPACE_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/TRACE_GATE.md',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/diffs/complete_publication.diff.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/diffs/wrapper.diff.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/038434530f5e4fab3672125ba65c09f33d39384d106cde367fce6cb31cddd577.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/03a031879d671fb717239f803279d5c08b97ba5f6a26fec8e9044bb01b5229eb.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/042d94837e54a488c960307663a2157e0bb3277e26917b9c6d61942bae94ec15.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/0b397cc7af2b6fe7d4dbdbc320c08f3ec300ea9ff21bef7c439c88a47fd4b49d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/0f8e216e95b99d9fb504d4abb0e9f3dfeea7f1b56c82d173b5ce2b27019ad2d9.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/1436b48b4a724ce8e69093801e21aef54969031243a81a28b52d241d9268c94d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/16bcd68ee4c3498abb22d4740d35e82aaf29cb94d5e87f8ca2e001ae879d85a3.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/16fd40ce1428a2002ba80d991f6befadb1eb10d90de096be224ab25f9b85732a.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/1cda3e6579ec5ae39c96dd254a5f80bf54a5c36f548b4fbcf3c7f95011a09c12.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/20566307fe3f8f0584bbf38038bb88e0d65a1af81191584e0cb5ca5112e2a5c7.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/24f37ae5ea6b126f5ed341494682da1a2a3012bc3ed73730632616ae2dae420d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/255856f0e5851b61236a41f16674f4e67743ea5a3c11cd7a4bbfce8e9ee7f24c.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/27c587b0190a93198bc1a56a6c7b2a69dc48ebe1d489c7eea0cc3f8c1effde3d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/295edee5608d3141fc3e3212bc51753265d953dadd68a8b44a66ed1e0e16e0d2.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/2a8fa44ae417596be95c5b140b431f62aba7429b1485dfd9869c7bfdc2eab9aa.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/2f19f7db1a8a7a609699a724a2a3b2e46d37266936a176b35d33ebcf73cfe0d4.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/301177980761d60533c3f5617c252c543cb81d1eb49ef1558d9a8cb39754e8dc.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/36fe340b319d866be7f60072761142e55131cbca86a9278c88e39f699f198f85.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3a2fb11ba448882ef504eb0d262a2ff490f90352395f0cf3c2944fe398b0aeed.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3b7d2be02a2baf31a74348048ed03bc595958c04c37958ffecd12a86930fd0d6.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3c3f4f99c5079766165657d872c9572b347bdc323bf801bcddb31f879420bbcd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3d87df259fa706405089bc20040bca881d959420dc673910c761e8cad8002505.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3d92b6099121d3166516fad381ffdcb76927be6b399fe5cb6d29e4746a6b4f3b.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4213357bf41060676fe9a2421537cca817569560f6448fe4368b7f3b1127799a.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4577fe7f2d4958b90507b759f9edc31d78e9499943d4d02ff6afd8df72a9e71d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4639fec24e8a414b7c2b2d1a902120a29ade7cde46143d209d54eeed277482af.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/467df84b0c5adc9012283aa88d818f76199e2d6b6080dc6fc26bb92bc2963509.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/47f8afea3865c18a0fd8ce93bad8d88a5ddb6cfbe85cb8d2a5cc6b9ee780ecbd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4e4693ad93a9a5a4382ad8398f90cac407ce068e5d5852d7f053294651596704.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5192486ca3011f2bc7102460e5f9419d04c32ab9d3fbff64c41d26fd6139ca76.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/587d05c84fe86776d7e057924e33f4d889df7ffc3bb06ff3866def555c499b95.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5955b0b88d76a52db083d8d67e0b8811a9de92e3fe5fe6a6cfe69461859c68f2.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5cdbe1c7fe22659b2a86e7814398c4e44a901ddd6a125d2e40671b884c5cb168.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5f422e8e3c6f351dbcd9a20d40c48d747aca5b420f7e7bf90e33840e2d93af6d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/60a218d91c6ec2ee0b84e364bc88dc8d8510d363d1a807366a8fe2aed8fa6344.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/60c3de98a51415dc7f94bec7d904b6f8b661a6398c6be6925c9d734837aae37c.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/65850322f6d46872dbec4c121122c9503f7c2f6c7047bb5d889ed38a3a79f3e0.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6afbec786c903afb93a7571b2dad6a3d24b46cba4fbb757db497bf1d0bf38699.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6d213eee178fef83f978778f7e3107fdae0bd628cf4975fa09277d292682598c.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6ddde3c397339a6c19f0a39a1c925f59693fee0d77bf9735bcccee776c7a0646.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/726870adf16ae14174562549bd2274911276ab42239060ab34728d16f30824f7.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/727401855bb3e6f050e0cd1b6fd633e6c6f6428fe936793e87b3f81148368bfd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/739264693eee5a06d233b1ba2831522f0e52000488d128be99cb3b8cb8ac89dd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/74a7587ca414497f354424b66feef0751fc11e1c8120a00d21cf3de56f16b996.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/79158a9d79c7b1e1df70b46d293a94b6bb10887ee89b2be16346ad7e23572abe.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/81cfcd86447b1f740cfb83579837af9f2729b09910191d3ca322d4d16d74575e.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/85420126d1af0cb2b85ae24906d4fcba4dfaaea2b4665ed52ddb231d828fdfe8.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/8bb80c1adbc231ef0596b6d024ac639cefc6e3a0d566543519da18eb8e211ed1.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/8f26d44f7b28fa25757152fb224570ceb34ce96db7981141025672ddb623ad9a.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/942631b3678d38c4d7ef7673eee0f79e2d7a7bff31fa51d67f3ed3048a6fa1cd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/951297ea13b62fb2211b2a13dea3347078fba7c3740b5a513baad76fadfc7de8.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/a6e35492426ba96338cbdcfb88882c93352872dbde95f71ff9bae131bb115640.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/aa2bbda45f5570093262dee3af96fd4e508e179cafaf8a764d479a462d22bbf1.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b158a453cd16c2209342294e1c69a27701f6fd3c920490b23f5bba655c9b1a5d.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b18a29f577aa04972acf399ca61adf9af01e65ba57b1d45abdccfb5152d4d140.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b3f42bcc86937a28fc7350b2cbe575303dba90de7cefa10eb0f915661818e94e.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b54d5016acf6530072cb732f6ca96e07d0bf2b7339c58d94935e2d809311ffa1.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b7d99f2d269129164435d0a4e9f6790d440a84e4e42db31e9c8af83e33ac9308.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b7fb058ce8590e1a56c31d1975b6a8d0874eb8db7766b2eb4b837338001fe5bd.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b91ee4bddf99c680271b7d33e2be52d01f9e0913474e722875c49cf21f204087.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/bccc2e837cfc925d91e88331581b0057e322cfb44da19271fcfc393b52a90938.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/bf6b01cd01b725f8721ce8d0acd07b2d693c8d96e6ff883cc7430079bb6cd820.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c1c8d311279ebccef1f805efcb98ce8012d08a1331dd41d6486d6dfee6ff8e36.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c4f52c58a044b03de4f92bed5b060d38a7b2028e5d696352fd649679435474d8.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c516257c249304266ee8dba6cbf218f57353fc4d396f2d94c7478e34324a030b.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d250ac7c1ee72a5ae7248a69e4c8258b8341b30237930bfc47e1c551af98fc75.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d253ae38078577f53d0e5cf5e4dbe03cf8a3f78c88d4567b1dbe7432e9ee7afe.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d4d56f9f6a8bd8b4c0ed0ba4b85a8c35f4ff5f387ff38887ced5c8030d869db7.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d6138cbf0988234631d58bbcfe529559231bc33fef64d33c1d4d625b0150bccc.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d6c4aa488e43bccb5f645b3ed9cb529f994cbae2cbf558d090c42b3292e3d69f.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d8b2543eaf232d2eff7212e035b597b113a6f991c130527c540170b4fb4036ce.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d9ee1efb3430cfbaa51c3ff130aac91be00ebfacb7a98805af51c766173a9f88.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d9ff3e2496279a29894ecbb62adc815fb74aa4296ee2a367c2630311007578d9.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/de72cfa077d6ea7fdd3c291382807343889663800880dc1f4a6225ee1068b2a5.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/dea318e93e4b4473d0d889860fcc3ed470d0c28b19afd2ec21384a93c4a1c606.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e092776db0cdb85565ff9092911782c6736867a19287bb0a704d0521f8d6c849.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e11975e59358569a1b44e28a52364dfe5611d40c6fcfc6b5da40ff950ba3b0f9.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e12209f8eaa71f95b1fd9a4e8c74c5fb52c0930c7400a89bd10a6833d7113bc9.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e19e99c8755e1b3bc482bc370031f5b86ae2c489622976040dc2e00cc225712c.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e50cb6c7e4459b01407547bb35c7f16ce9b60b88bd39ccec8490034e86e7337e.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e7dad1b0436540192779f55539f29ae1b535ccd6bafbfa6eb1b1a68dcaca2ad6.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ea0dc80624bf5f35a1c5bc5ae19da5746456ff30c74cabb10d27e29e8169ca51.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ec8d8560bfd53f720eea0df3420f401bb66b56a4d6f29f70a8e8d37716cc33b7.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ed69137fe35b57cc26808676dbef47dd93d5aa6b6666f1e4dbe5489b7c212c6c.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/f0321b9738a3ce1b5fb2f1542c1d2021a45cdd07ffaad0caf15272ebbcaa1be6.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/f5decd77922d61fc5412472fd2a7e43ccc11a8f368b7de5686706e38d236d62a.gz',
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/fbcf6097a1b2d74981aa0581d86a9a0ceb6976effeb2b8738ee18cfa2b875f23.gz',
 'archive/notes/docs/work_history/repo/review_feedback/EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md',
 'docs/JOINT_EVEN_MATTER_FINITE_LINK_INTERFACE_BOUNDED_THEOREM_NOTE_2026-10-14.md',
 'docs/THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_GAUSS_LAW_AS_A_SUPPORT_CONDITION_AMONG_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
 'docs/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md',
 'scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py']
EXTRA_PINS = {'.claude/science/physics-loops/toe-joint-matter-link-20261014/ASSUMPTIONS_AND_IMPORTS.md': {'bytes': 1383,
                                                                                             'sha256': '8163913179ce8111cf513870206e71d91cd6b2aaf8ea96072ff23d6ccc8d2c91'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CLAIM_REGISTRY_ADDITIONS.json': {'bytes': 1332,
                                                                                                'sha256': 'ae7e2e0b83026c7c3d5875fbe0dd466e81ea90431dd6f755d43ac65ddc13ea1d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CLAIM_STATUS_CERTIFICATE.md': {'bytes': 764,
                                                                                              'sha256': '04e41f14d9d47703297cf6da9599c53ca2b346cf476bd7274408374dfe4a8342'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/CONFORMANCE.md': {'bytes': 4128,
                                                                                 'sha256': 'a646b9480594f8efaf1f7e59c15584f3837500ab15761942e212fb3fcc315de8'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/DEPENDENCY_PLAN.md': {'bytes': 955,
                                                                                     'sha256': '55ad6846588262c054eace48fff14a9f13e0341dfe0380dfa02cfd5945689b0b'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/EVIDENCE_MAP.json': {'bytes': 115001,
                                                                                    'sha256': '7d974f0c7b1427e719df1b8dd2b968175e0bb4ca897d1a04ab5d77d236cdfe01'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/FULL_SOURCE_REVIEW.txt': {'bytes': 27549,
                                                                                         'sha256': '65850322f6d46872dbec4c121122c9503f7c2f6c7047bb5d889ed38a3a79f3e0'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/HANDOFF.md': {'bytes': 878,
                                                                             'sha256': '7146b5535a3140f1f2ce7cb6bc5ff5816b3def3f2e0cb5e86587ce542ce973bb'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_INTERFACE_BRANCH_PLAN.json': {'bytes': 384,
                                                                                                   'sha256': '0ebb599d9bca15e08a641aba591b13f68a07689a865b8d84484f589bc6386f3d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_INTERFACE_ROOT_ACCEPTANCE.json': {'bytes': 3294,
                                                                                                       'sha256': 'e092776db0cdb85565ff9092911782c6736867a19287bb0a704d0521f8d6c849'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/JOINT_SOURCE_ASSEMBLY_ACCEPTANCE.json': {'bytes': 1742,
                                                                                                        'sha256': '3d92b6099121d3166516fad381ffdcb76927be6b399fe5cb6d29e4746a6b4f3b'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/MARKDOWN_NOTATION_CLASSIFICATION.json': {'bytes': 132,
                                                                                                        'sha256': '3eed51c7510bd6a00ba6703619db2641a2e74f23523a14fb4a89f7b85e03267e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/NO_GO_DISCIPLINE_CHECKLIST.md': {'bytes': 524,
                                                                                                'sha256': 'bd4dc3a13fbbfef765ce52ef605f84ddebd86c304d18f6e179c731c8b935b713'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/NO_GO_LEDGER.md': {'bytes': 444,
                                                                                  'sha256': '190f2a73daab4a2ed697394726bb7ed281c765d8897320aaa8c78febbcf4d964'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/PARENT_BINDINGS.json': {'bytes': 16083,
                                                                                       'sha256': '5a677ad3e9ad9f9a68c96ceb38a254b893d3a47a1c44e3ab4c27fa0438edadc2'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/PUBLICATION_EDITS.json': {'bytes': 11793,
                                                                                         'sha256': '44ac8b659f87b7e5386419257e82ea5be1ae6b43eba489b334730e365c494351'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/REVIEW_HISTORY.md': {'bytes': 1107,
                                                                                    'sha256': '015bff33d526e7e6959c3acf8cb42588da3df1d78183f57028ef35313b899d74'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/ROOT_FINAL_REVIEW.txt': {'bytes': 7238,
                                                                                        'sha256': '2f19f7db1a8a7a609699a724a2a3b2e46d37266936a176b35d33ebcf73cfe0d4'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/ROOT_SOURCE_REVIEW.md': {'bytes': 4944,
                                                                                        'sha256': '3a2fb11ba448882ef504eb0d262a2ff490f90352395f0cf3c2944fe398b0aeed'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_ASSEMBLY_SNAPSHOT.json': {'bytes': 561,
                                                                                                'sha256': 'beea16d22c0f3fe14e4e18e318ea7186ab99c80691eb9f8f2b983204d06ff00b'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_REVIEW_STATUS.json': {'bytes': 2727,
                                                                                            'sha256': '09f9093077efd4d2ee46fd88f6b5e8efe2e5a30c1d76c86b58305deeecf99487'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/SOURCE_WHITESPACE_CLASSIFICATION.json': {'bytes': 131,
                                                                                                        'sha256': '0618357748e01ab644a231dabed211c13838f41ef1e7c358ab691bf6a915b4d5'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/TRACE_GATE.md': {'bytes': 530,
                                                                                'sha256': '9ff2e4d459762465c40b9486687bd75b014c124f73d83765be146c445cedb4de'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/diffs/complete_publication.diff.gz': {'bytes': 3903,
                                                                                                     'sha256': 'bc52fbdaf11bc6b3e3b1ef3f42ddad5b5d59624177644f77bd75e50b6b28cdb3'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/diffs/wrapper.diff.gz': {'bytes': 3907,
                                                                                        'sha256': '4c2e8a2565ee2cb3b69dab9674ed9e9d0066163a24c45af544582936eafaebba'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/038434530f5e4fab3672125ba65c09f33d39384d106cde367fce6cb31cddd577.gz': {'bytes': 352,
                                                                                                                                              'sha256': '8be5872e3fa0af18e386f3ebd66669eca5d264f0d0d98cba2a1cd7346dbe0e23'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/03a031879d671fb717239f803279d5c08b97ba5f6a26fec8e9044bb01b5229eb.gz': {'bytes': 658,
                                                                                                                                              'sha256': '24c075f240524b534c5cd8da6ffc6436a05e6e677197fdec1a3a5649656f919e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/042d94837e54a488c960307663a2157e0bb3277e26917b9c6d61942bae94ec15.gz': {'bytes': 309,
                                                                                                                                              'sha256': '98ed25ee9923a5e033968bae7c450fc432a64927bd3eba34b79b42ea6096af7a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/0b397cc7af2b6fe7d4dbdbc320c08f3ec300ea9ff21bef7c439c88a47fd4b49d.gz': {'bytes': 2086,
                                                                                                                                              'sha256': '6294e9b1fde6603ef1499aba67a405a0120d81ac77808f7280b290e9e928256e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/0f8e216e95b99d9fb504d4abb0e9f3dfeea7f1b56c82d173b5ce2b27019ad2d9.gz': {'bytes': 8989,
                                                                                                                                              'sha256': 'e3f8643de7e369e94c6c3ad1c230e5918374416b23e3749e730cc628f412a82c'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/1436b48b4a724ce8e69093801e21aef54969031243a81a28b52d241d9268c94d.gz': {'bytes': 567,
                                                                                                                                              'sha256': 'e82f6b3ffc8591e04a436fe9746efd051eddcb981510fb7ceb207e069991bf9d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/16bcd68ee4c3498abb22d4740d35e82aaf29cb94d5e87f8ca2e001ae879d85a3.gz': {'bytes': 2425,
                                                                                                                                              'sha256': '5f69297aaea44541f49c1da193ec022d695b0c5c783f12ad0f8117ff146f8baa'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/16fd40ce1428a2002ba80d991f6befadb1eb10d90de096be224ab25f9b85732a.gz': {'bytes': 2903,
                                                                                                                                              'sha256': 'ce576bec8ff3d164576dcb153abf7fdcd8879dcffbb43fd9691555c3cf98a128'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/1cda3e6579ec5ae39c96dd254a5f80bf54a5c36f548b4fbcf3c7f95011a09c12.gz': {'bytes': 4724,
                                                                                                                                              'sha256': 'a06f45d906bb1bfb8c3e8a821900032736210e480e5a473df9dcf45f7b569bd0'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/20566307fe3f8f0584bbf38038bb88e0d65a1af81191584e0cb5ca5112e2a5c7.gz': {'bytes': 1330,
                                                                                                                                              'sha256': '10d4dd01d0212fe6aeb2664aebb6ce4e116cc3069a54efca60d57bca84c5f84d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/24f37ae5ea6b126f5ed341494682da1a2a3012bc3ed73730632616ae2dae420d.gz': {'bytes': 1468,
                                                                                                                                              'sha256': '6ae55299d1c0b63194b910ea16e902771baee9e8c95bea5779f364a883aab8b6'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/255856f0e5851b61236a41f16674f4e67743ea5a3c11cd7a4bbfce8e9ee7f24c.gz': {'bytes': 303,
                                                                                                                                              'sha256': '7c1a473283331caea4bece3534ca32f964bca32e53e1d550103b57a0c68aab2e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/27c587b0190a93198bc1a56a6c7b2a69dc48ebe1d489c7eea0cc3f8c1effde3d.gz': {'bytes': 2922,
                                                                                                                                              'sha256': '445998fc8657eb3d655b9eec1df096762d9a9cfbf0bb1367c5f80e9a8354a97d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/295edee5608d3141fc3e3212bc51753265d953dadd68a8b44a66ed1e0e16e0d2.gz': {'bytes': 8683,
                                                                                                                                              'sha256': '64a44e8804ac09086c90cedec70ac01e70e63f7bd4d67023a8f88daa4ae6f914'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/2a8fa44ae417596be95c5b140b431f62aba7429b1485dfd9869c7bfdc2eab9aa.gz': {'bytes': 235,
                                                                                                                                              'sha256': 'abb3c65eafc796ab93d3e383b459beb3ff345f3336cd3b9c0e925607abac772e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/2f19f7db1a8a7a609699a724a2a3b2e46d37266936a176b35d33ebcf73cfe0d4.gz': {'bytes': 3501,
                                                                                                                                              'sha256': '6828019e5f8928a87f11d7f0e78bc37fc7bed812b1669f54f85b689abb9dc220'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/301177980761d60533c3f5617c252c543cb81d1eb49ef1558d9a8cb39754e8dc.gz': {'bytes': 2819,
                                                                                                                                              'sha256': '575f47216ae7c85326e14bb47177dadd9a33db01cc681fac746a9e244e5978cc'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca.gz': {'bytes': 16373,
                                                                                                                                              'sha256': 'a2e61c9b3a7c030a84d5a514d32f1c4fe33ece8a4fbcfb670a624d8295e2fa99'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/36fe340b319d866be7f60072761142e55131cbca86a9278c88e39f699f198f85.gz': {'bytes': 2136,
                                                                                                                                              'sha256': '80434894fd6585f8bd5b3486403040ee568f001a9601e57388719bd99fd2ba7d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3a2fb11ba448882ef504eb0d262a2ff490f90352395f0cf3c2944fe398b0aeed.gz': {'bytes': 2515,
                                                                                                                                              'sha256': '872bbc48b43a97a8cecb49c1165b9c4460f9f66c0a39f4fa54063458fc57a397'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3b7d2be02a2baf31a74348048ed03bc595958c04c37958ffecd12a86930fd0d6.gz': {'bytes': 3130,
                                                                                                                                              'sha256': '8ff71e104435e4e7c2c535e5df75e4c8e2b9833e33781e08f40bcc82595288d1'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3c3f4f99c5079766165657d872c9572b347bdc323bf801bcddb31f879420bbcd.gz': {'bytes': 12540,
                                                                                                                                              'sha256': '6033299b3aca3e5c5b3653ae95476e2b6e6925d48b296c075137dec9c08ae15a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3d87df259fa706405089bc20040bca881d959420dc673910c761e8cad8002505.gz': {'bytes': 4080,
                                                                                                                                              'sha256': 'a87ba10a0352af2c844db18075b3a8a4da5ee7234a0409e37e31d1e786408951'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/3d92b6099121d3166516fad381ffdcb76927be6b399fe5cb6d29e4746a6b4f3b.gz': {'bytes': 735,
                                                                                                                                              'sha256': '46abf20411a94f2a182c923d036bdc62b28a165d64a6b549ef41f07a7c0deb06'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4213357bf41060676fe9a2421537cca817569560f6448fe4368b7f3b1127799a.gz': {'bytes': 3982,
                                                                                                                                              'sha256': '5fa812fc5164da8fbb9cf2998b7c1706ea6e711fbc56d20bbe3cdae7abac5dc6'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4577fe7f2d4958b90507b759f9edc31d78e9499943d4d02ff6afd8df72a9e71d.gz': {'bytes': 283,
                                                                                                                                              'sha256': 'cb5f3c14f99b2fa2cefcabe9bab7f4ab2c5ff30eb0ba27bbd078a7bd9cb035ae'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4639fec24e8a414b7c2b2d1a902120a29ade7cde46143d209d54eeed277482af.gz': {'bytes': 1663,
                                                                                                                                              'sha256': '53410338a726442d32718b602df1fa6ec144078c551c1d885bffaff7ee0a0dc8'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/467df84b0c5adc9012283aa88d818f76199e2d6b6080dc6fc26bb92bc2963509.gz': {'bytes': 9728,
                                                                                                                                              'sha256': '3e4d604b925bef6b09cd2e24b42e65b386ff7378bcce76d73062a1011ed63625'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/47f8afea3865c18a0fd8ce93bad8d88a5ddb6cfbe85cb8d2a5cc6b9ee780ecbd.gz': {'bytes': 302,
                                                                                                                                              'sha256': '5d07dfe40c4d162e7aa3d6d52e21d4806d3dbb7d1a3aef861158b4ed7ff2bf76'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/4e4693ad93a9a5a4382ad8398f90cac407ce068e5d5852d7f053294651596704.gz': {'bytes': 138,
                                                                                                                                              'sha256': 'afaa173361cfb8ec7e27b0fc65fc32c68be3afab354f8233b4da147ddf5e916f'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5192486ca3011f2bc7102460e5f9419d04c32ab9d3fbff64c41d26fd6139ca76.gz': {'bytes': 2274,
                                                                                                                                              'sha256': '00d545a4c3d96c65e572f3b2febef5cbdf9dcd103dbc766018d1c63a898e1221'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/587d05c84fe86776d7e057924e33f4d889df7ffc3bb06ff3866def555c499b95.gz': {'bytes': 1851,
                                                                                                                                              'sha256': '66ad29f280fd5b8cd47d3a80589d27d3f9471abf842f73796d98c2af9fee6f26'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5955b0b88d76a52db083d8d67e0b8811a9de92e3fe5fe6a6cfe69461859c68f2.gz': {'bytes': 4177,
                                                                                                                                              'sha256': '6ccb8d926bcd0e7fb01b843439913defd6c40efb83689228f42e045fad22d42a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5cdbe1c7fe22659b2a86e7814398c4e44a901ddd6a125d2e40671b884c5cb168.gz': {'bytes': 2268,
                                                                                                                                              'sha256': 'ed9ef7506f4a6cd5926216ac8ba20f60e4445a11014339884a5923a8ecca4b67'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/5f422e8e3c6f351dbcd9a20d40c48d747aca5b420f7e7bf90e33840e2d93af6d.gz': {'bytes': 1292,
                                                                                                                                              'sha256': '2c5d520d02dfebdb7a8a452f5269a5062689983260f5321c41330996259d6092'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/60a218d91c6ec2ee0b84e364bc88dc8d8510d363d1a807366a8fe2aed8fa6344.gz': {'bytes': 585,
                                                                                                                                              'sha256': '0185796858f0a511cf5ef6bd5f519770d315d87632d19b6a53c02aeca042cdd7'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/60c3de98a51415dc7f94bec7d904b6f8b661a6398c6be6925c9d734837aae37c.gz': {'bytes': 2365,
                                                                                                                                              'sha256': '8ddc9e5af41a75c0bcff8046303e71765ba8dfe829aa98d26d856fc2ff6a8a06'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/65850322f6d46872dbec4c121122c9503f7c2f6c7047bb5d889ed38a3a79f3e0.gz': {'bytes': 11969,
                                                                                                                                              'sha256': '1dc66fef47267e756d0253896be49a7f6be9d1ed0675c2f29bf4a294a8ed81b8'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6afbec786c903afb93a7571b2dad6a3d24b46cba4fbb757db497bf1d0bf38699.gz': {'bytes': 298,
                                                                                                                                              'sha256': '7b868053cb1fbf96ecb41d79e639c8ec276d20bcce35e69891da71b46f02ed0a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6d213eee178fef83f978778f7e3107fdae0bd628cf4975fa09277d292682598c.gz': {'bytes': 2247,
                                                                                                                                              'sha256': '1aeefb22a7247aa97de8aa99bd3cab1a7ba61303cfb3bdaa13dbf6951189a9c1'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/6ddde3c397339a6c19f0a39a1c925f59693fee0d77bf9735bcccee776c7a0646.gz': {'bytes': 19310,
                                                                                                                                              'sha256': '2cee035d93bce29952d2c0632ca2397454bcef57d1a640bf25ac52c1fd58a6bd'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/726870adf16ae14174562549bd2274911276ab42239060ab34728d16f30824f7.gz': {'bytes': 1550,
                                                                                                                                              'sha256': 'f3fa34acbd3e43dd84387a4e4361ae498619bd829246591cdcbc1297e6156984'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/727401855bb3e6f050e0cd1b6fd633e6c6f6428fe936793e87b3f81148368bfd.gz': {'bytes': 3375,
                                                                                                                                              'sha256': 'e59513455b66ef995d29f5f4339392bab77b4fc096ab0f4a59f8b6b796c5d047'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/739264693eee5a06d233b1ba2831522f0e52000488d128be99cb3b8cb8ac89dd.gz': {'bytes': 982,
                                                                                                                                              'sha256': 'ee723a0380647abe56609141b097a28c08338f8882761826397024a906a295a0'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/74a7587ca414497f354424b66feef0751fc11e1c8120a00d21cf3de56f16b996.gz': {'bytes': 4761,
                                                                                                                                              'sha256': '7714a5c1797be4699c89160a618cf7cd299dd71cfa5d0b77422434a16c08624f'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/79158a9d79c7b1e1df70b46d293a94b6bb10887ee89b2be16346ad7e23572abe.gz': {'bytes': 2808,
                                                                                                                                              'sha256': 'cc025183da0bd666cb77489530035dc268aaed062e52c67e47c150fa1c50d82c'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/81cfcd86447b1f740cfb83579837af9f2729b09910191d3ca322d4d16d74575e.gz': {'bytes': 3072,
                                                                                                                                              'sha256': '612eac7c256235a912f4d89a46b61a1f45be2e842808c671ffd9443c0d82a0d2'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/85420126d1af0cb2b85ae24906d4fcba4dfaaea2b4665ed52ddb231d828fdfe8.gz': {'bytes': 706,
                                                                                                                                              'sha256': '865d0de55168ca9077062e297d5e4fb6911cc78b6485c9bbea1362f860dc8035'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/8bb80c1adbc231ef0596b6d024ac639cefc6e3a0d566543519da18eb8e211ed1.gz': {'bytes': 6154,
                                                                                                                                              'sha256': 'a659f359d659faf0af1b27ec92c0b14d4ab41d01003d7c7b8d0cb5590e2a7fb9'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/8f26d44f7b28fa25757152fb224570ceb34ce96db7981141025672ddb623ad9a.gz': {'bytes': 3360,
                                                                                                                                              'sha256': '78b335d88a94991e821237908ff4585d08cf515b122dd0acfb237fee94796c58'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753.gz': {'bytes': 4357,
                                                                                                                                              'sha256': '70b06ee88301b6b13ed28ba82d06b0ac071d9286ab55475e57434c84e507e631'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/942631b3678d38c4d7ef7673eee0f79e2d7a7bff31fa51d67f3ed3048a6fa1cd.gz': {'bytes': 6633,
                                                                                                                                              'sha256': '9253bc11f7afeb1d56067e25ba0e3f711ebb63ca9d241d626f671b22ba2ad3d2'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/951297ea13b62fb2211b2a13dea3347078fba7c3740b5a513baad76fadfc7de8.gz': {'bytes': 818,
                                                                                                                                              'sha256': '12406e6f030855bb3771e47361fe3c614067ed041a1f4cfe8583a4e6779c6d47'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/a6e35492426ba96338cbdcfb88882c93352872dbde95f71ff9bae131bb115640.gz': {'bytes': 6553,
                                                                                                                                              'sha256': 'e97018eb70c32417696598cb35da94b8124ce6df1827b5dfd81c3e2c9ea19eef'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/aa2bbda45f5570093262dee3af96fd4e508e179cafaf8a764d479a462d22bbf1.gz': {'bytes': 2609,
                                                                                                                                              'sha256': '69ca0f15647bbfa70c2bf6e1aa2a8b07ea9d2359aa93933ae292370e4a805185'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b158a453cd16c2209342294e1c69a27701f6fd3c920490b23f5bba655c9b1a5d.gz': {'bytes': 676,
                                                                                                                                              'sha256': 'd967209805b60705f61634c40a55abfa6987e467597a1d4e2ea9872017d5aac7'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b18a29f577aa04972acf399ca61adf9af01e65ba57b1d45abdccfb5152d4d140.gz': {'bytes': 565,
                                                                                                                                              'sha256': '32f78c861ca0889f5fb4ea7cb3c919298faeb6e662cf2efb7172ed64b7c37d34'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b3f42bcc86937a28fc7350b2cbe575303dba90de7cefa10eb0f915661818e94e.gz': {'bytes': 931,
                                                                                                                                              'sha256': '14a32073f2d728487f583b11ba8b2f54e9defd1c22052d4afd038d3c1c8e4d62'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b54d5016acf6530072cb732f6ca96e07d0bf2b7339c58d94935e2d809311ffa1.gz': {'bytes': 1743,
                                                                                                                                              'sha256': 'b90c9b424fcdeea68ba849b9a8ad3909fac968a6aa2070fc9c314b8838e61725'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b7d99f2d269129164435d0a4e9f6790d440a84e4e42db31e9c8af83e33ac9308.gz': {'bytes': 484,
                                                                                                                                              'sha256': '7e49a36b3a287cac133442edafac4a4440c4c3c04194e397e42b05a97481849d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b7fb058ce8590e1a56c31d1975b6a8d0874eb8db7766b2eb4b837338001fe5bd.gz': {'bytes': 542,
                                                                                                                                              'sha256': 'bac8810b2c1910743f12a7fbde23c313213115f5cd7bae2c87cc216cc0f32ceb'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/b91ee4bddf99c680271b7d33e2be52d01f9e0913474e722875c49cf21f204087.gz': {'bytes': 725,
                                                                                                                                              'sha256': '4dceae74f8d5cdfd60e5e54a4c738f3cc4f19f7986315f5fe7372fac134a0dc8'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/bccc2e837cfc925d91e88331581b0057e322cfb44da19271fcfc393b52a90938.gz': {'bytes': 10510,
                                                                                                                                              'sha256': '1c973cc221450cdeed674413f299e69d31cd176f05b0cf980e0b7daeb2d64b31'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/bf6b01cd01b725f8721ce8d0acd07b2d693c8d96e6ff883cc7430079bb6cd820.gz': {'bytes': 569,
                                                                                                                                              'sha256': 'e6f0acc8b5f4a69c614c76df9b345e4b7119ab642e046b56dacbdc705a104fba'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c1c8d311279ebccef1f805efcb98ce8012d08a1331dd41d6486d6dfee6ff8e36.gz': {'bytes': 2336,
                                                                                                                                              'sha256': '358ebbd2ed9ac7a0bd4fb55ea111a62c8b41a6c3860277a4fe80c6e86240ba3e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b.gz': {'bytes': 7317,
                                                                                                                                              'sha256': '50ba613547a49b515ea999d5bce6d61721da6498d6643ce3347f560aeb7af3f8'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c4f52c58a044b03de4f92bed5b060d38a7b2028e5d696352fd649679435474d8.gz': {'bytes': 4327,
                                                                                                                                              'sha256': '03707379ccd96a6c3e57afb1bc5d472edd5cf423b4a84ceb7940b00ac7a8dee1'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/c516257c249304266ee8dba6cbf218f57353fc4d396f2d94c7478e34324a030b.gz': {'bytes': 3759,
                                                                                                                                              'sha256': 'f926c8769b4e2a13145c6edbe9d83434df7bbdae29348d0984925a44cd180ead'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d250ac7c1ee72a5ae7248a69e4c8258b8341b30237930bfc47e1c551af98fc75.gz': {'bytes': 985,
                                                                                                                                              'sha256': '0cbddecc46e988f4f582a903a154c90d01b85bab8fe100f1590a7ccdfd1e945e'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d253ae38078577f53d0e5cf5e4dbe03cf8a3f78c88d4567b1dbe7432e9ee7afe.gz': {'bytes': 8344,
                                                                                                                                              'sha256': '0fc28619f4c7a2ea937ca1abc7fc611009ec2b853991c8fee59fd7046edb7ed5'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d4d56f9f6a8bd8b4c0ed0ba4b85a8c35f4ff5f387ff38887ced5c8030d869db7.gz': {'bytes': 1498,
                                                                                                                                              'sha256': 'd11c3d49f999e6c2ad706bdb98c466d244409bbc67db111381ca8f0ae05c2e2a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d6138cbf0988234631d58bbcfe529559231bc33fef64d33c1d4d625b0150bccc.gz': {'bytes': 460,
                                                                                                                                              'sha256': '5642dcedbce37bc86a898d07cd2a95bdd57ca37402dc2ccc7406740554dae02a'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d6c4aa488e43bccb5f645b3ed9cb529f994cbae2cbf558d090c42b3292e3d69f.gz': {'bytes': 5823,
                                                                                                                                              'sha256': '8f5a72bce7eb3b284102cd1b85771fcd4897f03990c894cf2a6072f064a45a3b'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d8b2543eaf232d2eff7212e035b597b113a6f991c130527c540170b4fb4036ce.gz': {'bytes': 9737,
                                                                                                                                              'sha256': '2354414b3e04a74f969a1318cbad1d8ceb15f6b93fa3b2199d7601aa5eac7ded'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d9ee1efb3430cfbaa51c3ff130aac91be00ebfacb7a98805af51c766173a9f88.gz': {'bytes': 2078,
                                                                                                                                              'sha256': 'fd2b9e56455040e22ecf483bf6e2db504322b3b34d53391bc288140b7de2e95b'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/d9ff3e2496279a29894ecbb62adc815fb74aa4296ee2a367c2630311007578d9.gz': {'bytes': 686,
                                                                                                                                              'sha256': '848dffee210ef96c28f7ef71ecf32b5beacf01e015de98f3d52f4a09e79d1979'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34.gz': {'bytes': 8820,
                                                                                                                                              'sha256': 'f56a522c3e671d609374de93e7d0e341c6ec109a5811ec73a5fb12430f9e6475'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/de72cfa077d6ea7fdd3c291382807343889663800880dc1f4a6225ee1068b2a5.gz': {'bytes': 1380,
                                                                                                                                              'sha256': 'd6524191f134dfb6be7ab36dbcbce4f39e14c908fbe9b022e04c537261501038'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/dea318e93e4b4473d0d889860fcc3ed470d0c28b19afd2ec21384a93c4a1c606.gz': {'bytes': 3636,
                                                                                                                                              'sha256': 'b73c14a0b22f6bc36156cf93f22ec7d0d9da0bb0047d638c062f3eade421877f'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e092776db0cdb85565ff9092911782c6736867a19287bb0a704d0521f8d6c849.gz': {'bytes': 1234,
                                                                                                                                              'sha256': 'f524c95d1cc4f700e4739812535931664dd75a2ba95a71b54d4d76c13d763593'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e11975e59358569a1b44e28a52364dfe5611d40c6fcfc6b5da40ff950ba3b0f9.gz': {'bytes': 442,
                                                                                                                                              'sha256': 'a98ad233bd342978fb7ff88bc3ac9bcf633cf967aa6ab2b4ea54388e564d4312'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e12209f8eaa71f95b1fd9a4e8c74c5fb52c0930c7400a89bd10a6833d7113bc9.gz': {'bytes': 365,
                                                                                                                                              'sha256': '1429412e527cbe1c1acc119c7f820dd625806f1fdcb4593c6248ad57797b04ab'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e19e99c8755e1b3bc482bc370031f5b86ae2c489622976040dc2e00cc225712c.gz': {'bytes': 2422,
                                                                                                                                              'sha256': 'eae6e0bb31f9e11a32ef8b65619c34b1299dd5f8f01786965106507129a5524d'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz': {'bytes': 20,
                                                                                                                                              'sha256': '9ceffb7310338057cfe71a4ae1e2c98d2c485d81cdef906532a801f457a38d64'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e50cb6c7e4459b01407547bb35c7f16ce9b60b88bd39ccec8490034e86e7337e.gz': {'bytes': 3927,
                                                                                                                                              'sha256': 'ae9106bf7d80c04d9cd133945fa1d93117f294cc0c44290abe41d8f30a642f27'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/e7dad1b0436540192779f55539f29ae1b535ccd6bafbfa6eb1b1a68dcaca2ad6.gz': {'bytes': 964,
                                                                                                                                              'sha256': 'e37547f7550ef3037035ecc66bc7f242b770c853be95952c3e4986efdcf4d304'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ea0dc80624bf5f35a1c5bc5ae19da5746456ff30c74cabb10d27e29e8169ca51.gz': {'bytes': 3855,
                                                                                                                                              'sha256': '32d88589902ea6f6e4f6002bbbae4aac497406608d3585fff22393e6cc0d6090'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ec8d8560bfd53f720eea0df3420f401bb66b56a4d6f29f70a8e8d37716cc33b7.gz': {'bytes': 893,
                                                                                                                                              'sha256': '964f6e736d81b16941237fc0819a93f815d11faef1c0cd249328abe366f70aa2'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/ed69137fe35b57cc26808676dbef47dd93d5aa6b6666f1e4dbe5489b7c212c6c.gz': {'bytes': 679,
                                                                                                                                              'sha256': '3085d7bcc988355dc5f0dabab0f0c09206b108ed82cf5b798fbcc72fd9c81fa2'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/f0321b9738a3ce1b5fb2f1542c1d2021a45cdd07ffaad0caf15272ebbcaa1be6.gz': {'bytes': 1713,
                                                                                                                                              'sha256': 'bd4e491680b5341bac5725f5118fc01168099eebab195ca9506bdc5ba89684c9'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/f5decd77922d61fc5412472fd2a7e43ccc11a8f368b7de5686706e38d236d62a.gz': {'bytes': 2068,
                                                                                                                                              'sha256': 'a0164fa5802b8cac41c7c08b97764d975b25b23aebeca45a6510c1a4a8beb2ff'},
 '.claude/science/physics-loops/toe-joint-matter-link-20261014/objects/fbcf6097a1b2d74981aa0581d86a9a0ceb6976effeb2b8738ee18cfa2b875f23.gz': {'bytes': 90,
                                                                                                                                              'sha256': 'bedb4db0584be25028aebc5f91125656e19ae9106db465261a704cf582b6b7da'}}
CLAIM = 'joint_even_matter_finite_link_interface_bounded_theorem_note_2026-10-14'
PACKET = '.claude/science/physics-loops/toe-joint-matter-link-20261014'
MAP_SHA = '7d974f0c7b1427e719df1b8dd2b968175e0bb4ca897d1a04ab5d77d236cdfe01'
EDITS_SHA = '44ac8b659f87b7e5386419257e82ea5be1ae6b43eba489b334730e365c494351'
PARENTS_SHA = '5a677ad3e9ad9f9a68c96ceb38a254b893d3a47a1c44e3ab4c27fa0438edadc2'
GRAPH_SHA = 'ae7e2e0b83026c7c3d5875fbe0dd466e81ea90431dd6f755d43ac65ddc13ea1d'
STATUS_SHA = '09f9093077efd4d2ee46fd88f6b5e8efe2e5a30c1d76c86b58305deeecf99487'
SOURCE_FREEZE_SHA = '8bb80c1adbc231ef0596b6d024ac639cefc6e3a0d566543519da18eb8e211ed1'
CORE_SHA = '34cbe355c3cd643e3eb3233560fa53259b5803fa1114e4c8eedabbb40475dbca'
EDIT_SCOPE = 'publication metadata, attribution links or current source-status pointers only; full original/current diff'
def need(ok,message):
    if not ok:raise ValueError(message)
def sha(b):return hashlib.sha256(b).hexdigest()
def diff(a,b,old,new):
    return b''.join(difflib.diff_bytes(difflib.unified_diff,a.splitlines(True),b.splitlines(True),fromfile=old.encode(),tofile=new.encode(),n=3))
def verify(root):
    root=root.resolve();reads={}
    def read(name):
        p=PurePosixPath(name);need(not p.is_absolute() and '..' not in p.parts,'Unsafe declared input')
        path=root.joinpath(*p.parts)
        need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),'Declared input missing or outside repository')
        if name not in reads:reads[name]=path.read_bytes()
        return reads[name]
    def pinned(name,digest,message):
        b=read(PACKET+'/'+name);need(sha(b)==digest,message);return json.loads(b)
    evidence=pinned('EVIDENCE_MAP.json',MAP_SHA,'Archive map changed');contents={};origins={}
    for obj in evidence['objects']:
        need(obj['sha256'] not in contents,'Duplicate archive object');z=read(PACKET+'/'+obj['path'])
        need(sha(z)==obj['stored_sha256'] and len(z)==obj['stored_bytes'],'Compressed archive changed')
        b=gzip.decompress(z)
        need(sha(b)==obj['sha256'] and len(b)==obj['bytes'] and len(b.splitlines())==obj['lines'],'Archived source changed')
        contents[obj['sha256']]=b
        for origin in obj['origins']:
            need(origin['path'] not in origins,'Duplicate original alias');origins[origin['path']]=obj['sha256']
    def archived(name):return contents[origins[name]]
    contract=evidence['accepted_source_package'];prefix=contract['path']+'/'
    def source(name):return archived(prefix+name)
    need(contract['freeze_sha256']==SOURCE_FREEZE_SHA and sha(source('FINAL_FREEZE.json'))==SOURCE_FREEZE_SHA,'Accepted source freeze differs')
    seal=json.loads(source('FINAL_FREEZE.json'));members=contract['members'];extras=contract['additional_files']
    need(seal['files']==members and len(members)==contract['member_count']==99,'Assembly membership differs')
    need(len(extras)==1 and extras[0]['path']=='FINAL_FREEZE.json' and contract['complete_file_count']==100,'Assembly additional membership differs')
    need({p for p in origins if p.startswith(prefix)}=={prefix+r['path'] for r in members+extras},'Complete assembly aliases differ')
    for r in members+extras:
        b=source(r['path']);need(sha(b)==r['sha256'] and len(b)==r['bytes'],'Assembly member identity differs')
    selection=json.loads(source('EVIDENCE_MANIFEST.json'))['files']
    need(len(selection)==evidence['original_source_selection_count']==84 and evidence['original_control_record_count']==9,'Original evidence selection differs')
    for r in selection:
        b=source(r['archive_path']);need(b==archived(r['original_path']) and sha(b)==r['sha256'] and len(b)==r['bytes'],'Original source alias differs')
    mapping=json.loads(source('SOURCE_MAP.json'));accepted=source(mapping['candidate']);wrapper=source(mapping['wrapper'])
    need(len(mapping['complete_extractions'])==1,'Accepted extraction count differs');x=mapping['complete_extractions'][0];core=source(x['source_archive'])
    start,end=x['candidate_byte_start_inclusive'],x['candidate_byte_end_exclusive']
    need(sha(core)==x['source_sha256']==CORE_SHA and len(core)==x['source_bytes']==39236 and len(core.splitlines())==310
         and accepted.count(core)==x['occurrences']==1 and accepted[start:end]==core,'Complete original proof differs')
    need(sha(accepted)==mapping['candidate_sha256'] and sha(wrapper)==mapping['wrapper_sha256']
         and accepted==wrapper+b'\n'+core+mapping['footer_utf8'].encode(),'Accepted candidate reconstruction differs')
    need(accepted[:start].count(b'\n')+1==x['candidate_line_start'] and accepted[:end].count(b'\n')==x['candidate_line_end'],'Accepted extraction lines differ')
    edits=pinned('PUBLICATION_EDITS.json',EDITS_SHA,'Publication transformation changed')
    need(edits['source_freeze_sha256']==SOURCE_FREEZE_SHA and edits['additional_mathematical_body_edits']==[] and len(edits['notes'])==1
         and edits['accepted_wrapper_edit_scope']==EDIT_SCOPE,'Publication scope differs')
    note=edits['notes'][0];assembled=b'';published_cores=[];rendered_wrapper=None;framing=[]
    need(archived(note['accepted_candidate_path'])==accepted and sha(accepted)==note['accepted_candidate_sha256'],'Accepted publication candidate differs')
    need([r['kind'] for r in note['pieces']]==['rendered_wrapper','literal_framing','accepted_core_slice','literal_framing'],'Publication piece order differs')
    for r in note['pieces']:
        if r['kind']=='rendered_wrapper':
            b=archived(r['source_path']);need(b==wrapper and sha(b)==r['source_sha256'],'Accepted wrapper differs')
            for t in r['replacements']:
                old,new=t['original'].encode(),t['rendered'].encode()
                need(t['scope']=='publication metadata, attribution links or current source-status pointers only' and b.count(old)==1,'Wrapper replacement differs');b=b.replace(old,new,1)
            rendered_wrapper=b
        elif r['kind']=='accepted_core_slice':
            b=archived(r['source_path'])
            need(b==core and sha(b)==r['source_sha256']==r['expected_slice_sha256'] and r['source_line_start']==1
                 and r['source_line_end']==310 and r['additional_mathematical_body_edits']==[],'Complete published proof differs');published_cores.append(b)
        else:b=r['text'].encode();framing.append(b)
        need(sha(b)==r['sha256'] and len(b)==r['bytes'] and r['byte_offset']==len(assembled)
             and r['byte_end_exclusive']==len(assembled)+len(b),'Publication piece bytes differ')
        need(r['first_line']==assembled.count(b'\n')+1 and r['last_line']==(assembled+b).count(b'\n'),'Publication piece lines differ');assembled+=b
    need(published_cores==[core] and framing==[b'\n',mapping['footer_utf8'].encode()],'Complete body or framing changed')
    actual=read(note['note'])
    need(actual==assembled and sha(actual)==note['published_sha256'] and len(actual)==note['published_bytes']
         and len(actual.splitlines())==note['published_lines'] and actual.count(core)==1,'Published source does not reconstruct')
    def diff_bytes(r):
        z=read(PACKET+'/'+r['diff']);d=gzip.decompress(z)
        need(sha(z)==r['diff_stored_sha256'] and sha(d)==r['diff_sha256'] and len(d)==r['diff_bytes']
             and len(z)==r['stored_bytes'] and r['context_lines']==3,'Raw diff archive changed');return d
    need(diff_bytes(note)==diff(accepted,actual,note['fromfile'],note['tofile']),'Full publication diff differs')
    wd=edits['wrapper_diff'];need(diff_bytes(wd)==diff(wrapper,rendered_wrapper,wd['fromfile'],wd['tofile']),'Complete wrapper diff differs')
    bindings=pinned('PARENT_BINDINGS.json',PARENTS_SHA,'Parent bindings changed')
    need(bindings['binding_complete'] is True and bindings['publication_ancestry_is_not_mathematical_dependency'] is True
         and bindings['history_theorem_imported'] is False,'Current source binding remains unresolved')
    definitions=bindings['definitions'];parents=bindings['parents']
    need([r['key'] for r in definitions]==['C235_NOTE','C235_PROGRAM','QL_CUT','QL_ENCODED']
         and parents==[r for r in definitions if r['registered_graph_note']],'Literal definition membership differs')
    need([r['key'] for r in bindings['required_roles']]==[r['key'] for r in definitions] and all(r['imported_theorem_result'] is False for r in bindings['required_roles']),'Required definition roles differ')
    for r in definitions:
        b=read(r['path']);need(sha(b)==r['published_sha256'] and len(b)==r['bytes'] and b==archived(r['archive_alias']),'Current definition source changed')
        need(r['role_class']=='literal_historical_definition_and_provenance' and r['imported_theorem_result'] is False
             and r['complete_body_identity_verified'] is True and r['relied_role_checked'] is True,'Definition role changed')
        need(r['markdown']=='['+r['label']+']('+r['target']+')' and actual.decode().count(r['markdown'])==1,'Definition attribution citation differs')
    need(re.findall(r'\[[^\]]*\]\(([^)\s#]+\.md)(?:#[^)]*)?\)',actual.decode())==bindings['all_markdown_note_targets'],'Recognized Markdown targets differ')
    for r,x in zip(parents,bindings['canonical_core_maps']):
        b=read(r['path']);s=archived(x['source_path'])
        need(x['key']==r['key'] and sha(b)==x['canonical_sha256']==x['source_sha256'] and b==s
             and x['byte_start_inclusive']==0 and x['byte_end_exclusive']==len(b) and x['first_line']==1
             and x['last_line']==len(b.splitlines()) and x['body_edits']==[],'Complete canonical definition identity differs')
    need(len(parents)==len(bindings['canonical_core_maps'])==2,'Canonical definition count differs')
    graph=pinned('CLAIM_REGISTRY_ADDITIONS.json',GRAPH_SHA,'Graph proposal changed');deps=[p['claim_id'] for p in parents]
    need(graph['binding_complete'] is True and len(graph['nodes'])==1 and graph['nodes'][0]['claim_id']==CLAIM
         and graph['nodes'][0]['path']==note['note'] and graph['nodes'][0]['deps']==deps
         and graph['direct_edges']==[{'from':CLAIM,'to':d} for d in deps] and graph['new_roots']==[]
         and graph['expected_delta']=={'nodes':1,'edges':len(deps),'roots':0},'Definition citation graph proposal differs')
    status=pinned('SOURCE_REVIEW_STATUS.json',STATUS_SHA,'Review scope changed')
    acceptance=read(PACKET+'/JOINT_SOURCE_ASSEMBLY_ACCEPTANCE.json');review=read(PACKET+'/ROOT_SOURCE_REVIEW.md');scope=json.loads(acceptance)
    need(sha(acceptance)==status['source_assembly_root_acceptance_sha256'] and sha(review)==status['source_assembly_root_review_sha256'],'Assembly root review changed')
    need(scope==status['source_review_coverage_verbatim'] and scope['accepted_freeze']['sha256']==SOURCE_FREEZE_SHA
         and scope['root_review']['sha256']==sha(review) and scope['canonical_execution_authorized'] is False
         and scope['disposition']=='accepted_source_assembly_for_separately_reviewed_publication_preparation','Assembly acceptance scope differs')
    need(status['no_go_packet_pass'] is False and status['new_independent_mathematical_review'] is False
         and status['mathematical_core_edits']==0 and status['retained_audit_status'] is False,'Review limitation differs')
    for name,p in EXTRA_PINS.items():
        b=read(name);need(sha(b)==p['sha256'] and len(b)==p['bytes'],'Additional publication integrity input changed')
    need(set(reads)==set(AUDIT_INPUT_PATHS) and len(AUDIT_INPUT_PATHS)==len(set(AUDIT_INPUT_PATHS)),'Declared read closure differs')
    return {'result':'source_identities_and_reconstruction_match','claim_id':CLAIM,'meaning':'Byte integrity only; no mathematical calculation, proof or audit executed.',
        'mathematical_operations_executed':False,'mathematical_predicates_executed':0,'scientific_mutations_executed':0,
        'no_go_packet_pass_supplied_by_tool':False,'independent_review_supplied_by_tool':False,
        'external_definition_input_reads':[p['path'] for p in definitions],'package_local_integrity_reads':sorted(set(reads)-{p['path'] for p in definitions})}
def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]),sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no CAR or Gauss identity was evaluated.')
    print('per_site: checked and not executed — source integrity only; no geometry or incidence bound was calculated.')
    print('per_mode: checked and not executed — source integrity only; no sector rank or occupation witness was computed.')
    print('per_block: checked and not executed — source integrity only; no Clifford or Wilson action was evaluated.')
    print('lattice_wide: checked and not executed — source integrity only; no native or photon theorem was verified.')
if __name__=='__main__':
    try:main()
    except Exception as error:
        print(json.dumps({'result':'identity_verification_incomplete','error':str(error),'mathematical_operations_executed':False,
            'mathematical_predicates_executed':0,'scientific_mutations_executed':0}),file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Modulated-kinetic-energy archive/reconstruction identity only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import difflib, gzip, hashlib, json, sys
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/ASSUMPTIONS_AND_IMPORTS.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/CLAIM_REGISTRY_ADDITIONS.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/CLAIM_STATUS_CERTIFICATE.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/COMBINED_VALIDATION_PLAN.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/CONFORMANCE.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/EVIDENCE_MAP.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/HANDOFF.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MARKDOWN_NOTATION_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_ENERGY_BRANCH_START.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_DISPOSITION.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_REVIEW.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_VERIFICATION.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/NO_GO_DISCIPLINE_CHECKLIST.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/PARENT_BINDINGS.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/PUBLICATION_EDITS.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/REVIEW_HISTORY.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_AUTHORITY_BOUNDARY.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_RECOVERY.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_REVIEW_STATUS.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_WHITESPACE_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/TRACE_GATE.md',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/diffs/modulated.publication.diff.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/diffs/modulated.wrapper0.diff.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/diffs/modulated.wrapper2.diff.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/diffs/required_normalization_correction.diff',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0425eec26273c83b10d8a0f5b630d1170b47fec69f60208b1474957186602559.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/04552fe2396b9ff394c131f8198ec3f672ba8c6a90d671d86b8a8796655abf69.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/04bc6d0a558cd3be87e972be92915a6484583f1973e31b850a6386fe57f02e16.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/05aa46d5699f2aa516f83a330019fa71386e5e26c874e50926cc76840e56bab1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/07b3838194ba6b60163923541f05a86afb6f817b6e56f300f1c14a5cfd8a0b1e.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0991b928e681892c5c3d3d514cd781c8fd0bf779f4cca07a2d525dd69bad4498.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0b6c2435be2112a196bcc64f3736ef3356710cfeb7253062445218e539ef4381.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0b975ded39f5bf0439fcc91a9d5f87e25fc9ed70acd101598f0b54474e020f00.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0e38bc3ccd32186e75db5d3f09a30388db9cb46c011f233ae141c1fd204a46ae.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/0ed542a3228607b3762f6f1c5c8295fc958a1ebd6620fffcbb2f23d54d87f08a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/118c6eebc51c26fa9402f8727b73b589d9ed555e75d46cfbd37be7da1c38bb80.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/13cbadb9c44fd1c9370db9b126d32545b9b86aa4b962b8e05f78dba5f9992838.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/143e2b82b667d94b5aae406c4c38ed89e0d6a74a7e25951acf635913ae139fd0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/15ce2bc98363e34bccd3105a5064551924fda8db0160d481b8a19effa3f9ab32.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/18413835314fde6b6238d59a9c8d4601ef3efdc1aadd5204dc1a77bac8370b92.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/1844393296a3b71c7ebdb51a5bb13f3235217b2a0ba6f9ed5aed08bed6d60b87.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/19120bdd1e1bc84735af7f0f858c5ced9268e0831ac4f1de8c9e51367026b512.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/210149d49b55ec31d7659ee2b98f5d3f2b35e99ea8419b0ea2882d6b3cd08f74.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/22641ffdd54b4b4406969c7a26bebfd9b5a29fbf063014c698bc11b30c0d8a16.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/22710f0af4cbfb084da0b15a959f150e750f09f157dd7489014bd805b8eb4fba.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/22b0f4877b2c537192e0e87dde7109fc50f426e61b72898b47869d5d0c84d66b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/26914ec67d3bcc5493656f3b2e7c422077d1bb2846569e01d754d65d17869885.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/2c218e91f763fbf5c9e087b39a9a9a81caba757bf0eff4b4c18cc0ef948cd2d9.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/2fc825965d0303de2b244d3dac2c704d1e2c37be92b9433fc47a7f9d809fd0fe.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/32ef87bbc88eb684e7be08250ca9c0462039688b9a4e13a37fb15f771aa6ec16.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/33718c87bccb71041d1800e5137c2ed0eb6b0b13a7365258a63df15c2e51236b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/3677dbd64dcf286affca5b5cb6b0c26499d2aa127c296834f348d921f145244f.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/390a9efec32c6ca740404cf607bd6c095e2816a66f913c16d97a1d5321bb41f1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/39a689492e3710536a4ad7707887fb81124485ba268666cbedaef0868dff7fd0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/3a084e70500188714bccdb5a7a94542bbebca568e643751fcb93f971e87a118b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/3d409e93abb3b58796a9c10ca6d21ba93b7edc73b8fb24e7364da97c805580a9.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/3d52327be3b4890f6e87573855d23f8e607a354104222c6302f5884acfbdc9d1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/40bebe4fa79afe383d50aae1941598f10007e79594464cfc7969c6cfd658dc19.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/422a92a8a24daa8fa240251ccae041fcca737af0335a486f33f3b20de0fb665a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/43b47e08ec8a9a990f7f2bf6cd5bc1c50dbd5057e72756ff351c830ac84e7ca0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/467fc3fdb898d426608a957e3dbd3b9875e2adbfb13d4480138ad7bd892a2252.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/4ace9d7d0c37d01325bb7326a298113bf4b2bf9897b48705fe537f88bed22472.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/4b97a24d758ba464202d6771024342805e8934ffb36b20e0100830a9d413afd7.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/4c7e3bba0a760bf09c3de680c18d44823af60d3f2b3ee43c5286065dac2b8d1e.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/4cb5929d7dcebe436889d3053692e8f57b0290f55b360e55914c0814795d22d8.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/4dcc2e62bea25faa0ac82d186974b568c2fd81c363cc31f22db07bbb30c0794d.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/510041af578e1cccbf3d2135afc9e2fa88e415a742c6e19e8779eaa0d7b879d1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/51d938226022b0cf102f4888903fd34cb7766a823a605bafbdddc43ce79c47f0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/526f442d6df264c5b02424835735f90513e5227a6cfce90cd9c692c782919fa1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/55ce027955d0e95beb42014bec0169fa2afd97058717917332b20281f7a6debe.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/5a93e8eff77a34fae5dc54debe43c85b923ef25e447c3a486e0f65f4f8c8c8e4.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/5b0699a94d06fdda853e52b39450e65aa497d06e80f210d9061bc3899fe4a473.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/63bbc78529748758531d7b36d8f8ec52ed85fffd226907d894735eeb4991bfd1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/693976789006e300d6159398972dcde8f7e122f009f18e4327a5a4a37e7f1946.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6a771ce17bbc5eb44f59a85c6a8cf6373d79c7c1b1ff7b7d283a531b45cbd918.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6bbadb246c5237c07aa65a5cdb5bd12c18afdb41b25ff71232a6d243bdde7a3c.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6bf8c39eeeab64f4610329b89e5f58e8d29fb8de744e8dccd1a76448f0a4c170.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6bf90945b4cfa48fc656822e208ae4ebe304803d924b0d212671d98b327a75a8.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/6ce2f66b5c660a0137665a3f597507394e70706861f10d006b56d52a4e6cefbd.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/718ad6e1583ba95b35788ad8dd6eb381aa9bbb2bdbe207dd6fdb5a4e64eb7ad3.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/71d0bb07028c8af23143a5973b2ad8f4f39ebe4cc8e6ca9c1dcd6c18d97ae71e.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/7218e6147b02748df11a38d7d87320a4766a83e8d2bf9d8cb068fb3f23804552.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/72b513050902a9631e08640d45c6331a82ffe64b4c175fd09c3c1b00f20a67fa.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/750f15023c5e8b7ae62ca84e0d9a677c70dfb3782befd0042cba8b697e030942.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/754fa7b9913c75b32665db816a3c9b6673172d1b8c2471e16acf19effddc555f.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/79b01d435e960943d2597676e9a1081b836980bc9a866d018d59efa95f0ace75.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/7d077850d6a8d9edbdaf7bcdbad92107f12d7947b27b657f73195696158f2113.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/7db9ad9198310183aa7c4a722c38e9cc165e8f5404bf83a63d5a438cb67fcc64.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/7f2bc9825f1df0f5dcb1dfc3349e703f1274f8206c9f374a4fd4749f7fd86ab4.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/81a009e6454194c9d2c200667c6091b490d55ac825b7bccb09a8ebbef3e76e05.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8421ecd9b51f0149ce19fa999a8039a639b7fbec4d998471b193c2625c488987.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/87aaeb551cba270eef3fc62b9ba28c525ef8597ad037d89b9687233da4712e40.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8b2c6ab73f58ad71413bddd1098387d27c3acba5fb60a1b40b32ee9a7bafee9d.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8b68b83cb4d809b03ab890cd7883b7db9af22ecf3c557b5ef1df8d6683259ef0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8c8cbe20f81349542d196bc523db9fc52f8762e721c95dadf611d11efbc04037.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8cfb329c3aa15a4f7ab0ceed0ad94ed6e4f3ffc6e3f2c166b833f316fcbeaf0a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/8e259f68ddadf738a9ed70c0e45bcb689dc867021f7ad30fee586f7ccc09d392.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/902f21d5e6d800c88f40f5d07c46c6a62c0f988de22c278aa35d1de93696c43f.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9065c89665f2de14f2229c4b3847a534d3ae4bf48c59ba98e0bba92c696452ee.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/919091668aa51244be2dd52e8f3bfd1ed0d25bd61213232f65cd2ad548d1fe66.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/91b52e0736eed466f97ab0103588d6e49719e6f4f6ea46a1cce718ef1bbfe70a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9719cdc68a9f27577484d8c1a1f6103188a2481b8acfd523ad983b851df1958d.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/974e43e24526d8abb19b37ece3e7889464dd7b24f930167f90a68cf4c356eb6c.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/990e2862c7c6d4867d127c740387a47cacc61e7d34dd5da652e87a80315b0799.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9b9d73943843f9f03df98fe8e17e940ae8f3d9b492e71c39bb43a3eb6aaa3395.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9ce1a40387f373e2f5cf9d696ae61408c42145203c50d08e4a1a2e4b982808f2.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/a14dddf49702ee2d9f4f81ecc6c4771e88cad8a9e94a86ca414b2b69ebef99ef.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/a20a5d24574d9564de355c96d5e4d6a2ea3dc579c3d9ff0027ef1cec1f1e70bd.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/a2bcfc6f1cccfabe124d53455630cb760d0babb3c50dfb21f9386813e1939681.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/a507cd3476c3e381701e698bae67128d3168e947f76e5d05ac9917ef99d53c1b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/a55573418998e6b496f985f3066835326ea8e74ef1fbb27c54a42bbc37ce422e.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/af9ea9054dc782919cf35de85d54bf81708167c52f5f9b7879df44c0f2f3b7fd.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/b1b6544a43e93459e54969800f7c07225acb9ff20cf860e7f6c6679be60427fe.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/b658ae7c4ecc76d40e1ed9abe7567a06d36e0c5053d4c9c09b0802bd6f5a0eef.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/b691dde5c6e05af94732abf7b3c79dbb239799fb296746ad0df6558da51b3388.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/ba209bcec3d7138e0e5667d2bcdd89abe0c9187324f551daa17d4b56bd54df44.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/ba52feda6f44d4651f9aff465f7e3f3e3ede5943f647f87b7a429466393c6f67.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c01f1feebf3e61de4593a74f076653b92d6b17b8a4b940f66c0ffc09fb3b4795.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c0f433a2b68517adae3929cd56d354de0f9da7a731a784e64c142da1994a08eb.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c195fdca3eb9ff7ba7be9fd271d7e1d5ab6ed432fef54253c9efb130e2d904be.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c24f4f4419c9cd04971e8d8ff2d0917e7d84441b10e0caaf55373547b8a47e90.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c29e889f7d45e67ab7f4dd05a78f9ddfcbadcac9624d986735a525608fdc6dc1.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c2aa65ec0dcb1150e28c9a17afd0b48e14a458083503d558f9df5069d3b8b8ae.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c2babe48fb44edb295948ea88f49aa5dc3094f947e31ef745324ae820226cb6a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c32a537caaa2be0dd08cb45c3a1f9b07f0e1956db116e73b78b214f2ee330b92.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c390310ca7db4b912df349d24b95187659575e067dab175806399e2e61ec0b16.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c5827f56924217b66bb50497d63af0c6da0cdaeb58f27f81f4661ab0cad69cb3.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c70bff5be604ac3b18608317dfe97467f21df8bf8285846266d0c65cee5f97d9.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c7467f0e5d70e764c02e68f7b0d15d7a0b7d183716df0d7df9838a21a3f5cba3.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c88198e8f493b312c0f2c0c4bb09c6b2fe54a52f4f01c66d93881597bdfe2878.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/ca02f29fe50826129d5999eeb73a48e6401db98fe6a1db7b1e178711a9df8079.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/d19a79cb97199d9ab4df34e03d627fcb969d15cf9c27e82441577bcb633c7c26.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/d73401de7f2bbdd9a1dc6e07a84fe5d2586b2467d81bc40d38fc37164193528b.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/dd3c7ef4266f16ff3d8346cb6103aa07fbadb5c76813cf415b4b328ee998ba63.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/dd56520304f1dc5c791bd9b945e8ddc0f3daeee1260d650e5e1934b8cfb8a48a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/e085c9c2b53847166a9ab17a44e66439cfbb5df6b69756723a75371648ed1cf3.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/e4e7acf45979838f356c04b7ec3095bb7b74e57a755db4c56726686e2186153a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/e8b34ef49f7e3d5c289584b8f662da40a05912794bcf1b4cb8e05e6c903bbc88.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/f1e2b781846a409de8fbec6fc761c6f5c035cdac61832a2cc0ce9555aa400789.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/f2ee7e0d1c0751be6080b514f391c6915be9730f59879cd250823432cb19e83e.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/fa94d5404c32b6c71fbbf2fe0704b75cf4b2fc80a52514532ca94f80957bf28a.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/fb26601111ee17fb0a859e4f54cc30c58a1514da54127fc6bda61cfabc36fca5.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/ff948157cffafd4565782da436cbe42bd52faf2b86c300e3007140cc55a6285d.gz',
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/objects/ffb6c644b70d9c9d23950d18157f5d6fd22d1a87f5fbf9dc5d4ee441d4ed5d8f.gz',
 'docs/GENERAL_COMPACT_CONTROL_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/KINETIC_CORRELATION_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/MODULATED_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md']
EXTRA_PINS = {'.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/ASSUMPTIONS_AND_IMPORTS.md': {'bytes': 1682,
                                                                                                    'sha256': '381040178ec5e07f57c495fe167fcb9431533790eed81bf28d2783ab53e610f0'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/CLAIM_STATUS_CERTIFICATE.md': {'bytes': 772,
                                                                                                     'sha256': 'b6ea9ed4ddc1eef609c2a07985dce3c22c0b7a69a753114762dd044f97df9647'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/COMBINED_VALIDATION_PLAN.json': {'bytes': 745,
                                                                                                       'sha256': 'd46c92cc564906e84dc0d9d8fdf704298ed95e735c1a4549266e540ab442db17'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/CONFORMANCE.md': {'bytes': 1141,
                                                                                        'sha256': 'aa6ea6ce4f5167b29007c8b1158fb6c472a400364e16d56e71f4957d84ae08f1'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/HANDOFF.md': {'bytes': 2273,
                                                                                    'sha256': 'f0bea7c6c5ed8553d7d82a01669452c4d24bf8c530cc7041367611ff6ed95da1'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MARKDOWN_NOTATION_CLASSIFICATION.json': {'bytes': 59,
                                                                                                               'sha256': 'b3fb351b1a7b5f7cef3df40732f3660b5fec9c34b14ca2bf46c5632a0c55d433'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_ENERGY_BRANCH_START.json': {'bytes': 2161,
                                                                                                                    'sha256': '1844393296a3b71c7ebdb51a5bb13f3235217b2a0ba6f9ed5aed08bed6d60b87'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_VERIFICATION.json': {'bytes': 44461,
                                                                                                                               'sha256': 'c24f4f4419c9cd04971e8d8ff2d0917e7d84441b10e0caaf55373547b8a47e90'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/NO_GO_DISCIPLINE_CHECKLIST.md': {'bytes': 728,
                                                                                                       'sha256': '7fa5dc91091af0cc082462bcc757dff6f8aa58f88f0d1cc3bbbbf8fc977aaad5'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/REVIEW_HISTORY.md': {'bytes': 4175,
                                                                                           'sha256': 'deca4a2a74e71b28536cb0c729d23be8970234944d967fa3c258ab460dc82d80'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_AUTHORITY_BOUNDARY.md': {'bytes': 1582,
                                                                                                      'sha256': '30834afe94837c9a2cd6cac9bef8680261a7ad9c1b52c4da34c694d2442deba9'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_RECOVERY.md': {'bytes': 1531,
                                                                                            'sha256': '5e653f7840861814f8cc2dfaad46897738b457bff5501baa1e2ded3741970b03'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/SOURCE_WHITESPACE_CLASSIFICATION.json': {'bytes': 40,
                                                                                                               'sha256': '1f17d6af0c04f649330e10640d58a597d18c20709555c9b01d786400c8b60430'},
 '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013/TRACE_GATE.md': {'bytes': 1015,
                                                                                       'sha256': 'eb00a2b8804275280afbaebfc09c122d88985d9db70e4045c31ade25aebad00b'}}
PACKET = '.claude/science/physics-loops/toe-modulated-kinetic-energy-20261013'
CLAIM = 'modulated_kinetic_energy_bounded_theorem_note_2026-10-13'
MAP_SHA = 'd1f1070647741d2d0319baa0086002e14d12057c07aef579c2590fb2b1017746'
EDITS_SHA = '57566c9a2f20163e6286bb98aa786c2e7a408794a32b0f3612e60d65c36b23e4'
PARENTS_SHA = 'd5cd1e41003f584c92bf2d322abf9ddc1dd8a3047f0c4d4c77a474ffbe530bcf'
STATUS_SHA = 'd0262d63ad080466e977573b94c0e66ca738257587106fb4b3b69c59260cfa3d'
GRAPH_SHA = '86dd3c57d521d8fac6613f5df964d421878dbf5a4b88ed220644527811808e3a'
SOURCE_FREEZE_SHA = 'c32a537caaa2be0dd08cb45c3a1f9b07f0e1956db116e73b78b214f2ee330b92'
ROOT_ACCEPTANCE_SHA = '4c7e3bba0a760bf09c3de680c18d44823af60d3f2b3ee43c5286065dac2b8d1e'
ROOT_REVIEW_SHA = '754fa7b9913c75b32665db816a3c9b6673172d1b8c2471e16acf19effddc555f'

def need(ok,message):
    if not ok: raise ValueError(message)
def sha(b): return hashlib.sha256(b).hexdigest()
def diff(a,b,old,new):
    return ''.join(difflib.unified_diff(a.decode().splitlines(keepends=True),b.decode().splitlines(keepends=True),fromfile=old,tofile=new,n=3)).encode()
def verify(root):
    reads={}
    def read(name):
        p=PurePosixPath(name)
        need(not p.is_absolute() and '..' not in p.parts,'Unsafe declared input')
        path=root.joinpath(*p.parts)
        need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),'Declared input missing or outside repository')
        if name not in reads: reads[name]=path.read_bytes()
        return reads[name]
    def pinned(name,digest,message):
        b=read(PACKET+'/'+name);need(sha(b)==digest,message);return json.loads(b)
    evidence=pinned('EVIDENCE_MAP.json',MAP_SHA,'Archive map changed')
    contents,origins={},{}
    for obj in evidence['objects']:
        need(obj['sha256'] not in contents,'Duplicate archive object')
        z=read(PACKET+'/'+obj['path'])
        need(sha(z)==obj['stored_sha256'] and len(z)==obj['stored_bytes'],'Compressed archive changed')
        b=gzip.decompress(z)
        need(sha(b)==obj['sha256'] and len(b)==obj['bytes'],'Archived source changed')
        contents[obj['sha256']]=b
        for origin in obj['origins']:
            need(origin['path'] not in origins,'Duplicate original alias');origins[origin['path']]=obj['sha256']
    contract=evidence['accepted_source_package'];prefix=contract['path']+'/'
    def archived(name):return contents[origins[name]]
    def source(name):return archived(prefix+name)
    need(contract['freeze_sha256']==SOURCE_FREEZE_SHA and sha(source('FINAL_FREEZE.json'))==SOURCE_FREEZE_SHA,'Accepted source freeze differs')
    seal=json.loads(source('FINAL_FREEZE.json'));members=contract['members']
    need(seal['files']==members and seal['file_count']==len(members)==174 and seal['total_files']==contract['all_files']==175,'Original membership differs')
    wanted={prefix+r['path'] for r in members}|{prefix+'FINAL_FREEZE.json'}
    need(len(wanted)==175 and {p for p in origins if p.startswith(prefix)}==wanted,'Source package aliases differ')
    for r in members:
        b=source(r['path']);need(sha(b)==r['sha256'] and len(b)==r['bytes'] and len(b.splitlines())==r['lines'],'Source member identity differs')
    selection=json.loads(source('SOURCE_SELECTION.json'));selected={r['path']:r for r in selection['sources']};inputs=json.loads(source('INPUT_FREEZE.json'));selection_seal=json.loads(source('SOURCE_SELECTION_SEAL.json'))
    need(len(selected)==len(selection['sources'])==135 and sha(source('SOURCE_SELECTION.json'))==selection_seal['sha256']==inputs['source_selection_sha256'],'Source selection differs')
    need({r['archive_path'] for r in selected.values()}=={r['path'] for r in inputs['files']} and len(inputs['files'])==135,'Input membership differs')
    for r in selected.values():
        b=source(r['archive_path']);need(sha(b)==r['sha256'] and len(b)==r['bytes'] and len(b.splitlines())==r['lines'],'Raw selected source differs')
    for r in inputs['files']:
        b=source(r['path']);need(sha(b)==r['sha256'] and len(b)==r['bytes'] and len(b.splitlines())==r['lines'],'Input freeze identity differs')
    need(selection['closures']==evidence['source_provenance_closure'] and len(selection['closures'])==7 and selection['recursive_upstream_audit'] is False,'Immediate closure scope differs')
    counts=[]
    for closure in selection['closures']:
        receipt_path=closure['receipt'];receipt=json.loads(source(selected[receipt_path]['archive_path']));rows=[]
        if closure['kind']=='files':
            for r in receipt['files']:
                p=PurePosixPath(r['path']);rows.append((str(p if p.is_absolute() else PurePosixPath(receipt_path).parent/p),r))
        elif closure['kind']=='root_seal':
            for r in [receipt['primary']]+receipt['source_snapshots']:rows.extend((r[k],r) for k in ['source','snapshot'])
        elif closure['kind']=='modulated_refresh':
            for group in ['new_source_and_authorized_metadata','prior_freezes','prior_bound_files','reused_live_scientific_sources']:
                for r in receipt[group]:
                    need(r['expected_sha256']==r['sha256'],'Refresh disagreement');rows.append((r['path'],r))
        else:raise ValueError('Unknown immediate closure kind')
        need([p for p,r in rows]==closure['members'],'Immediate receipt members differ');counts.append(len(rows))
        for p,r in rows:
            need(all(r[k]==selected[p][k] for k in ['sha256','bytes','lines'] if k in r),'Immediate receipt binding differs')
    need(counts==[32,14,57,14,29,23,7],'Closure extents differ')
    oldroot='payload/.claude/science/physics-loops/toe-modulated-kinetic-law-20261013';mapping=json.loads(source('SOURCE_MAP.json'));assembled=b'';cores={}
    for part in mapping['pieces']:
        b=source(part['source_path']);need(sha(b)==part['sha256'] and len(b)==part['bytes'] and b.count(b'\n')==part['lines'],'Accepted piece identity differs')
        need(part['output_bytes_0_half_open']==[len(assembled),len(assembled)+len(b)] and part['output_lines_1_inclusive']==[assembled.count(b'\n')+1,(assembled+b).count(b'\n')],'Accepted piece boundary differs')
        if part['role']=='unchanged_scientific_core':cores[prefix+part['source_path']]=b
        assembled+=b
    accepted_path=mapping['artifact']['path'];need(assembled==source(accepted_path) and sha(assembled)==mapping['artifact']['sha256'],'Accepted note differs')
    need(len(cores)==1 and len(next(iter(cores.values())).splitlines())==464 and sha(next(iter(cores.values())))=='422a92a8a24daa8fa240251ccae041fcca737af0335a486f33f3b20de0fb665a','Core extent differs')
    source_notes={'modulated':{'path':accepted_path,'pieces':[{'kind':'core','path':p[len(prefix):]} for p in cores]}}
    for pair in json.loads(source('SOURCE_DIFFS.json'))['pairs']:
        need(source(pair['diff'])==diff(source(pair['old']),source(pair['new']),pair['old_label'],pair['new_label']),'Historical complete source diff differs')
    edits=pinned('PUBLICATION_EDITS.json',EDITS_SHA,'Publication transformation changed')
    need(edits['source_freeze_sha256']==SOURCE_FREEZE_SHA and edits['additional_mathematical_body_edits']==[] and len(edits['notes'])==1,'Publication scope differs')
    published,wrappers={},{}
    for note in edits['notes']:
        assembled=b'';order=[]
        need(sha(archived(note['accepted_candidate_path']))==note['accepted_candidate_sha256'] and note['additional_mathematical_body_edits']==[],'Accepted candidate differs')
        for piece in note['pieces']:
            if piece['kind']=='accepted_complete_core':
                b=cores[piece['source_path']];order.append(piece['source_path'])
                need(sha(b)==piece['source_sha256'] and piece['additional_mathematical_body_edits']==[] and piece['historical_status_and_exposure_bytes_preserved'] is True,'Core contract differs')
            else:
                need(piece['kind']=='publication_wrapper','Unknown publication piece');b=piece['text'].encode()
                need(piece['wrapper_path'] not in wrappers,'Duplicate wrapper');wrappers[piece['wrapper_path']]=b
            need(piece['byte_offset']==len(assembled) and piece['bytes']==len(b) and piece['sha256']==sha(b) and piece['first_line']==assembled.count(b'\n')+1 and piece['last_line']==(assembled+b).count(b'\n'),'Publication piece boundary differs')
            assembled+=b
        accepted=source_notes[note['key']]
        need(order==[prefix+p['path'] for p in accepted['pieces'] if p['kind']=='core'],'Core order differs')
        actual=read(note['note'])
        need(actual==assembled and len(actual)==note['published_bytes'] and sha(actual)==note['published_sha256'] and len(actual.splitlines())==note['published_lines'],'Published source does not reconstruct')
        published[note['note']]=actual
        need(note['context_lines']==3 and note['fromfile']==accepted['path'] and note['tofile']==note['note'],'Publication diff convention differs')
        z=read(PACKET+'/'+note['diff']);d=gzip.decompress(z)
        need(sha(z)==note['diff_stored_sha256'] and sha(d)==note['diff_sha256'] and d==diff(archived(note['accepted_candidate_path']),actual,note['fromfile'],note['tofile']),'Complete publication diff differs')
    for w in edits['wrapper_changes']:
        old,new=archived(w['source']),wrappers[w['publication']]
        need(sha(old)==w['source_sha256'] and sha(new)==w['publication_sha256'] and w['context_lines']==3,'Wrapper identity or diff convention differs')
        z=read(PACKET+'/'+w['diff']);d=gzip.decompress(z)
        need(sha(z)==w['diff_stored_sha256'] and sha(d)==w['diff_sha256'] and d==diff(old,new,w['fromfile'],w['tofile']),'Complete wrapper diff differs')
    correction=edits['required_wrapper_correction'];oldprefix=source(oldroot+'/pieces/note_prefix.md');newprefix=next(iter(wrappers.values()))
    oldtext=correction['old_exact'].encode();newtext=correction['new_exact'].encode()
    need(oldprefix.count(oldtext)==1 and newprefix.count(newtext)==1 and oldtext not in newprefix,'Required normalization repair differs')
    repair=read(PACKET+'/'+correction['standalone_diff'])
    need(sha(repair)==correction['diff_sha256'] and repair==diff(oldprefix,oldprefix.replace(oldtext,newtext),'original_wrapper_prefix','normalization_corrected_wrapper_prefix'),'Required correction diff differs')
    bindings=pinned('PARENT_BINDINGS.json',PARENTS_SHA,'Parent bindings changed');parents=bindings['parents']
    need(len(parents)==len({p['path'] for p in parents})==3,'Canonical parent membership differs')
    for p in parents:
        b=read(p['path']);need(sha(b)==p['published_sha256'] and len(b)==p['bytes'],'Canonical parent bytes changed')
    need(bindings['same_packet_parents']==[] and len(bindings['canonical_core_maps'])==4,'Canonical input map scope differs')
    for m in bindings['canonical_core_maps']:
        body=read(m['canonical_path']);core=archived(m['archive_alias']);a=m['byte_start_inclusive'];b=m['byte_end_exclusive']
        need(sha(body)==m['canonical_sha256'] and sha(core)==m['core_sha256'] and body.count(core)==1 and body[a:b]==core and len(core)==m['bytes'] and len(core.splitlines())==m['lines'],'Published parent core map differs')
        need(body[:a].count(b'\n')+1==m['line_start_inclusive'] and body[:b].count(b'\n')==m['line_end_inclusive'],'Canonical line map differs')
    need(bindings['standalone_hypotheses']['edges_created']==[],'Supplied M23 hypotheses gained an edge')
    for h in bindings['history_only_relations']:need(sha(archived(h['archive_alias']))==h['sha256'] and h['direct_edge'] is False,'History identity or scope differs')
    graph=pinned('CLAIM_REGISTRY_ADDITIONS.json',GRAPH_SHA,'Graph proposal changed')
    edges={(r['from'],r['to']) for r in graph['direct_edges']};nodes={n['claim_id']:n for n in graph['nodes']}
    need(len(nodes)==1 and len(edges)==len(graph['direct_edges'])==3 and edges=={(n['claim_id'],d) for n in nodes.values() for d in n['deps']} and CLAIM in nodes,'Graph proposal differs')
    need(graph['archived_proof_import_relations']==bindings['archived_provisional_relations'] and len(bindings['archived_provisional_relations'])==0,'Archived proof relations differ')
    for p in bindings['archived_provisional_relations']:
        need(sha(archived(p['archive_alias']))==p['sha256'] and set(p['owner_claim_ids'])<=set(nodes),'Provisional proof input or owner differs')
    need(graph['history_only_relations']==bindings['history_only_relations'] and len(graph['history_only_relations'])==3,'History/math relation split changed')
    status=pinned('SOURCE_REVIEW_STATUS.json',STATUS_SHA,'Review scope changed')
    acceptance=read(PACKET+'/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_DISPOSITION.json')
    need(sha(acceptance)==ROOT_ACCEPTANCE_SHA and sha(read(PACKET+'/MODULATED_KINETIC_LAW_ASSEMBLY_ROOT_REVIEW.md'))==ROOT_REVIEW_SHA,'Root source review changed')
    scope=json.loads(acceptance)
    need(scope==status['source_review_coverage_verbatim'] and scope['freeze_sha256']==SOURCE_FREEZE_SHA and len(scope['required_publication_repairs'])==1 and status['required_publication_copy_repair_applied'] is True and scope['publication_preparation_authorized'] is True and scope['publication_execution_approved_by_this_receipt'] is False and status['N1']==status['N5']=='pending' and status['no_go_packet_pass'] is False and status['new_independent_mathematical_review'] is False and status['fresh_full_final_core_manual_read'] is True,'Review coverage or pending scope changed')
    for name,p in EXTRA_PINS.items():
        b=read(name);need(sha(b)==p['sha256'] and len(b)==p['bytes'],'Additional publication integrity input changed')
    need(set(reads)==set(AUDIT_INPUT_PATHS) and len(AUDIT_INPUT_PATHS)==len(set(AUDIT_INPUT_PATHS)),'Declared read closure differs')
    return {'result':'source_identities_and_reconstruction_match','claim_id':CLAIM,'meaning':'Byte integrity only; no mathematical calculation, proof or audit executed.','mathematical_operations_executed':False,'mathematical_predicates_executed':0,'scientific_mutations_executed':0,'no_go_packet_pass_supplied_by_tool':False,'independent_review_supplied_by_tool':False,'external_scientific_input_reads':[p['path'] for p in parents],'package_local_integrity_reads':sorted(set(reads)-{p['path'] for p in parents})}
def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]),sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no coefficient or moment formula was verified.')
    print('per_site: checked and not executed — source integrity only; no CAR or cell-locality theorem was tested.')
    print('per_mode: checked and not executed — source integrity only; no dispersion, alias or endpoint estimate was computed.')
    print('per_block: checked and not executed — source integrity only; no graph norm, commutator or domain theorem was tested.')
    print('lattice_wide: checked and not executed — source integrity only; no all-time, driven, energy-law or no-go theorem was verified.')
if __name__=='__main__':
    try:main()
    except Exception as error:
        print(json.dumps({'result':'identity_verification_incomplete','error':str(error),'mathematical_operations_executed':False,'mathematical_predicates_executed':0,'scientific_mutations_executed':0}),file=sys.stderr)
        raise SystemExit(1)

#!/usr/bin/env python3
"""Proposed source-identity primary; no mathematical predicate or archive execution."""
from pathlib import Path
import gzip,hashlib,json

REPO=Path(__file__).resolve().parents[1]
PACKET='.claude/science/physics-loops/toe-local-clock-windows-20261015'
NOTE='docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH=PACKET+'/INPUT_MANIFEST.json'
MANIFEST_SHA='eac7f6d5ac78530928351a243d9cb316a8b22e4c19837119873953f2b9ab7440'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=('.claude/science/physics-loops/toe-local-clock-windows-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/BINDING.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/0170c941e59b7b227dc2136d5945d6c6f3e8ec5b89a196f7d80c20413e81aae8.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/02d45e18bf8298d0bcdd977699dc62773ab6d3e8d60d4c743c8c2c375d8185d9.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/03d7e8d5519d3a2e0734d0b76d2fae2656494a77a30aaf04fad77af0c1ed8bbc.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/0cd0adfcdfd5d401f573d8083cc246467a81ab6af9ead7b85cbfe330dae339f9.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/0d2466043241f26eaa8e937099a5b3b3f74814df7e72f5949ec30360741f6250.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/0ee6ed33ca7ad3bc6a3ad52ca0cebc4d40512d70bf5986162651fe53ac2f4ea3.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/101d7778f3aaecbdb2db277c2d9857eee53cc7fae93941e444fe03d939ff36e9.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1398ab94f65a2a3522eee2b0cb709ff38a218c02d185cb636c6686c6a952e5fd.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/17dec3f88ec6af2c9d25a59a0853c3416577351e2ccb6f83dd54202c50258823.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/180ff93c22dbab6ad42f3893b212a6366c1507b6a7c329cf40815f5bcb99ee26.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/19124c6a57a9b1d0ab5504b32ee6f3a3c415820834e7e378e44de90b2720efbc.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1a537faac6c99de5cd7843c281e8c598fc2f0f79d8c9767756393f01b2d00a69.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1a977bf4218aaaf31b8513749bdc3a7195fe2567a3e2de53fdd781382bd9ffdf.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1b5eb8dae33a3eb3697fc48857284112eb265ea7803a6ef52069499f202ae918.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/1f7691b6584effc866e7b93264372d615ce1e20d6768278ccc6efda2138adad6.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/214cc18f05ebf2c3005e61666b3e5a87de1389f028468a3f468faabcc8d24bf8.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/21a6eb8e4d5e76f8804f98472a7822b2c7994a06d187b7fc2adbc39ee8b21454.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/21bc09749ed5057593ce66b5096d04c8e88e6c533a9eecbbd2f85ecc73935dc6.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/227ed73188146ac9cec8a7e54e2ce06c80728de4dfeb48ec4773a4a98fcf70b3.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/2a94eeb3988eab4cd64b411974ef367551e3a5ed3d4fdaba7c112f6ad8376b59.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/2aad7d6ab9e544e35c4fa3746876bb12b03cd2d505212f9e94fc8ff5befb3770.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/2f00195e9b7774759733f28f543cb87ab0c3fc5b268cf5afb9d1825e634749b2.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/360f55b23214b774f2b0c32a34ae3421862f98a2e6e3833d7ccf244ddb7e2200.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/371636eefb0d3ccb0b2738bd3feae3787bb27d17e1f34203a1d91399ee0a1176.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/3bef2534126fa1c283871eee8d97f1c74aebb75a47493bf4d6c982e96a944cd4.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/3f8114755c937da7b8c9c419c2ba63e2feac4a13381dc5c1ebbbd92ce6ac03cb.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/419450af5a2c156e3a8408a4ba24d00d1655694291a4798117b52e76802334f1.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/42ed00824cb27bdd5f0bee6069a49477eddf9ee44ad8ba348db405488c21ddfb.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/43676d510bef767f15d5f501afea09db777253f287668d16254f02475f437972.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/4570b2b4eedd68bc8ade7c83e20fc507da38f4f745ed59939c6f53bbbb27986e.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/459783198c2fffc1fde9e969af242484c93ae5cad266a9b7f2d578acb4c866dd.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/4662349b2df694154108cbf9af1af97b614f09e3128ac24a566b377e54384286.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/4a53b862cb59b43d5af5019e2b5047c1f82b888081214c7c69ae23dea451851f.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/4bcde7c39f8e3da28448bef59298cedab48d18851d9c2fd8d5d5a49a36ff4ce4.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/4e67377ed1a8a907fa93d4925ce4613967e13888d69baeb4a24ffa45f58d53e0.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/5415903eab5d628944305a2254320ed111ef4f0f9797d216d9f2efad11c2557d.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/55801a0c15695bff6e851572903aa7b89c3fdd6a94e7d1cfbaa848150e730af0.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/574d53ef66582ed75fce5cc973ded8c2f9ff372d6b8d9abceddba201728b082e.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/58b7587d674ad55c40c0620232b92b6aa43f1018d101c0f60aecb03c310fd831.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/6259f94e595dbd5bc698569158cb0a9900c402898764ea1933bcfa9519365a4d.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/636b82935502eed427be2f4544c5fc353ca47cfdd4d183d08e1072f99da14870.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/654d2a2d6c5846ba63b38457dbac6eef5872c78dc9087136b7e785c209e29c94.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/683fdd256cdc335fecd970d6988823b95101bbc1bb258d8e30bfafc5c74d6444.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/68e68622babd0b9eee16f6dd6ba8ba634a87fb3d604c82140d74ccb675ef564b.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/698c3c7a780c8a39ec6c62e8335c7375d03d62e7aa61076a4618c99b1bb1a755.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/6a0274bd8a5fd7e2367268d973e7ac50ba38b9e12d3cbfbc8652486d900b5aea.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/6c96605c7ad40d2999f3aeb5e8f24142c3f5ff4637b30e602714710bbf5ea944.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/73bbe26778b88afe6d8321320f0e202d3e29f2c0dd3e7c81b11e2fe14261f40a.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/74f8e3f1e058188087abe5bd13613ca47fd054e7add513e644ea3c9c1f481dec.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/78fd996830e5ac3ae7a808bb93c1dfb098d79acbe73430da6c7eb849265809a6.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/7cd21954688320e68215c33e1c02a2a402a92b47593fe7c4b1cc3ecf7eebd56e.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/80e8cc0a77c37b8d645b053cdd13bcf0e7eeb52d4d9545204e3a29076e261e7d.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8395454b774d9348d10759d17146a67b6515507543ac0b2769d6878650ed685c.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8582b4447a282f86a143d81e93b6593402f4438465fdddca49ca36ed28209f80.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8616797c17165078be2c8e6691a4b46f69f3fc6701870a9b7c002631cfbe80b3.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8629f32e8b3be8a1bfe9ffbb5b9ef1c779f1b0af1670041a42ad3bd2a9787ad5.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8799301a652f2986330e1ec3b11cca69a7e30e8a54b31c20debff6fbb53c1145.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/888ee6e46a124ecbcee57dafbe8d6a6cf13b5cf94c02ea658aedc9c81676e06c.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/894909dbd765aa3677ddb14ab9d6c9d55f0818ca670fc4320523dcfdf0362b40.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/8f4ba2ff48e5e5a78d9e3aec5ee38e94a58da44bbf3a3d3a7e2b0614f95e93c2.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/90931d2f217c45d1c6f5058a48d49dc8c5188c6fef226f7045fcb5f75786b47d.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/922a48a1238d3cc5ae0e2a80f2d8c53f44c7d54781da3d9c6fc6cb84fcfd09b7.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/92e64ba86be7a7d3e5d706d7538b825f9ed7043504c41e3c41d8976e5e47e945.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/92f6b1603e6bde15d7150b850ecc515d08d8b5cf41ece77e4acd6db49c323789.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9405b460055db67ddce232dcef91d4c1f0ebfd0968758c702894239ee109908a.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9457e034bfab15aa142633180829d9563654eb8cbef63d89811461458cf0ebd8.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/958b38f288a7864661ac6f86f32ea76441cd9fd1b35d332c865d75709ac04128.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/97b8b3f48918cf76e0254e3863584f8ab4d95a750380387bdff0f6c6c6c456c2.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9950cbcf67caff6b748047a330d259f6a80b1756ec608d42d7f455262f951da8.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9a0801884773a685356db2155af8442825d7288ef8c81d26ac2f752988117023.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9b2011b480fd2fe2e7583ebcca39d2e3667d9445d773cc4ae681c3e7c905f54a.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9b25e1081b5f4d54b62beaec676d5aed4b2e11593b5beb1dc2941e033cd799e3.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9b5178ff3e759cbd0b3cbd2283bd9c2fe5e91dd80337e1d532fb2cf10b8b61b2.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a037fe5308a8788c4a1c55faf24b194c78d9bc2702b0038529bf763144a11c60.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a03a97c3aa9c736e72b20b63f4530e0cbdc975ab1414653ecd75314d2bdcda7b.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a3908a5fec53c806cdc7479c115977d2c67f56cd1b64e3dca6035405a856c0fb.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a8e82d8ab6df91075035bbc44148ad351e69644cb5698fecb77bf113e886e257.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a94ed758a4982b3665537b134a71a8312e9a1a4a6b05d2dcf11cccf12f4ac276.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/a9f662157c5cea8ae70d8263089e92a7e1b02e294f0f745e893625678180e616.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/adc168e3e0cb9461e8f8dea825cef1949e1dc86fcc4bbfcb7d31612d0dbf186c.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b0f6467f65d83a100925fe7f82a076a9c6ad7ee9277914140afe32e9b8aef9ef.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b32f64d1570ac8d48564466d86187020cad6780a9d799bdb78f24048d3570d8f.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b68fbe20faff289c36dcfd8d89d067fce931728b1d70f307f8d055eabd8ca8c2.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b7d85ba266fcd54e17ae50ebf2a6dfe25b4cf981c650d8f8df19fc29b7a7cbf9.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/b7ed443212fbdb5c9ecea51b77b46d990e7404de0cdb01d93f00b16d705d1bc1.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/bc08f951f2912de840ff463f3db9549cb971f68ba22c5b1eea5c18bd721c83a9.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/bcdf175eb67349081d6c923c6c1b993b5a3eef4c5a587064df05339dd2a47673.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/bd6514b34022d37a0165c2c4cb86fdabc41ba7373da2f2dc90b24a7c509546f6.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/c1fab3fd4dff3572d036ec33fa63b1307f76e79691e2ac7f802b34774a7528ad.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/c910531b89a54bff5343aba5289226a273e9513f3c1364d62ad5e079c3f8c03e.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/c91d933e9f33a32f6549398a5da965c60903831d1f99964f029f43cd3b24a5df.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/cba477a130388b78cb2c4f6290dfc78e0d9ba28e017d92d5fd2370007c216f2c.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/d18dfd29beca4b1b672f122b79b0c232af70d155d44d486925eb13c914363e48.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/d1c523f544d79db8ab7ec745d30d950b93516c706115e04c8c9c84a08a24aaae.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/dd1c5d8f15f3bccc7e69735b4a2d4ff0e7e97b6676c79b8d028512f8b3ec7946.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/de1981bf0f34695f9b449fd1cc3243133a34bb29bc9a9df07fbe8a14dcf30385.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e18a83b5f5ec44d280b3fb0d71921be50d2387563fb9887e223da33c190e8ecd.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e2b62a31f92079a939e0137ac16fd549863d093bf16c76355813df3456ace2b5.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e40bf27e392c93841ef9b4cbe87ab230836fdb46a5775c79ca3d329c6d17bc70.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e69896772ced3d2232016a96c944466e1968cc35805edf9ab8001a4047ee99b5.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e84dae2e32c9522590e42c2cef2f850918a975f2b342c5433045af6f5afcf24c.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e8995423831d7f0c2b940cae8a1646ff6fe2b803370c683040e769861837291b.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/e94523325fe80daacbc1d291de59b666bf3e473517b95512d7ea9ce213a39ea4.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/eb567bcba8915f1766a030bf71e8b3570cf811932cfd33b83cc22c85c6d50e5b.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/eca51f43ac518003e2f14df73ad50cb621a457c971cd25e76f010af66f108591.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ecf14c8ada5e06c8dc17a89592afba47126988b704b45d94a03fbfab41acf107.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ed7ecceab529f2caba9fce560ff86f393d329388e65283a507da5f02bc4026f8.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ee27d4fa8d66500c2211cb4479a9fb4b4449c0dee4ab2af02befa4478a644f13.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ee57e1deb8df4bf3d4e112e6e62e70e462595b63668aa6fd60c84d9b00c90f6b.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ef0fe6d2ca51d199b97d422761ccf15b8147b9e15ce8bd72cae5a682b195e612.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/f08a7af4736053d55f465d5bbd79affebfb728a8efe6368cb3d4d0ab4661f3f7.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/f6f0a5d224078c7e55fed666a5994e7dffc5f317408f1d2c7136760853c00eee.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/f7af2d4465398c9b163348f5e9f33fbb7ac72250b561e04c2f3dc905b282ff35.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/f9466a3c8f5fa51d4f1e86609471fdb9382c1dcdb14f0e50d4a15164efd20e45.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/f9a8f884f202bcaf846ee8438cb64a0936f495c4fdf7cba55b7606c912d5cf7e.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/fc63ea1ed84f9e61f2ad0fc96ce33bdcff5779a9c0e38fa7c73d02f6a829cefc.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/fe55108b02a2e297054ac33bed23c6966bab75f6f7f0abf03a44887e884b241a.gz', '.claude/science/physics-loops/toe-local-clock-windows-20261015/archive/ff90c93cff07a82b5a9c26c7193083fc65907879d8e715dcf029f9fdac1dbe7d.gz', 'docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-local-clock-windows-20261015/INPUT_MANIFEST.json')
EXPECTED_PROOFS={
 'local_clock_readout_window_domain_revision/AFTER.md':'fc63ea1ed84f9e61f2ad0fc96ce33bdcff5779a9c0e38fa7c73d02f6a829cefc',
 'local_clock_readout_window_independent_domain_revision/AFTER.md':'101d7778f3aaecbdb2db277c2d9857eee53cc7fae93941e444fe03d939ff36e9',
 'local_clock_boundary_window_candidate/DERIVATION.md':'b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1',
}
EXPECTED_ACCEPTANCES={
 'local_clock_readout_window_root_review/ACCEPTANCE.md':'c910531b89a54bff5343aba5289226a273e9513f3c1364d62ad5e079c3f8c03e',
 'local_clock_readout_window_independent_root_review/ACCEPTANCE.md':'4662349b2df694154108cbf9af1af97b614f09e3128ac24a566b377e54384286',
 'local_clock_boundary_window_root_review/ACCEPTANCE.md':'bc08f951f2912de840ff463f3db9549cb971f68ba22c5b1eea5c18bd721c83a9',
}
EXPECTED_PARENTS = {'premises/root_word.md': ('docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                           18448,
                           36172,
                           'de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd'),
 'premises/independent_word.md': ('docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                                  36233,
                                  66890,
                                  '6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a'),
 'premises/root_cell.md': ('docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                           14202,
                           25142,
                           'ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6'),
 'premises/independent_cell.md': ('docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                                  25189,
                                  52484,
                                  '43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5')}

EXPECTED_CANONICAL = {'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md': '6a0274bd8a5fd7e2367268d973e7ac50ba38b9e12d3cbfbc8652486d900b5aea',
 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md': '1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256'}

def digest(raw):return hashlib.sha256(raw).hexdigest()

def checked_inputs():
    raw=(REPO/MANIFEST_PATH).read_bytes();assert digest(raw)==MANIFEST_SHA, 'input manifest identity'
    manifest=json.loads(raw);assert manifest['schema']=='finite-clock-window-inputs-v1'
    members=manifest['members']
    assert len(AUDIT_INPUT_PATHS)==len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS)==set(members)|{MANIFEST_PATH}, 'declared input coverage'
    data={}
    for path,row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b=(REPO/path).read_bytes();assert len(b)==row['bytes'] and digest(b)==row['sha256'],path
        data[path]=b
    index=json.loads(data[PACKET+'/SOURCE_INDEX.json']);assert index['schema']=='finite-clock-window-archive-v1'
    originals={}
    for alias,row in index['originals'].items():
        assert row['stored_path']==PACKET+'/archive/'+row['sha256']+'.gz'
        b=gzip.decompress(data[row['stored_path']]);assert len(b)==row['bytes'] and digest(b)==row['sha256'],alias
        originals[alias]=b
    mapping=json.loads(data[PACKET+'/BODY_MAP.json'])['complete_proofs']
    assert len(mapping)==3 and {r['alias']:r['sha256'] for r in mapping}==EXPECTED_PROOFS
    for row in mapping:
        b=originals[row['alias']]
        assert digest(b)==row['sha256']
        assert row['end']-row['start']==row['bytes']==len(b)
        assert data[NOTE][row['start']:row['end']]==b and data[NOTE].count(b)==1, 'complete proof interval'
    assert mapping[-1]['end']==len(data[NOTE])
    binding=json.loads(data[PACKET+'/BINDING.json'])
    assert binding['conditional_acceptances']==EXPECTED_ACCEPTANCES
    for alias,h in EXPECTED_ACCEPTANCES.items():assert digest(originals[alias])==h
    clauses=binding['exact_source_clauses'];assert len(clauses)==4
    assert {r['alias'] for r in clauses}==set(EXPECTED_PARENTS)
    for row in clauses:
        assert (row['canonical_path'],row['start'],row['end'],row['sha256'])==EXPECTED_PARENTS[row['alias']]
        b=originals[row['alias']];parent=data[row['canonical_path']]
        assert digest(b)==row['sha256'] and len(b)==row['bytes']
        assert digest(parent)==EXPECTED_CANONICAL[row['canonical_path']]
        assert parent[row['start']:row['end']]==b and parent.count(b)==1
        assert originals['canonical/'+row['canonical_path']]==parent
    assert set(binding['canonical_sources'])==set(EXPECTED_CANONICAL)
    assert all(binding['canonical_sources'][p]['sha256']==h for p,h in EXPECTED_CANONICAL.items())
    assert binding['binding_complete'] is True and binding['stage']=='root_bound_review_milestone'
    assert not binding['root_runtime_freshness_and_feature_binding_pending']
    assert binding['observed_base_head']==binding['feature_head']==binding['source_head']=='88a5ecbe090fefdacc7a13b6a0243aa2c0cc71fe'
    assert binding['observed_base_tree']=='9669328d461a451696d83f68010e62aeb5da2be1'
    assert binding['base_pr']==9590 and binding['base_branch']=='physics-loop/toe-local-clock-word-20261015'
    assert binding['branch']=='physics-loop/toe-local-clock-windows-20261015'
    assert binding['publication_pr'] is None  # Dated build record, not a live PR claim.
    deps=json.loads(data[PACKET+'/DEPENDENCIES.json'])
    assert deps['publication_binding']=={'binding_complete':True,'base_branch':binding['base_branch'],
        'base_head':binding['observed_base_head'],'base_tree':binding['observed_base_tree'],
        'base_pr':binding['base_pr'],'feature_head':binding['feature_head'],'publication_pr':None}
    assert deps['publication_binding_complete'] is True
    assert set(deps['intended_canonical_targets'])==set(EXPECTED_CANONICAL)
    assert deps['expected_after_actual_binding']=={'new_nodes':1,'new_edges':2}
    root_review=json.loads(data[PACKET+'/ROOT_SOURCE_REVIEW.json'])
    assert root_review['completed'] is True and root_review['scientific_programs_run']==0
    assert binding['new_scientific_programs_run']==0
    assert (binding['archived_selected_fixtures'],binding['archived_scientific_attempts'],
            binding['archived_successful_attempts'],binding['archived_failed_attempts'],
            binding['archived_failed_root_metadata_attempts'])==(3,3,3,0,1)
    assert binding['ancestry_alone_supplies_mathematical_premise'] is False
    assert binding['optional_four_rail_word_instance_adopted'] is False
    assert originals['local_clock_readout_window_domain_revision/BEFORE.md']==originals['local_clock_readout_window_candidate/DERIVATION.md']
    assert originals['local_clock_readout_window_independent_domain_revision/BEFORE.md']==originals['local_clock_readout_window_independent/DERIVATION.md']
    return data,originals

def checked_receipts(data,originals):
    archive=json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])
    science=archive['scientific_attempts'];assert len(science)==3
    assert {r['id'] for r in science}=={'root_exact','independent_logical','boundary_coefficients'}
    for row in science:
        receipt=json.loads(originals[row['receipt_alias']]);assert receipt['exit_code']==row['expected_exit_code']==0
        pre=json.loads(originals[row['preseal_alias']])
        assert pre[row['preseal_time_key']]<receipt[row['start_key']]<receipt[row['end_key']]
        for stream in ['stdout','stderr']:
            b=originals[row[stream+'_alias']]
            assert len(b)==receipt[stream]['bytes'] and digest(b)==receipt[stream]['sha256'], 'recorded stream: '+row['id']
        for member in pre[row['preseal_members_key']]:
            b=originals[row['source_group']+'/'+member['path']]
            assert len(b)==member['bytes'] and digest(b)==member['sha256']
    expected={'local_clock_readout_window_candidate_seal':0,'local_clock_readout_window_root_sources':0,
      'local_clock_window_independent_domain_revision':0,'local_clock_window_independent_root_sources':0,
      'local_clock_boundary_window_seal':0,'local_clock_boundary_window_root_sources':1,
      'local_clock_boundary_window_root_sources_retry':0}
    assert {r['label']:r['expected_exit_code'] for r in archive['root_metadata_attempts']}==expected
    for row in archive['root_metadata_attempts']:
        p=row['prefix'];receipt=json.loads(originals[p+'/EXECUTION.json'])
        assert receipt['exit_code']==row['expected_exit_code']
        for stream in ['stdout','stderr']:
            b=originals[p+'/'+stream];assert len(b)==receipt[stream]['bytes'] and digest(b)==receipt[stream]['sha256']
        b=originals[p+'/executed_source.py'];launch=receipt['child_source_at_launch']
        assert len(b)==launch['bytes'] and digest(b)==launch['sha256']
    assert b"KeyError: 'path'" in originals['actual_runs/local_clock_boundary_window_root_sources/stderr']
    return {'scientific_attempts':3,'failed_scientific_attempts':0,'root_metadata_attempts':7,
            'failed_root_metadata_attempts':1,'replayed':False}

def main():
    data,originals=checked_inputs();receipts=checked_receipts(data,originals)
    print(json.dumps({'result':'analytic_source_binding_completed','complete_proofs':3,
      'decoded_originals':len(originals),'scientific_programs_run':0,'archived_receipts':receipts,
      'dated_canonical_source_binding_complete':True,
      'scope':'Bytes, complete intervals and actual historical stream provenance only; no mathematical predicate executed.',
      'limits':'Dated actual word/cell body binding is separate from later PR status. Three distinct conditional windows, supplied preparation/vacancies and a conditional reader comparison; no concrete reader, native supply or retained audit. Source hashes are not proof.'},sort_keys=True))
    print('per_element: arbitrary old input/reference; supplied one-head entry and full time-indexed output')
    print('per_site: distinct negative m5 rays versus positive occupied-chain endpoint; actual vacancies required')
    print('per_mode: one-excitation prepared maps separated from full-space apparatus bounds')
    print('per_block: three signs/times/entry conventions retained; strict gap belongs only to positive apparatus')
    print('lattice_wide: growing resources and supplied reader interface; no concrete reader, stop or native realization')

if __name__=='__main__':main()

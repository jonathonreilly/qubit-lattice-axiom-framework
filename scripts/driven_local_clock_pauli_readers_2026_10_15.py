#!/usr/bin/env python3
"""Proposed source-identity primary; no mathematical predicates or archive execution."""
from pathlib import Path
from datetime import datetime
import difflib,gzip,hashlib,json

REPO=Path(__file__).resolve().parents[1]
PACKET='.claude/science/physics-loops/toe-local-clock-driven-readers-20261015'
NOTE='docs/DRIVEN_LOCAL_CLOCK_PAULI_READERS_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH=PACKET+'/INPUT_MANIFEST.json'
MANIFEST_SHA='7c52ecb94b44aea87005152bb7b76a5b78e65d9e6778e02d78e3610efd3e428f'
AUDIT_TIMEOUT_SEC=60
AUDIT_INPUT_PATHS=('.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/BINDING.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0112d4db3e258338a16b07c1409f2a3f298ac7cdd2ae196a2f2b756f66a3c470.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/02b8683d2b2841fe9fed86fc4b3aecee34ec9b366bc251aff1b2cf51bdfd036a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/03d7e8d5519d3a2e0734d0b76d2fae2656494a77a30aaf04fad77af0c1ed8bbc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/040ea1ededa3baff3e2646bfb56107bd01eb3b3fd1cc5570c894a131101416b3.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/04565926036d3044b93700cca29b218ed93f18ba66c13acabb5d17741275d20c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0687dc3b5f163e76fdfa0db2fca22bb754df95b2c68d3a426fc394ea1d6777cb.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/07cd03304d38dcc6ba6896b07813580d9f2079320aef3afd3ba5e8715db0ea8c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0833e2b41146250ae51ca0a4ac0029ac46a77bf44b8453cc60dc2d96d5134339.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0b61a4a77fca2da595d0c716d82d5b1c60beaf83a16a6bce984d3f0f6c5e9adc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0d9fe887c43141d0803dc8b4ec7e535e9099578c9748c3557d7acade68803ae6.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0e1f839d61b3d329ad735dea9c4c55f4c85691cc1e589782471725e32f95f875.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0f41bc45578c78a0511688be6411b10c8dff38adb25043855b44c396a27e643a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/0fe927d52fb85c5c97243faf0c5f0258d619095f3782b97d8cc37f16ff6d84c3.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/101d7778f3aaecbdb2db277c2d9857eee53cc7fae93941e444fe03d939ff36e9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/108a7ccea775e7916b13c45ce5995a052cc059ac0b21da0d208cde7f10663428.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1359377884308d5817be9cfb0e38b4e04c3cb29a28b2843fc43e26b3bdb1b3de.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/13bf3763094191529f5059094bc5046b23811ecd7a0bc5d1b171f401f8087e4c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1937fb2ade92404c2d304096d5f9b18ba7e63fd202851c3ffce320027fb8174d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1945bcbe783eb2d8006c096c57393a844c3c2b0a27dc5e763de565389fc21143.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1c47b621b74d45ffba5c3175b8531e249b418329873e4ea26043934ec03bc1cc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1cf03b8d6fee01a3b82ee196b78652a49153ad7528e4c6c7ab3168dff854d669.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/1db0909d0a7a7c1989b203825b644444fe47f07b3ce3d08596286ae1d36bf4fd.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/201e65732e78142b336be12988a28d6f350dbd9664611a837a45eae5668ff14c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2094fdb64f92b5c1cb801eff096c099f34588d37e32ed3ad34f68f3d8097d9a3.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2281fa76188a6642f60acbf3338d1cdbe09ff69650f33fa89212b3b252968dab.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/252eb8b955b4910f29a636adf2bd46da6c3ab5d4dd0830305536766d584e7210.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/27a34dd0d7027ad8687f5477cf9bd630c3820a7fa9c1f3ac5f323be764c65952.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/28411bfc4787d894bf6e300d777691f156bce72c0aaf9cbbb65c303a2cdb9164.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2874d5fd4f072f945d32e665e1f01da3bb956851ccab36c0f3aabe114561cd12.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2aad7d6ab9e544e35c4fa3746876bb12b03cd2d505212f9e94fc8ff5befb3770.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2b83aa1481b5beb011bb147b7b752ad367b20a21b0eb2770df4dc69b679725bf.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2beb8f39ad40c90b8e6646f9068e6da87dc7eaa016ce728b12fc0f29af0c7f89.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2d2a383d8caf1e5f4893c525822f8cd3572aff048fc1e64adea24a5d6ad15568.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2d45127878ceda1f419dee8e4e5011d59c65382b866255263b6d054e341cfdd9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2e21445ecff9477f49c45a05d80e285c3f81c50388b4dda2fc7daf278ddd1b35.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2e9bbf4c4a0df315cdeabbfeac01e330f4347809ad9cfe7270657f7bc8e5d1c0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/2f9f533f3e170037e38e1cd9c60bc12391b2db23f67d4b090c8ac082d89f1005.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3156bd2ef57f9ab55d338d303b3e67a6f25da4254d8ef3dd6acd3a0ef4f36db9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3156eded0dfce60389efebcc1ae3e45bfe9a1266dbaf17569e1b9b4c67de4b77.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/32dd117542dd437d6634e20fa5b9c728b08be55c9ddeaeb8aec1d61023359941.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/34779ed5044aad66be87dff241898a176869074871bad8f0a5e207e6de580ef6.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/36378547b4e4b8167bc4008dff5090632ca4ab81b39ac27d8c6a69aee02ead9e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/37f5586df59256638bb2fa009c58f7da908d69b817e1e3c10e0c0ddf1bc19baa.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/39b63ae95be19d901efc4db8b78cf6ff3aa9c7a9787c43e405d97b44c3bfeebe.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3a5b61812c4d282b1e2c52d768c6c51666b58748f356d067d130339e63c777f9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3b1572daa0182a20f94a784f1bfd1f866b1728d9fc7ca5451e99ad4f1637f37c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3bf3579c2bb962be55dfc53f65219d7aa975a27f4499213e7ac53b9393a24fc8.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/3e3739ce01f93dbe4db47076964b90130f499d05015ce4aee2ddfdef89827452.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/406dee0a10515f717b2f5741f926714621a79b3ebc5881b6fd19cb6401b506ee.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/430784aa8ab8af099c63d8f13a356c1eae5d88f6a702ea7bf860a023905e7c3d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/43e9ba6e75d74b10559506cc426966543d6ed28e54e4881b957c91f3b16c1574.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4569ac2f696f576731fe1a13c9e3b2f903270018b92a2e7decd55e9df944b406.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/459783198c2fffc1fde9e969af242484c93ae5cad266a9b7f2d578acb4c866dd.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/49de871d54f617af3bfa69ba15727fc9de3599788456f55d2d737433406f1982.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4c17e4aadb899315284c36fec71469b6d34b46f5fa5553e33b46fb9467e0cf35.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4dbbda67277c563b98d07d55b5dcb20b748bca427418d583a8e87cfa4f61993f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4dd88c8e50f8646ee12ca50dbabbd780814e4702717145bab4776be7e96eaa63.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4e67377ed1a8a907fa93d4925ce4613967e13888d69baeb4a24ffa45f58d53e0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/4ed65f2f981114053891e8ccbafafc07567a2667443b0649372e290fa3644912.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/518bd5992f7eef9d1c31279aa425a3aba50096f1973a711c219f6a3c5120cfaf.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/51a74faa6709096b47dd26305075aa18671a1a43a1ff5959079962668f3cd298.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/51ab1078436d33d57540ccbb81079dd4036857dfd3e595226b4b955d98ce847a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/526a92c6f5239f18b07cf46697a14e0a04da5df4a7f55150b655c9908eadef48.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/54eb325fcaefbbce00618beb9b1abef4ec46b08e6038a5f7a30c554408d35014.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/55801a0c15695bff6e851572903aa7b89c3fdd6a94e7d1cfbaa848150e730af0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/56f12c6eaa3baeecd6f905a800b05e077ff6604543df2728bc7b390ae84c0983.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/575e17f96ba606738733b0bd7a15e32f9c63f3d9e76a6653e5c509c13e519117.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5b376084d94dc58c54a35b115b71a5f454f7b09308a162e407fa8d7eaa5d560c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5ba2f6941dc6310054b4d7c99247ff65c94dbedf950e3128c563f12d5e433b6b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5c671d4ee02e48ffb57976a83f4c1cec57f3635fcb793182e181f1f3cc9bc8f0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5d795fb3458e1a3a37031c373251ffa6a372ef35b1b9cc33152df7d835d4c44d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5e40431e607aa5563282fe9b0313bc0a02be131e33c7e4a7da58d543e9ddd4f6.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5fd2dd9bb7b5e93e8ea01019a9506969f93176f298f57ab06daed6ff17b1ab2a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/5ffdd752c151a4d4c0aa99f8299d5095b1954ee87303a71f266606d6b9493940.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/617668dbc9b6d9d7f5e2cc50ceb3a2799baf3e2a619f432a61276cf6d75eb10b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/64654483cd0346270ebebe040e3f0b6d8d869a3f853b64a71ed1974e7e65194f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/67080402f1cde251fbb97721028f9ec83c7a12dd5fa9041ffe89d7db86475233.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/68b00f76892ace92c3492fa09f051fc203e9bcd85fdf0ad6b48d877a83fe0e1d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/6a0274bd8a5fd7e2367268d973e7ac50ba38b9e12d3cbfbc8652486d900b5aea.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/6c34c679014cee805599114b4aecfc4aff397565cbe8384d87a2d1090b5022d8.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/6df9dd44cc4748674a517002f5060c07a5bdcbd14563cc7091bd7a5a37c2dc30.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/6f66b229b6c222f9dfda0a3edf756e1883a3716699e3443cf6844e2e4371bc09.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/709dd337510602e3fe6b2c52d6942aff32fc237bdc00dc572a218b69df8c13ec.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/73f9d9ef43c06e33b886f1f20b3758b99298777d20ec670720efcd14b8216869.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/75cc73dd944f09f3c9a9147e69a80dc3cba9fac598b8d193296e7d5c03edf5ef.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/75ea239c34add68907f827eb4c66dcd5686c69a637331b0598e5a60e61eed1c0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/76d400191679c111d837f58417f77bae321221e2d74c3e7839f9ad8d05017208.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/7ba2172f10d03173f05c43f587d12923daafc57950d54a2fe494621d88ce5339.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/7bc52862da7a6d75f652cfbb5189b982ba291fb6d4a478a7de395f94a8063e2a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/7d8401db45dc73a120f7bd9a186ee82e01f41a9d1e191dde8f2a358d2ae84fe9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/7e84c820d3e390bafdd19ffdd3344ff5c3b70071029c05255094ba5993fe0f09.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/7eef265381bc999cc3067359198873cb54f9290a0faa07a2d8055c07b27e1f39.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/80e8cc0a77c37b8d645b053cdd13bcf0e7eeb52d4d9545204e3a29076e261e7d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/81be29700d7bf6c3dfdb45673cf5eb76123ef3891fb4a9fcd01c60597835954f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/821bd5ded4160e050f880b3bef25abe7661dbd0ec32bd56cd81cbfc181900645.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/856a38fed2b3b15adecfa265771afbcbe99520eecb51c74c5caaa8bb2bcf7411.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/86825ee1414b5a9b3bb66a6abbc6cc91af46748b7a0f538ce88cafd9b2a1dfdc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/86ca4fe604c844cf3dbb23cfbcb1399117f10c9d0cd57913752b3895fda5c69c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/879cf5a7275e4f9d712995477468158ccf0de50c6be094a057041d794ea48999.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/8cae5370d281c626e1696f173fce7e0ff971f234e33c397db2cd92ab47025f22.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/8f650ed3f3b28ddaedecaff4f7c09824b97a1b6948b70dce3adaf81afdf301fa.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/911d887d784f6551d15942f0261094a576141cda0c0bff505eccd5baca6c3d30.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9324f824a43e6d276572a2933b91659940c82e9bb9fa44a4be78f6edf4aa0556.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/932e61d2cfba57b43d8aee423bf0949585e464c15eac78429b9592a5925a83ba.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/94e6de34eb95c8c646e0e9bce153f48443241acaa908fada1a75124ac2c50d5e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9565dca4dad955b03a732757d1b2f853a713c84c3fdafa333422d52e75ed360b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9573f100d41187a753f6acbc0218efa6f54012d2d6843e1ceff1607d6aac8d11.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/95b9b2b1f391d7125f51ef63907de7d209bfd6d0185df6984f7578d5929af1b0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/98d364e94ceac96152614f37d3980983221bc975546b7872312f32dc8b32df30.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/999cc8f6e72c34eb4337ef3f5ba3e3d48d7c81c8e0568345b0e9353365feef8b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9a3ef0d7fa24d12d3578ff37487868444efafc1d65dbc9ae7a68bb20471fc393.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9add7c7852df8aa1607f9888be2aaacf89bd0cfecaddb4509ea2ba9c2408d6e1.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9bd8b6a2c019d56d490b176841ee8e1656709cd29159811dad5a91febf273f88.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9c56636d994795f6b2605d3f9e6759247b875ab301d992a6173bfafcf93fe95e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9d623702a79697aabe579cd5fcc89efcd0c37fea1ff989d551de4b9fdb560b78.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/9e394eb08986a678d53b329dc13f5e8a4e40ac6651c717df12035824b9de1003.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/a03b35a3327ecff6dbfb9cb3c4b7d48587f241e70969dd4dd21ed7cdfc0385b6.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/a3cfdf7d10c24cd7dd1a346df7663680c14580127483ab292d0a5fa766dd321d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/a6d380376eb6a5d990b6fb88c16b2599e05ee81049b091e0256f1e779a421c89.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/a76f8e787acdf99669a896b01e3f35587ab86f6cc074f62ee39b3c95c0349954.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/a7ddaac9b0a34fa9329ff4fed3371ad2c3d4a7d96d856bea990e9ba7dd30ae6d.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/aa6a4af364d1b695c9fbe4ac1802e727c43a8ed2b422a10b0db90f6d3ee1b2a9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ac637ee5bb4ebea974cede38599cec5328e411d43aefc4d27f8bc34a48f396d1.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ac8c45271bf7d5a0b20c2b42a13cedf348b3b9e6e8c09b8cf37ff475478aff1f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/acd5d95d75910ac3abe643405a2546113abbe6d9a065d1230727414e370286dc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ad25a03262bb43880a28ac36c31c294d94fad2d6cfe27131852eeed10568ad88.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ae19edfbbe118da2152e7a56ce0e2c91f2d05f383c6f6214adec63519fa4e2dd.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/afabf56f12b6dacdd51d579fcb7bf0bdd206eaea12e0dc5cf75fcaa901c5b101.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b13b41aa1e5a9a2116c4c961d55aeb0b54d3769221c019f287fc0e86de4af59e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b1aadd18a918dd866f515a77483b9e96c8352d2ed2f4daa93c2c89e206ccb20b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b209dc0774a17a95c37b83ef18a6a2bf51237f146cd9135ba10fc3d039c342eb.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b2d2c235b19446669f70359c303d644b07772cbc68951487b045668bf835ab9e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b3304a2b3d21485f92d43bd9166f39eca70bb3b48039c04e6e0d83f7f8901b12.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b39f1f41c5406fee5bf3463c1f48ad8e485e3ba850b015f590017e2fb81e372f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b4ceab86c4d3d2ad4cad63e3f49eab107cf266d9bf5bffc86aee6508cc2376cd.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b7ec0f92b73a80c9412993fd37a2832b3ab3664187a27a7e40f3769be9bb4c33.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b7ed443212fbdb5c9ecea51b77b46d990e7404de0cdb01d93f00b16d705d1bc1.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/b96cab186ad7c7411051e541e99be78799905bd34e63cf6a15a2bcc1dc14c428.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ba2f694ff92d9ec6fc0a7f39b49a30c60b70e132e2d593db6a9600b25f346638.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bac5f5ff7f4b4810f432ac131feba4520fc9e5cbfdb3ad325daada54093516bb.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bc08f951f2912de840ff463f3db9549cb971f68ba22c5b1eea5c18bd721c83a9.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bc9ac1b244a6f3706042bf37562d6c079d7d07b7e3ac3b361f54e9b0e2ccc57a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bcb56ed410c6543abdbef7a85d77aba64dc91f4d5a6f2bfcf9e310017b5e8178.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bd8c040cee65f3f9773753c49e092bbd9ff577759e875b4405a62d051cb8f7bf.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/bdfc692246dde8537f2741d657c7a1013725d51c1321a6788bdfba912dc007d4.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c07a718d29d7ca386588bf17fc8f3e5d98b985ce569c7395988631b998b5f420.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c0b3178b84946b4f2f034c0ce5e9198eb00baefa34fd876a4c89e84bd59ccb89.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c212cb345fd485b1f54816fe5d3635cd2d1b57240fdbde27cf1d9f630b7f0eaa.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c26c597603428254b1097a3f5ce93329701099f1d6e27a44487bd23f5b2f8026.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c312c0b37615de6a071ca36ac2fd67c1dd79312ecc8b72e3454bd1bc8b783651.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c3f6a86316b784fce9356eaf7cea8c7b6303124b553d6f1419b917c8e3e7d7b8.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c73ef879ff774b76ceca9f5c841f87c85c3290fd49d2431aa3a6a78bec898f00.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c75c38ca0cfc411d983a20b3b45d3cd1b401f6af598eaed1d5c80bb80832c943.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/c8d1cdeac768bb238b7763be525046599fcbe19403e60871a9ea7b0dd538fb4c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ca8d99be165879bb1277ab63514cd54922f8fee7e5ff7905411335574e46adb0.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/cab69946e0cae813bf757c69c0893ca51d6eb1e31dc589d2203ab07f9869042b.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/cc5d048bd3af708e3643abc7ed301ebb02e3e38bd2d098a9bc313590a1e69903.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/cd5bbc81bcbec9f089a117f5cae5d590d147fcb1f1824ec3bdd6f71cc9dbda37.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/cfc4e70f371b019a4d2b1467c0149f47e44d83e68a42f25feb7df345cce33274.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/cfdf055a103081b501ea9375814b3b572bc9fa6bb407a6fe723f07bbd79d5b32.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/d0b44ac7fb7446c070b257634f651ae177e73454af957a7691a9f975226c3c75.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/d3b69f817127fd89496ba7626dde1e3c49e4b74f3b15a1e3d2e8a6cccedd9788.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/d97f73675dfe4ff709820d1c559c9df31fe528896166ed3e9818aaa08c4da6fa.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/d9fe6a0d92fdcd1998fcf9981938759337017fc21848897d00fe0a3dc7395890.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e22128367932942d22a016ccb58c87128dd7cffb53521764b2334504e79ea0a3.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e2ecd747d61546bf8276ea76dcbc2cb590430f9eef384c71519e4c0651376272.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e72d1acf4c2c010f3f4c549c7b043363dc6073269a0cba83f4482da259172399.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e84dae2e32c9522590e42c2cef2f850918a975f2b342c5433045af6f5afcf24c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e8e7ff9f4e43d1f90324b041d38d84ac474be144dc05860b04a0128ae530b026.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/e9fbd1c24ca641944b584749e557f67900812222f275d2a2185063852aeafdaf.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ea4496c232b00caf7dbf51094fa10b5eff9a8edf3ab8754e38b1b378d5200571.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f18308406331cf6fa66164d26a15dff02efb9f9f759fceee83684888eca71155.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f4c1d323e5753e113cb1a88362bf262735caea0bb2d6aac94d2fbe82fe05c709.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f69ea0ec041dfdedc3ae938f794de498d0be05ec57c3dce63d459bcf1dca8568.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f7af2d4465398c9b163348f5e9f33fbb7ac72250b561e04c2f3dc905b282ff35.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f868e6c8ef374e807673d537e9d42143bf9c55a4bfe27416b647dc563ad0a645.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/f9f6bc84353e5573a4308f11dd5fc5c4ad7c0f23fae91d472b3984ff503e56a7.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/fb3007a63b2e685c6ba8921c65cb7c4f1d53365a28b26e5e68a8ba30cd4fea8c.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/fb557cb7843cdcc3eaefffd268db2a5b106895933ede0247101e504516cf3931.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/fc63ea1ed84f9e61f2ad0fc96ce33bdcff5779a9c0e38fa7c73d02f6a829cefc.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/fd129e22be5cd4e660d9402104d3ab0bc93325baad0a69b7eb99c985a934e956.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/fef79833c51085fdab835af3dcd172579586a1e1a6dd3ad5d11ee7f5e260c63e.gz', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/archive/ffac38409d08fc07c1fc4e16ea4bfe40006f7e62d4d00d048fd85f0d96635670.gz', 'docs/DRIVEN_LOCAL_CLOCK_PAULI_READERS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-local-clock-driven-readers-20261015/INPUT_MANIFEST.json')
EXPECTED_PROOFS={
 'local_clock_physical_reader_candidate/DERIVATION.md':'e22128367932942d22a016ccb58c87128dd7cffb53521764b2334504e79ea0a3',
 'local_clock_old_transit_reader_candidate/DERIVATION.md':'75cc73dd944f09f3c9a9147e69a80dc3cba9fac598b8d193296e7d5c03edf5ef',
 'local_clock_boundary_reader_domain_revision/AFTER.md':'9d623702a79697aabe579cd5fcc89efcd0c37fea1ff989d551de4b9fdb560b78',
}
EXPECTED_ACCEPTANCES={
 'local_clock_physical_reader_root_review/ACCEPTANCE.md':'406dee0a10515f717b2f5741f926714621a79b3ebc5881b6fd19cb6401b506ee',
 'local_clock_old_transit_reader_root_review/ACCEPTANCE.md':'5ba2f6941dc6310054b4d7c99247ff65c94dbedf950e3128c563f12d5e433b6b',
 'local_clock_boundary_reader_root_review/ACCEPTANCE.md':'5c671d4ee02e48ffb57976a83f4c1cec57f3635fcb793182e181f1f3cc9bc8f0',
}
EXPECTED_PARENTS={
 'premises/root_window.md':'fc63ea1ed84f9e61f2ad0fc96ce33bdcff5779a9c0e38fa7c73d02f6a829cefc',
 'premises/independent_window.md':'101d7778f3aaecbdb2db277c2d9857eee53cc7fae93941e444fe03d939ff36e9',
 'premises/boundary_window.md':'b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1',
 'premises/root_word.md':'de69e1821cb31a38e71998f116c881c177d498e6e8f373f62d4d2e31c68fb2dd',
 'premises/independent_word.md':'6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a',
 'premises/root_cell.md':'ca1cd46526063dab73e3d82afb99bce6bef1a903174f46134ceeeb854106d8d6',
 'premises/independent_cell.md':'43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5',
}

EXPECTED_CANONICAL = {'docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md': 'bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a',
 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md': '6a0274bd8a5fd7e2367268d973e7ac50ba38b9e12d3cbfbc8652486d900b5aea',
 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md': '1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256'}
EXPECTED_CLAUSES = {'premises/root_window.md': ('docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                             18674,
                             33077,
                             'fc63ea1ed84f9e61f2ad0fc96ce33bdcff5779a9c0e38fa7c73d02f6a829cefc'),
 'premises/independent_window.md': ('docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                                    33181,
                                    62080,
                                    '101d7778f3aaecbdb2db277c2d9857eee53cc7fae93941e444fe03d939ff36e9'),
 'premises/boundary_window.md': ('docs/FINITE_LOCAL_CLOCK_WORD_WINDOWS_BOUNDED_THEOREM_NOTE_2026-10-15.md',
                                 62134,
                                 80595,
                                 'b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1'),
 'premises/root_word.md': ('docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md',
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

def digest(raw):return hashlib.sha256(raw).hexdigest()

def checked_groups(index,originals):
    groups=index['source_groups'];assert len(groups)==17
    for group in groups:
        aliases=group['aliases'];prefix=group['group']+'/'
        assert len(aliases)==len(set(aliases))==group['complete_file_count']
        assert set(aliases)=={a for a in originals if a.startswith(prefix)}
        if 'seal_alias' not in group:continue
        raw=originals[group['seal_alias']];assert digest(raw)==group['seal_sha256']
        seal=json.loads(raw);seen=set();origin=Path(group['origin'])
        for row in seal['members']:
            path=Path(row['path'])
            if path.is_absolute():
                assert path.is_relative_to(origin);path=path.relative_to(origin)
            assert '..' not in path.parts and str(path) not in seen
            seen.add(str(path));b=originals[prefix+str(path)]
            assert len(b)==row['bytes'] and digest(b)==row['sha256']
        assert {prefix+p for p in seen}|{group['seal_alias']}==set(aliases)

def checked_inputs():
    raw=(REPO/MANIFEST_PATH).read_bytes();assert digest(raw)==MANIFEST_SHA, 'input manifest identity'
    manifest=json.loads(raw);assert manifest['schema']=='driven-clock-readers-inputs-v1'
    members=manifest['members']
    assert len(AUDIT_INPUT_PATHS)==len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS)==set(members)|{MANIFEST_PATH}, 'declared input coverage'
    data={}
    for path,row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b=(REPO/path).read_bytes();assert len(b)==row['bytes'] and digest(b)==row['sha256'],path
        data[path]=b
    index=json.loads(data[PACKET+'/SOURCE_INDEX.json']);assert index['schema']=='driven-clock-readers-archive-v1'
    originals={};objects=set()
    for alias,row in index['originals'].items():
        assert row['stored_path']==PACKET+'/archive/'+row['sha256']+'.gz'
        objects.add(row['stored_path']);b=gzip.decompress(data[row['stored_path']])
        assert len(b)==row['bytes'] and digest(b)==row['sha256'],alias
        originals[alias]=b
    assert len(originals)==351 and len(objects)==195
    assert objects=={p for p in members if p.startswith(PACKET+'/archive/')}
    checked_groups(index,originals)
    mapping=json.loads(data[PACKET+'/BODY_MAP.json'])['complete_proofs']
    assert len(mapping)==3 and {r['alias']:r['sha256'] for r in mapping}==EXPECTED_PROOFS
    for row in mapping:
        b=originals[row['alias']];assert digest(b)==row['sha256']
        assert row['end']-row['start']==row['bytes']==len(b)
        assert data[NOTE][row['start']:row['end']]==b and data[NOTE].count(b)==1, 'complete proof interval'
    assert mapping[-1]['end']==len(data[NOTE])
    binding=json.loads(data[PACKET+'/BINDING.json'])
    assert binding['publication_binding_complete'] is True
    assert binding['binding_complete'] is True and binding['stage']=='root_bound_review_milestone'
    assert not binding['root_runtime_freshness_and_feature_binding_pending']
    assert binding['observed_base_head']==binding['feature_head']==binding['source_head']=='f79cf5d36e69b78d3dcc878e2d249ad597155d1c'
    assert binding['observed_base_tree']=='85b386b89e07473d55096c70b0eb9e15e81d94f5'
    assert binding['base_pr']==9593 and binding['base_branch']=='physics-loop/toe-local-clock-windows-20261015'
    assert binding['branch']=='physics-loop/toe-local-driven-readers-20261015'
    assert binding['publication_pr'] is None  # Dated source build, not a live reader-PR assertion.
    assert binding['ancestry_alone_supplies_mathematical_premise'] is False
    assert binding['optional_four_rail_word_instance_adopted'] is False
    assert binding['new_scientific_programs_run']==0
    assert (binding['archived_selected_fixtures'],binding['archived_scientific_attempts'],
            binding['archived_successful_attempts'],binding['archived_failed_attempts'],
            binding['archived_root_metadata_attempts'],binding['archived_failed_root_metadata_attempts'])==(3,3,3,0,6,1)
    assert set(binding['canonical_sources'])==set(EXPECTED_CANONICAL)
    for p,h in EXPECTED_CANONICAL.items():
        assert digest(data[p])==h and originals['canonical/'+p]==data[p]
        assert binding['canonical_sources'][p]=={'bytes':len(data[p]),'sha256':h}
    deps=json.loads(data[PACKET+'/DEPENDENCIES.json'])
    assert deps['publication_binding']=={'binding_complete':True,'base_branch':binding['base_branch'],
        'base_head':binding['observed_base_head'],'base_tree':binding['observed_base_tree'],
        'base_pr':binding['base_pr'],'feature_head':binding['feature_head'],'publication_pr':None}
    assert deps['publication_binding_complete'] is True and deps['canonical_parent_binding_complete'] is True
    assert deps['reader_publication_binding_complete'] is False
    assert set(deps['intended_canonical_targets'])==set(EXPECTED_CANONICAL)
    assert deps['expected_after_root_integration']=={'new_nodes':1,'new_edges':3}
    assert deps['context_only_clause']=='premises/independent_window.md'
    root_review=json.loads(data[PACKET+'/ROOT_SOURCE_REVIEW.json'])
    assert root_review['completed'] is True and root_review['scientific_programs_run']==0
    assert binding['conditional_acceptances']==EXPECTED_ACCEPTANCES
    for alias,h in {**EXPECTED_PARENTS,**EXPECTED_ACCEPTANCES}.items():assert digest(originals[alias])==h
    clauses=binding['parent_clauses'];assert len(clauses)==7 and clauses==binding['exact_source_clauses']
    assert {r['alias']:r['sha256'] for r in clauses}==EXPECTED_PARENTS
    for row in clauses:
        b=originals[row['alias']]
        assert (row['canonical_path'],row['start'],row['end'],row['sha256'])==EXPECTED_CLAUSES[row['alias']]
        parent=data[row['canonical_path']]
        assert row['canonical_sha256']==EXPECTED_CANONICAL[row['canonical_path']]
        assert digest(parent)==row['canonical_sha256'] and parent[row['start']:row['end']]==b and parent.count(b)==1
        assert len(b)==row['bytes']
    checked_window_publication(originals,binding)
    return data,originals

def checked_window_publication(originals,binding):
    raw=originals['actual_window/PUBLICATION.json']
    assert digest(raw)=='fef79833c51085fdab835af3dcd172579586a1e1a6dd3ad5d11ee7f5e260c63e'
    pub=json.loads(raw);commitraw=originals['actual_window/COMMIT.json'];commit=json.loads(commitraw)
    assert digest(commitraw)==pub['commit']['sha256']=='c212cb345fd485b1f54816fe5d3635cd2d1b57240fdbde27cf1d9f630b7f0eaa'
    assert pub['number']==9593 and pub['state']=='OPEN' and pub['isDraft'] is False
    assert pub['headRefOid']==commit['head']=='f79cf5d36e69b78d3dcc878e2d249ad597155d1c'
    assert pub['tree']==commit['tree']=='85b386b89e07473d55096c70b0eb9e15e81d94f5'
    assert binding['windows_canonical_sha256']==pub['source_note']['sha256']=='bcefbb192900b56ee937255d54d78a2aba777c1120416addc5b040147d06700a'
    assert binding['windows_publication']==pub
    assert binding['windows_canonical_intervals']=={r['alias']:[r['start'],r['end']] for r in binding['parent_clauses'] if '/root_window.' in r['alias'] or '/independent_window.' in r['alias'] or '/boundary_window.' in r['alias']}
    prefix='actual_window/verify_pr/';receipt=json.loads(originals[prefix+'EXECUTION.json'])
    assert receipt['exit_code']==0 and receipt['python_source_at_launch'] is None
    for stream in ['stdout','stderr']:
        b=originals[prefix+stream];assert len(b)==receipt[stream]['bytes'] and digest(b)==receipt[stream]['sha256']
    for key,value in json.loads(originals[prefix+'stdout']).items():assert pub[key]==value
    recorder=originals['actual_window/recorder.py']
    assert len(recorder)==receipt['recorder']['bytes'] and digest(recorder)==receipt['recorder']['sha256']

def checked_revision(originals):
    prefix='local_clock_boundary_reader_domain_revision/'
    before=originals[prefix+'BEFORE.md'];after=originals[prefix+'AFTER.md']
    assert before==originals['local_clock_boundary_reader_candidate/DERIVATION.md']
    edits=json.loads(originals[prefix+'EDIT_MAP.json'])['edits'];assert len(edits)==2
    reconstructed=after
    for row in reversed(edits):
        old=row['old'].encode();new=row['new'].encode()
        a,b=row['after_range'];c,d=row['before_range']
        assert after[a:b]==new and before[c:d]==old and reconstructed.count(new)==1
        reconstructed=reconstructed.replace(new,old,1)
    assert reconstructed==before
    patch=originals[prefix+'CHANGE.diff'].decode();heads=patch.splitlines()
    expected=''.join(difflib.unified_diff(before.decode().splitlines(True),after.decode().splitlines(True),
        fromfile=heads[0][4:],tofile=heads[1][4:]))
    assert expected==patch

def checked_receipts(data,originals):
    archive=json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])
    science=archive['scientific_attempts'];assert len(science)==3
    assert {r['id'] for r in science}=={'original_full_norm','old_transit_residual','central_commutator'}
    for row in science:
        receipt=json.loads(originals[row['receipt_alias']])
        assert receipt[row['exit_key']]==row['expected_exit_code']==0
        pre=json.loads(originals[row['preseal_alias']])
        pretime=pre['sealed_utc'] if row['id']=='central_commutator' else pre['utc']
        assert datetime.fromisoformat(pretime)<datetime.fromisoformat(receipt[row['start_key']]), 'historical preseal chronology'
        assert datetime.fromisoformat(receipt[row['start_key']])<=datetime.fromisoformat(receipt[row['end_key']])
        for stream in ['stdout','stderr']:
            b=originals[row[stream+'_alias']]
            expected=receipt[stream] if isinstance(receipt.get(stream),dict) else {
                'bytes':receipt[stream+'_bytes'],'sha256':receipt[stream+'_sha256']}
            assert len(b)==expected['bytes'] and digest(b)==expected['sha256'], 'recorded stream: '+row['id']
        for member in pre['members']:
            path=member['path']
            if row['id']=='original_full_norm' and path=='DERIVATION.md':
                path='history/DERIVATION.precontrol_51a74faa.md'
            b=originals[row['source_group']+'/'+path]
            assert len(b)==member['bytes'] and digest(b)==member['sha256']
    expected={'local_clock_physical_reader_root_sources':0,'local_clock_old_transit_reader_seal':0,
      'local_clock_old_transit_reader_root_sources':0,'boundary_reader_root_source_closure':2,
      'boundary_reader_root_source_closure_retry':0,'boundary_reader_root_seal':0}
    assert {r['label']:r['expected_exit_code'] for r in archive['root_metadata_attempts']}==expected
    for row in archive['root_metadata_attempts']:
        p=row['prefix'];receipt=json.loads(originals[p+'/EXECUTION.json'])
        assert receipt['exit_code']==row['expected_exit_code']
        for stream in ['stdout','stderr']:
            b=originals[p+'/'+stream];assert len(b)==receipt[stream]['bytes'] and digest(b)==receipt[stream]['sha256']
        launch=receipt.get('child_source_at_launch')
        if launch is None:
            assert row['label']=='boundary_reader_root_source_closure'
            assert row['child_source_at_launch_present'] is False and p+'/executed_source.py' not in originals
        else:
            b=originals[p+'/executed_source.py']
            assert row['child_source_at_launch_present'] is True
            assert len(b)==launch['bytes'] and digest(b)==launch['sha256']
    assert b"can't open file" in originals['actual_runs/boundary_reader_root_source_closure/stderr']
    return {'scientific_attempts':3,'failed_scientific_attempts':0,'root_metadata_attempts':6,
            'failed_root_metadata_attempts':1,'replayed':False}

def main():
    data,originals=checked_inputs();checked_revision(originals);receipts=checked_receipts(data,originals)
    print(json.dumps({'result':'analytic_source_binding_completed','complete_proofs':3,
      'decoded_originals':len(originals),'scientific_programs_run':0,'archived_receipts':receipts,
      'dated_canonical_source_binding_complete':True,
      'scope':'Bytes, complete intervals and historical stream provenance only; no mathematical predicate executed.',
      'limits':'All three canonical parents and actual feature/source binding are dated records. Later reader publication and retained audit are separate. Hashes do not establish proof or physical supply.'},sort_keys=True))
    print('per_element: arbitrary old/reference input with supplied joint entry and pointer preparation; full coherent output')
    print('per_site: dirty-clock transit pays full drift; occupied-old transit retains the old bond and pays its stated local comparison')
    print('per_mode: whole logical-head domain; two-cell quarter commutator bound restricted to one excitation')
    print('per_block: exact raw bodies, domain repair, scalar/work/precision costs and failed metadata attempts preserved')
    print('lattice_wide: conditional driven coherent readers; no native initialization, classical instrument, reset, stop or common cap')

if __name__=='__main__':main()

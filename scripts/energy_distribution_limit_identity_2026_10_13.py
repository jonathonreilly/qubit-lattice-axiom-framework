#!/usr/bin/env python3
"""Source bytes and publication reconstruction only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import difflib
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-energy-observables-20261013/ENERGY_OBSERVABLES_SOURCE_ROOT_REVIEW.json', '.claude/science/physics-loops/toe-energy-observables-20261013/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-energy-observables-20261013/PARENT_BINDINGS.json', '.claude/science/physics-loops/toe-energy-observables-20261013/PUBLICATION_EDITS.json', '.claude/science/physics-loops/toe-energy-observables-20261013/SOURCE_REVIEW_STATUS.json', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/0420757086df43de2f3b9257ba20e7ac89eff8d087f356f3fbbf0eb56e139a1a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/048cc7f0852792dace24a11ad004848db063bd330793c6210de431ee930af503.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/05674ec1d3f0db95940085ccf3c5bc1339963211c9ff7a581f141f10999119f7.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/06b6b51eb4e0bc1b9165e403ac15a8513666a85626e32ef3a0a23dd4d7402e9a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/075ec5cd8d51bb61662270a6dc6118451a0c68a0256cf84b81c038c33fef11b1.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/08558443feae581617f6e35f0db346e4d282440141963573a19d436595d0e2f4.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/096542d72cd80cf834ecd0c8e5f2c7a31d6543c1ba3a4988e45baed22da33334.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/0d0db3e7dfd45bc1a17738812d12cc977ce57ef4e3ebf4325294addf7e433c89.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/0e63df95824fa167961b3395d38afef2c044721762fc0c41328b433634c67700.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1136039ff011a4af20a092ee18d56ad069274d10330b1adb0914192aa7f4a217.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1166b2a8ffe6a5b1ec8928689c003e0bfcb26bc68914af9f740eb1eded1d85eb.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/125278cf84521e074af7d40d86e10c52122ba30148a456ddc1cffe78e232a6af.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/129a1af703261521627e56786fa2bed2a31d494940a13a8d29dd672a1c63f472.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/12d9aa4e7acd40c2a62fa5b7595234f6221b726078051c818869538acd28a64c.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1398b67f4bde2fea0aa9efffcd3048d48de4e5d3fae2a139e3337824c6f0f320.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/147b8760324f8e37316008ac50d16e02231b1494a58b842d230d2e1d3e991575.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/165807c4801e05a6689b0dfe3579da1705ff93199d13cdcc2a8ff7dcf79384bb.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/18c4c80868a4aac146056baae6463eb2b689ee003543cb2cf26ab492a7e077d8.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1993b2db639299a130eeb3f826aeead0e071f22d0d517525a9cd2e5f30e1b26d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1c23a9e40e47473c654bc8c6ae1d0640f9c4b42dea0a7ae333d2f1f88e51ed40.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/1fc4a374f6903dfe183747196ae57f6271ae0ed43b4e8eb61e834b69a2a2bb9e.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/202b44242e9f9b1d8ba8e93302745e3c91425aa4a63b6b599850cb8f12de02e7.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/22764dc3cf673d95687fa94149b6164b86176a74a239b203f829312d8fff0f9a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/246871668fdf16ddc20743b35996e30fed74186c99ccd824b3ff56ed57b8df91.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/2660070967ab853c52b289c39170b0b72e8fe5fdd20b7315ab95ccad5c2ce1f3.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/29b3f3f6c7758d13d2ea78f5a20b42111a5b02450f3cfdc2d94b4fdda065c498.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/32032fe99b58d0a2b5e32608c3c2da2ab717a18590f99317fc80136da2ae31e3.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/3990bc92fae264e9c9f05fc2d8fcd847cd1e69bbe2ad478013459c1ab0e7a256.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/3dedafcd12dd970a010d42bd4b9617131314f6a7c33c082e4c670c66fd1d10c5.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/3ed69527ba6177ae17a66eeabe45f98591cf60a1d2f9367bfacd95306fca52f6.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/40a12aa86e18ee306421479f7d95d7602c5c9e4ec2810800fb7468f6b358128a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/41f79f0e42eccf94e88276be41f8d4576d0021b6ca2526fc72aead067395b38a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/4a33689a79b849c3463ba037565eca4ad919d53de0de5a781b150ef81ec889e3.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/4ab02757ff0be403b15d41779a04ca596436bc62240dbc027c01ac6d0fb78abc.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/4b9dab8d630df01804d2ef5f46a9a71f0d5d5816bfcff4d7338220ea1320ee0e.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/4bc270271b2f44ae2c98c21c935d53e608f4f1960463b892bde873705d6cf1df.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/4c6451db5b1cbed0009fb97a54041f34a7ff74ddbf3ca857c9a15fafb988e289.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/512f8ac3d95ea5f10d72540293ef93b49bb7dd4a4dbf57f1e403b616eba69080.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/52784539b9d0bd1939fba0e1be73a6f3f94e318a18a166cde29914b6463a4340.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/527ab5c136280ea960ab70a0d42d8e2c09bdd14e979ed7925b371fbd269b236d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/54214592e23043564b8e974714c6ef5764956f52899910824561a6f890b69ee3.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/54d600e491a46d3c84d9d4b3ae849d4d3019f18f5aa6e0736f3f1b606c9fdd62.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/5874a93f5ef924da7cbbf1e4d530ecbb5839e99938e0111ab4170d6b8ff1cbfe.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/588ccb434d6d4548922ebb5d541000d3d41b07e4de809ef84de5d4084d91cc85.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/58df7324e19e4782c828afe714299859a3d575980de91d51ece243989c159d0f.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/595d7af374c3e939f8d22522dc93f5fe59ab32978baa46ba64694a538f4bb9c1.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/5b4792f65f9cf19d902df17dd85f6c91434dec028701d6e5f65c77b2169ff26d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/5dae9f6a83557c316f0a02f73316744d853812a493e0144381086f9bf4c54d40.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/5e1e1f4965ad9721707270783de3574aa8bea2df66adeb8e58c9dbbd4aa10e07.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/602a583852990b5c8fbe8ef2ff4e8c9c80e935499f1e4731e169a7d4e9a0e917.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/62d98c8f61c8bb842daa3713e6fc46b08c795224073656295d517e7aa280a004.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/636d28b935346b1a767d0bbad6d8ec8caa37da0df7f12375798a0a73f96c2f20.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/6464ce56d8f7c6af182c24685b6d92f87e67abd1ddd9e6a4d5ee0eaf53f5d875.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/658b8aeadbd3d95075d4d942c1b6222c6380c6a8c2e9abc00e1387693f34aaf5.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7217a6628f47ed88577e4ff10a339a182835afac425e9f652347d19861686214.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/74315532c46b677f6f523b51577394daeae2eca78a98ffe0a30d74564ce18313.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/750186f9ce90d80502e5d39f9ce0fcbb3243e701f42a591bf80d2cdfb1ed5b1b.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/75df75413051189ee94a789a90188ad64033e0d44fcaf67f65501891382d1a2d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7658851f3f992225a98b5704e6e32628ec42f2b73f6f54e2d553bdfaa42eda8b.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/76aaecd7684249490c7cd95d482f2de75d3c75f471be873307e1f04e7ca7fc39.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/772907d024e96aa5c05b479a9d7dad1bc92c68aea597193055473a1d4a9548ff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7c9df64640d1296f2dc8a6d1a522652d0f766fdad769b14ec303f38dd8b6ff23.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7d4bc5d6ca3cc4fb64ba1951c089d8d1089f3459da3120eb274cb1b093f35fe5.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7daecafbb4dbd6aa20cc416375097bc08bb2829ddd145af5650584decd6e9afa.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7efcf29c90f47284d9a419349a31d1d03b851c0d951b16567bb5afc97a74a008.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7f4c5f6f773ba514de21da4b77634683f889ec77fde4dcb99081b330dce8fb80.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/7fbe15c5037fe15a79d84ded88217812683f6fc787b1da66f861b7e6a3a38eef.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/81fc601dcbf8ac40c4200f3d8e559fa0d078cc884c8648b079e20239c0912868.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/824088f6719c740b3c2b51afe4fc99cd4375f5154adfe3cbc4ace3f873f6de3c.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/8661801ccfb0652b3a00ba502fd35d6bc3ea9a1efae76559654416640bebfd86.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/8af0516189dd9b6fe4c374af0272942dfd0fc2875aa61205a87d898153ba8337.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/8b20782b2a60d49283c88808a3afd1dc5368767821a420684bd53817ac1d3fee.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/8d91ac2fb0401ca647bb84e224f91d36a8085b42a00d8be689d3d9f1b5aeb8bf.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/913a942db4f126628b2314e3222cc21f1a7efd08aeea224c720ee9df8c7da040.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/92a80fb57297812f544adef693caa19a8c28c3d6e008b7093af82526301cba86.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/945353398d26fdbb34aba5e60a372143eab0271fd7c792508ab4e28cec586774.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/94d6cae80356b347201074fdd0abb016b75e6b2ef4c52944ec2a01170f8f4e2f.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/9b8bb0b657386dffd6f2290d17c2f5a8da299238087a317e2edd7235516a9b63.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/9e3d831ba8c62a7e8625b20cd000b153c970bbaf4cd9f08676465054b3500cc5.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/9ef7886a37cdbaf76e46cc478cc5bf734ec7b6d28908a184c490e74e82a90d70.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/a1d672c50f5db0a91c358a41e4237a72351968d784356ab67b23d9d7ca3a2630.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/a341d29062a1f2f35fab9773972b1da122739466eb252caf400efe34d9eb599d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/a5f27437088f436a487028eb26e6d2d3118a9bfb102469b90b8596fce1eb252a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/a8a762ee57d703b0661b032e2510a6b6a2209185d159b0dbfec9a79ec67df78d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/a93c916148a2132dbca9025b318985e40381611b77eed8c905306c5ff2884350.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/aa3a814af1ee3294121f1a54b7d3c4e32f2d12ea08d8099f637d2c9a38296aeb.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/b2ebf1fb37862f24267dd1362ccd17b8a905b88413517f302efc2f03a3636ac4.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/b3b15bd16564603a9e10ce64dd5f96ed2e4a61e168b544edd01760f77a5abbc7.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/b587a19aa917d4700df9045c31c09ebbab83bd6f0a5947d0fc763babf8f99e31.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/b6c3834c2699809887e78fcd5c06409b12f5417db91e6b4156ba212d85abc8fa.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/b8f43c47e04fa47cc3a3c24a2c9642fc55d862d8da240e81ff129e527010830f.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/ba69194ef95c6934ac919a637a8e50997ee822652194a3fd774387f16923a0d3.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/bae356ec9593daf5ad1466bdfcfbcf68ae49a5b94f29eed2a635343fd5679a59.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/bb1de10d6d5652b7c4e59c8695ad76890b9d9d4c4d183a66b26fe60c72b6aef1.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/bd3f3e9e05b8f164ce33cdc0b242ce4e02b251efcb607990a1bbd4e293dcf72e.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c1db78a14a39083c29c44b94175e31e30612d668e5cbe4e1eccd4cac4f33f725.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c27cd2b0854d7b00b03e25afac145a71188fab22d0828560a75bf9c38718c100.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c35fedfbfc7beb6ae52151ff653a3a60fa9471989e00ad812759f688cb736380.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c4f43a9a7afb6cb9634aa89a49102fc1a478418b49d4974c44a9664bbcfa5f17.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c5a2eb448ead6ed7614148e601e0d434fd4ad141d14adeacc5dfdfb23e31262a.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/c92f863202d41a6e6fca83317e5e131f7f5316f21bc51599bbefab1e8c64a00c.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/d0741af5bdf39c8d76f63126217ea5f0ff16438f97bd90918ed654420d73567e.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/db26f9e0b70c28e7f4dbe2e5c35675522978386ccbf6f25c424e75e9a9942ec4.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/de896ce3b757cbd2365a9c1fdeacc76f47396e400b9a74d7379b2d145f8edf12.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e02e08d2fa0dd22663b3e94de91e36db16f0d5f13ba38dd02324e6b486604456.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e0d5a5e0eec454620bf702697156c8c708beee890e23304b272aeca6ccd937c4.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e0d9504585006de2d95126521cb1374df7765786a321aea7ac9b434f6762ff15.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e141f1e354763779f862c664843bbc1adacfaa4868861db59de38b31fc7900d5.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e6319e14fe1ecddd10784ebee64c8b8ef9f6b71ce3d561639e2cd49a9e063bc8.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e63f2b0e34d2465a0207d50cf300b20c8aaf75a7173a9d914982625b7c49e44e.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/e83e49571b92de2330f6bb391132699f584b6c78e7a40adf59a0389717cf4d70.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/eadfa1e1d9b8dc462273059fc00289a02bd2b8af998cd4cf415e1f492d75989c.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/ebbeb2c6fc021a5144508881fb7471cfddb3805441e1ea3fd9a26a55198eea97.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/ebf8d37b1466ff3a52af9a350a8c616f9de350e64a508f9dce541e8b2c2db864.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/edb856f0d09108b5d9630feff774705b0296106617c5218b75a7e1f6465add07.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/ee5dba9e02d68c2479da313741345d5eaf8d6b814ead5787ba306f0129211a49.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/eecc9f4f4cf9e946a0b814887f148d7e309ca6b7dfbeb92e6f4c7cb378e651aa.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/eef8bd18c3ad23b80f3b5bce9055464fe210b05f9ec20eb2bfa3312e02b2306c.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f0c0ca313f338a8ae1bdcaffd5a5db44bbdd651db1672fff7b0548aaf61bc582.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f22ad7e16fffce7252062e7a7c5da339a032d12dbc5997715c9cc4bd573cdd32.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f4bea91cac7b33cb702089ffb90765e8fe678e1315d9509f78d0eaaf76e095a7.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f59fd715c085af4e1419ab10120c33421f231f3cda462a22d0c847a72e2f9af1.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f5d2fb32a4a9fee8134e90f5391e5ce41009137e8b402f6593189a3dd3125fbc.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f5ec86825b5e772c31beec642d23731f7e0628b54abccda96b03cb809892755d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/f86f516d854dc324e31c1f7195c841c7c7020cc8044ff0e8b1374d008236e3c8.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/objects/fd617fb50c33edeae16ed3421bbf66ebcdf8be3f0bc8f3745c5379c5931a7b1d.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/distribution.complete-publication.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/distribution_appendix.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/distribution_header.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/weighted_appendix.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/weighted_current.complete-publication.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/weighted_current_between.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/weighted_header.diff.gz', '.claude/science/physics-loops/toe-energy-observables-20261013/publication_diffs/weighted_native_between.diff.gz', 'docs/ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BV_GRAPH_ENERGY_PROTOCOL_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/ENERGY_DISTRIBUTION_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/ENERGY_TRANSFER_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/ENERGY_WEIGHTED_CURRENT_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/PREPARED_DRIVEN_STATE_BOUNDED_THEOREM_NOTE_2026-10-13.md', 'docs/TIME_AVERAGED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-12.md']
PACKET = '.claude/science/physics-loops/toe-energy-observables-20261013'
CLAIM = 'energy_distribution_limit_bounded_theorem_note_2026-10-13'
MAP_SHA = 'add9f4baf970feb065e049239d8fc73fd39722aad3355324b9a5c9707cb64a75'
EDITS_SHA = 'b441e82a8f92ae4dac6fb95895b82d6a97f0d4d88b8f6cf7ad5417ff8c61c975'
PARENTS_SHA = 'd536141df755a815f4d88fa25bdc086f8df870fe5db15223580c878f1d31d7dc'
STATUS_SHA = '686876ade287626590e02dc1338c041878775a402e543320810db9f8ecebcb25'
SOURCE_FREEZE_SHA = '94d6cae80356b347201074fdd0abb016b75e6b2ef4c52944ec2a01170f8f4e2f'
ROOT_REVIEW_SHA = 'de896ce3b757cbd2365a9c1fdeacc76f47396e400b9a74d7379b2d145f8edf12'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def complete_diff(a, b, name_a, name_b):
    return ''.join(difflib.unified_diff(a.decode().splitlines(True), b.decode().splitlines(True),
        name_a, name_b, n=max(len(a.splitlines()), len(b.splitlines())))).encode()


def verify(root):
    reads = []
    def read(name):
        relative = PurePosixPath(name)
        need(not relative.is_absolute() and '..' not in relative.parts, 'Unsafe declared input')
        path = root.joinpath(*relative.parts)
        need(path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(root),
             'Declared input missing or outside repository')
        reads.append(name)
        return path.read_bytes()
    raw_map = read(PACKET + '/EVIDENCE_MAP.json')
    need(sha(raw_map) == MAP_SHA, 'Archive map changed')
    evidence = json.loads(raw_map)
    objects = evidence['objects']
    need(len({o['sha256'] for o in objects}) == len(objects) and
         len({o['path'] for o in objects}) == len(objects), 'Duplicate archive object')
    contents, origins = {}, {}
    for obj in objects:
        stored = read(PACKET + '/' + obj['path'])
        need(sha(stored) == obj['stored_sha256'] and len(stored) == obj['stored_bytes'], 'Compressed archive changed')
        data = gzip.decompress(stored)
        need(sha(data) == obj['sha256'] and len(data) == obj['bytes'], 'Archived source changed')
        contents[obj['sha256']] = data
        for origin in obj['origins']:
            need(origin['path'] not in origins, 'Duplicate original alias')
            origins[origin['path']] = obj['sha256']
    contract = evidence['accepted_source_package']
    prefix = contract['path'] + '/'
    need(contract['freeze_sha256'] == SOURCE_FREEZE_SHA and
         origins[prefix + 'SOURCE_FREEZE.json'] == SOURCE_FREEZE_SHA, 'Accepted source freeze differs')
    original_freeze = json.loads(contents[SOURCE_FREEZE_SHA])
    need(original_freeze['files'] == contract['members'] and
         original_freeze['file_count_excluding_self'] == 125 and
         len({r['path'] for r in contract['members']}) == len(contract['members']) == 125,
         'Original membership differs')
    expected_aliases = {prefix + r['path'] for r in contract['members']} | {prefix + 'SOURCE_FREEZE.json'}
    need({p for p in origins if p.startswith(prefix)} == expected_aliases, 'Source package aliases differ')
    for item in contract['members']:
        need(origins[prefix + item['path']] == item['sha256'] and
             len(contents[item['sha256']]) == item['bytes'], 'Source member identity differs')
    def archived(path):
        return contents[origins[path]]
    def source(name):
        return archived(prefix + name)
    manifest = json.loads(source('SCIENTIFIC_INPUT_MANIFEST.json'))
    sources = {s['name']: s for s in manifest['sources']}
    need(len(sources) == len(manifest['sources']) == 9, 'Scientific original membership differs')
    for item in sources.values():
        data = source(item['archive'])
        need(sha(data) == item['sha256'] and len(data) == item['bytes'], 'Original source archive differs')
    source_archive = json.loads(source('EVIDENCE_ARCHIVE_MANIFEST.json'))
    need(source_archive == evidence['source_archive_manifest'], 'Source archive metadata differs')
    for item in source_archive['metadata_originals'] + source_archive['procedural_templates']:
        data = source(item['archive'])
        need(sha(data) == item['sha256'] and len(data) == item['bytes'], 'Exact evidence archive differs')
    # Scoped projections are frozen members, not substitutes for excluded full
    # mixed-lane records. No read of their unarchived original paths occurs.
    body_edits = json.loads(source('AUTHORIZED_BODY_EDITS.json'))
    corrections = body_edits['edits']
    need(len(corrections) == len({e['id'] for e in corrections}) == 3, 'Accepted correction scope differs')
    body_manifest = json.loads(source('BODY_COPY_MANIFEST.json'))['bodies']
    corrected = {}
    for body in body_manifest:
        original = source(body['source_archive'])
        need(sha(original) == body['original_sha256'], 'Body original differs')
        revised = original
        for edit in [e for e in corrections if e['source'] == body['name']]:
            old, new = edit['old'].encode(), edit['new'].encode()
            need(original.count(old) == 1 and sha(original) == edit['original_sha256'] and
                 sha(old) == edit['old_sha256'] and sha(new) == edit['new_sha256'] and
                 sources[edit['authority']]['sha256'] == edit['authority_sha256'], 'Authorized wording differs')
            revised = revised.replace(old, new, 1)
        need(revised == source(body['body_copy']) and sha(revised) == body['transformed_sha256'] and
             len(revised) == body['transformed_bytes'], 'Accepted complete body differs')
        need(source(body['diff']) == complete_diff(original, revised, 'original/' + body['name'],
             body['body_copy']), 'Complete accepted body diff differs')
        corrected[prefix + body['body_copy']] = revised
    need(len(corrected) == len(body_manifest) == 4, 'Complete body membership differs')
    source_map = json.loads(source('LINE_PIECE_MAP.json'))
    need(len(source_map['notes']) == 2, 'Accepted candidate membership differs')
    for note in source_map['notes']:
        assembled = b''
        for piece in note['pieces']:
            if piece['kind'] == 'new scope/chronology wrapper':
                part = source(piece['source'])
            else:
                original = source(sources[piece['source']]['archive'])
                a, z = piece['source_byte_range']
                need(0 <= a <= z <= len(original), 'Original source range differs')
                part = original[a:z]
                if piece['kind'] != 'byte-identical original segment':
                    need(piece['kind'] == 'authorized wording replacement', 'Unknown accepted piece kind')
                    selected = [e for e in corrections if e['id'] == piece['authorized_edit_id']]
                    need(len(selected) == 1 and part == selected[0]['old'].encode(), 'Replacement piece differs')
                    part = selected[0]['new'].encode()
            first = assembled.count(b'\n') + 1
            end = (assembled + part).count(b'\n') + (0 if part.endswith(b'\n') else 1)
            need(piece['output_byte_range'] == [len(assembled), len(assembled) + len(part)] and
                 piece['output_line_range'] == [first, max(first, end)] and
                 sha(part) == piece['sha256'] and len(part) == piece['bytes'], 'Accepted piece boundary differs')
            assembled += part
        need(assembled == source(note['candidate_path']) and sha(assembled) == note['sha256'] and
             len(assembled) == note['bytes'], 'Accepted source-note reconstruction differs')
        baseline = b''.join(source(sources[n]['archive']) for n in note['source_body_order'])
        need(baseline == source(note['original_body_concatenation']) and source(note['complete_diff']) ==
             complete_diff(baseline, assembled, note['original_body_concatenation'], note['candidate_path']),
             'Complete accepted assembly diff differs')
    raw_edits = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(raw_edits) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(raw_edits)
    need(edits['source_freeze_sha256'] == SOURCE_FREEZE_SHA and edits['additional_mathematical_body_edits'] == [] and
         edits['source_stage_authorized_body_edits'] == body_edits and len(edits['notes']) == 2,
         'Publication scope differs')
    wrapper_contents = {}
    for note in edits['notes']:
        need(origins[note['accepted_candidate_path']] == note['accepted_candidate_sha256'] and
             note['additional_mathematical_body_edits'] == [], 'Accepted note or no-edit contract differs')
        assembled, bodies = b'', []
        for piece in note['pieces']:
            if piece['kind'] == 'accepted_corrected_body':
                need(piece['additional_mathematical_body_edits'] == [] and
                     piece['historical_status_and_exposure_bytes_preserved'] is True and
                     origins[piece['source_path']] == piece['source_sha256'], 'Body preservation differs')
                part = corrected[piece['source_path']]
                bodies.append(Path(piece['source_path']).name)
            else:
                need(piece['kind'] == 'publication_wrapper', 'Unknown publication piece')
                part = piece['text'].encode()
                need(piece['wrapper_path'] not in wrapper_contents, 'Duplicate wrapper')
                wrapper_contents[piece['wrapper_path']] = part
            need(len(assembled) == piece['byte_offset'] and len(part) == piece['bytes'] and sha(part) == piece['sha256'] and
                 assembled.count(b'\n') + 1 == piece['first_line'] and (assembled + part).count(b'\n') == piece['last_line'],
                 'Publication boundary differs')
            assembled += part
        accepted_note = next(n for n in source_map['notes'] if n['canonical_path'] == note['note'])
        need(bodies == accepted_note['source_body_order'], 'Complete body order differs')
        published = read(note['note'])
        need(published == assembled and len(published) == note['published_bytes'] and sha(published) == note['published_sha256'],
             'Published source does not reconstruct')
        stored_diff = read(PACKET + '/' + note['diff'])
        need(sha(stored_diff) == note['diff_stored_sha256'], 'Compressed publication diff changed')
        diff = gzip.decompress(stored_diff)
        need(sha(diff) == note['diff_sha256'] and diff == complete_diff(archived(note['accepted_candidate_path']),
             published, accepted_note['candidate_path'], note['note']), 'Complete publication diff differs')
    for wrapper in edits['wrapper_changes']:
        old, new = archived(wrapper['source']), wrapper_contents[wrapper['publication']]
        need(sha(old) == wrapper['source_sha256'] and sha(new) == wrapper['publication_sha256'], 'Wrapper identity differs')
        stored_diff = read(PACKET + '/' + wrapper['diff'])
        need(sha(stored_diff) == wrapper['diff_stored_sha256'], 'Compressed wrapper diff changed')
        diff = gzip.decompress(stored_diff)
        need(sha(diff) == wrapper['diff_sha256'] and diff == complete_diff(old, new,
             'accepted/' + wrapper['publication'], 'publication/' + wrapper['publication']), 'Complete wrapper diff differs')
    raw_parents = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(raw_parents) == PARENTS_SHA, 'Parent bindings changed')
    parents = json.loads(raw_parents)['parents']
    need(len(parents) == len({p['path'] for p in parents}) == 10, 'Parent membership differs')
    for item in parents:
        data = read(item['path'])
        need(sha(data) == item['published_sha256'] and len(data) == item['bytes'], 'Canonical parent bytes changed')
    raw_status = read(PACKET + '/SOURCE_REVIEW_STATUS.json')
    need(sha(raw_status) == STATUS_SHA, 'Review scope changed')
    status = json.loads(raw_status)
    root_review = read(PACKET + '/ENERGY_OBSERVABLES_SOURCE_ROOT_REVIEW.json')
    need(sha(root_review) == ROOT_REVIEW_SHA, 'Root source record changed')
    scope = json.loads(root_review)
    need(scope == status['source_review_coverage_verbatim'] and scope['root_accepts_source_assembly'] is True and
         scope['unchanged_complete_body_and_comparison_coverage_reused'] is True and
         scope['complete_final_notes_and_comparisons_read'] is False and
         scope['complete_raw_context_diffs_freshly_manually_read'] is False and
         scope['root_authorizes_publication_input_preparation'] is True and
         scope['root_authorizes_canonical_installation_or_execution'] is False and
         status['no_go_packet_pass'] is False and status['N1'] == status['N5'] == 'pending' and
         status['energy_source_freeze_sha256'] == SOURCE_FREEZE_SHA, 'Source coverage or pending status changed')
    need(set(reads) == set(AUDIT_INPUT_PATHS) and len(reads) == len(set(reads)), 'Declared read closure differs')
    return {'result': 'source_identities_and_reconstruction_match', 'claim_id': CLAIM,
        'meaning': 'Integrity only; no mathematical calculation, proof or audit was executed.',
        'mathematical_operations_executed': False, 'mathematical_predicates_executed': 0,
        'scientific_mutations_executed': 0, 'independent_review_supplied_by_tool': False,
        'no_go_packet_pass_supplied_by_tool': False,
        'external_scientific_input_reads': [p['path'] for p in parents],
        'package_local_integrity_reads': sorted(set(reads) - {p['path'] for p in parents})}


def main():
    print(json.dumps(verify(Path(__file__).resolve().parents[1]), sort_keys=True))
    print('per_element: checked and not executed — source integrity only; no energy-law or normalization bound was proved.')
    print('per_site: checked and not executed — source integrity only; no local support or current estimate was computed.')
    print('per_mode: checked and not executed — source integrity only; no moment, energy tail or spectral endpoint was computed.')
    print('per_block: checked and not executed — source integrity only; no weighted trace or coherence estimate was tested.')
    print('lattice_wide: checked and not executed — source integrity only; no continuum, physical-selection or no-go conclusion was verified.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False,
                          'mathematical_predicates_executed': 0,
                          'scientific_mutations_executed': 0}), file=sys.stderr)
        raise SystemExit(1)

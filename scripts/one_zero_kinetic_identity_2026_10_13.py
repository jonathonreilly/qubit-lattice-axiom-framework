#!/usr/bin/env python3
"""Kinetic-energy archive/reconstruction identity only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import difflib, gzip, hashlib, json, sys
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-kinetic-energy-20261013/ASSUMPTIONS_AND_IMPORTS.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/CLAIM_REGISTRY_ADDITIONS.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/CLAIM_STATUS_CERTIFICATE.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/COMBINED_VALIDATION_PLAN.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/CONFORMANCE.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/EVIDENCE_MAP.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/HANDOFF.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_ENERGY_BRANCH_START.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_LAW_ASSEMBLY_ROOT_ACCEPTANCE.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_LAW_ASSEMBLY_ROOT_REVIEW.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_LAW_ASSEMBLY_ROOT_VERIFICATION.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/MARKDOWN_NOTATION_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/NO_GO_DISCIPLINE_CHECKLIST.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/PARENT_BINDINGS.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/PUBLICATION_EDITS.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/REVIEW_HISTORY.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_AUTHORITY_BOUNDARY.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_RECOVERY.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_REVIEW_STATUS.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_WHITESPACE_CLASSIFICATION.json',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/TRACE_GATE.md',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/correlation.publication.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/correlation.wrapper0.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/correlation.wrapper2.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/general.publication.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/general.wrapper0.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/general.wrapper2.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/general.wrapper4.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/one_zero.publication.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/one_zero.wrapper0.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/one_zero.wrapper2.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/two_zero.publication.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/two_zero.wrapper0.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/diffs/two_zero.wrapper2.diff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/013341e5fb3c9f3f5436c5bbed59229ec968d80ce63365ac290ee1665faaf7d7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/04552fe2396b9ff394c131f8198ec3f672ba8c6a90d671d86b8a8796655abf69.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/05aa46d5699f2aa516f83a330019fa71386e5e26c874e50926cc76840e56bab1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/07136a2f7185ceb54b4809f9235bbb928bd32d39d7ba27c3c5a220cfcd23a0fc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/090a420b8e433184c480b868344f17c0c8a0adc961c58a9f3e2469dc87907fae.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/09735ccf3d4d35487cfe3a764b04082101325c3d34d432daaab9c167737879d3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0991b928e681892c5c3d3d514cd781c8fd0bf779f4cca07a2d525dd69bad4498.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0a3894a1ec61ad19c2a398b544eb099f72898b0b0717d7dc6332e968097c9fa3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0ab0e7b7428c80f6da09ee01db9470a98fab6bea6508afca9af37138f7c57298.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0b6c2435be2112a196bcc64f3736ef3356710cfeb7253062445218e539ef4381.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0e38bc3ccd32186e75db5d3f09a30388db9cb46c011f233ae141c1fd204a46ae.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/0ed542a3228607b3762f6f1c5c8295fc958a1ebd6620fffcbb2f23d54d87f08a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/105982102b850d4bb44fb2cc449b11343d5afe6edb9582fe8f6645cf2f7d7a3e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/10aa75b19058e8cc635a7c2a35a31552fbdb7976851c6bb0ec3c432ad9a061e3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/11feba7138c6f8676d932ea50c8e8da7430f2af2f54664b41a471ec14887994d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1233d147c85687c25c43f423da6c66b63954d9780123af8bcfe75c5e697388d7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/13f6980cf1315fbfcbdc51f397e02342c9a6e70f9e3d18cd0702cb1cdae0f737.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1499df763b7bbee6a162b0a6639a6de75c7a37ade42b1ff446cbb8bcdadb8557.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/14b31bb47679d710d2b3b507098f095c96662826c338a0478cbab1e0d0fc8cdb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/181af50fbe1847df07d1c55826013f74aba3021317eb0183610c0ce1a8214401.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1916d8ce84701eafe40b9fb4e3616c33dead2b1a5a34cfad29ece02fb08ec6f6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1930c88f042fc9998bd56fe5f4214aa2c91178cf8d68634637bbc57da8979146.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1ba2b386fb9b38c7383881d61e3f46b46afd6876049e2777f3421b7120fbd01a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1cb9d3036a2a978a0e92b0ceab5528e8e3808c3b0e5e7950c758b0133a3360df.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1cdb3d4623c11bf8212b127820c30d3c2fd0edd2589fdaa2345d9862596083dc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1f26106e3948a4db3ddd6c81cd0782cd131682d92abc7f6b39fb4e95318b1993.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1f71af03465e71a57bcbe0f7713759ab51ff36df02736bf8be5d9e798d9f725e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/1f986e2bfdd9a8e34bf372b06dc497f32524cb4b803ec9e660e7a1c80d319ca5.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/202456ee5809c4184a801f74c6ad187e30343df6aad0eaee47b8302065114241.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/21e88701eef85d477560659baea8624b876e53a129fd95afb939772e72377891.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/22710f0af4cbfb084da0b15a959f150e750f09f157dd7489014bd805b8eb4fba.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2332727c569a3cb8f32f90732f538e4eb45b1be1df2253d35b23f8839bfc503a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/23e7c264cda2a1b24f855fc0b1678fb09073dc20deb62e9e5ecd72971056dfc0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/240237932ec18bf6c4c4173a39265b6d291df13c8a8d703d10a49871f3e511cb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/27d5a8322e80bd487fc293f7705607420dd260a7b7db9b1a1a47a2fb1cdfedf2.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/27e2e2add858feecf52c977bd6ea8513dcbade88078a311f70128a448336aec6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/29977685f42ff877358efbb94bc9302aa5e6f4cd165b6dcbaad676b2b950a132.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2acc82dd9b3a7a895e857e699120da169bd57ac3688dc079070e612dfe5c476f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2bf34704e10f9af52efcf097e78628766fe9f0b1a8bae68aa51123882417461e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2c01a8886351c48f9a3d15ee5e5810d9383cc750e9054638d567a4ef123ca431.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2c218e91f763fbf5c9e087b39a9a9a81caba757bf0eff4b4c18cc0ef948cd2d9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2d89bf9c9e2d17ce71b1b933c3f23169f70661c1997a7acb5ed1d55f3920e64c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2e1ef5a724857b9d078262587cdc0fa824e390a1da840b2ecc8969bd16cefdf9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/2fc825965d0303de2b244d3dac2c704d1e2c37be92b9433fc47a7f9d809fd0fe.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/31c7c10d8a3078c0f2ee864ff876ee86810dd2737f8eb045659bba059663dde2.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/332d2731f3b32352a8563646e393b89271c994cbfd2327d89332d6e40e9a46df.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/33718c87bccb71041d1800e5137c2ed0eb6b0b13a7365258a63df15c2e51236b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/35b2def978d88c4e42ee165600f15e6505f143381a7d5eec9cf3e60a99ea5018.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/36a6a1938ee5fb3a139bff676aad1c2c22a19c5a9648827832135450dde290bc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/37b3c8a07e76eb57f7b1cc6514352a1b627f987e3618ee4b7e7d7cbba664f294.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/38cda3e5897139ab41e36b59c7e11b917a51b8e64e67f84ff7072ebe0677f6c0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/390a9efec32c6ca740404cf607bd6c095e2816a66f913c16d97a1d5321bb41f1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/39a689492e3710536a4ad7707887fb81124485ba268666cbedaef0868dff7fd0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/39bc9cef234b6b74e56e92d1d139ab5b0f6c26cb10363f6b5b8e3f923ed83009.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/39d9648dd127543de72f2add7163407233e8c6633f64d6c82ed3625bded94723.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/39e9d0915cdf4f14fd31a3b4ccd587b02936d21c15b152952437f6640cfd7f0e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3a83d75e2da1e0bf8b555fce7a5897b0386a110ffaab866eb76ee19e7b89b757.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3ac37d2fc693bdc66eb2a25f8c5cfae8ea902812073ab8d4418257520e817178.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3ae9511f5ca7a3e27da224a310cb39ace5047050c165217c38bcb96c3f8e5d47.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3c354404ada08f024e1df938fa18cdcc03193ef4e7199f8a0dd993251b05785f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3c7cb4b439458201d7efc012593967d66aa0e715ab5399618207ef4aa7e6b474.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3d409e93abb3b58796a9c10ca6d21ba93b7edc73b8fb24e7364da97c805580a9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3ee13e93acdd2bcb432255e0fb838df635db162a9cf2138933b531295559d5c9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/3f48175b85def4e7f66d78033ee85cb59d97438fb97f4790bc24d7d3ed360bee.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/402cbc03585ac1cf0fc32facfc18b889de09a2fc9b3bb1449dfda47beb813c0d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/408a47c0717f77a63058197dfbe9fb0df3d1e406d5898e8553cac455a674c4a1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/409f3631e7e955947d1010a90a8595b53dc94d7ec30104cd14e049bcea10e650.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/40bd948dab7dd7a05bfb358aa51090f7a3164f5f498a0eb0ede4b5f253f59d8c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/40bebe4fa79afe383d50aae1941598f10007e79594464cfc7969c6cfd658dc19.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/427098cb31088e2db8c5a25f5fd346548dd92d7acb6501f58e60bb4b8a3e5b1b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/42e77bbcace72d58e57932b91cfaa7f75bf6910f87acb111535f4b691fefcb69.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4317cfddb444f4a3d09d138ea9997f917807a29929140c3c91a93e73f623a187.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/43fa86459c017bc19b1e8a96e3faab1886cd2686ae3653ef1773525a2369b0c4.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/445177db07579f740f427089fbb981c2231f82ec42aa54deaefc2c23de16890a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/44f99e5ca0ebdc34f0fc48d6fbf77f8af4863929d220b77d852264cd18b4be3e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/467fc3fdb898d426608a957e3dbd3b9875e2adbfb13d4480138ad7bd892a2252.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/47c1781e22a6cc8972302ed1a189a06fa9b034f16c53c996778387b49255790b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/480d89f21b46701c97713b1010d52bd0e52e6377fe97e79866fb62b455d24efe.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/486ebb065e3b8ebedf857ba40f6b187c676991922f750d890ee772fa3406cea9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/494c8a0e50b3df80537458d4869cd7f20b7c7c7a4e686e0435adb6b5612bcad1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4ad02d5a71f95a64d115136bf3c22c6edb53e6e401b7554c3b7953ce4fc0b270.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4ba800fb77942547cd7e6d2bce426d1f437633f23d5a217e086ae6e31eea4c38.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4cb5929d7dcebe436889d3053692e8f57b0290f55b360e55914c0814795d22d8.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4d0a8c9b8a19ef46c4d7779f1a12f8149532762f39d5e607ae7c9b2edbad7f41.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4e0de0b1cb2362a28fba37a1ca1582d437ec33c118ab4fdf1dbe4e126ae36f7c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4e68d96fddcd1c5704e9b69133129e861c4b1ed8c85f7b7cb7fd15ae404fac4e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4f48ee137d1389602484778633474d6ec4b9a7c43f67c36db6f97b245f81c459.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/4fedacd422fe817d79a2b44304f5af4ad30ad8a9d93dbe9eb9c782cfcaeb4e2a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/506fbb1af66a12445c512912c62b3e8eefa189a127990bf06eae3bafe4ab08ff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/526f442d6df264c5b02424835735f90513e5227a6cfce90cd9c692c782919fa1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/53694f70cf61d072bf3f9ef7873e7a8d1aaceb44af86082d15808d8f4a72d885.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/54eed2287e1acf524517984d3f69614d68179ed9ac1ca5a20f7f9b1ffd536e01.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5594afa2d58271a4d29f4fb3277baad137d8a844f6874ccfa3fa5edbd609cb61.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/55ce027955d0e95beb42014bec0169fa2afd97058717917332b20281f7a6debe.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/56656c101eb030772b5d414e39c2e82bd5b501fed5454f34ecbfbe35b33b2e64.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/59a6ca44b8c152227dac33a2617ab7d4083385e37887887c0803c634f2c733e9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5a93e8eff77a34fae5dc54debe43c85b923ef25e447c3a486e0f65f4f8c8c8e4.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5b0699a94d06fdda853e52b39450e65aa497d06e80f210d9061bc3899fe4a473.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5d58b6ec220a2b9f84342896b45ac3c30a968357bf1582400797d286e4403890.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5ef492b017bafaa835639603ccd4384a679cfd6c95f2ce2cabe70ec1aad74681.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5f5289ff68d396f192dddb606dc9e2803a2b306f0f5885ceae4ee65e7034e498.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/5faaa32c2a93069079046778c740e468e8ed35d835238401d90fb3579c485ed6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/606b61a0a1294a9fd87de3d4df03214d85c21b298814b86a495e580589c37bea.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/629bc1ae4ad258f17780fe476b695a2db04dfbef184440771d7d264c91ec68e2.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/655a011c2b385e4eeae87c3abc593afb99666b7a5f0cda9108237de9f9963348.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/673064db42be7994c509e74efa390b57b7415fc51ded49c62ce3708bd435fabe.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/67cd7eb88113b74f5ccb44a90bd6e08f71c7c999d9c43147859ca2022475f464.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/67e431cf5f005fee75f2438db150a471411483ea76c7f361e2540ffcd126120c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/693976789006e300d6159398972dcde8f7e122f009f18e4327a5a4a37e7f1946.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6966dae6eb5b6c17be4a87fc8d26d7a1d40e1252fdd482061fe756c053a2e8de.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6a27828ee16e3b5e2028cef6d95d7d5a9edfa8ce43fb435558cb1c7d55e135b4.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6a4b928078a5cf8fd0754fdb4ef114b50e01c6754a4db4ea063d532b2fe25289.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6b8bbda5804f98bba27ef15953cfe166c7219b97b20c1babc90c4c5157d2674c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6bbcf624e47e4d91f2a6fbd8982698d788923bba63612f90d5930d04920ca49b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6bf90945b4cfa48fc656822e208ae4ebe304803d924b0d212671d98b327a75a8.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6ce2f66b5c660a0137665a3f597507394e70706861f10d006b56d52a4e6cefbd.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6d81a6b99be98432f5574d169da8c80f194b10380fbd3d8184c6c5ee840d4708.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6eb14ee15cbefe4794b866ef87f5043e17e0c7d5aa217ee38234f191944ed267.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/6f2c488dc398faf671e9f6b9521683071323694feaf8e4e8a1b7028eb5ebd45d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/71757206665d9243fef6be4a1c0e46385faecbef01870cd2654e48530a7950c7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/71d0bb07028c8af23143a5973b2ad8f4f39ebe4cc8e6ca9c1dcd6c18d97ae71e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/72dfb25e59ffd801ee1e2b22ed7a8168dba25d722fe3caa4bf4b5946328785db.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/74d013a74e3809a59045a2e265c2fc9061ddc650a9a01e7603d495234217ab6d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/750f15023c5e8b7ae62ca84e0d9a677c70dfb3782befd0042cba8b697e030942.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/75692c58d3d5fa3885aaec893f6663d0bf6df14d25bf3b58b0811dee0dd75443.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/75af8dd47360db9735da03b4e7379785baf2a8340dcc142e101005898ac90a94.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/75db2f06ba8f9fcc64096aa5f5eb3fc20a20e1274d6d73634c756cff07493007.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/765d1a875c5710b17cc16bac88be5d7dbd556a95f85b34527e40c662ed392309.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/76f4b57eea195c7b4c42d5d7c23dd663a9e176ff5ad4badf3100004c28cda947.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/787d5fd3eb49e5f605fd69a0eb2b925c087d9bd33a1d13c4739fb1067f4423d3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/798c14f8467d1bcfd61c6231da901a754390686d1645688120729b22e47b2560.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/7c08c7a6ef4fe7d88dced9397f87625fbc74394f85e96968d4d4e23c39830283.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/7c4d7027f3e198700cba992ff6557614162e1ec45c33c40c3f8182585902ddb5.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/7d077850d6a8d9edbdaf7bcdbad92107f12d7947b27b657f73195696158f2113.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/7fcf227a57f962bc1647ffd9e2ab3cefcd4168d828194593bcb235669c9e0332.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/811d15bb248873182054ee60d83728fbe00277b38f9891d860d92e0527bba81f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/81646207bd2f648f8ab6b78a8e8e217c1da1a23071911aed528e7a321164620c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/81a009e6454194c9d2c200667c6091b490d55ac825b7bccb09a8ebbef3e76e05.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/829bae7ebf39b4e4868da25d9d877fad0dfb4920eddce6199165e74fae4e0bae.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/82e9203fcf86d020a1410effbf8c81656dc7a1f6e43db5242e032aba474d8497.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/830f776447d0837fd48e2c739fec032d399712487f36b5f4affaa5dd66e4fee1.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/833421a632b07ab8705172d3fdbc41c5532a76e2ecf33c4c6ceef3c2d6fec069.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8361667a12e01be16c40b01a3fc6aff14512fb1fed6f29ccdd9cac2e4c408c09.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/85343b92a0f3448d44971484dfd80d0f6231f71f6301c71829e9be2bc913d782.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/86161013c7ee3a5999a6e0bb39da5dc356d01a43a6a69c7c3542f25956dd7231.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/86866bbed43b485960ef0cb37f753bbb26c327f0e18d4f3ec10597f222689226.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/86aaa6ab25143cfda24688c63a5dcf680e325ca7beb3775043c65b777f50f644.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/873d0a05ee4eeb6e52c78b79e6776ac6111cf5845e100e158ff3b3b1a2f08a0e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8754ec5e72c0db3171c0b2ff54fa0e15f5a77f87f3950ac8f19f4d1b0c623fca.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/884c265e010334de101a308c6e174f1f80ac2e7ae215aa73a5c6135c5db03329.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/892a77bb69fc47e9adde072035304710ef9255007f4c156ad07c3063a7a66629.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/89310e793d3eebe203b60df5ca0b4e081363035aa25aeda6c2e70ef130c613b7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/89ba3c7dc66a5457732bf9279bda500087827e5feb149568933d10419ccf65cd.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8a1a329e0dcd3e0915e469d9fbb08cf23b818c13549437903606639e2955c5e7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8a8c93b81f714431959edb36721463ab0247a605130cf104855b686869f476fa.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8b68b83cb4d809b03ab890cd7883b7db9af22ecf3c557b5ef1df8d6683259ef0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8c7604e0e7bfc2f34c75a2ec0d2cd7a8664a506920281a218f8df18e73e98a3c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8c8cbe20f81349542d196bc523db9fc52f8762e721c95dadf611d11efbc04037.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8d04130dbadce921cfe516afc056205409513e98b1261156878e7db8373780a6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8dccfd283ad3efad0c816f4d7290ebcc7ba7be8648830448049800e481d50811.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8e259f68ddadf738a9ed70c0e45bcb689dc867021f7ad30fee586f7ccc09d392.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8ee72acb47648e07218e66e3271f0008ae6bbae7e7a866246be474a53d1bedb9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8ef3bb68ff1e0fb129de54efc1d07b74bd80926dafeae709f044963478e79700.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8f6b577db80437efecaddaf50664b35c20559019870d65cab7367d53f15b6e45.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/8fab84608c413d952d361757fb6a3dc4a38b655e33bbc351e9f4954b47d0b462.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/902f21d5e6d800c88f40f5d07c46c6a62c0f988de22c278aa35d1de93696c43f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9065c89665f2de14f2229c4b3847a534d3ae4bf48c59ba98e0bba92c696452ee.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/909d0adfc19db41502d3cabe0c0c265ec042a03c30c254e76a9d93a836c3ea95.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/90a02c5caac9816adb1c79da539bb84a18e7ecb3dfc8594bd16efc414786d7eb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/91b52e0736eed466f97ab0103588d6e49719e6f4f6ea46a1cce718ef1bbfe70a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/922c97e0f3ffa99de71ae7a30fe10b8da2682d591dba5ffa0121bc4c0d43ff55.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9273fa8c29133aa51e2d5fec737ba46f9c49b7fb0da4b343e625e6d3a749005e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9312f7a49f250e5f8bcb0dc860f223d3ea91bb05e73ad3df72c9e7e33a419143.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/93c2604ddfd1a305d64fac039f62aa90dc73ecef7ea43de45022c13c1b61102a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/94b2f2f57c2c610a82c6d9b90cd14c360378a366163f2206e660afe70aae13bc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/95740530a07e50fcbae1bbb506262db6d51842d0086eeaf85683c553b7857ee8.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/96cf5fb68c76342e0e62d15df0cbd4646e4ab6dd342402363a1aa784c0d28633.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/974e43e24526d8abb19b37ece3e7889464dd7b24f930167f90a68cf4c356eb6c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/97ffc68a01169ad5414187c7185af5d8afef24663cfe5c75947f3a19bac2aa62.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/990e2862c7c6d4867d127c740387a47cacc61e7d34dd5da652e87a80315b0799.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9c36aef983c9eccca78e6d5b2d29fe006f81b25964e5ee7756581442fa55e8fc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9c6d57ad42f802816e3b2dc4f983cc96a78a613ef376f0da37f618e3eaab5e60.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9d0acc81d7637e0e13d05100f00ff3c088d6c1304ea263eb9c7069e44e7cdb68.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a04ef0b5dbc4ef8a7548417424d2a4135956463e339be6cadd8f7318a71fd54b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a10c7c59eec9e49a597f678202b4a1f4e1f5436db879633b4b12edc5003676a2.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a1248b2a9393f428cf853a2f4f400e92b4bf585deee98fe63366c14fb98ab898.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a202b93b9b6d983d67e66031074de3b37f03f1de66d5fd9cb7f23fb7f9b6742b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a20a5d24574d9564de355c96d5e4d6a2ea3dc579c3d9ff0027ef1cec1f1e70bd.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a3201e87e25b563e9b7a7233af32c051546aaff85f33883d87744562fc0e027f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a39f2158d59c481b21f6f33cbed11575ddf916be03a081948839bd90f73f0e11.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a507cd3476c3e381701e698bae67128d3168e947f76e5d05ac9917ef99d53c1b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a55573418998e6b496f985f3066835326ea8e74ef1fbb27c54a42bbc37ce422e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a7dc71dc9823520db9f19f881e4d960e2f6e3a1a9a11276d5f1fd8aa15175c14.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a89c8915a2f1207aaee8fbef7273494126445d4e26fbda625d418f0557a83cb6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/a9be793890809ab75d74c02c36595c819d2b7511b5f143364d2c6a31f6b2e269.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/aa11e3abf55c171788c1054a2f971aa3323ee1e732cc0f10c01dbd18b6639559.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/aa28431125d841bf77c518d9f99d69388f479ec811e88603534fbba9bdf812b7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/aa891ef3fff5f1ad6465432454226b157f1930be0461c698eaf55592108261e6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/aad56e3c125e3039a9107851e3ecebd713fa1c0aa474a17d5c0fdbdb8018b3c0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ab72a465949ba2c3ea36a61909e10ebfc233ffe9e67d3060e7733ad821fd1af7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ae506d27662e03fa3a4b4d12b243cdbcfb2ab7079c7a5bf109ac3453c89aa31c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/aec57f3440c19a7706e013410c8fbd349215f943e93806e83db941e75ba4a541.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/afde8e1e57250212812db9ff808c9cf30fcfd305d31c6f4af8a1668a40188d94.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b15dbff690c85203dc842bf1853945bb18136f17545e57835ec9b45ac68c8020.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b44108ca633f00561d7a7f739cfdcb175a1491dcb7c5f0c4be06cbde3a9e387e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b4bfa525a0bf7a9da2f22d796e2638fd6c0786012dc1309135d0eabaf51a9843.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b4c11d1e1273281dc4fd9a75999ca96a519466bc7c2b86290aa239c16d134c42.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b5997cdd02385104302482eb5136ee1091953fac8a31d3ebcb4751214fe55a27.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b59b35a844c84c6c26ed69078124aab8ed50e79d0140c4c0ad368b2d81211d17.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b5cc5f8bd9691ee3c07fd3ec8349b03235c6d25c983252a104d66bab0efc8c70.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b6320867800752fb0998293f74c09aa0e76aebd8ead94a4419408384d08d748a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b658ae7c4ecc76d40e1ed9abe7567a06d36e0c5053d4c9c09b0802bd6f5a0eef.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b792099f2687ae9e6e9f99cd240b03cdb894123d74a69c257ca0fbaa9261ad76.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/b7f45aa9830790528a192e300e6db0bb5d43d3f1783bab673dee9ccd217b381e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ba209bcec3d7138e0e5667d2bcdd89abe0c9187324f551daa17d4b56bd54df44.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ba52feda6f44d4651f9aff465f7e3f3e3ede5943f647f87b7a429466393c6f67.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/bb2c9db349d5a5a2477cbcf3ad61f4a86686d8e49fa49d8e16feb416e504433e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/bc6b21b9c519cdd3882b3c7efc2e4399cdb731833e7535ebff588d992077a17f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/bcb9fab44faa8d06a93cf98cb4dba53f3b910c40c5a9ea37d76c4c3836c4a857.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/be96ee66805254a830f203796fe47e232b3fe2b4a5e2d216380599bd9c7260dc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/bf9c337c0d0d6661d903d1f7ae5fd4088edc4af2c45f1ac2f73982b150eb00ba.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/bf9cce91e4a52530ac057a8f86a5a2a34c7c6613e735dacf0fe9b2558b5e387d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c01f1feebf3e61de4593a74f076653b92d6b17b8a4b940f66c0ffc09fb3b4795.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c0f433a2b68517adae3929cd56d354de0f9da7a731a784e64c142da1994a08eb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c1def9ee8738c5c446c592ea0ecbc8b79b1c8fb1513ebc343f4b5bb18395264d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c1ec777807052a01e8269392e82656d8f440af3a499b52136890aeda2e0cbd1a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c20291887b2a4dd00244bdc6a0d165ddef7a6f72c63cd808cc037e6a1ad58d13.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c2959e640ffd389256877004c000a20ebcfcd990cdb342fc4d2a5675fab40774.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c2aa65ec0dcb1150e28c9a17afd0b48e14a458083503d558f9df5069d3b8b8ae.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c2babe48fb44edb295948ea88f49aa5dc3094f947e31ef745324ae820226cb6a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c388c16e8b3518769ea8daad47a601066f4061b0286e2165d19e877c33715440.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c390310ca7db4b912df349d24b95187659575e067dab175806399e2e61ec0b16.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c3e59e7269a71697d05da2e64cd290c5efb221404a1104bb60e1f9407b3df035.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c4be1fa6db1de124f72119ebcf75680c62ffb9a01d534653f73e697070871dfe.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c69d638eb4519d81e51dd39fd920b7323d320d5aea9c427ff109736bdcda75dd.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c70bff5be604ac3b18608317dfe97467f21df8bf8285846266d0c65cee5f97d9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c7467f0e5d70e764c02e68f7b0d15d7a0b7d183716df0d7df9838a21a3f5cba3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c7bb0d0468b6b7e3a62b35c3bea61548b4eaaffc1cff1303db6f98638b3e7b0a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c8636c96d996db82fc609dc49a8fe12907d9a15b0280e2fa5e2799092ff59af4.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c88198e8f493b312c0f2c0c4bb09c6b2fe54a52f4f01c66d93881597bdfe2878.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c91974401260997fd6e9ac8d43de40ac5d6f66d8816704f6ce4e44d130c9e519.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c962f50a064176e217b9b7e54ae9cfb8093d7e9fa840b1f1034890e469b54644.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/c9e8f391a8218f5859662114039bf64edd7a7b02de2ca285db2a1ddf04ddff9b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ca02f29fe50826129d5999eeb73a48e6401db98fe6a1db7b1e178711a9df8079.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ccb6d0be93f26eca6cb320532c0abdfaa7fa62cf16621a60437edf1442482e07.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/cce2dd8ca0d97edd67a3de11a41e68eb463b559e2e529981202f2a294b3cffbf.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/cfb8a340043162557e5bd171f85eed13b2a3edffb482ff4a441198731656906c.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d19a79cb97199d9ab4df34e03d627fcb969d15cf9c27e82441577bcb633c7c26.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d37450b909f5365f42ccf96f41681576d4c0629f6865b51392483c60e3a77d74.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d3f10645348e292f88f1aef3cd30165c27cd581c3d64ac2d2b6a42b01760b58b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d3f834107369d377bdda581a632a53da43ecaceeea9e349d5a7b92c21497d4cf.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d446057160fbc1a42dd63cac4eac33d313fff91affd0e873ae71d5953b6f57ac.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d54917008c3cd19074157492aa6e11afeded34282acac61111009dc4a765e013.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d60ab15b6c88b63b72188509c43b5eeec2466721a3ea3e82d3a70b159da52420.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d60f93727acac604bee1876a641364493556f7dea3f8bf1cdda86a37f06baa3b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d7e828a767987e1d9dc894118c3d4a9fef609f29f19730f574ce95679287447b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d90813e7489a26957cf48dac0f448e40ee47f0d8edf440f686e539d1c3dba50b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d951f08942d6948839e72aa4283193c8845bdca0b617465f5ee8ad8ab735ba9e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d97347a9be6f01dbacf3676f57cd76bbe8e2d5f9d582d1c696ec5abb066d6cd7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/d9e2df0747dcb5ebe2bf0f86e56055cff62b17c4110136657e8d46808533c921.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/da386897f7862fa0f6276d23f33e7b7e40aa3009fcd1e816056292884d5b9d11.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/da50611976fe965976460a2cbfb98dc9f9ce91ac24796d65982b10b79ff7b71e.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/db200fe8489f848f5abe71c1f34a830f00eabf0855f5395d89a5f111b8785461.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/dd638de49a8e8f80ceda87684d7d48d61614ec392d2db79274f315d7f238e5c5.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/dd6c95ad24ebf0516b2a3905a7ca4c954ef073d80cf131e65e41a0aaa3e64e9a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/de009e3f226d1f39ba668436b158804d5e935d714dbcea4a43999bafd11f4637.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/de3470f82e5047fd048967850fc978dbf00b518523f4c275326f5eba5e51a7f9.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/de615309a63a561d79f1d6dd8fa4d5b0c73eb62c745d1e543ef2d134fef5c2cc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/de6e827bbd2f32721de59675544f61b69f140435732eaa2c98708277fda457b6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e0310f88effccdb0a377b8115e9412dc6a5f9259887c356be1ed96c9d4977075.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e12a8db3c0e8de5b466ab1eacd8856911e798d0ffbe14b8db88c90eb728700c5.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e1973088e54fb431d859ae3aa5dc549606560a04e75074638868c96d706b2db6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e20e7acb83c5ad42558d9af3b09b842b2bf7bcd60bf596a0a84c47d4b5648223.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e42b4b8d96d8af73bf840dbaadd180f0173e7df75e8cf054b2fbef5505d78746.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e4e7acf45979838f356c04b7ec3095bb7b74e57a755db4c56726686e2186153a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e61e181d4476d45480fb1d011ada2588c470acacdece4b21efb35337e0a9efb0.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e67dc87322ac90f50a2aa21cb780ed8d60bcd6761f3af670a10507e1c69aeb20.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e6a18bd6470440720164d61a3a16530079f1614c3aaca94aafde03ddae8219a7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e6b6c22c6f5d23fc72da5dfa909a235ab1fb9b0f73b68df19f0eed185fc4bc37.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e7d605b000d2af0b4f0b0e1298ed6b50765b7c03f80379ae6b6dcc38899103ff.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e8b34ef49f7e3d5c289584b8f662da40a05912794bcf1b4cb8e05e6c903bbc88.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/e949acc4f46e5ffbc7f58818ca78e58610f3c21f3ee647fa0b2a8cb3b8311c26.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ead2c5427190a463efadc81616ddca2203e4338870c6028d4b79f3ef8f2ccac8.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/eba0a48f224c8d8d73f2c8e4749e03a5cb5500b160ae34d5ae4033f7aca8b7d6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ebd4ce941c1ff04e851c05159fc06a6ad04d7700aa307b5bb44592d0bf40abae.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ecce4f5a072db7a4dbf454201fcc6e5f368530d94f5423667e5617cc234245eb.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/edc0abc368e2ea485a5f221cbd7e9a262f83945c790593c2667085109f84b24d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/eebe9b81d48fa517143ff3252e9c2744c8ed989ce144660302cc7bc24350e02b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ef7f402eb108f1f6c5988d3974612b14b7b91cc89ea5c3d42a38b4646d96e73b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f36c4c9de09c339609e942e22863781c06a9a7126322ca1d8ba23ebba2b3e1c7.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f4059ac8c0392c035e87b0b26a61accbfa22d0a8ada15b059fe894d92ac9ca0b.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f52ea2d5cae4d66fd1bc0f638af475209152be4ef911aeb99462d9e6623af9c6.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f8603b0278ad54bd4b33be0512dbabf03b2cc2a17d46aeefa4e188aea1594b16.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/fa94d5404c32b6c71fbbf2fe0704b75cf4b2fc80a52514532ca94f80957bf28a.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/fab7308a45eea59fb727475fc2d2eae65947a13b434384e2d5906eda1c5c68a3.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/fccf1ea3387b059b1d625b985d38bb71573a5bfd48af12e251dc33489b551960.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/fdda0cf69417d9787ca7deee14d3ac30ab74af3d3d10a2ab2455036644c45402.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/fee615613c637830bfb4caa115f85247b1e1fb9cc5787cd6a058411a63df0266.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ff948157cffafd4565782da436cbe42bd52faf2b86c300e3007140cc55a6285d.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ffa6c8bbe7d0e3e192e5d9b3eaed78712995cbaab80b48b29864a8a52c3b29e5.gz',
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/objects/ffd1fe2af89df10d6b39f14484c18781aec80e199514e97a406d55a0f2fd0593.gz',
 'docs/CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/ENERGY_ADAPTED_CALIBRATION_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md',
 'docs/GENERAL_COMPACT_CONTROL_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/KINETIC_CORRELATION_LIMITS_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/ONE_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/SMOOTH_PREPARATION_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-13.md',
 'docs/TWO_ZERO_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md']
EXTRA_PINS = {'.claude/science/physics-loops/toe-kinetic-energy-20261013/ASSUMPTIONS_AND_IMPORTS.md': {'bytes': 1094,
                                                                                          'sha256': '4f83272ccfb3bace1ebb011041c55772691be49ce9a2eac849fe368adfdaef6a'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/CLAIM_STATUS_CERTIFICATE.md': {'bytes': 732,
                                                                                           'sha256': 'f65136899ecb9288497eec656f6fe946aab40e74faf49225a111bddabe6b3df2'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/COMBINED_VALIDATION_PLAN.json': {'bytes': 862,
                                                                                             'sha256': 'ccae245a626d553510308e132e8521a87a440c10e7c21653018c4143f45ec293'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/CONFORMANCE.md': {'bytes': 1323,
                                                                              'sha256': '6cc92b3ce07e99e86a90ff36614b4b21cc59743e7fb269fec4a9df8d1d58e03f'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/HANDOFF.md': {'bytes': 1686,
                                                                          'sha256': '966b84da697549b117b601da38d9cebf656055ae55a468ffe343edf9d315384b'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_ENERGY_BRANCH_START.json': {'bytes': 591,
                                                                                                'sha256': 'd9e2df0747dcb5ebe2bf0f86e56055cff62b17c4110136657e8d46808533c921'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/KINETIC_LAW_ASSEMBLY_ROOT_VERIFICATION.json': {'bytes': 1969,
                                                                                                           'sha256': 'a1248b2a9393f428cf853a2f4f400e92b4bf585deee98fe63366c14fb98ab898'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/MARKDOWN_NOTATION_CLASSIFICATION.json': {'bytes': 2334,
                                                                                                     'sha256': '3122e408afe1be7fc9da5d2bfce621e223ba7d17370f6ae42403656dbace320e'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/NO_GO_DISCIPLINE_CHECKLIST.md': {'bytes': 865,
                                                                                             'sha256': '0c2e6e269cd87b5b7b95cf02fead12f25920638954ecff061a508d49bdd3e366'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/REVIEW_HISTORY.md': {'bytes': 4815,
                                                                                 'sha256': 'd8a76d64f2b0b5d0059743e95acfaf52ea2491b498368182a285c601e76284ee'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_AUTHORITY_BOUNDARY.md': {'bytes': 1831,
                                                                                            'sha256': '0830ba9d5364da96c26c227acca4e77e2983a9101a0b63be975c2546b5d5d551'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_RECOVERY.md': {'bytes': 1204,
                                                                                  'sha256': '75b660420e4f349f54579fa89297b84aa68897e4cf355ac8b0b938727a4ff5f7'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/SOURCE_WHITESPACE_CLASSIFICATION.json': {'bytes': 40,
                                                                                                     'sha256': '1f17d6af0c04f649330e10640d58a597d18c20709555c9b01d786400c8b60430'},
 '.claude/science/physics-loops/toe-kinetic-energy-20261013/TRACE_GATE.md': {'bytes': 833,
                                                                             'sha256': '034c67ec256e98713b98b128d85acb11b15d22377e47f6a4f2fb82c8e32bd2c4'}}
PACKET = '.claude/science/physics-loops/toe-kinetic-energy-20261013'
CLAIM = 'one_zero_kinetic_energy_bounded_theorem_note_2026-10-13'
MAP_SHA = '0fc14a64ece473f4fbde18d0f550bc65ce2cebf5e6bd1444dabed0098ba87af7'
EDITS_SHA = '138001987b78cc5027da6525648632941a0fff66118be13defcb5a6598165f76'
PARENTS_SHA = 'ee768be25b3c7e277d7c3b9304d907743c8748295de5ecdecb0f2bb8f64ff37b'
STATUS_SHA = '00ee2d4e7e8f03afad14808c6e9225627bb3541885e478ac4d8a8a622ea36984'
GRAPH_SHA = 'b500989660151414cc52f2544fb69eb8390a80c1e08093a01d07fac9e89d5c2d'
SOURCE_FREEZE_SHA = 'e949acc4f46e5ffbc7f58818ca78e58610f3c21f3ee647fa0b2a8cb3b8311c26'
ROOT_ACCEPTANCE_SHA = '3c354404ada08f024e1df938fa18cdcc03193ef4e7199f8a0dd993251b05785f'
ROOT_REVIEW_SHA = '40bd948dab7dd7a05bfb358aa51090f7a3164f5f498a0eb0ede4b5f253f59d8c'

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
    need(seal['files']==members and seal['member_count_excluding_this_receipt_and_sidecar']==len(members)==403,'Original membership differs')
    need(len({r['path'] for r in members})==403 and contract['all_files']==405,'Duplicate source membership')
    wanted={prefix+r['path'] for r in members}|{prefix+'FINAL_FREEZE.json',prefix+'FINAL_FREEZE.sha256'}
    need({p for p in origins if p.startswith(prefix)}==wanted,'Source package aliases differ')
    need(source('FINAL_FREEZE.sha256').decode().split()[0]==SOURCE_FREEZE_SHA,'Source receipt hash differs')
    for r in members:
        b=source(r['path']);need(sha(b)==r['sha256'] and len(b)==r['bytes'],'Source member identity differs')
    closure=json.loads(source('provenance/ONE_HOP_CLOSURE.json'))
    need(closure==evidence['source_provenance_closure'] and not closure['unresolved'] and len(closure['selected_receipts'])==28 and len(closure['bindings'])==468 and closure['unique_closure_object_count']==226,'One-hop closure scope differs')
    for r in closure['selected_receipts']+closure['bindings']:
        b=source(r['archive']);need(sha(b)==r['sha256'] and len(b)==r['bytes'],'Direct archived binding differs')
    specification=json.loads(source('assembly_spec.json'));source_notes={n['key']:n for n in specification['notes']}
    need(specification['diff_context_lines']==3 and len(source_notes)==4,'Accepted diff convention differs')
    cores={};core_lines=0
    for key,note in source_notes.items():
        mapping=json.loads(source('maps/'+key+'.pieces.json'));assembled=b'';baseline=b''
        need(len(note['pieces'])==len(mapping['pieces']) and not note['pending_slots'],'Accepted piece membership or decision differs')
        for old,part in zip(note['pieces'],mapping['pieces']):
            b=source(old['path'])
            need(part['source']==old['path'] and part['kind']==old['kind'] and sha(b)==part['sha256'],'Accepted piece identity differs')
            need(part['byte_start_inclusive']==len(assembled) and part['byte_end_exclusive']==len(assembled)+len(b) and part['line_start_inclusive']==assembled.count(b'\n')+1 and part['line_end_inclusive']==(assembled+b).count(b'\n'),'Accepted piece boundary differs')
            if old['kind']=='core':
                need(sha(b)==old['sha256'] and prefix+old['path'] not in cores,'Core identity/order differs');cores[prefix+old['path']]=b;core_lines+=len(b.splitlines());baseline+=b
                need(source('diffs/'+key+'.core'+str(part['index'])+'.diff')==b'','Core change diff nonempty')
            assembled+=b
        need(assembled==source(note['path']) and sha(assembled)==mapping['sha256'] and len(assembled)==mapping['bytes'] and len(assembled.splitlines())==mapping['lines'],'Accepted source reconstruction differs')
        need(source(mapping['baseline'])==baseline and source(mapping['wrapper_diff'])==diff(baseline,assembled,mapping['baseline'],note['path']),'Accepted context-three diff differs')
    need(len(cores)==5 and core_lines==2386,'Core count differs')
    original=source('sources/WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT.md');corrected=source('sources/WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md')
    need(source('sources/WEAK_DRIVE_KINETIC_PICTURE_V2.diff')==diff(original,corrected,'WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT.md','WEAK_DRIVE_KINETIC_RESPONSE_INDEPENDENT_V2.md'),'Historical picture repair changed')
    edits=pinned('PUBLICATION_EDITS.json',EDITS_SHA,'Publication transformation changed')
    need(edits['source_freeze_sha256']==SOURCE_FREEZE_SHA and edits['additional_mathematical_body_edits']==[] and len(edits['notes'])==4,'Publication scope differs')
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
    bindings=pinned('PARENT_BINDINGS.json',PARENTS_SHA,'Parent bindings changed');parents=bindings['parents']
    need(len(parents)==len({p['path'] for p in parents})==4,'Canonical parent membership differs')
    for p in parents:
        b=read(p['path']);need(sha(b)==p['published_sha256'] and len(b)==p['bytes'],'Canonical parent bytes changed')
    for p in bindings['same_packet_parents']:need(sha(published[p['path']])==p['published_sha256'],'Same-packet bytes differ')
    graph=pinned('CLAIM_REGISTRY_ADDITIONS.json',GRAPH_SHA,'Graph proposal changed')
    edges={(r['from'],r['to']) for r in graph['direct_edges']};nodes={n['claim_id']:n for n in graph['nodes']}
    need(len(nodes)==4 and len(edges)==len(graph['direct_edges'])==14 and edges=={(n['claim_id'],d) for n in nodes.values() for d in n['deps']} and CLAIM in nodes,'Graph proposal differs')
    need(graph['archived_proof_import_relations']==bindings['archived_provisional_relations'] and len(bindings['archived_provisional_relations'])==3,'Archived proof relations differ')
    for p in bindings['archived_provisional_relations']:
        need(sha(archived(p['archive_alias']))==p['sha256'] and set(p['owner_claim_ids'])<=set(nodes),'Provisional proof input or owner differs')
    need(graph['history_only_relations']==bindings['history_only_relations'] and len(graph['history_only_relations'])==5,'History/math relation split changed')
    status=pinned('SOURCE_REVIEW_STATUS.json',STATUS_SHA,'Review scope changed')
    acceptance=read(PACKET+'/KINETIC_LAW_ASSEMBLY_ROOT_ACCEPTANCE.json')
    need(sha(acceptance)==ROOT_ACCEPTANCE_SHA and sha(read(PACKET+'/KINETIC_LAW_ASSEMBLY_ROOT_REVIEW.md'))==ROOT_REVIEW_SHA,'Root source review changed')
    scope=json.loads(acceptance)
    need(scope==status['source_review_coverage_verbatim'] and scope['freeze_sha256']==SOURCE_FREEZE_SHA and scope['required_repairs']==[] and scope['publication_preparation_authorized'] is True and scope['publication_execution_authorized_by_this_receipt'] is False and status['N1']==status['N5']=='pending' and status['no_go_packet_pass'] is False and status['new_independent_mathematical_review'] is False and status['fresh_full_final_core_manual_read'] is False,'Review coverage or pending scope changed')
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

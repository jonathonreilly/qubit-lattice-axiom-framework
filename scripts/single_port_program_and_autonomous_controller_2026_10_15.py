"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-single-port-program-and-controller-20261015"
UNARY = "docs/POSITIVE_UNARY_CYCLE_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md"
EXPECTED_PARENTS = {UNARY: (42367, "fa7028e0e9ad6c2c7d4c1c399feae8f9581f301dda5b46f8800eb6c355137542", "positive_unary_cycle_clock_bounded_theorem_note_2026-10-14")}
PARENT_REVIEW = (".claude/science/physics-loops/toe-unary-cycle-clock-20261014/objects/8d76345b8a28d7d9a80675dda5ee8b1d3f9964994375bae852f02ea084a9a7b3.gz", 12394, "736e2741a361d4630c8a62be986382fb607711889745ee1a2fdaba882a2b6cee", 29118, "8d76345b8a28d7d9a80675dda5ee8b1d3f9964994375bae852f02ea084a9a7b3")
EXPECTED_ACCEPTANCES = {"external_compiler": "bbe2e9c911e3323f840855fb2e77cc5e86d1669486eb8c8dda2e8cdec3ff53eb", "autonomous_controller": "134cbee6390a6f999813dd0234fe869bdd0bec2dddbd5d47a2209091c0dcbe5f"}
EXPECTED_GIT_BASE = 'e93bc2b057492d0eef909907708871cb1920fdc6'
EXPECTED_BASE_PR = 9616
EXPECTED_BASE_BRANCH = 'physics-loop/toe-transverse-field-memory-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-local-bias-gibbs-sources-20261015'
MANIFEST_SHA256 = 'a5f48fa2fd8b37f58f4fae2cfe5dc630f639dc9de2097e63b383f280ee007399'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/3495e85725a1a859ceae2fe841e748cf345db4afa3426048c36bdd244417a0aa.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/51bea7edd9222b8217d29f03270712d579941ecedaa0b7db3a06ced0494d8ef5.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/595bc5ac321759aa883a0a0a8ed89f7192ac48aac16776f9dfef3bd62dd8decf.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/5cc8716d5a9608557f9680ec5ac138f4b66f942b7da387758e54087c8525847b.py', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/6077453829fd70821e2b251624346ed533dc2447cf877992bdbaafe9077ee425.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/8df5326aae7f13bc0d2c1cc9c0c7ddcde9957c2ee18feec5da1caf572aac8d52.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/91697189a3cd89c90fe1b5a36a87132c8d89e7f907746c61a27046c3176a7144.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/9de86eef643813f0384f81c34cce5a1709eb806a7402e83a20d51cd439ddc46a.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/a4c867cd3283817a1069505c2b3a47d2f011aa0d01d658d66fa3a4bbea0f5aa0.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/c2c576011f10bf011139756ee0ab96e5dedf609a4f354242d9c653198ca7b3c2.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/c3496c910e735e21369eb3b78938b2618bfbc6362ca3877988549219da30c53d.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/c9ba0902afde97941d2156ca2ee79be31656b18be647d83c8503b3dfca4199fb.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/d60d4cbbf6c3d5bb97fddbcc066d384810589613419e60ec34eda9229f8a9c84.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/dfb2d10713db8efe0f591fde30db425fade2120b66b5476253a7c568b054a2a0.json', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/e2e3157a88ea20e97fd8cc921d8a08e64178a12c0df314d6b3c00e903a039c52.py', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/binding_sources/f2fac13228af7cce764dd69e4f1f1ca3e165cfc2acca26a4f57965bc73aefb1d.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/02fa9c6d9f0ab9ede2c0442d514b335f5b021657ada94ed46e5eb0ef33f5a031.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/07dce28ca9f31d3f03559d6998b35d77c4779b70c7a5bb1424c64bdb3a0fffff.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/0922dc404713a76b19016144e9532a0e5d8b3e1fd2b149c960203d8d11e84683.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/0927ad04d7523a50a98b3ba3480b83b8fcb2963354fb6864f19c26fc0a7760d9.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/134cbee6390a6f999813dd0234fe869bdd0bec2dddbd5d47a2209091c0dcbe5f.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/15d6ad5e756548ddd1437624513b0d3b43060ba99a735b8a2ea9036449f7ba4c.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/16a38b3cd59461a347bcb7b05ef6e473f8c148ffaa341e0e5ee927527d4f6a77.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/18001b6e6218f15b146f1cafe2347893c349033e73e2d75a7b96e142a420f454.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/1dd3f40898b99f513980ad75af55c3fa9d9b99b332bb7b438fcb251ac0a6a329.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/1de6182ecb2cf58f521ff8f5f2558a51fede8d60bbbc2639c5e431b8097f66e1.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/2149bbaa3db6954ba2b516d832b98fd91462e3b923b1840d11c0ea0307e244bb.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/259ddd2707797de9e64dd6b6a955a58eb114b27afab381e9436eeeb7c99b568d.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/274119dd43f5ad046a9f532e4d2229150c72fb6f2f00fa3fec6550f69716815e.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/381d34ec60e13c02100283f751ac3ca3b26b21842af1a11b6ea474e86e7a0829.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/43699a3792072c843a11918bce090aa585591ec3ca6c132307eaafa50fd97262.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/4dd58d6860a2a2a0e73930ea2298210059a4f99e52d569846735ba3bc4cf1d07.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/5475bd67d04f14c0b7d2e0924d3139bcfc2c67170f201cc74191d2d8233cd153.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/5b84521fa00a92cb5bcf45de394aa1099ee52b333564c540286abd45dd0b06d8.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/61c7f4ac520ee1ed57733f35e27fc15f40cb347788df0db480f6703cb9c2cc4a.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/6aea7199218d76c6c809a2d44c6e1515b68663ea947d86d3c435e73b202bf8a9.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/6ce79f06293c9181470b133e666ba60003fc0f64f0675609667ae66e3d6cc6fa.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/6d0eb6e19a96167e3bb967a16f3a38f80daf2077563ac98195631c4622be6fe4.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/6e44442c9463c88fe6ef2aad75ad40a6d7b9eb9628d11e42d6adf06803906605.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/70a4803ac3bf813d85475b9b0e9e650158a9078dbad8eecc3fc5ca9955abb6b8.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/735e85c1501c220234a2e6935eab95afa47a844e35db0715e3f104c9721252a2.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/751e6273e5edce4d3eadf93c4ba83f6c59eb2b9a69df83ce6427ab892732df1e.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/7c550e22dfc0c0b99e1f20dcc1d22f20cd4ecd0ebeae8380c54080a6ac43101e.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/7f9b06e2bd539b52090e4c9f1a6dbc24bade2aa32c8dc32132c06a94d977a35a.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/85777def74d9b5e0e1c041acf43c9c5265b671cdbf5e9cf149c4f69a617da00a.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/8641cba03e079cee5b2ad81a05fb149a7aba48f49aa45b1a6e243c9078a06a03.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/8818c6ac3a11e7b0ebc1347257ac8c231f974db86af81b18dcf34791502592ea.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/92e2e9779011723e934b8b21e692501f168f4010b677ddacea089f85721472f5.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/994f9435ed1e772e8be2ce614a52569bc99c15dbfbead96c3d764de5e2e3bf33.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/9b7d3b4d1305a80c221ccfe749a5e4921def521260adbf772e07a26a1124c969.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/9b8f134b0a9a5c2131361e6e5cb99c6fad7bf7527267743cc38c50799b77ea43.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/9ef3a73f2495f26aa0fd470b29337202faa9d0cb874f28626b51045d9c504b17.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/a19e0fab5ecca54f0e31cbf6af167e86942868e6054156d35dd5c4bf9340ec8b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/a2ac0f77d5d0daf6278144a71c980e43210a21c4c7dce6699ae765e1ac8bcf92.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/a6df08142a325e928f179bab470d7fde711dcb8cc7524e0b665f9e0952db9b67.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/aad4ffbaa29dd1a4964437e93f4086fc94472a9e95b2aa37c4b0ddd33e7cc9d4.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/ab454bca5a612b8b69c24442e1b63fd44d83578c5536daaad9ade6e0ff3873aa.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/acf27628d6df223ae8432b70e707ebdc9d1dac86f71ea78cd52f800cdbdc1b4b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b1b6eb20146073ff278d12d786452eec533b4e5c16ea1750c90df9ba11c15d05.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b255fa80806059e01f087eb438a6540348ad7024f347a6baaacc9953cb1a2a3b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b495019f029b1174515fb04e8c459fe38792eb7c9413632b606fd2844cf1b0a6.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b648ac2139f59077b2edd7ccd4dc8c54888f51f78aec4ab7afff3c0232950260.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/b981b1b15d4bc75a8ab4d5d50ebd18eb5be22bfbb5d6c342545d0e337be23f99.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/bbe2e9c911e3323f840855fb2e77cc5e86d1669486eb8c8dda2e8cdec3ff53eb.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/c64f5ef88e56263becf876f92c105438f1371d0d011ee50c7edf70f151c56b6e.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/c75486365c5e4324270537f96c5a0210adfd75c9f8c8b5e25a9b6b8b7b9dbe5a.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/c79073c5d09b2235804a7596a81ec8639dd440c64469e96b835e2a5b946a81c7.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/cb55c8f137758dbab1c26693db14c8f5c5c3b3e4874846625286818e52ead6f0.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/d1d233a1f42dd6d3ca79a3d2c16eca45b2aa8f108ab4ea7adc11f31d1efac3fe.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/d4da9d90ed0ff34a7c89caad741447a02b0fc15971d511102a3e058b88a23d78.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/dad41827ab202b954d14982c3865040d74a9b1cdd043f9977ad92c6fb72fe76b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/db162743162a6811b4d245f33c7b762e2726895701f18c1baa89f8e239786369.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/dc8155a3798e8a8330cedcb3866d5e85f9480bc49e724fda7ec9394bccef2b53.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/dc8b9f0dfba5c708e1e5a494f973f503c8561c1cd7aa94b399dba279e54f437e.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/e8aafa85650d2a0a59cb6a4740a892e0895b5901f078ab634e17ab42d939df5f.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/ee5c24cc0cd75e063599661369c06e243464342e5795f3bda85e452aefa2788b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/f36120cdf7737058c4f40030e45d1a4da729be2752ee51bf6f90d4e099d88b1b.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/f3b497f3db6c64809877be9b8b547e048e673da9203e3a7d40a106d51e166d10.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/f3ed028f048f05d98e3bf474070561355cfca5b31ca48b8ed5a5d8322d24f2e7.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/f6e98cb5b38470ace605d81befd6df2e8c96e483b3e9b57c922c87e0b20e498c.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/fa2a52dcaf1d334e980b8d75e4ed187af40cee39322a944d4b72e341be1a88ba.blob', '.claude/science/physics-loops/toe-single-port-program-and-controller-20261015/source_recovery/fa848abcdd2e4f524f8cf8c346edfc83d905e036dab11a6f794beea5aa568893.blob', '.claude/science/physics-loops/toe-unary-cycle-clock-20261014/objects/8d76345b8a28d7d9a80675dda5ee8b1d3f9964994375bae852f02ea084a9a7b3.gz', 'docs/POSITIVE_UNARY_CYCLE_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'compiler_author': 'bda0be884fa79905ff81f0a2642def9e2efd5302796262f5f9eb4033b2c436c0', 'compiler_assessment': '3ad0ab6540ba9fae892824119aafa6c4e61ca16892ba3d23a7c59f95df82e7b5', 'controller_author': '0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d', 'controller_assessment': '52eb2e2dcd9fc56a7be490e193b57754bd85bfad5d585244d4a9fce947b4465d'}
EXPECTED_PARENT_BODIES = {'unary_clock_proof': (33019, 'c7a19c3acb7d731a95b97bfadc8a32e2624196d60555ac08e8e77b3ad71d1135')}

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

def compressed_review(row):
    require(row["container"]==PARENT_REVIEW[0] and row["encoding"]=="gzip","Canonical review container")
    require((row["stored_bytes"],row["stored_sha256"])==PARENT_REVIEW[1:3],"Declared compressed review identity")
    stored=safe(row["container"]).read_bytes()
    require((len(stored),digest(stored))==PARENT_REVIEW[1:3],"Canonical compressed review identity")
    raw=gzip.decompress(stored)
    require((len(raw),digest(raw))==PARENT_REVIEW[3:5],"Complete decompressed review identity")
    require(row["start_byte_inclusive"]==0 and row["end_byte_exclusive"]==len(raw),"Complete review interval")
    identity(raw,row)
    return raw

def main():
    mpath=PACKET+"/INPUT_MANIFEST.json"
    raw=safe(mpath).read_bytes()
    require(digest(raw)==MANIFEST_SHA256,"Input manifest identity")
    manifest=json.loads(raw)
    require(manifest["schema"]=="source_integrity_inputs_v1","Input schema")
    rows=manifest["inputs"]
    require(len({r["path"] for r in rows})==len(rows),"Duplicate input path")
    actual=PACKET+"/ACTUAL_BINDING.json"
    external=set(EXPECTED_PARENTS)|{PARENT_REVIEW[0]}
    expected={r["path"] for r in rows}|{mpath,actual}|external
    require(set(AUDIT_INPUT_PATHS)==expected and len(AUDIT_INPUT_PATHS)==len(expected),"Literal declared-input closure")
    for row in rows: identity(safe(row["path"]).read_bytes(),row)
    note=safe(NOTE).read_bytes()
    header=note.split(b"---",2)[1].decode().splitlines()
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false","runner: scripts/single_port_program_and_autonomous_controller_2026_10_15.py",'upstream_dependencies: ["positive_unary_cycle_clock_bounded_theorem_note_2026-10-14"]']:
        require(field in header,"Missing actual scope/binding field: "+field)
    body_map=read_json(PACKET+"/BODY_MAP.json")
    require(body_map["note"]==NOTE,"Body container")
    require({r["name"] for r in body_map["bodies"]}==set(EXPECTED_BODIES) and len(body_map["bodies"])==4,"Exactly four immutable bodies")
    for row in body_map["bodies"]:
        require(row["container"]==NOTE and row["sha256"]==EXPECTED_BODIES[row["name"]],"Immutable body identity")
        interval(row)
    parents=read_json(PACKET+"/DEPENDENCIES.json")["dependencies"]
    require(len(parents)==1 and {r["path"] for r in parents}==set(EXPECTED_PARENTS),"Exactly one direct mathematical parent")
    parent=parents[0]
    require((parent["bytes"],parent["sha256"],parent["claim_id"])==EXPECTED_PARENTS[parent["path"]],"Parent role or identity")
    identity(safe(parent["path"]).read_bytes(),parent)
    require(parent["required_mathematical_body_names"]==["unary_clock_proof"],"Only the generic unary-clock proof imported")
    ranges=parent["accepted_body_intervals"]
    require(len(ranges)==1 and {r["name"] for r in ranges}==set(EXPECTED_PARENT_BODIES),"Parent proof interval")
    for row in ranges:
        require(row["container"]==UNARY and (row["bytes"],row["sha256"])==EXPECTED_PARENT_BODIES[row["name"]],"Parent proof identity")
        interval(row)
    require(len(parent["review_evidence"])==1,"One exact canonical separate review")
    compressed_review(parent["review_evidence"][0])
    archive=read_json(PACKET+"/ARCHIVE_INDEX.json")["objects"]
    require(len({r["sha256"] for r in archive})==len(archive),"SHA-deduplicated source recovery")
    for row in archive: identity(safe(row["path"]).read_bytes(),row)
    sources=read_json(PACKET+"/SOURCE_MANIFEST.json")["sources"]
    require({r["sha256"] for r in sources if r["role"]=="root_conditional_source_acceptance"}==set(EXPECTED_ACCEPTANCES.values()),"Exact separate source decisions")
    for row in sources:
        recovery=row["recovery"]
        if recovery["kind"]=="blob": identity(safe(recovery["path"]).read_bytes(),row)
        elif recovery["kind"] in {"body_interval","external_body_interval"}:
            interval({**recovery,"bytes":row["bytes"],"sha256":row["sha256"]})
        elif recovery["kind"]=="external_gzip_interval":
            compressed_review({**recovery,"bytes":row["bytes"],"sha256":row["sha256"]})
        else:
            require(recovery["kind"]=="external_pinned" and recovery["path"] in external,"Unknown external input")
            identity(safe(recovery["path"]).read_bytes(),row)
    mapped={r["name"]:r for r in body_map["bodies"]}
    for row in sources:
        r=row["recovery"]
        if r["kind"]=="body_interval":
            require(r.get("body_name") in mapped,"Source body-map linkage")
            bound=mapped[r["body_name"]]
            require(all(r[k]==bound[k] for k in ("container","start_byte_inclusive","end_byte_exclusive")) and row["bytes"]==bound["bytes"] and row["sha256"]==bound["sha256"],"Source body-map linkage")
    selection=read_json(PACKET+"/RECOVERY_SELECTION.json")
    for member in selection["members"]:
        recovery=member.get("recovery")
        if recovery is not None:
            require(any(member["bytes"]==row["bytes"] and member["sha256"]==row["sha256"] and recovery==row["recovery"] for row in sources),"Recovery selection linkage")
    state=read_json(PACKET+"/PUBLICATION_STATE.json")
    require(state["kind"]=="dated_source_proposal_not_actual_binding","Historical state role")
    for field in ["canonical_binding","git_base","primary_execution","cache_execution","mutation_execution","graph_execution","publication_action","retained_audit"]:
        require(state[field] is None,"Historical null state must remain null: "+field)
    require(state["scientific_programs_run"]==state["historical_programs_replayed"]==0 and state["gibbs_frontier_imported"] is False,"Execution and excluded-claim scope")
    require(state["source_acceptances"]==EXPECTED_ACCEPTANCES,"Historical actual source decisions")
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and isinstance(EXPECTED_BASE_PR,int) and isinstance(EXPECTED_BASE_BRANCH,str),"Root must explicitly pin the actual Git base; source proposal has no chosen base")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding required")
    require(binding["root_read_complete"] is True,"Actual root publication inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES and binding["git_base"]==EXPECTED_GIT_BASE,"Actual source decisions and base")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_single_port_program_controller_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
    require(canonical["bound_note_sha256"]==digest(note) and canonical["actual_git_base"]==binding["git_base"] and canonical["canonical_parent_sha256"]==binding["parent_sha256"],"Current binding identities")
    require(binding["raw_bodies"]==body_map["bodies"] and binding["canonical_parents"]==parents,"Actual body and parent structure")
    freeze=json.loads(bound_blob(binding["source_proposal_freeze"]))
    require(freeze["immutable_bodies"]==4 and freeze["mathematical_parents"]==1 and freeze["scientific_programs_run"]==0 and freeze["actual_binding"] is None,"Historical proposal seal scope")
    evidence=binding["root_review_evidence"]
    review_raw=bound_blob(evidence["review"]);review=json.loads(review_raw)
    require(review["kind"]=="root_source_publication_review" and review["root_read_complete"] is True,"Actual publication review schema")
    require(review["source_draft_freeze"]["sha256"]==binding["source_proposal_freeze"]["sha256"],"Reviewed proposal identity")
    require(review["decision"]=="Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.","Actual publication interpretation decision")
    require({r["name"]:r["sha256"] for r in review["body_pins"]}==EXPECTED_BODIES and review["parents"]==parents,"Root reviewed bodies and parent")
    require({k:r["sha256"] for k,r in review["existing_source_acceptances"].items()}==EXPECTED_ACCEPTANCES,"Root reviewed separate source decisions")
    require(review["scientific_programs_run"]==review["primary_runs"]==review["historical_programs_replayed"]==0,"Root source-review execution scope")
    _,result=execution_evidence(evidence,True)
    require(result["review"]["sha256"]==digest(review_raw),"Actual review output linkage")
    require(result["members"]==178 and result["sources"]==107 and result["exact_functions"]==25,"Actual reviewed source counts")
    review_seal_raw=bound_blob(evidence["review_freeze"]);identity(review_seal_raw,result["freeze"])
    review_seal=json.loads(review_seal_raw);require(len(review_seal["files"])==1,"Actual review seal membership")
    identity(review_raw,review_seal["files"][0])
    require(binding["gibbs_frontier_imported"] is False,"No Gibbs mathematics through Git ancestry")
    receipt,observed=execution_evidence(binding["base_observation"],False)
    require(receipt["argv"]==["gh","pr","view",str(EXPECTED_BASE_PR),"--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual base observation command")
    require(observed["number"]==EXPECTED_BASE_PR and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]==EXPECTED_BASE_BRANCH and observed["baseRefName"]==EXPECTED_BASE_PARENT_BRANCH and observed["state"] in {"OPEN","MERGED"},"Actual base PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding["base_observation"].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(path in AUDIT_INPUT_PATHS for path in used),"Binding evidence literal closure")
    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and captured binding evidence only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: literal source coefficients and scalar ledgers preserved; no gate or physical element run")
    print("per_site: one-port and exterior NN supports preserved; installation and isolation remain supplied")
    print("per_mode: one-head clock and full auxiliary-sector distinctions preserved; no simulation run")
    print("per_block: four unchanged bodies, one mathematical parent and separate canonical review checked")
    print("lattice_wide: no native initialization, Gibbs frontier, common-cap, detector, reuse or retained audit certified")

if __name__=="__main__": main()

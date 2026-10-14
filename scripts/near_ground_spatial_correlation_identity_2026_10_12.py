#!/usr/bin/env python3
"""Source bytes and publication reconstruction only; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ['.claude/science/physics-loops/toe-spatial-control-20261012/EVIDENCE_MAP.json', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/02170e730a59c4b2a90918e3b3242f2b25f19af7e99e9b3cdb99bfc3d17c9616.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/025d4cd4eb9ba8ddfd0386ad7763cd61dd2eea681257a8cd26f6e53f0018f87d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/034ac8597df673ebc884a57f04627f196458b1945d689ec70c3f849c94ff6946.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/04ed66bc7b814ac855a935477db7883e656dbd9547874f458a446124634fad7b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/0a5e693a1cc00b53019fa2bf5f0878ff65eb77d5d2b144e1bd1e21c4715cc517.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/0baff703e54032d4d9aeb248d526df5e44815f7fee442fbb947fa389492b1541.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/0f34e11f5eb78f8ade42bfb53e1196a3dc863acee053426130d78a14aa3b8ac1.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/10c2bdb8e6e2ee65c0f85184cabc01f101f77b5b8ad1dcd3825e212fa9a9b185.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/136973352433c96e29b0b72562f12580ac8cd18a2f6cf84f9320dfa219d0ec34.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/1609311a6ac4baedae4a339b89498a013072021b94a66cbce01bda5e79995625.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/17944ad6520cab6e76f471c60dcc71cf662a4f44bd0867842789afee3befed1b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/187a92ac17ed9afd70e6a90b8e08a6d1cf6a25e93b416c9c3de20f3e45a8fb7d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/1d7bc9535d9d343fdf1b4e4b316102e3c5fe0649b20c4bddd339835ce070afe7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/1fbc1686e4758d8322a3d2c8bcaee5edfccd149644561dea2425220600f4cdcf.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/2091a39b31196b0cfbe3dcc5cd21b6872cec16538d979f6e1bcaee7b43fc7899.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/211679c882c33aebce693893328df3e597df8a130e1a68812db51172845beebd.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/22b57614cc79fe7db0fec7d5861363da64b1bda205a93f153acf274c28c5910e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/2311c445bffc809d3387089c0feb48892f15f535d889121664dabe49fa146b05.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/24046331fa3dd3a57ed5c574bdc36c41c4d2496dbbc850dc3b8193bdefee88b5.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/2412f37eff2cf2b8aed7b320709f50d5d95d159bd6436007286c084bfbef1d56.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/29af13602f055120f50294e43be3e8dc24b2e79506dc14a059ccbb27cfa7ee3d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/2a0254507a0b284df93dc62509a38cd61c8a09c4415fbd4a5338050fb5c1b91e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/3160cb7d2571e3bdbf5e9467c2d23521d31d624106fac1e440c0a8732ac017b9.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/3cbfd959a174462949090b01357f68fc550c654d6fd25a87f8369e86733da165.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/3ccc98a7a03d1617476bd14d25e3a64f20b33c12c0ffd16e9aec06fe0e88a76b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/437f4cc151e2437a898edf03763344637820d71b8c9bd10568b0f4374346a6f5.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/46c9f80a78925e57a2d5234b7baa64f87886d54929f474165af11c4e2d15006f.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/4b040fd09ecfebabf807c9ff83c2ac665eeb3c34f668f4e29950f17cf2281727.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/4de1d92d287731b1753b4d27189d7f58f34676acd4fff6a2ebad000532f6e984.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/4e1868e2d52f2c11a2bcb2c5fcfb7a9702560a6a1ac8ae50bc699a2c30dd344a.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/54d4cdbbb3659737f19d9e7877c0e4db68d12e7f02a21de2c9fbf4ae0d6d31b5.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5629d0dc77809ec65e74a1c419f8542ee0f5b261560bc29a19107d1f932508c3.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5806e54f98639830abfbf1f269ccb205ecec86a14dff850960fef0dc1352645b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5ad4b69afb27fd1eea6d84d82dea1b11b35056185451031db250572f9b28e83f.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5ba55c1d3afdde70ab04cded92e325d4461e78fb87c7d7d770c17447e2d1ba8e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5bd208bbaed5a62dfd73515988fe15dfafd2f4de157acde269258f7be784c76f.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/5bf44abe2d7d4896bd239f23c8abafb740c2a89d974fc75bfb02bdf2d6cbf36e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/606c7b92e73d86b2e72714e0b108818af42f6b5a6a7c1f8dc111204a1a6768aa.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/63a05c0e93e920705dc409e9b703a1a2f85412cbbf17532bd059a7f20102785b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/63f23b76814e6faada8506d42407d2b8be1ed027230959e624213b32c86e675b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/64e32c7f8382aeb375135c78f558baec64ff205316dcab62d2e310ea695c7269.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/667d2c11f903ff92e0f3ecd06ce0fe07d3746c7206afc14c500c4fe5b07f6f01.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/6d8908844934ba219c37216a137a7b8181b01e2f1414144c972e5e1cfeb701ef.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/729b719e680fc6eb641ab4ffe3f2218a1ee624b3dfdae5227cc59019f39afbc8.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/777a267401ac0a77891bacac0e2d10767d6cb97f17ebca6d9c90922394c10f33.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/79f2c951b7c9319865e09a10950c73e235cbefa08de73791595f5ac940568378.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/7eafe7c9837af5574dd729ce7acbda924c9c43d4a007bc805ea7f55c3a599ee8.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/7ec62ba1e2b3df609bb39c430653e2ca198da28ca1a5355e616ffc469db866e8.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/80408b062fef6767239736c1b255dfbc3c4cf37f0ab6e5cc978cd9a34766f8ba.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/83f067508692a2c5e9ea9311ad14f4affd66122425f936a6ea8c27d40419bbad.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/85f80a3a7c9689af83e485acfbdd11ae9fb98babbdbf38518b1240f0be6db30e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/863fe5ab95757ec1e24fbb8e8d70ac4a71384e9f663ea1a7ccf1129708baff43.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/86a39b4f7758a81900c95c450582c2c7cbc2e012f12bd05004b4fbe9db452ed8.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/876ef78f41752c3be2b9d2a49aafc215b815ac1dc911ef93318d6c38da4994d1.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/88a065965ac148e6173b931095937f917be6705267605a4ef1bd033f22a406ae.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/8938b93e4fd5cffa9919556cd68988a1ee44cbc98066c897977e5bba1db253ad.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/8b3ccd28f6fd0149df2877e7ef34f164d122304de56a3482e8826d516158a6ac.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/8c54958ebc57d721b56c12b947656e20652127385fc55d5eafac92aed73c191b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/8fdc997ce1735a7a132a2fe21732e5f9c9197ac386ea7dd0b4e4a1aa7269702e.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/9020ba5c2797d8f026ddb72871b13f18a18cad4e0ec326c0f4653ceb438751bc.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/9200dbdcc460848d6d3c359a0cf8c04b755caf391d607bb7a561ce2307c3e79d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/93553c410da517f665486bcdbd233f5a6841a5ce5c5ac60a402890875eec05e9.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/97b751b759eed816be489c0d1b993b2abfa4124843edb2c08fac79572be43793.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/a1ed1a8202f12727842d80633cad5315bea6da421f03cf98f999f7abf09e1acf.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/a20d805ad31393dd1fc5aa67cea330f330bd71eab7d4c04aa61171b4c9b2f665.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/a8c6146e75f1acb88666dd045aed75f0f70d34f405fefe457ea8f58994bcb615.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/aec4843a8585e1e9c08989e92b25d2d98e395af3b641a75abb13dc3e3d0b0854.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/af0cf7d6e9ea98fc92ac86df651c136cb2766f40571b814b69f3850304ebfe53.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/afe4cee20ea88109fa3e89ab05325f30a0403f8fa2ad30773fb90c30ec3479e6.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b11498c9589c5bea2aa57b4d4b79c11f5ba296c540f612ee270184013e96eee3.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b316b084ec3a9c106af5026d53783dabf401d23a33cb634f090a67d37143d225.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b6724a8fb761a891ec10571ee9b549b3f2db26e300a99ba8c153181dbb363ad7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b6f1694e01ad7fb447fb0d9ce2ecb7b67264205437797db58f26ad0fa4a7f1d7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/b8bcba769100bf819885937d850a7bff8543e4233c1df3cf65f68372552160e9.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/c2153751865f9bd9742d98596d7a58f741a631543ed327f6ac63bd946610e214.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/cb66c34f21d197bd04bfd791647fa38c300f24d55af5e9f1d6bd712b55402fbc.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/d017465a571bf6e17678d533a276a527dad21aee5332b1a4296fabdba6b771bc.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/d1a990891510fb52f80c7eaf8b005082b03f9b9f82cfc2dc86588acf4d139719.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/d380b1eb915aac41da20bf690225987312b0d89e602b985dc254bd3f8e6b7f48.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/d6872270a49203644ab9f57d0e86a54d1ef3218df2a5b63f1571f965973e449d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/d8caaf1056853a1f6917b8d30f0400a1e0a25347a02ac6f2309b381c0356d73d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/dd2862222f8501620d97adbac6ff2c2f38751a24043e09c34acc8bc6c162dfca.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/df4e1a20357554d15f630faf5bab3c37f758097fe7c66e93572ac3b9b792ccae.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/df8d5785933c0fcca37aa36b8ad537a17ec0e2ab59bac258a67b705bf8703805.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e21fc0184877fbe1c607d0dffd51803286621fde3f0bd54f4201ac1f98c5d319.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e4a0f999ffc4cffd6ca53476a047acfd08de284444f02de8698f754cfa8a4d8d.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e4e0f0bdc67f535c0ad4debdbcbe2a96c2d650c4d64a543536c52bcdd86189c7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e6b5eed3fba068589aed878b6eb4aa02176a666e62621a7a319aa0534c212d45.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e71ed20836992d1d88ce0a36d7280178bcc5cf60a0403ad5d250f23bf3a6faa6.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/e9fd773c5eecc2e20b6d5d43cc197280ee8b0a0e9502c1e9c8f495f40d91df13.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/ec7b6abae6b69a35cde008d337814281e156be92abadec04877c8c33eaa65754.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/ec957c9afc62192a4c6b9be46775a04f7a42b02cebb7c9a7ebfc89491be67d84.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/edb9b78838be7d57e653e54def1c59d7c6cb85383f600533f9c188a70c76ef6b.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/ee9598de29d55b3ec7e26c38095410d1577ec1e3d8364b71fa8c20b6bda5dcb9.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f1bfb9df80e15cea5e0cd8b340750d2bbc360e062c1ae6d83269e15e5f5d8338.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f4b4c87a0be81f8b803d3bb2de0541ca006bd5b34aabcbeafc7e8d1c339b70e8.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f7ba2eb41d45a74a095cdc5d3e3a847bf496b4b687984048f75b83f4ca20edd2.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f7d28a845311c6a87570ce20439378abe80e957563a1e8a9bf29fe0d46ab78d7.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/f9e325b2ff13a6de5d5ecab841050ddb77471dc0092c42a15382e8527c8e45bc.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/objects/fbd7cba6978428409a88e2063440491917c314d67d776d61ccb01cf4902a9b5a.gz', '.claude/science/physics-loops/toe-spatial-control-20261012/PUBLICATION_EDITS.json', 'docs/NATIVE_LOCAL_ALGEBRA_SPATIAL_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CONTINUUM_LOCAL_GROUND_SPATIAL_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/NEAR_GROUND_SPATIAL_CORRELATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-spatial-control-20261012/PARENT_BINDINGS.json', 'docs/CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/BOUNDED_INTERACTION_GROUND_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/ADIABATIC_GROUND_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-12.md', 'docs/EXCITATION_PULSE_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-12.md', '.claude/science/physics-loops/toe-spatial-control-20261012/SOURCE_REVIEW_STATUS.json']
PACKET = '.claude/science/physics-loops/toe-spatial-control-20261012'
CLAIM = 'near_ground_spatial_correlation_bounded_theorem_note_2026-10-12'
MAP_SHA = '10a391d0b046fdb29437558bd74540eee979d920882b534eda15e9e640617079'
EDITS_SHA = '2b48c0e1257e44210cfe732819506475b2865bc7135e23fcaaefe76354e2d88e'
PARENTS_SHA = 'fce48863471ee803f151ac3da54362e8087daac8903a87dafc0b37344b242e84'
STATUS_SHA = 'a81b72082ad6a58b9bbad196738d9bfd98ae793ab3bb55ecd6bb405c3a084904'
SOURCE_FREEZE_SHA = '64e32c7f8382aeb375135c78f558baec64ff205316dcab62d2e310ea695c7269'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


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
    need(contract['freeze_sha256'] == SOURCE_FREEZE_SHA and
         origins[contract['path'] + '/SOURCE_FREEZE.json'] == SOURCE_FREEZE_SHA, 'Accepted source freeze differs')
    original_freeze = json.loads(contents[SOURCE_FREEZE_SHA])
    need(original_freeze['files'] == contract['members'] and
         len({r['path'] for r in contract['members']}) == len(contract['members']), 'Original membership differs')
    prefix = contract['path'] + '/'
    expected_source_aliases = {prefix + r['path'] for r in contract['members']} | {prefix + 'SOURCE_FREEZE.json'}
    need({p for p in origins if p.startswith(prefix)} == expected_source_aliases, 'Source package aliases differ')
    for item in contract['members']:
        need(origins[prefix + item['path']] == item['sha256'] and
             len(contents[item['sha256']]) == item['bytes'], 'Source member identity differs')
    source_manifest = json.loads(contents[origins[prefix + 'INPUT_SOURCE_MANIFEST.json']])
    need(source_manifest['files'] == evidence['source_copy_pairs'], 'Original selected-copy inventory differs')
    for item in evidence['source_copy_pairs']:
        need(origins[item['origin']] == origins[prefix + item['copy']] == item['sha256'] and
             len(contents[item['sha256']]) == item['bytes'], 'Original/copy pair differs')
    literal_map = json.loads(contents[origins[prefix + 'LITERAL_SEGMENTS.json']])
    for item in literal_map['candidates']:
        assembled = b''
        for piece in item['pieces']:
            part = piece['literal'].encode() if piece['kind'] == 'separator' else contents[origins[prefix + piece['path']]]
            need(len(assembled) == piece['byte_offset'] and len(part) == piece['bytes'] and
                 sha(part) == piece['sha256'], 'Accepted literal-piece boundary differs')
            assembled += part
        need(assembled == contents[item['sha256']] and sha(assembled) == item['sha256'], 'Accepted candidate differs')
    raw_edits = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(raw_edits) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(raw_edits)
    need(edits['original_body_edits'] == [] and edits['source_freeze_sha256'] == SOURCE_FREEZE_SHA and
         len(edits['notes']) == 3 and {r['key'] for r in edits['notes']} == {'native','continuum','near'},
         'Publication membership or literal-body contract differs')
    for item in edits['notes']:
        need(origins[item['accepted_candidate_path']] == item['accepted_candidate_sha256'] and
             item['mathematical_body_edits'] == item['literal_metadata_removals'] == item['literal_citation_relocations'] == [],
             'Accepted candidate or no-edit contract differs')
        assembled = b''
        literal_hashes = []
        for piece in item['pieces']:
            if piece['kind'] == 'literal_source':
                need(origins[piece['source_path']] == piece['source_sha256'] and
                     piece['mathematical_body_edits'] == [] and piece['historical_status_and_exposure_bytes_preserved'] is True,
                     'Literal source scope changed')
                part = contents[piece['source_sha256']]
                literal_hashes.append(sha(part))
            elif piece['kind'] == 'publication_wrapper':
                part = piece['text'].encode()
            else:
                need(piece['kind'] == 'separator', 'Unknown publication piece')
                part = piece['literal'].encode()
            need(len(assembled) == piece['byte_offset'] and len(part) == piece['bytes'] and sha(part) == piece['sha256'] and
                 assembled.count(b'\n') + 1 == piece['first_line'] and (assembled + part).count(b'\n') == piece['last_line'],
                 'Publication boundary differs')
            assembled += part
        original = next(r for r in literal_map['candidates'] if r['claim_id'] == item['claim_id'])
        need(literal_hashes == [p['sha256'] for p in original['pieces'] if p['kind']=='literal_source'],
             'Literal body membership/order differs')
        published = read(item['note'])
        need(published == assembled and len(published) == item['published_bytes'] and sha(published) == item['published_sha256'],
             'Published source does not reconstruct')
    raw_parents = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(raw_parents) == PARENTS_SHA, 'Parent bindings changed')
    parents = json.loads(raw_parents)['parents']
    need(len(parents) == 6 and len({p['path'] for p in parents}) == 6, 'Live parent membership differs')
    for item in parents:
        data = read(item['path'])
        need(sha(data) == item['published_sha256'] and len(data) == item['bytes'], 'Canonical parent bytes changed')
    raw_status = read(PACKET + '/SOURCE_REVIEW_STATUS.json')
    need(sha(raw_status) == STATUS_SHA, 'Review scope changed')
    status = json.loads(raw_status)
    need(status['no_go_packet_pass'] is False and status['N1'] == status['N5'] == 'pending' and
         status['spatial_source_freeze_sha256'] == SOURCE_FREEZE_SHA, 'Formal packet or source status changed')
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
    print('per_element: checked and not executed — source integrity only; no Clifford averaging or field identity was proved.')
    print('per_site: checked and not executed — source integrity only; no boundary sum or interval-algebra norm estimate was computed.')
    print('per_mode: checked and not executed — source integrity only; no spectral measure, gap or filter estimate was computed.')
    print('per_block: checked and not executed — source integrity only; no ground response, parity support or near-ground theorem was tested.')
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

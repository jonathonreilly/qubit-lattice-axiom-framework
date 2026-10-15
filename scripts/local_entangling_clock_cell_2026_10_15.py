#!/usr/bin/env python3
"""Bind two analytic sources and all archived attempts; execute no mathematics."""
from pathlib import Path
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015'
NOTE = 'docs/LOCAL_ENTANGLING_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = '35e1f7a4283c98682001fb9b18bf938a7139749a86ff4fe640e3e97242e0ddf5'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/BINDING.json', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/010c0c0deba4705490424d83b5478f520a1971a1ed9d0e14898f0765e4f9e04e.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/020c43e091122bd02163c2480ac75358fa788f6ada1050115cafe83b8f032e96.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/02f4c819bad0a2c93b7f935522da71cfebdd3bd2a1628a7af97b5fd6ba1d795e.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/095d52f674c03453185afdd7126c526ebbf075e47b98a0c0d93d00599183cca5.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/0cec848de750534e46fd93a58a2c19d5646a48fa200c7e01a4d69f9faead75f5.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/12be9b00df013c81b8111b92b139a72d885d03cf81db258671a436f3b224e4b6.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/16868d7e340d94352cc667c594bec36a654ed0baf0423eec63c4fbedae56129c.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/16cc344c5ae26e0f8edc3465cbc57537898b8171080e542cddc47b88f91c5998.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/1fbf026317d6536dd197de580e07d9518d80c67e1bfdff0613b96978072c54f2.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/256f12b48ced6fafb78bf72bfe091687d59ea30bf3f37ccccb3a7ccf6195098a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/273519a163788928b653f758fa4ef89beec51c46871d2c1d26c48862c69b4171.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/275f6eb9135f1850d246a5cb735947f856f23741f049bc9f327476aa46f96c2a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/2c95a969f8d8f40f4190ece9f25d811c7e204a4f68de722f3fe393265b2c8115.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/31cf01981e2d8f6a98bda20339241317c1000b9920e3a34898ff8e351e0bdf87.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/35da19d8c689c01af0c9a3822b66f1f056aa7d445bd1284391cb64db3f8b01d1.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/386cbb1b43f7798d08534d0b69b6740a5aa9016bc5f34d505f5f027a9cf84acc.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/3c66d664f872257c8ee205ac26c929c83a2ee9c1e1c3ecad84e979ef47aeda42.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/423572fb1da66ed2811c553b8f8929efd4676a26e47a9e03e51403fe2b899c10.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/42869965e7cc6e6cd01bd201ad6b84c0a37682dbc0e6298899e938016fa9cbde.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/45eaf95001d009c391e4ca8e703f24ee54a99a76c9bb044c4ae1d7326ac09d46.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/46fddea0d6ba3492b2c1229c78a2f7ceeaaef742714409219a87cbb1868a553b.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/48af0ae3e94c5b1b9099eb0e0c9d4911e10eb30cfb1f48ddc63b02d6400396a5.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/48f52a510848e371621c1f825135328c2bc31280250795fba81824a4235aa841.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/498764a95ab6ff0a0013d9a4c9d5c6979f3de641984e4e67038741f99596db9a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/5051ffa2815029768e288ba4df154d27f2fca06c1512718f496a8686031f2724.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/51f8cf10199e65cf48de5b17f460dad0427a741e2e6f86e39ef3402114e5cf65.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/524544ffd82245ef28bd62871431f216cf6780126e2be570ef700375c9e95bf8.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/5732d498807ff8264f561a3c36520491950b285ce3f9862cc0b0567ffd48aeb3.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/5e5db9b1803f4f9996c2fe011b3505811dd2aeb7a4ae1c0929a4310c60d19b3f.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/602109014f8e022e168880535a5d37488c1ff6ced86492fa21de96cc456bdea5.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/6085f0118c8eb7fdac3b757f686f00e3abde4b48ea1ac6883fc42d954c42a543.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/613788ebb160033dfa5cb69955d183cf19aab3643169ada4b10aa61f2083de60.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/696f0fd4bc8b5ecbfd2be17c160daa152a960163ac939d1efbc311cabb98b9e4.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/6b97fef971c1755d1f5a55b1cb93c81fe21a443ff1e02e60c2d0bb9e25162655.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/6e1aebf3385e1188dce918b3837f0a2db75258e9f95a21fff8224b8050f1420f.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/70f8bc054b2e2d7f0ee014458a434d5d5132e74aade64d535c484fdddde2049e.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/718e56be97847c82934031d8ca56cb2773dd975a439c2e65f5f4016330b85a67.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/71c3bc48a4dd461d29002a7add5727d5ea1e3e1ff1dff370341354917c24b679.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7290d37e3f338fa1b64bc7691bf428eaff6109ffbb312f9ddebd13c349c12661.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7341eb3e16cd8866fa778fba5b8df9cc8d148212d537b64e9bbadb763035f754.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/744535009b26921d07b32b421c9f6a134305e907d8ca185b5341a3b0dd2b11e1.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/74549eeaa060817c3738bb7ea9945386710a6403f02c9e0d7a0065d6efdf51d0.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/746dde655f8fd9868e0c8c932804f7d7c6a11e12e23f8a7ac8e79dec67586462.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/754dfa75d30666c39d709f3c5a57db0e48f9430625249d94dacf3c725b507394.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7c637c3367b32bd666b694b65cccd76dfd90a94d8e27ff7a87ce05e54ea7748f.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7c80ee433e47f3849ac841d6b2f4750831ae3aa39dd041c74da3c99eb9cb9394.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7d3fcdcc0c035f78c5d43f4fe7517ad5818350e749f7a442a7a4b8a57604df38.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/7ee8fd4ee179f701f75d96f6e3881aa801bafc1aa8bf280287c6cb3b85bcc279.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/814d0faebc386b2bf8873defb9da7f8cf6b0f90fe94e7f400c5b3ebc0d52eca9.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/81e207b81b1137ca1535c73b22b26ba3b803ac5633d6320571d8813973f3f0b2.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/8670135c7cf4b3c6725e36c3cbab1ad0f54bc847a54861ac009b1ae2c4f683cf.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/8831f7bf0398f59780ca965539d9c9be70ec9137add5c3d6d219c895c3fb79b6.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/8a1a6d00e00e4754ff3b79c6bf1fc83bd32df0200b1d6194dc6d67dd26636197.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/8c245229d3dda3176d8ea058e1ed00c28b780e52ecc2c484c2bbd4ca95e815bd.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/919131c6a496fa4349fee090f454da0c582142ba8736bc4c01497792433430d4.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/92568d56f3ce7e51f4f479329b8c58c9f12d5f814876b10516ac7a91ed46bbcc.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/929808029a58f93360b83fa3adb473a749cfd8bcb5fc8e80b2165d3aa0133711.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/96d26a21e761bc1dd32015a33393c337c182c8cb215b3e3ba931ba41be2df070.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/973ff5af0bfad3116be8c71a6f804e75c3d5d1664f46969bc9354868d140af70.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/9e5150908f5e876b34de645dc332ebf716fd8467223934017afe800cd5315dd8.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/9ed008a6c12207dff383d4caed39c6b22bb5388f3372c8691b3816cdc7de18ad.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a0d39d165e5ea80db623103ebd4e28b50dae87a6122ae97bbe954e9979bba789.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a2b29297b855ed78499f0b758ca8f247cb9ad29457a438d220cb35cc3d60703a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a421a2f1d7f094516ee3a8c247b4df685ec0d3896a39ad1b8ba42feefea7f18a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a56690ff50a62d2e0dde30655d94c30eb57dc65fcaee188f7bd00e9ccdb63be9.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a7c6aa437b88cc89a91552de7b32fb185a2867bb91332d268a847f678596ed25.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a84adad3143a295f18c31af08a6c28d429a13f6b4b4159681952f5627339cf1a.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/a8f3611be2422878a4fbdbfef7d70ac9af9a3e5bd287b42f4aacb205ae08dbf8.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/b144943b0bc103fe59f4678a1a57ce9d6c64b6f7c273dc5f5c867bccc3f0f334.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/b1514dc2533da7d246cba88eeebf3faf991b32ce041ec1e5f9f1be0441baab2b.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/b84746b21ee6d380d75eb479f98b8ffdf039add060eca1cc171c403832ec10fb.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/ba43a48f0fd7a2289449c13d9cb3149d1db250cb42d803cb944e1e9be8cdc34d.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/bb3a4764729ad9c0fa73401b9dc0cce83bf8098e17380041d2e0494066eadd17.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/bcbef5af221a5feeeb04f291a71d2ce7c3410d50fb7441d50135ca5c98ee9353.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/bf83b30a4610b0e079821738984ff6e7be5f374da97e4ef778c224eea21b4644.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/c1e4f65f1548b66e005e5b06a3578459a2505ee867e885a21717cd8d01cf2893.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/c20291887b2a4dd00244bdc6a0d165ddef7a6f72c63cd808cc037e6a1ad58d13.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/c2f8698070bd003ece8f2ad03a4241837c05ac7c520ab9267321a7965c134331.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/c8aeb64e92b743542c1154a5e8554e66f18d3d20629cfec455ed6b2ed6314b6f.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/ca283a84b45c5e469346552cba905b0ec14dfd18e31e77b031ea064cd1a8357e.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/d27e37865eea2667d1b2caff45c68c3bf7299e7516e9477cc553b1ddbd469654.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/d28908933397eb710c323d3d25a3eef6db944afb51a60677741e3c55a4c5ceb4.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/d2ec9666530c7f0773243a41b83d0696909cf0b517435c908770ecc9012c9664.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/d2fe7f7ca1763980e3eff85fd124580954a3b4e5d54594f32217920e621bfca6.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/e3985930b9542d48a21e411b5e678b1422f1aa12ee7c095cc30627c246e00cec.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/e7cc1ef809c803bd1db16d8fb5510d19b5082e2acc1d56e355190298998f8229.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/e942bfc2df7e8c67b731c5b02847c3911086edfe7f5ef440e06b1a1d7031b598.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/e94ad7222730fee0112179daf620b7568f5866f4369e5726734ca7d3a231b446.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/ebaeebb9d6616e083d6e14ea5ee35120ddce48007866803ae682e00b8309b989.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/eeebf72d6e84bc787dc963553fe3b68033a375db78e5b0e114b881f5aded1290.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/ef22835854423c0f48e2cb717742b63071abe6b6d13a56a4408bb61fb1627413.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/ef9ed26d229c22f5be2f079fc31d3ccfbeb4e0d696a2aa3e6c7e0b892787c988.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/f02e80d2c69be61819c9fc43a8a3125cc1432f895c01b93a5e7081ec2b4d8755.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/f1b1bf41e22a651328dbb78a3137b66b75b6c431e00f54255a7194939c1991fe.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/f265b5600d8b86d8c6f9dfcf3c9d4017b9d7004036caf50307f0f3acf6b15b35.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/f50db4f3963186fc04fdda9b0459039e3645e61f2a8dc7b2687b42ef7e8b4f20.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/fc334b523b528a117e217fc7e1fd716e4cd656055f5c946a5b7450c01cd684b1.gz', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/archive/fe12497ed164d94c1e45ca4c3e260d7a10fe5b0c0ef1a7aaa5c0c75dbedad319.gz', 'docs/FINITE_RANGE_CLOCK_DATA_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md', 'docs/LOCAL_ENTANGLING_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/SIMULTANEOUS_MULTI_PORT_THREE_PAULI_BOUNDED_THEOREM_NOTE_2026-10-14.md', '.claude/science/physics-loops/toe-local-entangling-clock-cell-20261015/INPUT_MANIFEST.json')
EXPECTED_PROOFS = {
    'local_entangling_clock_gate_domain_revision/AFTER.md': '2c95a969f8d8f40f4190ece9f25d811c7e204a4f68de722f3fe393265b2c8115',
    'local_entangling_clock_gate_independent/DERIVATION.md': '6085f0118c8eb7fdac3b757f686f00e3abde4b48ea1ac6883fc42d954c42a543',
}
EXPECTED_CLAUSES = {
    'premises/be8_raw.md': (
        'docs/SIMULTANEOUS_MULTI_PORT_THREE_PAULI_BOUNDED_THEOREM_NOTE_2026-10-14.md',
        8389, 32138, 'be8f8d49362f5d9e363bd1df8b70b6e46b475beaa52e9ee5e18e0bece4293ddc'),
    'premises/mediator_raw.md': (
        'docs/FINITE_RANGE_CLOCK_DATA_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md',
        7032, 35421, '8831f7bf0398f59780ca965539d9c9be70ec9137add5c3d6d219c895c3fb79b6'),
}
EXPECTED_ACCEPTANCES = {
    'local_entangling_clock_gate_root_review/ACCEPTANCE.md': '35da19d8c689c01af0c9a3822b66f1f056aa7d445bd1284391cb64db3f8b01d1',
    'local_entangling_clock_gate_independent_root_review/ACCEPTANCE.md': '256f12b48ced6fafb78bf72bfe091687d59ea30bf3f37ccccb3a7ccf6195098a',
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_inputs():
    raw = (REPO/MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'local-entangling-clock-cell-inputs-v1'
    members = manifest['members']
    assert len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS) == set(members) | {MANIFEST_PATH}, 'declared input coverage'
    data = {}
    for path, row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b = (REPO/path).read_bytes()
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'input identity: '+path
        data[path] = b
    index = json.loads(data[PACKET+'/SOURCE_INDEX.json'])
    assert index['schema'] == 'local-entangling-clock-cell-archive-v1'
    originals = {}
    for alias, row in index['originals'].items():
        assert row['stored_path'] == PACKET+'/archive/'+row['sha256']+'.gz'
        b = gzip.decompress(data[row['stored_path']])
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'decoded original: '+alias
        originals[alias] = b
    body_map = json.loads(data[PACKET+'/BODY_MAP.json'])
    assert len(body_map['complete_proofs']) == 2
    assert {r['alias']:r['sha256'] for r in body_map['complete_proofs']} == EXPECTED_PROOFS
    for row in body_map['complete_proofs']:
        raw = originals[row['alias']]
        assert len(raw) == row['bytes'] and digest(raw) == row['sha256']
        assert row['end']-row['start'] == len(raw)
        assert data[NOTE][row['start']:row['end']] == raw and data[NOTE].count(raw) == 1, 'complete proof interval'
    before = originals['local_entangling_clock_gate_domain_revision/BEFORE.md']
    after = originals['local_entangling_clock_gate_domain_revision/AFTER.md']
    old = b'and single-qubit Hermitian Paulis B_y,C_w.'
    assert before.count(old) == 1 and after == before.replace(old,b'and nonidentity single-qubit Hermitian Paulis B_y,C_w.')
    assert before == originals['local_entangling_clock_gate_candidate/DERIVATION.md']
    binding = json.loads(data[PACKET+'/BINDING.json'])
    clauses = binding['exact_source_clauses']
    assert len(clauses) == 2 and {r['alias'] for r in clauses} == set(EXPECTED_CLAUSES)
    for row in clauses:
        assert (row['canonical_path'],row['start'],row['end'],row['sha256']) == EXPECTED_CLAUSES[row['alias']]
        raw = originals[row['alias']]
        parent = data[row['canonical_path']]
        assert digest(raw) == row['sha256'] and parent[row['start']:row['end']] == raw and parent.count(raw) == 1, 'source clause'
    assert binding['conditional_acceptances'] == EXPECTED_ACCEPTANCES
    assert all(digest(originals[alias]) == h for alias,h in EXPECTED_ACCEPTANCES.items())
    assert binding['binding_complete'] is True and binding['stage']=='root_bound_review_milestone'
    assert not binding['root_runtime_freshness_and_feature_binding_pending']
    assert binding['observed_base_head']==binding['feature_head']==binding['source_head']=='53be395f790a96a42f2d58c448f7a95b193580d7'
    assert binding['observed_base_tree']=='d27914669cd9411e96c7bc1830cd5be2e5aaaec2'
    assert binding['base_pr']==9587 and binding['base_branch']=='physics-loop/toe-local-pauli-clock-cell-20261015'
    assert binding['branch']=='physics-loop/toe-local-entangling-clock-cell-20261015'
    assert binding['new_scientific_programs_run'] == 0
    assert (binding['archived_selected_fixtures'],binding['archived_scientific_attempts'],
            binding['archived_successful_attempts'],binding['archived_failed_attempts']) == (2,3,2,1)
    assert binding['base_is_mathematical_dependency'] is False
    assert binding['external_residual_theorem_imported_for_cell'] is False
    return data, originals


def checked_archived_runs(data, originals):
    records = json.loads(data[PACKET+'/ARCHIVED_RUNS.json'])['scientific_attempts']
    assert len(records) == 3
    assert {r['id']:r['expected_exit_code'] for r in records} == {
        'four_rail_serialization_failure':1, 'four_rail_serialization_retry':0, 'compact_exact_and_float':0}
    receipts = {}
    for row in records:
        receipt = json.loads(originals[row['receipt_alias']])
        receipts[row['id']] = receipt
        assert receipt['exit_code'] == row['expected_exit_code']
        assert receipt[row['start_key']] < receipt[row['end_key']]
        for stream in ('stdout','stderr'):
            raw = originals[row[stream+'_alias']]
            assert digest(raw) == receipt[stream]['sha256'] and len(raw) == receipt[stream]['bytes'], 'recorded stream: '+row['id']
        pre = json.loads(originals[row['preseal_alias']])
        assert pre[row['seal_time_key']] < receipt[row['start_key']]
        for member in pre['members']:
            raw = originals[row['source_group']+'/'+member['path']]
            assert digest(raw) == member['sha256'] and len(raw) == member['bytes'], 'preseal member'
        pins = receipt['pins_before_launch'] if row['launch_schema'] == 'relative_list' else list(receipt['before'].values())
        for member in pins:
            rel = member['path'] if row['launch_schema'] == 'relative_list' else Path(member['path']).name
            raw = originals[row['source_group']+'/'+rel]
            assert digest(raw) == member['sha256'] and len(raw) == member['bytes'], 'launch source'
    group = 'local_entangling_clock_gate_decisive_check/'
    repair = json.loads(originals[group+'SERIALIZATION_REPAIR_SEAL.json'])
    assert receipts['four_rail_serialization_failure']['end_utc'] < repair['utc_before_retry'] < receipts['four_rail_serialization_retry']['start_utc']
    assert not originals[group+'run01/stdout']
    assert b'TypeError: Object of type Zero is not JSON serializable' in originals[group+'run01/stderr']
    assert originals[group+'RESULT.json'] == originals[group+'run02/stdout']
    return {'selected_fixtures':2,'attempts':len(records),'successful_attempts':2,'failed_attempts':1}


def main():
    data, originals = checked_inputs()
    attempts = checked_archived_runs(data, originals)
    print(json.dumps({'result':'analytic_source_binding_completed',
        'decoded_originals':len(originals),'complete_proofs':2,
        'scientific_programs_run':0,'archived_attempts_not_replayed':attempts,
        'scope':'Identity, intervals and historical receipt verification only; no mathematical predicate or control executed.',
        'limits':'Two separate one-active-cell contracts. Four-rail empty sector preserves K; compact empty sector applies K+cI+dBC. Supplied sites/input/calibration and complete costs; no word, reader, native realization or retained audit.'},sort_keys=True))
    print('per_element: adjacent unchanged old pair, arbitrary old/reference input and specified one-head supply')
    print('per_site: four-rail 26 fresh sites and 36 edges; compact 6 fresh sites and 12 edges; paid local loads')
    print('per_mode: full-space penalty inequality separated from total-one-excitation comparison')
    print('per_block: full prepared output, distinct phase targets and explicit bare-input finite-time errors')
    print('lattice_wide: no occupied-bulk packing, word composition, common cap or native claim')


if __name__ == '__main__':
    main()

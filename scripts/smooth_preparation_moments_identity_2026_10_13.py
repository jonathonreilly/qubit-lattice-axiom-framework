#!/usr/bin/env python3
"""Exact prepared-energy source recovery and publication bytes; zero mathematical predicates."""
from pathlib import Path, PurePosixPath
import difflib
import gzip
import hashlib
import json
import sys

AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    ".claude/science/physics-loops/toe-prepared-energy-20261013/CLAIM_REGISTRY_ADDITIONS.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/EVIDENCE_MAP.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/PARENT_BINDINGS.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/PREPARED_ENERGY_SOURCE_ROOT_ACCEPTANCE.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/PREPARED_ENERGY_SOURCE_ROOT_REVIEW.md",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/PUBLICATION_EDITS.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/SOURCE_REVIEW_STATUS.json",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/graph.publication.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/graph_appendix.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/graph_between_1.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/graph_between_2.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/graph_header.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/higher.publication.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/higher_appendix.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/higher_header.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/nonautonomous.publication.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/nonautonomous_appendix.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/nonautonomous_header.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/preparation.publication.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/preparation_appendix.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/diffs/preparation_header.diff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0314d66507c1012d86ea2223e21daa143e7b595c4441684305a820146b21296f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0387ccde2db5bbe34f0558f1fb28262ec700d63defc37611c98f9a0b1ab7c17d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/039d114bbfc9c90510975ac1383264a06b3aae467ad7e6c90ce6a059d3bd0dc2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/03a051715e85c11d38ad9a9875f8227dda579b1869a9ef7d58d1d858aac47008.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/044cb5e04a671675ac0f4e96b317ce888e03e7415eac853b4d1113b27d20a62b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/04711a120c4854f9420f7b2a8f80672d5950d53c65481010452aaeceb53173dc.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/05daad2b45a8655bf311ed21c21cec08bc4d6aff681b7c9c80725a297db7a98c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0600dbe796195535ff29526f42b660b3c59fdd4071fa7b9bef4f3b933506787c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0750f26e8e3e09a23f23c51918b16864cf1fb9bca401347dd50df2a2f447df9f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/08239379fa29d5ff69e90eda343972bdbc65277c02310e02232bf392d6cb2d79.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0a60527449e723dd39fbc4aa6f4eb69a5481c4dd7c3fbd6a135059695511de78.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0c9eed3f90f57e9a5a313dffe4f82eecbb42ae7915c0ad90c06b01243676fb99.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/0da8c65272573b53248e47ab572e06e03f317c71dd70dd72f4d5ccbf62aed42f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1034f0ef3c2b2f63d61e0b6920fa70125e6ca28835b5f8b3e19fc5c0eee774c6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/10aa75b19058e8cc635a7c2a35a31552fbdb7976851c6bb0ec3c432ad9a061e3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/11f6bf33ab247ec56f794e04dcd40d874de655625132b13b4c44ff102ad801de.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1397b1c6397ce7db4c84716cde94a529aa51422f19942ffec3ec43db7eb46c48.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/13ce9361ee2d17a4a3febfe7c69a0b8693fe3882da2254ec89a3543c7fe0a70b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/14c545558595709a433f1312b0ba13af22a31fd3b93b96e51f68f491c36e3b8e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/171c07a771e100fd9c53b3cce6f9300973b939e04d09b4e53ed86e01f721b3e7.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/17629db1ccf576fe1e6b677cfb3f177ce1e6e801132ed0ba1e90edf8d8046217.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/18c4c80868a4aac146056baae6463eb2b689ee003543cb2cf26ab492a7e077d8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1916d8ce84701eafe40b9fb4e3616c33dead2b1a5a34cfad29ece02fb08ec6f6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/19bae5624955f0829d255d939ad4d3881adc65a5edcc4b33c60ba905650f9b78.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1a2199f3721efa2d96f88e33efa8fea9f06d19df578f402abbe4f49588d08d51.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1aca7d6d8c24101b24ef54dab7acb5880830e812d9abe4dc75bd2aefa1df1c46.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1c4a6929b9c550faa09a624f0921bf8e4b39fe865b91a93c8f31d15c56227e5e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1ccd7af6dbe10d299f1fc2fb5477bfac8ea6df9bb792fa6747d58a4ba263b0e3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1d1a0d04d47f2ed1efa1d1fc28c57b4d52918b89419867d9e349e73b207fe11f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1d9bfe86bca0fea75f515f517857cdab6c086ab651bc89f7c8d0096ade3c5cbf.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1e324060c36eb7dfe9dd409dd1685f5f9411920b4ca6b8b7270e1e97cdab889e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1ec27bfe2495446ac96d36117255b8e2af351baa0b6f3ebdea7169c46af8c17f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/1f534bb856d68140359e7204b08577c204195ff6077e7d7f6c4974e92f0afaf2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/200678dc8825d930864a088bd171b855d2704f4161af1670a270d82ee18488b0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/21cd87c56dd0a29284b9d74374451727304ae170b77f7dfcb55e2f3d64c0f266.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2525421bd28a5025e46d4b72a166e26a3c637418f696ac61078c1660436d58e4.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/259a3f1d9c76decaa5ba887dcf8b9d6e150acd5b31adf2c8c671d33dff47b473.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/25a10184baddd2e077b38985d469d606b567c0d024639b6e9e4a4e5e9b430bc1.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/28f41b3d7ca74e5cbd86153eb9c4d3e18700155a6cbbd30ee38d8b92764e6af2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/29331bc8e729e544c2640b64b29629faebd8bcdbc05c680ac7e5f701300a9d5f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2a5d182fd08355d68f88d340c92900c6040c5b6726c20c4e617e8c610ddb648d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2cb8c4e52f05de6a6ae8f5f06b1aa06888074848066d98ed58e6313d51662a36.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2e42e051c902345872bab13a1abdcb975e89017097c9ec5a2a72b9b264a64ee0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/2f8b358229d1f40ecc72d49c0f6827af144e2e57670784376111ce7e516b868f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/301dc365eef769c9111f53d20725c1ad8e0b7bb9ce69ae25f753d5511073681e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/30b8230c55e16005cbb90b59fc6a6a21597277e98c58c94bbd32aa2571c41c6f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3110071920ca8ed270aae90a4588157da1de23e9a262da15da19bf00a2af6fce.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/312273c11bd06072d026d3bfdff09c42270e2b905fbc4f5f597af039bcda7346.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/32238b64fbcd6aed9a43557af422e0b9cb8da7cd070ce84f6d73028c1105b0fe.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3304eb1516644c96824a43198065e699b2e36e4555735895a09b307866a5a674.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/33d614ce74d9faff7e83b6569df0316f5d6deeae0d8b81423650d504ffe214dd.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3413d701fd5cce9370eac1c62148b80f673c1e3b6bca9678d8d8364790cb6991.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3478bb4179940624fb809b86b8f4fe0a221c9afa6d8c342d3d7570933dff448f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/34bf78f52b8928dacece75750ad8a881f4fe1b59f49dc943ced7bd9ed5b6dd38.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/34ef7165a170ff9ad3488d404828ec2cf25d6459dc70381bf9902a22be50ffd7.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/35bbbb4992768581ce3753daef7104447e67f599a3a38823e7d3bb3c5725e507.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/390a9efec32c6ca740404cf607bd6c095e2816a66f913c16d97a1d5321bb41f1.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3a5ab687c18ab65077cf99afed1a66050756e7b7d363693d98963c60cb5d7f80.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3aa99bd1eac294bfe92874946ba637ff8971b7b9dce6092b4c98b5056c8df90c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3ac841213823bba1b14f03780d0ad8378afd747ce4e8ff62eedb8984c3a5e4af.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3dd887ce0d97985823a5440a6d42c665db9595153632dfe43091149de196b098.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/3f9f5b938215a2a36e2f7a7888d6dd01150696dc263b9b4d6ff708273b9cb677.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/402cbc03585ac1cf0fc32facfc18b889de09a2fc9b3bb1449dfda47beb813c0d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/409f3631e7e955947d1010a90a8595b53dc94d7ec30104cd14e049bcea10e650.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/41fdd517ab0e3a492acf04688f9633eb5f873f4265ea591bf88b3a46bbf0227a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4282b72723f572ca518742fca1eb5918c8ac39d02dc7178e18802ef34d5e9389.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/42f5cc241c9ee6f110f1c1970204f767319132088b6c05c59f66aa65eef1e1a9.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/42fb76ac2c3da78313ba681f9c84b42313f5bcf0301087ccd5548f477ebd82aa.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/43fb149a2e43cbd6b7fb8afcbc554179334adfebd90262a1674ab03c6d91747c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/45679c5b2492b81c3d4af5800415de9aceb7c02fa74a1df5080685986a3a4cec.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/461559bc5c2ca009d03fa1f3bcbcec4f332dd51abd061231e73c5d10948de2a5.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4769ec871f991f4b194724a88db97e67852732541586726ef23c362044cac13a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/47d94f2b67f97b1180d2b32a1445d2afda9b3ce8322ec5a278c47d486d872160.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/49d6f82d509d5be043eed2e6d6a815b92c7bff21fb9be2af819123d543f9feac.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4a284b65adce4a3d89142527fae3cba87121f0e267027d4b2d15b8a4a6b3eea3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4ab02757ff0be403b15d41779a04ca596436bc62240dbc027c01ac6d0fb78abc.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4af8cc6b639c0adf185c2b16fbe59e25bde41953a7c73fce96473cdd822fbbf1.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4b942412445a292193f1e30e6ebe3697ab65e1cfb5a72caa0ff69e78119a832b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4bc61a1a3c7289e04051a2d59b8d05601045490a0bf78168a1cdec3fa8968060.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4bfb2341f3e6a7f31a985d47bb1e19b4bafe4ecc096f8ca81d8ae7051a469284.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4c1b4fcac5b3d4cdc98d70726bb9c16e674a8ed02658ac76d4f6ab29f9c4c8f2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4ca063f158a2b00f9c4043343c7e9ddfd66f04db08b5305914c0a971780fbab8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4d0086bd24839e61019e74188403ce5f4099d976027f81fc15a03c4280e7b3c8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4dccca8477e450eefc5ef14b0f6e1d53687381c1c27c9fd2ba7922d6ac68272f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/4edab819bc9b906b66ab89d47d0109fe83c7b4a55a702f9f0738c826f01ed014.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/50c0c6b5ade51c0abdf12a69852cff15897add19942cfa2fcd62bb01b06edbe6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/52fad42682aeaeb527de50bfa24bf0597d0ec3527d9157bd3b346428ef99f79e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/54d63f23f8fa6db8c1991b280ae4152bda7df68108e168419c7018f4bb9a07c6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/551cb658d83383f4b3895a7e99b9dc64510000a6e802b3c6b5dafd5a9525ae9b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/58a9401c428e34a8c7792a05a36b40a171fadbfe98097cf71860ddf0eb0c4dc3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/59e8512bf024732b2d6ba8d17de73fa09ed313d38ad431479758a115f36d8f9c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/5a18436678bdf79c77ee26f63aa9e6096b4a3568cbe7063b50c19975811eaa18.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/5a547188f112e16397382bc8ae0fae9d9293430d9d643c244a72fba1d82d35a7.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/5c0785f94fe80c09784a4d7ba3fcc7135bc6ddfaaafa9ecaa070d85f17ddd6fb.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/5c6c68ba283bac89678eb931731710ba67427e8692fbf50ebbeb43113a031781.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/5e3590b4c1e66c6de1ab2103649a6c429e52adbfaee054f70b61fcc9a0efabac.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/622273759a10a8d69eb05d01363dddca23fcdfb4f0aa9ab7c994e98c45ae76fe.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/646959f96ae30ecde5cffce08ef6ef6dd835be339a5fc02e97e488fe0bcf38c5.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/64b53e49285ed5c32602629756fd4975fae477892ae8e301e52fcbe7579fdd53.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/67df1109bb9a7b89fffbbc78b8690e20276bce502772b2b80f68af38842d0462.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6842c582e5c8aff8017917591242cfc5a3ba49638f6ed394d195797f3e778769.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/689dd6522cb09154df58c15cc1532cf43eba196bcfee77f0e4a985f94960c596.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/68c2960d1255d428eec830ff1755c86deda655cd12d39ff32d13457e6168c6d3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6afad8a650d6faf56eea661399aec7e1010051d788744786064567f170ff3166.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6c6141b79605102354484ffb94e7ddf1233758a080d28df4bf75092cc97f2720.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6d0b71105f3d546081cf6d618af3303d32bac937c5cb22f46c0a3d00a844061a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6eb14ee15cbefe4794b866ef87f5043e17e0c7d5aa217ee38234f191944ed267.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6efbe5a3988f28b4640e160835cfce860866ad75220394daff6538eb8790ea6b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/6fa0ad3dde2d0e842503ad3830c4dfb5a009fee36d9fd4c21a1c4e3b947bf32c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7152b07d22dfcfc26d7ea2494b53cd71a4799c9e8288bb19cf6d04ecbc037484.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/72106da9b7294792f05e8a34e70965edfd4167be234901840d05f7c552e3b7d4.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/72772c83acf9efb5920480ca9ea4e2167815bafc96820d4550c0c90aed250c0f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/73e29fdf8927deb3d4f5aec17e71cac52bc9e6a7faaa7523fa4c26b497325a76.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7530e46e5c58c73a25d8a135fb53008dcaa4ec96a9d180df77b97cf4257e490f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/77c78b18dd8bcc1eed1d4de01e48764a0f8ec84d5a3dbada4005eff40b0278b8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7a1131289ced1fa30796dc1e8ffaadad3b2cd48e878e3546211cace4ccc8fc96.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7ab78b9db65646dacd073622f183857af82cb979231dce25b122e5e2c5a3246b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7b3609ce9610f3b52ac41a0a95c85d5f07adc5f857198c3945c32d7e7d82ab74.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7b5a457257f56dd76f9cdc46afca39dff85586dcb3415c39e6ff638630e7adb0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7c9df64640d1296f2dc8a6d1a522652d0f766fdad769b14ec303f38dd8b6ff23.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7cf607b2e92afe0adae60e3b582f6e203494d0ea7095610a732c66e1fd2d4f29.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/7fcf227a57f962bc1647ffd9e2ab3cefcd4168d828194593bcb235669c9e0332.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/802ae0395718e44bf10e2bad7002f29c8bf3dbbfb8f6ed308fe09bf402cd33f7.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/80e8790f61b111cf334b3f5d8a1f265e672d2d0b4a8ad3df9018764f96614629.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/811d15bb248873182054ee60d83728fbe00277b38f9891d860d92e0527bba81f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/816344503ca981252b3f9c6ef67ee5a323d8e30cfa560c56b6806b240cd63eef.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/833421a632b07ab8705172d3fdbc41c5532a76e2ecf33c4c6ceef3c2d6fec069.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/834196ced1dec22a0544ac24184b6321ffb135ba34ad94d5172c8bec2700136b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8361667a12e01be16c40b01a3fc6aff14512fb1fed6f29ccdd9cac2e4c408c09.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8454f1c88d5d6c05910b5d7fd1ec34d454118c4b41ad3d930a339c77c97c45b2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/84859e8bd4c3c38e7221c09ff8760669ac42fd9d68111fb7df1a6cc829697ddd.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/858f51884dd0055591e730b3dafc1c48df3a7a5fd1e73a2c0b4635054d3a797e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/86badd4a83b4577aaada75955a567ba9752602f12b8cf442a1b9f3405a3c066a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8754ec5e72c0db3171c0b2ff54fa0e15f5a77f87f3950ac8f19f4d1b0c623fca.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/89fab0812c3da801cc9b6c86e0672495c9a223607b6576878eddf0efb657e11b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8a60ee0f26bb41d25319311c10a9f8afedc990a16abb8aafb67043338b493d47.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8c22229bf30825f80c7e7063e5311a4fcd0bf06f820db4cf7fbffd3b92a4b408.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8c5ff6af2c6de7291863124668f3b0fd6bd703644eb72a05f13873b30edb6d08.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8c7604e0e7bfc2f34c75a2ec0d2cd7a8664a506920281a218f8df18e73e98a3c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8c92f6c7e2f14cceee320db7ee23c7d21a62815364f5d428f080b747072a75bc.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8d92dc3d4e192aed2b4068b6d9ec6fd2f5b3046af364ba997e8144e54d17121d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8df5f60b85d5e9b22b7d6281bc9941c300ce408caba135f988a125393d212bb2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8e01914fc50ae90775b7336cfac3fba60e36ddb77948e681b2165498c65e3089.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8f1e13d1ca4c42bbf4e5483c4035cacf28fd2bc82ee4b470776409e7753323be.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8f27b1f66b00e96a4c6481ff8830111d921e2d5e17cf559156ecb070832e5292.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8f63e8060be7540312c0084100b2d63b369680f58d3ce185a50b87ac9e5b6671.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/8fdc997ce1735a7a132a2fe21732e5f9c9197ac386ea7dd0b4e4a1aa7269702e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9020ba5c2797d8f026ddb72871b13f18a18cad4e0ec326c0f4653ceb438751bc.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9108e63d7f06464bf971bcd5728f7b25c29f899c6eb462eeedd089218877fb58.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/91e59c40a122d16d3d5175c2eef225084f029a1ad4bdd9732e07da487263843b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9427093d7aea0e203b7101cd3e41cfdcab733388ce440a5391130064a90bba1e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/942a4de7774ae3e6cab57850dfd84f8213635b1090ee61c940b7a8c707392d17.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/947b6345707e4557f0548cb0ab1e09edad9ab4220fc868b2e422d023d0fef0cb.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/947e62ddd7be640eca2cfc98a0e093a5fd83fade9f641432779849064878aa3d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/94afdc8d941194ac543626ea6c90461d4fdb2efc334cffa7eab0f101ee06494a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/94efc728e98f71edd0395458638d9ba185431a0d7c4e3e8ef78cb39e3686acb9.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/954b69fb01dccbd675f89c93fb511e0606614065bee05eb46f86c3331fbdcbf9.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/956faf9d4e6a4a36b9695578e1bace750e287527dcf8aecb7780f124c1654859.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9579bd3f7591e260067a846c054af9f71308e03431ce736a58ed7e2f4a083d1f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/994811bb5ea0bd03f17d14d73611d5dabf17a4e1b7f4614d538cc6db0236a9c4.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9a0b03a94c3ac841e3bcc351bd5675218319325d1e0498dc52cfcea311f91283.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9a73c95f8a9bc25efef2d7fc18692b3caf3994e705bb05b88d7472ca0ce8e16f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9ac286239070f1ad6369d213e5714e0d3d24866566d03f1fd2bf3ce5ea756c8d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9b5365cd9b2474fac28741aa8d9bfe2618f00fa578049c93a55f2d66af2be791.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9c6d57ad42f802816e3b2dc4f983cc96a78a613ef376f0da37f618e3eaab5e60.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9d7a965b6fbbf99641be1a5281b738bc183cbb2f72c209d5153550bc594d105d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/9d8a19f669ba565fcbb40283c49fab5e22db5ebbf75fc106adfae576f7cc6f28.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a10c7c59eec9e49a597f678202b4a1f4e1f5436db879633b4b12edc5003676a2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a396e6b94743a5edbeceb7101f9bcc8c4e06981fea4511d9b72bfe4fb7c73e84.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a50bc4f6b5fa24edb58826dbe346e77f79a744bfa966d935817ea9ed9754182d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a582ae870d31fcb2577637e880f0e05a55feac832fea1ea8a731a90638c5ecd6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a68fe33f023bc35746035fde11d1562e094ef99fb85f1850a870d1cab2ef4b96.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a69c2a8bac4089df3eab5e4a7d65dd611a5a2b6f3e2e4bd8e1a435ea6f4276be.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a7cf84f03e8ccf8d8e6cb88e5d31d5145195c7a5c89fd77fefbe2dadaf02859c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/a89c8915a2f1207aaee8fbef7273494126445d4e26fbda625d418f0557a83cb6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/aadbcb1343d80754565c20386658726573224fa88fc252228f7a6d071a0468de.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ac8ac8434e49ed95de37f48ec94e27d355e594acf4ea301f5575617c173ee56a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ad94121b98b4eaac61c9674ee24c04f324ce1e1681605e664da80f3513baad79.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ae987c9b440a9f14ba21e7d8e4f46b876a0ff7d98b39a522a94c6939024ad578.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/aed07742c68b32057f70421ef02142a1dd589f9b95492432ebad4832316edb0e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/af37bfb2c20e4ac0356c947c895fcac6b58d2b1c2b91112d9a3876f81d8b7801.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/af3b0274a01529b44e8cb08af880a823f99e64f823c3196764a272ea6450c043.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/afe052795fe343d707e793fbecb119c6bfe8dc433706e26e76bba8b3bac162d6.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b0e7b738819072879a14a94ff22953a041cf3389318b8bc582e1cce02372c48e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b28f2ecf8d59ccb88a5117cb65cd6c76826394ffabd965a7072d915d4deef288.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b475f153fb1222b986fded829586604a0809ae422c16c190fb9e4107fcd499c5.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b5f51b58b40d03e537edd587787509098b0f6d132b4660d81c18cfc6d0dbd51d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b6c4e514a3acb11a6ec4e7cf7c2ef97864cb7497489b945effac36e6bc38db12.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/b98531bcfe62ccb45b55bcb56343103c44eb7c6b0e1f0e26f0668afd414f5691.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c08d283a34efe57a7ae0b97982f3db846fd978926ae49908211341555b278233.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c6193881bdcfb8a6ad04c8479f658a9cae14e912db859c85e2dd2b638ba6585c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c650d117e910cf6fad171a83c4ef2fca7e83c3e98103ef80b167e8751e84bb67.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c6656012420f470010f26e34b590c9bd4808ff07f3ebded1a65d120cf9674daa.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c69d638eb4519d81e51dd39fd920b7323d320d5aea9c427ff109736bdcda75dd.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c6c78653a9d1ac3d850125bc014ae60e8f50642ae9c9b8069f4f6b17afdad29d.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/c8571279d316625cd39c86bbb32799129542dd01b163dd95a102e38cd3fb4514.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cafbfd602724c2feb139cf2f74031534579e4863e86901ab0d484ea7990f2d42.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cb17ba5a2a63b5afcb999938c404b8adfcb93554f232b3d140e22d386ab0dc8e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cbc1f8cc701f4386c27b305285099ed90ab90509ccea83fe1d44da4e06e62740.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cc3f1822fd17f36aa0209d8ded99da354204a55414746baea00ab1d7d117ce45.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cc43fc44133dd1c42db5a35938fcf35dbb5882d37bdc06d7e556dbdf97df7e81.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cd268e66e306b243230ef750db43bee0eb494efa44f4221e752e1866abbb19ee.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cdd651507f511dde107bea1f781f2b189f9d66664a3f4a20ea714cf69a984611.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ce498f7ba723f8dfe57523ccc36ea0326e1f3452c205ec15b47c1bc6201615b0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ce88333f4d2918eb8006d401016f7ca11b529da719552c3b978ec5f965d686e4.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/cec5dae2c6b4ecb9f4037e5f34e986e86ae9302e3faf17fdfe5a6a69714529ba.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d2eb0136db0ff2f35cfbc4cec511f00fbbe8275096c9ba97f1669ccfdd2fd101.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d44f11b0f004c81ed500e19eb7b8009c890bfdc7a873a47e8c16b36a29071559.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d54917008c3cd19074157492aa6e11afeded34282acac61111009dc4a765e013.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d5a218cd25aa3a4479681cac8e18e12ba4ae9f6a92f7819d970195fa83eeebb0.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d7952cd81116d3b841a42f5971d3c6ae50a283c3f5a73ba9ad8e095b9379c6a2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d7cb3301a2ec31a3892bfbfe6c179dcd97af4e96013ff7376044e75cbb198d63.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d80fa9b6b5c3d6e757c04939d951f796351c06601e3eb97f677c7232fd2a69c3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d885d3366fa54ed240aafc081fd89c6121998cc978d8f536cb3d28e3600767d8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/d8b8e4e3f87fa05176c70e1b74ecfbbab59aebfacc3b906c1bce9c8261a1aa67.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/da386897f7862fa0f6276d23f33e7b7e40aa3009fcd1e816056292884d5b9d11.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/da7ebd2d535a54f6a06f3e4349201705171ae87cf0fc582d30d84764b43a96b5.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/da9f640fc27e27a12077156b4d5746dcdbac8ee89c54370df12d10f510324267.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/dc3c3598cf3a1d1e0f9f8213e94fd8ac92a43306ff37cbcaaa0617071945779c.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/dd0825ad3ccbc186d6e6a08faa34baebba54432e738bf36745909e2382a18f20.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/df4e1a20357554d15f630faf5bab3c37f758097fe7c66e93572ac3b9b792ccae.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/df973fdd1272f9ae8128bfdd8e0a646e4ca3c63b5dc6c2e11f5775e5ea95d568.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e09ae31f25eab2303e09d627bce30382e40eb716bbfa7060969ca7b2ea88c3e3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e183a2ac78bafc4094774fdb04865d50bd14f23961f7e892056a3c0cde95b1b9.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e5a7292c1b314687f51f26bc33630c7b85c98e873a3d8641513c2d458d0c5944.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e6b9117c5770ad581a00b47963b94497a87ceee2cd38c14b47f7a5e102754a84.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e89399865add08546caf81edb9557aed3848826e883efd9ddda0847bab923a42.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/e935f77414e25d02d644df5ae5606b9cd4a02a5b61b96115a40097556ba92ddf.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ebf8d37b1466ff3a52af9a350a8c616f9de350e64a508f9dce541e8b2c2db864.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ec65f39080ef91b740286604aadf6cc050bc36ece7cf366ff9044f8600d4b800.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ee60fa2ecce8368fb3e9cdf76e8a562781b84081b3d0c4e8b5b1f45832018dd1.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/ef7f402eb108f1f6c5988d3974612b14b7b91cc89ea5c3d42a38b4646d96e73b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/efaf8f346467182c3d1582f5c35c0d758497580d78b720e58dbe575a5e983f72.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f1d1fcec5a20b16c3fbf32c3142e41e4adbec733429f91792fc4c1341686f48a.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f22a85900549aed7ecf637357413c235b121deb5c34e0df6e409980dde2701c8.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f4059ac8c0392c035e87b0b26a61accbfa22d0a8ada15b059fe894d92ac9ca0b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f417d13fdfb7962bde14353087f33c1ae4ca738c05ec2fc7586cbbd18f291dfd.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f4a30fa92ec2f9bcd3aa114c85aeefdda6160640f0fe4ac2dd50e77f991a4fd2.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f61f0b6157138f143ac44835043d64f2c1c0ab2a10f82d922d152d683adefc59.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f8603b0278ad54bd4b33be0512dbabf03b2cc2a17d46aeefa4e188aea1594b16.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/f9f919573dfe48c433f3b366fe7659add901330e5511f8970f615dde1a6226eb.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/fab7308a45eea59fb727475fc2d2eae65947a13b434384e2d5906eda1c5c68a3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/fb3b0d9384868ac27ec012745bf030e93a1eeb04d36a138afe9ea2a9fecd1f4b.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/fcecae22ca22c39620c56b4c3ca3e30d633e95bfd8ecb4e87e95b7ff93a87ab3.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/fd8c544154f17d612530c9afcedf387eda86f28b6352e3c32498295a3eafba6e.gz",
    ".claude/science/physics-loops/toe-prepared-energy-20261013/objects/fdd07d75338052b822dac40b45375f95269f2113cc788114321ffef0acd79e75.gz",
    "docs/CORRECTED_DISPERSION_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/EFFECTIVE_POTENTIAL_GRAPH_LOCAL_ENDPOINT_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/EXPLICIT_EFFECTIVE_POTENTIAL_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/HIGHER_MOMENT_ENERGY_ENDPOINTS_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/MOMENT_SENSITIVE_CORRECTED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/NONAUTONOMOUS_CORRECTED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-10-13.md",
    "docs/SMOOTH_PREPARATION_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-13.md"
]
PACKET = '.claude/science/physics-loops/toe-prepared-energy-20261013'
CLAIM = 'smooth_preparation_moments_bounded_theorem_note_2026-10-13'
MAP_SHA = 'e2e6328e64e8201bdd3e677ef893c4bbc67ceffefd145c8cb26ea58d36a36d14'
EDITS_SHA = 'c11f15ba114f82dd0f46cb8b593f6529f3e0f03abd6c03a7edc10b9f62ec0cf5'
PARENTS_SHA = '23163ddaba4fbca8a0debc9af1835ad43a5c2248755cb486787c9ea540a73979'
STATUS_SHA = 'cf171eaf0d36fef4de3deea851124894c262d7778e3772490611755b06b4e763'
GRAPH_SHA = '9310baa60ae8232b47d94f4f58e5c546ecf8433be2e0e0eef682f6f68e505862'
SOURCE_FREEZE_SHA = '32238b64fbcd6aed9a43557af422e0b9cb8da7cd070ce84f6d73028c1105b0fe'
ROOT_ACCEPTANCE_SHA = '7a1131289ced1fa30796dc1e8ffaadad3b2cd48e878e3546211cace4ccc8fc96'
ROOT_REVIEW_SHA = '301dc365eef769c9111f53d20725c1ad8e0b7bb9ce69ae25f753d5511073681e'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def complete_diff(a, b, old, new):
    return ''.join(difflib.unified_diff(a.decode().splitlines(True), b.decode().splitlines(True),
        old, new, n=max(len(a.splitlines()), len(b.splitlines())))).encode()


def accepted_source_diff(a, b, old, new):
    # Exact prepared-energy ASSEMBLE_SOURCE_NOTES.py convention, not the older corrected convention.
    return ''.join(difflib.unified_diff(a.decode().splitlines(keepends=True),
        b.decode().splitlines(keepends=True), fromfile=old, tofile=new, n=3)).encode()


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
        value = gzip.decompress(stored)
        need(sha(value) == obj['sha256'] and len(value) == obj['bytes'], 'Archived source changed')
        contents[obj['sha256']] = value
        for origin in obj['origins']:
            need(origin['path'] not in origins, 'Duplicate original alias')
            origins[origin['path']] = obj['sha256']
    contract = evidence['accepted_source_package']
    prefix = contract['path'] + '/'
    need(contract['freeze_sha256'] == SOURCE_FREEZE_SHA and
         origins[prefix + 'SOURCE_FREEZE.json'] == SOURCE_FREEZE_SHA, 'Accepted source freeze differs')
    original_freeze = json.loads(contents[SOURCE_FREEZE_SHA])
    need(original_freeze['files'] == contract['members'] and
         original_freeze['file_count_excluding_self'] == 309 and
         len({r['path'] for r in contract['members']}) == len(contract['members']) == 309,
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
    identities = json.loads(source('SOURCE_IDENTITIES.json'))
    need(len(identities['files']) == identities['source_alias_count'] == 270 and
         len(set(identities['archive_relative_paths'])) == identities['archive_member_count'] == 232,
         'Original source-alias count differs')
    source_rows = {r['path']: r for r in identities['files']}
    for item in identities['files']:
        value = source(item['archive'])
        need(sha(value) == item['sha256'] and len(value) == item['bytes'] and
             len(value.splitlines()) == item['lines'], 'Exact original archive differs')
    closure = json.loads(source('PROVENANCE_CLOSURE.json'))
    need(closure == evidence['source_provenance_closure'] and closure['omitted_listed_members'] == [] and
         len(closure['packages']) == 7 and closure['listed_members'] == 205, 'Historical closure scope differs')
    for package in closure['packages']:
        old = json.loads(source(package['freeze']['archive']))[package['member_field']]
        need(package['all_listed_members_archived'] is True and package['deeper_references_recursively_closed'] is False and
             len(old) == package['listed_count'] == package['archived_count'] == len(package['members']),
             'Historical immediate closure differs')
        for before, now in zip(old, package['members']):
            row = source_rows[now['resolved_path']]
            need(now['original_member_path'] == before['path'] and
                 now['sha256'] == before['sha256'] == row['sha256'] and now['archive'] == row['archive'] and
                 sha(source(now['archive'])) == now['sha256'], 'Historical freeze member differs')
    bodies = json.loads(source('BODY_COPY_MANIFEST.json'))['bodies']
    complete, by_key = {}, {}
    need(len(bodies) == 6 and sum(b['lines'] for b in bodies) == 2923, 'Core membership differs')
    for body in bodies:
        original = source(body['archive'])
        need(sha(original) == body['sha256'] and len(original) == body['bytes'] and
             len(original.splitlines()) == body['lines'] and original == source(body['copy']) and
             source(body['core_change_diff']) == b'', 'Complete accepted core differs')
        complete[prefix + body['copy']] = original
        by_key[body['key']] = body
    source_map = json.loads(source('LINE_PIECE_MAP.json'))
    source_spec = json.loads(source('ASSEMBLY_SPEC.json'))
    source_notes = {n['key']: n for n in source_spec['notes']}
    need(len(source_map['notes']) == len(source_notes) == 4, 'Accepted candidate membership differs')
    for note in source_map['notes']:
        assembled, core_paths = b'', []
        line = 1
        for piece in note['pieces']:
            part = source(piece['source_piece'])
            need(piece['byte_start_inclusive'] == len(assembled) and
                 piece['byte_end_exclusive'] == len(assembled) + len(part) and
                 piece['line_start_inclusive'] == line and
                 piece['line_end_inclusive'] == line + len(part.splitlines()) - 1 and
                 sha(part) == piece['sha256'], 'Accepted piece boundary differs')
            need(piece['kind'] in {'core', 'wrapper'}, 'Unknown accepted piece kind')
            if piece['kind'] == 'core':
                core_paths.append(piece['source_piece'])
            assembled += part
            line += len(part.splitlines())
        expected_cores = [by_key[k]['copy'] for k in source_notes[note['key']]['core_keys']]
        need(core_paths == expected_cores and assembled == source(note['candidate']) and
             sha(assembled) == note['sha256'] and len(assembled) == note['bytes'] and
             len(assembled.splitlines()) == note['lines'], 'Accepted source-note reconstruction differs')
        baseline = b''.join(source(p) for p in core_paths)
        need(baseline == source(note['baseline']) and source(note['assembly_diff']) ==
             accepted_source_diff(baseline, assembled, note['baseline'], note['candidate']),
             'Complete accepted assembly diff differs')
        need(source(note['new_file_diff']) == accepted_source_diff(b'', assembled, '/dev/null', note['candidate']),
             'Accepted proposed-new-file diff differs')
    raw_edits = read(PACKET + '/PUBLICATION_EDITS.json')
    need(sha(raw_edits) == EDITS_SHA, 'Publication transformation changed')
    edits = json.loads(raw_edits)
    need(edits['source_freeze_sha256'] == SOURCE_FREEZE_SHA and
         edits['additional_mathematical_body_edits'] == [] and len(edits['notes']) == 4, 'Publication scope differs')
    wrappers, published_notes = {}, {}
    for note in edits['notes']:
        need(origins[note['accepted_candidate_path']] == note['accepted_candidate_sha256'] and
             note['additional_mathematical_body_edits'] == [], 'Accepted note or no-edit contract differs')
        assembled, body_paths = b'', []
        for piece in note['pieces']:
            if piece['kind'] == 'accepted_complete_core':
                need(piece['additional_mathematical_body_edits'] == [] and
                     piece['historical_status_and_exposure_bytes_preserved'] is True and
                     origins[piece['source_path']] == piece['source_sha256'], 'Core preservation differs')
                part = complete[piece['source_path']]
                body_paths.append(piece['source_path'][len(prefix):])
            else:
                need(piece['kind'] == 'publication_wrapper', 'Unknown publication piece')
                part = piece['text'].encode()
                need(piece['wrapper_path'] not in wrappers, 'Duplicate wrapper')
                wrappers[piece['wrapper_path']] = part
            need(len(assembled) == piece['byte_offset'] and len(part) == piece['bytes'] and
                 sha(part) == piece['sha256'] and assembled.count(b'\n') + 1 == piece['first_line'] and
                 (assembled + part).count(b'\n') == piece['last_line'], 'Publication boundary differs')
            assembled += part
        accepted_note = next(n for n in source_map['notes'] if n['key'] == note['key'])
        need(body_paths == [p['source_piece'] for p in accepted_note['pieces'] if p['kind'] == 'core'],
             'Complete core order differs')
        published = read(note['note'])
        need(published == assembled and len(published) == note['published_bytes'] and
             sha(published) == note['published_sha256'], 'Published source does not reconstruct')
        published_notes[note['note']] = published
        stored = read(PACKET + '/' + note['diff'])
        need(sha(stored) == note['diff_stored_sha256'], 'Compressed publication diff changed')
        delta = gzip.decompress(stored)
        need(sha(delta) == note['diff_sha256'] and delta == complete_diff(archived(note['accepted_candidate_path']),
             published, accepted_note['candidate'], note['note']), 'Complete publication diff differs')
    for wrapper in edits['wrapper_changes']:
        old, new = archived(wrapper['source']), wrappers[wrapper['publication']]
        need(sha(old) == wrapper['source_sha256'] and sha(new) == wrapper['publication_sha256'], 'Wrapper identity differs')
        stored = read(PACKET + '/' + wrapper['diff'])
        need(sha(stored) == wrapper['diff_stored_sha256'], 'Compressed wrapper diff changed')
        delta = gzip.decompress(stored)
        need(sha(delta) == wrapper['diff_sha256'] and delta == complete_diff(old, new,
             'accepted/' + wrapper['publication'], 'publication/' + wrapper['publication']), 'Complete wrapper diff differs')
    raw_parents = read(PACKET + '/PARENT_BINDINGS.json')
    need(sha(raw_parents) == PARENTS_SHA, 'Parent bindings changed')
    bindings = json.loads(raw_parents)
    parents = bindings['parents']
    need(len(parents) == len({p['path'] for p in parents}) == 5, 'Parent membership differs')
    for item in parents:
        value = read(item['path'])
        need(sha(value) == item['published_sha256'] and len(value) == item['bytes'], 'Canonical parent bytes changed')
        need(item['historical_binding_verbatim'] == source_spec['parents'][item['key']], 'Historical parent scope changed')
    dependencies = json.loads(source('DEPENDENCY_REGISTRY.json'))
    expected_same = {(e['from'], e['to']) for e in dependencies['direct_edges'] if e['to_key'] in source_notes}
    need(len(bindings['same_packet_parents']) == len(expected_same) == 3 and
         {(s['dependent'], s['parent']) for s in bindings['same_packet_parents']} == expected_same,
         'Same-packet parent membership differs')
    for same in bindings['same_packet_parents']:
        need(sha(published_notes[same['path']]) == same['published_sha256'], 'Same-packet parent bytes differ')
    need(bindings['archived_provisional_relations'] == dependencies['provisional_support_relations'] and
         len(bindings['archived_provisional_relations']) == 5 and
         bindings['historical_publication_lineage_verbatim'] == dependencies['parent_lineage'] and
         bindings['branch_lineage_is_mathematical_edge'] is False, 'Provisional or lineage scope changed')
    raw_graph = read(PACKET + '/CLAIM_REGISTRY_ADDITIONS.json')
    need(sha(raw_graph) == GRAPH_SHA, 'Graph proposal changed')
    graph = json.loads(raw_graph)
    edges = {(r['from'], r['to']) for r in graph['direct_edges']}
    need(len(graph['nodes']) == 4 and len(edges) == len(graph['direct_edges']) == 15 and
         edges == {(r['from'], r['to']) for r in dependencies['direct_edges']} and
         CLAIM in {n['claim_id'] for n in graph['nodes']}, 'Exact direct graph proposal differs')
    raw_status = read(PACKET + '/SOURCE_REVIEW_STATUS.json')
    need(sha(raw_status) == STATUS_SHA, 'Review scope changed')
    status = json.loads(raw_status)
    root_acceptance = read(PACKET + '/PREPARED_ENERGY_SOURCE_ROOT_ACCEPTANCE.json')
    need(sha(root_acceptance) == ROOT_ACCEPTANCE_SHA, 'Root source acceptance changed')
    scope = json.loads(root_acceptance)
    need(sha(read(PACKET + '/PREPARED_ENERGY_SOURCE_ROOT_REVIEW.md')) == ROOT_REVIEW_SHA, 'Root source review changed')
    need(scope == status['source_review_coverage_verbatim'] and scope['source_freeze_sha256'] == SOURCE_FREEZE_SHA and
         scope['mathematical_body_repairs'] == [] and scope['mathematical_predicates_executed'] == 0 and
         scope['formal_analytic_or_model_diverse_review'] is False and scope['retained_audit_verdict'] is False and
         status['no_go_packet_pass'] is False and status['N1'] == status['N5'] == 'pending' and
         status['prepared_source_freeze_sha256'] == SOURCE_FREEZE_SHA and
         status['fresh_full_final_core_manual_read'] is False and status['new_independent_mathematical_review'] is False,
         'Source coverage or pending status changed')
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
    print('per_element: checked and not executed — source integrity only; no scalar coefficient, moment or positivity theorem was proved.')
    print('per_site: checked and not executed — source integrity only; no CAR grading or locality estimate was computed.')
    print('per_mode: checked and not executed — source integrity only; no dispersion or physical-band estimate was computed.')
    print('per_block: checked and not executed — source integrity only; no graph domain, commutator or compression theorem was tested.')
    print('lattice_wide: checked and not executed — source integrity only; no preparation, BV, energy endpoint or no-go result was verified.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'result': 'identity_verification_incomplete', 'error': str(error),
                          'mathematical_operations_executed': False, 'mathematical_predicates_executed': 0,
                          'scientific_mutations_executed': 0}), file=sys.stderr)
        raise SystemExit(1)

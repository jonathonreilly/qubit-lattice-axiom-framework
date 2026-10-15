"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/TRANSVERSE_FIELD_GIBBS_MEMORY_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-transverse-field-memory-20261015"
PARENT = "docs/LOCAL_CONDITIONAL_BIAS_AND_ROTATED_GIBBS_BOUNDED_THEOREM_NOTE_2026-10-15.md"
EXPECTED_PARENTS = {'docs/LOCAL_CONDITIONAL_BIAS_AND_ROTATED_GIBBS_BOUNDED_THEOREM_NOTE_2026-10-15.md': (166194, 'ef7f472b1d7de4ef18206e113960649645bb831421a4fee892d34e98c6adcb89', 'local_conditional_bias_and_rotated_gibbs_bounded_theorem_note_2026-10-15', '637ccbabb9d275bffd3bc53c857d873ecc9ab3e7fd492600ef7d819b598c9b95')}
EXPECTED_PARENT_REVIEW = '90ff1d5dcaa1af35ad3f63c39e16232fb1e52342c4af8dbd0d4405caea49fde2'
EXPECTED_ACCEPTANCES = {
    "transverse_field": "41b736668534cc2f9c87f98b024e1ea349960baafdc3b354914cb0cd1ae2d49a",
}
# Root-selected base; actual binding and captured review evidence remain mandatory.
EXPECTED_GIT_BASE = '492cf6670fdddcd6c091ef5c978d7519e9ba0b6f'
EXPECTED_REVIEW_DECISION = 'Accept source-only publication proposal for separately reviewed actual integration; no primary or publication result yet'
MANIFEST_SHA256 = '8159f746b01debf40fed6d3e0a362a3170d7dbf3cda3aeffc0c9852f8f98d306'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-transverse-field-memory-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/CHANGED_CODE_MAP.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/HISTORICAL_METADATA_RECEIPTS.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/PROVENANCE_PLAN.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/202a0318ca45d24f7d343a83703d2d0f4c7849d818ead438adbf5ef4d57d81ef.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/291a8e91a8fa58422a6d13fc80f91c06e122a3ac85f6dc5416d258ba59c42190.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/38571274f835eb63a398f28495f367e2cddd2c4bd21b6596c2f1752820f48f23.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/3ef03d83a0ac0f5038955fd9986e87ca427e965d967d063331dc46627081ab82.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/41ed7d7d4ad1bcdf43b9004d1da164abfdda0a4d3090da2a180cbc11d4f045e1.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/48aa32bc68cff461bf4fdf7c93e518b60a15d058837306cb552f3b5adb63f806.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/5a713d4b4ea8d7babad150e297d247661d63f3748f7511f4ed8efcd4e09bacc5.py', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/63e43c97ba3a85a5dd81afbddbac974727d67f69c539f4d7ddc77cb31d37ee09.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/715f1263ef6bc5c8f36b158cd5dec26a40f51f643ac6339cfe6dccceab167182.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/780ac9767654dedd03e09594a46b54bfdf8a1859bb28805adb274ac99404f972.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/96e198bc616242f36fc59bb498c68d52cb4b2605fa3695f49eb4463720b43bee.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/a114f85b470a7e4d81a92d4bfad0fcf9a058732fede37f633b2e4ce4e057cfd8.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/d74ceff0f3eb91588e50d725b4effbe31101da328f09ac626ec30825770f4bfd.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/e1d53683f62a68261eda2616fc60770526144e4007823c8432b8c5e364802420.py', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/f2fac13228af7cce764dd69e4f1f1ca3e165cfc2acca26a4f57965bc73aefb1d.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/binding_sources/fb47dbfcfbdc5bc525356f831e654beb9237b8d9fc2a025774cecd1796b9a6c7.json', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/build_proposal.py.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/inspect_proposal.py.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_ASSUMPTIONS_AND_IMPORTS.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_CLAIM_STATUS_CERTIFICATE.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_COUNTEREXAMPLES.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_HANDOFF.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_PROVENANCE_PLAN.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_PR_BODY.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_RECOVERY_SCOPE.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_REVIEW_HISTORY.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/packet_TRACE_GATE.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/primary_template.py.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/record_metadata.py.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/seal_packet.py.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/packaging_diffs/wrapper.md.diff', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/10b075e8fb1cf76d2303cfc21960c5e5e9b26d3916343162eb5d7e03f319a2c7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/1463b310abfb086aa64039873fe7c2a3b7bfa148e5a4eaf857b94b92fba4d2da.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/1708bd8973c91c6efaa214778a4ccd09b9a35387b3d3bcebe8e10e5987cbbe29.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/1713e53034f530fd761de763ba91b2590dd0dc7c305e06f120850b6cfb5e16f1.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/1eb6dc4ffbe52b5fb81382c8fdedb09b81fd0870eef6ee5a85d50940901c4d3c.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/23c69777e1c9cede803731e85b0295cf4966f78d8736d41e041218474c68685c.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/2544d341f3925dadb5d610d736ef4a33ec6d3e692fe9b30cef6b310072da7852.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/2b2565fbe3ce3626fbe4ea734316f223c104a93967e88c4e3d8559526ab9e139.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/2f32b9e21ba256c8a1afe91ef967a2845932b40a05645935b4e934d4221d59ae.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/2f3967bde89d0ca5cdfb74e4c7eeddf0d3a57c653e14327cbd02f3e616b95e90.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/38ce43acd36276501867e202b5db145e2cc537a16a090cc2c7d656bc067cdbfe.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/3ff0ff43ccb169118a47c5585986376cf8a4dab549fa2812c9730fdb848717ac.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/41b736668534cc2f9c87f98b024e1ea349960baafdc3b354914cb0cd1ae2d49a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/444967a45050ef38aca3723ecf34c1e2c102ac2c6abe0ad12948e5b0469ff890.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/44f67af24d3d92c4e7f24afd1c9c9e217cc61fe4c8c5f2b093de689a6c4c161a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/483583c64d4b46ad901bfdf72a971ef7bf2e6ab08ec8a85f03d7a9ac0b94737a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/49b39aaaaa967a4bccab0aec74132cd5a147ecd160e94f7c84dafe652627aa4a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/4d9eebdfe214d86afa5968d5adf73662c9b96bbd2cec19fd0d94fbb4d96fcb70.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/507d2a85e7d7eddeef0cf97b5701832212b35b2ed692b8514f06ccec7af1e562.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/50d358e9b1a7d252c449e7d8ffd9db6f8ee760f2dc2e62cc76b1bdd72e8830ba.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/51a58e088885b4c68819a93ebf68775fbcac725be2557b28cfe59b469a2a26a7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/5256971fa7f3523ce9f6f99b9cd1379e2b8f288b2157a7786e45ab2612d3c3a1.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/5637cd854c837252157eb9ecf603690fa32e5d7cccc30e7f823f06dd7ae1f5c7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/5d81b31f98478c15d16cb72f056202bd9fc0df3d24300f89e357d4873ed704d0.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/6024d6e7e4337cadafb9753477de4d066e3b2b3f1e2715a937a6f1f8d157e7f3.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/67a7af8e049cacee2d69c0bab132fd4ecf40915a7acb73eb1b6498b8a1bf2a6f.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/68ad6535c26bd42f14c31f5a2aa3eeddfd636d513fcbc7e51d8e7f8be82e3356.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/6f44b2139e635f1f5ed14919a2250951b713ba10568cbd48cfcaea353886e2f7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/70bd9b7bf4569c544af9a893dd2c074d8078a0922e5a5353e0c8655ab3c34b10.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/715f1263ef6bc5c8f36b158cd5dec26a40f51f643ac6339cfe6dccceab167182.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/7284acc65ab45aa803518bd57221e03f87dfba1443a77a94279494a67ab06bb0.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/729b194f4bb85721715573ce8b37c8a81df6c67b3b84f9a3deaed02b23a5aad0.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/79d10728c72fcf450086834a8587008a16725f463abe4b43556ffbf61e5d23ec.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/7abab850904ec7f0c33899cb814c3384c65ef4b845afead19d4e6265cc9295be.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/7d9b9773894ae0aedfa0efb2d732f4d7e400ff819450e5f1136f28463d9630f4.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/86b626cc3c4ff238dcb9601a3bfde9583f8a9fa9f1e1c11e2d62418d96421561.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/8cfb69261c6cf18b0b516d712e9f22fd2e5e0b2313b9e216f4e9596379c87b64.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/96349ed2e9ab870e6dda51cb0b884288c22aa39e3ed98fcab37e51cb063daa36.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/9aae08f4c95c7b02d55e755d269c4d836384a8c0074f41fe9047c00b76068206.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/9ef365e53afd18f02b66ea7549904a6d9e14d4b19cd2b8a34ebbabf916e89c21.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/acdce88206ccaaec24da37c29ef1cd484ac28c11e62611d8d3cd8c76a362e8a5.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/ad9b39fb72f4e4ff7f6f76ff28ed59a1fa1656f7645ed55f866e4240999bc35e.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/b08c128d2fcf3a0e0cfe38da029ba5e63ddeb4908be2debc92e1bce21fb9163e.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/b53da933f3545ffb60ce7817722f8a9442d91a11d6caeef4d828d46c158ef221.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/b69f398c97cbeed620ed6c3c081b5d96c26b0e5c910706a677a7449657a80d7a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/b9cfba8929eaf8f4a2a85fb1ffe95c0c1cb38cb843e24fcff949cf67b343f97f.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/bd3309e15c18f0cdfb2a0ec610d45162c662ebf26f5aabd5089a17238c91b2b4.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c271bed5483f0e084c031ae5c855bc6c7a9b7439082937d7c96bd6064443a8c6.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c2c392635dd6c0320685da0275f28add2d3494eb6ca8316cf02f435b4bfc800b.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c43d813357cb38331da26d004e9f7846a96c03bedb16c5fe903fc48693bd7d68.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c8861caeb4a697e5de423842d6b02fd8018953fd77b5ff9dc0d04ac2379e31e6.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/c9ad1d105c8a3c766981a49da834dc87e16d826067a694a093de6eba24562b46.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/cdd2a40a53d39ac8cfee8004c84e9cb7242e8f624b0eb0eb83eda247e925d71d.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d1577da8b8796917c7660180daef846f8c0edfcce30deb70164b08354406e55e.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d38091546579dda821911ca839eb91f74fdf7e0a4a297091f2006c25f10e7443.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d83a9b713aa637811c126603a0b0da24ae5e701232c8f78ea3ca8e10c2968dd1.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d8536447cebcef30e5d05c9b81e230515a565b7471ae32c0fb85700653efe9b4.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/d8e50496df2cc4de3725b80ab771bc26e215f2a7b0a20228acdc86f2ef31ce9a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/dfef535a1f7bdfd6ad9d6084c6e709af69e52747f377ddb3ccfbb1a49fa30d39.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/e51556af7a1dbe1f2370d438d22d4a0797331780c239154e972d57df968a7c3b.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/e759dd544df26db9930b19e500a36a8cad9da9f84579906263297d435646e6cc.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/ea7242efaeb00ba35cc9aee3f155796fdf3b0f2345cdbf1f9f3cc4aba71c9f73.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/eacfe6f0f22274e972b5ea1082fe75d8303c2d80f2062693568a9b5a970be59d.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/ee89d673d0d3899dc1bcb0c50449275893adf52276a49f469bd044b0be76cfb7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/f7521b2759bf751b38d02529a7cbd407d9c5e0d873a13ce552c7e466886b11f1.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/f8d564f76d8e49d8be162ebca0668283418d31e28a76d2eb0468ff0c8cbeeb6a.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/fb47dbfcfbdc5bc525356f831e654beb9237b8d9fc2a025774cecd1796b9a6c7.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/feac515d67c7fdcf239c7867504dc22f19a96434154e046c999f564c88076f69.blob', '.claude/science/physics-loops/toe-transverse-field-memory-20261015/source_recovery/ff97acd2c1dbebb629537bec53e904c58129ab0d09e29abbdcca11f1384d4973.blob', 'docs/LOCAL_CONDITIONAL_BIAS_AND_ROTATED_GIBBS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/TRANSVERSE_FIELD_GIBBS_MEMORY_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'transverse_root': '5cbafbd7b04fa425c4b5f975c075cce33c0e7b19524917ed0a40051eea1fe5ec', 'transverse_independent': '5f7163966dcc27159591baf80aec86ad75757fedfac2fd69390c65a4a1df0b5f', 'transverse_comparison': '6693f24d1561fc915213c48e7debd7dd5d538ccc77686b747106ddfc1469baa8'}

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

def main():
    mpath=PACKET+"/INPUT_MANIFEST.json"
    raw=safe(mpath).read_bytes()
    require(digest(raw)==MANIFEST_SHA256,"Input manifest identity")
    manifest=json.loads(raw)
    require(manifest["schema"]=="source_integrity_inputs_v1","Input schema")
    rows=manifest["inputs"]
    require(len({r["path"] for r in rows})==len(rows),"Duplicate input path")
    actual=PACKET+"/ACTUAL_BINDING.json"
    expected={r["path"] for r in rows}|{mpath,actual}|set(EXPECTED_PARENTS)
    require(set(AUDIT_INPUT_PATHS)==expected,"Literal declared-input closure")
    for row in rows: identity(safe(row["path"]).read_bytes(),row)
    note=safe(NOTE).read_bytes()
    header=note.split(b"---",2)[1].decode().splitlines()
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false",'upstream_dependencies: ["local_conditional_bias_and_rotated_gibbs_bounded_theorem_note_2026-10-15"]',"runner: scripts/transverse_field_gibbs_memory_2026_10_15.py"]:
        require(field in header,"Missing actual scope/binding field: "+field)
    body_map=read_json(PACKET+"/BODY_MAP.json")
    require(body_map["note"]==NOTE,"Body container")
    require({r["name"] for r in body_map["bodies"]}==set(EXPECTED_BODIES) and len(body_map["bodies"])==len(EXPECTED_BODIES),"Immutable body roles")
    for row in body_map["bodies"]:
        require(row["container"]==NOTE and row["sha256"]==EXPECTED_BODIES[row["name"]],"Immutable body identity")
        interval(row)
    parents=read_json(PACKET+"/DEPENDENCIES.json")["dependencies"]
    require(len(parents)==1 and {r["path"] for r in parents}==set(EXPECTED_PARENTS),"Exactly one direct mathematical parent")
    for row in parents:
        require(row["role"]=="direct_mathematical_parent","Parent role")
        require((row["bytes"],row["sha256"],row["claim_id"],row["accepted_raw_source_sha256"])==EXPECTED_PARENTS[row["path"]],"Parent identity")
        identity(safe(row["path"]).read_bytes(),row)
        r=row["accepted_body_interval"]
        require(r["container"]==row["path"] and r["sha256"]==row["accepted_raw_source_sha256"],"Parent body role")
        interval(r)
        r=row["accepted_review_interval"]
        require(r["container"]==row["path"] and r["sha256"]==EXPECTED_PARENT_REVIEW,"Parent review role")
        interval(r)
    archive=read_json(PACKET+"/ARCHIVE_INDEX.json")["objects"]
    require(len({r["sha256"] for r in archive})==len(archive),"Recovery must be deduplicated by hash")
    for row in archive: identity(safe(row["path"]).read_bytes(),row)
    sources=read_json(PACKET+"/SOURCE_MANIFEST.json")["sources"]
    accepted={r["sha256"] for r in sources if r["role"]=="root_conditional_source_acceptance"}
    require(accepted==set(EXPECTED_ACCEPTANCES.values()),"Exact transverse-field source decision")
    for row in sources:
        r=row["recovery"]
        if r["kind"]=="blob": identity(safe(r["path"]).read_bytes(),row)
        elif r["kind"] in {"body_interval","external_body_interval"}:
            require(r["container"]==NOTE or r["container"] in EXPECTED_PARENTS,"Undeclared interval container")
            interval({**r,"bytes":row["bytes"],"sha256":row["sha256"]})
        else:
            require(r["kind"]=="external_pinned" and r["path"] in EXPECTED_PARENTS,"Unknown external input")
            identity(safe(r["path"]).read_bytes(),row)
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
    require(state["scientific_programs_run"]==0 and state["historical_programs_replayed"]==0,"Historical execution scope")
    require(state["source_decision"]==EXPECTED_ACCEPTANCES["transverse_field"],"Actual transverse-field source decision")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding is required; source draft is unbound")
    require(binding["root_read_complete"] is True,"Actual root inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES,"Actual source decision")
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and all(c in "0123456789abcdef" for c in EXPECTED_GIT_BASE),"Actual Git base must be source-bound by root")
    require(binding["git_base"]==EXPECTED_GIT_BASE,"Actual selected base")
    require(isinstance(binding["receipt_paths"],list) and bool(binding["receipt_paths"]),"Actual binding receipt required")
    for path in binding["receipt_paths"]:
        require(path in {r["path"] for r in rows} and path in AUDIT_INPUT_PATHS and safe(path).is_file(),"Actual receipt is not a pinned declared input")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_transverse_field_source_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
    require(canonical["bound_note_sha256"]==digest(note) and canonical["actual_git_base"]==binding["git_base"] and canonical["canonical_parent_sha256"]==binding["parent_sha256"],"Current binding identities")
    require(binding["raw_bodies"]==body_map["bodies"] and binding["canonical_parents"]==parents,"Actual body and parent structure")
    freeze=json.loads(bound_blob(binding["source_proposal_freeze"]))
    require(freeze["immutable_bodies"]==3 and freeze["mathematical_parents"]==1 and freeze["scientific_programs_run"]==0 and freeze["actual_binding"] is None,"Historical proposal seal scope")
    evidence=binding["root_review_evidence"]
    review_raw=bound_blob(evidence["review"]);review=json.loads(review_raw)
    require(review["kind"]=="root_source_publication_review" and isinstance(review["read_coverage"],str) and bool(review["read_coverage"]),"Actual source-publication review schema")
    require(review["proposal_freeze"]["sha256"]==binding["source_proposal_freeze"]["sha256"],"Reviewed proposal identity")
    require(isinstance(EXPECTED_REVIEW_DECISION,str) and review["disposition"]==EXPECTED_REVIEW_DECISION,"Actual publication interpretation decision")
    for role,rel in (("note",NOTE),("primary","scripts/transverse_field_gibbs_memory_2026_10_15.py")):
        matches=[r for r in freeze["files"] if r["path"].endswith("/proposal/"+rel)]
        require(len(matches)==1 and all(review[role][k]==matches[0][k] for k in ("bytes","sha256")),"Reviewed original source identity")
    require(review["accepted_science"]["sha256"]==EXPECTED_ACCEPTANCES["transverse_field"],"Root reviewed source decision")
    require(review["scientific_programs_run"]==0 and freeze["primary_execution"] is None,"Root source-review execution scope")
    _,result=execution_evidence(evidence,True)
    require(result["acceptance"]["sha256"]==digest(review_raw),"Actual review output linkage")
    require(result["members"]==227 and result["sources"]==114 and result["same_AST"]==22,"Actual reviewed source counts")
    review_freeze_raw=bound_blob(evidence["review_freeze"])
    identity(review_freeze_raw,result["freeze"])
    review_seal=json.loads(review_freeze_raw)
    require(len(review_seal["files"])==1,"Actual review seal membership")
    identity(review_raw,review_seal["files"][0])
    require(binding["extra_mathematical_dependencies_imported"] is False,"No additional mathematical imports")
    key="base_parent_observation"
    receipt,observed=execution_evidence(binding[key],False)
    require(receipt["argv"]==["gh","pr","view","9615","--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual "+key+" command")
    require(observed["number"]==9615 and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]=="physics-loop/toe-local-bias-gibbs-sources-20261015" and observed["baseRefName"]=="physics-loop/toe-finite-memory-bank-20261015" and observed["state"] in {"OPEN","MERGED"},"Actual "+key+" PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding[key].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(p in AUDIT_INPUT_PATHS for p in used),"Binding evidence literal closure")

    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and binding only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: literal fields, positive reserves and channel reconciliation preserved; no physical gate executed")
    print("per_site: finite source graph and fixed consumer endpoints remain supplied premises")
    print("per_mode: rare-record, reference and full-density quench limitations preserved as text")
    print("per_block: three immutable bodies, one parent and actual source binding checked")
    print("lattice_wide: no native Gibbs preparation, general noncommuting extension or audit certified")

if __name__=="__main__": main()

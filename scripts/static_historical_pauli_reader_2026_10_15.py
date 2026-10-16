#!/usr/bin/env python3
"""Bind static-reader sources and historical receipts; execute zero mathematics."""
from pathlib import Path
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
PACKET = '.claude/science/physics-loops/toe-static-historical-reader-20261015'
NOTE = 'docs/STATIC_HISTORICAL_PAULI_READER_BOUNDED_THEOREM_NOTE_2026-10-15.md'
MANIFEST_PATH = PACKET + '/INPUT_MANIFEST.json'
MANIFEST_SHA = '5e34602b69df6fdc8580b8f4c22b04d83352abfd66429998a9bf3e6f312aabb2'
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-static-historical-reader-20261015/ACTUAL_FEATURE_BINDING.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/ARCHIVED_RUNS.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/BINDING.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/SOURCE_INDEX.json', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/01b0022ce73dea3b06a98419eab55a77de9a1b11dfba228cb290367ce9a4ce82.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/0588b08d153d4f3e1f2824b2ba4545253db303e392f0f9c80707596099e8937b.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/0600873c6d99199a819645586ad876c1813eac35ba7545a83a0acfdea2e92563.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/0807b8b0dfaec98b5cae8f9f79f35457c2e95da0df3fadcf495cc3b300e0bd09.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/09ccff2ae0402a2930ae0d8087a50f84e00b8a5258430bd8e4dca7923910807c.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/1029c860ca2f0e047a917aad46f60bed7e37e64e61a44f6593d40aac316cb5c2.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/12828376cd901f28770855c17d17d6b9fb8b80a6b9fa89cec151b7e785dd1d14.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/132e4280a7dd657cec8e9e793dc838c957219f5456cf01f3ec6dd6ae081a9fd1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/16f098549611d7888151393c8ed4fa344f29c55132146c7e52c6ac34b32ba7b7.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/1c14b9c27553d9ca4efc6103f2b4d4c76152bf94e64b40e416b28331dc2c4256.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/1cb044cf387ef51f10b1d007db0f3eb27dd5b6292923220479e46a268dfc24c8.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/1f82ef542a4d31dacab22d3ee6155030509db8358074e54f3c13b9b7efb32a42.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/2145763224ac6f246c9b0ea49ea14e52563b9c9b8bfb86a186c6e1e524b6ff78.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/23c44e58b47f027abc3f4b7b7c0440b8ddcbcf12510c368f442670e2779f198f.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/267fea399357aa682568219e6e320cfe2100468589b0dc62ef65e05bcffef35d.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/2a07de85e1c92c5c9b397b4cac60b4a289f2e0de709ddcf4a09f745b93ca3f69.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/2bc76aea5d586a054a3797e59aaacfe6d6187a6e72e8705ff9a569cbca6d909d.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/2c95a969f8d8f40f4190ece9f25d811c7e204a4f68de722f3fe393265b2c8115.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/2f00195e9b7774759733f28f543cb87ab0c3fc5b268cf5afb9d1825e634749b2.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/31051975fed3ce2d2f0c3f2cf81238cb68c3a96102ae4c4f87569bdc2c0660c2.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/32f20e3bd7b78271e53d28e8e8d9482bb51062718b2c640f75a11a30c5cb59fd.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/385be1a468ec5bb9cceb77837a7c5acd7b90ccac980345728b4f2f7160408497.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/3b0bb2127854985cd98f9fec903e17cb2aa16f84b36fc8610bb2e8821554ac46.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/3f278725607d509fb02dcc321babd79d742464e32e0a5c0d647708eaf77ad995.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/4236468c02d3442334326549163362290df381e2e05cb4b83245da13c4910147.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/43e9ba6e75d74b10559506cc426966543d6ed28e54e4881b957c91f3b16c1574.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/494cc9a6400b2158f5b29275029a9b9575ba0e18e527d8586178c6adbd5cdd5d.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/49d6127f7423a3562c6b5b61e5b3b8e972d0b0de7c962b2018695d30653a14d1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/4bfa1bdf8112bc337922aea6d2e0096cc159025f0667389e51040a19d9e26236.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/4e67377ed1a8a907fa93d4925ce4613967e13888d69baeb4a24ffa45f58d53e0.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/4f2ce0f8e738a3b0b9bbb4f087d6fa7550f188c6b8a385110adb13a33d3de1b5.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/526a92c6f5239f18b07cf46697a14e0a04da5df4a7f55150b655c9908eadef48.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/52809309c191cb50085de18ac799fc42635478fe9f45e9d1f3fcf711ae04be65.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/52bed53ccef75832d309f436f905cad76e8030d7fc90c15d8e0ba177dfe9d6ae.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/53ece1acd0b940daeb9b04938b35bb0d1f16d462ee50de7d70a4ed024bbc97e9.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/54b04a35c15bc07e5fd0d67f28cb573fb03030caff3f20d268790185442b500b.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/5b035c92a858e3ae6ec6c0077441435cc39db4681708d77049b5b34277b9d519.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/5d829160707ab0499b7bb13c1a613c9f35484bcf11d630c5334ae262f17a516c.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/5ffdd752c151a4d4c0aa99f8299d5095b1954ee87303a71f266606d6b9493940.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/6085f0118c8eb7fdac3b757f686f00e3abde4b48ea1ac6883fc42d954c42a543.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/69bde9578c402ed6960fba46def0a5ac7253c559f4c37af872a6dddfeeb82095.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/6a0274bd8a5fd7e2367268d973e7ac50ba38b9e12d3cbfbc8652486d900b5aea.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/6cc5c1a83ea665e96666ea56c86ea8d2642f6e29dc0dd936bc918333e2f5202c.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/7c214bf1083c7c23003d784a9feea840889dc4d0cdfcbb893cba6161612d4ca4.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/7c94977b1f01534669f45f2e5f363f51159d24bebe445be68327f4aba28bf92d.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/7ce0edd27719eb8c33ef0dce0f42c18f0c9879ec8eb8e21e18b6fe65bbf83f50.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/7e87c25382195eb5d15509de75e1fbf343573dc86513da74b2301ea15a0b3530.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8213c7165c29ba36d097c313da5795d0098ab1b157a1eb9720ceab516604619b.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/82c652bf80410a7cfcba7dcbaff6ca7fb5365a4331734e94e2e109afed315fe3.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/84cf547032e5b118c9a190ef81df51cbf977aeb0696a6aa7de7e15d29914bd42.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8707d63e29597f179f68ca03f13dd62fe55e3c50b869531999898783bbd33e4f.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/87adc8c27d46ed24d34925ac0f01ededf057835e5d7993010bb310d7d5df2bd7.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8bc71d03136774789df2eba4e7484ee725447216b57ac49a5370223ead9ae236.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8c8e4225bd156504c3a5982eac566ab5f99dc7946e64378e2d8fd8bb8b296d92.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8e4830851a2e1d0e6bb1e31828ecf950be79beb6490637164bcfc87b1e5467df.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/8f1e40a4dbe05bbb614f445563ea33a6c9bf27ed250b287e1758178edf3c538c.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/933f3a853bdb517eae2d348e1e0a1dd73e85c46b92c66c997a0a1477a820f2f6.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/96447ca22d9f7aa0112c920dded856d63ee061e8557c27e6c7620e52b366db79.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9801055aea637b0e6f765f1558113a9998fe6b4d5a213b0d03d096fe96cb4cdb.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9951cf3d62c8763b671d014814fdb2777b4d5bff62c874ee7eea3215f95a8b35.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/996d947e8ac9f95dcc1ebfd193eaab877ce7e1d4fa4651196c8a269f4e390895.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9d7fae05a847679be328f0c38deabd7bebbe2aa84c606920c4de57620f686a45.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9d8db03a1cc81d6ccddc60a462a1f72b732be8d9fc1d7e350e2b9d9187f4c2e1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9e394eb08986a678d53b329dc13f5e8a4e40ac6651c717df12035824b9de1003.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/9eadb05f055abcb7d7288dc1792c718b45e6d3df29cdadc91950591a1f4e6434.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/a0a0aeacf418d3de567c1ed47be27d8fdfd58478b538c0f541b90d2373925096.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/a1612c82ad7a367617f3da3eb57ee8a192b46bacc87846afce52dda2b48af0df.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/a76f8e787acdf99669a896b01e3f35587ab86f6cc074f62ee39b3c95c0349954.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/abc619db587eed6d3be170b90dfceffbc4e5a18311ced10c1e3636efedd31046.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b114c205f7e6eb2c434b92d1832776918710547a4b4a03fd8cb06d23fd85055c.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b127e17df183662e53446215bdc38dbbebfd76ce1972e03066a6fb7584ffc43e.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b39f1f41c5406fee5bf3463c1f48ad8e485e3ba850b015f590017e2fb81e372f.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b3b6cb24b1f89396921fdcae7aea2394b4d4d7338bda0d1e1877a1a997a78be1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b4b2c5fcb89a3ec511c3f80876d7c0984aa546d4bd2d449adf613272369d3ef5.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b4ed230f860a3111e1ddd2ec4d7092590d5976729c06e8eb249badb917282052.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b7ed443212fbdb5c9ecea51b77b46d990e7404de0cdb01d93f00b16d705d1bc1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/b98bd925a0b72b556c507ae349fb34c112d4d5c2603c92b311b90c7234a15ef2.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/ba62702d9cd01b3e3c0eb02cecd2eccfe7eeead85c24a5981890980e03bddc7e.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/bd336a4e74cb302698bc7e644f6c3d19a398886d5b3442bbf7b8a045236abb54.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/bdca2229ea0694940aac64600289742dc39ce6c9d8a5ae72d83d77507c1c3746.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/bf80281ef867f677d1853e8b7a950d272be805789539b240b867da7f29d2ae7a.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/c1c8493a8e309bf1a6c57903c06b1670a60dbdb028edac581bcf331fe502c103.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/c228e6c0f4c08482fc1378926e7c32235a33e230e8905a857e2788192de2281b.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/c26f7b5493c1ea8b4025da764e6e4d721097093bef7a55210be485df0d148e75.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/c2d7ddbf7ed8fa17290247c072f711fc0b603fea025e86bc219b2ac6cf7206ae.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/c5afb3bb33ad98d135a14bc4a31f910f3a492c35b3661c55b70b82b52abaddd1.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/cbe537bd2f0ac5ebbf73c0e8f8359ccd3641dae354d9c89d4ecfb9124ac604ad.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/cca7b573a08ce89b332bde9443cd6928c3f8dc67634462f7a0244edf6e75b218.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/cfdd2640e810987e49ed0e9c54086c9e821a1c286750712269f8ffac5f788693.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/d3e1c28b5b0883581c5b095ba1e4d5e4d527179be691ff877ef6c16ea9f3984e.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/d8fe32afaecc742f9905e88f3289de24f8bd9a1a8d0aa400ddbcd980ac000c81.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/dbe98822bbc21c0765aa9042927f89bc3cc455e01d563843cefe735fd7adac08.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/de926921cfcf65a1b31a569e475ba0c703d99d3f45c432406cae5f5262d7ec86.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e18a83b5f5ec44d280b3fb0d71921be50d2387563fb9887e223da33c190e8ecd.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e3985930b9542d48a21e411b5e678b1422f1aa12ee7c095cc30627c246e00cec.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e4340f4c7b645b2bb78066429a77864d8cd1baa2e9b53dc636b5ead607b4d93b.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e49e5ee4d121cafc621eab57f185b38ad3e330fa4621fe94272410c681dfcd7e.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e94523325fe80daacbc1d291de59b666bf3e473517b95512d7ea9ce213a39ea4.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/e9508586f92a42cf5cc9782b84f66bfc97bd9ba890b18e97931572e2b5f350c6.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/ea35a8e6c7333ac9b2ff11e38cc2100e8cde9244a82dac81c05bb7275d138bfc.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/eb80b938afefad32f2206aaef54568d538279d23dedd095b218bcd3a1bd2168d.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/fa69d32f055e84571308187b07ce8baafb8ebeeaaa7020d516990430e19d3ce0.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/fd129e22be5cd4e660d9402104d3ab0bc93325baad0a69b7eb99c985a934e956.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/fdb9dbf2661fd3560922e1060ea3ffd5ddb0d2ca0cf3705249cdc3bb0915ea64.gz', '.claude/science/physics-loops/toe-static-historical-reader-20261015/archive/ff5112eb07a4bb6d73e01b5ea72e140a7f67d4464ee80a3a40354e9f3d695c56.gz', 'docs/LOCAL_ENTANGLING_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/STATIC_HISTORICAL_PAULI_READER_BOUNDED_THEOREM_NOTE_2026-10-15.md', '.claude/science/physics-loops/toe-static-historical-reader-20261015/INPUT_MANIFEST.json')
EXPECTED_BINDING = {'branch': 'physics-loop/toe-static-historical-reader-20261015', 'observed_base_head': '9054ebdc341b7fb593e38dab3880eddcd20354f7', 'observed_base_tree': '3689f9d7372d0ecd1e5be835e20d931c38353fef', 'base_branch': 'physics-loop/toe-local-driven-readers-20261015', 'base_pr': 9595, 'feature_head': '9054ebdc341b7fb593e38dab3880eddcd20354f7', 'main_observation': '92574ffe95192cc0724a27e1acad28e42d325115', 'instruction_observation': '3a4b2c66a1ead7a1c48b4359627e968f681e3c39'}
PROOF_ALIAS = 'local_clock_autonomous_reader_phase_revision/AFTER.md'
PROOF_SHA = 'fdb9dbf2661fd3560922e1060ea3ffd5ddb0d2ca0cf3705249cdc3bb0915ea64'
ACCEPTANCE_ALIAS = 'local_clock_autonomous_reader_root_review/ACCEPTANCE.md'
ACCEPTANCE_SHA = '2bc76aea5d586a054a3797e59aaacfe6d6187a6e72e8705ff9a569cbca6d909d'
EXPECTED_CLAUSES = {
    'premises/four_rail.md': ('docs/LOCAL_ENTANGLING_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 12329, 24737, '2c95a969f8d8f40f4190ece9f25d811c7e204a4f68de722f3fe393265b2c8115'),
    'premises/compact_counterexample.md': ('docs/LOCAL_ENTANGLING_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 24800, 46092, '6085f0118c8eb7fdac3b757f686f00e3abde4b48ea1ac6883fc42d954c42a543'),
    'premises/shared_head_method.md': ('docs/ORDERED_LOCAL_CLOCK_WORD_BOUNDED_THEOREM_NOTE_2026-10-15.md', 36233, 66890, '6d45cddc031e90e3667cb7de790d1f53c0b74687232023bf2e28307f8c428e0a'),
    'premises/positive_lift_method.md': ('docs/LOCAL_PAULI_CLOCK_CELL_BOUNDED_THEOREM_NOTE_2026-10-15.md', 25189, 52484, '43de02b9feab4d9127533401074cdb018b16da14ef1d57828e7d1989fc5becb5'),
}
EXPECTED_GROUPS = {
    'local_clock_autonomous_reader_candidate': 53,
    'local_clock_autonomous_reader_decisive_check': 83,
    'local_clock_autonomous_reader_phase_revision': 17,
    'local_clock_autonomous_reader_root_review': 11,
    'runs/local_clock_autonomous_reader_root_close': 4,
    'runs/local_clock_autonomous_reader_root_seal': 4,
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_inputs():
    raw = (REPO / MANIFEST_PATH).read_bytes()
    assert digest(raw) == MANIFEST_SHA, 'input manifest identity'
    manifest = json.loads(raw)
    assert manifest['schema'] == 'static-reader-inputs-v1'
    members = manifest['members']
    assert len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
    assert set(AUDIT_INPUT_PATHS) == set(members) | {MANIFEST_PATH}, 'declared literal input closure'
    data = {}
    for path, row in members.items():
        assert not Path(path).is_absolute() and '..' not in Path(path).parts
        b = (REPO / path).read_bytes()
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'input identity: ' + path
        data[path] = b
    index = json.loads(data[PACKET + '/SOURCE_INDEX.json'])
    assert index['schema'] == 'static-reader-archive-v1'
    assert {g: r['file_count'] for g, r in index['source_groups'].items()} == EXPECTED_GROUPS
    originals = {}
    for alias, row in index['originals'].items():
        assert row['stored_path'] == PACKET + '/archive/' + row['sha256'] + '.gz'
        b = gzip.decompress(data[row['stored_path']])
        assert len(b) == row['bytes'] and digest(b) == row['sha256'], 'decoded original: ' + alias
        originals[alias] = b
    assert len(originals) == 191 and len({r['stored_path'] for r in index['originals'].values()}) == 112
    for group, count in EXPECTED_GROUPS.items():
        subset = {a[len(group) + 1:]: b for a, b in originals.items() if a.startswith(group + '/')}
        assert len(subset) == count
        if not group.startswith('runs/'):
            frozen = json.loads(subset['FINAL_FREEZE.json'])
            assert frozen['file_count'] == len(frozen['files']) == count - 1
            assert set(subset) == {r['path'] for r in frozen['files']} | {'FINAL_FREEZE.json'}
            for row in frozen['files']:
                b = subset[row['path']]
                assert len(b) == row['bytes'] and digest(b) == row['sha256']
    body = json.loads(data[PACKET + '/BODY_MAP.json'])['complete_proofs']
    assert len(body) == 1
    row = body[0]
    assert row['alias'] == PROOF_ALIAS and row['sha256'] == PROOF_SHA
    b = originals[PROOF_ALIAS]
    assert digest(b) == PROOF_SHA and row['bytes'] == row['end'] - row['start'] == len(b)
    assert data[NOTE][row['start']:row['end']] == b and data[NOTE].count(b) == 1, 'complete proof interval'
    assert row['end'] == len(data[NOTE]) and data[NOTE].endswith(b'\n') and not data[NOTE].endswith(b'\n\n')
    binding = json.loads(data[PACKET + '/BINDING.json'])
    assert binding['binding_complete'] is True
    assert all(binding[k] == value for k, value in EXPECTED_BINDING.items()), 'dated feature binding'
    assert binding['feature_head'] == binding['observed_base_head'] and binding['publication_pr'] is None
    assert binding['root_runtime_freshness_and_stack_binding_pending'] is False
    assert not binding['finite_reservoir_imported']
    assert binding['base_is_mathematical_dependency'] is False
    assert binding['new_scientific_programs_run'] == 0
    assert not binding['reset_theorem_imported'] and not binding['unchanged_boundary_clock_retained']
    assert binding['conditional_acceptances'] == {ACCEPTANCE_ALIAS: ACCEPTANCE_SHA}
    assert digest(originals[ACCEPTANCE_ALIAS]) == ACCEPTANCE_SHA
    clauses = binding['exact_source_clauses']
    assert len(clauses) == 4 and {r['alias'] for r in clauses} == set(EXPECTED_CLAUSES)
    for row in clauses:
        assert (row['canonical_path'], row['start'], row['end'], row['sha256']) == EXPECTED_CLAUSES[row['alias']]
        b = originals[row['alias']]
        parent = data[row['canonical_path']]
        assert digest(b) == row['sha256'] and parent[row['start']:row['end']] == b and parent.count(b) == 1
    return data, originals


def checked_archived_receipts(data, originals):
    archive = json.loads(data[PACKET + '/ARCHIVED_RUNS.json'])
    rows = archive['actual_attempts']
    assert len(rows) == 11 and sum(r['scientific_attempt'] for r in rows) == 1
    assert sum(r['expected_exit_code'] != 0 for r in rows) == 1
    for row in rows:
        receipt = json.loads(originals[row['receipt_alias']])
        code = receipt['returncode'] if row['shape'] == 'author' else receipt['exit_code']
        assert code == row['expected_exit_code']
        for stream in ('stdout', 'stderr'):
            b = originals[row[stream]]
            h = receipt[stream + '_sha256'] if row['shape'] == 'author' else receipt[stream]['sha256']
            size = receipt[stream + '_bytes'] if row['shape'] == 'author' else receipt[stream]['bytes']
            assert digest(b) == h and len(b) == size, 'recorded stream identity'
        if row['shape'] == 'outer':
            prefix = row['receipt_alias'].rsplit('/', 1)[0]
            child = originals[prefix + '/executed_source.py']
            assert digest(child) == receipt['child_source_at_launch']['sha256']
            assert len(child) == receipt['child_source_at_launch']['bytes']
            assert digest(originals['procedures/root_recorder.py']) == receipt['recorder']['sha256']
    source = 'local_clock_autonomous_reader_candidate/'
    pre = json.loads(originals[source + 'PRECONTROL_SEAL.json'])
    run = json.loads(originals[source + 'logs/selected_control_01/RECEIPT.json'])
    assert run['returncode'] == 0 and pre['sealed_utc'] < run['started_utc']
    assert len(pre['files']) == 8
    for row in pre['files']:
        b = originals[source + row['path']]
        assert digest(b) == row['sha256'] and len(b) == row['bytes']
    result = json.loads(originals[source + 'logs/selected_control_01/stdout.txt'])
    assert result['source_sha256'] == digest(originals[source + 'selected_control.py'])
    assert result['input_sha256'] == digest(originals[source + 'CONTROL_INPUT.json'])
    failed = json.loads(originals[source + 'logs/source_capture_01/RECEIPT.json'])
    assert failed['returncode'] == 1 and b'FileNotFoundError' in originals[source + 'logs/source_capture_01/stderr.txt']
    return {'scientific_attempts_preserved': 1, 'scientific_attempts_executed': 0,
            'metadata_attempts_preserved': 10, 'failed_metadata_attempts_preserved': 1,
            'historical_limit': 'Original scientific child launch identity is not retroactively strengthened.'}


def checked_phase_revision(originals):
    group = 'local_clock_autonomous_reader_phase_revision/'
    before, after = originals[group + 'BEFORE.md'], originals[group + 'AFTER.md']
    assert before == originals['local_clock_autonomous_reader_candidate/DERIVATION.md']
    part = json.loads(originals[group + 'REPLACEMENT_MAP.json'])['ranges'][1]
    old, new = part['old'].encode(), part['new'].encode()
    assert before.count(old) == after.count(new) == 1
    assert before.replace(old, new) == after and after.replace(new, old) == before
    left, right = before.splitlines(keepends=True), after.splitlines(keepends=True)
    assert len(left) == len(right) == 328 and [i + 1 for i, (a, b) in enumerate(zip(left, right)) if a != b] == [155]
    formulas = [line for line in left if line.startswith(b'    ')]
    assert len(formulas) == 97 and formulas == [line for line in right if line.startswith(b'    ')]


def main():
    data, originals = checked_inputs()
    attempts = checked_archived_receipts(data, originals)
    checked_phase_revision(originals)
    print(json.dumps({'result': 'source_identity_binding_completed', 'decoded_originals': len(originals),
        'complete_proofs': 1, 'scientific_programs_run': 0, 'dated_feature_binding_complete': True, 'archived_attempts_not_replayed': attempts,
        'scope': 'Literal source/interval and actual receipt identities only; zero mathematical predicates.',
        'limits': 'Conditional replacement clock and historical coherent record. Supplied clean pointer/clock, full finite costs and actual time; no classical detector, reset, permanent memory or native realization. Dated feature binding is separate from later publication; ancestry supplies no mathematical premise.'}, sort_keys=True))
    print('per_element: arbitrary old input/reference; supplied clean pointer and one-head clock')
    print('per_site: occupied original chain retained; L+4n+18 eligible fresh sites and L+4n+27 selected ordinary edges')
    print('per_mode: full-space apparatus positivity distinct from one-excitation prepared-map domain')
    print('per_block: historical coherent pointer blocks retained; no postselection or physical outcome reader')
    print('lattice_wide: fixed finite n and finite window; growing strengths, scalar and energy costs, no efficient/native closure')


if __name__ == '__main__':
    main()

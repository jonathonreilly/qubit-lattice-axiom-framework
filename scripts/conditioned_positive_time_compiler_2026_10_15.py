"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-conditioned-positive-compiler-20261015"
PARENT = 'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md'
EXPECTED_PARENTS = {'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md': (136036, '9b08b7a78f21390d065322150d1fe6a222343323cc76dfe7f3b065a624d5a18e', 'single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15')}
EXPECTED_ACCEPTANCES = {'conditioned_compiler': '9f90d834ef33e01300eed265e196df1f8d66ec92f846bfa96d30716d7d25790d'}
EXPECTED_GIT_BASE = 'd7df9087a06d772bc7c7a443e479149a30f385fb'
EXPECTED_BASE_PR = 9621
EXPECTED_BASE_BRANCH = 'physics-loop/toe-polynomial-path-mediator-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-basis-state-clock-20261015'
MANIFEST_SHA256 = '72e3b156c002e44959246cfe8f44769825dbf0803d99f5b316158c94da232206'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/0409c0fc13fda1091e245958cffa67dfdfdf86e2ad9ee247349cb5a10b420814.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/0cdc01cd5b26bc48f250e5a854d93cb41ed3c135ae1a7dfed24be9d0e7d8c8fd.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/0ceb6356f19d41a423218f4f655afe1fcdd23e5093abc87b93436e89787f3e58.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/137a053a187876c9540c9a2f3efcc60d03af6cb2b5da28398c86b86d8981e3fa.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/283c0c87214ed8fa4d863ce217026f306c104ca011ba9868d82d4e3ff42e5f54.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/33b62c769b732593761bc6d503bd6218c8a88fb8e721b5a63c344bc119e028c9.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/3a0d721d371deefcdabc3db2733f42a8a4f9c363881a554d7ca7ac5469ca7d44.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/4473e20fa0b91406fe1c8706dd906143ceae6ba6dbb6eedaf700c47cbc08521c.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/51ffee6b82f62b65ae08940ad05b60cac4c39fe83588ccc0b2d3783ec949506f.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/58be88b6b396bb2cb30017819e083acf6932a1ed43b51ccebdb3d7a768887c4a.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/5b4bfd031c00a6727b4062419ebfe6a14066321d41db80ec0b105031fa54d08d.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/6115a3e6170855873d90fef2cd85f34dd8fa80e3f791defda585b6139f73abf4.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/62e3fb9432267ccb9af467a1ad074d9eb41078f3d3e2d24a4f8e1b8cb7e883ec.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/9325a8bef9e59a6d539154deb5d04df7c95c568bb9819f3a2736bb19faa5672b.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/b0ae046e02283d56c3a7b08e8aef2d7504ae525671eb7c7b6c374d8b069b7aae.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/b6b640a56c07a0a807e9c06ee4e56bae223b187a65ced63e07da60cb13e880ef.py', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/dc9b107da542e9e3217f723d0d75fff7adf9d60908d2ce33fe22d27433b5bdd4.py', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/df25ab872e8e2eca145172e54d8db83470f998f70e99a7c38cc9a2d89c8ce2b7.json', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/binding_sources/f04da9a0cd7760a1950fe6c592051486a5cb5e559be9540937b2682661c79ffb.py', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/01283fc08f7ed41d1e2525823043773c344f494adebc968069fce4c47a5ee790.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/062f93d6050b8320a47bcea056490d7ab5be760578925fa90ba89d5c00c7adc5.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/0723eee41c7d2e1c309c7b434666051853ebacb848c9e1eb6284bd0aa6d3e655.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/147a0528a96ecbbba510b4e57a885e5bce504a585c9930d4095c0b1fa3f2c83d.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/2099790774c866ba2debf24b13a6b9a81e2b8c017ab72e60bc29346c9a56ec8e.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/20d19c530c6f53eec6ff645c1c1e8b0c3e3f04c21f5ca5e40ea56fb8b67ba7bb.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/29d60870be44b3675bcee75b0dc0d917176498021cdff447025e65206478178e.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/2bb64dad8d58252a8ebb51c51d8c4db3c3132be19dce697bb9947d2bf3b5dc7f.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/3a2ffb101da380f47c390a059fffcc1df6dade3571ee9c7ef494e246cf3eed03.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/3bae7bad93ad1ada04012de08dc5db818acbf6828f716fa965a63f4d66c332ca.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/554ebf82ef443e3f97073bf86c67ae5b946f7d8960b0703665dde49b8b7045a3.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/57e7952202ef634c4c6da7841166177c1950dc2c9c81236499f4f6f8e1977922.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/586523f983bef60f52cd76d235074f98ea05a4a114475d349b59b36953edb47b.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/5a9db9605466bd03d70cf69b93cfbcda04b3f87d02b89d4acb68cf99a971aca5.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/6f82e3c2f85029972b6db153b4dee657a733ec426879d63ace058b2d6338b716.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/77e4c7ee4aa07b263d9264eaad9d7b6778348eee0111730408159e50cfebe2d3.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/7dd48ef56f4730fda276d707d637673853f9fd8af12af58eac0fa28bcf3659cf.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/83a15498975a7214727e923abd89e299368e5cbdbb54fe3a72460295230a28cf.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/8ea1cd436ad9e1529a6bff618a12b8e0d5a449bfbc2d36490a516820ce0adc75.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/9c6f5d32a7c821b32785ad3fa58fbf3c874c5e5edd4686ae4b85c393c4d68ad8.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/9d8a9140c7a3869e3db33e25c86b649b2e0c2873b8f41aa186af12b9ac4ef1e2.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/9f90d834ef33e01300eed265e196df1f8d66ec92f846bfa96d30716d7d25790d.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/a5b7a6c908db85f809619ddd00240058ea6f77feb1684fc32cafe13303c7a692.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/a87cefdcdb0a343d551fa6f3e963a1c9d1d68621fcd7db35473b45f94f4c3d84.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/ac640003d9322cb9d890b574ad7a7456ec30e4bf2c6a569f9c7eaf9f2a9afa44.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/af1cec2427a279585adbb637fffed02d348593658d46e2578d0f2ceca1adb5da.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/b55d8c220b8785fcfd72eea915492eed36066d979f048735958aa86dc978983f.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/b68de282b4cced3aedf8247355a37cf66381493259853c52ef631b03f745656e.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/baebd00dc3a9e597c36e66a0a8ebc9d3a74c842d371b3ccf5ea8008441e00e21.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/bc512e3ef95149b2fb7d5717996eab2a111a6f3d0fa13fd5d7c6094d4ff86fce.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/bd938cceb5738bd27cf22862a07545771447f439029409a7dcf5ea3658634d7e.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c16cda8db86834ee4cc00bd73fe3bc283073bdf38debffb1201c6b46e6eec025.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c60c74ebac71d61f0f7fc25ff051854817ba4e5d7e0452dcbb3910feee7cce41.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c67cc21328b18f059f8d91b77f9483c6652c3ca29ca4d4df4cf4f320406c8837.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c707dc710885a6c2b988454a98667abc9a0e0c364fe2dbcf6832489cff464e4a.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/c782654366b4a6ee865d7fd09db31cc6b61559fc39982b187d1c41c19942e1d9.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/d30ed09efe424a00942f79df8c4d94ab4f5a2e82dcf6f4a79a25365628a03048.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/db7b2b696bbbb59e09f9b5c9bf41df61f0f95f66cbe31bc357ed363929bc64e0.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/dbdd8110b702f59c0b48622d7226da3c6f3690e7dc77e988a1fafed055126750.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/df7655f7ed72b70c7810d1ebcbc63990cb0ccd5ac73e9b4e39fda37bc51663bf.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e045efb5a14cfe89095a62a1335d72cd91d6f6c9b602eb721d9af3de5c86e4db.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e1e7dd539129771cb7f6f37a019563dd957c84915960cd7a7dc0133a37ac8ce3.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e3751f20dcbd66e509afbf8cd74494d72fa32263e1c7d43530d3024f62db5288.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e42316f36326d22f2625a56659d3451e6763a8071a4eaa00c5c6bc94daf7e9b2.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e49ad0cd5e6031729fbecf236c61f973b74d0891491c18f43e6b79fafcb7844d.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e6e1c8e0884b669aff569787685c5b12b1186ae2114428ac04015bb4a89442b8.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e71dfe0ec3333325a1caceedb7c325096281d6623c995a9f4def13aee5665aec.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/e7871e6d8a3caec3b9898149904d636d5a5b3e8714433ed92a57978acd971901.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/f66d10f661ba466095877f9bc6a166759010927802bd97677d1fe9c42a386723.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', '.claude/science/physics-loops/toe-conditioned-positive-compiler-20261015/source_recovery/fdc87d95ecd57b0f636a3507e7afdfc2e23579fe79171abab55bf891355bf932.blob', 'docs/CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'root_author': '2de387eb501aa8ead91afa1f5a26f7d3a0bbf11e51285d99786715152ad5b6d6', 'independent_author': 'dd6cca8552a117d97f7be21c7b999ecd2276382f6cc762954bd97d00e3a6ff04', 'comparison': '227180a0822eab4e3dbfc002b6604d914af23589c29add9cca71e1a2f3ae2db0'}
EXPECTED_PARENT_BODIES = {'compiler_author': (33757, 'bda0be884fa79905ff81f0a2642def9e2efd5302796262f5f9eb4033b2c436c0')}
EXPECTED_PARENT_REVIEWS = {'compiler_assessment': (27426, '3ad0ab6540ba9fae892824119aafa6c4e61ca16892ba3d23a7c59f95df82e7b5')}

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
    external=set(EXPECTED_PARENTS)
    expected={r["path"] for r in rows}|{mpath,actual}|external
    require(set(AUDIT_INPUT_PATHS)==expected and len(AUDIT_INPUT_PATHS)==len(expected),"Literal declared-input closure")
    for row in rows: identity(safe(row["path"]).read_bytes(),row)
    note=safe(NOTE).read_bytes()
    header=note.split(b"---",2)[1].decode().splitlines()
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false","runner: scripts/conditioned_positive_time_compiler_2026_10_15.py",'upstream_dependencies: ["single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15"]']:
        require(field in header,"Missing actual scope/binding field: "+field)
    body_map=read_json(PACKET+"/BODY_MAP.json")
    require(body_map["note"]==NOTE,"Body container")
    require({r["name"] for r in body_map["bodies"]}==set(EXPECTED_BODIES) and len(body_map["bodies"])==3,"Exactly three immutable bodies")
    for row in body_map["bodies"]:
        require(row["container"]==NOTE and row["sha256"]==EXPECTED_BODIES[row["name"]],"Immutable body identity")
        interval(row)
    parents=read_json(PACKET+"/DEPENDENCIES.json")["dependencies"]
    require(len(parents)==1 and {r["path"] for r in parents}==set(EXPECTED_PARENTS),"Exactly one direct mathematical parent")
    parent=parents[0]
    require((parent["bytes"],parent["sha256"],parent["claim_id"])==EXPECTED_PARENTS[parent["path"]],"Parent role or identity")
    identity(safe(parent["path"]).read_bytes(),parent)
    require(parent["required_mathematical_body_names"]==["compiler_author"],"Only the qualified full-plant compiler proof imported")
    ranges=parent["accepted_body_intervals"]
    require(len(ranges)==1 and {r["name"] for r in ranges}==set(EXPECTED_PARENT_BODIES),"Parent proof interval")
    for row in ranges:
        require(row["container"]==PARENT and (row["bytes"],row["sha256"])==EXPECTED_PARENT_BODIES[row["name"]],"Parent proof identity")
        interval(row)
    require(len(parent["review_evidence"])==1,"One exact canonical separate review")
    review=parent["review_evidence"][0]
    require(review["container"]==PARENT and review["name"] in EXPECTED_PARENT_REVIEWS and (review["bytes"],review["sha256"])==EXPECTED_PARENT_REVIEWS[review["name"]],"Parent complete review identity")
    interval(review)
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
        else:
            require(recovery["kind"]=="external_pinned" and recovery["path"] in external,"Unknown external input")
            identity(safe(recovery["path"]).read_bytes(),row)
    mapped={r["name"]:r for r in body_map["bodies"]}
    for row in sources:
        r=row["recovery"]
        if r["kind"]=="body_interval":
            require(r.get("body_name") in mapped,"Source body-map linkage")
            b=mapped[r["body_name"]]
            require(all(r[k]==b[k] for k in ("container","start_byte_inclusive","end_byte_exclusive")) and row["bytes"]==b["bytes"] and row["sha256"]==b["sha256"],"Source body-map linkage")
    for member in read_json(PACKET+"/RECOVERY_SELECTION.json")["members"]:
        r=member.get("recovery")
        if r is not None:
            require(any(member["bytes"]==s["bytes"] and member["sha256"]==s["sha256"] and r==s["recovery"] for s in sources),"Recovery selection linkage")
    state=read_json(PACKET+"/PUBLICATION_STATE.json")
    require(state["kind"]=="dated_source_proposal_not_actual_binding","Historical state role")
    for field in ["canonical_binding","git_base","primary_execution","cache_execution","mutation_execution","graph_execution","publication_action","retained_audit"]:
        require(state[field] is None,"Historical null state must remain null: "+field)
    require(state["scientific_programs_run"]==state["historical_programs_replayed"]==0 and state["autonomous_clock_imported"] is False,"Execution and excluded-claim scope")
    require(state["source_acceptances"]==EXPECTED_ACCEPTANCES,"Historical actual source decisions")
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and isinstance(EXPECTED_BASE_PR,int) and isinstance(EXPECTED_BASE_BRANCH,str),"Root must explicitly pin the actual Git base; source proposal has no chosen base")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding required")
    require(binding["root_read_complete"] is True,"Actual root publication inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES and binding["git_base"]==EXPECTED_GIT_BASE,"Actual source decisions and base")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_conditioned_positive_compiler_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
    require(canonical["bound_note_sha256"]==digest(note) and canonical["actual_git_base"]==binding["git_base"] and canonical["canonical_parent_sha256"]==binding["parent_sha256"],"Current binding identities")
    require(binding["raw_bodies"]==body_map["bodies"] and binding["canonical_parents"]==parents,"Actual body and parent structure")
    freeze=json.loads(bound_blob(binding["source_proposal_freeze"]))
    require(freeze["immutable_bodies"]==3 and freeze["mathematical_parents"]==1 and freeze["scientific_programs_run"]==0 and freeze["actual_binding"] is None,"Historical proposal seal scope")
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
    require(result["members"]==247 and result["sources"]==84 and result["exact_functions"]==33,"Actual reviewed source counts")
    review_seal_raw=bound_blob(evidence["review_freeze"]);identity(review_seal_raw,result["freeze"])
    review_seal=json.loads(review_seal_raw);require(len(review_seal["files"])==1,"Actual review seal membership")
    identity(review_raw,review_seal["files"][0])
    require(binding["autonomous_clock_imported"] is False,"No excluded mathematics through Git ancestry")
    receipt,observed=execution_evidence(binding["base_observation"],False)
    require(receipt["argv"]==["gh","pr","view",str(EXPECTED_BASE_PR),"--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual base observation command")
    require(observed["number"]==EXPECTED_BASE_PR and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]==EXPECTED_BASE_BRANCH and observed["baseRefName"]==EXPECTED_BASE_PARENT_BRANCH and observed["state"] in {"OPEN","MERGED"},"Actual base PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding["base_observation"].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(path in AUDIT_INPUT_PATHS for path in used),"Binding evidence literal closure")
    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and captured binding evidence only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: certificate, pulse, duration and scalar ledgers preserved; no gate or physical element run")
    print("per_site: fixed filled-box NN path and one onsite port preserved; installation and isolation remain supplied")
    print("per_mode: full-plant and augmented actual-aging distinctions preserved; no simulation run")
    print("per_block: three unchanged bodies, one mathematical parent and separate canonical review checked")
    print("lattice_wide: no native waveform, uniform-lambda or large-system efficiency, autonomous clock, common-cap, detector, reuse or retained audit certified")

if __name__=="__main__": main()

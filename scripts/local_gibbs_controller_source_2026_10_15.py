"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import gzip
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/LOCAL_GIBBS_CONTROLLER_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-local-gibbs-controller-source-20261015"
UNARY = "docs/POSITIVE_UNARY_CYCLE_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md"
EXPECTED_PARENTS = {UNARY: (42367,"fa7028e0e9ad6c2c7d4c1c399feae8f9581f301dda5b46f8800eb6c355137542","positive_unary_cycle_clock_bounded_theorem_note_2026-10-14")}
EXPECTED_ACCEPTANCES = {"local_gibbs_controller":"c2e7680d5a133ca950483f07036e7ef5879871a83e439c490c4bd1c919833537"}
EXPECTED_PARENT_REVIEW_COMPRESSED = (12394,"736e2741a361d4630c8a62be986382fb607711889745ee1a2fdaba882a2b6cee")
EXPECTED_PARENT_REVIEW_DECODED = (29118,"8d76345b8a28d7d9a80675dda5ee8b1d3f9964994375bae852f02ea084a9a7b3")
EXPECTED_GIT_BASE = '86eac8cc4523f7f15c8d84824f462f9a5c037806'
EXPECTED_BASE_PR = 9617
EXPECTED_BASE_BRANCH = 'physics-loop/toe-single-port-program-and-controller-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-transverse-field-memory-20261015'
MANIFEST_SHA256 = '0aecfef4ef6cfbcc986ad7abeb7cb1e9b5786c5ef00f1b3d8e0828bf0d06cbb4'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/PARENT_REVIEW_BINDING.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/07fe994aa80009c71c6d868c3b3f48e1b0d1bed3ad60e7e639cd0ad2d1f5a8ce.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/2efa0c4821c9d3ccc01bf61afbe537c10a16b2ffc5029d93db9fa56e8dc978bd.py', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/513948f73233c8a6868405f3a822599d5e76452aa986533c341d3adfa48c1806.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/57e7952202ef634c4c6da7841166177c1950dc2c9c81236499f4f6f8e1977922.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/7cb943ff2b8a8ca88f13dee7fb54510cf36e88c078d6cf65cb6dcf4a9763d43a.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/a97b0287d16df1db6e6acc8a2a62ba30356555980de6973e6e0677b4663b933c.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/bf8a0ef9aeea39ee2fa902ae70cd5c5a1c3e4e514f4652d7756acfc0e8454c03.py', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/c1a78b657c4d41c2b18bd1e9d90a6705cd4446abc170874dffb23e104723da28.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/d4dd8e003d0870bf93a6a8d1ce5b07f82e1010b1d5eeaeb06f9c5d30c577a6cd.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/d54a4a8b37085ed737df451e55e0f202d5b0f95d8287a4ceccfd88148b2b6676.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/d72d85c8d7112546d92993bc023ee3dbd5c0de6b1fa53e75ea7bfa8c66bcfbd3.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/e045efb5a14cfe89095a62a1335d72cd91d6f6c9b602eb721d9af3de5c86e4db.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/e729fa28ed25d833e54c95d828be5bec6fee93711692b0e39352aaadfb7ce440.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/f2fac13228af7cce764dd69e4f1f1ca3e165cfc2acca26a4f57965bc73aefb1d.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/binding_sources/f48dc581b628b01203bae933c8d768d12f2116e6207cd8e702bf06a3afa11c14.json', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/0c0e6299eb8ce1f33fb6326c74013a22bc0fc5d1c4bf2b9433bca2016ebeef08.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/1134a35c531f39848e04bab2185c59a2aacd2f867a6142a8c73d4eefbbbd189b.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/1217498d36a7bc38d92a9b2cf2a2e29ec453bd53373112810315dbe0349ab302.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/1a7f61fe09c729f35943e73c596ea3564ebcc833037475332921b66d9099bbab.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/1dc70fe970de23533ad5604d4cb85d94ddf3e9dcbd4ca3368aba04fe464e16e5.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/27cf1cef03cdac9914e503731b0f053eea993b55f862f7df40a85336a40f1859.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/2a61c069caae5e7d3a4a63d2f7595eb92e9e54a2bffcc054f7cee3a586df1a87.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/3296ddaa7ce6c97e45cee7e1654467633685f75a944daab4e424e825b439b19d.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/32f18faf93644d5b32e35b9a60787297c00e07e612d4b8426a9ed5957b8d2db8.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/369360e11586200f363bb9087a6e2880255700eab2821ff5198950e72c85a567.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/395deb75d4d733683c51ba18a53fa3d1735cc86f62112c2f0c5d7fb2e94a4273.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/3c76519db1ee43435446f62d78880f4a078338591a75f493c581bb4aa88defbe.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/4616ac0e6ec7df04f063f6aa1b50c0bb09b45fe04f7026a958bbc76ccd2b7fb6.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/48267575a9d77db69bf1eea0d73050262051429fecec585dfbc09a1a08a71863.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/500621a53201e6dee054b6cf01d24647d952554016c3c340777ea8aada612679.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/5282fdefb2c4ad07378651132923865dfca4679680b588a9337267ff0acfa6ab.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/53eb8ab72f253269f654ec45a6dea92c5d112cec14264484d7e652fb46010306.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/656357ca8416febc385119582e14dd1640fca84d30659d0509c3cef4f36cff53.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/70264c3a9c76dccd9a5b561af70d3963a733b450cfdbb6394e6d06474ae4ee0e.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/736e2741a361d4630c8a62be986382fb607711889745ee1a2fdaba882a2b6cee.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/73f5f53d2cddb066295a8042816060f95a9769e48a2079e56a3636f4c8905645.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/75f6082dd4b7c31737a3fe426a714647f83299be418c7f339729de6b3b74158e.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/76774c73b07811df42460612bd104e0c9d64279871005a7e5ba5bee95e9dcf6c.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/7b58d56405a7807b67039577b65ae3539a2221e42575b08e6ec639fe6f039d74.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/8d76345b8a28d7d9a80675dda5ee8b1d3f9964994375bae852f02ea084a9a7b3.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/931a7565eb1d9c892c268898aa1b09df96e02db3b90dde196eba2b90048de1f1.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/977834884667414b48ab0501eabf8d4ad58df5d4e587040995b170eca8634133.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/a1bf5c76cd0f2fabf678251d869523b6480788767cc2d35987165d8ed8251e84.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/a7481d0fcd7db9e692fe48b6c021883607582aa1f7a3f22e0902a9c6a6f46b30.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/b726766403bf6f4b0080172d046cf773facad028eed538d7473417683b931bb7.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/b75159cd4f985feb6faf76863a7b279e26a93160aff5be9e9bc32e85bc9449bd.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/bbbd8f683c94a3feff8aaa25372f12d5ca3c2494fb50dac9e10f2413119aa3a5.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/c2e7680d5a133ca950483f07036e7ef5879871a83e439c490c4bd1c919833537.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/c36218bb3e5e096caebfb520212907f90c6851572528d10165d5b4fd1e27aa0f.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/c60a81d7fa057c0e99d3a33f3beb0682878e38b10ac118ffff60569b3b5207d9.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/c9c5e17680702e1dbafe8d8ecce823602dc717b674fa9f3abc8698b83ccaa77f.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/ceca11900946ddb6b4e9e542b1af3a2ac2c98eab167b90f89e9bdd403bab335c.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/d06649c8b8d9579fd8bd21c0a5e196975ce0d8ff2d869247829448aec6aceab8.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/eb08af71fdb97c736a17579a043c68ef7e917437ca8eeba3c06015126f978ede.blob', '.claude/science/physics-loops/toe-local-gibbs-controller-source-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', 'docs/LOCAL_GIBBS_CONTROLLER_SOURCE_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/POSITIVE_UNARY_CYCLE_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-14.md')
EXPECTED_BODIES = {'independent_normalized': '4e0c90fb7fa515868aaa491525e89c1e80014180e2e88189b32c07f04d2eeb40', 'root_unnormalized': '5a278bbd0f96eff93a2c506573898a9cb4b8cc2ffd8ac5d42d4ea2bcd17e712e', 'source_exposed_comparison': 'e36f9dd364a5846d66d2bc1a2e2529e39cfc5cff83b25b1a0e17bdfe1a87894c'}
EXPECTED_PARENT_BODIES = {'unary_cycle_proof': (33019, 'c7a19c3acb7d731a95b97bfadc8a32e2624196d60555ac08e8e77b3ad71d1135')}

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
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and all(c in "0123456789abcdef" for c in EXPECTED_GIT_BASE) and isinstance(EXPECTED_BASE_PR,int) and EXPECTED_BASE_PR>0 and isinstance(EXPECTED_BASE_BRANCH,str) and bool(EXPECTED_BASE_BRANCH),"Future base not supplied: root must bind and review the actual head/PR/branch literals")
    mpath=PACKET+"/INPUT_MANIFEST.json"
    raw=safe(mpath).read_bytes()
    require(digest(raw)==MANIFEST_SHA256,"Input manifest identity")
    manifest=json.loads(raw)
    require(manifest["schema"]=="source_integrity_inputs_v1","Input schema")
    rows=manifest["inputs"]
    require(len({r["path"] for r in rows})==len(rows),"Duplicate input path")
    actual=PACKET+"/ACTUAL_BINDING.json"
    expected={r["path"] for r in rows}|{mpath,actual}|set(EXPECTED_PARENTS)
    require(set(AUDIT_INPUT_PATHS)==expected and len(AUDIT_INPUT_PATHS)==len(expected),"Literal declared-input closure")
    for row in rows: identity(safe(row["path"]).read_bytes(),row)
    note=safe(NOTE).read_bytes()
    header=note.split(b"---",2)[1].decode().splitlines()
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false",'upstream_dependencies: ["positive_unary_cycle_clock_bounded_theorem_note_2026-10-14"]']:
        require(field in header,"Missing actual scope/binding field: "+field)
    body_map=read_json(PACKET+"/BODY_MAP.json")
    require(body_map["note"]==NOTE,"Body container")
    require({r["name"] for r in body_map["bodies"]}==set(EXPECTED_BODIES) and len(body_map["bodies"])==3,"Three immutable proof/comparison roles")
    for row in body_map["bodies"]:
        require(row["container"]==NOTE and row["sha256"]==EXPECTED_BODIES[row["name"]],"Immutable body identity")
        interval(row)
    parents=read_json(PACKET+"/DEPENDENCIES.json")["dependencies"]
    require(len(parents)==1 and {r["path"] for r in parents}==set(EXPECTED_PARENTS),"Exactly one direct mathematical parent")
    for row in parents:
        require((row["bytes"],row["sha256"],row["claim_id"])==EXPECTED_PARENTS[row["path"]],"Parent role or identity")
        identity(safe(row["path"]).read_bytes(),row)
        require(row["required_mathematical_body_names"]==["unary_cycle_proof"],"Exact inherited proof roles")
        intervals=row["accepted_body_intervals"]
        require(len(intervals)==len(EXPECTED_PARENT_BODIES) and {r["name"] for r in intervals}==set(EXPECTED_PARENT_BODIES),"Parent body recovery roles")
        for r in intervals:
            require(r["container"]==row["path"] and (r["bytes"],r["sha256"])==EXPECTED_PARENT_BODIES[r["name"]],"Parent body identity")
            interval(r)
    parent_review=read_json(PACKET+"/PARENT_REVIEW_BINDING.json")
    require(parent_review["canonical_parent"]==UNARY and parent_review["canonical_parent_sha256"]==EXPECTED_PARENTS[UNARY][1] and parent_review["reviewed_proof_sha256"]==EXPECTED_PARENT_BODIES["unary_cycle_proof"][1],"Parent review source/body linkage")
    require(parent_review["format"]=="gzip","Parent review encoding")
    compressed=parent_review["compressed"];decoded=parent_review["decompressed"]
    require((compressed["bytes"],compressed["sha256"])==EXPECTED_PARENT_REVIEW_COMPRESSED and (decoded["bytes"],decoded["sha256"])==EXPECTED_PARENT_REVIEW_DECODED,"Exact parent review identities")
    require(compressed["path"] in AUDIT_INPUT_PATHS and decoded["path"] in AUDIT_INPUT_PATHS,"Parent review input closure")
    raw_gzip=safe(compressed["path"]).read_bytes();raw_review=safe(decoded["path"]).read_bytes()
    identity(raw_gzip,compressed);identity(raw_review,decoded)
    require(gzip.decompress(raw_gzip)==raw_review,"Parent review exact gzip recovery")
    archive=read_json(PACKET+"/ARCHIVE_INDEX.json")["objects"]
    require(len({r["sha256"] for r in archive})==len(archive),"Recovery must be deduplicated by hash")
    for row in archive: identity(safe(row["path"]).read_bytes(),row)
    sources=read_json(PACKET+"/SOURCE_MANIFEST.json")["sources"]
    accepted={r["sha256"] for r in sources if r["role"]=="root_conditional_source_acceptance"}
    require(accepted==set(EXPECTED_ACCEPTANCES.values()),"Exact conditional Gibbs-source acceptance")
    for row in sources:
        r=row["recovery"]
        if r["kind"]=="blob": identity(safe(r["path"]).read_bytes(),row)
        elif r["kind"] in {"body_interval","external_body_interval"}:
            interval({**r,"bytes":row["bytes"],"sha256":row["sha256"]})
        else:
            require(r["kind"]=="external_pinned" and r["path"] in EXPECTED_PARENTS,"Unknown external input")
            identity(safe(r["path"]).read_bytes(),row)
    archive_map={r["path"]:(r["bytes"],r["sha256"]) for r in archive}
    blob_sources=[r for r in sources if r["recovery"]["kind"]=="blob"]
    require(set(archive_map)=={r["recovery"]["path"] for r in blob_sources},"Archive/source recovery coverage")
    require(all(archive_map[r["recovery"]["path"]]==(r["bytes"],r["sha256"]) for r in blob_sources),"Archive/source recovery identities")
    selection=read_json(PACKET+"/RECOVERY_SELECTION.json")["members"]
    require(len(archive)==47 and len(sources)==73 and len(selection)==63,"Exact current recovery index cardinalities")
    require(len({(r["freeze"],r["original"]) for r in selection})==len(selection),"Distinct selected frozen members")
    source_keys={(r["sha256"],r["bytes"],json.dumps(r["recovery"],sort_keys=True)) for r in sources}
    for member in selection:
        require(member["current_identity_verified"] is True,"Selected source identity status")
        if member.get("recovery") is not None:
            require((member["sha256"],member["bytes"],json.dumps(member["recovery"],sort_keys=True)) in source_keys,"Selected recovery linkage")
    state=read_json(PACKET+"/PUBLICATION_STATE.json")
    require(state["kind"]=="dated_source_proposal_not_actual_binding","Historical state role")
    for field in ["canonical_binding","git_base","primary_execution","cache_execution","mutation_execution","graph_execution","publication_action","retained_audit"]:
        require(state[field] is None,"Historical null state must remain null: "+field)
    require(state["scientific_programs_run"]==state["historical_programs_replayed"]==0 and state["future_base_supplied"] is False,"Historical execution and pending-base scope")
    require(state["source_acceptances"]==EXPECTED_ACCEPTANCES,"Historical actual source decisions")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding required; source draft is unbound")
    require(binding["root_read_complete"] is True,"Actual root inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES and binding["git_base"]==EXPECTED_GIT_BASE,"Actual source decisions and requested base")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_local_gibbs_controller_source_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
    require(canonical["bound_note_sha256"]==digest(note) and canonical["actual_git_base"]==binding["git_base"] and canonical["canonical_parent_sha256"]==binding["parent_sha256"],"Current binding identities")
    require(binding["raw_bodies"]==body_map["bodies"] and binding["canonical_parents"]==parents,"Actual body and parent structure")
    freeze=json.loads(bound_blob(binding["source_proposal_freeze"]))
    require(freeze["immutable_bodies"]==3 and freeze["mathematical_parents"]==1 and freeze["scientific_programs_run"]==0 and freeze["actual_binding"] is None,"Historical proposal seal scope")
    evidence=binding["root_review_evidence"]
    review_raw=bound_blob(evidence["review"]);review=json.loads(review_raw)
    require(review["kind"]=="root_source_publication_review" and review["root_read_complete"] is True,"Actual source-publication review schema")
    require(review["source_draft_freeze"]["sha256"]==binding["source_proposal_freeze"]["sha256"],"Reviewed proposal identity")
    require(review["decision"]=="Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.","Actual publication interpretation decision")
    require({r["name"]:r["sha256"] for r in review["body_pins"]}==EXPECTED_BODIES and review["parents"]==parents,"Root reviewed bodies and parent")
    require(review["parent_review_binding"]==parent_review,"Root reviewed exact parent review recovery")
    require({k:r["sha256"] for k,r in review["existing_source_acceptances"].items()}==EXPECTED_ACCEPTANCES,"Root reviewed source decisions")
    require(review["scientific_programs_run"]==review["primary_runs"]==review["historical_programs_replayed"]==0,"Root source-review execution scope")
    _,result=execution_evidence(evidence,True)
    require(result["review"]["sha256"]==digest(review_raw),"Actual review output linkage")
    receipt,observed=execution_evidence(binding["base_observation"],False)
    require(receipt["argv"]==["gh","pr","view",str(EXPECTED_BASE_PR),"--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual base observation command")
    require(observed["number"]==EXPECTED_BASE_PR and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]==EXPECTED_BASE_BRANCH and observed["baseRefName"]==EXPECTED_BASE_PARENT_BRANCH and observed["state"] in {"OPEN","MERGED"},"Actual base PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding["base_observation"].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(p in AUDIT_INPUT_PATHS for p in used),"Binding evidence literal closure")
    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and captured binding evidence only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: exact coefficient text retained; no physical element or gate executed")
    print("per_site: fixed path and supplied isolation are preserved; no hardware test executed")
    print("per_mode: full-sector analytic Gibbs spectrum retained; no mode simulation executed")
    print("per_block: three exact bodies, one parent and captured binding evidence checked")
    print("lattice_wide: source integrity only; cooling, runtime handoff and audit remain unexecuted")

if __name__=="__main__": main()

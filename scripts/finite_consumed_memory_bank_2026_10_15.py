"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/FINITE_CONSUMED_MEMORY_BANK_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-finite-memory-bank-20261015"
PARENT = "docs/CORRELATED_MEMORY_DELIVERY_AND_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md"
EXPECTED_PARENTS = {
    PARENT: (203198, "12bd18b0d2a1939639027ed51204a066744eab77d2b105a870f89bdb286b4d89", "correlated_memory_delivery_and_readiness_bounded_theorem_note_2026-10-15", "685db9bdbdefb04b855c28e0b45f03fae7401324b6f52589a25b2b25a045d9ea"),
}
EXPECTED_PARENT_REVIEW = "c001e42e06fe230e0e0d990f3664fef981d1d7e869b293beb1051fb04d4da3ef"
EXPECTED_ACCEPTANCES = {
    "finite_bank": "5bf680ccc41224a0446210d20cbc110ef5ebd63c426ed02de72612148a22e908",
}
# Root must replace this null in a separately reviewed bound version.
EXPECTED_GIT_BASE = '9369c12d0804f170f0016f5b26d7b12e057f0664'
MANIFEST_SHA256 = 'bc8d4a00e2bd5622532f06cd4a430c6907d4d1061773a2d682eb9a4607815432'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-finite-memory-bank-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/CHANGED_CODE_MAP.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/PROVENANCE_PLAN.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/REFS.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/SOURCE_DRAFT_FREEZE.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_failed_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_failed_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_failed_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/fetch_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/historical_recorder.py', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/inventory_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/inventory_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/inventory_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/live_recorder.py', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_fetch_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_fetch_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_fetch_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_inventory_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_inventory_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/prior_inventory_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/root_review_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/root_review_executed_source.py', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/root_review_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/root_review_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/stack_EXECUTION.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/stack_LAUNCH.json', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/stack_stderr', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/binding_sources/stack_stdout', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/build_proposal.py.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/inspect_proposal.py.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_ASSUMPTIONS_AND_IMPORTS.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_CLAIM_STATUS_CERTIFICATE.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_COUNTEREXAMPLES.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_HANDOFF.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_PROVENANCE_PLAN.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_PR_BODY.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_RECOVERY_SCOPE.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_REVIEW_HISTORY.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/packet_TRACE_GATE.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/primary_template.py.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/record_metadata.py.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/seal_packet.py.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/packaging_diffs/wrapper.md.diff', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/001e55f5cfeac36e4ca9dbf80a96938f05ac60a92c8e9575761d802c734ddf1e.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/098a5aa6be9160ee42f7e15b47dc0d6582221f04bffadd455c03006fa72259ef.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/0e2c4a627624deeb936e2b7f975a88135582e022211daf2c4ff86b2bea717510.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/10b075e8fb1cf76d2303cfc21960c5e5e9b26d3916343162eb5d7e03f319a2c7.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/1708bd8973c91c6efaa214778a4ccd09b9a35387b3d3bcebe8e10e5987cbbe29.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/193c9a0589488e13d5446149fda484861b981012d1bcba0cd155d0951f300a0b.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/2122bd0370928ad6fb8970af617cf76dc5f97d8557a5758008dc4335ea607827.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/21ab94d462060c28ad4eed645bf260b65e849a5238178d83152b840060b3a0ab.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/24117ab2b2f9dc5500b8915641dc330447b9d041baa6c136774a44ec965eb6e3.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/2e6cb71957cfa42040e5445184f081eb830709db2c10f23e747e9df0adb2eeb1.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/338a0a3199e8de397779aae38707ceb0077a2588d52c4d7ccce28e93e129ac95.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/34b4a66d6f77d590de86c9a18624fa2afdd861793c937ce4497950598ac99e7b.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/382cc76fcf42b9849bf9bea09acd942fae822f48c2351eb67a4fff7e2918652b.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/3add669ebcb29ab88b9049bd807a12d0732f4a6aecc0f38aabe5774850bfd02e.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/56c3a4c7a37c98178bbe6799b2c8bd0829d6ed541f501f0e27b402d67b223807.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/594691d17e1675047e27f9066725fba5568d56aede09bbe08c33be27505b772a.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/5bf680ccc41224a0446210d20cbc110ef5ebd63c426ed02de72612148a22e908.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/5eb3e36e3b9316982e9d19bfc1563a420ffdc7749ad33aa418658e7c78ca22e2.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/6729c8fe89f7c14b30ad818765db42314a401bab59fbb66de4c264ad0621b89b.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/67a7af8e049cacee2d69c0bab132fd4ecf40915a7acb73eb1b6498b8a1bf2a6f.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/79d10728c72fcf450086834a8587008a16725f463abe4b43556ffbf61e5d23ec.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/7a3b9dc1a67efb42a4acf579d51c5f81b5b2cd399ac247868df93387bab9d2f7.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/7d924a4c8b3ae428523616f801cf05ee10d372eced7b6939030f1eb5d5897aa4.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/7e85e05328c91e1b46b6959b8a709d1899901eac25e28b4e360623ceb95f48d4.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/88d8aae1bd0b07def238bdb5a1408f43a7bfe9ae7c46cf88952c45d9acf3c1f1.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/913fc4ce6f9d45d7b97c299de3a6af1522813752c2059a720e534d12356664dd.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/9c30e361c4537a152c469e4e8c95d535367718ec8ad3d4509a5ee9941dae0aa1.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/b8156831899212a51e6be24a262f593358d69da4bc1961c4a5c62dd42dab686d.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/bdeb8ecba472db14a87adf66e2d3ae6963a7b594a1fa14e26f0b496f58d2ac10.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/c0c872da3952ad48692803ef0e6f9919e34c76604ffb0f96f5af7d7245d944be.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/c812492b863ca373b61fcd928bbc7e69bc61da1bb80366b77df7949aa41d0305.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/c9ca1076761b2f7bf90d83b833429540bbc04896ba46839074ad0ffa0ea5ff85.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/ccf02591453159370f54aa69a32696f8541d3fb90ee5a414a97a34263c3343ae.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/cd8341414d4df65a10889af5e1dd0a281bfdc4cf54ab1dab8dd18eb9753513bf.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/ce05a70dea48ae35c1266fc92d5dcfe5964f55ea3da29cd522cec21335c8b767.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/dd10996065a41e9f116ebac93b135864443c823bc4210a74a3833901ac874ad5.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/e0a182f7db581c1fc6051bb1dcfa7e3fd54985a24bb35a0ecc0e19a44acc69f1.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/e351e996880c698c3715867a70b3b867308859ed3b6d6f3442e4db77c9cd2ddc.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/e66dc3d4d956acffc070076bca03e2bee3677550db809ed86e56594470044f0b.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/ea7242efaeb00ba35cc9aee3f155796fdf3b0f2345cdbf1f9f3cc4aba71c9f73.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/ee3c437b3752332de30d2ff49ae8a1774906663fbcb84bea873555dba767950d.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/f268ad7caad2db36a3274c7304c8ba97ce24d33afb49d4e9ad47b45a2848ec69.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/f5b9ef6e40c5596a9e851a0ce6a19bdc8856fa2a286394bbe2d4e723d75a97d4.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/f5def3706984cd0a22b403eec48483c05baa6eabfa355edfd0dba190afc2f45f.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/f860e77316e93fc0e9226d6f8a800e6bac9a916782f850384f64d2a9748ff5ce.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/fbdea87d13f978eb81d8f77f0cfd90678239b054bdfe967cc80a7c91a7ab43d0.blob', '.claude/science/physics-loops/toe-finite-memory-bank-20261015/source_recovery/feac515d67c7fdcf239c7867504dc22f19a96434154e046c999f564c88076f69.blob', 'docs/CORRELATED_MEMORY_DELIVERY_AND_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/FINITE_CONSUMED_MEMORY_BANK_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'bank_author': '162d7504ad3951ed29add0facefc0bbdb227fcdf582e22250baad04a4f63c521', 'bank_assessment': '16f6fbc729dd24fb77df435ecfe86b9545bf875ceec25067893a0ed853f811b6'}

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
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false",'upstream_dependencies: ["correlated_memory_delivery_and_readiness_bounded_theorem_note_2026-10-15"]',"runner: scripts/finite_consumed_memory_bank_2026_10_15.py"]:
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
    require(accepted==set(EXPECTED_ACCEPTANCES.values()),"Exact finite-bank source decision")
    for row in sources:
        r=row["recovery"]
        if r["kind"]=="blob": identity(safe(r["path"]).read_bytes(),row)
        elif r["kind"] in {"body_interval","external_body_interval"}:
            require(r["container"]==NOTE or r["container"] in EXPECTED_PARENTS,"Undeclared interval container")
            interval({**r,"bytes":row["bytes"],"sha256":row["sha256"]})
        else:
            require(r["kind"]=="external_pinned" and r["path"] in EXPECTED_PARENTS,"Unknown external input")
            identity(safe(r["path"]).read_bytes(),row)
    state=read_json(PACKET+"/PUBLICATION_STATE.json")
    require(state["kind"]=="dated_source_proposal_not_actual_binding","Historical state role")
    for field in ["canonical_binding","git_base","primary_execution","cache_execution","mutation_execution","graph_execution","publication_action","retained_audit"]:
        require(state[field] is None,"Historical null state must remain null: "+field)
    require(state["scientific_programs_run"]==0 and state["historical_programs_replayed"]==0,"Historical execution scope")
    require(state["source_decision"]==EXPECTED_ACCEPTANCES["finite_bank"],"Actual finite-bank source decision")
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
    canonical_binding = read_json(PACKET + '/CANONICAL_BINDING.json')
    require(canonical_binding['kind'] == 'actual_finite_bank_source_binding' and canonical_binding['canonical_parent_binding_complete'] is True and canonical_binding['root_read_complete'] is True, 'current finite-bank binding schema')
    require(canonical_binding['bound_note_sha256'] == digest(note) and canonical_binding['actual_checkout_head'] == canonical_binding['actual_git_base'] == binding['git_base'], 'current finite-bank binding identity')
    require(canonical_binding['canonical_parent_sha256'] == binding['parent_sha256'], 'current parent binding identity')
    require(binding['raw_bodies'] == body_map['bodies'] and binding['canonical_parents'] == parents, 'actual body and parent structure')
    selection = read_json(PACKET + '/RECOVERY_SELECTION.json')
    for selected in selection['members']:
        loc = selected.get('recovery')
        if isinstance(loc, dict) and loc.get('kind') == 'body_interval':
            require(loc['body_name'] in EXPECTED_BODIES and loc['container'] == NOTE and selected['sha256'] == EXPECTED_BODIES[loc['body_name']], 'selected recovery role')
            interval({**loc, 'bytes': selected['bytes'], 'sha256': selected['sha256']})
    require(binding['base_branch'] == canonical_binding['actual_branch_at_binding'] == 'physics-loop/toe-correlated-memory-delivery-20261015' and binding['planned_feature_branch'] == 'physics-loop/toe-finite-memory-bank-20261015', 'actual branch binding')
    require(binding['source_proposal_freeze']['sha256'] == 'da49c7c8d76ecd35ac6a02a8cfbb37a263df9f29d11bc5b7aa18369b0426274f' and binding['root_review_ack']['reviewed_source_sha256'] == binding['source_proposal_freeze']['sha256'], 'root reviewed source acknowledgment')
    require(binding['canonical_execution_not_yet_performed'] is True and binding['retained_audit'] is False, 'dated actual binding execution scope')
    prefix = PACKET + '/binding_sources/'
    expected_names = {'REFS.json', 'ROOT_SOURCE_REVIEW.json', 'SOURCE_DRAFT_FREEZE.json', 'historical_recorder.py', 'live_recorder.py', 'root_review_executed_source.py'}
    expected_names |= {label + '_' + name for label in ('fetch_failed', 'prior_fetch', 'prior_inventory', 'fetch', 'inventory', 'root_review') for name in ('EXECUTION.json', 'stdout', 'stderr')}
    expected_names |= {'stack_' + name for name in ('LAUNCH.json', 'EXECUTION.json', 'stdout', 'stderr')}
    require(len(binding['receipt_paths']) == len(expected_names) and set(binding['receipt_paths']) == {prefix + name for name in expected_names} and canonical_binding['receipt_paths'] == binding['receipt_paths'], 'exact binding receipt membership')
    freeze_raw = safe(prefix + 'SOURCE_DRAFT_FREEZE.json').read_bytes()
    identity(freeze_raw, binding['source_proposal_freeze'])
    freeze = json.loads(freeze_raw)
    require(freeze['immutable_bodies'] == 2 and freeze['mathematical_parents'] == 1 and freeze['actual_binding'] is None and freeze['primary_execution'] is None and freeze['scientific_programs_run'] == 0 and len(freeze['files']) == 180, 'historical bank proposal scope')
    root_raw = safe(prefix + 'ROOT_SOURCE_REVIEW.json').read_bytes()
    require(digest(root_raw) == binding['root_source_review']['sha256'] == '33c200eaf5fe0c0ad63bfccf2cb81e866cf05fc41e2588b1a810083074e8656d' and len(root_raw) == 8005, 'actual root review identity')
    root_review = json.loads(root_raw)
    require(root_review['kind'] == 'root_source_publication_review' and root_review['root_read_complete'] is True and root_review['source_draft_freeze']['sha256'] == binding['source_proposal_freeze']['sha256'], 'actual root review schema')
    require(root_review['sealed_members_verified'] == 180 and root_review['source_rows_verified'] == 63 and root_review['decision'] == 'Publication interpretation accepted at existing conditional source scope; actual checkout binding and integration remain pending.', 'actual root review decision')
    reused = root_review['scientific_source_reading_reused']
    require({'bank_author': reused['author'], 'bank_assessment': reused['review']} == EXPECTED_BODIES, 'actual root reviewed body identities')
    require({key: row['sha256'] for key, row in root_review['existing_source_acceptances'].items()} == EXPECTED_ACCEPTANCES and root_review['scientific_programs_run'] == root_review['historical_programs_replayed'] == 0, 'root source scope and acceptances')
    refresh_raw = safe(prefix + 'REFS.json').read_bytes()
    require(digest(refresh_raw) == '4efe5c41698ca84346baeb73bbf2f9f4b6761ee70f85995e85d1807602ff7c32', 'exact refresh identity')
    refresh = json.loads(refresh_raw)
    require(binding['origin_main'] == refresh['refs']['origin/main'] == 'bbada1fe09b2d10d610560864d86b68c24a59713' and binding['instruction_revision'] == refresh['refs']['origin/ai/execution'] == '3a4b2c66a1ead7a1c48b4359627e968f681e3c39' and refresh['refs']['HEAD'] == EXPECTED_GIT_BASE, 'actual refresh ref binding')
    inventory_raw = safe(prefix + 'inventory_stdout').read_bytes()
    identity(inventory_raw, refresh['inventory']);inventory = json.loads(inventory_raw)
    require(len(inventory) == 41, 'historical inventory schema')
    recorded_base = [row for row in inventory if row['number'] == 9611]
    require(len(recorded_base) == 1 and recorded_base[0]['headRefOid'] == binding['historical_base_pr_head'] == EXPECTED_GIT_BASE and recorded_base[0]['headRefName'] == binding['base_branch'] and recorded_base[0]['isDraft'] is False, 'historical base PR observation')
    history_source = safe(prefix + 'historical_recorder.py').read_bytes()
    live_source = safe(prefix + 'live_recorder.py').read_bytes()
    require(digest(history_source) == 'd125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95', 'historical recorder source identity')
    require(digest(live_source) == 'ca4afb56072401252f86358fb589055e109ccd0303aaf5ae5998e8577ce408c4', 'live recorder source identity')
    observed = binding['observed_parent_prs']['stack']
    require(set(binding['observed_parent_prs']) == {'stack'} and observed['number'] == 9611 and observed['state'] == 'OPEN' and observed['isDraft'] is False and observed['headRefOid'] == EXPECTED_GIT_BASE and observed['headRefName'] == 'physics-loop/toe-correlated-memory-delivery-20261015' and observed['baseRefName'] == 'physics-loop/toe-readiness-resources-20261015', 'observed parent PR binding')
    require(read_json(prefix + 'stack_stdout') == observed, 'observed parent PR stream')
    receipt = read_json(prefix + 'stack_EXECUTION.json')
    launch_raw = safe(prefix + 'stack_LAUNCH.json').read_bytes()
    require(receipt.get('exit_code') == 0 and isinstance(receipt.get('finished_utc'), str), 'live observation exit/schema')
    identity(launch_raw, receipt['launch']);launch = json.loads(launch_raw)
    require(launch['argv'] == ['gh', 'pr', 'view', '9611', '--repo', 'jonathonreilly/qubit-lattice-axiom-framework', '--json', 'number,state,isDraft,headRefOid,headRefName,baseRefName,url'] and launch['scientific_execution'] is False and launch['source_at_launch'] is None and launch['inputs_at_launch'] is None, 'live observation launch/schema')
    identity(live_source, launch['recorder'])
    for key in ('stdout', 'stderr'):identity(safe(prefix + 'stack_' + key).read_bytes(), receipt[key])
    require(safe(prefix + 'stack_stderr').read_bytes() == b'', 'live observation error stream')
    for label, expected_exit in (('fetch_failed', 128), ('prior_fetch', 0), ('prior_inventory', 0), ('fetch', 0), ('inventory', 0), ('root_review', 0)):
        receipt_raw = safe(prefix + label + '_EXECUTION.json').read_bytes();receipt = json.loads(receipt_raw)
        require(receipt.get('exit_code') == expected_exit and isinstance(receipt.get('start_utc'), str) and isinstance(receipt.get('end_utc'), str) and isinstance(receipt.get('argv'), list), 'historical observation schema')
        identity(history_source, receipt['recorder'])
        for key in ('stdout', 'stderr'):identity(safe(prefix + label + '_' + key).read_bytes(), receipt[key])
        if label in ('fetch_failed', 'prior_fetch', 'prior_inventory'):
            source_index = {'fetch_failed': 0, 'prior_fetch': 1, 'prior_inventory': 2}[label]
            identity(receipt_raw, refresh['actual_receipts'][source_index])
            require(receipt['child_source_at_launch'] is None, 'prior observation has no Python source file')
            if label == 'fetch_failed':require(receipt['argv'] == ['git', 'fetch', 'origin', 'main'], 'actual failed fetch command')
            elif label == 'prior_fetch':require(receipt['argv'] == ['git', '-C', '/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree', 'fetch', 'origin', 'main'], 'actual corrected fetch command')
            else:require(receipt['argv'][:4] == ['gh', 'pr', 'list', '--repo'], 'prior inventory command')
        elif label == 'fetch':
            expected_code = 'import subprocess; subprocess.run(["git","-C","/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/correlation_worktree","fetch","origin","main"],check=True)'
            require(receipt['argv'] == ['python3', '-c', expected_code] and receipt['child_source_at_launch'] is None, 'actual wrapped fetch command without source file')
            require(Path(refresh['actual_fetch_receipt']).parent.name == 'main_refresh_1800', 'current fetch receipt source')
        elif label == 'inventory':
            require(receipt['argv'] == ['gh', 'pr', 'list', '--repo', 'jonathonreilly/qubit-lattice-axiom-framework', '--state', 'open', '--limit', '200', '--json', 'number,title,headRefName,baseRefName,headRefOid,isDraft,url'] and receipt['child_source_at_launch'] is None, 'actual inventory command/source')
            require(Path(refresh['actual_inventory_receipt']).parent.name == 'open_inventory_1800', 'current inventory receipt source')
        else:
            executed = safe(prefix + 'root_review_executed_source.py').read_bytes();identity(executed, receipt['child_source_at_launch'])
            require(digest(executed) == '260e170963b63b95644c21c6383599c374f08436feba2196e46dfe6296d116fa' and Path(receipt['argv'][1]).name == 'review_bank_publication_1800.py', 'root review executed source')
            result = read_json(prefix + 'root_review_stdout')
            require(result['review']['sha256'] == digest(root_raw) and result['verified_members'] == 180 and result['verified_sources'] == 63 and result['scientific_programs_run'] == 0, 'root review output binding')

    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and binding only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: literal source coefficients are preserved; no physical gate executed")
    print("per_site: fixed old sites and finite bank geometry remain conditional source statements")
    print("per_mode: one-global-error and ideal-unused-bank scopes are preserved as text")
    print("per_block: two immutable bodies, one parent and actual source binding checked")
    print("lattice_wide: no native memory, restoration, autonomous program or audit certified")

if __name__=="__main__": main()

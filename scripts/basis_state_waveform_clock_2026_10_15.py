"""Source-integrity primary only: no scientific program, simulation or proof test."""
from pathlib import Path, PurePosixPath
import hashlib
import json

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-basis-state-clock-20261015"
PARENT = 'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md'
EXPECTED_PARENTS = {'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md': (136036, '9b08b7a78f21390d065322150d1fe6a222343323cc76dfe7f3b065a624d5a18e', 'single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15')}
EXPECTED_ACCEPTANCES = {"basis_clock":'174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0'}
EXPECTED_GIT_BASE = 'ce8e1842601b067f11141441aa73b1ccfd14476e'
EXPECTED_BASE_PR = 9618
EXPECTED_BASE_BRANCH = 'physics-loop/toe-local-gibbs-controller-source-20261015'
EXPECTED_BASE_PARENT_BRANCH = 'physics-loop/toe-single-port-program-and-controller-20261015'
MANIFEST_SHA256 = '8dc2970c38934bcb9c900568eb3114ca34019c3662fd1ac9c94a99113e8ca58c'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-basis-state-clock-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/ACTUAL_REFRESH_PROVENANCE.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/BINDING_CONTRACT.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/COUNTEREXAMPLES.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-basis-state-clock-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/RECOVERY_SELECTION.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/20ebf2a5171efc8b24dd7731af9969edda6c36defd076fe186a17fc59bd713bf.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/375aad4f021790bb4935f6ea5471d4ca96c20dfd85039a143c0c7ed385d1ca40.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/43e0aba645e3f15844096135323b074de03e5da217ea158c2526ca4897e15706.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/44b047f949494c18c3be903863dbc1d086d26c43e931ce927aeb08032e572f01.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/45b2c8dae126a8082667fa9899e994847ff86b4172039dc20ed5730bc645448b.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/48302bf348db0cf8aa46dac36e7155e322e6c4cc00c04137ea94f5af704aa266.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/5cb68783eb92da96600182e712ccd4529780c215f090807b4bb42dd43b8edd80.py', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/62e87a98350226701e84907a2d4eb2139fc82da073747af35d4660752fc67821.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/794f22d534ce6989712f085db1dc78928e2fdded1b6bb5a3559ebac049220f08.py', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/7d1c904ccad39714560697845ea919beb3266ff09c0b62aaa76777380920ad67.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/7ee919bfe0e3c1c318d51d7e38c2363e7eb53daee2815800a9223cc48820a8da.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/c4cf329ed0296e683768ea4713149bf684d38dbbfb2176b0a7dc41c34cd37617.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/c5d453f67f3723cfdb729a898a33dc8c717b59cec20a8663d795611db275ef24.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/c904492d9b5ae01038b1b545014a043912c1109ddc387694e24e7c3af7e73e0b.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.py', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/eb31fa43c503cfc659e3e5d18c7eafe3ed2927ee3efb45810c5ab4371a8d2708.json', '.claude/science/physics-loops/toe-basis-state-clock-20261015/binding_sources/f2fac13228af7cce764dd69e4f1f1ca3e165cfc2acca26a4f57965bc73aefb1d.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/0401494d66409ef11862bb304c0b20679a08fb97283e942bf76a0fcdd3127c82.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/05f3ec8e58ccd7a4d2a87643fb7ed4f12998c6a1d5721e3632a502de8a0ad6ce.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/0df4c2fd20f3241765c0ab06c4ef6b88b21095f766e0a4a8dc6822a217c502d8.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/10c6e80c36ce5e4691c045ed2045aba6f78c75e8d5ef7f404e4479a6ea87b95f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/150f26829933c8e50b4e478a3a73f03643d58a9c557f8b0108c4e160965abc09.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/174ff7dccd2e3e5b4afc631c8a551a893944c4891122a943d15dd154ef9e28e0.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/195ca29023402c8e86457d96e244eaa80305c68ac83f52ff89ce2a63030251b3.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/1dc70fe970de23533ad5604d4cb85d94ddf3e9dcbd4ca3368aba04fe464e16e5.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/2166582528c535897147977b8af3e242a804f22f26807207555a7cf2165bb31a.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/255f34b704d680b169f3fb08e4d9c3e890755161b316b8ed776e96c8c6840909.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/2a61c069caae5e7d3a4a63d2f7595eb92e9e54a2bffcc054f7cee3a586df1a87.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/2f7b36b683ef29e99b4c3e336ba292bd54ac7dbe83afea4dd1e6016919714c45.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/3076dae4499b300e0a43d5e5c47f38aea651df25e6a00c29a767f31479bf2b8f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/32f1392f32f798df3e4eb1db4a096b558de45c465295b27c3977c0faa5a1f81f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/3950bad051f9e678a70c47e8b5a9975d6cdd64f70918bef8427a4b504008cf45.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/3aabd0f8b80c31a0a607033b568493da5618468ab03974cf21be88928fb04c66.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/3d123055d2dc54a288bea3fcf1d694fa8a56e0f969f4c48246e90f650440ed4b.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/45cbce286c254e934d0b24e0ad39d8b949d7342426aca3d78f1fbfbfd6ee2451.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/48ade9aa8c72d772285081c78e09e9db5024df6ed21c87a35db292a81b917eac.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/51f2979535cd494acf2553f7f6ac0a464b2a9841552e16535f5a00ca48e67a4d.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/57e7952202ef634c4c6da7841166177c1950dc2c9c81236499f4f6f8e1977922.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/58511cc9b6f2ba50d6ac5bf347a13160c46f9adae73f6b1fbfacbc05f0e86eb6.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/5e81e709bc47249ee678ec7296b7b5d0b2a5ca32197503c19b7f1448f7b36149.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/6ba5444b903db131cad9e44e1f4865f4e9998f15e39e19004495a707dbfcfd47.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/6e678e807ac242b7caeeaf0ec4e40df801b482180a4bc6d5cfe8418c351df8f3.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/75f6082dd4b7c31737a3fe426a714647f83299be418c7f339729de6b3b74158e.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/7bd23b4adb3c76300c7b3b33720ead918241e5ea4bbca7f253b84320e0c9e276.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/838c0e8b40d8503b099b34085041f0a620ba1639d6ebca25e44f0e265857f098.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/9630198de15c5854a191f3b6d03a9675e771f0eadb6dcf7ae25a7a05571e0eab.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/a1bf65adc47df4d744be70319fbd828471666b747fe8a8b8a92b68954007791c.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/a24ea21b2c89a80554f09ca0038ef4ed61461ecca51e4a088dad6df4ce30fbea.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/a78da11dd125bdf7c2ec3754632b4ab78ad7d40c97e55296d3ef018216f5a10d.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/b2f0b33b7610bd3a33753dd4c2e1820b27cbffb6db287c8b8dcc9fe396e0286f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/bd840f812e2e89d9b3c0fdaa63a5c9f6616fef2e9734a7f421b9943a92a769e6.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/c42d4bcbe640fadad751d07aa53691eae40ec3d73ad852caddd7b8b7e6c58369.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/c462e0e6c225a2e28d96423c7959f572f6da902bb6e35298f5893570023697bb.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/c707dc710885a6c2b988454a98667abc9a0e0c364fe2dbcf6832489cff464e4a.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/ca2f2325ba990d868adef13bf2cea72d96b1a4b99bd07e84c32fa057a2c922f9.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/d236aa3e37c9efddc01ec30cce13ba7c2323d439c86fdde1d81445bfe00b05a1.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/d414aea900d8bdc722aca9db3c6975319228a356c87f410108ffb838c6eef30b.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/dbdd8110b702f59c0b48622d7226da3c6f3690e7dc77e988a1fafed055126750.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e045efb5a14cfe89095a62a1335d72cd91d6f6c9b602eb721d9af3de5c86e4db.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e2a7cfe5890fe5cc14c732c079b18c3d337ec43319a2bf10084a5461d92b0be8.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e3506bd12cf173c346b9d56efe3a2471ebe54ea8307857b5869a176b4d8ef135.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e58d83eedfa33c523ed7163f1441f3ad8083ed54c034b25fb8f10dce05cd24c6.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e6941af17176ce0243a2cf8bb03d4e1118841a42eac5c9d1e14e348889e3e7d6.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/e77e7efe17a30c4444b0de48a0d88d2bc6711d34549e7106153208a2da58566d.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/eac8b5827535edc484f7bffec2f1a4dde50dd565cfa489e8311bba8b74bbb30f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/ecaae2e348189870897deab31463076f4a57d53adf700088938dd744b0f56d7f.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/f1b04a745d3c321e555a98f77477cc43d6d87c9a89da153dd5870c78ebe99c3e.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/f1b13f52eaf575e781117694424c7542d507f4d32d6fb62e18ba598c3ba2f99c.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/f21a22336bab887f898ca2e14c4bd7c58b81f463a739e910cf6755c648d6eca2.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/f34115e73bcbdba7df8aa43693adc3baa741cf8754c07810430f9b4bfa2c006a.blob', '.claude/science/physics-loops/toe-basis-state-clock-20261015/source_recovery/f9a7b41213cee9ff0b7e9a28f79b555c152de52ef012ff3bcdd09b996d3aa32f.blob', 'docs/BASIS_STATE_WAVEFORM_CLOCK_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'root_author': '0fc2b7046b24c535ebd9549449601c42d8af6e3a9f95ca3e5a45a16eabb5eb46', 'independent_author': '84f03ca0de42477399e9a797f659b971e6beb88505d59fce6aaca5c6147acf39', 'comparison': '8c3ba783afdfa526e9da08df73760d8b6f0477c2598002b4c71fc042e480a2c2'}
EXPECTED_PARENT_BODIES = {'controller_author': (24070, '0e91f9369e387608f8fb3720c290e67f6aa98b10f13428866334c8507b9e989d')}
EXPECTED_PARENT_REVIEWS = {'controller_assessment': (32692, '52eb2e2dcd9fc56a7be490e193b57754bd85bfad5d585244d4a9fce947b4465d')}

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
    for field in ["canonical_parent_binding_complete: true","claim_type: bounded_theorem","actual_current_surface_status: conditional-support","trace_class: upstream_support","audit_required_before_effective_retained: true","bare_retained_allowed: false","runner: scripts/basis_state_waveform_clock_2026_10_15.py",'upstream_dependencies: ["single_port_program_and_autonomous_controller_bounded_theorem_note_2026-10-15"]']:
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
    require(parent["required_mathematical_body_names"]==["controller_author"],"Only the full-sector mediator proof imported")
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
    require(state["scientific_programs_run"]==state["historical_programs_replayed"]==0 and state["polynomial_mediator_imported"] is False,"Execution and excluded-claim scope")
    require(state["source_acceptances"]==EXPECTED_ACCEPTANCES,"Historical actual source decisions")
    require(isinstance(EXPECTED_GIT_BASE,str) and len(EXPECTED_GIT_BASE)==40 and isinstance(EXPECTED_BASE_PR,int) and isinstance(EXPECTED_BASE_BRANCH,str),"Root must explicitly pin the actual Git base; source proposal has no chosen base")
    binding=read_json(actual)
    require(binding["kind"]=="actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True,"Actual binding required")
    require(binding["root_read_complete"] is True,"Actual root publication inspection required")
    require(binding["note_sha256"]==digest(note),"Bound canonical note identity")
    require(binding["parent_sha256"]=={k:v[1] for k,v in EXPECTED_PARENTS.items()},"Actual parent pin")
    require(binding["source_acceptances"]==EXPECTED_ACCEPTANCES and binding["git_base"]==EXPECTED_GIT_BASE,"Actual source decisions and base")
    canonical=read_json(PACKET+"/CANONICAL_BINDING.json")
    require(canonical["kind"]=="actual_basis_state_clock_binding" and canonical["canonical_parent_binding_complete"] is True,"Current actual binding schema")
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
    require(result["members"]==204 and result["sources"]==78 and result["exact_functions"]==19,"Actual reviewed source counts")
    review_seal_raw=bound_blob(evidence["review_freeze"]);identity(review_seal_raw,result["freeze"])
    review_seal=json.loads(review_seal_raw);require(len(review_seal["files"])==1,"Actual review seal membership")
    identity(review_raw,review_seal["files"][0])
    require(binding["polynomial_mediator_imported"] is False,"No excluded mathematics through Git ancestry")
    receipt,observed=execution_evidence(binding["base_observation"],False)
    require(receipt["argv"]==["gh","pr","view",str(EXPECTED_BASE_PR),"--repo","jonathonreilly/qubit-lattice-axiom-framework","--json","number,state,isDraft,headRefOid,headRefName,baseRefName,url"],"Actual base observation command")
    require(observed["number"]==EXPECTED_BASE_PR and observed["isDraft"] is False and observed["headRefOid"]==EXPECTED_GIT_BASE and observed["headRefName"]==EXPECTED_BASE_BRANCH and observed["baseRefName"]==EXPECTED_BASE_PARENT_BRANCH and observed["state"] in {"OPEN","MERGED"},"Actual base PR identity")
    used={binding["source_proposal_freeze"]["path"]}|{r["path"] for r in evidence.values()}|{r["path"] for r in binding["base_observation"].values()}
    require(len(binding["receipt_paths"])==len(used) and set(binding["receipt_paths"])==used,"Exact binding evidence membership")
    require(all(path in AUDIT_INPUT_PATHS for path in used),"Binding evidence literal closure")
    print(json.dumps({"result":"source_integrity_verified","scope":"exact bytes, recovery and captured binding evidence only; no mathematical validation by execution","scientific_programs_run":0,"historical_programs_replayed":0,"publication_or_retained_status_certified":False},sort_keys=True))
    print("per_element: basis-clock coefficients and scalar ledgers preserved; no gate or physical element run")
    print("per_site: weighted clock and exterior NN supports preserved; installation and isolation remain supplied")
    print("per_mode: one-head clock and full auxiliary-sector distinctions preserved; no simulation run")
    print("per_block: three unchanged bodies, one mathematical parent and separate canonical review checked")
    print("lattice_wide: no native initialization, Markov or polynomial-mediator import, common-cap, detector, reuse or retained audit certified")

if __name__=="__main__": main()

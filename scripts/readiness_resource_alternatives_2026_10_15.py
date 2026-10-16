"""Source-integrity proposal only. Never imports or executes scientific helpers."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re

REPO = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
NOTE = "docs/READINESS_RESOURCE_ALTERNATIVES_BOUNDED_THEOREM_NOTE_2026-10-15.md"
PACKET = ".claude/science/physics-loops/toe-readiness-resources-20261015"
MASS = "docs/MASS_SCALED_MEDIATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-10-15.md"
JOINT = "docs/ROUTED_AUXILIARY_AND_JOINT_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md"
MASS_SHA256 = "48a53fe28aa64d0f6bc13560e17f2e41ad97b5ff87a135c7f63ea44c175db7dc"
JOINT_SHA256 = "00c2097abfb8ef1bc9fe1eb5e8f126c0fcbf897e132b74a25a879c14a6e60b4e"
JOINT_BYTES = 152470
EXPECTED_GIT_BASE = "b3a884425aa86e642172aef67c90fc1fe93ff942"
MANIFEST_SHA256 = '6129579634015cf03aa2c758a287733fc86a3ac506cd77449fe15a77eaae9c1f'
AUDIT_INPUT_PATHS = ('.claude/science/physics-loops/toe-readiness-resources-20261015/ACTUAL_BINDING.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/ACTUAL_HANDOFF.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/ARCHIVE_INDEX.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/ARTIFACT_PLAN.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/ASSUMPTIONS_AND_IMPORTS.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/BODY_MAP.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/CANONICAL_BINDING.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/CLAIM_STATUS_CERTIFICATE.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/DEPENDENCIES.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/EXPOSURE_AND_LIMITS.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/FAILURES_AND_LIMITS.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/GOAL.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/HANDOFF.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/INPUT_MANIFEST.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/PR_BODY.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/PR_TITLE.txt', '.claude/science/physics-loops/toe-readiness-resources-20261015/PUBLICATION_STATE.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/RECOVERY_SCOPE.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/REVIEW_HISTORY.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/SOURCE_MANIFEST.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/TRACE_GATE.md', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/REFS.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/ROOT_SOURCE_REVIEW.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/fetch_EXECUTION.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/fetch_stderr', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/fetch_stdout', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/historical_recorder.py', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/inventory_EXECUTION.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/inventory_stderr', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/inventory_stdout', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/live_recorder.py', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/mass_EXECUTION.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/mass_LAUNCH.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/mass_stderr', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/mass_stdout', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/root_review_EXECUTION.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/root_review_executed_source.py', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/root_review_stderr', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/root_review_stdout', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/stack_EXECUTION.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/stack_LAUNCH.json', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/stack_stderr', '.claude/science/physics-loops/toe-readiness-resources-20261015/binding_sources/stack_stdout', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/013e3e5115fcd223b9efda51b9f062b6371ee1578c5155604ccd0777702fc6f3.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/034007227658952584c7069e60a0db6b8290802876128b0e6c6328bd251795da.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/070ecbfde3e9ba0c1c7a90b1f872ba3dcd6fd621cf4b4be86e8c49f852cddcaf.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/0a7494f55c9ef355be6ec7806bc9e02e449d83d4bc20419e703352ed25e8bfa7.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/16c557054f500abbb3e4bdd22782267daa1e9dcfc0672990eca4f2070767e03b.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/1a0349e7a976252bcf866a01571962690676ab9f828c953785b340241c37cf71.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/1b09b3a11c1919614063d2979ef33c4bec44968b429f2036c394ef98b88ee1d1.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/1ba2c6040a15e79611cd775d298335109caa22f5fe0fc8ddf996abff14f521aa.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/203a0d9b789282e8b5c27c9dd439fe81e54de47d567a638894122cd3ca6020a5.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/261573ae1bde8d722e29cf74579dd74970960be7eae2d37913925af0218629ed.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/3adf7494c03a9d6a889d36d6e2fa9482cfba801b79f14af6c9fe66402480f312.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/423f442cbae80345b4a70ee24166b361668b1d6ef280d67d31620be41792941b.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/42ff097cd1c0d6d3800947ee6775f0ca77321a144029fd6d1a540c8b9cb0f55e.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/44d0bea91fc53f3d0b8bcf63db103f29c852e6cc816529de1044663db8d6b97d.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/4609012fafc12081d117c1418e394ece87da51d19b093f510e61c8993d0fe1f3.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/465e95c3312a2e993888ed66b7a5b8f16abb391885d52687e4456df127d3955c.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/494b678af6ca0c046fd93e087225b8413b16de928396be8038d1ec0b41bc19e3.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/4a131447cca1228aee107d55b628a8d8950f27cd1ec8c29cb9d9a06328d7f953.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/518163fca6072886e7c03b6d32a23e8f5003f8ffc38fa405db37e7ed4f22af5f.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/57fa0e29c2b1f233177043c251e3c610d6ea90237ac8ef7df63d20a2b2b5beb9.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/5871330e1923f70f7872f02f14e0d7e70dd9c3ab27b461e55b0dcd74c0165492.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/5b619320da6eb3cc011166b3b546d49adf2bab6057f8af9f1ffb842bf77e7928.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/5fbe463ae7fb7fe62b143ae037c42a37e31448966e6153fca96f656dd596de13.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/645890cd14ca945ddfeb77e1c5da5dff7876cb0f547bd057e0b9c0c2f720fd39.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/6d1f573d67167203275eeab83980a4c9c911a32d989f6d152e9dfa2757fe7561.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/6ec9e0dcd30a75b143d885f3e8afed0e548ef87770e2071a6d52070631f5c62f.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/6f97d4d7dcdebc0ee9e2ed6246b1e9089f71db2d9752a08fe26ddd868fd80968.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/73a10a94f237f18a9a7c5ec6c1eac2285975ade03fc831beeb53a3fc036ba478.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/742f78db80a42131d647b9d1e2a7d2550079c7c73123fc8d75df3685d60cd7bf.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/75c34a4b9c7ba3127bdada73ed88ccd0baf87ffd7a194878541d7e455013496e.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/7ba2fceab45352d0032731a56124463ee14b70f12dcd4ba1dd0245e2db57fd40.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/7e492ac7ea2538725418f1c7435c95ef567b101e1537dcb2fefc40f18f65809a.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/80052c7a3a4d604e38337dc293677b1b7e4511b7fb2cdb1607b0063470f450de.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/8eaeec3dfa257f5e6ff61c46e9c6441fd9e66eff9408ea27c0ae5977c3d239fa.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/918924baf9a69adbb18df7bdee69dd939d0df047f133bbdd3ad76f9393ce8fb0.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/99f418f191eb26bb1cc9bd2b63a32457f0a6b5b07964b30997b812b91016374e.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/9f45fd2a9ef8853e7cb1f416bc7a13a1c415e48402a751b48877a4eee774eec1.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/a11a3e726ad4c97465c345be1b735a3934dd022e7afe4f1a211698693d58f43e.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/a25eb0d72aeb878a93d2031f4343b1d932a817828cc90c59c47ab3ab593b701e.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/a30f5e4d99cf1305956d95ed194a4623b3cd714c466d3abe599ff0edf353cbc3.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/ad6514a827688342447cc2b2394a47643dac5d20cd680b1e23ab289692e24354.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/b2cd2a764dbf9e6acbd3f8bf16e29b8af7420d587f525a3e9834a472f94fc798.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/b34df6b7479df5b3960b02bf383ff7954621a10b1efb6831a25c65466d8da783.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/bbb19a370b49b354e51917c46b9e241ce3bbb41ec8c1e39f8964b7e1222310b4.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/be6ddff8fe2d92f86053226b52d68daf72ca84fdac60aa22e23f61a3f7f352e9.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/c18688a6bee7761515624068ebe6698f7ab51309759678fd0093f00ea9903e3d.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/c62cc3e50511d8b9950a01f84ec1c410563c6e2271974030f60796d1d92162b7.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/cbfbd781a016865893c3eaf7ef23e8d20daadca8b6ce2806311c149bca2dac04.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/cf51b4d69ae0bf2a6219b24b4dbc91c787c6be87be1865d40b6fe0244937b890.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/d125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/d17af944333edfb7d8871f41c59d90c57e5e801b6c229e1dd94ec9e1dd625404.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/d547b02deca6a116c7787b14205248e055275f51da26079e46003a65adc14a8c.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/d80e631c52a28cde90a339161b225197eb6f3536bc368b18d4ae5f2ef761e0d7.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/dcee9d6fbbe2e5a29a45a0ad6066c7038426398ececce8cefda7f08a7aa73179.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/e4522c4f900b0666673d4c3d3f71b540c9339e48de1bf8047dbd0e1b05d0a7f4.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/e997298db7a6c485dbdf5b08eae65a423ab9bba410824d9c14101bada1ec0ed6.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/f557cd388260dc5c8979ac62197329cd365ec2f5cf568fdadb83a0cb867542b9.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/f66b558e24c9434b6c44dde36a1b9cc5d33ce6eb929cbe54b549077727ce2e9d.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/f7c259a629623b5b1f54985f2a697b25308ad072f2c000ba88cb02d905af0aaa.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/fb52a955202d14002c723ac727b2cf94f3534cdd18231da8708c9110583cfeca.blob', '.claude/science/physics-loops/toe-readiness-resources-20261015/source_recovery/ff8cf33e30c43fed1b976a22b985189110fb9ac3524cd0e8359b50e56e1497ea.blob', 'docs/MASS_SCALED_MEDIATOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/READINESS_RESOURCE_ALTERNATIVES_BOUNDED_THEOREM_NOTE_2026-10-15.md', 'docs/ROUTED_AUXILIARY_AND_JOINT_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md')
EXPECTED_BODIES = {'fixed_duration_corrected_proof': 'b083c9d942d589ef927c868fc89720bd16e91051f0e29b20ef6404d85eb8d5a2', 'fixed_duration_original_review': 'aab0856d58f58dca9ec51afd1b792c2eb792d37f8666491d4ac2bc2fb065d512', 'fixed_duration_correction_review': '0cb131b154a9386e39e890f087eba404ecc01807e272c2433c0502598e2aef3a', 'fast_proof': 'a0457a19542db757d4789c7b8ba1a7320deb9c07a10e337e82b93e23e3620794', 'fast_full_review': 'f8e85619d0f6825090d85a462c45be2bdf3b140d7b788e0ce0091a09963d8569'}
EXPECTED_ACCEPTANCES = {
    "fixed_duration": "013e3e5115fcd223b9efda51b9f062b6371ee1578c5155604ccd0777702fc6f3",
    "fast": "494b678af6ca0c046fd93e087225b8413b16de928396be8038d1ec0b41bc19e3",
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def safe(path):
    relative = PurePosixPath(path)
    require(not relative.is_absolute() and ".." not in relative.parts, "Unsafe input path")
    resolved = (REPO / path).resolve()
    resolved.relative_to(REPO.resolve())
    return resolved

def read_json(path):
    return json.loads(safe(path).read_bytes())

def check_identity(data, row):
    require(len(data) == row["bytes"] and digest(data) == row["sha256"], "Input identity mismatch")

def interval(container, row):
    start, end = row["start_byte_inclusive"], row["end_byte_exclusive"]
    require(isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(container), "Body offsets")
    raw = container[start:end]
    check_identity(raw, row)
    require(container.count(raw) == 1, "Body must occur exactly once")
    return raw

def main():
    require(isinstance(JOINT_SHA256, str) and re.fullmatch(r"[0-9a-f]{64}", JOINT_SHA256),
            "Exact joint canonical identity required")
    require(isinstance(JOINT_BYTES, int) and JOINT_BYTES > 0, "Joint canonical size must be actually bound")
    manifest_path = PACKET + "/INPUT_MANIFEST.json"
    manifest_raw = safe(manifest_path).read_bytes()
    require(digest(manifest_raw) == MANIFEST_SHA256, "Input-manifest identity")
    manifest = json.loads(manifest_raw)
    require(manifest["schema"] == "source_integrity_inputs_v1", "Manifest schema")
    rows = manifest["inputs"]
    require(len({row["path"] for row in rows}) == len(rows), "Duplicate input path")
    actual_path = PACKET + "/ACTUAL_BINDING.json"
    expected_paths = {row["path"] for row in rows} | {manifest_path, MASS, JOINT, actual_path}
    require(set(AUDIT_INPUT_PATHS) == expected_paths, "Literal declared-input closure")
    for row in rows:
        check_identity(safe(row["path"]).read_bytes(), row)
    note = safe(NOTE).read_bytes()
    header = note.split(b"---", 2)[1].decode().splitlines()
    for line in ("canonical_parent_binding_complete: true", "claim_type: bounded_theorem",
                 "actual_current_surface_status: conditional-support", "trace_class: upstream_support",
                 "audit_required_before_effective_retained: true", "bare_retained_allowed: false",
                 'upstream_dependencies: ["mass_scaled_mediator_transport_bounded_theorem_note_2026-10-15", "routed_auxiliary_and_joint_readiness_bounded_theorem_note_2026-10-15"]'):
        require(line in header, "Missing current binding/scope field: " + line)
    body_map = read_json(PACKET + "/BODY_MAP.json")
    require(body_map["note"] == NOTE and len(body_map["bodies"]) == 5, "Five exact bodies required")
    require({row["name"] for row in body_map["bodies"]} == set(EXPECTED_BODIES), "Body roles")
    for row in body_map["bodies"]:
        require(row["container"] == NOTE and row["sha256"] == EXPECTED_BODIES[row["name"]], "Immutable body pin")
        interval(note, row)
    dependencies = read_json(PACKET + "/DEPENDENCIES.json")["dependencies"]
    require(len(dependencies) == 2 and {row["path"] for row in dependencies} == {MASS, JOINT}, "Exactly two mathematical parents")
    expected = {
        MASS: (45751, MASS_SHA256, "mass_scaled_mediator_transport_bounded_theorem_note_2026-10-15", "785e56e3f8e667750b1f54da8963274096ac3ddac9fb8c56db3d6460846773e7"),
        JOINT: (JOINT_BYTES, JOINT_SHA256, "routed_auxiliary_and_joint_readiness_bounded_theorem_note_2026-10-15", "dcee9d6fbbe2e5a29a45a0ad6066c7038426398ececce8cefda7f08a7aa73179"),
    }
    for row in dependencies:
        size, sha, claim, raw_sha = expected[row["path"]]
        require((row["bytes"], row["sha256"], row["claim_id"], row["accepted_raw_source_sha256"]) == (size, sha, claim, raw_sha), "Canonical parent role/pin")
        parent = safe(row["path"]).read_bytes()
        check_identity(parent, row)
        parent_body = row["accepted_body_interval"]
        require(parent_body["sha256"] == raw_sha and parent_body["container"] == row["path"], "Parent proof role")
        interval(parent, parent_body)
    archive = read_json(PACKET + "/ARCHIVE_INDEX.json")
    require(len({row["sha256"] for row in archive["objects"]}) == len(archive["objects"]), "Recovery must be SHA-deduplicated")
    for row in archive["objects"]:
        check_identity(safe(row["path"]).read_bytes(), row)
    sources = read_json(PACKET + "/SOURCE_MANIFEST.json")["sources"]
    require({row["sha256"] for row in sources if row["role"] == "resource_root_acceptance"} == set(EXPECTED_ACCEPTANCES.values()), "Exact source acceptances")
    for row in sources:
        recovery = row["recovery"]
        if recovery["kind"] == "blob":
            check_identity(safe(recovery["path"]).read_bytes(), row)
        elif recovery["kind"] == "body_interval":
            require(recovery["body_name"] in EXPECTED_BODIES and row["sha256"] == EXPECTED_BODIES[recovery["body_name"]], "Source/body correspondence")
        else:
            require(recovery["kind"] == "external_pinned", "Unknown recovery kind")
    state = read_json(PACKET + "/PUBLICATION_STATE.json")
    require(state["kind"] == "dated_source_proposal_not_actual_binding", "Historical state role")
    for field in ("canonical_binding", "git_base", "primary_execution", "cache_execution", "mutation_execution", "graph_execution", "publication_action", "retained_audit"):
        require(state[field] is None, "Historical null outcome must remain null: " + field)
    require(state["scientific_programs_run"] == 0 and state["historical_programs_replayed"] == 0, "Historical execution scope")
    binding = read_json(actual_path)
    require(binding["kind"] == "actual_root_canonical_binding" and binding["canonical_parent_binding_complete"] is True, "Actual binding required")
    require(binding["root_read_complete"] is True, "Actual root inspection required")
    require(binding["note_sha256"] == digest(note), "Actual bound-note identity")
    require(binding["parent_sha256"] == {MASS: MASS_SHA256, JOINT: JOINT_SHA256}, "Actual parent identities")
    require(binding["source_acceptances"] == EXPECTED_ACCEPTANCES, "Actual source-acceptance binding")
    require(binding["git_base"] == EXPECTED_GIT_BASE, "Actual Git base must bind the specified joint-parent head")
    require(bool(binding["receipt_paths"]), "Actual metadata receipts required")
    for path in binding["receipt_paths"]:
        require(path in AUDIT_INPUT_PATHS and safe(path).is_file(), "Actual binding receipt must be a declared input")
    canonical_binding = read_json(PACKET + '/CANONICAL_BINDING.json')
    require(canonical_binding['kind'] == 'actual_resource_source_binding' and canonical_binding['canonical_parent_binding_complete'] is True and canonical_binding['root_read_complete'] is True, 'current resource binding schema')
    require(canonical_binding['bound_note_sha256'] == digest(note) and canonical_binding['actual_checkout_head'] == canonical_binding['actual_git_base'] == binding['git_base'], 'current resource binding identity')
    require(canonical_binding['canonical_parent_sha256'] == binding['parent_sha256'], 'current parent binding identity')
    require(binding['raw_bodies'] == body_map['bodies'] and binding['canonical_parents'] == dependencies, 'actual body and parent structure')
    require(binding['base_branch'] == canonical_binding['actual_branch_at_binding'] == 'physics-loop/toe-joint-readiness-20261015' and binding['planned_feature_branch'] == 'physics-loop/toe-readiness-resources-20261015', 'actual branch binding')
    require(binding['source_proposal_freeze']['sha256'] == '2ef4152f629f9985ee5872fcad1fa45811561b8e82b6bb0076a7366600995ce9' and binding['root_review_ack']['reviewed_source_sha256'] == binding['source_proposal_freeze']['sha256'], 'root reviewed source acknowledgment')
    require(binding['canonical_execution_not_yet_performed'] is True and binding['retained_audit'] is False, 'dated actual binding execution scope')
    prefix = PACKET + '/binding_sources/'
    expected_names = {'REFS.json', 'ROOT_SOURCE_REVIEW.json', 'historical_recorder.py', 'live_recorder.py', 'root_review_executed_source.py'}
    expected_names |= {label + '_' + name for label in ('fetch', 'inventory', 'root_review') for name in ('EXECUTION.json', 'stdout', 'stderr')}
    expected_names |= {label + '_' + name for label in ('stack', 'mass') for name in ('LAUNCH.json', 'EXECUTION.json', 'stdout', 'stderr')}
    require(len(binding['receipt_paths']) == len(expected_names) and set(binding['receipt_paths']) == {prefix + name for name in expected_names} and canonical_binding['receipt_paths'] == binding['receipt_paths'], 'exact binding receipt membership')
    root_raw = safe(prefix + 'ROOT_SOURCE_REVIEW.json').read_bytes()
    require(digest(root_raw) == binding['root_source_review']['sha256'] == 'b9dcc711130524ae3c254805cefc9b823411a1ac030e48a3440bbed5e8a125ea' and len(root_raw) == 8443, 'actual root review identity')
    root_review = json.loads(root_raw)
    require(root_review['kind'] == 'root_source_publication_review' and root_review['root_read_complete'] is True and root_review['source_draft_freeze']['sha256'] == binding['source_proposal_freeze']['sha256'], 'actual root review schema')
    require(root_review['sealed_members_verified'] == 122 and root_review['source_rows_verified'] == 82 and root_review['decision'] == 'Publication interpretation accepted at existing conditional source scope; actual checkout binding/integration still pending.', 'actual root review decision')
    require({row['name']: row['sha256'] for row in root_review['five_body_pins']} == EXPECTED_BODIES and root_review['parents'] == dependencies, 'actual root reviewed bodies and parents')
    require({key: row['sha256'] for key, row in root_review['existing_source_acceptances'].items()} == EXPECTED_ACCEPTANCES and root_review['scientific_programs_run'] == root_review['primary_runs'] == root_review['historical_programs_replayed'] == 0, 'root source scope and acceptances')
    refresh_raw = safe(prefix + 'REFS.json').read_bytes()
    require(digest(refresh_raw) == '169ca44ac55dffbe3fc24db8f4ef69602335b69ac9f4f642e8b18fb30f1598f4', 'exact refresh identity')
    refresh = json.loads(refresh_raw)
    require(binding['origin_main'] == refresh['refs']['origin/main'] == 'bbada1fe09b2d10d610560864d86b68c24a59713' and binding['instruction_revision'] == refresh['refs']['origin/ai/execution'] == '3a4b2c66a1ead7a1c48b4359627e968f681e3c39' and binding['historical_refresh_head'] == refresh['refs']['HEAD'] == EXPECTED_GIT_BASE, 'actual refresh ref binding')
    inventory = safe(prefix + 'inventory_stdout').read_bytes()
    check_identity(inventory, refresh['inventory'])
    require(len(json.loads(inventory)) == refresh['open_pr_count'] == 37, 'historical inventory schema')
    history_source = safe(prefix + 'historical_recorder.py').read_bytes()
    live_source = safe(prefix + 'live_recorder.py').read_bytes()
    require(digest(history_source) == 'd125f804ab1451c3b4ba51c4d4ab21a7d078329395dcb333aebe823b6342de95', 'historical recorder source identity')
    require(digest(live_source) == '12927c9b242ace99876b7fdbce7f4760cd538524c5ce59beea7ba4ae5fc7a516', 'live recorder source identity')
    for label, number, head, branch, base_branch in (
        ('stack', 9607, EXPECTED_GIT_BASE, 'physics-loop/toe-joint-readiness-20261015', 'physics-loop/toe-mass-scaled-mediator-transport-20261015'),
        ('mass', 9606, '1fcff4c8e3cfe5b8ae5fae1a31ae882609ff5939', 'physics-loop/toe-mass-scaled-mediator-transport-20261015', 'physics-loop/toe-shared-mediator-programming-20261015')):
        observed = binding['observed_parent_prs'][label]
        require(observed['number'] == number and observed['state'] == 'OPEN' and observed['isDraft'] is False and observed['headRefOid'] == head and observed['headRefName'] == branch and observed['baseRefName'] == base_branch, 'observed parent PR binding')
        require(read_json(prefix + label + '_stdout') == observed, 'observed parent PR stream')
        receipt = read_json(prefix + label + '_EXECUTION.json')
        launch_raw = safe(prefix + label + '_LAUNCH.json').read_bytes()
        require(receipt.get('exit_code') == 0 and isinstance(receipt.get('finished_utc'), str), 'live observation exit/schema')
        check_identity(launch_raw, receipt['launch'])
        launch = json.loads(launch_raw)
        require(launch['argv'] == ['gh', 'pr', 'view', str(number), '--repo', 'jonathonreilly/qubit-lattice-axiom-framework', '--json', 'number,state,isDraft,headRefOid,headRefName,baseRefName,url'] and launch['scientific_execution'] is False and launch['source_at_launch'] is None and launch['inputs_at_launch'] is None, 'live observation launch/schema')
        check_identity(live_source, launch['recorder'])
        for key in ('stdout', 'stderr'):
            check_identity(safe(prefix + label + '_' + key).read_bytes(), receipt[key])
    for label in ('fetch', 'inventory', 'root_review'):
        receipt = read_json(prefix + label + '_EXECUTION.json')
        require(receipt.get('exit_code') == 0 and isinstance(receipt.get('start_utc'), str) and isinstance(receipt.get('end_utc'), str) and isinstance(receipt.get('argv'), list), 'historical observation schema')
        check_identity(history_source, receipt['recorder'])
        for key in ('stdout', 'stderr'):
            check_identity(safe(prefix + label + '_' + key).read_bytes(), receipt[key])
        if label == 'fetch':
            require(receipt['argv'][0] == 'git' and receipt['argv'][-4:] == ['fetch', 'origin', 'main', 'ai/execution'] and receipt['child_source_at_launch'] is None, 'historical fetch command/source')
        elif label == 'inventory':
            require(receipt['argv'][:4] == ['gh', 'pr', 'list', '--repo'] and receipt['child_source_at_launch'] is None, 'historical inventory command/source')
        else:
            executed = safe(prefix + 'root_review_executed_source.py').read_bytes()
            check_identity(executed, receipt['child_source_at_launch'])
            require(digest(executed) == 'b9946f90122df51f9d8969332e5b0d98d71f3d50d10f840f37ac67cdfea94315' and Path(receipt['argv'][1]).name == 'readiness_resource_root_review.py', 'root review executed source')
            result = read_json(prefix + 'root_review_stdout')
            require(result['root_review']['sha256'] == digest(root_raw) and result['members'] == 122, 'root review output binding')
    require({'b34df6b7479df5b3960b02bf383ff7954621a10b1efb6831a25c65466d8da783', '465e95c3312a2e993888ed66b7a5b8f16abb391885d52687e4456df127d3955c', 'ff8cf33e30c43fed1b976a22b985189110fb9ac3524cd0e8359b50e56e1497ea'} <= {row['sha256'] for row in archive['objects']}, 'original equality failure and full correction archive')

    print(json.dumps({"result": "source_integrity_verified", "scope": "identities and body/dependency structure only",
                      "scientific_programs_run": 0, "historical_programs_replayed": 0,
                      "publication_or_retained_status_certified": False}, sort_keys=True))
    print("per_element: source bytes and correction provenance only; no physical element validation")
    print("per_site: exact parent geometry interface preserved; no new lattice execution")
    print("per_mode: full-input preparation and conditional ready-sector simulation scopes retained")
    print("per_block: five immutable bodies and two canonical mathematical dependencies checked")
    print("lattice_wide: no native supplier, common cap, full program, scientific run or audit certified")

if __name__ == "__main__":
    main()

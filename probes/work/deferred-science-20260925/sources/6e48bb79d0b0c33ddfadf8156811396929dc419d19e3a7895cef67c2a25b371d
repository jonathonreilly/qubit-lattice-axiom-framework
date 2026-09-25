"""Freeze only explicitly released inputs into this new publication subpacket.

This source-management utility writes new local copies and an inventory. It is
not the read-only scientific correspondence checker, and executes no sources.
"""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
PUB = BASE / "native-ground-publication"
SHA = lambda b: hashlib.sha256(b).hexdigest()
manifest_path = BASE / "NATIVE_GROUND_PUBLICATION_FROZEN_SOURCES.json"
assert SHA(manifest_path.read_bytes()) == "d0460afcbbcf15a646e655d44888069bde0648552797e5af3b043c7651846b6f"
manifest = json.loads(manifest_path.read_text())
rows = []
seen = {}

def freeze(origin, role, expected=None):
    origin = Path(origin)
    rel = origin.relative_to(BASE)
    body = origin.read_bytes()
    sha = SHA(body)
    if expected is not None:
        assert sha == expected, (str(origin), sha, expected)
    if str(origin) in seen:
        entry = seen[str(origin)]
        if role not in entry["roles"]:
            entry["roles"].append(role)
        return
    dest = HERE / "sources" / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("xb") as stream:
        stream.write(body)
    entry = {"origin": str(origin), "copy": str(dest.relative_to(HERE)),
             "sha256": sha, "bytes": len(body), "roles": [role]}
    rows.append(entry)
    seen[str(origin)] = entry

freeze(manifest_path, "Released 27-file publication manifest")
assert len(manifest["files_sha256"]) == 27
for rel, sha in manifest["files_sha256"].items():
    freeze(PUB / rel, "Frozen publication input/evidence", sha)
for rel in ["scripts/runner_cache.py"]:
    freeze(PUB / rel, "Read as data: cache fingerprint/serialization implementation")
for name in ["NATIVE_GROUND_PUBLICATION_CACHE_EXECUTION.json",
             "NATIVE_GROUND_PRIMARY_ROOT_VERIFICATION.json",
             "NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT01_FAILURE.json",
             "NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT02_FAILURE.json",
             "verify_native_ground_publication_primary.py"]:
    freeze(BASE / name, "Root process evidence only; never executed here")
failure = json.loads((BASE / "NATIVE_GROUND_PRIMARY_VERIFICATION_ATTEMPT02_FAILURE.json").read_text())
for item in failure["preserved_files"]:
    freeze(item["path"], "Preserved second root bookkeeping failure; never executed", item["sha256"])

packets = {
    "native-one-pair-spectrum-personal": {"AUTHOR_SEAL.json": "69a754ada477506f4437705dbb49e8ebe93b3c230185b7376b3b8d6bfb18dc6d"},
    "native-ground-filling-personal": {"AUTHOR_SEAL.json": "0b72c3cd4dd5404a53de9808a5bf99fab48eab182defedba729b695ff4202066"},
    "ground-formation-incompatibility-personal": {"AUTHOR_SEAL.json": "24e2131d01c9e47b9d8c684486e726ab753d7cab1962566baee13fbd5fead572"},
    "native-one-pair-spectrum-independent": {
        "PRE_SEAL.json": "bed28ea9c81afb7822d0ddeeb552260e3e0547b6f387c9edb8dbd6aec83ee25b",
        "POST_SEAL.json": "69a4ee27e9f7990945f2f2ed54a269fd9221314ef726be69833eac2020519de9"},
    "native-ground-filling-independent": {
        "PRE_SEAL.json": "0d420d0263cb53ed341d79f361cfc7ee2dae9125f976b6715216bd48a5cd8384",
        "POST_SEAL.json": "913f1afadcdb43214ee63108b015e8e95df6c1cc98221a07295a99afbb404bed"},
    "ground-formation-incompatibility-independent": {
        "PRE_SEAL.json": "108fa39b7d3f86f2b9fd825307da6861dd8548bf9295a3415024a72dd19c4f51",
        "POST_SEAL.json": "85c0e0e9fc2c05217d48d21c73a8927b8c7f5718073355d65640c9a93fb41451"},
}
seals = []
for packet, names in packets.items():
    for name, expected in names.items():
        source = BASE / packet / name
        freeze(source, "Released prior seal, integrity checked without execution", expected)
        seal = json.loads(source.read_text())
        members = seal.get("members", seal.get("files"))
        if isinstance(members, dict):
            members = [dict(path=p, **v) for p, v in members.items()]
        verified = []
        for member in members:
            p = source.parent / member["path"]
            body = p.read_bytes()
            assert SHA(body) == member["sha256"], str(p)
            if "bytes" in member:
                assert len(body) == member["bytes"], str(p)
            verified.append({"path": str(p), "sha256": SHA(body), "bytes": len(body)})
            # Author inputs are copied completely. Independent packet science is
            # bound by seals; only its complete reports and source inventories
            # are recopied, so no historical writer is accidentally used.
            if packet.endswith("-personal") or member["path"] in ["PRE.md", "POST.md", "SOURCE_PINS.json", "POST_SOURCE_PINS.json"]:
                freeze(p, "Released prior author source/evidence" if packet.endswith("-personal") else "Released prior independent report/pins", member["sha256"])
        seals.append({"origin": str(source), "sha256": expected,
                      "verified_member_count": len(verified), "members": verified})

inventory = {"frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
             "scope": "Released-source bounded publication correspondence; no new blind claim or scientific rerun.",
             "publication_manifest_sha256": SHA(manifest_path.read_bytes()),
             "sources": rows, "prior_seals": seals,
             "existing_reports_unmodified": True, "author_programs_executed": False}
with (HERE / "SOURCE_INVENTORY.json").open("x") as out:
    json.dump(inventory, out, indent=2)
    out.write("\n")
print(json.dumps({"frozen_source_count": len(rows), "prior_seals": [
    {k: v for k, v in x.items() if k != "members"} for x in seals],
    "inventory_sha256": SHA((HERE / "SOURCE_INVENTORY.json").read_bytes())}, indent=2))

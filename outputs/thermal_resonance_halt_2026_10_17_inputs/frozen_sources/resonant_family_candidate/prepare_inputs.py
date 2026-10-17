"""Read-only source copying/hash bookkeeping; contains no scientific calculation."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import os

D = Path(__file__).resolve().parent
N = D.parent
W = N.parent / "correlation_worktree"
sources = [
 ("fixed.md", N/"resonant_escape_candidate/CANDIDATE.md", "c68350310ac5c471a38940660d76ba74d982306e2d62a28bbf9c330e79c984b8"),
 ("fixed_review.md", N/"resonant_escape_review/REPORT.md", "4d7694f51ec85edcc38977bef43412d8c9bc5baba4fa3c35809fe9adf3d00284"),
 ("fixed_acceptance.json", N/"resonant_escape_root_qualification/ACCEPTANCE.json", "1a3f12fa10400e13906a09954f328e996f5cba2755a91c879399662f7a3f1421"),
 ("fixed_qualification.md", N/"resonant_escape_root_qualification/QUALIFICATION.md", "0f77e687647ceaec73408aaf58eea65b4291337c9bddb496e3ca759b1690bed5"),
 ("family.md", N/"emitter_resource_family_candidate/CANDIDATE.md", "9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac"),
 ("family_acceptance.json", N/"emitter_family_root_qualification/ACCEPTANCE.json", "a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325"),
 ("family_qualification.md", N/"emitter_family_root_qualification/QUALIFICATION.md", "27a4008d6588fef9f0a5ac1d231d71240c12468db93d50a36ac2ee02f6ab7814"),
 ("installed.md", N/"emitter_installed_certificate/CANDIDATE.md", "4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee"),
 ("installed_acceptance.json", N/"emitter_installed_root_review/ACCEPTANCE.json", "c99e0c13ec2469910d74d1fe487d9d4ae09539d1ca3d46f53047dc36d509963c"),
 ("installed_qualification.md", N/"emitter_installed_root_review/QUALIFICATION.md", "dfe73e8d332dc81bac378daf480662f74e95e3091f01fce11d6e2098f7d7596d"),
 ("weighted.md", N/"weighted_emitter_escape_candidate/CANDIDATE.md", "a2e96d2947b1e0deef2417d4673ddc8afd54f7382236aee6913ba6cae98e32b5"),
 ("weighted_acceptance.json", N/"weighted_emitter_root_qualification/ACCEPTANCE.json", "01e6cf9d8e54d8dd38157f5901a0c9c2b7bc0ed2890e7895b2213a26b1469a16"),
 ("weighted_qualification.md", N/"weighted_emitter_root_qualification/QUALIFICATION.md", "f3513816c0bbe060f50860e02a2f1c49afcd42056314af9cc161885076882f4b"),
 ("moment.md", N/"ballistic_emitter_escape_candidate/CANDIDATE.md", "31449e982b27e623491f4e9cb0c8239e2ff15ebc9605668b8e4684055c52410f"),
 ("moment_acceptance.json", N/"ballistic_emitter_root_qualification/ACCEPTANCE.json", "bd2059184e105bd41437b1c28ca3f106a441215e09eac7a2b3ec316cbd674318"),
 ("moment_qualification.md", N/"ballistic_emitter_root_qualification/QUALIFICATION.md", "0b0ce9eaba582d878b982ecd0f86a53857c5f394b9a42b4e27306e58bb405102"),
 ("generic_v2.md", N/"finite_channel_wavepacket_bridge/THEOREM_V2.md", "db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3"),
 ("route.md", N/"autonomous_emitter_route/ROUTE.md", "f03626e591cddc3448bee72148edbee4717ae64af3a6543d4b5c184e7ef9f0a1"),
 ("interval.md", N/"two_body_interval_bridge/CANDIDATE.md", "b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45"),
 ("interval.json", N/"two_body_interval_bridge/CERTIFICATE.json", "a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251"),
 ("SCIENCE_WORKFLOW.md", W/"docs/ai_methodology/SCIENCE_WORKFLOW.md", "71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3")
]
entries=[]
for name, original, expected in sources:
    raw=original.read_bytes()
    digest=sha256(raw).hexdigest()
    if digest != expected:
        raise RuntimeError(f"Source identity mismatch: {original}: {digest} != {expected}")
    target=D/"inputs"/name
    if target.exists():
        raise RuntimeError(f"Refusing to overwrite snapshot: {target}")
    with target.open("xb") as out:
        out.write(raw); out.flush(); os.fsync(out.fileno())
    st=original.stat()
    entries.append({"snapshot":str(target.relative_to(D)),"original":str(original),"sha256":digest,"bytes":len(raw),"original_mtime_ns":st.st_mtime_ns,"original_device":st.st_dev,"original_inode":st.st_ino})
manifest={"created_utc":datetime.now(timezone.utc).isoformat(),"status":"byte-exact read-only source snapshots; historical labels unchanged", "claimed_repository_parent_from_task":"0e3993770a7a2dd872018f9dd3c76c2d9a624db9", "no_git_command_used":True, "entries":entries}
with (D/"SOURCE_MANIFEST.json").open("x") as out:
    json.dump(manifest,out,indent=2); out.write("\n"); out.flush(); os.fsync(out.fileno())
print(json.dumps({"source_count":len(entries),"manifest_sha256":sha256((D/"SOURCE_MANIFEST.json").read_bytes()).hexdigest(),"all_expected_pins_matched":True},indent=2))

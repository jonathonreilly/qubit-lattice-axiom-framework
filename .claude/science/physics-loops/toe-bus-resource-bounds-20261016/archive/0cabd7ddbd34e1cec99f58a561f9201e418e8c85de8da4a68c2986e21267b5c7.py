"""Read-only upstream source capture; metadata only, no scientific program replay."""
from pathlib import Path
import hashlib, json, datetime

OUT = Path(__file__).resolve().parent
N = OUT.parent
W = N.parent / 'correlation_worktree'
ITEMS = [
 ('proposal', N/'bus_preparation_resource_root_proposal/PROPOSED_LEMMAS.md', '625b1f6f9496fd4acea138f0b25b56afa8f0e90265b5bcdcabcdcd88a660e990', 'complete current read'),
 ('proposal_freeze', N/'bus_preparation_resource_root_proposal/FREEZE.json', '417eb37260f4391671650b3595e66755b9a301a0de4836ad4a19d44ffcd469c8', 'identity and proposal member'),
 ('resource_derivation', N/'reachable_bus_resource_candidate/DERIVATION.md', 'ce3ddd3ad376016f391992b30485454378607e6953fddcdeb2ecea702777d875', 'complete current read, sections 1-13'),
 ('resource_freeze', N/'reachable_bus_resource_candidate/FREEZE.json', '1eb2a662f00fe01c6d2bcee35c8039d0038001ed9a694980f6a5dbc9325a8996', 'identity only; other members not replayed or revalidated'),
 ('resource_acceptance', N/'reachable_bus_resource_root_review/QUALIFIED_ACCEPTANCE.json', 'd02d9205f451d73da584581970ff333ffd6d87a53a695c1e1b992db9ec615edd', 'complete current read'),
 ('resource_qualifications', N/'reachable_bus_resource_root_review/FINAL_QUALIFICATIONS.md', 'e50497e74e2022f97e6b1a42ff8bf176c2c7b30cd16b68d22b18f503457e541b', 'complete current read'),
 ('slew_acceptance', N/'bus_bounded_slew_preparation_root_review/QUALIFIED_ACCEPTANCE.json', 'b237e6550c7b500ff48cdaa2cd30e50cf4895205a610e8feb677da085bf82473', 'complete current read'),
 ('slew_qualifications', N/'bus_bounded_slew_preparation_root_review/FINAL_QUALIFICATIONS.md', '1c3714faadd94da6cc7789eb3472406ea2a5195b453ad941dbb163bb606ecc25', 'complete current read'),
 ('slew_proposal', N/'bus_bounded_slew_preparation_root_proposal/PROPOSED_LEMMAS.md', '6e09476675188bc8053e2b3b00095db3eb5e1ebf59c816c923da0675a33edc44', 'complete prior same-revision read reused'),
 ('slew_review', N/'bus_bounded_slew_preparation_exposed_check/REVIEW.md', 'a1b9ef4621b2a4a420d86f30c16449273d0a0a4bc46f22d078a4b2884cbda1d1', 'own complete prior derivation reused; no old computation replay'),
 ('slew_review_freeze', N/'bus_bounded_slew_preparation_exposed_check/FREEZE.json', '6794345fce3b8f11bb990512de09c1f40893f290d00d8e0032005ed783757525', 'prior verified freeze identity only; old runs not replayed'),
 ('installed_preparation', N/'bus_installed_preparation_candidate/DERIVATION.md', '71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29', 'complete prior same-revision read reused'),
 ('preparation_acceptance', N/'bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json', '28bef1945c65f807be837286d6e795d888f3d8b9ebb75024ac26ee0084409641', 'complete prior same-revision read reused'),
 ('preparation_qualifications', N/'bus_preparation_root_review/FINAL_QUALIFICATIONS.md', '1c94a58239c1bd9d168c837cf961522264a1f2d1705f3897ef541a3c8ced788e', 'complete prior same-revision read reused'),
 ('canonical_bus', W/'docs/STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md', '1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b', 'prior wrapper lines 1-151 and original mathematical sections 1-11 lines 230-668 reused; appended historical material not newly reviewed'),
]
def sha(data): return hashlib.sha256(data).hexdigest()

def main():
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    records = []
    # Check every selected upstream pin before writing source snapshots.
    loaded = []
    for key, src, expected, coverage in ITEMS:
        data = src.read_bytes()
        actual = sha(data)
        if actual != expected:
            raise RuntimeError(f'Upstream identity mismatch: {src}: {actual} != {expected}')
        loaded.append((key, src, data, actual, coverage))
    for key, src, data, actual, coverage in loaded:
        dest = OUT/'sources'/f'{key}{src.suffix}'
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.read_bytes() != data:
            raise RuntimeError(f'Refusing to replace changed snapshot: {dest}')
        dest.write_bytes(data)
        records.append(dict(key=key, original=str(src), capture=str(dest.relative_to(OUT)),
                            bytes=len(data), sha256=actual, read_coverage=coverage))
    result = dict(status='selected source identities verified and copied',
                  started_utc=start, completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  scientific_executions=0, metadata_only=True,
                  scope='Selected controlling texts only; not the full transitive execution/archive closure of historical freezes.',
                  sources=records)
    (OUT/'SOURCES.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], selected_sources=len(records), scientific_executions=0)))

if __name__ == '__main__': main()

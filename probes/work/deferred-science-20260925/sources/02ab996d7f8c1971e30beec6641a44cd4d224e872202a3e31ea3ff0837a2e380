"""Freeze only the released author40 packet; preserve all earlier local files."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json

HERE = Path(__file__).resolve().parent
AUTHOR = HERE.parent / 'native-charge-identification-personal'
DEST = HERE / 'post_sources'

def digest(data):
    return sha256(data).hexdigest()

def identify(path):
    data = path.read_bytes()
    stat = path.stat()
    return {'path':str(path), 'sha256':digest(data), 'bytes':len(data),
            'mtime_ns':stat.st_mtime_ns, 'ctime_ns':stat.st_ctime_ns}

def put(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(data)

def main():
    original = [identify(p) for p in sorted(HERE.rglob('*')) if p.is_file()
                and not p.name.startswith('post_') and 'post_sources' not in p.parts]
    seal_bytes = (AUTHOR/'AUTHOR_SEAL.json').read_bytes()
    assert digest(seal_bytes) == '08dd5ec99ddeccfb7f70a50e216cd40e3cf8ab954cbda6fca27fbbfcaecad83a'
    seal = json.loads(seal_bytes)
    pins = []
    for member in seal['members'] + [{'path':'AUTHOR_SEAL.json','sha256':digest(seal_bytes),'bytes':len(seal_bytes)}]:
        origin = AUTHOR/member['path']
        data = origin.read_bytes()
        assert digest(data)==member['sha256'] and len(data)==member['bytes']
        target = DEST/'author'/member['path']
        put(target, data)
        pins.append({'role':'released_author_source_or_evidence','origin':str(origin),
                     'frozen_path':str(target.relative_to(HERE)), **member})
    receipt = HERE.parent/'FORTIETH_PRE_ROOT_REVIEW.json'
    data = receipt.read_bytes()
    target = DEST/receipt.name
    put(target,data)
    pins.append({'role':'root_process_receipt_only','origin':str(receipt),
                 'frozen_path':str(target.relative_to(HERE)),
                 'sha256':digest(data),'bytes':len(data)})
    pre = json.loads((HERE/'PRE_SEAL.json').read_bytes())
    assert len(pre['members'])==54
    for member in pre['members']:
        data=(HERE/member['path']).read_bytes()
        assert digest(data)==member['sha256'] and len(data)==member['bytes']
    inherited=[]
    for member in json.loads((HERE/'SOURCE_PINS.json').read_bytes())['sources']:
        inherited.append(member)
    output={'phase':'released-source POST40','frozen_at_utc':datetime.now(timezone.utc).isoformat(),
            'new_source_pins':pins, 'inherited_PRE_source_pins':inherited,
            'PRE_seal_sha256':digest((HERE/'PRE_SEAL.json').read_bytes()),
            'preserved_prior_files':original,
            'scope':'Only author40 seal members and requested process receipt frozen. Prior-source pins reused without following author metadata references into other packets.'}
    put(HERE/'POST_SOURCE_PINS.json',(json.dumps(output,indent=2)+'\n').encode())
    print(json.dumps({'frozen_author_files':28,'root_receipts':1,'preserved_prior_files':len(original),
                      'PRE_members_verified':54,'pins_sha256':digest((HERE/'POST_SOURCE_PINS.json').read_bytes())},indent=2))

if __name__=='__main__':
    main()

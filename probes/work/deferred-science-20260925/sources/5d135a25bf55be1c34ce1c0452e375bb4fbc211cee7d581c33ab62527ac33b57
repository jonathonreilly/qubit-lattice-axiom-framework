"""New publication correspondence snapshots; only authorized exact sources."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess

HERE=Path(__file__).resolve().parent
OWN=HERE.parent
EXT=OWN.parent
PUB=EXT/'birth-charge-transport-publication'

def observed(path):
    st=path.stat();raw=path.read_bytes()
    return dict(path=str(path),sha256=sha256(raw).hexdigest(),bytes=len(raw),mode=st.st_mode,
                dev=st.st_dev,ino=st.st_ino,mtime_ns=st.st_mtime_ns,ctime_ns=st.st_ctime_ns,nlink=st.st_nlink)

def write(name,obj):
    with (HERE/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')

pins=[];seen={}
def capture(origin,snapshot,role,expected=None):
    if str(origin) in seen:return seen[str(origin)]
    row=observed(origin)
    if expected:assert row['sha256']==expected
    target=HERE/'sources'/snapshot
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open('xb') as f:f.write(origin.read_bytes())
    record=dict(origin=str(origin),snapshot=str(target.relative_to(HERE)),role=role,**{k:v for k,v in row.items() if k!='path'})
    pins.append(record);seen[str(origin)]=record
    return record

freeze=EXT/'BIRTH_CHARGE_TRANSPORT_FROZEN_SOURCES.json'
frozen=json.loads(freeze.read_text())
external_names=('BIRTH_CHARGE_TRANSPORT_FROZEN_SOURCES.json',
    'BIRTH_CHARGE_TRANSPORT_PRIMARY_ROOT_VERIFICATION.json',
    'BIRTH_CHARGE_TRANSPORT_PRIMARY_EXECUTION.json',
    'BIRTH_CHARGE_TRANSPORT_PUBLICATION_WORKING_SOURCES.json',
    'BIRTH_CHARGE_TRANSPORT_GRAPH_BUILD.stdout.txt','BIRTH_CHARGE_TRANSPORT_GRAPH_BUILD.stderr.txt')
for name in external_names:capture(EXT/name,'external/'+name,'Released publication/process evidence')
for rel,expected in frozen['files_sha256'].items():
    capture(PUB/rel,'publication/'+rel,'Authoritative publication freeze input',expected)
for rel in ('scripts/runner_cache.py','AGENTS.md','docs/ai_methodology/SCIENCE_WORKFLOW.md'):
    capture(PUB/rel,'publication/'+rel,'Mechanical cache code or unchanged procedure')

packets=(
    ('author42',EXT/'native-birth-charge-cluster-personal',('AUTHOR_SEAL.json',)),
    ('author43',EXT/'native-birth-cluster-transport-personal',('AUTHOR_SEAL.json',)),
    ('independent42',EXT/'native-birth-charge-cluster-independent',('PRE_SEAL.json','POST_SEAL.json')),
)
seal_summaries=[]
for label,directory,seals in packets:
    for name in seals:
        srow=capture(directory/name,label+'/'+name,'Explicitly released seal')
        seal=json.loads((directory/name).read_text())
        for member in seal['members']:
            relative=Path(member['path'])
            assert not relative.is_absolute() and '..' not in relative.parts
            row=capture(directory/relative,label+'/'+str(relative),'Explicitly released member',member['sha256'])
            assert row['bytes']==member['bytes']
        seal_summaries.append(dict(label=label,seal=name,sha256=srow['sha256'],members=len(seal['members'])))

own=[]
own_paths=set()
for name in ('PRE_SEAL.json','POST_SEAL.json'):
    seal=json.loads((OWN/name).read_text())
    own_paths.add(OWN/name)
    for row in seal['members']:
        path=OWN/row['path'];seen_row=observed(path)
        assert seen_row['sha256']==row['sha256'] and seen_row['bytes']==row['bytes']
        own_paths.add(path)
for name in ('PRE_SEAL_RECEIPT.json','POST_SEAL_RECEIPT.json'):own_paths.add(OWN/name)
for path in sorted(own_paths):own.append(observed(path))

base=frozen['base_revision']
relative='docs/audit/data/citation_graph_manifest.json'
raw=subprocess.check_output(['git','-C',str(PUB),'show',base+':'+relative])
target=HERE/'sources/base_citation_graph_manifest.json'
with target.open('xb') as f:f.write(raw)
git_context=dict(base_revision=base,graph_base_path=relative,base_graph_snapshot=str(target.relative_to(HERE)),
                 base_graph_sha256=sha256(raw).hexdigest(),
                 observed_HEAD=subprocess.check_output(['git','-C',str(PUB),'rev-parse','HEAD'],text=True).strip(),
                 observed_branch=subprocess.check_output(['git','-C',str(PUB),'branch','--show-current'],text=True).strip())
write('OWN_43_PRESERVATION_BEFORE.json',dict(files=own,stat_scope='Bytes and stable file stats; access time excluded.'))
write('SOURCE_PINS.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),phase='Released publication correspondence42+43',
    sources=pins,seals=seal_summaries,git_context=git_context,own43_files=len(own),
    frozen_manifest_sha256=sha256(freeze.read_bytes()).hexdigest(),
    no_source_references_beyond_released_members_followed=True,
    no_scientific_program_or_sealed_writer_execution=True))
print(json.dumps(dict(source_pins_sha256=sha256((HERE/'SOURCE_PINS.json').read_bytes()).hexdigest(),
    source_count=len(pins),seals=seal_summaries,own43_files=len(own),git_context=git_context),indent=2))

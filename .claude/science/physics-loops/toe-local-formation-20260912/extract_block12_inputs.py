#!/usr/bin/env python3
"""Copy pinned accepted-source data; this does not recertify its physical truth."""
from pathlib import Path
import hashlib
import json
import subprocess

HERE=Path(__file__).resolve().parent
REF='a2aca4bcf2d6c0c3868b852017de327f888f270a'
SOURCES={
 'quartic_inputs.json':'.claude/science/physics-loops/native-quartic-ward-20260910/source_draft/packet/INPUTS.json',
 'omega5_result.json':'.claude/science/physics-loops/native-finite-moment-ward-20260910/imports/OMEGA5_RESULT.json',
 'omega79_result.json':'.claude/science/physics-loops/native-gaussian-moment-jet-20260910/source_draft/omega/RESULT.json',
}


if __name__=='__main__':
    dest=HERE/'block12_inputs';dest.mkdir(exist_ok=True)
    entries=[]
    for name,path in SOURCES.items():
        raw=subprocess.check_output(['git','show',REF+':'+path])
        json.loads(raw)
        (dest/name).write_bytes(raw)
        entries.append({'revision':REF,'original_path':path,'copy':'block12_inputs/'+name,
                        'sha256':hashlib.sha256(raw).hexdigest()})
    (HERE/'BLOCK12_INPUT_MANIFEST.json').write_text(json.dumps({'sources':entries,
       'status':'pinned source copies; physical scalar/moment certificate truth inherited from source notes',
       'independent_replay':'not performed; new Clifford identities and arithmetic checked separately'},indent=2)+'\n')
    print(json.dumps(entries,indent=2))

#!/usr/bin/env python3
"""Freeze the declared sixteen-history follow-up using the unchanged simulator."""
from pathlib import Path
import datetime,hashlib,json,platform,subprocess,sys,time
HERE=Path(__file__).resolve().parent
def identity(p):
    p=Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,x):Path(p).write_text(json.dumps(x,indent=2)+'\n')
def run(cmd,prefix):
    start=time.time();p=subprocess.run(list(map(str,cmd)),capture_output=True)
    Path(str(prefix)+'.stdout').write_bytes(p.stdout);Path(str(prefix)+'.stderr').write_bytes(p.stderr)
    receipt=dict(command=list(map(str,cmd)),returncode=p.returncode,seconds=time.time()-start,
      stdout=identity(str(prefix)+'.stdout'),stderr=identity(str(prefix)+'.stderr'))
    save(str(prefix)+'.receipt.json',receipt);assert p.returncode==0 and not p.stderr
    return json.loads(p.stdout),receipt
def main():
    root=Path(sys.argv[1]).resolve();binary=Path(sys.argv[2]).resolve();root.mkdir(exist_ok=False)
    for name in ['geometry','validation','histories']:(root/name).mkdir()
    original=Path(sys.argv[3]).resolve();old=json.loads(original.read_text())
    assert identity(binary)==old['binary']
    assert identity(HERE/'dimer_routed_dynamics.cpp')==old['source']
    geometry=[];validation=[]
    for i,kind in enumerate(['winding','irregular']):
        seed=29122000+256+1000*i;path=root/'geometry'/f'N256_{kind}.bin'
        value,receipt=run([binary,'geometry',256,kind,seed,path],root/'geometry'/f'N256_{kind}')
        assert value['N']==256 and (kind=='winding' or value['accepted_flips']>0)
        geometry.append(dict(N=256,kind=kind,seed=seed,file=identity(path),generator=value,command_receipt=receipt))
        valpath=root/'validation'/f'N256_{kind}.json'
        val,vr=run([binary,'validate',path,202609218900+i,valpath],valpath)
        result=json.loads(valpath.read_text());assert result['key_permutation_verified'] and result['counts_verified']
        validation.append(dict(output=identity(valpath),state=identity(str(valpath)+'.state'),
          command_receipt=vr,attempts=val['attempts'],wall_seconds=val['wall_seconds'],
          scope='Unchanged simulator internal full checks; separate endpoint reconstruction remains pending.'))
        print(json.dumps(dict(kind=kind,validation_seconds=val['wall_seconds'],validation_attempts=val['attempts'])),flush=True)
    jobs=[]
    for i,kind in enumerate(['winding','irregular']):
        for rep in range(1,9):
            seed=202609261900+10000*i+rep;path=root/'histories'/f'N256_{kind}_r{rep:03}.json'
            jobs.append(dict(N=256,kind=kind,replicate=rep,seed=seed,output=str(path),
              command=[str(binary),'run',str(root/'geometry'/f'N256_{kind}.bin'),str(seed),str(path)]))
    assert len(jobs)==len({j['seed'] for j in jobs})==16
    save(root/'MANIFEST.json',dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      protocol=identity(HERE/'DIMER_ROUTED_256_FOLLOWUP_PROTOCOL.md'),
      construction=identity(HERE/'DIMER_ROUTED_RECORD_TRANSPORT.md'),source=identity(HERE/'dimer_routed_dynamics.cpp'),
      setup=identity(__file__),binary=identity(binary),original_manifest=identity(original),
      platform=dict(system=platform.platform(),python=sys.version),geometry=geometry,validation=validation,jobs=jobs,
      scope='Post-analysis larger-volume follow-up, fixed sixteen histories; no outcome-dependent sample selection.'))
    print(json.dumps(identity(root/'MANIFEST.json')),flush=True)
if __name__=='__main__':main()

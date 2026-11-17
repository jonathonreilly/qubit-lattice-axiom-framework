"""Run after every numeric process exits. Hash scratch data and copy small CSVs."""
import datetime as dt
import json
from pathlib import Path
import re
import shutil
from batch import HERE,SCRATCH,sha,utc,gate,ROOT

def main():
    gate()
    phases=('gh','p4','face')
    chains=[];phase_records=[]
    for phase in phases:
        plan=json.loads((HERE/(phase+'_plan.json')).read_text())
        batch=json.loads((HERE/(phase+'_batch.json')).read_text())
        analysis=json.loads((HERE/(phase+'_analysis_receipt.json')).read_text())
        verification=json.loads((HERE/(phase+'_verification.json')).read_text())
        if not batch['all_reaped']:raise RuntimeError('unreaped batch')
        phase_records.append(dict(phase=phase,batch=batch,analysis=analysis,verification=verification))
        for item in plan['chains']:
            receipt=json.loads((HERE/(item['tag']+'.json')).read_text())
            if not receipt['reaped'] or receipt['exit_code']!=0:raise RuntimeError('bad exit')
            for record in receipt['records']:
                p=Path(record['path'])
                if sha(p)!=record['sha256'] or p.stat().st_size!=record['bytes']:
                    raise RuntimeError('raw hash/size mismatch '+str(p))
                if p.name.endswith('.csv') and p.stat().st_size<=1_000_000:
                    dest=HERE/p.name
                    shutil.copyfile(p,dest)
                    if sha(dest)!=record['sha256']:raise RuntimeError('copy differs')
                    record['small_copy']=dest.name
            log=(HERE/(item['tag']+'.log')).read_text()
            receipt['nice']=int(re.search(r' nice (\d+)',log)[1])
            receipt['peak_rss_bytes']=int(re.search(r'peak_rss (\d+)',log)[1])
            if receipt['peak_rss_bytes']>2_000_000_000:raise RuntimeError('RSS exceeded')
            chains.append(receipt)
    ordered=sorted(chains,key=lambda r:r['started'])
    serial=all(a['ended']<=b['started'] for a,b in zip(ordered,ordered[1:]))
    if not serial:raise RuntimeError('production overlap')
    if not (phase_records[0]['analysis']['ended']<=phase_records[1]['batch']['started'] and
            phase_records[1]['analysis']['ended']<=phase_records[2]['batch']['started']):
        raise RuntimeError('analysis/successor phase ordering')
    details=[]
    for phase in phases:
        for row in json.loads((HERE/(phase+'_summary.json')).read_text()):
            item=row['detail'];p=Path(item['path'])
            if sha(p)!=item['sha256']:raise RuntimeError('detail hash mismatch')
            if p.stat().st_size<=1_000_000:
                dest=HERE/p.name
                shutil.copyfile(p,dest)
                if sha(dest)!=item['sha256']:raise RuntimeError('detail copy differs')
                item['small_copy']=dest.name
            details.append(item)
    sources=[]
    paths=[SCRATCH/'sa_ym4.tex',SCRATCH/'sa_ca_I.tex',SCRATCH/'automation_lock.py',
           Path('/tmp/sa-gap-long-skala.YIk2wV/paper.pdf'),
           HERE.parent/'gap-descent-mc-astra/su2_guarded.cpp',
           HERE.parent/'gap-descent-mc-astra/analyze.py',ROOT/'scripts/lab_ops.py']
    paths+=sorted(HERE.glob('*.py'))+sorted(HERE.glob('*.cpp'))
    for p in paths:sources.append(dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p)))
    pilots=[dict(path=str(p),bytes=p.stat().st_size,sha256=sha(p),excluded=True)
            for p in sorted(SCRATCH.glob('pilot_*')) if p.is_file()]
    manifest=dict(completed=utc(),source_commit='2b67c749cc219d0051de7b26c2a62c77c3948266',
        source_main='8b11ae2bb95e641494fe75ed83d108ee712fa3a9',scratch=str(SCRATCH),
        chains=chains,details=details,sources=sources,pilots=pilots,phases=phase_records,
        production_serial=serial,chains_count=len(chains),
        memory_free_min_pct=min(x['memory_free_pct'] for x in chains),
        peak_sampler_rss_bytes=max(x['peak_rss_bytes'] for x in chains),
        actual_nice_values=sorted(set(x['nice'] for x in chains)),
        scientific_status='GUIDE / OPEN only; no proof discharge or mass-gap claim')
    (HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(json.dumps({k:manifest[k] for k in ('chains_count','production_serial',
        'memory_free_min_pct','peak_sampler_rss_bytes','actual_nice_values')}))

if __name__=='__main__':main()

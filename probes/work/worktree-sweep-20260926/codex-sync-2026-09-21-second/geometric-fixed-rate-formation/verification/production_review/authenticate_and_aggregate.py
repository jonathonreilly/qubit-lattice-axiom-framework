#!/usr/bin/env python3
"""Post-endpoint-seal comparison and full saved-table aggregation.

Does not read analysis RESULTS.json or TABLE.md. Does not decode unselected
NPZ archives. All receipt files are hashed in place; no large files copied.
"""
from pathlib import Path
from collections import Counter,defaultdict
from concurrent.futures import ThreadPoolExecutor
import datetime,hashlib,json,math,time
HERE=Path(__file__).resolve().parent;RAW=HERE.parent
PROD=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-21-second/geometric_fixed_rate_followup')
ANAL=PROD.parent/'geometric_fixed_rate_analysis'
COLUMNS=('S1','S2','S3','S4','W','axis_mode_square','axis_shell_square','winding_square','time_per_volume','slides_per_site','site_reuse_fraction')
SPEC={'S1':(0,None,1),'W':(4,None,1),'S2_over_S1':(1,0,1),'S3_over_S1':(2,0,1),
      'S4_over_S1':(3,0,1),'W_over_S1':(4,0,1),'axis_mode_fourth_ratio':(5,0,2),
      'axis_shell_fourth_ratio':(6,0,2),'winding_fourth_ratio':(7,4,2),
      'time_per_volume':(8,None,1),'slides_per_site':(9,None,1),'site_reuse_fraction':(10,None,1)}
def identity(path):
    path=Path(path);h=hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1<<20),b''):h.update(block)
    return {'path':str(path),'bytes':path.stat().st_size,'sha256':h.hexdigest()}
def load(p):return json.loads(p.read_text())
def save(name,data): (HERE/name).write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
def close(a,b,atol=1e-12,rtol=1e-12):
    assert abs(a-b)<=atol+rtol*max(abs(a),abs(b)),(a,b)
    return abs(a-b)

def aggregate(rows):
    n=len(rows);assert n>=2
    mean=[math.fsum(row[i] for row in rows)/n for i in range(len(COLUMNS))]
    covariance=[[math.fsum((row[i]-mean[i])*(row[j]-mean[j]) for row in rows)/(n-1) for j in range(len(COLUMNS))] for i in range(len(COLUMNS))]
    values={}
    for name,(num,den,power) in SPEC.items():
        if den is not None and mean[den]<=0:
            values[name]={'estimate':None,'estimate_status':'zero_denominator','standard_error':None,'standard_error_status':'zero_denominator'};continue
        gradient=[0.]*len(COLUMNS)
        if den is None:value=mean[num];gradient[num]=1.
        else:
            value=mean[num]/mean[den]**power
            gradient[num]=mean[den]**(-power)
            gradient[den]=-power*mean[num]/mean[den]**(power+1)
        variance=math.fsum(gradient[i]*gradient[j]*covariance[i][j] for i in range(len(COLUMNS)) for j in range(len(COLUMNS)))/n
        assert variance>=0,(name,variance)
        values[name]={'estimate':value,'estimate_status':'defined','standard_error':math.sqrt(variance),'standard_error_status':'defined'}
    return {'n':n,'column_means':dict(zip(COLUMNS,mean)),'sample_covariance':covariance,'observables':values}

def run():
    seal=load(HERE/'ENDPOINT_PRECOMPARISON_SEAL.json')
    for row in seal['artifacts']+seal['sources']:assert identity(row['path'])==row
    selected=load(HERE/'ENDPOINT_RECONSTRUCTION.json')
    selected_by_name={r['selection']['name']:r for r in selected['rows']}
    expected_modes={tuple(m) for m in load(HERE/'SELECTION.json')['declared_modes']}
    manifest=load(PROD/'MANIFEST.json');summary=load(PROD/'SUMMARY.json')
    declared=[(N,b,210000000+10000*N+1000*j+rep) for N in [16,32,64,128] for j,b in enumerate([.1,1,10]) for rep in range(1,(64 if N==128 else 256)+1)]
    assert len(declared)==2496 and list(map(tuple,manifest['cases']))==declared
    assert summary['manifest']==manifest and not manifest['pilot']
    assert manifest['workers']==2 and manifest['event_cap']==10**9 and manifest['kappa']==1 and manifest['nu']==0
    for key,filename in [('source_sha256','geometric_partner_growth.cpp'),('wrapper_sha256','run_geometric_fixed_rate_followup.py'),('protocol_sha256','GEOMETRIC_FIXED_RATE_FOLLOWUP_PROTOCOL.md')]:
        assert manifest[key]==identity(RAW/filename)['sha256']
    assert manifest['binary_sha256']=='ffc3e77cf1793b5acb6fdb792563ee13db11ed73a698b2652dbff79300b4f10d'
    cases={tuple(row['case']) for row in summary['results']}
    assert cases==set(declared) and len(summary['results'])==2496
    counts=Counter(r['status'] for r in summary['results'])
    assert dict(counts)==summary['status_counts']=={'full_verified':2496} and summary['all_full_verified']
    per_history=load(ANAL/'PER_HISTORY.json')
    by_case={tuple(r['case']):r for r in per_history}
    assert len(by_case)==len(per_history)==2496 and set(by_case)==cases
    verification_receipts=load(ANAL/'RECEIPT_VERIFICATION.json')
    receipt_bindings={r['name']:r for r in verification_receipts['rows']}
    assert len(receipt_bindings)==2496 and verification_receipts['all_files_in_listed_receipts_hashed']
    assert verification_receipts['wrapper_exception_receipts_not_interpreted']==0
    groups=defaultdict(list);hash_jobs={};receipt_identities=[];endpoint_comparisons=[];executables=set()
    max_table_difference=0.;max_summary_difference=0.
    for rank,row in enumerate(summary['results']):
        N,beta,seed=row['case'];name=f'N{N}_b{beta}_s{seed}';prefix=PROD/name
        assert row['name']==name
        receipt_path=Path(str(prefix)+'.receipt.json');receipt=load(receipt_path);rid=identity(receipt_path);receipt_identities.append(rid)
        assert receipt['case']==row['case'] and receipt['status']==row['status'] and receipt['exit_code']==0 and receipt['verification_error'] is None
        assert receipt_bindings[name]['receipt_sha256']==rid['sha256'] and receipt_bindings[name]['files']==len(receipt['files'])
        cmd=receipt['command'];executables.add(cmd[0])
        assert cmd[1:]==[str(N),str(seed),str(beta),'1','1000000000',str(prefix),'0']
        for filename,digest in receipt['files'].items():
            path=PROD/filename;assert path.parent==PROD and path.name==filename
            assert path not in hash_jobs;hash_jobs[path]=digest
        d=load(Path(str(prefix)+'.json'));v=load(Path(str(prefix)+'.verification.json'))
        assert d['N']==N and d['beta']==beta and d['seed']==seed and d['full'] and d['winding_valid']
        assert d['birth_events']==N**3//2 and d['events']==d['birth_events']+d['slide_events'] and d['events']<=10**9
        assert v['archive']==name+'.state.npz' and v['archive_sha256']==receipt['files'][v['archive']]
        assert v['lossless_arrays_reopened_and_equal'] and v['integer_Gauss_max_abs']==0
        assert v['ASCII_headers']==[f'N {N}','site partner identity births_at_site']
        assert v['ASCII_site_column']==f'integers0..{N**3-1}'
        assert v['shells']==row['shells'] and v['winding_power_per_component']==row['winding_power_per_component']
        assert by_case[N,beta,seed]['name']==name and by_case[N,beta,seed]['winding']==d['winding']==row['winding']
        for key in ['time','events','slide_events','site_reuses','max_site_births']:
            max_summary_difference=max(max_summary_difference,close(d[key],row[key]))
        mode_map={tuple(m['ell']):m for m in v['modes']}
        assert set(mode_map)==expected_modes
        shells={k:[m['transverse_per_polarization'] for ell,m in mode_map.items() if sum(x*x for x in ell)==k] for k in [1,2,3,4]}
        assert [len(shells[k]) for k in [1,2,3,4]]==[3,6,4,3]
        for k in shells:close(math.fsum(shells[k])/len(shells[k]),v['shells'][str(k)])
        W=sum(x*x for x in d['winding'])/(3*N);close(W,v['winding_power_per_component'])
        reconstructed=[v['shells'][str(k)] for k in [1,2,3,4]]+[W,math.fsum(x*x for x in shells[1])/3,
            v['shells']['1']**2,W**2,d['time']/N**3,d['slide_events']/N**3,v['site_reuse_fraction']]
        item=by_case[N,beta,seed];assert set(item['observables'])==set(COLUMNS)
        for key,value in zip(COLUMNS,reconstructed):max_table_difference=max(max_table_difference,close(item['observables'][key],value))
        groups[N,beta].append([item['observables'][key] for key in COLUMNS])
        if name in selected_by_name:
            own=selected_by_name[name]
            assert own['archive']['sha256']==v['archive_sha256'] and own['ASCII_reconstruction_sha256']==v['ASCII_sha256']
            for key in ['orientation_counts','winding','site_reuses','max_site_births']:assert own[key]==d[key],(name,key)
            assert own['birth_budget']==2*d['birth_events']==N**3
            assert own['site_reuse_fraction']==v['site_reuse_fraction'] and own['winding_power_per_component']==W
            raw_modes={tuple(m['ell']):m for m in d['modes']};assert set(raw_modes)==set(mode_map)
            max_cpp=max_fft=0.
            for m in own['modes']:
                ell=tuple(m['ell'])
                for key in ['power','transverse_per_polarization']:
                    diff=abs(m[key]-raw_modes[ell][key]);assert diff<1e-8;max_cpp=max(max_cpp,diff)
                    diff=abs(m[key]-mode_map[ell][key]);assert diff<1e-8;max_fft=max(max_fft,diff)
                assert abs(m['longitudinal']-raw_modes[ell]['longitudinal'])<1e-8
            for key in own['shells']:close(own['shells'][key],v['shells'][key],atol=1e-8,rtol=0)
            endpoint_comparisons.append({'name':name,'all_integer_invariants_and_ASCII_hash_match':True,'max_power_difference_Cpp':max_cpp,'max_power_difference_author_FFT':max_fft})
        if (rank+1)%512==0:print('metadata and per-history derivations checked',rank+1,'of2496',flush=True)
    assert len(endpoint_comparisons)==24 and len(executables)==1
    executable_identity=identity(Path(next(iter(executables))));assert executable_identity['sha256']==manifest['binary_sha256']
    print('streaming hashes for',len(hash_jobs),'listed receipt files',flush=True)
    hashes=[];total_bytes=0
    with (HERE/'RECEIPT_FILE_HASHES.jsonl').open('w') as out,ThreadPoolExecutor(max_workers=4) as pool:
        for index,row in enumerate(pool.map(identity,hash_jobs)):
            assert row['sha256']==hash_jobs[Path(row['path'])],row
            out.write(json.dumps(row)+'\n');hashes.append(row);total_bytes+=row['bytes']
            if (index+1)%3000==0:print('receipt files authenticated',index+1,flush=True)
    for own in selected['rows']:
        assert hash_jobs[Path(own['archive']['path'])]==own['archive']['sha256']
    agg=[]
    for index,cell in enumerate(sorted(groups)):
        N,beta=cell;result=aggregate(groups[cell]);assert result['n']==(64 if N==128 else 256)
        agg.append({'N':N,'beta':beta,'declared_cell_index':index,'bootstrap_seed':2109211530+index,**result})
    save('INDEPENDENT_AGGREGATION.json',{'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'read_boundary':'Full per-history inputs read and aggregated, but analysis RESULTS.json and TABLE.md remain unopened.',
        'method':'math.fsum column means and paired sample-covariance quadratic forms for standard errors; no analyzer imports or bootstrap rerun.',
        'source':identity(ANAL/'PER_HISTORY.json'),'cells':agg})
    save('PRODUCTION_AUTHENTICATION.json',{'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'manifest':identity(PROD/'MANIFEST.json'),'summary':identity(PROD/'SUMMARY.json'),
        'receipt_verification':identity(ANAL/'RECEIPT_VERIFICATION.json'),'per_history':identity(ANAL/'PER_HISTORY.json'),
        'binary':executable_identity,'declared_histories':2496,'status_counts':dict(counts),
        'case_set_seed_and_command_grid_exact':True,'all_receipt_files_hashed':True,'listed_files':len(hashes),'listed_file_bytes':total_bytes,
        'receipt_identities':receipt_identities,'hash_inventory':identity(HERE/'RECEIPT_FILE_HASHES.jsonl'),
        'max_per_history_reconstruction_difference':max_table_difference,'max_summary_difference':max_summary_difference,
        'endpoint_comparisons':endpoint_comparisons,'no_unselected_NPZ_arrays_decoded':True,
        'not_claimed':'Historical generator/RNG replay, independent physical reconstruction of all2496 arrays, statistical coverage or phase conclusions.'})
    print('authenticated2496 histories; compared24 physical endpoints; aggregated12 cells without reading final estimates.',flush=True)

if __name__=='__main__':
    assert not (HERE/'PRODUCTION_AUTHENTICATION.json').exists()
    run()

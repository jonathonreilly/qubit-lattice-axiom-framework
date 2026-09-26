#!/usr/bin/env python3
"""Memory-bounded root adaptation of the previously sealed independent decoder.

The original selection is unchanged. Each selected history is reconstructed
and sealed before its observable JSON or receipt payload is opened. Reusing
the old independent RNG/FFT method is not a fresh independent review.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,struct,datetime,sys
import numpy as np
ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'dimer_routed_dynamic_independent/independent_decode.py'
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('sealed_decoder',SOURCE)
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
CHUNK=65536

def ident(p):
 p=Path(p);h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return dict(path=str(p.resolve()),bytes=p.stat().st_size,sha256=h.hexdigest())

def auth(row):
 r=ident(row['path']);assert r['sha256']==row['sha256'] and r['bytes']==row['bytes'];return r

def xyz(ids,N):return np.column_stack((ids//(N*N),(ids//N)%N,ids%N))
def black(j,N):
 xy=j//(N//2);return 2*j+(xy//N+xy%N)%2

def geometry(row):
 p=Path(row['file']['path']);auth(row['file'])
 with p.open('rb') as f:head=f.read(12)
 assert head[:8]==b'DRPAIR01';N=struct.unpack_from('<I',head,8)[0];V=N**3;K=V//2
 assert N==256 and p.stat().st_size==12+4*V
 partner=np.memmap(p,mode='r',dtype='<u4',offset=12,shape=(V,))
 for start in range(0,V,CHUNK):
  ids=np.arange(start,min(start+CHUNK,V));other=partner[ids]
  assert np.all(other<V) and np.array_equal(partner[other],ids)
  delta=(xyz(other.astype(np.int64),N)-xyz(ids,N))%N
  assert np.all(np.minimum(delta,N-delta).sum(axis=1)==1)
 routes=[]
 for delta in old.DIRECTIONS:
  q=np.empty(K,dtype=np.uint32)
  for start in range(0,K,CHUNK):
   j=np.arange(start,min(start+CHUNK,K));b=black(j,N);target=(xyz(b,N)+delta)%N
   tid=target[:,0]*N*N+target[:,1]*N+target[:,2];owner=partner[tid].astype(np.int64)
   assert np.all(xyz(owner,N).sum(axis=1)%2==0);q[j]=owner//2
  assert np.array_equal(np.sort(q),np.arange(K,dtype=np.uint32))
  inv=np.empty(K,dtype=np.uint32);inv[q]=np.arange(K,dtype=np.uint32);moving=0
  for start in range(0,K,CHUNK):
   j=np.arange(start,min(start+CHUNK,K));j=j[q[j]!=j];moving+=len(j)
   footprints=np.column_stack((inv[j],j,q[j],q[q[j]]))
   assert np.all(np.diff(np.sort(footprints,axis=1),axis=1)>0)
   dest=black(q[j].astype(np.int64),N);d=(xyz(partner[dest].astype(np.int64),N)-xyz(dest,N)+N//2)%N-N//2
   step=delta-d;assert np.all(np.abs(step).sum(axis=1)==2)
   assert np.all((step@delta>=1)&(step@delta<=2))
   assert np.array_equal((xyz(black(j,N),N)+step)%N,xyz(dest,N))
  routes.append(dict(direction=delta.tolist(),moving_channels=moving))
  del q,inv
 assert sum(r['moving_channels'] for r in routes)==5*K
 if row['kind']=='winding':
  for start in range(0,K,CHUNK):
   j=np.arange(start,min(start+CHUNK,K));b=black(j,N)
   assert np.array_equal(xyz(partner[b].astype(np.int64),N),(xyz(b,N)+[1,0,0])%N)
 return dict(N=N,K=K,geometry=ident(p),routes=routes,all_matching_sites_checked=V)

def fields(colors,keys,N):
 K=N**3//2;hist=np.zeros((3,N,14),dtype=np.int64)
 for start in range(0,K,CHUNK):
  j=np.arange(start,min(start+CHUNK,K));coords=xyz(black(j,N),N)
  c=colors[j] if keys is None else colors[keys[j]]
  for axis in range(3):hist[axis]+=np.bincount(coords[:,axis]*14+c,minlength=N*14).reshape(N,14)
 return np.array([np.fft.fft(h@old.FEATURE,axis=0)[1]/np.sqrt(K) for h in hist])

def run(kind,rep):
 selection=ROOT/'DIMER_ROUTED_256_ENDPOINT_CHECK_SELECTION.json';sel=json.loads(selection.read_text());auth(sel['manifest'])
 selected=[r for r in sel['selected_endpoint_histories'] if (r['kind'],r['replicate'])==(kind,rep)];assert len(selected)==1
 jobsel=selected[0];manifest=Path(sel['manifest']['path']);m=json.loads(manifest.read_text())
 job=next(j for j in m['jobs'] if (j['kind'],j['replicate'])==(kind,rep));assert all(job[k]==v for k,v in jobsel.items())
 path=Path(job['output']);receipt=Path(str(path)+'.receipt.json');state=Path(str(path)+'.state')
 assert receipt.exists(),'Selected history not complete; do not substitute another history'
 out=ROOT/'dimer_routed_256_endpoint_checks'/f'{kind}_r{rep:03d}';out.mkdir(parents=True,exist_ok=True)
 assert not (out/'RECONSTRUCTION.json').exists(),'Preserve the prior sealed reconstruction'
 gr=next(g for g in m['geometry'] if g['kind']==kind);g=geometry(gr);N,K=g['N'],g['K']
 with state.open('rb') as f:header=f.read(12)
 assert header[:8]==b'DRSTATE1' and struct.unpack_from('<I',header,8)[0]==N and state.stat().st_size==12+5*K
 keys=np.memmap(state,mode='r',dtype='<u4',offset=12,shape=(K,));colors=np.memmap(state,mode='r',dtype='u1',offset=12+4*K,shape=(K,))
 assert np.array_equal(np.sort(keys),np.arange(K,dtype=np.uint32)) and np.all(colors<14)
 initial,rejected=old.seeded_colors(job['seed'],K);assert np.array_equal(colors,initial)
 counts=np.bincount(initial,minlength=14);finalcounts=np.zeros(14,dtype=np.int64)
 for start in range(0,K,CHUNK):finalcounts+=np.bincount(colors[keys[start:start+CHUNK]],minlength=14)
 assert np.array_equal(counts,finalcounts)
 value=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),job=job,geometry=g,state=ident(state),
  selection=ident(selection),decoder=ident(SOURCE),adapter=ident(Path(__file__)),manifest=ident(manifest),
  boundary='No observable history JSON or receipt payload read before this reconstruction and seal.',
  keys_checked=K,physical_records_checked=2*K,record_identity_reason='All pair keys form a permutation; the full bipartite matching involution puts record 2*key at its black site and 2*key+1 at its white partner, proving distinctness, partner xor 1, and roles for every record.',
  seeded_initial_lookup_equal=True,initial_draw_rejections=rejected,color_counts=counts.tolist(),
  initial_fields=old.as_json_complex(fields(initial,None,N)),final_fields=old.as_json_complex(fields(colors,keys,N)))
 recon=out/'RECONSTRUCTION.json';recon.write_text(json.dumps(value,indent=2)+'\n')
 seal=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),artifacts=[ident(recon),ident(Path(__file__)),ident(SOURCE),ident(selection)])
 (out/'RECONSTRUCTION_SEAL.json').write_text(json.dumps(seal,indent=2)+'\n')
 for r in seal['artifacts']:auth(r)
 rr=json.loads(receipt.read_text());assert rr['status']=='complete_verified_receipt' and rr['returncode']==0 and rr['job']==job
 evidence=[auth(r) for r in rr['outputs']];a=json.loads(path.read_text())
 assert (a['N'],a['seed'],a['mode'])==(N,job['seed'],'production')
 assert a['pairs']==K and a['channels']==5*K and a['color_counts']==value['color_counts']
 assert a['geometry']==gr['file']['path'] and a['minimum_nontrivial_cycle']>=N//2
 assert a['gamma']==1 and a['k0']==1.1 and a['key_permutation_verified'] and a['counts_verified']
 assert 0<=a['color_changes']<=a['accepted']<=a['attempts']
 assert [s['t'] for s in a['snapshots']]==[0,7/16,7/8,21/16,7/4]
 errors=[]
 for i,k in [(0,'initial_fields'),(-1,'final_fields')]:
  stored=np.array(a['snapshots'][i]['fields']);assert stored.shape==(3,6,2)
  diff=np.array(value[k])-stored;err=float(np.max(np.hypot(diff[:,:,0],diff[:,:,1])));assert err<1e-8;errors.append(err)
 assert Path(str(path)+'.stderr').read_bytes()==b''
 result=dict(kind=kind,replicate=rep,N=N,keys_checked=K,physical_records_checked=2*K,
  endpoint_complex_errors=errors,evidence=evidence,receipt=ident(receipt),seal=ident(out/'RECONSTRUCTION_SEAL.json'),
  scope='Root memory-bounded adaptation of previously independently sealed decoder. Selected endpoints only, no aggregate statistics, intermediate snapshots or trajectory-clock replay. No fresh independent review claimed.')
 (out/'COMPARISON.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['evidence','scope']}),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('kind',choices=['winding','irregular']);p.add_argument('replicate',type=int);args=p.parse_args();run(args.kind,args.replicate)

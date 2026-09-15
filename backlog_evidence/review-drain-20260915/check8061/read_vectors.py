from pathlib import Path
import numpy as np,json,gzip,hashlib,io,time
p=Path(__file__).parent/'original-8061/outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs';start=time.monotonic();manifest=json.loads((p/'VECTOR_MANIFEST.json').read_text());by={x['name']:x for x in manifest};rows=[]
def read(name):
 row=by[name];packed=(p/row['compressed']).read_bytes();assert len(packed)==row['gzip_bytes'] and hashlib.sha256(packed).hexdigest()==row['gzip_sha256'];raw=gzip.decompress(packed);assert len(raw)==row['bytes'] and hashlib.sha256(raw).hexdigest()==row['sha256'];return raw
for name in ['firstP','firstO','secondP','secondO','sourceP','sourceO','chi_real']:
 x=np.load(io.BytesIO(read(name+'.npy')),allow_pickle=False);assert x.shape==(2**20,) and x.dtype==np.float64 and np.isfinite(x).all();z=np.frombuffer(read(name+'.bin'),dtype='<u8').reshape(-1,2);bits=x.view(np.uint64);col=0 if name.startswith('first') else 1
 assert np.array_equal(z[:,col],bits) and (z[:,1-col]==0).all()
 rows.append({'name':name,'complete_coordinates':len(x),'raw_phase':'real' if col==0 else'i','bitwise_bridge':True})
r={'status':'PASS','all14_compressed_and_raw_hashes_verified':True,'all7_complete_bit_bridges':rows,'seconds':time.monotonic()-start,'no_H_action_residual_or_solve':True};Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n');print(r)

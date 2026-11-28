#!/usr/bin/env python3
"""Compare nested magnetic matrices through different assembly/storage paths."""
from wilson import *
HERE=Path(__file__).resolve().parent
scratch=Path(sys.argv[1]);small=scratch/'wilson_J4E44';large=scratch/'wilson_J4E48'
a=np.load(small/'rows.npy');b=np.load(large/'rows.npy');kb=keys(b)
@njit
def mapping(rows,ks):
    out=np.empty(len(rows),np.int64)
    for i in range(len(rows)):out[i]=lookup(rows[i],ks)
    return out
indices=mapping(a,kb);assert np.all(indices>=0)
A=load_npz(small/'X.npz')
B=csr_matrix((np.load(large/'X_data.npy',mmap_mode='r'),np.load(large/'X_indices.npy',mmap_mode='r'),np.load(large/'X_indptr.npy',mmap_mode='r')),shape=(len(b),len(b)),copy=False)
worst=0.;checked=0
for start in range(0,len(a),4000):
    stop=min(len(a),start+4000)
    delta=A[start:stop]-B[indices[start:stop]][:,indices]
    if delta.nnz:worst=max(worst,float(np.max(np.abs(delta.data))))
    checked+=stop-start;base.memory_check()
assert worst<2e-12,worst
record={'grade':'GUIDE control','rows_checked':checked,'max_matrix_difference':worst,'peak_RSS_bytes':base.memory_check()}
(HERE/'nested_control.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)

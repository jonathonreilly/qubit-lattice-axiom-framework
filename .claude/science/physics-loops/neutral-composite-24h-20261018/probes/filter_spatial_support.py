from pathlib import Path
import itertools,json,numpy as np
R=Path(__file__).resolve().parents[5];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);M=np.array(d['mass_matrix']['real'])+1j*np.array(d['mass_matrix']['imag'])
def bands(k):return np.linalg.eigh(np.einsum('ks,sij->kij',np.exp(1j*k@sh.T),bl))
rows=[]
for N in [12,24,36]:
 xyz=np.array(list(itertools.product(range(N),repeat=3)));k=2*np.pi/N*(xyz+.5);e,U=bands(k);eo,Uo=bands(k+np.pi);V=Uo.conj().transpose(0,2,1)@M@U;de=eo[:,:,None]-e[:,None,:]
 r=np.minimum(xyz,N-xyz);r2=(r*r).sum(axis=1);boundary=(r.max(axis=1)>=N//2-1)
 for tau in [0,4,8,16,32,64]:
  F=np.exp(-.5*(tau*(de-.2))**2);Mk=Uo@(F*V)@U.conj().transpose(0,2,1)
  mr=np.fft.ifftn(Mk.reshape(N,N,N,12,12),axes=(0,1,2)).reshape(N**3,12,12)
  w=(abs(mr)**2).sum(axis=(1,2));norm=w.sum();p=w/norm
  row={'N':N,'tau':tau,'operator_HS_norm_per_cell':float(norm),'relative_support_rms_coarse_cells':float(np.sqrt(np.dot(p,r2))),'periodic_boundary_weight':float(p[boundary].sum()),'same_cell_weight':float(p[r2==0].sum())};rows.append(row);print(row,flush=True)
Path(__file__).with_name('filter_spatial_support.json').write_text(json.dumps({'scope':'Relative-separation support of filtered bilinear, not its center-of-mass envelope or a bound fermion size. Hilbert-Schmidt operator norm differs from ensemble response norm. Minimum-image radii need boundary control.','rows':rows},indent=2)+'\n')

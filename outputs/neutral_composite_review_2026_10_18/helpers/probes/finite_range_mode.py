"""Source-accessible finite-range neutral operators from exact Fourier convolution."""
from pathlib import Path
import itertools,json,numpy as np
from scipy.sparse.linalg import LinearOperator,cg
R=Path(__file__).resolve().parents[4];d=json.loads((R/'data/collective_corner_response/candidate.json').read_text());sh=np.array(d['shifts']);bl=np.array(d['blocks']['real'])+1j*np.array(d['blocks']['imag']);M0=np.array(d['mass_matrix']['real'])+1j*np.array(d['mass_matrix']['imag']);rows=[];saved={}
def ball(r):return [x for x in itertools.product(range(-r,r+1),repeat=3) if sum(map(abs,x))<=r]
q=np.ones(3)*np.pi;omega=.2
for radius in [0,1,2,3]:
 coords=ball(radius);outcoords=ball(radius+1);oi={x:i for i,x in enumerate(outcoords)};origin=coords.index((0,0,0));embed=np.array([oi[x] for x in coords]);maps=[np.array([oi[tuple(np.array(x)+s)] for x in coords]) for s in sh];ns=len(coords)
 def act(x):
  X=x.reshape(ns,12,12);Y=np.zeros((len(outcoords),12,12),complex)
  for s,b,ix in zip(sh,bl,maps):Y[ix]+=np.exp(1j*q@s)*(b@X)-X@b
  Y[embed]-=omega*X
  return Y.ravel()
 def adj(y):
  Y=y.reshape(len(outcoords),12,12);X=np.zeros((ns,12,12),complex)
  for s,b,ix in zip(sh,bl,maps):X+=np.exp(-1j*q@s)*(b.conj().T@Y[ix])-Y[ix]@b.conj().T
  X-=omega*Y[embed]
  return X.ravel()
 rng=np.random.default_rng(7);x=rng.normal(size=ns*144)+1j*rng.normal(size=ns*144);y=rng.normal(size=len(outcoords)*144)+1j*rng.normal(size=len(outcoords)*144)
 adjerr=abs(np.vdot(y,act(x))-np.vdot(adj(y),x));assert adjerr<1e-9
 source=np.zeros((ns,12,12),complex);source[origin]=M0/np.linalg.norm(M0);source=source.ravel()
 for eta in [.1,.01,.001]:
  op=LinearOperator((len(source),len(source)),matvec=lambda x:adj(act(x))+eta*x,dtype=complex)
  sol,info=cg(op,source,rtol=1e-9,maxiter=3000);assert info==0,info
  normalerr=np.linalg.norm(op@sol-source);assert normalerr<2e-9
  v=sol/np.linalg.norm(sol);res=np.linalg.norm(act(v));overlap=abs(np.vdot(source,v))**2
  coeff=v.reshape(ns,12,12);weights=(abs(coeff)**2).sum(axis=(1,2));rms=np.sqrt(np.dot(weights,np.sum(np.array(coords)**2,axis=1)))
  lv=act(v).reshape(len(outcoords),12,12);lv[embed]+=omega*coeff
  mean=np.vdot(coeff,lv[embed]).real;width=np.sqrt(max(0,np.linalg.norm(lv)**2-mean**2))
  row={'range_L1':radius,'coefficient_count':ns*144,'eta':eta,'omega_target':omega,'normalized_HS_residual':float(res),'normalized_HS_source_overlap_squared':float(overlap),'HS_mean_frequency':float(mean),'HS_frequency_std':float(width),'relative_support_rms':float(rms),'adjoint_error':float(adjerr),'normal_solve_error':float(normalerr)};rows.append(row);print(row,flush=True)
  saved[f'r{radius}_eta{eta}']=coeff;saved[f'coords{radius}']=np.array(coords)
Path(__file__).with_name('finite_range_mode.json').write_text(json.dumps({'scope':'Finite-range bilinear operator optimization, Hilbert-Schmidt norm, fixed supplied Hamiltonian; chosen center and source; not canonical scalar coupling or thermal spectral norm','q':q.tolist(),'rows':rows},indent=2)+'\n')
np.savez_compressed(Path(__file__).with_name('finite_range_modes.npz'),**saved)

import numpy as np,json,itertools
from scipy.special import expit
from pathlib import Path
p=Path(__file__).resolve().parents[2]
d=json.loads((p/'data/collective_corner_response/candidate.json').read_text())
get=lambda x:np.asarray(x['real'])+1j*np.asarray(x['imag'])
blocks=get(d['blocks']);sh=np.array(d['shifts']);M=get(d['mass_matrix']);mu=d['chemical_potential_development_value'];N=4;T=.03
H=lambda k:sum(block*np.exp(1j*np.dot(shift,k)) for shift,block in zip(sh,blocks))
# Exactly one representative per Q-pair: first momentum index0 or1.
ks=[2*np.pi*np.array(i)/N for i in itertools.product(range(2),range(N),range(N))]
pairs=[(H(k),H(k+np.pi)) for k in ks]
V=np.block([[np.zeros((12,12)),M],[M,np.zeros((12,12))]])
Hs=[np.block([[a,np.zeros((12,12))],[np.zeros((12,12)),b]]) for a,b in pairs]
def Om(x):
    E=np.linalg.eigvalsh(np.array(Hs)+x*V)
    return -T*np.logaddexp(0,(mu-E)/T).sum()/N**3
f0=Om(0);fd={}
for ep in [1e-3,3e-4,1e-4]:
    fd[str(ep)]=(Om(2*ep)-16*Om(ep)+30*f0-16*Om(-ep)+Om(-2*ep))/(12*ep**2)
# Spectral divided differences on24-dimensional folded cells: diagonal and repeated blocks explicit.
chi=chi_deg=0.
for A in Hs:
    e,U=np.linalg.eigh(A);v=U.conj().T@V@U
    for i in range(24):
      for j in range(24):
        if abs(e[i]-e[j])<1e-10:
          f=expit((mu-e[i])/T);term=f*(1-f)/T*abs(v[i,j])**2
          chi_deg+=term
        else:term=-(expit((mu-e[i])/T)-expit((mu-e[j])/T))/(e[i]-e[j])*abs(v[i,j])**2
        chi+=term
chi/=N**3;chi_deg/=N**3
E,U=np.linalg.eigh(H(np.pi/2*np.array([1,-1,1])));Eq,Uq=np.linalg.eigh(H(np.pi/2*np.array([1,-1,1])+np.pi))
sel=abs(E-mu)<1e-8;selq=abs(Eq-mu)<1e-8
vertex=Uq[:,selq].conj().T@M@U[:,sel]
sv=np.linalg.svd(vertex,compute_uv=False)
node=np.sum(sv**2)/(2*T*N**3)
source=json.loads((p/'outputs/collective_corner_response/result.json').read_text())
checks={'fd5point':max(abs(x-chi) for x in fd.values())<3e-6,'author_Kubo':abs(chi-source['response_rows'][1]['isothermal'])<1e-10,'author_degenerate':abs(chi_deg-source['response_rows'][1]['degenerate'])<1e-10,'four_node_states':sel.sum()==selq.sum()==2,'equal_singular_values':np.ptp(sv)<1e-10,'author_node':abs(node-source['node_curie_at_L4_T003'])<1e-10,'node_not_all_degenerate':chi_deg>node+1e-4,'static_threshold_index':source['response_rows'][16]['N']==12 and source['response_rows'][16]['shift']==.5 and source['response_rows'][16]['T']==.03}
out={'checks':{k:bool(v) for k,v in checks.items()},'chi':chi,'degenerate':chi_deg,'node':node,'singular_values':sv.tolist(),'fd5point':fd}
(p/'outputs/collective_corner_response/independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));assert all(checks.values())

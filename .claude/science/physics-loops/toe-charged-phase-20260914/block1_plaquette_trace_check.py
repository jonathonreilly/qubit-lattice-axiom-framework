"""Four-cycle with a magnetic term, full CAR sectors and positive histories."""
from pathlib import Path
import itertools,json
import numpy as np
from scipy.linalg import expm
N=3;V=4;omega=np.exp(2j*np.pi/N);beta=.41;tel=.36;mag=.73;hop=.38+.12j
D=np.zeros((V,V),int)
for l in range(V):D[l,l]=1;D[(l+1)%V,l]=-1

def charges(f):return np.array([((f>>i)&1)-((f>>(i+V))&1) for i in range(V)])

def fermi_hop(f,i,j):
    if not (f>>j)&1:return None
    f1=f^(1<<j);sg=(-1)**((f&((1<<j)-1)).bit_count())
    if (f1>>i)&1:return None
    return f1|(1<<i),sg*(-1)**((f1&((1<<i)-1)).bit_count())

basis=[]
for f in range(2**(2*V)):
    Q=charges(f)
    if sum(Q)%N:continue
    base=np.r_[np.cumsum(Q)[:3],0]
    for n in range(N):basis.append((f,tuple((base+n)%N)))
lookup={v:i for i,v in enumerate(basis)};dim=len(basis);He=np.zeros((dim,dim),complex);Hbm=np.zeros_like(He)
for i,(f,e) in enumerate(basis):
    He[i,i]=tel*sum(2-2*np.cos(2*np.pi*np.array(e)/N))
    Hbm[i,i]+=mag
    for sg in [-1,1]:Hbm[lookup[(f,tuple((np.array(e)+sg)%N))],i]-=mag/2
    for l in range(V):
        x=l;y=(l+1)%V
        for species,charge in [(0,1),(1,-1)]:
            z=hop if species==0 else hop.conjugate()
            for src,dst,amp,de in [(y,x,z,charge),(x,y,z.conjugate(),-charge)]:
                step=fermi_hop(f,dst+species*V,src+species*V)
                if step:
                    f2,sign=step;ee=list(e);ee[l]=(ee[l]+de)%N
                    Hbm[lookup[(f2,tuple(ee))],i]+=sign*amp
assert np.linalg.norm(Hbm-Hbm.conj().T)<1e-12
qs=list(itertools.product(range(N),repeat=V));qindex={v:i for i,v in enumerate(qs)};h=[];vb=[]
for q in qs:
    m=np.zeros((V,V),complex)
    for l in range(V):
        x=l;y=(l+1)%V;m[x,y]=hop*omega**q[l];m[y,x]=m[x,y].conjugate()
    h.append(m);vb.append(mag*(1-np.cos(2*np.pi*sum(q)/N)))
X=np.roll(np.eye(N),1,axis=0);out=[]
for M in [1,2]:
    dt=beta/M;K=expm(-dt*tel*(2*np.eye(N)-X-X.T));A=[expm(-dt*x) for x in h];weights=np.exp(-dt*np.array(vb))
    direct=np.trace(np.linalg.matrix_power(expm(-dt*He)@expm(-dt*Hbm),M))
    total=0
    for s in itertools.product(range(N),repeat=V):
        R=np.diag(omega**np.array(s));shift=D.T@np.array(s)
        for hol in range(N):
            q0=(0,0,0,hol);i0=qindex[q0];end=(np.array(q0)-shift)%N
            for q1 in (qs if M==2 else [q0]):
                i1=qindex[q1]
                scalar=np.prod([K[end[l],q1[l]] for l in range(V)])*weights[i0]
                B=A[i0]
                if M==2:
                    scalar*=np.prod([K[q1[l],q0[l]] for l in range(V)])*weights[i1]
                    B=A[i1]@B
                total+=scalar*abs(np.linalg.det(np.eye(V)+R@B))**2/N
    assert abs(direct-total)<2e-10*abs(direct)
    out.append({'M':M,'flux_CAR_trace':direct.real,'positive_history_trace':total,'relative_difference':abs(direct-total)/abs(direct)})
    if M==1:
        brute=0
        for s in itertools.product(range(N),repeat=V):
            R=np.diag(omega**np.array(s));shift=D.T@np.array(s)
            for q in qs:
                idx=qindex[q];end=(np.array(q)-shift)%N
                scalar=np.prod([K[end[l],q[l]] for l in range(V)])*weights[idx]
                brute+=scalar*abs(np.linalg.det(np.eye(V)+R@A[idx]))**2/N**V
        assert abs(brute-total)<2e-10*abs(total)
        out[-1]['unfixed_full_history_sum']=brute
Path(__file__).with_name('BLOCK1_PLAQUETTE_TRACE_CHECK.json').write_text(json.dumps({'N':N,'physical_dimension':dim,'beta':beta,'magnetic_coupling':mag,'cases':out},indent=2)+'\n')
print('physical dimension',dim)
for x in out:print(x)

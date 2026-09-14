import itertools,json
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix
from scipy.linalg import null_space

def fermions(q):
    dim=1<<q;ops=[]
    for a in range(q):
        rows=[];cols=[];data=[]
        for n in range(dim):
            if n>>a&1:
                rows.append(n^(1<<a));cols.append(n)
                data.append((-1)**((n&((1<<a)-1)).bit_count()))
        ops.append(coo_matrix((data,(rows,cols)),shape=(dim,dim),dtype=float).tocsr())
    return ops

def atomic_checks():
    rows=[]
    for q in (4,6,8):
        cs=fermions(q);D=1.7;dim=1<<q;s=np.zeros(dim);s[0]=s[-1]=1/np.sqrt(2)
        H=D*(np.eye(dim)-np.outer(s,s));I=np.eye(dim)
        a=cs[0].toarray();b=(H@a-a@H)/D
        ds=[a,b]
        for z in (.2+.7j,1.3+.4j):
            rm=np.linalg.inv(z*I-H);rp=np.linalg.inv(z*I+H)
            G=np.array([[s@A@rm@B.T@s+s@B.T@rp@A@s for B in ds] for A in ds])
            pred=(z*np.eye(2)-D*np.array([[0,1],[1,0]]))/(z*z-D*D)
            assert np.max(abs(G-pred))<2e-14
            assert np.max(abs(G@ (z*np.eye(2)+D*np.array([[0,1],[1,0]]))-np.eye(2)))<2e-14
        assert np.linalg.norm(b@b.T+b.T@b-I)>1
        n0=a.T@a;n1=cs[1].T@cs[1]
        assert abs(s@n0@n1@s-.5)<1e-14
        assert abs((s@n0@s)*(s@n1@s)-.25)<1e-14
        a2=cs[1].toarray();pair=a2@a@s
        assert abs(pair@pair-.5)<1e-14 and np.linalg.norm(H@pair-D*pair)<1e-14
        rows.append({'q':q,'gap':D,'one_and_two_particle_energy':D,'composite_not_independent_CAR':True})
    return rows

X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);pauli=[X,Y,Z]
def slab(L,k,offset=0.):
    b=offset+sum(1-np.cos(k));s=sum(np.sin(k[a])*pauli[a] for a in range(3))
    B=b*np.eye(L)-np.eye(L,k=-1)
    H=np.block([[np.kron(np.eye(L),s),np.kron(B,np.eye(2))],[np.kron(B.T,np.eye(2)),-np.kron(np.eye(L),s)]])
    return H,B,s,b

def slab_checks():
    rows=[]
    for L in (2,3,5,9):
        for k in [np.array(x)*np.pi for x in itertools.product((0,1),repeat=3)]+[np.array([.2,.7,-1.1]),np.array([1.2,2.1,.4])]:
            H,B,s,b=slab(L,k);keep=list(range(4*L-2));hp=H[np.ix_(keep,keep)];v=b**np.arange(L,dtype=float);v/=np.linalg.norm(v)
            V=np.zeros((4*L-2,2),complex);V[:2*L]=np.kron(v[:,None],np.eye(2))
            assert np.max(abs(hp@V-V@s))<1e-13
            lam=1+b*b-2*b*np.cos(np.arange(1,L)*np.pi/L)
            sn=np.linalg.norm(np.sin(k));expected=[-sn,sn]
            for l in lam:expected.extend([-np.sqrt(sn*sn+l)]*2+[np.sqrt(sn*sn+l)]*2)
            assert np.max(abs(np.linalg.eigvalsh(hp)-np.sort(expected)))<3e-13
            assert min(lam)>=np.sin(np.pi/L)**2-1e-14
            if sn<1e-14:
                r=round(b/2);zeros=sum(abs(np.linalg.eigvalsh(hp))<1e-11);assert zeros==2
                vel=[]
                for axis in range(3):
                    dh=np.zeros_like(hp)
                    dh[:2*L,:2*L]=np.kron(np.eye(L),np.cos(k[axis])*pauli[axis])
                    dh[2*L:,2*L:]=-np.kron(np.eye(L-1),np.cos(k[axis])*pauli[axis])
                    vel.append(V.conj().T@dh@V)
                sig=(np.trace(vel[0]@vel[1]@vel[2])/(2j)).real
                assert abs(sig-(-1)**r)<1e-13
                orig_zeros=sum(abs(np.linalg.eigvalsh(H))<1e-11);assert orig_zeros==(4 if r==0 else 0)
                short=slab(L-1,k)[0];fullkeep=[i for i in range(4*L) if i not in (2*L-2,2*L-1,4*L-2,4*L-1)]
                assert np.max(abs(H[np.ix_(fullkeep,fullkeep)]-short))<1e-14
                rows.append({'L':L,'corner_pi_count':r,'projected_zero_modes':int(zeros),'chirality':int(round(sig)),'target_end_weight':float(v[0]**2),'mirror_end_weight':float(v[-1]**2)})
        h=slab(L,np.zeros(3),offset=.3)[0];assert min(abs(np.linalg.eigvalsh(h)))>0
    return rows

def gaussian_dilation_checks():
    rows=[]
    for L in (2,4,7):
        for gap in (.5,2.,10.):
            for r in range(4):
                k=np.array([np.pi]*r+[0.]*(3-r));H,B,s,b=slab(L,k)
                h=np.zeros((4*L+2,4*L+2),complex);h[:4*L,:4*L]=H
                h[4*L-2:4*L,4*L:]=gap*np.eye(2);h[4*L:,4*L-2:4*L]=gap*np.eye(2)
                v=np.r_[b**np.arange(L),-b**L/gap];v=v/np.linalg.norm(v)
                W=np.zeros((4*L+2,2),complex);W[:2*L]=np.kron(v[:-1,None],np.eye(2));W[4*L:]=v[-1]*np.eye(2)
                assert np.max(abs(h@W))<1e-11
                assert sum(abs(np.linalg.eigvalsh(h))<1e-10)==2
                S=sum(b**(2*j) for j in range(L));speed=S/(S+b**(2*L)/gap**2)
                for a in range(3):
                    dh=np.zeros_like(h);dh[:2*L,:2*L]=np.kron(np.eye(L),np.cos(k[a])*pauli[a]);dh[2*L:4*L,2*L:4*L]=-np.kron(np.eye(L),np.cos(k[a])*pauli[a]);actual=W.conj().T@dh@W
                    assert np.max(abs(actual-speed*np.cos(k[a])*pauli[a]))<1e-13
                rows.append({'L':L,'gap':gap,'corner_pi_count':r,'speed':speed,'chirality':(-1)**r})
    return rows

def embedding(q,nb):
    P=np.zeros((1<<(q+nb),1<<nb))
    for n in range(1<<nb):P[n<<q,n]=P[(n<<q)+(1<<q)-1,n]=1/np.sqrt(2)
    return P

def fourth_order_checks():
    q=6;c=fermions(2*q);P=embedding(q,q);V=sum((c[a].T@c[q+a]+c[q+a].T@c[a]) for a in range(q))
    V2=V@(V@P);A=P.T@V2;D4=P.T@(V@(V@V2));n=np.array([x.bit_count() for x in range(1<<q)])
    assert np.max(abs(A-q/2*np.eye(1<<q)))<1e-13
    expected=3*(n-q/2)**2+3*q*q/4-q
    assert np.max(abs(D4-np.diag(expected)))<1e-12
    H4=2*A@A-D4;pred=q-q*q/4-3*(n-q/2)**2
    assert np.max(abs(H4-np.diag(pred)))<1e-12
    return {'q':q,'second_order_scalar':q/2,'fourth_order_values_by_number':[float(pred[n==j][0]) for j in range(q+1)],'operator_identity_error':float(np.max(abs(H4-np.diag(pred))))}

def feshbach_checks():
    q=4;nb=2;c=fermions(q+nb);P=embedding(q,nb);Q=null_space(P.T);H0=np.eye(len(P))-P@P.T
    V=(.2*(c[q].T@c[q+1]+c[q+1].T@c[q])+.3*(c[0].T@c[q]+c[q].T@c[0])+.4*(c[1].T@c[q+1]+c[q+1].T@c[1])).toarray()
    v=np.linalg.norm(V,2);A=P.T@V@P;rows=[]
    for U in (3.,7.,15.):
        assert U>2*v;H=U*H0+V;es=np.linalg.eigvalsh(H);low=es[:1<<nb];assert es[1<<nb]>=U-v-1e-13
        error=[]
        for e in low:
            F=A-P.T@V@Q@np.linalg.solve(Q.T@H@Q-e*np.eye(Q.shape[1]),Q.T@V@P)
            err=np.linalg.norm(F-A,2);assert err<=v*v/(U-2*v)
            assert min(abs(np.linalg.eigvalsh(F)-e))<1e-12
            error.append(err)
        rows.append({'U':U,'V_norm':v,'bound':v*v/(U-2*v),'largest_Feshbach_error':max(error),'low_spectrum':low.tolist()})
    return rows

if __name__=='__main__':
    result={'atomic':atomic_checks(),'slab':slab_checks(),'quadratic_dilation':gaussian_dilation_checks(),'fourth_order':fourth_order_checks(),'Feshbach':feshbach_checks()}
    print(json.dumps(result,indent=2))

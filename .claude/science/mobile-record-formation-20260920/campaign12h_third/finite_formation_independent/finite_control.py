"""Independent complete-sector and effective-Lindbladian checks; no author imports."""
from pathlib import Path
import itertools,json,sys
import sympy as s
import numpy as np
from scipy.sparse import csr_matrix,eye,kron
from scipy.sparse.linalg import expm_multiply

HERE=Path(__file__).resolve().parent
I=s.I

def model(n,A,edges,S=1):
    C=S*(S+1); states=[]
    for E in itertools.product(range(-S,S+1),repeat=len(edges)):
        q=[int(x in A) for x in range(n)]
        for e,(x,y) in enumerate(edges):q[x]+=E[e];q[y]-=E[e]
        if all(abs(z)<=1 for z in q):states.append((tuple(E),tuple(q)))
    index={z:i for i,z in enumerate(states)};dim=len(states)
    T=s.zeros(dim);Js=[s.zeros(dim) for _ in range(2*len(edges))]
    def image(E,q,e,step,newq):
        ee=list(E);ee[e]+=step
        if abs(ee[e])>S:return None
        a=s.sqrt(1-s.Rational(E[e]*(E[e]+step),C))
        return index[(tuple(ee),tuple(newq))],a
    for col,(E,q) in enumerate(states):
        for e,(x,y) in enumerate(edges):
            for source,dest,direction in ((x,y,1),(y,x,-1)):
                if q[source] and not q[dest]:
                    c=q[source];newq=list(q);newq[source]=0;newq[dest]=c
                    out=image(E,q,e,-direction*c,newq)
                    if out is not None:T[out[0],col]-=out[1]
            if q[x]==q[y]==0:
                for ci,c in enumerate((1,-1)):
                    newq=list(q);newq[x]=c;newq[y]=-c
                    out=image(E,q,e,c,newq)
                    if out is not None:Js[2*e+ci][out[0],col]=out[1]
    assert T==T.H
    Ws=[sum(q[a]==0 for a in A) for E,q in states]
    Ns=[sum(bool(z) for z in q) for E,q in states]
    W=s.diag(*Ws);Gamma=sum((J.H*J for J in Js),s.zeros(dim))
    coh=[Js[2*e]+Js[2*e+1] for e in range(len(edges))]
    assert sum((J.H*J for J in coh),s.zeros(dim))==Gamma
    assert all(W*J-J*W==-J for J in Js)
    assert all(T[i,j]==0 or abs(Ws[i]-Ws[j])==1 for i in range(dim) for j in range(dim))
    for col,(E,q) in enumerate(states):
        expected=sum(2*(1-s.Rational(E[e]**2,C)) for e,(x,y) in enumerate(edges) if q[x]==q[y]==0)
        assert Gamma[col,col]==expected
    return {'states':states,'T':T,'Js':Js,'coherent':coh,'W':W,'Ws':Ws,'Ns':Ns,'Gamma':Gamma}

def effective(m,delta=s.Integer(1),kappa=s.Integer(1),coherent=False):
    dim=len(m['states']);ids=[i for i,w in enumerate(m['Ws']) if w==0]
    P=s.zeros(dim,len(ids))
    for col,row in enumerate(ids):P[row,col]=1
    G=kappa*m['Gamma'];V=delta*m['T']
    R1=s.diag(*[(delta-I*G[i,i]/2)**-1 if w==1 else 0 for i,w in enumerate(m['Ws'])])
    R2=s.diag(*[(2*delta-I*G[i,i]/2)**-1 if w==2 else 0 for i,w in enumerate(m['Ws'])])
    X=-R1*V*P;Z=-R2*V*X
    z0=P.H*V*X;H=(z0+z0.H)/2
    jumps=[s.sqrt(kappa)*P.H*J*X for J in m['coherent' if coherent else 'Js']]
    Ge=sum((J.H*J for J in jumps),s.zeros(len(ids)))
    assert s.simplify(z0-z0.H+I*Ge)==s.zeros(len(ids))
    return P,X,Z,s.simplify(H),[s.simplify(J) for J in jumps]

def generator(H,Js,rho):
    ans=-I*(H*rho-rho*H)
    for J in Js:
        G=J.H*J;ans+=J*rho*J.H-(G*rho+rho*G)/2
    return ans

def exact_intertwiner(m):
    delta=s.Integer(2);kappa=s.Integer(3);dim=len(m['states'])
    report={}
    for coh in (False,True):
        P,X,Z,He,Je=effective(m,delta,kappa,coh);r=P.cols
        J0=[s.sqrt(kappa)*J for J in m['coherent' if coh else 'Js']]
        def L0(a):return generator(delta*m['W'],J0,a)
        def L1(a):return -I*delta*(m['T']*a-a*m['T'])
        def S0(a):return P*a*P.H
        def S1(a):return X*a*P.H+P*a*X.H
        def S2(a):
            G=X.H*X
            return X*a*X.H+Z*a*P.H+P*a*Z.H-P*(G*a+a*G)*P.H/2
        for i in range(r):
            for j in range(r):
                a=s.zeros(r);a[i,j]=1
                assert s.simplify(L0(S1(a))+L1(S0(a)))==s.zeros(dim)
                assert s.simplify(L0(S2(a))+L1(S1(a))-S0(generator(He,Je,a)))==s.zeros(dim)
                assert s.simplify(s.trace(S1(a)))==0
                assert s.simplify(s.trace(S2(a)))==0
        report['coherent' if coh else 'resolved']={'matrix_units':r*r,'Q2_correction_nonzero':bool(Z!=s.zeros(*Z.shape)),'X_norm_squared_trace':str(s.simplify(s.trace(X.H*X)))}
    return report

def star_report(leaves):
    m=model(leaves+1,{0},[(0,j) for j in range(1,leaves+1)])
    ids=[i for i,w in enumerate(m['Ws']) if w==0];n3=[i for i in ids if m['Ns'][i]==3]
    q1=[i for i,w in enumerate(m['Ws']) if w==1 and m['Ns'][i]==3]
    A=m['T'].extract(q1,n3);null=A.nullspace()
    if null:
        K=s.Matrix.hstack(*null);D=s.simplify(K*(K.H*K).inv()*K.H)
    else:D=s.zeros(len(n3))
    init=m['states'].index(((0,)*leaves,(1,)+(0,)*leaves))
    out={'dimension':len(m['states']),'P_dimension':len(ids),'N3_P_dimension':len(n3),'N3_Q_dimension':len(q1),'N3_hop_rank':A.rank(),'exact_P_N3_dark_dimension':len(null),'instruments':{}}
    for coh in (False,True):
        P,X,Z,H,Js=effective(m,coherent=coh);v=s.zeros(len(ids),1);v[ids.index(init)]=1
        first=sum((J*v*v.H*J.H for J in Js),s.zeros(len(ids)))
        rate=s.simplify(s.trace(first));first/=rate
        pos=[ids.index(i) for i in n3];rho1=first.extract(pos,pos)
        dark=s.simplify(s.trace(D*rho1))
        totalP=s.simplify(s.trace(rho1))
        assert totalP==1
        trapped=dark if leaves+1>3 else s.Integer(0)
        out['instruments']['coherent' if coh else 'resolved']={'first_rate_delta_kappa_1':str(rate),'first_event_exact_dark_probability':str(dark),'nonfull_trapped_probability':str(trapped),'eventual_full_probability':str(1-trapped),'first_state_purity':str(s.simplify(s.trace(rho1*rho1))),'nonzero_first_entries':int(sum(x!=0 for x in rho1))}
        # Every reported dark vector is also exactly annihilated by the full T.
        for w in null:
            full=s.zeros(len(m['states']),1)
            for i,z in zip(n3,w):full[i]=z
            assert m['T']*full==s.zeros(len(m['states']),1)
            assert m['W']*full==s.zeros(len(m['states']),1)
            assert all(J*full==s.zeros(len(m['states']),1) for J in m['Js'])
    return out

def npmat(a):return np.array(a.evalf(),dtype=complex)
def superop(H,Js):
    H=csr_matrix(H);d=H.shape[0];one=eye(d,dtype=complex,format='csr')
    out=-1j*(kron(one,H)-kron(H.T,one))
    for J in Js:
        J=csr_matrix(J);G=J.getH()@J
        out+=kron(J.conjugate(),J)-(kron(one,G)+kron(G.T,one))/2
    return out.tocsr()

def convergence(m):
    T=npmat(m['T']);W=npmat(m['W']);dim=len(T)
    init=m['states'].index(((0,0,0),(1,0,1,0)))
    rho=np.zeros((dim,dim),complex);rho[init,init]=1;time=.7;out={}
    for coh in (False,True):
        P,X,Z,H,Js=effective(m,coherent=coh);P=npmat(P)
        r=P.T@rho@P;Le=superop(npmat(H),[npmat(J) for J in Js])
        eff=expm_multiply(time*Le,r.reshape(-1,order='F')).reshape(r.shape,order='F')
        target=P@eff@P.T;rows=[]
        for eps in (.2,.1,.05):
            L=superop(W/eps**2+T/eps,[npmat(J)/eps for J in m['coherent' if coh else 'Js']])
            evolved=expm_multiply(time*L,rho.reshape(-1,order='F')).reshape(rho.shape,order='F')
            error=float(np.linalg.eigvalsh((evolved-target+evolved.conj().T-target.conj().T)/2).__abs__().sum())
            rows.append({'epsilon':eps,'trace_error':error,'error_over_epsilon':error/eps,'trace_defect':float(abs(np.trace(evolved)-1)),'minimum_eigenvalue':float(np.linalg.eigvalsh((evolved+evolved.conj().T)/2).min())})
        out['coherent' if coh else 'resolved']={'time':time,'rows':rows}
    return out

def main():
    path=model(4,{0,2},[(0,1),(2,1),(2,3)])
    print('exact path matrix-unit intertwiner',flush=True)
    inter=exact_intertwiner(path)
    print('two-leaf star',flush=True);star2=star_report(2)
    print('four-leaf star',flush=True);star4=star_report(4)
    print('finite-epsilon full Liouvillian',flush=True);conv=convergence(path)
    path2=model(4,{0,2},[(0,1),(2,1),(2,3)],S=2)
    fast_dark=[{'E':E,'q':q,'W':w} for (E,q),w,g in zip(path['states'],path['Ws'],list(path['Gamma'].diagonal())) if w>0 and g==0]
    data={'method':'independent electric-bit enumeration of complete finite tree Gauss sectors; exact SymPy identities and separately assembled SciPy Liouvillian','python':sys.version,'sympy':s.__version__,'numpy':np.__version__,'path_S1':{'dimension':len(path['states']),'W_multiplicities':{str(w):path['Ws'].count(w) for w in set(path['Ws'])},'fast_lossless_excited_basis_states':fast_dark,'intertwiner':inter},'path_S2_dimension':len(path2['states']),'star2':star2,'star4':star4,'convergence':conv}
    (HERE/'FINITE_CONTROL_RESULTS.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':main()

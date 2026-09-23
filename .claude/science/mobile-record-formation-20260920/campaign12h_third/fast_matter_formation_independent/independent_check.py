"""Source-informed decisive controls; only this agent's earlier builder is imported."""
from pathlib import Path
import sys,json,hashlib,math
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
OWN=BASE/'finite_formation_independent'/'finite_control.py'
assert hashlib.sha256(OWN.read_bytes()).hexdigest()=='abb86e2fec6d9202471dc1cd3a0a1cc27a4758202b42550d3231ededc8c728d1'
sys.path.insert(0,str(OWN.parent))
from finite_control import model,npmat,superop
import sympy as s
import numpy as np
from scipy.linalg import eigh,polar
from scipy.sparse import diags

models={'path':model(4,{0,2},[(0,1),(2,1),(2,3)]),
        'cycle_S1':model(4,{0,2},[(0,1),(1,2),(2,3),(3,0)]),
        'cycle_S2':model(4,{0,2},[(0,1),(1,2),(2,3),(3,0)],2)}

def coefficients(m):
    p=[i for i,w in enumerate(m['Ws']) if not w]
    q1=[i for i,w in enumerate(m['Ws']) if w==1]
    q2=[i for i,w in enumerate(m['Ws']) if w==2]
    A=m['T'].extract(q1,p);Z=m['T'].extract(q2,q1)*A;M=A.H*A
    return p,-M,M*M-Z.H*Z/2

def canonical_by_cluster_svd(W,T,eps):
    h=W+eps*T;vals,vecs=eigh(h,driver='evd');w=W.diagonal().real
    U=np.zeros_like(h,dtype=complex)
    for grade in sorted(set(w)):
        ix=np.flatnonzero(w==grade);selected=np.flatnonzero(abs(vals-grade)<.45)
        assert len(ix)==len(selected)
        V=vecs[:,selected]
        # SVD polar factor of the cluster-to-bare overlap, separately by grade.
        Q,_=polar(V.conj().T[:,ix])
        U[:,ix]=V@Q
    return U,U.conj().T@h@U

exact=[];rotor=[];numeric=[]
for name,m in models.items():
    p,H2,H4=coefficients(m);q=[i for i,w in enumerate(m['Ws']) if w]
    R=s.diag(*[s.Rational(1,m['Ws'][i]) for i in q])
    A=m['T'].extract(q,p);F=m['T'].extract(q,q)
    X1=-R*A;X2=-R*F*X1;X3=R*(X1*A.H*X1-F*X2)
    assert s.simplify(A.H*X1-H2)==s.zeros(len(p))
    assert s.simplify(A.H*X2)==s.zeros(len(p))
    assert s.simplify(A.H*X3-H4)==s.zeros(len(p))
    M=X1.H*X1
    assert s.simplify(M*H2-H2*M)==s.zeros(len(p))
    exact.append({'model':name,'dimension':len(m['states']),'P_dimension':len(p),'riccati_H2_H3_H4_and_normalization_exact':True})
    if name.startswith('cycle'):
        spin=int(name[-1]);C=spin*(spin+1)
        iv=[j for j,i in enumerate(p) if m['Ns'][i]==2]
        fields=[m['states'][p[j]][0][0] for j in iv]
        expected2=s.diag(*[-4+s.Rational(4*f*f,C) for f in fields])
        expected4=s.diag(*[12*(1-s.Rational(f*f,C))**2-s.Rational(4*f*f,C*C) for f in fields])
        for i,f in enumerate(fields):
            if f+1 in fields:
                j=fields.index(f+1);expected4[i,j]=expected4[j,i]=-2*(1-s.Rational(f*(f+1),C))**2
        assert s.simplify(H2.extract(iv,iv)-expected2)==s.zeros(len(iv))
        assert s.simplify(H4.extract(iv,iv)-expected4)==s.zeros(len(iv))
        q1=[i for i,w in enumerate(m['Ws']) if w==1]
        AA=m['T'].extract(q1,p)
        B=[-j.extract(p,q1)*AA for j in m['Js']]
        loss=sum((j.H*j for j in B),s.zeros(len(p)))
        predictedloss=s.diag(*[8*(1-s.Rational(f*f,C))**2 for f in fields])
        assert s.simplify(loss.extract(iv,iv)-predictedloss)==s.zeros(len(iv))
        rotor.append({'model':name,'fields':fields,'H2_exact':True,'H4_exact':True,'first_loss_exact_formula':'8(1-m^2/[S(S+1)])^2','first_loss_diagonal':list(map(str,predictedloss.diagonal()))})
    T=npmat(m['T']);W=npmat(m['W']);d=len(T);P=np.eye(d)[:,p]
    density_embed=np.kron(P,P);w=np.array(m['Ws']);diff=(w[:,None]-w[None,:]).reshape(-1,order='F')
    off=((w[:,None]==0)^(w[None,:]==0)).reshape(-1,order='F')
    A0=-1j*1.7*diff
    for eps in (.07,.035,.0175):
        U,ht=canonical_by_cluster_svd(W,T,eps)
        maxoff=float(np.max(np.abs(ht[(w[:,None]!=w[None,:])])))
        assert maxoff<3e-13
        coeff=(ht[np.ix_(p,p)]-eps**2*npmat(H2))/eps**4
        coeferr=float(np.linalg.norm(coeff-npmat(H4),2))
        row={'model':name,'epsilon':eps,'canonical_unitarity_defect':float(np.linalg.norm(U.conj().T@U-np.eye(d),2)),
             'off_grade_h_defect':maxoff,'H4_coefficient_error':coeferr,'H4_error_over_epsilon_squared':coeferr/eps**2}
        # Complete matrix-unit residual map on the smaller two graphs.
        if name!='cycle_S2':
            kindrows=[]
            for kind in ['resolved','coherent']:
                raw=m['Js' if kind=='resolved' else 'coherent'];jt=[U.conj().T@npmat(j)@U for j in raw]
                G=superop(1.7*ht/eps**4,[math.sqrt(.6)*j/eps for j in jt])
                q1=[i for i,x in enumerate(w) if x==1]
                A=npmat(m['T'].extract(q1,p))
                Bs=[-npmat(j.extract(p,q1))@A for j in raw]
                L=superop(1.7*npmat(H2)/eps**2+1.7*npmat(H4),[math.sqrt(.6)*j for j in Bs])
                discrepancy=G@density_embed-density_embed@L.toarray()
                offR=np.zeros_like(discrepancy);offR[off]=discrepancy[off]
                Cmap=np.zeros_like(discrepancy);Cmap[off]=-eps**4*offR[off]/A0[off,None]
                diagonal=discrepancy-offR
                residual=diagonal+(G-diags(A0/eps**4))@Cmap-Cmap@L.toarray()
                # This is a Hilbert-Schmidt map norm diagnostic, not the analytic
                # dimension-independent trace-norm proof in the report.
                norm=lambda x:float(np.linalg.norm(x,2))
                record={'instrument':kind,'off_source_norm':norm(offR),'epsilon_times_off_source':eps*norm(offR),'diagonal_source_over_epsilon':norm(diagonal)/eps,'correction_over_epsilon_cubed':norm(Cmap)/eps**3,'residual_over_epsilon':norm(residual)/eps}
                assert record['residual_over_epsilon']<500
                kindrows.append(record)
            row['complete_residual_map_controls']=kindrows
        numeric.append(row)
        print(name,eps,'H4 residual',coeferr,flush=True)

data={'source_informed':True,'author_builder_imports':False,'own_builder_sha256':hashlib.sha256(OWN.read_bytes()).hexdigest(),'exact_graph_series':exact,'finite_spin_loop_and_first_loss':rotor,'canonical_and_corrector_controls':numeric,'limits':'Exact finite-sector identities and complete matrix-unit numerical residual diagnostics. Analytic general bounds and unbounded-electric first-event limit are reviewed in REPORT.md; no finite numeric sample is called a proof.'}
(HERE/'INDEPENDENT_RESULTS.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))

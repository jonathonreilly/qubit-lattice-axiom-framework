#!/usr/bin/env python3
"""Actual microscopic matrices on the complete K(2,4) spin-one Gauss sector.
Two active A centers, shared B vertices, and capacity for two formations.
No campaign model builder is imported. Author consistency evidence only.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
import numpy as np
from scipy.linalg import eigh
from scipy.sparse import coo_matrix,diags
HERE=Path(__file__).resolve().parent

A=(0,1);B=(2,3,4,5);edges=tuple(product(A,B));spin=1;C=2
states=[]
for field in product((-1,0,1),repeat=len(edges)):
    q=[1,1,0,0,0,0]
    for (a,b),e in zip(edges,field):q[a]+=e;q[b]-=e
    if all(x in (-1,0,1) for x in q):states.append((tuple(q),field))
index={f:i for i,(q,f) in enumerate(states)};d=len(states)
assert d==721
W=np.array([sum(q[a]==0 for a in A) for q,f in states],float)
N=np.array([sum(x*x for x in q) for q,f in states])
Pidx=np.flatnonzero(W==0);P=diags((W==0).astype(float),format='csr')
E2=np.array([sum(e*e for e in f) for q,f in states],float)
D=np.array([sum(e*(e-q[a]) for (a,b),e in zip(edges,f) if q[a] and not q[b]) for q,f in states],float)
Fs=[];jumps=[]
for a in A:
    rr=[];cc=[];vv=[]
    for col,(q,f) in enumerate(states):
        for k,(aa,b) in enumerate(edges):
            if aa!=a or not q[a] or q[b]:continue
            shift=-q[a]
            if abs(f[k]+shift)>spin:continue
            ff=list(f);ff[k]+=shift;row=index[tuple(ff)]
            qq=list(q);qq[b]=qq[a];qq[a]=0
            assert states[row][0]==tuple(qq)
            assert 1-f[k]*(f[k]+shift)/C==1
            rr.append(row);cc.append(col);vv.append(1.)
    Fs.append(coo_matrix((vv,(rr,cc)),shape=(d,d)).tocsr())
F=sum(Fs)
for k,(a,b) in enumerate(edges):
    pair=[]
    for sign in (1,-1):
        rr=[];cc=[]
        for col,(q,f) in enumerate(states):
            if q[a] or q[b] or abs(f[k]+sign)>spin:continue
            ff=list(f);ff[k]+=sign;row=index[tuple(ff)]
            qq=list(q);qq[a]=sign;qq[b]=-sign
            assert states[row][0]==tuple(qq)
            assert 1-f[k]*(f[k]+sign)/C==1
            rr.append(row);cc.append(col)
        pair.append(coo_matrix((np.ones(len(rr)),(rr,cc)),shape=(d,d)).tocsr())
    jumps.append(pair)
M=P@F.T@F@P
comp=M+diags((W==0)*D/C)
# On K(2,4), every other A is in each center's overlapping-star gate, so
# the original supplied compensation is P supported; this is not assumed on
# a general graph. The electric addition preserves W on the complete sector.
assert ((diags(W)@comp-comp@diags(W)).nnz)==0

inputs=[]
for n in (0,1):
    field=[0]*len(edges)
    for edge,val in { (0,2):n,(1,2):-n,(1,3):n,(0,3):-n }.items():field[edges.index(edge)]=val
    i=index[tuple(field)];assert states[i][0]==(1,1,0,0,0,0)
    v=np.zeros(d,complex);v[i]=1;inputs.append((f'circulation_{n}',v))
inputs.append(('coherent_two_flux_input',(inputs[0][1]+1j*inputs[1][1])/np.sqrt(2)))

instruments={}
identity_rows=[]
for label in ('resolved','coherent'):
    js=[j for pair in jumps for j in pair] if label=='resolved' else [sum(pair) for pair in jumps]
    Bs=[];Rs=[]
    for mu,j in enumerate(js):
        Bj=P@j@F@P
        Rj=j@F@F@P/2-F@Bj
        center=edges[mu//2 if label=='resolved' else mu][0]
        defect=Rj+Fs[center]@Bj;defect.eliminate_zeros()
        assert defect.nnz==0
        assert (diags(W-1)@Rj).nnz==0
        Bs.append(Bj);Rs.append(Rj)
    instruments[label]=(js,Bs,Rs)
    identity_rows.append({'instrument':label,'marks':len(js),'all_physical_P_columns':len(Pidx),'exact_sparse_R_identity':True})

rows=[];two_birth_controls=[]
for lam in (0.,1.):
    Cs=comp+diags(lam*(E2-D)/C)
    Qdiag=((1-lam)*D+lam*E2)/C
    for epsilon in (.04,.02,.01):
        hs=diags(W)-epsilon*(F+F.T)+epsilon**2*Cs
        h=hs.toarray();values,V=eigh(h)
        assert np.count_nonzero(values<.5)==len(Pidx)
        low=V[:,:len(Pidx)];gram=low[Pidx,:]@low[Pidx,:].T
        gv,gq=eigh(gram);assert min(gv)>.9
        invroot=(gq*(1/np.sqrt(gv)))@gq.T
        UP=low@low[Pidx,:].T@invroot
        assert np.linalg.norm(UP.T@UP-np.eye(len(Pidx)))<3e-12
        for name,psi in inputs:
            dressed=UP@psi[Pidx]
            assert abs(np.vdot(dressed,dressed)-1)<3e-13
            Hd=hs@dressed
            for instrument,(js,Bs,Rs) in instruments.items():
                if instrument=='resolved' and name=='circulation_0':
                    twice=js[14]@(js[2]@dressed)  # (0,3,+), then (1,5,+)
                    prob=float(np.vdot(twice,twice).real)
                    assert prob>1e-12 and np.linalg.norm(twice*(N-6))<1e-15
                    two_birth_controls.append({'lambda':lam,'epsilon':epsilon,'ordered_marks':[[0,3,1],[1,5,1]],'unscaled_two_jump_squared_norm':prob,'entire_output_has_N6':True})
                predpower=actualpower=0.;moment_rows=[];blocked=0
                for mu,(j,Bj,Rj) in enumerate(zip(js,Bs,Rs)):
                    bv=Bj@psi;rv=Rj@psi
                    b=float(np.vdot(bv,bv).real);r=float(np.vdot(rv,rv).real)
                    predgain=float(np.vdot(bv,Qdiag*bv).real)+r
                    predloss=float(np.vdot(Bj.T@bv,Qdiag*psi).real)
                    predpower+=predgain-predloss
                    out=j@dressed;hout=hs@out
                    norm=float(np.vdot(out,out).real)
                    gain=float(np.vdot(out,hout).real)
                    loss=float(np.vdot(j@Hd,out).real)
                    actualpower+=(gain-loss)/epsilon**4
                    if b<1e-12:
                        blocked+=1;continue
                    mean=gain/norm
                    second=float(np.vdot(hout,hout).real)/norm
                    scaledmean=mean/epsilon**2
                    scaledvariance=(second-mean**2)/epsilon**2
                    predmean=predgain/b;predvariance=r/b
                    moment_rows.append({'mark_index':mu,'B_squared_norm':b,'R_squared_norm':r,
                         'predicted_scaled_mean':predmean,'actual_scaled_mean':scaledmean,
                         'predicted_scaled_variance':predvariance,'actual_scaled_variance':scaledvariance,
                         'scaled_mean_error':abs(scaledmean-predmean),'scaled_variance_error':abs(scaledvariance-predvariance)})
                rows.append({'lambda':lam,'epsilon':epsilon,'input':name,'instrument':instrument,
                       'predicted_scaled_power':predpower,'actual_scaled_power':actualpower,
                       'scaled_power_error':abs(actualpower-predpower),
                       'max_scaled_mean_error':max(x['scaled_mean_error'] for x in moment_rows),
                       'max_scaled_variance_error':max(x['scaled_variance_error'] for x in moment_rows),
                       'leading_blocked_marks_not_normalized':blocked,'mark_moments':moment_rows})

for lam in (0.,1.):
    for name,psi in inputs:
        for instrument in instruments:
            case=[x for x in rows if x['lambda']==lam and x['input']==name and x['instrument']==instrument]
            for metric in ('scaled_power_error','max_scaled_mean_error','max_scaled_variance_error'):
                assert case[-1][metric]<case[0][metric]/8+2e-7,(lam,name,instrument,metric)

result={'graph':'complete bipartite K(2,4), all edges oriented A to B','spin':1,'complete_Gauss_dimension':d,
        'P_dimension':len(Pidx),'sector_counts':{str(k):v for k,v in sorted(Counter((int(n),int(w)) for n,w in zip(N,W)).items())},
        'exact_all_P_operator_controls':identity_rows,'rows':rows,'all_assertions_passed':True,
        'actual_two_birth_nonzero_controls':two_birth_controls,
        'capacity':'The full N=6 sector is included; two formations are possible on this graph. No claim about six-site cycle capacity is changed.',
        'scope':'Direct canonical low-band dressing and original full microscopic H/j moments. Epsilon is varied at fixed S=1 to test the uniform perturbation formulas including the slow Q contribution; this is not a numerical S-to-infinity proof.'}
(HERE/'COMPLETE_TWO_CENTER_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'all_assertions_passed':True,'dimension':d,'P_dimension':len(Pidx),'cases':len(rows),
                  'largest_final_scaled_power_error':max(x['scaled_power_error'] for x in rows if x['epsilon']==.01),
                  'n0_final_rows':[{k:x[k] for k in ('lambda','instrument','predicted_scaled_power','actual_scaled_power','scaled_power_error')} for x in rows if x['epsilon']==.01 and x['input']=='circulation_0']},indent=2))

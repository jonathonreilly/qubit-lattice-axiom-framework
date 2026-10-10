# R1 check 2: (a) EH comparator with correct derivative sign (d -> i q, two derivatives give -qq),
# Jordan structure of the scalar mode when only the vector gauge is exact;
# (b) generic random gauge-invariant compact quadratic Hamiltonians: dispersion order and speed spread.
import numpy as np
from r1_modes import ops, phys_basis, lin, t2v, v2t
rng=np.random.default_rng(7)
nhat=np.array([0.31,0.52,0.79]); nhat/=np.linalg.norm(nhat)
def hamilton(W,K,V):
    Kp=W.T@K@W; Vp=W.T@V@W; n=W.shape[1]
    # H = 1/2 p.Kp.p + 1/2 x.Vp.x ; xdot = Kp p ; pdot = -Vp x
    return np.block([[np.zeros((n,n)),Kp],[-Vp,np.zeros((n,n))]])
for model in ['V_EH','VS_EH']:
    for kk in [1e-2,1e-3]:
        q=2*np.sin(kk*nhat/2); o=ops(q)
        cols=[o['Gt']] if model=='V_EH' else [o['Gt'],o['S'].T]
        W=phys_basis(cols); F=hamilton(W,o['DeW'],-o['R'])
        ev=np.linalg.eigvals(F)
        # nilpotency index of the zero-frequency block
        Fn=F.copy(); idx=1
        while idx<8 and np.abs(np.linalg.matrix_power(F,idx)).max()>1e-14: idx+=1
        print(model,'k=',kk,' omega (=|Im ev|)/k:',np.round(np.sort(np.abs(ev.imag))/kk,4),' max|Re ev|/k=',round(np.abs(ev.real).max()/kk,4))
    # scalar block alone
q=2*np.sin(1e-3*nhat/2); o=ops(q); W=phys_basis([o['Gt']])
# identify scalar (transverse trace) direction in W
P=np.eye(3)-np.outer(q,q)/(q@q); s=t2v(P)/np.linalg.norm(t2v(P))
c=W.T@s; print('V_EH: transverse-trace mode kinetic DeWitt coefficient s.K.s =',round(s@o['DeW']@s,12),
               '; potential s.(-R).s / k^2 =',round(s@(-o['R'])@s/(q@q),6))
Fs=np.array([[0, s@o['DeW']@s],[-(s@(-o['R'])@s),0]]); print('scalar Hamilton block',Fs,' F^2 =',Fs@Fs)
# (b) generic invariant compact Hamiltonians
def rand_pos(n): A=rng.normal(size=(n,n)); return A@A.T/n+0.2*np.eye(n)
print('\nGeneric compact invariant quadratic Hamiltonians (random positive coefficients):')
for model in ['V','VS','F']:
    slopes=[]; spreads=[]
    for trial in range(20):
        MK=rand_pos(9); MV=rand_pos(9) if model!="V" else rand_pos(6); KV=rand_pos(6)
        res=[]
        for kk in [1e-2,1e-3]:
            q=2*np.sin(kk*nhat/2); o=ops(q)
            if model=="V":  W=phys_basis([o["Gt"]])
            if model=='V':
                K=KV; V=o['R'].T@MV@o['R']
            if model=='VS':
                W=phys_basis([o['Gt'],o['S'].T]); K=o['C'].T@MK@o['C']; V=o['R'].T@MV[:6,:6]@o['R']
            if model=='F':
                W=phys_basis([o['Ft']]); K=KV; V=o['B'].T@MK@o['B']
            w2=np.real(np.linalg.eigvals((W.T@K@W)@(W.T@V@W)))
            res.append(np.sort(w2))
        sl=np.log(res[0]/res[1])/np.log(10); slopes.append(sl)
        spreads.append(np.sqrt(res[1].max()/res[1].min()))
    print(model,' slope of omega^2 vs k (all modes, 20 trials): min %.3f max %.3f ; max/min speed ratio median %.3f'%(np.min(slopes),np.max(slopes),np.median(spreads)))

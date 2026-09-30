import numpy as np
from t40_consts import *
A2 = a2()
# lattice g2 (Ward no-go note: g2^2 = 1/(d+1) = 1/4 at cutoff), one-loop SM running down to v
def g2_run(g2M=0.5, M=1.221e19, mu=246.22, b=-19/6):
    inv = 1/g2M**2 - (-b/(8*np.pi**2))*np.log(M/mu)*(-1)  # placeholder, fixed below
    # d(1/g^2)/dln mu = -b/(8 pi^2); going from M down to mu: 1/g^2(mu) = 1/g^2(M) + (-b/(8pi^2))*ln(mu/M)
    inv = 1/g2M**2 + (-b/(8*np.pi**2))*np.log(mu/M)
    return 1/np.sqrt(inv)
g2fw = g2_run()
print('g2 lattice-run one-loop at v: %.4f   (data on-shell 2mW/v = %.4f, MSbar(mZ) ~0.6517)'%(g2fw, 2*MW/V_GF))
rows=[]
print('\n P      dP    v_chain(GeV)  F2r m_tau/v dev%   F2a m_tau dev%     F1f(g2fw,v_chain) a2 dev%   F1f(g2fw,v_GF) dev%  F1(g2 data,v_GF) dev%')
for dP in (0.0,0.021,0.037,0.065):
    P=P0+dP
    vc=v_chain(P)          # MeV
    f2r = ABARE*alphaLM(P)*V_GF/MTAU-1          # ratio-form deviation, vs data v
    f2a = mtau_chain(P)/MTAU-1
    f1a = g2fw*vc/512/A2-1
    f1b = g2fw*V_GF/512/A2-1
    f1c = (2*MW/V_GF)*V_GF/512/A2-1
    print(' %.4f %.3f  %8.2f       %+8.3f          %+8.2f            %+8.2f                %+8.2f              %+8.3f'%(P,dP,vc/1000,f2r*100,f2a*100,f1a*100,f1b*100,f1c*100))
# Koide shape included: a2 predicted via F2r: a2 = alpha_bare*alpha_LM*V_GF/shape
print()
for dP in (0.0,0.021,0.037,0.065):
    P=P0+dP
    a2pred = ABARE*alphaLM(P)*V_GF/koide_shape()
    print('P=%.4f  a2 via F2r+Koide(2/9) = %.4f MeV  dev %+.3f%%'%(P,a2pred,(a2pred/A2-1)*100))
# Pre-registered decision
def dev(dP): 
    P=P0+dP
    return {'F2r':ABARE*alphaLM(P)*V_GF/MTAU-1,'F1f':g2fw*V_GF/512/A2-1}
q=dev(0.0); u=[dev(x) for x in (0.021,0.037,0.065)]
for k in ('F2r','F1f'):
    ok = abs(q[k])<=0.005 and all(abs(x[k])<=0.02 for x in u)
    print(k,'quenched dev %+.3f%%; unquenched devs'%(q[k]*100),['%+.2f%%'%(x[k]*100) for x in u],' -> PASS' if ok else ' -> FAIL')
# what P would F2r/F2a need for exact hit, and how tight is P
from scipy.optimize import brentq
Pneed=brentq(lambda P: ABARE*alphaLM(P)*V_GF/MTAU-1,0.5,0.7)
print('P needed for F2r exact: %.5f (quenched beta=6 P0 = %.4f)  -> matching to 0.0201%% needs P to %.4f%%'%(Pneed,P0,abs(Pneed/P0-1)*100))
Pneed2=brentq(lambda P: mtau_chain(P)/MTAU-1,0.5,0.7)
print('P needed for F2a exact: %.5f  (%.4f%% from P0)'%(Pneed2,abs(Pneed2/P0-1)*100))

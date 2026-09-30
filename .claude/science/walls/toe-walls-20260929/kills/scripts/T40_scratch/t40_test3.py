import numpy as np
from t40_consts import *
A2=a2()
print('Test 3: exponent required per anchor (scale a^2); integer within 0.1% => structural-count candidate')
print('anchor        ratio A/a2   log2     frac-dist-to-int   log4    (2*A: log2)')
for n,a in (('m_W',MW),('m_Z',MZ),('v(GF)',V_GF),('v/sqrt2',V_GF/np.sqrt(2)),('m_W*cosW-free g2v/2 -> g2 v',None)):
    if a is None: continue
    r=a/A2
    for dn,d in (('1',1),('2',2)):
        x=np.log2(d*r); rel=abs(2**round(x)/(d*r)-1)
        print('%-9s D=%s  %10.3f  %8.4f   nearest 2^%d off %.4f%%   log4=%.4f'%(n,dn,d*r,x,round(x),rel*100,x/2))
# 'g2' dressing: a2 = g2 * v/512  -> v/a2 = 512/g2
print('v/a2 =',V_GF/A2,'; 512/g2_data =',512/(2*MW/V_GF))
print('bits: log2(M_Pl/a2)=%.2f  log2(M_Pl/v)=%.2f  log2(v/a2)=%.2f'%(np.log2(MPL/A2),np.log2(MPL/V_GF),np.log2(V_GF/A2)))
print('a2/(v ab aLM) = %.5f   1/(4 sqrt2)=%.5f  off %.3f%%;  Koide shape (1+sqrt2 cos(2/9))^2=%.5f vs 4 sqrt2=%.5f (%.3f%%)'%(A2/(V_GF*ABARE*alphaLM(P0)),1/(4*np.sqrt(2)),(A2/(V_GF*ABARE*alphaLM(P0))*4*np.sqrt(2)-1)*100,koide_shape(),4*np.sqrt(2),(koide_shape()/(4*np.sqrt(2))-1)*100))
gimp=512*ABARE*alphaLM(P0)/koide_shape()
print('F1 and F2 together imply g2 = 512 alpha_bare alpha_LM/shape = %.5f vs 2mW/v = %.5f (%.3f%%)'%(gimp,2*MW/V_GF,(gimp/(2*MW/V_GF)-1)*100))
# m_W window and newer m_W measurements (values recalled, not verified in repo)
for name,mw,s in (('PDG note',80369.2,13.3),('CMS2024 (recalled)',80360.2,9.9),('ATLAS2024 (recalled)',80366.5,15.9),('CDF2022 (recalled)',80433.5,9.4)):
    print('%-22s N=%.4f  sigma from 256: %+.2f'%(name,mw/A2,(mw/A2-256)/(s/A2)))

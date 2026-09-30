import numpy as np
from t40_consts import *
A2=a2()
M=np.array([ME,MMU,MTAU])
print('Scheme test: a^2 pole = %.4f MeV;  m_W/a2 = %.3f'%(A2,MW/A2))
for alpha,mu,lab in ((1/137.036,MW,'1-loop QED MSbar(m_W), alpha=1/137'),(1/128.0,MW,'1-loop QED MSbar(m_W), alpha=1/128'),(1/137.036,MTAU,'1-loop QED MSbar(m_tau)')):
    m=M*(1-(alpha/np.pi)*(1+0.75*np.log(mu**2/M**2)))
    a=a2(tuple(m)); print('  %-40s a2=%.3f  shift %+.2f%%  m_W/a2=%.2f'%(lab,a,(a/A2-1)*100,MW/a))
m=np.array([0.48657,102.718,1746.24]); a=a2(tuple(m))
print('  lane-recalled MSbar(M_Z) masses         a2=%.3f  shift %+.2f%%  m_W/a2=%.2f (log2=%.3f)'%(a,(a/A2-1)*100,MW/a,np.log2(MW/a)))
print('  => pole-mass 0.03%% match sits inside a %.1f%% scheme spread (100x the offset)'%(abs(a/A2-1)*100))
print()
print('Cross-sector: same statistic for quarks, MSbar(M_Z) masses RECALLED (Xing-Zhang-Zhou 2008/2012, not verified here), GeV')
for lab,(mu_,md_,ms_,mc_,mb_,mt_) in (('XZZ2008',(1.27e-3,2.90e-3,55e-3,0.619,2.89,171.7)),('XZZ2012',(1.38e-3,2.82e-3,57e-3,0.638,2.86,172.1))):
    au=(sum(np.sqrt(x) for x in (mu_,mc_,mt_))/3)**2; ad=(sum(np.sqrt(x) for x in (md_,ms_,mb_))/3)**2
    print('  %s: a_u^2=%.3f GeV  mW/a_u^2=%.3f log2=%.3f | a_d^2=%.4f GeV  mW/a_d^2=%.2f log2=%.3f'%(lab,au,80.3692/au,np.log2(80.3692/au),ad,80.3692/ad,np.log2(80.3692/ad)))

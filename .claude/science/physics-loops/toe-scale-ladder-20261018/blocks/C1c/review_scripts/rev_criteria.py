#!/usr/bin/env python3
"""Reviewer recomputation of C1c's criterion numbers from the tabulated summaries (analysis_L4_L6_final.log)."""
import numpy as np
z=lambda a,ea,b,eb:(a-b)/np.hypot(ea,eb)
# EQ start-diff z from per-run values
print("EQ L4 b4: E",z(-54.643,.078,-54.668,.061),"W2",z(.11781,.011,.11058,.013),"S1",z(.32897,.0025,.32885,.002))
print("EQ L6 b6: E",z(-186.63,.094,-186.34,.084),"W2",z(.05047,.011,.039421,.0081),"S1",z(.20811,.0028,.20775,.0021))
print("EQ L6 b3: E",z(-173.42,.16,-173.45,.15),"W2",z(.45226,.022,.58831,.03),"S1",z(.29722,.0025,.29857,.0023))
# combined E L6: binned-combined vs scatter
b=0.5*np.hypot(.094,.084); sc=abs(-186.63+186.34)/2; print("L6 E binned comb",b,"scatter",sc)
# fit a(L)
L=np.array([4,6]); d=np.array([.69201,.626464]); ed=np.array([.021,.026]); a=L*d; ea=L*ed
s=(a[1]-a[0])/2; es=np.hypot(ea[0],ea[1])/2; print("a",a,ea,"s",s,es,"s/es",s/es)
dt=np.array([.670,.647]); edt=np.array([.020,.039]); at=L*dt; print("TI s",(at[1]-at[0])/2, np.hypot(*(L*edt))/2, ((at[1]-at[0])/2)/(np.hypot(*(L*edt))/2))
K=np.array([.114197,.0449456]); eK=np.array([.0083,.0067]); r=K[1]/K[0]; er=r*np.hypot(eK[0]/K[0],eK[1]/K[1]); print("K ratio",r,er,(0.5-r)/er)
# chunk-error K ratio
Kc4=np.mean([.1129,.1100]); eKc4=0.5*np.hypot(.0135,.0139); Kc6=np.mean([.0495,.0395]); eKc6=0.5*np.hypot(.0107,.0080)
rc=Kc6/Kc4; erc=rc*np.hypot(eKc4/Kc4,eKc6/Kc6); print("K ratio chunk",rc,erc,(0.5-rc)/erc)
S=np.array([.32891,.207931]); eS=np.array([.0016,.0018]); p=np.log(S[0]/S[1])/np.log(1.5); ep=np.hypot(eS[0]/S[0],eS[1]/S[1])/np.log(1.5); print("p",p,ep,"(1.6-p)/ep",(1.6-p)/ep,"(1.4-p)/ep",(1.4-p)/ep)
# dF1 decrease significance
print("dF1 decrease z",z(.69201,.021,.626464,.026))
# L8
E3,e3,E5,e5=-443.788,.192,-443.914,.218; Em=(E3+E5)/2; eb=0.5*np.hypot(e3,e5); sc=abs(E3-E5)/2
e=max(eb,sc); print("L8",Em,eb,sc,"z repo",z(Em,e,-443.364,.031),"z C1",z(Em,e,-443.83,.14))
f5=[-444.162,-444.376,-443.141,-444.395,-443.497]; f3=[-443.427,-444.015,-443.77,-443.672,-444.056]
ef=0.5*np.hypot(np.std(f3,ddof=1)/np.sqrt(5),np.std(f5,ddof=1)/np.sqrt(5)); print("fifths err",ef,"z repo",z(Em,ef,-443.364,.031))
for infl in (1.2,1.4): print("z repo with err x",infl, z(Em,e*infl,-443.364,.031))

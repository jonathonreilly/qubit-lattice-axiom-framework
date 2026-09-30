import numpy as np
# masses MeV (note's set, PDG-2020-ish) and PDG2024 set
ME,MMU,MTAU = 0.5109989461,105.6583745,1776.86
MW,MZ = 80369.2, 91187.6        # MeV
GF = 1.1663788e-5               # GeV^-2
V_GF = (np.sqrt(2)*GF)**-0.5*1000   # MeV  ~246220
MPL = 1.221e22                  # MeV (1.221e19 GeV, chain note)
P0 = 0.5934
ABARE = 1/(4*np.pi)
def a2(m=(ME,MMU,MTAU)):
    return (sum(np.sqrt(x) for x in m)/3)**2
def u0(P): return P**0.25
def alphaLM(P): return ABARE/u0(P)
def v_chain(P): return MPL*(7/8)**0.25*alphaLM(P)**16
def mtau_chain(P): return MPL*(7/8)**0.25*u0(P)*alphaLM(P)**18
def koide_shape(delta=2/9):  # m_tau / a^2 for r=1/2
    return (1+np.sqrt(2)*np.cos(delta))**2
if __name__=='__main__':
    print('a2 =',a2(),' MeV;  m_W/256 =',MW/256,' off %.4f%%'%((MW/256/a2()-1)*100))
    print('N = mW/a2 =',MW/a2(),' sigma from 256:',(MW/a2()-256)/(13.3/a2()))
    print('V_GF =',V_GF/1000,' GeV; g2 = 2mW/v =',2*MW/V_GF)
    print('v_chain(P0) =',v_chain(P0)/1000,'GeV;  alphaLM=',alphaLM(P0),' u0=',u0(P0))
    print('mtau_chain(P0) =',mtau_chain(P0),' MeV vs',MTAU,' dev %.4f%%'%((mtau_chain(P0)/MTAU-1)*100))
    print('m_tau/v_GF =',MTAU/V_GF,' alpha_bare*alpha_LM =',ABARE*alphaLM(P0),' dev %.4f%%'%((ABARE*alphaLM(P0)*V_GF/MTAU-1)*100))
    print('koide shape mtau/a2 =',koide_shape(),' data',MTAU/a2())

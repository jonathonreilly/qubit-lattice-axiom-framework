import numpy as np
from scipy.optimize import brentq
import lane_rge_copy as H
PI=np.pi
V=H.V_DERIVED            # 246.28
MPL=H.M_PL
t_v=np.log(V); t_pl=np.log(MPL)
ALPHA_LM=H.ALPHA_LM; ALPHA_BARE=H.ALPHA_BARE; U0=H.U0
ALPHA_S_V=H.ALPHA_S_V_DERIVED  # 0.1033
G1_K0, G2_K0 = 0.4644, 0.6480   # lane's kappa_EW = 0 values at v
K_SERIES = 1.0619               # docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md:534-540

def gauge_at_v(kEW=0, alpha_s=ALPHA_S_V):
    # kappa_EW=1 removes the sqrt(9/8) connected-trace factor: g_EW -> g_EW/sqrt(9/8)
    f = 1.0 if kEW==0 else 1/np.sqrt(9/8)
    return G1_K0*f, G2_K0*f, np.sqrt(4*PI*alpha_s)

def up(yt_v, g, lam_v=0.13, loop=3):
    y0=[g[0],g[1],g[2],yt_v,lam_v]
    sol=H.run_rge(y0,t_v,t_pl,n_f=6,loop_order=loop)
    return sol.y[:,-1]

def beta_lam_at_pl(yt_v, g, loop=3, lam_pl=0.0):
    ypl=up(yt_v,g,loop=loop)
    y=[ypl[0],ypl[1],ypl[2],ypl[3],lam_pl]
    return H.beta_full(t_pl,y,n_f=6,loop_order=loop)[4], ypl

def crit_yt_v(g, loop=3, lam_pl=0.0, lo=0.80, hi=1.05):
    f=lambda yt: beta_lam_at_pl(yt,g,loop=loop,lam_pl=lam_pl)[0]
    return brentq(f,lo,hi,xtol=1e-10)

def ward_yt_v(yt_pl_target, g, loop=3, lo=0.85, hi=1.08):
    # backward Ward scan: find yt(v) s.t. yt(M_Pl)=target, gauge couplings anchored at v
    f=lambda yt: up(yt,g,loop=loop)[3]-yt_pl_target
    return brentq(f,lo,hi,xtol=1e-10)

def down_from_pl(yt_pl, g_pl, mu_end, loop=3):
    y0=[g_pl[0],g_pl[1],g_pl[2],yt_pl,0.0]
    sol=H.run_rge(y0,t_pl,np.log(mu_end),n_f=6,loop_order=loop)
    return sol.y[:,-1]

def run_yt_from_v(yt_v, g, mu_end, loop=3, lam_v=0.13):
    y0=[g[0],g[1],g[2],yt_v,lam_v]
    sol=H.run_rge(y0,t_v,np.log(mu_end),n_f=6,loop_order=loop)
    return sol.y[:,-1]

def msbar_mass_scale(yt_v, g, loop=3):
    """find mu* with m(mu*) = y_t(mu*) V/sqrt2 = mu*; return (mu*, m(mu*))"""
    f=lambda mu: run_yt_from_v(yt_v,g,mu,loop=loop)[3]*V/np.sqrt(2)-mu
    mu=brentq(f,120.0,240.0,xtol=1e-6)
    return mu, mu

def pole_from_yt_v(yt_v, g, loop=3, kappaY0=False):
    """m_t(pole) = K * m_MSbar(m_t); yt_v is the y_t at v BEFORE any kappa_Y projection"""
    yv = yt_v*(np.sqrt(8/9) if kappaY0 else 1.0)
    mu,m = msbar_mass_scale(yv,g,loop=loop)
    return K_SERIES*m, m, mu

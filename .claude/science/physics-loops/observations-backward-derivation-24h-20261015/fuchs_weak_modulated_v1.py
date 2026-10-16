"""Complex bilinear weak probes; no physical channel assignment."""
import numpy as np
from fuchs_weak_math_v1 import windows

def modulated_integrals(t, z, u, duration, kappas, stride=1):
    rows=[]
    for window_index,(lo,hi) in enumerate(windows(t,duration)):
        ids=np.arange(lo,hi,stride)
        if ids[-1]!=hi-1: ids=np.r_[ids,hi-1]
        tt=t[ids]; zz=z[ids]; uu=u[ids]
        L=float(t[hi-1]-t[lo]); dt=tt-t[lo]; s=dt/L
        p=140*(s**3-3*s**4+3*s**5-s**6)/L
        dp=140*(3*s**2-12*s**3+15*s**4-6*s**5)/L**2
        ddp=140*(6*s-36*s**2+60*s**3-30*s**4)/L**3
        for kappa in kappas:
            oscillation=np.exp(-1j*kappa*dt)
            w=p*oscillation
            dw=(dp-1j*kappa*p)*oscillation
            ddw=(ddp-2j*kappa*dp-kappa**2*p)*oscillation
            weight_integral=np.trapezoid(w,tt)
            rows.append(dict(window_index=window_index,lo=lo,hi=hi,
                t0=float(tt[0]),t1=float(tt[-1]),kappa_per_s=float(kappa),
                weight_integral_complex=[float(weight_integral.real),float(weight_integral.imag)],
                moments=[np.trapezoid(w*zz,tt),np.trapezoid(dw*zz,tt),
                         np.trapezoid(ddw*zz,tt),np.trapezoid(w*uu,tt)]))
    return rows

def phase_slope(t, phasor):
    phase=np.unwrap(np.angle(phasor))
    centered=t-np.mean(t)
    slope=float(np.dot(centered,phase-np.mean(phase))/np.dot(centered,centered))
    residual=phase-(np.mean(phase)+slope*centered)
    return slope,dict(slope_rad_per_s=slope,
        affine_phase_residual_rms_rad=float(np.sqrt(np.mean(residual**2))),
        affine_phase_residual_max_rad=float(np.max(abs(residual))),
        net_unwrapped_phase_rad=float(phase[-1]-phase[0]))

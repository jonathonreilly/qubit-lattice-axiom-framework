"""Compact-window oscillator identities; no experimental channel identification."""
import numpy as np

def windows(t, duration):
    start = float(t[0]); stop = float(t[-1]); result = []
    for j in range(int(np.floor((stop-start)/duration))):
        lo = np.searchsorted(t, start+j*duration, side="left")
        hi = np.searchsorted(t, start+(j+1)*duration, side="right")
        if hi-lo < 5:
            raise ValueError("Insufficient samples")
        result.append((int(lo), int(hi)))
    return result

def integrals(t, z, u, duration, stride=1):
    rows = []
    for lo, hi in windows(t, duration):
        ids = np.arange(lo, hi, stride)
        if ids[-1] != hi-1:
            ids = np.r_[ids, hi-1]
        tt = t[ids]; zz = z[ids]; uu = u[ids]
        L = float(t[hi-1]-t[lo]); s = (tt-t[lo])/L
        w = 140*(s**3-3*s**4+3*s**5-s**6)/L
        wp = 140*(3*s**2-12*s**3+15*s**4-6*s**5)/L**2
        wpp = 140*(6*s-36*s**2+60*s**3-30*s**4)/L**3
        values = [np.trapezoid(w*zz, tt), np.trapezoid(wp*zz, tt),
                  np.trapezoid(wpp*zz, tt), np.trapezoid(w*uu, tt)]
        rows.append(dict(lo=lo, hi=hi, t0=float(tt[0]), t1=float(tt[-1]),
                         moments=values, weight_integral=float(np.trapezoid(w,tt))))
    return rows

def design(rows, Omega, exact=True):
    moments=np.array([r["moments"] for r in rows],dtype=complex)
    C,D,E,U=moments.T
    R=-D-1j*E/(2*Omega) if exact else -D
    B=C+1j*D/Omega if exact else C
    complex_design=np.column_stack([B,1j*C,U,1j*U])
    X=np.vstack([complex_design.real,complex_design.imag])
    y=np.r_[R.real,R.imag]
    return X,y,complex_design,R

def fit(rows,Omega,exact=True,train_count=None):
    X,y,Z,R=design(rows,Omega,exact)
    n=len(rows);ntrain=n if train_count is None else train_count
    ids=np.r_[np.arange(ntrain),np.arange(n,n+ntrain)]
    Xt,yt=X[ids],y[ids]
    scale=np.linalg.norm(Xt,axis=0)
    if np.any(scale==0): raise ValueError("Zero regressor column")
    normalized=Xt/scale
    pars_scaled,resid,rank,singular=np.linalg.lstsq(normalized,yt,rcond=None)
    pars=pars_scaled/scale
    predicted=Z@pars
    error=R-predicted
    train=np.arange(ntrain); test=np.arange(ntrain,n)
    def rms(v):return float(np.sqrt(np.mean(np.abs(v)**2))) if len(v) else None
    gamma=-2*pars[0]; omega0sq=Omega**2+2*Omega*pars[1]
    return dict(parameters=pars.tolist(),gamma_per_s=float(gamma),
                omega0_squared=float(omega0sq),
                inferred_mode_frequency_Hz=float(np.sqrt(omega0sq)/(2*np.pi)) if omega0sq>0 else None,
                forcing_coefficient_abs=float(np.hypot(pars[2],pars[3])),
                real_rank=int(rank),normalized_singular_values=singular.tolist(),
                raw_singular_values=np.linalg.svd(Xt,compute_uv=False).tolist(),
                normalized_condition=float(singular[0]/singular[-1]) if singular[-1]>0 else None,
                train_windows=ntrain,validation_windows=n-ntrain,
                train_residual_rms=rms(error[train]),train_R_rms=rms(R[train]),
                validation_residual_rms=rms(error[test]),validation_R_rms=rms(R[test]),
                predicted=[[float(v.real),float(v.imag)] for v in predicted],
                observed=[[float(v.real),float(v.imag)] for v in R],
                residual=[[float(v.real),float(v.imag)] for v in error])

def serial_rows(rows):
    return [{**{k:v for k,v in row.items() if k!="moments"},
             "moments":[[float(v.real),float(v.imag)] for v in row["moments"]]} for row in rows]

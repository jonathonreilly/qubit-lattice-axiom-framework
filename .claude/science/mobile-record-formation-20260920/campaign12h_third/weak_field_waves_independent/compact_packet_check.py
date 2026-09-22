"""Independent compact one-square weak-field wave-packet control.

This one-coordinate model tests normalization and the residual, not the
three-dimensional theorem. No author runner or output is imported.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import math
import numpy as np
from scipy.linalg import eigh

HERE=Path(__file__).resolve().parent


def cutoff(theta):
    inner=np.pi/2;outer=3*np.pi/4
    u=np.clip((np.abs(theta)-inner)/(outer-inner),0,1)
    return 1-10*u**3+15*u**4-6*u**5


def calculate(h, extra=0, grid=8192):
    mmax=math.ceil(10/math.sqrt(h))+extra
    m=np.arange(-mmax,mmax+1)
    theta=2*np.pi*(np.arange(grid)/grid-.5);x=theta/math.sqrt(h)
    # -4 d_x^2+x^2: a=1/2, E0=2, E1=6, x01=1.
    psi0=(.5/np.pi)**.25*np.exp(-x*x/4)
    psi1=x*psi0
    f0=h**(-.25)*cutoff(theta)*psi0
    f1=h**(-.25)*cutoff(theta)*psi1
    def coefficients(f):
        fft=np.fft.fft(f)/grid
        return np.sqrt(2*np.pi)*np.where(m%2==0,1.,-1.)*fft[m%grid]
    c0=coefficients(f0);c1=coefficients(f1)
    assert abs(np.vdot(c0,c1))<1e-12
    norm=math.sqrt((np.vdot(c0,c0).real+np.vdot(c1,c1).real)/2)
    initial=(c0+c1)/(np.sqrt(2)*norm)
    ham=np.diag(4*h*m*m+2/h)-(np.eye(len(m),k=1)+np.eye(len(m),k=-1))/h
    energies,vectors=eigh(ham)
    amplitudes=vectors.T@initial
    r0=ham@c0-2*c0;r1=ham@c1-6*c1
    assert abs(np.vdot(r0,r1))<1e-9
    residual=math.sqrt((np.vdot(r0,r0).real+np.vdot(r1,r1).real)/2)/norm
    phase=np.exp(1j*np.outer(theta,m))/np.sqrt(2*np.pi)
    rows=[]
    for t in (.2,.75,1.5):
        state=vectors@(np.exp(-1j*t*energies)*amplitudes)
        target=(np.exp(-2j*t)*c0+np.exp(-6j*t)*c1)/(np.sqrt(2)*norm)
        error=float(np.linalg.norm(state-target))
        assert abs(np.linalg.norm(target)-1)<1e-12
        assert error<=t*residual+1e-10
        field=phase@state;target_field=phase@target
        prob=2*np.pi/grid*np.abs(field)**2
        target_prob=2*np.pi/grid*np.abs(target_field)**2
        s=.6
        char=complex(np.sum(prob*np.exp(1j*s*x)))
        target_char=complex(np.sum(target_prob*np.exp(1j*s*x)))
        harmonic_char=complex(np.exp(-s*s/2)*(1-s*s/2+1j*s*np.cos(4*t)))
        assert abs(char-target_char)<=2*error+1e-10
        rows.append({'time':t,'state_norm_error':error,'error_divided_by_h':error/h,
                     'Duhamel_bound_time_times_residual':t*residual,
                     'scaled_angle_mean':float(np.sum(prob*x)),
                     'harmonic_scaled_angle_mean':math.cos(4*t),
                     'scaled_electric_mean':float(math.sqrt(h)*np.sum(m*np.abs(state)**2)),
                     'harmonic_scaled_electric_mean':-.5*math.sin(4*t),
                     'bounded_characteristic_difference':float(abs(char-harmonic_char)),
                     'cutoff_harmonic_characteristic_difference':float(abs(target_char-harmonic_char))})
    grid_norm=2*np.pi/grid*float(np.sum((f0*f0+f1*f1)/2))
    return {'h':h,'Fourier_cutoff':mmax,'grid':grid,'compact_norm_before_normalization':norm,
            'grid_norm_squared_minus_retained_norm_squared':grid_norm-norm**2,
            'residual_norm':residual,'residual_divided_by_h':residual/h,'times':rows}


def main():
    rows=[calculate(h) for h in (1/8,1/16,1/32,1/64,1/128,1/256)]
    predicted=math.sqrt(525)/12
    assert abs(rows[-1]['residual_divided_by_h']/predicted-1)<.02
    for j in range(3):
        assert all(rows[i+1]['times'][j]['state_norm_error']<rows[i]['times'][j]['state_norm_error']
                   for i in range(len(rows)-1))
    refined=calculate(1/32,extra=24,grid=16384)
    base=rows[2]
    comparisons=[]
    for x,y in zip(base['times'],refined['times']):
        keys=['state_norm_error','scaled_angle_mean','scaled_electric_mean','bounded_characteristic_difference']
        errors={k:abs(x[k]-y[k]) for k in keys}
        assert max(errors.values())<1e-9
        comparisons.append({'time':x['time'],'absolute_differences':errors})
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
         'model':'One cyclic square: H_h+2/h=4h m^2+(2-e^{i theta}-e^{-i theta})/h, on L2(S1); K=h,J=1/h.',
         'initial_packet':'C2 cutoff of h^-1/4 (psi0(theta/sqrt(h))+psi1(theta/sqrt(h)))/sqrt(2), normalized on the compact circle.',
         'harmonic_model':'-4 d_x^2+x^2; E0=2,E1=6, so the centroid frequency is 4.',
         'exact_leading_residual':'sqrt(525)/12 times h; x^8 mixture moment=(105+945)/2=525.',
         'predicted_residual_divided_by_h':predicted,'rows':rows,
         'independent_grid_and_Fourier_refinement':{'refined':refined,'differences':comparisons},
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'limits':'Floating finite Fourier calculations and explicit refinement; no interval enclosure or proof of the full 3D bound. The report provides the analytic finite-time argument.'}
    text=json.dumps(out,indent=2)+'\n';(HERE/'COMPACT_PACKET_RESULTS.json').write_text(text);print(text,end='')


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Independent small harmonic-symbol and unit-conversion controls.

No repository numerical code, source event data, likelihood, or microscopic
evolution is imported. Floating controls are not interval certificates.
"""
from pathlib import Path
import hashlib
import json
import time
import mpmath as mp
import numpy as np

mp.mp.dps = 70


def norm(v):
    return mp.sqrt(sum(x*x for x in v))


def omega(k):
    return mp.sqrt(sum(2*(1-mp.cos(x)) for x in k))


def vector_control(direction, x):
    n = [mp.mpf(y)/norm(direction) for y in direction]
    k = [x*y for y in n]
    w = omega(k)
    a4 = sum(y**4 for y in n)
    v = [mp.sin(y)/w for y in k]
    expected = [y+x*x*(a4*y/24-y**3/6) for y in n]
    radial = sum(y*z for y,z in zip(n,v))
    speed = norm(v)
    derivative_error = []
    for i in range(3):
        def shifted(t):
            point = k.copy()
            point[i] += t
            return omega(point)
        derivative_error.append(abs(mp.diff(shifted,0)-v[i]))
    phase_error = abs(w/x-(1-a4*x*x/24))/x**4
    vector_error = norm([s-t for s,t in zip(v,expected)])/x**4
    radial_error = abs(radial-(1-a4*x*x/8))/x**4
    speed_error = abs(speed-(1-a4*x*x/8))/x**4
    plane_time_error = abs(1/radial-(1+a4*x*x/8))/x**4
    ray_time_error = abs(1/speed-(1+a4*x*x/8))/x**4
    energy_plane_error = abs(1/radial-(1+a4*w*w/8))/w**4
    energy_ray_error = abs(1/speed-(1+a4*w*w/8))/w**4
    assert phase_error < mp.mpf(1)/400
    assert vector_error < mp.mpf(1)/40
    assert radial_error < mp.mpf(1)/40
    assert speed_error < mp.mpf(1)/20
    assert plane_time_error < mp.mpf(1)/16
    assert ray_time_error < mp.mpf(1)/10
    assert energy_plane_error < mp.mpf(1)/10
    assert energy_ray_error < mp.mpf(1)/6
    assert max(derivative_error)<mp.mpf('1e-60')
    assert speed <= 1
    # Construct the curl symbol from its three oriented cross-product rows.
    q = np.exp(1j*np.array([float(y) for y in k]))-1
    curl = np.array([[0,-q[2],q[1]],[q[2],0,-q[0]],[-q[1],q[0],0]],dtype=complex)
    squared = curl.conj().T@curl
    target = np.vdot(q,q).real*np.eye(3)-np.outer(q,q.conj())
    eigenvalues = np.linalg.eigvalsh(squared)
    gap_error = float(np.max(np.abs(eigenvalues-np.array([0,float(w*w),float(w*w)])))/float(w*w))
    assert np.max(np.abs(squared-target))<1e-14
    assert gap_error<2e-12
    return dict(direction=direction,x=str(x),A4=float(a4),
                velocity=[float(y) for y in v],tangential_speed=float(norm([z-radial*y for y,z in zip(n,v)])),
                derivative_error=float(max(derivative_error)),curl_relative_error=gap_error,
                scaled_remainders=dict(phase=float(phase_error),vector=float(vector_error),
                    radial=float(radial_error),speed=float(speed_error),
                    plane_time=float(plane_time_error),ray_time=float(ray_time_error),
                    energy_plane_time=float(energy_plane_error),energy_ray_time=float(energy_ray_error)))


def conversions():
    c=mp.mpf(299792458)
    h=mp.mpf('6.62607015e-34')
    charge=mp.mpf('1.602176634e-19')
    hbar_c=h*c/(2*mp.pi*charge*10**9)  # GeV m, from SI definitions.
    au=mp.mpf(149597870700)
    pc=648000/mp.pi*au
    mpc=10**6*pc
    eplanck=mp.mpf('1.22e19')  # Approximate value stated by the LHAASO paper.
    rows=[]
    for label,qg in [('MAGIC_quadratic_subluminal_with_systematics','5.9e10'),
                     ('MAGIC_quadratic_subluminal_without_systematics','8.0e10'),
                     ('LHAASO_v2_quadratic_subluminal_ML_MINOS','6.9e11')]:
        energy=mp.mpf(qg)
        length=mp.sqrt(12)*hbar_c/energy
        amax_axis=length
        amax_body=mp.sqrt(3)*length
        inverse=mp.sqrt(12)*hbar_c/length
        assert abs(inverse/energy-1)<mp.mpf('1e-65')
        rows.append(dict(label=label,E_QG2_GeV=float(energy),a_sqrt_A4_bound_m=float(length),
                         axis_a_bound_m=float(amax_axis),unknown_orientation_a_bound_m=float(amax_body),
                         quadratic_slowness_coefficient_GeV_minus2=float(mp.mpf(3)/(2*energy**2))))
    h0=mp.mpf('67.36')*1000/mpc
    om=mp.mpf('.315')
    z=mp.mpf('.151')
    def kernel(n,zval):
        return (1+zval)**n/mp.sqrt(om*(1+zval)**3+1-om)
    i0=mp.quad(lambda zval:kernel(0,zval),[0,z])/h0
    i2=mp.quad(lambda zval:kernel(2,zval),[0,z])/h0
    i2_independent=mp.gauss_quadrature(32,'legendre')
    nodes,weights=i2_independent
    checked=sum(weights[j]*kernel(2,z*(nodes[j]+1)/2) for j in range(32))*z/(2*h0)
    assert abs((checked-i2)/i2)<mp.mpf('1e-60')
    dq2=mp.mpf(1000)**2-mp.mpf(200)**2
    time_at_table=mp.mpf(3)/2*dq2*i2/mp.mpf('6.9e11')**2
    i_wrong=i0
    assert abs(i2/i_wrong-1)>.1
    eta_ul=mp.mpf('.32')
    from_eta=eplanck*mp.sqrt(mp.mpf('1e-15')/eta_ul)
    length_eta=mp.sqrt(12)*hbar_c/from_eta
    printed_eta_from_qg=mp.mpf('1e-15')*(eplanck/mp.mpf('6.9e11'))**2
    return dict(hbar_c_GeV_m=str(hbar_c),parsec_m=str(pc),rows=rows,
        cosmology=dict(H0_per_second=str(h0),Omega_m=str(om),z=str(z),
            I0_seconds=str(i0),I2_seconds=str(i2),I2_over_I0=str(i2/i0),
            two_quadratures_relative_difference=str(abs((checked-i2)/i2)),
            illustrative_1000_minus_200_GeV_delay_at_table_limit_seconds=str(time_at_table),
            description='Illustrative coefficient conversion; this is not a fit, measurement, or predicted value of a.'),
        LHAASO_printed_precision=dict(eta2_upper_printed=str(eta_ul),
            Eplanck_GeV_assumed=str(eplanck),EQG2_from_printed_eta_GeV=str(from_eta),
            EQG2_table_GeV='6.9e11',relative_difference=str(mp.mpf('6.9e11')/from_eta-1),
            eta2_from_printed_EQG2=str(printed_eta_from_qg),
            a_sqrt_A4_from_printed_eta_m=str(length_eta),
            conclusion='The displayed eta2 endpoint and displayed EQG2 value are not exact numerical inverses; retain both rather than claiming exact table correspondence.'))


def main():
    started=time.monotonic()
    directions=[[1,0,0],[1,1,0],[1,1,1],[1,2,3],[1,2,4],[2,-3,6]]
    rows=[vector_control(n,mp.mpf(x)) for n in directions for x in ['1','.1','.001']]
    # Two intentionally wrong replacements fail exact axis/diagonal identities.
    small=mp.mpf('.001')
    phase=2*mp.sin(small/2)/small
    group=mp.cos(small/2)
    phase_to_group=(1-phase)/(1-group)
    assert abs(phase_to_group-mp.mpf(1)/3)<mp.mpf('1e-8')
    axis=1-mp.cos(small/2)
    body=1-mp.cos(small/(2*mp.sqrt(3)))
    anisotropy=axis/body
    assert abs(anisotropy-3)<mp.mpf('1e-6')
    result=dict(scope='Independent finite harmonic symbol, analytic-remainder checks and conditional units/cosmology conversions. No source data or parent runner executed.',
        precision_decimal_digits=mp.mp.dps,rows=rows,
        mutations=dict(phase_velocity_substitution_delay_ratio=str(phase_to_group),
                       isotropic_A4_1_mutant_axis_to_body_ratio=str(anisotropy)),
        conversions=conversions(),elapsed_seconds=time.monotonic()-started,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    text=json.dumps(result,indent=2)+'\n'
    (Path(__file__).parent/'CONTROL_RESULTS.json').write_text(text)
    print(text,end='')


if __name__=='__main__':main()

"""Parent-authored canonical proper-time checks of the coordinate RHS.

The expected forces are evaluated from S derivatives at high precision;
the tested runner uses x=ln(S), double precision, and its own local functions.
No reviewer implementation is imported. Internal verification, not new data.
"""
from pathlib import Path
import json
import mpmath as mp
import numpy as np


def canonical_force_controls(rhs, close, check):
    cfg = json.loads((Path(__file__).parent/'OFF_TRAJECTORY_FIXTURES_v2.json').read_text())
    rows = []
    with mp.workdps(cfg['digits']):
        for aa in cfg['a']:
            for rr in cfg['R_over_S']:
                for ll in cfg['L_over_S']:
                    for mode in cfg['disturbances']:
                        a, rratio, lratio = map(mp.mpf, map(str, [aa, rr, ll]))
                        x = mp.mpf(str(mode['x']))
                        s = mp.exp(x)
                        l = lratio*s
                        b = rratio*s**(-mp.mpf(1)/3)
                        u = mp.mpf(str(mode['u_over_sqrt_a']))*mp.sqrt(a)
                        def rad(z):
                            return b*z**(mp.mpf(4)/3)
                        def base(z):
                            return l+a*z/2+a*rad(z)/3
                        def jmetric(z):
                            return 6*((1+a)*(z+rad(z))+l)*z*z/(a*(z+4*rad(z)/3))
                        def mass(z):
                            j = jmetric(z)
                            hess = j*mp.diff(base, z, 2)+mp.diff(jmetric, z)*mp.diff(base, z)/2
                            return a*j/hess+a*z*z/base(z)
                        def pot(uu, z):
                            return base(z)-mp.sqrt(a)*z*uu+mass(z)*uu*uu/2
                        j = jmetric(s)
                        rootg = s/mp.sqrt(j)
                        gamma = 1-s*mp.diff(jmetric, s)/(2*j)
                        v = pot(u, s)
                        vu = mp.diff(lambda z: pot(z, s), u)
                        # chi decreases with increasing S, fixing this sign.
                        vchi = -mp.sqrt(j)*mp.diff(lambda z: pot(u, z), s)
                        sm = s*mp.mpf(str(mode['matter_factor']))
                        sr = rad(s)*mp.mpf(str(mode['radiation_factor']))
                        hb = mp.sqrt(2*((1+a)*(s+rad(s))+l)/3)
                        udot = mp.mpf(str(mode['udot_over_sqrt_a_Hbar']))*mp.sqrt(a)*hb
                        chidot = mp.mpf(str(mode['chi_velocity_factor']))*mp.sqrt(a*(s+4*rad(s)/3))
                        h2 = (2*(sm+sr+v)+udot*udot+chidot*chidot)/3
                        h = mp.sqrt(h2)
                        hdot = -(sm+4*sr/3)-udot*udot-chidot*chidot
                        pu, px = udot/h, -chidot/(rootg*h)
                        state = np.array(list(map(float, [u,x,pu,px,mp.log(sm),mp.log(sr)])))
                        got = rhs(0., state, float(a), float(b), float(l))
                        uacc = -3*h*udot-vu-mp.sqrt(a)*sm
                        chiacc = -3*h*chidot-vchi
                        expected_pu = uacc/h2-pu*hdot/h2
                        expected_px = -chiacc/(rootg*h2)-px*hdot/h2-gamma*px*px
                        atol, rtol = cfg['atol'], cfg['rtol']
                        tag = str(len(rows))
                        close('off trajectory canonical u acceleration '+tag, got[2], expected_pu, atol, rtol)
                        close('off trajectory canonical chi acceleration '+tag, got[3], expected_px, atol, rtol)
                        close('off trajectory kinematic u '+tag, got[0], pu, atol, rtol)
                        close('off trajectory kinematic x '+tag, got[1], px, atol, rtol)
                        close('off trajectory matter exchange '+tag, got[4], -3+mp.sqrt(a)*pu, atol, rtol)
                        close('off trajectory tracefree radiation '+tag, got[5], -4, atol, rtol)
                        # Explicit sensitivity criterion: these fixtures cannot
                        # quietly collapse back to the exact constant-p curve.
                        check('off trajectory nonzero chi force '+tag,
                              abs(expected_px)>cfg['minimum_abs_p_acceleration'],
                              expected_p_acceleration=float(expected_px))
                        rows.append({'a':aa,'R_over_S':rr,'L_over_S':ll,
                                     'disturbance':mode,'state':state.tolist(),
                                     'H2':float(h2),'canonical_accelerations':[float(uacc),float(chiacc)],
                                     'actual_p_accelerations':got[2:4].tolist(),
                                     'expected_p_accelerations':[float(expected_pu),float(expected_px)]})
    return {'role':'internal off-trajectory differential-equation controls',
            'oracle':'canonical proper-time KG with 60-digit S derivatives',
            'rows':rows}

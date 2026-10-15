"""Full-field local Einstein jets and metric-only necessary compatibility controls."""
from pathlib import Path
import json
import mpmath as mp

mp.mp.dps = 50


def constants(k):
    a = (1-k)*(1+3*k)/4
    return a, (1+k)/(k*(1-3*k)), a/(1-3*a)


def replaced(v, i, t):
    q = list(v)
    q[i] = t
    return q


def jordan(v, pars):
    z, x, y = v
    k, hv, nu = pars
    a, s, lam = constants(k)
    xx = s+z*z
    dd = 1+2*(1+k)*(x*x+y*y)/3
    coeff = [1/lam, (1+s)*z*z*4*k/(9*dd), (1+s)*z*z*k/(3*dd)]
    p0 = 3*hv*hv*(s+z**4)+hv*hv*nu*z**4*mp.log(z)**2/a
    ax = hv*hv*k*xx*xx*z**((1-k)/a)/(1+s)
    ay = 2*hv*hv*k*xx*xx*z**((1+k)/a)/(3*(1+s))
    return xx, coeff, p0+ax*x*x+ay*y*y


def einstein(v, pars):
    xx, q, pot = jordan(v, pars)
    hh = [2*q[i]/xx+(6*v[0]**2/xx**2 if i == 0 else 0) for i in range(3)]
    return hh, pot/(xx*xx)


def rhs(radius, state, pars):
    v, vel = state[:3], state[3:6]
    cc = state[6]
    hh, pot = einstein(v, pars)
    deriv = [[mp.diff(lambda t: einstein(replaced(v, j, t), pars)[0][i], v[j])
              for j in range(3)] for i in range(3)]
    grad = [mp.diff(lambda t: einstein(replaced(v, i, t), pars)[1], v[i]) for i in range(3)]
    kinetic = sum(hh[i]*vel[i]**2 for i in range(3))/2
    cp = (1-cc)/radius-radius*(cc*kinetic+pot)
    ap = (1-cc)/(2*radius*cc)+radius*(cc*kinetic-pot)/(2*cc)
    acc = []
    for i in range(3):
        connection = sum(deriv[i][j]*vel[i]*vel[j] for j in range(3))/hh[i]
        connection -= sum(deriv[j][i]*vel[j]**2 for j in range(3))/(2*hh[i])
        acc.append(-(2/radius+ap+cp/(2*cc))*vel[i]-connection+grad[i]/(cc*hh[i]))
    return list(vel)+acc+[cp, ap]


def local_jets(radius, state, pars):
    jets = [state, rhs(radius, state, pars)]
    for order in (2, 3):
        def poly(t):
            return [sum(jets[j][i]*t**j/mp.factorial(j) for j in range(len(jets))) for i in range(8)]
        jets.append([mp.diff(lambda t: rhs(radius+t, poly(t), pars)[i], 0, order-1) for i in range(8)])

    def poly(t):
        return [sum(jets[j][i]*t**j/mp.factorial(j) for j in range(4)) for i in range(8)]

    def radial(t):
        zz = poly(t)[0]
        return (radius+t)/mp.sqrt(constants(pars[0])[1]+zz*zz)

    def lapse(t):
        q = poly(t)
        return q[7]-mp.log(constants(pars[0])[1]+q[0]**2)/2

    def metric_b(t):
        q = poly(t)
        xx = constants(pars[0])[1]+q[0]**2
        return q[6]*(1-(radius+t)*q[0]*q[3]/xx)**2

    r1, r2, r3 = [mp.diff(radial, 0, i) for i in (1, 2, 3)]
    e1, e2, e3 = [mp.diff(lapse, 0, i) for i in (1, 2, 3)]
    b1, b2 = [mp.diff(metric_b, 0, i) for i in (1, 2)]
    metric = (radial(0), metric_b(0), b1/r1, b2/r1**2-b1*r2/r1**3,
              e1/r1, e2/r1**2-e1*r2/r1**3,
              e3/r1**3-3*e2*r2/r1**4-e1*r3/r1**4+3*e1*r2*r2/r1**5)
    vr = [jets[1][i]/r1 for i in range(3)]
    vrr = [jets[2][i]/r1**2-jets[1][i]*r2/r1**3 for i in range(3)]
    return metric, vr, vrr, r1


def metric_parts(metric):
    r, b, bp, bpp, e1, e2, e3 = metric
    gt = (b-1)/r**2+bp/r
    gr = (b-1)/r**2+2*b*e1/r
    ga = b*(e2+e1**2+e1/r)+bp*(e1+1/r)/2
    gap = bp*(e2+e1**2+e1/r)+b*(e3+2*e1*e2+e2/r-e1/r**2)
    gap += bpp*(e1+1/r)/2+bp*(e2-1/r**2)/2
    gtp = bpp/r-2*(b-1)/r**3
    dd = b*(1/r-e1)
    dp = bp*(1/r-e1)+b*(-1/r**2-e2)
    u = (ga-gt)/dd
    up = (gap-gtp)/dd-u*dp/dd
    hh = gr-gt-b*(up+u*u)-(bp/2-b*e1)*u
    ww = -gt-hh/2-b*(up+u*u)-(bp/2+2*b/r)*u
    return gt, gr, ga, u, up, hh, ww, -(gt+gr+2*ga)


def invert(metric, pars, trial_x):
    r, b, bp, bpp, e1, e2, e3 = metric
    k, hv, nu = pars
    values = list(metric)+list(pars)+[trial_x]
    if not all(mp.isfinite(t) and mp.im(t) == 0 for t in values):
        raise ValueError('finite real metric, parameters and trial amplitude required')
    if not (r > 0 and b > 0 and 0 < k < mp.mpf(1)/3 and hv > 0 and nu > 0):
        raise ValueError('outside positive annular candidate domain')
    if b*(1/r-e1) == 0 or trial_x <= constants(k)[1]:
        raise ValueError('singular angular chart or nonpositive scalar coordinate')
    a, s, lam = constants(k)
    gt, gr, ga, u, up, hh, ww, curv = metric_parts(metric)
    z = mp.sqrt(trial_x-s)
    zp = trial_x*u/(2*z)
    zpp = trial_x*(up+u*u)/(2*z)-trial_x**2*u*u/(4*z**3)
    lz = b*zpp+(bp/2+b*e1+2*b/r)*zp
    p0 = lambda t: 3*hv*hv*(s+t**4)+hv*hv*nu*t**4*mp.log(t)**2/a
    tt = trial_x*hh/2-b*zp*zp/lam
    delta = trial_x*ww-p0(z)
    ee = 2*lz/lam+z*curv-2*tt/z-mp.diff(p0, z)
    lx, ly = [4*z/trial_x+(1+sign*k)/(a*z) for sign in (-1, 1)]
    ux = (ly*delta-ee)/(ly-lx)
    uy = (ee-lx*delta)/(ly-lx)
    ax = hv*hv*k*trial_x**2*z**((1-k)/a)/(1+s)
    ay = 2*hv*hv*k*trial_x**2*z**((1+k)/a)/(3*(1+s))
    return dict(z=z, zp=zp, zpp=zpp, T=tt, Delta=delta, E=ee, lx=lx, ly=ly,
                Ux=ux, Uy=uy, x2=ux/ax, y2=uy/ay)


def controls(protocol_path):
    protocol = json.loads(Path(protocol_path).read_text())
    checks, cases = [], []

    def equal(name, actual, expected):
        error = abs(actual-expected)/max(1, abs(expected))
        checks.append(dict(name=name, passed=bool(error < mp.mpf('1e-35')), error=str(error)))

    for num, case in enumerate(protocol['fixed_cases']):
        pars = list(map(mp.mpf, (case['k'], case['Hv'], case['nu'])))
        radius, state = mp.mpf(case['R']), list(map(mp.mpf, case['state']))
        metric, vr, vrr, r1 = local_jets(radius, state, pars)
        xx, q, pot = jordan(state[:3], pars)
        rec = invert(metric, pars, xx)
        r, b, bp, _, e1, _, _ = metric
        gt, gr, ga, u, up, hh, ww, curv = metric_parts(metric)
        z = state[0]
        fp = 2*z*vr[0]
        fpp = 2*vr[0]**2+2*z*vrr[0]
        kinetic = sum(q[i]*vr[i]**2 for i in range(3))
        original = [xx*gt+b*kinetic+pot+b*fpp+(bp/2+2*b/r)*fp,
                    xx*gr-b*kinetic+pot+(b*e1+2*b/r)*fp,
                    xx*ga+b*kinetic+pot+b*fpp+(bp/2+b*e1+b/r)*fp]
        for i in range(3):
            li = b*vrr[i]+(bp/2+b*e1+2*b/r)*vr[i]
            dq = [mp.diff(lambda t: jordan(replaced(state[:3], j, t), pars)[1][i], state[j]) for j in range(3)]
            cross = sum(mp.diff(lambda t: jordan(replaced(state[:3], i, t), pars)[1][j], state[i])*vr[j]**2 for j in range(3))
            pv = mp.diff(lambda t: jordan(replaced(state[:3], i, t), pars)[2], state[i])
            residual = 2*q[i]*li+2*b*sum(dq[j]*vr[j]*vr[i] for j in range(3))-b*cross-pv
            if i == 0:
                residual += z*curv
            original.append(residual)
        for i, value in enumerate(original):
            equal(f'{num}:original_full_field_equation_{i}', value, 0)
        equal(f'{num}:recovered_x_squared', rec['x2'], state[1]**2)
        equal(f'{num}:recovered_y_squared', rec['y2'], state[2]**2)
        equal(f'{num}:recovered_transverse_kinetic', rec['T'], b*(q[1]*vr[1]**2+q[2]*vr[2]**2))
        equal(f'{num}:metric_scalar_first_derivative', rec['zp'], vr[0])
        equal(f'{num}:metric_scalar_second_derivative', rec['zpp'], vrr[0])
        checks.append(dict(name=f'{num}:strict_nonzero_transverse_chart', passed=bool(r1>0 and rec['T']>0 and rec['Delta']>0 and rec['lx']*rec['Delta']<rec['E']<rec['ly']*rec['Delta'])))
        cases.append({'case':case, 'metric_jets':[str(t) for t in metric], 'reconstructed':{k:str(v) for k,v in rec.items()}, 'original_equations':[str(t) for t in original]})
    # Deliberate domain refusals are separate from the two solution controls.
    good_metric = metric
    good_pars = pars
    good_x = xx
    for name, met, par, amp in [
        ('invalid_k', good_metric, [mp.mpf(0), good_pars[1], good_pars[2]], good_x),
        ('nonpositive_Hv', good_metric, [good_pars[0], mp.mpf(0), good_pars[2]], good_x),
        ('negative_nu', good_metric, [good_pars[0], good_pars[1], mp.mpf(-1)], good_x),
        ('zero_z', good_metric, good_pars, constants(good_pars[0])[1]),
        ('nan_amplitude', good_metric, good_pars, mp.nan),
        ('nonpositive_B', replaced(good_metric, 1, mp.mpf(0)), good_pars, good_x),
        ('singular_angular_chart', replaced(good_metric, 4, 1/good_metric[0]), good_pars, good_x),
    ]:
        refused = False
        try:
            invert(met, par, amp)
        except ValueError:
            refused = True
        checks.append(dict(name='domain:'+name, passed=refused))
    return dict(checks=checks, cases=cases, empirical_tests=0,
                scope='Two synthetic local full-field Einstein ODE jets, not a global trajectory, observed metric or physical parameter fit')

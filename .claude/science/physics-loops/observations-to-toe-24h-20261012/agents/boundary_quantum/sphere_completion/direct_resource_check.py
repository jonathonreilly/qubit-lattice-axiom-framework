#!/usr/bin/env python3
"""Independent finite checks for the directly derived angular-cusp theorem."""
import datetime as dt
import hashlib
import json
from pathlib import Path

import mpmath as mp

RUNTIME = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')


def main():
    mp.mp.dps = 65
    path = RUNTIME / 'quantum/direct_resource/resource_check_v1.json'
    assert not path.exists()
    source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    coefficients = []
    for n in range(10):
        ell = 2*n+1
        cn = mp.binomial(2*n, n) / 4**n
        exact = cn**2 * (4*n+3) / (4*(n+1)**2)
        # Direct Legendre integration is separate from the coefficient formula.
        integral = (2*ell+1) * mp.quad(lambda theta:
            (1-2*theta/mp.pi)*mp.legendre(ell,mp.cos(theta))*mp.sin(theta),
            [0,mp.pi/4,mp.pi/2])
        err = abs(integral/exact-1)
        assert err < mp.mpf('1e-50')
        coefficients.append({'l':ell,'coefficient':str(exact),'relative_error':str(err)})
    cusp = []
    for k in [mp.mpf('0'),mp.mpf('.1'),mp.mpf('.3')]:
        theta = mp.mpf('1e-20')
        u,t = 1-2*theta/mp.pi,mp.tanh(k*mp.cos(theta))
        value = (u+t)/(1+u*t)
        observed = (1-value)/theta
        exact = 2/mp.pi*mp.exp(-2*k)
        err = abs(observed/exact-1)
        assert err < mp.mpf('1e-19')
        cusp.append({'k':str(k),'slope':str(exact),'finite_theta_relative_error':str(err)})
    moments = []
    for count in [1,10,100,1000]:
        cn = mp.mpf(1)
        first = mp.mpf(0)
        total = mp.mpf(0)
        for n in range(count+1):
            nxt = cn*(2*n+1)/(2*n+2)
            weight = cn**2-nxt**2
            first += (2*n+1)*weight
            total += weight
            cn = nxt
        tail = cn**2
        assert abs(total+tail-1)<mp.mpf('1e-60')
        direct_telescoping = 1+2*mp.fsum((mp.binomial(2*n,n)/4**n)**2 for n in range(1,count+1))-(2*count+1)*tail
        assert abs(first-direct_telescoping)<mp.mpf('1e-58')
        assert 2*tail <= mp.mpf(2)/(count+2)
        moments.append({'N':count,'tail':str(tail),'first_moment':str(first)})
    assert hashlib.sha256(Path(__file__).read_bytes()).hexdigest()==source
    note=Path(__file__).with_name('DIRECT_RESOURCE_OBSTRUCTION.md')
    result={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':source,
            'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'passed':True,
            'coefficients':coefficients,'cusp':cusp,'moments':moments,
            'limits':'Finite independent formulas support the author all-order proof; no proof-assistant certification, universal resource lower bound or observational fit.'}
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'cusp':cusp,'moments':moments},indent=2))


if __name__=='__main__':
    main()

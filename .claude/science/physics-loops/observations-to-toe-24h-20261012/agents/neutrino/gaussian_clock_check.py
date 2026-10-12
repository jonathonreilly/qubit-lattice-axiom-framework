#!/usr/bin/env python3
"""Conditional scalar-vacuum clock filters; synthetic, not fitted observations.

Frozen example: C=s=ell=lambda=1, Gaussian spatial width a=.25 in natural units.
Static-Gaussian and white-noise rivals match the vacuum Ramsey exponent at T=1.
T=4 and the full fixed T list are synthetic diagnostics, not empirical holdouts.
Independent integration uses mass/momentum coordinates rather than frequency/mass.
"""
from __future__ import annotations
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[name] = "1"
import json
import math
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre, gamma, beta

ROOT=Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
C,S,ELL,LAMBDA,A = 1.,1.,1.,1.,.25
TIMES=(.25,.5,1.,2.,4.,8.,16.)


def gaussian_rule(n, high):
    x,w=roots_legendre(n)
    return (x+1)*high/2,w*high/2


def spectrum_factory(n, width):
    theta, weights=gaussian_rule(n,np.pi/2)
    si,co=np.sin(theta),np.cos(theta)
    base=weights*si**(S-1)*co**2
    def spectrum(omega):
        if omega<=0:return 0.
        return C*omega**(S+1)/(2*np.pi)*float(np.sum(base*np.exp(-ELL*omega*si-width**2*omega**2*co**2)))
    return spectrum


def filter_square(omega,t,echo):
    if omega==0:return 0. if echo else t*t
    if echo:return 16*np.sin(omega*t/4)**4/omega**2
    return 4*(np.sin(omega*t/2)/omega)**2


def exponent(spectrum,t,echo):
    val,err=quad(lambda w:spectrum(w)*filter_square(w,t,echo),0.,60.,epsabs=2e-10,epsrel=2e-10,limit=500)
    prefactor=LAMBDA**2/(4*np.pi)
    return val*prefactor,err*prefactor


def independent_momentum_exponent(n,t,echo):
    mu,wm=gaussian_rule(n,40.)
    k,wk=gaussian_rule(n,24.)
    energy=np.sqrt(mu[:,None]**2+k[None,:]**2)
    if echo: filt=16*np.sin(energy*t/4)**4/energy**2
    else: filt=4*(np.sin(energy*t/2)/energy)**2
    weight=(C*wm*mu**(S-1)*np.exp(-ELL*mu))[:,None]*(wk*k*k*np.exp(-A*A*k*k))[None,:]
    return float(LAMBDA**2/(8*np.pi**2)*np.sum(weight*filt/energy))


def main():
    for name in ("STOP_REQUESTED","USER_STOP_REQUESTED"):
        if (ROOT/name).exists():raise SystemExit("Campaign stop marker present")
    deadline=json.loads((ROOT/"DEADLINE.json").read_text())["deadline_epoch"]
    if datetime.now(timezone.utc).timestamp()>=deadline:raise SystemExit("Campaign deadline elapsed")
    spec=spectrum_factory(256,A)
    spec_coarse=spectrum_factory(128,A)
    point=spectrum_factory(256,0.)
    rows=[]
    max_order_change,max_estimated_error=0.,0.
    for t in TIMES:
        cr,er=exponent(spec,t,False)
        ce,ee=exponent(spec,t,True)
        max_order_change=max(max_order_change,abs(cr-exponent(spec_coarse,t,False)[0]),abs(ce-exponent(spec_coarse,t,True)[0]))
        max_estimated_error=max(max_estimated_error,er,ee)
        rows.append({"T":t,"chi_Ramsey":cr,"chi_echo":ce,"visibility_Ramsey":math.exp(-cr),"visibility_echo":math.exp(-ce)})
    match=next(r["chi_Ramsey"] for r in rows if r["T"]==1.)
    for row in rows:
        t=row["T"]
        row.update({"matched_static_Gaussian_chi_Ramsey":match*t*t,"matched_static_Gaussian_chi_echo":0.,
                    "matched_white_chi_Ramsey":match*t,"matched_white_chi_echo":match*t})
    comparisons=[]
    for t in (1.,4.):
        for echo in (False,True):
            direct=independent_momentum_exponent(256,t,echo)
            direct_fine=independent_momentum_exponent(512,t,echo)
            spectral=exponent(spec,t,echo)[0]
            comparisons.append({"T":t,"echo":echo,"mass_momentum_256":direct,"mass_momentum_512":direct_fine,
                                "mass_frequency":spectral,"difference":direct_fine-spectral,"momentum_order_change":direct_fine-direct})
    assert max(abs(r["difference"]) for r in comparisons)<1e-8
    assert max_order_change<1e-8
    low=.001
    low_leading=C*beta(S/2,1.5)/(4*np.pi)*low**(S+1)
    high=1000.
    high_leading=C*gamma(S)/ELL**S*high/(2*np.pi)
    # Analytic potential is independently compared with a mass-integral quadrature.
    potentials=[]
    for r in (.2,1.,4.):
        numeric=-quad(lambda mu:C*mu**(S-1)*math.exp(-(r+ELL)*mu),0.,np.inf)[0]/(4*np.pi*r)
        exact=-C*gamma(S)/(4*np.pi*r*(r+ELL)**S)
        assert abs(numeric-exact)<1e-11
        potentials.append({"r":r,"numeric_unit_charge_potential":numeric,"analytic":exact})
    plateau=LAMBDA**2/(2*np.pi)*quad(lambda w:spec(w)/w**2 if w else .125,0.,60.,epsabs=1e-11)[0]
    result={"scope":"Supplied Gaussian scalar vacuum and ideal clock coupling; synthetic calculation, no measured data or fit.",
            "parameters":{"C":C,"s":S,"ell":ELL,"lambda":LAMBDA,"spatial_gaussian_a":A},
            "rival_calibration":"Match Ramsey chi at T=1 only; fixed static-Gaussian and white rivals.",
            "point_spectrum_low_ratio_to_leading":point(low)/low_leading,
            "point_spectrum_high_ratio_to_leading":point(high)/high_leading,
            "quadrature_max_order_128_to_256_change":max_order_change,
            "maximum_adaptive_error_estimate":max_estimated_error,
            "vacuum_Ramsey_plateau":plateau,"vacuum_echo_plateau":3*plateau,
            "rows":rows,"independent_coordinate_checks":comparisons,"potential_checks":potentials}
    output=ROOT/"neutrino/gaussian_clock_results.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print("SYNTHETIC VACUUM CLOCK: C=s=ell=lambda=1, a=.25; no empirical fit")
    for row in rows:print("T={T:5.2f} chi_R={chi_Ramsey:.10f} chi_E={chi_echo:.10f} V_R={visibility_Ramsey:.10f} V_E={visibility_echo:.10f}".format(**row))
    print("Independent-coordinate max discrepancy:",max(abs(r["difference"]) for r in comparisons))
    print("Theta order-change max discrepancy:",max_order_change)
    print("Long-time chi plateaus:",plateau,3*plateau)
    print("Point-spectrum high-frequency ratio to linear asymptotic:",point(high)/high_leading)
    print("OUTPUT:",output)


if __name__=="__main__":main()

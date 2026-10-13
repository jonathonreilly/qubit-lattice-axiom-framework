#!/usr/bin/env python3
"""Frozen conditional inverse reconstruction; published PPN bridge is explicit."""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
CHECKS = []


def rat(x):
    return Fraction(str(x))


def val(x):
    f = rat(x)
    return mp.mpf(f.numerator) / f.denominator


def fmt(x):
    return mp.nstr(x, 80)


def check(name, passed, **detail):
    CHECKS.append(dict(name=name, passed=bool(passed), **detail))


def near(name, actual, expected, tol="1e-65"):
    error = abs(actual - expected) / max(mp.mpf(1), abs(expected))
    check(name, error <= mp.mpf(tol), actual=fmt(actual),
          expected=fmt(expected), normalized_error=fmt(error), tolerance=tol)


def domain(av, zv):
    a, z = rat(av), rat(zv)
    f, j = 1 + z, 1 + (1 - 3*a)*z
    return a > 0 and f > 0 and j > 0


def coupling_at_u(u, a, s):
    z = s * mp.exp(2*mp.sqrt(a)*u)
    j = 1 + (1 - 3*a)*z
    b = mp.exp(mp.sqrt(a)*u) / mp.sqrt(1+z)
    metric = j/(1+z)**2
    # Derive coupling from matter metric in the normalized scalar coordinate.
    log_b_prime = mp.diff(
        lambda w: mp.sqrt(a)*w - mp.log(1+s*mp.exp(2*mp.sqrt(a)*w))/2, u)
    return b, metric, log_b_prime/mp.sqrt(metric)


def direct(a, z):
    u = mp.mpf(0)
    b, metric, alpha = coupling_at_u(u, a, z)
    beta = mp.diff(lambda w: coupling_at_u(w, a, z)[2], u)/mp.sqrt(metric)
    k = alpha**2
    dg = -2*k/(1+k)
    db = beta*k/(2*(1+k)**2)
    eta = 4*db-dg
    gn = b*b*(1+k)  # normalized by 1/(8 pi q).
    dlog = mp.diff(lambda w: mp.log(
        coupling_at_u(w, a, z)[0]**2*(1+coupling_at_u(w, a, z)[2]**2)), u)/mp.sqrt(metric)
    return dict(k=k, beta_D=beta, delta_gamma=dg, delta_beta=db,
                eta=eta, G_N_ratio=gn, dlogG_dphi=dlog)


def formula(a, z):
    j = 1+(1-3*a)*z
    k = a/j
    beta = -a*(1-3*a)*z*(1+z)/j**2
    dg = -2*k/(1+k)
    db = beta*k/(2*(1+k)**2)
    return dict(k=k, beta_D=beta, delta_gamma=dg, delta_beta=db,
                eta=4*db-dg, G_N_ratio=(1+k)/(1+z),
                dlogG_dphi=2*mp.sqrt(k)*(1+beta/(1+k)))


def symbolic_checks():
    a, z = sp.symbols("a z", positive=True)
    j = 1+(1-3*a)*z
    k = a/j
    alpha = sp.sqrt(a)/sp.sqrt(j)
    dz_dphi = 2*sp.sqrt(a)*z*(1+z)/sp.sqrt(j)
    beta = sp.simplify(sp.diff(alpha,z)*dz_dphi)
    target = -a*(1-3*a)*z*(1+z)/j**2
    check("symbolic.beta", sp.simplify(beta-target)==0)
    kap = sp.symbols("kap", positive=True)
    inva = kap*(1+z)/(1+3*kap*z)
    check("symbolic.inverse_k", sp.factor(k.subs(a,inva)-kap)==0)
    check("symbolic.inverse_beta", sp.factor(beta.subs(a,inva)+kap*(1-3*kap)*z)==0)
    # Along fixed a,s, B^2=z/[s(1+z)]; derivative loses constant s.
    log_g_prime = sp.diff(sp.log(z/(1+z)*(1+k)),z)*dz_dphi
    check("symbolic.fixed_theory_G", sp.simplify(
        log_g_prime-2*alpha*(1+beta/(1+k)))==0)
    eta = 2*k*(1+k+beta)/(1+k)**2
    check("symbolic.eta_G_relation", sp.simplify(
        eta-alpha*log_g_prime/(1+k))==0)
    an = (1-kap)*(1+3*kap)/4
    zn = (1+kap)/(kap*(1-3*kap))
    # Substitute only after fixed-theory differentiation.
    second = sp.diff(log_g_prime,z)*dz_dphi
    substituted = sp.factor(second.subs({a:an,z:zn}, simultaneous=True))
    check("symbolic.null_second_G", sp.factor(substituted+32*kap/(1-3*kap))==0)
    nu = sp.symbols("nu", positive=True)
    mass = (nu*(1+z)+12*a*z)/j
    check("symbolic.origin_mass", sp.factor(
        mass.subs(a,inva)-nu-3*kap*z*(nu+4))==0)


def inverse(kv, zv):
    k, z = rat(kv), rat(zv)
    d = 1+3*k*z
    if k <= 0 or z <= -1 or d <= 0:
        return dict(k_label=kv,z_label=zv,status="excluded_inverse_domain")
    a = k*(1+z)/d
    if k == Fraction(1,3):
        return dict(k_label=kv,z_label=zv,status="degenerate_k_one_third",
                    a_exact=str(a), beta_D="0",delta_gamma="-0.5")
    km, zm, am = val(k), val(z), val(a)
    f = direct(am,zm)
    kir = -f["delta_gamma"]/(2+f["delta_gamma"])
    br = 2*(1+kir)**2*f["delta_beta"]/kir
    zr = -br/(kir*(1-3*kir))
    ar = kir*(1+zr)/(1+3*kir*zr)
    for name,actual,expected in [("k",kir,km),("beta_D",br,-km*(1-3*km)*zm),("z",zr,zm),("a",ar,am)]:
        near("inverse."+str(kv)+"."+str(zv)+"."+name,actual,expected)
    return dict(k_label=kv,z_label=zv,status="identified_local_a_z",
                a_exact=str(a),a=fmt(am),recovered_a=fmt(ar),recovered_z=fmt(zr),
                **{key:fmt(v) for key,v in f.items()})


def membership(f, obs, n):
    dg=val(f["delta_gamma"]); eta=val(f["eta"])
    gm,gs=val(obs["Cassini"]["mean"]),val(obs["Cassini"]["reported_uncertainty"])
    em,es=val(obs["LLR"]["mean"]),val(obs["LLR"]["reported_uncertainty"])
    return abs(dg-gm)<=n*gs, abs(eta-em)<=n*es


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--evidence",type=Path,required=True)
    args=ap.parse_args()
    protocol=json.loads((HERE/"PROTOCOL_v2.json").read_text())
    obs=json.loads((HERE/"OBSERVATION_INPUTS_v1.json").read_text())
    mp.mp.dps=protocol["precision_digits"]
    freeze=json.loads((args.evidence/"FREEZE.json").read_text())
    for item in freeze["inputs"]:
        p=Path(item["path"])
        check("source."+str(p),hashlib.sha256(p.read_bytes()).hexdigest()==item["sha256"])
    symbolic_checks()
    sa, sz = sp.symbols("a z", positive=True)
    sj = 1+(1-3*sa)*sz
    sk = sa/sj
    sbeta = -sa*(1-3*sa)*sz*(1+sz)/sj**2
    sd = 2*sp.sqrt(sa)*sz*(1+sz)/sp.sqrt(sj)
    deriv = 2*sp.sqrt(sk)*(1+sbeta/(1+sk))
    canonical_derivatives = []
    for order in range(2, 5):
        deriv = sp.factor(sp.diff(deriv, sz)*sd)
        canonical_derivatives.append(deriv)
    high_derivatives = sp.lambdify((sa,sz),canonical_derivatives[1:],"mpmath",cse=True)
    forward=[]
    for av in protocol["a_grid"]:
        for zv in protocol["z_grid"]:
            row=dict(a_label=av,z_label=zv,admitted=domain(av,zv))
            if row["admitted"]:
                a,z=val(av),val(zv)
                f=direct(a,z);g=formula(a,z)
                for name in f:near("forward."+av+"."+zv+"."+name,f[name],g[name])
                row.update({key:fmt(v) for key,v in f.items()})
                row["inverse_degenerate"]=rat(av)==Fraction(1,3)
            else:row["reason"]="outside positive tensor/scalar kinetic domain"
            forward.append(row)
    inverse_rows=[inverse(k,z) for k in protocol["inverse_k_grid"] for z in protocol["z_grid"]]
    singular=[
        dict(delta_gamma="0",status="GR_boundary_not_finite_positive_a"),
        dict(delta_gamma="2.1e-5",status="positive_central_value_outside_positive_k_model"),
        dict(delta_gamma="-2",status="singular_inverse_denominator"),
        dict(delta_gamma="-3",status="negative_reconstructed_k_outside_model")
    ]
    null=[]
    finite=[]
    for kv in protocol["null_k_grid"]:
        kr=rat(kv); ar=(1-kr)*(1+3*kr)/4; zr=(1+kr)/(kr*(1-3*kr))
        k,a,z=val(kr),val(ar),val(zr)
        f=direct(a,z)
        near("null."+kv+".eta",f["eta"],mp.mpf(0))
        near("null."+kv+".G_first",f["dlogG_dphi"],mp.mpf(0))
        near("null."+kv+".beta",f["beta_D"],-(1+k))
        check("null."+kv+".gamma_nonzero",f["delta_gamma"]<0)
        def logg(u):
            b,metric,alpha=coupling_at_u(u,a,z)
            return mp.log(b*b*(1+alpha*alpha))
        metric=coupling_at_u(mp.mpf(0),a,z)[1]
        metric_prime=mp.diff(lambda u:coupling_at_u(u,a,z)[1],0)
        second=mp.diff(logg,0,2)/metric-metric_prime*mp.diff(logg,0)/(2*metric**2)
        near("null."+kv+".G_second",second,-32*k/(1-3*k))
        check("null."+kv+".G_maximum",second<0)
        masses=[]
        for nv in protocol["nu_grid"]:
            nu=val(nv);m2=(nu*(1+z)+12*a*z)/(1+(1-3*a)*z)
            near("null."+kv+".mass."+nv,m2,nu+3*k*z*(nu+4))
            check("null."+kv+".mass_positive."+nv,m2>0)
            masses.append(dict(nu_label=nv,mass_squared=fmt(m2),
                length_diagnostics=[dict(Hv_L_over_c=x,mL_over_c=fmt(mp.sqrt(m2)*val(x)))
                    for x in protocol["dimensionless_length_grid"]]))
        row=dict(k_label=kv,a_exact=str(ar),z_exact=str(zr),a=fmt(a),z=fmt(z),
                 G_second=fmt(second),masses=masses,**{key:fmt(v) for key,v in f.items()})
        row["observation_bands"]=[dict(n=n,Cassini=membership(row,obs,n)[0],
            LLR=membership(row,obs,n)[1]) for n in protocol["observation_band_multiples"]]
        null.append(row)
        ha=1-3*a
        remaining=mp.quad(lambda r:mp.sqrt(r*r+ha)/(1+r*r),[0,1/mp.sqrt(z)])/mp.sqrt(a)
        y=mp.sqrt(1+ha*z)
        closed_remaining=(mp.atanh(1/y)-mp.sqrt(3*a)*mp.atanh(mp.sqrt(3*a)/y))/mp.sqrt(a)
        near("null.distance."+kv,remaining,closed_remaining)
        row["remaining_canonical_distance"]=fmt(remaining)
        row["distance_over_sqrt_k"]=fmt(remaining/mp.sqrt(k))
        third,fourth=high_derivatives(a,z)
        check("null.fd."+kv+".nonzero_Taylor_coefficients",third!=0 and fourth!=0)
        prior_errors=None
        for hs in protocol["finite_difference_steps"]:
            h=val(hs)*remaining
            check("null.fd."+kv+"."+hs+".inside_endpoint",0<h<remaining)
            def scalar_length(u):
                return mp.quad(lambda w:mp.sqrt(1+(1-3*a)*z*mp.exp(2*mp.sqrt(a)*w))/(1+z*mp.exp(2*mp.sqrt(a)*w)),[0,u])
            up=mp.findroot(lambda u:scalar_length(u)-h,
                           (h/mp.sqrt(metric),mp.mpf("1.05")*h/mp.sqrt(metric)))
            um=mp.findroot(lambda u:scalar_length(u)+h,
                           (-h/mp.sqrt(metric),-mp.mpf("1.05")*h/mp.sqrt(metric)))
            near("null.fd."+kv+"."+hs+".positive_coordinate",scalar_length(up),h)
            near("null.fd."+kv+"."+hs+".negative_coordinate",scalar_length(um),-h)
            first=(logg(up)-logg(um))/(2*h)
            curvature=(logg(up)-2*logg(0)+logg(um))/h**2
            errors=(abs(first),abs(curvature-second))
            first_leading=h*h*third/6
            second_leading=h*h*fourth/12
            near("null.fd."+kv+"."+hs+".first_Taylor",first/first_leading,mp.mpf(1),tol="0.01")
            near("null.fd."+kv+"."+hs+".second_Taylor",(curvature-second)/second_leading,mp.mpf(1),tol="0.01")
            if prior_errors is not None:
                for index,(error,prior) in enumerate(zip(errors,prior_errors)):
                    check("null.fd."+kv+"."+hs+".convergence."+str(index),error<prior/20 or error<mp.mpf("1e-60"))
            finite.append(dict(k_label=kv,step_fraction=hs,h=fmt(h),remaining=fmt(remaining),up=fmt(up),um=fmt(um),first=fmt(first),
                second=fmt(curvature),second_error=fmt(errors[1]),first_leading=fmt(first_leading),second_leading=fmt(second_leading)))
            prior_errors=errors
    bands=[]
    for n in protocol["observation_band_multiples"]:
        gm,gs=rat(obs["Cassini"]["mean"]),rat(obs["Cassini"]["reported_uncertainty"])
        em,es=rat(obs["LLR"]["mean"]),rat(obs["LLR"]["reported_uncertainty"])
        deficit=n*gs-gm; km=deficit/(2-deficit)
        k=rat(protocol["diagnostic_k"]); base=2*k/(1+k); dk=2*k*k*(1-3*k)/(1+k)**2
        zlo=(base-(em+n*es))/dk; zhi=(base-(em-n*es))/dk
        physical_lower=max(Fraction(-1),zlo)
        bands.append(dict(n=n,gamma_low_exact=str(gm-n*gs),gamma_high_exact=str(gm+n*gs),
            k_max_exact=str(km),k_max=fmt(val(km)),diagnostic_k=str(k),
            eta_low_exact=str(em-n*es),eta_high_exact=str(em+n*es),
            z_lower_unrestricted_exact=str(zlo),z_lower_physical_exact=str(physical_lower),
            z_lower_open=physical_lower==Fraction(-1),z_upper_exact=str(zhi),
            a_upper_exact=str(k*(1+zhi)/(1+3*k*zhi))))
        near("band."+str(n)+".gamma_endpoint",-2*val(km)/(1+val(km)),val(gm-n*gs))
        for label,zv,target in [("lower",zlo,em+n*es),("upper",zhi,em-n*es)]:
            near("band."+str(n)+"."+label,val(base-dk*zv),val(target))
    diagnostic=[]
    kr=rat(protocol["diagnostic_k"])
    for zv in protocol["diagnostic_z_grid"]:
        zr=rat(zv); ar=kr*(1+zr)/(1+3*kr*zr)
        f=direct(val(ar),val(zr))
        row=dict(k_label=str(kr),z_label=zv,a_exact=str(ar),
                 **{key:fmt(v) for key,v in f.items()})
        row["bands"]=[dict(n=n,Cassini=membership(row,obs,n)[0],LLR=membership(row,obs,n)[1])
                      for n in protocol["observation_band_multiples"]]
        row["compactness_diagnostics"]=[dict(U=uv,beta_D_times_U=fmt(abs(f["beta_D"])*val(uv)))
                                       for uv in protocol["compactness_grid"]]
        diagnostic.append(row)

    # Post-serialization checks bind values, row inclusion, classifications and flags.
    expected_keys={(a,z) for a in protocol["a_grid"] for z in protocol["z_grid"]}
    check("serialized.forward_census",{(x["a_label"],x["z_label"]) for x in forward}==expected_keys and len(forward)==len(expected_keys))
    for row in forward:
        av,zv=row["a_label"],row["z_label"]; admitted=domain(av,zv)
        check("serialized.forward.domain."+av+"."+zv,row["admitted"]==admitted)
        if admitted:
            g=formula(val(av),val(zv))
            for key,expected in g.items():near("serialized.forward."+av+"."+zv+"."+key,val(row[key]),expected)
            check("serialized.forward.degeneracy."+av+"."+zv,row["inverse_degenerate"]==(rat(av)==Fraction(1,3)))
        else:check("serialized.forward.exclusion."+av+"."+zv,"reason" in row and "k" not in row)
    check("serialized.inverse_census",{(x["k_label"],x["z_label"]) for x in inverse_rows}=={(k,z) for k in protocol["inverse_k_grid"] for z in protocol["z_grid"]} and len(inverse_rows)==len(protocol["inverse_k_grid"])*len(protocol["z_grid"]))
    for row in inverse_rows:
        k,z=rat(row["k_label"]),rat(row["z_label"])
        expected="excluded_inverse_domain" if k<=0 or z<=-1 or 1+3*k*z<=0 else ("degenerate_k_one_third" if k==Fraction(1,3) else "identified_local_a_z")
        check("serialized.inverse.status."+str(k)+"."+str(z),row["status"]==expected)
        if expected=="identified_local_a_z":
            near("serialized.inverse.a."+str(k)+"."+str(z),val(row["recovered_a"]),val(k*(1+z)/(1+3*k*z)))
            near("serialized.inverse.z."+str(k)+"."+str(z),val(row["recovered_z"]),val(z))
    check("serialized.null_census",[x["k_label"] for x in null]==protocol["null_k_grid"])
    for row in null:
        k=val(row["k_label"])
        near("serialized.null.eta."+row["k_label"],val(row["eta"]),0)
        near("serialized.null.second."+row["k_label"],val(row["G_second"]),-32*k/(1-3*k))
        check("serialized.null.mass_census."+row["k_label"],[x["nu_label"] for x in row["masses"]]==protocol["nu_grid"])
        for mass in row["masses"]:
            near("serialized.null.mass."+row["k_label"]+"."+mass["nu_label"],val(mass["mass_squared"]),val(mass["nu_label"])+3*k*val(row["z"])*(val(mass["nu_label"])+4))
        for band in row["observation_bands"]:
            c,l=membership(row,obs,band["n"])
            check("serialized.null.membership."+row["k_label"]+"."+str(band["n"]),band["Cassini"]==c and band["LLR"]==l)
    check("serialized.diagnostic_census",[x["z_label"] for x in diagnostic]==protocol["diagnostic_z_grid"])
    for row in diagnostic:
        for key,target in formula(val(row["a_exact"]),val(row["z_label"])).items():
            near("serialized.diagnostic."+row["z_label"]+"."+key,val(row[key]),target)
        for band in row["bands"]:
            c,l=membership(row,obs,band["n"])
            check("serialized.diagnostic.membership."+row["z_label"]+"."+str(band["n"]),band["Cassini"]==c and band["LLR"]==l)
    check("serialized.finite_census",{(x["k_label"],x["step_fraction"]) for x in finite}=={(k,h) for k in protocol["null_k_grid"] for h in protocol["finite_difference_steps"]} and len(finite)==len(protocol["null_k_grid"])*len(protocol["finite_difference_steps"]))
    for row in finite:
        check("serialized.finite.inside."+row["k_label"]+"."+row["step_fraction"],0<val(row["h"])<val(row["remaining"]))
    check("serialized.bands_census",[b["n"] for b in bands]==protocol["observation_band_multiples"])
    passed=sum(x["passed"] for x in CHECKS)
    out=dict(scope="Conditional model-specific inverse algebra; imported PPN response, exposed processed data only. No raw empirical likelihood or independent observation test.",
        forward=forward,inverse=inverse_rows,singular=singular,null_family=null,
        null_finite_differences=finite,observation_bands=bands,diagnostic=diagnostic,
        counts=dict(passed=passed,failed=len(CHECKS)-passed,total=len(CHECKS)),checks=CHECKS)
    with (args.evidence/"RESULTS.json").open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    print(json.dumps(out["counts"]))
    for c in CHECKS:
        if not c["passed"]:print(json.dumps(c))
    raise SystemExit(0 if passed==len(CHECKS) else 1)


if __name__=="__main__":
    main()

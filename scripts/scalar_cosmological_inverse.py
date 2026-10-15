"""Parent-authored conditional cosmological inverse; synthetic controls only."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import mpmath as mp

AUDIT_TIMEOUT_SEC = 120
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp


def metric_readout(row):
    """Reconstruct kinetic stress and potential from physical Jordan inputs."""
    F, Fd, Fdd = row["F"], row["Fdot"], row["Fddot"]
    H, Hd = row["H"], row["Hdot"]
    rho, pressure, curvature = row["rho"], row["pressure"], row["curvature"]
    if F <= 0:
        raise ValueError("positive tensor coefficient required")
    D = -2 * F * (Hd - curvature) - rho - pressure - Fdd + H * Fd
    V = F * (3 * H * H + Hd + 2 * curvature) - (rho - pressure) / 2
    V += Fdd / 2 + 2.5 * H * Fd
    result = {"D": D, "V": V}
    if Fd != 0:
        result["omega"] = F * D / Fd**2
        denominator = 2 * F * D + 3 * Fd**2
        result["q"] = Fd**2 / denominator if denominator != 0 else None
    return result


def kinetic_inverse(first, second):
    rows = [first, second]
    if any(row["F"] <= 0 or row["D"] <= 0 or row["Fdot"] == 0 for row in rows):
        raise ValueError("kinetic inverse requires positive F,D and changing F")
    Y1, Y2 = [row["Fdot"]**2 / row["D"] for row in rows]
    F1, F2 = first["F"], second["F"]
    if F1 == F2 or Y1 == Y2:
        raise ValueError("unresolved kinetic inverse denominator")
    coefficient = (F2 - F1) / (Y2 - Y1)
    Fc = F1 - coefficient * Y1
    if not (0 < coefficient < 0.5 and 0 < Fc < min(F1, F2)):
        raise ValueError("candidate kinetic parameter domain failed")
    ac = 1 / (2 * coefficient + 3)
    k = (1 - 2 * mp.sqrt(2 * coefficient / (2 * coefficient + 3))) / 3
    Q0 = 4 * ac * Fc / (1 + k)**2
    return {"c": coefficient, "Fc": Fc, "ac": ac, "k": k,
            "Q0": Q0, "Q": Q0 * (1 + k),
            "F_separation": abs(F2-F1), "Y_separation": abs(Y2-Y1)}


def potential_basis(F, parameters):
    k, Fc, ac = parameters["k"], parameters["Fc"], parameters["ac"]
    if F <= Fc:
        raise ValueError("F must lie above the candidate chart boundary")
    s = (1 + k) / (k * (1 - 3 * k))
    E = Fc / (s * (F - Fc))
    u = mp.log(E) / (2 * mp.sqrt(ac))
    W = 1 + s * E
    B0 = 1.5 + 1.5 * s * (E - 1)**2 / W**2
    B1 = (1 + s) * u * u / (2 * W**2)
    return u, B0, B1


def potential_inverse(first, second, parameters):
    bases = [potential_basis(row["F"], parameters)[1:] for row in [first, second]]
    (B01, B11), (B02, B12) = bases
    Z1, Z2 = [row["V"] / row["F"]**2 for row in [first, second]]
    determinant = B01*B12-B02*B11
    if determinant == 0:
        raise ValueError("potential basis has unresolved rank")
    L = (Z1*B12-Z2*B11)/determinant
    T = (B01*Z2-B02*Z1)/determinant
    if not (L > 0 and T > 0):
        raise ValueError("candidate potential coefficient positivity failed")
    return {"L": L, "T": T, "nu": T/L,
            "Hv": mp.sqrt(L * parameters["Q"] / 2),
            "determinant": determinant,
            "condition_number": float(np.linalg.cond(np.asarray(bases, dtype=float)))}


def reconstruction_residual(row, kinetics, potential):
    Fc, coefficient = kinetics["Fc"], kinetics["c"]
    if row["F"] <= Fc:
        raise ValueError("candidate history leaves reconstructed chart")
    _, B0, B1 = potential_basis(row["F"], kinetics)
    kinetic = row["D"] * (row["F"] - Fc) - coefficient * row["Fdot"]**2
    kinetic_scale = max(abs(row["D"] * (row["F"] - Fc)),
                        abs(coefficient * row["Fdot"]**2), 1e-30)
    Z = row["V"] / row["F"]**2
    potential_value = potential["L"] * B0 + potential["T"] * B1
    return {"kinetic_relative": float(kinetic / kinetic_scale),
            "potential_relative": float((Z-potential_value)/max(abs(Z), 1e-30))}


def source_model():
    """Differentiate the supplied Einstein action, before constructing readouts."""
    u, k, nu = sp.symbols("u k nu", real=True)
    ac = (1-k)*(1+3*k)/4
    alpha = sp.sqrt(ac)
    s = (1+k)/(k*(1-3*k))
    E = sp.exp(2*alpha*u)
    W = 1+s*E
    J = 1+(1-3*ac)*s*E
    K = J/W**2
    A = sp.sqrt((1+s)*E/W)
    b = alpha/W
    U = sp.Rational(3,2)+3*s*(E-1)**2/(2*W**2)+nu*(1+s)*u**2/(2*W**2)
    return sp.lambdify((u,k,nu), (K,sp.diff(K,u),A,b,sp.diff(b,u),U,sp.diff(U,u)), "numpy", cse=True)


def number(value):
    return mp.mpf(str(value))


def lift(row):
    return {key: number(value) for key, value in row.items()}


def readout_from_state(row, case):
    """Assemble metric inputs at the same saved states, using extra precision.

    rhoE and aE are recovered from the original saved rounded Jordan row. No
    original parameter answer is supplied to the downstream general inverse.
    """
    k, nu, Q0, Hv = [number(case[key]) for key in ['k', 'nu', 'Q0', 'Hv']]
    Q = Q0 * (1+k)
    u, velocity = number(row['source_u']), number(row['source_velocity'])
    rhoE = number(row['rho']) * number(row['source_A'])**4
    aE = number(row['aJ']) / number(row['source_A'])
    ac = (1-k)*(1+3*k)/4
    alpha = mp.sqrt(ac)
    s = (1+k)/(k*(1-3*k))
    E = mp.exp(2*alpha*u)
    Ep = 2*alpha*E
    W = 1+s*E
    Wp = s*Ep
    J = 1+(1-3*ac)*s*E
    Jp = (1-3*ac)*s*Ep
    K = J/W**2
    Ku = Jp/W**2-2*J*Wp/W**3
    A = mp.sqrt((1+s)*E/W)
    b = alpha/W
    bu = -alpha*Wp/W**2
    U = mp.mpf('1.5')+mp.mpf('1.5')*s*(E-1)**2/W**2+nu*(1+s)*u*u/(2*W**2)
    Uu = 3*s*(E-1)*Ep/W**2-3*s*(E-1)**2*Wp/W**3
    Uu += nu*(1+s)*(u/W**2-u*u*Wp/W**3)
    HE = mp.sqrt((K*velocity**2+2*Hv**2*U+rhoE/Q)/3)
    acceleration = -Ku*velocity**2/(2*K)-3*HE*velocity-Hv**2*Uu/K-b*rhoE/(2*Q*K)
    HEdot = -K*velocity**2-rhoE/(2*Q)
    F = Q/A**2
    Fdot = -2*F*b*velocity/A
    Fddot = -2*F/A**2*(b*acceleration+(bu-3*b*b)*velocity**2)
    H = (HE+b*velocity)/A
    Hdot = (HEdot+b*acceleration+(bu-b*b)*velocity**2-HE*b*velocity)/A**2
    return {'F':F, 'Fdot':Fdot, 'Fddot':Fddot, 'H':H, 'Hdot':Hdot,
            'rho':rhoE/A**4, 'pressure':mp.mpf(0), 'curvature':mp.mpf(0),
            'source_u':u, 'source_velocity':velocity, 'source_A':A,
            'source_D':2*F*(K-3*b*b)*(velocity/A)**2,
            'source_V':2*Q*Hv**2*U/A**4, 'source_q':b*b/K,
            'aJ':A*aE, 'timeE':number(row['timeE']), 'timeJ':number(row['timeJ'])}


def synthetic_history(case, evaluate):
    k, nu, Q0, Hv = [case[key] for key in ["k", "nu", "Q0", "Hv"]]
    Q = Q0*(1+k)

    def field_state(y):
        u, velocity, rhoE, aE, timeJ = y
        K, K_u, A, b, b_u, U, U_u = [float(z) for z in evaluate(u,k,nu)]
        HE = math.sqrt((K*velocity**2+2*Hv**2*U+rhoE/Q)/3)
        acceleration = -K_u*velocity**2/(2*K)-3*HE*velocity-Hv**2*U_u/K-b*rhoE/(2*Q*K)
        HEdot = -K*velocity**2-rhoE/(2*Q)
        return K,A,b,b_u,U,HE,acceleration,HEdot

    def ode(timeE, y):
        K,A,b,b_u,U,HE,acceleration,HEdot = field_state(y)
        u,velocity,rhoE,aE,timeJ = y
        return [velocity,acceleration,(-3*HE+b*velocity)*rhoE,HE*aE,A]

    end = case["duration_Hv"] / Hv
    initial = [case["u0"],case["velocity_over_Hv"]*Hv,
               case["rhoE_over_QHv2"]*Q*Hv**2,1.0,0.0]
    solution = solve_ivp(ode,[0,end],initial,method="DOP853",rtol=2e-12,atol=2e-14,dense_output=True,max_step=end/32)
    if not solution.success:
        raise RuntimeError(solution.message)

    def read_rounded(timeE):
        y = solution.sol(timeE)
        u,velocity,rhoE,aE,timeJ = [float(z) for z in y]
        K,A,b,b_u,U,HE,acceleration,HEdot = field_state(y)
        F = Q/A**2
        Fdot = -2*F*b*velocity/A
        Fddot = -2*F/A**2*(b*acceleration+(b_u-3*b*b)*velocity**2)
        H = (HE+b*velocity)/A
        Hdot = (HEdot+b*acceleration+(b_u-b*b)*velocity**2-HE*b*velocity)/A**2
        row = {"timeE":float(timeE),"timeJ":timeJ,"aJ":A*aE,
               "H":float(H),"Hdot":float(Hdot),"F":float(F),
               "Fdot":float(Fdot),"Fddot":float(Fddot),
               "rho":float(rhoE/A**4),"pressure":0.0,"curvature":0.0,
               "source_u":u,"source_velocity":velocity,"source_A":A,
               "source_D":float(2*F*(K-3*b*b)*(velocity/A)**2),
               "source_V":float(2*Q*Hv**2*U/A**4),"source_q":float(b*b/K)}
        row.update(metric_readout(row))
        return row

    def read(timeE):
        # Double-precision trajectory; higher precision only assembles the ideal
        # model-generated metric inputs and inverse. This creates no observed digits.
        row = readout_from_state(read_rounded(timeE), case)
        row.update(metric_readout(row))
        return row

    sample_times = np.linspace(0,end,17)
    rows = [read(t) for t in sample_times]
    rounded_rows = []
    for timeE in sample_times:
        row = lift(read_rounded(timeE))
        row.update(metric_readout(row))
        rounded_rows.append(row)
    rounded_kinetic = kinetic_inverse(rounded_rows[0], rounded_rows[6])
    rounded_potential = potential_inverse(rounded_rows[0], rounded_rows[6], rounded_kinetic)
    rounded_errors = {key:abs((rounded_kinetic if key in rounded_kinetic else rounded_potential)[key]/number(case[key])-1) for key in ["k","Q0","nu","Hv"]}
    kinetic = kinetic_inverse(rows[0],rows[6])
    potential = potential_inverse(rows[0],rows[6],kinetic)
    residuals = [reconstruction_residual(row,kinetic,potential) for row in rows[7:]]
    midpoint = end/2
    h = end/1000
    points = [read(midpoint+i*h) for i in [-2,-1,0,1,2]]
    def derivative(key):
        return (points[0][key]-8*points[1][key]+8*points[3][key]-points[4][key])/(12*h)/points[2]["source_A"]
    derivative_errors = {"Hdot":abs(derivative("H")-points[2]["Hdot"]),
                         "Fddot":abs(derivative("Fdot")-points[2]["Fddot"])}
    return {"case":case,"rows":rows,"kinetic_inverse":kinetic,"potential_inverse":potential,
            "later_synthetic_residuals":residuals,"derivative_errors":derivative_errors,
            "rounded_readout_recovery_errors":rounded_errors,
            "readout_precision_digits":mp.mp.dps,
            "solver":{"method":"DOP853","rtol":2e-12,"atol":2e-14,"nfev":solution.nfev}}


def exact_controls():
    controls = []
    def zero(name, expression):
        residual = sp.factor(sp.cancel(expression))
        controls.append({"name":name,"passed":residual==0,"residual":str(residual)})

    F,Fd,Fdd,Fddd,H,Hd,Hdd,C,rho,p,pd = sp.symbols("F Fd Fdd Fddd H Hd Hdd C rho p pd", nonzero=True)
    D = -2*F*(Hd-C)-rho-p-Fdd+H*Fd
    V = F*(3*H**2+Hd+2*C)-(rho-p)/2+Fdd/2+sp.Rational(5,2)*H*Fd
    zero("first_metric_reconstruction",3*F*(H**2+C)-rho-D/2-V+3*H*Fd)
    zero("second_metric_reconstruction",-2*F*(Hd-C)-rho-p-D-Fdd+H*Fd)
    velocities = {F:Fd,Fd:Fdd,Fdd:Fddd,H:Hd,Hd:Hdd,C:-2*H*C,rho:-3*H*(rho+p),p:pd}
    derivative = lambda expression: sum(sp.diff(expression,x)*v for x,v in velocities.items())
    omega = F*D/Fd**2
    scalar = (2*omega+3)*(Fdd+3*H*Fd)-(rho-3*p)+2*F*derivative(V)/Fd-4*V+derivative(omega)*Fd
    zero("Bianchi_scalar_equation_nonzero_Fdot",scalar)

    k,E,Q = sp.symbols("k E Q", positive=True)
    ac = (1-k)*(1+3*k)/4
    s = (1+k)/(k*(1-3*k))
    W,J = 1+s*E,1+(1-3*ac)*s*E
    tensor = Q*W/((1+s)*E)
    Fc = Q*s/(1+s)
    q = ac/J
    b2 = ac/W**2
    K = J/W**2
    c = (1-3*ac)/(2*ac)
    zero("candidate_tensor_chart",tensor-Fc-Q/((1+s)*E))
    zero("candidate_coupling_geometry",q-ac*(tensor-Fc)/(tensor-3*ac*Fc))
    zero("candidate_Jordan_kinetic",(K-3*b2)/(2*b2)-c*tensor/(tensor-Fc))
    zero("candidate_Fc_normalization",Fc-Q*(1+k)/(4*ac))
    zero("shape_inverse_ac",ac-1/(2*c+3))
    zero("shape_inverse_k_squared",(1-3*k)**2-8*c/(2*c+3))

    u,nu,Hv = sp.symbols("u nu Hv", real=True)
    B0 = sp.Rational(3,2)+3*s*(E-1)**2/(2*W**2)
    B1 = (1+s)*u**2/(2*W**2)
    physical_C = (1+s)*E/W
    zero("potential_conformal_basis",2*Q*Hv**2*(B0+nu*B1)/physical_C**2/tensor**2-2*Hv**2/Q*(B0+nu*B1))

    F1,F2,Y1,Y2,c0,boundary = sp.symbols("F1 F2 Y1 Y2 c0 boundary", nonzero=True)
    reconstruction_c = (F2-F1)/(Y2-Y1)
    substitution = {Y1:(F1-boundary)/c0,Y2:(F2-boundary)/c0}
    zero("two_point_c_inverse",reconstruction_c.subs(substitution)-c0)
    zero("two_point_boundary_inverse",(F1-reconstruction_c*Y1).subs(substitution)-boundary)

    B01,B02,B11,B12,L,T = sp.symbols("B01 B02 B11 B12 L T")
    determinant = B01*B12-B02*B11
    Z1,Z2 = L*B01+T*B11,L*B02+T*B12
    zero("two_basis_L_inverse",(Z1*B12-Z2*B11)/determinant-L)
    zero("two_basis_T_inverse",(B01*Z2-B02*Z1)/determinant-T)

    t = sp.symbols("t", positive=True)
    power = {F:t,Fd:1,Fdd:0,H:1/t,Hd:-1/t**2,C:0,rho:0,p:0}
    zero("generic_healthy_powerlaw_D",D.subs(power)-3/t)
    zero("generic_healthy_powerlaw_V",V.subs(power)-sp.Rational(9,2)/t)
    zero("plateau_metric_D",D.subs({Fd:0,Fdd:0,Hd:-(rho+p)/(2*F)+C}))

    Fsrc,Fmid,Fobs = sp.symbols("Fsrc Fmid Fobs", positive=True)
    zero("smooth_endpoint_telescope",sp.sqrt(Fsrc/Fmid)*sp.sqrt(Fmid/Fobs)-sp.sqrt(Fsrc/Fobs))
    zero("equal_endpoint_cancellation",(sp.sqrt(Fsrc/Fmid)*sp.sqrt(Fmid/Fobs)).subs(Fobs,Fsrc)-1)
    reflection = (Fsrc-Fmid)/(Fsrc+Fmid)
    transmission = 2*Fsrc/(Fsrc+Fmid)
    zero("sharp_interface_flux_conservation",reflection**2+(Fmid/Fsrc)*transmission**2-1)

    # A conformal background transformation of Raychaudhuri independently fixes D.
    g,gd,rp,A = sp.symbols("g gd rp A", real=True, nonzero=True)
    kinetic_E_over_A2 = -(Hd+gd/2)+(g/2)*(H+g/2)-rp/(2*F)+C
    jordan_D = 2*F*(kinetic_E_over_A2-sp.Rational(3,4)*g*g)
    zero("Einstein_Raychaudhuri_conformal_readout",jordan_D-D.subs({Fd:F*g,Fdd:F*(gd+g*g),rho:rp-p}))
    x, y, Hv2 = sp.symbols("x y Hv2", real=True)
    u = sp.symbols("u", real=True)
    alpha = sp.sqrt(ac)
    transverse_denominator = 1+sp.Rational(2,3)*(1+k)*(x*x+y*y)
    Kxx = (1+s)*4*k/(9*W*transverse_denominator)
    Kyy = (1+s)*k/(3*W*transverse_denominator)
    Uxy = k*x*x*sp.exp(-(1-k)*u/alpha)/2+k*y*y*sp.exp(-(1+k)*u/alpha)/3
    zero("transverse_connection_x_uu",-sp.diff(K,x)/(2*Kxx))
    zero("transverse_connection_y_uu",-sp.diff(K,y)/(2*Kyy))
    zero("transverse_source_x",sp.diff(physical_C,x))
    zero("transverse_source_y",sp.diff(physical_C,y))
    zero("transverse_x_stationary_equation",sp.diff(Uxy,x)-k*x*sp.exp(-(1-k)*u/alpha))
    zero("transverse_y_stationary_equation",sp.diff(Uxy,y)-sp.Rational(2,3)*k*y*sp.exp(-(1+k)*u/alpha))
    Tperp, Fvelocity = sp.symbols("Tperp Fvelocity", nonzero=True)
    radial_D = c*Fvelocity**2/(tensor-Fc)
    full_D = radial_D+2*tensor*Tperp
    inverse_qrec = 2*tensor*full_D/Fvelocity**2+3
    zero("background_geometric_coupling_distinction",inverse_qrec-1/q-4*tensor**2*Tperp/Fvelocity**2)
    return controls


def _run(protocol):
    checks = exact_controls()
    def check(name, passed, detail):
        checks.append({"name":name,"passed":bool(passed),"detail":detail})
    curved = metric_readout({"F":mp.mpf(2), "Fdot":mp.mpf(1), "Fddot":mp.mpf(0),
                             "H":mp.mpf(".5"), "Hdot":mp.mpf("-.25"),
                             "rho":mp.mpf(0), "pressure":mp.mpf(0), "curvature":mp.mpf(".5")})
    check("implemented_curved_manufactured_history",
          curved["D"]==mp.mpf("3.5") and curved["V"]==mp.mpf("4.25")
          and abs(curved["q"]-mp.mpf(1)/17)<mp.mpf("1e-45"),curved)
    matter = metric_readout({"F":mp.mpf(2), "Fdot":mp.mpf(1), "Fddot":mp.mpf(0),
                             "H":mp.mpf(".5"), "Hdot":mp.mpf("-.25"),
                             "rho":mp.mpf(".3"), "pressure":mp.mpf(".1"), "curvature":mp.mpf(".5")})
    check("implemented_nonzero_pressure_metric",
          abs(matter["D"]-mp.mpf("3.1"))<mp.mpf("1e-45")
          and abs(matter["V"]-mp.mpf("4.15"))<mp.mpf("1e-45"),matter)
    evaluate = source_model()
    histories = []
    for index,case in enumerate(protocol["synthetic_cases"]):
        result = synthetic_history(case,evaluate)
        histories.append(result)
        rows,ki,pi = result["rows"],result["kinetic_inverse"],result["potential_inverse"]
        errors = {key:abs((ki if key in ki else pi)[key]-case[key])/abs(case[key]) for key in ["k","Q0","nu","Hv"]}
        check(f"case{index}_parameter_recovery",max(errors.values())<protocol["parameter_relative_tolerance"],errors)
        closure = {"D":max(abs(row["D"]-row["source_D"])/abs(row["source_D"]) for row in rows),
                   "V":max(abs(row["V"]-row["source_V"])/abs(row["source_V"]) for row in rows),
                   "q":max(abs(row["q"]-row["source_q"])/abs(row["source_q"]) for row in rows)}
        check(f"case{index}_action_metric_closure",max(closure.values())<1e-8,closure)
        residual = max(abs(v) for r in result["later_synthetic_residuals"] for v in r.values())
        check(f"case{index}_later_synthetic_residuals",residual<protocol["residual_relative_tolerance"],residual)
        check(f"case{index}_Jordan_clock_derivatives",max(result["derivative_errors"].values())<5e-7,result["derivative_errors"])
        check(f"case{index}_nonzero_monotone_domain",all(row["Fdot"]*rows[0]["Fdot"]>0 and row["D"]>0 for row in rows),[row["Fdot"] for row in rows])

    representative = histories[1]
    rows = representative["rows"]
    for label,first,second in [
        ("equal_epochs",rows[0],rows[0]),
        ("zero_Fdot",{**rows[0],"Fdot":0},rows[6]),
        ("nonpositive_D",{**rows[0],"D":-1},rows[6])]:
        try:
            kinetic_inverse(first,second)
            refused = False
        except ValueError:
            refused = True
        check("domain_"+label,refused,{"required":"explicit refusal"})
    try:
        kinetic_inverse({"F":1.0,"Fdot":1.0,"D":3.0},{"F":2.0,"Fdot":1.0,"D":1.5})
        refused=False
    except ValueError:
        refused=True
    check("healthy_general_action_outside_candidate",refused,{"candidate_c_would_be":3})

    ki,pi = representative["kinetic_inverse"],representative["potential_inverse"]
    for factor in [0.25,3.0,11.0]:
        changed=[{**row,**{key:factor*row[key] for key in ["F","Fdot","Fddot","rho","pressure","D","V"]}} for row in rows]
        new_k = kinetic_inverse(changed[0],changed[6])
        new_p = potential_inverse(changed[0],changed[6],new_k)
        errors=[abs(new_k["k"]-ki["k"]),abs(new_p["Hv"]-pi["Hv"]),abs(new_p["nu"]-pi["nu"]),abs(new_k["Q0"]/(factor*ki["Q0"])-1)]
        check(f"normalization_family_{factor}",max(errors)<1e-7,{"errors":errors,"Q0_scale":factor})

    # Transverse velocities add positive kinetic stress; the exact inverse is no longer justified.
    transverse_rows=[]
    for row in rows:
        extra = 0.07*row["F"]
        minimum=ki["c"]*row["Fdot"]**2/(row["F"]-ki["Fc"])
        transverse_rows.append({"full_D":row["D"]+extra,"minimum":minimum,"gap":row["D"]+extra-minimum})
    check("transverse_positive_gap",min(x["gap"] for x in transverse_rows)>0,transverse_rows)
    check("sharp_transition_not_geometric_optics",abs(2/(1+4)-math.sqrt(1/4))>0.05,{"sharp_amplitude":0.4,"geometric_optics_amplitude":0.5})
    check("vacuum_potential_rank_failure",np.linalg.det(np.array([[1.5,0.0],[1.5,0.0]]))==0,{"nu_information":False})
    failed_case = histories[9]
    check("rounded_measurements_do_not_gain_information_from_precision",
          failed_case["rounded_readout_recovery_errors"]["nu"] > protocol["parameter_relative_tolerance"],
          {"relative_nu_error":failed_case["rounded_readout_recovery_errors"]["nu"],
           "interpretation":"The original numerical failure remains; more arithmetic precision cannot restore information lost in rounded input functions."})
    try:
        potential_inverse(rows[0],rows[0],ki)
        refused=False
    except ValueError:
        refused=True
    check("repeated_potential_epoch_refused",refused,{"same_epoch_rank":1})
    return {"status":"conditional_synthetic_reconstruction","passed":sum(x["passed"] for x in checks),
            "failed":sum(not x["passed"] for x in checks),"checks":checks,"histories":histories,
            "independent_empirical_tests":0,"physical_input_functions_acquired":False,
            "interpretation":"Parameter reconstruction inside a supplied action class from exact-model synthetic readouts, not observed action or state selection."}



def run(protocol):
    with mp.workdps(50):
        return _run(protocol)


def decimal_json(value):
    if isinstance(value, mp.mpf):
        return mp.nstr(value,55)
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(type(value).__name__)

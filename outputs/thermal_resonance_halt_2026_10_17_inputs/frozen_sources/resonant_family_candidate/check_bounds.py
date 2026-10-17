"""New author-owned exact scalar corroboration, not an independent theorem review.

No prior scientific program is imported or executed. Analytic contour, BV and
operator hypotheses remain proof obligations of CANDIDATE.md. No parameter grid,
quadrature, matrix or dynamics computation occurs here.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
from datetime import datetime, timezone
import argparse
import json
import resource
import sys
import time

p=argparse.ArgumentParser()
p.add_argument("--packet-root", required=True)
p.add_argument("--prelaunch", required=True)
a=p.parse_args()
D=Path(a.packet_root).resolve()
prepath=Path(a.prelaunch).resolve()
pre=json.loads(prepath.read_text())
started=time.monotonic()
out={"status":"running", "started_utc":datetime.now(timezone.utc).isoformat(),
     "independence":"author corroboration only; no prior checker import/replay",
     "checks":{}, "values":{}, "failed_routes":{}, "resources":{}}

def ident(path):
    st=path.stat()
    return {"sha256":sha256(path.read_bytes()).hexdigest(),"bytes":st.st_size,
            "device":st.st_dev,"inode":st.st_ino,"mtime_ns":st.st_mtime_ns}

def val(name,x):
    out["values"][name]={"rational":str(x),"display_float":float(x)}
    return x

def ck(name,test):
    out["checks"][name]=bool(test)
    if not test:
        raise AssertionError(name)

def zadd(a,b): return (a[0]+b[0],a[1]+b[1])
def zsub(a,b): return (a[0]-b[0],a[1]-b[1])
def zmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zdiv(a,b):
    den=b[0]*b[0]+b[1]*b[1]
    return ((a[0]*b[0]+a[1]*b[1])/den,(a[1]*b[0]-a[0]*b[1])/den)
def zs(z): return [str(z[0]),str(z[1])]

try:
    for entry in pre["bindings"]:
        path=Path(entry["path"])
        if not path.is_absolute(): path=D/path
        ck("binding:"+entry["label"],ident(path)==entry["identity"])
    ck("cpu_limit_is_predeclared",resource.getrlimit(resource.RLIMIT_CPU)==(20,21))
    source_manifest=json.loads((D/"SOURCE_MANIFEST.json").read_text())
    for entry in source_manifest["entries"]:
        raw=(D/entry["snapshot"]).read_bytes()
        ck("snapshot:"+entry["snapshot"],sha256(raw).hexdigest()==entry["sha256"] and len(raw)==entry["bytes"])
    data={k:F(v) for k,v in json.loads((D/"SCALAR_INPUTS.json").read_text()).items()}
    point=json.loads((D/"inputs/interval.json").read_text())["exact_parameters"]
    J=F(point["J"]); sn=F(point["sin_k"]); cs=F(point["cos_k"])
    lo=data["kappa_low"]; hi=data["kappa_high"]; sig=data["sigma"]; v=data["v"]
    eps=data["epsilon"]; ninv=data["N_inverse_upper"]; sv=data["sqrt_v_lower"]
    off=data["off_diagonal_integrated_upper"]
    ck("exact_unit_circle",sn*sn+cs*cs==1)
    v0=val("v0",2*J*sn)
    b0=val("b0",4*sn*cs)
    sinphi=2*sn*cs; cosphi=cs*cs-sn*sn
    sigmare=val("Sigma0_real",-2*cosphi*sinphi/v0)
    sigmaim=val("Sigma0_imag",-2*sinphi*sinphi/v0)
    ck("Sigma0_modulus_identity",sigmare*sigmare+sigmaim*sigmaim==(b0/v0)**2)
    ck("Sigma0_imag_identity",-sigmaim==b0*b0/(2*v0))
    ck("center_velocity_interval",v<v0<F(3,100))
    ck("form_factor_interval",F(3,2)<b0<2)
    ck("curvature_ratio",2*J/v<F(5,2))
    ck("sqrt_velocity_surrogate",0<sv and sv*sv<v)
    ck("Gamma_coefficient",-sigmaim>19)
    ck("pole_horizontal_bound",abs(sigmare/v0)<3200)
    ck("pole_vertical_bound",-sigmaim/v0<3200)
    ck("all_poles_inside_rectangle",3200*hi*hi<sig/4)
    ck("pole_decay_coefficient",v*(-sigmaim)/v0>F(125,4)>30)
    ck("denominator_q_ratio",(1+2/b0)/v0<100)
    drel=val("denominator_relative_upper",100*(J*sig+560*hi*hi))
    ck("uniform_denominator_relative",drel<eps==4*sig)
    rin=val("incoming_pointwise_relative",(18*sig+eps)/(1-eps))
    rout=val("outgoing_pointwise_relative",(20*sig+eps)/(1-eps))
    eta=F(4,3)*sig
    ck("incoming_L2_floor",ninv*rin<30*sig)
    ck("outgoing_L2_floor",ninv*rout+4*eta*eta<30*sig)
    rd=val("density_relative",(36*sig+(18*sig)**2+2*eps+eps*eps)/(1-eps)**2)
    ck("density_relative_rounding",rd<45*sig)
    density_error=val("density_L1_floor",45*sig*ninv+16*hi*hi/(v*v*sig))
    ck("density_cutoff_kept",density_error<50*sig)
    Bstar=data["Bstar"]
    ck("real_affine_range",F(3,100)*sig+(2/v)*hi*hi<Bstar)
    logarg=val("max_log_argument",1+2*Bstar/(19*lo*lo))
    ck("exact_log_majorant",logarg<F(8,3)**40)
    ck("H0_coefficient",(2/v)*40==3200)
    ck("F0_coefficient",3200/(1-eps)<4000)
    # Total variation includes the two outer endpoint jumps: 8+8+4=20.
    tv_terms=[F(8),F(8),F(4)]
    ck("cutoff_total_variation",sum(tv_terms)==20)
    ck("cutoff_curvature_coefficient",F(5,2)*4==10)
    out["values"]["cutoff_TV_coefficients"]={"cutoff_derivative":"8", "rational_derivative":"8", "two_outer_endpoint_jumps":"4"}
    Tmin=val("minimum_onset",1/(hi*hi))
    Tmax=val("maximum_onset",1/(lo*lo))
    ck("halfline_sum_regime",v*Tmin>1)
    ck("finite_bottom_regime",v*sig*Tmin>1)
    pole=val("uniform_pole_ceiling",2*F(3,8)**30)
    half=val("uniform_directional_cutoff_plus_vertical",hi*hi/(v*sv)*(24/sig+10))
    sqsig=F(1,1000)
    ck("exact_sqrt_sigma",sqsig*sqsig==sig)
    bottom=val("uniform_incoming_bottom",hi**3/(v*v*sig*sqsig))
    qin=val("qin",30*sig+half+bottom)
    qout=val("qout",30*sig+half+2*bottom+pole)
    ck("actual_halfline_normalization_exists",qout<F(1,2))
    density_edges=val("uniform_density_contour_edges",12*hi**4/(v**3*sig*sig))
    ae=val("emitter_reference_amplitude",50*sig+pole+density_edges)
    sf=val("scalar_incoming_amplitude",1600*hi*rin+hi**3/(v*v)*(13/sig+5))
    cg0=val("constant_background_clock",31*sf)
    cgvar=val("varying_background_clock",2700*sig*2000*hi)
    kloc0=val("constant_localized_response_clock",hi*20000*ae)
    klocvar=val("varying_localized_response_clock",hi*1000000*sig)
    klocerr=val("all_emitter_error_coordinates_clock",hi*20000*(4*sig+off))
    clockcol=val("localized_clock_per_column",cg0+cgvar+kloc0+klocvar+klocerr)
    clockop=val("localized_clock_operator",F(3,2)*clockcol)
    emitterop=val("full_emitter_operator",ae+F(3,2)*(4*sig+off))
    loc=val("complete_localized_operator",clockop+emitterop)
    remainder=val("complete_escape_remainder",qin+qout+loc)
    ck("proposed_remainder",remainder<data["proposed_escape_remainder_upper"])
    total=val("complete_infinite_upper_expression",data["complete_seed_error"]+data["complete_reflection_error"]+remainder)
    ck("proposed_infinite_error",total<data["proposed_infinite_error_upper"])
    ck("proposed_trace_error",2*total<2*data["proposed_infinite_error_upper"])
    # For arbitrary real kappa the ceiling M>=50T, not integrality of T, is used.
    buffer=val("minimum_finite_buffer",(data["clock_extent_factor"]-data["observation_time_factor"]*data["prepared_sector_radius"]*F(6,5))*Tmin-(data["L"]+1)-9)
    ck("finite_graph_distance_buffer",buffer>0)
    finiteextra=val("finite_extra",F(32,5)*F(3,8)**9)
    ck("finite_extra_rounding",finiteextra<F(1,1000))
    val("complete_finite_upper_expression",total+finiteextra)
    ck("proposed_finite_error",total+finiteextra<data["proposed_finite_error_upper"])
    val("upper_coupling_clock_sites",50*Tmin)
    val("lower_coupling_clock_sites",50*Tmax)
    E0=val("E0",2*J*(1-cs))
    ck("positive_emitter_onsite_all_family",E0>2*hi)
    val("maximum_new_emitter_incident_load",E0+2*hi)
    val("maximum_added_attachment_incident_load",3*hi)
    val("actual_scalar_upper_endpoint",F(point["scalar_reserve"])+2*hi)
    val("actual_scalar_lower_endpoint",F(point["scalar_reserve"])+2*lo)
    # Concrete rejected proof routes, not physical counterexamples.
    old_cut=val("failed_old_cutoff_L2_single",4*hi/(v*sqsig))
    old_clock=val("failed_old_absolute_clock",153000*hi)
    ck("naive_substitution_misses_004",data["complete_seed_error"]+data["complete_reflection_error"]+2*old_cut+old_clock>F(1,250))
    ck("scalar_not_halfline_required",F(3,2)*31*30*sig>F(1,250)-data["complete_seed_error"]-data["complete_reflection_error"])
    one=(F(1),F(0)); im=(F(0),F(1)); Dz=(F(1),F(1)); Dzbar=(F(1),F(-1))
    tminus=zsub(one,zdiv((F(0),F(2)),Dz))
    correct=zsub(tminus,zdiv(Dzbar,Dz)); wrong=zsub(tminus,zdiv(Dz,Dzbar))
    ck("correct_phase_discriminator",correct==(F(0),F(0)))
    ck("wrong_reciprocal_discriminator",wrong==(F(0),F(-2)))
    out["failed_routes"]["reciprocal_phase"]={"correct_residual":zs(correct),"wrong_residual":zs(wrong)}
    # Integral_0^pi exp(-ik) dk=(exp(-i*pi)-1)/(-i)=-2i.
    endpoint_integral=zdiv((F(-2),F(0)),(F(0),F(-1)))
    ck("nonzero_endpoint_countercase",endpoint_integral==(F(0),F(-2)))
    out["failed_routes"]["omitted_endpoints"]={"constant_amplitude_derivative":"0", "exact_integral_over_0_pi":zs(endpoint_integral), "invalid_derivative_only_bound":"0", "meaning":"Piecewise integration by parts must keep endpoint terms."}
    out["failed_routes"]["old_absolute_estimates"]={"meaning":"Their sufficient ceilings exceed the desired budget; this is not an actual leakage lower bound."}
    out["status"]="PASS_exact_scalar_corroboration_only"
    out["resources"]={"matrix_dimension":0,"grid_points":0,"quadrature_points":0,"optimizer_calls":0,"dynamics_steps":0,"largest_integer_power_requested":40,"cpu_soft_hard_seconds":list(resource.getrlimit(resource.RLIMIT_CPU)),"scientific_program_wall_seconds":time.monotonic()-started,"python_version":sys.version,"transitive_runtime_fully_pinned":False}
    out["source_identity"]={"executed_sha256":sha256(Path(__file__).read_bytes()).hexdigest(),"prelaunch_sha256":sha256(prepath.read_bytes()).hexdigest(),"source_manifest_sha256":sha256((D/"SOURCE_MANIFEST.json").read_bytes()).hexdigest(),"input_count":len(source_manifest["entries"])}
except BaseException as error:
    out["status"]="FAILED"
    out["error"]={"type":type(error).__name__,"message":str(error)}
    print(json.dumps(out,indent=2),flush=True)
    raise
else:
    print(json.dumps(out,indent=2),flush=True)

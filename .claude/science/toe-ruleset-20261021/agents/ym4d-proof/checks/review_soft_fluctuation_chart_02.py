import numpy as np,itertools as it,json
from scipy.linalg import logm,expm
N=3;r=4.;theta=2*np.pi/N
U=np.exp(1j*theta)*np.eye(N);A=logm(U)
# Eigenvalue lifts theta+2*pi*k_j, sum k_j=-1, have squared norm
# 4*pi^2*(sum k_j^2-1/3), at least 8*pi^2/3 because integers sum -1.
minimum=2*np.pi*np.sqrt(2/3)
lifts=[(ks,np.linalg.norm(theta+2*np.pi*np.array(ks))) for ks in it.product(range(-3,4),repeat=N) if sum(ks)==-1]
kbest,vbest=min(lifts,key=lambda z:z[1])
B=1j*np.diag(theta+2*np.pi*np.array(kbest))
checks=[{'name':'center_is_SU3','pass':abs(np.linalg.det(U)-1)<2e-11},
 {'name':'principal_log_passes_original_norm_event','pass':np.linalg.norm(A)<r},
 {'name':'principal_log_is_not_su3','pass':abs(np.trace(A))>1},
 {'name':'traceless_log_minimum_exceeds_r','pass':minimum>r and abs(vbest-minimum)<2e-11},
 {'name':'r_is_below_HS_injectivity_radius','pass':r<np.pi*np.sqrt(2)},
 {'name':'minimizing_lift_exponentiates_to_center','pass':np.linalg.norm(expm(B)-U)<2e-11 and abs(np.trace(B))<2e-11},
 {'name':'smaller_common_principal_chart_excludes_witness','pass':2*np.pi/np.sqrt(N)<r and np.linalg.norm(A)>=2*np.pi/np.sqrt(N)-2e-11}]
print(json.dumps({'N':N,'r':r,'principal_HS_norm':float(np.linalg.norm(A)),'principal_trace':[np.trace(A).real,np.trace(A).imag],'minimum_traceless_log_norm':minimum,'injectivity_radius':float(np.pi*np.sqrt(2)),'minimizing_integer_lift':kbest,'checks':checks,'passed':int(sum(x['pass'] for x in checks)),'total':len(checks),'status':'Original definition needs explicit Lie-group log convention or smaller traceless principal-log chart; Gaussian Hessian unaffected.'},indent=2,default=lambda o:bool(o)))

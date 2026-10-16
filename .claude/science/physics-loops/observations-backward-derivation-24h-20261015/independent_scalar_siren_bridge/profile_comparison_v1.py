"""Post-exposure comparison of all author profile rows using physical flux variables."""
import json,hashlib,sys
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
HERE=Path(__file__).resolve().parent
reference=json.loads((HERE/'AUTHOR_EXPOSURE__SCALAR_SIREN_CONTROLS_v1.json').read_text())
rows=[]
for row in reference['details']['scattering_proxy']:
    a,b,k=row['a'],row['b'],row['k']
    def rhs(x,y):
        F=np.exp(a*(10*x**3-15*x**4+6*x**5)+b*64*x**3*(1-x)**3)
        return (np.array([[0,1/F],[-k*k*F,0]])@y.reshape((2,2))).reshape(-1)
    sol=solve_ivp(rhs,[0,1],np.eye(2).reshape(-1),method='Radau',rtol=3e-11,atol=3e-13)
    if not sol.success:raise RuntimeError(sol.message)
    mat=sol.y[:,-1].reshape((2,2));inc=np.array([1,1j*k]);ref=np.array([1,-1j*k]);out=np.exp(1j*k)*np.array([1,1j*k*np.exp(a)])
    rr,tt=np.linalg.solve(np.column_stack((mat@ref,-out)),-mat@inc)
    tr=complex(*row['strain_transmission']);rr0=complex(*row['reflection']);err=max(abs(tt-tr),abs(rr-rr0));flux=abs(rr)**2+np.exp(a)*abs(tt)**2
    rows.append({'profile_index':row['profile_index'],'k':k,'transmission':[tt.real,tt.imag],'reflection':[rr.real,rr.imag],'author_difference':err,'weighted_flux_error':abs(flux-1),'passed':bool(err<3e-8 and abs(flux-1)<3e-8)})
result={'scope':'Post-exposure all16author profile rows; independent Radau physical flux coordinates, no imported author solver','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'reference_sha256':hashlib.sha256((HERE/'AUTHOR_EXPOSURE__SCALAR_SIREN_CONTROLS_v1.json').read_bytes()).hexdigest(),'passed':sum(x['passed']for x in rows),'failed':sum(not x['passed']for x in rows),'rows':rows}
(HERE/'PROFILE_COMPARISON_RESULTS_v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'passed':result['passed'],'failed':result['failed'],'max_author_difference':max(x['author_difference']for x in rows),'max_flux_error':max(x['weighted_flux_error']for x in rows)}));sys.exit(bool(result['failed']))

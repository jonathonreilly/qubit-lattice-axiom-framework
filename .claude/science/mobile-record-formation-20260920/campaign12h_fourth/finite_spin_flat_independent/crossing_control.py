import json
from pathlib import Path
import numpy as np
from physical_builder import rotor_h2,flat_projector,PWORDS,PINDEX
from flat_probe import flat_mode

def J(theta):
    out=np.zeros((36,12),complex)
    for a in range(2):
        for r in range(6):
            for (q,z),v in flat_mode(a,r).items():out[PINDEX[q],6*a+r]+=complex(v)*np.exp(1j*z*theta)/np.sqrt(2)
    return out

def main():
    rows=[]
    for th in [0.,1e-4,.07,.31,np.pi/4,np.pi/2-1e-4,np.pi/2,2.19,3.14,4.6,6.2]:
        j=J(th);p=j@j.conj().T;q=np.eye(36)-p;g=rotor_h2(th)+4*np.eye(36)
        rank=np.count_nonzero(abs(np.linalg.eigvalsh(g))>1e-9)
        row={'theta':th,'J_isometry_error':float(np.linalg.norm(j.conj().T@j-np.eye(12))),'JG_zero_error':float(np.linalg.norm(g@j)),'wedge_projector_difference':float(np.linalg.norm(p-flat_projector(th))),'G_rank':int(rank)}
        distance=min(abs(th-k*np.pi/2) for k in range(-4,8))
        if distance>1e-9:
            R=np.linalg.solve(g+p,q)
            identity=np.linalg.norm(g@R-q)
            invnorm=np.linalg.norm(R,2)
            expected=1/(2*np.sqrt(2)*np.sin(distance/6))
            assert abs(invnorm/expected-1)<1e-8
            assert identity<1e-9
            row.update({'inverse_norm':float(invnorm),'predicted_inverse_norm':float(expected),'inverse_identity_error':float(identity)})
        assert row['J_isometry_error']<1e-12 and row['JG_zero_error']<1e-12 and row['wedge_projector_difference']<1e-12
        rows.append(row)
    result={'rows':rows,'crossings':'theta in (pi/2) Z; rank 22 at a crossing and rank 24 otherwise, while the physical flat frame remains rank 12 and smooth.','inverse_formula':'||G_Q(theta)^-1||=1/[2 sqrt(2) sin(dist(theta,(pi/2)Z)/6)] away from crossings.','status':'floating controls of analytically derived expressions'}
    Path('CROSSING_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

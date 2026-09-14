#!/usr/bin/env python3
"""Separate finite-matrix checks of the explicit Gaussian congruence bounds."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import block_diag


def spectral_checks():
    rng=np.random.default_rng(912844)
    raw=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    positive=raw.conj().T@raw/20
    rows=[]
    for mass in (.01,.3,2.):
        q=mass*np.eye(4)+positive
        edges=[(i,j,q[i,j]) for i in range(4) for j in range(i+1,4)]
        lengths=list(range(1,7))
        total=sum(lengths)
        triangular=np.zeros((total,total),complex)
        endpoint=np.zeros((total,4),complex)
        local=np.zeros((4+total,4+total),complex)
        local[:4,:4]=q
        cursor=0
        for (u,v,a),h in zip(edges,lengths):
            local[u,v]-=a
            local[v,u]-=a.conjugate()
            local[u,u]+=1
            local[v,v]+=h*abs(a)**2
            for j in range(h):
                k=cursor+j
                triangular[k,k]=1
                if j:
                    triangular[k,k-1]=1
                else:
                    endpoint[k,u]=1
                endpoint[k,v]=(-1)**(j+1)*a
                local[4+k,4+k]=1 if j==h-1 else 2
                if j:
                    local[4+k,3+k]=local[3+k,4+k]=1
            local[u,4+cursor]=local[4+cursor,u]=1
            last=4+cursor+h-1
            local[last,v]=(-1)**h*a
            local[v,last]=((-1)**h*a).conjugate()
            cursor+=h
        transform=np.block([[np.eye(4),np.zeros((4,total))],
                            [endpoint,triangular]])
        congruence=transform.conj().T@block_diag(q,np.eye(total))@transform
        assert np.max(abs(local-congruence))<1e-12
        h=max(lengths)
        degree=3
        amax=max(abs(a) for _,_,a in edges)
        b=np.sqrt((1+amax)*degree*max(1,h*amax))
        assert np.linalg.norm(endpoint,2)<=b
        assert np.linalg.norm(triangular,2)<=2
        assert np.linalg.norm(np.linalg.inv(triangular),2)<=h
        assert np.linalg.norm(transform,2)<=3+b
        assert np.linalg.norm(np.linalg.inv(transform),2)<=1+h*(1+b)
        qtop=np.linalg.eigvalsh(q)[-1]
        lower=min(mass,1)/(1+h*(1+b))**2
        upper=max(qtop,1)*(3+b)**2
        eig=np.linalg.eigvalsh(local)
        assert eig[0]>=lower and eig[-1]<=upper
        hidden=local[4:,4:]
        recovered=local[:4,:4]-local[:4,4:]@np.linalg.solve(hidden,local[4:,:4])
        assert np.max(abs(recovered-q))<1e-12
        assert abs(np.linalg.det(hidden)-1)<1e-12
        rows.append(dict(source_mass=mass,b_bound=b,lower_bound=lower,
                         actual_minimum=float(eig[0]),upper_bound=float(upper),
                         actual_maximum=float(eig[-1]),
                         schur_error=float(np.max(abs(recovered-q)))))
    return dict(cases=rows,hidden_variables=total,
                status='finite matrix congruence, norm, spectrum and Schur checks; all-volume bounds are proved separately')


def main():
    result=spectral_checks()
    Path(__file__).with_name('BLOCK4_SPECTRAL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

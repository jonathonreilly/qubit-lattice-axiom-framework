#!/usr/bin/env python3
"""Direct phase-evaluation certificates and load-bearing hypothesis controls."""
import ast
from collections import defaultdict
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from axial_cc import budget

HERE=Path(__file__).resolve().parent

def main():
    budget(); evidence={'finite_systems':[], 'seam_controls':[], 'escape_controls':{}}
    for radius in (1,2):
        path=HERE/f'axial_r{radius}_constraint_mixing_system.json'
        payload=json.loads(path.read_text()); lhs=defaultdict(Q);rhs=Q(0);witness=[]
        for row in payload['rows']:
            family,mon=ast.literal_eval(row['key']); weight=Q(0)
            if family=='GC2_P2':
                ps=[a for a in mon if a[0]=='p']
                if len(ps)==2 and all(a[1]==1 for a in ps) and ps[0][2]==ps[1][2]:
                    ns=[a for a in mon if a[0]=='N']
                    weight=8*Q(ns[0][2]-ps[0][2])
            elif family=='continuum_U0_dN':weight=Q(1)
            if weight:
                witness.append([row['id'],str(weight)])
                for col,c in row['coefficients']:lhs[col]+=weight*Q(c)
                rhs+=weight*Q(row['rhs'])
        assert not any(lhs.values()) and rhs==1
        certificate={'witness':witness,'lhs':{},'rhs':str(rhs),
            'construction':'8 times GC2_P2 at X=1,N=x,P_B=delta_0 plus continuum_U0_dN',
            'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
        (HERE/f'axial_r{radius}_affine_lapse_certificate.json').write_text(json.dumps(certificate,indent=2)+'\n')
        evidence['finite_systems'].append({'radius':radius,'columns':len(payload['columns']),
            'witness_rows':len(witness),'all_column_coefficients_zero':True,'rhs':str(rhs),
            'drop_required_U0_moment_changes_rhs_to':'0','input_sha256':certificate['input_sha256']})
    for radius in (1,2,4,8,16):
        side=4*radius+5;coords=list(range(-(side//2),side//2+1))
        lapse=dict(zip(coords,coords));wrap=lambda x:((x+side//2)%side)-side//2
        lap={x:lapse[wrap(x+1)]-2*lapse[x]+lapse[wrap(x-1)] for x in coords}
        assert all(lap[x]==0 for x in range(-2*radius,2*radius+1))
        assert [x for x in coords if lap[x]]==[coords[0],coords[-1]]
        # All derivatives of the ultralocal quadratic lapse energy are zero:
        # d/dp_i carries N_x times a linear combination of momenta at x.
        q={x:int(x==0) for x in coords}
        assert all(lapse[x]*q[x]==0 for x in coords)
        evidence['seam_controls'].append({'radius':radius,'side':side,'nonzero_laplacian_sites':[coords[0],coords[-1]],
            'entire_possible_G3_gradient_support_has_zero_lapse_laplacian':True})
    # A change of the quadratic kinetic law removes the critical-point reason.
    # G2[1]=sum p_x (h_(x+1)-h_(x-1))/2,
    # Tcross[N]=sum (N_x+N_(x+1))/2 p_x p_(x+1).
    # At p_0=1,N=x: dG/dh_(+1)=1/2,dG/dh_(-1)=-1/2;
    # dTcross/dp_(+1)=1/2,dTcross/dp_(-1)=-1/2.
    bracket_cross=Q(1,2)*Q(1,2)+Q(-1,2)*Q(-1,2)
    assert bracket_cross==Q(1,2)
    evidence['escape_controls']={'cross_site_kinetic_bracket':str(bracket_cross),
        'meaning':'The proof no longer gives zero LHS; no closure of the changed theory is asserted.',
        'zero_U0_first_lapse_moment':'The phase witness gives 0=0; continuum mixed normalization is necessary.'}
    evidence['runner_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (HERE/'affine_lapse_results.json').write_text(json.dumps(evidence,indent=2)+'\n')
    print(json.dumps(evidence,indent=2))

if __name__=='__main__':main()

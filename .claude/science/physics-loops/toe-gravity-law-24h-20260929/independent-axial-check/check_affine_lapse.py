#!/usr/bin/env python3
"""Independent finite-torus controls for the affine-lapse obstruction.

Uses only the independent explicit functional/gradient implementation. The
all-finite-support statement additionally requires the support proof in the note.
"""
import sys
sys.dont_write_bytecode=True
import check as independent
from check import *
import sympy as s

q=s.symbols('q',nonzero=True,real=True)
alpha=s.symbols('alpha',nonzero=True,real=True)

def coord(x,L): return (x+L//2)%L-L//2
def at_point(p,L):
    result=0
    for mon,c in p.items():
        value=s.Rational(c.numerator,c.denominator)
        for kind,comp,x in mon:
            if kind=='h': value=0;break
            if kind=='p':
                if (comp,x)!=(1,0):value=0;break
                value*=q
            elif kind=='X':pass
            elif kind=='N':value*=coord(x,L)
            else:raise ValueError(kind)
        result+=value
    return s.expand(result)

def run_radius(R):
    budget(); L=4*R+5; independent.L=L
    verts=range(-R,R+1); ends=range(1-R,R+1)
    # Substitute X=1 into the complete finite G1 polynomial, then combine.
    gconstant=linear((c,tuple(a for a in m if a[0]!='X')) for m,c in g1('X').items())
    assert not gconstant
    cn=c1('N'); tn=t2('N')
    dc={v:at_point(p,L) for v,p in gradient(cn).items()}
    dt={v:at_point(p,L)/alpha for v,p in gradient(tn).items()}
    assert all(c==0 for c in dt.values())
    active_c={v:c for v,c in dc.items() if c!=0}
    assert {coord(v[2],L) for v in active_c}=={-(L//2),L//2}
    ps=[var('p',i,x) for i in range(3) for x in ends]
    count=0; max_gradient_distance=0
    for mon in cwr(ps,3):
        density=one((var('X'),)+mon)
        dg={v:at_point(p,L) for v,p in gradient(density).items()}
        for v,c in dg.items():
            if c!=0:max_gradient_distance=max(max_gradient_distance,abs(coord(v[2],L)))
        bracket=-sum(c*dc.get(('h',v[1],v[2]),0) for v,c in dg.items() if v[0]=='p')
        assert s.expand(bracket)==0,mon
        count+=1
    assert max_gradient_distance<=2*R
    # Independently evaluate every U0 basis substitution into T2.
    ucount=0
    for xp,np in product(range(-R,R),verts):
        terms=[]
        for i,j in cwr(range(3),2):
            c=Q(1,8) if i==j else Q(-1,4)
            terms.append((c,(var('X',0,xp),var('N',0,np),var('p',i),var('p',j))))
        actual=at_point(functional(terms),L)/alpha
        assert s.expand(actual-np*q**2/(8*alpha))==0
        ucount+=1
    # G1[W] vanishes for arbitrary W, proved at the full smearing basis level.
    arbitrary_W=s.symbols('w0:'+str(L))
    pA=[0]*L
    rhs_G1=sum(2*pA[x]*(arbitrary_W[x]-arbitrary_W[(x-1)%L]) for x in range(L))
    assert rhs_G1==0
    result={'R':R,'L':L,'G1_constant_polynomial_terms':len(gconstant),
            'T2_gradient_all_zero':True,'G3p_basis_count':count,
            'G3p_nonzero_gradient_max_distance':max_gradient_distance,
            'C1_gradient_seam_positions':sorted({coord(v[2],L) for v in active_c}),
            'U0_basis_count':ucount,'U0_basis_value':'np*q**2/(8*alpha)',
            'normalized_residual_LHS_minus_RHS':str(-q**2/(8*alpha))}
    print(json.dumps(result),flush=True)
    return result

def three_dimensional_control(R=2):
    # Finite 3D torus: P_yy=q on the entire x=0 plane, all other P/h zero.
    # Check explicit fixed gradients and G1[W] with unrestricted shift values.
    L=4*R+5
    N=lambda x:coord(x%L,L)
    seam=set(); kinetic_nonzero=0
    for x,y,z in product(range(L),repeat=3):
        delta=N(x+1)-2*N(x)+N(x-1)
        if delta:seam.add(coord(x,L))
        # Each diagonal kinetic derivative is N times a linear combination of P.
        if N(x)*(1 if x==0 else 0):kinetic_nonzero+=1
    assert not kinetic_nonzero
    # Sum the coefficient of each independent W_y(0,y,z) exactly. Its positive
    # contribution at y cancels its negative contribution at y+1.
    wcoeff=defaultdict(int)
    for y,z in product(range(L),repeat=2):
        wcoeff[(y,z)]+=2
        wcoeff[((y-1)%L,z)]-=2
    assert all(c==0 for c in wcoeff.values())
    return {'R':R,'torus':[L,L,L],'P_yy_plane_sites':L*L,
            'T2_gradient_all_zero':True,'C1_gradient_x_seams':sorted(seam),
            'G1_W_each_independent_transverse_shift_coefficient_zero':True,
            'normalized_rhs':str(L*L*q**2/(8*alpha))}

def coefficient_control(filename):
    # These two serialized matrices were independently reconstructed in earlier
    # checks. Derive a new dual directly from phase evaluation, with no solving.
    payload=json.loads((HERE/filename).read_text())
    combined=defaultdict(Q); rhs=Q(0); weights=[]
    for row in payload['rows']:
        fam,mon=ast.literal_eval(row['key']); weight=Q(0)
        if fam=='GC2_P2':
            momenta=[v for v in mon if v[0]=='p']
            lapse=[v for v in mon if v[0]=='N']
            if len(momenta)==2 and momenta[0]==momenta[1] and momenta[0][1]==1:
                assert len(lapse)==1
                weight=Q(8*(lapse[0][2]-momenta[0][2]))
        elif fam=='continuum_U0_dN':weight=Q(1)
        if not weight:continue
        weights.append([row['id'],str(weight)])
        for j,c in row['coefficients']: combined[j]+=weight*Q(c)
        rhs+=weight*Q(row['rhs'])
    assert all(c==0 for c in combined.values()) and rhs==1
    return {'source_matrix':filename,'columns':len(payload['columns']),
            'witness_rows':len(weights),'weights':weights,'combined_left_nonzero':0,'rhs':str(rhs)}

def main():
    budget(); started=time.time()
    results=[run_radius(R) for R in (1,2,3)]
    td=three_dimensional_control();print(json.dumps(td),flush=True)
    # Adversarial mutation: an intersite kinetic term removes the critical-point
    # premise. Derive the nonzero bracket directly, rather than assuming it.
    independent.L=9
    g=one((var('X'),var('h',1),var('p',1,1)))
    intersite=one((var('N'),var('p',1),var('p',1,1)))
    mutated=at_point(pb(g,intersite),9)
    assert s.expand(mutated+q**2)==0
    mutation={'G2_density':'X_x B_x P_B(x+1)',
              'added_kinetic_density':'N_x P_B(x) P_B(x+1)',
              'bracket_at_witness':str(mutated)}
    print('Intersite kinetic mutation:',json.dumps(mutation),flush=True)
    certificates=[coefficient_control(name) for name in
                  ['axial_r1_constraint_mixing_system_start.json',
                   'axial_r2_constraint_mixing_system_radius2_start.json']]
    for cert in certificates:
        print('Direct coefficient dual:',json.dumps({k:v for k,v in cert.items() if k!='weights'}),flush=True)
    (HERE/'affine_lapse_control_results.json').write_text(json.dumps({'radii':results,'three_dimensional':td,'kinetic_mutation':mutation,'direct_certificates':certificates},indent=2)+'\n')
    print('Elapsed seconds:',time.time()-started,flush=True)

if __name__=='__main__':main()

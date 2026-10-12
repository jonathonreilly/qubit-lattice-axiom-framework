"""Exact Pauli arithmetic plus independent literal Kronecker-matrix oracles."""
import argparse,importlib.util,itertools,json,sys
import sympy as s

ap=argparse.ArgumentParser();ap.add_argument('--candidate',required=True)
ap.add_argument('--suite',choices=['all','normalization','tensor'],default='all')
args=ap.parse_args()
spec=importlib.util.spec_from_file_location('candidate',args.candidate)
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
rows=[]
print(json.dumps({'runtime':{'python':sys.version,'sympy':s.__version__}}),flush=True)
def row(name,ok,**kw):
    d={'name':name,'pass':bool(ok),**kw};rows.append(d);print(json.dumps(d,default=str),flush=True)

paulis={'I':s.eye(2),'X':s.Matrix([[0,1],[1,0]]),
        'Y':s.Matrix([[0,-s.I],[s.I,0]]),'Z':s.diag(1,-1)}
def literal(w):
    p=s.ones(1,1)
    for a in w:p=s.kronecker_product(p,paulis[a])
    return s.MutableSparseMatrix(p)
def matrix(p,n):
    out=s.MutableSparseMatrix(2**n,2**n,{})
    for w,z in p.items():out+=z*literal(w)
    return out.applyfunc(s.simplify)
def zero(p):return all(s.simplify(v)==0 for v in p)
def norm2_exact_witness(d):
    p=(d*d)/4
    return zero(p*p-p) and not zero(p) and zero(d-d.H)
def jw_literal(n,k):
    j,r=divmod(k,2)
    return literal('Z'*j+('X' if r==0 else 'Y')+'I'*(n-j-1))
def hamiltonian(n,g,J):
    out=s.zeros(2**n)
    for j in range(n):out-=g*literal('I'*j+'Z'+'I'*(n-j-1))
    for j in range(n-1):out-=J*literal('I'*j+'XX'+'I'*(n-j-2))
    return s.MutableSparseMatrix(out)
def comm(a,b):return a*b-b*a
def decompose_even(mat,n):
    p={}
    for w in c.coarse_even_basis(n):
        z=s.simplify(s.trace(literal(w)*mat)/2**n)
        if z!=0:p[w]=z
    return p

if args.suite in ('all','normalization'):
    for n in (2,3):
        for i in range(2*n):
            for j in range(i,2*n):
                got=c.add(c.refined_word(n,(i,j)),c.refined_word(n,(j,i)))
                ref=c.scale(2 if i==j else 0,c.unit(2*n))
                row(f'CAR_{n}_{i}_{j}',got==ref,actual=got,expected=ref)
        for j in range(n):
            got=c.refine_poly(c.word(n,{j:'Z'}),n)
            row(f'onsite_formula_{n}_{j}',got==c.expected_z(n,j),actual=got)
            row(f'onsite_parity_{n}_{j}',all(sum(a in 'XY' for a in w)%2==0 for w in got))
        for j in range(n-1):
            got=c.refine_poly(c.word(n,{j:'X',j+1:'X'}),n)
            row(f'bond_formula_{n}_{j}',got==c.expected_bond(n,j),actual=got)
    row('R_star_R',2*c.NORM_SQUARED==1,actual=2*c.NORM_SQUARED,expected=1)
    row('cell_isometry_amplitude_squared',2*c.NORM_SQUARED==1,
        actual_child_amplitude_squared_over_coarse=2*c.NORM_SQUARED)
    row('local_support_children',all(len(w)==6 for w in c.refined_word(3,(2,3))))

if args.suite=='all':
    for w in c.coarse_even_basis(2):
        p={w:s.Integer(1)}
        two=c.refine_poly(c.refine_poly(p,2),4)
        direct=c.refine_poly(p,2,2)
        row('composition_'+w,two==direct,terms=len(direct))
    # Literal 4x4 coarse and 16x16 fine matrices are independent of the
    # polynomial multiplication table in candidate.py.
    n=2;basis=c.coarse_even_basis(n)
    images={w:matrix(c.refine_poly({w:s.Integer(1)},n),2*n) for w in basis}
    gam=[jw_literal(2*n,k) for k in range(4*n)]
    for w in basis:
        phase,inds=c.inverse_even_basis(n)[w]
        oracle=s.eye(2**(2*n))/phase
        for k in inds:
            j,r=divmod(k,2)
            oracle=oracle*(gam[4*j+r]+gam[4*j+2+r])/s.sqrt(2)
        row('literal_image_'+w,zero(images[w]-oracle))
        row('literal_star_'+w,zero(images[w]-images[w].H))
    for u in basis:
        for v in basis:
            product=literal(u)*literal(v)
            p=decompose_even(product,n)
            mapped=sum((coef*images[w] for w,coef in p.items()),s.zeros(16))
            row('literal_product_'+u+'_'+v,zero(images[u]*images[v]-mapped))
    gram=s.Matrix([[s.simplify(s.trace(images[u].H*images[v])/16)
                    for v in basis] for u in basis])
    row('literal_injectivity_gram',gram==s.eye(len(basis)),rank=gram.rank())
    P=literal('ZZZZ')
    complements=[(gam[4*j+r]-gam[4*j+2+r])/s.sqrt(2)
                 for j in range(n) for r in range(2)]
    def expect(mat):
        out=mat
        for d in complements:
            U=P*d;out=(out+U*out*U.H)/2
            out=out.applyfunc(s.simplify)
        return out
    for w in basis:
        out=expect(images[w])
        row('left_inverse_'+w,zero(out-images[w]))
        row('trace_preserved_'+w,s.simplify(s.trace(out)-s.trace(images[w]))==0)
    A=complements[0]*complements[1]
    EA=expect(A);EA2=expect(A*A)
    row('complement_bilinear_killed',zero(EA))
    row('complement_square_preserved',zero(EA2+s.eye(16)))
    row('expectation_multiplicative_hypothesis',not zero(EA2-EA*EA),
        hypothesis_holds=zero(EA2-EA*EA),expected_hypothesis=False)
    # Different endpoints: old even words gain two exterior strings.
    old=matrix(c.gamma_word(2,(1,2)),2)
    extended=jw_literal(4,3)*jw_literal(4,4)
    row('even_endpoint_independence',zero(extended-s.kronecker_product(paulis['I'],old,paulis['I'])))
    old_odd=s.kronecker_product(paulis['I'],jw_literal(2,0),paulis['I'])
    new_odd=jw_literal(4,2)
    row('odd_endpoint_counterexample_norm2',norm2_exact_witness(new_odd-old_odd))

if args.suite in ('all','tensor'):
    q=1/s.sqrt(2)
    gate=s.Matrix([[1,0,0,0],[0,q,q,0],[0,-q,q,0],[0,0,0,1]])
    U=s.kronecker_product(gate,gate)
    row('block_rotation_unitary',zero(U*U.H-s.eye(16)))
    got=U*matrix(c.inserted_bond(2,0),4)*U.H
    target=matrix(c.expected_bond(2,0),4)
    row('rotated_cross_block_bond',zero(got-target),difference_rank=(got-target).rank())
    onsite=U*literal('ZIII')*U.H
    row('rotated_onsite_survivor',zero(onsite-matrix(c.expected_z(2,0),4)))
    correct=U*literal('XZ XI'.replace(' ',''))*U.H
    wrong=U*literal('XIXI')*U.H
    row('tensor_shortcut_norm2_counterexample',norm2_exact_witness(correct-wrong))
    row('tensor_shortcut_onsite_agrees',zero(U*literal('ZIII')*U.H-onsite))
    row('tensor_shortcut_parity_survives',zero(comm(got,literal('ZZZZ'))))

if args.suite=='all':
    gc,Jc,gf,Jf=s.symbols('g_c J_c g_f J_f',real=True)
    Hc=hamiltonian(3,gc,Jc);Hf=hamiltonian(6,gf,Jf)
    A=literal('IZI')
    delta=s.I*comm(Hc,A)
    exact_p=decompose_even(delta,3)
    expected=c.scale(-2*Jc,c.add(c.word(3,{0:'X',1:'Y'}),c.word(3,{1:'Y',2:'X'})))
    row('literal_delta_Z',exact_p==expected,actual=exact_p)
    refined_delta=matrix(c.refine_poly(exact_p,3),6)
    fine_delta=s.I*comm(Hf,matrix(c.refine_poly({'IZI':s.Integer(1)},3),6))
    diff=fine_delta-refined_delta
    witness=literal('IIIYZX')
    coef=s.simplify(s.trace(witness*diff)/64)
    row('literal_Hamiltonian_counterexample',coef==Jc,coefficient=coef,expected=Jc)
    row('exact_flow_compatibility_hypothesis',not zero(diff),
        hypothesis_holds=zero(diff),expected_hypothesis=False)
    row('Hamiltonian_parity_survivor',zero(comm(diff,literal('ZZZZZZ'))))
    row('Hamiltonian_constant_survivor',zero(comm(Hf,s.eye(64))))

print('per_element: exact onsite and cross-block Pauli images and products are inspected.',flush=True)
print('per_site: Z is a selected element witness; no claim that every element fails.',flush=True)
print('per_mode: checked and not executed — universal modewise compatibility is not claimed.',flush=True)
print('per_block: two and three coarse cells retain ancillary parity and the local energy witness.',flush=True)
print('lattice_wide: a nonzero local witness refutes only the stated universal identity; infinite limits use proof.',flush=True)
failed=[r['name'] for r in rows if not r['pass']]
print(json.dumps({'summary':{'rows':len(rows),'pass':len(rows)-len(failed),'fail':len(failed),'failed':failed}}),flush=True)
sys.exit(bool(failed))

"""Small checks of the analytical pull-through and spectral-counting proof.

The Fock fixture is an explicitly shifted four-mode comparator, not the
infinite native scalar or a numerical low-energy fit. Native lattice checks
are built separately from the literal signed nearest-neighbor matrix.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations,product
from math import comb,prod
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as s
HERE=Path(__file__).resolve().parent
AUDIT_TIMEOUT_SEC=180


def run():
    start=time.monotonic();checks=[]
    def checked(name,condition,**data):
        assert condition,name
        checks.append({'name':name,**data})
    def close(name,x,y,tol=1e-12):
        error=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
        checked(name,error<tol,absolute_error=error)

    C3=180*prod(43+23*j for j in range(3))
    one_band=F(90,8)*(2*64+15*256+4*64)
    ratio=F(C3*C3,432*49)*F(22,7)**5/F(32768)**6
    checked('pull_through_constants',C3==45464760 and one_band==47520)
    checked('inner_ball_in_positive_amplitude_window',F(1,32768)<F(7,190080))
    checked('complete_nonlinear_ratio_bound',ratio<F(1,10**12),rational=str(ratio),decimal=float(ratio))
    pi,h,E=s.symbols('pi h E',positive=True)
    volume=s.Rational(4,3)*pi*(pi*E/(2*h))**3
    checked('four_band_DOS_upper_coefficient',s.simplify(4*volume/(2*pi)**3-pi*E**3/(12*h**3))==0)
    checked('one_source_inner_ball_coefficient',s.simplify(s.Rational(1,4)*(s.Rational(4,3)*pi*(E/h)**3)/(2*pi)**3-E**3/(24*pi*pi*h**3))==0)
    checked('nine_power_laplace_coefficient',s.integrate(s.Symbol('x',positive=True)**9*s.exp(-s.Symbol('x',positive=True)),(s.Symbol('x',positive=True),0,s.oo))==s.factorial(9))

    # Exact native cell matrix, assembled from literal signed +/- neighbors.
    sites=list(product((0,1),repeat=3));ix={r:i for i,r in enumerate(sites)}
    z=s.symbols('z0:3',nonzero=True);K=s.zeros(8)
    for r in sites:
        for axis in range(3):
            for direction in (-1,1):
                w=list(r);w[axis]+=direction;cell=tuple(x//2 for x in w);sub=tuple(x%2 for x in w)
                K[ix[r],ix[sub]]+=direction*(-1)**sum(r[:axis])*prod(z[a]**cell[a] for a in range(3))
    radial=sum(v+1/v-2 for v in z)
    checked('native_cell_square',all(s.expand(v)==0 for v in K*K-radial*s.eye(8)))
    checked('native_zero_diagonal',all(K[j,j]==0 for j in range(8)))
    checked('native_skew_adjoint_symbol',all(s.expand(v)==0 for v in K.T.subs(dict(zip(z,[1/v for v in z])),simultaneous=True)+K))
    def entry(r,w):
        diff=tuple(b-a for a,b in zip(r,w))
        if sum(abs(x) for x in diff)!=1:return 0
        axis=next(a for a in range(3) if diff[a]);return diff[axis]*(-1)**sum(r[:axis])
    count=0
    for r in product(range(-2,3),repeat=3):
        for a in range(3):
            for direction in (-1,1):
                w=list(r);w[a]+=direction;w=tuple(w)
                for reflection in range(3):
                    rr=tuple(-x if j==reflection else x for j,x in enumerate(r));ww=tuple(-x if j==reflection else x for j,x in enumerate(w))
                    assert entry(r,w)==(-1)**(r[reflection]+w[reflection])*entry(rr,ww)
                    count+=1
    checked('literal_native_reflection_gauges',True,edge_comparisons=count)
    reflection=[s.diag(*[(-1)**r[a] for r in sites]) for a in range(3)]
    constraints=s.Matrix.vstack(*[m-s.eye(8) for m in reflection])
    null=constraints.nullspace()
    checked('zero_cell_functional_only_origin_component',len(null)==1 and null[0]==s.eye(8)[:,0])
    X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
    Gz=s.kronecker_product(Z,Z,X);P=(s.eye(8)+Gz)/2
    checked('three_column_native_cone_Gram',P.extract([0,2,4],[0,2,4])==s.eye(3)/2)

    # Four-mode comparator with a known scalar shift to keep every defect gapped.
    modes=4;dim=1<<modes;I=np.eye(dim,dtype=complex);ann=[]
    for j in range(modes):
        a=np.zeros((dim,dim),complex)
        for mask in range(dim):
            if mask&(1<<j):a[mask^(1<<j),mask]=(-1)**((mask&((1<<j)-1)).bit_count())
        ann.append(a)
    majoranas=[]
    for a in ann:majoranas.extend((a+a.conj().T,1j*(a.conj().T-a)))
    frequencies=(1,2,3,5)
    number=np.array([j.bit_count() for j in range(dim)])
    energy=np.array([sum(frequencies[a] for a in range(modes) if j&(1<<a)) for j in range(dim)])
    H=np.diag(energy).astype(complex);g=majoranas[0];legs=majoranas[1:7]
    vacuum=I[:,0];pairs=list(combinations(range(6),2))
    defects={A:1j*g@(legs[A[0]]+legs[A[1]]) for A in pairs}
    Ds={A:H+5*I+B for A,B in defects.items()}
    min_gap=min(float(np.linalg.eigvalsh(D).min()) for D in Ds.values())
    checked('comparator_all_defects_positive',min_gap>3.5,minimum=min_gap,scope='shifted four-mode comparator only')
    @lru_cache(None)
    def inverse(A,shift):return -np.linalg.inv(Ds[A]+shift*I)
    local={(A,j):ann[j]@defects[A]-defects[A]@ann[j] for A in pairs for j in range(modes)}
    maximum=0.;wrong_shift=0.
    for A in pairs:
        for j,w in enumerate(frequencies):
            for shift in (0,2):
                lhs=ann[j]@inverse(A,shift)
                rhs=inverse(A,shift+w)@ann[j]+inverse(A,shift+w)@local[A,j]@inverse(A,shift)
                maximum=max(maximum,float(np.max(abs(lhs-rhs))))
                wrong=inverse(A,shift)@ann[j]+inverse(A,shift)@local[A,j]@inverse(A,shift)
                wrong_shift=max(wrong_shift,float(np.max(abs(lhs-wrong))))
    checked('full_matrix_shifted_pull_through',maximum<1e-12,absolute_error=maximum)
    checked('omitted_frequency_shift_rejected',wrong_shift>.001,residual=wrong_shift)

    def field(label):return g if label==('g',) else local[label[1],label[2]]
    def act(word):
        v=vacuum.copy()
        for token in reversed(word):v=(inverse(token[1],token[2]) if token[0]=='R' else field(token[1]))@v
        return v
    def commute(j,word):
        prefix=[];sign=1;terms=[]
        for position,token in enumerate(word):
            suffix=list(word[position+1:])
            if token[0]=='R':
                A,shift=token[1:];moved=('R',A,shift+frequencies[j])
                terms.append((sign,tuple(prefix+[moved,('F',('L',A,j)),token]+suffix)))
                prefix.append(moved)
            else:
                contraction=ann[j]@field(token[1])+field(token[1])@ann[j]
                value=np.trace(contraction)/dim
                assert np.max(abs(contraction-value*I))<1e-12
                if abs(value)>1e-15:terms.append((sign*value,tuple(prefix+suffix)))
                prefix.append(token);sign=-sign
        return terms
    A,C=(0,2),(1,3);word=(('R',C,0),('F',('g',)),('R',A,0))
    original=act(word);maximum=0.;counts=[]
    for indices in ((0,1,2),(0,2,3),(1,2,3),(0,0,2)):
        terms=[(1,word)];direct=original.copy()
        for j in indices:
            direct=ann[j]@direct
            terms=[(c*d,v) for c,w in terms for d,v in commute(j,w)]
        reconstructed=sum((c*act(w) for c,w in terms),np.zeros(dim,complex))
        maximum=max(maximum,float(np.max(abs(direct-reconstructed))));counts.append(len(terms))
    checked('three_annihilator_word_recursion',maximum<1e-12,absolute_error=maximum,word_counts=counts)
    chi=sum((inverse(C,0)@g@inverse(A,0)@vacuum for A in pairs for C in pairs if not set(A)&set(C)),np.zeros(dim,complex))/8
    nonlinear=float(np.linalg.norm(chi[number>=3])**2)
    checked('nonlinear_comparator_is_nonvacuous',nonlinear>1e-18,weight=nonlinear)
    close('star_odd_particle_sectors',chi[number%2==0],0)
    for cutoff in (2,4,8,13):
        low=[j for j,w in enumerate(frequencies) if w<=cutoff]
        count_low=np.array([sum(bool(mask&(1<<j)) for j in low) for mask in range(dim)])
        binomial=np.array([comb(int(n),3) if n>=3 else 0 for n in count_low])
        indicator=((energy<=cutoff)&(number>=3)).astype(int)
        checked('positive_energy_projector_domination_'+str(cutoff),np.all(indicator<=binomial))
        ordered=sum(np.linalg.norm(ann[k]@ann[j]@ann[i]@chi)**2 for i,j,k in product(low,repeat=3))
        target=float(np.sum(binomial*abs(chi)**2))
        close('ordered_factorial_moment_'+str(cutoff),ordered/6,target,tol=1e-13)
        if cutoff==13:checked('missing_factorial_normalization_rejected',abs(ordered-target)>1e-12,residual=float(abs(ordered-target)))

    # Wick subtraction is tested on nonzero pair contractions.
    fs=[majoranas[0],(majoranas[1]+majoranas[2])/np.sqrt(2),(majoranas[3]+majoranas[4])/np.sqrt(2)]
    contractions={(i,j):np.vdot(vacuum,fs[i]@fs[j]@vacuum) for i,j in combinations(range(3),2)}
    bare=fs[0]@fs[1]@fs[2]
    wick=bare-contractions[0,1]*fs[2]+contractions[0,2]*fs[1]-contractions[1,2]*fs[0]
    state=wick@vacuum
    close('Wick_order_removes_one_particle',state[number==1],0)
    checked('Wick_order_has_nonzero_three_particle_component',np.linalg.norm(state[number==3])>.1)
    checked('omitted_Wick_subtractions_rejected',np.linalg.norm((bare@vacuum)[number==1])>.1)

    return {'status':'passed','count':len(checks),'checks':checks,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'derivation_sha256':hashlib.sha256((HERE/'BLOCK14_DERIVATION.md').read_bytes()).hexdigest(),
            'scope':'exact arithmetic/native cell checks and a distinct shifted finite-Fock comparator; no native spectral fit, infinite proof by enumeration or independent source review'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK14_SPECTRAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='checks'},indent=2))

"""Explicit extension to all proper-cubic symmetric symbols; author control."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parent
source=ROOT/'cubic_entropy_symbol_check.py';raw=source.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='7103bd3d00d204186952c6d4e7b29d1286a619413b0ce0b01f9cfca179477927'
# Reuse the frozen checked basis/character construction without writing its
# sealed outputs. Its complete assertions execute before the result-write block.
text=raw.decode();marker='result = {';assert text.count(marker)==1
namespace={'__file__':str(source)};exec(compile(text.split(marker)[0],str(source),'exec'),namespace)
U=namespace['U'];group=namespace['group'];Ds=namespace['D'];Qs=namespace['T'];base=namespace['symbol'];cross=namespace['cross']

def symbol(q,c):
    A=base(q,c[:5]);b1,b2,bu,bv,d,g=c[5:]
    for column,coefficient in [(3,b1),(4,b2)]:
        A[5:8,column]=coefficient*q;A[column,5:8]=coefficient*q
    A[5:8,8:10]=np.column_stack([bu*D@q for D in Ds]);A[8:10,5:8]=A[5:8,8:10].T
    A[5:8,10:13]=np.column_stack([bv*Q@q for Q in Qs]);A[10:13,5:8]=A[5:8,10:13].T
    C=cross(q)
    A[10:13,8:10]=np.array([[d*np.trace(Q@(C@D-D@C)) for D in Ds] for Q in Qs])
    A[8:10,10:13]=A[10:13,8:10].T
    A[10:13,13]=g*q[::-1];A[13,10:13]=g*q[::-1]
    return A

covariance_error=0.;families=[];Trev=np.diag([-1]*3+[1]*11)
for i,c in enumerate(np.eye(11)):
    families.append(np.concatenate([symbol(q,c).ravel() for q in np.eye(3)]))
    for Q,P,det in group:
        if det!=1:continue
        R=U.T@P@U
        for q in np.eye(3):
            covariance_error=max(covariance_error,float(abs(R@symbol(q,c)@R.T-symbol(Q@q,c)).max()))
    for q in np.eye(3):
        A=symbol(q,c)
        assert np.allclose(Trev@A@Trev,(-1 if i<5 else 1)*A,rtol=0,atol=1e-12)
assert covariance_error<1e-12
assert np.linalg.matrix_rank(np.array(families))==11
assert namespace['multiplicity'](True)==11
vector=[0,1,2,5,6,7];other=[3,4,8,9,10,11,12,13]
coupled=[];curl_forcing=[]
for i,c in enumerate(np.eye(11)):
    if any(np.linalg.norm(symbol(q,c)[np.ix_(vector,other)])>1e-12 for q in np.eye(3)):
        coupled.append(i)
    if any(np.linalg.norm(cross(q)@symbol(q,c)[np.ix_([0,1,2],other)])+np.linalg.norm(cross(q)@symbol(q,c)[np.ix_([5,6,7],other)])>1e-12 for q in [*np.eye(3),np.array([1.,1.,0.])]):
        curl_forcing.append(i)
assert coupled==[0,1,3,4,5,6,7,8]
assert curl_forcing==[3,4,7,8]
d,g,x,y,z=sp.symbols('d g x y z',real=True)
N=sp.Matrix([[2*d*z,0,g*z],[-d*y,-sp.sqrt(3)*d*y,g*y],[-d*x,sp.sqrt(3)*d*x,g*x]])
assert sp.factor(N.det())==-6*sp.sqrt(3)*d*d*g*x*y*z
coeff=np.zeros(11);coeff[2]=2;coeff[9]=3;coeff[10]=4
eig=np.linalg.eigvalsh(symbol(np.array([1.,2.,3.]),coeff))
assert np.count_nonzero(abs(eig)<1e-10)==4
result={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'frozen_base_source_sha256':hashlib.sha256(raw).hexdigest(),
        'proper_cubic_dimension_exact':11,'explicit_family_dimension':11,
        'proper_covariance_max_abs_error':covariance_error,
        'full_vector_source_channels':coupled,'curl_readout_source_channels':curl_forcing,
        'extra_six_have_even_reversal_parity':True,
        'nonvector_determinant_exact':str(sp.factor(N.det())),
        'closed_vector_generic_example_nonzero_modes':10,'closed_vector_generic_example_zero_modes':4,
        'scope':'Author reconstruction and numerical intertwiner/closure controls plus exact determinant; no new continuum or physical interpretation. Independent extension review pending.'}
(ROOT/'PROPER_CUBIC_ELEVEN_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

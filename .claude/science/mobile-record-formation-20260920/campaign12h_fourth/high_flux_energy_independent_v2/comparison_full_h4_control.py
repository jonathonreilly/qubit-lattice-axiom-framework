#!/opt/homebrew/opt/python@3.13/bin/python3.13
"""Post-PRE extension: own frozen direct operator implementation, symbolic n.
No author builder is imported. Author certificate read only after calculating
and saving the complete H4 image and symbolic moments.
"""
import sys
sys.dont_write_bytecode=True
from collections import Counter
from pathlib import Path
import hashlib,importlib.util,json
import sympy as sp
HERE=Path(__file__).resolve().parent
SOURCE=HERE/'direct_matrix_action_control.py'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='3523e5e79b181b82502bd71049daf99bc5dcf9eb1dce4facccf79b11c0600a6b'
spec=importlib.util.spec_from_file_location('own_frozen_PRE_matrix',SOURCE)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
n,K,delta=sp.symbols('n K delta', real=True)
V=tuple({(0,1):1,(1,3):1,(2,3):-1,(0,2):-1}.get(e,0) for e in m.EE)
q=tuple(int(i in m.AA) for i in range(8))
g={(q,tuple(n*v for v in V)):sp.Integer(1)}
v=m.B(g,m.EE.index((0,1)),(1,),None)
coh=m.B(g,m.EE.index((0,1)),(1,-1),None)

def moments(w):
    norm=m.inner(w,w);H=m.H4(w,None);D=m.D(w)
    h=m.plus(m.times(D,K),m.times(H,delta))
    dh=m.inner(w,D)/norm;hh=m.inner(w,H)/norm
    covariance=sp.simplify(m.inner(D,H)/norm-dh*hh)
    variance=sp.factor(m.inner(h,h)/norm-(K*dh+delta*hh)**2)
    return {'norm':norm,'D_mean':dh,'D_variance':sp.factor(m.inner(D,D)/norm-dh**2),
            'H4_mean':hh,'H4_second_moment':sp.factor(m.inner(H,H)/norm),
            'H4_variance':sp.factor(m.inner(H,H)/norm-hh**2),'symmetrized_D_H4_covariance':covariance,
            'h_mean':sp.factor(K*dh+delta*hh),'h_variance':variance,'H4_image_words':len(H)}

def gauss(s):
    q,E=s;div=[0]*8
    for (a,b),e in zip(m.EE,E):div[a]+=e;div[b]-=e
    return all(sp.simplify(div[i]-q[i]+int(i in m.AA))==0 for i in range(8))

def relative_dict(w):
    return {(q,tuple(sp.simplify(e-n*vi) for e,vi in zip(E,V))):a for (q,E),a in w.items()}

def rows(w):
    return [{'charges':q,'field':E,'amplitude':str(a)} for (q,E),a in sorted(w.items())]

Hv=m.H4(v,None)
assert all(gauss(s) for w in (g,v,Hv) for s in w)
relative=relative_dict(Hv)
# Recompute at literal n=0 from scratch; exact dictionary equality, not moments only.
g0={(q,(0,)*12):sp.Integer(1)}
v0=m.B(g0,0,(1,),None);H0=m.H4(v0,None)
assert relative==H0
hist=dict(sorted(Counter(str(a) for a in H0.values()).items()))
our={'scope':'Additional H4 moment reconstructed with own PRE implementation; author values now known, no author builder imported',
     'own_PRE_implementation_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
     'input':moments(g),'selected_resolved':moments(v),'selected_coherent':moments(coh),
     'H4_image_histogram':hist,'H4_image_norm_squared':m.inner(Hv,Hv),
     'input_support_coefficients':[{ 'q':s[0],'offset':tuple(sp.simplify(e-n*vi) for e,vi in zip(s[1],V)),
          'input_amplitude':a,'H4_amplitude':Hv.get(s,0)} for s,a in v.items()],
     'symbolic_translation_image_identity':True,
     'input0':rows(v0),'H4_image0':rows(H0),
     'initial_H4_image0':rows(m.H4(g0,None)),
     'initial_H4_histogram':dict(sorted(Counter(str(a) for a in m.H4(g0,None).values()).items()))}
(HERE/'COMPARISON_OWN_H4_MOMENTS.json').write_text(json.dumps(our,default=str,indent=2)+'\n')
# Author certificate is compared by all state/coefficient pairs after reconstruction.
author=HERE.parent/'high_flux_energy_extension_author/SELECTED_H4_IMAGE_CERTIFICATE.json'
data=json.loads(author.read_text())
def decode(rows):return {(tuple(r['charges']),tuple(r['field'])):sp.Rational(r['amplitude']) for r in rows}
assert decode(data['input'])==v0
assert decode(data['H4_image'])==H0
# Construct an independently wrong diagonal-H4 replacement; it must miss variance.
diagonal={s:Hv[s] for s in v}
wrongvar=sp.factor(m.inner(diagonal,diagonal)/m.inner(v,v)-(m.inner(v,diagonal)/m.inner(v,v))**2)
assert wrongvar!=our['selected_resolved']['H4_variance']
report={'author_certificate_sha256':hashlib.sha256(author.read_bytes()).hexdigest(),
        'every_input_and_H4_image_word_matches':True,'matched_image_words':len(H0),
        'wrong_diagonal_H4_variance':str(wrongvar),
        'actual_H4_variance':str(our['selected_resolved']['H4_variance']),
        'diagonal_replacement_mutation_detected':True,
        'symbolic_selected_h_variance':str(our['selected_resolved']['h_variance']),
        'symbolic_selected_covariance':str(our['selected_resolved']['symmetrized_D_H4_covariance']),
        'covariance_explanation':'On the two input-support words H4 v has the same multiple of the input coefficient; diagonal D never brings other image words into the cross moment.'}
(HERE/'COMPARISON_H4_CERTIFICATE_RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'moments':{key:our[key] for key in ('input','selected_resolved','selected_coherent','H4_image_histogram','H4_image_norm_squared')},'comparison':report},default=str,indent=2))

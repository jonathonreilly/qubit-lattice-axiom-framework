"""Compare full recorded refinement payloads at fixed protocol tolerances."""
import json
import numpy as np
from reporting import arguments,Book

def unpack(z):return np.array(z['real'])+1j*np.array(z['imag'])

def main():
    def extra(p):p.add_argument('--first',required=True);p.add_argument('--second',required=True)
    args,c=arguments(extra);b=Book('mixed_refinement_comparison',args)
    def data(path):
        raw=json.loads(open(path).read())
        return {r['context']['a']:r['context'] for r in raw['rows'] if r['name']=='resolution_comparison_payload'}
    first=data(args.first);second=data(args.second)
    assert set(first)==set(second)
    for a in first:
        u=first[a];v=second[a]
        for key in ['errors','error_squares','moments','defects']:
            b.check('refinement_'+key,np.max(np.abs(np.array(u[key])-np.array(v[key]))),8e-7,a=a)
        for key in ['covariance','continuum_covariance']:
            b.check('refinement_'+key,np.max(np.abs(unpack(u[key])-unpack(v[key]))),8e-7,a=a)
    b.finish('Compares retained coarse/fine or fine/high payloads at the same preregistered 8e-7 threshold. Agreement is not a rigorous continuum quadrature or infinite-volume bound. A failed lower refinement remains evidence even if the predeclared higher refinement passes.')

if __name__=='__main__':main()

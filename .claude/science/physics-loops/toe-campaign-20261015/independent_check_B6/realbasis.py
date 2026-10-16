# real basis for d=2 quaternion walks U = f + i g.sigma (f,g real trig polys), from rational complex basis
import sympy as sp, pickle
def real_basis(eb):
    """returns list of elements: dict n -> list of 4 sympy numbers (coeffs of q0..q3 i.e. f, g1,g2,g3) of e^{ikn}"""
    def vec(el):
        return {n:[d.get((a,0,0),0) for a in range(4)] for n,d in el.items()}
    els=[vec(el) for el in eb]
    keys=sorted({n for e in els for n in e})
    def flat(e): return sp.Matrix([x for n in keys for x in e.get(n,[0]*4)])
    cand=[]
    for e in els:
        es={tuple(-x for x in n):[sp.conjugate(c) for c in v] for n,v in e.items()}
        a={n:[sp.nsimplify(x) for x in v] for n,v in e.items()}
        p={}; q={}
        for n in set(e)|set(es):
            v1=e.get(n,[0]*4); v2=es.get(n,[0]*4)
            p[n]=[sp.expand(x+y) for x,y in zip(v1,v2)]
            q[n]=[sp.expand(sp.I*(x-y)) for x,y in zip(v1,v2)]
        cand+= [p,q]
    # reduce to independent set (over R; elements are 'real' in the sense e*=e)
    M=sp.Matrix.hstack(*[flat(c) for c in cand])
    # independence over C equals over R for e*=e elements
    _,piv=M.rref()
    return [cand[i] for i in piv], keys
if __name__=="__main__":
    import sys
    eb=pickle.load(open(sys.argv[1],'rb'))
    rb,keys=real_basis(eb)
    print(len(rb)); pickle.dump(rb,open(sys.argv[2],'wb'))

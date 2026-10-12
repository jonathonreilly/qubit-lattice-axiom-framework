"""Sequential scalar pullbacks against independently flattened spacetime words."""
import numpy as np
from fixtures import compose_coordinates,quadrature,words
from reporting import arguments,Book

def initial(q):
    return np.exp(-.7*(q-.24)**2+1j*(.31*q+.07*q*q))*(1+.1j*q)

def coordinate_oracle(q,word,m,v):
    eta,tau,ell=compose_coordinates(word,v)
    E=np.hypot(m,v*q);at=q*np.cosh(eta)+E/v*np.sinh(eta)
    return np.exp(-1j*(tau*E+ell*q))*np.sqrt(np.hypot(m,v*at)/E)*initial(at)

def main():
    args,c=arguments();b=Book('continuum_semidirect_composition',args)
    m=.8;v=1.3;q,w=quadrature(800,-16,16)
    norm=lambda x:float(np.sqrt(np.sum(w*np.abs(x)**2)))
    allwords=words()+[[('t',.25),('x',-.4),('b',.31),('t',-.12),('b',-.17),('x',.2)],
                      [('b',0.),('t',0.),('x',0.)]]
    for j,word in enumerate(allwords):
        proposed=c.positive_word(initial,q,word,m,v);exact=coordinate_oracle(q,word,m,v)
        b.check('coordinate_vs_pullback',norm(proposed-exact),2e-11,word=j,parameters=word)
        b.check('unitarity_weak',abs(norm(proposed)-norm(initial(q))),2e-11,word=j)
    for s in [-.31,0.,.27]:
        for t in [-.23,0.,.19]:
            lhs=[('b',s),('t',t),('b',-s)];rhs=c.q15_rhs(s,t,v)
            left=coordinate_oracle(q,lhs,m,v);right=c.positive_word(initial,q,rhs,m,v)
            b.check('Q15_boost_time',norm(left-right),2e-11,s=s,t=t,displacement=rhs[0][1])
            b.check('Q15_norm_weak',abs(norm(left)-norm(right)),2e-11,s=s,t=t)
        for ell in [-.33,0.,.21]:
            lhs=[('b',s),('x',ell),('b',-s)];rhs=c.q16_rhs(s,ell,v)
            left=coordinate_oracle(q,lhs,m,v);right=c.positive_word(initial,q,rhs,m,v)
            b.check('Q16_boost_space',norm(left-right),2e-11,s=s,ell=ell)
            b.check('Q16_norm_weak',abs(norm(left)-norm(right)),2e-11,s=s,ell=ell)
    b.finish('Reference multiplies spacetime semidirect coordinates with tau=-physical t, then applies one translated boost. Candidate sequentially pulls back momentum and accumulates phases/Jacobians. They do not share a composition implementation. Weak norms and zero parameters survive some wrong signs, as expected. This checks a finite parameter set, not the analytic compact-uniform theorem.')

if __name__=='__main__':main()

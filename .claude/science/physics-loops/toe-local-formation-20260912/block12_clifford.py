"""Formal Clifford recurrence for native vacuum and Ward-source moments.

No lattice diagonalization, quadrature, fitted input or Fock-space solve.
Gram and covariance tables are the analytical equations (12.7).
"""
from __future__ import annotations
from functools import lru_cache
from math import comb, factorial
import sympy as s

A0,C0=s.symbols('A0 C0',real=True)
ODD={r:s.Symbol(f'L{r}',real=True) for r in (1,3,5,7,9,11)}
ODD[-1]=C0


@lru_cache(None)
def radial(n):
    return sum(factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))*
               comb(2*a,a)*comb(2*b,b)*comb(2*(n-a-b),n-a-b)
               for a in range(n+1) for b in range(n-a+1))


class Algebra:
    def __init__(self,kind):
        assert kind in ('P','O');self.kind=kind
        self.labels=[('w',0)]+[(typ,j) for j in range(6) for typ in ('a','d')]
        self.lookup={v:i for i,v in enumerate(self.labels)}

    def D(self,n):
        return s.Integer(2*radial(n)) if self.kind=='P' else s.Rational(radial(n+1),3)

    def F(self,r):
        return 2*ODD[r] if self.kind=='P' else ODD[r+2]/3

    @lru_cache(None)
    def table(self,f,g):
        typ,i=self.labels[f];other,j=self.labels[g]
        if typ=='w' and other=='w':return (72*A0 if self.kind=='P' else s.Integer(12)),s.S.Zero
        if other=='w':
            dot,kap=self.table(g,f);return dot,-kap
        if typ=='w':
            if other=='a':
                if j%2==0:return s.Integer(2*(-1)**(j//2)*radial(j//2)),s.S.Zero
                return s.S.Zero,-2*(-1)**((j-1)//2)*ODD[j]
            if j%2:return -6*(-1)**((j-1)//2)*self.D((j-1)//2),s.S.Zero
            return s.S.Zero,-6*(-1)**(j//2)*self.F(j-1)
        if typ=='d' and other=='a':
            dot,kap=self.table(g,f);return dot,-kap
        m=i+j
        if typ==other:
            if m%2==0:return (-1)**(i+m//2)*(s.Integer(radial(m//2)) if typ=='a' else self.D(m//2)),s.S.Zero
            return s.S.Zero,(-1)**(i+(m+1)//2)*(ODD[m] if typ=='a' else self.F(m))
        if m%2:return s.Rational((-1)**(i+(m+1)//2)*radial((m+1)//2),3),s.S.Zero
        return s.S.Zero,(-1)**(i+m//2+1)*ODD[m+1]/3

    @staticmethod
    def collect(items):
        out={}
        for word,value in items:
            out[word]=out.get(word,0)+value
        return {word:s.expand(value) for word,value in out.items() if value!=0}

    @lru_cache(None)
    def left(self,i,word):
        if not word:return {(i,):s.S.One}
        j=word[0]
        if i<j:return {(i,)+word:s.S.One}
        if i==j:return {word[1:]:self.table(i,i)[0]}
        items=[((j,)+w,-value) for w,value in self.left(i,word[1:]).items()]
        items.append((word[1:],2*self.table(i,j)[0]))
        return self.collect(items)

    @lru_cache(None)
    def normal(self,word):
        out={():s.S.One}
        for i in reversed(word):
            out=self.collect((w,x*y) for v,x in out.items() for w,y in self.left(i,v).items())
        return out

    def product(self,a,b,adjoint_first=False):
        return self.collect((v,(s.conjugate(x) if adjoint_first else x)*y*z)
                            for w,x in a.items() for u,y in b.items()
                            for v,z in self.normal((w[::-1] if adjoint_first else w)+u).items())

    def step(self,poly):
        items=[]
        # [H0, .] is an ordinary derivation because H0 is even.
        for word,x in poly.items():
            for position,field in enumerate(word):
                typ,power=self.labels[field]
                new=self.lookup[('d',0)] if typ=='w' else self.lookup[(typ,power+1)]
                factor=6*s.I if typ=='w' else s.I
                rewritten=word[:position]+(new,)+word[position+1:]
                items.extend((w,x*factor*z) for w,z in self.normal(rewritten).items())
        # The defect B_A=i gamma(a)gamma(d) multiplies on the left.
        for word,x in poly.items():
            rewritten=(self.lookup[('a',0)],self.lookup[('d',0)])+word
            items.extend((w,s.I*x*z) for w,z in self.normal(rewritten).items())
        return self.collect(items)

    @lru_cache(None)
    def wick(self,word):
        if not word:return s.S.One
        if len(word)%2:return s.S.Zero
        i=word[0];value=s.S.Zero
        for position in range(1,len(word)):
            j=word[position];dot,kap=self.table(i,j)
            value+=(-1)**(position-1)*(dot+s.I*kap)*self.wick(word[1:position]+word[position+1:])
        return s.expand(value)

    def expectation(self,poly):
        return s.expand(sum(x*self.wick(word) for word,x in poly.items()))

    def moments(self,ward,max_n=10):
        state={(self.lookup[('w',0)],):s.S.One} if ward else {():s.S.One}
        states=[state]
        for _ in range((max_n+1)//2):states.append(self.step(states[-1]))
        values=[]
        for n in range(max_n+1):
            left=n//2;right=n-left
            values.append(self.expectation(self.product(states[left],states[right],adjoint_first=True)))
        return values,[len(x) for x in states]

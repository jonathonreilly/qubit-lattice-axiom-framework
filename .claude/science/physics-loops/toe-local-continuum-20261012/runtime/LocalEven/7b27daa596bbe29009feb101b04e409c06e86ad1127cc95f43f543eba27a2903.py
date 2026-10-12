"""Fixed compact polynomial fixtures and their independently integrated transforms."""
import importlib.util, json, math, pathlib
import numpy as np
from numpy.polynomial import Polynomial as Poly
from scipy.special import spherical_jn

def load_candidate(path):
    spec = importlib.util.spec_from_file_location('candidate_under_test', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class Field:
    def __init__(self, center, radius, even, odd):
        self.center, self.radius = center, radius
        self.even, self.odd = np.array(even), np.array(odd)
        b = Poly([1, 0, -1])**4
        self.polys = [b*Poly([x,y]) for x,y in zip(even,odd)]

    @property
    def support(self):
        return self.center-self.radius, self.center+self.radius

    def value(self, x, derivative=0):
        x=np.asarray(x)
        y=(x-self.center)/self.radius
        out=np.stack([p.deriv(derivative)(y)/self.radius**derivative for p in self.polys],axis=-1)
        return np.where((np.abs(y)<1)[...,None], out, 0)

    def integral(self, lo, hi, derivative=0):
        yl=np.clip((np.asarray(lo)-self.center)/self.radius,-1,1)
        yh=np.clip((np.asarray(hi)-self.center)/self.radius,-1,1)
        return self.radius**(1-derivative)*np.stack([p.deriv(derivative).integ()(yh)-p.deriv(derivative).integ()(yl) for p in self.polys],axis=-1)

    def norm(self, derivative=0):
        x,w=np.polynomial.legendre.leggauss(32)
        f=self.value(self.center+self.radius*x,derivative)
        return float(np.sqrt(self.radius*np.sum(w*np.sum(np.abs(f)**2,axis=-1))))

    def fourier(self, q):
        q=np.asarray(q)
        z=q*self.radius
        az=np.abs(z)
        safe=np.where(az==0,1,az)
        even=spherical_jn(4,az)/safe**4
        odd=np.sign(z)*spherical_jn(5,az)/safe**4
        even=np.where(az==0,1/(1*3*5*7*9),even)
        return (self.radius*2**5*math.factorial(4)/np.sqrt(2*np.pi)*np.exp(-1j*q*self.center))[...,None]*(even[...,None]*self.even-1j*odd[...,None]*self.odd)

FIELDS=[
    Field(-.31,1.17,[1.,.43],[.27,-.19]),
    Field(.46,.91,[.24,-.82],[-.31,.16]),
    Field(-.77,.73,[-.38,.64],[.21,.33]),
    Field(.83,1.03,[.61,.17],[-.23,.28]),
]

def cell_coefficients(candidate, field, n, a):
    return candidate.cell_factor(a)*field.integral(a*n,a*(n+1))

def row(label,value,bound,tolerance=2e-10):
    value=float(value); bound=float(bound)
    return {'label':label,'value':value,'bound':bound,'numerical_slack':tolerance,'passed':value <= bound+tolerance}

def finish(payload,output):
    rows=payload['rows']
    payload['summary']={'passed':sum(r['passed'] for r in rows),'failed':sum(not r['passed'] for r in rows)}
    pathlib.Path(output).write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
    raise SystemExit(0 if payload['summary']['failed']==0 else 1)

def complex_pair(z):
    return [float(np.real(z)),float(np.imag(z))]

"""Exact local-star spectrum and periodic pi-flux sign controls."""
from pathlib import Path
from itertools import product
from datetime import datetime,timezone
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent

def star(d):
    z=2*d
    L=s.zeros(z)
    for i in range(z):
        for j in range(i+1,z):
            if i//2!=j//2:
                L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    expected={s.Integer(0):1,s.Integer(z-2):d,s.Integer(z):d-1}
    assert L.eigenvals()==expected
    return {'dimension':d,'coordination':z,'exact_star_eigenvalues':{str(k):v for k,v in expected.items()}}

def flux(periods):
    d=len(periods)
    def shift(x,j):
        y=list(x);y[j]=(y[j]+1)%periods[j];return tuple(y)
    def nu(x,j):return sum(x[:j])%2
    total=0;charge_controls=0;wrap=0
    for x in product(*[range(L) for L in periods]):
        for i in range(d):
            for j in range(i+1,d):
                vals=[nu(x,i),nu(shift(x,i),j),nu(shift(x,j),i),nu(x,j)]
                signs=[1,1,-1,-1]
                assert sum(a*b for a,b in zip(vals,signs))%2==1
                if any(x[k]==periods[k]-1 for k in [i,j]):wrap+=1
                if sum(x)%2:
                    vals=vals[1:]+vals[:1];signs=signs[1:]+signs[:1]
                for qa,qc in product((-1,1),repeat=2):
                    increments=[-qa,-qa,-qc,-qc]
                    exponent=sum(v*sgn*delta for v,sgn,delta in zip(vals,signs,increments))
                    assert exponent%2==1
                    charge_controls+=1
                total+=1
    return {'periods':periods,'plaquettes':total,'wrapping_plaquettes':wrap,
            'charge_dependent_exchange_parity_checks':charge_controls,
            'all_exchange_signs_reversed':True}

def main():
    out={'created_utc':datetime.now(timezone.utc).isoformat(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'star_spectra':[star(d) for d in range(2,7)],
         'periodic_pi_flux':[flux(p) for p in [(6,6),(6,8),(6,6,6),(6,8,10)]],
         'analytic_identity':'The electric-basis unitary exp(i*pi*sum_e nu_e E_e) commutes with Gauss and electric energy and maps every R_p to -R_p, since all transported charges are odd integers.',
         'scope':'An overall magnetic-sign change alone gives a unitarily equivalent rotor target on these even boxes. This is not a derivation of a complete fermionic microscopic model.'}
    text=json.dumps(out,indent=2)+'\n';(HERE/'CHARGED_BAND_GEOMETRY_RESULTS.json').write_text(text);print(text,end='')
if __name__=='__main__':main()

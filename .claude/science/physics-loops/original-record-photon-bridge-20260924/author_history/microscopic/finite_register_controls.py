#!/usr/bin/env python3
"""Separate five-level selection-rule/order-of-limits and grid controls.
No cube, rotor photon, or parent numerical builder is imported.
"""
from pathlib import Path
import hashlib,json,time
import mpmath as mp
import sympy as sp
mp.mp.dps=80

def selection_rules():
    W=sp.diag(0,1,0,1,0);N=sp.diag(0,0,2,2,4);P=sp.diag(1,0,1,0,1)
    T=sp.zeros(5);C=sp.diag(1,0,1,0,0);j=sp.zeros(5)
    T[0,1]=T[1,0]=T[2,3]=T[3,2]=-1;j[2,1]=j[4,3]=1
    assert W*j-j*W==-j and j*P==sp.zeros(5)
    assert N*j-j*N==2*j and N*T==T*N and C*W==W*C
    A=W*T*P;M=A.T*A;C0=P*C*P
    H2=C0-M;H4=M*M-(M*C0+C0*M)/2+A.T*(W*C*W)*A
    Beff=-P*j*W*T*P
    assert H2==H4==sp.zeros(5)
    assert Beff[2,0]==Beff[4,2]==1 and sum(abs(v) for v in Beff)==2
    # Fixed-bin word append is isometric on legal prefixes; the terminal
    # missing image is irrelevant because the corresponding physical j=0.
    words=[(),(0,),(1,),(0,0),(0,1),(1,0),(1,1)]
    checked=0
    for symbol in (0,1):
        images=[w+(symbol,) for w in words if len(w)<2]
        assert len(images)==len(set(images));checked+=len(images)
    assert j[:,4]==sp.zeros(5,1)
    return {'states':['P0','Q0','P1','Q1','P2'],'H2_zero':True,'H4_zero':True,
            'effective_transitions':[[0,2,1],[2,4,1]],'legal_append_images_checked':checked,
            'scope':'Separate abstract parent-class finite model; not the actual cube.'}

def waiting_cdf(epsilon,delta,kappa,u):
    e=epsilon
    a=-1j*delta/e**2;d=-1j*delta/e**4-kappa/(2*e**2);off=1j*delta/e**3
    tr=a+d;det=a*d-off*off;root=mp.sqrt(tr*tr-4*det)
    ls,lf=sorted(((tr+root)/2,(tr-root)/2),key=abs)
    ce=off/(ls-lf)
    def integ(z):return mp.expm1(z*u)/z if z else u
    value=kappa/e**2*abs(ce)**2*(integ(2*mp.re(ls))+integ(2*mp.re(lf))-2*mp.re(integ(ls+mp.conj(lf))))
    assert abs(mp.im(value))<mp.mpf('1e-65')
    value=mp.re(value)
    assert -mp.mpf('1e-60')<=value<=1+mp.mpf('1e-60')
    return value

def waiting_controls():
    delta=mp.mpf(1);kappa=mp.mpf('.7');t=mp.mpf('.3');h=mp.mpf('.4');b=mp.mpf('.1')
    target=(mp.exp(-kappa*t)-mp.exp(-kappa*(t+h)))*(-mp.expm1(-kappa*b))
    rows=[]
    for se in ('.4','.2','.1','.05','.025','.0125'):
        e=mp.mpf(se);F=lambda u:waiting_cdf(e,delta,kappa,u)
        prob=(F(t+h)-F(t))*F(b);tiny=e**6;ratio=F(tiny)/(kappa*tiny)
        asympt=delta**2*e**4/3
        rows.append({'epsilon':se,'fixed_bin_probability':str(prob),'target_probability':str(target),
                     'fixed_bin_absolute_error':str(abs(prob-target)),
                     'shrinking_bin':str(tiny),'microscopic_CDF_over_kappa_bin':str(ratio),
                     'target_CDF_over_kappa_bin':str(-mp.expm1(-kappa*tiny)/(kappa*tiny)),
                     'ratio_to_predicted_small_bin_asymptotic':str(ratio/asympt)})
    assert mp.mpf(rows[-1]['fixed_bin_absolute_error'])<mp.mpf('1e-4')
    assert abs(mp.mpf(rows[-1]['ratio_to_predicted_small_bin_asymptotic'])-1)<mp.mpf('1e-6')
    assert mp.mpf(rows[-1]['microscopic_CDF_over_kappa_bin'])<mp.mpf('1e-7')
    return rows

def grid_controls():
    k=mp.mpf('.7');T=mp.mpf('1.2');t=mp.mpf('.3');h=mp.mpf('.4');b=mp.mpf('.1')
    exact=(mp.exp(-k*t)-mp.exp(-k*(t+h)))*(-mp.expm1(-k*b));rows=[]
    for mm in (6,12,24,48,96):
        eta=T/mm;lower=upper=mp.mpf(0);total=mp.mpf(0)
        for r in range(mm):
            x0=r*eta;x1=(r+1)*eta
            for s in range(r,mm):
                y0=s*eta;y1=(s+1)*eta
                if r==s:mass=mp.exp(-k*x0)*(1-mp.exp(-k*eta)*(1+k*eta))
                else:mass=eta*k*(mp.exp(-k*y0)-mp.exp(-k*y1))
                total+=mass
                intersects=x1>t and x0<t+h
                subset=x0>=t and x1<=t+h
                minlag=max(mp.mpf(0),y0-x1);maxlag=y1-x0
                if intersects and minlag<=b:upper+=mass
                if subset and maxlag<=b:lower+=mass
        assert abs(total-(1-mp.exp(-k*T)*(1+k*T)))<mp.mpf('1e-65')
        assert lower<=exact+mp.mpf('1e-65') and exact<=upper+mp.mpf('1e-65')
        assert upper-lower<=8*k*eta
        rows.append({'bins':mm,'mesh':str(eta),'lower':str(lower),'exact':str(exact),
                     'upper':str(upper),'sandwich_gap':str(upper-lower),
                     'proved_loose_gap_bound':str(8*k*eta),'all_two_event_word_mass':str(total)})
    return rows

def main():
    start=time.monotonic();result={'scope':'Separate finite penalty model and target time-grid control, not cubic photon propagation',
       'selection_rules':selection_rules(),'waiting_rows':waiting_controls(),'grid_rows':grid_controls(),
       'elapsed_seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    text=json.dumps(result,indent=2)+'\n';Path(__file__).with_name('FINITE_REGISTER_CONTROL_RESULTS.json').write_text(text);print(text,end='')

if __name__=='__main__':main()

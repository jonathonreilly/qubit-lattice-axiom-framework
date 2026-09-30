import math
z3=1.2020569031595942
def betas(nf):
    b0=11-2*nf/3; b1=102-38*nf/3
    b2=2857/2-5033*nf/18+325*nf**2/54
    b3=149753/6+3564*z3-(1078361/162+6508*z3/27)*nf+(50065/162+6472*z3/81)*nf**2+1093/729*nf**3
    return b0,b1,b2,b3
def run(al0,mu0,mu1,nf,steps=20000):
    b0,b1,b2,b3=betas(nf); a=al0/(4*math.pi)
    t0,t1=math.log(mu0**2),math.log(mu1**2); h=(t1-t0)/steps
    f=lambda a:-(b0*a**2+b1*a**3+b2*a**4+b3*a**5)
    for _ in range(steps):
        k1=f(a);k2=f(a+h*k1/2);k3=f(a+h*k2/2);k4=f(a+h*k3);a+=h*(k1+2*k2+2*k3+k4)/6
    return a*4*math.pi
for mt in (163.0,172.57):   # MSbar mass ~163 or pole ~172.6 as threshold
    amt=run(0.1180,91.1876,mt,5); av=run(amt,mt,246.2828,6)
    print(f"threshold {mt}: alpha_s(mt)={amt:.5f}  alpha_s(v)={av:.5f}  (attack 2-loop 0.10313; plaquette 0.10330)")

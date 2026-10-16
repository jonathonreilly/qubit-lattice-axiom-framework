"""Exact shell projection, differential elimination and synthetic rank diagnostic."""
import sympy as s
import mpmath as mp


def controls():
    N,r,k,c=s.symbols('N r k c',positive=True)
    chi=s.Function('chi')(N)
    f=s.Function('f')(N,r)
    checks=[]
    def check(name,value,**detail):
        checks.append(dict(name=name,passed=bool(value),**detail))
    def K(z):return r*s.diff(z,r)
    def D(z):return s.diff(z,r)/r
    def E(z,cc=chi):
        alpha=r*r/(4*cc*cc)
        return alpha*(K(z)+2*z)-z
    def P(z):
        for shift in [-4,-2,0,2]:z=s.expand(K(z)+shift*z)
        return z
    def Q(z,cc=chi):return P(E(E(D(z),cc),cc))
    def zero(z):return s.simplify(s.expand(z))==0
    g=-2*s.diff(chi,N)/chi
    check('changing_shell_operator',zero(s.diff(E(f),N)-E(s.diff(f,N))-g*(E(f)+f)))
    U=E(D(f))
    check('radial_potential_elimination',zero(E(s.diff(U,N))-g*(E(U)+U)-E(E(D(s.diff(f,N))))))
    check('commutator_cannot_be_omitted',not zero(E(s.diff(U,N))-E(E(D(s.diff(f,N))))))
    check('operator_order_is_material',not zero(P(E(r**6,c))-E(P(r**6),c)))
    check('kernel_is_smooth_nonzero_on_positive_r',zero(E(r**-2*s.exp(-2*c*c/r**2),c)))
    check('annihilator_roots',all(zero(P(r**n)) for n in [-2,0,2,4]))
    check('annihilator_does_not_kill_all_signals',not zero(Q(r**6,c)))
    aa,bb=s.Function('aa')(N),s.Function('bb')(N)
    css=aa+bb*r*r;du=aa/r**2+bb;uu=aa+bb*r*r
    check('shear_low_modes_A',zero(Q(css)) and zero(Q(s.diff(css,N))))
    check('shear_velocity_low_modes_B',zero(P(E(E(du)))) and zero(P(E(E(s.diff(du,N))))))
    check('velocity_low_modes_C',zero(P(E(uu))) and zero(P(E(s.diff(uu,N))-g*(E(uu)+uu))))
    # Cartesian differentiation, before substituting two rational unit directions.
    z=s.symbols('z0:3');w=s.symbols('w0:3');rad2=sum((z[i]-w[i])**2 for i in range(3))
    n1=s.Matrix([1,0,0]);n2=s.Matrix([s.Rational(3,5),s.Rational(4,5),0])
    subs={**{z[i]:c*n1[i] for i in range(3)},**{w[i]:c*n2[i] for i in range(3)}}
    rr=s.sqrt(s.Rational(4,5))*c
    cart=[]
    for degree in [2,4,6,8]:
        corr=rad2**(degree//2)
        cross=sum(n2[i]*s.diff(corr,w[i]) for i in range(3)).subs(subs)
        vel=sum(n1[i]*n2[j]*s.diff(corr,z[i],w[j]) for i in range(3) for j in range(3)).subs(subs)
        cart.append(zero(cross-(r/(2*c)*s.diff(r**degree,r)).subs(r,rr)))
        cart.append(zero(vel-E(D(r**degree),c).subs(r,rr)))
    check('direct_Cartesian_radial_projection',all(cart),comparisons=len(cart))
    mu=s.symbols('mu',real=True);C=s.Function('C')(N,r)
    rshell=chi*s.sqrt(2*(1-mu));angular=C.subs(r,rshell)
    pull=s.diff(angular,N)+2*(1-mu)*s.diff(chi,N)/chi*s.diff(angular,mu)
    chain=zero(s.diff(rshell,N)+2*(1-mu)*s.diff(chi,N)/chi*s.diff(rshell,mu))
    explicit=N**2*r**3+s.sin(N)*r**4
    angular_explicit=explicit.subs(r,rshell)
    chain_fixture=zero(s.diff(angular_explicit,N)+2*(1-mu)*s.diff(chi,N)/chi*s.diff(angular_explicit,mu)-s.diff(explicit,N).subs(r,rshell))
    check('fixed_separation_light_cone_derivative',chain and chain_fixture)
    # Flat Born Volterra kernel; polynomial modes regular at the observer.
    src,ell=s.symbols('src ell',positive=True)
    lens=[]
    for n in range(2,9):
        psi=s.integrate((src-ell)/(src*ell)*ell**n,(ell,0,src))
        lens.append(zero(s.diff(src**2*s.diff(psi,src),src)-src**n))
    check('lensing_inverse_regular_modes',all(lens),comparisons=len(lens))
    # A spatially invariant coefficient law implies the covariance identity.
    x,y,m,h=s.symbols('x y m h',real=True)
    SS,SV,VV,ST,VT=s.symbols('SS SV VV ST VT',real=True)
    SS1=-(2+x)*SS-y*ST-2*m*SV
    SV1=(h-1-x/2)*SV-SS/2-ST/2-y*VT/2-m*VV
    VV1=2*h*VV-SV-VT
    a0=(y-x-2)/2;c0=-h*y-m
    check('separated_covariance_constraint',zero((SS1-2*y*SV1+y*y*VV1)/2-a0*SS-(c0-a0*y)*SV+c0*y*VV))
    row=[SS/2,-SS/2-SV1+(h-1)*SV,VV1/2+SV/2-h*VV,SV,-VV]
    lift=[x,y,y*y,m-x*y/2,m*y]
    check('lifted_row',zero(sum(a*b for a,b in zip(row,lift))+SS1/2+SS))
    # Sufficient-rank diagnostic from actual homogeneous isotropic bounded ensembles.
    # Every shell has a positive definite (S,V,T) covariance; its radial kernel is j0.
    mp.mp.dps=90
    cov=[s.eye(3) for _ in range(5)]
    for i,ij,delta in [(1,(0,0),s.Rational(1,2)),(2,(0,1),s.Rational(1,4)),(3,(0,2),s.Rational(1,5)),(4,(1,2),s.Rational(1,6))]:
        a,b=ij;cov[i][a,b]+=delta
        if a!=b:cov[i][b,a]+=delta
    check('shell_covariances_positive_definite',all(all(v[:j,:j].det()>0 for j in [1,2,3]) for v in cov))
    event={x:s.Rational(3,50),y:s.Rational(2,5),m:s.Rational(28,15),h:s.Rational(-2,7)}
    kernel=Q(s.sin(k*r)/(k*r),c)
    kfun=s.lambdify((r,k,c),kernel,'mpmath',cse=True)
    mats=[];rhs=[];data=[]
    for radius in ['0.5','1','1.5','2','2.5','3']:
        dd=[mp.mpf('0')]*6
        for i,cv in enumerate(cov):
            loc={SS:cv[0,0],SV:cv[0,1],VV:cv[1,1],ST:cv[0,2],VT:cv[1,2],**event}
            vals=[loc[SS],loc[SV],loc[VV],SS1.subs(loc),SV1.subs(loc),VV1.subs(loc)]
            fq=kfun(mp.mpf(radius),mp.mpf(i+1)*mp.mpf('0.4'),mp.mpf('3'))
            dd=[a+fq*mp.mpf(str(b)) for a,b in zip(dd,vals)]
        A,B,C,A1,B1,C1=dd;hh=mp.mpf('-2')/7
        rr=[A/2,-A/2-B1+(hh-1)*B,C1/2+B/2-hh*C,B,-C]
        mats.append(rr);rhs.append(-A1/2-A);data.append(dd)
    mat=mp.matrix(mats[:5]);bvec=mp.matrix(rhs[:5]);got=mp.lu_solve(mat,bvec)
    expected=mp.matrix([mp.mpf(str(q.subs(event))) for q in lift])
    err=max(abs(got[i]-expected[i]) for i in range(5))
    holdout=abs(sum(mats[5][j]*got[j] for j in range(5))-rhs[5])
    check('synthetic_five_separation_inverse',err<mp.mpf('1e-65'),error=str(err),determinant=str(mp.det(mat)))
    check('reserved_sixth_separation',holdout<mp.mpf('1e-60'),residual=str(holdout))
    result={'scope':'Exact operator controls and synthetic homogeneous ensemble; no measured data, no empirical test','checks':checks,'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks),'synthetic':{'event':{str(k):str(v) for k,v in event.items()},'chi':'3','wave_numbers':['0.4','0.8','1.2','1.6','2.0'],'calibration_separations':['0.5','1','1.5','2','2.5'],'reserved_separation':'3','precision_decimal':90,'condition_inf':str(mp.mnorm(mat,'inf')*mp.mnorm(mat**-1,'inf')),'lift':[str(z) for z in got],'data':[[str(v) for v in z] for z in data]}}
    return result

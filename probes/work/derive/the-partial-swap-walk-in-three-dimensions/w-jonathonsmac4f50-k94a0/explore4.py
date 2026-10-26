import numpy as np
g=0.004;T=30.0
cases=[((1,0,0),(0,0,1)),((1,1,0),(0,0,1)),((1,-1,0),(1,1,1)),((1,1,-2),(1,1,1)),((2,1,0),(1,-2,3))]
meas={0.5:[-0.1185,-0.1109,-0.1114,-0.1111,-0.1149],0.25:[-0.2259,-0.2225,-0.2242,-0.2220,-0.2257]}
for k0 in (0.5,0.25):
    for idx,(m,gr) in enumerate(cases):
        m=np.array(m,float);m/=np.linalg.norm(m);gr=np.array(gr,float);gr/=np.linalg.norm(gr)
        k=k0*m
        d=np.sin(k);dn=np.linalg.norm(d);n=d/dn
        Cm=np.cos(k)
        gw=g*gr
        dv=-(Cm/(2*dn))*np.cross(Cm*gw,n)   # lattice adiabatic
        # wait: formula Delta v_j = -(c_j/(2|d|)) * sum_a c_a dw_a (e_a x n)_j
        v=np.zeros(3)
        for a in range(3):
            ea=np.zeros(3);ea[a]=1
            v+= -(Cm/(2*dn))*Cm[a]*gw[a]*np.cross(ea,n)
        # group velocity direction for 'motion'
        vg=Cm*n   # c_j * n_j  (velocity of band |d|: d|d|/dk_j = c_j n_j)
        vg/=np.linalg.norm(vg)
        # component along (gradient x motion)
        dirn=np.cross(gr,vg);dirn/=np.linalg.norm(dirn)
        print(k0,idx,'lattice-pred',round(T*v@dirn,4),'long-wl',round(-g*T/(2*k0),4),'meas',meas[k0][idx], 'also transverse parts', np.round(T*v,4))

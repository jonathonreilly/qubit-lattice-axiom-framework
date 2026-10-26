from e7 import *
OFF,Sm=d4cone();C=CA(OFF,Sm)
n=np.array([.3,-.5,.6,.55]);n/=np.linalg.norm(n)
m=np.array([.5,.7,-.1,.2]);m-=n*(n@m);m/=np.linalg.norm(m)
# z = n + i s m, z.z = 1 - s^2 ; null at s=1
for s in (0.5,0.9,0.99,0.999,0.9999):
    z=n+1j*s*m;zz=z@z
    out=[]
    for t in (.02,.01,.005):
        q=t*z;K,Tl,Tr,w,wm,g1,g2=Kc(C,q,0.0)
        a=Fw(Tl,Tr,w,wm,-4,4/3);out.append(np.linalg.norm(K-a)/np.linalg.norm(a))
    ev=np.linalg.eigvals(C.Q(0.01*z)); 
    ev=ev[np.argsort(abs(ev))]
    print('s',s,'z.z',zz,'resid',out,'ratios',out[0]/out[1],out[1]/out[2],'|ev| 33..42/t^2:',np.round(abs(ev[32:42])/1e-4,3))

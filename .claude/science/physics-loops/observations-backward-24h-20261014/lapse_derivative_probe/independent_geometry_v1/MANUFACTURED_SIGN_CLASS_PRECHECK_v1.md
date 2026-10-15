# Independently checked manufactured sign-class fixture

This is a post-proposal check of root's new fixture, before reading its implementation. It does not replace the original pre-exposure derivation and does not assert a full candidate solution or observed geometry.

On a unit flat spatial ball, let ell=epsilon(1-r^2), N=exp(ell), w=1, z=N^lambda, zB=1, Nmin=1. All functions have regular even central expansions and the complete spherical boundary obeys z=1. Direct differentiation gives

    R4=12epsilon-8epsilon^2 r^2,
    C=4lambda^2 epsilon^2 r^2,
    L_N z+(lambda/2)R4 z=N^lambda C=S>=0.

Thus the proposed original and transformed scalar equations hold exactly with this prescribed nonnegative source. At the center S=0. This cannot be the full positive-Hv candidate source there: at z>1 its positive quartic potential already makes S_z>0. The fixture is legitimate for the sign-class comparison/restoration algorithm, but cannot serve as a candidate realization, existence witness, or an empirical test.

For lambda=117/49 and epsilon=1/100 the geometric envelope gives

    eta <= exp[(2lambda+1)epsilon] 4lambda^2 epsilon^2/6
         <= 169/418950 <1.

The exponential enclosure uses x=283/4900 in (0,1). Since exp(x)<=1/(1-x), this is an exact rational upper bound. If the full physical prefactor is omitted, P(0)<=eta implies the erroneous center cap is at most

    1/(1-eta) <=418950/418781 <1001/1000.

But the actual center satisfies

    z(0)=exp(lambda epsilon)>1+lambda epsilon
         =5017/4900>51/50.

The separation has ample exact margin and requires no computed Green solution or continuum numerical certificate.

The implementation must remove the same factor that this witness tests. In general the physical prefactor is (N/Nmin)^lambda. The earlier oscillatory code used ratio^lambda times Nhat^lambda because its lapse was normalized to Nmax=1. To reuse that factorization here, set Nhat=N/Nmax=exp(-epsilon r^2), so Nhat(0)=1, Nhat_min=exp(-epsilon), and ratio=Nmax/Nmin=exp(epsilon). Then ratio^lambda Nhat^lambda=(N/Nmin)^lambda and deleting ratio^lambda produces the failed cap above. Deleting only Nmin^(-lambda) while retaining raw N in this fixture would do nothing because raw Nmin=1. The new reusable function and actual mutation must make this normalization explicit.

`manufactured_sign_class_controls_v1.py` checks 15 exact identities/inequalities, all passing. It imports no author implementation and executes no author aggregate. The parent-reported surviving pointwise-factor mutation remains an implementation-coverage issue until the repaired function and actual mutation are inspected; this precheck does not by itself certify that repair.

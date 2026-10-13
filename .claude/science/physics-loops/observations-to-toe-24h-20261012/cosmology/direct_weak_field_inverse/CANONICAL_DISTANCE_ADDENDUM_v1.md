# A finite scalar-coordinate endpoint exposed by the first run

Parent /root, 2026-10-13. Same conditional action and physical scope.
The first numerical run failed while solving for phi_0+h on the null family.
It used an absolute h=0.001 even for k=10^-8. That step exceeds the finite
remaining canonical distance. There is no such field point, so increasing
root iterations or loosening the root tolerance would not repair the test.
The original runner, freeze and ValueError are preserved in evidence_v1.

For z>0 and 0<a<1/3, put h_a=1-3a>0 and Y=sqrt(1+h_a z).
The previously derived scalar line element gives

    d phi/dz=sqrt(1+h_a z)/[2 sqrt(a) z(1+z)].

With r=1/sqrt(z), the distance to z=infinity is the regular finite integral

    Delta_phi(z)=1/sqrt(a) integral_0^(1/sqrt(z))
                       sqrt(r^2+h_a)/(1+r^2) dr.     (12)

An equivalent elementary expression is

    Delta_phi=[atanh(1/Y)
              -sqrt(3a) atanh(sqrt(3a)/Y)]/sqrt(a).  (13)

To verify it, substitute Y in the line element. Its integrand becomes

    (1/sqrt(a))[1/(Y^2-1)-3a/(Y^2-3a)] dY.

The primitive vanishes as Y->infinity, giving (13).
Both arguments of atanh lie strictly between0 and1 in the stated domain.
For fixed a and large z, Delta_phi~sqrt[(1-3a)/(a z)].
On the null family k->0, a->1/4,z~1/k and Delta_phi~sqrt(k).
This explains why a fixed absolute step cannot test every null-family point.
It is a coordinate-range fact of the supplied classical kinetic geometry;
it does not establish a UV cutoff, a pathology, or quantum inconsistency.

The revised numerical protocol will set h to0.01,0.001,0.0001 times this
remaining distance, determined by the integral before solving the local
coordinate. It will compare the integral with (13) and check all requested
endpoints are within the positive kinetic domain. The symbolic first and
second derivative identities are unchanged.

Central derivative errors depend on the third and fourth local derivatives:
f(phi)=ln G_N(phi) has central first error h^2 f'''/6+O(h^4)
and central second error h^2 f''''/12+O(h^4). The revised diagnostic will
compare these leading terms and demand convergence as h shrinks. It does
not assume the original uniform100 h^2 bound across parameters, for which
no proof had been provided. The original bound was not reached in the
failed first run; the recorded failure was the unavailable endpoint.

# Equal-diagonal reference emitter: spectral measure check

The proposed density and its cotangent-coordinate form are correct for every j>0 and 0<kappa<j. The reference emitter's spectral measure is purely absolutely continuous, has full mass one on the chain band, and has no atoms. The proposed hard-band tail bound is valid for 0<sigma<pi/2. It is an upper bound, sometimes larger than one, and should then be capped by one. No actual converter mass, calibration, complete-output error or runtime follows from this reference calculation alone.

This is a source-exposed reconstruction: the parent supplied the candidate formula before the derivation. I independently obtained it from the half-line recurrence and checked normalization by a separate elementary integral. It is not an independent origin of the formula or a model-diverse check. Applicable local collaboration/workflow instructions from the coherent campaign were reused; this task is distinct from any unfinished full-device proposal. No external source, scientific execution, numerical integration, delegation, Git operation, W change or prompt/model edit was used. Only this report was written.

## Operator, branch and density

Use the basis e_0,e_1,..., with e_0 the emitter. All diagonals of H are 2j. The e_0--e_1 hopping is -kappa, and all subsequent hoppings are -j. Set L=H-2jI and define resolvents in the convention (z-L)^-1, so a positive spectral measure has negative imaginary part in the upper half-plane. The state whose measure is calculated is the unit basis vector e_0.

Let m(z) be the boundary Green function of the disconnected uniform chain beginning at e_1. Removing its first site leaves the same chain, giving

    m(z) = 1/(z-j^2 m(z)).

The physical solution is selected by m(z)~1/z at infinity:

    m(z) = [z-s(z)]/(2j^2),
    s(z)=sqrt(z^2-4j^2), analytic off [-2j,2j], s(z)~z.

This branch choice matters. It has s(x)>0 for x>2j and s(x)<0 for x<-2j. On the upper lip of the band its value is +i sqrt(4j^2-x^2) for every -2j<x<2j. Choosing the ordinary positive square root indiscriminately on both exterior intervals would be wrong.

Schur elimination at the emitter gives the exact scalar resolvent

    g(z)=<e_0,(z-L)^-1 e_0> = 1/[z-kappa^2 m(z)].

Parametrize the physical energy by E(q)=2j-2j cos(q), 0<q<pi; its shifted value is x=-2j cos(q), and dE/dq=2j sin(q)>0. On the upper boundary,

    m(x+i0) = -exp(iq)/j,
    x-kappa^2 m(x+i0) = -a cos(q)+i b sin(q),
    a=2j-kappa^2/j, b=kappa^2/j.

Here a>j>0 and 0<b<j. Stone's sign is -Im g/pi, so the density in energy is

    dmu/dE = b sin(q) / [pi(a^2 cos^2(q)+b^2 sin^2(q))].

Multiplying by dE/dq gives precisely

    dmu/dq = 2 kappa^2 sin^2(q)
              /[pi(a^2 cos^2(q)+b^2 sin^2(q))].       (1)

This is the full probability density for the normalized emitter basis state; there is no additional Fourier factor, channel multiplicity or input-column norm. Equal diagonals do not mean zero onsite energy: the 2j shift is included in E(q), while only the resolvent variable above was centered.

## Atom absence and full mass: two checks

For a real shifted energy x>2j, the physical chain branch obeys 0<m(x)<=1/j. Thus

    x-kappa^2 m(x) >= 2j-kappa^2/j = a > 0.

For x<-2j, oddness gives m(x)<0 with |m(x)|<=1/j, and x-kappa^2 m(x)<0. Consequently no exterior pole occurs. At the band edges the denominators are respectively +a and -a, neither zero; the edge values of g are finite and cannot support atoms. In the band interior the denominator has imaginary part b sin(q)>0, so it has no real zero and the boundary Green function is smooth on every compact interior interval. Its explicit algebraic continuation then yields only the displayed absolutely continuous measure there. Any remaining singular measure could only be supported at the two edges, where there are no atoms. Thus the emitter measure is purely absolutely continuous.

There is also a direct full-mass integral that checks the normalization independently of the pole discussion. Put u=cot(q), to avoid confusing this coordinate with shifted energy x. Since dq=-du/(1+u^2), equation (1) becomes the positive density on the real u line

    dmu/du = 2 kappa^2
               /[pi(a^2 u^2+b^2)(1+u^2)].           (2)

The orientation reversal q:0→pi, u:+infinity→-infinity is absorbed by the positive measure. Since a>b>0 in the requested domain,

    1/[(a^2 u^2+b^2)(1+u^2)]
      = [a^2/(a^2 u^2+b^2)-1/(1+u^2)]/(a^2-b^2).

Integrating over the real line gives

    integral du/[(a^2 u^2+b^2)(1+u^2)] = pi/[b(a+b)].

Because a+b=2j and b=kappa^2/j,

    integral dmu = 2 kappa^2/[b(a+b)] = 1.           (3)

The scalar spectral measure of a unit vector has total mass one; alternatively g(z)~1/z fixes that normalization. Combining the local density formula with its integral (3) alone leaves no mass for missing atoms or singular components. One must not infer atom absence merely from g(z)~1/z before accounting for the density's integral. The two arguments above make that distinction explicit.

Since kappa and j are nonzero, successive applications of L to e_0 generate the finitely supported basis vectors recursively. Thus e_0 is cyclic for this Jacobi operator. The emitter-measure conclusion is not concealing an uncoupled dark eigenvector in this particular reference operator. This cyclicity claim would fail at kappa=0.

## Exact hard-band tail and the proposed upper bound

Let 0<sigma<pi/2, and t=tan(sigma)>0. The central momentum interval [pi/2-sigma,pi/2+sigma] corresponds to |u|<=t. Its exterior mass is therefore exactly

    p_out = (4 kappa^2/pi)
              integral_t^infinity du/[(a^2 u^2+b^2)(1+u^2)].

Since a^2 u^2+b^2 >= a^2 u^2 and 1+u^2>=1,

    p_out <= 4 kappa^2/(pi a^2 t)
           = 4 kappa^2/[pi a^2 tan(sigma)].          (4)

The inequalities are strict for the stated open parameter domain, although the proposed non-strict upper bound is of course valid. A universally useful reported ceiling is min{1, right side of (4)}. This is a probability bound; the corresponding exterior component's Hilbert norm is sqrt(p_out), not p_out.

For a sharper exact comparison, partial fractions give

    p_out = 4 kappa^2/[pi(a^2-b^2)]
      * [(a/b) arctan(b/(a t)) - (pi/2-sigma)].      (5)

Here a^2-b^2=4(j^2-kappa^2)>0. Equation (5) is well-defined in the requested domain, but the two bracket terms may nearly cancel; that is a numerical conditioning issue if it is later evaluated, not a new measure premise. No numerical evaluation was used in this check.

For fixed sigma in (0,pi/2), the exact small-kappa asymptotic is

    p_out / kappa^2 → [cot(sigma)+sigma-pi/2]/(pi j^2).

The coefficient is positive: cot(sigma)>pi/2-sigma on this interval. The upper bound (4) instead has limiting coefficient cot(sigma)/(pi j^2), so it is a correct but not sharp fixed-band leading estimate. In the narrow-band, weak-coupling regime kappa^2/j^2 << sigma << 1, the leading behavior is p_out approximately kappa^2/(pi j^2 sigma). The central momentum width is of order b/a approximately kappa^2/(2j^2), not of order kappa/j. This asymptotic description is not uniform when sigma shrinks to that linewidth scale. At fixed nonzero kappa, sigma→0 makes the actual p_out approach one while (4) diverges; the cap by one is then essential for a useful bound.

## Domain and limits of transfer

At sigma=pi/2 the band is the entire open chain band and exterior mass is zero; interpret (4) only by its limiting zero value, rather than evaluating tan(pi/2). For sigma>pi/2 the target interval already contains the band and the displayed tangent formula is not the appropriate bound. At sigma=0 there is no nontrivial central interval and no finite bound of the form (4). Thus the stated sigma domain must accompany the formula.

At kappa=0 the emitter is decoupled and its measure is a unit atom at E=2j; the density formula cannot be extended by naive pointwise substitution. As kappa tends to zero through positive values, its probability measures concentrate there. The requested strict kappa>0 excludes this counterexample. The formula is also continuous at kappa=j, where the equal-hopping reference reduces to the usual boundary chain density, but the partial-fraction expression (5) then requires a limit. No extension beyond the requested domain is needed here.

This is an exact reference-model statement. The proof used its uniform semi-infinite chain, equal diagonals, single emitter coupling and emitter basis seed. A different attached converter can change the endpoint self-energy, the spectral type and the exterior mass. Neither the reference's mass-one identity nor its tail coefficient can be substituted for those of a converter without an additional proved comparison. No complete-output/runtime conclusion, physical supplier, retained status or global no-go follows from this report.

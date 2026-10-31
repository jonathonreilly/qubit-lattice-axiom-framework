# Affected principal-log chart check

Declared after the independent initial checks and author checker inspection, before the witness code. Source initially reviewed: SHA256 7b579f43ff7c04dd922f652c76cb3a1b9a4add3d64d0bf29d6abf0e04f038296, lines 363–367. New issue exposed by analytic domain examination, not by tuning a failed numerical result.

For SU(3), examine the center U=exp(2 pi i/3) I and r=4. Its usual matrix principal logarithm has HS norm 2 pi/sqrt(3)<r and trace 2 pi i, but every traceless anti-Hermitian logarithm has HS norm at least 2 pi sqrt(2/3)>r. The SU(N) HS injectivity radius is pi sqrt(2): the first eigenvalue collision modulo 2 pi has difference 2 pi, costing norm at least pi sqrt(2), attained at diag(pi i,-pi i,0,...). Therefore an injective su(3) exponential ball of radius4 does not equal the event defined only by matrix-principal-log norm<4.

Check the determinant, principal trace and norm, traceless logarithm minimum through exact integer-lift reasoning with a finite sanity enumeration, and explicit exp equality. Numerical tolerance2e-11. The algebraic minimum uses sum k_j=-1 and sum k_j^2>=1, not a claim that a finite search proves all lifts. A strict norm margin gives a positive-measure neighborhood. A crossing link carrying U with internal tree links I passes the original interior-only cuts.

Repair candidate: explicitly define Omega_r as the image of the traceless Lie-algebra ball under the injective exponential map; if standard matrix principal logarithms are used, restrict r<min(injectivity radius,2 pi/sqrt(N)) and require tracelessness. Do not silently replace the original integral with a different event or claim that this affects the already checked quadratic precision.

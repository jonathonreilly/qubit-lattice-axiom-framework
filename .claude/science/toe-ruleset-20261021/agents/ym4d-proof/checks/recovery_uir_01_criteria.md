# Exact block-matching and infrared-degree checks

Pre-stated before writing/running `recovery_uir_01.py`. Target: UIR2_55 §1.6's displayed J_LS identification, not actual Yang–Mills rho-null.

A. Build polynomial 3-by-3 matrices over rational coefficients using the Leibniz determinant, independently of the Schur formula. With W(t)=[[a,bt],[bt,c]], B(t)=(bt,0), test the PRINTED J_LS=[[W,B],[B^T,c]] against W⊕c. Record the equality as FAIL when it is false; do not hide that outcome in a renamed PASS. The exact predicted difference is −c b²t². Test a,c>0,b≠0 at three rational triples. This can refute the printed universal block identity; it cannot establish the actual field-theory matching.

B. Replace the fine block of J_LS by diag(a,c), keeping B. Its determinant must equal det(W⊕c) exactly. A control dropping the level-to-transverse coupling must fail at order two. For a=c=b=1 the half-log determinant difference for the printed matrix must have t² coefficient −1/2; the corrected matrix must have zero difference.

C. Check exponent classifications from the analytic four-dimensional two-centre lemma. Individual local pole exponents must be <4. Total degree six with (a,b)=(4,2) must be rejected as locally divergent despite its advertised total degree; (3,3) is admissible, (3,2) has integrated scale t^−1 but becomes negligible after multiplying by t². Exact integer exponent checks do not certify any actual diagram.

D. Verify the rational factors in the independent Feynman-parameter evaluation of the transverse super-marginal core. The analytic proof supplies radial integrals; the script checks only their rational coefficients. A wrong factor 1/4 in place of 1/2 must be rejected.

Outputs use integers/Fraction only and preserve failed assertions explicitly. No scientific status is granted by aggregate runner success.

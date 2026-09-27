# Exact square Schur reduction and calibration diagnostic

Working extension of JOINT_CORRECTION_DRAFT.md, same supplied closed square and joint scaling. No claim about a physical device is added.

On the fully-B W2 sector, field m has E=(m,-1-m,-1-m,m), m=-S,...,S-1. Each of its four incoming reverse hops has squared amplitude d_m=1-m(m+1)/C. A W1 source has only one empty B site that can be filled to reach W2, so distinct m never mix in BB*. Therefore BB*=4 diag(d_m).

Set lambda=x² E/delta. Woodbury applied to the preceding exact Schur equation gives, away from its poles,

 E(1+4x-lambda) psi = [4K n² - delta Z*R(E)^(-1)Z]psi,
 R_m(E)=(1-lambda)(2-lambda)-4x d_m.

This is an exact energy-dependent tridiagonal problem. Its diagonal is
4K n²-4delta[d_(n-1)²/R_(n-1)+d_n²/R_n],
and adjacent entry(n+1,n)=-4delta d_n²/R_n.
At n=-S,S the exterior d coefficients vanish exactly. Use no ghost coupling. Elimination requires lambda!=1,2 and invertible R. In the low strip with lambda<1 and R>0 these conditions hold and the eliminated Q block is positive. The P Schur inertia then counts eigenvalues of the original matrix; this provides a route to certifying root labels. The present numerical solver checks R>0 and positive scalar derivative but is not an interval-certified root proof.

Full dense and Schur calculations agree within the measured floating residuals at S20,50,120. At S1000 the tridiagonal method can resolve the small correction without forming a huge delta/epsilon⁴ diagonal and subtracting nearly equal eigenvalues. First-order residual divided by x² stabilizes near839 for K=delta=1 and2065 for delta/K31.607246 across the largest tested spins. Floating residuals and finite tests are not uniform remainder bounds.

## Calibration changes the relevant sign

No experimental values enter this diagnostic. Choose the model H0 at K=1, delta=31.607246 and use its first two excitation gaps as targets. Hellmann-Feynman derivatives of those gaps with respect to K,delta form J. If c_j=<j|H1|j>-<0|H1|0>, preserving the two calibration gaps requires J_(1,2) dp=-c_(1,2). The remaining first-order change is x(c+J dp).

At this ratio dp=(-2.86311018,154.40849098) per x. The four next model gaps have first-order changes +0.94659549,+4.05746208,+10.95440676,+24.77605154 per x. Their raw changes before calibration were negative. Independent-of-perturbation nonlinear fits of the exact finite-S Schur problem to the same two model targets, at S50,100,200,500, give positive changes and approach those derivatives. Full output and scripts accompany this draft.

These observations concern an isolated zero-offset mathematical model with two calibration coordinates. They do not establish the sign after the actual four-coordinate cavity/offset calibration, or for all spin values. They do establish why reading the raw frequency shift as a correction to the measured residual would be unjustified. Spin S (and hence x) remains an independent uncalibrated input. No parameter was selected by matching the already examined experimental higher lines.

Next decision: independently check these exact reductions and calibration derivatives; then either derive the physical offset/resonator/preparation map with controlled errors, or identify an independent physical scale observable. A fit to the same higher lines is not a solution to that obligation.

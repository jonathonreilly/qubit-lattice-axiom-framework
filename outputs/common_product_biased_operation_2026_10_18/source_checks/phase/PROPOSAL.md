# Inelastic phase envelopes for a future finite transfer

Provisional ROOT analytical lemma, not independently checked and not an operational theorem. This isolates the changed spatial phase from pending full packet construction. No old finite theorem is imported.

Assume |k-pi/2|<=h<=.001, r in[0,.001], q=acos(cos k+r/2), E=2j(1-cos k), j>0. Then sin k,sin q>.99, |cos k|<=.001, |cos q|<=.0015. Differentiating:

    q'=sin k/sin q;
    q''=(cos k-cos q (q')^2)/sin q;
    q'''=(-sin k+sin q (q')^3-3cos q q' q'')/sin q.

Consequently .99<q'<1/.99, |q''|<.003 and |q'''|<3. These deliberately loose uniform bounds include r=0. Also |E''|,|E'''|<=2j. Let ell>=1000, ell>=100u0, t0=u0/j, T=7ell/(8j), tminus=3ell/(4j), with u0>0. For a compactly supported C2 Hilbert-space-valued amplitude f(k) inside the stated k band, let Fa=integral||f^(a)(k)||dk, a=0,1,2. Define

    A_n(t)=(2pi)^(-1/2) integral exp(i[nq(k)+(ell+57)k-tE(k)]) f(k) dk.

The Hilbert norm accommodates full channel/program/reference coefficients. Smooth compact support kills the IBP boundary terms. All claims below use triangle inequalities, not component counting or spectral completeness.

One IBP with |phi'|>=g gives ||A_n|| <=(F1+F0 sup|phi''/phi'|)/(sqrt(2pi)g). Two give <=[F2+3F1 sup|phi''/phi'|+F0(sup|phi'''/phi'|+3sup|phi''/phi'|^2)]/(sqrt(2pi)g^2).

For t in[0,T] and n>=ell, phi'>=.99n-.75ell+57>=.24ell+.99(n-ell). Since |phi''|<=.003n+1.75ell, its ratio to this lower bound is<8. Summing n>=ell+1 with integral comparison gives sum g_n^-2 <=1/(.99*.24ell)<5/ell. Thus the far-positive tail norm is <=2(F1+8F0)/sqrt(ell).

For t in[tminus,T], n<=0, E'>1.98j gives -phi'>=.485ell-57+.99|n|>=.428ell+.99|n|. Here |phi''|<=.003|n|+1.75ell, ratio<5. Sum over n<=0 is bounded by (.428ell)^-2+1/(.99*.428ell)<3/ell. Thus the nonpositive tail norm is <=2(F1+5F0)/sqrt(ell). This includes n=0; it is the full-integer mathematical outgoing comparison, not a claim that physical negative F sites exist.

At t=t0 and n>=0, phi'>=.98ell+.99n, and |phi''|<=.003n+.02ell, ratio<1. Sum of inverse squares is <2/ell, so the early nonnegative outgoing tail norm is <=2(F1+F0)/sqrt(ell).

For finite-boundary levels n=ell,ell+1,ell+2 and t in[t0,T], phi'>=qbound(t)=1.99ell-2jt (dropping positive57). This is >=.24ell. The ratio |phi''/phi'| is<8 and |phi'''/phi'|<20: the latter follows [3(ell+2)+1.75ell]/(.24ell)<20 for ell>=1000. Consequently

    ||A_n(t)|| <= [F2+24F1+212F0]/[sqrt(2pi)(1.99ell-2jt)^2].

Its time integral multiplied by j is at most [F2+24F1+212F0]/[sqrt(2pi)*.48ell], using integral j/(a-2jt)^2 dt=(1/2)(1/qend-1/qstart). Any actual boundary operator norm and number-of-level/channel factors must still be supplied. No physical cut estimate is claimed just from this scalar envelope.

The amplitude is f=sqrt(q')g times scattering or error coefficients for outgoing record1. Its first and second derivatives require derivatives of all such coefficients; those remain the separate packet proof obligation. Incoming record0 uses q=k. A general full outgoing residual may contain both record channels and must use the corresponding coefficient maps and phases, not assign q to record0. For the ideal R0-to-R1 column the displayed phase includes the exact -i factor as part of f and shift57; restoring physical exp[-it(c+mu)] is separate.

These estimates suggest uniform boundary/tail constants at nonzero r, but establish no normalized exact network packet, endpoint-seed matching, finite observation theorem, flag fidelity, improved temperature or resource exponent. ROOT read the full old finite source7286105ffd9b6b6d0caa97b121c5e79d37dfcf638128d63c6bbc144e9aa2a995 and full new stationary network cdf35dd3f9a8ea32ce0b52745ac00756885dba014d67db7e12f706e58e63b666 (composition check pending). The present arithmetic/IBP estimates are new and need a distinct check before use. Same-model/source-exposed author work, no scientific executable or retained audit.

# PRE-STATED hostile review of QFIX

UTC registration: 2026-10-28T22:02:57.056497+00:00

Review status at registration: NOT-VERIFIED. No target derivation has yet been read or checked. Prior exposure consists of the owner's assignment, which states the claimed numbers and suspected failure modes. This is an independent Codex review; the author's model identity is not independently verified.

Targets and refutation criteria, registered before derivation:

1. Consumer census and domain: independently search the permitted source ranges for q, its aliases, and induced powers. One omitted consumer, one adverse q dependence, one finite upper restriction, or an unjustified universal quantifier refutes the corresponding census/domain claim. A bounded search cannot establish an unrestricted negative.
2. Exponent chain: rebuild the epsilon_1 cutoff and a_RS construction with each symbol tied to its local definition. A changed minimum branch, a q-dependent hidden factor, or a nonconstant a_RS/epsilon_1^4 refutes an exact power-law claim; five fitted rows alone establish none.
3. Inherited corrections: reconstruct the alleged sqrt(10) discrepancy and the c_N band from the actual stated constants. An incorrect normalization or unsupported exactness refutes the corresponding correction.
4. Objective curve: use only exact rational/symbolic arithmetic in plain Python, with rigorous rational enclosures for logarithms and fractional powers. Compare q = 8, 11, 12, 32, 100, 1000 and the limiting objective against independently reconstructed formulas. Printed precision and rounding are part of the claim.
5. Decisiveness: inspect every permitted qf1 check and ask what counterexample it can reject. Inputs copied from the proposed conclusion, tautological comparisons, absent failure conditions, and untested minima cannot validate the underlying proof claim.
6. Live currency: trace the actual consumer of a_RS and the programme ceiling within the permitted sources. If the live route does not consume a_RS, a gain for a historical diagnostic must not be sold as improvement of the live proof obligation. Missing access or missing derivation remains NOT-VERIFIED, never confirmation.

Execution boundary: no git commands, no .git access, no edits outside this deliverable, no numerical libraries or floating-point numerical checks, no snapshots or audit ledgers. Read the named target/checks and explicitly allowed EPSSTAR/CONST_T sections; choose no more than two additional scientific sources, recorded below. Instruction-only reads: the supplied Science Workflow entry point and the installed review-loop skill. The owner's narrower read/write scope controls this review; no landing, audit, or general skill workflow is executed.

## Source selection and findings (appended incrementally)

Scientific extra-source selection is pending inspection of the target's references. Every finding below uses CONFIRMED / NOT-VERIFIED / REFUTED; underlying claim grades use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN.

### Source selection

The two additional scientific files are **SQ.md** (independent q-consumer and norm-convention search) and **PROOF.md** (bounded searches and excerpts for the a_RS formula and actual live consumer). No other scientific files will be read beyond the explicitly named scope. Instruction-only files supply no scientific evidence.

### F01 — REFUTED: the registered structural gate was impossible as written

Attachment: QFIX.md:76; checks/qf1_criteria.md:66-67; checks/qf1_q.py:165-182.

QFIX's original QF1-3 requires all clauses, expressly including 4/q <= 1/2, to hold at q=5,6,8,10. Exact substitution gives 4/5 > 1/2 and 2/3 > 1/2. That original gate cannot pass. The later criteria remove this clause from QF1-3 and test it separately as QF1-3b. This is a corrected test definition, not confirmation of the original registration. The elementary floor q>=8 for that particular clause is PROVEN; the full admissible domain remains under review.

### F02 — REFUTED: the permitted script squares the required t_pr a second time

Attachment: checks/qf1_q.py:229,289-300,305-317; compare QFIX.md:394-410.

Write K=3.31*10^7, H=5.05*10^9 and T=2*epsilon_1*sqrt(H*C_3). From t_pr=1/(K*C_D^2) >= T, the ceiling is C_D <= (K*T)^(-1/2). Line 289 computes (K*T^2)^(-1/2), larger by T^(-1/2). Thus the permitted script's DESC-epsilon ceilings and P-ct clearance tests use the wrong inequality. QFIX's reported corrected ceiling may have come from a later script, but it is not validated by this script. Numerical correction and output provenance will be added after independent rational enclosure.

F02 provenance update: QFIX.md:469-479 explicitly discloses this same error and claims a correction in qf1b_q.py. That filename does not match the owner's permitted qf1_* scope and has not been read. F02 is a refutation of the preserved first script, **not a newly discovered undisclosed error in the target's corrected formula**.

### F03 — REFUTED: there is another opposing consumer, and strict global monotonicity fails even in the printed model

Attachment: QFIX.md:117,129-134,325,485-488; checks/qf1_q.py:98-123.

Set t=4/q, X=27*c_s and m=19615. The varying part of C_S1^2 is

    f(t) = (1-t)*(4t)^(t/(1-t))*X^(1/(1-t)).
    d(log f)/dt = log(4*X*t)/(1-t)^2.
    dt/dq = -4/q^2.

Thus A_c*gamma_c decreases for q<16X, has its minimum at q=16X=432*c_s, and **increases** for q>16X. With the declared rational c_s, the turning point is exactly 177950.7234219926762352. This is consumer #4, already in the census, misclassified as LARGE for all q. No new source or imported theorem is needed. Under P-max #2 is indifferent, and #13-14 are domain floors, so even before this reversal the table is not thirteen strictly improving consumers.

A stronger counterexample follows without evaluating enormous numbers. Write A=108*c_s, h=3/4-1/(4m), J=(1+sqrt(6))^2/(2*m^2*h)>0. Then the printed bracket is

    H(t)= A^(1/(1-t))/2 + J*(f(t)+4096*c_g)
          +288*(c_g+18*(3*c_s*64^(-2+2t)+1/(36m))).

As t decreases to zero, f(t)=X+X*t*log(t)+O(t); all other varying terms are analytic at t=0. Hence

    H(t)-H(0)=J*X*t*log(t)+O(t)<0

for sufficiently small positive t. Therefore C_T approaches its finite limit **from below** eventually, and cannot be strictly decreasing throughout q>=8. Lambda is analytic in t with positive finite limit, so C_D likewise approaches its limit from below eventually. The artificial a_RS objective therefore exceeds its claimed limiting supremum at some finite q. This is an asymptotic mathematical refutation, not a claim of a useful numerical improvement at practical q. Claim grade: PROVEN for the displayed model.

### F04 — REFUTED: the all-consumer objective omits an actual minimum and its finite-q restriction

Attachment: QFIX.md:44-49,170-172,197-198,271-272,303-325,370-374; checks/qf1_criteria.md:87-94; SQ.md:1586-1587,1608-1612,1622-1623,1633-1637; EPSSTAR.md:519-521.

The source requires q*beta<=1/2. For a fixed positive beta this is the explicit upper restriction q<=1/(2*beta). Uniform application at a fixed positive theta via beta<=C_beta*theta uses q<=1/(2*C_beta*theta). Allowing theta to shrink with q changes the question; it does not remove the restriction for a fixed consumer.

More directly, SQ defines theta_0=min(theta_G,theta_epsilon), then tau_R<=theta_0/C'. The target's own descendant threshold uses t_pr=C'*tau_flat with tau_flat<=tau_R (EPSSTAR's tau_R branch, lines 518-520). Consequently the compatible chain must include

    t_pr <= min(1/(3.31e7*C_D(q)^2), theta_epsilon(q), theta_G(q), other inherited thresholds),
    theta_G(q)=1.168e-12/q,
    epsilon_1_cut <= t_pr/(2*sqrt(5.05e9*C_3)).

The script instead sets t_pr equal to the first branch alone and expressly reports theta_G without optimizing it. At fixed positive epsilon_1, even the necessary t_pr>epsilon_1 imposes q<1.168e-12/epsilon_1 (q<1.7432835821e27 at 6.7e-40, conditional on the target's theta_G prefactor). If epsilon_1 follows the cutoff instead, then as q tends to infinity the compatible cutoff is O(1/q), and the proposed fourth-power objective tends to **minus infinity**, not -28.575. The advertised global endpoint optimum is REFUTED independently of F03.

There is also a local stale-minimum witness. At the epsilon_*=1.12e-37 floor repeatedly used in QFIX:144-145,317-319, theta_epsilon(q)=epsilon_*/(16*3.34*32^(1/q)). The reported t_pr already exceeds theta_epsilon at q=12 and by roughly 26 times at q=1000. The plotted curve needs a new, q-dependent epsilon_* floor or the missing min; it is not valid uniformly at the floor it cites. Numerical enclosures follow below. The ability to choose a larger epsilon_* satisfying all earlier constraints is NOT-VERIFIED here.

### F05 — REFUTED: the census omits the q-dependent input smallness hypothesis

Attachment: QFIX.md:107-129; SQ.md:1460-1468,1495,1512,1515.

Independent searches used the requested strings q/(q-4), 4/q, 8/q, 1/q, 32^{1/}, ell^q and B(4a), plus forms the target did not name: |S|^q, 16^{1/q}, 3-4/q, q*beta, C_T(N,q), epsilon_*(N,q), and the actual tau_R/tau_flat minima. The lattice EPS-T input requires R^(3-4/q)*||S||_q <= epsilon_*. This is not merely the condition q>4. For a fixed nonzero source supported at one site and R>1, its left side increases strictly with q: take s=epsilon_* R^(-3+4/q0); it meets equality at q0 and fails for every q>q0. This is an algebraic counterexample to treating the input test as improving for all fixed inputs, not a claim that an arbitrary isolated source is the divergence of an admissible Yang-Mills field. In the actual cone application the exponential-moment estimate controls this input by shrinking theta_G, precisely the dependency omitted from the objective in F04.

The table contains fourteen numbered rows; there is no proof that these are fourteen distinct exhaustive consumers, and two are domain floors. Exact lane-wide completeness is NOT-VERIFIED under the bounded read scope. Its assertion of exactly one adverse dependence is REFUTED by F03 and the input gate above.

### F06 — CONFIRMED as a fit; NOT-VERIFIED as the a_RS exponent theorem

Attachment: QFIX.md:256-264,496-500; checks/qf1_q.py:57-62,204-225.

Independent exact Fraction arithmetic on the five printed pairs gives the maximum relative error for p=4 as **[0.000175964866, 0.000175964867] percent**, at the fifth row. Thus 0.0002 percent is a correct rounded description. The maximum errors for p=3 and p=5 are [7138976.293664539735,7138976.293664539736] percent and [99.998599263490,99.998599263491] percent. Exactly one of p=1,...,6 meets the registered 0.2 percent tolerance. These rows span about five orders in epsilon_1; the fit is not confined to a tiny range, but remains a fit.

The implication epsilon_1_cut=t_pr/(2*sqrt(H*C_3)) follows by solving t_pr^2/H >= 4*C_3*epsilon_1^2 for positive epsilon_1. On the C_D branch with fixed H,C_3,K it gives epsilon_1_cut proportional to C_D^(-2), PROVEN algebraically. If a_RS=constant*epsilon_1^4 on the same branch, the composite exponent is indeed -8, CONDITIONAL. But a five-point fit does not prove that antecedent, especially below the smallest row, as q=8 extrapolates to approximately 3.7e-49.

A direct witness to non-identifiability: in x=epsilon_1/(6.7e-40), let x_i be the five positive rational sample values and set P(x)=product_i(x-x_i). For any proposed function a(x), the function a(x)*(1+lambda*P(x)^2), lambda>0, has exactly the same five sampled values, stays positive, and changes values elsewhere. Thus the samples cannot decide a global fourth power. No source definition or proof of a_RS was available in the two selected scientific sources; PROOF's summary repeats the conclusion and is not independent proof. The original a_RS lemma and its active min branches remain NOT-VERIFIED.

## Reproducible rational certificate (code, then results)

The code below is part of this one permitted deliverable and is executed from memory. It imports only Fraction and is independent of qf1_q.py. All decimal inputs are exact rationals representing the target's **rounded input model**, not certified exact physical constants. Intervals are rounded outward to dyadics after operations. For log(x), reduce x=2^k*y, 1<=y<2, set z=(y-1)/(y+1), and use 64 terms of 2*sum z^(2j+1)/(2j+1); the omitted tail is bounded by 2*z^129/(129*(1-z^2)). For exp, reduce a nonnegative argument to <=1/8, use 64 Taylor terms and a geometric bound on the tail, then square back; negative arguments use reciprocals. B(8) uses k=1,...,128 with remainder at most 8*log(2)*(130)/2^128. The q=infinity row uses t=0 analytically, not a large finite surrogate.

<!-- BEGIN RATIONAL CERTIFICATE -->
```python
from fractions import Fraction as F
SCALE = 1 << 320

def down(x):
    return F((x.numerator*SCALE)//x.denominator, SCALE)
def up(x):
    return -down(-x)
def box(lo, hi=None):
    if hi is None: hi=lo
    return (down(F(lo)), up(F(hi)))
def pt(x):
    return (F(x),F(x))
def add(a,b):
    return box(a[0]+b[0], a[1]+b[1])
def neg(a):
    return (-a[1],-a[0])
def sub(a,b):
    return add(a,neg(b))
def mul(a,b):
    v=[x*y for x in a for y in b]
    return box(min(v),max(v))
def inv(a):
    assert a[0]>0 or a[1]<0
    return box(1/a[1],1/a[0])
def div(a,b):
    return mul(a,inv(b))
def times(a,x):
    return mul(a,pt(x))

def log_unit(y):
    assert 1<=y<=2
    z=box((y-1)/(y+1)); zz=mul(z,z); term=z; total=pt(0)
    for j in range(64):
        total=add(total,times(term,F(2,2*j+1)))
        term=mul(term,zz)
    tail=div(times(term,2),times(sub(pt(1),zz),129))
    return box(total[0],total[1]+tail[1])
LN2=log_unit(F(2))
def log_point(x):
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    power=F(2)**k
    y=x/power
    if y<1: k-=1; y*=2
    if y>=2: k+=1; y/=2
    return add(times(LN2,k),log_unit(y))
def log_iv(a):
    return box(log_point(a[0])[0],log_point(a[1])[1])
LN10=log_point(F(10))
def lg(a):
    return div(log_iv(a),LN10)

def exp_point(x):
    if x<0: return inv(exp_point(-x))
    k=0
    while x>F(1,8): x/=2; k+=1
    y=pt(x); term=pt(1); total=pt(1)
    for n in range(1,65):
        term=div(mul(term,y),pt(n)); total=add(total,term)
    first=div(mul(term,y),pt(65))
    tail=div(first,sub(pt(1),times(y,F(1,66))))
    result=box(total[0],total[1]+tail[1])
    for _ in range(k): result=mul(result,result)
    return result
def exp_iv(a):
    return box(exp_point(a[0])[0],exp_point(a[1])[1])
def pow_iv(a,p):
    return exp_iv(times(log_iv(a),p))
def root(a):
    return pow_iv(a,F(1,2))

def fixed_integer(v,d):
    sign='-' if v<0 else ''; v=abs(v)
    return sign+str(v//10**d)+'.'+str(v%10**d).zfill(d)
def interval(a,d=12):
    lo=(a[0]*10**d).numerator//(a[0]*10**d).denominator
    b=a[1]*10**d; hi=-((-b.numerator)//b.denominator)
    return '['+fixed_integer(lo,d)+', '+fixed_integer(hi,d)+']'

def emit(label,a,scale=1,d=12):
    print(label+' '+interval(times(a,scale),d))

cs=F('411.9229708842423061'); cg=F('5699.632830341894211')
m=F(19615); h=F(3,4)-1/(4*m)
r6=root(pt(6)); K=F('3.31e7'); H=F('5.05e9')
e0=F('6.7e-40'); ars0=F('5.93136e-166'); dx=F('2.456e-152')
DIV=times(root(pt(H)),2)
logB=pt(0)
for k in range(1,129):
    logB=add(logB,times(log_point(F(2**k-1)),F(8,2**k)))
logB=box(logB[0],logB[1]+times(LN2,F(8*130,2**128))[1])
B8=exp_iv(logB)
base=lg(pt(ars0/(100*dx)))

def model(q, ns=3, pmax=True):
    t=F(0) if q is None else F(4)/q
    a=1/(1-t)
    ctheta=pt(1) if t==0 else times(pow_iv(pt(4*t),t/(1-t)),1-t)
    ac2=times(mul(mul(add(pt(7),times(r6,2)),
                        add(mul(ctheta,pow_iv(pt(27*cs),a)),pt(4096*cg))),pt(1)),1/(m*m*h))
    source=times(pow_iv(pt(36*cs*ns),a),F(1,2))
    cutoff=times(add(pt(cg),times(add(times(pow_iv(pt(64),-2+2*t),ns*cs),pt(1/(36*m))),18)),288)
    bracket=add(add(source,times(ac2,F(1,2))),cutoff)
    btel=B8 if pmax else exp_iv(times(logB,a/2))
    ct=times(mul(mul(r6,btel),bracket),F('175.8'))
    lam=times(mul(pow_iv(pt(2),t),add(pt('4.94'),times(pow_iv(pt(2),5*t/4),F('3.34')))),16)
    cd=add(times(mul(lam,ct),F('4.044')),pt('93.6'))
    tpr=inv(times(mul(cd,cd),K))
    cut=div(tpr,DIV)
    obj=add(base,times(lg(div(cut,pt(e0))),4))
    thetaeps=div(pt('1.12e-37'),times(pow_iv(pt(2),5*t/4),F('53.44')))
    min_t=box(min(tpr[0],thetaeps[0]),min(tpr[1],thetaeps[1]))
    min_cut=div(min_t,DIV)
    min_obj=add(base,times(lg(div(min_cut,pt(e0))),4))
    return dict(ct=ct,cd=cd,tpr=tpr,cut=cut,obj=obj,lam=lam,
                thetaeps=thetaeps,min_cut=min_cut,min_obj=min_obj,
                epsstar_need=times(mul(tpr,pow_iv(pt(2),5*t/4)),F('53.44')))

emit('B8',B8)
emit('DIV',DIV)
emit('bare baseline',base)
rows={q:model(q) for q in [8,11,12,32,100,1000,None]}
for q,r in rows.items():
    print('q = '+str(q if q is not None else 'infinity limit'))
    emit('  C_T / 1e12',r['ct'],F('1e-12'))
    emit('  C_D / 1e15',r['cd'],F('1e-15'))
    emit('  cutoff / 1e-43',r['cut'],F('1e43'))
    emit('  artificial objective',r['obj'])
    emit('  t_pr / theta_epsilon',div(r['tpr'],r['thetaeps']))
    emit('  cutoff including theta_epsilon / 1e-44',r['min_cut'],F('1e44'))
    emit('  objective including theta_epsilon',r['min_obj'])
    emit('  epsilon_star required / 1e-37',r['epsstar_need'],F('1e37'))

limit=rows[None]
gain=sub(limit['obj'],rows[8]['obj'])
emit('q8 to limit artificial gain',gain)
emit('q12 to limit artificial gain',sub(limit['obj'],rows[12]['obj']))
emit('q12 to q1000 artificial gain',sub(rows[1000]['obj'],rows[12]['obj']))
emit('q8 to limit cutoff gain',times(gain,F(1,4)))
emit('q8 to limit conditional quadratic live exponent gain',times(gain,F(1,2)))
emit('q1000 forced epsilon lowering',lg(div(pt(e0),rows[1000]['cut'])))
emit('theta_G = plateau t_pr crossing q / 1e25',div(pt('1.168e-12'),limit['tpr']),F('1e-25'))
emit('theta_G = limiting theta_epsilon crossing q / 1e26',div(pt('1.168e-12'),limit['thetaeps']),F('1e-26'))
for q in [12,100,None]:
    ratio=div(model(q,ns=486)['cd'],model(q)['cd'])
    emit('H2 cutoff decades q='+str(q),times(lg(ratio),2))

T=times(DIV,e0); cd_need=root(inv(times(T,K)))
emit('corrected required t_pr / 1e-35',T,F('1e35'))
emit('ratio to printed 3.01e-35',div(T,pt('3.01e-35')))
emit('sqrt10',root(pt(10)))
emit('corrected C_D ceiling / 1e13',cd_need,F('1e-13'))
emit('wrong first-script C_D ceiling / 1e30',root(inv(times(mul(T,T),K))),F('1e-30'))
for cn in [1,2]:
    ceiling=div(sub(cd_need,pt('93.6')),times(rows[12]['lam'],F('2.022')*cn))
    emit('corrected C_T ceiling q12 cN='+str(cn)+' / 1e10',ceiling,F('1e-10'))
for q in [8,12,None]:
    emit('Lambda q='+str(q),rows[q]['lam'])
    emit('C_D/C_T leading coefficient cN1 q='+str(q),times(rows[q]['lam'],F('2.022')))
    emit('C_D/C_T leading coefficient cN2 q='+str(q),times(rows[q]['lam'],F('4.044')))
exactH=640*53**4
print('unrounded H = '+str(exactH))
emit('required t_pr with H=640*53^4 / 1e-35',times(root(pt(exactH)),2*e0),F('1e35'))
for q in [12,32,100,1000,None]:
    cd=model(q,pmax=False)['cd']
    if cd[1]<cd_need[0]: verdict='clear under printed branch'
    elif cd[0]>cd_need[1]: verdict='fails under printed branch'
    else: verdict='undecided'
    print('P-ct q='+str(q)+': '+verdict)
```
<!-- END RATIONAL CERTIFICATE -->

### Certificate output

Executed with plain Python and Fraction only; every bracket is an outward rational enclosure. No qf1 script was run.

```text
B8 [1931.481139315139, 1931.481139315140]
DIV [142126.704035518954, 142126.704035518955]
bare baseline [-15.617074078418, -15.617074078417]
q = 8
  C_T / 1e12 [824.514248020343, 824.514248020344]
  C_D / 1e15 [761.338542922148, 761.338542922149]
  cutoff / 1e-43 [0.000003667251, 0.000003667252]
  artificial objective [-52.664010536004, -52.664010536003]
  t_pr / theta_epsilon [0.000038353813, 0.000038353814]
  cutoff including theta_epsilon / 1e-44 [0.000036672514, 0.000036672515]
  objective including theta_epsilon [-52.664010536004, -52.664010536003]
  epsilon_star required / 1e-37 [0.000042956270, 0.000042956271]
q = 11
  C_T / 1e12 [9.773761729366, 9.773761729367]
  C_D / 1e15 [7.743853612951, 7.743853612952]
  cutoff / 1e-43 [0.035447209517, 0.035447209518]
  artificial objective [-36.723045080256, -36.723045080255]
  t_pr / theta_epsilon [0.329410910899, 0.329410910900]
  cutoff including theta_epsilon / 1e-44 [0.354472095171, 0.354472095172]
  objective including theta_epsilon [-36.723045080256, -36.723045080255]
  epsilon_star required / 1e-37 [0.368940220207, 0.368940220208]
q = 12
  C_T / 1e12 [5.288348017628, 5.288348017629]
  C_D / 1e15 [4.051788820556, 4.051788820557]
  cutoff / 1e-43 [0.129480008084, 0.129480008085]
  artificial objective [-34.472562417834, -34.472562417833]
  t_pr / theta_epsilon [1.172076596483, 1.172076596484]
  cutoff including theta_epsilon / 1e-44 [1.104706027514, 1.104706027515]
  objective including theta_epsilon [-34.748386394744, -34.748386394743]
  epsilon_star required / 1e-37 [1.312725788061, 1.312725788062]
q = 32
  C_T / 1e12 [1.454322965517, 1.454322965518]
  C_D / 1e15 [0.888876682653, 0.888876682654]
  cutoff / 1e-43 [2.690377944154, 2.690377944155]
  artificial objective [-29.202120113404, -29.202120113403]
  t_pr / theta_epsilon [20.331683584530, 20.331683584531]
  cutoff including theta_epsilon / 1e-44 [1.323244055500, 1.323244055501]
  objective including theta_epsilon [-34.434813482594, -34.434813482593]
  epsilon_star required / 1e-37 [22.771485614674, 22.771485614675]
q = 100
  C_T / 1e12 [1.396001193197, 1.396001193198]
  C_D / 1e15 [0.779871164173, 0.779871164174]
  cutoff / 1e-43 [3.495027493062, 3.495027493063]
  artificial objective [-28.747570903614, -28.747570903613]
  t_pr / theta_epsilon [24.537268075409, 24.537268075410]
  cutoff including theta_epsilon / 1e-44 [1.424375151431, 1.424375151432]
  objective including theta_epsilon [-34.306875734437, -34.306875734436]
  epsilon_star required / 1e-37 [27.481740244458, 27.481740244459]
q = 1000
  C_T / 1e12 [1.385947020925, 1.385947020926]
  C_D / 1e15 [0.745624197094, 0.745624197095]
  cutoff / 1e-43 [3.823458095824, 3.823458095825]
  artificial objective [-28.591547950067, -28.591547950066]
  t_pr / theta_epsilon [26.018700158005, 26.018700158006]
  cutoff including theta_epsilon / 1e-44 [1.469503884746, 1.469503884747]
  objective including theta_epsilon [-34.252690335217, -34.252690335216]
  epsilon_star required / 1e-37 [29.140944176966, 29.140944176967]
q = infinity limit
  C_T / 1e12 [1.385090430854, 1.385090430855]
  C_D / 1e15 [0.742060979450, 0.742060979451]
  cutoff / 1e-43 [3.860265105059, 3.860265105060]
  artificial objective [-28.574904765134, -28.574904765133]
  t_pr / theta_epsilon [26.178288076074, 26.178288076075]
  cutoff including theta_epsilon / 1e-44 [1.474605632668, 1.474605632669]
  objective including theta_epsilon [-34.246669735304, -34.246669735303]
  epsilon_star required / 1e-37 [29.319682645203, 29.319682645204]
q8 to limit artificial gain [24.089105770869, 24.089105770870]
q12 to limit artificial gain [5.897657652699, 5.897657652700]
q12 to q1000 artificial gain [5.881014467767, 5.881014467768]
q8 to limit cutoff gain [6.022276442717, 6.022276442718]
q8 to limit conditional quadratic live exponent gain [12.044552885434, 12.044552885435]
q1000 forced epsilon lowering [3.243618467912, 3.243618467913]
theta_G = plateau t_pr crossing q / 1e25 [2.128874338624, 2.128874338625]
theta_G = limiting theta_epsilon crossing q / 1e26 [5.573028571428, 5.573028571429]
H2 cutoff decades q=12 [6.365045455826, 6.365045455827]
H2 cutoff decades q=100 [1.454093279563, 1.454093279564]
H2 cutoff decades q=None [1.037481305977, 1.037481305978]
corrected required t_pr / 1e-35 [9.522489170379, 9.522489170380]
ratio to printed 3.01e-35 [3.163617664577, 3.163617664578]
sqrt10 [3.162277660168, 3.162277660169]
corrected C_D ceiling / 1e13 [1.781192096445, 1.781192096446]
wrong first-script C_D ceiling / 1e30 [1.825305303611, 1.825305303612]
corrected C_T ceiling q12 cN=1 / 1e10 [4.649582744498, 4.649582744499]
corrected C_T ceiling q12 cN=2 / 1e10 [2.324791372249, 2.324791372250]
Lambda q=8 [228.332906437232, 228.332906437233]
C_D/C_T leading coefficient cN1 q=8 [461.689136816083, 461.689136816084]
C_D/C_T leading coefficient cN2 q=8 [923.378273632166, 923.378273632167]
Lambda q=12 [189.459168646007, 189.459168646008]
C_D/C_T leading coefficient cN1 q=12 [383.086439002227, 383.086439002228]
C_D/C_T leading coefficient cN2 q=12 [766.172878004455, 766.172878004456]
Lambda q=None [132.479999999999, 132.480000000001]
C_D/C_T leading coefficient cN1 q=None [267.874559999999, 267.874560000001]
C_D/C_T leading coefficient cN2 q=None [535.749119999999, 535.749120000001]
unrounded H = 5049907840
required t_pr with H=640*53^4 / 1e-35 [9.522402279626, 9.522402279627]
P-ct q=12: fails under printed branch
P-ct q=32: fails under printed branch
P-ct q=100: fails under printed branch
P-ct q=1000: clear under printed branch
P-ct q=None: clear under printed branch
```

### F07 — CONFIRMED: requested printed objective rows, but only for the conditional surrogate

Attachment: QFIX.md:274-292; checks/qf1_q.py:233-264.

The independent rational certificate encloses every requested row. These are values of the **printed model**, with its supplied rounded constants, assumed fourth power, and its omitted minima still omitted:

| q | Rigorous enclosure of the surrogate objective | QFIX to 3 decimals | Verdict on rounding |
|---|---|---|---|
| 8 | [-52.664010536004, -52.664010536003] | -52.664 | CONFIRMED |
| 11 | [-36.723045080256, -36.723045080255] | -36.723 | CONFIRMED |
| 12 | [-34.472562417834, -34.472562417833] | -34.473 | CONFIRMED |
| 32 | [-29.202120113404, -29.202120113403] | -29.202 | CONFIRMED |
| 100 | [-28.747570903614, -28.747570903613] | -28.748 | CONFIRMED |
| 1000 | [-28.591547950067, -28.591547950066] | -28.592 | CONFIRMED |
| analytic limit | [-28.574904765134, -28.574904765133] | -28.575 | CONFIRMED as a limit; endpoint-optimum argument REFUTED |

The q=8-to-limit difference is [24.089105770869,24.089105770870] decades. At the actually recommended q=1000 it is [24.072462585937,24.072462585938]. The q=12-to-limit difference is [5.897657652699,5.897657652700]. These calculations do not certify the live proof objective or the fourth-power premise (F04, F06, F10).

The active-floor witness in F04 is quantitatively material:

| q | Plotted cutoff | Cutoff upper bound after restoring theta_epsilon at epsilon_*=1.12e-37 | Corresponding objective upper bound |
|---|---|---|---|
| 12 | 1.29480008084e-44 | 1.104706027515e-44 | -34.748386394743 |
| 1000 | 3.82345809582e-43 | 1.469503884747e-44 | -34.252690335216 |
| formal limit ignoring theta_G only | 3.86026510506e-43 | 1.474605632669e-44 | -34.246669735303 |

These upper bounds use only two entries of the full min; other entries can reduce them further. Restoring theta_G makes the actual infinite-q limit minus infinity. Alternatively, to preserve the plotted C_D branch one must demonstrate an admissible epsilon_* at least **1.312725788062e-37 at q=12**, **2.914094417697e-36 at q=1000**, and approximately **2.931968264520e-36 at the plateau**, rather than recycling 1.12e-37 as the no-change floor. No admissibility of those enlarged epsilon_* values is claimed here.

The theta_G versus theta_epsilon crossover 5.573e26 is correctly rounded for the *fixed old epsilon_* floor*. It is not the crossover against the plotted t_pr: theta_G equals the limiting C_D-branch t_pr already near **2.128874338624e25**. These are different comparisons with different thresholds, not interchangeable headroom figures.

### F08 — REFUTED literally, CONFIRMED in substance: the two inherited corrections are rounded corrections, not exact identities

Attachment: QFIX.md:392-410,416-428,485-491; EPSSTAR.md:521,523-525; SQ.md:1513,1624,1634; checks/qf1_criteria.md:40.

**Square-root correction.** Solving the displayed equations gives

    T = 2*(6.7e-40)*sqrt(5.05e9)
      in [9.522489170379,9.522489170380]*1e-35,
    T/(3.01e-35) in [3.163617664577,3.163617664578],
    sqrt(10) in [3.162277660168,3.162277660169].

These intervals are disjoint. The claim of an **exactly sqrt(10)** discrepancy is REFUTED; the claim that a factor ten was apparently lost inside a square root before rounding is consistent with the numbers, ARGUED rather than a reconstruction of the author's actions. The target itself gives the more accurate ratio in its body. Its corrected downstream ceilings are confirmed in the rounded-input model:

    C_D <= [1.781192096445,1.781192096446]*1e13,
    C_T(q=12,c_N=2) <= [2.324791372249,2.324791372250]*1e10,
    C_T(q=12,c_N=1) <= [4.649582744498,4.649582744499]*1e10.

Thus the original script's 1.825305303612e30 ceiling is replaced by approximately 1.781192096445e13, as the target disclosed. At the stated more primitive constants c_flat=1/640 and C'=53, H is **640*53^4=5,049,907,840**, not exactly 5,050,000,000. This gives T in [9.522402279626,9.522402279627]*1e-35. The rounded equation is adequate at three significant figures, but cannot be called exact to arbitrary precision.

**Prefactor correction.** Substitute C_T'=4*2^(2+4/q)*C_T and A_0=c_N*C_T'*(4.94+3.34*32^(1/q)) into G=2*(1.011*A_0+B_0). On G>C_r, this gives exactly

    C_D/C_T = 2.022*Lambda(q)*c_N + 2*B_0/C_T.

With the target's B_0=46.8 the final term is 93.6/C_T. Dropping this negligible but nonzero additive term gives the following leading coefficients, not literally the [500,900] band:

| q | c_N=1 leading coefficient | c_N=2 leading coefficient |
|---|---|---|
| 8 | [461.689136816083,461.689136816084] | [923.378273632166,923.378273632167] |
| 12 | [383.086439002227,383.086439002228] | [766.172878004455,766.172878004456] |
| infinity | **267.87456 exactly** | **535.74912 exactly** |

The target's q=12 entries **383.08 and 766.16** should round to **383.09 and 766.17**; its plateau **535.73** should be **535.75**. At fixed N=2,kappa_+=1,C_0=3.34, the variable c_N parametrizes the leading band; this is confirmed algebraically. That the inherited historical band had no other source of uncertainty is NOT-VERIFIED: its original REVIEW_SQ_S4 source was outside the two selected scientific extras. Moreover the rounded band [500,900] is not an interval containing the displayed exact leading range. The useful q-dependent prefactor correction survives; its “exactly” wording does not.

### F09 — REFUTED: the gates do not decide several claims for which they report success

Attachment: QFIX.md:67-80,444-465; checks/qf1_criteria.md:56-73; checks/qf1_q.py as specified below.

| Gate | What the code actually decides | Hostile finding and verdict |
|---|---|---|
| QF1-1 | Lines 129-140 gate only the seven m=19615 relative errors, plus B(4),B(8); m=7 errors are printed but excluded from `worst` | It can reject a large error in its selected inputs, CONFIRMED. It does not enforce the original complete reproduction claim. The original QFIX:74 also required CONST_T's B(4a) column to two significant figures. CONST_T:301 has **85 at q=24**, whereas the independently enclosed B(4a) is approximately **93.656**, so that original clause fails. The later criteria silently substitute checking B(4),B(8). REFUTED as fulfillment of the original test. |
| QF1-2 | Lines 145-156 compare 17 grid points and positivity of the last value | Neither strict monotonicity on a real interval nor a finite limit follows. F03 supplies a counterexample within its own formula. REFUTED as a global certificate. |
| QF1-3 | Lines 165-181 test a finite set of already algebraic identities and inequalities | The scale identity is PROVEN by cancelling (-2+8/q)=-2*(q-4)/q, not by sampling. The original inclusion of theta<=1/2 made the initial gate impossible (F01). The revised clause establishes no upper-range completeness. |
| QF1-3b | Lines 173-180 test the intended floor at sample integers | Its advertised floor is independently PROVEN by 4/q<=1/2 iff q>=8; no sampling is needed. CONFIRMED for that clause only. |
| QF1-4 | Lines 187-199 test two Lambda ratios | It is a discriminating check of this formula's q dependence. CONFIRMED for the supplied constants; it does not certify the historical band's provenance or a complete C_D bound. |
| QF1-5 | Lines 259-264 check a finite-grid increase bounded by 20 from q=12 | This is not a min over all consumers, nor a boundedness test over an unbounded domain. An arbitrary increase beyond 10^6 can be invisible. F04 exhibits the actual omitted constraint. REFUTED as the global optimum test. |
| QF1-6 | Lines 233-241,269-277 remove *all* q inputs before checking zero spread | In the frozen branch q is unused, so every entry is the same function call on identical arguments. The zero-spread half is tautological; wrong powers and missing consumers survive it. The live-spread half can fail for a flat supplied model, but does not validate the mechanism or detect the missing min. REFUTED as an adversarial validation of the science claim. |
| QF1-7 | Line 326 delegates comparison of formatted output files | The displayed rounded numbers agree; the actual differences are header line 2 and zero-exponent line 114. Finite-precision agreement is not exact arithmetic, an infinite-product remainder bound, or verification of unprinted digits. REFUTED as “exactness”; CONFIRMED as displayed-number stability. |
| QF1-8 | Lines 305-313 compare independently supplied conflicting t_pr numbers | This comparison can and does reject the inherited number. CONFIRMED as a discriminating check. Its secondary C_D output used F02's disclosed error. |
| QF1-9 | Lines 205-212 retain the first passing integer, and test only whether one exists | It prints “unique” without counting passing integers. Our independent Fraction check confirms uniqueness for these particular rows, but the implemented gate cannot enforce uniqueness in general and no such gate proves an analytic power law (F06). REFUTED as the claimed theorem check. |

The first-script P-ct clearance booleans are independently corrected to **false at q=12,32,100; true at q=1000 and at the formal limit**, under the printed C_D branch. This does not check compatibility with the other minimum entries. qf1b_* and qf1c_* were not read or executed because they do not match the permitted qf1_* glob; no certification of their contents is implied.

### F10 — NOT-VERIFIED: a_RS consumption and the asserted live programme margin

Attachment: QFIX.md:44-47,123,254-266,496-510,598-606; PROOF.md:73 at final check (71 at initial check), unique string “a_RS binds NOTHING on the live RLF-step v3 route”.

The supplied sibling conclusion is repeated in the current PROOF summary: it identifies the live exponent as **a=theta*a_bad**, says a_RS is confined to frozen v1 material, and says the a_RS input itself is excluded from RLF-step v3 hypotheses. I have **not** independently proved those absence statements or the live theorem: the controlling RLARGE body is not among the two extra scientific sources selected, and a summary's assertion is not evidence sufficient for CONFIRMED. This remains the most dangerous unverified issue.

Nevertheless, QFIX has not established that its objective is consumed by the live route. Its 24.089 is exactly the log-ratio improvement of a **hypothetical fourth-power a_RS/100 ceiling**, after choosing epsilon_1 to equal a DESC-epsilon cutoff on one selected branch. It is not automatically a margin for the constructive programme. If the sibling is right, the currency is wrong even if every table cell reproduces.

The conditional restatement can be derived without inventing a new live proof. EPSSTAR:527 explicitly gives a_bad=c_pr*epsilon_1^2. If the reported live exponent is a=theta*c_pr*epsilon_1^2 and theta,c_pr and the divisor remain fixed, then, along the same cutoff curve,

    Delta log10(a) = 2*Delta log10(epsilon_1_cut)
                  = -4*Delta log10(C_D),

rather than the fourth-power ceiling's -8*Delta log10(C_D). The q=8-to-limit gain is then **[12.044552885434,12.044552885435] decades**, and q=12-to-limit **[2.948828826349,2.948828826350] decades**, both CONDITIONAL and still subject to F04. A safe currency independent of a_RS consumption is the modeled cutoff gain itself: **6.022276442718 decades from q=8**, **1.474414413175 from q=12**. No live deficit is repaired merely by these changes. If epsilon_1 remains fixed and the other live factors remain fixed, raising q changes admissibility/headroom, not the value theta*c_pr*epsilon_1^2 once that branch is active.

The PROOF summary's positive absolute live-margin figure is **not** promoted to a verified result here. Only the algebraic ratio above is reconstructed. Claim grade: CONDITIONAL for the restatement; GAP for using a_RS as the programme objective.

### F11 — REFUTED: mixed baselines and stale numbers survive the target's own corrections

Attachment: QFIX.md:206-216,225-227,501-509.

1. The displayed H2 model gives a cutoff gain **6.365045455826... decades at q=12** and **1.037481305977... at the limit** (full C_D ratio, including B_0). The latter rounds to **1.037**, not the printed **1.038**, at three decimals. This is a small rounding defect, not a rejection of the large qualitative reduction. The analytic H2 source lemmas themselves remain NOT-VERIFIED.
2. QFIX:501 still calls the H2 plateau effect “approximately 0.9 decades” after :225-227 explicitly superseded it by **0.519 decades of C_T**. This is a stale status sentence.
3. QFIX:508 says q “recovers 24.089 of the 19.415 decades that lowering epsilon_1 would cost.” Those numbers have different baselines. The **24.089105770870** recovery starts at the q=8 cutoff, whose modeled fourth-power lowering penalty is **37.046936457586** decades. The **19.414571149580** penalty starts instead at the inherited q=12 cutoff **9.38495112638e-45**. From that inherited cutoff to the formal plateau the recovery is only **6.456740462863** decades; the remaining penalty is **12.957830686717**. From q=12 with Lambda already restored the recovery is **5.897657652700**. The phrase “24.089 of 19.415” is numerically invalid bookkeeping.

### F12 — REFUTED as a real-valued minimum: “the lowest admissible q is 12”

Attachment: QFIX.md:194-198,542-543; SQ.md:1459,1608.

No inspected statement requires q to be integral. With the target's same constants and c_N=2, the rational choice **q=23/2=11.5** gives C_D in **[5.421734663162,5.421734663163]*1e15**, below 6.7e15. Thus 12 is the **smallest passing integer in the tested list**, not the lowest real admissible exponent. Likewise the q=1000 recommendation is explicitly the first passing point on a sparse grid (200 jumps to 1000), not a continuous optimization result. The exact real threshold and an independently justified practical q are not claimed here.

## Symbol and citation control

- **q_Moser:** SQ:1459-1464, a real exponent >4. **rho_decay:** SQ:1096-1099,1524, the other printed q, bounded by (L^-2+L^-3)/2. At L=3 its endpoint is 2/27, giving rho_decay*L^2=2/3; it must never be inserted into 4/q_Moser. The target recognizes this collision correctly.
- **theta_SUP:** SQ:188, 1/(2*C_err). **theta_SQ4:** SQ:1622, min(theta_G,theta_epsilon). These are distinct. SQ:1633 places theta_SQ4/C' inside tau_R, while SQ:318-319 places tau_R inside tau_flat. This directly verifies the missing nested minimum in F04 without trusting a status label.
- **C_1 at SQ:190:** the SUP-price constant, 160 at the stated reference point. **C_1 at SQ:1587:** the CARL coefficient (9/8)*5^4*49*sqrt(6)*L^4. **C_1 at SQ:1487:** an energy-inequality coefficient, not automatically either of those. The target's c_s,c_g combination is evaluated as its own supplied model, not by silently substituting one of these C_1 values.
- **C_3 in the size clause:** EPSSTAR:523, multiplying epsilon_1^2. This is not the CARL coefficient called C_3 at SQ:1586-1587. Setting it to one is an explicit model input in the target, not a derivation of that bound.
- **epsilon_* in this review:** EPS-T's threshold from SQ:1460-1462. **epsilon_1:** the supplied RLARGE headline value in checks/qf1_criteria.md:43. Their roles are not exchanged.
- **c_N:** SQ:1389 supplies an N-dependent norm comparison, and SQ:1624 shows its multiplicative occurrence in A_0. The numerical interval [1,2] is an inherited input here; its proof was not inspected.
- **A verified citation error:** QFIX:396 and checks/qf1_criteria.md:41 cite **EPSSTAR:527** for eta_flat>=4*C_3*epsilon_1^2. That requirement is currently at **EPSSTAR:523-524**; :527 starts “What it does and does not break” and describes a_bad. The formula at :521 and the bad number at :525 remain at the cited positions. This is a real attachment error, irrespective of whether caused by drift or initial miscitation.
- QFIX cites PROOF only as an earlier source in its registration, without a numbered PROOF claim to verify. No PROOF line-number citation was invented or silently trusted in this review; :73 above is attached to its unique current string and used only as a conflicting route report.

## Summary table

| Item | Review verdict | Claim grade / consequence |
|---|---|---|
| Fourteen exhaustive consumers; thirteen favor larger q | REFUTED | GAP: one listed consumer reverses at q=432*c_s; input source smallness and threshold minima are not fully counted |
| Floor 4/q<=1/2 iff q>=8 | CONFIRMED | PROVEN elementary equivalence |
| No upper constraint; optimum only at q=infinity | REFUTED | GAP: q*beta<=1/2, nested thresholds and an adverse asymptotic term defeat the universal claim |
| a_RS proportional to epsilon_1^4 as an actual lemma | NOT-VERIFIED | GAP: five samples do not derive the lemma or its active branches |
| Five-row fourth-power fit to 0.0002 percent | CONFIRMED | PROVEN exact-rational fit of the printed data only |
| epsilon_1_cut proportional to C_D^-2 | CONFIRMED on one branch | CONDITIONAL on all other minima remaining inactive |
| Requested objective rows and 24.089 difference | CONFIRMED as model arithmetic | CONDITIONAL surrogate; not verified programme margin |
| -28.575 as a finite model limit | CONFIRMED | CONDITIONAL rounded value; equating the limiting value with a supremum is REFUTED |
| Inherited EPSSTAR square-root error | CONFIRMED in substance | PROVEN algebra; exact sqrt(10) wording REFUTED |
| Inherited C_D prefactor correction | CONFIRMED in its q dependence | CONDITIONAL input model; exact band equality REFUTED |
| Gate suite proves global claims | REFUTED | GAP: finite grids, an impossible original gate, a tautological frozen control, missing uniqueness enforcement |
| a_RS is consumed by live RLF-step v3 | NOT-VERIFIED | Most dangerous unresolved question; current route summary says it is not |
| 24.089 transferred to a fixed-coefficient quadratic live exponent | REFUTED | CONDITIONAL replacement is 12.044553, with the missing-min caveat |
| q=12 is the least real admissible q | REFUTED | q=11.5 is an explicit passing witness; 12 is a tested-integer statement |
| QFIX's mixed-baseline and stale H2 statements | REFUTED | Corrected figures and baselines in F11 |

Review conclusion: the arithmetic of the selected finite-q surrogate is reproducible, but **QFIX does not establish its headline as a live programme margin or a global optimum**. The useful result that survives is a conditional improvement of the C_D-derived cutoff over a practical finite q range, after rechecking every actual minimum and naming the live exponent. No scientific source was edited; no git command, audit operation, external numerical library, or scientific file beyond the declared read scope was used.

Precision qualification: refuting the equality of an exact limiting value and a supremum does **not** show that their three-decimal roundings differ. The finite-q optimum of a repaired model might still round to -28.575. What is proved false here is the global endpoint argument and the compatible infinite-q limit. The full repaired objective and its numerical maximum remain NOT-VERIFIED.

### Final source receipt

Observed drift during this review: the exact PROOF string “a_RS binds NOTHING on the live RLF-step v3 route” moved from line 71 to line 73. The final attachment was refreshed by string search; no inference was made from the old number.

This is a local-file review under the owner's no-git rule, not a verification of origin/main or of a retained scientific status. Source attachments are by current line plus identifying string; the large PROOF file was searched and excerpted only. Final receipt UTC: 2026-10-28T22:21:58.460640+00:00

- QFIX.md: 608 lines; SHA-256 `51c4eff88ccd12735855589884924336304b66c5a759070c4a9a96d8e75dd53d`.
- checks/qf1_q.py: 329 lines; SHA-256 `0a34760c2675ffb88de55f8325996abfb547604f75b3f80aaf06e29d40d7af14`.
- checks/qf1_criteria.md: 106 lines; SHA-256 `08f8e14e3f9e074feff331d91c21837e3c0d8c99a51e1ef2f33a47623316b36f`.
- checks/qf1_out.txt: 168 lines; SHA-256 `6cfed9cfb81c901f59f8dca25c44cae954f928b165bc1eba79e21428942fe44d`.
- checks/qf1_out_prec60.txt: 168 lines; SHA-256 `a0ca1eb15da74beaa075b22f849cf2b9287b08d2be49fad6a47365417479d5fe`.

## Short stdout summary

Verdicts: REFUTED — exhaustive 13-up/1-down census, no upper consumer constraint, endpoint optimum, original gate claims, and mixed-baseline accounting. CONFIRMED — the seven rounded surrogate objective rows and the 24.089105770870-decade modeled difference. NOT-VERIFIED — the analytic a_RS fourth-power lemma and its live consumption.

Numerical corrections (all scoped above):
- “13 improve, 1 opposes” -> at least a second adverse dependence: A_c*gamma_c reverses at q=177950.7234219926762352; one listed row is indifferent under P-max and two are floors.
- “least q=12” -> q=11.5 already passes, C_D=5.421734663163e15; 12 is a tested-integer statement.
- Infinite-q objective -28.575 -> compatible limit minus infinity when theta_G is restored; no corrected global maximum is asserted.
- At the quoted epsilon_*=1.12e-37 floor, q=1000 cutoff 3.823458095825e-43 -> at most 1.469503884747e-44, and objective -28.591547950066 -> at most -34.252690335216. Preserving the plotted branch instead needs epsilon_* about 2.914094417697e-36. At q=12, cutoff 1.29480008085e-44 -> at most 1.104706027515e-44 and objective -34.472562417833 -> at most -34.748386394743.
- Exactly sqrt(10) -> ratio 3.163617664578; the corrected t_pr is 9.522489170380e-35, versus the inherited 3.01e-35. With unrounded primitive denominator 5,049,907,840 instead of 5.05e9, it is 9.522402279627e-35.
- Erroneous first-script C_D ceiling 1.825305303612e30 (or inherited EPSSTAR 3.17e13) -> 1.781192096446e13. Corresponding q=12 C_T ceilings are 2.324791372250e10 to 4.649582744499e10.
- Exact [500,900] prefactor band -> leading [461.689136816084,923.378273632167], plus 93.6/C_T; q=12 entries 383.08/766.16 -> 383.09/766.17; plateau 535.73 -> 535.75.
- CONST_T's B(4a)=85 at q=24 -> 93.655714835335; the registered reproduction test never checks it.
- H2 plateau 1.038 -> 1.037481305978 decades (1.037 to three decimals); stale 0.9 -> 0.518740652989 decades of C_T (0.519).
- “24.089 recovered out of 19.415” -> 6.456740462864 recovered from that inherited cutoff baseline; 24.089 belongs to the q=8 baseline instead.
- If the live exponent is the reported fixed-coefficient quadratic theta*c_pr*epsilon_1^2: 24.089105770870 -> 12.044552885435 decades, still conditional on the omitted minima.

Most dangerous NOT-VERIFIED issue: whether the live route consumes a_RS at all. The current PROOF summary says it does not; this review does not promote that secondary report to proof.

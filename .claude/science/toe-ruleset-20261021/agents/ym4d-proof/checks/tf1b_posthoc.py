#!/usr/bin/env python3
# tf1b -- POST-HOC probe, run AFTER tf1_out.txt was read.  NOT pre-registered.
# Purpose: price the OTHER lever on eta_flat, namely C_err's PREFACTOR, since tf1 showed the C_T lever
# is floored.  Every constant transcribed; nothing re-derived.  Criteria: tf1b_criteria.md (one line).
from fractions import Fraction as F
from decimal import Decimal, getcontext
def E(m,e): return F(m)*F(10)**e
def d10(x,p=40):
    getcontext().prec=p+15
    return Decimal(x.numerator).log10()-Decimal(x.denominator).log10()
def sci(x,p=6):
    getcontext().prec=p
    return str(+Decimal(x.numerator)/Decimal(x.denominator))
L=[]
def p(s=""):
    L.append(s); print(s)
p("[POST-HOC, TF1-P2]  the C_err prefactor lever.  Run after tf1_out.txt was read.  NOT pre-registered.")
p("="*100)
# TRANSCRIBED:
# C_err := C_p(K^2 + K_top^2) + 4C_e[K^2/(L(L-1)) + 1.011 K C_D L/(L^2-1)]   SQ.md Thm SUP-price l.188
# C_p := 34 sqrt(N)  [SQ.md RSQ1-fix M-1 l.181];  C_e ~ 3.8e3, K ~ 78 C_D  [SQ.md Remark (a) l.206]
# K = 78.3 C_D, K_top = 81.3 C_D  [REVIEW_SQ_S4 S4-16 l.363];  L = 3, N = 2
Cp_bch=F(34)*F(14142135623730951,10**16)    # 34*sqrt(2), 17 digits
Ce=E(38,2); kK=F(783,10); kKt=F(813,10); Lf=F(3); Nf=F(2); one011=F(1011,1000)
p("  transcribed: C_p=34*sqrt(2)=%s  C_e=3.8e3  K/C_D=78.3  K_top/C_D=81.3  L=3  N=2" % sci(Cp_bch))
# C_err / C_D^2 :
term_bch = Cp_bch*(kK**2+kKt**2)
term_e   = 4*Ce*(kK**2/(Lf*(Lf-1)) + one011*kK*Lf/(Lf**2-1))
tot = term_bch+term_e
p("  C_p(K^2+K_top^2)/C_D^2            = %s   (%s%% of total)" % (sci(term_bch), sci(100*term_bch/tot,4)))
p("  4C_e[...]/C_D^2                   = %s   (%s%% of total)" % (sci(term_e),   sci(100*term_e/tot,4)))
p("  C_err/C_D^2 (reconstructed)       = %s" % sci(tot))
p("  REVIEW_SQ_S4 S4-16 l.364 states   = 1.655e7      ratio = %s" % sci(tot/E(1655,4),6))
p("")
# required drop: eta_flat ~ 1/C_err^2, shortfall 9.707 decades of energy (tf1_out.txt)
need_energy = E(5099,6)   # 10^9.707 = 5.0953e9 ; use exact 4C_3eps1^2 / eta_flat from tf1
# recompute exactly rather than transcribe the rounded decade:
Cprime=F(53); cb=F(1,640); th=2*E(1655,4); CT=E(5288,9); CD=E(9,2)*CT
t_pr=1/(th*CD*CD); eta=cb*(t_pr/Cprime)**2/Cprime**2; req=4*E(67,-41)**2
X2=req/eta
import math
isq=math.isqrt(X2.numerator*10**40//X2.denominator); X=F(isq,10**20)
p("  shortfall in eta_flat        = %s  (%s decades of energy)" % (sci(X2), str(+d10(X2).quantize(Decimal('0.001')))))
p("  eta_flat ~ 1/C_err^2, so C_err must fall by a factor X = sqrt(shortfall) = %s (%s decades)"
  % (sci(X), str(+d10(X).quantize(Decimal('0.001')))))
p("  target: C_err/C_D^2 must fall from %s to %s" % (sci(tot), sci(tot/X)))
p("")
p("  HOW MUCH of that is reachable, term by term (each an IDEALISED limit, not a proposal):")
p("   (a) C_e -> 0 entirely (the whole 4C_e bracket deleted):")
p("       C_err/C_D^2 -> %s, i.e. only %s decades of the %s needed"
  % (sci(term_bch), str(+d10(tot/term_bch).quantize(Decimal('0.001'))), str(+d10(X).quantize(Decimal('0.001')))))
p("   (b) with C_e -> 0, the residue is C_p(K^2+K_top^2). Solving C_p(k^2+k_top^2) = target for k,")
p("       holding k_top/k = 81.3/78.3:")
r=kKt/kK
k2=(tot/X)/(Cp_bch*(1+r*r))
isq2=math.isqrt(k2.numerator*10**40//k2.denominator); kneed=F(isq2,10**20)
p("       K/C_D must fall from 78.3 to %s, a factor %s" % (sci(kneed,4), sci(kK/kneed,4)))
p("   (c) SQ.md Remark (a) l.206/l.224 says C_e and K are 'crude by orders of magnitude' and that")
p("       'optimisation could gain several orders: unclaimed'; h6 measured the MSG constant at 3.5")
p("       against the proven 66, a factor %s." % sci(F(66)/F(35,10),3))
p("       So the required package is: delete the C_e bracket AND improve K's coefficient by ~%s."
  % sci(kK/kneed,3))
p("")
p("  The C_T lever, for comparison (tf1_out.txt): C_T = 5.288e12 against its own floor 4.4e12,")
p("  i.e. %s decades of room, against the %s decades the clause needs in C_err-equivalent terms."
  % (str(+d10(CT/E(44,11)).quantize(Decimal('0.001'))), str(+d10(X).quantize(Decimal('0.001')))))
p("  Since C_err ~ C_D^2 ~ C_T^2, those %s decades of C_T buy %s decades of C_err."
  % (str(+d10(CT/E(44,11)).quantize(Decimal('0.001'))), str(+(2*d10(CT/E(44,11))).quantize(Decimal('0.001')))))
p("="*100)
open("tf1b_out.txt","w").write("\n".join(L)+"\n")

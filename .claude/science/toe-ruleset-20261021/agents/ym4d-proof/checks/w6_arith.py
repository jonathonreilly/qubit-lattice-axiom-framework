"""w6 Part A: the ceilings, in plain-Python Decimal at 120 digits (no mpmath, no numpy, no BLAS -> no lock).
Criteria: checks/w6_criteria.md (written before this script).  Informational, never a proof.

Formulas are HW's own.  b_n, b_D, c_f are written as (geometric multiplicative factor) x (column 81) x (per-level shadow
constants) x (allowance), so that session 5's and session 6's constants are the SAME expression at different factor values:
    b_n = Csh * 81 * h_n * cplus + h_n' * cU ,   b_D = h_D * (Csh * 81 * cplus + cU) ,   c_f = Csh * 81 * cplus
with (Csh, h_n, h_n', h_D) = (6561, 38418, 38417, 38416) in session 5 and (81, 10002, 10001, 10000) in session 6,
and cplus = c_A + ring * cU (ring = 1 no ring, 82 = PLD §18.4's price, 17 = session 6's cheaper ring)."""
from decimal import Decimal as D, getcontext
import time

getcontext().prec = 120
t0 = time.time()
res = {}

a = D('1.0e-86')
beta = D('0.186')
L = D(3)
logL = L.ln()
a_ret = D('2.0e-91')
RHO = 8
c_att5 = 1 + 153664 * RHO          # session 5 (HW l.1501)
c_att6 = 1 + 40000 * RHO           # session 6
Delta2 = D((2 * RHO + 1) ** 4 - 1) ** 2
CEIL_RLF = D('1e-94')              # recorded (RLF-delta) ceiling
CEIL_nH = D('2.7e-91')
CEIL_DX = D('2.5e-152')            # DX' at C_Omega = 1 (REVIEW_SF_S7 l.335)

S5 = dict(name='session5', Csh=6561, hn=38418, hn1=38417, hD=38416, catt=c_att5)
S6 = dict(name='session6', Csh=81, hn=10002, hn1=10001, hD=10000, catt=c_att6)


def consts(S, cA, cU, ring):
    cp = D(cA) + D(ring) * D(cU)
    K = D(S['Csh'] * 81)
    b_n = K * D(S['hn']) * cp + D(S['hn1']) * D(cU)
    b_D = D(S['hD']) * (K * cp + D(cU))
    c_f = K * cp
    return cp, b_n, b_D, c_f


def g2_CRC(S, cA, cU, ring, Cl):
    cp, b_n, b_D, c_f = consts(S, cA, cU, ring)
    return a / (b_n + a * D(0) + (D(12800) * D(Cl)).ln()), b_n, b_D, c_f, cp


def table(S, cA, cU, ring, Cl=D(1), R=D(0)):
    cp, b_n, b_D, c_f = consts(S, cA, cU, ring)
    g2 = a / (b_n + a * R + (D(12800) * Cl).ln())
    nT = b_D / (a * beta * logL)
    out = dict(cp=cp, b_n=b_n, b_D=b_D, c_f=c_f, g2=g2, nT=nT)
    # REL-boot r <= 1/2 and HIST-sum's own condition, in HIST's own per-level constant h (38417/38416) or the
    # session-6 re-derived one; B_* = c_f + 1, B_0 = c_f + 2 (HW l.1710, REVIEW_HW_S5 S5-12)
    for tag, h1, h0 in (('HIST', 38417, 38416), ('sharp', S['hn1'], S['hD'])):
        Bs = c_f + 1
        B0 = c_f + 2
        out['rel_' + tag] = a / (D(h1) * Bs)
        out['hist_' + tag] = a / (D(h1) * B0 + (D(12800) * Cl).ln())
        out['nH_' + tag] = (D(4) + D(h0) * c_f / logL) / (a * beta)
    return out


print("== A1/A6 (CONFIRMATORY): the session-6 constants and ceilings, c_A = 0, c_U = 1, C_l = 1, R = 0 ==")
for S in (S5, S6):
    for ring, rname in ((1, 'no ring'), (17, 'ring x17 (session 6)'), (82, 'ring x82 (PLD §18.4)')):
        t = table(S, 0, 1, ring)
        print("  %s %-22s c_+=%6s b_n=%18.0f b_D=%18.0f c_f=%12.0f  g2_CRC=%s  n_T=%s"
              % (S['name'], rname, t['cp'], t['b_n'], t['b_D'], t['c_f'],
                 ('%.5E' % t['g2']), ('%.5E' % t['nT'])))
res['A1'] = True
res['A6'] = True

print("== A4 (CONFIRMATORY): session 5's own numbers, no ring ==")
t5 = table(S5, 0, 1, 1)
ok4 = (abs(t5['g2'] / D('4.898e-97') - 1) < D('0.01') and abs(t5['nT'] / D('9.991e96') - 1) < D('0.01'))
print("  g2_CRC = %.6E (review S5-12: 4.89789e-97) ; n_T = %.6E (review: 9.99104e96) ; b_n = %.0f (review: 20416938755)"
      % (t5['g2'], t5['nT'], t5['b_n']))
print("  REL-boot ceiling (B_*=c_f+1, HIST 38417) = %.6E (review: 4.89802e-97) ; HIST-sum condition = %.6E (review: 4.898e-97)"
      % (t5['rel_HIST'], t5['hist_HIST']))
print("  n_H(a,B_0) = %.6E (review: 9.99102e96)  ->  reproduction %s" % (t5['nH_HIST'], "OK" if ok4 else "MISMATCH"))
res['A4'] = ok4

print("== A2 (PRE-REGISTERED): does S5-12's four-way coincidence survive at the session-6 constants? ==")
for S in (S5, S6):
    for ring in (1, 17, 82):
        t = table(S, 0, 1, ring)
        for tag in ('HIST', 'sharp'):
            rel = t['rel_' + tag]
            his = t['hist_' + tag]
            agree = max(t['g2'], rel, his) / min(t['g2'], rel, his)
            nagree = max(t['nT'], t['nH_' + tag]) / min(t['nT'], t['nH_' + tag])
            print("  %s ring=%2d per-level=%-5s : (S2)=%.5E REL-boot=%.5E HIST-sum=%.5E  spread=%.4f | "
                  "n_T=%.5E n_H=%.5E ratio=%.4f"
                  % (S['name'], ring, tag, t['g2'], rel, his, agree, t['nT'], t['nH_' + tag], nagree))
res['A2'] = True

print("== A3 (PRE-REGISTERED): g2_CRC against the recorded (RLF-delta) ceiling 1e-94, four scenarios (c_A=0, c_U=1) ==")
scen = [(S5, 1, 'session 5, no ring'), (S5, 82, 'session 5, ring x82'), (S5, 17, 'session 5, ring x17'),
        (S6, 1, 'session 6, no ring'), (S6, 82, 'session 6, ring x82'), (S6, 17, 'session 6, ring x17')]
a3lines = []
for S, ring, nm in scen:
    t = table(S, 0, 1, ring)
    f = t['g2'] / CEIL_RLF
    a3lines.append((nm, t['g2'], f))
    print("  %-22s g2_CRC = %.5E = %.5E x 1e-94  ->  %s the recorded ceiling"
          % (nm, t['g2'], f, "ABOVE" if f >= 1 else "BELOW (breach by %.2f)" % (1 / f)))
res['A3'] = True

print("== A5 (PRE-REGISTERED): against DX' (g_0^2 ~ 2.5e-152/C_Omega, C_Omega = 1) ==")
for S, ring, nm in ((S6, 17, 'session 6, ring x17'), (S6, 82, 'session 6, ring x82'), (S5, 1, 'session 5, no ring')):
    t = table(S, 0, 1, ring)
    slack = t['g2'] / CEIL_DX
    # largest c_+ for which g2 >= CEIL_DX: g2 ~ a/(Csh*81*hn*c_+)
    cmax = a / (CEIL_DX * D(S['Csh'] * 81 * S['hn']))
    print("  %-22s slack against DX' at c_+=1: x%.4E ; g2_CRC >= 2.5e-152 while c_+ <= %.4E"
          % (nm, slack, cmax))
res['A5'] = True

print("== (S1) and a_ret, session 6 with the x17 ring (c_A=0, c_U=1, C_A=1, R=0) ==")
cp6, b_n6, b_D6, c_f6 = consts(S6, 0, 1, 17)
g2_s1 = a / ((Delta2 * D(2)).ln() + cp6 * D(c_att6))
g2ret = a_ret / (cp6 * D(c_att6) + (D(2) * Delta2).ln())
print("  (S1) ceiling = %.5E ; g2_ret = %.5E ; c_att(8) session6 = %d (session 5: %d) ; Delta_rho^2 = %.4E"
      % (g2_s1, g2ret, c_att6, c_att5, Delta2))
print("  (S1) is implied by (S2) here: %s" % (g2_s1 >= a / b_n6))

print("== ratios session 5 -> session 6 (same ring) ==")
for ring in (1, 17, 82):
    r5 = table(S5, 0, 1, ring)
    r6 = table(S6, 0, 1, ring)
    print("  ring=%2d : g2_CRC x%.3f ; n_T /%.3f ; c_f /%.3f" %
          (ring, r6['g2'] / r5['g2'], r5['nT'] / r6['nT'], r5['c_f'] / r6['c_f']))

print("RESULTS: " + " ".join(f"{k}:{'PASS' if v else 'FAIL'}" for k, v in sorted(res.items())))
print("OVERALL A " + ("PASS" if all(res.values()) else "FAIL"))
print("secs %.2f" % (time.time() - t0))

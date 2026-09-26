#!/usr/bin/env python3
"""Independent check of bending over fall at finite wave number.

Does not import the author's script. The packet runs and the straight-line
quadrature were not rebuilt. Hamilton's equations are checked through the
symbol identities they rest on.
"""
import sympy as sp

FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (f" :: {detail}" if detail else ""), flush=True)
    if not ok:
        FAIL.append(name)


k, ell, b = sp.symbols("k ell b", positive=True)
sin_k, cos_k = sp.sin(k), sp.cos(k)
raw = sin_k * (1 + b * cos_k**2)
reach = sin_k * (cos_k**2 + ell * sin_k**2)
check(
    "S symbol",
    sp.simplify(raw.subs(b, 1 / ell - 1) - reach / ell) == 0,
    "with 1+b=1/ell the reach-three symbol is sigma/ell, sigma = sin(cos^2 + ell sin^2)",
)

# frame factor
s_frame = sin_k / ell
frame_factor = sp.simplify(ell**2 * (sp.diff(s_frame, k) ** 2 + s_frame * sp.diff(s_frame, k, 2)))
check("S frame", frame_factor == sp.cos(2 * k), "ell^2 (s'^2 + s s'') = cos 2k, so A <= 1")

t = sp.Rational(3, 10)
cos_k = (1 - t**2) / (1 + t**2)
sin_k = 2 * t / (1 + t**2)
A_frame = sp.simplify(cos_k**2 - sin_k**2)
check(
    "B3 frame below 1",
    A_frame == sp.Rational(4681, 11881) and A_frame < sp.Rational(1, 2),
    "at tan(kappa/2)=3/10, A=4681/11881 < 1/2, so the far ratio is below 1 for a weak body",
)

# reach-three rho and axis speed
sig = sp.sin(k) * (sp.cos(k) ** 2 + ell * sp.sin(k) ** 2)
s = sig / ell
rho = sp.simplify(-ell * sp.diff(sp.log(s), ell))
rho_stated = sp.cos(k) ** 2 / (sp.cos(k) ** 2 + ell * sp.sin(k) ** 2)
axis_speed = sp.simplify(ell * sp.diff(s, k))
series_speed = sp.series(axis_speed, k, 0, 4).removeO()
check(
    "S reach rho",
    sp.simplify(rho - rho_stated) == 0
    and sp.simplify(series_speed - (1 + (3 * ell - sp.Rational(7, 2)) * k**2)) == 0,
    "rho_a = cos^2/(cos^2+ell sin^2); the axis speed exceeds w/ell near k=0 iff ell>7/6",
)
# maximum of cos(1 + 3(ell-1) sin^2) at ell=9/4
u = sp.symbols("u", positive=True)
speed_u = sp.sqrt(u) * (1 + 3 * (sp.Rational(9, 4) - 1) * (1 - u))
# u = cos^2, speed = cos * (1 + (15/4) sin^2) = sqrt(u) * (1 + 15/4 (1-u))
crit = sp.solve(sp.diff(speed_u, u), u)
check(
    "S fast wave",
    sp.Rational(19, 45) in crit
    and sp.simplify(speed_u.subs(u, sp.Rational(19, 45)) - sp.Rational(19, 6) * sp.sqrt(sp.Rational(19, 45))) == 0,
    "at ell=9/4 the fastest axis wave is (19/6) sqrt(19/45) times w/ell",
)

# witness carrier tan(kappa/2)=1/10, ell=9/4, diagonal, gradient across the velocity
lv = sp.Rational(9, 4)
tt = sp.Rational(1, 10)
subs = {
    sp.sin(k): 2 * tt / (1 + tt**2),
    sp.cos(k): (1 - tt**2) / (1 + tt**2),
    ell: lv,
}
factor = sp.simplify((ell**2 * (sp.diff(s, k) ** 2 + s * sp.diff(s, k, 2))).subs(ell, lv).rewrite(sp.sin))
# evaluate by replacing sin, cos after differentiation
factor_num = sp.simplify(factor.subs(subs))
rho_num = sp.simplify(rho_stated.subs(subs))
# group speed in units of w/ell: ell * |grad F|. Two equal components, velocity along (1,1).
# dF/dk_x = d|s|/dk_x. |s| = sqrt(2) |s_component| if both equal, so |grad| = sqrt( (dF/dkx)^2 * 2 ).
comp = sp.simplify(s.subs(ell, lv))
mag = sp.sqrt(2) * comp
grad = sp.diff(comp, k)
speed_ratio = sp.simplify((lv * grad).subs(subs))
check(
    "B2 witness numbers",
    factor_num == sp.Rational(1606444785801, 1061520150601)
    and rho_num == sp.Rational(1089, 1189)
    and speed_ratio == sp.Rational(1158399, 1030301),
    "A=1606444785801/1061520150601, rho=1089/1189, speed=1158399/1030301 times w/ell",
)

G = sp.symbols("G", positive=True)
R = 3 * (2 * G + 1) / (2 * (G + 1))
ratio = sp.simplify(factor_num * (1 + rho_num * (R - 1)))
stated = sp.Rational(1606444785801) * (6734 * G + 3467) / (sp.Rational(2524294918129178) * (G + 1))
check(
    "B2 ratio",
    sp.simplify(ratio - stated) == 0
    and sp.simplify(stated.subs(G, 50)) > 4
    and sp.simplify(stated.subs(G, 1000)) > sp.simplify(stated.subs(G, 50))
    and sp.limit(stated, G, sp.oo) > 4,
    "the witness ratio is the stated function of G; it exceeds 4 at G=50 and rises toward its limit",
)

# long-wave R from the one-body field
g, QQ, g0 = sp.symbols("g Q g0", positive=True)
w0 = 1 / (1 + 2 * QQ * g0)
chi = 1 + QQ * g
capital_n = 1 - QQ * w0 * g
ell_field = chi**2
ww = capital_n / chi
R_field = sp.simplify(1 - sp.diff(sp.log(ell_field), g) / sp.diff(sp.log(ww), g))
R_alt = (2 + 3 * QQ * g0 - QQ * g) / (1 + QQ * g0)
check(
    "B1 long wave",
    sp.simplify(R_field - R_alt) == 0
    and sp.simplify(R_field.subs(g, 0) - (3 + w0) / (1 + w0)) == 0
    and sp.simplify(R_field.subs(g, g0) - 2) == 0,
    "R = (2+3 Qg0 - Qg)/(1+Qg0), equal to 2 at the body and (3+w0)/(1+w0) far away",
)

# small-k anisotropy: A-1 starts at (12 ell - 14) k^2, and at R=3 the diagonal excess is (34 ell - 42) kappa^2
ka = sp.symbols("kappa", positive=True)
sig_series = sp.series(sig, k, 0, 6).removeO()
A_one = ell**2 * (sp.diff(s, k) ** 2 + s * sp.diff(s, k, 2))
A_series = sp.series(A_one, k, 0, 4).removeO()
check(
    "S quartic",
    sp.series(A_series, k, 0, 3).removeO() == 1 + (12 * ell - 14) * k**2,
    "A = 1 + (12 ell - 14) k^2 + ...; it exceeds 1 at small k iff ell > 7/6",
)

print(f"TOTAL FAIL={len(FAIL)}", flush=True)
if FAIL:
    print("SUMMARY: fails at " + ", ".join(FAIL), flush=True)
else:
    print(
        "SUMMARY: PARTIAL at finite wave number the frame ratio is A R with A = cos 2k <= 1, so it stays below 3 and "
        "drops below 1 for a diagonal carrier with tan(kappa/2)=3/10. Reach three has A>1 off axis when ell>7/6. "
        "The witness at ell=9/4 and tan(kappa/2)=1/10 has ratio above 4 for large G. "
        "Long waves stay in (1,3). Packet runs were not rebuilt.",
        flush=True,
    )
    print(
        "HIT: confirmed - under the reach-three coupling a diagonal ray at the witness point bends more than 4 times "
        "the fall of a body at rest once the body is strong, while a short frame wave on the diagonal bends less than "
        "the fall. Long waves stay between 1 and 3.",
        flush=True,
    )

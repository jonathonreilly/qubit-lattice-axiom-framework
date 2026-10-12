"""R13-4 (i): does the local compression P_h H_flat P_h keep R12-3's exact supercharge?
On a basic 1-form omega (T1 toy of r134_oneill_fd.py), X omega = 0, so
  [Q, P_h H_flat P_h] omega = [Q, H_q + T/2] omega = -(1/2) T Q omega,  T := P_h X^dag g^-1 X.
Nonzero T(Q omega) means the compression breaks Q-exactness; Q-exactness forces the O'Neill term."""
import importlib.util, sys, mpmath as mp
spec = importlib.util.spec_from_file_location("fd", __file__.replace("r134_susy_compression.py", "r134_oneill_fd_lib.py"))
fd = importlib.util.module_from_spec(spec); spec.loader.exec_module(fd)
mp.mp.dps = 90; fd.H = mp.mpf('1e-22')   # nesting depth 3: roundoff 1e-90/1e-66, truncation 1e-44
x0 = [mp.mpf(v) for v in ['0.3', '0.5', '-0.4', '0.7', '0.2']]
Q, Qs, Ph, Iu, Wu, mul, plus = fd.make(5, fd.W1, fd.u1, fd.gi1)
om = fd.pull([(fd.F1[0], (0,)), (fd.F1[1], (2,)), (fd.F1[2], (3,))], fd.dy1, 5)
Qom = Q(om)
X = plus(Iu(0, Qs(Qom)), Qs(Iu(0, Qom)))
gX = mul(lambda x: fd.gi1(x)[0][0], X)
T_Qom = Ph(plus(Q(Wu(0, gX)), Wu(0, Q(gX))))(x0)
Hflat = lambda f: plus(mul(lambda x: mp.mpf(1)/2, Q(Qs(f))), mul(lambda x: mp.mpf(1)/2, Qs(Q(f))))
lhs = fd.add(Q(Ph(Hflat(om)))(x0), fd.scal(Ph(Hflat(Qom))(x0), -1))     # [Q, P_h H_flat P_h] omega
print("|Q omega| =", mp.nstr(fd.norm(Qom(x0)), 6), " |T Q omega| =", mp.nstr(fd.norm(T_Qom), 6),
      " |[Q, P_h H_flat P_h] omega| =", mp.nstr(fd.norm(lhs), 6),
      " |[Q,P_hH_flatP_h]omega + T Q omega/2| =", mp.nstr(fd.diffn(lhs, fd.scal(T_Qom, -mp.mpf(1)/2)), 3))

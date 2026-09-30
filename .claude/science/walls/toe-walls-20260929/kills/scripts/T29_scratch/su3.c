// SU(3) Wilson gauge theory, 4D periodic L^4.  T29 attack test.
// mode 0: Cabibbo-Marinari heatbath (Kennedy-Pendleton SU(2)) + n_or overrelaxation sweeps
// mode 1: Metropolis with symmetric SU(2)-subgroup proposals (algorithmically independent)
// usage: su3 L beta nsweep ntherm mode seed start(0 cold,1 hot) n_or mevery outfile
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef double complex cplx;
typedef struct { cplx m[9]; } M3;

static uint64_t rs[4];
static inline uint64_t rotl(uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next64(void) {
  uint64_t r = rotl(rs[1] * 5, 7) * 9, t = rs[1] << 17;
  rs[2] ^= rs[0]; rs[3] ^= rs[1]; rs[1] ^= rs[2]; rs[0] ^= rs[3]; rs[2] ^= t; rs[3] = rotl(rs[3], 45);
  return r;
}
static uint64_t sm(uint64_t *x) { uint64_t z = (*x += 0x9e3779b97f4a7c15ULL); z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL; z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL; return z ^ (z >> 31); }
static inline double urand(void) { return ((next64() >> 11) + 0.5) * (1.0 / 9007199254740992.0); } // (0,1)
static double gauss(void) { double u = urand(), v = urand(); return sqrt(-2 * log(u)) * cos(2 * M_PI * v); }

static int L, V;
static int *up, *dn; // up[s*4+mu]
static M3 *U;
static double beta;

static inline void mul(const M3 *a, const M3 *b, M3 *c) {
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
    c->m[3*i+j] = a->m[3*i]*b->m[j] + a->m[3*i+1]*b->m[3+j] + a->m[3*i+2]*b->m[6+j];
  }
}
static inline void mul_bd(const M3 *a, const M3 *b, M3 *c) { // a * b^dagger
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
    c->m[3*i+j] = a->m[3*i]*conj(b->m[3*j]) + a->m[3*i+1]*conj(b->m[3*j+1]) + a->m[3*i+2]*conj(b->m[3*j+2]);
  }
}
static inline void mul_ad(const M3 *a, const M3 *b, M3 *c) { // a^dagger * b
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
    c->m[3*i+j] = conj(a->m[i])*b->m[j] + conj(a->m[3+i])*b->m[3+j] + conj(a->m[6+i])*b->m[6+j];
  }
}
static inline void mul_add(const M3 *a, const M3 *b, M3 *c) { // a^dagger * b^dagger
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) {
    c->m[3*i+j] = conj(a->m[i])*conj(b->m[3*j]) + conj(a->m[3+i])*conj(b->m[3*j+1]) + conj(a->m[6+i])*conj(b->m[3*j+2]);
  }
}
static inline double retr(const M3 *a) { return creal(a->m[0]) + creal(a->m[4]) + creal(a->m[8]); }
static inline double retr_ab(const M3 *a, const M3 *b) { // Re Tr(a b)
  double s = 0;
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) s += creal(a->m[3*i+j] * b->m[3*j+i]);
  return s;
}

static void reunit(M3 *a) {
  cplx *r0 = a->m, *r1 = a->m + 3, *r2 = a->m + 6;
  double n = 0; for (int j = 0; j < 3; j++) n += creal(r0[j]*conj(r0[j])); n = 1/sqrt(n);
  for (int j = 0; j < 3; j++) r0[j] *= n;
  cplx d = 0; for (int j = 0; j < 3; j++) d += conj(r0[j]) * r1[j];
  for (int j = 0; j < 3; j++) r1[j] -= d * r0[j];
  n = 0; for (int j = 0; j < 3; j++) n += creal(r1[j]*conj(r1[j])); n = 1/sqrt(n);
  for (int j = 0; j < 3; j++) r1[j] *= n;
  r2[0] = conj(r0[1]*r1[2] - r0[2]*r1[1]);
  r2[1] = conj(r0[2]*r1[0] - r0[0]*r1[2]);
  r2[2] = conj(r0[0]*r1[1] - r0[1]*r1[0]);
}
static double unit_err(const M3 *a) {
  M3 t; mul_bd(a, a, &t); double e = 0;
  for (int i = 0; i < 3; i++) for (int j = 0; j < 3; j++) { cplx d = t.m[3*i+j] - (i == j); e = fmax(e, cabs(d)); }
  return e;
}
static void rand_su3(M3 *a) {
  for (int i = 0; i < 9; i++) a->m[i] = gauss() + I * gauss();
  reunit(a);
}
static void setid(M3 *a) { for (int i = 0; i < 9; i++) a->m[i] = 0; a->m[0] = a->m[4] = a->m[8] = 1; }

static const int SG[3][2] = {{0,1},{0,2},{1,2}};

static void staple(int s, int mu, M3 *Vm) {
  M3 t1, t2;
  for (int i = 0; i < 9; i++) Vm->m[i] = 0;
  for (int nu = 0; nu < 4; nu++) {
    if (nu == mu) continue;
    int smu = up[s*4+mu], snu = up[s*4+nu];
    // forward: U_nu(s+mu) U_mu(s+nu)^dag U_nu(s)^dag
    mul_bd(&U[smu*4+nu], &U[snu*4+mu], &t1);
    mul_bd(&t1, &U[s*4+nu], &t2);
    for (int i = 0; i < 9; i++) Vm->m[i] += t2.m[i];
    // backward: U_nu(s+mu-nu)^dag U_mu(s-nu)^dag U_nu(s-nu)
    int sd = dn[s*4+nu], smd = dn[smu*4+nu];
    mul_add(&U[smd*4+nu], &U[sd*4+mu], &t1);
    mul(&t1, &U[sd*4+nu], &t2);
    for (int i = 0; i < 9; i++) Vm->m[i] += t2.m[i];
  }
}

// SU(2) quaternion (q0,q1,q2,q3) <-> matrix [[q0+i q3, q2+i q1],[-q2+i q1, q0-i q3]]
static inline void apply_left(M3 *a, int i, int j, const double *q) {
  cplx r00 = q[0] + I*q[3], r01 = q[2] + I*q[1], r10 = -q[2] + I*q[1], r11 = q[0] - I*q[3];
  for (int c = 0; c < 3; c++) {
    cplx x = a->m[3*i+c], y = a->m[3*j+c];
    a->m[3*i+c] = r00*x + r01*y;
    a->m[3*j+c] = r10*x + r11*y;
  }
}
static inline void quat_mul(const double *a, const double *b, double *c) { // matrix product a*b for SU(2) as above
  cplx a00 = a[0] + I*a[3], a01 = a[2] + I*a[1], a10 = -a[2] + I*a[1], a11 = a[0] - I*a[3];
  cplx b00 = b[0] + I*b[3], b01 = b[2] + I*b[1], b10 = -b[2] + I*b[1], b11 = b[0] - I*b[3];
  cplx c00 = a00*b00 + a01*b10, c01 = a00*b01 + a01*b11;
  c[0] = creal(c00); c[3] = cimag(c00); c[2] = creal(c01); c[1] = cimag(c01);
}
static inline int get_q(const M3 *w, int i, int j, double *q) {
  cplx a = w->m[3*i+i], b = w->m[3*i+j], c = w->m[3*j+i], d = w->m[3*j+j];
  q[0] = 0.5*(creal(a) + creal(d));
  q[3] = 0.5*(cimag(a) - cimag(d));
  q[2] = 0.5*(creal(b) - creal(c));
  q[1] = 0.5*(cimag(b) + cimag(c));
  return 0;
}

static void kp_sample(double alpha, double *x) { // x0 with weight sqrt(1-x0^2) exp(alpha x0); vector uniform
  double x0;
  for (;;) {
    double r1 = urand(), r2 = urand(), r3 = urand(), r4 = urand();
    double c = cos(2*M_PI*r2); c *= c;
    double delta = -(log(r1) + c*log(r3)) / alpha;
    if (r4*r4 <= 1.0 - 0.5*delta) { x0 = 1.0 - delta; break; }
  }
  double s = sqrt(fmax(0.0, 1 - x0*x0));
  double ct = 2*urand() - 1, st = sqrt(1 - ct*ct), ph = 2*M_PI*urand();
  x[0] = x0; x[1] = s*st*cos(ph); x[2] = s*st*sin(ph); x[3] = s*ct;
}

static void update_link_hb(int s, int mu, int ovr) {
  M3 Vm, W; staple(s, mu, &Vm);
  M3 *u = &U[s*4+mu];
  mul(u, &Vm, &W);
  for (int g = 0; g < 3; g++) {
    int i = SG[g][0], j = SG[g][1];
    double q[4]; get_q(&W, i, j, q);
    double k = sqrt(q[0]*q[0] + q[1]*q[1] + q[2]*q[2] + q[3]*q[3]);
    if (k < 1e-12) continue;
    double v[4] = {q[0]/k, q[1]/k, q[2]/k, q[3]/k};
    double vd[4] = {v[0], -v[1], -v[2], -v[3]};
    double R[4];
    if (!ovr) {
      double x[4]; kp_sample(2.0*beta*k/3.0, x);
      quat_mul(x, vd, R);
    } else {
      quat_mul(vd, vd, R);
    }
    apply_left(u, i, j, R);
    apply_left(&W, i, j, R);
  }
}

static double eps_met = 0.35; static long met_acc = 0, met_tot = 0;
static void update_link_met(int s, int mu, int nhit) {
  M3 Vm, W; staple(s, mu, &Vm);
  M3 *u = &U[s*4+mu];
  mul(u, &Vm, &W);
  for (int h = 0; h < nhit; h++) {
    int g = (int)(urand()*3); if (g > 2) g = 2;
    int i = SG[g][0], j = SG[g][1];
    double x[3] = {gauss()*eps_met, gauss()*eps_met, gauss()*eps_met};
    double n2 = x[0]*x[0] + x[1]*x[1] + x[2]*x[2];
    met_tot++;
    if (n2 >= 1) continue; // symmetric rejection of the proposal
    double X[4] = {sqrt(1 - n2), x[0], x[1], x[2]};
    // Re Tr(X W) - Re Tr(W) restricted to rows i,j
    cplx r00 = X[0] + I*X[3], r01 = X[2] + I*X[1], r10 = -X[2] + I*X[1], r11 = X[0] - I*X[3];
    double dTr = 0;
    dTr += creal(r00*W.m[3*i+i] + r01*W.m[3*j+i]) - creal(W.m[3*i+i]);
    dTr += creal(r10*W.m[3*i+j] + r11*W.m[3*j+j]) - creal(W.m[3*j+j]);
    double dS = (beta/3.0) * dTr; // weight exp(+dS)
    if (dS >= 0 || urand() < exp(dS)) {
      apply_left(u, i, j, X); apply_left(&W, i, j, X); met_acc++;
    }
  }
}

static double plaq(void) {
  double sum = 0; M3 t1;
  for (int s = 0; s < V; s++) for (int mu = 0; mu < 4; mu++) for (int nu = mu + 1; nu < 4; nu++) {
    int smu = up[s*4+mu], snu = up[s*4+nu];
    mul(&U[s*4+mu], &U[smu*4+nu], &t1);
    // P = U_mu(s) U_nu(s+mu) U_mu(s+nu)^dag U_nu(s)^dag
    M3 a, b;
    mul_bd(&t1, &U[snu*4+mu], &a);
    mul_bd(&a, &U[s*4+nu], &b);
    sum += retr(&b) / 3.0;
  }
  return sum / (6.0 * V);
}

#define RMAX 4
static M3 *line[4][RMAX + 1]; // line[mu][R][s]
static double wl[RMAX + 1][RMAX + 1];
static void loops(void) {
  for (int mu = 0; mu < 4; mu++) {
    for (int s = 0; s < V; s++) line[mu][1][s] = U[s*4+mu];
    for (int R = 2; R <= RMAX; R++) for (int s = 0; s < V; s++) {
      // line R at s = U_mu(s) * line R-1 at s+mu
      mul(&U[s*4+mu], &line[mu][R-1][up[s*4+mu]], &line[mu][R][s]);
    }
  }
  memset(wl, 0, sizeof wl);
  for (int mu = 0; mu < 4; mu++) for (int nu = 0; nu < 4; nu++) {
    if (mu == nu) continue;
    for (int R = 1; R <= RMAX; R++) for (int T = 1; T <= RMAX; T++) {
      double sum = 0;
      for (int s = 0; s < V; s++) {
        int s1 = s; for (int k = 0; k < R; k++) s1 = up[s1*4+mu];
        int s2 = s; for (int k = 0; k < T; k++) s2 = up[s2*4+nu];
        M3 a, b, c;
        mul(&line[mu][R][s], &line[nu][T][s1], &a);
        mul_bd(&a, &line[mu][R][s2], &b);
        mul_bd(&b, &line[nu][T][s], &c);
        sum += retr(&c) / 3.0;
      }
      wl[R][T] += sum / V / 12.0;
    }
  }
}

int main(int argc, char **argv) {
  if (argc < 11) { fprintf(stderr, "usage\n"); return 1; }
  L = atoi(argv[1]); beta = atof(argv[2]);
  long nsweep = atol(argv[3]), ntherm = atol(argv[4]);
  int mode = atoi(argv[5]); uint64_t seed = strtoull(argv[6], 0, 10);
  int start = atoi(argv[7]); int n_or = atoi(argv[8]); long mevery = atol(argv[9]);
  const char *outf = argv[10];
  V = L*L*L*L;
  uint64_t x = seed; for (int i = 0; i < 4; i++) rs[i] = sm(&x);
  up = malloc(sizeof(int) * V * 4); dn = malloc(sizeof(int) * V * 4);
  for (int s = 0; s < V; s++) {
    int c[4] = {s % L, (s / L) % L, (s / (L*L)) % L, s / (L*L*L)};
    for (int mu = 0; mu < 4; mu++) {
      int cu[4], cd[4]; memcpy(cu, c, sizeof c); memcpy(cd, c, sizeof c);
      cu[mu] = (c[mu] + 1) % L; cd[mu] = (c[mu] + L - 1) % L;
      up[s*4+mu] = cu[0] + L*(cu[1] + L*(cu[2] + L*cu[3]));
      dn[s*4+mu] = cd[0] + L*(cd[1] + L*(cd[2] + L*cd[3]));
    }
  }
  U = malloc(sizeof(M3) * V * 4);
  for (int i = 0; i < V*4; i++) { if (start) rand_su3(&U[i]); else setid(&U[i]); }
  if (mevery > 0) for (int mu = 0; mu < 4; mu++) for (int R = 1; R <= RMAX; R++) line[mu][R] = malloc(sizeof(M3) * V);
  FILE *fo = fopen(outf, "w");
  fprintf(fo, "# L=%d beta=%.6f nsweep=%ld ntherm=%ld mode=%d seed=%llu start=%d n_or=%d\n", L, beta, nsweep, ntherm, mode, (unsigned long long)seed, start, n_or);
  double maxerr = 0; clock_t t0 = clock();
  for (long it = 0; it < ntherm + nsweep; it++) {
    if (mode == 0) {
      for (int s = 0; s < V; s++) for (int mu = 0; mu < 4; mu++) update_link_hb(s, mu, 0);
      for (int o = 0; o < n_or; o++) for (int s = 0; s < V; s++) for (int mu = 0; mu < 4; mu++) update_link_hb(s, mu, 1);
    } else {
      for (int s = 0; s < V; s++) for (int mu = 0; mu < 4; mu++) update_link_met(s, mu, 6);
    }
    for (int i = 0; i < V*4; i++) reunit(&U[i]);
    if (it % 20 == 0) { for (int i = 0; i < V*4; i += 7) maxerr = fmax(maxerr, unit_err(&U[i])); }
    if (it >= ntherm) {
      double p = plaq();
      fprintf(fo, "%ld %.9f", it - ntherm, p);
      if (mevery > 0 && ((it - ntherm) % mevery == 0)) {
        loops();
        for (int R = 1; R <= RMAX; R++) for (int T = 1; T <= RMAX; T++) fprintf(fo, " %.9f", wl[R][T]);
      }
      fprintf(fo, "\n");
    }
    if (it == ntherm - 1 || it == ntherm + nsweep - 1) fflush(fo);
  }
  fprintf(fo, "# maxunit_err=%.3e met_acc=%.4f time=%.1fs\n", maxerr, met_tot ? (double)met_acc/met_tot : 0.0, (double)(clock() - t0) / CLOCKS_PER_SEC);
  fclose(fo);
  return 0;
}

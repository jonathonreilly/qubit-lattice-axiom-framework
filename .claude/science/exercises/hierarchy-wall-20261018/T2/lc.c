/* T-LIGHTCONE simulator. The landed 09-23 model on the doubled graph.
   Vertices (x,a), a in {0,1}, x on the L^3 torus. Edges (x,a)-(x+d,1-a), d in N7 = {0, +-e_j}.
   Pair law  ~ exp(beta * sum_edges s.s')   (T1 of the landed note).
   modes:
     wolff L beta nmeas ntherm seed out nlev   -> per meas: E, |M|^2, |M0|^2, |F_k|^2(avg 3 axes), then MCRG ops for levels 1..nlev
     lc    L beta nticks ntherm seed out        -> landed kernel, per tick: |M_level|^2, E_pair
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

static uint64_t rs[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static inline uint64_t nxt(void) {
  const uint64_t result = rotl(rs[1] * 5, 7) * 9; const uint64_t t = rs[1] << 17;
  rs[2] ^= rs[0]; rs[3] ^= rs[1]; rs[1] ^= rs[2]; rs[0] ^= rs[3]; rs[2] ^= t; rs[3] = rotl(rs[3], 45);
  return result;
}
static inline double U(void) { return (nxt() >> 11) * 0x1.0p-53; }
static void seedrng(uint64_t s) { for (int i = 0; i < 4; i++) { s += 0x9e3779b97f4a7c15ULL; uint64_t z = s;
  z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL; z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL; rs[i] = z ^ (z >> 31); } }
static void randunit(double *v) { double z = 2 * U() - 1, p = 2 * M_PI * U(), r = sqrt(1 - z * z); v[0] = r * cos(p); v[1] = r * sin(p); v[2] = z; }

static int L, N, NV;
static int *nb; /* NV x 7 */
static double *s; /* NV x 3 */
static int idx(int x, int y, int z) { x = (x + L) % L; y = (y + L) % L; z = (z + L) % L; return (x * L + y) * L + z; }
static void build(void) {
  N = L * L * L; NV = 2 * N; nb = malloc(sizeof(int) * NV * 7); s = malloc(sizeof(double) * NV * 3);
  int dd[7][3] = {{0,0,0},{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
  for (int a = 0; a < 2; a++) for (int x = 0; x < L; x++) for (int y = 0; y < L; y++) for (int z = 0; z < L; z++) {
    int v = a * N + idx(x, y, z);
    for (int k = 0; k < 7; k++) nb[v * 7 + k] = (1 - a) * N + idx(x + dd[k][0], y + dd[k][1], z + dd[k][2]);
  }
}
static double energy(void) { /* sum over edges: each edge once, from level-1 side */
  double e = 0; for (int x = 0; x < N; x++) { int v = N + x; double *a = s + 3 * v;
    for (int k = 0; k < 7; k++) { double *b = s + 3 * nb[v * 7 + k]; e += a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; } }
  return e;
}
/* Wolff */
static int *stk, *mark; static int gen = 0;
static int wolff(double beta) {
  double r[3]; randunit(r); gen++;
  int v0 = (int)(U() * NV); if (v0 >= NV) v0 = NV - 1;
  int sp = 0, sz = 0; stk[sp++] = v0; mark[v0] = gen;
  while (sp) {
    int v = stk[--sp]; double *a = s + 3 * v; double pa = a[0] * r[0] + a[1] * r[1] + a[2] * r[2];
    a[0] -= 2 * pa * r[0]; a[1] -= 2 * pa * r[1]; a[2] -= 2 * pa * r[2]; sz++;
    for (int k = 0; k < 7; k++) { int w = nb[v * 7 + k]; if (mark[w] == gen) continue; double *b = s + 3 * w;
      double pb = b[0] * r[0] + b[1] * r[1] + b[2] * r[2]; double q = pa * pb; /* pre-flip product */
      if (q > 0 && U() < 1 - exp(-2 * beta * q)) { mark[w] = gen; stk[sp++] = w; } }
  }
  return sz;
}
/* vMF draw on S^2 around unit mu with concentration kap */
static void vmf(const double *h, double beta, double *out) {
  double hn = sqrt(h[0] * h[0] + h[1] * h[1] + h[2] * h[2]); double kap = beta * hn; double w;
  if (hn < 1e-14) { randunit(out); return; }
  double u = U();
  if (kap < 1e-8) w = 2 * u - 1; else w = 1 + log(u + (1 - u) * exp(-2 * kap)) / kap;
  if (w > 1) w = 1; if (w < -1) w = -1;
  double mu[3] = {h[0] / hn, h[1] / hn, h[2] / hn}; double t[3];
  if (fabs(mu[0]) < 0.9) { t[0] = 0; t[1] = -mu[2]; t[2] = mu[1]; } else { t[0] = mu[2]; t[1] = 0; t[2] = -mu[0]; }
  double tn = sqrt(t[0] * t[0] + t[1] * t[1] + t[2] * t[2]); t[0] /= tn; t[1] /= tn; t[2] /= tn;
  double b2[3] = {mu[1] * t[2] - mu[2] * t[1], mu[2] * t[0] - mu[0] * t[2], mu[0] * t[1] - mu[1] * t[0]};
  double p = 2 * M_PI * U(), rr = sqrt(1 - w * w), c = rr * cos(p), d = rr * sin(p);
  for (int i = 0; i < 3; i++) out[i] = w * mu[i] + c * t[i] + d * b2[i];
}

/* MCRG blocking */
static int nlev = 0; static double *blk[8]; static int bl[8];
static inline double dot(const double *a, const double *b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
static void normalize(double *a) { double n = sqrt(dot(a, a)); if (n < 1e-300) { randunit(a); return; } a[0] /= n; a[1] /= n; a[2] /= n; }
static void do_block(void) {
  /* level 1: from doubled graph, 2x2x2 cube on both levels */
  int Lb = L / 2; bl[1] = Lb; double *B = blk[1]; memset(B, 0, sizeof(double) * 3 * Lb * Lb * Lb);
  for (int a = 0; a < 2; a++) for (int x = 0; x < L; x++) for (int y = 0; y < L; y++) for (int z = 0; z < L; z++) {
    int v = a * N + idx(x, y, z); int X = ((x / 2) * Lb + y / 2) * Lb + z / 2;
    B[3 * X] += s[3 * v]; B[3 * X + 1] += s[3 * v + 1]; B[3 * X + 2] += s[3 * v + 2]; }
  for (int X = 0; X < Lb * Lb * Lb; X++) normalize(B + 3 * X);
  for (int n = 2; n <= nlev; n++) {
    int Lp = bl[n - 1], Ln = Lp / 2; bl[n] = Ln; double *P = blk[n - 1], *Q = blk[n]; memset(Q, 0, sizeof(double) * 3 * Ln * Ln * Ln);
    for (int x = 0; x < Lp; x++) for (int y = 0; y < Lp; y++) for (int z = 0; z < Lp; z++) {
      int v = (x * Lp + y) * Lp + z; int X = ((x / 2) * Ln + y / 2) * Ln + z / 2;
      Q[3 * X] += P[3 * v]; Q[3 * X + 1] += P[3 * v + 1]; Q[3 * X + 2] += P[3 * v + 2]; }
    for (int X = 0; X < Ln * Ln * Ln; X++) normalize(Q + 3 * X);
  }
}
static inline int cid(int Lc, int x, int y, int z) { x = ((x % Lc) + Lc) % Lc; y = ((y % Lc) + Lc) % Lc; z = ((z % Lc) + Lc) % Lc; return (x * Lc + y) * Lc + z; }
/* ops: even[6], odd[9] */
static void ops(int n, double *o) {
  int Lc = bl[n]; double *S = blk[n]; for (int i = 0; i < 15; i++) o[i] = 0;
  int e1[3][3] = {{1,0,0},{0,1,0},{0,0,1}};
  int fd[6][3] = {{1,1,0},{1,-1,0},{1,0,1},{1,0,-1},{0,1,1},{0,1,-1}};
  int bd[4][3] = {{1,1,1},{1,1,-1},{1,-1,1},{1,-1,-1}};
  for (int x = 0; x < Lc; x++) for (int y = 0; y < Lc; y++) for (int z = 0; z < Lc; z++) {
    double *a = S + 3 * cid(Lc, x, y, z);
    double hnn[3] = {0,0,0}, hfd[3] = {0,0,0};
    for (int k = 0; k < 3; k++) { double *b = S + 3 * cid(Lc, x + e1[k][0], y + e1[k][1], z + e1[k][2]); double d = dot(a, b); o[0] += d; o[4] += d * d;
      double *b2 = S + 3 * cid(Lc, x + 2 * e1[k][0], y + 2 * e1[k][1], z + 2 * e1[k][2]); o[3] += dot(a, b2); }
    for (int k = 0; k < 6; k++) { double *b = S + 3 * cid(Lc, x + fd[k][0], y + fd[k][1], z + fd[k][2]); o[1] += dot(a, b); }
    for (int k = 0; k < 4; k++) { double *b = S + 3 * cid(Lc, x + bd[k][0], y + bd[k][1], z + bd[k][2]); o[2] += dot(a, b); }
    /* plaquettes */
    for (int i = 0; i < 3; i++) for (int j = i + 1; j < 3; j++) {
      double *pb = S + 3 * cid(Lc, x + e1[i][0], y + e1[i][1], z + e1[i][2]);
      double *pc = S + 3 * cid(Lc, x + e1[i][0] + e1[j][0], y + e1[i][1] + e1[j][1], z + e1[i][2] + e1[j][2]);
      double *pd = S + 3 * cid(Lc, x + e1[j][0], y + e1[j][1], z + e1[j][2]);
      o[5] += dot(a, pb) * dot(pc, pd) + dot(a, pd) * dot(pb, pc); }
    /* odd */
    for (int k = 0; k < 3; k++) for (int sg = -1; sg <= 1; sg += 2) { double *b = S + 3 * cid(Lc, x + sg * e1[k][0], y + sg * e1[k][1], z + sg * e1[k][2]);
      hnn[0] += b[0]; hnn[1] += b[1]; hnn[2] += b[2]; }
    for (int k = 0; k < 6; k++) for (int sg = -1; sg <= 1; sg += 2) { double *b = S + 3 * cid(Lc, x + sg * fd[k][0], y + sg * fd[k][1], z + sg * fd[k][2]);
      hfd[0] += b[0]; hfd[1] += b[1]; hfd[2] += b[2]; }
    double c1 = dot(a, hnn), c2 = dot(a, hfd);
    for (int i = 0; i < 3; i++) { o[6 + i] += a[i]; o[9 + i] += a[i] * c1; o[12 + i] += a[i] * c2; }
  }
}

int main(int argc, char **argv) {
  if (argc < 7) { fprintf(stderr, "usage\n"); return 1; }
  const char *mode = argv[1]; L = atoi(argv[2]); double beta = atof(argv[3]); long nmeas = atol(argv[4]); long nth = atol(argv[5]);
  seedrng((uint64_t)atoll(argv[6])); FILE *fo = fopen(argv[7], "wb"); if (argc > 8) nlev = atoi(argv[8]);
  build(); for (int v = 0; v < NV; v++) randunit(s + 3 * v);
  if (!strcmp(mode, "wolff")) {
    stk = malloc(sizeof(int) * NV); mark = calloc(NV, sizeof(int));
    for (int n = 1; n <= nlev; n++) { int Lb = L >> n; blk[n] = malloc(sizeof(double) * 3 * Lb * Lb * Lb); }
    /* ntherm in sweeps: thermalise by cumulative flipped sites, then estimate the mean cluster */
    double csum = 0; long ccount = 0; double tot = 0;
    while (tot < (double)nth * NV) tot += wolff(beta);
    tot = 0; while (tot < 0.5 * (double)nth * NV) { int c = wolff(beta); tot += c; csum += c; ccount++; }
    double mc = csum / ccount; int ncl = (int)(NV / mc); if (ncl < 1) ncl = 1;
    fprintf(stderr, "L=%d beta=%.5f mean cluster %.1f, clusters/meas %d\n", L, beta, mc, ncl);
    double kk = 2 * M_PI / L; double *cs = malloc(sizeof(double) * L), *sn = malloc(sizeof(double) * L);
    for (int i = 0; i < L; i++) { cs[i] = cos(kk * i); sn[i] = sin(kk * i); }
    double rec[4 + 15 * 8];
    for (long m = 0; m < nmeas; m++) {
      for (int c = 0; c < ncl; c++) wolff(beta);
      double M[3] = {0,0,0}, M0[3] = {0,0,0}; double Fr[3][3] = {{0}}, Fi[3][3] = {{0}};
      for (int a = 0; a < 2; a++) for (int x = 0; x < L; x++) for (int y = 0; y < L; y++) for (int z = 0; z < L; z++) {
        int v = a * N + (x * L + y) * L + z; double *q = s + 3 * v;
        for (int i = 0; i < 3; i++) { M[i] += q[i]; if (a == 0) M0[i] += q[i];
          Fr[0][i] += q[i] * cs[x]; Fi[0][i] += q[i] * sn[x]; Fr[1][i] += q[i] * cs[y]; Fi[1][i] += q[i] * sn[y]; Fr[2][i] += q[i] * cs[z]; Fi[2][i] += q[i] * sn[z]; } }
      double fk = 0; for (int ax = 0; ax < 3; ax++) for (int i = 0; i < 3; i++) fk += Fr[ax][i] * Fr[ax][i] + Fi[ax][i] * Fi[ax][i];
      rec[0] = energy(); rec[1] = dot(M, M); rec[2] = dot(M0, M0); rec[3] = fk / 3;
      int nr = 4;
      if (nlev > 0) { do_block(); for (int n = 1; n <= nlev; n++) { ops(n, rec + nr); nr += 15; } }
      fwrite(rec, sizeof(double), nr, fo);
    }
  } else { /* landed kernel, tick by tick */
    double *s2 = malloc(sizeof(double) * 3 * N); double *cur = s, *nw = s2; double rec[2];
    for (long t = 0; t < nth + nmeas; t++) {
      double M[3] = {0,0,0}, E = 0;
      for (int x = 0; x < N; x++) { double h[3] = {0,0,0}; int v = N + x; /* nb of level-1 vertex x are level-0 vertices x+d */
        for (int k = 0; k < 7; k++) { int w = nb[v * 7 + k] - N + N; int y = w; /* index into level 0 = 0..N-1 */
          double *b = cur + 3 * y; h[0] += b[0]; h[1] += b[1]; h[2] += b[2]; }
        double *o = nw + 3 * x; vmf(h, beta, o); E += dot(o, h); M[0] += o[0]; M[1] += o[1]; M[2] += o[2]; }
      double *tmp = cur; cur = nw; nw = tmp;
      if (t >= nth) { rec[0] = dot(M, M); rec[1] = E; fwrite(rec, sizeof(double), 2, fo); }
    }
  }
  fclose(fo); return 0;
}

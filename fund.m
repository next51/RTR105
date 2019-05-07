function dfx = fund(Ur)
global Ein
global I0
global R
global a
dfx = -1/R -a*I0*exp(a*(Ein-Ur));

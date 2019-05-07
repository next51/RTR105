function fx = funx(Ur)
global Ein
global I0
global R
global a
fx = I0*(exp(a*(Ein-Ur))-1)-Ur/R;

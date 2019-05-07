% Apzimesim funkciju f = x^2-4
x0 = 10;
x1 = x0-(x0^2-4)/(2*x0)
x2 = x1-(x1^2-4)/(2*x1)
x3 = x2-(x2^2-4)/(2*x2)
x4 = x3-(x3^2-4)/(2*x3)
x5 = x4-(x4^2-4)/(2*x4)
%Kedes sprieguma aprekinashana
% Ein = Ud + Ur
% Ir = Ur/R
% Id = I0*(exp*(a*Ud)-1)
% Id = I0*(exp*(a*(Ein-Ur))-1)
% Id = I0*(exp*(a*(Ein-Ur))-1)-Ur/R = 0
global Ein I0 a R
I0 = 1;
a = 1;
R = 10;

t= 0:0.1:1;
eint = 100*sin(2*pi*t*2);

Urt = [];

for Ein = eint
    ur = newmet("funx","fund")
    Urt = [Urt, ur]
end 

plot(t,eint,'b',t,Urt,'r')


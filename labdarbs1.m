Vm = [1 3 5 5.5 9];
Im = [10 25 55 60 190; 12 26 58 59 199; 8 25 50 70 186]*1e-3;

Imv = mean(Im);

V = min(Vm):0.01:max(Vm);
C = polyfit(Vm,Imv,2);
%I = C(1)*V.^3+C(2)*V.^2+C(3)*V.^1+...
I = polyval(C,V);
plot(Vm,Imv,"k*",V,I)
xlabel("U,V")
ylabel("I,A")
title("Grafiks")
grid on
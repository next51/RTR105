syms x
x = x^3;
f = diff(x);
x=-5:0.01:5;
y=eval(vectorize(f));
plot(x,y,'k')
grid on
xlabel('x')
ylabel('y')
title('f(x)=3*x^2')
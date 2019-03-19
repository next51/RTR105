syms x
x = x^3;
f = diff(x);
x=-5:0.01:5;
y=eval(vectorize(f));
plot(x,y,'k')
grid on
xlabel('x')
ylabel('y')
title('Otra uzdevuma grafiki')
hold on
syms X
X = X^3;
f = int(X);
X=0:0.01:5;
Y=eval(vectorize(f));
plot(X,Y)
legend('y=3x^2','y=x^4/4')
hold off

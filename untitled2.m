syms x
g1 = double(int(0*x,x,0,1))
g2 = double(int(sin(2*pi*(x-1)*1.25),x,1,2))
g3 = double(int(-2*(x-2.5),x,2,3))
g4 = double(int(-1,x,3,4))
vid = (g1+g2+g3+g4)/4


h = 0.01;
t = 0:h:5;

vid_t = (1/(length(t)-1))*sum(funkcija(t(1:end-1)))

plot(t,funkcija,t,vid*ones(size(t)))
grid on


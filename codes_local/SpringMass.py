GlowScript 3.0 VPython
tgraph=graph(title="Oscillating Mass", xtitle="t", ytitle="x")
f1=gcurve(color=color.blue)
k=4

wall=box(pos=vector(-0.05,0,0), size=vector(0.01,0.1,0.1))

ball=sphere(pos=vector(0.15,0,0), radius=0.03, color=color.yellow)
spring=helix(pos=wall.pos, axis=ball.pos-wall.pos, radius=0.02, thickness=0.007)
ball.m=.1

L0=.2
ball.p=ball.m*vector(.15,0,0)

t=0
dt=0.01

while t<15:
  rate(100)
  L=ball.pos-wall.pos
  F=k*(L0-mag(L))*norm(L)
  ball.p=ball.p+F*dt
  ball.pos=ball.pos+ball.p*dt/ball.m
  spring.axis=L
  f1.plot(t,ball.pos.x)
  t=t+dt
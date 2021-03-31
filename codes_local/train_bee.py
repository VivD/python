t_dis = 100 #miles
t_spd = 20  #mph
b_spd = 40  #mph
n     = 100000
x     = 0
n_spd = t_spd + b_spd #mph
t_out = t_dis / n_spd
print(t_out)
for i in range(n):
  x += 200*(1/3)**i
print(x)
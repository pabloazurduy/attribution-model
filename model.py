from scipy.stats import gamma

# simulation model 
# "real" parameters 
# ig[p], ig[r], tk, gl, off
pop_size = 10000
w =  [0.01, 0.02, 0.03, 0.05, 0.01] #market values no heterogenity 
w_bias = gamma.rvs(a = 2, scale=1, size=pop_size)
# generate campaings
days_sim = 7 * 20

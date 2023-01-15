import MDAnalysis as mda
import matplotlib.pyplot as plt
import numpy as np

u = mda.Universe('asyn.psf', 'asyn.dcd')
protein = u.select_atoms('all')

position_array = np.zeros((u.trajectory.n_frames, protein.n_atoms, 3))
for ts in u.trajectory:
    position_array[ts.frame] = (protein.positions[:, 0:3])

k_vec = 1 / 3.9 * np.array([1, 1, 1])


# @njit(fastmath=True)
def calculate_ISF(max_t):
    lagtimes = np.arange(1, max_t + 1)
    timeseries = np.zeros((max_t, 2))
    timeseries[:, 0] = lagtimes
    for lag in lagtimes:
        print(lag)
        dr_vec = position_array[lag:, :, :] - position_array[:-lag, :, :]
        dr_mul_k = np.sum(dr_vec * k_vec, axis=2)
        # take care of when wave vector is orthogonal to dr vector, at this point, sin(x)/x=1
        sinA_div_A = np.divide(np.sin(dr_mul_k), dr_mul_k, out=np.ones_like(dr_mul_k), where=dr_mul_k != 0)
        timeseries[lag - 1, 1] = np.mean(sinA_div_A)

    # normalize timeseries
    return timeseries / timeseries[0]


results = calculate_ISF(500)

plt.plot(results[:, 0], results[:, 1])
plt.xscale('log')
plt.savefig('isf.png')

np.savetxt('result.dat', results)

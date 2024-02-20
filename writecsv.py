import riemann_solver
import csv

def main():
    # Left State
    rho_L = 1.0
    vx_L  = 0.0
    P_L   = 1.0

	# Right State
    rho_R = 0.125
    vx_R  = 0.0
    P_R   = 0.1

	# ideal gas gamma
    gamma = 5./3. 
	
	# time 
    t     = 1.0
	
	# Riemann Solver 
    rs = riemann_solver.RiemannSolver(rho_L, vx_L, P_L, rho_R, vx_R, P_R, gamma, t)
    x, rho, vx, P = rs.solve()

    # export
    with open('riemann_solution.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['x', 'rho', 'vx', 'P'])
        for i in range(len(x)):
            writer.writerow([x[i], rho[i], vx[i], P[i]])


if __name__ == "__main__":
    main()
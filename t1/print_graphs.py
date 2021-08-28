import numpy as np
import matplotlib.pyplot as plt


def main():
    # Degree - PMF
    adj_g_pmf = np.loadtxt('data/adjnouns-degree-pmf.txt', delimiter=',')
    adj_g_x = np.loadtxt('data/adjnouns-degree-x.txt', delimiter=',')

    cel_g_pmf = np.loadtxt('data/celegans-degree-pmf.txt', delimiter=',')
    cel_g_x = np.loadtxt('data/celegans-degree-x.txt', delimiter=',')

    hos_g_pmf = np.loadtxt('data/hospital-degree-pmf.txt', delimiter=',')
    hos_g_x = np.loadtxt('data/hospital-degree-x.txt', delimiter=',')

    pro_g_pmf = np.loadtxt('data/protein-degree-pmf.txt', delimiter=',')
    pro_g_x = np.loadtxt('data/protein-degree-x.txt', delimiter=',')

    plt.figure(figsize=(5, 5))
    plt.title('Empirical PMF (Degree)')
    plt.plot(adj_g_x, adj_g_pmf, alpha=0.5, label='Adjnouns')
    plt.scatter(adj_g_x, adj_g_pmf, alpha=0.5)
    plt.plot(cel_g_x, cel_g_pmf, alpha=0.5, label='C. Elegans')
    plt.scatter(cel_g_x, cel_g_pmf, alpha=0.5)
    plt.plot(hos_g_x, hos_g_pmf, alpha=0.5, label='Hospital')
    plt.scatter(hos_g_x, hos_g_pmf, alpha=0.5)
    plt.plot(pro_g_x, pro_g_pmf, alpha=0.5, label='Protein')
    plt.scatter(pro_g_x, pro_g_pmf, alpha=0.5)
    plt.xlabel('Degree')
    plt.ylabel('Probability')
    plt.xlim(0, 60)
    plt.legend()
    plt.savefig('figs/degree_pmf.jpg')

    # Dista - PMF
    adj_d_pmf = np.loadtxt('data/adjnouns-dista-pmf.txt', delimiter=',')
    adj_d_x = np.loadtxt('data/adjnouns-dista-x.txt', delimiter=',')

    cel_d_pmf = np.loadtxt('data/celegans-dista-pmf.txt', delimiter=',')
    cel_d_x = np.loadtxt('data/celegans-dista-x.txt', delimiter=',')

    hos_d_pmf = np.loadtxt('data/hospital-dista-pmf.txt', delimiter=',')
    hos_d_x = np.loadtxt('data/hospital-dista-x.txt', delimiter=',')

    pro_d_pmf = np.loadtxt('data/protein-dista-pmf.txt', delimiter=',')
    pro_d_x = np.loadtxt('data/protein-dista-x.txt', delimiter=',')

    plt.figure(figsize=(5, 5))
    plt.title('Empirical PMF (Distance)')
    plt.plot(adj_d_x, adj_d_pmf, alpha=0.5, label='Adjnouns')
    plt.scatter(adj_d_x, adj_d_pmf, alpha=0.5)
    plt.plot(cel_d_x, cel_d_pmf, alpha=0.5, label='C. Elegans')
    plt.scatter(cel_d_x, cel_d_pmf, alpha=0.5)
    plt.plot(hos_d_x, hos_d_pmf, alpha=0.5, label='Hospital')
    plt.scatter(hos_d_x, hos_d_pmf, alpha=0.5)
    plt.plot(pro_d_x, pro_d_pmf, alpha=0.5, label='Protein')
    plt.scatter(pro_d_x, pro_d_pmf, alpha=0.5)
    plt.xlabel('Distance')
    plt.ylabel('Probability')
    plt.xlim(0, 10)
    plt.legend()
    plt.savefig('figs/distance_pmf.jpg')

    # Degree - CCDF
    adj_g_ccdf = np.loadtxt('data/adjnouns-degree-ccdf.txt', delimiter=',')

    cel_g_ccdf = np.loadtxt('data/celegans-degree-ccdf.txt', delimiter=',')

    hos_g_ccdf = np.loadtxt('data/hospital-degree-ccdf.txt', delimiter=',')

    pro_g_ccdf = np.loadtxt('data/protein-degree-ccdf.txt', delimiter=',')

    plt.figure(figsize=(5, 5))
    plt.title('Empirical CCDF (Degree)')
    #plt.plot(adj_g_x, adj_g_ccdf, alpha=0.5, label='Adjnouns')
    plt.scatter(adj_g_x, adj_g_ccdf, alpha=0.5, label='Adjnouns')
    #plt.plot(cel_g_x, cel_g_ccdf, alpha=0.5, label='C. Elegans')
    plt.scatter(cel_g_x, cel_g_ccdf, alpha=0.5, label='C. Elegans')
    #plt.plot(hos_g_x, hos_g_ccdf, alpha=0.5, label='Hospital')
    plt.scatter(hos_g_x, hos_g_ccdf, alpha=0.5, label='Hospital')
    #plt.plot(pro_g_x, pro_g_ccdf, alpha=0.5, label='Protein')
    plt.scatter(pro_g_x, pro_g_ccdf, alpha=0.5, label='Protein')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree')
    plt.ylabel('CCDF')
    plt.legend()
    plt.savefig('figs/degree_ccdf.jpg')

    # Dista - CCDF
    adj_d_ccdf = np.loadtxt('data/adjnouns-dista-ccdf.txt', delimiter=',')

    cel_d_ccdf = np.loadtxt('data/celegans-dista-ccdf.txt', delimiter=',')

    hos_d_ccdf = np.loadtxt('data/hospital-dista-ccdf.txt', delimiter=',')

    pro_d_ccdf = np.loadtxt('data/protein-dista-ccdf.txt', delimiter=',')

    plt.figure(figsize=(5, 5))
    plt.title('Empirical CCDF (Distance)')
    #plt.plot(adj_d_x, adj_d_ccdf, alpha=0.5, label='Adjnouns')
    plt.scatter(adj_d_x, adj_d_ccdf, alpha=0.5, label='Adjnouns')
    #plt.plot(cel_d_x, cel_d_ccdf, alpha=0.5, label='C. Elegans')
    plt.scatter(cel_d_x, cel_d_ccdf, alpha=0.5, label='C. Elegans')
    #plt.plot(hos_d_x, hos_d_ccdf, alpha=0.5, label='Hospital')
    plt.scatter(hos_d_x, hos_d_ccdf, alpha=0.5, label='Hospital')
    #plt.plot(pro_d_x, pro_d_ccdf, alpha=0.5, label='Protein')
    plt.scatter(pro_d_x, pro_d_ccdf, alpha=0.5, label='Protein')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Distance')
    plt.ylabel('CCDF')
    plt.legend()
    plt.savefig('figs/distance-ccdf.jpg')


if __name__ == '__main__':
    main()

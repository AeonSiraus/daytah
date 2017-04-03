import numpy as np
import matplotlib.pyplot as plt


def plot_lbf(data, x_axis,  y_axis, x_label=0, y_label=0,
             err=False, R=False, save=0, show=True, shows=True):
    if x_label == 0:
        x_label = x_axis
    if y_label == 0:
        y_label = y_axis
    xd = [float(row) for row in data[x_axis]]
    yd = [float(row) for row in data[y_axis]]

    # sort the data
    reorder = sorted(range(len(xd)), key=lambda ii: xd[ii])
    xd = [xd[ii] for ii in reorder]
    yd = [yd[ii] for ii in reorder]

    # make the scatter plot
    plt.scatter(xd, yd, s=30, alpha=0.15, marker='o')

    # determine best fit line
    par = np.polyfit(xd, yd, 1, full=True)

    slope = par[0][0]
    intercept = par[0][1]
    xl = [min(xd), max(xd)]
    yl = [slope * xx + intercept for xx in xl]

    # coefficient of determination, plot text
    variance = np.var(yd)
    residuals = np.var([(slope * xx + intercept - yy)
                        for xx, yy in zip(xd, yd)])
    Rsqr = np.round(1 - residuals / variance, decimals=2)
    if R is True:
        plt.text(.9 * max(xd) + .1 * min(xd), .9 * max(yd) +
                 .1 * min(yd), '$R^2 = %0.2f$' % Rsqr, fontsize=30)
    if shows is True:
        print(slope)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    yerr = [abs(slope * xx + intercept - yy) for xx, yy in zip(xd, yd)]
    par = np.polyfit(xd, yerr, 2, full=True)

    if err is True:

        yerrUpper = [(xx * slope + intercept) +
                     (par[0][0] * xx**2 + par[0][1] * xx + par[0][2])
                     for xx, yy in zip(xd, yd)]
        yerrLower = [(xx * slope + intercept) -
                     (par[0][0] * xx**2 + par[0][1] * xx + par[0][2])
                     for xx, yy in zip(xd, yd)]
        plt.plot(xd, yerrLower, '--r')
        plt.plot(xd, yerrUpper, '--r')

    plt.plot(xl, yl, '-r')
    if save != 0:
        plt.savefig(save)
    if show is True:
        plt.show()
    plt.clf()

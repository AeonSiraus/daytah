import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from daytah.Source.data_plot import *


class data:

    def __init__(self, csv_file=0, DataFrame=0):
        if csv_file is not 0:
            try:
                self.data = pd.read_csv(csv_file)
            except ImportError:
                print('File', csv_file, 'not found or invalid argument.')
        elif DataFrame is not 0:
            try:
                self.data = DataFrame
            except ImportError:
                print(DataFrame, 'not defined or invalid argument.')

    def calc(self, new_col_name, formula, rounding=-1):
        # check arguments
        if type(new_col_name) is not str:
            print('Invalid argument new_col_name :', new_col_name,
                  'Argument must be string!')
        elif rounding < -1:
            print('Invalid argument rounding:', rounding,
                  'Argument must be non-negative integer!')
        try:
            for row in self.data:
                value = formula
                if rounding is not -1:
                    col = [round(x, rounding) for x in value]
                else:
                    col = value
            result_col = pd.DataFrame({new_col_name: col})
            return result_col
        except ImportError:
            print('data.calc: No output, formula may be invalid')

    def calc_out(self, new_col_name, formula, rounding=-1):
        # check arguments
        if type(new_col_name) is not str:
            print('Invalid argument new_col_name :', new_col_name,
                  'Argument must be string!')
        elif rounding < -1:
            print('Invalid argument rounding:', rounding,
                  'Argument must be non-negative integer!')
        for row in self.data:
            value = formula
            if rounding is not -1:
                col = [round(x, rounding) for x in value]
            else:
                col = value
        self.data = pd.DataFrame({new_col_name: col})

    def appnd(self, to_append):
        outP = pd.concat([self.data, to_append], axis=1)
        return outP

    def write(self, output_file):
        self.data.to_csv(output_file)

    def calc_comb(self, new_col_name, formula, rounding=-1):
        calc = self.calc(new_col_name, formula, rounding)
        self.data = self.appnd(calc)

    def plot(self, x_axis,  y_axis, x_label=0, y_label=0,
             lbf=False, err=False, R=False, save=0, show=True, shows=True):
        if lbf is False:
            self.data.plot(x_axis, y_axis, kind='scatter')
            plt.show()
        else:
            plot_lbf(self.data, x_axis, y_axis, x_label=x_label,
                     y_label=y_label, err=err, R=R, save=save,
                     show=show, shows=shows)
            plt.show

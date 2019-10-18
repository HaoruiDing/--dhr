__author__ = 'dinghr'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.neutral = True
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.LOW, t.CLOSE, t.AMOUNT, t.VOLUME]  # ������Ҫ���ֶ�


    def factor_definition(self):
        s = time.time()
        needData = self.needData                                # ������������

        low = needData[t.LOW]
        close = needData[t.CLOSE]
        vwap = needData[t.AMOUNT] / needData[t.VOLUME]
        cl = (close + low) / 2
        hlret = self.calculator.Diff(x=cl, num=1) / self.calculator.Mean(x=cl, num=5)
        vwret = self.calculator.Diff(x=vwap, num=1) / self.calculator.Mean(x=vwap, num=5)
        val = hlret + vwret
        val[(hlret < 0) & (vwret > 0)] = hlret - vwret
        val[(hlret > 0) & (vwret < 0)] = - hlret + vwret
        val[(hlret < 0) & (vwret < 0)] = -1*val*3
        val[np.isinf(val)] = np.nan
        factor = self.calculator.Mean(x=val, num=5)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()
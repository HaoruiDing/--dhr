__author__ = 'dinghr'

import time

import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t

class Factor(FactorBase):

    def __init__(self):
        super(Factor,self).__init__()
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.CLOSE, t.VWAP]
        self.neutral=True
        # put remote conn here if need extra data

    def factor_definition(self):
        s = time.time()
        needData = self.needData

        close = needData[t.CLOSE]
        vwap = needData[t.VWAP]
        ret = close/vwap-1
        ret[ret<0]=2*ret

        factor = -self.calculator.Decaylinear(x=ret,d=5)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()
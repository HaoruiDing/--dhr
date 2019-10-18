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
        self.neutral = True
        self.needFields = [t.CLOSE, t.VWAP, t.PCTCHG]   # 设置需要的字段

    def factor_definition(self):
        s = time.time()
        needData = self.needData  # 计算所需数据

        ret = needData[t.PCTCHG]
        close = needData[t.CLOSE]
        vwap = needData[t.VWAP]

        factor1 = -self.calculator.cmpMax(x=(close / vwap) ,y= ret)
        factor = self.calculator.Decaylinear(x=factor1,d=5)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()
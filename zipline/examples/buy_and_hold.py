#encoding:utf-8
# Copyright 2015 Quantopian, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pandas as pd
from zipline import TradingAlgorithm
from zipline.api import order, sid,get_datetime
from zipline.data.loader import load_from_yahoo,load_data
from zipline.api import order_target, record, symbol, history,symbol,set_commission,order_percent,set_long_only,get_open_orders
from zipline.finance.commission import OrderCost
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False



# loading the data
input_data = load_data(
    stockList=['002057'],
    start="2015-11-04",
    end="2016-01-16"
)
def analyze(context=None, results=None):
    import matplotlib.pyplot as plt

    # Plot the portfolio and asset data.
    ax1 = plt.subplot(211)
    results.algorithm_period_return.plot(ax=ax1,color='blue',legend=u'策略收益')
    ax1.set_ylabel(u'收益')
    results.benchmark_period_return.plot(ax=ax1,color='red',legend=u'基准收益')

    # Show the plot.
    plt.gcf().set_size_inches(18, 8)
    plt.show()



def initialize(context):
    context.has_ordered = False
    set_commission(OrderCost(open_tax=0,close_tax=0.001,open_commission=0.0003,close_commission=0.0003,close_today_commission=0,min_commission=5))
    set_long_only()

def handle_data(context, data):

    #输出每天持仓情况

    if not context.has_ordered:
        for stock in data:
            #openprice=history(3, '1d', 'open')
            closeprice=history(5,'1d','close')
            #-2:昨天,-3 前天.-4 大前天
            print (get_datetime(),closeprice[sid(stock)][0],closeprice[sid(stock)][1],closeprice[sid(stock)][2],closeprice[sid(stock)][3],closeprice[sid(stock)][4])
            #print closeprice,closeprice[sid(stock)][1]
            if closeprice[sid(stock)][-2]>closeprice[sid(stock)][-3] and closeprice[sid(stock)][-3]>closeprice[sid(stock)][-4]:
                print ("buy",get_datetime())
                order(stock, 300)
            elif closeprice[sid(stock)][-2]<closeprice[sid(stock)][-3] and closeprice[sid(stock)][-3]<closeprice[sid(stock)][-4]:
                print ("sell",get_datetime())
                order(stock, -300)

# capital_base is the base value of capital
#
algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data,capital_base=10000,benchmark='399004')

#print input_data
#api: print all the api function
#print algo.all_api_methods()
results = algo.run(input_data)
print (results)
#print results['benchmark_period_return'],results['portfolio_value']
analyze(results=results)
#画k线蜡烛图 python_dataEE/plot/kline_candle.py

https://github.com/willowj/python_dataEE/blob/master/plot/kline_candle.py



#require modules: pyecharts,pandas,numpy





<<<<<<<<<<<<<example: jupyter-notbook

from pyecharts import Kline, Bar, Line, Grid, Overlap

import tushare as ts

df = ts.get_hist_data('hs300', ktype='5')

Kline_js('hs300_k-line-5min',df,ma=('ma10','ma20'),width=800, height=400,)

<<<<<<<<<<<<<<<<<





'''
params:
     name, df, prices_cols=None, ma=('ma10',), width=1600, height=750, kline_xaxis_pos='top', render_path=None

     name:    图例名称
     
     df:    columns包含 prices_cols以及‘volume’ 的pandas.DataFrame
     
     prices_cols :  默认 [u'open', u'close', u'low', u'high']
     
     width=1600, height=750 :   默认图片大小
     
     kline_xaxis_pos='top'： k-line图例默认在上方
     
     render_path：   render to html file path
     
'''


![image](https://github.com/willowj/python_dataEE/blob/master/plot/pyecharts_k-candle.png)

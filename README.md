# python_dataEE

画k线蜡烛图
plot/kline_candle.py
https://github.com/willowj/python_dataEE/blob/master/plot/kline_candle.py

#example: jupyter-notbook
import tushare as ts
df = ts.get_hist_data('hs300', ktype='5')
Kline_js('hs300_k-line-5min',df,ma=('ma10','ma20'),width=800, height=400,)


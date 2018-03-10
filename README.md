#画k线蜡烛图   

[ **python_dataEE/plot/kline_candle.py** ](https://github.com/willowj/python_dataEE/blob/master/plot/kline_candle.py)

> python: jupyter-notbook       #*建议使用jupyter-notbook*

```python
from kline_candle import Kline_js
import tushare as ts
df = ts.get_hist_data('hs300', ktype='5')
Kline_js('hs300_k-line-5min',
         df,
         ma=('ma10', 'ma20'),
         width=800, height=400,
         )
```

![image](https://github.com/willowj/python_dataEE/blob/master/plot/k_candle.gif)

params:

> name, df, prices_cols=None, ma=('ma10',), width=1600, height=750, kline_xaxis_pos='top', render_path=None

- name: *str*                               #图例名称 
- df:  *pandas.DataFrame*         #columns包含 prices_cols、‘volume’
- prices_cols : *list*                     #默认 [u'open', u'close', u'low', u'high']
- ma=('ma10',): *list or tuple*    #移动平均周期
- width=1600, height=750     # 默认图片大小
- kline_xaxis_pos='top'           #k-line图例默认在上方 
- render_path： *str*                 #html file path to save

https://github.com/willowj/python_dataEE/blob/master/plot/kline_candle.py

required modules : 

> pyecharts
> pandas
> tushare (for test)

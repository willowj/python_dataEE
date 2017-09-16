# -*- coding: utf-8 -*-
# 2017/09/16
# author : willow_j
# email : willow_j@foxmail.com

from __future__ import unicode_literals
from __future__ import print_function

from pyecharts import Kline, Bar, Line, Grid, Overlap


def kline_js(name, df, prices_cols=None, ma=('ma10',), width=1600, height=750, kline_xaxis_pos='top', render_path=None):
    '''
    params:
    name:    图例名称
    df:    columns包含 prices_cols以及‘volume’ 的pandas.DataFrame
    prices_cols :  默认 [u'open', u'close', u'low', u'high']
    width=1600, height=750 :   默认图片大小
    kline_xaxis_pos='top'： k-line图例默认在上方
    render_path：   render to html file path
    '''
    if not prices_cols:
        prices_cols = [u'open', u'close', u'low', u'high']

    if not set(prices_cols+['volume']) < set(df.columns):
        raise AttributeError("%s or 'volume' not in columns" %
                             str(prices_cols))

    df.sort_index(inplace=True)
    kline = Kline(name, width=width, height=height)
    kline.add('k-candle',
              df.index.format(),
              df[prices_cols].values.tolist(),
              is_datazoom_show=True,
              datazoom_xaxis_index=[0, 1],
              xaxis_pos=kline_xaxis_pos,
              is_xaxislabel_align=True,
              )

    # volume
    if not 'price_change' in df.columns:
        df['price_change'] = df[prices_cols[1]].diff()
    ups = df.where(df.price_change > 0, 0)['volume']
    downs = df.where(~(df.price_change > 0), 0)['volume']

    bar = Bar()
    bar.add('up',
            x_axis=ups.index.format(),
            y_axis=ups.values.tolist(),
            is_datazoom_show=True,
            legend_top="70%",
            is_stack=True,
            is_xaxislabel_align=True,
            )
    bar.add('down',
            x_axis=downs.index.format(),
            y_axis=downs.values.tolist(),
            is_datazoom_show=True,
            is_stack=True,
            legend_top="70%",
            legend_orient='vertical',
            legend_pos='left',
            yaxis_pos='right',
            is_xaxislabel_align=True,
            # mark_line=["average"],
            )

    # merge
    grid1 = Grid()
    grid1.add(kline, grid_bottom="18%")
    grid1.add(bar, grid_top="75%")

    # add ma
    Line_draw = False
    for ma_ in ma:
        if ma_ in df.columns:
            if Line_draw is False:
                Line_draw = True
                line = Line()
            line.add(ma_, df.index.format(), df[ma_].values.tolist())
    if Line_draw:
        overlap = Overlap()
        overlap.add(kline)  # overlap kline
        overlap.add(line)

    if render_path:
        grid1.render(render_path)
    return grid1  # .render('k-line.html')

if __name__ == '__main__':
    import tushare as ts
    
    name = 'hs300'
    period = '5'
    
    df = ts.get_hist_data(name, ktype=period)
    if period.isdigit():
        period += 'min'
        
    kline_js('%s_kline_%s' % (name, period), 
             df, 
             ma=['ma10', 'ma20'],
             render_path='%s_kline_%s.html' % (name, period)
        )

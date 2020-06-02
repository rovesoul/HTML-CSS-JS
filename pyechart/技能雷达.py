import pyecharts.options as opts
from pyecharts.charts import Radar
from pyecharts import options as opts
from pyecharts.charts import Graph, Page
from pyecharts.render import make_snapshot
 
from snapshot_phantomjs import snapshot

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=radar

目前无法实现的功能:

1、雷达图周围的图例的 textStyle 暂时无法设置背景颜色
"""
# v1计划目标，v2实际达成
"""
前端学了一套html，1/2套css，1/16套JS。
学了1/N的FLASK，
学了1/N的Django。
还学了1/N的JAVA。
还学了1/N的python tkinter模块。
"""
v1 = [[100, 100,100,100,100,100,100]]
v2 = [[80,  40  ,8,  12, 30, 5, 20]]


(
    Radar(init_opts=opts.InitOpts(width="1280px", height="720px", bg_color="white"))
    .set_colors(["red"])
    .add_schema(
        schema=[
            opts.RadarIndicatorItem(name="HTML语音", max_=100),
            opts.RadarIndicatorItem(name="CSS语言", max_=100),
            opts.RadarIndicatorItem(name="JavaScript语言", max_=100),
            opts.RadarIndicatorItem(name="FLASK模块", max_=100),
            opts.RadarIndicatorItem(name="Django模块", max_=100),
            opts.RadarIndicatorItem(name="Java语言", max_=100),
            opts.RadarIndicatorItem(name="python-tkinter模块", max_=100),
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="black",font_size=20),
    )
    .add(
        series_name="感觉要求程度",
        data=v1,
        linestyle_opts=opts.LineStyleOpts(color="green",width=2),
    )
    .add(
        series_name="实际学习程度",
        data=v2,
        linestyle_opts=opts.LineStyleOpts(color="red",width=2,),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="学习进度"), legend_opts=opts.LegendOpts()
    )
    .render("basic_radar_chart.html")
)


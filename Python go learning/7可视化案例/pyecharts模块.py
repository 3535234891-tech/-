#官方画廊 http://gallery.pyecharts.prg/#/README

# 利用pyecharts包去绘图
#
# 调包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(['中','英','美'])
# 添加y轴
line.add_yaxis('GDP',[30.20,10])

#全局配置set_global_opts()
line.set_global_opts(
    title_opts = TitleOpts(title='GDP展示',pos_left='center',pos_bottom='1%'),
    legend_opts = LegendOpts(is_show=True),
    toolbox_opts = ToolboxOpts(is_show=True),
    visualmap_opts = VisualMapOpts(is_show=True),
)
# render方法生成图像
line.render()
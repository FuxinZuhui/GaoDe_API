# GaoDe_API

调用高德API获取两个景点之间的距离信息。

- input：<景点，经度，纬度>的列表，命名为poi_list.csv放在根目录下
- output：获取景点之间的最短驾驶距离（m）、最短驾驶时间（s）、最少打车费用（CNY）及景点所属的区，输出为根目录下的geographic_info.data，格式为json串。

使用步骤：
- 在高德应用平台创建应用，参考https://zhuanlan.zhihu.com/p/343576260
- 在const.py中配置高德应用的key
- 运行main.py
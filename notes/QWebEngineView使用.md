主要是想学习下如何加载地图。

http://lbsyun.baidu.com/jsdemo.htm#a1_2

448E8EFFa04a4bee8327bf68241cd3b5 --AK

### 基础用法

**加载网上链接**

通过调用`viewName.load('http://xxx.com/xx')` 

这种调用需要加上协议名。

可以通过API获取界面直接显示，比如百度地图API显示地图。

**加载本地文件**

这个有个很重要的细节，很多文章里讲不到，就是加载本地HTML页面时，需要的是绝对路径。

```python
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ht.html"))
local_url = QUrl.fromLocalFile(file_path)
view.load( QUrl( local_url ))	
```
中文词云生成
===
* 通过调用Wordcloud和jieba这两个库实现中文词云。
* 想调用jieba库进行中文分词，再用Wordcloud生成词云。  
# 环境
* python3
* 安装Wordcloud库，```pip install wordcloud```或conda下```conda install -c conda-forge wordcloud```
* 安装jieba库,```pip install jieba```，这里我把jieba库下到项目里了。
# 使用
* imgs中是背景图片照片
![](http://github.com/mantuoluozk/chinese_wordcloud/raw/master/imgs/apple.png)
* 运行codes里的run1.py生成的词云颜色是依据据背景图片颜色生成的。
![](http://github.com/mantuoluozk/chinese_wordcloud/raw/master/imgs/示例1.png)
* 运行codes里的run2.py生成的词云颜色是随机生成的。
![](http://github.com/mantuoluozk/chinese_wordcloud/raw/master/imgs/示例2.png)
# Wordcloud库和jieba库地址
* ![jieba中文分词](https://github.com/fxsjy/jieba)
* ![wordcloud](https://github.com/amueller/word_cloud)

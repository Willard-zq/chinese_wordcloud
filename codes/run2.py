# -*- coding: utf-8 -*-

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from os import path
import jieba
import random

# 文本路径名
text_path = 'txt/apple.txt' 

# 中文字体路径名
font_path = 'txt/Hiragino.ttf' 

# 背景图片路径名
img_mask = 'imgs/apple.png'

# 保存的图片名字
img_result = 'result1.png' 

# 获取当前文件路径
p = path.dirname('.')

# 打开文本
text = open(path.join(p, text_path),'r', encoding='UTF-8').read()

# 中文分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 颜色函数
def random_color(word, font_size, position, orientation, font_path, random_state):
	s = 'hsl(0, %d%%, %d%%)' % (random.randint(0, 100), random.randint(0, 100))
	print(s)
	return s

# 生成对象
mask = np.array(Image.open(img_mask))
wc = WordCloud(mask=mask, font_path=font_path, mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

# 保存到文件
wc.to_file(path.join(p, img_result))
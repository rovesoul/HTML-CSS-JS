import random

xing="王   李 张 刘 陈 杨 黄 赵 吴 周 徐 孙 马 朱 胡 郭 何姚 卢 姜 崔 钟 谭 陆 汪 范 金 石 廖 贾 夏 韦 傅 方 白 邹 孟 熊 秦 邱 江 尹 高 林 罗 郑 梁 谢 宋 唐 许 韩 冯 邓 曹 彭 曾 萧 田 董 潘 袁 于 蒋 蔡 余 杜 叶 程 苏 魏 吕 丁 任 沈"
ming="风雅颂灵云糖"

xing=xing.replace(' ','')
ming=ming.replace(' ','')
if __name__=="__main__":
    n=input('输出多少个')
    for i in range(int(n)):
        a=random.choice(xing)
        c=random.randint(1,2)
        b=random.sample(ming,c)
        print(a+''.join(b))
import pymysql
import re

args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

#获取要插入的数据
def get_data(filename):
    """
    :param filename: 单词文本
    :return:可插入数据
    """
    data=[]
    file=open(filename)
    for line in file:
        word=re.findall(r"(\w+)\s+(.*)",line)
        data.append(word[0])
    file.close()
    return data

def main():
    #连接数据库
    db=pymysql.connect(**args)
    cur=db.cursor()
    #调用get_data获取数据
    data=get_data("dict.txt")
    #数据写操作 insert delete update
    try:
        sql="insert into words(word,mean) values(%s,%s);"
        cur.executemany(sql,data)
        db.commit()#统一提交写操作
    except:
        db.rollback()
    #关闭数据库连接
    cur.close()
    db.close()

if __name__ == '__main__':
    main()

# args = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "123456",
#     "database": "dict",
#     "charset": "utf8"
# }
#
#
# # 获取我要插入的数据
# def get_data(filename):
#     """
#     :param filename: 单词本文件
#     :return: 可插入数据
#     """
#     data = []  # 装单词 [(word,mean),()....]
#     file = open(filename)
#     for line in file:
#         word = re.findall(r"(\w+)\s+(.*)", line)
#         data.append(word[0])
#     file.close()
#     return data  # 要插入的单词
#
#
# def main():
#     # 连接数据库
#     db = pymysql.connect(**args)
#     cur = db.cursor()
#     # 调用get_data获取数据
#     data = get_data("dict.txt")
#     try:
#         sql = "insert into words (word,mean) values (%s,%s);"
#         cur.executemany(sql, data)
#         db.commit()
#     except:
#         db.rollback()
#
#     # 关闭数据库连接
#     cur.close()
#     db.close()
#
#
# if __name__ == '__main__':
#     main()
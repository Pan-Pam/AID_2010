import pymysql
n=input("请输入学生姓名")
args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"c_j",
    "charset":"utf8"
}

#连接数据库
db=pymysql.connect(**args)

#创建游标 游标对象:执行sql得到执行结果的对象
cur=db.cursor()

#数据写操作 insert delete update
try:
    name = input("Name:")
    sql="update cls set score=100 where name='%s';"%name
    #sql2="update cls set score=100 where id=%s;"%id

    cur.execute(sql)

    db.commit()#统一提交写操作
except Exception as e:
    print(e)
    db.rollback()

#关闭数据库连接
cur.close()
db.close()

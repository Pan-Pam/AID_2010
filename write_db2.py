import pymysql

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

#数据批量写操作 insert delete update
stu_list=[
    ("张三",23,'m',99),
    ("李四",21,'w',90),
    ("王五",20,'m',86),
    ("赵柳",19,'w',80)
]
try:
    sql="insert into cls(name,age,sex,score) values(%s,%s,%s,%s);"
    #sql2="update cls set score=105 where id=2;"
    cur.executemany(sql,stu_list)
    #cur.execute(sql2)
    db.commit()#统一提交写操作
except Exception as e:
    print(e)
    db.rollback()

#关闭数据库连接
cur.close()
db.close()
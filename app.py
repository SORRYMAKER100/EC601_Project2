from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
import uuid
# import requests
# import pymysql

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="006123",
#     database="new_schema",
# )
# db = pymysql.connect(host="localhost",
#                        user="root",
#                        passwd="mysql94201",
#                        database="test", charset='utf8')

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="mysql94201",
  database="project"
)
# 创建Flask对象app并初始化
cursor = db.cursor()
app = Flask(__name__)
app.config["SECRET_KEY"] = "JQ"

@app.route("/", methods=["GET", "POST"])

def index():
    return render_template("shouye.html")


@app.route("/search.html", methods=["GET", "POST"])
def root1():
    return render_template("search.html",stuid=session.get("sid"))


@app.route("/index.html", methods=["GET", "POST"])
def root2():
        # return render_template("index.html")
    if session.get("sid") == 0:
        return {'message': "error!"}
    else:
        sql = "select * from employee where stu_no ='%s' " %(session.get("sid"))
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        name = result[1]
        photo = result[3]
        qq = result[6]
        number = result[7]


        return render_template( "index.html",stuid=session.get("sid"),name = name, photo = photo, qq = qq, number = number)



@app.route("/category.html", methods=["GET", "POST"])
def root3():
    return render_template("category.html",stuid=session.get("sid"))


@app.route("/testimonials.html", methods=["GET", "POST"])
def root4():
    return render_template("testimonials.html",stuid=session.get("sid"))


@app.route("/portfolio.html", methods=["GET", "POST"])
def root5():
    return render_template("portfolio.html",stuid=session.get("sid"))


@app.route("/contact.html", methods=["GET", "POST"])
def root6():
    return render_template("contact.html",stuid=session.get("sid"))


@app.route("/searching.html", methods=["GET", "POST"])
def root7():
    return render_template("searching.html",stuid=session.get("sid"))


@app.route("/11.html", methods=["GET", "POST"])
def root8():
    if request.method == "POST":
        localid = request.form.get("localid")
    try:
        sql = "SELECT  test.activity.idActivity, test.activity.typeActivity,test.activity.descripitionActivity,test.relationship.idUser FROM test.activity,test.relationship WHERE test.relationship.idActivity in (select test.relationship.idActivity from test.relationship where test.relationship.statusUser = 2 and test.relationship.idUser='%s')  and test.relationship.statusUser=0"%(localid)
        cursor.execute(sql)
        u = cursor.fetchall()
    except:
        db.rollback()
        return {'message': "error!"}
    return render_template('11.html', u=u)


@app.route("/OBDC3", methods=["GET", "POST"])
def obdc3():
    if request.method == 'GET':
        print(8099)
        return render_template('OBDC3.html', jieguo=z)
    else:
        print("ttb")
        search_item = request.form.get('search_AC')
        a_id = request.form.get('a_id')
        stu_no = request.form.get('stu_no')
        print(a_id)
        sql = "SELECT idActivity,typeActivity,maxnumActivity,minnumActivity,startdateActivity,finishdateActivity,destinationActivity,nownumActivity,isfullActivity from activity where typeActivity LIKE '%%%s%%' or startdateActivity Like '%%%s%%' or destination Like '%%%s%%'" % (
            search_item, search_item, search_item)
        sql5 = "SELECT idActivity,maxnumActivity,nownumActivity,isfullActivity from activity where idActivity ='%s'" % (a_id)

        sql2 = 'insert into relationship(a_id,stu_id,r_id) values(%s,%s,%s)'
        sql3 = " Update activity set nownumActivity = nownumActivity+1 where idActivity ='%s'" % (a_id)
        sql4 = " Update activity set isfullActivity = 1 where a_id ='%s'" % (a_id)
        sql6 = "SELECT r_id from relationship where a_id ='%s'" % (a_id)
        if a_id is None:

            try:
                # 执行SQL语句
                cursor.execute(sql)
                print(sql)
                # 获取所有记录列表
                result = cursor.fetchall()
                print(result)
                print(908)
                return render_template('OBDC3.html', jieguo=result)
            except:
                print(3344)
                db.rollback()
        else:
            print(99999)
            try:
                # 执行SQL语句

                cursor.execute(sql6)
                # print("now?")
                result = cursor.fetchall()
                print("now?")
                print(result)
                if len(result)==0:
                    cursor.execute(sql2, (a_id, stu_no, a_id + stu_no))
                    print("fUCK")
                    return {"message": 'success'}
                # print(result[0][0])
                # print(int(a_id + stu_no))
                if result[0][0] == a_id + stu_no:
                    print(333333)
                    return {"message": 'already'}
                cursor.execute(sql5)
                result = cursor.fetchall()
                print(result[0][3])
                if result[0][3] != 1:
                    print('uuuu')
                    cursor.execute(sql2, (a_id, stu_no, a_id + stu_no))
                    print('dog')
                    cursor.execute(sql3)
                    print(5555)
                    cursor.execute(sql4)
                    # 获取所有记录列表
                    db.commit()
                    return {"message": 'success'}
                else:
                    return {"message": 'full'}
            except:
                db.rollback()




@app.route("/indexing", methods=["GET","POST"])
def indexing():


        # 如果获取的数据为空
    if session.get("sid") == 0:
        return {'message': "error!"}
    else:
        sql = "select * from employee where stu_no ='%s' " %(session.get("sid"))
        cursor.execute(sql)
        result = cursor.fetchone()
        photo = result[3]
        qq = result[6]
        number = result[7]

        # if isinstance(photo, bytes):
        #     photo = str(photo,encoding= 'utf-8')
        #
        # if isinstance(qq, bytes):
        #     qq = str(qq,encoding= 'utf-8')
        #
        # if isinstance(number, bytes):
        #     number = str(number,encoding= 'utf-8')
        print(qq)
        print(number)
        # return {'message': "success!", 'stuno': session.get("sid"), 'photo': photo, 'qq': qq, 'number': number}
        return render_template( "index.html",stuid=session.get("sid"),photo = photo, qq = qq, number = number)


# app的路由地址"/submit"即为ajax中定义的url地址，采用POST、GET方法均可提交
# @app.route("/submit", methods=["GET", "POST"])
# # 从这里定义具体的函数 返回值均为json格式
# def submit():
#     # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
#     if request.method == "POST":
#         name = request.form.get("name")
#     if request.method == "GET":
#         name = request.args.get("name")
#
#     # 如果获取的数据为空
#     if len(name) == 0:
#         return {'message': "error!"}
#     else:
#         # SQL 查询语句
#         sql = "SELECT password FROM EMPLOYEE WHERE stu_id='%s'" % (name)
#         try:
#             # 执行SQL语句
#             cursor.execute(sql)
#             # 获取所有记录列表
#             result = cursor.fetchone()
#             income = result[0]
#             print(income)
#         except:
#             db.rollback()
#             return {'message': "error!"}
#         return {'message': "success!", 'name': name, 'income': income}


@app.route("/create", methods=["GET", "POST"])
# 从这里定义具体的函数 返回值均为json格式
def create():
    # 由于POST、GET获取数据的方式不同，需要使用if语句进行判断
    if request.method == "POST":
        type = request.form.get("type1")
        min = request.form.get("minnumActivity")
        max = request.form.get("maxnumActivity")
        start = request.form.get("startdateActivity")
        end = request.form.get("finishdateActivity")
        ddl = request.form.get("ddlActivity")
        destination = request.form.get("destinationActivity")
        description = request.form.get("descripitionActivity")
        # min=int(min)
        # max=int(max)
        print("Min: ", min)
        print("Max: ", max)
    if request.method == "GET":
        type = request.args.get("type1")
    if start >= end:
        return {'message': "startime must be earlier than endtime"}
    if ddl >= start:
        return {'message': "Join DDL must be earlier than start time"}

    # 如果获取的数据为空
    if type == None:
        return {'message': "slect one type"}
    else:
        # SQL 查询语句
        as2 = uuid.uuid4()
        sql = "insert into Project.activity values('%s','%s','%d','%d','%s','%s','%s','%s','%s','%d','%d','%d')" % (
            as2, type, int(min), int(max), start, end, destination, description, ddl, 0, 0, 1)
        # 这里还差一个，创建成功的话，在relationship里面加一个关系,同时更新活动列表的nownum
        # sql1 = "insert into Project.relationgship(idUser,idActivity,statusUser) values ('s','s','d') %( ,as2,1)"
        # sql1 = "insert into Project.relationgship(stu_id,a_id,state) values ('s','s','d') %(,as2,1)"

        print(sql)
        # print(x)
        try:
            # 执行SQL语句
            cursor.execute(sql)

            # cursor.execute(sql1)
            # 获取所有记录列表
            db.commit()
        except:
            db.rollback()
            return {'message': "error!"}
        return {'message': "create success!", 'id': as2}


@app.route("/ac_info", methods=["GET", "POST"])
def acinfo():
    global y
    if request.method == 'GET':
        print(8956)
        return render_template('ac_info.html', jieguo=y)

    else:
        print("rroo")
        a_id = request.form.get('a_id')
        sql = "SELECT a_id,type,max,min,start_time,end_time,place,cur_num,introduce from activity where a_id = '%s'" % (
            a_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            print(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            print(12321)
            if len(result) == 0:
                return {'message': 'fail'}
            else:
                print(908777)
                y = result
                return render_template('ac_info.html', jieguo=result)
        except:
            db.rollback()


@app.route("/dele", methods=["GET", "POST"])
def dele():
    if request.method == 'GET':
        print(788)
        return render_template('manager.html')
    else:
        print("rr7")
        dele = request.form.get('dele')

        sql = "Update relationship set state = -1 where a_id ='%s'" % (dele)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            db.commit()
            print(sql)
            # 获取所有记录列表
        except:
            db.rollback()

        return render_template('manager.html', jieguo=z)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/searchuser', methods=['GET', 'POST'])
def search_User():
    global x
    if request.method == 'GET':
        return render_template('searching.html',stuid=session.get("sid"))
    else:
        search_User = request.form.get('search_User')

        sql = "SELECT stu_no,user,photo from employee where stu_no LIKE '%%%s%%' or user Like '%%%s%%'" % (
            search_User, search_User)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
        except:
            db.rollback()
            result = ''
        if len(result) == 0:
            return {'message': 'fail'}
        else:
            print(908)
            x = result
            return render_template('OBDC.html', jieguo=result)


@app.route('/search_AC', methods=['GET', 'POST'])
def search_AC():
    global z
    if request.method == 'GET':
        print("qfr")
        return render_template('searching.html',stuid=session.get("sid"))
    else:
        print("ttbrer")
        search_AC = request.form.get('search_AC')

        # sql = "SELECT a_id,type,max,min,start_time,end_time,place,cur_num from activity where type LIKE '%%%s%%' or start_time Like '%%%s%%' or place Like '%%%s%%'" % (search_item,search_item,search_item)
        sql = "SELECT idActivity ,typeActivity,maxnumActivity ,minnumActivity,startdateActivity,finishdateActivity,destinationActivity,nownumActivity from activity where typeActivity LIKE '%%%s%%' or startdateActivity Like '%%%s%%' or destinationActivity Like '%%%s%%'" % (
            search_AC, search_AC, search_AC)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            print(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            print()
        except:
            print('fucccck')
            db.rollback()
            result = ''
        if len(result) == 0:
            return {'message': 'fail'}
        else:
            print(908)
            z = result
            return render_template('OBDC3.html', jieguo=result)


@app.route('/submit1', methods=['GET', 'POST'])
def submit1():
    if request.method == "GET":
        stu_id = request.args.get('stu_id')
        user = request.args.get('user')
        password = request.args.get('password')
        password1 = request.args.get('password1')
        photo = request.args.get('pic')
        qq = request.args.get('qq')
        number = request.args.get('phone_number')
    if request.method == "POST":
        stu_id = request.form.get('stu_id')
        user = request.form.get('user')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        photo = request.form.get('pic')
        qq = request.form.get('qq')
        number = request.form.get('phone_number')
        print(stu_id)

    if password1 != password:
        return {'message': "success"}
    else:
        sql = "select * from employee where STU_NO = '%s'" % (stu_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
        except:
            db.rollback()
            result = ''
        if len(result) != 0:
            return {'message': 'fail'}
        else:
            sql = 'insert into employee(stu_no,user,password,photo,qq,number) values(%s,%s,%s,%s,%s,%s)'
            try:
                # 执行SQL语句
                cursor.execute(sql, (stu_id, user, password, photo, qq, number))
                # 提交到数据库执行
                db.commit()
            except:
                # 发生错误时回滚
                print("fuck")
                db.rollback()
            print("bad")
            return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        stu_id = request.form.get('stu_id')
        password = request.form.get('password')
        sql = "select * from employee where STU_NO = '%s'" % (stu_id)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
        except:
            db.rollback()
            result = ''

        if len(result) != 0:
            if result[0][2] != password:
                return {'message': 'fail'}
            elif result[0][4] == '1':
                return {'message': 'manager'}
            else:
                session["sid"] = stu_id
                print(session.get("sid"))
                return {'message': 'good'}
        else:
            session["sid"] = stu_id
            return {'message': 'success'}


# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     global x
#     if request.method == 'GET':
#         print("qfr")
#         return render_template('search.html')
#     else:
#         print("ttb")
#         search_item = request.form.get('search_item')
#
#         sql = "SELECT stu_no,user,photo from employee where stu_no LIKE '%%%s%%' or user Like '%%%s%%'" % (search_item,search_item)
#
#         try:
#             # 执行SQL语句
#             cursor.execute(sql)
#             # 获取所有记录列表
#             result = cursor.fetchall()
#
#         except:
#             db.rollback()
#             result = ''
#         if len(result) == 0:
#            return {'message': 'fail'}
#         else:
#             print(908)
#             x = result
#             return render_template('OBDC.html', jieguo = result)


@app.route("/OBDC", methods=["GET", "POST"])
def obdc():
    if request.method == 'GET':
        print(x)
        print(8099)
        return render_template('OBDC.html', jieguo=x)
    else:
        print("ttb")
        search_item = request.form.get('search_item')

        sql = "SELECT stu_no,user,photo from employee where stu_no LIKE '%%%s%%' or user Like '%%%s%%'" % (
            search_item, search_item)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            print(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            print(908)
            return render_template('OBDC.html', jieguo=result)
        except:
            db.rollback()


@app.route("/a_info", methods=["GET", "POST"])
def ainfo():
    global y
    if request.method == 'GET':
        print(8956)
        return render_template('a_info.html', jieguo=y)

    else:
        print("rroo")
        info = request.form.get('a_info')
        print(info)
        sql = "SELECT stu_no,user,photo from employee where STU_NO = '%s'" % (info)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            print(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            print(12321)
            if len(result) == 0:
                return {'message': 'fail'}
            else:
                print(908777)
                y = result
                return render_template('a_info.html', jieguo=result)
        except:
            db.rollback()


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    global z
    if request.method == 'GET':
        sql = "select * from activity join relationship on activity.a_id = relationship.a_id where relationship.state = 0"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            z = result
        except:
            db.rollback()

        if len(result) == 0:
            return {'message': 'fail'}
        else:
            return render_template('manager.html', jieguo=result)
    else:
        sql = "select * from activity join relationship on activity.a_id = relationship.a_id where relationship.ok = 0"
        try:
            cursor.execute(sql)
            print(sql)
            result = cursor.fetchall()
        except:
            db.rollback()

        if len(result) == 0:
            return {'message': 'fail'}
        else:
            print(908777)
            return render_template('manager.html', jieguo=result)


@app.route("/pas", methods=["GET", "POST"])
def pas():
    if request.method == 'GET':
        print(788)
        return render_template('manager.html')
    else:
        print("rr7")
        pas = request.form.get('pas')

        sql = "Update relationship set state = 1 where a_id ='%s'" % (pas)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            db.commit()
            # 获取所有记录列表
        except:
            db.rollback()

        return render_template('manager.html', jieguo=z)


@app.route('/search2', methods=['GET', 'POST'])
def search2():
    global x
    if request.method == 'GET':
        print("qfr")
        return render_template('search2.html')
    else:
        print("ttb")
        search_item = request.form.get('search_item')

        sql = "SELECT stu_no,user,photo from employee where stu_no LIKE '%%%s%%' or user Like '%%%s%%'" % (
            search_item, search_item)

        try:
            # 执行SQL语句
            cursor.execute(sql)
            print(sql)
            # 获取所有记录列表
            result = cursor.fetchall()
            print(result)

        except:
            db.rollback()
            result = ''
        if len(result) == 0:
            return {'message': 'fail'}
        else:
            print(908)
            x = result
            return render_template('OBDC2.html', jieguo=result)


@app.route("/OBDC2", methods=["GET", "POST"])
def obdc2():
    if request.method == 'GET':
        print(8099)
        return render_template('OBDC2.html', jieguo=x)
    else:
        print("ttb")
        search_item = request.form.get('search_item')
        obdc2 = request.form.get('obdc2')
        print(search_item)
        sql = "SELECT stu_no,user,photo from employee where stu_no LIKE '%%%s%%' or user Like '%%%s%%'" % (
            search_item, search_item)
        sql2 = "Update employee set ok = 0 where stu_no ='%s'" % (obdc2)
        print(2222)
        if obdc2 is None:
            try:
                # 执行SQL语句
                cursor.execute(sql)
                print(sql)
                # 获取所有记录列表
                result = cursor.fetchall()
                return render_template('OBDC2.html', jieguo=result)
            except:
                db.rollback()
        else:
            try:
                # 执行SQL语句
                cursor.execute(sql2)
                print(sql2)
                # 获取所有记录列表
                db.commit()
            except:
                db.rollback()


@app.route("/shenhe", methods=["GET", "POST"])
# 从这里定义具体的函数 返回值均为json格式
def shenhe():
    if request.method == "POST":
        userid = request.form.get("user")
        activity = request.form.get("activity")
        print(userid)
    print(111)
    try:
     sql = "UPDATE  test.relationship SET test.relationship.status=1 WHERE test.relationship.idActivity ='%s' and test.relationship.idUser='%s'" % (
        activity, userid)
     cursor.execute(sql)
     sql1="UPDATE test.ac "
     cursor.execute(sql1)
    except:
        db.rollback()
        return {'message': "error!"}
    return {'message': "update success!"}

# 定义app在8080端口运行
app.run(port=8080)

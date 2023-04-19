import functools
from flask import *
from src.dbconnectionnew import *

app = Flask(__name__)
app.secret_key="1234"


def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "lid" not in session:
            return render_template('loginindex.html')
        return func()

    return secure_function


@app.route('/logout')
def logout():
    session.clear()
    return render_template('loginindex.html')

@app.route('/')
def login():
    return render_template("loginindex.html")


@app.route('/logincode',methods=['post'])
def login_code():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
        return '''<script>alert("invalid");window.location='/'</script>'''
    elif res['Type']=='agriculture officer':

        session['lid'] = res['id']
        return redirect('/ag_home')

    elif res['Type']=='expert':
        session['lid']=res['id']
        return redirect('/expert_homepage')
    elif res['Type']=='farmer':
        session['lid'] = res['id']
        return redirect('/farmer_home')

    else:
        return '''<script>alert(" invalid ");window.location='/complaints'</script>'''

@app.route('/register')
def register():
    return render_template("regindex.html")


@app.route('/register1',methods=['post'])
def register1():
    fname = request.form['textfield']
    lname = request.form['textfield2']
    age = request.form['textfield3']
    place = request.form['textfield4']
    pin= request.form['textfield5']
    phoneno = request.form['textfield6']
    username = request.form['textfield7']
    password = request.form['textfield8']
    qry="insert into login values(null,%s,%s,'pending')"
    val=(username,password)
    id=iud(qry,val)
    qry="insert into farmer values(null,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,place,age,pin,phoneno)
    iud(qry,val)
    return '''<script>alert(" registered successully");window.location='/'</script>'''





@app.route('/ag_home')
def ag_home():
    return render_template("Agriculture Officer/aoindex.html")


@app.route('/add_crop',methods=['post','get'])
@login_required
def add_crop():
    return render_template("Agriculture Officer/Add Crop.html")


@app.route('/add_expert',methods=['post','get'])
@login_required
def add_expert():
    return render_template("Agriculture Officer/Add Experts.html")


@app.route('/add_notification')
@login_required
def add_notification():
    qry="SELECT * FROM notification WHERE l_id=%s"
    res=selectall2(qry,session['lid'])
    return render_template("Agriculture Officer/Add Notification.html",val=res)


@app.route('/manage_crop')
@login_required
def manage_crop():
    qry="select * from crop"
    res=selectall(qry)
    return render_template("Agriculture Officer/Manage Crop.html",val=res)

@app.route('/delete_crop')
@login_required
def delete_crop():
    id=request.args.get('id')
    qry="delete FROM crop WHERE c_id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully deleted");window.location='/manage_crop'</script>'''


@app.route('/edit_crop')
@login_required
def edit_crop():
    id=request.args.get('id')
    qry="select * FROM crop WHERE c_id=%s"
    res=selectone(qry,id)
    session['cid']=id
    return render_template("Agriculture Officer/Edit crop.html",val=res)

@app.route('/update_crop',methods=['post'])
@login_required
def update_crop():
    crop=request.form['textfield']
    description=request.form['textfield2']
    cid=session['cid']
    qry="UPDATE `crop` SET `crop_name`=%s,`description`=%s WHERE c_id=%s"
    val=(crop,description,cid)
    iud(qry,val)
    return '''<script>alert(" Successfully edited");window.location='/manage_crop'</script>'''




@app.route('/manage_expert')
@login_required
def manage_expert():
    qry="SELECT * from expert"
    res=selectall(qry)
    return render_template("Agriculture Officer/Manage Expert.html",val=res)

@app.route('/delete_expert')
@login_required
def delete_expert():
    id=request.args.get('id')
    qry="delete FROM expert WHERE ex_id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully deleted");window.location='/manage_expert'</script>'''

@app.route('/edit_expert')
@login_required
def edit_expert():
    id=request.args.get('id')
    qry="select * FROM expert WHERE ex_id=%s"
    res=selectone(qry,id)
    session['exid']=id
    return render_template("Agriculture Officer/Edit expert.html",val=res)

@app.route('/update_expert',methods=['post'])
@login_required
def update_expert():
    Fname=request.form['textfield']
    Lname=request.form['textfield2']
    Age = request.form['textfield3']
    Place = request.form['textfield4']
    Pin = request.form['textfield5']
    Phoneno = request.form['textfield6']

    exid=session['exid']
    qry="UPDATE `expert` SET `First_name`=%s,`Last_name`=%s,`Phone_no`=%s,`Place`=%s,`Age`=%s,`Pin`=%s WHERE ex_id=%s"
    val=(Fname,Lname,Phoneno,Place,Age,Pin,exid)
    iud(qry,val)
    return '''<script>alert(" Successfully edited");window.location='/manage_expert'</script>'''




@app.route('/send_notification',methods=['get','post'])
@login_required
def send_notification():
    return render_template("Agriculture Officer/Send Notifications.html")

@app.route('/delete_notification')
@login_required
def delete_notification():
    id=request.args.get('id')
    qry="delete FROM notification WHERE N_id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully deleted");window.location='/add_notification#about-us'</script>'''



@app.route('/verify_farmer')
@login_required
def verify_farmer():
    qry="SELECT * FROM `farmer` JOIN `login` ON `login`.`id`=`farmer`.`l_id` "
    res=selectall(qry)
    return render_template("Agriculture Officer/Verify Farmer.html",val=res)

@app.route('/accept_farmer')
@login_required
def accept_farmer():
    id = request.args.get('id')
    qry="UPDATE `login` SET `Type`='farmer' WHERE id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully accepted");window.location='/verify_farmer#about-us'</script>'''




@app.route('/reject_farmer')
@login_required
def reject_farmer():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `Type`='reject' WHERE id=%s"
    iud(qry, id)
    return '''<script>alert(" Successfully rejected");window.location='/verify_farmer#about-us'</script>'''



@app.route('/view_feedback')
@login_required
def view_feedback():
    qry ="SELECT farmer.First_name,farmer.Last_name,feedback.* FROM farmer JOIN feedback ON farmer.l_id=feedback.l_id"
    res =selectall(qry)
    return render_template("Agriculture Officer/View Feedback.html",val=res)


@app.route('/view_registered_users')
@login_required
def view_registered_users():
    qry = "select * from farmer"
    res = selectall(qry)
    return render_template("Agriculture Officer/View Registered Users.html",val=res)


@app.route('/expert_homepage')
def expert_homepage():
    return render_template("Expert/exindex.html")


@app.route('/add_fertilizer')
@login_required
def add_fertilizer():
    return render_template("Expert/Add Fertilizer.html")


@app.route('/add_tips')
@login_required
def add_tips():
    return render_template("Expert/Add Tips.html")


@app.route('/complaints')
@login_required
def complaints():
    qry="SELECT farmer.First_name,farmer.Last_name,complaint.* FROM farmer JOIN `complaint` ON farmer.l_id=complaint.F_id WHERE ex_id=%s"
    res=selectall2(qry,session['lid'])
    return render_template("Expert/Complaints.html",val=res)


@app.route('/doubt')
@login_required
def doubt():
    qry=" SELECT farmer.First_name,farmer.Last_name,doubt.* FROM farmer JOIN doubt ON farmer.l_id=doubt.F_id WHERE ex_id=%s"
    res = selectall2(qry, session['lid'])
    return render_template("Expert/Doubt.html",val=res)


@app.route('/manage_fertilizer')
@login_required
def manage_fertilizer():
    qry="select * from fertilizer"
    res=selectall(qry)
    return render_template("Expert/Manage Fertilizer.html",val=res)

@app.route('/delete_fertilizer')
@login_required
def delete_fertilizer():
    id=request.args.get('id')
    qry="delete FROM fertilizer WHERE Fert_id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully deleted");window.location='/manage_tips#about-us'</script>'''

@app.route('/edit_fertilizer')
@login_required
def edit_fertilizer():
    id=request.args.get('id')
    qry="select *   FROM fertilizer WHERE Fert_id=%s"
    res=selectone(qry,id)
    session['fertid']=id
    return render_template("Expert/Edit Fertilizer.html",val=res)



@app.route('/update_Fertilizer',methods=['post'])
@login_required
def update_Fertilizer():
    Fertname=request.form['textfield']
    description=request.form['textfield2']
    fertid=session['fertid']
    qry="UPDATE `fertilizer` SET `Fertilizer name`=%s,`Description`=%s WHERE Fert_id=%s"
    val=(Fertname,description,fertid)
    iud(qry,val)
    return '''<script>alert(" Successfully edited");window.location='/manage_fertilizer'</script>'''


@app.route('/manage_tips')
@login_required
def manage_tips():
    q="select * from tips"
    v=selectall(q)
    return render_template("Expert/Manage Tips.html",v=v)


@app.route('/delete_tip')
@login_required
def delete_tip():
    id=request.args.get('id')
    qry="delete FROM tips WHERE Tip_id=%s"
    iud(qry,id)
    return '''<script>alert(" Successfully deleted");window.location='/manage_tips#about-us'</script>'''


@app.route('/notification1')
@login_required
def notification1():
    qry="SELECT * from Notification"
    res=selectall(qry)
    return render_template("Expert/Notification.html",val=res)


@app.route('/farmer_home')
def farmer_home():
    return render_template("Farmer/faindex.html")


@app.route('/complaints1')
@login_required
def complaints1():
    qry="SELECT `complaint`.*,`expert`.`First_name`,`Last_name` FROM `expert` JOIN `complaint` ON `complaint`.`ex_id`=`expert`.`l_id` WHERE `complaint`.`F_id`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("Farmer/Complaints.html",val=res)


@app.route('/doubts1')
@login_required
def doubts1():
    qry="SELECT `doubt`.*,`expert`.`First_name`,`Last_name` FROM `expert` JOIN `doubt` ON `doubt`.ex_id=`expert`.`l_id` WHERE `doubt`.F_id=%s"
    res=selectall2(qry,session['lid'])
    return render_template("Farmer/Doubts.html",val=res)


@app.route('/feedback')
@login_required
def feedback():
    qry = "SELECT * from feedback"
    res = selectall(qry)

    return render_template("Farmer/Feedback.html",val=res)


@app.route('/pest_prediction')
@login_required
def pest_prediction():
    return render_template("Farmer/Pest Prediction.html")


@app.route('/send_complaints',methods=['post'])
@login_required
def send_complaints():
    q="SELECT * FROM `expert`"
    res=selectall(q)
    return render_template("Farmer/send Complaints.html",val=res)


@app.route('/send_complaints1',methods=['post'])
@login_required
def send_complaints1():
    comp=request.form['textfield2']
    eid=request.form['select']
    q="INSERT INTO `complaint`   VALUES(NULL,%s,%s,%s,'pending',CURDATE())"
    val=(session['lid'],eid,comp)
    iud(q,val)
    return '''<script>alert("Added");window.location='/complaints1'</script>'''



@app.route('/send_doubts',methods=['post'])
@login_required
def send_doubts():
    qry="select * from expert"
    res=selectall(qry)
    return render_template("Farmer/Send Doubts.html",val=res)

@app.route('/send_doubt1',methods=['post'])
@login_required
def send_doubt1():
    doubt=request.form['textfield2']
    eid=request.form['select']
    q="INSERT INTO `doubt`   VALUES(NULL,%s,%s,%s,curdate(),'pending')"
    val=(session['lid'],eid,doubt)
    iud(q,val)
    return '''<script>alert("Added");window.location='/doubts1'</script>'''



@app.route('/send_feedback',methods=['post'])
@login_required
def send_feedback():
    return render_template("Farmer/Send Feedback.html")

@app.route('/addfeedback',methods=['get','post'])
@login_required
def addfeedback():
    feedback=request.form['textfield']
    qry = "insert into feedback values(null,%s,%s,curdate())"
    val = (session['lid'],feedback )
    iud(qry, val)
    return '''<script>alert("Added");window.location='/feedback '</script>'''






@app.route('/view_crops')
@login_required
def view_crops():
    qry="SELECT * from crop"
    res=selectall(qry)
    return render_template("Farmer/View Crops.html",val=res)


@app.route('/view_fertilizer')
@login_required
def view_fertilizer():
    qry="SELECT * from fertilizer"
    res=selectall(qry)
    return render_template("Farmer/View Fertilizer.html",val=res)


@app.route('/view_notification')
@login_required
def view_notification():
    qry="SELECT * from notification"
    res=selectall(qry)
    return render_template("Farmer/View Notification.html",val=res)


@app.route('/view_tips')
@login_required
def view_tips():
    qry="SELECT  expert.First_name,expert.Last_name,tips.* FROM expert JOIN tips ON expert.l_id=tips.ex_id"
    res=selectall(qry)
    return render_template("Farmer/View Tips.html",val=res)



@app.route('/expertreg',methods=['get','post'])
@login_required
def expertreg():
    fname=request.form['textfield']
    lname=request.form['lname']
    age=request.form['textfield2']
    place=request.form['textfield4']
    pin=request.form['textfield3']
    phone_no=request.form['textfield5']
    uname=request.form['textfield6']
    pswrd=request.form['textfield7']
    qry="insert into login values(null,%s,%s,'expert')"
    val=(uname,pswrd)
    id=iud(qry,val)
    qry="insert into expert values(null,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,phone_no,place,age,pin)
    iud(qry,val)
    return'''<script>alert("Added");window.location='/manage_expert'</script>'''


@app.route('/cropmanage',methods=['get','post'])
@login_required
def cropmanage():
    cname=request.form['textfield']
    discription=request.form['textfield2']
    qry="insert into crop values(null,%s,%s)"
    val=(cname,discription)
    iud(qry,val)
    return'''<script>alert("Added");window.location='/manage_crop'</script>'''

@app.route('/addnotification1',methods=['get','post'])
@login_required
def addnotification1():
    notification=request.form['textfield']
    qry="insert into notification values(null,%s,%s,curdate())"
    val=(session['lid'],notification)
    iud(qry,val)
    return'''<script>alert("Added");window.location='/add_notification'</script>'''


@app.route('/addtips1',methods=['get','post'])
@login_required
def addtips1():
    tips=request.form['textfield']
    qry = "insert into tips values(null,%s,%s,curdate())"
    val = (session['lid'], tips)
    iud(qry, val)
    return '''<script>alert("Added");window.location='/manage_tips'</script>'''

@app.route('/addtips',methods=['get','post'])
@login_required
def addtips():
    return render_template('Expert/Add Tips.html')

@app.route('/addfertilizer1',methods=['get','post'])
@login_required
def addfertilizer1():
    fertname=request.form['textfield2']
    description=request.form['textfield']
    qry = "insert into fertilizer values(null,%s,%s,%s)"
    val = (session['lid'], fertname,description)
    iud(qry, val)
    return '''<script>alert("Added");window.location='/manage_fertilizer'</script>'''


@app.route('/reply_to_doubt')
@login_required
def reply_to_doubt():
    id=request.args.get('id')
    session['did']=id
    return render_template("Expert/Reply to Doubt.html")

@app.route('/sendreply',methods=['get','post'])
@login_required
def sendreply():
    reply=request.form['textfield']
    qry = "UPDATE `doubt` SET Reply=%s WHERE D_id=%s"
    val= ( reply,session['did'])
    iud(qry, val)
    return '''<script>alert("Added");window.location='/doubt'</script>'''



@app.route('/reply_to_complaints')
@login_required
def reply_to_complaints():
    id = request.args.get('id')
    session['cid'] = id
    return render_template("Expert/Reply to Complaints.html")

@app.route('/sendreplytocomplaints',methods=['get','post'])
@login_required
def sendreplytocomplaints():
    reply=request.form['textfield']
    qry = "UPDATE `complaint` SET Reply=%s WHERE Comp_id=%s"
    val= ( reply,session['cid'])
    iud(qry, val)
    return '''<script>alert("Reply Successfully");window.location='/complaints'</script>'''







app.run(debug=True)
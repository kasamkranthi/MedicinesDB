import pymysql
import pymysql.cursors
from datetime import date,datetime
from dateutil import parser
from dateutil.relativedelta import relativedelta
a=21
b=16
def reqmeduidinp(x):
	try:
		#deleting FKS first
		q1="DELETE FROM cures WHERE medicine_ID='%d';" % (x)
		curr.execute(q1)
		q2="DELETE FROM made_of WHERE medicine_ID='%d';" % (x)
		curr.execute(q2)
		q3="DELETE FROM uses WHERE m_ID='%d';" % (x)
		curr.execute(q3)
		q4="DELETE FROM cures WHERE medicine_ID='%d';" % (x)
		curr.execute(q1)
		query="DELETE FROM medicines WHERE UID='%d';" % (x)
		db.cursor().execute(query)
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)		
def medreq():
	try:
		na=input("Enter mobilenumber of the person:")
		query= "SELECT name_customer,name,quantity FROM details INNER JOIN rm_attributes ON details.p_number=rm_attributes.number WHERE p_number='%s';" % (na) #WHERE rm_attributes.number = '%s'
		curr.execute(query)
		rows=curr.fetchall()
		for row in rows:
			print (row["name_customer"],row["name"],row["quantity"])
		db.commit()
	except Exception as exp:	
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)	
def expdatecheck():
	try:
		#print(date.today())
		query="SELECT * FROM  medicines WHERE expiry_date <= DATE(NOW());"	
		curr.execute(query)
		rows=curr.fetchall()
		if len(rows)==0:
			print("None expired")
		for row in rows:
			print(row["UID"],row["medicine_name"],row["expiry_date"],row["type"])
		db.commit()
	except Exception as exp:	
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)	
def searchmed():
	try:
		na=input("Enter name of Medicine: ")
		queryy = "SELECT UID,medicine_name,cost,company_name,expiry_date from medicines WHERE medicine_name='%s';" % (na)
		curr.execute(queryy)
		rows = curr.fetchall()
		if len(rows)==0:
			print("Not found")
		else:
			for row in rows:
				print(row["UID"],row["medicine_name"],row["cost"],row["company_name"],row["expiry_date"])
		db.commit()
	except Exception as exp:	
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)	
def costofmed():
	try:
		na=int(input("Enter UID of The Medicine: "))		
		query= "SELECT UID,medicine_name,cost FROM medicines WHERE UID='%d';" % (na)
		curr.execute(query)
		rows=curr.fetchall()
		if len(rows)==0:
			print("Not found give correct UID")
		else :
			for row in rows:
				print(row["UID"],row["medicine_name"],row["cost"])
		db.commit()
	except Exception as exp:	
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)			
def reqmed():
	try:
		"""
		queryy = "SELECT * from people_requests;"
		curr.execute(queryy)
		rows = curr.fetchall()
		for row in rows:
			print(row)		
		"""
		newr={}
		newr[0]=input("Enter Mobile number:  ")
		check="SELECT mobilenumber FROM people_requests WHERE mobilenumber='%s';" % (newr[0])
		curr.execute(check)
		lat=curr.fetchall()
		if len(lat)==0 : 
			query="INSERT INTO people_requests VALUES ('%s');" % (newr[0])
			db.cursor().execute(query)
			print("Details")
			newr[1]=input("Enter your name: ")
			newr[2]=input("Home number: ")
			newr[3]=input("Street Name: ")
			newr[4]=input("Village Name: ")
			newr[5]=input("Pincode: ")
			newr[6]=input("State: ")
			newr[7]=input("Date of request: ")
			query1="INSERT INTO details VALUES ('%s','%s','%s','%s','%s','%s','%s','%s');" % (newr[1],newr[2],newr[3],newr[4],newr[5],newr[6],newr[7],newr[0])
			db.cursor().execute(query1)		
			query2="INSERT INTO requested_medicines VALUES ('%s');" % (newr[0])
			db.cursor().execute(query2)
			print("Medicine Details: as Name,quantity; seperate with semicolon")		
			MS=input()
			#medic={}
			medic=MS.split(';')
			lent=len(medic)
			print(lent)
			for x in range(lent):
				print(medic[x])
				dets = medic[x].split(',')
				print(dets[0])
				print(dets[1])
				query="INSERT INTO rm_attributes VALUES ('%s','%d','%s');" % (dets[0],int(dets[1]),newr[0])
				db.cursor().execute(query)
		else:
			print("Not new customer give medicine details directly")
			query2="INSERT INTO requested_medicines VALUES ('%s');" % (newr[0])
			db.cursor().execute(query2)			
			MS=input()
			#medic={}
			medic=MS.split(';')
			lent=len(medic)
			print(lent)
			for x in range(lent):
				print(medic[x])
				dets = medic[x].split(',')
		#		print(dets[0])
		#		print(dets[1])
				query="INSERT INTO rm_attributes (name,quantity,number) VALUES ('%s','%d','%s');" % (dets[0],int(dets[1]),newr[0])
				db.cursor().execute(query)		
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)	
def modmed():
	try:
		newr={}
		newr[0]=int(input("Give UID of medicine to change cost: "))
		newr[1]=int(input("GIVE the new cost:  "))
		query="UPDATE medicines SET cost = '%d' WHERE UID = '%d';" % (newr[1],newr[0])
		db.cursor().execute(query)
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)		
def remmed():
	try:
		newr={}
		newr[0]=int(input("Give UID of medicine to remove"))
		#deleting FKS first
		q1="DELETE FROM cures WHERE medicine_ID='%d';" % (newr[0])
		curr.execute(q1)
		q2="DELETE FROM made_of WHERE medicine_ID='%d';" % (newr[0])
		curr.execute(q2)
		q3="DELETE FROM uses WHERE m_ID='%d';" % (newr[0])
		curr.execute(q3)
		q4="DELETE FROM cures WHERE medicine_ID='%d';" % (newr[0])
		curr.execute(q1)
		query="DELETE FROM medicines WHERE UID='%d';" % (newr[0])
		db.cursor().execute(query)
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)	

def addMed():
	try:
		global a
		global b
		mq="SELECT UID FROM medicines ORDER BY UID DESC LIMIT 1;"
		curr.execute(mq)
		ids=curr.fetchall()
		a=int(ids[0]["UID"])
		a=a+2
		newr= {}
		newr[7]=a
		print("Enter details:  ")
		newr[0]=input("Medicine_name:  ")
		newr[1]=int(input("cost? "))
		MOD=input("date_of_manufacture:  ")
		newr[2]= parser.parse(MOD)
		newr[3]=int(input("Best before in months: "))
		print(newr[3])
		
		newr[4]= (newr[2] + relativedelta(months=+newr[3])).date()
		print(newr[4])
		newr[5]=input("Type Ointment,tablet,tonic,injection: ")
		newr[6]=input("Company Name: ")
		
		query="INSERT INTO company VALUES ('%s');" % (newr[6])
		print(query)
		db.cursor().execute(query)		
		query1= "INSERT INTO medicines (UID,medicine_name,cost,date_of_manufacture,best_before,expiry_date,type,company_name) VALUES ('%d','%s','%d','%s','%d','%s','%s','%s')" % (newr[7],newr[0],newr[1],newr[2],newr[3],newr[4],newr[5],newr[6])
#		a=a+2
		print(query1)
		db.cursor().execute(query1)
		print("Chemicals Used in this medicine: Give C1,C2,C3 so on as input")
		cid=0	
		chem=input()
		chems=chem.split(',')
		for che in chems:
			query="SELECT chemical_ID from chemical WHERE chemical_name='%s';" % (che)
			curr.execute(query)
			new=curr.fetchall()
			if len(new)==0:
				mq="SELECT chemical_ID FROM chemical ORDER BY chemical_ID DESC LIMIT 1;"
				curr.execute(mq)
				ids=curr.fetchall()
				b=int(ids[0]["chemical_ID"])				
				b=b+2;
				cid=b
				query1="INSERT INTO chemical VALUES ('%s','%d');" % (che,b)
				curr.execute(query1)
			else :
				cid=new[0]["chemical_ID"]
				#cid=new["chemical_ID"]
			query2="INSERT INTO made_of VALUES ('%d','%d');" % (a,cid)
			curr.execute(query2)
		symp="fever"
		dis=input("Diseases that can be cured by this medicine as d1,d2,d3 so on: ")
		dise=dis.split(',')
		for diseas in dise:
			dquery="SELECT disease_namename from disease WHERE disease_namename='%s';" % (diseas)
			curr.execute(dquery)
			disea=curr.fetchall()
			if len(disea)==0 : 
				query4="INSERT INTO disease VALUES ('%s')" % (diseas)
				diseasename=diseas
				curr.execute(query4)
			else:
				diseasename=diseas
			query5="INSERT INTO cures VALUES ('%d','%s','%s');" % (a,diseasename,symp)
			curr.execute(query5)
		#a=a+2
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)
	return
def medfordisease():
	try:
		na=input("Enter name of Disease: ")
		queryy = "SELECT medicine_ID from cures WHERE disease_name='%s';" % (na)
		curr.execute(queryy)
		rows = curr.fetchall()
		if len(rows)==0:
			print("Not found")
		else:
			for row in rows:
				querys="SELECT UID,medicine_name from medicines where UID='%s';" %(row["medicine_ID"])
				curr.execute(querys)
				meds=curr.fetchall()
				for med in meds:
					print(med["UID"] , med["medicine_name"])
		db.commit()
	except Exception as exp:	
		db.rollback()
		print("Failed")
		print(">>>>>>",exp)
def reqmedindec():
	try:
		queryy="SELECT name,quantity from rm_attributes ORDER BY name ASC"
		newdict=dict()
		#print(newdict)
		curr.execute(queryy)
		rows=curr.fetchall()
		my_list=[]
		print(rows)
		temp_name=rows[0]["name"]
		temp_quan=0
		for i in range(len(rows)):
			if temp_name==rows[i]["name"]:
				temp_quan+=int(rows[i]["quantity"])
			else :
				newdict[temp_name]=temp_quan
				temp_name=rows[i]["name"]
				temp_quan=int(rows[i]["quantity"])
			if i==len(rows)-1:
				newdict[temp_name]=temp_quan				
		#from operator import itemgetter
		#{k: v for k, v in sorted(newdict.items(), key=lambda item: item[1]).reverse()}
	#	newdict=sorted(newdict,key=itemgetter('quantity'))
		nnn=sorted(newdict.items(),key=lambda x: x[1],reverse=True)
		print ("Name : quantity")
		for a,b in nnn:
			print(a+ " : "+str(b))
	#	for key,value in nnn.items():
	#		print("{}: {}".format(key,value))
	#	my_list=my_list+(temp_name,temp_quan)
	#	my_list.sort(key=operator.itemgetter(1))
		#my_list.sort(key=lambda xW:x[1])
	#	print(my_list)
	#	print(newdict)
		db.commit()
	except Exception as exp:
		db.rollback()
		print("Failes")
		print(">>>>>",exp)
def bill():
	try:
		PRICE=0;
		na=input("Give medicine names seperated by commas M1,M2 so on : ")
		hello=na.split(",")
		for x in hello:
			query="SELECT UID,cost FROM medicines WHERE medicine_name='%s';" % (x)
			curr.execute(query)
			row=curr.fetchone()
			if row==None:
				print("Sorry the medicine "+ x + " Is not available but hey you can requested it" )
			else :
				PRICE = PRICE + int(row["cost"])
				print("Medicine Name: "+x + " Cost: "+str(row["cost"]))
				reqmeduidinp(int(row["UID"]))

		print("Total Price:  " + str(PRICE))
	except Exception as exp:
		db.rollback()
		print("Failes")
		print(">>>>>",exp)

def todo(inp):
	if(inp==1):
		addMed()
	elif inp==2:
		remmed()
	elif inp==3:
		modmed()
	elif inp==4:
		reqmed()
	elif inp==5:
		searchmed()
	elif inp==6:
		costofmed()
	elif inp==7:
		medreq()
	elif inp==8:
		expdatecheck()
	elif inp==9:
		medfordisease()
	elif inp==10:
		reqmedindec()
	elif inp==11:
		bill()
	else:
		print("Error choose only b/w 1 and 4")
hostn=input("Host of the MySql server:  ")
portn=int(input("Port number: "))
usern=input("Username: ")
pw=input("password: ")
while(1):
	db= pymysql.connect(host=hostn,user=usern,port=portn,password= pw,db= "MEDICINE", cursorclass=pymysql.cursors.DictCursor)
	if(db.open):
		with db.cursor() as curr:
			print("connected")
			print("choose 1 to add a new MEDICINE")
			print("choose 2 to remove a MEDICINE using UID")
			print("choose 3 to modify cost of a MEDICINE")
			print("choose 4 to request a medicine")
			print("choose 5 to search for a medicine")
			print("choose 6 to get cost of a medicine")			
			print("choose 7 to get all medicines requested by a person")			
			print("choose 8 to get list of medicines expired today")
			print("chosse 9 to get list of medicines available for a particular disease")			
			print("choose  10 to get requested medicines in  decreasing order of quantity")
			print("chosse 11 to to sell and get the bill")													
			print("Chppse any number more than 11 to exit")
			inp=int(input("Choose:  "))
			if inp>=12:
				break;
			else:
				todo(inp)
	else:
		print("connection failed")

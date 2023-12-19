from email import message
from unittest import result
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from webapp.models import UserInput
from webapp.forms import PostForm
import random

def index(request):
	rank = UserInput.objects.all().order_by("cUserScore")
	ranking = []
	for i in rank:
		ranking.insert(0, i)
	try:
		ranking_1 =str(ranking[0].cUserName) + "：" + str(ranking[0].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_2 =str(ranking[1].cUserName) + "：" + str(ranking[1].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_3 =str(ranking[2].cUserName) + "：" + str(ranking[2].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_4 =str(ranking[3].cUserName) + "：" + str(ranking[3].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_5 =str(ranking[4].cUserName) + "：" + str(ranking[4].cUserScore) + "連勝"
	except:
		pass
	
	if request.method == 'POST':
		inputaccount = request.POST['account']
		inputpassword = request.POST['password']
		
		try:
			unit = UserInput.objects.get(cUserAccount=inputaccount)
			check_account = True
		except:
			check_account = False
		
		if check_account:
			if unit.cUserPassword == inputpassword:
				loged_in_name = unit.cUserName
				loged_in_account = unit.cUserAccount
				loged_in_password = unit.cUserPassword
				loged_in_picture = unit.cUserPicture
				loged_in_style = unit.cUserStyle
				loged_in_score = unit.cUserScore
				print(loged_in_name, loged_in_account, loged_in_password, loged_in_picture, loged_in_style, loged_in_score)
				message = "成功登入"
				return render(request, "mainpage.html", locals())
			else:
				message = "密碼錯誤"
		else:
			message = "帳號錯誤"
		
		return render(request, "index.html", locals())
	else:
		return render(request, "index.html", locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	if request.method == 'get':
		return redirect('/signup/')
	postform = PostForm
	return render(request, "index.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')	

def signup(request):
	if request.method == 'POST':
		postform = PostForm(request.POST)
		if postform.is_valid():
			try:
				useraccount = postform.cleaned_data['cUserAccount']
				useraccount = UserInput.objects.get(cUserAccount=useraccount)
			except:
				useraccount=None
			
			try:
				username = postform.cleaned_data['cUserName']
				username = UserInput.objects.get(cUserName=username)
			except:
				username=None
			
			try:
				userpassword = postform.cleaned_data['cUserPassword']
				userpassword = UserInput.objects.get(cUserPassword=userpassword)
			except:
				userpassword=None
			
			if useraccount != None:
				print(useraccount)
				message = "帳號已存在!"
			elif username != None:
				message = "使用者名稱已被使用!"
			elif userpassword != None:
				message = "密碼已被使用!"

			else:
				cUserName = postform.cleaned_data['cUserName']
				cUserAccount = postform.cleaned_data['cUserAccount']
				cUserPassword = postform.cleaned_data['cUserPassword']
				user = UserInput.objects.create(cUserName=cUserName,
												cUserAccount=cUserAccount,
												cUserPassword=cUserPassword,
												)
				print(cUserName, cUserAccount, postform.cleaned_data['cUserName'])
				user.save()
				message = "註冊成功"
			return render(request, "signup.html", locals())	
			
	else:
		postform = PostForm
		return render(request, "signup.html", locals())

def setting_style(request):
	rank = UserInput.objects.all().order_by("cUserScore")
	ranking = []
	for i in rank:
		ranking.insert(0, i)
	try:
		ranking_1 =str(ranking[0].cUserName) + "：" + str(ranking[0].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_2 =str(ranking[1].cUserName) + "：" + str(ranking[1].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_3 =str(ranking[2].cUserName) + "：" + str(ranking[2].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_4 =str(ranking[3].cUserName) + "：" + str(ranking[3].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_5 =str(ranking[4].cUserName) + "：" + str(ranking[4].cUserScore) + "連勝"
	except:
		pass
	if request.method == 'POST':
		try:
			loged_in_name = request.POST['loged_in_name']
			loged_in_account = request.POST['loged_in_account']
			loged_in_password = request.POST['loged_in_password']
			loged_in_picture = request.POST['loged_in_picture']
			loged_in_style = request.POST['change_style']
			loged_in_score = request.POST['loged_in_score']
			unit = UserInput.objects.get(cUserAccount=loged_in_account)
			unit.cUserStyle = loged_in_style
			unit.save()
			print(loged_in_account, unit.cUserStyle)
			return render(request, "mainpage.html", locals())
		except:
			loged_in_name = request.POST['loged_in_name']
			loged_in_account = request.POST['loged_in_account']
			loged_in_password = request.POST['loged_in_password']
			#loged_in_picture = request.POST['loged_in_picture']
			loged_in_style = request.POST['loged_in_style']
			loged_in_score = request.POST['loged_in_score']
			return render(request, "mainpage.html", locals())

def games(request):
	if request.method == 'POST':
		loged_in_name = request.POST['loged_in_name']
		loged_in_account = request.POST['loged_in_account']
		loged_in_password = request.POST['loged_in_password']
		loged_in_picture = request.POST['loged_in_picture']
		loged_in_style = request.POST['loged_in_style']
		loged_in_score = request.POST['loged_in_score']
		try:
			unit = UserInput.objects.get(cUserAccount=loged_in_account)
			loged_in_temporarily_score = unit.cUserTemporarilyScore
			return render(request, "game1.html", locals())
		except:
			return render(request, "game1.html", locals())
		return render(request, "game1.html", locals())

def back(request):
	rank = UserInput.objects.all().order_by("cUserScore")
	ranking = []
	for i in rank:
		ranking.insert(0, i)
	try:
		ranking_1 =str(ranking[0].cUserName) + "：" + str(ranking[0].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_2 =str(ranking[1].cUserName) + "：" + str(ranking[1].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_3 =str(ranking[2].cUserName) + "：" + str(ranking[2].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_4 =str(ranking[3].cUserName) + "：" + str(ranking[3].cUserScore) + "連勝"
	except:
		pass
	try:
		ranking_5 =str(ranking[4].cUserName) + "：" + str(ranking[4].cUserScore) + "連勝"
	except:
		pass
	loged_in_name = request.POST['loged_in_name']
	loged_in_account = request.POST['loged_in_account']
	loged_in_password = request.POST['loged_in_password']
	loged_in_picture = request.POST['loged_in_picture']
	loged_in_style = request.POST['loged_in_style']
	loged_in_score = request.POST['loged_in_score']
	unit = UserInput.objects.get(cUserAccount=loged_in_account)
	return render(request, "mainpage.html", locals())

def janken_choki(request): #剪刀

	com_hand = random.randint(1, 3) #剪刀石頭布
	janken_result = 0   # 0:draw 1:win 2:lose
	player_hand = 'images/janken_choki.png'
	loged_in_account = request.POST['loged_in_account']
	unit = UserInput.objects.get(cUserAccount=loged_in_account)
	if com_hand == 1:
		janken_result = 'draw'
		com_hand = 'images/janken_choki.png'
		com_hand_l = 'images/janken_choki_l.png'
	elif com_hand == 2:
		janken_result = 'lose'
		com_hand = 'images/janken_gu.png'
		com_hand_l = 'images/janken_gu_l.png'
		unit.cUserTemporarilyScore = 0
	else:
		janken_result = 'win'
		com_hand = 'images/janken_pa.png'
		com_hand_l = 'images/janken_pa_l.png'
		unit.cUserTemporarilyScore = int(unit.cUserTemporarilyScore) + 1
	
	if int(unit.cUserTemporarilyScore) > int(unit.cUserScore):
		unit.cUserScore = unit.cUserTemporarilyScore
	unit.save()
	return render(request, "game1_result.html", locals())
	
def janken_gu(request):	#石頭
	com_hand = random.randint(1, 3) #剪刀石頭布
	janken_result = ''   # 0:draw 1:win 2:lose
	player_hand = 'images/janken_gu.png'
	loged_in_account = request.POST['loged_in_account']
	unit = UserInput.objects.get(cUserAccount=loged_in_account)
	if com_hand == 1:
		janken_result = 'win'
		com_hand = 'images/janken_choki.png'
		com_hand_l = 'images/janken_choki_l.png'
		unit.cUserTemporarilyScore = int(unit.cUserTemporarilyScore) + 1
	elif com_hand == 2:
		janken_result = 'draw'
		com_hand = 'images/janken_gu.png'
		com_hand_l = 'images/janken_gu_l.png'
	else:
		janken_result = 'lose'
		com_hand = 'images/janken_pa.png'
		com_hand_l = 'images/janken_pa_l.png'
		unit.cUserTemporarilyScore = 0
	
	if int(unit.cUserTemporarilyScore) > int(unit.cUserScore):
		unit.cUserScore = unit.cUserTemporarilyScore
	unit.save()
	return render(request, "game1_result.html", locals())

def janken_pa(request): #布
	com_hand = random.randint(1, 3) #剪刀石頭布
	janken_result = 0   # 0:draw 1:win 2:lose
	player_hand = 'images/janken_pa.png'
	loged_in_account = request.POST['loged_in_account']
	unit = UserInput.objects.get(cUserAccount=loged_in_account)
	if com_hand == 1:
		janken_result = 'lose'
		com_hand = 'images/janken_choki.png'
		com_hand_l = 'images/janken_choki_l.png'
		unit.cUserTemporarilyScore = 0
	elif com_hand == 2:
		janken_result = 'win'
		com_hand = 'images/janken_gu.png'
		com_hand_l = 'images/janken_gu_l.png'
		unit.cUserTemporarilyScore = int(unit.cUserTemporarilyScore) + 1
	else:
		janken_result = 'draw'
		com_hand = 'images/janken_pa.png'
		com_hand_l = 'images/janken_pa_l.png'
	
	if int(unit.cUserTemporarilyScore) > int(unit.cUserScore):
		unit.cUserScore = unit.cUserTemporarilyScore
	unit.save()
	return render(request, "game1_result.html", locals())
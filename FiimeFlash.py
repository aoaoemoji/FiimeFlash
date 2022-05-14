# -*- coding: utf-8 -*-
# @Author: aoao
# @Date:   2022-05-06 11:11:25
# @Last Modified by:   aoao
# @Last Modified time: 2022-05-14 22:04:29

import os
import time
import shutil
import re
import ctypes
import locale


"""
5.0.0版本
--新增中英文识别切换
--新增lib目录检查
"""


path = os.getcwd()
ospath = path + "\\DXY"
imgpath = path + "\\images\\"
libpath = path + "\\lib\\"
boot_patch = path + "\\images\\boot.img"
exe_path = path + '\\lib'



# 检测程序目录是否完整 V2.0版本
def binfinder():
	print("正在检测工作目录...")
	time.sleep(3)
	if os.path.exists(ospath) != True :
		print("当前目录不包含DXY文件夹(依赖工具库),请检查本工具所在路径是否在解压后的同级目录!")
		time.sleep(3)
		os.system("cls")
		exit()
	elif os.path.exists(imgpath) != True :
		print("当前目录不包含images文件夹(镜像数据),请检查本工具所在路径是否在解压后的同级目录!")
		time.sleep(3)
		os.system("cls")
		exit()
	elif os.path.exists(libpath) != True :
		print("当前目录不包含libs文件夹(组件库),请检查本工具所在路径是否在解压后的同级目录!")
		time.sleep(3)
		os.system("cls")
		exit()
	else:
		print("当前工作环境完整，检测通过!")
		time.sleep(2)
		os.system("cls")
		pass
def binfinder_en():
	print("Checking APP directory...")
	time.sleep(3)
	if os.path.exists(ospath) != True :
		print("The \"DXY\" folder does not exist, Please check!")
		time.sleep(3)
		os.system("cls")
		exit()
	elif os.path.exists(imgpath) != True :
		print("The \"images\" folder does not exist, Please check!")
		time.sleep(3)
		os.system("cls")
		exit()
	elif os.path.exists(libpath) != True :
		print("The \"lib\" folder does not exist, Please check!")
		time.sleep(3)
		os.system("cls")
		exit()
	else:
		print("PATH is Okay，PASS!")
		time.sleep(2)
		os.system("cls")
		pass



# 识别机型代码 V4.0
def getcode():
	global f_code
	code = str(path)
	re_miuiversion = re.search( r'(V[0-9.EDV]{10,40}|[0-9]{2}[0-9.]{2,3}[0-9]{1,2})', code, re.M)
	re_code = re.search( r'_[a-z]{3,8}_', code, re.M)
	if re_miuiversion:
		miuiversion = re_miuiversion.group()
	else:
		miuiversion = "无法识别MIUI版本"
	if re_code:
		f_code = re_code.group().replace("_","")
		devicelist = {'matisse':'红米K50 Pro','rubens':'红米K50','munch':'红米K40S','zeus':'小米12 Pro','cupid':'小米12','psyche':'小米12X','mona':'小米CIVI','elish':'小米平板5 Pro (WiFi)','odin':'小米MIX4','renoir':'小米11 青春版','star':'小米11 Pro / Ultra','thyme':'小米10S','haydn':'红米K40Pro/Pro+/小米11i','alioth':'红米K40 / POCO F3','venus':'小米11','apollo':'红米K30S 至尊纪念版/小米10T/10T','cas':'小米10Uitra','vangogh':'小米10青春版','lmi':'红米K30 Pro/变焦版/POCO F2 Pro','cmi':'小米10Pro','umi':'小米10','picasso':'红米K30 5G/红米K30i 5G'}
		devicename = devicelist[f_code]
		alist = ["rubens","matisse","cupid","zeus","psyche","odin","mona"]
		blist = ['elish','star','venus','renoir','thyme','alioth','haydn','munch']
		clist = ['umi','cmi','cas','vangogh','lmi','picasso','apollo']
		if f_code in alist:
			print("-------------------------------------------------------------------------------------- ")
			print("当前识别到代号为:%s,机型为:%s,类型为:Erofs机型,MIUI版本:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				erofs()
			elif sure == 'N':
				print("已经取消...")
				mainchoice()
			else:
				pass
		elif f_code in blist:
			print("-------------------------------------------------------------------------------------- ")
			print("当前识别到代号为:%s,机型为:%s,类型为:VAB机型,MIUI版本:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				erofs()
			elif sure == 'N':
				print("已经取消...")
				mainchoice()
			else:
				pass
		elif f_code in clist:
			print("-------------------------------------------------------------------------------------- ")
			print("当前识别到代号为:%s,机型为:%s,类型为:OnlyA机型,MIUI版本:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				onlya()
			elif sure == 'N':
				print("已经取消...")
				mainchoice()
			else:
				pass
		else:
			print("无法识别当前机型！")
			pass

	else:
		print("未识别到机型,请手动选择")
		time.sleep(1)
		pass
def getcode_en():
	global f_code
	code = str(path)
	re_miuiversion = re.search( r'(V[0-9.EDV]{10,40}|[0-9]{2}[0-9.]{2,3}[0-9]{1,2})', code, re.M)
	re_code = re.search( r'_[a-z]{3,8}_', code, re.M)
	if re_miuiversion:
		miuiversion = re_miuiversion.group()
	else:
		miuiversion = "Miui version can not be recognized"
	if re_code:
		f_code = re_code.group().replace("_","")
		devicelist = {'matisse':'RedmiK50 Pro','rubens':'RedmiK50','munch':'RedmiK40S','zeus':'Xiaomi12 Pro','cupid':'Xiaomi12','psyche':'Xiaomi12X','mona':'XiaomiCIVI','elish':'Xiaomi stable 5 Pro (WiFi)','odin':'XiaomiMIX4','renoir':'Xiaomi11 Young','star':'Xiaomi11 Pro / Ultra','thyme':'Xiaomi10S','haydn':'RedmiK40Pro/Pro+/Xiaomi11i','alioth':'RedmiK40 / POCO F3','venus':'Xiaomi11','apollo':'RedmiK30S Plus/Xiaomi10T/10T','cas':'Xiaomi10Uitra','vangogh':'Xiaomi10Young','lmi':'RedmiK30 Pro/POCO F2 Pro','cmi':'Xiaomi10Pro','umi':'Xiaomi10','picasso':'RedmiK30 5G/RedmiK30i 5G'}
		devicename = devicelist[f_code]
		alist = ["rubens","matisse","cupid","zeus","psyche","odin","mona"]
		blist = ['elish','star','venus','renoir','thyme','alioth','haydn','munch']
		clist = ['umi','cmi','cas','vangogh','lmi','picasso','apollo']
		if f_code in alist:
			print("-------------------------------------------------------------------------------------- ")
			print("Currently identified as:%s,Phone:%s,Type:Erofs,MIUI:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("Whether the identification is accurate?(Y/N):\n")
			if sure == 'Y':
				print("Begin to flash...")
				erofs_en()
			elif sure == 'N':
				print("Cancelled...")
				mainchoice_en()
			else:
				pass
		elif f_code in blist:
			print("-------------------------------------------------------------------------------------- ")
			print("Currently identified as:%s,Phone:%s,Type:VAB,MIUI:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("Whether the identification is accurate?(Y/N):\n")
			if sure == 'Y':
				print("Begin to flash...")
				erofs_en()
			elif sure == 'N':
				print("Cancelled...")
				mainchoice_en()
			else:
				pass
		elif f_code in clist:
			print("-------------------------------------------------------------------------------------- ")
			print("Currently identified as:%s,Phone:%s,Type:OnlyA,MIUI:%s"%(f_code,devicename,miuiversion))
			print("-------------------------------------------------------------------------------------- ")
			sure = input("Whether the identification is accurate?(Y/N):\n")
			if sure == 'Y':
				print("Begin to flash...")
				onlya_en()
			elif sure == 'N':
				print("Cancelled...")
				mainchoice_en()
			else:
				pass
		else:
			print("Unable to identify the current models!")
			pass

	else:
		print("Model not recognized, please select manually")
		time.sleep(1)
		pass


# 刷机工具环境
def flash(filepath,imgfile):
	os.chdir(ospath)
	os.system("fastboot.exe flash" + " " + filepath + " " + imgfile)

def flashsingle(order):
	os.chdir(ospath)
	os.system("fastboot.exe "+ " " + order)

# 新增修补boot文件
def fixboot():
	while True:
		dodo = input("是否需要修补boot分区?(Y/N):"+"\n")
		if dodo == "Y":
			os.chdir(exe_path) # 目录切换到boot_sh脚本
			shutil.copyfile(boot_patch, exe_path + "\\boot.img")
			os.system("boot_patch.bat boot.img")
			print("开始修补！")
			os.remove(exe_path + "\\boot.img")
			os.remove(boot_patch)
			shutil.copyfile(exe_path + "\\new-boot.img",boot_patch)
			os.remove(exe_path + "\\new-boot.img")
			print("修补并替换原版boot完成,即将开始其他操作...")
			break

		elif dodo == "N":
			print("您选择了取消修补boot,即将开始其他操作...")
			time.sleep(1)
			break
		else:
			print("输入错误，请重新输入!")
			break
def fixboot_en():
	while True:
		dodo = input("Need Fix boot.img with MagiskPath?(Y/N):"+"\n")
		if dodo == "Y":
			os.chdir(exe_path) # 目录切换到boot_sh脚本
			shutil.copyfile(boot_patch, exe_path + "\\boot.img")
			os.system("boot_patch.bat boot.img")
			print("Ahhh... start！")
			os.remove(exe_path + "\\boot.img")
			os.remove(boot_patch)
			shutil.copyfile(exe_path + "\\new-boot.img",boot_patch)
			os.remove(exe_path + "\\new-boot.img")
			print("Fixed and replace done ,well do another...")
			break

		elif dodo == "N":
			print("Cancel Fix boot,well do another...")
			time.sleep(1)
			break
		else:
			print("You may have made a big mistake, the size of the earth，Please Re-enter!")
			break


# 开始刷机脚本调用
def vab():
	pass

def onlya(): # 新增onlya刷机方案 3.0版本
	fixboot()
	while True:
		wipeuser = input("是否双清用户数据(Y/N):\n")
		if wipeuser == "Y":
			print("清除双清用户数据")
			os.chdir(ospath)
			os.system("fastboot erase metadata")
			os.system("fastboot erase userdata")
			break
		elif  wipeuser == "N":
			print("取消双清用户数据")
			break
		else:
			print("输入有误，重新输入！")
	while True:
		wipedata = input("是否清除DATA分区(Y/N),某些时候不清除可能卡开机:\n")
		if wipedata == "Y":
			print("清除DATA分区")
			os.chdir(ospath)
			os.system("fastboot -w")
			break
		elif  wipedata == "N":
			print("取消清除DATA分区")
			break
		else:
			print("输入有误，重新输入！")
	while True:
		sureflash =  input("确认开始刷机(Y/N):\n")
		if sureflash == "Y":
			print("确认执行刷机操作...")
			time.sleep(2)
			os.system("cls")
			filelist = os.listdir(imgpath)                                
			print("当前获取以下镜像文件:\n%s"%(filelist))
			print("3秒后自动开始刷机操作...")
			time.sleep(3)
			# 添加一个防止小白的功能 V3.0版本
			errorimg_list = ['system.img','vendor.img','product.img','odm.img','system_ext.img']
			for image_id in filelist:
				position=imgpath+"\\"+image_id # 镜像文件
				aa=image_id.replace('.img','') # 分区名字
				if image_id in errorimg_list:
					print("请检查images镜像文件夹，当前有不被允许的镜像:%s存在!"%(image_id))
					time.sleep(3)
					exit()
				else:
					if image_id =="NON-HLOS.img":
						os.rename(image_id, "modem.img")
					elif image_id =="uefi_sec.img":
						os.rename(image_id, "uefisecapp.img")
					elif image_id =="qupv3fw.img":
						os.rename(image_id, "qupfw.img")
					elif image_id =="km4.img":
						os.rename(image_id, "keymaster.img")
					elif image_id =="dspso.img":
						os.rename(image_id, "dsp.img")
					elif image_id =="BTFM.img":
						os.rename(image_id, "bluetooth.img")
					else :
						print("喵~")
			for imgxxx in filelist:
				kkpath=imgpath+"\\"+imgxxx # 镜像文件
				bb=imgxxx.replace('.img','') # 分区名字
				flash(bb,kkpath)
			# 重启设备 
			print("刷机完成!即将重启设备...")
			time.sleep(3)
			flashsingle("reboot")
			print("刷机完成!30秒后自动退出！")
			time.sleep(30)
			break
		elif sureflash == "N":
			print("取消刷机操作,正在退出程序...")
			time.sleep(3)
			os.system("cls")
			exit()
			break
		else:
			print("输入有误，重新输入！")
def onlya_en(): # 新增onlya刷机方案 3.0版本
	fixboot_en()
	while True:
		wipeuser = input("Wipe userdata(Y/N):\n")
		if wipeuser == "Y":
			print("Erasing userdata...")
			os.chdir(ospath)
			os.system("fastboot erase metadata")
			os.system("fastboot erase userdata")
			break
		elif  wipeuser == "N":
			print("Cancel Wipe userdata！")
			break
		else:
			print("Error in input, Please re-enter!")
	while True:
		wipedata = input("Wipe DATA Partition(Y/N),Sometimes it may not Boot if it is not wiped.:\n")
		if wipedata == "Y":
			print("Wipe DATA Partition...")
			os.chdir(ospath)
			os.system("fastboot -w")
			break
		elif  wipedata == "N":
			print("Cancel Wipe DATA Partition!")
			break
		else:
			print("Error in input, Please re-enter!")
	while True:
		sureflash =  input("Sure to Flash(Y/N):\n")
		if sureflash == "Y":
			print("Okay，I'm doing...")
			time.sleep(2)
			os.system("cls")
			filelist = os.listdir(imgpath)                                
			print("Gets the following image files:\n%s"%(filelist))
			print("Wait 3s and will start...")
			time.sleep(3)
			# 添加一个防止小白的功能 V3.0版本
			errorimg_list = ['system.img','vendor.img','product.img','odm.img','system_ext.img']
			for image_id in filelist:
				position=imgpath+"\\"+image_id # 镜像文件
				aa=image_id.replace('.img','') # 分区名字
				if image_id in errorimg_list:
					print("Please Check images folder，There are currently disallowed img file:%s found!"%(image_id))
					time.sleep(3)
					exit()
				else:
					if image_id =="NON-HLOS.img":
						os.rename(image_id, "modem.img")
					elif image_id =="uefi_sec.img":
						os.rename(image_id, "uefisecapp.img")
					elif image_id =="qupv3fw.img":
						os.rename(image_id, "qupfw.img")
					elif image_id =="km4.img":
						os.rename(image_id, "keymaster.img")
					elif image_id =="dspso.img":
						os.rename(image_id, "dsp.img")
					elif image_id =="BTFM.img":
						os.rename(image_id, "bluetooth.img")
					else :
						print("Miao~")
			for imgxxx in filelist:
				kkpath=imgpath+"\\"+imgxxx # 镜像文件
				bb=imgxxx.replace('.img','') # 分区名字
				flash(bb,kkpath)
			# 重启设备 
			print("Well Bro you are luck! I'm reboot now...")
			time.sleep(3)
			flashsingle("reboot")
			print("Work Done! After 30s and Autoexit！")
			time.sleep(30)
			break
		elif sureflash == "N":
			print("Cancel Flash,i'm planning to escape the earth...Bye,Bro!")
			time.sleep(3)
			os.system("cls")
			exit()
			break
		else:
			print("Error in input, Please re-enter!")


# 开始菜单 V4.1
def mainchoice():
	print('{:=^80}'.format(str1)) 
	print("请输入对应的\"数字\"指令选择机型进行刷机操作:")
	print("1.Erofs机型:\n[红米K50(rubens) 红米K50Pro(matisse) 小米12(cupid) 小米12Pro(zeus)\n小米12X(psyche) 小米MIX4(odin) 小米CIVI(mona)]")
	print("	") 
	print("2.Vab机型：\n[小米平板5ProWifi(elish) 小米11Pro(star) 小米11(venus) 小米11青春版(renoir)\n小米10S(thyme) 红米K40(alioth) 红米K40Pro(haydn) 红米K40S(munch)]")
	print("	") 
	print("3.OnlyA机型：\n[小米10(umi) 小米10Pro(cmi) 小米10Uitra(cas) 小米10青春版(vangogh)\n红米K30Pro(lmi) 红米K30i-5G(picasso) 红米K30S 至尊纪念版(apollo)]")
	print('{:=^80}'.format(str1)) 

	while True:
		userchocie = str(input("请输入数字指令:\n"))
		if userchocie == "1":
			print("您选择了:%s，这是Erofs机型"%(userchocie))
			erofs()
			break
		elif  userchocie == "2":
			print("您选择了:%s，这是Vab机型"%(userchocie))
			erofs()
			# vab()  通用暂时留空吧
			break
		elif  userchocie == "3":
			print("您选择了:%s，这是OnlyA机型"%(userchocie))
			onlya()
			# vab()  通用暂时留空吧
			break
		else:
			os.system("cls")
			print("输入有误,请重新输入!")
			time.sleep(1)
def erofs():
	fixboot()
	while True:
		wipeuser = input("是否双清用户数据(Y/N):\n")
		if wipeuser == "Y":
			print("清除双清用户数据")
			os.chdir(ospath)
			os.system("fastboot erase metadata")
			os.system("fastboot erase userdata")
			break
		elif  wipeuser == "N":
			print("取消双清用户数据")
			break
		else:
			print("输入有误，重新输入！")
	while True:
		wipedata = input("是否清除DATA分区(Y/N),某些时候不清除可能卡开机:\n")
		if wipedata == "Y":
			print("清除DATA分区")
			os.chdir(ospath)
			os.system("fastboot -w")
			break
		elif  wipedata == "N":
			print("取消清除DATA分区")
			break
		else:
			print("输入有误，重新输入！")
	while True:
		sureflash =  input("确认开始刷机(Y/N):\n")
		if sureflash == "Y":
			print("确认执行刷机操作...")
			time.sleep(2)
			os.system("cls")
			filelist = os.listdir(imgpath)                                
			print("当前获取以下镜像文件:\n%s"%(filelist))
			print("3秒后自动开始刷机操作...")
			time.sleep(3)
			# 添加一个防止小白的功能 V3.0版本
			errorimg_list = ['system.img','vendor.img','product.img','odm.img','system_ext.img']
			for image_id in filelist:
				position=imgpath+"\\"+image_id # 镜像文件
				aa=image_id.replace('.img','') # 分区名字
				if image_id in errorimg_list:
					print("请检查images镜像文件夹，当前有不被允许的镜像:%s存在!"%(image_id))
					time.sleep(3)
					exit()
				else:
					if aa == "vendor_dlkm":
						flashsingle("reboot fastboot")
						flashsingle("create-logical-partition vendor_dlkm_a")
						flashsingle("create-logical-partition vendor_dlkm_b 0")
						flash("vendor_dlkm_a",position)
					elif aa == "super":
						flash(aa,position)
					else:
						flash(aa+"_ab",position)
			# 设置活动分区
			flashsingle("set_active a")
			# 重启设备 
			print("刷机完成!即将重启设备...")
			time.sleep(3)
			flashsingle("reboot")
			print("刷机完成!30秒后自动退出！")
			time.sleep(30)
			break
		elif sureflash == "N":
			print("取消刷机操作,正在退出程序...")
			time.sleep(3)
			os.system("cls")
			exit()
			break
		else:
			print("输入有误，重新输入！")
def mainchoice_en():
	print('{:=^80}'.format(str1)) 
	print("Please input the Number to select the Flash Plan:")
	print("1.Erofs:\n[RedmiK50(rubens) RedmiK50Pro(matisse) Xiaomi12(cupid) Xiaomi12Pro(zeus)\nXiaomi12X(psyche) XiaomiMIX4(odin) XiaomiCIVI(mona)]")
	print("	") 
	print("2.Vab：\n[XiaomiTablet5ProWifi(elish) Xiaomi11Pro(star) Xiaomi11(venus) Xiaomi11Young(renoir)\nXiaomi10S(thyme) RedmiK40(alioth) RedmiK40Pro(haydn) RedmiK40S(munch)]")
	print("	") 
	print("3.OnlyA：\n[Xiaomi10(umi) Xiaomi10Pro(cmi) Xiaomi10Uitra(cas) Xiaomi10Young(vangogh)\nRedmiK30Pro(lmi) RedmiK30i-5G(picasso) RedmiK30S Plus(apollo)]")
	print('{:=^80}'.format(str1)) 

	while True:
		userchocie = str(input("Enter Number:\n"))
		if userchocie == "1":
			print("You choice:%s，This is Erofs Plan"%(userchocie))
			erofs_en()
			break
		elif  userchocie == "2":
			print("You choice:%s，This is Vab Plan"%(userchocie))
			erofs_en()
			# vab()  通用暂时留空吧
			break
		elif  userchocie == "3":
			print("You choice:%s，This is OnlyA Plan"%(userchocie))
			onlya_en()
			# vab()  通用暂时留空吧
			break
		else:
			os.system("cls")
			print("Error in input, Please re-enter!")
			time.sleep(1)
def erofs_en():
	fixboot_en()
	while True:
		wipeuser = input("Wipe userdata(Y/N):\n")
		if wipeuser == "Y":
			print("Erasing userdata...")
			os.chdir(ospath)
			os.system("fastboot erase metadata")
			os.system("fastboot erase userdata")
			break
		elif  wipeuser == "N":
			print("Cancel Wipe userdata！")
			break
		else:
			print("Error in input, Please re-enter!")
	while True:
		wipedata = input("Wipe DATA Partition(Y/N),Sometimes it may not Boot if it is not wiped.:\n")
		if wipedata == "Y":
			print("Wipe DATA Partition...")
			os.chdir(ospath)
			os.system("fastboot -w")
			break
		elif  wipedata == "N":
			print("Cancel Wipe DATA Partition!")
			break
		else:
			print("Error in input, Please re-enter!")
	while True:
		sureflash =  input("Sure to Flash(Y/N):\n")
		if sureflash == "Y":
			print("I'm Working emmmm...")
			time.sleep(2)
			os.system("cls")
			filelist = os.listdir(imgpath)                                
			print("Gets the following image files:\n%s"%(filelist))
			print("Wait 3s and will start...")
			time.sleep(3)
			# 添加一个防止小白的功能 V3.0版本
			errorimg_list = ['system.img','vendor.img','product.img','odm.img','system_ext.img']
			for image_id in filelist:
				position=imgpath+"\\"+image_id # 镜像文件
				aa=image_id.replace('.img','') # 分区名字
				if image_id in errorimg_list:
					print("Please Check images folder，There are currently disallowed img file:%s found!"%(image_id))
					time.sleep(3)
					exit()
				else:
					if aa == "vendor_dlkm":
						flashsingle("reboot fastboot")
						flashsingle("create-logical-partition vendor_dlkm_a")
						flashsingle("create-logical-partition vendor_dlkm_b 0")
						flash("vendor_dlkm_a",position)
					elif aa == "super":
						flash(aa,position)
					else:
						flash(aa+"_ab",position)
			# 设置活动分区
			flashsingle("set_active a")
			# 重启设备 
			print("Well Bro you are luck! I'm reboot now...")
			time.sleep(3)
			flashsingle("reboot")
			print("Work Done! After 30s and Autoexit！")
			time.sleep(30)
			break
		elif sureflash == "N":
			print("Cancel Flash,i'm planning to escape the earth...Bye,Bro!")
			time.sleep(3)
			os.system("cls")
			exit()
			break
		else:
			print("Error in input, Please re-enter!")





# 程序引导入口
def mainleader():
	global str1
	str1= "===="
	title = "欢迎使用FiimeFlash刷机脚本工具(作者:奥奥)"
	version = "Version:5.0.0"
	web = "官网: https://mi.fiime.cn   技术支持:DXY"
	print('{:=^80}'.format(str1)) 
	print('{: ^70}'.format(title))
	print('{: ^80}'.format(version))
	print("	")
	print('{: ^80}'.format(web))
	print("	")
	print("	")
	print("警告:此脚本仅适用于FiimeDXY,请勿刷写其他官改或官方线刷包!")
	print("正在识别机型...")
	time.sleep(1)
	# 获取code
	getcode()
	if f_code == "":
		mainchoice()
	else:
		pass
def mainleader_en():
	global str1
	str1= "===="
	title = "Welcome to use FiimeFlash(By:Jamine)"
	version = "Version:5.0.0"
	web = "Website: https://mi.fiime.cn   Support:DXY"
	print('{:=^80}'.format(str1)) 
	print('{: ^70}'.format(title))
	print('{: ^80}'.format(version))
	print("	")
	print('{: ^80}'.format(web))
	print("	")
	print("	")
	print("Warning: this script is only applicable to FiimeDXY, do not flash other officer or others package instead")
	print("Identifying model...")
	time.sleep(1)
	# 获取code
	getcode_en()
	if f_code == "":
		mainchoice_en()
	else:
		pass




# V4.3增加语言检测
dll_handle = ctypes.windll.kernel32
sys_lang = hex(dll_handle.GetSystemDefaultUILanguage())
if sys_lang == "0x804":
	lang_get="中文(CN)"
	print("当前目录为:%s"%(path))
	print("当前语言(language):%s"%(lang_get))
	# 检测工作环境		
	binfinder()
	time.sleep(2)
	os.system("cls")
	# 主要引导程序
	mainleader()
elif sys_lang == "0x409":
	lang_get="English(EN)"
	print("ROMPath:%s"%(path))
	print("Your language:%s"%(lang_get))
	# 检测工作环境		
	binfinder_en()
	time.sleep(2)
	os.system("cls")
	# 主要引导程序
	mainleader_en()
else:
	print('无法获取您的计算机语言设置\ncan\'t get your language')
	print("当前目录为:%s"%(path))
	# 检测工作环境		
	binfinder()
	time.sleep(2)
	os.system("cls")
	# 主要引导程序
	mainleader()


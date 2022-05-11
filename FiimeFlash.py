# -*- coding: utf-8 -*-
# @Author: aoao
# @Date:   2022-05-06 11:11:25
# @Last Modified by:   aoao
# @Last Modified time: 2022-05-11 11:01:39

import os
import time
import shutil
import re


path = os.getcwd()
ospath = path + "\\DXY"
imgpath = path + "\\images\\"
boot_patch = path + "\\images\\boot.img"
exe_path = path + '\\lib'

print("当前目录为:%s"%(path))
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
	else:
		print("当前工作环境完整，检测通过!")
		time.sleep(1)
		os.system("cls")
		pass




# 识别机型代码 V4.0
def getcode():
	code = str(path)
	re_code = re.search( r'_[a-z]{3,8}_', code, re.M)
	if re_code:
		f_code = re_code.group().replace("_","")
		devicelist = {'matisse':'红米K50 Pro','rubens':'红米K50','munch':'红米K40S','zeus':'小米12 Pro','cupid':'小米12','psyche':'小米12X','mona':'小米CIVI','elish':'小米平板5 Pro (WiFi)','odin':'小米MIX4','renoir':'小米11 青春版','star':'小米11 Pro / Ultra','thyme':'小米10S','haydn':'红米K40Pro/Pro+/小米11i','alioth':'红米K40 / POCO F3','venus':'小米11','apollo':'红米K30S 至尊纪念版/小米10T/10T','cas':'小米10Uitra','vangogh':'小米10青春版','lmi':'红米K30 Pro/变焦版/POCO F2 Pro','cmi':'小米10Pro','umi':'小米10','picasso':'红米K30 5G/红米K30i 5G'}
		devicename = devicelist[f_code]
		print(devicename)
		alist = ["rubens","matisse","cupid","zeus","psyche","odin","mona"]
		blist = ['elish','star','venus','renoir','thyme','alioth','haydn','munch']
		clist = ['umi','cmi','cas','vangogh','lmi','picasso','apollo']
		if f_code in alist:
			print("当前识别到代号为:%s,机型为:%s,类型为:Erofs机型"%(f_code,devicename))
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				erofs()
			elif sure == 'N':
				print("已经取消...")
				pass
			else:
				pass
		elif f_code in blist:
			print("当前识别到代号为:%s,机型为:%s,类型为:VAB机型"%(f_code,devicename))
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				erofs()
			elif sure == 'N':
				print("已经取消...")
				pass
			else:
				pass
		elif f_code in clist:
			print("当前识别到代号为:%s,机型为:%s,类型为:OnlyA机型"%(f_code,devicename))
			sure = input("识别是否准确?(Y/N):\n")
			if sure == 'Y':
				print("开始刷机...")
				onlya()
			elif sure == 'N':
				print("已经取消...")
				pass
			else:
				pass
		else:
			print("无法识别当前机型！")
			pass

	else:
		print("未识别到机型,请手动选择")
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




# 程序引导入口
def mainleader():
	str1= "===="
	title = "欢迎使用FiimeFlash刷机脚本工具(作者:奥奥)"
	version = "Version:3.0.0"
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
	if f_code == null:
		print('{:=^80}'.format(str1)) 
		print("请输入对应的\"数字\"指令选择机型进行刷机操作:")
		print("1.Erofs机型:\n[红米K50(rubens) 红米K50Pro(matisse) 小米12(cupid) 小米12Pro(zeus)\n小米12X(psyche) 小米MIX4(odin) 小米CIVI(mona)]")
		print("	") 
		print("2.Vab机型：\n[小米平板5ProWifi(elish) 小米11Pro(star) 小米11(venus) 小米11青春版(renoir)\n小米10S(thyme) 红米K40(alioth) 红米K40Pro(haydn) 红米K40S(munch)]")
		print("	") 
		print("3.OnlyA机型：\n[小米10(umi) 小米10Pro(cmi) 小米10Uitra(cas) 小米10青春版(vangogh)\n红米K30Pro(lmi) 红米K30i-5G(picasso) 红米K30S 至尊纪念版(apollo)]")
		print('{:=^80}'.format(str1)) 

		while True:
			userchocie = int(input("请输入数字指令:\n"))
			if userchocie <= 0 or userchocie > 3:
				print("输入有误,请重新输入!")

			else:
				if userchocie == 1:
					print("您选择了:%s，这是Erofs机型"%(userchocie))
					erofs()
					break
				elif  userchocie == 2:
					print("您选择了:%s，这是Vab机型"%(userchocie))
					erofs()
					# vab()  通用暂时留空吧
					break
				elif  userchocie == 3:
					print("您选择了:%s，这是OnlyA机型"%(userchocie))
					onlya()
					# vab()  通用暂时留空吧
					break
				else:
					os.system("cls")
					print('程序异常，正在退出...')
					time.sleep(3)
					exit()
	else:
		pass









# # 检测工作环境		
# binfinder()
# time.sleep(2)
# os.system("cls")
# # 主要引导程序
# mainleader()

getcode()
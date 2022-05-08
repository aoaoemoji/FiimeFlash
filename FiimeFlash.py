# -*- coding: utf-8 -*-
# @Author: aoao
# @Date:   2022-05-06 11:11:25
# @Last Modified by:   aoao
# @Last Modified time: 2022-05-09 00:18:09

import os
import time



path = os.getcwd()
ospath = path + "\\DXY"
imgpath = path + "\\images\\"

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




# 刷机方法调用
def flash(filepath,imgfile):
	os.chdir(ospath)
	os.system("fastboot.exe flash" + " " + filepath + " " + imgfile)

def flashsingle(order):
	os.chdir(ospath)
	os.system("fastboot.exe "+ " " + order)



# 开始刷机脚本调用
def vab():
	pass

def onlya(): # 新增onlya刷机方案 3.0版本
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









# 检测工作环境		
binfinder()
time.sleep(2)
os.system("cls")
# 主要引导程序
mainleader()
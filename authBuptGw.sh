#!/bin/bash

#-----------------------------------------#
# siwind 编写。QQ: 35949934
#
#
# 2013-05-07: fix
#    1) add URL_RELOGIN to disconnect other user in another location!
#
#
#-----------------------------------------#

#用户名及密码设置
USERNAME=2019140067
PASSWD=257716

URL_LOGIN=http://gw.bupt.edu.cn/login
URL_LOGOUT=http://gw.bupt.edu.cn/logout

# NGW_LINE: CUC-BRAS, CMCC-BRAS, CT-BRAS, __none__ for default, [empty] for original gateway (use mode 211 instead)
NGW_LINE=__none__


#------------#
#
#
#-----------#
#cmd1="curl ${URL_LOGIN} --data "user=${USERNAME}&pass=${PASSWORD}&line=${NGW_LINE}""

login()
{
	echo login...
    cmd="curl --silent ${URL_LOGIN} --data \"user=${USERNAME}&pass=${PASSWD}&line=${NGW_LINE}\" > /dev/null"
    #echo $cmd
    eval $cmd

    #cmd=$URL_LOGIN
	#eval $cmd
	echo login OK!
}

logout()
{
	echo logout...
	RESULT=`curl --silent "$URL_LOGOUT"`
	echo logout OK!
}

usage()
{	
    echo "Usage: $0 [-i|-o] "
	echo "where:     -i login to bupt school network"
	echo "           -o logout from bupt school network"
	echo 
	exit
}

if [ $# -lt 1 ] ; then
	usage
	exit
fi

case $1 in
-i)
    login;;
-o)
    logout;;
*)
	usage;;
esac

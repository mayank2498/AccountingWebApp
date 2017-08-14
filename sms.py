import requests
def send_sms(mobile,msg,sender="CodeNy"):
	authkey= "125195AnE7snTWFepK5925ea7c"
	url='http://api.msg91.com/api/sendhttp.php?authkey='+authkey+'&mobiles='
	url+=mobile
	url+='&message='+msg
	url+='&sender='+sender+'&route=4'
	print(requests.request('GET', url))
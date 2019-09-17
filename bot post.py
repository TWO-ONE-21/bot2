import mechanize
import time,sys,os

br = mechanize.Browser()
br = 0

#BROWSER
import cookielib,re,urllib2,urllib,threading
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_cookiejar(cookielib.LWPCookieJar())
br.set_handle_redirect(True)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0')]
os.system('clear')

class w():
    m = '\033[31m'
    k = '\033[32m'
    h = '\033[33m'
    b = '\033[34m'

def buka(link):
	try:
		x = br.open(link)
		br._factory.is_html = True
		x = x.read()
	except:
		print (w.m + "[!]Periksa koneksi internet anda")
		sys.exit()
	if '<link rel="redirect" href="' in x:
		return buka(br.find_link().url)
	else:
		return x

def pilihan():
    pilih = raw_input(w.b+'Apakah anda ingin mencoba lagi? [Y/N] '+w.h)
    pilih = pilih.upper()
    if pilih == 'Y':
        print (w.h+'[!] Login ulang')
        return login()
    elif pilih != 'Y' and pilih != 'N':
        print(w.m+'[!] Masukkan pilihan yang benar!!')
        return pilihan()
    else:
        print(w.m+'[!] Keluar')
        sys.exit()

def login():
        Email = raw_input(w.k+'[?] Email: '+w.b)
        Password = raw_input(w.k+'[?]Password: '+w.b)
        br.open('https://facebook.com')
        br.select_form(nr=0)
        br.form['email'] = Email
        br.form['pass'] = Password
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            print(w.h+'[!] Berhasil Login!!')
        elif 'checkpoint' in url:
            print(w.k+'[!] Akun anda checkpoint,\nHarap login dan konfirmasikan identitas anda. ')
            pilihan()
        else:
            print(w.m+'[!] Email/Password anda salah!!')
            pilihan()
def eksekusi():
    ID = raw_input(w.k+'Apakah anda telah mengumpulkan ID sebelumnya? [Y/N] '+w.h)
    ID = ID.upper()
    if ID == 'Y':
        post()
    elif ID != 'Y' and ID != 'N':
        print (w.m+'[!] Masukkan pilihan yang benar!!')
        return eksekusi()
    else:
        id() 

IdTeman = []        
def id_terkumpul(r):
	for i in re.findall(r'/friends/hovercard/mbasic/\?uid=(.*?)&',r):
		IdTeman.append(i)

def id():
	print w.k + 'Mengumpulkan id teman...'
	id_terkumpul(buka('https://m.facebook.com/friends/center/friends/?fb_ref=fbm&ref_component=mbasic_bookmark&ref_page=XMenuController'))
	next = br.find_link(url_regex='friends_center_main').url
	try:
		next
	except:
		if len(IdTeman) != 0:
			print w.h + '\nBerhasil mengumpulkan' + w.k + str(len(IdTeman)) + w.h + " ID Teman"
		else:
			sys.exit()
	while 1:
		id_terkumpul(buka(next))
		print w.b + str(len(IdTeman)) + w.h + ' ID terambil'
		sys.stdout.flush()
		try:
			next = br.find_link(url_regex='friends_center_main').url
		except:
			print w.k + '\nBerhasil mengumpulkan ' + w.m + str(len(IdTeman)) + w.k + ' ID Teman'
			break
	if len(IdTeman) != 0:
		print w.k + "Menyimpan ID teman"
		File = 0
		try:
			open(os.sys.path[0]+'/id.txt','w').write('\n'.join(IdTeman))
			print w.h + 'Berhasil menyimpan ID teman'
			File += 1
		except:
			print w.m + 'Gagal menyimpan'
		if File == 1:
			post()
		else:
			sys.exit()

def post():
    try:
        teman = open(os.sys.path[0]+'/id.txt', 'r')
    except:
        print (w.m+'[!] Anda belum mengumpulkan ID,\nHarap mengumpulkan ID terlebih dahulu!!')
        id()
    temaN = teman.readlines()
    teman.close()
    postingan = raw_input(w.h+'Tulis Postingan: '+w.k)
    terkirim = 0
    for i in temaN:
        buka('https://mbasic.facebook.com/profile.php?id='+i)
        br.select_form(nr=1)
        br.form['xc_message'] = postingan
        br.submit()
        terkirim += 1
        namanya = br.find_link(url_regex='?lst=').text
        url = br.geturl()
        if 'checkpoint' in url:
            print(w.m+'Akun anda checkpoint....')
        else:
            print (w.m+terkirim+w.h+'. terkirim ke '+w.m+namanya)
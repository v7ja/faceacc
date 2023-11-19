from rich.console import Console
from rich.table import Table
import time
from rich import print as L7N
from pystyle import *

O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
print(O+'')
table = Table(title="Tools Check instagram Email",style="red")
table.add_column("The Tool By : 𝐋7𝐍 «𓆩ᶠᴮᴵ𓆪» ™",style='red')
table.add_row("My User : @g_4_q",style='green')
table.add_row("My Channel : @Topython",style='Cyan')
table.add_row("My Channel 2 : @ZZKGZ",style='yellow')
console = Console()
console.print(table)
L7n = Console()
id = input(O+' -Enter ID Facebook :  : ')
print('\n')
token = input(O+' -Enter Token Facebook : ')
print('  '*10)
from gdolib import *
def L7N_inf_ACC_FC():
	
	phone = info_face.phone(id,token)
	name = info_face.name(id,token)
	frineds = info_face.friends(id,token)
	birthday = info_face.birthday(id,token)
	gander = info_face.gender(id,token)
	username = info_face.username(id,token)
	email = info_face.email(id,token)
	bio = info_face.bio(id,token)
	followers = info_face.followers(id,token)
	location = info_face.location(id,token)
	print(B+f"""

-Name : {name}
-Username : {username}
-Email : {email}
-Phone : {phone}
-Followers : {followers}
-Gender : {gander}
-Frinds : {frineds}
-Birthday : {birthday}
-Location : {location}
-Bio : {bio}

		""")
with L7n.status(B+'please wait !  ',spinner_style='point'):
        time.sleep(3)
L7N_inf_ACC_FC()

# simpleftp_py
# ftp
#p ftppy
pip install pyftpdlib

Simple python ftp script with configuration (config.json)

EN 🔐 FTP Permissions in pyftpdlib
Letter	Name	Allows the user to...
e	change directory	Change directories (CWD command)
l	list files	List files and folders (LIST, NLST)
r	retrieve files	Download files from the server (RETR)
a	append to files	Append data to an existing file (APPE)
d	delete files/folders	Delete files or directories (DELE, RMD)
f	rename files/folders	Rename files or directories (RNFR, RNTO)
m	make directories	Create new directories (MKD)
w	write/upload files	Upload files to the server (STOR)
M	change file mode	Change file permissions (SITE CHMOD) (UNIX)
T	change timestamps	Change file modification time (MFMT)

FULL PERM: elradfmwMT

PL 🔐 Lista uprawnień (permissions):
Litera	Znaczenie	Co pozwala robić
e	change directory	Zmieniać katalog (komenda CWD)
l	list files	Wyświetlać listę plików (LIST, NLST)
r	retrieve files	Pobierać pliki (RETR)
a	append to files	Dopisywać dane do pliku (APPE)
d	delete files/dirs	Usuwać pliki i katalogi (DELE, RMD)
f	rename files/dirs	Zmieniać nazwy plików/katalogów (RNFR, RNTO)
m	create dirs	Tworzyć nowe katalogi (MKD)
w	store (write/upload)	Wysyłać pliki na serwer (STOR)
M	change mode	Zmieniać uprawnienia (chmod – tylko UNIX, nie zawsze działa)
T	change timestamp	Zmieniać datę/godzinę pliku (komenda MFMT)

Wszystkie uprawienia: elradfmwMT

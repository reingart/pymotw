=============================
pwd -- Unix Password Database
=============================

.. module:: pwd
    :synopsis: Unix Password Database

:Purpose: Read user data from Unix password database.
:Available In: 1.4 and later

The pwd module can be used to read user information from the Unix
password database (usually ``/etc/passwd``).  The read-only interface
returns tuple-like objects with named attributes for the standard
fields of a password record.

===== ========= =======
Index Attribute Meaning
===== ========= =======
 0    pw_name   The user's login name
 1    pw_passwd Encrypted password (optional)
 2    pw_uid    User id (integer)
 3    pw_gid    Group id (integer)
 4    pw_gecos  Comment/full name
 5    pw_dir    Home directory
 6    pw_shell  Application started on login, usually a command interpreter
===== ========= =======

Querying All Users
==================

Suppose you need to print a report of all of the "real" users on a
system, including their home directories (for our purposes, "real" is
defined as having a name not starting with "``_``").  To load the
entire password database, you would use ``getpwall()``.  The return
value is a list with an undefined order, so you will need to sort it
before printing the report.

.. include:: pwd_getpwall.py
    :literal:
    :start-after: #end_pymotw_header

Most of the example code above deals with formatting the results
nicely.  The ``for`` loop at the end shows how to access fields from
the records by name.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pwd_getpwall.py'))
.. }}}

::

	$ python pwd_getpwall.py
	
	User                UID Home Dir                    Description
	------------------ ---- --------------------------- ------------------------------
	avahi               111 /var/run/avahi-daemon       Avahi mDNS daemon,,,
	avahi-autoipd       105 /var/lib/avahi-autoipd      Avahi autoip daemon,,,
	backup               34 /var/backups                backup
	bin                   2 /bin                        bin
	colord              113 /var/lib/colord             colord colour management daemon,,,
	daemon                1 /usr/sbin                   daemon
	dnsmasq             104 /var/lib/misc               dnsmasq,,,
	festival            116 /home/festival              
	games                 5 /usr/games                  games
	gnats                41 /var/lib/gnats              Gnats Bug-Reporting System (admin)
	hplip               114 /var/run/hplip              HPLIP system user,,,
	irc                  39 /var/run/ircd               ircd
	kernoops            106 /                           Kernel Oops Tracking Daemon,,,
	libuuid             100 /var/lib/libuuid            
	libvirt-dnsmasq     119 /var/lib/libvirt/dnsmasq    Libvirt Dnsmasq,,,
	libvirt-qemu        118 /var/lib/libvirt            Libvirt Qemu,,,
	lightdm             112 /var/lib/lightdm            Light Display Manager
	list                 38 /var/list                   Mailing List Manager
	lp                    7 /var/spool/lpd              lp
	mail                  8 /var/mail                   mail
	man                   6 /var/cache/man              man
	messagebus          102 /var/run/dbus               
	news                  9 /var/spool/news             news
	nobody             65534 /nonexistent                nobody
	postgres            117 /var/lib/postgresql         PostgreSQL administrator,,,
	proxy                13 /bin                        proxy
	pulse               115 /var/run/pulse              PulseAudio daemon,,,
	reingart           1000 /home/reingart              Mariano Reingart,,,
	root                  0 /root                       root
	rtkit               107 /proc                       RealtimeKit,,,
	saned               108 /home/saned                 
	speech-dispatcher   110 /var/run/speech-dispatcher  Speech Dispatcher,,,
	sync                  4 /bin                        sync
	sys                   3 /dev                        sys
	syslog              101 /home/syslog                
	usbmux              103 /home/usbmux                usbmux daemon,,,
	uucp                 10 /var/spool/uucp             uucp
	whoopsie            109 /nonexistent                
	www-data             33 /var/www                    www-data

.. {{{end}}}


Querying User By Name
=====================

If you need information about one user, it is not necessary to read
the entire password database.  Using ``getpwnam()``, you can retrieve
the information about a user by name.

.. include:: pwd_getpwnam.py
    :literal:
    :start-after: #end_pymotw_header

The passwords on my system are stored outside of the main user
database in a shadow file, so the password field, when set, is
reported as all ``*``.

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pwd_getpwnam.py $USER'))
.. cog.out(run_script(cog.inFile, 'pwd_getpwnam.py nobody', include_prefix=False))
.. }}}

::

	$ python pwd_getpwnam.py $USER
	
	Username: reingart
	Password: x
	Comment : Mariano Reingart,,,
	UID/GID : 1000 / 1000
	Home    : /home/reingart
	Shell   : /bin/bash

	$ python pwd_getpwnam.py nobody
	
	Username: nobody
	Password: x
	Comment : nobody
	UID/GID : 65534 / 65534
	Home    : /nonexistent
	Shell   : /usr/sbin/nologin

.. {{{end}}}


Querying User By UID
====================

It is also possible to look up a user by their numerical user id.
This is useful to find the owner of a file:

.. include:: pwd_getpwuid_fileowner.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pwd_getpwuid_fileowner.py'))
.. }}}

::

	$ python pwd_getpwuid_fileowner.py
	
	pwd_getpwuid_fileowner.py is owned by reingart (1000)

.. {{{end}}}


The numeric user id is can also be used to find information about the
user currently running a process:

.. include:: pwd_getpwuid_process.py
    :literal:
    :start-after: #end_pymotw_header

.. {{{cog
.. cog.out(run_script(cog.inFile, 'pwd_getpwuid_process.py'))
.. }}}

::

	$ python pwd_getpwuid_process.py
	
	Currently running with UID=1000 username=reingart

.. {{{end}}}


.. seealso::

    `pwd <http://docs.python.org/library/pwd.html>`_
        The standard library documentation for this module.

    :mod:`spwd`
        Secure password database access for systems using shadow passwords.

    :mod:`grp`
        The :mod:`grp` module reads Unix group information.

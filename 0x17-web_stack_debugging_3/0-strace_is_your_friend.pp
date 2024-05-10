#A script fixing apache 500 error
exec { 'fix-wordpress':
	command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/\
/var/www/html/wp-settings.php',
	path => '/usr/bin:usr/sbin:bin',
	subscribe => File['/var/www/html/wp-settings.php'],
}

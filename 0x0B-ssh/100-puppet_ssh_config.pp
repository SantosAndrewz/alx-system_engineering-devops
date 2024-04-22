#A script using puppet to make changes in the configuration file.

file_line {'no password allowed':
path => '/etc/ssh/ssh_config',
line => ' PasswordAuthentification no',
replace => true
}

file_line {'privite key accepted':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school',
replace => true
}

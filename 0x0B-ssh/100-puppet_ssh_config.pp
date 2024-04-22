#A script using puppet to make changes in the configuration file.

file_line {'no password allowed':
path => '/root/.ssh/config',
line => ' PasswordAuthentification no',
replace => true
}

file_line {'privite key accepted':
path => '/root/.ssh/config',
line => 'IdentityFile ~/.ssh/school',
replace => true
}

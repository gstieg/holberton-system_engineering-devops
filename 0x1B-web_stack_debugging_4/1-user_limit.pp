#fix OS config
exec { 'fix config':
  command => "/bin/sed -i 's/nofile 5000/g' /etc/security/limits.conf"
}

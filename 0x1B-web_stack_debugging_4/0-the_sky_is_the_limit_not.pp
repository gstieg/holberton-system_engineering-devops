#fix limit request limit
exec { 'change request limit':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx ; service nginx restart",
}

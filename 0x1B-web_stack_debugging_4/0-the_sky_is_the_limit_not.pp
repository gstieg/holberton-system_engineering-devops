#fix limit request limit
exec { 'change request limit':
  path => "/bin/sed -i 's/15/5000/g' /etc/default/nginx ; service nginx restart",
}

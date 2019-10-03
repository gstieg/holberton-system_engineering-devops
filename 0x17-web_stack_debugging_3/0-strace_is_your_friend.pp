#fix and debug apache
exec { 'php':
  command => "/bin/sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}

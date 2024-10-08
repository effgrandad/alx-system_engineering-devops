# fix nginx to accept and serve more requests

# boost ULIMIT and restart nginx
exec {'modify max open files limit setting':
  command => 'sed -i "s/15/5000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

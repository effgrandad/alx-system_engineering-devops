# Modify the OS configuration to enable the holberton user to log in
# and open files without receiving an error notice.
# boost limit and soft limit

exec {'OS security config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}

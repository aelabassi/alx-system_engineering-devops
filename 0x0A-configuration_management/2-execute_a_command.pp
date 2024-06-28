# A manifest to a kill a shell process named killmenow
exec {'pkill':

  command  => 'pkill killmenow',
  provider => 'shell'
}


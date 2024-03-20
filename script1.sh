sys=$(arch)
pro=$(nproc)
mem=$(free -m)
you=$(whoami)
mac=$(ip link | grep "link/ether"| awk '{print $2}')
las=$(uptime -s)
echo "Arquitetura: $sys"
echo "Numero de prosessadores: $pro"
echo "Memoria ram: $mem"
echo "Mac adress: $mac"
echo "ultimo reboot: $las"
echo "usuario: $you"

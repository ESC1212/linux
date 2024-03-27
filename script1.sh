sys=$(arch)
pro=$(nproc)
mem=$(free -m)
you=$(whoami)
mac=$(ip link | grep "link/ether"| awk '{print $2}')
las=$(uptime -s)
echo "Arquitetura: $sys"
echo "Numero de processadores: $pro"
echo "Memoria ram: $mem"
echo "Mac address: $mac"
echo "ultimo reboot: $las"
echo "usuario: $you"

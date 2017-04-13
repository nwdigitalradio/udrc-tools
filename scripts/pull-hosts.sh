cd /tmp
curl -o DCS_Hosts.txt http://ar-dns.net/dcs
curl -o DExtra_Hosts.txt http://ar-dns.net/dextra-gw
curl -o DPlus_Hosts.txt http://ar-dns.net/dplus-gw
for hosts in DCS_Hosts.txt DExtra_Hosts.txt DPlus_Hosts.txt
do
	if grep -Fq "# Prepared at ar-dns.net" "$hosts" 
	then 
		echo "Copying $hosts"
		sudo cp "$hosts" /usr/share/opendv
	else 
		echo "$hosts Bad, not copied"
	fi
	rm "$hosts"
done
echo "Restart ircddbgateway to use new files ..."

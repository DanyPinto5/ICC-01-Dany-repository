#!/bin/bash
echo
echo ### Network Tool ###
echo
echo "escolha um numero"
echo "1) check network interface information"
echo "2) ping a host"
echo "3) Port Scan with Nmap"
echo "4) display routing table"
echo "5) traceroute to host"
echo "6) exit"

read numero

case $numero in
	"1")
		echo "check network interface information"
		ifconfig
	;;
	"2")
		echo "put the host to ping"
		read host
		ping -c 4 $host
	;;
	"3")
		echo "put the port scan with Nmap"
		read host
		nmap -p $host
	;;
	"4")
		echo "Display Routing Table"
		route -n
	;;
	"5")
		echo "traceroute to host"
		read host
		traceroute $host
	;;
	"6")
		echo "exit"
	;;
	esac



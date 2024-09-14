#!/usr/bin/python3
from scapy.all import Ether,ARP,srp
from optparse import OptionParser
def whatip(ip_ring,cont):
    try:
        print("""
        __        ___   _    _  _____ ___ ____  
        \ \      / / | | |  / \|_   _|_ _|  _ \ 
         \ \ /\ / /| |_| | / _ \ | |  | || |_) |
          \ V  V / |  _  |/ ___ \| |  | ||  __/ 
           \_/\_/  |_| |_/_/   \_\_| |___|_|    
        ----------------------------------------                               
        Developed by: Ibrahem abo kila
        """)
        ring=[]
        ether_heeader = Ether(dst="FF:FF:FF:FF:FF:FF")
        cont=int(cont)
        for i in range(2,cont):
            ip_ring=ip_ring[:0]+ip_ring[:10]+str(i)
            arp_option= ARP(pdst=ip_ring)
            arp_packet= ether_heeader / arp_option
            print(arp_packet)
            result , noresult = srp(arp_packet,timeout=3)
            for send , recive in result:
                h=recive[Ether].psrc
                print(h)
                ring.append(h)
        print("""
         __        ___   _    _  _____ ___ ____  
         \ \      / / | | |  / \|_   _|_ _|  _ \ 
          \ \ /\ / /| |_| | / _ \ | |  | || |_) |
           \ V  V / |  _  |/ ___ \| |  | ||  __/ 
            \_/\_/  |_| |_/_/   \_\_| |___|_|    
                                            
                            
        ------------------------------------------
        Developed by: Ibrahem abo kila
        """)
        
        print("--",len(ring),"devices found::")
        for i in ring:
                print(">>",i)
    except Exception as e:
         print(e)

pars=OptionParser("""
    __        ___   _    _  _____ ___ ____  
    \ \      / / | | |  / \|_   _|_ _|  _ \ 
     \ \ /\ / /| |_| | / _ \ | |  | || |_) |
      \ V  V / |  _  |/ ___ \| |  | ||  __/ 
       \_/\_/  |_| |_/_/   \_\_| |___|_|    
                                       
                        
    -----------------------------------------
sudo whatip -r 192.168.1.1 -c 20
Developed by: Ibrahem abo kila
""")
pars.add_option("-r",dest="r_ip")
pars.add_option("-c",dest="c_ip")
(options,args)=pars.parse_args()
if options.r_ip==None:
    print(pars.usage)
elif options.c_ip==None:
    print(pars.usage)
else:
    whatip(options.r_ip,options.c_ip)


#!/usr/bin/python

'Setting the position of nodes'

from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.wifi.cli import CLI_wifi
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.net import Mininet_wifi



    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP
  link=wmediumd, wmediumd_mode=interference,
                        configure4addr=True, autoAssociation=False )
    info("*** Creating nodes\n")
                   
    net.addStation('sta1', mac='00:00:00:00:00:02', ip='10.0.0.1/8',
                   position='30,30,0')
    net.addStation(''sta2', mac='00:00:00:00:00:02', ip='10.0.0.2/8',
                   position='30,40,0')

    net.addStation('sta3', mac='00:00:00:00:00:02', ip='10.0.0.3/8',
                   position='30,30,0')
    net.addStation('sta4', mac='00:00:00:00:00:02', ip='10.0.0.4/8',
                   position='30,70,0')


    ap1 = net.addAccessPoint('ap1', ssid='new-ssid', mode='g', channel='1',
    ap1 = net.addAccessPoint('ap2', ssid='new-ssid', mode='g', channel='1',

                             position='50,50,0')

    net.propagationModel(model="logDistance", exp=4.5


    c1 = net.addController('c1', controller=Controller)

    h1 = net.addHost('h1', ip='10.0.0.3/8')
    h1 = net.addHost('h2', ip='10.0.0.5/8')


    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()
    net.addLink(ap1, h1)

    

    info("*** Running CLI\n")
    CLI_wifi(net)
    ap1.start([c1])
    ap2.start([c1])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Running CLI\n")
    CLI_wifi(net)
    net.addLink(ap2, h2)



    info("*** Creating links\n")
    net.plotGraph(max_x=100, max_y=100)

    info("*** Starting network\n")
    net.build()
    c1.start()

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()

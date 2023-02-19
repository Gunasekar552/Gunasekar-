import nmap
from termcolor import colored
import os
from pythonping import ping

check = nmap.PortScanner()

print(colored(" Welcome To TONY ", 'green'))

print(colored("""
       ................................................................................................
        _____________________________________________________________________________________________
       |      __________    _______                                                                  |
       |      ````||````   |       |    |||    |     \\      //                                       |
       |          ||       |       |    |  |   |      \\    //                                        |
       |          ||       |       |    |   |  |       \\  //                                         |
       |          ||       |       |    |    | |        \\//                                          |
       |          ||       |_______|    |    |||        //                                           |
       |                                               //                                            |
       |_____________________________________________________________________________________________|
       ................................................................................................ """, 'red',
              attrs=['bold']))

print(' ')

print(colored(' Enter --->> [ping]  for Checking  Host Is Active Or Not  ', 'green'))
print(" ")
print(colored(' Enter --->> [scan]  for Port Scanner  ', 'green'))
print(" ")
print(colored(' Enter --->> [Test]  For Testing   ', 'red'))
print(" ")
operate = str(input('  --->> '))
print(" ")

if operate == 'ping':

    print(colored('Starting Ping', 'green'))
    print(" ")
    ip = input('Enter Ip Address Or Domain Name --->> ')
    print(" ")
    pin = int(input('''Enter [0] To Ping Entire Network  [Only for Ip] |\nEnter [1] To Ping Given Ip Or Domain Name --->> '''))

    if pin == 0:
        dot = ip.rfind(".")
        Ip = ip[0:dot + 1]

        for i in range(1, 256):
            host = Ip + str(i)
            response = os.system('ping  -n 1 -w 1 ' + host + '>nul')
            if response == 0:
                print(colored(" Host --->> " + host + " is Active", 'green'))
            else:
                print(colored(" Host --->> " + host + " is Not Active",'red'))
    else:
        result = ping(ip)
        if not result:
            print(colored(" Host --->> " + ip + " is Not Active", 'red'))
        else:
            print(colored(" Host --->> " + ip + " is  Active", 'green'))


elif operate == 'scan':

    print(colored('Starting Port Scanner', 'green'))

    ip = input('Enter Ip Address ---> ')

    ask = int(input('Type [0] For Default Vulnerable Ports And Type [1] For Custom Ports ---> '))
    if ask == 0:
        ports = [7, 19, 20, 21, 22, 23, 25, 37, 53, 69, 79, 80, 110, 111, 135, 137, 138, 139, 445, 161, 443, 512,
                 513,
                 514, 993, 995, 1433, 1723, 3306, 3389, 4444, 5900, 8080]
        print('Given Ip Address --->> ' + ip, 'Ports  --->> ' + str(ports))
        check.scan(ip, str(ports))

        print('Mac Address Found --->> ', check[ip]['addresses']['mac'])

        print('----------------------------------------------------------------')

        print('Mac Address And Vendor Name --->> ', check[ip]['vendor'])

        print(" ")

        print('Host Is --->> ', check[ip].state())

        if check[ip].state() == 'up':

            print(check.command_line())

            print('----------------------------------------------------------------')

            for proto in check[ip].all_protocols():
                print('Protocol Found --->> ' + proto)

                for port in ports:

                    Port = int(port)
                    try:

                        result = check[ip][proto][Port]['state']

                        if result == 'open':
                            print(colored('Port ' + str(port) + ' is open', 'green'))

                        elif result == 'closed':
                            print(colored('Port ' + str(port) + ' is Closed', 'red'))

                        else:
                            print(colored('Port ' + str(port) + ' is Filtered','yellow'))
                    except KeyError:
                        print('Port ', port, 'is closed ')
                        continue
        else:
            print(colored('Host Seems to be Down Or Not Reachable', 'yellow'))

    else:
        start = input('Enter Beginning Port --->> ')
        initial = int(start)

        end = input('Enter Ending Port --->> ')
        final = int(end)

        print('Given Ip Address --->> ' + ip, 'Given Port Range --->> ' + start + "-" + end)

        check.scan(ip, start, end)

        print('Mac Address Found --->> ', check[ip]['addresses']['mac'])

        print("----------------------------------------------------------")

        print('Mac Address And Vendor Name --->> ', check[ip]['vendor'])

        print(" ")

        print('Host Is --->> ', check[ip].state())

        if check[ip].state() == 'up':

            print(check.command_line())

            for proto in check[ip].all_protocols():
                print(proto)

                for i in range(initial, final):                   
                    Port = int(i)
                    try:  

                         result = check[ip][proto][Port]['state']      

                         if result == 'open':

                             print(colored('Port ' + str(Port) + ' is open', 'green'))

                         elif result == 'closed':

                             print(colored('Port ' + str(Port) + ' is Closed', 'red'))
                         else:

                             print(colored('Port ', Port, 'is Filtered', "yellow"))   

                    except KeyError:
                        print('Port ', Port, 'is closed')
                        print(result)
                        continue
                                         
        else:
            print(colored('Host Seems to be Down Or Not Reachable',"yellow"))

import winrm
with open('cred_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        IP_address=line.split("|")[0]
        user=line.split("|")[1]
        passw=line.split("|")[2].split("\n")[0]
        print(IP_address,"-",user,"-",passw,"-")
        winrm_session = winrm.Session(IP_address, auth=(user, passw))
        try:
            print("IP Configuration:")
            result = winrm_session.run_cmd('ipconfig', ['/all'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Users:")
            result = winrm_session.run_cmd('net', ['user'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Groups:")
            result = winrm_session.run_cmd('net', ['localgroup'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Tasks:")
            result = winrm_session.run_cmd('tasklist', ['/svc'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Services:")
            result = winrm_session.run_cmd('net', ['start'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Task Scheduler:")
            result = winrm_session.run_cmd('schtasks')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Registry Control:")
            result = winrm_session.run_cmd('reg',['query','HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Active TCP & UDP ports:")
            result = winrm_session.run_cmd('netstat', ['-ano'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("File sharing:")
            result = winrm_session.run_cmd('net', ['view'])
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Files:")
            result = winrm_session.run_cmd('forfiles /D -10 /S /M *.exe /C "cmd /c echo @ext @fname @fdate"')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Firewall Config:")
            result = winrm_session.run_cmd('netsh firewall show config')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Sessions with other Systems:")
            result = winrm_session.run_cmd('net use')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Open Sessions:")
            result = winrm_session.run_cmd('net session')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
        try:
            print("Log Entries:")
            result = winrm_session.run_cmd('wevtutil qe security')
            for result_line in result.std_out.decode('ascii').split("\r\n"):
                print(result_line)
        except:
            pass
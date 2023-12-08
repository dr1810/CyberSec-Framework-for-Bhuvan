#This Program is used to extract the server data from the packet sniffer
server = open("C:\\Users\\dharu\\OneDrive\\Desktop\\ISROSpaceHackathon\\ssl_access.txt") #Loads the sever text file
con_server = server.readlines()
cols = ['ip_address', 'identd', 'user', 'timestamp', 'method', 'url', 'protocol', 'status', 'size', 'referer', 'user_agent']
data = []
for i in range(len(con_server)):
    match = pattern.match(log_entry)
    if match:
        values = [match.group('ip'), None, None, match.group('timestamp'), match.group('method'), match.group('url'),
                  match.group('protocol'), match.group('status'), match.group('size'), match.group('referer'), match.group('user_agent')]
        data.append(values)
df = pd.DataFrame(data)
df.columns = cols #Sets the columns for the dataframe
df = df.drop(["user","identd","referer"],axis = 1) #Drops the columns which are not needed
df.to_csv("C:/Users/dharu/OneDrive/Desktop/ISROSpaceHackathon/server_log_data.csv",index = False) #Converts the data to .csv format
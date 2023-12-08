#This program is for extracting the firewall data from the Packet Sniffer
file = open("C:/Users/dharu/OneDrive/Desktop/ISROSpaceHackathon/topic04/firewall logs/31Oct2023-messages.txt")
content = file.readlines() #This loads the data from the .txt file from the packet sniffer
columns = []
for j in range(len(content)):
    dt = {}
    for i in content[j].split():
        if '=' in i:
            new = i.split('=')
            dt[new[0]] = new[1]
    columns.append(dt)
new = pd.DataFrame(columns) #Creates the new dataframe
new.to_csv("C:/Users/dharu/OneDrive/Desktop/ISROSpaceHackathon/firewall.csv",index = False) #Converts the data to a csv format
file.close() #Closes the text file after data extraction
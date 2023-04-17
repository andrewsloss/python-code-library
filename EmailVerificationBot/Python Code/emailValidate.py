import getEmail

global tld_real
tld_real = False

def get_TLD():
    global all_TLD
    TLD_file = open('C:/Users/andre/OneDrive/Documents/GitHub/Email-Verification-Discord-Bot/MVP Base Code/domainExtensions.txt', 'r')
    all_TLD = TLD_file.readlines()
    count = 0
    for line in all_TLD:
        all_TLD[count] = line[:-1]
        count += 1

def split_Email():
    global recipient, domain, tld
    recipient = str(getEmail.userEmail.split("@")[0])
    domain = str(getEmail.userEmail.split("@")[1])
    tld = (str(getEmail.userEmail.split("@")[1].split(".")[1])).upper()

get_TLD()
split_Email()

for x in all_TLD:
    if (x == tld):
        tld_real = True
        break
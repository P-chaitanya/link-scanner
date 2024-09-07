
phishing_urls  =["revil.ru ","conti.ru","doubledragon.cn","nso.il","ryuk.ru","sam.com"]
url = input("Enter a URL :")
domain = url.split("//")[-1].split("/")[0]
if domain in phishing_urls :
    print("beaware ! This URL is Known phishing URL. ")
else :
    print("This URL does not to be a phishing URL. ")    


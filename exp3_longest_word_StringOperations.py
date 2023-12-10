def long_Word():
    str1=input("Enter String")
    words=str1.split()
    long_word=[]
    length=0
    for i in words:
        len_word=len(i)
        if(len_word>=length):
            length=len_word
            long_word.append(i)
            
    print("longest word:")        
    for i in long_word:
        print(i,end="\t")
    print()

def char_Occur():
    str1=input("enter string")
    count=0
    flag=0
    ch=input("Enter char:")
    for i in range(len(str1)):
        if (ch==str1[i]):
            count+=1
            flag=1
 
    print("character occurence",count)

def str_Pallindrome():
    str1=input("Enter string")
    str2=""
    for i in range(0,len(str1)):
        str2=str1[i]+str2
    print("Reverse of string:",str2)
    if str2==str1:
        print(str1,"is palindrome....")
    else:
        print(str1,"is not palindrome....")
        
def subString_Appearance():
    str1=input("Enter String")
    words=str1.split()
    count=0
    for i in words:
        try:
            print(i,"appears in string at index ",count)
            while(str1[count]!=' '):
                count+=1
        except:
            print("Exception caught...")
               
        count+=1
        
def word_Occur():
    s=input("Enter string")
    words = s.split()
    u_words = []
    word_counts = []
    
    for word in words:
        flag = False
             
        for i in range(len(u_words)):
            
            if word == u_words[i]:
                word_counts[i] += 1
                flag = True
                break
        if not flag:
            u_words.append(word)
            word_counts.append(1)
            
    for i in range(len(u_words)):
        print(u_words[i],":",word_counts[i])
 

if __name__=="__main__":
    #str1=""
    print("1.Longest Word....")
    print("2.Display Occurance of Particular Character...")
    print("3.String is Palindrome...")
    print("4.First Appearance of subString ...")
    print("5.Occurance of each word in String ...")
    while(True):
        
        print("enter choice:")
        ch=int(input())
        if ch==1:
            long_Word()
           
        elif ch==2:
            char_Occur()
        elif ch==3:
            str_Pallindrome()
        elif ch==4:
            subString_Appearance()
        elif ch==5:
            word_Occur()
        else:
             print("wrong choice...")
             break

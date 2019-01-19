import tkinter
from tkinter import *



opk=0



def calculation_main():
    


    nb=name.get()
    db=date.get()
    mb=mobile.get()
    
    temp_db=db 
    ld=len(db) 
    temp= db
    list(db)
    ln=len(nb)
    list(nb)
    kn=[None]*ln
    temp_mb=mb
    lm=len(mb)


#==========================================================================

                                      # CALCULATION FOR MOBILE NUMBER MULLAYNKA

    mblz=['']*lm
    mblzz=['']*lm
    mblzzf=''
    mblzf=''
    mblk1=''
    mblk2=''
    mblk3=''
    mblk4=''
    mblk5=''
    mblk6=''

    
    n0= mb.count('0')
    list(mb)

    l=list()
    kl=0
    if n0>0:
        if mb[0] != '0':
            l=list(mb)
            for i in range(1,lm):
                if l[i]=='0':
                
                    l[i]=l[i-1]
            kl='1'

            
    mblk1="\n------------------------------------------------\nআপনার মোবাইল নম্বরটি ={}".format(temp_mb)        
    if kl=='1':
        mb= ','.join(l)
        mb=mb.replace(',','')
        
        mblk2="\nশূণ্য পরিবর্তনের পরে মোবাইল নম্বরটি  = \n {}".format(mb)
        n1= mb.count('1')
        n2= mb.count('2')
        n3= mb.count('3')
        n4= mb.count('4')
        n5= mb.count('5')
        n6= mb.count('6')
        n7= mb.count('7')
        n8= mb.count('8')
        n9= mb.count('9')
        ttl=0
        for i in range(0,lm):
            if mb[i]== '1':
                ttl =ttl+1
            elif mb[i]== '2':
                ttl =ttl+2
            elif mb[i]== '3':
                ttl =ttl+3
            elif mb[i]== '4':
                ttl =ttl+4
            elif mb[i]== '5':
                ttl =ttl+5
            elif mb[i]== '6':
                ttl= ttl+6
            elif mb[i]== '7':
                ttl= ttl+7
            elif mb[i]== '8':
                ttl= ttl+8
            elif mb[i]== '9':
                ttl= ttl+9
            else:
                ttl= ttl+0

        mblk3='\nসংখ্যা গুলির যোগফল ={}'.format(ttl)


    
        ans=0

        new = [int(x) for x in str(ttl)]
        z=len(new)
    


        if z==1:
            ans=ttl
        
        
        elif z>1:
            q=0
            while (1<z):
                total=0
                mblz[q]="\nসংখ্যা গুলি={}".format(new)
                q=q+1
                for i in range(0,z):
                    total=total+new[i]
                ans=total
                mblz[q]="\nসংখ্যা গুলির যোগফল ={}".format(ans)
                new=[int(x) for x in str(ans)]
                z=len(new)
                q=q+1

            

            mblzf=''
            for x in range(0,q):
                
                mblzf=mblzf+mblz[x]
            
        mb_mlnk=ans
        mblk4="\nআপনার মোবাইল নাম্বারের মূল্যাঙ্ক={}".format(mb_mlnk)


    
    
    else:
        n1= temp_mb.count('1')
        n2= temp_mb.count('2')
        n3= temp_mb.count('3')
        n4= temp_mb.count('4')
        n5= temp_mb.count('5')
        n6= temp_mb.count('6')
        n7= temp_mb.count('7')
        n8= temp_mb.count('8')
        n9= temp_mb.count('9')
        total=0
        for i in range(0,lm):
            if temp_mb[i]== '1':
                total =total+1
            elif temp_mb[i]== '2':
                total =total+2
            elif temp_mb[i]== '3':
                total =total+3
            elif temp_mb[i]== '4':
                total =total+4
            elif temp_mb[i]== '5':
                total =total+5
            elif temp_mb[i]== '6':
                total= total+6
            elif temp_mb[i]== '7':
                total= total+7
            elif temp_mb[i]== '8':
                total= total+8
            elif temp_mb[i]== '9':
                total= total+9
            else:
                total= total+0
    
        mblk5="\nসংখ্যা গুলির যোগফল ={}".format(total)


    
        ans=0

        new = [int(x) for x in str(total)]
        z=len(new)
    


        if z==1:
            ans=total
        
        
        elif z>1:
            k=0
            
            while (1<z):
                total=0
                mblzz[k]="\nসংখ্যা গুলি={}".format(new)
                k=k+1
                for i in range(0,z):
                    total=total+new[i]
                ans=total
                mblzz[k]="\nসংখ্যা গুলির যোগফল ={}".format(ans)
                new=[int(x) for x in str(ans)]
                z=len(new)
                k=k+1
            
 
        
            for x in range(0,k):
                
                mblzzf=mblzzf+mblzz[x]
            
        mb_mlnk=ans
        mblk6="\nআপনার মোবাইল নাম্বারের মূল্যাঙ্ক={}".format(mb_mlnk)


    mblz=mblk1+mblk2+mblk3+mblzf+mblk4+mblk5+mblzzf+mblk6




#===========================================================


                             # PREDICTION FROM MOBILE NUMBER MULLAYAKA

    
    an1=''
    an2=''
    an3=''
    an4=''
    an5=''
    an6=''
    an7=''
    an8=''
    an9=''
    an10=''
    an11=''
    an12=''
    an13=''
    an14=''
    an15=''
    an16=''
    an17=''
    an18=''
    an19=''
    

    an1='\n মোবাইল নাম্বারের নম্বর ত্বত্ত ভিত্তিতে আপনার বৈশিষ্ট হওয়ার সম্ভবনা :\n\n'
    if n1==0 :
        an2='1 = রবি,অনুপস্থিতির জন্য : আত্মমর্যাদা কম থাকবে জীবনে\n'
    
    if n2==0 :
        an3='2 = চন্দ্র,অনুপস্থিতির জন্য : মনবল ,বিশ্বাস ,আবেগ কম থাকবে জীবনে \n'

    if n3==0 :
        an4='3 = বৃহস্পতি,অনুপস্থিতির জন্য : গুরু কৃপা কম থাকবে জীবনে \n'
    
    if n4==0 :
        an5='4 =রাহু,অনুপস্থিতির জন্য : জীবনের দীশা থাকবেনা \n'

    if n5==0 :
        an6='5 =বুধ,অনুপস্থিতির জন্য : তর্ক বিতর্ক আপনার দ্বারা কম হবে আপনি শান্ত হবেন \n'
    
    if n6==0 :
        an7='6 =শুক্র,অনুপস্থিতির জন্য : ভোগ সুখ কম থাকবে জীবনে \n'

    if n7==0 :
        an8='7 =কেতু,অনুপস্থিতির জন্য : ভালো সারকেল নষ্ট হবে , গবেষনামূলক কাজ কর্ম কম হবে \n'
    
    if n8==0 :
        an9='8  =শনি,অনুপস্থিতির জন্য : সিধান্ত নিতে অসুবিধা হবে আপনার \n'

    if n9==0 :
        an10='9 = মঙ্গল,অনুপস্থিতির জন্য : আপনি নিজের জন্য সংগ্রাম করতে পারবেন না \n'







    if n1==2 :
        an11='* নেতৃত্বদানকারি  * অহংকারী * অর্থবান * স্বাধীনচেতা *\n'
    
    if n2==2 :
        an12='* পরপোকারী * আবেগপ্রবণ * দয়ালু * ভালোবন্ধু *\n'

    if n3==2 :
        an13='* শৃঙ্খলাপরায়ণ * সত্যবাদী * ধার্মিক * নিয়মাবর্তী *\n'
    
    if n4==2 :
        an14='* নিয়ামুবর্তী * কঠোরপরিশ্রমী * ভোগবিলাসী * অতৃপ্ত *\n'

    if n5==2 :
        an15='* বিচক্ষণ * বুদ্ধিমান * উদ্যোগী * উৎসাহী * অস্থির * শিশুসুলভ *\n'
    
    if n6==2 :
        an16='* রসিক * হাস্যযুক্ত * কামুক * ভোগবিলাসী * সকলের প্রিয় *\n'

    if n7==2 :
        an17='* আত্মবিশ্বাসী * আত্মকেন্দ্রিক * বিশ্লেষক * গবেষক *\n'
    
    if n8==2 :
        an18='* নিরাশ * দীর্ঘসূত্রী * পারিশ্রমী * বাস্তববাদী * উচ্চাকাঙ্খী *\n'

    if n9==2 :
        an19='* আক্রমণাত্মক * আদর্শবাদী * স্পষ্টবক্তা * মহৎহৃদয় * \n'


    an='\n---------------------------------------------------------\n'+an1+an2+an3+an4+an5+an6+an7+an8+an9+an10+'\n---------------------------------------------------------\n'+an11+an12+an13+an14+an15+an16+an17+an18+an19+'---------------------------------------------------------\n'
#==================================================================
                                                  # CALCULATION OF NAME MULLAYANKA
    
    
    nv=['']*ln
    fnv=''
    nv11=''
    nv12=''
    nv13=''
    nv14=''
    k=''
    
    for i in range(0,ln):
        if nb[i]=='a' or nb[i]== 'A':
            kn[i]=1
        elif nb[i]== 'b' or nb[i]== 'B':
            kn[i]=2
        elif nb[i]== 'c' or nb[i]== 'C':
            kn[i]=3
        elif nb[i]== 'd' or nb[i]== 'D':
            kn[i]=4
        elif nb[i]== 'e' or nb[i]== 'E':
            kn[i]=5
        elif nb[i]== 'f' or nb[i]== 'F':
            kn[i]=6
        elif nb[i]== 'g' or nb[i]== 'G':
            kn[i]=7
        elif nb[i]== 'h' or nb[i]== 'H':
            kn[i]=8
        elif nb[i]== 'i' or nb[i]== 'I':
            kn[i]=9
        elif nb[i]== 'j' or nb[i]== 'J':
            kn[i]=1
        elif nb[i]== 'k' or nb[i]== 'K':
            kn[i]=2
        elif nb[i]== 'l' or nb[i]== 'L':
            kn[i]=3
        elif nb[i]== 'm' or nb[i]== 'M':
            kn[i]=4
        elif nb[i]== 'n' or nb[i]== 'N':
            kn[i]=5
        elif nb[i]== 'o' or nb[i]== 'O':
            kn[i]=6
        elif nb[i]== 'p' or nb[i]== 'P':
            kn[i]=7
        elif nb[i]== 'q' or nb[i]== 'Q':
            kn[i]=8
        elif nb[i]== 'r' or nb[i]== 'R':
            kn[i]=9
        elif nb[i]== 's' or nb[i]== 'S':
            kn[i]=1
        elif nb[i]== 't' or nb[i]== 'T':
            kn[i]=2
        elif nb[i]== 'u' or nb[i]== 'U':
            kn[i]=3
        elif nb[i]== 'v' or nb[i]== 'V':
            kn[i]=4
        elif nb[i]== 'w' or nb[i]== 'W':
            kn[i]=5
        elif nb[i]== 'x' or nb[i]== 'X':
            kn[i]=6
        elif nb[i]== 'y' or nb[i]== 'Y':
            kn[i]=7
        elif nb[i]== 'z' or nb[i]== 'Z':
            kn[i]=8
        elif nb[i]==' ':
            kn[i]=0
        else :
            kn[i]=0
    nv11="\n{} পরিবর্তন করে".format(nb)
    nv12="\nসংখ্যা গুলি হবে ====>>> \n{}".format(kn)




    to= 0
    for i in range(0,ln):
        to= to+kn[i]

    
    nv13="\nসংখ্যা গুলির যোগফল ={}".format(to)


    ans=0

    digits = [int(x) for x in str(to)]
    lt=len(digits)

    if lt==1:
        ans=to
    
    elif lt>1:
        k=0
        while (1<lt):
            
            sm=0
            nv[k]="\nসংখ্যা গুলি ={}".format(digits)
            k=k+1
            for i in range (0,lt):
                sm=sm+digits[i]
            ans=sm
            nv[k]="\nসংখ্যা গুলির যোগফল ={}".format(ans)
            digits = [int(x) for x in str(ans)]
            lt=len(digits)
            k=k+1

            

        
        for x in range(0,k):
            
            fnv=fnv+nv[x]

    nm_mlnk=ans
    nv14="\nআপনার নামের মূল্যাঙ্ক={}".format(nm_mlnk)
    nmut=nv11+nv12+nv13+fnv+nv14

    pbs=''

    if  ans==1 :
        pbs='\n* নেতৃত্বদানকারি \n\n* অহংকারী \n\n* অর্থবান \n\n* স্বাধীনচেতা'
    
    if ans==2 :
        pbs='\n* পরপোকারী \n\n* আবেগপ্রবণ \n\n* দয়ালু \n\n* ভালোবন্ধু'

    if  ans==3 :
        pbs='\n* শৃঙ্খলাপরায়ণ \n\n* সত্যবাদী \n\n* ধার্মিক \n\n* নিয়মাবর্তী'
    
    if  ans==4 :
        pbs='\n* নিয়ামুবর্তী \n\n* কঠোরপরিশ্রমী \n\n* ভোগবিলাসী \n\n* অতৃপ্ত'

    if  ans==5  :
        pbs='\n* বিচক্ষণ \n\n* বুদ্ধিমান \n\n* উদ্যোগী \n\n* উৎসাহী \n\n* অস্থির \n\n* শিশুসুলভ'
    
    if  ans==6:
        pbs='\n* রসিক \n\n* হাস্যযুক্ত \n\n* কামুক \n\n* ভোগবিলাসী \n\n* সকলের প্রিয়'

    if  ans==7:
        pbs='\n* আত্মবিশ্বাসী \n\n* আত্মকেন্দ্রিক \n\n* বিশ্লেষক \n\n* গবেষক'
    
    if  ans==8  :
        pbs='\n* নিরাশ \n\n* দীর্ঘসূত্রী \n\n* পারিশ্রমী \n\n* বাস্তববাদী \n\n* উচ্চাকাঙ্খী'

    if  ans==9:
        pbs='\n* আক্রমণাত্মক \n\n* আদর্শবাদী \n\n* স্পষ্টবক্তা \n\n* মহৎহৃদয়'
 

    bois.set(pbs)


#====================================================================

                                          # CALCULATION OF BIRTH DATE MULLAYANKA
    jm=['']*ld
    jmf=''
    jmk1=''
    jmk2=''
    jmk3=''

    total=0
    for i in range(0,ld):
        if db[i]== '1':
            total =total+1
        elif db[i]== '2':
            total =total+2
        elif db[i]== '3':
            total =total+3
        elif db[i]== '4':
            total =total+4
        elif db[i]== '5':
            total =total+5
        elif db[i]== '6':
            total= total+6
        elif db[i]== '7':
            total= total+7
        elif db[i]== '8':
            total= total+8
        elif db[i]== '9':
            total= total+9
        else:
            total= total+0



    jmk1="\nআপনার জন্ম তারিখ={}".format(temp_db)
    jmk2="\nসংখ্যা গুলির যোগফল ={}".format(total)


    total1=0
    ans=0

    new = [int(x) for x in str(total)]
    z=len(new)


    if z==1:
        ans=total
    
    elif z>1:
        w=0
        while (1<z):
            total=0
            jm[w]="\nসংখ্যা গুলি={}".format(new)
            w=w+1
            for i in range(0,z):
                total=total+new[i]
            ans=total
            jm[w]="\nসংখ্যা গুলির যোগফল ={}".format(ans)
            new=[int(x) for x in str(ans)]
            z=len(new)
            w=w+1
        
        for x in range(0,w):
            jmf=jmf+jm[x]
        

    bd_mlnk=ans
    jmk3="\nআপনার জন্ম তারিখ মূল্যাঙ্ক={}".format(bd_mlnk)

    
    bdut="\n-----------------------------------------"+jmk1+jmk2+jmf+jmk3


    nnn="আপনার নাম = {}".format(nb)
    bbb="\nআপনার জন্ম তারিখ = {}".format(temp_db)
    mmm="\nআপনার মোবাইল নম্বরটি = {}".format(temp_mb)
    kkk=nnn+bbb+mmm+"\n==========================================="

    
    calu=kkk+nmut+bdut+mblz+an
    calcu.set(calu)
    


#================================================================================



                                             # JOB PREDICTION CALCULATION FROM BIRTH DATE MULLAYANK

    jbb=0
    



    if bd_mlnk==1:
        jbb="1. রাজনীতি \n\n2. ডাক্তার \n\n3. সরকারি উচ্চপদাধিকারী \n\n4. ধর্মপ্রচারক \n\n5. মেডিসিন"
    

    elif bd_mlnk==2:
        jbb="1. সমাজসেবী \n\n2. সাহিত্যিক \n\n3. তরল পদার্থ ব্যাবসায়ী \n\n4. নার্স \n\n5. নেভি \n\n6. শিক্ষক \n\n7. কবি"
    

    elif bd_mlnk==3:
        jbb="1. আইন \n\n2. ব্যাঙ্ক \n\n3. ফাইন্যান্স \n\n4. ধর্মগুরু \n\n5. ডাক্তার \n\n6. ডেকরেটর"
    

    elif bd_mlnk==4:
        jbb="1. ইঞ্জিনিয়ার \n\n2. শেয়ার মার্কেট \n\n3. ঝুঁকি পূর্ণকাজ  \n\n4. অবৈধকর্ম"
    

    elif bd_mlnk==5:
        jbb="1. লেখক \n\n2. সাংবাদিক \n\n3. এজেন্ট \n\n4. অ্যাকাউন্ট্যান্ট \n\n5. জ্যোতিষী \n\n6. শিক্ষক"
    

    elif bd_mlnk==6:
        jbb="1. শিল্পী \n\n2. রিসেপসনিস্ট \n\n3. জাজ \n\n4. লাক্সারী দ্রব্য ডিলার \n\n5. ইন্টারনেট সংক্রান্ত (IT jobs)\n\n6. জুয়েলারী ডিলার"
    

    elif bd_mlnk==7:
        jbb="1. সমাজসেবী \n\n2. গোয়েন্দা \n\n3. জাদুকর \n\n4. এজেন্ট \n\n5. গুপ্তচর \n\n6. ফিসারী"
    

    elif bd_mlnk==8:
        jbb="1. হার্ডওয়ার \n\n2. পঞ্চায়েত \n\n3. মাইনিং \n\n4. জোতিষী \n\n5. গণিতজ্ঞ \n\n6. উপদেষ্টা"
    

    elif bd_mlnk==9:
        jbb="1. ডিফেন্স \n\n2. পুলিশ \n\n3. ইনডাস্ট্রিয়ালিষ্ট \n\n4. সার্জেন \n\n5. আইন \n\n6. কেমিষ্ট-ড্রাগিষ্ট \n\n7. কৃষিবিভাগ \n\n8. ডাক্তার \n\n9. ইনসুরেন্স \n\n10. খেলয়ার"
    
    else:
        jbb="PROBLEM..!! \nIs The Date Of Birth Entered Correctly ?"

    job.set(jbb)
    
    

#============== mullaynka ==============

    mlall=0
    nml="[1] আপনার নামের মূল্যাঙ্ক  = {0:1}".format(nm_mlnk)
    mbl="\n\n[3] আপনার মোবাইল নাম্বারের মূল্যাঙ্ক  = {0:1}".format(mb_mlnk)
    dtl="\n\n[2] আপনার জন্ম তারিখের মূল্যাঙ্ক  = {0:1}".format(bd_mlnk)
    mlall=nml+dtl+mbl
    mulla.set(mlall)


# ========================================================



                                                          # CALCULATION OF IF MOBILE NUMBER IS LUCKY OR NOT





    mbs=0
    if (mb_mlnk == nm_mlnk) or (mb_mlnk == bd_mlnk) or (bd_mlnk == nm_mlnk) :
    
        mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে খুব শুভ.....!!!!"
            
        
    elif mb_mlnk==1:
    
    
        if nm_mlnk==4 or nm_mlnk== 8 or bd_mlnk==4 or bd_mlnk== 8:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
                

    elif mb_mlnk==2:
    
        if nm_mlnk== 4 or nm_mlnk== 7 or nm_mlnk== 8 or nm_mlnk==9or bd_mlnk==4 or bd_mlnk==7 or bd_mlnk==8 or bd_mlnk== 9:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==3:
    
        if nm_mlnk==5 or nm_mlnk==6 or nm_mlnk==7 or nm_mlnk== 9or bd_mlnk==5 or bd_mlnk== 6 or bd_mlnk== 7 or bd_mlnk== 9:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==4:
    
        if nm_mlnk==1 or nm_mlnk==2 or nm_mlnk==8or bd_mlnk==1 or bd_mlnk==2 or bd_mlnk==8:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
                
    elif mb_mlnk==5:
    
        if nm_mlnk==3 or nm_mlnk==9or bd_mlnk==3 or bd_mlnk== 9:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==6:
    
        if nm_mlnk==3 or nm_mlnk==9or bd_mlnk==3 or bd_mlnk== 9:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==7:
    
        if nm_mlnk==2 or nm_mlnk==6or bd_mlnk==2 or bd_mlnk== 6:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==8:
    
        if nm_mlnk==1 or nm_mlnk== 4or bd_mlnk==1 or bd_mlnk== 4:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"
            

    elif mb_mlnk==9:

        if nm_mlnk==2 or nm_mlnk== 3 or nm_mlnk== 6 or bd_mlnk==2 or bd_mlnk== 3 or bd_mlnk== 6:
            mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে শুভ"
        else :
             mbs="আপনার মোবাইল নম্বরটি আপনার পক্ষে সাধারন (Nutral)"

    mobsuv.set(mbs)


                                                             # End of main calculation function

#=================================================================================================================================================================
def submit():
    zz=0
    key=a.get()
    k="N@7991"
    b.set(None)
    if key==k:
        a.set("")
        i='WELCOME....!!!!'
        b.set(i)

        
        lg.after(500, lambda: lg.destroy())
        global opk
        opk = 1
    else:
        i='Access Denied...!! Invalid Key Please Try Again'
        b.set(i)
        a.set("")



def savetx():
    
    nm=''
    dt=''
    mbl=''
    bo=''
    jo=''
    mul=''
    mbs=''
    calc=''

    
    
    nm=name.get()
    dt=date.get()
    mbl=mobile.get()
    bo=bois.get()
    jo=job.get()
    mul=mulla.get()
    mbs=mobsuv.get()
    calc=calcu.get()

    
    if nm!=0:

        pt=''
        f=nm+".txt"
        f=open(f,'w',encoding="utf-8")
        fl="\t\t\t -: Welcome To Numerology Softere :-\n\n\n"+"\t\tName :\n"+ nm+"\n\n\n\n\t\tDate of Birth :\n"+dt+"\n\n\n\n\t\tMobile Number :\n"+mbl+"\n\n\n\n\t\tBoisisto : \n"+bo+"\n\n\n\n\t\tSomvobbo job :\n"+jo+"\n\n\n\n\t\tMullayanka : \n"+mul+"\n\n\n\n\t\tMobile number suvo ki na : \n"+mbs+"\n\n\n\n\t\tcalculation :\n"+calc+"\n\n\n\n\n\n\n\t\t\t -: Developed By Purnendu Das (das888purnendu@gmail.com) :-"
        
        f.write(fl)
        f.close()





#====================================================================================================================================================================
                                                         # Main GUI programme starts




lg=Tk()
lg.title("Lg In Page")
lg.geometry("700x680+330+10")
lg.resizable(0,0)
lg.config(bg="black")

a=StringVar()
b=StringVar()

ph=PhotoImage(file="label-image1.gif")
Label(lg,image=ph,height=400,bg="black").place(x=0,y=0)



Label(lg,text="Enter The Software Key :",fg="white",bg="black",font=('cooper',10,'bold')).place(x=60,y=470)

pas=Entry(lg,width=55,textvariable=a,show="*").place(x=230,y=470)



Button(lg,text="Submit",width=12,fg="green",command=submit).place(x=270,y=530)
Button(lg,text="Exit",width=12,fg="red",command=lg.destroy).place(x=370,y=530)


inf=Label(lg,height=2,textvariable=b,width=50,font=('arial',14,'italic'),bg="black",fg="red").place(x=90,y=590)

lg.mainloop()
#==========================================================================================================================================
                                           # main programme with if condition :



if opk==1:
    w1= Tk()
    w1.title("Home Page")
    w1.geometry("654x654+370+20")
    w1.configure(bg="#20043B")









    l1=Label(w1,text='Welcome To The Numerology Software', font=('arial',15,'bold'),fg='blue',bg='white',width=54).place(x=0,y=5)


    l2=Label(w1,text="আপনার নাম লিখুন :",fg='white',bg='#20043B',font=('cooper',10,'bold')).place(x=160,y=70)
    l3=Label(w1,text="আপনার জন্ম তারিখ লিখুন :",bg='#20043B',fg='white',font=('cooper',10,'bold')).place(x=160,y=100)
    l4=Label(w1,text="আপনার মোবাইল নম্বরটি লিখুন :",bg='#20043B',fg='white',font=('cooper',10,'bold')).place(x=160,y=130)



    name=StringVar() #input name
    date=StringVar() #input birth date
    mobile=StringVar() #input mobile number

    bois=StringVar() #output boisisto
    job=StringVar() #output job
    mulla=StringVar() #output mullaynka
    mobsuv=StringVar() #output number suvo
    calcu=StringVar() # calculation





    nm_e = Entry(w1,textvariable=name,width=40,bg='#F9E7D8').place(x=380,y=70)        # Entry name   
    bd_e = Entry(w1,textvariable=date,width=40,bg='#F9D5D8').place(x=380,y=100)       # Entry Birth Date  
    mn_e = Entry(w1,textvariable=mobile,width=40,bg='#E5D5D8').place(x=380,y=130)     # Entry Mobile Number   




    Button(w1,text="Submit",width=12,relief=RAISED,command=calculation_main,fg="#135C00").place(x=250,y=200)# Submit Button
    Button(w1,text="Exit",width=12,command=w1.destroy,relief=RAISED,fg="#820000").place(x=350,y=200) # Exit button



    photo1=PhotoImage(file="label-image2.gif")
    Label(w1,image=photo1,bg="#20043B",height=150,width=150).place(x=0,y=40)                                      # photo


    Label(w1,text="    ____________________________________________________________________________________________________________________________",bg="#20043B",fg="white").place(x=0,y=230)

    Label(w1,text=": সম্ভাবনা :",bg="#20043B",fg="white",height=1).place(x=280,y=248)  # somvobona text
    Label(w1,text="বৈশিষ্ট্য  :",bg="#20043B",fg="white").place(x=378,y=270)            # boisistotext
    Label(w1,text="মানানসই চাকরি :",bg="#20043B",fg="white").place(x=5,y=270)       # job text
    Label(w1,text="মূল্যাঙ্ক :",bg="#20043B",fg="white").place(x=370,y=490)              # mullayanka text




    jb =Label(w1,textvariable=job,height=19,width=45,bg="#DFF0FF",fg='blue').place(x=10,y=290)    #boisisto bs
    bs =Label(w1,textvariable=bois,height=12,width=35,bg="#FFF4F9",fg='green').place(x=380,y=290)  # job jb
    ml=Label(w1,textvariable=mulla,height=6,width=35,bg="#D4FDFF",fg='red').place(x=380,y=510)      # mullayanka ml






    Label(w1,text="    ____________________________________________________________________________________________________________________________",bg="#20043B",fg="white").place(x=0,y=622)
    Label(w1,text="|| Developed BY PURNENDU DAS ||  das888purnendu@gmail.com ||",bg="#20043B",fg="white",font=('arial',7,'bold'),height=1).place(x=170,y=640)

    ns=Label(w1,textvariable=mobsuv,height=1,width=75,bg="#F6A2FF").place(x=52,y=610)  # number suvo ns








    Label(width=0,height=40,bg="white").place(x=670,y=30) #divider border


    Label(text="গনণা :",bg="#20043B",fg="white",font=('cooper',10,'bold')).place(x=720,y=5) #calculation text

    cl=Label(w1,textvariable=calcu,width=75,height=43,bg="#FFDBC3").place(x=735,y=25) #calculation label cl

    Button(w1,text="Save to TXT File",width=15,height=1,command=savetx).place(x=850,y=680) #save to txt button
    Button(w1,text="Exit",width=12,height=1,command=w1.destroy,relief=RAISED,fg="#820000").place(x=1050,y=680) # Exit button



    w1.mainloop()
#=========================================================================== Programme End ============================================================================

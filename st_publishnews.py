
import streamlit as st
import string
import time
import textwrap

st.title("Example Only - Resources News Releases")

cntr = 2000 ### CHANGE
YYYYMMDD = '20240715' ### TODAY'S AEST/AEDT DATE

i = open('C:\\RWE\\publishready.txt','r')
l = i.readlines()
#print(ld.close()

for x in range(len(l)):
    if l[x][0:4] == '!STD':
        begin = x
        print(str(x) + " " + l[x+1])
        headline = l[x+1] ##:blue-background[highlight]
        st.subheader(headline)
        
        
        
    if l[x][0:4] == '!END':
        finish = x
        #print(str(x))

        story = l[begin+2:finish-1]
        #body = l[begin+2:finish-1]
        
        o = open('C:\\tempstore0\\temp' + str(x) +'.txt','w')
        for y in range(len(story)):
            story[y] = str.replace(story[y],' $',' USD')  
            story[y] = str.replace(story[y],'US$',' USD')                     
            story[y] = str.replace(story[y],'â€™',"'")
            story[y] = str.replace(story[y],'â€˜','')
            story[y] = str.replace(story[y],'â€ ','')  #USD  
            o.write(story[y])
            
            st.markdown(story[y])
            
        st.divider()
        o.close()

        cntr = cntr + 1
        scntr = str(cntr)
        if len(scntr) < 2:
            scntr = '0' + scntr
        
        ff1 = open('C:\\tempstore0\\temp' + str(x) +'.txt','r')
        ff2 = ff1.read()
        #ff3 = string.split(ff2,'          ')
        #st.markdown(ff2)

        #if len(ff2) > 250:
            
#         wrapper = textwrap.TextWrapper(width=100)
#         word_list = wrapper.wrap(text = ff2)
#         o = open("C:\\tempstore_STREAMLIT\\st_"  + YYYYMMDD + '_' + scntr + '.txt', 'w')
#         s = "\n"
#         wl = s.join(word_list)
#         #o.write(wl) #s = ","
#         #s.join(country_names)
#         o.close()        
 

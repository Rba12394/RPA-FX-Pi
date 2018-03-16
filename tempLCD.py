 def menu():  
  timelastchecked = 0  
  time.sleep(0.5)  
  while(1):  
   if time.time() >= timelastchecked:  
    timelastchecked = time.time()+3  
    mystring = ""  
    mytime = ""  
    mytemp = ""  
    pretemp =   
    posttemp = "*F "  
    f=os.popen("date")  
    for i in f.readlines():  
     mytime += i  
     mytime = mytime[11:-13]  
     f=os.popen("/opt/vc/bin/vcgencmd measure_temp")  
     for i in f.readlines():  
      mytemp += i  
      mytemp = mytemp[5:-3]  
      mystring = mytemp + posttemp + mytime  
      lcd_byte(LCD_LINE_1, LCD_CMD)  
      lcd_string(mystring,1)  
      lcd_byte(LCD_LINE_2, LCD_CMD)  
      lcd_string("< Off   Menu >",2)  
   else:  
    if ( GPIO.input(NEXT) == False):  
     menu1()  
    if ( GPIO.input(PREV) == False):  
     off() 
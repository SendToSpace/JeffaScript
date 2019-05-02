import xlwt

def strmatch(word,arry):
    result = False
    for i in range(len(arry)):
        if word==arry[i]:
            result = True
    return result

def convert():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('stats')
    f = open("test.txt","r+")
    c =0
    r =0
    word = ''
    parameter = ['host_inst_rate' ,"host_tick_rate"]
    while True:
        data = f.readline()
        index=0
        if data:
            while index < len((data))-1:


                if not data[index].isspace():
                    word = word+data[index]
                    index+=1
                else:
                    print(strmatch(word,parameter))
                    if strmatch(word,parameter)==False:
                        word =''
                        break
                    ws.write(c,r,word)
                    print(word)
                    word =''
                    index+=1

                    while data[index].isspace():
                        if(index<len(data)-1):
                            index+=1
                        else:
                            break


                    if(c==0):
                        c+=1
                        while index < len((data)) - 1:
                            if not data[index].isspace():
                                word = word + data[index]
                                index += 1
                            else:
                                ws.write(c, r, word)
                                print(word)
                                word = ''
                                index += 1
                                r+=1
                                c-=1
                                break

                        break

        else:
            break

    wb.save('example.xls')
    f.close()



convert()

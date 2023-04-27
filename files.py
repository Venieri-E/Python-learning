# var = input("Add some text : ")
# fw = open('doc/file1.txt','a')
# fw.write(var)
# fw.close()
# a - запись новых данных в конец файла
# w - запись новых данных , c удалением старых

# fw = open('doc/file2.txt','w')
# fw.write("Privet")
# fw.close()

#  fr / r чтение файла
fr = open('doc/file1.txt','r')
text = fr.read()
fr.close()
print(text)

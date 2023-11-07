import mysql.connector
from datetime import date
import getpass
import matplotlib.pyplot as plt


fine = 1.0
today = date.today()
#View suggested book
api_key = 'AIzaSyCNtTzKSt_iYCXSy63XiYGn6l7mETD1QPM'
from googleapiclient.discovery import build
def vieww():
    book = build('books','v1',developerKey=api_key)
    req = book.volumes()
    res = req.list(q='intitle')
    ite = res.execute()
    print("                   S U G G E S T E D  B O O K S  F O R  Y O U")
    for i in ite['items']:
        print("-"*80)
        print("Title: ")
        print(i['volumeInfo']['title'])
        print("\n")
        print("-"*80)
#Add member
def add_stu():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print("\n\n                     I N S E R T  A  N E W  D E T A I L\n\n")
    idn = input('Enter Student id : ')
    name = input('Enter Student Name :')
    email = input('Enter Student Email  : ')
    cmd = 'INSERT INTO user_details VALUES ( "' + idn + '","' + name + '","'+email+'" );'
    cursor.execute(cmd)
    conn.commit()
    conn.close()
    print('\nNew Student added successfully')
    wait = input('\nPress any key to continue....')
#Update student
def upd_stu():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print('\n\n\n            M O D I F Y  S T U D E N T  I N F O R M A T I O N')
    print('\n1. Name')
    print('\n2. Email')
    print('\n')
    choice = int(input('Enter your choice :'))
    ch =''
    if choice == 1:
        ch ='name'
    if choice == 2:
        ch = 'email'
    iid =input('Enter Student ID :')
    val = input('Enter detail :')
    cmd = 'UPDATE user_details SET '+ ch +' = "'+val+'" WHERE id = '+iid+';'
    cursor.execute(cmd)
    print('\nStudent details Updated.....')
    conn.commit()
    conn.close()
    wait = input('\nPress any key to continue....')
#delete member
def delete_stu():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print("\n\n           D E L E T E   A  S T U D E N T   R E C O R D")
    idi = input("Enter ID: ")
    cmd = 'DELETE FROM user_details WHERE id = "' + idi + '";';
    cursor.execute(cmd)
    print('Student record Deleted.....')
    conn.commit()
    conn.close()
    wait = input('\n Press any key to continue....')
#show member list

def students():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print('\n\n      S T U D E N T S   L I S T\n\n ')
    cmd = 'SELECT * FROM user_details'
    cursor.execute(cmd)
    rec = cursor.fetchall()
    for i in rec:
        print(i)
    conn.commit()
    conn.close()
    wait = input('\nPress any key to continue.....')
#search for a particular member
def search_stu():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print('\n\n    F I N D  A  P A R T I C U L A R  S T U D E N T\n\n')
    p_id =input('Enter student ID :')
    cmd = 'SELECT * FROM user_details WHERE id = "'+ p_id +'";'
    print('        DETAILS    ')
    cursor.execute(cmd)
    rec = cursor.fetchall()
    for i in rec:
        print(rec)
    conn.close()
    wait = input('\nPress any key to continue....')

#issue status
def book_issue_status(book_id,mem_id):
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(
        host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    sql = 'select * from trans where b_id ='+str(book_id) + ' and m_id ='+ str(mem_id) +' and dare_r is NULL;'
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
#book_id = input("Enter Book Id: ")
#mem_id = input("Enter Student Id: ")
#book_issue_status(book_id,mem_id)


#Number of issued books by a particular student
def issue_status():
    global mem_id
    mem_id = input("Enter your ID: ")
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(
        host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    sql ='select * from trans where m_id ='+ str(mem_id) +' and dare_r is NULL;'
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

#Issue a book

def issue():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    print('\n\n B O O K    I S S U E   I N F O\n\n')
    book_id = input('Enter Book  ID : ')
    s_id  = input('Enter Student ID :')
    today = date.today()
    cmd = 'INSERT INTO trans(b_id, m_id, date_b) VALUES('+book_id+','+s_id+',"'+str(today)+'");'
    print('\n\nBook issued successfully')
    cursor.execute(cmd)
    conn.commit()
    conn.close()
    wait = input('\nPress any key to continue....')
#issue()
#Return book
def return_book():
    us = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    global fine
    fine = 1.0
    print('\n     B O O K  R E T U R N  I N F O    ')
    book_id = input('Enter Book  ID : ')
    s_id = input('Enter Student ID :')
    today = date.today()
    res = book_issue_status(book_id, s_id)
    if res == None:
        print('Book was not issued...Check Book Id and Member ID again..')
    else:
        sql = 'UPDATE book_data SET status ="available" WHERE Book_Id =' + book_id + ';'
        d = (today - res[3]).days
        fin = d * fine
        sql1 = 'UPDATE trans SET dare_r ="' + str(today) + '" , fine=' + str(
            fin) + ' WHERE b_id=' + book_id + ' AND m_id=' + s_id + ' AND dare_r IS NULL;'

        cursor.execute(sql)
        cursor.execute(sql1)
        print('\n\nBook returned successfully')
    conn.commit()
    conn.close()
    wait = input('\nPress any key to continue....')
# return_book()

#Search and Add Book to the library
import urllib.request
import json
import textwrap
def addboook():
    #try:
        while True:
            print("*"*80)
            print("\nS E A R C H   M E N U")
            print("\n1.By Book Title\n2.By ISBN\n3.By Author's name\n0.Exit")
            choice = int(input())
            #link = 'https://www.googleapis.com/books/v1/mylibrary/bookshelves/1/volumes
            if (choice==1):
                api_link = "https://www.googleapis.com/books/v1/volumes?q=intitle:"
                tit = input("Enter Title: ").strip()
                with urllib.request.urlopen(api_link + tit) as f:
                    text = f.read()
                decode = text.decode("utf-8")
                obj = json.loads(decode)
                print("\nTitle:", obj["items"][0]["volumeInfo"]["title"])
                aut = obj["items"][0]["volumeInfo"]["authors"]
                print("\nAuthor(s):")
                print(",".join(aut))
                #print("\nDescription: ", obj["items"][0]['volumeInfo']['description'])
                print("\nPublished Date:")
                print(obj['items'][0]["volumeInfo"]["publishedDate"])
                print("\nRating: ")
                print(obj["items"][0]['volumeInfo']['averageRating'])
                print("\nPage Count:")
                print(obj['items'][0]["volumeInfo"]["pageCount"])
                print("-*30")
                print("Add the book to the library? y or no. ")
                ch = input()
                if (ch == 'y'):
                    ############################################################################################################
                    us = input("Enter username: ")
                    passs = input("Enter password: ")
                    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
                    cursor = conn.cursor()
                    title = obj["items"][0]["volumeInfo"]["title"]
                    autho = obj["items"][0]["volumeInfo"]["authors"]
                    author = ",".join(autho)
                    rat = obj["items"][0]['volumeInfo']['averageRating']
                    pub_date = obj['items'][0]["volumeInfo"]["publishedDate"]
                    pages = obj['items'][0]["volumeInfo"]["pageCount"]
                    cmd = 'INSERT INTO book_data(Title,Author,Rating,Page_Count) VALUES ( "' + title + '","' + author + '","' + str(
                        rat) + '",' + str(pages) + ');'
                    cursor.execute(cmd)
                    conn.commit()
                    conn.close()
                    print('\n\nNew Book added successfully')
                    wait = input('\nPress any key to continue....')
                if (ch == 'n'):
                    wait = input('\nPress any key to continue....')
            if (choice == 2):
                base_api_link = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
                isbnn = input("Enter ISBN: ").strip()
                with urllib.request.urlopen(base_api_link + isbnn) as f:
                    text = f.read()
                decode = text.decode("utf-8")
                obj = json.loads(decode)
                print("\nTitle:", obj["items"][0]["volumeInfo"]["title"])
                aut = obj["items"][0]["volumeInfo"]["authors"]
                print("\nAuthor(s):")
                print(",".join(aut))
                # print("\nDescription: ", obj["items"][0]['volumeInfo']['description'])
                print("\nPublished Date:")
                print(obj['items'][0]["volumeInfo"]["publishedDate"])
                print("\nRating: ")
                print(obj["items"][0]['volumeInfo']['averageRating'])
                print("\nPage Count:")
                print(obj['items'][0]["volumeInfo"]["pageCount"])
                print("Add the book to the library? y or no. ")
                ch = input()
                if (ch == 'y'):
                    us = input("Enter username: ")
                    passs = input("Enter password: ")
                    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
                    cursor = conn.cursor()
                    title = obj["items"][0]["volumeInfo"]["title"]
                    autho = obj["items"][0]["volumeInfo"]["authors"]
                    author = ",".join(autho)
                    rat = obj["items"][0]['volumeInfo']['averageRating']
                    pub_date = obj['items'][0]["volumeInfo"]["publishedDate"]
                    pages = obj['items'][0]["volumeInfo"]["pageCount"]
                    cmd = 'INSERT INTO book_data(Title,Author,Rating,Page_Count) VALUES ( "' + title + '","' + author + '","' + str(
                        rat) + '",' + str(pages) + ');'
                    cursor.execute(cmd)
                    conn.commit()
                    conn.close()
                    print('\n\nNew Book added successfully')
                    wait = input('\nPress any key to continue....')
                if (ch == 'n'):
                    wait = input('\nPress any key to continue....')
            elif (choice == 3):
                base_api_link = "https://www.googleapis.com/books/v1/volumes?q=inauthor:"
                auth = input("Enter Author Name: ").strip()
                with urllib.request.urlopen(base_api_link + auth) as f:
                    text = f.read()
                decode = text.decode("utf-8")
                obj = json.loads(decode)
                print("\nTitle:", obj["items"][0]["volumeInfo"]["title"])
                aut = obj["items"][0]["volumeInfo"]["authors"]
                print("\nAuthor(s):")
                print(",".join(aut))
                # print("\nDescription: ", obj["items"][0]['volumeInfo']['description'])
                print("\nPublished Date:")
                print(obj['items'][0]["volumeInfo"]["publishedDate"])
                print("\nRating: ")
                print(obj["items"][0]['volumeInfo']['averageRating'])
                print("\nPage Count:")
                print(obj['items'][0]["volumeInfo"]["pageCount"])
                print("Add the book to the library? y or no. ")
                ch = input()
                if (ch == 'y'):
                    us = input("Enter username: ")
                    passs = input("Enter password: ")
                    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
                    cursor = conn.cursor()
                    title = obj["items"][0]["volumeInfo"]["title"]
                    autho = obj["items"][0]["volumeInfo"]["authors"]
                    author = ",".join(autho)
                    rat = obj["items"][0]['volumeInfo']['averageRating']
                    pub_date = obj['items'][0]["volumeInfo"]["publishedDate"]
                    pages = obj['items'][0]["volumeInfo"]["pageCount"]
                    cmd = 'INSERT INTO book_data(Title,Author,Rating,Page_Count) VALUES ( "' + title + '","' + author + '","' + str(
                        rat) + '",' + str(pages) + ');'
                    cursor.execute(cmd)
                    conn.commit()
                    conn.close()
                    print('\n\nNew Book added successfully')
                    wait = input('\nPress any key to continue....')
                if (ch == 'n'):
                    wait = input('\nPress any key to continue....')
                elif (choice == 0):
                    print("Press any key to continue.")
                    break

#Add book manually

def add_book():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    title = input('Enter Book Title :')
    author = input('Enter Book Author : ')
    desc = input("Enter description : ")
    pages = input('Enter Book Pages : ')
    pub_date = input("Enter date : ")
    cmd = 'INSERT INTO book_data(Title,Author,Description,Page_Count,Published_Date) VALUES ( "' + title + '","' + author+'","'+desc+'",'+str(pages)+',"'+pub_date+'");'
    cursor.execute(cmd)
    conn.commit()
    conn.close()
    print('\n\nNew Book added successfully')
    wait = input('\nPress any key to continue....')

#Fine

def fine():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs)
    cursor = conn.cursor()
    cmd ='SELECT SUM(fine) FROM trans WHERE dare_r ="'+str(date.today())+'";'
    cursor.execute(cmd)
    result = cursor.fetchone()
    print('\n\n               F I N E   C O L L E C T I O N \n')
    print('Total fine collected Today :',result[0])
    print('\n')
    conn.commit()
    conn.close()
    wait = input('\nPress any key to continue.....')
#fine()
#Fine collected per student
"""
def finee():
    us  = input("Enter username: ")
    passs = input("Enter password: ")
    conn = mysql.connector.connect(host='localhost', database='users', user=us, password=passs, port=3306)
    cursor = conn.cursor()
    #print("\n\n         F I N E  C O L L E C T E D  P E R   S T U D E N T \n")
    cmd = 'SELECT * FROM trans'
    cursor.execute(cmd)
    rec = cursor.fetchall()
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.set_xlabel("Students ID")
    axes.set_ylabel("Fine")
    axes.set_title("F I N E  C O L L E C T E D  P E R   S T U D E N T")
    for i in rec:
        l = list(i)
        #print(l[1],",",l[-1])
        axes.bar(l[2],l[-1])
    conn.commit()
    conn.close()
finee()
"""
#Admin menu
def emp():
    while True:
        print("\n\nH E L L O , A D M I N")
        print("\t")
        print("M E N U: ")
        print("1. Display all students")
        print("2. Add a new student")
        print("3. Search for the details of a particular student")
        print("4. Update information about a particular student")
        print("5. Delete a particular Student")
        print("6. Search and Add a book to the library")
        print("7. Add a book manually")
        print("8. Issue a book to student")
        print("9. Fine")
        print("10. Exit")
        c = int(input("Choice: "))
        if c==1:
            students()
        if c==2:
            add_stu()
        if c==3:
            search_stu()
        if c==4:
            upd_stu()
        if c == 5:
            delete_stu()
        if c == 6:
            addboook()
        if c == 7:
            add_book()
        if c == 8:
            issue()
        if c == 9:
            fine()
        if c == 10:
            finee()
        if c == 11:
            print("Exiting...")
            print("Exited.")
            main_m()
            break

#Student menu
def stuu():
    while True:
        print("\n\n")
        print("H E L L O , S T U D E N T")
        print("\n\nM E N U")
        print("1. Search and Add a book to the library")
        print("2. Add a book to the library manually")
        print("3. Return a book")
        print("4. Exit.")
        choice = int(input("Choice: "))
        if(choice==1):
            addboook()
        if (choice==2):
            add_book()
        if (choice==3):
            return_book()
        if (choice==4):
            print("Exiting...")
            print("Exited.")
            main_m()
            break


def main_m():
    print("W E L C O M E  T O   L M S: ")
    print("-"*20)
    print("Enter your login choice for: ")
    print ("1. ADMIN")
    print ("2. STUDENT")
    print("3. EXIT")
    #try:
    choice = int(input("Choose: "))
    if (choice==1):
        while True:
            p = getpass.getpass('E N T E R  P A S S W O R D')
            if p=='z4+vCZ':
                print ("\n\nAdmin Login Successful.\n\n")
                emp()
                break
            else:
                print("W R O N G   P  A S S W O R D. T R Y  A G A I N.")
    if (choice==2):
        print("Student Login Successful.")
        stuu()
    if (choice==3):
        wait = input("Press any key to exit.")
    else:
        print("Invalid choice. Please choose correct login info.")
        main_m()
main_m()
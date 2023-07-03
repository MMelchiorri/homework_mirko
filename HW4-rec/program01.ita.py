#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uno dei meccanismi utilizzati per conservare e gestire grandi
quantità di dati è costituito dai database. Esistono tantissimi
tipi di database, ma quello che ha rivoluzionato il settore è
costituito dai database organizzati secondo il modello relazionale
teorizzato da Codd ormai mezzo secolo fa. Secondo questo modello
i dati sono organizzati in tabelle e relazioni fra di esse, in
modo da ottimizzare le richieste di memoria, favorire la coerenza
dei dati e minimizzare gli errori.

Dobbiamo progettare un insieme di funzioni che implementi una
semplice forma di database relazionale di una scuola di formazione
in cui ci sono quattro tabelle, ovvero students, teachers, courses
ed exams. I database sono di tre diverse dimensioni, ovvero small,
medium e large. Le tabelle del database di dimensione dbsize sono
salvate in quattro file json <dbsize>_<nometabella>.json (ad esempio,
il db small è composto dai file small_students.json, small_teachers.json,
small_courses.json e small_exams.json). Le tabelle sono organizzate in
liste di dizionari (si veda ad esempio small_students.json) e hanno le
seguenti strutture:
    - students: chiavi stud_code, stud_name, stud_surname, stud_email
    - teachers: chiavi teach_code, teach_name, teach_surname, teach_email
    - courses: chiavi course_code, course_name, teach_code
    - exams: chiavi exam_code, course_code, stud_code, date, grade.
La relazione fra le tabelle implica che ogni riga in ognuna delle
tabelle ha un riferimento ad un'altra tabella: ad esempio, un esame
(exam_code) corrisponde ad un voto (grade) dato da un docente
(teach_code) ad uno studente (stud_code) per aver sostanuto
l'esame di un certo corso (course_code) in una certa data (date). Ogni
studente può aver sostenuto diversi esami. Ogno docente può tenere
diversi corsi. Ogni corso è tenuto da un solo docente.

Il campo stud_code è una chiave primaria per la tabella students poiché
identifica univocamente uno studente, ovvero non esistono due studenti
con lo stesso stud_code. Similmente, teach_code, course_code ed exam_code
sono le chiavi primarie rispettivamente delle tabelle teachers, courses ed
exams. Per questo motivo, tali campi vengono utilizzati per realizzare
la relazione fra le tabelle.

Inoltre, i campi in tutte le tabelle non sono mai vuoti.

Dobbiamo realizzare alcune funzioni per poter interrogare i database delle
diverse dimensioni. Quindi, le funzioni prevedono di usare sempre il
parametro dbsize di tipo stringa, che può assumere i valori 'small',
'medium' e 'large'. Le funzioni sono:
    - media_studente(stud_code, dbsize), che riceve una stud_code di
      uno studente e ritorna la media dei voti degli esami sostenuti,
      dallo studente.
    - media_corso(course_code, dbsize), che riceve un identificatore per un
      corso e ritorna la media dei voti degli esami per quel corso,
      sostenuti da tutti gli studenti.
    - media_docente(teach_code, dbsize), che riceve un identificatore
      di un docente e ritorna la media dei voti per gli esami
      sostenuti in tutti i corsi del docente.
    - studenti_brillanti(dbisze), che ritorna la lista delle matricole
      (stud_code) con una media di esami sostenuti superiore o uguale a 28,
      ordinate in modo decrescente per media e, in caso di parità, in
      ordine lessicografico per il cognome e il nome dello studente. In
      caso di ulteriore parità, si usi il valore numerico dello stud_code
      in ordine crescente.
    - stampa_esami_sostenuti(stud_code, fileout, dbsize), che riceve un
      numero di stud_code e salva nel file fileout la lista degli esami
      sostenuti dallo studente identificato dal valore stud_code.
      Le righe nel file devono essere ordinate in modo crescente
      per data di esame sostenuto e, in caso di stessa data, in ordine
      alfabetico. Il file ha una riga iniziale con il testo
       "Esami sostenuti dallo studente  <stud_surname> <stud_name>, matricola <stud_code>",
      mentre le righe seguenti hanno la seguente struttura
        "<course_name>\t<date>\t<grade>", in cui i campi sono allineati
      rispetto al nome del corso più lungo (ovvero tutte le date e
      i voti sono allineati verticalmente). La funzione ritorna
      il numero di esami sostenuti dallo studente.
    - stampa_studenti_brillanti(fileout, dbsize), che salva nel file
      fileout una riga per ogni studente con una media di esami
      sostenuti superiore o uguale a 28. Le righe nel file
      devono essere ordinate in modo decrescente per media e,
      in caso di parità, in ordine lessicografico per il
      cognome e il nome dello studente.
      Le righe nel file hanno la seguente struttura:
          "<stud_surname> <stud_name>\t<media>", in cui il valore media
      è allineato verticalmente per tutte le righe. La funzione
      ritorna il numero di righe salvate nel file.
    - stampa_verbale(exam_code, fileout, dbsize), che riceve un identificatore
      di esame e salva nel fileout le informazioni relative
      all'esame indicato, usando la seguente formula
        "Lo studente <stud_surname> <stud_name>, matricola <stud_code>, ha sostenuto in data <date> l'esame di <course_name> con il docente <teach_surname> <teach_name> con votazione <grade>."
      La funzione ritorna il voto dell'esame associato
      all'identificatore ricevuto in input.

Tutte le medie devono essere arrotondate alla seconda cifra decimale,
anche prima di ogni funzione di ordinamento.
Tutti i file devono avere encoding "utf8".
Per stampare agevolmente righe allineate considerare la funzione format con
i modificatori per l'allineamento (https://pyformat.info/#string_pad_align)
e con i parametri dinamici (https://pyformat.info/#param_align).
"""
import json

def media_studente(stud_code, dbsize):
    sum_of_votes=0
    sum_of_exam=0
    match dbsize:
        case 'small':
           
            with open('./small_exams.json') as file_exam:
                data_exams = json.load(file_exam)        
            for i in range(len(data_exams)):
                if stud_code==data_exams[i]['stud_code']:
                    sum_of_votes += data_exams[i]['grade']
                    sum_of_exam += 1
            return round((sum_of_votes/sum_of_exam),2)
            
        case 'medium':
              with open('./medium_exams.json') as file_exam:
                data_exams = json.load(file_exam)
              for i in range(len(data_exams)):
                if stud_code==data_exams[i]['stud_code']:
                    sum_of_votes += data_exams[i]['grade']
                    sum_of_exam += 1
              return round((sum_of_votes/sum_of_exam),2)
        case 'large':
          
            with open('./large_exams.json') as file_exam:
                data_exams = json.load(file_exam) 
            for i in range(len(data_exams)):
              if stud_code == data_exams[i]['stud_code']:
                sum_of_votes += data_exams[i]['grade']
                sum_of_exam += 1
            return round((sum_of_votes/sum_of_exam),2)

    pass

def media_corso(course_code, dbsize):
    sum_of_votes=0
    sum_of_exam=0
    match dbsize:
        case 'small':
          with open('./small_exams.json') as file_exam:
              data_exam = json.load(file_exam)
          with open('./small_students.json') as file_students:
              data_student = json.load(file_students)
          for i in range(len(data_student)):
              for j in range(len(data_exam)):
                  if data_exam[j]['stud_code'] == data_student[i]['stud_code'] and data_exam[j]['course_code']==course_code:
                      sum_of_votes += data_exam[j]['grade']
                      sum_of_exam +=1
          if sum_of_exam==0:
             print("Course not existed or no one does this exam")
             return
                        
          return round((sum_of_votes/sum_of_exam),2)      
        case 'medium':
              with open('./medium_exams.json') as file_exam:
                data_exam = json.load(file_exam)
              with open('./medium_students.json') as file_students:
                data_student = json.load(file_students)
              for i in range(len(data_student)):
                for j in range(len(data_exam)):
                  if data_exam[j]['stud_code'] == data_student[i]['stud_code'] and data_exam[j]['course_code']==course_code:
                      sum_of_votes += data_exam[j]['grade']
                      sum_of_exam +=1
              if sum_of_votes==0:
                 print("I'm in medium and this course not existed or no one does this exam")
                 return
              return round((sum_of_votes/sum_of_exam),2)   
        case 'large':
              with open('./large_exams.json') as file_exam:
                data_exam = json.load(file_exam)
              with open('./large_students.json') as file_students:
                data_student = json.load(file_students)
              for i in range(len(data_student)):
                for j in range(len(data_exam)):
                  if data_exam[j]['stud_code'] == data_student[i]['stud_code'] and data_exam[j]['course_code']==course_code:
                      sum_of_votes += data_exam[j]['grade']
                      sum_of_exam +=1
              if(sum_of_exam==0):
                 print("I'm in large and this course not existed or no one does this exam")
                 return
              return round((sum_of_votes/sum_of_exam),2)          
    pass

def media_docente(teach_code, dbsize):
    sum_of_votes=0
    sum_of_exam=0
    match dbsize:
       case 'small':
          with open('./small_courses.json') as file_courses:
             data_courses = json.load(file_courses)
          with open('./small_exams.json') as file_exams:
             data_exams = json.load(file_exams)
          for i in range(len(data_courses)):
             if teach_code==data_courses[i]['teach_code']:
                for j in range(len(data_exams)):
                   if data_courses[i]['course_code']==data_exams[j]['course_code']:
                      sum_of_votes+= data_exams[j]['grade']
                      sum_of_exam +=1
                if sum_of_exam==0:
                   print("No exam has been sustaneid from student or this professor not exist")
          return round((sum_of_votes/sum_of_exam),2) 
       case 'medium':
        with open('./medium_courses.json') as file_courses:
             data_courses = json.load(file_courses)
        with open('./medium_exams.json') as file_exams:
             data_exams = json.load(file_exams)
        for i in range(len(data_courses)):
          if teach_code==data_courses[i]['teach_code']:
                print(data_courses[i]['course_code'])
                for j in range(len(data_exams)):
                   if data_courses[i]['course_code']==data_exams[j]['course_code']:
                      sum_of_votes+= data_exams[j]['grade']
                      sum_of_exam +=1
                if sum_of_exam==0:
                   print("No exam has been sustaneid from student or this professor not exist")
        return round((sum_of_votes/sum_of_exam),2) 
       case 'large':
        with open('./large_courses.json') as file_courses:
             data_courses = json.load(file_courses)
        with open('./large_exams.json') as file_exams:
             data_exams = json.load(file_exams)
        for i in range(len(data_courses)):
          if teach_code==data_courses[i]['teach_code']:
                for j in range(len(data_exams)):
                   if data_courses[i]['course_code']==data_exams[j]['course_code']:
                      sum_of_votes+= data_exams[j]['grade']
                      sum_of_exam +=1
                if sum_of_exam==0:
                   print("No exam has been sustaneid from student or this professor not exist")
        return round((sum_of_votes/sum_of_exam),2) 
           


    pass

def studenti_brillanti(dbsize):
    index_student =0
    with open('./small_students.json') as file_students:
      data_student = json.load(file_students)
      list_student = [None] * len(data_student)
      for i in range(len(data_student)):
        value = media_studente(data_student[i]['stud_code'],dbsize)
        if(value >=28):
          obj_student  = {'stud_code':data_student[i]['stud_code'],'avg_score':value,'stud_name':data_student[i]['stud_name'],'stud_surname':data_student[i]['stud_surname']}
          list_student[index_student]= obj_student
          index_student +=1
    list_student = list_student[:index_student]
    for i in range(0,len(list_student)):
       for j in range(i+1,len(list_student)):
          if(list_student[i]['avg_score']<list_student[j]['avg_score']):
             temp = list_student[i]['avg_score']
             list_student[i]['avg_score']=list_student[j]['avg_score']
             list_student[j]['avg_score']=temp

       
    print(list_student)
    pass

def stampa_verbale(exam_code, dbsize, fileout):
    pass

def stampa_esami_sostenuti(stud_code, dbsize, fileout):
    pass

def stampa_studenti_brillanti(dbsize, fileout):
    pass


# media studente
'''
small_value = media_studente('1803891','small')

medium_value = media_studente('1512987','medium')

large_value = media_studente('1654889','large')

print('small media studente ',small_value)

print('medium media studente',medium_value)

print('large media studente', large_value)'''

# media corso

'''

small_value = media_corso('EDIELFAC0x5203a7','small')

medium_value = media_corso('TDC0x4003e','medium')

large_value = media_corso('IDMESAM0xb22d4c','large')

print('small media corso ',small_value)

print('medium media corso ',medium_value)

print('large media corso ',large_value)

'''

# media docente

'''

small_value_media_docente = media_docente('003',"small")

print('small media docente', small_value_media_docente)

medium_value_media_docente = media_docente('0010',"medium")

print('medium media docente', medium_value_media_docente)

large_value_media_docente = media_docente('00015',"large")

print('large media docente', large_value_media_docente)

'''

# studenti brillanti

studenti_brillanti("small")
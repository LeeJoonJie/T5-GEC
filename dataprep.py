import pandas as pd 
import csv 

def connl_csv(csv_path, x, y):
    with open(csv_path, 'w', newline='') as csvfile:
        writter = csv.writer(csvfile)
        writter.writerow(["input", "target"])
        for idx in range(len(x)):
          input_text = "grammar: " + x[idx].rstrip("\n")
          correction = y[idx].rstrip("\n")
          if input_text and correction:
              writter.writerow([input_text, correction])

def clang_csv(csv_path, lines):

    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in lines:
            row = row.split('\t')
            input_text = "grammar: " + row[0].rstrip("\n")
            correction = row[1].rstrip("\n")
            if input_text and correction:
                writer.writerow([input_text, correction])
 

def dataprep():
    x_train_file = open("x_train.txt", "r")
    y_train_file = open("y_train.txt", "r")

    x_train = x_train_file.readlines()
    y_train = y_train_file.readlines()

    clang = open('clang8_source_target_en.spacy_tokenized.tsv')
    clang_lines = clang.readlines()[:400000]

    connl_csv("train.csv", x_train, y_train)
    clang_csv("train.csv", clang_lines)


dataprep()



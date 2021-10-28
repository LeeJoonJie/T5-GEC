from happytransformer import HappyTextToText, TTSettings, TTTrainArgs
import csv

def generate_csv(csv_path, x, y):
    with open(csv_path, 'w', newline='') as csvfile:
        writter = csv.writer(csvfile)
        writter.writerow(["input", "target"])
        for idx in range(len(x)):
          input_text = "grammar: " + x[idx].rstrip("\n")
          correction = y[idx].rstrip("\n")
          if input_text and correction:
              writter.writerow([input_text, correction])

def dataprep():
    x_train_file = open("x_train.txt", "r")
    x_test_file = open("x_test.txt", "r")
    y_train_file = open("y_train.txt", "r")
    y_test_file = open("y_test.txt", "r")

    x_train = x_train_file.readlines()
    x_test = x_test_file.readlines()
    y_train = y_train_file.readlines()
    y_test = y_test_file.readlines()

    generate_csv("train.csv", x_train, y_train)
    generate_csv("test.csv", x_test, y_test)

def train():
    happy_tt = HappyTextToText("T5", "t5-base")
    args = TTTrainArgs(batch_size=32)
    happy_tt.train("train.csv", args=args)
    happy_tt.save("model/")

    #beam_settings =  TTSettings(num_beams=5, min_length=1, max_length=50)


if __name__ == "__main__":
    dataprep()
    train()

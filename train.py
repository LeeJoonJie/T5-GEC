from happytransformer import HappyTextToText, TTTrainArgs
import csv


def train():
    happy_tt = HappyTextToText("T5", "t5-base")
    args = TTTrainArgs(batch_size=2, num_train_epochs=2)
    happy_tt.train("train.csv", args=args)
    happy_tt.save("model/")


if __name__ == "__main__":
    train()

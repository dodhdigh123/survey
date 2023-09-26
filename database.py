import pandas as pd

def save(congestion, gender, question, add):
    idx = len(pd.read_csv("./database.csv"))
    new_df = pd.DataFrame({"congestion":congestion,
                           "gender":gender,
                           "question":question,
                            "add":add}, 
                         index = [idx])
    new_df.to_csv("./database.csv",mode = "a", header = False)
    return None

def load_list():
    survey_list = []
    df = pd.read_csv("./database.csv")
    for i in range(len(df)):
        survey_list.append(df.iloc[i].tolist())
    return survey_list

def now_index():
    df = pd.read_csv("./database.csv")
    return len(df)-1


def load_survey(idx):
    df = pd.read_csv("./database.csv")
    survey_info = df.iloc[idx]
    return survey_info


if __name__ =="__main__":
    load_list()

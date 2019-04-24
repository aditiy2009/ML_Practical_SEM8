import pydotplus
import pandas as pd
from sklearn.externals.six import StringIO
from sklearn.tree import DecisionTreeClassifier
from  sklearn.tree import export_graphviz
from sklearn.metrics import confusion_matrix
from  sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def load_dataset():
    path="lipstick.csv"
    df=pd.read_csv(path,usecols=['AGE','INCOME','GENDER','MS','BUYS'])
    return df

def labelEncoder(df):
    for columns in df.columns:
        if df[columns].dtype==type(object):
            le=preprocessing.LabelEncoder()
            df[columns]=le.fit_transform(df[columns])
            print(le.classes_)
    return df
def split_data(df):
    X=df.values[:,0:4]
    Y=df.values[:,-1]
    return train_test_split(X,Y,test_size=0.2,random_state=42)
def create_model(Xtrain,Ytrain,gini):
    if gini=="True":
        clf=DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3,min_samples_leaf=5)
        clf.fit(Xtrain,Ytrain)
    else:
        clf=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)
        clf.fit(Xtrain,Ytrain)
    return clf
def predict(clf,Xtest):
    return clf.predict(Xtest)

def modelEvaluation(Ytest,Ypredict):
    print("test data : ",Ytest)
    print("predict data : ",Ypredict)
    print("accuracy of model : ",accuracy_score(Ytest,Ypredict)*100)
    print("report is : ",classification_report(Ytest,Ypredict))
    print("confusion matrix : ",confusion_matrix(Ytest,Ypredict))

def visualizeTree(clf):

    dot_point=StringIO()
    export_graphviz(clf,out_file=dot_point,precision=2,rounded='True',filled='True',proportion='False',
                    feature_names=['AGE','INCOME','GENDER','MS'],class_names=['YES',"NO"])
    graph=pydotplus.graph_from_dot_data(dot_point.getvalue())
    graph.write_png('newtree.png')

def main():
    df=load_dataset()
    df=labelEncoder(df)

    Xtrain,Xtest,Ytrain,Ytest=split_data(df)
    clf=create_model(Xtrain,Ytrain,gini="True")
    Ypredict=predict(clf,Xtest)
    modelEvaluation(Ytest,Ypredict)
    y=[['<21','low','female','married']]
    y=pd.DataFrame(data=y)
    y=labelEncoder(y)
    print(predict(clf,y))
    visualizeTree(clf)
main()

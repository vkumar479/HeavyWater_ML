# HeavyWater Machine Learning Problem



### Problem Statement

Generally, the goal of this problem is to build a text classification model based on machine learning. Input is given as a csv file, which contains all documents that serve as our dataset to train and test our model. The document entry format is like this:

```
CANCELLATION NOTICE,641356219cbc f95d0bea231b ... [lots more words] ... 52102c70348d b32153b8b30c
```

So each document is composed of a label which indicates document type at its beginning, and a series of obscured OCR(Optical Character Recognition) data seperated by space and each of them maps to a unique word in original document.



### General Steps

In the given dataset as the label is being already provided we will focus on the supervised learning. 

1. Dataset Preprossing - Load our dataset and perform basic pre-processing. E.g. figure our our dataset's composition and split dataset into train and test sets.
2. Feature Selection - Transform raw dataset into flat features that can be used in our machine learning model.
3. Model Training - Train the model on labelled dataset.

#### Step 1: Dataset Preparation
 There're 62204 documents in total and their distribution is shown below:


Then we need to split our dataset for training and testing. The training part is used to train our model to make correct classification. And the testing part is used to validate the model's correctness. 


#### Step 2: Feature Selection

Our raw obscured text dataset cannot work directly with machine learning algorithms, which needs numeric data representation. So in this step we need to convert the text to numbers. 

A simple and effective model for thinking about text documents in machine learning is called the **Bag-of-Words** Model, or **BoW**. The model is simple in that it throws away all of the order information in the words and focuses on the occurrence of words in a document. The **sklearn** library provides 3 different schemes(Word Counts with **CountVectorizer**, Word Frequencies with **TfidfVectorizer** and Hashing with **HashingVectorizer**) that we can use to achieve this goal, they are introduced in the following link:


In our solution we will use **TfidfVectorizer** because it's a refined version of **CountVectorizer** and easier to implement than **HashingVectorizer**. Since the vectorizer requires the raw_documents to be str, unicode or file objects type, we will convert our dataframe into unicode before transforming the data. 

After we vectorize our data, let's print and check the numeric matrix.
```
  (0, 290693)	0.11966728067482815
  (0, 630669)	0.027930338102784877
  (0, 741273)	0.5053247463636006
  (0, 140159)	0.027446260919014562
  (0, 527647)	0.08764998192233651
  (0, 812021)	0.17521859465377745
  (0, 703628)	0.11798909834518305
  (0, 601896)	0.09424065432278207
  :	:
  (49762, 726701)	0.1252014592533339
  (49762, 691873)	0.12747884824803968
  (49762, 857232)	0.11654331817294304
  (49762, 665928)	0.13385960033372477
  (49762, 160794)	0.1302661471113159
  (49762, 769263)	0.1302661471113159
  (49762, 307783)	0.1302661471113159
  (49762, 134960)	0.12747884824803968
```
Now we are good to use this feature set to train our model.



#### Step 3: Model Training

Now it's time to build a model for our training. In this problem we choose the popular classification model - Logistic Regression, which both works on continuous data and discrete data. The document type is predicted by the refined frequency of each word.

Finally we achieved the accuracy of 84.73%, which is pretty good.



### Deploy Model

Deployed the Model on AWS Elastic Beanstalk as it automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, one can retain full control over the AWS resources powering the application and can access the underlying resources at any time.The general layout of my deployed project:
```
/heavywater
   ├── templates
   │   └── index.html
   │   └── result.html
   ├── static
   │   └── home.css
   │   └── result.css
   ├── venv/
   ├── requirements.txt
   ├── .gitignore
   ├── Ml_Model.pkl
   └── app.py
```

#### Preparation Step

**Flask** is a framework for small scale Python web development. We use flask as because it can bind with the HTML and can provide the experience for the browser. Two HTML files have been atached to the project one for the input and the other for the output part. To support these HTML pages 2 CSS templates have also been provided. 


AWS Link to test the classification Model
```
http://heavywater.us-east-2.elasticbeanstalk.com/
```

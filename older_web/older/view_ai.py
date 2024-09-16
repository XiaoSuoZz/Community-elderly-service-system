from matplotlib.font_manager import json_dump
import pandas as pd 
import json
from sklearn import preprocessing

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


import pandas as pd 
from sklearn import preprocessing


from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os


df = pd.read_csv(os.getcwd() + '/older/user.csv')
df = df[['is_marry', 'is_live_alone', 'is_disability', 'diseases_history', 'major_diseases_history', 'care_level']]

for col in ['diseases_history', 'major_diseases_history']:
    dplist = []
    for dfi in df[col]:
        # dfi = len(json.loads(dfi))
        dplist.append(len(json.loads(dfi)))
        # print(dfi)
    # enc=preprocessing.LabelEncoder()   #获取一个LabelEncoder
    # enc=enc.fit(df[col])  #训练LabelEncoder
    
    # df[col]=enc.transform(df[col])
    df[col]=dplist
    print(df[col])
#缺失值处理，直接删除有空字段的记录  nan
df = df.dropna()
#数据基本处理
#确定特征值，目标值
# 包外估计 约有36.8%数据取不到 无偏估计 所有样本出现概率一样大 辅助剪枝 将取不到用于测试等等，防止过拟合
traffic_feature = df.iloc[:, :5]
traffic_target = df.iloc[:, 5:6]
# 数据集划分
## 20%测试数据，80%训练数据
feature_train, feature_test, target_train, target_test = train_test_split(traffic_feature, traffic_target, test_size=0.2,random_state=0)
# clf = RandomForestClassifier(criterion='entropy')
#实例化随机森林，训练
clf = RandomForestClassifier()
clf.fit(feature_train,target_train)
#模型评估
predict_results=clf.predict(feature_test)
#print(accuracy_score(predict_results, target_test))

# 加载输入数据
# df = pd.read_csv('input.csv')  # 后续改成输入的csv名字
# # 输入csv 含这5个字段
# df1 = df[['is_marry', 'is_live_alone', 'is_disability', 'diseases_history', 'major_diseases_history']].sample(1)

# for col in ['diseases_history', 'major_diseases_history']:
#     enc=preprocessing.LabelEncoder()   #获取一个LabelEncoder
#     enc=enc.fit(df[col])  #训练LabelEncoder
#     df1[col]=enc.transform(df1[col])
    
# predict_results=clf.predict(df1)
#print('预测结果', predict_results)

def ai_level(is_marry, is_live_alone, is_disability, diseases_history, major_diseases_history):
    data_input = {}
    data_input['is_marry'] = is_marry
    data_input['is_live_alone'] = is_live_alone
    data_input['is_disability'] = is_disability
    data_input['diseases_history'] = diseases_history
    data_input['major_diseases_history'] = major_diseases_history
    data_input = pd.DataFrame(data_input, index=[0])
    predict_results=clf.predict(data_input)
    print('自动评级：', predict_results)
    return predict_results[0]

# level_str = ai_level('1', '1', '0', '2', '0')
# print(level_str)

import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV


# Đề bài: Xây dựng mô hình dự báo giá nhà trên/m2 của bài toán mua bán nhà mặt phố quận Đống Đa
# df = pd.read_csv('Case_study\RoadSurfaceHouseTrading.csv')
# df = df[df['ten_quan'] == 'Quận Đống Đa']
# df = df[df['do_rong_duong_ml'] == 'Mặt phố - Mặt đường']
# print(df)
# df.to_csv('file_sua2.csv')
# df1 = pd.read_csv('file_sua2.csv')
# # # df1 = df.where(pd.notnull(df), None)

# print(df.isnull().sum())
# # # print(df.isnull().sum())
# # df = df.where(pd.notnull(df), None)

#B1: Chọn feature đặc trưng: dien_tich, do_rong_duong, ten_duong, so_tang, mat_tien, so_do, (lat-long ???)
# target = df1[['mat_tien','so_tang','do_rong_duong','dien_tich','so_do','ten_duong', 'gia_m2']]

#B2: Lọc nhiễu
# Xóa các cột có giá trị Null: ten_duong
# df1 = df1[df1['ten_duong'].notna()]
# print(df1.isnull().sum())
# print(df.so_do)
# df1.so_do.replace({np.nan: None}, inplace=True)
# print(df1)
#  Chuyen du lieu category sang numerical
# def convert_category_to_id(value):
#     if value == None :
#         return 0
#     else:
#         return 1

# df1['so_do'] = df1.apply(lambda x:convert_category_to_id(x['so_do']),axis=1).reset_index(drop=True)
# print(df1.isnull().sum())
# print(df1)
# df1['ten_duong'] = df1['ten_duong'].astype('category').cat.codes # thay bang lat-long

# Loại bỏ outlier
def subset_by_iqr(df, column, whisker_width=1.5):
   
    # Calculate Q1, Q2 and IQR
    Q1 = df[column].quantile(0.25)                 
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    # print(Q1)
    # print(Q3)
    # print(IQR)
    # Apply filter with respect to IQR, including optional whiskers
    filter = (df[column] >= (Q1 - whisker_width*IQR)) & (df[column] <= (Q3 + whisker_width*IQR))
    return df.loc[filter]                                                     

# df1 = subset_by_iqr(df1, 'mat_tien', whisker_width=1.5)
# df1 = subset_by_iqr(df1, 'so_tang', whisker_width=1.5)
# df1 = subset_by_iqr(df1, 'do_rong_duong', whisker_width=1.5)
# df1 = subset_by_iqr(df1, 'dien_tich', whisker_width=1.5)
# df1 = subset_by_iqr(df1, 'gia_m2', whisker_width=1.5)
# print(df1)

# Thay các giá trị Null ở các cột bằng giá trị mean tương ứng với từng cột
# df1['mat_tien'] = df1['mat_tien'].fillna(int(df1['mat_tien'].mean()))
# df1['so_tang'] = df1['so_tang'].fillna(int(df1['so_tang'].mean()))
# df1['do_rong_duong'] = df1['do_rong_duong'].fillna(int(df1['do_rong_duong'].mean()))
# df1['dien_tich'] = df1['dien_tich'].fillna(int(df1['dien_tich'].mean()))
# df1['gia_m2'] = df1['gia_m2'].fillna(int(df1['gia_m2'].mean()))
# df1.to_csv('file_clear.csv')

#B3: normalizer data 
df2 = pd.read_csv('file_clear.csv')
df2 = df2[df2['lat'].notna()]
df2 = df2[df2['long'].notna()]

# print(df2.isnull().sum())
# print(df2)
df3 = df2[['mat_tien','so_tang','do_rong_duong','dien_tich','so_do','ten_duong','lat','long', 'gia_m2']]
# Khai báo đối tượng MinMaxScaler
scaler = MinMaxScaler()
# Chuẩn hóa dữ liệu trong df với StandardScaler
df_s = scaler.fit_transform(df3)
# lấy danh sáchc cột
col_names = list(df3.columns)
# chuyển về DataFrame, gán các cột của df cho dữ liệu đã được chuẩn hóa
df_s = pd.DataFrame(df_s, columns=col_names)
df_s.boxplot()
plt.show()

#B4: Chọn mô hình: Dessiontree

target = df2[['mat_tien','so_tang','do_rong_duong','dien_tich','so_do','ten_duong','lat','long', 'gia_m2']]
X, y = target[['mat_tien','so_tang','do_rong_duong','dien_tich','so_do','ten_duong','lat','long']], df2['gia_m2']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X_train, y_train)
pred = regressor.predict(X_test)
# print("MAPE: ",mean_absolute_percentage_error(y_test, pred))

#B5: finuntune hyperparameter
# Hyper parameters range intialization for tuning 
# parameters = {"splitter":["best","random"],
#             "max_depth" : [1,3,5,7],
#            "min_samples_leaf":[1,2,3,4,5,6,7,8,9,10],
#            "min_weight_fraction_leaf":[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9],
#            "max_features":["auto","log2","sqrt",None],
#            "max_leaf_nodes":[None,10,20,30,40,50,60,70,80,90] }
# tuning_model = GridSearchCV(regressor,param_grid=parameters,scoring='neg_mean_squared_error',cv=3,verbose=3)
# tuning_model.fit(X_train,y_train) 
# y_pred = tuning_model.best_estimator_.predict(X_test)
# print('MPE: ', mean_absolute_percentage_error(y_test,pred))














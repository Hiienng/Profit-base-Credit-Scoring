import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(r'C:\Users\hiennpd3\OneDrive - VPBank\AA Team\Mô hình Scorecard\hien-main\01. data\input\final_input.csv')

######################################################
### Bước 1: Chuẩn bị dữ liệu và đổi tên các cột
######################################################
# Chuyển đổi các cột cần thiết sang kiểu số (nếu cần)
data['OutDay'] = pd.to_datetime(data['OutDay'])
data['InDay'] = pd.to_datetime(data['InDay'])
data['Month'] = data['Month'].astype(str)

# Mã hóa các biến phân loại (nếu cần)
data = pd.get_dummies(data, columns=['product_group', 'bi_card_type', 'campaign_group', 'income_tier', 'gender', 'marital_status', 'edu_level', 'province_city', 'cus_class', 'revolver_group'])

# Đổi tên các cột để không chứa các ký tự đặc biệt
data.columns = [col.replace('[', '').replace(']', '').replace('<', '').replace('>', '').replace(' ', '_') for col in data.columns]

# Chọn các cột đầu vào (X) và đầu ra (y)
X = data[0:27]
y = data['nii_24m']

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Chuẩn hóa dữ liệu (nếu cần)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


############################################################
##Bước 2: Huấn luyện mô hình
############################################################
# Huấn luyện mô hình Random Forest
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

# Huấn luyện mô hình XGBoost
xgb = XGBRegressor(objective='reg:squarederror')
xgb.fit(X_train, y_train)
xgb_preds = xgb.predict(X_test)

##############################################################
###Bước 3: Đánh giá mô hình
############################################################
# Tính toán các số liệu đánh giá cho Random Forest
rf_mae = mean_absolute_error(y_test, rf_preds)
rf_mse = mean_squared_error(y_test, rf_preds)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_preds)

# Tính toán các số liệu đánh giá cho XGBoost
xgb_mae = mean_absolute_error(y_test, xgb_preds)
xgb_mse = mean_squared_error(y_test, xgb_preds)
xgb_rmse = np.sqrt(xgb_mse)
xgb_r2 = r2_score(y_test, xgb_preds)

# In ra các số liệu đánh giá
print("Random Forest:")
print(f"MAE: {rf_mae:.2f}")
print(f"MSE: {rf_mse:.2f}")
print(f"RMSE: {rf_rmse:.2f}")
print(f"R^2: {rf_r2:.2f}")

print("\nXGBoost:")
print(f"MAE: {xgb_mae:.2f}")
print(f"MSE: {xgb_mse:.2f}")
print(f"RMSE: {xgb_rmse:.2f}")
print(f"R^2: {xgb_r2:.2f}")
